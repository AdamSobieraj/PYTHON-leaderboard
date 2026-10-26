# PLAN.md: Contract Extraction Pipeline (PDF → data → Salesforce)

An implementation plan intended for the Claude Code CLI. Place it in the repo root next to `CLAUDE.md` (section 0).

## 0. How to work with Claude Code

1. Create a `CLAUDE.md` with the "Rules" section below and a reference to this file.
2. Work in **phases** (section 5). One phase = one session = one commit/PR. Before each phase: `Read PLAN.md, implement phase N, do not go beyond its scope.`
3. Tests first, then implementation. A phase is done when `make check` passes.
4. Use plan mode (`/plan` or Shift+Tab) for phases 3, 4, 6.

### Rules (paste into CLAUDE.md)

> Aligned with the PYTHON-Agent-MCP project conventions: Strategy + hard-limit enforcer, factory + lightweight fallback (local-first), lazy backend imports, always-on and non-fatal metrics, explicit configuration precedence, separated production/experiment data paths.

```
- Python 3.12, uv, ruff, mypy --strict (src/), pytest.
- Pydantic v2 for all contracts (src/contracts_ai/schemas).
- ARCHITECTURE (ports and adapters): pipeline logic (pipeline/, agents/, retrieval/, spec/) communicates with
  the database, S3, LLM, Langfuse, parser and form EXCLUSIVELY through the interfaces in src/contracts_ai/ports/.
  Implementations live in src/contracts_ai/adapters/. Goal: swap an implementation (e.g. a different DB, a
  different storage) without changing the logic.
- No imports of boto3, sqlalchemy, celery, fastapi, openai, langfuse, openpyxl outside adapters/, api/, workers/
  (langchain_core only in ports/document_parser.py and adapters/parsing/). Enforced by import-linter in make check.
- Dependencies injected via constructor / PipelineContext. The only place an implementation is chosen: bootstrap.py
  (composition root). Heavy/optional backend libraries are imported lazily INSIDE bootstrap, so that choosing one
  backend does not pull in the libraries of the others — the system and tests run without any optional dependency.
- Celery tasks and FastAPI endpoints are a thin layer: they build the context via bootstrap and call pipeline/stages.py.
- A swappable algorithm = Strategy pattern: the orchestrator (Context) does not know the implementation, it selects
  the strategy from config via a factory by name. A new strategy = a new class, with no change to the orchestrator
  (see ChunkingStrategy: fixedSize/sentenceBased/semanticChunker/agentic).
- Every swappable strategy comes with a shared "hard-limit enforcer" (last line of defense): regardless of the chosen
  strategy it guarantees a hard limit (e.g. max chunk size). The strategy cares about sense/context, the enforcer
  about the technical limit.
- Every port selects its implementation through a factory based on a config value, and has a lightweight variant
  (in-memory or file/JSONL) as a fallback, so the system works without the core infrastructure (local-first). The
  accessor/factory acts as a singleton with a reset() method for tests.
- A shared contract test suite is run against EVERY implementation of a port (lightweight + production) in make check.
- Ports raise domain exceptions (ArtifactNotFound, RepositoryError, TransientError). Adapters translate library
  exceptions. Celery retry is based on TransientError.
- Artifact key layout (e.g. {id}/{id}_markdown.md) and stable IDs (deterministic hash: source + index + content
  fragment) are defined by the domain (the artifact_key function), not the adapter.
- Metadata: a whitelist of known keys, everything else goes into extra_data; name normalization at the boundary
  (e.g. page → page_number).
- A document page NEVER comes from the LLM: only from page_map.json.
- Celery tasks must be idempotent (check the artifact on S3 before working).
- No contract content in logs. To Langfuse only after masking (src/contracts_ai/observability/masking.py).
- Metrics/telemetry are always on (no "enable" flag) and NEVER break the pipeline: collection errors are logged and
  swallowed (non-fatal). When the primary store (Postgres/Langfuse) is unavailable → file fallback (JSONL). The schema
  is created idempotently (IF NOT EXISTS) at startup.
- Tokens/cost: if the provider does not report usage, estimate it (chars/4) and mark the row metadata.estimated=true
  to separate real data from estimated; cost is always computed from a single place (COST_* / config).
- Production and experiment/evaluation data paths are separated: experimental data goes into separate tables/collections
  (a prefix, e.g. exp_) and is run explicitly (opt-in), never by the normal application flow.
- Configuration: a single accessor (dot notation) with explicit precedence — default (code/YAML) < profile
  (APP_PROFILE) < environment variables < CLI (CLI has the highest priority). Base mechanism: pydantic-settings
  (+ optional YAML profiles). No hard-coded values.
- Do not add dependencies without justification in the PR.
- Commands: make check (lint+types+tests), make up, make down.
```

