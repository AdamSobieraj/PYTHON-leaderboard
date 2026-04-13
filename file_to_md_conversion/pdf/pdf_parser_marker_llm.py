import base64
import io
import logging
import os
import time
from typing import List, Union, Optional

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
    Parser PDF oparty na Marker (0.3.1+) z analizą Vision
    i konfigurowalnymi filtrami obrazów.
    """

    def __init__(self):
        logger.info("Inicjalizacja modeli Marker (API 0.3.x)...")
        start_init = time.time()

        # Ładowanie modeli lokalnych
        self.model_dict = create_model_dict()
        self.converter = PdfConverter(artifact_dict=self.model_dict)

        # Konfiguracja filtrów obrazów
        self._filters_config = {
            'size': {
                'enabled': True,
                'min_image_size': 10000,
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
            'rejected_aspect_ratio': 0,
            'rejected_no_image': 0,
        }

        # Konfiguracja promptu
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
        self._filters_config['aspect_ratio']['enabled'] = False
        logger.info("Wszystkie filtry: WYŁĄCZONE")
        return self

    def enable_all_filters(self):
        """Włącza wszystkie filtry z domyślnymi ustawieniami."""
        self._filters_config['size']['enabled'] = True
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
        logger.info(f"Rozpoczynam przetwarzanie: {source_name}")
        self.reset_filter_stats()

        overall_start = time.time()
        temp_file = None

        try:
            # Przygotowanie ścieżki do pliku
            if isinstance(file_source, str):
                pdf_path = file_source
            else:
                temp_file = self._save_temp_file(file_source)
                pdf_path = temp_file

            # 1. KONWERSJA MARKER
            logger.info(f"[{source_name}] Uruchamiam silnik Marker...")
            conv_start = time.time()

            rendered = self.converter(pdf_path)

            full_markdown = getattr(rendered, "markdown", "")
            extracted_images = getattr(rendered, "images", {})

            logger.info(f"[{source_name}] Ekstrakcja zakończona w {time.time() - conv_start:.2f}s.")
            logger.info(f"[{source_name}] Znaleziono {len(extracted_images)} obrazów.")

            # 2. PODZIAŁ NA STRONY
            pages_raw = full_markdown.split("\f")
            total_pages = len(pages_raw)
            logger.info(f"[{source_name}] Wykryto {total_pages} stron.")

            final_documents = []
            max_pages_to_process = kwargs.get('max_pages', 999)

            # 3. ANALIZA STRON I WIZJI
            for i, page_content in enumerate(pages_raw):
                page_no = i + 1
                content = page_content.strip()
                if not content:
                    continue

                logger.info(f"  -> Przetwarzanie strony {page_no}/{total_pages}...")

                # SZUKANIE I ANALIZA OBRAZÓW
                image_descriptions = []
                for img_name, pil_img in extracted_images.items():
                    if img_name in content:
                        self._filter_stats['total_images'] += 1

                        if self._should_process_image(pil_img, img_name):
                            self._filter_stats['accepted'] += 1
                            logger.info(f"     [VISION] Analizuję grafikę '{img_name}'...")
                            vlm_start = time.time()
                            desc = self._analyze_image_with_vlm(pil_img)
                            logger.info(f"     [VISION] OK ({time.time() - vlm_start:.2f}s)")
                            image_descriptions.append(f"\n{desc}\n")
                        else:
                            logger.debug(f"     [SKIP] Pominięto obraz '{img_name}'")

                if image_descriptions:
                    content += "\n" + "\n".join(image_descriptions)

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

            # Podsumowanie filtrowania
            logger.info(f"[STATS] Obrazów łącznie: {self._filter_stats['total_images']}")
            logger.info(f"[STATS] Zaakceptowanych: {self._filter_stats['accepted']}")
            logger.info(f"[STATS] Odrzuconych - brak obrazu: {self._filter_stats['rejected_no_image']}")
            logger.info(f"[STATS] Odrzuconych - rozmiar: {self._filter_stats['rejected_size']}")
            logger.info(f"[STATS] Odrzuconych - proporcje: {self._filter_stats['rejected_aspect_ratio']}")

            logger.info(f"SUKCES: {source_name} w {time.time() - overall_start:.2f}s.")
            return final_documents

        except Exception as e:
            logger.error(f"KRYTYCZNY BŁĄD parsera MarkerLLM: {e}", exc_info=True)
            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)
            return []

    def _should_process_image(self, pil_img, img_name: str) -> bool:
        """
        Główna metoda decydująca czy obraz powinien być wysłany do VLM.
        Uruchamia wszystkie włączone filtry.

        Uwaga: Marker nie dostarcza informacji o pozycji obrazu na stronie,
        więc filtr pozycji nie jest dostępny.
        """
        try:
            if pil_img is None:
                logger.debug(f"[REJECT] pil_image is None dla '{img_name}'")
                self._filter_stats['rejected_no_image'] += 1
                return False

            width, height = pil_img.size
            logger.debug(f"[DEBUG] Sprawdzam obraz '{img_name}' {width}x{height}px")

            # Filtr 1: Rozmiar obrazu
            if self._filters_config['size']['enabled']:
                if not self._filter_by_size(pil_img):
                    self._filter_stats['rejected_size'] += 1
                    return False

            # Filtr 2: Proporcje (aspect ratio)
            if self._filters_config['aspect_ratio']['enabled']:
                if not self._filter_by_aspect_ratio(pil_img):
                    self._filter_stats['rejected_aspect_ratio'] += 1
                    return False

            logger.debug(f"[ACCEPT] Obraz '{img_name}' ({width}x{height}) zaakceptowany do analizy")
            return True

        except Exception as e:
            logger.warning(f"Błąd podczas filtrowania obrazu '{img_name}': {e}", exc_info=True)
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

    def _analyze_image_with_vlm(self, pil_img) -> str:
        """Wysyła obrazek do LLM i pobiera jego opis."""
        try:
            if pil_img is None:
                return "[Błąd: Obraz jest pusty]"

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
                        "image_url": {"url": f"data:image/png;base64,{img_base64}"}
                    },
                ]
            )

            response = self.llm.invoke([message])
            return response.content.strip()

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

        return """Jesteś ekspertem od dokumentacji technicznej ISO 20022. Przeanalizuj schemat/diagram i wyjaśnij jego znaczenie biznesowe.

