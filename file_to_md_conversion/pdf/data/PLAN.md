# PLAN.md: Contract Extraction Pipeline (PDF → dane → Salesforce)

Plan implementacji przeznaczony dla Claude Code CLI. Umieść go w katalogu głównym repo obok `CLAUDE.md` (sekcja 0).

## 0. Jak pracować z Claude Code

1. Utwórz `CLAUDE.md` z sekcją "Zasady" poniżej i odwołaniem do tego pliku.
2. Pracuj **fazami** (sekcja 5). Jedna faza = jedna sesja = jeden commit/PR. Przed każdą fazą: `Przeczytaj PLAN.md, zrealizuj fazę N, nie wychodź poza jej zakres.`
3. Najpierw testy, potem implementacja. Faza jest skończona, gdy `make check` przechodzi.
4. Używaj trybu plan (`/plan` lub Shift+Tab) dla faz 3, 4, 6.

### Zasady (wklej do CLAUDE.md)

```
- Python 3.12, uv, ruff, mypy --strict (src/), pytest.
- Pydantic v2 dla wszystkich kontraktów (src/contracts_ai/schemas).
- ARCHITEKTURA (porty i adaptery): logika pipeline'u (pipeline/, agents/, retrieval/, spec/) komunikuje się z
  bazą, S3, LLM, Langfuse, parserem i formularzem WYŁĄCZNIE przez interfejsy z src/contracts_ai/ports/.
  Implementacje są w src/contracts_ai/adapters/. Cel: zmiana implementacji (np. innej bazy, innego storage)
  bez zmian w logice.
- Zakaz importów boto3, sqlalchemy, celery, fastapi, openai, langfuse, openpyxl poza adapters/, api/, workers/
  (langchain_core tylko w ports/document_parser.py i adapters/parsing/). Wymusza to import-linter w make check.
- Zależności wstrzykiwane przez konstruktor / PipelineContext. Jedyne miejsce wyboru implementacji: bootstrap.py.
- Taski Celery i endpointy FastAPI to cienka warstwa: budują kontekst przez bootstrap i wołają pipeline/stages.py.
- Każdy port ma implementację in-memory/fake oraz wspólną suitę testów kontraktowych uruchamianą na wszystkich implementacjach.
- Porty zgłaszają wyjątki domenowe (ArtifactNotFound, RepositoryError, TransientError). Adaptery tłumaczą wyjątki bibliotek.
  Retry w Celery opiera się na TransientError.
- Układ kluczy artefaktów (np. {id}/{id}_markdown.md) definiuje domena (funkcja artifact_key), nie adapter.
- Strona dokumentu NIGDY nie pochodzi od LLM: tylko z page_map.json.
- Zadania Celery muszą być idempotentne (sprawdź artefakt na S3 przed pracą).
- Żadnej treści umów w logach. Do Langfuse tylko po maskowaniu (src/contracts_ai/observability/masking.py).
- Konfiguracja wyłącznie przez zmienne środowiskowe (pydantic-settings).
- Nie dodawaj zależności bez uzasadnienia w PR.
- Komendy: make check (lint+types+tests), make up, make down.
```

## 1. Założenia

| Obszar | Decyzja |
|---|---|
| Wolumen | ok. 100 umów/dzień, PDF do 300 stron |
| LLM | Azure OpenAI (prywatny tenant, region UE) |
| Typy umów | wiele, specyfikacja pól w Excelu per typ, pola płaskie |
| Język | polski |
| Konwerter PDF → MD | **blackbox** za interfejsem `BaseDocumentParser` (sekcja 4a), na start `FakeParser` |
| Formularz / Salesforce | **blackbox** (Protocol `FormFiller`), na start mock |
| Retrieval | hybrid (BM25 + embeddingi, RRF) w pamięci, indeks utrwalany na S3 |
| Zatwierdzenie | user zatwierdza przed wysłaniem do formularza |
| Obserwowalność | Langfuse (self-hosted), jeden trace na `contract_id` |

## 2. Stack

FastAPI, Celery + Redis (broker), PostgreSQL (SQLAlchemy 2 + Alembic), boto3 (MinIO lokalnie), `openai` (klient `AzureOpenAI`), `langfuse`, `rank_bm25`, `numpy`, `rapidfuzz`, `openpyxl`, `pydantic-settings`, `tenacity`, `structlog`, `pytest`, `moto` lub MinIO w testach, `ruff`, `mypy`, `import-linter` (pilnuje granic warstw), `langchain-core` (tylko dla interfejsu parsera).

