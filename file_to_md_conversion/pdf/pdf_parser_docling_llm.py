import base64
import io
import logging
import os
from collections import defaultdict
from typing import List, Optional, Union

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
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from base_parser import BaseDocumentParser

load_dotenv()

logger = logging.getLogger("DoclingVisionParser")

LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_MODEL = os.getenv("LLM_MODEL")
LLM_API_KEY = os.getenv("LLM_API_KEY")

class PdfParser(BaseDocumentParser):
    def __init__(
            self,
            use_gpu: bool = True,
            do_ocr: bool = True,
            table_mode: str = "accurate",
    ):
        self._device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"

        # Domyślna konfiguracja filtrów
        self._filters_config = {
            'size': {
                'enabled': True,
                'min_image_size': 10000,
            },
            'position': {
                'enabled': True,
                'header_margin': 0.15,
                'footer_margin': 0.10,
            },
            'aspect_ratio': {
                'enabled': True,
                'min_aspect_ratio': 0.3,
                'max_aspect_ratio': 5.0,
                'square_logo_threshold': 20000,
            }
        }

        # Statystyki filtrowania
        self._filter_stats = {
            'total_images': 0,
            'accepted': 0,
            'rejected_size': 0,
            'rejected_position': 0,
            'rejected_aspect_ratio': 0,
            'rejected_no_image': 0,
        }

        # Konfiguracja promptu
        self._vision_prompt_template = None

        pipeline_options = PdfPipelineOptions(
            do_ocr=do_ocr,
            do_table_structure=True,
            generate_picture_images=True,
            table_structure_options=TableStructureOptions(
                mode=TableFormerMode.ACCURATE if table_mode == "accurate" else TableFormerMode.FAST
            ),
            accelerator_options=AcceleratorOptions(
                num_threads=4,
                device=AcceleratorDevice.CUDA if self._device == "cuda" else AcceleratorDevice.CPU,
            ),
        )

        if do_ocr:
            pipeline_options.ocr_options = EasyOcrOptions(lang=["pl", "en"])

        self.converter = DocumentConverter(
            format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
        )

        self.llm = ChatOpenAI(
            base_url=LLM_BASE_URL,
            api_key=LLM_API_KEY,
            model=LLM_MODEL,
            max_tokens=1200
        )

    # Metody konfiguracji filtra rozmiaru
    def configure_size_filter(self, enabled: bool = True, min_image_size: int = 10000):
        """
        Konfiguruje filtr rozmiaru obrazu.

        Args:
            enabled: Czy filtr jest włączony
            min_image_size: Minimalna powierzchnia obrazu w pikselach
        """
        self._filters_config['size']['enabled'] = enabled
        self._filters_config['size']['min_image_size'] = min_image_size
        logger.info(f"Filtr rozmiaru: {'WŁĄCZONY' if enabled else 'WYŁĄCZONY'}, min_size={min_image_size}px")
        return self

    def disable_size_filter(self):
        """Wyłącza filtr rozmiaru."""
        self._filters_config['size']['enabled'] = False
        logger.info("Filtr rozmiaru: WYŁĄCZONY")
        return self

    # Metody konfiguracji filtra pozycji
    def configure_position_filter(
            self,
            enabled: bool = True,
            header_margin: float = 0.15,
            footer_margin: float = 0.10
    ):
        """
        Konfiguruje filtr pozycji obrazu na stronie.

        Args:
            enabled: Czy filtr jest włączony
            header_margin: Margines nagłówka (0.0 - 1.0)
            footer_margin: Margines stopki (0.0 - 1.0)
        """
        self._filters_config['position']['enabled'] = enabled
        self._filters_config['position']['header_margin'] = header_margin
        self._filters_config['position']['footer_margin'] = footer_margin
        logger.info(f"Filtr pozycji: {'WŁĄCZONY' if enabled else 'WYŁĄCZONY'}, "
                    f"header={header_margin}, footer={footer_margin}")
        return self

    def disable_position_filter(self):
        """Wyłącza filtr pozycji."""
        self._filters_config['position']['enabled'] = False
        logger.info("Filtr pozycji: WYŁĄCZONY")
        return self

    # Metody konfiguracji filtra proporcji
    def configure_aspect_ratio_filter(
            self,
            enabled: bool = True,
            min_aspect_ratio: float = 0.3,
            max_aspect_ratio: float = 5.0,
            square_logo_threshold: int = 20000
    ):
        """
        Konfiguruje filtr proporcji obrazu.

        Args:
            enabled: Czy filtr jest włączony
            min_aspect_ratio: Minimalna proporcja szerokość/wysokość
            max_aspect_ratio: Maksymalna proporcja szerokość/wysokość
            square_logo_threshold: Próg powierzchni dla kwadratowych logo
        """
        self._filters_config['aspect_ratio']['enabled'] = enabled
        self._filters_config['aspect_ratio']['min_aspect_ratio'] = min_aspect_ratio
        self._filters_config['aspect_ratio']['max_aspect_ratio'] = max_aspect_ratio
        self._filters_config['aspect_ratio']['square_logo_threshold'] = square_logo_threshold
        logger.info(f"Filtr proporcji: {'WŁĄCZONY' if enabled else 'WYŁĄCZONY'}, "
                    f"ratio={min_aspect_ratio}-{max_aspect_ratio}")
        return self

    def disable_aspect_ratio_filter(self):
        """Wyłącza filtr proporcji."""
        self._filters_config['aspect_ratio']['enabled'] = False
        logger.info("Filtr proporcji: WYŁĄCZONY")
        return self

    # Metody globalne
    def disable_all_filters(self):
        """Wyłącza wszystkie filtry - wszystkie obrazy będą analizowane."""
        self._filters_config['size']['enabled'] = False
        self._filters_config['position']['enabled'] = False
        self._filters_config['aspect_ratio']['enabled'] = False
        logger.info("Wszystkie filtry: WYŁĄCZONE")
        return self

    def enable_all_filters(self):
        """Włącza wszystkie filtry z domyślnymi ustawieniami."""
        self._filters_config['size']['enabled'] = True
        self._filters_config['position']['enabled'] = True
        self._filters_config['aspect_ratio']['enabled'] = True
        logger.info("Wszystkie filtry: WŁĄCZONE")
        return self

    def get_filters_config(self) -> dict:
        """Zwraca aktualną konfigurację filtrów."""
        return self._filters_config.copy()

    def get_filter_stats(self) -> dict:
        """Zwraca statystyki filtrowania obrazów."""
        return self._filter_stats.copy()

    def reset_filter_stats(self):
        """Resetuje statystyki filtrowania."""
        self._filter_stats = {
            'total_images': 0,
            'accepted': 0,
            'rejected_size': 0,
            'rejected_position': 0,
            'rejected_aspect_ratio': 0,
            'rejected_no_image': 0,
        }
        return self

    def set_vision_prompt(self, prompt: str):
        """
        Ustawia własny prompt dla analizy obrazów przez VLM.

        Args:
            prompt: Tekst promptu, który zostanie wysłany do modelu wizyjnego
        """
        self._vision_prompt_template = prompt
        logger.info("Ustawiono niestandardowy prompt dla VLM")
        return self

    def reset_vision_prompt(self):
        """Resetuje prompt do wartości domyślnej."""
        self._vision_prompt_template = None
        logger.info("Przywrócono domyślny prompt dla VLM")
        return self

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        source_name = self._get_source_name(file_source)
        logger.info(f"Rozpoczynam parsowanie VISION dla: {source_name}")
        self.reset_filter_stats()

        try:
            conv_source = self._prepare_source(file_source)
            result = self.converter.convert(conv_source)
            doc = result.document

            page_contents = defaultdict(list)

            for item, level in doc.iterate_items():
                label = getattr(item, "label", None)
                label_val = str(label.value) if hasattr(label, "value") else str(label)

                if label_val in {"page_header", "page_footer"}:
                    continue

                page_no = 0
                if hasattr(item, "prov") and item.prov:
                    page_no = item.prov[0].page_no

                if label_val == "picture":
                    self._filter_stats['total_images'] += 1

                    if self._should_process_image(item):
                        self._filter_stats['accepted'] += 1
                        logger.info(f"[VISION] Wykryto istotny obraz na stronie {page_no}. Analizuję przez {LLM_MODEL}")
                        description = self._analyze_image_with_vlm(item)
                        page_contents[page_no].append(f"\n{description}\n")
                    else:
                        logger.debug(f"[SKIP] Pominięto obraz na stronie {page_no}")
                else:
                    md_fragment = self._item_to_markdown(item, level, doc)
                    if md_fragment:
                        page_contents[page_no].append(md_fragment)

            final_docs = []
            for p in sorted(page_contents.keys()):
                if p <= 0:
                    continue
                final_docs.append(Document(
                    page_content="\n\n".join(page_contents[p]),
                    metadata={"page_number": p, "source": source_name}
                ))

            # Podsumowanie filtrowania
            logger.info(f"[STATS] Obrazów łącznie: {self._filter_stats['total_images']}")
            logger.info(f"[STATS] Zaakceptowanych: {self._filter_stats['accepted']}")
            logger.info(f"[STATS] Odrzuconych - brak obrazu: {self._filter_stats['rejected_no_image']}")
            logger.info(f"[STATS] Odrzuconych - rozmiar: {self._filter_stats['rejected_size']}")
            logger.info(f"[STATS] Odrzuconych - pozycja: {self._filter_stats['rejected_position']}")
            logger.info(f"[STATS] Odrzuconych - proporcje: {self._filter_stats['rejected_aspect_ratio']}")

            return final_docs

        except Exception as e:
            logger.error(f"Błąd VisionParser: {e}", exc_info=True)
            return []

    def _should_process_image(self, item) -> bool:
        """
        Główna metoda decydująca czy obraz powinien być wysłany do VLM.
        Uruchamia wszystkie włączone filtry.
        """
        try:
            if not hasattr(item, "image") or item.image is None:
                logger.debug(f"[REJECT] Brak atrybutu image")
                self._filter_stats['rejected_no_image'] += 1
                return False

            pil_img = item.image.pil_image
            if pil_img is None:
                logger.debug(f"[REJECT] pil_image is None")
                self._filter_stats['rejected_no_image'] += 1
                return False

            width, height = pil_img.size
            logger.debug(f"[DEBUG] Sprawdzam obraz {width}x{height}px")

            # Filtr 1: Rozmiar obrazu
            if self._filters_config['size']['enabled']:
                if not self._filter_by_size(pil_img):
                    self._filter_stats['rejected_size'] += 1
                    return False

            # Filtr 2: Pozycja na stronie
            if self._filters_config['position']['enabled']:
                if not self._filter_by_position(item):
                    self._filter_stats['rejected_position'] += 1
                    return False

            # Filtr 3: Proporcje (aspect ratio)
            if self._filters_config['aspect_ratio']['enabled']:
                if not self._filter_by_aspect_ratio(pil_img):
                    self._filter_stats['rejected_aspect_ratio'] += 1
                    return False

            logger.debug(f"[ACCEPT] Obraz ({width}x{height}) zaakceptowany do analizy")
            return True

        except Exception as e:
            logger.warning(f"Błąd podczas filtrowania obrazu: {e}", exc_info=True)
            return False

    def _filter_by_size(self, pil_img) -> bool:
        """
        Filtruje obrazy po rozmiarze - małe obrazy to często logo.

        Returns:
            True jeśli obraz jest wystarczająco duży
            False jeśli obraz jest zbyt mały (prawdopodobnie logo)
        """
        width, height = pil_img.size
        area = width * height
        min_size = self._filters_config['size']['min_image_size']

        if area < min_size:
            logger.debug(f"[FILTER_SIZE] Obraz zbyt mały ({width}x{height}={area}px < {min_size}px)")
            return False

        logger.debug(f"[FILTER_SIZE] OK ({width}x{height}={area}px >= {min_size}px)")
        return True

    def _filter_by_position(self, item) -> bool:
        """
        Filtruje obrazy znajdujące się w nagłówkach lub stopkach strony.
        Logo firmowe często umieszczane jest właśnie tam.

        Returns:
            True jeśli obraz jest w głównej części strony
            False jeśli obraz jest w nagłówku lub stopce
        """
        if not hasattr(item, "prov") or not item.prov:
            logger.debug(f"[FILTER_POSITION] Brak prov - akceptuję")
            return True

        prov = item.prov[0]

        logger.debug(f"[FILTER_POSITION] prov attributes: {dir(prov)}")

        if not hasattr(prov, "bbox") or prov.bbox is None:
            logger.debug(f"[FILTER_POSITION] Brak bbox - akceptuję")
            return True

        bbox = prov.bbox
        logger.debug(f"[FILTER_POSITION] bbox type: {type(bbox)}, attributes: {dir(bbox)}")

        try:
            y_top = None
            page_height = None

            # Różne warianty dostępu do współrzędnych w Docling
            if hasattr(bbox, 't') and hasattr(bbox, 'page_height'):
                y_top = bbox.t
                page_height = bbox.page_height
                logger.debug(f"[FILTER_POSITION] Użyto bbox.t i bbox.page_height")
            elif hasattr(bbox, 'y') and hasattr(bbox, 'height'):
                y_top = bbox.y
                page_height = bbox.height
                logger.debug(f"[FILTER_POSITION] Użyto bbox.y i bbox.height")
            elif hasattr(bbox, 'top') and hasattr(bbox, 'page_height'):
                y_top = bbox.top
                page_height = bbox.page_height
                logger.debug(f"[FILTER_POSITION] Użyto bbox.top i bbox.page_height")
            elif isinstance(bbox, (tuple, list)) and len(bbox) >= 4:
                y_top = bbox[0]
                page_height = 1.0
                logger.debug(f"[FILTER_POSITION] bbox jest listą/tuple")
            else:
                logger.debug(f"[FILTER_POSITION] Nie znaleziono znanego formatu bbox - akceptuję obraz")
                return True

            if y_top is None or page_height is None or page_height == 0:
                logger.debug(f"[FILTER_POSITION] Nie można określić pozycji - akceptuję")
                return True

            relative_pos = y_top / page_height
            header_margin = self._filters_config['position']['header_margin']
            footer_margin = self._filters_config['position']['footer_margin']

            logger.debug(f"[FILTER_POSITION] y_top={y_top}, page_height={page_height}, relative_pos={relative_pos:.3f}")

            if relative_pos < header_margin:
                logger.debug(f"[FILTER_POSITION] Obraz w nagłówku (y={relative_pos:.2f} < {header_margin})")
                return False

            if relative_pos > (1 - footer_margin):
                logger.debug(f"[FILTER_POSITION] Obraz w stopce (y={relative_pos:.2f} > {1 - footer_margin})")
                return False

            logger.debug(
                f"[FILTER_POSITION] OK (y={relative_pos:.2f} w zakresie {header_margin} - {1 - footer_margin})")
            return True

        except Exception as e:
            logger.debug(f"[FILTER_POSITION] Błąd podczas sprawdzania pozycji: {e} - akceptuję obraz")
            return True

    def _filter_by_aspect_ratio(self, pil_img) -> bool:
        """
        Filtruje obrazy po proporcjach szerokość/wysokość.
        Logo często mają charakterystyczne proporcje:
        - Kwadratowe (aspect ratio ~ 1.0)
        - Bardzo szerokie bannery (aspect ratio > 5.0)
        - Bardzo wysokie (aspect ratio < 0.3)

        Returns:
            True jeśli proporcje wskazują na diagram/schemat
            False jeśli proporcje wskazują na logo/dekorację
        """
        width, height = pil_img.size

        if height == 0:
            logger.debug(f"[FILTER_ASPECT] Wysokość = 0")
            return False

        aspect_ratio = width / height
        area = width * height

        config = self._filters_config['aspect_ratio']
        min_ratio = config['min_aspect_ratio']
        max_ratio = config['max_aspect_ratio']
        square_threshold = config['square_logo_threshold']

        # Małe kwadratowe obrazy to prawdopodobnie logo
        if 0.8 < aspect_ratio < 1.2 and area < square_threshold:
            logger.debug(
                f"[FILTER_ASPECT] Małe kwadratowe logo ({width}x{height}, ratio={aspect_ratio:.2f}, area={area})")
            return False

        # Zbyt wąskie lub szerokie obrazy (bannery, paski)
        if aspect_ratio < min_ratio or aspect_ratio > max_ratio:
            logger.debug(f"[FILTER_ASPECT] Nieprawidłowe proporcje ({width}x{height}, "
                         f"ratio={aspect_ratio:.2f} poza zakresem {min_ratio}-{max_ratio})")
            return False

        logger.debug(f"[FILTER_ASPECT] OK ({width}x{height}, ratio={aspect_ratio:.2f})")
        return True

    def _analyze_image_with_vlm(self, item) -> str:
        """Wysyła obrazek do LLM i pobiera jego opis."""
        try:
            if not hasattr(item, "image") or item.image is None:
                return "[Błąd: Obraz nie został wygenerowany przez Docling]"

            pil_img = item.image.pil_image
            if pil_img is None:
                return "[Błąd: Nie udało się wyrenderować pil_image z ImageRef]"

            buffered = io.BytesIO()
            pil_img.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            message = HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": self._get_vision_prompt()
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{img_base64}"},
                    },
                ]
            )

            response = self.llm.invoke([message])
            description = response.content.strip()

            logger.info(f"[VISION Success] Analiza gotowa (długość: {len(description)} znaków)")
            return description

        except Exception as e:
            logger.warning(f"Błąd analizy VLM: {e}")
            return f"[Nie udało się przeanalizować obrazu: {str(e)}]"

    def _get_vision_prompt(self) -> str:
        """
        Zwraca prompt używany do analizy obrazów przez VLM.
        Wydzielone do osobnej metody dla łatwej edycji.
        """
        if self._vision_prompt_template:
            return self._vision_prompt_template

        return """You are an expert document OCR and layout parsing assistant. 
            Extract the text, tables, and formatting from the provided document image 
            and output it EXACTLY as clean Markdown. 
            Rules:
            - Preserve heading levels (#, ##, etc.)
            Convert tables to Markdown tables.
            - Do not add ANY conversational filler (e.g., 'Here is the markdown:').
            - Stop generating immediately when you reach the end of the page content."""

    def _item_to_markdown(self, item, level, doc) -> Optional[str]:
        try:
            if hasattr(item, "export_to_markdown"):
                return item.export_to_markdown(doc=doc)
        except:
            pass
        return getattr(item, "text", None)

    def _prepare_source(self, source):
        if isinstance(source, str):
            return source
        return DocumentStream(
            name="doc.pdf",
            stream=io.BytesIO(source) if isinstance(source, bytes) else source
        )

    def _get_source_name(self, source):
        return os.path.basename(source) if isinstance(source, str) else "stream.pdf"