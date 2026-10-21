import asyncio
import concurrent.futures
import io
import logging
import math
import os
import re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union

import pymupdf  # PyMuPDF – header/footer removal, page analysis, page splitting
from langchain_core.documents import Document
from kreuzberg import extract_bytes, ExtractionConfig, OcrConfig

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# ======================================================================
# SETTINGS
# ======================================================================

# Master switch: remove headers and footers before extraction?
REMOVE_HEADERS_FOOTERS = True

# How to find headers / footers (used only if REMOVE_HEADERS_FOOTERS is True):
#   "auto"  - removes only text blocks in the top/bottom zone that REPEAT across
#             pages (page numbers, running titles). Safe for energy certificates,
#             plans and tables. Works only on pages with a text layer.
#   "fixed" - removes fixed margins (below) from every page, including scans.
#             Risky for mixed documents (may delete real content near the edge).
HEADER_FOOTER_MODE = "auto"

# --- "fixed" mode ---
FIXED_TOP_MARGIN_PT = 50          # 1 pt = 1/72 inch
FIXED_BOTTOM_MARGIN_PT = 60
FIXED_MIN_CONTENT_HEIGHT_PT = 50  # pages shorter than margins + this are left untouched

# --- "auto" mode ---
AUTO_HEADER_ZONE_RATIO = 0.10     # top 10% of the page height is the header zone
AUTO_FOOTER_ZONE_RATIO = 0.10     # bottom 10% is the footer zone
AUTO_MIN_REPEAT_PAGES = 3         # a block must repeat on at least this many pages...
AUTO_MIN_REPEAT_RATIO = 0.30      # ...and on at least this share of pages with text
AUTO_MAX_BLOCK_CHARS = 200        # longer blocks are never treated as header/footer

# --- Page classification ---
MIN_TEXT_CHARS = 20               # fewer characters in the text layer = "no real text"
BLANK_INK_RATIO = 0.001           # share of "ink" pixels below which a page is blank
INK_DELTA = 50                    # pixel is "ink" if darker than background by this much
CLASSIFY_MAX_PX = 800             # longer side of the low-res render used for classification

# --- OCR noise filter (OCR on plans/photos returns garbage) ---
MIN_OCR_LETTERS = 10
MIN_OCR_LETTER_RATIO = 0.4        # letters / non-space characters

# --- Pages without extractable text (plans, drawings, photos, stamps) ---
INCLUDE_NON_TEXT_PAGES = True     # keep them as a short placeholder Document
NON_TEXT_PLACEHOLDER = "[Strona bez tekstu: rysunek, plan lub obraz]"

# FIX: pages that DO have a text layer but whose per-page extraction failed
# (Kreuzberg error / empty result) are now flagged explicitly instead of being
# silently dropped, so section_index / page numbering never has a silent gap.
INCLUDE_FAILED_PAGES = True
FAILED_PLACEHOLDER = "[Błąd ekstrakcji tekstu ze strony]"

# Tesseract language code(s), e.g. "pol", "pol+eng"
# FIX: default changed from "pol" to "pol+eng" - contracts/planograms routinely
# contain English brand names, SKUs, retail terms ("facing", "planogram", ...).
DEFAULT_LANGUAGE = "pol+eng"

# FIX: concurrency limit for the async extraction batch - Tesseract/Kreuzberg
# can be CPU-heavy, so unlimited concurrency across all pages of a large file
# could overload the machine. Also avoids spinning up one event loop per page.
MAX_CONCURRENT_EXTRACTIONS = 4


@dataclass
class PageInfo:
    """Lightweight per-page record used internally while building the result."""
    number: int                  # 1-based page number
    kind: str                    # "text" | "scan" | "drawing" | "blank"
    section_index: int
    has_embedded_raster: bool    # FIX: informational only, no longer gates OCR


