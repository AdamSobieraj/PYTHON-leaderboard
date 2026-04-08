import io
import logging
import os
import time
from typing import List, Union

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from base_parser import BaseDocumentParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MarkerLlmParser")

# --- KONFIGURACJA TWOJEGO LLM ---
LLM_BASE_URL = "http://192.168.50.112:1234/v1"
LLM_MODEL = "Qwen2.5-vl-7B-Instruct"
LLM_API_KEY = "not-needed"


class PdfParser(BaseDocumentParser):
    """
    Parser PDF oparty na najnowszej wersji Marker (0.3.x+)
    z analizą LLM (Qwen2.5-vl).
    """

    def __init__(self):
        logger.info("Inicjalizacja modeli Marker (nowe API 0.3+)...")

        # Nowy sposób ładowania modeli w Marker
        self.model_dict = create_model_dict()
        self.converter = PdfConverter(
            artifact_dict=self.model_dict,
        )

        logger.info(f"Konfiguracja LLM: {LLM_MODEL} na {LLM_BASE_URL}")
        self.llm = ChatOpenAI(
            base_url=LLM_BASE_URL,
            api_key=LLM_API_KEY,
            model=LLM_MODEL,
            temperature=0.1
        )
        logger.info("PdfParser (Marker+LLM) gotowy.")

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        source_name = self._get_source_name(file_source)
        logger.info(f"[{source_name}] Rozpoczynam konwersję Marker...")

        start_time = time.time()
        temp_file = None

        try:
            # Marker 0.3+ wymaga ścieżki do pliku
            if isinstance(file_source, str):
                pdf_path = file_source
            else:
                temp_file = self._save_temp_file(file_source)
                pdf_path = temp_file

            # 1. Konwersja za pomocą nowego API
            rendered = self.converter(pdf_path)
            full_text, _, metadata = rendered.model_dump().values()

            logger.info(f"[{source_name}] Marker zakończył ekstrakcję w {time.time() - start_time:.2f}s.")

            # 2. Podział na strony (Marker używa znaku \f - Form Feed)
            pages_raw = full_text.split("\f")
            if len(pages_raw) <= 1:
                # Fallback jeśli brak znaków podziału
                pages_raw = full_text.split("\n\n---\n\n")

            final_documents = []
            max_llm_pages = 5

            for i, page_content in enumerate(pages_raw):
                page_no = i + 1
                content = page_content.strip()
                if not content: continue

                llm_summary = ""
                if i < max_llm_pages:
                    logger.info(f"  [LLM] Analiza strony {page_no}...")
                    llm_summary = self._get_llm_summary(content)

                enriched_content = f"{llm_summary}\n\n{content}" if llm_summary else content

                final_documents.append(
                    Document(
                        page_content=enriched_content,
                        metadata={
                            "page_number": page_no,
                            "source": source_name,
                            "parser": "marker_0.3_llm",
                            "has_llm_summary": bool(llm_summary)
                        }
                    )
                )

            # Usuwamy plik tymczasowy jeśli powstał
            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)

            logger.info(f"[{source_name}] Proces zakończony. Łączny czas: {time.time() - start_time:.2f}s.")
            return final_documents

        except Exception as e:
            logger.error(f"Błąd parsera MarkerLLM: {e}", exc_info=True)
            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)
            return []

    def _get_llm_summary(self, text: str) -> str:
        try:
            prompt = ChatPromptTemplate.from_messages([
                ("system", "Podsumuj treść strony w jednym krótkim zdaniu."),
                ("user", "{text}")
            ])
            chain = prompt | self.llm
            response = chain.invoke({"text": text[:3000]})
            return f"> **Marker+AI Summary:** {response.content.strip()}"
        except Exception as e:
            logger.warning(f"LLM Error: {e}")
            return ""

    def _get_source_name(self, source):
        if isinstance(source, str): return os.path.basename(source)
        return "stream.pdf"

    def _save_temp_file(self, source: Union[io.BytesIO, bytes]) -> str:
        temp_path = f"temp_{int(time.time())}_marker.pdf"
        with open(temp_path, "wb") as f:
            f.write(source.getbuffer() if isinstance(source, io.BytesIO) else source)
        return temp_path