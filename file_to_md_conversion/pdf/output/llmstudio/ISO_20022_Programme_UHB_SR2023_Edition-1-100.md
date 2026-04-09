<!-- ELEMENT 1 -->
This Cross-Border Payment Reporting plus (CBPR+) User Handbook is intended to document and explain a variety of ISO 20022 payment related topics, as well as provide practical use cases to ensure a common understanding and adoption of ISO 20022 within the payment industry.

The SWIFT FINplus service will support CBPR+ messages on the SWIFT network traditionally associated with correspondent banking (many-to-many). These messages may be exchanged either between Agents in the same country or between Agents in

The use cases focus on a core topics where other relevant messages may also be referred to within the use case, it may also be necessary to consider other documented use cases, in order to capture a wider variation of scenarios.

Note:
This document jointly developed with the CBPR+ group continues to evolve inline with the Standards Release as:

- CBPR+ continue to develop market practice guidelines for additional message.
- Inaccuracies are identified and corrected.
- Further use cases and/or explanation needs are identified

---

<!-- ELEMENT 2 -->
Page 2 Updated – note

Page 5 Updated – new messages added to index

Page 6 Updated – new messages added to index

Page 11 Updated – correction of Intermediary code

Page 33 Updated – new messages and Usage Ids added

Page 40 Updated – new pain message added to index

Page 45 Updated – recognition of Payment Initiation relay rulebook

Page 107 Updated – recognition of Payment Initiation relay rulebook

Page 122 Updated – additional use cases in the index

Page 126 New – use case

Page 134 New – use case

Page 135-182 New – pain.008 message section

Page 184 Update – new messages added to index

Page 204 Update – removed refer to Wait For Settlement Market Practice

Page 351 New – new high level message flow

Page 371 Updated – new messages added to index

Page 379-380 New – pacs.003 use cases

Page 400 Updated – additional guidance on ultimate parties on the return

Page 423 Updated – correct to Agent description in Step 7

Page 458-488 New – pacs.010 Margin Collection section

Page 489-529 New – pacs.003 Customer Direct Debit section

Page 530 Updated – new message added to index

Page 674 Updated – removed reference to SR 2023

Page 682 Updated – moved reference to multiple notification, now at an Item level

Page 691 Updated – reference to multiple notification item Rule

Page 698-716 New – camt.058 Notice to Received Cancellation section

Page 743 Updated - new message added to index

Page 764 Updated - use case Id correction

Page 774-795 New – Customer Cancellation Request section

Page 823-883 New – Cheque message sections

---

<!-- ELEMENT 3 -->
```markdown
| Message type and direction | Optional Message type and direction | Focal Message type and direction |
| --- | --- | --- |
| Exception & Investigation Case Assigner | Exception & Investigation Case Assignee | Payment Initiation (pain) |
| Statement Account Owner | Statement Account Servicer | Payment Clearing and Settlement (pacs) |
| Statement Authorised Party | Shortcut to other part of document | Cash Management Reporting (camt) |
| Extra attention is needed | Legacy FIN MT message | Cash Management Exception & Investigations (camt) |
| gpi Tracker | Focus message | Agent processing legacy format during a coexistence period |
| Market Infrastructure | New slide since last iteration | Slide updated since last iteration |

---

<!-- ELEMENT 4 -->
```markdown
# Table of Contents

1. Introduction to ISO 20022
2. Business Application Header
3. Payment Initiation (pain)
   - pain.001 - Interbank Customer Credit Transfer Initiation
   - pain.002 - Interbank Customer Payment Status Report
   - pain.008 – Customer Direct Debit Initiation [new for SR2023]
4. Payment, Clearing and Settlement (pacs) messages
   - pacs.002 – Financial Institution to Financial Institution Payment Status Report
   - pacs.004 – Payment Return
   - pacs.003 – Financial Institution to Financial Institution Customer Direct Debit [new for SR2023]
   - pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer
   - pacs.009 (core) - Financial Institution Credit Transfer
   - pacs.009 (cov) - Financial Institution 'Cover' Credit Transfer
   - pacs.009 (adv) – Financial Institution 'Advice' Credit Transfer

---

<!-- ELEMENT 5 -->
# Table of Contents (continued)

5. Cash Management Reporting (camt) messages

* camt.052 - Bank to Customer Account Report
* camt.053 - Bank to Customer Statement
* camt.054 - Bank to Customer Debit Credit Notification
* camt.057 – Notification to Receive
* camt.058 – Notification to Receive Cancellation Advice (new for SR2023)

6. Cash Management Exception & Investigation (camt) messages

* camt.029 - Resolution of Investigation
* camt.055 – Customer Payment Cancellation Request (new for SR2023)
* camt.056 - FI to FI Cancellation Request

7. Cheques

* camt.107 – Cheque Presentment Notification (new for SR2023)
* camt.108 – Cheque Cancellation or Stop Notification (new for SR2023)
* camt.109 – Cheque Cancellation or Stop Report (new for SR2023)

---

<!-- ELEMENT 6 -->
# Introduction to ISO 20022

---

<!-- ELEMENT 7 -->
ISO 20022 introduces a fundamental change to the traditional language used by the payments industry for several decades. It also describes participants (i.e., parties) to a business transaction differently based upon the business domain (area) being described, in a similar way you may describe a person as a colleague, parent or sibling depending upon the context you wish to describe them. This section is designed to capture and explain some of the differences.

---

<!-- ELEMENT 8 -->
# Domains

## Payment and Cash Management
* Securities
* Trade Services
* Foreign Exchange
* Card Payment

## Message Definitions
| acmt | Account Management |
| auth | Authorities |
| camt | Cash Management |
| pacs | Payment Clearing and Settlement |
| pain | Payment Initiation |
| remt | Payment Remittance Advice |

# Message Sets

camt.052 Bank to Customer Account Report<br>
camt.053 Bank to Customer Statement<br>
camt.054 Bank to Customer Debit Credit Notification<br>
camt.056 FI to FI Payment Cancellation Request<br>
camt.057 Notification to Receive<br>

pacs.002 FI to FI Payment Status Report<br>
pacs.004 Payment Return<br>
pacs.008 FI to FI Customer Credit Transfer<br>
pacs.009 Financial Institution Credit Transfer<br>

pain.001 Customer Credit Transfer initiation<br>
pain.002 Customer Payment Status Report<br>
pain.012 Creditor Payment Activation Request<br>

## ISO 20022 catalogue messages hierarchically beginning with a Business Domain, contain a various sets of Message Definitions, which in turn contain a variety of Message Sets.
* for example:
    * Payment and Cash Management
    * Payments Clearing and Settlement

---

<!-- ELEMENT 9 -->
```markdown
4!a . 3!c . 3!n . 2!n

| Business area | Variant | Message identifier/functionality | Version |
|---------------|---------|---------------------------------|----------|
| Example       | pacs.008.001.08 | FI To FI Customer Credit Transfer | Payments Clearing and Settlement | Version 8 | Variant 1 |

---

<!-- ELEMENT 10 -->
```markdown
# Payment Initiation (pain)

| Ultimate Debtor | Forwarding Agent |
| --- | --- |
| Initiating Party |

## Payments Clearing & Settlement (pacs)

### Previous Instructing Agents
:72::INS:

### Reimbursement Agents
:53a, :54a, :55a

### Intermediary Agents
:56a, :72::INT:

## Cash Management (camt)

| Ultimate Creditor | Creditor |

---

<!-- ELEMENT 11 -->
The diagram attempts to explain the construct of an ISO 20022 message sent across the SWIFT network using the FINplus service (which is designated to support various ISO 20022 business domains on SWIFT Interact).

