"""
docling_pdf_parser.py

PDF → Markdown parser based on IBM Docling with GPU acceleration.

Three-layer header/footer removal:
  1. PRE-CROP  — physical cropping of the margins (PyMuPDF cropbox)
  2. SEMANTIC  — Docling recognizes PAGE_HEADER / PAGE_FOOTER
  3. POST-FILTER — filter by bounding box position (fallback without pymupdf)

Requires:
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
    pip install docling easyocr langchain-core pymupdf
"""

import io
import logging
import os
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

# ── Optional dependency: PyMuPDF (for physical cropping) ──────
try:
    import pymupdf

    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False
    logger.info(
        "PyMuPDF (fitz) niedostępny → obcinanie marginesów przez post-filtr bbox. "
        "Dla najlepszych rezultatów zainstaluj: pip install pymupdf"
    )


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on IBM Docling with GPU acceleration
    and three-layer header/footer removal.

    Margins given in typographic points (1 pt = 1/72 inch).
    Standard A4 page: 595 × 842 pt.

    Typical values:
        top_margin_crop=50   — removes the header (~1.8 cm)
        bottom_margin_crop=60 — removes the footer with page numbering (~2.1 cm)
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
    ):
        """
        Args:
            use_gpu:              Whether to use GPU (auto-fallback to CPU).
            do_ocr:               Whether to run OCR (for scans).
            ocr_languages:        OCR languages (default ["pl", "en"]).
            table_mode:           "accurate" (GPU) or "fast" (ok on CPU).
            num_threads:          CPU threads.
            top_margin_crop:      Top margin to crop [pt].
            bottom_margin_crop:   Bottom margin to crop [pt].
            left_margin_crop:     Left margin to crop [pt].
            right_margin_crop:    Right margin to crop [pt].
        """
        # ── Margins────────────────────────────────────────────
        self._top_margin = top_margin_crop
        self._bottom_margin = bottom_margin_crop
        self._left_margin = left_margin_crop
        self._right_margin = right_margin_crop
        self._margins_enabled = any(
            [top_margin_crop, bottom_margin_crop, left_margin_crop, right_margin_crop]
        )

        if self._margins_enabled:
            crop_method = "pre-crop (PyMuPDF)" if FITZ_AVAILABLE else "post-filtr (bbox)"
            logger.info(
                f"Marginesy: top={top_margin_crop}pt, bottom={bottom_margin_crop}pt, "
                f"left={left_margin_crop}pt, right={right_margin_crop}pt | "
                f"metoda: {crop_method}"
            )

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

        # ── Tables────────────────────────────────────────────────
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

        # ── Converter─────────────────────────────────────────────
        logger.info("Ładowanie modeli Docling...")

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
            f"DoclingPdfParser gotowy | device={self._device} | "
            f"OCR={do_ocr} ({ocr_languages}) | tabele={table_mode}"
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
        Processes a PDF → list of Documents (Markdown, 1 page = 1 Document).

        Kwargs:
            full_document (bool): The whole document as a single Document.
                                  Default False.
        """
        full_document = kwargs.get("full_document", False)
        source_name = self._get_source_name(file_source)

        try:
            # ── 1. PRE-CROP of margins (PyMuPDF)─────────────────
            original_page_dims = None

            if self._margins_enabled and FITZ_AVAILABLE:
                logger.info(f"Pre-crop marginesów: {source_name}")
                cropped_stream, original_page_dims = self._precrop_pdf(file_source)
                conv_source = self._prepare_source(cropped_stream)
            else:
                conv_source = self._prepare_source(file_source)

            # ── 2. Docling conversion (GPU)────────────────────────
            logger.info(f"Konwersja Docling: {source_name}")
            result = self.converter.convert(conv_source)
            doc = result.document
            logger.info(f"Konwersja zakończona: {source_name}")

            # ── 3. Building the documents───────────────────────────
            # Bbox post-filter only when pymupdf is unavailable and margins are enabled
            use_postfilter = self._margins_enabled and not FITZ_AVAILABLE

            if full_document:
                documents = self._build_full_document(doc, source_name)
            else:
                documents = self._build_page_documents(
                    doc,
                    source_name,
                    postfilter_margins=use_postfilter,
                )

            # ── 4. Enriching the metadata with the original dimensions──
            if original_page_dims:
                for d in documents:
                    page_no = d.metadata.get("page_number", 1)
                    if page_no in original_page_dims:
                        dims = original_page_dims[page_no]
                        d.metadata["original_page_width_pt"] = dims[0]
                        d.metadata["original_page_height_pt"] = dims[1]
                    d.metadata["margin_top_pt"] = self._top_margin
                    d.metadata["margin_bottom_pt"] = self._bottom_margin

            # ── 5. Cleanup GPU ────────────────────────────────────
            self._cleanup_gpu()

            logger.info(f"Wynik: {len(documents)} dokumentów z '{source_name}'")
            return documents

        except Exception as e:
            logger.error(f"Błąd Docling ({source_name}): {e}", exc_info=True)
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
            "crop_method": "pre-crop (PyMuPDF)" if FITZ_AVAILABLE else "post-filtr (bbox)",
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
    ) -> Tuple[io.BytesIO, Dict[int, Tuple[float, float]]]:
        """
        Physical cropping of the margins using PyMuPDF cropbox.

        Docling will NEVER see the content in the margins — it will not
        process it, wasting no GPU compute on it.

        Returns:
            (cropped_pdf_stream, original_page_dimensions)
            original_page_dimensions: {page_no: (width, height)}
        """
        if isinstance(file_source, str):
            pdf_doc = pymupdf.Document(file_source)
        elif isinstance(file_source, bytes):
            pdf_doc = pymupdf.Document(stream=file_source, filetype="pdf")
        elif isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            pdf_doc = pymupdf.Document(stream=file_source.read(), filetype="pdf")
        else:
            raise ValueError(f"Nieobsługiwany typ: {type(file_source)}")

        original_dims: Dict[int, Tuple[float, float]] = {}
        pages_cropped = 0

        for page_idx, page in enumerate(pdf_doc):
            rect = page.rect  # Original dimensions (x0, y0, x1, y1)

            # Save the original dimensions
            original_dims[page_idx + 1] = (rect.width, rect.height)

            # Compute the new cropbox with validation
            new_x0 = rect.x0 + self._left_margin
            new_y0 = rect.y0 + self._top_margin
            new_x1 = rect.x1 - self._right_margin
            new_y1 = rect.y1 - self._bottom_margin

            # Validation: check that a sensible area remains after cropping
            remaining_width = new_x1 - new_x0
            remaining_height = new_y1 - new_y0

            if remaining_width < 100 or remaining_height < 100:
                logger.warning(
                    f"Strona {page_idx + 1}: marginesy zbyt duże "
                    f"(zostałoby {remaining_width:.0f}×{remaining_height:.0f} pt). "
                    f"Pomijam cropowanie tej strony."
                )
                continue

            new_rect = pymupdf.Rect(new_x0, new_y0, new_x1, new_y1)
            page.set_cropbox(new_rect)
            pages_cropped += 1

        logger.info(
            f"Pre-crop: przycięto {pages_cropped}/{len(pdf_doc)} stron "
            f"(top={self._top_margin}pt, bottom={self._bottom_margin}pt, "
            f"left={self._left_margin}pt, right={self._right_margin}pt)"
        )

        # Save the cropped PDF to memory
        output = io.BytesIO()
        pdf_doc.save(output)
        pdf_doc.close()
        output.seek(0)

        return output, original_dims

    # ══════════════════════════════════════════════════════════════
    # LAYER 3: POST-FILTER (provenance bounding box)
    # Fallback when PyMuPDF is unavailable
    # ══════════════════════════════════════════════════════════════

    def _is_in_margin(
        self, item, page_height: float, page_width: float
    ) -> bool:
        """
        Checks whether the element lies in the margin zone
        based on its provenance bounding box.

        Supports both Docling coordinate systems:
        - TOPLEFT:    (0,0) in the top-left corner
        - BOTTOMLEFT: (0,0) in the bottom-left corner
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
            is_topleft = origin_value in ("TOPLEFT", "topleft", None)

            if is_topleft:
                # TOPLEFT: small t = top of the page, large b = bottom of the page
                #   bbox.t = distance from the top to the element's top edge
                #   bbox.b = distance from the top to the element's bottom edge
                if self._top_margin > 0 and bbox.b <= self._top_margin:
                    return True  # The whole element is in the top margin
                if self._bottom_margin > 0 and bbox.t >= page_height - self._bottom_margin:
                    return True  # The whole element is in the bottom margin
                if self._left_margin > 0 and bbox.r <= self._left_margin:
                    return True
                if self._right_margin > 0 and bbox.l >= page_width - self._right_margin:
                    return True
            else:
                # BOTTOMLEFT: small b = bottom of the page, large t = top of the page
                if self._bottom_margin > 0 and bbox.t <= self._bottom_margin:
                    return True  # Element in the bottom margin
                if self._top_margin > 0 and bbox.b >= page_height - self._top_margin:
                    return True  # Element in the top margin
                if self._left_margin > 0 and bbox.r <= self._left_margin:
                    return True
                if self._right_margin > 0 and bbox.l >= page_width - self._right_margin:
                    return True

        except Exception as e:
            logger.debug(f"Błąd sprawdzania marginesu bbox: {e}")
            return False

        return False

    def _get_page_dimensions(self, doc) -> Dict[int, Tuple[float, float]]:
        """
        Gets the page dimensions from the Docling document.

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
    # BUILDING THE DOCUMENTS
    # ══════════════════════════════════════════════════════════════

    def _build_page_documents(
        self,
        doc,
        source_name: str,
        postfilter_margins: bool = False,
    ) -> List[Document]:
        """
        Builds a list of Documents split by page.

        Three-layer filtering:
        1. SKIP_LABELS (semantic — page_header / page_footer)
        2. Pre-crop (if applied earlier — the elements are already removed)
        3. Bbox post-filter (if postfilter_margins=True)
        """
        page_contents: Dict[int, List[str]] = defaultdict(list)

        # Page dimensions (for the post-filter)
        page_dims = self._get_page_dimensions(doc) if postfilter_margins else {}

        skipped_semantic = 0
        skipped_margin = 0
        total_elements = 0

        for item, level in doc.iterate_items():
            total_elements += 1
            label = getattr(item, "label", None)
            label_value = label.value if hasattr(label, "value") else str(label)

            # ── Layer 2: Semantic filter (SKIP_LABELS)───────
            if label_value in self.SKIP_LABELS:
                skipped_semantic += 1
                continue

            # Page number
            page_no = self._get_page_number(item)

            # ── Layer 3: Margin post-filter (bbox)──────────
            if postfilter_margins and page_no in page_dims:
                pw, ph = page_dims[page_no]
                if self._is_in_margin(item, page_height=ph, page_width=pw):
                    skipped_margin += 1
                    continue

            # Convert to Markdown
            md_fragment = self._item_to_markdown(item, level)
            if md_fragment:
                page_contents[page_no].append(md_fragment)

        # Logging the filtering statistics
        if skipped_semantic or skipped_margin:
            logger.info(
                f"Filtrowanie '{source_name}': "
                f"{total_elements} elementów, "
                f"pominięto {skipped_semantic} semantycznie + "
                f"{skipped_margin} marginesem"
            )

        # ── Fallbacks─────────────────────────────────────────────
        if not page_contents:
            logger.warning(f"Brak elementów w '{source_name}' → fallback export_to_markdown()")
            return self._build_full_document(doc, source_name)

        if list(page_contents.keys()) == [0]:
            logger.warning(f"Brak provenance stron w '{source_name}' → jeden Document")
            return self._build_full_document(doc, source_name)

        # ── Building the Document objects───────────────────────────
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
        """The whole document as a single Document (native Docling export)."""
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
    # HELPER METHODS
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _detect_device(use_gpu: bool) -> str:
        if not use_gpu:
            logger.info("GPU wyłączone → CPU")
            return "cpu"
        try:
            import torch

            if torch.cuda.is_available():
                name = torch.cuda.get_device_name(0)
                vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
                logger.info(f"GPU: {name} ({vram:.1f} GB VRAM)")
                return "cuda"
            elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                logger.info("Apple Silicon GPU (MPS)")
                return "mps"
            else:
                logger.warning("CUDA/MPS niedostępne → CPU")
                return "cpu"
        except ImportError:
            logger.warning("PyTorch nie zainstalowany → CPU")
            return "cpu"

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "strumień pamięci (S3/RAM)"

    @staticmethod
    def _prepare_source(file_source: Union[str, io.BytesIO, bytes]):

        if isinstance(file_source, str):
            if not os.path.exists(file_source):
                raise FileNotFoundError(f"Plik nie istnieje: {file_source}")
            return file_source

        if isinstance(file_source, bytes):
            return DocumentStream(name="document.pdf", stream=io.BytesIO(file_source))

        if isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            return DocumentStream(name="document.pdf", stream=file_source)

        raise ValueError(f"Nieobsługiwany typ: {type(file_source)}")

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
        try:
            import torch

            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        except ImportError:
            pass