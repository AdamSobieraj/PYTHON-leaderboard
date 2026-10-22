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

Table handling: native Docling export (TableFormer) -> markdown.
Table of contents (Docling label "document_index") is a TableItem and is
exported the same way as tables.
Image handling (e.g. plans, layouts): optional export to PNG files + link in
the markdown (images_output_dir parameter).

Requirements:
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
    pip install docling easyocr langchain-core pymupdf pillow
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

# ── TableItem: detect tables by type (covers the "document_index" label) ──
try:
    from docling_core.types.doc import TableItem
except ImportError:
    TableItem = None

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

# Markdown image links: any link / only links with a real (non-empty) path
_MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_MD_EXPORTED_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")


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
       - drawing -> placeholder (plan / image without text); exported image
                    links are kept if images_output_dir is set,
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
        images_output_dir: Optional[str] = None,
        images_scale: float = 2.0,
    ):
        """
        Args:
            use_gpu:             Whether to use GPU (auto-fallback to CPU).
            do_ocr:              Whether to run OCR (for scans).
            ocr_languages:       OCR languages (default ["pl", "en"]).
            table_mode:          "accurate" (GPU) or "fast" (CPU ok).
            num_threads:         CPU threads.
            images_output_dir:   Directory to save images (e.g. plans, layouts).
                                 If None, images appear as placeholders without
                                 a saved file.
            images_scale:        Image rendering scale (higher means better
                                 quality, but slower / more RAM).
        """
        if REMOVE_HEADERS_FOOTERS:
            if FITZ_AVAILABLE:
                logger.info(
                    f"Header/footer removal: ON (mode={HEADER_FOOTER_MODE}, "
                    f"method: PyMuPDF redaction)"
                )
            else:
                logger.info(
                    "Header/footer removal: ON, but PyMuPDF is missing -> "
                    "semantic filter only"
                    + (" + bbox post-filter" if HEADER_FOOTER_MODE == "fixed" else "")
                )
        else:
            logger.info("Header/footer removal: OFF")

        self._coord_origin_warned = False  # one-time warning flag

        # ── Images ───────────────────────────────────────────────
        self._images_output_dir = images_output_dir
        self._images_scale = images_scale
        if images_output_dir:
            os.makedirs(images_output_dir, exist_ok=True)
            logger.info(f"Images will be saved to: {images_output_dir}")

        # ── GPU ──────────────────────────────────────────────────
        self._device = self._detect_device(use_gpu)

        accelerator = AcceleratorOptions(
            num_threads=num_threads,
            device=(
                AcceleratorDevice.CUDA
                if self._device == "cuda"
                else AcceleratorDevice.CPU
            ),
        )

        # ── Tables ───────────────────────────────────────────────
        table_structure = TableStructureOptions(
            mode=(
                TableFormerMode.ACCURATE
                if table_mode == "accurate"
                else TableFormerMode.FAST
            ),
        )

        # ── OCR ──────────────────────────────────────────────────
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

        # Generate picture images only if we actually want to save them
        if images_output_dir:
            try:
                pipeline_options.generate_picture_images = True
                pipeline_options.images_scale = images_scale
            except AttributeError:
                logger.warning(
                    "This Docling version does not support generate_picture_images/"
                    "images_scale - images will only be placeholders."
                )

        # ── Converter ────────────────────────────────────────────
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
            full_document (bool): Whole document as a single Document.
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

                pages_modified = 0
                if REMOVE_HEADERS_FOOTERS:
                    logger.info(f"Removing headers/footers: {source_name}")
                    pages_modified = self._remove_headers_footers(pdf_doc)

                # Classification runs AFTER removal, so a page that contained only
                # a page number becomes 'blank'
                pages_info = self._analyze_pages(pdf_doc)

                if all(p.kind == "blank" for p in pages_info):
                    logger.warning(f"All pages are blank in '{source_name}'")
                    return []

                pdf_to_process = pdf_doc.tobytes() if pages_modified else raw_bytes
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
            "images_output_dir": str(self._images_output_dir),
            "images_scale": str(self._images_scale),
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

    @staticmethod
    def _strip_images(text: str) -> str:
        """Text without markdown image links (placeholders and exported files)."""
        return _MD_IMAGE_RE.sub("", text or "").strip()

    @staticmethod
    def _exported_image_refs(text: str) -> str:
        """Only the image links that point to a real exported file."""
        return "\n\n".join(_MD_EXPORTED_IMAGE_RE.findall(text or ""))

    # ══════════════════════════════════════════════════════════════
    # HEADER / FOOTER REMOVAL (PyMuPDF redaction)
    # ══════════════════════════════════════════════════════════════

    def _remove_headers_footers(self, pdf_doc: "pymupdf.Document") -> int:
        """
        Removes headers / footers by redaction (behaves the same for every
        extraction engine). Pages are never deleted, so page numbers stay
        aligned with the original file.

        Returns the number of modified pages.
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
        return pages_redacted

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
        Checks whether an element lies within the top/bottom margin zone
        based on its bounding box from provenance.

        Supports both Docling coordinate systems:
        - TOPLEFT:    (0,0) at the top-left corner
        - BOTTOMLEFT: (0,0) at the bottom-left corner
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

            # Explicit warning instead of a silent assumption
            if coord_origin is None and not self._coord_origin_warned:
                logger.warning(
                    "Element coord_origin is None - assuming TOPLEFT. "
                    "Verify this assumption against a sample of your own "
                    "documents (check the actual bbox.coord_origin values)!"
                )
                self._coord_origin_warned = True

            is_topleft = origin_value in ("TOPLEFT", "topleft", None)

            if is_topleft:
                # TOPLEFT: small t = top of page, large b = bottom of page
                if bbox.b <= FIXED_TOP_MARGIN_PT:
                    return True  # entire element in the top margin
                if bbox.t >= page_height - FIXED_BOTTOM_MARGIN_PT:
                    return True  # entire element in the bottom margin
            else:
                # BOTTOMLEFT: small b = bottom of page, large t = top of page
                if bbox.t <= FIXED_BOTTOM_MARGIN_PT:
                    return True  # element in the bottom margin
                if bbox.b >= page_height - FIXED_TOP_MARGIN_PT:
                    return True  # element in the top margin

        except Exception as e:
            logger.debug(f"Error checking bbox margin: {e}")
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
    # DOCUMENT BUILDING
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _iter_items(doc):
        """
        Iterates over the Docling items with with_groups=True (so nested content
        inside groups is not lost). When header/footer removal is OFF, tries to
        include the 'furniture' layer too (page headers/footers live there and
        newer Docling versions skip it by default). Falls back gracefully for
        older Docling versions that lack these arguments.
        """
        kwargs = {"with_groups": True}
        if not REMOVE_HEADERS_FOOTERS and ContentLayer is not None:
            kwargs["included_content_layers"] = {
                ContentLayer.BODY,
                ContentLayer.FURNITURE,
            }

        try:
            return doc.iterate_items(**kwargs)
        except TypeError:
            pass

        try:
            return doc.iterate_items(with_groups=True)
        except TypeError:
            return doc.iterate_items()

    def _collect_page_contents(
        self, doc, source_name: str, postfilter_margins: bool
    ) -> Dict[int, List[str]]:
        """Converts Docling items to Markdown fragments grouped by page."""
        page_contents: Dict[int, List[str]] = defaultdict(list)
        page_heights = self._get_page_heights(doc) if postfilter_margins else {}

        skipped_semantic = 0
        skipped_margin = 0
        skipped_no_page = 0  # elements without a page number
        total_elements = 0
        image_counter = [0]  # counter for naming exported images

        for item, level in self._iter_items(doc):
            total_elements += 1
            label = getattr(item, "label", None)
            label_value = label.value if hasattr(label, "value") else str(label)

            # Diagnostic log (switch to debug / remove once verified)
            logger.info(
                f"item p{self._get_page_number(item)} "
                f"label={label_value} type={type(item).__name__}"
            )

            # ── Semantic filter (page_header / page_footer) ──────
            if REMOVE_HEADERS_FOOTERS and label_value in self.SKIP_LABELS:
                skipped_semantic += 1
                continue

            page_no = self._get_page_number(item)

            if page_no <= 0:
                # Rendered anyway, lands on "page 0" and is dropped at assembly
                skipped_no_page += 1
            elif postfilter_margins and page_no in page_heights:
                # ── Margin post-filter (bbox) ─────────────────────
                if self._is_in_margin(item, page_height=page_heights[page_no]):
                    skipped_margin += 1
                    continue

            md_fragment = self._item_to_markdown(
                item, level, doc, page_no, source_name, image_counter
            )
            if md_fragment:
                page_contents[page_no].append(md_fragment)

        if skipped_semantic or skipped_margin or skipped_no_page:
            logger.info(
                f"Filtering '{source_name}': {total_elements} elements, "
                f"skipped {skipped_semantic} semantically + {skipped_margin} by margin, "
                f"{skipped_no_page} without a page number (lost at assembly)"
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
                logger.warning(
                    f"No elements in '{source_name}' -> export_to_markdown() fallback"
                )
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
            body = self._strip_images(text)   # text without image links
            image_refs = self._exported_image_refs(text)
            page_type = info.kind
            method = "docling"

            if info.kind == "text":
                if not body:
                    # Fallback: text layer from PyMuPDF (+ exported image links)
                    text = "\n\n".join(p for p in (info.plain_text, image_refs) if p)
                    method = "pymupdf-text"
                if not self._strip_images(text):
                    failed_pages.append(info.number)
                    continue
            else:  # 'scan' or 'drawing'
                if self._is_noise(body):
                    # OCR garbage: keep whatever short text exists + image links
                    text = "\n\n".join(p for p in (info.plain_text, image_refs) if p)
                    method = "pymupdf-text"
                    page_type = "drawing"

                if not self._strip_images(text):
                    # Nothing but (possibly) image links
                    non_text_pages.append(info.number)
                    if INCLUDE_NON_TEXT_PAGES:
                        text = f"{NON_TEXT_PLACEHOLDER}\n\n{text}".strip()
                        method = "placeholder"
                    elif text:
                        method = "image-only"
                    else:
                        continue

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
            logger.info(
                f"Pages without extractable text (plans/images) {non_text_pages} ({source_name})"
            )
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
        """Whole document as a single Document (native Docling export)."""
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
    # HELPER METHODS - ELEMENT CONVERSION
    # ══════════════════════════════════════════════════════════════

    def _item_to_markdown(
        self,
        item,
        level: int,
        doc,
        page_no: int,
        source_name: str,
        image_counter: List[int],
    ) -> Optional[str]:
        """Converts a single Docling element to a markdown fragment."""
        label = getattr(item, "label", None)
        label_value = label.value if hasattr(label, "value") else str(label)

        # Tables AND table of contents (label "document_index" is a TableItem)
        is_table = (
            (TableItem is not None and isinstance(item, TableItem))
            or label_value in ("table", "document_index")
        )
        if is_table:
            return self._table_to_markdown(item, doc)

        if label_value == "section_header":
            text = getattr(item, "text", "")
            if not text:
                return None
            heading_level = min(max(getattr(item, "level", level + 1), 1), 6)
            return f"{'#' * heading_level} {text}"

        if label_value == "title":
            text = getattr(item, "text", "")
            return f"# {text}" if text else None

        if label_value == "picture":
            return self._picture_to_markdown(
                item, doc, page_no, source_name, image_counter
            )

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

        # Items without a text field (e.g. unknown floating items): native export
        if hasattr(item, "export_to_markdown"):
            try:
                md = item.export_to_markdown(doc)
                if md and md.strip():
                    return md.strip()
            except Exception:
                pass

        logger.debug(
            f"Dropped item: label={label_value}, page={page_no}, "
            f"type={type(item).__name__}"
        )
        return None

    def _table_to_markdown(self, item, doc) -> Optional[str]:
        """
        Table export: the correct method is `item.export_to_markdown(doc)` on the
        TableItem (TableData has no such method, so the structure would be lost).
        """
        try:
            md = item.export_to_markdown(doc)
            if md and md.strip():
                return md.strip()
        except Exception as e:
            logger.warning(
                f"TableItem.export_to_markdown(doc) failed ({e}), "
                f"trying fallback via TableData"
            )

        try:
            if (
                hasattr(item, "data")
                and item.data is not None
                and hasattr(item.data, "export_to_markdown")
            ):
                md = item.data.export_to_markdown()
                if md and md.strip():
                    return md.strip()
        except Exception as e:
            logger.warning(f"Fallback export_to_markdown() on TableData also failed ({e})")

        text = getattr(item, "text", None)
        if text:
            logger.warning(
                "Table exported as plain text - STRUCTURE LOST. "
                "Check the Docling version / TableFormer quality on this page."
            )
            return text.strip()

        logger.error("Table could not be exported in any way - skipping.")
        return None

    def _picture_to_markdown(
        self,
        item,
        doc,
        page_no: int,
        source_name: str,
        image_counter: List[int],
    ) -> Optional[str]:
        """
        Image handling (e.g. plans, layouts).

        If images_output_dir is set, saves the image as a PNG and inserts a
        markdown link. Otherwise inserts a placeholder with a caption (if any).
        """
        caption = ""
        try:
            if hasattr(item, "caption_text"):
                caption = item.caption_text(doc) or ""
        except Exception:
            caption = ""

        if not self._images_output_dir:
            alt = caption or f"image (page {page_no}) - set images_output_dir to export the file"
            return f"![{alt}]()"

        try:
            pil_image = item.get_image(doc)
            if pil_image is None:
                logger.warning(f"item.get_image(doc) returned None on page {page_no}")
                alt = caption or f"image, page {page_no}"
                return f"![{alt}]()"

            image_counter[0] += 1
            safe_source = re.sub(r"[^\w\-.]", "_", os.path.splitext(source_name)[0])
            filename = f"{safe_source}_p{page_no}_img{image_counter[0]}.png"
            filepath = os.path.join(self._images_output_dir, filename)
            pil_image.save(filepath)

            alt = caption or "image"
            return f"![{alt}]({filepath})"

        except Exception as e:
            logger.warning(f"Could not save image (page {page_no}): {e}")
            alt = caption or f"image, page {page_no}"
            return f"![{alt}]()"

    # ══════════════════════════════════════════════════════════════
    # HELPER METHODS - GENERAL
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _detect_device(use_gpu: bool) -> str:
        if not use_gpu:
            logger.info("GPU disabled -> CPU")
            return "cpu"
        try:
            if torch.cuda.is_available():
                name = torch.cuda.get_device_name(0)
                vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
                logger.info(f"GPU: {name} ({vram:.1f} GB VRAM)")
                return "cuda"
            elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                logger.info("Apple Silicon GPU (MPS)")
                return "mps"
            else:
                logger.warning("CUDA/MPS not available -> CPU")
                return "cpu"
        except Exception as e:
            logger.warning(f"GPU detection failed ({e}) -> CPU")
            return "cpu"

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "in-memory stream (S3/RAM)"

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
    def _cleanup_gpu():
        try:
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                # Clear cache for Apple Silicon (MPS) as well
                if hasattr(torch, "mps") and hasattr(torch.mps, "empty_cache"):
                    torch.mps.empty_cache()
        except Exception:
            pass