"""
docling_pdf_parser.py

PDF -> Markdown parser based on IBM Docling with GPU acceleration, for
"stitched" contracts: many documents in one file (contracts, energy
certificates, plans, Excel printouts), separated by blank pages.

Header/footer removal (controlled by REMOVE_HEADERS_FOOTERS):
  1. PRE-REMOVAL  - PyMuPDF redaction before Docling sees the file
                    ("auto": repeated blocks only, or "fixed": constant margins)
  2. SEMANTIC     - Docling labels PAGE_HEADER / PAGE_FOOTER are skipped
  3. POST-FILTER  - bbox position filter, only when PyMuPDF is unavailable
                    and HEADER_FOOTER_MODE == "fixed"

Requires:
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
    pip install docling easyocr langchain-core pymupdf
"""

import io
import logging
import math
import os
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union

import torch
from docling.datamodel.base_models import InputFormat
from docling.datamodel.document import DocumentStream
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    EasyOcrOptions,
    PdfPipelineOptions,
    TableFormerMode,
    TableStructureOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from langchain_core.documents import Document

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# ── Optional dependency: PyMuPDF (redaction + page analysis) ──
try:
    import pymupdf

    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False
    logger.info(
        "PyMuPDF not available -> no page classification and no redaction. "
        "For best results install: pip install pymupdf"
    )

# ── Optional: content layers (to include furniture when removal is OFF) ──
try:
    from docling_core.types.doc import ContentLayer
except ImportError:
    ContentLayer = None

# ======================================================================
# SETTINGS
# ======================================================================

# Master switch: remove headers and footers?
# (controls PyMuPDF redaction, Docling's semantic page_header/page_footer
# filter and the bbox post-filter)
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


