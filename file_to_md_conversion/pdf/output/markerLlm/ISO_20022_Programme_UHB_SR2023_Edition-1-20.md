<!-- ELEMENT 1 -->
<span id="page-0-0"></span>![](_page_0_Picture_0.jpeg)

Przesłany obraz nie jest schematem technicznym, diagramem przepływu ani modelem danych ISO 20022. Jest to pojedynczy nagłówek tekstowy. Jako ekspert od dokumentacji ISO 20022, analizuję go w kontekście struktury standardów finansowych.

## Cel schematu
Przesłany element pełni funkcję **znacznika strukturalnego (nagłówka)** w dokumencie technicznym. Jego celem jest zasygnalizowanie początku sekcji wstępnej ("Preface"), która w dokumentacji ISO 20022 służy do wprowadzenia czytelnika w zakres dokumentu, wyjaśnienia celu danej specyfikacji wiadomości oraz określenia kontekstu biznesowego dla opisanych w dalszej części standardów.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| Preface | Wstęp / Przedmowa. Sekcja dokumentacji technicznej, która zawiera informacje o celu opracowania, grupie docelowej oraz ogólnych założeniach stosowanych w danej specyfikacji ISO 20022. |

## Logika i relacje
W przesłanym obrazie nie występuje logika procesowa ani przepływ informacji, ponieważ nie jest to diagram funkcjonalny. Z punktu widzenia hierarchii dokumentacji ISO 20022:
1. **Poziom Hierarchiczny:** Jest to element najwyższego poziomu w strukturze rozdziałów (Level 1 Header).
2. **Zależność:** Sekcja ta poprzedza definicje biznesowe (Business Process), modele danych (Data Model) oraz konkretne schematy XML/JSON. Stanowi ona fundament interpretacyjny dla wszystkich kolejnych sekcji technicznych.

## Kluczowe wnioski
- Przesłany obraz nie zawiera informacji o procesach biznesowych, komunikatach ani mapowaniach pól.
- Jest to jedynie element typograficzny wskazujący na początek części wprowadzającej dokumentację.
- Aby przeprowadzić pełną analizę techniczną (np. przepływu wiadomości `pacs` lub `camt`), konieczne jest dostarczenie właściwego diagramu sekwencji, modelu danych lub schematu XML.


![](_page_0_Picture_1.jpeg)

This Cross -Border Payment Reporting plus (CBPR+) User Handbook is intended to document and explain a variety of ISO 20022 payment related topics, as well as provide practical use cases to ensure a common understanding and adoption of ISO 20022 within the payment industry.

The SWIFT FINplus service will support CBPR+ messages on the SWIFT network traditionally associated with correspondent banking (many to -many). These messages may be exchanged either between Agents in the same country or between Agents in different countries.

The use cases focus on a core topics where other relevant messages may also be referred to within the use case, it may also be necessary to consider other documented use cases, in order to capture a wider variation of scenarios.

### Note:

This document jointly developed with the CBPR+ group continues to evolve inline with the Standards

- Release as: CBPR+ continue to develop market practice guidelines for additional message.
- Inaccuracies are identified and corrected.
- Further use cases and/or explanation needs are identified

![](_page_1_Picture_0.jpeg)

# **Change log (since last iteration)**

