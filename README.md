## 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Architecture](#-architecture)
- [Implemented Parsers](#-implemented-parsers)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Running the Benchmark](#-running-the-benchmark)
- [Project Structure](#-project-structure)
- [Benchmark Results](#-benchmark-results)
- [Adding a New Parser](#-adding-a-new-parser)
- [Margin Configuration](#-margin-configuration)
- [Roadmap](#-roadmap)
- [FAQ](#-faq)

---

## 🎯 About the Project

**PDF Parse Bench** is a modular platform for objectively comparing
different PDF document processing methods in the context of building
**RAG (Retrieval-Augmented Generation)** systems.

The project answers the following questions:

| Question | How the platform answers it |
|---|---|
| Which parser handles tables best? | Side-by-side Markdown output comparison |
| Which one is the fastest? | Time measurement with millisecond precision |
| How much text does each parser extract? | Character and element counting |
| Does OCR work correctly on scanned documents? | Tests on scanned PDFs |
| How does GPU affect Docling's speed? | CPU vs GPU benchmark |

Every parser implements a **uniform interface** (`BaseDocumentParser`),
enabling a fair apples-to-apples comparison.

---

## 🏗 Architecture

```
                         ┌──────────────────────┐
                         │   BaseDocumentParser │  ← Abstract interface
                         │   (base_parser.py)   │     (ABC)
                         └──────────┬───────────┘
         ┌───────────────────┬──────┴────────────┬───────────────────┐
         ▼                   ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  PyMuPDF4LLM    │ │   Kreuzberg     │ │   Docling       │ │   MinerU        │
│  (C++, fastest) │ │   (+ Tesseract) │ │   (DL + GPU)    │ │   (DL + OCR)    │
│                 │ │                 │ │                 │ │                 │
│  pdf_parser_    │ │  pdf_parser_    │ │  pdf_parser_    │ │  pdf_parser_    │
│  pymupdf4llm.py │ │  kreuzberg.py   │ │  docling.py     │ │  mineru.py      │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │                   │
         └───────────────────┴──────┬────────────┴───────────────────┘
                                    ▼
                         ┌───────────────────────┐
                         │   Benchmark Runner    │
                         │   (main.py)           │
                         │                       │
                         │  • Time & Resources   │
                         │  • Hardware monitor   │
                         │  • Chart Generator    │
                         └──────────┬────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │   output/            │
                         │  ├── pymupdf4llm/    │
                         │  ├── kreuzberg/      │
                         │  ├── docling/        │
                         │  ├── mineru/         │
                         │  ├── timing_*.txt    │
                         │  └── charts_*.png    │ ← Visual Dashboard
                         └──────────────────────┘
```

---

## 🔌 Implemented Parsers

### 1. PyMuPDF4LLM — `pdf_parser_pymupdf4llm.py`

| Feature | Value |
|---|---|
| Engine | C++ (MuPDF) |
| Speed | ⚡⚡⚡⚡⚡ fastest |
| Tables | ✅ good |
| Scanned PDF OCR | ❌ none |
| GPU | not required |
| Native Markdown | ✅ yes |

**When to use:** digital PDFs, speed is the priority, no GPU available.

---

### 2. Kreuzberg — `pdf_parser_kreuzberg.py`

| Feature | Value |
|---|---|
| Engine | Tesseract + PyMuPDF |
| Speed | ⚡⚡⚡ |
| Tables | ⚠️ basic |
| Scanned PDF OCR | ✅ Tesseract |
| GPU | not required |
| API | asynchronous (async/await) |

**When to use:** mixed documents (digital + scans), no GPU available.

---

### 3. Docling (IBM) — `pdf_parser_docling.py`

| Feature | Value |
|---|---|
| Engine | Deep Learning (TableFormer, LayoutLM) |
| Speed | ⚡⚡ (GPU) / ⚡ (CPU) |
| Tables | ✅✅✅ best |
| Scanned PDF OCR | ✅ EasyOCR (multilingual) |
| GPU | optional (CUDA), 10x speedup |
| Header/footer removal | semantic (PAGE_HEADER/FOOTER) |
| Native Markdown | ✅ yes |

**When to use:** complex tables, scans, documents with equations, when quality > speed.

---

### 4. MinerU (OpenDataLab) — `pdf_parser_mineru.py`

| Feature | Value |
|---|---|
| Engine | DL (LayoutLMv3) |
| Speed | ⚡⚡ |
| Tables | ✅✅ great | 
| OCR | ✅ PaddleOCR |
| GPU | optional | 
| Native Markdown | ✅ yes |

**When to use:** highly structured academic papers, complex layouts, math formulas.

---

**Three-layer header/footer removal:**

```
Layer 1: PRE-CROP      — physical PyMuPDF cropbox trimming
Layer 2: SEMANTIC       — Docling recognizes PAGE_HEADER / PAGE_FOOTER
Layer 3: POST-FILTER    — bounding box filter (fallback without PyMuPDF)
```

---

## 💻 System Requirements

### Minimum (CPU only)

| Component | Requirement |
|---|---|
| OS | Linux / macOS / Windows |
| Python | 3.10+ |
| RAM | 8 GB |
| Disk | 3 GB (Docling models ~1.5 GB, cache) |
| Tesseract | required for Kreuzberg |

### Recommended (with GPU)

| Component | Requirement |
|---|---|
| GPU | NVIDIA with CUDA 12.1+ (min. 4 GB VRAM) |
| RAM | 16 GB |
| CUDA Toolkit | 12.1 |
| cuDNN | 8.x |

---

## 🚀 Installation

### Step 1 — Clone the repository

```bash
git clone https://github.com/your-username/pdf-parse-bench.git
cd pdf-parse-bench
```

### Step 2 — Virtual environment

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Step 3 — Install dependencies

#### Option A: Full installation (GPU + all parsers)

```bash
# 1. PyTorch with CUDA (BEFORE other packages!)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# 2. All parsers and dependencies
pip install -r requirements.txt

# 3. Tesseract OCR (required by Kreuzberg)
# Ubuntu/Debian:
sudo apt-get install tesseract-ocr tesseract-ocr-pol

# macOS:
brew install tesseract tesseract-lang

# Windows: download installer from https://github.com/UB-Mannheim/tesseract/wiki
```

#### Option B: Minimal installation (PyMuPDF4LLM only, no GPU)

```bash
pip install pymupdf4llm langchain-core
```

#### Option C: No GPU (CPU only, all parsers)

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

### Step 4 — Verify installation

```bash
# Check GPU
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"

# Check Tesseract
tesseract --version

# Check all parsers
python -c "
from pdf_parser_pymupdf4llm import PdfParser as P1
from pdf_parser_kreuzberg import PdfParser as P2
from pdf_parser_docling import PdfParser as P3
print('All parsers loaded successfully!')
"
```

---

## 📦 requirements.txt

```text
# ── Core ──────────────────────────────────────
langchain-core>=0.2.0

# ── Parser: PyMuPDF4LLM ──────────────────────
PyMuPDF>=1.24.0
pymupdf4llm>=0.0.12

# ── Parser: Kreuzberg ────────────────────────
kreuzberg>=0.3.0

# ── Parser: Docling (IBM) ────────────────────
docling>=2.0.0
docling-core>=2.0.0
easyocr>=1.7.0

# ── GPU (install BEFORE requirements.txt) ────
# torch (installed separately with CUDA index)
# torchvision (installed separately with CUDA index)
```

---

## ▶️ Running the Benchmark

### Basic usage

```bash
# Default test file (data/ISO_20022_Programme_UHB_SR2023_Edition.pdf)
python main.py

# Custom PDF file
python main.py path/to/your/file.pdf

# Scanned document (OCR test)
python main.py data/scanned_document.pdf
```

### What happens after launch

```
1. The output/ folder is cleaned (fresh results)
2. Each parser processes the same PDF
3. For each parser the following is measured:
   - Processing time (seconds)
   - Number of extracted elements (pages)
   - Total character count
4. Markdown is saved to output/<parser>/<filename>.md
5. Summary report → output/timing_<filename>.txt
```

### Example console output

```
No file argument provided. Using default: data/ISO_20022_Programme_UHB_SR2023_Edition.pdf

[pymupdf4llm] Processing file: data/ISO_20022_Programme_UHB_SR2023_Edition.pdf...
[pymupdf4llm] Saving output to: output/pymupdf4llm/ISO_20022_Programme_UHB_SR2023_Edition.md
[pymupdf4llm] Done! Elements saved: 245, Characters: 389102. Time: 1.23 s.

[kreuzberg] Processing file: data/ISO_20022_Programme_UHB_SR2023_Edition.pdf...
[kreuzberg] Saving output to: output/kreuzberg/ISO_20022_Programme_UHB_SR2023_Edition.md
[kreuzberg] Done! Elements saved: 245, Characters: 367890. Time: 4.56 s.

[docling] Processing file: data/ISO_20022_Programme_UHB_SR2023_Edition.pdf...
[docling] Saving output to: output/docling/ISO_20022_Programme_UHB_SR2023_Edition.md
[docling] Done! Elements saved: 245, Characters: 401234. Time: 12.78 s.

Saving performance report to: output/timing_ISO_20022_Programme_UHB_SR2023_Edition.txt
All tasks completed successfully. Check the 'output' folder.
```

### Example report (`output/timing_*.txt`)

```
Processing report for file: data/ISO_20022_Programme_UHB_SR2023_Edition.pdf
============================================================
Parser: pymupdf4llm
Execution time: 1.2340 seconds
Number of returned elements (e.g. pages): 245
Total extracted characters: 389102
----------------------------------------
Parser: kreuzberg
Execution time: 4.5670 seconds
Number of returned elements (e.g. pages): 245
Total extracted characters: 367890
----------------------------------------
Parser: docling
Execution time: 12.7800 seconds
Number of returned elements (e.g. pages): 245
Total extracted characters: 401234
----------------------------------------
```

---

## 📁 Project Structure

```
PYTHON_leaderboard/
├── data/
│   └── ISO_20022_Programme_UHB_SR2023_Edition.pdf
├── output/                              # Benchmark results
│   ├── docling/                         # Markdown outputs
│   ├── kreuzberg/
│   ├── pymupdf4llm/
│   ├── mineru/
│   ├── timing_ISO_*.txt                 # Text Report
│   └── charts_ISO_*.png                 # 📊 Auto-generated Dashboard
├── base_parser.py
├── main.py                              # Benchmark runner
├── pdf_parser_docling.py
├── pdf_parser_kreuzberg.py
├── pdf_parser_mineru.py                 # New parser!
└── pdf_parser_pymupdf4llm.py

```

---

## 🧩 Adding a New Parser

Every new parser **must** inherit from `BaseDocumentParser` and implement
the `parse()` method:

### Base interface (contract)

```python
import io
from abc import ABC, abstractmethod
from typing import List, Union
from langchain_core.documents import Document


class BaseDocumentParser(ABC):
    """Abstract base class for all document parsers."""

    @abstractmethod
    def parse(
        self, file_source: Union[str, io.BytesIO, bytes], **kwargs
    ) -> List[Document]:
        """
        Processes a file (local path or in-memory stream) and returns
        a list of Document objects (with content in Markdown format).

        Args:
            file_source: File path (str), raw bytes (bytes),
                         or in-memory stream (io.BytesIO).

        Returns:
            List of langchain Document objects where:
            - page_content: content in Markdown format
            - metadata["page_number"]: page number (int)
        """
        pass
```

### New parser template

```python
# pdf_parser_my_parser.py

import io
import logging
import os
from typing import List, Union

from langchain_core.documents import Document
from base_parser import BaseDocumentParser

logger = logging.getLogger(__name__)


class PdfParser(BaseDocumentParser):
    """My new PDF → Markdown parser."""

    def parse(
        self, file_source: Union[str, io.BytesIO, bytes], **kwargs
    ) -> List[Document]:
        documents = []
        source_name = (
            os.path.basename(file_source)
            if isinstance(file_source, str)
            else "in-memory stream"
        )

        try:
            # 1. Load PDF (handle str, bytes, BytesIO)
            if isinstance(file_source, str):
                with open(file_source, "rb") as f:
                    pdf_bytes = f.read()
            elif isinstance(file_source, io.BytesIO):
                pdf_bytes = file_source.read()
            elif isinstance(file_source, bytes):
                pdf_bytes = file_source
            else:
                raise ValueError(f"Unsupported type: {type(file_source)}")

            # 2. Your parsing logic
            #    ...
            #    md_pages = your_parser.convert(pdf_bytes)

            # 3. Convert to List[Document]
            # for i, page_md in enumerate(md_pages):
            #     if page_md.strip():
            #         documents.append(
            #             Document(
            #                 page_content=page_md.strip(),
            #                 metadata={"page_number": i + 1},
            #             )
            #         )

            return documents

        except Exception as e:
            logger.error(f"Parsing error ({source_name}): {e}")
            return []
```

### Register in the benchmark

Add the import and entry in `main.py`:

```python
# main.py — add import
from pdf_parser_my_parser import PdfParser as MyParser

# Add entry to the parsers dictionary:
parsers = {
    "pymupdf4llm": PyMuPdfParser,
    "kreuzberg": KreuzbergParser,
    "docling": DoclingParser,
    "my_parser": MyParser,            # ← NEW
}
```

**That's it.** The benchmark will automatically:
- Create the `output/my_parser/` folder
- Measure execution time
- Count characters and elements
- Add results to the report

---

## ✂️ Margin Configuration

All parsers trim repeating page headers and footers (e.g., page numbers,
company logos) by manipulating the PyMuPDF CropBox.

### Default values

| Parser | Top | Bottom |
|---|---|---|
| PyMuPDF4LLM | 50 pt (~1.8 cm) | 60 pt (~2.1 cm) |
| Kreuzberg | 50 pt | 60 pt |
| Docling | 50 pt | 60 pt |

### Conversion table

```
Points (pt)    Centimeters    What it typically trims
──────────     ───────────    ──────────────────────────
   30           ~1.1 cm       Page number only
   50           ~1.8 cm       Header / small footer
   60           ~2.1 cm       Footer with page number and date
   80           ~2.8 cm       Large company header
  100           ~3.5 cm       Logo + address in footer
  120           ~4.2 cm       Full letterhead
```

> **Note:** A standard A4 page = 595 × 842 typographic points.
> 1 point = 1/72 inch ≈ 0.353 mm.

### Changing margins

**PyMuPDF4LLM / Kreuzberg** — edit the class constants:

```python
TOP_MARGIN_TO_CROP = 80      # increase if the header is large
BOTTOM_MARGIN_TO_CROP = 100   # increase if the footer is elaborate
```

**Docling** — constructor parameters:

```python
parser = DoclingParser(
    top_margin_crop=80,
    bottom_margin_crop=100,
    left_margin_crop=30,      # side margins (optional)
    right_margin_crop=30,
)
```

---

## 📊 Benchmark Results

### Parser comparison (example results)

```
File: ISO_20022_Programme_UHB_SR2023_Edition.pdf (245 pages, ~15 MB)
Hardware: Intel i9-13900K, 64 GB RAM, NVIDIA RTX 4090 24 GB

┌─────────────────┬──────────┬───────────┬──────────┬───────────────┐
│ Parser          │ Time [s] │ Elements  │ Chars    │ Chars/s       │
├─────────────────┼──────────┼───────────┼──────────┼───────────────┤
│ pymupdf4llm     │     1.23 │      245  │  389,102 │   316,344     │
│ kreuzberg       │     4.56 │      245  │  367,890 │    80,678     │
│ docling (GPU)   │    12.78 │      245  │  401,234 │    31,395     │
│ docling (CPU)   │    58.90 │      245  │  401,234 │     6,813     │
└─────────────────┴──────────┴───────────┴──────────┴───────────────┘
```

### Key observations

| Aspect | Best parser |
|---|---|
| Speed | pymupdf4llm (10–50x faster) |
| Text volume | Docling (extracts more via DL) |
| Table quality | Docling (TableFormer) |
| Scanned PDF OCR | Docling (EasyOCR) > Kreuzberg (Tesseract) |
| Heading recognition | Docling (semantic) > PyMuPDF (heuristics) |
| Memory usage | pymupdf4llm (lowest) |

---

## 🗺 Roadmap

### PDF Parsers

- [x] PyMuPDF4LLM (C++, fastest)
- [x] Kreuzberg (Tesseract OCR)
- [x] Docling / IBM (Deep Learning + GPU)
- [ ] Marker (surya OCR + DL, requires GPU)
- [x] MinerU / OpenDataLab (LayoutLMv3 + PaddleOCR)
- [ ] Zerox (Vision LLM — GPT-4o / Gemini)
- [ ] LlamaParse (cloud API)
- [ ] Mistral OCR (cloud API)
- [ ] Azure Document Intelligence

### Chunking (text splitting)

- [ ] MarkdownHeaderTextSplitter (by headings ##)
- [ ] RecursiveCharacterTextSplitter (by characters)
- [ ] SemanticChunker (by embedding similarity)
- [ ] TokenTextSplitter (by model tokens)

### Embeddings

- [ ] OpenAI `text-embedding-3-small` / `large`
- [ ] Cohere `embed-multilingual-v3`
- [ ] Voyage AI `voyage-3`
- [ ] BGE-M3 (local, multilingual)
- [ ] Jina Embeddings v3

### Platform

- [ ] Automated Markdown quality comparison (diff)
- [ ] RAM / VRAM usage benchmark
- [ ] DOCX, PPTX, HTML support
- [ ] Web GUI (Streamlit / Gradio)
- [ ] Report export to CSV / JSON
- [ ] CI/CD with automated benchmark on PR

---

## ❓ FAQ

### Does Docling download models on first run?

**Yes.** On the first run Docling downloads DL models (~1.5 GB) to
cache (`~/.cache/docling/`). Subsequent runs use the cache.

### Can I run only a specific parser?

Yes, simply comment out the unwanted entries in the `parsers` dictionary
in `main.py`:

```python
parsers = {
    "pymupdf4llm": PyMuPdfParser,
    # "kreuzberg": KreuzbergParser,    ← commented out
    # "docling": DoclingParser,        ← commented out
}
```

### Why does Docling extract more characters than PyMuPDF4LLM?

Docling uses Deep Learning models for layout analysis, which allows it to:
- Better recognize text inside tables (TableFormer)
- Extract text from graphical elements
- OCR reads text from scanned fragments

### How do I add S3 support?

Every parser accepts `bytes` and `io.BytesIO`. Simply download the file
from S3 into memory:

```python
import boto3

s3 = boto3.client("s3")
response = s3.get_object(Bucket="bucket", Key="doc.pdf")
pdf_bytes = response["Body"].read()

documents = parser.parse(pdf_bytes)
```

### Docling doesn't see the GPU — what should I do?

```bash
# 1. Check PyTorch CUDA installation
python -c "import torch; print(torch.cuda.is_available())"

# 2. If False — reinstall PyTorch
pip uninstall torch torchvision
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# 3. Check CUDA version
nvidia-smi
```

---

## 📜 License

not stated yet

---

<p align="center">
  <strong>Happy Parsing! 📄→📝</strong>
</p>
```