## 1. Assumptions

| Area | Decision |
|---|---|
| Volume | ~100 contracts/day, PDFs up to 300 pages |
| LLM | Azure OpenAI (private tenant, EU region) |
| Contract types | many; field specification in Excel per type; flat fields |
| Language | Polish |
| PDF → MD converter | **blackbox** behind the `BaseDocumentParser` interface (section 4a); `FakeParser` to start |
| Form / Salesforce | **blackbox** (`FormFiller` Protocol); mock to start |
| Retrieval | hybrid (BM25 + embeddings, RRF) in memory; index persisted on S3 |
| Approval | the user approves before sending to the form |
| Observability | Langfuse (self-hosted); one trace per `contract_id` |

## 2. Stack

FastAPI, Celery + Redis (broker), PostgreSQL (SQLAlchemy 2 + Alembic), boto3 (MinIO locally), `openai` (the `AzureOpenAI` client), `langfuse`, `rank_bm25`, `numpy`, `rapidfuzz`, `openpyxl`, `pydantic-settings`, `tenacity`, `structlog`, `pytest`, `moto` or MinIO in tests, `ruff`, `mypy`, `import-linter` (guards layer boundaries), `langchain-core` (only for the parser interface).

## 3. Repo structure

```
.
├── CLAUDE.md
├── PLAN.md
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── pyproject.toml
├── .env.example
├── alembic/
├── specs/                      # the spec in Excel (versioned)
│   └── spec_v1.xlsx
├── src/contracts_ai/
│   ├── config.py               # pydantic-settings
│   ├── schemas/                # Pydantic: ContractResult, FieldResult, Spec, Chunk...
│   ├── api/
│   │   ├── main.py
│   │   ├── deps.py             # auth, db session
│   │   └── routes/contracts.py
│   ├── ports/                  # interfaces (ABC), zero infrastructure dependencies
│   │   ├── artifact_store.py   # ArtifactStore (S3 and others)
│   │   ├── repositories.py     # ContractRepository, StageRepository, CorrectionRepository, AuditRepository
│   │   ├── document_parser.py  # BaseDocumentParser (interface from the project, returns List[Document])
│   │   ├── llm.py              # LLMClient, EmbeddingClient
│   │   ├── tracing.py          # Tracer
│   │   ├── form_filler.py      # FormFiller
│   │   └── spec_source.py      # SpecSource
│   ├── adapters/               # port implementations; the only place with boto3, sqlalchemy, openai, langfuse, openpyxl
│   │   ├── storage/            # S3ArtifactStore, InMemoryArtifactStore
│   │   ├── db/                 # SqlAlchemy*Repository (models, session), InMemory*Repository
│   │   ├── parsing/            # concrete parsers (BaseDocumentParser) + FakeParser
│   │   ├── llm/                # AzureLLMClient, AzureEmbeddingClient, FakeLLM
│   │   ├── tracing/            # LangfuseTracer, NoopTracer
│   │   ├── form/               # MockFormFiller (Salesforce later)
│   │   └── spec/               # ExcelSpecSource
│   ├── pipeline/               # stage logic: functions/classes taking ports
│   │   ├── context.py          # PipelineContext (set of ports)
│   │   ├── keys.py             # artifact_key(contract_id, kind)
│   │   ├── parsing.py          # documents_to_markdown(): List[Document] → markdown + page_map
│   │   └── stages.py           # convert, build_index, classify, extract_group, validate, finalize, submit
│   ├── bootstrap.py            # composition root: settings → concrete adapters → PipelineContext
│   ├── spec/                   # spec validation rules (pure logic; Excel reading in adapters/spec)
│   ├── retrieval/              # chunker, bm25, embeddings, rrf, index (save/load S3)
│   ├── llm/                    # prompts (versioned), structured output schemas (client in adapters/llm)
│   ├── agents/
│   │   ├── classifier.py
│   │   ├── orchestrator.py     # code, no LLM
│   │   ├── extractor.py
│   │   └── validator.py        # mostly code; LLM-judge only for annexes
│   ├── observability/          # masking (pure logic); Langfuse in adapters/tracing
│   └── workers/
│       ├── app.py              # Celery app, heavy/llm/cpu queues
│       └── tasks.py            # thin wrappers: bootstrap → pipeline.stages
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/               # 3-5 short contracts .md + page_map.json + expected JSON
└── eval/                       # per-field accuracy scoring script
```

