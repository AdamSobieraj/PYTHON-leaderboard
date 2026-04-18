<!-- ELEMENT 1 -->
U
Preface
| This Cross-Border Payment    | The use cases focus on a  | Note:  |
| ---------------------------- | ------------------------- | ------ |
| Reporting plus (CBPR+) User  | core topics where other   |        |
Handbook is intended to  relevant messages may  This document jointly
document and explain a  also be referred to within  developed with the CBPR+
variety of ISO 20022 payment  the use case, it may also be  group continues to evolve
related topics, as well as  necessary to consider other  inline with the Standards
provide practical use cases to  documented use cases, in  Release as:
| ensure a common  | order to capture a wider  |     |
| ---------------- | ------------------------- | --- |
understanding and adoption of  variation of scenarios. • CBPR+ continue to
| ISO 20022 within the payment  |     | develop market practice    |
| ----------------------------- | --- | -------------------------- |
| industry.                     |     | guidelines for additional  |
message.
The SWIFT FINplus service
| will support CBPR+ messages  |     | • Inaccuracies are  |
| ---------------------------- | --- | ------------------- |
identified and corrected.
on the SWIFT network
| traditionally associated with  |     | • Further use cases  |
| ------------------------------ | --- | -------------------- |
and/or explanation
correspondent banking (many-
needs are identified
to-many). These messages
may be exchanged either
between Agents in the same
country or between Agents in
different countries.
1

---

<!-- ELEMENT 2 -->
Change log (since last iteration)
Updated – note
Page 2
Updated – new messages added to index
Page 5
Updated – new messages added to index
Page 6
Updated – correction of Intermediary code
Page 11
Updated – new messages and Usage Ids added
Page 33
Updated – new pain message added to index
Page 40
Updated – recognition of Payment Initiation relay rulebook
Page 45
Updated – recognition of Payment Initiation relay rulebook
Page 107
Updated – additional use cases in the index
Page 122
New –use case
Page 126
Page 134
New – use case
Page 135-182 New – pain.008 message section
Page 184
Page 204
Page 351
Page 371
Page 379-380 New – pacs.003 use cases
Page 400
Page 423
Page 458-488 New – pacs.010 Margin Collection section
Page 489-529 New – pacs.003 Customer Direct Debit section
Page 530
Page 674
Page 682
Page 691
Page 698-716 New – camt.058 Notice to Received Cancellation section
Updated - new message added to index
Page 743
Page 764
Updated - use case id correction
Page 774-795 New – Customer Cancellation Request section
Page 823-883 New – Cheque message sections
Page 880

Update – new messages added to index
Update – removed refer to Wait For Settlement Market Practice
New – new high level message flow
Updated – new messages added to index

Updated – additional guidance on ultimate parties on the return
Updated – correct to Agent description in Step 7

Updated - use case id correction

Updated – new message added to index
Updated – removed reference to SR 2023
Updated – moved reference to multiple notification, now at an Item level
Updated – reference to multiple notification item Rule

U

The following  icons dignify  changes to slide from the previous  itineration.
Updates  to text on a slide are captured in gold.

New slide since last iteration

U

Slide updated  since last iteration
2

---

<!-- ELEMENT 3 -->
Legend
| Message type and direction |     | Payment Initiation  | (pain) |
| -------------------------- | --- | ------------------- | ------ |
Exception & Investigation  Case Assigner
Optional Message type and direction
Payment Clearing and Settlement (pacs)
Exception & Investigation  Case Assignee
Focal Message type and direction
Cash Management Reporting (camt)
| pacs Debtor | Statement Account Owner |     |     |
| ----------- | ----------------------- | --- | --- |
Cash Management Exception &
|     |     | Investigations  (camt) |     |
| --- | --- | ---------------------- | --- |
pacs Creditor
Statement Account Servicer
Focus message
pacs.008 Ultimate Debtor
Statement Authorised Party
Element Hierarchy Path
pacs.008 Ultimate Creditor
Nested Element
Initiating  party on behalf of the Debtor
Shortcut to other part of document
Element Choice
Agent
Extra attention is needed
Nested Element involving a choice
Agent processing legacy format
MT
|     | Legacy FIN MT message | New slide since last iteration |     |
| --- | --------------------- | ------------------------------ | --- |
during a coexistence period
|                          | gpi Tracker        | Slide updated since last iteration |     |
| ------------------------ | ------------------ | ---------------------------------- | --- |
| Market Infrastructure    | U                  |                                    |     |
| Exceptional circumstance | Use Case variation | Best practice                      |     |
3

