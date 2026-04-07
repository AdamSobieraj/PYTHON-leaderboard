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

<!-- ELEMENT 101 -->
## **position at the Secondary Account)** 

In the interbank sweep scenario, the Initiating Party (Agent I) initiates the pain.001 message to the Debtor Agent to sweep excess cash from the account of the Debtor and consolidate the cash for a Corporate. 

**==> picture [730 x 282] intentionally omitted <==**

**----- Start of picture text -----**<br>
Sweep  camt.052 1 3 4<br>Contract<br>2<br>Interbank pain.001 pacs.008<br>camt.053<br>I Interbank pain.002 A pacs.002 B<br>3a<br>1 3 4<br>Agent I receives intraday  Creditor Agent (B) receives credit transfer<br>Debtor Agent (A) debits the account of<br>balance report from Debtor  Debtor and initiates a credit transfer message, credits the Creditor, and sends<br>Agent (A) on behalf of their  a camt.053 (statement) at the end of the<br>mutual customer. business day to the Creditor. An optional<br>status report is sent to the previous Agent<br>based upon a bilateral agreement<br>2 3a<br>Agent (I) initiates a sweep on  Debtor Agent (A) optionally provides a<br>behalf of the Corporate by  status update to the Initiating Party  See use case p.8.1.2 for a sweeping contract with<br>sending pain.001 to the Debtor  (Agent I), based upon a bilateral<br>a short position<br>Agent agreement<br>**----- End of picture text -----**<br>


See use case p.8.1.2 for a sweeping contract with a short position

---

<!-- ELEMENT 102 -->
## **pay themselves as the Creditor.** 

In the Authorised Party Initiation scenario, the Initiating Party (Agent I) initiates a payment from the Debtor’s account based on Debit Authorisation already in place to move money to themselves as the Creditor 

**==> picture [758 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
Debit<br>DA<br>Authorisation 3 4<br>2<br>Interbank pain.001 pacs.008<br>camt.053<br>I Interbank pain.002 A pacs.002 B I<br>3a<br>DA 3 4<br>As a pre-requisite the Debtor  Debtor Agent (A) debits the account of  Creditor Agent (B) receives the credit transfer<br>provides Debit Authorisation to  Debtor and initiates a credit transfer message, credits the Creditor, and sends a<br>Agent I to Initiate Payment from their  camt.053 (statement) at the end of the<br>account with the Debtor Agent (A) business day to the Creditor. An optional<br>status report is sent to the previous Agent<br>2 3a based upon a bilateral agreement<br>Agent (I) initiates a payment request<br>Debtor Agent (A) optionally provides a<br>(pain.001) to the Debtor Agent (A) to<br>status update to the Initiating Party<br>move fund from the Debtor’s<br>(Agent I), based upon a bilateral<br>account, as an authorised party, to<br>agreement<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 103 -->
## **Payment Initiation** 

## The Initiating Party (Agent I) initiates a payment from their own account with the Debtor Agent to move the funds to a non-Financial Institution Creditor 

**==> picture [650 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
2 3<br>1<br>Interbank pain.001 pacs.008<br>camt.053<br>I Interbank pain.002 A pacs.002 B<br>2a<br>1 2<br>3<br>Agent (I), the Debtor, initiates a  Debtor Agent (A) debits the account of  Creditor Agent (B) receives credit<br>payment request (pain.001) to  Agent (I), the Debtor and initiates a  transfer message, credits the Creditor,<br>the Debtor Agent (A) to move  credit transfer and sends the camt.053 (statement) at<br>funds from their own account the end of the business day to the non-<br>FI Creditor. An optional status report is<br>sent to the previous Agent based upon a<br>2a<br>bilateral agreement<br>Debtor Agent (A) optionally provides a<br>status update to the Initiating Party<br>(Agent I), based upon a bilateral<br>agreement<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 104 -->
# **Interbank Customer Payment Status Report** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 105 -->
**==> picture [177 x 79] intentionally omitted <==**

**----- Start of picture text -----**<br>
pain.002<br>**----- End of picture text -----**<br>


**==> picture [139 x 63] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [139 x 63] intentionally omitted <==**

**----- Start of picture text -----**<br>
Original Group<br>Information And Status<br>**----- End of picture text -----**<br>


Original Payment Information And Status 

## The pain.002 message is composed of four building blocks: 

- _**Group Header**_ which contains a set of characteristics shared by all individual transactions in the message. 

- _**Original Group Information and Status**_ contains the group of transactions, to which the status report message refers to. 

- _**Original Payment Information And Status**_ contains information about the original payment information, to which the status report message refers. 

- _**Transaction Information And Status**_ provides information on the original transactions to which the status report message refers. 

It is used to inform the previous party in the payment chain about the positive or negative status of an instruction. It is also used to report on a pending instruction.

---

<!-- ELEMENT 106 -->
**==> picture [734 x 247] intentionally omitted <==**

**----- Start of picture text -----**<br>
F A B<br>Debtor Initiating Party Forwarding Debtor Agent* Creditor Agent Creditor<br>Agent<br>pain.001<br>Interbank pain.001<br>pain.002**<br>Interbank pain.002 pacs.008<br>pacs.002<br>camt.053<br>*Debtor Agent is the same as the Initiating Party who initiates the payment status report message.<br>**or other proprietary method for informing about the status of an instruction<br>**----- End of picture text -----**<br>


Interbank Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the agents. There are three common use cases: 

_**Relay**_ : The pain.002 message is sent by the Debtor Agent to the Forwarding Agent which acts as a concentrating financial institution. It **1**

---

<!-- ELEMENT 107 -->
**==> picture [734 x 226] intentionally omitted <==**

**----- Start of picture text -----**<br>
F A B<br>Debtor Initiating Party Forwarding Debtor Agent* Creditor Agent Creditor<br>Agent<br>pain.001<br>FINplus pain.001<br>pain.002**<br>FINplus pain.002 pacs.008<br>pacs.002<br>camt.053<br>*Debtor Agent is the same as the Initiating Party who initiates the payment status report message.<br>**or other proprietary method for informing about the status of an instruction<br>**----- End of picture text -----**<br>


FINplus Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the agents. There are three common use cases: 

_**Relay**_ : The pain.002 message is sent by the Debtor Agent to the Forwarding Agent which acts as a concentrating financial institution. It **1** will forward the pain.002 message to the Initiating Party.

---

<!-- ELEMENT 108 -->
**==> picture [734 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>Debtor Initiating Party Debtor Agent Creditor Agent Creditor<br>Interbank pain.001<br>Interbank pain.002 pacs.008<br>pacs.002 pacs.008<br>camt.053<br>pacs.002<br>**----- End of picture text -----**<br>


Interbank Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the agents. There are three common use cases: 

**3** 

_**Financial Institution Payment Initiation**_ (to non-FI) : The pain.002 message is sent by the Debtor Agent to the Debtor (Financial

---

<!-- ELEMENT 109 -->
**==> picture [803 x 237] intentionally omitted <==**

**----- Start of picture text -----**<br>
B A F<br>Debtor Debtor Agent Creditor Agent Forwarding Initiating Party* Creditor<br>Agent<br>pain.008**<br>Interbank pain.008<br>pain.002<br>Interbank pain.002<br>pacs.003<br>pacs.002<br>camt.053<br>*Initiating Party may alternative represent an authorised party such as a head office<br>**----- End of picture text -----**<br>


- *Initiating Party may alternative represent an authorised party such as a head office **or other proprietary method for instructing a direct debit initiation request. 

Interbank Customer Direct Debit Initiation message is sent by the Initiating Party to the Forwarding Agent or the Creditor Agent. It is used to request single or bulk collection(s) of funds from one or various debtor’s account(s) to a creditor. 

_**Relay**_ : Interbank pain.008 message is sent by the Initiating party (the Creditor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.008 message to the Creditor Agent to initiate the direct debit instruction(s)..

---

<!-- ELEMENT 111 -->
## **Min 1 – Max 1** 

**==> picture [74 x 52] intentionally omitted <==**

Each ISO20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Payment Initiation (pain) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction. 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [54 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
CGI<br>**----- End of picture text -----**<br>


Each transaction’s _Credit Transfer Transaction Information_ contains a variety of nested _Payment Identification_ elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference). 

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor Agent) of the pain.002. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 112 -->
## **Min 1 – Max 1** 

- The pain.001 message _**Creation Date Time**_ captures the date and time the message was created. 

It is defined by _**ISO Date Time**_ with mandatory date and time components expressed in the following formats: 

**10** 

1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ 2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

3. Local time format YYYY-MM-DDThh:mm:ss.sss 

**==> picture [60 x 60] intentionally omitted <==**

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2[nd] option). Otherwise use UTC time (1[st] option). Decimal fractions of seconds with 3 digits. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 113 -->
**==> picture [248 x 207] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initiating Party = Debtor Agent<br>Forwarding  Authorised FI Debtor<br>Agent Party<br>**----- End of picture text -----**<br>


## **Min 1 – Max 1** 

The _**Initiating Party**_ in the context of interbank payment initiation report is always the _**Debtor Agent**_ which initiates the pain.002 message. _**Business Identifier Code**_ (BIC FI) is mandated to identify the _Initiating Party_ in the pain.002 message. There are three use cases below: 

**1. Relay** : The _**Debtor Agent**_ sends the pain.002 message to the _**Forwarding Agent**_ which acts as a concentrating financial institution. It will forward the pain.002 message to the original _Initiating Party_ who can be the _Debtor_ themselves or the Authorised Party. This is commonly known as a relay scenario. 

**2. Authorised Party** : The _**Debtor Agent**_ sends the pain.002 to the Financial Institution ( _**Initiating Party**_ ) which has the authority to initiate a payment on behalf of the _Debtor_ , e.g., multi-bank liquidity sweeps 

**3. Financial Institution Payment Initiation** : The _**Debtor Agent**_ sends the pain.002 to the Financial Institution which is the _**Debtor**_ who initiate a payment from their account to move funds to a non-Financial Institution _Creditor_ 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 114 -->
**==> picture [44 x 49] intentionally omitted <==**

**Min 0 – Max 1** The _**Forwarding Agent**_ is mandatory in a relay scenario whereby the receiver of the pain.002 message is not the original Debtor. In this case, the _Initiating Party_ (the _Debtor Agent_ ) has to provide _**Business Identifier Code**_ (BIC FI) of the _Forwarding Agent_ in the pain.002 message. The Forwarding Agent _acts as a concentrating financial institution and forwards the pain.002 message to the Debtor or the Initiating Party._ 

Other options to identify the _**Forwarding Agent**_ include: 

- Clearing System Member ID 

- LEI (Legal Entity Identifier) 

**==> picture [286 x 122] intentionally omitted <==**

**----- Start of picture text -----**<br>
BICFI<br>Financial  Clearing<br>Clearing<br>Institution         System<br>System Id<br>Identification Member Id<br>LEI<br>**----- End of picture text -----**<br>


**==> picture [62 x 52] intentionally omitted <==**

For the use case of multi-bank liquidity sweeps, Forwarding Agent is not required. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 116 -->
**CGI** 

## **Min 1 – Max 1** 

The pain.002 Customer Payment Status Report uses elements in the _**Original Group Information and Status**_ to capture the message identifier and message name of the underlying payment the _Payment Status Report_ relates to. The mandatory _**Original Message Identification**_ contains the point-to-point reference, and the mandatory _**Original Message Name Identification**_ contains the message name of the underlying payment being reported upon. Optionally the _**Original Creation Date Time**_ can also be captured. For example: 

_Original Message Name Identification_ “pain.001.001.09” confirms the Status Report is of a pain.001 Customer Credit Transfer Initiation. 

**==> picture [61 x 62] intentionally omitted <==**

Original Message Identification must transport the Message Identification of the underlying payment (e.g., pain.001). 

For a relay scenario, Forwarding Agent (F) should respect the Message ID provided by the Initiating Party of the pain.001 and pain.002. 

**==> picture [370 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
F A<br>pain.001 Interbank pain.001<br>Message  Message<br>abcd1234 abcd1234<br>Identification Identification<br>pain.002 Interbank pain.002<br>Message  Message<br>xyz9875 xyz9875<br>Identification Identification<br>Original Message  abcd1234 Original Message  abcd1234<br>Identification Identification<br>Original Message Original Message<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 117 -->
## **Identification** 

## **Min 1 – Max 1** 

**==> picture [74 x 52] intentionally omitted <==**

The pain.002 Customer Payment Status Report uses element _**Original Payment Information Identification**_ , located in the Original Group Information and Status. This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group or batch reference if the message contains multiple transactions. 

**==> picture [62 x 64] intentionally omitted <==**

Since the interbank pain.001 and pain.002 usage guidelines are restricted to one single transaction, this value is the same as the Original Message ID of the Original Group Information And Status. 

**==> picture [11 x 10] intentionally omitted <==**

**==> picture [11 x 6] intentionally omitted <==**

**==> picture [11 x 6] intentionally omitted <==**

**==> picture [10 x 11] intentionally omitted <==**

_Original Payment Information and Status_

---

<!-- ELEMENT 118 -->
**Min 1 – Max 1** 

The pain.002 _Customer Payment Status Report_ nested _**Transaction Information And Status**_ element is used to capture information from the underlying payment that the _Payment Status Report_ relates to. 

**==> picture [59 x 62] intentionally omitted <==**

**Mandatory** element (in addition to _Original Message identification_ and _Original Message Name Identification_ described on the previous pages) include: _**Original End to End Identification**_ **Min 1 – Max 1** _**Original UETR**_ **Min 1 – Max 1** The following element is optional: _**Original Instruction Identification**_ **Min 0 – Max 1** 

These Original elements enable the _**Initiating Party**_ to associate the Payment Status with the payment they originally sent. 

**==> picture [11 x 10] intentionally omitted <==**

_Original Payment Information and Status Transaction Information and Status Original End to End Identification Original UETR_

---

<!-- ELEMENT 119 -->
**Min 1 – Max 1** 

## **Information** 

The pain.002 _Customer Payment Status Report_ _**Transaction Status**_ utilizes the externalized ISO _Payment Transaction Status_ code list to provide a status update on a pain message previously received. The _Transaction Status_ element is arguable the most significant/core parts of the pain.002 and optionally may further be complimented with _**Status Reason Information.**_ 

**Min 0 – Max 1** 

**==> picture [69 x 79] intentionally omitted <==**

The nested _**Status Reason Information**_ enable the optional inclusion of: _**Originator**_ – the party that issues the status. Typically, the pain.002 Initiating Party and therefore Originator is not necessary. 

_**Reason**_ – which utilises an ISO external Status Reason code. For example, **AC04** ‘Closed Account Number’ would compliment a RJCT (Reject) Transaction Status. _**Additional Information**_ – a text element to provide further status reason information, necessary where the _Reason_ code is NARR 

**==> picture [50 x 50] intentionally omitted <==**

Note: A _**Reason**_ code must be provided where the _**Transaction Status**_ RJCT (Reject) code is used.

---

<!-- ELEMENT 120 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|ACCC|AcceptedSettlementCompleted|Settlement on the creditor's account has been completed.|Sent by**Creditor Agent**to confirm the settlement on the creditor’s account|
|ACCP|AcceptedCustomerProfile|Preceding check of technical validation was successful. Customer<br>profile check was also successful.|Sent by**any Agent**in the payment chain to confirm acceptance prior to<br>technical validation.|
|ACFC|AcceptedFundsChecked|Preceding check of technical validation and customer profile was<br>successful and an automatic funds check was positive.|Sent by**any Agent**in the payment chain to confirm the technical validation/<br>profile w as positive and automatic funds check w as positive.|
|ACIS|AcceptedandChequeIssued|Payment instruction to issue a cheque has been accepted, and the<br>cheque has been issued but not yet been deposited or cleared.|Sent by**any Agent**in the payment chain to confirm a cheque has been issued<br>as requested.|
|ACSC|AcceptedSettlementCompleted|Settlement has been completed.|Sent by the**Any Agent**to confirm settlement of a payment message leg.|
|ACSP|AcceptedSettlementInProcess|All preceding checks such as technical validation and customer<br>profile were successful and therefore the payment initiation has been<br>accepted for execution.|Sent by**any Agent**to the to confirm the payment is accepted follow ing<br>technical validations being successfully completed.|
|ACTC|AcceptedTechnicalValidation|Authentication and syntactical and semantical validation are<br>successful|Sent by**any Agent**in the payment chain to the previous Agent to confirm the<br>payment is accepted follow ing technical validations being successfully<br>completed.|
|ACWC|AcceptedWithChange|Instruction is accepted but a change will be made, such as date or<br>remittance not sent.|Sent by**any Agent**in the payment chain to the previous Agent to confirm the<br>payment is accepted follow ing amendments being made.|
|ACWP|AcceptedWithoutPosting|Payment instruction included in the credit transfer is accepted<br>without being posted to the creditor customer’s account.|Sent by**Creditor Agent**to the previous Agent to confirm the acceptance of<br>payment w ithout settlement on the creditor’s account,|
|CPUC|CashPickedUpByCreditor|Cash has been picked up by the Creditor.|Sent by**Creditor Agent**to the previous Agent to confirm that the cash<br>collection has been picked up by the Creditor,|
|PDNG|Pending|Payment initiation or individual transaction included in the payment<br>initiation is pending. Further checks and status update will be<br>performed.|Sent by**any Agent**in the payment chain to the previous Agent as an interim<br>status w hilst other validations are performed.|

---

<!-- ELEMENT 121 -->
The interbank pain.002 _Customer Payment Transaction Status_ element facilitates updates from the _Debtor Agent_ to the previous Agent, e.g., the _Forwarding Agent_ or the payment originator (the _Debtor_ / the _Initiating Party_ ) on changes to the status of the payment. Such Status Information messages (pain.002), with the exception of **reject code RJCT** which **is mandatory in CBPR+** , are bilateral agreed, where upon a variety of these Transaction Statuses may be used by the Instructed Agent at different stages of the payment processing. 

This diagram illustrates the logical order in which these codes may be used during the processing of the Payment Initiation messages (pain) and the interbank Payment Clearing And Settlement message (pacs) and the role of the Agents in providing these status. 

**==> picture [484 x 286] intentionally omitted <==**

**----- Start of picture text -----**<br>
Forwarding/Debtor Agent<br>Any RCVD<br>Agent<br>ACTC<br>ACCP<br>ACFC<br>PDNG<br>CPUC<br>RJCT ACWC<br>ACWP Creditor<br>ACIS Agent<br>ACCC<br>ACSP<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 122 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

## **Interbank Customer Payment Status Report – Relay** 

Use Case pn.2.1.1 – High Level Payment Initiation Interbank ‘relay’ status report 

Use Case pn.2.1.1.a – High Level Payment Initiation Interbank ‘relay’ status report Multi-bank Sweep 

Use Case pn.2.1.2 – High Level Payment Initiation Interbank ‘relay’ status report involving a Payment Market Infrastructure Use Case pn.2.1.3 – High Level Direct Debit Initiation Interbank ‘relay’ status report involving a Payment Market Infrastructure 

## **Interbank Customer Payment Status Report – Authorised Party** 

Use Case pn.2.2.1 – High Level Payment Initiation Interbank status report for Authorised Party 

Use Case pn.2.2.1.a. – High Level Payment Initiation Interbank status report for FI-Initiated Sweep (Long position at the Secondary Account) Use Case pn.2.2.1.b. – High Level Payment Initiation Interbank status report for Authorised Party to pay themselves as the Creditor. 

**Interbank Customer Payment Status Report – Financial Institution** Use Case pn.2.3.1 – High Level Payment Initiation Interbank status report for Financial Institution Payment Initiation 

## **Interbank multiple Payment Status Reports** 

Use Case pn.2.4.1 – High Level Payment Initiation Interbank ‘relay’ multiple status reports Use Case pn.2.4.2 – High Level Rejection of an incomplete ‘relay’ Payment 

Use Case pn.2.4.3 – High Level Direct Debit Initiation Interbank ‘relay’ multiple status reports involving a Payment Market Infrastructure

---

<!-- ELEMENT 123 -->
In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party. 

**==> picture [758 x 283] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4<br>pain.001 Interbank pain.001<br>pacs.008 camt.053<br>pain.002 F Interbank pain.002 A B<br>3a<br>3b<br>1 3 3b<br>Debtor Agent (A) debits the<br>Initiating Party sends a<br>account of Debtor and  Forwarding Agent (F) relays the<br>payment instruction to the<br>status ACSP (accepted settlement<br>initiates a credit transfer by<br>Forwarding Agent<br>in progress) to the Initiating Party,<br>forwarding a local credit<br>based upon a bilateral agreement<br>transfer message pacs.008<br>2<br>Forwarding Agent (F) forwards<br>the payment instruction to the  4<br>3a<br>Debtor Agent (A)<br>Debtor Agent (A) provides a  Creditor Agent (B) receives the<br>status update ACSP (accepted  credit transfer message, credits the<br>settlement in progress) to the Creditor and sends a camt 053<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 124 -->
## **Multi-bank Sweep** 

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party. 

**==> picture [758 x 283] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4<br>pain.001 Interbank pain.001<br>pacs.008 camt.053<br>pain.002 F Interbank pain.002 A B<br>3a<br>3b<br>1 3 3b<br>Debtor Agent (A) debits the<br>Initiating Party sends a payment<br>account of Debtor and  Forwarding Agent (F) relays the<br>instruction to the Forwarding<br>status ACSP (accepted settlement<br>initiates a credit transfer by<br>Agent to sweep excess funds<br>in progress) to the Initiating Party,<br>forwarding a local credit<br>from its subsidiary’s account to<br>based upon a bilateral agreement<br>the master account with Bank B transfer message pacs.008<br>4<br>2 3a<br>Debtor Agent (A) provides a  Creditor Agent (B) receives<br>Forwarding Agent (F) forwards<br>status update ACSP (accepted  the credit transfer message, credits<br>the payment instruction to the  settlement in progress) to the the Creditor and sends a<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 125 -->
## **a Payment Market Infrastructure** 

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party. 

**==> picture [744 x 284] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2<br>3 4<br>pain.001 Interbank pain.001<br>pacs.008 pacs.008<br>pain.002 F Interbank pain.002 A B<br>3a<br>3b<br>1 3 3b<br>Debtor Agent (A) debits the account<br>Initiating Party sends a  Forwarding Agent (F) relays the<br>of Debtor and initiates a credit<br>payment instruction to the  status ACSP (accepted settlement<br>transfer by forwarding a local credit<br>Forwarding Agent in progress) to the Initiating Party,<br>transfer message pacs.008 to a<br>based upon a bilateral agreement<br>Payment Market Infrastructure<br>2<br>(PMI)<br>Forwarding Agent (F) forwards<br>the payment instruction to the<br>3a 4<br>Debtor Agent (A)<br>Debtor Agent (A) provides a status  Creditor Agent (B) receives local<br>update ACSP (accepted settlement  credit transfer message via the<br>in progress) to the Forwarding  Payment Market Infrastructure and<br>Agent (F) based upon a bilateral credits the Creditor<br>**----- End of picture text -----**<br>


**==> picture [60 x 61] intentionally omitted <==**

---

<!-- ELEMENT 126 -->
## **involving a Payment Market Infrastructure** 

In the interbank relay scenario, the Creditor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party. 

**==> picture [746 x 280] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 3 2 1<br>Interbank pain.008 pain.008<br>pacs.003 pacs.003<br>B A Interbank pain.002 F pain.002<br>3a 3b<br>1 3 3b<br>Creditor Agent (A) instructs a<br>Initiating Party sends a direct  Forwarding Agent (F) relays the<br>direct debit transaction by<br>debit instruction to the  status ACSP (accepted settlement<br>sending a local direct debit<br>Forwarding Agent in progress) to the Initiating Party,<br>message pacs.003 to a Payment<br>based upon a bilateral agreement<br>Market Infrastructure<br>2<br>3a 4<br>Forwarding Agent (F) forwards  Creditor Agent (A) provides a<br>Debtor Agent (B) receives a local<br>the payment instruction to the  status update ACSP (accepted<br>direct debit message via the<br>Creditor Agent (A) settlement in progress) to the<br>Payment Market Infrastructure and<br>Forwarding Agent (F), based upon  debits the account of the Debtor<br>**----- End of picture text -----**<br>


**==> picture [61 x 60] intentionally omitted <==**

---

<!-- ELEMENT 127 -->
## **Party** 

In the scenario Authorised Party Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a payment based on Debit Authorisation with the Debtor and the Debtor Agent. 

**==> picture [758 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
Debit<br>DA<br>Authorisation 3 4<br>2<br>Interbank pain.001 pacs.008<br>camt.053<br>I Interbank pain.002 A pacs.002 B<br>3a<br>3<br>DA 4<br>As a pre-requisite the Debtor<br>Debtor Agent (A) debits the account of  Creditor Agent (B) receives credit transfer<br>provides Debit Authorisation to<br>Agent I to Initiate Payment from  Debtor and initiates a credit transfer message, credits the Creditor and<br>optionally provided a status report to<br>their account with the Debtor<br>Debtor Agent based upon a bilateral<br>Agent (A)<br>agreement. It also sends the result of the<br>2 3a sweep by camt.052 (intraday sweep) and<br>Agent (I) initiates a payment  or camt.053 (statement) to the Corporate<br>Debtor Agent (A) optionally provides a<br>request (pain.001) to the Debtor<br>status update to the Initiating Party<br>Agent (A) to move fund from the<br>(Agent I), based upon a bilateral<br>Debtor’s account, as an<br>agreement<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 128 -->
## **Party: FI-Initiated Sweep (Long position at the Secondary Account)** 

In the scenario Authorised Party Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a liquidity sweep on behalf of a corporate customer based on the sweep contract 

**==> picture [730 x 282] intentionally omitted <==**

**----- Start of picture text -----**<br>
Sweep  camt.052 1 3 4<br>Contract<br>2<br>Interbank pain.001 pacs.008<br>camt.053<br>I Interbank pain.002 A pacs.002 B<br>3a<br>1 3 4<br>Agent I receives intraday  Creditor Agent (B) receives credit transfer<br>Debtor Agent (A) debits the account of<br>balance report from  the Debtor and initiates a credit transfer message, credits the Creditor,  and sends<br>Debtor Agent (A) on behalf  a camt.053 (statement) at the end of the business<br>of their mutual customer day to the Creditor. An optional status report is sent<br>to the previous Agent based upon a bilateral<br>agreement<br>2 3a<br>Agent (I) initiates a sweep on  Debtor Agent (A) optionally provides a<br>behalf of the Corporate by  status update to the Initiating Party  See use case p.8.1.2 for a sweeping contract with<br>sending pain.001 to the Debtor  (Agent I), based upon a bilateral<br>a short position<br>Agent agreement<br>**----- End of picture text -----**<br>


See use case p.8.1.2 for a sweeping contract with a short position

---

<!-- ELEMENT 129 -->
## **Party to pay themselves as the Creditor** 

In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor’s account based on Debit Authorisation already in place to move money to themselves as the Creditor 

**==> picture [758 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
Debit<br>DA<br>Authorisation 3 4<br>2<br>Interbank pain.001 pacs.008<br>camt.053<br>I Interbank pain.002 A pacs.002 B I<br>3a<br>DA 3 4<br>As a pre-requisite the Debtor  Debtor Agent (A) debits the account of  Creditor Agent (B) receives the credit transfer<br>provides Debit Authorisation to  Debtor and initiates a credit transfer message, credits the Creditor, and sends a<br>Agent I to Initiate Payment from their  camt.053 (statement) at the end of the<br>account with the Debtor Agent (A) business day to the Creditor. An optional<br>status report is sent to the Debtor Agent based<br>upon a bilateral agreement<br>2 3a<br>Agent (I) initiates a payment request<br>Debtor Agent (A) optionally provides a<br>(pain.001) to the Debtor Agent (A) to<br>status update to the Initiating Party<br>move fund from the Debtor’s<br>(Agent I), based upon a bilateral<br>account, as an authorised party, to<br>agreement<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 130 -->
## **Institution Payment Initiation** 

In the scenario Financial Institution Payment Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a payment to a non-Financial Institution Creditor using their own account 

**==> picture [669 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
2 3<br>1<br>Interbank pain.001 pacs.008<br>camt.053<br>I Interbank pain.002 2a A pacs.002 B<br>1 2 3<br>Agent (I), the Debtor, initiates a  Creditor Agent (B) receives credit transfer<br>Debtor Agent (A) debits the account of<br>payment request (pain.001) to  message, credits the Creditor, and<br>Agent (I), the Debtor and initiates a<br>the Debtor Agent (A) to move  credit transfer optionally returns a status report to Debtor<br>funds from their own account Agent based upon a bilateral agreement.<br>It also sends camt.053 (statement) to the<br>non-FI Creditor<br>2a<br>Debtor Agent (A) optionally provides a<br>status update to the Initiating Party<br>(Agent I), based upon a bilateral<br>agreement<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 131 -->
In the interbank relay scenario, the Forwarding Agent provides multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle. 

**==> picture [796 x 286] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2<br>4 5<br>pain.001 Interbank pain.001<br>camt.053<br>pacs.008<br>pain.002 3a F Interbank pain.002 3 A B<br>pain.002 4b Interbank pain.002 4a<br>1 3 4b<br>4<br>Initiating Party sends a  Debtor Agent (A) optionally  Debtor Agent (A) processes the  Forwarding Agent (F) relays a<br>payment instruction to the  provides a status update ACTC  payment and sends to the  further status update ACSP<br>Forwarding Agent (accepted technical validations  Creditor Agent (B) (accepted settlement in<br>are successful) to the  progress), to the Initiating Party,<br>2 Forwarding Agent (F), based  based upon a bilateral<br>Forwarding Agent (F) forwards upon a bilateral agreement. 4a agreement.<br>Debtor Agent (A) optionally<br>the payment instruction to the<br>provides a further status update<br>Debtor Agent (A) 3a 5<br>ACSP (accepted settlement in<br>Forwarding Agent (F) relays the<br>progress) to the Forwarding Agent  Creditor Agent (B) processes the<br>status ACTC (accepted technical<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 132 -->
In the interbank relay scenario, the Forwarding Agent provides multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle. 

**==> picture [820 x 298] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2<br>3<br>pain.001 Interbank pain.001<br>pacs.008<br>pain.002 3b F Interbank pain.002 3a A B<br>pacs.002<br>pain.002 4b Interbank pain.002 4a<br>+ Reject<br>+ Reject  + Reject  Reason  Where a  payment is rejected , the use of<br>Reason  Reason  the pain.002 status RJCT (Reject) with the<br>ISO Status Reason Code is  mandatory.<br>1 3b 4a<br>3<br>Initiating Party sends a  Debtor Agent (A) processes the  Forwarding Agent (F) relays the status  Debtor Agent refund the Debtor’s<br>payment instruction to the  payment and sends to the  ACSP (accepted settlement in  account and update the status<br>Forwarding Agent Creditor Agent (C) progress) to the Initiating Party, based  RJCT with the reason code to the<br>upon a bilateral agreement. Forwarding Agent<br>2<br>3a<br>Forwarding Agent (F) relays  4b<br>Debtor Agent (A) optionally  Having received the payment the  Forwarding Agent (F) relays a<br>the payment to the Debtor<br>provides a status update ACSP  Creditor Agent  recognises the payment  further status update RJCT with<br>Agent (A)<br>( t d ttl t i ) th d t th I iti ti<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 133 -->
## **(pain.002) involving a Payment Market Infrastructure** 

In the interbank relay scenario, the Creditor Agent sends multiple status reports to the Forwarding Agent which relays the same information to the Initiating Party. 

**==> picture [821 x 283] intentionally omitted <==**

**----- Start of picture text -----**<br>
3 2 1<br>pacs.003 pacs.003 Interbank pain.008 pain.008<br>B pacs.002 pacs.002 A 3a Interbank pain.002 F 3b pain.002<br>pacs.002<br>Where a direct debit is  rejected/  4a Interbank pain.002 4b pain.002<br>returned , the use of the pain.002<br>status RJCT (Reject) with the ISO  + Reject<br>+ Reject  + Reject<br>Status Reason Code is  mandatory. Reason<br>Reason  Reason<br>1 3 4a<br>3b<br>Initiating Party sends a direct  Creditor Agent (A) instructs a direct  Forwarding Agent (F) relays the  Creditor Agent update the status<br>debit instruction to the  debit transaction by sending a local  status ACSP (accepted settlement  RJCT with the reason code to the<br>Forwarding Agent direct debit message pacs.003 to a  in progress) to the Initiating Party,  Forwarding Agent<br>Payment Market Infrastructure  based upon a bilateral agreement<br>2 (PMI)<br>Forwarding Agent (F) forwards<br>3a 4<br>the payment instruction to the<br>Creditor Agent (A) Creditor Agent (A) provides a  Having received the direct debit, PMI  Forwarding Agent (F) relays a<br>i h i b<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 134 -->
# **Interbank Customer Direct Debit Initiation** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 135 -->
**==> picture [41 x 52] intentionally omitted <==**

**==> picture [59 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
ISO<br>**----- End of picture text -----**<br>


ISO 20022 message element 

## _**Group Header**_ 

- ➢ _**Message Identification**_ 

- ➢ _**Initiating Party**_ – where different from _**Creditor**_ 

- ➢ _**Forwarding Agent**_ 

## _**Payment Information**_ 

   - ➢ _**Payment Information Identification**_ 

   - ➢ _**Requested Collection Date**_ 

   - ➢ _**Creditor**_ 

- ➢ _**Creditor Agent**_ 

- _**Direct Debit Transaction Information**_ 

   - ➢ _**Payment Identification**_ 

   - ➢ _**Instructed Amount**_ 

   - ➢ _**Charge Bearer**_ 

   - ➢ _**Mandate Identification**_ 

   - ➢ _**Debtor Agent**_ 

**==> picture [60 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
MT<br>**----- End of picture text -----**<br>


MT Field Name & (Tag option) 

- **Sequence A –** General Information **:** ➢ **Sender’s Reference** (Field 20) 

- ➢ **Instructing Party** (Field 50 C or L) 

- Message **Sender** in a ‘relay’ scenario **Sequence A –** General Information **:** 

   - ➢ **Customer Specified Reference** (Field 21R) 

   - ➢ **Requested Execution Date** (Field 30) 

   - ➢ **Creditor** (Field 50 A or K)* 

- ➢ **Creditor’s Bank** (Field 52 A, C or D)* 

- **Sequence B –** Transaction Details **:** 

   - ➢ **Transaction Reference** (Field 21) 

   - ➢ **Currency and Transaction Amount** (Field 32B) 

   - ➢ **Details of Charges** (Field 71A) 

   - ➢ **Mandate Reference** (Field 21C) 

   - ➢ **Debtor’s Bank** (Field 57 A, C or D)

---

<!-- ELEMENT 136 -->
**==> picture [140 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
pain.008<br>**----- End of picture text -----**<br>


**==> picture [105 x 65] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [105 x 66] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Information<br>**----- End of picture text -----**<br>


**==> picture [104 x 63] intentionally omitted <==**

**----- Start of picture text -----**<br>
Direct Debit<br>Transaction<br>Information<br>**----- End of picture text -----**<br>


The pain.008 message is composed of three blocks: 

- _**Group Header**_ contains a set of characteristics that relates to all individual transaction. 

   - _**Payment Information**_ contains a set of characteristics that relates to the credit side of the transaction, such as Creditor and Creditor Agent. 

- 

- _**Direct Debit Transaction Information**_ contains, among others, elements related to the debit side of the transaction, such as Debtor and Debtor Agent and optionally mandate related information. 

**==> picture [60 x 60] intentionally omitted <==**

Direct Debit Initiation relay messages in a many-to-many space allow for multiple transactions as they will be typically cleared by Automated Clearing House (ACH) batch

---

<!-- ELEMENT 137 -->
**==> picture [803 x 237] intentionally omitted <==**

**----- Start of picture text -----**<br>
B A F<br>Debtor Debtor Agent Creditor Agent Forwarding Initiating Party* Creditor<br>Agent<br>pain.008**<br>Interbank pain.008<br>pain.002<br>Interbank pain.002<br>pacs.003<br>pacs.002<br>camt.053<br>*Initiating Party may alternative represent an authorised party such as a head office<br>**----- End of picture text -----**<br>


- *Initiating Party may alternative represent an authorised party such as a head office **or other proprietary method for instructing a direct debit initiation request. 

Interbank Customer Direct Debit Initiation message is sent by the Initiating Party to the Forwarding Agent or the Creditor Agent. It is used to request single or bulk collection(s) of funds from one or various debtor’s account(s) to a creditor. 

_**Relay**_ : Interbank pain.008 message is sent by the Initiating party (the Creditor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.008 message to the Creditor Agent to initiate the direct debit instruction(s)..

---

<!-- ELEMENT 139 -->
**Min 1 – Max 1** 

**==> picture [74 x 52] intentionally omitted <==**

Each ISO20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For the Payment Initiation (pain) messages the _Message Identification_ has no exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction. 

**==> picture [60 x 60] intentionally omitted <==**

Each transaction’s _Direct Debit Transaction Information_ contains a variety of nested _Payment Identification_ elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference). 

**==> picture [55 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
CGI<br>**----- End of picture text -----**<br>


For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Creditor or authorized third party) of the pain.008. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 140 -->
## **Min 1 – Max 1** 

The pain.008 message _**Creation Date Time**_ captures the date and time which the message was created. 

It is defined by _**ISO Date Time**_ with mandatory date and time components expressed in the following formats: 

**10** 

1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ 2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 3. Local time format YYYY-MM-DDThh:mm:ss.sss 

**==> picture [60 x 60] intentionally omitted <==**

Unlike other CBPR+ messages, the interbank pain.008 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2[nd] option). Otherwise use UTC time (1[st] option). Decimal fractions of milliseconds with 3 digits are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 141 -->
## **Min 0 – Max 2** 

The pain.008 message _**Authorisation**_ allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The _Authorisation_ uses an embedded code set or free text form. It has no equivalent in the legacy MT direct debit message. 

|**Code**|**Description**|**Description**|
|---|---|---|
|ILEV|Instruction Level Authorisation|File requires all customer transactions to be authorised or approved.|
|FDET|File Level Authorisation Details|Additional file level approval, with the ability to view both the payment information block<br>and supportingtransaction detail.|
|FSUM|File Level Authorisation Summary|Additional file level approval, with the ability to view only the payment information block.|
|AUTH|Pre Authorised File|File has been pre-authorised or approved within the originating customer environment<br>and no further approval is required.|
|For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for<br>Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.|||



**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 142 -->
**Min 1 – Max 1** The pain.008 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

Multiple transactions are allowed in CBPR+ direct debit usage guidelines. However, it is recommended to have only one single direct debit transaction unless bilaterally determined. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ direct debit usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant collection, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 143 -->
**==> picture [248 x 207] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initiating Party<br>Creditor Authorised Party<br>Forwarding Agent / FI<br>**----- End of picture text -----**<br>


**Min 1 – Max 1** 

The _**Initiating Party**_ can either be the _**Creditor**_ or an Authorised Party who initiates direct debit transactions on behalf of the _Creditor_ . The Initiating Party can be, for example, the Head Office which is authorised by its subsidiary to request for payment amount to be collected from the _Debtor_ . In the centralization model, the _Initiating Party_ can also be a payment factory or shared service centre or third party agent, which has authority to send the message on behalf of the _Creditor_ . 

In the interbank pain.008 ‘Relay’ message use case: The _Initiating Party_ sends the pain.008 message to the _**Forwarding Agent**_ which acts as a concentrating financial . institution. It will forward the pain.008 message to the _**Creditor Agent**_ 

**==> picture [60 x 59] intentionally omitted <==**

Initiating Party has a mandate (debit authority agreement) to debit the account of the Debtor.

---

<!-- ELEMENT 144 -->
The _**Initiating Party**_ can either be the _**Creditor**_ or an authorised party, such as Financial Institution, in the context of interbank pain.008. Sub elements describe the _Initiating Party_ in greater detail. 

Mandatory _**Name**_ where Postal Address is provided. 

_**Name**_ 

**==> picture [228 x 295] intentionally omitted <==**

**==> picture [272 x 192] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address Initiating<br>Party<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing _**structured**_ Postal Address including at least Town Name and Country if used. 

Nested element capturing the various types of identifiers, e.g. BIC, LEI etc. 

_**Identification**_ 

**==> picture [91 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
Contact<br>Details<br>**----- End of picture text -----**<br>


Optional element to capture the Initiating Party’s ISO country code 

_**Country of Residence**_

---

<!-- ELEMENT 145 -->
**==> picture [44 x 49] intentionally omitted <==**

**Min 1 – Max 1** The _**Forwarding Agent**_ is mandatory in a relay scenario whereby the _Initiating Party_ (the _Creditor_ or authorised third party) has to provide _**Business Identifier Code**_ (BICFI) of the _Forwarding Agent_ in the pain.008 message. The Forwarding Agent acts as a concentrating financial institution and forwards the pain.008 message to the _Creditor Agent_ for execution. 

Other options to complement the identity of the _**Forwarding Agent**_ include: 

- Clearing System Member ID 

- • LEI (Legal Entity Identifier) 

**==> picture [287 x 162] intentionally omitted <==**

**----- Start of picture text -----**<br>
BICFI<br>Clearing<br>Clearing<br>System<br>Financial  Member Id System Id<br>Institution<br>Identification<br>LEI<br>Various sub-<br>element<br>**----- End of picture text -----**<br>


**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 147 -->
The CBPR+ pain.008 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognise that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory. 

As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message. Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used. 

**CGI-MP** payment Initiation/ **CBPR+** payment initiation interbank Structured Unstructured 

**==> picture [45 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
pain.008<br>**----- End of picture text -----**<br>


**==> picture [48 x 53] intentionally omitted <==**

**==> picture [367 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
Unstructured Many domestic proprietary<br>payments<br>Structured Unstructured<br>CBPR+  payments<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 148 -->
## **Min 1 – Max 1** 

The Interbank Customer Direct Debit Initiation _**Payment Information Identification**_ provides a mandatory element to identify the payment information group within the message. 

**==> picture [89 x 58] intentionally omitted <==**

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions. 

**==> picture [63 x 62] intentionally omitted <==**

For a single batch in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 149 -->
## **Min 1 – Max 1** 

The pain.008 message _**Payment Method**_ specifies the means of payment that will be used to move the amount of money. The payment method code “DD” Direct Debit must be used. 

**==> picture [63 x 65] intentionally omitted <==**

**Code Name Definition** DD Direct Debit Collection of an amount of money from the Debtor’s bank account by the Creditor. The amount of money and dates of collections may vary. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 150 -->
## **Min 0 – Max 1** 

The pain.008 message _**Batch Booking**_ identifies whether a single entry per individual transaction or a batch entry for the sum of the amounts of all transactions within the group of a message is requested. 

**==> picture [42 x 54] intentionally omitted <==**

Batch booking is used to request for a consolidated credit entry on the Creditor’s account. Where this optional element is not used, the default of single credit entries is applied on the Creditor’s account. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 151 -->
**Min 1 – Max 1** The pain.008 message mandatory _**Requested Collection Date**_ element, captures the date at which the creditor requests that the amount of money is to be collected from the debtor. 

**10** 

It is defined by _**ISO Date**_ expressed in the _**YYYY-MM-DD format**_ . 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 152 -->
## **Min 1 – Max 1** 

Mandatory _**Name**_ (where a BIC identifier is not provided) by which the party is known 

The ISO 20022 pain messages describe the _**Creditor**_ as the party whose account was credited for a transaction. The _Creditor_ sub elements describe the _Creditor_ in greater detail. 

_**Name**_ 

**==> picture [195 x 295] intentionally omitted <==**

Nested element capturing either structured or unstructured _Creditor_ address details. 

_**Postal Address**_ 

## _Creditor_ 

Note: Structured address is strongly recommended with mandatory Town Name and Country 

**==> picture [35 x 34] intentionally omitted <==**

**==> picture [69 x 78] intentionally omitted <==**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

_**Identification**_ 

Optional element to _**Country of**_ capture the _Creditor_ ’s ISO _**Residence**_

---

<!-- ELEMENT 153 -->
**Min 1 – Max 1** The pain.008 _**Creditor Account**_ is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement. 

The _**Creditor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account, recommended. **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 154 -->
**Min 1 – Max 1** 

The _**Creditor Agent**_ is a static role in the pain.008 Customer Direct Debit Initiation. This agent maintains a relationship with their customers, the _Creditor_ . 

**==> picture [80 x 137] intentionally omitted <==**

**==> picture [62 x 63] intentionally omitted <==**

Note: Although the _**Creditor Agent, Debtor Agent, Creditor and Debtor**_ all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Creditor Agent and Debtor Agent become the Statement Account Servicer and the Creditor and the Debtor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section. 

**==> picture [53 x 39] intentionally omitted <==**

For Agent Identification, BIC is preferred, alternatively Clearing Member

---

<!-- ELEMENT 155 -->
## **Min 0 – Max 1** 

The pain.008 _**Creditor Agent Account**_ is used to capture the account information related to the Creditor Agent. 

The _**Creditor Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Account Servicing Institution **Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [62 x 51] intentionally omitted <==**

Creditor Agent and Debtor Agent are Financial Institutions, therefore the nested elements _**Name**_ and _**Proxy**_ are unlikely to be used.

---

<!-- ELEMENT 156 -->
**Min 0 – Max 1** The pain.008 optional _**Charges Account**_ element, which is used to process charges associated with a transaction. 

**==> picture [83 x 70] intentionally omitted <==**

Charges account should be used when charges have to be booked to an account different from the account identified in debtor’s account. 

**==> picture [60 x 60] intentionally omitted <==**

This element is not widely used in the payment industry. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 157 -->
**Min 0 – Max 1** The pain.008 optional _**Charges Account Agent**_ element, which is used to specify the agent that services a charges account. 

**==> picture [83 x 99] intentionally omitted <==**

Charges account agent should only be used when the charges account agent is different from the creditor agent. 

**==> picture [60 x 60] intentionally omitted <==**

This element is not widely used in the payment industry. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 159 -->
**Min 1 – Max 1** 

The pain.008 message contains _**Payment Identification**_ which provides a set of elements to identify the payment of which several are mandatory elements. 

**==> picture [235 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Identification<br>$<br>**----- End of picture text -----**<br>


a point-to-point reference of 35 characters long will be returned to account statements if provided by the initiating party. 

_**Instruction Identification**_ **Min 0 – Max 1** 

**==> picture [33 x 34] intentionally omitted <==**

Note: Instruction Id is mandatory in other CBPR+ messages as it maps directly with the mandatory Sender’s Reference (Field 20) of the legacy MT payment messages. 

an end-to-end reference provided by the _Initiating Party_ which must be passed unchanged throughout the payment and reported to the _Creditor_ . 

_**End to End Identification**_ **Min 1 – Max 1** 

note: if the Initiating Party has not provided an end-to-end identifier, the _Creditor Agent_ may populate “NOTPROVIDED” to comply the mandatory need of this element. 

**==> picture [33 x 35] intentionally omitted <==**

the Unique End-to-end Transaction Reference created using the UUID v4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their Payment Initiation request, and also included in reporting messages. _Direct Debit Transfer Transaction Information_ 

**==> picture [54 x 26] intentionally omitted <==**

**----- Start of picture text -----**<br>
UETR<br>**----- End of picture text -----**<br>


**==> picture [60 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1<br>**----- End of picture text -----**<br>


_Direct Debit Transfer Transaction Information_ 

**==> picture [10 x 11] intentionally omitted <==**

---

<!-- ELEMENT 160 -->
**Min 0 – Max 1** 

The pain message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. 

_**Instruction Priority**_ **Min 0 – Max 1** 

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the 

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. 

_**Service**_ code or a _**Level**_ **Min 0 – Max 3** _**Local** Payment_ _**Instrument** Type_ **Min 0 – Max 1** _Information_ _**Sequence Type**_ i **Min 0 – Max 1** 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, CORE is a transaction related to SEPADirect Debit Core. 

**==> picture [36 x 33] intentionally omitted <==**

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

A nested element which uses an embedded code to identify the direct debit sequence, such as first, recurrent, final or one-off 

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. 

_**Category**_ 

_Direct Debit Transfer Transaction Information_ 

**==> picture [10 x 11] intentionally omitted <==**

---

<!-- ELEMENT 161 -->
**£ $** 

¥ 

**Min 1 – Max 1** The pain.008 nested _**Instructed Amount**_ element captures the amount of money to be moved between the Debtor and the Creditor before deduction of charges. 

**==> picture [44 x 44] intentionally omitted <==**

_**Instructed Amount**_ 

The _**Instructed Amount**_ captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the as ordered the This amount has to be currency by initiating party. transported unchanged through the transaction chain. This element is comparable with both the legacy Field 33B and Field 32B. 

**==> picture [60 x 60] intentionally omitted <==**

For multiple transactions, the currency must be the same for each transaction. 

_Direct Debit Transfer Transaction Information_ 

**==> picture [10 x 11] intentionally omitted <==**

---

<!-- ELEMENT 162 -->
**Min 0 – Max 1** 

The _**Charge Bearer**_ element exists at the Direct Debit Transaction Information level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A ‘Details of Charges’ 

**Charge Code Description Bearer** CRED Creditor **(0.1)** DEBT Debtor **71A: Details Code Description** SHAR Shared **of Charges** BEN Beneficiar y SLEV Followin Service Level g OUR Our Customer Charges SHA Shared Charges 

**==> picture [54 x 52] intentionally omitted <==**

Charge Bearer Code SLEV (Following Service Level) is not allowed in the CBPR+ pain.008 interbank. 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 163 -->
## **Min 0 – Max 1** The pain.008 _**Direct Debit Transaction**_ component provides information specific to the direct debit mandate. 

> _**Mandate**_ Provides further details of the direct debit mandate signed between 

> _**Related**_ the creditor and the debtor. E.g., Mandate Identification, Date of 

> _**Information**_ Signature and Electronic Signature. **Min 0 – Max 1** _Direct Debit_ _**Creditor Scheme**_ Credit party that signs the mandate, may be used _Transaction_ _**Identification**_ supported by the Direct Debit Schema. (see next page **Min 0 – Max 1** 

Credit party that signs the mandate, may be used if supported by the Direct Debit Schema. (see next page for additional detail on this nested element) 

_**Pre Notification Identification**_ **Min 0 – Max 1** 

Unique and unambiguous identification of the pre-notification which is sent separately from the direct debit instruction. 

_**Pre Notification**_ 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 164 -->
## **Min 0 – Max 1** 

The _**Creditor Scheme Identification**_ element within the pain.008 message optionally provides information related to the credit party that signs the mandate who is different from the Creditor. 

**==> picture [88 x 87] intentionally omitted <==**

The _**Creditor Scheme Identification**_ element offers the following options: 

Name 

Postal Address: Not used often Identification 

Country of Residence Contact Details 

**==> picture [54 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
CGI<br>**----- End of picture text -----**<br>


CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit Scheme. 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 165 -->
Ultimate Party Ultimate Ultimate Debtor Creditor 

**Min 0 – Max 1** 

**Min 0 – Max 1** 

The pain.008 message introduces _**Ultimate Creditor**_ and _**Ultimate Debtor**_ . The _**Ultimate Creditor**_ element should not be confused with an _**Initiating**_ who send a direct debit initiation on behalf of the _**Party**_ may request _**Creditor** ,_ for example, Payment Factory. 

CBPR+ premise is that an _**Ultimate Creditor**_ has no financial regulated direct account relationship with the corresponding Creditor. Likewise, an _**Ultimate Debtor**_ has no financial regulated account relationship with the corresponding Debtor. 

The _**Ultimate Creditor**_ and _**Ultimate Debtor**_ can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence. 

**==> picture [59 x 60] intentionally omitted <==**

In the context of direct debit, _Ultimate Creditor_ and _Ultimate Debtor_ are not commonly used. 

_Direct Debit Transaction Information_ 

**==> picture [11 x 11] intentionally omitted <==**

---

<!-- ELEMENT 166 -->
**Min 1 – Max 1** The _**Debtor Agent**_ is a static roles in the pain.008 Customer Direct Debit Initiation. This agent maintain a relationship with their customers, the _Debtor_ . 

**==> picture [84 x 137] intentionally omitted <==**

**==> picture [62 x 63] intentionally omitted <==**

Note: Although the _**Debtor Agent, Creditor Agent, Debtor and Creditor**_ all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section. 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 167 -->
## **Min 0 – Max 1** 

. The pain.008 _**Debtor Agent Account**_ is used to capture the account information related to the _Debtor Agent_ 

The _**Debtor Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**==> picture [42 x 22] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Account Servicing Institution **Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 168 -->
**Min 1 – Max 1** 

**==> picture [92 x 82] intentionally omitted <==**

**----- Start of picture text -----**<br>
Name<br>**----- End of picture text -----**<br>


## _**Name**_ by which the party is known 

The ISO 20022 pain messages describes the _**Debtor**_ as the party whose account was debited for a transaction. The _Debtor_ sub elements describe the _Debtor_ in greater detail. 

Note: it is recommended to include the Postal Address together with the Name 

**==> picture [200 x 296] intentionally omitted <==**

**==> picture [169 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
Debtor<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Debtor_ address details. 

_**Postal Address**_ 

Note: Structured address is strongly recommended with mandatory Town Name and Country 

**==> picture [35 x 34] intentionally omitted <==**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

_**Identification**_ 

Optional element to capture the _Debtor_ ’s ISO 

_**Country of Residence**_

---

<!-- ELEMENT 169 -->
**Min 1 – Max 1** The pain.008 _**Debtor Account**_ is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement. 

The _**Debtor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

- **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 170 -->
Ultimate Party Ultimate Ultimate Debtor Creditor 

**Min 0 – Max 1** 

**Min 0 – Max 1** 

The pain.008 message introduces _**Ultimate Debtor**_ and _**Ultimate Creditor**_ . The _**Ultimate Debtor**_ element should not be confused with an _**Initiating Party**_ who may send a payment initiation request on behalf of the _**Debtor** ,_ for example, Payment Factory. 

CBPR+ premise is that an _**Ultimate Debtor**_ has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an _**Ultimate Creditor**_ has no financial regulated account relationship with the corresponding Creditor. 

The _**Ultimate Debtor**_ and _**Ultimate Creditor**_ can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence. 

**==> picture [59 x 60] intentionally omitted <==**

In the context of direct debit, Ultimate Creditor and Ultimate Debtor are not commonly used. 

_Direct Debit Transaction Information_ 

**==> picture [11 x 11] intentionally omitted <==**

---

<!-- ELEMENT 171 -->
## **Min 0 – Max 1** 

The _**Instruction for Creditor Agent**_ element within the pain.008 message optionally provides information related to the processing of the direct debit. 

**==> picture [88 x 87] intentionally omitted <==**

The _**Instruction for Creditor Agent**_ element offers a maximum of 140 characters to provide further information related to the processing of the direct debit instruction, that may need to be acted upon by the _Creditor Agent_ , depending on bilateral agreement. 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 172 -->
## **Min 0 – Max 1** 

The _**Purpose**_ element within the pain.008 message captures the reason for the payment transaction which use an external ISO code or may either Purpose a proprietary code. 

The is used to the nature of the IVPT Invoice FEES of purpose capture payment, e.g., Payment, Payment Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the _Debtor_ . 

**==> picture [123 x 91] intentionally omitted <==**

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. For example, LOAR is classified within the Finance categorisation, with the _Name_ Loan Repayment described as a repayment of loan to lender. 

**==> picture [63 x 63] intentionally omitted <==**

_Category Purpose_ also captures a high level purpose, which unlike _Purpose_ is less granular but can trigger special processing e.g. _Category Purpose_ code RPRE ‘Represented’ may trigger a representation of previously reversed or returned direct debit transactions. 

**==> picture [11 x 12] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 173 -->
## **Min 0 – Max 10** 

The _**Regulatory Reporting**_ block within the pain.008 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s. 

**Min 0 – Max 1** 

The _**Debit Credit Reporting Indicator**_ utilises an embedded choice of code to indicate whether the regulatory reporting applies to the: 

**==> picture [109 x 67] intentionally omitted <==**

- DEBT (debit) 

- • CRED (credit) 

- • BOTH 

**Min 0 – Max 1** The _**Authority**_ element captures the _**Name**_ and _**Country**_ code of the Authority/Entity requiring the regulatory reporting information. 

**Min 0 – Max *** The _**Details**_ element provides the detail on the regulatory reporting information. 

**==> picture [62 x 37] intentionally omitted <==**

**==> picture [10 x 4] intentionally omitted <==**

_Direct Debit Transaction Information       Regulatory Reporting_ Debit Credit Reporting Indicator

---

<!-- ELEMENT 174 -->
**Min 0 – Max 1** 

The pain.008 nested _**Tax**_ element captures information related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s). 

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

<!-- ELEMENT 175 -->
## **Min 0 – Max 10** 

The _**Related Remittance Information**_ element within the pain.008 message is nested to provide information related to the handling of remittance information. 

## **Min 0 – Max 1** 

The _**Remittance Identification**_ captures a unique reference assigned by the initiating party of the direct debit to identify the remittance information sent separately from the direct debit instruction. 

## **Min 0 – Max *** 

**==> picture [89 x 83] intentionally omitted <==**

- The _**Remittance Location Details**_ uses a set of nested elements to provide information on either the location of or the delivery of remittance information. 

   - _**Method**_ requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email) 

   - _**Electronic Address**_ provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information maybe deposited or retrieved. 

   - _**Postal Address**_ provides the postal address to which an agent is to send the remittance information 

**==> picture [62 x 63] intentionally omitted <==**

- Unlike CBPR+ pacs messages, in the interbank pain.008 message, Related Remittance Information and Remittance Information are non-mutually exclusive due to a corporate use case of populating both information . 

- blocks for detailing remittance advices which are part of value-added service offered by the _Creditor Agent_ 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 176 -->
**Min 0 – Max 1** 

The optional _**Remittance Information**_ element within the pain.008 message is nested to provide either _**Structured**_ or _**Unstructured**_ information related to payment, such as invoices. 

_**Remittance Information**_ enables the matching/reconciliation of an entry that the payment is intended to settle. 

**==> picture [56 x 65] intentionally omitted <==**

**Min 0 – Max 1** The **Unstructured** sub element captures free format _Remittance Information_ which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence. **Min 0 – Max *** The **Structured** element is nested capturing rich structured _Remittance Information,_ and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification) The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-toend transportation of this data. 

**==> picture [11 x 12] intentionally omitted <==**

**==> picture [11 x 10] intentionally omitted <==**

**==> picture [10 x 5] intentionally omitted <==**

_Direct Debit Transaction Information_ 

Remittance Information

---

<!-- ELEMENT 177 -->
The bilaterally/multilaterally agreed _**Remittance Information**_ which is _**Structured**_ must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information. 

**==> picture [457 x 131] intentionally omitted <==**

## example of _Structured_ invoice information 

The _**Creditor Remittance Information**_ is provided by the _**Creditor**_ in the Cash Management Reporting messages’ Remittance Information component, for example, the camt.053 Bank to Customer Statement. 

**Structured** <Strd> xml tag In this example Referred Document **Reference Document** <Rf rdDocInf> Information and its nested elements have **Information** multiplicity which support up to 9,000 **Type** <Tp> business character of information. Whereby this element names **Code Or Proprietary** <CdOrPrtry > information element can be repeated to include more **Code** <Cd> **CINV** coded information such as another invoice. **Number** <Nb> **A0000101 Related Date** <Dt> **2019-10-29** 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [188 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
Remittance Information<br>**----- End of picture text -----**<br>


_Direct Debit Transaction Information_

---

<!-- ELEMENT 178 -->
The _**Creditor Reference**_ in the _Creditor Reference Information_ component in the structured remittance information is generated by _Creditor_ to allow for the identification of the underlying documents and enable reconciliation by the Creditor upon receipt of the amount of money. Creditor Reference in the Structured Remittance Information can be based on ISO 11649 

- 2 letters “RF” 

- 2 digits check digit 

- 21 letters/digits creditor reference 

By providing the Creditor Reference in the pain.008, such as invoice number for collection, it will facilitate STP and auto-match the incoming credit entry. The Creditor Reference can be extracted from the statement (e.g., camt.053 Structured Remittance information within the Transaction Details or MT 940 Field 61 or Field 86). Equally the End-To-End Identification could perform a similar function 

**==> picture [52 x 49] intentionally omitted <==**

SCORE Guideline: For Creditor Reference information, in instances where the Creditor Reference Type code is SCOR (Structured Communication Reference) and the Creditor Reference is structured in accordance with ISO 11649, the 

_Direct Debit Transaction Information_ 

**==> picture [11 x 9] intentionally omitted <==**

Remittance Information 

**==> picture [10 x 11] intentionally omitted <==**

---

<!-- ELEMENT 179 -->
Use case should be considered as a principle example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

**Interbank Customer Direct Debit Initiation - Relay** – Use Case pn.8.1.1 High Level Direct Debit Initiation Interbank ‘relay’ (pain.008) – Use Case pn.8.1.2 High Level Direct Debit Initiation Interbank ‘relay’ (pain.008) involving a Payment Market Infrastructure

---

<!-- ELEMENT 180 -->
In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collections of funds from the debtor's accounts for a creditor. 

**==> picture [758 x 283] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 3 2 1<br>Interbank pain.008 pain.008<br>camt.053 pacs.003<br>B A Interbank pain.002 F pain.002<br>3a<br>camt.053 3b<br>1 3 3b<br>Creditor Agent (A) instructs<br>Initiating Party sends a direct<br>debit instruction to the  Debtor Agent (B) to perform a  Forwarding Agent (F) relays the<br>status ACSP (accepted settlement<br>direct debit transaction by<br>Forwarding Agent<br>in progress) to the Initiating Party,<br>sending a local direct debit<br>based upon a bilateral agreement<br>message or pacs.003<br>2<br>Forwarding Agent (F) forwards<br>the direct debit instruction to  4<br>3a<br>the Creditor Agent (A) Creditor Agent (A) provides a  Debtor Agent (B) processes the<br>status update ACSP (accepted  direct debit and sends the statement<br>settlement in progress) to the to Debtor<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 181 -->
## **Payment Market Infrastructure** 

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collection of funds from the debtor's accounts for a creditor (through a Payment Market Infrastructure). 

**==> picture [760 x 281] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 3 2 1<br>Interbank pain.008 pain.008<br>camt.053 pacs.003 pacs.003<br>B Interbank pain.002 F pain.002<br>A<br>3a camt.053 3b<br>1 3 3b<br>Creditor Agent (A) instructs a<br>Initiating Party sends a direct  Forwarding Agent (F) relays the<br>direct debit transaction by<br>debit instruction to the  status ACSP (accepted settlement<br>sending a local direct debit<br>Forwarding Agent in progress) to the Initiating Party,<br>message or pacs.003 to a<br>based upon a bilateral agreement<br>Payment Market Infrastructure<br>2 3a 4<br>Creditor Agent (A) provides a  Debtor Agent (B) receives a local<br>Forwarding Agent (F) forwards<br>status update ACSP (accepted  direct debit message via the<br>the payment instruction to the<br>settlement in progress) to the  Payment Market Infrastructure<br>Creditor Agent (A)<br>Forwarding Agent (F) based upon (PMI) and debits the account of the<br>**----- End of picture text -----**<br>


**==> picture [61 x 61] intentionally omitted <==**

---

<!-- ELEMENT 182 -->
# **messages**

---

<!-- ELEMENT 183 -->
## **Payments** 

**pacs.008** - Financial Institution to Financial Institution Customer Credit Transfer **pacs.009** - Financial Institution Credit Transfer **pacs.009 (cov)** - Financial Institution ‘Cover’ Credit Transfer **– pacs.009 (adv)** Financial Institution ‘advice’ of Credit Transfer 

**Payment Rejection and Return pacs.002** – Financial Institution To Financial Institution Payment Status Report – **pacs.004** Payment Return 

**Direct Debit Payments pacs.010** - Interbank Direct Debit **pacs.010 (col) -** Interbank Direct Debit Margin Collection **pacs.003** - Financial Institution to Financial Institution Customer Direct Debit

---

<!-- ELEMENT 184 -->
# **Financial Institution to Financial Institution Customer Credit Transfer** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 185 -->
## The pacs.008 has two core sets of nested elements: 

**pacs.008** 

**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


Credit Transfer Transaction Information 

**==> picture [60 x 60] intentionally omitted <==**

- _**Group Header**_ which contains a set of characteristics that relates to all individual transaction 

- _**Credit Transfer Transaction Information**_ which contains elements providing information specific to the individual credit transfer transaction. 

Payment messages in a many-to-many payment are considered as a 

single transaction.

---

<!-- ELEMENT 186 -->
**==> picture [748 x 223] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.008<br>pacs.002<br>pacs.008<br>pacs.008<br>pacs.002<br>pacs.002<br>**----- End of picture text -----**<br>


The Financial Institution To Financial Institution Customer Credit Transfer message is sent by the Debtor Agent to the Creditor Agent, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a Debtor account to a

---

<!-- ELEMENT 188 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For and Settlement the Identification has no Payment Clearing (pacs) messages Message exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field could be considered a similar where a contains a 20) comparison pacs message single Transaction. 

**==> picture [60 x 60] intentionally omitted <==**

Each transaction’s _Credit Transfer Transaction Information_ contains a variety of nested _Payment Identification_ elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference) 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 189 -->
**Min 1 – Max 1** 

## The pacs.008 message _**Creation Date**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 190 -->
## **Min 1 – Max 1** 

The pacs.008 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 191 -->
**Min 1 – Max 1** 

The pacs.008 _**Settlement Method**_ element within the Group Header _**Settlement Information**_ , includes one of the embedded codes to indicate how the payment message will be settled. 

The _**Settlement Method** element_ in the pacs.008 allows a choice of an embedded code. 

**==> picture [28 x 28] intentionally omitted <==**

**----- Start of picture text -----**<br>
$<br>€<br>**----- End of picture text -----**<br>


**COVE** indicate this Customer Credit Transfer will be settlement using a covering pacs.009 (COV). The Agents being used in the covering payment to reimburse the Instructed Agent can be provided in the dedicated Reimbursement Agent elements. This allows the Instructed Agent to identify the debit account on their books from the Reimbursement Agent account or look up the account related to the reimbursement agent. 

**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated _**Settlement Account**_ element. 

**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated _**Settlement Account**_ element. 

**==> picture [60 x 47] intentionally omitted <==**

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in

---

<!-- ELEMENT 192 -->
**==> picture [216 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>**----- End of picture text -----**<br>


The pacs messages introduce the _**Settlement Method**_ element within the Group Header _**Settlement Information**_ . Settlement refers to the Agent whose role is to act as an **D** Account Servicing Institution i.e. owns the account and **27** provides service to the customer (Account Owner). 

The Account Owner can be an Agent or another Party. 

Traditionally an interbank account relationship may have been referred to as a Nostro/Vostro relationship or an Agent’s account held on another Agent’s books/ another Agent’s account held on my books. 

Typically the commonality of this can be simplified to the Agent who provides the official Account statement is servicing the account and therefore is the Agent responsible for performing the settlement. 

## **Why is it so important to understand which Agent Services the account ?** 

In ISO 20022, much like the legacy FIN process, each leg of a payment has a settlement component. Commonly one of these settlement legs occurs over a Market Infrastructure, who typically owns or instructs the settlement between the two Market Infrastructure participant Agents at a national Central Bank. In this case the Central Bank services both the Instructing Agent and Instructed Agent accounts which is represented by **CLRG** in the Settlement Method of a pacs message. In a number of business Use Cases there are examples of additional legs, which may occur prior to or after a potential Market Infrastructure, where an Agent is responsible for the role to service an account and perform settlement of that leg.

---

<!-- ELEMENT 193 -->
**==> picture [797 x 350] intentionally omitted <==**

**----- Start of picture text -----**<br>
Your account with me If we simplify a point-to-point message leg and look at when it is settled (booked using<br>traditional language) we can ask ourselves: is the Instructing Agent’s account held<br>D<br>(serviced) on the books of the Instructed Agent or 27 is the Instructing Agent holding<br>A (servicing) the account of the Instructed Agent.<br>Depending on the answer to this question, this determines the Settlement Method in a<br>OR<br>serial payment process.<br>Where the IN structin G A gent services the account and is responsible for settling the<br>B payment leg, the Settlement Method code  INGA  is used.<br>Where the IN structe D A gent services the account and is responsible for settling the<br>My account with you payment leg, the Settlement Method code  INDA  is used.<br>Payment transaction lifecycle<br>pacs.008 pacs.008 pacs.008 pacs.008<br>A B<br>C D<br>INDA CLRG CLRG INGA<br>B C<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 194 -->
The relationship between the settlement of a payment leg and the message process flow is an important one. The state of settlement influences further messages in the process flow. 

The pacs message sent by the Instructing Agent to the Instructed Agent has already been settled. **Instructing Agent** may (for example) send 

**==> picture [116 x 79] intentionally omitted <==**

- a pacs.002 to the Previous Agent with status ACSC Accepted Settlement Complete. 

**INGA** 

- a camt.053 Customer Statement to the Instructed Agent (as Account Owner) 

- **Instructed Agent** can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the Instructed Agent must result in a pacs.004 Payment Return (which in turn triggers a Reverse Indicator on the Account Owners statement). **Creditor Agent** having performed the settlement on the Creditor’s account, camt reporting message may be used to report or notify on this credit entry. 

The pacs message sent by the Instructing Agent to the Instructed Agent has not been settled. **Instructing Agent** may (for example) send 

**INDA** 

- a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress 

- **Instructed Agent** may 

   - Reject the pacs message received, using a pacs.002, as it has not been settled. 

- a camt.053 Customer Statement to the Instructing Agent (as Account Owner) Although an rejected entry will not appear in the camt.053 

- **Creditor Agent** of a pacs.009 (particularly in the cover scenario) may forward the pacs.009 to the Creditor, as the Creditor will perform the settlement (they are the Account Servicing Institution) 

The pacs message sent by the Instructing Agent to the Instructed Agent has not been settled. Settlement is performed by the Market Infrastructure. **Instructing Agent** may (for example) send 

**CLRG** 

- a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress 

- **Instructed Agent** may 

   - can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the Instructed Agent must result in a pacs.004 Payment Return.

---

<!-- ELEMENT 195 -->
**==> picture [823 x 349] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>Settlement Method<br>Settlement Method<br>INDA<br>INGA<br>pacs.008<br>pacs.008<br>Instructing Instructed Agent C is unable to process the<br>Agent: Agent A Agent: Agent B<br>Instructing Instructed payment. As the payment was<br>Agent: Agent B Agent: Agent C already settled by the Instructing<br>Agent (Settlement Method INGA)<br>Agent C must use a pacs.004 to<br>instruct the return of the payment<br>pacs.004<br>pacs.004<br>Return<br>camt.053 camt.053<br>Reason<br>Return<br>Reason Group Header Settlement Information Settlement Method<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 196 -->
**==> picture [732 x 345] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>D<br>Settlement Method<br>Settlement Method<br>INDA Settlement Method<br>INGA<br>pacs.008 INDA<br>pacs.008<br>pacs.008<br>Instructing Instructed<br>Agent: Agent A Agent: Agent B Instructing Instructed<br>Instructing Instructed<br>Agent: Agent B Agent: Agent C<br>Agent: Agent C Agent: Agent D<br>Reject<br>Reason<br>pacs.002<br>pacs.004<br>pacs.004 Agent D is unable to process the<br>Return<br>camt.053 camt.053 Reason<br>Return<br>Reason Agent D must use a pacs.002 to<br>**----- End of picture text -----**<br>


Agent D is unable to process the payment. As the payment has not been settled by themselves Instructed Agent (Settlement Method INDA)

---

<!-- ELEMENT 197 -->
The pacs.008 message _**Settlement Account**_ is a nested element as part of _**Settlement Information,**_ this element identifies information related to an account used to settle the payment instruction. 

**Min 0 – Max 1** The _**Settlement Account**_ identifies the account details maintained at the account institution for the settlement of the instruction as servicing (Agent responsible indicated in the _**Settlement Method**_ ) 

**==> picture [80 x 84] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 198 -->
The a number of Reimbursement as a sub element to _**Settlement**_ pacs message captures Agents _**Information**_ these elements detail the Agent in the cover method who will process the pacs.009 cover. 

These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as The _**Instructing Reimbursement Agent, Instructed Reimbursement Agent**_ and _**Third Reimbursement Agent.**_ Each of these reimbursement agents also has a dedicated account element to optionally capture their related account details. 

## **Min 0 – Max 1** 

**==> picture [71 x 44] intentionally omitted <==**

**----- Start of picture text -----**<br>
$<br>**----- End of picture text -----**<br>


The _**Instructing Reimbursement Agent**_ captures the Agent who will execute a covering payment (i.e. pacs.009 COV or domestic equivalent) often referred to as the currency correspondent. This optional element is comparable with the Field 53a in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Instructing Reimbursement Agent Account**_ captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 53.

---

<!-- ELEMENT 199 -->
**Min 0 – Max 1** 

**==> picture [60 x 60] intentionally omitted <==**

**----- Start of picture text -----**<br>
$<br>€<br>**----- End of picture text -----**<br>


The _**Instructed Reimbursement Agent**_ captures the Agent who will receive the covering payment (i.e., pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer _Instructed Agent_ . This optional element is comparable with the Field 54a in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Instructed Reimbursement Agent Account**_ captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 54. 

**Min 0 – Max 1** 

**==> picture [83 x 63] intentionally omitted <==**

The _**Third Reimbursement Agent**_ captures an additional Agent who will receive the covering payment, where this is not the Agent detailed in the _Instructed Reimbursement Agent_ . This optional element is comparable with the Field 55a in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Third Reimbursement Agent Account**_ captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 55.

---

<!-- ELEMENT 201 -->
**Min 1 – Max 1** 

## The pacs message _**Payment Identification**_ provides a set of elements to identify the payment, of which several are mandatory elements 

**==> picture [158 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Identification<br>**----- End of picture text -----**<br>


**==> picture [89 x 58] intentionally omitted <==**

**----- Start of picture text -----**<br>
$<br>**----- End of picture text -----**<br>


a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender’s Reference (Field 20) of the legacy MT payment message. 

_**Instruction Identification**_ **Min 1 – Max 1** 

an end-to-end reference provided by the _Debtor_ which must be passed unchanged throughout the payment and reported to the Creditor. 

_**End to End Identification**_ **Min 1 – Max 1** 

note: if the Debtor has not provide an end-toend identifier, the _Debtor Agent_ may populate “NOTPROVIDED” to comply the mandatory need of this element. 

**==> picture [36 x 35] intentionally omitted <==**

**==> picture [104 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
UETR<br>Min 1 – Max 1<br>**----- End of picture text -----**<br>


the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their

---

<!-- ELEMENT 202 -->
## **Min 1 – Max 1** The _**Identification** also_ elements pacs message _**Payment**_ provides a set of optional to identify the payment. 

**==> picture [752 x 244] intentionally omitted <==**

**----- Start of picture text -----**<br>
Transaction an end-to-end reference assigned by the first Instructing<br>Identification Agent to identify the transaction.<br>Payment Min 0 – Max 1<br>Identification<br>$ a point-to-point reference populated by a Payment<br>Clearing<br>Market Infrastructure, typically to the settlement leg of a<br>System<br>clearing system transaction as a reference to the settled<br>Reference<br>Min 0 – Max 1 clearing transaction.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 203 -->
**Min 0 – Max 1** 

The pacs message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. 

a choice of imbedded codes representing the _**Instruction**_ urgency considered by _**Priority**_ the Instructing Agent, **Min 0 – Max 1** this point-to-point information may be used by the Instructed Agent to differentiate the processing priority. 

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS 

_**Clearing Channel**_ 

**Min 0 – Max 1** 

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed* service level which should be applied to the payment. 

_**Service Level**_ **Min 0 – Max 3** 

For example, code G001 can be used to identify a gpi Tracked Customer Credit Transfer similarly to Field 111 value 001 in the MT 103 

_Payment Type Information_ i 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order. 

_**Local Instrument**_ **Min 0 – Max 1** 

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

**==> picture [35 x 33] intentionally omitted <==**

**==> picture [87 x 41] intentionally omitted <==**

**----- Start of picture text -----**<br>
Category<br>**----- End of picture text -----**<br>


A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- ELEMENT 204 -->
**£** 

**$** 

¥ 

## The pacs.008 message has two key element to capture the amount of the Credit Transfer, _**Interbank Settlement Amount**_ and _**Interbank Settlement Date**_ 

**Min 1 – Max 1 Min 1 – Max 1** 

_**Interbank Settlement Amount**_ 

A mandated currency amount moved between the _Instructing Agent_ and the _Instructed Agent._ This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A 

**==> picture [44 x 44] intentionally omitted <==**

_**Interbank Settlement Date**_ 

A mandated date on which the _Interbank Settlement_ should be executed between the _Instructing Agent_ and the _Instructed Agent._ This therefore is the value date comparable with the MT Field 32A 

**==> picture [61 x 59] intentionally omitted <==**

Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important one. Instructed Amount relates to the amount Instructed to be executed from the Debtor’s account and only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not

---

<!-- ELEMENT 205 -->
The pacs.008 message has three optional elements to capture the optional information related to the settlement of the instructions. 

**Min 0 – Max 1** 

**==> picture [59 x 55] intentionally omitted <==**

The _**Settlement Priority**_ provides an optional choice of embedded codes to indicate the instruction’s settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the _**Settlement Method**_ and should not be confused with the _**Instruction Priority.**_ 

**==> picture [36 x 35] intentionally omitted <==**

Note: where _**Settlement Method**_ of the pacs.008 is ‘COVE’ (settled via a covering pacs.009 COV) Settlement Priority is relevant to the covering payment not the pacs.008 

**==> picture [59 x 68] intentionally omitted <==**

**Min 0 – Max 1** 

The _**Settlement Time Indication**_ optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure. 

This DateTime can be captured in two nested elements, _**Debit Date Time**_ and _**Credit Date Time**_ . 

**Min 0 – Max 1** 

**==> picture [60 x 65] intentionally omitted <==**

The _**Settlement Time Request**_ optionally captures the time settlement is requested for the payment instruction by the Instructing Agent.  This Time can be capture in four nested elements: 

- _**CLS Time**_ the time the amount must be credit to CLS Bank 

- _**Till Time**_ the time until which the payment may be settled

---

<!-- ELEMENT 206 -->
**$100** 

## **Min 0 – Max 1** 

The _**Instructed Amount**_ captures currency and amount instructed by the Debtor. This conditional element is required when the _**Interbank Settlement Amount**_ is not the same currency and/or amount as originally instructed by the _Debtor._ For example, a charge is taken, or the transactions is converted to another currency. This element is comparable with the legacy Field 33B. 

**==> picture [44 x 44] intentionally omitted <==**

**----- Start of picture text -----**<br>
£<br>**----- End of picture text -----**<br>


**==> picture [44 x 44] intentionally omitted <==**

**----- Start of picture text -----**<br>
¥<br>**----- End of picture text -----**<br>


**Min 0 – Max 1** 

The _**Exchange Rate**_ capture the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency. 

As a best practice to provide consistency and transparency the _Exchange Rate_ used to convert the _Instructed Amount (base currency)_ to the _Interbank Settlement Amount (quote currency)_ should use the Instructed currency as the whole unit to perform the exchange. 

**==> picture [36 x 35] intentionally omitted <==**

For example if _Instructed Amount_ currency is CAD and the Interbank Settlement currency is USD the rate should reflected as 0.83 (CAD 1 equals USD 0.83) 

**==> picture [41 x 21] intentionally omitted <==**

Note: a number of Cross Element Rules exist which relate to the _Instructed_

---

<!-- ELEMENT 207 -->
**Min 1 – Max 1** 

The mandated _**Charge Bearer**_ element uses an embedded code that is used to specify which party/parties would bear associated with the transaction. This element is any charges processing payment comparable with MT Field 71A ‘Details of Charges’ 

||**Code**<br>**Description**<br>CRED<br>Creditor<br>DEBT<br>Debtor<br>SHAR<br>Shared<br>SLEV<br>Service Level|**Code**<br>**Description**<br>CRED<br>Creditor<br>DEBT<br>Debtor<br>SHAR<br>Shared<br>SLEV<br>Service Level||**Code**<br>**Description**<br>BEN<br>Beneficiary<br>OUR<br>Our Customer Charges<br>SHA<br>Shared Charges|**Code**<br>**Description**<br>BEN<br>Beneficiary<br>OUR<br>Our Customer Charges<br>SHA<br>Shared Charges|
|---|---|---|---|---|---|
|**Charge**<br>**Bearer**<br>**(1.1)**|**Code**|**Description**||||
||CRED|Creditor||||
||DEBT|Debtor||||
||||**71A: Details**<br>**of Charges**|**Code**|**Description**|
||SHAR|Shared||||
|||||BEN|Beneficiary|
||SLEV|Service Level||||
|||||OUR|Our Customer Charges|
|||||||
|||||SHA|Shared Charges|
|||||||
|||||||



**==> picture [61 x 63] intentionally omitted <==**

Note: _Charge Bearer_ code SLEV applies following rules agreed as part of a bilateral agreed Service Level or as part of a scheme (commonly used in Instant Payment schemes) This code has no equivalent in legacy MT messages. SLEV is removed from CBPR+ usage guideline specifications for the beginning of the

---

<!-- ELEMENT 208 -->
**Min 1 – Max 1** 

## **Min 0 – Max *** 

The _**Charges Information**_ element provides information on the charges to be paid by the _**Charge Bearer**_ . This element is comparable with MT Fields: 71F ‘Senders Charges’ and 71G ‘Receiver’s Charges’ 

**Charge** Amount **Information** Currenc y **(0.*)** Agent BICFI Name 

Structured Postal Address 

In addition to the legacy MT message the pacs.008 _Charge Information_ mandate the _Agent,_ this represent the Agent for who the Charges are either; due (pre-paid charges) or has taken a charge (deduct from the transaction) 

**==> picture [37 x 35] intentionally omitted <==**

CBPR+ best practice recommends the use of the structured Agent BIC. 

As the _**Charges Information**_ element is repetitive it can capture charges related to previous legs of the payment transaction. 

**==> picture [61 x 63] intentionally omitted <==**

Note: As the _Charge Information_ element has the capability to capture both charges deducted and charges included i.e. pre-paid charges, the use of the _Interbank Settlement Amount_ and _Instructed Amount_ elements play an important role. 

Also note: If Charge Bearer DEBT is provided only one optional occurrence of pre-paid charges is allowed. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 209 -->
## **charges** 

**==> picture [755 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>1 2 3 4<br>Debtor requests a payment for  Debtor Agent executes the USD  Agent B processes the  Agent C processes the<br>USD 100 specifying the  100 payment charging the  payment deducting their fee of  payment deducting their fee of<br>charges should be shared Debtor as commercially agreed.  USD 10  USD 5<br>**----- End of picture text -----**<br>


**==> picture [197 x 85] intentionally omitted <==**

**==> picture [195 x 136] intentionally omitted <==**

**==> picture [196 x 148] intentionally omitted <==**

---

<!-- ELEMENT 210 -->
## **of charges** 

**==> picture [832 x 325] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>1 2 3<br>Debtor requests a  Debtor Agent executes the USD 100  Agent B identifies the pre-payment of<br>payment for USD 100  payment including a previous negotiated  charges by the inclusion of their BIC in the<br>specifying  any charges  pre-payment of charges (USD 30). The  Charge Information Agent element.<br>will be borne by them,  Debtor is debited for USD 100 plus the  Removing charge (USD 30), they forward<br>in accordance with their Charges in accordance with their  the payment to the next Agent. The next<br>banking agreement. account agreement. Agent many request a charge.<br>Pre-payment of<br>charges are identified<br>by the instructed Agent<br>by the inclusion of their<br>BIC in the Charge<br>Information Agent<br>element of the payment<br>message they receive pre-payment of charge versus<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 211 -->
## **of multiple charges** 

**==> picture [837 x 191] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>1 2 3 4<br>Debtor requests a  Debtor Agent executes the USD 100  Agent B identifies the pre-payment of  Agent C identifies the pre-payment of charges<br>payment for USD 100  payment including a previous negotiated  charges by the inclusion of their BIC in the  by the inclusion of their BIC in the Charge<br>specifying  any charges  pre-payment of charges (USD 30). The  Charge Information Agent element.  Information Agent element. Removing this<br>will be taken by them, in  Debtor is debited for USD 100 plus the  Removing charge (USD 30), they forward  pre-payment of charges they forward the<br>accordance with their Charges in accordance with their  the payment, including USD 20 of pre- payment to the Next Agent and indicate they<br>banking agreement. account agreement. payment of charges of the next Agent.  will bear the cost of any charge claims.<br>**----- End of picture text -----**<br>


**==> picture [36 x 34] intentionally omitted <==**

Pre-payment of charges are identified by the instructed Agent by the inclusion of their BIC in the Charge Information Agent element of the payment 

**==> picture [196 x 127] intentionally omitted <==**

**==> picture [197 x 124] intentionally omitted <==**

**==> picture [196 x 84] intentionally omitted <==**

**==> picture [221 x 19] intentionally omitted <==**

---

<!-- ELEMENT 212 -->
## ISO 20022 pacs.008 message standards document **“If ChargesInformation is present, then the currency of ChargesInformation/ChargesAmount is recommended to be the same as the currency of InterbankSettlementAmount”** 

**==> picture [580 x 138] intentionally omitted <==**

**----- Start of picture text -----**<br>
Interbank Settlement  Interbank Settlement  Currency of Charge<br>Amount received Amount forwarded Information (where a<br>charge occurs)<br>USD USD USD<br>USD EUR EUR<br>**----- End of picture text -----**<br>


**==> picture [62 x 62] intentionally omitted <==**

ISO 20022 does not prevent Charges from being booked in a different currency, but for transparency the Charge should be represented within the Charge Information in the Interbank Settlement Amount Currency. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 213 -->
## **charges** 

**==> picture [738 x 315] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>1 2 3<br>Debtor requests a payment for GBP Debtor Agent executes a payment for  Agent B processes the payment<br>100 to be initiated from their USD  GBP 95 (GBP 100 minus a 5 GBP charge  deducting their fee of GBP 10<br>account, specifying the charges should  deducted as this is borne by the Creditor.<br>be borne by the Creditor<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 214 -->
The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent. 

**Min 0 – Max 1** 

**==> picture [63 x 66] intentionally omitted <==**

**==> picture [63 x 65] intentionally omitted <==**

The _**Previous Instructing Agent 1**_ captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Previous Instructing 1 Account**_ captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message 

**Min 0 – Max 1** 

The _**Previous Instructing 2**_ captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message. 

**Min 0 – Max 1** 

**==> picture [63 x 65] intentionally omitted <==**

**==> picture [52 x 57] intentionally omitted <==**

The _**Previous Instructing 2 Account**_ captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** The _**Previous Instructing 3**_ captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message. **Min 0 – Max 1**

---

<!-- ELEMENT 215 -->
**==> picture [645 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.008<br>Instructing Instructed pacs.008 Instructing Agent<br>Agent: Agent A Agent: Agent B<br>Instructing Instructed<br>Agent: Agent B Agent: Agent C<br>**----- End of picture text -----**<br>


**==> picture [61 x 61] intentionally omitted <==**

_**Instructing Agent**_ and _**Instructed Agent**_ represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment leg. 

**==> picture [47 x 48] intentionally omitted <==**

_Instructing Agent_ and _Instructed Agent_ elements are required in all pacs messages and are only available in the _**Credit Transfer Information**_ 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 216 -->
## **Intermediary Agents** 

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. _**Intermediary Agent**_ is an example of this, where these agents are classified in numeric order (i.e. _Intermediary Agent 1_ ) _**Previous Instructing Agent**_ however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment. 

. The below diagram visualizes the change of Agent role at different stages of the payment transaction life cycle 

**==> picture [802 x 240] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E<br>Debtor Instructing Agent &  Instructed Agent Intermediary Agent 1 Intermediary Agent 2 Creditor Agent Creditor<br>Debtor Agent<br>Debtor Debtor Agent Instructing Agent  Instructed Agent Intermediary Agent 1 Creditor Agent Creditor<br>Debtor Debtor Agent Previous Instructing  Instructing Agent  Instructed Agent Creditor Agent Creditor<br>Agent 1<br>Debtor Debtor Agent Previous Instructing  Previous Instructing  Instructing Agent Creditor Agent &  Creditor<br>Agent 1 Agent 2 Instructed Agent<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 217 -->
The can to 3 which a role in the pacs message capture up Intermediary Agents, play dynamic payment between the Debtor Agent and Creditor Agent. 

**Min 0 – Max 1** 

**==> picture [61 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 1**_ captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 1 Account**_ captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a. 

## **Min 0 – Max 1** 

**2** 

**==> picture [51 x 37] intentionally omitted <==**

The _**Intermediary Agent 2**_ captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 2 Account**_ captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

**==> picture [62 x 53] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 3**_ captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. **Min 0 – Max 1**

---

<!-- ELEMENT 218 -->
## **authority to instruct payment from their Headquarter (HQ) settlement account.** 

Usually a serial payment is instructed through each Agent in a serial process. In some circumstances a branch of an Institution (Agent A) may be given Debit Authority to instruct payment from their Headquarters (Agent HQ) account with its currency correspondent (Agent B). In much the same way as if this had occurred serially, it is important that the payment instructed by Agent B correctly reflect Agent HQ as an Agent participating in the transaction, particularly if the payment is returned. 

**==> picture [667 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>A<br>HQ 1 2<br>Debtor Agent executes the  Agent B processes the payment debiting the<br>payment using their Headquarters  account of Agent A Headquarters, and including<br>as the settlement account them as the Previous Instructing Agent in the<br>purpose Agent C (in payment transaction.<br>has a responsibility to Interbank Settlement Amount USD 100<br>associated with the Interbank Settlement  USD 100<br>Amount<br>is captured in the Settlement Account Id 12345<br>leg as a Previous Settlement Account 12345<br>This also ensures, Debtor Agent AAAAGB2LABC<br>Return occur, all Debtor Agent AAAAGB2LABC<br>**----- End of picture text -----**<br>


**==> picture [116 x 61] intentionally omitted <==**

For transparency purpose Agent C (in this use case) has a responsibility to ensure the Agent associated with the Settlement Account is captured in the next payment leg as a Previous Instructing Agent. This also ensures, should a Payment Return occur, all 

**==> picture [48 x 44] intentionally omitted <==**

---

<!-- ELEMENT 219 -->
The pacs.008 message introduces ultimate parties to the FI to FI Customer Credit Transfer message. The _**Ultimate Debtor**_ element should not be confused with an _**Initiating Party**_ who may send a payment initiation request on behalf of the Debtor. (see dedication section on _Initiating Party_ ) 

**==> picture [257 x 175] intentionally omitted <==**

**----- Start of picture text -----**<br>
Ultimate<br>Party<br>Ultimate Ultimate<br>Debtor Creditor<br>**----- End of picture text -----**<br>


**Min 0 – Max 1** 

➢ CBPR+ premise is that an _**Ultimate Debtor**_ has no financial regulated direct account relationship with the corresponding _Debtor_ . **Min 0 – Max 1** ➢ CBPR+ premise is that an _**Ultimate Creditor**_ has no financial regulated direct account relationship with the corresponding _Creditor_ . 

An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor depending on the payment scenario) 

**==> picture [42 x 7] intentionally omitted <==**

_Credit Transfer Transaction Information_ Ultimate Creditor

---

<!-- ELEMENT 220 -->
## **Debtor** 

An individual walks into a Money Transfer Bureau with relevant Private Identification (e.g. a passport) and requests a payment to be paid on their behalf to a Creditor. Having accepted payment for the transaction, the Money Transfer Bureau executes a payment initiation request to their Agent (Bank) as the Debtor, on behalf of the individual who is represented as the Ultimate Debtor. 

**==> picture [825 x 251] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>1 3<br>Ultimate Debtor requests a<br>Debtor Agent (A) initiates a<br>payment to be initiated on their<br>serial payment towards the<br>behalf to the Creditor<br>Creditor Agent (D) using<br>Agents B & C as intermediaries<br>2<br>Debtor requests a payment to<br>be initiated on behalf of the<br>Ultimate Debtor to the Creditor<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 221 -->
## **Creditor** 

A payments is initiated to credit a retirement care facility to pay the fees of one of its residents. The retirement facility is the Creditor of the payment transaction, whereby the resident of the facility is represented as the Ultimate Creditor (beneficiary of the services the fee is paying for) 

**==> picture [820 x 268] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>1 2<br>Debtor initiates a payment<br>Debtor Agent (A) initiates a<br>instruction to the Debtor Agent<br>serial payment towards the<br>Creditor Agent (D) using<br>Agents B & C as intermediaries<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 222 -->
**==> picture [215 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initiating Party<br>Debtor Third Party<br>A<br>Debtor Agent<br>**----- End of picture text -----**<br>


**Min 0 – Max 1** 

**Min 1 – Max 1** 

The _**Initiating Party**_ of a payment is often the _**Debtor**_ themselves and therefore this optional element is not necessary. More often the _Initiating Party_ is a third party providing payment initiation services on behalf of the _Debtor_ (often referred to as a Third Party Provider) whereby the _Debtor_ maintains an account with the Debtor Agent but the Third Party Provider has authority to initiate payment on behalf of the _Debtor_ . This is distinctly different from an Ultimate Party (such as _Ultimate Debtor_ ) who instructs the _Debtor_ to initiate a payment on their behalf. 

**==> picture [61 x 62] intentionally omitted <==**

In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the _Initiating Party_ is often the _Creditor_ , however the same context of a Third Party Provider can exist where the third party is responsible for collecting funds on behalf of the _Creditor_ . 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 223 -->
Mandatory _**Name**_ (where a BIC identifier is not provided) by which the party is known 

The ISO 20022 pacs messages describe the party debited for a transaction as the _**Debtor**_ . The _Debtor_ sub elements describe the _Debtor_ in greater detail. 

_**Name**_ 

**==> picture [213 x 295] intentionally omitted <==**

**==> picture [272 x 192] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Debtor<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Debtor_ address details 

**==> picture [92 x 90] intentionally omitted <==**

**----- Start of picture text -----**<br>
Identification<br>**----- End of picture text -----**<br>


Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

Optional element to _**Country of**_ capture the Debtor’s ISO _**Residence**_

---

<!-- ELEMENT 224 -->
**Min 0 – Max 1** The pacs.008 _**Debtor Account**_ is used to capture the account information for which debit entry is/has been applied to the Debtor’s account, which are also reflected in their account Statement. 

The _**Debtor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 225 -->
||||||||||
|---|---|---|---|---|---|---|---|---|
|**ISO 20022 Debtor data**||**element example**||||**Customer data record**<br>**example**||**MT – free format option**|
|Debtor|Name|||||JOHN HECTOR<br>JOSEPH SMITH -<br>MASTERSONS||:50K:/BE3000121637141<br>JOHN HECTOR JOSEPH SMITH - MASTERSO<br>HOOGSTRAAT 6BRUSSELS<br>1000BELGIUM<br>PASSPORT1111111111|
||Postal<br>Address|Department|||||||
|||Sub Department|||||||
|||Street Name||||HOOGSTRAAT|||
|||Building Number||||6|||
||||||||||
|||Post Code||||1000||**MT – structured option with risk of potential truncation & loss of info**|
|||Town Name||||BRUSSELS||:50F:/BE3000121637141<br>1/JOHN HECTOR JOSEPH SMITH - MASTER<br>1/SONS<br>2/HOOGSTRAAT 6<br>3/BE/BRUSSELS<br>1000|
|||Country||||BE|||
||Identification|Private<br>Id|Other|Id||1111111111|||
|||||Scheme<br>Name|Code|CCPT|||
|Debtor<br>Account|Identification|IBAN||||BE3000121637141|||
||||||||||

---

<!-- ELEMENT 226 -->
**Min 1 – Max 1 Min 1 – Max 1** The _**Debtor Agent**_ and _**Creditor Agent**_ are static roles in the pacs.008 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the _Debtor_ and _Creditor_ . 

**==> picture [61 x 62] intentionally omitted <==**

**==> picture [80 x 136] intentionally omitted <==**

**==> picture [84 x 137] intentionally omitted <==**

Note: Although the _**Debtor Agent, Creditor Agent, Debtor and Creditor**_ all maintain static roles in the pacs messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 227 -->
## **Account** 

## **Min 0 – Max 1** 

The pacs.008 _**Debtor Agent Account**_ and _**Creditor Agent Account**_ are used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction. 

The _**Debtor Agent Account**_ and _**Creditor Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Account Servicing Institution _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing **Min 0 – Max 1** Institution 

_**Proxy**_ captures an alternative identification of the account number such as an email **Min 0 – Max 1** address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 21] intentionally omitted <==**

---

<!-- ELEMENT 228 -->
Mandatory _**Name**_ (where a BIC identifier is not provided) by which the party is known 

The ISO 20022 pacs messages describe the party credited for a transaction as the _**Creditor**_ . The _Creditor_ sub elements describe the _Creditor_ in greater detail. 

_**Name**_ 

**==> picture [198 x 295] intentionally omitted <==**

**==> picture [279 x 211] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Creditor<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Creditor_ address details 

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

Optional element to _**Country of**_ capture the Creditor’s ISO _**Residence**_

---

<!-- ELEMENT 229 -->
**Min 0 – Max 1** The pacs.009 _**Creditor Account**_ is used to capture the account information for which a credit entry is intended to be applied to the Creditor’s account, which are also reflected in their account Statement. 

The _**Creditor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

- **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 230 -->
## **Account** 

## **Min 0 – Max 1** 

The pacs.008 _**Debtor Agent Account**_ and _**Creditor Agent Account**_ are used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction. 

The _**Debtor Agent Account**_ and _**Creditor Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Account Servicing Institution _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing **Min 0 – Max 1** Institution 

_**Proxy**_ captures an alternative identification of the account number such as an email **Min 0 – Max 1** address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 21] intentionally omitted <==**

---

<!-- ELEMENT 231 -->
The _**Instruction for Next Agent**_ and _**Instruction for Creditor Agent**_ elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents. 

**Min 0 – Max 2** 

**==> picture [52 x 55] intentionally omitted <==**

The _**Instruction for Creditor Agent**_ element offers a multiplicity of up to 2 occurrences of information. This element enables: 

➢ the use of 2 embedded codes to describe the instruction 

➢ free format _instruction information_ 

➢ or both, where the free format complements the code. 

The use of this element may be bilaterally agreed with the _Creditor Agent_ . It must be passed . on throughout the life cycle of the transaction until the payment reaches the _Credit Agent_ 

**Min 0 – Max 6** 

**==> picture [51 x 56] intentionally omitted <==**

The _**Instruction for Next Agent**_ element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format _instruction information_ in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent) 

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 232 -->
## **Min 0 – Max 1** 

The _**Purpose**_ element within the pacs.008 FI to FI Customer Credit Transfer captures the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code. The purpose is used to capture the nature of the payment e.g. IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Debtor. 

**==> picture [123 x 91] intentionally omitted <==**

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. 

For example: GDSV is classified within the Commercial categorisation, with the _Name_ Purchase Sale of Goods and Services described as a Transaction is related to purchase and sale of goods. 

**==> picture [61 x 62] intentionally omitted <==**

_Category Purpose_ also captures a high level purpose, which unlike _Purpose_ is less granular but can trigger special processing e.g. Category Purpose code SALA ‘Salary Payment’ may trigger a reporting process which restricts sensitive data i.e., individual salary names. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 233 -->
**Min 0 – Max 10** The _**Regulatory Reporting**_ element within the pacs.008 FI to FI Customer Credit Transfer is nested to capture regulatory and statutory information needed to report to the appropriate authority/s. 

**Min 0 – Max 1** 

**==> picture [118 x 73] intentionally omitted <==**

- The _**Debit Credit Reporting Indicator**_ utilises an embedded choice of code to indicate whether the regulatory reporting information applies to the: • DEBT (debit) 

- • CRED (credit) or 

- • BOTH 

**Min 0 – Max 1** 

- The _**Authority**_ element captures the _**Name**_ and _**Country**_ code of the Authority/Entity requiring the regulatory reporting information. 

**Min 0 – Max *** 

The _**Details**_ element provides the detail on the regulatory reporting information. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information     Regulatory Reporting_

---

<!-- ELEMENT 234 -->
## **Min 0 – Max 1** 

The _**Related Remittance Information**_ element within the pacs.008 FI to FI Customer Credit Transfer is nested to provide information related to the handling of remittance information. This information is typically provided by the Debtor in the payment initiation request. 

**Min 0 – Max 1** The _**Remittance Identification**_ captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction. 

**Min 0 – Max 2** 

**==> picture [92 x 83] intentionally omitted <==**

- The _**Remittance Location Details**_ uses a set of nested elements to provide information on either the location of or the delivery of remittance information. 

   - _**Method**_ requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email) 

   - _**Electronic Address**_ provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved. 

   - _**Postal Address**_ provides the postal address to which an agent is to send the remittance information 

**==> picture [53 x 49] intentionally omitted <==**

Remittance advices are typically considered as a traditional value added service provided by the Debtor Agent to the Debtor, in order to provide _Remittance Information_ to the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting messages. 

_**Remittance Information**_ is a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022. _Related Remittance Information_ and _Remittance Information_ are mutually exclusive (can’t both be present)

---

<!-- ELEMENT 235 -->
The optional _**Remittance Information**_ element within the pacs.008 FI to FI Customer Credit Transfer is nested to provide either _**Structured**_ or _**Unstructured**_ information related to payment, such as invoices. 

**Min 0 – Max 1** 

_**Remittance Information**_ enable the matching/reconciliation of an entry that the payment is intended to settle 

**==> picture [66 x 73] intentionally omitted <==**

**Min 0 – Max 1** 

The **Unstructured** sub element captures free format _Remittance Information_ which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence. 

**Min 0 – Max *** The **Structured** element is nested capturing rich structured _Remittance Information,_ and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification) The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-to-end transportation of this data. 

**==> picture [53 x 31] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [12 x 7] intentionally omitted <==**

_Related Remittance Information_ and _Remittance Information_ are

---

<!-- ELEMENT 236 -->
The bilaterally/multilaterally agreed _**Remittance Information**_ which is _**Structured**_ must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information. 

**==> picture [457 x 131] intentionally omitted <==**

## example of _Structured_ invoice information 

The _**Creditor Remittance Information**_ is provided to the _**Creditor**_ in the Cash Management Reporting messages’ Remittance Information component, for example, the camt.053 Bank to Customer Statement. 

**Structured** <Strd> xml tag In this example Referred Document **Reference Document** <Rf rdDocInf> Information and it nested elements has **Information** multiplicity which support up to 9,000 **Type** <Tp> business character of information. Whereby this element names **Code Or Proprietary** <CdOrPrtry > information element can be repeated to include more **Code** <Cd> **CINV** coded information such as another invoice. **Number** <Nb> **A0000101 Related Date** <Dt> **2019-10-29** 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_ Remittance Information

---

<!-- ELEMENT 237 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

## **Serial Financial Institution to Financial Institution to Customer Credit Transfer** 

Use Case p.8.1.1 – High Level FI to FI Customer Credit Transfer (pacs.008) settled over a Payment Market Infrastructure Use Case p.8.1.2 – High Level FI to FI Customer Credit Transfer (pacs.008) Sweeps (Short position at the Secondary Account) **Cover Method Financial Institution to Financial Institution to Customer Credit Transfer** 

Use Case p.8.2.1 - High Level FI to FI Customer Credit Transfer settled using the cover method (pacs.009 COV) over a Payment Market Infrastructure 

Use Case p.8.2.2 - High Level FI to FI Customer Credit Transfer involved a serial leg into a cover method (pacs.009 COV) Use Case p.8.2.3 - High Level FI to FI Customer Credit Transfer involved a serial leg in and out of a cover method (pacs.009 COV) Use Case p.8.2.4 - High Level FI to FI Customer Credit Transfer involved a serial leg out of a cover method (pacs.009 COV)

---

<!-- ELEMENT 238 -->
## **Market Infrastructure** 

**==> picture [813 x 310] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5 6<br>pacs.008 pacs.008 pacs.008 pacs.008<br>A C<br>pacs.002 B pacs.002 pacs.002 D<br>Settlement<br>Complete<br>1 3 5<br>Agent B processes the payment<br>Debtor initiates a payment  Agent C processes the payment<br>on Agent C, via the Payment<br>instruction to the Debtor Agent. onto Agent D.<br>Market Infrastructure.<br>2<br>6<br>Debtor Agent (A) initiates a  4<br>serial payment towards the  Payment Market Infrastructure,  Agent D credits the account of the<br>Creditor Agent (D) using  settles the payment between Agent  Creditor, and may optionally<br>Agents B & C as  B and Agent C as direct  provide a notification e.g. credit<br>intermediaries, who are direct  participants of the Market  notification in addition to an<br>participants of the Payment Infrastructure and provides a t t t t ( t 053)<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 239 -->
## **Authorised Party** 

**==> picture [778 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
Debit<br>DA<br>Authorisation 3 4<br>2<br>Interbank pain.001 pacs.008<br>camt.053<br>I Interbank pain.002 A pacs.002 B<br>3a<br>DA 3 4<br>As a pre-requisite the Debtor<br>Debtor Agent (A) debits the account of  Creditor Agent (B) receives the credit<br>provides Debit Authorisation to<br>Agent I to Initiate Payment from  Debtor and initiates a credit transfer transfer message, credits the Creditor, and<br>sends a camt.053 (statement) at the end of<br>their account with the Debtor<br>the business day to the Creditor. An optional<br>Agent (A)<br>status report is sent to the previous Agent<br>based upon a bilateral agreement<br>2 3a<br>Agent (I) initiates a payment<br>Debtor Agent (A) optionally provides a<br>request (pain.001) to the Debtor<br>status update to the Initiating Party<br>Agent (A) to move fund from the  See use case pn.1.2.1 for an Authorised Party<br>(Agent I), based upon a bilateral<br>Debtor’s account, as an  Payment.<br>agreement<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 240 -->
**==> picture [851 x 376] intentionally omitted <==**

**----- Start of picture text -----**<br>
(pacs.009 COV) over a Payment Market Infrastructure<br>7<br>1 2a<br>pacs.008<br>A pacs.002 D<br>2b<br>6<br>1 3 4 5<br>Debtor initiates a payment<br>pacs.009 cov pacs.009 cov<br>instruction to the Debtor Agent 6<br>B pacs.002 C Agent C produces an end of day<br>account statement report. An<br>2a<br>optional real time notification e.g.<br>Debtor Agent (A) initiates a  Settlement  4 advice of credit may have also been<br>payment using the cover method  Complete Payment Market Infrastructure,  created at the time of the credit<br>settles the payment between Agent<br>to the Creditor Agent (D) posting<br>B and Agent C as direct<br>participants of the Market<br>2b Infrastructure, and provides a  7<br>settlement confirmation to Agent B<br>In parallel the Debtor Agent (A)  Agent D reconciles the covering<br>3<br>initiates a covering payment to  funds and credits the account of the<br>credit the account of Agent (D)  Agent B processes the payment  5 Creditor, and may optionally<br>with their correspondent (Agent  on Agent C, via the Payment  Agent C receives the payment and  provide a notification e.g. credit<br>C) Market Infrastructure credits the account of Agent D notification<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 241 -->
**==> picture [851 x 376] intentionally omitted <==**

**----- Start of picture text -----**<br>
method (pacs.009 COV)<br>4<br>1 2 3a<br>pacs.008<br>pacs.008<br>A B pacs.002 E<br>pacs.002<br>3b<br>6<br>5<br>1<br>Debtor initiates a payment<br>pacs.009 cov<br>instruction to the Debtor Agent 5<br>pacs.002 Agent C processes the payment on<br>C D<br>Agent D, using a correspondent<br>2<br>banking business relationship<br>Debtor Agent (A) initiates a<br>payment using the serial method<br>towards the Creditor Agent (E) 4<br>6<br>Agent E receives the payment  Agent D receives the payment and<br>3a 3b instruction and credits the account of  credits the account of Agent E.<br>the Creditor, and may optionally  Agent D produces an end of day<br>Agent B initiates a payment<br>In parallel the Agent (B) initiates a  provide a notification e.g. credit  account statement report. An<br>using the cover method towards<br>the Creditor Agent (E) by  covering payment to credit the account  notification. Alternatively, they may  optional real time notification e.g.<br>sending a direct pacs.008 to  of Agent (E) with their correspondent  have chosen to await until settlement  advice of credit may have also been<br>(Agent D) occurred in Step 6 based upon their  created at the time of the credit<br>Agent E who they have business<br>relationship with risk appetite. posting<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 242 -->
**==> picture [851 x 377] intentionally omitted <==**

**----- Start of picture text -----**<br>
of a cover method (pacs.009 COV)<br>4<br>7<br>1 2 3a<br>pacs.008 pacs.008<br>pacs.008<br>A pacs.002 B pacs.002 E pacs.002 F<br>3b<br>6<br>5<br>6<br>1<br>pacs.009 cov Agent D receives the payment and<br>Debtor initiates a payment  credits the account of Agent E.<br>instruction to the Debtor Agent Agent D produces an end of day<br>pacs.002<br>C D<br>account statement report. An<br>3a 4 optional real time notification e.g.<br>2 Agent B initiates a payment using  Agent E receives the payment  advice of credit may have also been<br>the cover method towards the  instruction and process the payment  created at the time of the credit<br>Debtor Agent (A) initiates a<br>payment using the serial method  Creditor Agent (F) by sending a  on to Agent F. Alternatively they may  posting<br>towards the Creditor Agent (F) direct pacs.008 to Agent E who they  have chosen to await until settlement<br>have business relationship with. occurred in Step 6 based upon their<br>risk appetite.<br>7<br>3b Agent F receives the payment and<br>5<br>In parallel the Agent (B) initiates a  credits the account of the Creditor,<br>Agent C processes the payment on<br>covering payment to credit the account  and may optionally provide a<br>Agent D, using a correspondent<br>of Agent (E) with their correspondent  notification e.g. credit notification.<br>banking business relationship<br>(A t D)<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 243 -->
**==> picture [851 x 374] intentionally omitted <==**

**----- Start of picture text -----**<br>
cover method (pacs.009 COV)<br>3<br>4<br>1 2a<br>pacs.008 pacs.008<br>A pacs.002 D pacs.002 E<br>2b<br>6<br>5<br>pacs.009 cov<br>B pacs.002 C<br>1<br>2b 4 6<br>Debtor initiates a payment  In parallel the Agent (A) initiates a  Agent E receives the payment and  Agent C receives the payment and<br>instruction to the Debtor Agent covering payment to credit the account  credits the account of the Creditor,  credits the account of Agent D.<br>of Agent (D) with their correspondent  and may optionally provide a  Agent C produces an end of day<br>(Agent C) notification e.g. credit notification. account statement report. An<br>2a optional real time notification e.g.<br>advice of credit may have also been<br>Debtor Agent (A) initiates a  3<br>Agent D receives the payment  created at the time of the credit<br>payment using the cover<br>method towards the Creditor  instruction and process the payment  5 posting<br>on to Agent E. Alternatively they may<br>Agent (E) by sending a direct  Agent B processes the payment on<br>have chosen to await until settlement<br>pacs.008 to Agent D who they  Agent C, using a correspondent<br>have business relationship with occurred in Step 6 based upon their  banking business relationship<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 244 -->
# **Financial Institution to Financial Institution Customer Credit Transfer** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 245 -->
## The pacs.008 STP has two core sets of nested elements: 

**pacs.008** 

**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


Credit Transfer Transaction Information 

**==> picture [60 x 60] intentionally omitted <==**

- _**Group Header**_ which contains a set of characteristics that relates to all individual transaction 

- _**Credit Transfer Transaction Information**_ which contains elements providing information specific to the individual credit transfer transaction. 

Payment messages in a many-to-many payment are considered as a single transaction. The pacs.008 STP is a message who’s Usage Guideline has been further restricted by remove elements considered

---

<!-- ELEMENT 246 -->
**==> picture [748 x 223] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.008 STP<br>pacs.002<br>pacs.008 STP<br>pacs.008 STP<br>pacs.002<br>pacs.002<br>**----- End of picture text -----**<br>


The Financial Institution To Financial Institution Customer Credit Transfer message is sent by the Debtor Agent to the Creditor Agent, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a Debtor account to a

---

<!-- ELEMENT 247 -->
The pacs.008 STP message has enhance STP feature over and above the pacs.008 and legacy MT 103 STP. At a high level the key difference between the pacs.008 and pacs.008 STP are summarized. 

**==> picture [743 x 303] intentionally omitted <==**

**----- Start of picture text -----**<br>
STP<br>pacs.008 pacs.008<br>Business Application Header<br>Business Service swift.cbprplus.02 swift.cbprplus.stp.02<br>Credit Transfer Transaction Information<br>Previous Instructing Agent 1<br>Previous Instructing Agent 2 Financial Institution identifiers: Financial Institution identifiers:<br>Previous Instructing Agent 3 • BIC • BIC<br>• •<br>Intermediary Agent 1 Clearing System Member Id Clearing System Member Id<br>Intermediary Agent 2 • LEI • LEI<br>Intermediary Agent 3 • Name Name removed<br>Debtor Agent • Postal Address Postal Address removed<br>Creditor Agent<br>Debtor  Addition Debtor and Creditor<br>Creditor IBAN rules<br>Creditor Account Account optional Account mandatory<br>Instruction for Next Agent Instruction for Next Agent  removed<br>Elements optional<br>Instruction for Creditor Agent Instruction for Creditor Agent  removed<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 248 -->
# **Financial Institution Credit Transfer** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 249 -->
**==> picture [137 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009<br>**----- End of picture text -----**<br>


**==> picture [110 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


Credit Transfer Transaction Information 

**==> picture [135 x 68] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 (COV)<br>**----- End of picture text -----**<br>


Group Header 

Credit Transfer Transaction Information 

Underlying Customer Credit Transfer 

## The pacs.009 has two main use cases: 

- as a core Financial Institution Credit Transfer message. 

- As a **COV** where it is used as cover of (to settle) a pacs.008. 

The pacs.009 therefore contain information of the underlying Customer Credit Transfer (pacs.008) for use in the cover scenario, which is the key attribute to differentiate between these two use cases. 

The pacs.009 may also be used as a **ADV** where it is sent as an advice and is settled using the pacs.009 as a core message.

---

<!-- ELEMENT 250 -->
**==> picture [583 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.009<br>pacs.002<br>pacs.009<br>pacs.002 camt.053<br>**----- End of picture text -----**<br>


The Financial Institution Credit Transfer message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are **Financial Institutions** .

---

<!-- ELEMENT 252 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender’s Reference (Field could be considered a similar where a contains a 20) comparison pacs message single Transaction. 

**==> picture [60 x 60] intentionally omitted <==**

Each transaction’s _Credit Transfer Transaction Information_ contains a variety of nested _Payment Identification_ elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference) 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 253 -->
**Min 1 – Max 1** 

## The pacs.009 message _**Creation Date**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 254 -->
## **Min 1 – Max 1** 

The pacs.009 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 255 -->
## **Min 1 – Max 1** 

The pacs.009 _**Settlement Method**_ element within the Group Header _**Settlement Information**_ , includes one of the embedded codes to indicate how the payment message will be settled. 

The _**Settlement Method** element_ in the pacs.009 allows a choice of an embedded code. 

**==> picture [28 x 28] intentionally omitted <==**

**----- Start of picture text -----**<br>
$<br>€<br>**----- End of picture text -----**<br>


**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated _**Settlement Account**_ element. 

**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated _**Settlement Account**_ element. 

**==> picture [60 x 47] intentionally omitted <==**

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in

---

<!-- ELEMENT 256 -->
The pacs.009 message _**Settlement Account**_ is a nested element as part of _**Settlement Information,**_ this element identifies information related to an account used to settle the payment instruction. 

**Min 0 – Max 1** The _**Settlement Account**_ identifies the account details maintained at the account institution for the settlement of the instruction as servicing (Agent responsible indicated in the _**Settlement Method**_ ) 

**==> picture [80 x 84] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 258 -->
**Min 1 – Max 1** 

## The pacs message _**Payment Identification**_ provides a set of elements to identify the payment, of which several are mandatory elements 

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender’s Reference (Field 20) of the legacy MT payment message. 

_**Instruction Identification**_ **Min 1 – Max 1** 

an end-to-end reference provided by the _Debtor_ which must be passed unchanged throughout the payment and reported to the Creditor. 

**==> picture [158 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Identification<br>**----- End of picture text -----**<br>


note: for a pacs.009 COV the end-to-end id is provided by the Debtor from the pacs.008 Instruction id. In a pacs.009 COR if the Debtor has not provide an end-to-end identifier, the _Debtor Agent_ may populate “NOTPROVIDED” to comply the mandatory need of this element. 

_**End to End Identification**_ 

**==> picture [35 x 35] intentionally omitted <==**

**Min 1 – Max 1 $** 

the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their 

**==> picture [54 x 22] intentionally omitted <==**

**----- Start of picture text -----**<br>
UETR<br>**----- End of picture text -----**<br>


**==> picture [61 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 259 -->
## **Min 1 – Max 1** The _**Identification** also_ elements pacs message _**Payment**_ provides a set of optional to identify the payment. 

**==> picture [752 x 244] intentionally omitted <==**

**----- Start of picture text -----**<br>
Transaction an end-to-end reference assigned by the first Instructing<br>Identification Agent to identify the transaction.<br>Payment Min 0 – Max 1<br>Identification<br>$ a point-to-point reference populated by a Payment<br>Clearing<br>Market Infrastructure, typically to the settlement leg of a<br>System<br>clearing system transaction as a reference to the settled<br>Reference<br>clearing transaction.<br>Min 0 – Max 1<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 260 -->
**Min 0 – Max 1** 

The pacs message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. 

a choice of imbedded codes representing the urgency considered by the Instructing Agent, **Min 0 –** this point-to-point information may be used by the Instructed Agent to differentiate the processing priority. 

_**Instruction Priority**_ **Min 0 – Max 1** 

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS 

_**Clearing Channel**_ 

**Min 0 – Max 1** 

A nested element which may either use an external ISO Service Level code* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. 

_**Service Level**_ **Min 0 – Max 3** 

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV 

_Payment Type Information_ 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order. 

_**Local Instrument**_ **Min 0 – Max 1** 

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

i 

**==> picture [35 x 33] intentionally omitted <==**

**==> picture [87 x 41] intentionally omitted <==**

**----- Start of picture text -----**<br>
Category<br>**----- End of picture text -----**<br>


A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- ELEMENT 261 -->
**£** 

**$** 

¥ 

## The pacs.009 message (unlike the pacs.008) has only one element to capture the amount of the Credit Transfer, _**Interbank Settlement Amount**_ . 

**Min 1 – Max 1** 

A mandated currency amount moved between the _Instructing Agent_ and the _Instructed Agent._ _**Interbank**_ This therefore is the point-to-point currency amount exchanged, comparable with the MT Field _**Settlement**_ 32A _**Amount**_ 

**Min 1 – Max 1** 

**==> picture [44 x 44] intentionally omitted <==**

_**Interbank Settlement Date**_ 

A mandated date on which the _Interbank Settlement_ should be executed between the _Instructing Agent_ and the _Instructed Agent._ This therefore is the value date comparable with the MT Field 32A 

**==> picture [63 x 62] intentionally omitted <==**

Note: the Financial Institution Credit Transfer (pacs.009) has no _Instructed Amount_ element, _Exchange Rate_ or _Charger Bearer_ (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain

---

<!-- ELEMENT 262 -->
## **Request** 

The pacs.009 message has three optional elements to capture the optional information related to the settlement of the instructions. 

## **Min 0 – Max 1** 

**==> picture [59 x 55] intentionally omitted <==**

**==> picture [59 x 68] intentionally omitted <==**

The _**Settlement Priority**_ provides an optional choice of embedded codes to indicate the instruction’s settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the _**Settlement Method**_ and should not be confused with the _**Instruction Priority.**_ 

Note: Where the _**Settlement Method**_ of the pacs.009 is ‘INDA’ (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code ‘INGA’ implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary. **Min 0 – Max 1** 

**==> picture [36 x 35] intentionally omitted <==**

The _**Settlement Time Indication**_ optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure. 

This DateTime can be captured in two nested elements, _**Debit Date Time**_ and _**Credit Date Time**_ . 

## **Min 0 – Max 1** 

**==> picture [60 x 65] intentionally omitted <==**

The _**Settlement Time Request**_ optionally captures the time settlement is requested for the payment instruction by the Instructing Agent.  This Time can be capture in four nested elements: 

- _**CLS Time**_ the time the amount must be credit to CLS Bank 

- _**Till Time**_ the time until which the payment may be settled

---

<!-- ELEMENT 263 -->
The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent. 

**Min 0 – Max 1** 

**==> picture [63 x 66] intentionally omitted <==**

**==> picture [63 x 65] intentionally omitted <==**

**==> picture [61 x 63] intentionally omitted <==**

The _**Previous Instructing Agent 1**_ captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Previous Instructing Agent 1 Account**_ captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message 

**Min 0 – Max 1** 

The _**Previous Instructing Agent 2**_ captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message. **Min 0 – Max 1** The _**Previous Instructing Agent 2 Account**_ captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** The _**Previous Instructing Agent 3**_ captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message. **Min 0 – Max 1** The _**Previous Instructing Agent 3 Account**_ captured the account related between this Agent and Previous

---

<!-- ELEMENT 264 -->
**==> picture [47 x 48] intentionally omitted <==**

**==> picture [545 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.009<br>Instructing Instructed pacs.009 Instructing Agent<br>Agent: Agent A Agent: Agent B<br>Instructing Instructed<br>Agent: Agent B Agent: Agent C<br>**----- End of picture text -----**<br>


_**Instructing Agent**_ and _**Instructed Agent**_ represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment leg. 

_Instructing Agent_ and _Instructed Agent_ elements are required in all pacs messages and are only available in the _**Credit Transfer Information**_ 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 265 -->
## **Intermediary Agents** 

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. _**Intermediary Agent**_ is an example of this, where these agents are classified in numeric order (i.e. _Intermediary Agent 1_ ) _**Previous Instructing Agent**_ however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment. 

. The below diagram visualizes the change of Agent role at different stages of the payment transaction life cycle 

**==> picture [802 x 240] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E F G<br>Debtor Instructing Agent &  Instructed Agent Intermediary Agent 1 Intermediary Agent 2 Creditor Agent Creditor<br>Debtor Agent<br>Debtor Debtor Agent Instructing Agent  Instructed Agent Intermediary Agent 1 Creditor Agent Creditor<br>Debtor Debtor Agent Previous Instructing  Instructing Agent  Instructed Agent Creditor Agent Creditor<br>Agent 1<br>Debtor Debtor Agent Previous Instructing  Previous Instructing  Instructing Agent Creditor Agent &  Creditor<br>Agent 1 Agent 2 Instructed Agent<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 266 -->
The can to 3 which a role in the pacs message capture up Intermediary Agents, play dynamic payment between the Debtor Agent and Creditor Agent. 

**Min 0 – Max 1** 

**==> picture [61 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 1**_ captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 1 Account**_ captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a. 

## **Min 0 – Max 1** 

**2** 

**==> picture [51 x 37] intentionally omitted <==**

The _**Intermediary Agent 2**_ captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 2 Account**_ captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

**==> picture [62 x 53] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 3**_ captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. **Min 0 – Max 1**

---

<!-- ELEMENT 267 -->
**==> picture [127 x 29] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>identifies the  Debtor<br>**----- End of picture text -----**<br>


## The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the _**Debtor**_ . The _Debtor_ sub elements describe the _Debtor_ in greater detail. 

**==> picture [52 x 25] intentionally omitted <==**

**----- Start of picture text -----**<br>
BICFI<br>**----- End of picture text -----**<br>


**==> picture [441 x 325] intentionally omitted <==**

**----- Start of picture text -----**<br>
Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Debtor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either<br>Postal<br>structured or unstructured  Debtor<br>Address<br>address details<br>**----- End of picture text -----**<br>


**==> picture [214 x 295] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 268 -->
**Min 0 – Max 1** The pacs.009 _**Debtor Account**_ is used to capture the account information for which debit entry is/has been applied to the Debtor’s account, which are also reflected in their account Statement. 

The _**Debtor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

---

<!-- ELEMENT 269 -->
**Min 0 – Max 1 Min 0 – Max 1** The _**Debtor Agent**_ and _**Creditor Agent**_ are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the _Debtor_ and _Creditor_ . However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship. 

**==> picture [61 x 62] intentionally omitted <==**

**==> picture [80 x 137] intentionally omitted <==**

**==> picture [84 x 137] intentionally omitted <==**

Note: Where the _**Debtor**_ and _**Creditor**_ maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the _**Creditor Agent**_ element to align with translation from . the legacy MT message 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 270 -->
## **Account** 

## **Min 0 – Max 1** 

The pacs.009 _**Debtor Agent Account**_ and _**Creditor Agent Account**_ is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction. 

The _**Debtor Agent Account**_ and _**Creditor Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

- **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

---

<!-- ELEMENT 271 -->
**==> picture [441 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>whose account<br>identifies the  Creditor<br>BICFI<br>The Creditor sub<br>Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Creditor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either<br>Postal<br>structured or unstructured  Debtor<br>Address<br>address details<br>**----- End of picture text -----**<br>


The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the _**Creditor**_ . The _Creditor_ sub elements describe the _Creditor_ in greater detail. 

**==> picture [186 x 301] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 272 -->
**Min 0 – Max 1** The pacs.009 _**Creditor Account**_ is used to capture the account information for which a credit entry is intended to be applied to the Creditor’s account, which are also reflected in their account Statement. 

The _**Creditor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

---

<!-- ELEMENT 273 -->
The _**Instruction for Next Agent**_ and _**Instruction for Creditor Agent**_ elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents. 

**Min 0 – Max 2** 

**==> picture [52 x 55] intentionally omitted <==**

**==> picture [90 x 110] intentionally omitted <==**

The _**Instruction for Creditor Agent**_ element offers a multiplicity of up to 2 occurrences of information. This element enables: 

➢ the use of 2 embedded codes to describe the instruction 

➢ free format _instruction information_ 

➢ or both, where the free format complements the code. The use of this element may be bilaterally agreed with the _Creditor Agent_ . It must be passed . on throughout the life cycle of the transaction until the payment reaches the _Credit Agent The Creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) Instruction for Creditor Agent, Instruction Information element preceded by /UDLC/ (UnDerLying Creditor) to provide party transparency in the settlement message._ 

**Min 0 – Max 6** 

The _**Instruction for Next Agent**_ element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format _instruction information_ in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent) _Credit Transfer Transaction Information_

---

<!-- ELEMENT 274 -->
**Min 0 – Max 2** 

An _**Instruction for Creditor Agent**_ elements within the pacs.009 Financial Institution Credit Transfer, used to settle a pacs.009 Financial Institution Credit Transfer Advice (ADV), provides information related to the Creditor in the advice message (Underlying Creditor). 

The _**Creditor**_ of the pacs.009 ADV are commonly captured in one of the following ways: 

- As a BIC ( _**BICFI**_ ) either on its own, or 

- • As a _**Clearing System Member Identification**_ or a _**LEI**_ with _**Name**_ , and _**Postal Address**_ 

|**pacs.009 ADV**<br>**Creditor/Financial Institution**|**pacs.009 ADV**<br>**Creditor/Financial Institution**|**pacs.009 ADV**<br>**Creditor/Financial Institution**|**Data example**|
|---|---|---|---|
||**BICFI**||ABCDGB22|
||**Clearing**<br>**System**<br>**Member**<br>**Identification**|Clearing Sy stem<br>Identif ication|GBDSC|
|||Member<br>Identif ication|205050|
||**LEI**||123456A1BCDEFG2T54|
||**Name**||ABC BANK|
|||**Various**<br>**Structured**<br>**elements**|252<br>HIGH STREET<br>LONDON<br>EC1 1WX<br>GB|



**==> picture [41 x 57] intentionally omitted <==**

pacs.009 _**Instruction for Creditor Agent**_ **/Instruction Information.** 

**==> picture [51 x 55] intentionally omitted <==**

Up to 2 occurrences of Instruction Information may be provided. The last available occurrence of **Instruction Information** , preceded by /UDLC/, must be used to capture the Underlying Creditor provided in the pacs.009 ADV. 

**pacs.009 Instruction for Creditor Agent/Instruction Information** /UDLC/ABCDGB22 

**BICFI** only. 

## **OR** 

**Name** and structured **Postal Address** (TownName and Country Code should be prioritised). 

- /UDLC/ABC BANK LONDON GB 

## **OR** 

**Name** and unstructured **Address Line** (TownName and Country Code should be prioritised, where possible). 

/UDLC/ABC BANK LONDON EC1 1WX GB

---

<!-- ELEMENT 275 -->
## **Min 0 – Max 1** 

The _**Purpose**_ elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code. The is used the the nature of the CORT Trade Settlement CFEE purpose by capture payment e.g., Payment, Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008. 

**==> picture [123 x 91] intentionally omitted <==**

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. 

For example: 

OTCD is classified within the Collateral categorisation, with the _Name_ OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated. 

**==> picture [61 x 62] intentionally omitted <==**

_Category Purpose_ also captures a high level purpose, which unlike _Purpose_ is less granular but can trigger special processing e.g., Category Purpose code SECU ‘Securities’ may trigger pacs.002 _Payment Status Report_ to provide update on the progress of the payment to the previous Agent. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 276 -->
The optional _**Remittance Information**_ element within the pacs.009 Financial Institution Credit Transfer is nested to provide _**Unstructured**_ information related to payment. 

**Min 0 – Max 1** _**Remittance Information**_ enable the matching/reconciliation of an entry that the payment is intended to settle 

**==> picture [66 x 73] intentionally omitted <==**

**==> picture [62 x 62] intentionally omitted <==**

**Min 0 – Max 1** The **Unstructured** sub element captures free format _Remittance Information_ which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence. 

Note: unlike the pacs.008 _Remittance Information_ can only be captured in an _Unstructured_ element in the pacs.009 Financial Institution Credit Transfer. _**Remittance Information**_ is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [12 x 7] intentionally omitted <==**

---

<!-- ELEMENT 277 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

## **Serial Financial Institution Payments** 

Use Case p.9.1.1 – High Level Financial Institution Credit Transfer (pacs.009) settled over a Payment Market Infrastructure Use Case p.9.1.2 - High Level Financial Institution Credit Transfer (pacs.009) pre-advised settled using pacs.009.

---

<!-- ELEMENT 278 -->
## **Payment Market Infrastructure** 

**==> picture [671 x 323] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4<br>pacs.009 pacs.009 pacs.009 camt.053<br>A pacs.002 B pacs.002 C camt.054 D<br>Settlement<br>Complete<br>4<br>1 2<br>Agent C credits the account of the<br>Agent B processes the payment<br>Debtor initiates a payment<br>Creditor (Agent D), and may<br>on Agent C, via the Payment<br>instruction to the Debtor Agent<br>Market Infrastructure. optionally provide a notification<br>e.g. credit notification in addition to<br>an account statement (camt.054)<br>in addition to a customer statement<br>3<br>(camt.053)<br>Payment Market Infrastructure,<br>settles the payment between<br>Agent B and Agent C as direct<br>participants of the Market<br>Infrastructure, and provides a<br>settlement confirmation to Agent B<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 279 -->
**==> picture [851 x 370] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 (advice)<br>5<br>2a<br>pacs.009  camt.054<br>(ADV)<br>A B E F<br>1 2b<br>4<br>3<br>4<br>1<br>pacs.009 Agent D credits the account of<br>Debtor initiates a payment<br>Agent E and should provide a<br>instruction to the Debtor Agent C pacs.002 D notification e.g. credit notification<br>(camt.054) in addition to a<br>customer statement (camt.053)<br>2a 2b<br>Debtor Agent (B) provided a notification to In parallel the Debtor Agent (B) initiates a<br>Creditor Agent (E) using a pacs.009 advice to payment to credit the account of Agent (E)<br>indicate a ‘pre-advise and provides the related as the creditor in the pacs.009 settlement  5<br>payment details (in step 2b) This provides Agent message<br>E the ability to take the payment amount into Agent E receives the payment and<br>their position, particularly where final settlement 3 credits the account of Agent F as<br>in step 5 occur after their business day. (i.e. time Agent C processes the payment on to  the Creditor, and may optionally<br>zone differences between the various Agent in Agent D provide a notification e.g. credit<br>notification.<br>the payment chain.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 280 -->
# **Financial Institution Credit Transfer** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 281 -->
**==> picture [186 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 (ADV)<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


The pacs.009 advice is used to preadvice an Agent of a fund movement toward the Creditor. 

The core pacs.009 is used to perform the settlement of this pre-advice message. 

**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Credit Transfer<br>Transaction Information<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 282 -->
**==> picture [583 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.009<br>pacs.009 ADV<br>pacs.002<br>pacs.009<br>pacs.002 camt.053<br>**----- End of picture text -----**<br>


The Financial Institution Credit Transfer (advice) message is sent by a Debtor Agent to a Creditor Agent, directly. In this context the pacs.009 ADV is used as a direct advice message. 

It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are **Financial Institutions** . 

**==> picture [43 x 11] intentionally omitted <==**

_To provide party transparency in the pacs.009 ADV, the_ _**Debtor** of the pacs.009 ADV remains the Debtor of_

---

<!-- ELEMENT 284 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender’s Reference (Field could be considered a similar where a contains a 20) comparison pacs message single Transaction. 

**==> picture [60 x 60] intentionally omitted <==**

Each transaction’s _Credit Transfer Transaction Information_ contains a variety of nested _Payment Identification_ elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference) 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 285 -->
**Min 1 – Max 1** 

## The pacs.009 message _**Creation Date**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 286 -->
## **Min 1 – Max 1** 

The pacs.009 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 287 -->
**Min 1 – Max 1** 

The pacs.009 _**Settlement Method**_ element within the Group Header _**Settlement Information**_ , includes one of the embedded codes to indicate how the payment message will be settled. 

**$** € 

The _**Settlement Method** element_ in the pacs.009 ADV is fixed to **COVE** . This indicate this advice of Financial Institution Credit Transfer will be settlement using a covering pacs.009. 

Like the pacs.008, the Agents being used in the covering payment to reimburse the Instructed Agent can be provided in the dedicated Reimbursement Agent elements. This allows the Instructed Agent to identify the debit account on their books from the Reimbursement Agent account or look up the account related to the reimbursement agent.

---

<!-- ELEMENT 288 -->
The a number of Reimbursement as a sub element to _**Settlement**_ pacs message captures Agents _**Information**_ these elements detail the Agent in the cover method who will process the pacs.009 cover. These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as The _**Instructing Reimbursement Agent,**_ and _**Instructed Reimbursement Agent.**_ Each of these reimbursement agents also has a dedicated account element to optionally capture their related account details. 

## **Min 0 – Max 1** 

**$** 

The _**Instructing Reimbursement Agent**_ captures the Agent who will execute a covering payment (i.e. pacs.009 COV or domestic equivalent) often referred to as the currency correspondent. This optional element is comparable with the Field 53a in the legacy FIN message. 

## **Min 0 – Max 1** 

The _**Instructing Reimbursement Agent Account**_ captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 53. 

**Min 0 – Max 1** 

**==> picture [59 x 60] intentionally omitted <==**

**----- Start of picture text -----**<br>
$<br>€<br>**----- End of picture text -----**<br>


The _**Instructed Reimbursement Agent**_ captures the Agent who will receive the covering payment (i.e., pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer _Instructed Agent_ . This optional element is comparable with the Field 54a in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Instructed Reimbursement Agent Account**_ captured the account related to this Reimbursement Agent.

---

<!-- ELEMENT 290 -->
## **Min 1 – Max 1** 

## The pacs message _**Payment Identification**_ provides a set of elements to identify the payment, of which several are mandatory elements 

**==> picture [211 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Identification<br>$<br>**----- End of picture text -----**<br>


a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender’s Reference (Field 20) of the legacy MT payment message. 

**==> picture [119 x 199] intentionally omitted <==**

**----- Start of picture text -----**<br>
Instruction<br>Identification<br>Min 1 – Max 1<br>End to End<br>Identification<br>Min 1 – Max 1<br>**----- End of picture text -----**<br>


Note: this reference must be transported in the _End-toEnd Identification_ of the pacs.009 message used to settle the pacs.009 ADV 

**==> picture [35 x 33] intentionally omitted <==**

an end-to-end reference provided by the _Debtor_ which must be passed unchanged throughout the payment and reported to the Creditor. 

note: In a pacs.009 ADV if the Debtor has not provide an end-to-end identifier, the _Debtor Agent_ may populate “NOTPROVIDED” to comply the mandatory need of this element. 

**==> picture [36 x 34] intentionally omitted <==**

**==> picture [105 x 69] intentionally omitted <==**

**----- Start of picture text -----**<br>
UETR<br>Min 1 – Max 1<br>**----- End of picture text -----**<br>


the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their

---

<!-- ELEMENT 291 -->
## **Min 1 – Max 1** The _**Identification** also_ elements pacs message _**Payment**_ provides a set of optional to identify the payment. 

**==> picture [752 x 244] intentionally omitted <==**

**----- Start of picture text -----**<br>
Transaction an end-to-end reference assigned by the first Instructing<br>Identification Agent to identify the transaction.<br>Payment Min 0 – Max 1<br>Identification<br>$ a point-to-point reference populated by a Payment<br>Clearing<br>Market Infrastructure, typically to the settlement leg of a<br>System<br>clearing system transaction as a reference to the settled<br>Reference<br>clearing transaction.<br>Min 0 – Max 1<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 292 -->
**Min 0 – Max 1** 

The pacs message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. 

a choice of imbedded codes representing the urgency considered by the Instructing Agent, **Min 0 –** this point-to-point information may be used by the Instructed Agent to differentiate . the processing priority 

_**Instruction Priority**_ **Min 0 – Max 1** 

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS 

_**Clearing Channel**_ 

**Min 0 – Max 1** 

A nested element which may either use an external ISO Service Level code* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. 

_**Service Level**_ **Min 0 – Max 3** 

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV 

_Payment Type Information_ 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order. 

_**Local Instrument**_ **Min 0 – Max 1** 

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

i 

**==> picture [35 x 33] intentionally omitted <==**

**==> picture [87 x 41] intentionally omitted <==**

**----- Start of picture text -----**<br>
Category<br>**----- End of picture text -----**<br>


A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- ELEMENT 293 -->
**Date** 

**£** 

**$** 

¥ 

## The pacs.009 message (unlike the pacs.008) has only one element to capture the amount of the Credit Transfer, _**Interbank Settlement Amount**_ . 

**Min 1 – Max 1** 

A mandated currency amount moved between the _Instructing Agent_ and the _Instructed Agent._ _**Interbank**_ This therefore is the point-to-point currency amount exchanged, comparable with the MT Field _**Settlement**_ 32A _**Amount**_ 

**==> picture [44 x 44] intentionally omitted <==**

_**Interbank Settlement Date**_ 

A mandated date on which the _Interbank Settlement_ should be executed between the _Instructing Agent_ and the _Instructed Agent._ This therefore is the value date comparable with the MT Field 32A 

**==> picture [63 x 62] intentionally omitted <==**

Note: the Financial Institution Credit Transfer (pacs.009) has no _Instructed Amount_ element, _Exchange Rate_ or _Charger Bearer_ (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain

---

<!-- ELEMENT 294 -->
## **& Request** 

The pacs.009 message has three optional elements to capture the optional information related to the settlement of the instructions. 

## **Min 0 – Max 1** 

**==> picture [59 x 55] intentionally omitted <==**

The _**Settlement Priority**_ provides an optional choice of embedded codes to indicate the instruction’s settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the _**Settlement Method**_ and should not be confused with the _**Instruction Priority.**_ 

**==> picture [36 x 35] intentionally omitted <==**

Note: As the _**Settlement Method**_ of the pacs.009 (ADV) is ‘COVE’ (settled via a covering pacs.009) Settlement Priority is relevant to the covering payment not the pacs.009 ADV 

**==> picture [59 x 68] intentionally omitted <==**

**Min 0 – Max 1** 

The _**Settlement Time Indication**_ optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure. 

This DateTime can be captured in two nested elements, _**Debit Date Time**_ and _**Credit Date Time**_ . 

## **Min 0 – Max 1** 

**==> picture [60 x 65] intentionally omitted <==**

The _**Settlement Time Request**_ optionally captures the time settlement is requested for the payment instruction by the Instructing Agent.  This Time can be capture in four nested elements: 

- _**CLS Time**_ the time the amount must be credit to CLS Bank 

- _**Till Time**_ the time until which the payment may be settled

---

<!-- ELEMENT 295 -->
**==> picture [47 x 48] intentionally omitted <==**

**==> picture [545 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.009<br>Instructing Instructed pacs.009 Instructing Agent<br>Agent: Agent A Agent: Agent B<br>Instructing Instructed<br>Agent: Agent B Agent: Agent C<br>**----- End of picture text -----**<br>


_**Instructing Agent**_ and _**Instructed Agent**_ represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment leg. 

_Instructing Agent_ and _Instructed Agent_ elements are required in all pacs messages and are only available in the _**Credit Transfer Information**_ 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 296 -->
## **Intermediary Agents** 

**==> picture [34 x 34] intentionally omitted <==**

Unlike the other pacs.009 messages in the CBPR+ collection, the pacs.009 ADV message is exchanged directly between the Debtor Agent (as an Instructing Agent) and Creditor Agent (as an Instructed Agent). The roles of previous Instructing Agents and Intermediary Agents are therefore irreverent in the pacs.009 (ADV) 

**==> picture [802 x 240] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E F G<br>Debtor Instructing Agent &  Instructed Agent Intermediary Agent 1 Intermediary Agent 2 Creditor Agent Creditor<br>Debtor Agent<br>Debtor Debtor Agent Instructing Agent  Instructed Agent Intermediary Agent 1 Creditor Agent Creditor<br>Debtor Debtor Agent Previous Instructing  Instructing Agent  Instructed Agent Creditor Agent Creditor<br>Agent 1<br>Debtor Debtor Agent Previous Instructing  Previous Instructing  Instructing Agent Creditor Agent &  Creditor<br>Agent 1 Agent 2 Instructed Agent<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 297 -->
**==> picture [127 x 29] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>identifies the  Debtor<br>**----- End of picture text -----**<br>


## The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the _**Debtor**_ . The _Debtor_ sub elements describe the _Debtor_ in greater detail. 

**==> picture [52 x 25] intentionally omitted <==**

**----- Start of picture text -----**<br>
BICFI<br>**----- End of picture text -----**<br>


**==> picture [441 x 325] intentionally omitted <==**

**----- Start of picture text -----**<br>
Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Debtor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either<br>Postal<br>structured or unstructured  Debtor<br>Address<br>address details<br>**----- End of picture text -----**<br>


**==> picture [214 x 295] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 298 -->
**Min 0 – Max 1** The pacs.009 _**Debtor Account**_ is used to capture the account information for which debit entry is/has been applied to the Debtor’s account, which are also reflected in their account Statement. 

The _**Debtor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

---

<!-- ELEMENT 299 -->
**Min 0 – Max 1 Min 0 – Max 1** The _**Debtor Agent**_ and _**Creditor Agent**_ are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the _**Debtor**_ and _**Creditor**_ . However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship. 

**==> picture [61 x 62] intentionally omitted <==**

**==> picture [80 x 137] intentionally omitted <==**

**==> picture [84 x 137] intentionally omitted <==**

Note: Where the _**Debtor**_ and _**Creditor**_ maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the _**Creditor Agent**_ element to align with translation from the legacy MT message. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 300 -->
## **Agent Account** 

## **Min 0 – Max 1** 

The pacs.009 _**Debtor Agent Account**_ and _**Creditor Agent Account**_ is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction. 

The _**Debtor Agent Account**_ and _**Creditor Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

- **Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

- **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

---

<!-- ELEMENT 301 -->
The BIC which whose account describe the Agent identifies the _Creditor_ _**BICFI**_ as the _**Creditor**_ . The _Creditor_ sub in greater detail. _**Clearing**_ Information used to identify a _**System**_ Debtor by a clearing system _**Member Id**_ identifier. _Creditor_ Legal entity identifier of _**LEI**_ the financial institution. _**Name**_ by which the _**Name**_ Agent is known _The Creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009_ Nested element capturing either _**Postal** ADV) Instruction for Creditor Agent, Instruction_ structured or unstructured _Debtor_ _**Address** Information element preceded by /UDLC/_ 

The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the _**Creditor**_ . The _Creditor_ sub elements describe the _Creditor_ in greater detail. 

**==> picture [186 x 295] intentionally omitted <==**

**==> picture [37 x 36] intentionally omitted <==**

---

<!-- ELEMENT 302 -->
**Min 0 – Max 1** The pacs.009 _**Creditor Account**_ is used to capture the account information for which a credit entry is intended to be applied to the Creditor’s account, which are also reflected in their account Statement. 

The _**Creditor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

---

<!-- ELEMENT 303 -->
The _**Instruction for Next Agent**_ and _**Instruction for Creditor Agent**_ elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents. 

## **Min 0 – Max 2** 

**==> picture [52 x 55] intentionally omitted <==**

The _**Instruction for Creditor Agent**_ element offers a multiplicity of up to 2 occurrences of information. This element enables: 

➢ the use of 2 embedded codes to describe the instruction 

➢ free format _instruction information_ 

➢ or both, where the free format complements the code. The use of this element may be bilaterally agreed with the _Creditor Agent_ . It must be passed . on throughout the life cycle of the transaction until the payment reaches the _Credit Agent_ 

**Min 0 – Max 6** 

**==> picture [51 x 57] intentionally omitted <==**

The _**Instruction for Next Agent**_ element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format _instruction information_ in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent) 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 304 -->
## **Min 0 – Max 1** 

The _**Purpose**_ elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code. The is used the the nature of the CORT Trade Settlement CFEE purpose by capture payment e.g. Payment, Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008. 

**==> picture [123 x 91] intentionally omitted <==**

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. 

For example: 

OTCD is classified within the Collateral categorisation, with the _Name_ OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated. 

**==> picture [61 x 62] intentionally omitted <==**

_Category Purpose_ also captures a high level purpose, which unlike _Purpose_ is less granular but can trigger special processing e.g. Category Purpose code SECU ‘Securities’ may trigger pacs.002 _Payment Status Report_ to provide update on the progress of the payment to the previous Agent. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 305 -->
The optional _**Remittance Information**_ element within the pacs.009 Financial Institution Credit Transfer is nested to provide _**Unstructured**_ information related to payment. 

**Min 0 – Max 1** _**Remittance Information**_ enable the matching/reconciliation of an entry that the payment is intended to settle 

**==> picture [66 x 73] intentionally omitted <==**

**==> picture [62 x 62] intentionally omitted <==**

**Min 0 – Max 1** The **Unstructured** sub element captures free format _Remittance Information_ which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence. 

Note: unlike the pacs.008 _Remittance Information_ can only be captured in an _Unstructured_ element in the pacs.009 Financial Institution Credit Transfer. _**Remittance Information**_ is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [12 x 7] intentionally omitted <==**

---

<!-- ELEMENT 306 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

## **Financial Institution Advice Payments** 

Use Case p.9.1.2.a - High Level Financial Institution Credit Transfer (pacs.009) pre-advised using pacs.009 (advice) Use Case p.9.1.2.b - High Level Financial Institution Credit Transfer (pacs.009) pre-advised using pacs.009 (advice)

---

<!-- ELEMENT 307 -->
**==> picture [851 x 370] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 (advice)<br>2a 5<br>pacs.009 pacs.009 (ADV) camt.054<br>A 1 B E camt.053 F<br>2b<br>4<br>3<br>4<br>1<br>pacs.009 Agent D credits the account of<br>Debtor initiates a payment<br>Agent E and should provide a<br>instruction to the Debtor Agent C pacs.002 D notification e.g. credit notification<br>(camt.054) in addition to a<br>customer statement (camt.053)<br>2a 2b<br>Debtor Agent (B) provided a notification to In parallel the Debtor Agent (B) initiates a<br>Creditor Agent (E) using a pacs.009 advice to payment to credit the account of Agent (E)<br>indicate a ‘pre-advise and provides the related as the creditor in the pacs.009 settlement  5<br>payment details (in step 2b) This provides Agent message<br>E the ability to take the payment amount into Agent E receives the payment and<br>their position, particularly where final settlement 3 credits the account of Agent F as<br>in step 5 occur after their business day. (i.e. time Agent C processes the payment on to  the Creditor, and may optionally<br>zone differences between the various Agent in Agent D provide a notification e.g. credit<br>notification.<br>the payment chain.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 308 -->
**==> picture [851 x 370] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 (advice)<br>2a 5<br>pacs.009 pacs.009 (ADV) camt.054<br>A 1 B E camt.053 F<br>2b<br>4<br>3<br>4<br>1<br>pacs.009 Agent D processes the payment<br>Debtor initiates a payment<br>on to Agent E (as the Account<br>instruction to the Debtor Agent C pacs.002 D Servicing Institution, Settlement<br>method INDA)<br>2a 2b<br>Debtor Agent (B) provided a notification to In parallel the Debtor Agent (B) initiates a<br>Creditor Agent (E) using a pacs.009 advice to payment to credit the account of Agent (E)<br>indicate a ‘pre-advise and provides the related as the creditor in the pacs.009 settlement  5<br>payment details (in step 2b) This provides Agent message<br>E the ability to take the payment amount into Agent E receives the payment and<br>their position, particularly where final settlement 3 credits the account of Agent F as<br>in step 5 occur after their business day. (i.e. time Agent C processes the payment on to  the Creditor, and may optionally<br>zone differences between the various Agent in Agent D provide a notification e.g. credit<br>notification.<br>the payment chain.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 309 -->
# **Financial Institution Credit Transfer (Cover)** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 310 -->
**==> picture [137 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009<br>**----- End of picture text -----**<br>


**==> picture [110 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [110 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
Credit Transfer<br>Transaction<br>Information<br>**----- End of picture text -----**<br>


**==> picture [135 x 68] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 (COV)<br>**----- End of picture text -----**<br>


Group Header 

**==> picture [110 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
Credit Transfer<br>Transaction<br>Information<br>**----- End of picture text -----**<br>


The pacs.009 has two main use cases: 

- as a core Financial Institution Credit Transfer message 

- As a **COV** where it is used as cover of (to settle) a pacs.008. 

The pacs.009 therefore contain information of the underlying Customer Credit Transfer (pacs.008) for use in the cover scenario, which is the key attribute to differentiate between these two use cases. 

**==> picture [111 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
Underlying<br>Customer Credit<br>Transfer<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 311 -->
**==> picture [583 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.009<br>pacs.002<br>pacs.009<br>pacs.002 camt.053<br>**----- End of picture text -----**<br>


The Financial Institution Credit Transfer message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are **Financial Institutions** .

---

<!-- ELEMENT 312 -->
## **roles between messages** 

**==> picture [799 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.008<br>pacs.002<br>pacs.009 cov<br>pacs.002<br>pacs.009 cov<br>pacs.002 camt.054<br>Party pacs.008 pacs.009 cov<br>camt.053<br>Debtor Underlying Debtor<br>The Financial Institution Credit Transfer cover message is sent by a<br>Debtor Agent Debtor<br>Debtor Financial Institution to a Creditor Financial Institution, directly<br>or through other agents and/or a payment clearing and settlement<br>Creditor Agent Creditor system. It is important to recognise that some  roles change  between<br>**----- End of picture text -----**<br>


The Financial Institution Credit Transfer cover message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is important to recognise that some **roles change** between these parallel messages. 

**==> picture [32 x 21] intentionally omitted <==**

---

<!-- ELEMENT 313 -->
## **roles between messages** 

**==> picture [744 x 338] intentionally omitted <==**

**----- Start of picture text -----**<br>
CA<br>DA C<br>D<br>pacs.008<br>A D pacs.002 D<br>C<br>DA CA<br>pacs.009 cov pacs.009 cov<br>C<br>B pacs.002<br>Party pacs.008 pacs.009 cov<br>Debtor Underlying Debtor<br>The correspondent banking cover payment method<br>Debtor  both the pacs.008 and pacs.009 cov as a whole<br>Agent Debtor whereby the UETR element within these messages contain the<br>same  UETRwhich effectively interlink the messages.<br>Creditor<br>Creditor As interlinked it is understand<br>**----- End of picture text -----**<br>


**==> picture [61 x 61] intentionally omitted <==**

The correspondent banking cover payment method utilises both the pacs.008 and pacs.009 cov as a whole transaction, whereby the UETR element within these messages contain the **same** UETRwhich effectively interlink the messages.

---

<!-- ELEMENT 315 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender’s Reference (Field could be considered a similar where a contains a 20) comparison pacs message single Transaction. 

**==> picture [60 x 60] intentionally omitted <==**

Each transaction’s _Credit Transfer Transaction Information_ contains a variety of nested _Payment Identification_ elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference) 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 316 -->
**Min 1 – Max 1** 

## The pacs.009 message _**Creation Date**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 317 -->
## **Transactions** 

## **Min 1 – Max 1** 

The pacs.009 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 318 -->
## **Min 1 – Max 1** 

The pacs.009 _**Settlement Method**_ element within the Group Header _**Settlement Information**_ , includes one of the embedded codes to indicate how the payment message will be settled. 

The _**Settlement Method** element_ in the pacs.009 allows a choice of an embedded code. 

**==> picture [28 x 28] intentionally omitted <==**

**----- Start of picture text -----**<br>
$<br>€<br>**----- End of picture text -----**<br>


**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated _**Settlement Account**_ element. 

**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated _**Settlement Account**_ element. 

**==> picture [60 x 47] intentionally omitted <==**

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in

---

<!-- ELEMENT 319 -->
The pacs.009 message _**Settlement Account**_ is a nested element as part of _**Settlement Information,**_ this element identifies information related to an account used to settle the payment instruction. 

**Min 0 – Max 1** The _**Settlement Account**_ identifies the account details maintained at the account institution for the settlement of the instruction as servicing (Agent responsible indicated in the _**Settlement Method**_ ) 

**==> picture [80 x 84] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 321 -->
**Min 1 – Max 1** 

## The pacs message _**Payment Identification**_ provides a set of elements to identify the payment, of which several are mandatory elements 

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender’s Reference (Field 20) of the legacy MT payment message. 

_**Instruction Identification**_ **Min 1 – Max 1** 

an end-to-end reference provided by the _Debtor_ which must be passed unchanged throughout the payment and reported to the Creditor. 

**==> picture [158 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Identification<br>**----- End of picture text -----**<br>


note: for a pacs.009 COV the end-to-end id is provided (by the Debtor) from the pacs.008 Instruction id. In a pacs.009 COR if the Debtor has not provided an end-to-end identifier, the _Debtor Agent_ may populate “NOTPROVIDED” to comply the mandatory need of this element. 

_**End to End Identification**_ 

**==> picture [303 x 58] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1<br>$<br>**----- End of picture text -----**<br>


**==> picture [35 x 35] intentionally omitted <==**

the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their 

**==> picture [54 x 22] intentionally omitted <==**

**----- Start of picture text -----**<br>
UETR<br>**----- End of picture text -----**<br>


**==> picture [61 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 322 -->
## **(continued)** 

## **Min 1 – Max 1** 

## The _**Identification** also_ elements pacs message _**Payment**_ provides a set of optional to identify the payment. 

**==> picture [752 x 244] intentionally omitted <==**

**----- Start of picture text -----**<br>
Transaction an end-to-end reference assigned by the first Instructing<br>Identification Agent to identify the transaction.<br>Payment Min 0 – Max 1<br>Identification<br>$ a point-to-point reference populated by a Payment<br>Clearing<br>Market Infrastructure, typically to the settlement leg of a<br>System<br>clearing system transaction as a reference to the settled<br>Reference<br>clearing transaction.<br>Min 0 – Max 1<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 323 -->
**Min 0 – Max 1** 

## **Information** 

The pacs message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. 

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. 

_**Service Level Instruction**_ **Min 0 – Max 3** _**Priority**_ **Min 0 – Max 1** 

a choice of imbedded codes representing the urgency considered by the Instructing Agent, **Min 0 –** this point-to-point information may be used by the Instructed Agent to differentiate the processing priority. 

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV 

_Payment Type Information_ 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order. 

_**Local Instrument**_ **Min 0 – Max 1** 

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS 

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

i 

**==> picture [35 x 33] intentionally omitted <==**

_**Clearing Channel**_ 

**==> picture [87 x 41] intentionally omitted <==**

**----- Start of picture text -----**<br>
Category<br>**----- End of picture text -----**<br>


A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to 

**Min 0 – Max 1**

---

<!-- ELEMENT 324 -->
**Date** 

**£** 

**$** 

¥ 

## The pacs.009 message (unlike the pacs.008) has only one element to capture the amount of the Credit Transfer, _**Interbank Settlement Amount**_ . 

**Min 1 – Max 1** 

A mandated currency amount moved between the _Instructing Agent_ and the _Instructed Agent._ _**Interbank**_ This therefore is the point-to-point currency amount exchanged, comparable with the MT Field _**Settlement**_ 32A _**Amount**_ 

**Min 1 – Max 1** 

**==> picture [44 x 44] intentionally omitted <==**

_**Interbank Settlement Date**_ 

A mandated date on which the _Interbank Settlement_ should be executed between the _Instructing Agent_ and the _Instructed Agent._ This therefore is the value date comparable with the MT Field 32A 

**==> picture [63 x 62] intentionally omitted <==**

Note: the Financial Institution Credit Transfer (pacs.009) has no _Instructed Amount_ element, _Exchange Rate_ or _Charger Bearer_ (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain

---

<!-- ELEMENT 325 -->
## **Request** 

The pacs.009 message has three optional elements to capture the optional information related to the settlement of the instructions. 

**Min 0 – Max 1** 

**==> picture [59 x 55] intentionally omitted <==**

**==> picture [59 x 68] intentionally omitted <==**

The _**Settlement Priority**_ provides an optional choice of embedded codes to indicate the instruction’s settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the _**Settlement Method**_ and should not be confused with the _**Instruction Priority.**_ 

Note: Where the _**Settlement Method**_ of the pacs.009 is ‘INDA’ (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code ‘INGA’ implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary. **Min 0 – Max 1** 

**==> picture [36 x 35] intentionally omitted <==**

The _**Settlement Time Indication**_ optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure. 

This DateTime can be captured in two nested elements, _**Debit Date Time**_ and _**Credit Date Time**_ . 

## **Min 0 – Max 1** 

**==> picture [60 x 65] intentionally omitted <==**

The _**Settlement Time Request**_ optionally captures the time settlement is requested for the payment instruction by the Instructing Agent.  This Time can be capture in four nested elements: 

- _**CLS Time**_ the time the amount must be credit to CLS Bank 

- _**Till Time**_ the time until which the payment may be settled

---

<!-- ELEMENT 326 -->
## **Agents** 

**==> picture [545 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.009<br>Instructing Instructed pacs.009 Instructing Agent<br>Agent: Agent A Agent: Agent B<br>Instructing Instructed<br>Agent: Agent B Agent: Agent C<br>**----- End of picture text -----**<br>


_**Instructing Agent**_ and _**Instructed Agent**_ represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment leg. 

**==> picture [47 x 48] intentionally omitted <==**

_Instructing Agent_ and _Instructed Agent_ elements are required in all pacs messages and are only available in the _**Credit Transfer Information**_ 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 327 -->
The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent. 

**Min 0 – Max 1** 

**==> picture [63 x 66] intentionally omitted <==**

**==> picture [63 x 65] intentionally omitted <==**

**==> picture [61 x 63] intentionally omitted <==**

The _**Previous Instructing Agent 1**_ captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Previous Instructing Agent 1 Account**_ captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message 

**Min 0 – Max 1** 

The _**Previous Instructing Agent 2**_ captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message. **Min 0 – Max 1** The _**Previous Instructing Agent 2 Account**_ captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** The _**Previous Instructing Agent 3**_ captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message. **Min 0 – Max 1** The _**Previous Instructing Agent 3 Account**_ captured the account related between this Agent and Previous

---

<!-- ELEMENT 328 -->
## **Intermediary Agents** 

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. _**Intermediary Agent**_ is an example of this, where these agents are classified in numeric order (i.e., _Intermediary Agent 1_ ) _**Previous Instructing Agent**_ however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment. 

. The below diagram visualizes the change of Agent role at different stages of the payment transaction life cycle 

**==> picture [802 x 240] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E F G<br>Debtor Instructing Agent &  Instructed Agent Intermediary Agent 1 Intermediary Agent 2 Creditor Agent Creditor<br>Debtor Agent<br>Debtor Debtor Agent Instructing Agent  Instructed Agent Intermediary Agent 1 Creditor Agent Creditor<br>Debtor Debtor Agent Previous Instructing  Instructing Agent  Instructed Agent Creditor Agent Creditor<br>Agent 1<br>Debtor Debtor Agent Previous Instructing  Previous Instructing  Instructing Agent Creditor Agent &  Creditor<br>Agent 1 Agent 2 Instructed Agent<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 329 -->
The can to 3 which a role in the pacs message capture up Intermediary Agents, play dynamic payment between the Debtor Agent and Creditor Agent. 

**Min 0 – Max 1** 

**==> picture [61 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 1**_ captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 1 Account**_ captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a. 

## **Min 0 – Max 1** 

**2** 

**==> picture [51 x 37] intentionally omitted <==**

The _**Intermediary Agent 2**_ captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 2 Account**_ captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

**==> picture [62 x 53] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 3**_ captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. **Min 0 – Max 1**

---

<!-- ELEMENT 330 -->
**==> picture [441 x 364] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>identifies the  Debtor<br>BICFI<br>sub<br>Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Debtor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either<br>Postal<br>structured or unstructured  Debtor<br>Address<br>address details<br>**----- End of picture text -----**<br>


## The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the _**Debtor**_ . The _Debtor_ sub elements describe the _Debtor_ in greater detail. 

**==> picture [214 x 295] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 331 -->
**Min 0 – Max 1** The pacs.009 _**Debtor Account**_ is used to capture the account information for which debit entry is/has been applied to the Debtor’s account, which are also reflected in their account Statement. 

The _**Debtor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

---

<!-- ELEMENT 332 -->
**Min 0 – Max 1 Min 0 – Max 1** The _**Debtor Agent**_ and _**Creditor Agent**_ are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the _Debtor_ and _Creditor_ . However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship. 

**==> picture [61 x 62] intentionally omitted <==**

**==> picture [80 x 137] intentionally omitted <==**

**==> picture [84 x 137] intentionally omitted <==**

Note: Where the _**Debtor**_ and _**Creditor**_ maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the _**Creditor Agent**_ element to align with translation from . the legacy MT message 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 333 -->
## **Agent Account** 

## **Min 0 – Max 1** 

The pacs.009 _**Debtor Agent Account**_ and _**Creditor Agent Account**_ is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction. 

The _**Debtor Agent Account**_ and _**Creditor Agent Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

- **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

---

<!-- ELEMENT 334 -->
**==> picture [441 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>whose account<br>identifies the  Creditor<br>BICFI<br>The Creditor sub<br>Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Creditor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either<br>Postal<br>structured or unstructured  Debtor<br>Address<br>address details<br>**----- End of picture text -----**<br>


The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the _**Creditor**_ . The _Creditor_ sub elements describe the _Creditor_ in greater detail. 

**==> picture [186 x 301] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 335 -->
**Min 0 – Max 1** The pacs.009 _**Creditor Account**_ is used to capture the account information for which a credit entry is intended to be applied to the Creditor’s account, which are also reflected in their account Statement. 

The _**Creditor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 22] intentionally omitted <==**

---

<!-- ELEMENT 336 -->
The _**Instruction for Next Agent**_ and _**Instruction for Creditor Agent**_ elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents. 

## **Min 0 – Max 2** 

**==> picture [52 x 55] intentionally omitted <==**

The _**Instruction for Creditor Agent**_ element offers a multiplicity of up to 2 occurrences of information. This element enables: 

➢ the use of 2 embedded codes to describe the instruction 

➢ free format _instruction information_ 

➢ or both, where the free format complements the code. The use of this element may be bilaterally agreed with the _Creditor Agent_ . It must be passed . on throughout he life cycle of the transaction until the payment reaches the _Credit Agent_ 

**Min 0 – Max 6** 

**==> picture [51 x 57] intentionally omitted <==**

The _**Instruction for Next Agent**_ element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format _instruction information_ in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent) 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 337 -->
## **Min 0 – Max 1** 

The _**Purpose**_ elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code. The is used the the nature of the CORT Trade Settlement CFEE purpose by capture payment e.g. Payment, Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008. 

**==> picture [123 x 91] intentionally omitted <==**

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. 

For example: 

OTCD is classified within the Collateral categorisation, with the _Name_ OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated. 

**==> picture [61 x 62] intentionally omitted <==**

_Category Purpose_ also captures a high level purpose, which unlike _Purpose_ is less granular but can trigger special processing e.g. Category Purpose code SECU ‘Securities’ may trigger pacs.002 _Payment Status Report_ to provide update on the progress of the payment to the previous Agent. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_

---

<!-- ELEMENT 338 -->
The optional _**Remittance Information**_ element within the pacs.009 COV Financial Institution Credit Transfer is nested to provide _**Unstructured**_ information related to payment. 

**Min 0 – Max 1** _**Remittance Information**_ enable the matching/reconciliation of an entry that the payment is intended to settle. 

**==> picture [66 x 73] intentionally omitted <==**

**Min 0 – Max 1** The **Unstructured** sub element captures free format _Remittance Information_ which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence. 

Note: the pacs.008 _**Remittance Information** is captured in the pacs.009 COV within the_ _**Underlying Customer Credit Transfer** ,_ _**Remittance Information** element. The_ _**Remittance Information** in the pacs.009 COV is for_ _**Creditor** this message (often the Creditor Agent of the pacs.008) As this information is not present in the pacs.008 it is unlikely the pacs.009 COV remittance information will be used._ 

**==> picture [63 x 62] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [12 x 7] intentionally omitted <==**

---

<!-- ELEMENT 339 -->
## **Transfer** 

The _**Underlying Customer Credit Transfer**_ element is used when the pacs.009 _Financial Institution Credit Transfer_ message is being utilized to cover a pacs.008 _FI to FI Customer Credit Transfer_ . The  information contained within this nested element relates directly to the information exchanged between the Instructing Agent and Instructed Agent of the pacs.008 FI to FI Customer Credit Transfer and can be compared with Sequence B of the legacy MT 202 COV. 

**Min 1 – Max 1** 

**==> picture [816 x 235] intentionally omitted <==**

**----- Start of picture text -----**<br>
When utilizing the  Underlying Customer<br>Credit Transfer  nested element as part of a<br>pacs.009  Financial Institution Credit<br>Transfer cover  message the:<br>➢ Debtor  Min 1 – Max 1<br>➢ Debtor Agent  Min 1 – Max 1<br>pacs.009<br>pacs.008 ➢ Creditor Agent Min 1 – Max 1<br>(cov)<br>➢ Creditor Min 1 – Max 1<br>Group<br>Group<br>Header are all mandatory elements.<br>Header<br>Credit<br>Credit<br>Transfer<br>Note:  Instruction for Creditor  Transaction  Transfer<br>Transaction<br>Information<br>Agent  from the Underlying  Information<br>Credit Transfer Transaction Information<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 340 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

## **Cover Method Financial Institution Payments** 

Use Case p.9.2.1 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) Use Case p.9.2.2 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) over a Payment Market Infrastructure Use Case p.9.2.3 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) where an incorrect intermediary is used Use Case p.9.2.4 – High Level FI to FI Customer Credit Transfer involved a serial leg into a cover method (pacs.009 COV) Use Case p.9.2.5 – High Level FI to FI Customer Credit Transfer involved a serial leg in and out of a cover method (pacs.009 COV) Use Case p.9.2.6 - High Level FI to FI Customer Credit Transfer involved a serial leg out of a cover method (pacs.009 COV)

---

<!-- ELEMENT 341 -->
**==> picture [851 x 376] intentionally omitted <==**

**----- Start of picture text -----**<br>
method (pacs.009 COV)<br>6<br>1 2a<br>pacs.008<br>A pacs.002 D<br>2b<br>5<br>1 3 4<br>Debtor initiates a payment<br>pacs.009 cov<br>instruction to the Debtor Agent 5<br>B pacs.002 Agent C produces an end of day<br>C<br>account statement report. An<br>2a<br>optional real time notifications e.g.<br>Debtor Agent (A) initiates a payment using  advice of credit may have also been<br>3<br>the cover method to the Creditor Agent (D) created at the time of the credit<br>Agent B processes the payment<br>posting<br>on to Agent C<br>2b<br>6<br>In parallel the Debtor Agent (A) initiates a covering<br>payment to credit the account of Agent (D) who become  Agent D reconciles the covering<br>the Creditor of the cover payment (pacs.009 cov).   4 funds and credits the account of the<br>Agent A’s role also changes in the cover payment  Agent C receives the payment and  Creditor, and may optionally<br>where it becomes the Debtor, whereby Agent A’s  credits the account of Agent D as  provide a notification e.g. credit<br>account with their correspondent (Agent B) is debited the Creditor notification<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 342 -->
## **method (pacs.009 COV) over a Payment Market Infrastructure** 

**==> picture [805 x 360] intentionally omitted <==**

**----- Start of picture text -----**<br>
7<br>1 2a<br>pacs.008<br>A pacs.002 D<br>2b<br>6<br>3<br>1 4 5<br>Debtor initiates a payment<br>pacs.009 cov pacs.009 cov<br>instruction to the Debtor Agent 6<br>C<br>B pacs.002 Agent C produces an end of day<br>account statement report. An<br>2a<br>optional real time notifications e.g.<br>Debtor Agent (A) initiates a  Settlement  4 advice of credit may have also been<br>payment using the cover method  Complete Payment Market Infrastructure,  created at the time of the credit<br>settles the payment between Agent<br>to the Creditor Agent (D) posting<br>B and Agent C as direct<br>participants of the Market<br>2b Infrastructure, and provides a  7<br>settlement confirmation to Agent B<br>In parallel the Debtor Agent (A)  Agent D reconciles the covering<br>3<br>initiates a covering payment to  funds and credits the account of the<br>credit the account of Agent (D)  Agent B processes the payment  5 Creditor, and may optionally<br>with their correspondent (Agent  on Agent C, via the Payment  Agent C receives the payment and  provide a notification e.g. credit<br>C) Market Infrastructure credits the account of Agent D notification<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 343 -->
## **method (pacs.009 COV) where an incorrect intermediary is used.** 

**==> picture [805 x 358] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2a 6<br>pacs.008<br>A pacs.002 D<br>2b<br>4<br>1 3 5 Recognising the error Agent B re-<br>processes the payment on to<br>Debtor initiates a payment<br>pacs.009 cov Agent C using the same UETR<br>instruction to the Debtor Agent<br>(correcting the error in step 3)<br>Z<br>B pacs.002<br>5<br>2a 4 pacs.009 cov Agent C receives the payment and<br>C<br>Debtor Agent (A) initiates a payment using  credits the account of Agent D. Agent C<br>the cover method to the Creditor Agent (D) 3 produces an end of day account<br>statement report. An optional real time<br>Agent B processes the payment on to<br>notifications e.g. advice of credit may<br>Agent Z<br>2b have also been created at the time of the<br>credit posting<br>In parallel the Debtor Agent (A) initiates a covering<br>payment to credit the account of Agent (D) who become<br>Agent Z receives the payment and  6<br>the Creditor of the cover payment (pacs.009 cov).<br>recognises they do not hold the account of<br>Agent A’s role also changes in the cover payment  Agent D reconciles the covering funds<br>Agent D as the Creditor. Agent Z reject the<br>where it becomes the Debtor, whereby Agent A’s  and credits the account of the Creditor,<br>account with their correspondent (Agent B) is debited cover payment (pacs.009 cov) using a  and may optionally provide a notification<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 344 -->
**==> picture [851 x 376] intentionally omitted <==**

**----- Start of picture text -----**<br>
method (pacs.009 COV)<br>4<br>1 2 3a<br>pacs.008<br>pacs.008<br>A B pacs.002 E<br>pacs.002<br>3b<br>6<br>5<br>1<br>Debtor initiates a payment<br>pacs.009 cov<br>instruction to the Debtor Agent 5<br>pacs.002 Agent C processes the payment on<br>C D<br>Agent D, using a correspondent<br>2<br>banking business relationship<br>Debtor Agent (A) initiates a<br>payment using the serial method<br>towards the Creditor Agent (E) 4<br>6<br>Agent E receives the payment  Agent D receives the payment and<br>3a 3b instruction and credits the account of  credits the account of Agent E.<br>the Creditor, and may optionally  Agent D produces an end of day<br>Agent B initiates a payment<br>In parallel the Agent (B) initiates a  provide a notification e.g. credit  account statement report. An<br>using the cover method towards<br>the Creditor Agent (E) by  covering payment to credit the account  notification. Alternatively, they may  optional real time notification e.g.<br>sending a direct pacs.008 to  of Agent (E) with their correspondent  have chosen to await until settlement  advice of credit may have also been<br>(Agent D) occurred in Step 6 based upon their  created at the time of the credit<br>Agent E who they have business<br>relationship with risk appetite. posting<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 345 -->
**==> picture [851 x 377] intentionally omitted <==**

**----- Start of picture text -----**<br>
of a cover method (pacs.009 COV)<br>4<br>7<br>1 2 3a<br>pacs.008 pacs.008<br>pacs.008<br>A pacs.002 B pacs.002 E pacs.002 F<br>3b<br>6<br>5<br>6<br>1<br>pacs.009 cov Agent D receives the payment and<br>Debtor initiates a payment  credits the account of Agent E.<br>instruction to the Debtor Agent Agent D produces an end of day<br>pacs.002<br>C D<br>account statement report. An<br>3a 4 optional real time notification e.g.<br>2 Agent B initiates a payment using  Agent E receives the payment  advice of credit may have also been<br>the cover method towards the  instruction and process the payment  created at the time of the credit<br>Debtor Agent (A) initiates a<br>payment using the serial method  Creditor Agent (F) by sending a  on to Agent F. Alternatively they may  posting<br>towards the Creditor Agent (F) direct pacs.008 to Agent E who they  have chosen to await until settlement<br>have business relationship with. occurred in Step 6 based upon their<br>risk appetite.<br>7<br>3b Agent F receives the payment and<br>5<br>In parallel the Agent (B) initiates a  credits the account of the Creditor,<br>Agent C processes the payment on<br>covering payment to credit the account  and may optionally provide a<br>Agent D, using a correspondent<br>of Agent (E) with their correspondent  notification e.g. credit notification.<br>banking business relationship<br>(A t D)<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 346 -->
**==> picture [851 x 374] intentionally omitted <==**

**----- Start of picture text -----**<br>
cover method (pacs.009 COV)<br>3<br>4<br>1 2a<br>pacs.008 pacs.008<br>A pacs.002 D pacs.002 E<br>2b<br>6<br>5<br>pacs.009 cov<br>B pacs.002 C<br>1<br>2b 4 6<br>Debtor initiates a payment  In parallel the Agent (A) initiates a  Agent E receives the payment and  Agent C receives the payment and<br>instruction to the Debtor Agent covering payment to credit the account  credits the account of the Creditor,  credits the account of Agent D.<br>of Agent (D) with their correspondent  and may optionally provide a  Agent C produces an end of day<br>(Agent C) notification e.g. credit notification. account statement report. An<br>2a optional real time notification e.g.<br>advice of credit may have also been<br>Debtor Agent (A) initiates a  3<br>Agent D receives the payment  created at the time of the credit<br>payment using the cover<br>method towards the Creditor  instruction and process the payment  5 posting<br>on to Agent E. Alternatively they may<br>Agent (E) by sending a direct  Agent B processes the payment on<br>have chosen to await until settlement<br>pacs.008 to Agent D who they  Agent C, using a correspondent<br>have business relationship with occurred in Step 6 based upon their  banking business relationship<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 347 -->
# **FI to FI Payment Status Report** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 348 -->
**==> picture [186 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.002<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


The Financial Institution To Financial Institution Payment Status Report message is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an instruction. It is also used to report on a pending instruction 

Transaction Information And Status

---

<!-- ELEMENT 349 -->
## **Customer Payment (pacs.008)** 

**==> picture [804 x 346] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pain.001<br>pain.002<br>pacs.008<br>CBPR+ restricted<br>pacs.002<br>the pacs.002 to a<br>pacs.008<br>single transaction<br>pacs.002<br>Reject &<br>pacs.004 Reason<br>pacs.002 Return &<br>Reason<br>The FIToFIPaymentStatusReport<br>message is sent by an instructed agent<br>The code list representing the  to the previous party in the payment<br>Payment Transaction Status  is part  chain. It is used to inform this party about<br>of the ISO 20022 external code list the positive or negative status of an<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 350 -->
**==> picture [803 x 252] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>A<br>Debtor Debtor Agent Creditor Agent Initiating Party* Creditor<br>pain.008**<br>pain.002<br>pacs.003<br>pacs.002<br>camt.053<br>*Initiating Party may alternative represent an authorised party such as a head office<br>**or other proprietary method for instructing a direct debit initiation request.<br>**----- End of picture text -----**<br>


The FIToFIPaymentStatusReportmessage is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an instruction. It is also used to report on a pending instruction.

---

<!-- ELEMENT 352 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 353 -->
**Min 1 – Max 1** 

## The pacs.002 message _**Creation Date**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 355 -->
**Min 1 – Max 1** 

The pacs.002 FI to FI Payment Status Report uses elements in the _**Original Group Information**_ to capture the message identifier and message name of the underlying payment the _Payment Status Report_ relates to. The mandatory _**Original Message Identification**_ contains the point-to-point reference, and the mandatory _**Original Message Name Identification**_ contains the message name of the underlying payment being reported upon. Optionally the _**Original Creation Date Time**_ can also be captured. 

**==> picture [321 x 238] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>the<br>pacs.008<br>Financial Message<br>abcd1234<br>Identification<br>Credit<br>pacs.002<br>Message<br>Group Header Identification xyz9875<br>Original Message<br>abcd1234<br>Original Group Identification<br>Information Original Message<br>**----- End of picture text -----**<br>


For example: 

_Original Message Name Identification_ “pacs.008.001.08” confirms the Status Report is of a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as “pacs.009.001.08” confirms the Status Report is of a pacs.009 Financial Institution Credit Transfer. 

**==> picture [35 x 34] intentionally omitted <==**

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 356 -->
The pacs.002 _FI to FI Payment Status Report_ also uses a number of other **Original** elements in the _**Transaction Information And Status**_ to capture information from the underlying payment that the _Payment Status Report_ relates to. 

_**Original Original Instruction End to End Identification Identification**_ 

**Mandatory** element (in addition to _Original Message identification_ and _Original Message Name Identification_ described on the previous page) include: 

_**Original End to End Identification Original UETR**_ 

**Min 1 – Max 1 Min 1 – Max 1** 

**Min 0 – Max 1 Min 0 – Max 1** Optionally _**Original Transaction Identification**_ and _**Original Instruction Identification**_ also be used. may 

_**Original Original Transaction UETR Identification**_ 

These Original elements enables the _**Instructed Agent**_ in the pacs.002 _Payment Status Report_ to associate the Payment Status with the payment they originally sent. 

_Transaction Information and Status Original Instruction Identification Original End to End Identification_

---

<!-- ELEMENT 357 -->
**Min 1 – Max 1** 

The pacs.002 _FI to FI Payment Status Report_ _**Transaction Status**_ utilizes the externalized ISO _Payment Transaction Status_ code list to provide a status update on a pacs message previously received. The _Transaction Status_ element is arguable the most significant/core parts of the pacs.002 and optionally may further be complimented with _**Status Reason Information.**_ 

**Min 0 – Max 1** 

**==> picture [50 x 50] intentionally omitted <==**

The nested _**Status Reason Information**_ enable the optional inclusion of: _**Originator**_ – the party that issues the status. Typically, the pacs.002 Instructing Agent and therefore Originator is not necessary. 

**==> picture [69 x 79] intentionally omitted <==**

_**Reason**_ – which utilizes either an ISO external Status Reason code or a proprietary reason. For example, **AC04** ‘Closed Account Number’ would compliment a RJCT (Reject) Transaction Status. 

_**Additional Information**_ – a text element to provide further status reason information, necessary where the _Reason_ code is NARR 

Note: A _**Reason**_ code must be provided where the _**Transaction Status**_ RJCT (Reject) code is used. 

The next two slides take a look at: 

- The code relevant to CBPR+ Payment Statuses, the codes description and the High Level Use Case. 

-

---

<!-- ELEMENT 358 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|ACCC|AcceptedSettlementCompleted|Settlement on the creditor's account has been completed.|Sent by**Creditor Agent**to confirm the settlement on the creditor’s account|
|ACCP|AcceptedCustomerProfile|Preceding check of technical validation was successful. Customer<br>profile check was also successful.|Sent by**any Agent**in the payment chain to confirm acceptance prior to<br>technical validation.|
|ACFC|AcceptedFundsChecked|Preceding check of technical validation and customer profile was<br>successful and an automatic funds check was positive.|Sent by**any Agent**in the payment chain to confirm the technical validation/<br>profile w as positive and automatic funds check w as positive.|
|ACIS|AcceptedandChequeIssued|Payment instruction to issue a cheque has been accepted, and the<br>cheque has been issued but not yet been deposited or cleared.|Sent by**any Agent**in the payment chain to confirm a cheque has been issued<br>as requested.|
|ACSC|AcceptedSettlementCompleted|Settlement has been completed.|Sent by the**Any Agent**to confirm settlement of a payment message leg.|
|ACSP|AcceptedSettlementInProcess|All preceding checks such as technical validation and customer<br>profile were successful and therefore the payment initiation has been<br>accepted for execution.|Sent by**any Agent**to the to confirm the payment is accepted follow ing<br>technical validations being successfully completed.|
|ACTC|AcceptedTechnicalValidation|Authentication and syntactical and semantical validation are<br>successful|Sent by**any Agent**in the payment chain to the previous Agent to confirm the<br>payment is accepted follow ing technical validations being successfully<br>completed.|
|ACWC|AcceptedWithChange|Instruction is accepted but a change will be made, such as date or<br>remittance not sent.|Sent by**any Agent**in the payment chain to the previous Agent to confirm the<br>payment is accepted follow ing amendments being made.|
|ACWP|AcceptedWithoutPosting|Payment instruction included in the credit transfer is accepted<br>without being posted to the creditor customer’s account.|Sent by**Creditor Agent**to the previous Agent to confirm the acceptance of<br>payment w ithout settlement on the creditor’s account,|
|CPUC|CashPickedUpByCreditor|Cash has been picked up by the Creditor.|Sent by**Creditor Agent**to the previous Agent to confirm that the cash<br>collection has been picked up by the Creditor,|
|PDNG|Pending|Payment initiation or individual transaction included in the payment<br>initiation is pending. Further checks and status update will be<br>performed.|Sent by**any Agent**in the payment chain to the previous Agent as an interim<br>status w hilst other validations are performed.|

---

<!-- ELEMENT 359 -->
The pacs.002 _Payment Transaction Status_ element facilitates updates to the previous Agent on changes to the status of the payment. Such Status Information messages (pacs.002), with the exception of **reject code RJCT** which **is mandatory in CBPR+** , are bilateral agreed, where upon a variety of these Transaction Statuses may be used by the Instructed Agent at different stages of the payment processing. 

This diagram illustrates the logical order in which these codes may be used during the processing of the Payment Clearing And Settlement message (pacs) and the role of the Agent in providing these status. 

**==> picture [485 x 288] intentionally omitted <==**

**----- Start of picture text -----**<br>
Any RCVD<br>Agent<br>ACTC<br>ACCP<br>ACFC<br>PDNG<br>CPUC<br>RJCT ACWC<br>ACWP Creditor<br>ACIS Agent<br>ACCC<br>ACSP<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 360 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|AC01|IncorrectAccountNumber|Format of the account number specified is not correct or Account<br>number is missing|Sent by**Instructed Agent**w hen a settlement account number is incorrect|
|AC02|InvalidDebtorAccountNumber|<br>Debtor account number invalid or missing|Sent by**Instructed Agent**w hen Debtor account number is incomplete|
|AC04|ClosedAccountNumber|<br>Account number specified has been closed on the bank of<br>account's books|Sent by**Creditor Agent**w hen the Creditor account number is closed|
|AC06|BlockedAccount|Account specified is blocked, prohibiting posting of transactions<br>against it.|Sent by**Creditor Agent**w hen Creditor account is blocked from posting<br>credit entries.<br>Sent by**Instructed Agent**w hen a settlement account is blocked|
|AC07|ClosedCreditorAccountNumber|<br>Creditor account number closed|Sent by**Creditor Agent**w hen account number is closed.<br>_CBPRplus recommend using AC04, but support AC07 to remain_<br>_interoperable with other clearing systems._|
|AC13|InvalidDebtorAccountType|Debtor account type is missing or invalid|Sent by**Instructed Agent**w hen Debtor account type element is incorrect|
|AGNT|IncorrectAgent|<br>Agent in the payment w orkflow  is incorrect|Sent by**Instructed Agent**w hen an agent in the payment transaction has<br>an incorrect identification element|
|AG01|TransactionForbidden|<br>Transaction forbidden on this type of account (formerly<br>NoAgreement)|Sent by**Instructed Agent**w hen the type of payment transaction is not<br>allow ed for the specified account|
|AG07|UnsuccesfulDirectDebit|Debtor account cannot be debited for a generic reason.<br>Code value may be used in general purposes and as a<br>replacement for AM04 if debtor bank does not reveal its<br>customer's insufficient funds for privacy reasons|Sent by**Debtor Agent**of a Direct Debit message**,**w hen debtor account<br>can not be debited|
|AM02|NotAllow edAmount|<br>Specific transaction/message amount is greater than allow ed<br>maximum|Sent by**Instructed Agent**w hen payment amount is above an allow ed<br>amount. For example the clearing system w ith a upper amount threshold|

---

<!-- ELEMENT 361 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|AM03|NotAllowedCurrency|Specified message amount is a non processable currency<br>outside ofexisting agreement|Sent by**Instructed Agent**w hen the currency of the payment is not allow ed<br>w ithin the existing business agreement|
|AM04|InsufficientFunds|Amount of funds available to cover specified message<br>amountisinsufficient.|Sent by**Instructed Agent**w hen there is not sufficient funds to settle the<br>payment transaction.|
|AM05|Duplication|Payment is a duplicate of another payment|Sent by**Instructed Agent**w hen the payment is a duplicate._CBPRplus_<br>_recommend using DUPL, but support AM05 to remain interoperable with other_<br>_clearing systems._|
|AM06|TooLowAmount|Specified transaction amount is less than agreed<br>minimum.|Sent by**Instructed Agent**w hen the payment amount is below  a minimum<br>amount.|
|AM07|BlockedAmount|Amount specified in message has been blocked by<br>regulatory authorities|Sent by**Instructed Agent**w hen the payment amount is blocked by regulators|
|AM09|WrongAmount|<br>Amount received is not the amount agreed or expected|Sent by**Instructed Agent**w hen the payment amount is incorrect|
|BE01|InconsistenWithEndCustomer|Identification of end customer is not consistent with<br>associated account number (formerly<br>CreditorConsistency).|Sent by**Creditor Agent**w hen there is an inconsistency betw een the Creditor’s<br>identification and the account number|
|BE04|MissingCreditorAddress|Specification of creditor's address, which is required for<br>payment, is missing/not correct (formerly<br>IncorrectCreditorAddress).|Sent by**Instructed Agent**w hen the Creditor’s address is missing<br>Sent by**Creditor Agent**w hen the Creditor’s address is incorrect|
|BE05|UnrecognisedInitiatingParty|Party who initiated the message is not recognised by the<br>end customer|Sent by**Creditor Agent**w hen the initiating party is unknow n to the beneficiary|
|BE07|MissingDebtorAddress|Specification of debtor's address, which is required for<br>payment, is missing/not correct.|Sent by**Instructed Agent**w hen the address of the Debtor is missing or<br>incorrect|

---

<!-- ELEMENT 362 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|BE10|InvalidDebtorCountry|Debtor country code is missing or invalid|Sent by**Instructed Agent**w hen the country code of the Debtor is missing or<br>incorrect|
|BE11|InvalidCreditorCountry|Creditor country code is missing or invalid|Sent by**Instructed Agent**w hen the country code of the Creditor is missing or<br>incorrect|
|BE16|InvalidDebtorIdentificationCode|Debtor or Ultimate Debtor identification code missing or<br>invalid|<br>Sent by**Instructed Agent**w hen the identification of the Debtor or Ultimate<br>Debtor is missing or incorrect|
|BE17|InvalidCreditorIdentificationCode|Creditor or Ultimate Creditor identification code missing<br>or invalid|<br>Sent by the**Instructed Agent**w hen the identification of the Creditor or<br>Ultimate Creditor is missing or incorrect|
|CN01|AuthorisationCancelled|Authorisation is cancelled.|Sent by**Instructed Agent**w hen a third party debit authorisation has been<br>cancelled or is not in place.|
|CNOR|Creditor bank is not registered|Creditor bank is not registered under this BIC in the<br>Clearing Settlement Mechanism (CSM)|Sent by**Instructed Agent**w hen the Creditor Agent is not reachable in the<br>Market Infrastructure (CSM) and an appropriate correspondent can not be<br>determined.|
|CURR|IncorrectCurrency|Currency of the payment is incorrect|Sent by**the Creditor Agent**w hen the**Interbank Settlement Amount**<br>Currency is not the same as the Creditor account currency and a currency<br>conversion is not accepted on the Creditor’s account.|
|CUST|RequestedByCustomer|Cancellation requested by the Debtor|Sent by**Instructed Agent**upon request by Debtor._CBPRplus recommend_<br>_using FOCR, but support CUST to remain interoperable with other clearing_<br>_systems._|
|DT01|InvalidDate|Invalid date (eg, wrong or missing settlement date)|Sent by**Instructed Agent**w hen the settlement date is in the past and an<br>agreement is in place to reject rather than apply the next possible value date.|

---

<!-- ELEMENT 363 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|DUPL|DuplicatePayment|Payment is a duplicate of another payment|Sent by**Instructed Agent**w hen the payment is a duplicate|
|ERIN|ERIOptionNotSupported|The Extended Remittance Information (ERI) option is not<br>supported.|<br>Sent by**Instructed Agent**w hen extended Remittance information (**Related**<br>**Remittance Information**) is not supported or bilaterally/multilaterally agreed|
|ED05|SettlementFailed|Settlement of the transaction has failed.|Sent by**Instructed Agent**w hen the settlement of payment has failed or been<br>unsuccessful.|
|FF03|InvalidPaymentTypeInformation|Payment Type Information is missing or invalid.<br>Generic usage if cannot specify Service Level or Local<br>Instrument code|Sent by**Instructed Agent**w hen the Payment Type Information (**Instruction**<br>**Priority**,**Clearing Channel**) provided for the payment is incorrect or not<br>supported.|
|FF04|InvalidServiceLevelCode|Service Level code is missing or invalid|Sent by**Instructed Agent**w hen the Payment Type Information**Service Level**<br>provided for the payment is incorrect or not supported|
|FF05|InvalidLocalInstrumentCode|Local Instrument code is missing or invalid|Sent by**Instructed Agent**w hen the Payment Type Information**Local**<br>**Instrument**provided for the payment is incorrect or not supported|
|FF06|InvalidCategoryPurposeCode|Category Purpose code is missing or invalid|Sent by**Instructed Agent**w hen the Payment Type Information**Category**<br>**Purpose**provided for the payment is incorrect or not supported|
|FF07|InvalidPurpose|Purpose is missing or invalid|Sent by**Instructed Agent**w hen the**Purpose**provided for the payment is<br>either missing or incorrect|
|FOCR|FollowingCancellationRequest|Return following a cancellation request|Sent by**Instructed Agent**that has accepted a payment cancellation request<br>(camt.056) and subsequently is rejecting the unsettled payment instruction.|
|FR01|Fraud|Returned as a result of fraud.|Sent by**Instructed Agent**w hen the payment is identified as fraudulent.|

---

<!-- ELEMENT 364 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|MD02|MissingMandatoryInformationIn<br>Mandate|<br>Mandate related information data required by the<br>scheme is missing.|Sent by**Instructed Agent**w hen information required by the clearing scheme<br>is missing.|
|MD05|CollectionNotDue|Creditor or creditor's agent should not have collected the<br>direct debit|<br>Sent by**Instructed Agent**w hen a Direct Debit collection w as not due|
|MD07|EndCustomerDeceased|End customer is deceased.|Sent by**Creditor Agent**w hen the Creditor or Ultimate Creditor is deceased|
|MS02|NotSpecifiedReasonCustomer<br>Generated|Reason has not been specified by end customer|Sent by**Creditor Agent**w here instructed to reject by the Creditor, but no<br>reason w as specified|
|MS03|NotSpecifiedReasonAgent<br>Generated|Reason has not been specified by agent.|Sent by**Instructed Agent**but no reason is specified|
|NARR|Narrative|Reason is provided as narrative information in the<br>additional reason information.|Sent by**Instructed Agent**the reason is provided as narrative information.<br>**Only to be used where no other code is appropriate!**(i.e. exceptional<br>circumstances)|
|NOAS|NoAnswerFromCustomer|No response from Beneficiary|Sent by**Instructed Agent**w hen the Creditor did not respond to query for<br>additional information in order that the payment could be credited e.g. currency<br>control documentation.|
|NOCM|Not compliant (more generic)|Customer account is not compliant with regulatory<br>requirements, for example FICA (in South Africa) or any<br>other regulatory requirements which render an account<br>inactive for certain processing.|Sent by**Instructed Agent**w hen the Creditor account is not compliant w ith<br>certain regulatory requirements.|
|RC01|BankIdentifierIncorrect|<br>Bank Identifier code specified in the message has an<br>incorrect format (formerly<br>IncorrectFormatForRoutingCode).|Sent by**Instructed Agent**w hen an incorrect BIC has been used in the<br>payment|

---

<!-- ELEMENT 365 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|RC04|InvalidCreditorBankIdentifier|Creditor bank identifier is invalid or missing|Sent by**Instructed Agent**w hen the Creditor Agent identification is incorrect or<br>missing|
|RC08|InvalidClearingSystemMemberIden<br>tifier|ClearingSystemMemberidentifier is invalid or missing.<br>Generic usage if cannot specify between debit or credit<br>account|<br>Sent by**Instructed Agent**w hen the clearing system member identification for<br>an Agent is incorrect|
|RC11|InvalidIntermediaryAgent|Intermediary Agent is invalid or missing|Sent by**Instructed Agent**w hen the intermediary agent identification is<br>incorrect|
|RF01|NotUniqueTransactionReference|Transaction reference is not unique within the<br>message.|Sent by**Instructed Agent**w hen the transaction reference (UETR and<br>Instruction Identification) are not unique|
|RR01|Missing Debtor Account or<br>Identification|Specification of the debtor’s account or unique<br>identification needed for reasons of regulatory<br>requirements is insufficient or missing|Sent by**Instructed Agent**w hen the Debtor identification or debtor account is<br>missing, or the information provided are not sufficient|
|RR02|Missing Debtor Name or Address|<br>Specification of the debtor’s name and/or address needed for<br>regulatory requirements is insufficient or missing.|<br>Sent by **Instructed Agent**since the Debtor name or Address is missing, or<br>information provided is not sufficient|
|RR03|Missing Creditor Name or Address|Specification of the creditor’s name and/or address needed<br>for regulatory requirements is insufficient or missing.|Sent by**Instructed  Agent**since the Creditor name or Address is missing, or<br>information provided is not sufficient|
|RR04|Regulatory Reason|Regulatory Reason|Sent by**Instructed Agent**due to any unspecified regulatory reason|
|RR05|RegulatoryInformationInvalid|Regulatory or Central Bank Reporting information missing,<br>incomplete or invalid.|Sent by**Instructed Agent**w hen the reporting information required by the<br>central bank or reporting authority is missing or not complete|

---

<!-- ELEMENT 366 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|RR07|RemittanceInformationInvalid|Remittance information structure does not comply w ith rules<br>for payment type.|Sent by **Instructed Agent**since the remittance information is incorrect|
|RR08|RemittanceInformationTruncated|Remittance information truncated to comply w ith rules for<br>payment type.|Sent by **Instructed Agent**w here the Structured Remittance Information<br>has not been bilaterally or multilaterally agreed, w hich or has resulted in<br>truncation|
|RR09|InvalidStructuredCreditorReference|Structured creditor reference invalid or missing.|Sent by **Instructed Agent**w hen the structure of the creditor reference in<br>the remittance information is invalid or missing|
|RR11|InvalidDebtorAgentServiceID|Invalid or missing identification of a bank proprietary service.|Sent by **Instructed Agent**w here the proprietary identification for the Debtor<br>is invalid or not understood|
|RR12|InvalidPartyID|Invalid or missing identification required w ithin a particular<br>country or payment type.|Sent by**Instructed Agent**w here a proprietary party identification is<br>considered invalid or not understood|
|RUTA|ReturnUponUnableToApply|Return following investigation request and no remediation<br>possible.|Sent by**Instructed  Agent**that is unsatisfied w ith the outcome of the unable<br>to apply request and is subsequently rejecting the payment instruction.<br>Alternatively it can be used by the original**Creditor Agent**w hen the creditor<br>is unable to apply the transaction|
|TM01|Invalid Cut off time|Associated message, payment information block, or<br>transaction was received after agreed processing cut-off<br>time.|Sent by**Instructed  Agent**w hen the message w as received after the<br>agreed processing cut off time and an agreement is in place to reject rather<br>than apply the next possible value date.|

---

<!-- ELEMENT 367 -->
Definitions and High Level Use Cases 

**Code Name ISO Definition High Level Use Case** In a FIToFI Customer Credit Transfer: Credit to the creditor’s account is pending, status Originator is waiting Optionally sent by **the Creditor Agent** w ent the cover has not been settled at G004 CreditPendingFunds for funds provided via a cover. Update will follow from the the creditor agent account at the reimbursement agent Status Originator.

---

<!-- ELEMENT 368 -->
**Min 0 – Max 1** 

The pacs.002 _FI to FI Payment Status Report_ optional _**Effective Interbank Settlement Date**_ allows a choice of _**Date**_ or _**Date Time**_ to confirm when a point-to-point transaction is completed/effected. 

When _**Date Time**_ is chosen CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [11 x 4] intentionally omitted <==**

---

<!-- ELEMENT 369 -->
**==> picture [645 x 252] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>Instructing Instructed<br>Agent: Agent A Agent: Agent B<br>Instructing Instructed<br>Agent: Agent B Agent: Agent C<br>pacs.008<br>pacs.004<br>pacs.008 Instructing Agent<br>Instructed Instructing pacs.002<br>Agent: Agent A Agent: Agent B<br>Instructed Instructing<br>Agent: Agent B Agent: Agent C leg.<br>**----- End of picture text -----**<br>


**==> picture [61 x 61] intentionally omitted <==**

_**Instructing Agent**_ and _**Instructed Agent**_ represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment leg. 

**==> picture [47 x 48] intentionally omitted <==**

_Instructing Agent_ and _Instructed Agent_ elements are required in all pacs messages 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Transfer Transaction Information_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 370 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

## **Serial Financial Institution to Financial Institution to Customer Credit Transfer** 

Use Case p.2.1.1 – High Level Payment Status Information (pacs.002) of multiple Payment Transaction Status updates Use Case p.2.1.2 – High Level Rejection of an incomplete Customer Credit Transfer (pacs.008) **Serial Financial Institution Credit Transfer** 

Use Case p.2.2.1 – High Level Rejection of an incomplete Financial Institution Credit Transfer (pacs.009) **Cover Method Financial Institution to Financial Institution to Customer Credit Transfer** 

Use Case p.2.3.1.a – High Level Rejection of an incomplete payment using the cover method Use Case p.2.3.1.b – High Level Rejection of an incomplete payment using the cover method **Financial Institution Direct Debit** 

Use Case p.2.4.1 – High Level Status Information of a Financial Institution Direct Debit Use Case p.2.4.2 – High Level Rejection of a Financial Institution Direct Debit **Financial Institution to Financial Institution Customer Direct Debit** Use Case p.2.5.1 – High Level FI to FI Customer Direct Debit (pacs.003) successful settlement Use Case p.2.5.2 – High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement

---

<!-- ELEMENT 371 -->
## **Transaction Status updates** 

An agent may provide multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle i.e. from receipt through to onward processing. 

**==> picture [788 x 266] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 5<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>pacs.002 3<br>pacs.002 4<br>1<br>Debtor initiates a payment<br>instruction to the Debtor Agent 3 4 5<br>Agent B provides a further status<br>Agent B provides a status update<br>Agent B processes the payment<br>update ACSP (accepted<br>ACTC (accepted technical<br>on Agent C<br>2 validations are successful) to  settlement in progress) to Agent<br>A, based upon a bilateral<br>Debtor Agent (A) initiates a  Agent A, based upon a bilateral<br>agreement.<br>serial payment towards the  agreement.<br>Creditor Agent (D) using<br>Agents B & C as intermediaries<br>Where a  payment is rejected , the use of the pacs.002<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 372 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4<br>pacs.008 pacs.008 pacs.008<br>A pacs.004 B pacs.004 C pacs.002 D<br>6 5<br>+ Return  + Return  + Reject<br>Reason  Reason  Reason<br>1 3<br>5<br>Debtor initiates a payment  Agent B processes the payment  Having received the payment Agent  Agent C return funds to Agent B,<br>instruction to the Debtor Agent on Agent C D recognises the payment can not  together with the reason code for<br>be completed as requested e.g. the  return.<br>Creditor’s account is closed. Agent<br>2 D rejects the payment to Agent C<br>4 6<br>using a Status information message<br>Debtor Agent (A) initiates a  Agent B return funds to Agent A,<br>Agent C processes the payment  (pacs.002) also including the return<br>serial payment towards the  together with the reason code for<br>Creditor Agent (D) using  on Agent D reason code. return.<br>Agents B & C as intermediaries<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 373 -->
**(pacs.009)** 

**==> picture [647 x 137] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3<br>pacs.009 pacs.009<br>A B<br>pacs.004 C pacs.002 D E<br>5 4<br>+ Return  + Reject<br>Reason  Reason<br>**----- End of picture text -----**<br>


**==> picture [367 x 175] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2<br>Agent A as the Debtor initiates<br>Agent C processes the<br>a payment instruction to the<br>payment onto Agent D<br>Debtor Agent (Agent B)<br>2<br>Debtor Agent (B) debits the<br>account of Agent A and<br>initiates a serial payment<br>towards the Creditor (Agent E)<br>using Agents C as an<br>intermediary.<br>**----- End of picture text -----**<br>


4 Having received the payment Agent Agent C return funds to Agent B, D recognises the payment can not together with the reason code for be completed as requested e.g. the return. Creditor’s account is closed. Agent D rejects the payment to Agent C 5 using a Status Information message Agent B advises Agent A of the return (pacs.002) also including the reject of payment together with the reason code. using the camt.053 and may optionally provide a notification e.g. credit notification.

---

<!-- ELEMENT 374 -->
**==> picture [851 x 374] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2a<br>pacs.008<br>A pacs.002 D<br>6b<br>2b<br>1<br>+ Reject<br>Debtor initiates a payment  post-settlement returns see<br>Reason  pacs.004 use case p.4.3.1.a<br>instruction to the Debtor Agent<br>5 and p.4.3.1.b<br>3 4<br>2a<br>pacs.009 cov<br>Debtor Agent (A) initiates a  + Return  8<br>payment using the cover method  Reason  B pacs.004 C 6b<br>to the Creditor Agent (D) 7<br>Agent D requests the return of covering<br>+ Return  funds, together with the reason for<br>+ Return<br>2b Reason  return, having already rejected the<br>In parallel the Debtor Agent (A) initiates a covering  Reason  pacs.008<br>payment to credit the account of Agent (D) with their  4<br>correspondent (Agent C) 3<br>Agent B processes the  Agent C receives the payment  7<br>payment on Agent C and credits the account of  Agent C return of covering funds to<br>Agent D Agent B, together with the reason code<br>Having received the payment with settlement method  for return.<br>COVE Agent D recognises (prior to the settlement via  5<br>pacs.009 COV) the payment can not be completed as<br>Agent C produces an end of day account statement report.  8<br>requested e.g. the Creditor’s account is closed. Agent  An optional real time notifications e g credit notification Agent B return of covering funds to<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 375 -->
**==> picture [851 x 371] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2a<br>pacs.008<br>A pacs.002 D<br>2b 5<br>1<br>+ Reject<br>Debtor initiates a payment<br>instruction to the Debtor Agent Reason<br>3 4<br>2a post-settlement return see<br>pacs.009 cov<br>pacs.004 use case p.4.3.1.a<br>Debtor Agent (A) initiates a  + Return  7<br>payment using the cover method  Reason  B pacs.004 C<br>to the Creditor Agent (D) 6 5<br>Having not settled the pacs.009 cov<br>+ Return  Agent D rejects the covering funds,<br>2b<br>Reason  together with the reason for rejection.<br>In parallel the Debtor Agent (A)  4<br>initiates a covering payment to   6<br>Agent C receives the payment and credits their internal account with Agent D.<br>Agent (D) as the Creditor of the  Agent C returns the settled covering<br>Agent C forwards a pacs.009 cov with Settlement Method INDA (indicating<br>pacs.009 cov funds to Agent B, together with the<br>Agent D is responsible for the settlement of this leg of the payment transaction.<br>reason code for return.<br>7<br>3<br>Having received the payment Agent D recognises the payment can not be  Agent C returns the settled covering<br>Agent B processes the payment  completed as requested e.g. the Creditor’s account is closed. Having not funds to Agent B, together with the<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 376 -->
## **(pacs.010)** 

**==> picture [677 x 306] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>pacs.010<br>1a pacs.002<br>A B pacs.009 pacs.009 camt.053 E<br>C D<br>2<br>3 4<br>1 2 4<br>Agent E initiates a Direct Debit Debtor Agent (B) initiates a  Agent D credits the account of the<br>instruction to debit Agent A’s  serial payment towards the  Creditor (Agent E), and may<br>account Creditor Agent (E) using  optionally provide a notification<br>Agents B & C as intermediaries e.g. credit notification in addition to<br>an account statement (camt.053)<br>3<br>1a<br>Agent B provides a positive  Agent C processes the payment<br>status update to Agent E on Agent D<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 377 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>pacs.010<br>pacs.002<br>A B E<br>C D<br>1<br>Agent D initiates a Direct Debit<br>instruction to debit Agent A’s<br>account<br>Debtor Agent (B) rejects the<br>instruction, using a pacs.002,<br>as no mandate agreement is in<br>place.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 378 -->
**==> picture [632 x 124] intentionally omitted <==**

**----- Start of picture text -----**<br>
3 2 1<br>pacs.003 pain.008<br>camt.053<br>B pacs.002 A pain.002<br>4<br>Settlement<br>Complete<br>**----- End of picture text -----**<br>


**==> picture [430 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 3<br>Creditor initiates a direct debit  The Debtor Agent debits the account<br>of the Debtor, and may optionally<br>instruction to the Creditor Agent<br>provide a notification e.g. debit<br>notification in addition to an account<br>2 statement (camt.053). The Debtor<br>Creditor Agent (A) initiates a  Agent also provides a status update<br>direct debit collection by  ACSC (accepted settlement<br>sending a pacs.003 message to  completed) to the Creditor Agent.<br>the Debtor Agent with the<br>settlement method “INDA”<br>**----- End of picture text -----**<br>


**==> picture [225 x 72] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>Creditor Agent (A) relays the status<br>ACSC (accepted settlement<br>completed) to the Initiating Party,<br>based upon a bilateral agreement<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 379 -->
**==> picture [68 x 97] intentionally omitted <==**

**==> picture [182 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>Creditor initiates a direct debit<br>instruction to the Creditor Agent<br>2<br>Creditor Agent (A) initiates a<br>direct debit collection by<br>sending a pacs.003 message to<br>the Debtor Agent with the<br>settlement method “INDA”<br>**----- End of picture text -----**<br>


**==> picture [482 x 276] intentionally omitted <==**

**----- Start of picture text -----**<br>
3 2 1<br>pacs.003 pain.008<br>B pacs.002 A pain.002<br>4<br>Reject<br>Reason<br>3 4<br>Creditor Agent (A) relays the status<br>RJCT (Rejected) to the Initiating<br>The Debtor Agent fails to debit the<br>Party with the rejection reason<br>account of the Debtor (e.g., account<br>information<br>is closed). The Debtor Agent<br>provides a status update RJCT<br>(Rejected) with the rejection reason<br>information.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 380 -->
# **Payment Return** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 381 -->
**pacs.008 pacs.009 cov** Group Header Group Header 

Credit Transfer Credit Transfer Transaction Transaction Information Information Underlying Customer Credit 

**pacs.004** Group Header 

Transaction Information Original Group Information Original Transaction 

In a similar structure to the pacs.009 (cov) underlying Customer Credit Transfer, the pacs.004 Payment Return message has amongst other elements Original Group Information which captures original information such as the Original UETR and Original Interbank Settlement Amount etc. and an Original Transaction Reference which contain the key elements of the original payment e.g. Debtor, Creditor etc.

---

<!-- ELEMENT 382 -->
## **FI Customer Payment (pacs.008)** 

**==> picture [466 x 276] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pacs.008<br>pacs.002<br>pacs.008<br>pacs.002<br>Reject &<br>pacs.004<br>Reason<br>Return &<br>pacs.002<br>Reason<br>**----- End of picture text -----**<br>


**==> picture [181 x 69] intentionally omitted <==**

The PaymentReturn message is sent by an agent to the previous agent in the payment chain to undo a payment previously settled.

---

<!-- ELEMENT 384 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender’s Reference (Field could be considered a similar where a contains a 20) comparison pacs message single Transaction. 

**==> picture [60 x 60] intentionally omitted <==**

Each transaction’s _Credit Transfer Transaction Information_ contains a variety of nested _Payment Identification_ elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference) 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 385 -->
**Min 1 – Max 1** 

## The pacs.004 message _**Creation Date**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 386 -->
## **Min 1 – Max 1** 

The pacs.004 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 387 -->
## **Min 1 – Max 1** 

The pacs.004 _**Settlement Method**_ element within the Group Header _**Settlement Information**_ , includes one of the embedded codes to indicate how the payment message will be settled. 

The _**Settlement Method**_ element in the pacs.004 allows a choice of an embedded code. 

**==> picture [28 x 28] intentionally omitted <==**

**----- Start of picture text -----**<br>
$<br>€<br>**----- End of picture text -----**<br>


**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated _**Settlement Account**_ element. 

**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated _**Settlement Account**_ element. 

**==> picture [60 x 47] intentionally omitted <==**

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in

---

<!-- ELEMENT 388 -->
The pacs.004 message _**Settlement Account**_ is a nested element as part of _**Settlement Information,**_ this element identifies information related to an account used to settle the payment instruction. 

**Min 0 – Max 1** The _**Settlement Account**_ identifies the account details maintained at the account institution for the settlement of the instruction as servicing (Agent responsible indicated in the _**Settlement Method**_ ) 

**==> picture [80 x 84] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 390 -->
## **Min 0 – Max 1** 

The pacs.004 message _**Return Identification**_ captures a point-to-point reference used to unambiguously identify the Payment Return message, created by the _**Instructing Agent**_ in the _**Return Chain**_ . 

**==> picture [102 x 79] intentionally omitted <==**

The 35 character return identifier could be considered similar to the legacy Sender’s Reference (Field 20) of an MT return payment message.

---

<!-- ELEMENT 391 -->
**Min 0 – Max 1** 

The pacs.004 _Payment Return_ uses elements in the _**Original Group Information**_ to capture the message identifier and name of the the _Return_ relates to. The message underlying payment _Payment_ mandatory _**Original Message Identification**_ contains the point-to-point reference, and the mandatory _**Original Message Name Identification**_ contains the message name of the underlying payment being returned. Optionally the _**Original Creation Date Time**_ can also be captured. 

**==> picture [322 x 238] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>the<br>pacs.008<br>Institution Message<br>abcd1234<br>the Identification<br>pacs.004<br>Message<br>Group Header Identification xyz9875<br>Original Message<br>abcd1234<br>Original Group Identification<br>Information Original Message<br>**----- End of picture text -----**<br>


For example: 

_Original Message Name Identification_ “pacs.008.001.xx” confirms the return is of a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as “pacs.009.001.xx” confirms the return is of a pacs.009 Financial Institution Credit Transfer. 

**==> picture [35 x 34] intentionally omitted <==**

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 392 -->
**Min 1 – Max 1** 

The pacs.004 _Payment Return_ also uses a number of other **Original** elements in the _**Transaction Information**_ to capture information from the underlying payment that the _Payment Return_ relates to. **Mandatory** element examples of this (in addition to _Original Message identification_ and _Original Message Name Identification_ described on the previous page) include: 

**==> picture [233 x 238] intentionally omitted <==**

**----- Start of picture text -----**<br>
Original<br>End to End Original<br>UETR<br>Identification<br>Original  Original<br>Interbank  Interbank<br>Settlement Settlement<br>Date Amount<br>**----- End of picture text -----**<br>


These Original elements enables the _**Instructed Agent**_ in the pacs.004 _Payment Return_ to re-associate the Return with the payment they originally sent. 

**==> picture [11 x 11] intentionally omitted <==**

_Transaction Information_ 

_Original End to end Identification Original UETR_

---

<!-- ELEMENT 393 -->
## **Settlement Date** 

**$** 

**Min 1 – Max 1** 

**Min 1 – Max 1 Min 1 – Max 1** The _**Returned Interbank Settlement Amount**_ and subsequent _**Interbank Settlement Date**_ are mandatory elements in the pacs.004 _Payment Return,_ these elements are used to capture the currency and amount being returned together with the settlement date of the Payment Return. 

**==> picture [60 x 60] intentionally omitted <==**

The _**Returned Interbank Settlement Amount**_ may be a different amount than the _**Original Interbank Settlement Amount**_ (amount received the Agent instructing the _Payment Return_ ) for example a charge may have been levied for processing the _Payment Return_ or the Payment Return is a partial amount for overpayment or partial refund In this case the _**Returned Instructed Amount**_ should be equal to the _**Interbank Settlement Amount,**_ on the first leg of the _Payment Return._ Charge levied should also be captured in the _**Charge Information**_ element. 

**==> picture [11 x 11] intentionally omitted <==**

_Transaction Information_ 

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 394 -->
The pacs.004 message has two optional elements to capture the optional information related to the settlement of the instructions. 

**Min 0 – Max 1** 

**==> picture [59 x 54] intentionally omitted <==**

The _**Settlement Priority**_ provides an optional choice of embedded codes to indicate the instruction’s settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the _**Settlement Method**_ and should not be confused with the _**Instruction Priority.**_ 

**==> picture [36 x 34] intentionally omitted <==**

Note: Where the _**Settlement Method**_ of the pacs.004 is ‘INDA’ (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code ‘INGA’ implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary. 

**==> picture [59 x 68] intentionally omitted <==**

**Min 0 – Max 1** 

The _**Settlement Time Indication**_ optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure. 

This DateTime can be captured in two nested elements, _**Debit Date Time**_ and _**Credit Date Time**_ . 

**==> picture [10 x 5] intentionally omitted <==**

---

<!-- ELEMENT 395 -->
**$100** 

**Min 0 – Max 1** The _**Returned Instructed Amount**_ captures currency and amount instructed by the _**Debtor**_ in the _**Return Chain**_ . This conditional element is required when the _**Returned Interbank Settlement Amount**_ is not the same currency and/or amount as originally instructed by the _Debtor._ For example a charge is taken or the transactions is converted to another currency. 

**==> picture [44 x 44] intentionally omitted <==**

**----- Start of picture text -----**<br>
£<br>**----- End of picture text -----**<br>


**==> picture [44 x 44] intentionally omitted <==**

**----- Start of picture text -----**<br>
¥<br>**----- End of picture text -----**<br>


**Min 0 – Max 1** 

The _**Exchange Rate**_ capture the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency. 

**==> picture [10 x 5] intentionally omitted <==**

---

<!-- ELEMENT 396 -->
**Min 1 – Max 1** 

The pacs.004 _**Charge Bearer**_ element uses an embedded code that is used to specify which party/parties would bear associated with the transaction. This element is any charges processing payment comparable with MT Field 71A ‘Details of Charges’ 

**Charge Code Description Bearer** CRED Creditor **(1.1)** SHAR Shared **71A: Details Code Description of Charges** BEN Beneficiar y SHA Shared Charges 

**==> picture [65 x 53] intentionally omitted <==**

**==> picture [61 x 63] intentionally omitted <==**

Note: _Charge Bearer_ code DEBT (implying the _**Return Chain,**_ **Debtor** will bear any charges) is removed from the CBPR+ pacs.004. Should a non-CBPR+ Payment Return be received with Charge Bearer DEBT, it is recommended to use SHAR in any onward processed Payment Return.

---

<!-- ELEMENT 397 -->
**Min 0 – Max 1** 

**Min 0 – Max *** 

The _**Charges Information**_ element provides information on the return charges to be paid by the _**Charge Bearer**_ . This element is comparable with MT Fields: 71F ‘Senders Charges’ and 71G ‘Receiver’s Charges’, although pre-paid charges (legacy 71G ‘Receiver’s Charges’ are an unlikely use case for Payment Returns 

**Charge** Amount **Information** Currenc y **(0.*)** Agent BICFI Name Structured Postal Address 

In addition to the legacy MT message the pacs.004 _Charge Information_ mandate the _Agent,_ this represent the Agent who has taken a charge (deduct from the transaction) CBPR+ best practice recommends the use of the structured Agent BIC. 

As the _**Charges Information**_ element is repetitive it can capture charges related to previous legs of the Payment Return transaction chain. 

**==> picture [61 x 63] intentionally omitted <==**

Note: _Charge Information_ element is required where a charge is taken on the Payment Return. A charge for returning an incomplete payment by the originator of the Payment Return (Return Chain Debtor) is common practice. It is encouraged that Agents who processed the original payment transaction consider the total operation cost when defining their payment cost recovery model. Whereby further charges on Return Payments should be avoided. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 398 -->
**==> picture [688 x 272] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>Instructing Instructed<br>Agent: Agent A Agent: Agent B<br>Instructing Instructed<br>Agent: Agent B Agent: Agent C<br>pacs.008 Instructing Instructed<br>Agent: Agent C Agent: Agent D<br>pacs.004<br>pacs.008<br>pacs.008<br>Instructed Instructing pacs.004<br>Agent: Agent A Agent: Agent B pacs.002<br>Instructed Instructing<br>Agent: Agent B Agent: Agent C<br>Instructed Instructing<br>Agent: Agent C Agent: Agent D<br>Instructing Agent  and  Instructed Agent<br>**----- End of picture text -----**<br>


_**Instructing Agent**_ and _**Instructed Agent**_ represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [10 x 10] intentionally omitted <==**

_Transaction Information_

---

<!-- ELEMENT 399 -->
**Min 1 – Max 1** 

The mandatory _**Return Chain**_ element captures all the parties involved in the return transaction, in much the same way the underlying payment message captures all the parties involved in a payment. 

In this element the **role** of the various parties **change** , to reflect the fact the payment is now a _Payment Return,_ for example, the _Creditor Agent_ of the underlying payment may become the _Debtor Agent_ of the _Payment Return_ . 

Although Ultimate Debtor and Ultimate Creditor are present in the Return chain it is extremely unlikely one of these Parties would be involved in the return chain and can only do so if present as an Ultimate Party in the original payment. 

**==> picture [795 x 194] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E<br>Debtor Debtor Agent Previous Instructing  Previous Instructing  Instructing Agent Instructed Agent &  Creditor<br>Agent 1 Agent 2 Creditor Agent<br>A B C D E<br>Creditor Creditor Agent Intermediary Intermediary Instructed Agent  Debtor Agent & Debtor<br>Agent 2 Agent 1 Instructing Agent<br>original<br>return chain<br>**----- End of picture text -----**<br>


Note: the static Previous Instructing Agent roles in the original payment transition to

---

<!-- ELEMENT 400 -->
Arguably the most common example of a Payment Return is where it is initiated by the Creditor Agent of the original payment, this Agent’s role the become the mandatory Debtor in the _**Return Chain**_ element (as they owe the money to the party the return is intended for). 

Recognising that the original Creditor is not party to the return, for example, they might be a known customer of the original Creditor Agent whereby a reject or return code ‘AC01’ may be used. In this way the original Creditor was not involved in the Payment Return. 

**==> picture [795 x 194] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E<br>Debtor Debtor Agent Previous Instructing Previous Instructing Instructing Agent Instructed Agent &  Creditor<br>Agent 1 Agent 2 Creditor Agent<br>A B C D E<br>Creditor Creditor Agent Intermediary Agent 2 Intermediary Agent 1 Debtor Agent & Debtor &<br>Instructed Agent Instructing Agent<br>original<br>return chain<br>**----- End of picture text -----**<br>


**==> picture [23 x 19] intentionally omitted <==**

Note: the static Previous Instructing Agent roles in the original payment transition to Intermediary

---

<!-- ELEMENT 401 -->
Various other Payment Return use cases exist where the common principal is the initiator of the Payment Return becomes the mandatory Debtor in the _**Return Chain**_ element (as they owe the money to the party the return is intended for). And the mandatory Creditor in the _**Return Chain**_ element is the party the payment is being returned to. 

**==> picture [795 x 195] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E<br>Debtor Debtor Agent Instructing Agent Instructed Agent Intermediary Agent 1 Creditor Agent Creditor<br>A B C<br>Creditor Creditor Agent Debtor Agent & Debtor &<br>Instructed Agent Instructing Agent<br>original<br>return chain<br>**----- End of picture text -----**<br>


**==> picture [36 x 33] intentionally omitted <==**

Note: a party Rejecting the payment using a pacs.002 would not be considered to be involved in

---

<!-- ELEMENT 402 -->
- **Min 1 – Max 1** 

- The _**Return Reason Information**_ element captures detailed information on the return reason. Within this element: 

## ? 

- the _**Originator**_ element helps identify the party who initiated the request to return the payment. This party would have been included in the underlying payment and may also be included the pacs.004 _Return Chain._ 

- the _**Reason**_ is mandatory and is represented by an externalised _**Code**_ choice ( ) 

- the _**Additional Information**_ element also be included to further details on the may provide 

- reason for return. 

**==> picture [48 x 47] intentionally omitted <==**

The code list representing the _Return Reason_ is part of the ISO 20022 external code list 

**==> picture [11 x 10] intentionally omitted <==**

**==> picture [10 x 11] intentionally omitted <==**

_Transaction Information     Return Reason Information_ 

_Originator_

---

<!-- ELEMENT 403 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|AC01|IncorrectAccountNumber|Format of the account number specified is not correct or<br>Account number is missing|Sent by**any Agent**w hen a settlement account number is incorrect|
|AC02|InvalidDebtorAccountNumber|<br>Debtor account number invalid or missing|Sent by**any Agent**w hen Debtor account number is incomplete|
|AC04|ClosedAccountNumber|Account number specified has been closed on the bank of<br>account's books|Sent by**Creditor Agent**w hen the Creditor account number is closed|
|AC06|BlockedAccount|Account specified is blocked, prohibiting posting of transactions<br>against it.|Sent by**Creditor Agent**w hen Creditor account is blocked from posting credit<br>entries.<br>Sent by**any Agent**w hen a settlement account is blocked|
|AC07|ClosedCreditorAccountNumber|Creditor account number closed|Sent by**Creditor Agent**w hen account number is closed.<br>_CBPRplus recommend using AC04, but support AC07 to remain interoperable_<br>_with other clearing systems._|
|AC13|InvalidDebtorAccountType|Debtor account type is missing or invalid|Sent by**any Agent**w hen Debtor account type element is incorrect|
|AGNT|IncorrectAgent|Agent in the payment w orkflow  is incorrect|Sent by**any Agent**w hen an agent in the payment transaction has an incorrect<br>identification element|
|AG01|TransactionForbidden|Transaction forbidden on this type of account (formerly<br>NoAgreement)|Sent by**any Agent**w hen the type of payment transaction is not allow ed for the<br>specified account|
|AG07|UnsuccesfulDirectDebit|Debtor account cannot be debited for a generic reason.<br>Code value may be used in general purposes and as a<br>replacement for AM04 if debtor bank does not reveal its<br>customer's insufficient funds for privacy reasons|Sent by**Debtor Agent**of a Direct Debit message**,**w hen debtor account can not<br>be debited.|
|AM02|NotAllow edAmount|<br>Specific transaction/message amount is greater than allow ed<br>maximum|Sent by**any Agent**w hen payment amount is above an allow ed amount. For<br>example the clearing system w ith a upper amount threshold.|

---

<!-- ELEMENT 404 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|AM03|NotAllowedCurrency|Specified message amount is a non processable currency<br>outside ofexisting agreement|Sent by**any Agent**w hen the currency of the payment is not allow ed w ithin the<br>existing business agreement|
|AM04|InsufficientFunds|Amount of funds available to cover specified message<br>amountisinsufficient.|Sent by**any Agent**w hen there is not sufficient funds to settle the payment<br>transaction.|
|AM05|Duplication|Payment is a duplicate of another payment|Sent by**any Agent**w hen the payment is a duplicate._CBPRplus recommend_<br>_using DUPL, but support AM05 to remain interoperable with other clearing_<br>_systems._|
|AM06|TooLowAmount|Specified transaction amount is less than agreed<br>minimum.|Sent by**any Agent**w hen the payment amount is below  a minimum amount.|
|AM07|BlockedAmount|Amount specified in message has been blocked by<br>regulatory authorities|Sent by**any Agent**w hen the payment amount is blocked by regulators|
|AM09|WrongAmount|<br>Amount received is not the amount agreed or expected|Sent by**any Agent**w hen the payment amount is incorrect|
|BE01|InconsistenWithEndCustomer|Identification of end customer is not consistent with<br>associated account number (formerly<br>CreditorConsistency).|Sent by**Creditor Agent**w hen there is an inconsistency betw een the Creditor’s<br>identification and the account number|
|BE04|MissingCreditorAddress|Specification of creditor's address, which is required for<br>payment, is missing/not correct (formerly<br>IncorrectCreditorAddress).|Sent by**any Agent**w hen the Creditor’s address is missing<br>Sent by**Creditor Agent**w hen the Creditor’s address is incorrect|
|BE05|UnrecognisedInitiatingParty|Party who initiated the message is not recognised by the<br>end customer|Sent by**Creditor Agent**w hen the initiating party is unknow n to the beneficiary|
|BE07|MissingDebtorAddress|Specification of debtor's address, which is required for<br>payment, is missing/not correct.|Sent by**any Agent**w hen the address of the Debtor is missing or incorrect|

---

<!-- ELEMENT 405 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|BE10|InvalidDebtorCountry|Debtor country code is missing or invalid|Sent by**any Agent**w hen the country code of the Debtor is missing or incorrect|
|BE11|InvalidCreditorCountry|Creditor country code is missing or invalid|Sent by**any Agent**w hen the country code of the Creditor is missing or<br>incorrect|
|BE16|InvalidDebtorIdentificationCode|Debtor or Ultimate Debtor identification code missing or<br>invalid|<br>Sent by**any Agent**w hen the identification of the Debtor or Ultimate Debtor is<br>missing or incorrect|
|BE17|InvalidCreditorIdentificationCode|Creditor or Ultimate Creditor identification code missing<br>or invalid|<br>Sent by the**any Agent**w hen the identification of the Creditor or Ultimate<br>Creditor is missing or incorrect|
|CN01|AuthorisationCancelled|Authorisation is cancelled.|Sent by**any Agent**w hen a third party debit authorisation has been cancelled<br>or is not in place.|
|CNOR|Creditor bank is not registered|Creditor bank is not registered under this BIC in the<br>Clearing Settlement Mechanism (CSM)|Sent by**any Agent**w hen the Creditor Agent is not reachable in the Market<br>Infrastructure (CSM) and an appropriate correspondent can not be determined.|
|CURR|IncorrectCurrency|Currency of the payment is incorrect|Sent by the **Creditor Agent**w hen the**Interbank Settlement Amount**<br>Currency is not the same as the Creditor account currency and a currency<br>conversion is not accepted on the Creditor’s account.|
|CUST|RequestedByCustomer|Cancellation requested by the Debtor|Sent by**any Agent**upon request by Debtor._CBPRplus recommend using_<br>_FOCR, but support CUST to remain interoperable with other clearing systems._|
|DT01|InvalidDate|Invalid date (eg, wrong or missing settlement date)|Sent by**any Agent**w hen the settlement date is in the past and an agreement<br>is in place to reject rather than apply the next possible value date.|
|DT04|FutureDateNotSupported|Future date not supported|Sent by**any Agent**w hen a future settlement date is not supported or appear to<br>be an error e.g. is the w rong year.|

---

<!-- ELEMENT 406 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|DUPL|DuplicatePayment|Payment is a duplicate of another payment|Sent by**any Agent**w hen the payment is a duplicate|
|ERIN|ERIOptionNotSupported|The Extended Remittance Information (ERI) option is not<br>supported.|<br>Sent by**any Agent**w hen extended Remittance information (**Related**<br>**Remittance Information**) is not supported or bilaterally/multilaterally agreed|
|ED05|SettlementFailed|Settlement of the transaction has failed.|Sent by**any Agent**w hen the settlement of payment has failed or been<br>unsuccessful.|
|FF03|InvalidPaymentTypeInformation|Payment Type Information is missing or invalid.<br>Generic usage if cannot specify Service Level or Local<br>Instrument code|Sent by**any Agent**w hen the Payment Type Information (**Instruction Priority**,<br>**Clearing Channel**) provided for the payment is incorrect or not supported.|
|FF04|InvalidServiceLevelCode|Service Level code is missing or invalid|Sent by**any Agent**w hen the Payment Type Information**Service Level**<br>provided for the payment is incorrect or not supported|
|FF05|InvalidLocalInstrumentCode|Local Instrument code is missing or invalid|Sent by**any Agent**w hen the Payment Type Information**Local Instrument**<br>provided for the payment is incorrect or not supported|
|FF06|InvalidCategoryPurposeCode|Category Purpose code is missing or invalid|Sent by**any Agent**w hen the Payment Type Information**Category Purpose**<br>provided for the payment is incorrect or not supported|
|FF07|InvalidPurpose|Purpose is missing or invalid|Sent by**any Agent**w hen the**Purpose**provided for the payment is either<br>missing or incorrect|
|FOCR|FollowingCancellationRequest|Return following a cancellation request|Sent by**any Agent**that has accepted a payment cancellation request<br>(camt.056) and subsequently is rejecting the unsettled payment instruction.|
|FR01|Fraud|Returned as a result of fraud.|Sent by**any Agent**w hen the payment is identified as fraudulent.|

---

<!-- ELEMENT 407 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|MD02|MissingMandatoryInformationIn<br>Mandate|<br>Mandate related information data required by the<br>scheme is missing.|Sent by**any Agent**w hen information required by the clearing scheme is<br>missing.|
|MD05|CollectionNotDue|Creditor or creditor's agent should not have collected the<br>direct debit|<br>Sent by**any Agent**w hen a Direct Debit collection w as not due|
|MD07|EndCustomerDeceased|End customer is deceased.|Sent by**Creditor Agent**w hen the Creditor or Ultimate Creditor is deceased|
|MS02|NotSpecifiedReasonCustomer<br>Generated|Reason has not been specified by end customer|Sent by**Creditor Agent**w here instructed to reject by the Creditor, but no<br>reason w as specified|
|MS03|NotSpecifiedReasonAgent<br>Generated|Reason has not been specified by agent.|Sent by**any Agent**but no reason is specified|
|NARR|Narrative|Reason is provided as narrative information in the<br>additional reason information.|Sent by**any Agent**the reason is provided as narrative information.**Only to be**<br>**used where no other code is appropriate!**(i.e. exceptional circumstances)|
|NOAS|NoAnswerFromCustomer|No response from Beneficiary|Sent by**any Agent**w hen the Creditor did not respond to query for additional<br>information in order that the payment could be credited e.g. currency control<br>documentation.|
|NOCM|Not compliant (more generic)|Customer account is not compliant with regulatory<br>requirements, for example FICA (in South Africa) or any<br>other regulatory requirements which render an account<br>inactive for certain processing.|Sent by**any Agent**w hen the Creditor account is not compliant w ith certain<br>regulatory requirements.|
|RC01|BankIdentifierIncorrect|<br>Bank Identifier code specified in the message has an<br>incorrect format (formerly<br>IncorrectFormatForRoutingCode).|Sent by**any Agent**w hen an incorrect BIC has been used in the payment|

---

<!-- ELEMENT 408 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|RC04|InvalidCreditorBankIdentifier|Creditor bank identifier is invalid or missing|Sent by**any Agent**w hen the Creditor Agent identification is incorrect or<br>missing|
|RC08|InvalidClearingSystemMemberIden<br>tifier|ClearingSystemMemberidentifier is invalid or missing.<br>Generic usage if cannot specify between debit or credit<br>account|<br>Sent by**any Agent**w hen the clearing system member identification for an<br>Agent is incorrect|
|RC11|InvalidIntermediaryAgent|Intermediary Agent is invalid or missing|Sent by**any Agent**w hen the intermediary agent identification is incorrect|
|RF01|NotUniqueTransactionReference|Transaction reference is not unique within the<br>message.|Sent by**any Agent**w hen the transaction reference (UETR and Instruction<br>Identification) are not unique|
|RR01|Missing Debtor Account or<br>Identification|Specification of the debtor’s account or unique<br>identification needed for reasons of regulatory<br>requirements is insufficient or missing|Sent by**any Agent**w hen the Debtor identification or debtor account is<br>missing, or the information provided are not sufficient|
|RR02|Missing Debtor Name or Address|<br>Specification of the debtor’s name and/or address needed for<br>regulatory requirements is insufficient or missing.|<br>Sent**by any Agent**since the Debtor name or Address is missing, or<br>information provided is not sufficient|
|RR03|Missing Creditor Name or Address|Specification of the creditor’s name and/or address needed<br>for regulatory requirements is insufficient or missing.|Sent by**any Agent**since the Creditor name or Address is missing, or<br>information provided is not sufficient|
|RR04|Regulatory Reason|Regulatory Reason|Sent**by any Agent**due to any unspecified regulatory reason|
|RR05|RegulatoryInformationInvalid|Regulatory or Central Bank Reporting information missing,<br>incomplete or invalid.|Sent**by any Agent**w hen the reporting information required by the central<br>bank or reporting authority is missing or not complete|

---

<!-- ELEMENT 409 -->
Definitions and High Level Use Cases 

|**Code**|**Name**|**ISO Definition**|**High Level Use Case**|
|---|---|---|---|
|RR07|RemittanceInformationInvalid|Remittance information structure does not comply w ith rules<br>for payment type.|Sent**by any Agent**since the remittance information is incorrect|
|RR08|RemittanceInformationTruncated|Remittance information truncated to comply w ith rules for<br>payment type.|Sent**by any Agent**w here the Structured Remittance Information has not<br>been bilaterally or multilaterally agreed, w hich or has resulted in truncation|
|RR09|InvalidStructuredCreditorReference|Structured creditor reference invalid or missing.|Sent**by any Agent**w hen the structure of the creditor reference in the<br>remittance information is invalid or missing|
|RR11|InvalidDebtorAgentServiceID|Invalid or missing identification of a bank proprietary service.|Sent**by any Agent**w here the proprietary identification for the Debtor is<br>invalid or not understood|
|RR12|InvalidPartyID|Invalid or missing identification required w ithin a particular<br>country or payment type.|Sent**by any Agent**w here a proprietary party identification is considered<br>invalid or not understood|
|RUTA|ReturnUponUnableToApply|Return following investigation request and no remediation<br>possible.|Sent by**any Agent**that is unsatisfied w ith the outcome of the unable to<br>apply request and is subsequently rejecting the payment instruction.<br>Alternatively it can be used by the original**Creditor Agent**w hen the creditor<br>is unable to apply the transaction|
|TM01|Invalid Cut off time|Associated message, payment information block, or<br>transaction was received after agreed processing cut-off<br>time.|Sent by**any Agent**w hen the message w as received after the agreed<br>processing cut off time and an agreement is in place to reject rather than<br>apply the next possible value date.|
|UPAY|UnduePayment|Payment is not justified.|Sent by**any Agent**the payment is undue|

---

<!-- ELEMENT 410 -->
**Min 0 – Max 1** The _**Original Transaction Reference**_ optionally capture elements related to the original transactions. The inclusion of this element is particularly useful where the _Payment Return_ includes an Agent not party to the original transaction, or where a significant time lapse has occurred between the original payment and the _Payment Return_ i.e., information may have been archived by Agent in the Return chain. CBPR+ has two rules describing when the Original Transaction Reference should be used. The _Amount_ within the nesting of this Original Transaction Reference element only allows for the _Instructed Amount_ , as instructed by the Debtor in the original payment initiation request. If the _Instructed Amount_ was present in the original payment, populating this data is simple. However, we should also recognise the _Instructed Amount_ is not always present (and in fact is not available in the pacs.009), whereby this value should represent the amount in the _Interbank Settlement Amount_ of the pacs message being returned. The use of _Instructed Amount_ is best described in the pacs.008 Currency and Amount section. 

**==> picture [61 x 62] intentionally omitted <==**

Note: the role of Parties and Agent in Original element remain unchanged unlike elements such as the Return chain 

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

---

<!-- ELEMENT 411 -->
**==> picture [540 x 122] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.008 pacs.008 pacs.008<br>A pacs.004 B pacs.004 C pacs.002 D<br>+ Return  + Return  + Reject<br>Reason  Reason  Reason<br>**----- End of picture text -----**<br>


**==> picture [111 x 60] intentionally omitted <==**

**==> picture [61 x 61] intentionally omitted <==**

## Within the Payment Return (pacs.004) 

- the _Original Group Information element is used to_ refers to original message for which the return relates to. e.g. based upon the above example pacs.008 as the original message would be included in the pacs.004 

- the _Transaction Information > Original UETR_ element would include UETR of the payment message received. i.e. the _**same UETR is used on the Payment Return**_ . 

- the _Original Transaction Reference_ element includes detail from the _Original Message Name Identification_ e.g. the _Debtor_ of the original pacs.008.001.xx 

- the _Return Chain_ element includes the parties in the return payment chain, noting the parties reverse (i.e. change role) from the original payment whereby the _Debtor_ of the original payment becomes the _Creditor_

---

<!-- ELEMENT 412 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

## **Serial Customer Payments** 

Use Case p.4.1.1 – Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008) Use Case p.4.1.2 – Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008) Use Case p.4.1.2.a – Partial Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008) Use Case p.4.1.2.b – Refund Payment of a complete Customer Credit Transfer (pacs.008) Use Case p.4.1.3 - Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008) involving a Market Infrastructure 

## **Serial Financial Institution Payments** 

Use Case p.4.2.1 - Payment Return (pacs.004) of an incomplete Financial Institution Credit Transfer (pacs.009) Use Case p.4.2.2 - Payment Return (pacs.004) of a complete Financial Institution Credit Transfer (pacs.009) Use Case p.4.2.3 - Payment Return (pacs.004) of an incomplete Financial Institution Credit Transfer (pacs.009) involving a Market Infrastructure 

## **Cover Method Payments** 

Use Case p.4.3.1.a - Payment Return (pacs.004) of an incomplete payment using the cover method Use Case p.4.3.1.b - Payment Return (pacs.004) of an incomplete payment using the cover method Use Case p.4.3.2 - Payment Return (pacs.004) of a complete payment using the cover method Use Case p.4.3.2.a - Payment Return (pacs.004) of a complete payment using the cover method Use Case p.4.3.3 - Payment Return (pacs.004) of an incomplete cover payment

---

<!-- ELEMENT 413 -->
## **(pacs.008)** 

**==> picture [806 x 311] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4<br>pacs.008 pacs.008 pacs.008<br>A pacs.004 B pacs.004 C pacs.004 D<br>6 5<br>+ Return  + Return  + Return<br>Reason  Reason  Reason<br>1 3<br>5<br>Debtor initiates a payment  Agent B processes the payment  Having received the payment Agent  Agent C return funds to Agent B,<br>instruction to the Debtor Agent on Agent C D recognises the payment can not  together with the reason code for<br>be completed as requested e.g. the  return.<br>Creditor’s account is closed. Agent<br>2 D return the payment to Agent C<br>4 6<br>(as the original payment had<br>Debtor Agent (A) initiates a  Agent B return funds to Agent A,<br>Agent C processes the payment  already settled) together with the<br>serial payment towards the  together with the reason code for<br>Creditor Agent (D) using  on Agent D return reason. return.<br>Agents B & C as intermediaries<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 414 -->
**==> picture [851 x 375] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>pacs.008 pacs.008 pacs.008<br>A pacs.004 B pacs.004 C pacs.004 D<br>8 7 6<br>+ Return  + Return  + Return<br>Reason  Reason  Reason<br>1 3<br>7<br>Debtor initiates a payment  Agent B processes the payment  Creditor determines that they wish  Agent C return funds to Agent B, together<br>instruction to the Debtor Agent on Agent C to return the payment e.g. they are  with the reason code for return.<br>unable to apply, and instructs their<br>bank (Agent D) to return the<br>4<br>2 payment together with the reason. 8<br>Agent C processes the payment  Agent B return funds to Agent A,<br>Debtor Agent (A) initiates a<br>on Agent D together with the reason code for return.<br>serial payment towards the<br>6<br>Creditor Agent (D) using<br>Agents B & C as intermediaries 5 Agent D returns the payment to<br>Agent C using a Payment Return<br>Agent D credits the account of<br>message (pacs.004) also<br>the Creditor, and may optionally<br>id tifi ti dit including the return reason code<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 415 -->
## **(pacs.008)** 

**==> picture [815 x 338] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>pacs.008 pacs.008 pacs.008<br>A pacs.004 B pacs.004 C pacs.004 D<br>8 7 6<br>+ Return  + Return  + Return<br>Reason  Reason  Reason<br>1 3<br>7<br>Debtor initiates a payment  Agent B processes the payment  Creditor determines that they wish  Agent C return funds to Agent B, together<br>instruction to the Debtor Agent on Agent C to partially return the payment e.g.  with the reason code for return.<br>they were over paid or provide a<br>partial refund, and instructs their<br>4<br>2 bank (Agent D) to partially return  8<br>Agent C processes the payment  the payment together with the  Agent B return funds to Agent A,<br>Debtor Agent (A) initiates a<br>on Agent D reason. together with the reason code for return.<br>serial payment towards the<br>Creditor Agent (D) using<br>Agents B & C as intermediaries 5 6<br>Agent D credits the account of  Agent D returns the payment to<br>the Creditor, and may optionally  Agent C using a Payment Return<br>id tifi ti dit message (pacs 004) also<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 416 -->
**==> picture [761 x 100] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>**----- End of picture text -----**<br>


**==> picture [563 x 156] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 3<br>5<br>Debtor initiates a payment  Agent B processes the payment  Agent D credits the account of<br>instruction to the Debtor Agent on Agent C the Creditor, and may optionally<br>provide a notification e.g. credit<br>notification in addition to an<br>4<br>2 account statement (camt.053)<br>Agent C processes the payment<br>Debtor Agent (A) initiates a<br>on Agent D<br>serial payment towards the<br>Creditor Agent (D) using<br>Agents B & C as intermediaries<br>**----- End of picture text -----**<br>


**==> picture [198 x 118] intentionally omitted <==**

**----- Start of picture text -----**<br>
Creditor determines that they wish<br>to refund the payment e.g. they<br>could not provide the goods or<br>services paid for. They instruct a<br>new payment from their bank<br>account.<br>**----- End of picture text -----**<br>


In some circumstances the Creditor may take it upon themselves to provide a refund, using a new

---

<!-- ELEMENT 417 -->
## **(pacs.008) involving a Market Infrastructure** 

**==> picture [802 x 323] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3<br>pacs.008 pacs.008<br>A<br>pacs.004 pacs.004 B<br>4<br>+ Return  + Return<br>Reason  Reason  pre-settlement reject see<br>pacs.002 section<br>1 3<br>4<br>Debtor initiates a payment  The payment is  settled via the  Having received the payment Agent  The Market Infrastructure returns the<br>instruction to the Debtor Agent local ISO 20022 Market  B recognises the payment can not  payment performing the necessary<br>Infrastructure, whereby the  be completed as requested e.g. the  settlement posting between Agent B<br>payment is forwarded to the  Creditor’s account is closed. Agent  and Agent A.<br>2 Creditor Agent (B) B returns the payment to Agent A<br>using a Payment Return message<br>Debtor Agent (A) initiates a<br>(pacs.004) also including the return<br>serial payment towards the<br>reason code.<br>Creditor Agent (B) using the<br>local currency ISO 20022<br>Market Infrastructure<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 418 -->
**(pacs.009)** 

**==> picture [773 x 327] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3<br>pacs.009<br>pacs.009 pacs.009<br>A camt.053 B<br>pacs.004 C pacs.002 D E<br>5 4<br>+ Return  + Reject<br>Reason  Reason<br>1<br>3 4<br>Agent A as the Debtor initiates  Agent C processes the  Having received the payment  Agent C return funds to Agent B,<br>a payment instruction to the  payment onto Agent D instruction Agent D recognises the  together with the reason code for<br>Debtor Agent (Agent B) payment can not be completed as  return.<br>requested e.g. the Creditor’s account<br>2<br>is closed. Agent D rejects the  5<br>Debtor Agent (B) debits the  payment to Agent C using a Status  Agent B advises Agent A of the return<br>account of Agent A and  Information message (pacs.002) also  of payment together with the reason<br>initiates a serial payment  including the return reject code. using the camt.053 and may optionally<br>towards the Creditor (Agent E)  provide a notification e.g. credit<br>using Agents C as an  notification.<br>intermediary.<br>**----- End of picture text -----**<br>


4 Having received the payment Agent C return funds to Agent B, instruction Agent D recognises the together with the reason code for payment can not be completed as return. requested e.g. the Creditor’s account is closed. Agent D rejects the 5 payment to Agent C using a Status Agent B advises Agent A of the return Information message (pacs.002) also of payment together with the reason including the return reject code. using the camt.053 and may optionally provide a notification e.g. credit notification.

---

<!-- ELEMENT 419 -->
**(pacs.009)** 

**==> picture [808 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3<br>pacs.009 pacs.009 camt.053<br>A camt.053 B pacs.004 C pacs.004 D<br>5 4<br>+ Return<br>+ Return<br>Reason<br>Reason<br>1 3<br>4<br>Agent A as the Debtor initiates  Creditor Agent (C) credits the  Having received the payment Agent  Agent C return funds to Agent B,<br>a payment instruction to the  account of Agent D and may  D recognises the payment is  together with the reason code for<br>Debtor Agent (Agent B) optionally provide a notification  incorrect e.g. the wrong amount  return.<br>e.g. credit notification, in  was received . Agent D sends a<br>2 addition to an account<br>Payment Return to Agent C  5<br>Debtor Agent (B) debits the  statement (camt.053) including the return reason. Agent B advises Agent A of the return<br>account of Agent A and  of payment together with the reason<br>initiates a serial payment  using the camt.053 and may optionally<br>towards the Creditor (Agent D)  provide a notification e.g. credit<br>using Agents C as an  notification.<br>intermediary.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 420 -->
## **Transfer (pacs.009) involving a Market Infrastructure** 

**==> picture [806 x 338] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 3<br>2<br>pacs.009<br>pacs.009 pacs.009<br>camt.053 B C D<br>A pacs.004 pacs.004<br>6<br>5 4<br>+ Return  + Return<br>Reason  Reason<br>1 3<br>5<br>Agent A as the Debtor initiates  The payment is settled via the  Having received the payment Agent  The payment return is settled via the<br>a payment instruction to the  local ISO 20022 Market  local ISO 20022 Market Infrastructure,<br>C recognises the payment can not<br>Debtor Agent (Agent B) Infrastructure, whereby the  be completed as requested e.g. the  whereby the payment return is<br>payment is forwarded to the  Creditor’s account is closed. Agent  forwarded to the Creditor Agent (B)<br>2<br>Creditor Agent (C) C returns the payment towards<br>Debtor Agent (B) debits the  Agent B using a Payment Return  6<br>account of Agent A and  message (pacs.004) also including  Agent B advises Agent A of the return<br>initiates a serial payment  the return reason code. of payment together with the reason<br>towards the Creditor (Agent D)<br>using the camt.053 and may optionally<br>using the local currency ISO<br>4 provide a notification e.g. credit<br>20022 Market Infrastructure.<br>Agent C returns the payment to  notification.<br>Agent B, together with the reason<br>code for return via the local currency<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 421 -->
**==> picture [851 x 376] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2a<br>pacs.008<br>A D<br>6<br>2b<br>1<br>Debtor initiates a payment  + Return<br>instruction to the Debtor Agent<br>5 Reason<br>3 4<br>2a pre-settlement rejects see<br>pacs.009 cov<br>pacs.004 use case p.2.3.1<br>Debtor Agent (A) initiates a  + Return  8<br>payment using the cover method  Reason  B pacs.004 C<br>to the Creditor Agent (D) 7 6<br>Agent D instructs the return of settled<br>+ Return  covering funds, together with the<br>2b Reason  reason for return.<br>In parallel the Debtor Agent (A)  4 5<br>initiates a covering payment to  Agent C produces an end of day account  7<br>Agent C receives the payment<br>credit the account of Agent (D)  Agent C returns the settled covering<br>and credits the account of  statement report. An optional real time<br>with their correspondent (Agent  notifications e.g. credit notification funds to Agent B, together with the<br>Agent D<br>C) (camt.054) may have also been created  reason code for return.<br>at the time of the credit posting<br>8<br>3<br>Agent C returns the settled covering<br>Agent B processes the payment  Having received the payment, Agent D recognises the payment can not be ’ funds to Agent B, together with the<br>l t d t d th C dit t i l d H i t<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 422 -->
**==> picture [851 x 371] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2a<br>pacs.008<br>A pacs.002 D<br>2b 5<br>1<br>+ Reject<br>Debtor initiates a payment<br>instruction to the Debtor Agent Reason<br>3 4<br>2a post-settlement return see<br>pacs.009 cov<br>pacs.004 use case p.4.3.1.a<br>Debtor Agent (A) initiates a  + Return  7<br>payment using the cover method  Reason  B pacs.004 C<br>to the Creditor Agent (D) 6 5<br>Having not settled the pacs.009 cov<br>+ Return  Agent D rejects the covering funds,<br>2b<br>Reason  together with the reason for rejection.<br>In parallel the Debtor Agent (A)  4<br>initiates a covering payment to   6<br>Agent C receives the payment and credits their internal account with Agent D.<br>Agent (D) as the Creditor of the  Agent C returns the settled covering<br>Agent C forwards a pacs.009 cov with Settlement Method INDA (indicating<br>pacs.009 cov funds to Agent B, together with the<br>Agent D is responsible for the settlement of this leg of the payment transaction.<br>reason code for return.<br>7<br>3<br>Having received the payment Agent D recognises the payment can not be  Agent B returns the settled covering<br>Agent B processes the payment  completed as requested e.g. the Creditor’s account is closed. Having not funds to Agent A, together with the<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 423 -->
**==> picture [851 x 375] intentionally omitted <==**

**----- Start of picture text -----**<br>
6<br>1<br>2a<br>pacs.008<br>A D<br>7<br>2b<br>1<br>Debtor initiates a payment<br>instruction to the Debtor Agent<br>5<br>3 4<br>+ Return<br>2a<br>pacs.009 cov<br>Reason<br>Debtor Agent (A) initiates a  + Return  9<br>payment using the cover method  Reason  B pacs.004 C<br>to the Creditor Agent (D) 8<br>7<br>+ Return  Agent D requests the return of<br>2b 6 covering funds, together with the return<br>Reason<br>reason.<br>In parallel the Debtor Agent (A)  4 Agent D reconciles the covering<br>initiates a covering payment to  funds and credits the account of the<br>Agent C receives the payment and<br>credit the account of Agent (D)  Creditor, and may optionally  8<br>credits the account of Agent D Agent C return of covering funds to<br>with their correspondent (Agent  provide a notification e.g., credit<br>C) notification (camt.054) Agent B, together with the reason code<br>for return.<br>5<br>3 Agent C produces an end of day  9<br>account statement report. An  Creditor determines that they wish<br>Agent B processes the payment  Agent B return of covering funds to<br>optional real time notifications e g to return the payment e g they are<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 424 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
6<br>7<br>1<br>2a<br>pacs.008<br>pacs.008<br>A D<br>pacs.004 E<br>2b<br>8<br>9<br>1 + Return<br>Debtor initiates a payment  Reason<br>instruction to the Debtor Agent<br>5<br>3 4 Creditor determines that they wish to return the payment<br>2a e.g. they are unable to apply, and instructs their bank<br>(Agent E) to return the payment together with the reason.<br>Debtor Agent (A) initiates a  pacs.009 cov<br>11<br>payment using the cover<br>method to the Creditor Agent  B pacs.004 C + Return  8<br>(D) + Return  10 Reason  Agent E returns the  original pacs.008 , using a<br>Reason  pacs.004 together with the reason for return.<br>+ Return<br>2b Reason<br>In parallel the Debtor Agent (A)  4 9 Agent D returns the  original pacs.009<br>initiates a covering payment to  Agent D reconciles the covering  cov , using a pacs.004 together with the<br>Agent C receives the payment and credits<br>credit the account of Agent (D)  funds and processes the payment  reason for return.<br>the account of Agent D<br>onto Agent E<br>with their correspondent (Agent<br>C) 10<br>5 7 Agent C return of covering funds to<br>Agent C produces an end of day account  Agent E credits the account of  Agent B, together with the reason code<br>3<br>statement report. An optional real time  the Creditor, and may optionally  for return.<br>Agent B processes the payment  notifications e.g. credit notification provide a notification e.g., credit<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 425 -->
**==> picture [851 x 372] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2a<br>pacs.008<br>A 6 camt.056 D<br>2b<br>See use case p.8.2.1 for the cover payment sample<br>1 3 c.29.2.2 for case resolution and p.56.2.2 for<br>payment return<br>Debtor initiates a payment  pacs.009 cov<br>instruction to the Debtor Agent + Return  5<br>pacs.002 4<br>Reason  B C<br>4 Agent C rejects the covering funds to<br>2a<br>Agent B, together with the reason code<br>Debtor Agent (A) initiates a  + Reject  for rejection.<br>payment using the cover method  Reason<br>to the Creditor Agent (D)<br>5<br>Agent B return of covering funds to<br>2b<br>Agent A, together with the reason code<br>3 for return.<br>In parallel the Debtor Agent (A)<br>initiates a covering payment to  Agent B processes the payment  Agent C receives the payment and<br>credit the account of Agent (D)  on Agent C recognises the payment can not be  6<br>with their correspondent (Agent  completed as requested e.g. the Agent D  Agent A initiates a Request for<br>does not maintain an account with them.<br>C) Cancellation include the Cancellation<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 426 -->
# **Financial Institution Direct Debit** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 427 -->
## The pacs.010 has two core sets of nested elements: 

**pacs.010** 

Group Header 

Credit Instruction 

**==> picture [60 x 60] intentionally omitted <==**

- _**Group Header**_ which contains a set of characteristics that relates to the transaction 

- _**Credit Instruction**_ which contains elements providing information specific to direct debit transaction information and credit instruction. 

Typically a Direct Debit message in a many-to-many payment (FINplus service) would be considered a point-to-point message, successfully resulting in a payment transaction which may be exchange over

---

<!-- ELEMENT 428 -->
**==> picture [32 x 34] intentionally omitted <==**

**A B C secl.010 pacs.010 pacs.002 camt.053 camt.053** 

The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor’s account to the Creditor, where both Debtor and Creditor are financial institutions.

---

<!-- ELEMENT 429 -->
**==> picture [583 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>secl.010<br>pacs.010<br>pacs.002<br>camt.053 pacs.009<br>camt.053<br>**----- End of picture text -----**<br>


The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor’s account to the Creditor, where both Debtor and Creditor are financial institutions.

---

<!-- ELEMENT 431 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 432 -->
## **Min 1 – Max 1** 

## The pacs.010 message _**Creation Date Time**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 433 -->
## **Min 1 – Max 1** 

The pacs.0010 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 435 -->
## **Min 1 – Max 1** 

The Financial Institution Direct Debit _**Credit Identification**_ provides a mandatory element to identify the Direct Debit instruction. 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT Financial Markets Direct Debit message. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 436 -->
**==> picture [615 x 183] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.010<br>Instructed<br>Instructing<br>Agent: Agent B<br>Agent: Agent D<br>pacs.009<br>pacs.009<br>**----- End of picture text -----**<br>


_**Instructing Agent**_ and _**Instructed Agent**_ represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each message leg. 

**==> picture [47 x 43] intentionally omitted <==**

_Instructing Agent_ and _Instructed Agent_ elements are required in all pacs messages and is only available in the _**Credit Instruction.**_ 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Instruction_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 437 -->
## **Min 0 – Max 1** 

The _**Creditor Agent**_ is a static role in the pacs messages. This agent maintain a relationship with their customer, the _**Creditor**_ . Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor. 

**==> picture [82 x 137] intentionally omitted <==**

**Min 0 – Max 1** Where the _**Creditor Agent**_ is utilised the _**Creditor Agent Account**_ may optionally be used to capture the account of the Creditor Agent with the Agent immediate before them in the transaction chain (the Agent Serving their account) 

This would only apply where the message includes a _Creditor Agent_ , however CBPRplus does not recommend to use this element unless mandated within a community or bilaterally agreed. 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [13 x 10] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 438 -->
**==> picture [441 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>whose account<br>identifies the  Creditor<br>BICFI<br>The Creditor sub<br>Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Creditor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either<br>Postal<br>structured or unstructured  Creditor<br>Address<br>address details<br>**----- End of picture text -----**<br>


The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the _**Creditor**_ . The _Creditor_ sub elements describe the _Creditor_ in greater detail. 

**==> picture [186 x 301] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 439 -->
## **Min 0 – Max 1** 

The Financial Institution Direct Debit _**Creditor Account**_ provides a optional element to identify the Creditor’s Account for which the Direct Debit instruction intends to instruct the movement of money to. 

**Min 1 – Max 1** a unique _**Identification**_ for the account, between the Account Servicer and _**Identification**_ Account Owner. The element is further nested by choice of _**IBAN**_ or _**Other**_ to capture the account. 

**==> picture [389 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
An<br>Type<br>Account<br>Currency<br>Name<br>P T<br>**----- End of picture text -----**<br>


An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. 

The _**Currency**_ for which the account is held. This is identified . using the three characters ISO currency code 

The Name of the Account, as Assigned by the servicing institution. 

A nested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 440 -->
## **Min 1 – Max 1** 

The Financial Institution Direct Debit message _**Direct Debit Transaction Information**_ nested element captures information related to the Debit part of the transaction, such as the Debtor, the amount and settlement date. 

**==> picture [56 x 64] intentionally omitted <==**

It is important to recognise that the data elements contained in this part of the Direct Debit message are identical the pacs.009 Financial Institution Credit Transfer message which represents the next stage of the journey should the Direct Debit be accepted. 

**i** 

_From a business perspective authorisation of a direct debit instruction can be predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit scheme). Either_ _**third party debt authority** could be granted to the Agent instructing of the Direct Debit, or the_ _**Payment Identification** could be used to_ 

**==> picture [47 x 47] intentionally omitted <==**

_Credit Instruction Direct Debit Transaction Information_ 

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 441 -->
**Min 1 – Max 1** 

## The pacs message _**Payment Identification**_ provides a set of elements to identify the payment, of which several are mandatory elements 

**==> picture [211 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Identification<br>$<br>**----- End of picture text -----**<br>


a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender’s Reference (Field 20) of the legacy MT payment message. 

_**Instruction Identification**_ **Min 1 – Max 1** 

an end-to-end reference provided by the _Creditor_ which must be passed unchanged throughout the payment and reported back to the Creditor. 

_**End to End Identification**_ **Min 1 – Max 1** 

note: if the Creditor has not provide an endto-end identifier, the _Creditor Agent_ may populate “NOTPROVIDED” to comply the mandatory need of this element. 

**==> picture [36 x 35] intentionally omitted <==**

**==> picture [104 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
UETR<br>Min 1 – Max 1<br>**----- End of picture text -----**<br>


the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their

---

<!-- ELEMENT 442 -->
## **(continued)** 

## **Min 1 – Max 1** The _**Identification** also_ a set of elements to the direct pacs message _**Payment**_ provides optional identify debit transaction. 

**==> picture [752 x 244] intentionally omitted <==**

**----- Start of picture text -----**<br>
Transaction an end-to-end reference assigned by the first Instructing<br>Identification Agent to identify the transaction.<br>Payment Min 0 – Max 1<br>Identification<br>$ a point-to-point reference populated by a Payment<br>Clearing<br>Market Infrastructure, typically to the settlement leg of a<br>System<br>clearing system transaction as a reference to the settled<br>Reference<br>Min 0 – Max 1 clearing transaction.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 443 -->
**Min 0 – Max 1** 

The Financial Institution Direct Debit message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. 

A nested element which may either use an external _**Service**_ ISO Service Level code or a proprietary code. It is _**Instruction Level**_ used to identify a particular agreed service level which _**Priority**_ **Min 0 – Max 3** should be applied to the payment. **Min 0 – Max 1** 

a choice of imbedded codes representing the urgency considered by **Min 0 –** the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority. 

_Payment Type Information_ _**Local Instrument**_ **Min 0 – Max 1** _**Category Purpose**_ **Min 0 – Max 1** 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order. 

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

**==> picture [36 x 34] intentionally omitted <==**

A nested element which may either use an external ISO 

**==> picture [11 x 12] intentionally omitted <==**

_Credit Instruction_ 

_Direct Debit Transaction Information_ 

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 444 -->
## The pacs.010 message (unlike the pacs.008) has one element to capture the amount of the Transfer, _**Interbank Settlement Amount**_ . 

**Min 1 – Max 1** 

**==> picture [45 x 59] intentionally omitted <==**

**==> picture [46 x 59] intentionally omitted <==**

_**Interbank Settlement Amount**_ 

A mandated currency amount moved between the _Instructing Agent_ and the _Instructed Agent._ This therefore is the point-to-point currencyamount exchanged, comparable with the MT Field 32 

**==> picture [46 x 59] intentionally omitted <==**

**==> picture [63 x 63] intentionally omitted <==**

Note: the Financial Institution Direct Debit (pacs.010) has no _Instructed Amount_ element, _Exchange Rate_ or _Charger Bearer_ (like the pacs.009) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 445 -->
## **Min 1 – Max 1** The Financial Institution Direct Debit _**Interbank Settlement Date**_ the _**Date**_ the transaction message captures is completed/effected. 

**10** 

This _**Date**_ element use ISODate YYYY-MM-DD For example: 2002-10-10 (10 October 2002) 

**==> picture [11 x 12] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 446 -->
## **Min 0  – Max 1** 

The Financial Institution Direct Debit _**Settlement**_ message _**Time Request**_ captures the requested settlement time as a choice of nested elements. 

**==> picture [87 x 64] intentionally omitted <==**

Where _**Settlement Time Request**_ is used the nested: 

- _**CLS Time**_ **Min 0 – Max 1** 

- • _**Till Time**_ **Min 0 – Max 1** • _**From Time**_ **Min 0 – Max 1** • **Min 0 – Max 1** _**Reject Time**_ 

- may be used to capture information related to this time. 

**==> picture [11 x 12] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 447 -->
**==> picture [127 x 29] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>identifies the  Debtor<br>**----- End of picture text -----**<br>


## The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the _**Debtor**_ . The _Debtor_ sub elements describe the _Debtor_ in greater detail. 

**==> picture [52 x 25] intentionally omitted <==**

**----- Start of picture text -----**<br>
BICFI<br>**----- End of picture text -----**<br>


**==> picture [441 x 325] intentionally omitted <==**

**----- Start of picture text -----**<br>
Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Debtor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either<br>Postal<br>structured or unstructured  Debtor<br>Address<br>address details<br>**----- End of picture text -----**<br>


**==> picture [214 x 295] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 448 -->
## **Min 0 – Max 1** 

The Financial Institution Direct Debit message _**Debtor Account**_ also provides an number of optional nested element to identify the account for which debit and credit entries have been made. 

**Min 1 – Max 1** a unique _**Identification**_ for the account, between the Account Servicer and _**Identification**_ Account Owner. The element is further nested by choice of _**IBAN**_ or _**Other**_ to capture the account. 

**==> picture [389 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
An<br>Type<br>Account<br>Currency<br>Name<br>P T<br>**----- End of picture text -----**<br>


An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. 

The _**Currency**_ for which the account is held. This is identified . using the three characters ISO currency code 

The Name of the Account, as Assigned by the servicing institution. 

A nested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 449 -->
## **Min 0 – Max 1** 

The _**Debtor Agent**_ is a static role in the pacs messages. This agent maintain a relationship with their customer, the _**Debtor**_ . Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor. 

**==> picture [81 x 137] intentionally omitted <==**

**Min 0 – Max 1** Where the _**Debtor Agent**_ is utilised the _**Debtor Agent Account**_ may optionally be used to capture the account of the Debtor Agent with the Agent immediate after them in the transaction chain (the Agent Serving their account) This would only apply where the message includes a _Debtor Agent_ , however CBPRplus does not recommend to use this element unless mandated within a community or bilaterally agreed. 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [13 x 10] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 450 -->
The _**Instruction for Debtor Agent**_ elements within the pacs.010 Financial Institution Direct Debit optionally provides information related to the processing of the direct debit instruction. 

**==> picture [52 x 55] intentionally omitted <==**

**Min 0 – Max 1** The _**Instruction for Debtor Agent**_ element offers a occurrence of free format information. The use of this element should be bilaterally agreed with the _Debtor Agent_ to maximize the ability to Straight Through Process the instruction. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 451 -->
## **Min 0 – Max 1** 

The _**Purpose**_ elements within the pacs.010 Financial Institution Direct Debit capture the reason for the payment transaction which would result from a successful direct debit. This element may either use an external ISO Purpose code or a proprietary code. 

The is used the the nature of the CORT Trade Settlement CFEE purpose by capture payment e.g. Payment, Cancellation Fees etc. and should not be confused with Regulatory Reporting codes. 

**==> picture [123 x 90] intentionally omitted <==**

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. 

For example: 

OTCD is classified within the Collateral categorisation, with the _Name_ OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated. 

**==> picture [10 x 11] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 452 -->
The optional _**Remittance Information**_ element within the pacs.010 Financial Institution Direct Debit is nested to provide _**Unstructured**_ information related to payment. 

**Min 0 – Max 1** 

**==> picture [175 x 175] intentionally omitted <==**

_**Remittance Information**_ enable the matching/reconciliation of an entry that the payment is intended to settle 

**Min 0 – Max 1** The **Unstructured** sub element captures free format _Remittance Information_ which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence. 

Note: like the pacs.009 _Remittance Information_ can only be captured in an _Unstructured_ element. _**Remittance Information**_ is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using 

**==> picture [62 x 62] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [12 x 7] intentionally omitted <==**

---

<!-- ELEMENT 453 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

## **Financial Institution Direct Debit** 

Use Case p.10.1.1 - High Level Payment of a Financial Institution Direct Debit (pacs.010) Use Case p.10.1.1.a  - High Level Book movement of a Financial Institution Direct Debit (pacs.010) Use Case p.10.1.2 - High Level Rejection of a Financial Institution Direct Debit (pacs.010)

---

<!-- ELEMENT 454 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>pacs.010<br>pacs.002<br>A<br>camt.053 B pacs.009 pacs.009 camt.053 E<br>2a C D<br>2<br>3 4<br>1 2a 4<br>Debtor Agent (B) debits the<br>Agent E initiates a Direct Debit<br>Agent D credits the account of the<br>Debtor (Agent A) optionally<br>instruction to debit Agent A’s<br>account provide a notification e.g. credit  Creditor (Agent E), and may<br>notification in addition to an  optionally provide a notification<br>e.g. credit notification in addition to<br>account statement (camt.053)<br>2 an account statement (camt.053)<br>Debtor Agent (B) initiates a<br>3<br>serial payment towards the<br>Creditor Agent (E) using<br>Agent C processes the payment<br>Agents B & C as intermediaries<br>on Agent D<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 455 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>pacs.010<br>pacs.002<br>camt.053<br>A camt.053 B C<br>2a 2b<br>1 2a 2b<br>Debtor Agent (B) debits the<br>Agent E initiates a Direct Debit<br>Agent B credits the account of the<br>Debtor (Agent A) optionally<br>instruction to debit Agent A’s<br>account provide a notification e.g. credit  Creditor (Agent C), and may<br>notification in addition to an  optionally provide a notification<br>e.g. credit notification in addition to<br>account statement (camt.053)<br>an account statement (camt.053)<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 456 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>pacs.010<br>pacs.002<br>A B E<br>C D<br>1<br>Agent D initiates a Direct Debit<br>instruction to debit Agent A’s<br>account<br>Debtor Agent (B) rejects the<br>instruction, using a pacs.002,<br>as no mandate agreement is in<br>place.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 457 -->
# **Financial Institution Direct Debit – Margin Collection** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 458 -->
## The pacs.010 has two core sets of nested elements: 

**pacs.010** 

Group Header 

**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Credit Instruction<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

- _**Group Header**_ which contains a set of characteristics that relates to the transaction 

- _**Credit Instruction**_ which contains elements providing information specific to direct debit transaction information and credit instruction. 

The Financial Institution Direct Debit Margin Collection is designed to allow a Central Counterpart to collect money by triggering a payment. Whereby the pacs.010 Debit transfer the money to the Creditor using a pacs.009. Unlikely the pacs.010 Financial Institution Direct Debit additional Credit Instruction elements are allowed in this Usage Guideline.

---

<!-- ELEMENT 459 -->
**==> picture [583 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>secl.010<br>pacs.010<br>pacs.002<br>pacs.009<br>camt.053<br>**----- End of picture text -----**<br>


The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor’s account to the Creditor, where both Debtor and Creditor are financial institutions.

---

<!-- ELEMENT 461 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 462 -->
## **Min 1 – Max 1** 

## The pacs.010 message _**Creation Date Time**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 463 -->
## **Min 1 – Max 1** 

The pacs.0010 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 465 -->
## **Min 1 – Max 1** 

The Financial Institution Direct Debit _**Credit Identification**_ provides a mandatory element to identify the Direct Debit instruction. 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT Financial Markets Direct Debit message. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 466 -->
**Min 0 – Max 1** 

## The pacs message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. These elements are applied to the pacs.009 which results from this message. 

_**Instruction Priority**_ **Min 0 – Max 1** _Payment Type Information_ 

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-topoint information may be used by the Instructed Agent to differentiate the processing priority. 

_**Category Purpose**_ **Min 0 – Max 1** 

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, SECU Transactionis the payment of securities.

---

<!-- ELEMENT 467 -->
**Agents** 

**==> picture [615 x 183] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.010<br>Instructed<br>Instructing<br>Agent: Agent B<br>Agent: Agent D<br>pacs.009<br>pacs.009<br>**----- End of picture text -----**<br>


_**Instructing Agent**_ and _**Instructed Agent**_ represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each message leg. 

**==> picture [47 x 43] intentionally omitted <==**

_Instructing Agent_ and _Instructed Agent_ elements are required in all pacs messages and is only available in the _**Credit Instruction.**_ 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Instruction_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 468 -->
The can to 3 which a role in the pacs message capture up Intermediary Agents, play dynamic payment between the Debtor Agent and Creditor Agent. 

**Min 0 – Max 1** 

**==> picture [61 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 1**_ captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 1 Account**_ captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a. 

## **Min 0 – Max 1** 

**2** 

**==> picture [51 x 37] intentionally omitted <==**

The _**Intermediary Agent 2**_ captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 2 Account**_ captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

**==> picture [62 x 53] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 3**_ captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. **Min 0 – Max 1**

---

<!-- ELEMENT 469 -->
## **Agent Account** 

## **Min 0 – Max 1** 

The _**Creditor Agent**_ is a static role in the pacs messages. This agent maintain a relationship with their customer, the _**Creditor**_ . Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor. 

**==> picture [82 x 137] intentionally omitted <==**

**Min 0 – Max 1** Where the _**Creditor Agent**_ is utilised the _**Creditor Agent Account**_ may optionally be used to capture the account of the Creditor Agent with the Agent immediate before them in the transaction chain (the Agent Serving their account) 

This would only apply where the message includes a _Creditor Agent_ , however CBPRplus does not recommend to use this element unless mandated within a community or bilaterally agreed. 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [13 x 10] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 470 -->
**==> picture [441 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>whose account<br>identifies the  Creditor<br>BICFI<br>The Creditor sub<br>Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Creditor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either<br>Postal<br>structured or unstructured  Creditor<br>Address<br>address details<br>**----- End of picture text -----**<br>


The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the _**Creditor**_ . The _Creditor_ sub elements describe the _Creditor_ in greater detail. 

**==> picture [186 x 301] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 471 -->
## **Min 0 – Max 1** 

The Financial Institution Direct Debit _**Creditor Account**_ provides an optional element to identify the Creditor’s Account for which the Direct Debit instruction intends to instruct the movement of money to. 

**Min 1 – Max 1** a unique _**Identification**_ for the account, between the Account Servicer and _**Identification**_ Account Owner. The element is further nested by choice of _**IBAN**_ or _**Other**_ to capture the account. 

An element which may either use an external ISO Cash Account _**Type**_ Type code or a proprietary code. It is used to identifier a particular type of account. _Account_ The _**Currency**_ for which the account is held. This is identified _**Currency**_ 

The _**Currency**_ for which the account is held. This is identified . using the three characters ISO currency code 

The Name of the Account, as Assigned by the servicing institution. 

_**Name**_ 

**==> picture [15 x 15] intentionally omitted <==**

**==> picture [76 x 32] intentionally omitted <==**

A nested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 472 -->
## **Information** 

## **Min 1 – Max 1** 

The Financial Institution Direct Debit message _**Direct Debit Transaction Information**_ nested element captures information related to the Debit part of the transaction, such as the Debtor, the amount and settlement date. 

**==> picture [56 x 64] intentionally omitted <==**

It is important to recognise that the data elements contained in this part of the Direct Debit message are identical the pacs.009 Financial Institution Credit Transfer message which represents the next stage of the journey should the Direct Debit be accepted. 

**i** 

_From a business perspective authorisation of a direct debit instruction can be predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit scheme). Either_ _**third party debt authority** could be granted to the Agent instructing of the Direct Debit, or the_ _**Payment Identification** could be used to_ 

**==> picture [47 x 47] intentionally omitted <==**

**==> picture [11 x 11] intentionally omitted <==**

_Credit Instruction_ 

_Direct Debit Transaction Information_ 

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 473 -->
**Min 1 – Max 1** 

## The pacs message _**Payment Identification**_ provides a set of elements to identify the payment, of which several are mandatory elements 

**==> picture [211 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Identification<br>$<br>**----- End of picture text -----**<br>


a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender’s Reference (Field 20) of the legacy MT payment message. 

_**Instruction Identification**_ **Min 1 – Max 1** 

an end-to-end reference provided by the _Creditor_ which must be passed unchanged throughout the payment and reported back to the Creditor. 

_**End to End Identification**_ **Min 1 – Max 1** 

note: if the Creditor has not provide an endto-end identifier, the _Creditor Agent_ may populate “NOTPROVIDED” to comply the mandatory need of this element. 

**==> picture [36 x 35] intentionally omitted <==**

**==> picture [104 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
UETR<br>Min 1 – Max 1<br>**----- End of picture text -----**<br>


the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their

---

<!-- ELEMENT 474 -->
## **(continued)** 

## **Min 1 – Max 1** The _**Identification** also_ a set of elements to the direct pacs message _**Payment**_ provides optional identify debit transaction. 

**==> picture [752 x 244] intentionally omitted <==**

**----- Start of picture text -----**<br>
Transaction an end-to-end reference assigned by the first Instructing<br>Identification Agent to identify the transaction.<br>Payment Min 0 – Max 1<br>Identification<br>$ a point-to-point reference populated by a Payment<br>Clearing<br>Market Infrastructure, typically to the settlement leg of a<br>System<br>clearing system transaction as a reference to the settled<br>Reference<br>Min 0 – Max 1 clearing transaction.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 475 -->
**Min 0 – Max 1** 

The Financial Institution Direct Debit message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described.  These elements apply to the debit transaction, whereby the Credit Instruction has it own Payment Type Information. 

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. 

_**Service Level**_ **Min 0 – Max 3** 

a choice of imbedded codes representing the urgency considered by **Min 0 –** the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority. 

_**Instruction Priority**_ 

**Min 0 – Max 1** 

_Payment Type Information_ _**Category Purpose**_ **Min 0 – Max 1** 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order. 

_**Local Instrument**_ **Min 0 – Max 1** 

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

**==> picture [36 x 34] intentionally omitted <==**

A nested element which may either use an external ISO 

**==> picture [11 x 12] intentionally omitted <==**

_Credit Instruction_ 

_Direct Debit Transaction Information_ 

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 476 -->
## The pacs.010 message (unlike the pacs.008) has one element to capture the amount of the Transfer, _**Interbank Settlement Amount**_ . 

**Min 1 – Max 1** 

**==> picture [45 x 59] intentionally omitted <==**

**==> picture [46 x 59] intentionally omitted <==**

_**Interbank Settlement Amount**_ 

A mandated currency amount moved between the _Instructing Agent_ and the _Instructed Agent._ This therefore is the point-to-point currencyamount exchanged, comparable with the MT Field 32 

**==> picture [46 x 59] intentionally omitted <==**

**==> picture [63 x 63] intentionally omitted <==**

Note: the Financial Institution Direct Debit (pacs.010) has no _Instructed Amount_ element, _Exchange Rate_ or _Charger Bearer_ (like the pacs.009) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 477 -->
## **Min 1 – Max 1** The Financial Institution Direct Debit _**Interbank Settlement Date**_ the _**Date**_ the transaction message captures is completed/effected. 

**10** 

This _**Date**_ element use ISODate YYYY-MM-DD For example: 2002-10-10 (10 October 2002) 

**==> picture [11 x 12] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 478 -->
## **Min 0  – Max 1** 

The Financial Institution Direct Debit _**Settlement**_ message _**Time Request**_ captures the requested settlement time as a choice of nested elements. 

**==> picture [87 x 64] intentionally omitted <==**

Where _**Settlement Time Request**_ is used the nested: 

- _**CLS Time**_ **Min 0 – Max 1** 

- • _**Till Time**_ **Min 0 – Max 1** • _**From Time**_ **Min 0 – Max 1** • **Min 0 – Max 1** _**Reject Time**_ 

- may be used to capture information related to this time. 

**==> picture [11 x 12] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 479 -->
**==> picture [127 x 29] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>identifies the  Debtor<br>**----- End of picture text -----**<br>


## The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the _**Debtor**_ . The _Debtor_ sub elements describe the _Debtor_ in greater detail. 

**==> picture [52 x 25] intentionally omitted <==**

**----- Start of picture text -----**<br>
BICFI<br>**----- End of picture text -----**<br>


**==> picture [441 x 325] intentionally omitted <==**

**----- Start of picture text -----**<br>
Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Debtor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either<br>Postal<br>structured or unstructured  Debtor<br>Address<br>address details<br>**----- End of picture text -----**<br>


**==> picture [214 x 295] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 480 -->
## **Min 0 – Max 1** 

The Financial Institution Direct Debit message _**Debtor Account**_ also provides an number of optional nested element to identify the account for which debit and credit entries have been made. 

**Min 1 – Max 1** 

a unique _**Identification**_ for the account, between the Account Servicer and _**Identification**_ Account Owner. The element is further nested by choice of _**IBAN**_ or _**Other**_ to capture the account. 

**==> picture [389 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
An<br>Type<br>Account<br>Currency<br>Name<br>P T<br>**----- End of picture text -----**<br>


An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. 

The _**Currency**_ for which the account is held. This is identified . using the three characters ISO currency code 

The Name of the Account, as Assigned by the servicing institution. 

A nested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 481 -->
## **Agent Account** 

## **Min 0 – Max 1** 

The _**Debtor Agent**_ is a static role in the pacs messages. This agent maintain a relationship with their customer, the _**Debtor**_ . Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor. 

**==> picture [81 x 137] intentionally omitted <==**

**Min 0 – Max 1** Where the _**Debtor Agent**_ is utilised the _**Debtor Agent Account**_ may optionally be used to capture the account of the Debtor Agent with the Agent immediate after them in the transaction chain (the Agent Serving their account) This would only apply where the message includes a _Debtor Agent_ , however CBPRplus does not recommend to use this element unless mandated within a community or bilaterally agreed. 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [13 x 10] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 482 -->
The _**Instruction for Debtor Agent**_ elements within the pacs.010 Financial Institution Direct Debit optionally provides information related to the processing of the direct debit instruction. 

**Min 0 – Max 1** 

**==> picture [52 x 55] intentionally omitted <==**

The _**Instruction for Debtor Agent**_ element offers a occurrence of free format information. 

The use of this element should be bilaterally agreed with the _Debtor Agent_ to maximize the ability to Straight Through Process the instruction. 

**==> picture [11 x 11] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 483 -->
## **Min 0 – Max 1** 

The _**Purpose**_ elements within the pacs.010 Financial Institution Direct Debit capture the reason for the payment transaction which would result from a successful direct debit. This element may either use an external ISO Purpose code or a proprietary code. 

The is used the the nature of the CCPC CCP Cleared Initial and purpose by capture payment e.g. Margin should not be confused with Regulatory Reporting codes. 

**==> picture [123 x 90] intentionally omitted <==**

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. 

For example: 

OTCD is classified within the Collateral categorisation, with the _Name_ OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated. 

**==> picture [10 x 11] intentionally omitted <==**

_Credit Instruction_

---

<!-- ELEMENT 484 -->
The optional _**Remittance Information**_ element within the pacs.010 Financial Institution Direct Debit is nested to provide _**Unstructured**_ information related to payment. 

**Min 0 – Max 1** 

**==> picture [175 x 175] intentionally omitted <==**

_**Remittance Information**_ enable the matching/reconciliation of an entry that the payment is intended to settle 

**Min 0 – Max 1** The **Unstructured** sub element captures free format _Remittance Information_ which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence. 

Note: like the pacs.009 _Remittance Information_ can only be captured in an _Unstructured_ element. _**Remittance Information**_ is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using 

**==> picture [62 x 62] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [12 x 7] intentionally omitted <==**

---

<!-- ELEMENT 485 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

**Financial Institution Direct Debit** Use Case p.10.2.1 - High Level Payment Of A Financial Institution Direct Debit (pacs.010) Use Case p.10.2.2 - High Level Rejection Of A Financial Institution Direct Debit (pacs.010)

---

<!-- ELEMENT 486 -->
**==> picture [91 x 19] intentionally omitted <==**

**----- Start of picture text -----**<br>
(pacs.010)<br>**----- End of picture text -----**<br>


**==> picture [677 x 312] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>pacs.010<br>pacs.002<br>A B pacs.009 pacs.009 camt.053 E<br>C D<br>2<br>3 4<br>1 3 4<br>Agent E initiates a Direct Debit<br>Agent C processes the payment  Agent D credits the account of the<br>instruction to debit Agent A’s<br>on Agent D Creditor (Agent E), and may<br>account<br>optionally provide a notification<br>e.g. credit notification in addition to<br>2 an account statement (camt.053)<br>Debtor Agent (B) initiates a<br>serial payment towards the<br>Creditor Agent (E) using<br>Agents B & C as intermediaries<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 487 -->
**(pacs.010)** 

**==> picture [672 x 307] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>pacs.010<br>pacs.002<br>A B E<br>C D<br>1<br>Agent D initiates a Direct Debit<br>instruction to debit Agent A’s<br>account<br>Debtor Agent (B) rejects the<br>instruction, using a pacs.002,<br>as no mandate agreement is in<br>place.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 488 -->
# **Financial Institution to Financial Institution Customer Direct Debit** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 489 -->
**==> picture [186 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.003<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Direct Debit Transaction<br>Information<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

## The pacs.003 has two core sets of nested elements: 

- _**Group Header**_ which contains a set of characteristics that relates to all individual transaction 

- _**Direct Debit Transaction Information**_ which contains elements providing information specific to the individual direct debit transaction. 

Payment messages in a many-to-many payment are considered as a 

single transaction.

---

<!-- ELEMENT 490 -->
**==> picture [803 x 240] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>A<br>Debtor Debtor Agent Creditor Agent Initiating Party* Creditor<br>pain.008**<br>pain.002<br>pacs.003<br>pacs.002<br>camt.053<br>*Initiating Party may alternative represent an authorised party such as a head office<br>**----- End of picture text -----**<br>


*Initiating Party may alternative represent an authorised party such as a head office **or other proprietary method for instructing a direct debit initiation request. 

The Financial Institution To Financial Institution Customer Direct Debit message is sent by the Creditor Agent to the Debtor Agent, directly or through other agents and/or a payment clearing and settlement system. It is used to collect funds from a Debtor account for a Creditor, whereby one or both of these Parties are nonFinancial Institutions.

---

<!-- ELEMENT 492 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 payment message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For and Settlement the Identification has no Payment Clearing (pacs) messages Message exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field could be considered a similar where a contains a 20) comparison pacs message single Transaction. 

**==> picture [60 x 60] intentionally omitted <==**

Each transaction’s _Direct Debit Transaction Information_ contains a variety of nested _Payment Identification_ elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference) 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 493 -->
**Min 1 – Max 1** 

## The pacs.003 message _**Creation Date**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 494 -->
## **Min 1 – Max 1** 

The pacs.003 message _**Number of Transactions**_ captures the number of individual transaction contained within the message. 

**==> picture [52 x 69] intentionally omitted <==**

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 

**==> picture [65 x 73] intentionally omitted <==**

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 495 -->
**Min 1 – Max 1** 

The pacs.003 _**Settlement Method**_ element within the Group Header _**Settlement Information**_ , includes one of the embedded codes to indicate how the payment message will be settled. 

The _**Settlement Method** element_ in the pacs.003 allows a choice of an embedded code. 

**INDA** indicate this Customer Direct Debit will be settled by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated _**Settlement Account**_ element. 

**$** € 

**INGA** indicate this Customer Direct Debit has already been settled by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated _**Settlement Account**_ element. 

**==> picture [60 x 60] intentionally omitted <==**

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification

---

<!-- ELEMENT 496 -->
The pacs.003 message _**Settlement Account**_ is a nested element as part of _**Settlement Information,**_ this element identifies information related to an account used to settle the direct debit instruction. 

**Min 0 – Max 1** The _**Settlement Account**_ identifies the account details maintained at the account institution for the settlement of the instruction as servicing (Agent responsible indicated in the _**Settlement Method**_ ) 

**==> picture [80 x 84] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 498 -->
**Min 1 – Max 1** 

## The pacs message _**Payment Identification**_ provides a set of elements to identify the payment, of which several are mandatory elements 

**==> picture [211 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Payment<br>Identification<br>$<br>**----- End of picture text -----**<br>


a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender’s Reference (Field 20) of the legacy MT payment message. 

_**Instruction Identification**_ **Min 1 – Max 1** 

an end-to-end reference provided by the _Creditor_ which must be passed unchanged throughout the payment and reported back to the Creditor. 

_**End to End Identification**_ **Min 1 – Max 1** 

note: if the Creditor has not provide an endto-end identifier, the _Creditor Agent_ may populate “NOTPROVIDED” to comply the mandatory need of this element. 

**==> picture [36 x 35] intentionally omitted <==**

**==> picture [104 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
UETR<br>Min 0 – Max 1<br>**----- End of picture text -----**<br>


the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their

---

<!-- ELEMENT 499 -->
## **Min 1 – Max 1** The _**Identification** also_ a set of elements to the direct pacs message _**Payment**_ provides optional identify debit transaction. 

**==> picture [752 x 244] intentionally omitted <==**

**----- Start of picture text -----**<br>
Transaction an end-to-end reference assigned by the first Instructing<br>Identification Agent to identify the transaction.<br>Payment Min 0 – Max 1<br>Identification<br>$ a point-to-point reference populated by a Payment<br>Clearing<br>Market Infrastructure, typically to the settlement leg of a<br>System<br>clearing system transaction as a reference to the settled<br>Reference<br>Min 0 – Max 1 clearing transaction.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 500 -->
**Min 0 – Max 1** 

The pacs message _**Payment Type Information**_ provides a set of optional elements where the payment type can be described. 

a choice of imbedded codes representing the _**Instruction**_ urgency considered by _**Priority**_ the Instructing Agent, **Min 0 – Max 1** this point-to-point information may be used by the Instructed Agent to differentiate the processing priority. 

a choice of imbedded codes representing the clearing channel to be used to process direct debits. 

_**Clearing Channel**_ 

**Min 0 – Max 1** 

A nested element which may either use an external ISO Service Level code* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. 

_**Service Level**_ **Min 0 – Max 3** 

_Payment Type Information_ i 

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order. 

_**Local Instrument**_ **Min 0 – Max 1** 

Note: the ISO instrument codes are registered by specific community group (captured in the code list) 

**==> picture [35 x 33] intentionally omitted <==**

**==> picture [87 x 41] intentionally omitted <==**

**----- Start of picture text -----**<br>
Category<br>**----- End of picture text -----**<br>


A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the

---

<!-- ELEMENT 501 -->
**£** 

**$** 

¥ 

## The pacs.003 message has two key element to capture the amount of the Credit Transfer, _**Interbank Settlement Amount**_ and _**Interbank Settlement Date**_ . 

**Min 1 – Max 1 Min 1 – Max 1** 

_**Interbank Settlement Amount**_ 

A mandated currency amount moved between the _Instructing Agent_ and the _Instructed Agent._ This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32B 

**==> picture [44 x 44] intentionally omitted <==**

_**Interbank Settlement Date**_ 

A mandated date on which the _Interbank Settlement_ should be executed between the _Instructing Agent_ and the _Instructed Agent._ This therefore is the value date comparable with the MT Field 30 

**==> picture [61 x 59] intentionally omitted <==**

Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important one. Instructed Amount relates to the amount Instructed to be debited from the Debtor’s account and only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not the

---

<!-- ELEMENT 502 -->
The pacs.003 message has two optional elements to capture the information related to the settlement of the instructions. 

**Min 0 – Max 1** 

**==> picture [59 x 55] intentionally omitted <==**

The _**Settlement Priority**_ provides an optional choice of embedded codes to indicate the instruction’s settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the _**Settlement Method**_ and should not be confused with the _**Instruction Priority.**_ 

**==> picture [62 x 62] intentionally omitted <==**

Note: where _**Settlement Priority**_ of the pacs.003 is ‘URGT’ (Urgent) means the highest priority possible to process the direct debit settlement and the amount of money becomes available to the Creditor Agent. 

**==> picture [59 x 68] intentionally omitted <==**

**Min 0 – Max 1** 

The _**Settlement Time Indication**_ optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure. This DateTime can be captured in two nested elements, _**Debit Date Time**_ and _**Credit Date Time**_ .

---

<!-- ELEMENT 503 -->
**$100** 

## **Min 0 – Max 1** 

The _**Instructed Amount**_ captures currency and amount instructed by the Creditor. This conditional element is required when the _**Interbank Settlement Amount**_ is not the same currency and/or amount as originally instructed by the _Creditor._ For example, a charge is taken, or the transactions is converted to another currency. This element is comparable with the legacy Field 33B. 

**==> picture [44 x 44] intentionally omitted <==**

**----- Start of picture text -----**<br>
£<br>**----- End of picture text -----**<br>


¥ 

**Min 0 – Max 1** 

The _**Exchange Rate**_ captures the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency. 

Note: a number of Cross Element Rules exist which relate to the _Instructed_ 

**==> picture [42 x 19] intentionally omitted <==**

---

<!-- ELEMENT 504 -->
**Min 1 – Max 1** 

The mandated _**Charge Bearer**_ element uses an embedded code that is used to specify which party/parties would bear associated with the transaction. This element is any charges processing payment comparable with MT Field 71A ‘Details of Charges’ 

**Charge Code Description Bearer** CRED Creditor **(1.1)** DEBT Debtor **71A: Details Code Description** SHAR Shared **of Charges** BEN Beneficiar y SLEV Service Level OUR Our Customer Charges SHA Shared Charges 

**==> picture [61 x 63] intentionally omitted <==**

Note: SLEV is removed from CBPR+ usage guideline specifications.

---

<!-- ELEMENT 505 -->
**Min 1 – Max 1** 

## **Min 0 – Max *** 

The _**Charges Information**_ element provides information on the charges to be paid by the _**Charge Bearer**_ . This element is comparable with MT Fields: 71F ‘Senders Charges’ and 71G ‘Receiver’s Charges’ 

**Charge** Amount **Information** Currenc y **(0.*)** Agent BICFI Name 

Structured Postal Address 

In addition to the legacy MT message the pacs.003 _Charge Information_ mandate the _Agent,_ this represent the Agent for who the Charges are either; due (pre-paid charges) or has taken a charge (deduct from the transaction) 

**==> picture [37 x 35] intentionally omitted <==**

CBPR+ best practice recommends the use of the structured Agent BIC. 

As the _**Charges Information**_ element is repetitive it can capture charges related to previous legs of the payment transaction. 

**==> picture [61 x 63] intentionally omitted <==**

Note: As the _Charge Information_ element has the capability to capture both charges deducted and charges included i.e. pre-paid charges, the use of the _Interbank Settlement Amount_ and _Instructed Amount_ elements play an important role. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 506 -->
**Min 1 – Max 1** The pacs.003 message mandatory _**Requested Collection Date**_ element, captures the date on which the creditor requests that the amount of money is to be collected from the debtor. 

**10** 

It is defined by _**ISO Date**_ expressed in the _**YYYY-MM-DD format**_ . 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 507 -->
**Min 0 – Max 1** 

## The pacs.003 _**Direct Debit Transaction**_ component provides information specific to the direct debit mandate. 

> _**Mandate**_ Provides further details of the direct debit mandate signed between 

> _**Related**_ the creditor and the debtor. E.g., Mandate Identification, Date of 

> _**Information**_ Signature and Electronic Signature. **Min 0 – Max 1** _Direct Debit_ _**Creditor Scheme**_ Credit party that signs the mandate, may be used _Transaction_ _**Identification**_ supported by the Direct Debit Schema. (see next page **Min 0 – Max 1** 

Credit party that signs the mandate, may be used if supported by the Direct Debit Schema. (see next page for additional detail on this nested element) 

_**Pre Notification Identification**_ **Min 0 – Max 1** 

Unique and unambiguous identification of the pre-notification which is sent separately from the direct debit instruction. 

**==> picture [102 x 72] intentionally omitted <==**

**----- Start of picture text -----**<br>
Pre<br>Notification<br>Date<br>**----- End of picture text -----**<br>


_Direct Debit Transaction Information_ 

**==> picture [11 x 11] intentionally omitted <==**

---

<!-- ELEMENT 508 -->
## **Min 0 – Max 1** 

The _**Creditor Scheme Identification**_ element within the pacs.003 message optionally provides information related to the credit party that signs the mandate who is different from the Creditor. 

**==> picture [88 x 87] intentionally omitted <==**

The _**Creditor Scheme Identification**_ element offers the following options: 

Name 

Postal Address: Not used often Identification Country of Residence Contact Details 

**==> picture [54 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
CGI<br>**----- End of picture text -----**<br>


CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit Scheme. 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 509 -->
Mandatory _**Name**_ , where a BIC identifier is not provided, by which the party is known 

The ISO 20022 pacs messages describe the party credited for a transaction as the _**Creditor**_ . The _**Creditor**_ sub elements describe the _Creditor_ in greater detail. **Min 1 – Max 1** 

_**Name**_ 

**==> picture [198 x 295] intentionally omitted <==**

**==> picture [272 x 192] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Creditor<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Creditor_ address details 

**==> picture [92 x 90] intentionally omitted <==**

**----- Start of picture text -----**<br>
Identification<br>**----- End of picture text -----**<br>


Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

Optional element to _**Country of**_ capture the Creditor’s ISO _**Residence**_

---

<!-- ELEMENT 510 -->
**Min 0 – Max 1** The pacs.003 _**Creditor Account**_ is used to capture the account information for which a credit entry is intended to be applied to the Creditor’s account, which are also reflected in their account Statement. 

The _**Creditor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Creditor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency if the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) 

- **Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 511 -->
**Min 1 – Max 1 Min 1 – Max 1** The _**Debtor Agent**_ and _**Creditor Agent**_ are static roles in the pacs.003 FI to FI Customer Direct Debit. These agent maintain a relationship with their customers; the _Debtor_ and _Creditor_ . 

**==> picture [80 x 136] intentionally omitted <==**

**==> picture [84 x 137] intentionally omitted <==**

**==> picture [61 x 62] intentionally omitted <==**

Note: Although the _**Debtor Agent, Creditor Agent, Debtor and Creditor**_ all maintain static roles in the pacs messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section. 

_Direct Debit Transaction Information_ 

**==> picture [11 x 11] intentionally omitted <==**

---

<!-- ELEMENT 512 -->
## **Account** 

## **Min 0 – Max 1** 

The pacs.003 _**Debtor Agent Account**_ and _**Creditor Agent Account**_ are used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the direct debit transaction. 

The _**Debtor Agent Account**_ and _**Creditor Agent Account**_ use a variety of nested elements to capture information related to the account. 

**==> picture [73 x 78] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Account Servicing Institution 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account 

**Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Account Servicing Institution 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used. 

**==> picture [42 x 21] intentionally omitted <==**

---

<!-- ELEMENT 513 -->
The pacs.003 message introduces ultimate parties to the FI to FI Customer Direct Debit message. The _**Ultimate Creditor**_ element should not be confused with an _**Initiating Party**_ who may send a direct debit initiation request on behalf of the Creditor. (see dedication section on _Initiating Party_ ) 

**==> picture [257 x 175] intentionally omitted <==**

**----- Start of picture text -----**<br>
Ultimate<br>Party<br>Ultimate Ultimate<br>Debtor Creditor<br>**----- End of picture text -----**<br>


**Min 0 – Max 1** 

➢ CBPR+ premise is that an _**Ultimate Debtor**_ has no financial regulated direct account relationship with the corresponding _Debtor_ . **Min 0 – Max 1** ➢ CBPR+ premise is that an _**Ultimate Creditor**_ has no financial regulated direct account relationship with the corresponding _Creditor_ . 

An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor depending on the payment scenario) 

**==> picture [42 x 7] intentionally omitted <==**

_Direct Debit Transaction Information_ Ultimate Creditor

---

<!-- ELEMENT 514 -->
**==> picture [215 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initiating Party<br>Debtor Third Party<br>A<br>Debtor Agent<br>**----- End of picture text -----**<br>


**Min 0 – Max 1** 

**Min 1 – Max 1** 

The _**Initiating Party**_ of a direct debit is often the _**Creditor**_ themselves and therefore this optional element is not necessary. More often the _Initiating Party_ is a third party providing direct debit collection services on behalf of the _Creditor_ (often referred to as a Third Party Provider) whereby the _Creditor_ maintains an account with the Creditor Agent but the Third Party Provider has authority to initiate collection on behalf of the Creditor. This is distinctly different from an Ultimate Party (such as _Ultimate Creditor_ ) who instructs the _Creditor_ to initiate a collection on their behalf. 

**==> picture [61 x 62] intentionally omitted <==**

In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the _Initiating Party_ is often the _Creditor_ , however the same context of a Third Party Provider can exist where the third party is responsible for collecting funds on behalf of the _Creditor_ . 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 515 -->
**==> picture [47 x 48] intentionally omitted <==**

**==> picture [60 x 61] intentionally omitted <==**

**==> picture [61 x 61] intentionally omitted <==**

**==> picture [241 x 62] intentionally omitted <==**

**----- Start of picture text -----**<br>
B A<br>**----- End of picture text -----**<br>


**==> picture [341 x 164] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.003<br>Instructed Instructing<br>Agent: Agent B Agent: Agent A<br>**----- End of picture text -----**<br>


_**Instructing Agent**_ and _**Instructed Agent**_ represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment leg. 

_Instructing Agent_ and _Instructed Agent_ elements are required in all pacs messages and are available in the _**Direct Debit Transaction Information**_ 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 516 -->
The can to 3 which a role in the pacs message capture up Intermediary Agents, play dynamic payment between the Debtor Agent and Creditor Agent. 

**Min 0 – Max 1** 

**==> picture [61 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 1**_ captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 1 Account**_ captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a. 

## **Min 0 – Max 1** 

**2** 

**==> picture [51 x 37] intentionally omitted <==**

The _**Intermediary Agent 2**_ captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

The _**Intermediary Agent 2 Account**_ captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message. 

**Min 0 – Max 1** 

**==> picture [62 x 53] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>**----- End of picture text -----**<br>


The _**Intermediary Agent 3**_ captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message. **Min 0 – Max 1**

---

<!-- ELEMENT 517 -->
Mandatory _**Name**_ (where a BIC identifier is not provided) by which the party is known 

## The ISO 20022 pacs messages describe the party debited for a transaction as the _**Debtor**_ . The _**Debtor**_ sub elements describe the _Debtor_ in greater detail. **Min 1 – Max 1** 

_**Name**_ 

**==> picture [213 x 295] intentionally omitted <==**

**==> picture [272 x 192] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Debtor<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Debtor_ address details 

**==> picture [92 x 90] intentionally omitted <==**

**----- Start of picture text -----**<br>
Identification<br>**----- End of picture text -----**<br>


Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

Optional element to _**Country of**_ capture the Debtor’s ISO _**Residence**_

---

<!-- ELEMENT 518 -->
## **Min 1 – Max 1** 

The pacs.003 mandatory _**Debtor Account**_ is used to capture the account information for which debit entry is/has been applied to the Debtor’s account, which are also reflected in their account Statement. 

The _**Debtor Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 1  – Max 1** _**Identification**_ identifies the account maintained at the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 519 -->
## A children sports clubs (Creditor), collects its monthly membership fee via direct debit, against the parents (Debtor) of one of it members (Ultimate Debtor). 

**==> picture [808 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>4 3 2<br>pain.008<br>camt.053 pacs.003<br>B pacs.002 A pain.002<br>DR / CR<br>1 2 3 4<br>Sports club, the Creditor who  Agent A, the Creditor Agent,  Debtor Agent (B) debits the  Debtor, receives a statement<br>has a mandate* with the  initiates a direct debit  account of the Debtor, credits  from their bank confirming the<br>Debtor, initiates a direct debit  instruction by sending a  the account of the Creditor  monthly Debt Debit, for their<br>instruction by sending a  pacs.003 message to the  Agent and confirms the direct  child (Ultimate Debtors) sports<br>pain.008 message to their  Debtor Agent (B). debit status using a pain.002. club membership fee, has<br>bank, Creditor Agent (A). debited either account,<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 520 -->
## **Min 0 – Max 1** 

The _**Purpose**_ element within the pacs.003 FI to FI Customer Direct Debit captures the reason for the direct debit transaction which use an external ISO code or may either Purpose a proprietary code. The purpose is used to capture the nature of the payment e.g. IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Creditor. 

**==> picture [123 x 91] intentionally omitted <==**

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. 

For example, LOAR is classified within the Finance categorisation, with the _Name_ Loan Repayment described as a repayment of loan to lender. 

**==> picture [61 x 62] intentionally omitted <==**

_Category Purpose_ also captures a high level purpose, which unlike _Purpose_ is less granular but can trigger special processing e.g. Category Purpose code SALA ‘Salary Payment’ may trigger a reporting process which restricts sensitive data i.e., individual salary names. 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information_

---

<!-- ELEMENT 521 -->
## **Min 0 – Max 10** 

The _**Regulatory Reporting**_ element within the pacs.003 FI to FI Customer Direct Debit is nested to capture regulatory and statutory information needed to report to the appropriate authority/s. 

**Min 0 – Max 1** 

**==> picture [118 x 73] intentionally omitted <==**

- The _**Debit Credit Reporting Indicator**_ utilises an embedded choice of code to indicate whether the regulatory reporting information applies to the: • DEBT (debit) 

- • CRED (credit) or 

- • BOTH 

**Min 0 – Max 1** 

- The _**Authority**_ element captures the _**Name**_ and _**Country**_ code of the Authority/Entity requiring the regulatory reporting information. 

**Min 0 – Max *** 

The _**Details**_ element provides the detail on the regulatory reporting information. 

**==> picture [11 x 11] intentionally omitted <==**

_Direct Debit Transaction Information     Regulatory Reporting_

---

<!-- ELEMENT 522 -->
## **Min 0 – Max 1** 

The _**Related Remittance Information**_ element within the pacs.003 FI to FI Customer Direct Debit is nested to provide information related to the handling of remittance information. This information is typically provided by the Creditor in the direct debit initiation request. 

**Min 0 – Max 1** The _**Remittance Identification**_ captures a unique reference assigned by the initiating party of the collection to identify the remittance information sent separately from the direct debit instruction. 

**Min 0 – Max 2** 

**==> picture [92 x 83] intentionally omitted <==**

- The _**Remittance Location Details**_ uses a set of nested elements to provide information on either the location of or the delivery of remittance information. 

   - _**Method**_ requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email) 

   - _**Electronic Address**_ provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved. 

   - _**Postal Address**_ provides the postal address to which an agent is to send the remittance information 

**==> picture [53 x 49] intentionally omitted <==**

Remittance advices are typically considered as a traditional value added service provided by the Creditor Agent to the Creditor, in order to facilitate reconciliation for the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting messages. _**Remittance Information**_ is a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022. _Related Remittance Information_ and _Remittance Information_ are mutually exclusive (can’t both be present) 

Business examples are emerging where information is externalised using a URL repository solution.

---

<!-- ELEMENT 523 -->
The optional _**Remittance Information**_ element within the pacs.003 FI to FI Customer Direct Debit is nested to provide either _**Structured**_ or _**Unstructured**_ information related to direct debit collections, such as invoices. 

**Min 0 – Max 1** 

_**Remittance Information**_ enable the matching/reconciliation of an entry that the direct debit is intended to settle 

**==> picture [66 x 73] intentionally omitted <==**

**Min 0 – Max 1** 

The **Unstructured** sub element captures free format _Remittance Information_ which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence. 

**Min 0 – Max *** The **Structured** element is nested capturing rich structured _Remittance Information,_ and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification) The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-to-end transportation of this data. 

**==> picture [53 x 31] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [12 x 7] intentionally omitted <==**

_Related Remittance Information_ and _Remittance Information_ are

---

<!-- ELEMENT 524 -->
The bilaterally/multilaterally agreed _**Remittance Information**_ which is _**Structured**_ must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information. 

**==> picture [457 x 131] intentionally omitted <==**

## example of _Structured_ invoice information 

The _**Creditor Remittance Information**_ is provided to the _**Creditor**_ in the Cash Management Reporting messages’ Remittance Information component, for example, the camt.053 Bank to Customer Statement. 

**Structured** <Strd> xml tag In this example Referred Document **Reference Document** <Rf rdDocInf> Information and it nested elements has **Information** multiplicity which support up to 9,000 **Type** <Tp> business character of information. Whereby this element names **Code Or Proprietary** <CdOrPrtry > information element can be repeated to include more **Code** <Cd> **CINV** coded information such as another invoice. **Number** <Nb> **A0000101 Related Date** <Dt> **2019-10-29** 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [11 x 9] intentionally omitted <==**

_Direct Debit Transaction Information_ 

Remittance Information

---

<!-- ELEMENT 525 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

**Serial Financial Institution to Financial Institution Customer Direct Debit** Use Case p.3.1.1 – High Level FI to FI Customer Direct Debit (pacs.003) successful settlement Use Case p.3.1.2 – High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement

---

<!-- ELEMENT 526 -->
**==> picture [647 x 220] intentionally omitted <==**

**----- Start of picture text -----**<br>
3 2 1<br>pacs.003 pain.008<br>camt.053<br>B pacs.002 A pain.002<br>4<br>Settlement<br>Complete<br>3 4<br>Creditor Agent (A) relays the status<br>Creditor initiates a direct debit  The Debtor Agent debits the account<br>ACSC (accepted settlement<br>of the Debtor, and may optionally<br>instruction to the Creditor Agent completed) to the Initiating Party,<br>provide a notification e.g. debit<br>based upon a bilateral agreement<br>notification in addition to an account<br>**----- End of picture text -----**<br>


**==> picture [421 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 3<br>Creditor initiates a direct debit  The Debtor Agent debits the account<br>of the Debtor, and may optionally<br>instruction to the Creditor Agent<br>provide a notification e.g. debit<br>notification in addition to an account<br>2 statement (camt.053). The Debtor<br>Creditor Agent (A) initiates a  Agent also provides a status update<br>direct debit collection by  ACSC (accepted settlement<br>sending a pacs.003 message to  completed) to the Creditor Agent.<br>the Debtor Agent with the<br>settlement method “INDA”<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 527 -->
**==> picture [68 x 97] intentionally omitted <==**

**==> picture [183 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>Creditor initiates a direct debit<br>instruction to the Creditor Agent<br>2<br>Creditor Agent (A) initiates a<br>direct debit collection by<br>sending a pacs.003 message to<br>the Debtor Agent with the<br>settlement method “INDA”<br>**----- End of picture text -----**<br>


**==> picture [467 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
3 2 1<br>pacs.003 pain.008<br>B pacs.002 A pain.002<br>4<br>Reject<br>Reason<br>**----- End of picture text -----**<br>


**==> picture [469 x 129] intentionally omitted <==**

**----- Start of picture text -----**<br>
3 4<br>Creditor Agent (A) relays the status<br>RJCT (Rejected) to the Initiating<br>The Debtor Agent fails to debit the<br>Party with the rejection reason<br>account of the Debtor (e.g., account<br>information<br>is closed). The Debtor Agent<br>provides a status update RJCT<br>(Rejected) with the rejection reason<br>information.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 528 -->
# **messages**

---

<!-- ELEMENT 529 -->
**Cash Management Reporting camt.052** - Bank to Customer Account Report **camt.053** - Bank to Customer Statement **camt.054** - Bank to Customer Debit Credit Notification **camt.057** – Notification To Receive **camt.058** – Notification To Receive Cancellation Advice **camt.060** – Account Report Request

---

<!-- ELEMENT 530 -->
# **Bank to Customer Account Report** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 531 -->
**camt.052** 

The _Bank To Customer Account Report_ message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message. It can be used to inform the account owner, or authorised party, of: 

- entries reported to the account (Intraday Statement) 

Group Header 

- account balance information (Account Balance Report) 

- or both. 

- for a given point in time. 

**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Report<br>**----- End of picture text -----**<br>


**==> picture [60 x 56] intentionally omitted <==**

The Bank to Customer Account Report is restricted to a single account statements per InterAct message (100,000 bytes) 

This message must be bilaterally agreed between the Account Servicing

---

<!-- ELEMENT 532 -->
**==> picture [768 x 288] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pacs.008<br>pacs.002<br>camt.052 pacs.008<br>camt.052<br>camt.052 camt.052<br>**----- End of picture text -----**<br>


Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Account Report message to Account Servicer and Account Owner. Whereby the report is send by the Account Servicer to the Account

---

<!-- ELEMENT 534 -->
**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 cash management reporting message has a _Message Identification_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Cash Management (camt) messages the _Message Identification_ has no exact equivalent in the legacy MT Customer Statement message. However, the _Transaction Reference Number_ (Field 20) could be considered a similar comparison. 

_Group Header_ Message Identification

---

<!-- ELEMENT 535 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 536 -->
## **Min 0 – Max 1** 

The Bank to Customer Account Report _**Message Recipient**_ nested element provides details of the party authorised by the _Account Owner_ to receive the Account Report. 

This element **should only** be used to identify the _Message Recipient_ when different from the account owner, which is implied by the usage of COPY in the _Copy Duplicate Indicator_ within the nested Statement element. 

**==> picture [57 x 82] intentionally omitted <==**

## Where _**Message Recipient**_ is used the nested: 

- _**Name**_ **Min 0 – Max 1** 

- • _**Postal Address**_ **Min 0 – Max 1** 

- _**Postal Address**_ 

- _**Identification**_ 

**Min 0 – Max 1** 

- **Min 0 – Max 1** 

- _**Contact Details**_ 

- may be used to capture information related to this party. 

**==> picture [11 x 11] intentionally omitted <==**

_Group Header_ Message _Recipient Name_

---

<!-- ELEMENT 537 -->
**Min 0 – Max 1** The Bank to Customer Account Report _**Original Business Query**_ element identifies a query to generate a report, for example a camt.060 Account Reporting Request. 

**==> picture [103 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
?<br>**----- End of picture text -----**<br>


**Min 1 – Max 1** 

Where _**Original Business Query**_ is used the original _**Message identification**_ (i.e., the message identification of the camt.060 message) is required. Original _**Message Name identification**_ and Original _**Creation Date Time**_ may also be provided. **Min 0 – Max 1 Min 0 – Max 1** 

**==> picture [10 x 11] intentionally omitted <==**

_Group Header_ Original Business Query

---

<!-- ELEMENT 538 -->
**Min 0 – Max 1** The Bank to Customer Account Report _**Additional Information**_ element represents further details related to the account statement. 

**==> picture [82 x 85] intentionally omitted <==**

In accordance to the usage in the camt.053 this element could be used to describe additional information to distinguish the different camt.052 usage i.e., where the report is only reporting an intraday balance, intraday entries or both. Unlike the camt.053 there is no recommended identification string to represent usage. 

**==> picture [60 x 60] intentionally omitted <==**

Additional Information is a textual element restricted in CBPR+ to 500 characters. 

_Group Header_ Additional Information

---

<!-- ELEMENT 540 -->
## **Min 1 – Max 1** 

The Bank to Customer Account Report _**Report**_ element provides information related to an account, most typically associated with intraday account entries and or accounting balances (where entries have been processed on the account). The report element can be used to advise entries reported to the account (Intraday Statement), account balance information (Account Balance Report) or both. 

**==> picture [143 x 155] intentionally omitted <==**

The _Report_ element has been restricted to one account report. To report additional accounts to the Account Owner this would need to occur via a separate message in a similar way to the legacy MT 942. 

**==> picture [60 x 47] intentionally omitted <==**

It **should also be noted** the Account Report message is modelled identically to the Account Statement (camt.053) therefore where used as an intraday transaction report 

_Report_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 541 -->
**==> picture [808 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
Similar to the legacy MT Intraday Reporting message (i.e., 942) the camt.052<br>1 camt.052<br>Bank to Customer Account Report is constrained in CBPR+ by the FINplus<br>service’s message size. Consideration therefore need to be given (when 2 camt.052<br>D<br>reporting transactional information) to identifying; the report order , the report<br>correlation and the  last report page . 3 camt.052<br>1 Report Pagination 2 Report Pagination 3 Report Pagination<br>Page 1 Page 2 Page 3<br>Last Page  No<br>Last Page  No Last Page  Yes<br>Electronic Sequence Number  16<br>Electronic Sequence Number 16 Electronic Sequence Number  16<br>Legal Sequence Number  3<br>Legal Sequence Number  3 Legal Sequence Number  3<br>Account<br>Account Account<br>Id  12345<br>Id  12345 Id  12345<br>Currency  EUR<br>Currency  EUR      Currency  EUR<br>Entry<br>Entry Balance<br>….<br>….. ITAV Interim Available<br>Entry<br>……<br>**----- End of picture text -----**<br>


**Report Order:** identifying the order in which statements should be processed or reconstituted. Options: 

**==> picture [28 x 16] intentionally omitted <==**

**Report Correlation:** identifying statement which relate to each other for  a given statement period. Options: 

**==> picture [24 x 15] intentionally omitted <==**

_Legal Sequence Number_ 

**Last Report:** identifying when no further statements for a given period are expected i.e. period statement in finalised. Options: 

**==> picture [23 x 17] intentionally omitted <==**

_Report Pagination, Last Page Indicator_

---

<!-- ELEMENT 542 -->
## **Min 1 – Max 1** 

The Bank to Customer Account Report message _**Identification**_ provides a mandatory element to identify the statement 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 543 -->
## **Min 1 – Max 1** 

The Bank to Customer Account Report message _**Report Pagination**_ element provides the page number of the report. 

**==> picture [124 x 76] intentionally omitted <==**

**Min 1 – Max 1 Min 1 – Max 1** _**Report Pagination**_ includes the _**Page Number**_ and _**Last Page indicator**_ elements. 

**For example,** a _Page Number_ of 2 represents the current account report, being the second page of the and implying a previous account report page had been sent. The _Last Page indicator_ further implies whether more pages are expected 

**==> picture [60 x 47] intentionally omitted <==**

Noted: as **Report Pagination** is required, even if there is only one page to the report being sent. Both the **Page Number** and **Last Page indicator** will need to be provided 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 544 -->
**Min 0 – Max 1** 

The Bank to Customer Account Report message _**Electronic Sequence Number**_ allows the _Account Servicer_ to assign a number to each Report which should increment by 1 for each electronic statement report sent. 

> **1 3 4 2 5** 

This element allows easy recognition of the Report order, equivalent to the legacy Field 28C Statement Number. The sequence should increment for each camt.052 message sent to the Account Owner or Authorised Party this number must be the same value where the statement continues over multiple pages ( _Report Pagination_ ) of the report for a give account. 

Should this sequence number be reset by the _Account Servicer_ , this should not occur more frequently than once a day. Likewise, this 18 digit counter could be incremented to its maximum value before it’s reset. 

**==> picture [46 x 49] intentionally omitted <==**

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the _Account Servicer_ and the _Account Owner_ 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 545 -->
## **Min 0 – Max 1** 

**==> picture [17 x 16] intentionally omitted <==**

The Bank to Customer Account Report message _**Reporting Sequence**_ specifies the choice of identification sequences. This can be used as an alterative to the _**Report Pagination**_ or _**Electronic Sequence Number**_ as a way to identify the report order, which is not confined to numeric values. 

Where used the _**Reporting Sequence**_ mandate a choice of nested element: 

**A B D C** 

- **Min 1 –** 

- _**From Sequence**_ identifies the start of a sequence range. 

- • **Min 1 – Max 1** _**To Sequence**_ identifies the end of a sequence range. 

**Min 1 – Max 1** 

- _**From To Sequence**_ identifies the start and end of a sequence range. 

- • **Min 1 – Max *** _**Equal Sequence**_ identifies a sequence. 

- • _**Not Equal Sequence**_ identifies a sequence to be excluded. **Min 1 – Max *** 

**Min 1 – Max *** 

**==> picture [80 x 79] intentionally omitted <==**

**camt.060 camt report** 

**==> picture [79 x 71] intentionally omitted <==**

The Reporting Sequence may be provided in the camt.060 Account Reporting request to specify, for example, a range of Statements to be sent. Alternatively, Account Reports can often be produced on a bilaterally agreed period basis. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [19 x 7] intentionally omitted <==**

---

<!-- ELEMENT 546 -->
## **Min 0 – Max 1** 

The Bank to Customer Account Report message _**Legal Sequence Number**_ allows the _Account Servicer_ to assign a number to each report which should increment by 1 for each Report sent. 

**==> picture [106 x 35] intentionally omitted <==**

Where the Intraday Account Report uses multiple camt.052 messages for a given report period the _**Legal Sequence Number**_ must be the same number in each report message during that reporting period. This element can be considered an equivalent to the legacy Field 28C Statement Number 

**==> picture [46 x 49] intentionally omitted <==**

Either _**Electronic Sequence** Number_ or _**Legal Sequence Number**_ should be provided to enable the identification of a report number. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 547 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 548 -->
**Min 0 – Max 1** 

The Bank to Customer Account Report message _**From to Date**_ allows the _Account Servicer_ to specify the start date time and end date time applicable to the intraday account entries and or accounting balances being reported. 

For intraday account reports this is an important attribute that allows the account owner to understand the period for which the report applies. The element is not mandatory as the report may only contain the balance, whereby the report _**Creation DateTime**_ may be used to identify the date and time associated to the balance. 

**Min 1 – Max 1 Min 1 – Max 1** 

Where _**From to Date**_ is used the _**From Date Time**_ and _**To Date Time**_ become mandatory elements. CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 44] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are 

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 549 -->
**Min 0 – Max 1** 

The Bank to Customer Account Report message _**Copy Duplicate Indicator**_ is used as a choice to identify additional reports from the original sent to the Account Owner. 

**==> picture [68 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
COPY<br>**----- End of picture text -----**<br>


_**COPY**_ is used when a copy of the report is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service. 

_**DUPL**_ is used when a duplicate of the report is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. **DUPL** _**CODU**_ is used when a duplicate of a report copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in **CODU** place with the Account Servicer. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [19 x 7] intentionally omitted <==**

---

<!-- ELEMENT 550 -->
## **Min 0 – Max 1** 

The Bank to Customer Account Report message _**Reporting Source**_ allows the _Account Servicer_ to define the source of the intraday account entry and or account balance report, typically associated with an application. 

**==> picture [59 x 56] intentionally omitted <==**

_**Reporting Source**_ utilises the external Reporting Source code list. For example **ACCT** represents a statement or report based on accounting data, whereas **DEPT** represents a cash or deposit system. Where the source of the statement is functionally required by the consumer of the statement i.e., the _Account Owner_ or _authorised Third Party_ , the codes used should be bilaterally agreed. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [19 x 7] intentionally omitted <==**

---

<!-- ELEMENT 551 -->
## **Min 1 – Max 1** 

The Bank to Customer Account Report message _**Account**_ provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath _Account_ . 

**==> picture [211 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Account<br>**----- End of picture text -----**<br>


**Min 1 – Max 1** 

a unique _**Identification**_ for the account, between the _**Identification**_ Account Servicer and Account Owner. The element is further nested by choice of _**IBAN**_ or _**Other**_ to capture the account. 

**==> picture [104 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
Currency<br>**----- End of picture text -----**<br>


**Min 1 – Max 1** 

The _**Currency**_ for which the account is held. This is identified using the three characters ISO currency code. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 552 -->
**Min 0 – Max 1** 

**Min 1 – Max 1** 

The Bank to Customer Account Report message mandatory _**Account**_ also provides a number of optional nested element to identify the account for which debit and credit entries have been made. 

_**Type**_ 

An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. 

**==> picture [22 x 13] intentionally omitted <==**

_Account_ 

**==> picture [59 x 57] intentionally omitted <==**

**==> picture [16 x 17] intentionally omitted <==**

The Name of the Account, as Assigned by the servicing institution. 

_**Name Proxy Owner**_ 

A nested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO Proxy Account Type code or a proprietary code. 

A nest element that contains the Party that legally owns the account. 

**==> picture [15 x 14] intentionally omitted <==**

---

<!-- ELEMENT 553 -->
**Min 0 – Max 1** The Bank to Customer Account Report message _**Related Account**_ allows the identification of a related parent account for the account report. For example sweeping, pooling or virtual account for which the report is produced can identify the parent account they hierarchically relate to. 

**Min 1 – Max 1 Min 1 – Max 1** 

**==> picture [51 x 60] intentionally omitted <==**

**==> picture [73 x 57] intentionally omitted <==**

When _**Related Account**_ is utilized, like _**Account**_ , the _**Identification**_ and _**Currency**_ element become mandatory. 

Additionally, the nested _**Type**_ element, _**Name**_ and nested _**Proxy**_ element are optionally available. **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1** 

**==> picture [57 x 56] intentionally omitted <==**

_Related Account_ uses a variety of common elements described in more detail within the _Account_ section. 

_Report Related Account Identification Type_ 

**==> picture [20 x 10] intentionally omitted <==**

---

<!-- ELEMENT 554 -->
**Min 0 – Max *** 

The Bank to Customer Account Report message _**Interest**_ provides interest information that applies to the account. 

An element which may either use an embedded ISO Interest Type code; **INDY** (Intraday) **OVRN** (Over Night) or a proprietary code. It is used to identifier a particular interest type. 

_**Type**_ 

**==> picture [22 x 14] intentionally omitted <==**

The type of interest Rate defined as a _Percentage_ and in an _Other_ form. Validity Range optionally defines an _Amount_ , _Credit Debit Indicator_ and _Currency_ . 

_**Rate**_ 

**==> picture [93 x 22] intentionally omitted <==**

**----- Start of picture text -----**<br>
Interest<br>**----- End of picture text -----**<br>


**==> picture [17 x 17] intentionally omitted <==**

**==> picture [16 x 16] intentionally omitted <==**

The date range for which interest has been calculated. _From Date Time_ and _To Date Time_ must be representing when using this element. 

_**From To Date**_ 

**+** 

**-** 

**==> picture [15 x 16] intentionally omitted <==**

The optional Reason for which interest is applied. 

_**Reason**_ 

**==> picture [79 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
Tax<br>**----- End of picture text -----**<br>


Provides details on any tax applied to the Interest. Where optional

---

<!-- ELEMENT 555 -->
## **Min 0 – Max *** 

## The Bank to Customer Account Report message optional _**Balance**_ is a nested element to define the account balance at a specific point in time. The following four elements nested beneath _Balance_ are mandatory **Min 1 – Max 1** 

A nested element which may either use an external ISO Balance Type code or a proprietary code. For example, OPAV – Opening Available. _**Type**_ Additionally, a Sub Type represented by either use an external ISO Balance Sub Type code or a proprietary code, may be used. 

_Balance_ _**Amount**_ Balance amount. _**Credit Debit**_ Embedded code CRDT (Credit balance) DBIT (Debit balance) _**Indicator Date**_ A nested element representing the _Date_ and the _DateTime_ (with UTC 

**==> picture [22 x 7] intentionally omitted <==**

---

<!-- ELEMENT 556 -->
_Balance Type_ code are used within the nested _Balance_ element to represent the type/s of balance being reported. In comparison the legacy MT 941 utilizes different Fields and Tag options to represent a number of these Balance Types. The below extract from the externalised ISO _Balance Type_ code list compares the code with the population of the equivalent information in the Legacy MT 941 Balance Report. 

|**Code**|**Name**|**Definition**|**MT 941**<br>**Comparison**|
|---|---|---|---|
|**CLAV**|ClosingAvailable|Closing balance of amount of money that is at the disposal of the account owner on the date specified.|Field 64|
|**CLBD**|ClosingBooked|Balance of the account at the end of the pre-agreed account reporting period. It is the sum of the opening<br>booked balance at the beginning of the period and all entries booked to the account during the pre-agreed<br>accountreporting period.|**Field 62F**|
|**FWAV**|Forw ardAvailable|Forward available balance of money that is at the disposal of the account owner on the date specified.|**Field 65**|
|**INFO**|Information|Balance for informational purposes.|**No equivalent**|
|**ITAV**|InterimAvailable|Available balance calculated in the course of the account servicer's business day, at the time specified, and<br>subject to further changes during the business day. The interim balance is calculated on the basis of booked<br>credit and debit items during the calculation time/period specified.|**Field 64**|
|**ITBD**|InterimBooked|Balance calculated in the course of the account servicer's business day, at the time specified, and subject to<br>further changes during the business day. The interim balance is calculated on the basis of booked credit and<br>debit items during the calculation time/period specified.|**Field 62F**|
|**OPAV**|OpeningAvailable|Opening balance of amount of money that is at the disposal of the account owner on the date specified.|**No equivalent**|
|**OPBD**|OpeningBooked|Book balance of the account at the beginning of the account reporting period. It always equals the closing<br>book balance from the previous report.|**Field 60F**|
|**PRCD**|PreviouslyClosedBooked|Balance of the account at the previously closed account reporting period. The opening booked balance for the<br>new period has to be equal to this balance.<br>Usage: the previously booked closing balance should equal (inclusive date) the booked closing balance of the<br>date it references and equal the actual booked opening balance of the current date.|**No equivalent**|
|**XPCD**|Expected|Balance, composed of booked entries and pending items known at the time of calculation, which projects the<br>end of day balance if everything is booked on the account and no other entry is posted.|No equivalent|

---

<!-- ELEMENT 557 -->
**Min 1 – Max *** 

## The Bank to Customer Account Report message mandatory _**Balance**_ also provides the optional set of nested element to define a _**Credit Line**_ 

**Min 0 – Max *** 

The true/false Boolean of _**Included**_ to clearly determine whether the Credit Line Amount is included in the balance is mandatory in the set of Credit Line element. 

- Additionally, the following optional nested element may be used to identify: 

**==> picture [104 x 68] intentionally omitted <==**

- The _**Type**_ of Credit Line, which may either use an external ISO Credit Line Type code or a proprietary code. 

- A set of elements to provide _**Credit Line**_ details 

- The _**Amount**_ (Currency and Amount) of the Credit Line 

- The _**Date**_ (nested as Date, DateTime) of the Credit Line, provided to distinguish where multiple Credit Line exist. 

The final optional nested element within _**Balance**_ is the _**Availability**_ of the booked amount i.e., when it is available to be accessed. 

**==> picture [57 x 51] intentionally omitted <==**

The _Credit Line_ element is unlimited (Max *) whereby more that one _Credit Line_ may be reported, the _Date_ becomes an important element to distinguish between different Credit Lines. 

_Report Balance Type Credit Line Amount_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 558 -->
**Min 0 – Max 1** 

The Bank to Customer Account Report message optional _**Transaction Summary**_ provides a set of nested element to summarize entry information. Where the intraday account entries and or accounting balances are reported using multiple camt.052 messages for a given reporting period the _Transaction Summary_ should only be included on the first Report message ( _Balance Type_ OPBD with no Balance _Sub Type_ ) summarizing the whole Statement Report (entire statement period) This aligns with the Common Global Implementation (CGI) where a _Transaction Summary_ , if provided, would appear before the first _Entry_ elements. 

**==> picture [70 x 79] intentionally omitted <==**

Each of the following element allow an optional total of entries either as a _**Number of Entries**_ and or as a _**Sum**_ . 

- ➢ _**Total Entries**_ 

- ➢ _**Total Credit Entries**_ 

- ➢ _**Total Debit Entries**_ 

- ➢ _**Total Entries Per Bank Transaction Code**_ 

**Min 0 – Max *** 

In addition to the _**Number of Entries**_ and _**Sum**_ , the _**Total Entries Per Bank Transaction Code**_ requires the _**Bank Transaction Code**_ element and optionally allows a variety of other optional elements. **Min 1 – Max 1** 

**==> picture [57 x 51] intentionally omitted <==**

The _Total Entries Per Bank Transaction Code_ element is unlimited (Max *) whereby more that one _Bank Transaction Code_ may be summarised. 

_Report Transaction Summary Total Entries_ 

**==> picture [10 x 9] intentionally omitted <==**

_Total Credit Entries_ 

_Total Debit Entries_ 

**==> picture [10 x 10] intentionally omitted <==**

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 559 -->
## **Min 0 – Max *** 

The Bank to Customer Account Report message optional _**Entry**_ provides a significant variety of nested elements to represent the details associated with each _**Entry**_ . For active accounts which have intraday entries posted across them, this set of nested elements is arguably the most relevant for the account owner and in many way is comparable with the MT 942 Field 61 Statement Line. 

**==> picture [47 x 82] intentionally omitted <==**

**==> picture [505 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 0 – Max 1 Min 1 – Max 1 Min 1 – Max 1 Min 0 – Max 1 Min 1 – Max 1<br>Credit<br>Entry Debit Reversal<br>Amount Status<br>Reference Indicator<br>Indicator<br>Min 0 – Max 1 Min 1 – Max 1 Min 0 – Max 1 Min 0 – Max * Min 1 – Max 1<br>Account Bank<br>Booking Value<br>Date Date Servicer Availability Transaction<br>Reference Code<br>Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1<br>Commission Additional Technical<br>Amount<br>Waiver Information Charges Input<br>Details<br>Indicator Indicator Channel<br>Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max * Min 0 – Max 1<br>Additional Report Entry<br>C d<br>**----- End of picture text -----**<br>


Unlike the legacy MT Interim Transaction Report message, the camt.052 has a number of dedicated elements to capture a variety of entry level data. It also has a number of enhancements on the legacy MT Interim Transaction Report message where parties in the payment and customer remittance information, as examples, can provided to the _Account Owner._

---

<!-- ELEMENT 560 -->
**Min 0 – Max 1** 

_**Entry Reference**_ 

Unique reference for the booking entry, created by the Account Servicing Institution as a reference they assign to identify the entry posted to the account. 

**Min 1 – Max 1** 

Mandatory element representing the currency and amount of the entry. This can be compared to Field 61 subfield 4 and 5 of the legacy MT 942. 

_**Amount**_ 

**==> picture [103 x 211] intentionally omitted <==**

**Min 1 – Max 1** _**Credit Debit Indicator**_ **Min 0 – Max 1** 

Mandatory element indicating whether the _**Amount**_ entry is a **DBIT** (Debit) or **CRDT** (Credit) to the account. This can be compared to Field 61 subfield 3 of the legacy MT 942. 

Indicates whether the entry is a result of a reversal. for example, an entry related to a pacs.004 Payment Return or reverses an error such as an incorrect value date applied to the entry. Where the _**Reversal Indicator**_ is **Yes,** the _**Credit Debit Indicator**_ should be the opposite of the original entry, for example original _**Credit Debit Indicator**_ of **CRDT** would expect a reversal entry 

_**Reversal Indicator**_

---

<!-- ELEMENT 561 -->
**==> picture [46 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1<br>**----- End of picture text -----**<br>


Mandatory element representing the status using an external ISO Entry Status code for example BOOK is _**Status**_ used to confirm the entry is booked. 

Status BOOK is the only status that can be reversed using the _**Reverse Indicator**_ 

**Min 0 – Max 1** 

**==> picture [47 x 82] intentionally omitted <==**

**==> picture [17 x 17] intentionally omitted <==**

_**Booking Date**_ 

Mandatory choice of _**Date**_ or _**Date Time**_ the entry was posted to the _**Account**_ . This can be compared to Field 61 subfield 2 of the legacy MT 942. 

**==> picture [23 x 13] intentionally omitted <==**

Noting CBPR+ usage guidelines mandate the time zone that the _**Date Time**_ represents as an offset against Universal Time Coordinated (UTC) 

**==> picture [63 x 62] intentionally omitted <==**

**Min 1 – Max 1** 

Mandatory choice of _**Date**_ or _**Date Time**_ the entry become available. This can be compared to Field 61 subfield 1 of the legacy MT 942. 

_**Value Date**_ 

**==> picture [23 x 14] intentionally omitted <==**

**Min 0 – Max 1** _**Account Servicer Reference**_ 

Additional optional Reference typically assigned by the Account Servicer’s payment engine or accounting platform. This reference would be used to query an entry. This can be compared to Field 61 subfield 8 of the legacy MT 942. 

**Min 0 – Max *** 

_**Availability**_ 

Indicates when the booked amount is available i.e., when it is available to be accessed. 

**==> picture [14 x 5] intentionally omitted <==**

---

<!-- ELEMENT 562 -->
**Min 1 – Max 1** 

_**Bank**_ The _**Bank Transaction Code Transaction**_ is designed to deliver a _**Code**_ harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the **account servicer** to correctly report a transaction, which in its turn will help **account owners** to perform their cash management and reconciliation operations. 

Domain Family Sub-Family 

The structure of the Bank Transaction Code has three levels: _**Domain**_ : Highest definition level to identify the subledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.) **Family** : Medium definition level e.g. type of payment; credit transfer, direct debit etc. _**Sub-family**_ : Lowest definition level e.g. type of cheques; draft etc. 

Bank Transaction Codes are an external code set defined in the _Bank Transaction Code combinations_ external code sets. 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

---

<!-- ELEMENT 563 -->
**==> picture [387 x 171] intentionally omitted <==**

**Min 1 – Max 1** The description of _**Bank Transaction Codes**_ are available to download from the ISO20022.org external code list page. These include the descriptions for Payments Domain Families and sub-families for both Received and Issued Credit Transfers. https://www.iso20022.org/external_code_list.page

---

<!-- ELEMENT 564 -->
**==> picture [705 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Bank Transaction Code - all permitted combinations of the BTC code sets<br>All codes in light grey are defined as the generic codes available for all Domains and Families<br>Domain Family SubFamily<br>Payments Issued Credit Transfers Cross-Border Credit Transfer PMNT ICDT XBCT New 27/4/2009<br>Payments Received Credit  Cross-Border Credit Transfer PMNT RCDT XBCT New 27/4/2009<br>Transfers<br>Status<br>Domain CodeFamily CodeSubFamily Code Status Date<br>ExternalBankTransactionDomain1CodeExternalBankTransactionFamily1CodeExternalBankTransactionSubFamily1Code<br>**----- End of picture text -----**<br>


Bank Transaction Codes are an external code set defined in the _Bank Transaction Code combinations_ external code sets. 

As an example a debit statement transaction which relates to a cross-border payment initiated from an account would be represented by: 

**Domain Family Sub-Family** PMNT (Payment) ICDT (Issued Credit Transfer) XBCT (Cross-Border Credit Transfer

---

<!-- ELEMENT 565 -->
**==> picture [55 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 0 – Max 1<br>**----- End of picture text -----**<br>


_**Commission Waiver Indicator**_ 

**==> picture [103 x 211] intentionally omitted <==**

Optional element indicating, as a Boolean, whether the entry is exempt from commission. This element is not typically associated with Correspondent Banking payments 

**Min 0 – Max 1** Optional element indicating whether the underlying transaction details are provided through a _**Additional**_ separate message. Where the _**Message Name Identification**_ represents the message used to _**Information**_ provide the additional information and _**Message Identification**_ specifies the reference of the _**Indicator**_ message that provides the additional information. 

Optional nested element which provides various elements to represent an aggregated (consolidated) original amount. Where individual transaction amounts can be represented, if required, within the _**Entry Detail**_ set of elements. 

**Min 0 – Max 1** 

_**Amount Details**_ **Min 0 – Max 1** 

This element is useful to capture original amount details where they are different to the **Entry** , **Amount** , for example the _**Instructed Amount**_ of the payment can be included, together with a potential _**Currency Exchange**_ rate, where necessary. 

Optional nested element to provide information on charges either pre-advised or taken from the entry. 

_**Charges**_ 

**==> picture [14 x 14] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 566 -->
**==> picture [56 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 0 – Max 1<br>**----- End of picture text -----**<br>


_**Technical Input Channel**_ 

**==> picture [23 x 12] intentionally omitted <==**

Optional element which may either use an external ISO Technical Input Channel code or a proprietary code used to represent the technical channel used to input the entry. 

**Min 0 – Max 1** _**Interest**_ 

Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry amount. 

**==> picture [14 x 13] intentionally omitted <==**

**Min 0 – Max 1** 

**==> picture [47 x 82] intentionally omitted <==**

**==> picture [17 x 16] intentionally omitted <==**

Optional nested element which provides details associated with a card transaction such as the card number, card brand etc. 

_**Card Transactions**_ **Min 0 – Max *** 

_**Entry**_ Additional optional nested element containing details on the entry. See dedicated section on _**Details**_ . _**Entry Details**_ 

**Min 0 – Max 1** _**Additional Statement**_ 

Additional optional element to represent further information related to the account 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 567 -->
## **Min 0 – Max *** 

The Bank to Customer Account Report message optional _**Entry Details**_ provides a variety of nested elements . to represent the details associated with each _**Entry**_ 

**==> picture [47 x 82] intentionally omitted <==**

_**Batch**_ provides details on batched transactions such as the total _**Number of Transactions**_ the batched entry (sometimes referred to as a consolidated entry) represents. _**Transaction Details**_ is a significant nested element which represents information on the underlying transaction. 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 568 -->
**Min 0 – Max *** 

**Min 1 – Max 1** 

When the Bank to Customer Account Report message optional _**Entry Details**_ is utilized the nested _**Transaction Details**_ element is mandatory. 

_**Transaction Details**_ has a variety of nested elements closely associated with _**Entry**_ level elements. The _**References**_ element however is nested to include a variety of references related to the entry including for example the _**UETR**_ 

**==> picture [784 x 168] intentionally omitted <==**

**----- Start of picture text -----**<br>
$ Min 1 – Max 1 Min 1 – Max 1 Min 1 – Max 1 Credit Min 0 – Max 1 Min 0 – Max* Min 0 – Max 1 Bank Min 0 – Max 1 Min 0 – Max 1<br>Amount<br>References Amount Debit Details Availability Transaction Charges Interest<br>Indicator Code<br>Additionally, Transaction Details  also has a variety of elements capturing details from the underlying<br>transaction, which amongst other business transactions includes payment transaction data. For example,<br>Remittance Information  and  Related Parties<br>**----- End of picture text -----**<br>


**==> picture [10 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 569 -->
**Min 0 – Max 1** 

**Min 0 – Max 1** 

The Bank to Customer Account Report message _**Related Parties**_ and _**Related Agents**_ represents a set of optional nested elements related to the underlying transaction. Where the _**Entry Details**_ (the set of elements _Related Parties/Agents_ belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message. 

**==> picture [106 x 98] intentionally omitted <==**

- These _**Related Parties**_ include : These _**Related Agents**_ include : • • _Instructing Party Instructing Agent_ 

- • • _Debtor Instructed Agent_ 

- • • _Debtor Account Debtor Agent_ 

- • • _Ultimate Debtor Creditor Agent_ 

- • • _Creditor Intermediary Agent 1_ 

- • • _Creditor Account Intermediary Agent 2_ 

- • • _Ultimate Creditor Intermediary Agent 3_ 

**==> picture [57 x 50] intentionally omitted <==**

_**Trading Party**_ is also present in the _**Related Parties**_ elements, and the following are present in the _**Related Agents**_ elements: _**Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place**_ . Although these elements are not directly associated with a payment, as a Customer receiving an Account Report related to other Business Domains e.g. a Security

---

<!-- ELEMENT 570 -->
## The Bank to Customer Account Report message _**Entry Details**_ have a number of additional elements beyond _**Related Parties**_ and _**Related Agents**_ to capture information from the underlying payment. 

## These are: 

- _Local Instrument_ 

- _Purpose_ 

- _Related Remittance Information_ 

**==> picture [46 x 82] intentionally omitted <==**

- _Remittance Information_ 

- _Related Dates_ such as the _Interbank Settlement Date_ 

- • _Tax_ 

- For _Payment Return_ (pacs.004) it is also possible to capture _**Return Information**_ which includes: 

- The _Original Bank Transaction Code_ of the original Entry 

- The _Originator_ of the return from the pacs.004 

- And the _Reason_ code. 

**==> picture [60 x 47] intentionally omitted <==**

_**Remittance Information**_ as an end-to-end element should be passed unaltered from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account

---

<!-- ELEMENT 571 -->
It should also be mentioned that the Bank to Customer Account Report message _**Entry Details**_ have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture _**Additional Transaction Information**_ . 

## These are: 

**==> picture [46 x 82] intentionally omitted <==**

- _Related Quantity_ 

- _Financial Instrument Identification_ 

- _Corporate Action_ 

- _Safekeeping Account_ 

- _Cash Deposit_ 

- • _Card Transactions_

---

<!-- ELEMENT 572 -->
Use case should be considered as a principal example whereby use case may be cross referenced 

## **Bank to Customer Reports** 

Use Case c.52.1.a – Bank to Customer Account Balance Report produced by the Creditor Agent Use Case c.52.1.b – Bank to Customer Account Intraday Transaction Report produced by the Creditor Agent Use Case c.52.1.b.1 – Bank to Customer Account Intraday Transaction Report/s and Account Statement produced by the Creditor Agent Use Case c.52.1.c – Bank to Customer Account Intraday Transaction and Balance Report produced by the Creditor Agent 

Use Case camt.060 for requesting a Bank to Customer report 

Use Case for copy or duplicate reports refer to camt.053 use cases

---

<!-- ELEMENT 573 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>pacs.008 pacs.008 pacs.008 camt.052<br>D<br>A B C<br>6<br>1 3<br>5<br>Debtor initiates a payment  Agent B processes the payment<br>Creditor Agent credits the<br>instruction to the Debtor Agent on Agent C account of the Creditor<br>2 4 6<br>Debtor Agent (A) initiates a  Agent C processes the payment  Creditor Agent as the Account<br>serial payment towards the  on Agent D Servicer produces and sends a<br>Creditor Agent (D) using<br>balance report to either the<br>Agents B & C as intermediaries Account Owner, or an<br>authorised third party.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 574 -->
## **Creditor Agent** 

**==> picture [780 x 313] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>pacs.008 pacs.008 pacs.008 camt.052<br>D<br>A B C<br>6<br>1 3<br>5<br>Debtor initiates a payment  Agent B processes the payment<br>Creditor Agent credits the<br>instruction to the Debtor Agent on Agent C account of the Creditor<br>2 4 6<br>Debtor Agent (A) initiates a  Agent C processes the payment  Creditor Agent as the Account<br>serial payment towards the  on Agent D Servicer produces and sends a<br>Creditor Agent (D) using<br>balance report to either the<br>Agents B & C as intermediaries Account Owner, or an<br>authorised third party.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 575 -->
## **Statement produced by the Creditor Agent** 

**==> picture [721 x 338] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5 6<br>pacs.008 pacs.008 pacs.008 camt.052<br>D<br>A B C<br>camt.053<br>7<br>6<br>1 Creditor Agent as the Account<br>Servicer produces and sends<br>Debtor initiates a payment<br>several intraday transaction<br>instruction to the Debtor Agent<br>reports throughout the business<br>day to either the Account<br>Owner, or an authorised third<br>4<br>2<br>party.<br>Agent C processes the payment<br>Debtor Agent (A) initiates a<br>on Agent D<br>serial payment towards the<br>Creditor Agent (D) using<br>7<br>Agents B & C as intermediaries<br>5 Creditor Agent C as the<br>Creditor Agent credits the  Account Servicer produces an<br>account of the Creditor Account Statement at the close<br>3<br>of the business day reflecting all<br>Agent B processes the payment  the transaction entries, include<br>on Agent C<br>those provide in the Intraday<br>**----- End of picture text -----**<br>


**==> picture [61 x 63] intentionally omitted <==**

---

<!-- ELEMENT 576 -->
## **by the Creditor Agent** 

**==> picture [721 x 326] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>pacs.008 pacs.008 pacs.008 camt.052<br>D<br>A B C<br>6<br>1 3<br>5<br>Debtor initiates a payment  Agent B processes the payment<br>Creditor Agent credits the<br>instruction to the Debtor Agent on Agent C account of the Creditor<br>2 4 6<br>Debtor Agent (A) initiates a  Agent C processes the payment  Creditor Agent as the Account<br>serial payment towards the  on Agent D Servicer produces and sends a<br>Creditor Agent (D) using<br>intraday transaction and<br>Agents B & C as intermediaries<br>balance report to either the<br>Account Owner, or an<br>authorised third party.<br>**----- End of picture text -----**<br>


**==> picture [61 x 63] intentionally omitted <==**

---

<!-- ELEMENT 577 -->
## **Bank to Customer Statement** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 578 -->
**camt.053** 

Group Header 

Statement 

**==> picture [60 x 60] intentionally omitted <==**

The _Bank To Customer Statement_ message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message. It is used to inform the account owner, or authorised party, of the entries booked to the account, and to provide the owner with balance information on the account at a given point in time 

The Bank to Customer Account Statement is restricted to a single account statements per InterAct message (100,000 bytes) This message must be bilaterally agreed between the Account Servicing Institution and the Account owner, and is establish by an

---

<!-- ELEMENT 579 -->
**==> picture [768 x 288] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pacs.008<br>pacs.002<br>camt.053 pacs.008<br>camt.053<br>camt.053 camt.053<br>**----- End of picture text -----**<br>


Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Statement message to Account Servicer and Account Owner. Whereby the statement is send by the Account Servicer to the Account

---

<!-- ELEMENT 580 -->
Like the legacy MT Statement messages, the camt.053 Bank to Customer Account Statement is constrained in CBPR+ by the FINplus service’s message size. Account Owner who needs to translate the camt.053 into the legacy MT 940 format has several considerations for the Account Serving Institution. 

**==> picture [59 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
ISO<br>**----- End of picture text -----**<br>


**==> picture [165 x 18] intentionally omitted <==**

**----- Start of picture text -----**<br>
ISO 20022 message element<br>**----- End of picture text -----**<br>


**==> picture [40 x 51] intentionally omitted <==**

**==> picture [60 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
MT<br>**----- End of picture text -----**<br>


MT Field Name & (Tag option) 

**==> picture [16 x 19] intentionally omitted <==**

_Statement Identification Legal Sequence Number Statement Pagination_ 

**==> picture [25 x 16] intentionally omitted <==**

**==> picture [26 x 20] intentionally omitted <==**

needed to create MT 940 Field 20 Transaction Reference Number 

needed to create MT 940 Field 28C Statement Number 

needed to create MT 940 Field 28C Sequence Number 

**==> picture [16 x 16] intentionally omitted <==**

_Account_ (Identification) 

needed to create MT 940 Field 25a  Account Identification 

**==> picture [22 x 15] intentionally omitted <==**

**==> picture [14 x 20] intentionally omitted <==**

## _Balance Type_ 

**OPBD** (with no _Sub Type_ INTM) **OPBD** (with _Sub Type_ **INTM** ) 

_Entry_ 

needed to create MT 940 Field 60F  (first) Opening Balance needed to create MT 940 Field 60M (intermediate) Opening Balance used to create MT 940 Field 61 Statement Line 

**==> picture [22 x 15] intentionally omitted <==**

## _Balance Type_ 

**CLBD** (with no _Sub Type_ INTM) 

Note up to 190 _**Entry**_ occurrences will translate into a basic MT 940 (inside of the existing MT 940 message size) 

**==> picture [18 x 17] intentionally omitted <==**

needed to create MT 940 Field 62F  (final) Closing Balance

---

<!-- ELEMENT 581 -->
Interest rate changes on an account can be communicated using the camt.053. An Account Serving Institution who is considering the camt.053 to communicate such rate changes to the Account Owner may find the following comparison against the legacy MT 935 useful. However, compared the camt.053 to legacy MT, using the camt.053 is like combining the information of both the MT 935 and MT 940 together into one message. 

**MT** MT Field Name & (Tag option) 

**==> picture [40 x 52] intentionally omitted <==**

**==> picture [165 x 68] intentionally omitted <==**

**----- Start of picture text -----**<br>
ISO<br>ISO 20022 message element<br>**----- End of picture text -----**<br>


- ➢ **Transaction Reference Number** (Field 20) 

## **Sequence** 

- ➢ **Further Identification** (Field 13C) ➢ **Account Identification** (Field 25) 

- ➢ **Effective Date of New Rate** (Field 30) ➢ **New Interest Rate** (Field 37H) 

**==> picture [73 x 16] intentionally omitted <==**

**----- Start of picture text -----**<br>
NOT MAPPED<br>**----- End of picture text -----**<br>


   - ➢ _**Group Header / Message Identification**_ 

   - ➢ _**Statement / Account / Identification**_ ➢ _**Statement / Interest / From Date**_ ➢ _**Statement / Interest / Rate**_ 

- ➢ **Sender To Receiver Information** (Field 72) 

## **NOT MAPPED** 

_**Note** - various other elements are mandatory in the camt.053 which are not derived from the payment instruction including_ _**; Message Identification, Creation Date Time, Statement Identification, Statement Pagination, Balance,  Credit Debit Indicator, Status, Bank Transaction Code/..** often these data elements and potentially other optional elements will be generated by the bank application when creating  th e reporting message._

---

<!-- ELEMENT 583 -->
**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 cash management reporting message has a _Message Identification_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Cash Management (camt) messages the _Message Identification_ has no exact equivalent in the legacy MT Customer Statement message. However, the _Transaction Reference Number_ (Field 20) could be considered a similar comparison. 

_Group Header_ Message Identification

---

<!-- ELEMENT 584 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 585 -->
**Min 0 – Max 1** The Bank to Customer Statement _**Message Recipient**_ nested element provides details of the party authorised by the _Account Owner_ to receive the Account Statement. 

This element **should only** be used to identify the _Message Recipient_ when different from the account owner, which is implied by the usage of COPY in the _Copy Duplicate Indicator_ within the nested Statement element. 

**==> picture [57 x 82] intentionally omitted <==**

## Where _**Message Recipient**_ is used the nested: 

- _**Name**_ **Min 0 – Max 1** 

- • _**Postal Address**_ **Min 0 – Max 1** 

- _**Postal Address**_ 

- _**Identification**_ 

**Min 0 – Max 1** 

- **Min 0 – Max 1** 

- _**Contact Details**_ 

may be used to capture information related to this party. 

**==> picture [11 x 11] intentionally omitted <==**

_Group Header_ Message _Recipient Name_

---

<!-- ELEMENT 586 -->
**Min 0 – Max 1** The Bank to Customer Statement _**Original Business Query**_ element identifies a query to generate a report, for example a camt.060 Account Reporting Request. 

**==> picture [103 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
?<br>**----- End of picture text -----**<br>


**Min 1 – Max 1** 

Where _**Original Business Query**_ is used the original _**Message identification**_ (i.e., the message identification of the camt.060 message) is required. Original _**Message Name identification**_ and Original _**Creation Date Time**_ may also be provided. **Min 0 – Max 1 Min 0 – Max 1** 

**==> picture [10 x 11] intentionally omitted <==**

_Group Header_ Original Business Query

---

<!-- ELEMENT 587 -->
## **Min 0 – Max 1** 

The Bank to Customer Statement _**Additional Information**_ element represents further details related to the account statement. 

**==> picture [82 x 85] intentionally omitted <==**

Where the camt.053 is used for various end of cycle statement reporting (statement periods) the follow codes may be used to distinguish the different camt.053 usage: 

**/EODY/** for End of Day - Daily Statement **/EOWK/** for End of Week - Weekly Statement **/EOMH/** for End of Month - Monthly Statement **/EOYR/** for End of Year - Yearly Statement 

**==> picture [60 x 60] intentionally omitted <==**

Additional Information is a textual element restricted in CBPR+ to 500 characters. 

**==> picture [10 x 10] intentionally omitted <==**

_Group Header_ 

Additional Information

---

<!-- ELEMENT 589 -->
## **Min 1 – Max 1** 

The Bank to Customer Account Statement _**Statement**_ nested element reports information related to an account, most typically associated with account balances, and accounting entries (where entries have been processed on the account). 

The _Statement_ element has been restricted to one statements. To report additional account statements to the Account Owner this would need to occur via a separate message in a similar way to the legacy MT 940 or MT 950. 

**==> picture [56 x 66] intentionally omitted <==**

**==> picture [60 x 47] intentionally omitted <==**

It **should also be noted** the Account Statement message is modelled identically to the Account Report (camt.052) therefore where an intraday transaction report is used the 

_Statement_ 

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 590 -->
**==> picture [808 x 287] intentionally omitted <==**

**----- Start of picture text -----**<br>
Similar to the legacy MT Statement messages the camt.053 Bank to Customer 1 camt.053<br>Account Statement is constrained in CBPR+ by the FINplus service’s message<br>2 camt.053<br>size. Consideration therefore need to be given to identifying; the statement D<br>order , the  statement correlation  and the  last statement page . 3 camt.053<br>1 Statement Pagination 2 Statement Pagination 3 Statement Pagination<br>Page 1 Page 2 Page 3<br>Last Page  No<br>Last Page  No Last Page  Yes<br>Electronic Sequence Number  16<br>Electronic Sequence Number 16 Electronic Sequence Number  16<br>Legal Sequence Number  3<br>Legal Sequence Number  3 Legal Sequence Number  3<br>Account<br>Account Account<br>Id  12345<br>Id  12345 Id  12345<br>Currency  EUR<br>Currency  EUR      Currency  EUR<br>Balance<br>Balance Balance<br>OPBD  (Opening Booked)<br>OPBD  (Opening Booked)  Closing Interim  OPBD  (Opening Booked)<br>Sub Type  CLBDINTM  (Closing Booked)  (Interim) of  next statementOpening Interim= Sub Type Sub Type  CLBDINTMINTM  (Closing Booked)  (Interim) (Interim) of  next statementOpening InterimClosing Interim = Sub Type  CLBDINTM   Closing Booked (Interim)<br>**----- End of picture text -----**<br>


**Statement Order:** identifying the order in which statements should be processed or reconstituted. Options: 

**==> picture [28 x 16] intentionally omitted <==**

**Last Statement:** identifying when no further statements for a given period are expected i.e. period statement in finalised. Options: 

**Statement Correlation:** identifying statement which relate to each other for  a given statement period. Options: 

_Legal Sequence Number_ 

**==> picture [23 x 16] intentionally omitted <==**

**==> picture [28 x 15] intentionally omitted <==**

---

<!-- ELEMENT 591 -->
**Min 1 – Max 1** 

The Bank to Customer Statement message _**Identification**_ provides a mandatory element to identify the statement 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the account servicer to unambiguously identify the account statement. Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 592 -->
## **Min 1 – Max 1** 

The Bank to Customer Statement message _**Statement Pagination**_ element provides the page number of the statement. 

**==> picture [124 x 76] intentionally omitted <==**

**Min 1 – Max 1 Min 1 – Max 1** _**Statement Pagination**_ includes the _**Page Number**_ and _**Last Page indicator**_ elements. 

**For example** a _Page Number_ of 2 represents the current account statement, being the second page of the and implying a previous account statement page had been sent. The _Last Page indicator_ further implies whether more pages are expected 

**==> picture [60 x 60] intentionally omitted <==**

Note: Where Page Number is equal to 1 a Balance Type OPBD (Opening Booked)must be provided, without a sub type of INTM (Interim). Whereas if the Page Number is greater than 1 a Balance Type OPBD (Opening Booked) must be provided, with a sub type of INTM (Interim). Where Last Page Indicator is true a Balance Type CLBD (Closing Booked) must be provided, without a sub type of INTM (Interim). Whereas if the Last Page Indicator is false a Balance Type CLBD (Closed Booked) must be provided, with a sub type of INTM (Interim). 

**==> picture [11 x 7] intentionally omitted <==**

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 593 -->
**Min 0 – Max 1** 

The Bank to Customer Statement message _**Electronic Sequence Number**_ allows the _Account Servicer_ to assign a number to each statement which should increment by 1 for each electronic statement report sent. 

> **1 3 4 2 5** 

This element allows easy recognition of the statement order, equivalent to the legacy Field 28C Statement Number. The sequence should increment for each camt.053 electronic statement sent to the Account Owner or Authorised Party this number must be the same value where the statement continues over multiple pages ( _Statement Pagination_ ) of the statement for a give account on a given day. 

Should this sequence number be reset by the _Account Servicer_ , this should not occur more frequently than once a year. Likewise, this 18 digit counter could be incremented to its maximum value before it’s reset. 

**==> picture [46 x 49] intentionally omitted <==**

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the _Account Servicer_ and the _Account Owner._ 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 594 -->
## **Min 0 – Max 1** 

**==> picture [17 x 16] intentionally omitted <==**

The Bank to Customer Statement the choice of identification message _**Reporting Sequence**_ specifies This can be used as an alterative to the _**Statement**_ or _**Number**_ sequences. _**Pagination Electronic Sequence**_ as a way to identify the statement order, which is not confined to numeric values. 

Where used the _**Reporting Sequence**_ mandate a choice of nested element: 

- **Min 1 – Max 1** 

- _**From Sequence**_ identifies the start of a sequence range. 

- **A B** • **Min 1 – Max 1** _**To Sequence**_ identifies the end of a sequence range. 

- • _**From To Sequence**_ identifies the start and end of a sequence range. 

- • **Min 1 – Max *** _**Equal Sequence**_ identifies a sequence. 

- **D C** • _**Not Equal Sequence**_ identifies a sequence to be excluded. **Min 1 – Max *** 

**Min 1 – Max *** 

**==> picture [310 x 78] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.060<br>camt report<br>**----- End of picture text -----**<br>


The Reporting Sequence may be provided in the camt.060 Account Reporting request to specify, for example, a range of Statements to be sent. More traditionally Account Statements are generated automatically on an end of day cycle. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [20 x 7] intentionally omitted <==**

---

<!-- ELEMENT 595 -->
## **Min 0 – Max 1** 

The Bank to Customer Statement message _**Legal Sequence Number**_ allows the _Account Servicer_ to assign a number to each statement which should increment by 1 for each statement report sent. 

**==> picture [106 x 35] intentionally omitted <==**

Where the statement is reported using multiple camt.053 messages for a given statement period the _**Legal Sequence Number**_ must be the same number in each statement message, as it can be used to correlate the statements. Where a paper statement is a legal requirement, it may have a number different from the electronic sequential number. In this case the _**Legal Sequence Number**_ element represents the sequence number of the paper statement. 

**==> picture [60 x 60] intentionally omitted <==**

Either _**Electronic Sequence Number**_ or _**Legal Sequence Number**_ must be provided to enable the identification of a statement number. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 596 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 597 -->
**Min 0 – Max 1** 

The Bank to Customer Statement message _**From to Date**_ allows the _Account Servicer_ to specify the start date time and end date time applicable to the statement. Where _**From to Date**_ is used the _**From Date Time**_ and _**To Date Time**_ become mandatory elements. **Min 1 – Max 1 Min 1 – Max 1** 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 44] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are 

**==> picture [11 x 7] intentionally omitted <==**

---

<!-- ELEMENT 598 -->
**Min 0 – Max 1** 

The Bank to Customer Statement message _**Copy Duplicate Indicator**_ is used as a choice to identify additional statement from the original sent to the Account Owner. 

**==> picture [68 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
COPY<br>**----- End of picture text -----**<br>


_**COPY**_ is used when a copy of the statement is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service such as liquidity sweeping or statement consolidation. 

_**DUPL**_ is used when a duplicate of the statement is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. **DUPL** _**CODU**_ is used when a duplicate of a statement copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in **CODU** place with the Account Servicer. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [18 x 7] intentionally omitted <==**

---

<!-- ELEMENT 599 -->
## **Min 0 – Max 1** 

The Bank to Customer Statement message _**Reporting Source**_ allows the _Account Servicer_ to define the source of the statement, typically associated with an application. 

**==> picture [59 x 56] intentionally omitted <==**

_**Reporting Source**_ utilises the external Reporting Source code list. For example **ACCT** represents a statement or report based on accounting data, whereas **DEPT** represents a cash or deposit system. Where the source of the statement is functionally required by the consumer of the statement i.e., the _Account Owner_ or _Authorised Third Party_ , the codes used should be bilaterally agreed. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [18 x 7] intentionally omitted <==**

---

<!-- ELEMENT 600 -->
**Min 1 – Max 1** 

The Bank to Customer Statement message _**Account**_ provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath _Account_ . 

**==> picture [211 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Account<br>**----- End of picture text -----**<br>


**Min 1 – Max 1** 

a unique _**Identification**_ for the account, between the _**Identification**_ Account Servicer and Account Owner. The element is further nested by choice of _**IBAN**_ or _**Other**_ to capture the account. 

**==> picture [104 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
Currency<br>**----- End of picture text -----**<br>


**Min 1 – Max 1** 

The _**Currency**_ for which the account is held. This is identified using the three characters ISO currency code. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 601 -->
**Min 0 – Max 1** 

**Min 1 – Max 1 Min 0 – Max 1** The Bank to Customer Statement message mandatory _**Account**_ also provides a number of optional nested element to identify the account for which debit and credit entries have been made. 

An element which may either use an external ISO Cash Account Type code or _**Type**_ a proprietary code. It is used to identifier a particular type of account. 

**==> picture [22 x 13] intentionally omitted <==**

The Name of the Account, as Assigned by the servicing institution. 

_**Name** Account_ _**Proxy Owner**_ 

A nested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO Proxy Account Type code or a proprietary code. 

A nest element that contains the Party that legally owns the account. 

**==> picture [16 x 15] intentionally omitted <==**

**==> picture [80 x 35] intentionally omitted <==**

A nested element which identifies the Financial Institution who manages

---

<!-- ELEMENT 602 -->
**Min 0 – Max 1** The Bank to Customer Statement message _**Related Account**_ allows the identification of a related parent account for the account statement. For example, sweeping, pooling or virtual account for which the statement is produced can identify the parent account they hierarchically relate to. 

**Min 1 – Max 1 Min 1 – Max 1** 

**==> picture [51 x 60] intentionally omitted <==**

**==> picture [73 x 57] intentionally omitted <==**

When _**Related Account**_ is utilized, like _**Account**_ , the _**Identification**_ and _**Currency**_ element become mandatory. 

Additionally the nested _**Type**_ element, _**Name**_ and nested _**Proxy**_ element are optionally available. **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1** 

**==> picture [57 x 56] intentionally omitted <==**

_Related Account_ uses a variety of common elements described in more detail within the _Account_ section. 

_Statement Related Account Identification Type_ 

**==> picture [20 x 10] intentionally omitted <==**

---

<!-- ELEMENT 603 -->
**Min 0 – Max *** 

## The Bank to Customer Statement message _**Interest**_ provides interest information that applies to the account. 

**==> picture [93 x 22] intentionally omitted <==**

**----- Start of picture text -----**<br>
Interest<br>**----- End of picture text -----**<br>


**+** 

**-** 

**==> picture [17 x 17] intentionally omitted <==**

An element which may either use an embedded ISO Interest Type code; **INDY** (Intraday) **OVRN** (Over Night) or a proprietary code. It is used to identifier a particular interest type. 

_**Type**_ 

**==> picture [22 x 14] intentionally omitted <==**

The type of interest Rate defined as a _Percentage_ and in an _Other_ form. Validity Range optionally defines an _Amount_ , _Credit Debit Indicator_ and _Currency_ . 

_**Rate**_ 

**==> picture [16 x 16] intentionally omitted <==**

The date range for which interest has been calculated. _From Date Time_ and _To Date Time_ must be representing when using this element. 

_**From To Date**_ 

**==> picture [15 x 16] intentionally omitted <==**

The optional Reason for which interest is applied. 

_**Reason**_ 

**==> picture [79 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
Tax<br>**----- End of picture text -----**<br>


Provides details on any tax applied to the Interest. Where optional

---

<!-- ELEMENT 604 -->
**Min 1 – Max *** 

## The Bank to Customer Statement message mandatory _**Balance**_ provides nested element to define the _Balance_ are account balance at a specific point in time. The following four elements nested beneath mandatory 

A nested element which may either use an external ISO Balance Type code or a proprietary code. For example, OPAV – Opening Available. Additionally, a Sub Type represented by either use an external ISO Balance Sub Type code or a proprietary code, may be used. 

**==> picture [282 x 37] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1<br>Type<br>**----- End of picture text -----**<br>


**==> picture [336 x 214] intentionally omitted <==**

**----- Start of picture text -----**<br>
Balance<br>Amount<br>Credit<br>Debit<br>Indicator<br>**----- End of picture text -----**<br>


_Balance Sub Type_ code **INTM** is essential for identifying opening and closing balances in a statement sent over more than one message. 

**==> picture [16 x 17] intentionally omitted <==**

Balance amount. 

Embedded code CRDT (Credit balance) DBIT (Debit balance) 

**==> picture [87 x 54] intentionally omitted <==**

**----- Start of picture text -----**<br>
Date<br>**----- End of picture text -----**<br>


A nested element representing the _Date_ and the _DateTime_ (with UTC

---

<!-- ELEMENT 605 -->
_Balance Type_ code are used within the nested _Balance_ element to represent the type/s of balance being reported. In comparison the legacy MT 940 utilizes different Fields and Tag options to represent a number of these Balance Types. The below extract from the externalised ISO _Balance Type_ code list compares the code with the population of the equivalent information in the Legacy MT 940 Customer Statement. 

|**Code**|**Sub**<br>**Type**|**Name**|**Definition**|**MT 940**<br>**Comparison**|
|---|---|---|---|---|
|**CLAV**||ClosingAvailable|Closing balance of amount of money that is at the disposal of the account owner on the date specified.|Field 64|
|**CLBD**||ClosingBooked|Balance of the account at the end of the pre-agreed account reporting period. It is the sum of the opening booked balance at the beginning<br>of the period and all entries booked to the account during the pre-agreed account reporting period.|<br>Field 62F|
||**INTM**|ClosingBooked (Interim)|Interim Balance of the account at the end of the pre-agreed account reporting page. It is the sum of the opening booked<br>balance at the beginningof theperiod and all entries booked to the account duringthepre-agreed account reporting page.|Field 62M|
|**FWAV**||Forw ardAvailable|Forward available balance of money that is at the disposal of the account owner on the date specified.|Field 65|
|**INFO**||Information|Balance for informational purposes.|No equivalent|
|**ITAV**||InterimAvailable|Available balance calculated in the course of the account servicer's business day, at the time specified, and subject to further changes<br>during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period<br>specified.|No equivalent|
|**ITBD**||InterimBooked|Balance calculated in the course of the account servicer's business day, at the time specified, and subject to further changes during the<br>business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified.|No equivalent|
|**OPAV**||OpeningAvailable|Opening balance of amount of money that is at the disposal of the account owner on the date specified.|No equivalent|
|**OPBD**||OpeningBooked|Book balance of the account at the beginning of the account reporting period. It always equals the closing book balance from the previous<br>report.|Field 60F|
||**INTM**|OpeningBooked (Interim)|Interim Book balance of the account at the beginning of the account reporting page. It alw ays equals the closing book<br>balance from the previous report page.|Field 60M|
|**PRCD**||PreviouslyClosedBooked|<br>Balance of the account at the previously closed account reporting period. The opening booked balance for the new period has to be equal<br>to this balance.<br>Usage: the previously booked closing balance should equal (inclusive date) the booked closing balance of the date it references and equal<br>the actual booked opening balance of the current date.|<br>Field 60F|

---

<!-- ELEMENT 606 -->
**Min 1 – Max *** 

## The Bank to Customer Statement message mandatory _**Balance**_ also provides the optional set of nested element to define a _**Credit Line**_ 

**Min 0 – Max *** 

The true/false Boolean of _**Included**_ to clearly determine whether the Credit Line Amount is included in the balance is mandatory in the set of Credit Line element. 

- Additionally, the following optional nested element may be used to identify: 

**==> picture [104 x 68] intentionally omitted <==**

- The _**Type**_ of Credit Line, which may either use an external ISO Credit Line Type code or a proprietary code. 

- A set of elements to provide _**Credit Line**_ details 

- The _**Amount**_ (Currency and Amount) of the Credit Line 

- The _**Date**_ (nested as Date, DateTime) of the Credit Line, provided to distinguish where multiple Credit Line exist. 

The final optional nested element within _**Balance**_ is the _**Availability**_ of the booked amount i.e., when it is available to be accessed. 

**==> picture [57 x 51] intentionally omitted <==**

The _Credit Line_ element is unlimited (Max *) whereby more that one _Credit Line_ may be reported, the _Date_ becomes an important element to distinguish between different Credit Lines. 

_Statement Balance Type Credit Line Amount_ 

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 607 -->
**Min 0 – Max 1** 

The Bank to Customer Statement message optional _**Transaction Summary**_ provides a set of nested element to summarize entry information. Where the statement is reported using multiple camt.053 messages for a given statement period the _Transaction Summary_ should only be included on the opening Statement message ( _Balance Type_ OPBD with no Balance _Sub Type_ ) summarizing the whole Statement Report (entire statement period) This aligns with the Common Global Implementation (CGI) where a _Transaction Summary_ , if provided, would appear before the first _Entry_ elements. 

**==> picture [70 x 79] intentionally omitted <==**

Each of the following element allow an optional total of entries either as a _**Number of Entries**_ and or as a _**Sum**_ . 

- ➢ _**Total Entries**_ 

- ➢ _**Total Credit Entries**_ 

- ➢ _**Total Debit Entries**_ 

- ➢ _**Total Entries Per Bank Transaction Code**_ 

**Min 0 – Max *** 

In addition to the _**Number of Entries**_ and _**Sum**_ , the _**Total Entries Per Bank Transaction Code**_ requires the _**Bank Transaction Code**_ element and optionally allows a variety of other optional elements. **Min 1 – Max 1** 

**==> picture [57 x 51] intentionally omitted <==**

The _Total Entries Per Bank Transaction Code_ element is unlimited (Max *) whereby more that one _Bank Transaction Code_ may be summarised. 

**==> picture [10 x 11] intentionally omitted <==**

_Statement Transaction Summary Total Entries_ 

_Total Credit Entries_ 

_Total Debit Entries_ 

**==> picture [10 x 10] intentionally omitted <==**

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 608 -->
**Min 0 – Max *** 

The Bank to Customer Statement message optional _**Entry**_ provides a significant variety of nested elements to represent the details associated with each _**Entry**_ . For active accounts which have entries posted across them, this set of nested elements is arguably the most relevant for the account owner and in many way is comparable with the MT 940 Field 61 Statement Line. 

**==> picture [47 x 82] intentionally omitted <==**

**==> picture [720 x 280] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||
|---|---|---|---|---|---|
|Min 0 – Max 1|Min 1 – Max 1|Min 1 – Max 1|Min 0 – Max 1|Min 1 – Max 1|
|Credit|
|Unlike the legacy MT Statement|Entry|Debit|Reversal|
|Amount|Status|
|Reference|Indicator|
|messages, the camt.053 has a|Indicator|
|number of dedicated elements to|
|capture a variety of entry level|
|data.|Min 0 – Max 1|Min 1 – Max 1|Min 0 – Max 1|Min 0 – Max *|Min 1 – Max 1|
|Account|Bank|
|It also has a number of|Booking|Value|
|enhancements on the legacy MT|Date|Date|ReferenceServicer|Availability|TransactionCode|
|Statement message where parties|
|in the payment and customer|
|remittance information, as|Min 0 – Max 1|Min 0 – Max 1|Min 0 – Max 1|Min 0 – Max 1|Min 0 – Max 1|
|Commission|Additional|Technical|
|examples, can provided to the|Waiver|Information|Amount|Charges|Input|
|Details|
|Account Owner.|Indicator|Indicator|Channel|
|Min 0 – Max 1|Min 0 – Max 1|Min 0 – Max *|Min 0 – Max 1|
|Additional|Statement|Entry|
|C|d|

**----- End of picture text -----**<br>

---

<!-- ELEMENT 609 -->
**Min 0 – Max 1** 

**==> picture [59 x 24] intentionally omitted <==**

**----- Start of picture text -----**<br>
Entry<br>Reference<br>**----- End of picture text -----**<br>


Unique reference for the booking entry, created by the Account Servicing Institution as a reference they assign to identify the entry posted to the account. 

**Min 1 – Max 1** 

Mandatory element representing the currency and amount of the entry. This can be compared to Field 61 subfield 4 and 5 of the legacy MT 940. 

_**Amount**_ 

**==> picture [103 x 211] intentionally omitted <==**

**==> picture [16 x 16] intentionally omitted <==**

Amount element within CBPR+ allows up to 18 digits unlike the payment messages. It allows entries reported for non CBPR+ transactions to be reported. 

**Min 1 – Max 1** _**Credit Debit Indicator**_ **Min 0 – Max 1** 

Mandatory element indicating whether the _**Amount**_ entry is a **DBIT** (Debit) or **CRDT** (Credit) to the account. This can be compared to Field 61 subfield 3 of the legacy MT 940. 

Indicates whether the entry is a result of a reversal. for example, an entry related to a pacs.004 Payment Return or reverses an error such as an incorrect value date applied to the entry. Where the _**Reversal Indicator**_ is **Yes,** the _**Credit Debit Indicator**_ should be the opposite of the original entry, for example original _**Credit Debit Indicator**_ of **CRDT** would expect a reversal entry 

_**Reversal Indicator**_

---

<!-- ELEMENT 610 -->
**==> picture [46 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1<br>**----- End of picture text -----**<br>


Mandatory element representing the status using an external ISO Entry Status code for example BOOK is _**Status**_ used to confirm the entry is booked. 

Status BOOK is the only status that can be reversed using the _**Reverse Indicator**_ 

**Min 0 – Max 1** 

**==> picture [47 x 82] intentionally omitted <==**

**==> picture [17 x 17] intentionally omitted <==**

_**Booking Date**_ 

Mandatory choice of _**Date**_ or _**Date Time**_ the entry was posted to the _**Account**_ . This can be compared to Field 61 subfield 2 of the legacy MT 940. 

**==> picture [23 x 13] intentionally omitted <==**

Noting CBPR+ usage guidelines mandate the time zone that the _**Date Time**_ represents as an offset against Universal Time Coordinated (UTC) 

**==> picture [63 x 62] intentionally omitted <==**

**Min 1 – Max 1** 

Mandatory choice of _**Date**_ or _**Date Time**_ the entry become available. This can be compared to Field 61 subfield 1 of the legacy MT 940. 

_**Value Date**_ 

**==> picture [23 x 14] intentionally omitted <==**

**Min 0 – Max 1** _**Account Servicer Reference**_ 

Additional optional Reference typically assigned by the Account Servicer’s payment engine or accounting platform. This reference would be used to query an entry. This can be compared to Field 61 subfield 8 of the legacy MT 940. 

**Min 0 – Max *** 

_**Availability**_ 

Indicates when the booked amount is available i.e., when it is available to be accessed. 

**==> picture [14 x 5] intentionally omitted <==**

---

<!-- ELEMENT 611 -->
**Min 1 – Max 1** 

_**Bank**_ The _**Bank Transaction Code Transaction**_ is designed to deliver a _**Code**_ harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the **account servicer** to correctly report a transaction, which in its turn will help **account owners** to perform their cash management and reconciliation operations. 

Domain Family Sub-Family 

The structure of the Bank Transaction Code has three levels: _**Domain**_ : Highest definition level to identify the subledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.) **Family** : Medium definition level e.g. type of payment; credit transfer, direct debit etc. _**Sub-family**_ : Lowest definition level e.g. type of cheques; draft etc. 

Bank Transaction Codes are an external code set defined in the _Bank Transaction Code combinations_ external code sets. 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

---

<!-- ELEMENT 612 -->
**==> picture [387 x 171] intentionally omitted <==**

**Min 1 – Max 1** The description of _**Bank Transaction Codes**_ are available to download from the ISO20022.org external code list page. These include the descriptions for Payments Domain Families and sub-families for both Received and Issued Credit Transfers. https://www.iso20022.org/external_code_list.page

---

<!-- ELEMENT 613 -->
**==> picture [705 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Bank Transaction Code - all permitted combinations of the BTC code sets<br>All codes in light grey are defined as the generic codes available for all Domains and Families<br>Domain Family SubFamily<br>Payments Issued Credit Transfers Cross-Border Credit Transfer PMNT ICDT XBCT New 27/4/2009<br>Payments Received Credit  Cross-Border Credit Transfer PMNT RCDT XBCT New 27/4/2009<br>Transfers<br>Status<br>Domain CodeFamily CodeSubFamily Code Status Date<br>ExternalBankTransactionDomain1CodeExternalBankTransactionFamily1CodeExternalBankTransactionSubFamily1Code<br>**----- End of picture text -----**<br>


Bank Transaction Codes are an external code set defined in the _Bank Transaction Code combinations_ external code sets. 

As an example a debit statement transaction which relates to a cross-border payment initiated from an account would be represented by: 

**Domain Family Sub-Family** PMNT (Payment) ICDT (Issued Credit Transfer) XBCT (Cross-Border Credit Transfer

---

<!-- ELEMENT 614 -->
**==> picture [55 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 0 – Max 1<br>**----- End of picture text -----**<br>


_**Commission Waiver Indicator**_ 

**==> picture [103 x 211] intentionally omitted <==**

Optional element indicating, as a Boolean, whether the entry is exempt from commission. This element is not typically associated with Correspondent Banking payments 

**Min 0 – Max 1** Optional element indicating whether the underlying transaction details are provided through a _**Additional**_ separate message. Where the _**Message Name Identification**_ represents the message used to _**Information**_ provide the additional information and _**Message Identification**_ specifies the reference of the _**Indicator**_ message that provides the additional information. 

Optional nested element which provides various elements to represent an aggregated (consolidated) original amount. Where individual transaction amounts can be represented, if required, within the _**Entry Detail**_ set of elements. 

**Min 0 – Max 1** 

_**Amount Details**_ **Min 0 – Max 1** 

This element is useful to capture original amount details where they are different to the **Entry** , **Amount** , for example the _**Instructed Amount**_ of the payment can be included, together with a potential _**Currency Exchange**_ rate, where necessary. 

Optional nested element to provide information on charges either pre-advised or taken from the entry. 

_**Charges**_ 

**==> picture [14 x 14] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 615 -->
**==> picture [56 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 0 – Max 1<br>**----- End of picture text -----**<br>


_**Technical Input Channel**_ 

**==> picture [23 x 12] intentionally omitted <==**

Optional element which may either use an external ISO Technical Input Channel code or a proprietary code used to represent the technical channel used to input the entry. 

**Min 0 – Max 1** _**Interest**_ 

Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry amount. 

**==> picture [14 x 13] intentionally omitted <==**

**Min 0 – Max 1** 

**==> picture [47 x 82] intentionally omitted <==**

**==> picture [17 x 16] intentionally omitted <==**

Optional nested element which provides details associated with a card transaction such as the card number, card brand etc. 

_**Card Transactions**_ **Min 0 – Max *** 

_**Entry**_ Additional optional nested element containing details on the entry. See dedicated section on _**Details**_ . _**Entry Details**_ 

**Min 0 – Max 1** _**Additional Statement**_ 

Additional optional element to represent further information related to the account 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 616 -->
## **Min 0 – Max *** 

The Bank to Customer Statement message optional _**Entry Details**_ provides a variety of nested elements to . represent the details associated with each _**Entry**_ 

**==> picture [47 x 82] intentionally omitted <==**

_**Batch**_ provides details on batched transactions such as the total _**Number of Transactions**_ the batched entry (sometimes referred to as a consolidated entry) represents. _**Transaction Details**_ is a significant nested element which represents information on the underlying transaction. 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

---

<!-- ELEMENT 617 -->
**Min 1 – Max 1** 

**Min 0 – Max *** 

When the Bank to Customer Statement message optional _**Entry Details**_ is utilized the nested _**Transaction Details**_ element is mandatory. 

_**Transaction Details**_ has a variety of nested elements closely associated with _**Entry**_ level elements. The _**References**_ element however is nested to include a variety of references related to the entry including for example the _**UETR**_ 

**==> picture [783 x 97] intentionally omitted <==**

**----- Start of picture text -----**<br>
$ Min 1 – Max 1 Min 1 – Max 1 Min 1 – Max 1 Credit Min 0 – Max 1 Min 0 – Max* Min 0 – Max 1 Bank Min 0 – Max 1 Min 0 – Max 1<br>Amount<br>References Amount Debit Details Availability Transaction Charges Interest<br>Indicator Code<br>**----- End of picture text -----**<br>


Additionally, _**Transaction Details**_ also has a variety of elements capturing details from the underlying transaction, which amongst other business transactions includes payment transaction data. For example, _**Remittance Information**_ and _**Related Parties**_ 

**==> picture [16 x 16] intentionally omitted <==**

Amount element within CBPR+ allows up to 18 digits unlike the payment messages. It allows entries reported for 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 618 -->
**Min 0 – Max 1** 

**Min 0 – Max 1** 

The Bank to Customer Statement message _**Related Parties**_ and _**Related Agents**_ represents a set of optional nested elements related to the underlying transaction. Where the _**Entry Details**_ (the set of elements _Related Parties/Agents_ belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message. 

**==> picture [106 x 98] intentionally omitted <==**

- These _**Related Parties**_ include : These _**Related Agents**_ include : • • _Instructing Party Instructing Agent_ 

- • • _Debtor Instructed Agent_ 

- • • _Debtor Account Debtor Agent_ 

- • • _Ultimate Debtor Creditor Agent_ 

- • • _Creditor Intermediary Agent 1_ 

- • • _Creditor Account Intermediary Agent 2_ 

- • • _Ultimate Creditor Intermediary Agent 3_ 

**==> picture [57 x 50] intentionally omitted <==**

_**Trading Party**_ is also present in the _**Related Parties**_ elements, and the following are present in the _**Related Agents**_ elements: _**Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place**_ . Although these elements are not directly associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security

---

<!-- ELEMENT 619 -->
## The Bank to Customer Statement message _**Entry Details**_ have a number of additional elements beyond _**Related Parties**_ and _**Related Agents**_ to capture information from the underlying payment. 

## These are: 

- _Local Instrument_ 

- _Purpose_ 

- _Related Remittance Information_ 

**==> picture [46 x 82] intentionally omitted <==**

- _Remittance Information_ 

- _Related Dates_ such as the _Interbank Settlement Date_ 

- • _Tax_ 

- For _Payment Return_ (pacs.004) it is also possible to capture _**Return Information**_ which includes: 

- The _Original Bank Transaction Code_ of the original Entry 

- The _Originator_ of the return from the pacs.004 

- And the _Reason_ code. 

**==> picture [60 x 47] intentionally omitted <==**

_**Remittance Information**_ as an end-to-end element should be passed unaltered from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account

---

<!-- ELEMENT 620 -->
It should also be mentioned that the Bank to Customer Statement message _**Entry Details**_ have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture _**Additional Transaction Information**_ . 

## These are: 

**==> picture [46 x 82] intentionally omitted <==**

- _Related Quantity_ 

- _Financial Instrument Identification_ 

- _Corporate Action_ 

- _Safekeeping Account_ 

- _Cash Deposit_ 

- • _Card Transactions_

---

<!-- ELEMENT 621 -->
Use case should be considered as a principal example whereby use case may be cross referenced 

## **Bank to Customer Statements** 

Use Case c.53.1.a – Bank to Customer Statement produced by the Creditor Agent 

Use Case c.53.1.b – Bank to Customer Statement produced by the Debtor Agent 

Use Case c.53.1.c – Bank to Customer Statement produced by an intermediary Agent 

## **Copy of Bank to Customer Statements** 

Use Case c.53.2 – Bank to Customer Statement sent as an additionally copy to an authorised party 

## **Resent Bank to Customer Statements** 

Use Case c.53.3 – Bank to Customer Statement resent a previously sent statement/s to the Account Owner Use Case c.53.4 – Bank to Customer Statement resent a previously sent copy statement/s to an authorised party 

## **Forwarding of Bank to Customer Statements** 

Use Case c.53.5 – Bank to Customer Statement sent to an authorised party who forward/provides on to the Account Owner (commonly referred to as an account concentrating model) 

Use Case camt.060 for requesting a Bank to Customer statement 

Use Case for copy or duplicate reports refer to camt.053 use cases

---

<!-- ELEMENT 622 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>pacs.008 pacs.008 pacs.008 camt.053<br>D<br>A B C<br>6<br>1 3<br>5<br>Debtor initiates a payment  Agent B processes the payment<br>Creditor Agent credits the<br>instruction to the Debtor Agent on Agent C account of the Creditor<br>2 4 6<br>Debtor Agent (A) initiates a  Agent C processes the payment  Creditor Agent as the Account<br>serial payment towards the  on Agent D Servicer produces and sends a<br>Creditor Agent (D) using  statement to either the Account<br>Agents B & C as intermediaries Owner, or an authorised third<br>party.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 623 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>A pacs.008 pacs.008 pacs.008<br>B C D<br>camt.053<br>6<br>1 3<br>5<br>Debtor initiates a payment  Agent B processes the payment<br>Creditor Agent credits the<br>instruction to the Debtor Agent on Agent C account of the Creditor<br>2 4 6<br>Debtor Agent (A) initiates a  Agent C processes the payment  Debtor Agent as the Account<br>serial payment towards the  on Agent D Servicer produces and sends a<br>Creditor Agent (D) using  statement to either the Account<br>Agents B & C as intermediaries Owner, or an authorised third<br>party.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 624 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>pacs.008 pacs.008 pacs.008<br>B<br>A C D<br>camt.053<br>6<br>1 3<br>5<br>Debtor initiates a payment  Agent B processes the payment<br>Creditor Agent credits the<br>instruction to the Debtor Agent on Agent C account of the Creditor<br>2 4 6<br>Debtor Agent (A) initiates a  Agent C processes the payment  Intermediary Agent as the<br>serial payment towards the  on Agent D Account Servicer produces and<br>Creditor Agent (D) using  sends a statement to either the<br>Agents B & C as intermediaries Account Owner, or an<br>authorised third party.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 625 -->
**==> picture [851 x 376] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5 6<br>pacs.008 pacs.008 pacs.008 camt.053<br>D<br>A B C<br>7<br>camt.053<br>1 3 6<br>Debtor initiates a payment  Agent B processes the payment  Creditor Agent as the Account Servicer<br>instruction to the Debtor Agent on Agent C produces and sends a statement to the<br>Account Owner.<br>2 4<br>Debtor Agent (A) initiates a  Agent C processes the payment<br>serial payment towards the  on Agent D 7<br>Creditor Agent (D) using<br>Agents B & C as intermediaries Creditor Agent as the Account Servicer<br>5 sends an additional copy of the<br>statement to an authorised third part.<br>Creditor Agent credits the<br>COPY is populated in the Copy<br>account of the Creditor<br>Duplicate Indicator element within the<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 626 -->
## **Account Owner** 

**==> picture [781 x 336] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5 6 7<br>pacs.008 pacs.008 pacs.008 D camt.053<br>A B C<br>camt.053<br>8<br>1 4<br>Debtor initiates a payment  Agent C processes the payment  7<br>instruction to the Debtor Agent on Agent D Creditor as the Account Owner<br>requests a previously sent statement<br>message/s to be resent to them.<br>5<br>2<br>Creditor Agent credits the<br>Debtor Agent (A) initiates a<br>account of the Creditor<br>serial payment towards the  8<br>Creditor Agent (D) using<br>Creditor Agent as the Account Servicer<br>Agents B & C as intermediaries 6 re-sends a duplicate statement to the<br>account owner. DUPL is populated in<br>Creditor Agent as the Account<br>the Copy Duplicate Indicator element<br>3 Servicer produces and sends a<br>statement to the Account  within the Bank to Customer Statement<br>Agent B processes the payment<br>Owner. message (camt.053)<br>on Agent C<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 627 -->
## **authorised party** 

**==> picture [785 x 339] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5<br>pacs.008 pacs.008 pacs.008<br>D<br>A B C<br>7<br>6 camt.053<br>camt.053<br>8<br>1 4<br>7<br>Debtor initiates a payment  Agent C processes the payment  Authorised third party requests a<br>instruction to the Debtor Agent on Agent D previously sent statement message/s to<br>be resent to them.<br>5<br>2<br>Creditor Agent credits the<br>Debtor Agent (A) initiates a  account of the Creditor 8<br>serial payment towards the<br>Creditor Agent as the Account Servicer<br>Creditor Agent (D) using<br>re-sends a duplicate statement to the<br>Agents B & C as intermediaries 6<br>authorised third party. CODU is<br>Creditor Agent as the Account  populated in the Copy Duplicate<br>3 Servicer produces and sends a  Indicator element within the Bank to<br>statement to an authorised  Customer Statement message<br>Agent B processes the payment<br>thi d t (camt 053)<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 628 -->
## **the Account Owner (commonly referred to as an account concentrating model)** 

**==> picture [785 x 315] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5 6<br>pacs.008 pacs.008 camt.053<br>C<br>A B<br>1 4 6<br>Debtor initiates a payment  Creditor Agent credits the  Authorised third part provides statement<br>instruction to the Debtor Agent account of the Creditor information to the Account Owner.<br>Which could be the forwarded<br>Camt.053 statement or the details via<br>2 5 an alternative channel (e.g. host to host<br>Creditor Agent as the Account  file, GUI etc.)<br>Debtor Agent (A) initiates a<br>Servicer produces and sends a<br>serial payment towards the<br>statement to an authorised<br>Creditor Agent (C) using<br>third part.<br>Agents as an intermediary<br>3<br>Agent B processes the payment<br>on Agent C<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 629 -->
# **Bank to Customer Debit Credit Notification** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 630 -->
**camt.054** 

**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Notification<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

The _Bank To Customer Debit Credit Notification_ message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message. It can be used to inform the account owner, or authorised party, of single or multiple debit and/or credit entries reported to the account 

The Bank to Customer Debit Credit Notification allows multiple Notifications per InterAct message (100,000 bytes) It is however recommended to report single notifications per transaction. This message must be bilaterally agreed between the Account Servicing Institution and the Account owner, and is establish by an

---

<!-- ELEMENT 631 -->
**==> picture [555 x 172] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pacs.008<br>pacs.002<br>camt.054 pacs.008<br>camt.054<br>camt.054<br>**----- End of picture text -----**<br>


**==> picture [55 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
C<br>**----- End of picture text -----**<br>


**==> picture [56 x 56] intentionally omitted <==**

**==> picture [180 x 24] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.054<br>**----- End of picture text -----**<br>


**==> picture [104 x 86] intentionally omitted <==**

**==> picture [101 x 95] intentionally omitted <==**

**==> picture [101 x 95] intentionally omitted <==**

**==> picture [101 x 95] intentionally omitted <==**

**==> picture [101 x 55] intentionally omitted <==**

Role of the Agent/s, Debtor and Creditor in the payment changes by description in the Bank to Customer Debit Credit Notification message to Account Servicer and Account Owner. Whereby the notification is sent by the Account Servicer to

---

<!-- ELEMENT 632 -->
The _Customer Debit Credit Notification_ are optionally provided between the account servicing institution and the account owner, or authorised (third) party. These messages: 

- are used to inform on debit and/or credit entries reported to an account. 

- and may also be complemented by: 

   - a _Status Information_ message: 

      - pacs.002 in Payment Clearing and Settlement, or pain.002 in Payment Initiation. 

   - or by a bank statement such as the camt.053 _Bank to_ 

**==> picture [494 x 346] intentionally omitted <==**

**----- Start of picture text -----**<br>
pain.001<br>pain.002<br>camt.054<br>camt.054<br>camt.053<br>camt.053<br>pacs.008/pacs.009<br>pacs.002<br>camt.054<br>camt.054<br>camt.053<br>camt.053<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 634 -->
**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 cash management reporting message has a _Message Identification_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Cash Management (camt) messages the _Message Identification_ has no exact equivalent in the legacy MT Customer Statement message. However the _Transaction Reference Number_ (Field 20) could be considered a similar comparison. 

_Group Header_ Message Identification

---

<!-- ELEMENT 635 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 636 -->
## **Min 0 – Max 1** 

The Bank to Customer Debit Credit Notification _**Message Recipient**_ nested element provides details of the party authorised by the _Account Owner_ to receive the Debit Credit Notification. 

This element **should only** be used to identify the _Message Recipient_ when different from the account owner, which is implied by the usage of COPY in the _Copy Duplicate Indicator_ within the nested Notification element. 

**==> picture [57 x 82] intentionally omitted <==**

## Where _**Message Recipient**_ is used the nested: 

- _**Name**_ **Min 0 – Max 1** 

- • _**Postal Address**_ **Min 0 – Max 1** 

- _**Postal Address**_ 

- _**Identification**_ 

**Min 0 – Max 1** 

- **Min 0 – Max 1** 

- _**Contact Details**_ 

- May be used to capture information related to this party. 

**==> picture [11 x 11] intentionally omitted <==**

_Group Header_ Message _Recipient Name_

---

<!-- ELEMENT 637 -->
**Min 0 – Max 1** The Bank to Customer Debit Credit Notification _**Original Business Query**_ element identifies a query to generate a report, for example a camt.060 Account Reporting Request. 

**==> picture [103 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
?<br>**----- End of picture text -----**<br>


**Min 1 – Max 1** 

Where _**Original Business Query**_ is used the original _**Message identification**_ (i.e. the message identification of the camt.060 message) is required. Original _**Message Name identification**_ and Original _**Creation Date Time**_ may also be provided. **Min 0 – Max 1 Min 0 – Max 1** 

**==> picture [10 x 11] intentionally omitted <==**

_Group Header_ Original Business Query

---

<!-- ELEMENT 638 -->
## **Min 0 – Max 1** 

The Bank to Customer Debit Credit Notification _**Additional Information**_ element represents further details related to the account statement. 

**==> picture [82 x 85] intentionally omitted <==**

The camt.054 may be used to indicate a particular type of notification, recognizing all transactions within the notification belong to the type indicated below: **/LBOX/** Lock Box 

**/BULK/** Bulk reporting (batch transaction with underlying transaction) **/RTRN/** Return report 

- **/CRED/** Notification with Credit entries ONLY 

**==> picture [60 x 60] intentionally omitted <==**

Additional Information is a textual element restricted in CBPR+ to 500 characters. 

_Group Header_ Additional Information

---

<!-- ELEMENT 640 -->
**Min 0 – Max *** The Bank to Customer Debit Credit Notification _**Notification**_ nested element captures debit and credit entry information for an account. 

**==> picture [135 x 101] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>**----- End of picture text -----**<br>


The _Notification_ element has a couple of options to notify on multiple Debits and or Credits. This can be achieved at either the _**Notification**_ element itself which could principally report on more than one account held by the account owner with the Account Servicer or can be achieved at an _**Entry**_ level. Notification of multiple Debits and or Credits is perhaps more associated with a timed or batch creation of the camt.054 Bank to Customer Debit Credit Notification. Whereas the more common example of a real-time notification produced at the point of an account posting would typically notify on a single . _Entry_ 

**==> picture [11 x 10] intentionally omitted <==**

_Notification_

---

<!-- ELEMENT 641 -->
## **Min 1 – Max 1** 

The Bank to Customer Debit Credit Notification message _**Identification**_ provides a mandatory element to identify the notification 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the account servicer to unambiguously identify the account statement. Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 642 -->
## **Min 0 – Max 1** The Bank to Customer Debit Credit Notification message _**Notification Pagination**_ element provides the page number of the notification. 

**Min 1 – Max 1 Min 1 – Max 1** 

**==> picture [124 x 76] intentionally omitted <==**

Where _**Notification Pagination**_ is used the _**Page Number**_ and _**Last Page indicator**_ elements are both mandatory. 

**For example,** a _Page Number_ of 2 represents the current account statement, being the second page of the and implying a previous account statement page had been sent. The _Last Page indicator_ further implies whether more pages are expected 

**==> picture [60 x 60] intentionally omitted <==**

Either _Message Pagination_ (Group Header) or _Notification Pagination_ (Notification) may used but not both 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

---

<!-- ELEMENT 643 -->
**Min 0 – Max 1** 

The Bank to Customer Debit Credit Notification message _**Electronic Sequence Number**_ allows the _Account Servicer_ to assign a number to each notification which should increment by 1 for each electronic notification report sent. 

> **1 3 4 2 5** 

As a good practice this element allows easy recognition of the notification order, if not recognisable by other data within the notification, such as the _**Notification**_ > _**Identification**_ element. 

Should this sequence number be reset by the _Account Servicer_ , this should not occur more frequently than once a year. Likewise, this 18 digit counter could be incremented to its maximum value before it’s reset. 

**==> picture [46 x 49] intentionally omitted <==**

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the _Account Servicer_ and the _Account Owner_ 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 644 -->
**Min 0 – Max 1** 

**==> picture [17 x 17] intentionally omitted <==**

The Bank to Customer Debit Credit Notification the choice of message _**Reporting Sequence**_ specifies identification This can be used as an alterative to the _**Statement**_ or _**Electronic**_ sequences. _**Pagination Sequence Number**_ as a way to identify the statement order, which is not confined to numeric values. 

Where used the _**Reporting Sequence**_ mandate a choice of nested element: 

**A** 

**B** 

**D C** 

- **Min 1 –** 

- _**From Sequence**_ identifies the start of a sequence range. 

- • **Min 1 – Max 1** _**To Sequence**_ identifies the end of a sequence range. 

**Min 1 – Max 1** 

- _**From To Sequence**_ identifies the start and end of a sequence range. 

- • **Min 1 – Max *** _**Equal Sequence**_ identifies a sequence. 

- • _**Not Equal Sequence**_ identifies a sequence to be excluded. **Min 1 – Max *** 

**Min 1 – Max *** 

**==> picture [60 x 60] intentionally omitted <==**

Although the Reporting Sequence may be provided in a camt.060 Account Reporting Request, the use of this message to request a Bank to Customer Debit Credit Notification is less compelling, whereby such notifications are typically triggered as the result of an account posting, rather than being requested. 

**==> picture [11 x 6] intentionally omitted <==**

**==> picture [19 x 7] intentionally omitted <==**

---

<!-- ELEMENT 645 -->
**Min 0 – Max 1** 

The Bank to Customer Debit Credit Notification message _**Legal Sequence Number**_ allows the _Account Servicer_ to assign a number to each notification which should increment by 1 for each notification report sent. 

**==> picture [105 x 35] intentionally omitted <==**

In the case of a real-time notification the _**Legal Sequence Number**_ element has little value, unlike its use in a statement message. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 646 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 647 -->
**Min 0 – Max 1** 

The Bank to Customer Debit Credit Notification message _**From to Date**_ allows the _Account Servicer_ to specify the start date time and end date time applicable to the notification. Where _**From to Date**_ is used the _**From Date Time**_ and _**To Date Time**_ become mandatory elements. **Min 1 – Max 1 Min 1 – Max 1** 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 44] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are 

**==> picture [11 x 7] intentionally omitted <==**

---

<!-- ELEMENT 648 -->
**Min 0 – Max 1** 

## The Bank to Customer Debit Credit Notification message _**Copy Duplicate Indicator**_ is used as a choice to identify additional notification from the original sent to the Account Owner. 

**==> picture [68 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
COPY<br>**----- End of picture text -----**<br>


_**COPY**_ is used when a copy of the notification is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service such as liquidity sweeping or statement consolidation. 

_**DUPL**_ is used when a duplicate of the notification is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. **DUPL** _**CODU**_ is used when a duplicate of a notification copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in **CODU** place with the Account Servicer. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [18 x 7] intentionally omitted <==**

---

<!-- ELEMENT 649 -->
## **Min 0 – Max 1** 

The Bank to Customer Debit Credit Notification message _**Reporting Source**_ allows the _Account Servicer_ to define the source of the notification, typically associated with an application. 

**==> picture [59 x 56] intentionally omitted <==**

_**Reporting Source**_ utilizes the external Reporting Source code list. For example, **ACCT** represents a notification based on accounting data, whereas **DEPT** represents a cash or deposit system. Where the source of the notification is functionally required by the consumer of the notification i.e., the _Account Owner_ or _authorised Third Party_ , the codes used should be bilaterally agreed. 

**==> picture [11 x 6] intentionally omitted <==**

**==> picture [18 x 7] intentionally omitted <==**

---

<!-- ELEMENT 650 -->
**Min 1 – Max 1** 

The Bank to Customer Debit Credit Notification message _**Account**_ provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath _Account_ . 

**Min 1 – Max 1** 

a unique _**Identification**_ for the account, between the _**Identification**_ Account Servicer and Account Owner. The element is further nested by choice of _**IBAN**_ or _**Other**_ to capture the account. 

_Account_ further nested by choice of _**IBAN**_ or _**Other**_ to capture the account. **Min 1 – Max 1** The _**Currency**_ for which the account is held. This is _**Currency**_ identified using the three characters ISO currency code. 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [12 x 6] intentionally omitted <==**

---

<!-- ELEMENT 651 -->
**Min 1 – Max 1** The Bank to Customer Debit Credit Notification message mandatory _**Account**_ also provides a number of optional nested element to identify the account for which debit and credit entries have been made. **Min 0 – Max 1** 

**==> picture [34 x 15] intentionally omitted <==**

**----- Start of picture text -----**<br>
Type<br>**----- End of picture text -----**<br>


An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. 

**==> picture [22 x 13] intentionally omitted <==**

The Name of the Account, as Assigned by the servicing institution. 

_**Name** Account_ _**Proxy Owner**_ 

A nested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO Proxy Account Type code or a proprietary code. 

A nest element that contains the Party that legally owns the account. 

**==> picture [15 x 14] intentionally omitted <==**

---

<!-- ELEMENT 652 -->
**Min 0 – Max 1** 

The Bank to Customer Debit Credit Notification message _**Related Account**_ allows the identification of a related parent account for the account notification. For example sweeping, pooling or virtual account for which the notification is produced can identify the parent account they hierarchically relate to. 

**Min 1 – Max 1 Min 1 – Max 1** 

**==> picture [51 x 60] intentionally omitted <==**

When _**Related Account**_ is utilized, like _**Account**_ , the _**Identification**_ and _**Currency**_ element become mandatory. 

Additionally, the nested _**Type**_ element, _**Name**_ and nested _**Proxy**_ element are optionally available. **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1** 

**==> picture [73 x 57] intentionally omitted <==**

**==> picture [57 x 56] intentionally omitted <==**

_Related Account_ uses a variety of common elements described in more detail within the _Account_ section. 

**==> picture [11 x 11] intentionally omitted <==**

_Notification Related Account_ 

_Identification Type_ 

**==> picture [20 x 10] intentionally omitted <==**

---

<!-- ELEMENT 653 -->
**Min 0 – Max *** 

The Bank to Customer Debit Credit Notification _**Interest**_ message provides interest information that applies to the account. Inclusion of such interest information is perhaps more common to the camt.053 Statement than a Debit Credit Notification. 

An element which may either use an embedded ISO Interest Type code; **INDY** _**Type**_ (Intraday) **OVRN** (Over Night) or a proprietary code. It is used to identifier a particular interest type. 

The type of interest Rate defined as a _Percentage_ and in an _Other_ form. Validity Range optionally defines an _Amount_ , _Credit Debit Indicator_ and _Currency_ . 

**==> picture [93 x 22] intentionally omitted <==**

**----- Start of picture text -----**<br>
Interest<br>**----- End of picture text -----**<br>


_**Rate**_ 

**==> picture [17 x 17] intentionally omitted <==**

**==> picture [16 x 14] intentionally omitted <==**

The date range for which interest has been calculated. _From Date Time_ and _To Date Time_ must be representing when using this element. 

_**From To Date**_ 

**+** 

**-** 

**==> picture [15 x 14] intentionally omitted <==**

The optional Reason for which interest is applied. 

_**Reason**_ 

**==> picture [79 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
Tax<br>**----- End of picture text -----**<br>


Provides details on any tax applied to the Interest. Where optional

---

<!-- ELEMENT 654 -->
**Min 0 – Max 1** 

The Bank to Customer Debit Credit Notification message optional _**Transaction Summary**_ provides a set of nested element to summarize entry information. More commonly the Bank to Customer Debit Credit Notification is reporting a single Debit or Credit transaction, where understandably the use of Transaction Summary provides little value. 

Each of the following element allow an optional total of entries either as a _**Number of Entries**_ and or as a _**Sum**_ . 

**==> picture [70 x 79] intentionally omitted <==**

➢ _**Total Entries**_ 

- ➢ _**Total Credit Entries**_ 

- ➢ _**Total Debit Entries**_ 

- ➢ _**Total Entries Per Bank Transaction Code**_ 

**Min 0 – Max *** 

In addition to the _**Number of Entries**_ and _**Sum**_ , the _**Total Entries Per Bank Transaction Code**_ requires the _**Bank Transaction Code**_ element and optionally allows a variety of other optional elements. **Min 1 – Max 1** 

**==> picture [57 x 51] intentionally omitted <==**

The _Total Entries Per Bank Transaction Code_ element is unlimited (Max *) whereby more that one _Bank Transaction Code_ may be summarised. 

**==> picture [10 x 11] intentionally omitted <==**

_Notification Transaction Summary_ 

**==> picture [10 x 9] intentionally omitted <==**

_Total Entries_ 

_Total Credit Entries_ 

_Total Debit Entries_ 

**==> picture [10 x 10] intentionally omitted <==**

**==> picture [10 x 10] intentionally omitted <==**

---

<!-- ELEMENT 655 -->
**==> picture [61 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 0 – Max *<br>**----- End of picture text -----**<br>


The Bank to Customer Debit Credit Notification message optional _**Entry**_ provides a significant variety of . nested elements to represent the details associated with each Debit or Credit _**Entry**_ 

**==> picture [47 x 82] intentionally omitted <==**

Unlike the legacy MT 900 MT 910 confirmation messages, the camt.054 has a number of dedicated elements to capture a variety of entry level data. It also has an number of enhancements on the legacy MT confirmation message where parties in the payment and customer remittance information, as examples, can provided to the _Account Owner._ 

**==> picture [505 x 281] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 0 – Max 1 Min 1 – Max 1 Min 1 – Max 1 Min 0 – Max 1 Min 1 – Max 1<br>Credit<br>Entry Debit Reversal<br>Amount Status<br>Reference Indicator<br>Indicator<br>Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max * Min 1 – Max 1<br>Account Bank<br>Booking Value<br>Date Date Servicer Availability Transaction<br>Reference Code<br>Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1<br>Commission Additional Technical<br>Amount<br>Waiver Information Charges Input<br>Details<br>Indicator Indicator Channel<br>Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max * Min 0 – Max 1<br>Additional Notification Entry<br>C d<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 656 -->
**Min 0 – Max 1** 

**==> picture [59 x 24] intentionally omitted <==**

**----- Start of picture text -----**<br>
Entry<br>Reference<br>**----- End of picture text -----**<br>


Unique reference for the booking entry, created by the Account Servicing Institution as a reference they assign to identify the entry posted to the account. 

**Min 1 – Max 1** 

Mandatory element representing the currency and amount of the entry. This can be compared to Field 32A of the legacy MT 900 and MT 910. 

_**Amount**_ 

**==> picture [103 x 211] intentionally omitted <==**

**Min 1 – Max 1** _**Credit Debit Indicator**_ **Min 0 – Max 1** 

Mandatory element indicating whether the _**Amount**_ entry is a **DBIT** (Debit) or **CRDT** (Credit) to the account. 

Indicates whether the entry is a result of a reversal. for example, an entry related to a pacs.004 Payment Return or reverses an error such as an incorrect value date applied to the entry. Where the _**Reversal Indicator**_ is **Yes,** the _**Credit Debit Indicator**_ should be the opposite of the original entry, for example original _**Credit Debit Indicator**_ of **CRDT** would expect a reversal entry _**Credit Debit Indicator**_ of **DBIT** 

_**Reversal Indicator**_

---

<!-- ELEMENT 657 -->
**==> picture [55 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1<br>**----- End of picture text -----**<br>


_**Status**_ 

**==> picture [22 x 13] intentionally omitted <==**

Mandatory element representing the status using an external ISO Entry Status code for example BOOK is used to confirm the entry is booked. 

Status BOOK is the only status that can be reversed using the _**Reverse Indicator**_ 

**Min 0 – Max 1** 

**==> picture [47 x 82] intentionally omitted <==**

**==> picture [17 x 17] intentionally omitted <==**

_**Booking Date**_ 

Mandatory choice of _**Date**_ or _**Date Time**_ the entry was posted to the _**Account**_ . 

**==> picture [23 x 13] intentionally omitted <==**

Noting CBPR+ usage guidelines mandate the time zone that the _**Date Time**_ represents as an offset against Universal Time Coordinated (UTC) 

**==> picture [63 x 62] intentionally omitted <==**

**Min 0 – Max 1** 

Mandatory choice of _**Date**_ or _**Date Time**_ the entry become available. This can be compared to Field 32A of the legacy MT 900 and MT 910. 

_**Value Date**_ 

**==> picture [23 x 14] intentionally omitted <==**

**Min 0 – Max 1** 

_**Account Servicer Reference**_ 

Additional optional Reference typically assigned by the Account Servicer’s payment engine or accounting platform. This reference would be used to query an entry. 

**Min 0 – Max *** 

_**Availability**_ 

Indicates when the booked amount is available i.e., when it is available to be accessed. 

**==> picture [14 x 5] intentionally omitted <==**

---

<!-- ELEMENT 658 -->
**Min 1 – Max 1** 

_**Bank**_ The _**Bank Transaction Code Transaction**_ is designed to deliver a _**Code**_ harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the **account servicer** to correctly report a transaction, which in its turn will help **account owners** to perform their cash management and reconciliation operations. 

Domain Family Sub-Family 

The structure of the Bank Transaction Code has three levels: _**Domain**_ : Highest definition level to identify the subledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.) **Family** : Medium definition level e.g. type of payment; credit transfer, direct debit etc. _**Sub-family**_ : Lowest definition level e.g. type of cheques; draft etc. 

Bank Transaction Codes are an external code set defined in the _Bank Transaction Code combinations_ external code sets. 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 659 -->
## **descriptions** 

**==> picture [387 x 171] intentionally omitted <==**

**Min 1 – Max 1** The description of _**Bank Transaction Codes**_ are available to download from the ISO20022.org external code list page. These include the descriptions for Payments Domain Families and sub-families for both Received and Issued Credit Transfers. https://www.iso20022.org/external_code_list.page

---

<!-- ELEMENT 660 -->
## **combinations** 

**==> picture [749 x 319] intentionally omitted <==**

**----- Start of picture text -----**<br>
Bank Transaction Code - all permitted combinations of the BTC code sets<br>All codes in light grey are defined as the generic codes available for all Domains and Families<br>Domain Family SubFamily<br>Payments Issued Credit Transfers Cross-Border Credit Transfer PMNT ICDT XBCT New 27/4/2009<br>Payments Received Credit  Cross-Border Credit Transfer PMNT RCDT XBCT New 27/4/2009<br>Transfers<br>Bank Transaction Codes are an external code set defined in the  Bank Transaction Code combinations  external<br>code sets.<br>As an example a debit notification which relates to a cross-border payment initiated from an account would be<br>represented by:<br>Domain Family Sub-Family<br>PMNT (Payment) ICDT (Issued Credit Transfer) XBCT (Cross-Border Credit Transfer<br>Status<br>Domain CodeFamily CodeSubFamily Code Status Date<br>ExternalBankTransactionDomain1CodeExternalBankTransactionFamily1CodeExternalBankTransactionSubFamily1Code<br>**----- End of picture text -----**<br>


Bank Transaction Codes are an external code set defined in the _Bank Transaction Code combinations_ external code sets. 

As an example a debit notification which relates to a cross-border payment initiated from an account would be represented by:

---

<!-- ELEMENT 661 -->
**Min 0 – Max 1** 

_**Commission Waiver Indicator**_ 

**==> picture [103 x 211] intentionally omitted <==**

Optional element indicating, as a Boolean, whether the entry is exempt from commission. This element is not typically associated with Correspondent Banking payments 

**Min 0 – Max 1** Optional element indicating whether the underlying transaction details are provided through a _**Additional**_ separate message. Where the _**Message Name Identification**_ represents the message used to _**Information**_ provide the additional information and _**Message Identification**_ specifies the reference of the _**Indicator**_ message that provides the additional information. 

Optional nested element which provides various elements to represent an aggregated (consolidated) original amount. Where individual transaction amounts can be represented, if required, within the _**Entry Detail**_ set of elements. 

**Min 0 – Max 1** 

_**Amount Details**_ 

This element is useful to capture original amount details where they are different to the **Entry** , **Amount** , for example the _**Instructed Amount**_ of the payment can be included, together with a potential _**Currency Exchange**_ rate, where necessary. 

**==> picture [14 x 14] intentionally omitted <==**

**Min 0 – Max 1** 

Optional nested element to provide information on charges either pre-advised or taken from the entry. 

_**Charges**_ 

**==> picture [14 x 14] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 662 -->
**==> picture [56 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 0 – Max 1<br>**----- End of picture text -----**<br>


_**Technical Input Channel**_ 

**==> picture [23 x 12] intentionally omitted <==**

Optional element which may either use an external ISO Technical Input Channel code or a proprietary code used to represent the technical channel used to input the entry. 

**Min 0 – Max 1** _**Interest**_ 

Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry amount. 

**==> picture [14 x 13] intentionally omitted <==**

**Min 0 – Max 1** 

**==> picture [47 x 82] intentionally omitted <==**

**==> picture [17 x 16] intentionally omitted <==**

Optional nested element which provides details associated with a card transaction such as the card number, card brand etc. 

_**Card Transactions**_ **Min 0 – Max *** 

_**Entry**_ Additional optional nested element containing details on the entry. See dedicated section on _**Details**_ . _**Entry Details**_ 

**Min 0 – Max 1** _**Additional Statement**_ 

Additional optional element to represent further information related to the account 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 663 -->
## **Min 0 – Max *** 

The Bank to Customer Debit Credit Notification message optional _**Entry Details**_ provides a variety of nested . elements to represent the details associated with each _**Entry**_ 

**==> picture [47 x 82] intentionally omitted <==**

_**Batch**_ provides details on batched transactions such as the total _**Number of Transactions**_ the batched entry (sometimes referred to as a consolidated entry) represents. _**Transaction Details**_ is a significant nested element which represents information on the underlying transaction. 

**==> picture [11 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

---

<!-- ELEMENT 664 -->
## **Min 0 – Max *** 

When the Bank to Customer Debit Credit Notification message optional _**Entry Details**_ is utilized the nested _**Transaction Details**_ element is mandatory. 

**Min 1 – Max 1** 

_**Transaction Details**_ has a variety of nested elements closely associated with _**Entry**_ level elements. The _**References**_ element however is nested to include a variety of references related to the entry including for example the _**UETR**_ 

**==> picture [784 x 168] intentionally omitted <==**

**----- Start of picture text -----**<br>
$ Min 1 – Max 1 Min 1 – Max 1 Min 1 – Max 1 Credit Min 0 – Max 1 Min 0 – Max* Min 0 – Max 1 Bank Min 0 – Max 1 Min 0 – Max 1<br>Amount<br>Reference Amount Debit Details Availability Transaction Charges Interest<br>Indicator Code<br>Additionally Transaction Details  also has a variety of elements capturing details from the underlying<br>transaction, which amongst other business transactions includes payment transaction data. For example<br>Remittance Information  and  Related Parties<br>**----- End of picture text -----**<br>


**==> picture [11 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 665 -->
## **Agents** 

## **Min 0 – Max 1** 

## **Min 0 – Max 1** 

The Bank to Customer Debit Credit Notification message _**Related Parties**_ and _**Relegated Agents**_ represents a set of optional nested elements related to the underlying transaction. Where the _**Entry Details**_ (the set of elements _Related Parties/Agents_ belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message. 

**==> picture [106 x 98] intentionally omitted <==**

- These _**Related Parties**_ include : These _**Related Agents**_ include : • • _Instructing Party Instructing Agent_ 

- • • _Debtor Instructed Agent_ 

- • • _Debtor Account Debtor Agent_ 

- • • _Ultimate Debtor Creditor Agent_ 

- • • _Creditor Intermediary Agent 1_ 

- • • _Creditor Account Intermediary Agent 2_ 

- • • _Ultimate Creditor Intermediary Agent 3_ 

**==> picture [57 x 50] intentionally omitted <==**

_**Trading Party**_ is also present in the _**Related Parties**_ elements, and the following are present in the _**Related Agents**_ elements: _**Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place**_ . Although these elements are not directly associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security

---

<!-- ELEMENT 666 -->
## The Bank to Customer Debit Credit Notification message _**Entry Details**_ have a number of additional elements beyond _**Related Parties**_ and _**Related Agents**_ to capture information from the underlying payment. 

## These are: 

- _Local Instrument_ 

- _Purpose_ 

- _Related Remittance Information_ 

**==> picture [46 x 82] intentionally omitted <==**

- _Remittance Information_ 

- _Related Dates_ such as the _Interbank Settlement Date_ 

- • _Tax_ 

- For _Payment Return_ (pacs.004) it is also possible to capture _**Return Information**_ which includes: 

- The _Original Bank Transaction Code_ of the original Entry 

- The _Originator_ of the return from the pacs.004 

- And the _Reason_ code. 

**==> picture [60 x 47] intentionally omitted <==**

_**Remittance Information**_ as an end-to-end element should be passed unaltered from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account

---

<!-- ELEMENT 667 -->
It should also be mentioned that the Bank to Customer Credit Debit Notification message _**Entry Details**_ have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture _**Additional Transaction Information**_ . 

## These are: 

**==> picture [46 x 82] intentionally omitted <==**

- _Related Quantity_ 

- _Financial Instrument Identification_ 

- _Corporate Action_ 

- _Safekeeping Account_ 

- _Cash Deposit_ 

- • _Card Transactions_

---

<!-- ELEMENT 668 -->
Use case should be considered as a principal example whereby use case may be cross referenced 

## **Debit/Credit Notification related to a Serial Customer Payments** 

Use Case c.54.1.1 – Customer Debit/Credit Notification (camt.054) of a Customer Credit Transfer (pacs.008) **Debit/Credit Notification related to a Serial Financial Institution Payments** Use Case c.54.2.1 – Customer Debit/Credit Notification (camt.054) of a FI to FI Credit Transfer (pacs.009) **Debit/Credit Notification related to a Cover Method Payments** Use Case c.54.3.1 – Customer Debit/Credit Notification (camt.054) of a payment using the cover method

---

<!-- ELEMENT 669 -->
## **(pacs.008)** 

**==> picture [764 x 330] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2a 3 4 5<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>camt.054<br>camt.054<br>2b<br>1 2b 4<br>Debtor initiates a payment  Agent A provides a debit  Agent C processes the payment<br>instruction to the Debtor Agent notification to the debtor using the  on Agent D<br>camt.054 to confirm their account<br>has been debited for the payment  5<br>initiation request. This notification<br>2 Agent D credits the account of<br>may compliment additional status<br>Debtor Agent (A) initiates a  information or statement report  the Creditor, providing a credit<br>serial payment towards the  messages notification using the camt.054<br>Creditor Agent (D) using<br>Agents B & C as intermediaries<br>3<br>Agent B processes the payment<br>on Agent C<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 670 -->
**(pacs.009)** 

**==> picture [522 x 332] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>1 2a<br>camt.054<br>pacs.009<br>A B C camt.053 D<br>camt.054<br>2b<br>1 2b 3<br>Agent A as the Debtor initiates  Debtor Agent (Agent B)<br>a payment instruction to the  provides a debit notification to  account of Agent D and<br>Debtor Agent (Agent B) the debtor using the camt.054<br>to confirm their account has<br>2 been debited for the payment<br>Debtor Agent (B) debits the  initiation request. This<br>account of Agent A and  notification may be<br>initiates a serial payment  complimented by an additional<br>towards the Creditor (Agent D)  status information message.<br>using Agents C as an  But typically will be compliment<br>intermediary. by an end of business day<br>statement report messages<br>**----- End of picture text -----**<br>


**==> picture [153 x 79] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>Creditor Agent (C) credits the<br>account of Agent D and<br>provides a credit notification<br>(camt.054) in addition to an<br>account statement (camt.053)<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 671 -->
## **method** 

**==> picture [829 x 363] intentionally omitted <==**

**----- Start of picture text -----**<br>
5<br>1<br>2a<br>pacs.008<br>camt.054<br>A pacs.002 D<br>2b<br>1<br>Debtor initiates a payment<br>instruction to the Debtor Agent<br>4<br>3a<br>2a<br>Debtor Agent (A) initiates a  3b pacs.009.cov 6<br>payment using the cover method  B C<br>to the Creditor Agent (D)<br>3b 4 6<br>2b<br>Agent C receives the payment and<br>Agent B provides a debit notification  Agent C produces an end of day<br>In parallel the Debtor Agent (A)  credits the account of Agent D and<br>to Agent A using the camt.054 to  account statement report. An optional<br>initiates a coving payment to  confirm their account has been  provides a credit notification (camt.054)  real time notifications e.g. advice of<br>credit the account of Agent (D)<br>debited for the payment initiation  credit may have also been created at<br>with their correspondent (Agent<br>request. This notification may be   5 the time of the credit posting<br>C)<br>complimented by an additional status  Upon receipt of the credit notification<br>information message or statement  (camt.054) confirming settlement of the<br>3a report messages covering payment, Agent D may chose  Intraday Credit Notification is<br>required when using the cover<br>to process the pacs.008 (if not already<br>Agent B processes the payment  method unless an alternative<br>done so) and apply a credit to the<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 672 -->
# **Notification to Receive** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 673 -->
**camt.057** 

**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Notification<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

The _NotificationToReceive_ message is sent by an account owner or by a party acting on the account owner's behalf to one of the account owner's account servicing institutions. It is an advance notice that the account servicing institution will receive funds to be credited to the account of the account owner. The _NotificationToReceive_ message is used to advise the account servicing institution of funds that the account owner expects to have credited to its account. 

The Notification to Receive message is the ISO 20022 equivalent of the legacy MT210 Notice to Receive. It can be cancelled using the camt.058 where in the meantime the legacy MT 292 can be used to

---

<!-- ELEMENT 674 -->
**==> picture [360 x 137] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>A<br>camt.057<br>pacs<br>camt.058<br>**----- End of picture text -----**<br>


Role of the Creditor Agent and Creditor in the payment changes description in the Notification to Receive message (camt.057). The Account Owner is typically the Creditor and the Account Servicer is typically the Creditor Agent. This will

---

<!-- ELEMENT 675 -->
## **payment message (pacs.008/pacs.009) and the Notification to Receive (camt.057)** 

**==> picture [799 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>camt.057<br>pacs<br>pacs<br>pacs.002<br>pacs<br>pacs.002<br>camt.053<br>pacs.002<br>Party pacs camt.057<br>D<br>Debtor Debtor<br>The Parties defined within the Notification to Receive (camt.0057)<br>Debtor Agent Debtor Agent<br>provide advance information to the Account Servicer of information<br>included in the payment message. Noting a Debtor must always be<br>Creditor Agent Account Servicer present in the camt.057 (it is mandatory in the pacs payment<br>**----- End of picture text -----**<br>


The Parties defined within the Notification to Receive (camt.0057) provide advance information to the Account Servicer of information included in the payment message. Noting a Debtor must always be present in the camt.057 (it is mandatory in the pacs payment message) but Debtor Agent may not be provided (Debtor Agent is 

**==> picture [36 x 23] intentionally omitted <==**

**==> picture [32 x 21] intentionally omitted <==**

---

<!-- ELEMENT 677 -->
**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 cash management reporting message has a _Message Identification_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

**Min 1 – Max 1** The _**Message Identification**_ in the Cash Management (camt) messages is equivalent to field 20 Transaction Reference Number of the MT 210 in the legacy MT Notice to Receive. 

_Group Header_ Message Identification

---

<!-- ELEMENT 678 -->
## **Min 1 – Max 1** 

## The camt.057 message _**Creation Date Time**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 679 -->
## **Min 0 – Max 1** 

The Notification to Receive _**Message Sender**_ nested element provides details of the party that is sending the message, where the _**Message Sender**_ is different from the account owner. 

## Where _**Message Sender, Party**_ is used the nested: 

- _**Name**_ **Min 0 – Max 1** 

**==> picture [57 x 82] intentionally omitted <==**

- _**Postal Address**_ 

**Min 0 – Max 1** 

- _**Identification**_ 

**Min 0 – Max 1** 

- **Min 0 – Max 1** 

- _**Contact Details**_ 

- May be used to capture information related to this party. 

## Where _**Message Sender, Agent**_ is used the nested _**Financial Institution**_ : 

- _**BICFI**_ 

**Min 1 – Max 1** 

- _**Clearing System Member Identification**_ 

- • _**LEI**_ 

**Min 0 – Max 1 Min 0 – Max 1** 

_Group Header_ Message _Sender Name_ 

May be used to capture information related to this Agent. 

**==> picture [11 x 11] intentionally omitted <==**

---

<!-- ELEMENT 681 -->
## **Min 1 – Max 1** 

The Notification to Receive _**Notification**_ element contains nested elements to provide further details on the account notification such as the related parties, the expected amount to be received and value date of the expected receipt. 

**==> picture [135 x 101] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>**----- End of picture text -----**<br>


The Notification nested element **Item** can contain multiple Credits. Where there is only one expected credit then only the Item element will contain the Item **Identification** and the **Amount** . 

**==> picture [56 x 57] intentionally omitted <==**

Today the status of a camt.057 has no documented ISO 20022 reporting process, to the Account Owner by the Account Servicer. 

Generally, if the Account Servicer does not require notification the message will be ignored. 

_Notification_ 

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 682 -->
## **Min 1 – Max 1** 

The Notification to Receive message _**Notification Identification**_ provides a mandatory element to identify the account notification. 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the account owner to unambiguously identify the account notification. There is no equivalent in the MT210. It is recommended that the Message Identification is repeated for the Notice to Receive Identification. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 683 -->
## **Min 0 – Max 1** 

The Notification to Receive message _**Account**_ element provides nested elements to identify the account for which the credit entry has been made. The following two mandatory elements are nested beneath _**Account**_ . **Min 1 – Max 1** a unique _**Identification**_ for the account, between the Account Servicer and _**Identification**_ Account Owner. The element is further nested by choice of _**IBAN**_ or _**Other**_ to capture the account. 

**==> picture [389 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
An<br>Type<br>Account<br>Currency<br>Name<br>P T<br>**----- End of picture text -----**<br>


An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. 

The _**Currency**_ for which the account is held. This is identified . using the three characters ISO currency code 

The Name of the Account, as Assigned by the servicing institution. 

A nested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 684 -->
## **Min 0 – Max 1** 

## **Min 0 – Max 1** 

The _**Account Owner**_ is the Creditor, and the _**Account Servicer**_ is the Creditor Agent. They are static roles in the camt.057 Notification to Receive. 

The _**Account Owner**_ must be identified either the name and address or as a by Party postal an Agent using Financial Institution identification. The _**Account Servicer**_ must be identified as an Agent by using the Financial Institution identification. 

**==> picture [82 x 136] intentionally omitted <==**

**==> picture [56 x 57] intentionally omitted <==**

The Account Owner and the Account Servicer are the Creditor and Creditor Agent respectively in a pacs.008 FI to FI Customer. Where utilised, it is **recommended** to use the element at the Item level. 

**==> picture [11 x 11] intentionally omitted <==**

_Notification_

---

<!-- ELEMENT 685 -->
**Min 0 – Max 1** 

The Notification to Receive _**Related Account**_ element allows the identification of a related message parent account for the account notification. For example sweeping, pooling or virtual account for which the notification is produced can identify the parent account they hierarchically relate to. In the context of a Notification to Receive this element provides little business value. 

**==> picture [51 x 60] intentionally omitted <==**

**==> picture [73 x 57] intentionally omitted <==**

**Min 1 – Max 1** 

**Min 0 – Max 1** 

When _**Related Account**_ is utilized, like _**Account**_ , the _**Identification**_ and _**Currency**_ element become mandatory. 

Additionally, the nested _**Type**_ element, _**Name**_ and nested _**Proxy**_ element are optionally available. **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1** 

**==> picture [57 x 56] intentionally omitted <==**

_Related Account_ uses a variety of common elements described in more detail within the _Account_ section. 

_Notification Related Account Identification Type_ 

**==> picture [20 x 10] intentionally omitted <==**

---

<!-- ELEMENT 686 -->
**Min 0 – Max 1** 

The Notification to Receive _**Total Amount**_ the sum of all the amounts of all the _**Item**_ message provides entries. Where utilised the _**Item**_ element is a mandatory element which contains information about the expected receipt. The Notification to Receive can contain multiple items. _**Expected Value Date**_ is the date on which the final receiving agent expects to receive the total amount. **Min 0 – Max 1** 

**10 $** 

The Total Amount provides a control total where there are multiple credits recorded within the Item element. The Total Amount element should not be used where there is a single expected credit. 

**==> picture [57 x 56] intentionally omitted <==**

**==> picture [385 x 16] intentionally omitted <==**

**----- Start of picture text -----**<br>
The Expected Value Date  takes the format YYYY-MM-DD<br>**----- End of picture text -----**<br>


_Notification Total Amount Notification Expected Date_ 

**==> picture [11 x 11] intentionally omitted <==**

---

<!-- ELEMENT 687 -->
Mandatory _**Name**_ (where a BIC identifier is not provided) by which the party is known 

or The Notification to Receive message describes the **Party Agent** that owes the amount of money as the _**Debtor**_ . The following describes the _Debtor_ nested **Party** elements in greater detail. 

_**Name**_ 

**==> picture [213 x 295] intentionally omitted <==**

**==> picture [272 x 192] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Debtor<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Debtor_ address details 

**==> picture [92 x 90] intentionally omitted <==**

**----- Start of picture text -----**<br>
Identification<br>**----- End of picture text -----**<br>


Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

Optional element to _**Country of**_ capture the Debtor’s ISO _**Residence**_

---

<!-- ELEMENT 688 -->
**==> picture [440 x 364] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>Party  or  Agent that  identifies the  Debtor<br>BICFI<br>following describes the<br>Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Debtor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either  Postal<br>structured or unstructured  Debtor Address<br>**----- End of picture text -----**<br>


The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the _**Debtor**_ . The following describes the _Debtor_ nested **Agent** elements in greater detail. 

**==> picture [214 x 295] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 689 -->
**==> picture [51 x 55] intentionally omitted <==**

**Min 0 – Max 1** The _**Debtor Agent**_ element in the camt.057 Notification to Receive captures the Debtor Agent of the payment i.e., the Financial Institution servicing an account for the Debtor. The _**Debtor Agent**_ and _**Intermediary Agent**_ elements allow the Treasury function at the Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time. 

**Min 0 – Max 1** 

**==> picture [51 x 54] intentionally omitted <==**

**==> picture [61 x 54] intentionally omitted <==**

The _**Intermediary Agent**_ element in the camt.057 Notification to Receive capture the Intermediary agent between the Debtor Agent and the Account Servicer i.e. the Agent from whom the Creditor Agent expects to receive the payment from. 

The _**Debtor Agent**_ and _**Intermediary Agent**_ elements allow the Treasury function at the Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time. 

The _**Debtor Agent**_ and _**Intermediary Agent**_ elements allow the Account Servicing Institution’s Treasury department to proactively follow up, as necessary, the actual payment if it fails to arrive by an expected time. 

**==> picture [143 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
Notification<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 690 -->
**Min 1 – Max *** 

The Notification to Receive _**Item**_ element details of the amount on the message mandatory provides expected account serviced by the account servicer. There is no equivalent field in the legacy MT210 Notice to Receive. 

**==> picture [60 x 56] intentionally omitted <==**

The various nested elements within the _**Item**_ element are useful in the case where very there are multiple credits. The Creditor Agent will be able to reconcile the incoming receipts against the list of expected receipts detailed in the _**Item**_ element and will be check completeness of all expected receipts and identify any missing receipts. 

**==> picture [54 x 51] intentionally omitted <==**

A single occurrence of _**Item**_ should be used unless bilaterally agreed. 

_Notification Item_ 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [19 x 10] intentionally omitted <==**

**==> picture [20 x 10] intentionally omitted <==**

_Identification_

---

<!-- ELEMENT 691 -->
## **Min 1 – Max *** 

The Notification to Receive message mandatory _**Item**_ element provides details of the expected amount on the account serviced by the account servicer. There is no equivalent field in the legacy MT210 Notice to Receive. 

**==> picture [61 x 56] intentionally omitted <==**

Only the _**Identification**_ and _**Amount**_ elements are mandatory. 

**==> picture [454 x 241] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1<br>End to End<br>Account<br>Identification UETR<br>Identification Account<br>Owner<br>Min 0 – Max 1 Min 0 – Max 1 Min 1 – Max 1 Min 0 – Max * Min 0 – Max 1<br>Expected<br>Account Related<br>Amount Value Debtor<br>Servicer Account<br>Date<br>Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1<br>Debtor<br>Intermediary<br>Purpose<br>Agent<br>Agent<br>**----- End of picture text -----**<br>


**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

---

<!-- ELEMENT 692 -->
Use case should be considered as a principal example whereby use case may be cross referenced 

## **Notification to Receive multiple receipts** 

Use Case c.57.1.1 – Notification to Receive (camt.057) followed by Customer Credit Transfers (pacs.008) Use Case c.57.1.2 – Notification to Receive (camt.057) followed by FI Credit Transfers (pacs.009) Use Case c.57.1.3 – Notification to Receive (camt.057) where the receipt is settled by the cover method. Use Case c.57.1.4 – Notification to Receive (camt.057) for a FI Credit Transfers cover (pacs.009 cov).

---

<!-- ELEMENT 693 -->
**(pacs.008)** 

**==> picture [601 x 297] intentionally omitted <==**

**----- Start of picture text -----**<br>
5<br>2 3 4<br>camt.053<br>pacs.008 pacs.008<br>C<br>A B camt.057<br>1<br>3 5<br>1<br>Creditor is expecting to receive a  Debtor Agent (A) initiates a  Creditor Agent (C) as Account<br>payment from the Debtor. As the  serial payment towards the  Servicer sends and end of day<br>Account Owner sends a  Creditor Agent (C) using  statement to Creditor as<br>Notification to Receive to Agent  Agents B as an intermediary. Account Owner confirming<br>C as Account Servicer. accounting entries.<br>2 4<br>Debtor initiates a payment<br>Agent (B) processes the<br>instruction to the Debtor Agent (A).<br>payment on to the Creditor<br>Agent (C).<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 694 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 4<br>2 3<br>camt.053<br>pacs.009 pacs.009<br>C<br>A B camt.057<br>1<br>4<br>2<br>1<br>Creditor Agent (C) as Account<br>Creditor is expecting to receive a  Debtor (A) initiates a serial payment<br>Servicer sends and end of day<br>payment from Debtor. As the  towards the Creditor Agent (C) using  statement to Creditor as<br>Account Owner sends a  Agents (B) as an intermediary.<br>Account Owner confirming<br>Notification to Receive to Agent C<br>accounting entries.<br>as Account Servicer.<br>3<br>Agent (B) processes the payment on<br>to the Creditor Agent (C).<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 695 -->
**==> picture [72 x 15] intentionally omitted <==**

**----- Start of picture text -----**<br>
method.<br>**----- End of picture text -----**<br>


**==> picture [779 x 358] intentionally omitted <==**

**----- Start of picture text -----**<br>
2a<br>1<br>pacs.008<br>A D<br>2b<br>3<br>4<br>5<br>1<br>Debtor initiates a payment  pacs.009 cov<br>instruction to the Debtor Agent<br>B 5<br>C<br>Agent C receives the payment and<br>2a<br>3 credits the account of Agent D as<br>Debtor Agent (A) initiates a payment using  the Creditor, producing an end of<br>Upon receipt of the pacs.008<br>the cover method to the Creditor Agent (D) day account statement report. An<br>advising settlement will occur<br>optional real time notifications e.g.<br>via a cover payment. Agent D<br>advice of credit may have also<br>sends a Notification to<br>2b been created at the time of the<br>Receive to Agent C.<br>In parallel the Debtor Agent (A) initiates a covering  credit posting.<br>payment to credit the account of Agent (D) who become<br>the Creditor of the cover payment (pacs.009 cov).<br>4<br>Agent A’s role also changes in the cover payment<br>where it becomes the Debtor, whereby Agent A’s  Agent B processes the payment<br>account with their correspondent (Agent B) is debited on to Agent C<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 696 -->
**cov).** 

**==> picture [823 x 355] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2a<br>pacs.008<br>A D<br>2b<br>1 3b<br>Agent B also sends a notification to<br>Debtor initiates a payment<br>receive on behalf of Agent D to notify<br>instruction to the Debtor Agent 6<br>Agent C a credit is expect on their<br>3b account.<br>2a<br>Debtor Agent (A) initiates a payment  4<br>using the cover method towards the  Agent E processes the cover payment on to Agent<br>B C<br>Creditor Agent (D) F.<br>3a<br>2b<br>5<br>In parallel the Debtor Agent (A)<br>Agent F processes the cover payment on to Agent<br>initiates a covering payment to credit<br>C.<br>the account of Agent (D) who become<br>the Creditor of the cover payment<br>5<br>(pacs.009 cov).<br>6<br>Agent C receives the cover payment (as the<br>3a pacs.009 cov Creditor Agent) recognising they have also be<br>Agent B processes the cover payment  E 4 F Notified they would receive this payment (by<br>on to Agent E camt 057) They apply value to Agent D<br>pacs.009<br>cov pacs.009<br>cov<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 697 -->
# **Notification to Receive Cancelation Advice** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 698 -->
**==> picture [137 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.058<br>**----- End of picture text -----**<br>


**==> picture [110 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


The _Notification To Receive Cancellation Advice_ message is sent by an account owner or by a party acting on the account owner's behalf to one of the account owner's account servicing institutions. It is used to advise the account servicing institution about the cancellation of a notification sent in a previous _Notification To Receive_ message. 

**==> picture [110 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
Original<br>Notification<br>**----- End of picture text -----**<br>


**==> picture [110 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cancellation<br>Reason<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 699 -->
**==> picture [360 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>A<br>camt.057<br>pacs<br>camt.058<br>**----- End of picture text -----**<br>


Role of the Creditor Agent and Creditor in the payment changes description in the Notification to Receive message (camt.057). The Account Owner is typically the Creditor and the Account Servicer is typically the Creditor Agent. The Notification to Receive Cancellation Advice (camt.058) is used to request the cancellation of a previous Notification to Receive.

---

<!-- ELEMENT 701 -->
**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 cash management reporting message has a _Message Identification_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

**Min 1 – Max 1** The _**Message Identification**_ in the Cash Management (camt) messages is equivalent to field 20 Transaction Reference Number of the MT 292 in the legacy MT Request for Cancellation. 

_Group Header_ Message Identification

---

<!-- ELEMENT 702 -->
## **Min 1 – Max 1** 

## The camt.058 message _**Creation Date Time**_ captures the date and time which the message was created. 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 703 -->
## **Min 0 – Max 1** 

The Notification to Receive Cancellation Advice _**Message Sender**_ nested element provides details of the _**Party**_ or _**Agent**_ that is sending the message, where the _**Message Sender**_ is different from the account owner. 

This element has no equivalent in the legacy MT 292 Request for Cancellation. 

## Where _**Message Sender, Party**_ is used the nested: 

**==> picture [57 x 82] intentionally omitted <==**

- _**Name**_ **Min 0 – Max 1** 

- • _**Postal Address**_ **Min 0 – Max 1** 

- _**Identification**_ **Min 0 – Max 1** 

- **Min 0 – Max 1** 

- _**Contact Details**_ 

May be used to capture information related to this party. 

Where _**Message Sender, Agent**_ is used the nested _**Financial Institution**_ : 

- _**BICFI**_ 

**Min 1 – Max 1** 

- _**Clearing System Member Identification**_ 

- • _**LEI**_ 

**Min 0 – Max 1 Min 0 – Max 1** 

_Group Header_ Message _Sender Name_ 

May be used to capture information related to this Agent. 

**==> picture [11 x 11] intentionally omitted <==**

---

<!-- ELEMENT 705 -->
## **Min 1 – Max 1** 

The Notification to Receive Cancellation Advice _**Original Notification**_ element contains nested elements to provide further details on the original camt.057 notification to receive. such as the related parties, the expected amount to be received and value date of the expected receipt. 

The _**Original Notification**_ nested element enables the ability to reconcile this cancellation advice against the Notification originally received, so that appropriate action can be take to remove the advised currency and amount from predicted currency positions at the Account Servicer. 

**1** 

**==> picture [137 x 38] intentionally omitted <==**

**----- Start of picture text -----**<br>
Camt.057<br>ISO<br>**----- End of picture text -----**<br>


## _**Group Header**_ 

- ➢ _**Message Identification**_ ➢ _**Creation Date Time**_ 

**==> picture [220 x 69] intentionally omitted <==**

**----- Start of picture text -----**<br>
Camt.058<br>ISO<br>Original Notification<br>**----- End of picture text -----**<br>


- ➢ _**Original Message Identification**_ ➢ _**Original Creation Date Time**_ 

_**Notification**_ 

_**Item**_ 

- ➢ _**Identification**_ 

- ➢ _**Debtor**_ 

- ➢ _**Identification**_ 

- ➢ _**End to End Identification**_ 

- ➢ _**Original Notification Identification**_ ➢ _**Original Notification Reference**_ 

   - ➢ _**Debtor**_ ➢ _**Original Item**_ 

      - ➢ _**Original Item Identification**_ ➢ _**Original End to End Identification**_

---

<!-- ELEMENT 706 -->
## **Min 1 – Max 1** 

The Notification to Receive Cancellation Advice message _**Original Message Identification**_ provides a . mandatory element to identify the Message Identification from the original camt.057 

**==> picture [89 x 59] intentionally omitted <==**

This 35 character identifier is a point-to-point reference used to unambiguously identify the Notification to Receive message, capture in its group header. 

**==> picture [11 x 11] intentionally omitted <==**

_Original Notification_

---

<!-- ELEMENT 707 -->
## **Min 0 – Max 1** 

The camt.058 _**Creation Date Time**_ the date and time which the message _**Original**_ captures original Notification to Receive was created. message 

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

**==> picture [11 x 11] intentionally omitted <==**

_Original Notification_

---

<!-- ELEMENT 708 -->
## **Min 1 – Max 1** 

## The Notification to Receive Cancellation Advice message _**Original Notification Identification**_ provides a . mandatory element to identify the account notification 

**==> picture [89 x 59] intentionally omitted <==**

Unique reference assigned by the account owner to unambiguously identify the original account notification. 

**==> picture [11 x 11] intentionally omitted <==**

_Original Notification_

---

<!-- ELEMENT 709 -->
Mandatory _**Name**_ (where a BIC identifier is not provided) by which the party is known 

or The Notification to Receive message describes the **Party Agent** that owes the amount of money as the _**Debtor**_ . The following describes the _Debtor_ nested **Party** elements in greater detail. 

_**Name**_ 

**==> picture [213 x 295] intentionally omitted <==**

**==> picture [272 x 192] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Debtor<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Debtor_ address details 

**==> picture [92 x 90] intentionally omitted <==**

**----- Start of picture text -----**<br>
Identification<br>**----- End of picture text -----**<br>


Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

Optional element to _**Country of**_ capture the Debtor’s ISO _**Residence**_

---

<!-- ELEMENT 710 -->
**==> picture [440 x 364] intentionally omitted <==**

**----- Start of picture text -----**<br>
The BIC which<br>Party  or  Agent that  identifies the  Debtor<br>BICFI<br>following describes the<br>Information used to identify a  Clearing<br>Debtor by a clearing system  System<br>identifier.  Member Id<br>Debtor<br>LEI<br> by which the Agent is  Name<br>Nested element capturing either  Postal<br>structured or unstructured  Debtor Address<br>**----- End of picture text -----**<br>


The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the _**Debtor**_ . The following describes the _Debtor_ nested **Agent** elements in greater detail. 

**==> picture [214 x 295] intentionally omitted <==**

Legal entity identifier of the financial institution. 

_**Name**_ by which the Agent is known

---

<!-- ELEMENT 711 -->
**==> picture [52 x 55] intentionally omitted <==**

**Min 0 – Max 1** The _**Debtor Agent**_ element in the camt.058 Notification to Receive Cancellation Advice captures the Debtor Agent provided in the original Notification to Receive (camt.057) i.e., the Financial Institution servicing an account for the Debtor. 

**==> picture [61 x 42] intentionally omitted <==**

Debtor Agent may be provided within the _**Original Notification**_ 

**==> picture [11 x 11] intentionally omitted <==**

_Original Notification_

---

<!-- ELEMENT 712 -->
## **Min 1 – Max 1** 

The Notification to Receive Cancellation Advice _**Original Item Reference**_ nested element captures  the references of the Original Item in the original Notification to Receive message. 

## **Min 1 – Max *** 

**==> picture [60 x 56] intentionally omitted <==**

The _**Original Item**_ nested element is repetitive as the original Notification to Receive message has the ability to notify on more than one item i.e. currency and amount expect. The following elements are nested within _**Original Item**_ , of which _**Identification**_ and _**Amount**_ are required. 

**==> picture [707 x 105] intentionally omitted <==**

**----- Start of picture text -----**<br>
Min 1 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 1 – Max 1 Min 0 – Max * Min 0 – Max 1 Min 0 – Max 1<br>End to End Expected Debtor<br>Identification Identification UETR Amount Value Debtor Agent<br>Date<br>Original Notification<br>**----- End of picture text -----**<br>


**==> picture [24 x 7] intentionally omitted <==**

---

<!-- ELEMENT 714 -->
**Min 1 – Max 1** 

The Notification to Receive Cancellation Advice _**Cancellation Reason**_ nested element captures information associated with the reason for the Cancellation request. 

## ? 

**Min 0 – Max 1** the _**Originator**_ element helps identify the party who issued the Cancellation request. Typically, this element would be used to identify the Account Owner as the Originator of the request, where the Notification to Receive Cancelation Advice a _**Sender**_ on the message captured _**Message**_ acting account owner’s behalf. 

**Min 1 – Max 1** the _**Reason**_ is mandatory and represented by an embedded CBPR+ Cancellation _**Code**_ choice ( ) 

**Min 0 – Max 2** The _**Additional Information**_ element also be included to further details on the may provide Cancellation reason. 

**==> picture [35 x 32] intentionally omitted <==**

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request. 

_Cancellation Reason_ 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [11 x 10] intentionally omitted <==**

_Originator_

---

<!-- ELEMENT 715 -->
Use case should be considered as a principal example whereby use case may be cross referenced 

## **Notification to Receive multiple receipts** 

Use Case c.58.1.1 – Cancellation Advice for a Notification to Receive (camt.057) expecting a Customer Credit Transfers (pacs.008) Use Case c.58.1.2 – Cancellation Advice for a Notification to Receive (camt.057) expecting a FI Credit Transfers (pacs.009) Use Case c.58.1.3 – Cancellation Advice for a Notification to Receive (camt.057) where the receipt is settled by the cover method.

---

<!-- ELEMENT 716 -->
## **Customer Credit Transfers (pacs.008)** 

**==> picture [615 x 221] intentionally omitted <==**

**----- Start of picture text -----**<br>
5<br>C<br>A B camt.057 1<br>camt.058<br>2<br>1 2<br>Creditor subsequently understand the<br>Creditor is expecting to receive a<br>payment should no longer be expected<br>payment from the Debtor. As the<br>for the given amount. They issue a<br>Account Owner they send a<br>cancellation advice to Agent C as<br>Notification to Receive to Agent<br>C as Account Servicer. Account Servicer, providing the reason<br>NOLE (not longer expected).<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 717 -->
## **Transfers (pacs.009)** 

**==> picture [602 x 218] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>C<br>A B camt.057 1<br>camt.058<br>2<br>1 2<br>Creditor is expecting to receive a<br>Creditor subsequently understand the<br>payment from Debtor. As the<br>payment should no longer be expected<br>Account Owner sends a<br>for the given amount. They issue a<br>Notification to Receive to Agent C<br>cancellation advice to Agent C as<br>as Account Servicer.<br>Account Servicer, providing the reason<br>NOLE (not longer expected).<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 718 -->
## **is settled by the cover method.** 

**==> picture [779 x 354] intentionally omitted <==**

**----- Start of picture text -----**<br>
1a<br>pacs.008<br>A 4 camt.056 D<br>1b 2<br>5<br>Rejected<br>+Reason  3<br>B<br>C 4<br>1a Agent A send a Request for<br>2 Cancellation to Agent D including<br>Debtor Agent (A) initiates a payment using<br>Upon receipt of the pacs.008  the reason COVR to confirm the<br>the cover method to the Creditor Agent (D)<br>advising settlement will occur  cover payment was cancelled.<br>via a cover payment. Agent D<br>sends a Notification to<br>1b<br>Receive to Agent C. 5<br>In parallel the Debtor Agent (A) initiates a covering<br>payment to credit the account of Agent (D) who become  Agent D subsequently issue a<br>the Creditor of the cover payment (pacs.009 cov).   cancellation advice to Agent C as<br>3<br>Agent A’s role also changes in the cover payment  Account Servicer, providing the<br>where it becomes the Debtor, whereby Agent A’s  Agent B rejects the payment  reason NOLE (not longer<br>account with their correspondent (Agent B) is debited advising Agent A expected)<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 719 -->
# **Account Reporting Request** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 720 -->
**==> picture [186 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.060<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Reporting Request<br>**----- End of picture text -----**<br>


**==> picture [60 x 56] intentionally omitted <==**

The AccountReportingRequest message is sent by the account owner, either directly or through a forwarding agent, to one of its account servicing institutions. It is used to ask the account servicing institution to send a report for the account owner's account: ▪ BankToCustomerAccountReport (camt.052) or ▪ BankToCustomerStatement (camt.053) or ▪ BankToCustomerDebitCreditNotification (camt.054). 

Account reports are often configured by the Account Servicing Institution as part of a static configuration. The Account Report Request could however be used as an alternative mechanism to request reports on a frequent or ad hoc basis. 

Account Report Request can contain multiple _Reporting Request_ elements as

---

<!-- ELEMENT 721 -->
**==> picture [797 x 350] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pacs.008<br>pacs.002<br>camt.060 pacs.008<br>camt.060<br>camt report camt.060 camt.060<br>camt report<br>camt report camt report<br>Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Report Request<br>message to Account Servicer and Account Owner. Whereby the report request is sent by the Account Owner or authorised<br>party to the Account Servicer. This message is used to request a report/s of the entries on an account, and/or to provide<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 723 -->
## **Min 1 – Max 1** 

**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 cash management reporting message has a _**Message Identification**_ element, located in the Group Header. This 35 character identifier is a point to point reference used to unambiguously identify the message. 

For Cash Management (camt) messages the _Message Identification_ has no exact equivalent in the legacy MT Customer Statement message. However the _Transaction Reference Number_ (Field 20) could be considered a similar comparison. 

_Group Header_ Message Identification

---

<!-- ELEMENT 724 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 725 -->
## **Min 0 – Max 1** 

The Account Report Request _**Message Sender**_ nested element provides details of the party that is sending the request. 

This element **should only** be used to identify the _Message Sender_ when different from the account owner. 

**==> picture [65 x 78] intentionally omitted <==**

Where _**Message Sender**_ is used, a choice of nested **Party** or **Agent** may be used to identify the Sender. 

## **Party** : 

**Agent** : 

- _**Name**_ **Min 0 – Max 1** 

- • _**Postal Address**_ **Min 0 – Max 1** • _**Identification**_ **Min 0 – Max 1** • **Min 0 – Max 1** _**Country of Residency**_ 

**==> picture [36 x 35] intentionally omitted <==**

Take me to the Agent identification 

**==> picture [19 x 12] intentionally omitted <==**

**==> picture [10 x 10] intentionally omitted <==**

_Group Header_ Message _Sender_

---

<!-- ELEMENT 727 -->
**Min 1 – Max *** The Account Reporting Request _**Reporting Request**_ nested element capture the detail related the request. 

**==> picture [134 x 101] intentionally omitted <==**

Many **Account Servicing Institutions** service their **Account Owner** customers through statics account configuration/s. Whereby a variety of reports can be generated on either a time or event bases routine. 

The _**Reporting Request**_ may be used as either an alterative to a static configuration or to request ad hoc reports (whether that be an additional report to the statics configuration or to resend reports previous reported). 

**==> picture [11 x 10] intentionally omitted <==**

_Reporting Request_

---

<!-- ELEMENT 728 -->
## **Min 1 – Max 1** 

The Account Reporting Request message _**Identification**_ provides a mandatory element to identify the Request 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the account owner (or Message Sender on behalf of the account owner) to unambiguously identify the account statement. Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT request message. 

**==> picture [11 x 6] intentionally omitted <==**

---

<!-- ELEMENT 729 -->
## **Min 1 – Max 1** 

The Account Reporting Request message _**Requested Message Name Identification**_ provides a mandatory element to identify the name of the report being request. 

**==> picture [134 x 101] intentionally omitted <==**

This element specifies which type of report is begin requested. The report is representedby its full name. For example: **camt.052.001.08** or **camt.053.001.08** or **camt.054.001.08** 

**==> picture [12 x 10] intentionally omitted <==**

---

<!-- ELEMENT 730 -->
## **Min 0 – Max 1** 

The Account Reporting Request message _**Account**_ provides nested elements to identify the account for which the request relates to. A number of elements are nested beneath _Account_ , of which the _**Identification**_ element is mandatory. 

**==> picture [128 x 81] intentionally omitted <==**

**Min 1 – Max 1** 

a unique _**Identification**_ for the account, between the Account Servicer and Account Owner. The element is further nested by choice of _**IBAN**_ or _**Other**_ to capture the account.

---

<!-- ELEMENT 731 -->
**Min 0 – Max 1** 

**Min 1 – Max 1 Min 0 – Max 1** The Account Reporting Request message _**Account**_ also provides an number of optional nested element to identify the account for which the request relates to. 

**==> picture [762 x 280] intentionally omitted <==**

**----- Start of picture text -----**<br>
An element which may either use an external ISO Cash Account Type code or<br>Type a proprietary code. It is used to identifier a particular type of account.<br>The Currency for which the account is held. This is identified<br>Currency using the three characters ISO currency code. ISO currency code.<br>Account<br>The Name of the Account, as Assigned by the servicing<br>Name<br>institution.<br>Proxy A nested element which contains a Proxy Identifier together with<br>the Proxy Type represented by either use an external ISO Proxy Proxy<br>**----- End of picture text -----**<br>


The _**Currency**_ for which the account is held. This is identified . using the three characters ISO currency code. ISO currency code. 

The Name of the Account, as Assigned by the servicing institution. 

A nested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO Proxy Proxy Account Type code or a proprietary code.

---

<!-- ELEMENT 732 -->
**Min  – Max 1** 

The Account Reporting Request message _**Account Owner**_ identifiers the mandatory owner of the account that the Account Report Request relates to. 

Where _**Account Owner**_ is used, a choice of nested **Party** or **Agent** may be used to identify the owner. 

**==> picture [71 x 65] intentionally omitted <==**

## **Party** : 

- _**Name**_ **Min 0 – Max 1** 

- • _**Postal Address**_ **Min 0 – Max 1** • _**Identification**_ **Min 0 – Max 1** • **Min 0 – Max 1** _**Country of Residency**_ 

## **Agent** : 

**==> picture [34 x 35] intentionally omitted <==**

Take me to the Agent identification 

**==> picture [60 x 47] intentionally omitted <==**

Typically the Account Name (see the previous page) represents the Account Owner’s Name in accordance with standard Know Your Customer (KYC). The mandatory Account Owner elements enables more detail to

---

<!-- ELEMENT 733 -->
## **Min 0 – Max 1** 

The Account Reporting Request message _**Account Servicer**_ provides an optional element to capture the Agent who is acting as an Account Servicing Institution. Typically, this would be the same Agent the Account Reporting Request is sent to, who is also identified in the Business Application Header. 

**==> picture [57 x 77] intentionally omitted <==**

## **Financial InstitutionIdentification** : 

- _**BICFI**_ 

- _**Clearing System Member Identification**_ 

- _**LEI**_ 

- _**Name**_ 

- • _**Postal Address**_ Take me to the Agent identification

---

<!-- ELEMENT 734 -->
## **Min 0 – Max 1** 

The Account Reporting Request message _**Report Period**_ provides the ability to specify the period for which the request relates. Where used this nested element captures a mandatory _**From to Date**_ and an optionally _**From to Time**_ element. **Min 1 – Max 1** 

**Min 0 – Max 1** 

_**From to Date**_ captures a mandatory _**From Date**_ and an optional _**To Date**_ . It allows the request to specify the date period for which the report is being requested. 

**10** 

**==> picture [60 x 32] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are 

**==> picture [12 x 11] intentionally omitted <==**

_Reporting Request       Report Period_

---

<!-- ELEMENT 735 -->
## **Min 0 – Max 1** 

**==> picture [17 x 16] intentionally omitted <==**

The Account Reporting Request message _**Reporting Sequence**_ specifies the choice of identification This can be used as an alterative to the where sequences. _**Reporting Period**_ to request a sequence of reports, the Account Servicing Institution uses this element within the reports they provide. 

Where used the _**Reporting Sequence**_ mandate a choice of nested element: 

**A B D C** 

• **Min 1 – Max 1** _**From Sequence**_ identifies the start of a sequence range. • **Min 1 – Max 1** _**To Sequence**_ identifies the end of a sequence range. • **Min 1 – Max *** _**From To Sequence**_ identifies the start and end of a sequence range. • **Min 1 – Max *** _**Equal Sequence**_ identifies a sequence. • _**Not Equal Sequence**_ identifies a sequence to be excluded. **Min 1 – Max *** 

**==> picture [10 x 6] intentionally omitted <==**

**==> picture [19 x 7] intentionally omitted <==**

---

<!-- ELEMENT 736 -->
**Min 0 – Max 1** The Account Reporting Request message _**Requested Transaction Type**_ provides the ability to identify the specific type of transactions the request wishes to be reported. 

**Min 1 – Max 1 Min 1 – Max 1** Where used the _**Status**_ element and _**Credit Debit Indicator**_ elements are mandatory. 

**==> picture [109 x 64] intentionally omitted <==**

- _**Status**_ is a nested element which may either use a choice of external ISO Entry Status code or a proprietary code. It is used to indicate the transaction entry status for which the requested reported should reflect. 

- _**Credit Debit Indicator**_ is a choice of embedded code to indicate whether Debit or Credit transaction entries should be reported. 

**Min 0 – Max 1** An optional _**Floor Limit**_ element may also be used. This element requests a minimum value, for which transaction entries above this value should be reported. Where used the _**Amount**_ and _**Credit Debit Indicator**_ elements are mandatory. 

**==> picture [59 x 48] intentionally omitted <==**

As a request for specific transaction type/s to be reported, typically this request would relate to a camt.052 Bank to Customer Account Report where the specified balance information is an intraday report. The use of the camt.060 Account Reporting Request and the ability to specify specific reporting requirements in the

---

<!-- ELEMENT 737 -->
## **Min 0 – Max *** 

The Account Reporting Request message _**Requested Balance Type**_ provides the ability to identify the specific type of balances the request wishes to be reported. 

**Min 1 – Max 1** 

**==> picture [131 x 108] intentionally omitted <==**

Where used a choice of balance _**Code**_ is mandatory which may either use a choice of external ISO Balance Type code or a proprietary code. 

**Min 0  – Max 1** An optional _**Sub Type**_ element may also be used which a choice of external ISO Balance Sub Type code or a proprietary code. 

**==> picture [60 x 60] intentionally omitted <==**

As a request for specific balance type/s (or sub balance type/s) to be reported, typically this request would relate to a camt.052 Bank to Customer Account Report where the specified balance information is an intraday report. The use of the camt.060 Account Reporting Request and the ability to specify specific reporting requirements in the request is dependent on the Account Servicing Institution and should bilaterally agreed by

---

<!-- ELEMENT 738 -->
Use case should be considered as a principal example whereby use case may be cross referenced 

**Financial Institution Account Reporting Request** Use Case c.60.1.1 – High Level Financial Institution daily Account Reporting Request Use Case c.60.1.2 – Financial Institution interim Account Reporting Request

---

<!-- ELEMENT 739 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>2 3<br>1<br>camt.060<br>pacs.009 pacs.009<br>A pacs.002 B pacs.002 C camt.053 D<br>5<br>Settlement<br>Complete<br>1 3<br>Payment Market Infrastructure,<br>Agent D requests a daily statement<br>Debtor initiates a payment  settles the payment between<br>using a camt.060 (not having an<br>instruction to the Debtor Agent Agent B and Agent C as direct<br>automatic statement produced by<br>participants of the Market<br>their account servicing institution<br>Infrastructure, and provides a<br>settlement confirmation to Agent B<br>4 5<br>2<br>Agent B processes the payment  Agent C credits the account of the  Agent C produces a customer<br>on Agent C, via the Payment  Creditor (Agent D) statement (camt.053) following the<br>Market Infrastructure. request from Agent D<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 740 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>2 3<br>1<br>camt.060<br>pacs.009 pacs.009<br>A pacs.002 B pacs.002 C camt.052 D<br>camt.053<br>5<br>Settlement<br>Complete<br>1 3<br>Payment Market Infrastructure,<br>Agent D requests an interim<br>Debtor initiates a payment  settles the payment between<br>statement using a camt.060 (not<br>instruction to the Debtor Agent Agent B and Agent C as direct<br>having an automatic interim statement<br>participants of the Market<br>produced by their account servicing<br>Infrastructure, and provides a  institution<br>settlement confirmation to Agent B<br>4 5<br>2<br>Agent B processes the payment  Agent C credits the account of the  Agent C produces a customer statement<br>on Agent C, via the Payment  Creditor (Agent D) (camt.052) following the request from<br>Market Infrastructure. Agent D<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 741 -->
# **(camt) messages**

---

<!-- ELEMENT 742 -->
**camt.029 –** Resolution of Investigation **camt.055 –** Customer Payment Cancellation Request **camt.056** – FI to FI Payment Cancellation Request

---

<!-- ELEMENT 743 -->
# **Resolution of Investigation** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 744 -->
**==> picture [137 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.029<br>**----- End of picture text -----**<br>


**==> picture [110 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
Assignement<br>**----- End of picture text -----**<br>


The Resolution of Investigation message is sent by an Agent to respond to the Cancellation Request, either directly or serially through other agents. 

The message is used to provide: 

▪ final outcome of the case, whether positive or negative, or ▪ an interim update prior to the final outcome. 

**==> picture [110 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
Status<br>**----- End of picture text -----**<br>


**==> picture [110 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cancellation<br>Details<br>**----- End of picture text -----**<br>


**==> picture [60 x 59] intentionally omitted <==**

Following a positive acceptance of the Cancellation request. The appropriate payment message (pacs.002 or pacs.004) is used to reject or return a

---

<!-- ELEMENT 745 -->
**==> picture [851 x 372] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pacs.008<br>pacs.002<br>pacs.008<br>camt.055<br>camt.053<br>camt.056<br>camt.056<br>camt.029<br>camt.029<br>The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide<br>a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any<br>payment previous settled is necessary to trigger reversing account postings.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 746 -->
**==> picture [770 x 292] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pacs.008<br>pacs.002<br>pacs.008<br>camt.055<br>camt.053<br>camt.056<br>camt.029<br>**----- End of picture text -----**<br>


The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any

---

<!-- ELEMENT 747 -->
The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview. 

**==> picture [385 x 116] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cancel & return<br>my payment<br>please CASE123<br>CASEABC<br>STATYXZ STAT789<br>Customer X<br>ISO<br>Camt.056 Payment Cancellation Request<br>**----- End of picture text -----**<br>


**==> picture [316 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
OK, I can<br>understand the<br>mistake.<br>CASE545<br>STAT54X<br>Customer Y<br>ISO<br>camt.029 Resolution of Investigation<br>**----- End of picture text -----**<br>


|**element**|**description**|**example**||**element**|**description**|**example**|
|---|---|---|---|---|---|---|
|Assigner|Sender of the camt.056|Agent B||Assigner|Sender of the camt.029|Agent C|
|Assignee|Receiver of the camt.056|Agent C||Assignee|Receiver of the camt.029|Agent B|
|Assignment<br>Identification|Unique Id generated by the assigner<br>to identify the Payment Cancellation<br>Request message|CASE123/1||Assignment<br>Identification|Unique Id generated by the assigner<br>to identify the Resolution of<br>Investigation message|STAT789/1|
|Cancellation<br>identification|<br>Optional Cancellation Id of the Agent<br>sending (assigner) the Payment<br>Cancellation Request message.|**CASE123**||Cancellation<br>Status<br>Identification|<br>Case Reference of the Agent<br>sending (assigner) the Resolution of<br>Investigation message.|**STAT789**|
|Case<br>Identification|<br>Case Id of the Agent sending<br>(assigner) the Payment Cancellation<br>Request message.|**CASE123**||Resolved<br>(Original) Case<br>Identification|<br>Case Id of the original case the<br>Resolution of Investigation is<br>responding to.|**CASE123**|



**==> picture [33 x 62] intentionally omitted <==**

---

<!-- ELEMENT 749 -->
## **Min 1 – Max 1** 

The Payment Cancellation Request message _**Identification**_ provides a mandatory element to identify the Request 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the assigner to unambiguously identify the Cancellation request. For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison. 

Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 750 -->
**==> picture [645 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.008<br>camt.056<br>pacs.008 Assigner  and<br>camt.029<br>camt.056<br>Assignee  Assigner camt.029<br>Agent: Agent A Agent: Agent B<br>leg.<br>Assignee Assigner<br>Agent: Agent B Agent: Agent C<br>**----- End of picture text -----**<br>


**==> picture [61 x 61] intentionally omitted <==**

_**Assigner**_ and _**Assignee**_ represent the Agents involved in the point-to-point investigation message exchange. These roles therefore change on each message leg. 

_Assignment_ 

**==> picture [10 x 11] intentionally omitted <==**

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 751 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 753 -->
**Min 1 – Max 1** 

## The Resolution of Investigation _**Confirmation**_ provides a mandatory element to specify the status of the Payment Cancellation Request’s investigation. 

## The _**Confirmation**_ element includes a choice of three embedded confirmation codes: 

**==> picture [46 x 46] intentionally omitted <==**

**----- Start of picture text -----**<br>
✓<br>**----- End of picture text -----**<br>


**==> picture [47 x 47] intentionally omitted <==**

**----- Start of picture text -----**<br>
X<br>**----- End of picture text -----**<br>


**==> picture [58 x 47] intentionally omitted <==**

**----- Start of picture text -----**<br>
?<br>**----- End of picture text -----**<br>


- _**CNCL**_ – The payment has been cancelled as requested. This status concludes the investigation, whereby a Payment Return may follow if funds need to be returned. 

- • _**PDCR**_ – The Investigation of the Payment Cancellation Request is pending i.e. is under ongoing investigation to provide a final status confirmation. An addition _**Cancellation Status Reason Information**_ should be provided to further clarify the current status. For example, a Status Reason code RQDA can be used to indicate debit authority has been requested from the Creditor. 

- – 

- _**RJCR**_ The Payment Cancellation Request is rejected. A status concluding the investigation which must include additional _**Cancellation Status Reason Information**_ to provide an explanation as to why the request was rejected. 

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

---

<!-- ELEMENT 755 -->
**Min 1 – Max 1** 

The Resolution of Investigation _**Transaction Information and Status**_ is a mandatory nested element to capture information related to the original payment and to provide further information on the status reason Payment Cancellation Request’s investigation. 

**==> picture [71 x 78] intentionally omitted <==**

As part of this nested element, information is captured to reference; the case the investigation is attempting to resolve, various original references related to the original payment and the investigation status information. 

**==> picture [10 x 5] intentionally omitted <==**

**==> picture [11 x 5] intentionally omitted <==**

---

<!-- ELEMENT 756 -->
## **Min 1 – Max 1** 

The Resolution of Investigation message _**Cancellation Status Identification**_ provides a mandatory element to identify the status update. 

**==> picture [90 x 58] intentionally omitted <==**

**----- Start of picture text -----**<br>
!<br>**----- End of picture text -----**<br>


Unique reference assigned by the resolution assigner to unambiguously identify the Cancellation status. 

For Exceptions and Investigations messages the _Cancellation Status Identification_ can be considered an equivalent in the legacy MT Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message. 

**==> picture [10 x 5] intentionally omitted <==**

**==> picture [11 x 5] intentionally omitted <==**

---

<!-- ELEMENT 757 -->
## **Min 1 – Max 1** 

The Resolution of Investigation message _**Resolved Case**_ provides a mandatory nested element to identify the Resolved Case _**Identification**_ and the _**Creator**_ of the case. 

## **Min 1 – Max 1** 

**==> picture [115 x 92] intentionally omitted <==**

**----- Start of picture text -----**<br>
id<br>✓<br>X<br>**----- End of picture text -----**<br>


The _**Identification**_ element captures the unique case reference assigned by the Payment Cancellation Request Assigner to unambiguously identify the Cancellation investigation case being resolved. 

For Exceptions and Investigations messages this _Case Identification_ can be considered an equivalent of the _Related Reference_ (Field 21) of the legacy MT Answer message. 

**Min 1 – Max 1** 

The _**Creator**_ element captures the party who created the Payment Cancellation Request investigation (see camt.056 Case Creator). 

This mandatory party can represent as either an _**Agent**_ i.e., the Bank who created the case or as a _**Party**_ i.e., the customer (for example the Debtor) who created the request. This element has no equivalent in the legacy MT Request for Cancellation message. 

**==> picture [10 x 5] intentionally omitted <==**

**==> picture [11 x 5] intentionally omitted <==**

---

<!-- ELEMENT 758 -->
**Min 1 – Max 1** 

The Resolution of Investigation uses elements in the _**Original Group Information**_ to capture the message identifier and name of the for to. The message underlying payment which the investigation relates mandatory _**Original Message Identification**_ contains the point-to-point reference from this payment, and the mandatory _**Original Message Name Identification**_ contains the message name of the underlying payment. Optionally the _**Original Creation Date Time**_ can also be captured. 

**==> picture [350 x 258] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>confirms the<br>pacs.008<br>to Financial Message<br>abcd1234<br>Identification<br>Institution<br>camt.056<br>camt.029<br>Assignment Identification xyz9875<br>Original Message<br>Original  abcd1234<br>Cancellatio Identification<br>n Details Group Original Message<br>**----- End of picture text -----**<br>


For example: 

_Original Message Name Identification_ “pacs.008.001.08” confirms the investigation relates to a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as “pacs.009.001.08” confirms the investigation relates to a pacs.009 Financial Institution Credit Transfer. 

**==> picture [35 x 34] intentionally omitted <==**

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 759 -->
The Resolution of Investigation also uses a number of other **Original** elements in the _**Transaction Information**_ to capture information from the underlying payment that the Cancellation request relates to. 

**==> picture [58 x 62] intentionally omitted <==**

The Original elements enables the _**Assignee**_ to identify the Payment which is being request to be cancelled. The following element (in addition to _Original Message identification_ and _Original Message Name Identification_ described on the previous page) are mandated: **Min 1 – Max 1** _**Original UETR**_ 

The following element (in addition to _Original Message identification_ and _Original Message Name Identification_ described on the previous page) are optional: _**Original End to End Identification**_ **Min 0 – Max 1** _**Original Instruction Identification**_ **Min 0 – Max 1** _Cancellation Details     Transaction Information and Status_ _**Original Transaction Identification**_ **Min 0 – Max 1** _Original Group Information Original Instruction Identification_ _**Original Clearing System Reference**_ **Min 0 – Max 1** 

_Cancellation Details     Transaction Information and Status Original Group Information Original Instruction Identification Original End to End Identification Original Transaction_

---

<!-- ELEMENT 760 -->
**Min 0 – Max 1** 

The Resolution of Investigation _**Cancellation Status Reason Information**_ nested element captures the information related to the status reason of the Cancellation Resolution. 

## **Min 0 – Max 1** 

the _**Originator**_ element helps identify the party who provided the Cancellation status. This party would have been included in the underlying payment and is also included the pacs.004 _Return Chain._ ? **Min 0 –0 – – Max 1** 

**==> picture [145 x 178] intentionally omitted <==**

**----- Start of picture text -----**<br>
the<br>the<br>**----- End of picture text -----**<br>


**Min 0 –0 – – Max 1** the _**Reason**_ for the Cancellation status, which is mandatory where the Resolution Status is RJCR, is represented by an embedded CBPR+ Cancellation _**Code**_ choice ( ) 

**Min 0 – Max 1** 

the _**Additional Information**_ element also be included to further details on the may provide Cancellation reason. 

**==> picture [35 x 32] intentionally omitted <==**

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request. 

_Cancellation Details     Transaction Information and Status Original Group Information Originator_ 

In the event that an **indemnity agreement** is need to be established, **INDM** should be indicated at the beginning of the Additional 

**==> picture [18 x 11] intentionally omitted <==**

---

<!-- ELEMENT 761 -->
Definitions and High Level Use Cases 

**Min 0 – Max 1** 

The Resolution of Investigation _**Reason**_ element is optional. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded _**Code**_ choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened after the coexistence period. 

|**Code**|**Name**|**Definition**|**Use Case**|
|---|---|---|---|
|AC04|Closed Account<br>Number|Account number specified has been<br>closed on the receiver’s books.|Complimenting aRejectStatus. Payment Cancellation Request can not be<br>accepted as the Creditor has since closed their account.|
|AGNT|Agent Decision|Reported when the cancellation<br>cannot be accepted because of an<br>agent refuses to cancel.|Complimenting aRejectStatus. Payment Cancellation Request can not be<br>accepted as an Agent in the payment transaction does not accept the<br>request.|
|AM04|Insufficient Funds|Amount of funds available to cover<br>specified message amount is<br>insufficient.|Complimenting aRejectStatus. Payment Cancellation Request can not be<br>accepted as the Creditor has insufficient funds to perform the return payment.|
|ARDT|Already Returned|Cancellation not accepted as the<br>transaction has already been returned.|Complimenting aRejectStatus. Payment Cancellation Request can not be<br>accepted as the payment has already return payment.|
|CUST|Customer Decision|Reported when the cancellation<br>cannot be accepted because of a<br>customer decision (Creditor).|Complimenting aRejectStatus. Payment Cancellation Request can not be<br>accepted as the Creditor does not provide authority to return the payment. i.e.<br>believe the payment was justified.|
|INDM|Indemnity Request|Indemnity is required before funds can<br>be returned|Complimenting aPendingorRejectStatus. Payment Cancellation Request<br>can not be accepted until an indemnity agreement is established.|

---

<!-- ELEMENT 762 -->
Definitions and High Level Use Cases 

|**LEGL**|**Legal Decision**|**Reported when the cancellation cannot be**<br>**accepted because of regulatory rules.**||
|---|---|---|---|
|NAAR|Narrative|Reason is provided as narrative information in the<br>additional reason information.|Complimenting aRejectorPendingStatus to provide further<br>narrativeAdditional Information.|
|NOAS|No Answer From<br>Customer|No response from beneficiary (to the cancellation<br>request).|Complimenting aRejectStatus. Payment Cancellation Request<br>can not be accepted as the Creditor has not responded to a<br>Debit Authority request to return the payment.|
|NOOR|No Original<br>Transaction<br>Received|Original transaction (subject to cancellation) never<br>received.|Complimenting aRejectStatus. Payment Cancellation Request<br>can not be accepted as it is believed that the original payment<br>was never received for the UETR and references provided.|
|PTNA|Passed To The<br>Next Agent|Reported when the cancellation request cannot be<br>accepted because the payment instruction has been<br>passed to the next agent.|Complimenting aPendingStatus. Payment has been onward<br>processed to the next agent in the transaction. The Payment<br>Cancellation Request has therefore been forward to this Agent,<br>a further resolution message will be sent once this Agent<br>provides a response.|
|RQDA|Requesting Debit<br>Authority|Reported when authority is required by the Creditor to<br>return the payment.|Complimenting aPendingStatus. Payment has been credited<br>to the creditor, Authority to Debit the Creditor and return the<br>payment is being request. A further resolution message will be<br>sent once the Creditor provides a response.|

---

<!-- ELEMENT 763 -->
Use case should be considered as a principal example whereby use case may be cross referenced 

## **Resolution of Investigation** 

Use Case c.29.1.1 – High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008) Use Case c.29.1.1.a – High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.29.1.2 – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008) Use Case c.29.1.2.a – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.29.2.1 – High Level Resolution of Investigation (camt.029) of a complete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.29.2.2 – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.29.2.3 – High Level Resolution of Investigation (camt.029) of a Customer Credit Transfers (pacs.008) where the cover is returned Use Case c.29.3.1 – High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer (pacs.009) Use Case c.29.4.1 – High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer advice (pacs.009 adv)

---

<!-- ELEMENT 764 -->
## **Transfer (pacs.008)** 

**==> picture [772 x 307] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.008 pacs.008 pacs.008 pacs.008<br>A camt.056 camt.056 C camt.056<br>B D<br>4 camt.029 camt.029 camt.029<br>3 2<br>1<br>1 3<br>Debtor Agent (B) updates their case  See use case p.8.1.1 for the original payment,<br>Agent D provides a final<br>history and relays the outcome of the  c.56.1.1 for case resolution and p.4.1.3. for an<br>outcome of the investigation to<br>investigation to Agent A using the  example payment return<br>Agent C using the camt.029.<br>camt.029<br>2<br>4<br>Debtor Agent (C) updates their<br>Debtor Agent (A) updates their case<br>case history and relays the<br>history and informs the customer of<br>outcome of the investigation to<br>the outcome of the investigation.<br>Agent B using the camt.029<br>**----- End of picture text -----**<br>


**==> picture [61 x 61] intentionally omitted <==**

---

<!-- ELEMENT 765 -->
## **Transfer (pacs.008) using gpi Stop and Recall** 

**==> picture [823 x 339] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.056<br>3 camt.056 2 1<br>camt.029<br>camt.029<br>pacs.008 pacs.008 pacs.008 pacs.008<br>A B C D<br>See use case p.8.1.1 for the original payment,<br>c.29.1.1 for case resolution and p.4.1.3. for an<br>example payment return<br>1 3<br>Agent D provides an update on Debtor Agent (A) updates their case<br>the investigation to the gpi history and informs the customer of the<br>Tracker using the camt.029. outcome of the investigation.<br>2<br>gpi Tracker forwards the<br>response to Agent A as the<br>initiator of the original camt.056<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 766 -->
## **Credit Transfer (pacs.008)** 

**==> picture [664 x 227] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.008 pacs.008 pacs.008<br>camt.056 camt.056<br>A C<br>B D<br>3 camt.029 camt.029<br>2 1<br>1<br>1 3<br>Agent C provides a final  See use caseuse case p.8.1.1<br>Debtor Agent (A) updates their case<br>outcome of the investigation to<br>history and informs the customer of<br>Agent B using the camt.029 example payment return<br>the outcome of the investigation.<br>**----- End of picture text -----**<br>


**==> picture [61 x 61] intentionally omitted <==**

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [208 x 35] intentionally omitted <==**

**----- Start of picture text -----**<br>
See use caseuse case p.8.1.1 for the original payment,<br>c.56.1.2 for case resolution and p.4.1.3. for an<br>example payment return<br>**----- End of picture text -----**<br>


**==> picture [180 x 65] intentionally omitted <==**

**----- Start of picture text -----**<br>
2<br>Debtor Agent (B) updates their<br>case history and relays the<br>outcome of the investigation to<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 767 -->
## **Credit Transfer (pacs.008) using gpi Stop and Recall** 

**==> picture [579 x 339] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.056<br>camt.056 2<br>3<br>camt.029 1<br>camt.029<br>pacs.008 pacs.008 pacs.008<br>A C<br>B<br>1 3<br>Agent C provides an update on Debtor Agent (A) updates their case<br>the investigation to the gpi history and informs the customer of the<br>Tracker using the camt.029. outcome of the investigation.<br>2<br>gpi Tracker forwards the<br>response to Agent A as the<br>initiator of the original camt.056<br>**----- End of picture text -----**<br>


**==> picture [61 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
D<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

---

<!-- ELEMENT 768 -->
## **Transfer (pacs.008) settled using a cover method** 

**==> picture [798 x 344] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.008<br>A pacs.002 D<br>3<br>1 2 camt.056<br>camt.029<br>pacs.009 cov pacs.009 cov<br>B pacs.002 C<br>See use case p.8.2.1 for the original payment,<br>Settlement  c.56.2.1 for case resolution and p.4.3.2 for an<br>Complete example payment return<br>1 2 3<br>Debtor request their bank to  Debtor Agent (A) assigns a  Agent D creates an investigation case. Recognising the<br>recall a previous instructed  Cancellation Request to Agent  payment has already been credited to the creditor. They request<br>payment, as the amount was  D (assignee) requesting the  debit authority, proving the reason specified for the return<br>incorrect. request and update Agent A.<br>original pacs.008 is returned,<br>Once the outcome to the debit authorisation is know a final<br>using reason code AM09.<br>resolution to the investigation can be relayed and any necessary<br>t t b i iti t d<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 769 -->
## **Credit Transfer (pacs.008) settled using a cover method.** 

**==> picture [798 x 329] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.008<br>A 2 camt.056 D 3<br>1<br>camt.029<br>pacs.009 cov pacs.009 cov<br>B pacs.002 C<br>See use case p.8.2.1 for the original payment,<br>Settlement  c.29.2.1 for case resolution and p.4.3.2 for an<br>Complete example payment return<br>1 2 3<br>Debtor request their bank to  Debtor Agent (A) assigns a  Agent D creates an investigation case. Recognising the<br>recall a previous instructed  Cancellation Request to Agent  payment has not been credited to the creditor. They update<br>payment, as the amount was  D (assignee) requesting the  Agent A that the Cancellation Request is accepted and arrange<br>incorrect. the necessary return payment once the pacs.009 cov settlement<br>original pacs.008 is returned,<br>is confirmed by Agent C<br>using reason code AM09.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 770 -->
## **Transfers (pacs.008) where the cover is returned** 

**==> picture [807 x 347] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.008<br>A 1 camt.056 D<br>camt.029<br>2<br>pacs.009 cov<br>+ Return<br>pacs.002<br>Reason  B C<br>See use case p.8.2.1 for an example of a  cover<br>+ Reject<br>payment c.56.2.1 for case resolution and p.4.3.3for<br>Reason  payment return<br>2<br>1<br>Agent D creates an investigation case. Recognising the<br>Debtor Agent (A) assigns a<br>Agent C receives the payment and  cover payment will not be received to settle the pacs.008.<br>Cancellation Request to Agent D<br>recognises the payment can not be  As the creditor has not been credited in advance of cover<br>(assignee) requesting the original<br>completed as requested e.g. the Agent D  settlement, a final resolution to the investigation can be<br>pacs.008 is considered null and<br>does not maintain an account with them.  provided. A payment return is not necessary.<br>void, using reason code COVR.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 771 -->
## **Credit Transfer (pacs.009)** 

**==> picture [734 x 186] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 pacs.009 pacs.009 camt.053<br>A pacs.002 B pacs.002 C camt.054 D<br>camt.056 camt.056<br>camt.029 2 camt.029 1<br>See use case p.9.1.1 for the cover payment sample<br>c.56.3.1 for case resolution and p.4.2.3 for payment<br>return<br>**----- End of picture text -----**<br>


**==> picture [427 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2<br>Agent C provides a final  Debtor Agent (B) updates their case<br>outcome of the investigation to  history and informs the customer<br>Agent B using the camt.029. (Agent A) of the outcome of the<br>investigation.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 772 -->
## **Credit Transfer advice (pacs.009 adv)** 

**==> picture [790 x 339] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 (ADV) camt.054<br>A B 2 camt.056 E F<br>1 camt.029 3<br>pacs.009<br>C pacs.002<br>D<br>See use case p.9.1.2 for the cover payment sample<br>c.56.4.1 for case resolution and p.4.2.3 for payment<br>return<br>1 2 3<br>Debtor request their bank to  Debtor Agent (A) assigns a  Agent E creates an investigation case. Recognising the payment<br>recall a previous instructed  Cancellation Request to Agent  has already been credited to the creditor. They request debit<br>payment, as the amount was  E (assignee) requesting the  authority, proving the reason specified for the return request and<br>incorrect. update Agent B.<br>original pacs.008 is returned,<br>Once the outcome to the debit authorisation is know a final<br>using reason code AM09.<br>**----- End of picture text -----**<br>


See use case p.9.1.2 for the cover payment sample c.56.4.1 for case resolution and p.4.2.3 for payment return 

Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed and any necessary

---

<!-- ELEMENT 773 -->
# **Customer Payment Cancellation Request** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 774 -->
**==> picture [186 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.055<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Assignment<br>**----- End of picture text -----**<br>


The Customer Payment Cancellation Request message is sent by an Agent to request the Cancellation of a payment initiation request previous sent. 

The message is sent either: 

- directly to the Agent a previous Payment initiation request was sent to. 

**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Underlying<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 775 -->
**==> picture [782 x 302] intentionally omitted <==**

**----- Start of picture text -----**<br>
F B<br>A<br>Debtor Initiating Party Forwarding Debtor Agent Creditor Agent Creditor<br>Agent<br>pain.001<br>Interbank pain.001<br>pain.002<br>Interbank pain.002 pacs.008<br>camt.055<br>camt.055 pacs.002<br>camt.053<br>camt.029<br>camt.029 camt.056<br>camt.029<br>**----- End of picture text -----**<br>


The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This

---

<!-- ELEMENT 776 -->
**Initiation”** 

**==> picture [60 x 61] intentionally omitted <==**

**==> picture [61 x 46] intentionally omitted <==**

**----- Start of picture text -----**<br>
Debtor<br>**----- End of picture text -----**<br>


**==> picture [59 x 56] intentionally omitted <==**

**==> picture [607 x 302] intentionally omitted <==**

**----- Start of picture text -----**<br>
I A B<br>Initiating Debtor Agent Creditor Agent Creditor<br>Party<br>Interbank pain.001<br>Interbank pain.002 pacs.008<br>camt.055 pacs.002<br>camt.053<br>camt.029 camt.056<br>camt.029<br>**----- End of picture text -----**<br>


The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This

---

<!-- ELEMENT 777 -->
**==> picture [784 x 300] intentionally omitted <==**

**----- Start of picture text -----**<br>
I A B C<br>Debtor Initiating Party Debtor Agent Creditor Agent Creditor<br>Interbank pain.001<br>Interbank pain.002 pacs.008<br>camt.055 pacs.002 pacs.008<br>camt.053<br>camt.029 camt.056 pacs.002<br>camt.029 camt.056<br>camt.029<br>**----- End of picture text -----**<br>


The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This

---

<!-- ELEMENT 778 -->
## The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview. 

**==> picture [807 x 320] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||||
|---|---|---|---|---|---|---|---|
|Cancel & return|OK, I can|
|my payment|understand the|
|please|CASE123|mistake.|
|CASE545|
|STAT789|STAT54X|
|Customer X|
|Customer Y|
|ISO|ISO|
|Camt.055 Payment Cancellation Request|camt.029 Resolution of Investigation|
|element|description|example|element|description|example|
|Assigner|Sender of the camt.055|Agent A|Assigner|Sender of the camt.029|Agent|
|Assignee|Receiver of the camt.055|Agent B|Assignee|Receiver of the camt.029|Agent A|
|Assignment|Unique Id|generated by the assigner|CASE123/1|Assignment|Unique Id|generated by the assigner|STAT789/1|
|Identification|to identify the Payment Cancellation|Identification|to identify the Resolution|of|
|Request message|Investigation message|
|Cancellation|Optional Cancellation|Id of the Agent|CASE123|Cancellation|Case|Reference of the Agent|STAT789|
|identification|sending (assigner) the Payment|Status|sending (assigner) the Resolution of|
|Cancellation Request message.|Identification|Investigation message.|
|Case|Case|Id of the Agent sending|CASE123|Resolved|Case Id of the original case the|CASE123|
|Identification|(assigner) the Payment Cancellation|(Original) Case|Resolution of Investigation is|
|Request message.|Identification|responding to.|
|Case|Party w ho created|the original|Agent A|Case Creator|Party w ho created|the original|Agent A|
|Creator|cancellation|request (w hich may be|cancellation|request (w hich is the|
|another Agent other than the current|same original case creator in the|
|Assigner.|Payment Cancellation Request)|

**----- End of picture text -----**<br>

---

<!-- ELEMENT 780 -->
## **Min 1 – Max 1** 

The Payment Cancellation Request message _**Identification**_ provides a mandatory element to identify the Request 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the assigner to unambiguously identify the Cancellation request. For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison. 

Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 781 -->
**==> picture [807 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pain.001<br>camt.055<br>pacs.008 Assigner  and  Assignee  represent the<br>camt.029<br>camt.056 Agents involved in the point-to-point<br>Assigner  Assignee investigation message exchange. These<br>camt.029<br>Agent: Agent A Agent: Agent B roles therefore change on each message<br>leg.<br>Assigner Assignee<br>Agent: Agent B Agent: Agent C<br>**----- End of picture text -----**<br>


_Assignment_ 

**==> picture [10 x 11] intentionally omitted <==**

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 782 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 783 -->
# **Information and Cancellation.**

---

<!-- ELEMENT 784 -->
## **Identification** 

## **Min 1 – Max 1** 

The Payment Cancellation Request message _**Original Payment Information Identification**_ provides a mandatory element to identify the Original Payment Initiation Request 

**==> picture [353 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>pain.001<br>Message<br>abcd1234<br>Identification<br>Payment Information<br>abcd1234<br>Identification<br>in the<br>camt.055<br>Assignment Identification xyz9875<br>Original Payment Infomation<br>abcd1234<br>Identification<br>Original Message<br>Underlying Original  Identification abcd1234<br>Group<br>Original Message<br>Information  Name Identification pain.001.001. 09<br>**----- End of picture text -----**<br>


This Unique reference identifies the Payment Information Identification from the original Payment Initiation request. 

Refer to the relevant Payment Information Identification element in the original message for details on that reference. 

Link to Pain.001 Link to Pain.008 

**==> picture [11 x 11] intentionally omitted <==**

_Underlying Original Payment Information and Cancellation_

---

<!-- ELEMENT 785 -->
## **Min 1 – Max 1** 

The Payment Cancellation Request uses elements in the _**Original Group Information**_ to capture the identifier and name of the for which the Cancellation is message message underlying payment being requested. The mandatory _**Original Message Identification**_ contains the point-to-point reference from this payment, and the mandatory _**Original Message Name Identification**_ contains the message name of the underlying payment. Optionally the _**Original Creation Date Time**_ can also be captured. 

**==> picture [352 x 256] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>confirms the<br>pain.001<br>Credit<br>Message<br>abcd1234<br>Identification<br>Payment Information<br>abcd1234<br>Identification<br>camt.055<br>Assignment Identification xyz9875<br>Original Payment Infomation<br>abcd1234<br>Identification<br>Original Message<br>Underlying Original  Identification abcd1234<br>Group<br>**----- End of picture text -----**<br>


For example: 

_Original Message Name Identification_ “pain.001.001.09” confirms the Cancellation request is for a pain.001 Interbank Customer Credit Transfer Initiation. 

**==> picture [35 x 34] intentionally omitted <==**

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 786 -->
## **Min 0 – Max 1** 

The Payment Cancellation Request message _**Cancelation Identification**_ provides an optional element to identify the Request 

**==> picture [90 x 58] intentionally omitted <==**

**----- Start of picture text -----**<br>
!<br>**----- End of picture text -----**<br>


Unique reference assigned by the assigner to unambiguously identify the Cancellation request. 

For Exceptions and Investigations messages the _Cancellation Identification_ can be considered an equivalent in the legacy MT Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message. 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [11 x 6] intentionally omitted <==**

_Underlying Original Payment Information and Cancellation_

---

<!-- ELEMENT 787 -->
**Min 1 – Max 1** 

The Payment Cancellation Request message _**Case**_ provides a mandatory nested element to identify the Case _**Identification**_ and the _**Creator**_ of the case. 

## **Min 1 – Max 1** 

The _**Identification**_ element captures a unique case reference assigned by the assigner to unambiguously identify the Cancellation investigation case. 

**==> picture [90 x 75] intentionally omitted <==**

**----- Start of picture text -----**<br>
id<br>**----- End of picture text -----**<br>


For Exceptions and Investigations messages the _Case Identification_ can be considered an equivalent of the _Transaction Reference Number_ (Field 20) of the legacy MT Request for Cancellation message. 

**Min 1 – Max 1** 

The _**Creator**_ element captures the party who created the investigation. This mandatory party can represent as either an _**Agent**_ i.e., the Bank who created the case or as a _**Party**_ i.e., the customer (for example the Debtor) who created the request. In CBPR+ the creator is always expected to be an Agent. This element has no equivalent in the legacy MT Request for Cancellation message. 

**==> picture [10 x 10] intentionally omitted <==**

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [11 x 7] intentionally omitted <==**

_Original Payment Information and Cancellation_ 

_Underlying_

---

<!-- ELEMENT 788 -->
The Payment Cancellation Request also uses a number of other **Original** elements in the _**Transaction Information**_ to capture information from the underlying payment that the Cancellation request relates to. 

The Original elements enables the _**Assignee**_ to identify the Payment which is being request to be cancelled. The following element (in addition to _Original Message identification_ and _Original Message Name Identification_ ) are mandated: 

**==> picture [58 x 62] intentionally omitted <==**

_**Original End to End Identification**_ **Min 1 – Max 1** _**Original UETR**_ **Min 1 – Max 1** _**Original Instructed Amount**_ **Min 1 – Max 1** 

One of the following elements is also required depending on the Date element in the original where Execution Date relates to the and message, Original Request pain.001 Original Request Collection Date relates to the pain.008 : 

_Underlying Original Payment Information and Cancellation Transaction Information Original Instruction Identification Original End to End Identification Original UETR Original Instructed Amount Original Requested Execution Date_ 

_**Original Requested Execution Date Original Request Collection Date**_ 

**Min 0 – Max 1 Min 0 – Max 1** 

The following element is optional:

---

<!-- ELEMENT 789 -->
**Min 1 – Max 1** 

The Payment Cancellation Request _**Cancellation Reason Information**_ nested element captures information associated with the reason for the Cancellation request. 

## ? 

**Min 0 – Max 1** the _**Originator**_ element helps identify the party who request the payment Cancellation. This party would have been included in the underlying payment and is also included the pacs.004 _Return Chain as the Creditor._ 

**Min 1 – Max 1** the _**Reason**_ is mandatory and represented by an embedded CBPR+ Cancellation _**Code**_ choice ( ) **Min 0 – Max 2** the _**Additional Information**_ element also be included to further details on the may provide Cancellation reason. Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request. 

**==> picture [10 x 12] intentionally omitted <==**

_Underlying Original Payment Information and Cancellation Transaction Information     Cancellation Reason Info’ Originator_ 

**==> picture [18 x 11] intentionally omitted <==**

---

<!-- ELEMENT 790 -->
Definitions and High Level Use Cases 

**Min 1 – Max 1** 

The Payment Cancellation Request _**Reason**_ element is mandatory. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded _**Code**_ choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened after the coexistence period. 

|**Code**|**Name**|**Definition**|**Use Case**|
|---|---|---|---|
|AGNT|Incorrect Agent|Agent in the payment workflow is<br>incorrect.|A payment previous executed is identified as containing an incorrect<br>correspondent (Agent) within the payment flow. A Cancellation request is<br>generated so that the payment can be remediated following the successful<br>return.|
|AM09|Wrong Amount|Amount is not the amount agreed or<br>expected.|The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently realizes they had provided an incorrect amount.|
|CURR|Incorrect<br>Currency|Currency of the payment is incorrect.|The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently realizes they requested the wrong currency, as the<br>payment has been executed. They request their bank to recall<br>the funds so that the payment can be re-executed in the correct currency|
|CUST|Requested By<br>Customer|Cancellation requested by the Debtor.|The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently wishes to recall the payment. The exactly<br>underlying reason for the customer request is either not specified by the<br>customer or is not aligned to a more specific reason and therefore is not<br>appropriate.|

---

<!-- ELEMENT 791 -->
Definitions and High Level Use Cases 

## **(continued)** 

|**Code**|**Name**|**Definition**|**Use Case**|
|---|---|---|---|
|CUTA|Cancel Upon<br>Unable To Apply|Cancellation requested because an investigation<br>request has been received and no remediation is<br>possible.|An error occurred in the original payment (such as incorrect<br>information) which was highlighted as part of an Investigation<br>query. The request to cancel complements a response to the<br>Investigation.|
|DUPL|Duplicate<br>Payment|Payment is a duplicate of another payment.|A customer (Debtor) requests the initiation of a payment from<br>their bank account, but subsequently initiates<br>a new (separate) payment request in duplication of a previous<br>payment. Having realized the error, the customer requests the<br>recall of the duplicate transaction.|
|FRAD|Fraudulent Origin|Cancellation requested following a transaction that was<br>originated fraudulently. The use of the Fraudulent<br>Origin code should be governed by jurisdictions.|Either the customer (Debtor) or a bank (Agent) in the payment<br>transaction experiences an activity which causes a payment to<br>be executed by alleged fraudulent means.|
|NARR|Narrative|Narrative reason provided in the Additional Information.|Used only where a more specific reason is not appropriate.<br>Narrative description is provided.|
|TECH|Technical<br>Problem|Cancellation requested following technical problems<br>resulting in an erroneous transaction.|Either the customer (Debtor) or a bank (Agent) in the payment<br>flow experiences a technology issue which causes data within<br>a payment to be incorrect.|
|UPAY|Undue Payment|Payment is not justified.|Either the customer (Debtor) or a bank (Agent) in the payment<br>flow experiences an activity which causes a<br>payment to be executed under unexpected circumstances.|

---

<!-- ELEMENT 792 -->
Use case should be considered as a principal example whereby use case may be cross referenced 

**Payment Cancellation Request** Use Case c.55.1.1 –

---

<!-- ELEMENT 793 -->
In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collections of funds from the debtor's accounts for a creditor. 

**==> picture [758 x 237] intentionally omitted <==**

**----- Start of picture text -----**<br>
Interbank pain.008 pain.008<br>camt.053 pacs.003<br>B A Interbank pain.002 F pain.002<br>camt.056 3 camt.055 2 camt.055 1<br>camt.029 camt.029 camt.029<br>1 2 3<br>Forwarding Agent (F) assigns<br>Creditor request the recall a  Creditor Agent (A) assigns a<br>a Customer Cancellation<br>previous instructed Direct  Cancellation Request to Agent B<br>Request to Agent A<br>Debit collection, as the amount  (assignee) requesting the original<br>(assignee) requesting the<br>was incorrect. pacs.003 is cancelled, using<br>original pain.008 is cancelled,  reason code AM09.<br>using reason code AM09.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 794 -->
## **Payment Market Infrastructure** 

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collection of funds from the debtor's accounts for a creditor (through a Payment Market Infrastructure). 

**==> picture [61 x 60] intentionally omitted <==**

**==> picture [701 x 253] intentionally omitted <==**

**----- Start of picture text -----**<br>
Interbank pain.008 pain.008<br>pacs.003 pacs.003<br>B A Interbank pain.002 F pain.002<br>camt.056 3 camt.055 2 camt.055 1<br>camt.029 camt.029 camt.029<br>1 2 3<br>Forwarding Agent (F) assigns<br>Creditor request the recall a  Creditor Agent (A) assigns a<br>a Customer Cancellation<br>previous instructed Direct  Cancellation Request to Agent B<br>Request to Agent A<br>Debit collection, as the amount  (assignee) requesting the original<br>(assignee) requesting the<br>was incorrect. pacs.003 is cancelled, using<br>original pain.008 is cancelled,  reason code AM09.<br>using reason code AM09.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 795 -->
# **Financial Institution to Financial Institution Payment Cancellation Request** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 796 -->
**==> picture [186 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.056<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Assignment<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Underlying<br>**----- End of picture text -----**<br>


The FI to FI Payment Cancellation Request message is sent by an Agent to request the Cancellation of a payment previous sent. 

The message is sent either: 

- directly (through the SWIFT Community CASE solution), or 

- • serially through other agents. 

It is not recommended to request a Payment Cancellation Request (camt.056) of a Payment Return (pacs.004) instead an Exception and 

**==> picture [60 x 59] intentionally omitted <==**

---

<!-- ELEMENT 797 -->
**==> picture [851 x 372] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pacs.008<br>pacs.002<br>pacs.008<br>camt.055<br>camt.053<br>camt.056<br>camt.056<br>camt.029<br>camt.029<br>The FIToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This<br>message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The<br>FIToFIPaymentCancellationRequest message is exchanged between the payment Instructing Agent and the Instructed<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 798 -->
**==> picture [851 x 372] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>pacs.008<br>pacs.002<br>pacs.008<br>camt.055<br>camt.053<br>camt.056<br>camt.029<br>The FIToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This<br>message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The<br>FIToFIPaymentCancellationRequest message is exchanged between the payment Instructing Agent and the Instructed<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 799 -->
The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview. 

**==> picture [385 x 116] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cancel & return<br>my payment<br>please CASE123<br>CASEABC<br>STATYXZ STAT789<br>Customer X<br>ISO<br>Camt.056 Payment Cancellation Request<br>**----- End of picture text -----**<br>


**==> picture [316 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
OK, I can<br>understand the<br>mistake.<br>CASE545<br>STAT54X<br>Customer Y<br>ISO<br>camt.029 Resolution of Investigation<br>**----- End of picture text -----**<br>


|**element**|**description**|**example**||**element**|**description**|**example**|
|---|---|---|---|---|---|---|
|Assigner|Sender of the camt.056|Agent B||Assigner|Sender of the camt.029|Agent C|
|Assignee|Receiver of the camt.056|Agent C||Assignee|Receiver of the camt.029|Agent B|
|Assignment<br>Identification|Unique Id generated by the assigner<br>to identify the Payment Cancellation<br>Request message|CASE123/1||Assignment<br>Identification|Unique Id generated by the assigner<br>to identify the Resolution of<br>Investigation message|STAT789/1|
|Cancellation<br>identification|<br>Optional Cancellation Id of the Agent<br>sending (assigner) the Payment<br>Cancellation Request message.|**CASE123**||Cancellation<br>Status<br>Identification|<br>Case Reference of the Agent<br>sending (assigner) the Resolution of<br>Investigation message.|**STAT789**|
|Case<br>Identification|<br>Case Id of the Agent sending<br>(assigner) the Payment Cancellation<br>Request message.|**CASE123**||Resolved<br>(Original) Case<br>Identification|<br>Case Id of the original case the<br>Resolution of Investigation is<br>responding to.|**CASE123**|



**==> picture [33 x 62] intentionally omitted <==**

---

<!-- ELEMENT 801 -->
## **Min 1 – Max 1** 

The Payment Cancellation Request message _**Identification**_ provides a mandatory element to identify the Request 

**==> picture [90 x 58] intentionally omitted <==**

Unique reference assigned by the assigner to unambiguously identify the Cancellation request. For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison. 

Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message. 

**==> picture [10 x 6] intentionally omitted <==**

---

<!-- ELEMENT 802 -->
**==> picture [807 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>pacs.008<br>camt.056<br>pacs.008 Assigner  and  Assignee  represent the<br>camt.029<br>camt.056 Agents involved in the point-to-point<br>Assigner  Assignee investigation message exchange. These<br>camt.029<br>Agent: Agent A Agent: Agent B roles therefore change on each message<br>leg.<br>Assigner Assignee<br>Agent: Agent B Agent: Agent C<br>**----- End of picture text -----**<br>


_Assignment_ 

**==> picture [10 x 11] intentionally omitted <==**

**==> picture [11 x 10] intentionally omitted <==**

---

<!-- ELEMENT 803 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 805 -->
## **Min 0 – Max 1** 

The Payment Cancellation Request message _**Cancellation Identification**_ provides an optional element to identify the Request 

**==> picture [90 x 58] intentionally omitted <==**

**----- Start of picture text -----**<br>
!<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

Unique reference assigned by the assigner to unambiguously identify the Cancellation request. 

For Exceptions and Investigations messages the _Cancellation Identification_ can be considered an equivalent in the legacy MT Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message. 

Where Cancellation Identification is used this should represent the reference value as the Case Identification 

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [11 x 6] intentionally omitted <==**

_Underlying Transaction Information_

---

<!-- ELEMENT 806 -->
**Min 1 – Max 1** 

The Payment Cancellation Request message _**Case**_ provides a mandatory nested element to identify the Case _**Identification**_ and the _**Creator**_ of the case. 

## **Min 1 – Max 1** 

The _**Identification**_ element captures a unique case reference assigned by the assigner to unambiguously identify the Cancellation investigation case. 

**==> picture [90 x 75] intentionally omitted <==**

**----- Start of picture text -----**<br>
id<br>**----- End of picture text -----**<br>


For Exceptions and Investigations messages the _Case Identification_ can be considered an equivalent of the _Transaction Reference Number_ (Field 20) of the legacy MT Request for Cancellation message. 

**Min 1 – Max 1** 

The _**Creator**_ element captures the party who created the investigation. This mandatory party can represent as either an _**Agent**_ i.e., the Bank who created the case or as a _**Party**_ i.e., the customer (for example the Debtor) who created the request. In CBPR+ the creator is always expected to be an Agent. This element has no equivalent in the legacy MT Request for Cancellation message. 

**==> picture [10 x 10] intentionally omitted <==**

**==> picture [11 x 11] intentionally omitted <==**

**==> picture [11 x 6] intentionally omitted <==**

_Transaction Information_ 

_Underlying_

---

<!-- ELEMENT 807 -->
## **Min 1 – Max 1** 

The Payment Cancellation Request uses elements in the _**Original Group Information**_ to capture the identifier and name of the for which the Cancellation is message message underlying payment being requested. The mandatory _**Original Message Identification**_ contains the point-to-point reference from this payment, and the mandatory _**Original Message Name Identification**_ contains the message name of the underlying payment. Optionally the _**Original Creation Date Time**_ can also be captured. 

**==> picture [350 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>confirms the<br>pacs.008<br>Financial Message<br>abcd1234<br>Identification<br>Institution<br>camt.029<br>camt.056<br>Assignment Identification xyz9875<br>Original Message<br>Original  abcd1234<br>Identification<br>Underlying Group<br>**----- End of picture text -----**<br>


For example: 

_Original Message Name Identification_ “pacs.008.001.08” confirms the Cancellation request is for a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as “pacs.009.001.08” confirms the Cancellation request for a pacs.009 Financial Institution Credit Transfer. 

**==> picture [35 x 34] intentionally omitted <==**

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 808 -->
The Payment Cancellation Request also uses a number of other **Original** elements in the _**Transaction Information**_ to capture information from the underlying payment that the Cancellation request relates to. 

**==> picture [58 x 62] intentionally omitted <==**

The Original elements enables the _**Assignee**_ to identify the Payment which is being request to be cancelled. The following element (in addition to _Original Message identification_ and _Original Message Name Identification_ described on the previous page) are mandated: _**Original End to End Identification**_ **Min 1 – Max 1** _**Original UETR**_ **Min 1 – Max 1** _**Original Interbank Settlement Amount**_ **Min 1 – Max 1** _**Original Interbank Settlement Date**_ **Min 1 – Max 1** 

The following element (in addition to _Original Message identification_ and _Original Message Name Identification_ described on the previous page) are optional: _**Original Instruction Identification**_ **Min 0 – Max 1** _Underlying Transaction Information_ _**Original Transaction Identification**_ **Min 0 – Max 1** _Original Instruction Identification Original End to End Identification_ _**Original Clearing System Reference**_ **Min 0 – Max 1** 

_Underlying Transaction Information Original Instruction Identification Original End to End Identification Original Transaction Original UETR Original Clearing System Reference Original Interbank Settlement Amount_

---

<!-- ELEMENT 809 -->
**Min 1 – Max 1** 

The Payment Cancellation Request _**Cancellation Reason Information**_ nested element captures information associated with the reason for the Cancellation request. 

**Min 0 – Max 1** 

## ? 

the _**Originator**_ element helps identify the party who request the payment Cancellation. This party would have been included in the underlying payment and is also included the pacs.004 _Return Chain as the Creditor._ **Min 1 – Max 1** the _**Reason**_ is mandatory and represented by an embedded CBPR+ Cancellation _**Code**_ choice ( ) **Min 0 – Max 2** the _**Additional Information**_ element also be included to further details on the may provide Cancellation reason. Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request. 

_Underlying Transaction Information     Cancellation Reason Info’_ to _Originator_ 

In the event that the case assigner wishes it indicate a willingness to 

**==> picture [18 x 11] intentionally omitted <==**

---

<!-- ELEMENT 810 -->
Definitions and High Level Use Cases 

**Min 1 – Max 1** 

The Payment Cancellation Request _**Reason**_ element is mandatory. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded _**Code**_ choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened after the coexistence period. 

|**Code**|**Name**|**Definition**|**Use Case**|
|---|---|---|---|
|AGNT|Incorrect Agent|Agent in the payment workflow is<br>incorrect.|A payment previous executed is identified as containing an incorrect<br>correspondent (Agent) within the payment flow. A Cancellation request is<br>generated so that the payment can be remediated following the successful<br>return.|
|AM09|Wrong Amount|Amount is not the amount agreed or<br>expected.|The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently realizes they had provided an incorrect amount.|
|COVR|Cover Cancelled<br>Or Returned|Cover payments has either been<br>returned or cancelled.|Identifies an Agent to request the Cancellation of a pacs message where<br>settlement method was COVE and the covering payment has been cancelled<br>or returned.|
|CURR|Incorrect<br>Currency|Currency of the payment is incorrect.|The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently realizes they requested the wrong currency, as the<br>payment has been executed. They request their bank to recall<br>the funds so that the payment can be re-executed in the correct currency|

---

<!-- ELEMENT 811 -->
Definitions and High Level Use Cases 

## **(continued)** 

|**Code**|**Name**|**Definition**|**Use Case**|
|---|---|---|---|
|CUTA|Cancel Upon<br>Unable To Apply|Cancellation requested because an investigation<br>request has been received and no remediation is<br>possible.|An error occurred in the original payment (such as incorrect<br>information) which was highlighted as part of an Investigation<br>query. The request to cancel complements a response to the<br>Investigation.|
|DUPL|Duplicate<br>Payment|Payment is a duplicate of another payment.|A customer (Debtor) requests the initiation of a payment from<br>their bank account, but subsequently initiates<br>a new (separate) payment request in duplication of a previous<br>payment. Having realized the error, the customer requests the<br>recall of the duplicate transaction.|
|FRAD|Fraudulent Origin|Cancellation requested following a transaction that was<br>originated fraudulently. The use of the Fraudulent<br>Origin code should be governed by jurisdictions.|Either the customer (Debtor) or a bank (Agent) in the payment<br>transaction experiences an activity which causes a payment to<br>be executed by alleged fraudulent means.|
|NARR|Narrative|Narrative reason provided in the Additional Information.|Used only where a more specific reason is not appropriate.<br>Narrative description is provided.|
|TECH|Technical<br>Problem|Cancellation requested following technical problems<br>resulting in an erroneous transaction.|Either the customer (Debtor) or a bank (Agent) in the payment<br>flow experiences a technology issue which causes data within<br>a payment to be incorrect.|
|UPAY|Undue Payment|Payment is not justified.|Either the customer (Debtor) or a bank (Agent) in the payment<br>flow experiences an activity which causes a<br>payment to be executed under unexpected circumstances.|

---

<!-- ELEMENT 812 -->
Use case should be considered as a principal example whereby use case may be cross referenced 

## **Payment Cancellation Request** 

Use Case c.56.1.1 – High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008) Use Case c.56.1.1.a  – High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.56.1.2 – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008) Use Case c.56.1.2.a – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.56.2.1 – High Level Payment Cancellation Request (camt.056) of a complete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.56.2.2 – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.56.2.3 – High Level Payment Cancellation Request (camt.056) of a Customer Credit Transfers (pacs.008) where the cover is returned Use Case c.56.3.1 – High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer (pacs.009) Use Case c.56.4.1 – High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer advice (pacs.009 adv)

---

<!-- ELEMENT 813 -->
## **Credit Transfer (pacs.008)** 

**==> picture [822 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
See use case p.8.1.1 for the original payment,<br>c.29.1.1 for case resolution and p.4.1.3. for an<br>example payment return<br>pacs.008 pacs.008 pacs.008 pacs.008<br>A camt.056 camt.056 C camt.056<br>B D<br>1 2 camt.029 3 camt.029 4 camt.029 5<br>**----- End of picture text -----**<br>


**==> picture [429 x 166] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 3<br>Debtor request their bank to  Agent B creates an investigation case.<br>recall a previous instructed  Recognising the payment has already<br>payment, as the amount was  been onward processed. They update<br>incorrect. Agent A and assign a Cancellation<br>Request directly to Agent C.<br>2<br>4<br>Debtor Agent (A) assigns a  Agent C creates an investigation case.<br>Cancellation Request to Agent  Recognising the payment has already<br>B (assignee) requesting the  been onward processed. They update<br>original pacs 008 is returned Agent B and assign a Cancellation<br>**----- End of picture text -----**<br>


5 Agent D creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, providing the reason specified for the return request and updates Agent C. Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed any necessary return payment is arrange.

---

<!-- ELEMENT 814 -->
## **Credit Transfer (pacs.008) using gpi Stop and Recall** 

**==> picture [823 x 344] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.056<br>2 camt.056 3 4<br>camt.029<br>camt.029<br>pacs.008 pacs.008 pacs.008 pacs.008<br>A B C D<br>1<br>See use case p.8.1.1 for the original payment,<br>c.29.1.1 for case resolution and p.4.1.3. for an<br>example payment return<br>1 3 4<br>Debtor request their bank to  gpi Tracker identifies the payment is  Agent D creates an investigation case.<br>recall a previous instructed  complete and forwards a camt.056 to  Recognising the payment has already been<br>payment, as the amount was  Agent D. credited to the creditor. They request debit<br>incorrect.<br>authority, providing the reason specified for<br>the return request and updates the gpi<br>Tracker.<br>2 Once the outcome to the debit authorisation is<br>Debtor Agent (A) initiates a gpi know a final resolution to the investigation can<br>Stop and Recall, requesting be provided and any necessary return<br>the original pacs.008 is  payment is arrange.<br>returned using reason code<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 815 -->
## **Credit Transfer (pacs.008)** 

**==> picture [822 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
See use case p.8.1.1 for the original payment,<br>c.29.1.2 for case resolution and p.4.1.3. for an<br>example payment return<br>pacs.008 pacs.008 pacs.008<br>camt.056 camt.056<br>A C<br>B D<br>1 2 camt.029 3 camt.029 4<br>**----- End of picture text -----**<br>


**==> picture [429 x 106] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 3<br>Debtor request their bank to  Agent B creates an investigation case.<br>recall a previous instructed  Recognising the payment has already<br>payment, as the amount was  been onward processed. They update<br>incorrect. Agent A and assign a Cancellation<br>Request directly to Agent C.<br>**----- End of picture text -----**<br>


2 Debtor Agent (A) assigns a Cancellation Request to Agent B (assignee) requesting the 

**==> picture [223 x 102] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>Agent C creates an investigation case.<br>Recognising the payment has not been<br>onward processed. They update Agent<br>B that the Cancellation Request is<br>accepted any necessary return<br>payment is arrange.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 816 -->
## **Credit Transfer (pacs.008) using gpi Stop and Recall** 

**==> picture [722 x 133] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.056<br>camt.056 3<br>2<br>camt.029 4<br>camt.029<br>pacs.008 pacs.008 pacs.008<br>A B C D<br>1<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

**==> picture [429 x 77] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 3<br>Debtor request their bank to  gpi Tracker identifies the payment is<br>recall a previous instructed  incomplete and forwards a camt.056 to<br>payment, as the amount was  Agent C.<br>incorrect.<br>**----- End of picture text -----**<br>


**==> picture [255 x 80] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>Agent C creates an investigation case.<br>Recognising the payment has not been onward<br>processed. They updates the gpi Tracker any<br>necessary return payment is arrange.<br>**----- End of picture text -----**<br>


2 Debtor Agent (A) initiates a gpi Stop and Recall, requesting the original pacs.008 is

---

<!-- ELEMENT 817 -->
## **Transfer (pacs.008) settled using a cover method.** 

**==> picture [798 x 344] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.008<br>A 2 camt.056 D 3<br>1<br>camt.029<br>pacs.009 cov pacs.009 cov<br>B pacs.002 C<br>See use case p.8.2.1 for the original payment,<br>Settlement  c.29.2.1 for case resolution and p.4.3.2 for an<br>Complete example payment return<br>1 2 3<br>Debtor request their bank to  Debtor Agent (A) assigns a  Agent D creates an investigation case. Recognising the<br>recall a previous instructed  Cancellation Request to Agent  payment has already been credited to the creditor. They request<br>payment, as the amount was  D (assignee) requesting the  debit authority, proving the reason specified for the return<br>incorrect. request and update Agent A.<br>original pacs.008 is returned,<br>Once the outcome to the debit authorisation is know a final<br>using reason code AM09.<br>resolution to the investigation can be relayed and any necessary<br>t t b i iti t d<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 818 -->
## **Credit Transfer (pacs.008) settled using a cover method.** 

**==> picture [798 x 329] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.008<br>A 2 camt.056 D 3<br>1<br>camt.029<br>pacs.009 cov pacs.009 cov<br>B pacs.002 C<br>See use case p.8.2.1 for the original payment,<br>Settlement  c.29.2.1 for case resolution and p.4.3.2 for an<br>Complete example payment return<br>1 2 3<br>Debtor request their bank to  Debtor Agent (A) assigns a  Agent D creates an investigation case. Recognising the<br>recall a previous instructed  Cancellation Request to Agent  payment has not been credited to the creditor. They update<br>payment, as the amount was  D (assignee) requesting the  Agent A that the Cancellation Request is accepted and arrange<br>incorrect. the necessary return payment once the pacs.009 cov settlement<br>original pacs.008 is returned,<br>is confirmed by Agent C<br>using reason code AM09.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 819 -->
## **Transfers (pacs.008) where the cover is returned** 

**==> picture [807 x 347] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.008<br>A 1 camt.056 D<br>camt.029<br>2<br>pacs.009 cov<br>+ Return<br>pacs.002<br>Reason  B C<br>See use case p.8.2.1 for the cover payment sample<br>+ Reject<br>c.29.2.2 for case resolution and p.4.3.3 for payment<br>Reason  return<br>2<br>1<br>Agent D creates an investigation case. Recognising the<br>Debtor Agent (A) assigns a<br>Agent C receives the payment and  cover payment will not be received to settle the pacs.008.<br>Cancellation Request to Agent D<br>recognises the payment can not be  As the creditor has not been credited in advance of cover<br>(assignee) requesting the original<br>completed as requested e.g. the Agent D  settlement, a final resolution to the investigation can be<br>pacs.008 is considered null and<br>does not maintain an account with them.  provided. A payment return is not necessary.<br>void, using reason code COVR.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 820 -->
## **Institution Credit Transfer (pacs.009)** 

**==> picture [739 x 166] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 pacs.009<br>pacs.009 camt.053<br>A pacs.002 B pacs.002 C camt.054 D<br>1 camt.056 2 camt.056 3<br>camt.029 camt.029<br>See use case p.9.1.1 for the cover payment sample<br>c.29.3.1 for case resolution and p.4.2.3 for payment<br>return<br>**----- End of picture text -----**<br>


**==> picture [177 x 77] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>Debtor request their bank to<br>recall a previous instructed<br>payment, as the amount was<br>incorrect.<br>**----- End of picture text -----**<br>


2 Debtor Agent (A) assigns a Cancellation Request to Agent C (assignee) requesting the original pacs.009 is returned, using reason code AM09. 

3 Agent C creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, proving the reason specified for the return request and update Agent C. 

Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed and

---

<!-- ELEMENT 821 -->
## **Credit Transfer advice (pacs.009 adv)** 

**==> picture [790 x 339] intentionally omitted <==**

**----- Start of picture text -----**<br>
pacs.009 (ADV) camt.054<br>A B 2 camt.056 E F<br>1 camt.029 3<br>pacs.009<br>C pacs.002<br>D<br>See use case p.9.1.2 for the cover payment sample<br>c.29.4.1 for case resolution and p.4.2.3 for payment<br>return<br>1 2 3<br>Debtor request their bank to  Debtor Agent (A) assigns a  Agent E creates an investigation case. Recognising the payment<br>recall a previous instructed  Cancellation Request to Agent  has already been credited to the creditor. They request debit<br>payment, as the amount was  E (assignee) requesting the  authority, proving the reason specified for the return request and<br>incorrect. update Agent B.<br>original pacs.008 is returned,<br>Once the outcome to the debit authorisation is know a final<br>using reason code AM09.<br>**----- End of picture text -----**<br>


See use case p.9.1.2 for the cover payment sample c.29.4.1 for case resolution and p.4.2.3 for payment return 

Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed and any necessary

---

<!-- ELEMENT 822 -->
**camt.107 – Cheque Presentment Notification camt.108 - Cheque Cancellation or Stop Request camt.109 – Cheque Cancellation or Stop Report**

---

<!-- ELEMENT 823 -->
# **Cheque Presentment Notification** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 824 -->
**==> picture [186 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.107<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cheque<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

The ChequePresentmentNotificationmessage is sent by a drawer bank, or a bank acting on behalf of the drawer bank to the bank on which a cheque has been drawn (the drawee bank). 

It is used to advise the drawee bank, or confirm to an enquiring bank, the details concerning the cheque referred to in the message. 

The Cheque Presentment Notification is restricted to a single cheque per InterAct message.

---

<!-- ELEMENT 825 -->
**==> picture [409 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>B<br>Drawer Agent Drawee Agent<br>camt.107<br>**----- End of picture text -----**<br>


The Agent A (drawer agent) sends a ChequePresentmentNotification message to Agent B (the drawee agent). The ChequePresentmentNotification message informs the drawee agent about the cheque submission. The notification message facilitates the drawee agent to follow up the cheque submission and relevant business process.

---

<!-- ELEMENT 827 -->
**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 cash management message has a _Message Identification_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Cash Management (camt) messages the _Message Identification_ has no exact equivalent in the legacy MT Advice of Cheque message. However, the _Sender’s Reference_ (Field 20) could be considered a similar comparison. 

_Group Header_ Message Identification

---

<!-- ELEMENT 828 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 829 -->
**==> picture [94 x 83] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>**----- End of picture text -----**<br>


The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1. 

_Group Header_ Number Of Cheques

---

<!-- ELEMENT 831 -->
## **Min 1 – Max 1** 

The Cheque Presentment Notification _**Cheque**_ nested element specifies the details of the Cheque. 

**==> picture [80 x 42] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>**----- End of picture text -----**<br>


This Cheque element has been restricted to one cheque occurrence. 

**==> picture [10 x 10] intentionally omitted <==**

_Cheque_

---

<!-- ELEMENT 832 -->
**Min 1 – Max 1** The Cheque Presentment Notification _**Instruction Identification**_ provides an optional element to identify unambiguously the instruction 

**==> picture [89 x 57] intentionally omitted <==**

Point to point reference that can be used between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving this message) to refer to the individual instruction. 

_Cheque                Instruction Identification_

---

<!-- ELEMENT 833 -->
## **Min 1 – Max 1** 

The Cheque Number Notification _**Cheque Number**_ provides a mandatory element to identify unambiguously the Cheque. 

**==> picture [102 x 121] intentionally omitted <==**

Unique and unambiguous number for a cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque 

_Cheque                Cheque Number_

---

<!-- ELEMENT 834 -->
The Cheque Presentment Notification has several element to capture a Date related to the cheque. 

**10** 

**Min 1 – Max 1** The _**Issue Date**_ is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer 

**Min 0 – Max 1** 

**10** 

The _**Stale Date**_ is element and the date after which a is no an optional represents cheque longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days” or may be determined in accordance with domestic banking practice. Not all countries will have a validity period. 

**==> picture [12 x 10] intentionally omitted <==**

_Cheque_

---

<!-- ELEMENT 835 -->
**Min 1 – Max 1 £ $** A mandated **Amount** of the currency cheque to be paid to the payee. ¥ 

**Min 0 – Max 1** 

**10** 

The _**Value Date**_ is an optional element, it is used to capture the **Date** , where different to the **Issue Date** , i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account. 

_Cheque_ 

**==> picture [12 x 10] intentionally omitted <==**

**==> picture [29 x 13] intentionally omitted <==**

**==> picture [13 x 10] intentionally omitted <==**

_Amount_

---

<!-- ELEMENT 836 -->
## **Min 1 – Max 1** 

The Cheque Presentment Notification _**Payer**_ captures the party that instructs the Drawee Agent to issues a cheque to pay a specific amount, upon presentment, to the payee. The Payer sub-element describe the Payer in greater detail. 

Mandatory _**Name**_ 

_**Name**_ 

**==> picture [198 x 283] intentionally omitted <==**

**==> picture [254 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Payer<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Payer_ address details 

**==> picture [92 x 90] intentionally omitted <==**

**----- Start of picture text -----**<br>
Identification<br>**----- End of picture text -----**<br>


Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

Optional element to _**Country of**_ capture the Payee’s ISO _**Residence**_

---

<!-- ELEMENT 837 -->
**Min 0 – Max 1** 

The Cheque Presentment Notification _**Payer Account**_ is used to capture the account of the party that instructs the Drawee Agent to issues a cheque to pay a specific amount, upon presentment, to the payee. 

The _**Payer Account**_ uses a variety of nested elements to capture information related to the account. 

**==> picture [65 x 71] intentionally omitted <==**

**Min 0  – Max 1** _**Identification**_ identifies the account maintained at the Drawer Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Type**_ uses the external Cash Account Type code list to identify the type of account **Min 0 – Max 1** _**Currency**_ identifies the currency of the account **Min 0 – Max 1** _**Name**_ identifies the name of the account as assigned by the Drawer Agent (Account Servicing Institution) 

**Min 0 – Max 1** _**Proxy**_ captures an alternative identification of the account number such as an email address. This element has further nested _**Type**_ which is a choice of external code list or proprietary code and _**Identification**_ which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 838 -->
## **Min 0 – Max 1** 

The Cheque Presentment Notification _**Drawer Agent**_ optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification is sent to the _**Drawee Agent**_ . 

**Min 0 – Max 1** The _**Drawer Agent Account**_ optionally captures the Drawer Agent’s Account with the _**Drawee Agent**_ and who would receive an order the pay the cheque upon presentment. 

**==> picture [158 x 86] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>DRAWEE AGENT ID<br>DRAWER AGENT ACCOUNT 1234<br>**----- End of picture text -----**<br>


**==> picture [61 x 62] intentionally omitted <==**

The Drawer Bank is typically identified on the cheque together with their Postal Address. The Drawer Agent’s Account with the Drawee Agent is also often also identified on the cheque. 

**==> picture [13 x 10] intentionally omitted <==**

_Cheque_ 

_Drawer Agent_

---

<!-- ELEMENT 839 -->
## **Min 1 – Max 1** 

The Cheque Presentment Notification _**Payee**_ captures the party that should receive an amount of money as specified in the cheque. The Payee sub-element describe the Payee in greater detail. 

Mandatory _**Name**_ 

_**Name**_ 

**==> picture [198 x 295] intentionally omitted <==**

**==> picture [279 x 211] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Payee<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Payee_ address details 

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

Optional element to _**Country of**_ capture the Payee’s ISO _**Residence**_

---

<!-- ELEMENT 840 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

**Serial Financial Institution to Financial Institution to Customer Credit Transfer** Use Case c.107.1 – High Level Drawer Agent Cheque issuance to Payee, on their account with the Drawer Agent Use Case c.107.2 - High Level Drawer Agent Cheque issuance to Payee, on their head office’s account with the Drawer Agent

---

<!-- ELEMENT 841 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
Drawee Agent<br>1<br>2a 12,000<br>A<br>4<br>2b<br>Payer Drawer Payee<br>12,000<br>3 6<br>1 5<br>Payer instructs the Drawer<br>Agent to issue a cheque to the<br>Payee<br>B C<br>2a Drawee<br>Drawer Agent (A) issues a  4<br>6<br>cheque to the Payee drawn of  Payee received the cheque and<br>their account at the Drawee  Drawee Agent (B) receives the<br>present it to their bank (Agent C)<br>Agent (B)  cheque presentment via the cheque<br>3 clearing. They validate the<br>2b The Drawee Agent (B) receives  presented cheque details again the<br>In parallel the Drawer Agent (A)  the Cheque Presentment  5 information received on the Cheque<br>initiates a Cheque Presentment  Notification and store the  Agent C receives the cheque  Presentment Notification to<br>Notification to the Drawee Agent  information in anticipation for  deposit and present it into the  conclude whether the cheque can<br>(B) the cheque to be presented domestic cheque clearing be settled.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 842 -->
## **account with the Drawee Agent** 

**==> picture [808 x 348] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2a 12,000<br>A<br>4<br>2b<br>Payee<br>Payer<br>HO 12,000<br>Drawer<br>3 6<br>1 5<br>Payer instructs their Bank<br>(Agent A) to issue a cheque to<br>the Payer<br>B C<br>2a Drawee<br>Agent (A) issues a cheque to the  4 6<br>Payee received the cheque and<br>Payee drawn of their head<br>office’s (HO) account at the  present it to their bank (Agent C) Drawee Agent (B) receives the<br>Drawer Agent (B)  3 cheque presentment via the cheque<br>clearing. They validate the<br>2b The Drawee Agent (B) receives  5 presented cheque details again the<br>the Cheque Presentment  information received on the Cheque<br>In parallel the Agent (A) initiates  Notification and store the  Agent C receives the cheque<br>Presentment Notification to<br>a Cheque Presentment  information in anticipation for  deposit and present it into the  conclude whether the cheque can<br>Notification to the Drawee Agent  domestic cheque clearing<br>the cheque to be presented be settled.<br>(B)<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 843 -->
# **Cheque Cancellation or Stop Request** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 844 -->
**==> picture [186 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.108<br>**----- End of picture text -----**<br>


The Cheque Cancellation Or Stop Request message is sent by a drawer bank, or a bank acting on behalf of the drawer bank, to the agent on which a cheque has been drawn (the drawee bank) to request for the cancellation of the presentment and/or stop the payment of the cheque referred to in the message. 

**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cheque<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

The Cheque Cancelation or Stop Report is restricted to a single cheque per InterAct message.

---

<!-- ELEMENT 845 -->
**==> picture [409 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>B<br>Drawer Agent Drawee Agent<br>camt.107<br>camt.108<br>camt.109<br>**----- End of picture text -----**<br>


The Agent A (Drawer Agent) sends a ChequeCancelationOrStopRequest message to Agent B (the Drawee Agent). The ChequeCancelationOrStopReques message requests the drawee agent to place a stop (refusal to settle) upon presentment of the cheque, effectively canceling the issued cheque.

---

<!-- ELEMENT 847 -->
**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 cash management message has a _Message Identification_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Cash Management (camt) messages the _Message Identification_ has no exact equivalent in the legacy MT Advice of Cheque message. However, the _Sender’s Reference_ (Field 20) could be considered a similar comparison. 

_Group Header_ Message Identification

---

<!-- ELEMENT 848 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 849 -->
**==> picture [94 x 83] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>**----- End of picture text -----**<br>


The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1. 

_Group Header_ Number Of Cheques

---

<!-- ELEMENT 851 -->
## **Min 1 – Max 1** 

The Cheque Cancellation or Stop Request _**Cheque**_ nested element specifies the details of the Cheque. 

**==> picture [80 x 42] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>**----- End of picture text -----**<br>


This Cheque element has been restricted to one cheque occurrence. 

**==> picture [10 x 10] intentionally omitted <==**

_Cheque_

---

<!-- ELEMENT 852 -->
**Min 0 – Max 1** The Cheque Cancellation or Stop Request _**Instruction Identification**_ provides an optional element to identify unambiguously the instruction 

**==> picture [89 x 57] intentionally omitted <==**

Point to point reference that can be used between the Agent instructing the Cheque Cancellation or Stop Request and the Drawee Agent (Agent receiving this message) to refer to the individual instruction. 

_Cheque                Instruction Identification_

---

<!-- ELEMENT 853 -->
## **Min 1 – Max 1** 

The Cheque Cancellation or Stop Request _**Original Instruction Identification**_ provides an optional element to identify unambiguously the original instruction 

**==> picture [89 x 58] intentionally omitted <==**

Point to point reference that can be used to identify the original Cheque Presentment Notification between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving this message) to refer to the individual instruction. 

_Cheque            Original Instruction Identification_

---

<!-- ELEMENT 854 -->
## **Min 1 – Max 1** 

The Cheque Cancellation or Stop Request _**Cheque Number**_ provides a mandatory element to identify unambiguously the Cheque. 

**==> picture [102 x 121] intentionally omitted <==**

Unique and unambiguous number for the cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque 

_Cheque                Cheque Number_

---

<!-- ELEMENT 855 -->
The Cheque Cancellation or Stop Request has several element to capture a Date related to the cheque. 

**10** 

**Min 1 – Max 1** The _**Issue Date**_ is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer 

**Min 0 – Max 1** 

**10** 

The _**Stale Date**_ is element and the date after which a is no an optional represents cheque longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days” or may be determined in accordance with domestic banking practice. Not all countries will have a validity period. 

**==> picture [12 x 10] intentionally omitted <==**

_Cheque_

---

<!-- ELEMENT 856 -->
**£ $** ¥ 

**Min 1 – Max 1** 

A mandated **Amount** of the currency cheque to be paid to the payee. 

## **Min 0 – Max 1** 

**10** 

The _**Effective Date**_ is an optional element, it is used to capture the original **Value Date** (as provided in the camt.107), where different to the original **Issue Date** , i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account. 

**==> picture [12 x 10] intentionally omitted <==**

_Cheque_ 

**==> picture [13 x 10] intentionally omitted <==**

_Amount_

---

<!-- ELEMENT 857 -->
## **Min 0 – Max 1** 

The Cheque Cancellation or Stop Request _**Drawer Agent**_ optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification is sent to the _**Drawee Agent.**_ 

The _**Drawer Agent Account**_ optionally captures the Drawer Agent’s Account with the _**Drawee Agent**_ and who would receive an order the pay the cheque upon presentment. 

**==> picture [158 x 86] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>DRAWEE AGENT ID<br>DRAWER AGENT ACCOUNT 1234<br>**----- End of picture text -----**<br>


**==> picture [61 x 62] intentionally omitted <==**

The Drawer Agent and Drawer Account elements where present should match that of the original camt.107 Cheque Presentment Notification. 

**==> picture [13 x 10] intentionally omitted <==**

_Cheque_ 

_Drawer Agent_

---

<!-- ELEMENT 858 -->
**Min 0 – Max 1** 

The Cheque Cancellation or Stop Request _**Payee**_ captures the party that should receive an amount of money as specified in the cheque. The Payee sub-element describe the Payee in greater detail. 

Mandatory _**Name**_ 

_**Name**_ 

**==> picture [198 x 295] intentionally omitted <==**

**==> picture [279 x 211] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Payee<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Payee_ address details 

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

**==> picture [92 x 79] intentionally omitted <==**

**----- Start of picture text -----**<br>
Country of<br>Residence<br>**----- End of picture text -----**<br>


Optional element to capture the Payee’s ISO

---

<!-- ELEMENT 859 -->
## **Min 1 – Max 1** 

The Cheque Cancellation or Stop Request _**Cheque Cancellation or Stop Reason**_ nested element captures information Cancellation or associated with the reason for the Cheque Stop request. 

**Min 0 – Max 1** 

## ? 

the _**Originator**_ element is a embedded code choice that helps identify the party who request the cheque cancellation or stop request. Where used this party would typically be the Payer (code **PAYR** ) of the cheque. 

**Min 1 – Max 1** the _**Reason**_ is mandatory and represented by an embedded CBPR+ Cancellation _**Code**_ choice ( ) 

**Min 0 – Max 2** the _**Additional Information**_ element also be included to further details on the may provide cancellation or stop reason. 

**==> picture [35 x 32] intentionally omitted <==**

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cheque Cancellation or Stop request. 

_Cheque     Cheque Cancellation or Stop Reason_ 

**==> picture [11 x 12] intentionally omitted <==**

**==> picture [11 x 10] intentionally omitted <==**

**==> picture [18 x 11] intentionally omitted <==**

_Originator_

---

<!-- ELEMENT 860 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

**Serial Financial Institution to Financial Institution to Customer Credit Transfer** Use Case c.108.1 – High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque Use Case c.108.2 – High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.

---

<!-- ELEMENT 861 -->
**==> picture [851 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
lost cheque.<br>1<br>12,000<br>A<br>2 Drawer Payee<br>Payer<br>See use case c.109.1.1 for an example the Cheque<br>Cancellation or Stop Report<br>3 B C<br>Drawee<br>2 3<br>1<br>Drawer Agent (A) issues a  Drawee Agent (B) match the request<br>Payer instructs the Drawer<br>cheque cancellation or stop  to the previous Cheque Presentment<br>Agent they wish to cancel or<br>request to the Drawee Agent (B)  Notification (camt.107). As the<br>stop a previously issued<br>with reason code LOST cheque has not been presented the<br>cheque, as the Payee informs<br>status record is identified as not to be<br>them the cheque has been lost.<br>paid if presented, as a result of a<br>cancellation/stop request. This is<br>reported back to the Drawer Agent<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 862 -->
## **of the Payer customer.** 

**==> picture [808 x 354] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>12,000<br>A<br>Drawer<br>2 Payee<br>Payer<br>12,000<br>See use case c.109.1.2 for an example the<br>Cheque Cancellation or Stop Report<br>3 B C<br>Drawee<br>2 3<br>1<br>Drawee Agent (B) match the request<br>Drawer Agent (A) issues a<br>Payer instructs the Drawer<br>to the previous Cheque Presentment<br>cheque cancellation or stop<br>Agent they wish to cancel or  Notification (camt.107). As the<br>request to the Drawee Agent (B)<br>stop a previously issued<br>with reason code CUST cheque has already been presented<br>cheque, as the Payer informs<br>and paid the cancellation/stop<br>them they no longer wish to<br>request can not be executed. This is<br>honour the cheque. reported back to the Drawer Agent<br>(A) as rejected with additional<br>information to explain the cheque has<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 863 -->
# **Cheque Cancellation or Stop Report** 

**==> picture [851 x 175] intentionally omitted <==**

---

<!-- ELEMENT 864 -->
**==> picture [186 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
camt.109<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Group Header<br>**----- End of picture text -----**<br>


**==> picture [149 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cheque<br>**----- End of picture text -----**<br>


**==> picture [60 x 60] intentionally omitted <==**

The Cheque Cancellation or Stop Report message is sent by the drawee agent (on which a cheque is drawn) to the drawer agent, or the agent acting on behalf of the drawer agent, to indicate what actions have been taken in attempting to cancel the presentment and/or stop the payment of the cheque referred to in the message. 

The Cheque Cancelation or Stop Request is restricted to a single cheque per InterAct message.

---

<!-- ELEMENT 865 -->
**==> picture [409 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>B<br>Drawer Agent Drawee Agent<br>camt.107<br>camt.108<br>camt.109<br>**----- End of picture text -----**<br>


The Agent B (Drawee Agent) sends a ChequeCancelationOrStopReport message to Agent A (the Drawer Agent). The ChequeCancelationOrStopReport message reports the outcome of a Cheque Cancellation or Stop Request.

---

<!-- ELEMENT 867 -->
**==> picture [89 x 58] intentionally omitted <==**

Each ISO 20022 cash management message has a _Message Identification_ element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message. 

For Cash Management (camt) messages the _Message Identification_ has no exact equivalent in the legacy MT Advice of Cheque message. However, the _Sender’s Reference_ (Field 20) could be considered a similar comparison. 

_Group Header_ Message Identification

---

<!-- ELEMENT 868 -->
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC): 

**10** 

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm 

- ➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 

**==> picture [60 x 60] intentionally omitted <==**

All CBPR+ time elements need offset against UTC. Milliseconds are optional. 

_Group Header_ Creation Date Time

---

<!-- ELEMENT 869 -->
**==> picture [94 x 83] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>**----- End of picture text -----**<br>


The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1. 

_Group Header_ Number Of Cheques

---

<!-- ELEMENT 871 -->
## **Min 1 – Max 1** 

The Cheque Cancellation or Stop Report _**Cheque**_ nested element specifies the details of the Cheque. 

**==> picture [80 x 42] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>**----- End of picture text -----**<br>


This Cheque element has been restricted to one cheque occurrence. 

**==> picture [10 x 10] intentionally omitted <==**

_Cheque_

---

<!-- ELEMENT 872 -->
## **Min 0 – Max 1** 

The Cheque Cancellation or Stop Report _**Instruction Identification**_ provides an optional element to identify unambiguously the instruction 

**==> picture [89 x 57] intentionally omitted <==**

Point to point reference that can be used between the Drawee Agent providing the Cheque Cancellation or Stop Report and the Drawee Agent (Agent receiving this message) to refer to the individual instruction. 

_Cheque                Instruction Identification_

---

<!-- ELEMENT 873 -->
## **Min 1 – Max 1** 

The Cheque Cancellation or Stop Request _**Original Instruction Identification**_ provides an optional element to identify unambiguously the original instruction 

**==> picture [89 x 58] intentionally omitted <==**

Point to point reference that can be used to identify the original Cheque Cancellation or Stop Request between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving the request message) to refer to the individual request. 

_Cheque            Original Instruction Identification_

---

<!-- ELEMENT 874 -->
## **Min 1 – Max 1** 

The Cheque Cancellation or Stop Request _**Cheque Number**_ provides a mandatory element to identify unambiguously the Cheque. 

**==> picture [102 x 121] intentionally omitted <==**

Unique and unambiguous number for the cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque 

_Cheque                Cheque Number_

---

<!-- ELEMENT 875 -->
The Cheque Cancellation or Stop Report has several element to capture a Date related to the cheque. 

**10** 

**Min 1 – Max 1** The _**Issue Date**_ is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer 

**Min 0 – Max 1** 

**10** 

The _**Stale Date**_ is element and the date after which a is no an optional represents cheque longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days” or may be determined in accordance with domestic banking practice. Not all countries will have a validity period. 

**==> picture [12 x 10] intentionally omitted <==**

_Cheque_

---

<!-- ELEMENT 876 -->
**£ $** ¥ 

**Min 1 – Max 1** 

A mandated **Amount** of the currency cheque to be paid to the payee. 

## **Min 0 – Max 1** 

**10** 

The _**Effective Date**_ is an optional element, it is used to capture the original **Value Date** (as provided in the camt.107), where different to the original **Issue Date** , i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account. 

**==> picture [12 x 10] intentionally omitted <==**

_Cheque_ 

**==> picture [13 x 10] intentionally omitted <==**

_Amount_

---

<!-- ELEMENT 877 -->
## **Min 0 – Max 1** 

The Cheque Cancellation or Stop Request _**Drawer Agent**_ optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification is sent to the _**Drawee Agent.**_ 

The _**Drawer Agent Account**_ optionally captures the Drawer Agent’s Account with the _**Drawee Agent**_ and who would receive an order the pay the cheque upon presentment. 

**==> picture [158 x 86] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>DRAWEE AGENT ID<br>DRAWER AGENT ACCOUNT 1234<br>**----- End of picture text -----**<br>


**==> picture [61 x 62] intentionally omitted <==**

The Drawer Agent and Drawer Account elements where present should match that of the original camt.107 Cheque Presentment Notification. 

**==> picture [13 x 10] intentionally omitted <==**

_Cheque_ 

_Drawer Agent_

---

<!-- ELEMENT 878 -->
**Min 0 – Max 1** 

The Cheque Cancellation or Stop Request _**Payee**_ captures the party that should receive an amount of money as specified in the cheque. The Payee sub-element describe the Payee in greater detail. 

Mandatory _**Name**_ 

_**Name**_ 

**==> picture [198 x 295] intentionally omitted <==**

**==> picture [279 x 211] intentionally omitted <==**

**----- Start of picture text -----**<br>
Postal<br>Address<br>Payee<br>Identification<br>**----- End of picture text -----**<br>


Nested element capturing either structured or unstructured _Payee_ address details 

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. 

**==> picture [92 x 79] intentionally omitted <==**

**----- Start of picture text -----**<br>
Country of<br>Residence<br>**----- End of picture text -----**<br>


Optional element to capture the Payee’s ISO

---

<!-- ELEMENT 879 -->
## **Min 1 – Max 1** 

The Cheque Cancellation or Stop Request _**Cheque Cancellation or Stop Reason**_ nested element captures information Cancellation or associated with the reason for the Cheque Stop request. 

**Min 0 – Max 1** the _**Originator**_ element helps identify the party who request the cheque cancellation or stop request. Where used this party would typically be the Payer of the cheque. **Min 1 – Max 1** ! the _**Status**_ is mandatory and represented by an embedded status _**Code**_ choice ( ) REJT (Rejected) or ACCP (Accepted) 

**Min 0 – Max 2** 

the _**Additional Information**_ element also be included to further details on the may provide cancellation or stop reason. 

**==> picture [36 x 32] intentionally omitted <==**

Note where Status code REJT is used additional information must be provided to describe the reason for the rejection. 

_Cheque     Cheque Cancellation or Stop Reason Originator_ 

**==> picture [11 x 12] intentionally omitted <==**

**==> picture [18 x 11] intentionally omitted <==**

---

<!-- ELEMENT 880 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases. 

**Serial Financial Institution to Financial Institution to Customer Credit Transfer** Use Case c.109.1 – High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque Use Case c.109.2 – High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.

---

<!-- ELEMENT 881 -->
## **lost cheque.** 

**==> picture [806 x 306] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>A<br>Payer Drawer Payee<br>B C<br>1<br>Drawee<br>1<br>See use case c.108.1.1 for an example the Cheque<br>Drawee Agent (B) reports to the<br>Cancellation or Stop Request<br>Drawer Agent (A) that the Cheque<br>Cancellation or Stop request has<br>been accepted.<br>**----- End of picture text -----**<br>

---

<!-- ELEMENT 882 -->
## **the Payer customer.** 

**==> picture [657 x 327] intentionally omitted <==**

**----- Start of picture text -----**<br>
12,000<br>A<br>Payer Drawer Payee<br>12,000<br>B C<br>1<br>Drawee<br>1<br>Drawee Agent (B) reports to the<br>Drawer Agent (A) that the Cheque<br>Cancellation or Stop request has<br>been rejected. Additional Information<br>is provided to explain that the cheque<br>has already been presented and paid.<br>**----- End of picture text -----**<br>


See use case c.108.1.2 for an example the Cheque Cancellation or Stop Request

---

<!-- ELEMENT 883 -->
**==> picture [99 x 99] intentionally omitted <==**

www.swift.com

---