## 4. Key contracts

```python
# schemas/result.py (sketch)
class Source(BaseModel):
    original_pdf: str          # s3://bucket/{id}/{id}.pdf
    markdown_file: str         # s3://bucket/{id}/{id}_markdown.md
    page: int                  # from page_map, not from the LLM
    markdown_line: int
    quote: str

class FieldResult(BaseModel):
    field_name: str
    value: str | None
    raw_value: str | None
    confidence: float
    status: Literal["extracted", "not_found", "uncertain", "corrected_by_user"]
    source: Source | None
    candidates: list[Candidate] = []
    user_review: UserReview

class ContractResult(BaseModel):
    contract_id: UUID
    contract_type: str
    spec_version: str
    spec_hash: str
    pipeline_version: str
    prompt_versions: dict[str, str]
    fields: list[FieldResult]

# Ports: full list and signatures in section 4a
```

`page_map.json`: `[{"page": 1, "line_start": 1, "line_end": 48}, ...]`.

Stage statuses (the `stages` table): `pending | running | done | failed | needs_user_input`.

## 4a. Architecture: ports and adapters

Pipeline logic knows only the interfaces. Changing the DB, storage, LLM provider or parser = a new adapter + a value in config, with no change to `pipeline/`, `agents/`, `retrieval/`.

```
 api/ , workers/  (delivery, thin)
        │ bootstrap.build_context(settings)
        ▼
 pipeline/ agents/ retrieval/ spec/   ──►  ports/ (ABC)  ◄──  adapters/ (boto3, sqlalchemy, openai, langfuse, ...)
        (all logic, zero infrastructure imports)
```

### Ports (signature sketch)

```python
# ports/artifact_store.py
class ArtifactStore(ABC):
    @abstractmethod
    def put_bytes(self, key: str, data: bytes, content_type: str | None = None) -> str: ...  # returns URI
    @abstractmethod
    def get_bytes(self, key: str) -> bytes: ...          # ArtifactNotFound
    @abstractmethod
    def exists(self, key: str) -> bool: ...
    @abstractmethod
    def uri(self, key: str) -> str: ...
    # helpers (default implementation in the base class): put_json/get_json/put_text/get_text

# ports/repositories.py
class ContractRepository(ABC):
    def create(self, contract_id: UUID, uploaded_by: str, filename: str) -> None: ...
    def get(self, contract_id: UUID) -> ContractRecord: ...
    def set_type(self, contract_id: UUID, contract_type: str, source: Literal["auto", "user"]) -> None: ...
    def save_result(self, result: ContractResult) -> None: ...
    def get_result(self, contract_id: UUID) -> ContractResult | None: ...
class StageRepository(ABC):
    def start(self, contract_id: UUID, stage: str) -> None: ...
    def finish(self, contract_id: UUID, stage: str, meta: dict) -> None: ...
    def fail(self, contract_id: UUID, stage: str, error: str) -> None: ...
    def needs_user_input(self, contract_id: UUID, stage: str, reason: str) -> None: ...
    def list(self, contract_id: UUID) -> list[StageRecord]: ...
class CorrectionRepository(ABC): ...   # user corrections (data for evaluation)
class AuditRepository(ABC): ...        # who uploaded / approved / corrected

# ports/document_parser.py  (interface from the project, unchanged)
import io
from abc import ABC, abstractmethod
from typing import List, Union
from langchain_core.documents import Document

class BaseDocumentParser(ABC):
    """Abstract base class for all document parsers."""
    @abstractmethod
    def parse(self, file_source: Union[str, io.BytesIO, bytes], **kwargs) -> List[Document]:
        """Processes a file (local or an in-memory stream) and returns
        a list of Document objects (with content in Markdown format)."""

# ports/llm.py
class LLMClient(ABC):
    def complete_structured(self, *, deployment: str, system: str, user: str,
                            schema: type[BaseModel], trace: TraceHandle | None) -> BaseModel: ...
class EmbeddingClient(ABC):
    def embed(self, texts: list[str]) -> np.ndarray: ...

# ports/tracing.py, form_filler.py, spec_source.py: Tracer, FormFiller, SpecSource
```