Within the CBPR+ User Handbook, the predominant focus is on the **Request Payload**, as this is where the business information is contained. However, it is worth noting that a network provider will have additional containers around the Request Payload to perform functionality on its network. This diagram presents the additional containers on the SWIFT network such as the Request Header often referred to as the Technical Header of the message.

| Exchange Request |
| --- |
| Request |
| RequestHeader |
| RequestPayload |
| Application Header |
| Document |
| MX Message Instance |
| Crypto |

SWIFTNet Headers

Envelope - container for the business message
The business message comprises the application header and 'business' document
The 'business' document contains the MX message instance (or ISO 20022 message instance)

ISO 20022 Business Application Header

ISO 20022 Message

---

<!-- ELEMENT 12 -->
```markdown
# XML Elements

An XML instance or document contains data in elements and nested elements (elements which contain other elements) corresponding to the hierarchy imposed by the XML schema. In the CBPR+ Usage Guidelines we often refer to the element hierarchy by levels (to understand the nested relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example, in a pacs.008 Customer Credit Transfer the Interbank Settlement Date is a sub-element (Level 2) of the Credit Transfer Transaction Information element (Level 1).

## Naming conventions

An XML element is named according to the following rules:
- The name can contain letters, numbers, and other characters, but must not start with a number or punctuation mark.
- The name must not start with XML, xml, or Xml.
- The name must not contain any spaces.

## MX naming conventions

There are some generic naming rules that apply to most items in the database:
- The names of all items in the database use the upper CamelCase convention, as follows:
  - Each word starts with a capital letter.
  - There are no white spaces between words.
  - A name may be made up of multiple words, each consisting of alphanumeric characters.
  - Words use British English vocabulary.
  - All names must start with an alphabetic character.
  - All characters that follow the first characters must be letters or numbers.

### Example of a Street Name element: `<StrtNm>Oxford Street</StrtNm>`

## MX message element multiplicity (occurrences)

| Min | Max | Element Multiplicity |
| --- | --- | --- |
| 1   | 1   | Required element     |
| 0   | 1   | Optional element      |
| 0   | *    | Unlimited element occurrences |

---

<!-- ELEMENT 13 -->
Empty XML Elements

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element.

A common example of this is in payment message is Financial Institution.

| Financial Institution Identification | 1 | 1 |
| --- | --- | --- |
| BICFI | 0 | 1 |
| Clearing System Member Identification | 0 | 1 |
| LEI | 0 | 1 |
| Name | 0 | 1 |
| Postal Address | 0 | 1 |

Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e., `<FinInstnId>`</FinInstnId>

In the FINplus service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where business data should be provided within a nested element, it is provided.

---

<!-- ELEMENT 14 -->
MyStandards describes the element's context by its path whereby each element is divided by a forward slash (/). For example, the pacs.008 Town Name within the Debtor Postal Address is described as /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/PstlAdr/TwnNm

Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing the element in an XML naming convention.

For example, to describe the pacs.008 Payment Identification, the following is displayed on the bottom right-hand side of the page to explain Payment Identification is an element below Credit Transfer Transaction Information.


In this way, the CBPR+ User Handbook uses three main icons to explain the relationships between elements by displaying the icon after the element name.

- To visualize an element which has nested elements beneath it
- To visualize an element which has a choice associated with it i.e., a Code where a choice of which code can be determined
- To visualize an element which is nested and has a choice associated with it. For example, an Identification where a choice must be made between an Organisation Identification and a Private Identification element which is nested but where both cannot be used together.

---

<!-- ELEMENT 15 -->
```markdown
# CBPR+

Cross-Border Payments and Reporting Plus (CBPR+) specifications define how ISO 20022 is used for cross-border payments and cash reporting on the Swift network. Conformance to CBPR+ specifications will be validated by Swift messaging services and interfaces, so it is imperative that users implement the specifications correctly. The resources available on this page aim to help Swift's community to understand and implement CBPR+ specifications.

Learn more about ISO 20022 Readiness: [Link]

## Additional resources

Find out how ISO 20022 is used for cross-border payments and cash reporting on the Swift network.

### Document centre
- **CBPR+ user handbook**: Documents the CBPR+ Guidelines request common business scenarios in cross-border payment and reporting processes.
    - Download: [Link]
- **Derived data mapping guidance**: Provides guidance on how to populate information from one messaging standard to another subsequent message.
    - Download: [Link]
- **MT / MX equivalence table**: Documents the CBPR+ Usage Guidelines supported on Swift network HVPAS messages in comparison with the equivalent MT message.
    - Download: [Link]

### Samples library
- **CBPR+ sample messages**: Sample messages refer to test use cases described in the CBPR+ user handbook.
    - Learn more: [Link]
- **In-flow translation service sample messages**: Sample test messages for the In-flow translation service.
    - Learn more: [Link]

## CBPR+ and HVPAS+ alignment
This document outlines similarities and differences between the two market practice sets.

Download: [Link]

## Lessons learnt since go-live
This document intends to provide guidance to the community regarding observations that may be identified before or after the migration.

Download: [Link]

---

<!-- ELEMENT 16 -->
```markdown
# Cross Border Payments and Reporting Plus

## CBPRplus.pacs.008.001.08 FIToF Customer Credit Transfer

CBPRplus (ISO 20025 Portfolio: November 2022 Release 2.0 | Technical version: 1, Version: V2.0 FOR IMPLEMENTATION, Format: MX, Status: Final)

Usage Identifier: swift.cbpplus.01 Version: V2.0 FOR IMPLEMENTATION Status: Final

### Content
- Show details

Many of the CBPRplus Usage Guidelines have useful key principals and additional information. These can be expanded in MyStandards by clicking on 'show details' in the middle of the Usage Guideline description pane.

---

<!-- ELEMENT 17 -->
Traditionally in the Legacy FIN standard rules related to a message were described as either **Network Validation Rules** – those validated by the network, or **Usage rules** – rules not validated by the network. FIN also has the concept of **Usage Guidelines** – guideline to recommend a best practice.

In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated Usage Guideline (e.g. CBPR plus)

Within CBPR+ Usage Guideline specification the rules dedicate to CBPR+ are often described as:

- **Formal Rules** which are validated on the network; these are identified by the word *Rule* appended to the rule description. For example:  
  ![](https://example.com/image1.png) Rule "CBPR_Party_Name_Any_BIC_FormalRule"

- **Textual Rules** which are not validated on the network, these are identified by with the word *TextualRule* appended to the rule description. For example:  
  ![](https://example.com/image2.png) Rule "CBPR_Agent_Option_1_TextualRule"

- **Guideline Rules** which provide recommended best practice; these are identified by the word *Guideline* appended to the rule description. For example:  
  ![](https://example.com/image3.png) Rule "CBPR_Purpose_Guideline"

Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a CrossElementSimpleRule and a CrossElementComplexRule

---

<!-- ELEMENT 18 -->
```markdown
“<Short issuer organisation>•<Business context>{•<Business context>} n times•<version>
1-10 chars A 1 char B 1-10 chars C, D,... 1 char E 2 chars

Total max 35 char

- Type: String
- Max allowed size: 35 characters
- Structure:
    - Must contain minimum A & B, optionally followed by 1 or more additional business context elements (C, D, ...).
    - Always ends with version element E (format "nn", e.g., "01")
    - Each element is separated by a period ".".
    - Length of each text element can vary up to max 10 characters. Total length, including periods, cannot exceed 35 chars.
    - Consistency enforced by lightweight SWIFT review/registration: E.g., "ecb" to represent the ECB, not "eucb"
    - Lowercase alphanumeric characters only

In CBPR+ the Usage Identifier is captured within the Business Application Header, Business Service element. More detail can be found in the dedicated Business Application Header chapter of this document,

---

