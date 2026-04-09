<!-- ELEMENT ? -->
<span id="page-0-0"></span>This Cross -Border Payment Reporting plus (CBPR+) User Handbook is intended to document and explain a variety of ISO 20022 payment related topics, as well as provide practical use cases to ensure a common understanding and adoption of ISO 20022 within the payment

industry. The SWIFT FINplus service will support CBPR+ messages on the SWIFT network traditionally associated with correspondent banking (many to -many). These messages may be exchanged either between Agents in the same country or between Agents in

-

The use cases focus on a core topics where other relevant messages may also be referred to within the use case, it may also be necessary to consider other documented use cases, in order to capture a wider variation of scenarios.

# Note:

This document jointly developed with the CBPR+ group continues to evolve inline with the Standards

- Release as: CBPR+ continue to develop market practice guidelines for additional message.
- Inaccuracies are identified and corrected.
- Further use cases and/or explanation needs are identified

| Page 2<br>Page 5         | Updated –<br>note                                                                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                          | Updated –<br>new messages added to index                                                                                                                                                                   |
| Page 6                   | Updated –<br>new messages added to index                                                                                                                                                                   |
| Page 11                  | Updated –<br>correction of Intermediary code                                                                                                                                                               |
| Page 33                  | Updated –<br>new messages and Usage Ids added                                                                                                                                                              |
| Page 40                  | Updated –<br>new pain message added to index                                                                                                                                                               |
| Page 45                  | Updated –<br>recognition of Payment Initiation relay rulebook                                                                                                                                              |
| Page 107                 | Updated –<br>recognition of Payment Initiation relay rulebook                                                                                                                                              |
| Page 122                 | Updated –<br>additional use cases in the index                                                                                                                                                             |
| Page 126                 | New –use case                                                                                                                                                                                              |
| Page 134                 | New –<br>use case                                                                                                                                                                                          |
| Page 135-182             | New –<br>pain.008 message section                                                                                                                                                                          |
| Page 184                 | Update –<br>new messages added to index                                                                                                                                                                    |
| Page 204                 | Update –<br>removed refer to Wait For Settlement Market Practice                                                                                                                                           |
| Page 351                 | New –<br>new high level message flow                                                                                                                                                                       |
| Page 371                 | Updated –<br>new messages added to index                                                                                                                                                                   |
| Page 379-380             | New –<br>pacs.003 use cases                                                                                                                                                                                |
| Page 400                 | Updated –<br>additional guidance on ultimate parties on the return                                                                                                                                         |
| Page 423                 | Updated –<br>correct to Agent description in Step 7                                                                                                                                                        |
| Page 458-488             | New –<br>pacs.010 Margin Collection section                                                                                                                                                                |
| Page 489-529             | New –<br>pacs.003 Customer Direct Debit section                                                                                                                                                            |
| Page 530                 | Updated –<br>new message added to index                                                                                                                                                                    |
| Page 674                 | Updated –<br>removed reference to SR 2023                                                                                                                                                                  |
| Page 682                 | Updated –<br>moved reference to multiple notification, now at an Item<br>level                                                                                                                             |
| Page 691                 | Updated –<br>reference to multiple notification item Rule                                                                                                                                                  |
| Page 698-716             | New –<br>camt.058 Notice to Received Cancellation section                                                                                                                                                  |
| Page 743                 | Updated -<br>new message added to index                                                                                                                                                                    |
| Page 764                 | Updated -<br>use case id correction                                                                                                                                                                        |
| Page 774-795             | New –<br>Customer Cancellation Request section                                                                                                                                                             |
| Page 823-883<br>Page 880 | The following icons dignify changes to slide from the previous itineration.<br>New –<br>Cheque message sections<br>Updates to text on a slide are captured in gold.<br>Updated -<br>use case id correction |

![](_page_2_Picture_0.jpeg)

# **Table of contents**

