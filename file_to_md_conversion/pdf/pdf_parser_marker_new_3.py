import os
import platform

# Set backend PyTorch for Apple Silicon before import torch/marker
if platform.system() == "Darwin" and platform.machine() == "arm64":
    os.environ.setdefault("TORCH_DEVICE", "mps")
    os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

import hashlib
import io
import logging
import re
import tempfile
import threading
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

import pymupdf  # PyMuPDF
import torch
from langchain_core.documents import Document
from marker.config.parser import ConfigParser
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict

from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# ======================================================================
# SETTINGS
# ======================================================================

# --- OCR approach: every page is a (possibly skewed) scan ---
# Marker is forced to OCR the whole file instead of trusting the embedded
# text layer: pdftext extraction is skipped entirely, and in balanced mode
# each page is rebuilt from a single full-page OCR call on the rendered
# image - so a skewed scan is read from the picture, not from a misaligned
# text layer. The PyMuPDF text layer stays only as a last-resort fallback
# for pages whose OCR produced nothing usable.
FORCE_OCR = True

# --- Page classification ---
MIN_TEXT_CHARS = 20               # fewer characters in the text layer = "no real text"
BLANK_INK_RATIO = 0.001           # share of "ink" pixels below which a page is blank
INK_DELTA = 50                    # pixel is "ink" if darker than background by this much
CLASSIFY_MAX_PX = 800             # longer side of the low-res render used for classification

# --- OCR noise filter (OCR on plans/photos returns garbage) ---
MIN_OCR_LETTER_RATIO = 0.4        # letters / non-space characters

# --- Pages without extractable text (plans, drawings, photos, stamps) ---
INCLUDE_NON_TEXT_PAGES = True     # keep them as a short placeholder Document
NON_TEXT_PLACEHOLDER = "[Strona bez tekstu: rysunek, plan lub obraz]"

# --- Images / figures detected by Marker ---
# Pictures and figures that Marker extracts are saved to
#   <IMAGES_DIR>/<document name>_<hash>/<marker file name>
# and the reference in the Markdown is replaced with a marker built from
# IMAGE_MARKER_TEMPLATE ({path} = relative path, {name} = file name).
# Markdown-image variant: IMAGE_MARKER_TEMPLATE = "![OBRAZ {name}]({path})"
SAVE_IMAGES = True
IMAGES_DIR = "img"
IMAGE_MARKER_TEMPLATE = "[OBRAZ: {path}]"
# Pictures with a shorter side below this are treated as noise (pen initials,
# small stamps, codes) and are neither saved nor referenced in the Markdown.
# Independent of OCR_PICTURE_MIN_PX, which only gates the second OCR pass.
IMAGE_MIN_PX = 150

