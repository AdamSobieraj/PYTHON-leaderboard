<!-- ELEMENT 1 -->
Preface

This Cross-Border Payment Reporting plus (CBPR+) User Handbook is intended to document and explain a variety of ISO 20022 payment related topics, as well as provide practical use cases to ensure a common understanding and adoption of ISO 20022 within the payment industry.

The SWIFT FINplus service will support CBPR+ messages on the SWIFT network traditionally associated with correspondent banking (manyto-many). These messages may be exchanged either between Agents in the same country or between Agents in different countries.

The use cases focus on a core topics where other relevant messages may also be referred to within the use case, it may also be necessary to consider other documented use cases, in order to capture a wider variation of scenarios.

Note:

This document jointly developed with the CBPR+ group continues to evolve inline with the Standards Release as:

CBPR+ continue to develop market practice guidelines for additional message.

Inaccuracies are identified and corrected.

Further use cases and/or explanation needs are identified

---

<!-- ELEMENT 2 -->
Change log (since last iteration)

Page 2 Updated - note Page 5 Updated - new messages added to index Page 6 Updated - new messages added to index Page 11 Updated - correction of Intermediary code Page 33 Updated - new messages and Usage Ids added Page 40 Updated - new pain message added to index Page 45 Updated - recognition of Payment Initiation relay rulebook Page 107 Updated - recognition of Payment Initiation relay rulebook Page 122 Updated - additional use cases in the index Page 126 New -use case Page 134 New - use case Page 135-182 New - pain.008 message section Page 184 Update - new messages added to index Page 204 Update - removed refer to Wait For Settlement Market Practice Page 351 New - new high level message flow Page 371 Updated - new messages added to index Page 379-380 New - pacs.003 use cases Page 400 Updated - additional guidance on ultimate parties on the return Page 423 Updated - correct to Agent description in Step 7 Page 458-488 New - pacs.010 Margin Collection section Page 489-529 New - pacs.003 Customer Direct Debit section Page 530 Updated - new message added to index Page 674 Updated - removed reference to SR 2023 Page 682 Updated - moved reference to multiple notification, now at an Item level Page 691 Updated - reference to multiple notification item Rule Page 698-716 New - camt.058 Notice to Received Cancellation section Page 743 Updated - new message added to index Page 764 Updated - use case id correction Page 774-795 New - Customer Cancellation Request section Page 823-883 New - Cheque message sections Page 880 Updated - use case id correction

The following icons dignify  changes to slide from the previous itineration. Updates to text on a slide are captured in gold .

---

<!-- ELEMENT 3 -->
Legend

Message type and direction

Optional Message type and direction

Focal Message type and direction

Agent

Legacy FIN  MT message

Payment Initiation  (pain)

Payment Clearing and Settlement (pacs)

Cash Management  Reporting (camt)

Cash Management  Exception & Investigations  (camt)

Focus message

Market  Infrastructure

Exceptional circumstance

Statement Authorised Party

Exception & Investigation  Case Assignee

Exception & Investigation  Case Assigner

pacs.008 Ultimate Debtor

pacs.008 Ultimate Creditor

Use Case variation

MT

pacs Debtor

pacs Creditor

Agent processing legacy format during a coexistence period

Statement Account Servicer

Extra attention  is needed

Initiating  party on behalf of the Debtor

New slide since last iteration

Slide updated since last iteration

U

Nested Element

Element Hierarchy Path

Element Choice

Nested Element involving  a choice

Shortcut to other part of document

Best practice

Statement Account Owner

gpi Tracker

---

<!-- ELEMENT 4 -->
Table of contents

Introduction to ISO 20022

Business Application Header

Payment Initiation (pain)

pain.001 - Interbank Customer Credit Transfer Initiation pain.002 - Interbank Customer Payment Status Report

pain.008 - Customer Direct Debit Initiation

new for SR2023

Payment, Clearing and Settlement (pacs) messages

pacs.002 - Financial Institution to Financial Institution Payment Status Report

pacs.004 - Payment Return

pacs.003 - Financial Institution to Financial Institution  Customer Direct Debit pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer

