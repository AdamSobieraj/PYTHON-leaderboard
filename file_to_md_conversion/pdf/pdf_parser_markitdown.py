import io
import logging
import os
import tempfile
from typing import List, Optional, Union

import pymupdf  # PyMuPDF – page analysis, page splitting and OCR
from langchain_core.documents import Document
from markitdown import MarkItDown

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on MarkItDown (Microsoft) + PyMuPDF, adapted for contracts
    (mixed PDFs: text pages + scans of signatures, annexes, attachments).

    MarkItDown does not perform OCR for PDFs, so the file is processed page by page:
      - page with a text layer       -> MarkItDown (keeps Markdown structure),
      - image-only / near-empty page -> OCR (PyMuPDF + Tesseract),
      - page with no text or images  -> skipped (truly empty).

    OCR requires Tesseract with the language pack (e.g. 'pol') and, if it is not
    in the default location, the TESSDATA_PREFIX environment variable.
    """

    # If a page has images and fewer characters than this, it is treated as a scan
    # (e.g. a scanned page with only a printed page number in the text layer)
    MIN_TEXT_CHARS = 20

    def __init__(self, ocr_language: str = "pol", ocr_dpi: int = 300):
        """
        Args:
            ocr_language: Tesseract language code(s), e.g. "pol" or "pol+eng".
            ocr_dpi:      Resolution used for OCR rendering.
        """
        # llm_client=None means a purely local mode, no API calls
        self._converter = MarkItDown(llm_client=None, llm_model=None)
        self._ocr_language = ocr_language
        self._ocr_dpi = ocr_dpi

    # ------------------------------------------------------------------
    # Main method
    # ------------------------------------------------------------------

    def parse(
        self,
        file_source: Union[str, io.BytesIO, bytes],
        **kwargs,
    ) -> List[Document]:
        source_name = (
            os.path.basename(file_source)
            if isinstance(file_source, str)
            else "memory stream (MarkItDown)"
        )

        documents: List[Document] = []
        empty_pages: List[int] = []
        failed_pages: List[int] = []
        pdf_doc = None

        try:
            pdf_doc = self._open_pdf(file_source)

            for i, page in enumerate(pdf_doc):
                page_number = i + 1
                plain_text = page.get_text().strip()
                has_images = bool(page.get_images(full=True))

                if not plain_text and not has_images:
                    empty_pages.append(page_number)
                    continue

                method = "markitdown"
                text = ""

                try:
                    if plain_text:
                        text = self._convert_page_markitdown(pdf_doc, i)
                        if not text:
                            # Fallback: plain text from PyMuPDF
                            text = plain_text
                            method = "pymupdf-text"

                    # Scanned page (or a page where the text layer is just a footer)
                    if has_images and len(plain_text) < self.MIN_TEXT_CHARS:
                        ocr_text = self._ocr_page(page)
                        if len(ocr_text) > len(text):
                            text = ocr_text
                            method = "ocr"
                except Exception as e:
                    logger.error(
                        f"[MarkItDown] Page {page_number} error ('{source_name}'): {e}"
                    )
                    failed_pages.append(page_number)
                    continue

                if text:
                    documents.append(
                        Document(
                            page_content=text,
                            metadata={
                                "page_number": page_number,
                                "source": source_name,
                                "parser": "markitdown",
                                "extraction_method": method,
                            },
                        )
                    )
                else:
                    failed_pages.append(page_number)

            if empty_pages:
                logger.info(f"[MarkItDown] Skipped empty pages {empty_pages} ('{source_name}')")
            if failed_pages:
                logger.warning(
                    f"[MarkItDown] No text from pages {failed_pages} ('{source_name}') "
                    f"- check OCR (Tesseract, language pack, TESSDATA_PREFIX)"
                )
            if not documents:
                logger.warning(
                    f"[MarkItDown] File '{source_name}' returned an empty result after conversion."
                )

            logger.info(
                f"[MarkItDown] File '{source_name}' parsed. Pages: {len(documents)}."
            )
            return documents

        except Exception as e:
            logger.error(
                f"[MarkItDown] Error processing file '{source_name}': {e}",
                exc_info=True,
            )
            return []
        finally:
            if pdf_doc is not None:
                pdf_doc.close()

    # ------------------------------------------------------------------
    # Page-level processing
    # ------------------------------------------------------------------

    def _convert_page_markitdown(self, pdf_doc: pymupdf.Document, page_index: int) -> str:
        """Cuts a single page into a separate PDF and converts it with MarkItDown."""
        single = pymupdf.open()
        try:
            single.insert_pdf(pdf_doc, from_page=page_index, to_page=page_index)
            page_bytes = single.tobytes()
        finally:
            single.close()

        return self._convert_bytes_via_tempfile(page_bytes)

    def _ocr_page(self, page: pymupdf.Page) -> str:
        """Runs Tesseract OCR on a page (full-page OCR, ignoring the text layer)."""
        tessdata: Optional[str] = os.environ.get("TESSDATA_PREFIX")
        textpage = page.get_textpage_ocr(
            language=self._ocr_language,
            dpi=self._ocr_dpi,
            full=True,
            tessdata=tessdata,
        )
        return page.get_text(textpage=textpage).strip()

    def _convert_bytes_via_tempfile(self, raw_bytes: bytes) -> str:
        """
        Writes the bytes to a temporary .pdf file, converts it with MarkItDown
        and removes the file (also when an exception occurs).
        """
        # delete=False because MarkItDown opens the file by path itself
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_file:
            tmp_path = tmp_file.name
            tmp_file.write(raw_bytes)

        try:
            result = self._converter.convert(tmp_path)
            return (result.text_content or "").strip()
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    # ------------------------------------------------------------------
    # Loading the PDF (supports str, bytes, BytesIO)
    # ------------------------------------------------------------------

    @staticmethod
    def _open_pdf(file_source: Union[str, io.BytesIO, bytes]) -> pymupdf.Document:
        """Opens a PDF file from disk or memory."""
        if isinstance(file_source, str):
            return pymupdf.Document(file_source)
        if isinstance(file_source, bytes):
            return pymupdf.Document(stream=file_source, filetype="pdf")
        if isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            return pymupdf.Document(stream=file_source.read(), filetype="pdf")
        raise ValueError(f"[MarkItDown] Unsupported source type: {type(file_source)}")