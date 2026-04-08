import base64
import io
import logging
import os
import time
from typing import List, Union

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

# --- KONFIGURACJA TWOJEGO LLM ---
LLM_BASE_URL = "http://192.168.50.112:1234/v1"
LLM_MODEL = "Qwen2.5-vl-7B-Instruct"
LLM_API_KEY = "not-needed"


class PdfParser(BaseDocumentParser):
    """
    Parser PDF oparty na Marker (0.3.1+) z poprawionym dostępem do pól
    i analizą Vision (Qwen2.5-vl).
    """

    def __init__(self):
        logger.info("Inicjalizacja modeli Marker (API 0.3.x)...")
        start_init = time.time()

        # Ładowanie modeli lokalnych
        self.model_dict = create_model_dict()
        self.converter = PdfConverter(artifact_dict=self.model_dict)

        logger.info(f"Konfiguracja LLM: {LLM_MODEL}")
        self.llm = ChatOpenAI(
            base_url=LLM_BASE_URL,
            api_key=LLM_API_KEY,
            model=LLM_MODEL,
            max_tokens=1000,
            temperature=0.1
        )
        logger.info(f"PdfParser gotowy (Inicjalizacja: {time.time() - start_init:.2f}s).")

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        source_name = self._get_source_name(file_source)
        logger.info(f"[*] ROZPOCZYNAM PRZETWARZANIE: {source_name}")

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

            # rendered to obiekt klasy MarkdownOutput
            rendered = self.converter(pdf_path)

            # --- Używamy .markdown zamiast .markdown_text ---
            full_markdown = getattr(rendered, "markdown", "")
            extracted_images = getattr(rendered, "images", {})  # Słownik {nazwa: PIL.Image}

            logger.info(f"[{source_name}] Ekstrakcja zakończona w {time.time() - conv_start:.2f}s.")

            # 2. PODZIAŁ NA STRONY (\f to separator stron w Markerze)
            pages_raw = full_markdown.split("\f")
            total_pages = len(pages_raw)
            logger.info(f"[{source_name}] Wykryto {total_pages} stron.")

            final_documents = []
            max_pages_to_process = 10  # Limit dla benchmarku

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
                    # Marker wstawia ![](img_name.png) w tekst, szukamy tego odniesienia
                    if img_name in content:
                        logger.info(f"     [VISION] Analizuję grafikę '{img_name}'...")
                        vlm_start = time.time()
                        desc = self._analyze_image_with_vlm(pil_img)
                        logger.info(f"     [VISION] OK ({time.time() - vlm_start:.2f}s)")
                        image_descriptions.append(f"\n> 🖼️ **AI Vision ({img_name}):** {desc}\n")

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
                    logger.info(f"[*] Osiągnięto limit {max_pages_to_process} stron.")
                    break

            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)

            logger.info(f"[*] SUKCES: {source_name} w {time.time() - overall_start:.2f}s.")
            return final_documents

        except Exception as e:
            logger.error(f"KRYTYCZNY BŁĄD parsera MarkerLLM: {e}", exc_info=True)
            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)
            return []

    def _analyze_image_with_vlm(self, pil_img) -> str:
        """Przesyła obraz do modelu"""
        try:
            buffered = io.BytesIO()
            pil_img.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            message = HumanMessage(
                content=[
                    {"type": "text", "text": "Opisz dokładnie co przedstawia ten schemat techniczny ISO 20022."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}},
                ]
            )

            response = self.llm.invoke([message])
            return response.content.strip()
        except Exception as e:
            return f"[Błąd Vision: {str(e)}]"

    def _get_source_name(self, source) -> str:
        return os.path.basename(source) if isinstance(source, str) else "stream_input.pdf"

    def _save_temp_file(self, source) -> str:
        temp_path = f"temp_marker_{int(time.time())}.pdf"
        with open(temp_path, "wb") as f:
            f.write(source.getbuffer() if isinstance(source, io.BytesIO) else source)
        return temp_path