[Page 2](#page-0-0) Updated – note

[Page 5](#page-0-0) Updated – new messages added to index [Page 6](#page-4-0) Updated – new messages added to index [Page 11](#page-9-0) Updated – correction of Intermediary code Page 33 Updated – new messages and Usage Ids added Page 40 Updated – new pain message added to index

Page 45 Updated – recognition of Payment Initiation relay rulebook Page 107 Updated – recognition of Payment Initiation relay rulebook

Page 122 Updated – additional use cases in the index

Page 126 New –use case Page 134 New – use case

Page 135-182 New – pain.008 message section

Page 184 Update – new messages added to index

Page 204 Update – removed refer to Wait For Settlement Market Practice

Page 351 New – new high level message flow Page 371 Updated – new messages added to index

Page 379-380 New – pacs.003 use cases

Page 400 Updated – additional guidance on ultimate parties on the return

Page 423 Updated – correct to Agent description in Step 7 Page 458-488 New – pacs.010 Margin Collection section Page 489-529 New – pacs.003 Customer Direct Debit section Page 530 Updated – new message added to index Page 674 Updated – removed reference to SR 2023

Page 682 Updated – moved reference to multiple notification, now at an *Item* level

Page 691 Updated – reference to multiple notification item Rule Page 698-716 New – camt.058 Notice to Received Cancellation section

Page 743 Updated - new message added to index

Page 764 Updated - use case id correction

Page 774-795 New – Customer Cancellation Request section

Page 823-883 New – Cheque message sections Page 880 Updated - use case id correction

![](_page_1_Picture_20.jpeg)




The following icons dignify changes to slide from the previous itineration. Updates to text on a slide are captured in **gold**.

![](_page_1_Picture_22.jpeg)

![](_page_1_Picture_24.jpeg)

New slide since last iteration **U** Slide updated since last iteration

## Legend

![](_page_2_Picture_1.jpeg)

![](_page_2_Picture_2.jpeg)

![](_page_2_Picture_3.jpeg)

## Cel schematu
Celem tego schematu jest zdefiniowanie kluczowych ról uczestników w procesie rozliczeniowym i clearingowym w ramach standardu ISO 20022. Ilustruje on dwa podstawowe byty finansowe, które są niezbędne do przeprowadzenia każdej transakcji płatniczej: stronę wysyłającą środki oraz stronę je odbierającą w kontekście komunikatów typu `pacs`.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **pacs** | Skrót od *Payments Clearing and Settlement*. Jest to kategoria komunikatów ISO 20022 wykorzystywanych do rozliczeń międzybankowych (interbank), służących do przesyłania instrukcji płatniczych i potwierdzeń między instytucjami finansowymi. |
| **Debtor** | Dłużnik / Płatnik. Podmiot, który jest zobowiązany do zapłaty lub inicjuje transfer środków. W przepływie pieniężnym jest to strona, z której rachunku środki zostają pobrane. |
| **Creditor** | Wierzyciel / Odbiorca. Podmiot, który ma prawo otrzymać płatność. W przepływie pieniężnym jest to strona docelowa, na której rachunku środki zostaną zaksięgowane. |

## Logika i relacje
Schemat przedstawia fundamentalną relację finansową typu **nadawca $\rightarrow$ odbiorca**. 

Logika biznesowa opiera się na przepływie wartości (pieniędzy) oraz informacji:
1. **Kierunek transferu:** Środki finansowe przemieszczają się od `pacs Debtor` do `pacs Creditor`.
2. **Kontekst komunikacyjny:** Przedrostek `pacs` wskazuje, że relacja ta nie dotyczy bezpośredniej instrukcji klienta do banku (co byłoby domeną komunikatów `pain`), lecz operacji na poziomie rozliczeniowym między bankami/agentami finansowymi.
3. **Zależność:** Aby transakcja była poprawna w standardzie ISO 20022, oba te role muszą być jednoznacznie zidentyfikowane (np. poprzez kody BIC lub numery rachunków IBAN),


![](_page_2_Picture_4.jpeg)

![](_page_2_Picture_5.jpeg)

![](_page_2_Picture_6.jpeg)

![](_page_2_Picture_7.jpeg)

## Cel schematu
Schemat ten służy do zdefiniowania i symbolicznego przedstawienia roli **Agenta** w ekosystemie standardu ISO 20022. Jego celem jest wskazanie podmiotu, który występuje w charakterze pośrednika lub wykonawcy instrukcji finansowych, działając w imieniu innej strony (klienta lub innej instytucji) w celu realizacji transakcji lub wymiany komunikatów.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| Agent | Podmiot (zazwyczaj instytucja finansowa, np. bank), który działa w imieniu innej strony (tzw. mocodawcy/klienta) w celu ułatwienia realizacji transakcji finansowej lub przekazania komunikatu zgodnie ze standardem ISO 20022. |

## Logika i relacje
W logice biznesowej ISO 20022, Agent nie jest jedynie punktem końcowym, lecz kluczowym ogniwem w łańcuchu wartości płatności. Relacje i przepływy z nim związane wyglądają następująco:

1.  **Relacja Zleceniodawca $\rightarrow$ Agent:** Klient (osoba fizyczna lub firma) przekazuje instrukcję płatniczą swojemu Agentowi (np. bankowi prowadzącemu rachunek).
2.  **Rola Operacyjna:** Agent odpowiada za walidację komunikatu, sprawdzenie zgodności z regułami biznesowymi oraz nadanie mu odpowiedniego formatu XML zgodnie ze schematami ISO 20022.
3.  **Relacja Agent $\rightarrow$ Agent (Interbank):** W przypadku płatności transgranicznych, Agent może przekazać komunikat do innego Agenta (np. banku korespondenta), który działa jako kolejny pośrednik w procesie routingu środków.
4.  **Relacja Agent $\rightarrow$ Odbiorca:** Ostatni Agent w łańcuchu dostarcza środki i informację o płatności do odbiorcy końcowego (Beneficiary).

## Kluczowe wnios


Agent processing legacy format during a coexistence period

![](_page_2_Picture_9.jpeg)

Przedstawiony obraz nie jest schematem procesowym ani diagramem technicznym, lecz **identyfikatorem domeny biznesowej** w kontekście standardu ISO 20022. W dokumentacji technicznej tego standardu takie oznaczenia służą do kategoryzacji komunikatów i ról uczestników rynku.

## Cel schematu
Celem tego oznaczenia jest zdefiniowanie i wyodrębnienie obszaru **Infrastruktury Rynkowej (Market Infrastructure)** jako kluczowego ogniwa w ekosystemie finansowym. Komunikuje ono, że analizowane elementy (np. konkretne wiadomości XML lub procesy) dotyczą systemów centralnych, które umożliwiają bezpieczne i efektywne rozliczanie transakcji między uczestnikami rynku, a nie bezpośrednich relacji między dwoma bankami komercyjnymi.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Market Infrastructure** | Infrastruktura Rynkowa – zestaw systemów i instytucji (takich jak systemy płatności RTGS, centralne depozyty papierów wartościowych CSD czy izby rozliczeniowe CCP), które zapewniają stabilność finansową poprzez zarządzanie procesami kompensacji (clearing) i rozliczania (settlement). |

## Logika i relacje
W logice biznesowej ISO 20022, "Market Infrastructure" pełni rolę **centralnego węzła (hubu)**. Relacje między elementami w tej domenie wyglądają następująco:

1.  **Uczestnicy $\rightarrow$ Infrastruktura Rynkowa:** Instytucje finansowe (banki) przesyłają komunikaty do infrastruktury rynkowej, aby zainicjować transfer środków lub aktywów.
2.  **Infrastruktura Rynkowa $\rightarrow$ Finalizacja:** Systemy te weryfikują poprawność transakcji i dokonują ich ostatecznego rozliczenia (settlement), co gwarantuje nieodwołalność operacji.
3.  **Zależność systemowa:** Infrastruktura rynkowa stanowi "szkielet", na którym opierają się wszystkie pozostałe usługi finansowe; bez niej niemożliwe


Exceptional circumstance

![](_page_2_Picture_11.jpeg)

Exception & Investigation Case Assigner

![](_page_2_Picture_13.jpeg)

![](_page_2_Picture_14.jpeg)

![](_page_2_Picture_15.jpeg)

![](_page_2_Picture_16.jpeg)

![](_page_2_Picture_17.jpeg)

![](_page_2_Picture_18.jpeg)

![](_page_2_Figure_19.jpeg)

![](_page_2_Figure_20.jpeg)

Na podstawie dostarczonego fragmentu grafiki, który odnosi się do standardów SWIFT i ISO 20022 w kontekście płatności transgranicznych, poniżej znajduje się analiza biznesowa.

## Cel schematu
Celem tego elementu jest zilustrowanie koncepcji **widoczności i śledzenia płatności w czasie rzeczywistym** w ramach globalnej sieci bankowej. Schemat komunikuje istnienie scentralizowanej infrastruktury (reprezentowanej przez chmurę), która pozwala instytucjom finansowym na monitorowanie statusu przelewu międzynarodowego na każdym etapie jego drogi – od banku nadawcy, przez banki pośredniczące, aż do banku odbiorcy. Rozwiązuje on biznesowy problem "czarnej dziury" w płatnościach cross-border, gdzie nadawca nie wiedział, gdzie dokładnie znajdują się środki i jaki jest aktualny status transakcji.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **gpi** | **Global Payments Innovation**. Jest to zestaw reguł i standardów opracowanych przez SWIFT, mających na celu przyspieszenie płatności transgranicznych, zwiększenie ich przejrzystości oraz zapewnienie pełnej śledzalności. W kontekście ISO 20022, gpi wykorzystuje ustandaryzowane komunikaty do przesyłania informacji o statusie płatności. |
| **gpi Tracker** | Scentralizowane narzędzie/usługa monitorowania, która pozwala bankom (a za ich pośrednictwem klientom końcowym) śledzić w czasie rzeczywistym drogę przelewu. Umożliwia sprawdzenie, który bank obecnie przetwarza płatność, czy zostały pobrane opłaty przez banki pośredniczące oraz kiedy środki dotarły do odbiorcy. |

## Logika i relacje
Logika biznesowa przedstawiona na schemacie opiera się na modelu **centralnego rejestru statusów**:

1.  **Identyfikator UETR:** Podstawą działania gpi Tracker jest unikalny identyfikator transakcji (Unique End-to-End Transaction Reference - UETR), który towarzyszy płatności w standardzie ISO 20022 na każdym etapie jej przepływu.
2.  **Przepływ informacji:** Każdy bank uczestniczący w procesie gpi ma obowią


![](_page_2_Figure_21.jpeg)

![](_page_2_Picture_22.jpeg)

![](_page_2_Picture_23.jpeg)

![](_page_2_Picture_24.jpeg)

![](_page_2_Picture_25.jpeg)

![](_page_2_Picture_26.jpeg)

![](_page_2_Picture_27.jpeg)

![](_page_2_Picture_28.jpeg)

![](_page_2_Picture_29.jpeg)

![](_page_2_Figure_30.jpeg)

![](_page_2_Figure_31.jpeg)

![](_page_2_Picture_32.jpeg)

![](_page_2_Picture_33.jpeg)

Przesłany obraz nie jest schematem technicznym, diagramem przepływu danych ani modelem logicznym w rozumieniu specyfikacji ISO 20022 (takich jak modele koncepcyjne czy definicje wiadomości XML). Jest to **symbol/znacznik (badge)** stosowany w dokumentacji technicznej.

Poniżej znajduje się analiza tego elementu z perspektywy eksperta ds. dokumentacji ISO 20022.

## Cel schematu
Celem tego elementu jest pełnienie funkcji **wskaźnika jakościowego i normatywnego**. W obszernych dokumentacjach technicznych (takich jak *Implementation Guides* czy *Usage Guidelines* dla standardu ISO 20022), taki znacznik służy do szybkiej identyfikacji rozwiązań, które są uznawane za optymalne. Informuje on implementatora (programistę, analityka biznesowego), że opisana obok metoda, sposób mapowania pól lub struktura wiadomości jest zgodna z najwyższymi standardami rynkowymi i zalecanymi praktykami organizacji nadzorujących standard.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| Best practice | "Najlepsza praktyka" – w kontekście ISO 20022 oznacza to sposób implementacji elementu wiadomości (np. `pacs


![](_page_2_Picture_34.jpeg)

3

![](_page_3_Picture_0.jpeg)

# **Table of contents**

- **1. [Introduction to ISO 20022](#page-5-0)**
- **2. Business Application Header**
- **3. Payment Initiation (pain)**

```
pain.001 - Interbank Customer Credit Transfer Initiation
pain.002 - Interbank Customer Payment Status Report
pain.008 – Customer Direct Debit Initiation
```

**4. Payment, Clearing and Settlement (pacs) messages**

```
pacs.002 – Financial Institution to Financial Institution Payment Status Report 
pacs.004 – Payment Return
pacs.003 – Financial Institution to Financial Institution Customer Direct Debit
pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer 
pacs.009 (core) - Financial Institution Credit Transfer 
pacs.009 (cov) - Financial Institution 'Cover' Credit Transfer
pacs.009 (adv) – Financial Institution 'Advice' Credit Transfer 
pacs.010 – Financial Institution Direct Debit
```

![](_page_3_Picture_8.jpeg)

![](_page_4_Picture_0.jpeg)

# <span id="page-4-0"></span>**Table of contents (continued)**

**5. Cash Management Reporting (camt) messages**

**camt.052 - Bank to Customer Account Report**

**camt.053 - Bank to Customer Statement**

**camt.054 - Bank to Customer Debit Credit Notification**

**camt.057 – Notification to Receive**

**camt.058 – Notification to Receive Cancelation Advice**  new for SR2023

**6. Cash Management Exception & Investigation (camt) messages**

**camt.029 - Resolution of Investigation**

**camt.055 – Customer Payment Cancelation Request**

**camt.056 - FI to FI Cancellation Request**

#### **7. Cheques**

**camt.107 – Cheque Presentment Notification**

**camt.108 – Cheque Cancellation or Stop Notification**

**camt.109 – Cheque Cancellation or Stop Report**

![](_page_4_Picture_16.jpeg)

# <span id="page-5-0"></span>**Introduction to ISO 20022**

![](_page_5_Picture_1.jpeg)

# **Introduction to ISO 20022**

ISO 20022 introduces a fundamental change to the traditional language used by the payments industry for several decades. It also describes participants (i.e., parties) to a business transaction differently based upon the business domain (area) being described, in a similar way you may describe a person as a colleague, parent or sibling depending upon the context you wish to describe them. This section is designed to capture and explain some of the differences.

![](_page_6_Picture_2.jpeg)

# **Introduction to ISO 20022 – Business Domains**

## **Domains**

### **Payment and Cash Management**

Securities

Trade Services

Foreign Exchange

Card Payment

## **Message Definitions**

**acmt** Account Management

**auth** Authorities

**camt** Cash Management

**pacs** Payment Clearing and Settlement

**pain** Payment Initiation

**remt** Payment Remittance Advice

## **Message Sets**

camt.052 Bank to Customer Account Report

camt.053 Bank to Customer Statement

camt.054 Bank to Customer Debit Credit Notification

camt.056 FI to FI Payment Cancellation Request

camt.057 Notification to Receive

pacs.002 FI to FI Payment Status Report

pacs.004 Payment Return

pacs.008 FI to FI Customer Credit Transfer

pacs.009 Financial Institution Credit Transfer

pain.001 Customer Credit Transfer initiation

pain.002 Customer Payment Status Report

pain.012 Creditor Payment Activation Request

![](_page_7_Picture_27.jpeg)

## Cel schematu
Schemat ilustruje hierarchiczną architekturę standardu ISO 20022. Jego celem jest przedstawienie modelu budowy komunikatów finansowych, który opiera się na zasadzie modularności i reużywalności danych. Ilustruje on przejście od najbardziej ogólnych definicji biznesowych (fundamentu), poprzez konkretne struktury wiadomości, aż po zestawy komunikatów realizujące pełne procesy biznesowe.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Domain** | Najniższy poziom architektury (warstwa bazowa). Zawiera wspólne komponenty danych i definicje pojęć biznesowych, które są identyczne dla wszystkich komunikatów w standardzie. Zapewnia to spójność semantyczną (np. że "data" lub "kwota" jest definiowana tak samo w każdym komunikacie). |
| **Message Definition** | Poziom średni, w którym z elementów warstwy Domain budowane są konkretne schematy wiadomości. Jest to definicja struktury pojedynczego komunikatu (np. `pacs.008` dla przelewu klienta), określająca, jakie pola są wymagane i opcjonalne dla danego przypadku użycia. |
| **Message Sets** | Najwyższy poziom organizacji. Są to grupy powiązanych ze sobą definicji wiadomości, które wspólnie obsługują kompletny proces biznesowy (end-to-end). Zestaw ten obejmuje wszystkie komunikaty niezbędne do zainicjowania, przetworzenia i rozliczenia danej operacji finansowej. |

## Logika i relacje
Schemat przedstawia relację zależności typu "od ogółu do szczegółu" (bottom-up):

1. **Zależność Domain $\rightarrow$ Message Definition**: Definicja wiadomości nie istnieje w próżni – jest ona konstrukcją złożoną z klocków dostarczonych przez warstwę *Domain*.


ISO 20022 catalogue messages hierarchically beginning with a Business Domain, contain a various sets of Message Definitions, which in turn contain a variety of Message Sets.

### for example:

- ➢ Payment and Cash Management
  - ➢ Payments Clearing and Settlement
    - ➢ FI to FI Customer Credit Transfer (pacs.008)

![](_page_7_Picture_33.jpeg)

# **Introduction to ISO 20022 - Message Identifier**

![](_page_8_Figure_1.jpeg)

## Cel schematu
Celem tego schematu jest zdefiniowanie **standardu nazewnictwa i struktury identyfikatora wiadomości w standardzie ISO 20022**. Ilustruje on precyzyjną składnię (syntaktykę), według której budowane są kody identyfikacyjne komunikatów finansowych. Pozwala to na jednoznaczną klasyfikację każdej wiadomości w globalnym ekosystemie płatności, umożliwiając systemom informatycznym automatyczne rozpoznanie przeznaczenia komunikatu, jego wersji oraz specyfiki biznesowej.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **4


![](_page_8_Figure_2.jpeg)

## Cel schematu
Celem tego schematu jest wyjaśnienie struktury i składni identyfikatora wiadomości w standardzie ISO 20022. Ilustruje on, w jaki sposób sformalizowany ciąg znaków (w tym przypadku `pacs.008.001.08`) koduje informacje o przeznaczeniu biznesowym, typie operacji, wariancie oraz wersji technicznej dokumentu. Pozwala to systemom informatycznym na jednoznaczne rozpoznanie i poprawną interpretację otrzymanego komunikatu finansowego.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **pacs** | Skrót od *Payments Clearing and Settlement*. Jest to obszar biznesowy (Business Area) odpowiedzialny za rozliczenia i clearing płatności między instytucjami finansowymi. |
| **008** | Identyfikator konkretnego typu wiadomości w ramach danego obszaru. W tym przypadku oznacza *FI To FI Customer Credit Transfer* (Przelew kredytowy klienta między instytucjami finansowymi). |
| **001** | Numer wariantu (*Variant*). Określa on konkretną wersję struktury wiadomości, która może być dostosowana do specyficznych wymagań rynkowych lub prawnych przy zachowaniu tego samego celu biznesowego. |
| **08** | Numer wersji (*Version*). Wskazuje na iterację techniczną schematu. Zmiany w numerze wersji oznaczają aktualizacje w definicji pól, walidacjach lub strukturze XML. |
| **pacs.008.001.08** | Pełny identyfikator wiadomości ISO 20022, który unikalnie definiuje standard komunikatu. |

## Logika i relacje
Schemat przedstawia hierarchiczną strukturę nazewnictwa, gdzie każdy segment identyfikatora zawęża zakres definicji wiadomości:

1. **Poziom Obszaru (Business Area):** Najbardziej ogólny poziom (`pacs`). Określa on kontekst biznesowy całej grupy komunikatów.
2. **Poziom Typu Wiadomości (Message Identifier):** Wewnątrz obszaru `pacs` wybierany jest konkretny proces biznesowy (`008`), czyli w tym przypadku przelew międzybankowy dla klienta.
3. **Poziom Wariantu (Variant):** Dla danego


![](_page_8_Picture_3.jpeg)

# <span id="page-9-0"></span>**What is changing? Party Identifiers**

**Legend:**

**ISO 20022**

![](_page_9_Picture_3.jpeg)

![](_page_9_Picture_4.jpeg)

**New parties introduced in ISO 20022**

![](_page_9_Picture_6.jpeg)

**:XX FIN MT format equivalent**

![](_page_9_Figure_8.jpeg)




![](_page_9_Picture_9.jpeg)

## **SWIFT FINplus Message structure**

The diagram attempts to explain the construct of an ISO 20022 message sent across the SWIFT network using the **FINplus** service (which is designated to support various ISO 20022 business domains on SWIFT Interact)

Within the CBPR+ User Handbook the predominant focus is on the **Request Payload,** as this is where the business information is contained. However, it is worth noting that a network provider will have additional containers around the Request Payload to perform functionality on its network. This diagram presents the additional containers on the SWIFT network such as the Request Header often referred to as the Technical Header of the message.

![](_page_10_Figure_3.jpeg)

## Cel schematu
Celem schematu jest przedstawienie architektury enkapsulacji (zagnieżdżania) wiadomości finansowych w standardzie ISO 20022 podczas ich przesyłania przez sieć SWIFTNet. Ilustruje on relację między warstwą transportową (techniczną), a warstwą biznesową, pokazując, jak konkretna wiadomość biznesowa jest "opakowana" w nagłówki niezbędne do jej bezpiecznego i prawidłowego dostarczenia od nadawcy do odbiorcy.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Exchange Request** | Najwyższy poziom struktury; całkowity pakiet wymiany danych przesyłany w sieci. |
| **Request** | Główny obiekt żądania, zawierający dane techniczne i merytoryczne. |
| **SWIFTNet Headers** | Zbiór nagłówków transportowych SWIFT, które odpowiadają za routing i obsługę techniczną wiadomości w sieci. |
| **RequestHeader** | Nagłówek żądania zawierający metadane niezbędne dla infrastruktury sieciowej do zidentyfikowania celu i typu przesyłki. |
| **RequestPayload** | "Ładunek" żądania; kontener, w którym znajduje się właściwa wiadomość biznesowa. |
| **Crypto** | Warstwa kryptograficzna zapewniająca integralność, autentyczność i poufność danych (szyfrowanie/podpis cyfrowy). |
| **Envelope** | "Koperta" – logiczny kontener oddzielający warstwę transportową od treści biznesowej. |
| **Business Message** | Kompletna wiadomość biznesowa, składająca się z nagłówka aplikacji oraz dokumentu biznesowego. |
| **Application Header / `<AppHdr>`** | ISO 20022 Business Application


![](_page_10_Picture_4.jpeg)

# **XML Elements**

#### **XML Elements**

An XML instance or document contains data in elements and nested elements (elements which contain other elements) corresponding to the hierarchy imposed by the XML schema. In the CBPR+ Usage Guidelines we often refer to the element hierarchy by levels (to understand the nested relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example in a pacs.008 Customer Credit Transfer the *Interbank Settlement Date* is a sub-element (Level 2) of the *Credit Transfer Transaction Information* element (Level 1).

#### **Naming conventions**

An XML element is named according to the following rules:

- The name can contain letters, numbers, and other characters, but must not start with a number or punctuation mark.
- The name must not start with XML, xml, or Xml.
- The name must not contain any spaces.

#### **MX naming conventions**

There are some generic naming rules that apply to most items in the database.

- The names of all items in the database use the upper CamelCase convention, as follows:
  - Each word starts with a capital letter.
  - There are no white spaces between words.
- A name may be made up of multiple words, each consisting of alphanumeric characters.
- Words use British English vocabulary.
- All names must start with an alphabetic character.
- All characters that follow the first characters must be letters or numbers.

**Example of a Street Name element:** <StrtNm>Oxford Street</StrtNm>

#### **MX message element multiplicity (occurrences)**

An MX message element specifies its cardinality (number of elements in a set) using minimum (min) & maximum (max) to describe the occurrences.

![](_page_11_Picture_20.jpeg)

## Cel schematu
Celem tego schematu jest zdefiniowanie zasad **kardynalności (multiplicity)** elementów w strukturze wiadomości ISO 20022. Ilustruje on, w jaki sposób wartości minimalne (`Min`) i maksymalne (`Max`) określają obowiązkowość oraz dopuszczalną liczbę wystąpień danego pola danych (elementu) w komunikacie XML. Jest to kluczowy element walidacji technicznej wiadomości finansowych, który pozwala systemom informatycznym rozstrzygnąć, czy wiadomość jest poprawna pod kątem składniowym i biznesowym.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Element Multiplicity** | Wielokrotność elementu; określa reguły dotyczące liczby wystąpień danego pola w strukturze dokumentu. |
| **Min** | Minimalna liczba wystąpień elementu wymagana, aby wiadomość została uznana za poprawną (walidacyjną). |
| **Max** | Maksymalna dopuszczalna liczba wystąpień danego elementu w wiadomości. |
| **Required element** | Element obowiązkowy; musi wystąpić dokładnie jeden raz. Brak tego pola lub jego powielenie spowoduje błąd walidacji. |
| **Optional element** | Element opcjonalny; może nie wystąpić wcale (0) lub wystąpić maksymalnie jeden raz (1). |
| **Unlimited element occurrences** | Nieograniczona liczba wystąpień; element może być całkowicie pominięty lub pojawić się dowolną liczbę razy (np. lista odbiorców, zestaw transakcji). |
| **\*** (symbol gwiazdki) | W kontekście `Max`, symbol ten oznacza wartość "nieograniczoną" (unbounded). |

## Logika i relacje
Logika schematu opiera się na przedziale wartości $[Min, Max]$, który definiuje rygor biznesowy dla każdego pola danych:

1.  **Relacja 1:1 (Obowiązkowość)** $\rightarrow$ Gdy `Min=1` i `Max=1`, system wymusza obecność elementu. Jest to krytyczna informacja biznesowa, której brak uniemożliwia przetworzenie instrukcji (np. numer rachunku płatnika).
2.  **Relacja 0:1 (Opcjonalność)** $\rightarrow$ Gdy `Min=0` i `Max=1`, element jest traktowany jako dodatkowy. Jego obecność zależy od konkretnego przypadku biznesowego, ale jeśli się pojawi, nie może być powielony.
3.  **Relacja 0:\* (Kolekcja/Lista)** $\rightarrow$ Gdy `Min=0` i `Max=*`, element pełni rolę listy lub tablicy. Pozwala to na przesyłanie zmiennej liczby danych w ramach jednego bloku (np. wiele załączników do jednej wiadomości).

## Kluczowe wnioski
- Schemat stanowi fundament dla **walidacji XSD**


# **XML Elements (continued)**

#### **Empty XML Elements**

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element.

A common example of this is in payment message is Financial Institution.

| ✓                                          | 1 | 1 |
|--------------------------------------------|---|---|
| > o BICFI                                  | 0 | 1 |
| >    Clearing System Member Identification | 0 | 1 |
| • LEI                                      | 0 | 1 |
| <ul> <li>Name</li> </ul>                   | 0 | 1 |
| > o Postal Address                         | 0 | 1 |

Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e., <FinInstnId></FinInstnId>

In the **FINplus** service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where business data should be provided within a nested element, it is provided.

![](_page_12_Picture_7.jpeg)

# **XML Elements within CBPR+ User Hand Book**

MyStandards describes the element's context by its path whereby each element is divided by a forward slash (/) For example the pacs.008 Town Name within the Debtor Postal Address is described as /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/PstlAdr/TwnNm

Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing the element in an XML naming convention.

For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment Identification is an element below Credit Transfer Transaction Information.

*Credit Transfer Transaction Info' Payment Identification*

In this way the CBPR+ User Hand Book uses three main icon to explain the relationships between element, by display the icon after the element name.

To visualise an element which has nested elements beneath it

To visualise an element which has a choice associated with it i.e., a Code where a choice of which code can be determined

To visualise an element which is nested and has a choice associated with it. For example, an Identification where a choice must be made between an Organisation Identification and a Private Identification element which is nested, but where both cannot be used together.

![](_page_13_Picture_9.jpeg)

# **The CBPR+ group has published all its usage guidelines in MyStandards**

![](_page_14_Picture_1.jpeg)

## Cel schematu
Prezentowany schemat jest mapą ekosystemu wdrożeniowego **CBPR+ (Cross-Border Payments and Reporting Plus)**. Jego celem jest dostarczenie instytucjom finansowym kompletnego zestawu narzędzi, wytycznych i dokumentacji niezbędnych do przejścia z legacy standardów wiadomości (MT) na nowoczesny standard **ISO 20022 (MX)** w obszarze płatności transgranicznych i raportowania gotówkowego. Schemat ilustruje ścieżkę od teoretycznych wytycznych, przez techniczne mapowanie danych, aż po praktyczną walidację za pomocą próbek wiadomości.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **CBPR+** (Cross-Border Payments and Reporting Plus) | Specyficzne wytyczne Swift, które definiują, w jaki sposób standard ISO 20022 jest stosowany w płatnościach transgranicznych i raportowaniu gotówkowym. |
| **ISO 20022** | Globalny standard wymiany danych finansowych oparty na XML, zapewniający większą strukturę i bogactwo informacji niż starsze standardy. |
| **MT (Message Text)** | Legacy standard wiadomości Swift (format tekstowy), który jest zastępowany przez format MX. |
| **MX** | Nowoczesny format wiadomości oparty na standardzie ISO 20022 (XML). |
| **CBPR+ Usage Guidelines and Readiness Portal** | Portal zawierający szczegółowe zasady stosowania standardu oraz narzędzia do oceny gotowości instytucji do migracji. |
| **CBPR+ Translation Portal** | Narzędzie wspierające proces tłumaczenia wiadomości między formatem MT a MX (interoperacyjność). |
| **CBPR+ user handbook** | Podręcz


**<https://www2.swift.com/mystandards/#/c/cbpr/landing>**

![](_page_14_Picture_3.jpeg)

# **Message Usage Guideline – Additional Information and principals**

![](_page_15_Figure_1.jpeg)

## Cel schematu
Celem przedstawionego zrzutu ekranu jest zaprezentowanie sposobu dostępu do **Usage Guidelines** (Wytycznych Użytkowania) w ramach platformy MyStandards dla standardu CBPR+. Schemat ilustruje, w jaki sposób ogólny standard ISO 20022 zostaje doprecyzowany przez konkretne reguły biznesowe (tzw. "Principles"), które muszą być zastosowane przez instytucje finansowe, aby zapewnić interoperacyjność płatności transgranicznych.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **CBPR+** | Cross Border Payments and Reporting Plus – zestaw wspólnych wytycznych dla banków w celu ujednolicenia wdrażania standardu ISO 20022 w płatnościach transgranicznych. |
| **pacs.008.001.08** | Identyfikator konkretnego typu wiadomości ISO 20022: *Financial Institution to Financial Institution Customer Credit Transfer* (Przelew klienta między instytucjami finansowymi). |
| **FIToFICustomerCreditTransfer** | Pełna nazwa procesu biznesowego: Przelew środków od klienta realizowany pomiędzy dwiema instytucjami finansowymi. |
| **ISO 20022 Portfolio November 2022 Release 2.0** | Konkretna wersja zbioru standardów i wytycznych wydana w listopadzie 2022 roku. |
| **MX** | Format wiadomości oparty na XML, charakterystyczny dla standardu ISO


![](_page_15_Picture_2.jpeg)

# **Rules**

Traditionally in the Legacy FIN standard rules related to a message were described as either *Network Validation Rules* – those validated by the network, or *Usage rules* – rules not validated by the network. FIN also has the concept of *Usage Guidelines* – guideline to recommend a best practice.

In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated Usage Guideline (e.g. CBPR plus)

Within CBPR+ Usage Guideline specification the rules dedicate to CBPR+ are often described as:

**Formal Rules** which are validated on the network, these are identified by the word **Rule** appended to the rule description. For example: *Rule "CBPR\_Party\_Name\_Any\_BIC\_FormalRule"*

**Textual Rules** which are not validated on the network, these are identified by with the word **TextualRule** appended to the rule description. For example: *Rule "CBPR\_Agent\_Option\_1\_TextualRule"*

**Guideline Rules** which provide recommended best practice, these are identified by the word **Guideline** appended to the rule description. For example: *Rule "CBPR\_Purpose\_Guideline"*

Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a **CrossElementSimpleRule** and a **CrossElementComplexRule**

![](_page_16_Picture_8.jpeg)

## **Usage Identifier – Format**

![](_page_17_Figure_1.jpeg)

## Cel schematu
Celem tego schematu jest zdefiniowanie rygorystycznej struktury składniowej (syntaktyki) dla identyfikatora lub kodu referencyjnego stosowanego w standardzie ISO 20022. Schemat ten określa sposób budowania ustandaryzowanego ciągu znaków, który ma zapewnić interoperacyjność między różnymi instytucjami finansowymi. Gwarantuje on, że każdy element kodu (emitent, kontekst biznesowy i wersja) znajduje się w określonym miejscu i nie przekracza limitów długości, co pozwala na automatyczne parsowanie danych przez systemy informatyczne.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| `<Short issuer organisation>` (A) | Skrócony identyfikator organizacji, która wydała dany kod lub zdefiniowała standard (np. kod banku, organizacji regulacyjnej). Długość: 1-10 znaków. |
| `.` (kropka / separator) | Znacznik oddzielający poszczególne segmenty logiczne ciągu znaków. Zajmuje dokładnie 1 znak. |
| `<Business context>` (B, C, D...) | Definicja obszaru biznesowego lub konkretnego procesu, do którego odnosi się kod. Może występować jednokrotnie lub wielokrotnie w celu doprecyzowania hierarchii. Długość każdego segmentu: 1-10 znaków. |
| `{.<Business context>} n times` | Wskazanie na opcjonalną, powtarzalną strukturę. Pozwala na dodanie wielu poziomów kontekstu biznesowego (np. Kontekst Główny $\rightarrow$ Podkontekst $\rightarrow$ Szczegół), gdzie `n` oznacza liczbę powtórzeń. |
| `<version>` (E) | Numer wersji schematu lub kodu, umożliwiający śledzenie zmian w czasie i zapewnienie kompatybilności wstecznej. Długość: dokładnie 2 znaki. |
| `1-10 chars` | Limit długości dla poszczególnych segmentów tekstowych (minimum 1, maksimum 10 znaków). |
| `2 chars` | Ścisły wymóg długości dla pola wersji. |
| `Total max 35 char` | Całkowity limit długości całego sformatowanego ciągu znaków, który nie może przekroczyć 35 znaków. |

## Logika i relacje
Schemat przedstawia hierarchiczną strukturę budowania identyfikatora od ogółu do szczegółu:

1.  **Identyfik


- Type: **String**
- Max allowed size: **35 characters**
- Structure:
  - o Must contain minimum **A & B**, **optionally followed by 1 or more additional business context elements (C, D, …).**
  - o Always **ends** with **version element E** (format "nn", e.g., "01")
  - o Each element is separated by a period "."
  - o Length of **each** text element **can vary** up to **max 10** characters. Total length, including periods, cannot exceed 35 chars.
  - o Consistency enforced by lightweight SWIFT review/registration: E.g., "ecb" to represent the ECB, not "eucb"
  - o **Lowercase** alphanumerical characters only

![](_page_17_Picture_11.jpeg)




In CBPR+ the Usage Identifier is captured within the *Business Application Header*, *Business Service* element. More detail can be found in the dedicated Business Application Header chapter of this document,

![](_page_17_Picture_13.jpeg)

# **ISO 20022 External Code Lists**

![](_page_18_Picture_1.jpeg)

Jako ekspert od dokumentacji technicznej ISO 20022, muszę zaznaczyć na wstępie, że przesłany obraz nie jest szczegółowym schematem technicznym (takim jak diagram sekwencji UML czy model danych), lecz **ikoną symboliczną**. W kontekście standardu ISO 20022, ikona ta reprezentuje koncepcję **interoperacyjności i cyfryzacji danych finansowych**.

Poniżej znajduje się analiza biznesowa tego symbolu w odniesieniu do ekosystemu ISO 20022.

## Cel schematu
Celem tego schematu jest zilustrowanie procesu **integracji ustrukturyzowanych danych z systemami komunikacyjnymi**. W świecie ISO 20022 obrazuje on przejście od surowych informacji biznesowych (reprezentowanych przez wykres) do ich technicznej transmisji za pomocą ustandaryzowanego "interfejsu" (reprezentowanego przez kabel/wtyczkę). Ilustruje problem tzw. *data richness* – czyli zdolność standardu do przenoszenia bogatych, precyzyjnych danych w sposób zautomatyzowany i kompatybilny między różnymi instytucjami finansowymi.

## Kluczowe koncepcje

Ponieważ schemat nie zawiera tekstu, analiza opiera się na symbolice technicznej stosowanej w dokumentacji systemów płatniczych:

| Pojęcie/Symbol | Wyjaśnienie biznesowe w kontekście ISO 20022 |
|----------------|--------------------------------------------------|
| **Słupki wykresu (Data)** | Reprezentują ustrukturyzowane dane finansowe. W ISO 20022 oznacza to przejście z formatów tekstowych (np. MT) na bogate schematy XML, które pozwalają na dokładniejszą analitykę i raportowanie


Many ISO 20022 message use data elements represented by codes. Such codes are often externalised from the message itself, enabling maintenance of the code list on a quarterly basis without requiring a new message version.

Some data element may also be embedded in the message.

example of Charge Bearer in pacs.008 v8 which uses embedded codes

![](_page_18_Picture_5.jpeg)

## Cel schematu
Celem tego schematu jest zdefiniowanie elementu `Charge Bearer` w standardzie ISO 20022, który określa **podział kosztów i prowizji** związanych z realizacją transakcji płatniczej. Schemat ten służy do jednoznacznego wskazania, która ze stron uczestniczących w przelewie (zleceniodawca, zleceniobiorca czy obie strony) ponosi opłaty bankowe, co eliminuje nieporozumienia między instytucjami finansowymi w procesie rozliczeniowym.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Charge Bearer** | Podmiot ponoszący koszty transakcji. Jest to element nadrzędny, który definiuje odpowiedzialność za opłaty bankowe. |
| **Borne By Debtor [DEBT]** | Model kosztowy "OUR". Wszystkie opłaty za przelew są pokrywane przez dłużnika (zleceniodawcę). Odbiorca otrzymuje pełną kwotę. |
| **Borne By Creditor [CRED]** | Model kosztowy "BEN". Wszystkie opłaty są ponoszone przez wierzyciela (zleceniobiorcę). Opłaty są potrącane z kwoty przelewu przed jej zaksięgowaniem. |
| **Shared [SHAR]** | Model kosztowy "SHA". Koszty są dzielone: dłużnik płaci opłaty swojemu bankowi, a wierzyciel opłaty bankom pośredniczącym i swojemu bankowi. |
| **Following Service Level [SLEV]** | Wskazuje, że podział kosztów nie jest zdefiniowany sztywno w tej wiadomości, lecz wynika z zapisów umowy o poziomie usług (Service Level Agreement) właściwej dla danego systemu płatniczego. |
| **1 1** | Kardynalność elementu. Oznacza, że pole `Charge Bearer` jest obowiązkowe i musi wystąpić dokładnie jeden raz w wiadomości. |

## Logika i relacje
Schemat przedstawia strukturę typu **wyliczenie (enumeration)**. Logika biznesowa opiera się na zasadzie wzajem


Proprietary Codes may also be available for certain data elements. These are typically inherited from legacy formats and require definitions in user documentation as these are not captured in the baseline ISO 20022 standards

example of Return Reason Information in pacs.004 v9 which uses externalised codes

![](_page_18_Figure_8.jpeg)

## Cel schematu
Celem tego schematu jest zdefiniowanie struktury danych oraz dopuszczalnych wartości dla informacji dotyczących powodu zwrotu transakcji (Return Reason) w standardzie ISO 20022. Ilustruje on przejście od wysokopoziomowej struktury wiadomości XML, poprzez definicję techniczną typu danych, aż po konkretny słownik kodów (Code Set), które są uznawane za poprawne i interoperacyjne między instytucjami finansowymi.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Return Reason Information** | Główny blok danych zawierający szczegółowe informacje o przyczynie zwrotu płatności lub transakcji. |
| **Originator** | Podmiot (instytucja), który wygenerował informację o powodzie zwrotu. |
| **Reason** | Element określający konkretną przyczynę, dla której transakcja nie mogła zostać sfinalizowana. |
| **Code** | Standaryzowany kod identyfikujący pow


![](_page_18_Picture_9.jpeg)

XLSX format is readable in MS Excel 19

---