<!-- ELEMENT 19 -->
Many ISO 20022 message use data elements represented by codes. Such codes are often externalised from the message itself, enabling maintenance of the code list on a quarterly basis without requiring a new message version.

Some data element may also be embedded in the message.


example of Charge Bearer in pacs.008 v8 which uses embedded codes
| Charge Bearer | 1 |
| --- | --- |
| Borne By Debtor [DEBT] |  |
| Borne By Creditor [CRED] |  |
| Shared [SHAR] |  |
| Following Service Level [SLEV] |  |

example of Return Reason Information in pacs.004 v9 which uses externalised codes
| Type | ExternalReturnReason1Code (has a string) |
| --- | --- |
| minLength: 1 | DTH1 |
| maxLength: 4 | Invalidata |
| Definition | Reason for the return, as an external reason code |

Proprietary Codes may also be available for certain data elements. These are typically inherited from legacy formats and require definitions in user documentation as these are not captured in the baseline ISO 20022 standards

---

<!-- ELEMENT 20 -->
All SWIFT ISO MX message elements (fields) which are defined (by data Type) as text are restricted to FIN X Characters: a-z A-Z 0-9 / - ? : ( ) . , ' + .

Special characters are additionally allowed in:
- All party (agents and non-agents) Name and Address elements.
- The Related Remittance Information element
- The Remittance Information (structured & unstructured) element
- The Email Address where included as part of a Proxy elements
- City of Birth and Province of Birth elements nested in Private Identification

Currencies in the payments should be expressed in ISO Currency Codes only (3 Characters, e.g. EUR)

Translation of any special character: #&%*='^_`{|}~"@[{}$>< into MT messages will be represented by a . (Full Stop)

List of special characters:
! < > & [ ] =

---

<!-- ELEMENT 21 -->
```markdown
# Point-to-point

refers to data passed within a message from one party to the next. This data will not necessarily be passed in subsequent messages.

For example: the Instruction Identification element contains a reference meaningful to the party sending a message, subsequent messages in a payment transaction chain can expect the Instruction Identification to be replaced by a reference meaningful to the party sending that message leg.


# End-to-end

refers to data passed throughout the transaction life cycle i.e. within a message from one party to the next and continued in subsequent messages.

For example: the UETR element contains a Unique End-to-end Transaction Reference in accordance with the UUID version 4 standards. This same reference is used in all messages related to the payment transaction.

---

<!-- ELEMENT 22 -->
ISO 20022 messages have a number of elements associated with Agents which allow for these Agents to be referenced by a variety of Financial Institution identifiers.
More commonly the ISO 9362 Financial Institution BIC (BICFI) is considered the best practice de facto standard for 'many to many' / correspondent banking payments. However other options include:
Clearing System Member Identifiers when accompanied with the Clearing System Identification.
LEI (Legal Entity Identifier)
Name and either structured or unstructured Postal Address.

| Financial Institution Identification |
| --- |
| BICFI |
| Clearing System Member Id |
| LEI |
| Name |

Clearing System Id

---

<!-- ELEMENT 23 -->
Two common elements to ISO 20022 messages are **Date** and **DateTime**.

CBPR+ usage guidelines **DateTime** elements mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/−hh:mm
For example: 2002-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)
note - milliseconds are optional.

The ISO 20022 **Date** elements allow the date to include an offset. As a data model, shared by other business domains, an offset date can provide great business clarity, such as something expiring at the end of a business date. However, in payments such a date offset provides little business value, whereby should an offset be included with the date, this offset should be ignored.

---

<!-- ELEMENT 24 -->
| Country | Code Name | MT Clearing System code | ISO 20022 Clearing System Identification |
| --- | --- | --- | --- |
| Australia | Australian Bank State Branch Code (BSB) | AU | AUBSB |
| Austria | Austrian Bankleitzahl | AT | ATBLZ |
| Canada | Canadian Payments Association Payment Routing Number | CC | CACPA |
| China | Bank Branch code used in China | CN | CNAPS |
| Germany | German Bankleitzahl | BL | DEBLZ |
| Greece | Helenic Bank Identification Code | GR | GRBIC |
| Hong Kong | Hong Kong Bank Code | HK | HKNCC |
| India | Indian Financial System Code | IN | INFSC |
| Ireland | Irish National Clearing Code | IE | IENCC |
| Italy | Italian Domestic Identification Code | IT | ITNCC |
| Japan | Japan Zengin Clearing Code | JP | JPZGN |
| New Zealand | New Zealand National Clearing Code | NZ | NZNCC |
| Poland | Polish National Clearing Code | PL | PLKNR |
| Portugal | Portuguese National Clearing Code | PT | PTNCC |
| Russia | Russian Central Bank Identification Code | RU | RUCBC |
| South Africa | South African National Clearing Code | ZA | ZANCC |
| Spain | Spanish Domestic Interbanking Code | ES | ESNCC |
| Switzerland | Swiss Clearing Code (BC Code) | SW | CHBCC |
| Switzerland | Swiss Clearing Code (SIC Code) | SW | CHSIC |
| Taiwan | Financial Institution Code | TW | TWNCC |
| UK | UK Domestic Sort Code | SC | GBPSC |

For translation rules and comparison purposes this table provides a list of published MT National Clearing System codes against their equivalent ISO 20022 Clearing System Identification in the external code list.

---

<!-- ELEMENT 25 -->
```markdown
# Business Application Header

---

<!-- ELEMENT 26 -->
The head.001 Business Application Header **Character Set** element declares the character set, in addition to Latin, that is contained in the Business Document e.g. the pacs.008.

The **Character Set** element uses the UnicodeChartsCode string to declare an additional character set, for example Cyrillic (Unicode range: 0400-04FF).

This allows the party for which the message is addressed *To* to know in advance the additional character set contained within the Business Document. In this way the message can be routed to a specific application to process the Character Set or handled as an exception if the Character Set is not appropriate for that business transaction.

Extending character sets is not intended in CBPR+ from the initial implementation of the service. This element is intended for use once extended character sets are implemented, whereby the string represented in this element can enable any necessary network validations, such as a closed user group for that character set.

---

<!-- ELEMENT 27 -->
The head.001 Business Application Header **From** element identifies the BIC of the party who created the Business Document (e.g., pacs.008). Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

A choice must be made for the BIC depending on the party it represents.
**Financial Institution Identification**, which identifies a Financial Institution, and may be further complemented with
- **Clearing System Member Identification**
- **LEI**
as an additional identification.

---

<!-- ELEMENT 28 -->
The head.001 Business Application Header **To** element identifies the BIC of the party who will ultimately process the Business Document (e.g., pacs.008) Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

A choice must be made for the BIC depending on the party it represents.
**Financial Institution Identification** which identifies a Financial Institution, and may be further complemented with
- **Clearing System Member Identification**
- **LEI**
as an additional identification.

---

<!-- ELEMENT 29 -->
The head.001 Business Application Header **Business Message Identifier** element contains the Message Identification captured within the Business Document's Group Header. The content of this element should match the Business Document to avoid incorrect routing by the recipient.

| Business Application Header | Business Message Identifier: 1A245878.. |
| --- | --- |
| Business Document | Group Header<br>Message Identification: 1A245878.. |

---

<!-- ELEMENT 30 -->
The head.001 Business Application Header **Message Definition Identifier** element contains the name of the Business Document. The content of this element should match the Business Document to avoid incorrect routing by the recipient.

| Business Application Header |
| --- |
| Message Definition Identifier | pacs.009.001.08 |

| <Document "pacs.009.001.08"> |
| --- |

Group Header

---

<!-- ELEMENT 31 -->
The head.001 Business Application Header **Business Service** element is used to identify administered services on the SWIFT network. The data represented in this elements is referred to as a **Usage Identifier**. For CBPR+ examples are provided below, these values may be used together with the Message Definition Identifier to determine routing rules to specific applications without having to open the business document.

