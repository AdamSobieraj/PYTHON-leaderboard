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
Schemat ilustruje hierarchiczną strukturę budowy standardu ISO 20022. Jego celem jest przedstawienie warstwowej architektury metodologii projektowania komunikatów finansowych, pokazując przejście od ogólnych definicji biznesowych (fundamentów) do konkretnych zestawów komunikatów stosowanych w procesach operacyjnych. Ilustruje on zasadę reużywalności danych i modularność standardu.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Domain** | Najniższy poziom architektury (warstwa bazowa). Definiuje wspólny słownik biznesowy, komponenty danych oraz reguły właściwe dla danej dziedziny (np. płatności, zarządzanie aktywami), niezależnie od konkretnego komunikatu. |
| **Message Definition** | Poziom definicji pojedynczego komunikatu. Polega na wykorzystaniu elementów z warstwy "Domain" do stworzenia struktury konkretnej wiadomości (np. pacs.008), określając, które dane są wymagane i w jakiej kolejności występują. |
| **Message Sets** | Najwyższy poziom organizacji. Jest to logiczne grupowanie wielu definicji komunikatów, które wspólnie realizują dany proces biznesowy lub konkretny scenariusz wymiany informacji (use case). |

## Logika i relacje
Schemat przedstawia relację zależności typu **bottom-up** (od dołu do góry), gdzie każda kolejna warstwa budowana jest na fundamencie poprzedniej:

1. **Zależność Domain $\rightarrow$ Message Definition**: Definicja komunikatu nie powstaje "z próżni", lecz czerpie z puli komponentów zdefiniowanych w Domenie. Dzięki temu ten sam element (np. "Kod waluty") jest identyczny we wszystkich komunikatach danej domeny, co zapewnia spójność danych (interoperacyjność).
2. **Zależność Message Definition $\rightarrow$ Message Sets**: Zbiory komunikatów są kompozycją pojedynczych definicji. Logika biznesowa na tym poziomie nie dotyczy już tego, "jak wygląda pole", ale "jakie komunikaty muszą zostać wymienione", aby proces (np. przelew transgraniczny) został sfinalizowany.


---

<!-- ELEMENT 9 -->
Introduction to ISO 20022 - Message Identifier