`PipelineContext` is a dataclass holding all ports (`store`, `contracts`, `stages`, `corrections`, `audit`, `parser`, `llm`, `embeddings`, `tracer`, `form_filler`, `spec_source`) plus `settings`. Every stage has the signature `def convert(ctx: PipelineContext, contract_id: UUID) -> None`.

### Integration with `BaseDocumentParser`

The parser is a port with no extra layer. A concrete implementation goes into `adapters/parsing/` and is registered in `bootstrap.py` under the name from `PARSER_BACKEND`. The `convert` stage:

1. `pdf = ctx.store.get_bytes(artifact_key(id, "pdf"))`
2. `docs = ctx.parser.parse(io.BytesIO(pdf), **settings.parser_kwargs)`
3. `parsed = documents_to_markdown(docs, page_key, page_base)` (a pure function in `pipeline/parsing.py`)
4. writes `{id}_markdown.md` and `{id}_page_map.json` through `ctx.store`.

The interface returns only `List[Document]`, while the pipeline needs a page map. So we adopt a contract for `documents_to_markdown`:

- The page number comes from `Document.metadata[PARSER_PAGE_METADATA_KEY]` (default `page`), with a `PARSER_PAGE_BASE` correction (0 or 1).
- No page number in the metadata → `PageInfoMissing` (the `convert` stage ends with an error). Pages are **not guessed**. Optionally the flag `PARSER_ASSUME_ONE_DOC_PER_PAGE=true`, when the parser returns exactly one `Document` per page.
- Documents from the same page are merged. Page numbers must be non-decreasing.
- Before the content of each page a `<!-- page:N -->` marker is inserted on its own line. Line numbering starts at 1, and the page's range in `page_map` includes the marker.
- A page with no text (an empty scan) is saved with empty content and a warning in the stage metadata.
- The function verifies consistency: each line belongs to exactly one page, and ranges do not overlap.
- Tests on a `FakeParser` returning a recorded `List[Document]`, including cases: missing metadata, numbering from 0 and from 1, multiple `Document`s per page, an empty page.

### Automatically enforced rules

- `import-linter` in `pyproject.toml`: `pipeline`, `agents`, `retrieval`, `spec`, `schemas` must not import `adapters`, `api`, `workers`, `boto3`, `sqlalchemy`, `celery`, `fastapi`, `openai`, `langfuse`, `openpyxl`. `ports` must not import anything except `schemas`, stdlib, `numpy`, `pydantic` and `langchain_core` (only `document_parser.py`).
- Contract tests in `tests/contracts/`: one suite parametrized over the port implementations (in-memory + real), e.g. `test_artifact_store_contract.py` run against `InMemoryArtifactStore` and `S3ArtifactStore` (MinIO), `test_repositories_contract.py` against in-memory and SQLAlchemy.
- The pipeline never builds clients on its own: no `boto3.client(...)`, `create_engine(...)`, `AzureOpenAI(...)` outside `adapters/` and `bootstrap.py`.

## 5. Implementation phases

### Phase 1. Skeleton and infrastructure
- `pyproject.toml` (uv), `Makefile`, `ruff`, `mypy`, `pytest`, CI (lint + tests).
- `config.py`, Dockerfile, docker-compose (section 7), `.env.example`.
- Healthcheck API (`/health`), connection to Postgres, Redis, MinIO.
- Skeleton of `ports/`, `adapters/`, `pipeline/context.py`, `bootstrap.py` and the `import-linter` contracts (section 4a), so layer boundaries are guarded from the first commit.
- **DoD**: `make up` starts everything, `make check` green.

