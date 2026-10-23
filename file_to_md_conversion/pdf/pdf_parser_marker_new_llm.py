import base64
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
import pymupdf
from dotenv import load_dotenv
load_dotenv()
from PIL import Image
import torch
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from marker.config.parser import ConfigParser
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)

# --- Vision model (VLM) for the second pass (from .env) ---
# Used for pictures inside pages and for whole pages without a text layer;
# OpenAI-compatible endpoint (e.g. LM Studio); see the SETTINGS block below.
# load_dotenv() runs AFTER the torch/marker imports on purpose: they read
# environment variables (CUDA_VISIBLE_DEVICES, OMP_NUM_THREADS, ...) at
# import time, so .env must not leak into them.

LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")

# ======================================================================
# SETTINGS
# ======================================================================

# --- Page classification ---
# Two categories only: the page has a usable text layer (Marker path) or not.
# Every "notext" page is rendered to a PNG, cropped to its ink region and sent
# to the vision model, which decides what it is (see the VLM sections below).
MIN_TEXT_CHARS = 20               # fewer characters in the text layer = "no real text"
INK_DELTA = 50                    # pixel is "ink" if darker than background by this much
                                  # (used for the crop-to-ink of rendered pages)

# --- Pages the VLM decides are a drawing/image (plans, drawings, photos) ---
INCLUDE_NON_TEXT_PAGES = True     # keep them in the output as an [IMAGE: ...] marker
NON_TEXT_PLACEHOLDER = "[No text on page: drawing, plan or image]"

# --- Images / figures detected by Marker ---
# Pictures and figures that Marker extracts are saved to
#   <IMAGES_DIR>/<document name>_<hash>/<marker file name>
# and the reference in the Markdown is replaced with a marker built from
# IMAGE_MARKER_TEMPLATE ({path} = relative path, {name} = file name).
# Markdown-image variant: IMAGE_MARKER_TEMPLATE = "![IMAGE {name}]({path})"
SAVE_IMAGES = True
IMAGES_DIR = "img"
IMAGE_MARKER_TEMPLATE = "[IMAGE: {path}]"
# Pictures with a shorter side below this are treated as noise (pen initials,
# small stamps, codes) and are neither saved nor referenced in the Markdown.
# Independent of OCR_PICTURE_MIN_PX, which only gates the second OCR pass.
IMAGE_MIN_PX = 150

# --- Second pass on pictures: VLM (vision-language model) ---
# Marker does not run OCR inside blocks it labels as Picture/Figure. A scanned
# fragment pasted into a page (e.g. a quarter of a page, slightly skewed) is
# often labelled that way. With OCR_PICTURES on, every picture Marker detected
# is cropped to its ink region and sent to the vision model (LLM_BASE_URL /
# LLM_API_KEY / LLM_MODEL from .env), which returns the recognized text as
# Markdown. The result is kept only if it clears the picture-specific noise
# thresholds below.
OCR_PICTURES = True
OCR_PICTURE_MIN_PX = 150          # pictures with a shorter side are skipped
OCR_PICTURES_MAX_PER_DOC = 50     # safety limit of extra VLM calls per file
VLM_MAX_TOKENS = 2000             # max length of the Markdown the model may return
VLM_MAX_PX = 2000                 # longest side (px) of the image sent to the VLM
OCR_TEXT_LABEL = "[Text recognized from the image]"
# The second pass often reads slightly-skewed scans imperfectly, so it uses
# its own, more forgiving noise thresholds than the main OCR filter above.
PIC_OCR_MIN_LETTERS = 6
PIC_OCR_LETTER_RATIO = 0.3

# --- VLM decision on whole pages without a text layer ---
# Every "notext" page is rendered, cropped to its ink region and sent to the
# VLM, which answers exactly EMPTY, exactly IMAGE, or the transcribed text as
# Markdown. The sentinels are parsed strictly (case-insensitive exact match
# after trimming) - any other answer is treated as the transcribed text.
VLM_PAGE_EMPTY = "EMPTY"          # answer: the page has no usable content
VLM_PAGE_IMAGE = "IMAGE"          # answer: drawing / plan / diagram / photo

