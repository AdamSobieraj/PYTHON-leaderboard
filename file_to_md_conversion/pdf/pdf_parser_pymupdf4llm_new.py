"""
pymupdf4llm_parser.py

Lightweight, CPU-friendly PDF -> Markdown parser based on PyMuPDF4LLM, extended
with the same "stitched contracts" handling used by the Marker-based parser:

  - header/footer removal (auto repeated-block detection, or fixed margins)
  - per-page classification: text | scan | drawing | blank
  - blank pages mark boundaries between stitched sub-documents (section_index)
  - optional OCR fallback for scanned/drawing pages via Tesseract (pytesseract)
  - OCR / fallback-text noise filtering (plans, photos, stamps produce garbage)

Unlike the Marker-based parser, this one does not require GPU models (no
Surya/EasyOCR) - OCR, if enabled, runs via the system Tesseract binary through
pytesseract. This is much lighter and faster, but generally less accurate on
poor-quality scans. Use this parser when speed/cost matters and most pages are
born-digital text, and reserve Marker/Docling for scan-heavy document batches.

Requirements:
    pip install pymupdf pymupdf4llm langchain-core
    # optional, for OCR of scanned/drawing pages:
    pip install pytesseract pillow
    # + the Tesseract binary installed on the system, with pol/eng trained data
    #   (e.g. apt-get install tesseract-ocr tesseract-ocr-pol)
"""

import io
import logging
import math
import os
import re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

# FIX (#0, critical - missed in the previous review): the original file used
# `pymupdf.Document(...)` without ever importing `pymupdf` directly - only
# `pymupdf4llm` was imported. pymupdf4llm imports pymupdf internally, but that
# import does NOT leak into this module's namespace. The original code would
# raise `NameError: name 'pymupdf' is not defined` on the very first call to
# parse() for any str/bytes/BytesIO source. This import fixes that.
import pymupdf
import pymupdf4llm
from langchain_core.documents import Document

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# ── Optional dependency: Tesseract OCR (for scanned/drawing pages) ────
try:
    import pytesseract
    from PIL import Image

    # Fails fast if the Tesseract *binary* itself is missing, not just the
    # Python wrapper package - a very common deployment mistake.
    pytesseract.get_tesseract_version()
    OCR_AVAILABLE = True
except Exception:
    OCR_AVAILABLE = False
    logger.warning(
        "pytesseract/Tesseract not available -> scanned and drawing pages will "
        "fall back to a placeholder instead of OCR text. Install with: "
        "pip install pytesseract pillow, plus the Tesseract binary."
    )

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
# FIX (#5): the height check above is now actually enforced in
# _fixed_margin_rects() below, instead of being absent (the original code
# would crash with an invalid pymupdf.Rect on unusually small/rotated pages,
# e.g. non-standard-size store layout plans).

# --- "auto" mode ---
AUTO_HEADER_ZONE_RATIO = 0.10     # top 10% of the page height is the header zone
AUTO_FOOTER_ZONE_RATIO = 0.10     # bottom 10% is the footer zone
AUTO_MIN_REPEAT_PAGES = 3         # a block must repeat on at least this many pages...
AUTO_MIN_REPEAT_RATIO = 0.30      # ...and on at least this share of pages with text
AUTO_MAX_BLOCK_CHARS = 200        # longer blocks are never treated as header/footer
# KNOWN LIMITATION (same as in the Marker parser): the repetition threshold is
# computed GLOBALLY across the whole stitched file. A contract template that
# appears only once or twice in a large "stitched" PDF will not have its
# header/footer recognized as repeating and will not be cleaned, while the
# most common template will be. A per-section fix would require classifying
# pages into sections BEFORE redaction, which conflicts with the current
# design (a page containing only a page number must become 'blank' only
# AFTER redaction). Documented limitation, not fixed here.