| Message Definition Identifier | Business Service | Business Use Case |
|--- | --- | ---|
| pacs.009.001.08 | swift.cbprplus.cov.01 | Financial Institution (Cover) Credit Transfer |
| pacs.009.001.08 | swift.cbprplus.01 | Serial Financial Institution Credit Transfer |
| pacs.008.001.08 | swift.cbprplus.stp.01 | STP Customer Credit Transfer |

The **Business Service** is also intended to be incremented for the same message version, when an updated Usage Guideline is released. For example a new restriction is applied to the pacs.009.001.08 Usage Guideline, the Business Service swift.cbprplus.cov.02 and swift.cbprplus.02 will be used to reflect these new Guidelines and allow network validate.

Note: when a new message (Message Definition Identifier) version is introduced the numeric value for the Business Service is increased.

---

<!-- ELEMENT 32 -->
```markdown
| Message Definition Identifier | Business Service |
| --- | --- |
| pain.001.001.09 | swift.cbrplus.02 |
| pain.002.001.10 | swift.cbrplus.02 |
| pain.008.001.03 | swift.cbrplus.01 |
| pacs.002.001.10 | swift.cbrplus.02 |
| pacs.003.001.08 | swift.cbrplus.01 |
| pacs.004.001.09 | swift.cbrplus.02 |
| pacs.008.001.08 | swift.cbrplus.02 |
| pacs.008.001.08 (STP/STP EU) | swift.cbrplus.stp.02 |
| pacs.009.001.08 (advice) | swift.cbrplus.adv.02 |
| pacs.009.001.08 (core) | swift.cbrplus.02 |
| pacs.009.001.08 (cov) | swift.cbrplus.cov.02 |
| pacs.010.001.03 | swift.cbrplus.02 |
| pacs.010.001.03 (Margin Collection) | swift.cbrplus.col.01 |
| cant.029.001.09 | swift.cbrplus.02 |
| cant.052.001.08 | swift.cbrplus.02 |
| cant.053.001.08 | swift.cbrplus.02 |
| cant.054.001.08 | swift.cbrplus.02 |
| cant.055.001.08 | swift.cbrplus.01 |
| cant.056.001.08 | swift.cbrplus.02 |

| Message Definition Identifier | Business Service |
| --- | --- |
| cant.058.001.08 | swift.cbrplus.01 |
| cant.060.001.05 | swift.cbrplus.02 |
| cant.107.001.01 | swift.cbrplus.01 |
| cant.108.001.01 | swift.cbrplus.01 |
| cant.109.001.01 | swift.cbrplus.01 |

The data represented in the Business Service, together with the Message Definition Identifier has a number of roles, in addition to the routing rules referred to on the previous page.

This data value:
- Identifies explicitly the Usage Guideline within a library of guideline. For example an application may have various pacs.008 libraries within a collection, for which only one of these is appropriate to be used to identify data requirements or perform validation.
- is also populated in the Request Header of the InterAct message in the Request Sub Type element which allow the service (FINplus for CBPR+) to apply network validation rules.

---

<!-- ELEMENT 33 -->
The head.001 Business Application Header **Market Practice** element is used to identify administered services on the SWIFT network.
This element is currently not foreseen to be used by CBPR+.

---

<!-- ELEMENT 34 -->
The head.001 Business Application Header **Creation Date** captures the date and time which the Business Application Header was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
➔ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 35 -->
The head.001 Business Application Header **Copy Duplicate** indicator is used as a choice to identify scenarios where a message was previously sent.

| COPY | DUPL | CODU |
| --- | --- | --- |
| COPY is used to represent a copy of a message being sent to an additional party. This scenario is only associated with camt reporting messages. | DUPL is used to represent a duplicate of a previously sent camt reporting message. To receive a duplicate payment message, Interact message retrieval should be utilised. | CODU is used to represent a duplicate of a previously sent COPY message. This scenario is only associated with camt reporting messages. |

---

<!-- ELEMENT 36 -->
The head.001 Business Application Header **Possible Duplicate** element is used as a flag to indicate that if the party who will ultimately process the Business Document (e.g., pacs.008) received the original, then it should perform necessary actions to avoid processing this Business Message again.

This element is represented by a Yes/No Boolean, whereby **true** represent this is a Possible Duplicate.
It is not necessary to represent **false** (No) the absence of this optional element itself indicates that this is not considered a Possible Duplicate.

The FINplus Technical Header has an element **PDIndicator** (Possible Duplicate Indicator) which uses a Yes/No Boolean. This may be populated by the network interface to identify a message it considers may be a possible duplicate.

---

<!-- ELEMENT 37 -->
The head.001 Business Application Header **Priority** element allows a choice of Business Message Priority Code to indicate the priority which may be applied to the business message.

This element must represent the priority code of the business document (instance) which is only applicable for pacs messages. The pacs message priority is captured in the Payment Type Priority/Instruction Priority.

---

<!-- ELEMENT 38 -->
The head.001 Business Application Header **Related** nested element enables the capture of the Business Application Header from a related Business Document. For example, in a pacs.004 Payment Return the **Related** Business Application Header from the original message can be included. This could allow the receiver to apply specific routing to the message, based on the related information i.e., return of a pacs.009 cov may be routed to different payment engine than a core pacs.009.

The following elements are nested within the Related element. Where used these contain the original data from the related Business Application Header:

| From | To |
| --- | --- |
| **Business Message Identifier** | **Min 1 – Max 1** |
| **Message Definition Identifier** | **Min 1 – Max 1** |
| **Business Service** | **Min0 - Max 1** |
| **Creation Date** | **Min 1 – Max 1** |
| **Copy Duplicate** | **Min 0 – Max 1** |
| **Priority** | **Min 0 – Max 1** |

---

<!-- ELEMENT 39 -->
```markdown
pain.001 - Interbank Customer Credit Transfer initiation  
pain.002 – Interbank Customer Payment Status Report  
pain.008 – Customer Direct Debit Initiation

---

<!-- ELEMENT 40 -->
Interbank Customer Credit Transfer Initiation

---

<!-- ELEMENT 41 -->
```markdown
## ISO 20022 message element

| Group Header |
| --- |
| Message Identification |
| Initiating Party – where different from Debtor |
| Forwarding Agent |

| Payment Information |
| --- |
| Payment Information Identification |
| Requested Execution Date |
| Debtor |
| Debtor Agent |

| Credit Transfer Transaction Information |
| --- |
| Payment Identification |
| Amount |
| Charge Bearer |
| Creditor Agent |
| Creditor |

## Sequence A – General Information:

| Sender's Reference (Field 20) |
| --- |
| Instructing Party (Field 50 C or L) |
| Message Sender in a 'relay' scenario |

| Customer Specified Reference (Field 21R) |
| --- |
| Requested Execution Date (Field 30) |
| Ordering Customer (Field 50 F, G or H)* |
| Account Servicing Institution (Field 52 A or C)* |

## Sequence B – Transaction Details:

| Transaction Reference (Field 21) |
| --- |
| Currency/Transaction Amount (Field 32B) |
| Details of Charges (Field 71A) |
| Account With Institution (Field 57 A, C or D) |
| Beneficiary (Field 59 no letter, A or F)

---

<!-- ELEMENT 42 -->
```markdown
The pain.001 message is composed of three blocks:
- **Group Header** contains a set of characteristics that relates to all individual transaction.
- **Payment Information** contains a set of characteristics that relates to the debit side of the transaction, such as Debtor and Debtor Agent.
- **Credit Transfer Transaction Information** contains, among others, elements related to the credit side of the transaction, such as Creditor and Creditor Agent.

![](image.png) Payment messages in a many-to-many payment are considered as a single transaction.

---

