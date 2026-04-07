<!-- ELEMENT ? -->
<span id="page-0-0"></span>This Cross -Border Payment Reporting plus (CBPR+) User Handbook is intended to document and explain a variety of ISO 20022 payment related topics, as well as provide practical use cases to ensure a common understanding and adoption of ISO 20022 within the payment

industry. The SWIFT FINplus service will support CBPR+ messages on the SWIFT network traditionally associated with correspondent banking (many to -many). These messages may be exchanged either between Agents in the same country or between Agents in

-

The use cases focus on a core topics where other relevant messages may also be referred to within the use case, it may also be necessary to consider other documented use cases, in order to capture a wider variation of scenarios.

### Note:

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

## **Table of contents**

- **1. [Introduction to ISO 20022](#page-5-0)**
- **2. [Business Application Header](#page-24-0)**
- **3. [Payment Initiation \(pain\)](#page-38-0)**

```
pain.001 - Interbank Customer Credit Transfer Initiation
```

**pain.002 - [Interbank Customer Payment Status Report](#page-103-0)**

**pain.008 – [Customer Direct Debit Initiation](#page-133-0)**

### **4. [Payment, Clearing and Settlement \(pacs\) messages](#page-181-0)**

```
pacs.002 – Financial Institution to Financial Institution Payment Status Report
```

**pacs.004 – [Payment Return](#page-379-0)**

**pacs.003 – [Financial Institution to Financial Institution Customer Direct Debit](#page-487-0)**

**pacs.008 - [Financial Institution to Financial Institution Customer Credit Transfer](#page-183-0)** 

**pacs.009 (core) - [Financial Institution Credit Transfer](#page-247-0)** 

**pacs.009 (cov) - [Financial Institution 'Cover' Credit Transfer](#page-279-0)**

**pacs.009 (adv) – [Financial Institution 'Advice' Credit Transfer](#page-279-0)** 

## <span id="page-4-0"></span>**Table of contents (continued)**

**[5. Cash Management Reporting \(camt\) messages](#page-527-0)**

**camt.052 - [Bank to Customer Account Report](#page-529-0)**

**camt.053 - [Bank to Customer Statement](#page-535-0)**

**camt.054 - [Bank to Customer Debit Credit Notification](#page-628-0)**

**camt.057 – [Notification to Receive](#page-671-0)**

**camt.058 – [Notification to Receive Cancelation Advice](#page-696-0)** 

**[6. Cash Management Exception & Investigation \(camt\) messages](#page-693-0)**

**camt.029 - [Resolution of Investigation](#page-742-0)**

**camt.055 – [Customer Payment Cancelation Request](#page-772-0)**

**camt.056 - [FI to FI Cancellation Request](#page-794-0)**

#### **[7. Cheques](#page-780-0)**

**camt.107 – [Cheque Presentment Notification](#page-822-0)**

**camt.108 – [Cheque Cancellation or Stop Notification](#page-842-0)**

**camt.109 – [Cheque Cancellation or Stop Report](#page-862-0)**

![](_page_4_Picture_16.jpeg)

## <span id="page-5-0"></span>**Introduction to ISO 20022**

ISO 20022 introduces a fundamental change to the traditional language used by the payments industry for several decades. It also describes participants (i.e., parties) to a business transaction differently based upon the business domain (area) being described, in a similar way you may describe a person as a colleague, parent or sibling depending upon the context you wish to describe them. This section is designed to capture and explain some of the differences.

## **Domains**

### **Payment and Cash Management**

Securities Trade Services Foreign Exchange Card Payment

### **Message Definitions**

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

![](_page_11_Picture_17.jpeg)

**MX message element multiplicity (occurrences)**

#### **Empty XML Elements**

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element.

A common example of this is in payment message is Financial Institution.

| ✓ o Financial Institution Identification  |   |   |  |  |
|-------------------------------------------|---|---|--|--|
| > o BICFI                                 | 0 | 1 |  |  |
| > o Clearing System Member Identification | 0 | 1 |  |  |
| • LEI                                     | 0 | 1 |  |  |
| <ul> <li>Name</li> </ul>                  | 0 | 1 |  |  |
| > o Postal Address                        | 0 | 1 |  |  |
|                                           |   |   |  |  |

Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e., <FinInstnId></FinInstnId>

In the **FINplus** service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where business data should be provided within a nested element, it is provided.

MyStandards describes the element's context by its path whereby each element is divided by a forward slash (/) For example the pacs.008 Town Name within the Debtor Postal Address is described as /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/PstlAdr/TwnNm

Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing the element in an XML naming convention.

For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment Identification is an element below Credit Transfer Transaction Information.

#### *Credit Transfer Transaction Info' Payment Identification*

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

<span id="page-18-0"></span>![](_page_18_Picture_0.jpeg)

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

<span id="page-21-0"></span>![](_page_21_Picture_0.jpeg)

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

## <span id="page-24-0"></span>**Business Application Header**

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

| Message Definition<br>Identifier    | Business Service       | Message Definition<br>Identifier                                                                                                               | Business Service             |  |
|-------------------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|--|
| pain.001.001.09                     | sw ift.cbprplus.02     | camt.058.001.08                                                                                                                                | sw ift.cbprplus.01           |  |
| pain.002.001.10                     | sw ift.cbprplus.02     | camt.060.001.05                                                                                                                                | sw ift.cbprplus.02           |  |
| pain.008.001.03                     | sw ift.cbprplus.01     | camt.107.001.01                                                                                                                                | sw ift.cbprplus.01           |  |
| pacs.002.001.10                     | sw ift.cbprplus.02     | camt.108.001.01                                                                                                                                | sw ift.cbprplus.01           |  |
| pacs.003.001.08                     | sw ift.cbprplus.01     | camt.109.001.01                                                                                                                                | sw ift.cbprplus.01           |  |
| pacs.004.001.09                     | sw ift.cbprplus.02     |                                                                                                                                                |                              |  |
| pacs.008.001.08                     | sw ift.cbprplus.02     |                                                                                                                                                |                              |  |
| pacs.008.001.08<br>(STP/STP EU)     | sw ift.cbprplus.stp.02 | The<br>data<br>represented<br>in<br>the<br>Business<br>Service,<br>together                                                                    |                              |  |
| pacs.009.001.08 (advice)            | sw ift.cbprplus.adv.02 | Message<br>Definition<br>Identifier<br>has<br>a<br>number<br>of<br>roles,                                                                      |                              |  |
| pacs.009.001.08 (core)              | sw ift.cbprplus.02     | routing<br>rules<br>referred<br>to<br>on<br>the                                                                                                | previous<br>page.            |  |
| pacs.009.001.08 (cov)               | sw ift.cbprplus.cov.02 | This<br>data<br>value:                                                                                                                         |                              |  |
| pacs.010.001.03                     | sw ift.cbprplus.02     |                                                                                                                                                |                              |  |
| pacs.010.001.03 (Margin Collection) | sw ift.cbprplus.col.01 | ▪<br>Identifiers<br>explicitly<br>the                                                                                                          | Usage<br>Guideline<br>within |  |
| camt.029.001.09                     | sw ift.cbprplus.02     | guideline.<br>For<br>example<br>an<br>application<br>may<br>have<br>various<br>libraries<br>within<br>a<br>collection,<br>for<br>which<br>only |                              |  |
| camt.052.001.08                     | sw ift.cbprplus.02     | one<br>appropriate<br>to<br>be<br>used<br>to<br>identify<br>data<br>requirements<br>validation.                                                |                              |  |
| camt.053.001.08                     | sw ift.cbprplus.02     |                                                                                                                                                |                              |  |

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

<span id="page-38-0"></span>**pain.001 - [Interbank Customer Credit Transfer initiation](#page-39-0) pain.002 – [Interbank Customer Payment Status Report](#page-103-0) pain.008 – [Customer Direct Debit Initiation](#page-133-0)**

## <span id="page-39-0"></span>**Interbank Customer Credit Transfer Initiation**

![](_page_40_Picture_1.jpeg)

![](_page_40_Picture_2.jpeg)

ISO 20022 message element MT Field Name & (Tag option)

#### *Group Header*

- ➢ *Message Identification*
- ➢ *Initiating Party*  where different from *Debtor*
- ➢ *Forwarding Agent*

#### *Payment Information*

- ➢ *Payment Information Identification*
- ➢ *Requested Execution Date*
- ➢ *Debtor*
- ➢ *Debtor Agent*

#### *Credit Transfer Transaction Information*

- ➢ *Payment Identification*
- ➢ *Amount*
- ➢ *Charge Bearer*
- ➢ *Creditor Agent*
- ➢ *Creditor*

#### **Sequence A –** General Information**:**

- ➢ **Sender's Reference** (Field 20)
- ➢ **Instructing Party** (Field 50 C or L)

#### Message **Sender**in a 'relay' scenario

#### **Sequence A –** General Information**:**

- ➢ **Customer Specified Reference** (Field 21R)
- ➢ **Requested Execution Date** (Field 30)
- ➢ **Ordering Customer** (Field 50 F, G or H)\*
- ➢ **Account Servicing Institution** (Field 52 A or C)\*

#### **Sequence B –** Transaction Details**:**

- ➢ **Transaction Reference** (Field 21)
- ➢ **Currency/Transaction Amount** (Field 32B)
- ➢ **Details of Charges** (Field 71A)
- ➢ **Account With Institution** (Field 57 A, C or D)
- ➢ **Beneficiary** (Field 59 no letter, A or F)

## pain.001 Group Header Payment Information Credit Transfer Transaction Information

#### The pain.001 message is composed of three blocks:

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

## **Group Header**

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

### **pain.001 Interbank Customer Credit Transfer Initiation – Authorisation**

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

### **pain.001 Interbank Customer Credit Transfer Initiation – Number of Transactions**

**Min 1 – Max 1**

The pain.001 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_50_Picture_3.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_50_Picture_5.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

### **pain.001 Interbank Customer Credit Transfer Initiation – Initiating Party**

![](_page_51_Picture_1.jpeg)

For the second and the third use case, BIC of the Initiating Party is required.

#### **Min 1 – Max 1**

The *Initiating Party* can either be the *Debtor* or an Authorised Party who initiates payment transactions on behalf of the *Debtor*. The Initiating Party can be, for example, the Head Office which has the authority to debit the account of its subsidiary. In the centralization model, the *Initiating Party* can also be a payment factory or shared service center or third-party agent, which has authority to send the message on behalf of the *Debtor*.

There are three common use cases in the context of interbank pain.001 message:

- **1. Relay**: The *Initiating Party*, which is either the *Debtor* themselves or authorised party, sends the pain.001 message to the *Forwarding Agent* which acts as a concentrating financial institution. It will forward the pain.001 message to the *Debtor Agent*. This is commonly known as a relay scenario. Whereby the Forwarding Agent is performing a technical role in the payment transaction, they would not be represented in the payment, clearing and settlement message.
- **2. Authorised Party**: The *Initiating Party* is the *Financial Institution* which has the authority to send the pain.001 message on behalf of the *Debtor*, e.g., multi-bank liquidity sweeps.
- **3. Financial Institution Payment Initiation**: The *Initiating Party* is the *Financial Institution* which is the *Debtor* who initiate a payment from their account to move

![](_page_52_Figure_0.jpeg)

## **pain.001 Interbank Customer Credit Transfer Initiation – Forwarding Agent**

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

## **Payment Information**

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

### **pain.001 Interbank Customer Credit Transfer Initiation – Requested Execution Date**

**Min 1 – Max 1**

The pain.001 message mandatory *Requested Execution Date* element, captures the date and time at which the initiating party requests the clearing agent to process the payment.

![](_page_59_Picture_3.jpeg)

It is the date on which the debtor's account is debited. If payment by cheque, the date when the cheque must be generated by the bank. It is defined by either *ISO Date* expressed in the *YYYY-MM-DD format* or *ISO Date Time* below:

- 1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
- 2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
- 3. Local time format YYYY-MM-DDThh:mm:ss.sss

![](_page_59_Picture_8.jpeg)

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2nd option). Otherwise use UTC time (1 st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

### **pain.001 Interbank Customer Credit Transfer Initiation – Pooling Adjustment Date**

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

#### **Min 1 – Max 1**

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

#### **Min 0 – Max 1**

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

### **pain.001 Interbank Customer Credit Transfer Initiation – Charges Account**

**Min 0 – Max 1** The pain.001 optional *Charges Account* element, which is used to process charges associated with a transaction.

![](_page_68_Picture_2.jpeg)

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

![](_page_68_Picture_4.jpeg)

This element is not widely used in the payment industry.

### **pain.001 Interbank Customer Credit Transfer Initiation – Charges Account Agent**

**Min 0 – Max 1**

The pain.001 optional *Charges Account Agent* element, which is used to specify the agent that services a charges account.

![](_page_69_Picture_3.jpeg)

Charges account agent should only be used when the charges account agent is different from the debtor agent.

![](_page_69_Picture_5.jpeg)

This element is not widely used in the payment industry. It should also be noted that the ChargesAccountAgentRule inherited from the base message should be ignored as the optional Branch of DebtorAgent is removed from this Usage Guideline.

## **Credit Transfer Transaction Information**

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

### **pain.001 Interbank Customer Credit Transfer Initiation – Intermediary Agent Account**

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

## **ISO 20022 Programme**

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

#### **Interbank Customer Credit Transfer Initiation - Relay**

Use Case pn.1.1.1 – High Level Payment Initiation Interbank 'relay' (pain.001)

Use Case pn.1.1.1.a – High Level Payment Initiation Interbank 'relay' (pain.001) Multi-bank Sweep

Use Case pn.1.1.2 – High Level Payment Initiation Interbank 'relay' (pain.001) involving a Payment Market Infrastructure

#### **Interbank Customer Credit Transfer Initiation – Authorised Party**

Use Case pn.1.2.1 – High Level Payment Initiation Interbank (pain.001) by an Authorised Party

Use Case pn.1.2.1.a. – High Level Payment Initiation Interbank (pain.001) FI-Initiated Sweep (Long position at the Secondary Account)

Use Case pn.1.2.1.b. – High Level Payment Initiation Interbank (pain.001) by an Authorised Party to pay themselves as the Creditor

#### **Interbank Customer Credit Transfer Initiation – Financial Institution**

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

#### **Market Infrastructure**

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor initiate a credit transfer through a Payment Market Infrastructure.

![](_page_98_Figure_2.jpeg)

<span id="page-99-0"></span>In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place between the Debtor and the Debtor Agent

![](_page_99_Figure_1.jpeg)

- As a pre-requisite the Debtor provides Debit Authorisation to Agent A, which allows Agent I to Initiate Payment from their account
- Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

- Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement
- Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

### position at the Secondary Account)

In the interbank sweep scenario, the Initiating Party (Agent I) initiates the pain.001 message to the Debtor Agent to sweep excess cash from the account of the Debtor and consolidate the cash for a Corporate.

![](_page_100_Figure_2.jpeg)

Agent I receives intraday balance report from Debtor Agent (A) on behalf of their mutual customer.

Agent (I) initiates a sweep on behalf of the Corporate by sending pain.001 to the Debtor

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

Creditor Agent (B) receives credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

![](_page_100_Picture_8.jpeg)

### pay themselves as the Creditor.

In the Authorised Party Initiation scenario, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place to move money to themselves as the Creditor

![](_page_101_Figure_2.jpeg)

- As a pre-requisite the Debtor provides Debit Authorisation to Agent I to Initiate Payment from their account with the Debtor Agent (A)
- Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an authorised party, to

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

### **Payment Initiation**

The Initiating Party (Agent I) initiates a payment from their own account with the Debtor Agent to move the funds to a non-Financial Institution Creditor

![](_page_102_Figure_2.jpeg)

Agent (I), the Debtor, initiates a payment request (pain.001) to the Debtor Agent (A) to move funds from their own account

Debtor Agent (A) debits the account of Agent (I), the Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

Creditor Agent (B) receives credit transfer message, credits the Creditor, and sends the camt.053 (statement) at the end of the business day to the non-FI Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

## <span id="page-103-0"></span>**Interbank Customer Payment Status Report**

### **pain.002**

Group Header

Original Group Information And Status

Original Payment Information And Status

Transaction Information

The pain.002 message is composed of four building blocks:

- *Group Header* which contains a set of characteristics shared by all individual transactions in the message.
- *Original Group Information and Status* contains the group of transactions, to which the status report message refers to.
- *Original Payment Information And Status* contains information about the original payment information, to which the status report message refers.
- *Transaction Information And Status* provides information on the original transactions to which the status report message refers.

It is used to inform the previous party in the payment chain about the positive or negative status of an instruction. It is also used to report on a pending instruction.

![](_page_105_Figure_1.jpeg)

Interbank Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the agents. There are three common use cases:

**Relay**: The pain 002 message is sent by the Debtor Agent to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain 002 message to the Initiating Party.

-----

<span id="page-106-0"></span>![](_page_106_Figure_1.jpeg)

FINplus Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the agents. There are three common use cases:

![](_page_106_Picture_3.jpeg)

**Relay**: The pain 002 message is sent by the Debtor Agent to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain 002 message to the Initiating Party.

![](_page_107_Figure_1.jpeg)

Interbank Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the agents. There are three common use cases:

**3**

*Financial Institution Payment Initiation* (to non-FI) : The pain.002 message is sent by the Debtor Agent to the Debtor (Financial Institution) who requested to initiate a payment from their account with the Debtor Agent to move funds to a non-Financial Institution

![](_page_108_Figure_1.jpeg)

Interbank Customer Direct Debit Initiation message is sent by the Initiating Party to the Forwarding Agent or the Creditor Agent. It is used to request single or bulk collection(s) of funds from one or various debtor's account(s) to a creditor.

**Relay**: Interbank pain.008 message is sent by the Initiating party (the Creditor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.008 message to the Creditor Agent to initiate the direct debit instruction(s).

## **Group Header**

![](_page_110_Picture_1.jpeg)

Each ISO20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Initiation (pain) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

![](_page_110_Picture_4.jpeg)

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

![](_page_110_Picture_6.jpeg)

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor Agent) of the pain.002. **CGI**

The pain.001 message *Creation Date Time* captures the date and time the message was created.

![](_page_111_Picture_2.jpeg)

It is defined by *ISO Date Time* with mandatory date and time components expressed in the following formats:

- 1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
- 2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
- 3. Local time format YYYY-MM-DDThh:mm:ss.sss

![](_page_111_Picture_7.jpeg)

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2nd option). Otherwise use UTC time (1st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

### **pain.002 Interbank Customer Payment Status Report – Initiating Party**

![](_page_112_Picture_1.jpeg)

**Min 1 – Max 1**

The *Initiating Party* in the context of interbank payment initiation report is always the *Debtor Agent* which initiates the pain.002 message. *Business Identifier Code* (BIC FI) is mandated to identify the *Initiating Party* in the pain.002 message. There are three use cases below:

- **1. Relay**: The *Debtor Agent* sends the pain.002 message to the *Forwarding Agent* which acts as a concentrating financial institution. It will forward the pain.002 message to the original *Initiating Party* who can be the *Debtor* themselves or the Authorised Party. This is commonly known as a relay scenario.
- **2. Authorised Party**: The *Debtor Agent* sends the pain.002 to the Financial Institution (*Initiating Party*) which has the authority to initiate a payment on behalf of the *Debtor*, e.g., multi-bank liquidity sweeps
- **3. Financial Institution Payment Initiation**: The *Debtor Agent* sends the pain.002 to the Financial Institution which is the *Debtor* who initiate a payment from their account to move funds to a non-Financial Institution *Creditor*

### **pain.002 Interbank Customer Payment Status Report – Forwarding Agent**

![](_page_113_Picture_1.jpeg)

The *Forwarding Agent* is mandatory in a relay scenario whereby the receiver of the pain.002 message is not the original Debtor. In this case, the *Initiating Party* (the *Debtor Agent*) has to provide *Business Identifier Code* (BIC FI) of the *Forwarding Agent* in the pain.002 message. The Forwarding Agent *acts as a concentrating financial institution and forwards the pain.002 message to the Debtor or the Initiating Party.*  **Min 0 – Max 1**

Other options to identify the *Forwarding Agent* include:

- Clearing System Member ID
- LEI (Legal Entity Identifier)

![](_page_113_Picture_6.jpeg)

![](_page_113_Picture_7.jpeg)

For the use case of multi-bank liquidity sweeps, Forwarding Agent is not required.

## **Original Group Information and Status**

The pain.002 Customer Payment Status Report uses elements in the *Original Group Information and Status* to capture the message identifier and message name of the underlying payment the *Payment Status Report* relates to. The mandatory *Original Message Identification* contains the point-to-point reference, and the mandatory *Original Message Name Identification* contains the message name of the underlying payment being reported upon. Optionally the *Original Creation Date Time* can also be captured. **Min 1 – Max 1**

### For example:

*Original Message Name Identification* "pain.001.001.09" confirms the Status Report is of a pain.001 Customer Credit Transfer Initiation.

![](_page_115_Picture_3.jpeg)

Original Message Identification must transport the Message Identification of the underlying payment (e.g., pain.001).

![](_page_115_Picture_5.jpeg)

For a relay scenario, Forwarding Agent (F) should respect the Message ID provided by the Initiating Party of the pain.001 and pain.002.

![](_page_115_Figure_7.jpeg)

## **Identification**

![](_page_116_Picture_1.jpeg)

![](_page_116_Picture_2.jpeg)

The pain.002 Customer Payment Status Report uses element *Original Payment Information Identification*, located in the Original Group Information and Status. This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group or batch reference if the message contains multiple transactions.

![](_page_116_Picture_4.jpeg)

Since the interbank pain.001 and pain.002 usage guidelines are restricted to one single transaction, this value is the same as the Original Message ID of the Original Group Information And Status.

The pain.002 *Customer Payment Status Report* nested *Transaction Information And Status* element is used to capture information from the underlying payment that the *Payment Status Report* relates to.

![](_page_117_Picture_2.jpeg)

**Mandatory** element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous pages) include:

*Original End to End Identification Original UETR*

**Min 1 – Max 1 Min 1 – Max 1**

The following element is optional:

*Original Instruction Identification*

**Min 0 – Max 1**

These Original elements enable the *Initiating Party* to associate the Payment Status with the payment they originally sent.

![](_page_117_Figure_10.jpeg)

## **Information**

The pain.002 *Customer Payment Status Report Transaction Status* utilizes the externalized ISO *Payment Transaction Status* code list to provide a status update on a pain message previously received. The *Transaction Status* element is arguable the most significant/core parts of the pain.002 and optionally may further be complimented with *Status Reason Information.*

**Min 0 – Max 1**

![](_page_118_Picture_3.jpeg)

The nested *Status Reason Information* enable the optional inclusion of:

*Originator* – the party that issues the status. Typically, the pain.002 Initiating Party and therefore Originator is not necessary.

*Reason* – which utilises an ISO external Status Reason code. For example, **AC04** 'Closed Account Number' would compliment a RJCT (Reject) Transaction Status.

**Min 1 – Max 1**

*Additional Information* – a text element to provide further status reason information, necessary where the *Reason* code is NARR

![](_page_118_Picture_8.jpeg)

Note: A *Reason* code must be provided where the *Transaction Status* RJCT (Reject) code is used.

| Code | Name                        | ISO Definition                                                                                                                                                     | High Level Use Case                                                                                                                                                     |
|------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACCC | AcceptedSettlementCompleted | Settlement on the creditor's account has been completed.                                                                                                           | Sent by Creditor Agent to confirm the settlement on<br>the creditor's account                                                                                           |
| ACCP | AcceptedCustomerProfile     | Preceding check of technical validation was successful. Customer<br>profile check was also successful.                                                             | Sent by any Agent<br>in the payment chain to confirm acceptance prior to<br>technical validation.                                                                       |
| ACFC | AcceptedFundsChecked        | Preceding check of technical validation and customer profile was<br>successful and an automatic funds check was positive.                                          | Sent by any Agent<br>in the payment chain to confirm the technical validation/<br>profile w as positive<br>and automatic funds check w as positive.                     |
| ACIS | AcceptedandChequeIssued     | Payment instruction to issue a cheque has been accepted, and the<br>cheque has been issued but not yet been deposited or cleared.                                  | Sent by any Agent<br>in the payment chain to confirm a cheque has been issued<br>as requested.                                                                          |
| ACSC | AcceptedSettlementCompleted | Settlement has been completed.                                                                                                                                     | Sent by the Any Agent to confirm settlement of a payment message leg.                                                                                                   |
| ACSP | AcceptedSettlementInProcess | All preceding checks such as technical validation and customer<br>profile were successful and therefore the payment initiation has been<br>accepted for execution. | Sent by any Agent to the to confirm the payment is accepted follow ing<br>technical validations being successfully completed.                                           |
| ACTC | AcceptedTechnicalValidation | Authentication and syntactical and semantical validation are<br>successful                                                                                         | Sent by any<br>Agent in the payment chain to the previous Agent to confirm the<br>payment is accepted follow ing technical validations being successfully<br>completed. |
| ACWC | AcceptedWithChange          | Instruction is accepted but a change will be made, such as date or<br>remittance not sent.                                                                         | Sent by any<br>Agent in the payment chain to the previous Agent to confirm the<br>payment is accepted follow ing amendments being made.                                 |
| ACWP | AcceptedWithoutPosting      | Payment instruction included in the credit transfer is accepted<br>without being posted to the creditor customer's account.                                        | Sent by Creditor Agent to the previous<br>Agent to confirm the acceptance of<br>payment w ithout settlement on the creditor's account,                                  |
| CPUC | CashPickedUpByCreditor      | Cash has been picked up by the Creditor.                                                                                                                           | Sent by Creditor Agent to the previous<br>Agent to confirm that<br>the cash<br>collection has been picked up by the Creditor,                                           |
| PDNG | Pending                     | Payment initiation or individual transaction included in the payment<br>initiation is pending. Further checks and status update will be<br>performed.              | Sent<br>by any<br>Agent in the payment chain to the previous Agent as an interim<br>status w hilst other validations are performed.                                     |
| RCVD | Received                    | Payment initiation has been received by the receiving agent.                                                                                                       | Sent by Any Agent to the previous Agent as confirmation that their Customer                                                                                             |

The interbank pain.002 *Customer Payment Transaction Status*  element facilitates updates from the *Debtor Agent* to the previous Agent, e.g., the *Forwarding Agent* or the payment originator (the *Debtor* / the *Initiating Party*) on changes to the status of the payment. Such Status Information messages (pain.002), with the exception of **reject code RJCT** which **is mandatory in CBPR+**, are bilateral agreed, where upon a variety of these Transaction Statuses may be used by the Instructed Agent at different stages of the payment processing.

This diagram illustrates the logical order in which these codes may be used during the processing of the Payment Initiation messages (pain) and the interbank Payment Clearing And Settlement message (pacs) and the role of the Agents in providing these status.

![](_page_120_Figure_2.jpeg)

<span id="page-121-0"></span>Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Interbank Customer Payment Status Report – Relay**

Use Case pn.2.1.1 – High Level Payment Initiation Interbank 'relay' status report

Use Case pn.2.1.1.a – High Level Payment Initiation Interbank 'relay' status report Multi-bank Sweep

Use Case pn.2.1.2 – High Level Payment Initiation Interbank 'relay' status report involving a Payment Market Infrastructure

Use Case pn.2.1.3 – High Level Direct Debit Initiation Interbank 'relay' status report involving a Payment Market Infrastructure

#### **Interbank Customer Payment Status Report – Authorised Party**

Use Case pn.2.2.1 – High Level Payment Initiation Interbank status report for Authorised Party

Use Case pn.2.2.1.a. – High Level Payment Initiation Interbank status report for FI-Initiated Sweep (Long position at the Secondary Account)

Use Case pn.2.2.1.b. – High Level Payment Initiation Interbank status report for Authorised Party to pay themselves as the Creditor.

#### **Interbank Customer Payment Status Report – Financial Institution**

Use Case pn.2.3.1 – High Level Payment Initiation Interbank status report for Financial Institution Payment Initiation

#### **Interbank multiple Payment Status Reports**

Use Case pn.2.4.1 – High Level Payment Initiation Interbank 'relay' multiple status reports

Use Case pn.2.4.2 – High Level Rejection of an incomplete 'relay' Payment

Use Case pn.2.4.3 – High Level Direct Debit Initiation Interbank 'relay' multiple status reports involving a Payment Market Infrastructure

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

![](_page_122_Figure_1.jpeg)

settlement in progress) to the

Creditor, and sends a camt.053

### **Multi-bank Sweep**

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

![](_page_123_Figure_2.jpeg)

Initiating Party sends a payment instruction to the Forwarding Agent to sweep excess funds from its subsidiary's account to the master account with Bank B

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008

Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

Forwarding Agent (F) forwards the payment instruction to the

Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the

Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a

### a Payment Market Infrastructure

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

![](_page_124_Figure_2.jpeg)

## <span id="page-125-0"></span>**involving a Payment Market Infrastructure**

In the interbank relay scenario, the Creditor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

![](_page_125_Figure_2.jpeg)

### **Party**

In the scenario Authorised Party Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a payment based on Debit Authorisation with the Debtor and the Debtor Agent.

![](_page_126_Figure_2.jpeg)

- As a pre-requisite the Debtor provides Debit Authorisation to Agent I to Initiate Payment from their account with the Debtor Agent (A)
- Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

Creditor Agent (B) receives credit transfer message, credits the Creditor and optionally provided a status report to Debtor Agent based upon a bilateral agreement. It also sends the result of the sweep by camt.052 (intraday sweep) and or camt.053 (statement) to the Corporate

### Party: FI-Initiated Sweep (Long position at the Secondary Account)

In the scenario Authorised Party Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a liquidity sweep on behalf of a corporate customer based on the sweep contract

![](_page_127_Figure_2.jpeg)

- Agent I receives intraday balance report from the Debtor Agent (A) on behalf of their mutual customer
- Agent (I) initiates a sweep on behalf of the Corporate by sending pain.001 to the Debtor

- Debtor Agent (A) debits the account of Debtor and initiates a credit transfer
- Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement
- Creditor Agent (B) receives credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

![](_page_127_Figure_8.jpeg)

### Party to pay themselves as the Creditor

In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place to move money to themselves as the Creditor

![](_page_128_Figure_2.jpeg)

- As a pre-requisite the Debtor provides Debit Authorisation to Agent I to Initiate Payment from their account with the Debtor Agent (A)
- Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an authorised party, to

- Debtor Agent (A) debits the account of Debtor and initiates a credit transfer
- Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the Debtor Agent based upon a bilateral agreement

### **Institution Payment Initiation**

In the scenario Financial Institution Payment Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a payment to a non-Financial Institution Creditor using their own account

![](_page_129_Figure_2.jpeg)

Agent (I), the Debtor, initiates a payment request (pain.001) to the Debtor Agent (A) to move funds from their own account

Debtor Agent (A) debits the account of Agent (I), the Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

Creditor Agent (B) receives credit transfer message, credits the Creditor, and optionally returns a status report to Debtor Agent based upon a bilateral agreement. It also sends camt.053 (statement) to the non-FI Creditor

In the interbank relay scenario, the Forwarding Agent provides multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle.

![](_page_130_Figure_1.jpeg)

Initiating Party sends a payment instruction to the Forwarding Agent

Forwarding Agent (F) forwards the payment instruction to the Debtor Agent (A)

Debtor Agent (A) optionally provides a status update ACTC (accepted technical validations are successful) to the Forwarding Agent (F), based upon a bilateral agreement.

Forwarding Agent (F) relays the

Debtor Agent (A) processes the payment and sends to the Creditor Agent (B)

Debtor Agent (A) optionally provides a further status update ACSP (accepted settlement in progress) to the Forwarding Agent

Forwarding Agent (F) relays a further status update ACSP (accepted settlement in progress), to the Initiating Party, based upon a bilateral agreement.

Creditor Agent (B) processes the

In the interbank relay scenario, the Forwarding Agent provides multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle.

![](_page_131_Figure_1.jpeg)

- Initiating Party sends a payment instruction to the Forwarding Agent
- Forwarding Agent (F) relays the payment to the Debtor Agent (A)
- Debtor Agent (A) processes the payment and sends to the Creditor Agent (C)
- Debtor Agent (A) optionally provides a status update ACSP

- Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement.
- Having received the payment the Creditor Agent recognises the payment

- Debtor Agent refund the Debtor's account and update the status RJCT with the reason code to the Forwarding Agent
- Forwarding Agent (F) relays a further status update RJCT with

### <span id="page-132-0"></span>(pain.002) involving a Payment Market Infrastructure

In the interbank relay scenario, the Creditor Agent sends multiple status reports to the Forwarding Agent which relays the same information to the Initiating Party.

![](_page_132_Figure_2.jpeg)

## <span id="page-133-0"></span>**Interbank Customer Direct Debit Initiation**

![](_page_134_Picture_2.jpeg)

![](_page_134_Picture_3.jpeg)

ISO 20022 message element MT Field Name & (Tag option)

#### *Group Header*

- ➢ *Message Identification*
- ➢ *Initiating Party*  where different from *Creditor*
- ➢ *Forwarding Agent*

### *Payment Information*

- ➢ *Payment Information Identification*
- ➢ *Requested Collection Date*
- ➢ *Creditor*
- ➢ *Creditor Agent*

### *Direct Debit Transaction Information*

- ➢ *Payment Identification*
- ➢ *Instructed Amount*
- ➢ *Charge Bearer*
- ➢ *Mandate Identification*
- ➢ *Debtor Agent*
- ➢ *Debtor*

#### **Sequence A –** General Information**:**

- ➢ **Sender's Reference** (Field 20)
- ➢ **Instructing Party** (Field 50 C or L)

### Message **Sender**in a 'relay' scenario

#### **Sequence A –** General Information**:**

- ➢ **Customer Specified Reference** (Field 21R)
  - ➢ **Requested Execution Date** (Field 30)
  - ➢ **Creditor** (Field 50 A or K)\*
  - ➢ **Creditor's Bank** (Field 52 A, C or D)\*

### **Sequence B –** Transaction Details**:**

- ➢ **Transaction Reference** (Field 21)
- ➢ **Currency and Transaction Amount** (Field 32B)
- ➢ **Details of Charges** (Field 71A)
- ➢ **Mandate Reference** (Field 21C)
- ➢ **Debtor's Bank** (Field 57 A, C or D)
- ➢ **Debtor**(Field 59 no letter or A)

![](_page_135_Picture_0.jpeg)

The pain.008 message is composed of three blocks:

- *Group Header* contains a set of characteristics that relates to all individual transaction.
- *Payment Information* contains a set of characteristics that relates to the credit side of the transaction, such as Creditor and Creditor Agent.
- *Direct Debit Transaction Information* contains, among others, elements related to the debit side of the transaction, such as Debtor and Debtor Agent and optionally mandate related information.

![](_page_135_Picture_5.jpeg)

Direct Debit Initiation relay messages in a many-to-many space allow for multiple transactions as they will be typically cleared by Automated Clearing House (ACH) batch processing system.

![](_page_136_Figure_1.jpeg)

Interbank Customer Direct Debit Initiation message is sent by the Initiating Party to the Forwarding Agent or the Creditor Agent. It is used to request single or bulk collection(s) of funds from one or various debtor's account(s) to a creditor.

**Relay**: Interbank pain.008 message is sent by the Initiating party (the Creditor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.008 message to the Creditor Agent to initiate the direct debit instruction(s).

## **Group Header**

![](_page_138_Picture_1.jpeg)

Each ISO20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For the Payment Initiation (pain) messages the *Message Identification* has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

![](_page_138_Picture_4.jpeg)

Each transaction's *Direct Debit Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

![](_page_138_Picture_6.jpeg)

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Creditor or authorized third party) of the pain.008.

**Min 1 – Max 1**

**pain.008 Interbank Customer Direct Debit Initiation – Creation Date Time**

**Min 1 – Max 1**

The pain.008 message *Creation Date Time* captures the date and time which the message was created.

![](_page_139_Picture_3.jpeg)

It is defined by *ISO Date Time* with mandatory date and time components expressed in the following formats:

- 1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
- 2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
- 3. Local time format YYYY-MM-DDThh:mm:ss.sss

![](_page_139_Picture_8.jpeg)

Unlike other CBPR+ messages, the interbank pain.008 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2nd option). Otherwise use UTC time (1st option). Decimal fractions of milliseconds with 3 digits are optional.

### **pain.008 Interbank Customer Direct Debit Initiation – Authorisation**

**Min 0 – Max 2**

The pain.008 message *Authorisation* allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The *Authorisation* uses an embedded code set or free text form. It has no equivalent in the legacy MT direct debit message.

| Code | Description                      | Description                                                                                                                          |
|------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ILEV | Instruction Level Authorisation  | File<br>requires all customer transactions to be authorised or approved.                                                             |
| FDET | File Level Authorisation Details | Additional file level approval, with the ability to view<br>both the payment information block<br>and supporting transaction detail. |
| FSUM | File Level Authorisation Summary | Additional<br>file level approval, with the ability to view only the payment information block.                                      |
| AUTH | PreAuthorised File               | File has been pre-authorised or approved within the originating customer environment<br>and no further approval is required.         |

![](_page_140_Picture_3.jpeg)

For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.

### **pain.008 Interbank Customer Direct Debit Initiation – Number of Transactions**

**Min 1 – Max 1**

The pain.008 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_141_Picture_3.jpeg)

Multiple transactions are allowed in CBPR+ direct debit usage guidelines. However, it is recommended to have only one single direct debit transaction unless bilaterally determined.

![](_page_141_Picture_5.jpeg)

Single transactions in the CBPR+ direct debit usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant collection, supporting the next generation of innovation.

### **pain.008 Interbank Customer Direct Debit Initiation – Initiating Party**

![](_page_142_Picture_1.jpeg)

**Min 1 – Max 1**

The *Initiating Party* can either be the *Creditor* or an AuthorisedParty who initiates direct debit transactions on behalf of the *Creditor*. The Initiating Party can be, for example, the Head Office which is authorised by its subsidiary to request for payment amount to be collected from the *Debtor*. In the centralization model, the *Initiating Party* can also be a payment factory or shared service centre or third party agent, which has authority to send the message on behalf of the *Creditor*.

In the interbank pain.008 'Relay' message use case: The *Initiating Party* sends the pain.008 message to the *Forwarding Agent* which acts as a concentrating financial institution. It will forward the pain.008 message to the *Creditor Agent*.

![](_page_142_Picture_5.jpeg)

Initiating Party has a mandate (debit authority agreement) to debit the account of the Debtor.

![](_page_143_Figure_0.jpeg)

### **pain.008 Interbank Customer Direct Debit Initiation – Forwarding Agent**

![](_page_144_Picture_1.jpeg)

The *Forwarding Agent* is mandatory in a relay scenario whereby the *Initiating Party* (the *Creditor* or authorised third party) has to provide *Business Identifier Code* (BICFI) of the *Forwarding Agent* in the pain.008 message. The Forwarding Agent acts as a concentrating financial institution and forwards the pain.008 message to the *Creditor Agent* for execution. **Min 1 – Max 1**

Other options to complement the identity of the *Forwarding Agent* include:

- Clearing System Member ID
- LEI (Legal Entity Identifier)

![](_page_144_Figure_6.jpeg)

## **Payment Information**

<span id="page-146-0"></span>The CBPR+ pain.008 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognise that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory.

As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message.

Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used.

![](_page_146_Figure_3.jpeg)

The Interbank Customer Direct Debit Initiation *Payment Information Identification* provides a mandatory element to identify the payment information group within the message.

![](_page_147_Picture_2.jpeg)

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions.

![](_page_147_Picture_4.jpeg)

For a single batch in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header.

The pain.008 message *Payment Method* specifies the means of payment that will be used to move the amount of money. The payment method code "DD" Direct Debit must be used.

![](_page_148_Picture_2.jpeg)

| Code | Name         | Definition                                                                                                                                    |
|------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| DD   | Direct Debit | Collection of an amount of money from the Debtor's<br>bank account by the Creditor. The amount of money<br>and dates of collections may vary. |

#### **Min 0 – Max 1**

The pain.008 message *Batch Booking* identifies whether a single entry per individual transaction or a batch entry for the sum of the amounts of all transactions within the group of a message is requested.

![](_page_149_Picture_2.jpeg)

Batch booking is used to request for a consolidated credit entry on the Creditor's account. Where this optional element is not used, the default of single credit entries is applied on the Creditor's account.

**pain.008 Interbank Customer Direct Debit Initiation – Requested Collection Date**

**Min 1 – Max 1**

The pain.008 message mandatory *Requested Collection Date* element, captures the date at which the creditor requests that the amount of money is to be collected from the debtor.

![](_page_150_Picture_3.jpeg)

It is defined by *ISO Date* expressed in the *YYYY-MM-DD format*. **10**

The ISO 20022 pain messages describe the *Creditor* as the party whose account was credited for a transaction. The *Creditor* sub elements describe the *Creditor* in greater detail. **Min 1 – Max 1**

Mandatory *Name* (where a BIC identifier is not provided) by which the party is known

> *Postal Address*

*Name*

![](_page_151_Figure_3.jpeg)

Nested element capturing either structured or unstructured *Creditor* address details. Note: Structured address is

![](_page_151_Picture_5.jpeg)

strongly recommended with mandatory Town Name and Country

*Identification* Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Optional element to

*Creditor*

*Country of Residence* capture the *Creditor*'s ISO country code of residence

#### **Min 1 – Max 1**

The pain.008 *Creditor Account* is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

> The *Creditor Account* uses a variety of nested elements to capture information related to the account.

![](_page_152_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account *Currency* identifies the currency of the account, recommended. **Min 0 – Max 1 Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

![](_page_152_Picture_8.jpeg)

Indication of Currency of the Creditor Account is recommended in case of multi-currency accounts

**Min 1 – Max 1**

The *Creditor Agent* is a static role in the pain.008 Customer Direct Debit Initiation. This agent maintains a relationship with their customers, the *Creditor*.

![](_page_153_Picture_2.jpeg)

![](_page_153_Picture_3.jpeg)

Note: Although the *Creditor Agent, Debtor Agent, Creditor and Debtor* all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Creditor Agent and Debtor Agent become the Statement Account Servicer and the Creditor and the Debtor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

![](_page_153_Picture_5.jpeg)

**Min 0 – Max 1**

**Min 0 – Max 1 Min 0 – Max 1**

**Min 0 – Max 1**

The pain.008 *Creditor Agent Account* is used to capture the account information related to the Creditor Agent.

**pain.008 Interbank Customer Direct Debit Initiation – Creditor Agent Account**

The *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

![](_page_154_Picture_3.jpeg)

**Min 1 – Max 1** *Identification*identifies the account maintained at theAccount Servicing Institution

*Type* uses the external CashAccount Type code list to identify the type of account

*Currency* identifies the currency of the account

*Name* identifies the name of the account as assigned by theAccount Servicing Institution **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_154_Picture_9.jpeg)

Creditor Agent and Debtor Agent are Financial Institutions, therefore the nested elements *Name* and *Proxy* are unlikely to be used.

### **pain.008 Interbank Customer Direct Debit Initiation – Charges Account**

**Min 0 – Max 1** The pain.008 optional *Charges Account* element, which is used to process charges associated with a transaction.

![](_page_155_Picture_2.jpeg)

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

![](_page_155_Picture_4.jpeg)

This element is not widely used in the payment industry.

### **pain.008 Interbank Customer Direct Debit Initiation – Charges Account Agent**

**Min 0 – Max 1**

The pain.008 optional *Charges Account Agent* element, which is used to specify the agent that services a charges account.

![](_page_156_Picture_3.jpeg)

Charges account agent should only be used when the charges account agent is different from the creditor agent.

![](_page_156_Picture_5.jpeg)

This element is not widely used in the payment industry.

## **Direct Debit Transaction Information**

The pain.008 message contains *Payment Identification* which provides a set of elements to identify the payment of which several are mandatory elements.

![](_page_158_Figure_2.jpeg)

a point-to-point reference of 35 characters long will be returned

to account statements if provided by the initiating party.

*Information*

i

*Purpose* 

The pain message *Payment Type Information* provides a set of optional elements where the payment type can be described.

*Instruction Priority*  **Min 0 – Max 1**

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the

processing

*Service Level*  **Min 0 – Max 3** Anested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

*Payment Type Local Instrument*  **Min 0 – Max 1**

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, CORE is a transaction related to SEPADirect Debit Core.

![](_page_159_Picture_8.jpeg)

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

A nested element which uses an embedded code to identify the direct debit sequence, such as first, recurrent, final or one-off

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. *Category* 

*Sequence Type* **Min 0 – Max 1**

*Direct Debit Transfer Transaction Information*

### **pain.008 Interbank Customer Direct Debit Initiation – Instructed Amount**

**Min 1 – Max 1**

The pain.008 nested *Instructed Amount* element captures the amount of money to be moved between the Debtor and the Creditor before deduction of charges.

![](_page_160_Picture_2.jpeg)

![](_page_160_Picture_3.jpeg)

![](_page_160_Picture_4.jpeg)

![](_page_160_Picture_5.jpeg)

*Amount*

The *Instructed Amount* captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. This amount has to be transported unchanged through the transaction chain. This element is comparable with both the legacy Field 33B and Field 32B.

![](_page_160_Picture_7.jpeg)

For multiple transactions, the currency must be the same for each transaction.

#### **Min 0 – Max 1**

The *Charge Bearer* element exists at the Direct Debit Transaction Information level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

![](_page_161_Figure_2.jpeg)

![](_page_161_Picture_3.jpeg)

Charge Bearer Code SLEV (Following Service Level) is not allowed in the CBPR+ pain.008 interbank.

![](_page_162_Figure_0.jpeg)

#### **Min 0 – Max 1**

The *Creditor Scheme Identification* element within the pain.008 message optionally provides information related to the credit party that signs the mandate who is different from the Creditor.

![](_page_163_Picture_2.jpeg)

The *Creditor Scheme Identification* element offers the following options:

Name

Postal Address: Not used often

Identification

Country of Residence

Contact Details

![](_page_163_Picture_9.jpeg)

CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit Scheme.

The pain.008 message introduces *Ultimate Creditor* and *Ultimate Debtor*. The *Ultimate Creditor* element should not be confused with an *Initiating Party* who may send a direct debit initiation request on behalf of the *Creditor,* for example, Payment Factory.

CBPR+ premise is that an *Ultimate Creditor* has no financial regulated direct account relationship with the corresponding Creditor. Likewise, an *Ultimate Debtor* has no financial regulated account relationship with the corresponding Debtor.

The *Ultimate Creditor* and *Ultimate Debtor* can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

![](_page_164_Picture_4.jpeg)

In the context of direct debit, *Ultimate Creditor* and *Ultimate Debtor* are not commonly used.

**Min 0 – Max 1 Min 0 – Max 1**

Min 1 - Max 1

The **Debtor Agent** is a static roles in the pain.008 Customer Direct Debit Initiation. This agent maintain a relationship with their customers, the **Debtor**.

![](_page_165_Picture_2.jpeg)

![](_page_165_Picture_3.jpeg)

Note: Although the *Debtor Agent, Creditor Agent, Debtor and Creditor* all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

**Min 0 – Max 1**

**Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1**

The pain.008 *Debtor Agent Account* is used to capture the account information related to the *Debtor Agent*.

**pain.008 Interbank Customer Direct Debit Initiation – Debtor Agent Account**

The *Debtor Agent Account* uses a variety of nested elements to capture information related to the account.

![](_page_166_Picture_3.jpeg)

**Min 1 – Max 1** *Identification*identifies the account maintained at theAccount Servicing Institution **Min 0 – Max 1**

*Type* uses the external CashAccount Type code list to identify the type of account

*Currency* identifies the currency of the account

*Name* identifies the name of the account as assigned by theAccount Servicing Institution *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_166_Picture_8.jpeg)

The ISO 20022 pain messages describes the *Debtor* as the party whose account was debited for a transaction. The *Debtor* sub elements describe the *Debtor* in greater detail. *Debtor Name Name* by which the party is known *Identification* Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. *Country of Residence* Optional element to capture the *Debtor*'s ISO *Postal Address* Nested element capturing either structured or unstructured *Debtor* address details. Note: Structured address is strongly recommended with mandatory Town Name and Country **Min 1 – Max 1** Note: it is recommended to include the Postal Address together with the Name

country code of residence

**Min 0 – Max 1**

The pain.008 *Debtor Account* is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

> The *Debtor Account* uses a variety of nested elements to capture information related to the account.

![](_page_168_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency of the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

The pain.008 message introduces *Ultimate Debtor* and *Ultimate Creditor*. The *Ultimate Debtor* element should not be confused with an *Initiating Party* who may send a payment initiation request on behalf of the *Debtor,* for example, Payment Factory.

CBPR+ premise is that an *Ultimate Debtor* has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an *Ultimate Creditor* has no financial regulated account relationship with the corresponding Creditor.

The *Ultimate Debtor* and *Ultimate Creditor* can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

![](_page_169_Picture_4.jpeg)

In the context of direct debit, Ultimate Creditor and Ultimate Debtor are not commonly used.

**Min 0 – Max 1 Min 0 – Max 1**

The *Instruction for Creditor Agent* element within the pain.008 message optionally provides information related to the processing of the direct debit.

![](_page_170_Picture_2.jpeg)

The *Instruction for Creditor Agent* element offers a maximum of 140 characters to provide further information related to the processing of the direct debit instruction, that may need to be acted upon by the *Creditor Agent*, depending on bilateral agreement.

**Min 0 – Max 1**

The *Purpose* element within the pain.008 message captures the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment, e.g., IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the *Debtor*.

![](_page_171_Picture_3.jpeg)

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. For example, LOAR is classified within the Finance categorisation, with the *Name* Loan Repayment described as a repayment of loan to lender.

![](_page_171_Picture_5.jpeg)

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. *Category Purpose* code RPRE 'Represented' may trigger a representation of previously reversed or returned direct debit transactions.

The *Regulatory Reporting* block within the pain.008 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

**Min 0 – Max 1**

The *Debit Credit Reporting Indicator* utilises an embedded choice of code to indicate whether the regulatory reporting applies to the:

- DEBT (debit)
- CRED (credit)
- BOTH

![](_page_172_Picture_7.jpeg)

**Min 0 – Max 1**

The *Authority* element captures the *Name* and *Country* code of the Authority/Entity requiring the regulatory reporting information.

**Min 0 – Max \***

The *Details* element provides the detail on the regulatory reporting information.

![](_page_172_Picture_12.jpeg)

![](_page_172_Picture_13.jpeg)

**Min 0 – Max 1**

The pain.008 nested *Tax* element captures information related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s).

This element caters for two main types of tax related payments:

- Tax payment obligation that is required to be transmitted with a payment
- Information that accompanies an actual payment of a tax obligation The follow nested elements may be used to capture detailed tax information:

![](_page_173_Picture_5.jpeg)

![](_page_173_Figure_6.jpeg)

![](_page_173_Picture_7.jpeg)

Tax information block is also available within the Structured Remittance Information block which is applicable when tax information is used by the creditor as part of remittance information. *Direct Debit Transaction Information*

**Min 0 – Max 10**

The *Related Remittance Information* element within the pain.008 message is nested to provide information related to the handling of remittance information.

**Min 0 – Max 1**

The *Remittance Identification* captures a unique reference assigned by the initiating party of the direct debit to identify the remittance information sent separately from the direct debit instruction.

**Min 0 – Max \***

The *Remittance Location Details* uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- *Method* requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email)
- *Electronic Address* provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information maybe deposited or retrieved.
- *Postal Address* provides the postal address to which an agent is to send the remittance information

![](_page_174_Picture_9.jpeg)

Unlike CBPR+ pacs messages, in the interbank pain.008 message, Related Remittance Information and Remittance Information are non-mutually exclusive due to a corporate use case of populating both information blocks for detailing remittance advices which are part of value-added service offered by the *CreditorAgent*.

![](_page_174_Picture_11.jpeg)

The optional *Remittance Information* element within the pain.008 message is nested to provide either *Structured* or *Unstructured* information related to payment, such as invoices.

*Remittance Information* enables the matching/reconciliation of an entry that the payment is intended to settle.

![](_page_175_Picture_3.jpeg)

**Min 0 – Max 1**

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

**Min 0 – Max \***

The **Structured** element is nested capturing rich structured *Remittance Information,* and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification)

The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-toend transportation of this data.

The bilaterally/multilaterally agreed *Remittance Information* which is *Structured* must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

![](_page_176_Figure_1.jpeg)

example of *Structured* invoice information

![](_page_176_Figure_3.jpeg)

The *Creditor Remittance Information* is provided by the *Creditor* in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.

> In this example Referred Document Information and its nested elements have multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.

The *Creditor Reference* in the *Creditor Reference Information* component in the structured remittance information is generated by *Creditor* to allow for the identification of the underlying documents and enable reconciliation by the Creditor upon receipt of the amount of money.

Creditor Reference in the Structured Remittance Information can be based on ISO 11649

- 2 letters "RF"
- 2 digits check digit
- 21 letters/digits creditor reference

By providing the Creditor Reference in the pain.008, such as invoice number for collection, it will facilitate STP and auto-match the incoming credit entry. The Creditor Reference can be extracted from the statement (e.g., camt.053 Structured Remittance information within the Transaction Details or MT 940 Field 61 or Field 86).

Equally the End-To-End Identification could perform a similar function

![](_page_177_Picture_7.jpeg)

Use case should be considered as a principle example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Interbank Customer Direct Debit Initiation - Relay**

Use Case pn.8.1.1 – High Level Direct Debit Initiation Interbank 'relay' (pain.008)

Use Case pn.8.1.2 – High Level Direct Debit Initiation Interbank 'relay' (pain.008) involving a Payment Market Infrastructure

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collections of funds from the debtor's accounts for a creditor.

![](_page_179_Figure_1.jpeg)

## **Payment Market Infrastructure**

Creditor Agent (A)

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collection of funds from the debtor's accounts for a creditor (through a Payment Market Infrastructure).

![](_page_180_Figure_2.jpeg)

settlement in progress) to the Forwarding Agent (F), based upon

Payment Market Infrastructure (PMI) and debits the account of the

## <span id="page-181-0"></span>**Payment, Clearing and Settlement (pacs) messages**

![](_page_182_Picture_0.jpeg)

#### <span id="page-182-0"></span>**Payments**

**pacs.008** - [Financial Institution to Financial Institution Customer Credit Transfer](#page-183-0)

**pacs.009** - [Financial Institution Credit Transfer](#page-247-0)

**pacs.009 (cov)**- [Financial Institution 'Cover' Credit Transfer](#page-247-0)

**pacs.009 (adv) –** [Financial Institution 'advice' of Credit Transfer](#page-279-0)

### **Payment Rejection and Return**

**pacs.002** – [Financial Institution To Financial Institution Payment Status Report](#page-346-0)

**pacs.004** – [Payment Return](#page-379-0)

#### **Direct Debit Payments**

**pacs.010** - [Interbank Direct Debit](#page-425-0)

**pacs.010 (col) -** [Interbank Direct Debit Margin Collection](#page-456-0)

**pacs.003** - [Financial Institution to Financial Institution Customer Direct Debit](#page-487-0)

<span id="page-183-0"></span>**Financial Institution to Financial Institution Customer Credit Transfer** **pacs.008** Group Header Credit Transfer

The pacs.008 has two core sets of nested elements:

- *Group Header* which contains a set of characteristics that relates to all individual transaction
- *Credit Transfer Transaction Information* which contains elements providing information specific to the individual credit transfer transaction.

![](_page_184_Picture_4.jpeg)

Transaction Information Payment messages in a many-to-many payment are considered as a single transaction.

![](_page_185_Figure_0.jpeg)

The Financial Institution To Financial Institution Customer Credit Transfer message is sent by the Debtor Agent to the Creditor Agent, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a Debtor account to a

## **Group Header**

![](_page_187_Picture_0.jpeg)

![](_page_187_Picture_1.jpeg)

Each ISO 20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

![](_page_187_Picture_4.jpeg)

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference)

The pacs.008 message *Creation Date* captures the date and time which the message was created.

![](_page_188_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_188_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The pacs.008 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_189_Picture_2.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_189_Picture_4.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

**Min 1 – Max 1**

The pacs.008 *Settlement Method* element within the Group Header *Settlement Information*, includes one of the embedded codes to indicate how the payment message will be settled.

The *Settlement Method element* in the pacs.008 allows a choice of an embedded code.

![](_page_190_Picture_3.jpeg)

**COVE** indicate this Customer Credit Transfer will be settlement using a covering pacs.009 (COV). The Agents being used in the covering payment to reimburse the Instructed Agent can be provided in the dedicated Reimbursement Agent elements. This allows the Instructed Agent to identify the debit account on their books from the Reimbursement Agent account or look up the account related to the reimbursement agent.

**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated *Settlement Account* element.

**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated *Settlement Account*  element.

![](_page_190_Picture_7.jpeg)

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification (HVPS+)

![](_page_191_Picture_0.jpeg)

The pacs messages introduce the **Settlement Method** element within the Group Header **Settlement Information**. Settlement refers to the Agent whose role is to act as an Account Servicing Institution i.e. owns the account and provides service to the customer (Account Owner).

The Account Owner can be an Agent or another Party.

Traditionally an interbank account relationship may have been referred to as a Nostro/Vostro relationship or an Agent's account held on another Agent's books/ another Agent's account held on my books.

Typically the commonality of this can be simplified to the Agent who provides the official Account statement is servicing the account and therefore is the Agent responsible for performing the settlement.

### Why is it so important to understand which Agent Services the account?

In ISO 20022, much like the legacy FIN process, each leg of a payment has a settlement component. Commonly one of these settlement legs occurs over a Market Infrastructure, who typically owns or instructs the settlement between the two Market Infrastructure participant Agents at a national Central Bank. In this case the Central Bank services both the Instructing Agent and Instructed Agent accounts which is represented by **CLRG** in the Settlement Method of a pacs message. In a number of business Use Cases there are examples of additional legs, which may occur prior to or after a potential Market

Infrastructure, where an Agent is responsible for the role to service an account and perform settlement of that leg.

![](_page_192_Figure_0.jpeg)

If we simplify a point-to-point message leg and look at when it is settled (booked using traditional language) we can ask ourselves: is the Instructing Agent's account held (serviced) on the books of the Instructed Agent or is the Instructing Agent holding (servicing) the account of the Instructed Agent.

Depending on the answer to this question, this determines the Settlement Method in a serial payment process.

Where the **IN**structin**G** Agent services the account and is responsible for settling the payment leg, the Settlement Method code **INGA** is used.

Where the **IN**structe**D** Agent services the account and is responsible for settling the payment leg, the Settlement Method code **INDA** is used.

![](_page_192_Figure_5.jpeg)

The relationship between the settlement of a payment leg and the message process flow is an important one. The state of settlement influences further messages in the process flow.

![](_page_193_Picture_1.jpeg)

The pacs message sent by the Instructing Agent to the Instructed Agent has already been settled.

- **Instructing Agent** may (for example) send
  - a pacs.002 to the Previous Agent with status ACSC Accepted Settlement Complete.
  - a camt.053 Customer Statement to the Instructed Agent (as Account Owner)

**Instructed Agent** can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the Instructed Agent must result in a pacs.004 Payment Return (which in turn triggers a Reverse Indicator on the Account Owners statement). **Creditor Agent** having performed the settlement on the Creditor's account, camt reporting message may be used to report or notify on this credit entry.

![](_page_193_Picture_7.jpeg)

The pacs message sent by the Instructing Agent to the Instructed Agent has not been settled.

**Instructing Agent** may (for example) send

• a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress

#### **Instructed Agent** may

- Reject the pacs message received, using a pacs.002, as it has not been settled.

• a camt.053 Customer Statement to the Instructing Agent (as Account Owner) Although an rejected entry will not appear in the camt.053 **Creditor Agent** of a pacs.009 (particularly in the cover scenario) may forward the pacs.009 to the Creditor, as the Creditor will perform the settlement (they are the Account Servicing Institution)

![](_page_193_Picture_15.jpeg)

The pacs message sent by the Instructing Agent to the Instructed Agent has not been settled. Settlement is performed by the Market Infrastructure. **Instructing Agent** may (for example) send

• a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress

#### **Instructed Agent** may

• can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the Instructed Agent must result in a pacs.004 Payment Return.

**Market Infrastructure** may

![](_page_194_Figure_0.jpeg)

![](_page_195_Figure_0.jpeg)

The pacs.008 message *Settlement Account* is a nested element as part of *Settlement Information,* this element identifies information related to an account used to settle the payment instruction.

**Min 0 – Max 1**

The *Settlement Account* identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the *Settlement Method*)

![](_page_196_Picture_3.jpeg)

**Min 0 – Max 1**

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account

*Currency* identifies the currency if the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

The pacs message captures a number of Reimbursement Agents as a sub element to *Settlement Information* these elements detail the Agent in the cover method who will process the pacs.009 cover.

These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as The *Instructing Reimbursement Agent, Instructed Reimbursement Agent* and *Third Reimbursement Agent.* Each of these reimbursement agents also has a dedicated account element to optionally capture their related account details.

![](_page_197_Picture_2.jpeg)

#### **Min 0 – Max 1**

The *Instructing Reimbursement Agent* captures the Agent who will execute a covering payment (i.e. pacs.009 COV or domestic equivalent) often referred to as the currency correspondent. This optional element is comparable with the Field 53a in the legacy FIN message.

**Min 0 – Max 1**

The *Instructing Reimbursement Agent Account* captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 53.

**Min 0 – Max 1**

![](_page_198_Picture_1.jpeg)

The *Instructed Reimbursement Agent* captures the Agent who will receive the covering payment (i.e., pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer \$ *Instructed Agent*. This optional element is comparable with the Field 54a in the legacy FIN message.

**Min 0 – Max 1**

The *Instructed Reimbursement Agent Account* captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 54.

**Min 0 – Max 1**

![](_page_198_Picture_6.jpeg)

The *Third Reimbursement Agent* captures an additional Agent who will receive the covering payment, where this is not the Agent detailed in the *Instructed Reimbursement Agent*. This optional element is comparable with the Field 55a in the legacy FIN message.

**Min 0 – Max 1**

The *Third Reimbursement Agent Account* captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 55.

## **Credit Transfer Transaction Information**

**Min 1 – Max 1**

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

![](_page_200_Figure_2.jpeg)

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

> an end-to-end reference provided by the *Debtor* which must be passed unchanged throughout the payment and reported to the Creditor.

![](_page_200_Picture_5.jpeg)

note: if the Debtor has not provide an end-toend identifier, the *Debtor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

*UETR* **Min 1 – Max 1** the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting

#### **Min 1 – Max 1**

The pacs message *Payment Identification also* provides a set of optional elements to identify the payment.

![](_page_201_Figure_2.jpeg)

<span id="page-202-0"></span>The pacs message *Payment Type Information* provides a set of optional elements where the payment type can be described. **Min 0 – Max 1**

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point *Instruction Priority*  **Min 0 – Max 1** information may be used by the Instructed Agent to differentiate the processing priority.

a choice of imbedded codes representing the clearing channel to be used to process the payment.

*Clearing Channel* **Min 0 – Max 1**

e.g., RTGS

*Service Level*  **Min 0 – Max 3**

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed\* service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Customer Credit Transfer similarly to Field 111 value 001 in the MT 103

*Payment Type Information*

i

*Local Instrument*  **Min 0 – Max 1**

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, SECU *Category* 

### The pacs.008 message has two key element to capture the amount of the Credit Transfer, *Interbank Settlement Amount* and *Interbank Settlement Date*

**Min 1 – Max 1 Min 1 – Max 1**

![](_page_203_Picture_3.jpeg)

*Interbank Settlement Amount*

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent.* This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

![](_page_203_Picture_6.jpeg)

![](_page_203_Picture_7.jpeg)

![](_page_203_Picture_8.jpeg)

![](_page_203_Picture_9.jpeg)

A mandated date on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent.* This therefore is the value date comparable with the MT Field 32A

![](_page_203_Picture_11.jpeg)

Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important one. Instructed Amount relates to the amount Instructed to be executed from the Debtor's account and only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not the same currency amount.

The pacs.008 message has three optional elements to capture the optional information related to the settlement of the instructions.

**Min 0 – Max 1**

![](_page_204_Picture_2.jpeg)

The *Settlement Priority* provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the *Settlement Method* and should not be confused with the *Instruction Priority.* 

![](_page_204_Picture_4.jpeg)

Note: where *Settlement Method* of the pacs.008 is 'COVE' (settled via a covering pacs.009 COV) SettlementPriority is relevant to the covering payment not the pacs.008

![](_page_204_Picture_6.jpeg)

**Min 0 – Max 1**

The *Settlement Time Indication* optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, *Debit Date Time* and *Credit Date Time*.

**Min 0 – Max 1**

![](_page_204_Picture_11.jpeg)

The *Settlement Time Request* optionally captures the time settlement is requested for the payment instruction by the Instructing Agent. This Time can be capture in four nested elements:

• *CLS Time* the time the amount must be credit to CLS Bank

• *From Time* the time from which the payment may be settled

• *Till Time* the time until which the payment may be settled

*Credit Transfer Transaction Information*

![](_page_205_Picture_0.jpeg)

#### Min 0 - Max 1

The *Instructed Amount* captures currency and amount instructed by the Debtor. This conditional element is required when the *Interbank Settlement Amount* is not the same currency and/or amount as originally instructed by the *Debtor*. For example, a charge is taken, or the transactions is converted to another currency. This element is comparable with the legacy Field 33B.

![](_page_205_Picture_3.jpeg)

#### Min 0 - Max 1

The *Exchange Rate* capture the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency.

![](_page_205_Picture_6.jpeg)

As a best practice to provide consistency and transparency the *Exchange Rate* used to convert the *Instructed Amount (base currency)* to the *Interbank Settlement Amount (quote currency)* should use the Instructed currency as the whole unit to perform the exchange.

For example if *Instructed Amount* currency is CAD and the Interbank Settlement currency is USD the rate should reflected as 0.83 (CAD 1 equals USD 0.83)

![](_page_205_Picture_9.jpeg)

Note: a number of Cross Element Rules exist which relate to the *Instructed Amount* element. For example if the *Instructed Amount* is present and the

#### **Min 1 – Max 1**

The mandated *Charge Bearer* element uses an embedded code that is used to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

| Charge | Code | Description      |                               |      |                      |  |
|--------|------|------------------|-------------------------------|------|----------------------|--|
| Bearer | CRED | Creditor         |                               |      |                      |  |
| (1.1)  | DEBT | Debtor           |                               |      |                      |  |
|        | SHAR | Shared           | 71A: Details<br>of<br>Charges | Code | Description          |  |
|        | SLEV | Service<br>Level |                               | BEN  | Beneficiary          |  |
|        |      |                  |                               | OUR  | Our Customer Charges |  |
|        |      |                  |                               | SHA  | Shared Charges       |  |
|        |      |                  |                               |      |                      |  |

![](_page_206_Picture_3.jpeg)

Note: *Charge Bearer* codeSLEV applies following rules agreed as part of a bilateral agreed Service Level or as part of a scheme (commonly used in Instant Payment schemes) This code has no equivalent in legacy MT messages. SLEV is removed from CBPR+ usage guideline specifications for the beginning of the coexistence period.

The *Charges Information* element provides information on the charges to be paid by the *Charge Bearer*. This element is comparable with MT Fields: 71F 'Senders Charges' and 71G 'Receiver's Charges'

| Charge      | Amount   |                          |  |  |  |  |  |
|-------------|----------|--------------------------|--|--|--|--|--|
| Information | Currency |                          |  |  |  |  |  |
| (0.*)       | Agent    | BICFI                    |  |  |  |  |  |
|             |          | Name                     |  |  |  |  |  |
|             |          | StructuredPostal Address |  |  |  |  |  |

In addition to the legacy MT message the pacs.008 *Charge Information* mandate the *Agent,* this represent the Agent for who the Charges are either; due (pre-paid charges) or has taken a charge (deduct from the transaction)

![](_page_207_Picture_5.jpeg)

As the *Charges Information* element is repetitive it can capture charges related to previous legs of the payment transaction.

Deducted Charges are not appropriate with Charge Bearer DEBT.

![](_page_207_Picture_7.jpeg)

Note: As the *Charge Information* element has the capability to capture both charges deducted and charges included i.e. pre-paid charges, the use of the *Interbank Settlement Amount* and *Instructed Amount* elements play an important role.

Also note: If Charge Bearer DEBT is provided only one optional occurrence of pre-paid charges is allowed.

*Credit Transfer Transaction Info'* Charge Information

## **charges**

![](_page_208_Figure_1.jpeg)

Debtor requests a payment for USD 100 specifying the charges should be shared

Debtor Agent executes the USD 100 payment charging the Debtor as commercially agreed. 2

Agent B processes the payment deducting their fee of USD 10 3

| tlement           | USD 90                |                        |                        |  |  |  |
|-------------------|-----------------------|------------------------|------------------------|--|--|--|
| Instructed Amount |                       |                        | USD 100                |  |  |  |
| Code              |                       |                        | SHAR                   |  |  |  |
| Amount            | ount                  |                        | 10                     |  |  |  |
| Currency          | ,                     |                        | USD                    |  |  |  |
| Agent             |                       | BIC                    | BBBBUS3N               |  |  |  |
|                   | Code  Amount Currency | Code  Amount  Currency | Code  Amount  Currency |  |  |  |

Agent C processes the payment deducting their fee of USD 5

4

| Interbank Settlement<br>Amount |          |   | USD 85  |          |  |  |
|--------------------------------|----------|---|---------|----------|--|--|
| Instructed Amount              |          |   | USD 100 |          |  |  |
| Charge<br>Bearer               | Code     |   |         | SHAR     |  |  |
| Charge                         | Amount   |   |         | 10       |  |  |
| Information                    | Currency | , |         | USD      |  |  |
|                                | Agent    |   | BIC     | BBBBUS3N |  |  |
| Charge<br>Information          | Amount   |   |         | 5        |  |  |

## **of charges**

![](_page_209_Figure_1.jpeg)

3

Debtor requests a payment for USD 100 specifying any charges will be borne by them, in accordance with their banking agreement.

Pre-payment of

BIC in the Charge Information Agent 2

Debtor Agent executes the USD 100 payment including a previous negotiated pre-payment of charges (USD 30). The Debtor is debited for USD 100 plus the Charges in accordance with their account agreement.

charges are identified by the instructed Agent by the inclusion of their element of the payment message they receive pre-payment of charge versus

Agent B identifies the pre-payment of charges by the inclusion of their BIC in the Charge Information Agent element. Removing charge (USD 30), they forward the payment to the next Agent. The next Agent many request a charge.

| Interbank Set<br>Amount | tlement | USD 100 |      |   |
|-------------------------|---------|---------|------|---|
|                         |         |         |      |   |
| Charge<br>Bearer        | Code    |         | DEBT | ١ |

## **of multiple charges**

2

![](_page_210_Figure_1.jpeg)

3

Debtor requests a payment for USD 100 specifying any charges will be taken by them, in accordance with their banking agreement.

Debtor Agent executes the USD 100 payment including a previous negotiated pre-payment of charges (USD 30). The Debtor is debited for USD 100 plus the Charges in accordance with their account agreement.

Agent B identifies the pre-payment of charges by the inclusion of their BIC in the Charge Information Agent element. Removing charge (USD 30), they forward the payment, including USD 20 of prepayment of charges of the next Agent.

Agent C identifies the pre-payment of charges by the inclusion of their BIC in the Charge Information Agent element. Removing this pre-payment of charges they forward the payment to the Next Agent and indicate they will bear the cost of any charge claims. 4

| Pre-payment of            |
|---------------------------|
| charges are identified    |
| by the instructed Agent   |
| by the inclusion of their |
| BIC in the Charge         |
| Information Agent         |
| element<br>of the payment |
|                           |

| Interbank Settlement<br>Amount |          |   | SD 130  |          |   |  |
|--------------------------------|----------|---|---------|----------|---|--|
| Instructed Amount              |          |   | USD 100 |          |   |  |
| Charge<br>Bearer               | Code     |   |         | DEBT     |   |  |
| Charge                         | Amount   |   |         | 30       |   |  |
| Information                    | Currency | , |         | USD      |   |  |
|                                | Agent    |   | BIC     | BBBBUS3N | 4 |  |

| Pre-payment of<br>charges are identified             |  |  |  |  |  |             |                  |
|------------------------------------------------------|--|--|--|--|--|-------------|------------------|
| by the instructed Agent<br>by the inclusion of their |  |  |  |  |  |             |                  |
| BIC in the Charge                                    |  |  |  |  |  |             |                  |
| Information Agent<br>element<br>of the payment       |  |  |  |  |  |             |                  |
| message they receive                                 |  |  |  |  |  | pre-payment | of charge versus |

![](_page_210_Figure_9.jpeg)

ISO 20022 pacs.008 message standards document **"If ChargesInformation is present, then the currency of ChargesInformation/ChargesAmount is recommended to be the same as the currency of InterbankSettlementAmount"**

| Interbank Settlement<br>Amount received | Interbank Settlement<br>Amount forwarded | Currency<br>of Charge<br>Information (where a<br>charge occurs) |
|-----------------------------------------|------------------------------------------|-----------------------------------------------------------------|
| USD                                     | USD                                      | USD                                                             |
| USD                                     | EUR                                      | EUR                                                             |

![](_page_211_Picture_2.jpeg)

ISO 20022 does not prevent Charges from being booked in a different currency, but for transparency the Charge should be represented within the Charge Information in the Interbank Settlement Amount Currency.

## <span id="page-212-0"></span>**charges**

![](_page_212_Figure_1.jpeg)

Debtor requests a payment for GBP 100 to be initiated from their USD account, specifying the charges should be borne by the Creditor

Debtor Agent executes a payment for GBP 95 (GBP 100 minus a 5 GBP charge deducted as this is borne by the Creditor. 2

| Interbank Settlement<br>Amount |          |          | GBP 95 |          |  |  |
|--------------------------------|----------|----------|--------|----------|--|--|
| Instructed Amount              |          |          | BP 100 |          |  |  |
| Charge<br>Bearer               | Code     |          |        | CRED     |  |  |
| Charge                         | Amount   |          |        | 5        |  |  |
| Information                    | Currency | Currency |        | GBP      |  |  |
|                                | Agent    |          | BIC    | AAAAGB22 |  |  |

Agent B processes the payment deducting their fee of GBP 10 3

| Interbank Set<br>Amount | GBP 85            |   |      |          |  |  |
|-------------------------|-------------------|---|------|----------|--|--|
| Instructed Am           | Instructed Amount |   |      | GBP 100  |  |  |
| Charge<br>Bearer        | Code              |   | CRED |          |  |  |
| Charge                  | Amount            |   |      | 5        |  |  |
| Information             | Currency          | / |      | GBP      |  |  |
|                         | Agent             |   | BIC  | AAAAGB22 |  |  |
| Charge                  | Amount            |   |      | 10       |  |  |
| Information             | Currence          | V |      | GRP      |  |  |

The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent.

![](_page_213_Picture_1.jpeg)

**Min 0 – Max 1**

The *Previous Instructing Agent 1* captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message.

**Min 0 – Max 1**

The *Previous Instructing 1 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message

![](_page_213_Picture_6.jpeg)

The *Previous Instructing 2* captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.

**Min 0 – Max 1** The *Previous Instructing 2 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Previous Instructing 3* captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message. **Min 0 – Max 1**

The *Previous Instructing 3 Account* captured the account related between this Agent and Previous

![](_page_213_Picture_11.jpeg)

![](_page_213_Picture_12.jpeg)

![](_page_214_Figure_0.jpeg)

![](_page_214_Picture_1.jpeg)

### **Intermediary Agents**

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. *Intermediary Agent* is an example of this, where these agents are classified in numeric order (i.e. *Intermediary Agent* 1) *Previous Instructing Agent* however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment.

The below diagram visualizes the change of Agent role at different stages of the payment transaction life cycle.

![](_page_215_Picture_3.jpeg)

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

![](_page_216_Picture_1.jpeg)

**Min 0 – Max 1**

The *Intermediary Agent 1* captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 1 Account* captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

![](_page_216_Picture_6.jpeg)

**3**

**Min 0 – Max 1**

The *Intermediary Agent 2* captures the second Intermediary Agent between the Intermediary Agent 1 and the CreditorAgent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 2 Account* captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

![](_page_216_Picture_11.jpeg)

The *Intermediary Agent 3* captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 3 Account* captured the account related to this Intermediary Agent, with the

## authority to instruct payment from their Headquarter (HQ) settlement account.

Usually a serial payment is instructed through each Agent in a serial process. In some circumstances a branch of an Institution (Agent A) may be given Debit Authority to instruct payment from their Headquarters (Agent HQ) account with its currency correspondent (Agent B). In much the same way as if this had occurred serially, it is important that the payment instructed by Agent B correctly reflect Agent HQ as an Agent participating in the transaction, particularly if the payment is returned.

![](_page_217_Figure_2.jpeg)

The pacs.008 message introduces ultimate parties to the FI to FI Customer Credit Transfer message. The *Ultimate Debtor* element should not be confused with an *Initiating Party* who may send a payment initiation request on behalf of the Debtor. (see dedication section on *Initiating Party*)

![](_page_218_Picture_1.jpeg)

➢ CBPR+ premise is that an *Ultimate Debtor* has no financial regulated direct account relationship with the corresponding *Debtor*. **Min 0 – Max 1**

➢ CBPR+ premise is that an *Ultimate Creditor* has no financial regulated direct account relationship with the corresponding *Creditor*. **Min 0 – Max 1**

An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor depending on the payment scenario)

*Credit Transfer Transaction Information*

## **Debtor**

An individual walks into a Money Transfer Bureau with relevant Private Identification (e.g. a passport) and requests a payment to be paid on their behalf to a Creditor. Having accepted payment for the transaction, the Money Transfer Bureau executes a payment initiation request to their Agent (Bank) as the Debtor, on behalf of the individual who is represented as the Ultimate Debtor.

![](_page_219_Figure_2.jpeg)

## **Creditor**

A payments is initiated to credit a retirement care facility to pay the fees of one of its residents. The retirement facility is the Creditor of the payment transaction, whereby the resident of the facility is represented as the Ultimate Creditor (beneficiary of the services the fee is paying for)

![](_page_220_Figure_2.jpeg)

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

![](_page_220_Figure_5.jpeg)

![](_page_221_Picture_0.jpeg)

**Min 0 – Max 1 Min 1 – Max 1**

The *Initiating Party* of a payment is often the *Debtor* themselves and therefore this optional element is not necessary. More often the *Initiating Party* is a third party providing payment initiation services on behalf of the *Debtor* (often referred to as a Third Party Provider) whereby the *Debtor* maintains an account with the Debtor Agent but the Third Party Provider has authority to initiate payment on behalf of the *Debtor*. This is distinctly different from an Ultimate Party (such as *Ultimate Debtor*) who instructs the *Debtor* to initiate a payment on their behalf.

![](_page_221_Picture_4.jpeg)

In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the *Initiating Party* is often the *Creditor*, however the same context of a Third Party Provider can exist where the third party is responsible for collecting funds on behalf of the *Creditor*.

The ISO 20022 pacs messages describe the party debited for a transaction as the *Debtor*. The *Debtor* sub elements describe the *Debtor* in greater detail.

![](_page_222_Figure_1.jpeg)

country code of residence

![](_page_222_Figure_2.jpeg)

Nested element capturing the

address details

various types of identifiers for the party e.g. BIC, LEI etc.

**Min 0 – Max 1**

**pacs.008 FI to FI Customer Credit Transfer–Debtor Account**

The pacs.008 *Debtor Account* is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

> The *Debtor Account* uses a variety of nested elements to capture information related to the account.

![](_page_223_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency of the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

|                   | ISO 20022 Debtor<br>data element<br>example |               |                 |                        |  | Customer data record<br>example | MT –<br>free format option           |  |                                                |                       |
|-------------------|---------------------------------------------|---------------|-----------------|------------------------|--|---------------------------------|--------------------------------------|--|------------------------------------------------|-----------------------|
| Debtor            | Name                                        |               |                 |                        |  |                                 |                                      |  | JOHN<br>HECTOR<br>JOSEPH SMITH -<br>MASTERSONS | :50K:/BE3000121637141 |
|                   | Postal                                      | Department    |                 |                        |  |                                 |                                      |  |                                                |                       |
|                   | Address                                     |               | Sub Department  |                        |  |                                 | PASSPORT<br>1111111111               |  |                                                |                       |
|                   |                                             | Street Name   |                 | HOOGSTRAAT             |  |                                 |                                      |  |                                                |                       |
|                   |                                             |               | Building Number |                        |  | 6                               |                                      |  |                                                |                       |
|                   |                                             |               |                 |                        |  |                                 |                                      |  |                                                |                       |
|                   |                                             | Town Name     |                 |                        |  | BRUSSELS                        | :50F:/BE3000121637141                |  |                                                |                       |
|                   |                                             | Country       |                 |                        |  | BE                              |                                      |  |                                                |                       |
|                   | Identification                              | Private<br>Id | Other           | Id                     |  | 1111111111                      | 1/SONS                               |  |                                                |                       |
|                   |                                             |               |                 | Scheme<br>Code<br>Name |  | CCPT                            | 2/HOOGSTRAAT 6<br>3/BE/BRUSSELS 1000 |  |                                                |                       |
| Debtor<br>Account | IBAN<br>Identification                      |               | BE3000121637141 |                        |  |                                 |                                      |  |                                                |                       |

#### **MT – free format option**

:50K:/BE3000121637141 JOHN HECTOR JOSEPH SMITH - MASTERSO HOOGSTRAAT 6 BRUSSELS 1000 BELGIUM PASSPORT 1111111111

Post Code 1000 **MT – structured option with risk of potential truncation & loss of info**

1/JOHN HECTOR JOSEPH SMITH - MASTER 1/SONS 2/HOOGSTRAAT 6 3/BE/BRUSSELS 1000

**Min 1 – Max 1 Min 1 – Max 1**

The *Debtor Agent* and *Creditor Agent* are static roles in the pacs.008 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the *Debtor* and *Creditor*.

![](_page_225_Picture_3.jpeg)

![](_page_225_Picture_4.jpeg)

![](_page_225_Picture_5.jpeg)

Note: Although the *Debtor Agent, Creditor Agent, Debtor and Creditor* all maintain static roles in the pacs messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

## **Account**

**Min 0 – Max 1**

**Min 0 – Max 1**

The pacs.008 *Debtor Agent Account* and *Creditor Agent Account* are used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

**pacs.008 FI to FI Customer Credit Transfer– Debtor Agent Account and Creditor Agent** 

![](_page_226_Picture_3.jpeg)

The *Debtor Agent Account* and *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification*identifies the account maintained at theAccount Servicing Institution *Type* uses the external CashAccount Type code list to identify the type of account *Currency* identifies the currency of the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1 Min 0 – Max 1**

> *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_226_Picture_8.jpeg)

Debtor Agent and Creditor Agent are a Financial Institution, therefore

The ISO 20022 pacs messages describe the party credited for a transaction as the *Creditor*. The *Creditor* sub elements describe the *Creditor* in greater detail.

Mandatory *Name* (where a BIC identifier is not provided) by which the party is known

Optional element to

*Identification*

*Postal Address*

![](_page_227_Picture_2.jpeg)

![](_page_227_Figure_3.jpeg)

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Nested element capturing either structured or unstructured *Creditor*

address details

*Country of Residence* capture the Creditor's ISO country code of residence

#### **Min 0 – Max 1**

The pacs.009 *Creditor Account* is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

> The *Creditor Account* uses a variety of nested elements to capture information related to the account.

![](_page_228_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency if the account **Min 0 – Max 1**

**pacs.008 FI to FI Customer Credit Transfer – Creditor Account**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

## **Account**

**Min 0 – Max 1**

**Min 0 – Max 1**

The pacs.008 *Debtor Agent Account* and *Creditor Agent Account* are used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

**pacs.008 FI to FI Customer Credit Transfer– Debtor Agent Account and Creditor Agent** 

![](_page_229_Picture_3.jpeg)

The *Debtor Agent Account* and *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification*identifies the account maintained at theAccount Servicing Institution *Type* uses the external CashAccount Type code list to identify the type of account *Currency* identifies the currency of the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1 Min 0 – Max 1**

> *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_229_Picture_8.jpeg)

Debtor Agent and Creditor Agent are a Financial Institution, therefore

The *Instruction for Next Agent* and *Instruction for Creditor Agent* elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

![](_page_230_Picture_1.jpeg)

**Min 0 – Max 2**

The *Instruction for Creditor Agent* element offers a multiplicity of up to 2 occurrences of information. This element enables:

- ➢ the use of 2 embedded codes to describe the instruction
- ➢ free format *instruction information*
- ➢ or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the *Creditor Agent*. It must be passed on throughout the life cycle of the transaction until the payment reaches the *Credit Agent*.

![](_page_230_Picture_8.jpeg)

**Min 0 – Max 6**

*Credit Transfer Transaction Information* The *Instruction for Next Agent* element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format *instruction information* in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

**Min 0 – Max 1**

The *Purpose* element within the pacs.008 FI to FI Customer Credit Transfer captures the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment e.g. IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Debtor.

![](_page_231_Picture_3.jpeg)

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example: GDSVis classified within the Commercial categorisation, with the *Name* Purchase Sale of Goods and Services described as a Transaction is related to purchase and sale of goods.

![](_page_231_Picture_6.jpeg)

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

The *Regulatory Reporting* element within the pacs.008 FI to FI Customer Credit Transfer is nested to capture regulatory and statutory information needed to report to the appropriate authority/s. **Min 0 – Max 10**

![](_page_232_Picture_1.jpeg)

**Min 0 – Max 1**

The *Debit Credit Reporting Indicator* utilises an embedded choice of code to indicate whether the regulatory reporting information applies to the:

- DEBT (debit)
- CRED (credit) or
- BOTH

**Min 0 – Max 1**

The *Authority* element captures the *Name* and *Country* code of the Authority/Entity requiring the regulatory reporting information.

**Min 0 – Max \*** The *Details* element provides the detail on the regulatory reporting information.

**Min 0 – Max 1**

The *Related Remittance Information* element within the pacs.008 FI to FI Customer Credit Transfer is nested to provide information related to the handling of remittance information. This information is typically provided by the Debtor in the payment initiation request.

**Min 0 – Max 1**

The *Remittance Identification* captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction.

**Min 0 – Max 2**

The *Remittance Location Details* uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- *Method* requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email)
- *Electronic Address* provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.
- *Postal Address* provides the postal address to which an agent is to send the remittance information

Remittance advices are typically considered as a traditional value added service provided by the Debtor Agent to the Debtor, in order to provide *Remittance Information* to the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting messages.

*Remittance Information* is a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022. *Related Remittance Information* and *Remittance Information* are mutually exclusive (can't both be present)

Business examples are emerging where information is externalised using a URL repository solution.

![](_page_233_Picture_11.jpeg)

![](_page_233_Picture_12.jpeg)

The optional *Remittance Information* element within the pacs.008 FI to FI Customer Credit Transfer is nested to provide either *Structured* or *Unstructured* information related to payment, such as invoices.

**Min 0 – Max 1**

*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle

![](_page_234_Picture_3.jpeg)

**Min 0 – Max 1**

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

**Min 0 – Max \***

The **Structured** element is nested capturing rich structured *Remittance Information,*  and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification)

The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-to-end transportation of this data.

![](_page_234_Picture_9.jpeg)

mutually exclusive (can't both be present)

The bilaterally/multilaterally agreed *Remittance Information* which is *Structured* must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

![](_page_235_Figure_1.jpeg)

example of *Structured* invoice information

![](_page_235_Figure_3.jpeg)

The *Creditor Remittance Information* is provided to the *Creditor* in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.

> In this example Referred Document Information and it nested elements has multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Serial Financial Institution to Financial Institution to Customer Credit Transfer**

Use Case p.8.1.1 – High Level FI to FI Customer Credit Transfer (pacs.008) settled over a Payment Market Infrastructure

Use Case p.8.1.2 – High Level FI to FI Customer Credit Transfer (pacs.008) Sweeps (Short position at the Secondary Account)

#### **Cover Method Financial Institution to Financial Institution to Customer Credit Transfer**

Use Case p.8.2.1 - High Level FI to FI Customer Credit Transfer settled using the cover method (pacs.009 COV) over a Payment Market Infrastructure

Use Case p.8.2.2 - High Level FI to FI Customer Credit Transfer involved a serial leg into a cover method (pacs.009 COV)

Use Case p.8.2.3 - High Level FI to FI Customer Credit Transfer involved a serial leg in and out of a cover method (pacs.009 COV)

Use Case p.8.2.4 - High Level FI to FI Customer Credit Transfer involved a serial leg out of a cover method (pacs.009 COV)

### <span id="page-237-0"></span>**Market Infrastructure**

![](_page_237_Figure_1.jpeg)

Debtor initiates a payment instruction to the Debtor Agent.

Agent B processes the payment on Agent C, via the Payment Market Infrastructure

Agent C processes the payment onto Agent D.

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries, who are direct

Payment Market Infrastructure, settles the payment between Agent B and Agent C as direct participants of the Market

Agent D credits the account of the Creditor, and may optionally provide a notification e.g. credit notification in addition to an

## <span id="page-238-0"></span>**Authorised Party**

![](_page_238_Figure_1.jpeg)

- As a pre-requisite the Debtor provides Debit Authorisation to Agent I to Initiate Payment from their account with the Debtor Agent (A)
- Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

![](_page_238_Picture_7.jpeg)

See use case <u>pn.1.2.1</u> for an Authorised Party Payment.

<span id="page-239-0"></span>![](_page_239_Figure_0.jpeg)

![](_page_240_Figure_0.jpeg)

the Creditor Agent (E) by sending a direct pacs.008 to Agent E who they have business (Agent D) covering payment to credit the account of Agent (E) with their correspondent occurred in Step 6 based upon their risk appetite.

![](_page_241_Figure_0.jpeg)

![](_page_242_Figure_0.jpeg)

**Financial Institution to Financial Institution Customer Credit Transfer**

**pacs.008** Group Header Credit Transfer Transaction Information The pacs.008 STP has two core sets of nested elements:

- *Group Header* which contains a set of characteristics that relates to all individual transaction
- *Credit Transfer Transaction Information* which contains elements providing information specific to the individual credit transfer transaction.

![](_page_244_Picture_4.jpeg)

Payment messages in a many-to-many payment are considered as a single transaction. The pacs.008 STP is a message who's Usage Guideline has been further restricted by remove elements considered

![](_page_245_Figure_0.jpeg)

The Financial Institution To Financial Institution Customer Credit Transfer message is sent by the Debtor Agent to the Creditor Agent, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a Debtor account to a

The pacs.008 STP message has enhance STP feature over and above the pacs.008 and legacy MT 103 STP. At a high level the key difference between the pacs.008 and pacs.008 STP are summarized.

![](_page_246_Picture_1.jpeg)

![](_page_246_Picture_2.jpeg)

Business Application Header

Credit Transfer Transaction Information

Intermediary Agent 1 Intermediary Agent 2 Debtor Agent Creditor Agent

Debtor Creditor

Creditor Account

swift.cbprplus.02 swift.cbprplus.stp.02

Financial Institution identifiers:

- BIC
- Clearing System Member Id
- LEI
- Name
- Postal Address

Financial Institution identifiers:

- BIC
- Clearing System Member Id
- LEI

Name removed

Postal Address removed

Account optional

Elements optional

ISO Code or Proprietary

IBAN rules Account mandatory

Addition Debtor and Creditor

Instruction for Next Agent removed Instruction for Creditor Agent removed

ISO Code or Proprietary removed

## <span id="page-247-0"></span>**Financial Institution Credit Transfer**

![](_page_248_Figure_0.jpeg)

The pacs.009 has two main use cases:

- as a core Financial Institution Credit Transfer message.
- As a **COV** where it is used as cover of (to settle) a pacs.008.

The pacs.009 therefore contain information of the underlying Customer Credit Transfer (pacs.008) for use in the cover scenario, which is the key attribute to differentiate between these two use cases.

The pacs.009 may also be used as a **ADV** where it is sent as an advice and is settled using the pacs.009 as a core message.

![](_page_249_Figure_0.jpeg)

The Financial Institution Credit Transfer message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are **Financial Institutions**.

## **Group Header**

![](_page_251_Picture_1.jpeg)

Each ISO 20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

![](_page_251_Picture_4.jpeg)

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference)

The pacs.009 message *Creation Date* captures the date and time which the message was created.

![](_page_252_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_252_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The pacs.009 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_253_Picture_2.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_253_Picture_4.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

**Min 1 – Max 1**

The pacs.009 *Settlement Method* element within the Group Header *Settlement Information*, includes one of the embedded codes to indicate how the payment message will be settled.

The *Settlement Method element* in the pacs.009 allows a choice of an embedded code.

![](_page_254_Picture_3.jpeg)

**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated *Settlement Account* element.

**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated *Settlement Account*  element.

![](_page_254_Picture_6.jpeg)

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification (HVPS+)

The pacs.009 message *Settlement Account* is a nested element as part of *Settlement Information,* this element identifies information related to an account used to settle the payment instruction.

**Min 0 – Max 1**

The *Settlement Account* identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the *Settlement Method*)

![](_page_255_Picture_3.jpeg)

**Min 0 – Max 1**

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account

*Currency* identifies the currency if the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

## **Credit Transfer Transaction Information**

**Min 1 – Max 1**

**Min 1 – Max 1**

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

![](_page_257_Figure_2.jpeg)

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

an end-to-end reference provided by the *Debtor* which must be passed unchanged throughout the payment and reported to the Creditor.

> note: for a pacs.009 COV the end-to-end id is provided by the Debtor from the pacs.008 Instruction id.

In a pacs.009 COR if the Debtor has not provide an end-to-end identifier, the *Debtor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting

#### **Min 1 – Max 1**

The pacs message *Payment Identification also* provides a set of optional elements to identify the payment.

![](_page_258_Figure_2.jpeg)

*Payment Type Information* The pacs message *Payment Type Information* provides a set of optional elements where the payment type can be described. **Min 0 – Max 1** A nested element which may either use an external ISO Service Level code\* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV *Service Level*  **Min 0 – Max 3** A nested element which may either use an *Local Instrument Instruction Priority*  **Min 0 – Max 1** a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

**Min 0 – Max 1**

i

*Category* 

a choice of imbedded codes representing the clearing channel to be used to process the payment.

*Clearing Channel* **Min 0 – Max 1**

e.g., RTGS

external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

identify the category of payment. For example, SECU

The pacs.009 message (unlike the pacs.008) has only one element to capture the amount of the Credit Transfer, *Interbank Settlement Amount*.

**Min 1 – Max 1**

![](_page_260_Picture_2.jpeg)

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent.* This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

![](_page_260_Picture_4.jpeg)

**Min 1 – Max 1**

A mandated date on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent.* This therefore is the value date comparable with the MT Field 32A

![](_page_260_Picture_7.jpeg)

Note: the Financial Institution Credit Transfer (pacs.009) has no *Instructed Amount* element, *Exchange Rate* or *Charger Bearer* (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

## **Request**

The pacs.009 message has three optional elements to capture the optional information related to the settlement of the instructions.

![](_page_261_Picture_2.jpeg)

**Min 0 – Max 1**

The *Settlement Priority* provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the *Settlement Method* and should not be confused with the *Instruction Priority.* 

![](_page_261_Picture_5.jpeg)

Note: Where the *Settlement Method* of the pacs.009 is 'INDA' (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code 'INGA' implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary. **Min 0 – Max 1**

![](_page_261_Picture_7.jpeg)

The *Settlement Time Indication* optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, *Debit Date Time* and *Credit Date Time*.

![](_page_261_Picture_10.jpeg)

![](_page_261_Picture_11.jpeg)

The *Settlement Time Request* optionally captures the time settlement is requested for the payment instruction by the Instructing Agent. This Time can be capture in four nested elements:

- *CLS Time* the time the amount must be credit to CLS Bank
- *Till Time* the time until which the payment may be settled

• *From Time* the time from which the payment may be settled

*Credit Transfer Transaction Information*

The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent.

![](_page_262_Picture_1.jpeg)

The *Previous Instructing Agent 1* captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message.

**Min 0 – Max 1**

**Min 0 – Max 1**

The *Previous Instructing Agent 1 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message

![](_page_262_Picture_5.jpeg)

**Min 0 – Max 1**

The *Previous Instructing Agent 2* captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.

**Min 0 – Max 1**

The *Previous Instructing Agent 2 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message.

![](_page_262_Picture_10.jpeg)

**Min 0 – Max 1**

The *Previous Instructing Agent 3* captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message. **Min 0 – Max 1**

The *Previous Instructing Agent 3 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in

![](_page_263_Figure_0.jpeg)

*Instructing Agent* and *Instructed Agent* elements are required in all pacs messages and are only available in the *Credit Transfer Information Credit Transfer Transaction Information*

### **Intermediary Agents**

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. *Intermediary Agent* is an example of this, where these agents are classified in numeric order (i.e. *Intermediary Agent* 1) *Previous Instructing Agent* however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment.

The below diagram visualizes the change of Agent role at different stages of the payment transaction life cycle.

![](_page_264_Picture_3.jpeg)

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

![](_page_265_Picture_1.jpeg)

**Min 0 – Max 1**

The *Intermediary Agent 1* captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 1 Account* captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

![](_page_265_Picture_6.jpeg)

**3**

**Min 0 – Max 1**

The *Intermediary Agent 2* captures the second Intermediary Agent between the Intermediary Agent 1 and the CreditorAgent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 2 Account* captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

![](_page_265_Picture_11.jpeg)

The *Intermediary Agent 3* captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 3 Account* captured the account related to this Intermediary Agent, with the

![](_page_266_Figure_0.jpeg)

**Min 0 – Max 1**

**Min 0 – Max 1**

The pacs.009 *Debtor Account* is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

**pacs.009 Financial Institution Credit Transfer – Debtor Account**

The *Debtor Account* uses a variety of nested elements to capture information related to the account.

![](_page_267_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account *Currency* identifies the currency if the account **Min 0 – Max 1 Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_267_Picture_8.jpeg)

the pacs.009 the Debtor is a Financial Institution, therefore the nested

The *Debtor Agent* and *Creditor Agent* are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the *Debtor* and *Creditor*. However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship.

![](_page_268_Picture_3.jpeg)

![](_page_268_Picture_4.jpeg)

![](_page_268_Picture_5.jpeg)

Note: Where the *Debtor* and *Creditor* maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the *Creditor Agent* element to align with translation from the legacy MT message.

## **Account**

**Min 0 – Max 1**

**Min 0 – Max 1**

The pacs.009 *Debtor Agent Account* and *Creditor Agent Account* is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

**pacs.009 Financial Institution Credit Transfer – Debtor Agent Account and Creditor Agent** 

![](_page_269_Picture_3.jpeg)

The *Debtor Agent Account* and *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency if the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

> *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_269_Picture_10.jpeg)

Debtor Agent and Creditor Agent are a Financial Institutions, therefore

![](_page_270_Figure_0.jpeg)

**Min 0 – Max 1**

**Min 0 – Max 1**

The pacs.009 *Creditor Account* is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

**pacs.009 Financial Institution Credit Transfer – Creditor Account**

The *Creditor Account* uses a variety of nested elements to capture information related to the account.

![](_page_271_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account *Currency* identifies the currency if the account **Min 0 – Max 1 Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_271_Picture_8.jpeg)

the pacs.009 the Creditor is a Financial Institution, therefore the

The *Instruction for Next Agent* and *Instruction for Creditor Agent* elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

![](_page_272_Picture_1.jpeg)

**Min 0 – Max 2**

The *Instruction for Creditor Agent* element offers a multiplicity of up to 2 occurrences of information. This element enables:

- ➢ the use of 2 embedded codes to describe the instruction
- ➢ free format *instruction information*
- ➢ or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the *Creditor Agent*. It must be passed on throughout the life cycle of the transaction until the payment reaches the *Credit Agent*.

![](_page_272_Picture_8.jpeg)

*The Creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) Instruction for Creditor Agent, Instruction Information element preceded by /UDLC/ (UnDerLying Creditor) to provide party transparency in the settlement message.*

![](_page_272_Picture_10.jpeg)

**Min 0 – Max 6**

*Credit Transfer Transaction Information* The *Instruction for Next Agent* element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format *instruction information* in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

#### **Min 0 – Max 2**

An *Instruction for Creditor Agent* elements within the pacs.009 Financial Institution Credit Transfer, used to settle a pacs.009 Financial Institution Credit Transfer Advice (ADV), provides information related to the Creditor in the advice message (Underlying Creditor).

The *Creditor* of the pacs.009 ADV are commonly captured in one of the following ways:

- As a BIC (*BICFI*) either on its own, or
- As a *Clearing System Member Identification* or a *LEI* with *Name*, and *Postal Address*

![](_page_273_Picture_5.jpeg)

![](_page_273_Picture_6.jpeg)

![](_page_273_Picture_7.jpeg)

pacs.009 *Instruction for Creditor Agent***/Instruction Information.**

Up to 2 occurrences of Instruction Information may be provided. The last available occurrence of **Instruction Information**, preceded by /UDLC/, must be used to capture the Underlying Creditor provided in the pacs.009 ADV.

![](_page_273_Figure_10.jpeg)

**BICFI** only.

**Name** and structured **Postal Address**  (TownName and Country Code should be prioritised).

**Name** and unstructured **Address Line** (TownName and Country Code should be prioritised, where possible).

**Min 0 – Max 1**

The *Purpose* elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used by the capture the nature of the payment e.g., CORT Trade Settlement Payment, CFEE Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.

![](_page_274_Picture_3.jpeg)

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCD is classified within the Collateral categorisation, with the *Name* OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

![](_page_274_Picture_7.jpeg)

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g., Category Purpose code SECU 'Securities' may trigger pacs.002 *Payment Status Report* to provide update on the progress of the payment to the previous Agent.

The optional *Remittance Information* element within the pacs.009 Financial Institution Credit Transfer is nested to provide *Unstructured* information related to payment.

**Min 0 – Max 1**

*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle

![](_page_275_Picture_3.jpeg)

**Min 0 – Max 1**

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

*Credit Transfer Transaction Info'* Remittance Information

![](_page_275_Picture_6.jpeg)

ISO 20022.

Note: unlike the pacs.008 *Remittance Information* can only be captured in an *Unstructured* element in the pacs.009 Financial Institution Credit Transfer. *Remittance Information* is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Serial Financial Institution Payments**

Use Case p.9.1.1 – High Level Financial Institution Credit Transfer (pacs.009) settled over a Payment Market Infrastructure Use Case p.9.1.2 - High Level Financial Institution Credit Transfer (pacs.009) pre-advised settled using pacs.009.

## **Payment Market Infrastructure**

![](_page_277_Figure_1.jpeg)

participants of the Market Infrastructure, and provides a settlement confirmation to Agent B

![](_page_278_Figure_0.jpeg)

## <span id="page-279-0"></span>**Financial Institution Credit Transfer**

![](_page_280_Picture_0.jpeg)

The pacs.009 advice is used to preadvice an Agent of a fund movement toward the Creditor.

The core pacs.009 is used to perform the settlement of this pre-advice message.

![](_page_281_Figure_0.jpeg)

The Financial Institution Credit Transfer (advice) message is sent by a Debtor Agent to a Creditor Agent, directly. In this context the pacs.009 ADV is used as a direct advice message.

It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are **Financial Institutions**.

![](_page_281_Picture_3.jpeg)

## **Group Header**

![](_page_283_Picture_1.jpeg)

Each ISO 20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

![](_page_283_Picture_4.jpeg)

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference)

The pacs.009 message *Creation Date* captures the date and time which the message was created.

![](_page_284_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_284_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The pacs.009 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_285_Picture_2.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_285_Picture_4.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

**Min 1 – Max 1**

The pacs.009 *Settlement Method* element within the Group Header *Settlement Information*, includes one of the embedded codes to indicate how the payment message will be settled.

![](_page_286_Picture_2.jpeg)

The *Settlement Method element* in the pacs.009 ADV is fixed to **COVE**. This indicate this advice of Financial Institution Credit Transfer will be settlement using a covering pacs.009.

Like the pacs.008, the Agents being used in the covering payment to reimburse the Instructed Agent can be provided in the dedicated Reimbursement Agent elements. This allows the Instructed Agent to identify the debit account on their books from the Reimbursement Agent account or look up the account related to the reimbursement agent.

The pacs message captures a number of Reimbursement Agents as a sub element to *Settlement Information* these elements detail the Agent in the cover method who will process the pacs.009 cover. These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as The *Instructing Reimbursement Agent,* and *Instructed Reimbursement Agent.* Each of these reimbursement agents also has a dedicated account element to optionally capture their related account details.

**Min 0 – Max 1**

The *Instructing Reimbursement Agent* captures the Agent who will execute a covering payment (i.e. pacs.009 COV or domestic equivalent) often referred to as the currency correspondent. This optional element is comparable with the Field 53a in the legacy FIN message.

**Min 0 – Max 1**

The *Instructing Reimbursement Agent Account* captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 53.

**Min 0 – Max 1**

The *Instructed Reimbursement Agent* captures the Agent who will receive the covering payment (i.e., pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer *InstructedAgent*. This optional element is comparable with the Field 54a in the legacy FIN message.

**Min 0 – Max 1**

The *Instructed Reimbursement Agent Account* captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 54.

![](_page_287_Picture_9.jpeg)

![](_page_287_Picture_10.jpeg)

## **Credit Transfer Transaction Information**

**Min 1 – Max 1**

**Min 1 – Max 1**

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

![](_page_289_Figure_2.jpeg)

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

> Note: this reference must be transported in the *End-to-End Identification* of the pacs.009 message used to settle the pacs.009 ADV

an end-to-end reference provided by the *Debtor* which must be passed unchanged throughout the payment and reported to the Creditor.

> note: In a pacs.009 ADV if the Debtor has not provide an end-to-end identifier, the *Debtor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting

#### **Min 1 – Max 1**

The pacs message *Payment Identification also* provides a set of optional elements to identify the payment.

![](_page_290_Figure_2.jpeg)

*Payment Type*  The pacs message *Payment Type Information* provides a set of optional elements where the payment type can be described. **Min 0 – Max 1** A nested element which may either use an external ISO Service Level code\* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV *Service Level*  **Min 0 – Max 3** *Instruction Priority*  **Min 0 – Max 1** a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

i

*Clearing Channel* **Min 0 – Max 1**

*Category* 

a choice of imbedded codes representing the clearing channel to be used to process the payment.

e.g., RTGS

*Information* A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order. *Local Instrument*  **Min 0 – Max 1**

> Note: the ISO instrument codes are registered by specific community group (captured in the code list)

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

identify the category of payment. For example, SECU

## **Date**

The pacs.009 message (unlike the pacs.008) has only one element to capture the amount of the Credit Transfer, *Interbank Settlement Amount*.

**Min 1 – Max 1**

![](_page_292_Picture_3.jpeg)

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent.* This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

![](_page_292_Picture_5.jpeg)

A mandated date on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent.* This therefore is the value date comparable with the MT Field 32A

![](_page_292_Picture_7.jpeg)

Note: the Financial Institution Credit Transfer (pacs.009) has no *Instructed Amount* element, *Exchange Rate* or *Charger Bearer* (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

## **& Request**

The pacs.009 message has three optional elements to capture the optional information related to the settlement of the instructions.

![](_page_293_Picture_2.jpeg)

![](_page_293_Picture_3.jpeg)

The *Settlement Priority* provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the *Settlement Method* and should not be confused with the *Instruction Priority.* 

![](_page_293_Picture_5.jpeg)

Note: As the *Settlement Method* of the pacs.009 (ADV) is 'COVE' (settled via a covering pacs.009) SettlementPriority is relevant to the covering payment not the pacs.009ADV

![](_page_293_Picture_7.jpeg)

**Min 0 – Max 1**

The *Settlement Time Indication* optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, *Debit Date Time* and *Credit Date Time*.

#### **Min 0 – Max 1**

![](_page_293_Picture_12.jpeg)

The *Settlement Time Request* optionally captures the time settlement is requested for the payment instruction by the Instructing Agent. This Time can be capture in four nested elements:

• *CLS Time* the time the amount must be credit to CLS Bank

• *From Time* the time from which the payment may be settled

• *Till Time* the time until which the payment may be settled

*Credit Transfer Transaction Information*

![](_page_294_Figure_0.jpeg)

### **Intermediary Agents**

![](_page_295_Picture_1.jpeg)

Unlike the other pacs.009 messages in the CBPR+ collection, the pacs.009 ADV message is exchanged directly between the Debtor Agent (as an Instructing Agent) and Creditor Agent (as an Instructed Agent). The roles of previous Instructing Agents and Intermediary Agents are therefore irreverent in the pacs.009 (ADV)

![](_page_295_Picture_3.jpeg)

![](_page_296_Figure_0.jpeg)

#### **Min 0 – Max 1**

The pacs.009 *Debtor Account* is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

> The *Debtor Account* uses a variety of nested elements to capture information related to the account.

![](_page_297_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency if the account **Min 0 – Max 1**

**pacs.009 (ADV) Financial Institution Credit Transfer – Debtor Account**

*Name* identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

![](_page_297_Picture_9.jpeg)

the pacs.009 the Debtor is a Financial Institution, therefore the nested

The *Debtor Agent* and *Creditor Agent* are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the *Debtor* and *Creditor*. However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship.

![](_page_298_Picture_3.jpeg)

![](_page_298_Picture_4.jpeg)

![](_page_298_Picture_5.jpeg)

Note: Where the *Debtor* and *Creditor* maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the *Creditor Agent* element to align with translation from the legacy MT message.

## **Agent Account**

The pacs.009 *Debtor Agent Account* and *Creditor Agent Account* is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction. **Min 0 – Max 1**

**pacs.009 (ADV) Financial Institution Credit Transfer – Debtor Agent Account and Creditor** 

![](_page_299_Picture_2.jpeg)

The *Debtor Agent Account* and *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency if the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

> *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_299_Picture_9.jpeg)

**Min 0 – Max 1**

Debtor Agent and Creditor Agent are a Financial Institutions, therefore

The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the *Creditor*. The *Creditor* sub elements describe the *Creditor* in greater detail. *Creditor Name Name* by which the Agent is known *Postal Address* Information used to identify a Debtor by a clearing system identifier. *BICFI* The BIC which identifies the *Creditor Clearing System Member Id* Nested element capturing either structured or unstructured *Debtor LEI* Legal entity identifier of the financial institution. *The Creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) Instruction for Creditor Agent, Instruction Information element preceded by /UDLC/* 

*(UnDerLying Creditor) to provide party* 

address details

#### **Min 0 – Max 1**

**Min 0 – Max 1**

The pacs.009 *Creditor Account* is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

> The *Creditor Account* uses a variety of nested elements to capture information related to the account.

![](_page_301_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency if the account **Min 0 – Max 1**

**pacs.009 (ADV) Financial Institution Credit Transfer – Creditor Account**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_301_Picture_9.jpeg)

For the pacs.009 the Creditor is a Financial Institution, therefore the

The *Instruction for Next Agent* and *Instruction for Creditor Agent* elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

![](_page_302_Picture_1.jpeg)

**Min 0 – Max 2**

The *Instruction for Creditor Agent* element offers a multiplicity of up to 2 occurrences of information. This element enables:

- ➢ the use of 2 embedded codes to describe the instruction
- ➢ free format *instruction information*
- ➢ or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the *Creditor Agent*. It must be passed on throughout the life cycle of the transaction until the payment reaches the *Credit Agent*.

![](_page_302_Picture_8.jpeg)

**Min 0 – Max 6**

The *Instruction for Next Agent* element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format *instruction information* in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

**Min 0 – Max 1**

The *Purpose* elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used by the capture the nature of the payment e.g. CORT Trade Settlement Payment, CFEE Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.

![](_page_303_Picture_3.jpeg)

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCD is classified within the Collateral categorisation, with the *Name* OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

![](_page_303_Picture_7.jpeg)

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. Category Purpose code SECU 'Securities' may trigger pacs.002 *Payment Status Report* to provide update on the progress of the payment to the previous Agent.

The optional *Remittance Information* element within the pacs.009 Financial Institution Credit Transfer is nested to provide *Unstructured* information related to payment.

**Min 0 – Max 1**

*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle

![](_page_304_Picture_3.jpeg)

**Min 0 – Max 1**

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

*Credit Transfer Transaction Info'* Remittance Information

![](_page_304_Picture_6.jpeg)

ISO 20022.

Note: unlike the pacs.008 *Remittance Information* can only be captured in an *Unstructured* element in the pacs.009 Financial Institution Credit Transfer. *Remittance Information* is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Financial Institution Advice Payments**

Use Case p.9.1.2.a - High Level Financial Institution Credit Transfer (pacs.009) pre-advised using pacs.009 (advice) Use Case p.9.1.2.b - High Level Financial Institution Credit Transfer (pacs.009) pre-advised using pacs.009 (advice)

![](_page_306_Figure_0.jpeg)

![](_page_307_Figure_0.jpeg)

Agent D

zone differences between the various Agent in

the payment chain.

provide a notification e.g. credit

notification

## **Financial Institution Credit Transfer (Cover)**

![](_page_309_Figure_0.jpeg)

The pacs.009 has two main use cases:

- as a core Financial Institution Credit Transfer message
- As a **COV** where it is used as cover of (to settle) a pacs.008.

The pacs.009 therefore contain information of the underlying Customer Credit Transfer (pacs.008) for use in the cover scenario, which is the key attribute to differentiate between these two use cases.

![](_page_310_Figure_0.jpeg)

The Financial Institution Credit Transfer message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are **Financial Institutions**.

![](_page_311_Figure_0.jpeg)

## roles between messages

![](_page_312_Figure_1.jpeg)

## **Group Header**

![](_page_314_Picture_1.jpeg)

Each ISO 20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

![](_page_314_Picture_4.jpeg)

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference)

The pacs.009 message *Creation Date* captures the date and time which the message was created.

![](_page_315_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_315_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

## **Transactions**

**Min 1 – Max 1**

The pacs.009 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_316_Picture_3.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_316_Picture_5.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

**Min 1 – Max 1**

The pacs.009 *Settlement Method* element within the Group Header *Settlement Information*, includes one of the embedded codes to indicate how the payment message will be settled.

The *Settlement Method element* in the pacs.009 allows a choice of an embedded code.

![](_page_317_Picture_3.jpeg)

**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated *Settlement Account* element.

**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated *Settlement Account*  element.

![](_page_317_Picture_6.jpeg)

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification (HVPS+)

The pacs.009 message *Settlement Account* is a nested element as part of *Settlement Information,* this element identifies information related to an account used to settle the payment instruction.

**Min 0 – Max 1**

The *Settlement Account* identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the *Settlement Method*)

![](_page_318_Picture_3.jpeg)

**Min 0 – Max 1**

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account

*Currency* identifies the currency if the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

## **Credit Transfer Transaction Information**

**Min 1 – Max 1**

**Min 1 – Max 1**

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

![](_page_320_Figure_2.jpeg)

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

an end-to-end reference provided by the *Debtor* which must be passed unchanged throughout the payment and reported to the Creditor.

> note: for a pacs.009 COV the end-to-end id is provided (by the Debtor) from the pacs.008 Instruction id.

In a pacs.009 COR if the Debtor has not provided an end-to-end identifier, the *Debtor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting

## **(continued)**

**Min 1 – Max 1**

The pacs message *Payment Identification also* provides a set of optional elements to identify the payment.

![](_page_321_Figure_3.jpeg)

## **Information**

The pacs message *Payment Type Information* provides a set of optional elements where the payment type **Min 0 – Max 1**

can be described.

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the

Instructed Agent to differentiate

a choice of imbedded codes representing the clearing channel to be used to process the payment.

the processing priority.

e.g., RTGS

*Channel* **Min 0 – Max 1**

*Clearing*

*Instruction Priority*  **Min 0 – Max 1**

*Service Level*  **Min 0 – Max 3**

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV

*Payment Type Information*

*Category* 

*Local Instrument*  **Min 0 – Max 1**

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

i

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, SECU

## **Date**

The pacs.009 message (unlike the pacs.008) has only one element to capture the amount of the Credit Transfer, *Interbank Settlement Amount*.

**Min 1 – Max 1**

![](_page_323_Picture_3.jpeg)

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent.* This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

![](_page_323_Picture_5.jpeg)

**Min 1 – Max 1**

A mandated date on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent.* This therefore is the value date comparable with the MT Field 32A

![](_page_323_Picture_8.jpeg)

Note: the Financial Institution Credit Transfer (pacs.009) has no *Instructed Amount* element, *Exchange Rate* or *Charger Bearer* (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

## **Request**

The pacs.009 message has three optional elements to capture the optional information related to the settlement of the instructions.

![](_page_324_Picture_2.jpeg)

**Min 0 – Max 1**

The *Settlement Priority* provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the *Settlement Method* and should not be confused with the *Instruction Priority.* 

![](_page_324_Picture_5.jpeg)

Note: Where the *Settlement Method* of the pacs.009 is 'INDA' (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code 'INGA' implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary. **Min 0 – Max 1**

![](_page_324_Picture_7.jpeg)

The *Settlement Time Indication* optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, *Debit Date Time* and *Credit Date Time*.

![](_page_324_Picture_10.jpeg)

The *Settlement Time Request* optionally captures the time settlement is requested for the payment instruction by the Instructing Agent. This Time can be capture in four nested elements:

- *CLS Time* the time the amount must be credit to CLS Bank
- *Till Time* the time until which the payment may be settled

• *From Time* the time from which the payment may be settled

*Credit Transfer Transaction Information*

## **Agents**

![](_page_325_Figure_1.jpeg)

![](_page_325_Picture_2.jpeg)

*Instructing Agent* and *Instructed Agent* elements are required in all pacs messages and are only available in the *Credit Transfer Information Credit Transfer Transaction Information*

![](_page_325_Picture_4.jpeg)

The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent.

![](_page_326_Picture_1.jpeg)

The *Previous Instructing Agent 1* captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message.

**Min 0 – Max 1**

**Min 0 – Max 1**

The *Previous Instructing Agent 1 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message

![](_page_326_Picture_5.jpeg)

**Min 0 – Max 1**

The *Previous Instructing Agent 2* captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.

**Min 0 – Max 1** The *Previous Instructing Agent 2 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message.

![](_page_326_Picture_10.jpeg)

**Min 0 – Max 1**

The *Previous Instructing Agent 3* captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message. **Min 0 – Max 1**

The *Previous Instructing Agent 3 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in

### **Intermediary Agents**

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. *Intermediary Agent* is an example of this, where these agents are classified in numeric order (i.e., *Intermediary Agent 1*) *Previous Instructing Agent* however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment.

The below diagram visualizes the change of Agent role at different stages of the payment transaction life cycle.

![](_page_327_Picture_3.jpeg)

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

![](_page_328_Picture_1.jpeg)

**Min 0 – Max 1**

The *Intermediary Agent 1* captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 1 Account* captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

![](_page_328_Picture_6.jpeg)

**3**

**Min 0 – Max 1**

The *Intermediary Agent 2* captures the second Intermediary Agent between the Intermediary Agent 1 and the CreditorAgent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 2 Account* captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

![](_page_328_Picture_11.jpeg)

The *Intermediary Agent 3* captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 3 Account* captured the account related to this Intermediary Agent, with the

![](_page_329_Figure_0.jpeg)

#### **Min 0 – Max 1**

The pacs.009 *Debtor Account* is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

**pacs.009 (COV) Financial Institution Credit Transfer – Debtor Account**

The *Debtor Account* uses a variety of nested elements to capture information related to the account.

![](_page_330_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account *Currency* identifies the currency if the account **Min 0 – Max 1 Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

![](_page_330_Picture_8.jpeg)

the pacs.009 the Debtor is a Financial Institution, therefore the nested

The *Debtor Agent* and *Creditor Agent* are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the *Debtor* and *Creditor*. However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship.

![](_page_331_Picture_3.jpeg)

![](_page_331_Picture_4.jpeg)

![](_page_331_Picture_5.jpeg)

Note: Where the *Debtor* and *Creditor* maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the *Creditor Agent* element to align with translation from the legacy MT message.

## **Agent Account**

The pacs.009 *Debtor Agent Account* and *Creditor Agent Account* is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction. **Min 0 – Max 1**

**pacs.009 (COV) Financial Institution Credit Transfer – Debtor Agent Account and Creditor** 

![](_page_332_Picture_2.jpeg)

The *Debtor Agent Account* and *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency if the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

> *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_332_Picture_9.jpeg)

**Min 0 – Max 1**

Debtor Agent and Creditor Agent are Financial Institutions, therefore

![](_page_333_Figure_0.jpeg)

#### **Min 0 – Max 1**

**Min 0 – Max 1**

The pacs.009 *Creditor Account* is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

**pacs.009 (COV) Financial Institution Credit Transfer – Creditor Account**

The *Creditor Account* uses a variety of nested elements to capture information related to the account.

![](_page_334_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account *Currency* identifies the currency if the account **Min 0 – Max 1 Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_334_Picture_8.jpeg)

the pacs.009 the Creditor is a Financial Institution, therefore the

The *Instruction for Next Agent* and *Instruction for Creditor Agent* elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

![](_page_335_Picture_1.jpeg)

**Min 0 – Max 2**

The *Instruction for Creditor Agent* element offers a multiplicity of up to 2 occurrences of information. This element enables:

- ➢ the use of 2 embedded codes to describe the instruction
- ➢ free format *instruction information*
- ➢ or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the *Creditor Agent*. It must be passed on throughout he life cycle of the transaction until the payment reaches the *Credit Agent*.

![](_page_335_Picture_8.jpeg)

**Min 0 – Max 6**

The *Instruction for Next Agent* element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format *instruction information* in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

**Min 0 – Max 1**

The *Purpose* elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used by the capture the nature of the payment e.g. CORT Trade Settlement Payment, CFEE Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.

![](_page_336_Picture_3.jpeg)

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCD is classified within the Collateral categorisation, with the *Name* OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

![](_page_336_Picture_7.jpeg)

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. Category Purpose code SECU 'Securities' may trigger pacs.002 *Payment Status Report* to provide update on the progress of the payment to the previous Agent.

The optional *Remittance Information* element within the pacs.009 COV Financial Institution Credit Transfer is nested to provide *Unstructured* information related to payment.

**Min 0 – Max 1**

*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle.

![](_page_337_Picture_3.jpeg)

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

![](_page_337_Picture_5.jpeg)

Note: the pacs.008 *Remittance Information is captured in the pacs.009 COV within the Underlying Customer Credit Transfer, Remittance Information element. The Remittance Information in the pacs.009 COV is for Creditorthis message (often the Creditor Agent of the pacs.008) As this information is not present in the pacs.008 it is unlikely the pacs.009 COV remittance information will be used.*

![](_page_337_Picture_7.jpeg)

**Transfer**

The *Underlying Customer Credit Transfer* element is used when the pacs.009 *Financial Institution Credit Transfer* message is being utilized to cover a pacs.008 *FI to FI Customer Credit Transfer*. The information contained within this nested element relates directly to the information exchanged between the Instructing Agent and Instructed Agent of the pacs.008 FI to FI Customer Credit Transfer and can be compared with Sequence B of the legacy MT 202 COV.

![](_page_338_Figure_2.jpeg)

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Cover Method Financial Institution Payments**

Use Case p.9.2.1 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV)

Use Case p.9.2.2 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) over a Payment Market Infrastructure

Use Case p.9.2.3 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) where an incorrect intermediary is used

Use Case p.9.2.4 – High Level FI to FI Customer Credit Transfer involved a serial leg into a cover method (pacs.009 COV)

Use Case p.9.2.5 – High Level FI to FI Customer Credit Transfer involved a serial leg in and out of a cover method (pacs.009 COV)

Use Case p.9.2.6 - High Level FI to FI Customer Credit Transfer involved a serial leg out of a cover method (pacs.009 COV)

![](_page_340_Figure_0.jpeg)

![](_page_341_Figure_0.jpeg)

![](_page_342_Figure_0.jpeg)

![](_page_343_Figure_0.jpeg)

![](_page_344_Figure_0.jpeg)

![](_page_345_Figure_0.jpeg)

## <span id="page-346-0"></span>**FI to FI Payment Status Report**

![](_page_347_Picture_0.jpeg)

The Financial Institution To Financial Institution Payment Status Report message is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an instruction. It is also used to report on a pending instruction

![](_page_348_Figure_0.jpeg)

![](_page_349_Figure_0.jpeg)

<span id="page-349-0"></span>![](_page_349_Figure_1.jpeg)

The FIToFIPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an instruction. It is also used to report on a pending instruction.

## **Group Header**

![](_page_351_Picture_1.jpeg)

Each ISO 20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

The pacs.002 message *Creation Date* captures the date and time which the message was created.

![](_page_352_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_352_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

## **Transaction Information and Status**

The pacs.002 FI to FI Payment Status Report uses elements in the *Original Group Information* to capture the message identifier and message name of the underlying payment the *Payment Status Report* relates to. The mandatory *Original Message Identification* contains the point-to-point reference, and the mandatory **Min 1 – Max 1**

*Original Message Name Identification* contains the message name of the underlying payment being reported upon. Optionally the *Original Creation Date Time* can also be captured.

**<sup>A</sup> <sup>B</sup>** For example:

*Original Message Name Identification* "pacs.008.001.08" confirms the Status Report is of a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as "pacs.009.001.08" confirms the Status Report is of a pacs.009 Financial Institution Credit Transfer.

**pacs.002** Message Identification abcd1234 pacs.008.001.**<sup>08</sup>** Original Message Original Message Identification abcd1234 Message Identification xyz9875 Original Group Information Group Header **pacs.008**

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message The pacs.002 *FI to FI Payment Status Report* also uses a number of other **Original** elements in the *Transaction Information And Status* to capture information from the underlying payment that the *Payment Status Report* relates to.

![](_page_355_Picture_1.jpeg)

**Mandatory** element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) include:

*Original End to End Identification Original UETR*

**Min 1 – Max 1**

**Min 1 – Max 1**

Optionally *Original Transaction Identification* and *Original Instruction Identification* may also be used. **Min 0 – Max 1 Min 0 – Max 1**

These Original elements enables the *Instructed Agent* in the pacs.002 *Payment Status Report* to associate the Payment Status with the payment they originally sent.

*Transaction Information and Status*

*Original Instruction Identification*

*Original End to End Identification*

**Min 1 – Max 1**

The pacs.002 *FI to FI Payment Status Report Transaction Status* utilizes the externalized ISO *Payment Transaction Status* code list to provide a status update on a pacs message previously received. The *Transaction Status* element is arguable the most significant/core parts of the pacs.002 and optionally may further be complimented with *Status Reason Information.*

**Min 0 – Max 1**

![](_page_356_Picture_3.jpeg)

The nested *Status Reason Information* enable the optional inclusion of:

*Originator* – the party that issues the status. Typically, the pacs.002 Instructing Agent and therefore Originator is not necessary.

*Reason* – which utilizes either an ISO external Status Reason code or a proprietary reason. For example, **AC04** 'Closed Account Number' would compliment a RJCT (Reject) Transaction Status.

*Additional Information* – a text element to provide further status reason information, necessary where the *Reason* code is NARR

![](_page_356_Picture_8.jpeg)

Note: A *Reason* code must be provided where the *Transaction Status* RJCT (Reject) code is used.

The next two slides take a look at:

- The code relevant to CBPR+ Payment Statuses, the codes description and the High Level Use Case.
- Logical order in which these codes may be used in one or multiple Payment Status Report updates.

| Code | Name                        | ISO Definition                                                                                                                                                     | High Level Use Case                                                                                                                                                     |
|------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACCC | AcceptedSettlementCompleted | Settlement on the creditor's account has been completed.                                                                                                           | Sent by Creditor Agent to confirm the settlement on<br>the creditor's account                                                                                           |
| ACCP | AcceptedCustomerProfile     | Preceding check of technical validation was successful. Customer<br>profile check was also successful.                                                             | Sent by any Agent<br>in the payment chain to confirm acceptance prior to<br>technical validation.                                                                       |
| ACFC | AcceptedFundsChecked        | Preceding check of technical validation and customer profile was<br>successful and an automatic funds check was positive.                                          | Sent by any Agent<br>in the payment chain to confirm the technical validation/<br>profile w as positive<br>and automatic funds check w as positive.                     |
| ACIS | AcceptedandChequeIssued     | Payment instruction to issue a cheque has been accepted, and the<br>cheque has been issued but not yet been deposited or cleared.                                  | Sent by any Agent<br>in the payment chain to confirm a cheque has been issued<br>as requested.                                                                          |
| ACSC | AcceptedSettlementCompleted | Settlement has been completed.                                                                                                                                     | Sent by the Any Agent to confirm settlement of a payment message leg.                                                                                                   |
| ACSP | AcceptedSettlementInProcess | All preceding checks such as technical validation and customer<br>profile were successful and therefore the payment initiation has been<br>accepted for execution. | Sent by any Agent to the to confirm the payment is accepted follow ing<br>technical validations being successfully completed.                                           |
| ACTC | AcceptedTechnicalValidation | Authentication and syntactical and semantical validation are<br>successful                                                                                         | Sent by any<br>Agent in the payment chain to the previous Agent to confirm the<br>payment is accepted follow ing technical validations being successfully<br>completed. |
| ACWC | AcceptedWithChange          | Instruction is accepted but a change will be made, such as date or<br>remittance not sent.                                                                         | Sent by any<br>Agent in the payment chain to the previous Agent to confirm the<br>payment is accepted follow ing amendments being made.                                 |
| ACWP | AcceptedWithoutPosting      | Payment instruction included in the credit transfer is accepted<br>without being posted to the creditor customer's account.                                        | Sent by Creditor Agent to the previous<br>Agent to confirm the acceptance of<br>payment w ithout settlement on the creditor's account,                                  |
| CPUC | CashPickedUpByCreditor      | Cash has been picked up by the Creditor.                                                                                                                           | Sent by Creditor Agent to the previous<br>Agent to confirm that<br>the cash<br>collection has been picked up by the Creditor,                                           |
| PDNG | Pending                     | Payment initiation or individual transaction included in the payment<br>initiation is pending. Further checks and status update will be<br>performed.              | Sent<br>by any<br>Agent in the payment chain to the previous Agent as an interim<br>status w hilst other validations are performed.                                     |
| RCVD | Received                    | Payment initiation has been received by the receiving agent.                                                                                                       | Sent by Any Agent to the previous Agent as confirmation that their Customer                                                                                             |

The pacs.002 *Payment Transaction Status* element facilitates updates to the previous Agent on changes to the status of the payment. Such Status Information messages (pacs.002), with the exception of **reject code RJCT** which **is mandatory in CBPR+**, are bilateral agreed, where upon a variety of these Transaction Statuses may be used by the Instructed Agent at different stages of the payment processing.

This diagram illustrates the logical order in which these codes may be used during the processing of the Payment ClearingAnd Settlement message (pacs) and the role of the Agent in providing these status.

![](_page_358_Figure_2.jpeg)

| Code | Name                        | ISO Definition                                                                                                                                                                                                                | High Level Use Case                                                                                                                                               |
|------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC01 | IncorrectAccountNumber      | Format of the account number specified is not correct or Account<br>number is missing                                                                                                                                         | Sent by Instructed Agent w hen<br>a settlement account number is incorrect                                                                                        |
| AC02 | InvalidDebtorAccountNumber  | Debtor account number invalid or missing                                                                                                                                                                                      | Sent by Instructed Agent w hen Debtor account number is incomplete                                                                                                |
| AC04 | ClosedAccountNumber         | Account number specified has been closed on the bank of<br>account's books                                                                                                                                                    | Sent by Creditor Agent w hen the Creditor account number is closed                                                                                                |
| AC06 | BlockedAccount              | Account specified is blocked, prohibiting posting of transactions<br>against it.                                                                                                                                              | Sent by Creditor Agent w hen Creditor account is blocked from posting<br>credit entries.<br>Sent by Instructed Agent w hen a settlement account is blocked        |
| AC07 | ClosedCreditorAccountNumber | Creditor account number closed                                                                                                                                                                                                | Sent by Creditor Agent w hen account number is closed.<br>CBPRplus recommend using AC04, but support AC07 to remain<br>interoperable with other clearing systems. |
| AC13 | InvalidDebtorAccountType    | Debtor account type is missing or invalid                                                                                                                                                                                     | Sent by Instructed Agent w hen Debtor account type element is incorrect                                                                                           |
| AGNT | IncorrectAgent              | Agent in the payment w orkflow is incorrect                                                                                                                                                                                   | Sent by Instructed Agent w hen an agent in the payment transaction has<br>an incorrect identification element                                                     |
| AG01 | TransactionForbidden        | Transaction forbidden on this type of account (formerly<br>NoAgreement)                                                                                                                                                       | Sent by Instructed Agent w hen the type of payment transaction is not<br>allow ed for the specified account                                                       |
| AG07 | UnsuccesfulDirectDebit      | Debtor account cannot be debited for a generic reason.<br>Code value may be used in general purposes and as a<br>replacement for AM04 if debtor bank does not reveal its<br>customer's insufficient funds for privacy reasons | Sent by Debtor Agent of a Direct Debit message, w hen debtor account<br>can not be debited                                                                        |
| AM02 | NotAllow edAmount           | Specific transaction/message amount is greater than allow ed<br>maximum                                                                                                                                                       | Sent by Instructed Agent w hen payment amount is above an allow ed<br>amount. For example the clearing system w ith a upper amount threshold                      |

| Code | Name                        | ISO Definition                                                                                                                        | High Level Use Case                                                                                                                                                      |
|------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AM03 | NotAllowedCurrency          | Specified message amount is a non processable currency<br>outside of existing agreement                                               | Sent by Instructed Agent w hen<br>the currency of the payment is not allow ed<br>w ithin the existing business agreement                                                 |
| AM04 | InsufficientFunds           | Amount of funds available to cover specified message<br>amount is insufficient.                                                       | Sent by Instructed Agent w hen<br>there is not sufficient funds to settle the<br>payment transaction.                                                                    |
| AM05 | Duplication                 | Payment is a duplicate of another payment                                                                                             | Sent by Instructed Agent w hen<br>the payment is a duplicate. CBPRplus<br>recommend using DUPL, but support AM05 to remain interoperable with other<br>clearing systems. |
| AM06 | TooLowAmount                | Specified transaction amount is less than agreed<br>minimum.                                                                          | Sent by Instructed Agent w hen<br>the payment amount is below a minimum<br>amount.                                                                                       |
| AM07 | BlockedAmount               | Amount specified in message has been blocked by<br>regulatory authorities                                                             | Sent by Instructed Agent w hen the payment amount is blocked by regulators                                                                                               |
| AM09 | WrongAmount                 | Amount received is not the amount agreed or expected                                                                                  | Sent by Instructed Agent w hen<br>the payment amount is incorrect                                                                                                        |
| BE01 | InconsistenWithEndCustomer  | Identification of end customer is not consistent with<br>associated account number (formerly<br>CreditorConsistency).                 | Sent by Creditor Agent w hen there is an inconsistency betw een the Creditor's<br>identification and the account number                                                  |
| BE04 | MissingCreditorAddress      | Specification of creditor's address, which is required for<br>payment, is missing/not correct (formerly<br>IncorrectCreditorAddress). | Sent by Instructed Agent<br>w hen the Creditor's address is missing<br>Sent by Creditor Agent<br>w hen the Creditor's address is incorrect                               |
| BE05 | UnrecognisedInitiatingParty | Party who initiated the message is not recognised by the<br>end customer                                                              | Sent by Creditor Agent w hen<br>the initiating party is unknow n<br>to the beneficiary                                                                                   |
| BE07 | MissingDebtorAddress        | Specification of debtor's address, which is required for<br>payment, is missing/not correct.                                          | Sent by Instructed<br>Agent w hen the address of the Debtor is missing or<br>incorrect                                                                                   |

| Code | Name                              | ISO Definition                                                                                  | High Level Use Case                                                                                                                                                                                         |
|------|-----------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BE10 | InvalidDebtorCountry              | Debtor country code is missing or invalid                                                       | Sent by Instructed Agent w hen the country code of the Debtor is missing or<br>incorrect                                                                                                                    |
| BE11 | InvalidCreditorCountry            | Creditor country code is missing or invalid                                                     | Sent by Instructed Agent w hen<br>the country code of the Creditor is missing or<br>incorrect                                                                                                               |
| BE16 | InvalidDebtorIdentificationCode   | Debtor or Ultimate Debtor identification code missing or<br>invalid                             | Sent by Instructed Agent w hen the identification of the Debtor or Ultimate<br>Debtor is missing or incorrect                                                                                               |
| BE17 | InvalidCreditorIdentificationCode | Creditor or Ultimate Creditor identification code missing<br>or invalid                         | Sent by the Instructed Agent w hen the identification of the Creditor or<br>Ultimate<br>Creditor is missing or incorrect                                                                                    |
| CN01 | AuthorisationCancelled            | Authorisation is cancelled.                                                                     | Sent by Instructed Agent w hen a third party debit authorisation has been<br>cancelled or is not in place.                                                                                                  |
| CNOR | Creditor bank is not registered   | Creditor bank is not registered under this BIC in the<br>Clearing Settlement Mechanism<br>(CSM) | Sent by Instructed Agent w hen the Creditor Agent is not reachable in the<br>Market Infrastructure (CSM) and an appropriate correspondent can not be<br>determined.                                         |
| CURR | IncorrectCurrency                 | Currency of the payment is incorrect                                                            | Sent by the Creditor<br>Agent w hen the Interbank Settlement Amount<br>Currency<br>is not the same as the Creditor account currency and a currency<br>conversion is not accepted on the Creditor's account. |
| CUST | RequestedByCustomer               | Cancellation requested by the Debtor                                                            | Sent by Instructed Agent upon request by Debtor. CBPRplus recommend<br>using FOCR, but support CUST to remain interoperable with other clearing<br>systems.                                                 |
| DT01 | InvalidDate                       | Invalid date (eg, wrong or missing settlement date)                                             | Sent by Instructed Agent w hen the settlement date is in the past and an<br>agreement is in place to reject rather than apply the next possible value date.                                                 |
| DT04 | FutureDateNotSupported            | Future date not supported                                                                       | Sent by Instructed Agent w hen a future settlement date is not supported or<br>appear to be an error e.g. is the w rong year.                                                                               |

| Code | Name                          | ISO Definition                                                                                                               | High Level Use Case                                                                                                                                                |
|------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DUPL | DuplicatePayment              | Payment is a duplicate of another payment                                                                                    | Sent by Instructed Agent w hen the payment is a duplicate                                                                                                          |
| ERIN | ERIOptionNotSupported         | The Extended Remittance Information (ERI) option is not<br>supported.                                                        | Sent by Instructed Agent w hen extended Remittance information (Related<br>Remittance Information) is not supported or bilaterally/multilaterally agreed           |
| ED05 | SettlementFailed              | Settlement of the transaction has failed.                                                                                    | Sent by Instructed Agent w hen the settlement of payment has failed or been<br>unsuccessful.                                                                       |
| FF03 | InvalidPaymentTypeInformation | Payment Type Information is missing or invalid.<br>Generic usage if cannot specify Service Level or Local<br>Instrument code | Sent by Instructed Agent w hen the Payment Type Information (Instruction<br>Priority, Clearing Channel) provided for the payment is incorrect or not<br>supported. |
| FF04 | InvalidServiceLevelCode       | Service Level code is missing or invalid                                                                                     | Sent by Instructed Agent w hen the Payment Type Information Service Level<br>provided for the payment is incorrect or not supported                                |
| FF05 | InvalidLocalInstrumentCode    | Local Instrument code is missing or invalid                                                                                  | Sent by Instructed Agent w hen the Payment Type Information Local<br>Instrument<br>provided for the payment is incorrect or not supported                          |
| FF06 | InvalidCategoryPurposeCode    | Category Purpose code is missing or invalid                                                                                  | Sent by Instructed Agent w hen the Payment Type Information Category<br>Purpose<br>provided for the payment is incorrect or not supported                          |
| FF07 | InvalidPurpose                | Purpose is missing or invalid                                                                                                | Sent by Instructed Agent w hen the Purpose provided for the payment is<br>either missing or incorrect                                                              |
| FOCR | FollowingCancellationRequest  | Return following a cancellation request                                                                                      | Sent by Instructed Agent that has accepted a payment cancellation request<br>(camt.056) and subsequently is rejecting the unsettled payment instruction.           |
| FR01 | Fraud                         | Returned as a result of fraud.                                                                                               | Sent by Instructed Agent w hen the payment is identified as fraudulent.                                                                                            |

MD01 NoMandate No Mandate Sent by **Instructed Agent** w hen a Direct Debit message has no mandate in

|      |                                         |                                                                                                                                                                                                  | Definitions and High Level Use Cases                                                                                                                                                   |
|------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | Name                                    | ISO Definition                                                                                                                                                                                   | High Level Use Case                                                                                                                                                                    |
| MD02 | MissingMandatoryInformationIn Mandate   | Mandate related information data required by the scheme is missing.                                                                                                                              | Sent by <b>Instructed Agent</b> when information required by the clearing scheme is missing.                                                                                           |
| MD05 | CollectionNotDue                        | Creditor or creditor's agent should not have collected the direct debit                                                                                                                          | Sent by Instructed Agent when a Direct Debit collection was not due                                                                                                                    |
| MD07 | EndCustomerDeceased                     | End customer is deceased.                                                                                                                                                                        | Sent by Creditor Agent when the Creditor or Ultimate Creditor is deceased                                                                                                              |
| MS02 | NotSpecifiedReasonCustomer<br>Generated | Reason has not been specified by end customer                                                                                                                                                    | Sent by <b>Creditor Agent</b> where instructed to reject by the Creditor, but no reason was specified                                                                                  |
| MS03 | NotSpecifiedReasonAgent<br>Generated    | Reason has not been specified by agent.                                                                                                                                                          | Sent by Instructed Agent but no reason is specified                                                                                                                                    |
| NARR | Narrative                               | Reason is provided as narrative information in the additional reason information.                                                                                                                | Sent by <b>Instructed Agent</b> the reason is provided as narrative information. <b>Only to be used where no other code is appropriate!</b> (i.e. exceptional circumstances)           |
| NOAS | NoAnswerFromCustomer                    | No response from Beneficiary                                                                                                                                                                     | Sent by <b>Instructed Agent</b> when the Creditor did not respond to query for additional information in order that the payment could be credited e.g. currency control documentation. |
| NOCM | Not compliant (more generic)            | Customer account is not compliant with regulatory requirements, for example FICA (in South Africa) or any other regulatory requirements which render an account inactive for certain processing. | Sent by <b>Instructed Agent</b> when the Creditor account is not compliant with certain regulatory requirements.                                                                       |
| RC01 | BankldentifierIncorrect                 | Bank Identifier code specified in the message has an incorrect format (formerly IncorrectFormatForRoutingCode).                                                                                  | Sent by <b>Instructed Agent</b> when an incorrect BIC has been used in the payment                                                                                                     |
| PC03 | InvalidDebtorBankIdentifier             | Debter bank identifier is invalid or missing                                                                                                                                                     | Sent by Instructed Agent when the Debtor Agent identification is incorrect or                                                                                                          |

| Code | Name                                        | ISO Definition                                                                                                                                | High Level Use Case                                                                                                                                 |
|------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| RC04 | InvalidCreditorBankIdentifier               | Creditor bank identifier is invalid or missing                                                                                                | Sent by Instructed Agent w hen the Creditor Agent identification is incorrect or<br>missing                                                         |
| RC08 | InvalidClearingSystemMemberIden<br>tifier   | ClearingSystemMemberidentifier is invalid or missing.<br>Generic usage if cannot specify between debit or credit<br>account                   | Sent by Instructed Agent w hen the clearing system member identification for<br>an Agent is incorrect                                               |
| RC11 | InvalidIntermediaryAgent                    | Intermediary Agent is invalid or missing                                                                                                      | Sent by Instructed Agent w hen the intermediary agent identification is<br>incorrect                                                                |
| RF01 | NotUniqueTransactionReference               | Transaction reference is not unique within the<br>message.                                                                                    | Sent by Instructed Agent w hen the transaction reference (UETR and<br>Instruction Identification) are not unique                                    |
| RR01 | Missing Debtor Account or<br>Identification | Specification of the debtor's account or unique<br>identification needed for reasons of regulatory<br>requirements is insufficient or missing | Sent by Instructed Agent w hen the Debtor identification or debtor account is<br>missing, or the information provided are not sufficient            |
| RR02 | Missing Debtor Name or Address              | Specification of the debtor's name and/or address needed for<br>regulatory requirements is insufficient or missing.                           | Sent by<br>Instructed Agent<br>since the Debtor name or Address is<br>missing, or<br>information provided is not sufficient                         |
| RR03 | Missing Creditor Name or Address            | Specification of the creditor's name and/or address needed<br>for regulatory requirements is insufficient or missing.                         | Sent by Instructed Agent since the Creditor name or Address is<br>missing, or<br>information provided is not sufficient                             |
| RR04 | Regulatory Reason                           | Regulatory Reason                                                                                                                             | Sent<br>by Instructed Agent<br>due to any unspecified regulatory reason                                                                             |
| RR05 | RegulatoryInformationInvalid                | Regulatory or Central Bank Reporting information missing,<br>incomplete or invalid.                                                           | Sent<br>by Instructed Agent<br>w hen the reporting<br>information required by the<br>central bank or reporting authority is missing or not complete |

RR06 TaxInformationInvalid Tax information missing, incomplete or invalid. Sent by **Instructed Agent** w here required tax information is missing, not valid

| Code | Name                               | ISO Definition                                                                                                         | High Level Use Case                                                                                                                                                                                                                                                             |
|------|------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RR07 | RemittanceInformationInvalid       | Remittance information structure does not comply w ith rules<br>for payment type.                                      | Sent by<br>Instructed Agent<br>since the<br>remittance information is incorrect                                                                                                                                                                                                 |
| RR08 | RemittanceInformationTruncated     | Remittance information truncated to comply w ith rules for<br>payment type.                                            | Sent by<br>Instructed Agent<br>w here the Structured Remittance Information<br>has not been bilaterally or multilaterally agreed, w hich or has resulted in<br>truncation                                                                                                       |
| RR09 | InvalidStructuredCreditorReference | Structured creditor reference invalid or missing.                                                                      | Sent by<br>Instructed Agent<br>w hen the structure of the creditor reference<br>in<br>the remittance information is invalid or missing                                                                                                                                          |
| RR11 | InvalidDebtorAgentServiceID        | Invalid or missing identification of a bank proprietary service.                                                       | Sent by<br>Instructed Agent w here the proprietary<br>identification for the Debtor<br>is invalid<br>or not understood                                                                                                                                                          |
| RR12 | InvalidPartyID                     | Invalid or missing identification required w ithin a particular<br>country or payment type.                            | Sent<br>by Instructed Agent w here a proprietary party identification<br>is<br>considered invalid<br>or not understood                                                                                                                                                          |
| RUTA | ReturnUponUnableToApply            | Return following investigation request and no remediation<br>possible.                                                 | Sent by Instructed Agent that is unsatisfied w ith the outcome of the unable<br>to apply request and is subsequently rejecting the payment instruction.<br>Alternatively it can be used by the original Creditor Agent w hen the creditor<br>is unable to apply the transaction |
| TM01 | Invalid Cut off time               | Associated message, payment information block, or<br>transaction was received after agreed processing cut-off<br>time. | Sent by Instructed Agent w hen the message w as received after the<br>agreed processing cut off time and an agreement is in place to reject rather<br>than apply the next possible value date.                                                                                  |
| UPAY | UnduePayment                       | Payment is not justified.                                                                                              | Sent by Instructed Agent the payment is undue                                                                                                                                                                                                                                   |

| Code | Name               | ISO Definition                                                                                                                                                                                          | High Level Use Case                                                                                                                    |
|------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| G004 | CreditPendingFunds | In a FIToFI Customer Credit Transfer: Credit to the<br>creditor's account is pending, status Originator is waiting<br>for funds provided via a cover. Update will follow from the<br>Status Originator. | Optionally sent by the Creditor Agent w ent the cover has not been settled at<br>the creditor agent account at the reimbursement agent |

The pacs.002 *FI to FI Payment Status Report* optional *Effective Interbank Settlement Date* allows a choice of *Date* or *Date Time* to confirm when a point-to-point transaction is completed/effected.

![](_page_367_Picture_2.jpeg)

When *Date Time* is chosen CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

*Transaction Information and Status*

![](_page_368_Figure_0.jpeg)

![](_page_368_Picture_1.jpeg)

<span id="page-369-0"></span>Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Serial Financial Institution to Financial Institution to Customer Credit Transfer**

Use Case p.2.1.1 – High Level Payment Status Information (pacs.002) of multiple Payment Transaction Status updates

Use Case p.2.1.2 – High Level Rejection of an incomplete Customer Credit Transfer (pacs.008)

#### **Serial Financial Institution Credit Transfer**

Use Case p.2.2.1 – High Level Rejection of an incomplete Financial Institution Credit Transfer (pacs.009)

#### **Cover Method Financial Institution to Financial Institution to Customer Credit Transfer**

Use Case p.2.3.1.a – High Level Rejection of an incomplete payment using the cover method

Use Case p.2.3.1.b – High Level Rejection of an incomplete payment using the cover method

#### **Financial Institution Direct Debit**

Use Case p.2.4.1 – High Level Status Information of a Financial Institution Direct Debit

Use Case p.2.4.2 – High Level Rejection of a Financial Institution Direct Debit

#### **Financial Institution to Financial Institution Customer Direct Debit**

Use Case p.2.5.1 – High Level FI to FI Customer Direct Debit (pacs.003) successful settlement

Use Case p.2.5.2 – High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement

### **Transaction Status updates**

An agent may provide multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle i.e. from receipt through to onward processing.

![](_page_370_Figure_2.jpeg)

Where a payment is rejected, the use of the pacs.002

![](_page_371_Figure_0.jpeg)

![](_page_371_Picture_1.jpeg)

Agent B processes the payment on Agent C

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent C processes the payment on Agent D

Having received the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D rejects the payment to Agent C using a Status information message (pacs.002) also including the return reason code

Agent C return funds to Agent B, together with the reason code for return.

## (pacs.009)

![](_page_372_Figure_1.jpeg)

![](_page_372_Picture_2.jpeg)

- Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)
- Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent E) using Agents C as an intermediary.
- Agent C processes the payment onto Agent D

- Having received the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D rejects the payment to Agent C using a Status Information message (pacs.002) also including the reject code.
- Agent C return funds to Agent B, together with the reason code for return.
- Agent B advises Agent A of the return of payment together with the reason using the camt.053 and may optionally provide a notification e.g. credit notification.

<span id="page-373-0"></span>![](_page_373_Figure_0.jpeg)

![](_page_374_Figure_0.jpeg)

## **(pacs.010)**

![](_page_375_Figure_1.jpeg)

![](_page_375_Figure_2.jpeg)

Agent E initiates a Direct Debit instruction to debit Agent A's account 1

Agent B provides a positive status update to Agent E 1a

Debtor Agent (B) initiates a serial payment towards the Creditor Agent (E) using Agents B & C as intermediaries 2

Agent C processes the payment on Agent D

3

Agent D credits the account of the Creditor (Agent E), and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

![](_page_376_Picture_0.jpeg)

1

![](_page_376_Figure_1.jpeg)

Agent D initiates a Direct Debit instruction to debit Agent A's account

Debtor Agent (B) rejects the instruction, using a pacs.002, as no mandate agreement is in place.

<span id="page-377-0"></span>![](_page_377_Figure_0.jpeg)

Creditor initiates a direct debit instruction to the Creditor Agent

Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method "INDA" 2

The Debtor Agent debits the account of the Debtor, and may optionally provide a notification e.g. debit notification in addition to an account statement (camt.053). The Debtor Agent also provides a status update ACSC (accepted settlement completed) to the Creditor Agent.

3

Creditor Agent (A) relays the status ACSC (accepted settlement completed) to the Initiating Party, based upon a bilateral agreement

![](_page_378_Picture_0.jpeg)

![](_page_378_Figure_1.jpeg)

Creditor initiates a direct debit instruction to the Creditor Agent

Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method "INDA" 2

The Debtor Agent fails to debit the account of the Debtor (e.g., account is closed). The Debtor Agent provides a status update RJCT (Rejected) with the rejection reason information.

3

Creditor Agent (A) relays the status RJCT (Rejected) to the Initiating Party with the rejection reason information

## <span id="page-379-0"></span>**Payment Return**

![](_page_380_Figure_0.jpeg)

In a similar structure to the pacs.009 (cov) underlying Customer Credit Transfer, the pacs.004 Payment Return message has amongst other elements Original Group Information which captures original information such as the Original UETR and Original Interbank Settlement Amount etc. and an Original Transaction Reference which contain the key elements of the original payment e.g. Debtor, Creditor etc.

### **FI Customer Payment (pacs.008) pacs.008 pacs.002 pacs.008 pacs.004 pacs.002 Return & Reason pacs.002 Reject & Reason A B C** The PaymentReturn message is sent by an agent to the previous agent in the payment chain to undo a payment previously settled.

![](_page_381_Picture_1.jpeg)

In the unlikely event that a pacs.004 is instructed by mistake, the best practice is to allow the Payment Return

## **Group Header**

![](_page_383_Picture_1.jpeg)

Each ISO 20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

![](_page_383_Picture_4.jpeg)

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-endTransactionReference)

The pacs.004 message *Creation Date* captures the date and time which the message was created.

![](_page_384_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_384_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The pacs.004 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_385_Picture_2.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_385_Picture_4.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

**Min 1 – Max 1**

The pacs.004 *Settlement Method* element within the Group Header *Settlement Information*, includes one of the embedded codes to indicate how the payment message will be settled.

The *Settlement Method* element in the pacs.004 allows a choice of an embedded code.

![](_page_386_Picture_3.jpeg)

**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated *Settlement Account* element.

**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated *Settlement Account*  element.

![](_page_386_Picture_6.jpeg)

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification (HVPS+)

The pacs.004 message *Settlement Account* is a nested element as part of *Settlement Information,* this element identifies information related to an account used to settle the payment instruction.

**Min 0 – Max 1**

The *Settlement Account* identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the *Settlement Method*)

![](_page_387_Picture_3.jpeg)

**Min 0 – Max 1**

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account

*Currency* identifies the currency if the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

## **Transaction Information**

**Min 0 – Max 1** The pacs.004 message *Return Identification* captures a point-to-point reference used to unambiguously identify the Payment Return message, created by the *Instructing Agent* in the *Return Chain*.

![](_page_389_Picture_1.jpeg)

The 35 character return identifier could be considered similar to the legacy Sender's Reference (Field 20) of an MT return payment message.

**Min 0 – Max 1**

The pacs.004 *Payment Return* uses elements in the *Original Group Information* to capture the message identifier and message name of the underlying payment the *Payment Return* relates to. The mandatory *Original Message Identification* contains the point-to-point reference, and the mandatory *Original Message Name Identification* contains the message name of the underlying payment being returned. Optionally the *Original Creation Date Time* can also be captured.

*Original Message Name Identification* "pacs.008.001.xx" confirms the return is of a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as "pacs.009.001.xx" confirms the return is of a pacs.009 Financial Institution Credit Transfer.

**pacs.004 <sup>A</sup> <sup>B</sup>** For example: Message Identification abcd1234 **pacs.008.001.08** Original Message Original Message Identification abcd1234 Message Identification xyz9875 Original Group Information Group Header **pacs.008**

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message The pacs.004 *Payment Return* also uses a number of other **Original** elements in the *Transaction Information* to capture information from the underlying payment that the *Payment Return* relates to. **Mandatory** element examples of this (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) include:

![](_page_391_Picture_2.jpeg)

*Identification* These Original elements enables the *Instructed Agent* in the pacs.004 *Payment Return* to re-associate the Return with the payment they originally sent.

![](_page_391_Picture_4.jpeg)

## **Settlement Date**

![](_page_392_Picture_1.jpeg)

**Min 1 – Max 1 Min 1 – Max 1**

The *Returned Interbank Settlement Amount* and subsequent *Interbank Settlement Date* are mandatory elements in the pacs.004 *Payment Return,* these elements are used to capture the currency and amount being returned together with the settlement date of the Payment Return.

![](_page_392_Picture_4.jpeg)

The *Returned Interbank Settlement Amount* may be a different amount than the *Original Interbank Settlement Amount* (amount received the Agent instructing the *Payment Return*) for example a charge may have been levied for processing the *Payment Return* or the Payment Return is a partial amount for overpayment or partial refund

In this case the *Returned Instructed Amount* should be equal to the *Interbank Settlement Amount,* on the first leg of the *Payment Return.* Charge levied should also be captured in the *Charge Information* element.

The pacs.004 message has two optional elements to capture the optional information related to the settlement of the instructions.

![](_page_393_Picture_1.jpeg)

![](_page_393_Picture_2.jpeg)

The *Settlement Priority* provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the *Settlement Method* and should not be confused with the *Instruction Priority.* 

![](_page_393_Picture_4.jpeg)

Note: Where the *Settlement Method* of the pacs.004 is 'INDA' (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code 'INGA' implies settlement has already occurred for this point-to-point payment and therefore the SettlementPriority is not necessary.

![](_page_393_Picture_6.jpeg)

**Min 0 – Max 1**

The *Settlement Time Indication* optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, *Debit Date Time* and *Credit Date Time*.

*Transaction Information*

![](_page_394_Picture_0.jpeg)

**Min 0 – Max 1**

The *Returned Instructed Amount* captures currency and amount instructed by the *Debtor* in the *Return Chain*. This conditional element is required when the *Returned Interbank Settlement Amount* is not the same currency and/or amount as originally instructed by the *Debtor.* For example a charge is taken or the transactions is converted to another currency.

![](_page_394_Picture_3.jpeg)

**Min 0 – Max 1**

The *Exchange Rate* capture the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency.

*Transaction Information*

#### **Min 1 – Max 1**

The pacs.004 *Charge Bearer* element uses an embedded code that is used to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

| Charge | Code | Description |               |      |                |  |
|--------|------|-------------|---------------|------|----------------|--|
| Bearer | CRED | Creditor    |               |      |                |  |
| (1.1)  | SHAR | Shared      | 71A: Details  | Code | Description    |  |
|        |      |             | of<br>Charges | BEN  | Beneficiary    |  |
|        |      |             |               | SHA  | Shared Charges |  |
|        |      |             |               |      |                |  |

![](_page_395_Picture_3.jpeg)

Note: *Charge Bearer* code DEBT (implying the *Return Chain,* **Debtor** will bear any charges) is removed from the CBPR+ pacs.004. Should a non-CBPR+ Payment Return be received with Charge Bearer DEBT, it is recommended to use SHAR in any onward processed Payment Return.

The *Charges Information* element provides information on the return charges to be paid by the *Charge Bearer*. This element is comparable with MT Fields: 71F 'Senders Charges' and 71G 'Receiver's Charges', although pre-paid charges (legacy 71G 'Receiver's Charges' are an unlikely use case for Payment Returns **Min 0 – Max \* Min 0 – Max 1**

| Charge      | Amount<br>Currency |                          | In<br>addition<br>to<br>the<br>legacy<br>MT<br>message<br>the<br>pacs.004<br>Charge                                                                              |
|-------------|--------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Information |                    |                          | Information<br>mandate<br>the<br>Agent,<br>this<br>represent<br>the<br>Agent                                                                                     |
| (0.*)       | Agent              | BICFI                    | who<br>has<br>taken<br>a<br>charge<br>(deduct<br>from<br>the<br>transaction)<br>CBPR+<br>best<br>practice<br>recommends<br>the<br>use<br>of<br>the<br>structured |
|             |                    | Name                     | Agent<br>BIC.                                                                                                                                                    |
|             |                    | StructuredPostal Address |                                                                                                                                                                  |

As the *Charges Information* element is repetitive it can capture charges related to previous legs of the Payment Return transaction chain.

![](_page_396_Picture_4.jpeg)

Note: *Charge Information* element is required where a charge is taken on the Payment Return. A charge for returning an incomplete payment by the originator of the Payment Return (Return Chain Debtor) is common practice. It is encouraged that Agents who processed the original payment transaction consider the total operation cost when defining their payment cost recovery model. Whereby further charges on Return Payments should be avoided.

*Transaction Information* Charge Information

![](_page_397_Figure_0.jpeg)

roles therefore change on each payment

#### Min 1 - Max 1

<span id="page-398-0"></span>The mandatory *Return Chain* element captures all the parties involved in the return transaction, in much the same way the underlying payment message captures all the parties involved in a payment.

In this element the **role** of the various parties **change**, to reflect the fact the payment is now a *Payment Return*, for example, the *Creditor Agent* of the underlying payment may become the *Debtor Agent* of the *Payment Return*.

Although Ultimate Debtor and Ultimate Creditor are present in the Return chain it is extremely unlikely one of these Parties would be involved in the return chain and can only do so if present as an Ultimate Party in the original payment.

![](_page_398_Figure_4.jpeg)

Note: the static Previous Instructing Agent roles in the original payment transition to

Arguably the most common example of a Payment Return is where it is initiated by the Creditor Agent of the original payment, this Agent's role the become the mandatory Debtor in the *Return Chain* element (as they owe the money to the party the return is intended for).

Recognising that the original Creditor is not party to the return, for example, they might be a known customer of the original Creditor Agent whereby a reject or return code 'AC01' may be used. In this way the original Creditor was not involved in the Payment Return.

![](_page_399_Figure_2.jpeg)

Note: the static Previous Instructing Agent roles in the original payment transition to Intermediary

Various other Payment Return use cases exist where the common principal is the initiator of the Payment Return becomes the mandatory Debtor in the *Return Chain* element (as they owe the money to the party the return is intended for). And the mandatory Creditor in the *Return Chain* element is the party the payment is being returned to.

![](_page_400_Figure_1.jpeg)

Note: a party Rejecting the payment using a pacs.002 would not be considered to be involved in the Payment Return as they would not owe money to the party the return is intended for.

The *Return Reason Information* element captures detailed information on the return reason. Within this element:

![](_page_401_Picture_2.jpeg)

- the *Originator* element helps identify the party who initiated the request to return the payment. This party would have been included in the underlying payment and may also be included the pacs.004 *Return Chain.*
- the *Reason* is mandatory and is represented by an externalised *Code* choice ( )
- the *Additional Information* element may also be included to provide further details on the reason for return.

![](_page_401_Picture_6.jpeg)

The code list representing the *Return Reason* is part of the ISO 20022 external code list

![](_page_401_Picture_8.jpeg)

| Code | Name                        | ISO Definition                                                                                                                                                                                                                | High Level Use Case                                                                                                                                               |
|------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC01 | IncorrectAccountNumber      | Format of the account number specified is not correct or<br>Account number is missing                                                                                                                                         | Sent by any Agent w hen<br>a settlement account number is incorrect                                                                                               |
| AC02 | InvalidDebtorAccountNumber  | Debtor account number invalid or missing                                                                                                                                                                                      | Sent by any Agent w hen Debtor account number is incomplete                                                                                                       |
| AC04 | ClosedAccountNumber         | Account number specified has been closed on the bank of<br>account's books                                                                                                                                                    | Sent by Creditor Agent w hen the Creditor account number is closed                                                                                                |
| AC06 | BlockedAccount              | Account specified is blocked, prohibiting posting of transactions<br>against it.                                                                                                                                              | Sent by Creditor Agent w hen Creditor account is blocked from posting credit<br>entries.<br>Sent by any Agent w hen a settlement account is blocked               |
| AC07 | ClosedCreditorAccountNumber | Creditor account number closed                                                                                                                                                                                                | Sent by Creditor Agent w hen account number is closed.<br>CBPRplus recommend using AC04, but support AC07 to remain interoperable<br>with other clearing systems. |
| AC13 | InvalidDebtorAccountType    | Debtor account type is missing or invalid                                                                                                                                                                                     | Sent by any Agent w hen Debtor account type element is incorrect                                                                                                  |
| AGNT | IncorrectAgent              | Agent in the payment w orkflow is incorrect                                                                                                                                                                                   | Sent by any Agent w hen an agent in the payment transaction has an incorrect<br>identification element                                                            |
| AG01 | TransactionForbidden        | Transaction forbidden on this type of account (formerly<br>NoAgreement)                                                                                                                                                       | Sent by any Agent w hen the type of payment transaction is not allow ed for the<br>specified account                                                              |
| AG07 | UnsuccesfulDirectDebit      | Debtor account cannot be debited for a generic reason.<br>Code value may be used in general purposes and as a<br>replacement for AM04 if debtor bank does not reveal its<br>customer's insufficient funds for privacy reasons | Sent by Debtor Agent of a Direct Debit message, w hen debtor account can not<br>be debited.                                                                       |
| AM02 | NotAllow edAmount           | Specific transaction/message amount is greater than allow ed<br>maximum                                                                                                                                                       | Sent by any Agent w hen payment amount is above an allow ed amount. For<br>example the clearing system w ith a upper amount threshold.                            |

| Code | Name                        | ISO Definition                                                                                                                        | High Level Use Case                                                                                                                                               |
|------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AM03 | NotAllowedCurrency          | Specified message amount is a non processable currency<br>outside of existing agreement                                               | Sent by any Agent w hen<br>the currency of the payment is not allow ed w ithin the<br>existing business agreement                                                 |
| AM04 | InsufficientFunds           | Amount of funds available to cover specified message<br>amount is insufficient.                                                       | Sent by any Agent w hen<br>there is not sufficient funds to settle the payment<br>transaction.                                                                    |
| AM05 | Duplication                 | Payment is a duplicate of another payment                                                                                             | Sent by any Agent w hen<br>the payment is a duplicate. CBPRplus recommend<br>using DUPL, but support AM05 to remain interoperable with other clearing<br>systems. |
| AM06 | TooLowAmount                | Specified transaction amount is less than agreed<br>minimum.                                                                          | Sent by any Agent w hen<br>the payment amount is below a minimum amount.                                                                                          |
| AM07 | BlockedAmount               | Amount specified in message has been blocked by<br>regulatory authorities                                                             | Sent by any<br>Agent w hen the payment amount is blocked by regulators                                                                                            |
| AM09 | WrongAmount                 | Amount received is not the amount agreed or expected                                                                                  | Sent by any Agent w hen<br>the payment amount is incorrect                                                                                                        |
| BE01 | InconsistenWithEndCustomer  | Identification of end customer is not consistent with<br>associated account number (formerly<br>CreditorConsistency).                 | Sent by Creditor Agent w hen there is an inconsistency betw een the Creditor's<br>identification and the account number                                           |
| BE04 | MissingCreditorAddress      | Specification of creditor's address, which is required for<br>payment, is missing/not correct (formerly<br>IncorrectCreditorAddress). | Sent by any Agent<br>w hen the Creditor's address is missing<br>Sent by Creditor Agent<br>w hen the Creditor's address is incorrect                               |
| BE05 | UnrecognisedInitiatingParty | Party who initiated the message is not recognised by the<br>end customer                                                              | Sent by Creditor Agent w hen<br>the initiating party is unknow n<br>to the beneficiary                                                                            |
| BE07 | MissingDebtorAddress        | Specification of debtor's address, which is required for<br>payment, is missing/not correct.                                          | Sent by any<br>Agent w hen the address of the Debtor is missing or incorrect                                                                                      |

| Code | Name                              | ISO Definition                                                                                  | High Level Use Case                                                                                                                                                                                               |
|------|-----------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BE10 | InvalidDebtorCountry              | Debtor country code is missing or invalid                                                       | Sent by any Agent w hen the country code of the Debtor is missing or incorrect                                                                                                                                    |
| BE11 | InvalidCreditorCountry            | Creditor country code is missing or invalid                                                     | Sent by any Agent w hen<br>the country code of the Creditor is missing or<br>incorrect                                                                                                                            |
| BE16 | InvalidDebtorIdentificationCode   | Debtor or Ultimate Debtor identification code missing or<br>invalid                             | Sent by any Agent w hen the identification of the Debtor or Ultimate<br>Debtor is<br>missing or incorrect                                                                                                         |
| BE17 | InvalidCreditorIdentificationCode | Creditor or Ultimate Creditor identification code missing<br>or invalid                         | Sent by the any<br>Agent w hen the identification of the Creditor or Ultimate<br>Creditor is missing or incorrect                                                                                                 |
| CN01 | AuthorisationCancelled            | Authorisation is cancelled.                                                                     | Sent by any Agent w hen a third party debit authorisation has been cancelled<br>or is not in place.                                                                                                               |
| CNOR | Creditor bank is not registered   | Creditor bank is not registered under this BIC in the<br>Clearing Settlement Mechanism<br>(CSM) | Sent by any Agent w hen the Creditor Agent is not reachable in the Market<br>Infrastructure (CSM) and an appropriate correspondent can not be determined.                                                         |
| CURR | IncorrectCurrency                 | Currency of the payment is incorrect                                                            | Sent by<br>the<br>Creditor<br>Agent w hen the Interbank Settlement Amount<br>Currency<br>is not the same as the Creditor account currency and a currency<br>conversion is not accepted on the Creditor's account. |
| CUST | RequestedByCustomer               | Cancellation requested by the Debtor                                                            | Sent by any Agent upon request by Debtor. CBPRplus recommend using<br>FOCR, but support CUST to remain interoperable with other clearing systems.                                                                 |
| DT01 | InvalidDate                       | Invalid date (eg, wrong or missing settlement date)                                             | Sent by any Agent w hen the settlement date is in the past and an agreement<br>is in place to reject rather than apply the next possible value date.                                                              |
| DT04 | FutureDateNotSupported            | Future date not supported                                                                       | Sent by any<br>Agent w hen a future settlement date is not supported or appear to<br>be an error e.g. is the w rong year.                                                                                         |

| Code | Name                          | ISO Definition                                                                                                               | High Level Use Case                                                                                                                                         |
|------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DUPL | DuplicatePayment              | Payment is a duplicate of another payment                                                                                    | Sent by any<br>Agent w hen the payment is a duplicate                                                                                                       |
| ERIN | ERIOptionNotSupported         | The Extended Remittance Information (ERI) option is not<br>supported.                                                        | Sent by any<br>Agent w hen extended Remittance information (Related<br>Remittance Information) is not supported or bilaterally/multilaterally agreed        |
| ED05 | SettlementFailed              | Settlement of the transaction has failed.                                                                                    | Sent by any<br>Agent w hen the settlement of payment has failed or been<br>unsuccessful.                                                                    |
| FF03 | InvalidPaymentTypeInformation | Payment Type Information is missing or invalid.<br>Generic usage if cannot specify Service Level or Local<br>Instrument code | Sent by any<br>Agent w hen the Payment Type Information (Instruction Priority,<br>Clearing Channel) provided for the payment is incorrect or not supported. |
| FF04 | InvalidServiceLevelCode       | Service Level code is missing or invalid                                                                                     | Sent by any<br>Agent w hen the Payment Type Information Service Level<br>provided for the payment is incorrect or not supported                             |
| FF05 | InvalidLocalInstrumentCode    | Local Instrument code is missing or invalid                                                                                  | Sent by any<br>Agent w hen the Payment Type Information Local Instrument<br>provided for the payment is incorrect or not supported                          |
| FF06 | InvalidCategoryPurposeCode    | Category Purpose code is missing or invalid                                                                                  | Sent by any<br>Agent w hen the Payment Type Information Category Purpose<br>provided for the payment is incorrect or not supported                          |
| FF07 | InvalidPurpose                | Purpose is missing or invalid                                                                                                | Sent by any<br>Agent w hen the Purpose provided for the payment is either<br>missing or incorrect                                                           |
| FOCR | FollowingCancellationRequest  | Return following a cancellation request                                                                                      | Sent by any<br>Agent that has accepted a payment cancellation request<br>(camt.056) and subsequently is rejecting the unsettled payment instruction.        |
| FR01 | Fraud                         | Returned as a result of fraud.                                                                                               | Sent by any<br>Agent w hen the payment is identified as fraudulent.                                                                                         |

MD01 NoMandate No Mandate Sent by **any Agent** w hen a Direct Debit message has no mandate in place.

| Code | Name                                    | ISO Definition                                                                                                                                                                                   | High Level Use Case                                                                                                                                                             |
|------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MD02 | MissingMandatoryInformationIn Mandate   | Mandate related information data required by the scheme is missing.                                                                                                                              | Sent by <b>any Agent</b> when information required by the clearing scheme is missing.                                                                                           |
| MD05 | CollectionNotDue                        | Creditor or creditor's agent should not have collected the direct debit                                                                                                                          | Sent by any Agent when a Direct Debit collection was not due                                                                                                                    |
| MD07 | EndCustomerDeceased                     | End customer is deceased.                                                                                                                                                                        | Sent by Creditor Agent when the Creditor or Ultimate Creditor is deceased                                                                                                       |
| MS02 | NotSpecifiedReasonCustomer<br>Generated | Reason has not been specified by end customer                                                                                                                                                    | Sent by <b>Creditor Agent</b> where instructed to reject by the Creditor, but no reason was specified                                                                           |
| MS03 | NotSpecifiedReasonAgent<br>Generated    | Reason has not been specified by agent.                                                                                                                                                          | Sent by any Agent but no reason is specified                                                                                                                                    |
| NARR | Narrative                               | Reason is provided as narrative information in the additional reason information.                                                                                                                | Sent by <b>any Agent</b> the reason is provided as narrative information. <b>Only to be used where no other code is appropriate!</b> (i.e. exceptional circumstances)           |
| NOAS | NoAnswerFromCustomer                    | No response from Beneficiary                                                                                                                                                                     | Sent by <b>any Agent</b> when the Creditor did not respond to query for additional information in order that the payment could be credited e.g. currency control documentation. |
| NOCM | Not compliant (more generic)            | Customer account is not compliant with regulatory requirements, for example FICA (in South Africa) or any other regulatory requirements which render an account inactive for certain processing. | Sent by <b>any Agent</b> when the Creditor account is not compliant with certain regulatory requirements.                                                                       |
| RC01 | BankldentifierIncorrect                 | Bank Identifier code specified in the message has an incorrect format (formerly IncorrectFormatForRoutingCode).                                                                                  | Sent by <b>any Agent</b> when an incorrect BIC has been used in the payment                                                                                                     |
| RC03 | InvalidDebtorBankIdentifier             | Debtor bank identifier is invalid or missing                                                                                                                                                     | Sent by any Agent when the Debtor Agent identification is incorrect or missing                                                                                                  |

| Code | Name                                        | ISO Definition                                                                                                                                | High Level Use Case                                                                                                                       |
|------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| RC04 | InvalidCreditorBankIdentifier               | Creditor bank identifier is invalid or missing                                                                                                | Sent by any Agent w hen the Creditor Agent identification is incorrect or<br>missing                                                      |
| RC08 | InvalidClearingSystemMemberIden<br>tifier   | ClearingSystemMemberidentifier is invalid or missing.<br>Generic usage if cannot specify between debit or credit<br>account                   | Sent by any Agent w hen the clearing system member identification for an<br>Agent is incorrect                                            |
| RC11 | InvalidIntermediaryAgent                    | Intermediary Agent is invalid or missing                                                                                                      | Sent by any Agent w hen the intermediary agent identification is incorrect                                                                |
| RF01 | NotUniqueTransactionReference               | Transaction reference is not unique within the<br>message.                                                                                    | Sent by any Agent w hen the transaction reference (UETR and Instruction<br>Identification) are not unique                                 |
| RR01 | Missing Debtor Account or<br>Identification | Specification of the debtor's account or unique<br>identification needed for reasons of regulatory<br>requirements is insufficient or missing | Sent by any Agent w hen the Debtor identification or debtor account is<br>missing, or the information provided are not sufficient         |
| RR02 | Missing Debtor Name or Address              | Specification of the debtor's name and/or address needed for<br>regulatory requirements is insufficient or missing.                           | Sent by any Agent<br>since the Debtor name or Address is<br>missing, or<br>information provided is not sufficient                         |
| RR03 | Missing Creditor Name or Address            | Specification of the creditor's name and/or address needed<br>for regulatory requirements is insufficient or missing.                         | Sent by any Agent since the Creditor name or Address is<br>missing, or<br>information provided is not sufficient                          |
| RR04 | Regulatory Reason                           | Regulatory Reason                                                                                                                             | Sent by any Agent<br>due to any unspecified regulatory reason                                                                             |
| RR05 | RegulatoryInformationInvalid                | Regulatory or Central Bank Reporting information missing,<br>incomplete or invalid.                                                           | Sent by any Agent<br>w hen the reporting<br>information required by the central<br>bank or reporting authority is missing or not complete |

RR06 TaxInformationInvalid Tax information missing, incomplete or invalid. Sent **by any Agent** w here required tax information is missing, not valid or not

| Code | Name                               | ISO Definition                                                                                                         | High Level Use Case                                                                                                                                                                                                                                                      |
|------|------------------------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RR07 | RemittanceInformationInvalid       | Remittance information structure does not comply w ith rules<br>for payment type.                                      | Sent by any Agent<br>since the<br>remittance information is incorrect                                                                                                                                                                                                    |
| RR08 | RemittanceInformationTruncated     | Remittance information truncated to comply w ith rules for<br>payment type.                                            | Sent by any Agent<br>w here the Structured Remittance Information has not<br>been bilaterally or multilaterally agreed, w hich or has resulted in truncation                                                                                                             |
| RR09 | InvalidStructuredCreditorReference | Structured creditor reference invalid or missing.                                                                      | Sent by any Agent<br>w hen the structure of the creditor reference<br>in the<br>remittance information is invalid or missing                                                                                                                                             |
| RR11 | InvalidDebtorAgentServiceID        | Invalid or missing identification of a bank proprietary service.                                                       | Sent by any Agent w here the proprietary<br>identification for the Debtor is<br>invalid<br>or not understood                                                                                                                                                             |
| RR12 | InvalidPartyID                     | Invalid or missing identification required w ithin a particular<br>country or payment type.                            | Sent by any Agent w here a proprietary party identification<br>is considered<br>invalid<br>or not understood                                                                                                                                                             |
| RUTA | ReturnUponUnableToApply            | Return following investigation request and no remediation<br>possible.                                                 | Sent by any Agent that is unsatisfied w ith the outcome of the unable to<br>apply request and is subsequently rejecting the payment instruction.<br>Alternatively it can be used by the original Creditor Agent w hen the creditor<br>is unable to apply the transaction |
| TM01 | Invalid Cut off time               | Associated message, payment information block, or<br>transaction was received after agreed processing cut-off<br>time. | Sent by any Agent w hen the message w as received after the agreed<br>processing cut off time and an agreement is in place to reject rather than<br>apply the next possible value date.                                                                                  |
| UPAY | UnduePayment                       | Payment is not justified.                                                                                              | Sent by any Agent the payment is undue                                                                                                                                                                                                                                   |

#### **Min 0 – Max 1**

The *Original Transaction Reference* optionally capture elements related to the original transactions. The inclusion of this element is particularly useful where the *Payment Return* includes an Agent not party to the original transaction, or where a significant time lapse has occurred between the original payment and the *Payment Return* i.e., information may have been archived by Agent in the Return chain. CBPR+ has two rules describing when the Original Transaction Reference should be used.

The *Amount* within the nesting of this Original Transaction Reference element only allows for the *Instructed Amount*, as instructed by the Debtor in the original payment initiation request. If the *Instructed Amount* was present in the original payment, populating this data is simple. However, we should also recognise the *Instructed Amount* is not always present (and in fact is not available in the pacs.009), whereby this value should represent the amount in the *Interbank Settlement Amount* of the pacs message being returned. The use of *Instructed Amount* is best described in the pacs.008 [Currency](#page-212-0) and Amount section.

![](_page_409_Picture_3.jpeg)

Note: the role of Parties and Agent in Original element remain unchanged unlike elements such as the Return chain

![](_page_410_Figure_0.jpeg)

Within the Payment Return (pacs.004)

- the *Original Group Information element is used to* refers to original message for which the return relates to. e.g. based upon the above example pacs.008 as the original message would be included in the pacs.004
- the *Transaction Information > Original UETR* element would include UETR of the payment message received. i.e. the *same UETR is used on the Payment Return*.
- the Original Transaction Reference element includes detail from the Original Message Name Identification e.g. the Debtor of the original pacs.008.001.xx
- the Return Chain element includes the parties in the return payment chain, noting the parties reverse (i.e. change role) from the original payment whereby the Debtor of the original payment becomes the Creditor in the Poture Chain.

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Serial Customer Payments**

Use Case p.4.1.1 – Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008)

Use Case p.4.1.2 – Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008)

Use Case p.4.1.2.a – Partial Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008)

Use Case p.4.1.2.b – Refund Payment of a complete Customer Credit Transfer (pacs.008)

Use Case p.4.1.3 - Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008) involving a Market Infrastructure

#### **Serial Financial Institution Payments**

Use Case p.4.2.1 - Payment Return (pacs.004) of an incomplete Financial Institution Credit Transfer (pacs.009)

Use Case p.4.2.2 - Payment Return (pacs.004) of a complete Financial Institution Credit Transfer (pacs.009)

Use Case p.4.2.3 - Payment Return (pacs.004) of an incomplete Financial Institution Credit Transfer (pacs.009) involving a Market Infrastructure

#### **Cover Method Payments**

Use Case p.4.3.1.a - Payment Return (pacs.004) of an incomplete payment using the cover method

Use Case p.4.3.1.b - Payment Return (pacs.004) of an incomplete payment using the cover method

Use Case p.4.3.2 - Payment Return (pacs.004) of a complete payment using the cover method

Use Case p.4.3.2.a - Payment Return (pacs.004) of a complete payment using the cover method

Use Case p.4.3.3 - Payment Return (pacs.004) of an incomplete cover payment

## (pacs.008)

![](_page_412_Figure_1.jpeg)

Debtor initiates a payment instruction to the Debtor Agent

Agent B processes the payment on Agent C

3

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent C processes the payment on Agent D

Having received the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D return the payment to Agent C (as the original payment had already settled) together with the return reason

Agent C return funds to Agent B, together with the reason code for return.

![](_page_413_Figure_0.jpeg)

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent B processes the payment on Agent C

Agent C processes the payment on Agent D

Agent D credits the account of the Creditor, and may optionally

5

Creditor determines that they wish to return the payment e.g. they are unable to apply, and instructs their bank (Agent D) to return the payment together with the reason.

Agent D returns the payment to
Agent C using a Payment Return
message (pacs.004) also\nincluding the return reason code

Agent C return funds to Agent B, together with the reason code for return.

## (pacs.008)

![](_page_414_Figure_1.jpeg)

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent B processes the payment on Agent C

Agent C processes the payment on Agent D

Agent D credits the account of the Creditor, and may optionally

Creditor determines that they wish to partially return the payment e.g. they were over paid or provide a partial refund, and instructs their bank (Agent D) to partially return the payment together with the reason.

Agent D returns the payment to Agent C using a Payment Return

Agent C return funds to Agent B, together with the reason code for return.

![](_page_415_Figure_0.jpeg)

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent B processes the payment on Agent C

Agent C processes the payment on Agent D

Agent D credits the account of the Creditor, and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

Creditor determines that they wish to refund the payment e.g. they could not provide the goods or services paid for. They instruct a new payment from their bank account.

In some circumstances the Creditor may take it upon themselves to provide a refund, using a new payment. Equally the period the original payment is store prior to data archive, particularly by the Creditor

## (pacs.008) involving a Market Infrastructure

![](_page_416_Figure_1.jpeg)

- Debtor initiates a payment instruction to the Debtor Agent
- Debtor Agent (A) initiates a serial payment towards the Creditor Agent (B) using the local currency ISO 20022

  Market Infrastructure

- The payment is **settled** via the local ISO 20022 Market Infrastructure, whereby the payment is forwarded to the Creditor Agent (B)
- Having received the payment Agent B recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent B returns the payment to Agent A using a Payment Return message (pacs.004) also including the return reason code.
- The Market Infrastructure returns the payment performing the necessary settlement posting between Agent B and Agent A.

## (pacs.009)

![](_page_417_Figure_1.jpeg)

![](_page_417_Picture_2.jpeg)

- Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)
- Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent E) using Agents C as an intermediary.

Agent C processes the payment onto Agent D

- Having received the payment instruction Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D rejects the payment to Agent C using a Status Information message (pacs.002) also including the return reject code.
- Agent C return funds to Agent B, together with the reason code for return.
- Agent B advises Agent A of the return of payment together with the reason using the camt.053 and may optionally provide a notification e.g. credit notification.

(pacs.009)

![](_page_418_Figure_1.jpeg)

- Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)
- Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent D) using Agents C as an intermediary.
- Creditor Agent (C) credits the account of Agent D and may optionally provide a notification e.g. credit notification, in addition to an account statement (camt.053)

- Having received the payment Agent D recognises the payment is incorrect e.g. the wrong amount was received. Agent D sends a Payment Return to Agent C including the return reason.
- Agent C return funds to Agent B, together with the reason code for return.
- Agent B advises Agent A of the return of payment together with the reason using the camt.053 and may optionally provide a notification e.g. credit notification.

### Transfer (pacs.009) involving a Market Infrastructure

![](_page_419_Figure_1.jpeg)

![](_page_419_Picture_2.jpeg)

Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent D) using the local currency ISO 20022 Market Infrastructure.

The payment is settled via the local ISO 20022 Market Infrastructure, whereby the payment is forwarded to the Creditor Agent (C)

Having received the payment Agent C recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent C returns the payment towards Agent B using a Payment Return message (pacs.004) also including the return reason code.

Agent C returns the payment to Agent B, together with the reason

The payment return is settled via the local ISO 20022 Market Infrastructure, whereby the payment return is forwarded to the Creditor Agent (B)

Agent B advises Agent A of the return of payment together with the reason using the camt.053 and may optionally provide a notification e.g. credit notification.

<span id="page-420-0"></span>![](_page_420_Figure_0.jpeg)

<span id="page-421-0"></span>![](_page_421_Figure_0.jpeg)

![](_page_422_Figure_0.jpeg)

![](_page_423_Figure_0.jpeg)

![](_page_424_Figure_0.jpeg)

## <span id="page-425-0"></span>**Financial Institution Direct Debit**

![](_page_426_Picture_0.jpeg)

The pacs.010 has two core sets of nested elements:

- *Group Header* which contains a set of characteristics that relates to the transaction
- *Credit Instruction* which contains elements providing information specific to direct debit transaction information and credit instruction.

![](_page_426_Picture_4.jpeg)

Typically a Direct Debit message in a many-to-many payment (FINplus service) would be considered a point-to-point message, successfully resulting in a payment transaction which may be exchange over various messages.

![](_page_427_Figure_0.jpeg)

The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor's account to the Creditor, where both Debtor and Creditor are financial institutions.

![](_page_428_Figure_0.jpeg)

The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor's account to the Creditor, where both Debtor and Creditor are financial institutions.

## **Group Header**

![](_page_430_Picture_0.jpeg)

![](_page_430_Picture_1.jpeg)

Each ISO 20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

The pacs.010 message *Creation Date Time* captures the date and time which the message was created.

![](_page_431_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_431_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The pacs.0010 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_432_Picture_2.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_432_Picture_4.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

## **Credit Instruction**

The Financial Institution Direct Debit *Credit Identification* provides a mandatory element to identify the Direct Debit instruction.

![](_page_434_Picture_2.jpeg)

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT Financial Markets Direct Debit message.

![](_page_435_Picture_0.jpeg)

![](_page_435_Figure_1.jpeg)

*Instructing Agent* and *Instructed Agent*  represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each message leg.

![](_page_435_Picture_3.jpeg)

![](_page_435_Picture_4.jpeg)

#### **Min 0 – Max 1**

The *Creditor Agent* is a static role in the pacs messages. This agent maintain a relationship with their customer, the *Creditor*. Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor.

![](_page_436_Picture_2.jpeg)

**Min 0 – Max 1**

Where the *Creditor Agent* is utilised the *Creditor Agent Account* may optionally be used to capture the account of the Creditor Agent with the Agent immediate before them in the transaction chain (the Agent Serving their account)

This would only apply where the message includes a *Creditor Agent*, however CBPRplus does not recommend to use this element unless mandated within a community or bilaterally agreed.

![](_page_437_Figure_0.jpeg)

The Financial Institution Direct Debit *Creditor Account* provides a optional element to identify the Creditor's Account for which the Direct Debit instruction intends to instruct the movement of money to. **Min 0 – Max 1 Min 1 – Max 1** An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. *Account Currency* The *Currency* for which the account is held. This is identified using the three characters ISO currency code. The Name of the Account, as Assigned by the servicing institution. *Type Name* a unique *Identification* for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account. *Identification*

*Proxy*

Anested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO Proxy Account Type code The Financial Institution Direct Debit message *Direct Debit Transaction Information* nested element captures information related to the Debit part of the transaction, such as the Debtor, the amount and settlement date.

![](_page_439_Picture_2.jpeg)

It is important to recognise that the data elements contained in this part of the Direct Debit message are identical the pacs.009 Financial Institution Credit Transfer message which represents the next stage of the journey should the Direct Debit be accepted.

![](_page_439_Picture_4.jpeg)

*From a business perspective authorisation of a direct debit instruction can be predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit scheme). Either third party debt authority could be granted to the Agent instructing of the Direct Debit, or the Payment Identification could be used to capture a static or incremental value (i.e., a mandate) to determine if the*

![](_page_439_Picture_6.jpeg)

**Min 1 – Max 1**

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

![](_page_440_Figure_2.jpeg)

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

> an end-to-end reference provided by the *Creditor* which must be passed unchanged throughout the payment and reported back to the Creditor.

![](_page_440_Picture_5.jpeg)

note: if the Creditor has not provide an endto-end identifier, the *Creditor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

*UETR* **Min 1 – Max 1** the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their Direct Debit Initiation request, and also included in reporting

## **(continued)**

The pacs message *Payment Identification also* provides a set of optional elements to identify the direct debit transaction. **Min 1 – Max 1**

![](_page_441_Figure_2.jpeg)

**Min 0 – Max 1**

The Financial Institution Direct Debit message *Payment Type Information* provides a set of optional elements where the payment type can be described. **Min 0 – Max 1**

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point *Instruction* 

*Service Level*  **Min 0 – Max 3**

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

*Payment Type Information* information may be used by the Instructed Agent to differentiate the processing priority.

*Priority*  **Min 0 – Max 1**

*Category Purpose*  **Min 0 – Max 1**

*Local Instrument*  **Min 0 – Max 1**

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

![](_page_442_Picture_7.jpeg)

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

A nested element which may either use an external ISO

![](_page_442_Picture_10.jpeg)

![](_page_442_Picture_11.jpeg)

The pacs.010 message (unlike the pacs.008) has one element to capture the amount of the Transfer, *Interbank Settlement Amount*.

**Min 1 – Max 1**

![](_page_443_Picture_2.jpeg)

*Interbank Settlement Amount*

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent.* This therefore is the point-to-point currencyamount exchanged, comparable with the MT Field 32

![](_page_443_Picture_5.jpeg)

![](_page_443_Picture_6.jpeg)

![](_page_443_Picture_7.jpeg)

![](_page_443_Picture_8.jpeg)

Note: the Financial Institution Direct Debit (pacs.010) has no *Instructed Amount* element, *Exchange Rate* or *Charger Bearer*(like the pacs.009) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

The Financial Institution Direct Debit message *Interbank Settlement Date* captures the *Date* the transaction is completed/effected.

![](_page_444_Picture_2.jpeg)

This *Date* element use ISODate YYYY-MM-DD

**10** For example: 2002-10-10 (10 October 2002)

The Financial Institution Direct Debit message *Settlement Time Request* captures the requested settlement time as a choice of nested elements.

![](_page_445_Picture_2.jpeg)

Where *Settlement Time Request* is used the nested:

• *CLS Time* **Min 0 – Max 1**

• *Till Time* **Min 0 – Max 1**

• *From Time* **Min 0 – Max 1**

• *Reject Time* **Min 0 – Max 1**

may be used to capture information related to this time.

![](_page_446_Figure_0.jpeg)

The Financial Institution Direct Debit message *Debtor Account* also provides an number of optional nested element to identify the account for which debit and credit entries have been made. **Min 0 – Max 1**

![](_page_447_Figure_1.jpeg)

*Proxy*

Type represented by either use an external ISO Proxy Account Type code

#### **Min 0 – Max 1**

The *Debtor Agent* is a static role in the pacs messages. This agent maintain a relationship with their customer, the *Debtor*. Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor.

![](_page_448_Picture_2.jpeg)

**Min 0 – Max 1**

Where the *Debtor Agent* is utilised the *Debtor Agent Account* may optionally be used to capture the account of the Debtor Agent with the Agent immediate after them in the transaction chain (the Agent Serving their account) This would only apply where the message includes a *Debtor Agent*, however CBPRplus does not recommend to use this element unless mandated within a community or bilaterally agreed.

The *Instruction for Debtor Agent* elements within the pacs.010 Financial Institution Direct Debit optionally provides information related to the processing of the direct debit instruction.

![](_page_449_Picture_1.jpeg)

**Min 0 – Max 1**

The *Instruction for Debtor Agent* element offers a occurrence of free format information.

The use of this element should be bilaterally agreed with the *Debtor Agent* to maximize the ability to Straight Through Process the instruction.

The *Purpose* elements within the pacs.010 Financial Institution Direct Debit capture the reason for the payment transaction which would result from a successful direct debit. This element may either use an external ISO Purpose code or a proprietary code. **Min 0 – Max 1**

The purpose is used by the capture the nature of the payment e.g. CORT Trade Settlement Payment, CFEE Cancellation Fees etc. and should not be confused with Regulatory Reporting codes.

![](_page_450_Picture_2.jpeg)

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCD is classified within the Collateral categorisation, with the *Name* OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

The optional *Remittance Information* element within the pacs.010 Financial Institution Direct Debit is nested to provide *Unstructured* information related to payment.

![](_page_451_Picture_1.jpeg)

**Min 0 – Max 1**

*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle

**Min 0 – Max 1**

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

![](_page_451_Picture_6.jpeg)

ISO 20022.

Note: like the pacs.009 *Remittance Information* can only be captured in an *Unstructured* element.

*Remittance Information* is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Financial Institution Direct Debit**

Use Case p.10.1.1 - High Level Payment of a Financial Institution Direct Debit (pacs.010) Use Case p.10.1.1.a - High Level Book movement of a Financial Institution Direct Debit (pacs.010) Use Case p.10.1.2 - High Level Rejection of a Financial Institution Direct Debit (pacs.010)

![](_page_453_Figure_0.jpeg)

Agent E initiates a Direct Debit instruction to debit Agent A's account

1

Debtor Agent (B) initiates a serial payment towards the Creditor Agent (E) using Agents B & C as intermediaries 2

Debtor Agent (B) debits the Debtor (Agent A) optionally provide a notification e.g. credit notification in addition to an account statement (camt.053) 2a

Agent C processes the payment on Agent D 3

Agent D credits the account of the Creditor (Agent E), and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

![](_page_454_Figure_0.jpeg)

Agent E initiates a Direct Debit instruction to debit Agent A's account

Debtor Agent (B) debits the Debtor (Agent A) optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

Agent B credits the account of the Creditor (Agent C), and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

![](_page_455_Picture_0.jpeg)

1

![](_page_455_Figure_1.jpeg)

Agent D initiates a Direct Debit instruction to debit Agent A's account

Debtor Agent (B) rejects the instruction, using a pacs.002, as no mandate agreement is in place.

## <span id="page-456-0"></span>Financial Institution Direct Debit – Margin Collection

![](_page_457_Picture_0.jpeg)

The pacs.010 has two core sets of nested elements:

- *Group Header* which contains a set of characteristics that relates to the transaction
- *Credit Instruction* which contains elements providing information specific to direct debit transaction information and credit instruction.

![](_page_457_Picture_4.jpeg)

The Financial Institution Direct Debit Margin Collection is designed to allow a Central Counterpart to collect money by triggering a payment. Whereby the pacs.010 Debit transfer the money to the Creditor using a pacs.009. Unlikely the pacs.010 Financial Institution Direct Debit additional Credit Instruction elements are allowed in this Usage Guideline.

The Financial Institution Direct Debit Margin Collection can be used for

![](_page_458_Figure_0.jpeg)

The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor's account to the Creditor, where both Debtor and Creditor are financial institutions.

## **Group Header**

![](_page_460_Picture_0.jpeg)

![](_page_460_Picture_1.jpeg)

Each ISO 20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

The pacs.010 message *Creation Date Time* captures the date and time which the message was created.

![](_page_461_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_461_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The pacs.0010 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_462_Picture_2.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_462_Picture_4.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

## **Credit Instruction**

The Financial Institution Direct Debit *Credit Identification* provides a mandatory element to identify the Direct Debit instruction.

![](_page_464_Picture_2.jpeg)

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT Financial Markets Direct Debit message.

The pacs message *Payment Type Information* provides a set of optional elements where the payment type can be described. These elements are applied to the pacs.009 which results from this message.

![](_page_465_Figure_2.jpeg)

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-topoint information may be used by the Instructed Agent to differentiate the processing priority.

*Category Purpose*  **Min 0 – Max 1**

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, SECU Transactionis the payment of securities.

## **Agents**

![](_page_466_Picture_1.jpeg)

![](_page_466_Figure_2.jpeg)

*Instructing Agent* and *Instructed Agent*  represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each message leg.

![](_page_466_Picture_4.jpeg)

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

![](_page_467_Picture_1.jpeg)

**Min 0 – Max 1**

The *Intermediary Agent 1* captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 1 Account* captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

![](_page_467_Picture_6.jpeg)

**3**

**Min 0 – Max 1**

The *Intermediary Agent 2* captures the second Intermediary Agent between the Intermediary Agent 1 and the CreditorAgent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 2 Account* captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

![](_page_467_Picture_11.jpeg)

The *Intermediary Agent 3* captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 3 Account* captured the account related to this Intermediary Agent, with the

## **Agent Account**

**Min 0 – Max 1**

The *Creditor Agent* is a static role in the pacs messages. This agent maintain a relationship with their customer, the *Creditor*. Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor.

![](_page_468_Picture_3.jpeg)

**Min 0 – Max 1**

Where the *Creditor Agent* is utilised the *Creditor Agent Account* may optionally be used to capture the account of the Creditor Agent with the Agent immediate before them in the transaction chain (the Agent Serving their account)

This would only apply where the message includes a *Creditor Agent*, however CBPRplus does not recommend to use this element unless mandated within a community or bilaterally agreed.

![](_page_469_Figure_0.jpeg)

The Financial Institution Direct Debit *Creditor Account* provides an optional element to identify the Creditor's Account for which the Direct Debit instruction intends to instruct the movement of money to. **Min 0 – Max 1 Min 1 – Max 1** An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. Anested element which contains a Proxy Identifier together with the Proxy *Account Currency* The *Currency* for which the account is held. This is identified using the three characters ISO currency code. The Name of the Account, as Assigned by the servicing institution. *Type Name* a unique *Identification* for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account. *Identification*

*Proxy*

Type represented by either use an external ISO Proxy Account Type code

## **Information**

**Min 1 – Max 1**

The Financial Institution Direct Debit message *Direct Debit Transaction Information* nested element captures information related to the Debit part of the transaction, such as the Debtor, the amount and settlement date.

![](_page_471_Picture_3.jpeg)

It is important to recognise that the data elements contained in this part of the Direct Debit message are identical the pacs.009 Financial Institution Credit Transfer message which represents the next stage of the journey should the Direct Debit be accepted.

![](_page_471_Picture_5.jpeg)

*From a business perspective authorisation of a direct debit instruction can be predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit scheme). Either third party debt authority could be granted to the Agent instructing of the Direct Debit, or the Payment Identification could be used to capture a static or incremental value (i.e., a mandate) to determine if the*

![](_page_471_Picture_7.jpeg)

**Min 1 – Max 1**

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

![](_page_472_Figure_2.jpeg)

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

> an end-to-end reference provided by the *Creditor* which must be passed unchanged throughout the payment and reported back to the Creditor.

![](_page_472_Picture_5.jpeg)

note: if the Creditor has not provide an endto-end identifier, the *Creditor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

*UETR* **Min 1 – Max 1** the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their Direct Debit Initiation request, and also included in reporting

## **(continued)**

The pacs message *Payment Identification also* provides a set of optional elements to identify the direct debit transaction. **Min 1 – Max 1**

![](_page_473_Figure_2.jpeg)

**Min 0 – Max 1**

The Financial Institution Direct Debit message *Payment Type Information* provides a set of optional elements where the payment type can be described. These elements apply to the debit transaction, whereby the Credit Instruction has it own Payment Type Information. **Min 0 – Max 1** A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. *Service Level*  **Min 0 – Max 3** a choice of imbedded codes representing the urgency considered by the Instructing Agent, *Instruction Priority*  **Min 0 – Max 1**

*Payment Type Information Local Instrument*  **Min 0 – Max 1** *Category Purpose*  this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

**Min 0 – Max 1**

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

![](_page_474_Picture_3.jpeg)

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

A nested element which may either use an external ISO

![](_page_474_Picture_6.jpeg)

The pacs.010 message (unlike the pacs.008) has one element to capture the amount of the Transfer, *Interbank Settlement Amount*.

**Min 1 – Max 1**

![](_page_475_Picture_2.jpeg)

*Interbank Settlement Amount*

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent.* This therefore is the point-to-point currencyamount exchanged, comparable with the MT Field 32

![](_page_475_Picture_5.jpeg)

![](_page_475_Picture_6.jpeg)

![](_page_475_Picture_7.jpeg)

![](_page_475_Picture_8.jpeg)

Note: the Financial Institution Direct Debit (pacs.010) has no *Instructed Amount* element, *Exchange Rate* or *Charger Bearer*(like the pacs.009) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

The Financial Institution Direct Debit message *Interbank Settlement Date* captures the *Date* the transaction is completed/effected.

![](_page_476_Picture_2.jpeg)

This *Date* element use ISODate YYYY-MM-DD

**10** For example: 2002-10-10 (10 October 2002)

The Financial Institution Direct Debit message *Settlement Time Request* captures the requested settlement time as a choice of nested elements.

![](_page_477_Picture_2.jpeg)

Where *Settlement Time Request* is used the nested:

• *CLS Time* **Min 0 – Max 1**

• *Till Time* **Min 0 – Max 1**

• *From Time* **Min 0 – Max 1**

• *Reject Time*

**Min 0 – Max 1**

may be used to capture information related to this time.

![](_page_478_Figure_0.jpeg)

The Financial Institution Direct Debit message *Debtor Account* also provides an number of optional nested element to identify the account for which debit and credit entries have been made. **Min 0 – Max 1**

**Min 1 – Max 1** An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. Anested element which contains a Proxy Identifier together with the Proxy *Account Currency* The *Currency* for which the account is held. This is identified using the three characters ISO currency code. The Name of the Account, as Assigned by the servicing institution. *Type Name* a unique *Identification* for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account. *Identification*

*Proxy*

Type represented by either use an external ISO Proxy Account Type code

## **Agent Account**

**Min 0 – Max 1**

The *Debtor Agent* is a static role in the pacs messages. This agent maintain a relationship with their customer, the *Debtor*. Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor.

![](_page_480_Picture_3.jpeg)

Where the *Debtor Agent* is utilised the *Debtor Agent Account* may optionally be used to capture the account of the Debtor Agent with the Agent immediate after them in the transaction chain (the Agent Serving their account) This would only apply where the message includes a *Debtor Agent*, however CBPRplus does not recommend to use this element unless mandated within a community or bilaterally agreed.

**Min 0 – Max 1**

The *Instruction for Debtor Agent* elements within the pacs.010 Financial Institution Direct Debit optionally provides information related to the processing of the direct debit instruction.

**Min 0 – Max 1**

![](_page_481_Picture_2.jpeg)

The *Instruction for Debtor Agent* element offers a occurrence of free format information.

The use of this element should be bilaterally agreed with the *Debtor Agent* to maximize the ability to Straight Through Process the instruction.

The *Purpose* elements within the pacs.010 Financial Institution Direct Debit capture the reason for the payment transaction which would result from a successful direct debit. This element may either use an external ISO Purpose code or a proprietary code. **Min 0 – Max 1**

The purpose is used by the capture the nature of the payment e.g. CCPC CCP Cleared Initial Margin and should not be confused with Regulatory Reporting codes.

![](_page_482_Picture_2.jpeg)

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCD is classified within the Collateral categorisation, with the *Name* OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

The optional *Remittance Information* element within the pacs.010 Financial Institution Direct Debit is nested to provide *Unstructured* information related to payment.

![](_page_483_Picture_1.jpeg)

**Min 0 – Max 1**

*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle

**Min 0 – Max 1**

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

![](_page_483_Picture_6.jpeg)

ISO 20022.

Note: like the pacs.009 *Remittance Information* can only be captured in an *Unstructured* element.

*Remittance Information* is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Financial Institution Direct Debit**

Use Case p.10.2.1 - High Level Payment Of A Financial Institution Direct Debit (pacs.010) Use Case p.10.2.2 - High Level Rejection Of A Financial Institution Direct Debit (pacs.010)

## **(pacs.010)**

![](_page_485_Figure_1.jpeg)

![](_page_485_Figure_2.jpeg)

Agent E initiates a Direct Debit instruction to debit Agent A's account 1

Debtor Agent (B) initiates a serial payment towards the Creditor Agent (E) using Agents B & C as intermediaries 2

Agent C processes the payment on Agent D 3

Agent D credits the account of the Creditor (Agent E), and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

## **(pacs.010)**

![](_page_486_Picture_1.jpeg)

![](_page_486_Figure_2.jpeg)

Agent D initiates a Direct Debit instruction to debit Agent A's account 1

Debtor Agent (B) rejects the instruction, using a pacs.002, as no mandate agreement is in place.

## <span id="page-487-0"></span>**Financial Institution to Financial Institution Customer Direct Debit**

**pacs.003** Group Header Direct Debit Transaction

The pacs.003 has two core sets of nested elements:

- *Group Header* which contains a set of characteristics that relates to all individual transaction
- *Direct Debit Transaction Information* which contains elements providing information specific to the individual direct debit transaction.

![](_page_488_Picture_4.jpeg)

Information Payment messages in a many-to-many payment are considered as a single transaction.

![](_page_489_Figure_0.jpeg)

The Financial Institution To Financial Institution Customer Direct Debit message is sent by the Creditor Agent to the Debtor Agent, directly or through other agents and/or a payment clearing and settlement system. It is used to collect funds from a Debtor account for a Creditor, whereby one or both of these Parties are non-Financial Institutions.

## **Group Header**

![](_page_491_Picture_0.jpeg)

![](_page_491_Picture_1.jpeg)

Each ISO 20022 payment message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

![](_page_491_Picture_4.jpeg)

Each transaction's *Direct Debit Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference)

The pacs.003 message *Creation Date* captures the date and time which the message was created.

![](_page_492_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_492_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The pacs.003 message *Number of Transactions* captures the number of individual transaction contained within the message.

![](_page_493_Picture_2.jpeg)

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

![](_page_493_Picture_4.jpeg)

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

The pacs.003 *Settlement Method* element within the Group Header *Settlement Information*, includes one of the embedded codes to indicate how the payment message will be settled.

The *Settlement Method element* in the pacs.003 allows a choice of an embedded code.

**INDA** indicate this Customer Direct Debit will be settled by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated *Settlement Account*  element.

![](_page_494_Picture_4.jpeg)

**INGA** indicate this Customer Direct Debit has already been settled by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated *Settlement Account*  element.

![](_page_494_Picture_6.jpeg)

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification

![](_page_494_Picture_8.jpeg)

The pacs.003 message *Settlement Account* is a nested element as part of *Settlement Information,* this element identifies information related to an account used to settle the direct debit instruction.

**Min 0 – Max 1**

The *Settlement Account* identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the *Settlement Method*)

![](_page_495_Picture_3.jpeg)

**Min 0 – Max 1**

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account

*Currency* identifies the currency if the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

## **Direct Debit Transaction Information**

**Min 1 – Max 1**

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

![](_page_497_Figure_2.jpeg)

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

> an end-to-end reference provided by the *Creditor* which must be passed unchanged throughout the payment and reported back to the Creditor.

![](_page_497_Picture_5.jpeg)

note: if the Creditor has not provide an endto-end identifier, the *Creditor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

*UETR* **Min 0 – Max 1** the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their Direct Debit Initiation request, and also included in reporting

#### **Min 1 – Max 1**

The pacs message *Payment Identification also* provides a set of optional elements to identify the direct debit transaction.

![](_page_498_Figure_2.jpeg)

**Min 0 – Max 1**

clearing system transaction as a reference to the settled clearing transaction.

*Payment Type Information* The pacs message *Payment Type Information* provides a set of optional elements where the payment type can be described. **Min 0 – Max 1** A nested element which may either use an external ISO Service Level code\* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. *Service Level*  **Min 0 – Max 3** A nested element which may either use an *Local Instrument*  **Min 0 – Max 1** a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point *Instruction Priority*  **Min 0 – Max 1** information may be used by the Instructed Agent to differentiate the processing priority.

*Category* 

i

a choice of imbedded codes representing the clearing channel to be used to process direct debits.

*Clearing Channel* **Min 0 – Max 1**

external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the

category of payment. For example, RPRE means to re-present

The pacs.003 message has two key element to capture the amount of the Credit Transfer, *Interbank Settlement Amount* and *Interbank Settlement Date*.

**Min 1 – Max 1 Min 1 – Max 1**

![](_page_500_Picture_3.jpeg)

*Interbank Settlement Amount*

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent.* This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32B

![](_page_500_Picture_6.jpeg)

![](_page_500_Picture_7.jpeg)

![](_page_500_Picture_8.jpeg)

![](_page_500_Picture_9.jpeg)

A mandated date on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent.* This therefore is the value date comparable with the MT Field 30

![](_page_500_Picture_11.jpeg)

Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important one. Instructed Amount relates to the amount Instructed to be debited from the Debtor's account and only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not the same currency amount.

The pacs.003 message has two optional elements to capture the information related to the settlement of the instructions.

**Min 0 – Max 1**

![](_page_501_Picture_2.jpeg)

The *Settlement Priority* provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the *Settlement Method* and should not be confused with the *Instruction Priority.* 

![](_page_501_Picture_4.jpeg)

Note: where *Settlement Priority* of the pacs.003 is 'URGT' (Urgent) means the highest priority possible to process the direct debit settlement and the amount of money becomes available to the Creditor Agent.

![](_page_501_Picture_6.jpeg)

**Min 0 – Max 1**

The *Settlement Time Indication* optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, *Debit Date Time* and *Credit Date Time*.

![](_page_502_Picture_0.jpeg)

#### **Min 0 – Max 1**

The *Instructed Amount* captures currency and amount instructed by the Creditor. This conditional element is required when the *Interbank Settlement Amount* is not the same currency and/or amount as originally instructed by the *Creditor.* For example, a charge is taken, or the transactions is converted to another currency. This element is comparable with the legacy Field 33B.

![](_page_502_Picture_3.jpeg)

#### **Min 0 – Max 1**

The *Exchange Rate* captures the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency.

![](_page_502_Picture_6.jpeg)

Note: a number of Cross Element Rules exist which relate to the *Instructed Amount* element. For example, if the *Instructed Amount* is present and the

**Min 1 – Max 1**

The mandated *Charge Bearer* element uses an embedded code that is used to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

![](_page_503_Figure_2.jpeg)

![](_page_503_Picture_3.jpeg)

Note: SLEV is removed from CBPR+ usage guideline specifications.

**Min 0 – Max \* Min 1 – Max 1**

The *Charges Information* element provides information on the charges to be paid by the *Charge Bearer*. This element is comparable with MT Fields: 71F 'Senders Charges' and 71G 'Receiver's Charges'

| Charge      | Amount   |                          |  |
|-------------|----------|--------------------------|--|
| Information | Currency |                          |  |
| (0.*)       | Agent    | BICFI                    |  |
|             |          | Name                     |  |
|             |          | StructuredPostal Address |  |

In addition to the legacy MT message the pacs.003 *Charge Information* mandate the *Agent,* this represent the Agent for who the Charges are either; due (pre-paid charges) or has taken a charge (deduct from the transaction)

CBPR+ best practice recommends the use of the structured Agent BIC.

As the *Charges Information* element is repetitive it can capture charges related to previous legs of the payment transaction.

![](_page_504_Picture_7.jpeg)

Note: As the *Charge Information* element has the capability to capture both charges deducted and charges included i.e. pre-paid charges, the use of the *Interbank Settlement Amount* and *Instructed Amount* elements play an important role.

### **pacs.003 FI to FI Customer Direct Debit – Requested Collection Date**

**Min 1 – Max 1**

The pacs.003 message mandatory *Requested Collection Date* element, captures the date on which the creditor requests that the amount of money is to be collected from the debtor.

![](_page_505_Picture_3.jpeg)

It is defined by *ISO Date* expressed in the *YYYY-MM-DD format*. **10**

Credit party that signs the mandate, may be used if supported by the Direct Debit Schema. (see next page for additional detail on this nested element) The pacs.003 *Direct Debit Transaction* component provides information specific to the direct debit mandate. Unique and unambiguous identification of the pre-notification which is sent separately from the direct debit instruction. **Min 0 – Max 1** *Direct Debit Transaction Pre*  Provides further details of the direct debit mandate signed between the creditor and the debtor. E.g., Mandate Identification, Date of Signature and Electronic Signature. *Pre Notification Identification Creditor Scheme Identification Mandate Related Information* **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1**

**pacs.003 FI to FI Customer Direct Debit – Direct Debit Transaction**

Date on which the creditor notifies the debtor about the amount and date on

*Notification Date*

#### **Min 0 – Max 1**

The *Creditor Scheme Identification* element within the pacs.003 message optionally provides information related to the credit party that signs the mandate who is different from the Creditor.

![](_page_507_Picture_2.jpeg)

The *Creditor Scheme Identification* element offers the following options:

Name

Postal Address: Not used often

Identification

Country of Residence

Contact Details

![](_page_507_Picture_9.jpeg)

CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit Scheme.

The ISO 20022 pacs messages describe the party credited for a transaction as the *Creditor*. The *Creditor* sub elements describe the *Creditor* in greater detail. **Min 1 – Max 1**

Mandatory *Name*, where a BIC identifier is not provided, by which the party is known

*Postal* 

![](_page_508_Picture_2.jpeg)

![](_page_508_Figure_3.jpeg)

Nested element capturing the various types of identifiers for

Nested element capturing either structured or unstructured *Creditor*

the party e.g. BIC, LEI etc.

address details

*Creditor Identification Address*

Optional element to capture the Creditor's ISO country code of residence

*Country of Residence*

#### **Min 0 – Max 1**

**pacs.003 FI to FI Customer Direct Debit – Creditor Account**

The pacs.003 *Creditor Account* is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

> The *Creditor Account* uses a variety of nested elements to capture information related to the account.

![](_page_509_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency if the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

**Min 1 – Max 1 Min 1 – Max 1**

The *Debtor Agent* and *Creditor Agent* are static roles in the pacs.003 FI to FI Customer Direct Debit. These agent maintain a relationship with their customers; the *Debtor* and *Creditor*.

![](_page_510_Picture_3.jpeg)

![](_page_510_Picture_4.jpeg)

![](_page_510_Picture_5.jpeg)

Note: Although the *Debtor Agent, Creditor Agent, Debtor and Creditor* all maintain static roles in the pacs messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

## **Account**

**Min 0 – Max 1**

**Min 0 – Max 1**

The pacs.003 *Debtor Agent Account* and *Creditor Agent Account* are used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the direct debit transaction.

**pacs.003 FI to FI Customer Direct Debit – Debtor Agent Account and Creditor Agent** 

![](_page_511_Picture_3.jpeg)

The *Debtor Agent Account* and *Creditor Agent Account* use a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Account Servicing Institution

*Type* uses the external CashAccount Type code list to identify the type of account *Currency* identifies the currency of the account **Min 0 – Max 1 Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Account Servicing Institution **Min 0 – Max 1**

> *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

![](_page_511_Picture_9.jpeg)

Debtor Agent and Creditor Agent are a Financial Institution, therefore

The pacs.003 message introduces ultimate parties to the FI to FI Customer Direct Debit message. The *Ultimate Creditor* element should not be confused with an *Initiating Party* who may send a direct debit initiation request on behalf of the Creditor. (see dedication section on *Initiating Party*)

![](_page_512_Picture_1.jpeg)

➢ CBPR+ premise is that an *Ultimate Debtor* has no financial regulated direct account relationship with the corresponding *Debtor*.

**Min 0 – Max 1**

➢ CBPR+ premise is that an *Ultimate Creditor* has no financial regulated direct account relationship with the corresponding *Creditor*. **Min 0 – Max 1**

An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor depending on the payment scenario)

![](_page_512_Picture_5.jpeg)

*Direct Debit Transaction Information*

![](_page_513_Picture_0.jpeg)

**Min 0 – Max 1 Min 1 – Max 1**

The *Initiating Party* of a direct debit is often the *Creditor* themselves and therefore this optional element is not necessary. More often the *Initiating Party* is a third party providing direct debit collection services on behalf of the *Creditor* (often referred to as a Third Party Provider) whereby the *Creditor* maintains an account with the Creditor Agent but the Third Party Provider has authority to initiate collection on behalf of the Creditor. This is distinctly different from an Ultimate Party (such as *Ultimate Creditor*) who instructs the *Creditor* to initiate a collection on their behalf.

![](_page_513_Picture_4.jpeg)

In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the *Initiating Party* is often the *Creditor*, however the same context of a Third Party Provider can exist where the third party is responsible for collecting funds on behalf of the *Creditor*.

![](_page_514_Figure_0.jpeg)

![](_page_514_Picture_1.jpeg)

*Instructing Agent* and *Instructed Agent*  represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment leg.

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

![](_page_515_Picture_1.jpeg)

**Min 0 – Max 1**

The *Intermediary Agent 1* captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 1 Account* captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

![](_page_515_Picture_6.jpeg)

**3**

**Min 0 – Max 1**

The *Intermediary Agent 2* captures the second Intermediary Agent between the Intermediary Agent 1 and the CreditorAgent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 2 Account* captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

![](_page_515_Picture_11.jpeg)

The *Intermediary Agent 3* captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**

The *Intermediary Agent 3 Account* captured the account related to this Intermediary Agent, with the

The ISO 20022 pacs messages describe the party debited for a transaction as the *Debtor*. The *Debtor* sub elements describe the *Debtor* in greater detail. **Min 1 – Max 1**

*Debtor Name* Mandatory *Name* (where a BIC identifier is not provided) by which the party is known *Identification Postal Address* Nested element capturing either structured or unstructured *Debtor*

Optional element to

capture the Debtor's ISO country code of residence *Country of Residence*

Nested element capturing the

various types of identifiers for the party e.g. BIC, LEI etc.

address details

**pacs.003 FI to FI Customer Direct Debit – Debtor Account**

The pacs.003 mandatory *Debtor Account* is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

> The *Debtor Account* uses a variety of nested elements to capture information related to the account.

![](_page_517_Picture_3.jpeg)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency of the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. **Min 0 – Max 1**

A children sports clubs (Creditor), collects its monthly membership fee via direct debit, against the parents (Debtor) of one of it members (Ultimate Debtor).

![](_page_518_Figure_1.jpeg)

3

Sports club, the Creditor who has a mandate\* with the Debtor, initiates a direct debit instruction by sending a pain.008 message to their bank, Creditor Agent (A).

Agent A, the Creditor Agent, initiates a direct debit instruction by sending a pacs.003 message to the Debtor Agent (B).

2

Debtor Agent (B) debits the account of the Debtor, credits the account of the Creditor Agent and confirms the direct debit status using a pain.002.

Debtor, receives a statement from their bank confirming the monthly Debt Debit, for their child (Ultimate Debtors) sports club membership fee, has debited either account,

**Min 0 – Max 1**

The *Purpose* element within the pacs.003 FI to FI Customer Direct Debit captures the reason for the direct debit transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment e.g. IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Creditor.

![](_page_519_Picture_3.jpeg)

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example, LOAR is classified within the Finance categorisation, with the *Name* Loan Repayment described as a repayment of loan to lender.

![](_page_519_Picture_6.jpeg)

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

The *Regulatory Reporting* element within the pacs.003 FI to FI Customer Direct Debit is nested to capture regulatory and statutory information needed to report to the appropriate authority/s. **Min 0 – Max 10**

![](_page_520_Picture_1.jpeg)

**Min 0 – Max 1**

The *Debit Credit Reporting Indicator* utilises an embedded choice of code to indicate whether the regulatory reporting information applies to the:

- DEBT (debit)
- CRED (credit) or
- BOTH

**Min 0 – Max 1**

The *Authority* element captures the *Name* and *Country* code of the Authority/Entity requiring the regulatory reporting information.

**Min 0 – Max \*** The *Details* element provides the detail on the regulatory reporting information.

**Min 0 – Max 1**

The *Related Remittance Information* element within the pacs.003 FI to FI Customer Direct Debit is nested to provide information related to the handling of remittance information. This information is typically provided by the Creditor in the direct debit initiation request.

**Min 0 – Max 1**

The *Remittance Identification* captures a unique reference assigned by the initiating party of the collection to identify the remittance information sent separately from the direct debit instruction.

**Min 0 – Max 2**

The *Remittance Location Details* uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- *Method* requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email)
- *Electronic Address* provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.
- *Postal Address* provides the postal address to which an agent is to send the remittance information

Remittance advices are typically considered as a traditional value added service provided by the Creditor Agent to the Creditor, in order to facilitate reconciliation for the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting messages.

*Remittance Information* is a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022. *Related Remittance Information* and *Remittance Information* are mutually exclusive (can't both be present)

Business examples are emerging where information is externalised using a URL repository solution.

![](_page_521_Picture_12.jpeg)

![](_page_521_Picture_13.jpeg)

The optional *Remittance Information* element within the pacs.003 FI to FI Customer Direct Debit is nested to provide either *Structured* or *Unstructured* information related to direct debit collections, such as invoices.

**Min 0 – Max 1**

*Remittance Information* enable the matching/reconciliation of an entry that the direct debit is intended to settle

![](_page_522_Picture_3.jpeg)

**Min 0 – Max 1**

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

**Min 0 – Max \***

The **Structured** element is nested capturing rich structured *Remittance Information,*  and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification)

The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-to-end transportation of this data.

![](_page_522_Picture_9.jpeg)

mutually exclusive (can't both be present)

The bilaterally/multilaterally agreed *Remittance Information* which is *Structured* must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

![](_page_523_Figure_1.jpeg)

example of *Structured* invoice information

![](_page_523_Figure_3.jpeg)

The *Creditor Remittance Information* is provided to the *Creditor* in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.

> In this example Referred Document Information and it nested elements has multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Serial Financial Institution to Financial Institution Customer Direct Debit**

Use Case p.3.1.1 – High Level FI to FI Customer Direct Debit (pacs.003) successful settlement Use Case p.3.1.2 – High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement

![](_page_525_Figure_0.jpeg)

Creditor initiates a direct debit instruction to the Creditor Agent

Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method "INDA" 2

The Debtor Agent debits the account of the Debtor, and may optionally provide a notification e.g. debit notification in addition to an account statement (camt.053). The Debtor Agent also provides a status update ACSC (accepted settlement completed) to the Creditor Agent.

3

Creditor Agent (A) relays the status ACSC (accepted settlement completed) to the Initiating Party, based upon a bilateral agreement

![](_page_526_Picture_0.jpeg)

![](_page_526_Figure_1.jpeg)

Creditor initiates a direct debit instruction to the Creditor Agent

Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method "INDA" 2

The Debtor Agent fails to debit the account of the Debtor (e.g., account is closed). The Debtor Agent provides a status update RJCT (Rejected) with the rejection reason information.

3

Creditor Agent (A) relays the status RJCT (Rejected) to the Initiating Party with the rejection reason information

# <span id="page-527-0"></span>messages

![](_page_528_Picture_0.jpeg)

#### <span id="page-528-0"></span>**Cash Management Reporting**

**camt.052** [-Bank to Customer Account Report](#page-529-0) 

**camt.053** [-Bank to Customer Statement](#page-576-0)

**camt.054** [-Bank to Customer Debit Credit Notification](#page-628-0)

**camt.057** – [Notification To Receive](#page-696-0)

**camt.058** – [Notification To Receive Cancellation Advice](#page-696-0) 

**camt.060** [–Account Report Request](#page-718-0)

## <span id="page-529-0"></span>**Bank to Customer Account Report**

![](_page_530_Picture_0.jpeg)

The *Bank To Customer Account Report*  message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message. It can be used to inform the account owner, or authorised party, of:

- entries reported to the account (Intraday Statement)
- account balance information (Account Balance Report)

Institution and the Account owner, and is establish by an RMA business profile.

• or both.

for a given point in time.

![](_page_530_Picture_6.jpeg)

![](_page_531_Figure_0.jpeg)

Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Account Report message to Account Servicer and Account Owner. Whereby the report is send by the Account Servicer to the Account Owner and or authorised party. This message is used to inform the account owner, or authorised party, of the entries

## **Group Header**

![](_page_533_Picture_0.jpeg)

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Customer Statement message. However, the *Transaction Reference Number* (Field 20) could be considered a similar comparison.

![](_page_534_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_534_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

<span id="page-535-0"></span>The Bank to Customer Account Report *Message Recipient* nested element provides details of the party authorised by the *Account Owner* to receive the Account Report.

This element **should only** be used to identify the *Message Recipient* when different from the account owner, which is implied by the usage of COPY in the *Copy Duplicate Indicator* within the nested Statement element.

![](_page_535_Picture_3.jpeg)

Where *Message Recipient* is used the nested:

- Name Min 0 Max 1
- Postal Address Min 0 Max 1
- Identification Min 0 Max 1
- Contact Details Min 0 Max 1

may be used to capture information related to this party.

Min 0 - Max 1

The Bank to Customer Account Report *Original Business Query* element identifies a query to generate a report, for example a camt.060 Account Reporting Request.

![](_page_536_Picture_2.jpeg)

Where *Original Business Query* is used the original *Message identification* (i.e., the message identification of the camt.060 message) is required.

Original *Message Name identification* and Original *Creation Date Time* may also be provided.

Min 0 – Max 1

Min 1 - Max 1

The Bank to Customer Account Report *Additional Information* element represents further details related to the account statement.

![](_page_537_Picture_2.jpeg)

In accordance to the usage in the camt.053 this element could be used to describe additional information to distinguish the different camt.052 usage i.e., where the report is only reporting an intraday balance, intraday entries or both. Unlike the camt.053 there is no recommended identification string to represent usage.

![](_page_537_Picture_4.jpeg)

Additional Information is a textual element restricted in CBPR+ to 500 characters.

![](_page_538_Picture_0.jpeg)

The Bank to Customer Account Report *Report* element provides information related to an account, most typically associated with intraday account entries and or accounting balances (where entries have been processed on the account). The report element can be used to advise entries reported to the account (Intraday Statement), account balance information (Account Balance Report) or both.

![](_page_539_Picture_2.jpeg)

The *Report* element has been restricted to one account report. To report additional accounts to the Account Owner this would need to occur via a separate message in a similar way to the legacy MT 942.

![](_page_539_Picture_4.jpeg)

It **should also be noted** the Account Report message is modelled identically to the Account Statement (camt.053) therefore where used as an intraday transaction report the content can be capture identically to the statement at the close of the business day,

![](_page_539_Picture_6.jpeg)

<span id="page-540-0"></span>Similar to the legacy MT Intraday Reporting message (i.e., 942) the camt.052 Bank to Customer Account Report is constrained in CBPR+ by the FINplus service's message size. Consideration therefore need to be given (when reporting transactional information) to identifying; the **report order**, the **report correlation**and the **last report page**.

![](_page_540_Picture_1.jpeg)

![](_page_540_Picture_2.jpeg)

![](_page_540_Picture_3.jpeg)

**Report Order:** identifying the order in which statements should be processed or reconstituted. Options:

**Report Correlation:** identifying statement which relate to each other for a given statement period. Options:

*Report Pagination Legal Sequence Number*

**Last Report:** identifying when no further statements for a given period are expected i.e. period statement in finalised. Options:

*Entry ……*

*Report Pagination, Last Page Indicator*

The Bank to Customer Account Report message *Identification* provides a mandatory element to identify the statement

![](_page_541_Picture_2.jpeg)

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

The Bank to Customer Account Report message *Report Pagination* element provides the page number of the report.

![](_page_542_Picture_2.jpeg)

**Min 1 – Max 1 Min 1 – Max 1**

*Report Pagination* includes the*Page Number* and *Last Page indicator* elements.

**For example,** a *Page Number* of 2 represents the current account report, being the second page of the and implying a previous account report page had been sent. The *Last Page indicator*furtherimplies whether more pages are expected

![](_page_542_Picture_7.jpeg)

*Report* Report *Pagination* Noted: as **Report Pagination** is required, even if there is only one page to the report being sent. Both the **Page Number** and **Last Page indicator** will need to be provided i.e., 1 and Yes.

The Bank to Customer Account Report message *Electronic Sequence Number* allows the *Account Servicer* to assign a number to each Report which should increment by 1 for each electronic statement report sent.

![](_page_543_Picture_2.jpeg)

This element allows easy recognition of the Report order, equivalent to the legacy Field 28C Statement Number. The sequence should increment for each camt.052 message sent to the Account Owner or Authorised Party this number must be the same value where the statement continues over multiple pages (*Report Pagination*) of the report for a give account.

Should this sequence number be reset by the *Account Servicer*, this should not occur more frequently than once a day. Likewise, this 18 digit counter could be incremented to its maximum value before it's reset.

![](_page_543_Picture_5.jpeg)

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the *Account Servicer* and the *Account Owner* 

Fither Electronic Sequence Number or Legal Sequence Number

The Bank to Customer Account Report message *Reporting Sequence* specifies the choice of identification sequences. This can be used as an alterative to the *Report Pagination* or *Electronic Sequence Number* as a way to identify the report order, which is not confined to numeric values.

![](_page_544_Picture_3.jpeg)

Where used the *Reporting Sequence* mandate a choice of nested element:

- *From Sequence* identifies the start of a sequence range. **Min 1 – Max 1**
- *To Sequence* identifies the end of a sequence range. **Min 1 – Max 1**
- *From To Sequence* identifies the start and end of a sequence range. **Min 1 – Max \***
- *Equal Sequence* identifies a sequence. **Min 1 – Max \***
- *Not Equal Sequence* identifies a sequence to be excluded. **Min 1 – Max \***

![](_page_544_Picture_10.jpeg)

The Reporting Sequence may be provided in the camt.060 Account Reporting request to specify, for example, a range of Statements to be sent. Alternatively, Account Reports can often be produced on a bilaterally agreed period basis.

The Bank to Customer Account Report message *Legal Sequence Number* allows the *Account Servicer* to assign a number to each report which should increment by 1 for each Report sent.

![](_page_545_Picture_2.jpeg)

Where the Intraday Account Report uses multiple camt.052 messages for a given report period the *Legal Sequence Number* must be the same number in each report message during that reporting period. This element can be considered an equivalent to the legacy Field 28C Statement Number

![](_page_545_Picture_4.jpeg)

Either *Electronic Sequence Number* or *Legal Sequence Number* should be provided to enable the identification of a report number.

![](_page_546_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_546_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The Bank to Customer Account Report message *From to Date* allows the *Account Servicer* to specify the start date time and end date time applicable to the intraday account entries and or accounting balances being reported.

For intraday account reports this is an important attribute that allows the account owner to understand the period for which the report applies. The element is not mandatory as the report may only contain the balance, whereby the report *Creation DateTime* may be used to identify the date and time associated to the balance. **Min 1 – Max 1 Min 1 – Max 1**

Where *From to Date* is used the *From Date Time* and *To Date Time* become mandatory elements.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

![](_page_547_Picture_5.jpeg)

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_547_Picture_8.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional. *Report*

The Bank to Customer Account Report message *Copy Duplicate Indicator* is used as a choice to identify additional reports from the original sent to the Account Owner.

![](_page_548_Picture_2.jpeg)

*COPY* is used when a copy of the report is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service.

![](_page_548_Picture_4.jpeg)

*DUPL* is used when a duplicate of the report is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request.

![](_page_548_Picture_6.jpeg)

*CODU* is used when a duplicate of a report copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in place with the Account Servicer.

**Min 0 – Max 1**

The Bank to Customer Account Report message *Reporting Source* allows the *Account Servicer* to define the source of the intraday account entry and or account balance report, typically associated with an application.

![](_page_549_Picture_2.jpeg)

*Reporting Source* utilises the external Reporting Source code list. For example **ACCT** represents a statement or report based on accounting data, whereas **DEPT** represents a cash or deposit system.

Where the source of the statement is functionally required by the consumer of the statement i.e., the *Account Owner* or *authorised Third Party*, the codes used should be bilaterally agreed.

The Bank to Customer Account Report message *Account* provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath *Account*.

![](_page_550_Figure_2.jpeg)

The Bank to Customer Account Report message mandatory *Account* also provides a number of optional nested element to identify the account for which debit and credit entries have been made.

![](_page_551_Figure_3.jpeg)

The Bank to Customer Account Report message *Related Account* allows the identification of a related parent account for the account report. For example sweeping, pooling or virtual account for which the report is produced can identify the parent account they hierarchically relate to.

![](_page_552_Picture_2.jpeg)

When *Related Account* is utilized, like *Account*, the *Identification* and *Currency* element become mandatory. **Min 1 – Max 1 Min 1 – Max 1**

Additionally, the nested *Type* element, *Name* and nested *Proxy* element are optionally available. **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1**

![](_page_552_Picture_5.jpeg)

*Related Account* uses a variety of common elements described in more detail within the *Account* section.

![](_page_552_Picture_7.jpeg)

![](_page_552_Picture_8.jpeg)

The Bank to Customer Account Report message *Interest* provides interest information that applies to the account. **Min 0 – Max \*** *Interest Reason* An element which may either use an embedded ISO Interest Type code; **INDY** (Intraday) **OVRN** (Over Night) or a proprietary code. It is used to identifier a particular interest type. The optional Reason for which interest is applied. The type of interest Rate defined as a *Percentage* and in an *Other* form. Validity Range optionally defines an *Amount*, *Credit Debit Indicator*and *Currency*. The date range for which interest has been calculated. *From Date Time* and *To Date Time* must be representing when using this element. Provides details on any tax applied to the Interest. Where optional **+ -** *Type Rate From To Date Tax*

*Identification* describes the tax levied, additionally with a *Rate* and or

The Bank to Customer Account Report message optional *Balance* is a nested element to define the account balance at a specific point in time. The following four elements nested beneath *Balance* are mandatory **Min 0 – Max \***

*Balance* Balance amount. Embedded code CRDT (Credit balance) DBIT (Debit balance) A nested element which may either use an external ISO Balance Type code or a proprietary code. For example, OPAV – OpeningAvailable. Additionally, a Sub Type represented by either use an external ISO BalanceSub Type code or a proprietary code, may be used. A nested element representing the *Date* and the *DateTime* (with UTC offset) *of the balance* **Min 1 – Max 1** *Type Amount Credit Debit Indicator Date*

*Balance Type* code are used within the nested *Balance* element to represent the type/s of balance being reported. In comparison the legacy MT 941 utilizes different Fields and Tag options to represent a number of these Balance Types. The below extract from the externalised ISO *Balance Type* code list compares the code with the population of the equivalent information in the Legacy MT 941 Balance Report.

| Code | Name                   | Definition                                                                                                                                                                                                                                                                                                                                                         | MT 941<br>Comparison |
|------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| CLAV | ClosingAvailable       | Closing balance of amount of money that is at the disposal of the account owner on the date specified.                                                                                                                                                                                                                                                             | Field 64             |
| CLBD | ClosingBooked          | Balance of the account at the end of the pre-agreed account reporting period. It is the sum of the opening<br>booked balance at the beginning of the period and all entries booked to the account during the pre<br>-agreed<br>account reporting period.                                                                                                           | Field 62F            |
| FWAV | Forw ardAvailable      | Forward available balance of money that is at the disposal of the account owner on the date specified.                                                                                                                                                                                                                                                             | Field 65             |
| INFO | Information            | Balance for informational purposes.                                                                                                                                                                                                                                                                                                                                | No equivalent        |
| ITAV | InterimAvailable       | Available balance calculated in the course of the account servicer's business day, at the time specified, and<br>subject to further changes during the business day. The interim balance is calculated on the basis of booked<br>credit and debit items during the calculation time/period specified.                                                              | Field 64             |
| ITBD | InterimBooked          | Balance calculated in the course of the account servicer's business day, at the time specified, and subject to<br>further changes during the business day. The interim balance is calculated on the basis of booked credit and<br>debit items during the calculation time/period specified.                                                                        | Field 62F            |
| OPAV | OpeningAvailable       | Opening balance of amount of money that is at the disposal of the account owner on the date specified.                                                                                                                                                                                                                                                             | No equivalent        |
| OPBD | OpeningBooked          | Book balance of the account at the beginning of the account reporting period. It always equals the closing<br>book balance from the previous report.                                                                                                                                                                                                               | Field 60F            |
| PRCD | PreviouslyClosedBooked | Balance of the account at the previously closed account reporting period. The opening booked balance for the<br>new period has to be equal to this balance.<br>Usage: the previously booked closing balance should equal (inclusive date) the booked closing balance of the<br>date it references and equal the actual booked opening balance of the current date. | No equivalent        |
| XPCD | Expected               | Balance, composed of booked entries and pending items known at the time of calculation, which projects the<br>end of day balance if everything is booked on the account and no other entry is posted.                                                                                                                                                              | No equivalent        |

[Take me to an implementation example involving](#page-540-0) *Balance Type* codes

The Bank to Customer Account Report message mandatory *Balance* also provides the optional set of nested element to define a *Credit Line*

**Min 0 – Max \***

The true/false Boolean of *Included* to clearly determine whether the Credit Line Amount is included in the balance is mandatory in the set of Credit Line element.

![](_page_556_Picture_4.jpeg)

Additionally, the following optional nested element may be used to identify:

- The *Type* of Credit Line, which may either use an external ISO Credit Line Type code or a proprietary code.
- A set of elements to provide *Credit Line* details
- The *Amount*(Currency and Amount) of the Credit Line
- The *Date* (nested as Date, DateTime) of the Credit Line, provided to distinguish where multiple Credit Line exist.

The final optional nested element within *Balance* is the *Availability* of the booked amount i.e., when it is available to be accessed.

![](_page_556_Picture_11.jpeg)

The *Credit Line* element is unlimited (Max \*) whereby more that one *Credit Line*  may be reported, the *Date* becomes an important element to distinguish between different Credit Lines.

![](_page_556_Picture_13.jpeg)

The Bank to Customer Account Report message optional *Transaction Summary* provides a set of nested element to summarize entry information. Where the intraday account entries and or accounting balances are reported using multiple camt.052 messages for a given reporting period the *Transaction Summary* should only be included on the first Report message (*Balance Type* OPBD with no Balance *Sub Type*) summarizing the whole Statement Report (entire statement period) This aligns with the Common Global Implementation (CGI) where a *Transaction Summary*, if provided, would appear before the first *Entry* elements.

![](_page_557_Picture_2.jpeg)

Each of the following element allow an optional total of entries either as a *Number of Entries* and or as a *Sum*.

- ➢ *Total Entries*
- ➢ *Total Credit Entries*
- ➢ *Total Debit Entries*
- ➢ *Total EntriesPer Bank Transaction Code*

**Min 0 – Max \***

In addition to the *Number of Entries* and *Sum*, the *Total Entries Per Bank Transaction Code* requires the *Bank Transaction Code* element and optionally allows a variety of other optional elements. **Min 1 – Max 1**

![](_page_557_Picture_10.jpeg)

*Report Transaction Summary*

*Total Entries*

*Total Credit Entries*

*Total Debit Entries*

**Min 0 – Max \***

The Bank to Customer Account Report message optional *Entry* provides a significant variety of nested elements to represent the details associated with each *Entry*. For active accounts which have intraday entries posted across them, this set of nested elements is arguably the most relevant for the account owner and in many way is comparable with the MT 942 Field 61 Statement Line.

![](_page_558_Picture_2.jpeg)

Unlike the legacy MT Interim Transaction Report message, the camt.052 has a number of dedicated elements to capture a variety of entry level data. It also has a number of enhancements on the legacy MT Interim Transaction Report message where parties in the payment and customer remittance information, as examples, can provided to the *Account Owner.* 

![](_page_558_Figure_4.jpeg)

![](_page_559_Figure_0.jpeg)

![](_page_560_Figure_0.jpeg)

![](_page_561_Picture_0.jpeg)

The *Bank Transaction Code*  is designed to deliver a harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the **account servicer** to correctly report a transaction, which in its turn will help **account owners** to perform their cash management and reconciliation operations. Domain Family

The structure of the Bank Transaction Code has three levels:

> *Domain*: Highest definition level to identify the subledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.) **Family**: Medium definition level e.g. type of payment; credit transfer, direct debit etc. *Sub-family*: Lowest definition level e.g. type of cheques; draft etc.

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code combinations*  external code sets.

|          | Payments Domain Families  The description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the description of the de |                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                    |                                                                                                                                                        |  |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 1.       | Received Credit<br>Transfers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | the account owner. The receivable credit transfers are related to transactions received account owner.                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                    | The description of <b>Ba</b> available to download                                                                                                     |  |
| 2.       | Issued Credit Transfers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Payable Credit Transfers are instructions to transfer an amount of money by the account of a creditor. The payable credit transfers are related to instructions sent by the account   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                    | code list page. These<br>Payments Domain Fa                                                                                                            |  |
| 3.       | Received Cash<br>Concentration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                       | ction is related to incoming cash movements that are related to cash management estimitiated by the owner of the sending account to optimise the return on the av                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                    |                                                                                                                                                        |  |
| 4.<br>5. | Issued Cash Concentration Received Direct Debits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | activities initiated b                                                                                                                                                                | ction is related to outgoing cash movements that are related to cash management estimated by the owner of the account to optimise the return on the available for ceived Direct Debit transactions are related to instructions received by the account to optimise the return on the available for the ceived Direct Debit transactions are related to instructions received by the account to optimise the return on the available for the ceived Direct Debit transactions are related to instructions received by the account to optimise the return on the available for the ceived Direct Debit transactions are related to instructions received by the account to optimise the return on the available for the ceived Direct Debit transactions are related to instructions received by the account to optimise the return on the available for the ceived Direct Debit transactions are related to instructions received by the account to optimise the return on the available for the ceived Direct Debit transactions are related to instructions received by the account to optimise the return on the available for the ceived Direct Debit transactions are related to instructions received by the account to optimise the return on the available for the ceived Direct Debit transactions are related to instructions received by the account to the ceived Direct Debit transactions are related to instructions received by the account to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direct Debit transactions are related to the ceived Direc |                                                                                                    |                                                                                                                                                        |  |
| 6.       | Issued Direct Debits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The Received Direct Debit transactions are related to instructions received by the account.  The Issued Direct Debit transactions are related to instructions sent by the account own |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                    | <u> </u>                                                                                                                                               |  |
| 7.       | Received Cheques                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | collect an amount o<br>Transaction is relate<br>from the cheque dra                                                                                                                   | on is relate Received and Issued Credit Transfers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                    |                                                                                                                                                        |  |
| 8.       | Issued Cheques                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                       | Internal Book Transfer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Transaction is a transfer between -two differ                                                      | rent accounts within the same bank                                                                                                                     |  |
|          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Transaction is related                                                                                                                                                                | Standing Order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Transaction is a standing order. A standing of<br>authority on the debtor's account to debit, i.e. | order is an instruction given by a party having<br>e. either debit account owner or originating pa<br>at specified intervals during an implicit or exp |  |
|          | Cross-Border Standing Order SEPA Credit Transfer Domestic Credit Transaction is a cross-border standing order Transaction is a SEPA credit transfer Transaction is a in-country domestic currency credit transfer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | cv credit transfer                                                                                 |                                                                                                                                                        |  |
|          | Transfer  Cross-Border Credit Transaction is a cross-border credit transfer  Transfer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                    |                                                                                                                                                        |  |
|          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Credit Transfer with agreed Commercial  Transaction is a credit transfer including commercial information, i.e. additionagreed between the sender and the receiver.                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                    | nmercial information, i.e. additional informat                                                                                                         |  |
|          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                       | Information Financial Institution Credit Transfer Priority Credit Transfer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | institutions.<br>Transaction is a credit transfer defined with 1                                   | ansfer, i.e. the debtor and creditor are financi<br>higher priority, eg a PRIEURO credit transfe:                                                      |  |
|          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                       | Darmall/Calaury Darms and                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Transaction is related to the marm out of a ma                                                     |                                                                                                                                                        |  |

The description of *Bank Transaction Codes* are available to download from the ISO20022.org external code list page. These include the descriptions for Payments Domain Families and sub-families for both Received and Issued Credit Transfers. **Min 1 – Max 1**

[https://www.iso20022.org/external\\_code\\_list.page](https://www.iso20022.org/external_code_list.page)

![](_page_563_Figure_0.jpeg)

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code combinations* external code sets.

As an example a debit statement transaction which relates to a cross-border payment initiated from an account would be represented by:

| Domain         | Family                        | Sub-Family                         |
|----------------|-------------------------------|------------------------------------|
| PMNT (Payment) | ICDT (Issued Credit Transfer) | XBCT (Cross-Border Credit Transfer |

![](_page_564_Figure_0.jpeg)

![](_page_565_Figure_0.jpeg)

The Bank to Customer Account Report message optional *Entry Details* provides a variety of nested elements to represent the details associated with each *Entry*. **Min 0 – Max \***

![](_page_566_Picture_1.jpeg)

*Batch* provides details on batched transactions such as the total *Number of Transactions*  the batched entry (sometimes referred to as a consolidated entry) represents. *Transaction Details* is a significant nested element which represents information on the underlying transaction.

When the Bank to Customer Account Report message optional *Entry Details* is utilized the nested *Transaction Details* element is mandatory.

> *Transaction Details* has a variety of nested elements closely associated with *Entry* level elements. The *References* element however is nested to include a variety of references related to the entry including for example the *UETR*

![](_page_567_Picture_4.jpeg)

![](_page_567_Figure_5.jpeg)

Additionally, *Transaction Details* also has a variety of elements capturing details from the underlying transaction, which amongst other business transactions includes payment transaction data. For example, *Remittance Information* and *Related Parties*

**Min 0 – Max 1 Min 0 – Max 1**

The Bank to Customer Account Report message *Related Parties* and *Related Agents* represents a set of optional nested elements related to the underlying transaction. Where the *Entry Details* (the set of elements *Related Parties/Agents* belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message.

![](_page_568_Picture_2.jpeg)

#### These *Related Parties* include : These *Related Agents* include :

- *Instructing Party*
- *Debtor*
- *Debtor Account*
- *Ultimate Debtor*
- *Creditor*
- *Creditor Account*
- *Ultimate Creditor*

Settlement, it could be conceivable that these optional CBPR+ element may be populated

- *Instructing Agent*
- *Instructed Agent*
- *Debtor Agent*
- *Creditor Agent*
- *Intermediary Agent 1*
- *Intermediary Agent 2*
- *Intermediary Agent 3*

![](_page_568_Picture_18.jpeg)

*Trading Party* is also present in the *Related Parties* elements, and the following are present in the *Related Agents* elements: *Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place*. Although these elements are not directly associated with a payment, as a Customer receiving an Account Report related to other Business Domains e.g. a Security

The Bank to Customer Account Report message *Entry Details* have a number of additional elements beyond *Related Parties* and *Related Agents* to capture information from the underlying payment.

![](_page_569_Picture_1.jpeg)

### These are:

- *Local Instrument*
- *Purpose*
- *Related Remittance Information*
- *Remittance Information*
- *Related Dates* such as the *Interbank Settlement Date*
- *Tax*

For *Payment Return* (pacs.004) it is also possible to capture *Return Information* which includes:

- The *Original Bank Transaction Code* of the original Entry
- The *Originator*of the return from the pacs.004
- And the *Reason* code.

![](_page_569_Picture_13.jpeg)

*Remittance Information* as an end-to-end element should be passed unaltered from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account Statement/Account Report (camt) The *Remittance Information* element is common to these message sets.

It should also be mentioned that the Bank to Customer Account Report message *Entry Details* have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture *Additional Transaction Information*.

![](_page_570_Picture_1.jpeg)

### These are:

- *Related Quantity*
- *Financial Instrument Identification*
- *Corporate Action*
- *Safekeeping Account*
- *Cash Deposit*
- *Card Transactions*

Use case should be considered as a principal example whereby use case may be cross referenced

#### **Bank to Customer Reports**

Use Case c.52.1.a – Bank to Customer Account Balance Report produced by the Creditor Agent

Use Case c.52.1.b – Bank to Customer Account Intraday Transaction Report produced by the Creditor Agent

Use Case c.52.1.b.1 – Bank to Customer Account Intraday Transaction Report/s and Account Statement produced by the Creditor Agent

Use Case c.52.1.c – Bank to Customer Account Intraday Transaction and Balance Report produced by the Creditor Agent

![](_page_571_Figure_6.jpeg)

![](_page_571_Figure_7.jpeg)

![](_page_572_Figure_0.jpeg)

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries 2 4

Agent B processes the payment on Agent C 3

Agent C processes the payment on Agent D

Creditor Agent credits the account of the Creditor 5

Creditor Agent as the Account Servicer produces and sends a balance report to either the Account Owner, or an authorised third party. 6

## **Creditor Agent**

![](_page_573_Figure_1.jpeg)

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries 2 4

Agent B processes the payment on Agent C 3

Agent C processes the payment on Agent D

Creditor Agent credits the account of the Creditor 5

6

Creditor Agent as the Account Servicer produces and sends a balance report to either the Account Owner, or an authorised third party.

## **Statement produced by the Creditor Agent**

![](_page_574_Figure_1.jpeg)

- Debtor initiates a payment instruction to the Debtor Agent
- Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries 32
- Agent B processes the payment on Agent C

- Agent C processes the payment on Agent D 4
  - Creditor Agent credits the account of the Creditor

5

Creditor Agent as the Account Servicer produces and sends several intraday transaction reports throughout the business day to either the Account Owner, or an authorised third party.

Creditor Agent C as the Account Servicer produces an Account Statement at the close of the business day reflecting all the transaction entries, include those provide in the Intraday

## **by the Creditor Agent**

![](_page_575_Figure_1.jpeg)

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries 2 4

Agent B processes the payment on Agent C 3

Agent C processes the payment on Agent D

Creditor Agent credits the account of the Creditor 5

6

Creditor Agent as the Account Servicer produces and sends a intraday transaction and balance report to either the Account Owner, or an authorised third party.

## <span id="page-576-0"></span>**Bank to Customer Statement**

![](_page_577_Picture_0.jpeg)

The *Bank To Customer Statement*  message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message. It is used to inform the account owner, or authorised party, of the entries booked to the account, and to provide the owner with balance information on the account at a given point in time

![](_page_577_Picture_2.jpeg)

The Bank to Customer Account Statement is restricted to a single account statements per InterAct message (100,000 bytes) This message must be bilaterally agreed between the Account Servicing Institution and the Account owner, and is establish by an

![](_page_578_Figure_0.jpeg)

Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Statement message to Account Servicer and Account Owner. Whereby the statement is send by the Account Servicer to the Account Owner and or authorised party. This message is used to inform the account owner, or authorised party, of the entries

Like the legacy MT Statement messages, the camt.053 Bank to Customer Account Statement is constrained in CBPR+ by the FINplus service's message size. Account Owner who needs to translate the camt.053 into the legacy MT 940 format has several considerations fortheAccount Serving Institution.

![](_page_579_Picture_1.jpeg)

![](_page_579_Picture_3.jpeg)

![](_page_579_Picture_4.jpeg)

ISO 20022 message element MT Field Name & (Tag option)

![](_page_579_Picture_7.jpeg)

![](_page_579_Picture_8.jpeg)

![](_page_579_Picture_9.jpeg)

*Balance Type*  **OPBD** (with no *Sub Type* INTM) **OPBD** (with *Sub Type* **INTM**)

![](_page_579_Picture_11.jpeg)

*Balance Type*  **CLBD** (with no *Sub Type* INTM) **CLBD** (with *Sub Type* **INTM**)

*Statement Identification* needed to create MT 940 Field 20 Transaction Reference Number

*Legal Sequence Number* needed to create MT 940 Field 28C Statement Number

needed to create MT 940 Field 28C Sequence Number

needed to create MT 940 Field 25a Account Identification

needed to create MT 940 Field 60F (first) Opening Balance needed to create MT 940 Field 60M (intermediate) Opening Balance

*Entry* used to create MT 940 Field 61 Statement Line

![](_page_579_Picture_19.jpeg)

needed to create MT 940 Field 62F (final) Closing Balance needed to create MT 940 Field 62M (intermediate) Closing Balance Interest rate changes on an account can be communicated using the camt.053. An Account Serving Institution who is considering the camt.053 to communicate such rate changes to the Account Owner may find the following comparison against the legacy MT 935 useful. However, compared the camt.053 to legacy MT, using the camt.053 is like combining the information of both the MT 935 and MT 940 together into one message.

![](_page_580_Picture_1.jpeg)

![](_page_580_Picture_2.jpeg)

![](_page_580_Picture_3.jpeg)

ISO 20022 message element

➢ **Transaction Reference Number** (Field 20)

### **Sequence**

➢ **Further Identification** (Field 13C)

- ➢ **Account Identification** (Field 25)
- ➢ **Effective Date of New Rate** (Field 30)
- ➢ **New Interest Rate** (Field 37H)
- ➢ **Sender To Receiver Information** (Field 72)

**NOT MAPPED**

**NOT MAPPED**

➢ *Group Header / Message Identification*

- ➢ *Statement / Account / Identification*
- ➢ *Statement / Interest / From Date*
- ➢ *Statement / Interest / Rate*

*Note - various other elements are mandatory in the camt.053 which are not derived from the payment instruction including ; Message Identification, Creation Date Time, Statement Identification, Statement Pagination, Balance, Credit Debit Indicator, Status, Bank Transaction Code/.. often these data elements and potentially other optional elements will be generated by the bank application when creating th e reporting message.*

## **Group Header**

![](_page_582_Picture_0.jpeg)

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Customer Statement message. However, the *Transaction Reference Number* (Field 20) could be considered a similar comparison.

![](_page_583_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_583_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The Bank to Customer Statement *Message Recipient* nested element provides details of the party authorised by the *Account Owner* to receive the Account Statement.

This element **should only** be used to identify the *Message Recipient* when different from the account owner, which is implied by the usage of COPY in the *Copy Duplicate Indicator* within the nested Statement element.

![](_page_584_Picture_3.jpeg)

Where *Message Recipient* is used the nested:

- Name Min 0 Max 1
- Postal Address Min 0 Max 1
- Identification Min 0 Max 1
- Contact Details Min 0 Max 1

may be used to capture information related to this party.

The Bank to Customer Statement *Original Business Query* element identifies a query to generate a report, for example a camt.060 Account Reporting Request.

![](_page_585_Picture_2.jpeg)

Where *Original Business Query* is used the original *Message identification* (i.e., the message identification of the camt.060 message) is required.

Original *Message Name identification* and Original *Creation Date Time* may also be provided.

Min 0 – Max 1

Min 1 - Max 1

The Bank to Customer Statement *Additional Information* element represents further details related to the account statement.

![](_page_586_Picture_2.jpeg)

Where the camt.053 is used for various end of cycle statement reporting (statement periods) the follow codes may be used to distinguish the different camt.053 usage:

**/EODY/** for End of Day - Daily Statement **/EOWK/** for End of Week - Weekly Statement **/EOMH/** for End of Month - Monthly Statement **/EOYR/** for End of Year - Yearly Statement

![](_page_586_Picture_5.jpeg)

Additional Information is a textual element restricted in CBPR+ to 500 characters.

![](_page_587_Picture_0.jpeg)

The Bank to Customer Account Statement *Statement* nested element reports information related to an account, most typically associated with account balances, and accounting entries (where entries have been processed on the account).

![](_page_588_Picture_2.jpeg)

The *Statement* element has been restricted to one statements. To report additional account statements to the Account Owner this would need to occur via a separate message in a similar way to the legacy MT 940 or MT 950.

![](_page_588_Picture_4.jpeg)

It **should also be noted** the Account Statement message is modelled identically to the Account Report (camt.052) therefore where an intraday transaction report is used the content can be capture identically to the statement at the close of the business day, in

<span id="page-589-0"></span>Similar to the legacy MT Statement messages the camt.053 Bank to Customer Account Statement is constrained in CBPR+ by the FINplus service's message order, the statement correlation and the last statement page.

![](_page_589_Figure_1.jpeg)

**Statement Order:** identifying the order in which statements should be processed or reconstituted. Options:

Statement Pagination

**Statement Correlation:** identifying statement which relate to each other for a given statement period. Options:

Legal Sequence Number

Last Statement: identifying when no further statements for a given period are expected i.e. period statement in finalised. Options:

camt.053

Statement Pagination, Last Page Indicator

The Bank to Customer Statement message *Identification* provides a mandatory element to identify the statement

![](_page_590_Picture_2.jpeg)

Unique reference assigned by the account servicer to unambiguously identify the account statement. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

The Bank to Customer Statement message *Statement Pagination* element provides the page number of the statement.

![](_page_591_Picture_2.jpeg)

*Statement Pagination* includes the *Page Number* and *Last Page indicator* elements. **Min 1 – Max 1 Min 1 – Max 1**

**For example** a *Page Number* of 2 represents the current account statement, being the second page of the and implying a previous account statement page had been sent. The *Last Page indicator*furtherimplies whether more pages are expected

![](_page_591_Picture_5.jpeg)

Note: Where Page Number is equal to 1 a Balance Type OPBD (Opening Booked)must be provided, without a sub type of INTM (Interim). Whereas if the Page Number is greater than 1 a Balance Type OPBD (Opening Booked) must be provided, with a sub type of INTM (Interim).

Where Last Page Indicator is true a Balance Type CLBD (Closing Booked) must be provided, without a sub type of INTM (Interim). Whereas if the Last Page Indicator is false a Balance Type CLBD (Closed Booked) must be provided, with a sub type of INTM (Interim).

The Bank to Customer Statement message *Electronic Sequence Number* allows the *Account Servicer* to assign a number to each statement which should increment by 1 for each electronic statement report sent.

![](_page_592_Picture_2.jpeg)

This element allows easy recognition of the statement order, equivalent to the legacy Field 28C Statement Number. The sequence should increment for each camt.053 electronic statement sent to the Account Owner or Authorised Party this number must be the same value where the statement continues over multiple pages (*Statement Pagination*) of the statement for a give account on a given day.

Should this sequence number be reset by the *Account Servicer*, this should not occur more frequently than once a year. Likewise, this 18 digit counter could be incremented to its maximum value before it's reset.

![](_page_592_Picture_5.jpeg)

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the *Account Servicer* and the *Account Owner*.

Fither Electronic Sequence Number or Legal Sequence Number

![](_page_593_Picture_1.jpeg)

The Bank to Customer Statement message *Reporting Sequence* specifies the choice of identification sequences. This can be used as an alterative to the *Statement Pagination* or *Electronic Sequence Number* as a way to identify the statement order, which is not confined to numeric values.

Where used the *Reporting Sequence* mandate a choice of nested element:

![](_page_593_Picture_4.jpeg)

- *From Sequence* identifies the start of a sequence range. **Min 1 – Max 1**
- *To Sequence* identifies the end of a sequence range. **Min 1 – Max 1**
- *From To Sequence* identifies the start and end of a sequence range. **Min 1 – Max \***
- *Equal Sequence* identifies a sequence. **Min 1 – Max \***
- *Not Equal Sequence* identifies a sequence to be excluded. **Min 1 – Max \***

![](_page_593_Figure_10.jpeg)

The Reporting Sequence may be provided in the camt.060 Account Reporting request to specify, for example, a range of Statements to be sent. More traditionally Account Statements are generated automatically on an end of day cycle.

The Bank to Customer Statement message *Legal Sequence Number* allows the *Account Servicer* to assign a number to each statement which should increment by 1 for each statement report sent.

![](_page_594_Picture_2.jpeg)

Where the statement is reported using multiple camt.053 messages for a given statement period the *Legal Sequence Number* must be the same number in each statement message, as it can be used to correlate the statements.

Where a paper statement is a legal requirement, it may have a number different from the electronic sequential number. In this case the *Legal Sequence Number* element represents the sequence number of the paper statement.

![](_page_594_Picture_5.jpeg)

Either *Electronic Sequence Number* or *Legal Sequence Number* must be provided to enable the identification of a statement number.

![](_page_595_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_595_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The Bank to Customer Statement message *From to Date* allows the *Account Servicer* to specify the start date time and end date time applicable to the statement.

Where *From to Date* is used the *From Date Time* and *To Date Time* become mandatory elements.

**Min 1 – Max 1 Min 1 – Max 1**

![](_page_596_Picture_5.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_596_Picture_9.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

*Statement*

The Bank to Customer Statement message *Copy Duplicate Indicator* is used as a choice to identify additional statement from the original sent to the Account Owner.

![](_page_597_Picture_2.jpeg)

*COPY* is used when a copy of the statement is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service such as liquidity sweeping or statement consolidation.

![](_page_597_Picture_4.jpeg)

*DUPL* is used when a duplicate of the statement is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request.

![](_page_597_Picture_6.jpeg)

*CODU* is used when a duplicate of a statement copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in place with the Account Servicer.

The Bank to Customer Statement message *Reporting Source* allows the *Account Servicer* to define the source of the statement, typically associated with an application.

![](_page_598_Picture_2.jpeg)

*Reporting Source* utilises the external Reporting Source code list. For example **ACCT** represents a statement or report based on accounting data, whereas **DEPT** represents a cash or deposit system.

Where the source of the statement is functionally required by the consumer of the statement i.e., the *Account Owner* or *Authorised Third Party*, the codes used should be bilaterally agreed.

The Bank to Customer Statement message *Account* provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath *Account*.

![](_page_599_Figure_2.jpeg)

The Bank to Customer Statement message mandatory *Account* also provides a number of optional nested element to identify the account for which debit and credit entries have been made.

![](_page_600_Figure_3.jpeg)

The Bank to Customer Statement message *Related Account* allows the identification of a related parent account for the account statement. For example, sweeping, pooling or virtual account for which the statement is produced can identify the parent account they hierarchically relate to.

![](_page_601_Picture_2.jpeg)

When *Related Account* is utilized, like *Account*, the *Identification* and *Currency* element become mandatory. **Min 1 – Max 1 Min 1 – Max 1**

Additionally the nested *Type* element, *Name* and nested *Proxy* element are optionally available. **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1**

![](_page_601_Picture_5.jpeg)

*Related Account* uses a variety of common elements described in more detail within the *Account* section.

![](_page_601_Picture_7.jpeg)

![](_page_601_Picture_8.jpeg)

![](_page_601_Picture_9.jpeg)

Tax

Provides details on any tax applied to the Interest. Where optional

The Bank to Customer Statement message mandatory *Balance* provides nested element to define the account balance at a specific point in time. The following four elements nested beneath *Balance* are **Min 1 – Max \***

![](_page_603_Figure_1.jpeg)

Balance Type code are used within the nested Balance element to represent the type/s of balance being reported. In comparison the legacy MT 940 utilizes different Fields and Tag options to represent a number of these Balance Types. The below extract from the externalised ISO Balance Type code list compares the code with the population of the equivalent information in the Legacy MT 940 Customer Statement.

| Code        | Sub<br>Type | Nam e                   | Definition                                                                                                                                                                                                                                                                                                                                                  | MT 940<br>Comparison |
|-------------|-------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| CLAV        |             | ClosingAvailable        | Closing balance of amount of money that is at the disposal of the account owner on the date specified.                                                                                                                                                                                                                                                      | Field 64             |
| CLBD        |             | ClosingBooked           | Balance of the account at the end of the pre-agreed account reporting period. It is the sum of the opening booked balance at the beginning of the period and all entries booked to the account during the pre-agreed account reporting period.                                                                                                              | Field 62F            |
| CLBD        | INTM        | ClosingBooked (Interim) | Interim Balance of the account at the end of the pre-agreed account reporting page. It is the sum of the opening booked balance at the beginning of the period and all entries booked to the account during the pre-agreed account reporting page.                                                                                                          | Field 62M            |
| <b>FWAV</b> |             | Forw ard Available      | Forward available balance of money that is at the disposal of the account owner on the date specified.                                                                                                                                                                                                                                                      | Field 65             |
| INFO        |             | Information             | Balance for informational purposes.                                                                                                                                                                                                                                                                                                                         | No equivalent        |
| ITAV        |             | InterimAvailable        | Available balance calculated in the course of the account servicer's business day, at the time specified, and subject to further changes during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified.                                                             | No equivalent        |
| ITBD        |             | InterimBooked           | Balance calculated in the course of the account servicer's business day, at the time specified, and subject to further changes during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified.                                                                       | No equivalent        |
| <b>OPAV</b> |             | OpeningAvailable        | Opening balance of amount of money that is at the disposal of the account owner on the date specified.                                                                                                                                                                                                                                                      | No equivalent        |
| OBBD        |             | OpeningBooked           | Book balance of the account at the beginning of the account reporting period. It always equals the closing book balance from the previous report.                                                                                                                                                                                                           | Field 60F            |
| OPBD        | INTM        | OpeningBooked (Interim) | Interim Book balance of the account at the beginning of the account reporting page. It always equals the closing book balance from the previous report page.                                                                                                                                                                                                | Field 60M            |
| PRCD        |             | PreviouslyClosedBooked  | Balance of the account at the previously closed account reporting period. The opening booked balance for the new period has to be equal to this balance.  Usage: the previously booked closing balance should equal (inclusive date) the booked closing balance of the date it references and equal that actual booked opening balance of the current date. | Field 60F            |

**Min 1 – Max \***

The Bank to Customer Statement message mandatory *Balance* also provides the optional set of nested element to define a *Credit Line*

**Min 0 – Max \***

The true/false Boolean of *Included* to clearly determine whether the Credit Line Amount is included in the balance is mandatory in the set of Credit Line element.

![](_page_605_Picture_4.jpeg)

Additionally, the following optional nested element may be used to identify:

- The *Type* of Credit Line, which may either use an external ISO Credit Line Type code or a proprietary code.
- A set of elements to provide *Credit Line* details
- The *Amount*(Currency and Amount) of the Credit Line
- The *Date* (nested as Date, DateTime) of the Credit Line, provided to distinguish where multiple Credit Line exist.

The final optional nested element within *Balance* is the *Availability* of the booked amount i.e., when it is available to be accessed.

![](_page_605_Picture_11.jpeg)

The *Credit Line* element is unlimited (Max \*) whereby more that one *Credit Line*  may be reported, the *Date* becomes an important element to distinguish between different Credit Lines.

![](_page_605_Picture_13.jpeg)

The Bank to Customer Statement message optional *Transaction Summary* provides a set of nested element to summarize entry information. Where the statement is reported using multiple camt.053 messages for a given statement period the *Transaction Summary* should only be included on the opening Statement message (*Balance Type* OPBD with no Balance *Sub Type*) summarizing the whole Statement Report (entire statement period) This aligns with the Common Global Implementation (CGI) where a *Transaction Summary*, if provided, would appear before the first *Entry* elements.

![](_page_606_Picture_2.jpeg)

Each of the following element allow an optional total of entries either as a *Number of Entries* and or as a *Sum*.

- ➢ *Total Entries*
- ➢ *Total Credit Entries*
- ➢ *Total Debit Entries*
- ➢ *Total EntriesPer Bank Transaction Code*

**Min 0 – Max \***

In addition to the *Number of Entries* and *Sum*, the *Total Entries Per Bank Transaction Code* requires the *Bank Transaction Code* element and optionally allows a variety of other optional elements. **Min 1 – Max 1**

![](_page_606_Picture_10.jpeg)

*Statement Transaction Summary*

*Total Entries*

*Total Credit Entries*

*Total Debit Entries*

**Min 0 – Max \***

The Bank to Customer Statement message optional *Entry* provides a significant variety of nested elements to represent the details associated with each *Entry*. For active accounts which have entries posted across them, this set of nested elements is arguably the most relevant for the account owner and in many way is comparable with the MT 940 Field 61 Statement Line.

Unlike the legacy MT Statement messages, the camt.053 has a number of dedicated elements to capture a variety of entry level data.

It also has a number of enhancements on the legacy MT Statement message where parties in the payment and customer remittance information, as examples, can provided to the *Account Owner.* 

![](_page_607_Figure_5.jpeg)

![](_page_608_Figure_0.jpeg)

![](_page_609_Figure_0.jpeg)

![](_page_610_Picture_0.jpeg)

The *Bank Transaction Code*  is designed to deliver a harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the **account servicer** to correctly report a transaction, which in its turn will help **account owners** to perform their cash management and reconciliation operations. Domain Family

The structure of the Bank Transaction Code has three levels:

> *Domain*: Highest definition level to identify the subledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.) **Family**: Medium definition level e.g. type of payment; credit transfer, direct debit etc. *Sub-family*: Lowest definition level e.g. type of cheques; draft etc.

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code combinations*  external code sets.

|    |                         | Payn                                                                                      | ents Domain Families                    |                                                | The description of <b>Pa</b>                     |
|----|-------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------|------------------------------------------------|--------------------------------------------------|
| 1. | Received Credit         | Receivable Credit Transfers are instructions to receive an amount of money from a del     |                                         |                                                | The description of <b>Ba</b>                     |
|    | Transfers               | the account owner. The receivable credit transfers are related to transactions received t |                                         |                                                | available to download                            |
|    |                         | account owner.                                                                            |                                         |                                                |                                                  |
| 2. | Issued Credit Transfers | Payable Credit Transfers are instructions to transfer an amount of money by the account   |                                         |                                                | code list page. These                            |
|    | 233000 01000 11002013   |                                                                                           |                                         | elated to instructions sent by the account     | . •                                              |
| 3. | Received Cash           | Transaction is related to incoming cash movements that are related to cash management     |                                         | Payments Domain Fa                             |                                                  |
|    | Concentration           |                                                                                           |                                         | account to optimise the return on the av       | Received and Issued                              |
|    |                         | funds.                                                                                    |                                         |                                                | Received and issued                              |
| 4. | Issued Cash             | Transaction is relate                                                                     | ed to outgoing cash moven               | nents that are related to cash managemen       |                                                  |
|    | Concentration           |                                                                                           |                                         | to optimise the return on the available f      | https://www.ico20022                             |
| 5. | Received Direct Debits  |                                                                                           |                                         | ated to instructions received by the acco      | https://www.iso20022                             |
|    |                         | to debit the account.                                                                     |                                         |                                                |                                                  |
| 6. | Issued Direct Debits    |                                                                                           |                                         | d to instructions sent by the account owi      |                                                  |
| _  |                         | collect an amount o Sub-Families for both                                                 |                                         |                                                |                                                  |
| 7. | Received Cheques        | Transaction is relate                                                                     |                                         | Received and Issued Credit Tra Definition      | usfers                                           |
|    | Issued Cheques          | from the cheque dra                                                                       | Internal Book Transfer                  | Transaction is a transfer between –two differ  | cent accounts within the same bank               |
| 8. | Issued Chedues          | 1 Transaction is relate                                                                   | Standing Order                          |                                                | order is an instruction given by a party having  |
|    |                         |                                                                                           | Standing Order                          |                                                | e. either debit account owner or originating pa  |
|    |                         |                                                                                           |                                         |                                                | at specified intervals during an implicit or exp |
|    |                         |                                                                                           |                                         | period of time. It is given once, and is valid | for an open or closed period of time.            |
|    |                         |                                                                                           | Cross-Border Standing                   | Transaction is a cross-border standing order   |                                                  |
|    |                         |                                                                                           | Order                                   |                                                |                                                  |
|    |                         |                                                                                           | SEPA Credit Transfer<br>Domestic Credit | Transaction is a SEPA credit transfer          |                                                  |
|    |                         |                                                                                           | Transfer                                | Transaction is a in-country domestic current   | cy credit transfer                               |
|    |                         |                                                                                           | Cross-Border Credit                     | Transaction is a cross-border credit transfer  |                                                  |
|    |                         |                                                                                           | Transfer                                |                                                |                                                  |
|    | Credit Transfer with    |                                                                                           |                                         | Transaction is a credit transfer including con | nmercial information, i.e. additional informat   |
|    |                         |                                                                                           | agreed Commercial                       | agreed between the sender and the receiver.    |                                                  |
|    |                         |                                                                                           | Information                             |                                                |                                                  |
|    |                         |                                                                                           | Financial Institution                   |                                                | ansfer, i.e. the debtor and creditor are financi |
|    |                         |                                                                                           | Credit Transfer                         | institutions.                                  | higher priority, or a DDIELIDO gradit tof-       |
|    |                         |                                                                                           | Priority Credit Transfer                |                                                | higher priority, eg a PRIEURO credit transfe:    |

The description of *Bank Transaction Codes* are available to download from the ISO20022.org external code list page. These include the descriptions for Payments Domain Families and sub-families for both Received and Issued Credit Transfers. **Min 1 – Max 1**

[https://www.iso20022.org/external\\_code\\_list.page](https://www.iso20022.org/external_code_list.page)

![](_page_612_Figure_0.jpeg)

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code combinations* external code sets.

As an example a debit statement transaction which relates to a cross-border payment initiated from an account would be represented by:

| Domain         | Family                        | Sub-Family                         |
|----------------|-------------------------------|------------------------------------|
| PMNT (Payment) | ICDT (Issued Credit Transfer) | XBCT (Cross-Border Credit Transfer |

![](_page_613_Figure_0.jpeg)

![](_page_614_Figure_0.jpeg)

The Bank to Customer Statement message optional *Entry Details* provides a variety of nested elements to represent the details associated with each *Entry*.

![](_page_615_Picture_2.jpeg)

*Batch* provides details on batched transactions such as the total *Number of Transactions*  the batched entry (sometimes referred to as a consolidated entry) represents. *Transaction Details* is a significant nested element which represents information on the underlying transaction.

When the Bank to Customer Statement message optional *Entry Details* is utilized the nested *Transaction Details* element is mandatory.

> *Transaction Details* has a variety of nested elements closely associated with *Entry* level elements. The *References* element however is nested to include a variety of references related to the entry including for example the *UETR*

![](_page_616_Picture_4.jpeg)

![](_page_616_Figure_5.jpeg)

Additionally, *Transaction Details* also has a variety of elements capturing details from the underlying transaction, which amongst other business transactions includes payment transaction data. For example, *Remittance Information* and *Related Parties*

![](_page_616_Picture_7.jpeg)

**Min 0 – Max 1 Min 0 – Max 1**

The Bank to Customer Statement message *Related Parties* and *Related Agents* represents a set of optional nested elements related to the underlying transaction. Where the *Entry Details* (the set of elements *Related Parties/Agents* belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message.

![](_page_617_Picture_3.jpeg)

#### These *Related Parties* include : These *Related Agents* include :

- *Instructing Party*
- *Debtor*
- *Debtor Account*
- *Ultimate Debtor*
- *Creditor*
- *Creditor Account*
- *Ultimate Creditor*

Settlement, it could be conceivable that these optional CBPR+ element may be populated

- *Instructing Agent*
- *Instructed Agent*
- *Debtor Agent*
- *Creditor Agent*
- *Intermediary Agent 1*
- *Intermediary Agent 2*
- *Intermediary Agent 3*

![](_page_617_Picture_19.jpeg)

*Trading Party* is also present in the *Related Parties* elements, and the following are present in the *Related Agents* elements: *Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place*. Although these elements are not directly associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security

The Bank to Customer Statement message *Entry Details* have a number of additional elements beyond *Related Parties* and *Related Agents* to capture information from the underlying payment.

![](_page_618_Picture_1.jpeg)

### These are:

- *Local Instrument*
- *Purpose*
- *Related Remittance Information*
- *Remittance Information*
- *Related Dates* such as the *Interbank Settlement Date*
- *Tax*

For *Payment Return* (pacs.004) it is also possible to capture *Return Information* which includes:

- The *Original Bank Transaction Code* of the original Entry
- The *Originator*of the return from the pacs.004
- And the *Reason* code.

![](_page_618_Picture_13.jpeg)

*Remittance Information* as an end-to-end element should be passed unaltered from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account Statement (camt) The *Remittance Information* element is common to these message sets.

It should also be mentioned that the Bank to Customer Statement message *Entry Details* have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture *Additional Transaction Information*.

![](_page_619_Picture_1.jpeg)

### These are:

- *Related Quantity*
- *Financial Instrument Identification*
- *Corporate Action*
- *Safekeeping Account*
- *Cash Deposit*
- *Card Transactions*

Use case should be considered as a principal example whereby use case may be cross referenced

#### **Bank to Customer Statements**

Use Case c.53.1.a – Bank to Customer Statement produced by the Creditor Agent

Use Case c.53.1.b – Bank to Customer Statement produced by the Debtor Agent

Use Case c.53.1.c – Bank to Customer Statement produced by an intermediary Agent

#### **Copy of Bank to Customer Statements**

Use Case c.53.2 – Bank to Customer Statement sent as an additionally copy to an authorised party

#### **Resent Bank to Customer Statements**

Use Case c.53.3 – Bank to Customer Statement resent a previously sent statement/s to the Account Owner

Use Case c.53.4 – Bank to Customer Statement resent a previously sent copy statement/s to an authorised party

#### **Forwarding of Bank to Customer Statements**

Use Case c.53.5 – Bank to Customer Statement sent to an authorised party who forward/provides on to the Account Owner (commonly referred to as an account concentrating model)

![](_page_620_Figure_12.jpeg)

![](_page_620_Figure_13.jpeg)

![](_page_621_Figure_0.jpeg)

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries 2 4

Agent B processes the payment on Agent C 3

Agent C processes the payment on Agent D

Creditor Agent credits the account of the Creditor 5

Creditor Agent as the Account Servicer produces and sends a statement to either the Account Owner, or an authorised third party. 6

![](_page_622_Figure_0.jpeg)

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries 2 4

Agent B processes the payment on Agent C 3

Agent C processes the payment on Agent D

Creditor Agent credits the account of the Creditor 5

6

Debtor Agent as the Account Servicer produces and sends a statement to either the Account Owner, or an authorised third party.

![](_page_623_Figure_0.jpeg)

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent B processes the payment on Agent C

Agent C processes the payment on Agent D

Creditor Agent credits the account of the Creditor

Intermediary Agent as the Account Servicer produces and sends a statement to either the Account Owner, or an authorised third party.

![](_page_624_Figure_0.jpeg)

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries 2 4

Agent B processes the payment on Agent C 3

Agent C processes the payment on Agent D

Creditor Agent credits the account of the Creditor 5

Creditor Agent as the Account Servicer produces and sends a statement to the Account Owner. 6

Creditor Agent as the Account Servicer sends an additional copy of the statement to an authorised third part. COPY is populated in the Copy

7

Duplicate Indicator element within the

## **Account Owner**

![](_page_625_Figure_1.jpeg)

- Debtor initiates a payment instruction to the Debtor Agent
- Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries 2
- Agent B processes the payment on Agent C 3

- Agent C processes the payment on Agent D 4
  - Creditor Agent credits the account of the Creditor

5

Creditor Agent as the Account Servicer produces and sends a statement to the Account Owner. 6

Creditor as the Account Owner requests a previously sent statement message/s to be resent to them. 7

8

Creditor Agent as the Account Servicer re-sends a duplicate statement to the account owner. DUPL is populated in the Copy Duplicate Indicator element within the Bank to Customer Statement message (camt.053)

## **authorised party**

![](_page_626_Figure_1.jpeg)

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries 2

Agent B processes the payment 3

Agent C processes the payment on Agent D 4

Creditor Agent credits the account of the Creditor 5

Creditor Agent as the Account Servicer produces and sends a statement to an authorised 6

third part.

Authorised third party requests a previously sent statement message/s to be resent to them.

Creditor Agent as the Account Servicer re-sends a duplicate statement to the authorised third party. CODU is populated in the Copy Duplicate Indicator element within the Bank to Customer Statement message

(camt.053)

8

### <span id="page-627-0"></span>**the Account Owner (commonly referred to as an account concentrating model)**

![](_page_627_Figure_1.jpeg)

5

![](_page_627_Picture_2.jpeg)

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (C) using Agents as an intermediary 2

Agent B processes the payment on Agent C 3

Creditor Agent credits the account of the Creditor 4

Creditor Agent as the Account Servicer produces and sends a statement to an authorised third part.

Authorised third part provides statement information to the Account Owner. Which could be the forwarded Camt.053 statement or the details via an alternative channel (e.g. host to host file, GUI etc.) 6

## <span id="page-628-0"></span>**Bank to Customer Debit Credit Notification**

![](_page_629_Picture_0.jpeg)

The *Bank To Customer Debit Credit Notification* message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message. It can be used to inform the account owner, or authorised party, of single or multiple debit and/or credit entries reported to the account

![](_page_629_Picture_2.jpeg)

The Bank to Customer Debit Credit Notification allows multiple Notifications per InterAct message (100,000 bytes) It is however recommended to report single notifications per transaction. This message must be bilaterally agreed between the Account Servicing Institution and the Account owner, and is establish by an

![](_page_630_Figure_0.jpeg)

Role of the Agent/s, Debtor and Creditor in the payment changes by description in the Bank to Customer Debit Credit Notification message to Account Servicer and Account Owner. Whereby the notification is sent by the Account Servicer to the Account Owner and or authorised party.

The *Customer Debit Credit Notification*  are optionally provided between the account servicing institution and the account owner, or authorised (third) party.

#### These messages:

- are used to inform on debit and/or credit entries reported to an account.
- and may also be complemented by:
  - a *Status Information*  message:
    - pacs.002 in Payment Clearing and Settlement, or pain.002 in Payment Initiation.
  - or by a bank statement such as the camt.053 *Bank to Customer Statement Report*

![](_page_631_Picture_7.jpeg)

![](_page_631_Figure_8.jpeg)

## **Group Header**

![](_page_633_Picture_0.jpeg)

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Customer Statement message. However the *Transaction Reference Number* (Field 20) could be considered a similar comparison.

![](_page_634_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_634_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The Bank to Customer Debit Credit Notification *Message Recipient* nested element provides details of the party authorised by the *Account Owner* to receive the Debit Credit Notification.

This element **should only** be used to identify the *Message Recipient* when different from the account owner, which is implied by the usage of COPY in the *Copy Duplicate Indicator* within the nested Notification element.

![](_page_635_Picture_2.jpeg)

Where *Message Recipient* is used the nested:

- Name Min 0 Max 1
- Postal Address Min 0 Max 1
- Identification Min 0 Max 1
- Contact Details Min 0 Max 1

May be used to capture information related to this party.

Min 0 - Max 1

The Bank to Customer Debit Credit Notification *Original Business Query* element identifies a query to generate a report, for example a camt.060 Account Reporting Request.

![](_page_636_Picture_2.jpeg)

Where *Original Business Query* is used the original *Message identification* (i.e. the message identification of the camt.060 message) is required.

Original *Message Name identification* and Original *Creation Date Time* may also be provided.

Min 0 - Max 1

Min 1 - Max 1

The Bank to Customer Debit Credit Notification *Additional Information* element represents further details related to the account statement.

![](_page_637_Picture_2.jpeg)

The camt.054 may be used to indicate a particular type of notification, recognizing all transactions within the notification belong to the type indicated below:

**/LBOX/** Lock Box

**/BULK/** Bulk reporting (batch transaction with underlying transaction)

**/RTRN/** Return report

**/CRED/** Notification with Credit entries ONLY

![](_page_637_Picture_8.jpeg)

Additional Information is a textual element restricted in CBPR+ to 500 characters.

![](_page_638_Picture_0.jpeg)

The Bank to Customer Debit Credit Notification *Notification* nested element captures debit and credit entry information for an account.

![](_page_639_Picture_2.jpeg)

The *Notification* element has a couple of options to notify on multiple Debits and or Credits. This can be achieved at either the *Notification* element itself which could principally report on more than one account held by the account owner with the Account Servicer or can be achieved at an *Entry* level.

Notification of multiple Debits and or Credits is perhaps more associated with a timed or batch creation of the camt.054 Bank to Customer Debit Credit Notification. Whereas the more common example of a real-time notification produced at the point of an account posting would typically notify on a single *Entry*.

The Bank to Customer Debit Credit Notification message *Identification* provides a mandatory element to identify the notification

![](_page_640_Picture_2.jpeg)

Unique reference assigned by the account servicer to unambiguously identify the account statement. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

The Bank to Customer Debit Credit Notification message *Notification Pagination* element provides the page number of the notification.

![](_page_641_Picture_2.jpeg)

**Min 1 – Max 1**

**Min 1 – Max 1**

Where *Notification Pagination* is used the *Page Number* and *Last Page indicator* elements are both mandatory.

**For example,** a *Page Number* of 2 represents the current account statement, being the second page of the and implying a previous account statement page had been sent. The *Last Page indicator* further implies whether more pages are expected

![](_page_641_Picture_7.jpeg)

Either *Message Pagination* (Group Header) or *Notification Pagination*  (Notification) may used but not both

The Bank to Customer Debit Credit Notification message *Electronic Sequence Number* allows the *Account Servicer* to assign a number to each notification which should increment by 1 for each electronic notification report sent.

![](_page_642_Picture_2.jpeg)

As a good practice this element allows easy recognition of the notification order, if not recognisable by other data within the notification, such as the **Notification** > **Identification** element.

Should this sequence number be reset by the *Account Servicer*, this should not occur more frequently than once a year. Likewise, this 18 digit counter could be incremented to its maximum value before it's reset.

![](_page_642_Picture_5.jpeg)

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the *Account Servicer* and the *Account Owner* 

The Bank to Customer Debit Credit Notification message *Reporting Sequence* specifies the choice of identification sequences. This can be used as an alterative to the *Statement Pagination* or *Electronic Sequence Number* as a way to identify the statement order, which is not confined to numeric values.

Where used the *Reporting Sequence* mandate a choice of nested element:

![](_page_643_Picture_3.jpeg)

- *From Sequence* identifies the start of a sequence range. **Min 1 – Max 1**
- *To Sequence* identifies the end of a sequence range. **Min 1 – Max 1**
- *From To Sequence* identifies the start and end of a sequence range. **Min 1 – Max \***
- *Equal Sequence* identifies a sequence. **Min 1 – Max \***
- *Not Equal Sequence* identifies a sequence to be excluded. **Min 1 – Max \***

![](_page_643_Picture_9.jpeg)

Although the Reporting Sequence may be provided in a camt.060 Account Reporting Request, the use of this message to request a Bank to Customer Debit Credit Notification is less compelling, whereby such notifications are typically triggered as the result of an account posting, rather than being requested.

The Bank to Customer Debit Credit Notification message *Legal Sequence Number* allows the *Account Servicer* to assign a number to each notification which should increment by 1 for each notification report sent.

![](_page_644_Picture_2.jpeg)

In the case of a real-time notification the *Legal Sequence Number* element has little value, unlike its use in a statement message.

![](_page_645_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_645_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The Bank to Customer Debit Credit Notification message *From to Date* allows the *Account Servicer* to specify the start date time and end date time applicable to the notification.

Where *From to Date* is used the *From Date Time* and *To Date Time* become mandatory elements.

**Min 1 – Max 1 Min 1 – Max 1**

![](_page_646_Picture_5.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_646_Picture_9.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

*Notification*

The Bank to Customer Debit Credit Notification message *Copy Duplicate Indicator* is used as a choice to identify additional notification from the original sent to the Account Owner.

![](_page_647_Picture_2.jpeg)

*COPY* is used when a copy of the notification is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service such as liquidity sweeping or statement consolidation.

![](_page_647_Picture_4.jpeg)

*DUPL* is used when a duplicate of the notification is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request.

![](_page_647_Picture_6.jpeg)

*CODU* is used when a duplicate of a notification copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in place with the Account Servicer.

The Bank to Customer Debit Credit Notification message *Reporting Source* allows the *Account Servicer* to define the source of the notification, typically associated with an application.

![](_page_648_Picture_2.jpeg)

*Reporting Source* utilizes the external Reporting Source code list. For example, **ACCT** represents a notification based on accounting data, whereas **DEPT** represents a cash or deposit system.

Where the source of the notification is functionally required by the consumer of the notification i.e., the *Account Owner* or *authorised Third Party*, the codes used should be bilaterally agreed.

#### **Min 1 – Max 1**

The Bank to Customer Debit Credit Notification message *Account* provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath *Account*.

![](_page_649_Figure_2.jpeg)

The Bank to Customer Debit Credit Notification message mandatory *Account* also provides a number of optional nested element to identify the account for which debit and credit entries have been made. **Min 1 – Max 1**

![](_page_650_Figure_1.jpeg)

The Bank to Customer Debit Credit Notification message *Related Account* allows the identification of a related parent account for the account notification. For example sweeping, pooling or virtual account for which the notification is produced can identify the parent account they hierarchically relate to.

**Min 1 – Max 1 Min 1 – Max 1**

When *Related Account* is utilized, like *Account*, the *Identification* and *Currency* element become mandatory.

Additionally, the nested *Type* element, *Name* and nested *Proxy* element are optionally available. **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1**

![](_page_651_Picture_6.jpeg)

![](_page_651_Picture_7.jpeg)

*Related Account* uses a variety of common elements described in more detail within the *Account* section.

![](_page_651_Picture_9.jpeg)

![](_page_651_Picture_10.jpeg)

![](_page_651_Picture_11.jpeg)

The Bank to Customer Debit Credit Notification message *Interest* provides interest information that applies to the account. Inclusion of such interest information is perhaps more common to the camt.053 Statement than a Debit Credit Notification. **Min 0 – Max \*** *Interest Reason* An element which may either use an embedded ISO Interest Type code; **INDY** (Intraday) **OVRN** (Over Night) or a proprietary code. It is used to identifier a particular interest type. The optional Reason for which interest is applied. The type of interest Rate defined as a *Percentage* and in an *Other* form. Validity Range optionally defines an *Amount*, *Credit Debit Indicator*and *Currency*. The date range for which interest has been calculated. *From Date Time* and *To Date Time* must be representing when using this element. Provides details on any tax applied to the Interest. Where optional **+ -** *Type Rate From To Date Tax*

*Identification* describes the tax levied, additionally with a *Rate* and or

The Bank to Customer Debit Credit Notification message optional *Transaction Summary* provides a set of nested element to summarize entry information. More commonly the Bank to Customer Debit Credit Notification is reporting a single Debit or Credit transaction, where understandably the use of Transaction Summary provides little value.

![](_page_653_Picture_2.jpeg)

Each of the following element allow an optional total of entries either as a *Number of Entries* and or as a *Sum*.

- ➢ *Total Entries*
- ➢ *Total Credit Entries*
- ➢ *Total Debit Entries*
- ➢ *Total EntriesPer Bank Transaction Code*

**Min 0 – Max \***

In addition to the *Number of Entries* and *Sum*, the *Total Entries Per Bank Transaction Code* requires the *Bank Transaction Code* element and optionally allows a variety of other optional elements. **Min 1 – Max 1**

![](_page_653_Picture_10.jpeg)

*Notification Transaction Summary*

*Total Entries*

*Total Credit Entries*

*Total Debit Entries*

The Bank to Customer Debit Credit Notification message optional *Entry* provides a significant variety of nested elements to represent the details associated with each Debit or Credit *Entry*.

![](_page_654_Picture_2.jpeg)

Unlike the legacy MT 900 MT 910 confirmation messages, the camt.054 has a number of dedicated elements to capture a variety of entry level data. It also has an number of enhancements on the legacy MT confirmation message where parties in the payment and customer remittance information, as examples, can provided to the *Account Owner.* 

![](_page_654_Figure_4.jpeg)

![](_page_655_Figure_0.jpeg)

![](_page_656_Figure_0.jpeg)

![](_page_657_Picture_0.jpeg)

The *Bank Transaction Code*  is designed to deliver a harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the **account servicer** to correctly report a transaction, which in its turn will help **account owners** to perform their cash management and reconciliation operations. Domain

Family

The structure of the Bank Transaction Code has three levels:

> *Domain*: Highest definition level to identify the subledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.) **Family**: Medium definition level e.g. type of payment; credit transfer, direct debit etc. *Sub-family*: Lowest definition level e.g. type of cheques; draft etc.

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code combinations*  external code sets.

## **descriptions**

| Payments Domain Families  1. Received Credit Transfers are instructions to receive an amount of money from a de the account owner. The receivable credit transfers are related to transactions received account owner.  2. Issued Credit Transfers  Payable Credit Transfers are instructions to transfer an amount of money by the account or a creditor. The payable credit transfers are related to instructions sent by the account or a creditor. The payable credit transfers are related to cash management activities initiated by the owner of the sending account to optimise the return on the area funds.  1. Issued Cash Transaction is related to outgoing cash movements that are related to cash management activities initiated by the owner of the account to optimise the return on the available activities initiated by the owner of the account to optimise the return on the available | available to download code list page. These Payments Domain For Received and Issue |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| the account owner. The receivable credit transfers are related to transactions received account owner.  2. Issued Credit Transfers  Payable Credit Transfers are instructions to transfer an amount of money by the account of a creditor. The payable credit transfers are related to instructions sent by the account of a creditor. The payable credit transfers are related to instructions sent by the account concentration activities initiated by the owner of the sending account to optimise the return on the affunds.  4. Issued Cash  Transaction is related to outgoing cash movements that are related to cash managements activities initiated by the owner of the sending account to optimise the return on the affunds.                                                                                                                                                                     | available to download code list page. These Payments Domain For Received and Issue |
| account owner.  2. Issued Credit Transfers  Payable Credit Transfers are instructions to transfer an amount of money by the account to a creditor. The payable credit transfers are related to instructions sent by the account to a creditor. The payable credit transfers are related to instructions sent by the account Concentration  Transaction is related to incoming cash movements that are related to cash management activities initiated by the owner of the sending account to optimise the return on the affunds.  Transaction is related to outgoing cash movements that are related to cash management account to optimise the return on the affunds.                                                                                                                                                                                                                                        | code list page. These Payments Domain F Received and Issue                         |
| 2. Issued Credit Transfers     Payable Credit Transfers are instructions to transfer an amount of money by the account to a creditor. The payable credit transfers are related to instructions sent by the account to a creditor. The payable credit transfers are related to instructions sent by the account Concentration activities initiated to incoming cash movements that are related to cash management funds.  4. Issued Cash  Transaction is related to outgoing cash movements that are related to cash management funds.                                                                                                                                                                                                                                                                                                                                                                         | code list page. These Payments Domain F Received and Issue                         |
| to a creditor. The payable credit transfers are related to instructions sent by the account.  3. Received Cash Concentration  Transaction is related to incoming cash movements that are related to cash management activities initiated by the owner of the sending account to optimise the return on the argunds.  4. Issued Cash  Transaction is related to outgoing cash movements that are related to cash management activities initiated by the owner of the sending account to optimise the return on the argunds.                                                                                                                                                                                                                                                                                                                                                                                    | Payments Domain F Received and Issue                                               |
| 3. Received Cash Concentration Transaction is related to incoming cash movements that are related to cash management activities initiated by the owner of the sending account to optimise the return on the argunds.  4. Issued Cash Transaction is related to outgoing cash movements that are related to cash management activities initiated by the owner of the sending account to optimise the return on the argunds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Received and Issue                                                                 |
| Concentration activities initiated by the owner of the sending account to optimise the return on the argunds.  4. Issued Cash Transaction is related to outgoing cash movements that are related to cash managements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Received and Issue                                                                 |
| funds.  4. Issued Cash  Transaction is related to outgoing cash movements that are related to cash manageme                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Neceived and issue                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :                                                                                  |
| Concentration activities initiated by the owner of the account to optimise the return on the available                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | https://www.iso2002                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | \                                                                                  |
| 5. Received Direct Debits The Received Direct Debit transactions are related to instructions received by the account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | , <u>,,</u>                                                                        |
| 6. Issued Direct Debits  The Issued Direct Debit transactions are related to instructions sent by the account ow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                    |
| collect an amount o                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                    |
| 7. Received Cheques Transaction is relate Received and Issued Credit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                    |
| from the cheque dra Sub-Family Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                    |
| 8. Issued Cheques Transaction is relate Internal Book Transfer Transaction is a transfer between -two d                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ng order is an instruction given by a party having                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | , i.e. either debit account owner or originating pa                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | rs at specified intervals during an implicit or exp                                |
| period of time. It is given once, and is va                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                    |
| Cross-Border Standing Order Transaction is a cross-border standing or                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | ler                                                                                |
| SEPA Credit Transfer Transaction is a SEPA credit transfer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                    |
| Domestic Credit Transaction is a in-country domestic cur                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | rency credit transfer                                                              |
| Transfer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                    |
| Cross-Border Credit  Transaction is a cross-border credit trans                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | er                                                                                 |
| Transfer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | commercial information, i.e. additional informat                                   |
| agreed Commercial agreed between the sender and the receiv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | er.                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | t transfer, i.e. the debtor and creditor are financi                               |
| Credit Transfer institutions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | . a and a country and a country are finding                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ith higher priority, eg a PRIEURO credit transfe:                                  |
| Payroll/Salary Payment Transaction is related to the payment of                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                    |

The description of *Bank Transaction Codes* are available to download from the ISO20022.org external code list page. These include the descriptions for Payments Domain Families and sub-families for both Received and Issued Credit Transfers.

**Min 1 – Max 1**

[https://www.iso20022.org/external\\_code\\_list.page](https://www.iso20022.org/external_code_list.page)

#### combinations

![](_page_659_Figure_1.jpeg)

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code combinations* external code sets.

As an example a debit notification which relates to a cross-border payment initiated from an account would be represented by:

| Domain         | Family                        | Sub-Family                         |
|----------------|-------------------------------|------------------------------------|
| PMNT (Payment) | ICDT (Issued Credit Transfer) | XBCT (Cross-Border Credit Transfer |

![](_page_660_Figure_0.jpeg)

![](_page_661_Figure_0.jpeg)

The Bank to Customer Debit Credit Notification message optional *Entry Details* provides a variety of nested elements to represent the details associated with each *Entry*.

![](_page_662_Picture_2.jpeg)

underlying transaction.

*Batch* provides details on batched transactions such as the total *Number of Transactions*  the batched entry (sometimes referred to as a consolidated entry) represents. *Transaction Details* is a significant nested element which represents information on the

When the Bank to Customer Debit Credit Notification message optional *Entry Details* is utilized the nested *Transaction Details* element is mandatory. **Min 0 – Max \***

**Min 1 – Max 1**

*Transaction Details* has a variety of nested elements closely associated with *Entry* level elements. The *References* element however is nested to include a variety of references related to the entry including for example the *UETR*

![](_page_663_Picture_2.jpeg)

Additionally *Transaction Details* also has a variety of elements capturing details from the underlying transaction, which amongst other business transactions includes payment transaction data. For example *Remittance Information* and *Related Parties*

## **Agents**

The Bank to Customer Debit Credit Notification message *Related Parties* and *Relegated Agents* represents a set of optional nested elements related to the underlying transaction. Where the *Entry Details* (the set of elements *Related Parties/Agents* belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message. **Min 0 – Max 1 Min 0 – Max 1**

![](_page_664_Picture_2.jpeg)

#### These *Related Parties* include : These *Related Agents* include :

- *Instructing Party*
- *Debtor*
- *Debtor Account*
- *Ultimate Debtor*
- *Creditor*
- *Creditor Account*
- *Ultimate Creditor*

Settlement, it could be conceivable that these optional CBPR+ element may be populated

- *Instructing Agent*
- *Instructed Agent*
- *Debtor Agent*
- *Creditor Agent*
- *Intermediary Agent 1*
- *Intermediary Agent 2*
- *Intermediary Agent 3*

![](_page_664_Picture_18.jpeg)

*Trading Party* is also present in the *Related Parties* elements, and the following are present in the *Related Agents* elements: *Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place*. Although these elements are not directly associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security

The Bank to Customer Debit Credit Notification message *Entry Details* have a number of additional elements beyond *Related Parties* and *Related Agents* to capture information from the underlying payment.

![](_page_665_Picture_1.jpeg)

### These are:

- *Local Instrument*
- *Purpose*
- *Related Remittance Information*
- *Remittance Information*
- *Related Dates* such as the *Interbank Settlement Date*
- *Tax*

For *Payment Return* (pacs.004) it is also possible to capture *Return Information* which includes:

- The *Original Bank Transaction Code* of the original Entry
- The *Originator*of the return from the pacs.004
- And the *Reason* code.

![](_page_665_Picture_13.jpeg)

*Remittance Information* as an end-to-end element should be passed unaltered from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account Statement (camt) The Bank to Customer Debit Credit Notification may also capture this information. The

It should also be mentioned that the Bank to Customer Credit Debit Notification message *Entry Details* have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture *Additional Transaction Information*.

![](_page_666_Picture_1.jpeg)

### These are:

- *Related Quantity*
- *Financial Instrument Identification*
- *Corporate Action*
- *Safekeeping Account*
- *Cash Deposit*
- *Card Transactions*

Use case should be considered as a principal example whereby use case may be cross referenced

#### **Debit/Credit Notification related to a Serial Customer Payments**

Use Case c.54.1.1 – Customer Debit/Credit Notification (camt.054) of a Customer Credit Transfer (pacs.008)

#### **Debit/Credit Notification related to a Serial Financial Institution Payments**

Use Case c.54.2.1 – Customer Debit/Credit Notification (camt.054) of a FI to FI Credit Transfer (pacs.009)

#### **Debit/Credit Notification related to a Cover Method Payments**

Use Case c.54.3.1 – Customer Debit/Credit Notification (camt.054) of a payment using the cover method

## (pacs.008)

![](_page_668_Figure_1.jpeg)

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent A provides a debit notification to the debtor using the camt.054 to confirm their account has been debited for the payment initiation request. This notification may compliment additional status information or statement report messages

Agent C processes the payment on Agent D

Agent D credits the account of the Creditor, providing a credit notification using the camt.054

Agent B processes the payment on Agent C

**(pacs.009)**

![](_page_669_Figure_1.jpeg)

Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

2

Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent D) using Agents C as an intermediary.

2b

Debtor Agent (Agent B) provides a debit notification to the debtor using the camt.054 to confirm their account has been debited for the payment initiation request. This notification may be complimented by an additional status information message. But typically will be compliment by an end of business day statement report messages

3

Creditor Agent (C) credits the account of Agent D and provides a credit notification (camt.054) in addition to an account statement (camt.053)

![](_page_670_Figure_0.jpeg)

Agent B processes the payment

to process the pacs.008 (if not already done so) and apply a credit to the

Intraday Credit Notification is required when using the cover method unless an alternative

## <span id="page-671-0"></span>**Notification to Receive**

<span id="page-672-0"></span>![](_page_672_Picture_0.jpeg)

The *NotificationToReceive* message is sent by an account owner or by a party acting on the account owner's behalf to one of the account owner's account servicing institutions. It is an advance notice that the account servicing institution will receive funds to be credited to the account of the account owner. The *NotificationToReceive*message is used to advise the account servicing institution of funds that the account owner expects to have credited to its account.

![](_page_672_Picture_2.jpeg)

The Notification to Receive message is the ISO 20022 equivalent of the legacy MT210 Notice to Receive. It can be cancelled using the camt.058 where in the meantime the legacy MT 292 can be used to request its cancelation.

![](_page_673_Picture_0.jpeg)

Role of the Creditor Agent and Creditor in the payment changes description in the Notification to Receive message (camt.057). The Account Owner is typically the Creditor and the Account Servicer is typically the Creditor Agent. This will be followed up with a pacs transferring the funds to the Account Servicer on the expected value date.

#### **payment message (pacs.008/pacs.009) and the Notification to Receive (camt.057)** The Parties defined within the Notification to Receive (camt.0057) provide advance information to the Account Servicer of information included in the payment message. Noting a Debtor must always be present in the camt.057 (it is mandatory in the pacs payment message) but Debtor Agent may not be provided (Debtor Agent is mandatory in the pacs..08 but not he pacs.009) **camt.053 pacs.002 camt.057 A B C Party pacs camt.057** Debtor Debtor Agent Creditor Creditor Agent Account Servicer Debtor Agent Debtor Account Owner **D pacs pacs.002 pacs pacs.002 pacs D**

## **Group Header**

![](_page_676_Picture_0.jpeg)

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

**Min 1 – Max 1**

The *Message Identification* in the Cash Management (camt) messages is equivalent to field 20 Transaction Reference Number of the MT 210 in the legacy MT Notice to Receive.

The camt.057 message *Creation Date Time* captures the date and time which the message was created.

![](_page_677_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_677_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Min 0 - Max 1

The Notification to Receive *Message Sender* nested element provides details of the party that is sending the message, where the *Message Sender* is different from the account owner.

![](_page_678_Picture_2.jpeg)

#### Where *Message Sender, Party* is used the nested:

- Name Min 0 Max 1
- Postal Address Min 0 Max 1
- Identification Min 0 Max 1
- Contact Details Min 0 Max 1

May be used to capture information related to this party.

#### Where *Message Sender, Agent* is used the nested *Financial Institution*:

BICFI Min 1 – Max 1

- Clearing System Member Identification Min 0 Max 1
- LEI Min 0 Max 1

Group Header → Message Sender

May be used to capture information related to this Agent.

![](_page_679_Picture_0.jpeg)

#### **Min 1 – Max 1**

<span id="page-680-0"></span>The Notification to Receive *Notification* element contains nested elements to provide further details on the account notification such as the related parties, the expected amount to be received and value date of the expected receipt.

![](_page_680_Picture_2.jpeg)

The Notification nested element **Item** can contain multiple Credits. Where there is only one expected credit then only the Item element will contain the Item **Identification**and the **Amount**.

![](_page_680_Picture_4.jpeg)

Today the status of a camt.057 has no documented ISO 20022 reporting process, to theAccount Owner by theAccount Servicer.

Generally, if the Account Servicer does not require notification the message will be ignored.

![](_page_680_Picture_7.jpeg)

The Notification to Receive message *Notification Identification* provides a mandatory element to identify the account notification.

![](_page_681_Picture_2.jpeg)

Unique reference assigned by the account owner to unambiguously identify the account notification. There is no equivalent in the MT210. It is recommended that the Message Identification is repeated for the Notice to Receive Identification.

The Notification to Receive message *Account* element provides nested elements to identify the account for which the credit entry has been made. The following two mandatory elements are nested beneath *Account*. **Min 0 – Max 1 Min 1 – Max 1** An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account. *Account Currency* The *Currency* for which the account is held. This is identified using the three characters ISO currency code. The Name of the Account, as Assigned by the servicing institution. *Type Name* a unique *Identification* for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account. *Identification*

*Proxy*

Anested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO Proxy Account Type code The *Account Owner* is the Creditor, and the *Account Servicer* is the Creditor Agent. They are static roles in the camt.057 Notification to Receive.

The *Account Owner* must be identified either by the Party name and postal address or as an Agent using a Financial Institution identification. The *Account Servicer* must be identified as an Agent by using the Financial Institution identification.

![](_page_683_Picture_4.jpeg)

The Account Owner and the Account Servicer are the Creditor and Creditor Agent respectively in a pacs.008 FI to FI Customer. Where utilised, it is **recommended** to use the element at the Item level.

![](_page_683_Picture_6.jpeg)

The Notification to Receive message *Related Account* element allows the identification of a related parent account for the account notification. For example sweeping, pooling or virtual account for which the notification is produced can identify the parent account they hierarchically relate to.

In the context of a Notification to Receive this element provides little business value.

![](_page_684_Picture_3.jpeg)

When *Related Account* is utilized, like *Account*, the *Identification* and *Currency* element become mandatory. **Min 1 – Max 1 Min 0 – Max 1**

Additionally, the nested *Type* element, *Name* and nested *Proxy* element are optionally available. **Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1**

![](_page_684_Picture_6.jpeg)

*Related Account* uses a variety of common elements described in more detail within the *Account* section.

![](_page_684_Picture_8.jpeg)

The Notification to Receive message *Total Amount* provides the sum of all the amounts of all the *Item* entries. Where utilised the *Item* element is a mandatory element which contains information about the expected receipt. The Notification to Receive can contain multiple items. *Expected Value Date* is the date on which the final receiving agent expects to receive the total amount. **Min 0 – Max 1**

![](_page_685_Picture_2.jpeg)

The Total Amount provides a control total where there are multiple credits recorded within the Item element. The Total Amount element should not be used where there is a single expected credit.

![](_page_685_Picture_4.jpeg)

The*Expected Value Date* takes the format YYYY-MM-DD

![](_page_685_Picture_6.jpeg)

The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the *Debtor*. The following describes the *Debtor* nested **Party** elements in greater detail.

*Debtor Name* Mandatory *Name* (where a BIC identifier is not provided) by which the party is known *Identification Country of*  Optional element to *Postal Address* Nested element capturing either structured or unstructured *Debtor*

> capture the Debtor's ISO country code of residence

*Residence*

![](_page_686_Figure_2.jpeg)

Nested element capturing the

address details

various types of identifiers for the party e.g. BIC, LEI etc.

The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the *Debtor*. The following describes the *Debtor* nested **Agent** elements in greater detail. *Debtor Name* by which the Agent is *Name* known *Postal Address* Information used to identify a Debtor by a clearing system identifier. *BICFI* The BIC which identifies the *Debtor Clearing System Member Id* Nested element capturing either structured or unstructured *Debtor* Legal entity identifier of the *LEI* financial institution.

address details

![](_page_688_Picture_0.jpeg)

![](_page_688_Picture_1.jpeg)

The *Debtor Agent* element in the camt.057 Notification to Receive captures the Debtor Agent of the payment i.e., the Financial Institution servicing an account for the Debtor.

The *Debtor Agent* and *Intermediary Agent* elements allow the Treasury function at the Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time.

#### **Min 0 – Max 1**

![](_page_688_Picture_5.jpeg)

The *Intermediary Agent* element in the camt.057 Notification to Receive capture the Intermediary agent between the Debtor Agent and the Account Servicer i.e. the Agent from whom the Creditor Agent expects to receive the payment from.

The *Debtor Agent* and *Intermediary Agent* elements allow the Treasury function at the Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time.

![](_page_688_Picture_8.jpeg)

The *Debtor Agent* and *Intermediary Agent* elements allow the Account Servicing Institution's Treasury department to proactively follow up, as necessary, the actual payment if it fails to arrive by an expected time.

![](_page_688_Picture_10.jpeg)

<span id="page-689-0"></span>The Notification to Receive message mandatory *Item* element provides details of the expected amount on the account serviced by the account servicer. There is no equivalent field in the legacy MT210 Notice to Receive.

![](_page_689_Picture_2.jpeg)

The various nested elements within the *Item* element are very useful in the case where there are multiple credits. The Creditor Agent will be able to reconcile the incoming receipts against the list of expected receipts detailed in the *Item* element and will be check completeness of all expected receipts and identify any missing receipts.

![](_page_689_Picture_4.jpeg)

**Min 1 – Max \***

The Notification to Receive message mandatory *Item* element provides details of the expected amount on the account serviced by the account servicer. There is no equivalent field in the legacy MT210 Notice to Receive.

![](_page_690_Figure_2.jpeg)

Use case should be considered as a principal example whereby use case may be cross referenced

#### **Notification to Receive multiple receipts**

Use Case c.57.1.1 – Notification to Receive (camt.057) followed by Customer Credit Transfers (pacs.008)

Use Case c.57.1.2 – Notification to Receive (camt.057) followed by FI Credit Transfers (pacs.009)

Use Case c.57.1.3 – Notification to Receive (camt.057) where the receipt is settled by the cover method.

Use Case c.57.1.4 – Notification to Receive (camt.057) for a FI Credit Transfers cover (pacs.009 cov).

## **(pacs.008)**

![](_page_692_Figure_1.jpeg)

Creditor is expecting to receive a payment from the Debtor. As the Account Owner sends a Notification to Receive to Agent C as Account Servicer. 1

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (C) using Agents B as an intermediary. 3

Creditor Agent (C) as Account Servicer sends and end of day statement to Creditor as Account Owner confirming accounting entries.

5

2 Debtor initiates a payment instruction to the Debtor Agent (A).

Agent (B) processes the payment on to the Creditor Agent (C).

4

<span id="page-693-0"></span>![](_page_693_Figure_0.jpeg)

Creditor is expecting to receive a payment from Debtor. As the Account Owner sends a Notification to Receive to Agent C as Account Servicer. 1 2

Debtor (A) initiates a serial payment towards the Creditor Agent (C) using Agents (B) as an intermediary.

Creditor Agent (C) as Account Servicer sends and end of day statement to Creditor as Account Owner confirming accounting entries.

Agent (B) processes the payment on to the Creditor Agent (C). 3

![](_page_694_Figure_0.jpeg)

![](_page_695_Figure_0.jpeg)

## <span id="page-696-0"></span>**Notification to Receive Cancelation Advice**

![](_page_697_Picture_0.jpeg)

The *Notification To Receive Cancellation Advice* message is sent by an account owner or by a party acting on the account owner's behalf to one of the account owner's account servicing institutions. It is used to advise the account servicing institution about the cancellation of a notification sent in a previous *Notification To Receive* message.

![](_page_698_Picture_0.jpeg)

Role of the Creditor Agent and Creditor in the payment changes description in the Notification to Receive message (camt.057). The Account Owner is typically the Creditor and the Account Servicer is typically the Creditor Agent. The Notification to Receive Cancellation Advice (camt.058) is used to request the cancellation of a previous Notification to Receive.

## **Group Header**

![](_page_700_Picture_0.jpeg)

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

**Min 1 – Max 1**

The *Message Identification* in the Cash Management (camt) messages is equivalent to field 20 Transaction Reference Number of the MT 292 in the legacy MT Request for Cancellation.

The camt.058 message *Creation Date Time* captures the date and time which the message was created.

![](_page_701_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_701_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

#### Min 0 - Max 1

The Notification to Receive Cancellation Advice *Message Sender* nested element provides details of the *Party* or *Agent* that is sending the message, where the *Message Sender* is different from the account owner.

This element has no equivalent in the legacy MT 292 Request for Cancellation.

![](_page_702_Picture_3.jpeg)

Where *Message Sender*, *Party* is used the nested:

- Name Min 0 Max 1
- Postal Address Min 0 Max 1
- Identification Min 0 Max 1
- Contact Details Min 0 Max 1

May be used to capture information related to this party.

Where *Message Sender, Agent* is used the nested *Financial Institution*:

- BICFI Min 1 Max 1
- Clearing System Member Identification Min 0 Max 1
  - LEI Min 0 Max 1

Group Header Message Sender

May be used to capture information related to this Agent.

## **Original Notification**

#### **Min 1 – Max 1**

The Notification to Receive Cancellation Advice *Original Notification* element contains nested elements to provide further details on the original camt.057 notification to receive. such as the related parties, the expected amount to be received and value date of the expected receipt.

![](_page_704_Picture_2.jpeg)

The *Original Notification* nested element enables the ability to reconcile this cancellation advice against the Notification originally received, so that appropriate action can be take to remove the advised currency and amount from predicted currency positions at theAccount Servicer.

![](_page_704_Picture_4.jpeg)

![](_page_704_Picture_6.jpeg)

![](_page_704_Picture_7.jpeg)

Camt.058

#### *Group Header*

- ➢ *Message Identification*
- ➢ *Creation Date Time*

#### *Notification*

- ➢ *Identification*
- ➢ *Debtor*

#### *Item*

- ➢ *Identification*
- ➢ *End to End Identification*

#### *Original Notification*

- ➢ *Original Message Identification*
- ➢ *Original Creation Date Time*
- ➢ *Original Notification Identification*
- ➢ *Original Notification Reference*
  - ➢ *Debtor*
  - ➢ *Original Item*
    - ➢ *Original Item Identification*
    - ➢ *Original End to End Identification*

The Notification to Receive Cancellation Advice message *Original Message Identification* provides a mandatory element to identify the Message Identification from the original camt.057.

![](_page_705_Picture_2.jpeg)

This 35 character identifier is a point-to-point reference used to unambiguously identify the Notification to Receive message, capture in its group header.

The camt.058 message *Original Creation Date Time* captures the date and time which the original Notification to Receive message was created.

![](_page_706_Picture_2.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_706_Picture_6.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The Notification to Receive Cancellation Advice message *Original Notification Identification* provides a mandatory element to identify the account notification.

![](_page_707_Picture_2.jpeg)

Unique reference assigned by the account owner to unambiguously identify the original account notification.

The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the **Debtor**. The following describes the *Debtor* nested **Party** elements in greater detail.

identifier is not provided) by Name which the party is known Nested element capturing either Postal structured or unstructured Debtor **Address Debtor** Identification Optional element to Country of

Residence

Mandatory *Name* (where a BIC

capture the Debtor's ISO

country and of regidence

![](_page_708_Figure_2.jpeg)

Nested element capturing the

various types of identifiers for the party e.g. BIC, LEI etc.

address details

The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the *Debtor*. The following describes the *Debtor* nested **Agent** elements in greater detail. *Debtor Name* by which the Agent is *Name* known *Postal Address* Information used to identify a Debtor by a clearing system identifier. *BICFI* The BIC which identifies the *Debtor Clearing System Member Id* Nested element capturing either structured or unstructured *Debtor* Legal entity identifier of the *LEI* financial institution.

address details

![](_page_710_Picture_0.jpeg)

The *Debtor Agent* element in the camt.058 Notification to Receive Cancellation Advice captures the Debtor Agent provided in the original Notification to Receive (camt.057) i.e., the Financial Institution servicing an account for the Debtor. **Min 0 – Max 1**

![](_page_710_Picture_2.jpeg)

*Original Notification Reference*

The Notification to Receive Cancellation Advice *Original Item Reference* nested element captures the references of the Original Item in the original Notification to Receive message.

![](_page_711_Picture_2.jpeg)

**Min 1 – Max \***

The *Original Item* nested element is repetitive as the original Notification to Receive message has the ability to notify on more than one item i.e. currency and amount expect. The following elements are nested within *Original Item*, of which *Identification* and *Amount* are required.

![](_page_711_Figure_5.jpeg)

![](_page_711_Picture_6.jpeg)

![](_page_711_Picture_7.jpeg)

## **Cancelation Reason**

The Notification to Receive Cancellation Advice *Cancellation Reason* nested element captures information associated with the reason for the Cancellation request.

![](_page_713_Picture_2.jpeg)

**Min 0 – Max 1**

the *Originator* element helps identify the party who issued the Cancellation request. Typically, this element would be used to identify the Account Owner as the Originator of the request, where the Notification to Receive Cancelation Advice message captured a *Message Sender* acting on the account owner's behalf.

![](_page_713_Picture_5.jpeg)

**Min 1 – Max 1**

the *Reason* is mandatory and represented by an embedded CBPR+ Cancellation *Code* choice ( )

![](_page_713_Picture_8.jpeg)

The *Additional Information* element may also be included to provide further details on the Cancellation reason.

![](_page_713_Picture_10.jpeg)

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

![](_page_713_Picture_12.jpeg)

Use case should be considered as a principal example whereby use case may be cross referenced

#### **Notification to Receive multiple receipts**

Use Case c.58.1.1 – Cancellation Advice for a Notification to Receive (camt.057) expecting a Customer Credit Transfers (pacs.008) Use Case c.58.1.2 – Cancellation Advice for a Notification to Receive (camt.057) expecting a FI Credit Transfers (pacs.009) Use Case c.58.1.3 – Cancellation Advice for a Notification to Receive (camt.057) where the receipt is settled by the cover method.

## **Customer Credit Transfers (pacs.008)**

![](_page_715_Picture_1.jpeg)

![](_page_715_Picture_2.jpeg)

![](_page_715_Picture_3.jpeg)

![](_page_715_Picture_4.jpeg)

Creditor is expecting to receive a payment from the Debtor. As the Account Owner they send a Notification to Receive to Agent C as Account Servicer.

Creditor subsequently understand the payment should no longer be expected for the given amount. They issue a cancellation advice to Agent C as Account Servicer, providing the reason NOLE (not longer expected). 2

## **Transfers (pacs.009)**

![](_page_716_Picture_1.jpeg)

![](_page_716_Picture_2.jpeg)

![](_page_716_Picture_3.jpeg)

Creditor is expecting to receive a payment from Debtor. As the Account Owner sends a Notification to Receive to Agent C as Account Servicer.

Creditor subsequently understand the payment should no longer be expected for the given amount. They issue a cancellation advice to Agent C as Account Servicer, providing the reason NOLE (not longer expected). 2

![](_page_717_Figure_0.jpeg)

## <span id="page-718-0"></span>**Account Reporting Request**

![](_page_719_Picture_0.jpeg)

The AccountReportingRequest message is sent by the account owner, either directly or through a forwarding agent, to one of its account servicing institutions. It is used to ask the account servicing institution to send a report for the account owner's account:

- BankToCustomerAccountReport (camt.052) or
- BankToCustomerStatement (camt.053) or
- BankToCustomerDebitCreditNotification (camt.054).

Account reports are often configured by the Account Servicing Institution as part of a static configuration. The Account Report Request could however be used as an alternative mechanism to request reports on a frequent or ad hoc basis.

Account Report Request can contain multiple *Reporting Request* elements as the maximum multiplicity is unbounded. This effectively allows multiple

![](_page_720_Figure_0.jpeg)

Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Report Request message to Account Servicer and Account Owner. Whereby the report request is sent by the Account Owner or authorised party to the Account Servicer. This message is used to request a report/s of the entries on an account, and/or to provide

## **Group Header**

![](_page_722_Picture_1.jpeg)

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point to point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Customer Statement message. However the *Transaction Reference Number* (Field 20) could be considered a similar comparison.

![](_page_723_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_723_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

The Account Report Request *Message Sender* nested element provides details of the party that is sending the request.

This element **should only** be used to identify the *Message Sender* when different from the account owner.

![](_page_724_Picture_3.jpeg)

Where *Message Sender* is used, a choice of nested **Party** or **Agent** may be used to identify the Sender.

• *Name*

**Min 0 – Max 1**

• *Postal Address*

**Min 0 – Max 1**

• *Identification*

**Min 0 – Max 1**

• *Country of Residency* **Min 0 – Max 1**

#### **Party**: **Agent**:

![](_page_724_Picture_14.jpeg)

![](_page_725_Picture_0.jpeg)

The Account Reporting Request *Reporting Request* nested element capture the detail related the request.

![](_page_726_Picture_2.jpeg)

Many **Account Servicing Institutions** service their **Account Owner** customers through statics account configuration/s. Whereby a variety of reports can be generated on either a time or event bases routine.

The *Reporting Request* may be used as either an alterative to a static configuration or to request ad hoc reports (whether that be an additional report to the statics configuration or to resend reports previous reported).

The Account Reporting Request message *Identification* provides a mandatory element to identify the Request

![](_page_727_Picture_2.jpeg)

Unique reference assigned by the account owner (or Message Sender on behalf of the account owner) to unambiguously identify the account statement. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT request message.

The Account Reporting Request message *Requested Message Name Identification* provides a mandatory element to identify the name of the report being request.

![](_page_728_Picture_2.jpeg)

This element specifies which type of report is begin requested. The report is representedby its full name. For example:

**camt.052.001.08** or **camt.053.001.08** or **camt.054.001.08**

#### **Min 0 – Max 1**

The Account Reporting Request message *Account* provides nested elements to identify the account for which the request relates to. A number of elements are nested beneath *Account*, of which the *Identification* element is mandatory.

![](_page_729_Picture_2.jpeg)

#### **Min 1 – Max 1**

a unique *Identification* for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account.

The Account Reporting Request message *Account* also provides an number of optional nested element to identify the account for which the request relates to.

![](_page_730_Figure_3.jpeg)

The Account Reporting Request message *Account Owner* identifiers the mandatory owner of the account that the Account Report Request relates to.

![](_page_731_Picture_2.jpeg)

Where *Account Owner* is used, a choice of nested **Party** or **Agent** may be used to identify the owner.

• *Name*

**Min 0 – Max 1**

• *Postal Address* • *Identification*

**Min 0 – Max 1**

**Min 0 – Max 1**

• *Country of Residency* **Min 0 – Max 1**

**Party**: **Agent**:

![](_page_731_Picture_12.jpeg)

[Take me to the Agent identification](#page-21-0)

Typically the Account Name (see the previous page) represents the Account Owner's Name in accordance with standard Know Your Customer (KYC). The mandatory Account Owner elements enables more detail to be captured such as an address for a Party or a BIC for an Agent.

**Min 0 – Max 1**

The Account Reporting Request message *Account Servicer* provides an optional element to capture the Agent who is acting as an Account Servicing Institution. Typically, this would be the same Agent the Account Reporting Request is sent to, who is also identified in the Business Application Header.

![](_page_732_Picture_2.jpeg)

### **Financial InstitutionIdentification**:

- *BICFI*
- *Clearing System MemberIdentification*
- *LEI*
- *Name*
- *Postal Address*

![](_page_732_Picture_9.jpeg)

The Account Reporting Request message *Report Period* provides the ability to specify the period for which the request relates. Where used this nested element captures a mandatory *From to Date* and an optionally *From to Time* element. **Min 1 – Max 1**

**Min 0 – Max 1**

![](_page_733_Picture_3.jpeg)

*From to Date* captures a mandatory *From Date* and an optional *To Date*. It allows the request to specify the date period for which the report is being requested.

![](_page_733_Picture_5.jpeg)

*From to Date*

![](_page_734_Picture_1.jpeg)

The Account Reporting Request message *Reporting Sequence* specifies the choice of identification sequences. This can be used as an alterative to the *Reporting Period* to request a sequence of reports, where the Account Servicing Institution uses this element within the reports they provide.

![](_page_734_Picture_3.jpeg)

Where used the *Reporting Sequence* mandate a choice of nested element:

- *From Sequence* identifies the start of a sequence range. **Min 1 – Max 1**
- *To Sequence* identifies the end of a sequence range. **Min 1 – Max 1**
- *From To Sequence* identifies the start and end of a sequence range. **Min 1 – Max \***
- *Equal Sequence* identifies a sequence. **Min 1 – Max \***
- *Not Equal Sequence* identifies a sequence to be excluded. **Min 1 – Max \***

**Min 0 – Max 1**

The Account Reporting Request message *Requested Transaction Type* provides the ability to identify the specific type of transactions the request wishes to be reported.

**Min 1 – Max 1 Min 1 – Max 1**

Where used the *Status* element and *Credit Debit Indicator* elements are mandatory.

![](_page_735_Picture_5.jpeg)

- *Status* is a nested element which may either use a choice of external ISO Entry Status code or a proprietary code. It is used to indicate the transaction entry status for which the requested reported should reflect.
- *Credit Debit Indicator* is a choice of embedded code to indicate whether Debit or Credit transaction entries should be reported.

**Min 0 – Max 1**

An optional *Floor Limit* element may also be used. This element requests a minimum value, for which transaction entries above this value should be reported.

Where used the *Amount* and *Credit Debit Indicator* elements are mandatory.

![](_page_735_Picture_11.jpeg)

As a request for specific transaction type/s to be reported, typically this request would relate to a camt.052 Bank to Customer Account Report where the specified balance information is an intraday report. The use of the camt.060 Account Reporting Request and the ability to specify specific reporting requirements in the request is dependent on the Account Servicing Institution and should bilaterally agreed by Account Owner

The Account Reporting Request message *Requested Balance Type* provides the ability to identify the specific type of balances the request wishes to be reported.

![](_page_736_Picture_2.jpeg)

**Min 1 – Max 1**

Where used a choice of balance *Code* is mandatory which may either use a choice of external ISO Balance Type code or a proprietary code.

**Min 0 – Max 1**

An optional *Sub Type* element may also be used which a choice of external ISO Balance Sub Type code or a proprietary code.

![](_page_736_Picture_7.jpeg)

As a request for specific balance type/s (or sub balance type/s) to be reported, typically this request would relate to a camt.052 Bank to Customer Account Report where the specified balance information is an intraday report. The use of the camt.060 Account Reporting Request and the ability to specify specific reporting requirements in the request is dependent on the Account Servicing Institution and should bilaterally agreed by Account Owner with them.

Use case should be considered as a principal example whereby use case may be cross referenced

#### **Financial Institution Account Reporting Request**

Use Case c.60.1.1 – High Level Financial Institution daily Account Reporting Request Use Case c.60.1.2 – Financial Institution interim Account Reporting Request

![](_page_738_Figure_0.jpeg)

Payment Market Infrastructure, settles the payment between Agent B and Agent C as direct participants of the Market Infrastructure, and provides a settlement confirmation to Agent B

Agent D requests a daily statement using a camt.060 (not having an automatic statement produced by their account servicing institution

Agent B processes the payment on Agent C, via the Payment Market Infrastructure

Agent C credits the account of the Creditor (Agent D)

Agent C produces a customer statement (camt.053) following the request from Agent D

![](_page_739_Figure_0.jpeg)

Payment Market Infrastructure, settles the payment between Agent B and Agent C as direct participants of the Market Infrastructure, and provides a settlement confirmation to Agent B

Agent D requests an interim statement using a camt.060 (not having an automatic interim statement produced by their account servicing institution

Agent B processes the payment on Agent C, via the Payment Market Infrastructure

Agent C credits the account of the Creditor (Agent D)

Agent C produces a customer statement (camt.052) following the request from Agent D

## **Cash Management Exception & Investigation (camt) messages**

![](_page_741_Picture_0.jpeg)

<span id="page-741-0"></span>**camt.029 –** [Resolution of Investigation](#page-742-0)

**camt.055 –** [Customer Payment Cancellation Request](#page-772-0)

**camt.056** – [FI to FI Payment Cancellation Request](#page-794-0)

## <span id="page-742-0"></span>**Resolution of Investigation**

![](_page_743_Picture_0.jpeg)

The Resolution of Investigation message is sent by an Agent to respond to the Cancellation Request, either directly or serially through other agents.

The message is used to provide:

- final outcome of the case, whether positive or negative, or
- an interim update prior to the final outcome.

![](_page_743_Picture_5.jpeg)

Following a positive acceptance of the Cancellation request. The appropriate payment message (pacs.002 or pacs.004) is used to reject or return a previously received payment.

![](_page_744_Figure_0.jpeg)

The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any payment previous settled is necessary to trigger reversing account postings.

![](_page_745_Figure_0.jpeg)

The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any payment previous settled is necessary to trigger reversing account postings.

The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview.

![](_page_746_Figure_1.jpeg)

Camt.056 Payment Cancellation Request **ISO**

![](_page_746_Picture_3.jpeg)

![](_page_746_Picture_4.jpeg)

**ISO** camt.029 Resolution of Investigation

| Assignment<br>Identification   | Unique Id<br>generated by the assigner<br>to identify the Payment Cancellation<br>Request message                                 | CASE123/1 |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------|
| Cancellation<br>identification | Optional Cancellation<br>Id of the Agent<br>sending (assigner) the Payment<br>Cancellation Request message.                       | CASE123   |
| Case<br>Identification         | Case<br>Id of the Agent sending<br>(assigner) the Payment Cancellation<br>Request message.                                        | CASE123   |
| Case<br>Creator                | Party w ho created<br>the original<br>cancellation<br>request (w hich may be<br>another Agent other than the current<br>Assigner. |           |

| element                        | description                                                                                                                       | example    |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------|
| Assigner                       | Sender of the camt.056                                                                                                            | Agent<br>B |
| Assignee                       | Receiver of the camt.056                                                                                                          | Agent C    |
| Assignment<br>Identification   | Unique Id<br>generated by the assigner<br>to identify the Payment Cancellation<br>Request message                                 | CASE123/1  |
| Cancellation<br>identification | Optional Cancellation<br>Id of the Agent<br>sending (assigner) the Payment<br>Cancellation Request message.                       | CASE123    |
| Case<br>Identification         | Case<br>Id of the Agent sending<br>(assigner) the Payment Cancellation<br>Request message.                                        | CASE123    |
| Case<br>Creator                | Party w ho created<br>the original<br>cancellation<br>request (w hich may be<br>another Agent other than the current<br>Assigner. | Agent A    |

![](_page_747_Picture_0.jpeg)

The Payment Cancellation Request message *Identification* provides a mandatory element to identify the Request

![](_page_748_Picture_2.jpeg)

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.

For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.

Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

![](_page_749_Figure_0.jpeg)

![](_page_750_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_750_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

![](_page_751_Picture_0.jpeg)

The Resolution of Investigation *Confirmation* provides a mandatory element to specify the status of the Payment Cancellation Request's investigation.

![](_page_752_Picture_2.jpeg)

![](_page_752_Picture_3.jpeg)

- *CNCL* The payment has been cancelled as requested. This status concludes the investigation, whereby aPayment Return may follow if funds need to be returned.
- *PDCR* The Investigation of the Payment Cancellation Request is pending i.e. is under ongoing investigation to provide a final status confirmation. An addition *Cancellation Status Reason Information* should be provided to further clarify the current status. For example, a Status Reason code RQDA can be used to indicate debit authority has been requested from the Creditor.
- *RJCR* The Payment Cancellation Request is rejected. A status concluding the investigation which must include additional *Cancellation Status Reason Information* to provide an explanation as to why the request was rejected.

## **Cancellation Details**

The Resolution of Investigation *Transaction Information and Status* is a mandatory nested element to capture information related to the original payment and to provide further information on the status reason Payment Cancellation Request's investigation.

![](_page_754_Picture_2.jpeg)

As part of this nested element, information is captured to reference; the case the investigation is attempting to resolve, various original references related to the original payment and the investigation status information.

The Resolution of Investigation message *Cancellation Status Identification* provides a mandatory element to identify the status update.

![](_page_755_Picture_2.jpeg)

Unique reference assigned by the resolution assigner to unambiguously identify the Cancellation status.

For Exceptions and Investigations messages the *Cancellation Status Identification* can be considered an equivalent in the legacy MT Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

The Resolution of Investigation message *Resolved Case* provides a mandatory nested element to identify the Resolved Case *Identification* and the *Creator* of the case.

![](_page_756_Picture_2.jpeg)

#### **Min 1 – Max 1**

The *Identification* element captures the unique case reference assigned by the Payment Cancellation Request Assigner to unambiguously identify the Cancellation investigation case being resolved.

For Exceptions and Investigations messages this *Case Identification* can be considered an equivalent of the *Related Reference* (Field 21) of the legacy MT Answer message.

#### **Min 1 – Max 1**

The *Creator* element captures the party who created the Payment Cancellation Request investigation (see [camt.056](#page-805-0) Case Creator).

This mandatory party can represent as either an *Agent* i.e., the Bank who created the case or as a *Party* i.e., the customer (for example the Debtor) who created the request. This element has no equivalent in the legacy MT Request for Cancellation message.

The Resolution of Investigation uses elements in the *Original Group Information* to capture the message identifier and message name of the underlying payment for which the investigation relates to. The mandatory *Original Message Identification* contains the point-to-point reference from this payment, and the mandatory *Original Message Name Identification* contains the message name of the underlying payment. **Min 1 – Max 1**

Optionally the *Original Creation Date Time* can also be captured.

## **<sup>A</sup> <sup>B</sup>** For example:

*Original Message Name Identification* "pacs.008.001.08" confirms the investigation relates to a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as "pacs.009.001.08" confirms the investigation relates to a pacs.009 Financial Institution Credit Transfer.

Original Group

Assignment

Cancellatio n Details

Original Message Identification abcd1234 Identification xyz9875

pacs.008.001.**<sup>08</sup>** Original Message

**camt.029**

**camt.056**

Identification abcd1234

**pacs.008**

Message

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message The Resolution of Investigation also uses a number of other **Original** elements in the *Transaction Information* to capture information from the underlying payment that the Cancellation request relates to.

![](_page_758_Picture_1.jpeg)

The Original elements enables the *Assignee* to identify the Payment which is being request to be cancelled. The following element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) are mandated:

*Original UETR*

**Min 1 – Max 1**

The following element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) are optional:

*Original End to End Identification Original Instruction Identification Original Transaction Identification Original Clearing System Reference*

**Min 0 – Max 1**

**Min 0 – Max 1**

**Min 0 – Max 1**

**Min 0 – Max 1**

![](_page_758_Figure_11.jpeg)

The Resolution of Investigation *Cancellation Status Reason Information* nested element captures the information related to the status reason of the Cancellation Resolution.

![](_page_759_Picture_2.jpeg)

the *Originator* element helps identify the party who provided the Cancellation status. This party would have been included in the underlying payment and is also included the pacs.004 *Return Chain.* **Min 0 – Max 1**

![](_page_759_Picture_4.jpeg)

the *Reason* for the Cancellation status, which is mandatory where the Resolution Status is RJCR, is represented by an embedded CBPR+ Cancellation *Code* choice ( )

![](_page_759_Picture_6.jpeg)

**Min 0 – Max 1**

the *Additional Information* element may also be included to provide further details on the Cancellation reason.

![](_page_759_Picture_9.jpeg)

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

![](_page_759_Picture_11.jpeg)

In the event that an **indemnity agreement** is need to be established, *Original Group Information* **INDM** should be indicated at the beginning of the Additional Information element. Any subsequent additional information may then

![](_page_759_Picture_13.jpeg)

The Resolution of Investigation *Reason* element is optional. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded *Code* choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened afterthe coexistence period.

| Code | Name                     | Definition                                                                                         | Use Case                                                                                                                                                                                              |
|------|--------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC04 | Closed Account<br>Number | Account number specified has been<br>closed on the receiver's books.                               | Complimenting a Reject<br>Status. Payment Cancellation Request can not be<br>accepted as the Creditor has since closed their account.                                                                 |
| AGNT | Agent Decision           | Reported when the cancellation<br>cannot be accepted because of an<br>agent refuses to cancel.     | Complimenting a Reject<br>Status. Payment Cancellation Request can not be<br>accepted as an Agent in the payment transaction<br>does not accept the<br>request.                                       |
| AM04 | Insufficient Funds       | Amount of funds available to cover<br>specified message amount is<br>insufficient.                 | Complimenting a Reject<br>Status. Payment Cancellation Request can not be<br>accepted as the Creditor has insufficient funds to perform the return payment.                                           |
| ARDT | Already Returned         | Cancellation not accepted as the<br>transaction has already been returned.                         | Complimenting a Reject<br>Status. Payment Cancellation Request can not be<br>accepted as the payment has already return payment.                                                                      |
| CUST | Customer Decision        | Reported when the cancellation<br>cannot be accepted because of a<br>customer decision (Creditor). | Complimenting a Reject<br>Status. Payment Cancellation Request can not be<br>accepted as the Creditor does not provide<br>authority to return the payment. i.e.<br>believe the payment was justified. |
| INDM | Indemnity Request        | Indemnity is required before funds can<br>be returned                                              | Complimenting a Pending<br>or Reject<br>Status. Payment Cancellation Request<br>can not be accepted until an<br>indemnity agreement is established.                                                   |

| LEGL | Legal Decision                         | Reported when the cancellation cannot be<br>accepted because of regulatory rules.                                                  |                                                                                                                                                                                                                                                                                  |
|------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAAR | Narrative                              | Reason is provided as narrative information in the<br>additional reason information.                                               | Complimenting a Reject<br>or Pending<br>Status<br>to provide further<br>narrative Additional Information.                                                                                                                                                                        |
| NOAS | No Answer From<br>Customer             | No response from beneficiary (to the cancellation<br>request).                                                                     | Complimenting a Reject<br>Status. Payment Cancellation Request<br>can not be accepted as the Creditor has not responded to a<br>Debit Authority request to return the payment.                                                                                                   |
| NOOR | No Original<br>Transaction<br>Received | Original transaction (subject to cancellation) never<br>received.                                                                  | Complimenting a Reject<br>Status. Payment Cancellation Request<br>can not be accepted as it is believed that the original payment<br>was<br>never received for the UETR and references provided.                                                                                 |
| PTNA | Passed To The<br>Next Agent            | Reported when the cancellation request cannot be<br>accepted because the payment instruction has been<br>passed to the next agent. | Complimenting a Pending<br>Status. Payment has been onward<br>processed to the next agent in the transaction. The Payment<br>Cancellation Request has therefore been forward to this Agent,<br>a further resolution message will be sent once this Agent<br>provides a response. |
| RQDA | Requesting Debit<br>Authority          | Reported when authority is required by the Creditor to<br>return the payment.                                                      | Complimenting a Pending<br>Status. Payment has been credited<br>to the creditor, Authority to Debit the Creditor and return the<br>payment is being request. A further resolution message will be<br>sent once the Creditor provides a response.                                 |

<span id="page-762-0"></span>Use case should be considered as a principal example whereby use case may be cross referenced

#### **Resolution of Investigation**

Use Case c.29.1.1 – High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008)

Use Case c.29.1.1.a – High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.29.1.2 – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008)

Use Case c.29.1.2.a – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.29.2.1 – High Level Resolution of Investigation (camt.029) of a complete Customer Credit Transfers (pacs.008) settled using the cover method

Use Case c.29.2.2 – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.29.2.3 – High Level Resolution of Investigation (camt.029) of a Customer Credit Transfers (pacs.008) where the cover is returned

Use Case c.29.3.1 – High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer (pacs.009)

Use Case c.29.4.1 – High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer advice (pacs.009 adv)

### Transfer (pacs.008)

![](_page_763_Figure_1.jpeg)

Agent D provides a final outcome of the investigation to Agent C using the camt.029.

Debtor Agent (B) updates their case history and relays the outcome of the investigation to Agent A using the camt.029 See use case p.8.1.1 for the original payment, c.56.1.1 for case resolution and p.4.1.3. for an example payment return

Debtor Agent (C) updates their case history and relays the outcome of the investigation to Agent B using the camt.029

Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

## Transfer (pacs.008) using gpi Stop and Recall

![](_page_764_Figure_1.jpeg)

Agent D provides an update on the investigation to the gpi Tracker using the camt.029.

Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

gpi Tracker forwards the response to Agent A as the initiator of the original camt.056

## **Credit Transfer (pacs.008)**

![](_page_765_Figure_1.jpeg)

Agent C provides a final outcome of the investigation to Agent B using the camt.029

Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

![](_page_765_Figure_4.jpeg)

Debtor Agent (B) updates their case history and relays the outcome of the investigation to

## **Credit Transfer (pacs.008) using gpi Stop and Recall**

![](_page_766_Figure_1.jpeg)

3

![](_page_766_Picture_2.jpeg)

![](_page_766_Picture_3.jpeg)

Agent C provides an update on the investigation to the gpi Tracker using the camt.029. 1

Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

gpi Tracker forwards the response to Agent A as the initiator of the original camt.056 2

## **Transfer (pacs.008) settled using a cover method**

![](_page_767_Figure_1.jpeg)

## **Credit Transfer (pacs.008) settled using a cover method.**

![](_page_768_Figure_1.jpeg)

![](_page_769_Figure_0.jpeg)

## **Credit Transfer (pacs.009)**

![](_page_770_Figure_1.jpeg)

![](_page_770_Figure_2.jpeg)

See use case p.9.1.1 for the cover payment sample c.56.3.1 for case resolution and p.4.2.3 for payment return

Agent C provides a final outcome of the investigation to Agent B using the camt.029. 1

Debtor Agent (B) updates their case history and informs the customer (Agent A) of the outcome of the investigation. 2

![](_page_771_Figure_0.jpeg)

## <span id="page-772-0"></span>**Customer Payment Cancellation Request**

![](_page_773_Picture_0.jpeg)

The Customer Payment Cancellation Request message is sent by an Agent to request the Cancellation of a payment initiation request previous sent.

The message is sent either:

• directly to the Agent a previous Payment initiation request was sent to.

![](_page_774_Figure_0.jpeg)

The CustomerPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The

## Initiation" Initiating Debtor Creditor Debtor Agent Creditor Agent Party Interbank pain.001 Interbank pain.002 pacs.008 camt.055 pacs.002 camt.053 camt.029 camt.056 camt.029

The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The

![](_page_776_Figure_0.jpeg)

The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview.

![](_page_777_Figure_1.jpeg)

![](_page_777_Picture_2.jpeg)

| Assignment<br>Identification   | Unique Id<br>generated by the assigner<br>to identify the Payment Cancellation<br>Request message                                 | CASE123/1 |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------|
| Cancellation<br>identification | Optional Cancellation<br>Id of the Agent<br>sending (assigner) the Payment<br>Cancellation Request message.                       | CASE123   |
| Case<br>Identification         | Case<br>Id of the Agent sending<br>(assigner) the Payment Cancellation<br>Request message.                                        | CASE123   |
| Case<br>Creator                | Party w ho created<br>the original<br>cancellation<br>request (w hich may be<br>another Agent other than the current<br>Assigner. |           |

![](_page_777_Picture_4.jpeg)

| element                        | description                                                                                                                       | example    |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------|
| Assigner                       | Sender of the camt.055                                                                                                            | Agent<br>A |
| Assignee                       | Receiver of the camt.055                                                                                                          | Agent B    |
| Assignment<br>Identification   | Unique Id<br>generated by the assigner<br>to identify the Payment Cancellation<br>Request message                                 | CASE123/1  |
| Cancellation<br>identification | Optional Cancellation<br>Id of the Agent<br>sending (assigner) the Payment<br>Cancellation Request message.                       | CASE123    |
| Case<br>Identification         | Case<br>Id of the Agent sending<br>(assigner) the Payment Cancellation<br>Request message.                                        | CASE123    |
| Case<br>Creator                | Party w ho created<br>the original<br>cancellation<br>request (w hich may be<br>another Agent other than the current<br>Assigner. | Agent A    |

![](_page_778_Picture_0.jpeg)

The Payment Cancellation Request message *Identification* provides a mandatory element to identify the Request

![](_page_779_Picture_2.jpeg)

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.

For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.

Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

<span id="page-780-0"></span>![](_page_780_Figure_0.jpeg)

![](_page_781_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_781_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

# Information and Cancellation.

## **Identification**

The Payment Cancellation Request message *Original Payment Information Identification* provides a **Min 1 – Max 1**

mandatory element to identify the Original Payment Initiation Request

This Unique reference identifies the Payment Information Identification from the originalPayment Initiation request.

Refer to the relevant Payment Information Identification element in the original message for details on that reference.

Link to Pain.001 Link to Pain.008

![](_page_783_Figure_6.jpeg)

The Payment Cancellation Request uses elements in the *Original Group Information* to capture the message identifier and message name of the underlying payment for which the Cancellation is being requested. The mandatory *Original Message Identification* contains the point-to-point reference from this payment, and the mandatory *Original Message Name Identification* contains the message name of the underlying payment. Optionally the *Original Creation Date Time* can also be captured. **Min 1 – Max 1**

### For example:

*Original Message Name Identification* "pain.001.001.09" confirms the Cancellation request is for a pain.001 Interbank Customer Credit Transfer Initiation.

![](_page_784_Figure_3.jpeg)

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message The Payment Cancellation Request message *Cancelation Identification* provides an optional element to identify the Request

![](_page_785_Picture_2.jpeg)

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.

For Exceptions and Investigations messages the *Cancellation Identification* can be considered an equivalent in the legacy MT Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

The Payment Cancellation Request message *Case* provides a mandatory nested element to identify the Case *Identification* and the *Creator* of the case.

![](_page_786_Picture_2.jpeg)

#### **Min 1 – Max 1**

The *Identification* element captures a unique case reference assigned by the assigner to unambiguously identify the Cancellation investigation case.

For Exceptions and Investigations messages the *Case Identification* can be considered an equivalent of the *Transaction Reference Number* (Field 20) of the legacy MT Request for Cancellation message.

#### **Min 1 – Max 1**

The *Creator* element captures the party who created the investigation. This mandatory party can represent as either an *Agent* i.e., the Bank who created the case or as a *Party* i.e., the customer (for example the Debtor) who created the request. In CBPR+ the creatoris always expected to be an Agent.

This element has no equivalent in the legacy MT Request for Cancellation message.

The Payment Cancellation Request also uses a number of other **Original** elements in the *Transaction Information* to capture information from the underlying payment that the Cancellation request relates to.

> The Original elements enables the *Assignee* to identify the Payment which is being request to be cancelled. The following element (in addition to *Original Message identification* and *Original Message Name Identification*) are mandated:

![](_page_787_Picture_2.jpeg)

*Original End to End Identification Original UETR Original Instructed Amount* **Min 1 – Max 1 Min 1 – Max 1 Min 1 – Max 1**

One of the following elements is also required depending on the Date element in the original message, where Original Request Execution Date relates to the pain.001 and Original Request Collection Date relates to the pain.008 :

> **Min 0 – Max 1 Min 0 – Max 1**

*Original Requested Execution Date Original Request Collection Date*

*Original Instructed Amount* The following element is optional:

*Original Instruction Identification Original End to End Identification Original UETR Transaction Information Underlying Original Payment Information and Cancellation*

*Original Requested Execution Date*

The Payment Cancellation Request *Cancellation Reason Information* nested element captures information associated with the reason for the Cancellation request.

![](_page_788_Picture_2.jpeg)

**Min 0 – Max 1**

the *Originator* element helps identify the party who request the payment Cancellation. This party would have been included in the underlying payment and is also included the pacs.004 *Return Chain as the Creditor.*

![](_page_788_Picture_5.jpeg)

the *Reason* is mandatory and represented by an embedded CBPR+ Cancellation *Code* choice ( )

![](_page_788_Picture_7.jpeg)

the *Additional Information* element may also be included to provide further details on the Cancellation reason.

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

![](_page_788_Picture_11.jpeg)

The Payment Cancellation Request *Reason* element is mandatory. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded *Code* choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened afterthe coexistence period.

| Code | Name                     | Definition                                      | Use Case                                                                                                                                                                                                                                                                                                                       |
|------|--------------------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AGNT | Incorrect Agent          | Agent in the payment workflow is<br>incorrect.  | A payment previous executed is identified as containing an incorrect<br>correspondent (Agent) within the<br>payment flow. A Cancellation request is<br>generated so that the payment can be remediated following<br>the successful<br>return.                                                                                  |
| AM09 | Wrong Amount             | Amount is not the amount agreed or<br>expected. | The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently realizes they had provided an incorrect amount.                                                                                                                                                                        |
| CURR | Incorrect<br>Currency    | Currency of the payment is incorrect.           | The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently realizes<br>they requested the wrong currency, as the<br>payment has been executed. They request their bank to recall<br>the funds so that the payment can be re-executed in the correct currency                      |
| CUST | Requested By<br>Customer | Cancellation requested by the Debtor.           | The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently wishes<br>to recall the payment. The exactly<br>underlying reason for the customer request is either not specified by the<br>customer or is not aligned to a more specific reason and therefore is not<br>appropriate. |

## **(continued)**

| Code | Name                           | Definition                                                                                                                                                        | Use Case                                                                                                                                                                                                                                                                                     |
|------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CUTA | Cancel Upon<br>Unable To Apply | Cancellation requested because an investigation<br>request has been received and no remediation is<br>possible.                                                   | An error occurred in the original payment (such as incorrect<br>information) which was highlighted as part of an Investigation<br>query. The request to cancel complements a response to the<br>Investigation.                                                                               |
| DUPL | Duplicate<br>Payment           | Payment is a duplicate of another payment.                                                                                                                        | A customer (Debtor) requests the initiation of a payment from<br>their bank account, but subsequently initiates<br>a new (separate) payment request in duplication of a previous<br>payment. Having realized the error, the<br>customer requests the<br>recall of the duplicate transaction. |
| FRAD | Fraudulent Origin              | Cancellation requested following a transaction that was<br>originated fraudulently. The use of the Fraudulent<br>Origin code should be governed by jurisdictions. | Either the customer (Debtor) or a bank (Agent) in the payment<br>transaction experiences an activity which causes a payment to<br>be executed by alleged fraudulent means.                                                                                                                   |
| NARR | Narrative                      | Narrative reason<br>provided in the Additional Information.                                                                                                       | Used only<br>where a more specific reason is not appropriate.<br>Narrative description is provided.                                                                                                                                                                                          |
| TECH | Technical<br>Problem           | Cancellation requested following technical problems<br>resulting in an erroneous transaction.                                                                     | Either the customer (Debtor) or a bank (Agent) in the payment<br>flow experiences a technology issue which causes<br>data within<br>a payment to be incorrect.                                                                                                                               |
| UPAY | Undue Payment                  | Payment is not justified.                                                                                                                                         | Either the customer (Debtor) or a bank (Agent) in the payment<br>flow experiences an activity which causes a<br>payment to be executed under unexpected circumstances.                                                                                                                       |

Use case should be considered as a principal example whereby use case may be cross referenced

#### **Payment Cancellation Request**

Use Case c.55.1.1 –

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collections of funds from the debtor's accounts for a creditor.

![](_page_792_Figure_1.jpeg)

## **Payment Market Infrastructure**

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collection of funds from the debtor's accounts for a creditor (through a Payment Market Infrastructure).

![](_page_793_Figure_2.jpeg)

<span id="page-794-0"></span>**Financial Institution to Financial Institution Payment Cancellation Request**

![](_page_795_Picture_0.jpeg)

The FI to FI Payment Cancellation Request message is sent by an Agent to request the Cancellation of a payment previous sent.

The message is sent either:

- directly (through the SWIFT Community CASE solution), or
- serially through other agents.

![](_page_795_Figure_5.jpeg)

It is not recommended to request a Payment Cancellation Request (camt.056) of a Payment Return (pacs.004) instead an Exception and Investigation should be initiated to resolve this

![](_page_796_Figure_0.jpeg)

The FIToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The FIToFIPaymentCancellationRequest message is exchanged between the payment Instructing Agent and the Instructed

![](_page_797_Figure_0.jpeg)

The FIToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The FIToFIPaymentCancellationRequest message is exchanged between the payment Instructing Agent and the Instructed

The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview.

![](_page_798_Figure_1.jpeg)

Camt.056 Payment Cancellation Request **ISO**

![](_page_798_Picture_3.jpeg)

![](_page_798_Picture_4.jpeg)

**ISO** camt.029 Resolution of Investigation

|  | Assignment<br>Identification   | Unique Id<br>generated by the assigner<br>to identify the Payment Cancellation<br>Request message                                 | CASE123/1 |
|--|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------|
|  | Cancellation<br>identification | Optional Cancellation<br>Id of the Agent<br>sending (assigner) the Payment<br>Cancellation Request message.                       | CASE123   |
|  | Case<br>Identification         | Case<br>Id of the Agent sending<br>(assigner) the Payment Cancellation<br>Request message.                                        | CASE123   |
|  | Case<br>Creator                | Party w ho created<br>the original<br>cancellation<br>request (w hich may be<br>another Agent other than the current<br>Assigner. |           |

![](_page_798_Picture_7.jpeg)

![](_page_799_Picture_0.jpeg)

The Payment Cancellation Request message *Identification* provides a mandatory element to identify the Request

![](_page_800_Picture_2.jpeg)

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.

For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.

Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

![](_page_801_Figure_0.jpeg)

![](_page_802_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_802_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

## Onderrying – Fransaction information

The Payment Cancellation Request message *Cancellation Identification* provides an optional element to identify the Request

![](_page_804_Picture_2.jpeg)

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.

For Exceptions and Investigations messages the *Cancellation Identification* can be considered an equivalent in the legacy MT Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

![](_page_804_Picture_5.jpeg)

Where Cancellation Identification is used this should represent the reference value as the Case Identification

<span id="page-805-0"></span>The Payment Cancellation Request message *Case* provides a mandatory nested element to identify the Case *Identification* and the *Creator* of the case.

![](_page_805_Picture_2.jpeg)

#### **Min 1 – Max 1**

The *Identification* element captures a unique case reference assigned by the assigner to unambiguously identify the Cancellation investigation case.

For Exceptions and Investigations messages the *Case Identification* can be considered an equivalent of the *Transaction Reference Number* (Field 20) of the legacy MT Request for Cancellation message.

#### **Min 1 – Max 1**

The *Creator* element captures the party who created the investigation. This mandatory party can represent as either an *Agent* i.e., the Bank who created the case or as a *Party* i.e., the customer (for example the Debtor) who created the request. In CBPR+ the creatoris always expected to be an Agent.

This element has no equivalent in the legacy MT Request for Cancellation message.

![](_page_805_Picture_10.jpeg)

The Payment Cancellation Request uses elements in the *Original Group Information* to capture the message identifier and message name of the underlying payment for which the Cancellation is being requested. The mandatory *Original Message Identification* contains the point-to-point reference from this payment, and the mandatory *Original Message Name Identification* contains the message name of the underlying payment. Optionally the *Original Creation Date Time* can also be captured. **Min 1 – Max 1**

## **<sup>A</sup> <sup>B</sup>** For example:

*Original Message Name Identification* "pacs.008.001.08" confirms the Cancellation request is for a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as "pacs.009.001.08" confirms the Cancellation request for a pacs.009 Financial Institution Credit Transfer.

**camt.056** Message Identification abcd1234 pacs.008.001.**<sup>08</sup>** Original Message Original Message Identification abcd1234 Identification xyz9875 Original Group Assignment **pacs.008** Underlying **camt.029**

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message The Payment Cancellation Request also uses a number of other **Original** elements in the *Transaction Information* to capture information from the underlying payment that the Cancellation request relates to.

> The Original elements enables the *Assignee* to identify the Payment which is being request to be cancelled. The following element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) are mandated:

![](_page_807_Picture_2.jpeg)

**Min 1 – Max 1 Min 1 – Max 1 Min 1 – Max 1 Min 1 – Max 1** *Original End to End Identification Original UETR Original Interbank Settlement Amount Original Interbank Settlement Date*

The following element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) are optional:

*Original Instruction Identification Original Transaction Identification Original Clearing System Reference*

![](_page_807_Picture_6.jpeg)

The Payment Cancellation Request *Cancellation Reason Information* nested element captures information associated with the reason for the Cancellation request.

**Min 0 – Max 1**

![](_page_808_Picture_3.jpeg)

the *Originator* element helps identify the party who request the payment Cancellation. This party would have been included in the underlying payment and is also included the pacs.004 *Return Chain as the Creditor.*

**Min 1 – Max 1**

the *Reason* is mandatory and represented by an embedded CBPR+ Cancellation *Code* choice ( )

**Min 0 – Max 2**

![](_page_808_Picture_8.jpeg)

the *Additional Information* element may also be included to provide further details on the Cancellation reason.

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

![](_page_808_Picture_11.jpeg)

*Underlying Transaction Information Cancellation Reason Info'* 

![](_page_808_Picture_13.jpeg)

The Payment Cancellation Request *Reason* element is mandatory. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded *Code* choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened afterthe coexistence period.

| Code | Name                           | Definition                                               | Use Case                                                                                                                                                                                                                                                                                                       |
|------|--------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AGNT | Incorrect Agent                | Agent in the payment workflow is<br>incorrect.           | A payment previous executed is identified as containing an incorrect<br>correspondent (Agent) within the<br>payment flow. A Cancellation request is<br>generated so that the payment can be remediated following<br>the successful<br>return.                                                                  |
| AM09 | Wrong Amount                   | Amount is not the amount agreed or<br>expected.          | The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently realizes they had provided an incorrect amount.                                                                                                                                                        |
| COVR | Cover Cancelled<br>Or Returned | Cover payments has either been<br>returned or cancelled. | Identifies an Agent to request the Cancellation of<br>a pacs message where<br>settlement method was COVE and the covering payment has been cancelled<br>or returned.                                                                                                                                           |
| CURR | Incorrect<br>Currency          | Currency of the payment is incorrect.                    | The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently realizes<br>they requested the wrong currency, as the<br>payment has been executed. They request their bank to recall<br>the funds so that the payment can be re-executed in the correct currency      |
| CUST | Requested By<br>Customer       | Cancellation requested by the Debtor.                    | The customer (Debtor) requests the initiation of a payment from their bank<br>account, but subsequently wishes<br>to recall the payment. The exactly<br>underlying reason for the customer request is either not specified by the<br>customer or is not aligned to a more specific reason and therefore is not |

## **(continued)**

| Code | Name                           | Definition                                                                                                                                                        | Use Case                                                                                                                                                                                                                                                                                     |
|------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CUTA | Cancel Upon<br>Unable To Apply | Cancellation requested because an investigation<br>request has been received and no remediation is<br>possible.                                                   | An error occurred in the original payment (such as incorrect<br>information) which was highlighted as part of an Investigation<br>query. The request to cancel complements a response to the<br>Investigation.                                                                               |
| DUPL | Duplicate<br>Payment           | Payment is a duplicate of another payment.                                                                                                                        | A customer (Debtor) requests the initiation of a payment from<br>their bank account, but subsequently initiates<br>a new (separate) payment request in duplication of a previous<br>payment. Having realized the error, the<br>customer requests the<br>recall of the duplicate transaction. |
| FRAD | Fraudulent Origin              | Cancellation requested following a transaction that was<br>originated fraudulently. The use of the Fraudulent<br>Origin code should be governed by jurisdictions. | Either the customer (Debtor) or a bank (Agent) in the payment<br>transaction experiences an activity which causes a payment to<br>be executed by alleged fraudulent means.                                                                                                                   |
| NARR | Narrative                      | Narrative reason<br>provided in the Additional Information.                                                                                                       | Used only<br>where a more specific reason is not appropriate.<br>Narrative description is provided.                                                                                                                                                                                          |
| TECH | Technical<br>Problem           | Cancellation requested following technical problems<br>resulting in an erroneous transaction.                                                                     | Either the customer (Debtor) or a bank (Agent) in the payment<br>flow experiences a technology issue which causes<br>data within<br>a payment to be incorrect.                                                                                                                               |
| UPAY | Undue Payment                  | Payment is not justified.                                                                                                                                         | Either the customer (Debtor) or a bank (Agent) in the payment<br>flow experiences an activity which causes a<br>payment to be executed under unexpected circumstances.                                                                                                                       |

Use case should be considered as a principal example whereby use case may be cross referenced

#### **Payment Cancellation Request**

Use Case c.56.1.1 – High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008) Use Case c.56.1.1.a – High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.56.1.2 – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008)

Use Case c.56.1.2.a – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.56.2.1 – High Level Payment Cancellation Request (camt.056) of a complete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.56.2.2 – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.56.2.3 – High Level Payment Cancellation Request (camt.056) of a Customer Credit Transfers (pacs.008) where the cover is returned

Use Case c.56.3.1 – High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer (pacs.009)

Use Case c.56.4.1 – High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer advice (pacs.009 adv)

### **Credit Transfer (pacs.008)**

![](_page_812_Figure_1.jpeg)

- Debtor request their bank to recall a previous instructed payment, as the amount was incorrect
- Debtor Agent (A) assigns a
  Cancellation Request to Agent
  B (assignee) requesting the

- Agent B creates an investigation case.
  Recognising the payment has already been onward processed. They update Agent A and assign a Cancellation Request directly to Agent C.
- Agent C creates an investigation case.
  Recognising the payment has already been onward processed. They update

Agent D creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, providing the reason specified for the return request and updates Agent C.

Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed any necessary return payment is arrange.

## Credit Transfer (pacs.008) using gpi Stop and Recall

![](_page_813_Figure_1.jpeg)

### **Credit Transfer (pacs.008)**

See use case <u>p.8.1.1</u> for the original payment, c.29.1.2 for case resolution and p.4.1.3. for an example payment return

![](_page_814_Picture_2.jpeg)

![](_page_814_Picture_3.jpeg)

![](_page_814_Picture_4.jpeg)

- Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.
- Debtor Agent (A) assigns a
  Cancellation Request to Agent
  B (assignee) requesting the

Agent B creates an investigation case.
Recognising the payment has already been onward processed. They update Agent A and assign a Cancellation Request directly to Agent C.

Agent C creates an investigation case.
Recognising the payment has not been onward processed. They update Agent B that the Cancellation Request is accepted any necessary return payment is arrange.

## **Credit Transfer (pacs.008) using gpi Stop and Recall**

![](_page_815_Figure_1.jpeg)

![](_page_815_Picture_2.jpeg)

![](_page_815_Picture_3.jpeg)

Debtor request their bank to recall a previous instructed payment, as the amount was incorrect. 1

- gpi Tracker identifies the payment is incomplete and forwards a camt.056 to Agent C. 3 4
- Agent C creates an investigation case. Recognising the payment has not been onward processed. They updates the gpi Tracker any necessary return payment is arrange.

Debtor Agent (A) initiates a gpi Stop and Recall, requesting the original pacs.008 is returned, using reason code 2

## **Transfer (pacs.008) settled using a cover method.**

![](_page_816_Figure_1.jpeg)

## **Credit Transfer (pacs.008) settled using a cover method.**

![](_page_817_Figure_1.jpeg)

![](_page_818_Figure_0.jpeg)

## **Institution Credit Transfer (pacs.009)**

![](_page_819_Figure_1.jpeg)

Debtor request their bank to recall a previous instructed payment, as the amount was incorrect. 1

Debtor Agent (A) assigns a Cancellation Request to Agent C (assignee) requesting the original pacs.009 is returned, using reason code AM09. 2 3

Agent C creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, proving the reason specified for the return request and update Agent C.

Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed and any necessary return payment can be initiated.

![](_page_820_Figure_0.jpeg)

![](_page_821_Picture_0.jpeg)

<span id="page-821-0"></span>**camt.107 – [Cheque Presentment Notification](#page-822-0) camt.108 - [Cheque Cancellation or Stop Request](#page-842-0) camt.109 – [Cheque Cancellation or Stop Report](#page-862-0)**

## <span id="page-822-0"></span>**Cheque Presentment Notification**

![](_page_823_Picture_0.jpeg)

The ChequePresentmentNotificationmessage is sent by a drawer bank, or a bank acting on behalf of the drawer bank to the bank on which a cheque has been drawn (the drawee bank).

It is used to advise the drawee bank, or confirm to an enquiring bank, the details concerning the cheque referred to in the message.

![](_page_823_Picture_3.jpeg)

The Cheque Presentment Notification is restricted to a single cheque per InterAct message.

![](_page_824_Picture_0.jpeg)

The Agent A (drawer agent) sends a ChequePresentmentNotificationmessage to Agent B (the drawee agent). The ChequePresentmentNotificationmessage informs the drawee agent about the cheque submission. The notification message facilitates the drawee agent to follow up the cheque submission and relevant business process.

## **Group Header**

![](_page_826_Picture_0.jpeg)

Each ISO 20022 cash management message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Advice of Cheque message. However, the *Sender's Reference* (Field 20) could be considered a similar comparison.

![](_page_827_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_827_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

![](_page_828_Picture_0.jpeg)

The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1.

![](_page_829_Picture_0.jpeg)

#### Min 1 – Max 1

The Cheque Presentment Notification *Cheque* nested element specifies the details of the Cheque.

![](_page_830_Figure_2.jpeg)

This Cheque element has been restricted to one cheque occurrence.

#### **Min 1 – Max 1**

The Cheque Presentment Notification *Instruction Identification* provides an optional element to identify unambiguously the instruction

![](_page_831_Picture_2.jpeg)

Point to point reference that can be used between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

The Cheque Number Notification *Cheque Number* provides a mandatory element to identify unambiguously the Cheque.

![](_page_832_Picture_2.jpeg)

Unique and unambiguous number for a cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque

The Cheque Presentment Notification has several element to capture a Date related to the cheque.

![](_page_833_Picture_1.jpeg)

**Min 1 – Max 1**

The *Issue Date* is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer

![](_page_833_Picture_4.jpeg)

**Min 0 – Max 1**

The *Stale Date* is an optional element and represents the date after which a cheque is no longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days" or may be determined in accordance with domestic banking practice. Not all countries will have a validity period.

![](_page_834_Picture_0.jpeg)

<sup>A</sup> mandated currency **Amount** of the cheque to be paid to the payee. **£ \$ Min 1 – Max 1**

![](_page_834_Picture_2.jpeg)

**Min 0 – Max 1**

The *Value Date* is an optional element, it is used to capture the **Date**, where different to the **Issue Date**, i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account.

![](_page_834_Picture_5.jpeg)

![](_page_834_Picture_6.jpeg)

*Cheque*

The Cheque Presentment Notification *Payer* captures the party that instructs the Drawee Agent to issues a cheque to pay a specific amount, upon presentment, to the payee. The Payer sub-element describe the Payer in greater detail. **Min 1 – Max 1** *Country of Residence* Optional element to capture the Payee's ISO country code of residence *Identification* Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. *Postal Address* Nested element capturing either structured or unstructured *Payer* address details Mandatory *Name Name Payer*

The Cheque Presentment Notification *Payer Account* is used to capture the account of the party that instructs the Drawee Agent to issues a cheque to pay a specific amount, upon presentment, to the payee.

> The *Payer Account* uses a variety of nested elements to capture information related to the account.

![](_page_836_Picture_3.jpeg)

**Min 0 – Max 1**

**Min 0 – Max 1** *Identification* identifies the account maintained at the Drawer Agent (Account Servicing Institution)

*Type* uses the external CashAccount Type code list to identify the type of account **Min 0 – Max 1**

*Currency* identifies the currency of the account **Min 0 – Max 1**

*Name* identifies the name of the account as assigned by the Drawer Agent (Account Servicing Institution) **Min 0 – Max 1**

*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

#### **Min 0 – Max 1**

The Cheque Presentment Notification *Drawer Agent* optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification is sent to the *Drawee Agent*.

#### **Min 0 – Max 1**

The *Drawer Agent Account* optionally captures the Drawer Agent's Account with the *Drawee Agent*  and who would receive an order the pay the cheque upon presentment.

![](_page_837_Picture_4.jpeg)

![](_page_837_Picture_5.jpeg)

The Drawer Bank is typically identified on the cheque together with their Postal Address. The Drawer Agent's Account with the DraweeAgent is also often also identified on the cheque.

The Cheque Presentment Notification *Payee* captures the party that should receive an amount of money as specified in the cheque. The Payee sub-element describe the Payee in greater detail. **Min 1 – Max 1** *Postal Address* Nested element capturing either structured or unstructured *Payee* address details Mandatory *Name Name*

![](_page_838_Figure_1.jpeg)

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Serial Financial Institution to Financial Institution to Customer Credit Transfer**

Use Case c.107.1 – High Level Drawer Agent Cheque issuance to Payee, on their account with the Drawer Agent Use Case c.107.2 - High Level Drawer Agent Cheque issuance to Payee, on their head office's account with the Drawer Agent

![](_page_840_Figure_0.jpeg)

![](_page_841_Figure_0.jpeg)

## <span id="page-842-0"></span>**Cheque Cancellation or Stop Request**

![](_page_843_Picture_0.jpeg)

The Cheque Cancellation Or Stop Request message is sent by a drawer bank, or a bank acting on behalf of the drawer bank, to the agent on which a cheque has been drawn (the drawee bank) to request for the cancellation of the presentment and/or stop the payment of the cheque referred to in the message.

![](_page_843_Picture_2.jpeg)

The Cheque Cancelation or Stop Report is restricted to a single cheque per InterAct message.

![](_page_844_Figure_0.jpeg)

The Agent A (Drawer Agent) sends a ChequeCancelationOrStopRequest message to Agent B (the Drawee Agent). The ChequeCancelationOrStopReques message requests the drawee agent to place a stop (refusal to settle) upon presentment of the cheque, effectively canceling the issued cheque.

## **Group Header**

![](_page_846_Picture_0.jpeg)

Each ISO 20022 cash management message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Advice of Cheque message. However, the *Sender's Reference* (Field 20) could be considered a similar comparison.

![](_page_847_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_847_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

![](_page_848_Picture_0.jpeg)

The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1.

![](_page_849_Picture_0.jpeg)

#### **Min 1 – Max 1**

The Cheque Cancellation or Stop Request *Cheque* nested element specifies the details of the Cheque.

![](_page_850_Figure_2.jpeg)

This Cheque element has been restricted to one cheque occurrence.

#### **Min 0 – Max 1**

The Cheque Cancellation or Stop Request *Instruction Identification* provides an optional element to identify unambiguously the instruction

![](_page_851_Picture_2.jpeg)

Point to point reference that can be used between the Agent instructing the Cheque Cancellation or Stop Request and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

The Cheque Cancellation or Stop Request *Original Instruction Identification* provides an optional element to identify unambiguously the original instruction

![](_page_852_Picture_2.jpeg)

Point to point reference that can be used to identify the original Cheque Presentment Notification between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

The Cheque Cancellation or Stop Request *Cheque Number* provides a mandatory element to identify unambiguously the Cheque.

![](_page_853_Picture_2.jpeg)

Unique and unambiguous number for the cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque

The Cheque Cancellation or Stop Request has several element to capture a Date related to the cheque.

![](_page_854_Picture_1.jpeg)

**Min 1 – Max 1**

The *Issue Date* is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer

![](_page_854_Picture_4.jpeg)

**Min 0 – Max 1**

The *Stale Date* is an optional element and represents the date after which a cheque is no longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days" or may be determined in accordance with domestic banking practice. Not all countries will have a validity period.

![](_page_855_Picture_0.jpeg)

<sup>A</sup> mandated currency **Amount** of the cheque to be paid to the payee. **£ \$ Min 1 – Max 1**

![](_page_855_Picture_2.jpeg)

**Min 0 – Max 1** The *Effective Date* is an optional element, it is used to capture the original **Value Date** (as provided in the camt.107), where different to the original **Issue Date**, i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account.

![](_page_855_Picture_4.jpeg)

The Cheque Cancellation or Stop Request *Drawer Agent* optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification is sent to the *Drawee Agent.* 

The *Drawer Agent Account* optionally captures the Drawer Agent's Account with the *Drawee Agent*  and who would receive an order the pay the cheque upon presentment.

![](_page_856_Picture_3.jpeg)

![](_page_856_Picture_4.jpeg)

The Drawer Agent and Drawer Account elements where present should match that of the original camt.107 Cheque Presentment Notification.

![](_page_856_Picture_6.jpeg)

The Cheque Cancellation or Stop Request *Payee* captures the party that should receive an amount of money as specified in the cheque. The Payee sub-element describe the Payee in greater detail. **Min 0 – Max 1** Nested element capturing either

![](_page_857_Figure_1.jpeg)

Mandatory *Name Name*

The Cheque Cancellation or Stop Request *Cheque Cancellation or Stop Reason* nested element captures information associated with the reason for the Cheque Cancellation or Stop request.

**Min 0 – Max 1**

![](_page_858_Picture_3.jpeg)

the *Originator* element is a embedded code choice that helps identify the party who request the cheque cancellation or stop request. Where used this party would typically be the Payer (code **PAYR**) of the cheque.

**Min 1 – Max 1**

the *Reason* is mandatory and represented by an embedded CBPR+ Cancellation *Code* choice ( )

**Min 0 – Max 2**

![](_page_858_Picture_8.jpeg)

the *Additional Information* element may also be included to provide further details on the cancellation or stop reason.

![](_page_858_Picture_10.jpeg)

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cheque Cancellation or Stop request.

![](_page_858_Picture_12.jpeg)

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Serial Financial Institution to Financial Institution to Customer Credit Transfer**

Use Case c.108.1 – High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque Use Case c.108.2 – High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.

![](_page_860_Figure_0.jpeg)

Agent they wish to cancel or stop a previously issued cheque, as the Payee informs them the cheque has been lost.

cheque cancellation or stop request to the Drawee Agent with reason code LOST

Drawee Agent (B) match the request to the previous Cheque Presentment Notification (camt.107). As the cheque has not been presented the status record is identified as not to be paid if presented, as a result of a cancellation/stop request. This is reported back to the Drawer Agent

![](_page_861_Figure_0.jpeg)

## <span id="page-862-0"></span>**Cheque Cancellation or Stop Report**

![](_page_863_Picture_0.jpeg)

The Cheque Cancellation or Stop Report message is sent by the drawee agent (on which a cheque is drawn) to the drawer agent, or the agent acting on behalf of the drawer agent, to indicate what actions have been taken in attempting to cancel the presentment and/or stop the payment of the cheque referred to in the message.

![](_page_863_Picture_2.jpeg)

The Cheque Cancelation or Stop Request is restricted to a single cheque per InterAct message.

![](_page_864_Figure_0.jpeg)

The Agent B (Drawee Agent) sends a ChequeCancelationOrStopReport message to Agent A (the Drawer Agent). The ChequeCancelationOrStopReport message reports the outcome of a Cheque Cancellation or Stop Request.

## **Group Header**

![](_page_866_Picture_0.jpeg)

Each ISO 20022 cash management message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Advice of Cheque message. However, the *Sender's Reference* (Field 20) could be considered a similar comparison.

![](_page_867_Picture_0.jpeg)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

![](_page_867_Picture_4.jpeg)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

![](_page_868_Picture_0.jpeg)

The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1.

![](_page_869_Picture_0.jpeg)

The Cheque Cancellation or Stop Report *Cheque* nested element specifies the details of the Cheque.

![](_page_870_Figure_2.jpeg)

This Cheque element has been restricted to one cheque occurrence.

The Cheque Cancellation or Stop Report *Instruction Identification* provides an optional element to identify unambiguously the instruction

![](_page_871_Picture_2.jpeg)

Point to point reference that can be used between the Drawee Agent providing the Cheque Cancellation or Stop Report and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

The Cheque Cancellation or Stop Request *Original Instruction Identification* provides an optional element to identify unambiguously the original instruction

![](_page_872_Picture_2.jpeg)

Point to point reference that can be used to identify the original Cheque Cancellation or Stop Request between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving the request message) to refer to the individual request.

The Cheque Cancellation or Stop Request *Cheque Number* provides a mandatory element to identify unambiguously the Cheque.

![](_page_873_Picture_2.jpeg)

Unique and unambiguous number for the cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque

The Cheque Cancellation or Stop Report has several element to capture a Date related to the cheque.

![](_page_874_Picture_1.jpeg)

**Min 1 – Max 1**

The *Issue Date* is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer

![](_page_874_Picture_4.jpeg)

**Min 0 – Max 1**

The *Stale Date* is an optional element and represents the date after which a cheque is no longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days" or may be determined in accordance with domestic banking practice. Not all countries will have a validity period.

![](_page_875_Picture_0.jpeg)

<sup>A</sup> mandated currency **Amount** of the cheque to be paid to the payee. **£ \$ Min 1 – Max 1**

![](_page_875_Picture_2.jpeg)

The *Effective Date* is an optional element, it is used to capture the original **Value Date** (as provided in the camt.107), where different to the original **Issue Date**, i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account. **Min 0 – Max 1**

![](_page_875_Picture_4.jpeg)

The Cheque Cancellation or Stop Request *Drawer Agent* optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification is sent to the *Drawee Agent.* 

The *Drawer Agent Account* optionally captures the Drawer Agent's Account with the *Drawee Agent*  and who would receive an order the pay the cheque upon presentment.

![](_page_876_Picture_3.jpeg)

![](_page_876_Picture_4.jpeg)

The Drawer Agent and Drawer Account elements where present should match that of the original camt.107 Cheque Presentment Notification.

![](_page_876_Picture_6.jpeg)

The Cheque Cancellation or Stop Request *Payee* captures the party that should receive an amount of money as specified in the cheque. The Payee sub-element describe the Payee in greater detail. **Min 0 – Max 1** Nested element capturing either

![](_page_877_Figure_1.jpeg)

Mandatory *Name Name*

<span id="page-878-0"></span>The Cheque Cancellation or Stop Request *Cheque Cancellation or Stop Reason* nested element captures information associated with the reason for the Cheque Cancellation or Stop request.

#### **Min 0 – Max 1**

the *Originator* element helps identify the party who request the cheque cancellation or stop request. Where used this party would typically be the Payer of the cheque.

#### **Min 1 – Max 1**

!

the *Status* is mandatory and represented by an embedded status *Code* choice ( ) REJT (Rejected) or ACCP (Accepted)

#### **Min 0 – Max 2**

the *Additional Information* element may also be included to provide further details on the cancellation or stop reason.

![](_page_878_Picture_8.jpeg)

![](_page_878_Picture_9.jpeg)

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

#### **Serial Financial Institution to Financial Institution to Customer Credit Transfer**

Use Case c.109.1 – High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque Use Case c.109.2 – High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.

![](_page_880_Figure_0.jpeg)

Drawee Agent (B) reports to the Drawer Agent (A) that the Cheque Cancellation or Stop request has been accepted. 1

![](_page_880_Figure_2.jpeg)

See use case c.108.1.1 for an example the Cheque Cancellation or Stop Request

![](_page_881_Figure_0.jpeg)

![](_page_881_Figure_1.jpeg)

Drawee Agent (B) reports to the Drawer Agent (A) that the Cheque Cancellation or Stop request has been rejected. Additional Information is provided to explain that the cheque has already been presented and paid. 1

![](_page_881_Figure_3.jpeg)

See use case c.108.1.2 for an example the Cheque Cancellation or Stop Request

![](_page_882_Picture_0.jpeg)

www.swift.com

---