<!-- Obraz ze strony 3 (112x118px) -->
```markdown
<!-- No text or tables found in the image -->
```

<!-- Obraz ze strony 3 (93x83px) -->
```markdown
```

<!-- Obraz ze strony 3 (132x153px) -->
gpi

---

<!-- ELEMENT 4 -->
U

Table of contents

1.

2.

3.

Introduction to ISO 20022

Business Application Header

Payment Initiation (pain)

pain.001 - Interbank Customer Credit Transfer Initiation

pain.002 - Interbank Customer Payment Status Report

pain.008 – Customer Direct Debit Initiation

new  for SR2023

4. Payment, Clearing and Settlement (pacs) messages

pacs.002 – Financial Institution to Financial Institution Payment Status Report

pacs.004 – Payment Return

pacs.003 – Financial Institution to Financial Institution  Customer Direct Debit

new  for SR2023

pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer

pacs.009 (core) - Financial Institution Credit Transfer

pacs.009 (cov) - Financial Institution ‘Cover’ Credit Transfer

pacs.009 (adv) – Financial Institution ‘Advice’ Credit Transfer

pacs.010 – Financial Institution Direct Debit

pacs.010 – Financial Institution Direct Debit – Margin Collection

new  for SR2023

4

---

<!-- ELEMENT 5 -->
Table of contents (continued)

5. Cash Management Reporting (camt) messages

camt.052 - Bank to Customer Account Report

camt.053 - Bank to Customer Statement

camt.054 - Bank to Customer Debit Credit Notification

camt.057 – Notification to Receive

camt.058 – Notification to Receive Cancelation Advice

new  for SR2023

6. Cash Management Exception & Investigation (camt) messages

camt.029 - Resolution of Investigation

camt.055 – Customer Payment Cancelation Request

new  for SR2023

camt.056 - FI to FI Cancellation Request

7. Cheques

camt.107 – Cheque Presentment Notification

new  for SR2023

camt.108 – Cheque Cancellation or Stop Notification

new  for SR2023

camt.109 – Cheque Cancellation or Stop Report

new  for SR2023

U

5

---

<!-- ELEMENT 6 -->
Introduction to ISO 20022

6

---

<!-- ELEMENT 7 -->
Introduction to ISO 20022

ISO 20022 introduces a
fundamental change to the
traditional language used by the
payments industry for several
decades. It also describes
participants (i.e., parties) to a
business transaction  differently
based upon the business domain
(area) being described, in a similar
way you may describe a person as a
colleague, parent or sibling
depending upon the context you
wish to describe them. This section
is designed to capture and explain
some of the differences.

7

---

<!-- ELEMENT 8 -->
Message
Sets

Message
Definition

Domain

Introduction to ISO 20022 – Business Domains

Domains

Message Sets

Payment and Cash Management
Securities
Trade Services
Foreign Exchange
Card Payment

Message  Definitions

acmt
auth
camt
pacs
pain
remt

Account Management
Authorities
Cash Management
Payment Clearing and Settlement
Payment Initiation
Payment Remittance Advice

camt.052  Bank  to Customer  Account Report
camt.053  Bank  to Customer  Statement
camt.054  Bank  to Customer  Debit  Credit  Notification
camt.056  FI  to FI  Payment  Cancellation  Request
camt.057  Notification  to Receive