pacs.009 (core) - Financial Institution Credit Transfer pacs.009 (cov) - Financial Institution 'Cover' Credit Transfer

pacs.009 (adv) - Financial Institution 'Advice' Credit Transfer pacs.010 - Financial Institution Direct Debit

new for SR2023

---

<!-- ELEMENT 5 -->
Table of contents (continued)

5. Cash Management Reporting (camt) messages camt.052 - Bank to Customer Account Report

camt.053 - Bank to Customer Statement camt.054 - Bank to Customer Debit Credit Notification

camt.057 - Notification to Receive camt.058 - Notification to Receive Cancelation Advice

new for SR2023

6. Cash Management Exception & Investigation (camt) messages camt.029 - Resolution of Investigation

camt.055 - Customer Payment Cancelation Request new for SR2023

camt.056 - FI to FI Cancellation Request

7. Cheques

camt.107 - Cheque Presentment Notification new for SR2023

camt.108 - Cheque Cancellation or Stop Notification new for SR2023

camt.109 - Cheque Cancellation or Stop Report new for SR2023

---

<!-- ELEMENT 6 -->
Introduction to ISO 20022

---

<!-- ELEMENT 7 -->
Introduction to ISO 20022

ISO 20022 introduces a fundamental change to the traditional language used by the payments industry for several decades. It also describes participants (i.e., parties) to a business transaction  differently based upon the business domain (area) being described, in a similar way you may describe a person as a colleague, parent or sibling depending upon the context you wish to describe them. This section is designed to capture and explain some of the differences.

---

<!-- ELEMENT 8 -->
Introduction to ISO 20022 - Business Domains

Domains

Payment and Cash Management

Securities Trade Services Foreign Exchange

Card Payment

Message  Definitions

acmt

Account Management

auth

Authorities

camt

Cash Management

pacs

Payment Clearing and Settlement

pain

Payment Initiation

remt

Payment Remittance Advice

Message Sets

camt.052  Bank  to Customer  Account Report camt.053  Bank  to Customer  Statement camt.054  Bank  to Customer  Debit  Credit  Notification camt.056  FI  to FI  Payment  Cancellation  Request camt.057  Notification  to Receive pacs.002 FI  to FI  Payment  Status Report pacs.004 Payment  Return pacs.008 FI  to FI  Customer  Credit  Transfer pacs.009 Financial  Institution  Credit  Transfer

pain.001  Customer  Credit  Transfer initiation pain.002  Customer  Payment  Status Report pain.012  Creditor  Payment  Activation Request

ISO 20022 catalogue messages hierarchically beginning with a Business Domain, contain a various sets of Message Definitions, which in turn contain a variety of Message Sets.

for example:

Payment and Cash Management

Payments Clearing and Settlement

FI to FI Customer Credit Transfer (pacs.008)


## Cel schematu
Schemat ilustruje hierarchiczną architekturę modelu danych standardu ISO 20022. Jego celem jest przedstawienie sposobu budowania komunikatów finansowych w sposób modułowy – od najbardziej ogólnych definicji (fundamentów) po konkretne zestawy wiadomości wykorzystywane w procesach biznesowych. Ilustruje on zasadę "od ogółu do szczegółu", zapewniając spójność danych na wszystkich poziomach komunikacji międzyinstytucjonalnej.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Domain** | Poziom bazowy (domena). Zawiera wspólne komponenty, typy danych i słowniki, które są ustandaryzowane dla całego ekosystemu ISO 20022. Gwarantuje, że to samo pojęcie (np. "kod waluty" czy "identyfikator agenta") ma identyczne znaczenie w każdym komunikacie, niezależnie od jego przeznaczenia. |
| **Message Definition** | Poziom definicji pojedynczego komunikatu. Jest to konkretna struktura wiadomości zbudowana przy użyciu elementów z poziomu Domain. Określa, jakie pola są wymagane, opcjonalne oraz jaka jest ich kolejność w ramach jednej, konkretnej operacji biznesowej (np. zlecenie przelewu). |
| **Message Sets** | Poziom zestawów komunikatów. Grupa powiązanych ze sobą definicji wiadomości, które wspólnie realizują pełny proces biznesowy (tzw. *business case*). Zestaw ten opisuje przepływ informacji między uczestnikami procesu, gdzie jedna wiadomość inicjuje zdarzenie, a kolejne służą do potwierdzenia, rozliczenia lub odrzucenia operacji. |

