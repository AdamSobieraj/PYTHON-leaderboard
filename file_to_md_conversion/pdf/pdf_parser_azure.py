import io
import logging
import os
from typing import Dict, List, Optional, Tuple, Union

from langchain_core.documents import Document

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)


try:
    import pymupdf  # PyMuPDF

    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False
    logger.warning("PyMuPDF (fitz) niedostępny! Obcinanie marginesów przed wysłaniem do Azure nie zadziała.")

try:
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.documentintelligence import DocumentIntelligenceClient

    AZURE_AVAILABLE = True
except ImportError:
    AZURE_AVAILABLE = False


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on the cloud Azure Document Intelligence service.
    Uses the latest 'prebuilt-layout' model, which natively returns Markdown.

    Uses Pre-Crop (PyMuPDF) to cut headers and footers off locally,
    so they are not sent to the cloud (saves on analysis and keeps the Markdown clean).
    """

    def __init__(
            self,
            endpoint: Optional[str] = None,
            key: Optional[str] = None,
            top_margin_crop: float = 50.0,
            bottom_margin_crop: float = 60.0,
            left_margin_crop: float = 0.0,
            right_margin_crop: float = 0.0,
    ):
        """
        Args:
            endpoint:             Azure endpoint (e.g. https://<your-name>.cognitiveservices.azure.com/).
            key:                  Azure API key.
            top_margin_crop:      Top margin to crop [pt] (removes the header).
            bottom_margin_crop:   Bottom margin to crop [pt] (removes the footer with page numbering).
            left_margin_crop:     Left margin to crop [pt].
            right_margin_crop:    Right margin to crop [pt].
        """
        if not AZURE_AVAILABLE:
            raise ImportError("Zainstaluj Azure SDK: pip install azure-ai-documentintelligence")

        # ── Azure authentication ─────────────────────────────────
        self._endpoint = endpoint or os.getenv("AZURE_DOCUMEN" "T_INTELLIGENCE_ENDPOINT")
        self._key = key or os.getenv("AZURE_DOCUMENT_INTELLIGENCE_KEY")

        if not self._endpoint or not self._key:
            raise ValueError(
                "Brak poświadczeń Azure! Podaj 'endpoint' i 'key' w konstruktorze "
                "lub ustaw zmienne środowiskowe AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT "
                "oraz AZURE_DOCUMENT_INTELLIGENCE_KEY."
            )

        self.client = DocumentIntelligenceClient(
            endpoint=self._endpoint,
            credential=AzureKeyCredential(self._key)
        )

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
                f"Azure Parser gotowy. Marginesy pre-crop aktywne (top={top_margin_crop}pt, bottom={bottom_margin_crop}pt).")
        elif self._margins_enabled and not FITZ_AVAILABLE:
            logger.warning("Marginesy włączone, ale brak PyMuPDF. Cały dokument zostanie wysłany do Azure!")
        else:
            logger.info("Azure Parser gotowy. Marginesy wyłączone.")

    # ══════════════════════════════════════════════════════════════
    # PUBLIC INTERFACE
    # ══════════════════════════════════════════════════════════════

    def parse(
            self,
            file_source: Union[str, io.BytesIO, bytes],
            **kwargs,
    ) -> List[Document]:
        """
        Processes the PDF → list of Documents (Azure returns one merged Document in Markdown).
        """
        source_name = self._get_source_name(file_source)

        try:
            # ── 1. PRE-CROP of margins (PyMuPDF) ─────────────────
            # Crop the margins
            original_page_dims = None

            if self._margins_enabled and FITZ_AVAILABLE:
                logger.info(f"Lokalny Pre-crop przed wysyłką: {source_name}")
                cropped_stream, original_page_dims = self._precrop_pdf(file_source)
                file_bytes = cropped_stream.getvalue()
            else:
                file_bytes = self._get_bytes(file_source)

            # ── 2. Upload to the Azure cloud ─────────────────────
            logger.info(f"Wysyłanie pliku do Azure Document Intelligence: {source_name} ({len(file_bytes)} bajtów)")

            poller = self.client.begin_analyze_document(
                model_id="prebuilt-layout",
                body=file_bytes,
                output_content_format="markdown",
            )

            result = poller.result()
            logger.info(f"Analiza Azure zakończona sukcesem: {source_name}")

            # ── 3. Building the document ─────────────────────────
            md_text = getattr(result, "content", "")

            if not md_text or not md_text.strip():
                logger.warning(f"Zwrócono pusty tekst dla '{source_name}'")
                return []

            # Gather the metadata
            page_count = len(result.pages) if hasattr(result, "pages") and result.pages else 1

            metadata = {
                "source": source_name,
                "parser": "azure_document_intelligence",
                "total_pages": page_count,
                "margin_top_pt": self._top_margin,
                "margin_bottom_pt": self._bottom_margin,
                "pre_cropped": self._margins_enabled and FITZ_AVAILABLE
            }

            return [Document(page_content=md_text.strip(), metadata=metadata)]

        except Exception as e:
            logger.error(f"Błąd komunikacji z Azure dla ({source_name}): {e}", exc_info=True)
            return []

    def diagnostics(self) -> Dict[str, str]:
        """Diagnostic information."""
        return {
            "engine": "Azure Document Intelligence (prebuilt-layout)",
            "endpoint": self._endpoint,
            "margins_enabled": str(self._margins_enabled),
            "margin_top_pt": str(self._top_margin),
            "margin_bottom_pt": str(self._bottom_margin),
            "crop_method": "pre-crop (PyMuPDF)" if FITZ_AVAILABLE else "Brak (zainstaluj pymupdf)",
        }

    # ══════════════════════════════════════════════════════════════
    # LAYER 1: PRE-CROP (PyMuPDF cropbox)
    # ══════════════════════════════════════════════════════════════

    def _precrop_pdf(
            self, file_source: Union[str, io.BytesIO, bytes]
    ) -> Tuple[io.BytesIO, Dict[int, Tuple[float, float]]]:
        """
        Physical cropping of the margins using PyMuPDF cropbox.
        The Azure cloud receives a file with the top and bottom physically removed.
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
            rect = page.rect

            original_dims[page_idx + 1] = (rect.width, rect.height)

            new_x0 = rect.x0 + self._left_margin
            new_y0 = rect.y0 + self._top_margin
            new_x1 = rect.x1 - self._right_margin
            new_y1 = rect.y1 - self._bottom_margin

            remaining_width = new_x1 - new_x0
            remaining_height = new_y1 - new_y0

            # Prevent destroying the page with absurd margins
            if remaining_width < 100 or remaining_height < 100:
                logger.warning(
                    f"Strona {page_idx + 1}: marginesy zbyt duże. Pomijam przycinanie tej strony."
                )
                continue

            new_rect = pymupdf.Rect(new_x0, new_y0, new_x1, new_y1)
            page.set_cropbox(new_rect)
            pages_cropped += 1

        # Save the cropped file to RAM, ready to be sent over the network
        output = io.BytesIO()
        pdf_doc.save(output)
        pdf_doc.close()
        output.seek(0)

        return output, original_dims

    # ══════════════════════════════════════════════════════════════
    # HELPER METHODS
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "strumień_pamięci"

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
        raise ValueError(f"Nieobsługiwany typ: {type(file_source)}")