pacs.002 FI  to FI  Payment  Status Report
pacs.004 Payment  Return
pacs.008 FI  to FI  Customer  Credit  Transfer
pacs.009 Financial  Institution  Credit  Transfer

pain.001  Customer  Credit  Transfer initiation
pain.002  Customer  Payment  Status Report
pain.012  Creditor  Payment  Activation Request

ISO 20022 catalogue messages hierarchically beginning with a
Business Domain, contain a various sets of Message Definitions, which
in turn contain a variety of Message Sets.

for example:
➢ Payment and Cash Management

➢ Payments Clearing and Settlement

➢ FI to FI Customer Credit Transfer (pacs.008)

8

<!-- Obraz ze strony 8 (112x102px) -->
No text found in the image.

---

<!-- ELEMENT 9 -->
Introduction to ISO 20022 - Message Identifier

4!a . 3!c . 3!n . 2!n

Example

pacs.008.001.08

Version

Variant

Message identifier/functionality

Business area

Version  8

Variant  1

FI To FI  Customer
Credit Transfer

Payments Clearing and
Settlement

9

---

<!-- ELEMENT 10 -->
U
|     |     |     |     |     |     |     |     |     |     | Legend: | ISO 20022 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- |
What is changing? Party Identifiers
New parties  :XX FIN MT format
introduced in
equivalent
ISO 20022
Payment Initiation (pain) Payments Clearing & Settlement (pacs) Cash Management
(camt)
|     |     |     | :72:/INS/ |     | :53a | :54a | :55a | :56a | :72:/INTA/ |     |     |
| --- | --- | --- | --------- | --- | ---- | ---- | ---- | ---- | ---------- | --- | --- |
Ultimate  Forwarding  Previous Instructing  Reimbursement Intermediary
Ultimate
| Debtor | Agent |     | Agents  |     |     | Agents  |     |     | Agents  |     |     |
| ------ | ----- | --- | ------- | --- | --- | ------- | --- | --- | ------- | --- | --- |
Creditor
|     |     | 1   | 2   | 3   | 1   | 2   | 3   | 1   | 2   | 3   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Debtor Initiating  Debtor  Instructing Instructed Creditor  Creditor
|      | Party | Agent |     | Agent  |     |     | Agent    |     |     | Agent |      |
| ---- | ----- | ----- | --- | ------ | --- | --- | -------- | --- | --- | ----- | ---- |
| :50a |       | :52a  |     | Sender |     |     | Receiver |     |     | :57a  | :59a |
10

---

<!-- ELEMENT 11 -->
SWIFT FINplus  Message structure

The diagram attempts to explain the
construct of an ISO 20022 message sent
across the SWIFT network using the
FINplus service (which is designated to
support various ISO 20022 business
domains on SWIFT Interact)

Within the CBPR+ User Handbook the
predominant focus is on the Request
Payload, as this is where the business
information is contained. However, it is
worth noting that a network provider will
have additional containers around the
Request Payload to perform functionality
on its network. This diagram presents the
additional containers on the SWIFT
network such as the Request Header
often referred to as the Technical Header
of the message.

<AppHdr>
…
</AppHdr>

<Document>

…

</Document>

ISO 20022
Business
Application  Header

ISO 20022
Message

Business
Message

11

---

<!-- ELEMENT 12 -->
XML Elements