## 3. Struktura repo

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
├── specs/                      # Excel ze specyfikacją (wersjonowany)
│   └── spec_v1.xlsx
├── src/contracts_ai/
│   ├── config.py               # pydantic-settings
│   ├── schemas/                # Pydantic: ContractResult, FieldResult, Spec, Chunk...
│   ├── api/
│   │   ├── main.py
│   │   ├── deps.py             # auth, db session
│   │   └── routes/contracts.py
│   ├── ports/                  # interfejsy (ABC), zero zależności od infrastruktury
│   │   ├── artifact_store.py   # ArtifactStore (S3 i inne)
│   │   ├── repositories.py     # ContractRepository, StageRepository, CorrectionRepository, AuditRepository
│   │   ├── document_parser.py  # BaseDocumentParser (interfejs z projektu, zwraca List[Document])
│   │   ├── llm.py              # LLMClient, EmbeddingClient
│   │   ├── tracing.py          # Tracer
│   │   ├── form_filler.py      # FormFiller
│   │   └── spec_source.py      # SpecSource
│   ├── adapters/               # implementacje portów; jedyne miejsce z boto3, sqlalchemy, openai, langfuse, openpyxl
│   │   ├── storage/            # S3ArtifactStore, InMemoryArtifactStore
│   │   ├── db/                 # SqlAlchemy*Repository (modele, sesja), InMemory*Repository
│   │   ├── parsing/            # konkretne parsery (BaseDocumentParser) + FakeParser
│   │   ├── llm/                # AzureLLMClient, AzureEmbeddingClient, FakeLLM
│   │   ├── tracing/            # LangfuseTracer, NoopTracer
│   │   ├── form/               # MockFormFiller (później Salesforce)
│   │   └── spec/               # ExcelSpecSource
│   ├── pipeline/               # logika etapów: funkcje/klasy przyjmujące porty
│   │   ├── context.py          # PipelineContext (zbiór portów)
│   │   ├── keys.py             # artifact_key(contract_id, kind)
│   │   ├── parsing.py          # documents_to_markdown(): List[Document] → markdown + page_map
│   │   └── stages.py           # convert, build_index, classify, extract_group, validate, finalize, submit
│   ├── bootstrap.py            # composition root: settings → konkretne adaptery → PipelineContext
│   ├── spec/                   # reguły walidacji specyfikacji (czysta logika; odczyt Excela w adapters/spec)
│   ├── retrieval/              # chunker, bm25, embeddings, rrf, index (save/load S3)
│   ├── llm/                    # prompty (wersjonowane), schematy structured outputs (klient w adapters/llm)
│   ├── agents/
│   │   ├── classifier.py
│   │   ├── orchestrator.py     # kod, bez LLM
│   │   ├── extractor.py
│   │   └── validator.py        # głównie kod; LLM-sędzia tylko dla aneksów
│   ├── observability/          # masking (czysta logika); Langfuse w adapters/tracing
│   └── workers/
│       ├── app.py              # Celery app, kolejki heavy/llm/cpu
│       └── tasks.py            # cienkie wrappery: bootstrap → pipeline.stages
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/               # 3-5 krótkich umów .md + page_map.json + oczekiwane JSON
└── eval/                       # skrypt oceny dokładności per pole
```

## 4. Kluczowe kontrakty

```python
# schemas/result.py (szkic)
class Source(BaseModel):
    original_pdf: str          # s3://bucket/{id}/{id}.pdf
    markdown_file: str         # s3://bucket/{id}/{id}_markdown.md
    page: int                  # z page_map, nie od LLM
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

# Porty: pełna lista i sygnatury w sekcji 4a
```

`page_map.json`: `[{"page": 1, "line_start": 1, "line_end": 48}, ...]`.

Statusy etapów (tabela `stages`): `pending | running | done | failed | needs_user_input`.

## 4a. Architektura: porty i adaptery

Logika pipeline'u zna tylko interfejsy. Zmiana bazy, storage, dostawcy LLM czy parsera = nowy adapter + wartość w konfiguracji, bez zmian w `pipeline/`, `agents/`, `retrieval/`.

```
 api/ , workers/  (delivery, cienkie)
        │ bootstrap.build_context(settings)
        ▼
 pipeline/ agents/ retrieval/ spec/   ──►  ports/ (ABC)  ◄──  adapters/ (boto3, sqlalchemy, openai, langfuse, ...)
        (cała logika, zero importów infrastruktury)
