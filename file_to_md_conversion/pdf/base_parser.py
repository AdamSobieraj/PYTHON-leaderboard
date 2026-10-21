import io
from abc import ABC, abstractmethod
from typing import List, Union
from langchain_core.documents import Document


class BaseDocumentParser(ABC):
    """Abstract base class for all document parsers."""

    @abstractmethod
    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        """
        Processes a file (local or an in-memory stream) and returns
        a list of Document objects (with content in Markdown format).
        """
        pass
