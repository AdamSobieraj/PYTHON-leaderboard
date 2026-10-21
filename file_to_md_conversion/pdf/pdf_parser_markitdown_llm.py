import io
import logging
import os
import tempfile
import base64
from typing import List, Union

import pymupdf
from dotenv import load_dotenv
from langchain_core.documents import Document
from markitdown import MarkItDown
from openai import OpenAI

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# Minimum image size to skip icons/decorations (in pixels)
MIN_IMAGE_WIDTH  = 80
MIN_IMAGE_HEIGHT = 80

load_dotenv()

LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_MODEL = os.getenv("LLM_MODEL")
LLM_API_KEY = os.getenv("LLM_API_KEY")

DEFAULT_LLM_PROMPT = """You are an expert document OCR and layout parsing assistant. 
                       Extract the text, tables, and formatting from the provided document image 
                       and output it EXACTLY as clean Markdown. 
                       Rules:
                       - Preserve heading levels (#, ##, etc.)
                       Convert tables to Markdown tables.
                       - Do not add ANY conversational filler (e.g., 'Here is the markdown:').
                       - Stop generating immediately when you reach the end of the page content."""


class PdfParser(BaseDocumentParser):
    """
    PDF parser with a hybrid approach:
    - PyMuPDF     → text extraction and image detection
    - MarkItDown  → text conversion to Markdown
    - LLM (vision)→ image description via an OpenAI-compatible API
    """

    def __init__(
        self
    ):

        self._llm_client = OpenAI(
            base_url=LLM_BASE_URL,
            api_key=LLM_API_KEY,
        )

        self._converter = MarkItDown(
            llm_client=self._llm_client,
            llm_model=LLM_MODEL,
            llm_prompt=DEFAULT_LLM_PROMPT,
        )

        logger.info(
            f"[markitdownllm] Zainicjalizowano z modelem '{LLM_MODEL}' "
            f"na endpoincie '{LLM_BASE_URL}'."
        )

    def parse(
        self,
        file_source: Union[str, io.BytesIO, bytes],
        **kwargs
    ) -> List[Document]:

        source_name = (
            os.path.basename(file_source)
            if isinstance(file_source, str)
            else "strumień pamięci (markitdownllm)"
        )

        try:
            logger.info(f"[markitdownllm] Konwersja pliku '{source_name}'...")

            # 1. Load the PDF via PyMuPDF
            pdf_doc = self._load_pdf(file_source)

            # 2. Process page by page
            documents = []
            for page_index, page in enumerate(pdf_doc):
                page_num = page_index + 1
                page_content_parts = []

                # 2a. Page text via MarkItDown (through a temporary page file)
                page_md = self._extract_page_text_as_markdown(pdf_doc, page_index)
                if page_md.strip():
                    page_content_parts.append(page_md.strip())

                # 2b. Page images described by the LLM
                image_descriptions = self._describe_page_images(pdf_doc, page, page_num)
                if image_descriptions:
                    page_content_parts.extend(image_descriptions)

                # 2c. Assemble the full page
                full_page_content = "\n\n".join(page_content_parts).strip()

                if full_page_content:
                    doc = Document(
                        page_content=full_page_content,
                        metadata={
                            "page_number":  page_num,
                            "source":       source_name,
                            "parser":       "markitdown-llm",
                            "llm_model":    LLM_MODEL,
                            "llm_endpoint": LLM_BASE_URL,
                        }
                    )
                    documents.append(doc)

            pdf_doc.close()

            logger.info(
                f"[markitdownllm] Zakończono. "
                f"Stron: {len(documents)} z pliku '{source_name}'."
            )
            return documents

        except Exception as e:
            logger.error(
                f"[markitdownllm] Błąd przetwarzania '{source_name}': {e}",
                exc_info=True
            )
            return []

    # ──────────────────────────────────────────────────────────────────────────
    # Private methods
    # ──────────────────────────────────────────────────────────────────────────

    def _load_pdf(self, file_source: Union[str, io.BytesIO, bytes]) -> pymupdf.Document:
        """Loads a PDF from disk or RAM into a pymupdf.Document object."""
        if isinstance(file_source, str):
            return pymupdf.open(file_source)
        elif isinstance(file_source, bytes):
            return pymupdf.open(stream=file_source, filetype="pdf")
        elif isinstance(file_source, io.BytesIO):
            return pymupdf.open(stream=file_source.read(), filetype="pdf")
        else:
            raise ValueError(f"Nieobsługiwany typ źródła: {type(file_source)}")

    def _extract_page_text_as_markdown(
        self,
        pdf_doc: pymupdf.Document,
        page_index: int
    ) -> str:
        """
        Exports a single page as a separate PDF in RAM,
        then converts it to Markdown through MarkItDown.
        This gives us page-by-page text without LLM calls for the text.
        """
        try:
            # Create a new PDF with just this one page
            single_page_pdf = pymupdf.open()
            single_page_pdf.insert_pdf(pdf_doc, from_page=page_index, to_page=page_index)

            # Save to RAM
            pdf_bytes = single_page_pdf.tobytes()
            single_page_pdf.close()

            # MarkItDown via a temporary file
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp_path = tmp.name
                tmp.write(pdf_bytes)

            try:
                result = self._converter.convert(tmp_path)
                return result.text_content or ""
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)

        except Exception as e:
            logger.warning(f"[markitdownllm] Błąd ekstrakcji tekstu strony {page_index + 1}: {e}")
            return ""

    def _describe_page_images(
        self,
        pdf_doc: pymupdf.Document,
        page: pymupdf.Page,
        page_num: int
    ) -> List[str]:
        """
        Detects images on the page via PyMuPDF, filters out small icons,
        then sends each image to the vision LLM and returns the descriptions.
        """
        descriptions = []
        images = page.get_images(full=True)

        if not images:
            return descriptions

        logger.info(f"[markitdownllm] Strona {page_num}: znaleziono {len(images)} obrazów.")

        # Track already-processed xrefs so duplicates are not described
        processed_xrefs = set()

        for img_info in images:
            xref = img_info[0]

            if xref in processed_xrefs:
                continue
            processed_xrefs.add(xref)

            try:
                image_data = pdf_doc.extract_image(xref)
                width      = image_data["width"]
                height     = image_data["height"]

                # Skip small icons and decorations
                if width < MIN_IMAGE_WIDTH or height < MIN_IMAGE_HEIGHT:
                    logger.debug(
                        f"[markitdownllm] Pominięto mały obraz "
                        f"xref={xref} ({width}x{height}px) na stronie {page_num}."
                    )
                    continue

                img_bytes  = image_data["image"]
                img_ext    = image_data["ext"]  # png, jpeg, etc.
                img_base64 = base64.b64encode(img_bytes).decode("utf-8")
                mime_type  = f"image/{img_ext}"

                logger.info(
                    f"[markitdownllm] Opisuję obraz xref={xref} "
                    f"({width}x{height}px) ze strony {page_num}..."
                )

                description = self._call_llm_vision(img_base64, mime_type)

                if description:
                    # Wrap the description in a Markdown block with metadata
                    block = (
                        f"<!-- Obraz ze strony {page_num} ({width}x{height}px) -->\n"
                        f"{description}"
                    )
                    descriptions.append(block)

            except Exception as e:
                logger.warning(
                    f"[markitdownllm] Błąd opisu obrazu xref={xref} "
                    f"na stronie {page_num}: {e}"
                )

        return descriptions

    def _call_llm_vision(self, img_base64: str, mime_type: str) -> str:
        """
        Sends the image (base64) to the LLM via the OpenAI vision API
        and returns the textual description in Markdown.
        """
        response = self._llm_client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": DEFAULT_LLM_PROMPT
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime_type};base64,{img_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1024,
            temperature=0.1,  # Low temperature = more deterministic descriptions
        )

        return response.choices[0].message.content.strip()