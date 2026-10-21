import io
import logging
import os
from typing import List, Union

import pymupdf4llm
from langchain_core.documents import Document
from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on PyMuPDF4LLM.
    Recognizes page layout, extracts tables, lists and headings,
    and then converts everything into clean Markdown.
    """

    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        documents = []
        source_name = os.path.basename(file_source) if isinstance(file_source, str) else "strumień pamięci S3"

        # Margin configuration to be cropped (in typographic points)
        # A standard A4 page is about 842 points tall.
        # Usually 50-70 points is enough to remove the footer.
        BOTTOM_MARGIN_TO_CROP = 60

        # If there is also a repeating header at the top, you can crop the top too:
        TOP_MARGIN_TO_CROP = 50

        try:
            # 1. Load the PDF file, with support for RAM memory and local disk
            if isinstance(file_source, str):
                # From disk (Local Loader)
                pdf_doc = pymupdf.Document(file_source)
            elif isinstance(file_source, bytes):
                # Raw bytes (S3 Loader)
                pdf_doc = pymupdf.Document(stream=file_source, filetype="pdf")
            elif isinstance(file_source, io.BytesIO):
                # In-memory stream (S3 Loader)
                pdf_doc = pymupdf.Document(stream=file_source.read(), filetype="pdf")
            else:
                raise ValueError("Nieobsługiwany typ źródła dla PDF")

            # 1.5 Remove footers (CropBox trimming before LLM analysis)
            for page in pdf_doc:
                rect = page.rect  # Get the current page dimensions (x0, y0, x1, y1)

                # Define a new rectangle by cutting the bottom (decrease y1),
                # optionally cutting the top as well (increase y0)
                new_rect = pymupdf.Rect(
                    rect.x0,
                    rect.y0 + TOP_MARGIN_TO_CROP,  # Change to: rect.y0 + TOP_MARGIN_TO_CROP if you want to crop the header too
                    rect.x1,
                    rect.y1 - BOTTOM_MARGIN_TO_CROP
                )

                # Set the new working area of the page.
                # pymupdf4llm will take into account ONLY the text inside this rectangle.
                page.set_cropbox(new_rect)

            # 2. Conversion magic: generate Markdown split by pages
            # page_chunks=True returns a list of dictionaries, where each dictionary is one page
            md_pages = pymupdf4llm.to_markdown(doc=pdf_doc, page_chunks=True)

            # 3. Convert to LangChain Document format
            for i, page_data in enumerate(md_pages):
                # page_data["text"] contains the ready-made Markdown for the given page
                md_text = page_data.get("text", "").strip()

                if md_text:
                    doc = Document(
                        page_content=md_text,
                        metadata={"page_number": i + 1}
                    )
                    documents.append(doc)

            # 4. Free memory (very important for large PDFs!)
            pdf_doc.close()

            return documents

        except Exception as e:
            logger.error(f"Błąd przetwarzania PDF na Markdown ({source_name}): {e}")
            return []


'''
NOTE

The value 60 used in the code is in points (1 point = 1/72 of an inch). A standard A4 page is 842 points tall.
A value between 50 and 80 usually perfectly "eats" the page numbering and the footer without cutting into the actual
document text. If the footer is unusually tall, you can simply increase this number (e.g. to 100).

To transform PDF files into a true Markdown format (preserving headings, bold, lists,
and above all tables), we must abandon the pypdf library. That tool can only "spit out"
a plain text string and does not understand page layout.

Currently the best and fastest industry standard for PDF-to-Markdown conversion for RAG systems
is the pymupdf4llm library (created by the authors of PyMuPDF).

Most importantly - this library has a built-in page_chunks=True feature that splits the PDF perfectly into pages,
which fits our LangChain logic perfectly (1 page = 1 Document object).

It also supports reading files directly from RAM memory (for S3).

PyMuPDF (pymupdf) is written in C++. It is one of the fastest engines for PDF manipulation in the Python world.
Downloading and parsing a file from AWS S3 on the fly will be blazing fast.

Headings: Large, bold texts will be converted to ## and ### tags, so during chunking
(e.g. using MarkdownHeaderTextSplitter from LangChain) you can split the PDF precisely along logical
sections (chapters), not at random places in the middle of a sentence.
'''