### Phase 2. Storage, DB, upload, status
- Ports `ArtifactStore`, `ContractRepository`, `StageRepository` + in-memory and production implementations (`S3ArtifactStore` on MinIO, SQLAlchemy repositories) + contract tests on both. Generate `contract_id` (UUID4). Endpoints use only the ports from `PipelineContext`.
- `POST /contracts` (validation: MIME, magic bytes `%PDF`, max size from config) → save `{id}/{id}.pdf`, record in DB, start the chain.
- `GET /contracts/{id}/status` (list of stages, errors).
- Auth: to start, a header/JWT behind the `get_current_user` interface; save `uploaded_by` (audit).
- **DoD**: an integration upload test on MinIO; status returns `pending`.

### Phase 3. Excel specification
- `spec/loader.py` (openpyxl → Pydantic `Spec`), `spec/validator.py` with rules: uniqueness of `field_name` within a type, existence of `type_id`, known `data_type`, an `enum` has `allowed_values`, an active type has a required field and a `group`, groups ≤ 8 fields (warning).
- File hash → `spec_hash`. Validation errors block application startup.
- Generate `specs/spec_v1.xlsx` with 2 contract types (an example) per the schema: sheets `contract_types`, `fields`, `dictionary`, `changelog`.
- **DoD**: tests on a correct and 6 incorrect Excel files.

### Phase 4. Conversion and index (retrieval)
- Port `BaseDocumentParser` (as in section 4a) + `FakeParser` (returns a recorded `List[Document]` from fixtures).
- `pipeline/parsing.py::documents_to_markdown` per the contract in section 4a (page markers, page_map, consistency validation).
- Task `convert_pdf` (queue `heavy`) as a thin wrapper on `stages.convert`: save `{id}_markdown.md` and `{id}_page_map.json` through `ArtifactStore`.
- `retrieval/chunker.py`: splitting by headers/paragraphs/§, overlap, a chunk carries `line_start/line_end/page_range`; lines numbered at render time (`532| text`).
- Hybrid: BM25 (`rank_bm25`, simple Polish tokenization + lowercase) + Azure embeddings (batch, retry, cache) + RRF.
- Index persisted on S3 (`index/chunks.json`, `index/embeddings.npy`); the worker loads and caches it in the process.
- Short-contract threshold (`SHORT_DOC_PAGES`, default 40): skip retrieval, return the whole text.
- **DoD**: retrieval tests on fixtures (recall@k for known fields ≥ the agreed threshold), index reproducible from S3.

### Phase 5. Classifier
- A versioned prompt in `llm/prompts/classifier_v1.md`; input: the first 3-5 pages + headers + the list of types.
- Structured output: `contract_type`, `confidence`, `alternatives`, `evidence_lines`.
- `confidence < CLASSIFIER_MIN_CONF` or a type outside the list → stage `needs_user_input`, the chain stops.
- `POST /contracts/{id}/type` (the user chooses a type) → resumes part B of the pipeline.
- **DoD**: tests with a fake LLM for: a certain type, an uncertain type, a type outside the list, resumption.

### Phase 6. Extraction (agents)
- `orchestrator.py` (code): fields → groups per the `group` column; concurrency limit (semaphore/rate limiter for TPM/RPM).
- `extractor.py`: for a group, retrieval per field (query = name + description + synonyms) → deduplicate chunks → prompt → structured output with `candidates` (`raw_value`, `value`, `line`, `quote`, `confidence`).
- Celery: `chord(group(extract_group...), validate.s())`, queue `llm`, `acks_late`, `autoretry_for` (429, timeouts) with exponential backoff + jitter.
- **DoD**: tests with a fake LLM and golden files; a test that the prompt never contains more than `MAX_CONTEXT_TOKENS`.

### Phase 7. Validator and result
- Fuzzy match the quote against lines ±2 (`rapidfuzz`, threshold `QUOTE_MATCH_MIN`), no match → `uncertain`.
- `line → page` from `page_map.json`.
- Parsers and validators for types: date, decimal, integer, bool, enum, NIP (checksum), REGON, IBAN, e-mail.
- Annexes: detect document boundaries (rules by headers, e.g. "Aneks nr"); a later document overrides an earlier one; on ambiguity an LLM-judge decides, and in doubt the field is `uncertain`.
- `missing_required` for required fields that are `not_found`.
- Final confidence = f(LLM, fuzzy, format, candidate agreement); the formula in one place + tests.
- Save `{id}/{id}.json` (S3) + status `ready`.
- **DoD**: unit tests for the validators (min. 5 cases per data type), a test for an annex overriding a value.

