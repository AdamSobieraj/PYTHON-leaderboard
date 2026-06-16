<!-- ELEMENT 1 -->
This Cross-Border Payment Reporting plus (CBPR+) User Handbook is intended to document and explain a variety of ISO 20022 payment related topics, as well as provide practical use cases to ensure understanding and adoption of ISO 20022 within the payment industry.

The SWIFT FINplus service will support CBPR+ messages on the SWIFT network traditionally associated with correspondent banking (many-to-many). These messages may be exchanged either between Agents in the same country or between Agents in

The use cases focus on a core topics where relevant messages may also be referred to within the use case, it may also be necessary to consider other documented use cases, in order to capture a wider variation of scenarios.

**Note:**
This document jointly developed with the CBPR+ group continues to evolve inline with the Standards Release as:

*   CBPR+ continue to develop market practice guidelines for additional message.
*   Inaccuracies are identified and corrected.
*   Further use cases and/or explanation needs are identified

---

<!-- ELEMENT 2 -->
* Page 2 Updated - note
* Page 5 Updated - new messages added to index
* Page 6 Updated - new messages added to index
* Page 11 Updated - correction of intermediary code
* Page 33 Updated - new messages and Usage ids added
* Page 40 Updated - new pain message added to index
* Page 45 Updated - recognition of Payment Initiation relaybook
* Page 107 Updated - recognition of Payment Initiation relaybook
* Page 122 Updated - additional use cases in the index
* Page 126 New - use case
* Page 134 New - use case
* Page 135-182 Page - pain.008 message section
* Page 184 Update - new messages added to index
* Page 204 Update - removed referer to Wait For Settlement Market Practice
* Page 351 New - new high level message flow
* Page 371 Updated - new messages added to index
* Page 379-380 Page - .003 use cases
* Page 400 Updated - additional guidance on ultimate parties on the return
* Page 423 Updated - corrected to Agent description in Step 7
* Page 458-488 Updated - docs.Origin Margin Collection section
* Page 489-529 Page - .003 Customer Direct section
* Page 530 Updated - new message added to index
* Page 674 Updated - removed reference to SR 2023
* Page 682 Updated - moved reference to multiple notification, now at Itemlevel
* Page 691 Updated - reference to multiple notification Item Rule
* Page 698-716 Page - cert.058 Notice to Received Cancellation section
* Page 743 Updated - new message added to index
* Page 764 Updated - Use case id correction
* Page 774-795 Page - Customer Cancellation Request section
* Page 823-883 New - Customer Message flow

The following icons signify changes to slide from the previous iteration.

---

<!-- ELEMENT 3 -->
* Message type and direction
* Optional Message type and direction
* Focal Message type and direction
* pacs Debtor
* pacs Creditor
* pacs.008 Ultimate Debtor
* pacs.008 Ultimate Creditor
* Initiating party on behalf of the Debtor
* Agent
* Agent processing legacy format during a coexistence period
* Market Infrastructure
* Exception & Investigation Case Assigner
* Exception & Investigation Case Assignee
* Statement Account Owner
* Statement Account Servicer
* Statement Authorised Party
* Payment Initiation (pain)
* Payment Clearing and Settlement (pacs)
* Cash Management Reporting (camt)
* Exception & Investigation (camt)
* Focus message
* Element Hierarchy Path
* Nested Element
* Element Choice
* Nested Element involving a choice
* New slide since last iteration
* Slide updated since last iteration

---

<!-- ELEMENT 4 -->
# Table of Contents

1. Introduction to ISO 20022
2. Business Application Header
3. Payment Initiation (pain)
    * pain.001 - Interbank Customer Credit Transfer Initiation
    * pain.002 - Interbank Customer Payment Status Report
    * pain.008 – Customer Direct Debit Initiation [new for SR2023]
4. Payment, Clearing and Settlement (pacs) messages
    * pacs.002 – Financial Institution to Financial Institution Payment Status Report
    * pacs.004 – Payment Return
    * pacs.003 – Financial Institution to Financial Institution Customer Direct Debit [new for SR2023]
    * pacs.008 – Financial Institution to Financial Institution Customer Credit Transfer
    * pacs.009 (core) - Financial Institution Credit Transfer
    * pacs.009 (cov) - Financial Institution 'Cover' Credit Transfer
    * pacs.009 (adv) - Financial Institution 'Advice' Credit Transfer

---

<!-- ELEMENT 5 -->
# 5. Cash Management Contents (continued)

