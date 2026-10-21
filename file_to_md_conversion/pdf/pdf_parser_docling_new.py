"""
docling_pdf_parser.py

PDF → Markdown parser based on IBM Docling with GPU acceleration.

Three-layer removal of page headers/footers:
  1. PRE-CROP    — physical margin trimming (PyMuPDF cropbox)
  2. SEMANTIC    — Docling recognizes PAGE_HEADER / PAGE_FOOTER
  3. POST-FILTER — bounding-box position filter (fallback / pages
                   that could not be physically cropped)

Table handling: native Docling export (TableFormer) → markdown.
Image handling (e.g. store planogram layouts): optional export to
PNG files + link in the markdown (images_output_dir parameter).

Requirements:
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
    pip install docling easyocr langchain-core pymupdf pillow
"""

import io
import logging
import os
import re
from collections import defaultdict
from typing import Dict, List, Optional, Tuple, Union

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
import torch
from langchain_core.documents import Document

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# ── Optional dependency: PyMuPDF (for physical cropping) ──────────
try:
    import pymupdf

    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False
    logger.info(
        "PyMuPDF (fitz) not available → margin trimming via bbox post-filter. "
        "For best results install: pip install pymupdf"
    )


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on IBM Docling with GPU acceleration
    and three-layer header/footer removal.

    Margins are given in typographic points (1 pt = 1/72 inch).
    Standard A4 page: 595 × 842 pt.

    Typical values:
        top_margin_crop=50    — removes header (~1.8 cm)
        bottom_margin_crop=60 — removes footer with page numbers (~2.1 cm)
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
        top_margin_crop: float = 50.0,
        bottom_margin_crop: float = 60.0,
        left_margin_crop: float = 0.0,
        right_margin_crop: float = 0.0,
        images_output_dir: Optional[str] = None,  # FIX: image handling
        images_scale: float = 2.0,  # FIX: resolution of exported images
    ):
        """
        Args:
            use_gpu:              Whether to use GPU (auto-fallback to CPU).
            do_ocr:                Whether to run OCR (for scans).
            ocr_languages:         OCR languages (default ["pl", "en"]).
            table_mode:            "accurate" (GPU) or "fast" (CPU ok).
            num_threads:           CPU threads.
            top_margin_crop:       Top margin to trim [pt].
            bottom_margin_crop:    Bottom margin to trim [pt].
            left_margin_crop:      Left margin to trim [pt].
            right_margin_crop:     Right margin to trim [pt].
            images_output_dir:     Directory to save images (e.g. store
                                   layout plans). If None, images will
                                   appear as placeholders without a
                                   saved file.
            images_scale:          Image rendering scale (higher means
                                   better quality, but slower/more RAM).
        """
        # ── Margins ──────────────────────────────────────────────
        self._top_margin = top_margin_crop
        self._bottom_margin = bottom_margin_crop
        self._left_margin = left_margin_crop
        self._right_margin = right_margin_crop
        self._margins_enabled = any(
            [top_margin_crop, bottom_margin_crop, left_margin_crop, right_margin_crop]
        )
        self._coord_origin_warned = False  # FIX: one-time warning flag

        if self._margins_enabled:
            crop_method = "pre-crop (PyMuPDF)" if FITZ_AVAILABLE else "post-filter (bbox)"
            logger.info(
                f"Margins: top={top_margin_crop}pt, bottom={bottom_margin_crop}pt, "
                f"left={left_margin_crop}pt, right={right_margin_crop}pt | "
                f"method: {crop_method}"
            )

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

        # FIX: generate images only if we actually want to save them
        if images_output_dir:
            try:
                pipeline_options.generate_picture_images = True
                pipeline_options.images_scale = images_scale
            except AttributeError:
                logger.warning(
                    "This Docling version does not support generate_picture_images/"
                    "images_scale — images will only be placeholders."
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
        Processes a PDF → list of Document objects (Markdown, 1 page = 1 Document).

        Kwargs:
            full_document (bool): Whole document as a single Document.
                                  Default False.
        """
        full_document = kwargs.get("full_document", False)
        source_name = self._get_source_name(file_source)

        try:
            # ── 1. PRE-CROP margins (PyMuPDF) ────────────────────
            original_page_dims = None
            postfilter_pages: Optional[set] = set()  # empty set = no filter needed

            if self._margins_enabled:
                if FITZ_AVAILABLE:
                    logger.info(f"Pre-cropping margins: {source_name}")
                    cropped_stream, original_page_dims, uncropped_pages = (
                        self._precrop_pdf(file_source)
                    )
                    conv_source = self._prepare_source(cropped_stream)
                    # FIX: post-filter only for pages that could NOT be
                    # physically cropped (validation rejected an oversized margin)
                    postfilter_pages = uncropped_pages
                    if uncropped_pages:
                        logger.warning(
                            f"Pages without physical cropping (bbox post-filter "
                            f"will apply): {sorted(uncropped_pages)}"
                        )
                else:
                    conv_source = self._prepare_source(file_source)
                    # None = apply post-filter to ALL pages
                    postfilter_pages = None
            else:
                conv_source = self._prepare_source(file_source)

            # ── 2. Docling conversion (GPU) ──────────────────────
            logger.info(f"Docling conversion: {source_name}")
            result = self.converter.convert(conv_source)
            doc = result.document
            logger.info(f"Conversion finished: {source_name}")

            # ── 3. Building documents ─────────────────────────────
            if full_document:
                documents = self._build_full_document(doc, source_name)
            else:
                documents = self._build_page_documents(
                    doc,
                    source_name,
                    postfilter_pages=postfilter_pages,
                )

            # ── 4. Enriching metadata with original dimensions ───
            if original_page_dims:
                for d in documents:
                    page_no = d.metadata.get("page_number", 1)
                    if page_no in original_page_dims:
                        dims = original_page_dims[page_no]
                        d.metadata["original_page_width_pt"] = dims[0]
                        d.metadata["original_page_height_pt"] = dims[1]
                    d.metadata["margin_top_pt"] = self._top_margin
                    d.metadata["margin_bottom_pt"] = self._bottom_margin

            # ── 5. GPU cleanup ────────────────────────────────────
            self._cleanup_gpu()

            logger.info(f"Result: {len(documents)} documents from '{source_name}'")
            return documents

        except Exception as e:
            logger.error(f"Docling error ({source_name}): {e}", exc_info=True)
            self._cleanup_gpu()
            return []

    def diagnostics(self) -> Dict[str, str]:
        """Diagnostic information."""

        info = {
            "device": self._device,
            "ocr": str(self._do_ocr),
            "table_mode": self._table_mode,
            "margins_enabled": str(self._margins_enabled),
            "margin_top_pt": str(self._top_margin),
            "margin_bottom_pt": str(self._bottom_margin),
            "margin_left_pt": str(self._left_margin),
            "margin_right_pt": str(self._right_margin),
            "crop_method": "pre-crop (PyMuPDF)" if FITZ_AVAILABLE else "post-filter (bbox)",
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
    # LAYER 1: PRE-CROP (PyMuPDF cropbox)
    # ══════════════════════════════════════════════════════════════

    def _precrop_pdf(
        self, file_source: Union[str, io.BytesIO, bytes]
    ) -> Tuple[io.BytesIO, Dict[int, Tuple[float, float]], set]:
        """
        Physically trims margins using the PyMuPDF cropbox.

        Docling will NEVER see content within the margins on pages
        that were successfully cropped — it will not process it and
        will not waste GPU compute on it.

        Returns:
            (cropped_pdf_stream, original_page_dimensions, uncropped_pages)
            original_page_dimensions: {page_no: (width, height)}
            uncropped_pages: set of page numbers that were NOT cropped
                             (because validation rejected oversized margins)
        """
        if isinstance(file_source, str):
            pdf_doc = pymupdf.Document(file_source)
        elif isinstance(file_source, bytes):
            pdf_doc = pymupdf.Document(stream=file_source, filetype="pdf")
        elif isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            pdf_doc = pymupdf.Document(stream=file_source.read(), filetype="pdf")
        else:
            raise ValueError(f"Unsupported type: {type(file_source)}")

        original_dims: Dict[int, Tuple[float, float]] = {}
        uncropped_pages: set = set()  # FIX: tracking pages without cropping
        pages_cropped = 0

        for page_idx, page in enumerate(pdf_doc):
            rect = page.rect  # Original dimensions (x0, y0, x1, y1)
            page_no = page_idx + 1

            # Save original dimensions
            original_dims[page_no] = (rect.width, rect.height)

            # Calculate new cropbox with validation
            new_x0 = rect.x0 + self._left_margin
            new_y0 = rect.y0 + self._top_margin
            new_x1 = rect.x1 - self._right_margin
            new_y1 = rect.y1 - self._bottom_margin

            # Validation: check if a reasonable area remains after cropping
            remaining_width = new_x1 - new_x0
            remaining_height = new_y1 - new_y0

            if remaining_width < 100 or remaining_height < 100:
                logger.warning(
                    f"Page {page_no}: margins too large "
                    f"(would leave {remaining_width:.0f}×{remaining_height:.0f} pt). "
                    f"Skipping cropping for this page (bbox post-filter will be used instead)."
                )
                uncropped_pages.add(page_no)  # FIX
                continue

            new_rect = pymupdf.Rect(new_x0, new_y0, new_x1, new_y1)
            page.set_cropbox(new_rect)
            pages_cropped += 1

        logger.info(
            f"Pre-crop: cropped {pages_cropped}/{len(pdf_doc)} pages "
            f"(top={self._top_margin}pt, bottom={self._bottom_margin}pt, "
            f"left={self._left_margin}pt, right={self._right_margin}pt)"
        )

        # Save the cropped PDF to memory
        output = io.BytesIO()
        pdf_doc.save(output)
        pdf_doc.close()
        output.seek(0)

        return output, original_dims, uncropped_pages

    # ══════════════════════════════════════════════════════════════
    # LAYER 3: POST-FILTER (provenance bounding box)
    # Fallback when PyMuPDF is unavailable OR for pages that could
    # not be physically cropped
    # ══════════════════════════════════════════════════════════════

    def _is_in_margin(
        self, item, page_height: float, page_width: float
    ) -> bool:
        """
        Checks whether an element lies within the margin zone based
        on its bounding box from provenance.

        Supports both Docling coordinate systems:
        - TOPLEFT:    (0,0) at the top-left corner
        - BOTTOMLEFT: (0,0) at the bottom-left corner
        """
        if not hasattr(item, "prov") or not item.prov:
            return False

        try:
            bbox = item.prov[0].bbox

            # Read the coordinate system
            coord_origin = getattr(bbox, "coord_origin", None)
            origin_value = (
                coord_origin.value
                if hasattr(coord_origin, "value")
                else str(coord_origin)
            )

            # FIX: explicit warning instead of a silent assumption
            if coord_origin is None and not self._coord_origin_warned:
                logger.warning(
                    "Element coord_origin is None — assuming TOPLEFT. "
                    "Verify this assumption against a sample of your own "
                    "documents (check the actual bbox.coord_origin values)!"
                )
                self._coord_origin_warned = True

            is_topleft = origin_value in ("TOPLEFT", "topleft", None)

            if is_topleft:
                # TOPLEFT: small t = top of page, large b = bottom of page
                if self._top_margin > 0 and bbox.b <= self._top_margin:
                    return True  # Entire element in the top margin
                if self._bottom_margin > 0 and bbox.t >= page_height - self._bottom_margin:
                    return True  # Entire element in the bottom margin
                if self._left_margin > 0 and bbox.r <= self._left_margin:
                    return True
                if self._right_margin > 0 and bbox.l >= page_width - self._right_margin:
                    return True
            else:
                # BOTTOMLEFT: small b = bottom of page, large t = top of page
                if self._bottom_margin > 0 and bbox.t <= self._bottom_margin:
                    return True  # Element in the bottom margin
                if self._top_margin > 0 and bbox.b >= page_height - self._top_margin:
                    return True  # Element in the top margin
                if self._left_margin > 0 and bbox.r <= self._left_margin:
                    return True
                if self._right_margin > 0 and bbox.l >= page_width - self._right_margin:
                    return True

        except Exception as e:
            logger.debug(f"Error checking bbox margin: {e}")
            return False

        return False

    def _get_page_dimensions(self, doc) -> Dict[int, Tuple[float, float]]:
        """
        Retrieves page dimensions from the Docling document.

        Returns:
            {page_no: (width, height)}
        """
        dims: Dict[int, Tuple[float, float]] = {}

        if hasattr(doc, "pages"):
            for page_no, page_item in doc.pages.items():
                if hasattr(page_item, "size") and page_item.size:
                    dims[page_no] = (page_item.size.width, page_item.size.height)

        return dims

    # ══════════════════════════════════════════════════════════════
    # DOCUMENT BUILDING
    # ══════════════════════════════════════════════════════════════

    def _build_page_documents(
        self,
        doc,
        source_name: str,
        postfilter_pages: Optional[set] = None,
    ) -> List[Document]:
        """
        Builds a list of Document objects split by page.

        Three-layer filtering:
        1. SKIP_LABELS (semantic — page_header / page_footer)
        2. Pre-crop (if applied earlier — elements already removed)
        3. Post-filter bbox:
           - postfilter_pages is None  → filter applied to ALL pages
             (no PyMuPDF)
           - postfilter_pages = {...}  → filter applied only to the
             listed pages (pages that could not be physically cropped)
           - postfilter_pages = set()  → filter completely disabled
        """
        page_contents: Dict[int, List[str]] = defaultdict(list)

        do_postfilter_any = postfilter_pages is None or len(postfilter_pages) > 0
        page_dims = self._get_page_dimensions(doc) if do_postfilter_any else {}

        skipped_semantic = 0
        skipped_margin = 0
        skipped_no_page = 0  # FIX: counter for elements without a page number
        total_elements = 0
        image_counter = [0]  # FIX: counter for naming exported images

        # FIX: with_groups=True so nested content inside groups is not
        # lost, with a fallback for older Docling versions without
        # this parameter
        try:
            items_iter = doc.iterate_items(with_groups=True)
        except TypeError:
            items_iter = doc.iterate_items()

        for item, level in items_iter:
            total_elements += 1
            label = getattr(item, "label", None)
            label_value = label.value if hasattr(label, "value") else str(label)

            # ── Layer 2: Semantic filter (SKIP_LABELS) ───────────
            if label_value in self.SKIP_LABELS:
                skipped_semantic += 1
                continue

            # Page number
            page_no = self._get_page_number(item)

            if page_no <= 0:
                # FIX: log instead of silently losing it — we still
                # try to render the content, it will land on "page 0"
                # and be discarded at assembly time (see below)
                skipped_no_page += 1
            else:
                # ── Layer 3: Margin post-filter (bbox) ────────────
                needs_postfilter = (
                    postfilter_pages is None or page_no in postfilter_pages
                )
                if needs_postfilter and page_no in page_dims:
                    pw, ph = page_dims[page_no]
                    if self._is_in_margin(item, page_height=ph, page_width=pw):
                        skipped_margin += 1
                        continue

            # Convert to Markdown
            md_fragment = self._item_to_markdown(
                item, level, doc, page_no, source_name, image_counter
            )
            if md_fragment:
                page_contents[page_no].append(md_fragment)

        # Log filtering statistics
        if skipped_semantic or skipped_margin or skipped_no_page:
            logger.info(
                f"Filtering '{source_name}': "
                f"{total_elements} elements, "
                f"skipped {skipped_semantic} semantically + "
                f"{skipped_margin} by margin, "
                f"{skipped_no_page} without a page number (lost at assembly)"
            )

        # ── Fallbacks ────────────────────────────────────────────
        if not page_contents:
            logger.warning(f"No elements in '{source_name}' → fallback to export_to_markdown()")
            return self._build_full_document(doc, source_name)

        if list(page_contents.keys()) == [0]:
            logger.warning(f"No page provenance in '{source_name}' → single Document")
            return self._build_full_document(doc, source_name)

        # ── Building Document objects ───────────────────────────
        documents = []
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
                    },
                )
            )

        return documents

    def _build_full_document(self, doc, source_name: str) -> List[Document]:
        """Whole document as a single Document (native Docling export)."""
        try:
            full_md = doc.export_to_markdown().strip()
        except Exception as e:
            logger.error(f"export_to_markdown() failed: {e}")
            return []

        if not full_md:
            return []

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
                },
            )
        ]

    # ══════════════════════════════════════════════════════════════
    # HELPER METHODS — ELEMENT CONVERSION
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
        """
        Converts a single Docling element to a markdown fragment.

        FIX: no longer a @staticmethod — needs self (access to
        images_output_dir) and doc (needed for proper table export
        and image retrieval).
        """
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
            return self._table_to_markdown(item, doc)

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

        return None

    def _table_to_markdown(self, item, doc) -> Optional[str]:
        """
        FIX: Corrected table export.

        The previous version called `item.data.export_to_markdown()`
        (TableData does not have this method → always raised an
        exception → silently fell through to `item.text`, i.e. the
        table structure was lost). The correct method is
        `item.export_to_markdown(doc)` on the TableItem object.
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
                "Table exported as plain text — STRUCTURE LOST. "
                "Check the Docling version / TableFormer quality on this page."
            )
            return text.strip()

        logger.error("Table could not be exported in any way — skipping.")
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
        FIX: New image handling (e.g. store layout plans).

        Without this method, images were completely dropped from the
        markdown output (no .text attribute → no trace at all in the
        output).

        If images_output_dir is set, saves the image as a PNG and
        inserts a markdown link. Otherwise inserts a placeholder with
        a caption (if available).
        """
        caption = ""
        try:
            if hasattr(item, "caption_text"):
                caption = item.caption_text(doc) or ""
        except Exception:
            caption = ""

        if not self._images_output_dir:
            alt = caption or f"image (page {page_no}) — set images_output_dir to export the file"
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
    # HELPER METHODS — GENERAL
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _detect_device(use_gpu: bool) -> str:
        if not use_gpu:
            logger.info("GPU disabled → CPU")
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
                logger.warning("CUDA/MPS not available → CPU")
                return "cpu"
        except Exception as e:
            logger.warning(f"GPU detection failed ({e}) → CPU")
            return "cpu"

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "in-memory stream (S3/RAM)"

    @staticmethod
    def _prepare_source(file_source: Union[str, io.BytesIO, bytes]):

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
                # FIX: clear cache for Apple Silicon (MPS) as well
                if hasattr(torch, "mps") and hasattr(torch.mps, "empty_cache"):
                    torch.mps.empty_cache()
        except Exception:
            pass