## Logika i relacje
Schemat przedstawia relację zależności typu **bottom-up (od dołu do góry)** lub **warstwową**:

1. **Fundament $\rightarrow$ Struktura:** Poziom **Domain** stanowi fundament dla wszystkich pozostałych warstw. Bez zdefiniowanej domeny nie można stworzyć spójnej definicji wiadomości (**Message Definition**), ponieważ to domena dostarcza "cegiełek" (typów danych).
2. **Struktura $\rightarrow$ Proces:** Pojedyncze definicje wiadomości (**Message Definition**) są następnie grupowane w zestawy (**Message Sets**). Logika biznesowa polega


---

<!-- ELEMENT 9 -->
Introduction to ISO 20022 - Message Identifier


## Cel schematu
Celem schematu jest zdefiniowanie standardowej struktury nazewnictwa identyfikatorów wiadomości biznesowych w standardzie ISO 20022. Ilustruje on rygorystyczną składnię, która pozwala na jednoznaczną identyfikację rodzaju komunikatu finansowego, jego przeznaczenia oraz konkretnej wersji technicznej w skali globalnej. Rozwiązuje to problem interoperacyjności między różnymi systemami bankowymi i finansowymi, zapewniając, że każda instytucja interpretuje strukturę wiadomości w ten sam sposób.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **4!a** | Oznaczenie techniczne: 4 znaki alfabetu (litery). Określa obszar biznesowy. |
| **Business area** | Obszar Biznesowy – najwyższy poziom klasyfikacji, definiujący domenę funkcjonalną komunikatu (np. pacs, camt, pain). |
| **3!c** | Oznaczenie techniczne: 3 znaki alphanumeric/charaktery. Określa konkretny identyfikator wiadomości. |
| **Message identifier/functionality** | Identyfikator/Funkcjonalność wiadomości – precyzyjne określenie, jaką funkcję pełni wiadomość w danym obszarze biznesowym (np. przelew, wyciąg). |
| **3!n** | Oznaczenie techniczne: 3 cyfry (liczby). Określa wariant komunikatu. |
| **Variant** | Wariant – modyfikacja podstawowej funkcjonalności wiadomości dla specyficznych zastosowań lub rynków, przy zachowaniu głównego celu biznesowego. |
| **2!n** | Oznaczenie techniczne: 2 cyfry (liczby). Określa wersję komunikatu. |
| **Version** | Wersja – numer iteracji schematu XML/JSON, wskazujący na konkretną rewizję techniczną i zestaw reguł walidacyjnych. |

## Logika i rel



## Cel schematu
Celem tego schematu jest wyjaśnienie struktury i nomenklatury identyfikatora wiadomości w standardzie ISO 20022. Ilustruje on, w jaki sposób sformalizowany kod (w tym przypadku `pacs.008.001.08`) służy do jednoznacznej identyfikacji obszaru biznesowego, rodzaju transakcji, wariantu wiadomości oraz jej wersji technicznej. Jest to kluczowe dla zapewnienia interoperacyjności między systemami różnych instytucji finansowych na całym świecie.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **pacs** | Skrót od *Payments Clearing and Settlement*. Jest to obszar biznesowy (Business Area) odpowiedzialny za rozliczenia i clearing płatności między instytucjami finansowymi. |
| **008** | Identyfikator konkretnego typu wiadomości w ramach obszaru pacs. W tym przypadku odnosi się do *FI To FI Customer Credit Transfer* (Przelew kredytowy klienta między instytucjami finansowymi). |
| **001** | Numer wariantu (*Variant*). Określa on konkretną odmianę struktury wiadomości, która może być dostosowana do różnych scenariuszy biznesowych lub wymagań regulacyjnych. |
| **08** | Numer wersji (*Version*). Wskazuje na konkretną rewizję techniczną schematu XML. Każda nowa wersja może wprowadzać zmiany w polach danych lub regułach walidacji. |
| **pacs.008.001.08** | Pełny identyfikator wiadomości ISO 20022, który precyzyjnie definiuje standard komunikacyjny dla danej transakcji. |