TWOJE ZADANIE:
1. Wyjaśnij CEL i ZNACZENIE tego schematu - co komunikuje, jakie koncepcje przedstawia
2. Zidentyfikuj wszystkie kluczowe pojęcia, skróty, kody i terminy techniczne widoczne na schemacie
3. Wyjaśnij RELACJE i PRZEPŁYW między elementami - jaka jest logika biznesowa
4. Stwórz tabelę pojęć z ich wyjaśnieniem

NIE OPISUJ jak schemat wygląda wizualnie (kolory, kształty, położenie) - WYJAŚNIJ CO ON OZNACZA.

WYMAGANY FORMAT ODPOWIEDZI:

## Cel schematu
[Wyjaśnij po co został stworzony ten schemat, jaką wiedzę przekazuje, jaki problem biznesowy/techniczny ilustruje]

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| [termin z grafiki] | [co to oznacza] |
| [kolejny termin] | [wyjaśnienie] |

## Logika i relacje
[Wyjaśnij jak elementy współpracują ze sobą, jaki jest przepływ informacji/procesu, jakie są zależności między pojęciami]

## Kluczowe wnioski
- [Wniosek 1 - co najważniejszego pokazuje ten schemat]
- [Wniosek 2]
- [Wniosek 3]

WAŻNE: Wyciągnij CAŁY tekst ze schematu i umieść go w tabeli pojęć z wyjaśnieniem. Jeśli schemat zawiera proces - opisz jego kroki. Jeśli zawiera hierarchię - wyjaśnij poziomy."""

    def _get_source_name(self, source) -> str:
        return os.path.basename(source) if isinstance(source, str) else "stream_input.pdf"

    def _save_temp_file(self, source) -> str:
        temp_path = f"temp_marker_{int(time.time())}.pdf"
        with open(temp_path, "wb") as f:
            f.write(source.getbuffer() if isinstance(source, io.BytesIO) else source)
        return temp_path