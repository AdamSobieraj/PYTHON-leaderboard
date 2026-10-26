```
┌──────────┐ 1. upload PDF  ┌──────────────────────────┐
│   USER   │───────────────►│ FastAPI (delivery)       │ auth, walidacja pliku
│(operator)│◄───────────────│ POST   /contracts        │
└──────────┘ contract_id    │ GET    /status, /result  │
   ▲    │      (UUID)       │ POST   /type, /approve   │
   │    │                   │ PATCH  /fields/{name}    │
   │    │                   └────────────┬─────────────┘
   │    │                                │ bootstrap → PipelineContext
   │    │                                ▼
   │    │   ┌────────────────────────────────────────────────────────┐
   │    │   │ CELERY (broker Redis) – cienkie taski → pipeline/stages│
   │    │   │ kolejki: [heavy] [cpu] [llm]                           │
   │    │   │                                                        │
   │    │   │ ══════════════ CZĘŚĆ A ══════════════                  │
   │    │   │ 2. store PDF  {id}/{id}.pdf                            │
   │    │   │        ▼                                               │
   │    │   │ 3. CONVERT   BaseDocumentParser.parse() (BLACKBOX)     │
   │    │   │    List[Document] → documents_to_markdown()            │
   │    │   │    → {id}_markdown.md  + {id}_page_map.json            │
   │    │   │        ▼                                               │
   │    │   │ 4. BUILD_INDEX  chunking + BM25 + embeddingi           │
   │    │   │    → index/chunks.json, index/embeddings.npy           │
   │    │   │        ▼                                               │
   │    │   │ 5. CLASSIFY  agent klasyfikator ◄──────────── EXCEL    │
   │    │   │        │                          (spec: typy + pola)  │
   │    │   │        ├─ pewny ───────────────────┐                   │
   │    │   │        └─ niepewny → needs_user_input                  │
   │    │ ◄─┼──────────────────┘ (user wybiera typ: POST /type)      │
   │    │ ──┼──────────────────────────────────►│                    │
   │    │   │                                   ▼                    │
   │    │   │ ══════════════ CZĘŚĆ B ══════════════                  │
   │    │   │ 6. ORKIESTRATOR (kod) – grupy pól wg kolumny "grupa"   │
   │    │   │        ├──────────────┬──────────────┐                 │
   │    │   │        ▼              ▼              ▼                 │
   │    │   │ 7. EXTRACT_GROUP A  GROUP B  ...  GROUP N (równolegle) │
   │    │   │    retrieval (hybrid RRF, top-k) → LLM → kandydaci     │
   │    │   │        └──────────────┴──────────────┘ (chord)         │
   │    │   │        ▼                                               │
   │    │   │ 8. VALIDATE  cytat↔linie, strona z page_map, format,   │
   │    │   │    aneksy, confidence, statusy                         │
   │    │   │        ▼                                               │
   │    │   │ 9. FINALIZE  zapis {id}.json + status "ready"          │
   │    │   └────────────────────────┬───────────────────────────────┘
   │    │                            │
   │    │ 10. REVIEW: wartość, cytat, strona, confidence
   │    └────────────────────────────┘
   │         user poprawia (PATCH) i zatwierdza (POST /approve)
   │                    │
   └────────────────────┤ wynik submitu (ok/error, ID rekordu)
                        ▼
          ┌──────────────────────────────────┐
          │ 11. SUBMIT_FORM  FormFiller      │
          │     (BLACKBOX → Salesforce)      │
          └──────────────────────────────────┘


══════════ ARCHITEKTURA: pipeline widzi tylko porty ══════════

  pipeline/ agents/ retrieval/ spec/        (cała logika)
                  │  tylko interfejsy
                  ▼
  ports/:  ArtifactStore  Repositories  BaseDocumentParser
           LLMClient  EmbeddingClient  Tracer  FormFiller  SpecSource
                  ▲  implementacje wybiera bootstrap.py (config)
                  │
  adapters/: S3 / InMemory   SQLAlchemy / InMemory   parser(y) / Fake
             Azure OpenAI / FakeLLM   Langfuse / Noop   Mock / Salesforce
             ExcelSpecSource

══════════ WARSTWY PRZEKROJOWE ══════════

  Azure OpenAI (prywatny, UE) ◄── klasyfikator, ekstrakcja, embeddingi
  Langfuse (self-hosted)      ◄── 1 trace na contract_id, maskowanie PII
  Postgres (przez repozytoria)◄── etapy, wersje, audyt, korekty usera
  S3 (przez ArtifactStore)    ◄── PDF, markdown, page_map, indeks, JSON
  Flower / alerty / DLQ       ◄── monitoring Celery
```

## Opis etapów

1. **Upload (API):** waliduje plik (typ, rozmiar, nagłówek `%PDF`), nadaje `contract_id` (UUID), zapisuje rekord z informacją, kto wgrał, i od razu zwraca id. Reszta dzieje się asynchronicznie.
2. **Zapis PDF:** oryginał trafia przez `ArtifactStore` do `{id}/{id}.pdf`. To punkt odniesienia dla całej proweniencji.
3. **Convert:** wywołuje Twój `BaseDocumentParser`, a funkcja `documents_to_markdown` składa z wyniku jeden plik Markdown z markerami stron i mapę stron. Zapisuje `{id}_markdown.md` i `{id}_page_map.json`. Brak numerów stron w metadanych oznacza błąd, nie zgadywanie.
4. **Build index:** dzieli Markdown na chunki (każdy zna swoje linie i strony), liczy embeddingi i indeks BM25 i zapisuje je na S3, żeby każdy worker mógł je odtworzyć. Dla krótkich umów etap jest pomijany.
5. **Classify:** tańszy model ustala typ umowy na podstawie początku dokumentu, nagłówków i listy typów z Excela. Przy niskiej pewności status zmienia się na `needs_user_input`, pipeline się zatrzymuje, a user wybiera typ przez `POST /type`, co uruchamia część B.
6. **Orkiestrator:** czysty kod, bez LLM. Bierze pola dla wybranego typu i dzieli je na grupy (kolumna `grupa`), pilnując limitów równoległości względem TPM/RPM na Azure.
7. **Extract group:** dla każdej grupy równolegle: retrieval hybrydowy dla każdego pola (zapytanie z nazwy, opisu i synonimów), potem LLM dostaje tylko trafione chunki z numerowanymi liniami. Zwraca kandydatów z wartością, numerem linii i dosłownym cytatem albo `not_found`.
8. **Validate:** głównie kod. Sprawdza, czy cytat faktycznie występuje w podanych liniach, wylicza stronę z `page_map`, weryfikuje format (data, kwota, NIP, IBAN), rozstrzyga aneksy i sprzeczności (późniejszy nadpisuje, w razie wątpliwości LLM-sędzia lub `uncertain`) i liczy końcowy confidence.
9. **Finalize:** składa `{id}.json` z wartościami, źródłem (plik, strona, linia, cytat), statusami i wersjami (spec, prompty, pipeline), zapisuje go i ustawia status `ready`.
10. **Review:** user widzi pola z cytatem, stroną i confidence, poprawia wartości (`PATCH`, korekta jest zapisywana jako dane do ewaluacji) i zatwierdza całość (`POST /approve`).
11. **Submit form:** dopiero po zatwierdzeniu `FormFiller` (blackbox, na start mock) wysyła zatwierdzony JSON do formularza lub Salesforce i zwraca `ok/error` oraz ID rekordu.