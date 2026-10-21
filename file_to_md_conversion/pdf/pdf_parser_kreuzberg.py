import asyncio
import concurrent.futures
import io
import logging
import math
import os
import re
from collections import Counter
from typing import Dict, List, Union

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

# Tesseract language code(s), e.g. "pol", "pol+eng"
DEFAULT_LANGUAGE = "pol"


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
       - drawing -> no OCR (vector plan or image without text), placeholder,
       - blank   -> skipped; blank pages also mark a boundary between documents
                    (metadata["section_index"]).
    """

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

            blank_pages: List[int] = []
            non_text_pages: List[int] = []
            failed_pages: List[int] = []

            section_index = 0
            pending_gap = False   # a blank page was seen after some content
            has_content = False

            for i, page in enumerate(pdf_doc):
                page_number = i + 1
                kind = self._classify_page(page)

                if kind == "blank":
                    blank_pages.append(page_number)
                    if has_content:
                        pending_gap = True
                    continue

                # First content page after a gap -> new stitched document
                if pending_gap:
                    section_index += 1
                    pending_gap = False
                has_content = True

                text = ""
                page_type = kind

                try:
                    if kind == "text":
                        text = self._extract_single_page(
                            pdf_doc, i, force_ocr=False, **kwargs
                        )
                        if not text:
                            failed_pages.append(page_number)
                            continue
                    elif kind == "scan":
                        text = self._extract_single_page(
                            pdf_doc, i, force_ocr=True, **kwargs
                        )
                        if self._is_noise(text):
                            text = ""
                            page_type = "drawing"
                    else:  # "drawing": keep whatever short text exists, no OCR
                        text = page.get_text().strip()
                except Exception as e:
                    logger.error(
                        "Page %d extraction error (%s): %s", page_number, source_name, e
                    )
                    failed_pages.append(page_number)
                    continue

                if not text:
                    non_text_pages.append(page_number)
                    if not INCLUDE_NON_TEXT_PAGES:
                        continue
                    text = NON_TEXT_PLACEHOLDER

                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "page_number": page_number,
                            "page_type": page_type,
                            "section_index": section_index,
                            "source": source_name,
                            "parser": "kreuzberg",
                        },
                    )
                )

            if blank_pages:
                logger.info("Skipped blank pages %s (%s)", blank_pages, source_name)
            if non_text_pages:
                logger.info(
                    "Pages without extractable text (plans/images) %s (%s)",
                    non_text_pages,
                    source_name,
                )
            if failed_pages:
                logger.warning(
                    "Failed to extract text from pages %s (%s) "
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
    # Page classification
    # ------------------------------------------------------------------

    def _classify_page(self, page: pymupdf.Page) -> str:
        """
        Returns 'text' | 'scan' | 'drawing' | 'blank'.
        Runs AFTER header/footer removal, so a page that contained only a
        page number becomes 'blank'.
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
    # Single page extraction
    # ------------------------------------------------------------------

    def _extract_single_page(
        self, pdf_doc: pymupdf.Document, page_index: int, force_ocr: bool, **kwargs
    ) -> str:
        """Cuts a single page into a separate PDF and runs it through Kreuzberg."""
        single = pymupdf.open()
        try:
            single.insert_pdf(pdf_doc, from_page=page_index, to_page=page_index)
            page_bytes = single.tobytes()
        finally:
            single.close()

        page_kwargs = dict(kwargs)
        page_kwargs.setdefault("language", DEFAULT_LANGUAGE)
        page_kwargs["force_ocr"] = force_ocr

        result = self._run_extraction(page_bytes, **page_kwargs)
        return (result.content or "").strip()

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
                # Rects are in visible (rotated) coordinates; redaction needs
                # unrotated ones (identity matrix for pages with rotation 0)
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
        Runs the asynchronous Kreuzberg extraction in a synchronous context.
        If an asyncio event loop is already running (Jupyter, FastAPI),
        the extraction is run in a separate thread.
        """
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            return asyncio.run(self._async_extract(pdf_bytes, **kwargs))

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            return pool.submit(
                asyncio.run, self._async_extract(pdf_bytes, **kwargs)
            ).result()

    @staticmethod
    async def _async_extract(pdf_bytes: bytes, **kwargs):
        """
        Asynchronous content extraction from a PDF (bytes) using the
        Kreuzberg v4 ExtractionConfig API.
        Supported kwargs: force_ocr (bool), language (str, e.g. 'pol').
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