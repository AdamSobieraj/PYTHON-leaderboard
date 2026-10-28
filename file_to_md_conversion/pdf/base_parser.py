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

        Optional image contract: a parser that extracts images (pictures,
        figures, rendered page crops) should NOT write them to disk itself -
        it returns them in the Document metadata and the consuming script
        (e.g. basestartscript.py) saves them next to the output file. Each
        image is an entry of Document.metadata["images"], a list of dicts:
            {
                "path": "images/<doc>_<hash>/file.png",  # relative path
                        # (forward slashes) where the consumer saves the file
                "data": <bytes>,                         # encoded image
            }
        The Markdown content already references the images by that relative
        "path", so once the consumer saves the files the references resolve
        against the folder the .md file is written to. Parsers that extract
        no images simply omit the "images" key.
        """
        pass