### Phase 8. User review and form
- `GET /contracts/{id}/result`, `PATCH /contracts/{id}/fields/{name}` (correction → `corrected_by_user`, save who and when), `POST /contracts/{id}/approve`.
- After `approve`: task `submit_form` → `FormFiller` (the mock saves to a file/DB), the result in the status.
- Corrections go into the `field_corrections` table (data for evaluation).
- **DoD**: an E2E test on fakes: upload → ready → patch → approve → submit.

### Phase 9. Langfuse, resilience, evaluation
- One trace per `contract_id` (a deterministic trace id from `contract_id`, so tasks in different workers land in the same trace; check the API in the installed SDK version). Spans: stage, agent, LLM call; tags: `spec_version`, `prompt_version`, `contract_type`. Cost and tokens per stage.
- `masking.py`: mask PESEL, NIP, IBAN, e-mail, phone before sending to Langfuse (a configurable disable only in the dev environment).
- Dead-letter / manual retry: `POST /contracts/{id}/retry?stage=...` (admin).
- Retention: a periodic task (celery beat) deleting data after `RETENTION_DAYS`.
- `eval/run_eval.py`: comparison against hand-described contracts, per-field metrics (exact match, `not_found` precision/recall), CSV report.
- **DoD**: the evaluation report is generated with one command (`make eval`).

### Phase 10. Hardening
- API rate limiting, size limits, antivirus (ClamAV as an optional sidecar), S3 encryption (SSE), presigned upload for large files (`POST /contracts/presign` + callback).
- Metrics (Prometheus) and alerts; Flower only on the internal network.
- Load test: 100 contracts × 300 pages (fake LLM with delay), checking queues and time.

## 6. Configuration (`.env.example`)

```
APP_ENV=dev
STORE_BACKEND=s3               # adapter choice in bootstrap.py
REPO_BACKEND=sqlalchemy
PARSER_BACKEND=fake            # registered parser name
PARSER_PAGE_METADATA_KEY=page
PARSER_PAGE_BASE=0             # 0 or 1: page numbering in Document metadata
LLM_BACKEND=azure
TRACER_BACKEND=langfuse
FORM_BACKEND=mock
DATABASE_URL=postgresql+psycopg://app:app@postgres:5432/contracts
REDIS_URL=redis://redis:6379/0
S3_ENDPOINT_URL=http://minio:9000
S3_BUCKET=contracts
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=
AZURE_DEPLOYMENT_CHAT=          # main extraction model
AZURE_DEPLOYMENT_CHAT_MINI=     # classifier
AZURE_DEPLOYMENT_EMBEDDING=
LANGFUSE_HOST=
LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
SPEC_PATH=/app/specs/spec_v1.xlsx
SHORT_DOC_PAGES=40
CLASSIFIER_MIN_CONF=0.8
QUOTE_MATCH_MIN=90
LLM_MAX_CONCURRENCY=8
MAX_UPLOAD_MB=100
RETENTION_DAYS=90
```

## 7. Docker

### Dockerfile (multi-stage, uv)

```dockerfile
# syntax=docker/dockerfile:1.7
FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/app/.venv
COPY --from=ghcr.io/astral-sh/uv:0.5 /uv /usr/local/bin/uv
WORKDIR /app

# --- production dependencies ---
FROM base AS builder
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev
COPY src ./src
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# --- dev/test image (includes developer tools) ---
FROM base AS dev
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project
COPY . .
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen
ENV PATH="/app/.venv/bin:$PATH" PYTHONPATH=/app/src
CMD ["uvicorn", "contracts_ai.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# --- production image ---
FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app/src
RUN useradd --create-home --uid 1000 app
WORKDIR /app
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --chown=app:app src ./src
COPY --chown=app:app alembic ./alembic
COPY --chown=app:app alembic.ini ./
COPY --chown=app:app specs ./specs
USER app
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import urllib.request;urllib.request.urlopen('http://localhost:8000/health')" || exit 1
CMD ["uvicorn", "contracts_ai.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Note: if the converter blackbox requires system libraries (e.g. poppler, tesseract), add them in a separate stage/image for the `heavy` worker, so as not to bloat the API image.

### docker-compose.yml (dev)

```yaml
x-app: &app
  build:
    context: .
    target: dev
  env_file: .env
  volumes:
    - ./src:/app/src
    - ./specs:/app/specs
  depends_on:
    postgres: {condition: service_healthy}
    redis: {condition: service_healthy}
    minio: {condition: service_healthy}

