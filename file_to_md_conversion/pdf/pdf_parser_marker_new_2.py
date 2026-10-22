import os
import platform

# Set backend PyTorch for Apple Silicon before import torch/marker
if platform.system() == "Darwin" and platform.machine() == "arm64":
    os.environ.setdefault("TORCH_DEVICE", "mps")
    os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

import io
import logging
import math
import re
import tempfile
import threading
# FIX: removed duplicate `import os` (was imported twice in the original file)
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

import torch
from langchain_core.documents import Document

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

try:
    import pymupdf  # PyMuPDF
    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False
    logger.warning(
        "PyMuPDF not available! Header/footer removal and page classification will not work."
    )

try:
    # API for newer Marker-PDF versions (v1.0+)
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.config.parser import ConfigParser
    MARKER_AVAILABLE = True
except ImportError:
    MARKER_AVAILABLE = False

# ======================================================================
# SETTINGS
# ======================================================================

# Master switch: remove headers and footers before extraction?
REMOVE_HEADERS_FOOTERS = False

# How to find headers / footers (used only if REMOVE_HEADERS_FOOTERS is True):
#   "auto"  - removes only text blocks in the top/bottom zone that REPEAT across
#             pages (page numbers, running titles). Safe for energy certificates,
#             plans and tables. Works only on pages with a text layer.
#   "fixed" - removes fixed margins (below) from every page, including scans.
#             Risky for mixed documents (may delete real content near the edge).
HEADER_FOOTER_MODE = "auto"

# --- "fixed" mode ---
FIXED_TOP_MARGIN_PT = 50          # 1 pt = 1/72 inch
FIXED_BOTTOM_MARGIN_PT = 60
FIXED_MIN_CONTENT_HEIGHT_PT = 50  # pages shorter than margins + this are left untouched

# --- "auto" mode ---
AUTO_HEADER_ZONE_RATIO = 0.10     # top 10% of the page height is the header zone
AUTO_FOOTER_ZONE_RATIO = 0.10     # bottom 10% is the footer zone
AUTO_MIN_REPEAT_PAGES = 3         # a block must repeat on at least this many pages...
AUTO_MIN_REPEAT_RATIO = 0.30      # ...and on at least this share of pages with text
AUTO_MAX_BLOCK_CHARS = 200        # longer blocks are never treated as header/footer
# FIX / KNOWN LIMITATION: the repetition threshold above is computed GLOBALLY
# across the whole stitched file (see _find_repeated_blocks). If the PDF
# contains many DIFFERENT contract templates (each appearing only once or
# twice), a template-specific letterhead will never reach the repetition
# threshold and will NOT be removed, while the most common template in the
# file will be cleaned. A more correct approach would compute repetition
# PER section_index (i.e. per stitched sub-document) instead of globally.
# This is not implemented here because of a chicken-and-egg dependency:
# section_index is only known AFTER page classification, and classification
# currently runs AFTER header/footer redaction (so that a page containing
# only a page number becomes 'blank'). Doing per-section redaction would
# require a first classification pass BEFORE redaction, which is less
# reliable (a header/footer block long enough to exceed MIN_TEXT_CHARS could
# make a blank-looking page be misclassified as 'text', creating a false
# section boundary). Left as a documented limitation for now.

# --- Page classification ---
MIN_TEXT_CHARS = 20               # fewer characters in the text layer = "no real text"
BLANK_INK_RATIO = 0.001           # share of "ink" pixels below which a page is blank
INK_DELTA = 50                    # pixel is "ink" if darker than background by this much
CLASSIFY_MAX_PX = 800             # longer side of the low-res render used for classification

# --- OCR noise filter (OCR on plans/photos returns garbage) ---
MIN_OCR_LETTERS = 10
MIN_OCR_LETTER_RATIO = 0.4        # letters / non-space characters

