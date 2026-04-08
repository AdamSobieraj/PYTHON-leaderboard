import io
import logging
import os
import time
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
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from base_parser import BaseDocumentParser

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger("DoclingLlmParser")

# --- KONFIGURACJA LLM ---
LLM_BASE_URL = "http://192.168.50.112:1234/v1"
LLM_MODEL = "Qwen2.5-vl-7B-Instruct"
LLM_API_KEY = "not-needed"


class PdfParser(BaseDocumentParser):
    """
    Parser PDF oparty na IBM Docling z logowaniem postępu
    i analizą LLM (Qwen2.5-vl).
    """

    SKIP_LABELS: set = {"page_header", "page_footer"}

    def __init__(
            self,
            use_gpu: bool = True,
            do_ocr: bool = True,
            ocr_languages: Optional[List[str]] = None,
            table_mode: str = "accurate",
    ):
        logger.info("Inicjalizacja PdfParser (Docling + LLM)...")

        # 1. Wybór urządzenia
        self._device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
        logger.info(f"Wybrane urządzenie: {self._device.upper()}")

        accelerator = AcceleratorOptions(
            num_threads=4,
            device=AcceleratorDevice.CUDA if self._device == "cuda" else AcceleratorDevice.CPU,
        )

        # 2. Konfiguracja Docling
        pipeline_options = PdfPipelineOptions(
            do_ocr=do_ocr,
            do_table_structure=True,
            table_structure_options=TableStructureOptions(
                mode=TableFormerMode.ACCURATE if table_mode == "accurate" else TableFormerMode.FAST
            ),
            accelerator_options=accelerator,
        )

        if do_ocr:
            langs = ocr_languages or ["pl", "en"]
            logger.info(f"OCR włączony. Języki: {langs}")
            pipeline_options.ocr_options = EasyOcrOptions(lang=langs)

        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )

        # 3. Konfiguracja LLM
        logger.info(f"Łączenie z LLM: {LLM_MODEL} pod adresem {LLM_BASE_URL}")
        self.llm = ChatOpenAI(
            base_url=LLM_BASE_URL,
            api_key=LLM_API_KEY,
            model=LLM_MODEL,
            temperature=0.1
        )
        logger.info("PdfParser gotowy do pracy.")

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        source_name = self._get_source_name(file_source)
        logger.info(f"Rozpoczynam parsowanie pliku: {source_name}")

        start_time = time.time()

        try:
            # A. Konwersja Docling
            conv_source = self._prepare_source(file_source)
            logger.info(f"[{source_name}] Uruchamiam konwersję Docling (to może potrwać)...")

            result = self.converter.convert(conv_source)
            doc = result.document

            logger.info(f"[{source_name}] Konwersja Docling zakończona w {time.time() - start_time:.2f}s.")

            # B. Grupowanie elementów w strony z logowaniem postępu
            logger.info(f"[{source_name}] Rozpoczynam iterację po elementach dokumentu...")
            page_contents = defaultdict(list)
            element_count = 0
            last_logged_page = -1

            # doc.iterate_items() zwraca tysiące elementów dla dużych PDF
            for item, level in doc.iterate_items():
                element_count += 1

                label = getattr(item, "label", None)
                label_val = str(label.value) if hasattr(label, "value") else str(label)

                if label_val in self.SKIP_LABELS:
                    continue

                page_no = self._get_page_number(item)

                # Logowanie postępu co stronę lub co 500 elementów
                if page_no != last_logged_page:
                    logger.info(f"  -> Przetwarzanie strony: {page_no} (łącznie elementów: {element_count})")
                    last_logged_page = page_no
                elif element_count % 500 == 0:
                    logger.debug(f"     ...przetworzono {element_count} elementów...")

                md_fragment = self._item_to_markdown(item, level, doc)
                if md_fragment:
                    page_contents[page_no].append(md_fragment)

            logger.info(f"[{source_name}] Zakończono ekstrakcję. Przetworzono {element_count} elementów.")

            # C. Analiza LLM
            final_documents = []
            sorted_pages = sorted(page_contents.keys())
            total_pages_to_process = len(sorted_pages)

            # Limit dla benchmarku
            max_llm_pages = 5

            logger.info(f"[{source_name}] Rozpoczynam fazę LLM (limit: {max_llm_pages} stron).")

            for i, page_no in enumerate(sorted_pages):
                if page_no <= 0: continue

                raw_content = "\n\n".join(page_contents[page_no]).strip()
                if not raw_content: continue

                llm_summary = ""
                if i < max_llm_pages:
                    logger.info(f"  [LLM] Analizuję stronę {page_no}/{total_pages_to_process}...")
                    llm_start = time.time()
                    llm_summary = self._get_llm_summary(raw_content)
                    logger.info(f"  [LLM] Strona {page_no} gotowa ({time.time() - llm_start:.2f}s)")

                enriched_content = f"{llm_summary}\n\n{raw_content}" if llm_summary else raw_content

                final_documents.append(
                    Document(
                        page_content=enriched_content,
                        metadata={
                            "page_number": page_no,
                            "source": source_name,
                            "has_llm_summary": bool(llm_summary)
                        }
                    )
                )

            logger.info(f"[{source_name}] Cały proces zakończony sukcesem w {time.time() - start_time:.2f}s.")
            return final_documents

        except Exception as e:
            logger.error(f"BŁĄD: {str(e)}", exc_info=True)
            return []

    def _get_llm_summary(self, text: str) -> str:
        """Wysyła tekst strony do LLM """
        try:
            truncated_text = text[:3000]  # Qwen - krótszy kontekst startowy
            prompt = ChatPromptTemplate.from_messages([
                ("system", "Podsumuj tę stronę dokumentu jednym krótkim zdaniem."),
                ("user", "{text}")
            ])
            chain = prompt | self.llm
            response = chain.invoke({"text": truncated_text})
            summary = response.content.strip()
            logger.debug(f"LLM Response: {summary}")
            return f"> **AI Page Summary:** {summary}"
        except Exception as e:
            logger.warning(f"Nie udało się uzyskać podsumowania LLM: {e}")
            return ""

    def _get_page_number(self, item) -> int:
        if hasattr(item, "prov") and item.prov:
            return item.prov[0].page_no
        return 0

    def _item_to_markdown(self, item, level: int, doc) -> Optional[str]:
        """Konwertuje element na MD z obsługą PictureItem."""
        try:
            if hasattr(item, "export_to_markdown"):
                # Przekazanie doc jest krytyczne w Docling 2.x dla obrazów/tabel
                return item.export_to_markdown(doc=doc)
        except Exception as e:
            logger.debug(f"Błąd eksportu elementu: {e}")
        return getattr(item, "text", None)

    def _prepare_source(self, source):
        if isinstance(source, str): return source
        if isinstance(source, bytes): return DocumentStream(name="doc.pdf", stream=io.BytesIO(source))
        if isinstance(source, io.BytesIO): return DocumentStream(name="doc.pdf", stream=source)
        return source

    def _get_source_name(self, source):
        if isinstance(source, str): return os.path.basename(source)
        return "memory_stream.pdf"