import io
import logging
import os
import tempfile
from typing import List, Union

from langchain_core.documents import Document
from markitdown import MarkItDown

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)


class PdfParser(BaseDocumentParser):
    """
    Parser dla plików PDF oparty na bibliotece MarkItDown (Microsoft).
    Konwertuje dokumenty PDF na format Markdown z zachowaniem struktury
    (nagłówki, listy, tabele).

    MarkItDown wspiera wiele formatów (PDF, DOCX, XLSX, PPTX, HTML itp.),
    co czyni go wszechstronnym narzędziem do pre-processingu RAG.
    """

    def __init__(self):
        # Inicjalizacja konwertera MarkItDown
        # llm_client=None oznacza tryb czysto lokalny, bez wywołań do API
        self._converter = MarkItDown(llm_client=None, llm_model=None)

    def parse(
        self,
        file_source: Union[str, io.BytesIO, bytes],
        **kwargs
    ) -> List[Document]:

        source_name = (
            os.path.basename(file_source)
            if isinstance(file_source, str)
            else "strumień pamięci (MarkItDown)"
        )

        try:
            markdown_text = self._convert_to_markdown(file_source)

            if not markdown_text or not markdown_text.strip():
                logger.warning(
                    f"[MarkItDown] Plik '{source_name}' "
                    f"zwrócił pusty wynik po konwersji."
                )
                return []

            # MarkItDown zwraca cały dokument jako jeden string Markdown.
            # Dzielimy go na "strony" po separatorach form feed (\f),
            # które niektóre konwertery PDF wstawiają jako znaczniki strony.
            pages = self._split_into_pages(markdown_text)

            documents = []
            for i, page_text in enumerate(pages):
                stripped = page_text.strip()
                if stripped:
                    doc = Document(
                        page_content=stripped,
                        metadata={
                            "page_number": i + 1,
                            "source": source_name,
                            "parser": "markitdown",
                        }
                    )
                    documents.append(doc)

            logger.info(
                f"[MarkItDown] Plik '{source_name}' sparsowany. "
                f"Stron/segmentów: {len(documents)}."
            )
            return documents

        except Exception as e:
            logger.error(
                f"[MarkItDown] Błąd przetwarzania pliku '{source_name}': {e}",
                exc_info=True
            )
            return []

    # ------------------------------------------------------------------
    # Metody prywatne
    # ------------------------------------------------------------------

    def _convert_to_markdown(self, file_source: Union[str, io.BytesIO, bytes]) -> str:
        """
        Wywołuje MarkItDown i zwraca surowy tekst Markdown.

        MarkItDown.convert() akceptuje:
          - ścieżkę do pliku (str)  → bezpośredni odczyt
          - obiekt BytesIO          → poprzez plik tymczasowy (obejście)
          - surowe bajty (bytes)    → poprzez plik tymczasowy (obejście)

        Uwaga: aktualne API MarkItDown nie obsługuje natywnie strumieni
        BytesIO, dlatego dla danych z pamięci RAM używamy pliku tymczasowego.
        """

        if isinstance(file_source, str):
            # Ścieżka lokalna — najprostszy przypadek
            result = self._converter.convert(file_source)
            return result.text_content

        # Dane binarne lub strumień → zapis do pliku tymczasowego
        if isinstance(file_source, bytes):
            raw_bytes = file_source
        elif isinstance(file_source, io.BytesIO):
            raw_bytes = file_source.read()
        else:
            raise ValueError(
                f"[MarkItDown] Nieobsługiwany typ źródła: {type(file_source)}"
            )

        return self._convert_bytes_via_tempfile(raw_bytes)

    def _convert_bytes_via_tempfile(self, raw_bytes: bytes) -> str:
        """
        Zapisuje bajty do tymczasowego pliku .pdf na dysku,
        konwertuje go przez MarkItDown, a następnie usuwa plik.
        Używa context managera, by mieć pewność że plik zostanie usunięty
        nawet w przypadku wyjątku.
        """
        # delete=False bo MarkItDown sam otwiera plik po ścieżce
        with tempfile.NamedTemporaryFile(
            suffix=".pdf",
            delete=False
        ) as tmp_file:
            tmp_path = tmp_file.name
            tmp_file.write(raw_bytes)

        try:
            result = self._converter.convert(tmp_path)
            return result.text_content
        finally:
            # Gwarantowane sprzątanie pliku tymczasowego
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    @staticmethod
    def _split_into_pages(markdown_text: str) -> List[str]:
        """
        Próbuje podzielić Markdown na logiczne strony.

        Strategia podziału (w kolejności priorytetu):
        1. Znak form feed (\\f) — wstawiany przez niektóre konwertery PDF
           jako jawny znacznik podziału strony.
        2. Jeśli brak \\f — zwraca cały dokument jako jedną "stronę",
           co jest zachowaniem bezpiecznym i zgodnym z interfejsem
           (1 Document = cały plik).
        """
        if "\f" in markdown_text:
            pages = markdown_text.split("\f")
            logger.debug(
                f"[MarkItDown] Znaleziono znaczniki \\f. "
                f"Podział na {len(pages)} stron."
            )
            return pages

        # Brak jawnych podziałów strony → jeden duży dokument
        logger.debug(
            "[MarkItDown] Brak znaczników \\f. "
            "Zwracam cały dokument jako jeden segment."
        )
        return [markdown_text]