```

### Porty (szkic sygnatur)

```python
# ports/artifact_store.py
class ArtifactStore(ABC):
    @abstractmethod
    def put_bytes(self, key: str, data: bytes, content_type: str | None = None) -> str: ...  # zwraca URI
    @abstractmethod
    def get_bytes(self, key: str) -> bytes: ...          # ArtifactNotFound
    @abstractmethod
    def exists(self, key: str) -> bool: ...
    @abstractmethod
    def uri(self, key: str) -> str: ...
    # pomocnicze (implementacja domyślna w klasie bazowej): put_json/get_json/put_text/get_text

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
class CorrectionRepository(ABC): ...   # korekty usera (dane do ewaluacji)
class AuditRepository(ABC): ...        # kto wgrał / zatwierdził / poprawił

# ports/document_parser.py  (interfejs z projektu, bez zmian)
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

`PipelineContext` to dataclass trzymająca wszystkie porty (`store`, `contracts`, `stages`, `corrections`, `audit`, `parser`, `llm`, `embeddings`, `tracer`, `form_filler`, `spec_source`) plus `settings`. Każdy etap ma sygnaturę `def convert(ctx: PipelineContext, contract_id: UUID) -> None`.

### Integracja z `BaseDocumentParser`

Parser jest portem bez dodatkowej warstwy. Konkretna implementacja trafia do `adapters/parsing/` i jest rejestrowana w `bootstrap.py` pod nazwą z `PARSER_BACKEND`. Etap `convert`:

1. `pdf = ctx.store.get_bytes(artifact_key(id, "pdf"))`
2. `docs = ctx.parser.parse(io.BytesIO(pdf), **settings.parser_kwargs)`
3. `parsed = documents_to_markdown(docs, page_key, page_base)` (czysta funkcja w `pipeline/parsing.py`)
4. zapis `{id}_markdown.md` i `{id}_page_map.json` przez `ctx.store`.

Interfejs zwraca tylko `List[Document]`, a pipeline potrzebuje mapy stron. Dlatego przyjmujemy kontrakt dla `documents_to_markdown`:

- Numer strony pochodzi z `Document.metadata[PARSER_PAGE_METADATA_KEY]` (domyślnie `page`), z korektą `PARSER_PAGE_BASE` (0 lub 1).
- Brak numeru strony w metadanych → `PageInfoMissing` (etap `convert` kończy się błędem). Strony **nie zgadujemy**. Opcjonalnie flaga `PARSER_ASSUME_ONE_DOC_PER_PAGE=true`, gdy parser zwraca dokładnie jeden `Document` na stronę.
- Dokumenty z tą samą stroną są scalane. Numery stron muszą być niemalejące.
- Przed treścią każdej strony wstawiany jest marker `<!-- page:N -->` w osobnej linii. Numeracja linii jest od 1, a zakres strony w `page_map` obejmuje marker.
- Strona bez tekstu (pusty skan) jest zapisywana z pustą treścią i ostrzeżeniem w metadanych etapu.
- Funkcja weryfikuje spójność: każda linia należy do dokładnie jednej strony, a zakresy się nie nakładają.
- Testy na `FakeParser` zwracającym zapisane `List[Document]`, w tym przypadki: brak metadanych, numeracja od 0 i od 1, wiele `Document` na stronę, pusta strona.

### Reguły wymuszane automatycznie

- `import-linter` w `pyproject.toml`: `pipeline`, `agents`, `retrieval`, `spec`, `schemas` nie mogą importować `adapters`, `api`, `workers`, `boto3`, `sqlalchemy`, `celery`, `fastapi`, `openai`, `langfuse`, `openpyxl`. `ports` nie może importować niczego poza `schemas`, stdlib, `numpy`, `pydantic` i `langchain_core` (tylko `document_parser.py`).
- Testy kontraktowe w `tests/contracts/`: jedna suita parametryzowana po implementacjach portu (in-memory + prawdziwa), np. `test_artifact_store_contract.py` odpalany na `InMemoryArtifactStore` i `S3ArtifactStore` (MinIO), `test_repositories_contract.py` na in-memory i SQLAlchemy.
- Pipeline nigdy nie buduje klientów samodzielnie: brak `boto3.client(...)`, `create_engine(...)`, `AzureOpenAI(...)` poza `adapters/` i `bootstrap.py`.