# --- Second OCR pass on pictures ---
# Marker does not run OCR inside blocks it labels as Picture/Figure. A scanned
# fragment pasted into a page (e.g. a quarter of a page, slightly skewed) is
# often labelled that way. With OCR_PICTURES on, every picture Marker detected
# is wrapped in a one-page PDF and converted again, so Marker treats it as a
# scan. Each picture is first cropped to its ink region, then the OCR result is
# kept only if it clears the picture-specific noise thresholds below.
OCR_PICTURES = True
OCR_PICTURE_MIN_PX = 150          # pictures with a shorter side are skipped
OCR_PICTURES_MAX_PER_DOC = 50     # safety limit of extra conversions per file
OCR_TEXT_LABEL = "[Tekst rozpoznany z obrazu]"
# The second pass often reads slightly-skewed scans imperfectly, so it uses
# its own, more forgiving noise thresholds than the main OCR filter above.
PIC_OCR_MIN_LETTERS = 6
PIC_OCR_LETTER_RATIO = 0.3


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
    1. Classify every page: text | scan | drawing | blank (blank pages are
       skipped; they mark the boundary between stitched documents -
       metadata["section_index"]).
    2. Convert the whole file with Marker in force-OCR mode (FORCE_OCR):
       every page is treated as a (possibly skewed) scan and re-read from the
       rendered image - the embedded text layer is not trusted.
    3. Build one Document per page:
       - Marker OCR text is the source of truth for every page,
       - the PyMuPDF text layer is used only when OCR produced nothing usable
         (empty / noise),
       - a page with no extractable text at all gets a placeholder.
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

    # Same, but captures the file name/path (group 1)
    _MD_IMAGE_REF_RE = re.compile(r"!\[[^\]]*\]\(([^)]*)\)")

    # A lettered sub-list item that Marker renumbered: an ordered-list marker
    # ("1." / "1)") directly followed by the original letter marker ("a." /
    # "A." / "a)") plus a space or end of line, e.g. "1. a. txt" -> "a. txt".
    # Matches at any position - full-page VLM OCR often collapses the whole
    # list into one line - but the lookbehind keeps dotted chapter.item
    # numbering like "2.1." intact. Group 1 = the letter marker to keep.
    _LIST_DOUBLE_MARKER_RE = re.compile(
        r"(?<![\d.])\d+[.)]\s+([a-zA-Z][.)])(?=\s|$)", re.MULTILINE
    )

    def __init__(self, languages: str = "pl,en", images_dir: str = IMAGES_DIR):
        """
        Args:
            languages: Comma-separated language codes (e.g. "pl,en").
                       May be ignored in newer Marker versions.
            images_dir: Folder for pictures/figures extracted by Marker
                        (used only if SAVE_IMAGES is True).
        """
        # ── GPU / Marker models ──────────────────────────────────
        # Note: the device is chosen by Marker itself (TORCH_DEVICE environment
        # variable, set BEFORE importing Marker). The value below is informational only.
        self._device = self._detect_device()
        self.models = self._get_shared_models()

        # Converter configuration:
        #  - paginate_output -> page separators in the Markdown
        #  - force_ocr       -> OCR every page from the rendered image, ignoring
        #                       the embedded text layer (see FORCE_OCR)
        config_dict = ConfigParser(
            {
                "languages": languages,
                "paginate_output": True,
                "force_ocr": FORCE_OCR,
            }
        ).generate_config_dict()
        self.converter = PdfConverter(
            config=config_dict,
            artifact_dict=self.models,
        )

        self.languages = languages
        self.images_dir = images_dir

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
            # ── 1. Page analysis (PyMuPDF) ───────────────────────
            pdf_bytes = self._get_bytes(file_source)
            pdf_doc = pymupdf.Document(stream=pdf_bytes, filetype="pdf")
            pages_info = self._analyze_pages(pdf_doc)

            if all(p.kind == "blank" for p in pages_info):
                logger.warning(f"All pages are blank in '{source_name}'")
                return []

            # ── 2. Write to a temporary file ─────────────────────
            # PdfConverter takes a file path, so a temporary file is required.
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
                temp_pdf.write(pdf_bytes)
                temp_pdf_path = temp_pdf.name

            # ── 3. Marker conversion (GPU), serialized ───────────
            logger.info(f"Starting Marker (Surya) conversion: {source_name}")
            with self._convert_lock:
                rendered = self.converter(temp_pdf_path)
            md_text = (rendered.markdown or "").strip()
            # Second OCR pass on pictures (e.g. a scanned fragment pasted into a page)
            md_text = self._inject_picture_ocr(md_text, getattr(rendered, "images", None))
            # Pictures/figures detected by Marker -> files in images_dir.
            # The Markdown still holds the raw "![](...)" references at this
            # point; they are replaced later, when the documents are built
            # (the page logic needs to see them to detect image-only pages).
            image_map = self._save_images(
                getattr(rendered, "images", None), source_name, pdf_bytes
            )
            logger.info(f"Conversion finished: {source_name}")

            # ── 4. Building documents ────────────────────────────
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
                    [
                        Document(
                            page_content=self._apply_images(md_text, image_map),
                            metadata=self._base_metadata(source_name),
                        )
                    ]
                    if md_text
                    else []
                )
            else:
                if marker_pages and max(marker_pages) > len(pages_info):
                    logger.warning(
                        f"Marker returned page {max(marker_pages)} but the file has "
                        f"{len(pages_info)} pages ({source_name}) - page numbers may be misaligned."
                    )
                documents = self._build_documents(
                    marker_pages, pages_info, source_name, image_map
                )

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
    # IMAGES (pictures / figures detected by Marker)
    # ══════════════════════════════════════════════════════════════

    @staticmethod
    def _image_marker(path: str) -> str:
        """Marker text that replaces an image reference in the Markdown."""
        return IMAGE_MARKER_TEMPLATE.format(path=path, name=os.path.basename(path))

    def _save_images(
        self,
        images: Optional[Dict[str, object]],
        source_name: str,
        pdf_bytes: bytes,
    ) -> Dict[str, str]:
        """
        Saves Marker's images (PIL) to <images_dir>/<document>_<hash>/.
        Returns {marker file name: relative path with forward slashes}.
        """
        if not SAVE_IMAGES or not images:
            return {}

        stem = re.sub(r"[^\w.-]+", "_", os.path.splitext(source_name)[0]).strip("._") or "document"
        folder = f"{stem}_{hashlib.sha1(pdf_bytes).hexdigest()[:8]}"
        target_dir = os.path.join(self.images_dir, folder)
        os.makedirs(target_dir, exist_ok=True)

        image_map: Dict[str, str] = {}
        skipped = 0
        for name, image in images.items():
            width, height = image.size
            if min(width, height) < IMAGE_MIN_PX:
                # noise: pen initials, small stamps / codes
                skipped += 1
                continue
            safe_name = os.path.basename(name)
            file_path = os.path.join(target_dir, safe_name)
            try:
                # JPEG cannot store alpha / palette modes
                if safe_name.lower().endswith((".jpg", ".jpeg")) and image.mode != "RGB":
                    image = image.convert("RGB")
                image.save(file_path)
            except Exception as e:
                logger.warning(f"Could not save image '{name}' ({source_name}): {e}")
                continue
            image_map[name] = f"{self.images_dir}/{folder}/{safe_name}".replace(os.sep, "/")

        logger.info(
            f"Saved {len(image_map)}/{len(images)} images to '{target_dir}' "
            f"({source_name}); {skipped} below IMAGE_MIN_PX skipped"
        )
        return image_map

    def _apply_images(self, text: str, image_map: Optional[Dict[str, str]]) -> str:
        """Replaces Marker's '![](file)' references with image markers."""
        if not text or not image_map:
            return text

        def _replace(match: "re.Match") -> str:
            path = image_map.get(match.group(1))
            # References to images we did not save (too small / noise) are
            # dropped from the Markdown instead of left as a broken link.
            return self._image_marker(path) if path else ""

        return self._MD_IMAGE_REF_RE.sub(_replace, text)

    def _image_paths(self, text: str, image_map: Optional[Dict[str, str]]) -> List[str]:
        """Saved image paths referenced in the given Marker text."""
        if not text or not image_map:
            return []
        return [image_map[n] for n in self._MD_IMAGE_REF_RE.findall(text) if n in image_map]

    @staticmethod
    def _crop_to_ink(image):
        """
        Crops a picture to the region that actually contains ink. A scanned
        fragment pasted onto a mostly-white page otherwise occupies only a
        fraction of the frame, and the second OCR pass reads it far better
        when the text fills the image. Returns the input unchanged when there
        is no clear ink region.
        """
        width, height = image.size
        try:
            gray = image.convert("L")
            hist = gray.histogram()
            background = max(range(256), key=hist.__getitem__)
            # ink mask: 255 where the pixel is darker than the dominant level
            mask = gray.point(lambda v: 255 if v < background - INK_DELTA else 0)
            bbox = mask.getbbox()
            if bbox is None:
                return image
            pad = max(8, int(0.02 * max(width, height)))  # room so glyphs are not clipped
            left, top = max(0, bbox[0] - pad), max(0, bbox[1] - pad)
            right, bottom = min(width, bbox[2] + pad), min(height, bbox[3] + pad)
            if left == 0 and top == 0 and right == width and bottom == height:
                return image  # ink fills the frame; nothing to crop
            return image.crop((left, top, right, bottom))
        except Exception:
            return image  # never let cropping break the OCR pass

    def _ocr_picture(self, image) -> str:
        """
        Second Marker pass on ONE picture. The picture is wrapped in a one-page
        PDF without a text layer, so Marker treats it as a scan and runs OCR
        instead of labelling it a figure again. Returns "" for noise.
        """
        image = self._crop_to_ink(image)  # small fragment on white -> text fills frame
        width, height = image.size
        if min(width, height) < OCR_PICTURE_MIN_PX:
            return ""

        tmp_path = None
        try:
            buf = io.BytesIO()
            image.convert("RGB").save(buf, format="PNG")

            page_w = 595.0  # A4 width in points; height keeps the aspect ratio
            page_h = page_w * height / width
            doc = pymupdf.open()
            try:
                page = doc.new_page(width=page_w, height=page_h)
                page.insert_image(page.rect, stream=buf.getvalue())
                pdf_bytes = doc.tobytes()
            finally:
                doc.close()

            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp.write(pdf_bytes)
                tmp_path = tmp.name

            with self._convert_lock:
                rendered = self.converter(tmp_path)

            text = rendered.markdown or ""
            text = self._PAGE_SEPARATOR_RE.sub("\n", text)
            text = self._MD_IMAGE_RE.sub("", text).strip()

            compact = re.sub(r"\s", "", text)
            letters = sum(ch.isalpha() for ch in compact)
            if letters < PIC_OCR_MIN_LETTERS or letters / max(len(compact), 1) < PIC_OCR_LETTER_RATIO:
                return ""
            return text
        except Exception as e:
            logger.warning(f"Picture OCR failed: {e}")
            return ""
        finally:
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)

    def _inject_picture_ocr(self, md_text: str, images: Optional[Dict[str, object]]) -> str:
        """
        Puts the text recognized in pictures right after their '![](file)'
        references. Done on the raw Marker Markdown, BEFORE the page logic, so a
        page whose only content is such a picture is no longer treated as empty.
        """
        if not OCR_PICTURES or not images or not md_text:
            return md_text

        ocr_by_name: Dict[str, str] = {}
        candidates = list(images.items())[:OCR_PICTURES_MAX_PER_DOC]
        for name, image in candidates:
            text = self._ocr_picture(image)
            if text:
                ocr_by_name[name] = text

        logger.info(f"Picture OCR: text recognized in {len(ocr_by_name)}/{len(candidates)} pictures")
        if not ocr_by_name:
            return md_text

        def _replace(match: "re.Match") -> str:
            text = ocr_by_name.get(match.group(1))
            if not text:
                return match.group(0)
            return f"{match.group(0)}\n\n{OCR_TEXT_LABEL}\n{text}\n"

        return self._MD_IMAGE_REF_RE.sub(_replace, md_text)

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
        if letters < 3:
            return True
        # Short fragments are judged only by the number of letters; the
        # letter/character ratio is applied only to longer text
        if len(compact) < 60:
            return False
        return letters / len(compact) < MIN_OCR_LETTER_RATIO

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

    def _collapse_list_numbers(self, text: str) -> str:
        """
        Removes the redundant outer numbering Marker adds in front of lettered
        sub-list items ("1. a. txt" -> "a. txt" - also when the whole list sits
        on one line, the letter is uppercase, or the outer marker is "1)"), so
        the document's original a/b/c lettering is what remains.
        """
        return self._LIST_DOUBLE_MARKER_RE.sub(r"\1", text)

    def _build_documents(
        self,
        marker_pages: Dict[int, str],
        pages_info: List[PageInfo],
        source_name: str,
        image_map: Optional[Dict[str, str]] = None,
    ) -> List[Document]:
        """Combines Marker output with the page analysis into one Document per page."""
        documents: List[Document] = []
        blank_pages: List[int] = []
        non_text_pages: List[int] = []

        for info in pages_info:
            if info.kind == "blank":
                blank_pages.append(info.number)
                continue

            text = marker_pages.get(info.number, "")
            raw_marker_text = text  # still contains the "![](...)" references
            page_type = info.kind
            method = "marker"

            # OCR-first (FORCE_OCR): Marker re-read every page from the
            # rendered image, so its output is the source of truth - also for
            # pages that carry an embedded text layer (on a skewed scan that
            # layer is exactly what cannot be trusted). The PyMuPDF layer is
            # only a last resort, for pages whose OCR produced nothing usable.
            if self._is_noise(self._MD_IMAGE_RE.sub("", text).strip()):
                text = info.plain_text
                method = "pymupdf-text"

            # A page still without usable text (empty / noise from both
            # sources) becomes a placeholder, so e.g. a plan page is not
            # silently dropped.
            if not text or self._is_noise(text):
                logger.warning(
                    f"[p{info.number}] placeholder: kind={info.kind} "
                    f"plain={len(info.plain_text)} discarded={text[:200]!r}"
                )
                non_text_pages.append(info.number)
                if not INCLUDE_NON_TEXT_PAGES:
                    continue
                text = NON_TEXT_PLACEHOLDER
                method = "placeholder"

            # Images Marker detected on this page
            page_image_paths = self._image_paths(raw_marker_text, image_map)
            if method == "marker":
                text = self._apply_images(text, image_map)
            elif page_image_paths:
                # Text came from PyMuPDF or is the placeholder: the Marker text
                # with the references was not used, so append the markers
                text = text + "\n\n" + "\n".join(self._image_marker(p) for p in page_image_paths)

            metadata = self._base_metadata(source_name)
            metadata.update(
                {
                    "page_number": info.number,
                    "page_type": page_type,
                    "section_index": info.section_index,
                    "extraction_method": method,
                }
            )
            if page_image_paths:
                metadata["image_count"] = len(page_image_paths)
                metadata["image_paths"] = ";".join(page_image_paths)
            text = self._collapse_list_numbers(text)
            documents.append(Document(page_content=text, metadata=metadata))

        if blank_pages:
            logger.info(f"Skipped blank pages {blank_pages} ({source_name})")
        if non_text_pages:
            logger.info(f"Pages without extractable text (plans/images) {non_text_pages} ({source_name})")

        return documents

    @staticmethod
    def _base_metadata(source_name: str) -> Dict[str, object]:
        return {
            "source": source_name,
            "parser": "marker",
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