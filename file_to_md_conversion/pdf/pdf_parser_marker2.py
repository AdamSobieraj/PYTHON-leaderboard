import io
import logging
import os
import re
import tempfile
import threading
from typing import Dict, List, Union

import torch
from langchain_core.documents import Document

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

try:
    import pymupdf  # PyMuPDF
    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False
    logger.warning("PyMuPDF not available! Margin removal will not work.")

try:
    # API for newer Marker-PDF versions (v1.0+)
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.config.parser import ConfigParser
    MARKER_AVAILABLE = True
except ImportError:
    MARKER_AVAILABLE = False


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on the Marker library (Surya OCR + DL models).
    Requires GPU acceleration for acceptable performance.

    Margins (headers / footers) are removed BEFORE the file is passed to the
    AI models, using redaction (PyMuPDF) instead of CropBox, because redaction
    behaves the same for every engine and also clears pixels in scanned pages.

    Output: one Document per page (metadata["page_number"], 1-based).
    """

    # Surya models are heavy (VRAM) - load them once per process
    _shared_models = None
    _shared_models_lock = threading.Lock()

    # Marker is not thread-safe - serialize conversions
    _convert_lock = threading.Lock()

    # Marker page separator with paginate_output=True, e.g. "\n\n{0}------...------\n\n"
    # (Marker page numbering starts at 0)
    _PAGE_SEPARATOR_RE = re.compile(r"\n*\{(\d+)\}-{10,}\n*")

    # Minimum content dimension [pt] that must remain after removing margins
    _MIN_REMAINING_DIM = 100

    def __init__(
        self,
        languages: str = "pl,en",
        top_margin_crop: float = 50.0,
        bottom_margin_crop: float = 60.0,
        left_margin_crop: float = 0.0,
        right_margin_crop: float = 0.0,
    ):
        """
        Args:
            languages:            Comma-separated language codes (e.g. "pl,en").
                                  May be ignored in newer Marker versions.
            top_margin_crop:      Top margin to remove [pt] (header).
            bottom_margin_crop:   Bottom margin to remove [pt] (footer).
            left_margin_crop:     Left margin to remove [pt].
            right_margin_crop:    Right margin to remove [pt].
        """
        if not MARKER_AVAILABLE:
            raise ImportError("Install Marker: pip install marker-pdf")

        # ── Margins ──────────────────────────────────────────────
        self._top_margin = top_margin_crop
        self._bottom_margin = bottom_margin_crop
        self._left_margin = left_margin_crop
        self._right_margin = right_margin_crop
        self._margins_enabled = any(
            [top_margin_crop, bottom_margin_crop, left_margin_crop, right_margin_crop]
        )

        if self._margins_enabled and FITZ_AVAILABLE:
            logger.info(
                f"Margins: top={top_margin_crop}pt, bottom={bottom_margin_crop}pt, "
                f"left={left_margin_crop}pt, right={right_margin_crop}pt | "
                f"Method: redaction (PyMuPDF)"
            )
        elif self._margins_enabled and not FITZ_AVAILABLE:
            logger.warning("Margins enabled, but PyMuPDF is missing! Install 'pymupdf'.")

        # ── GPU / Marker models ──────────────────────────────────
        # Note: the device is chosen by Marker itself (TORCH_DEVICE environment
        # variable, set BEFORE importing Marker). The value below is informational only.
        self._device = self._detect_device()
        self.models = self._get_shared_models()

        # Converter configuration (paginate_output -> page separators in Markdown)
        config_dict = ConfigParser(
            {"languages": languages, "paginate_output": True}
        ).generate_config_dict()
        self.converter = PdfConverter(
            config=config_dict,
            artifact_dict=self.models,
        )

        self.languages = languages
        logger.info("MarkerPdfParser ready.")

    # ══════════════════════════════════════════════════════════════
    # PUBLIC INTERFACE
    # ══════════════════════════════════════════════════════════════

    def parse(
        self,
        file_source: Union[str, io.BytesIO, bytes],
        **kwargs,
    ) -> List[Document]:
        """
        Processes a PDF -> list of Documents (one Document per page).
        """
        source_name = self._get_source_name(file_source)
        temp_pdf_path = None

        try:
            # ── 1. Margin removal (PyMuPDF) ──────────────────────
            if self._margins_enabled and FITZ_AVAILABLE:
                logger.info(f"Removing margins: {source_name}")
                pdf_to_process = self._precrop_pdf(file_source)
            else:
                pdf_to_process = self._get_bytes(file_source)

            # ── 2. Write to a temporary file ─────────────────────
            # PdfConverter takes a file path, so a temporary file is required.
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
                temp_pdf.write(pdf_to_process)
                temp_pdf_path = temp_pdf.name

            # ── 3. Marker conversion (GPU), serialized ───────────
            logger.info(f"Starting Marker (Surya) conversion: {source_name}")
            with self._convert_lock:
                rendered = self.converter(temp_pdf_path)
            md_text = rendered.markdown
            logger.info(f"Conversion finished: {source_name}")

            # ── 4. Building documents ────────────────────────────
            if not md_text or not md_text.strip():
                logger.warning(f"Empty text returned for '{source_name}'")
                return []

            documents = self._build_documents(md_text, source_name)

            if not documents:
                logger.warning(f"No content after splitting into pages for '{source_name}'")
            else:
                logger.info(f"Extracted {len(documents)} pages from '{source_name}'")
            return documents

        except Exception as e:
            logger.error(f"Marker error ({source_name}): {e}", exc_info=True)
            return []

        finally:
            # Temporary file cleanup
            if temp_pdf_path and os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)

            # Free VRAM
            self._cleanup_gpu()

    def diagnostics(self) -> Dict[str, str]:
        """Diagnostic information for Marker."""
        info = {
            "device": self._device,
            "languages": self.languages,
            "margins_enabled": str(self._margins_enabled),
            "margin_top_pt": str(self._top_margin),
            "margin_bottom_pt": str(self._bottom_margin),
            "margin_left_pt": str(self._left_margin),
            "margin_right_pt": str(self._right_margin),
            "torch_version": torch.__version__,
            "cuda_available": str(torch.cuda.is_available()),
        }
        if torch.cuda.is_available():
            info["gpu_name"] = torch.cuda.get_device_name(0)
            info["gpu_vram_gb"] = f"{torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f}"
        return info

    # ══════════════════════════════════════════════════════════════
    # SPLITTING INTO PAGES
    # ══════════════════════════════════════════════════════════════

    def _build_documents(self, md_text: str, source_name: str) -> List[Document]:
        """
        Splits the Markdown into pages using Marker's separators and creates
        a Document for every non-empty page. If there are no separators,
        returns the whole text as a single Document (without page_number).
        """
        base_metadata = {
            "source": source_name,
            "parser": "marker",
            "margin_top_pt": self._top_margin,
            "margin_bottom_pt": self._bottom_margin,
        }

        matches = list(self._PAGE_SEPARATOR_RE.finditer(md_text))
        if not matches:
            logger.warning(
                f"No page separators detected in Marker output ({source_name}). "
                f"Returning the whole text as a single Document."
            )
            return [Document(page_content=md_text.strip(), metadata=base_metadata)]

        documents: List[Document] = []

        # Text before the first separator (usually empty)
        preamble = md_text[: matches[0].start()].strip()
        if preamble:
            documents.append(Document(page_content=preamble, metadata=dict(base_metadata)))

        for idx, match in enumerate(matches):
            start = match.end()
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md_text)
            page_text = md_text[start:end].strip()
            if not page_text:
                continue

            metadata = dict(base_metadata)
            metadata["page_number"] = int(match.group(1)) + 1  # Marker counts from 0
            documents.append(Document(page_content=page_text, metadata=metadata))

        return documents

    # ══════════════════════════════════════════════════════════════
    # MARGIN REMOVAL (PyMuPDF redaction)
    # ══════════════════════════════════════════════════════════════

    def _precrop_pdf(self, file_source: Union[str, io.BytesIO, bytes]) -> bytes:
        """
        Removes the content of the margins (text, graphics, image pixels) via redaction.
        Pages are not deleted, so page numbering matches the original.
        """
        pdf_doc = pymupdf.Document(stream=self._get_bytes(file_source), filetype="pdf")
        pages_redacted = 0

        try:
            for page in pdf_doc:
                r = page.rect  # dimensions with the page rotation taken into account

                remaining_w = r.width - self._left_margin - self._right_margin
                remaining_h = r.height - self._top_margin - self._bottom_margin
                if remaining_w < self._MIN_REMAINING_DIM or remaining_h < self._MIN_REMAINING_DIM:
                    logger.warning(f"Page {page.number + 1}: margins too large. Skipping.")
                    continue

                margin_rects = []
                if self._top_margin:
                    margin_rects.append(
                        pymupdf.Rect(r.x0, r.y0, r.x1, r.y0 + self._top_margin)
                    )
                if self._bottom_margin:
                    margin_rects.append(
                        pymupdf.Rect(r.x0, r.y1 - self._bottom_margin, r.x1, r.y1)
                    )
                if self._left_margin:
                    margin_rects.append(
                        pymupdf.Rect(r.x0, r.y0, r.x0 + self._left_margin, r.y1)
                    )
                if self._right_margin:
                    margin_rects.append(
                        pymupdf.Rect(r.x1 - self._right_margin, r.y0, r.x1, r.y1)
                    )

                for rect in margin_rects:
                    # Convert to unrotated coordinates (important for rotated pages;
                    # for rotation 0 the matrix is the identity)
                    page.add_redact_annot(rect * page.derotation_matrix)

                page.apply_redactions(
                    images=pymupdf.PDF_REDACT_IMAGE_PIXELS,
                    graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                )
                pages_redacted += 1

            logger.info(f"Margin redaction: {pages_redacted}/{len(pdf_doc)} pages.")
            return pdf_doc.tobytes()
        finally:
            pdf_doc.close()

    # ══════════════════════════════════════════════════════════════
    # HELPER METHODS
    # ══════════════════════════════════════════════════════════════

    @classmethod
    def _get_shared_models(cls):
        """Loads Marker models once per process (thread-safe)."""
        with cls._shared_models_lock:
            if cls._shared_models is None:
                logger.info("Loading Marker (Surya) models...")
                cls._shared_models = create_model_dict()
            return cls._shared_models

    @staticmethod
    def _detect_device() -> str:
        """Informational only - the actual device is chosen by Marker."""
        if torch.cuda.is_available():
            return "cuda"
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            return "mps"
        return "cpu"

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "stream/bytes"

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
        raise ValueError(f"Unsupported type: {type(file_source)}")

    @staticmethod
    def _cleanup_gpu():
        """Frees the VRAM cache after a document has been processed."""
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            torch.mps.empty_cache()