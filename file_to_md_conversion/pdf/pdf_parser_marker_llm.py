import base64
import io
import logging
import os
import re
import time
from typing import List, Union, Optional, Dict

from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict

from base_parser import BaseDocumentParser

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger("MarkerVisionParser")

LLM_BASE_URL = "http://192.168.50.112:1234/v1"
LLM_MODEL = "gemma-4-31b"
LLM_API_KEY = "not-needed"


class PdfParser(BaseDocumentParser):
    """
    Parser PDF oparty na Marker (0.3.1+) z analizą Vision (Qwen2.5-vl)
    i konfigurowalnymi filtrami obrazów.
    """

    def __init__(self):
        logger.info("Inicjalizacja modeli Marker (API 0.3.x)...")
        start_init = time.time()

        self.model_dict = create_model_dict()
        self.converter = PdfConverter(artifact_dict=self.model_dict)

        self._filters_config = {
            'size': {
                'enabled': True,
                'min_image_size': 10000,
            },
            'position': {
                'enabled': False,
                'header_margin': 0.15,
                'footer_margin': 0.10,
                'supported': False,
            },
            'aspect_ratio': {
                'enabled': True,
                'min_aspect_ratio': 0.3,
                'max_aspect_ratio': 5.0,
                'square_logo_threshold': 20000,
            }
        }

        self._filter_stats = {
            'total_images': 0,
            'accepted': 0,
            'rejected_size': 0,
            'rejected_position': 0,
            'rejected_aspect_ratio': 0,
            'rejected_no_image': 0,
        }

        self._vision_prompt_template = None

        logger.info(f"Konfiguracja LLM: {LLM_MODEL}")
        self.llm = ChatOpenAI(
            base_url=LLM_BASE_URL,
            api_key=LLM_API_KEY,
            model=LLM_MODEL,
            max_tokens=1200,
            temperature=0.1
        )
        logger.info(f"PdfParser gotowy (Inicjalizacja: {time.time() - start_init:.2f}s).")

    def configure_size_filter(self, enabled: bool = True, min_image_size: int = 10000):
        self._filters_config['size']['enabled'] = enabled
        self._filters_config['size']['min_image_size'] = min_image_size
        logger.info(f"Filtr rozmiaru: {'WŁĄCZONY' if enabled else 'WYŁĄCZONY'}, min_size={min_image_size}px")
        return self

    def disable_size_filter(self):
        self._filters_config['size']['enabled'] = False
        logger.info("Filtr rozmiaru: WYŁĄCZONY")
        return self

    def configure_position_filter(self, enabled: bool = True, header_margin: float = 0.15, footer_margin: float = 0.10):
        if enabled:
            logger.warning("UWAGA: Filtr pozycji nie jest wspierany przez parser Marker.")
            enabled = False
        self._filters_config['position']['enabled'] = enabled
        self._filters_config['position']['header_margin'] = header_margin
        self._filters_config['position']['footer_margin'] = footer_margin
        return self

    def disable_position_filter(self):
        self._filters_config['position']['enabled'] = False
        logger.info("Filtr pozycji: WYŁĄCZONY")
        return self

    def configure_aspect_ratio_filter(self, enabled: bool = True, min_aspect_ratio: float = 0.3,
                                      max_aspect_ratio: float = 5.0, square_logo_threshold: int = 20000):
        self._filters_config['aspect_ratio']['enabled'] = enabled
        self._filters_config['aspect_ratio']['min_aspect_ratio'] = min_aspect_ratio
        self._filters_config['aspect_ratio']['max_aspect_ratio'] = max_aspect_ratio
        self._filters_config['aspect_ratio']['square_logo_threshold'] = square_logo_threshold
        logger.info(
            f"Filtr proporcji: {'WŁĄCZONY' if enabled else 'WYŁĄCZONY'}, ratio={min_aspect_ratio}-{max_aspect_ratio}")
        return self

    def disable_aspect_ratio_filter(self):
        self._filters_config['aspect_ratio']['enabled'] = False
        logger.info("Filtr proporcji: WYŁĄCZONY")
        return self

    def disable_all_filters(self):
        self._filters_config['size']['enabled'] = False
        self._filters_config['position']['enabled'] = False
        self._filters_config['aspect_ratio']['enabled'] = False
        logger.info("Wszystkie filtry: WYŁĄCZONE")
        return self

    def enable_all_filters(self):
        self._filters_config['size']['enabled'] = True
        self._filters_config['aspect_ratio']['enabled'] = True
        logger.info("Wszystkie filtry: WŁĄCZONE (poza filtrem pozycji)")
        return self

    def get_filters_config(self) -> dict:
        return self._filters_config.copy()

    def get_filter_stats(self) -> dict:
        return self._filter_stats.copy()

    def reset_filter_stats(self):
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
        self._vision_prompt_template = prompt
        logger.info("Ustawiono niestandardowy prompt dla VLM")
        return self

    def reset_vision_prompt(self):
        self._vision_prompt_template = None
        logger.info("Przywrócono domyślny prompt dla VLM")
        return self

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        source_name = self._get_source_name(file_source)
        logger.info(f"Rozpoczynam przetwarzanie: {source_name}")
        self.reset_filter_stats()

        overall_start = time.time()
        temp_file = None

        try:
            if isinstance(file_source, str):
                pdf_path = file_source
            else:
                temp_file = self._save_temp_file(file_source)
                pdf_path = temp_file

            logger.info(f"Uruchamiam silnik Marker...")
            conv_start = time.time()

            rendered = self.converter(pdf_path)
            full_markdown = getattr(rendered, "markdown", "")
            extracted_images = getattr(rendered, "images", {})

            logger.info(f"Ekstrakcja zakończona w {time.time() - conv_start:.2f}s.")
            logger.info(f"Znaleziono {len(extracted_images)} obrazów.")

            pages_raw = full_markdown.split("\f")
            total_pages = len(pages_raw)
            logger.info(f"Wykryto {total_pages} stron.")

            final_documents = []
            max_pages_to_process = kwargs.get('max_pages', 999)

            # PRZETWARZANIE KAŻDEJ STRONY
            for i, page_content in enumerate(pages_raw):
                page_no = i + 1
                content = page_content.strip()
                if not content:
                    continue

                logger.info(f"Przetwarzanie strony {page_no}/{total_pages}...")

                # ZNAJDŹ WSZYSTKIE REFERENCJE DO OBRAZÓW wraz z całym markdown
                # Wzorzec: ![dowolny tekst](ścieżka)
                image_pattern = r'(!\[.*?\]\(([^)]+)\))'
                matches = re.findall(image_pattern, content)

                logger.info(f"  Znaleziono {len(matches)} referencji do obrazów")

                # PRZETWARZAJ KAŻDĄ REFERENCJĘ
                for full_markdown_ref, img_path in matches:
                    # full_markdown_ref to np: '![](image.jpg)' lub '![alt text](image.jpg)'
                    # img_path to np: '_page_0_Picture_0.jpeg'

                    logger.debug(f"  -> Referencja: '{full_markdown_ref}' -> ścieżka: '{img_path}'")

                    # Szukaj obrazu
                    pil_img = self._find_image(img_path, extracted_images)

                    if pil_img is None:
                        logger.debug(f"     NIE znaleziono obrazu PIL dla '{img_path}'")
                        continue

                    self._filter_stats['total_images'] += 1

                    # Sprawdź filtry
                    if self._should_process_image(pil_img, img_path):
                        self._filter_stats['accepted'] += 1
                        logger.info(f"     [VISION] Analizuję '{img_path}'...")
                        vlm_start = time.time()
                        desc = self._analyze_image_with_vlm(pil_img)
                        logger.info(f"     [VISION] OK ({time.time() - vlm_start:.2f}s)")

                        # ZAMIEŃ DOKŁADNĄ REFERENCJĘ (z alt textem jeśli jest)
                        replacement = f'{full_markdown_ref}\n\n{desc}\n'

                        # Użyj replace tylko RAZ dla tej konkretnej referencji
                        if full_markdown_ref in content:
                            content = content.replace(full_markdown_ref, replacement, 1)
                            logger.debug(f"     Wstawiono opis AI po obrazie")
                        else:
                            logger.warning(f"     BŁĄD: Nie znaleziono '{full_markdown_ref}' w content!")
                    else:
                        logger.debug(f"     [SKIP] Obraz odrzucony przez filtry")

                final_documents.append(
                    Document(
                        page_content=content,
                        metadata={
                            "page_number": page_no,
                            "total_pages": total_pages,
                            "source": source_name,
                            "parser": "marker_vision_llm"
                        }
                    )
                )

                if page_no >= max_pages_to_process:
                    logger.info(f"Osiągnięto limit {max_pages_to_process} stron.")
                    break

            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)

            logger.info(f"[STATS] Obrazów: {self._filter_stats['total_images']}, "
                        f"Przeanalizowanych: {self._filter_stats['accepted']}, "
                        f"Pominięto: {self._filter_stats['total_images'] - self._filter_stats['accepted']}")

            logger.info(f"SUKCES: {source_name} w {time.time() - overall_start:.2f}s.")
            return final_documents

        except Exception as e:
            logger.error(f"KRYTYCZNY BŁĄD: {e}", exc_info=True)
            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)
            return []

    def _find_image(self, img_ref: str, extracted_images: Dict) -> Optional[object]:
        """Szuka obrazu próbując różnych wariantów nazwy."""
        variants = [
            img_ref,
            os.path.basename(img_ref),
            os.path.splitext(img_ref)[0],
            os.path.splitext(os.path.basename(img_ref))[0],
        ]

        for variant in variants:
            if variant in extracted_images:
                return extracted_images[variant]

        # Fuzzy match
        for key in extracted_images.keys():
            if img_ref in key or key in img_ref:
                return extracted_images[key]

        return None

    def _should_process_image(self, pil_img, img_name: str) -> bool:
        try:
            if pil_img is None:
                self._filter_stats['rejected_no_image'] += 1
                return False

            width, height = pil_img.size

            if self._filters_config['size']['enabled']:
                if not self._filter_by_size(pil_img):
                    self._filter_stats['rejected_size'] += 1
                    return False

            if self._filters_config['aspect_ratio']['enabled']:
                if not self._filter_by_aspect_ratio(pil_img):
                    self._filter_stats['rejected_aspect_ratio'] += 1
                    return False

            return True

        except Exception as e:
            logger.warning(f"Błąd filtrowania: {e}")
            return False

    def _filter_by_size(self, pil_img) -> bool:
        width, height = pil_img.size
        area = width * height
        min_size = self._filters_config['size']['min_image_size']
        return area >= min_size

    def _filter_by_aspect_ratio(self, pil_img) -> bool:
        width, height = pil_img.size

        if height == 0:
            return False

        aspect_ratio = width / height
        area = width * height

        config = self._filters_config['aspect_ratio']
        min_ratio = config['min_aspect_ratio']
        max_ratio = config['max_aspect_ratio']
        square_threshold = config['square_logo_threshold']

        if 0.8 < aspect_ratio < 1.2 and area < square_threshold:
            return False

        if aspect_ratio < min_ratio or aspect_ratio > max_ratio:
            return False

        return True

    def _analyze_image_with_vlm(self, pil_img) -> str:
        try:
            if pil_img is None:
                return "[Błąd: Obraz jest pusty]"

            buffered = io.BytesIO()
            pil_img.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            message = HumanMessage(
                content=[
                    {"type": "text", "text": self._get_vision_prompt()},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}},
                ]
            )

            response = self.llm.invoke([message])
            return response.content.strip()

        except Exception as e:
            logger.error(f"Błąd analizy VLM: {e}", exc_info=True)
            return f"[Nie udało się przeanalizować obrazu: {str(e)}]"

    def _get_vision_prompt(self) -> str:
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

    def _get_source_name(self, source) -> str:
        return os.path.basename(source) if isinstance(source, str) else "stream_input.pdf"

    def _save_temp_file(self, source) -> str:
        temp_path = f"temp_marker_{int(time.time())}.pdf"
        with open(temp_path, "wb") as f:
            f.write(source.getbuffer() if isinstance(source, io.BytesIO) else source)
        return temp_path