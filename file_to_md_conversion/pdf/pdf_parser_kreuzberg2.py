import io
import logging
import os
import asyncio
import concurrent.futures
from typing import List, Union

import fitz  # PyMuPDF – margin trimming and page analysis
from langchain_core.documents import Document
from kreuzberg import extract_bytes

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)


class PdfParser(BaseDocumentParser):
    """
    PDF parser (Kreuzberg + PyMuPDF), adapted for contracts (mixed PDFs:
    text pages + scans of signatures, annexes, attachments).

    Steps:
    1. Remove the content of the top and bottom margins (redaction instead of CropBox).
    2. Analyze each page: does it have a text layer / images.
    3. Page-by-page extraction:
       - page with text         -> regular extraction,
       - image-only page        -> forced OCR,
       - page with no text or images -> skipped (truly empty).
    """

    # Margins to remove (typographic points, 1 pt = 1/72 inch)
    TOP_MARGIN_TO_CROP = 50
    BOTTOM_MARGIN_TO_CROP = 60

    # Minimum content height that must remain after removing the margins
    MIN_CONTENT_HEIGHT = 50

    DEFAULT_LANGUAGE = "pol"

    # ------------------------------------------------------------------
    # Main method
    # ------------------------------------------------------------------

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        documents: List[Document] = []
        source_name = (
            os.path.basename(file_source)
            if isinstance(file_source, str)
            else "S3 memory stream"
        )

        pdf_doc = None
        try:
            pdf_doc = self._open_pdf(file_source)
            self._crop_margins(pdf_doc)

            empty_pages: List[int] = []
            failed_pages: List[int] = []

            for i, page in enumerate(pdf_doc):
                page_number = i + 1
                has_text = bool(page.get_text().strip())
                has_images = bool(page.get_images(full=True))

                if not has_text and not has_images:
                    empty_pages.append(page_number)
                    continue

                try:
                    text = self._extract_single_page(
                        pdf_doc, i, force_ocr=not has_text, **kwargs
                    )
                except Exception as e:
                    logger.error(
                        "Page %d extraction error (%s): %s", page_number, source_name, e
                    )
                    failed_pages.append(page_number)
                    continue

                if text:
                    documents.append(
                        Document(
                            page_content=text,
                            metadata={"page_number": page_number},
                        )
                    )
                else:
                    failed_pages.append(page_number)

            if empty_pages:
                logger.info(
                    "Skipped empty pages %s (%s)", empty_pages, source_name
                )
            if failed_pages:
                logger.warning(
                    "Failed to extract text from pages %s (%s) "
                    "- check OCR (Tesseract, language pack)",
                    failed_pages,
                    source_name,
                )
            if not documents:
                logger.warning(
                    "PDF file is empty or text extraction failed (%s)",
                    source_name,
                )

            logger.info(
                "Extracted %d pages from PDF (%s)", len(documents), source_name
            )
            return documents

        except Exception as e:
            logger.error(
                "Error converting PDF to Markdown (%s): %s", source_name, e
            )
            return []
        finally:
            if pdf_doc is not None:
                pdf_doc.close()

    # ------------------------------------------------------------------
    # Single page extraction
    # ------------------------------------------------------------------

    def _extract_single_page(
        self, pdf_doc: fitz.Document, page_index: int, force_ocr: bool, **kwargs
    ) -> str:
        """Cuts a single page into a separate PDF and runs it through Kreuzberg."""
        single = fitz.open()
        try:
            single.insert_pdf(pdf_doc, from_page=page_index, to_page=page_index)
            page_bytes = single.tobytes()
        finally:
            single.close()

        page_kwargs = dict(kwargs)
        page_kwargs.setdefault("language", self.DEFAULT_LANGUAGE)
        if force_ocr:
            page_kwargs["force_ocr"] = True

        result = self._run_extraction(page_bytes, **page_kwargs)
        return (result.content or "").strip()

    # ------------------------------------------------------------------
    # Loading the PDF (supports str, bytes, BytesIO)
    # ------------------------------------------------------------------

    @staticmethod
    def _open_pdf(file_source: Union[str, io.BytesIO, bytes]) -> fitz.Document:
        """Opens a PDF file from disk or memory."""
        if isinstance(file_source, str):
            return fitz.Document(file_source)
        if isinstance(file_source, bytes):
            return fitz.Document(stream=file_source, filetype="pdf")
        if isinstance(file_source, io.BytesIO):
            return fitz.Document(stream=file_source.read(), filetype="pdf")
        raise ValueError("Unsupported PDF source type")

    # ------------------------------------------------------------------
    # Removing headers / footers (redaction instead of CropBox)
    # ------------------------------------------------------------------

    def _crop_margins(self, pdf_doc: fitz.Document) -> None:
        """
        Removes the content of the top and bottom margins on every page.
        Unlike set_cropbox, it behaves the same for any extraction engine
        and OCR (it also removes image pixels within the margin area).
        """
        for page in pdf_doc:
            r = page.rect

            # Safeguard against pages too short for such margins
            if r.height <= self.TOP_MARGIN_TO_CROP + self.BOTTOM_MARGIN_TO_CROP + self.MIN_CONTENT_HEIGHT:
                continue

            top = fitz.Rect(r.x0, r.y0, r.x1, r.y0 + self.TOP_MARGIN_TO_CROP)
            bottom = fitz.Rect(r.x0, r.y1 - self.BOTTOM_MARGIN_TO_CROP, r.x1, r.y1)

            page.add_redact_annot(top)
            page.add_redact_annot(bottom)
            page.apply_redactions(
                images=fitz.PDF_REDACT_IMAGE_PIXELS,
                graphics=fitz.PDF_REDACT_LINE_ART_NONE,
            )

    # ------------------------------------------------------------------
    # Async -> sync handling (Kreuzberg has an async API)
    # ------------------------------------------------------------------

    def _run_extraction(self, pdf_bytes: bytes, **kwargs):
        """
        Runs the asynchronous Kreuzberg extraction in a synchronous context.
        If an asyncio event loop is already running (Jupyter, FastAPI),
        the extraction is run in a separate thread.
        """
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            return asyncio.run(self._async_extract(pdf_bytes, **kwargs))

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            return pool.submit(
                asyncio.run, self._async_extract(pdf_bytes, **kwargs)
            ).result()

    @staticmethod
    async def _async_extract(pdf_bytes: bytes, **kwargs):
        """
        Asynchronous content extraction from a PDF (bytes).
        Supported kwargs: force_ocr (bool), language (str, e.g. 'pol').
        """
        extra = {}
        if kwargs.get("force_ocr"):
            extra["force_ocr"] = True
        if kwargs.get("language"):
            extra["language"] = kwargs["language"]

        return await extract_bytes(
            pdf_bytes, mime_type="application/pdf", **extra
        )