* camt.052 - Bank to Customer Account Report
* camt.053 - Bank to Customer Statement
* camt.054 - Bank to Customer Debit Credit Notification
* camt.057 – Notification to Receive
* camt.058 – Notification to Receive Cancellation Advice (new for SR2023)

## 6. Cash Management Exception & Investigation (camt) messages

* camt.029 - Resolution of Investigation
* camt.055 – Customer Payment Cancellation Request (new for SR2023)
* camt.056 - FI to FI Cancellation Request

## 7. Cheques

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
Payment and Cash Management
Securities
Trade Services
Foreign Exchange
Card Payment

# Message Definitions
acmt: Account Management
auth: Authorities
camt: Cash Management
pacs: Payment Clearing and Settlement
pain: Payment Initiation
remt: Payment Remittance Advice

# Message Sets
cant.052 Bank to Customer Account Report
cant.053 Bank to Customer Statement
cant.054 Bank to Customer Debit Credit Notification
cant.056 FI to Payment Cancellation Request
cant.057 Notification to Receive
pacs.002 FI to Payment Status Report
pacs.004 Payment Return
pacs.008 FI to Customer Credit Transfer
pacs.009 Financial Institution Credit Transfer
pain.001 Customer Credit Transfer Initiation
pain.002 Customer Payment Status Report
pain.012 Creditor Payment Activation Request

ISO 20022 catalogue messages hierarchically beginning with a Business Domain, contain a various sets of Message Definitions, which in turn contain a variety of Message Sets.

for example:
* Payment and Cash Management
* Payments Clearing and Settlement

---

<!-- ELEMENT 9 -->
4!a . 3!c . 3!n . 2!n
|-------------------|
Business area
|
Message identifier/functionality
|
Variant
|
Version

***

Example
pacs.008.001.08
|
Version 8
|
Variant 1
|
FI To FI Customer Credit Transfer
|
Payments Clearing and Settlement

---

<!-- ELEMENT 10 -->
# Payment Initiation (pain)
*   Ultimate Debtor $\rightarrow$ Debtor (.50a)
*   Ultimate Debtor $\rightarrow$ Forwarding Agent
*   Debtor $\rightarrow$ Initiating Party

# Payments Clearing & Settlement (pacs)
*   **Input/Agents:** Previous Instructing Agents (:72:INS/)
*   **Reimbursement Agents:** (:53a, :54a, :55a)
*   **Intermediary Agents:** (:72:INT/)

**Flow of Actors:**
1.  Debtor Agent (.52a) $\rightarrow$ Instructing Agent (Sender)
2.  Instructed Agent (Receiver)
3.  Creditor Agent (.57a)

# Cash Management (camt)
*   Ultimate Creditor $\rightarrow$ Creditor (.59a)

***
*(Note: The diagram includes small annotations indicating that certain elements were "introduced in ISO 20022" and refer to the "XML format equivalent.")*

---

<!-- ELEMENT 11 -->
The diagram attempts to explain the construct of an ISO 20022 message sent across the SWIFT network using the FINplus service (which is designated to support various ISO 20022 business domains on SWIFT Interact).

Within the CBPR+ User Handbook the predominant focus is on the Request Payload, as this is where the business information is contained. However, it is worth noting that a network provider will have additional containers around the Request Payload to perform functionality on its network. This diagram presents the additional containers on the SWIFT network such as the Request Header often referred to as the Technical Header of the message.

***

**Message Structure Flow:**

*   Exchange Request
    *   Request
        *   RequestHeader
            *   RequestPayload
                *   Application Header
                    *   Document
                        *   MX Message Instance
                        *   Crypto

**Annotations and Components:**

*   SWIFTNet Headers
*   Envelope - container for the business message
*   The business message comprises the application header and 'business' document
*   The 'business' document contains the MX message instance (or ISO 20022 message instance)

**Structural Tags:**

*   `<AppHdr>`
    *   `...`
    *   `</AppHdr>`
*   `<Document>`
    *   `...`

**Message Types:**

*   ISO 20022 Business Application Header
*   Business Message
*   ISO 20022 Message

---

<!-- ELEMENT 12 -->
## XML Elements

