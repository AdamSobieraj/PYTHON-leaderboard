"""
markitdown_pdf_parser.py

PDF -> Markdown parser based on MarkItDown (Microsoft) + PyMuPDF, extended with
the same "stitched contracts" handling used by the other parsers in this
project (Marker-based, PyMuPDF4LLM-based):

  - header/footer removal (auto repeated-block detection, or fixed margins)
  - per-page classification: text | scan | drawing | blank
  - blank pages mark boundaries between stitched sub-documents (section_index)
  - OCR (via PyMuPDF's native Tesseract integration) for BOTH scanned pages
    AND vector-only "drawing" pages (e.g. store layout plans with labels
    drawn as vector shapes rather than selectable text or raster images)
  - OCR / fallback-text noise filtering

KNOWN ARCHITECTURAL LIMITATION (read before using on table-heavy documents):
MarkItDown has no native per-page chunking API for PDFs (unlike pymupdf4llm's
page_chunks=True). To produce one Document per page - required for
section_index / blank-page boundary detection - each page is physically cut
into an isolated single-page PDF before being handed to MarkItDown. This means
MarkItDown NEVER sees two pages at once, so a table that spans two pages WILL
be split into two incomplete fragments; MarkItDown has no way to recognize or
reconstruct the continuation. This is an inherent limitation of driving
MarkItDown page-by-page, not a fixable bug. Pages where this is likely to
matter are flagged via metadata["table_may_be_split_across_pages"]. If your
documents are table-heavy and multi-page tables are common, prefer the
PyMuPDF4LLM or Docling/Marker-based parsers instead, which process the whole
document at once and preserve cross-page table structure.

Requirements:
    pip install pymupdf markitdown langchain-core
    # OCR requires the Tesseract binary + language pack installed on the
    # system (e.g. apt-get install tesseract-ocr tesseract-ocr-pol), and,
    # if not in the default location, the TESSDATA_PREFIX env variable.
"""

import io
import logging
import math
import os
import re
import tempfile
import threading
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

import pymupdf  # PyMuPDF - page analysis, page splitting, header/footer redaction, OCR
from langchain_core.documents import Document
from markitdown import MarkItDown

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# ======================================================================
# SETTINGS
# ======================================================================

# Master switch: remove headers and footers before extraction?
REMOVE_HEADERS_FOOTERS = True

# How to find headers / footers (used only if REMOVE_HEADERS_FOOTERS is True):
#   "auto"  - removes only text blocks in the top/bottom zone that REPEAT across
#             pages (page numbers, running titles). Safe for mixed documents.
#             Works only on pages with a text layer.
#   "fixed" - removes fixed margins (below) from every page, including scans.
#             Risky for mixed documents (may delete real content near the edge).
HEADER_FOOTER_MODE = "auto"

# --- "fixed" mode ---
FIXED_TOP_MARGIN_PT = 50          # 1 pt = 1/72 inch
FIXED_BOTTOM_MARGIN_PT = 60
FIXED_MIN_CONTENT_HEIGHT_PT = 50  # pages shorter than margins + this are left untouched

# --- "auto" mode ---
AUTO_HEADER_ZONE_RATIO = 0.10
AUTO_FOOTER_ZONE_RATIO = 0.10
AUTO_MIN_REPEAT_PAGES = 3
AUTO_MIN_REPEAT_RATIO = 0.30
AUTO_MAX_BLOCK_CHARS = 200
# KNOWN LIMITATION (shared with the other two parsers in this project): the
# repetition threshold is computed GLOBALLY across the whole stitched file.
# A contract template appearing only once or twice will not be recognized as
# repeating and its header/footer will not be removed. Documented, not fixed
# here - see the equivalent comment in the Marker/PyMuPDF4LLM parsers for why.

# --- Page classification ---
MIN_TEXT_CHARS = 20               # fewer characters in the text layer = "no real text"
BLANK_INK_RATIO = 0.001           # share of "ink" pixels below which a page is blank
INK_DELTA = 50                    # pixel is "ink" if darker than background by this much
CLASSIFY_MAX_PX = 800             # longer side of the low-res render used for classification

# --- OCR ---
MIN_OCR_LETTERS = 10
MIN_OCR_LETTER_RATIO = 0.4        # letters / non-space characters

# --- Pages without extractable text (plans, drawings, photos, stamps) ---
INCLUDE_NON_TEXT_PAGES = True
NON_TEXT_PLACEHOLDER = "[Strona bez tekstu: rysunek, plan lub obraz]"