@dataclass
class PageInfo:
    """Result of the page analysis (1-based page number)."""
    number: int
    kind: str            # 'text' | 'scan' | 'drawing' | 'blank'
    section_index: int   # index of the stitched document (blank pages = boundaries)
    plain_text: str      # text layer from PyMuPDF (fallback for Docling)


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on IBM Docling with GPU acceleration + PyMuPDF page analysis.

    Steps:
    1. Optionally remove headers / footers (see REMOVE_HEADERS_FOOTERS).
    2. Classify every page: text | scan | drawing | blank.
    3. Convert the whole file with Docling (pages are never deleted, so Docling's
       page numbers match the original file). Docling runs its own OCR
       (EasyOCR) on bitmap areas, so scans do not need a separate OCR pass.
    4. Build one Document per page:
       - text    -> Docling output (fallback: PyMuPDF text layer),
       - scan    -> Docling OCR output, noise-filtered,
       - drawing -> placeholder (plan / image without text),
       - blank   -> skipped; blank pages also mark a boundary between documents
                    (metadata["section_index"]).
    """

    # Labels to skip (semantic layer)
    SKIP_LABELS: set = {"page_header", "page_footer"}

    def __init__(
        self,
        use_gpu: bool = True,
        do_ocr: bool = True,
        ocr_languages: Optional[List[str]] = None,
        table_mode: str = "accurate",
        num_threads: int = 4,
    ):
        """
        Args:
            use_gpu:        Whether to use GPU (auto-fallback to CPU).
            do_ocr:         Whether to run OCR (for scans).
            ocr_languages:  OCR languages (default ["pl", "en"]).
            table_mode:     "accurate" (GPU) or "fast" (ok on CPU).
            num_threads:    CPU threads.
        """
        if REMOVE_HEADERS_FOOTERS:
            if FITZ_AVAILABLE:
                logger.info(
                    f"Header/footer removal: ON (mode={HEADER_FOOTER_MODE}, method: PyMuPDF redaction)"
                )
            else:
                logger.info(
                    "Header/footer removal: ON, but PyMuPDF is missing -> "
                    "semantic filter only"
                    + (" + bbox post-filter" if HEADER_FOOTER_MODE == "fixed" else "")
                )
        else:
            logger.info("Header/footer removal: OFF")

        # ── GPU ───────────────────────────────────────────────────
        self._device = self._detect_device(use_gpu)

        accelerator = AcceleratorOptions(
            num_threads=num_threads,
            device=(
                AcceleratorDevice.CUDA
                if self._device == "cuda"
                else AcceleratorDevice.CPU
            ),
        )

        # ── Tables ────────────────────────────────────────────────
        table_structure = TableStructureOptions(
            mode=(
                TableFormerMode.ACCURATE
                if table_mode == "accurate"
                else TableFormerMode.FAST
            ),
        )

        # ── OCR ───────────────────────────────────────────────────
        if ocr_languages is None:
            ocr_languages = ["pl", "en"]

        pipeline_options = PdfPipelineOptions(
            do_ocr=do_ocr,
            do_table_structure=True,
            table_structure_options=table_structure,
            accelerator_options=accelerator,
        )

        if do_ocr:
            pipeline_options.ocr_options = EasyOcrOptions(lang=ocr_languages)

        # ── Converter ─────────────────────────────────────────────
        logger.info("Loading Docling models...")

        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pipeline_options,
                )
            }
        )

        self._do_ocr = do_ocr
        self._table_mode = table_mode

        logger.info(
            f"DoclingPdfParser ready | device={self._device} | "
            f"OCR={do_ocr} ({ocr_languages}) | tables={table_mode}"
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
        Processes a PDF -> list of Documents (Markdown, 1 non-blank page = 1 Document).

        Kwargs:
            full_document (bool): The whole document as a single Document.
                                  Default False.
        """
        full_document = kwargs.get("full_document", False)
        source_name = self._get_source_name(file_source)
        pdf_doc = None

        try:
            # ── 1. Header/footer removal + page analysis (PyMuPDF) ──
            pages_info: Optional[List[PageInfo]] = None

            if FITZ_AVAILABLE:
                raw_bytes = self._get_bytes(file_source)
                pdf_doc = pymupdf.Document(stream=raw_bytes, filetype="pdf")

                if REMOVE_HEADERS_FOOTERS:
                    logger.info(f"Removing headers/footers: {source_name}")
                    self._remove_headers_footers(pdf_doc)

                # Classification runs AFTER removal, so a page that contained only
                # a page number becomes 'blank'
                pages_info = self._analyze_pages(pdf_doc)

                if all(p.kind == "blank" for p in pages_info):
                    logger.warning(f"All pages are blank in '{source_name}'")
                    return []

                pdf_to_process = pdf_doc.tobytes() if REMOVE_HEADERS_FOOTERS else raw_bytes
                conv_source = DocumentStream(
                    name="document.pdf", stream=io.BytesIO(pdf_to_process)
                )
            else:
                conv_source = self._prepare_source(file_source)

            # ── 2. Docling conversion (GPU) ───────────────────────
            logger.info(f"Docling conversion: {source_name}")
            result = self.converter.convert(conv_source)
            doc = result.document
            logger.info(f"Conversion finished: {source_name}")

            # ── 3. Building the documents ─────────────────────────
            # bbox post-filter only without PyMuPDF and in "fixed" mode
            use_postfilter = (
                REMOVE_HEADERS_FOOTERS
                and not FITZ_AVAILABLE
                and HEADER_FOOTER_MODE == "fixed"
            )

            if full_document:
                documents = self._build_full_document(doc, source_name, pages_info)
            else:
                documents = self._build_page_documents(
                    doc,
                    source_name,
                    pages_info=pages_info,
                    postfilter_margins=use_postfilter,
                )

            logger.info(f"Result: {len(documents)} documents from '{source_name}'")
            return documents

        except Exception as e:
            logger.error(f"Docling error ({source_name}): {e}", exc_info=True)
            return []

        finally:
            if pdf_doc is not None:
                pdf_doc.close()
            self._cleanup_gpu()

    def diagnostics(self) -> Dict[str, str]:
        """Diagnostic information."""
        info = {
            "device": self._device,
            "ocr": str(self._do_ocr),
            "table_mode": self._table_mode,
            "remove_headers_footers": str(REMOVE_HEADERS_FOOTERS),
            "header_footer_mode": HEADER_FOOTER_MODE,
            "pymupdf_available": str(FITZ_AVAILABLE),
            "torch_version": torch.__version__,
            "cuda_available": str(torch.cuda.is_available()),
        }

        if torch.cuda.is_available():
            info["gpu_name"] = torch.cuda.get_device_name(0)
            info["gpu_vram_gb"] = (
                f"{torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f}"
            )

        return info

    # ══════════════════════════════════════════════════════════════
    # PAGE ANALYSIS (classification + section boundaries)
    # ══════════════════════════════════════════════════════════════

    def _analyze_pages(self, pdf_doc: "pymupdf.Document") -> List[PageInfo]:
        """Classifies every page and assigns section_index (blank pages = boundaries)."""
        result: List[PageInfo] = []
        section_index = 0
        pending_gap = False   # a blank page was seen after some content
        has_content = False

        for i, page in enumerate(pdf_doc):
            plain_text = page.get_text().strip()
            kind = self._classify_page(page, plain_text)

            if kind == "blank":
                if has_content:
                    pending_gap = True
            else:
                # First content page after a gap -> new stitched document
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
            return "blank"  # truly empty page or a scan of an empty page

        return "scan" if page.get_images(full=True) else "drawing"

    @staticmethod
    def _ink_ratio(page: "pymupdf.Page") -> float:
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

    # ══════════════════════════════════════════════════════════════
    # HEADER / FOOTER REMOVAL (PyMuPDF redaction)
    # ══════════════════════════════════════════════════════════════

    def _remove_headers_footers(self, pdf_doc: "pymupdf.Document") -> None:
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
            f"Header/footer removal ({HEADER_FOOTER_MODE}): "
            f"{pages_redacted}/{len(pdf_doc)} pages modified."
        )

    @staticmethod
    def _fixed_margin_rects(pdf_doc: "pymupdf.Document") -> Dict[int, List["pymupdf.Rect"]]:
        """'fixed' mode: top and bottom strips of a constant height on every page."""
        result: Dict[int, List["pymupdf.Rect"]] = {}
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
            counts.update({(zone, sig) for zone, sig, _ in entries})  # once per page
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
    # POST-FILTER (provenance bounding box)
    # Fallback when PyMuPDF is unavailable ("fixed" mode only)
    # ══════════════════════════════════════════════════════════════

    def _is_in_margin(self, item, page_height: float) -> bool:
        """
        Checks whether the element lies in the top/bottom margin zone
        based on its provenance bounding box.

        Supports both Docling coordinate systems:
        - TOPLEFT:    (0,0) in the top-left corner
        - BOTTOMLEFT: (0,0) in the bottom-left corner
        """
        if not hasattr(item, "prov") or not item.prov:
            return False

        try:
            bbox = item.prov[0].bbox

            coord_origin = getattr(bbox, "coord_origin", None)
            origin_value = (
                coord_origin.value
                if hasattr(coord_origin, "value")
                else str(coord_origin)
            )
            is_topleft = origin_value in ("TOPLEFT", "topleft", None)

            if is_topleft:
                # bbox.t / bbox.b = distance from the top of the page
                if bbox.b <= FIXED_TOP_MARGIN_PT:
                    return True  # whole element in the top margin
                if bbox.t >= page_height - FIXED_BOTTOM_MARGIN_PT:
                    return True  # whole element in the bottom margin
            else:
                # bbox.b / bbox.t = distance from the bottom of the page
                if bbox.t <= FIXED_BOTTOM_MARGIN_PT:
                    return True  # element in the bottom margin
                if bbox.b >= page_height - FIXED_TOP_MARGIN_PT:
                    return True  # element in the top margin

        except Exception as e:
            logger.debug(f"Bbox margin check error: {e}")
            return False

        return False

    @staticmethod
    def _get_page_heights(doc) -> Dict[int, float]:
        """Gets the page heights from the Docling document: {page_no: height}."""
        heights: Dict[int, float] = {}
        if hasattr(doc, "pages"):
            for page_no, page_item in doc.pages.items():
                if hasattr(page_item, "size") and page_item.size:
                    heights[page_no] = page_item.size.height
        return heights

    # ══════════════════════════════════════════════════════════════
    # BUILDING THE DOCUMENTS
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _iter_items(doc):
        """
        Iterates over the Docling items. When header/footer removal is OFF,
        tries to include the 'furniture' layer too (page headers/footers live
        there and newer Docling versions skip it by default).
        """
        if not REMOVE_HEADERS_FOOTERS and ContentLayer is not None:
            try:
                return doc.iterate_items(
                    included_content_layers={ContentLayer.BODY, ContentLayer.FURNITURE}
                )
            except TypeError:
                pass  # older Docling without the layer argument
        return doc.iterate_items()

    def _collect_page_contents(
        self, doc, source_name: str, postfilter_margins: bool
    ) -> Dict[int, List[str]]:
        """Converts Docling items to Markdown fragments grouped by page."""
        page_contents: Dict[int, List[str]] = defaultdict(list)
        page_heights = self._get_page_heights(doc) if postfilter_margins else {}

        skipped_semantic = 0
        skipped_margin = 0
        total_elements = 0

        for item, level in self._iter_items(doc):
            total_elements += 1
            label = getattr(item, "label", None)
            label_value = label.value if hasattr(label, "value") else str(label)

            # ── Semantic filter (page_header / page_footer) ──────
            if REMOVE_HEADERS_FOOTERS and label_value in self.SKIP_LABELS:
                skipped_semantic += 1
                continue

            page_no = self._get_page_number(item)

            # ── Margin post-filter (bbox) ─────────────────────────
            if postfilter_margins and page_no in page_heights:
                if self._is_in_margin(item, page_height=page_heights[page_no]):
                    skipped_margin += 1
                    continue

            md_fragment = self._item_to_markdown(item, level)
            if md_fragment:
                page_contents[page_no].append(md_fragment)

        if skipped_semantic or skipped_margin:
            logger.info(
                f"Filtering '{source_name}': {total_elements} elements, "
                f"skipped {skipped_semantic} semantically + {skipped_margin} by margin"
            )

        return page_contents

    def _build_page_documents(
        self,
        doc,
        source_name: str,
        pages_info: Optional[List[PageInfo]],
        postfilter_margins: bool = False,
    ) -> List[Document]:
        """Builds a list of Documents split by page."""
        page_contents = self._collect_page_contents(doc, source_name, postfilter_margins)

        # ── Fallbacks ─────────────────────────────────────────────
        if page_contents and list(page_contents.keys()) == [0]:
            logger.warning(f"No page provenance in '{source_name}' -> single Document")
            return self._build_full_document(doc, source_name, pages_info)

        if pages_info is None:
            # No PyMuPDF -> no classification, only Docling's own pagination
            if not page_contents:
                logger.warning(f"No elements in '{source_name}' -> export_to_markdown() fallback")
                return self._build_full_document(doc, source_name, pages_info)
            return self._build_documents_unclassified(page_contents, source_name)

        return self._build_documents_classified(page_contents, pages_info, source_name)

    def _build_documents_classified(
        self,
        page_contents: Dict[int, List[str]],
        pages_info: List[PageInfo],
        source_name: str,
    ) -> List[Document]:
        """Combines Docling output with the page analysis into one Document per page."""
        documents: List[Document] = []
        blank_pages: List[int] = []
        non_text_pages: List[int] = []
        failed_pages: List[int] = []
        total_pages = len(pages_info)

        for info in pages_info:
            if info.kind == "blank":
                blank_pages.append(info.number)
                continue

            text = "\n\n".join(page_contents.get(info.number, [])).strip()
            page_type = info.kind
            method = "docling"

            if info.kind == "text":
                if not text:
                    # Fallback: text layer from PyMuPDF
                    text = info.plain_text
                    method = "pymupdf-text"
                if not text:
                    failed_pages.append(info.number)
                    continue
            else:  # 'scan' or 'drawing'
                if self._is_noise(text):
                    text = info.plain_text  # whatever short text exists, may be empty
                    method = "pymupdf-text"
                    page_type = "drawing"

            if not text:
                non_text_pages.append(info.number)
                if not INCLUDE_NON_TEXT_PAGES:
                    continue
                text = NON_TEXT_PLACEHOLDER
                method = "placeholder"

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "page_number": info.number,
                        "total_pages": total_pages,
                        "page_type": page_type,
                        "section_index": info.section_index,
                        "extraction_method": method,
                        "source": source_name,
                        "parser": "docling",
                        "headers_footers_removed": REMOVE_HEADERS_FOOTERS,
                    },
                )
            )

        if blank_pages:
            logger.info(f"Skipped blank pages {blank_pages} ({source_name})")
        if non_text_pages:
            logger.info(f"Pages without extractable text (plans/images) {non_text_pages} ({source_name})")
        if failed_pages:
            logger.warning(f"No text from pages {failed_pages} ({source_name})")

        return documents

    @staticmethod
    def _build_documents_unclassified(
        page_contents: Dict[int, List[str]], source_name: str
    ) -> List[Document]:
        """Fallback without PyMuPDF: only Docling's pagination (no page analysis)."""
        documents: List[Document] = []
        total_pages = max(page_contents.keys()) if page_contents else 0

        for page_no in sorted(page_contents.keys()):
            if page_no <= 0:
                continue
            content = "\n\n".join(page_contents[page_no]).strip()
            if not content:
                continue
            documents.append(
                Document(
                    page_content=content,
                    metadata={
                        "page_number": page_no,
                        "total_pages": total_pages,
                        "source": source_name,
                        "parser": "docling",
                        "headers_footers_removed": REMOVE_HEADERS_FOOTERS,
                    },
                )
            )
        return documents

    def _build_full_document(
        self, doc, source_name: str, pages_info: Optional[List[PageInfo]]
    ) -> List[Document]:
        """The whole document as a single Document (native Docling export)."""
        try:
            full_md = doc.export_to_markdown().strip()
        except Exception as e:
            logger.error(f"export_to_markdown() failed: {e}")
            return []

        if not full_md:
            return []

        if pages_info is not None:
            total_pages = len(pages_info)
        else:
            total_pages = len(doc.pages) if hasattr(doc, "pages") else 1

        return [
            Document(
                page_content=full_md,
                metadata={
                    "page_number": 1,
                    "total_pages": total_pages,
                    "source": source_name,
                    "parser": "docling",
                    "mode": "full_document",
                    "headers_footers_removed": REMOVE_HEADERS_FOOTERS,
                },
            )
        ]

    # ══════════════════════════════════════════════════════════════
    # HELPER METHODS
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _detect_device(use_gpu: bool) -> str:
        if not use_gpu:
            logger.info("GPU disabled -> CPU")
            return "cpu"

        if torch.cuda.is_available():
            name = torch.cuda.get_device_name(0)
            vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
            logger.info(f"GPU: {name} ({vram:.1f} GB VRAM)")
            return "cuda"
        if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            logger.info("Apple Silicon GPU (MPS)")
            return "mps"

        logger.warning("CUDA/MPS not available -> CPU")
        return "cpu"

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "memory stream (S3/RAM)"

    @staticmethod
    def _get_bytes(file_source: Union[str, io.BytesIO, bytes]) -> bytes:
        if isinstance(file_source, str):
            if not os.path.exists(file_source):
                raise FileNotFoundError(f"File does not exist: {file_source}")
            with open(file_source, "rb") as f:
                return f.read()
        if isinstance(file_source, bytes):
            return file_source
        if isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            return file_source.read()
        raise ValueError(f"Unsupported type: {type(file_source)}")

    @staticmethod
    def _prepare_source(file_source: Union[str, io.BytesIO, bytes]):
        """Source for Docling when PyMuPDF is unavailable."""
        if isinstance(file_source, str):
            if not os.path.exists(file_source):
                raise FileNotFoundError(f"File does not exist: {file_source}")
            return file_source

        if isinstance(file_source, bytes):
            return DocumentStream(name="document.pdf", stream=io.BytesIO(file_source))

        if isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            return DocumentStream(name="document.pdf", stream=file_source)

        raise ValueError(f"Unsupported type: {type(file_source)}")

    @staticmethod
    def _get_page_number(item) -> int:
        if hasattr(item, "prov") and item.prov:
            prov = item.prov[0]
            if hasattr(prov, "page_no"):
                return prov.page_no
        return 0

    @staticmethod
    def _item_to_markdown(item, level: int) -> Optional[str]:
        label = getattr(item, "label", None)
        label_value = label.value if hasattr(label, "value") else str(label)

        if label_value == "section_header":
            text = getattr(item, "text", "")
            if not text:
                return None
            heading_level = min(max(getattr(item, "level", level + 1), 1), 6)
            return f"{'#' * heading_level} {text}"

        if label_value == "title":
            text = getattr(item, "text", "")
            return f"# {text}" if text else None

        if label_value == "table":
            try:
                if hasattr(item, "data") and item.data is not None:
                    return item.data.export_to_markdown()
                if hasattr(item, "export_to_markdown"):
                    return item.export_to_markdown()
                return getattr(item, "text", None)
            except Exception:
                return getattr(item, "text", None)

        if label_value == "list_item":
            text = getattr(item, "text", "")
            return f"- {text}" if text else None

        if label_value == "code":
            text = getattr(item, "text", "")
            return f"```\n{text}\n```" if text else None

        if label_value == "formula":
            text = getattr(item, "text", "")
            return f"$$\n{text}\n$$" if text else None

        if label_value == "caption":
            text = getattr(item, "text", "")
            return f"*{text}*" if text else None

        if label_value == "footnote":
            text = getattr(item, "text", "")
            return f"> {text}" if text else None

        text = getattr(item, "text", None)
        if text and text.strip():
            return text.strip()

        return None

    @staticmethod
    def _cleanup_gpu():
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            torch.mps.empty_cache()