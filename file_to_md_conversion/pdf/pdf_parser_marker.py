import io
import logging
import os
import tempfile
from typing import Dict, List, Tuple, Union

import torch
from langchain_core.documents import Document

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

try:
    import fitz  # PyMuPDF
    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False
    logger.warning("PyMuPDF (fitz) niedostępny! Fizyczne obcinanie marginesów nie zadziała.")

try:
    # API dla nowszych wersji Marker-PDF (v1.0+)
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.config.parser import ConfigParser
    MARKER_AVAILABLE = True
except ImportError:
    MARKER_AVAILABLE = False


class PdfParser(BaseDocumentParser):
    """
    Parser PDF oparty na bibliotece Marker (Surya OCR + modele DL).
    Wymaga akceleracji GPU dla akceptowalnej wydajności.
    
    Wykorzystuje Pre-Crop (PyMuPDF) do fizycznego usuwania nagłówków 
    i stopek z dokumentu PRZED przekazaniem go do modeli AI.
    """

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
            languages:            Kody języków oddzielone przecinkami (np. "pl,en").
            top_margin_crop:      Górny margines do obcięcia [pt] (usuwa nagłówek).
            bottom_margin_crop:   Dolny margines do obcięcia [pt] (usuwa stopkę).
            left_margin_crop:     Lewy margines do obcięcia [pt].
            right_margin_crop:    Prawy margines do obcięcia [pt].
        """
        if not MARKER_AVAILABLE:
            raise ImportError("Zainstaluj Marker: pip install marker-pdf")

        # ── Marginesy ────────────────────────────────────────────
        self._top_margin = top_margin_crop
        self._bottom_margin = bottom_margin_crop
        self._left_margin = left_margin_crop
        self._right_margin = right_margin_crop
        self._margins_enabled = any(
            [top_margin_crop, bottom_margin_crop, left_margin_crop, right_margin_crop]
        )

        if self._margins_enabled and FITZ_AVAILABLE:
            logger.info(
                f"Marginesy: top={top_margin_crop}pt, bottom={bottom_margin_crop}pt | "
                f"Metoda: Pre-crop (PyMuPDF)"
            )
        elif self._margins_enabled and not FITZ_AVAILABLE:
            logger.warning("Marginesy włączone, ale brak PyMuPDF! Zainstaluj 'pymupdf'.")

        # ── GPU / Modele Marker ──────────────────────────────────
        self._device = self._detect_device()
        logger.info(f"Ładowanie modeli Marker (Surya) do pamięci {self._device.upper()}...")
        
        # Inicjalizacja modeli w VRAM
        self.models = create_model_dict()
        
        # Konfiguracja konwertera
        config_dict = ConfigParser({"languages": languages}).generate_config_dict()
        self.converter = PdfConverter(
            config=config_dict, 
            artifact_dict=self.models
        )
        
        self.languages = languages
        logger.info("MarkerPdfParser gotowy do pracy.")

    # ══════════════════════════════════════════════════════════════
    # INTERFEJS PUBLICZNY
    # ══════════════════════════════════════════════════════════════

    def parse(
        self,
        file_source: Union[str, io.BytesIO, bytes],
        **kwargs,
    ) -> List[Document]:
        """
        Przetwarza PDF → lista Document (Marker domyślnie łączy całość w 1 Document).
        """
        source_name = self._get_source_name(file_source)
        temp_pdf_path = None

        try:
            # ── 1. PRE-CROP marginesów (PyMuPDF) ─────────────────
            original_page_dims = None

            if self._margins_enabled and FITZ_AVAILABLE:
                logger.info(f"Pre-crop marginesów: {source_name}")
                cropped_stream, original_page_dims = self._precrop_pdf(file_source)
                pdf_to_process = cropped_stream.getvalue()
            else:
                pdf_to_process = self._get_bytes(file_source)

            # ── 2. Zapis do pliku tymczasowego ───────────────────
            # Marker najlepiej działa z plikami na dysku. Bezpieczny fallback:
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
                temp_pdf.write(pdf_to_process)
                temp_pdf_path = temp_pdf.name

            # ── 3. Konwersja Marker (GPU) ────────────────────────
            logger.info(f"Rozpoczęto konwersję Marker (Surya): {source_name}")
            rendered = self.converter(temp_pdf_path)
            md_text = rendered.markdown
            logger.info(f"Konwersja zakończona: {source_name}")

            # ── 4. Budowanie dokumentu ───────────────────────────
            if not md_text or not md_text.strip():
                logger.warning(f"Zwrócono pusty tekst dla '{source_name}'")
                return []

            metadata = {
                "source": source_name,
                "parser": "marker",
                "margin_top_pt": self._top_margin,
                "margin_bottom_pt": self._bottom_margin,
            }

            doc = Document(page_content=md_text.strip(), metadata=metadata)
            
            return [doc]

        except Exception as e:
            logger.error(f"Błąd Marker ({source_name}): {e}", exc_info=True)
            return []
            
        finally:
            # Cleanup pliku tymczasowego
            if temp_pdf_path and os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)
            
            # Zwolnienie VRAM
            self._cleanup_gpu()

    def diagnostics(self) -> Dict[str, str]:
        """Informacje diagnostyczne dla Markera."""
        info = {
            "device": self._device,
            "languages": self.languages,
            "margins_enabled": str(self._margins_enabled),
            "margin_top_pt": str(self._top_margin),
            "margin_bottom_pt": str(self._bottom_margin),
            "torch_version": torch.__version__,
            "cuda_available": str(torch.cuda.is_available()),
        }
        if torch.cuda.is_available():
            info["gpu_name"] = torch.cuda.get_device_name(0)
            info["gpu_vram_gb"] = f"{torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f}"
        return info

    # ══════════════════════════════════════════════════════════════
    # WARSTWA 1: PRE-CROP (PyMuPDF cropbox)
    # ══════════════════════════════════════════════════════════════

    def _precrop_pdf(
        self, file_source: Union[str, io.BytesIO, bytes]
    ) -> Tuple[io.BytesIO, Dict[int, Tuple[float, float]]]:
        """
        Fizyczne przycięcie marginesów za pomocą PyMuPDF cropbox.
        Modele Surya w ogóle nie zobaczą obciętych obszarów.
        """
        if isinstance(file_source, str):
            pdf_doc = fitz.Document(file_source)
        elif isinstance(file_source, bytes):
            pdf_doc = fitz.Document(stream=file_source, filetype="pdf")
        elif isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            pdf_doc = fitz.Document(stream=file_source.read(), filetype="pdf")
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

            # Walidacja (zapobieganie obcięciu całej strony)
            remaining_width = new_x1 - new_x0
            remaining_height = new_y1 - new_y0

            if remaining_width < 100 or remaining_height < 100:
                logger.warning(
                    f"Strona {page_idx + 1}: marginesy zbyt duże. Pomijam."
                )
                continue

            new_rect = fitz.Rect(new_x0, new_y0, new_x1, new_y1)
            page.set_cropbox(new_rect)
            pages_cropped += 1

        logger.info(f"Pre-crop: przycięto {pages_cropped}/{len(pdf_doc)} stron.")

        output = io.BytesIO()
        pdf_doc.save(output)
        pdf_doc.close()
        output.seek(0)

        return output, original_dims

    # ══════════════════════════════════════════════════════════════
    # METODY POMOCNICZE
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _detect_device() -> str:
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
        raise ValueError(f"Nieobsługiwany typ: {type(file_source)}")

    @staticmethod
    def _cleanup_gpu():
        """Zwalnia cache VRAM po przetworzeniu strony."""
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            # gc.collect() - opcjonalne, w modelu Marker czasem się przydaje