<!-- ELEMENT 43 -->
```markdown
![](https://example.com/image.png)

FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

1. Relay: The pain.001 message is sent by the Initiating party (the Debtor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.001 message to the Debtor Agent.

---

<!-- ELEMENT 44 -->
```markdown
![](https://example.com/image.png)

This use case may not apply to all Financial Institution, depending on the products and service provided by that Financial Institution to their customer

FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

2. Authorised Party Initiation: The pain.001 message is sent by the Financial Institution as an Initiating Party to the Debtor Agent to initiate a payment on behalf of the Debtor who is the account holder. For example, a FI initiates; a liquidity sweep on behalf of a corporate customer or payment from the Debtor account based on Tri-party agreement (agreement from the Debtor with the Debtor

---

<!-- ELEMENT 45 -->
```markdown
![](https://example.com/image.png)

Interbank Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

3. Financial Institution Payment Initiation (to non-FI): The pain.001 message is sent by the Financial Institution as both the Debtor and Initiating Party to initiate a payment from their account with the Debtor Agent to move funds to a non-Financial Institution Creditor

---

<!-- ELEMENT 46 -->
The following descriptions are defined in the ISO 20022 Standard for core parties participating in an Interbank Customer Credit Transfer Initiation relationship.

| Forwarding Agent | Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution. Applicable for pain.001 use case 1 only |
| --- | --- |
| Initiating Party | Party that initiates the payment, which may be the Debtor or a Party acting on behalf of the Debtor e.g., the Agent initiating a liquidity sweep service |
| Debtor Agent | Financial institution servicing an account for the debtor. |
| Creditor Agent | Financial institution servicing an account for the creditor. |
| Debtor | Party that owes an amount of money to the (ultimate) creditor. |
| Creditor | Party to which an amount of money is due. |

---

<!-- ELEMENT 47 -->
Group Header

---

<!-- ELEMENT 48 -->
```markdown
# Interbank Customer Credit Transfer Initiation - Message Identification

Each ISO20022 payment message has a **Message Identification** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For the Payment Initiation (pain) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

Each transaction's Credit Transfer Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor or authorized third party) of the pain.001.

---

<!-- ELEMENT 49 -->
```markdown
The pain.001 message **Creation Date Time** captures the date and time which the message was created.

It is defined by **ISO Date Time** with mandatory date and time components expressed in the following formats:

1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
3. Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2nd option). Otherwise use UTC time (1st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

---

<!-- ELEMENT 50 -->
```markdown
The pain.001 message **Authorisation** allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The Authorisation uses an embedded code set or free text form. It has no exact equivalent in the legacy MT payment message, however, the Authorisation (Field 25) could be considered as a similar comparison.

| Code | Description |
| --- | --- |
| ILEV | Instruction Level Authorisation | File requires all customer transactions to be authorised or approved. |
| FDET | File Level Authorisation Details | Additional file level approval, with the ability to view both the payment information block and supporting transaction detail. |
| FSUM | File Level Authorisation Summary | Additional file level approval, with the ability to view only the payment information block. |
| AUTH | Pre Authorised File | File has been pre-authorised or approved within the originating customer environment and no further approval is required. |

For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.

---

<!-- ELEMENT 51 -->
```markdown
# Interbank Customer Credit Transfer Initiation - Number of Transactions

The pain.001 message **Number of Transactions** captures the number of individual transactions contained within the message.

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 52 -->
```markdown
# Interbank Customer Credit Transfer Initiation - Initiating Party

The **Initiating Party** can either be the *Debtor* or an Authorised Party who initiates payment transactions on behalf of the Debtor. The Initiating Party can be, for example, the Head Office which has the authority to debit the account of its subsidiary. In the centralization model, the Initiating Party can also be a payment factory or shared service center or third-party agent, which has authority to send the message on behalf of the Debtor.

There are three common use cases in the context of interbank pain.001 message:

1. **Relay**: The Initiating Party, which is either the Debtor themselves or authorised party, sends the pain.001 message to the *Forwarding Agent* which acts as a concentrating financial institution. It will forward the pain.001 message to the *Debtor Agent*. This is commonly known as a relay scenario. Whereby the Forwarding Agent is performing a technical role in the payment transaction, they would not be represented in the payment, clearing and settlement message.
2. **Authorised Party**: The Initiating Party is the *Financial Institution* which has the authority to send the pain.001 message on behalf of the Debtor, e.g., multi-bank liquidity sweeps.
3. **Financial Institution Payment Initiation**: The Initiating Party is the *Financial Institution* which is the Debtor who initiates a payment from their account to move

**For the second and third use case, BIC of the Initiating Party is required.**

---

<!-- ELEMENT 53 -->
```markdown
# Interbank Customer Credit Transfer Initiation - Initiating Party

The **Initiating Party** can either be the *Debtor* or an authorised party, such as Financial Institution, in the context of interbank pain.001. Sub elements describe the Initiating Party in greater detail.

| Postal Address |
| --- |
| Department |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Room |
| Post Code |
| Town Name |
| Town Location Name |
| District Name |
| Country Sub Division |

Nested element capturing structured Postal Address including at least Town Name and Country if used.

Mandatory *Name* where Postal Address is provided.

Nested element capturing the various types of identifiers, e.g., BIC, LEI etc. **BIC** is mandatory for an Authorised Party initiation and FI payment initiation.

Optional element to capture the Initiating Party's ISO country code of residence.

---

<!-- ELEMENT 54 -->
```markdown
#pain.001 Interbank Customer Credit Transfer Initiation – Forwarding Agent

The **Forwarding Agent** is mandatory in a relay scenario whereby the *Initiating Party* (the Debtor or authorised third party) has to provide the *Business Identifier Code* (BIC FI) of the Forwarding Agent in the original pain.001 message. The Forwarding Agent acts as a concentrating financial institution and forwards the pain.001 message to the Debtor Agent for execution.

Other options to identify the **Forwarding Agent** include:
- Clearing System Member ID
- LEI (Legal Entity Identifier)

| Financial Institution Identification |
| --- |
| BICFI |
| Clearing System Member Id |
| LEI |
| Various sub-element |

For the use cases of Authorised Party initiation and FI payment initiation, Forwarding Agent is not required.

---

<!-- ELEMENT 55 -->
# Payment Information

---

<!-- ELEMENT 56 -->
The CBPR+ pain.001 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognize that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory.
As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message. Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used.

### CGI-MP payment Initiation/ CBPR+ payment initiation interbank

| Structured | Unstructured |
| --- | --- |
|  |  |

Many domestic proprietary payments

Structured | Unstructured
--- | ---
CBPR+ payments

---

<!-- ELEMENT 57 -->
The Interbank Customer Credit Transfer Initiation **Payment Information Identification** provides a mandatory element to identify the payment initiation.

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions.

For single transactions in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header.

---

<!-- ELEMENT 58 -->
The pain.001 message **Payment Method** specifies the means of payment that will be used to move the amount of money. One of the following payment method codes must be used:

| Code | Name | Definition |
| --- | --- | --- |
| CHK | Cheque | Written order to a bank to pay a certain amount of money from one person to another person. |
| TRF | Credit Transfer | Transfer of an amount of money in the books of the account servicer. |

---

<!-- ELEMENT 59 -->
The pain message provides a set of optional elements where the payment type can be described.

# Payment Type Information

## Service Level (Min0 – Max1)
A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored.

## Instruction Priority (Min 0 – Max 1)
A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the processing.

## Local Instrument (Min 0 – Max 1)
A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, INST - Instant Credit Transfer for SEPA Service Level.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

## Category Purpose
A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends.

---

<!-- ELEMENT 60 -->
```markdown
The pain.001 message mandatory **Requested Execution Date** element, captures the date and time at which the initiating party requests the clearing agent to process the payment.

It is the date on which the debtor's account is debited. If payment by cheque, the date when the cheque must be generated by the bank. It is defined by either ISO Date expressed in the YYYY-MM-DD format or ISO Date Time below:

1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
3. Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2<sup>nd</sup> option). Otherwise use UTC time (1<sup>st</sup> option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

---

<!-- ELEMENT 61 -->
```markdown
# Interbank Customer Credit Transfer Initiation - Pooling Adjustment Date

The pain.001 message optional **Pooling Adjustment Date** element, is used for the correction of the value date of a cash pool movement that has been posted with a different value date.

It is defined by ISO Date expressed in the YYYY-MM-DD format

This element is not widely used in the payment industry. For the use case of interbank, it is even less likely to be utilized.

---

<!-- ELEMENT 62 -->
The ISO 20022 pain messages describes the party whose account is debited for a transaction as the **Debtor**. (Min 1 - Max 1)

The Debtor sub elements describe the Debtor in greater detail.

| Postal Address |
| --- |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Room |
| Postal Code |
| Town/Name |
| Town/Location Name |
| District Name |
| Country/Sub Division |
| Country |
| Address Line |

Nested element capturing either structured or unstructured Debtor address details.

Note: Structured address is strongly recommended with mandatory Town Name and Country

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Mandatory **Name** (where a BIC identifier is not provided) by which the party is known

Postal Address

Identification

Country of Residence

---

<!-- ELEMENT 63 -->
The pain.001 **Debtor Account** is used to capture the account information for which debit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The **Debtor Account** uses a variety of nested elements to capture information related to the account.

| Min 1 – Max 1 | Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution) |
| --- | --- |
| Min 0 – Max 1 | Type uses the external Cash Account Type code list to identify the type of account |
| Min 0 – Max 1 | Currency identifies the currency of the account, recommended. |
| Min 0 – Max 1 | Name identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) |
| Min 0 – Max 1 | Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used. |

