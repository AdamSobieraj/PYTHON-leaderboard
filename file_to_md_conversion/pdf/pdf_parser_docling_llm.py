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
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from base_parser import BaseDocumentParser

logger = logging.getLogger("DoclingVisionParser")

# --- KONFIGURACJA TWOJEGO LLM ---
LLM_BASE_URL = "http://192.168.50.112:1234/v1"
LLM_MODEL = "Qwen2.5-vl-7B-Instruct"
LLM_API_KEY = "not-needed"

class PdfParser(BaseDocumentParser):
    def __init__(
            self,
            use_gpu: bool = True,
            do_ocr: bool = True,
            table_mode: str = "accurate",
    ):
        self._device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"

        # 1. KONFIGURACJA DOCLING Z OBSŁUGĄ OBRAZÓW
        pipeline_options = PdfPipelineOptions(
            do_ocr=do_ocr,
            do_table_structure=True,
            generate_picture_images=True,  # <--- KLUCZOWE: Włączamy wycinanie obrazów
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

        # 2. KONFIGURACJA
        self.llm = ChatOpenAI(
            base_url=LLM_BASE_URL,
            api_key=LLM_API_KEY,
            model=LLM_MODEL,
            max_tokens=500
        )

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        source_name = self._get_source_name(file_source)
        logger.info(f"Rozpoczynam parsowanie VISION dla: {source_name}")

        try:
            conv_source = self._prepare_source(file_source)
            result = self.converter.convert(conv_source)
            doc = result.document

            page_contents = defaultdict(list)

            # Iteracja po elementach
            for item, level in doc.iterate_items():
                label = getattr(item, "label", None)
                label_val = str(label.value) if hasattr(label, "value") else str(label)

                if label_val in {"page_header", "page_footer"}:
                    continue

                page_no = 0
                if hasattr(item, "prov") and item.prov:
                    page_no = item.prov[0].page_no

                # --- LOGIKA OBSŁUGI OBRAZÓW ---
                if label_val == "picture":
                    logger.info(f"  [VISION] Wykryto obraz na stronie {page_no}. Analizuję przez Qwen...")
                    description = self._analyze_image_with_vlm(item)
                    page_contents[page_no].append(f"\n>**Analiza obrazu AI:** {description}\n")
                else:
                    # Standardowa konwersja tekstu/tabel
                    md_fragment = self._item_to_markdown(item, level, doc)
                    if md_fragment:
                        page_contents[page_no].append(md_fragment)

            # Budowanie finalnych dokumentów
            final_docs = []
            for p in sorted(page_contents.keys()):
                if p <= 0: continue
                final_docs.append(Document(
                    page_content="\n\n".join(page_contents[p]),
                    metadata={"page_number": p, "source": source_name}
                ))

            return final_docs

        except Exception as e:
            logger.error(f"Błąd VisionParser: {e}", exc_info=True)
            return []

    def _analyze_image_with_vlm(self, item) -> str:
        """Wysyła obrazek do LLM i pobiera jego opis."""
        try:
            # W Docling v2, item.image to obiekt ImageRef.
            # Musimy wyciągnąć z niego faktyczny obiekt PIL Image za pomocą .pil_image
            if not hasattr(item, "image") or item.image is None:
                return "[Błąd: Obraz nie został wygenerowany przez Docling]"

            # POBIERAMY PIL IMAGE Z OBIEKTU ImageRef
            pil_img = item.image.pil_image

            if pil_img is None:
                return "[Błąd: Nie udało się wyrenderować pil_image z ImageRef]"

            # Teraz możemy bezpiecznie wykonać .save()
            buffered = io.BytesIO()
            pil_img.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            # Przygotowanie wiadomości Vision dla modelu
            message = HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": "To jest schemat lub grafika z dokumentacji technicznej ISO 20022. Opisz bardzo dokładnie co przedstawia ten diagram, uwzględniając tekst widoczny na grafice."
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{img_base64}"},
                    },
                ]
            )

            # Wysłanie do Twojego lokalnego serwera
            response = self.llm.invoke([message])
            description = response.content.strip()

            # Logowanie kawałka odpowiedzi, żebyś widział postęp w konsoli
            logger.info(f"  [VISION Success] Analiza gotowa: {description[:50]}...")

            return description

        except Exception as e:
            logger.warning(f"Błąd analizy VLM: {e}")
            return f"[Nie udało się przeanalizować obrazu: {str(e)}]"

        except Exception as e:
            logger.warning(f"Błąd analizy VLM: {e}")
            return "[Nie udało się przeanalizować obrazu]"

    def _item_to_markdown(self, item, level, doc) -> Optional[str]:
        try:
            if hasattr(item, "export_to_markdown"):
                return item.export_to_markdown(doc=doc)
        except:
            pass
        return getattr(item, "text", None)

    def _prepare_source(self, source):
        if isinstance(source, str): return source
        return DocumentStream(name="doc.pdf", stream=io.BytesIO(source) if isinstance(source, bytes) else source)

    def _get_source_name(self, source):
        return os.path.basename(source) if isinstance(source, str) else "stream.pdf"