class PdfParser(BaseDocumentParser):
    """
    PDF parser (Kreuzberg v4 + PyMuPDF) for "stitched" contracts: many documents
    in one file (contracts, energy certificates, plans, Excel printouts),
    separated by blank pages.

    Steps:
    1. Optionally remove headers / footers (see REMOVE_HEADERS_FOOTERS).
    2. Classify every page: text | scan | drawing | blank.
    3. Extract page by page:
       - text    -> regular extraction,
       - scan    -> forced OCR (noise-filtered),
       - drawing -> FIX: forced OCR as well (noise-filtered) - a vector plan
                    or outlined-text graphic has no embedded raster image but
                    may still carry real, OCR-readable content once rendered,
       - blank   -> skipped; blank pages also mark a boundary between documents
                    (metadata["section_index"]).

    Known architectural limitation: in the default (per-page) mode every page
    is cut into its own single-page PDF before extraction, so a table that
    spans two pages is never seen whole by Kreuzberg. Pages suspected of being
    part of such a split table are flagged via
    metadata["table_may_be_split_across_pages"]. Use full_document=True (see
    __init__) to process a whole file in one Kreuzberg call instead (trades
    away section_index / page_type granularity for correct cross-page tables).
    """

    def __init__(
        self,
        enable_ocr: bool = True,
        ocr_language: str = DEFAULT_LANGUAGE,
        full_document: bool = False,
        images_output_dir: Optional[str] = None,
        images_scale: float = 2.0,
    ) -> None:
        # FIX: configurable constructor, aligned with the other three parsers
        # (Marker / PyMuPDF4LLM / MarkItDown) instead of hardcoded module constants.
        self._enable_ocr = enable_ocr
        self._ocr_language = ocr_language
        self._full_document = full_document
        self._images_output_dir = images_output_dir
        self._images_scale = images_scale
        self._last_stats: Dict = {}

        if self._images_output_dir:
            os.makedirs(self._images_output_dir, exist_ok=True)

    # ------------------------------------------------------------------
    # Diagnostics
    # ------------------------------------------------------------------

    def diagnostics(self) -> Dict:
        """
        Returns stats from the last parse() call. Useful for monitoring /
        tests without parsing log output.
        """
        stats = dict(self._last_stats)
        stats["known_limitation"] = (
            "Cross-page tables are split: pages are cut into single-page PDFs "
            "before extraction unless full_document=True is used."
        )
        return stats

    # ------------------------------------------------------------------
    # Main method
    # ------------------------------------------------------------------

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        documents: List[Document] = []
        source_name = (
            os.path.basename(file_source)
            if isinstance(file_source, str)
            else "S3 memory stream"
        )

        pdf_doc = None
        try:
            pdf_doc = self._open_pdf(file_source)

            if REMOVE_HEADERS_FOOTERS:
                self._remove_headers_footers(pdf_doc)

            if self._full_document:
                return self._build_full_document(pdf_doc, source_name, **kwargs)

            pages_info, blank_pages = self._analyze_pages(pdf_doc)

            # --- Prepare extraction jobs for non-blank pages ---
            jobs: List[Tuple[int, bytes, dict]] = []  # (page_number, pdf_bytes, kwargs)
            for info in pages_info:
                if info.kind == "blank":
                    continue
                force_ocr = info.kind in ("scan", "drawing")  # FIX: drawing now OCR'd too
                if force_ocr and not self._enable_ocr:
                    continue  # OCR disabled by configuration, handled below as non-text
                page_bytes = self._extract_single_page_bytes(pdf_doc, info.number - 1)
                page_kwargs = dict(kwargs)
                page_kwargs.setdefault("language", self._ocr_language)
                page_kwargs["force_ocr"] = force_ocr
                jobs.append((info.number, page_bytes, page_kwargs))

            # FIX: one batched async run instead of one event loop per page.
            results = self._run_extraction_batch(jobs)
            text_by_page: Dict[int, Optional[str]] = {}
            for (page_number, _bytes, _kwargs), result in zip(jobs, results):
                if isinstance(result, Exception):
                    logger.error(
                        "Page %d extraction error (%s): %s", page_number, source_name, result
                    )
                    text_by_page[page_number] = None
                else:
                    text_by_page[page_number] = (result.content or "").strip()

            non_text_pages: List[int] = []
            failed_pages: List[int] = []
            ocr_noise_pages: List[int] = []

            info_by_number = {info.number: info for info in pages_info}
            final_kind_by_number: Dict[int, str] = {}

            for info in pages_info:
                if info.kind == "blank":
                    continue

                if info.kind == "text":
                    text = text_by_page.get(info.number)
                    if text is None:
                        failed_pages.append(info.number)
                        final_kind_by_number[info.number] = "extraction_failed"
                        continue
                    if not text:
                        failed_pages.append(info.number)
                        final_kind_by_number[info.number] = "extraction_failed"
                        continue
                    final_kind_by_number[info.number] = "text"
                    continue

                # kind in ("scan", "drawing")
                page_type = info.kind
                if not self._enable_ocr:
                    text = ""
                else:
                    text = text_by_page.get(info.number)
                    if text is None:
                        text = ""
                    elif self._is_noise(text):
                        ocr_noise_pages.append(info.number)
                        text = ""
                        if info.kind == "scan":
                            # FIX: downgrade label only for 'scan' -> likely a
                            # photo/stamp, not real scanned text. 'drawing' stays
                            # 'drawing' (it already implies no embedded raster).
                            page_type = "drawing"

                if not text:
                    non_text_pages.append(info.number)
                final_kind_by_number[info.number] = page_type
                text_by_page[info.number] = text

            # --- Build Documents in page order, tracking section boundaries ---
            section_index = 0
            pending_gap = False
            has_content = False

            ordered_numbers = sorted(final_kind_by_number.keys())
            flags = self._compute_adjacent_text_flags(pages_info, final_kind_by_number)

            for info in pages_info:
                page_number = info.number
                if info.kind == "blank":
                    if has_content:
                        pending_gap = True
                    continue

                if pending_gap:
                    section_index += 1
                    pending_gap = False
                has_content = True

                page_type = final_kind_by_number[page_number]
                text = text_by_page.get(page_number) or ""

                if page_type == "extraction_failed":
                    if not INCLUDE_FAILED_PAGES:
                        continue
                    text = FAILED_PLACEHOLDER
                elif not text:
                    if not INCLUDE_NON_TEXT_PAGES:
                        continue
                    text = NON_TEXT_PLACEHOLDER
                    self._maybe_save_page_image(pdf_doc, page_number - 1, source_name)

                metadata = {
                    "page_number": page_number,
                    "page_type": page_type,
                    "section_index": section_index,
                    "source": source_name,
                    "parser": "kreuzberg",
                    "has_embedded_raster": info.has_embedded_raster,
                }
                if flags.get(page_number):
                    metadata["table_may_be_split_across_pages"] = True

                documents.append(Document(page_content=text, metadata=metadata))

            self._last_stats = {
                "source": source_name,
                "pages_total": len(pages_info),
                "sections": section_index + 1 if documents else 0,
                "blank_pages": blank_pages,
                "non_text_pages": non_text_pages,
                "failed_pages": failed_pages,
                "ocr_noise_pages": ocr_noise_pages,
                "documents_emitted": len(documents),
            }

            if blank_pages:
                logger.info("Skipped blank pages %s (%s)", blank_pages, source_name)
            if non_text_pages:
                logger.info(
                    "Pages without extractable text (plans/images) %s (%s)",
                    non_text_pages,
                    source_name,
                )
            if ocr_noise_pages:
                logger.info(
                    "OCR output discarded as noise on pages %s (%s)",
                    ocr_noise_pages,
                    source_name,
                )
            if failed_pages:
                logger.warning(
                    "Failed to extract text from pages with a text layer %s (%s) "
                    "- check OCR (Tesseract, language pack, TESSDATA_PREFIX)",
                    failed_pages,
                    source_name,
                )
            if not documents:
                logger.warning(
                    "PDF file is empty or text extraction failed (%s)", source_name
                )

            logger.info(
                "Extracted %d pages from PDF in %d section(s) (%s)",
                len(documents),
                section_index + 1 if documents else 0,
                source_name,
            )
            return documents

        except Exception as e:
            logger.error("Error converting PDF to Markdown (%s): %s", source_name, e)
            return []
        finally:
            if pdf_doc is not None:
                pdf_doc.close()

    # ------------------------------------------------------------------
    # full_document mode
    # ------------------------------------------------------------------

    def _build_full_document(
        self, pdf_doc: pymupdf.Document, source_name: str, **kwargs
    ) -> List[Document]:
        """
        Processes the whole (already redacted) PDF in a single Kreuzberg call.
        Preserves cross-page table structure at the cost of section_index /
        per-page page_type granularity.
        """
        page_kwargs = dict(kwargs)
        page_kwargs.setdefault("language", self._ocr_language)
        page_kwargs.setdefault("force_ocr", False)

        pdf_bytes = pdf_doc.tobytes()
        try:
            result = self._run_extraction(pdf_bytes, **page_kwargs)
        except Exception as e:
            logger.error("full_document extraction failed (%s): %s", source_name, e)
            return []

        text = (result.content or "").strip()
        if not text:
            logger.warning("full_document extraction returned empty text (%s)", source_name)
            return []

        self._last_stats = {
            "source": source_name,
            "mode": "full_document",
            "pages_total": len(pdf_doc),
            "documents_emitted": 1,
        }

        return [
            Document(
                page_content=text,
                metadata={
                    "page_number": None,
                    "page_count": len(pdf_doc),
                    "page_type": "full_document",
                    "section_index": 0,
                    "source": source_name,
                    "parser": "kreuzberg",
                },
            )
        ]

    # ------------------------------------------------------------------
    # Page analysis / classification
    # ------------------------------------------------------------------

    def _analyze_pages(self, pdf_doc: pymupdf.Document) -> Tuple[List[PageInfo], List[int]]:
        """Classifies every page once, up front. Section index is assigned later."""
        pages_info: List[PageInfo] = []
        blank_pages: List[int] = []

        for i, page in enumerate(pdf_doc):
            page_number = i + 1
            kind = self._classify_page(page)
            has_raster = bool(page.get_images(full=True))
            if kind == "blank":
                blank_pages.append(page_number)
            pages_info.append(
                PageInfo(
                    number=page_number,
                    kind=kind,
                    section_index=0,  # filled in later while building Documents
                    has_embedded_raster=has_raster,
                )
            )

        return pages_info, blank_pages

    def _classify_page(self, page: pymupdf.Page) -> str:
        """
        Returns 'text' | 'scan' | 'drawing' | 'blank'.
        Runs AFTER header/footer removal, so a page that contained only a
        page number becomes 'blank'.

        NOTE: 'scan' vs 'drawing' only distinguishes whether an embedded
        raster image is present. FIX: this distinction no longer controls
        whether OCR is attempted - both kinds are OCR'd (see parse()); it is
        kept purely as informational metadata (has_embedded_raster).
        """
        if len(page.get_text().strip()) >= MIN_TEXT_CHARS:
            return "text"

        if self._ink_ratio(page) < BLANK_INK_RATIO:
            return "blank"  # truly empty page or a scan of an empty page

        return "scan" if page.get_images(full=True) else "drawing"

    @staticmethod
    def _ink_ratio(page: pymupdf.Page) -> float:
        """
        Share of 'ink' pixels in a low-resolution render. Works for images and
        vector graphics alike. The background level is estimated from the page
        itself, so off-white scans of empty pages are still recognized as blank.
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
        """True if OCR output looks like garbage (typical for plans and photos)."""
        compact = re.sub(r"\s", "", text or "")
        if not compact:
            return True
        letters = sum(ch.isalpha() for ch in compact)
        return letters < MIN_OCR_LETTERS or letters / len(compact) < MIN_OCR_LETTER_RATIO

    # ------------------------------------------------------------------
    # Cross-page table heuristic (FIX: new, mirrors the MarkItDown parser)
    # ------------------------------------------------------------------

    @staticmethod
    def _compute_adjacent_text_flags(
        pages_info: List[PageInfo], final_kind_by_number: Dict[int, str]
    ) -> Dict[int, bool]:
        """
        Flags pages where a table might continue onto the next/previous page:
        heuristic - the adjacent page within the same (contiguous, non-blank)
        run is also of kind 'text'. Not a guarantee, just a signal for manual
        review or for preferring full_document=True on such files.
        """
        flags: Dict[int, bool] = {}
        numbers_in_order = [info.number for info in pages_info if info.kind != "blank"]
        kind_lookup = final_kind_by_number

        for idx, number in enumerate(numbers_in_order):
            if kind_lookup.get(number) != "text":
                continue
            prev_number = numbers_in_order[idx - 1] if idx > 0 else None
            next_number = numbers_in_order[idx + 1] if idx + 1 < len(numbers_in_order) else None

            prev_is_text = prev_number is not None and kind_lookup.get(prev_number) == "text" \
                and prev_number == number - 1
            next_is_text = next_number is not None and kind_lookup.get(next_number) == "text" \
                and next_number == number + 1

            if prev_is_text or next_is_text:
                flags[number] = True

        return flags

    # ------------------------------------------------------------------
    # Single page extraction
    # ------------------------------------------------------------------

    @staticmethod
    def _extract_single_page_bytes(pdf_doc: pymupdf.Document, page_index: int) -> bytes:
        """Cuts a single page into a separate PDF (bytes)."""
        single = pymupdf.open()
        try:
            single.insert_pdf(pdf_doc, from_page=page_index, to_page=page_index)
            return single.tobytes()
        finally:
            single.close()

    def _maybe_save_page_image(
        self, pdf_doc: pymupdf.Document, page_index: int, source_name: str
    ) -> None:
        """
        Optional: saves a PNG render of pages that ended up with no usable
        text (plans/drawings), so they can be routed to a multimodal LLM
        later instead of being lost entirely. Mirrors the Docling parser's
        images_output_dir feature.
        """
        if not self._images_output_dir:
            return
        try:
            page = pdf_doc[page_index]
            pix = page.get_pixmap(matrix=pymupdf.Matrix(self._images_scale, self._images_scale))
            base = os.path.splitext(os.path.basename(source_name))[0]
            out_path = os.path.join(
                self._images_output_dir, f"{base}_page{page_index + 1}.png"
            )
            pix.save(out_path)
        except Exception as e:
            logger.warning(
                "Could not save page image for page %d (%s): %s",
                page_index + 1, source_name, e,
            )

    # ------------------------------------------------------------------
    # Loading the PDF (supports str, bytes, BytesIO)
    # ------------------------------------------------------------------

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
        raise ValueError("Unsupported PDF source type")

    # ------------------------------------------------------------------
    # Removing headers / footers
    # ------------------------------------------------------------------

    def _remove_headers_footers(self, pdf_doc: pymupdf.Document) -> None:
        """
        Removes headers / footers by redaction (behaves the same for every
        extraction engine). Pages are never deleted, so page numbers stay
        aligned with the original file.
        """
        if HEADER_FOOTER_MODE == "auto":
            rects_by_page = self._find_repeated_blocks(pdf_doc)
            image_mode = pymupdf.PDF_REDACT_IMAGE_NONE  # text blocks only
        elif HEADER_FOOTER_MODE == "fixed":
            rects_by_page = self._fixed_margin_rects(pdf_doc)
            image_mode = pymupdf.PDF_REDACT_IMAGE_PIXELS  # also clears scanned pixels
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
                # CAUTION: rects are in visible (rotated) coordinates; redaction
                # needs unrotated ones (identity matrix for pages with rotation
                # 0). Not verified on pages rotated 90/180/270 degrees - test
                # against a real rotated-page sample before relying on this.
                page.add_redact_annot(rect * page.derotation_matrix)
            page.apply_redactions(
                images=image_mode,
                graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
            )
            pages_redacted += 1

        logger.info(
            "Header/footer removal (%s): %d/%d pages modified.",
            HEADER_FOOTER_MODE,
            pages_redacted,
            len(pdf_doc),
        )

    @staticmethod
    def _fixed_margin_rects(pdf_doc: pymupdf.Document) -> Dict[int, List[pymupdf.Rect]]:
        """'fixed' mode: top and bottom strips of a constant height on every page."""
        result: Dict[int, List[pymupdf.Rect]] = {}
        for i, page in enumerate(pdf_doc):
            r = page.rect
            if r.height <= FIXED_TOP_MARGIN_PT + FIXED_BOTTOM_MARGIN_PT + FIXED_MIN_CONTENT_HEIGHT_PT:
                continue  # page too short for such margins
            result[i] = [
                pymupdf.Rect(r.x0, r.y0, r.x1, r.y0 + FIXED_TOP_MARGIN_PT),
                pymupdf.Rect(r.x0, r.y1 - FIXED_BOTTOM_MARGIN_PT, r.x1, r.y1),
            ]
        return result

    @staticmethod
    def _normalize_block(text: str) -> str:
        """Digits -> '#', lowercase, collapsed whitespace ('Strona 3 z 10' == 'Strona 7 z 10')."""
        text = re.sub(r"\d+", "#", (text or "").lower())
        return re.sub(r"\s+", " ", text).strip()

    def _find_repeated_blocks(
        self, pdf_doc: pymupdf.Document
    ) -> Dict[int, List[pymupdf.Rect]]:
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
            counts.update({(zone, sig) for zone, sig, _ in entries})  # once per page
            per_page.append(entries)

        threshold = max(AUTO_MIN_REPEAT_PAGES, math.ceil(AUTO_MIN_REPEAT_RATIO * text_pages))
        repeated = {key for key, count in counts.items() if count >= threshold}

        logger.debug(
            "Repeated header/footer patterns: %d (threshold=%d pages, text pages=%d)",
            len(repeated),
            threshold,
            text_pages,
        )

        return {
            i: [rect for zone, sig, rect in entries if (zone, sig) in repeated]
            for i, entries in enumerate(per_page)
        }

    # ------------------------------------------------------------------
    # Async -> sync handling (Kreuzberg has an async API)
    # ------------------------------------------------------------------

    def _run_extraction(self, pdf_bytes: bytes, **kwargs):
        """
        Runs a single asynchronous Kreuzberg extraction in a synchronous
        context (used by full_document mode).
        """
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            return asyncio.run(self._async_extract(pdf_bytes, **kwargs))

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            return pool.submit(
                asyncio.run, self._async_extract(pdf_bytes, **kwargs)
            ).result()

    def _run_extraction_batch(self, jobs: List[Tuple[int, bytes, dict]]) -> List:
        """
        FIX: runs ALL page extractions for a document through a single event
        loop (bounded concurrency), instead of spinning up a new event loop /
        thread pool per page. Returns a list of results in the same order as
        `jobs`, with exceptions captured as exception objects rather than
        raised, so one failing page does not abort the whole document.
        """
        if not jobs:
            return []

        payload = [(pdf_bytes, kw) for _num, pdf_bytes, kw in jobs]

        try:
            asyncio.get_running_loop()
        except RuntimeError:
            return asyncio.run(self._async_extract_many(payload))

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            return pool.submit(asyncio.run, self._async_extract_many(payload)).result()

    @staticmethod
    async def _async_extract_many(payload: List[Tuple[bytes, dict]]) -> List:
        semaphore = asyncio.Semaphore(MAX_CONCURRENT_EXTRACTIONS)

        async def _bounded(pdf_bytes: bytes, kw: dict):
            async with semaphore:
                try:
                    return await PdfParser._async_extract(pdf_bytes, **kw)
                except Exception as e:  # noqa: BLE001 - surfaced to caller, not raised here
                    return e

        return await asyncio.gather(*[_bounded(b, kw) for b, kw in payload])

    @staticmethod
    async def _async_extract(pdf_bytes: bytes, **kwargs):
        """
        Asynchronous content extraction from a PDF (bytes) using the
        Kreuzberg v4 ExtractionConfig API.
        Supported kwargs: force_ocr (bool), language (str, e.g. 'pol+eng').
        """
        config = ExtractionConfig(
            force_ocr=bool(kwargs.get("force_ocr", False)),
            ocr=OcrConfig(
                backend="tesseract",
                language=kwargs.get("language", DEFAULT_LANGUAGE),
            ),
        )

        return await extract_bytes(
            pdf_bytes,
            mime_type="application/pdf",
            config=config,
        )