Indication of Currency of the Debtor Account is recommended in case of multi-currency

---

<!-- ELEMENT 64 -->
The **Debtor Agent** is a static role in the pain.001 Customer Credit Transfer Initiation. This agent maintains a relationship with their customers, the *Debtor*.

Note: Although the **Debtor Agent**, **Creditor Agent**, **Debtor and Creditor** all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

For Agent Identification, BIC is preferred, alternatively Clearing Member ID together with Name and Address may be provided

---

<!-- ELEMENT 65 -->
The pain.001 **Debtor Agent Account** is used to capture the account information related to the Debtor Agent.

The **Debtor Agent Account** uses a variety of nested elements to capture information related to the account.

| Min 0 – Max 1 | Identification |
| --- | --- |
| Min 0 – Max 1 | Type |
| Min 0 – Max 1 | Currency |
| Min 0 – Max 1 | Name |
| Min 0 – Max 1 | Proxy |

Identification identifies the account maintained at the Account Servicing Institution. Type uses the external Cash Account Type code list to identify the type of account. Currency identifies the currency of the account. Name identifies the name of the account as assigned by the Account Servicing Institution. Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

Debtor Agent and Creditor Agent are Financial Institutions, therefore the nested elements **Name** and **Proxy** are unlikely to be used.

---

<!-- ELEMENT 66 -->
The Instruction for Debtor Agent element within the pain.001 message optionally provides information related to the processing of the payment.

The Instruction for Debtor Agent element offers a maximum of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the Debtor Agent, depending on bilateral agreement.

---

<!-- ELEMENT 67 -->
The pain.001 message introduces **Ultimate Debtor** and **Ultimate Creditor**. The **Ultimate Debtor** element should not be confused with an **Initiating Party** who may send a payment initiation request on behalf of the **Debtor**, for example, Payment Factory.

CBPR+ premise is that an **Ultimate Debtor** has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an **Ultimate Creditor** has no financial regulated account relationship with the corresponding Creditor.

The **Ultimate Debtor** and **Ultimate Creditor** can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 68 -->
The **Charge Bearer** element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

| Charge Bearer (0.1) | Code | Description |
| --- | --- | --- |
| CRED | Creditor |  |
| DEBT | Debtor |  |
| SHAR | Shared |  |

71A: Details of Charges
| Code | Description |
| --- | --- |
| BEN | Beneficiary |
| OUR | Our Customer Charges |
| SHA | Shared Charges |

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 69 -->
```markdown
The pain.001 optional **Charges Account** element, which is used to process charges associated with a transaction.

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

This element is not widely used in the payment industry.

---

<!-- ELEMENT 70 -->
```markdown
The pain.001 optional **Charges Account Agent** element, which is used to specify the agent that services a charges account.

Charges account agent should only be used when the charges account agent is different from the debtor agent.

This element is not widely used in the payment industry. It should also be noted that the ChargesAccountAgentRule inherited from the base message should be ignored as the optional Branch of DebtorAgent is removed from this Usage Guideline.

---

<!-- ELEMENT 71 -->
Credit Transfer Transaction Information

---

<!-- ELEMENT 72 -->
The pain.001 message contains **Payment Identification** which provides a set of elements to identify the payment of which several are mandatory elements.

| Instruction Identification | Min 0 – Max 1 |
| --- | --- |
| End to End Identification | Min 1 – Max 1 |
| UETR | Min 1 – Max 1 |

a point-to-point reference of 35 characters long will be returned to account statements if provided by the initiating party.

Note: Instruction Id is mandatory in other CBPR+ messages as it maps directly with the mandatory Sender's Reference (Field 20) of the legacy MT payment messages.

an end-to-end reference provided by the Debtor which must be passed unchanged throughout the payment and reported to the Creditor.  
note: if the Debtor has not provide an end-to-end identifier, the Debtor Agent may populate "NOT PROVIDED" to comply the mandatory need of this element.

the Unique End-to-end Transaction Reference created using the UUID v4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting messages.

---

<!-- ELEMENT 73 -->
The pain.001 **Payment Type Information** provides a set of optional elements where the payment type can be described.

| Service Level | Min 0 – Max 3 |
| --- | --- |
| Local Instrument | Min 0 – Max 1 |

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored.

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, INST – Instant Credit Transfer for SEPA Service Level.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends.

---

<!-- ELEMENT 74 -->
```markdown
# pain.001 Interbank Customer Credit Transfer Initiation - Currency and Amount

The pain.001 nested **Amount** element has a choice of either *Instructed Amount* or *Equivalent Amount* to capture the amount and currency of the Customer Credit Transfer Initiation.

## Instructed Amount
The *Instructed Amount* captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. This amount has to be transported unchanged through the transaction chain. This element is comparable with the legacy Field 33B.

## Equivalent Amount
The *Equivalent Amount* nested element captures currency and *Amount* of money to be moved between the Debtor and Creditor, before deduction of charges, and is expressed in the currency of the Debtor's account. The *Currency Of Transfer* element captures the equivalent currency to be transferred which the first agent will convert the credit transfer into.

---

<!-- ELEMENT 75 -->
```markdown
# Interbank Customer Credit Transfer Initiation - Exchange Rate Information

The pain.001 **Exchange Rate Information** element provides details on the currency exchange rate and contract.

| Element | Description |
| --- | --- |
| Unit Currency | Currency in which the rate of exchange is expressed in a currency exchange. For example, 1GBP = xxxCUR, the unit currency is GBP. |
| Exchange Rate | The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency. |
| Rate Type | Specifies the type used to complete the currency exchange, such as SPOT, SALE or AGRD (Agreed). |

Contract: Unique and unambiguous reference to the foreign

---

<!-- ELEMENT 76 -->
The **Charge Bearer** element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

