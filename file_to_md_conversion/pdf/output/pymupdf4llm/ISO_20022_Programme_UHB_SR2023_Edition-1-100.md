<!-- ELEMENT 1 -->
This Cross-Border Payment Reporting plus (CBPR+) User Handbook is intended to document and explain a variety of ISO 20022 payment related topics, as well as provide practical use cases to ensure a common understanding and adoption of ISO 20022 within the payment industry. 

The SWIFT FINplus service will support CBPR+ messages on the SWIFT network traditionally associated with correspondent banking (manyto-many). These messages may be exchanged either between Agents in the same 

The use cases focus on a core topics where other relevant messages may also be referred to within the use case, it may also be necessary to consider other documented use cases, in order to capture a wider variation of scenarios. 

Note: 

This document jointly developed with the CBPR+ group continues to evolve inline with the Standards Release as: 

- CBPR+ continue to develop market practice guidelines for additional message. 

- Inaccuracies are identified and corrected. 

- • Further use cases and/or explanation needs are identified

---

<!-- ELEMENT 2 -->
|Page|2|Updated – note|
|---|---|---|
|Page|5|Updated – new messages added to index|
|Page|6|Updated – new messages added to index|
|Page|11|Updated – correction of Intermediary code|
|Page|33|Updated – new messages and Usage Ids added|
|Page|40|Updated – new pain message added to index|
|Page|45|Updated – recognition of Payment Initiation relay rulebook|
|Page|107|Updated – recognition of Payment Initiation relay rulebook|
|Page|122|Updated – additional use cases in the index|
|Page|126|New –use case|
|Page|134|New – use case|
|Page|135-182|New – pain.008 message section|
|Page|184|Update – new messages added to index|
|Page|204|Update – removed refer to Wait For Settlement Market Practice|
|Page|351|New – new high level message flow|
|Page|371|Updated – new messages added to index|
|Page|379-380|New – pacs.003 use cases|
|Page|400|Updated – additional guidance on ultimate parties on the return|
|Page|423|Updated – correct to Agent description in Step 7|
|Page|458-488|New – pacs.010 Margin Collection section|
|Page|489-529|New – pacs.003 Customer Direct Debit section|
|Page|530|Updated – new message added to index|
|Page|674|Updated – removed reference to SR 2023|
|Page|682|Updated – moved reference to multiple notification, now at an_Item_level|
|Page|691|Updated – reference to multiple notification item Rule|
|Page|698-716|New – camt.058 Notice to Received Cancellation section|
|Page|743|Updated - new message added to index|
|Page|764|Updated - use case id correction|
|Page<br>Page|774-795<br>823-883|New – Customer Cancellation Request section<br>New – Cheque message sections|



The following icons dignify changes to slide from the previous itineration.

---

<!-- ELEMENT 3 -->
**==> picture [39 x 77] intentionally omitted <==**

Message type and direction 

Exception & Investigation Case Assigner 

Optional Message type and direction Focal Message type and direction 

Exception & Investigation Case Assignee 

pacs Debtor Statement Account Owner pacs Creditor Statement Account Servicer pacs.008 Ultimate Debtor Statement Authorised Party pacs.008 Ultimate Creditor Initiating party on behalf of the Debtor Shortcut to other part of document Agent Extra attention is needed Agent processing legacy format **MT** Legacy FIN MT message during a coexistence period Market Infrastructure gpi Tracker 

**==> picture [31 x 285] intentionally omitted <==**

Payment Initiation (pain) 

Payment Clearing and Settlement (pacs) Cash Management Reporting (camt) Cash Management Exception & Investigations (camt) Focus message Element Hierarchy Path Nested Element Element Choice Nested Element involving a choice 

New slide since last iteration **U** Slide updated since last iteration

---

<!-- ELEMENT 4 -->
**1. Introduction to ISO 20022** 

**2. Business Application Header** 

**3. Payment Initiation (pain) pain.001 - Interbank Customer Credit Transfer Initiation pain.002 - Interbank Customer Payment Status Report pain.008 – Customer Direct Debit Initiation** new  for SR2023 

**4. Payment, Clearing and Settlement (pacs) messages** 

**pacs.002 – Financial Institution to Financial Institution Payment Status Report – pacs.004 Payment Return** 

**pacs.003 – Financial Institution to Financial Institution  Customer Direct Debit pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer pacs.009 (core) - Financial Institution Credit Transfer pacs.009 (cov) - Financial Institution ‘Cover’ Credit Transfer** 

new  for SR2023 

**pacs.009 (adv) – Financial Institution ‘Advice’ Credit Transfer**

---

<!-- ELEMENT 5 -->
**5. Cash Management Reporting (camt) messages camt.052 - Bank to Customer Account Report camt.053 - Bank to Customer Statement camt.054 - Bank to Customer Debit Credit Notification camt.057 – Notification to Receive camt.058 – Notification to Receive Cancelation Advice** new  for SR2023 **6. Cash Management Exception & Investigation (camt) messages camt.029 - Resolution of Investigation camt.055 – Customer Payment Cancelation Request** new  for SR2023 **camt.056 - FI to FI Cancellation Request 7. Cheques camt.107 – Cheque Presentment Notification** new  for SR2023 **camt.108 – Cheque Cancellation or Stop Notification** new  for SR2023 **camt.109 – Cheque Cancellation or Stop Report** new  for SR2023

---

<!-- ELEMENT 7 -->
ISO 20022 introduces a fundamental change to the traditional language used by the payments industry for several decades. It also describes participants (i.e., parties) to a business transaction  differently based upon the business domain (area) being described, in a similar way you may describe a person as a colleague, parent or sibling depending upon the context you wish to describe them. This section is designed to capture and explain some of the differences.

---

<!-- ELEMENT 8 -->
## **Domains** 

**Payment and Cash Management** Securities 

Trade Services Foreign Exchange Card Payment 

**Message  Definitions** 

**acmt** Account Management **auth** Authorities **camt** Cash Management **pacs** Payment Clearing and Settlement **pain** Payment Initiation **remt** Payment Remittance Advice 

**==> picture [139 x 173] intentionally omitted <==**

**----- Start of picture text -----**<br>
Message<br>Sets<br>Message<br>Definition<br>Domain<br>**----- End of picture text -----**<br>


## **Message Sets** 

camt.052 Bank to Customer Account Report camt.053 Bank to Customer Statement 

camt.054 Bank to Customer Debit Credit Notification camt.056 FI to FI Payment Cancellation Request camt.057 Notification to Receive 

pacs.002 FI to FI Payment Status Report pacs.004 Payment Return pacs.008 FI to FI Customer Credit Transfer pacs.009 Financial Institution Credit Transfer 

pain.001 Customer Credit Transfer initiation pain.002 Customer Payment Status Report pain.012 Creditor Payment Activation Request 

ISO 20022 catalogue messages hierarchically beginning with a Business Domain, contain a various sets of Message Definitions, which . in turn contain a variety of Message Sets for example: 

➢ Payment and Cash Management ➢ Payments Clearing and Settlement

---

<!-- ELEMENT 9 -->
4!a . 3!c . 3!n . 2!n Version Variant Message identifier/functionality Business area 

## **Example** 

pacs.008.001.08 Version 8 Variant 1 FI To FI Customer Credit Transfer Payments Clearing and Settlement

---

<!-- ELEMENT 10 -->
**introduced in equivalent ISO 20022** 

## **Payment Initiation (pain)** 

## **Payments Clearing & Settlement (pacs)** 

**Cash Management (camt)** 

**==> picture [794 x 257] intentionally omitted <==**

**----- Start of picture text -----**<br>
:72:/INS/ :53a :54a :55a :56a :72:/INTA/<br>Ultimate  Forwarding  Previous Instructing  Reimbursement Intermediary<br>Ultimate<br>Debtor Agent Agents  Agents  Agents<br>Creditor<br>1 2 3 1 2 3 1 2 3<br>Debtor Initiating  Debtor  Instructing Instructed Creditor  Creditor<br>Party Agent Agent Agent Agent<br>:50a :52a Sender Receiver :57a :59a<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 11 -->
The diagram attempts to explain the construct of an ISO 20022 message sent across the SWIFT network using the **FINplus** service (which is designated to support various ISO 20022 business domains on SWIFT Interact) 

Within the CBPR+ User Handbook the predominant focus is on the **Request Payload,** as this is where the business information is contained. However, it is worth noting that a network provider will have additional containers around the Request Payload to perform functionality on its network. This diagram presents the additional containers on the SWIFT network such as the Request Header often referred to as the Technical Header of the message. 

**==> picture [386 x 251] intentionally omitted <==**

> <AppHdr> ISO 20022 

> … Business </AppHdr> Application Header 

> <Document> Business Message … ISO 20022

---

<!-- ELEMENT 12 -->
## **XML Elements** 