# --- Page render for the VLM page decision ---
# Every page without a text layer is rendered with PyMuPDF at the resolution
# below and cropped to its ink region before the VLM call (the content fills
# the frame, so the model reads it much better). The crop is saved to the
# images folder for every non-EMPTY decision, so a drawing/plan is never lost
# from the output.
OCR_PLACEHOLDER_PAGES = True          # run the VLM pass on the ink crop
SAVE_PLACEHOLDER_PAGE_IMAGES = True   # save the ink crop as a PNG
PLACEHOLDER_PAGE_DPI = 150            # render resolution of the page
PLACEHOLDER_PAGE_MAX_PX = 3000        # longest side cap (px) of that render


@dataclass
class PageInfo:
    """Result of the page analysis (1-based page number)."""
    number: int
    kind: str            # 'text' | 'notext' (no usable text layer)
    section_index: int   # index of the stitched document (VLM-confirmed empty
                         # pages = boundaries; assigned after the VLM pass)
    plain_text: str      # text layer from PyMuPDF (fallback for Marker)


class PdfParser(BaseDocumentParser):
    """
    PDF parser based on Marker (Surya OCR + DL models) + PyMuPDF, for "stitched"
    contracts: many documents in one file (contracts, energy certificates,
    plans, Excel printouts), separated by blank pages.
    Requires GPU acceleration for acceptable performance.

    Steps:
    1. Classify every page: text (usable text layer) | notext.
    2. Convert the whole file with Marker (page numbers match the original file).
    3. Build one Document per page:
       - text   -> Marker output (fallback: PyMuPDF text layer),
       - notext -> the page is rendered to a PNG, cropped to its ink region
                   and sent to the vision model (VLM), which decides what it
                   is: EMPTY -> skipped (VLM-confirmed empty pages mark the
                   boundary between stitched documents,
                   metadata["section_index"]); IMAGE -> the saved page render
                   becomes the content as an [IMAGE: ...] marker; text ->
                   the page transcribed as Markdown.
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

    # A numbered item duplicated by Marker: the source already prints the
    # numbering and Marker adds its own ordered-list marker in front, so the
    # line starts with "1. 1." - the number, then the SAME number again after
    # an unknown run of spaces/tabs. Group 1 = leading indent, group 2 = the
    # number. The backreference keeps only true duplicates ("1. 2." is left
    # alone), the lookahead keeps section refs like "1. 1.1", and the trailing
    # [ \t]* is consumed so the replacement yields a single, clean space.
    _NUM_DOUBLE_MARKER_RE = re.compile(r"^(\s*)(\d+)\.[ \t]+\2\.(?=[ \t]|$)[ \t]*", re.MULTILINE)

    # A code fence some models wrap the whole answer in ("```markdown ... ```")
    _CODE_FENCE_RE = re.compile(r"^```[^\n]*\n(.*?)\n?```\s*$", re.DOTALL)

    # Page index embedded in Marker's image names (e.g. "_page_3_Picture_0.jpeg");
    # Marker counts pages from 0
    _IMAGE_PAGE_RE = re.compile(r"page[_-]?(\d+)", re.IGNORECASE)

    # Prompt for the vision model: the answer must be the transcribed text as
    # Markdown and nothing else ("EMPTY" is caught by the noise filter below).
    _VLM_PROMPT = (
        "You are an expert document OCR and layout assistant. Transcribe the "
        "text in the image exactly as it appears and output it as clean Markdown.\n"
        "Rules:\n"
        "- Keep the original language of the document - do not translate.\n"
        "- Preserve headings (#, ##, ...), lists and paragraph structure.\n"
        "- Convert tables to Markdown tables.\n"
        "- Do not add any conversational filler, explanations or comments.\n"
        "- Do not wrap the answer in code fences.\n"
        "- If the image contains no readable text, output exactly: EMPTY"
    )

    # Prompt for the VLM pass over a whole page without a text layer: the
    # model decides what the page is. Exactly EMPTY -> nothing usable on the
    # page (it is skipped and marks a section boundary); exactly IMAGE -> a
    # drawing/plan/diagram/photo (the saved page render becomes the content);
    # anything else -> the transcribed text as clean Markdown.
    _VLM_PAGE_PROMPT = (
        "You are an expert document analysis assistant. Look at this PDF page "
        "image and decide what it contains.\n"
        "- If the page is empty, or contains no usable document content "
        "(only blank space, borders or unreadable marks), output exactly: EMPTY\n"
        "- If the page is a drawing, floor plan, technical plan, diagram, map, "
        "chart or photo with no document text to transcribe, output exactly: IMAGE\n"
        "- Otherwise transcribe ALL the text exactly as it appears and output "
        "it as clean Markdown.\n"
        "Transcription rules:\n"
        "- Keep the original language of the document - do not translate.\n"
        "- Preserve headings (#, ##, ...), lists and paragraph structure.\n"
        "- Convert tables to Markdown tables.\n"
        "- Do not add any conversational filler, explanations or comments.\n"
        "- Do not wrap the answer in code fences."
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

        # Converter configuration (paginate_output -> page separators in Markdown)
        config_dict = ConfigParser(
            {"languages": languages, "paginate_output": True}
        ).generate_config_dict()
        self.converter = PdfConverter(
            config=config_dict,
            artifact_dict=self.models,
        )

        # ── VLM for the second pass ─────────────────────────────
        # OpenAI-compatible vision model (e.g. LM Studio) from .env; without
        # it the VLM pass is disabled: pictures are not OCR'd and non-text
        # pages become saved images/placeholders (logged at init).
        if LLM_BASE_URL and LLM_MODEL:
            self.vlm = ChatOpenAI(
                base_url=LLM_BASE_URL,
                api_key=LLM_API_KEY,
                model=LLM_MODEL,
                max_tokens=VLM_MAX_TOKENS,
                temperature=0.0,
                timeout=600,  # a local model on a large image can be slow
            )
            logger.info(f"VLM ready: {LLM_MODEL} @ {LLM_BASE_URL}")
        else:
            self.vlm = None
            logger.warning(
                "LLM_BASE_URL / LLM_MODEL missing in .env - "
                "the second pass (VLM: pictures and non-text pages) is disabled"
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
        Processes a PDF -> list of Documents (one per page; VLM-confirmed
        empty pages are skipped). Per-page problems degrade to placeholders;
        a conversion-level failure (unreadable PDF, Marker/model error) is
        re-raised.
        """
        source_name = self._get_source_name(file_source)
        temp_pdf_path = None
        pdf_doc = None

        try:
            # ── 1. Page analysis (PyMuPDF) ───────────────────────
            pdf_bytes = self._get_bytes(file_source)
            pdf_doc = pymupdf.Document(stream=pdf_bytes, filetype="pdf")
            pages_info = self._analyze_pages(pdf_doc)

            # A file whose pages all lack a text layer is a valid scanned
            # document - the VLM pass decides per page, so there is no early
            # exit here (only a truly page-less file ends up empty).
            if not pages_info:
                logger.warning(f"No pages in '{source_name}'")
                return []

            # ── 2. Write to a temporary file ─────────────────────
            # PdfConverter takes a file path, so a temporary file is required.
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
                temp_pdf.write(pdf_bytes)
                temp_pdf_path = temp_pdf.name

            # ── 3. Marker conversion (GPU), serialized ───────────
            logger.info(
                f"Starting Marker (Surya) conversion: {source_name} ({len(pages_info)} pages)"
            )
            with self._convert_lock:
                rendered = self.converter(temp_pdf_path)
            md_text = (rendered.markdown or "").strip()
            # Pictures/figures detected by Marker -> files in images_dir.
            # The Markdown still holds the raw "![](...)" references at this
            # point; they are replaced later, when the documents are built
            # (the page logic needs to see them to detect image-only pages).
            # Saving runs BEFORE the VLM pass so the second pass only sees
            # pictures that will actually be referenced in the output.
            # The hash is computed once and reused for the images folder.
            doc_hash = hashlib.sha1(pdf_bytes).hexdigest()[:8]
            image_map = self._save_images(
                getattr(rendered, "images", None), source_name, doc_hash
            )
            # Second pass on pictures via the VLM (e.g. a scanned fragment pasted into a page)
            md_text = self._inject_picture_ocr(
                md_text, getattr(rendered, "images", None), image_map,
                total_pages=len(pages_info),
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
                    pdf_doc=pdf_doc, doc_hash=doc_hash,
                )

            if not documents:
                logger.warning(f"No content extracted for '{source_name}'")
            else:
                logger.info(f"Extracted {len(documents)} pages from '{source_name}'")
            return documents

        except Exception as e:
            # Re-raise: a total failure (corrupt PDF, Marker OOM, model load
            # error) must not look like a genuinely empty document - callers
            # (e.g. the benchmark driver) catch per-file errors themselves.
            logger.error(f"Marker error ({source_name}): {e}", exc_info=True)
            raise

        finally:
            # Cleanup must never mask the result or the exception above: on
            # Windows a fresh temp file is often still locked by antivirus.
            if pdf_doc is not None:
                try:
                    pdf_doc.close()
                except Exception as e:
                    logger.warning(f"Could not close PDF document: {e}")
            if temp_pdf_path and os.path.exists(temp_pdf_path):
                try:
                    os.remove(temp_pdf_path)
                except OSError as e:
                    logger.warning(f"Could not remove temp file '{temp_pdf_path}': {e}")
            # Free VRAM
            try:
                self._cleanup_gpu()
            except Exception as e:
                logger.warning(f"GPU cleanup failed: {e}")

    def diagnostics(self) -> Dict[str, str]:
        """Diagnostic information for Marker."""
        with self._stats_lock:
            fallback_count = self._fallback_whole_document_count

        info = {
            "device": self._device,
            "languages": self.languages,
            "vlm_model": LLM_MODEL or "not set",
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

    @classmethod
    def _image_page_number(cls, name: str) -> Optional[int]:
        """1-based page number from a Marker image name, or None."""
        match = cls._IMAGE_PAGE_RE.search(name)
        return int(match.group(1)) + 1 if match else None

    def _images_folder(self, source_name: str, doc_hash: str) -> str:
        """Per-document images folder <images_dir>/<stem>_<hash8>, created.

        doc_hash is the 8-char prefix of SHA-1 over the whole PDF, computed
        ONCE in parse() (hashing a large file per call would be wasteful).
        """
        stem = re.sub(r"[^\w.-]+", "_", os.path.splitext(source_name)[0]).strip("._") or "document"
        folder = f"{stem}_{doc_hash}"
        target_dir = os.path.join(self.images_dir, folder)
        os.makedirs(target_dir, exist_ok=True)
        return target_dir

    def _save_images(
        self,
        images: Optional[Dict[str, object]],
        source_name: str,
        doc_hash: str,
    ) -> Dict[str, str]:
        """
        Saves Marker's images (PIL) to <images_dir>/<document>_<hash>/.
        Returns {marker file name: relative path with forward slashes}.
        """
        if not SAVE_IMAGES or not images:
            return {}

        target_dir = self._images_folder(source_name, doc_hash)
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

    def _vlm_invoke(self, image, prompt: str) -> str:
        """
        Sends ONE image to the vision model (LLM_* from .env) with the given
        prompt and returns the cleaned answer as a plain string: code fence
        removed, Markdown-image refs stripped. Returns "" when the VLM is not
        configured or the call fails. No noise filtering here - each caller
        applies its own thresholds (or sentinel parsing).
        """
        if self.vlm is None:
            return ""
        # A local VLM is slow on huge images - cap the longest side.
        width, height = image.size
        if max(width, height) > VLM_MAX_PX:
            scale = VLM_MAX_PX / max(width, height)
            image = image.resize(
                (max(1, int(width * scale)), max(1, int(height * scale))),
                Image.LANCZOS,
            )

        try:
            buf = io.BytesIO()
            image.convert("RGB").save(buf, format="PNG")
            img_base64 = base64.b64encode(buf.getvalue()).decode("ascii")

            message = HumanMessage(
                content=[
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{img_base64}"},
                    },
                ]
            )
            # Serialized like the Marker conversions: a local model server
            # (e.g. LM Studio) has a single inference slot.
            with self._convert_lock:
                response = self.vlm.invoke([message])

            text = self._extract_vlm_text(response.content)
            text = self._strip_code_fence(text)
            return self._MD_IMAGE_RE.sub("", text).strip()
        except Exception as e:
            logger.warning(f"VLM call failed: {e}")
            return ""

    def _vlm_picture(self, image) -> str:
        """
        Second pass on ONE picture via the vision model (LLM_* from .env): the
        ink-cropped picture is sent to the VLM, which returns the recognized
        text as Markdown. Returns "" for noise.
        """
        image = self._crop_to_ink(image)  # small fragment on white -> text fills frame
        width, height = image.size
        if min(width, height) < OCR_PICTURE_MIN_PX:
            return ""
        if self.vlm is None:
            return ""
        text = self._vlm_invoke(image, self._VLM_PROMPT)
        if not text:
            return ""
        compact = re.sub(r"\s", "", text)
        letters = sum(ch.isalpha() for ch in compact)
        if letters < PIC_OCR_MIN_LETTERS or letters / max(len(compact), 1) < PIC_OCR_LETTER_RATIO:
            # The model produced something but it looked like noise (the EMPTY
            # sentinel is caught here as well) - keep the raw output in the log
            # so a failing page can be diagnosed
            logger.info(
                f"Picture VLM rejected as noise (letters={letters}, "
                f"compact={len(compact)}): {text[:150]!r}"
            )
            return ""
        return text

    @staticmethod
    def _extract_vlm_text(content) -> str:
        """
        The VLM answer as one plain string. Newer langchain-openai versions may
        return a list of content parts (text, reasoning tokens, ...) instead.
        """
        if isinstance(content, list):
            content = "".join(
                part.get("text", "") if isinstance(part, dict) else str(part)
                for part in content
            )
        return (content or "").strip()

    @classmethod
    def _strip_code_fence(cls, text: str) -> str:
        """Removes the ```markdown ... ``` fence some models wrap the answer in."""
        match = cls._CODE_FENCE_RE.match(text)
        return match.group(1).strip() if match else text

    def _inject_picture_ocr(
        self,
        md_text: str,
        images: Optional[Dict[str, object]],
        image_map: Optional[Dict[str, str]] = None,
        total_pages: Optional[int] = None,
    ) -> str:
        """
        Puts the text recognized in pictures right after their '![](file)'
        references. Done on the raw Marker Markdown, BEFORE the page logic, so a
        page whose only content is such a picture is no longer treated as empty.
        Only pictures that are referenced in the Markdown AND actually saved
        (image_map) are sent to the VLM - anything else would waste the
        serialized inference slot and/or leave an orphaned text block.
        """
        if not OCR_PICTURES or self.vlm is None or not images or not md_text:
            return md_text

        image_map = image_map or {}
        referenced = set(self._MD_IMAGE_REF_RE.findall(md_text))
        ocr_by_name: Dict[str, str] = {}
        candidates = [
            (name, image)
            for name, image in images.items()
            if name in referenced and name in image_map
        ][:OCR_PICTURES_MAX_PER_DOC]
        for idx, (name, image) in enumerate(candidates):
            page_no = self._image_page_number(name)
            if page_no is not None and total_pages and not 1 <= page_no <= total_pages:
                page_no = None  # name no longer matches this file - don't mislabel
            prefix = f"[p{page_no}] " if page_no else ""
            logger.info(f"{prefix}Picture VLM {idx + 1}/{len(candidates)}: '{name}'")
            text = self._vlm_picture(image)
            if text:
                ocr_by_name[name] = text
                logger.info(f"{prefix}Picture VLM: +{len(text)} chars")

        logger.info(f"Picture VLM: text recognized in {len(ocr_by_name)}/{len(candidates)} pictures")
        if not ocr_by_name:
            return md_text

        def _replace(match: "re.Match") -> str:
            text = ocr_by_name.get(match.group(1))
            if not text:
                return match.group(0)
            return f"{match.group(0)}\n\n{OCR_TEXT_LABEL}\n{text}\n"

        return self._MD_IMAGE_REF_RE.sub(_replace, md_text)

    def _vlm_page(
        self,
        pdf_doc: Optional["pymupdf.Document"],
        info: PageInfo,
        source_name: str,
        doc_hash: Optional[str],
    ) -> Tuple[str, str, Optional[str]]:
        """
        VLM decision for ONE page without a text layer: the page is rendered
        with PyMuPDF, cropped to its ink region and sent to the vision model,
        which answers exactly "EMPTY" (nothing usable on the page), exactly
        "IMAGE" (a drawing/plan/diagram/photo) or the transcribed text as
        Markdown (strict parsing: anything else is treated as the text).
        The ink crop is saved to the images folder for every non-EMPTY
        decision (gated by SAVE_PLACEHOLDER_PAGE_IMAGES), so a drawing/plan is
        never lost from the output.
        Returns (decision, text, saved_image_path): decision is "empty",
        "image" or "text"; text is the Markdown for decision "text" (""
        otherwise); saved_image_path is the relative path of the saved crop
        (None for "empty" or when saving is off/failed).
        """
        if pdf_doc is None or not doc_hash:
            return "image", "", None
        try:
            # Cap the longest side: a large-format plan sheet at 150 DPI could
            # otherwise allocate a multi-GB pixmap.
            rect = pdf_doc[info.number - 1].rect
            scale = min(
                PLACEHOLDER_PAGE_DPI / 72,
                PLACEHOLDER_PAGE_MAX_PX / max(rect.width, rect.height),
            )
            pix = pdf_doc[info.number - 1].get_pixmap(
                matrix=pymupdf.Matrix(scale, scale), alpha=False
            )
            image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            render_size = image.size
            image = self._crop_to_ink(image)
        except Exception as e:
            logger.warning(f"[p{info.number}] page render failed ({source_name}): {e}")
            return "image", "", None

        raw = self._vlm_invoke(image, self._VLM_PAGE_PROMPT) if OCR_PLACEHOLDER_PAGES else ""
        # Strict sentinel parse: only an exact (case-insensitive, trimmed)
        # EMPTY / IMAGE answer counts as a decision - any longer answer is the
        # transcribed text.
        sentinel = raw.strip().upper()
        if sentinel == VLM_PAGE_EMPTY:
            logger.info(f"[p{info.number}] page VLM: EMPTY ({source_name})")
            return "empty", "", None
        if sentinel == VLM_PAGE_IMAGE:
            logger.info(f"[p{info.number}] page VLM: IMAGE ({source_name})")
            rel_path = self._save_rendered_image(
                image, source_name, doc_hash, f"page_{info.number:03d}.png"
            )
            return "image", "", rel_path
        if not raw:
            # VLM disabled, unavailable or the call failed: keep the page as
            # an image with the saved render, so nothing is lost. The sizes
            # show which step to check (render == crop means the ink touches
            # the frame; a small crop means a sparse page - see page_NNN.png).
            logger.warning(
                f"[p{info.number}] page VLM produced no decision "
                f"(render={render_size[0]}x{render_size[1]} -> "
                f"crop={image.size[0]}x{image.size[1]}) ({source_name})"
            )
            rel_path = self._save_rendered_image(
                image, source_name, doc_hash, f"page_{info.number:03d}.png"
            )
            return "image", "", rel_path
        logger.info(f"[p{info.number}] page VLM: text, {len(raw)} chars ({source_name})")
        rel_path = self._save_rendered_image(
            image, source_name, doc_hash, f"page_{info.number:03d}.png"
        )
        return "text", raw, rel_path

    def _save_rendered_image(
        self, image, source_name: str, doc_hash: str, file_name: str
    ) -> Optional[str]:
        """
        Saves a rendered (ink-cropped) page to the per-document images folder.
        Returns the relative path with forward slashes, or None.
        """
        if not SAVE_PLACEHOLDER_PAGE_IMAGES:
            return None
        try:
            target_dir = self._images_folder(source_name, doc_hash)
            image.save(os.path.join(target_dir, file_name))
            return (
                f"{self.images_dir}/{os.path.basename(target_dir)}/{file_name}"
            ).replace(os.sep, "/")
        except Exception as e:
            logger.warning(f"Could not save rendered page '{file_name}' ({source_name}): {e}")
            return None

    # ══════════════════════════════════════════════════════════════
    # PAGE ANALYSIS (classification)
    # ══════════════════════════════════════════════════════════════

    def _analyze_pages(self, pdf_doc: "pymupdf.Document") -> List[PageInfo]:
        """
        Classifies every page as 'text' (usable text layer) or 'notext'.
        section_index is assigned later, in _build_documents, once the VLM
        has confirmed which notext pages are truly empty (those mark the
        boundaries between the stitched documents).
        """
        result: List[PageInfo] = []
        for i, page in enumerate(pdf_doc):
            plain_text = page.get_text().strip()
            result.append(
                PageInfo(
                    number=i + 1,
                    kind=self._classify_page(plain_text),
                    section_index=0,
                    plain_text=plain_text,
                )
            )

        counts = Counter(p.kind for p in result)
        logger.info(f"Page classification: {dict(counts)}")
        return result

    @staticmethod
    def _classify_page(plain_text: str) -> str:
        """Returns 'text' when the page has a usable text layer, else 'notext'."""
        return "text" if len(plain_text) >= MIN_TEXT_CHARS else "notext"

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
        Removes the redundant outer numbering Marker adds in front of items
        that are already numbered in the source:
        - numbered items: "1. 1. txt" -> "1. txt" (the duplicated number is
          dropped, whatever the spaces/tabs between the two markers are),
        - lettered sub-list items: "1. a. txt" -> "a. txt", "1. a) txt" ->
          "a) txt", so the document's original a/b/c lettering remains.
        """
        # Number pass first: "1. 1. a. txt" -> "1. a. txt" -> "a. txt"
        text = self._NUM_DOUBLE_MARKER_RE.sub(r"\1\2. ", text)
        return self._LIST_DOUBLE_MARKER_RE.sub(r"\1\2\3", text)

    def _build_documents(
        self,
        marker_pages: Dict[int, str],
        pages_info: List[PageInfo],
        source_name: str,
        image_map: Optional[Dict[str, str]] = None,
        pdf_doc: Optional["pymupdf.Document"] = None,
        doc_hash: str = "",
    ) -> List[Document]:
        """
        Combines Marker output with the page analysis into one Document per
        page:
        - 'text' pages   -> Marker output (fallback: PyMuPDF text layer),
        - 'notext' pages -> decided by the VLM on the rendered page (see
          _vlm_page): empty (skipped, section boundary), image (the saved
          page render becomes the content) or text (VLM transcription).
        """
        built: List[Tuple[PageInfo, Document]] = []
        empty_pages: List[int] = []
        image_pages: List[int] = []
        failed_pages: List[int] = []
        total_pages = len(pages_info)
        # Lines repeated on 2+ pages (headers, footers, watermarks) inflate the
        # raw text layer and would wrongly trigger the PyMuPDF fallback below -
        # the fallback compares against the layer without such lines.
        line_counts = Counter()
        for p in pages_info:
            for line in p.plain_text.splitlines():
                line = line.strip()
                if line:
                    line_counts[line] += 1

        for info in pages_info:
            if info.kind == "text":
                text = marker_pages.get(info.number, "")
                raw_marker_text = text  # still contains the "![](...)" references
                page_type = "text"
                method = "marker"
                # Images Marker detected on this page
                page_image_paths = self._image_paths(raw_marker_text, image_map)

                visible = self._MD_IMAGE_RE.sub("", text).strip()
                # Plain layer WITHOUT lines repeated on 2+ pages (headers,
                # footers, watermarks), which would otherwise inflate it and
                # trigger the fallback for a correct, shorter Marker output.
                plain_effective = sum(
                    len(line) + 1
                    for line in info.plain_text.splitlines()
                    if line.strip() and line_counts[line.strip()] == 1
                )
                # Fallback: text layer from PyMuPDF when Marker returned nothing
                # or lost a large part of the text (e.g. a block classified as
                # header/footer or as a picture)
                if plain_effective and len(visible) < 0.5 * plain_effective:
                    text = info.plain_text
                    method = "pymupdf-text"
                if not text:
                    failed_pages.append(info.number)
                    continue
            else:  # 'notext': no usable text layer - the VLM decides
                decision, vlm_text, rel_path = self._vlm_page(
                    pdf_doc, info, source_name, doc_hash
                )
                if decision == "empty":
                    logger.info(
                        f"[p{info.number}/{total_pages}] done: type=empty "
                        f"(VLM-confirmed, no usable content)"
                    )
                    empty_pages.append(info.number)
                    continue
                page_image_paths = [rel_path] if rel_path else []
                if decision == "text":
                    page_type = "scan"
                    method = "vlm-page"
                    text = f"{OCR_TEXT_LABEL}\n{vlm_text}"
                elif INCLUDE_NON_TEXT_PAGES:
                    page_type = "drawing"
                    method = "image" if rel_path else "placeholder"
                    text = self._image_marker(rel_path) if rel_path else NON_TEXT_PLACEHOLDER
                    image_pages.append(info.number)
                else:
                    # Flag off: drawing/image pages are dropped from the output
                    logger.info(
                        f"[p{info.number}/{total_pages}] done: type=drawing "
                        f"(INCLUDE_NON_TEXT_PAGES=False, skipped)"
                    )
                    continue

            if method == "marker":
                text = self._apply_images(text, image_map)
            elif method in ("pymupdf-text", "vlm-page") and page_image_paths:
                # Text came from the PyMuPDF layer or from the VLM page pass:
                # append the saved images (Marker references / the page render)
                # so the drawings/scans behind the text are not lost
                text = text + "\n\n" + "\n".join(self._image_marker(p) for p in page_image_paths)

            metadata = self._base_metadata(source_name)
            metadata.update(
                {
                    "page_number": info.number,
                    "page_type": page_type,
                    "extraction_method": method,
                }
            )
            if page_image_paths:
                metadata["image_count"] = len(page_image_paths)
                metadata["image_paths"] = ";".join(page_image_paths)
            text = self._collapse_list_numbers(text)
            logger.info(
                f"[p{info.number}/{total_pages}] done: type={page_type} "
                f"method={method} chars={len(text)}"
            )
            built.append((info, Document(page_content=text, metadata=metadata)))

        # Section boundaries, decided only now that the VLM has confirmed
        # which pages are truly empty: the first content page after one or
        # more empty pages starts a new stitched document.
        empty_set = set(empty_pages)
        section_index = 0
        pending_gap = False
        for info in pages_info:
            if info.number in empty_set:
                pending_gap = True
            elif pending_gap:
                section_index += 1
                pending_gap = False
            info.section_index = section_index

        documents: List[Document] = []
        for info, document in built:
            document.metadata["section_index"] = info.section_index
            documents.append(document)

        if empty_pages:
            logger.info(f"Skipped empty pages (VLM-confirmed) {empty_pages} ({source_name})")
        if image_pages:
            logger.info(f"Image pages (drawings/plans) {image_pages} ({source_name})")
        if failed_pages:
            logger.warning(f"No text from pages {failed_pages} ({source_name})")
        logger.info(f"Sections: {section_index + 1} ({source_name})")

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