import io
import logging
import os
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Dict, FrozenSet, List, Union

from langchain_core.documents import Document

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# ── Kluczowy krok: ustawiamy ścieżkę do konfiguracji ZANIM MinerU ──
# ── cokolwiek zaimportuje.  Zmienna środowiskowa musi być ustawiona  ──
# ── PRZED pierwszym importem magic_pdf.                              ──
_PROJECT_ROOT = Path(__file__).resolve().parent
_CONFIG_PATH = _PROJECT_ROOT / "magic-pdf.json"

if _CONFIG_PATH.exists():
    os.environ["MINERU_TOOLS_CONFIG_JSON"] = str(_CONFIG_PATH)
    logger.info("MinerU config → %s", _CONFIG_PATH)
else:
    logger.warning("Brak magic-pdf.json w %s — MinerU użyje domyślnej ścieżki ~/magic-pdf.json", _PROJECT_ROOT)


class PdfParser(BaseDocumentParser):
    """
    Parser plików PDF oparty na MinerU (magic-pdf) z akceleracją CUDA.

    Automatycznie rozpoznaje:
    - nagłówki / stopki / numerację stron  →  pomija
    - tabele                               →  tabele Markdown
    - wzory matematyczne                   →  LaTeX
    - skany / obrazy                       →  OCR
    """

    SKIP_CATEGORIES: FrozenSet[str] = frozenset(
        {"page_header", "page_footer", "page_number"}
    )

    def __init__(
        self,
        skip_headers_footers: bool = True,
    ) -> None:
        self._skip_headers_footers = skip_headers_footers

    # ──────────────────────────────────────────────────────────────
    #  Publiczne API
    # ──────────────────────────────────────────────────────────────
    def parse(
        self,
        file_source: Union[str, io.BytesIO, bytes],
        **kwargs,
    ) -> List[Document]:
        source_name = (
            os.path.basename(file_source)
            if isinstance(file_source, str)
            else "strumień pamięci S3"
        )

        try:
            # ── lazy import ──────────────────────────────────────
            from magic_pdf.data.dataset import PymuDocDataset
            from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze

            # 1. PDF → bajty
            pdf_bytes = self._read_source(file_source)

            # 2. Klasyfikacja: OCR vs tekst cyfrowy
            ds = PymuDocDataset(pdf_bytes)

            inference = ds.classify()
            ocr_mode = "ocr" in str(inference).lower()
            logger.info(
                "MinerU | %s | tryb: %s | device: CUDA (RTX 5090)",
                source_name,
                "OCR" if ocr_mode else "TXT",
            )

            # 3. Analiza layoutu (na GPU)
            infer_result = ds.apply(doc_analyze, ocr=ocr_mode)

            # 4. Ekstrakcja treści → dokumenty LangChain
            with tempfile.TemporaryDirectory() as tmp_dir:
                image_dir = os.path.join(tmp_dir, "images")
                os.makedirs(image_dir, exist_ok=True)

                content_list = infer_result.get_content_list(image_dir)

                documents = self._content_list_to_documents(
                    content_list,
                    source_name=source_name,
                    ocr_mode=ocr_mode,
                )

            logger.info(
                "MinerU | %s | wynik: %d stron",
                source_name,
                len(documents),
            )
            return documents

        except ImportError as exc:
            logger.error(
                "Brak MinerU: %s → pip install 'magic-pdf[full]'", exc
            )
            return []
        except Exception as exc:
            logger.error(
                "Błąd przetwarzania PDF (%s): %s",
                source_name,
                exc,
                exc_info=True,
            )
            return []

    # ──────────────────────────────────────────────────────────────
    #  Metody prywatne
    # ──────────────────────────────────────────────────────────────
    @staticmethod
    def _read_source(file_source: Union[str, io.BytesIO, bytes]) -> bytes:
        if isinstance(file_source, str):
            with open(file_source, "rb") as fh:
                return fh.read()
        if isinstance(file_source, bytes):
            return file_source
        if isinstance(file_source, io.BytesIO):
            return file_source.read()
        raise ValueError(f"Nieobsługiwany typ źródła: {type(file_source)}")

    def _content_list_to_documents(
        self,
        content_list: list,
        *,
        source_name: str,
        ocr_mode: bool,
    ) -> List[Document]:
        pages: Dict[int, List[str]] = defaultdict(list)

        for block in content_list:
            category = block.get("category_type") or block.get("type") or ""
            if self._skip_headers_footers and category in self.SKIP_CATEGORIES:
                continue

            page_idx: int = block.get("page_idx", 0)
            text = (block.get("text") or "").strip()
            if text:
                pages[page_idx].append(text)

        documents: List[Document] = []
        for page_idx in sorted(pages):
            md_text = "\n\n".join(pages[page_idx]).strip()
            if md_text:
                documents.append(
                    Document(
                        page_content=md_text,
                        metadata={
                            "page_number": page_idx + 1,
                            "source": source_name,
                            "parser": "MinerU",
                            "ocr_mode": ocr_mode,
                        },
                    )
                )
        return documents