An XML instance or document contains data in elements and nested elements (elements which contain other elements) corresponding to the hierarchy imposed by the XML schema. In the CBPR+ Usage Guidelines we often refer to the element hierarchy by levels (to understand the nested relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example in a pacs.008 Customer Credit Transfer the _Interbank Settlement Date_ is a sub-element (Level 2) of the _Credit Transfer Transaction Information_ element (Level 1). 

## **Naming conventions** 

An XML element is named according to the following rules: 

- The name can contain letters, numbers, and other characters, but must not start with a number or punctuation mark. 

- The name must not start with XML, xml, or Xml. 

- The name must not contain any spaces. 

## **MX naming conventions** 

There are some generic naming rules that apply to most items in the database. 

- The names of all items in the database use the upper CamelCase convention, as follows: 

   - Each word starts with a capital letter. 

   - There are no white spaces between words. 

- A name may be made up of multiple words, each consisting of alphanumeric characters. 

- Words use British English vocabulary. 

- All names must start with an alphabetic character. 

- All characters that follow the first characters must be letters or numbers. 

## **Example of a Street Name element:** <StrtNm>Oxford Street</StrtNm> 

**==> picture [230 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
Element Multiplicity<br>Required element<br>Optional element<br>Unlimited element occurrences<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 13 -->
## **Empty XML Elements** 

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element. 

A common example of this is in payment message is Financial Institution. 

Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e., <FinInstnId></FinInstnId> 

In the **FINplus** service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where business data should be provided within a nested element, it is provided.

---

<!-- ELEMENT 14 -->
MyStandards describes the element’s context by its path whereby each element is divided by a forward slash (/) For example the pacs.008 Town Name within the Debtor Postal Address is described as /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/PstlAdr/TwnNm 

Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing the element in an XML naming convention. 

For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment Identification is an element below Credit Transfer Transaction Information. 

_Credit Transfer Transaction Info’ Payment Identification_ 

In this way the CBPR+ User Hand Book uses three main icon to explain the relationships between element, by display the icon after the element name. 

**==> picture [49 x 89] intentionally omitted <==**

To visualise an element which has nested elements beneath it 

To visualise an element which has a choice associated with it i.e., a Code where a choice of which code can be determined 

To visualise an element which is nested and has a choice associated with it. For example, an Identification where a choice must be made between an Organisation Identification and a Private Identification element which is nested, but where both cannot be used together.

---

<!-- ELEMENT 15 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
https://www2.swift.com/mystandards/#/c/cbpr/landing<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 16 -->
**==> picture [708 x 130] intentionally omitted <==**

Many of the CBPRplus Usage Guidelines have useful key principals and additional information. These can be expanded in MyStandards by clicking on ‘show details’ in the middle of the Usage Guideline description pane. 

**==> picture [420 x 195] intentionally omitted <==**

---

<!-- ELEMENT 17 -->
– Traditionally in the Legacy FIN standard rules related to a message were described as either _**Network Validation Rules**_ – those validated by the network, or _**Usage rules**_ rules not validated by the network. FIN also has the concept of _**Usage Guidelines**_ – guideline to recommend a best practice. 

In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated Usage Guideline (e.g. CBPR plus) 

Within CBPR+ Usage Guideline specification the rules dedicate to CBPR+ are often described as: 

**Formal Rules** which are validated on the network, these are identified by the word **Rule** appended to the rule description. For example: _**Rule “CBPR_Party_Name_Any_BIC_FormalRule”**_ 

**Textual Rules** which are not validated on the network, these are identified by with the word **TextualRule** appended to the rule description. For example: 

## _**Rule “CBPR_Agent_Option_1_TextualRule”**_ 

**Guideline Rules** which provide recommended best practice, these are identified by the word **Guideline** appended to the rule description. For example: _**Rule “CBPR_Purpose_Guideline”**_ 

Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a

---

<!-- ELEMENT 18 -->
## “ <Short issuer organisation> **.** <Business context>{ **.** <Business context>} n times **.** <version> 

**==> picture [419 x 47] intentionally omitted <==**

**----- Start of picture text -----**<br>
1-10 chars 1-10 chars 1-10 chars 2 chars<br>A 1 char B 1 char C, D,… 1 char E<br>**----- End of picture text -----**<br>


## Total max 35 char 

- Type: **String** 

- Max allowed size: **35 characters** 

## • Structure: 

- Must contain minimum **A & B** , **optionally followed by 1 or more additional business context elements (C, D, …).** 

- `o` Always **ends** with **version element E** (format “nn”, e.g., “01”) 

- Each element is separated by a period “.” 

- Length of **each** text element **can vary** up to **max 10** characters. Total length, including periods, cannot exceed 35 chars. 

- Consistency enforced by lightweight SWIFT review/registration: E.g., “ecb” to represent the ECB, not “eucb” 

- **Lowercase** alphanumerical characters only 

**==> picture [59 x 60] intentionally omitted <==**

In CBPR+ the Usage Identifier is captured within the _Business Application Header_ , _**Business Service**_ element. More detail can be found in the dedicated Business Application Header chapter of this document,

---

<!-- ELEMENT 19 -->
**==> picture [57 x 58] intentionally omitted <==**

Many ISO 20022 message use data elements represented by codes. Such codes are often externalised from the message itself, enabling maintenance of the code list on a quarterly basis without requiring a new message version. Some data element may also be embedded in the message. 

example of Charge Bearer in pacs.008 v8 which uses embedded codes 

example of Return Reason Information in pacs.004 v9 which uses externalised codes 

**==> picture [266 x 85] intentionally omitted <==**

**==> picture [284 x 86] intentionally omitted <==**

Proprietary Codes may also be available for certain data elements. These are typically inherited from legacy formats and require definitions in user documentation as these are not captured in the baseline ISO 20022 standards 

**==> picture [183 x 72] intentionally omitted <==**

---

<!-- ELEMENT 20 -->
All SWIFT ISO MX message elements (fields) which are defined (by data Type) as text are restricted to FIN X Characters: 

**a-z A-Z 0-9 / - ? : ( ) . , ' + .** 

Special characters are additionally allowed in: 

- All party (agents and non-agents) Name and Address elements. 

- The Related Remittance Information element 

Currencies in the payments should be expressed in ISO Currency Codes only (3Characters, e.g. EUR) 

Translation of any special character: **!#&%*=^_`{|}~";@[\]$ ><** into MT messages will be represented by a **. (Full Stop)** 

- The Remittance Information (structured & unstructured) element 

- The Email Address where included as part of a Proxy elements 

- City of Birth and Province of Birth elements nested in Private Identification 

- List of special characters: 

**==> picture [172 x 112] intentionally omitted <==**

**----- Start of picture text -----**<br>
$ ! \ %<br>*<br>< # ]<br>=<br>> & [<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 21 -->
**Point-to-point** refers to data passed within a message from one party to the next. This data will not necessarily be passed in subsequent messages. 

- ➢ For example: the _Instruction Identification element_ contains a reference meaningful to the party sending a message, subsequent messages in a payment transaction chain can expect the _Instruction Identification_ to be replaced by a reference meaningful to the party sending that message leg. 

**==> picture [75 x 17] intentionally omitted <==**

**End-to-end** refers to data passed throughout the transaction life cycle i.e. within a message from one party to the next and continued in subsequent messages. 

- ➢ For example: the _UETR element_ contains a Unique End-to-end Transaction Reference in accordance with the UUID version 4 standards. This same reference is used in all messages related to the payment transaction.

---

<!-- ELEMENT 22 -->
**==> picture [50 x 55] intentionally omitted <==**

ISO 20022 have a number of elements associated which allow for these messages with Agents Agents to be referenced by a variety of Financial Institution identifiers. More commonly the ISO 9362 Financial Institution BIC ( _BICFI_ ) is considered the best practice de facto standard for ‘many to many’ / correspondent banking payments. However other options include: 

_Clearing System Member Identifiers_ when accompanied with the _Clearing System Identification_ . _LEI_ (Legal Entity Identifier) 

_Name_ and either structured or unstructured _Postal Address_ . 

**==> picture [37 x 31] intentionally omitted <==**

**==> picture [141 x 15] intentionally omitted <==**

**----- Start of picture text -----**<br>
Back to previous page<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 23 -->
## Two common elements to ISO 20022 messages are _**Date**_ and _**DateTime.**_ 

CBPR+ usage guidelines _**DateTime**_ elements mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) note - milliseconds are optional. 

**10** 

The ISO 20022 _**Date**_ elements allow the date to include an offset. As a data model, shared by other business domains, an offset date can provide great business clarify, such as something expiring at the end of a business date. However, in payments such a date offset provides little business value, whereby should an offset be include with the date, this offset should be ignored.

---

<!-- ELEMENT 24 -->
|**Country**|**Code Name**|**MT Clearing**<br>**System code**|**ISO 20022 Clearing**<br>**System Identification**|
|---|---|---|---|
|**Australia**|Australian Bank State Branch Code (BSB)|AU|AUBSB|
|**Austria**|Austrian Bankleitzahl|AT|ATBLZ|
|**Canada**|Canadian Payments Association Payment<br>RoutingNumber|CC|CACPA|
|**China**|Bank Branchcode usedinChina|CN|CNAPS|
|**Germany**|German Bankleitzahl|BL|DEBLZ|
|**Greece**|HelenicBank IdentificationCode|GR|GRBIC|
|**Hong Kong**|HongKongBankCode|HK|HKNCC|
|**India**|Indian FinancialSystemCode|IN|INFSC|
|**Ireland**|Irish National Clearing Code|IE|IENCC|
|**Italy**|Italian Domestic Identification Code|IT|ITNCC|
|**Japan**|Japan Zengin Clearing Code|JP|JPZGN|
|**New Zealand**|New Zealand National Clearing Code|NZ|NZNCC|
|**Poland**|Polish National Clearing Code|PL|PLKNR|
|**Portugal**|Portuguese National Clearing Code|PT|PTNCC|
|**Russia**|Russian Central Bank Identification Code|RU|RUCBC|
|**South Africa**|South African National Clearing Code|ZA|ZANCC|
|**Spain**|Spanish Domestic Interbanking Code|ES|ESNCC|
|**Switzerland**|Swiss Clearing Code (BC Code)|SW|CHBCC|
|**Switzerland**|Swiss Clearing Code (SIC Code)|SW|CHSIC|
|**Taiwan**|Financial Institution Code|TW|TWNCC|



**==> picture [52 x 61] intentionally omitted <==**

For translation rules and comparison purposes this table provides a list of published MT National Clearing System codes again their equivalent ISO 20022 Clearing System Identification in the external code list.

---

<!-- ELEMENT 26 -->
**Min 0 – Max 1** 

The head.001 Business Application Header _**Character Set**_ element declares the character set, in addition to Latin, that is contained in the Business Document e.g. the pacs.008. 

**Ж œ** 

The _**Character Set**_ element uses the UnicodeChartsCode string to declare an additional character set, for example **Cyrillic** (Unicode range: 0400-04FF). 

**图 ݒ** 

This allows the party for which the message is addressed _**To**_ to know in advance the additional character set contained within the Business Document. In this the way message can be routed to a to the Character Set or handled as an specific application process exception if the Character Set is not appropriate for that business transaction. 

**==> picture [59 x 60] intentionally omitted <==**

Extending character sets is not intended in CBPR+ from the initial implementation of the service. This element is intended for use once extended character sets are implemented, whereby the string represented in this element can enable any necessary network validations, such as a closed

---

<!-- ELEMENT 27 -->
**Min 1 – Max 1** 

The head.001 Business Application Header _**From**_ element identifies the BIC of the party who created the Business Document (e.g. pacs.008). Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC. 

**==> picture [77 x 54] intentionally omitted <==**

A choice must be made for the BIC depending on the party it represents. _**Financial Institution Identification**_ which identifies a Financial Institution, and may be further complemented with 

- _**Clearing System Member Identification**_ 

- • _**LEI**_ 

as an additional identification. 

**==> picture [7 x 5] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

_From_

---

<!-- ELEMENT 28 -->
**Min 1 – Max 1** 

The head.001 Business Application Header _**To**_ element identifies the BIC of the party who will ultimately the Business Document Additional information on this also be process (e.g. pacs.008) optional party may captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC. 

**==> picture [81 x 62] intentionally omitted <==**

A choice must be made for the BIC depending on the party it represents. _**Financial Institution Identification**_ which identifies a Financial Institution, and may be further complemented with 

- _**Clearing System Member Identification**_ 

- • _**LEI**_ 

as an additional identification. 

**==> picture [7 x 5] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

_To_

---

<!-- ELEMENT 29 -->
**Min 1 – Max 1** 

The head.001 Business Application Header _**Business Message Identifier**_ element contains the _Message Identification_ captured within the Business Document’s Group Header. The content of this element should match the Business Document to avoid incorrect routing by the recipient. 

**==> picture [365 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
Business<br>Business Message<br>1A245878..<br>Application Identifier<br>Header<br>Group Header<br>Business<br>Message<br>1A245878..<br>Document Identification<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 30 -->
**Min 1 – Max 1** 

The head.001 Business Application Header _**Message Definition Identifier**_ element contains the name of the Business Document. The content of this element should match the Business Document to avoid incorrect routing by the recipient. 

**==> picture [353 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
Business<br>Message Definition<br>pacs.009.001.08<br>Application Identifier<br>Header<br>Message<br>Identification<Document “pacs.009.001.08” ><br>Business<br>Group Header<br>Document<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 31 -->
**Min 1 – Max 1** 

The head.001 Business Application Header _**Business Service**_ element is used to identify administered services on the SWIFT network. The data represented in this elements is referred to as a **Usage Identifier** . For CBPR+ examples are provided below, these values may be used together with the _Message Definition Identifier_ to determine routing rules to specific applications without having to open the business document. 

**Message Definition Identifier BusinessService Business Use Case** pacs.009.001.08 _swift.cbprplus.cov.01_ Financial Institution (Cover) Credit Transfer pacs.009.001.08 _swift.cbprplus.01_ Serial Financial Institution Credit Transfer pacs.008.001.08 _swift.cbprplus.stp.01_ STP Customer Credit Transfer 

The _**Business Service**_ is also intended to be incremented for the same message version, when an updated Usage Guideline is released. For example a new restriction is applied to the pacs.009.001.08 Usage Guideline, the **Business Service** swift.cbprplus.cov.02 and swift.cbprplus.02 will be used to reflect these new Guidelines and allow network validate. 

**Note** : when a new message (Message Definition Identifier) version is introduced the numeric value for the

---

<!-- ELEMENT 32 -->
|**Message Definition Identifier**|**Business Service**|
|---|---|
|pain.001.001.09|sw ift.cbprplus.02|
|pain.002.001.10|sw ift.cbprplus.02|
|pain.008.001.03|sw ift.cbprplus.01|
|pacs.002.001.10|sw ift.cbprplus.02|
|pacs.003.001.08|sw ift.cbprplus.01|
|pacs.004.001.09|sw ift.cbprplus.02|
|pacs.008.001.08|sw ift.cbprplus.02|
|pacs.008.001.08 (STP/STP EU)|sw ift.cbprplus.stp.02|
|pacs.009.001.08 (advice)|sw ift.cbprplus.adv.02|
|pacs.009.001.08 (core)|sw ift.cbprplus.02|
|pacs.009.001.08 (cov)|sw ift.cbprplus.cov.02|
|pacs.010.001.03|sw ift.cbprplus.02|
|pacs.010.001.03 (Margin Collection)|sw ift.cbprplus.col.01|
|camt.029.001.09|sw ift.cbprplus.02|
|camt.052.001.08|sw ift.cbprplus.02|
|camt.053.001.08|sw ift.cbprplus.02|
|camt.054.001.08|sw ift.cbprplus.02|
|camt.055.001.08|sw ift.cbprplus.01|



|**Message Definition Identifier**|**Business Service**|
|---|---|
|camt.058.001.08|sw ift.cbprplus.01|
|camt.060.001.05|sw ift.cbprplus.02|
|camt.107.001.01|sw ift.cbprplus.01|
|camt.108.001.01|sw ift.cbprplus.01|
|camt.109.001.01|sw ift.cbprplus.01|



The data represented in the Business Service, together with the Message Definition Identifier has a number of roles, in addition to the routing rules referred to on the previous page. 

This data value: 

- Identifiers explicitly the Usage Guideline within a library of guideline. For example an application may have various pacs.008 libraries within a collection, for which only one of these is appropriate to be used to identify data requirements or perform validation. 

- is also populated in the Request Header of the InterAct message in the **Request Sub Type** element which allow the service

---

<!-- ELEMENT 33 -->
## **Min 0 – Max 1** 

The head.001 Business Application Header _**Market Practice**_ element is used to identify administered services on the SWIFT network. This element is currently not foreseen to be used by CBPR+.

---

<!-- ELEMENT 34 -->
**Min 1 – Max 1** 

The head.001 Business Application Header _**Creation Date**_ captures the date and time which the Business Application Header was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 35 -->
**Min 0 – Max 1** 

The head.001 Business Application Header _**Copy Duplicate**_ indicator is used as a choice to identify scenarios where a message was previously sent. 

**==> picture [68 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
COPY<br>**----- End of picture text -----**<br>


_**COPY**_ is used to represent a copy of a message being sent to an additional party. This scenario is only associated with camt reporting messages. 

_**DUPL**_ is used to represent a duplicate of a previously sent camt reporting message. To receive a duplicate payment message, Interact message retrieval should be utilised. **DUPL** _**CODU**_ is used to represent a duplicate of a previously sent _**COPY**_ message. This scenario is only associated with camt reporting messages. **CODU**

---

<!-- ELEMENT 36 -->
**Min 0 – Max 1** 

The head.001 Business Application Header _**Possible Duplicate**_ element is used as a flag to indicate that if the party who will ultimately process the Business Document (e.g. pacs.008) received the original, then it should perform necessary actions to avoid processing this Business Message again. 

**==> picture [60 x 95] intentionally omitted <==**

This element is represented by a Yes/No Boolean, whereby **true** represent this is a Possible Duplicate. 

It is not necessary to represent **false** (No) the absence of this optional element itself indicates that this is not considered a Possible Duplicate. 

**==> picture [55 x 51] intentionally omitted <==**

The FINplus Technical Header has an element **PDIndicator** (Possible Duplicate Indicator) which uses a Yes/No Boolean. This may be populated by the network interface to identify a message it considers may be a possible duplicate.

---

<!-- ELEMENT 37 -->
**Min 0 – Max 1** 

The head.001 Business Application Header _**Priority**_ element allows a choice of Business Message Priority Code to indicate the priority which may be applied to the business message. 

**==> picture [104 x 108] intentionally omitted <==**

This element must represent the priority code of the business document (instance) which is only applicable for pacs messages. The pacs message priority is captured in the Payment Type Priority/Instruction Priority.

---

<!-- ELEMENT 38 -->
**Min 0 – Max 1** 

The head.001 Business Application Header _**Related**_ nested element enables the capture of the Business Application Header from a related Business Document. For example, in a pacs.004 Payment Return the _**Related**_ Business Application Header from the original message can be included. This could allow the receiver to apply specific routing to the message, based on the related information i.e., return of a pacs.009 cov may be routed to different payment engine than a core pacs.009. 

**==> picture [51 x 60] intentionally omitted <==**

**==> picture [73 x 57] intentionally omitted <==**

The following elements are nested within the Related element. Where used these contain the original data from the related Business Application Header: 

_**From**_ **Min 1 – Max 1** _**To**_ **Min 1 – Max 1** 

_**Business Message Identifier**_ **Min 1 – Max 1** _**Message Definition Identifier**_ **Min 1 – Max 1** _**Business Service**_ **Min 0 – Max 1** _**Creation Date**_ **Min 1 – Max 1 Min 0 – Max 1** _**Copy Duplicate**_ **Min 0 – Max 1** _**Priority**_

---

<!-- ELEMENT 39 -->
**pain.001 - Interbank Customer Credit Transfer initiation pain.002 – Interbank Customer Payment Status Report pain.008 – Customer Direct Debit Initiation**

---

<!-- ELEMENT 40 -->
# **Interbank Customer Credit Transfer Initiation** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 41 -->
**==> picture [41 x 52] intentionally omitted <==**

**==> picture [59 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
ISO<br>**----- End of picture text -----**<br>


ISO 20022 message element 

## _**Group Header**_ 

   - ➢ _**Message Identification**_ 

   - ➢ _**Initiating Party**_ – where different from _**Debtor**_ 

   - ➢ _**Forwarding Agent**_ 

- _**Payment Information**_ 

   - ➢ _**Payment Information Identification**_ 

   - ➢ _**Requested Execution Date**_ 

   - ➢ _**Debtor**_ 

   - ➢ _**Debtor Agent**_ 

## _**Credit Transfer Transaction Information**_ 

- ➢ _**Payment Identification**_ 

- ➢ _**Amount**_ 

- ➢ _**Charge Bearer**_ 

- ➢ _**Creditor Agent**_ 

- ➢ _**Creditor**_ 

**==> picture [60 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
MT<br>**----- End of picture text -----**<br>


## MT Field Name & (Tag option) 

- **Sequence A –** General Information **:** ➢ **Sender’s Reference** (Field 20) 

- ➢ **Instructing Party** (Field 50 C or L) 

- Message **Sender** in a ‘relay’ scenario **Sequence A –** General Information **:** 

   - ➢ **Customer Specified Reference** (Field 21R) 

   - ➢ **Requested Execution Date** (Field 30) 

   - ➢ **Ordering Customer** (Field 50 F, G or H)* 

- ➢ **Account Servicing Institution** (Field 52 A or C)* 

- **Sequence B –** Transaction Details **:** 

   - ➢ **Transaction Reference** (Field 21) 

   - ➢ **Currency/Transaction Amount** (Field 32B) 

   - ➢ **Details of Charges** (Field 71A) 

   - ➢ **Account With Institution** (Field 57 A, C or D) 

   - ➢ **Beneficiary** (Field 59 no letter, A or F)

---

<!-- ELEMENT 42 -->
**==> picture [140 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
pain.001<br>**----- End of picture text -----**<br>


**==> picture [105 x 65] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [105 x 66] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Information<br>**----- End of picture text -----**<br>


**==> picture [104 x 63] intentionally omitted <==**

**----- Start of picture text -----**<br>
Credit Transfer<br>Transaction<br>Information<br>**----- End of picture text -----**<br>


The pain.001 message is composed of three blocks: 

- _**Group Header**_ contains a set of characteristics that relates to all individual transaction. 

   - _**Payment Information**_ contains a set of characteristics that relates to the debit side of the transaction, such as Debtor and Debtor Agent. 

- 

- _**Credit Transfer Transaction Information**_ contains, among others, elements related to the credit side of the transaction, such as Creditor and Creditor Agent. 

**==> picture [60 x 60] intentionally omitted <==**

Payment messages in a many-to-many payment are considered as a single transaction.

---

<!-- ELEMENT 43 -->
**==> picture [732 x 237] intentionally omitted <==**

**----- Start of picture text -----**<br>
F B<br>A<br>Debtor Initiating Party* Forwarding Debtor Agent Creditor Agent Creditor<br>Agent<br>pain.001**<br>FINplus pain.001<br>pain.002<br>FINplus pain.002 pacs.008<br>pacs.002<br>camt.053<br>*Initiating Party may alternative represent an authorised party such as a head office<br>**or other proprietary method for instructing a payment initiation request.<br>**----- End of picture text -----**<br>


FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases: _**Relay**_ : The pain.001 message is sent by the Initiating party (the Debtor or authorised party) to the Forwarding Agent which acts as a **1** concentrating financial institution. It will forward the pain.001 message to the Debtor Agent

---

<!-- ELEMENT 44 -->
**==> picture [734 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
I A B<br>Debtor Initiating Debtor Agent Creditor Agent Creditor<br>Party<br>FINplus pain.001<br>FINplus pain.002 pacs.008<br>pacs.002<br>camt.053<br>**----- End of picture text -----**<br>


**==> picture [35 x 35] intentionally omitted <==**

This use case may not apply to all Financial Institution, depending on the products and service provided by that Financial Institution to their customer 

FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases: **2** _**Authorised Party Initiation:**_ The pain.001 message is sent by the Financial Institution as an Initiating Party to the Debtor Agent to initiate a payment on behalf of the Debtor who is the account holder. For example, a FI Initiates; a liquidity sweep on behalf of a

---

<!-- ELEMENT 45 -->
**==> picture [734 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
I A B C<br>Debtor Initiating Party Debtor Agent Creditor Agent Creditor<br>Interbank pain.001<br>Interbank pain.002 pacs.008<br>pacs.002 pacs.008<br>camt.053<br>pacs.002<br>**----- End of picture text -----**<br>


Interbank Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases: 

**3** _**Financial Institution Payment Initiation**_ (to non-FI) : The pain.001 message is sent by the Financial Institution as both the Debtor and Initiating Party to initiate a payment from their account with the Debtor Agent to move funds to a non-Financial Institution Creditor

---

<!-- ELEMENT 46 -->
The following descriptions are defined in the ISO 20022 Standard for core parties participating in an Interbank Customer Credit Transfer Initiation relationship. 

**==> picture [61 x 61] intentionally omitted <==**

**==> picture [90 x 170] intentionally omitted <==**

**==> picture [60 x 59] intentionally omitted <==**

**Forwarding Agent -** “Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution”. Applicable for pain.001 use case 1 only 

**Initiating Party –** “Party that initiates the payment.” which may be the **Debtor** or a Party acting on behalf of the Debtor e.g., the Agent initiating a liquidity sweep service 

**Creditor Agent -** “Financial institution servicing an account for the creditor.” 

**Debtor Agent -** “Financial institution servicing an account for the debtor.” 

**Debtor -** “Party that owes an amount of money to the (ultimate) creditor.” 

**Creditor -** “Party to which an amount of money is due.” 

**==> picture [91 x 72] intentionally omitted <==**

**==> picture [61 x 61] intentionally omitted <==**

---

<!-- ELEMENT 48 -->
**Min 1 – Max 1** 

**==> picture [74 x 52] intentionally omitted <==**

Each ISO20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For the Payment Initiation (pain) messages the _Message Identification_ has no exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction. 

**==> picture [60 x 60] intentionally omitted <==**

Each transaction’s _Credit Transfer Transaction Information_ contains a variety of nested _Payment Identification_ elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference). 

**==> picture [55 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
CGI<br>**----- End of picture text -----**<br>


For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor or authorized third party) of the pain.001. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 49 -->
## **Min 1 – Max 1** 

The pain.001 message _**Creation Date Time**_ captures the date and time which the message was created. 

It is defined by _**ISO Date Time**_ with mandatory date and time components expressed in the following formats: 

**10** 

1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ 2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 3. Local time format YYYY-MM-DDThh:mm:ss.sss 

**==> picture [60 x 60] intentionally omitted <==**

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2[nd] option). Otherwise use UTC time (1[st] option). Decimal fractions of seconds with 3 digits. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 50 -->
## **Min 0 – Max 2** 

The pain.001 message _**Authorisation**_ allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The _Authorisation_ uses an embedded code set or free text form. It has no exact equivalent in the legacy MT payment message, however, the Authorisation (Field 25) could be considered as a similar comparison. 

|**Code**|**Description**|**Description**|
|---|---|---|
|ILEV|Instruction Level Authorisation|File requires all customer transactions to be authorised or approved.|
|FDET|File Level Authorisation Details|Additional file level approval, with the ability to view both the payment information block<br>and supportingtransaction detail.|
|FSUM|File Level Authorisation Summary|Additional file level approval, with the ability to view only the payment information block.|
|AUTH|Pre Authorised File|File has been pre-authorised or approved within the originating customer environment<br>and no further approval is required.|
|For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for<br>Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.|||



**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 51 -->
**Min 1 – Max 1** The pain.001 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 52 -->
**==> picture [243 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initiating Party<br>Debtor Authorised Party<br>**----- End of picture text -----**<br>


**==> picture [135 x 15] intentionally omitted <==**

**----- Start of picture text -----**<br>
Forwarding Agent / FI<br>**----- End of picture text -----**<br>


**==> picture [62 x 63] intentionally omitted <==**

For the second and the third use case, BIC of the Initiating Party is required. 

## **Min 1 – Max 1** 

The _**Initiating Party**_ can either be the _**Debtor**_ or an Authorised Party who initiates payment transactions on behalf of the _Debtor_ . The Initiating Party can be, for example, the Head Office which has the authority to debit the account of its subsidiary. In the centralization model, the _Initiating Party_ can also be a payment factory or shared service center or third-party agent, which has authority to send the message on behalf of the _Debtor_ . 

There are three common use cases in the context of interbank pain.001 message: **1. Relay** : The _Initiating Party_ , which is either the _Debtor_ themselves or authorised party, sends the pain.001 message to the _**Forwarding Agent**_ which acts as a concentrating financial institution. It will forward the pain.001 message to the _**Debtor Agent**_ . This is commonly known as a relay scenario. Whereby the Forwarding Agent is performing a technical role in the payment transaction, they would not be represented in the payment, clearing and settlement message. **2. Authorised Party** : The _Initiating Party_ is the _**Financial Institution**_ which has the authority to send the pain.001 message on behalf of the _Debtor_ , e.g., multi-bank liquidity sweeps. 

**3. Financial Institution Payment Initiation** : The _Initiating Party_ is the _**Financial**_

---

<!-- ELEMENT 53 -->
The _**Initiating Party**_ can either be the _**Debtor**_ or an authorised party, such as Financial Institution, in the context of interbank pain.001. Sub elements describe the _Initiating Party_ in greater detail. 

Mandatory _**Name**_ where Postal Address is provided. 

_**Name**_ 

**==> picture [228 x 295] intentionally omitted <==**

**==> picture [92 x 91] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>**----- End of picture text -----**<br>


**==> picture [169 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initiating<br>Party<br>**----- End of picture text -----**<br>


Nested element capturing _**structured**_ Postal Address including at least Town Name and Country if used. 

Nested element capturing the various types of identifiers, e.g., BIC, LEI etc. _**BIC**_ is mandatory for an Authorised Party initiation and FI payment initiation. 

_**Identification**_ 

**==> picture [91 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
Contact<br>Details<br>**----- End of picture text -----**<br>


Optional element to capture the Initiating Party’s ISO country code 

_**Country of Residence**_

---

<!-- ELEMENT 54 -->
**==> picture [44 x 49] intentionally omitted <==**

**Min 0 – Max 1** The _**Forwarding Agent**_ is mandatory in a relay scenario whereby the _Initiating Party_ (the _Debtor_ or authorised third party) has to provide _**Business Identifier Code**_ (BIC FI) of the _Forwarding Agent_ in the original pain.001 message. The Forwarding Agent acts as a concentrating financial institution and forwards the pain.001 message to the _Debtor Agent_ for execution. 

Other options to identify the _**Forwarding Agent**_ include: 

- Clearing System Member ID 

- LEI (Legal Entity Identifier) 

**==> picture [287 x 162] intentionally omitted <==**

**----- Start of picture text -----**<br>
BICFI<br>Clearing<br>Clearing<br>System<br>Financial  Member Id System Id<br>Institution<br>Identification<br>LEI<br>Various sub-<br>element<br>**----- End of picture text -----**<br>


**==> picture [62 x 52] intentionally omitted <==**

For the use cases of Authorised Party initiation and FI payment initiation, Forwarding 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 56 -->
The CBPR+ pain.001 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognise that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory. 

As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message. Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used. 

**==> picture [522 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
Unstructured Many domestic proprietary<br>payments<br>pain.001<br>Structured Unstructured<br>CBPR+  payments<br>**----- End of picture text -----**<br>


**CGI-MP** payment Initiation/ **CBPR+** payment initiation interbank Structured Unstructured

---

<!-- ELEMENT 57 -->
**Min 1 – Max 1** 

## The Interbank Customer Credit Transfer Initiation _**Payment Information Identification**_ provides a . mandatory element to identify the payment initiation 

**==> picture [89 x 58] intentionally omitted <==**

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions. 

**==> picture [63 x 62] intentionally omitted <==**

For single transactions in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 58 -->
**Min 1 – Max 1** The pain.001 message _**Payment Method**_ specifies the means of payment that will be used to move the amount of money. One of the following payment method codes must be used: 

**==> picture [63 x 65] intentionally omitted <==**

**Code Name Definition** CHK Cheque Written order to a bank to pay a certain amount of money from one person to another person. TRF Credit Transfer Transfer of an amount of money in the books of the account servicer. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 59 -->
**Min 0 – Max 1** 

The pain message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. 

_**Instruction Priority**_ **Min 0 – Max 1** 

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the 

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored. 

_**Service Level**_ **Min 0 – Max 3** 

_Payment Type Information_ 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the – type of local instrument. For example, INST Instant Credit Transfer for SEPA Service Level. 

_**Local Instrument**_ **Min 0 – Max 1** 

**==> picture [36 x 35] intentionally omitted <==**

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

i 

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends. 

_**Category**_ 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 60 -->
- **Min 1 – Max 1** 

- The pain.001 message mandatory _**Requested Execution Date**_ element, captures the date and time at which the initiating party requests the clearing agent to process the payment. 

**10** 

It is the date on which the debtor’s account is debited. If payment by cheque, the date when the cheque must be generated by the bank. It is defined by either _**ISO Date**_ expressed in the _YYYY-MM-DD format_ or _**ISO Date Time**_ below: 

1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ 2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 3. Local time format YYYY-MM-DDThh:mm:ss.sss 

**==> picture [60 x 60] intentionally omitted <==**

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2[nd] option). Otherwise use UTC time (1[st] option). Decimal fractions of seconds with 3 digits. Milliseconds are optional. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 61 -->
## **Min 0 – Max 1** 

The pain.001 message optional _**Pooling Adjustment Date**_ element, is used for the correction of the value date of a cash pool movement that has been posted with a different value date. 

**10** 

It is defined by _**ISO Date**_ expressed in the _YYYY-MM-DD format_ 

**==> picture [60 x 60] intentionally omitted <==**

This element is not widely used in the payment industry. For the use case of interbank, it is even less likely to be utilized. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 62 -->
Mandatory _**Name**_ (where a BIC identifier is not provided) by which the party is known 

The ISO 20022 pain messages describes the party whose account is debited for a transaction as the _**Debtor**_ . **Min 1 – Max 1** The _Debtor_ sub elements describe the _Debtor_ in greater detail. 

_**Name**_ 

**==> picture [195 x 295] intentionally omitted <==**

**==> picture [169 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
Debtor<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Debtor_ address details. 

_**Postal Address**_ 

Note: Structured address is strongly recommended with mandatory Town Name and Country 

**==> picture [35 x 34] intentionally omitted <==**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

_**Identification**_ 

Optional element to _**Country of**_ capture the _Debtor_ ’s ISO _**Residence**_

---

<!-- ELEMENT 63 -->
**Min 1 – Max 1** The pain.001 _**Debtor Account**_ is used to capture the account information for which debit entry will be made as a result of the transaction, which will be also reflected in their account Statement. 

The _**Debtor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account, recommended. **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 64 -->
**Min 1 – Max 1** The _**Debtor Agent**_ is a static role in the pain.001 Customer Credit Transfer Initiation. This agent maintains a relationship with their customers, the _Debtor_ . 

**==> picture [80 x 137] intentionally omitted <==**

**==> picture [62 x 63] intentionally omitted <==**

Note: Although the _**Debtor Agent, Creditor Agent, Debtor and Creditor**_ all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section. 

**==> picture [53 x 39] intentionally omitted <==**

For Agent Identification, BIC is preferred, alternatively Clearing Member

---

<!-- ELEMENT 65 -->
## **Min 0 – Max 1** 

The pain.001 _**Debtor Agent Account**_ is used to capture the account information related to the Debtor Agent. 

The _**Debtor Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Account Servicing Institution **Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [62 x 51] intentionally omitted <==**

Debtor Agent and Creditor Agent are Financial Institutions, therefore the nested elements _**Name**_ and _**Proxy**_ are unlikely to be used.

---

<!-- ELEMENT 66 -->
## **Min 0 – Max 1** 

The _**Instruction for Debtor Agent**_ element within the pain.001 message optionally provides information related to the processing of the payment. 

**==> picture [88 x 87] intentionally omitted <==**

The _**Instruction for Debtor Agent**_ element offers a maximum of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the _Debtor Agent_ , depending on bilateral agreement.

---

<!-- ELEMENT 67 -->
Ultimate Party Ultimate Ultimate Debtor Creditor 

**Min 0 – Max 1** 

**Min 0 – Max 1** 

The pain.001 message introduces _**Ultimate Debtor**_ and _**Ultimate Creditor**_ . The _**Ultimate Debtor**_ element should not be confused with an _**Initiating Party**_ who may send a payment initiation request on behalf of the _**Debtor** ,_ for example, Payment Factory. 

CBPR+ premise is that an _**Ultimate Debtor**_ has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an _**Ultimate Creditor**_ has no financial regulated account relationship with the corresponding Creditor. 

The _**Ultimate Debtor**_ and _**Ultimate Creditor**_ can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence. 

**==> picture [63 x 63] intentionally omitted <==**

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 68 -->
**Min 0 – Max 1** The _**Bearer**_ element exists at the Information level and Transaction level. It uses an _**Charge**_ Payment embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A ‘Details of Charges’ 

**Charge Code Description Bearer** CRED Creditor **(0.1)** DEBT Debtor **71A: Details Code Description** SHAR Shared **of Charges** BEN Beneficiar y OUR Our Customer Charges SHA Shared Charges 

**==> picture [54 x 52] intentionally omitted <==**

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 69 -->
**Min 0 – Max 1** The pain.001 optional _**Charges Account**_ element, which is used to process charges associated with a transaction. 

**==> picture [83 x 70] intentionally omitted <==**

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account. 

**==> picture [60 x 60] intentionally omitted <==**

This element is not widely used in the payment industry. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 70 -->
## **Min 0 – Max 1** 

The pain.001 optional _**Charges Account Agent**_ element, which is used to specify the agent that services a charges account. 

**==> picture [83 x 99] intentionally omitted <==**

Charges account agent should only be used when the charges account agent is different from the debtor agent. 

**==> picture [60 x 60] intentionally omitted <==**

This element is not widely used in the payment industry. It should also be noted that the ChargesAccountAgentRule inherited from the base message should be ignored as the optional Branch of DebtorAgent is removed from this Usage Guideline. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 72 -->
**Min 1 – Max 1** 

The pain.001 message contains _**Payment Identification**_ which provides a set of elements to identify the payment of which several are mandatory elements. 

a point-to-point reference of 35 characters long will be returned to account statements if provided by the initiating party. 

_**Instruction Identification**_ **Min 0 – Max 1** _Payment Identification_ _**End to End Identification**_ **Min 1 – Max 1 $** 

**==> picture [33 x 34] intentionally omitted <==**

Note: Instruction Id is mandatory in other CBPR+ messages as it maps directly with the mandatory Sender’s Reference (Field 20) of the legacy MT payment messages. 

an end-to-end reference provided by the _Debtor_ which must be passed unchanged throughout the payment and reported to the Creditor. 

note: if the Debtor has not provide an end-to-end identifier, the _Debtor Agent_ may populate “NOTPROVIDED” to comply the mandatory need of this element. 

**==> picture [33 x 35] intentionally omitted <==**

the Unique End-to-end Transaction Reference created using the UUID v4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting messages. _Credit Transfer Transaction Information_ 

**==> picture [54 x 26] intentionally omitted <==**

**----- Start of picture text -----**<br>
UETR<br>**----- End of picture text -----**<br>


**==> picture [60 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 73 -->
**Min 0 – Max 1** 

The pain.001 _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. 

_**Instruction Priority**_ **Min 0 – Max 1** 

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the 

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored. 

_**Service Level**_ **Min 0 – Max 3** 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the – type of local instrument. For example, INST Instant Credit Transfer for SEPA Service Level. 

_Payment Type Information_ 

_**Local Instrument**_ **Min 0 – Max 1** 

**==> picture [35 x 35] intentionally omitted <==**

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

i 

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends. 

_**Category**_ 

_Credit Transfer Transaction Information_ 

**==> picture [11 x 11] intentionally omitted <==**

---

<!-- ELEMENT 74 -->
**£** 

**$** 

¥ 

**Min 1 – Max 1** The pain.001 nested _**Amount**_ element has a choice of either _**Instructed Amount**_ or _**Equivalent Amount**_ to capture the amount and currency of the Customer Credit Transfer Initiation. 

**==> picture [44 x 44] intentionally omitted <==**

_**Instructed Amount**_ 

_**Equivalent Amount**_ 

The _**Instructed Amount**_ captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the as ordered the This amount has to be currency by initiating party. transported unchanged through the transaction chain. This element is comparable with the legacy Field 33B. 

The _**Equivalent Amount** nested_ element captures currency and _**Amount**_ of money to be moved between the Debtor and Creditor, before deduction of charges, and is expressed in the currency of the Debtor's account. The _**Currency Of Transfer**_ element capture the equivalent currency to be transferred which the first agent will convert the credit transfer into. 

**==> picture [10 x 5] intentionally omitted <==**

**==> picture [19 x 6] intentionally omitted <==**

---

<!-- ELEMENT 75 -->
## **Min 0 – Max 1** The pain.001 _**Exchange Rate Information**_ element provides details on the currency exchange rate and contract. 

Currency in which the rate of exchange is expressed in a currency exchange. For example, 1GBP = xxxCUR, the unit currency is GBP. 

_**Unit Currency** Exchange_ _**Exchange Rate** Rate Information_ 

The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency. 

Specifies the type used to complete the currency exchange, such as SPOT, SALE or AGRD (Agreed). 

_**Rate Type**_ 

**==> picture [87 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
Contract<br>**----- End of picture text -----**<br>


Unique and unambiguous reference to the foreign 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 76 -->
**Min 0 – Max 1** 

The _**Bearer**_ element exists at the Information level and Transaction level. It uses an _**Charge**_ Payment embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A ‘Details of Charges’ 

**==> picture [64 x 52] intentionally omitted <==**

**Charge Code Description Bearer** CRED Creditor **(0.1)** DEBT Debtor SHAR Shared 

**71A: Details Code Description of Charges** BEN Beneficiar y OUR Our Customer Charges SHA Shared Charges 

**==> picture [54 x 52] intentionally omitted <==**

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 77 -->
**Min 0 – Max 1** 

The _**Cheque Instruction**_ information block contains a set of elements needed to issue a cheque. The following types of cheques are commonly used in the market: 

**==> picture [96 x 60] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>**----- End of picture text -----**<br>


**==> picture [63 x 63] intentionally omitted <==**

|**Cheque**<br>**Type**|**Code**|**Description**|
|---|---|---|
|Bank<br>Cheque|BCHQ|Cheque drawn on the account of the debtor's financial institution, which is debited<br>on the debtor's account when the cheque is issued. These cheques are printed by<br>the debtor's financial institution and payment is guaranteed by the financial<br>institution. Synonym is 'cashier's cheque'.|
|Customer<br>Cheque|CCHQ|Cheque drawn on the account of the debtor and debited on the debtor's account<br>when the cheque is cashed. Synonym is 'corporate cheque'.|
|Draft|DRFT|A guaranteed bank cheque with a future value date (do not pay before], which in<br>commercial terms is a 'negotiatable instrument': the beneficiary can receive early<br>payment from any bank under subtraction of a discount. The ordering customer's<br>account is debited on value date.|
|The**_Delivery Method_**element specifies the method to be used in delivering the cheque by the_Debtor Agent_.<br>For example, a code CRCD is used to courier the cheque to the_Creditor_.|||



**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 78 -->
Ultimate Party Ultimate Ultimate Debtor Creditor 

**Min 0 – Max 1** 

**Min 0 – Max 1** 

The pain.001 message introduces _**Ultimate Debtor**_ and _**Ultimate Creditor**_ . The _**Ultimate Debtor**_ element should not be confused with an _**Initiating Party**_ who may send a payment initiation request on behalf of the _**Debtor** ,_ for example, Payment Factory. 

CBPR+ premise is that an _**Ultimate Debtor**_ has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an _**Ultimate Creditor**_ has no financial regulated account relationship with the corresponding Creditor. 

The _**Ultimate Debtor**_ and _**Ultimate Creditor**_ can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence. 

**==> picture [63 x 63] intentionally omitted <==**

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined. 

_Credit Transfer Transaction Information_ 

**==> picture [11 x 11] intentionally omitted <==**

---

<!-- ELEMENT 79 -->
## **Min 0 – Max 1** 

The pain.001 has three optional _**Intermediary Agent (1,2**_ and _**3)**_ elements. These agents represent the agent(s) that exist between the _Debtor Agent_ and the _Creditor Agent_ . 

**==> picture [46 x 19] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>**----- End of picture text -----**<br>


- If more than one intermediary agent is present, then _**Intermediary Agent 1**_ identifies the agent between the _Debtor Agent_ and the _**Intermediary Agent 2**_ . 

- If more than two intermediary agents are present, then _**Intermediary Agent 2**_ identifies the agent between the _**Intermediary Agent 1**_ and the _**Intermediary Agent 3**_ . 

**==> picture [44 x 20] intentionally omitted <==**

**----- Start of picture text -----**<br>
2<br>**----- End of picture text -----**<br>


- If _**Intermediary Agent 3**_ is present, then it identifies the agent between the _**Intermediary Agent 2**_ and the _Creditor Agent_ . 

- More commonly the ISO 9362 Financial Institution _**Business Identifier Code**_ is considered the best practice de factor standard for ‘many to many’ / correspondent banking payments. 

- Other options to identify the _**Intermediary Agent**_ include: 

**==> picture [46 x 20] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>**----- End of picture text -----**<br>


- Clearing System Member ID 

- LEI (Legal Entity Identifier) 

- Name and either structured, or unstructured Postal Address 

_Credit Transfer Transaction Information_ 

**==> picture [11 x 10] intentionally omitted <==**

**==> picture [12 x 11] intentionally omitted <==**

**==> picture [12 x 6] intentionally omitted <==**

Intermediary Agent 1

---

<!-- ELEMENT 80 -->
**Min 0 – Max 1** The pain.001 _**Intermediary Agent (1,2**_ and _**3) Accounts**_ are used to capture the account information related to these Agents. 

The _**Intermediary Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**==> picture [42 x 22] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Account Servicing Institution. **Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account. **Min 0 – Max 1** _**Currency**_ identifies the currency of the account. **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution. **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

_Credit Transfer Transaction Information_ 

**==> picture [12 x 11] intentionally omitted <==**

**==> picture [12 x 6] intentionally omitted <==**

**==> picture [11 x 10] intentionally omitted <==**

Intermediary Agent Account 1

---

<!-- ELEMENT 81 -->
**Min 0 – Max 1** The _**Creditor Agent**_ is a static roles in the pain.001 Customer Credit Transfer Initiation. This agent maintain a relationship with their customers, the _Creditor_ . 

**==> picture [84 x 137] intentionally omitted <==**

**==> picture [62 x 63] intentionally omitted <==**

Note: Although the _**Debtor Agent, Creditor Agent, Debtor and Creditor**_ all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section. 

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 82 -->
## **Min 0 – Max 1** 

. The pain.001 _**Creditor Agent Account**_ is used to capture the account information related to the _Creditor Agent_ 

The _**Creditor Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Account Servicing Institution **Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 83 -->
## **Min 1 – Max 1** 

Mandatory _**Name**_ (where a BIC identifier is not provided) by which the party is known 

_**Creditor**_ as The ISO 20022 pain messages describe the the party whose account was credited for a transaction. The _Creditor_ sub elements describe the _Creditor_ in greater detail. 

_**Name**_ 

**==> picture [200 x 296] intentionally omitted <==**

**==> picture [169 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
Creditor<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Creditor_ address details. 

_**Postal Address**_ 

Note: Structured address is strongly recommended with mandatory Town Name and Country 

**==> picture [35 x 34] intentionally omitted <==**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

_**Identification**_ 

Optional element to _**Country of**_ capture the _Creditor_ ’s ISO _**Residence**_

---

<!-- ELEMENT 84 -->
## **Min 0 – Max 1** 

The pain.001 _**Creditor Account**_ is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement. 

The _**Creditor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [62 x 45] intentionally omitted <==**

Creditor Account is not required for cheque payments. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 85 -->
**Min 0 – Max 1** 

**Min 0 – Max 1** 

Ultimate Party Ultimate Ultimate Debtor Creditor 

The pain.001 message introduces _**Ultimate Debtor**_ and _**Ultimate Creditor**_ . The _**Ultimate Debtor**_ element should not be confused with an _**Initiating Party**_ who may send a payment initiation request on behalf of the _**Debtor** ,_ for example, Payment Factory. 

CBPR+ premise is that an _**Ultimate Debtor**_ has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an _**Ultimate Creditor**_ has no financial regulated account relationship with the corresponding Creditor. 

The _**Ultimate Debtor**_ and _**Ultimate Creditor**_ can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 86 -->
## **Min 0 – Max 2** 

The _**Instruction for Creditor Agent**_ element within the pain.001 message optionally provides information related to the processing of the payment for the Creditor Agent. 

The _**Instruction for Creditor Agent**_ element offers a multiplicity of up to 2 occurrences of information. This element enables: 

**==> picture [91 x 85] intentionally omitted <==**

- 

- ➢ the use of an embedded choice of code to describe the instruction (e.g. CHQB Pay Creditor by Cheque) 

- ➢ free format _instruction information_ 

➢ or both, where the free format complements the code. The use of this element may be bilaterally agreed with the _Creditor Agent_ . It must be passed . on throughout the life cycle of the transaction until the payment reaches the _Credit Agent_ 

**==> picture [11 x 12] intentionally omitted <==**

**==> picture [42 x 8] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 87 -->
**==> picture [47 x 42] intentionally omitted <==**

**ISO 20022 Programme Quality data, quality payments** 

**CBPR+ User Handbook** SR 2023 Edition 

March 2023

---

<!-- ELEMENT 88 -->
## **Min 0 – Max 1** 

The _**Instruction for Debtor Agent**_ element within the pain.001 message optionally provides information related to the processing of the payment. 

**==> picture [88 x 87] intentionally omitted <==**

The _**Instruction for Debtor Agent**_ element offers a maximum of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the _Debtor Agent_ , depending on bilateral agreement. 

**==> picture [11 x 12] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 89 -->
## **Min 0 – Max 1** 

The _**Purpose**_ element within the pain.001 message captures the reason for the payment transaction which use an external ISO code or may either Purpose a proprietary code. 

The is used to the nature of the IVPT Invoice FEES of purpose capture payment, e.g., Payment, Payment Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the _Debtor_ . 

**==> picture [123 x 91] intentionally omitted <==**

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. 

For example, LIMA is classified within the Cash Management categorisation, with the _Name_ Liquidity Management described as a Bank initiated account transfer to support zero target balance management, pooling or sweeping. 

**==> picture [63 x 63] intentionally omitted <==**

_Category Purpose_ also captures a high-level purpose, which unlike _Purpose_ is less granular but can trigger special processing e.g., Category Purpose code SALA ‘Salary Payment’ may trigger a reporting process which restricts sensitive data i.e., individual salary names. 

_Credit Transfer Transaction Information_ 

**==> picture [11 x 12] intentionally omitted <==**

---

<!-- ELEMENT 90 -->
## **Min 0 – Max 10** 

The _**Regulatory Reporting**_ block within the pain.001 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s. 

**Min 0 – Max 1** 

The _**Debit Credit Reporting Indicator**_ utilises an embedded choice of code to indicate whether the regulatory reporting applies to the: 

**==> picture [109 x 67] intentionally omitted <==**

- DEBT (debit) 

- • CRED (credit) 

- • BOTH 

**Min 0 – Max 1** The _**Authority**_ element captures the _**Name**_ and _**Country**_ code of the Authority/Entity requiring the regulatory reporting information. 

**Min 0 – Max *** The _**Details**_ element provides the detail on the regulatory reporting information. 

**==> picture [10 x 4] intentionally omitted <==**

_Credit Transfer Transaction Information       Regulatory Reporting_ Debit Credit Reporting Indicator

---

<!-- ELEMENT 91 -->
**Min 0 – Max 1** 

The pain.001 nested _**Tax**_ element captures information related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s). 

This element caters for two main types of tax related payments: 

**==> picture [67 x 27] intentionally omitted <==**

**==> picture [69 x 37] intentionally omitted <==**

**==> picture [62 x 50] intentionally omitted <==**

- Tax payment obligation that is required to be transmitted with a payment 

- • Information that accompanies an actual payment of a tax obligation 

- The follow nested elements may be used to capture detailed tax information: 

**==> picture [542 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1<br>Total<br>Creditor Debtor Administration Reference Method Taxable<br>Zone Number Base Amount<br>Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max *<br>Total Tax  Date Sequence<br>Record<br>Amount Number<br>**----- End of picture text -----**<br>


Tax information block is also available within the Structured Remittance Information block which is applicable 

**==> picture [10 x 5] intentionally omitted <==**

---

<!-- ELEMENT 92 -->
## **Min 0 – Max 10** 

The _**Related Remittance Information**_ element within the pain.001 message is nested to provide information related to the handling of remittance information. 

## **Min 0 – Max 1** 

The _**Remittance Identification**_ captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction. 

## **Min 0 – Max *** 

**==> picture [89 x 83] intentionally omitted <==**

The _**Remittance Location Details**_ uses a set of nested elements to provide information on either the location of or the delivery of remittance information. 

- _**Method**_ requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email) 

- _**Electronic Address**_ provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved. 

- _**Postal Address**_ provides the postal address to which an agent is to send the remittance information 

**==> picture [84 x 112] intentionally omitted <==**

- Unlike CBPR+ pacs messages, in the interbank pain.001 message, Related Remittance Information and Remittance Information are non-mutually exclusive due to a corporate use case of populating both information . 

- blocks for detailing remittance advices which are part of value-added service offered by the _Debtor Agent_ 

   - SCORE Guideline: If the Related Remittance Information is used, and a Remittance Identification is provided, it is recommended that the Remittance Identification equal the End To End Identification. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 93 -->
**Min 0 – Max 1** 

The optional _**Remittance Information**_ element within the pain.001 message is nested to provide either _**Structured**_ or _**Unstructured**_ information related to payment, such as invoices. 

_**Remittance Information**_ enables the matching/reconciliation of an entry that the payment is intended to settle. 

**==> picture [56 x 65] intentionally omitted <==**

**Min 0 – Max 1** The **Unstructured** sub element captures free format _Remittance Information_ which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence. **Min 0 – Max *** The **Structured** element is nested capturing rich structured _Remittance Information,_ and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification) The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-toend transportation of this data. 

**==> picture [63 x 36] intentionally omitted <==**

**==> picture [390 x 29] intentionally omitted <==**

**----- Start of picture text -----**<br>
Recommend to refer to CGI-MP Document Centre for Country<br>i t R itt I f ti<br>**----- End of picture text -----**<br>


_Credit Transfer Transaction Information_ Remittance Information 

**==> picture [10 x 5] intentionally omitted <==**

**==> picture [11 x 12] intentionally omitted <==**

---

<!-- ELEMENT 94 -->
The bilaterally/multilaterally agreed _**Remittance Information**_ which is _**Structured**_ must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information. 

**==> picture [457 x 131] intentionally omitted <==**

## example of _Structured_ invoice information 

The _**Creditor Remittance Information**_ is provided to the _**Creditor**_ in the Cash Management Reporting messages’ Remittance Information component, for example, the camt.053 Bank to Customer Statement. 

**Structured** <Strd> xml tag In this example Referred Document **Reference Document** <Rf rdDocInf> Information and its nested elements have **Information** multiplicity which support up to 9,000 **Type** <Tp> business character of information. Whereby this element names **Code Or Proprietary** <CdOrPrtry > information element can be repeated to include more **Code** <Cd> **CINV** coded information such as another invoice. **Number** <Nb> **A0000101 Related Date** <Dt> **2019-10-29** 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [11 x 9] intentionally omitted <==**

_Credit Transfer Transaction Information_ 

Remittance Information

---

<!-- ELEMENT 95 -->
The _**Creditor Reference**_ in the _Creditor Remittance Information_ component in the structured remittance information is generated by _Creditor_ to inform the _Debtor_ who has to include the reference in the Remittance Information component of the pain.001. 

Creditor Reference in the Structured Remittance Information is based on ISO 11649 

- 2 letters “RF” 

- 2 digits check digit 

- 21 letters/digits  creditor reference 

Facilitates STP and auto-match with the creditor reference and its account receivable 

- A vendor can add the creditor reference to its invoice. When a customer pays the invoice,  they write the creditor reference instead of the invoice number in the payment message (e.g., MT 101 F70 which will be carried in MT 103) 

- When the vendor receives the payment, it can auto-match the incoming credit entry and the creditor reference extracted from the statement (e.g., MT 940 F61/86) 

**==> picture [52 x 49] intentionally omitted <==**

SCORE Guideline: For Creditor Reference information, in instances where the Creditor Reference Type code is SCOR (Structured Communication Reference) and the Creditor Reference is structured in accordance with ISO 11649, the 

_Credit Transfer Transaction Information_ 

**==> picture [11 x 9] intentionally omitted <==**

Remittance Information 

**==> picture [10 x 11] intentionally omitted <==**

---

<!-- ELEMENT 96 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g., a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

## **Interbank Customer Credit Transfer Initiation - Relay** 

Use Case pn.1.1.1 – High Level Payment Initiation Interbank ‘relay’ (pain.001) Use Case pn.1.1.1.a – High Level Payment Initiation Interbank ‘relay’ (pain.001) Multi-bank Sweep Use Case pn.1.1.2 – High Level Payment Initiation Interbank ‘relay’ (pain.001) involving a Payment Market Infrastructure 

## **Interbank Customer Credit Transfer Initiation – Authorised Party** 

Use Case pn.1.2.1 – High Level Payment Initiation Interbank (pain.001) by an Authorised Party Use Case pn.1.2.1.a. – High Level Payment Initiation Interbank (pain.001) FI-Initiated Sweep (Long position at the Secondary Account) Use Case pn.1.2.1.b. – High Level Payment Initiation Interbank (pain.001) by an Authorised Party to pay themselves as the Creditor 

## **Interbank Customer Credit Transfer Initiation – Financial Institution** 

Use Case pn.1.3.1 – High Level Payment Initiation Interbank (pain.001) Financial Institution Payment Initiation

---

<!-- ELEMENT 97 -->
In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor and initiate a credit transfer. 

**==> picture [758 x 283] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4<br>pain.001 Interbank pain.001<br>pacs.008 camt.053<br>pain.002 F Interbank pain.002 A B<br>3a<br>3b<br>1 3 3b<br>Debtor Agent (A) debits the<br>Initiating Party sends a<br>account of Debtor and  Forwarding Agent (F) relays the<br>payment instruction to the<br>status ACSP (accepted settlement<br>initiates a credit transfer by<br>Forwarding Agent<br>in progress) to the Initiating Party,<br>forwarding a local credit<br>based upon a bilateral agreement<br>transfer message pacs.008<br>2<br>Forwarding Agent (F) forwards<br>the payment instruction to the  4<br>3a<br>Debtor Agent (A)<br>Debtor Agent (A) provides a  Creditor Agent (B) processes the<br>status update ACSP (accepted  payment and sends the statement to<br>settlement in progress) to the Creditor<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 98 -->
In the interbank relay scenario, the Forwarding Agent relaying the pain.001 message to the Debtor Agent(s) in this case to sweep excess cash from the account of the Debtor and consolidate cash for a Corporate. 

**==> picture [758 x 283] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4<br>pain.001 Interbank pain.001<br>pacs.008 camt.053<br>pain.002 F Interbank pain.002 A B<br>3a<br>3b<br>1 3 3b<br>Debtor Agent (A) debits the<br>Initiating Party sends a payment<br>account of Debtor and  Forwarding Agent (F) relays the<br>instruction to the Forwarding<br>status ACSP (accepted settlement<br>initiates a credit transfer by<br>Agent to sweep excess funds<br>in progress) to the Initiating Party,<br>forwarding a local credit<br>from its subsidiary’s account to<br>based upon a bilateral agreement<br>the master account with Bank B transfer message pacs.008<br>4<br>2 3a<br>Debtor Agent (A) provides a  Creditor Agent (B) processes the<br>Forwarding Agent (F) forwards<br>status update ACSP (accepted  payment and notifies Creditor of a<br>the payment instruction to the  settlement in progress) to the successful sweep through the<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 99 -->
## **Market Infrastructure** 

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor initiate a credit transfer through a Payment Market Infrastructure. 

**==> picture [744 x 286] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2<br>3 4<br>pain.001 Interbank pain.001<br>pacs.008 pacs.008<br>pain.002 F Interbank pain.002 A B<br>3a<br>3b<br>1 3 3b<br>Debtor Agent (A) debits the account<br>Initiating Party sends a  Forwarding Agent (F) relays the<br>of Debtor and initiates a credit<br>payment instruction to the  status ACSP (accepted settlement<br>transfer by forwarding a local credit<br>Forwarding Agent in progress) to the Initiating Party,<br>transfer message pacs.008 to a<br>based upon a bilateral agreement<br>Payment Market Infrastructure<br>2<br>(PMI)<br>Forwarding Agent (F) forwards<br>the payment instruction to the<br>3a 4<br>Debtor Agent (A)<br>Debtor Agent (A) provides a status  Creditor Agent (B) receives local<br>update ACSP (accepted settlement  credit transfer message via the<br>in progress) to the Forwarding  Payment Market Infrastructure<br>Agent (F) based upon a bilateral (PMI) and credits the Creditor<br>**----- End of picture text -----**<br>


**==> picture [60 x 61] intentionally omitted <==**

---

<!-- ELEMENT 100 -->
In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor’s account based on Debit Authorisation already in place between the Debtor and the Debtor Agent 

**==> picture [758 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
Debit<br>DA<br>Authorisation 3 4<br>2<br>Interbank pain.001 pacs.008<br>camt.053<br>I Interbank pain.002 A pacs.002 B<br>3a<br>3<br>DA 4<br>As a pre-requisite the Debtor<br>Debtor Agent (A) debits the account of  Creditor Agent (B) receives the credit<br>provides Debit Authorisation to<br>Agent A, which allows Agent I  Debtor and initiates a credit transfer transfer message, credits the Creditor, and<br>sends a camt.053 (statement) at the end of<br>to Initiate Payment from their<br>the business day to the Creditor. An optional<br>account<br>status report is sent to the previous Agent<br>2 3a based upon a bilateral agreement<br>Agent (I) initiates a payment<br>Debtor Agent (A) optionally provides a<br>request (pain.001) to the Debtor<br>status update to the Initiating Party<br>Agent (A) to move fund from the<br>(Agent I), based upon a bilateral<br>Debtor’s account, as an<br>agreement<br>**----- End of picture text -----**<br>

---