@dataclass
class PageInfo:
    """Result of the page analysis (1-based page number)."""
    number: int
    kind: str            # 'text' | 'scan' | 'drawing' | 'blank'
    section_index: int   # index of the stitched document (blank pages = boundaries)
    plain_text: str      # text layer from PyMuPDF (fallback)


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on MarkItDown (Microsoft) + PyMuPDF, extended to handle
    "stitched" contracts: many documents in one file (contracts, energy
    certificates, plans, Excel printouts), separated by blank pages.

    Steps:
    1. Optionally remove headers / footers (see REMOVE_HEADERS_FOOTERS),
       applied once to the whole document via redaction before any splitting.
    2. Classify every page: text | scan | drawing | blank (same classifier as
       the other parsers in this project, for consistent metadata).
    3. For 'text' pages: cut the single page into an isolated one-page PDF and
       convert it via MarkItDown (see the module docstring for the resulting
       cross-page-table limitation).
    4. For 'scan' AND 'drawing' pages: run PyMuPDF's native Tesseract OCR
       (full-page render-and-OCR), regardless of whether the page contains a
       raster image - this is what lets vector-only content (e.g. store
       layout plans with vector-drawn labels) be recovered via OCR instead of
       being silently dropped.
    5. Build one Document per page:
       - text    -> MarkItDown output (fallback: PyMuPDF text layer),
       - scan    -> OCR output, noise-filtered,
       - drawing -> OCR output if it passes the noise filter, otherwise a
                    placeholder,
       - blank   -> skipped; blank pages also mark a boundary between
                    documents (metadata["section_index"]).

    OCR requires Tesseract with the language pack (e.g. 'pol') and, if it is
    not in the default location, the TESSDATA_PREFIX environment variable.
    """

    # FIX (#11): MarkItDown's thread-safety for concurrent .convert() calls on
    # a shared instance is not documented/verified. Serializing calls is a
    # cheap, defensive precaution, mirroring the _convert_lock used in the
    # Marker-based parser for a library with a similar lack of guarantees.
    _convert_lock = threading.Lock()

    def __init__(
        self,
        ocr_language: str = "pol+eng",
        ocr_dpi: int = 300,
        enable_ocr: bool = True,
    ):
        """
        Args:
            ocr_language: Tesseract language code(s), e.g. "pol" or "pol+eng".
            ocr_dpi:      Resolution used for OCR rendering.
            enable_ocr:   Whether to attempt OCR on scan/drawing pages at all.
        """
        # llm_client=None means a purely local mode, no API calls
        self._converter = MarkItDown(llm_client=None, llm_model=None)
        self._ocr_language = ocr_language
        self._ocr_dpi = ocr_dpi
        self._enable_ocr = enable_ocr

        if REMOVE_HEADERS_FOOTERS:
            logger.info(f"Header/footer removal: ON (mode={HEADER_FOOTER_MODE})")
        else:
            logger.info("Header/footer removal: OFF")

        logger.info(
            f"MarkItDown parser ready | ocr={enable_ocr} ({ocr_language}, {ocr_dpi} dpi)"
        )

    # ══════════════════════════════════════════════════════════════
    # PUBLIC INTERFACE
    # ══════════════════════════════════════════════════════════════

    def parse(
        self,
        file_source: Union[str, io.BytesIO, bytes],
        **kwargs,
    ) -> List[Document]:
        """
        Processes a PDF -> list of Documents (one Document per non-blank page).

        Kwargs:
            full_document (bool): Whole document as a single Document, via one
                                   MarkItDown call on the whole (redacted)
                                   file. Preserves cross-page table structure
                                   (see module docstring), but does NOT get
                                   per-page classification / section_index.
                                   Default False.
        """
        full_document = kwargs.get("full_document", False)
        source_name = self._get_source_name(file_source)
        pdf_doc = None

        try:
            pdf_doc = self._open_pdf(file_source)

            # ── 1. Header/footer removal (once, on the whole document) ───
            if REMOVE_HEADERS_FOOTERS:
                logger.info(f"Removing headers/footers: {source_name}")
                self._remove_headers_footers(pdf_doc)

            # ── 2. Page classification (AFTER redaction) ──────────────────
            pages_info = self._analyze_pages(pdf_doc)

            if all(p.kind == "blank" for p in pages_info):
                logger.warning(f"All pages are blank in '{source_name}'")
                return []

            # ── 3. Full-document shortcut ──────────────────────────────────
            if full_document:
                return self._build_full_document(pdf_doc, source_name)

            # ── 4. Per-page building ────────────────────────────────────────
            documents = self._build_documents(pdf_doc, pages_info, source_name)

            if not documents:
                logger.warning(f"No content extracted for '{source_name}'")
            else:
                logger.info(f"Extracted {len(documents)} pages from '{source_name}'")
            return documents

        except Exception as e:
            logger.error(f"[MarkItDown] Error processing '{source_name}': {e}", exc_info=True)
            return []
        finally:
            if pdf_doc is not None:
                pdf_doc.close()

    def diagnostics(self) -> Dict[str, str]:
        """Diagnostic information, for consistency with the other parsers."""
        return {
            "ocr_enabled": str(self._enable_ocr),
            "ocr_language": self._ocr_language,
            "ocr_dpi": str(self._ocr_dpi),
            "remove_headers_footers": str(REMOVE_HEADERS_FOOTERS),
            "header_footer_mode": HEADER_FOOTER_MODE,
            "known_limitation": (
                "cross-page tables are split (MarkItDown has no multi-page "
                "context when driven page-by-page)"
            ),
        }

    # ══════════════════════════════════════════════════════════════
    # PAGE ANALYSIS (classification + section boundaries)
    # Identical approach to the other parsers in this project, for
    # consistent metadata (page_type, section_index) across engines.
    # ══════════════════════════════════════════════════════════════

    def _analyze_pages(self, pdf_doc: "pymupdf.Document") -> List[PageInfo]:
        """Classifies every page and assigns section_index (blank pages = boundaries)."""
        result: List[PageInfo] = []
        section_index = 0
        pending_gap = False
        has_content = False

        for i, page in enumerate(pdf_doc):
            plain_text = page.get_text().strip()
            kind = self._classify_page(page, plain_text)

            if kind == "blank":
                if has_content:
                    pending_gap = True
            else:
                if pending_gap:
                    section_index += 1
                    pending_gap = False
                has_content = True

            result.append(
                PageInfo(
                    number=i + 1,
                    kind=kind,
                    section_index=section_index,
                    plain_text=plain_text,
                )
            )

        counts = Counter(p.kind for p in result)
        logger.info(f"Page classification: {dict(counts)}, sections: {section_index + 1}")
        return result

    def _classify_page(self, page: "pymupdf.Page", plain_text: str) -> str:
        """
        Returns 'text' | 'scan' | 'drawing' | 'blank'.

        FIX (#1, critical): the original implementation only checked
        `page.get_images(full=True)` to decide whether to attempt OCR at all.
        That check only detects EMBEDDED RASTER images - a page containing
        ONLY vector graphics (lines, shapes, vector-drawn text/labels, e.g. a
        store layout plan) has no text layer AND no raster image, so it was
        previously classified as a truly empty page and silently dropped,
        with no OCR attempt whatsoever. The ink-ratio check below (same
        technique used by the other two parsers in this project) correctly
        distinguishes "genuinely blank page" from "page with vector content
        but no raster image", routing the latter to 'drawing' -> OCR attempt.
        """
        if len(plain_text) >= MIN_TEXT_CHARS:
            return "text"

        if self._ink_ratio(page) < BLANK_INK_RATIO:
            return "blank"

        return "scan" if page.get_images(full=True) else "drawing"

    @staticmethod
    def _ink_ratio(page: "pymupdf.Page") -> float:
        """
        Share of 'ink' pixels in a low-resolution render. Works for raster
        images and vector graphics alike (unlike get_images(), which only
        sees embedded raster XObjects). The background level is estimated
        from the page itself, so off-white scans of empty pages are still
        recognized as blank.
        """
        r = page.rect
        scale = min(40 / 72, CLASSIFY_MAX_PX / max(r.width, r.height))
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(scale, scale),
            colorspace=pymupdf.csGRAY,
            alpha=False,
        )
        samples = pix.samples
        if not samples:
            return 0.0

        hist = Counter(samples)
        background = max(hist, key=hist.get)
        ink = sum(count for value, count in hist.items() if value < background - INK_DELTA)
        return ink / len(samples)

    @staticmethod
    def _is_noise(text: str) -> bool:
        """
        True if OCR/fallback text looks like garbage (typical for plans,
        photos, stamps).

        FIX (#3): the original code had no noise filter at all - any OCR
        output, however garbled, was accepted as long as it was non-empty
        and "longer than the alternative". This mirrors the noise filter
        used in the other two parsers for consistent behavior.
        """
        compact = re.sub(r"\s", "", text or "")
        if not compact:
            return True
        letters = sum(ch.isalpha() for ch in compact)
        return letters < MIN_OCR_LETTERS or letters / len(compact) < MIN_OCR_LETTER_RATIO

    # ══════════════════════════════════════════════════════════════
    # BUILDING DOCUMENTS
    # ══════════════════════════════════════════════════════════════

    def _build_documents(
        self,
        pdf_doc: "pymupdf.Document",
        pages_info: List[PageInfo],
        source_name: str,
    ) -> List[Document]:
        """Combines MarkItDown/OCR output with the page analysis into one Document per page."""
        documents: List[Document] = []
        blank_pages: List[int] = []
        non_text_pages: List[int] = []
        failed_pages: List[int] = []

        # FIX (#5, documentation not a code fix): precompute, per text page,
        # whether an adjacent page in the same section is also a text page -
        # a (conservative, approximate) signal that a table might continue
        # across the page break and therefore might have been split by the
        # page-by-page MarkItDown architecture. This cannot be detected with
        # certainty without inspecting the actual table content, so treat it
        # as a hint for downstream review, not a guarantee.
        adjacency_flags = self._compute_adjacent_text_flags(pages_info)

        for info in pages_info:
            if info.kind == "blank":
                blank_pages.append(info.number)
                continue

            page_type = info.kind
            method = ""
            text = ""

            if info.kind == "text":
                # FIX (#8): markitdown conversion and OCR are now independent
                # try/except blocks (see below for scan/drawing), so a
                # failure in one path doesn't prevent falling back to the
                # plain PyMuPDF text layer.
                try:
                    text = self._convert_page_markitdown(pdf_doc, info.number - 1)
                    method = "markitdown"
                except Exception as e:
                    logger.error(
                        f"[MarkItDown] Page {info.number} conversion error "
                        f"('{source_name}'): {e}"
                    )
                    text = ""

                if not text:
                    text = info.plain_text
                    method = "pymupdf-text"

            else:  # 'scan' or 'drawing'
                # FIX (#1): OCR is now attempted for 'drawing' pages too, not
                # only pages that happen to contain an embedded raster image.
                ocr_text = ""
                if self._enable_ocr:
                    try:
                        ocr_text = self._ocr_page(pdf_doc[info.number - 1])
                    except Exception as e:
                        logger.warning(
                            f"[MarkItDown] OCR failed on page {info.number} "
                            f"('{source_name}'): {e}"
                        )

                # FIX (#3, #9): selection is now based on passing the noise
                # filter, not on "whichever candidate is longer" (the
                # original `len(ocr_text) > len(text)` heuristic, which a
                # long garbled OCR result could win against a short-but
                # correct fragment).
                if ocr_text and not self._is_noise(ocr_text):
                    text = ocr_text
                    method = "ocr"
                elif info.plain_text and not self._is_noise(info.plain_text):
                    text = info.plain_text
                    method = "pymupdf-text"

            if not text or self._is_noise(text):
                non_text_pages.append(info.number)
                if not INCLUDE_NON_TEXT_PAGES:
                    continue
                text = NON_TEXT_PLACEHOLDER
                method = "placeholder"

            # FIX (#4): metadata schema unified with the other two parsers in
            # this project (page_type, section_index added; previously
            # missing here entirely).
            metadata = self._base_metadata(source_name)
            metadata.update(
                {
                    "page_number": info.number,
                    "page_type": page_type,
                    "section_index": info.section_index,
                    "extraction_method": method,
                    "table_may_be_split_across_pages": adjacency_flags.get(info.number, False),
                }
            )
            documents.append(Document(page_content=text, metadata=metadata))

        if blank_pages:
            logger.info(f"[MarkItDown] Skipped blank pages {blank_pages} ('{source_name}')")
        if non_text_pages:
            logger.info(
                f"[MarkItDown] Pages without extractable text (plans/images) "
                f"{non_text_pages} ('{source_name}')"
            )
        if failed_pages:
            logger.warning(f"[MarkItDown] No text from pages {failed_pages} ('{source_name}')")

        flagged = [n for n, v in adjacency_flags.items() if v]
        if flagged:
            logger.info(
                f"[MarkItDown] Pages possibly containing a cross-page table "
                f"fragment (see module docstring on this limitation): "
                f"{flagged} ('{source_name}')"
            )

        return documents

    @staticmethod
    def _compute_adjacent_text_flags(pages_info: List[PageInfo]) -> Dict[int, bool]:
        """
        For every 'text' page, flags whether the previous or next page within
        the SAME section is also a 'text' page - a rough heuristic hint that
        a table (or any other multi-page structure) might span the boundary
        and therefore might have been split by the per-page MarkItDown
        architecture (see module docstring).
        """
        by_number = {p.number: p for p in pages_info}
        flags: Dict[int, bool] = {}
        for p in pages_info:
            if p.kind != "text":
                continue
            prev_p = by_number.get(p.number - 1)
            next_p = by_number.get(p.number + 1)
            adjacent_text = (
                (prev_p is not None and prev_p.kind == "text" and prev_p.section_index == p.section_index)
                or (next_p is not None and next_p.kind == "text" and next_p.section_index == p.section_index)
            )
            flags[p.number] = adjacent_text
        return flags

    def _build_full_document(self, pdf_doc: "pymupdf.Document", source_name: str) -> List[Document]:
        """
        Whole document as a single Document, via one MarkItDown call on the
        whole (already redacted) file. This path preserves cross-page table
        structure (MarkItDown sees the complete document at once), but does
        NOT produce per-page classification / section_index metadata.
        """
        try:
            whole_bytes = pdf_doc.tobytes()
            text = self._convert_bytes_via_tempfile(whole_bytes)
        except Exception as e:
            logger.error(f"[MarkItDown] Full-document conversion failed: {e}")
            return []

        if not text:
            return []

        metadata = self._base_metadata(source_name)
        metadata.update({"page_number": 1, "mode": "full_document"})
        return [Document(page_content=text, metadata=metadata)]

    @staticmethod
    def _base_metadata(source_name: str) -> Dict[str, object]:
        return {
            "source": source_name,
            "parser": "markitdown",
            "headers_footers_removed": REMOVE_HEADERS_FOOTERS,
        }

    # ══════════════════════════════════════════════════════════════
    # PAGE-LEVEL PROCESSING
    # ══════════════════════════════════════════════════════════════

    def _convert_page_markitdown(self, pdf_doc: pymupdf.Document, page_index: int) -> str:
        """
        Cuts a single page into a separate PDF and converts it with MarkItDown.

        NOTE: this physical isolation is the root cause of the cross-page
        table limitation described in the module docstring - MarkItDown is
        given no way to see beyond the single page's content.
        """
        single = pymupdf.open()
        try:
            single.insert_pdf(pdf_doc, from_page=page_index, to_page=page_index)
            page_bytes = single.tobytes()
        finally:
            single.close()

        return self._convert_bytes_via_tempfile(page_bytes)

    def _ocr_page(self, page: pymupdf.Page) -> str:
        """Runs Tesseract OCR on a page (full-page OCR, ignoring the text layer)."""
        tessdata: Optional[str] = os.environ.get("TESSDATA_PREFIX")
        textpage = page.get_textpage_ocr(
            language=self._ocr_language,
            dpi=self._ocr_dpi,
            full=True,
            tessdata=tessdata,
        )
        return page.get_text(textpage=textpage).strip()

    def _convert_bytes_via_tempfile(self, raw_bytes: bytes) -> str:
        """
        Writes the bytes to a temporary .pdf file, converts it with MarkItDown
        and removes the file (also when an exception occurs).

        FIX (#11): the actual .convert() call is now serialized via
        _convert_lock as a defensive measure against unverified thread-safety
        assumptions for a shared MarkItDown instance.
        """
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_file:
            tmp_path = tmp_file.name
            tmp_file.write(raw_bytes)

        try:
            with self._convert_lock:
                result = self._converter.convert(tmp_path)
            return (result.text_content or "").strip()
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    # ══════════════════════════════════════════════════════════════
    # HEADER / FOOTER REMOVAL (PyMuPDF redaction)
    # Same approach as the other two parsers in this project, applied once
    # to the whole document BEFORE per-page classification/splitting, so
    # MarkItDown also sees the redacted content on each isolated page.
    # ══════════════════════════════════════════════════════════════

    def _remove_headers_footers(self, pdf_doc: "pymupdf.Document") -> None:
        if HEADER_FOOTER_MODE == "auto":
            rects_by_page = self._find_repeated_blocks(pdf_doc)
            image_mode = pymupdf.PDF_REDACT_IMAGE_NONE
        elif HEADER_FOOTER_MODE == "fixed":
            rects_by_page = self._fixed_margin_rects(pdf_doc)
            image_mode = pymupdf.PDF_REDACT_IMAGE_PIXELS
        else:
            raise ValueError(
                f"Unknown HEADER_FOOTER_MODE: {HEADER_FOOTER_MODE!r} (use 'auto' or 'fixed')"
            )

        pages_redacted = 0
        for i, page in enumerate(pdf_doc):
            rects = rects_by_page.get(i)
            if not rects:
                continue
            for rect in rects:
                # CAUTION: rects are in visible (rotated) coordinates;
                # redaction needs unrotated ones. Not empirically verified
                # against real pages with /Rotate 90/180/270 - test on an
                # actual rotated page before trusting this in production.
                page.add_redact_annot(rect * page.derotation_matrix)
            page.apply_redactions(
                images=image_mode,
                # CAUTION: vector graphics are never removed by this, even in
                # "fixed" mode. Usually harmless for text/OCR extraction.
                graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
            )
            pages_redacted += 1

        logger.info(
            f"Header/footer removal ({HEADER_FOOTER_MODE}): "
            f"{pages_redacted}/{len(pdf_doc)} pages modified."
        )

    @staticmethod
    def _fixed_margin_rects(pdf_doc: "pymupdf.Document") -> Dict[int, List["pymupdf.Rect"]]:
        result: Dict[int, List["pymupdf.Rect"]] = {}
        for i, page in enumerate(pdf_doc):
            r = page.rect
            if r.height <= FIXED_TOP_MARGIN_PT + FIXED_BOTTOM_MARGIN_PT + FIXED_MIN_CONTENT_HEIGHT_PT:
                logger.warning(
                    f"Page {i + 1}: too short for fixed margins "
                    f"(height={r.height:.0f}pt) - skipping margin removal for this page."
                )
                continue
            result[i] = [
                pymupdf.Rect(r.x0, r.y0, r.x1, r.y0 + FIXED_TOP_MARGIN_PT),
                pymupdf.Rect(r.x0, r.y1 - FIXED_BOTTOM_MARGIN_PT, r.x1, r.y1),
            ]
        return result

    @staticmethod
    def _normalize_block(text: str) -> str:
        text = re.sub(r"\d+", "#", (text or "").lower())
        return re.sub(r"\s+", " ", text).strip()

    def _find_repeated_blocks(
        self, pdf_doc: "pymupdf.Document"
    ) -> Dict[int, List["pymupdf.Rect"]]:
        per_page: List[List[tuple]] = []
        counts: Counter = Counter()
        text_pages = 0

        for page in pdf_doc:
            r = page.rect
            header_limit = r.y0 + r.height * AUTO_HEADER_ZONE_RATIO
            footer_limit = r.y1 - r.height * AUTO_FOOTER_ZONE_RATIO

            entries = []
            page_has_text = False

            for x0, y0, x1, y1, txt, _block_no, block_type in page.get_text("blocks"):
                if block_type != 0:
                    continue
                signature = self._normalize_block(txt)
                if not signature:
                    continue
                page_has_text = True

                if y1 <= header_limit:
                    zone = "top"
                elif y0 >= footer_limit:
                    zone = "bottom"
                else:
                    continue

                if len(signature) > AUTO_MAX_BLOCK_CHARS:
                    continue
                entries.append((zone, signature, pymupdf.Rect(x0, y0, x1, y1)))

            if page_has_text:
                text_pages += 1
            counts.update({(zone, sig) for zone, sig, _ in entries})
            per_page.append(entries)

        threshold = max(AUTO_MIN_REPEAT_PAGES, math.ceil(AUTO_MIN_REPEAT_RATIO * text_pages))
        repeated = {key for key, count in counts.items() if count >= threshold}

        logger.debug(
            f"Repeated header/footer patterns: {len(repeated)} "
            f"(threshold={threshold} pages, text pages={text_pages})"
        )

        return {
            i: [rect for zone, sig, rect in entries if (zone, sig) in repeated]
            for i, entries in enumerate(per_page)
        }

    # ══════════════════════════════════════════════════════════════
    # LOADING THE PDF (supports str, bytes, BytesIO)
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _open_pdf(file_source: Union[str, io.BytesIO, bytes]) -> pymupdf.Document:
        """Opens a PDF file from disk or memory."""
        if isinstance(file_source, str):
            return pymupdf.Document(file_source)
        if isinstance(file_source, bytes):
            return pymupdf.Document(stream=file_source, filetype="pdf")
        if isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            return pymupdf.Document(stream=file_source.read(), filetype="pdf")
        raise ValueError(f"[MarkItDown] Unsupported source type: {type(file_source)}")

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "memory stream (MarkItDown)"