XML Elements
An XML instance or document contains data in elements and nested elements (elements which contain other elements) corresponding to the hierarchy
imposed by the XML schema.
In the CBPR+ Usage Guidelines we often refer to the element hierarchy by levels (to understand the nested
relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example in a pacs.008 Customer Credit Transfer
the Interbank Settlement Date is a sub-element (Level 2) of the Credit Transfer Transaction Information element (Level 1).

Naming  conventions
An XML  element is named according to the following  rules:

• The name can contain letters, numbers, and other characters, but must not start with a number or punctuation  mark.
• The name must not start with XML,  xml, or Xml.
• The name must not contain  any spaces.

MX naming  conventions
There are some generic naming rules that apply  to most items in the database.

• The names of all items in the database use the upper CamelCase convention,  as follows:

• Each word starts with a capital letter.
• There are no white spaces between  words.

• A name may be made up of multiple  words, each consisting of alphanumeric  characters.
• Words use British English vocabulary.
• All  names must start with an alphabetic  character.
• All  characters that follow the first characters must be letters or numbers.

Example  of a Street Name element: <StrtNm>Oxford Street</StrtNm>

Element Multiplicity

Required element

Optional element

Unlimited element occurrences

MX message element multiplicity  (occurrences)
An MX  message element specifies its cardinality  (number of elements in a set) using minimum (min) & maximum (max) to describe the occurrences.

12

<!-- Obraz ze strony 12 (208x383px) -->
| Min | Max |
|---|---|
| | |
| 1 | 1 |
| 0 | 1 |
| 0 | * |

<!-- Obraz ze strony 12 (231x106px) -->
- Credit Transfer Transaction Information
    - Interbank Settlement Amount
    - Interbank Settlement Date

---

<!-- ELEMENT 13 -->
XML Elements (continued)
| Empty | XML Elements |     |     |     |     |
| ----- | ------------ | --- | --- | --- | --- |
An empty XMLelement is an element that contains no data content and therefore is described as empty. Although this makes little business sense,
this is a knownfeature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does
not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested
element.
| Acommonexample |     | of this is | in payment message | is Financial | Institution. |
| -------------- | --- | ---------- | ------------------ | ------------ | ------------ |
Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e.,
<FinInstnId></FinInstnId>
In the FINplus service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where
| business | data should | beprovided | within a nested | element, | it is provided. |
| -------- | ----------- | ---------- | --------------- | -------- | --------------- |
13

---

<!-- ELEMENT 14 -->
XML Elements within CBPR+ User Hand Book
MyStandards describes the element’s context by its path whereby each element is divided by a forward slash (/) For example the pacs.008 Town
Name within the Debtor PostalAddress is described as /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/PstlAdr/TwnNm
Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing
| the element | in an XML | naming convention. |     |     |     |
| ----------- | --------- | ------------------ | --- | --- | --- |
For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment
| Identification | is an element | below | Credit Transfer                   | Transaction | Information.           |
| -------------- | ------------- | ----- | --------------------------------- | ----------- | ---------------------- |
|                |               |       | Credit Transfer Transaction Info’ |             | Payment Identification |
In this way the CBPR+ User Hand Book uses three main icon to explain the relationships between element, by display the icon after the element
name.
|     | To visualise | an element | whichhas | nested elements | beneath it |
| --- | ------------ | ---------- | -------- | --------------- | ---------- |
To visualise an element whichhas a choiceassociated withit i.e., aCode where achoice of which codecan bedetermined
To visualise an element which is nested and has a choice associated with it. For example, an Identification where a choice must be
made between an Organisation Identification and a Private Identification element which is nested, but where both cannot be used
together.
14

---

<!-- ELEMENT 15 -->
The CBPR+ group has published all its usage guidelines in MyStandards

https://www2.swift.com/mystandards/#/c/cbpr/landing

15

---

<!-- ELEMENT 16 -->
Message Usage Guideline – Additional Information and principals
| Many           | of  | the      | CBPRplus     |        |            | Usage    |
| -------------- | --- | -------- | ------------ | ------ | ---------- | -------- |
| Guidelines     |     | have     | useful       | key    | principals |          |
| and additional |     |          | information. |        | These      | can      |
| be expanded    |     | in       | MyStandards  |        | by         | clicking |
| on ‘show       |     | details’ | in the       | middle |            | of the   |
UsageGuidelinedescriptionpane.
16

<!-- Obraz ze strony 16 (1654x303px) -->
# Cross Border Payments and Reporting Plus
**PUBLISHED** | MyStandards

## CBPRPlus-pac.008.001.08_FIToFICustomerCreditTransfer
**CBPRPlus_ISO 20022 Portfolio_November 2022_Release 2.0** (Technical version: 1, Version: V2.0 FOR IMPLEMENTATION, Format: MX, Status: Final)
**Usage Identifier:** swift.cbprplus.01 **Version:** V2.0 FOR IMPLEMENTATION **Status:** Final

Show details

---
Content | **Result View** | History | Sample Messages
---

[ ] Show xml tags | FI To FI Customer Credit Transfer V08 (pac.008.001.08)

<!-- Obraz ze strony 16 (154x83px) -->
Show details

---

<!-- ELEMENT 17 -->
Rules
Traditionally in the Legacy FIN standard rules related to a message were described as either Network Validation Rules –
those validated by the network, or Usage rules – rules not validated by the network. FIN also has the concept of Usage
| Guidelines–guidelineto |     | recommend | a best practice. |
| ---------------------- | --- | --------- | ---------------- |
In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated
| UsageGuideline(e.g. | CBPRplus) |     |     |
| ------------------- | --------- | --- | --- |
WithinCBPR+UsageGuidelinespecificationtherules dedicateto CBPR+are oftendescribedas:
Formal Rules which are validated on the network, these are identified by the word Rule appended to the rule
description.Forexample:
Rule “CBPR_Party_Name_Any_BIC_FormalRule”
Textual Rules which are not validated on the network, these are identified by with the word TextualRule
|     | appendedto | the rule | description.Forexample: |
| --- | ---------- | -------- | ----------------------- |
Rule “CBPR_Agent_Option_1_TextualRule”
Guideline Rules which provide recommended best practice, these are identified by the word Guideline
|     | appendedto | the rule | description.Forexample: |
| --- | ---------- | -------- | ----------------------- |
Rule “CBPR_Purpose_Guideline”
Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a
CrossElementSimpleRuleand a CrossElementComplexRule
17

---

<!-- ELEMENT 18 -->
Usage  Identifier  – Format

“<Short issuer organisation>.<Business context>{.<Business context>} n times.<version>

1-10 chars
A

1-10 chars
B

1 char

1-10 chars
C, D,…

1 char

2 chars
E

1 char

• Type: String
• Max allowed size: 35 characters
• Structure:

Total max 35 char

o Must  contain minimum A  & B, optionally  followed  by 1 or more additional business context elements (C, D, …).
o Always  ends with version element E (format “nn”, e.g., “01”)
o Each element  is separated by a period “.”
o
o Consistency enforced by lightweight  SWIFT review/registration:  E.g.,  “ecb” to represent the ECB, not “eucb”
o

Length  of each text element  can vary up to max  10 characters. Total  length,  including  periods, cannot exceed 35 chars.

Lowercase alphanumerical  characters only

In CBPR+ the Usage Identifier is captured within the Business Application Header, Business
Service element. More detail can be found in the dedicated Business Application Header chapter
of this document,

18

---

<!-- ELEMENT 19 -->
ISO 20022 External Code Lists

Many ISO 20022 message use data elements  represented by codes. Such codes are often
externalised  from the message itself, enabling  maintenance  of the code list on a quarterly basis
without requiring  a new message version.
Some data element  may also be embedded in  the message.

example of Charge Bearer in pacs.008 v8
which uses embedded codes

example of Return Reason Information in
pacs.004 v9 which uses externalised codes

Proprietary Codes may also be available  for certain data elements.
These are typically inherited  from legacy formats and require
definitions  in  user documentation  as these are not captured in  the
baseline  ISO 20022 standards

https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets

XLSX  format is readable in MS Excel

19

<!-- Obraz ze strony 19 (255x231px) -->
# Type
ExternalReturnReason1Code (based on string )
- minLength: 1
- maxLength: 4

# Definition
Reason for the return, as published in an external reason code list.

---