## 5. Fazy implementacji

### Faza 1. Szkielet i infrastruktura
- `pyproject.toml` (uv), `Makefile`, `ruff`, `mypy`, `pytest`, CI (lint + testy).
- `config.py`, Dockerfile, docker-compose (sekcja 7), `.env.example`.
- Healthcheck API (`/health`), połączenie z Postgres, Redis, MinIO.
- Szkielet `ports/`, `adapters/`, `pipeline/context.py`, `bootstrap.py` i kontrakty `import-linter` (sekcja 4a), żeby granice warstw były pilnowane od pierwszego commita.
- **DoD**: `make up` startuje wszystko, `make check` zielony.

### Faza 2. Storage, DB, upload, status
- Porty `ArtifactStore`, `ContractRepository`, `StageRepository` + implementacje in-memory i produkcyjne (`S3ArtifactStore` na MinIO, repozytoria SQLAlchemy) + testy kontraktowe na obu. Generowanie `contract_id` (UUID4). Endpointy używają wyłącznie portów z `PipelineContext`.
- `POST /contracts` (walidacja: MIME, magic bytes `%PDF`, max rozmiar z configu) → zapis `{id}/{id}.pdf`, rekord w DB, start chain.
- `GET /contracts/{id}/status` (lista etapów, błędy).
- Auth: na start nagłówek/JWT za interfejsem `get_current_user`, zapis `uploaded_by` (audyt).
- **DoD**: test integracyjny uploadu na MinIO, status zwraca `pending`.

### Faza 3. Specyfikacja Excela
- `spec/loader.py` (openpyxl → Pydantic `Spec`), `spec/validator.py` z regułami: unikalność `field_name` w typie, istnienie `typ_id`, znany `typ_danych`, `enum` ma `dozwolone_wartosci`, aktywny typ ma pole wymagane i `grupa`, grupy ≤ 8 pól (ostrzeżenie).
- Hash pliku → `spec_hash`. Błędy walidacji blokują start aplikacji.
- Wygeneruj `specs/spec_v1.xlsx` z 2 typami umów (przykład) wg schematu: arkusze `typy_umow`, `pola`, `slownik`, `changelog`.
- **DoD**: testy na poprawnym i 6 błędnych plikach Excela.

### Faza 4. Konwersja i indeks (retrieval)
- Port `BaseDocumentParser` (jak w sekcji 4a) + `FakeParser` (zwraca zapisane `List[Document]` z fixtures).
- `pipeline/parsing.py::documents_to_markdown` wg kontraktu z sekcji 4a (marker stron, page_map, walidacja spójności).
- Zadanie `convert_pdf` (kolejka `heavy`) jako cienki wrapper na `stages.convert`: zapis `{id}_markdown.md` i `{id}_page_map.json` przez `ArtifactStore`.
- `retrieval/chunker.py`: podział po nagłówkach/paragrafach/§, overlap, chunk niesie `line_start/line_end/page_range`; linie numerowane przy renderowaniu (`532| tekst`).
- Hybrid: BM25 (`rank_bm25`, tokenizacja polska prosta + lowercase) + embeddingi Azure (batch, retry, cache) + RRF.
- Zapis indeksu na S3 (`index/chunks.json`, `index/embeddings.npy`); worker ładuje i cache'uje w procesie.
- Próg krótkiej umowy (`SHORT_DOC_PAGES`, domyślnie 40): pomija retrieval, zwraca cały tekst.
- **DoD**: testy retrievalu na fixtures (recall@k dla znanych pól ≥ ustalony próg), indeks odtwarzalny z S3.

### Faza 5. Klasyfikator
- Prompt wersjonowany w `llm/prompts/classifier_v1.md`; wejście: pierwsze 3-5 stron + nagłówki + lista typów.
- Structured output: `contract_type`, `confidence`, `alternatives`, `evidence_lines`.
- `confidence < CLASSIFIER_MIN_CONF` lub typ spoza listy → etap `needs_user_input`, chain się zatrzymuje.
- `POST /contracts/{id}/type` (user wybiera typ) → wznawia część B pipeline'u.
- **DoD**: testy z fake LLM dla: pewny typ, niepewny typ, typ spoza listy, wznowienie.