| Charge Bearer (0.1) | Code | Description |
| --- | --- | --- |
| CRED | Creditor | ISO 20022 |
| DEBT | Debtor |  |
| SHAR | Shared |  |

### 71A: Details of Charges
| Code | Description |
| --- | --- |
| BEN | Beneficiary |
| OUR | Our Customer Charges |
| SHA | Shared Charges |

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 77 -->
The Cheque Instruction information block contains a set of elements needed to issue a cheque. The following types of cheques are commonly used in the market:

| Cheque Type | Code | Description |
| --- | --- | --- |
| Bank Cheque | BCHQ | Cheque drawn on the account of the debtor's financial institution, which is debited on the debtor's account when the cheque is issued. These cheques are printed by the debtor's financial institution and payment is guaranteed by the financial institution. Synonym is 'cashier's cheque'. |
| Customer Cheque | CCHQ | Cheque drawn on the account of the debtor and debited on the debtor's account when the cheque is cashed. Synonym is 'corporate cheque'. |
| Draft | DRFT | A guaranteed bank cheque with a future value date (do not pay before), which in commercial terms is a 'negotiable instrument': the beneficiary can receive early payment from any bank under subtraction of a discount. The ordering customer's account is debited on value date. |

The Delivery Method element specifies the method to be used in delivering the cheque by the Debtor Agent. For example, a code CRCR is used to courier the cheque to the Creditor.

---

<!-- ELEMENT 78 -->
The pain.001 message introduces **Ultimate Debtor** and **Ultimate Creditor**. The **Ultimate Debtor** element should not be confused with an **Initiating Party** who may send a payment initiation request on behalf of the **Debtor**, for example, Payment Factory.

CBPR+ premise is that an **Ultimate Debtor** has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an **Ultimate Creditor** has no financial regulated account relationship with the corresponding Creditor.

The **Ultimate Debtor** and **Ultimate Creditor** can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 79 -->
The pain.001 has three optional *Intermediary Agent* (1,2 and 3) elements. These agents represent the agent(s) that exist between the Debtor Agent and the Creditor Agent.

- If more than one intermediary agent is present, then **Intermediary Agent 1** identifies the agent between the Debtor Agent and the Intermediary Agent 2.
- If more than two intermediary agents are present, then **Intermediary Agent 2** identifies the agent between the Intermediary Agent 1 and the Intermediary Agent 3.
- If **Intermediary Agent 3** is present, then it identifies the agent between the Intermediary Agent 2 and the Creditor Agent.

More commonly the ISO 9362 Financial Institution *Business Identifier Code* is considered the best practice de facto standard for 'many to many' / correspondent banking payments.

Other options to identify the **Intermediary Agent** include:
- Clearing System Member ID
- LEI (Legal Entity Identifier)
- Name and either structured, or unstructured Postal Address

---

<!-- ELEMENT 80 -->
```markdown
# Interbank Customer Credit Transfer Initiation – Intermediary Agent Account

The pain.001 **Intermediary Agent (1,2 and 3) Accounts** are used to capture the account information related to these Agents.

## The Intermediary Agent Account

The **Intermediary Agent Account** uses a variety of nested elements to capture information related to the account.

| Element | Description |
| --- | --- |
| Identification | Identifies the account maintained at the Account Servicing Institution. |
| Type | Uses the external Cash Account Type code list to identify the type of account. |
| Currency | Identifies the currency of the account. |
| Name | Identifies the name of the account as assigned by the Account Servicing Institution. |
| Proxy | Captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used. |

## Intermediary Agent

Intermediary Agent is a Financial Institution, therefore the nested

---

<!-- ELEMENT 81 -->
The **Creditor Agent** is a static role in the pain.001 Customer Credit Transfer Initiation. This agent maintains a relationship with their customers, the *Creditor*.

Note: Although the *Debtor Agent*, *Creditor Agent*, *Debtor and Creditor* all maintain static roles in the pain messages, the description of these parties changes in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

---

<!-- ELEMENT 82 -->
The pain.001 **Creditor Agent Account** is used to capture the account information related to the Creditor Agent.

The **Creditor Agent Account** uses a variety of nested elements to capture information related to the account.

| Element | Description |
| --- | --- |
| Identification | Identifies the account maintained at the Account Servicing Institution |
| Type | Uses the external Cash Account Type code list to identify the type of account |
| Currency | Identifies the currency of the account |
| Name | Identifies the name of the account as assigned by the Account Servicing Institution |
| Proxy | Captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used. |

Debtor Agent and Creditor Agent are Financial Institutions, therefore

---

<!-- ELEMENT 83 -->
The ISO 20022 pain messages describe the **Creditor** as the party whose account was credited for a transaction. The Creditor sub elements describe the Creditor in greater detail.

| Postal Address |
| --- |
| Department |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Room |
| Post Code |
| Town Name |
| Town Location |
| District Name |
| Country Sub Division |
| Country Code |
| Address Line |

Nested element capturing either structured or unstructured Creditor address details.

Note: Structured address is strongly recommended with mandatory Town Name and Country

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Mandatory **Name** (where a BIC identifier is not provided) by which the party is known

Postal Address

Identification

Country of Residence

---

<!-- ELEMENT 84 -->
The pain.001 **Creditor Account** is used to capture the account information for which credit entry will be made as a result of the transaction, which will also be reflected in their account Statement.

The **Creditor Account** uses a variety of nested elements to capture information related to the account.

| Element | Description |
| --- | --- |
| Identification | identifies the account maintained at the Creditor Agent (Account Servicing Institution) |
| Type | uses the external Cash Account Type code list to identify the type of account |
| Currency | identifies the currency of the account |
| Name | identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) |
| Proxy | captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used. |

Creditor Account is not required for cheque payments.

---

<!-- ELEMENT 85 -->
The pain.001 message introduces **Ultimate Debtor** and **Ultimate Creditor**. The **Ultimate Debtor** element should not be confused with an **Initiating Party** who may send a payment initiation request on behalf of the **Debtor**, for example, Payment Factory.

CBPR+ premise is that an **Ultimate Debtor** has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an **Ultimate Creditor** has no financial regulated account relationship with the corresponding Creditor.

The **Ultimate Debtor** and **Ultimate Creditor** can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

---

<!-- ELEMENT 86 -->
The Instruction for Creditor Agent element within the pain.001 message optionally provides information related to the processing of the payment for the Creditor Agent.

The Instruction for Creditor Agent element offers a multiplicity of up to 2 occurrences of information. This element enables:
- the use of an embedded choice of code to describe the instruction (e.g. CHQB – Pay Creditor by Cheque)
- free format instruction information
- or both, where the free format complements the code.
The use of this element may be bilaterally agreed with the Creditor Agent. It must be passed on throughout the life cycle of the transaction until the payment reaches the Credit Agent.

---

<!-- ELEMENT 87 -->
```markdown
# ISO 20022 Programme

Quality data, quality payments

## CBPR+ User Handbook

SR 2023 Edition  
March 2023

---

<!-- ELEMENT 88 -->
The Instruction for Debtor Agent element within the pain.001 message optionally provides information related to the processing of the payment.

The Instruction for Debtor Agent element offers a maximum of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the Debtor Agent, depending on bilateral agreement.

---

<!-- ELEMENT 89 -->
The Purpose element within the pain.001 message captures the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment, e.g., IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Debtor.

| The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.
For example, LIMA is classified within the Cash Management categorisation, with the Name Liquidity Management described as a Bank initiated account transfer to support zero target balance management, pooling or sweeping. |

Category Purpose also captures a high-level purpose, which unlike Purpose is less granular but can trigger special processing e.g., Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

Credit Transfer Transaction Information

---

<!-- ELEMENT 90 -->
The **Regulatory Reporting** block within the pain.001 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