# --- Pages without extractable text (plans, drawings, photos, stamps) ---
INCLUDE_NON_TEXT_PAGES = True     # keep them as a short placeholder Document
NON_TEXT_PLACEHOLDER = "[Strona bez tekstu: rysunek, plan lub obraz]"


@dataclass
class PageInfo:
    """Result of the page analysis (1-based page number)."""
    number: int
    kind: str            # 'text' | 'scan' | 'drawing' | 'blank'
    section_index: int   # index of the stitched document (blank pages = boundaries)
    plain_text: str      # text layer from PyMuPDF (fallback for Marker)


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on Marker (Surya OCR + DL models) + PyMuPDF, for "stitched"
    contracts: many documents in one file (contracts, energy certificates,
    plans, Excel printouts), separated by blank pages.
    Requires GPU acceleration for acceptable performance.

    Steps:
    1. Optionally remove headers / footers (see REMOVE_HEADERS_FOOTERS).
    2. Classify every page: text | scan | drawing | blank.
    3. Convert the whole file with Marker (pages are never deleted, so Marker's
       page numbers match the original file).
    4. Build one Document per page:
       - text    -> Marker output (fallback: PyMuPDF text layer),
       - scan    -> Marker OCR output, noise-filtered,
       - drawing -> placeholder (plan / image without text),
       - blank   -> skipped; blank pages also mark a boundary between documents
                    (metadata["section_index"]).
    """

    # Surya models are heavy (VRAM) - load them once per process
    _shared_models = None
    _shared_models_lock = threading.Lock()

    # Marker is not thread-safe - serialize conversions
    _convert_lock = threading.Lock()

    # Marker page separator with paginate_output=True, e.g. "\n\n{0}------...------\n\n"
    # (Marker page numbering starts at 0)
    _PAGE_SEPARATOR_RE = re.compile(r"\n*\{(\d+)\}-{10,}\n*")

    # Markdown image references (Marker emits them for figures)
    _MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")

    # FIX (list numbering): Marker renders list items with its own markdown
    # prefix ("1. " or "- ") while the original numbering from the PDF stays in
    # the text, which yields "1. 2. Text" instead of "2. Text".
    #   "1. 2. Strony zobowiazuja sie..."  ->  "2. Strony zobowiazuja sie..."
    #   "- 2) Strony..."                   ->  "2) Strony..."
    # Hierarchical numbering ("1.1", "2.3.1") and ordinary lists ("1. Text")
    # are left untouched. To also handle letters ("a)", "b)") change the second
    # group to (\d{1,3}[.)]|[a-zA-Z][.)]).
    _LIST_PREFIX_DUP_RE = re.compile(
        r"^([ \t]*)(?:\d{1,3}\.|[-*+])[ \t]+(\d{1,3}[.)])[ \t]+",
        re.MULTILINE,
    )

    def __init__(self, languages: str = "pl,en"):
        """
        Args:
            languages: Comma-separated language codes (e.g. "pl,en").
                       May be ignored in newer Marker versions.
        """
        if not MARKER_AVAILABLE:
            raise ImportError("Install Marker: pip install marker-pdf")

        if REMOVE_HEADERS_FOOTERS and not FITZ_AVAILABLE:
            logger.warning("Header/footer removal enabled, but PyMuPDF is missing! Install 'pymupdf'.")
        elif REMOVE_HEADERS_FOOTERS:
            logger.info(f"Header/footer removal: ON (mode={HEADER_FOOTER_MODE})")
        else:
            logger.info("Header/footer removal: OFF")

        # ── GPU / Marker models ──────────────────────────────────
        # Note: the device is chosen by Marker itself (TORCH_DEVICE environment
        # variable, set BEFORE importing Marker). The value below is informational only.
        self._device = self._detect_device()
        self.models = self._get_shared_models()

        # Converter configuration (paginate_output -> page separators in Markdown)
        config_dict = ConfigParser(
            {"languages": languages, "paginate_output": True}
        ).generate_config_dict()
        self.converter = PdfConverter(
            config=config_dict,
            artifact_dict=self.models,
        )

        self.languages = languages

        # FIX: hard, queryable counter for the "no page separators found"
        # fallback path, instead of relying solely on an easily-missed
        # logger.warning. Incremented in parse() under _stats_lock.
        self._fallback_whole_document_count = 0
        self._stats_lock = threading.Lock()

        logger.info("MarkerPdfParser ready.")

    # ══════════════════════════════════════════════════════════════
    # PUBLIC INTERFACE
    # ══════════════════════════════════════════════════════════════

    def parse(
        self,
        file_source: Union[str, io.BytesIO, bytes],
        **kwargs,
    ) -> List[Document]:
        """
        Processes a PDF -> list of Documents (one Document per non-blank page).
        """
        source_name = self._get_source_name(file_source)
        temp_pdf_path = None
        pdf_doc = None

        try:
            # ── 1. Header/footer removal + page analysis (PyMuPDF) ──
            pages_info: Optional[List[PageInfo]] = None

            if FITZ_AVAILABLE:
                pdf_doc = pymupdf.Document(
                    stream=self._get_bytes(file_source), filetype="pdf"
                )
                if REMOVE_HEADERS_FOOTERS:
                    logger.info(f"Removing headers/footers: {source_name}")
                    self._remove_headers_footers(pdf_doc)

                # Classification runs AFTER removal, so a page that contained only
                # a page number becomes 'blank'
                pages_info = self._analyze_pages(pdf_doc)

                if all(p.kind == "blank" for p in pages_info):
                    logger.warning(f"All pages are blank in '{source_name}'")
                    return []

                pdf_to_process = pdf_doc.tobytes()
            else:
                pdf_to_process = self._get_bytes(file_source)

            # ── 2. Write to a temporary file ─────────────────────
            # PdfConverter takes a file path, so a temporary file is required.
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
                temp_pdf.write(pdf_to_process)
                temp_pdf_path = temp_pdf.name

            # ── 3. Marker conversion (GPU), serialized ───────────
            logger.info(f"Starting Marker (Surya) conversion: {source_name}")
            with self._convert_lock:
                rendered = self.converter(temp_pdf_path)
            md_text = (rendered.markdown or "").strip()
            # FIX (list numbering): remove the duplicated list prefix added by Marker
            md_text = self._fix_list_numbering(md_text)
            logger.info(f"Conversion finished: {source_name}")

            # ── 4. Building documents ────────────────────────────
            if pages_info is None:
                # No PyMuPDF -> no classification, only Marker's own pagination
                documents = self._build_documents_unclassified(md_text, source_name)
            else:
                marker_pages = self._split_marker_pages(md_text)
                if marker_pages is None:
                    # FIX: increment hard counter in addition to the warning,
                    # so this degraded path is queryable via diagnostics()
                    # instead of relying solely on logs.
                    with self._stats_lock:
                        self._fallback_whole_document_count += 1
                        fallback_count = self._fallback_whole_document_count
                    logger.warning(
                        f"No page separators detected in Marker output ({source_name}). "
                        f"Returning the whole text as a single Document. "
                        f"(cumulative fallback count: {fallback_count})"
                    )
                    documents = (
                        [Document(page_content=md_text, metadata=self._base_metadata(source_name))]
                        if md_text
                        else []
                    )
                else:
                    if marker_pages and max(marker_pages) > len(pages_info):
                        logger.warning(
                            f"Marker returned page {max(marker_pages)} but the file has "
                            f"{len(pages_info)} pages ({source_name}) - page numbers may be misaligned."
                        )
                    documents = self._build_documents(marker_pages, pages_info, source_name)

            if not documents:
                logger.warning(f"No content extracted for '{source_name}'")
            else:
                logger.info(f"Extracted {len(documents)} pages from '{source_name}'")
            return documents

        except Exception as e:
            logger.error(f"Marker error ({source_name}): {e}", exc_info=True)
            return []

        finally:
            if pdf_doc is not None:
                pdf_doc.close()

            # Temporary file cleanup
            if temp_pdf_path and os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)

            # Free VRAM
            self._cleanup_gpu()

    def diagnostics(self) -> Dict[str, str]:
        """Diagnostic information for Marker."""
        with self._stats_lock:
            fallback_count = self._fallback_whole_document_count

        info = {
            "device": self._device,
            "languages": self.languages,
            "remove_headers_footers": str(REMOVE_HEADERS_FOOTERS),
            "header_footer_mode": HEADER_FOOTER_MODE,
            "pymupdf_available": str(FITZ_AVAILABLE),
            "torch_version": torch.__version__,
            "cuda_available": str(torch.cuda.is_available()),
            # FIX: expose the fallback counter so degraded conversions
            # (whole-document fallback due to missing page separators)
            # are visible in monitoring, not just in logs.
            "fallback_whole_document_count": str(fallback_count),
        }
        if torch.cuda.is_available():
            info["gpu_name"] = torch.cuda.get_device_name(0)
            info["gpu_vram_gb"] = f"{torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f}"
        return info

    # ══════════════════════════════════════════════════════════════
    # MARKDOWN POST-PROCESSING
    # ══════════════════════════════════════════════════════════════

    @classmethod
    def _fix_list_numbering(cls, text: str) -> str:
        """
        Removes the list prefix added by Marker when the content already
        carries its own number from the PDF ("1. 2. Text" -> "2. Text").
        Page separators ("{0}------...") start with '{', so they are never touched.
        """
        return cls._LIST_PREFIX_DUP_RE.sub(r"\1\2 ", text)

    # ══════════════════════════════════════════════════════════════
    # PAGE ANALYSIS (classification + section boundaries)
    # ══════════════════════════════════════════════════════════════

    def _analyze_pages(self, pdf_doc: "pymupdf.Document") -> List[PageInfo]:
        """Classifies every page and assigns section_index (blank pages = boundaries)."""
        result: List[PageInfo] = []
        section_index = 0
        pending_gap = False   # a blank page was seen after some content
        has_content = False

        for i, page in enumerate(pdf_doc):
            plain_text = page.get_text().strip()
            kind = self._classify_page(page, plain_text)

            if kind == "blank":
                if has_content:
                    pending_gap = True
            else:
                # First content page after a gap -> new stitched document
                if pending_gap:
                    section_index += 1
                    pending_gap = False
                has_content = True

            result.append(
                PageInfo(
                    number=i + 1,
                    kind=kind,
                    section_index=section_index,
                    plain_text=plain_text,
                )
            )

        counts = Counter(p.kind for p in result)
        logger.info(f"Page classification: {dict(counts)}, sections: {section_index + 1}")
        return result

    def _classify_page(self, page: "pymupdf.Page", plain_text: str) -> str:
        """Returns 'text' | 'scan' | 'drawing' | 'blank'."""
        if len(plain_text) >= MIN_TEXT_CHARS:
            return "text"

        if self._ink_ratio(page) < BLANK_INK_RATIO:
            return "blank"  # truly empty page or a scan of an empty page

        return "scan" if page.get_images(full=True) else "drawing"

    @staticmethod
    def _ink_ratio(page: "pymupdf.Page") -> float:
        """
        Share of 'ink' pixels in a low-resolution render. Works for images and
        vector graphics alike. The background level is estimated from the page
        itself, so off-white scans of empty pages are still recognized as blank.
        """
        r = page.rect
        scale = min(40 / 72, CLASSIFY_MAX_PX / max(r.width, r.height))
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(scale, scale),
            colorspace=pymupdf.csGRAY,
            alpha=False,
        )
        samples = pix.samples
        if not samples:
            return 0.0

        hist = Counter(samples)
        background = max(hist, key=hist.get)
        ink = sum(count for value, count in hist.items() if value < background - INK_DELTA)
        return ink / len(samples)

    @staticmethod
    def _is_noise(text: str) -> bool:
        """True if OCR output looks like garbage (typical for plans and photos)."""
        compact = re.sub(r"\s", "", text or "")
        if not compact:
            return True
        letters = sum(ch.isalpha() for ch in compact)
        return letters < MIN_OCR_LETTERS or letters / len(compact) < MIN_OCR_LETTER_RATIO

    # ══════════════════════════════════════════════════════════════
    # BUILDING DOCUMENTS
    # ══════════════════════════════════════════════════════════════

    def _split_marker_pages(self, md_text: str) -> Optional[Dict[int, str]]:
        """
        Splits Marker's Markdown by its page separators.
        Returns {page_number (1-based): text}, or None if no separators were found.
        """
        matches = list(self._PAGE_SEPARATOR_RE.finditer(md_text))
        if not matches:
            return None

        pages: Dict[int, str] = {}
        for idx, match in enumerate(matches):
            start = match.end()
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md_text)
            page_text = md_text[start:end].strip()
            if page_text:
                pages[int(match.group(1)) + 1] = page_text  # Marker counts from 0
        return pages

    def _build_documents(
        self,
        marker_pages: Dict[int, str],
        pages_info: List[PageInfo],
        source_name: str,
    ) -> List[Document]:
        """Combines Marker output with the page analysis into one Document per page."""
        documents: List[Document] = []
        blank_pages: List[int] = []
        non_text_pages: List[int] = []
        failed_pages: List[int] = []

        for info in pages_info:
            if info.kind == "blank":
                blank_pages.append(info.number)
                continue

            text = marker_pages.get(info.number, "")
            page_type = info.kind
            method = "marker"

            if info.kind == "text":
                if not text:
                    # Fallback: text layer from PyMuPDF
                    text = info.plain_text
                    method = "pymupdf-text"
                # FIX: this branch is currently unreachable in practice, because
                # info.kind == "text" implies len(info.plain_text) >= MIN_TEXT_CHARS
                # (see _classify_page), so `text` can never be empty here at this
                # point. Left in place defensively in case the classification
                # logic above changes in the future (e.g. MIN_TEXT_CHARS tuning,
                # or plain_text consisting only of whitespace/control characters).
                if not text:
                    failed_pages.append(info.number)
                    continue
            else:  # 'scan' or 'drawing'
                without_images = self._MD_IMAGE_RE.sub("", text).strip()
                if self._is_noise(without_images):
                    text = info.plain_text  # whatever short text exists, may be empty
                    method = "pymupdf-text"
                    page_type = "drawing"

            # FIX: previously this only checked `if not text:`, so a short,
            # noisy PyMuPDF fallback (1-19 chars of garbage, e.g. a stray
            # scan artifact) could slip through as "real" content without a
            # placeholder. Now we also re-check _is_noise() on the fallback
            # text itself.
            if not text or self._is_noise(text):
                non_text_pages.append(info.number)
                if not INCLUDE_NON_TEXT_PAGES:
                    continue
                text = NON_TEXT_PLACEHOLDER
                method = "placeholder"

            metadata = self._base_metadata(source_name)
            metadata.update(
                {
                    "page_number": info.number,
                    "page_type": page_type,
                    "section_index": info.section_index,
                    "extraction_method": method,
                }
            )
            documents.append(Document(page_content=text, metadata=metadata))

        if blank_pages:
            logger.info(f"Skipped blank pages {blank_pages} ({source_name})")
        if non_text_pages:
            logger.info(f"Pages without extractable text (plans/images) {non_text_pages} ({source_name})")
        if failed_pages:
            logger.warning(f"No text from pages {failed_pages} ({source_name})")

        return documents

    def _build_documents_unclassified(self, md_text: str, source_name: str) -> List[Document]:
        """Fallback without PyMuPDF: only Marker's pagination (no page analysis)."""
        if not md_text:
            return []

        marker_pages = self._split_marker_pages(md_text)
        if marker_pages is None:
            return [Document(page_content=md_text, metadata=self._base_metadata(source_name))]

        documents = []
        for number, text in sorted(marker_pages.items()):
            metadata = self._base_metadata(source_name)
            metadata["page_number"] = number
            documents.append(Document(page_content=text, metadata=metadata))
        return documents

    @staticmethod
    def _base_metadata(source_name: str) -> Dict[str, object]:
        return {
            "source": source_name,
            "parser": "marker",
            "headers_footers_removed": REMOVE_HEADERS_FOOTERS,
        }

    # ══════════════════════════════════════════════════════════════
    # HEADER / FOOTER REMOVAL (PyMuPDF redaction)
    # ══════════════════════════════════════════════════════════════

    def _remove_headers_footers(self, pdf_doc: "pymupdf.Document") -> None:
        """
        Removes headers / footers by redaction (behaves the same for every
        extraction engine). Pages are never deleted, so page numbers stay
        aligned with the original file.
        """
        if HEADER_FOOTER_MODE == "auto":
            rects_by_page = self._find_repeated_blocks(pdf_doc)
            image_mode = pymupdf.PDF_REDACT_IMAGE_NONE  # text blocks only
        elif HEADER_FOOTER_MODE == "fixed":
            rects_by_page = self._fixed_margin_rects(pdf_doc)
            image_mode = pymupdf.PDF_REDACT_IMAGE_PIXELS  # also clears scanned pixels
        else:
            raise ValueError(
                f"Unknown HEADER_FOOTER_MODE: {HEADER_FOOTER_MODE!r} (use 'auto' or 'fixed')"
            )

        pages_redacted = 0
        for i, page in enumerate(pdf_doc):
            rects = rects_by_page.get(i)
            if not rects:
                continue
            for rect in rects:
                # Rects are in visible (rotated) coordinates; redaction needs
                # unrotated ones (identity matrix for pages with rotation 0).
                # FIX / CAUTION: this has NOT been empirically verified against
                # real pages with /Rotate 90, 180 or 270 in the current PyMuPDF
                # version. If redaction appears to clip the wrong part of a
                # rotated page, this is the first place to check - test on an
                # actual rotated page before trusting this in production.
                page.add_redact_annot(rect * page.derotation_matrix)
            page.apply_redactions(
                images=image_mode,
                # FIX / CAUTION: vector graphics (e.g. a horizontal rule drawn
                # under a header, or a vector-drawn logo) are NEVER removed,
                # even in "fixed" mode. This is usually harmless for text
                # extraction (vectors don't produce text), but if Marker
                # rasterizes the page before OCR, leftover vector artifacts in
                # the header/footer zone could theoretically be picked up as
                # OCR noise. Low risk, but not a complete visual clean-up.
                graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
            )
            pages_redacted += 1

        logger.info(
            f"Header/footer removal ({HEADER_FOOTER_MODE}): "
            f"{pages_redacted}/{len(pdf_doc)} pages modified."
        )

    @staticmethod
    def _fixed_margin_rects(pdf_doc: "pymupdf.Document") -> Dict[int, List["pymupdf.Rect"]]:
        """'fixed' mode: top and bottom strips of a constant height on every page."""
        result: Dict[int, List["pymupdf.Rect"]] = {}
        for i, page in enumerate(pdf_doc):
            r = page.rect
            if r.height <= FIXED_TOP_MARGIN_PT + FIXED_BOTTOM_MARGIN_PT + FIXED_MIN_CONTENT_HEIGHT_PT:
                continue  # page too short for such margins
            result[i] = [
                pymupdf.Rect(r.x0, r.y0, r.x1, r.y0 + FIXED_TOP_MARGIN_PT),
                pymupdf.Rect(r.x0, r.y1 - FIXED_BOTTOM_MARGIN_PT, r.x1, r.y1),
            ]
        return result

    @staticmethod
    def _normalize_block(text: str) -> str:
        """Digits -> '#', lowercase, collapsed whitespace ('Strona 3 z 10' == 'Strona 7 z 10')."""
        text = re.sub(r"\d+", "#", (text or "").lower())
        return re.sub(r"\s+", " ", text).strip()

    def _find_repeated_blocks(
        self, pdf_doc: "pymupdf.Document"
    ) -> Dict[int, List["pymupdf.Rect"]]:
        """
        'auto' mode: finds text blocks in the header / footer zone whose
        (normalized) content repeats across many pages.

        KNOWN LIMITATION (see comment near AUTO_MIN_REPEAT_RATIO above):
        repetition is computed GLOBALLY across the whole stitched file. For a
        file containing many distinct contract templates, a template-specific
        header appearing only once or twice will not be removed, while the
        single most common template's header will be. Fixing this properly
        would require computing repetition per section_index, which in turn
        requires page classification to run BEFORE redaction - the opposite
        of the current order - and is left as a future improvement.
        """
        per_page: List[List[tuple]] = []
        counts: Counter = Counter()
        text_pages = 0

        for page in pdf_doc:
            r = page.rect
            header_limit = r.y0 + r.height * AUTO_HEADER_ZONE_RATIO
            footer_limit = r.y1 - r.height * AUTO_FOOTER_ZONE_RATIO

            entries = []
            page_has_text = False

            for x0, y0, x1, y1, txt, _block_no, block_type in page.get_text("blocks"):
                if block_type != 0:  # 0 = text block, 1 = image block
                    continue
                signature = self._normalize_block(txt)
                if not signature:
                    continue
                page_has_text = True

                if y1 <= header_limit:
                    zone = "top"
                elif y0 >= footer_limit:
                    zone = "bottom"
                else:
                    continue

                if len(signature) > AUTO_MAX_BLOCK_CHARS:
                    continue
                entries.append((zone, signature, pymupdf.Rect(x0, y0, x1, y1)))

            if page_has_text:
                text_pages += 1
            counts.update({(zone, sig) for zone, sig, _ in entries})  # once per page
            per_page.append(entries)

        threshold = max(AUTO_MIN_REPEAT_PAGES, math.ceil(AUTO_MIN_REPEAT_RATIO * text_pages))
        repeated = {key for key, count in counts.items() if count >= threshold}

        logger.debug(
            f"Repeated header/footer patterns: {len(repeated)} "
            f"(threshold={threshold} pages, text pages={text_pages})"
        )

        return {
            i: [rect for zone, sig, rect in entries if (zone, sig) in repeated]
            for i, entries in enumerate(per_page)
        }

    # ══════════════════════════════════════════════════════════════
    # HELPER METHODS
    # ══════════════════════════════════════════════════════════════

    @classmethod
    def _get_shared_models(cls):
        """Loads Marker models once per process (thread-safe)."""
        with cls._shared_models_lock:
            if cls._shared_models is None:
                logger.info("Loading Marker (Surya) models...")
                cls._shared_models = create_model_dict()
            return cls._shared_models

    @staticmethod
    def _detect_device() -> str:
        """Informational only - the actual device is chosen by Marker."""
        if torch.cuda.is_available():
            return "cuda"
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            return "mps"
        return "cpu"

    @staticmethod
    def _get_source_name(file_source: Union[str, io.BytesIO, bytes]) -> str:
        if isinstance(file_source, str):
            return os.path.basename(file_source)
        return "stream/bytes"

    @staticmethod
    def _get_bytes(file_source: Union[str, io.BytesIO, bytes]) -> bytes:
        if isinstance(file_source, str):
            with open(file_source, "rb") as f:
                return f.read()
        elif isinstance(file_source, bytes):
            return file_source
        elif isinstance(file_source, io.BytesIO):
            file_source.seek(0)
            return file_source.read()
        raise ValueError(f"Unsupported type: {type(file_source)}")

    @staticmethod
    def _cleanup_gpu():
        """Frees the VRAM cache after a document has been processed."""
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            torch.mps.empty_cache()