### Faza 6. Ekstrakcja (agenci)
- `orchestrator.py` (kod): pola → grupy wg kolumny `grupa`; limit równoległości (semafor/rate limiter pod TPM/RPM).
- `extractor.py`: dla grupy: retrieval per pole (zapytanie = nazwa + opis + synonimy) → deduplikacja chunków → prompt → structured output z `candidates` (`raw_value`, `value`, `line`, `quote`, `confidence`).
- Celery: `chord(group(extract_group...), validate.s())`, kolejka `llm`, `acks_late`, `autoretry_for` (429, timeouty) z exponential backoff + jitter.
- **DoD**: testy z fake LLM i golden files; test, że prompt nigdy nie zawiera więcej niż `MAX_CONTEXT_TOKENS`.

### Faza 7. Walidator i wynik
- Fuzzy match cytatu z liniami ±2 (`rapidfuzz`, próg `QUOTE_MATCH_MIN`), brak dopasowania → `uncertain`.
- `line → page` z `page_map.json`.
- Parsery i walidatory typów: date, decimal, integer, bool, enum, NIP (suma kontrolna), REGON, IBAN, e-mail.
- Aneksy: wykrycie granic dokumentów (reguły po nagłówkach, np. "Aneks nr"), późniejszy dokument nadpisuje wcześniejszy; przy niejednoznaczności LLM-sędzia, a w razie wątpliwości `uncertain`.
- `missing_required` dla wymaganych pól `not_found`.
- Confidence końcowe = f(LLM, fuzzy, format, zgodność kandydatów), wzór w jednym miejscu + testy.
- Zapis `{id}/{id}.json` (S3) + status `ready`.
- **DoD**: testy jednostkowe walidatorów (min. 5 przypadków na typ danych), test aneksu nadpisującego wartość.

### Faza 8. Review usera i formularz
- `GET /contracts/{id}/result`, `PATCH /contracts/{id}/fields/{name}` (korekta → `corrected_by_user`, zapis kto i kiedy), `POST /contracts/{id}/approve`.
- Po `approve`: zadanie `submit_form` → `FormFiller` (mock zapisuje do pliku/DB), wynik w statusie.
- Korekty trafiają do tabeli `field_corrections` (dane do ewaluacji).
- **DoD**: test E2E na fake'ach: upload → ready → patch → approve → submit.