# --- Page classification ---
MIN_TEXT_CHARS = 20               # fewer characters in the text layer = "no real text"
BLANK_INK_RATIO = 0.001           # share of "ink" pixels below which a page is blank
INK_DELTA = 50                    # pixel is "ink" if darker than background by this much
CLASSIFY_MAX_PX = 800             # longer side of the low-res render used for classification

# --- OCR ---
OCR_RENDER_DPI = 300              # render resolution for OCR; higher = better accuracy, slower
MIN_OCR_LETTERS = 10
MIN_OCR_LETTER_RATIO = 0.4        # letters / non-space characters

# --- Pages without extractable text (plans, drawings, photos, stamps) ---
INCLUDE_NON_TEXT_PAGES = True     # keep them as a short placeholder Document
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
    PDF parser based on PyMuPDF4LLM + PyMuPDF, extended to handle "stitched"
    contracts: many documents in one file (contracts, energy certificates,
    plans, Excel printouts), separated by blank pages.

    Lighter-weight alternative to the Marker-based parser: no GPU / deep
    learning OCR models, just the system Tesseract binary (optional).

    Steps:
    1. Optionally remove headers / footers (see REMOVE_HEADERS_FOOTERS).
    2. Classify every page: text | scan | drawing | blank.
    3. Convert born-digital pages via PyMuPDF4LLM (page_chunks=True, so page
       order and count are index-aligned with the PDF - no fragile separator
       parsing needed, unlike engines that emit a single combined markdown
       string with inline page markers).
    4. For 'scan' and 'drawing' pages, optionally run Tesseract OCR on a
       rendered image of the page (useful for plans where labels are drawn
       as vector shapes/outlines rather than selectable text).
    5. Build one Document per page:
       - text    -> PyMuPDF4LLM output (fallback: PyMuPDF text layer),
       - scan    -> Tesseract OCR output, noise-filtered,
       - drawing -> Tesseract OCR output if it passes the noise filter,
                    otherwise a placeholder,
       - blank   -> skipped; blank pages also mark a boundary between
                    documents (metadata["section_index"]).
    """

    def __init__(self, enable_ocr: bool = True, ocr_languages: str = "pol+eng"):
        """
        Args:
            enable_ocr:    Whether to attempt Tesseract OCR on scanned/drawing
                           pages. Forced to False if pytesseract/Tesseract is
                           not installed (with a warning).
            ocr_languages: Tesseract language string, e.g. "pol+eng".
        """
        self._enable_ocr = enable_ocr and OCR_AVAILABLE
        if enable_ocr and not OCR_AVAILABLE:
            logger.warning(
                "enable_ocr=True but Tesseract is not available - "
                "scanned/drawing pages will use placeholders instead of OCR text."
            )
        self._ocr_languages = ocr_languages

        if REMOVE_HEADERS_FOOTERS:
            logger.info(f"Header/footer removal: ON (mode={HEADER_FOOTER_MODE})")
        else:
            logger.info("Header/footer removal: OFF")

        logger.info(
            f"PyMuPDF4LLM parser ready | ocr={self._enable_ocr} ({ocr_languages})"
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
            full_document (bool): Whole document as a single Document.
                                   Default False.
        """
        full_document = kwargs.get("full_document", False)
        source_name = self._get_source_name(file_source)
        pdf_doc = None

        try:
            pdf_doc = pymupdf.Document(
                stream=self._get_bytes(file_source), filetype="pdf"
            )

            # ── 1. Header/footer removal ──────────────────────────
            if REMOVE_HEADERS_FOOTERS:
                logger.info(f"Removing headers/footers: {source_name}")
                self._remove_headers_footers(pdf_doc)

            # ── 2. Page classification (AFTER redaction, so a page ──
            #       that contained only a page number becomes 'blank')
            pages_info = self._analyze_pages(pdf_doc)

            if all(p.kind == "blank" for p in pages_info):
                logger.warning(f"All pages are blank in '{source_name}'")
                return []

            # ── 3. Full-document shortcut ──────────────────────────
            if full_document:
                return self._build_full_document(pdf_doc, source_name)

            # ── 4. PyMuPDF4LLM conversion (born-digital pages) ─────
            md_by_page = self._convert_text_pages(pdf_doc, source_name)

            # ── 5. Building documents ──────────────────────────────
            documents = self._build_documents(pdf_doc, pages_info, md_by_page, source_name)

            if not documents:
                logger.warning(f"No content extracted for '{source_name}'")
            else:
                logger.info(f"Extracted {len(documents)} pages from '{source_name}'")
            return documents

        except Exception as e:
            logger.error(f"PDF processing error ({source_name}): {e}", exc_info=True)
            return []

        finally:
            # FIX (#3): previously pdf_doc.close() was only called on the
            # success path, right before `return documents`. Any exception
            # raised between opening the document and that line (e.g. during
            # cropping/redaction or during pymupdf4llm conversion) left the
            # document handle open - a real leak when batch-processing many
            # "stitched" files in a loop.
            if pdf_doc is not None:
                pdf_doc.close()

    def diagnostics(self) -> Dict[str, str]:
        """Diagnostic information."""
        return {
            "ocr_available": str(OCR_AVAILABLE),
            "ocr_enabled": str(self._enable_ocr),
            "ocr_languages": self._ocr_languages,
            "remove_headers_footers": str(REMOVE_HEADERS_FOOTERS),
            "header_footer_mode": HEADER_FOOTER_MODE,
        }

    # ══════════════════════════════════════════════════════════════
    # PAGE ANALYSIS (classification + section boundaries)
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
        """Returns 'text' | 'scan' | 'drawing' | 'blank'."""
        if len(plain_text) >= MIN_TEXT_CHARS:
            return "text"

        if self._ink_ratio(page) < BLANK_INK_RATIO:
            return "blank"

        return "scan" if page.get_images(full=True) else "drawing"

    @staticmethod
    def _ink_ratio(page: "pymupdf.Page") -> float:
        """
        Share of 'ink' pixels in a low-resolution render. The background level
        is estimated from the page itself, so off-white scans of empty pages
        are still recognized as blank.
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
        """True if OCR/fallback text looks like garbage (typical for plans and photos)."""
        compact = re.sub(r"\s", "", text or "")
        if not compact:
            return True
        letters = sum(ch.isalpha() for ch in compact)
        return letters < MIN_OCR_LETTERS or letters / len(compact) < MIN_OCR_LETTER_RATIO

    # ══════════════════════════════════════════════════════════════
    # OCR (scan / drawing pages)
    # ══════════════════════════════════════════════════════════════

    def _ocr_page(self, page: "pymupdf.Page") -> str:
        """
        Renders a page to an image and runs Tesseract OCR on it.

        Used for both 'scan' pages (photographed/scanned documents) and
        'drawing' pages (e.g. store layout plans) - in the latter case labels
        are sometimes drawn as vector outlines rather than selectable text,
        and rendering + OCR can still recover them, unlike a plain text-layer
        read which would see nothing at all.
        """
        if not self._enable_ocr:
            return ""

        try:
            zoom = OCR_RENDER_DPI / 72
            pix = page.get_pixmap(
                matrix=pymupdf.Matrix(zoom, zoom),
                colorspace=pymupdf.csRGB,
                alpha=False,
            )
            image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            text = pytesseract.image_to_string(image, lang=self._ocr_languages)
            return text.strip()
        except Exception as e:
            logger.warning(f"OCR failed on page {page.number + 1}: {e}")
            return ""

    # ══════════════════════════════════════════════════════════════
    # PYMUPDF4LLM CONVERSION (born-digital text pages)
    # ══════════════════════════════════════════════════════════════

    def _convert_text_pages(
        self, pdf_doc: "pymupdf.Document", source_name: str
    ) -> Dict[int, str]:
        """
        Converts the whole document via PyMuPDF4LLM (page_chunks=True) and
        returns {page_number (1-based): markdown_text}.

        Note: because page_chunks=True returns one chunk per page IN DOCUMENT
        ORDER (pages are never deleted, only their cropbox/content may be
        redacted), this mapping is index-aligned by construction - unlike
        engines that emit a single combined markdown string with inline
        separators that must be parsed via regex (fragile across versions).
        """
        try:
            # FIX (#11): try to disable PyMuPDF4LLM's own built-in header/
            # footer heuristic (hdr_info), since we already do our own
            # redaction-based removal above and don't want the two mechanisms
            # to interact in an unpredictable way. Guarded for older
            # pymupdf4llm versions that may not support this parameter.
            md_pages = pymupdf4llm.to_markdown(doc=pdf_doc, page_chunks=True, hdr_info=False)
        except TypeError:
            md_pages = pymupdf4llm.to_markdown(doc=pdf_doc, page_chunks=True)

        if len(md_pages) != len(pdf_doc):
            logger.warning(
                f"PyMuPDF4LLM returned {len(md_pages)} chunks but the document "
                f"has {len(pdf_doc)} pages ({source_name}) - page numbers may "
                f"be misaligned for the remaining pages."
            )

        result: Dict[int, str] = {}
        for i, page_data in enumerate(md_pages):
            text = (page_data.get("text") or "").strip()
            if text:
                result[i + 1] = text
        return result

    # ══════════════════════════════════════════════════════════════
    # BUILDING DOCUMENTS
    # ══════════════════════════════════════════════════════════════

    def _build_documents(
        self,
        pdf_doc: "pymupdf.Document",
        pages_info: List[PageInfo],
        md_by_page: Dict[int, str],
        source_name: str,
    ) -> List[Document]:
        """Combines PyMuPDF4LLM/OCR output with the page analysis into one Document per page."""
        documents: List[Document] = []
        blank_pages: List[int] = []
        non_text_pages: List[int] = []

        for info in pages_info:
            if info.kind == "blank":
                blank_pages.append(info.number)
                continue

            page_type = info.kind
            method = ""
            text = ""

            if info.kind == "text":
                text = md_by_page.get(info.number, "")
                method = "pymupdf4llm"
                if not text:
                    # Fallback: raw text layer, in case PyMuPDF4LLM produced
                    # an empty chunk for a page that does have a text layer
                    # (e.g. a page containing only a table PyMuPDF4LLM failed
                    # to render as markdown).
                    text = info.plain_text
                    method = "pymupdf-text"

            else:  # 'scan' or 'drawing'
                ocr_text = self._ocr_page(pdf_doc[info.number - 1])
                if ocr_text and not self._is_noise(ocr_text):
                    text = ocr_text
                    method = "tesseract-ocr"
                elif info.plain_text and not self._is_noise(info.plain_text):
                    # Rare, but possible: a handful of selectable characters
                    # exist even though the page was classified as scan/drawing.
                    text = info.plain_text
                    method = "pymupdf-text"

            # FIX (#1): previously only `if not text:` was checked, so a
            # short, noisy fallback (a few garbage characters) could slip
            # through as "real" content without a placeholder. Now the noise
            # filter is re-applied to whatever text survived the branches
            # above, regardless of its source.
            if not text or self._is_noise(text):
                non_text_pages.append(info.number)
                if not INCLUDE_NON_TEXT_PAGES:
                    continue
                text = NON_TEXT_PLACEHOLDER
                method = "placeholder"

            metadata = self._base_metadata(source_name)
            metadata.update(
                {
                    "page_number": info.number,
                    "page_type": page_type,
                    "section_index": info.section_index,
                    "extraction_method": method,
                }
            )
            documents.append(Document(page_content=text, metadata=metadata))

        if blank_pages:
            logger.info(f"Skipped blank pages {blank_pages} ({source_name})")
        if non_text_pages:
            logger.info(
                f"Pages without extractable text (plans/images) {non_text_pages} ({source_name})"
            )

        return documents

    def _build_full_document(self, pdf_doc: "pymupdf.Document", source_name: str) -> List[Document]:
        """Whole document as a single Document (native PyMuPDF4LLM export, no page split)."""
        try:
            try:
                full_md = pymupdf4llm.to_markdown(doc=pdf_doc, hdr_info=False)
            except TypeError:
                full_md = pymupdf4llm.to_markdown(doc=pdf_doc)
        except Exception as e:
            logger.error(f"pymupdf4llm.to_markdown() failed: {e}")
            return []

        full_md = (full_md or "").strip()
        if not full_md:
            return []

        metadata = self._base_metadata(source_name)
        metadata.update({"page_number": 1, "mode": "full_document"})
        return [Document(page_content=full_md, metadata=metadata)]

    @staticmethod
    def _base_metadata(source_name: str) -> Dict[str, object]:
        return {
            "source": source_name,
            "parser": "pymupdf4llm",
            "headers_footers_removed": REMOVE_HEADERS_FOOTERS,
        }

    # ══════════════════════════════════════════════════════════════
    # HEADER / FOOTER REMOVAL (PyMuPDF redaction)
    # ══════════════════════════════════════════════════════════════

    def _remove_headers_footers(self, pdf_doc: "pymupdf.Document") -> None:
        """
        Removes headers / footers by redaction. Pages are never deleted, so
        page numbers stay aligned with the original file.
        """
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
                # redaction needs unrotated ones. This has not been
                # empirically verified against real pages with /Rotate 90,
                # 180 or 270 - test on an actual rotated page before trusting
                # this in production.
                page.add_redact_annot(rect * page.derotation_matrix)
            page.apply_redactions(
                images=image_mode,
                # CAUTION: vector graphics (e.g. a ruled line under a header)
                # are never removed, even in "fixed" mode. Usually harmless
                # for text/OCR extraction, but not a complete visual clean-up.
                graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
            )
            pages_redacted += 1

        logger.info(
            f"Header/footer removal ({HEADER_FOOTER_MODE}): "
            f"{pages_redacted}/{len(pdf_doc)} pages modified."
        )

    @staticmethod
    def _fixed_margin_rects(pdf_doc: "pymupdf.Document") -> Dict[int, List["pymupdf.Rect"]]:
        """'fixed' mode: top and bottom strips of a constant height on every page."""
        result: Dict[int, List["pymupdf.Rect"]] = {}
        for i, page in enumerate(pdf_doc):
            r = page.rect
            # FIX (#5): validation that was missing in the original file -
            # pages shorter than the configured margins (e.g. non-standard
            # small-format plans) are now safely skipped instead of
            # potentially producing an invalid pymupdf.Rect / crashing.
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
        """Digits -> '#', lowercase, collapsed whitespace ('Page 3 of 10' == 'Page 7 of 10')."""
        text = re.sub(r"\d+", "#", (text or "").lower())
        return re.sub(r"\s+", " ", text).strip()

    def _find_repeated_blocks(
        self, pdf_doc: "pymupdf.Document"
    ) -> Dict[int, List["pymupdf.Rect"]]:
        """
        'auto' mode: finds text blocks in the header / footer zone whose
        (normalized) content repeats across many pages.
        """
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
                if block_type != 0:  # 0 = text block, 1 = image block
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
    # HELPER METHODS
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        # FIX (#9): translated from "strumień pamięci S3"
        return "in-memory stream (S3/RAM)"

    @staticmethod
    def _get_bytes(file_source: Union[str, io.BytesIO, bytes]) -> bytes:
        if isinstance(file_source, str):
            with open(file_source, "rb") as f:
                return f.read()
        elif isinstance(file_source, bytes):
            return file_source
        elif isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            return file_source.read()
        # FIX (#9): translated from "Nieobsługiwany typ źródła dla PDF"
        raise ValueError(f"Unsupported source type for PDF: {type(file_source)}")