The **Debit Credit Reporting Indicator** utilises an embedded choice of code to indicate whether the regulatory reporting applies to the:
- DEBT (debit)
- CRED (credit)
- BOTH

The **Authority** element captures the Name and Country code of the Authority/Entity requiring the regulatory reporting information.

The **Details** element provides the detail on the regulatory reporting information.

---

<!-- ELEMENT 91 -->
The pain.001 nested **Tax** element captures information related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s).

This element caters for two main types of tax-related payments:
- Tax payment obligation that is required to be transmitted with a payment
- Information that accompanies an actual payment of a tax obligation

The following nested elements may be used to capture detailed tax information:

| Creditor | Debtor | Administration Zone | Reference Number | Method | Total Taxable Base Amount |
| --- | --- | --- | --- | --- | --- |
| **Min 0 – Max 1** | **Min 0 – Max 1** | **Min 0 – Max 1** | **Min 0 – Max 1** | **Min 0 – Max 1** | **Min 0 – Max 1** |

| Total Tax Amount | Date | Sequence Number | Record |
| --- | --- | --- | --- |
| **Min 0 – Max 1** | **Min 0 – Max 1** | **Min 0 – Max 1** | **Min 0 – Max *** |

Tax information block is also available within the Structured Remittance Information block which is applicable when tax information is used by the creditor as part of remittance information.

---

<!-- ELEMENT 92 -->
The **Related Remittance Information** element within the pain.001 message is nested to provide information related to the handling of remittance information.

The **Remittance Identification** captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction.

The **Remittance Location Details** uses a set of nested elements to provide information on either the location of or the delivery of remittance information.
- **Method** requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. **EMAIL (email)**
- **Electronic Address** provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.
- **Postal Address** provides the postal address to which an agent is to send the remittance information

Unlike CBPR+ pacs messages, in the interbank pain.001 message, Related Remittance Information and Remittance Information are non-mutually exclusive due to a corporate use case of populating both information blocks for detailing remittance advices which are part of value-added service offered by the **Debtor Agent**.

SCORE Guideline: If the Related Remittance Information is used, and a Remittance Identification is provided, it is recommended that the Remittance Identification equal the End To End Identification.

---

<!-- ELEMENT 93 -->
The optional **Remittance Information** element within the pain.001 message is nested to provide either Structured or Unstructured information related to payment, such as invoices.

**Remittance Information** enables the matching/reconciliation of an entry that the payment is intended to settle.

The **Unstructured** sub element captures free format Remittance Information which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

The **Structured** element is nested capturing rich structured Remittance Information, and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification) The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-to-end transportation of this data.

Recommend to refer to CGI-MP Document Centre for Country

---

<!-- ELEMENT 94 -->
The bilaterally/multilaterally agreed **Remittance Information** which is **Structured** must not exceed 9,000 characters of business content (i.e., the information). This nested element is used to capture a variety of structured remittance information.

| Structured |
| --- |
| Reference Document Information |
| Type |
| Code Or Proprietary |
| Code |
| Number |
| Related Date |

The **Creditor Remittance Information** is provided to the **Creditor** in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.

In this example Referred Document Information and its nested elements have multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.

---

<!-- ELEMENT 95 -->
The Creditor Reference in the Creditor Remittance Information component in the structured remittance information is generated by Creditor to inform the Debtor who has to include the reference in the Remittance Information component of the pain.001.

Creditor Reference in the Structured Remittance Information is based on ISO 11649
- 2 letters "RF"
- 2 digits check digit
- 21 letters/digits creditor reference

Facilitates STP and auto-match with the creditor reference and its account receivable
- A vendor can add the creditor reference to its invoice. When a customer pays the invoice, they write the creditor reference instead of the invoice number in the payment message (e.g., MT 101 F70 which will be carried in MT 103)
- When the vendor receives the payment, it can auto-match the incoming credit entry and the creditor reference extracted from the statement (e.g., MT 940 F61/86)

SCORE Guideline: For Creditor Reference information, in instances where the Creditor Reference Type code is SCOR (Structured Communication Reference) and the Creditor Reference is structured in accordance with ISO 11649, the

---

<!-- ELEMENT 96 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g., a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

Interbank Customer Credit Transfer Initiation - Relay

* Use Case pn.1.1.1 – High Level Payment Initiation Interbank 'relay' (pain.001)
* Use Case pn.1.1.1.a – High Level Payment Initiation Interbank 'relay' (pain.001) Multi-bank Sweep
* Use Case pn.1.1.2 – High Level Payment Initiation Interbank 'relay' (pain.001) involving a Payment Market Infrastructure

Interbank Customer Credit Transfer Initiation - Authorised Party

* Use Case pn.1.2.1 – High Level Payment Initiation Interbank (pain.001) by an Authorised Party
* Use Case pn.1.2.1.a. – High Level Payment Initiation Interbank (pain.001) FI-Initiated Sweep (Long position at the Secondary Account)
* Use Case pn.1.2.1.b. – High Level Payment Initiation Interbank (pain.001) by an Authorised Party to pay themselves as the Creditor

Interbank Customer Credit Transfer Initiation - Financial Institution

* Use Case pn.1.3.1 – High Level Payment Initiation Interbank (pain.001) Financial Institution Payment Initiation

---

<!-- ELEMENT 97 -->
In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor and initiate a credit transfer.

| Initiating Party sends a payment instruction to the Forwarding Agent |
| --- |
| 1 |

| Forwarding Agent (F) forwards the payment instruction to the Debtor Agent (A) |
| --- |
| 2 |

| Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008 |
| --- |
| 3 |

| Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the |
| --- |
| 3a |

| Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the initiating Party, based upon a bilateral agreement |
| --- |
| 3b |

| Creditor Agent (B) processes the payment and sends the statement to Creditor |
| --- |
| 4 |

---

<!-- ELEMENT 98 -->
In the interbank relay scenario, the Forwarding Agent relaying the pain.001 message to the Debtor Agent(s) in this case to sweep excess cash from the account of the Debtor and consolidate cash for a Corporate.

| Initiating Party sends a payment instruction to the Forwarding Agent to sweep excess funds from its subsidiary's account to the master account with Bank B |
| --- |
| Forwarding Agent (F) forwards the payment instruction to the |
| Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008 |
| Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the |
| Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the initiating Party, based upon a bilateral agreement |
| Creditor Agent (B) processes the payment and notifies Creditor of a successful sweep through the |

---

<!-- ELEMENT 99 -->
# Market Infrastructure

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor initiate a credit transfer through a Payment Market Infrastructure.

| Step | Description |
| --- | --- |
| 1 | Initiating Party sends a payment instruction to the Forwarding Agent |
| 2 | Forwarding Agent (F) forwards the payment instruction to the Debtor Agent (A) |
| 3a | Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the Forwarding Agent (F), based upon a bilateral agreement |
| 3b | Interbank pain.001 |
| 4 | Creditor Agent (B) receives local credit transfer message via the Payment Market Infrastructure (PMI) and credits the Creditor |

| Step | Description |
| --- | --- |
| 1 | Initiating Party sends a payment instruction to the Forwarding Agent |
| 2 | Forwarding Agent (F) forwards the payment instruction to the Debtor Agent (A) |
| 3a | Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008 to a Payment Market Infrastructure (PMI) |
| 3b | Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement |
| 4 | Creditor Agent (B) receives local credit transfer message via the Payment Market Infrastructure (PMI) and credits the Creditor

---

<!-- ELEMENT 100 -->
In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place between the Debtor and the Debtor Agent

| DA | Debit Authorisation |
| --- | --- |
| 1 | Interbank pain.001 |
| 2 | Interbank pain.002 |

As a pre-requisite the Debtor provides Debit Authorisation to Agent A, which allows Agent I to Initiate Payment from their account

Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 statement at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

---