## Logika i relacje
Schemat przedstawia hierarchiczną strukturę identyfikacji od ogółu do szczegółu (od lewej do prawej). Logika biznesowa opiera się na kaskadowym zawężaniu definicji wiadomości:

1. **Poziom Obszaru (pacs):** Najpierw system określa kontekst wysokiego poziomu – w tym przypadku rozliczenia międzybankowe.
2. **Poziom Funkcji (008):** W ramach obszaru pacs definiowany jest konkretny cel biznesowy – przesłanie środków klienta z jednego banku do drugiego.
3. **Poziom Implementacji (001):** Następnie wskazywany jest wariant, który precyzuje strukturę danych dla tego konkretnego celu.


---

<!-- ELEMENT 10 -->

## Cel schematu
Celem tego schematu jest przedstawienie ewolucji identyfikacji stron transakcji (Party Identifiers) w przejściu z tradycyjnego formatu SWIFT MT (FIN) na nowoczesny standard ISO 20022. Ilustruje on pełny cykl życia płatności – od jej zainicjowania, przez rozliczenia międzybankowe, aż


---

<!-- ELEMENT 11 -->
SWIFT FINplus Message structure

The diagram attempts to explain the construct of an ISO 20022 message sent across the SWIFT network using the FINplus service (which is designated to support various ISO 20022 business domains on SWIFT Interact)

Within the CBPR+ User Handbook the predominant focus is on the Request Payload, as this is where the business information is contained. However, it is worth noting that a network provider will have additional containers around the Request Payload to perform functionality on its network. This diagram presents the additional containers on the SWIFT network such as the Request Header often referred to as the Technical Header of the message.


## Cel schematu
Celem schematu jest przedstawienie architektury warstwowej (modelu enkapsulacji) wiadomości finansowej przesyłanej w sieci SWIFT przy użyciu standardu ISO 20022. Ilustruje on rozróżnienie pomiędzy **warstwą transportową/sieciową** (SWIFTNet Headers), która odpowiada za dostarczenie wiadomości, a **warstwą biznesową** (Business Message), która zawiera właściwą treść merytoryczną i instrukcje aplikacyjne.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Exchange Request** | Najwyższy poziom opakowania komunikatu; kompletne żądanie wymiany danych między dwoma punktami końcowymi w sieci. |
| **Request** | Struktura zawierająca wszystkie elementy niezbędne do przetworzenia żądania przez infrastrukturę sieciową. |
| **RequestHeader** | Nagłówek techniczny poziomu sieci, zawierający informacje niezbędne dla routerów i systemów SWIFT do przekierowania komunikatu. |
| **RequestPayload** | „Koperta” (envelope) – kontener, w którym zamknięta jest właściwa wiadomość biznesowa; oddziela warstwę transportu od treści. |
| **Crypto


---

<!-- ELEMENT 12 -->
XML Elements

XML Elements