services:
  api:
    <<: *app
    ports: ["8000:8000"]

  worker-heavy:
    <<: *app
    command: celery -A contracts_ai.workers.app worker -Q heavy,cpu -c 2 -n heavy@%h --loglevel=INFO
    # prod: run without volumes and with target: runtime

  worker-llm:
    <<: *app
    command: celery -A contracts_ai.workers.app worker -Q llm -c 8 -n llm@%h --loglevel=INFO

  beat:
    <<: *app
    command: celery -A contracts_ai.workers.app beat --loglevel=INFO

  flower:
    <<: *app
    command: celery -A contracts_ai.workers.app flower --port=5555
    ports: ["5555:5555"]

  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app
      POSTGRES_DB: contracts
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app -d contracts"]
      interval: 5s
      retries: 10

  redis:
    image: redis:7
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      retries: 10

  minio:
    image: minio/minio
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    ports: ["9000:9000", "9001:9001"]
    volumes: [miniodata:/data]
    healthcheck:
      test: ["CMD", "mc", "ready", "local"]
      interval: 5s
      retries: 10

  minio-init:
    image: minio/mc
    depends_on:
      minio: {condition: service_healthy}
    entrypoint: >
      /bin/sh -c "mc alias set local http://minio:9000 minioadmin minioadmin &&
      mc mb -p local/contracts || true"

volumes:
  pgdata:
  miniodata:
```

Run self-hosted Langfuse separately (the official Langfuse compose requires, among others, ClickHouse, Redis and S3), and provide `LANGFUSE_HOST` in `.env`. Do not squeeze it into this compose.

### Makefile (minimum)

```make
up:      ; docker compose up -d --build
down:    ; docker compose down
check:   ; docker compose run --rm api sh -c "ruff check . && mypy src && pytest -q"
migrate: ; docker compose run --rm api alembic upgrade head
eval:    ; docker compose run --rm api python -m eval.run_eval
```

## 8. Testing strategy

- **Architecture**: `import-linter` and port contract tests (one suite, many implementations) in `make check`.
- **Unit**: chunker, RRF, type validators, quote fuzzy match, line→page mapping, Excel loader.
- **Contract**: a fake LLM returning recorded answers (golden); structured output schema tests.
- **Integration**: MinIO + Postgres + Redis in compose, Celery in eager mode only for logic tests, a separate test with a real worker.
- **Evaluation** (`eval/`): 10-20 hand-described contracts of different types, per-field metrics; a comparison of the "whole contract" vs "retrieval" modes.
- A real LLM only in marked tests (`-m live`), outside CI.

## 9. Decisions and risks to keep in mind

- **Swapping implementations**: no change to the DB, storage or LLM may touch `pipeline/`, `agents/`, `retrieval/`. If it does, the port boundary is drawn wrong and must be fixed.
- **Page metadata from the parser**: `documents_to_markdown` requires a page number in `Document.metadata`. Agree this with the parser author before phase 4.
- **Index across workers**: always persisted on S3; do not assume shared memory.
- **Resumption after `needs_user_input`**: the pipeline is split into part A (convert → index → classify) and B (extract → validate → finalize); B starts from the API.
- **Azure TPM/RPM**: a global limiter (Redis) shared by workers, not just an in-process semaphore.
- **Versioning**: `spec_hash`, `prompt_versions`, `pipeline_version` in every result; reprocessing creates a new result version instead of overwriting.
- **Personal data**: masking before Langfuse, no content in logs, S3 encryption, retention.
- **To be decided later**: the real converter (must return page_map), the form/Salesforce shape, the review UI (who builds it), the authentication mechanism.

## 10. Ready starting prompts for Claude Code

```
Phase 1: Read PLAN.md and CLAUDE.md. Implement phase 1 (skeleton, Dockerfile, compose, Makefile, CI). Do not implement business logic. At the end run make check and make up.

Phase 3: Implement phase 3. First write the Excel validator tests (a correct file + 6 incorrect ones), then the implementation. Generate specs/spec_v1.xlsx with the script in scripts/make_sample_spec.py.

Phase 6: Enter plan mode. Propose the module split and signatures for phase 6, wait for approval, only then implement. Use FakeLLM in the tests.
```
