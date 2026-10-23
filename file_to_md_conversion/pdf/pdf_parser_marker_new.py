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
from typing import Dict, List, Optional, Tuple, Union

import pymupdf  # PyMuPDF
from PIL import Image
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

# --- Placeholder pages where Marker detected no picture ---
# A scanned fragment that Marker treats as a scan (not a Picture/Figure)
# leaves no image behind, and when its OCR comes back as noise the page
# would become a bare placeholder with nothing saved. For such pages the
# page is rendered with PyMuPDF and cropped to its ink region: the second
# OCR pass is run on the crop (the text fills the frame, so it reads much
# better) and the crop is saved to the images folder, so the drawing/plan
# is not lost.
OCR_PLACEHOLDER_PAGES = True          # second OCR pass on the ink crop
SAVE_PLACEHOLDER_PAGE_IMAGES = True   # save the ink crop as a PNG
PLACEHOLDER_PAGE_DPI = 150            # render resolution of the page


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
    1. Classify every page: text | scan | drawing | blank.
    2. Convert the whole file with Marker (page numbers match the original file).
    3. Build one Document per page:
       - text    -> Marker output (fallback: PyMuPDF text layer),
       - scan    -> Marker OCR output, noise-filtered,
       - drawing -> placeholder (plan / image without text); as a last
                    resort the page is rendered and cropped to ink, the
                    second OCR pass is tried on the crop, and the crop is
                    saved to the images folder so the drawing is not lost,
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

    # Same, but captures the file name/path (group 1)
    _MD_IMAGE_REF_RE = re.compile(r"!\[[^\]]*\]\(([^)]*)\)")

    # A lettered sub-list item that Marker renumbered: an ordered-list marker
    # ("1.") directly followed by the original letter marker ("a." or "a)")
    # plus a space, e.g. "1. a. txt" or "1. a) txt". Group 1 = leading indent,
    # group 2 = the letter, group 3 = the original delimiter ("." or ")").
    _LIST_DOUBLE_MARKER_RE = re.compile(r"^(\s*)\d+\.\s+([a-z])([.)])(?=\s)", re.MULTILINE)

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

        # Converter configuration (paginate_output -> page separators in Markdown)
        config_dict = ConfigParser(
            {"languages": languages, "paginate_output": True}
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
                    marker_pages, pages_info, source_name, image_map,
                    pdf_doc=pdf_doc, pdf_bytes=pdf_bytes,
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

    def _images_folder(self, source_name: str, pdf_bytes: bytes) -> str:
        """Per-document images folder <images_dir>/<stem>_<hash8>, created."""
        stem = re.sub(r"[^\w.-]+", "_", os.path.splitext(source_name)[0]).strip("._") or "document"
        folder = f"{stem}_{hashlib.sha1(pdf_bytes).hexdigest()[:8]}"
        target_dir = os.path.join(self.images_dir, folder)
        os.makedirs(target_dir, exist_ok=True)
        return target_dir

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

        target_dir = self._images_folder(source_name, pdf_bytes)
        folder = os.path.basename(target_dir)

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
                # OCR produced something but it looked like noise - keep the
                # raw output in the log so a failing page can be diagnosed
                logger.info(
                    f"Picture OCR rejected as noise (letters={letters}, "
                    f"compact={len(compact)}): {text[:150]!r}"
                )
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

    def _recover_placeholder_page(
        self,
        pdf_doc: Optional["pymupdf.Document"],
        info: PageInfo,
        source_name: str,
        pdf_bytes: Optional[bytes],
    ) -> Tuple[str, Optional[str]]:
        """
        Last resort for a page that is about to become a non-text placeholder
        but on which Marker detected no picture: a scanned fragment (e.g. a
        quarter page, slightly skewed) that Marker treated as a scan and whose
        OCR came back as noise. Renders the page with PyMuPDF and crops it to
        ink. Returns (ocr_text, saved_image_path): the second OCR pass is
        tried on the crop (the text fills the frame, so it reads much better)
        and the crop is saved to the images folder, so the drawing/plan is not
        lost.
        """
        if pdf_doc is None or pdf_bytes is None:
            return "", None
        try:
            mat = pymupdf.Matrix(PLACEHOLDER_PAGE_DPI / 72, PLACEHOLDER_PAGE_DPI / 72)
            pix = pdf_doc[info.number - 1].get_pixmap(matrix=mat, alpha=False)
            image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            render_size = image.size
            image = self._crop_to_ink(image)
        except Exception as e:
            logger.warning(f"[p{info.number}] page render failed ({source_name}): {e}")
            return "", None

        ocr_text = self._ocr_picture(image) if OCR_PLACEHOLDER_PAGES else ""
        if ocr_text:
            logger.info(
                f"[p{info.number}] recovered {len(ocr_text)} chars via cropped page OCR ({source_name})"
            )
        else:
            # The sizes show which step failed: render == crop means the ink
            # touches the frame (nothing to crop, the fragment still floats in
            # white space); a small crop with no text means the VLM could not
            # read it (check the saved page_NNN.png).
            logger.warning(
                f"[p{info.number}] cropped page OCR returned no text "
                f"(render={render_size[0]}x{render_size[1]} -> "
                f"crop={image.size[0]}x{image.size[1]}) ({source_name})"
            )
        rel_path = self._save_rendered_image(
            image, source_name, pdf_bytes, f"page_{info.number:03d}.png"
        )
        return ocr_text, rel_path

    def _save_rendered_image(
        self, image, source_name: str, pdf_bytes: bytes, file_name: str
    ) -> Optional[str]:
        """
        Saves a rendered (ink-cropped) page to the per-document images folder.
        Returns the relative path with forward slashes, or None.
        """
        if not SAVE_PLACEHOLDER_PAGE_IMAGES:
            return None
        try:
            target_dir = self._images_folder(source_name, pdf_bytes)
            image.save(os.path.join(target_dir, file_name))
            return (
                f"{self.images_dir}/{os.path.basename(target_dir)}/{file_name}"
            ).replace(os.sep, "/")
        except Exception as e:
            logger.warning(f"Could not save rendered page '{file_name}' ({source_name}): {e}")
            return None

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
        sub-list items ("1. a. txt" -> "a. txt", "1. a) txt" -> "a) txt"), so
        the document's original a/b/c lettering is what remains.
        """
        return self._LIST_DOUBLE_MARKER_RE.sub(r"\1\2\3", text)

    def _build_documents(
        self,
        marker_pages: Dict[int, str],
        pages_info: List[PageInfo],
        source_name: str,
        image_map: Optional[Dict[str, str]] = None,
        pdf_doc: Optional["pymupdf.Document"] = None,
        pdf_bytes: Optional[bytes] = None,
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
            raw_marker_text = text  # still contains the "![](...)" references
            page_type = info.kind
            method = "marker"
            # Images Marker detected on this page (computed early: the
            # placeholder recovery below may add its saved page render)
            page_image_paths = self._image_paths(raw_marker_text, image_map)

            if info.kind == "text":
                visible = self._MD_IMAGE_RE.sub("", text).strip()
                # Fallback: text layer from PyMuPDF when Marker returned nothing
                # or lost a large part of the text (e.g. a block classified as
                # header/footer or as a picture)
                if len(visible) < 0.5 * len(info.plain_text):
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
            if not text or (info.kind != "text" and self._is_noise(text)):
                logger.warning(
                    f"[p{info.number}] placeholder: kind={info.kind} "
                    f"plain={len(info.plain_text)} discarded={text[:200]!r}"
                )
                # Marker treated the page as a scan, its OCR came back as
                # noise, and no picture block was detected - the drawing/plan
                # would be lost entirely. Render the page and crop it to ink:
                # try the second OCR pass on the crop and save the crop.
                fallback_text, rel_path = self._recover_placeholder_page(
                    pdf_doc, info, source_name, pdf_bytes
                )
                if rel_path:
                    page_image_paths.append(rel_path)
                if fallback_text:
                    text = f"{OCR_TEXT_LABEL}\n{fallback_text}"
                    method = "marker-page-ocr"
                else:
                    non_text_pages.append(info.number)
                    if not INCLUDE_NON_TEXT_PAGES:
                        continue
                    text = NON_TEXT_PLACEHOLDER
                    method = "placeholder"

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
        if failed_pages:
            logger.warning(f"No text from pages {failed_pages} ({source_name})")

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