### Faza 9. Langfuse, odporność, ewaluacja
- Jeden trace na `contract_id` (deterministyczny trace id z `contract_id`, żeby zadania w różnych workerach trafiały do tego samego trace'a; sprawdź API w zainstalowanej wersji SDK). Spany: etap, agent, wywołanie LLM; tagi: `spec_version`, `prompt_version`, `contract_type`. Koszt i tokeny per etap.
- `masking.py`: maskowanie PESEL, NIP, IBAN, e-mail, telefon przed wysyłką do Langfuse (konfigurowalne wyłączenie tylko w środowisku dev).
- Dead-letter / ręczny retry: `POST /contracts/{id}/retry?stage=...` (admin).
- Retencja: zadanie okresowe (celery beat) usuwające dane po `RETENTION_DAYS`.
- `eval/run_eval.py`: porównanie z ręcznie opisanymi umowami, metryki per pole (exact match, `not_found` precision/recall), raport CSV.
- **DoD**: raport ewaluacji generuje się jedną komendą (`make eval`).

### Faza 10. Hardening
- Rate limiting API, limity rozmiaru, antywirus (ClamAV jako opcjonalny sidecar), szyfrowanie S3 (SSE), presigned upload dla dużych plików (`POST /contracts/presign` + callback).
- Metryki (Prometheus) i alerty, Flower tylko w sieci wewnętrznej.
- Test obciążeniowy: 100 umów × 300 stron (fake LLM z opóźnieniem), sprawdzenie kolejek i czasu.

## 6. Konfiguracja (`.env.example`)

```
APP_ENV=dev
STORE_BACKEND=s3               # wybór adaptera w bootstrap.py
REPO_BACKEND=sqlalchemy
PARSER_BACKEND=fake            # nazwa zarejestrowanego parsera
PARSER_PAGE_METADATA_KEY=page
PARSER_PAGE_BASE=0             # 0 lub 1: numeracja stron w metadata Document
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
AZURE_DEPLOYMENT_CHAT=          # główny model ekstrakcji
AZURE_DEPLOYMENT_CHAT_MINI=     # klasyfikator
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

# --- zależności produkcyjne ---
FROM base AS builder
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev
COPY src ./src
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# --- obraz dev/test (zawiera narzędzia developerskie) ---
FROM base AS dev
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project
COPY . .
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen
ENV PATH="/app/.venv/bin:$PATH" PYTHONPATH=/app/src
CMD ["uvicorn", "contracts_ai.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# --- obraz produkcyjny ---
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

Uwaga: jeśli blackbox konwertera wymaga bibliotek systemowych (np. poppler, tesseract), dodaj je w osobnym etapie/obrazie dla workera `heavy`, żeby nie powiększać obrazu API.

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
    # prod: uruchamiaj bez volumes i z target: runtime

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

Langfuse self-hosted uruchamiaj osobno (oficjalny compose Langfuse wymaga m.in. ClickHouse, Redis i S3), a w `.env` podaj `LANGFUSE_HOST`. Nie wciskaj go do tego compose'a.

### Makefile (minimum)

```make
up:      ; docker compose up -d --build
down:    ; docker compose down
check:   ; docker compose run --rm api sh -c "ruff check . && mypy src && pytest -q"
migrate: ; docker compose run --rm api alembic upgrade head
eval:    ; docker compose run --rm api python -m eval.run_eval
```

## 8. Strategia testów

- **Architektura**: `import-linter` oraz testy kontraktowe portów (jedna suita, wiele implementacji) w `make check`.
- **Unit**: chunker, RRF, walidatory typów, fuzzy match cytatu, mapowanie line→page, loader Excela.
- **Kontraktowe**: fake LLM zwracający zapisane odpowiedzi (golden), test schematów structured outputs.
- **Integracyjne**: MinIO + Postgres + Redis w compose, Celery w trybie eager tylko dla testów logiki, osobny test z prawdziwym workerem.
- **Ewaluacja** (`eval/`): 10-20 ręcznie opisanych umów różnych typów, metryki per pole; porównanie trybów "cała umowa" vs "retrieval".
- LLM realny tylko w oznaczonych testach (`-m live`), poza CI.

## 9. Decyzje i ryzyka do pilnowania

- **Wymiana implementacji**: żadna zmiana bazy, storage czy LLM nie może dotykać `pipeline/`, `agents/`, `retrieval/`. Jeśli dotyka, to granica portu jest źle poprowadzona i trzeba ją poprawić.
- **Metadane stron z parsera**: `documents_to_markdown` wymaga numeru strony w `Document.metadata`. Ustal to z autorem parsera przed fazą 4.
- **Indeks między workerami**: zawsze utrwalany na S3, nie zakładaj współdzielonej pamięci.
- **Wznowienie po `needs_user_input`**: pipeline podzielony na część A (convert → index → classify) i B (extract → validate → finalize), B startuje z API.
- **TPM/RPM Azure**: globalny limiter (Redis) współdzielony przez workery, a nie tylko semafor w procesie.
- **Wersjonowanie**: `spec_hash`, `prompt_versions`, `pipeline_version` w każdym wyniku, ponowne przetwarzanie tworzy nową wersję wyniku zamiast nadpisywać.
- **Dane osobowe**: maskowanie przed Langfuse, brak treści w logach, szyfrowanie S3, retencja.
- **Do ustalenia później**: realny konwerter (musi zwracać page_map), forma formularza/Salesforce, UI do przeglądu (kto go buduje), mechanizm uwierzytelniania.

## 10. Gotowe prompty startowe dla Claude Code

```
Faza 1: Przeczytaj PLAN.md i CLAUDE.md. Zrealizuj fazę 1 (szkielet, Dockerfile, compose, Makefile, CI). Nie implementuj logiki biznesowej. Na końcu uruchom make check i make up.

Faza 3: Zrealizuj fazę 3. Najpierw napisz testy walidatora Excela (poprawny plik + 6 błędnych), potem implementację. Wygeneruj specs/spec_v1.xlsx skryptem w scripts/make_sample_spec.py.

Faza 6: Wejdź w tryb plan. Zaproponuj podział na moduły i sygnatury dla fazy 6, poczekaj na akceptację, dopiero potem implementuj. Użyj FakeLLM w testach.
```