## Cel schematu
Schemat przedstawia strukturę i składnię **identyfikatora wiadomości ISO 20022** (tzw. *Message Identification*). Jego celem jest zdefiniowanie ustandaryzowanego formatu nazewnictwa, który pozwala systemom finansowym na jednoznaczne rozpoznanie rodzaju przesyłanego komunikatu, jego przeznaczenia biznesowego oraz wersji technicznej. Rozwiązuje on problem interoperacyjności w globalnym obrocie finansowym, zapewniając, że każda instytucja interpretuje typ wiadomości w ten sam sposób.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **4!a** | Definicja długości i typu danych dla obszaru biznesowego: dokładnie 4 znaki alfanumeryczne. |
| **3!c** | Definicja długości i typu danych dla identyfikatora wiadomości: dokładnie 3 znaki (litery/charaktery). |
| **3!n** | Definicja długości i typu danych dla wariantu: dokładnie 3 cyfry (numeric). |
| **2!n** | Definicja długości i typu danych dla wersji: dokładnie 2 cyfry (numeric). |
| **Business area** | Obszar biznesowy – najwyższy poziom kategoryzacji (np. *pacs* dla płatności międzybankowych, *pain*



## Cel schematu
Celem tego schematu jest wyjaśnienie struktury i nomenklatury identyfikatora wiadomości w standardzie ISO 20022. Ilustruje on hierarchiczny sposób nazywania komunikatów finansowych, pozwalając na precyzyjne określenie domeny biznesowej, konkretnego typu operacji, wariantu implementacyjnego oraz wersji technicznej danego schematu XML.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **pacs** | Skrót od *Payments Clearing and Settlement*. Jest to obszar biznesowy (Business Area) odpowiedzialny za rozliczenia i clearing płatności między instytucjami finansowymi. |
| **008** | Identyfikator konkretnego typu wiadomości w ramach domeny pacs. W tym przypadku oznacza on *FI To FI Customer Credit Transfer* – przelew kredytowy klienta realizowany pomiędzy dwiema instytucjami finansowymi. |
| **001** | Numer wariantu (*Variant*). Wskazuje na konkretną odmianę wiadomości, która może być dostosowana do specyficznych wymogów rynkowych lub prawnych przy zachowaniu ogólnej funkcji komunikatu. |
| **08** | Numer wersji (*Version*). Określa iterację techniczną schematu. Wersjonowanie pozwala na wprowadzanie zmian w strukturze danych bez przerywania kompatybilności z systemami obsługującymi starsze wersje. |
| **pacs.008.001.08** | Pełny identyfikator wiadomości ISO 20022, który jednoznacznie definiuje standard komunikatu używanego w transakcji. |

## Logika i relacje
Logika schematu opiera się na hierarchii od ogółu do szczegółu (od lewej do prawej). Struktura identyfikatora jest zbudowana z czterech segmentów oddzielonych kropkami, gdzie każdy kolejny element zawęża definicję komunikatu:

1. **Domena ($\text{pacs}$) $\rightarrow$ Funkcja ($\text{008}$):** Najpierw określamy obszar biznesowy (rozliczenia), a następnie konkretną operację w tym obszarze (przelew klient-klient przez banki).
2. **Funkcja ($\text{008}$) $\rightarrow$ Wariant ($\text{001}$):** Dla jednej funkcji biznesowej może istnieć kilka wariantów zależnie od kontekstu zastosowania.
3. **


---

<!-- ELEMENT 10 -->




---

<!-- ELEMENT 11 -->
SWIFT FINplus Message structure

The diagram attempts to explain the construct of an ISO 20022 message sent across the SWIFT network using the FINplus service (which is designated to support various ISO 20022 business domains on SWIFT Interact)

Within the CBPR+ User Handbook the predominant focus is on the Request Payload, as this is where the business information is contained. However, it is worth noting that a network provider will have additional containers around the Request Payload to perform functionality on its network. This diagram presents the additional containers on the SWIFT network such as the Request Header often referred to as the Technical Header of the message.


## Cel schematu
Celem tego schematu jest przedstawienie architektury opakowywania (enkapsulacji) wiadomości finansowych w standardzie ISO 20022 podczas ich przesyłania za pośrednictwem sieci SWIFTNet. Schemat ilustruje różnicę między warstwą transportową (techniczną), a warstwą biznesową, pokazując, jak konkretna wiadomość MX (ISO 20022) jest osadzona wewnątrz kolejnych struktur („kopert”), aby mogła zostać bezpiecznie i prawidłowo dostarczona do odbiorcy.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Exchange Request** | Najwyższy poziom struktury; całe zapytanie o wymianę danych, które jest przesyłane w sieci. |
| **Request** | Główny obiekt żądania zawierający nagłówki transportowe oraz ładunek (payload). |
| **SWIFTNet Headers** | Nagłówki techniczne sieci SWIFT, odpowiedzialne za routing i dostarczenie wiadomości między punktami końcowymi. |
| **RequestHeader** | Specyficzny element nagłówka transportowego zawierający informacje niezbędne do przekazania zapytania w infrastrukturze SWIFT. |
| **RequestPayload** | „Koperta” (envelope), która służy jako kontener dla właściwej wiadomości biznesowej. Oddziela warstwę przesyłu od treści. |
| **Crypto** | Warstwa kryptograficzna zapewniająca bezpieczeństwo, integralność i autentyczność przesyłanych danych (szyfrowanie/podpisy). |
| **Application Header / `<AppHdr>`** | Biznesowy nagłówek aplikacji ISO 20022. Zawiera metadane niezbędne do przetwarzania biznesowego (np. identyfikator nadawcy, odbiorcy i typ wiadomości). |
| **Document / `<Document>`** | Główny korpus wiadomości ISO 20022 zawierający faktyczne dane finansowe/biznesowe. |
| **MX Message Instance** |


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
Celem tego schematu jest zdefiniowanie struktury danych dotyczących rozliczeń międzybankowych w ramach pojedynczej transakcji przelewu kredytowego (Credit Transfer) zgodnie ze standardem ISO 20022. Schemat ilustruje zależność między ogólnymi informacjami o transakcji a konkretnymi parametrami technicznymi procesu rozliczania środków pomiędzy instytucjami finansowymi, co pozwala na precyzyjne określenie, kiedy i w jakiej kwocie nastąpi faktyczny przepływ pieniędzy między bankami (tzw. *settlement*).

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Credit Transfer Transaction Information** | Zbiór danych identyfikujących i opisujących konkretny przelew kredytowy. Jest to nadrzędny kontener informacji o transakcji, który zawiera szczegóły dotyczące płatności zleconej przez klienta. |
| **Interbank Settlement Amount** | Kwota rozliczenia międzybankowego. Jest to faktyczna suma pieniędzy, która zostaje przelana pomiędzy rachunkami banków w systemie rozliczeniowym (np. w banku centralnym), co może różnić się od kwoty przelewu klienta ze względu na np. opłaty lub netting. |
| **Interbank Settlement Date** | Data rozliczenia międzybankowego. Precyzyjna data, w której środki zostają sfinalizowane pomiędzy instytucjami finansowymi (data wartości rozliczeniowej), co nie zawsze jest tożsame z datą księgowania transakcji na rachunku klienta. |

## Logika i relacje
Schemat przedstawia relację hierarchiczną typu **rodzic-dziecko (parent-child)**:

1.  **Punkt wyjścia:** Głównym elementem jest `Credit Transfer Transaction Information`. Stanowi on kontekst dla całej operacji płatniczej.
2.  **Specyfikacja rozliczeń:** Z tego elementu wywodzą się dwa kluczowe atrybuty dotyczące warstwy infrastrukturalnej (międzybankowej). 
3.  **Zależność biznesowa:** Logika wskazuje, że każda informacja o transakcji przelewu musi być powiązana z konkretną kwotą i datą rozliczenia między bankiem wysyłającym a bankiem otrzymującym. Rozdzielenie tych dwóch pól (`Amount` i `Date`) pozwala na pełną kontrolę nad płynnością finansową banków oraz precyzyjne zarządzanie ryzykiem w systemach RTGS (Real-Time Gross Settlement).

## Kluczowe wnioski
- **



## Cel schematu
Celem schematu jest zdefiniowanie zasad tzw. multiplicity (krotności/wielokrotności) elementów w strukturze komunikatów ISO 20022. Dokument ten służy jako techniczny klucz do interpretacji schematów XML (XSD), określając, ile razy dany element danych może lub musi pojawić się w wiadomości finansowej. Jest to krytyczne dla zapewnienia interoperacyjności między instytucjami finansowymi – odbiorca komunikatu musi wiedzieć, czy brak danego pola jest błędem, czy dopuszczalną sytuacją biznesową.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Element Multiplicity** | Krotność elementu; reguła określająca minimalną i maksymalną liczbę wystąpień danego pola w komunikacie. |
| **Min** | Minimalna liczba wystąpień elementu wymagana do uznania komunikatu za poprawny z punktu widzenia schematu technicznego. |
| **Max** | Maksymalna dopuszczalna liczba wystąpień danego elementu w jednej wiadomości. |
| **Required element** | Element obowiązkowy; musi wystąpić dokładnie jeden raz. Jego brak lub podwojenie spowoduje odrzucenie komunikatu (błąd walidacji). |
| **Optional element** | Element opcjonalny; może nie wystąpić wcale lub wystąpić maksymalnie raz. |
| **Unlimited element occurrences** | Nieograniczona liczba wystąpień; element może nie wystąpić, wystąpić raz lub wielokrotnie (np. lista wielu odbiorców przelewu). |
| ***** (gwiazdka) | Symbol techniczny oznaczający wartość "unbounded" (nieograniczony), czyli brak górnego limitu liczby powtórzeń elementu. |

## Logika i relacje
Logika schematu opiera się na przedziale wartości pomiędzy wartością minimalną (**Min**) a maksymalną (**Max**). Relacja ta determinuje status biznesowy pola w komunikacie:

1.  **Relacja 1 $\rightarrow$ 1 (Sztywna):** Gdy zarówno minimum jak i maksimum wynosi 1, tworzona jest zależność absolutna. Biznesowo oznacza to pole krytyczne (np. numer referencyjny transakcji), bez którego operacja nie może zostać przetworzona.
2.  **Relacja 0 $\rightarrow$ 1 (Elastyczna):** Gdy minimum wynosi 0, a maksimum 1, element staje się opcjonalny. Logika biznesowa dopuszcza tutaj brak informacji, ale zakazuje jej duplikowania w obrębie jednego bloku danych.
3.  **Relacja 0 $\rightarrow$ * (Kolekcyjna):** Gdy minimum wynosi 0, a maksimum jest nieograniczone, element funkcjonuje jako lista/tablica. Pozwala to na przesyłanie zmiennej liczby rekordów w jednym komunikacie (np. wiele pozycji w wyciągu


---

<!-- ELEMENT 13 -->
XML Elements (continued)

Empty XML Elements

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element.

Acommon example of this is in payment message is Financial Institution.


## Cel schematu
Schemat przedstawia strukturę danych służącą do jednoznacznej identyfikacji instytucji finansowej w ramach standardu ISO 20022. Jego celem jest zdefiniowanie zestawu atrybutów, które pozwalają systemom bankowym i rozliczeniowym na precyzyjne określenie, która organizacja uczestniczy w danej transakcji lub komunikacie (np. jako agent przesyłający, odbiorca lub instytucja rozliczająca). Ilustruje on hierarchię danych oraz zasady ich występowania (kardynalność), co jest kluczowe dla poprawnej walidacji komunikatów XML.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Financial Institution Identification** | Główny kontener (element nadrzędny) zawierający wszystkie dane służące do identyfikacji instytucji finansowej. |
| **BICFI** | *Business Identifier Code for Financial Institutions* – ustandaryzowany kod SWIFT/BIC używany do identyfikacji banków i instytucji finansowych w ruchu międzynarodowym. |
| **Clearing System Member Identification** | Identyfikator członka systemu rozliczeniowego – unikalny kod przypisany instytucji w konkretnym systemie clearingowym (np. systemach RTGS lub ACH). |
| **LEI** | *Legal Entity Identifier* | Globalny, unikatowy kod identyfikacyjny dla podmiotów prawnych uczestniczących w transakcjach finansowych (standard ISO 17442). |
| **Name** | Pełna, oficjalna nazwa instytucji finansowej. |
| **Postal Address** | Adres pocztowy siedziby instytucji, zawierający szczegóły takie jak ulica, miasto i kraj. |
| **Kardynalność (np. 1 1 / 0 1)** | Wskaźnik występowania elementu: pierwsza cyfra to liczba minimalna, druga to maksymalna. `1 1` oznacza element obowią


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
Celem przedstawionego zestawienia jest dostarczenie kompleksowego ekosystemu dokumentacji i narzędzi niezbędnych dla instytucji finansowych do wdrożenia standardu **CBPR+ (Cross-Border Payments and Reporting Plus)**. Schemat ten służy jako mapa drogowa implementacji normy ISO 20022 w obszarze płatności transgranicznych i raportowania gotówkowego w sieci SWIFT, zapewniając spójność danych pomiędzy różnymi uczestnikami rynku oraz umożliwiając migrację z przestarzałych standardów (MT) na nowoczesny format XML (MX).

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **CBPR+** | *Cross-Border Payments and Reporting Plus* – zbiór wytycznych określających, w jaki sposób standard ISO 20022 jest stosowany w płatnościach transgranicznych i raportowaniu w sieci SWIFT. |
| **ISO 20022** | Globalny standard wymiany danych finansowych oparty na języku XML, zapewniający większą strukturę i bogactwo informacji niż poprzednie standardy. |
| **CBPR+ Usage Guidelines and Readiness Portal** | Portal zawierający szczegółowe wytyczne dotyczące stosowania standardu oraz narzędzia do oceny gotowości instytucji do jego wdrożenia. |
| **CBPR+ Translation Portal** | Narzędzie/portal służące do zarządzania tłumaczeniem komunikatów pomiędzy różnymi formatami (np. MT $\leftrightarrow$ MX). |
| **CBPR+ user handbook** | Podręcznik użytkownika opisujący typowe scenariusze biznesowe w procesach płatności i raportowania transgranicznego. |
| **Data integrity market practice guidance** | Wytyczne dotyczące zachowania integralności danych, szczególnie w sytuacjach, gdy informacje są ucinane lub brakuje ich w standardzie MT. |
| **CBPR+ and HVPS+ alignment** | Analiza


https://www2.swift.com/mystandards/#/c/cbpr/landing

---

<!-- ELEMENT 16 -->
Message Usage Guideline - Additional Information and principals


## Cel schematu
Celem przedstawionego zrzutu ekranu jest prezentacja **Usage Guideline (Wytycznych Użytkowania)** dla konkretnego typu wiadomości w standardzie ISO 20022, w ramach ekosystemu CBPR+. Schemat ten służy jako techniczna specyfikacja implementacyjna, która definiuje, jak generyczny standard ISO 20022 (w tym przypadku `pacs.008`) ma być stosowany w praktyce przez instytucje finansowe uczestniczące w sieci płatności transgranicznych. Dokument ten rozwiązuje problem braku jednoznaczności standardu poprzez narzucenie konkretnych reguł biznesowych i ograniczeń danych.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **CBPR+ (Cross Border Payments and Reporting Plus)** | Globalny zestaw wytycznych dla płatności transgranicznych oparty na standardzie ISO 20022, mający na celu ujednolicenie komunikacji międzybankowej. |
| **pacs.008.001.08** | Specyficzny typ wiadomości ISO 20022: *Financial Institution Customer Credit Transfer*. Służy do przesyłania przelewu od klienta jednego banku do klienta innego banku. |
| **Usage Guideline (UG)** | Dokument definiujący, które elementy standardu są obowiązkowe, opcjonalne lub zakazane w konkretnym kontekście biznesowym (tutaj: dla CBPR+). |
| **MX** | Format wiadomości oparty na XML, będący podstawą nowoczesnego standardu ISO 20022 (w przeciwieństwie do starszych formatów MT/FIN). |
| **Usage Identifier (`swift.cbprplus


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
Celem tego schematu jest zdefiniowanie ścisłej struktury składniowej (syntaksy) identyfikatora biznesowego stosowanego w standardzie ISO 20022. Schemat określa zasady budowy ciągu znaków, który służy do jednoznacznego określenia kontekstu biznesowego transakcji lub komunikatu, zapewniając interoperacyjność między różnymi systemami finansowymi poprzez narzucenie limitów długości i konkretnej kolejności elementów.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| `<Short issuer organisation>` (A) | Krótki identyfikator organizacji, która wystawiła dany kod/identyfikator. Może mieć długość od 1 do 10 znaków. |
| `<Business context>` (B) | Główny kontekst biznesowy określający obszar lub rodzaj operacji. Może mieć długość od 1 do 10 znaków. |
| `{.<Business context>} n times` (C, D...) | Opcjonalne, dodatkowe poziomy doprecyzowania kontekstu biznesowego. Każdy kolejny element jest oddzielony kropką i może mieć od 1 do 10 znaków. Litera "n" oznacza dowolną liczbę powtórzeń w ramach limitu całkowitego. |
| `<version>` (E) | Numer wersji identyfikatora, co pozwala na ewolucję standardu bez utraty kompatybilności wstecznej. Ma stałą długość 2 znaków. |
| `.` (1 char) | Separator w postaci kropki, służący do rozdzielenia poszczególnych segmentów identyfikatora w celu łatwego parsowania danych. |
| `Total max 35 char` | Całkowity limit długości całego ciągu znaków, który nie może przekroczyć 35 znaków. |

## Logika i relacje
Schemat przedstawia hierarchiczną strukturę budowania identyfikatora "od ogółu do szczegółu". Logika przepływu informacji wewnątrz ciągu znaków jest następująca:

1. **Identyfikacja źródła:** Proces zaczyna się od wskazania organizacji wydającej (`Short issuer organisation`).
2. **Definicja kontekstu:** Następnie określa się główny obszar biznesowy, a jeśli jest to konieczne, dodaje się kolejne poziomy szczegółowości (hierarchia podkontekstów $\text{B} \rightarrow \text{C} \rightarrow \text{D} \dots$).
3. **Wersjonowanie:** Całość zamyka wersja identyfikatora, co pozwala systemowi odbiorcy wiedzieć, według której specyfikacji interpretować powyższe dane.

Każdy element jest od siebie oddzielony kropką, co tworzy strukturę przypominającą notację domenową (np. `


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
Schemat przedstawia definicję elementu **Charge Bearer** (Kto ponosi koszty), który jest kluczowym komponentem komunikatów w standardzie ISO 20022 (np. w wiadomościach typu pacs - *Payments Clearing and Settlement*). Jego celem jest jednoznaczne określenie, która ze stron transakcji finansowej – dłużnik (zleceniodawca) czy wierzyciel (zleceniobiorca) – jest odpowiedzialna za opłacenie kosztów i prowizji bankowych związanych z realizacją przelewu. Rozwiązuje to problem biznesowy dotyczący rozliczania kosztów operacyjnych między instytucjami finansowymi a klientami końcowymi.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Charge Bearer** | Główny element określający model rozliczenia kosztów transakcji (prowizji). W schemacie występuje z kardynalnością 1..1, co oznacza, że jest polem obowiązkowym i musi wystąpić dokładnie raz. |
| **Borne By Debtor [DEBT]** | Model "OUR". Wszystkie koszty transakcji ponosi dłużnik (zleceniodawca). Wierzyciel powinien otrzymać pełną kwotę przelewu bez potrąceń. |
| **Borne By Creditor [CRED]** | Model "BEN". Wszystkie koszty transakcji ponosi wierzyciel (zleceniobiorca). Prowizje są potrącane z kwoty przesyłanej, w efekcie czego wierzyciel otrzymuje kwotę pomniejszoną o koszty. |
| **Shared [SHAR]** | Model "SHA". Koszty są dzielone: dłużnik opłaca prowizję swojego banku, a wierzyciel ponosi koszty swojego banku oraz ewentualnych banków pośredniczących. |
| **Following Service Level [SLEV]** | Oznacza, że rozliczenie kosztów nie jest zdefiniowane w tym konkretnym polu, lecz wynika ze szczegółowych umów o poziomie usług (Service Level Agreement - SLA) zawartych między uczestnikami procesu. |

## Logika i relacje
Schemat reprezentuje strukturę **wyboru jednokrotnego (enumeracji)**. Logika biznesowa opiera się na następujących zależnościach:

1.  **Kardynalność (1 1):** Wymusza, aby każda wiadomość finansowa zawierała dokładnie jedną instrukcję dotyczącą kosztów. Brak tej informacji uniemożliwiłby bankom prawidłowe zaksięgowanie przelewu i pobranie opłat.
2.  **Relacja Wykluczania:** Wartości `DEBT`, `CRED`, `SHAR` oraz `SLEV` są wzajemnie wykluczające się. System przetwarzający komunikat musi wybrać tylko jeden z tych kodów, co determinuje dalszy przepływ środków pieniężnych.


Proprietary Codes may also be available for certain data elements.

These are typically inherited from legacy formats and require definitions in user documentation  as these are not captured in the baseline ISO 20022 standards


## Cel schematu
Celem tego schematu jest przedstawienie sposobu implementacji **zewnętrznych zestawów kodów (externalised codes)** w standardzie ISO 20022, na przykładzie komunikatu `pacs.004` (Payment Return). Schemat ilustruje mechanizm, w którym zamiast wpisywać opisowy powód zwrotu płatności w formie tekstu wolnego, system wykorzystuje ustandaryzowany kod o określonej długości, który odnosi się do zewnętrznego słownika definicji. Ma to na celu zapewnienie interoperacyjności między różnymi instytucjami finansowymi oraz umożliwienie automatycznego przetwarzania powodów zwrotów bez konieczności manualnej interpretacji tekstu.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **pacs.004 v9** | Wersja 9 komunikatu "Payment Clearing and Settlement", konkretnie typu *Payment Return* (zwrot płatności). |
| **Return Reason Information** | Blok danych zawierający szczegółowe informacje o przyczynach, dla których transakcja została zwrócona. |
| **Originator** | Podmiot/instytucja, która zainicjowała proces zwrotu środków. |
| **Reason** | Element nadrzędny określający powód zwrotu; może być wyrażony poprzez kod lub tekst własny (proprietary). |
| **Code** | Pole na ustandaryzowany kod powodu zwrotu. Jest ono obowiązkowe (kardynalność 1..1). |
| **Proprietary** | Pole na opis powodu zwrotu w formacie własnym instytucji, stosowane gdy standardowe kody są niewystarczające. |
|


19 XLSX format is readable in MS Excel

---

<!-- ELEMENT 20 -->
Character Set

All SWIFT ISO MX message elements (fields) which are defined (by data Type) as text are restricted to FIN X Characters:

a-z A-Z 0-9 / - ? : ( ) . , ' + .

Special characters are additionally allowed in:

All party (agents and non-agents) Name and Address elements.

The Related Remittance Information element

The Remittance Information (structured & unstructured) element

The Email Address where included as part of a Proxy elements

City of Birth and Province of Birth elements nested in Private Identification

List of special characters:

Currencies in the payments should be expressed in ISO Currency Codes only (3Characters, e.g. EUR)

Translation of any special character:

!#&%*=^_`{|}~";@[\]$ >< into MT messages will be represented by a . (Full Stop)


Jako ekspert od dokumentacji technicznej ISO 20022, analizuję przedstawiony obraz w kontekście standardów przesyłania wiadomości finansowych. Choć na pierwszy rzut oka schemat wydaje się być zbiorem przypadkowych symboli, w świecie ISO 20022 i komunikatów XML mają one krytyczne znaczenie dla **walidacji danych (Data Validation)** oraz **interoperacyjności systemów**.

## Cel schematu
Celem tego schematu jest zidentyfikowanie **znaków specjalnych (Special Characters)**, które w standardzie ISO 20022 są traktowane jako znaki ryzykowne lub zabronione w określonych polach danych. Schemat ilustruje problem tzw. "Character Set Restrictions". W kontekście biznesowym komunikuje on konieczność stosowania filtrów walidacyjnych (tzw. *sanitization*), aby uniknąć błędów parsowania plików XML oraz problemów z kompatybilnością przy konwersji wiadomości ISO 20022 na starsze formaty (np. SWIFT MT).

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie w kontekście ISO 20022 / XML |
|----------------|---------------------------------------------------|
| `$` | Symbol walutowy; dopuszczalny w polach opisowych, ale często monitorowany w polach kwot. |
| `!` | Znak specjalny; może być ograniczony w niektórych zestawach znaków (np. Latin Character Set). |
| `\` | Backslash; znany z problemów przy mapowaniu ścieżek plików i systemów legacy. |
| `%` | Procent; często używany w polach instrukcji, ale wymagający kontroli w walidacji typów danych. |
| `<` | **Znak krytyczny (XML)**; otwiera tag w XML. Jest zabroniony w treści pól bez eskapowania (`&lt;`). |
| `#` | Zнак specjalny; często używany jako separator, co może prowadzić do błędów w systemach legacy. |
| `]` | Nawias kwadratowy zamykający; znak techn


---

<!-- ELEMENT 21 -->
Point-to-point versus End-to-end

Point-to-point refers to data passed within a message from one party to the next. This data will not necessarily be passed in subsequent  messages.

For example: the Instruction Identification element contains a reference meaningful  to the party sending  a message, subsequent  messages in a payment transaction chain  can expect the Instruction Identification to be replaced by a reference meaningful  to the party sending  that message leg.

End-to-end refers to data passed throughout  the transaction life cycle i.e. within a message from one party to the next and continued  in subsequent  messages.

For example: the UETR element contains a Unique  End-to-end Transaction Reference in accordance with the UUID  version 4 standards. This same reference is used in all messages related to the payment transaction.

---

<!-- ELEMENT 22 -->
Agent Identification

ISO 20022 messages have a number of elements associated with Agents which allow for these Agents to be referenced by a variety of Financial Institution identifiers.

More commonly the ISO 9362 Financial Institution BIC ( BICFI ) is considered the best practice de facto standard for 'many to many' / correspondent banking payments. However other options include:

Clearing System Member Identifiers when accompanied with the Clearing System Identification . LEI (Legal Entity Identifier)

Name and either structured or unstructured Postal Address .


## Cel schematu
Celem tego schematu jest przedstawienie struktury danych służącej do jednoznacznej identyfikacji instytucji finansowej w ramach standardu ISO 20022. Ilustruje on hierarchię i zestaw atrybutów (identyfikatorów), które mogą być wykorzystane w komunikatach finansowych, aby wyeliminować niejednoznaczność przy przesyłaniu środków lub informacji między bankami i innymi podmiotami finansowymi na świecie.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| Financial Institution Identification | Główny komponent (kontener), który grupuje wszystkie dane służące do identyfikacji instytucji finansowej. |
| BICFI | Business Identifier Code for Financial Institutions. Standaryzowany kod (zwykle 8 lub 11 znaków) służący do globalnej identyfikacji banków i instytucji w sieci SWIFT. |
| Clearing System Member Id | Unikalny identyfikator członka przypisany przez konkretny system rozliczeniowy (np. system RTGS lub ACH). |
| Clearing System Id | Identyfikator samego systemu rozliczeniowego, który określa, w jakim środowisku/sieci funkcjonuje wspomniany powyżej Member Id. |
| LEI | Legal Entity Identifier. Globalny, 20-znakowy kod alfanumeryczny służący do identyfikacji podmiotów prawnych uczestniczących w transakcjach finansowych. |
| Name | Pełna, oficjalna nazwa instytucji finansowej. |
| Postal Address | Adres pocztowy siedziby instytucji. |
| Various sub element | Szczegółowe składowe adresu, takie jak: kraj, miasto, ulica, numer budynku czy kod pocztowy (zgodnie ze strukturą ISO 20022 dla adresów). |

## Logika i relacje
Schemat przedstawia relację hierarchiczną typu "jeden do wielu". Centralnym punktem jest **Financial Institution Identification**, z którego wywodzą się różne metody identyfikacji. Logika biznesowa opiera się na zasadzie komplementarności danych:

1.  **Różnorodność identyfikatorów:** System dopuszcza stosowanie różnych typów identyfikacji w zależności od kontekstu transakcji (np. BIC dla przelewów międzynarodowych, LEI dla raportowania regulacyjnego).
2.  **Zależności kontekstowe (Nesting):** 
    *   `Clearing System Member Id` nie może występować samodzielnie bez `Clearing


---

<!-- ELEMENT 23 -->
Date and DateTime

Two common elements to ISO 20022 messages are Date and DateTime.

CBPR+ usage guidelines DateTime elements mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) note - milliseconds are optional.

The ISO 20022 Date elements allow the date to include  an offset. As a data model, shared by other business domains, an offset date can provide great business clarify, such as something  expiring at the end of a business date. However, in payments such a date offset provides little business  value, whereby should an offset be include  with the date, this offset should be ignored.

---

<!-- ELEMENT 24 -->
Clearing System Identification comparison to National Clearing System Code

| Country      | Code Name                                            | MTClearing System code   | ISO 20022 Clearing System Identification   |
|--------------|------------------------------------------------------|--------------------------|--------------------------------------------|
| Australia    | Australian Bank State Branch Code (BSB)              | AU                       | AUBSB                                      |
| Austria      | Austrian Bankleitzahl                                | AT                       | ATBLZ                                      |
| Canada       | Canadian Payments Association Payment Routing Number | CC                       | CACPA                                      |
| China        | Bank Branch codeused in China                        | CN                       | CNAPS                                      |
| Germany      | German Bankleitzahl                                  | BL                       | DEBLZ                                      |
| Greece       | Helenic Bank IdentificationCode                      | GR                       | GRBIC                                      |
| Hong Kong    | Hong Kong Bank Code                                  | HK                       | HKNCC                                      |
| India        | Indian Financial SystemCode                          | IN                       | INFSC                                      |
| Ireland      | Irish National Clearing Code                         | IE                       | IENCC                                      |
| Italy        | Italian Domestic Identification Code                 | IT                       | ITNCC                                      |
| Japan        | Japan Zengin Clearing Code                           | JP                       | JPZGN                                      |
| New Zealand  | NewZealand National Clearing Code                    | NZ                       | NZNCC                                      |
| Poland       | Polish National Clearing Code                        | PL                       | PLKNR                                      |
| Portugal     | Portuguese National Clearing Code                    | PT                       | PTNCC                                      |
| Russia       | Russian Central Bank IdentificationCode              | RU                       | RUCBC                                      |
| South Africa | South African National ClearingCode                  | ZA                       | ZANCC                                      |
| Spain        | Spanish Domestic Interbanking Code                   | ES                       | ESNCC                                      |
| Switzerland  | Swiss Clearing Code (BC Code)                        | SW                       | CHBCC                                      |
| Switzerland  | Swiss Clearing Code (SIC Code)                       | SW                       | CHSIC                                      |
| Taiwan       | Financial InstitutionCode                            | TW                       | TWNCC                                      |
| UK           | UK Domestic Sort Code                                | SC                       | GBDSC                                      |
| US           | CHIPS Participant Identifier                         | CP                       | USPID                                      |
|              | United States Routing Number                         | FW                       | USABA                                      |

For translation rules and comparison purposes this table provides a list of published MT National Clearing System codes again their equivalent ISO 20022 Clearing System Identification in the external code list.

---

<!-- ELEMENT 25 -->
Business Application Header

---

<!-- ELEMENT 26 -->
head.001 Business Application Header - Character Set

Min 0 - Max 1

The head.001 Business Application Header Character Set element declares the character set, in addition to Latin, that is contained in the Business Document e.g. the pacs.008.

The Character Set element uses the UnicodeChartsCode string to declare an additional character set, for example Cyrillic (Unicode range: 0400-04FF).

Ж œ

This allows the party for which the message is addressed To to know in advance the additional character set contained within the Business Document. In this way the message can be routed to a specific application to process the Character Set or handled as an exception if the Character Set is not appropriate for that business transaction.

ݒ

图

Extending character sets is not intended in CBPR+ from the initial implementation of the service. This element is intended for use once extended character sets are implemented, whereby the string represented in this element can enable any necessary network validations, such as a closed user group for that character set.

---

<!-- ELEMENT 27 -->
head.001 Business Application Header - From

Min 1 - Max 1

The head.001 Business Application Header From element identifies the BIC of the party who created the Business Document (e.g. pacs.008). Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

A choice must be made for the BIC depending on the party it represents.

Financial Institution Identification which identifies a Financial Institution, and may be further complemented with

Clearing System Member Identification

LEI

as an additional identification.

---

<!-- ELEMENT 28 -->
head.001 Business Application Header - To

The head.001 Business Application Header To element identifies the BIC of the party who will ultimately process the Business Document (e.g. pacs.008) Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

A choice must be made for the BIC depending on the party it represents.

Financial Institution Identification which identifies a Financial Institution, and may be further complemented with

Clearing System Member Identification

LEI

as an additional identification.

---

<!-- ELEMENT 29 -->
head.001 Business Application Header - Business Message Identifier

Min 1 - Max 1

The head.001 Business Application Header Business Message Identifier element contains the Message Identification captured within the Business Document's Group Header. The content of this element should match the Business Document to avoid incorrect routing by the recipient.


## Cel schematu
Celem schematu jest zilustrowanie mechanizmu korelacji i powiązania pomiędzy warstwą transportową/opakowaniową (**Business Application Header**) a właściwą treścią biznesową wiadomości (**Business Document**) w standardzie ISO 20022. Schemat pokazuje, w jaki sposób unikalny identyfikator służy do jednoznacznego przypisania nagłówka aplikacji do konkretnego dokumentu biznesowego, co jest kluczowe dla zapewnienia integralności danych i możliwości śledzenia (traceability) wiadomości w systemach bankowych i finansowych.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Business Application Header (BAH)** | Standardowy nagłówek aplikacji biznesowej (często utożsamiany z formatem `head.001`). Pełni rolę "koperty", która zawiera informacje niezbędne do rutowania, autoryzacji i kontroli wiadomości, niezależnie od jej treści biznesowej. |
| **Business Message Identifier** | Unikalny identyfikator przypisany w nagłówku BAH. Służy do identyfikacji całej jednostki komunikacyjnej w systemach przesyłowych. |
| **Business Document** | Właściwa treść biznesowa (payload), np. zlecenie przelewu (`pain`), potwierdzenie płatności (`pacs`) czy informacja o saldzie (`camt`). Jest to "list" umieszczony wewnątrz "koperty" BAH. |
| **Group Header** | Nagłówek grupy znajdujący się wewnątrz dokumentu biznesowego. Zawiera dane wspólne dla wszystkich transakcji zgrupowanych w jednym dokumencie. |
| **Message Identification** | Unikalny identyfikator nadany bezpośrednio w treści dokument


---

<!-- ELEMENT 30 -->
head.001 Business Application Header - Message Definition Identifier

Min 1 - Max 1

The head.001 Business Application Header Message Definition Identifier element contains the name of the Business Document. The content of this element should match the Business Document to avoid incorrect routing by the recipient.


## Cel schematu
Celem niniejszego schematu jest zilustrowanie struktury i zależności pomiędzy warstwą transportową/rutującą a warstwą merytoryczną wiadomości w standardzie ISO 20022. Diagram pokazuje mechanizm identyfikacji typu wiadomości, zapewniając spójność między nagłówkiem aplikacyjnym (BAH) a właściwym dokumentem biznesowym, co jest kluczowe dla poprawnego procesowania i walidacji komunikatów finansowych w systemach bankowych.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Business Application Header (BAH)** | Biznesowy nagłówek aplikacyjny. Jest to ustandaryzowany "kopertowy" element wiadomości, który zawiera informacje niezbędne do rutowania i obsługi komunikatu, niezależnie od jego treści merytorycznej. |
| **Message Definition Identifier** | Identyfikator definicji wiadomości. Pole w BAH, które precyzyjnie określa, jaki typ dokumentu biznesowego znajduje się wewnątrz przesyłki. |
| **pacs.009.001.08** | Kon


---

<!-- ELEMENT 31 -->
head.001 Business Application Header - Business Service

Min 1 - Max 1

The head.001 Business Application Header Business Service element is used to identify administered services on the SWIFT network. The data represented in this elements is referred to as a Usage Identifier . For CBPR+ examples are provided below, these values may be used together with the Message Definition Identifier to determine routing rules to specific applications without having to open the business document.

| MessageDefinitionIdentifier   | BusinessService       | BusinessUse Case                              |
|-------------------------------|-----------------------|-----------------------------------------------|
| pacs.009.001.08               | swift.cbprplus.cov.01 | Financial Institution (Cover) Credit Transfer |
| pacs.009.001.08               | swift.cbprplus.01     | Serial Financial Institution Credit Transfer  |
| pacs.008.001.08               | swift.cbprplus.stp.01 | STPCustomerCreditTransfer                     |

The Business Service is also intended to be incremented for the same message version, when an updated Usage Guideline is released. For example a new restriction is applied to the pacs.009.001.08 Usage Guideline, the Business Service swift.cbprplus.cov.02 and swift.cbprplus.02 will be used to reflect these new Guidelines and allow network validate.

Business Service Note : when a new message (Message Definition Identifier) version is introduced the numeric value for the Business Service is reset.

---

<!-- ELEMENT 32 -->
head.001 Business Application Header - Business Service

| Message Definition Identifier       | Business Service      |
|-------------------------------------|-----------------------|
| pain.001.001.09                     | swift.cbprplus.02     |
| pain.002.001.10                     | swift.cbprplus.02     |
| pain.008.001.03                     | swift.cbprplus.01     |
| pacs.002.001.10                     | swift.cbprplus.02     |
| pacs.003.001.08                     | swift.cbprplus.01     |
| pacs.004.001.09                     | swift.cbprplus.02     |
| pacs.008.001.08                     | swift.cbprplus.02     |
| pacs.008.001.08 (STP/STP EU)        | swift.cbprplus.stp.02 |
| pacs.009.001.08 (advice)            | swift.cbprplus.adv.02 |
| pacs.009.001.08 (core)              | swift.cbprplus.02     |
| pacs.009.001.08 (cov)               | swift.cbprplus.cov.02 |
| pacs.010.001.03                     | swift.cbprplus.02     |
| pacs.010.001.03 (Margin Collection) | swift.cbprplus.col.01 |
| camt.029.001.09                     | swift.cbprplus.02     |
| camt.052.001.08                     | swift.cbprplus.02     |
| camt.053.001.08                     | swift.cbprplus.02     |
| camt.054.001.08                     | swift.cbprplus.02     |
| camt.055.001.08                     | swift.cbprplus.01     |
| camt.056.001.08                     | swift.cbprplus.02     |
| camt.057.001.06                     | swift.cbprplus.02     |

| Message Definition Identifier   | Business Service   |
|---------------------------------|--------------------|
| camt.058.001.08                 | swift.cbprplus.01  |
| camt.060.001.05                 | swift.cbprplus.02  |
| camt.107.001.01                 | swift.cbprplus.01  |
| camt.108.001.01                 | swift.cbprplus.01  |
| camt.109.001.01                 | swift.cbprplus.01  |

The data represented in the Business Service, together with the Message Definition Identifier has a number of roles, in addition to the routing rules referred to on the previous page.

This data value:

Identifiers explicitly the Usage Guideline within a library of guideline. For example an application may have various pacs.008 libraries within a collection, for which only one of these is appropriate to be used to identify data requirements or perform validation.

is also populated in the Request Header of the InterAct message in the Request Sub Type element which allow the service (FINplus for CBPR+) to apply network validation rules.

---

<!-- ELEMENT 33 -->
head.001 Business Application Header - Market Practice

Min 0 - Max 1

The head.001 Business Application Header Market Practice element is used to identify administered services on the SWIFT network.

This element is currently not foreseen to be used by CBPR+.

---

<!-- ELEMENT 34 -->
head.001 Business Application Header - Creation Date

Min 1 - Max 1

The head.001 Business Application Header Creation Date captures the date and time which the Business Application Header was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 35 -->
head.001 Business Application Header - Copy Duplicate

Min 0 - Max 1

The head.001 Business Application Header Copy Duplicate indicator is used as a choice to identify scenarios where a message was previously sent.

COPY is used to represent a copy of a message being sent to an additional party. This scenario is only associated with camt reporting messages.

DUPL is used to represent a duplicate of a previously sent camt reporting message. To receive a duplicate payment message, Interact message retrieval should be utilised.

CODU is used to represent a duplicate of a previously sent COPY message. This scenario is only associated with camt reporting messages.

Copy Duplicate

---

<!-- ELEMENT 36 -->
head.001 Business Application Header - Possible Duplicate

Min 0 - Max 1

The head.001 Business Application Header Possible Duplicate element is used as a flag to indicate that if the party who will ultimately process the Business Document (e.g. pacs.008) received the original, then it should perform necessary actions to avoid processing this Business Message again.

This element is represented by a Yes/No Boolean, whereby true represent this is a Possible Duplicate.

It is not necessary to represent false (No) the absence of this optional element itself indicates that this is not considered a Possible Duplicate.

The FINplus Technical Header has an element PDIndicator (Possible Duplicate Indicator) which uses a Yes/No Boolean. This may be populated by the network interface to identify a message it considers may be a possible duplicate.

Possible Duplicate

---

<!-- ELEMENT 37 -->
head.001 Business Application Header - Priority

Min 0 - Max 1

The head.001 Business Application Header Priority element allows a choice of Business Message Priority Code to indicate the priority which may be applied to the business message.

This element must represent the priority code of the business document (instance) which is only applicable for pacs messages. The pacs message priority is captured in the Payment Type Priority/Instruction Priority.

---

<!-- ELEMENT 38 -->
head.001 Business Application Header - Related

Min 0 - Max 1

The head.001 Business Application Header Related nested element enables the capture of the Business Application Header from a related Business Document. For example, in a pacs.004 Payment Return the Related Business Application Header from the original message can be included. This could allow the receiver to apply specific routing to the message, based on the related information i.e., return of a pacs.009 cov may be routed to different payment engine than a core pacs.009.

The following elements are nested within the Related element. Where used these contain the original data from the related Business Application Header:

From

To

Business Message Identifier Message Definition Identifier

Business Service

Creation Date

Copy Duplicate Priority

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 1 - Max 1

Min 1 - Max 1

Min 1 - Max 1

Min 1 - Max 1

Min 1 - Max 1

Related

---

<!-- ELEMENT 39 -->
Payment Initiation - Messages index

pain.001 Interbank Customer Credit Transfer initiation pain.002 - Interbank Customer Payment Status Report pain.008 - Customer Direct Debit Initiation

---

<!-- ELEMENT 40 -->
Interbank Customer Credit Transfer Initiation

---

<!-- ELEMENT 41 -->
High level pain.001 comparison with legacy MT 101

ISO 20022 message element

Group Header

Message Identification

Initiating Party - where different from Debtor

Forwarding Agent

Payment Information

Payment Information Identification

Requested Execution Date

Debtor

Debtor Agent

Credit Transfer Transaction Information

Payment Identification

Amount

Charge Bearer

Creditor Agent

Creditor

MT Field Name & (Tag option)

Sequence A General Information :

Sender's Reference (Field 20)

Instructing Party (Field 50 C or L)

Message Sender in a 'relay' scenario

Sequence A General Information :

Customer Specified Reference (Field 21R)

Requested Execution Date (Field 30)

Ordering Customer (Field 50 F, G or H)*

Account Servicing Institution (Field 52 A or C)*

Sequence B Transaction Details :

Transaction Reference (Field 21)

Currency/Transaction Amount (Field 32B)

Details of Charges (Field 71A)

Account With Institution (Field 57 A, C or D)

Beneficiary (Field 59 no letter, A or F)

*or in Sequence B - Transaction Detail

---

<!-- ELEMENT 42 -->
pain.001 Interbank Customer Credit Transfer Initiation


## Cel schematu
Schemat przedstawia strukturę logiczną i hierarchiczną wiadomości **pain.001**, która w standardzie ISO 20022 służy do inicjowania przelewu kredytowego przez klienta (Customer Credit Transfer Initiation). Celem tego diagramu jest zilustrowanie sposobu organizacji danych wewnątrz pliku płatniczego – od informacji ogólnych, przez dane grupowe, aż po szczegóły pojedynczych transakcji. Pozwala to na zrozumienie, jak systemy bankowe i korporacyjne interpretują instrukcje płatnicze przesyłane w formacie XML.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **pain.001** | Identyfikator typu wiadomości ISO 20022 (Payment Initiation). Jest to instrukcja płatnicza wysyłana przez dłużnika do swojego banku w celu wykonania jednego lub wielu przelewów. |
| **Group Header** | Nagłówek grupy. Zawiera dane wspólne dla całego pliku/wiadomości, takie jak identyfikator wiadomości, data i godzina utworzenia oraz informacje o nadawcy pliku. Służy do kontroli integralności całej paczki danych. |
| **Payment Information** | Informacje o płatności. Sekcja zawierająca dane wspólne dla grupy transakcji (np. ten sam rachunek dłużnika, ta sama data wykonania lub ten sam typ przelewu), co pozwala na grupowanie wielu zleceń w jedną partię. |
| **Credit Transfer Transaction Information** | Szczegółowe informacje o pojedynczej transakcji przelewu kredytowego. Zawiera dane unikalne dla każdego odbiorcy, takie jak kwota przelewu, numer rachunku odbiorcy (IBAN), kod BIC banku oraz tytuł płatności. |

## Logika i relacje
Schemat obrazuje hierarchiczną strukturę typu "rodzic-dziecko" (nesting), która odzwierciedla logikę biznesową procesu masowych płatności:

1.  **Poziom Globalny (`pain.001`)**: Jest to najwyższy poziom opakowania całej komunikacji.
2.  **Relacja 1:1 (`Group Header`)**: Każda wiadomość `pain.001` musi posiadać jeden nagłówek grupy, który definiuje kontekst całego pliku.
3.  **Relacja 1:N (`Payment Information`)**: Jeden plik może zawierać wiele bloków informacji o płat


The pain.001 message is composed of three blocks:

Group Header contains a set of characteristics that relates to all individual transaction.

Payment Information contains a set of characteristics that relates to the debit side of the transaction, such as Debtor and Debtor Agent.

Credit Transfer Transaction Information contains, among others, elements related to the credit side of the transaction, such as Creditor and Creditor Agent.

Payment messages in a many-to-many payment are considered as a single transaction.

---

<!-- ELEMENT 43 -->
High Level serial message flow: Payment Initiation 'Relay'

pain.001


## Cel schematu
Schemat przedstawia kompletny proces biznesowy i techniczny przelewu płatniczego (Customer Credit Transfer) w standardzie ISO 20022. Jego celem jest zilustrowanie pełnego cyklu życia instrukcji płatniczej – od momentu jej zainicjowania przez dłużnika, poprzez pośredników i banki rozliczeniowe, aż po powiadomienie wierzyciela o wpływie środków. Schemat obrazuje transformację komunikatów między różnymi poziomami (klient $\rightarrow$ bank $\rightarrow


FINplus Customer Credit Transfer Initiation  message is sent by the Initiating  Party to the Forwarding Agent or the Debtor Agent.  It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

Relay : The pain.001 message is sent by the Initiating  party (the Debtor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.001 message to the Debtor Agent

A Payment Initiation Rulebook, available in the Standards Documentation Centre, replaces the legacy MT Request for Transfer Service Level Agreement.

Noting in CGI-MP a pain.001 may also be sent by the Initiating Party/Debtor directly to the Debtor Agent which is outside of the scope of CBPR+, however the CBPR+ FINplus pain.001 message is interoperable with CGI-MP.

---

<!-- ELEMENT 44 -->
High Level serial message flow: Payment Initiation 'Authorised Party Initiation'

pain.001


## Cel schematu
Schemat przedstawia kompletny przepływ informacji i środków pieniężnych w procesie przelewu płatniczego zgodnie ze standardem ISO 20022. Ilustruje on tzw. "ścieżkę pieniądza" (payment journey) od momentu zlecenia przelewu przez nadawcę, poprzez pośrednictwo instytucji finansowych (agentów), aż do zaksięgowania środków u odbiorcy końcowego. Schemat ten definiuje, jakie konkretne typy wiadomości XML są wykorzystywane na każdym etapie komunikacji między uczestnikami procesu.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Initiating Party** | Strona inicjująca – podmiot (np. klient biznesowy lub osoba prywatna), który zleca wykonanie przelewu. |
| **Debtor Agent** | Agent dłużnika – instytucja finansowa (bank), w której stronę inicjująca posiada rachunek i która realizuje zlecenie płatności. |
|


This use case may not apply to all Financial Institution, depending on the products and service provided by that Financial Institution to their customer

FINplus Customer Credit Transfer Initiation  message is sent by the Initiating  Party to the Forwarding Agent or the Debtor Agent.  It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

Authorised Party Initiation: The pain.001 message is sent by the Financial Institution  as an Initiating  Party to the Debtor Agent to initiate  a payment on behalf of the Debtor who is the account holder. For example, a FI Initiates;  a liquidity  sweep on behalf of a corporate customer or payment from the Debtor account based on Tri-party  agreement (agreement from the Debtor with the Debtor Agent to provide authority  that the Initiating  Party is authorised to execute payments from their account)

---

<!-- ELEMENT 45 -->
High Level serial message flow: Payment Initiation 'FI Payment Initiation'

pain.001


## Cel schematu
Schemat przedstawia pełny cykl życia przelewu płatniczego (Customer Credit Transfer) w standardzie ISO 20022. Jego celem jest zilustrowanie przepływu komunikatów pomiędzy dłużnikiem, instytucjami finansowymi (agentami) oraz wierzycielem. Diagram obrazuje proces inicjowania płatności, jej przesyłania przez systemy międzybankowe (w tym przez bank pośredniczący) oraz końcowego powiadomienia odbiorcy o wpłynięciu środków.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Debtor** | Dłużnik – strona zlecająca przelew, z której konta pobierane są środki. |
| **Initiating Party** | Strona inicjująca – podmiot, który technicznie wysyła zlecenie płatności (może być to sam dłużnik lub np. jego księgowy/skarbnik). |
| **Debtor Agent** | Bank Dłużnika (Bank A) – instytucja finansowa obsługująca nadawcę i odpowiedzialna za pierwszą walidację zlecenia.


Interbank  Customer Credit Transfer Initiation  message is sent by the Initiating  Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

Financial Institution  Payment Initiation (to non-FI) : The pain.001  message is sent by the Financial Institution  as both the Debtor and Initiating  Party to initiate a payment from their account with the Debtor Agent  to move funds to a non-Financial  Institution Creditor

---

<!-- ELEMENT 46 -->
pain.001 Interbank Customer Credit Transfer Initiation - Core Party Descriptions

The following descriptions are defined in the ISO 20022 Standard for core parties participating in an Interbank Customer Credit Transfer Initiation relationship.

Forwarding Agent 'Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution'. Applicable for pain.001 use case 1 only

Initiating Party 'Party that initiates the payment.' which may be the Debtor or a Party acting on behalf of the Debtor e.g., the Agent initiating a liquidity sweep service

Debtor Agent 'Financial institution servicing an account for the debtor.'

Debtor 'Party that owes an amount of money to the (ultimate) creditor.'

Creditor Agent 'Financial institution servicing an account for the creditor.'

Creditor 'Party to which an amount of money is due.'

---

<!-- ELEMENT 47 -->
Group Header

---

<!-- ELEMENT 48 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Message Identification

Min 1 - Max 1

Each ISO20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For the Payment Initiation (pain) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

Each transaction's Credit Transfer Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor or authorized third party) of the pain.001.

---

<!-- ELEMENT 49 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Creation  Date Time

Min 1 - Max 1

The pain.001 message Creation Date Time captures the date and time which the message was created.

It is defined by ISO Date Time with mandatory date and time components expressed in the following formats:

Universal  Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2 nd option). Otherwise use UTC time (1 st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

---

<!-- ELEMENT 50 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Authorisation

Min 0 - Max 2

The pain.001 message Authorisation allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The Authorisation uses an embedded code set or free text form. It has no exact equivalent in the legacy MT payment message, however, the Authorisation (Field 25) could be considered as a similar comparison.

| Code   | Description                      | Description                                                                                                                    |
|--------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ILEV   | Instruction Level Authorisation  | File requires all customer transactions to be authorised or approved.                                                          |
| FDET   | File Level Authorisation Details | Additional file level approval, with the ability to view both the payment information block and supporting transaction detail. |
| FSUM   | File LevelAuthorisationSummary   | Additional file level approval, with the ability to view only the payment information block.                                   |
| AUTH   | PreAuthorised File               | File has been pre-authorised or approved within the originating customer environment and no further approval is required.      |

For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.

---

<!-- ELEMENT 51 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Number  of Transactions

Min 1 - Max 1

The pain.001 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 52 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Initiating  Party


## Cel schematu
Schemat przedstawia model ról w procesie inicjowania instrukcji płatniczej zgodnie ze standardem ISO 20022. Jego celem jest zdefiniowanie podmiotów zaangażowanych w etap nadawczy transakcji oraz określenie, kto ma prawo zainicjować przelew i do kogo ta instrukcja jest kierowana w pierwszej kolejności przed trafić do systemu rozliczeń. Ilustruje on oddzielenie roli właściciela środków od roli podmiotu uprawnionego do dysponowania tymi środkami.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Initiating Party** | Strona inicjująca – ogólne określenie grupy podmiotów, które rozpoczynają proces przesyłania instrukcji płatniczej. Obejmuje ona zarówno dłużnika, jak i ewentualnych pełnomocników. |
| **Debtor** | Dłużnik – podmiot, z którego rachunku mają zostać pobrane środki pieniężne. W kontekście schematu może to być osoba fizyczna lub organizacja korzystająca z usług banku. |
| **Authorised Party** | Strona uprawniona – podmiot (np. agent płatniczy, system treasury, księgowy), który posiada formalne uprawnienie do inicjowania instrukcji w imieniu Dłużnika. |
| **Forwarding Agent / FI** | Agent przekazujący / Instytucja Finansowa (Financial Institution) – bank lub inny dostawca usług płatniczych, który odbiera instrukcję od strony inicjującej i przesyła ją dalej do odpowiedniego systemu rozliczeniowego. |

## Logika i relacje
Logika biznesowa schematu opiera się na przepływie instrukcji finansowej z poziomu klienta do infrastruktury bankowej:

1.  **Grupowanie (Initiating Party):** Schemat zakłada, że proces inicjacji może być realizowany przez samego **Dłużnika (Debtor)** lub przez zewnętrzny podmiot uprawniony (**Authorised Party**). Obie te role tworzą razem tzw. Stronę Inicjującą.
2.  **Relacja Uprawnień:** Istnieje zależność między Dłużnikiem a Stroną Uprawnioną – Author


For the second and the third use case, BIC of the Initiating Party is required.

Min 1 - Max 1

The Initiating Party can either be the Debtor or an Authorised Party who initiates payment transactions on behalf of the Debtor . The Initiating Party can be, for example, the Head Office which has the authority to debit the account of its subsidiary. In the centralization model, the Initiating Party can also be a payment factory or shared service center or third-party agent, which has authority to send the message on behalf of the Debtor .

Therearethree common use casesin the context of interbank pain.001 message:

Relay : The Initiating Party , which is either the Debtor themselves or authorised party, sends the pain.001 message to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.001 message to the Debtor Agent . This is commonly known as a relay scenario. Whereby the Forwarding Agent is performing a technical role in the payment transaction, they wouldnot be represented in the payment, clearing and settlement message.

Authorised Party : The Initiating Party is the Financial Institution which has the authority to send the pain.001 message on behalf of the Debtor , e.g., multi-bank liquidity sweeps.

Financial Institution Payment Initiation : The Initiating Party is the Financial Institution which is the Debtor who initiate a payment from their account to move funds to a non-Financial Institution Creditor

---

<!-- ELEMENT 53 -->

## Cel schematu
Celem tego schematu jest zdefiniowanie struktury danych oraz reguł biznesowych dotyczących elementu **Initiating Party** (Strona Inicjująca) w wiadomości `pain.001` (Interbank Customer Credit Transfer Initiation). Schemat ten określa, jakie informacje muszą zostać dostarczone, aby jednoznacznie zidentyfikować podmiot, który zleca przelew bankowy, oraz wskazuje zależności między poszczególnymi polami danych w zależności od roli tej strony.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Initiating Party** | Podmiot inicjujący proces przelewu; może nim być dłużnik (Debtor) lub upoważniona strona trzecia. |
| **Debtor** | Dłużnik – strona, z której rachunku mają zostać pobrane środki. |
| **Authorised Party / Financial Institution** | Upoważniona strona lub instytucja finansowa, która w imieniu dłużnika inicjuje zlecenie płatności. |
| **Name** | Pełna nazwa/imię i nazwisko strony inicjującej; pole obowiązkowe, jeśli podano adres pocztowy. |
| **Postal Address** | Strukturalny adres pocztowy strony inicjującej. |
| **Identification** | Element zawierający unikalne identyfikatory strony (np. BIC, LEI


---

<!-- ELEMENT 54 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Forwarding  Agent

The Forwarding Agent is mandatory in a relay scenario whereby the Initiating Party (the Debtor or authorised third party) has to provide Business  Identifier Code (BIC FI) of the Forwarding Agent in the original pain.001 message. The Forwarding Agent acts as a concentrating  financial institution  and forwards the pain.001 message to the Debtor Agent for execution.

Other options to identify the Forwarding Agent include:

Clearing System Member ID

LEI (Legal Entity Identifier)


## Cel schematu
Celem tego schematu jest zdefiniowanie struktury identyfikacji instytucji finansowej w standardzie ISO 20022. Ilustruje on koncepcję "wyboru" (choice), pokazując, że podmiot finansowy może być zidentyfikowany za pomocą różnych, ustandaryzowanych identyfikatorów, w zależności od kontekstu transakcji, wymagań regulatora lub specyfiki systemu rozliczeniowego. Rozwiązuje on problem braku jednolitego globalnego identyfikatora, oferując zestaw alternatywnych metod jednoznacznej identyfikacji uczestników ruchu finansowego.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Financial Institution Identification** | Główny element (kompozyt), który służy do jednoznacznego określenia tożsamości instytucji finansowej uczestniczącej w procesie płatności lub komunikacji finansowej. |
| **BICFI** | Business Identifier Code for Financial Institutions. Jest to standardowy kod ISO 9362 (często nazywany kodem SWIFT), który identyfikuje konkretną instytucję finansową w sieci globalnej. |
| **Clearing System Member Id** | Unikalny numer członka systemu rozliczeniowego. Jest to identyfikator nadawany bankowi przez operatora konkretnego systemu kompensacyjnego lub rozliczeniowego (np. system RTGS). |
| **Clearing System Id** | Kod identyfikujący sam system rozliczeniowy. Jest on niezbędny, aby nadać kontekst dla `Clearing System Member Id`, ponieważ jedna instytucja może mieć różne numery członka w różnych systemach rozliczeniowych. |
| **LEI** | Legal Entity Identifier. Globalny, 20-znakowy kod alfanumeryczny (zgodny z ISO 17442), który służy do identyfikacji podmiotów prawnych uczestniczących w transakcjach finansowych na całym świecie. |
| **Various sub-element** | Pozostałe, specyficzne elementy identyfikacyjne, które mogą być wymagane w zależności od jurysdykcji lub konkretnego standardu wiadomości (np. lokalne numery licencyjne, kody krajowe). |

## Logika i relacje
Schemat przedstawia strukturę hierarchiczną o charakterze wyboru (**choice**). 

1. **Relacja Nadrzędna**: Punktem wyjścia jest `Financial Institution Identification`. Wszystkie pozostałe elementy są jego rozwinięciem.
2. **Logika Alternatywy (OR)**: Elementy takie jak BICFI, LEI czy Clearing System Member Id są alternaty


For the use cases of Authorised Party initiation and FI payment initiation, Forwarding Agent is not required.

---

<!-- ELEMENT 55 -->
Payment Information

---

<!-- ELEMENT 56 -->
Postal  Address  - Structured  versus Unstructured.

The CBPR+ pain.001 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognise that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory.

As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message.

Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used.

CBPR+ payments HVPS+ payments


## Cel schematu
Celem schematu jest zilustrowanie procesu inicjowania przelewu płatniczego w standardzie ISO 20022 oraz pokazanie, jak dane wprowadzone przez klienta (w formie ustrukturyzowanej lub nieustrukturyzowanej) są przetwarzane przez instytucję finansową i przekazywane dalej do różnych systemów rozliczeniowych. Schemat obrazuje przepływ od momentu wysłania instrukcji płatniczej (`pain.001`) do końcowego rodzaju przelewu, z uwzględnieniem obowiązujących standardów rynkowych (CGI-MP, CBPR+, HVPS+).

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **pain.001** | Standardowa wiadomość ISO 20022 "Customer Credit Transfer Initiation". Jest to instrukcja płatnicza przesyłana przez klienta (zleceniodawcę) do swojego banku w celu zainicjowania przelewu. |
| **CGI-MP** | *Common Global Implementation - Market Practice*. Zbiór wspólnych wytycznych implementacyjnych, które ujednolicają sposób stosowania standardów ISO 20022 przez różne instytucje finansowe na świecie. |
| **CBPR+** | *Cross-Border Payments and Reporting Plus*. Globalne wytyczne dotyczące płatności transgranicznych (oparte na ISO 20022), mające na celu ujednolicenie formatów danych


---

<!-- ELEMENT 57 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Payment  Information  Identification

Min 1 - Max 1

The Interbank Customer Credit Transfer Initiation Payment Information Identification provides a mandatory element to identify the payment initiation.

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions.

For single transactions in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header.

---

<!-- ELEMENT 58 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Payment  Method

Min 1 - Max 1

The pain.001 message Payment Method specifies the means of payment that will be used to move the amount of money. One of the following payment method codes must be used:

| Code   | Name            | Definition                                                                                  |
|--------|-----------------|---------------------------------------------------------------------------------------------|
| CHK    | Cheque          | Written order to a bank to pay a certain amount of money from one person to another person. |
| TRF    | Credit Transfer | Transfer of an amount of money in the books of the account servicer.                        |

---

<!-- ELEMENT 59 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Payment  Type Information

Min 0 - Max 1

Payment Type Information provides a set of optional elements where the payment type

Payment Type Information

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

Anested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored.

Local Instrument

Anested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, INST - Instant Credit Transfer for SEPA Service Level.

Min 0 - Max 1

Anested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends.

Payment Information

Payment Type Information

Payment Type Information  at Payment Information  Level and Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally  determined.

The pain message can be described.

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the processing priority.

---

<!-- ELEMENT 60 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Requested  Execution  Date

Min 1 - Max 1

The pain.001 message mandatory Requested Execution Date element, captures the date and time at which the initiating  party requests the clearing agent to process the payment.

It is the date on which the debtor's account is debited. If payment by cheque, the date when the cheque  must be generated by the bank. It is defined by either ISO Date expressed in the YYYY-MM-DD format or ISO Date Time below:

Universal  Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2 nd option). Otherwise use UTC time (1 st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

---

<!-- ELEMENT 61 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Pooling  Adjustment  Date

Min 0 - Max 1

The pain.001 message optional Pooling Adjustment Date element, is used for the correction of the value date of a cash pool movement  that has been posted with a different value date.

It is defined by ISO Date expressed in the YYYY-MM-DD format

This element is not widely used in the payment industry. For the use case of interbank, it is even less likely to be utilized.

---

<!-- ELEMENT 62 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Debtor

The ISO 20022 pain messages describes the party whose account is debited for a transaction as the Debtor . The Debtor sub elements describe the Debtor in greater detail. Min 1 - Max 1


## Cel schematu
Celem tego schematu jest zdefiniowanie **strukturalnej budowy adresu pocztowego (`PostalAddress`)** zgodnie ze standardem ISO 20022. Schemat ten służy do ujednolicenia sposobu przesyłania danych adresowych w międzynarodowym obrocie finansowym. Zamiast przesyłać adres jako jeden ciąg tekstu (tzw. *unstructured address*), standard narzuca rozbicie go na konkretne komponenty (tzw. *structured address*). Pozwala to systemom bankowym na automatyczną walidację danych, dokładniejszą weryfikację przeciwdziałania praniu pieniędzy (AML) oraz eliminuje błędy wynikające z różnic w formatach adresów w różnych krajach.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Postal Address** | Główny element (kontener), który grupuje wszystkie informacje niezbędne do dostarczenia przesyłki lub identyfikacji fizycznej lokalizacji podmiotu. |
| **Department** | Nazwa działu lub jednostki organizacyjnej wewnątrz instytucji/firmy. |
| **Sub Department** | Poddział lub mniejsza jednostka w ramach głównego działu. |
| **Street Name** | Oficjalna nazwa ulicy, alei, placu itp. |
| **Building Number** | Numer budynku (numer domu/kamienicy). |
| **Building Name** | Nazwa budynku (stosowana często w centrach biznesowych lub biurowcach). |
| **Floor** | Piętro, na którym znajduje się odbiorca. |
| **Post Box** | Numer skrzynki pocztowej (P.O. Box). |
| **Room** | Numer pokoju lub konkretne pomieszczenie w budynku. |
| **Post Code** | Kod pocztowy przypisany do danej lokalizacji. |
| **Town Name** | Nazwa miejscowości, miasta lub wsi. |
| **Town Location Name** | Specyficzna nazwa części miasta lub obszaru lokalnego. |
| **District Name** | Nazwa dzielnicy lub dystryktu administracyjnego. |
| **Country


Nested element capturing either structured or unstructured Debtor address details.

Note: Structured address is strongly recommended with mandatory Town Name and Country

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

In order to process the pain.001 interbank into a CBPR+ payment, CBPR+ requires either structured or unstructured postal address.


## Cel schematu
Celem tego schematu jest zdefiniowanie struktury danych i wymagań informacyjnych dla podmiotu pełniącego rolę **Dłużnika (Debtor)** w standardzie ISO 20022. Ilustruje on, jakie atrybuty są niezbędne do jednoznacznej identyfikacji strony inicjującej płatność lub zobowiązanej do zapłaty, co ma kluczowe znaczenie dla procesów KYC (Know Your Customer), AML (Anti-Money Laundering) oraz zapewnienia poprawności księgowania transakcji w systemach finansowych.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Debtor** | Strona transakcji, która jest dłużnikiem (płatnikiem) – podmiot, z którego konta odpływają środki. |
| **Name** | Oficjalna nazwa lub imię i nazwisko dłużnika. Jest elementem obowiązkowym w przypadku braku identyfikatora BIC. |
| **Postal Address** | Adres pocztowy dłużnika, służący do jego fizycznej lokalizacji i weryfikacji. |
| **Identification** | Zbiór unikalnych identyfikatorów przypisanych do dłużnika (np. numery rejestrowe, kody krajowe), które pozwalają na jednoznaczną identyfikację podmiotu bez polegania wyłącznie na nazwie. |
| **Country of Residence** | Opcjonalny element określający kod kraju rezydencji dłużnika zgodnie ze standardem ISO (np. PL, US, DE). |
| **BIC identifier** | Bank Identifier Code – międzynarodowy kod identyfikujący instytucję finansową; w kontekście schematu jego obecność może modyfikować wymóg podania pełnej nazwy. |

## Logika i relacje
Schemat przedstawia model hierarchiczny (gwiazdowy), w którym centralnym punktem jest encja **Debtor**. Wszystkie pozostałe elementy są atrybutami opisującymi ten podmiot. Logika biznesowa opiera się na następujących zależnościach:

1.  **Zależność warunkowa (Name $\leftrightarrow$ BIC):** Istnieje ścisła relacja między nazwą a identyfikatorem BIC. Jeśli dłużnik nie jest zidentyfikowany za pomocą kodu BIC, pole **Name** staje się obowiązkowe. Jest to mechanizm zabezpieczający przed anonimowością transakcji.
2.  **Uzupełnianie danych (Identification $\rightarrow$ Debtor):** Elementy identyfikacji służą do uszczegółowienia tożsamości dłużnika, eliminując ryzy


---

<!-- ELEMENT 63 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Debtor  Account

Min 1 - Max 1

The pain.001 Debtor Account is used to capture the account information  for which debit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The Debtor Account uses a variety of nested elements to capture information related to the account.

Min 1  - Max 1

Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Currency identifies the currency of the account, recommended.

Name identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

Indication of Currency of the Debtor Account is recommended in case of multi-currency accounts whereby a single account number is allocated to the Debtor Account.

63

---

<!-- ELEMENT 64 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Debtor  Agent

Min 1 - Max 1

The Debtor Agent is a static role in  the pain.001 Customer Credit Transfer Initiation. This agent maintains  a relationship  with their customers, the Debtor .

Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

For Agent Identification, BIC is preferred, alternatively Clearing Member ID together with Name and Address may be provided.

---

<!-- ELEMENT 65 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Debtor Agent Account

Min 0 - Max 1

The pain.001 Debtor Agent Account is used to capture the account information related to the Debtor Agent.

The Debtor Agent Account uses a variety of nested elements to capture information related to the account.

Min 1  - Max 1

Identification identifies the account maintained at the Account Servicing Institution

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Currency identifies the currency of the account

Name identifies the name of the account as assigned by the Account Servicing Institution

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

Debtor Agent and Creditor Agent are Financial Institutions, therefore the nested elements Name and Proxy are unlikely to be used.

---

<!-- ELEMENT 66 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Instruction  For Debtor Agent

Min 0 - Max 1

The Instruction for Debtor Agent element within the pain.001 message optionally provides information related to the processing of the payment.

The Instruction for Debtor Agent element offers a maximum  of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the Debtor Agent , depending  on bilateral agreement.

---

<!-- ELEMENT 67 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Ultimate  Debtor


## Cel schematu
Celem tego schematu jest zilustrowanie hierarchii i klasyfikacji ról uczestników w transakcji finansowej zgodnie ze standardem ISO 20022. Schemat przedstawia koncepcję "ostatecznych stron" (Ultimate Parties), co ma kluczowe znaczenie dla przejrzystości przepływów pieniężnych. Służy on rozróżnieniu między podmiotami, które bezpośrednio inicjują lub otrzymują przelew w systemie bankowym (Direct Parties), a rzeczywistymi beneficjentami lub nadawcami środków, którzy mogą znajdować się na końcach długiego łańcucha pośredników.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Ultimate Party** | Nadrzędna kategoria określająca każdą stronę transakcji, która jest rzeczywistym nadawcą lub odbiorcą środków, niezależnie od tego, czy bezpośrednio uczestniczy w komunikacji z operatorem systemu płatności. |
| **Ultimate Debtor** | Ostateczny dłużnik. Podmiot, który jest faktycznym źródłem funduszy w transakcji. Może on różnić się od "Debtora" (bezpośredniego zleceniodawcy), np. w przypadku korzystania z usług agenta płatniczego lub firmy obsługującej płatności. |
| **Ultimate Creditor** | Ostateczny wierzyciel. Podmiot, który jest faktycznym odbiorcą końcowym środków finansowych. Może on różnić się od "Creditora" (bezpośredniego odbiorcy), np. gdy środki trafiają najpierw do powiernika lub agenta rozliczeniowego. |

## Logika i relacje
Logika schematu opiera się na relacji typu **dziedziczenie/przynależność**. 

1. **Hierarchia:** `Ultimate Party` jest pojęciem abstrakcyjnym (rodzajem kategorii), do której należą zarówno `Ultimate Debtor`, jak i `Ultimate Creditor`.
2. **Relacja Biznesowa:** Schemat pokazuje, że każda transakcja finansowa w standardzie ISO 20022 dąży do zidentyfikowania obu końców łańcucha wartości. 
3. **Przepływ informacji:** W komunikatach ISO 20022 (np. w wiadomościach `pacs`), dane o tych podmiotach są przekazywane w oddzielnych blokach, aby systemy bankowe i organy nadzorcze mogły prześledzić drogę pieniądza od rzeczywistego nadawcy (`Ultimate Debtor


Min 0 - Max 1

Min 0 - Max 1

The pain.001 message introduces Ultimate Debtor and Ultimate Creditor . The Ultimate Debtor element should not be confused with an Initiating Party who may send a payment initiation request on behalf of the Debtor , for example, Payment Factory.

CBPR+ premise is that an Ultimate Debtor has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an Ultimate Creditor has no financial regulated account relationship with the corresponding Creditor.

The Ultimate Debtor and Ultimate Creditor can be identified by a combination  of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 68 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Charge  Bearer

Min 0 - Max 1

The Charge Bearer element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

| Charge Bearer   | Code   | Description   |
|-----------------|--------|---------------|
| Charge Bearer   | CRED   | Creditor      |
| Charge Bearer   | DEBT   | Debtor        |
| Charge Bearer   | SHAR   | Shared        |


## Cel schematu
Celem tego schematu jest przedstawienie mapowania (odpowiedniości) między dwoma standardami komunikatów finansowych: legacy **SWIFT MT** (konkretnie format MT 101) a nowoczesnym standardem **ISO 20022**. Ilustruje on, w jaki sposób instrukcje dotyczące tego, kto ponosi koszty transakcji (opłaty bankowe), są tłumaczone z jednego systemu na drugi podczas migracji lub współistnienia obu standardów.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **ISO 20022** | Nowoczesny, globalny standard wymiany danych finansowych oparty na XML, który zastępuje starsze formaty MT. |
| **MT 101** | Rodzaj komunikatu SWIFT (Legacy), służący do przekazywania instrukcji przelewu z klienta do banku. |
| **Charge Bearer (0.1)** | Element w standardzie ISO 20022 określający stronę, która ponosi koszty operacji płatniczej. |
| **71A: Details of Charges** | Konkretne pole w komunikacie MT, dedykowane do określenia podziału opłat za przelew. |
| **CRED (Creditor)** | Kod ISO 20022: Wskazuje, że wszystkie koszty ponosi wierzyciel (odbiorca). |
| **DEBT (Debtor)** | Kod ISO 20022: Wskazuje, że wszystkie koszty ponosi dłużnik (nadawca). |
| **SH


Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 69 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Charges  Account

Min 0 - Max 1

The pain.001 optional Charges Account element, which is used to process charges associated with a transaction.

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

This element is not widely used in the payment industry.

---

<!-- ELEMENT 70 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Charges  Account  Agent

Min 0 - Max 1

The pain.001 optional Charges Account Agent element, which is used to specify the agent that services a charges account.

Charges account agent should  only be used when the charges account agent is different from the debtor agent.

This element is not widely used in the payment industry. It should also be noted that the ChargesAccountAgentRule inherited from the base message should be ignored as the optional Branchof DebtorAgent is removed from this Usage Guideline.

---

<!-- ELEMENT 71 -->
Credit Transfer Transaction Information

---

<!-- ELEMENT 72 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Payment  Identification

Min 1 - Max 1

The pain.001 message contains Payment Identification which provides a set of elements to identify the payment of which several are mandatory elements.


## Cel schematu
Celem tego schematu jest zdefiniowanie i rozróżnienie trzech różnych mechanizmów identyfikacji płatności w standardzie ISO 20022 (konkretnie w ramach informacji o transakcji przelewu kredytowego – *Credit Transfer Transaction Information*). Schemat ilustruje, które identyfikatory służą do celów technicznych/operacyjnych między bankami, które są przeznaczone dla klientów końcowych, a który pełni rolę globalnego, unikalnego klucza śledzenia transakcji.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Payment Identification** | Nadrzędna koncepcja identyfikacji płatności; zestaw pól służących do jednoznacznego rozpoznania transakcji w systemie finansowym. |
| **Instruction Identification** | Identyfikator instrukcji; referencja typu "punkt-do-punkt" (point-to-point), używana do komunikacji między bezpośrednio współpracującymi instytucjami finansowymi. |
| **End to End Identification** | Identyfikator koniec-koniec; unikalna referencja nadana przez dłużnika, która musi przejść przez cały łańcuch płatności bez zmian, aż do wierzyciela. |
| **UETR (Unique End-to-End Transaction Reference)** | Unikalny identyfikator transakcji koniec-koniec; techniczny klucz o zasięgu globalnym, służący do śledzenia statusu płatności w czasie rzeczywistym. |
| **Min 0 – Max 1** | Kardynalność pola: element jest opcjonalny (może wystąpić zero razy lub maksymalnie jeden raz). |
| **Min 1 – Max 1** | Kardynalność pola: element jest obowiązkowy (musi wystąpić dokładnie jeden raz). |
| **


Payment Identification

---

<!-- ELEMENT 73 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Payment  Type Information

Min 0 - Max 1

The pain.001 Payment Type Information provides a set of optional elements where the payment type can be described.

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the processing priority.

Service Level

Min 0 - Max 3

Payment Type Information

Anested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored.

Local Instrument

Anested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, INST - Instant Credit Transfer for SEPA Service Level.

Min 0 - Max 1

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

Anested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends.

Credit Transfer Transaction Information

Payment Type Information

Payment Type Information  at the Payment Information  Level and Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally  determined.

---

<!-- ELEMENT 74 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Currency  and Amount

Min 1 - Max 1

The pain.001 nested Amount element has a choice of either Instructed Amount or Equivalent Amount to capture the amount and currency of the Customer Credit Transfer Initiation.

Instructed Amount

The Instructed Amount captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. This amount has to be transported unchanged through the transaction chain. This element is comparable with the legacy Field 33B.

The Equivalent Amount nested element captures currency and Amount of money to be moved between the Debtor and Creditor, before deduction of charges, and is expressed in the currency of the Debtor's account. The Currency Of Transfer element capture the equivalent currency to be transferred which the first agent will convert the credit transfer into.

Credit Transfer Transaction Information Currency and Amount

Instructed Amount

Equivalent Amount

---

<!-- ELEMENT 75 -->

## Cel schematu
Celem tego schematu jest zdefiniowanie struktury i przeznaczenia elementu **Exchange Rate Information** w ramach komunikatu **pain.001** (Interbank Customer Credit Transfer Initiation) standardu ISO 20022. Schemat ten ilustruje, w jaki sposób w instrukcji przelewu mają zostać przekazane szczegółowe dane dotyczące kursu wymiany walut oraz powiązanego z nim kontraktu FX, aby zapewnić transparentność i jednoznaczność rozliczeń między zleceniodawcą a bankiem.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **pain.001** | Standardowy komunikat ISO 20022 służący do inicjowania przelewów kredytowych przez klienta (Customer Credit Transfer Initiation). |
| **Exchange Rate Information** | Blok danych zawierający szczegółowe informacje o zastosowanym kursie wymiany walut oraz kontrakcie wymiany. |
| **Unit Currency** | Waluta bazowa, w której wyrażony jest kurs wymiany (np. jeśli kurs to 1 GBP = 1.20 USD, to Unit Currency jest walutą GBP). |
| **Exchange Rate** | Współczynnik/mnożnik stosowany do przeliczenia kwoty z jednej waluty na drugą; odzwierciedla cenę zakupu jednej waluty za pomocą drugiej. |
| **Rate Type** | Określenie rodzaju zastosowanego kursu wymiany (


---

<!-- ELEMENT 76 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Charge  Bearer

Min 0 - Max 1

The Charge Bearer element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'


## Cel schematu
Celem schematu jest przedstawienie mapowania (odpowiedniości) między dwoma standardami komunikatów finansowych: nowym standardem **ISO 20022** a starszym standardem **SWIFT MT** (konkretnie dla komunikatu MT 101). Schemat ilustruje, jak kody określające podmiot ponoszący koszty transakcyjne w standardzie legacy są tłumaczone na nowoczesne odpowiedniki w standardzie ISO 20022, co jest kluczowe dla zachowania spójności danych podczas migracji systemów lub współistnienia obu standardów (interoperacyjności).

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Charge Bearer (0.1)** | Element w standardzie ISO 20022 określający, która ze stron transakcji ponosi koszty operacji. |
| **ISO 20022** | Nowoczesny, globalny standard wymiany danych finansowych oparty na XML, zastępujący starsze formaty MT. |
| **MT 101** | Typ komunikatu SWIFT (Request for Transfer), służący do zlecania przelewów z konta klienta przez niego reprezentowanego agenta. |
| **71A:


Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

Credit Transfer Transaction Information

Charge Bearer

---

<!-- ELEMENT 77 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Cheque Instruction

Min 0 - Max 1

The Cheque Instruction information block contains a set of elements needed to issue a cheque. The following types of cheques are commonly  used in the market:

| Cheque Type     | Code   | Description                                                                                                                                                                                                                                                                 |
|-----------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bank Cheque     | BCHQ   | Chequedrawnon the account of the debtor's financial institution,whichis debited on the debtor's accountwhenthe chequeis issued.Thesechequesareprintedby the debtor's financial institutionand paymentis guaranteedbythe financial institution.Synonymis 'cashier's cheque'. |
| Customer Cheque | CCHQ   | Chequedrawnon the account of the debtorand debitedon the debtor's account when the chequeis cashed.Synonymis 'corporate cheque'.                                                                                                                                            |
| Draft           | DRFT   | Aguaranteedbankchequewitha future value date (do not pay before],which in commercial terms is a 'negotiatable instrument': the beneficiary canreceiveearly payment fromany bank undersubtraction of a discount. Theorderingcustomer's account is debitedon value date.      |

The Delivery Method element specifies the method to be used in delivering the cheque by the Debtor Agent . For example, a code CRCD is used to courier the cheque to the Creditor .

Credit Transfer Transaction Information

---

<!-- ELEMENT 78 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Ultimate  Debtor


## Cel schematu
Celem tego schematu jest zdefiniowanie i zobrazowanie koncepcji „ostatecznych stron” (Ultimate Parties) w ramach standardu ISO 20022. Schemat ilustruje hierarchiczną i logiczną strukturę uczestników transakcji finansowej, rozróżniając między podmiotami bezpośrednio zaangażowanymi w przesyłanie instrukcji płatniczej a podmiotami, które są faktycznymi (ekonomicznymi) nadawcami i odbiorcami środków. Jest to kluczowe z punktu widzenia przejrzystości przepływów pieniężnych oraz wymogów regulacyjnych w zakresie AML (przeciwdziałanie praniu pieniędzy) i KYC (poznaj swojego klienta).

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Ultimate Party** | Termin nadrzędny określający ostateczną stronę transakcji. Jest to podmiot, który jest rzeczywistym beneficjentem lub źródłem środków w łańcuchu płatności, niezależnie od liczby pośredników zaangażowanych w proces. |
| **Ultimate Debtor** | Ostateczny dłużnik. Podmiot, z którego fundusze faktycznie pochodzą lub który ponosi ostateczną odpowiedzialność za zapłatę, nawet jeśli instrukcję przelewu wysłał w jego imieniu agent lub inny pośrednik (np. firma windykacyjna, agent płatniczy). |
| **Ultimate Creditor** | Ostateczny wierzyciel. Podmiot, który jest faktycznym odbiorcą końcowym środków finansowych i czerpie z nich korzyść ekonomiczną, nawet jeśli środki wpłynęły najpierw na rachunek pośrednika (np. agenta rozliczeniowego lub powiernika). |

## Logika i relacje
Schemat przedstawia relację inkluzji i symetrii w procesie płatniczym:

1.  **Hierarchia:** `Ultimate Party` stanowi kategorię nadrzędną. Zarówno `Ultimate Debtor`, jak i `Ultimate Creditor` są specyficznymi instancjami "Ostatecznej Strony".
2.  **Logika przepływu:** W standardzie ISO 20022 rozróżnia się dłużnika (Debtor) od ostatecznego dłużnika (Ultimate Debtor) oraz wierzyciela (Creditor) od ostatecznego wierzyciela (Ultimate Creditor). Logika biznesowa zakłada, że w prostych transakcjach te role mogą się pokrywać. Jednak w złożonych łańcuchach płatności (np. płatności zbiorcze, rozliczenia przez agentów), schemat ten wymusza identyfikację "punktu startowego" i "punktu koń


Min 0 - Max 1

Min 0 - Max 1

The pain.001 message introduces Ultimate Debtor and Ultimate Creditor . The Ultimate Debtor element should not be confused with an Initiating Party who may send a payment initiation request on behalf of the Debtor , for example, Payment Factory.

CBPR+ premise is that an Ultimate Debtor has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an Ultimate Creditor has no financial regulated account relationship with the corresponding Creditor.

The Ultimate Debtor and Ultimate Creditor can be identified by a combination  of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

Credit Transfer Transaction Information

---

<!-- ELEMENT 79 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Intermediary  Agents

The pain.001 has three optional Intermediary Agent (1,2 and 3) elements. These agents represent the agent(s) that exist between the Debtor Agent and the Creditor Agent .

If more than one intermediary agent is present, then Intermediary Agent 1 identifies the agent between the Debtor Agent and the Intermediary Agent 2 .

If more than two intermediary agents are present, then Intermediary Agent 2 identifies the agent between the Intermediary Agent 1 and the Intermediary Agent 3 .

If Intermediary Agent 3 is present, then it identifies the agent between the Intermediary Agent 2 and the Creditor Agent .

More commonly  the ISO 9362 Financial  Institution Business  Identifier Code is considered the best practice de factor standard for 'many to many'  / correspondent banking  payments.

Other options to identify the Intermediary Agent include:

Clearing System Member ID

LEI (Legal Entity Identifier)

Name and either structured, or unstructured Postal Address

In order to process the pain.001 interbank into a CBPR+ payment, CBPR+ requires either structured or unstructured postal address.

Credit Transfer Transaction Information

Intermediary Agent 1

Intermediary Agent 2

Intermediary Agent 3

---

<!-- ELEMENT 80 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Intermediary  Agent  Account

Min 0 - Max 1

The pain.001 Intermediary Agent (1,2 and 3) Accounts are used to capture the account information related to these Agents.

The Intermediary Agent Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Account Servicing Institution.

Type uses the external Cash Account Type code list to identify the type of account. Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Intermediary Agent is a Financial Institution, therefore the nested elements Name and Proxy are unlikely to be used.

Currency identifies the currency of the account.

Name identifies the name of the account as assigned by the Account Servicing Institution.

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

Credit Transfer Transaction Information

Intermediary Agent Account 1

Intermediary Agent Account 2

Intermediary Agent Account 3

---

<!-- ELEMENT 81 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Creditor  Agent

Min 0 - Max 1

The Creditor Agent is a static roles in the pain.001 Customer Credit Transfer Initiation. This agent maintain  a relationship  with their customers, the Creditor .

Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

Credit Transfer Transaction Information

---

<!-- ELEMENT 82 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Creditor Agent Account

Min 0 - Max 1

The pain.001 Creditor Agent Account is used to capture the account information  related to the Creditor Agent .

The Creditor Agent Account uses a variety of nested elements to capture information related to the account.

Min 1  - Max 1

Identification identifies the account maintained at the Account Servicing Institution

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Currency identifies the currency of the account

Name identifies the name of the account as assigned by the Account Servicing Institution

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

Credit Transfer Transaction Information

---

<!-- ELEMENT 83 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Creditor

Min 1 - Max 1

The ISO 20022 pain messages describe the Creditor as the party whose account was credited for a transaction. The Creditor sub elements describe the Creditor in greater detail.


## Cel schematu
Schemat przedstawia strukturę danych dla elementu **Postal Address** (Adres Pocztowy) zgodnie ze standardem ISO 20022. Jego celem jest definicja tzw. **strukturyzowanego adresu**, która zastępuje tradycyjny, nieustrukturyzowany opis adresu (wolny tekst). 

Z biznesowego punktu widzenia schemat ten ma na celu:
- **Eliminację błędów** w przesyłaniu informacji o lokalizacji kontrahentów.
- **Umożliwienie automatyzacji (STP - Straight Through Processing)**, dzięki czemu systemy informatyczne mogą automatycznie walidować i przetwarzać dane bez ingerencji człowieka.
- **Zapewnienie zgodności z regulacjami KYC/AML**, gdzie precyzyjna identyfikacja fizycznej lokalizacji podmiotu jest niezbędna do przeciwdziałania praniu pieniędzy i finansowaniu terroryzmu.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Postal Address** | Główny kontener danych zawierający pełne informacje o fizycznej lokalizacji podmiotu. |
| **Department** | Nazwa jednostki organizacyjnej wewnątrz firmy/instytucji (np. Dział Księgowości). |
| **Sub Department** | Bardziej szczegółowy podział wewnątrz działu (np. Sekcja Płatności Zagranicznych). |
| **Street Name** | Nazwa ulicy, alei lub placu. |
| **Building Number** | Numer budynku/domu. |
| **Building Name** | Nazwa budynku (stosowana często w centrach biznesowych lub biurowcach).


In order to process the pain.001 interbank into a CBPR+ payment, CBPR+ requires either structured or unstructured postal address.

Mandatory Name (where a BIC identifier is not provided) by which the party is known

Nested element capturing either structured or unstructured Creditor address details.

Name

Postal Address

Note: Structured address is strongly recommended with mandatory Town Name and Country

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Optional element to capture the Creditor 's  ISO country code of residence

Country of Residence

Credit Transfer Transaction Information

Creditor

---

<!-- ELEMENT 84 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Creditor Account

Min 0 - Max 1

The pain.001 Creditor Account is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The Creditor Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1

Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Currency identifies the currency of the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

Creditor Account is not required for cheque payments.

Credit Transfer Transaction Information

---

<!-- ELEMENT 85 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Ultimate  Creditor

Min 0 - Max 1

Min 0 - Max 1

The pain.001 message introduces Ultimate Debtor and Ultimate Creditor . The Ultimate Debtor element should not be confused with an Initiating Party who may send a payment initiation request on behalf of the Debtor , for example, Payment Factory.

CBPR+ premise is that an Ultimate Debtor has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an Ultimate Creditor has no financial regulated account relationship with the corresponding Creditor.


## Cel schematu
Celem tego schematu jest zdefiniowanie i zilustrowanie koncepcji tzw. „ostatecznych stron” (Ultimate Parties) w ramach standardu ISO 20022. Schemat komunikuje hierarchiczną i kategoryczną zależność między ogólnym pojęciem strony transakcji a konkretnymi rolami, jakie te strony pełnią w przepływie finansowym. Służy on do rozróżnienia między podmiotami pośredniczącymi (np. bankami, agentami) a rzeczywistymi beneficjentami i płatnikami środków w łańcuchu płatności.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Ultimate Party** | Termin nadrzędny (abstrakcyjny) określający każdą stronę transakcji, która znajduje się na samym końcu łańcucha płatności. Jest to podmiot, który jest rzeczywistym źródłem lub ostatecznym celem środków pieniężnych, niezależnie od liczby pośredników zaangażowanych w proces. |
| **Ultimate Debtor** | Ostateczny Dłużnik. Podmiot, który faktycznie ponosi koszt płatności i z którego zasobów pochodzą środki, ale który może nie być bezpośrednim zleceniodawcą przelewu (np. firma matka zlecająca płatność w imieniu spółki córki lub klient korzystający z usług agenta płatniczego). |
| **Ultimate Creditor** | Ostateczny Wierzyciel. Podmiot, który jest rzeczywistym odbiorcą końcowym środków pieniężnych i do którego należą te fundusze, nawet jeśli przelew wpłynął najpierw na konto agenta lub instytucji pośredniczącej. |

## Logika i relacje
Schemat przedstawia strukturę kategoryzacji (dziedziczenia pojęć). Logika biznesowa opiera się na następujących zależnościach:

1.  **Relacja nadrzędności:** `Ultimate Party` stanowi wspólny mianownik dla obu pozostałych ról. Każdy `Ultimate Debtor` i każdy `Ultimate Creditor` jest z definicji `Ultimate Party`.
2.  **Opozycja funkcjonalna:** `Ultimate Debtor` i `Ultimate Creditor` reprezentują dwa przeciwstawne bieguny przepływu finansowego (źródło vs cel). 
3.  **Separacja od pośredników:** Kluczową logiką tego modelu jest odd


The Ultimate Debtor and Ultimate Creditor can be identified by a combination  of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

---

<!-- ELEMENT 86 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Instruction  For Creditor  Agent

The Instruction for Creditor Agent element within the pain.001 message optionally provides information related to the processing of the payment for the Creditor Agent.

The Instruction for Creditor Agent element offers a multiplicity  of up to 2 occurrences of information. This element enables:

the use of an embedded choice of code to describe the instruction (e.g. CHQB - Pay Creditor by Cheque)

free format instruction information

or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the Creditor Agent . It must be passed on throughout  the life cycle of the transaction until the payment reaches the Credit Agent .

Credit Transfer Transaction Information

Instruction for Creditor Agent

---

<!-- ELEMENT 87 -->
ISO 20022 Programme

Quality data, quality payments

CBPR+ User Handbook

SR 2023 Edition March 2023

---

<!-- ELEMENT 88 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Instruction  For Debtor Agent

Min 0 - Max 1

The Instruction for Debtor Agent element within the pain.001 message optionally provides information related to the processing of the payment.

The Instruction for Debtor Agent element offers a maximum  of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the Debtor Agent , depending  on bilateral agreement.

Credit Transfer Transaction Information

Instruction for Debtor Agent

---

<!-- ELEMENT 89 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Purpose

Min 0 - Max 1

The Purpose element within the pain.001 message captures the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment, e.g., IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Debtor .

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example, LIMA is classified within the Cash Management categorisation, with the Name Liquidity Management described as a Bank initiated account transfer to support zero target balance management, pooling or sweeping.

Category Purpose also captures a high-level purpose, which unlike Purpose is less granular but can trigger special processing e.g., Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

Credit Transfer Transaction Information

---

<!-- ELEMENT 90 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Regulatory  Reporting

The Regulatory Reporting block within the pain.001 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

Min 0 - Max 1

The Debit Credit Reporting Indicator utilises  an embedded choice of code to indicate whether the regulatory reporting applies to the:

DEBT (debit)

CRED (credit)

BOTH

Min 0 - Max 1

The Authority element captures the Name and Country code of the Authority/Entity requiring the regulatory reporting information.

Min 0 - Max *

The Details element provides the detail on the regulatory reporting information.

Credit Transfer Transaction Information       Regulatory Reporting

Authority

Details

---

<!-- ELEMENT 91 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Tax

Min 0 - Max 1

The pain.001 nested Tax element captures information  related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s).

This element caters for two main types of tax related payments:

Tax payment obligation that is required to be transmitted with a payment

Information that accompanies an actual payment of a tax obligation

The follow nested elements may be used to capture detailed tax information:


## Cel schematu
Schemat przedstawia strukturę logiczną (model danych) komponentu wiadomości w standardzie ISO 20022, dedykowanego do rozliczeń podatkowych lub raportowania fiskalnego. Jego celem jest zdefiniowanie zbioru atrybutów niezbędnych do prawidłowej identyfikacji płatności podatkowej, stron transakcji oraz podstawy naliczenia podatku. Ilustruje on tzw. "biznesowy obiekt danych", określając, jakie informacje muszą zostać przekazane między podmiotem płacącym (podatnikiem) a organem podatkowym (wierzycielem), aby transakcja była jednoznaczna i możliwa do zaksięgowania.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Creditor** | Wierzyciel – w kontekście podatkowym jest to organ podatkowy (np. urząd skarbowy), który ma prawo otrzymać należność. |
| **Debtor** | Dłużnik – podmiot zobowiązany do zapłaty podatku (podatnik). |
| **Administration Zone** | Strefa administracyjna – określenie


Taxinformation block is also available within the Structured Remittance Information block which is applicable when tax information is used by the creditor as part of remittance information.

Credit Transfer Transaction Information

---

<!-- ELEMENT 92 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Related  Remittance  Information

Min 0 - Max 10

The Related Remittance Information element within the pain.001 message is nested to provide information related to the handling of remittance information.

Min 0 - Max 1

The Remittance Identification captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction.

Min 0 - Max *

The Remittance Location Details uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

Method requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email)

Electronic Address provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.

Postal Address provides the postal address to which an agent is to send the remittance information

Unlike CBPR+ pacs messages, in the interbank pain.001 message, Related Remittance Information and Remittance Information are non-mutually exclusive due to a corporate use case of populating both information blocks for detailing remittance advices which are part of value-added service offered by the Debtor Agent .

SCORE Guideline: If the Related Remittance Information is used, and a Remittance Identification is provided, it is recommended that the Remittance Identification equal the End To End Identification.

Credit Transfer Transaction Information

---

<!-- ELEMENT 93 -->
pain.001  Customer  Credit  Transfer Initiation  - Remittance  Information

Min 0 - Max 1

The optional Remittance Information element within the pain.001 message is nested to provide either Structured or Unstructured information  related to payment, such as invoices.

Remittance Information enables the matching/reconciliation  of an entry that the payment is intended to settle.

Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Min 0 - Max *

The Structured element is nested capturing rich structured Remittance Information, and is unlimited  in its multiplicity, but must not exceed 9,000 characters of business information (does not include  the xml element identification)

The use of this nested element should  be bilaterally/multilaterally  agreed, to ensure end-toend transportation of this data.

Recommend to refer to CGI-MP Document Centre for Country requirements on Remittance Information.


## Cel schematu
Schemat przedstawia hierarchiczną strukturę elementów danych w wiadomościach finansowych standardu ISO 20022 (prawdopodobnie z obszaru komunikatów `pain` lub `pacs`). Jego celem jest zdefiniowanie sposobu przekazywania informacji o przelewie, a konkretnie wskazanie, w jaki sposób dane dotyczące celu płatności (tzw. informacje remitencyjne) są zagnieżdżone i kategoryzowane wewnątrz transakcji kredytowej.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Credit Transfer Transaction Information** | Główny blok danych zawierający wszystkie szczegóły dotyczące pojedynczej transakcji przelewu kredytowego (np. kwota, waluta, dane dłużnika i wierzyciela). |
| **Remittance Information** | Informacje remitencyjne – dane dostarczane przez płatnika dla odbiorcy, które pozwalają na identyfikację celu płatności oraz ułatwiają rozliczenie należności (rekonsyliację). |
| **Structured** | Strukturyzowane informacje remitencyjne. Dane zapisane w ściśle określonym formacie/kodzie (np. referencja RF zgodnie z ISO 11649), co umożliwia ich pełną automatyzację po stronie odbiorcy. |
| **Unstructured** | Niestrukturyzowane informacje remitencyjne. Dowolny tekst wpisany w polu "tytuł przelewu", który zazwyczaj wymaga ręcznej analizy lub zaawansowanych narzędzi OCR/AI do przypisania do konkretnej faktury. |

## Logika i relacje
Schemat ilustruje relację typu **rodzic-dziecko (hierarchię)**, która w standardzie ISO 20022 odzwierciedla strukturę pliku XML:

1.  **Poziom nadrzędny:** Wszystko zaczyna się od `Credit Transfer Transaction Information`. Jest to kontener dla całej transakcji.
2.  **Drugi poziom (zależność):** Wewnątrz informacji o transakcji znajduje się element `Remittance Information`. Oznacza to, że informacje o celu płatności są integralną częścią danych transakcyjnych, ale stanowią oddzielny blok logiczny.
3.  **Trzeci poziom (wybór/specyfikacja):** Informacje remitencyjne dzielą się na dwie ścieżki: `Structured` oraz `Unstructured`. Z biznesowego punktu widzenia jest to rozróżnienie między danymi sformatowanymi (maszynowymi) a tekstem wolnym.

**Przepływ danych:** 
Płatnik inicjuje przelew $\rightarrow$ System przypisuje dane do bloku transak


---

<!-- ELEMENT 94 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Structured  Remittance  Information

The bilaterally/multilaterally agreed Remittance Information which is Structured must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.


## Cel schematu
Schemat przedstawia strukturę **Ustrukturyzowanych Informacji o Płatności (Structured Remittance Information)** w standardzie ISO 20022. Jego celem jest zdefiniowanie zestawu konkretnych pól danych, które mogą zostać dołączone do przelewu pieniężnego zamiast jednego pola tekstowego (nieustrukturyzowanego).

Z biznesowego punktu widzenia schemat ten ilustruje mechanizm umożliwiający **automatyczne rozliczanie płatności (Automatic Reconciliation/Straight-Through Processing - STP)**. Dzięki takiemu podziałowi, systemy księgowe odbiorcy mogą automatycznie dopasować przelew do konkretnej faktury, kwoty podatku lub zlecenia komorniczego bez konieczności ręcznej analizy tytułu przelewu przez pracownika księgowości.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Structured** | Główny kontener danych; oznacza, że informacje o płatności są przekazywane w formie ustrukturyzowanej (zgodnie z określonym schematem XML), a nie jako swobodny tekst. |
| **Refered Document Information** | Dane identyfikacyjne dokumentu, do którego odnosi się płatność (np. numer faktury, data wystawienia, numer noty kredytowej). |
| **Refered Document Amount** | Dokładna kwota przypisana do konkretnego referowanego dokumentu (pozwala na częściową spłatę wielu faktur w jednym przelewie). |
| **Creditor Reference Information** | Unikalny identyfikator płatności nadany przez wierzyciela (np. numer referencyjny RF), który pozwala odbiorcy natychmiast zidentyfikować nadawcę i cel wpłaty. |
| **Invoicer** | Informacje o podmiocie, który wystawił fakturę (ważne w sytuacjach, gdy wystawca faktury jest inny niż końcowy odbiorca środków). |
| **Invoice** | Szczegółowe


example of Structured invoice information

The Creditor Remittance Information is provided to the Creditor in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.


## Cel schematu
Celem tego schematu jest zilustrowanie mapowania pomiędzy trzema poziomami reprezentacji danych w standardzie ISO 20022: poziomem biznesowym (nazwy elementów), poziomem technicznym (tagi XML) oraz poziomem instancji danych (konkretne wartości biznesowe). Schemat wyjaśnia, w jaki sposób abstrakcyjne pojęcia biznesowe są przekładane na konkretną strukturę techniczną w celu zapewnienia interoperacyjności systemów finansowych.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **element names** | Biznesowe nazwy pól zdefiniowane w modelu logicznym ISO 20022; określają, co dana informacja oznacza z punktu widzenia biznesowego. |
| **xml tag** | Techniczne oznaczenie elementu w formacie XML (schemat XSD), które służy do przesyłania danych między systemami informatycznymi. |
| **business information** | Konkretne dane wejściowe (wartości), które są przesyłane w ramach danej transakcji/wiadomości. |
| **Structured (`<Strd>`)** | Wskaźnik mówiący o tym, że informacja jest przekazywana w formie ustrukturyzowanej (zgodnie z określonym schematem), a nie jako zwykły tekst wolny (unstructured). |
| **Reference Document Information (`<RfRdDocInf>`)** | Komponent służący do identyfikacji dokumentu referencyjnego, na który powołuje się w wiadomości (np. faktura, umowa). |
| **Type (`<Tp>`)** | Określa rodzaj/typ dokumentu referencyjnego. |
| **Code Or Proprietary (`<CdOrPrtry>`)


In this example Referred Document Information and its nested elements have multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.


## Cel schematu
Schemat przedstawia hierarchiczną strukturę danych w standardzie ISO 20022, konkretnie w kontekście przelewu kredytowego (Credit Transfer). Jego celem jest zdefiniowanie sposobu organizacji informacji o płatności, aby umożliwić precyzyjną identyfikację celu przelewu i automatyzację procesu księgowania po stronie odbiorcy. Ilustruje on przejście od ogólnej informacji o transakcji do konkretnego, ustrukturyzowanego formatu danych referencyjnych.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Credit Transfer Transaction Information** | Blok danych zawierający wszystkie szczegóły dotyczące pojedynczej transakcji przelewu kredytowego (np. kwota, waluta, dane dłużnika i wierzyciela). Jest to nadrzędny kontener dla informacji o konkretnej płatności. |
| **Remittance Information** | Informacja o celu płatności (tzw. "tytuł przelewu"). Służy do identyfikacji przez odbiorcę, za co została dokonana wpłata (np. numer faktury, numer zamówienia), co umożliwia automatyczne rozliczenie należności. |
| **Structured** | Wariant informacji o celu płatności, który nie jest wolnym tekstem, lecz posiada ściśle zdefiniowany format (np. zgodny ze standardem ISO 11649 RF). Pozwala to systemom informatycznym na automatyczne parsowanie danych bez konieczności ręcznej analizy treści. |

## Logika i relacje
Schemat przedstawia relację hierarchiczną typu **rodzic-dziecko (nesting)**, która odzwierciedla strukturę pliku XML w standardzie ISO 20022:

1.  **Poziom najwyższy (Root/Parent):** `Credit Transfer Transaction Information` stanowi kontekst całej operacji finansowej. Wszystkie pozostałe elementy są przypisane do tej konkretnej transakcji.
2.  **Poziom średni:** Wewnątrz transakcji znajduje się element `Remittance Information`. Jest to logiczne powiązanie: "każda transakcja może posiadać informacje o celu płatności".
3.  **Poziom najniższy (Specyfikacja):** Element `Structured` jest konkretyzacją informacji o celu płatności. Logika biznesowa wskazuje tutaj na wybór między informacją nieustrukturyzowaną (wolny tekst) a ustrukturyzowaną. Wybr


---

<!-- ELEMENT 95 -->
pain.001  Interbank  Customer  Credit  Transfer Initiation  - Structured  Remittance  Information

The Creditor Reference in the Creditor Remittance Information component  in the structured remittance information  is generated by Creditor to inform the Debtor who has to include the reference in the Remittance Information component of the pain.001.

Creditor Reference in the Structured Remittance Information is based on ISO 11649

2 letters 'RF'

2 digits check digit

21 letters/digits  creditor reference

Facilitates STP and auto-match with the creditor reference and its account receivable

A vendor can add the creditor reference to its invoice. When a customer pays the invoice,  they write the creditor reference instead of the invoice number in the payment message (e.g., MT 101 F70 which will be carried in MT 103)

When the vendor receives the payment, it can auto-match the incoming credit entry and the creditor reference extracted from the statement (e.g., MT 940 F61/86)

SCORE Guideline: For Creditor Reference information, in instances where the Creditor Reference Type code is SCOR (Structured Communication Reference) and the Creditor Reference is structured in accordance with ISO 11649, the Issuer should be specified with the text 'ISO' (without the quote marks)

Credit Transfer Transaction Information

Remittance Information

---

<!-- ELEMENT 96 -->
Index of pain.001 Use Cases

Use case should be considered as a principal example whereby use case may be cross referenced e.g., a use case involving  a Ma rket  Infrastructure can apply the Market  Infrastructure  legs to other use cases.

Interbank Customer Credit Transfer Initiation - Relay

Use Case pn.1.1.1 - High Level Payment Initiation  Interbank  'relay'  (pain.001)

Use Case pn.1.1.1.a  - High Level Payment Initiation  Interbank  'relay'  (pain.001)  Multi-bank  Sweep

Use Case pn.1.1.2 - High Level Payment Initiation  Interbank  'relay'  (pain.001) involving  a Payment Market  Infrastructure

Interbank Customer Credit Transfer Initiation - Authorised  Party

Use Case pn.1.2.1 - High Level Payment Initiation  Interbank  (pain.001) by an Authorised  Party

Use Case pn.1.2.1.a.  - High Level Payment Initiation  Interbank  (pain.001) FI-Initiated  Sweep (Long position at the Secondary Account)

Use Case pn.1.2.1.b.  - High Level Payment Initiation  Interbank  (pain.001) by an Authorised Party to pay themselves as the Creditor

Interbank Customer Credit Transfer Initiation - Financial Institution

Use Case pn.1.3.1 - High Level Payment Initiation  Interbank  (pain.001) Financial Institution  Payment Initiation

---

<!-- ELEMENT 97 -->
High Level Payment Initiation Interbank 'relay' (pain.001)

Use Case pn.1.1.1

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor and initiate a credit transfer.

1

1

2

3

3a

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding  a local credit transfer message pacs.008

Debtor Agent (A) provides  a status update ACSP (accepted settlement in progress) to the Forwarding  Agent (F), based upon a bilateral agreement

3b

Forwarding  Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

4

Creditor Agent (B) processes the payment and sends the statement to Creditor

Initiating Party sends a payment instruction to the Forwarding  Agent

Forwarding  Agent (F) forwards the payment instruction to the Debtor Agent (A)

---

<!-- ELEMENT 98 -->
High Level Payment Initiation Interbank 'relay' (pain.001) Multi-bank Sweep

Use Case pn.1.1.1.a

In the interbank relay scenario, the Forwarding Agent relaying the pain.001 message to the Debtor Agent(s) in this case to sweep excess cash from the account of the Debtor and consolidate cash for a Corporate.

1

1

2

Debtor Agent (A) debits the initiates a credit transfer by 3

3a account of Debtor and forwarding  a local credit transfer message pacs.008

Debtor Agent (A) provides  a status update ACSP (accepted settlement in progress) to the Forwarding  Agent (F), based upon a bilateral agreement

3b

Forwarding  Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

4

Creditor Agent (B) processes the payment and notifies Creditor of a successful sweep through the statement

Initiating Party sends a payment instruction to the Forwarding Agent to sweep excess funds from its subsidiary's account to the master account with Bank B

Forwarding  Agent (F) forwards the payment instruction to the Debtor Agent (A)

---

<!-- ELEMENT 99 -->
High Level Payment Initiation Interbank 'relay' (pain.001) involving a Payment Market Infrastructure

Use Case pn.1.1.2

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor initiate a credit transfer through a Payment Market Infrastructure.

1


## Cel schematu
Schemat przedstawia end-to-end przepływ komunikacyjny w procesie przelewu płatniczego zgodnie ze standardem ISO 20022. Jego celem jest zilustrowanie drogi instrukcji płatniczej od inicjatora, poprzez agentów pośredniczących i infrastrukturę rynku, aż do odbiorcy końcowego. Dokumentuje on transformację wiadomości typu "Customer-to-Bank" (pain) na wiadomości typu "Interbank" (pacs), a także mechanizm zwrotny informowania o statusie transakcji.

## Kluczowe koncepcje

| Pojęcie/Termin | Wyjaśnienie |
|----------------|-------------|
| **Initiating Party** | Podmiot inicjujący płatność (np. klient korporacyjny lub osoba fizyczna). |
| **Forwarding Agent (F)** | Agent pośredniczący, który przyjmuje instrukcję od inicjatora i przekazuje ją do agenta dłużnika. |
| **Debtor Agent (A)** | Bank/instytucja finansowa dłużnika; podmiot odpowiedzial


---

<!-- ELEMENT 100 -->
High Level Payment Initiation Interbank (pain.001) by an Authorised Party

Use Case pn.1.2.1

In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place between the Debtor and the Debtor Agent

DA

As a pre-requisite  the Debtor provides  Debit Authorisation to Agent A, which allows Agent I to Initiate Payment from their account

request (pain.001)  to the Debtor Agent (A) to move fund  from the 2

Agent (I) initiates a payment Debtor's account, as an authorised party.

3

3a

4

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides  a status update to the Initiating Party (Agent I), based upon a bilateral agreement

Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous  Agent based upon a bilateral agreement

---