An XML instance or document contains data in elements and nested elements (elements which contain other elements) corresponding to the hierarchy imposed by the XML schema. In the CBPR+ Usage Guidelines we often refer to the element hierarchy by levels (to understand the nested relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example in a pacs.008 Customer Credit Transfer the Interbank Settlement Date is a sub-element (Level 2 of the Credit Transfer Transaction Information element (Level 1).

| Element | Description |
| :--- | :--- |
| Credit Transfer Transaction Information | |
| Interbank Settlement Amount | |
| Interbank Settlement Date | |

## Naming conventions

An XML element is named according to the following rules:

*   The name can contain letters, numbers, and other characters, but must not start with a number or punctuation mark.
*   The name must not start with XML, xml, or Xml.
*   The name must not contain any spaces.

| Min | Max | Element Multiplicity |
| :---: | :---: | :--- |
| 1 | 1 | Required element |
| 0 | 1 | Optional element |
| 0 | * | Unlimited element occurrences |

## MX naming conventions

There are some generic naming rules that apply to most items in the database.

*   The names of all items in the database use the upper CamelCase convention, as follows:
    *   Each word starts with a capital letter.
    *   There are no white spaces between words.
*   A name may be made up of multiple words, each consisting of alphanumeric characters.
*   Words use British English vocabulary.
*   All names must start with an alphabetic character.
*   All characters that follow the first characters must be letters or numbers.

Example of a Street Name element: `<StrNn>Oxford Street</StrNn

---

<!-- ELEMENT 13 -->
## Empty XML Elements

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element.

A common example of this is in pavement message is Financial Institution.

| Element | Count 1 | Count 2 |
| :--- | :---: | :---: |
| Financial Institution Identification | 1 | 1 |
| BICFI | 0 | 1 |
| Clearing System Member Identification | 0 | 1 |
| LEI | 0 | 1 |
| Name | 0 | 1 |
| Postal Address | 0 | 1 |

Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e., `<FinInstnId></FinInstnId>`.

In the FINplus service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where business data should be provided within a nested element, it is provided.

---

<!-- ELEMENT 14 -->
MyStandards describes the element's context by its path whereby each element is divided by a forward slash (/). For example the pacs.008 Town Name within the Debtor Postal Address is described as /Document/FIToFICstmrCdtTrf/Cdtr/PstlAdr/Town

Within the CBPR+ a similar Path principal is often used to visualise an element being explained, where the name is expanded rather than describing the element in an XML naming convention.

For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment Identification is an element below Credit Transfer Transaction Information.

*   To visualise an element which has nested elements beneath it
*   To visualise an element which has a choice associated with it i.e., a Code where a choice of which code can be determined
*   To visualise an element which is nested and has a choice associated with it. For example, an identification where a choice must be made between an Organisation Identification and a Private Identification element which is nested, but where both cannot be used together.

---

<!-- ELEMENT 15 -->
SWIFT MyStandards
Search Standards Overview CBPR+ Swift Guidelines Corporate

Cross-Border Payments and Reporting Plus (CBPR+) specifications define how ISO 20022 is used for cross-border payments and cash reporting on the Swift network. Customization to CBPR+ specifications will be validated by Swift messaging services and interfaces, so it is imperative that users implement these specifications correctly. The resources available on this page aim to help Swift's community to understand CBPR+ specifications.

Learn more about CBPR+ Readiness

CBPR+ Usage Guidelines and Readiness Portal
CBPR+ Transition Portal

Additional resources

**CBPR+ user handbook**
Captures how CBPR+ Usage Guidelines support business operations in cross-border payment and reporting processes.
Download >

**Data integrity market practice guidance**
Defines recommended market practices to report localized or missing information using the MT messaging standard.
Download >

**CBPR+ and HYFS alignment**
Links the capabilities and differences between the two market practices for payments.
Download >

**Derived data mapping guidance**
Provides guidance on how to populate information from one messaging standard to their other subsequent message.
Download >

**MT/MX equivalence table**
Documents the CBPR+ Usage Guidelines supported on Swift Interlocutor in comparison with the equivalent MT message.
Download >

**Lessons learnt since go-live**
This document provides to provide guidance to community regarding lessons learned since go-live or after migration.
Download >

Samples library

**CBPR+ sample messages**
Sample messages sets to find the use cases described in the CBPR+ user handbook.
Learn more >

**Inflow transaction service sample messages**
Sample test messages for the flow of inflow service.
Learn more >

https://www2.swift.com/mystandards/#/c/cbpr/landing

---

<!-- ELEMENT 16 -->
# Cross Border Payments and Reporting Plus

CBPRplus-gacs.008.001_FtdCustomerCreditTransfer

CBPRplus ISO 20022 Portfolio, November 2022, Release 2.0 | Technical version: 1, Version: V2.0 FOR IMPLEMENTATION, Format: XML, Status: Final
Usage identifier: swift.cbprplus.v2.0_FOR_IMPLEMENTATION Status: Final

[Content] [Result View] [History] [Sample Messages]

Show xml tags

Many of the CBPRplus Usage Guidelines have useful key principals and additional information. These can be expanded in MyStandards by clicking on 'show details' in the middle of the Usage Guideline description pane.

***

## Metadata Details (Right Panel)

| Field | Value |
| :--- | :--- |
| Publisher: | Cross Border Payments and Reporting Plus (CBPR+) |
| Technical version: | 1 |
| Version: | V2.0 FOR IMPLEMENTATION |
| Status: | Final |
| Standard: | gacs.008.001 |
| Format: | XML |
| Usage identifier: | swift.cbprplus.v2.0_FOR_IMPLEMENTATION |

**Description:**

TA: AGENTS IDENTIFICATION - RECOMMENDATION

A principal is present, then a Postal Address is NOT allowed (Claiming/Intermediary/Beneficiary and LC may complement). However, it is also possible that the Principal does not have an address.

TA: BIC is absent, (Name & Postal Address) or Clearing/intermediary/beneficiation must be present and both are allowed together.

Note: "Instructed Instructed Agents" must be identified with a BIC - Clearing System Identifiers and LC are optional.

TA: DEBITORIDENTIFIER - PASTY IDENTIFICATION - RECOMMENDATION

If any BIC is present, then Name and Postal Address is NOT allowed (either elements remain). However, in case of conflicting
information, the BIC will always take precedence.

---

<!-- ELEMENT 17 -->
Traditionally in the Legacy FIN standard rules related to a message were described as either Network Validation Rules – those validated by the network, or Usage rules – rules not validated by the network. FIN also has the concept of Usage Guidelines– guideline to recommend a best practice.

In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated Usage Guideline (e.g. CBPR plus)

**Formal Rules** which are validated on the network, these are identified by the word Rule appended to the rule description. For example: ⚠️ Rule “CBPR_Party_Any_BIC_FormalRule”

**Textual Rules** which are not validated on the network, these are identified by the word TextualRule appended to the rule description. For example: ⚠️ Rule “CBPR_Agent_Option_1_TextualRule”

**Guideline Rules** which provide recommended best practice, these are identified by the word Guideline appended to the rule description. For example: ⚠️ Rule “CBPR_Purpose_Guideline”

Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a CrossElementSimpleRule and a CrossElementComplexRule.

---

<!-- ELEMENT 18 -->
`<Short issuer organisation>.<Business context>.<Business context> n times.<version>`
| A | B | C, D,... | E |
| :---: | :---: | :---: | :---: |
| 1-10 chars | 1-10 chars | 1-10 chars | 2 chars |

Total max 35 char

*   **Type:** String
*   **Max allowed size:** 35 characters
*   **Structure:**
    *   Must contain minimum A & B optionally followed by 1 or more additional business context elements (C, D, ...).
    *   Always ends with version element E (format "nn", e.g., "01").
    *   Each element is separated by a period ".".
    *   Length of each text element can vary up to max 10 characters.
    *   Consistency enforced by lightweight SWIFT review/registration: E.g., "ecb" to represent the ECB, not "eucb".
    *   Lowercase alphanumerical characters only.

In CBPR+ the Usage Identifier is captured within the Business Application Header, Business Service element. More detail can be found in the dedicated Business Application Header chapter of this document.

---

<!-- ELEMENT 19 -->
Many ISO 20022 message use data elements represented by codes. Such codes are often externalised from the message itself, enabling maintenance of the code list on a quarterly basis without requiring a new message version.

Some data element may also be embedded in the message.

example of Charge Bearer in pacs.008 v8
| Field | Value |
| :--- | :--- |
| Charge Bearer | 1 |
| Borne By Debtor [DEBT] | 1 |
| Borne By Creditor [CRED] | 1 |
| Shared [SHAR] | 1 |
| Following Service Level [SLEV] | 1 |

example of Return Reason Information in pacs.004 v9 which uses externalised codes
| Field | Value |
| :--- | :--- |
| Return Reason Information | 0 |
| Originator | 1 |
| Reason | 1 |
| Code | 1 |
| Proprietary | 1 |

Proprietary Codes may also be available for certain data elements. These are typically inherited from legacy formats and require definitions in user documentation as these are not captured in the baseline ISO 20022 standards

| Definition | Type |
| :--- | :--- |
| Reason for the return, an external reason code | ExternalReturnReasonCode (by on string) |
| | max length: 1 |
| | max length: 4 |
| ReturnReasonCode | E051 |
| | E052 |
| | E053 |
| | E054 |
| | E055 |
| | E056 |
| | E057 |
| | E058 |
| | E059 |
| | E060 |

---