An XML instance or document contains data in elements and nested elements (elements which contain other elements) corresponding to the hierarchy imposed by the XML schema. In the CBPR+ Usage Guidelines we often refer to the element hierarchy by levels (to understand the nested relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example in a pacs.008 Customer Credit Transfer the Interbank Settlement Date is a sub-element (Level 2) of the Credit Transfer Transaction Information element (Level 1).

Naming conventions

An XML  element is named according to the following rules:

The name can contain letters, numbers, and other characters, but must not start with a number or punctuation  mark.

The name must not start with XML,  xml, or Xml.

The name must not contain any spaces.

MX naming conventions

There are some generic naming rules that apply to most items in the database.

The names of all items in the database use the upper CamelCase convention,  as follows:

Each word starts with a capital letter.

There are no white spaces between words.

A name may be made up of multiple words, each consisting of alphanumeric characters.

Words use British English vocabulary.

All  names must start with an alphabetic character.

All  characters that follow the first characters must be letters or numbers.

Example of a Street Name element: <StrtNm>Oxford Street</StrtNm>

MX message element multiplicity  (occurrences)

An MX  message element specifies its cardinality (number of elements in a set) using minimum (min) & maximum (max) to describe the occurrences.


## Cel schematu
Schemat przedstawia strukturę danych w standardzie ISO 20022 dotyczącą rozliczeń międzybankowych w ramach przelewu kredytowego (Credit Transfer). Jego celem jest zdefiniowanie hierarchii informacji, wskazując, jakie konkretne parametry finansowe i czasowe muszą być powiązane z danymi transakcyjnymi, aby proces rozliczenia środków między instytucjami finansowymi (settlement) mógł zostać prawidłowo przeprowadzony.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Credit Transfer Transaction Information** | Główny kontener danych zawierający szczegółowe informacje o pojedynczej transakcji przelewu kredytowego. Jest to poziom nadrzędny, który grupuje wszystkie atrybuty konkretnego zlecenia płatniczego. |
| **Interbank Settlement Amount** | Kwota rozliczenia międzybankowego. Jest to rzeczywista wartość środków, która zostaje przesunięta między rachunkami banków w systemie rozliczeniowym (np. w banku centralnym), co może różnić się od kwoty zlecenia, jeśli doliczone są opłaty lub prowizje międzybankowe. |
| **Interbank Settlement Date** | Data rozliczenia międzybankowego. Jest to data walutowa (value date), w której środki zostają faktycznie rozliczone pomiędzy instytucjami finansowymi uczestniczącymi w transakcji. |
| **mark.** | Fragment tekstu widoczny na schemacie; w kontekście technicznym może być częścią dłuższego słowa (np. "benchmark") lub oznaczeniem przypisu, jednak nie stanowi on samodzielnego terminu biznesowego standardu ISO 20022. |

## Logika i relacje
Schemat przedstawia relację hierarchiczną typu **jeden-do-wielu** (parent-child). 

1. **Punkt wyjścia:** Element nadrzęd



## Cel schematu
Celem tego schematu jest zdefiniowanie zasad **kardynalności (multiplicity)** elementów danych w standardzie ISO 20022. Ilustruje on techniczne reguły określające, ile razy dany element (pole/tag) może lub musi wystąpić w wiadomości XML. Jest to kluczowe dla procesu walidacji komunikatów finansowych – pozwala systemom odbiorczym określić, czy wiadomość jest kompletna i poprawnie sformatowana zgodnie z definicją biznesową.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| Element Multiplicity | Wielokrotność elementu; określa dopuszczalną liczbę wystąpień danego pola w strukturze wiadomości. |
| Min | Minimalna liczba wymaganych wystąpień elementu. Jeśli wynosi 1, pole jest obowiązkowe. Jeśli 0, pole może zostać pominięte. |
| Max | Maksymalna dopuszczalna liczba wystąpień elementu w ramach jednego bloku danych. |
| Required element | Element wymagany; musi wystąpić dokładnie jeden raz (nie może go zabraknąć i nie może być powielony). |
| Optional element | Element opcjonalny; może wystąpić zero lub jeden raz. Jest dopuszczalny, ale jego brak nie powoduje błędu walidacji. |
| Unlimited element occurrences | Nieograniczona liczba wystąpień; element może nie wystąpić wcale lub pojawić się dowolną liczbę razy (np. lista transakcji). |
| * (gwiazdka) | Symbol techniczny oznaczający brak górnego limitu (nieograniczoną ilość powtórzeń). |

## Logika i relacje
Logika schematu opiera się na matematycznym przedziale między wartościami **Min** a **Max**, co bezpośrednio przekłada się na biznesowy status pola w wiadomości ISO 20022:

1.  **Relacja 1 $\rightarrow$ 1 (Ścisła zależność):** Gdy minimum i maksimum wynoszą 1, tworzy to wymóg bezwzględny. Z punktu widzenia biznesowego jest to krytyczna informacja (np. numer referencyjny przelewu), bez której wiadomość jest nieprawidłowa.
2.  **Relacja 0 $\rightarrow$ 1 (Dopuszczalna nieobecność):** Gdy minimum wynosi 0, a maksimum 1, pole staje się opcjonalne. Biznesowo oznacza to informację dodatkową, która może być


---

<!-- ELEMENT 13 -->
XML Elements (continued)

Empty XML Elements

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element.

Acommon example of this is in payment message is Financial Institution.


## Cel schematu
Schemat ten definiuje strukturę danych służącą do jednoznacznej identyfikacji instytucji finansowej w ramach standardu ISO 20022. Jego celem jest zapewnienie ustandaryzowanego sposobu przekazywania informacji o bankach lub innych podmiotach finansowych uczestniczących w transakcji (np. agent dłużnika, agent wierzyciela), co minimalizuje ryzyko błędów w routingu płatności i zwiększa transparentność operacji finansowych na poziomie globalnym.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Financial Institution Identification** | Główny blok (kontener) danych służący do identyfikacji instytucji finansowej. Jest elementem obowiązkowym (kardynalność 1:1). |
| **BICFI** | Business Identifier Code for Financial Institutions. Standardowy kod SWIFT/BIC, który pozwala na jednoznaczną identyfikację banku w sieci międzynarodowej. |
| **Clearing System Member Identification** | Identyfikator członka systemu rozliczeniowego. Unikalny kod przypisany do instytucji w ramach konkretnego krajowego lub regionalnego systemu rozliczeń (np. systemy RTGS). |
| **LEI** | Legal Entity Identifier. Globalny, 20-znakowy kod identyfikacyjny dla podmiotów prawnych uczestniczących w aktywnościach finansowych, zwiększający przejrzystość rynków kapitałowych. |
| **Name** | Pełna, oficjalna nazwa instytucji finansowej. |
| **Postal Address** | Adres pocztowy siedziby instytucji, zawierający szczegóły lokalizacji geograficznej. |
| **1 1 (kardynalność)** | Oznacza, że element jest obowiązkowy i musi wystąpić dokładnie jeden raz. |
| **0 1 (kardynalność)** | Oznacza, że element jest opcjonalny – może nie wystąpić wcale


Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e., <FinInstnId></FinInstnId>

In the FINplus service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where business data should be provided within a nested element, it is provided.

---

<!-- ELEMENT 14 -->
XML Elements within CBPR+ User Hand Book

MyStandards describes the element's context by its path whereby each element is divided by a forward slash (/) For example the pacs.008 Town Name within the Debtor Postal Address is described as /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/PstlAdr/TwnNm

Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing the element in an XML naming convention.

For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment Identification is an element below Credit Transfer Transaction Information.

Credit Transfer Transaction Info' Payment Identification

In this way the CBPR+ User Hand Book uses three main icon to explain the relationships between element, by display the icon after the element name.

To visualise an element which has nested elements beneath it

To visualise an element which has a choice associated with it i.e., a Code where a choice of which code can be determined

To visualise an element which is nested and has a choice associated with it. For example, an Identification where a choice must be made between an Organisation Identification and a Private Identification element which is nested, but where both cannot be used together.

---

<!-- ELEMENT 15 -->
The CBPR+ group has published all its usage guidelines in MyStandards


## Cel schematu
Przedstawiony obraz to centrum zasobów technicznych i biznesowych dla standardu **CBPR+ (Cross-Border Payments and Reporting Plus)** w ramach platformy SWIFT MyStandards. Jego celem jest dostarczenie instytucjom finansowym kompletnego ekosystemu dokumentacji, narzędzi i wytycznych niezbędnych do implementacji standardu ISO 20022 w płatnościach transgranicznych. Schemat ten ilustruje strukturę wspar


https://www2.swift.com/mystandards/#/c/cbpr/landing

---

<!-- ELEMENT 16 -->
Message Usage Guideline - Additional Information and principals


## Cel schematu
Celem przedstawionego materiału jest zaprezentowanie sposobu dostępu do i interpretacji **Usage Guidelines** (wytycznych użytkowania) dla konkretnego standardu wiadomości ISO 20022 w ramach sieci SWIFT. Schemat ilustruje, jak teoretyczny standard ISO zostaje doprecyzowany do poziomu konkretnych zasad biznesowych (**Principles**) stosowanych w programie CBPR+ (Cross Border Payments and Reporting Plus), aby zapewnić interoperacyjność i automatyzację przelewów transgranicznych między bankami.

## Kluczowe koncepcje

| Pojęcie/Termin |


---

<!-- ELEMENT 17 -->
Rules

Traditionally in the Legacy FIN standard rules related to a message were described as either Network Validation Rules -those validated by the network, or Usage rules - rules not validated by the network. FIN also has the concept of Usage Guidelines -guideline to recommend a best practice.

In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated UsageGuideline(e.g. CBPRplus)

Within CBPR+ UsageGuidelinespecification the rules dedicate to CBPR+ are often described as:

Formal Rules which are validated on the network, these are identified by the word Rule appended to the rule description. For example: Rule 'CBPR_Party_Name_Any_BIC_FormalRule'

Textual Rules which are not validated on the network, these are identified by with the word TextualRule appendedto the rule description. For example: Rule 'CBPR_Agent_Option_1_TextualRule'

Guideline Rules which provide recommended best practice, these are identified by the word Guideline appendedto the rule description. For example:

Rule 'CBPR_Purpose_Guideline'

Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a CrossElementSimpleRule and a CrossElementComplexRule

---

<!-- ELEMENT 18 -->
Usage Identifier  - Format


## Cel schematu
Celem tego schematu jest zdefiniowanie rygorystycznej struktury syntaktycznej (formatu) identyfikatora tzw. **Business Context** w standardzie ISO 20022. Schemat ten określa, w jaki sposób należy budować ciąg znaków, który pozwala systemom finansowym jednoznacznie zidentyfikować: kto stworzył daną regułę biznesową (organizacja), jakiego obszaru ona dotyczy (kontekst) oraz w której wersji jest ona aktualna. 

Jest to kluczowe dla interoperacyjności między bankami i instytucjami finansowymi, aby oba końce transakcji wiedziały, jaki "zeszyt reguł" (rulebook) jest stosowany do walidacji danej wiadomości.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| `<Short issuer organisation>` (A) | Skrócony identyfikator organizacji, która wydała standard lub regułę biznesową (np. SWIFT, EPC). Limit: od 1 do 10 znaków. |
| `<Business context>` (B, C, D...) | Określenie konkretnego obszaru biznesowego, procesu lub usługi, której dotyczy wiadomość. Może występować jeden lub wiele takich elementów. Każdy z nich ma limit 1-10 znaków. |
| `{.<Business context>} n times` | Wskazanie na strukturę rekurencyjną/powtarzalną. Oznacza, że po pierwszym kontekście mogą nastąpić kolejne poziomy uszczegółowienia (n razy), przedzielone kropką. |
| `<version>` (E) | Numer wersji reguły biznesowej, co pozwala na wersjonowanie standardów bez przerywania ciągłości procesów. Limit: dokładnie 2 znaki. |
| `.` (1 char) | Separator w formie kropki, który oddziela poszczególne poziomy hierarchii identyfikatora. |
| `Total max 35 char` | Całkowity limit długości całego ciągu znaków, którego nie można przekroczyć (ograniczenie techniczne pola w wiadomości ISO 20022). |

## Logika i relacje
Schemat przedstawia hierarchiczny przepływ informacji od ogółu do szczegółu:

1. **Poziom najwyższy (Wydawca):** Proces zaczyna się od identyfikacji organizacji (`Short issuer organisation`), która jest "właścicielem" standardu.
2. **Poziom średni


Type: String

Max allowed size: 35 characters

Structure:

o Must contain minimum A & B , optionally  followed by 1 or more additional business context elements (C, D, …).

o Always ends with version element E (format 'nn', e.g., '01')

o Each element is separated by a period '.'

o Length of each text element can vary up to max 10 characters. Total length, including periods, cannot exceed 35 chars.

o Consistency enforced by lightweight  SWIFT review/registration:  E.g., 'ecb' to represent the ECB, not 'eucb'

o Lowercase alphanumerical characters only

In CBPR+ the Usage Identifier is captured within the Business Application Header , Business Service element. More detail can be found in the dedicated Business Application Header chapter of this document,

.

.

.

---

<!-- ELEMENT 19 -->
ISO 20022 External Code Lists

Many ISO 20022 message use data elements represented by codes. Such codes are often externalised from the message itself, enabling maintenance  of the code list on a quarterly basis without requiring a new message version.

Some data element may also be embedded in the message.

example of Charge Bearer in pacs.008 v8 which uses embedded codes


## Cel schematu
Celem tego schematu jest zdefiniowanie elementu **Charge Bearer** (Podmiot ponoszący koszty), który w standardzie ISO 20022 służy do jednoznacznego określenia, która ze stron transakcji płatniczej pokrywa opłaty i prowizje bankowe związane z realizacją przelewu. Schemat ten eliminuje niejednoznaczność w rozliczeniach międzybankowych, wskazując na konkretny kod instrukcji kosztowej.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Charge Bearer** | Główny element (kontener) określający zasady ponoszenia kosztów transakcji. |
| **1 1** (Kardynalność) | Oznacza, że element ten jest obowiązkowy i musi wystąpić dokładnie jeden raz w wiadomości. |
| **Borne By Debtor [DEBT]** | Koszty są ponoszone przez dłużnika (nadawcę przelewu). Odpowiada to tradycyjnemu modelowi "OUR". |
| **Borne By Creditor [CRED]** | Koszty są ponoszone przez wierzyciela (odbiorcę przelewu). Odpowiada to tradycyjnemu modelowi "BEN". |
| **Shared [SHAR]** | Koszty są dzielone: dłużnik płaci opłaty swojemu bankowi, a wierzyciel opłatom banków pośredniczących i swojego banku. Odpowiada to modelowi "SHA". |
| **Following Service Level [SLEV]** | Koszty są określane zgodnie z poziomem usług (Service Level Agreement) uzgodnionym między instytucjami finansowymi. |

## Logika i relacje
Schemat przedstawia strukturę hierarchiczną typu **wybór (enumeration)**. 

1. **Relacja nadrzędna**: `Charge Bearer` jest elementem nadrzędnym, który definiuje kontekst biznesowy (kto płaci).
2. **Logika wyboru**: Elementy znajdujące się poniżej (`DEBT`, `CRED`, `SHAR`, `SLEV`) są alternatywnymi wartościami. W konkretnej wiadomości XML ISO


Proprietary Codes may also be available for certain data elements.

These are typically inherited from legacy formats and require definitions in user documentation  as these are not captured in the baseline ISO 20022 standards


## Cel schematu
Schemat przedstawia strukturę i zasady walidacji danych dla elementu **Return Reason Information** w ramach standardu ISO 20022, konkretnie dla komunikatu **pacs.004 v9 (Payment Return)**. 

Jego głównym celem biznesowym jest ujednolicenie sposobu raportowania przyczyn zwrotów płatności między instytucjami finansowymi. Zamiast stosować opisowy tekst wolny (który byłby niejednoznaczny), schemat wymusza zastosowanie **zewnętrznych kodów reason (externalised codes)**. Dzięki temu systemy bankowe mogą automatycznie przetwarzać powody zwrotów, co przyspiesza procesy operacyjne i minimalizuje błędy w komunikacji międzybankowej.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **pacs.004 v9** | Standardowy komunikat ISO 20022 służący do informowania o zwrocie przelewu (Payment Return). |
| **Return Reason Information** | Blok danych zawierający szczegółowe informacje o tym, dlaczego dana płatność została zwrócona. |
| **Originator** | Podmiot


19 XLSX format is readable in MS Excel

---