- **1. [Introduction to ISO 20022](#page-5-0)**
- **2. [Business Application Header](#page-24-0)**
- **3. [Payment Initiation \(pain\)](#page-38-0)**

```
pain.001 - Interbank Customer Credit Transfer Initiation
```

**pain.002 - Interbank Customer Payment Status Report**

**pain.008 – Customer Direct Debit Initiation**

### **4. Payment, Clearing and Settlement (pacs) messages**

```
pacs.002 – Financial Institution to Financial Institution Payment Status Report
```

**pacs.004 – Payment Return**

**pacs.003 – Financial Institution to Financial Institution Customer Direct Debit**

**pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer** 

**pacs.009 (core) - Financial Institution Credit Transfer** 

**pacs.009 (cov) - Financial Institution 'Cover' Credit Transfer**

**pacs.009 (adv) – Financial Institution 'Advice' Credit Transfer** 

# <span id="page-4-0"></span>**Table of contents (continued)**

**5. Cash Management Reporting (camt) messages**

**camt.052 - Bank to Customer Account Report**

**camt.053 - Bank to Customer Statement**

**camt.054 - Bank to Customer Debit Credit Notification**

**camt.057 – Notification to Receive**

**camt.058 – Notification to Receive Cancelation Advice** 

**6. Cash Management Exception & Investigation (camt) messages**

**camt.029 - Resolution of Investigation**

**camt.055 – Customer Payment Cancelation Request**

**camt.056 - FI to FI Cancellation Request**

### **7. Cheques**

**camt.107 – Cheque Presentment Notification**

**camt.108 – Cheque Cancellation or Stop Notification**

**camt.109 – Cheque Cancellation or Stop Report**

![](_page_4_Picture_16.jpeg)

# <span id="page-5-0"></span>**Introduction to ISO 20022**

ISO 20022 introduces a fundamental change to the traditional language used by the payments industry for several decades. It also describes participants (i.e., parties) to a business transaction differently based upon the business domain (area) being described, in a similar way you may describe a person as a colleague, parent or sibling depending upon the context you wish to describe them. This section is designed to capture and explain some of the differences.

# **Domains**

### **Payment and Cash Management**

Securities Trade Services Foreign Exchange Card Payment

## **Message Definitions**

**acmt** Account Management

**auth** Authorities

**camt** Cash Management

**pacs** Payment Clearing and Settlement

**pain** Payment Initiation

**remt** Payment Remittance Advice

### **Message Sets**

camt.052 Bank to Customer Account Report camt.053 Bank to Customer Statement

camt.054 Bank to Customer Debit Credit Notification camt.056 FI to FI Payment Cancellation Request

camt.057 Notification to Receive

pacs.002 FI to FI Payment Status Report

pacs.004 Payment Return pacs.008 FI to FI Customer Credit Transfer

pacs.009 Financial Institution Credit Transfer

pain.001 Customer Credit Transfer initiation pain.002 Customer Payment Status Report pain.012 Creditor Payment Activation Request

![](_page_7_Picture_21.jpeg)

ISO 20022 catalogue messages hierarchically beginning with a Business Domain, contain a various sets of Message Definitions, which in turn contain a variety of Message Sets.

### for example:

- ➢ Payment and Cash Management
  - ➢ Payments Clearing and Settlement ➢ FI to FI Customer Credit Transfer (pacs.008)

<span id="page-8-0"></span>![](_page_8_Figure_0.jpeg)

![](_page_8_Figure_1.jpeg)

<span id="page-9-0"></span>![](_page_9_Figure_1.jpeg)

The diagram attempts to explain the construct of an ISO 20022 message sent across the SWIFT network using the **FINplus** service (which is designated to support various ISO 20022 business domains on SWIFT Interact)

Within the CBPR+ User Handbook the predominant focus is on the **Request Payload,** as this is where the business information is contained. However, it is worth noting that a network provider will have additional containers around the Request Payload to perform functionality on its network. This diagram presents the additional containers on the SWIFT network such as the Request Header often referred to as the Technical Header of the message.

![](_page_10_Figure_2.jpeg)

### **XML Elements**

An XML instance or document contains data in elements and nested elements (elements which contain other elements) corresponding to the hierarchy imposed by the XML schema. In the CBPR+ Usage Guidelines we often refer to the element hierarchy by levels (to understand the nested relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example in a pacs.008 Customer Credit Transfer the *Interbank Settlement Date* is a sub-element (Level 2) of the *Credit Transfer Transaction Information* element (Level 1).

### **Naming conventions**

An XML element is named according to the following rules:

- The name can contain letters, numbers, and other characters, but must not start with a number or punctuation mark.
- The name must not start with XML, xml, or Xml.
- The name must not contain any spaces.

### **MX naming conventions**

There are some generic naming rules that apply to most items in the database.

- The names of all items in the database use the upper CamelCase convention, as follows:
  - Each word starts with a capital letter.
  - There are no white spaces between words.
- A name may be made up of multiple words, each consisting of alphanumeric characters.
- Words use British English vocabulary.
- All names must start with an alphabetic character.
- All characters that follow the first characters must be letters or numbers.

**Example of a Street Name element:** <StrtNm>Oxford Street</StrtNm>

![](_page_11_Picture_17.jpeg)

**MX message element multiplicity (occurrences)**

### **Empty XML Elements**

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element.

A common example of this is in payment message is Financial Institution.

| ✓ o Financial Institution Identification  |   |   |
|-------------------------------------------|---|---|
| > o BICFI                                 | 0 | 1 |
| > o Clearing System Member Identification | 0 | 1 |
| • LEI                                     | 0 | 1 |
| <ul> <li>Name</li> </ul>                  | 0 | 1 |
| > o Postal Address                        | 0 | 1 |
|                                           |   |   |

Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e., <FinInstnId></FinInstnId>

In the **FINplus** service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where business data should be provided within a nested element, it is provided.

MyStandards describes the element's context by its path whereby each element is divided by a forward slash (/) For example the pacs.008 Town Name within the Debtor Postal Address is described as /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/PstlAdr/TwnNm

Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing the element in an XML naming convention.

For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment Identification is an element below Credit Transfer Transaction Information.

### *Credit Transfer Transaction Info' Payment Identification*

In this way the CBPR+ User Hand Book uses three main icon to explain the relationships between element, by display the icon after the element name.

To visualise an element which has nested elements beneath it

To visualise an element which has a choice associated with it i.e., a Code where a choice of which code can be determined

To visualise an element which is nested and has a choice associated with it. For example, an Identification where a choice must be made between an Organisation Identification and a Private Identification element which is nested, but where both cannot be used together.

![](_page_14_Picture_0.jpeg)

#### CBPR+

Cross-Border Payments and Reporting Plus (CBPR+) specifications define how ISO 20022 is used for cross-border payments and cash reporting on the Swift network. Conformance to CBPR+ specifications will be validated by Swift messaging services and interfaces, so it is imperative that users implement the specifications correctly. The resources available on this page aim to help Swift's community to understand and implement CBPR+ specifications.

Learn more about ISO 20022 Readiness >

CBPR+ Usage Guidelines and Readiness Portal

**CBPR+ Translation Portal** 

![](_page_14_Figure_6.jpeg)

### https://www2.swift.com/mystandards/#/c/cbpr/landing

Traditionally in the Legacy FIN standard rules related to a message were described as either *Network Validation Rules* – those validated by the network, or *Usage rules* – rules not validated by the network. FIN also has the concept of *Usage Guidelines* – guideline to recommend a best practice.

In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated Usage Guideline (e.g. CBPR plus)

Within CBPR+ Usage Guideline specification the rules dedicate to CBPR+ are often described as:

**Formal Rules** which are validated on the network, these are identified by the word **Rule** appended to the rule description. For example: *Rule "CBPR\_Party\_Name\_Any\_BIC\_FormalRule"*

**Textual Rules** which are not validated on the network, these are identified by with the word **TextualRule** appended to the rule description. For example: *Rule "CBPR\_Agent\_Option\_1\_TextualRule"*

**Guideline Rules** which provide recommended best practice, these are identified by the word **Guideline** appended to the rule description. For example: *Rule "CBPR\_Purpose\_Guideline"*

Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a **CrossElementSimpleRule** and a **CrossElementComplexRule**

![](_page_17_Figure_0.jpeg)

- Type: **String**
- Max allowed size: **35 characters**
- Structure:
  - o Must contain minimum **A & B**, **optionally followed by 1 or more additional business context elements (C, D, …).**
  - o Always **ends** with **version element E** (format "nn", e.g., "01")
  - o Each element is separated by a period "."
  - o Length of **each** text element **can vary** up to **max 10** characters. Total length, including periods, cannot exceed 35 chars.
  - o Consistency enforced by lightweight SWIFT review/registration: E.g., "ecb" to represent the ECB, not "eucb"
  - o **Lowercase** alphanumerical characters only

![](_page_17_Picture_10.jpeg)

In CBPR+ the Usage Identifier is captured within the *Business Application Header*, *Business Service* element. More detail can be found in the dedicated Business Application Header chapter of this document,

![](_page_18_Picture_0.jpeg)

Many ISO 20022 message use data elements represented by codes. Such codes are often externalised from the message itself, enabling maintenance of the code list on a quarterly basis without requiring a new message version.

Some data element may also be embedded in the message.

example of Charge Bearer in pacs.008 v8 which uses embedded codes

| →                                | 1 | 1 |
|----------------------------------|---|---|
| ♦ Borne By Debtor [DEBT]         |   |   |
| ♦ Borne By Creditor [CRED]       |   |   |
| ♦ Shared [SHAR]                  |   |   |
| ♦ Following Service Level [SLEV] |   |   |

Proprietary Codes may also be available for certain data elements. These are typically inherited from legacy formats and require definitions in user documentation as these are not captured in the baseline ISO 20022 standards

example of Return Reason Information in pacs.004 v9 which uses externalised codes

![](_page_18_Figure_7.jpeg)

All SWIFT ISO MX message elements (fields) which are defined (by data Type) as text are restricted to FIN X Characters:

**a-z A-Z 0-9 / - ? : ( ) . , ' + .**

Special characters are additionally allowed in:

- All party (agents and non-agents) Name and Address elements.
- The Related Remittance Information element
- The Remittance Information (structured & unstructured) element
- The Email Address where included as part of a Proxy elements
- City of Birth and Province of Birth elements nested in Private Identification

Currencies in the payments should be expressed in ISO Currency Codes only (3- Characters, e.g. EUR)

Translation of any special character:

**!#&%\*=^\_`{|}~";@[\]\$ ><**  into MT messages will be represented by a **. (Full Stop)**

![](_page_19_Figure_11.jpeg)

List of special characters: **!#&%\*=^\_`{|}~";@[\] \$ > <**

![](_page_20_Picture_0.jpeg)

**Point-to-point** refers to data passed within a message from one party to the next. This data will not necessarily be passed in subsequent messages.

➢ For example: the *Instruction Identification element* contains a reference meaningful to the party sending a message, subsequent messages in a payment transaction chain can expect the *Instruction Identification* to be replaced by a reference meaningful to the party sending that message leg.

![](_page_20_Picture_3.jpeg)

**End-to-end** refers to data passed throughout the transaction life cycle i.e. within a message from one party to the next and continued in subsequent messages.

➢ For example: the *UETR element* contains a Unique End-to-end Transaction Reference in accordance with the UUID version 4 standards. This same reference is used in all messages related to the payment transaction.

![](_page_21_Picture_0.jpeg)

ISO 20022 messages have a number of elements associated with Agents which allow for these Agents to be referenced by a variety of Financial Institution identifiers.

More commonly the ISO 9362 Financial Institution BIC (*BICFI*) is considered the best practice de facto standard for 'many to many' / correspondent banking payments. However other options include:

*Clearing System Member Identifiers* when accompanied with the *Clearing System Identification*. *LEI* (Legal Entity Identifier)

*Name* and either structured or unstructured *Postal Address*.

![](_page_21_Figure_5.jpeg)

![](_page_21_Picture_6.jpeg)

Two common elements to ISO 20022 messages are *Date* and *DateTime.*

![](_page_22_Picture_1.jpeg)

CBPR+ usage guidelines *DateTime* elements mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) note - milliseconds are optional.

![](_page_22_Picture_5.jpeg)

The ISO 20022 *Date* elements allow the date to include an offset. As a data model, shared by other business domains, an offset date can provide great business clarify, such as something expiring at the end of a business date. However, in payments such a date offset provides little business value, whereby should an offset be include with the date, this offset should be ignored.

| Country      | Code Name                                               | MT<br>Clearing<br>System code | ISO<br>20022 Clearing<br>System Identification |  |
|--------------|---------------------------------------------------------|-------------------------------|------------------------------------------------|--|
| Australia    | Australian Bank State Branch Code (BSB)                 | AU                            | AUBSB                                          |  |
| Austria      | Austrian Bankleitzahl                                   | AT                            | ATBLZ                                          |  |
| Canada       | Canadian Payments Association Payment<br>Routing Number | CC                            | CACPA                                          |  |
| China        | Bank Branch code used in China                          | CN                            | CNAPS                                          |  |
| Germany      | German Bankleitzahl                                     | BL                            | DEBLZ                                          |  |
| Greece       | Helenic Bank Identification Code                        | GR                            | GRBIC                                          |  |
| Hong Kong    | Hong Kong Bank Code                                     | HK                            | HKNCC                                          |  |
| India        | Indian Financial System Code                            | IN                            | INFSC                                          |  |
| Ireland      | Irish National Clearing Code                            | IE                            | IENCC                                          |  |
| Italy        | Italian Domestic Identification Code                    | IT                            | ITNCC                                          |  |
| Japan        | Japan Zengin<br>Clearing Code                           | JP                            | JPZGN                                          |  |
| New Zealand  | New Zealand National Clearing Code                      | NZ                            | NZNCC                                          |  |
| Poland       | Polish National Clearing Code                           | PL                            | PLKNR                                          |  |
| Portugal     | Portuguese National Clearing Code                       | PT                            | PTNCC                                          |  |
| Russia       | Russian Central Bank Identification Code                | RU                            | RUCBC                                          |  |
| South Africa | South African National Clearing Code                    | ZA                            | ZANCC                                          |  |
| Spain        | Spanish Domestic Interbanking<br>Code                   | ES                            | ESNCC                                          |  |
| Switzerland  | Swiss Clearing Code (BC Code)                           | SW                            | CHBCC                                          |  |
| Switzerland  | Swiss Clearing Code (SIC Code)                          | SW                            | CHSIC                                          |  |
| Taiwan       | Financial Institution Code                              | TW                            | TWNCC                                          |  |
| UK           | UK Domestic Sort Code                                   | SC                            | GBDSC                                          |  |

![](_page_23_Picture_1.jpeg)

For translation rules and comparison purposes this table provides a list of published MT National Clearing System codes again their equivalent ISO 20022 Clearing System Identification in the external code list.

# <span id="page-24-0"></span>**Business Application Header**

The head.001 Business Application Header *Character Set* element declares the character set, in addition to Latin, that is contained in the Business Document e.g. the pacs.008.

![](_page_25_Picture_2.jpeg)

The *Character Set* element uses the UnicodeChartsCode string to declare an additional character set, for example **Cyrillic** (Unicode range: 0400-04FF).

![](_page_25_Picture_4.jpeg)

![](_page_25_Picture_5.jpeg)

This allows the party for which the message is addressed *To* to know in advance the additional character set contained within the Business Document. In this way the message can be routed to a specific application to process the Character Set or handled as an exception if the Character Set is not appropriate for that business transaction.

![](_page_25_Picture_7.jpeg)

Extending character sets is not intended in CBPR+ from the initial implementation of the service. This element is intended for use once extended character sets are implemented, whereby the string represented in this element can enable any necessary network validations, such as a closed user group for that character set.

The head.001 Business Application Header *From* element identifies the BIC of the party who created the Business Document (e.g. pacs.008). Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

![](_page_26_Picture_2.jpeg)

A choice must be made for the BIC depending on the party it represents.

*Financial Institution Identification* which identifies a Financial Institution, and may be further complemented with

- *Clearing System Member Identification*
- *LEI*

as an additional identification.

The head.001 Business Application Header *To* element identifies the BIC of the party who will ultimately process the Business Document (e.g. pacs.008) Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

![](_page_27_Picture_2.jpeg)

A choice must be made for the BIC depending on the party it represents.

*Financial Institution Identification* which identifies a Financial Institution, and may be further complemented with

- *Clearing System Member Identification*
- *LEI*

as an additional identification.

*To*

The head.001 Business Application Header *Business Message Identifier* element contains the *Message Identification* captured within the Business Document's Group Header. The content of this element should match the Business Document to avoid incorrect routing by the recipient.

![](_page_28_Figure_2.jpeg)

The head.001 Business Application Header *Message Definition Identifier* element contains the name of the Business Document. The content of this element should match the Business Document to avoid incorrect routing by the recipient.

![](_page_29_Figure_2.jpeg)

**Min 1 – Max 1**

The head.001 Business Application Header *Business Service* element is used to identify administered services on the SWIFT network. The data represented in this elements is referred to as a **Usage Identifier**. For CBPR+ examples are provided below, these values may be used together with the *Message Definition Identifier* to determine routing rules to specific applications without having to open the business document.

| Message Definition Identifier | BusinessService       | Business Use Case                                |
|-------------------------------|-----------------------|--------------------------------------------------|
| pacs.009.001.08               | swift.cbprplus.cov.01 | Financial Institution (Cover) Credit<br>Transfer |
| pacs.009.001.08               | swift.cbprplus.01     | Serial Financial Institution Credit Transfer     |
| pacs.008.001.08               | swift.cbprplus.stp.01 | STP Customer Credit Transfer                     |

The *Business Service* is also intended to be incremented for the same message version, when an updated Usage Guideline is released. For example a new restriction is applied to the pacs.009.001.08 Usage Guideline, the **Business Service** swift.cbprplus.cov.02 and swift.cbprplus.02 will be used to reflect these new Guidelines and allow network validate.

**Note**: when a new message (Message Definition Identifier) version is introduced the numeric value for the

Business Service is reset.

<span id="page-31-0"></span>

| Message Definition<br>Identifier    | Business Service       | Message Definition<br>Identifier                                                                                                                                                                                                                        | Business Service             |  |
|-------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|--|
| pain.001.001.09                     | sw ift.cbprplus.02     | camt.058.001.08                                                                                                                                                                                                                                         | sw ift.cbprplus.01           |  |
| pain.002.001.10                     | sw ift.cbprplus.02     | camt.060.001.05                                                                                                                                                                                                                                         | sw ift.cbprplus.02           |  |
| pain.008.001.03                     | sw ift.cbprplus.01     | camt.107.001.01                                                                                                                                                                                                                                         | sw ift.cbprplus.01           |  |
| pacs.002.001.10                     | sw ift.cbprplus.02     | camt.108.001.01                                                                                                                                                                                                                                         | sw ift.cbprplus.01           |  |
| pacs.003.001.08                     | sw ift.cbprplus.01     | camt.109.001.01                                                                                                                                                                                                                                         | sw ift.cbprplus.01           |  |
| pacs.004.001.09                     | sw ift.cbprplus.02     |                                                                                                                                                                                                                                                         |                              |  |
| pacs.008.001.08                     | sw ift.cbprplus.02     |                                                                                                                                                                                                                                                         |                              |  |
| pacs.008.001.08<br>(STP/STP EU)     | sw ift.cbprplus.stp.02 | The<br>data<br>represented<br>in<br>the<br>Business<br>Service,<br>together<br>Message<br>Definition<br>Identifier<br>has<br>a<br>number<br>of<br>roles,<br>in<br>addition                                                                              |                              |  |
| pacs.009.001.08 (advice)            | sw ift.cbprplus.adv.02 |                                                                                                                                                                                                                                                         |                              |  |
| pacs.009.001.08 (core)              | sw ift.cbprplus.02     | routing<br>rules<br>referred<br>to<br>on<br>the                                                                                                                                                                                                         | previous<br>page.            |  |
| pacs.009.001.08 (cov)               | sw ift.cbprplus.cov.02 | This<br>data<br>value:                                                                                                                                                                                                                                  |                              |  |
| pacs.010.001.03                     | sw ift.cbprplus.02     |                                                                                                                                                                                                                                                         |                              |  |
| pacs.010.001.03 (Margin Collection) | sw ift.cbprplus.col.01 | ▪<br>Identifiers<br>explicitly<br>the                                                                                                                                                                                                                   | Usage<br>Guideline<br>within |  |
| camt.029.001.09                     | sw ift.cbprplus.02     | guideline.<br>For<br>example<br>an<br>application<br>may<br>have<br>various<br>libraries<br>within<br>a<br>collection,<br>for<br>which<br>only<br>one<br>of<br>appropriate<br>to<br>be<br>used<br>to<br>identify<br>data<br>requirements<br>validation. |                              |  |
| camt.052.001.08                     | sw ift.cbprplus.02     |                                                                                                                                                                                                                                                         |                              |  |
| camt.053.001.08                     | sw ift.cbprplus.02     |                                                                                                                                                                                                                                                         |                              |  |

camt.054.001.08 sw ift.cbprplus.02 camt.055.001.08 sw ift.cbprplus.01 camt.056.001.08 sw ift.cbprplus.02

validation. • is also populated in the Request Header of the InterAct message in the **Request Sub Type** element which allow the service (FINplus for CBPR+) to apply network validation rules.

The head.001 Business Application Header *Market Practice* element is used to identify administered services on the SWIFT network.

This element is currently not foreseen to be used by CBPR+.

The head.001 Business Application Header *Creation Date* captures the date and time which the Business Application Header was created.

![](_page_33_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_33_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The head.001 Business Application Header *Copy Duplicate* indicator is used as a choice to identify scenarios where a message was previously sent.

![](_page_34_Picture_2.jpeg)

*COPY* is used to represent a copy of a message being sent to an additional party. This scenario is only associated with camt reporting messages.

![](_page_34_Picture_4.jpeg)

*DUPL* is used to represent a duplicate of a previously sent camt reporting message. To receive a duplicate payment message, Interact message retrieval should be utilised.

![](_page_34_Picture_6.jpeg)

*CODU* is used to represent a duplicate of a previously sent *COPY* message. This scenario is only associated with camt reporting messages.

The head.001 Business Application Header *Possible Duplicate* element is used as a flag to indicate that if the party who will ultimately process the Business Document (e.g. pacs.008) received the original, then it should perform necessary actions to avoid processing this Business Message again.

![](_page_35_Picture_2.jpeg)

This element is represented by a Yes/No Boolean, whereby **true** represent this is a Possible Duplicate.

![](_page_35_Picture_4.jpeg)

It is not necessary to represent **false** (No) the absence of this optional element itself indicates that this is not considered a Possible Duplicate.

![](_page_35_Picture_6.jpeg)

The FINplus Technical Header has an element **PDIndicator**(Possible Duplicate Indicator) which uses a Yes/No Boolean. This may be populated by the network interface to identify a message it considers may be a possible duplicate.

The head.001 Business Application Header *Priority* element allows a choice of Business Message Priority Code to indicate the priority which may be applied to the business message.

![](_page_36_Picture_2.jpeg)

This element must represent the priority code of the business document (instance) which is only applicable for pacs messages. The pacs message priority is captured in the Payment Type Priority/Instruction Priority.

The head.001 Business Application Header *Related* nested element enables the capture of the Business Application Header from a related Business Document. For example, in a pacs.004 Payment Return the *Related* Business Application Header from the original message can be included. This could allow the receiver to apply specific routing to the message, based on the related information i.e., return of a pacs.009 cov may be routed to different payment engine than a core pacs.009.

![](_page_37_Picture_2.jpeg)

The following elements are nested within the Related element. Where used these contain the original data from the related Business Application Header:

*From To Business Message Identifier Message Definition Identifier Business Service Creation Date Copy Duplicate Priority* **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 1 – Max 1 Min 1 – Max 1 Min 1 – Max 1 Min 1 – Max 1 Min 1 – Max 1**

![](_page_38_Picture_0.jpeg)

<span id="page-38-0"></span>**pain.001 - [Interbank Customer Credit Transfer initiation](#page-39-0) pain.002 – Interbank Customer Payment Status Report pain.008 – Customer Direct Debit Initiation**

# <span id="page-39-0"></span>**Interbank Customer Credit Transfer Initiation**

![](_page_40_Picture_1.jpeg)

![](_page_40_Picture_2.jpeg)

ISO 20022 message element MT Field Name & (Tag option)

### *Group Header*

- ➢ *Message Identification*
- ➢ *Initiating Party*  where different from *Debtor*
- ➢ *Forwarding Agent*

### *Payment Information*

- ➢ *Payment Information Identification*
- ➢ *Requested Execution Date*
- ➢ *Debtor*
- ➢ *Debtor Agent*

### *Credit Transfer Transaction Information*

- ➢ *Payment Identification*
- ➢ *Amount*
- ➢ *Charge Bearer*
- ➢ *Creditor Agent*
- ➢ *Creditor*

### **Sequence A –** General Information**:**

- ➢ **Sender's Reference** (Field 20)
- ➢ **Instructing Party** (Field 50 C or L)

### Message **Sender**in a 'relay' scenario

### **Sequence A –** General Information**:**

- ➢ **Customer Specified Reference** (Field 21R)
- ➢ **Requested Execution Date** (Field 30)
- ➢ **Ordering Customer** (Field 50 F, G or H)\*
- ➢ **Account Servicing Institution** (Field 52 A or C)\*

### **Sequence B –** Transaction Details**:**

- ➢ **Transaction Reference** (Field 21)
- ➢ **Currency/Transaction Amount** (Field 32B)
- ➢ **Details of Charges** (Field 71A)
- ➢ **Account With Institution** (Field 57 A, C or D)
- ➢ **Beneficiary** (Field 59 no letter, A or F)

# pain.001 Group Header Payment Information Credit Transfer Transaction Information

### The pain.001 message is composed of three blocks:

- Group Header contains a set of characteristics that relates to all individual transaction.
- Payment Information contains a set of characteristics that relates to the debit side of the transaction, such as Debtor and Debtor Agent.
- Credit Transfer Transaction Information contains, among others, elements related to the credit side of the transaction, such as Creditor and Creditor Agent.

![](_page_41_Picture_5.jpeg)

Payment messages in a many-to-many payment are considered as a single transaction.

- -----

<span id="page-42-0"></span>![](_page_42_Figure_1.jpeg)

FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

**Relay**: The pain.001 message is sent by the Initiating party (the Debtor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.001 message to the Debtor Agent

**pain.001**

![](_page_43_Figure_1.jpeg)

FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

*Authorised Party Initiation:* The pain.001 message is sent by the Financial Institution as an Initiating Party to the Debtor Agent to initiate a payment on behalf of the Debtor who is the account holder. For example, a FI Initiates; a liquidity sweep on behalf of a corporate customer or payment from the Debtor account based on Tri-party agreement (agreement from the Debtor with the Debtor **2**

![](_page_44_Figure_1.jpeg)

Interbank Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

*Financial Institution Payment Initiation* (to non-FI) : The pain.001 message is sent by the Financial Institution as both the Debtor and Initiating Party to initiate a payment from their account with the Debtor Agent to move funds to a non-Financial Institution Creditor **3**

The following descriptions are defined in the ISO 20022 Standard for core parties participating in an Interbank Customer Credit Transfer Initiation relationship.

![](_page_45_Picture_1.jpeg)

**Forwarding Agent -** "Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution". Applicable for pain.001 use case 1 only

![](_page_45_Picture_3.jpeg)

**Initiating Party –** "Party that initiates the payment." which may be the **Debtor** or a Party acting on behalf of the Debtor e.g., the Agent initiating a liquidity sweep service

![](_page_45_Picture_5.jpeg)

**Debtor Agent -** "Financial institution servicing an account for the debtor."

**Creditor Agent -** "Financial institution servicing an account for the creditor."

![](_page_45_Picture_8.jpeg)

![](_page_45_Picture_9.jpeg)

**Debtor -** "Party that owes an amount of money to the (ultimate) creditor."

**Creditor -** "Party to which an amount of money is due."

![](_page_45_Picture_12.jpeg)

# **Group Header**

![](_page_47_Picture_1.jpeg)

![](_page_47_Picture_2.jpeg)

Each ISO20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For the Payment Initiation (pain) messages the *Message Identification* has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

![](_page_47_Picture_5.jpeg)

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

![](_page_47_Picture_7.jpeg)

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor or authorized third party) of the pain.001.

**pain.001 Interbank Customer Credit Transfer Initiation – Creation Date Time**

**Min 1 – Max 1**

The pain.001 message *Creation Date Time* captures the date and time which the message was created.

![](_page_48_Picture_3.jpeg)

It is defined by *ISO Date Time* with mandatory date and time components expressed in the following formats:

- 1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
- 2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
- 3. Local time format YYYY-MM-DDThh:mm:ss.sss

![](_page_48_Picture_8.jpeg)

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2nd option). Otherwise use UTC time (1st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

## **pain.001 Interbank Customer Credit Transfer Initiation – Authorisation**

**Min 0 – Max 2**

The pain.001 message *Authorisation* allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The *Authorisation* uses an embedded code set or free text form. It has no exact equivalent in the legacy MT payment message, however, the Authorisation (Field 25) could be considered as a similar comparison.

| Code | Description                      | Description                                                                                                                          |
|------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ILEV | Instruction Level Authorisation  | File<br>requires all customer transactions to be authorised or approved.                                                             |
| FDET | File Level Authorisation Details | Additional file level approval, with the ability to view<br>both the payment information block<br>and supporting transaction detail. |
| FSUM | File Level Authorisation Summary | Additional<br>file level approval, with the ability to view only the payment information block.                                      |
| AUTH | PreAuthorised File               | File has been pre-authorised or approved within the originating customer environment<br>and no further approval is required.         |

![](_page_49_Picture_3.jpeg)

For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.

# **pain.001 Interbank Customer Credit Transfer Initiation – Number of Transactions**

**Min 1 – Max 1**

The pain.001 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_50_Picture_3.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_50_Picture_5.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

# **pain.001 Interbank Customer Credit Transfer Initiation – Initiating Party**

![](_page_51_Picture_1.jpeg)

For the second and the third use case, BIC of the Initiating Party is required.

### **Min 1 – Max 1**

The *Initiating Party* can either be the *Debtor* or an Authorised Party who initiates payment transactions on behalf of the *Debtor*. The Initiating Party can be, for example, the Head Office which has the authority to debit the account of its subsidiary. In the centralization model, the *Initiating Party* can also be a payment factory or shared service center or third-party agent, which has authority to send the message on behalf of the *Debtor*.

There are three common use cases in the context of interbank pain.001 message:

- **1. Relay**: The *Initiating Party*, which is either the *Debtor* themselves or authorised party, sends the pain.001 message to the *Forwarding Agent* which acts as a concentrating financial institution. It will forward the pain.001 message to the *Debtor Agent*. This is commonly known as a relay scenario. Whereby the Forwarding Agent is performing a technical role in the payment transaction, they would not be represented in the payment, clearing and settlement message.
- **2. Authorised Party**: The *Initiating Party* is the *Financial Institution* which has the authority to send the pain.001 message on behalf of the *Debtor*, e.g., multi-bank liquidity sweeps.
- **3. Financial Institution Payment Initiation**: The *Initiating Party* is the *Financial Institution* which is the *Debtor* who initiate a payment from their account to move

![](_page_52_Figure_0.jpeg)

# **pain.001 Interbank Customer Credit Transfer Initiation – Forwarding Agent**

![](_page_53_Picture_1.jpeg)

The *Forwarding Agent* is mandatory in a relay scenario whereby the *Initiating Party* (the *Debtor* or authorised third party) has to provide *Business Identifier Code* (BIC FI) of the *Forwarding Agent* in the original pain.001 message. The Forwarding Agent acts as a concentrating financial institution and forwards the pain.001 message to the *Debtor Agent* for execution.

Other options to identify the *Forwarding Agent* include:

**Min 0 – Max 1**

- Clearing System Member ID
- LEI (Legal Entity Identifier)

![](_page_53_Figure_6.jpeg)

*Group Header Forwarding Agent*

![](_page_53_Picture_7.jpeg)

For the use cases of Authorised Party initiation and FI payment initiation, Forwarding Agent is not required.

# **Payment Information**

<span id="page-55-0"></span>The CBPR+ pain.001 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognise that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory.

As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message.

Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used.

![](_page_55_Figure_3.jpeg)

The Interbank Customer Credit Transfer Initiation *Payment Information Identification* provides a mandatory element to identify the payment initiation.

![](_page_56_Picture_2.jpeg)

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions.

![](_page_56_Picture_4.jpeg)

For single transactions in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header.

The pain.001 message *Payment Method* specifies the means of payment that will be used to move the amount of money. One of the following payment method codes must be used:

![](_page_57_Picture_2.jpeg)

![](_page_57_Picture_3.jpeg)

| Code | Name               | Definition                                                                                     |
|------|--------------------|------------------------------------------------------------------------------------------------|
| CHK  | Cheque             | Written order to a bank to pay a certain amount of<br>money from one person to another person. |
| TRF  | Credit<br>Transfer | Transfer of an amount of money in the books of the<br>account<br>servicer.                     |

The pain message *Payment Type Information* provides a set of optional elements where the payment type can be described.

*Instruction Priority*  **Min 0 – Max 1**

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the

processing

*Service Level*  **Min 0 – Max 3** Anested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored.

*Payment Type Information*

i

*Local Instrument*  **Min 0 – Max 1**

Anested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, INST – Instant Credit Transfer forSEPAService Level.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

*Category Purpose* 

Anested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends.

*Payment Information Payment Type Information*

## **pain.001 Interbank Customer Credit Transfer Initiation – Requested Execution Date**

**Min 1 – Max 1**

The pain.001 message mandatory *Requested Execution Date* element, captures the date and time at which the initiating party requests the clearing agent to process the payment.

![](_page_59_Picture_3.jpeg)

It is the date on which the debtor's account is debited. If payment by cheque, the date when the cheque must be generated by the bank. It is defined by either *ISO Date* expressed in the *YYYY-MM-DD format* or *ISO Date Time* below:

- 1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
- 2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
- 3. Local time format YYYY-MM-DDThh:mm:ss.sss

![](_page_59_Picture_8.jpeg)

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2nd option). Otherwise use UTC time (1 st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

# **pain.001 Interbank Customer Credit Transfer Initiation – Pooling Adjustment Date**

**Min 0 – Max 1**

The pain.001 message optional *Pooling Adjustment Date* element, is used for the correction of the value date of a cash pool movement that has been posted with a different value date.

![](_page_60_Picture_3.jpeg)

It is defined by *ISO Date* expressed in the *YYYY-MM-DD format*

![](_page_60_Picture_5.jpeg)

This element is not widely used in the payment industry. For the use case of interbank, it is even less likely to be utilized.

The ISO 20022 pain messages describes the party whose account is debited for a transaction as the *Debtor*. The *Debtor* sub elements describe the *Debtor* in greater detail. **Min 1 – Max 1**

Mandatory *Name* (where a BIC identifier is not provided) by which the party is known

*Name*

![](_page_61_Figure_3.jpeg)

Nested element capturing either structured or unstructured *Debtor* address details.

![](_page_61_Picture_5.jpeg)

Note: Structured address is strongly recommended with mandatory Town Name and Country

*Identification* Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

*Postal Address*

*Country of* 

*Debtor*

*Residence* Optional element to capture the *Debtor*'s ISO country code of residence

### **Min 1 – Max 1**

The pain.001 *Debtor Account* is used to capture the account information for which debit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

> The *Debtor Account* uses a variety of nested elements to capture information related to the account.

![](_page_62_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account *Currency* identifies the currency of the account, recommended. **Min 0 – Max 1 Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

![](_page_62_Picture_8.jpeg)

Indication of Currency of the Debtor Account is recommended in case of multi-currency

**Min 1 – Max 1**

The *Debtor Agent* is a static role in the pain.001 Customer Credit Transfer Initiation. This agent maintains a relationship with their customers, the *Debtor*.

![](_page_63_Picture_2.jpeg)

![](_page_63_Picture_3.jpeg)

Note: Although the *Debtor Agent, Creditor Agent, Debtor and Creditor* all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

![](_page_63_Picture_5.jpeg)

**Min 0 – Max 1**

**Min 0 – Max 1 Min 0 – Max 1**

**Min 0 – Max 1**

The pain.001 *Debtor Agent Account* is used to capture the account information related to the Debtor Agent.

**pain.001 Interbank Customer Credit Transfer Initiation – Debtor Agent Account**

The *Debtor Agent Account* uses a variety of nested elements to capture information related to the account.

![](_page_64_Picture_3.jpeg)

**Min 1 – Max 1** *Identification*identifies the account maintained at theAccount Servicing Institution

*Type* uses the external CashAccount Type code list to identify the type of account

*Currency* identifies the currency of the account

*Name* identifies the name of the account as assigned by theAccount Servicing Institution **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_64_Picture_9.jpeg)

Debtor Agent and Creditor Agent are Financial Institutions, therefore the nested elements *Name* and *Proxy* are unlikely to be used.

**Min 0 – Max 1**

The *Instruction for Debtor Agent* element within the pain.001 message optionally provides information related to the processing of the payment.

![](_page_65_Picture_2.jpeg)

The *Instruction for Debtor Agent* element offers a maximum of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the *Debtor Agent*, depending on bilateral agreement.

![](_page_66_Picture_0.jpeg)

The pain.001 message introduces *Ultimate Debtor* and *Ultimate Creditor*. The *Ultimate Debtor* element should not be confused with an *Initiating Party* who may send a payment initiation request on behalf of the *Debtor,* for example, Payment Factory.

**Min 0 – Max 1**

**Min 0 – Max 1**

CBPR+ premise is that an *Ultimate Debtor* has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an *Ultimate Creditor* has no financial regulated account relationship with the corresponding Creditor.

The *Ultimate Debtor* and *Ultimate Creditor* can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

![](_page_66_Picture_4.jpeg)

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

### **Min 0 – Max 1**

The *Charge Bearer* element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

| Charge | Code | Description |               |      |                      |  |
|--------|------|-------------|---------------|------|----------------------|--|
| Bearer | CRED | Creditor    |               |      |                      |  |
| (0.1)  | DEBT | Debtor      |               |      |                      |  |
|        | SHAR | Shared      | 71A: Details  | Code | Description          |  |
|        |      |             | of<br>Charges | BEN  | Beneficiary          |  |
|        |      |             |               | OUR  | Our Customer Charges |  |
|        |      |             |               | SHA  | Shared Charges       |  |
|        |      |             |               |      |                      |  |

![](_page_67_Picture_3.jpeg)

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

*Payment Information Charges Account*

## **pain.001 Interbank Customer Credit Transfer Initiation – Charges Account**

**Min 0 – Max 1** The pain.001 optional *Charges Account* element, which is used to process charges associated with a transaction.

![](_page_68_Picture_2.jpeg)

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

![](_page_68_Picture_4.jpeg)

This element is not widely used in the payment industry.

## **pain.001 Interbank Customer Credit Transfer Initiation – Charges Account Agent**

**Min 0 – Max 1**

The pain.001 optional *Charges Account Agent* element, which is used to specify the agent that services a charges account.

![](_page_69_Picture_3.jpeg)

Charges account agent should only be used when the charges account agent is different from the debtor agent.

![](_page_69_Picture_5.jpeg)

This element is not widely used in the payment industry. It should also be noted that the ChargesAccountAgentRule inherited from the base message should be ignored as the optional Branch of DebtorAgent is removed from this Usage Guideline.

# **Credit Transfer Transaction Information**

The pain.001 message contains *Payment Identification* which provides a set of elements to identify the payment of which several are mandatory elements.

![](_page_71_Figure_2.jpeg)

The pain.001 *Payment Type Information* provides a set of optional elements where the payment type can

be described.

*Instruction Priority*  **Min 0 – Max 1**

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the

processing

*Service Level*  **Min 0 – Max 3** Anested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored.

*Payment Type Information*

i

*Local Instrument*  A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, INST – Instant Credit Transfer forSEPA Service Level.

![](_page_72_Picture_10.jpeg)

**Min 0 – Max 1** Note: the ISO instrument codes are registered by specific community group (captured in the code list)

![](_page_72_Picture_12.jpeg)

Anested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends.

**pain.001 Interbank Customer Credit Transfer Initiation – Currency and Amount**

The pain.001 nested *Amount* element has a choice of either *Instructed Amount* or *Equivalent Amount* to capture the amount and currency of the Customer Credit Transfer Initiation. **Min 1 – Max 1**

![](_page_73_Picture_2.jpeg)

The *Instructed Amount* captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. This amount has to be transported unchanged through the transaction chain. This element is comparable with the legacy Field 33B.

![](_page_73_Picture_4.jpeg)

*Equivalent Amount*

The *Equivalent Amount nested* element captures currency and *Amount* of money to be moved between the Debtor and Creditor, before deduction of charges, and is expressed in the currency of the Debtor's account. The *Currency Of Transfer* element capture the equivalent currency to be transferred which the first agent will convert the credit transfer into.

The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency. The pain.001 *Exchange Rate Information* element provides details on the currency exchange rate and contract. Specifies the type used to complete the currency exchange, such as SPOT, SALE or AGRD (Agreed). **pain.001 Interbank Customer Credit Transfer Initiation – Exchange Rate Information Min 0 – Max 1** *Exchange Rate Information Unit Currency Exchange Rate Rate Type Contract*  Currency in which the rate of exchange is expressed in a currency exchange. For example, 1GBP = xxxCUR, the unit currency is GBP. Unique and unambiguous reference to the foreign *Credit Transfer Transaction Information*

exchange contract agreed between the *Initiating*

The *Charge Bearer* element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

![](_page_75_Figure_2.jpeg)

![](_page_75_Picture_3.jpeg)

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

The *Cheque Instruction* information block contains a set of elements needed to issue a cheque. The following types of cheques are commonly used in the market:

| 12,000 |
|--------|
|        |
|        |

| Cheque<br>Type     | Code | Description                                                                                                                                                                                                                                                                                            |
|--------------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bank<br>Cheque     | BCHQ | Cheque drawn on the account of the debtor's financial institution, which is debited<br>on the debtor's account when the cheque is issued. These cheques are printed by<br>the debtor's financial institution and payment is guaranteed by the financial<br>institution. Synonym is 'cashier's cheque'. |
| Customer<br>Cheque | CCHQ | Cheque drawn on the account of the debtor and debited on the debtor's account<br>when the cheque is cashed. Synonym is 'corporate cheque'.                                                                                                                                                             |
| Draft              | DRFT | A guaranteed bank cheque with a future value date (do not pay before], which in<br>commercial terms is a 'negotiatable instrument': the beneficiary can receive early<br>payment from any bank under subtraction of a discount. The ordering customer's<br>account is debited on value date.           |

![](_page_76_Picture_4.jpeg)

The *Delivery Method* element specifies the method to be used in delivering the cheque by the *Debtor Agent*. For example, a code CRCD is used to courier the cheque to the *Creditor*.

![](_page_77_Picture_0.jpeg)

The pain.001 message introduces *Ultimate Debtor* and *Ultimate Creditor*. The *Ultimate Debtor* element should not be confused with an *Initiating Party* who may send a payment initiation request on behalf of the *Debtor,* for example, Payment Factory.

**Min 0 – Max 1**

CBPR+ premise is that an *Ultimate Debtor* has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an *Ultimate Creditor* has no financial regulated account relationship with the corresponding Creditor.

The *Ultimate Debtor* and *Ultimate Creditor* can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

![](_page_77_Picture_4.jpeg)

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

**Min 0 – Max 1**

**Min 0 – Max 1**

The pain.001 has three optional *Intermediary Agent (1,2* and *3)* elements. These agents represent the agent(s) that exist between the *Debtor Agent* and the *Creditor Agent*.

![](_page_78_Picture_2.jpeg)

- If more than one intermediary agent is present, then *Intermediary Agent 1* identifies the agent between the *Debtor Agent* and the *Intermediary Agent 2*.
- If more than two intermediary agents are present, then *Intermediary Agent 2* identifies the agent between the *Intermediary Agent 1* and the *Intermediary Agent 3*.
- If *Intermediary Agent 3* is present, then it identifies the agent between the *Intermediary Agent 2* and the *Creditor Agent*.

![](_page_78_Picture_6.jpeg)

More commonly the ISO 9362 Financial Institution *Business Identifier Code* is considered the best practice de factor standard for 'many to many' / correspondent banking payments.

Other options to identify the *Intermediary Agent* include:

![](_page_78_Picture_9.jpeg)

- Clearing System Member ID
- LEI (Legal Entity Identifier)
- Name and either structured, or unstructured Postal Address

![](_page_78_Picture_13.jpeg)

![](_page_78_Picture_14.jpeg)

Intermediary Agent 2

![](_page_78_Picture_15.jpeg)

![](_page_78_Picture_16.jpeg)

# **pain.001 Interbank Customer Credit Transfer Initiation – Intermediary Agent Account**

The pain.001 *Intermediary Agent (1,2* and *3) Accounts* are used to capture the account information related to these Agents. **Min 0 – Max 1**

![](_page_79_Picture_2.jpeg)

**Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1**

The *Intermediary Agent Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification*identifies the account maintained at theAccount Servicing Institution. *Type* uses the external CashAccount Type code list to identify the type of account.

*Currency* identifies the currency of the account.

*Name* identifies the name of the account as assigned by theAccount Servicing Institution.

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_79_Picture_8.jpeg)

Intermediary Agent Account 1 *Credit Transfer Transaction Information*

Intermediary Agent Account 2

#### **Min 0 – Max 1**

The *Creditor Agent* is a static roles in the pain.001 Customer Credit Transfer Initiation. This agent maintain a relationship with their customers, the *Creditor*.

![](_page_80_Picture_2.jpeg)

![](_page_80_Picture_3.jpeg)

Note: Although the *Debtor Agent, Creditor Agent, Debtor and Creditor* all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

![](_page_80_Picture_5.jpeg)

**Min 0 – Max 1**

**Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1**

The pain.001 *Creditor Agent Account* is used to capture the account information related to the *Creditor Agent*.

The *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

![](_page_81_Picture_3.jpeg)

**Min 1 – Max 1** *Identification*identifies the account maintained at theAccount Servicing Institution

*Type* uses the external CashAccount Type code list to identify the type of account

*Currency* identifies the currency of the account

**pain.001 Interbank Customer Credit Transfer Initiation – Creditor Agent Account**

*Name* identifies the name of the account as assigned by theAccount Servicing Institution *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_81_Picture_8.jpeg)

The ISO 20022 pain messages describe the *Creditor* as the party whose account was credited for a transaction. The *Creditor* sub elements describe the *Creditor* in greater detail. **Min 1 – Max 1**

Mandatory *Name* (where a BIC identifier is not provided) by

![](_page_82_Picture_2.jpeg)

*Identification* Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. strongly recommended with mandatory Town Name and Country

address details.

*Country of Residence* Optional element to capture the *Creditor*'s ISO country code of residence

![](_page_82_Picture_5.jpeg)

**Min 0 – Max 1**

The pain.001 *Creditor Account* is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

> The *Creditor Account* uses a variety of nested elements to capture information related to the account.

![](_page_83_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency of the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

Creditor Account is not required for cheque payments.

*Credit Transfer Transaction Information*

![](_page_84_Picture_0.jpeg)

The pain.001 message introduces *Ultimate Debtor* and *Ultimate Creditor*. The *Ultimate Debtor* element should not be confused with an *Initiating Party* who may send a payment initiation request on behalf of the *Debtor,* for example, Payment Factory.

CBPR+ premise is that an *Ultimate Debtor* has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an *Ultimate Creditor* has no financial regulated account relationship with the corresponding Creditor.

The *Ultimate Debtor* and *Ultimate Creditor* can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

**Min 0 – Max 1 Min 0 – Max 1**

![](_page_85_Picture_0.jpeg)

The *Instruction for Creditor Agent* element within the pain.001 message optionally provides information related to the processing of the payment for the Creditor Agent.

> The *Instruction for Creditor Agent* element offers a multiplicity of up to 2 occurrences of information. This element enables:

![](_page_85_Picture_3.jpeg)

- ➢ the use of an embedded choice of code to describe the instruction (e.g. CHQB Pay Creditor by Cheque)
- ➢ free format *instruction information*
- ➢ or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the *Creditor Agent*. It must be passed on throughout the life cycle of the transaction until the payment reaches the *Credit Agent*.

![](_page_85_Picture_8.jpeg)

![](_page_85_Picture_9.jpeg)

![](_page_86_Picture_0.jpeg)

# **ISO 20022 Programme**

**Quality data, quality payments**

**CBPR+ User Handbook**

SR 2023 Edition March 2023

**Min 0 – Max 1**

The *Instruction for Debtor Agent* element within the pain.001 message optionally provides information related to the processing of the payment.

![](_page_87_Picture_2.jpeg)

The *Instruction for Debtor Agent* element offers a maximum of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the *Debtor Agent*, depending on bilateral agreement.

The *Purpose* element within the pain.001 message captures the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment, e.g., IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the *Debtor*.

![](_page_88_Picture_3.jpeg)

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example, LIMAis classified within the Cash Management categorisation, with the *Name* Liquidity Management described as a Bank initiated account transfer to support zero target balance management, pooling or sweeping.

![](_page_88_Picture_6.jpeg)

*Category Purpose* also captures a high-level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g., Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

The *Regulatory Reporting* block within the pain.001 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

**Min 0 – Max 1**

The *Debit Credit Reporting Indicator* utilises an embedded choice of code to indicate whether the regulatory reporting applies to the:

- DEBT (debit)
- CRED (credit)
- BOTH

![](_page_89_Picture_7.jpeg)

**Min 0 – Max 1**

The *Authority* element captures the *Name* and *Country* code of the Authority/Entity requiring the regulatory reporting information.

**Min 0 – Max \***

The *Details* element provides the detail on the regulatory reporting information.

**Min 0 – Max 1**

The pain.001 nested *Tax* element captures information related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s).

This element caters for two main types of tax related payments:

- Tax payment obligation that is required to be transmitted with a payment
- Information that accompanies an actual payment of a tax obligation The follow nested elements may be used to capture detailed tax information:

![](_page_90_Picture_5.jpeg)

![](_page_90_Picture_6.jpeg)

Tax information block is also available within the Structured Remittance Information block which is applicable when tax information is used by the creditor as part of remittance information.

*Credit Transfer Transaction Information*

**Min 0 – Max 10**

The *Related Remittance Information* element within the pain.001 message is nested to provide information related to the handling of remittance information.

**Min 0 – Max 1**

The *Remittance Identification* captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction.

**Min 0 – Max \***

The *Remittance Location Details* uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- *Method* requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email)
- *Electronic Address* provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.
- *Postal Address* provides the postal address to which an agent is to send the remittance information

![](_page_91_Picture_9.jpeg)

Unlike CBPR+ pacs messages, in the interbank pain.001 message, Related Remittance Information and Remittance Information are non-mutually exclusive due to a corporate use case of populating both information blocks for detailing remittance advices which are part of value-added service offered by the *Debtor Agent*.

![](_page_91_Picture_11.jpeg)

SCORE Guideline: If the Related Remittance Information is used, and a Remittance Identification is provided, it is recommended that the Remittance Identification equal the End To End Identification.

![](_page_91_Picture_13.jpeg)

The optional *Remittance Information* element within the pain.001 message is nested to provide either *Structured* or *Unstructured* information related to payment, such as invoices.

*Remittance Information* enables the matching/reconciliation of an entry that the payment is intended to settle.

![](_page_92_Picture_3.jpeg)

**Min 0 – Max 1**

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

![](_page_92_Picture_6.jpeg)

The **Structured** element is nested capturing rich structured *Remittance Information,* and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification)

The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-toend transportation of this data.

![](_page_92_Picture_9.jpeg)

*Structured*

requirements on Remittance Information.

The bilaterally/multilaterally agreed *Remittance Information* which is *Structured* must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

![](_page_93_Figure_1.jpeg)

example of *Structured* invoice information

![](_page_93_Figure_3.jpeg)

The *Creditor Remittance Information* is provided to the *Creditor* in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.

> In this example Referred Document Information and its nested elements have multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.

> > *Credit Transfer Transaction Information*

The *Creditor Reference* in the *Creditor Remittance Information* component in the structured remittance information is generated by *Creditor* to inform the *Debtor* who has to include the reference in the Remittance Information component of the pain.001.

Creditor Reference in the Structured Remittance Information is based on ISO 11649

- 2 letters "RF"
- 2 digits check digit
- 21 letters/digits creditor reference

Facilitates STP and auto-match with the creditor reference and its account receivable

- A vendor can add the creditor reference to its invoice. When a customer pays the invoice, they write the creditor reference instead of the invoice number in the payment message (e.g., MT 101 F70 which will be carried in MT 103)
- When the vendor receives the payment, it can auto-match the incoming credit entry and the creditor reference extracted from the statement (e.g., MT 940 F61/86)

![](_page_94_Picture_8.jpeg)

SCORE Guideline: For Creditor Reference information, in instances where the Creditor Reference Type code is SCOR (Structured Communication Reference) and the Creditor Reference is structured in accordance with ISO 11649, the

Use case should be considered as a principal example whereby use case may be cross referenced e.g., a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

### **Interbank Customer Credit Transfer Initiation - Relay**

Use Case pn.1.1.1 – High Level Payment Initiation Interbank 'relay' (pain.001)

Use Case pn.1.1.1.a – High Level Payment Initiation Interbank 'relay' (pain.001) Multi-bank Sweep

Use Case pn.1.1.2 – High Level Payment Initiation Interbank 'relay' (pain.001) involving a Payment Market Infrastructure

### **Interbank Customer Credit Transfer Initiation – Authorised Party**

Use Case pn.1.2.1 – High Level Payment Initiation Interbank (pain.001) by an Authorised Party

Use Case pn.1.2.1.a. – High Level Payment Initiation Interbank (pain.001) FI-Initiated Sweep (Long position at the Secondary Account)

Use Case pn.1.2.1.b. – High Level Payment Initiation Interbank (pain.001) by an Authorised Party to pay themselves as the Creditor

### **Interbank Customer Credit Transfer Initiation – Financial Institution**

Use Case pn.1.3.1 – High Level Payment Initiation Interbank (pain.001) Financial Institution Payment Initiation

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor and initiate a credit transfer.

![](_page_96_Figure_1.jpeg)

settlement in progress) to the

Creditor

In the interbank relay scenario, the Forwarding Agent relaying the pain.001 message to the Debtor Agent(s) in this case to sweep excess cash from the account of the Debtor and consolidate cash for a Corporate.

![](_page_97_Figure_1.jpeg)

Initiating Party sends a payment instruction to the Forwarding Agent to sweep excess funds from its subsidiary's account to the master account with Bank B

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008

Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

Forwarding Agent (F) forwards the payment instruction to the

Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the

Creditor Agent (B) processes the payment and notifies Creditor of a successful sweep through the

### **Market Infrastructure**

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor initiate a credit transfer through a Payment Market Infrastructure.

![](_page_98_Figure_2.jpeg)

In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place between the Debtor and the Debtor Agent

![](_page_99_Figure_1.jpeg)

- As a pre-requisite the Debtor provides Debit Authorisation to Agent A, which allows Agent I to Initiate Payment from their account
- Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

- Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement
- Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

---

