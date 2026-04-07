<!-- ELEMENT 1 -->
This Cross-Border Payment Reporting plus (CBPR+) User Handbook is intended to document and explain a variety of ISO 20022 payment related topics, as well as provide practical use cases to ensure a common industry.

The SWIFT FINplus service on the SWIFT network traditionally associated with correspondent banking (manyto-many). These messages may be exchanged either between Agents in the same understanding and adoption of ISO 20022 within the payment will support CBPR+ messages

The use cases focus on a core topics where other relevant messages may also be referred to within the use case, it may also be necessary to consider other documented use cases, in order to capture a wider variation of scenarios.

# Note:

This document jointly developed with the CBPR+ group continues to evolve inline with the Standards Release as:

- CBPR+ continue to develop market practice guidelines for additional message.

- Inaccuracies are identified and corrected.

- Further use cases and/or explanation needs are identified

---

<!-- ELEMENT 2 -->
```
Page 2 Updated - note Page 5 Updated - new messages added to index Page 6 Updated - new messages added to index Page 11 Updated - correction of Intermediary code Page 33 Updated - new messages and Usage Ids added Page 40 Updated - new pain message added to index Page 45 Updated - recognition of Payment Initiation relay rulebook Page 107 Updated - recognition of Payment Initiation relay rulebook Page 122 Updated - additional use cases in the index Page 126 New -use case Page 134 New - use case Page 135-182 New - pain.008 message section Page 184 Update - new messages added to index Page 204 Update - removed refer to Wait For Settlement Market Practice Page 351 New - new high level message flow Page 371 Updated - new messages added to index Page 379-380 New - pacs.003 use cases Page 400 Updated - additional guidance on ultimate parties on the return Page 423 Updated - correct to Agent description in Step 7 Page 458-488 New - pacs.010 Margin Collection section Page 489-529 New - pacs.003 Customer Direct Debit section Page 530 Updated - new message added to index Page 674 Updated - removed reference to SR 2023 Page 682 Updated - moved reference to multiple notification, now at an Item level Page 691 Updated - reference to multiple notification item Rule Page 698-716 New - camt.058 Notice to Received Cancellation section Page 743 Updated - new message added to index Page 764 Updated - use case id correction Page 774-795 New - Customer Cancellation Request section Page 823-883 New - Cheque message sections
```

The following icons dignify  changes to slide from the previous itineration.

---

<!-- ELEMENT 3 -->
Message type and direction

Optional Message type and direction

Focal Message type and direction

pacs Debtor pacs Creditor

pacs.008 Ultimate Debtor pacs.008 Ultimate Creditor

Initiating  party on behalf of the Debtor

Agent

Agent processing legacy format during a coexistence period

Market  Infrastructure

Exception & Investigation  Case Assigner

Exception & Investigation  Case Assignee

Statement Account Owner

Statement Account Servicer

Statement Authorised Party

Shortcut to other part of document

Extra attention  is needed

Legacy FIN  MT message gpi Tracker

Payment Initiation  (pain)

Payment Clearing and Settlement (pacs)

Cash Management  Reporting (camt)

Cash Management  Exception & Investigations  (camt)

Focus message

Element Hierarchy Path

Nested Element

Element Choice

Nested Element involving  a choice

New slide since last iteration

Slide updated since last iteration

---

<!-- ELEMENT 4 -->
- Introduction to ISO 20022

- Business Application Header

- Payment Initiation (pain)

pain.001 - Interbank Customer Credit Transfer Initiation pain.002 - Interbank Customer Payment Status Report

pain.008 - Customer Direct Debit Initiation new for SR2023

- Payment, Clearing and Settlement (pacs) messages

pacs.002 - Financial Institution to Financial Institution Payment Status Report pacs.004 - Payment Return

pacs.003 - Financial Institution to Financial Institution  Customer Direct Debit pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer

pacs.009 (core) - Financial Institution Credit Transfer pacs.009 (cov) - Financial Institution 'Cover' Credit Transfer

pacs.009 (adv) - Financial Institution 'Advice' Credit Transfer new for SR2023

---

<!-- ELEMENT 5 -->
5. Cash Management Reporting (camt) messages camt.052 - Bank to Customer Account Report

camt.053 - Bank to Customer Statement camt.054 - Bank to Customer Debit Credit Notification

camt.057 - Notification to Receive camt.058 - Notification to Receive Cancelation Advice

new for SR2023

6. Cash Management Exception & Investigation (camt) messages camt.029 - Resolution of Investigation

camt.055 - Customer Payment Cancelation Request new for SR2023

camt.056 - FI to FI Cancellation Request

# 7. Cheques

camt.107 - Cheque Presentment Notification new for SR2023

camt.108 - Cheque Cancellation or Stop Notification new for SR2023

camt.109 - Cheque Cancellation or Stop Report new for SR2023

---

<!-- ELEMENT 7 -->
ISO 20022 introduces a fundamental change to the traditional language used by the payments industry for several decades. It also describes participants (i.e., parties) to a business transaction  differently based upon the business domain (area) being described, in a similar way you may describe a person as a colleague, parent or sibling depending upon the context you wish to describe them. This section is designed to capture and explain some of the differences.

---

<!-- ELEMENT 8 -->
# Domains

# Payment and Cash Management

Securities

Trade Services Foreign Exchange Card Payment

# Message  Definitions

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

# Message Sets

camt.052  Bank  to Customer  Account Report camt.053  Bank  to Customer  Statement camt.054  Bank  to Customer  Debit  Credit  Notification camt.056  FI  to FI  Payment  Cancellation  Request camt.057  Notification  to Receive pacs.002 FI  to FI  Payment  Status Report pacs.004 Payment  Return pacs.008 FI  to FI  Customer  Credit  Transfer pacs.009 Financial  Institution  Credit  Transfer

pain.001  Customer  Credit  Transfer initiation pain.002  Customer  Payment  Status Report pain.012  Creditor  Payment  Activation Request

ISO 20022 catalogue messages hierarchically beginning with a Business Domain, contain a various sets of Message Definitions, which in turn contain a variety of Message Sets.

for example:

- Payment and Cash Management

- Payments Clearing and Settlement

---

<!-- ELEMENT 10 -->
Payment Initiation (pain)

Ultimate

Forwarding

Debtor

Debtor

:50a

Agent

Initiating

Party

Payments Clearing & Settlement (pacs)

:72:/INS/

Previous Instructing

Agents

1

Debtor

Agent

:52a

2

3

1

Instructing

Agent

Sender

:53a

:54a

:55a

Reimbursement

Agents

2

3

Instructed

Agent

Receiver

:56a

:72:/INTA/

Intermediary

Agents

2

1

3

Creditor

Agent

:57a introduced in

equivalent

ISO 20022

Cash Management

(camt)

Ultimate

Creditor

Creditor

:59a

---

<!-- ELEMENT 11 -->
The diagram attempts to explain the construct of an ISO 20022 message sent across the SWIFT network using the FINplus service (which is designated to support various ISO 20022 business domains on SWIFT Interact)

Within the CBPR+ User Handbook the predominant focus is on the Request Payload, as this is where the business information is contained. However, it is worth noting that a network provider will have additional containers around the Request Payload to perform functionality on its network. This diagram presents the additional containers on the SWIFT network such as the Request Header often referred to as the Technical Header of the message.

---

<!-- ELEMENT 12 -->
# XML Elements

An XML instance or document contains data in elements and nested elements (elements which contain other elements) corresponding to the hierarchy imposed by the XML schema. In the CBPR+ Usage Guidelines we often refer to the element hierarchy by levels (to understand the nested relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example in a pacs.008 Customer Credit Transfer the Interbank Settlement Date is a sub-element (Level 2) of the Credit Transfer Transaction Information element (Level 1).

# Naming conventions

An XML  element is named according to the following rules:

- The name can contain letters, numbers, and other characters, but must not start with a number or punctuation  mark.

- The name must not start with XML,  xml, or Xml.

- The name must not contain any spaces.

# MX naming conventions

There are some generic naming rules that apply to most items in the database.

- The names of all items in the database use the upper CamelCase convention,  as follows:

- Each word starts with a capital letter.

- There are no white spaces between words.

- A name may be made up of multiple words, each consisting of alphanumeric characters.

- Words use British English vocabulary.

- All  names must start with an alphabetic character.

- All  characters that follow the first characters must be letters or numbers.

Example of a Street Name element: <StrtNm>Oxford Street</StrtNm>

---

<!-- ELEMENT 13 -->
# Empty XML Elements

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element.

# Acommon example of this is in payment message is Financial Institution.

Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e., <FinInstnId></FinInstnId>

In the FINplus service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where business data should be provided within a nested element, it is provided.

---

<!-- ELEMENT 14 -->
MyStandards describes the element's context by its path whereby each element is divided by a forward slash (/) For example the pacs.008 Town Name within the Debtor Postal Address is described as /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/PstlAdr/TwnNm

Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing the element in an XML naming convention.

For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment Identification is an element below Credit Transfer Transaction Information.

# Credit Transfer Transaction Info' Payment Identification

In this way the CBPR+ User Hand Book uses three main icon to explain the relationships between element, by display the icon after the element name.

To visualise an element which has nested elements beneath it

To visualise an element which has a choice associated with it i.e., a Code where a choice of which code can be determined

To visualise an element which is nested and has a choice associated with it. For example, an Identification where a choice must be made between an Organisation Identification and a Private Identification element which is nested, but where both cannot be used together.

---

<!-- ELEMENT 15 -->
# https://www2.swift.com/mystandards/#/c/cbpr/landing

---

<!-- ELEMENT 17 -->
Traditionally in the Legacy FIN standard rules related to a message were described as either Network Validation Rules -those validated by the network, or Usage rules - rules not validated by the network. FIN also has the concept of Usage Guidelines -guideline to recommend a best practice.

In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated UsageGuideline(e.g. CBPRplus)

Within CBPR+ UsageGuidelinespecification the rules dedicate to CBPR+ are often described as:

Formal Rules which are validated on the network, these are identified by the word Rule appended to the rule description. For example: Rule 'CBPR_Party_Name_Any_BIC_FormalRule'

Textual Rules which are not validated on the network, these are identified by with the word TextualRule appendedto the rule description. For example: Rule 'CBPR_Agent_Option_1_TextualRule'

Guideline Rules which provide recommended best practice, these are identified by the word Guideline appendedto the rule description. For example:

Rule 'CBPR_Purpose_Guideline'

Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a

---

<!-- ELEMENT 18 -->
.

.

.

- Type: String

- Max allowed size: 35 characters

- Structure:

- o Must contain minimum A & B , optionally  followed by 1 or more additional business context elements (C, D, …).

- o Always ends with version element E (format 'nn', e.g., '01')

- o Each element is separated by a period '.'

- o Length of each text element can vary up to max 10 characters. Total length, including periods, cannot exceed 35 chars.

- o Consistency enforced by lightweight  SWIFT review/registration:  E.g., 'ecb' to represent the ECB, not 'eucb'

- o Lowercase alphanumerical characters only

In CBPR+ the Usage Identifier is captured within the Business Application Header , Business Service element. More detail can be found in the dedicated Business Application Header chapter of this document,

---

<!-- ELEMENT 19 -->
Many ISO 20022 message use data elements represented by codes. Such codes are often externalised from the message itself, enabling maintenance  of the code list on a quarterly basis without requiring a new message version.

Some data element may also be embedded in the message.

example of Charge Bearer in pacs.008 v8 which uses embedded codes

Proprietary Codes may also be available for certain data elements.

These are typically inherited from legacy formats and require definitions in user documentation  as these are not captured in the baseline ISO 20022 standards example of Return Reason Information in pacs.004 v9 which uses externalised codes

---

<!-- ELEMENT 20 -->
All SWIFT ISO MX message elements (fields) which are defined (by data Type) as text are restricted to FIN X Characters:

# a-z A-Z 0-9 / - ? : ( ) . , ' + .

Special characters are additionally allowed in:

- All party (agents and non-agents) Name and Address elements.

- The Related Remittance Information element

- The Remittance Information (structured & unstructured) element

- The Email Address where included as part of a Proxy elements

- City of Birth and Province of Birth elements nested in Private Identification

List of special characters:

Currencies in the payments should be expressed in ISO Currency Codes only (3Characters, e.g. EUR)

Translation of any special character: !#&%*=^_`{|}~";@[\]$ >< into MT messages will be represented by a . (Full Stop)

---

<!-- ELEMENT 21 -->
Point-to-point refers to data passed within a message from one party to the next. This data will not necessarily be passed in subsequent  messages.

- For example: the Instruction Identification element contains a reference meaningful  to the party sending  a message, subsequent  messages in a payment transaction chain  can expect the Instruction Identification to be replaced by a reference meaningful  to the party sending  that message leg.

End-to-end refers to data passed throughout  the transaction life cycle i.e. within a message from one party to the next and continued  in subsequent  messages.

- For example: the UETR element contains a Unique  End-to-end Transaction Reference in accordance with the UUID  version 4 standards. This same reference is used in all messages related to the payment transaction.

---

<!-- ELEMENT 22 -->
ISO 20022 messages have a number of elements associated with Agents which allow for these Agents to be referenced by a variety of Financial Institution identifiers.

More commonly the ISO 9362 Financial Institution BIC ( BICFI ) is considered the best practice de facto standard for 'many to many' / correspondent banking payments. However other options include:

Clearing System Member Identifiers when accompanied with the Clearing System Identification . LEI (Legal Entity Identifier)

Name and either structured or unstructured Postal Address .

---

<!-- ELEMENT 23 -->
CBPR+ usage guidelines DateTime elements mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) note - milliseconds are optional.

The ISO 20022 Date elements allow the date to include  an offset. As a data model, shared by other business domains, an offset date can provide great business clarify, such as something  expiring at the end of a business date. However, in payments such a date offset provides little business  value, whereby should an offset be include  with the date, this offset should be ignored.

---

<!-- ELEMENT 24 -->
For translation rules and comparison purposes this table provides a list of published MT National Clearing System codes again their equivalent ISO 20022 Clearing System Identification in the external code list.

---

<!-- ELEMENT 26 -->
# Min 0 - Max 1

The head.001 Business Application Header Character Set element declares the character set, in addition to Latin, that is contained in the Business Document e.g. the pacs.008.

The Character Set element uses the UnicodeChartsCode string to declare an additional character set, for example Cyrillic (Unicode range: 0400-04FF).

Ж œ

This allows the party for which the message is addressed To to know in advance the additional character set contained within the Business Document. In this way the message can be routed to a specific application to process the Character Set or handled as an exception if the Character Set is not appropriate for that business transaction.

ݒ

图

Extending character sets is not intended in CBPR+ from the initial implementation of the service. This element is intended for use once extended character sets are implemented, whereby the string represented in this element can enable any necessary network validations, such as a closed

---

<!-- ELEMENT 27 -->
# Min 1 - Max 1

The head.001 Business Application Header From element identifies the BIC of the party who created the Business Document (e.g. pacs.008). Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

A choice must be made for the BIC depending on the party it represents.

Financial Institution Identification which identifies a Financial Institution, and may be further complemented with

- Clearing System Member Identification

- LEI

as an additional identification.

From

---

<!-- ELEMENT 28 -->
# Min 1 - Max 1

The head.001 Business Application Header To element identifies the BIC of the party who will ultimately process the Business Document (e.g. pacs.008) Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

A choice must be made for the BIC depending on the party it represents.

Financial Institution Identification which identifies a Financial Institution, and may be further complemented with

- Clearing System Member Identification

- LEI

as an additional identification.

To

---

<!-- ELEMENT 29 -->
The head.001 Business Application Header Business Message Identifier element contains the Message Identification captured within the Business Document's Group Header. The content of this element should match the Business Document to avoid incorrect routing by the recipient.

---

<!-- ELEMENT 30 -->
The head.001 Business Application Header Message Definition Identifier element contains the name of the Business Document. The content of this element should match the Business Document to avoid incorrect routing by the recipient.

---

<!-- ELEMENT 31 -->
The head.001 Business Application Header Business Service element is used to identify administered services on the SWIFT network. The data represented in this elements is referred to as a Usage Identifier . For CBPR+ examples are provided below, these values may be used together with the Message Definition Identifier to determine routing rules to specific applications without having to open the business document.

The Business Service is also intended to be incremented for the same message version, when an updated Usage Guideline is released. For example a new restriction is applied to the pacs.009.001.08 Usage Guideline, the Business Service swift.cbprplus.cov.02 and swift.cbprplus.02 will be used to reflect these new Guidelines and allow network validate.

Note : when a new message (Message Definition Identifier) version is introduced the numeric value for the

---

<!-- ELEMENT 32 -->
The data represented in the Business Service, together with the Message Definition Identifier has a number of roles, in addition to the routing rules referred to on the previous page.

# This data value:

- Identifiers explicitly the Usage Guideline within a library of guideline. For example an application may have various pacs.008 libraries within a collection, for which only one of these is appropriate to be used to identify data requirements or perform validation.

- is also populated in the Request Header of the InterAct message in the Request Sub Type element which allow the service

---

<!-- ELEMENT 33 -->
The head.001 Business Application Header Market Practice element is used to identify administered services on the SWIFT network.

This element is currently not foreseen to be used by CBPR+.

---

<!-- ELEMENT 34 -->
The head.001 Business Application Header Creation Date captures the date and time which the Business Application Header was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 35 -->
The head.001 Business Application Header Copy Duplicate indicator is used as a choice to identify scenarios where a message was previously sent.

COPY is used to represent a copy of a message being sent to an additional party. This scenario is only associated with camt reporting messages.

DUPL is used to represent a duplicate of a previously sent camt reporting message. To receive a duplicate payment message, Interact message retrieval should be utilised.

CODU is used to represent a duplicate of a previously sent COPY message. This scenario is only associated with camt reporting messages.

---

<!-- ELEMENT 36 -->
Min 0 - Max 1

The head.001 Business Application Header Possible Duplicate element is used as a flag to indicate that if the party who will ultimately process the Business Document (e.g. pacs.008) received the original, then it should perform necessary actions to avoid processing this Business Message again.

This element is represented by a Yes/No Boolean, whereby true represent this is a Possible Duplicate.

It is not necessary to represent false (No) the absence of this optional element itself indicates that this is not considered a Possible Duplicate.

The FINplus Technical Header has an element PDIndicator (Possible Duplicate Indicator) which uses a Yes/No Boolean. This may be populated by the network interface to identify a message it considers may be a possible duplicate.

---

<!-- ELEMENT 37 -->
The head.001 Business Application Header Priority element allows a choice of Business Message Priority Code to indicate the priority which may be applied to the business message.

This element must represent the priority code of the business document (instance) which is only applicable for pacs messages. The pacs message priority is captured in the Payment Type Priority/Instruction Priority.

---

<!-- ELEMENT 38 -->
# Min 0 - Max 1

The head.001 Business Application Header Related nested element enables the capture of the Business Application Header from a related Business Document. For example, in a pacs.004 Payment Return the Related Business Application Header from the original message can be included. This could allow the receiver to apply specific routing to the message, based on the related information i.e., return of a pacs.009 cov may be routed to different payment engine than a core pacs.009.

The following elements are nested within the Related element. Where used these contain the original data from the related Business Application Header:

From

To

Business Message Identifier

Message Definition Identifier

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

---

<!-- ELEMENT 39 -->
pain.001 Interbank Customer Credit Transfer initiation pain.002 - Interbank Customer Payment Status Report pain.008 - Customer Direct Debit Initiation

---

<!-- ELEMENT 40 -->
# Interbank Customer Credit Transfer Initiation

---

<!-- ELEMENT 41 -->
# Group Header

- Message Identification

- Initiating Party - where different from Debtor

- Forwarding Agent

# Payment Information

- Payment Information Identification

- Requested Execution Date

- Debtor

- Debtor Agent

# Credit Transfer Transaction Information

- Payment Identification

- Amount

- Charge Bearer

- Creditor Agent

- Creditor

# MT Field Name & (Tag option)

# Sequence A General Information :

- Sender's Reference (Field 20)

- Instructing Party (Field 50 C or L)

Message Sender in a 'relay' scenario

# Sequence A General Information :

- Customer Specified Reference (Field 21R)

- Requested Execution Date (Field 30)

- Ordering Customer (Field 50 F, G or H)*

- Account Servicing Institution (Field 52 A or C)*

# Sequence B Transaction Details :

- Transaction Reference (Field 21)

- Currency/Transaction Amount (Field 32B)

- Details of Charges (Field 71A)

- Account With Institution (Field 57 A, C or D)

- Beneficiary (Field 59 no letter, A or F)

---

<!-- ELEMENT 42 -->
# The pain.001 message is composed of three blocks:

- Group Header contains a set of characteristics that relates to all individual transaction.

- Payment Information contains a set of characteristics that relates to the debit side of the transaction, such as Debtor and Debtor Agent.

- Credit Transfer Transaction Information contains, among others, elements related to the credit side of the transaction, such as Creditor and Creditor Agent.

---

<!-- ELEMENT 43 -->
FINplus Customer Credit Transfer Initiation  message is sent by the Initiating  Party to the Forwarding Agent or the Debtor Agent.  It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

Relay : The pain.001 message is sent by the Initiating  party (the Debtor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.001 message to the Debtor Agent

---

<!-- ELEMENT 44 -->
FINplus Customer Credit Transfer Initiation  message is sent by the Initiating  Party to the Forwarding Agent or the Debtor Agent.  It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

Authorised Party Initiation: The pain.001 message is sent by the Financial Institution  as an Initiating  Party to the Debtor Agent to initiate  a payment on behalf of the Debtor who is the account holder. For example, a FI Initiates;  a liquidity  sweep on behalf of a corporate customer or payment from the Debtor account based on Tri-party  agreement (agreement from the Debtor with the Debtor

---

<!-- ELEMENT 45 -->
Interbank  Customer Credit Transfer Initiation  message is sent by the Initiating  Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

Financial Institution  Payment Initiation (to non-FI) : The pain.001  message is sent by the Financial Institution  as both the Debtor and Initiating  Party to initiate a payment from their account with the Debtor Agent  to move funds to a non-Financial  Institution Creditor

---

<!-- ELEMENT 46 -->
The following descriptions are defined in the ISO 20022 Standard for core parties participating in an Interbank Customer Credit Transfer Initiation relationship.

Forwarding Agent 'Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution'. Applicable for pain.001 use case 1 only

Initiating Party 'Party that initiates the payment.' which may be the Debtor or a Party acting on behalf of the Debtor e.g., the Agent initiating a liquidity sweep service

Debtor Agent 'Financial institution servicing an account for the debtor.'

Debtor 'Party that owes an amount of money to the (ultimate) creditor.'

Creditor Agent 'Financial institution servicing an account for the creditor.'

Creditor 'Party to which an amount of money is due.'

---

<!-- ELEMENT 48 -->
Min 1 - Max 1

Each ISO20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For the Payment Initiation (pain) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

Each transaction's Credit Transfer Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor or authorized third party) of the pain.001.

---

<!-- ELEMENT 49 -->
Min 1 - Max 1

The pain.001 message Creation Date Time captures the date and time which the message was created.

It is defined by ISO Date Time with mandatory date and time components expressed in the following formats:

- Universal  Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ

- Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2 nd option). Otherwise use UTC time (1 st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

---

<!-- ELEMENT 50 -->
# Min 0 - Max 2

The pain.001 message Authorisation allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The Authorisation uses an embedded code set or free text form. It has no exact equivalent in the legacy MT payment message, however, the Authorisation (Field 25) could be considered as a similar comparison.

For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.

---

<!-- ELEMENT 51 -->
# Min 1 - Max 1

The pain.001 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 52 -->
Min 1 - Max 1

The Initiating Party can either be the Debtor or an Authorised Party who initiates payment transactions on behalf of the Debtor . The Initiating Party can be, for example, the Head Office which has the authority to debit the account of its subsidiary. In the centralization model, the Initiating Party can also be a payment factory or shared service center or third-party agent, which has authority to send the message on behalf of the Debtor .

Therearethree common use casesin the context of interbank pain.001 message:

- Relay : The Initiating Party , which is either the Debtor themselves or authorised party, sends the pain.001 message to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.001 message to the Debtor Agent . This is commonly known as a relay scenario. Whereby the Forwarding Agent is performing a technical role in the payment transaction, they wouldnot be represented in the payment, clearing and settlement message.

- Authorised Party : The Initiating Party is the Financial Institution which has the authority to send the pain.001 message on behalf of the Debtor , e.g., multi-bank liquidity sweeps.

- Financial Institution Payment Initiation : The Initiating Party is the Financial Institution which is the Debtor who initiate a payment from their account to move

---

<!-- ELEMENT 53 -->
The Initiating Party can either be the Debtor or an authorised party, such as Financial  Institution, in the context of interbank pain.001. Sub elements describe the Initiating Party in greater detail.

Nested element capturing structured Postal Address including at least Town Name and Country if used.

Name

Mandatory Name wherePostal Address is provided.

Postal

Address

Nested element capturing the various types of identifiers, e.g., BIC, LEI etc. BIC is mandatory for an Authorised Party initiation and FI payment initiation.

Initiating

Party

Identification

Optional element to capture the Initiating Party's ISO country code

Contact

Country of

Residence

Details

---

<!-- ELEMENT 54 -->
Min 0 - Max 1

The Forwarding Agent is mandatory in a relay scenario whereby the Initiating Party (the Debtor or authorised third party) has to provide Business  Identifier Code (BIC FI) of the Forwarding Agent in the original pain.001 message. The Forwarding Agent acts as a concentrating  financial institution  and forwards the pain.001 message to the Debtor Agent for execution.

Other options to identify the Forwarding Agent include:

- Clearing System Member ID

- LEI (Legal Entity Identifier)

For the use cases of Authorised Party initiation and FI payment initiation, Forwarding Agent is not required.

---

<!-- ELEMENT 56 -->
The CBPR+ pain.001 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognise that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory.

As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message.

Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used.

---

<!-- ELEMENT 57 -->
The Interbank Customer Credit Transfer Initiation Payment Information Identification provides a mandatory element to identify the payment initiation.

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions.

For single transactions in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header.

---

<!-- ELEMENT 58 -->
Min 1 - Max 1

The pain.001 message Payment Method specifies the means of payment that will be used to move the amount of money. One of the following payment method codes must be used:

---

<!-- ELEMENT 59 -->
The pain message can be described.

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the

Min 0 - Max 1

Payment Type Information provides a set of optional elements where the payment type

Service Level Min 0 - Max 3

# Payment Type Information

Anested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored.

Local Instrument Min 0 - Max 1

Anested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, INST - Instant Credit Transfer for SEPA Service Level.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

Anested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends.

---

<!-- ELEMENT 60 -->
Min 1 - Max 1

The pain.001 message mandatory Requested Execution Date element, captures the date and time at which the initiating  party requests the clearing agent to process the payment.

It is the date on which the debtor's account is debited. If payment by cheque, the date when the cheque  must be generated by the bank. It is defined by either ISO Date expressed in the YYYY-MM-DD format or ISO Date Time below:

- Universal  Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ

- Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2 nd option). Otherwise use UTC time (1 st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

---

<!-- ELEMENT 61 -->
Min 0 - Max 1

The pain.001 message optional Pooling Adjustment Date element, is used for the correction of the value date of a cash pool movement  that has been posted with a different value date.

It is defined by ISO Date expressed in the YYYY-MM-DD format

This element is not widely used in the payment industry. For the use case of interbank, it is even less likely to be utilized.

---

<!-- ELEMENT 62 -->
The ISO 20022 pain messages describes the party whose account is debited for a transaction as the Debtor . The Debtor sub elements describe the Debtor in greater detail. Min 1 - Max 1

Mandatory Name (where a BIC identifier is not provided) by which the party is known

Nested element capturing either structured or unstructured Debtor address details.

Name

Postal Address

Note: Structured address is strongly recommended with mandatory Town Name and Country

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Optional element to capture the Debtor 's  ISO

Debtor

Country of Residence

---

<!-- ELEMENT 63 -->
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

---

<!-- ELEMENT 64 -->
Min 1 - Max 1

The Debtor Agent is a static role in  the pain.001 Customer Credit Transfer Initiation. This agent maintains  a relationship  with their customers, the Debtor .

Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

For Agent Identification, BIC is preferred, alternatively Clearing Member

---

<!-- ELEMENT 65 -->
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
Min 0 - Max 1

The Instruction for Debtor Agent element within the pain.001 message optionally provides information related to the processing of the payment.

The Instruction for Debtor Agent element offers a maximum  of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the Debtor Agent , depending  on bilateral agreement.

---

<!-- ELEMENT 67 -->
Min 0 - Max 1

Min 0 - Max 1

The pain.001 message introduces Ultimate Debtor and Ultimate Creditor . The Ultimate Debtor element should not be confused with an Initiating Party who may send a payment initiation request on behalf of the Debtor , for example, Payment Factory.

CBPR+ premise is that an Ultimate Debtor has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an Ultimate Creditor has no financial regulated account relationship with the corresponding Creditor.

The Ultimate Debtor and Ultimate Creditor can be identified by a combination  of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 68 -->
Min 0 - Max 1

The Charge Bearer element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 69 -->
Min 0 - Max 1

The pain.001 optional Charges Account element, which is used to process charges associated with a transaction.

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

This element is not widely used in the payment industry.

---

<!-- ELEMENT 70 -->
Min 0 - Max 1

The pain.001 optional Charges Account Agent element, which is used to specify the agent that services a charges account.

Charges account agent should  only be used when the charges account agent is different from the debtor agent.

This element is not widely used in the payment industry. It should also be noted that the ChargesAccountAgentRule inherited from the base message should be ignored as the optional Branchof DebtorAgent is removed from this Usage Guideline.

---

<!-- ELEMENT 72 -->
# Min 1 - Max 1

The pain.001 message contains Payment Identification which provides a set of elements to identify the payment of which several are mandatory elements.

---

<!-- ELEMENT 74 -->
Min 1 - Max 1

The pain.001 nested Amount element has a choice of either Instructed Amount or Equivalent Amount to capture the amount and currency of the Customer Credit Transfer Initiation.

Instructed Amount

The Instructed Amount captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. This amount has to be transported unchanged through the transaction chain. This element is comparable with the legacy Field 33B.

The Equivalent Amount nested element captures currency and Amount of money to be moved between the Debtor and Creditor, before deduction of charges, and is expressed in the currency of the Debtor's account. The Currency Of Transfer element capture the equivalent currency to be transferred which the first agent will convert the credit transfer into.

---

<!-- ELEMENT 75 -->
Min 0 - Max 1

The pain.001 Exchange Rate Information element provides details on the currency exchange  rate and contract.

Unit Currency

Currency in which the rate of exchange is expressed in a currency exchange. For example, 1GBP = xxxCUR, the unit currency is GBP.

Exchange Rate

The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency.

Rate Type

Specifies the type used to complete the currency exchange,such as SPOT,SALE or AGRD (Agreed).

Unique and unambiguous reference to the foreign

Exchange Rate Information

Contract

---

<!-- ELEMENT 76 -->
Min 0 - Max 1

The Charge Bearer element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 77 -->
Min 0 - Max 1

The Cheque Instruction information block contains a set of elements needed to issue a cheque. The following types of cheques are commonly  used in the market:

The Delivery Method element specifies the method to be used in delivering the cheque by the Debtor Agent . For example, a code CRCD is used to courier the cheque to the Creditor .

---

<!-- ELEMENT 78 -->
Min 0 - Max 1

Min 0 - Max 1

The pain.001 message introduces Ultimate Debtor and Ultimate Creditor . The Ultimate Debtor element should not be confused with an Initiating Party who may send a payment initiation request on behalf of the Debtor , for example, Payment Factory.

CBPR+ premise is that an Ultimate Debtor has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an Ultimate Creditor has no financial regulated account relationship with the corresponding Creditor.

The Ultimate Debtor and Ultimate Creditor can be identified by a combination  of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

---

<!-- ELEMENT 79 -->
The pain.001 has three optional Intermediary Agent (1,2 and 3) elements. These agents represent the agent(s) that exist between the Debtor Agent and the Creditor Agent .

- If more than one intermediary agent is present, then Intermediary Agent 1 identifies the agent between the Debtor Agent and the Intermediary Agent 2 .

- If more than two intermediary agents are present, then Intermediary Agent 2 identifies the agent between the Intermediary Agent 1 and the Intermediary Agent 3 .

- If Intermediary Agent 3 is present, then it identifies the agent between the Intermediary Agent 2 and the Creditor Agent .

More commonly  the ISO 9362 Financial  Institution Business  Identifier Code is considered the best practice de factor standard for 'many to many'  / correspondent banking  payments.

Other options to identify the Intermediary Agent include:

- Clearing System Member ID

- LEI (Legal Entity Identifier)

- Name and either structured, or unstructured Postal Address

Credit Transfer Transaction Information

Intermediary Agent 1

---

<!-- ELEMENT 80 -->
Min 0 - Max 1

The pain.001 Intermediary Agent (1,2 and 3) Accounts are used to capture the account information related to these Agents.

The Intermediary Agent Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1

Identification identifies the account maintained at the Account Servicing Institution.

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account.

Currency identifies the currency of the account.

Name identifies the name of the account as assigned by the Account Servicing Institution.

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

Credit Transfer Transaction Information

Intermediary Agent Account 1

---

<!-- ELEMENT 81 -->
Min 0 - Max 1

The Creditor Agent is a static roles in the pain.001 Customer Credit Transfer Initiation. This agent maintain  a relationship  with their customers, the Creditor .

Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

---

<!-- ELEMENT 82 -->
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

---

<!-- ELEMENT 83 -->
Min 1 - Max 1

The ISO 20022 pain messages describe the Creditor as the party whose account was credited for a transaction. The Creditor sub elements describe the Creditor in greater detail.

Mandatory Name (where a BIC identifier is not provided) by which the party is known

Nested element capturing either structured or unstructured Creditor address details.

Name

Postal Address

Note: Structured address is strongly recommended with mandatory Town Name and Country

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Optional element to capture the Creditor 's  ISO

Creditor

Country of Residence

---

<!-- ELEMENT 84 -->
Min 0 - Max 1

The pain.001 Creditor Account is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The Creditor Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency of the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

Creditor Account is not required for cheque payments.

---

<!-- ELEMENT 85 -->
Min 0 - Max 1

Min 0 - Max 1

The pain.001 message introduces Ultimate Debtor and Ultimate Creditor . The Ultimate Debtor element should not be confused with an Initiating Party who may send a payment initiation request on behalf of the Debtor , for example, Payment Factory.

CBPR+ premise is that an Ultimate Debtor has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an Ultimate Creditor has no financial regulated account relationship with the corresponding Creditor.

The Ultimate Debtor and Ultimate Creditor can be identified by a combination  of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

---

<!-- ELEMENT 86 -->
The Instruction for Creditor Agent element within the pain.001 message optionally provides information related to the processing of the payment for the Creditor Agent.

The Instruction for Creditor Agent element offers a multiplicity  of up to 2 occurrences of information. This element enables:

- the use of an embedded choice of code to describe the instruction (e.g. CHQB - Pay Creditor by Cheque)

- free format instruction information

- or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the Creditor Agent . It must be passed on throughout  the life cycle of the transaction until the payment reaches the Credit Agent .

---

<!-- ELEMENT 87 -->
# ISO 20022 Programme

# Quality data, quality payments

# CBPR+ User Handbook

SR 2023 Edition March 2023

---

<!-- ELEMENT 88 -->
Min 0 - Max 1

The Instruction for Debtor Agent element within the pain.001 message optionally provides information related to the processing of the payment.

The Instruction for Debtor Agent element offers a maximum  of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the Debtor Agent , depending  on bilateral agreement.

---

<!-- ELEMENT 89 -->
The Purpose element within the pain.001 message captures the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment, e.g., IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Debtor .

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example, LIMA is classified within the Cash Management categorisation, with the Name Liquidity Management described as a Bank initiated account transfer to support zero target balance management, pooling or sweeping.

Category Purpose also captures a high-level purpose, which unlike Purpose is less granular but can trigger special processing e.g., Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

---

<!-- ELEMENT 90 -->
The Regulatory Reporting block within the pain.001 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

# Min 0 - Max 1

The Debit Credit Reporting Indicator utilises  an embedded choice of code to indicate whether the regulatory reporting applies to the:

- DEBT (debit)

- CRED (credit)

- BOTH

# Min 0 - Max 1

The Authority element captures the Name and Country code of the Authority/Entity requiring the regulatory reporting information.

Min 0 - Max *

The Details element provides the detail on the regulatory reporting information.

Credit Transfer Transaction Information       Regulatory Reporting

Debit Credit Reporting Indicator

---

<!-- ELEMENT 91 -->
# Min 0 - Max 1

The pain.001 nested Tax element captures information  related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s).

This element caters for two main types of tax related payments:

- Tax payment obligation that is required to be transmitted with a payment

- Information that accompanies an actual payment of a tax obligation

The follow nested elements may be used to capture detailed tax information:

Taxinformation block is also available within the Structured Remittance Information block which is applicable

---

<!-- ELEMENT 92 -->
The Related Remittance Information element within the pain.001 message is nested to provide information related to the handling of remittance information.

Min 0 - Max 1

The Remittance Identification captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction.

Min 0 - Max *

The Remittance Location Details uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- Method requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email)

- Electronic Address provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.

- Postal Address provides the postal address to which an agent is to send the remittance information

Unlike CBPR+ pacs messages, in the interbank pain.001 message, Related Remittance Information and Remittance Information are non-mutually exclusive due to a corporate use case of populating both information blocks for detailing remittance advices which are part of value-added service offered by the Debtor Agent .

SCORE Guideline: If the Related Remittance Information is used, and a Remittance Identification is provided, it is recommended that the Remittance Identification equal the End To End Identification.

---

<!-- ELEMENT 93 -->
The optional Remittance Information element within the pain.001 message is nested to provide either Structured or Unstructured information  related to payment, such as invoices.

Remittance Information enables the matching/reconciliation  of an entry that the payment is intended to settle.

# Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

# Min 0 - Max *

The Structured element is nested capturing rich structured Remittance Information, and is unlimited  in its multiplicity, but must not exceed 9,000 characters of business information (does not include  the xml element identification)

The use of this nested element should  be bilaterally/multilaterally  agreed, to ensure end-toend transportation of this data.

Recommend to refer to CGI-MP Document Centre for Country

---

<!-- ELEMENT 94 -->
The bilaterally/multilaterally agreed Remittance Information which is Structured must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

---

<!-- ELEMENT 95 -->
The Creditor Reference in the Creditor Remittance Information component  in the structured remittance information  is generated by Creditor to inform the Debtor who has to include the reference in the Remittance Information component of the pain.001.

Creditor Reference in the Structured Remittance Information is based on ISO 11649

- 2 letters 'RF'

- 2 digits check digit

- 21 letters/digits  creditor reference

Facilitates STP and auto-match with the creditor reference and its account receivable

- A vendor can add the creditor reference to its invoice. When a customer pays the invoice,  they write the creditor reference instead of the invoice number in the payment message (e.g., MT 101 F70 which will be carried in MT 103)

- When the vendor receives the payment, it can auto-match the incoming credit entry and the creditor reference extracted from the statement (e.g., MT 940 F61/86)

SCORE Guideline: For Creditor Reference information, in instances where the Creditor Reference Type code is SCOR (Structured Communication Reference) and the Creditor Reference is structured in accordance with ISO 11649, the

Credit Transfer Transaction Information

---

<!-- ELEMENT 96 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g., a use case involving  a Ma rket  Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Interbank Customer Credit Transfer Initiation - Relay

Use Case pn.1.1.1 - High Level Payment Initiation  Interbank  'relay'  (pain.001)

Use Case pn.1.1.1.a  - High Level Payment Initiation  Interbank  'relay'  (pain.001)  Multi-bank  Sweep

Use Case pn.1.1.2 - High Level Payment Initiation  Interbank  'relay'  (pain.001) involving  a Payment Market  Infrastructure

# Interbank Customer Credit Transfer Initiation - Authorised  Party

Use Case pn.1.2.1 - High Level Payment Initiation  Interbank  (pain.001) by an Authorised  Party

Use Case pn.1.2.1.a.  - High Level Payment Initiation  Interbank  (pain.001) FI-Initiated  Sweep (Long position at the Secondary Account)

Use Case pn.1.2.1.b.  - High Level Payment Initiation  Interbank  (pain.001) by an Authorised Party to pay themselves as the Creditor

# Interbank Customer Credit Transfer Initiation - Financial Institution

Use Case pn.1.3.1 - High Level Payment Initiation  Interbank  (pain.001) Financial Institution  Payment Initiation

---

<!-- ELEMENT 97 -->
1

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor and initiate a credit transfer.

---

<!-- ELEMENT 98 -->
1

In the interbank relay scenario, the Forwarding Agent relaying the pain.001 message to the Debtor Agent(s) in this case to sweep excess cash from the account of the Debtor and consolidate cash for a Corporate.

1

2

3

3a

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding  a local credit transfer message pacs.008

Debtor Agent (A) provides  a status update ACSP (accepted

3b

Forwarding  Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

4

Creditor Agent (B) processes the payment and notifies Creditor of a

Initiating Party sends a payment instruction to the Forwarding Agent to sweep excess funds from its subsidiary's account to the master account with Bank B

Forwarding  Agent (F) forwards the payment instruction to the

---

<!-- ELEMENT 99 -->
1

# Market Infrastructure

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor initiate a credit transfer through a Payment Market Infrastructure.

---

<!-- ELEMENT 100 -->
In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place between the Debtor and the Debtor Agent

---

<!-- ELEMENT 101 -->
# position at the Secondary Account)

In the interbank sweep scenario, the Initiating Party (Agent I) initiates the pain.001 message to the Debtor Agent to sweep excess cash from the account of the Debtor and consolidate the cash for a Corporate.

---

<!-- ELEMENT 102 -->
# pay themselves as the Creditor.

In the Authorised Party Initiation scenario, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place to move money to themselves as the Creditor

---

<!-- ELEMENT 103 -->
# Payment Initiation

The Initiating Party (Agent I) initiates a payment from their own account with the Debtor Agent to move the funds to a non-Financial Institution Creditor

1

2

2a

3

Agent (I), the Debtor, initiates a payment request (pain.001)  to the Debtor Agent (A) to move funds from their own account

Debtor Agent (A) debits the account of Agent (I), the Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides  a status update to the Initiating Party (Agent I), based upon a bilateral

Creditor Agent (B) receives credit transfer message, credits the Creditor, and sends the camt.053 (statement) at the end of the business day to the nonFI Creditor. An optional status report is sent to the previous  Agent based upon a bilateral agreement

---

<!-- ELEMENT 104 -->
# Interbank Customer Payment Status Report

---

<!-- ELEMENT 106 -->
Interbank  Customer Payment Status Report message is sent by the Debtor Agent  to the previous agent in the payment chain. It is used to provide notification  of a rejected status, as required. The provision of a positive status is determined by a bilateral  agreement between the agents. There are three common use cases:

Relay : The pain.002 message is sent by the Debtor Agent to the Forwarding Agent which acts as a concentrating financial institution. It

---

<!-- ELEMENT 108 -->
Interbank  Customer Payment Status Report message is sent by the Debtor Agent  to the previous agent in the payment chain. It is used to provide notification  of a rejected status, as required. The provision of a positive status is determined by a bilateral  agreement between the agents. There are three common use cases:

Financial Institution  Payment Initiation (to non-FI) : The pain.002  message is sent by the Debtor Agent  to the Debtor (Financial Institution)  who requested to initiate  a payment from their account with the Debtor Agent to move funds to a non-Financial  Institution

---

<!-- ELEMENT 109 -->
Interbank  Customer Direct Debit Initiation  message is sent by the Initiating  Party to the Forwarding Agent or the Creditor Agent.  It is used to request single or bulk collection(s) of funds from one or various debtor's account(s) to a creditor.

Relay : Interbank  pain.008 message is sent by the Initiating  party (the Creditor or authorised party) to the Forwarding Agent which a cts as a concentrating financial institution. It will forward the pain.008 message to the Creditor Agent  to initiate  the direct debit instruction(s)..

---

<!-- ELEMENT 111 -->
Each ISO20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Initiation (pain) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

Each transaction's Credit Transfer Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor Agent) of the pain.002.

---

<!-- ELEMENT 112 -->
The pain.001 message Creation Date Time captures the date and time the message was created.

It is defined by ISO Date Time with mandatory date and time components expressed in the following formats:

- Universal  Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ

- Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2 nd option). Otherwise use UTC time (1 st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

---

<!-- ELEMENT 113 -->
# Min 1 - Max 1

The Initiating Party in the context of interbank payment initiation  report is always the Debtor Agent which initiates the pain.002 message. Business Identifier Code (BIC FI) is mandated to identify the Initiating Party in the pain.002 message. There are three use cases below:

- Relay : The Debtor Agent sends the pain.002 message to the Forwarding Agent which acts as a concentrating  financial  institution. It will forward the pain.002 message to the original Initiating Party who can be the Debtor themselves or the Authorised Party. This is commonly known as a relay scenario.

- Authorised Party : The Debtor Agent sends the pain.002 to the Financial  Institution  ( Initiating Party ) which has the authority to initiate a payment on behalf of the Debtor , e.g., multi-bank liquidity sweeps

- Financial Institution Payment Initiation : The Debtor Agent sends the pain.002 to the Financial  Institution which is the Debtor who initiate a payment from their account to move funds to a non-Financial Institution Creditor

---

<!-- ELEMENT 114 -->
Min 0 - Max 1

The Forwarding Agent is mandatory in a relay scenario whereby the receiver of the pain.002 message is not the original Debtor. In this case, the Initiating Party (the Debtor Agent ) has to provide Business  Identifier Code (BIC FI) of the Forwarding Agent in the pain.002 message. The Forwarding Agent acts as a concentrating financial institution and forwards the pain.002 message to the Debtor or the Initiating Party.

Other options to identify the Forwarding Agent include:

- Clearing System Member ID

- LEI (Legal Entity Identifier)

For the use case of multi-bank liquidity sweeps, Forwarding Agent is not required.

---

<!-- ELEMENT 116 -->
Min 1 - Max 1

The pain.002 Customer Payment Status Report uses elements in the Original Group Information and Status to capture the message identifier and message name of the underlying payment the Payment Status Report relates to. The mandatory Original Message Identification contains the point-to-point reference, and the mandatory Original Message Name Identification contains the message name of the underlying payment being reported upon. Optionally the Original Creation Date Time can also be captured.

For example:

Original Message Name Identification 'pain.001.001.09' confirms the Status Report is of a pain.001 Customer Credit Transfer Initiation.

Original Message Identification must transport the Message Identification of the underlying payment (e.g., pain.001).

For a relay scenario, Forwarding Agent (F) should respect the Message ID provided by the Initiating Party of the pain.001 and pain.002.

---

<!-- ELEMENT 117 -->
# Identification

Min 1 - Max 1

The pain.002 Customer Payment Status Report uses element Original Payment Information Identification , located in the Original Group Information and Status. This 35 character identifier is a point-to-point reference used to unambiguously  identify the payment information  group or batch reference if the message contains multiple  transactions.

Since the interbank pain.001 and pain.002 usage guidelines  are restricted to one single transaction, this value  is the same as the Original Message ID of the Original Group Information And Status.

---

<!-- ELEMENT 118 -->
Min 1 - Max 1

The pain.002 Customer Payment Status Report nested Transaction Information And Status element is used to capture information from the underlying payment that the Payment Status Report relates to.

Mandatory element (in addition to Original Message identification and Original Message Name Identification described on the previous pages) include:

Original End to End Identification Original UETR

The following element is optional:

Original Instruction Identification

Min 1 - Max 1

Min 1 - Max 1

Min 0 - Max 1

These Original elements enable the Initiating Party to associate the Payment Status with the payment they originally sent.

---

<!-- ELEMENT 119 -->
# Information

# Min 1 - Max 1

The pain.002 Customer Payment Status Report Transaction Status utilizes the externalized ISO Payment Transaction Status code list to provide a status update on a pain message previously received. The Transaction Status element is arguable the most significant/core parts of the pain.002 and optionally may further be complimented with Status Reason Information.

Min 0 - Max 1

The nested Status Reason Information enable the optional inclusion of:

Originator - the party that issues the status. Typically, the pain.002 Initiating Party and therefore Originator is not necessary.

Reason - which utilises an ISO external Status Reason code. For example, AC04 'Closed Account Number' would compliment a RJCT (Reject) Transaction Status.

Additional Information -a text element to provide further status reason information, necessary where the Reason code is NARR

Note: A Reason code must be provided where the Transaction Status RJCT (Reject) code is used.

---

<!-- ELEMENT 121 -->
The interbank pain.002 Customer Payment Transaction Status element facilitates updates from the Debtor Agent to the previous Agent, e.g., the Forwarding Agent or the payment originator (the Debtor / the Initiating Party )  on  changes to the status of the payment. Such Status Information messages (pain.002), with the exception of reject code RJCT which is mandatory in CBPR+ ,  are bilateral agreed, where upon a variety of these Transaction Statuses may be used by the Instructed Agent at different stages of the payment processing.

This diagram illustrates the logical order in which these codes may be used during the processing of the Payment Initiation messages (pain) and the interbank Payment Clearing And Settlement message (pacs) and the role of the Agents in providing these status.

---

<!-- ELEMENT 122 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Interbank Customer Payment Status Report - Relay

Use Case pn.2.1.1 - High Level Payment Initiation  Interbank  'relay'  status report Use Case pn.2.1.1.a  - High Level Payment Initiation  Interbank  'relay'  status report Multi-bank  Sweep Use Case pn.2.1.2 - High Level Payment Initiation  Interbank  'relay'  status report involving  a Payment Market  Infrastructure Use Case pn.2.1.3 - High Level Direct Debit Initiation  Interbank  'relay'  status report involving  a Payment Market  Infrastructure

# Interbank Customer Payment Status Report - Authorised Party

Use Case pn.2.2.1 - High Level Payment Initiation  Interbank  status report for Authorised Party Use Case pn.2.2.1.a.  - High Level Payment Initiation  Interbank  status report for FI-Initiated  Sweep (Long position at the Secondary Account) Use Case pn.2.2.1.b.  - High Level Payment Initiation  Interbank  status report for Authorised Party to pay themselves as the Creditor.

# Interbank Customer Payment Status Report - Financial  Institution

Use Case pn.2.3.1 - High Level Payment Initiation  Interbank  status report for Financial Institution  Payment Initiation

# Interbank multiple Payment Status Reports

Use Case pn.2.4.1 - High Level Payment Initiation  Interbank  'relay'  multiple status reports Use Case pn.2.4.2 - High Level Rejection of an incomplete 'relay' Payment

Use Case pn.2.4.3 - High Level Direct Debit Initiation  Interbank  'relay'  multiple status reports involving  a Payment Market  Infrastructure

---

<!-- ELEMENT 123 -->
1

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

---

<!-- ELEMENT 124 -->
# Multi-bank Sweep

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

1

1

2

3

3a

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding  a local credit transfer message pacs.008

Debtor Agent (A) provides  a status update ACSP (accepted

3b

Forwarding  Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

4

Creditor Agent (B) receives the credit transfer message, credits

Initiating Party sends a payment instruction to the Forwarding Agent to sweep excess funds from its subsidiary's account to the master account with Bank B

Forwarding  Agent (F) forwards the payment instruction to the

---

<!-- ELEMENT 125 -->
1

# a Payment Market Infrastructure

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

---

<!-- ELEMENT 126 -->
# involving a Payment Market Infrastructure

In the interbank relay scenario, the Creditor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

---

<!-- ELEMENT 127 -->
# Party

In the scenario Authorised Party Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a payment based on Debit Authorisation with the Debtor and the Debtor Agent.

---

<!-- ELEMENT 128 -->
# Party: FI-Initiated Sweep (Long position at the Secondary Account)

In the scenario Authorised Party Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a liquidity sweep on behalf of a corporate customer based on the sweep contract

1

2

3

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

- Debtor Agent (A) optionally provides  a 3a

status update to the Initiating Party (Agent I), based upon a bilateral

4

Agent I receives  intraday balance report from the Debtor Agent (A) on behalf of their mutual customer

Agent (I) initiates a sweep on behalf  of the Corporate  by sending pain.001 to the Debtor

Creditor Agent (B) receives credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous  Agent based upon a bilateral agreement

See use case p.8.1.2for a sweeping contract with a short position

---

<!-- ELEMENT 129 -->
# Party to pay themselves as the Creditor

In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place to move money to themselves as the Creditor

DA

As a pre-requisite  the Debtor provides  Debit Authorisation to Agent I to Initiate Payment from their account with the Debtor Agent (A)

- (pain.001)  to the Debtor Agent (A) to 2

Agent (I) initiates a payment request move  fund from the Debtor's account, as an authorised party, to

3

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

- Debtor Agent (A) optionally provides  a 3a

status update to the Initiating Party (Agent I), based upon a bilateral

4

Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the Debtor Agent based upon a bilateral agreement

---

<!-- ELEMENT 130 -->
# Institution Payment Initiation

In the scenario Financial Institution Payment Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a payment to a non-Financial Institution Creditor using their own account

1

Agent (I), the Debtor, initiates a payment request (pain.001)  to the Debtor Agent (A) to move funds from their own account

2

2a

3

Creditor Agent (B) receives credit transfer message, credits the Creditor, and optionally returns a status report to Debtor Agent based upon a bilateral agreement. It also sends camt.053 (statement) to the non-FI  Creditor

Debtor Agent (A) debits the account of Agent (I), the Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides  a status update to the Initiating Party (Agent I), based upon a bilateral

---

<!-- ELEMENT 131 -->
In the interbank relay scenario, the Forwarding Agent provides multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle.

---

<!-- ELEMENT 132 -->
In the interbank relay scenario, the Forwarding Agent provides multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle.

---

<!-- ELEMENT 133 -->
# (pain.002) involving a Payment Market Infrastructure

In the interbank relay scenario, the Creditor Agent sends multiple status reports to the Forwarding Agent which relays the same information to the Initiating Party.

---

<!-- ELEMENT 134 -->
# Interbank Customer Direct Debit Initiation

---

<!-- ELEMENT 135 -->
# Group Header

- Message Identification

- Initiating Party - where different from Creditor

- Forwarding Agent

# Payment Information

- Payment Information Identification

- Requested Collection Date

- Creditor

- Creditor Agent

# Direct Debit Transaction Information

- Payment Identification

- Instructed Amount

- Charge Bearer

- Mandate Identification

- Debtor Agent

- ➢

# MT Field Name & (Tag option)

# Sequence A General Information :

- Sender's Reference (Field 20)

- Instructing Party (Field 50 C or L)

Message Sender in a 'relay' scenario

# Sequence A General Information :

- Customer Specified Reference (Field 21R)

- Requested Execution Date (Field 30)

- Creditor (Field 50 A or K)*

- Creditor's Bank (Field 52 A, C or D)*

# Sequence B Transaction Details :

- Transaction Reference (Field 21)

- Currency and Transaction Amount (Field 32B)

- Details of Charges (Field 71A)

- Mandate Reference (Field 21C)

- Debtor's Bank (Field 57 A, C or D)

- ➢

---

<!-- ELEMENT 136 -->
# The pain.008 message is composed of three blocks:

- Group Header contains a set of characteristics that relates to all individual transaction.

- Payment Information contains a set of characteristics that relates to the credit side of the transaction, such as Creditor and Creditor Agent.

- Direct Debit Transaction Information contains, among others, elements related to the debit side of the transaction, such as Debtor and Debtor Agent and optionally mandate related information.

Direct Debit Initiation relay messages in a many-to-many space allow for multiple transactions as they will be typically cleared by Automated Clearing House (ACH) batch

---

<!-- ELEMENT 137 -->
Interbank  Customer Direct Debit Initiation  message is sent by the Initiating  Party to the Forwarding Agent or the Creditor Agent.  It is used to request single or bulk collection(s) of funds from one or various debtor's account(s) to a creditor.

Relay : Interbank  pain.008 message is sent by the Initiating  party (the Creditor or authorised party) to the Forwarding Agent which a cts as a concentrating financial institution. It will forward the pain.008 message to the Creditor Agent  to initiate  the direct debit instruction(s)..

---

<!-- ELEMENT 139 -->
Min 1 - Max 1

Each ISO20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For the Payment Initiation (pain) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

Each transaction's Direct Debit Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Creditor or authorized third party) of the pain.008.

---

<!-- ELEMENT 140 -->
Min 1 - Max 1

The pain.008 message Creation Date Time captures the date and time which the message was created.

It is defined by ISO Date Time with mandatory date and time components expressed in the following formats:

- Universal  Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ

- Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.008 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2 nd option). Otherwise use UTC time (1 st option). Decimal fractions of milliseconds with 3 digits are optional.

---

<!-- ELEMENT 141 -->
# Min 0 - Max 2

The pain.008 message Authorisation allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The Authorisation uses an embedded code set or free text form. It has no equivalent in the legacy MT direct debit message.

For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.

---

<!-- ELEMENT 142 -->
Min 1 - Max 1

The pain.008 message Number of Transactions captures the number of individual transaction contained within the message.

Multiple transactions are allowed in CBPR+ direct debit usage guidelines. However, it is recommended to have only one single direct debit transaction unless  bilaterally determined.

Single transactions in the CBPR+ direct debit usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant collection, supporting the next generation of innovation.

---

<!-- ELEMENT 143 -->
# Min 1 - Max 1

The Initiating Party can either be the Creditor or an Authorised Party who initiates direct debit transactions on behalf of the Creditor .  The Initiating Party can be, for example, the Head Office which is authorised by its subsidiary to request for payment amount to be collected from the Debtor .  In the centralization model, the Initiating Party can also be a payment factory or shared service  centre or third party agent, which has authority to send the message on behalf of the Creditor .

In the interbank pain.008 'Relay' message use case: The Initiating Party sends the pain.008 message to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.008 message to the Creditor Agent .

---

<!-- ELEMENT 144 -->
The Initiating Party can either be the Creditor or an authorised party, such as Financial  Institution, in the context of interbank pain.008. Sub elements describe the Initiating Party in greater detail.

Nested element capturing structured Postal Address including at least Town Name and Country if used.

Name

Mandatory Name wherePostal Address is provided.

Postal

Address

Nested element capturing the various types of identifiers, e.g. BIC, LEI etc.

Initiating

Party

Identification

Optional element to capture the Initiating Party's ISO country code

Contact

Country of

Residence

Details

---

<!-- ELEMENT 145 -->
Min 1 - Max 1

The Forwarding Agent is mandatory in a relay scenario whereby the Initiating Party (the Creditor or authorised third party) has to provide Business  Identifier Code (BICFI) of the Forwarding Agent in the pain.008 message. The Forwarding Agent acts as a concentrating financial  institution  and forwards the pain.008 message to the Creditor Agent for execution.

Other options to complement  the identity of the Forwarding Agent include:

- Clearing System Member ID

- LEI (Legal Entity Identifier)

---

<!-- ELEMENT 147 -->
The CBPR+ pain.008 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognise that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory.

As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message.

Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used.

---

<!-- ELEMENT 148 -->
The Interbank Customer Direct Debit Initiation Payment Information Identification provides a mandatory element to identify the payment information group within the message.

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions.

For a single batch in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header.

---

<!-- ELEMENT 149 -->
Min 1 - Max 1

The pain.008 message Payment Method specifies the means of payment that will be used to move the amount of money. The payment method code 'DD' Direct Debit must be used.

---

<!-- ELEMENT 150 -->
Min 0 - Max 1

The pain.008 message Batch Booking identifies whether a single entry per individual  transaction or a batch entry for the sum of the amounts of all transactions within the group of a message is requested.

Batch booking is used to request for a consolidated credit entry on the Creditor's account. Where this optional element is not used, the default of single credit entries is applied on the Creditor's account.

---

<!-- ELEMENT 151 -->
Min 1 - Max 1

The pain.008 message mandatory Requested Collection Date element, captures the date at which the creditor requests that the amount  of money is to be collected from the debtor.

It is defined by ISO Date expressed in the YYYY-MM-DD format .

---

<!-- ELEMENT 152 -->
Min 1 - Max 1

The ISO 20022 pain messages describe the Creditor as the party whose account was credited for a transaction. The Creditor sub elements describe the Creditor in greater detail.

Mandatory Name (where a BIC identifier is not provided) by which the party is known

Nested element capturing either structured or unstructured Creditor address details.

Name

Postal Address

Note: Structured address is strongly recommended with mandatory Town Name and Country

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Identification

Optional element to capture the Creditor 's  ISO

Creditor

Country of Residence

---

<!-- ELEMENT 153 -->
Min 1 - Max 1

The pain.008 Creditor Account is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The Creditor Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency of the account, recommended.

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 154 -->
The Creditor Agent is a static role in the pain.008 Customer Direct Debit Initiation. This agent maintains  a relationship  with their customers, the Creditor .

Note: Although the Creditor Agent, Debtor Agent, Creditor and Debtor all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Creditor Agent and Debtor Agent become the Statement Account Servicer and the Creditor and the Debtor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

For Agent Identification, BIC is preferred, alternatively Clearing Member

---

<!-- ELEMENT 155 -->
Min 0 - Max 1

The pain.008 Creditor Agent Account is used to capture the account information  related to the Creditor Agent.

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

Creditor Agent and Debtor Agent are Financial Institutions, therefore the nested elements Name and Proxy are unlikely to be used.

---

<!-- ELEMENT 156 -->
Min 0 - Max 1

The pain.008 optional Charges Account element, which is used to process charges associated with a transaction.

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

This element is not widely used in the payment industry.

---

<!-- ELEMENT 157 -->
Min 0 - Max 1

The pain.008 optional Charges Account Agent element, which is used to specify the agent that services a charges account.

Charges account agent should  only be used when the charges account agent is different from the creditor agent.

This element is not widely used in the payment industry.

---

<!-- ELEMENT 159 -->
# Min 1 - Max 1

The pain.008 message contains Payment Identification which provides a set of elements to identify the payment of which several are mandatory elements.

---

<!-- ELEMENT 160 -->
The pain message can be described.

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the

Min 0 - Max 1

Payment Type Information provides a set of optional elements where the payment type

Service Level Min 0 - Max 3

Payment Type Information

Anested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

Anested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, CORE is a transaction related to SEPADirect Debit Core.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

Sequence Type

Min 0 - Max 1

A nested element which uses an embedded code to identify the direct debit sequence, such as first, recurrent, final or one-off

A nested element which may either use an external ISO proprietary code. It is used to identify the category of payment.

Category Purpose code or a

---

<!-- ELEMENT 161 -->
Min 1 - Max 1

The pain.008 nested Instructed Amount element captures the amount of money to be moved between the Debtor and the Creditor before deduction of charges.

The Instructed Amount captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. This amount has to be transported unchanged through the transaction chain. This element is comparable with both the legacy Field 33B and Field 32B.

For multiple transactions, the currency must be the same for each transaction.

---

<!-- ELEMENT 162 -->
Min 0 - Max 1

The Charge Bearer element exists at the Direct Debit Transaction Information level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

Charge Bearer Code SLEV (Following Service Level) is not allowed in the CBPR+ pain.008 interbank.

---

<!-- ELEMENT 163 -->
# Direct Debit Transaction

Pre Notification

Min 0 - Max 1

The pain.008 Direct Debit Transaction component provides information  specific to the direct debit mandate.

Mandate Related Information Min 0 - Max 1

Provides further details of the direct debit mandate signed between the creditor and the debtor. E.g., Mandate Identification, Date of Signature and Electronic Signature.

Creditor Scheme Identification Min 0 - Max 1

Credit party that signs the mandate, may be used if supported by the Direct Debit Schema. (see next page for additional detail on this nested element)

Pre Notification Identification Min 0 - Max 1

Unique and unambiguous identification of the pre-notification which is sent separately from the direct debit instruction.

---

<!-- ELEMENT 164 -->
Min 0 - Max 1

The Creditor Scheme Identification element within the pain.008 message optionally provides information related to the credit party that signs the mandate who is different from the Creditor.

The Creditor Scheme  Identification element offers the following options:

Name

Postal Address: Not used often

Identification

Country of Residence

Contact Details

CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit Scheme.

---

<!-- ELEMENT 165 -->
Min 0 - Max 1

Min 0 - Max 1

The pain.008 message introduces Ultimate Creditor and Ultimate Debtor . The Ultimate Creditor element should not be confused with an Initiating Party who may send a direct debit initiation request on behalf of the Creditor , for example, Payment Factory.

CBPR+ premise is that an Ultimate Creditor has no financial regulated direct account relationship with the corresponding Creditor. Likewise, an Ultimate Debtor has no financial regulated account relationship with the corresponding Debtor.

The Ultimate Creditor and Ultimate Debtor can be identified by a combination  of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

In the context of direct debit, Ultimate Creditor and Ultimate Debtor are not commonly used.

---

<!-- ELEMENT 166 -->
Min 1 - Max 1

The Debtor Agent is a static roles in the pain.008 Customer Direct Debit Initiation. This agent maintain  a relationship  with their customers, the Debtor .

Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

---

<!-- ELEMENT 167 -->
Min 0 - Max 1

The pain.008 Debtor Agent Account is used to capture the account information related to the Debtor Agent .

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

---

<!-- ELEMENT 168 -->
Min 1 - Max 1

The ISO 20022 pain messages describes the Debtor as the party whose account was debited for a transaction. The Debtor sub elements describe the Debtor in greater detail.

Name by which the party is known

Note: it is recommended to include the Postal Address together with the Name

Nested element capturing either structured or unstructured Debtor address details.

Name

Postal Address

Note: Structured address is strongly recommended with mandatory Town Name and Country

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Optional element to capture the Debtor 's  ISO

Debtor

Country of Residence

---

<!-- ELEMENT 169 -->
Min 1 - Max 1

The pain.008 Debtor Account is used to capture the account information  for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The Debtor Account uses a variety of nested elements to capture information related to the account.

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

---

<!-- ELEMENT 170 -->
Min 0 - Max 1

Min 0 - Max 1

The pain.008 message introduces Ultimate Debtor and Ultimate Creditor . The Ultimate Debtor element should not be confused with an Initiating Party who may send a payment initiation request on behalf of the Debtor , for example, Payment Factory.

CBPR+ premise is that an Ultimate Debtor has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an Ultimate Creditor has no financial regulated account relationship with the corresponding Creditor.

The Ultimate Debtor and Ultimate Creditor can be identified by a combination  of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

In the context of direct debit, Ultimate Creditor and Ultimate Debtor are not commonly used.

---

<!-- ELEMENT 171 -->
Min 0 - Max 1

The Instruction for Creditor Agent element within the pain.008 message optionally provides information related to the processing of the direct debit.

The Instruction for Creditor Agent element offers a maximum  of 140 characters to provide further information related to the processing of the direct debit instruction, that may need to be acted upon by the Creditor Agent , depending on bilateral agreement.

---

<!-- ELEMENT 172 -->
The Purpose element within the pain.008 message captures the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment, e.g., IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Debtor .

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. For example, LOAR is classified within the Finance categorisation, with the Name Loan Repayment described as a repayment of loan to lender.

Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger special processing e.g. Category Purpose code RPRE 'Represented' may trigger a representation of previously reversed or returned direct debit transactions.

---

<!-- ELEMENT 173 -->
The Regulatory Reporting block within the pain.008 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

Min 0 - Max 1

The Debit Credit Reporting Indicator utilises  an embedded choice of code to indicate whether the regulatory reporting applies to the:

- DEBT (debit)

- CRED (credit)

- BOTH

# Min 0 - Max 1

The Authority element captures the Name and Country code of the Authority/Entity requiring the regulatory reporting information.

Min 0 - Max *

The Details element provides the detail on the regulatory reporting information.

Direct Debit Transaction Information       Regulatory Reporting

Debit Credit Reporting Indicator

---

<!-- ELEMENT 174 -->
# Min 0 - Max 1

The pain.008 nested Tax element captures information  related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s).

This element caters for two main types of tax related payments:

- Tax payment obligation that is required to be transmitted with a payment

- Information that accompanies an actual payment of a tax obligation

The follow nested elements may be used to capture detailed tax information:

Taxinformation block is also available within the Structured Remittance Information block which is applicable

---

<!-- ELEMENT 175 -->
The Related Remittance Information element within the pain.008 message is nested to provide information related to the handling of remittance information.

Min 0 - Max 1

The Remittance Identification captures a unique reference assigned by the initiating party of the direct debit to identify the remittance information sent separately from the direct debit instruction.

Min 0 - Max *

The Remittance Location Details uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- Method requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email)

- Electronic Address provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information maybe deposited or retrieved.

- Postal Address provides the postal address to which an agent is to send the remittance information

Unlike CBPR+ pacs messages, in the interbank pain.008 message, Related Remittance Information and Remittance Information are non-mutually exclusive due to a corporate use case of populating both information blocks for detailing remittance advices which are part of value-added service offered by the Creditor Agent .

---

<!-- ELEMENT 176 -->
The optional Remittance Information element within the pain.008 message is nested to provide either Structured or Unstructured information  related to payment, such as invoices.

Remittance Information enables the matching/reconciliation  of an entry that the payment is intended to settle.

# Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

# Min 0 - Max *

The Structured element is nested capturing rich structured Remittance Information, and is unlimited  in its multiplicity, but must not exceed 9,000 characters of business information (does not include  the xml element identification)

The use of this nested element should  be bilaterally/multilaterally  agreed, to ensure end-toend transportation of this data.

---

<!-- ELEMENT 177 -->
The bilaterally/multilaterally agreed Remittance Information which is Structured must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

Direct Debit Transaction Information

---

<!-- ELEMENT 178 -->
The Creditor Reference in the Creditor Reference Information component  in the structured remittance information  is generated by Creditor to allow for the identification  of the underlying  documents  and enable reconciliation  by the Creditor upon receipt of the amount  of money.

Creditor Reference in the Structured Remittance Information  can be based on ISO 11649

- 2 letters 'RF'

- 2 digits check digit

- 21 letters/digits creditor reference

By providing the Creditor Reference in the pain.008, such as invoice number for collection, it will facilitate STP and auto-match the incoming credit entry. The Creditor Reference can be extracted from the statement (e.g., camt.053 Structured Remittance information within the Transaction Details or MT 940 Field 61 or Field 86).

Equally the End-To-End Identification could perform a similar function

SCORE Guideline: For Creditor Reference information, in instances where the Creditor Reference Type code is SCOR (Structured Communication Reference) and the Creditor Reference is structured in accordance with ISO 11649, the

---

<!-- ELEMENT 179 -->
Use case should be considered as a principle example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Interbank Customer Direct Debit Initiation - Relay

Use Case pn.8.1.1 - High Level Direct Debit Initiation  Interbank  'relay'  (pain.008) Use Case pn.8.1.2 - High Level Direct Debit Initiation  Interbank  'relay'  (pain.008) involving  a Payment Market  Infrastructure

---

<!-- ELEMENT 180 -->
In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collections of funds from the debtor's accounts for a creditor.

---

<!-- ELEMENT 181 -->
# Payment Market Infrastructure

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collection of funds from the debtor's accounts for a creditor (through a Payment Market Infrastructure).

---

<!-- ELEMENT 182 -->
# messages

---

<!-- ELEMENT 183 -->
# Payments

pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer

pacs.009 - Financial Institution Credit Transfer

pacs.009 (cov)

- Financial Institution 'Cover' Credit Transfer

pacs.009 (adv) -

Financial Institution 'advice' of Credit Transfer

# Payment Rejection and Return

pacs.002

- Financial Institution To Financial Institution Payment Status Report pacs.004 - Payment Return

# Direct Debit Payments

pacs.010 - Interbank Direct Debit pacs.010 (col) -

Interbank Direct Debit Margin Collection pacs.003 - Financial Institution to Financial Institution Customer Direct Debit

---

<!-- ELEMENT 184 -->
Financial Institution to Financial Institution Customer Credit Transfer

---

<!-- ELEMENT 186 -->
The Financial Institution To Financial Institution Customer Credit Transfer message is sent by the Debtor Agent to the Creditor Agent, directly or through other agents and/or a payment clearing and settlement system.

---

<!-- ELEMENT 188 -->
# Min 1 - Max 1

Each ISO 20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's Credit Transfer Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR(UniqueEnd-to-endTransactionReference)

---

<!-- ELEMENT 189 -->
The pacs.008 message Creation Date captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 190 -->
The pacs.008 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 191 -->
The pacs.008 Settlement Method element within the Group Header Settlement Information , includes one of the embedded codes to indicate how the payment message will be settled.

D

2 7

The Settlement Method element in the pacs.008 allows a choice of an embedded code.

COVE indicate this Customer Credit Transfer will be settlement using a covering pacs.009 (COV). The Agents being used in the covering payment to reimburse the Instructed Agent can be provided in the dedicated Reimbursement Agent elements. This allows the Instructed Agent to identify the debit account on their books from the Reimbursement Agent account or look up the account related to the reimbursement agent.

INDA indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated Settlement Account element.

INGA indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in

---

<!-- ELEMENT 192 -->
D 2 7 The pacs messages introduce the Settlement Method element within the Group Header Settlement Information . Settlement refers to the Agent whose role is to act as an Account Servicing Institution i.e. owns the account and provides service to the customer (Account Owner).

TheAccountOwnercan be an Agent or anotherParty.

Traditionally an interbank account relationship may have been referred to as a Nostro/Vostro relationship or an Agent's account held on another Agent's books/ another Agent's account held on my books.

Typically the commonality of this can be simplified to the Agent who provides the official Account statement is servicing the account and therefore is the Agent responsible for performing the settlement.

# Why is it so important to understand which Agent Services the account ?

In ISO 20022, much like the legacy FIN process, each leg of a payment has a settlement component. Commonly one of these settlement legs occurs over a Market Infrastructure, who typically owns or instructs the settlement between the two Market Infrastructure participant Agents at a national Central Bank. In this case the Central Bank services both the Instructing Agent and Instructed Agent accounts which is represented by CLRG in the Settlement Method of a pacs message.

In a number of business Use Cases there are examples of additional legs, which may occur prior to or after a potential Market Infrastructure, where an Agent is responsible for the role to service an account and perform settlement of that leg.

---

<!-- ELEMENT 193 -->
D 2 7 If we simplify a point-to-point message leg and look at when it is settled (booked using traditional language) we can ask ourselves: is the Instructing Agent's account held (serviced) on the books of the Instructed Agent or is the Instructing Agent holding (servicing) the account of the Instructed Agent.

Depending on the answer to this question, this determines the Settlement Method in a serial payment process.

Where the IN structin G A gent services the account and is responsible for settling the payment leg, the Settlement Method code INGA is used.

Where the IN structe D A gent services the account and is responsible for settling the payment leg, the Settlement Method code INDA is used.

---

<!-- ELEMENT 194 -->
The relationship between the settlement of a payment leg and the message process flow is an important one. The state of settlement influences further messages in the process flow.

The pacs message sent by the Instructing Agent to the Instructed Agent has already been settled. Instructing Agent may (for example) send

- a pacs.002 to the Previous Agent with status ACSC Accepted Settlement Complete.

- a camt.053 Customer Statement to the Instructed Agent (as Account Owner)

Instructed Agent can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the Instructed Agent must result in a pacs.004 Payment Return (which in turn triggers a Reverse Indicator on the Account Owners statement). Creditor Agent having performed the settlement on the Creditor's account, camt reporting message may be used to report or notify on this credit entry.

The pacs message sent by the Instructing Agent to the Instructed Agent has not been settled. Instructing Agent may (for example) send

- a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress

# Instructed Agent may

- Reject the pacs message received, using a pacs.002, as it has not been settled.

- a camt.053 Customer Statement to the Instructing Agent (as Account Owner) Although an rejected entry will not appear in the camt.053 Creditor Agent of a pacs.009 (particularly in the cover scenario) may forward the pacs.009 to the Creditor, as the Creditor will perform the settlement (they are the Account Servicing Institution)

The pacs message sent by the Instructing Agent to the Instructed Agent has not been settled. Settlement is performed by the Market Infrastructure. Instructing Agent may (for example) send

- a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress

# Instructed Agent may

- can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the Instructed Agent must result in a pacs.004 Payment Return.

D

2 7

---

<!-- ELEMENT 197 -->
The pacs.008 message Settlement Account is a nested element as part of Settlement Information, this element identifies information related to an account used to settle the payment instruction.

Min 0 - Max 1

The Settlement Account identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the Settlement Method )

Min 1  - Max 1

Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Account Servicing Institution

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 198 -->
The pacs message captures a number of Reimbursement Agents as a sub element to Settlement Information these elements detail the Agent in the cover method who will process the pacs.009 cover.

These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as The Instructing Reimbursement Agent, Instructed Reimbursement Agent and Third Reimbursement Agent. Each of these reimbursement agents also has a dedicated account element to optionally capture their related account details.

Min 0 - Max 1

The Instructing Reimbursement Agent captures the Agent who will execute a covering payment (i.e. pacs.009 COV or domestic equivalent) often referred to as the currency correspondent. This optional element is comparablewith the Field 53a in the legacy FIN message.

# Min 0 - Max 1

The Instructing Reimbursement Agent Account captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 53.

---

<!-- ELEMENT 199 -->
Min 0 - Max 1

The Instructed Reimbursement Agent captures the Agent who will receive the covering payment (i.e., pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer Instructed Agent . This optional element is comparable with the Field 54a in the legacy FIN message.

Min 0 - Max 1

The Instructed Reimbursement Agent Account captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 54.

Min 0 - Max 1

The Third Reimbursement Agent captures an additional Agent who will receive the covering payment, where this is not the Agent detailed in the Instructed Reimbursement Agent . This optional element is comparable with the Field 55a in the legacy FIN message.

Min 0 - Max 1

The Third Reimbursement Agent Account captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 55.

---

<!-- ELEMENT 201 -->
Min 1 - Max 1

The pacs message Payment Identification provides a set of elements to identify the payment, of which several are mandatory elements

---

<!-- ELEMENT 202 -->
Min 1 - Max 1

The pacs message Payment Identification also provides a set of optional elements to identify the payment.

---

<!-- ELEMENT 203 -->
The pacs message can be described.

# Min 0 - Max 1

# Payment Type Information provides a set of optional elements where the payment type

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point Instruction Priority Min 0 - Max 1 information may be used by the Instructed Agent to differentiate the processing priority.

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS

Clearing Channel Min 0 - Max 1

# Payment Type Information

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed* service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Customer Credit Transfer similarly to Field 111 value 001 in the MT 103

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group(captured in the code list)

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- ELEMENT 204 -->
The pacs.008 message has two key element to capture the amount of the Credit Transfer, Interbank Settlement Amount and Interbank Settlement Date

Min 1 - Max 1

Interbank Settlement Amount

Min 1 - Max 1

A mandated currency amount moved between the Instructing Agent and the Instructed Agent. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

Interbank Settlement Date

A mandated date on which the Interbank Settlement should be executed between the Instructing Agent and the Instructed Agent. This therefore is the value date comparable with the MT Field 32A

Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important one. Instructed Amount relates to the amount Instructed to be executed from the Debtor's account and only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not

---

<!-- ELEMENT 205 -->
The pacs.008 message has three optional elements to capture the optional information  related to the settlement of the instructions.

Min 0 - Max 1

The Settlement Priority provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused with the Instruction Priority.

Note: where Settlement Method of the pacs.008 is 'COVE' (settled via a covering pacs.009 COV) Settlement Priority is relevant to the covering payment not the pacs.008

Min 0 - Max 1

The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time .

Min 0 - Max 1

The Settlement Time Request optionally captures the time settlement is requested for the payment instruction by the Instructing Agent.  This Time can be capture in four nested elements:

- CLS Time the time the amount must be credit to CLS Bank

- Till Time the time until which the payment may be settled

---

<!-- ELEMENT 206 -->
# Min 0 - Max 1

The Instructed Amount captures currency and amount instructed by the Debtor. This conditional element is required when the Interbank Settlement Amount is not the same currency and/or amount as originally instructed by the Debtor. For example, a charge is taken, or the transactions is convertedto another currency. This element is comparable with the legacy Field 33B.

# Min 0 - Max 1

The Exchange Rate capture the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency.

As a best practice to provide consistency and transparency the Exchange Rate used to convert the Instructed Amount (base currency) to the Interbank Settlement Amount (quote currency) should use the Instructed currency as the whole unit to perform the exchange.

For example if Instructed Amount currency is CAD and the Interbank  Settlement currency is USD the rate should reflected as 0.83 (CAD 1 equals USD 0.83)

Note: a number of Cross Element Rules exist which relate to the Instructed

---

<!-- ELEMENT 207 -->
Min 1 - Max 1

The mandated Charge Bearer element uses an embedded code that is used to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

Note: Charge Bearer codeSLEV applies following rules agreed as part of a bilateral agreed Service Level or as part of a scheme (commonly used in Instant Payment schemes) This code has no equivalent in legacy MT messages. SLEV is removed from CBPR+ usage guideline specifications for the beginning of the

---

<!-- ELEMENT 208 -->
Min 0 - Max *

The Charges Information element provides information  on the charges to be paid by the Charge Bearer . This element is comparable with MT Fields: 71F 'Senders Charges' and 71G 'Receiver's Charges'

In addition to the legacy MT message the pacs.008 Charge Information mandate the Agent, this represent the Agent for who the Charges are either; due (pre-paid charges) or has taken a charge (deduct from the transaction)

CBPR+ best practice recommends the use of the structured Agent BIC.

As the Charges Information element is repetitive it can capture charges related to previous legs of the payment transaction.

Note: As the Charge Information element has the capability to capture both charges deducted and charges included i.e. pre-paid charges, the use of the Interbank Settlement Amount and Instructed Amount elements play an important role.

Also note: If Charge Bearer DEBT is provided only one optional occurrence of pre-paid charges is allowed.

---

<!-- ELEMENT 209 -->
# charges

---

<!-- ELEMENT 210 -->
1

# of charges

2

3

Debtor requests a payment for USD 100 specifying  any charges will be borne by them, in accordance with their banking agreement.

Pre-payment of charges are identified by the instructed Agent by the inclusion of their BIC in the Charge Information  Agent element of the payment

Debtor Agent executes the USD 100 payment including a previous  negotiated pre-payment of charges (USD 30). The Debtor is debited for USD 100 plus the Charges in accordance with their account agreement.

Agent B identifies the pre-payment of charges by the inclusion of their BIC in the Charge  Information  Agent element. Removing  charge (USD 30), they forward the payment to the next Agent. The  next Agent many request a charge.

USD 100

Ammount

Charge Bearer

Code

DEBT

---

<!-- ELEMENT 211 -->
1

# of multiple charges

2

3

4

Debtor requests a payment for USD 100 specifying  any charges will be taken by them, in accordance with their banking agreement.

Pre-payment of charges are identified by the instructed Agent by the inclusion of their BIC in the Charge Information  Agent element of the payment

Debtor Agent executes the USD 100 payment including a previous  negotiated pre-payment of charges (USD 30). The Debtor is debited for USD 100 plus the Charges in accordance with their account agreement.

Agent B identifies the pre-payment of charges by the inclusion of their BIC in the Charge  Information  Agent element. Removing  charge (USD 30), they forward the payment, including USD 20 of prepayment of charges of the next Agent.

Agent C identifies the pre-payment of charges by the inclusion of their BIC in the Charge Information  Agent element. Removing  this pre-payment of charges they forward  the payment to the Next Agent and indicate they will bear the cost of any charge claims.

Interbank Senlement

USD 100 USD 100

Charge Bearer Charge Bearer

Code Code

DEBT DEBT

---

<!-- ELEMENT 212 -->
ISO 20022 pacs.008 message standards document 'If ChargesInformation is present, then the currency of ChargesInformation/ChargesAmount  is recommended to be the same as the currency of InterbankSettlementAmount'

ISO 20022 does not prevent Charges from being booked in a different currency, but for transparency the Charge should be represented within the Charge Information in the Interbank Settlement Amount Currency.

---

<!-- ELEMENT 213 -->
# charges

---

<!-- ELEMENT 214 -->
The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 - Max 1

The Previous Instructing Agent 1 captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message.

Min 0 - Max 1

The Previous Instructing 1 Account captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message

Min 0 - Max 1

The Previous Instructing 2 captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.

Min 0 - Max 1

The Previous Instructing 2 Account captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

The Previous Instructing 3 captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN

message.

Min 0 - Max 1

---

<!-- ELEMENT 215 -->
Instructing Agent and Instructed Agent elements are required in all pacs messages and are only available in the Credit Transfer Information

---

<!-- ELEMENT 216 -->
# Intermediary Agents

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. Intermediary Agent is an example of this, where these agents are classified in numeric order (i.e. Intermediary Agent 1 ) Previous Instructing Agent however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment.

Thebelowdiagramvisualizes the change of Agent role at different stages of the payment transaction life cycle.

---

<!-- ELEMENT 217 -->
The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 - Max 1

The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 - Max 1

The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

# Min 0 - Max 1

The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

---

<!-- ELEMENT 218 -->
# authority to instruct payment from their Headquarter (HQ) settlement account.

Usually a serial payment is instructed through each Agent in a serial process. In some circumstances a branch of an Institution (Agent A) may be given Debit Authority to instruct payment from their Headquarters (Agent HQ) account with its currency correspondent (Agent B). In much the same way as if this had occurred serially, it is important that the payment instructed by Agent B correctly reflect Agent HQ as an Agent participating in the transaction, particularly if the payment is returned.

---

<!-- ELEMENT 219 -->
The pacs.008 message introduces ultimate parties to the FI to FI Customer Credit Transfer message. The Ultimate Debtor element should not be confused with an Initiating Party who may send a payment initiation request on behalf of the Debtor. (see dedication section on Initiating Party )

Min 0 - Max 1

- CBPR+ premise is that an Ultimate Debtor has no financial regulated direct account relationship  with the corresponding Debtor .

Min 0 - Max 1

- CBPR+ premise is that an Ultimate Creditor has no financial regulated direct account relationship  with the corresponding Creditor .

An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor depending on the payment scenario)

# Credit Transfer Transaction Information

---

<!-- ELEMENT 220 -->
# Debtor

An individual walks into a Money Transfer Bureau with relevant Private Identification (e.g. a passport) and requests a payment to be paid on their behalf to a Creditor. Having accepted payment for the transaction, the Money Transfer Bureau executes a payment initiation request to their Agent (Bank) as the Debtor, on behalf of the individual who is represented as the Ultimate Debtor.

---

<!-- ELEMENT 221 -->
# Creditor

A payments is initiated to credit a retirement care facility to pay the fees of one of its residents. The retirement facility is the Creditor of the payment transaction, whereby the resident of the facility is represented as the Ultimate Creditor (beneficiary of the services the fee is paying for)

---

<!-- ELEMENT 222 -->
Min 0 - Max 1

Min 1 - Max 1

The Initiating Party of a payment is often the Debtor themselves and therefore this optional element is not necessary. More often the Initiating Party is a third party providing payment initiation services on behalf of the Debtor (often referred to as a Third Party Provider) whereby the Debtor maintains an account with the Debtor Agent but the Third Party Provider has authority to initiate payment on behalf of the Debtor . This is distinctly different from an Ultimate Party (such as Ultimate Debtor ) who instructs the Debtor to initiate a payment on their behalf.

In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the Initiating Party is often the Creditor , however the same context of a Third Party Provider can exist where the third party is responsible for collecting funds on behalf of the Creditor .

---

<!-- ELEMENT 223 -->
The ISO 20022 pacs messages describe the party debited for a transaction as the Debtor . The Debtor sub elements describe the Debtor in greater detail.

Mandatory Name (where a BIC identifier is not provided) by which the party is known

Nested element capturing either structured or unstructured Debtor address details

Name

Postal

Address

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Identification

Optional element to capture the Debtor's ISO

Debtor

Country of

Residence

---

<!-- ELEMENT 224 -->
Min 0 - Max 1

The pacs.008 Debtor Account is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The Debtor Account uses a variety of nested elements to capture information related to the account.

Min 1  - Max 1

Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Currency identifies the currency of the account

Name identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 225 -->
# MT - free format option

:50K:/BE3000121637141

JOHN HECTOR JOSEPH SMITH - MASTERSO HOOGSTRAAT 6 BRUSSELS 1000 BELGIUM PASSPORT 1111111111

# MT - structured option with risk of potential truncation & loss of info

:50F:/BE3000121637141

1/JOHN HECTOR JOSEPH SMITH - MASTER

1/SONS

- 2/HOOGSTRAAT 6

- 3/BE/BRUSSELS 1000

---

<!-- ELEMENT 226 -->
Min 1 - Max 1

Min 1 - Max 1

The Debtor Agent and Creditor Agent are static roles in the pacs.008 FI to FI Customer Credit Transfer. These agent maintain  a relationship with their customers; the Debtor and Creditor .

Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the pacs messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

---

<!-- ELEMENT 227 -->
# Account

Min 0 - Max 1

The pacs.008 Debtor Agent Account and Creditor Agent Account are used to capture the account information  related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The Debtor Agent Account and Creditor Agent Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1

Min 0 - Max 1

Identification identifies the account maintained at the Account Servicing Institution Type uses the external Cash Account Type code list to identify the type of account Currency identifies the currency of the account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Name identifies the name of the account as assigned by the Account Servicing Institution

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 228 -->
The ISO 20022 pacs messages describe the party credited for a transaction as the Creditor . The Creditor sub elements describe the Creditor in greater detail.

Mandatory Name (where a BIC identifier is not provided) by which the party is known

Nested element capturing either structured or unstructured Creditor address details

Name

Postal

Address

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Identification

Optional element to capture the Creditor's ISO

Creditor

Country of

Residence

---

<!-- ELEMENT 229 -->
Min 0 - Max 1

The pacs.009 Creditor Account is used to capture the account information  for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The Creditor Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1

Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 230 -->
# Account

Min 0 - Max 1

The pacs.008 Debtor Agent Account and Creditor Agent Account are used to capture the account information  related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The Debtor Agent Account and Creditor Agent Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1

Min 0 - Max 1

Identification identifies the account maintained at the Account Servicing Institution Type uses the external Cash Account Type code list to identify the type of account Currency identifies the currency of the account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Name identifies the name of the account as assigned by the Account Servicing Institution

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 231 -->
The Instruction for Next Agent and Instruction for Creditor Agent elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

# Min 0 - Max 2

The Instruction for Creditor Agent element offers a multiplicity  of up to 2 occurrences of information. This element enables:

- the use of 2 embedded codes to describe the instruction

- free format instruction information

- or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the Creditor Agent . It must be passed on throughout  the life cycle of the transaction until the payment reaches the Credit Agent .

# Min 0 - Max 6

The Instruction for Next Agent element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format instruction information in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

---

<!-- ELEMENT 232 -->
The Purpose element within the pacs.008 FI to FI Customer Credit Transfer captures the reason for payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment e.g. etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Debtor.

the IVPT Invoice Payment, FEES Payment of Fees

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example: GDSVis classified within the Commercial categorisation, with the Name Purchase Sale of Goods and Services described as a Transaction is related to purchase and sale of goods.

Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger special processing e.g. Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

---

<!-- ELEMENT 233 -->
The Regulatory Reporting element within the pacs.008 FI to FI Customer Credit Transfer is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

# Min 0 - Max 1

The Debit Credit Reporting Indicator utilises  an embedded choice of code to indicate whether the regulatory reporting information applies to the:

- DEBT (debit)

- CRED (credit) or

- BOTH

# Min 0 - Max 1

The Authority element captures the Name and Country code of the Authority/Entity requiring the regulatory reporting information.

Min 0 - Max * The Details element provides the detail on the regulatory reporting information.

---

<!-- ELEMENT 234 -->
The Related Remittance Information element within the pacs.008 FI to FI Customer Credit Transfer is nested to provide information related to the handling of remittance information. This information is typically provided by the Debtor in the payment initiation request.

Min 0 - Max 1

The Remittance Identification captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction.

# Min 0 - Max 2

The Remittance Location Details uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- Method requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email)

- Electronic Address provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.

- Postal Address provides the postal address to which an agent is to send the remittance information

Remittance advices are typically considered as a traditional value added service provided by the Debtor Agent to the Debtor, in order to provide Remittance Information to the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting messages.

Remittance Information is a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022. Related Remittance Information and Remittance Information are mutually exclusive (can't both be present)

---

<!-- ELEMENT 235 -->
The optional Remittance Information element within the pacs.008 FI to FI Customer Credit Transfer is nested to provide either Structured or Unstructured information  related to payment, such as invoices.

Min 0 - Max 1

Remittance Information enable the matching/reconciliation  of an entry that the payment is intended to settle

Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Min 0 - Max *

The Structured element is nested capturing rich structured Remittance Information, and is unlimited  in its multiplicity, but must not exceed 9,000 characters of business information  (does not include the xml element identification)

The use of this nested element should  be bilaterally/multilaterally end-to-end transportation of this data.

Related Remittance Information and Remittance Information are agreed, to ensure

---

<!-- ELEMENT 236 -->
The bilaterally/multilaterally agreed Remittance Information which is Structured must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

Credit Transfer Transaction Information

---

<!-- ELEMENT 237 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Serial Financial Institution to Financial Institution to Customer Credit Transfer

Use Case p.8.1.1 - High Level FI to FI Customer Credit Transfer (pacs.008) settled over a Payment Market  Infrastructure

Use Case p.8.1.2 - High Level FI to FI Customer Credit Transfer (pacs.008) Sweeps (Short position at the Secondary Account)

# Cover Method Financial  Institution to Financial Institution to Customer Credit Transfer

Use Case p.8.2.1 - High Level FI to FI Customer Credit Transfer settled using the cover method (pacs.009 COV) over a Payment Market Infrastructure

Use Case p.8.2.2 - High Level FI to FI Customer Credit Transfer involved  a serial leg into a cover method (pacs.009 COV)

Use Case p.8.2.3 - High Level FI to FI Customer Credit Transfer involved  a serial leg in and out of a cover method (pacs.009 COV)

Use Case p.8.2.4 - High Level FI to FI Customer Credit Transfer involved  a serial leg out of a cover method (pacs.009 COV)

---

<!-- ELEMENT 238 -->
# Market Infrastructure

---

<!-- ELEMENT 239 -->
# Authorised Party

DA

2

As a pre-requisite  the Debtor provides  Debit Authorisation to Agent I to Initiate Payment from their account with the Debtor Agent (A)

Agent (I) initiates a payment request (pain.001)  to the Debtor Agent (A) to move fund  from the Debtor's account, as an

3

3a

4

Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

Debtor Agent (A) optionally provides  a status update to the Initiating Party (Agent I), based upon a bilateral

Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous  Agent based upon a bilateral agreement

See use case pn.1.2.1 for an Authorised Party Payment.

---

<!-- ELEMENT 240 -->
1

2a

Debtor Agent (A) initiates a payment using the cover  method to the Creditor  Agent (D)

2b

In parallel the Debtor Agent (A) initiates a covering  payment to credit the account of Agent (D) with their correspondent  (Agent

# (pacs.009 COV) over a Payment Market Infrastructure

1

2a

2b

A

Debtor initiates a payment instruction to the Debtor Agent

3

B

pacs.009 cov pacs.002

Settlement Complete

Agent B processes the payment on Agent C, via the Payment

3

pacs.008

pacs.002

4

4

5

pacs.009 cov

C

Payment Market Infrastructure, settles the payment between  Agent B and Agent C as direct participants of the Market Infrastructure,  and provides  a settlement confirmation  to Agent B

Agent C receives  the payment and

5

6

6

Agent C produces an end of day account statement report. An optional real time notification e.g. advice  of credit may have  also been created at the time of the credit posting

7

D

7

Agent D reconciles the covering funds and credits the account of the Creditor, and may optionally provide  a notification e.g. credit

---

<!-- ELEMENT 241 -->
4

6

Debtor Agent (A) initiates a payment using the serial method towards the Creditor Agent (E)

3a

Agent B initiates a payment using the cover  method towards the Creditor Agent (E) by sending a direct pacs.008 to Agent E who they have  business

3b

In parallel the Agent (B) initiates a covering  payment to credit the account of Agent (E) with their correspondent (Agent D)

Agent E receives  the payment instruction and credits the account of the Creditor, and may optionally provide  a notification e.g. credit notification. Alternatively, they may have  chosen to await until settlement occurred in Step 6 based upon their

Agent D receives  the payment and credits the account of Agent E. Agent D produces an end of day account statement report. An optional real time notification e.g. advice  of credit may have  also been created at the time of the credit

---

<!-- ELEMENT 242 -->
# of a cover method (pacs.009 COV)

1

Debtor initiates a payment instruction to the Debtor Agent

2

Debtor Agent (A) initiates a payment using the serial method towards the Creditor Agent (F)

1

2

pacs.008

pacs.002

3a

Agent B initiates a payment using the cover  method towards the Creditor Agent (F) by sending a direct pacs.008 to Agent E who they have  business relationship with.

3b

In parallel the Agent (B) initiates a covering  payment to credit the account of Agent (E) with their correspondent

3a

3b

B

C

5

4

5

pacs.008

pacs.002

pacs.009 cov pacs.002

D

Agent E receives  the payment instruction and process the payment on to Agent F. Alternatively they may have  chosen to await until settlement occurred in Step 6 based upon their risk appetite.

Agent C processes the payment on Agent D, using a correspondent

6

E

4

pacs.008

pacs.002

F

6

Agent D receives  the payment and credits the account of Agent E. Agent D produces an end of day account statement report. An optional real time notification e.g. advice  of credit may have  also been created at the time of the credit posting

7

7

Agent F receives the payment and credits the account of the Creditor, and may optionally provide  a notification e.g. credit notification.

---

<!-- ELEMENT 243 -->
2b

In parallel the Agent (A) initiates a covering  payment to credit the account of Agent (D) with their correspondent (Agent C)

- 3

Agent D receives  the payment instruction and process the payment on to Agent E. Alternatively they may have  chosen to await until settlement occurred in Step 6 based upon their

4

5

6

Agent C receives  the payment and credits the account of Agent D. Agent C produces an end of day account statement report. An optional real time notification e.g. advice  of credit may have  also been created at the time of the credit posting

1

2a

Debtor Agent (A) initiates a payment using the cover method towards the Creditor Agent (E) by sending a direct pacs.008 to Agent D who they

Debtor initiates a payment instruction to the Debtor Agent

Agent E receives  the payment and credits the account of the Creditor, and may optionally provide  a notification e.g. credit notification.

Agent B processes the payment on Agent C, using a correspondent

---

<!-- ELEMENT 244 -->
Financial Institution to Financial Institution Customer Credit Transfer

---

<!-- ELEMENT 246 -->
The Financial Institution To Financial Institution Customer Credit Transfer message is sent by the Debtor Agent to the Creditor Agent, directly or through other agents and/or a payment clearing and settlement system.

---

<!-- ELEMENT 247 -->
The pacs.008 STP message has enhance STP feature over and above the pacs.008 and legacy MT 103 STP . At a high level the key difference between the pacs.008 and pacs.008 STP are summarized.

---

<!-- ELEMENT 248 -->
# Financial Institution Credit Transfer

---

<!-- ELEMENT 250 -->
The Financial Institution Credit Transfer message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a debtor account to a creditor,

---

<!-- ELEMENT 252 -->
# Min 1 - Max 1

Each ISO 20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's Credit Transfer Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR(UniqueEnd-to-endTransactionReference)

---

<!-- ELEMENT 253 -->
The pacs.009 message Creation Date captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 254 -->
The pacs.009 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 255 -->
The pacs.009 Settlement Method element within the Group Header Settlement Information , includes one of the embedded codes to indicate how the payment message will be settled.

D

2 7

The SettlementMethod element in the pacs.009 allows a choice of an embedded code.

INDA indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated Settlement Account element.

INGA indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in

---

<!-- ELEMENT 256 -->
The pacs.009 message Settlement Account is a nested element as part of Settlement Information, this element identifies information related to an account used to settle the payment instruction.

Min 0 - Max 1

The Settlement Account identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the Settlement Method )

Min 1  - Max 1

Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Account Servicing Institution

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 258 -->
Min 1 - Max 1

The pacs message Payment Identification provides a set of elements to identify the payment, of which several are mandatory elements

---

<!-- ELEMENT 259 -->
Min 1 - Max 1

The pacs message Payment Identification also provides a set of optional elements to identify the payment.

---

<!-- ELEMENT 260 -->
The pacs message can be described.

# Min 0 - Max 1

# Payment Type Information provides a set of optional elements where the payment type

Instruction Priority Min 0 - Max 1

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS

Payment Type Information

A nested element which may either use an external ISO Service Level code* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group(captured in the code list)

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- ELEMENT 261 -->
The pacs.009 message (unlike  the pacs.008) has only one element to capture the amount  of the Credit Transfer, Interbank Settlement Amount .

Min 1 - Max 1

Interbank Settlement Amount

Interbank Settlement Date

A mandated currency amount moved between the Instructing Agent and the Instructed Agent. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

# Min 1 - Max 1

A mandated date on which the Interbank Settlement should be executed between the Instructing Agent and the Instructed Agent. This therefore is the value date comparable with the MT Field 32A

Note: the Financial Institution Credit Transfer (pacs.009) has no Instructed Amount element, Exchange Rate or Charger Bearer (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain

---

<!-- ELEMENT 262 -->
# Request

The pacs.009 message has three optional elements to capture the optional information  related to the settlement of the instructions.

Min 0 - Max 1

The Settlement Priority provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused with the Instruction Priority.

Note: Where the Settlement Method of the pacs.009 is 'INDA' (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code 'INGA' implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary.

Min 0 - Max 1

The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time .

Min 0 - Max 1

The Settlement Time Request optionally captures the time settlement is requested for the payment instruction by the Instructing Agent.  This Time can be capture in four nested elements:

- CLS Time the time the amount must be credit to CLS Bank

- Till Time the time until which the payment may be settled

---

<!-- ELEMENT 263 -->
The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 - Max 1

The Previous Instructing Agent 1 captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message.

Min 0 - Max 1

The Previous Instructing Agent 1 Account captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message

Min 0 - Max 1

The Previous Instructing Agent 2 captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.

Min 0 - Max 1

The Previous Instructing Agent 2 Account captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

The Previous Instructing Agent 3 captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message. Min 0 - Max 1

The Previous Instructing Agent 3 Account captured the account related between this Agent and Previous

---

<!-- ELEMENT 265 -->
# Intermediary Agents

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. Intermediary Agent is an example of this, where these agents are classified in numeric order (i.e. Intermediary Agent 1 ) Previous Instructing Agent however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment.

Thebelowdiagramvisualizes the change of Agent role at different stages of the payment transaction life cycle.

---

<!-- ELEMENT 266 -->
The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 - Max 1

The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 - Max 1

The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

# Min 0 - Max 1

The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

---

<!-- ELEMENT 267 -->
The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the Debtor . The Debtor sub elements describe the Debtor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Debtor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Debtor structured or unstructured

BICFI

Debtor

Postal

Address

---

<!-- ELEMENT 268 -->
Min 0 - Max 1

The pacs.009 Debtor Account is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The Debtor Account uses a variety of nested elements to capture information related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 269 -->
Min 0 - Max 1

Min 0 - Max 1

The Debtor Agent and Creditor Agent are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain  a relationship with their customers; the Debtor and Creditor . However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial  Institutions) maintain  a direct Nostro/Vostro account relationship.

Note: Where the Debtor and Creditor maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the Creditor Agent element to align with translation from the legacy MT message.

---

<!-- ELEMENT 270 -->
# Account

The pacs.009 Debtor Agent Account and Creditor Agent Account is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The Debtor Agent Account and Creditor Agent Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 271 -->
The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the Creditor . The Creditor sub elements describe the Creditor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Creditor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Debtor structured or unstructured

BICFI

Creditor

Postal

Address

---

<!-- ELEMENT 272 -->
The pacs.009 Creditor Account is used to capture the account information  for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The Creditor Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 273 -->
The Instruction for Next Agent and Instruction for Creditor Agent elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

Min 0 - Max 2

The Instruction for Creditor Agent element offers a multiplicity  of up to 2 occurrences of information. This element enables:

- the use of 2 embedded codes to describe the instruction

- free format instruction information

- or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the Creditor Agent . It must be passed on throughout  the life cycle of the transaction until the payment reaches the Credit Agent .

The Creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) Instruction for Creditor Agent, Instruction Information element preceded by /UDLC/ (UnDerLying Creditor) to provide party transparency in the settlement message.

Min 0 - Max 6

Credit Transfer Transaction Information The Instruction for Next Agent element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format instruction information in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

---

<!-- ELEMENT 274 -->
An Instruction for Creditor Agent elements within the pacs.009 Financial Institution Credit Transfer, used to settle a pacs.009 Financial Institution Credit Transfer Advice (ADV), provides information related to the Creditor in the advice message (Underlying Creditor).

The Creditor of the pacs.009 ADV are commonly captured in one of the following ways:

- As a BIC ( BICFI )  either  on its own, or

- As a Clearing System Member Identification or a LEI with Name ,  and Postal Address

pacs.009 Instruction for Creditor Agent /Instruction Information.

Up to 2 occurrences of Instruction Information may be provided. The last available occurrence of Instruction Information ,  preceded by /UDLC/, must be used to capture the Underlying Creditor provided in the pacs.009 ADV .

BICFI

only.

Name and structured Postal Address (TownName and Country Code should be prioritised).

Name and unstructured Address Line (TownName and Country Code should be prioritised, where possible).

---

<!-- ELEMENT 275 -->
The Purpose elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used by the capture the nature of the payment e.g., CORT Trade Settlement Payment, CFEE Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCDis classified within the Collateral categorisation, with the Name OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger special processing e.g., Category Purpose code SECU 'Securities' may trigger pacs.002 Payment Status Report to provide update on the progress of the payment to the previous Agent.

---

<!-- ELEMENT 276 -->
The optional Remittance Information element within the pacs.009 Financial  Institution  Credit Transfer is nested to provide Unstructured information  related to payment.

Min 0 - Max 1

Remittance Information enable the matching/reconciliation  of an entry that the payment is intended to settle

Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: unlike the pacs.008 Remittance Information can only be captured in an Unstructured element in the pacs.009 Financial Institution Credit Transfer. Remittance Information is  however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using

---

<!-- ELEMENT 277 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Serial Financial Institution Payments

Use Case p.9.1.1 - High Level Financial Institution  Credit Transfer (pacs.009) settled over a Payment Market  Infrastructure Use Case p.9.1.2 High Level Financial Institution  Credit Transfer (pacs.009) pre-advised settled using pacs.009.

---

<!-- ELEMENT 278 -->
# Payment Market Infrastructure

---

<!-- ELEMENT 279 -->
2a

Debtor Agent (B) provided a notification to Creditor Agent (E) using a pacs.009 advice to indicate a 'pre-advise and provides the related payment details (in step 2b) This provides Agent E the ability to take the payment amount into their position, particularly where final settlement in step 5 occur after their business day. (i.e. time zone differences between the various Agent in

In parallel the Debtor Agent (B) initiates a payment to credit the account of Agent (E) as the creditor in the pacs.009 settlement message

Agent C processes the payment on to Agent D

5

2b

3

Agent E receives  the payment and credits the account of Agent F as the Creditor, and may optionally provide  a notification e.g. credit notification.

---

<!-- ELEMENT 280 -->
# Financial Institution Credit Transfer

---

<!-- ELEMENT 282 -->
The Financial Institution Credit Transfer (advice) message is sent by a Debtor Agent to a Creditor Agent, directly. In this context the pacs.009 ADV is used as a direct advice message.

It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are Financial Institutions .

To provide party transparency in the pacs.009 ADV, the Debtor of the pacs.009 ADV remains the Debtor of

---

<!-- ELEMENT 284 -->
# Min 1 - Max 1

Each ISO 20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's Credit Transfer Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR(UniqueEnd-to-endTransactionReference)

---

<!-- ELEMENT 285 -->
The pacs.009 message Creation Date captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 286 -->
The pacs.009 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 287 -->
The pacs.009 Settlement Method element within the Group Header Settlement Information , includes one of the embedded codes to indicate how the payment message will be settled.

D

2 7

The Settlement Method element in the pacs.009 ADV is fixed to COVE .  This  indicate this advice of Financial Institution Credit Transfer will be settlement using a covering pacs.009.

Like the pacs.008, the Agents being used in the covering payment to reimburse the Instructed Agent can be provided in the dedicated Reimbursement Agent elements. This allows the Instructed Agent to identify the debit account on their books from the Reimbursement Agent account or look up the account related to the reimbursement agent.

---

<!-- ELEMENT 288 -->
The pacs message captures a number of Reimbursement Agents as a sub element to Settlement Information these elements detail the Agent in the cover method who will process the pacs.009 cover. These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as The Instructing Reimbursement Agent, and Instructed Reimbursement Agent. Each of these reimbursement agents also has a dedicated account element to optionally capture their related account details.

Min 0 - Max 1

The Instructing Reimbursement Agent captures the Agent who will execute a covering payment (i.e. pacs.009 COV or domestic equivalent) often referred to as the currency correspondent. This optional element is comparablewith the Field 53a in the legacy FIN message.

Min 0 - Max 1

The Instructing Reimbursement Agent Account captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 53.

Min 0 - Max 1

The Instructed Reimbursement Agent captures the Agent who will receive the covering payment (i.e., pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer Instructed Agent . This optional element is comparable with the Field 54a in the legacy FIN message.

Min 0 - Max 1

The Instructed Reimbursement Agent Account captured the account related to this Reimbursement Agent.

---

<!-- ELEMENT 290 -->
Payment Identification

Min 1 - Max 1

The pacs message Payment Identification provides a set of elements to identify the payment, of which several are mandatory elements

End to End Identification

Min 1 - Max 1

a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

Note: this reference must be transported in the End-toEnd Identification of the pacs.009 message used to settle the pacs.009 ADV

an end-to-end reference provided by the Debtor which must be passed unchanged throughout the payment and reported to the Creditor.

note: In a pacs.009 ADV if the Debtor has not provide an end-to-end identifier, the Debtor Agent may populate 'NOTPROVIDED' to comply the mandatory need of this element.

UETR

Min 1 - Max 1

the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their

---

<!-- ELEMENT 291 -->
Min 1 - Max 1

The pacs message Payment Identification also provides a set of optional elements to identify the payment.

---

<!-- ELEMENT 292 -->
The pacs message can be described.

# Min 0 - Max 1

# Payment Type Information provides a set of optional elements where the payment type

Instruction Priority Min 0 - Max 1

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS

Payment Type Information

A nested element which may either use an external ISO Service Level code* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group(captured in the code list)

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- ELEMENT 293 -->
# Date

The pacs.009 message (unlike  the pacs.008) has only one element to capture the amount  of the Credit Transfer, Interbank Settlement Amount .

Min 1 - Max 1

Interbank Settlement Amount

A mandated currency amount moved between the Instructing Agent and the Instructed Agent. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

Interbank Settlement Date

A mandated date on which the Interbank Settlement should be executed between the Instructing Agent and the Instructed Agent. This therefore is the value date comparable with the MT Field 32A

Note: the Financial Institution Credit Transfer (pacs.009) has no Instructed Amount element, Exchange Rate or Charger Bearer (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain

---

<!-- ELEMENT 294 -->
# & Request

The pacs.009 message has three optional elements to capture the optional information  related to the settlement of the instructions.

Min 0 - Max 1

The Settlement Priority provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused with the Instruction Priority.

Note: As the Settlement Method of the pacs.009 (ADV) is 'COVE' (settled via a covering pacs.009) Settlement Priority is relevant to the covering payment not the pacs.009 ADV

Min 0 - Max 1

The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time .

Min 0 - Max 1

The Settlement Time Request optionally captures the time settlement is requested for the payment instruction by the Instructing Agent.  This Time can be capture in four nested elements:

- CLS Time the time the amount must be credit to CLS Bank

- Till Time the time until which the payment may be settled

---

<!-- ELEMENT 296 -->
# Intermediary Agents

Unlike the other pacs.009 messages in the CBPR+ collection, the pacs.009 ADV message is exchanged directly between the Debtor Agent (as an Instructing Agent) and Creditor Agent (as an Instructed Agent). The roles of previous Instructing Agents and Intermediary Agents are therefore irreverent in the pacs.009 (ADV)

---

<!-- ELEMENT 297 -->
The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the Debtor . The Debtor sub elements describe the Debtor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Debtor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Debtor structured or unstructured

BICFI

Debtor

Postal

Address

---

<!-- ELEMENT 298 -->
Min 0 - Max 1

The pacs.009 Debtor Account is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The Debtor Account uses a variety of nested elements to capture information related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 299 -->
Min 0 - Max 1

Min 0 - Max 1

The Debtor Agent and Creditor Agent are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain  a relationship with their customers; the Debtor and Creditor . However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial  Institutions) maintain  a direct Nostro/Vostro account relationship.

Note: Where the Debtor and Creditor maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the Creditor Agent element to align with translation from the legacy MT message.

---

<!-- ELEMENT 300 -->
# Agent Account

Min 0 - Max 1

The pacs.009 Debtor Agent Account and Creditor Agent Account is used to capture the account information  related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The Debtor Agent Account and Creditor Agent Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 301 -->
The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the Creditor . The Creditor sub elements describe the Creditor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name

LEI

by which the

Agent is known

Name

The Creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) Instruction for Creditor Agent, Instruction Information element preceded by /UDLC/

Nested element capturing either structured or unstructured Debtor

Postal

Address

The BIC which

Creditor identifies the

Clearing

System

Member Id

BICFI

Creditor

---

<!-- ELEMENT 302 -->
Min 0 - Max 1

The pacs.009 Creditor Account is used to capture the account information  for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The Creditor Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 303 -->
The Instruction for Next Agent and Instruction for Creditor Agent elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

Min 0 - Max 2

The Instruction for Creditor Agent element offers a multiplicity  of up to 2 occurrences of information. This element enables:

- the use of 2 embedded codes to describe the instruction

- free format instruction information

- or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the Creditor Agent . It must be passed on throughout  the life cycle of the transaction until the payment reaches the Credit Agent .

Min 0 - Max 6

The Instruction for Next Agent element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format instruction information in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

---

<!-- ELEMENT 304 -->
The Purpose elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used by the capture the nature of the payment e.g. CORT Trade Settlement Payment, CFEE Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCDis classified within the Collateral categorisation, with the Name OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger special processing e.g. Category Purpose code SECU 'Securities' may trigger pacs.002 Payment Status Report to provide update on the progress of the payment to the previous Agent.

---

<!-- ELEMENT 305 -->
The optional Remittance Information element within the pacs.009 Financial  Institution  Credit Transfer is nested to provide Unstructured information  related to payment.

Min 0 - Max 1

Remittance Information enable the matching/reconciliation  of an entry that the payment is intended to settle

Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: unlike the pacs.008 Remittance Information can only be captured in an Unstructured element in the pacs.009 Financial Institution Credit Transfer. Remittance Information is  however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using

---

<!-- ELEMENT 306 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Financial Institution Advice Payments

Use Case p.9.1.2.a - High Level Financial Institution  Credit Transfer (pacs.009) pre-advised using pacs.009 (advice) Use Case p.9.1.2.b - High Level Financial Institution  Credit Transfer (pacs.009) pre-advised using pacs.009 (advice)

---

<!-- ELEMENT 307 -->
Debtor Agent (B) provided a notification to Creditor Agent (E) using a pacs.009 advice to indicate a 'pre-advise and provides the related payment details (in step 2b) This provides Agent E the ability to take the payment amount into their position, particularly where final settlement in step 5 occur after their business day. (i.e. time zone differences between the various Agent in

In parallel the Debtor Agent (B) initiates a payment to credit the account of Agent (E) as the creditor in the pacs.009 settlement message

Agent C processes the payment on to Agent D

5

2a

2b

3

Agent E receives  the payment and credits the account of Agent F as the Creditor, and may optionally provide  a notification e.g. credit notification.

---

<!-- ELEMENT 308 -->
2a

2b

3

Debtor Agent (B) provided a notification to Creditor Agent (E) using a pacs.009 advice to indicate a 'pre-advise and provides the related payment details (in step 2b) This provides Agent E the ability to take the payment amount into their position, particularly where final settlement in step 5 occur after their business day. (i.e. time zone differences between the various Agent in

In parallel the Debtor Agent (B) initiates a payment to credit the account of Agent (E) as the creditor in the pacs.009 settlement message

Agent C processes the payment on to Agent D

5

Agent E receives  the payment and credits the account of Agent F as the Creditor, and may optionally provide  a notification e.g. credit notification.

---

<!-- ELEMENT 309 -->
# Financial Institution Credit Transfer (Cover)

---

<!-- ELEMENT 311 -->
The Financial Institution Credit Transfer message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a debtor account to a creditor,

---

<!-- ELEMENT 312 -->
# roles between messages

Debtor

Debtor Agent

Creditor Agent

Underlying  Debtor

Debtor

Creditor

The Financial Institution Credit Transfer cover message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is important to recognise that some roles change between these parallel messages.

---

<!-- ELEMENT 313 -->
# roles between messages

The correspondent banking cover payment method utilises both the pacs.008 and pacs.009 cov as a whole transaction, whereby the UETR element within these messages contain the same UETRwhicheffectivelyinterlink the messages.

---

<!-- ELEMENT 315 -->
# Min 1 - Max 1

Each ISO 20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's Credit Transfer Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR(UniqueEnd-to-endTransactionReference)

---

<!-- ELEMENT 316 -->
The pacs.009 message Creation Date captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 317 -->
# Transactions

The pacs.009 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 318 -->
The pacs.009 Settlement Method element within the Group Header Settlement Information , includes one of the embedded codes to indicate how the payment message will be settled.

D

2 7

The Settlement Method element in the pacs.009 allows a choice of an embedded code.

INDA indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated Settlement Account element.

INGA indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in

---

<!-- ELEMENT 319 -->
The pacs.009 message Settlement Account is a nested element as part of Settlement Information, this element identifies information related to an account used to settle the payment instruction.

Min 0 - Max 1

The Settlement Account identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the Settlement Method )

Min 1  - Max 1

Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Account Servicing Institution

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 321 -->
Min 1 - Max 1

The pacs message Payment Identification provides a set of elements to identify the payment, of which several are mandatory elements

---

<!-- ELEMENT 322 -->
# (continued)

Min 1 - Max 1

The pacs message Payment Identification also provides a set of optional elements to identify the payment.

---

<!-- ELEMENT 323 -->
# Information

The pacs message can be described.

Min 0 - Max 1

# Payment Type Information provides a set of optional elements where the payment type

Instruction Priority Min 0 - Max 1

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS

Payment Type Information

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group(captured in the code list)

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- ELEMENT 324 -->
# Date

The pacs.009 message (unlike  the pacs.008) has only one element to capture the amount  of the Credit Transfer, Interbank Settlement Amount .

Min 1 - Max 1

Interbank Settlement Amount

Interbank Settlement Date

A mandated currency amount moved between the Instructing Agent and the Instructed Agent. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

Min 1 - Max 1

A mandated date on which the Interbank Settlement should be executed between the Instructing Agent and the Instructed Agent. This therefore is the value date comparable with the MT Field 32A

Note: the Financial Institution Credit Transfer (pacs.009) has no Instructed Amount element, Exchange Rate or Charger Bearer (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain

---

<!-- ELEMENT 325 -->
# Request

The pacs.009 message has three optional elements to capture the optional information  related to the settlement of the instructions.

Min 0 - Max 1

The Settlement Priority provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused with the Instruction Priority.

Note: Where the Settlement Method of the pacs.009 is 'INDA' (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code 'INGA' implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary.

Min 0 - Max 1

The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time .

Min 0 - Max 1

The Settlement Time Request optionally captures the time settlement is requested for the payment instruction by the Instructing Agent.  This Time can be capture in four nested elements:

- CLS Time the time the amount must be credit to CLS Bank

- Till Time the time until which the payment may be settled

---

<!-- ELEMENT 326 -->
D

Instructing Agent and Instructed Agent represent the Agents involved  in the pacs point-to-point message exchange.  These roles therefore change on each payment leg.

---

<!-- ELEMENT 327 -->
The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 - Max 1

The Previous Instructing Agent 1 captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message.

Min 0 - Max 1

The Previous Instructing Agent 1 Account captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message

Min 0 - Max 1

The Previous Instructing Agent 2 captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.

Min 0 - Max 1

The Previous Instructing Agent 2 Account captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

The Previous Instructing Agent 3 captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message. Min 0 - Max 1

The Previous Instructing Agent 3 Account captured the account related between this Agent and Previous

---

<!-- ELEMENT 328 -->
# Intermediary Agents

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. Intermediary Agent is an example of this, where these agents are classified in numeric order (i.e., Intermediary Agent 1 ) Previous Instructing Agent however is a static role which allows additional Previous Instructing Agent to be appendedto the history of the payment.

Thebelowdiagramvisualizes the change of Agent role at different stages of the payment transaction life cycle.

---

<!-- ELEMENT 329 -->
The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 - Max 1

The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 - Max 1

The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

# Min 0 - Max 1

The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

---

<!-- ELEMENT 330 -->
The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the Debtor . The Debtor sub elements describe the Debtor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Debtor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Debtor structured or unstructured

BICFI

Debtor

Postal

Address

---

<!-- ELEMENT 331 -->
Min 0 - Max 1

The pacs.009 Debtor Account is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The Debtor Account uses a variety of nested elements to capture information related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 332 -->
Min 0 - Max 1

Min 0 - Max 1

The Debtor Agent and Creditor Agent are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain  a relationship with their customers; the Debtor and Creditor . However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial  Institutions) maintain  a direct Nostro/Vostro account relationship.

Note: Where the Debtor and Creditor maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the Creditor Agent element to align with translation from the legacy MT message.

---

<!-- ELEMENT 333 -->
# Agent Account

Min 0 - Max 1

The pacs.009 Debtor Agent Account and Creditor Agent Account is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The Debtor Agent Account and Creditor Agent Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 334 -->
The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the Creditor . The Creditor sub elements describe the Creditor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Creditor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Debtor structured or unstructured

BICFI

Creditor

Postal

Address

---

<!-- ELEMENT 335 -->
Min 0 - Max 1

The pacs.009 Creditor Account is used to capture the account information  for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The Creditor Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1 Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 336 -->
The Instruction for Next Agent and Instruction for Creditor Agent elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

Min 0 - Max 2

The Instruction for Creditor Agent element offers a multiplicity  of up to 2 occurrences of information. This element enables:

- the use of 2 embedded codes to describe the instruction

- free format instruction information

- or both, where the free format complements the code.

The use of this element may be bilaterally agreed with the Creditor Agent . It must be passed on throughout  he life cycle of the transaction until the payment reaches the Credit Agent .

Min 0 - Max 6

The Instruction for Next Agent element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format instruction information in CBPR+. The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

---

<!-- ELEMENT 337 -->
The Purpose elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used by the capture the nature of the payment e.g. CORT Trade Settlement Payment, CFEE Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCDis classified within the Collateral categorisation, with the Name OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger special processing e.g. Category Purpose code SECU 'Securities' may trigger pacs.002 Payment Status Report to provide update on the progress of the payment to the previous Agent.

---

<!-- ELEMENT 338 -->
The optional Remittance Information element within the pacs.009 COV Financial  Institution  Credit Transfer is nested to provide Unstructured information  related to payment.

Min 0 - Max 1

Remittance Information enable the matching/reconciliation  of an entry that the payment is intended to settle.

Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: the pacs.008 Remittance Information is captured in the pacs.009 COV within the Underlying CustomerCredit Transfer , Remittance Information element. The Remittance Information in the pacs.009 COV is for Creditor this message (often the Creditor Agent of the pacs.008) As this information is  not present in the pacs.008 it is unlikely the pacs.009 COV remittance information will be used.

---

<!-- ELEMENT 339 -->
# Transfer

The Underlying Customer Credit Transfer element is used when the pacs.009 Financial Institution Credit Transfer message is being utilized to cover a pacs.008 FI to FI Customer Credit Transfer . The  information contained within this nested element relates directly to the information  exchanged  between the Instructing Agent and Instructed Agent of the pacs.008 FI to FI Customer Credit Transfer and can be compared with Sequence B of the legacy MT 202 COV.

---

<!-- ELEMENT 340 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Cover Method Financial  Institution Payments

Use Case p.9.2.1 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV)

Use Case p.9.2.2 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) over a Payment Market Infrastructure

Use Case p.9.2.3 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) where an incorrect intermediary is used

Use Case p.9.2.4 - High Level FI to FI Customer Credit Transfer involved  a serial leg into a cover method (pacs.009 COV)

Use Case p.9.2.5 - High Level FI to FI Customer Credit Transfer involved  a serial leg in and out of a cover method (pacs.009 COV)

Use Case p.9.2.6 - High Level FI to FI Customer Credit Transfer involved  a serial leg out of a cover method (pacs.009 COV)

---

<!-- ELEMENT 341 -->
2b

In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) who become the Creditor of the cover  payment (pacs.009 cov). Agent A's role also changes in the cover  payment where  it becomes the Debtor, whereby  Agent A's

6

4

Agent C receives  the payment and credits the account of Agent D as

Agent D reconciles the covering funds and credits the account of the Creditor, and may optionally provide  a notification e.g. credit

---

<!-- ELEMENT 342 -->
1

2a

Debtor Agent (A) initiates a payment using the cover  method to the Creditor  Agent (D)

2b

In parallel the Debtor Agent (A) initiates a covering  payment to credit the account of Agent (D) with their correspondent  (Agent

# method (pacs.009 COV) over a Payment Market Infrastructure

1

2a

2b

A

Debtor initiates a payment instruction to the Debtor Agent

3

B

pacs.009 cov pacs.002

Settlement Complete

Agent B processes the payment on Agent C, via the Payment

3

pacs.008

pacs.002

4

4

5

pacs.009 cov

C

Payment Market Infrastructure, settles the payment between  Agent B and Agent C as direct participants of the Market Infrastructure,  and provides  a settlement confirmation  to Agent B

Agent C receives  the payment and

5

6

6

Agent C produces an end of day account statement report. An optional real time notifications e.g. advice  of credit may have  also been created at the time of the credit posting

7

D

7

Agent D reconciles the covering funds and credits the account of the Creditor, and may optionally provide  a notification e.g. credit

---

<!-- ELEMENT 343 -->
1

# method (pacs.009 COV) where an incorrect intermediary is used.

1

2a

2b

Debtor initiates a payment instruction to the Debtor Agent

2a

4

Debtor Agent (A) initiates a payment using the cover  method to the Creditor Agent (D)

2b

A

B

3

In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) who become the Creditor of the cover  payment (pacs.009 cov). Agent A's role also changes in the cover  payment where  it becomes the Debtor, whereby  Agent A's pacs.009 cov

pacs.002

pacs.009 cov

3

Agent B processes the payment on to Agent Z

Agent Z receives the payment and recognises they do not hold the account of Agent D as the Creditor.  Agent Z reject the pacs.008

pacs.002

Z

5

C

5

6

4

Recognising the error  Agent B reprocesses the payment on to Agent C using the same UETR (correcting the error in step 3)

Agent C receives  the payment and credits the account of Agent D. Agent C produces an end of day account statement report. An optional real time notifications e.g. advice of credit may have  also been created at the time of the credit posting

Agent D reconciles the covering  funds and credits the account of the Creditor,

D

6

---

<!-- ELEMENT 344 -->
4

6

Debtor Agent (A) initiates a payment using the serial method towards the Creditor Agent (E)

3a

Agent B initiates a payment using the cover  method towards the Creditor Agent (E) by sending a direct pacs.008 to Agent E who they have  business

3b

In parallel the Agent (B) initiates a covering  payment to credit the account of Agent (E) with their correspondent (Agent D)

Agent E receives  the payment instruction and credits the account of the Creditor, and may optionally provide  a notification e.g. credit notification. Alternatively, they may have  chosen to await until settlement occurred in Step 6 based upon their

Agent D receives  the payment and credits the account of Agent E. Agent D produces an end of day account statement report. An optional real time notification e.g. advice  of credit may have  also been created at the time of the credit

---

<!-- ELEMENT 345 -->
# of a cover method (pacs.009 COV)

1

Debtor initiates a payment instruction to the Debtor Agent

2

Debtor Agent (A) initiates a payment using the serial method towards the Creditor Agent (F)

1

2

pacs.008

pacs.002

3a

Agent B initiates a payment using the cover  method towards the Creditor Agent (F) by sending a direct pacs.008 to Agent E who they have  business relationship with.

3b

In parallel the Agent (B) initiates a covering  payment to credit the account of Agent (E) with their correspondent

3a

3b

B

C

5

4

5

pacs.008

pacs.002

pacs.009 cov pacs.002

D

Agent E receives  the payment instruction and process the payment on to Agent F. Alternatively they may have  chosen to await until settlement occurred in Step 6 based upon their risk appetite.

Agent C processes the payment on Agent D, using a correspondent

6

E

4

pacs.008

pacs.002

F

6

Agent D receives  the payment and credits the account of Agent E. Agent D produces an end of day account statement report. An optional real time notification e.g. advice  of credit may have  also been created at the time of the credit posting

7

7

Agent F receives the payment and credits the account of the Creditor, and may optionally provide  a notification e.g. credit notification.

---

<!-- ELEMENT 346 -->
2b

In parallel the Agent (A) initiates a covering  payment to credit the account of Agent (D) with their correspondent (Agent C)

- 3

Agent D receives  the payment instruction and process the payment on to Agent E. Alternatively they may have  chosen to await until settlement occurred in Step 6 based upon their

4

5

6

Agent C receives  the payment and credits the account of Agent D. Agent C produces an end of day account statement report. An optional real time notification e.g. advice  of credit may have  also been created at the time of the credit posting

1

2a

Debtor Agent (A) initiates a payment using the cover method towards the Creditor Agent (E) by sending a direct pacs.008 to Agent D who they

Debtor initiates a payment instruction to the Debtor Agent

Agent E receives  the payment and credits the account of the Creditor, and may optionally provide  a notification e.g. credit notification.

Agent B processes the payment on Agent C, using a correspondent

---

<!-- ELEMENT 347 -->
# FI to FI Payment Status Report

---

<!-- ELEMENT 349 -->
# Customer Payment (pacs.008)

A

pain.001

pain.002

pacs.008

pacs.002

pacs.004

pacs.002

The code list representing the Payment Transaction Status is  part of the ISO 20022 external code list

B

pacs.008

pacs.002

Return &

Reason

C

Reject &

Reason

The FIToFIPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an

CBPR+ restricted the pacs.002 to a single transaction

---

<!-- ELEMENT 350 -->
The FIToFIPaymentStatusReportmessage is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an instruction. It is also used to report on a pending instruction.

---

<!-- ELEMENT 352 -->
# Min 1 - Max 1

Each ISO 20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

---

<!-- ELEMENT 353 -->
The pacs.002 message Creation Date captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 355 -->
Min 1 - Max 1

The pacs.002 FI to FI Payment Status Report uses elements in the Original Group Information to capture the message identifier and message name of the underlying payment the Payment Status Report relates to. The mandatory Original Message Identification contains the point-to-point reference, and the mandatory Original Message Name Identification contains the message name of the underlying payment being reported upon. Optionally the Original Creation Date Time can also be captured.

# For example:

Original Message Name Identification 'pacs.008.001.08' confirms the Status Report is of a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as 'pacs.009.001.08' confirms the Status Report is of a pacs.009 Financial Institution Credit Transfer.

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 356 -->
The pacs.002 FI to FI Payment Status Report also uses a number of other Original elements in the Transaction Information And Status to capture information from the underlying payment that the Payment Status Report relates to.

Mandatory element (in addition to Original Message identification and Original Message Name Identification described on the previous page) include:

Original End to End Identification Original UETR

Min 0 - Max 1

Min 0 - Max 1

Optionally Original Transaction Identification and Original Instruction Identification may also be used.

These Original elements enables the Instructed Agent in the pacs.002 Payment Status Report to associate the Payment Status with the payment they originally sent.

Transaction Information and Status

Original Instruction Identification

Original End to End Identification

Min 1 - Max 1

Min 1 - Max 1

---

<!-- ELEMENT 357 -->
# Min 1 - Max 1

The pacs.002 FI to FI Payment Status Report Transaction Status utilizes the externalized ISO Payment Transaction Status code list to provide a status update on a pacs message previously received. The Transaction Status element is arguable the most significant/core parts of the pacs.002 and optionally may further be complimented with Status Reason Information.

Min 0 - Max 1

The nested Status Reason Information enable the optional inclusion of:

Originator - the party that issues the status. Typically, the pacs.002 Instructing Agent and therefore Originator is not necessary.

Reason - which utilizes either an ISO external Status Reason code or a proprietary reason. For example, AC04 'Closed Account Number' would compliment a RJCT (Reject) Transaction Status.

Additional Information -a text element to provide further status reason information, necessary where the Reason code is NARR

Note: A Reason code must be provided where the Transaction Status RJCT (Reject) code is used.

The next two slides take a look at:

- The code relevant to CBPR+ Payment Statuses, the codes description and the High Level Use Case.

---

<!-- ELEMENT 359 -->
The pacs.002 Payment Transaction Status element facilitates updates to the previous Agent on changes to the status of the payment. Such Status Information messages (pacs.002), with the exception of reject code RJCT which is mandatoryin CBPR+ ,  are bilateral agreed, where upon a variety of these Transaction Statuses may be used by the Instructed Agent at different stages of the payment processing.

This diagram illustrates the logical order in which these codes may be used during the processing of the Payment Clearing And Settlement message (pacs) and the role of the Agent in providing these status.

---

<!-- ELEMENT 368 -->
The pacs.002 FI to FI Payment Status Report optional Effective Interbank Settlement Date allows a choice of Date or Date Time to confirm when a point-to-point transaction is completed/effected.

When Date Time is chosen CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

---

<!-- ELEMENT 370 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Serial Financial Institution to Financial Institution to Customer Credit Transfer

Use Case p.2.1.1 - High Level Payment Status Information  (pacs.002) of multiple Payment Transaction Status updates

Use Case p.2.1.2 - High Level Rejection of an incomplete Customer Credit Transfer (pacs.008)

# Serial Financial Institution Credit Transfer

Use Case p.2.2.1 - High Level Rejection of an incomplete Financial Institution  Credit Transfer (pacs.009)

# Cover Method Financial  Institution to Financial Institution to Customer Credit Transfer

Use Case p.2.3.1.a - High Level Rejection of an incomplete payment using the cover method

Use Case p.2.3.1.b - High Level Rejection of an incomplete payment using the cover method

# Financial Institution Direct Debit

Use Case p.2.4.1 - High Level Status Information  of a Financial Institution  Direct Debit

Use Case p.2.4.2 - High Level Rejection of a Financial Institution  Direct Debit

# Financial Institution to Financial Institution Customer Direct Debit

Use Case p.2.5.1 - High Level FI to FI Customer Direct Debit (pacs.003) successful settlement

Use Case p.2.5.2 - High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement

---

<!-- ELEMENT 371 -->
# Transaction Status updates

An agent may provide multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle i.e. from receipt through to onward processing.

Where a payment is rejected ,  the  use of the pacs.002

---

<!-- ELEMENT 372 -->
1

2

- Agent B processes the payment 3

on Agent C

4

- 5 Agent C return funds to Agent B, together with the reason code for return.

- Agent B return funds to Agent A, together with the reason code for return. 6

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent C processes the payment on Agent D

Having  received  the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D rejects the payment to Agent C using a Status information  message (pacs.002) also including the return reason code.

---

<!-- ELEMENT 373 -->
# (pacs.009)

1

Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent E) using Agents C as an intermediary.

- 2

4

5

2

Agent C processes the payment onto Agent D

Having  received  the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D rejects the payment to Agent C using a Status Information  message (pacs.002) also including the reject code.

Agent C return funds to Agent B, together with the reason code for return.

Agent B advises  Agent A of the return of payment together with the reason using the camt.053 and may optionally provide  a notification e.g. credit notification.

---

<!-- ELEMENT 374 -->
1

2a

2b

1

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a payment using the cover  method to the Creditor  Agent (D)

8

A

2b

+ Return Reason

In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) with their correspondent  (Agent C)

Having  received  the payment with settlement method COVE Agent D recognises (prior  to the settlement via pacs.009 COV) the payment can not be completed as requested e.g. the Creditor's account is closed. Agent

2a

3

5

3

B

pacs.008

pacs.002

# + Reject Reason

pacs.009 cov pacs.004

+ Return Reason

Agent B processes the payment on Agent C

4

7

5

C

+ Return Reason

Agent C receives  the payment and credits the account of Agent D

Agent C produces an end of day account statement report.

4

D

6b

7

8

6b

post-settlement returns see pacs.004 use case p.4.3.1.a and p.4.3.1.b

Agent D requests the return of covering funds, together with the reason for return, having  already rejected the pacs.008

Agent C return of covering  funds to Agent B, together with the reason code for return.

---

<!-- ELEMENT 375 -->
3

7

Agent B processes the payment

Having  received  the payment Agent D recognises the payment can not be

Agent C returns the settled covering

---

<!-- ELEMENT 376 -->
# (pacs.010)

1

Agent E initiates a Direct Debit instruction to debit Agent A's account

1a

Agent B provides a positive status update to Agent E

2

3

4

Debtor Agent (B) initiates a serial payment towards the Creditor Agent (E) using Agents B & C as intermediaries

Agent C processes the payment on Agent D

Agent D credits the account of the Creditor (Agent E), and may optionally provide  a notification e.g. credit notification in addition to an account statement (camt.053)

---

<!-- ELEMENT 377 -->
1

Agent D initiates a Direct Debit instruction to debit Agent A's account

Debtor Agent (B) rejects the instruction, using a pacs.002, as no mandate agreement is in place.

pacs.010

pacs.002

---

<!-- ELEMENT 378 -->
1

2

3

4

Creditor Agent (A) relays the status ACSC (accepted settlement completed) to the Initiating Party, based upon a bilateral agreement

Creditor initiates a direct debit instruction to the Creditor Agent

Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method 'INDA'

The Debtor Agent debits the account of the Debtor, and may optionally provide  a notification e.g. debit notification in addition to an account statement (camt.053). The Debtor Agent also provides  a status update ACSC (accepted settlement completed) to the Creditor  Agent.

---

<!-- ELEMENT 379 -->
1

2

Creditor initiates a direct debit instruction to the Creditor Agent

Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method 'INDA'

3

4

Creditor Agent (A) relays the status RJCT  (Rejected)  to the Initiating Party with the rejection reason information

The Debtor Agent fails to debit the account of the Debtor (e.g., account is closed). The Debtor Agent provides  a status update RJCT (Rejected) with the rejection reason information.

---

<!-- ELEMENT 380 -->
# Payment Return

---

<!-- ELEMENT 382 -->
# FI Customer Payment (pacs.008)

The PaymentReturn message is sent by an agent to the previous agent in the payment chain to undo a payment previously settled.

---

<!-- ELEMENT 384 -->
# Min 1 - Max 1

Each ISO 20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's Credit Transfer Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR(UniqueEnd-to-endTransactionReference)

---

<!-- ELEMENT 385 -->
The pacs.004 message Creation Date captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 386 -->
The pacs.004 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 387 -->
The pacs.004 Settlement Method element within the Group Header Settlement Information , includes one of the embedded codes to indicate how the payment message will be settled.

D

2 7

The Settlement Method element in the pacs.004 allows a choice of an embedded code.

INDA indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated Settlement Account element.

INGA indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in

---

<!-- ELEMENT 388 -->
The pacs.004 message Settlement Account is a nested element as part of Settlement Information, this element identifies information related to an account used to settle the payment instruction.

Min 0 - Max 1

The Settlement Account identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the Settlement Method )

Min 1  - Max 1

Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Account Servicing Institution

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 390 -->
Min 0 - Max 1

The pacs.004 message Return Identification captures a point-to-point reference used to unambiguously identify the Payment Return message, created by the Instructing Agent in the Return Chain .

The 35 character return identifier could be considered similar to the legacy Sender's Reference (Field 20) of an MT return payment message.

---

<!-- ELEMENT 391 -->
Min 0 - Max 1

The pacs.004 Payment Return uses elements in the Original Group Information to capture the message identifier and message name of the underlying payment the Payment Return relates to. The mandatory Original Message Identification contains the point-to-point reference, and the mandatory Original Message Name Identification contains the message name of the underlying payment being returned. Optionally the Original Creation Date Time can also be captured.

# For example:

Original Message Name Identification 'pacs.008.001.xx' confirms the return is of a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as 'pacs.009.001.xx' confirms the return is of a pacs.009 Financial Institution Credit Transfer.

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 392 -->
Min 1 - Max 1

The pacs.004 Payment Return also uses a number of other Original elements in the Transaction Information to capture information from the underlying payment that the Payment Return relates to. Mandatory element examples of this (in addition to Original Message identification and Original Message Name Identification described on the previous page) include:

These Original elements enables the Instructed Agent in the pacs.004 Payment Return to re-associate the Return with the payment they originally sent.

Transaction Information

Original End to end Identification

Original UETR

---

<!-- ELEMENT 393 -->
# Settlement Date

# Min 1 - Max 1

Min 1 - Max 1

The Returned Interbank Settlement Amount and subsequent Interbank Settlement Date are mandatory elements in the pacs.004 Payment Return, these elements are used to capture the currency and amount being returned together with the settlement date of the Payment Return.

The Returned Interbank Settlement Amount may be a different amount than the Original Interbank Settlement Amount (amount received the Agent instructing the Payment Return )  for example a charge may have been levied for processing the Payment Return or the Payment Return is a partial amount for overpayment or partial refund

In this case the Returned Instructed Amount should be equal to the Interbank Settlement Amount, on the first leg of the Payment Return. Charge levied should also be captured in the Charge Information element.

Transaction Information

Returned Interbank Settlement Amoun

---

<!-- ELEMENT 394 -->
The pacs.004 message has two optional elements to capture the optional information related to the settlement of the instructions.

Min 0 - Max 1

The Settlement Priority provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused with the Instruction Priority.

Note: Where the Settlement Method of the pacs.004 is 'INDA' (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code 'INGA' implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary.

Min 0 - Max 1

The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time .

---

<!-- ELEMENT 395 -->
# Min 0 - Max 1

The Returned Instructed Amount captures currency and amount instructed by the Debtor in the Return Chain . This conditional element is required when the Returned Interbank Settlement Amount is not the same currency and/or amount as originally instructed by the Debtor. For example a charge is taken or the transactions is converted to another currency.

Min 0 - Max 1

The Exchange Rate capture the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency.

---

<!-- ELEMENT 396 -->
Min 1 - Max 1

The pacs.004 Charge Bearer element uses an embedded code that is used to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

Note: Charge Bearer code DEBT (implying the Return Chain, Debtor will bear any charges) is removed from the CBPR+ pacs.004. Should a non-CBPR+ Payment Return be received with Charge Bearer DEBT, it is recommended to use SHAR in any onward processed Payment Return.

---

<!-- ELEMENT 397 -->
Min 0 - Max *

Min 0 - Max 1

The Charges Information element provides information  on the return charges to be paid by the Charge Bearer . This element is comparable with MT Fields: 71F 'Senders Charges' and 71G 'Receiver's Charges', although  pre-paid charges (legacy 71G 'Receiver's Charges' are an unlikely  use case for Payment Returns

In addition to the legacy MT message the pacs.004 Charge Information mandate the Agent, this represent the Agent who has taken a charge (deduct from the transaction) CBPR+ best practice recommends the use of the structured Agent BIC.

As the Charges Information element is repetitive it can capture charges related to previous legs of the Payment Return transaction chain.

Note: Charge Information element is required where a charge is taken on the Payment Return. A charge for returning an incomplete payment by the originator of the Payment Return (Return Chain Debtor) is common practice. It is encouraged that Agents who processed the original payment transaction consider the total operation cost when defining their payment cost recovery model. Whereby further charges on Return Payments should be avoided.

---

<!-- ELEMENT 398 -->
Transaction Information

Instructing Agent and Instructed Agent represent the Agents involved  in the pacs point-to-point message exchange. These roles therefore change on each payment

---

<!-- ELEMENT 399 -->
# Min 1 - Max 1

The mandatory Return Chain element captures all the parties involved in the return transaction, in much the same way the underlying payment message capturesall the parties involved in a payment.

In this element the role of the various parties change , to reflect the fact the payment is now a Payment Return, for example, the Creditor Agent of the underlying payment may become the Debtor Agent of the PaymentReturn .

Although Ultimate Debtor and Ultimate Creditor are present in the Return chain it is extremely unlikely one of these Parties would be involved in the return chain and can only do so if present as an Ultimate Party in the original payment.

Note: the static Previous Instructing Agent roles in the original payment transition to

---

<!-- ELEMENT 400 -->
Arguably the most common example of a Payment Return is where it is initiated by the Creditor Agent of the original payment, this Agent's role the become the mandatory Debtor in the Return Chain element (as they owe the money to the party the return is intended for).

Recognising that the original Creditor is not party to the return, for example, they might be a known customer of the original Creditor Agent whereby a reject or return code 'AC01' may be used. In this way the original Creditor was not involved in the Payment Return.

Note: the static Previous Instructing Agent roles in the original payment transition to Intermediary

---

<!-- ELEMENT 401 -->
Various other Payment Return use cases exist where the common principal is the initiator of the Payment Return becomes the mandatory Debtor in the Return Chain element (as they owe the money to the party the return is intended for). And the mandatory Creditor in the Return Chain element is the party the payment is being returned to.

Note: a party Rejecting the payment using a pacs.002 would not be considered to be involved  in

---

<!-- ELEMENT 402 -->
Min 1 - Max 1

The Return Reason Information element captures detailed information on the return reason. Within this element:

5

- the Originator element helps identify the party who initiated the request to return the payment. This party would have been included in the underlying payment and may also be included the pacs.004 Return Chain.

- the Reason is mandatory and is represented by an externalised Code choice ( )

- the Additional Information element may also be included to provide further details on the reason for return.

The code list representing the Return Reason is part of the ISO 20022 external code list

Transaction Information     Return Reason Information

---

<!-- ELEMENT 410 -->
Min 0 - Max 1

The Original Transaction Reference optionally capture elements related to the original transactions. The inclusion of this element is particularly useful where the Payment Return includes an Agent not party to the original transaction, or where a significant time lapse has occurred between the original payment and the Payment Return i.e., information may have been archived by Agent in the Return chain. CBPR+ has two rules describing when the Original Transaction Reference should be used.

The Amount within the nesting of this Original Transaction Reference element only allows for the Instructed Amount , as instructed by the Debtor in the original payment initiation request. If the Instructed Amount was present in the original payment, populating this data is simple. However, we should also recognise the Instructed Amount is not always present (and in fact is not available in the pacs.009), whereby this value should represent the amount in the Interbank Settlement Amount of the pacs message being returned. The use of Instructed Amount is best described in the pacs.008 Currency and Amount section.

Note: the role of Parties and Agent in Original element remain unchanged unlike  elements such as the Return chain

---

<!-- ELEMENT 411 -->
Within the Payment Return (pacs.004)

- the Original Group Information element is used to refers to original message for which the return relates to. e.g. based upon the above example  pacs.008 as the original message would be included  in the pacs.004

- the Transaction Information > Original UETR element would include UETR of the payment message received. i.e. the same UETR is used on the Payment Return .

- the Original Transaction Reference element includes  detail from the Original Message Name Identification e.g. the Debtor of the original pacs.008.001.xx

- the Return Chain element includes the parties in the return payment chain, noting the parties reverse (i.e. change role) from the original payment whereby the Debtor of the original payment becomes the Creditor

---

<!-- ELEMENT 412 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Serial Customer Payments

Use Case p.4.1.1 - Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008)

Use Case p.4.1.2 - Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008)

Use Case p.4.1.2.a - Partial Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008)

Use Case p.4.1.2.b - Refund Payment of a complete Customer Credit Transfer (pacs.008)

Use Case p.4.1.3 - Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008) involving  a Market  Infrastructure

# Serial Financial Institution Payments

Use Case p.4.2.1 - Payment Return (pacs.004) of an incomplete Financial Institution  Credit Transfer (pacs.009)

Use Case p.4.2.2 - Payment Return (pacs.004) of a complete Financial Institution  Credit Transfer (pacs.009)

Use Case p.4.2.3 - Payment Return (pacs.004) of an incomplete Financial Institution  Credit Transfer (pacs.009) involving  a Market  Infrastructure

# Cover Method Payments

Use Case p.4.3.1.a - Payment Return (pacs.004) of an incomplete payment using the cover method

Use Case p.4.3.1.b - Payment Return (pacs.004) of an incomplete payment using the cover method

Use Case p.4.3.2 - Payment Return (pacs.004) of a complete payment using the cover method

Use Case p.4.3.2.a - Payment Return (pacs.004) of a complete payment using the cover method

Use Case p.4.3.3 - Payment Return (pacs.004) of an incomplete cover payment

---

<!-- ELEMENT 413 -->
# (pacs.008)

1

2

- Agent B processes the payment 3

on Agent C

4

- 5 Agent C return funds to Agent B, together with the reason code for return.

6

Agent B return funds to Agent A, together with the reason code for return.

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent C processes the payment on Agent D

Having  received  the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D return the payment to Agent C (as the original payment had already settled) together with the return reason.

---

<!-- ELEMENT 415 -->
# (pacs.008)

1

2

- Agent B processes the payment 3

on Agent C

4

5

7

8

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent C processes the payment on Agent D

Agent D credits the account of the Creditor, and may optionally

6

Creditor determines that they wish to partially return the payment e.g. they were  over  paid or provide  a partial refund, and instructs their bank (Agent D) to partially return the payment together with the reason.

Agent D returns the payment to Agent C using a Payment Return

Agent C return funds to Agent B, together with the reason code for return.

Agent B return funds to Agent A, together with the reason code for return.

---

<!-- ELEMENT 416 -->
1

2

- Agent B processes the payment 3

on Agent C

4

5

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent C processes the payment on Agent D

Creditor determines that they wish to refund the payment e.g. they could not provide  the goods or services paid for. They instruct a new payment from their bank account.

Agent D credits the account of the Creditor, and may optionally provide  a notification e.g. credit notification in addition to an account statement (camt.053)

In  some circumstances the Creditor may take it upon themselves to provide a refund, using a new

---

<!-- ELEMENT 417 -->
# (pacs.008) involving a Market Infrastructure

1

2

3

4

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (B) using the local currency ISO 20022 Market Infrastructure

The payment is settled via  the local ISO 20022 Market Infrastructure,  whereby the payment is forwarded  to the Creditor Agent (B)

Having  received  the payment Agent B recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent B returns the payment to Agent A using a Payment Return message (pacs.004) also including the return reason code.

The Market Infrastructure  returns the payment performing  the necessary settlement posting between  Agent B and Agent A.

---

<!-- ELEMENT 418 -->
# (pacs.009)

1

Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent E) using Agents C as an intermediary.

2

- Agent C processes the 3

payment onto Agent D

Having  received  the payment instruction Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D rejects the payment to Agent C using a Status Information  message (pacs.002) also including the return reject code.

4

5

Agent C return funds to Agent B, together with the reason code for return.

Agent B advises  Agent A of the return of payment together with the reason using the camt.053 and may optionally provide  a notification e.g. credit notification.

---

<!-- ELEMENT 419 -->
# (pacs.009)

1

Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent D) using Agents C as an intermediary.

2

3

4

5

Creditor Agent (C) credits the account of Agent D and may optionally provide  a notification e.g. credit notification, in addition to an account statement (camt.053)

Having  received  the payment Agent D recognises the payment is incorrect e.g. the wrong  amount was received  . Agent D sends a Payment Return  to Agent C including the return reason.

Agent C return funds to Agent B, together with the reason code for return.

Agent B advises  Agent A of the return of payment together with the reason using the camt.053 and may optionally provide  a notification e.g. credit notification.

---

<!-- ELEMENT 420 -->
# Transfer (pacs.009) involving a Market Infrastructure

1

2

3

5

6

Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent D) using the local currency ISO 20022 Market Infrastructure.

The payment is settled via the local ISO 20022 Market Infrastructure,  whereby the payment is forwarded  to the Creditor Agent (C)

4

Having  received  the payment Agent C recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent C returns the payment towards Agent B using a Payment Return message (pacs.004) also including the return reason code.

Agent C returns the payment to Agent B, together with the reason

The payment return is settled via the local ISO 20022 Market Infrastructure, whereby the payment return is forwarded  to the Creditor Agent (B)

Agent B advises  Agent A of the return of payment together with the reason using the camt.053 and may optionally provide  a notification e.g. credit notification.

---

<!-- ELEMENT 421 -->
1

2a

2b

In parallel the Debtor Agent (A) initiates a covering  payment to credit the account of Agent (D) with their correspondent  (Agent C)

3

1

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a payment using the cover  method to the Creditor  Agent (D)

Agent B processes the payment

A

2b

+ Return Reason

3

B

# + Return Reason

4

Agent C receives  the payment and credits the account of Agent D

pacs.008

pacs.009 cov pacs.004

7

C

5

Agent C produces an end of day account statement report. An optional real time notifications e.g. credit notification (camt.054) may have  also been created at the time of the credit posting

Having  received  the payment, Agent D recognises the payment can not be

2a

8

4

5

D

6

7

8

6

# + Return Reason

pre-settlement rejects see pacs.004 use case p.2.3.1

Agent D instructs the return of settled covering  funds, together with the reason for return.

Agent C returns the settled covering funds to Agent B, together with the reason code for return.

Agent C returns the settled covering

---

<!-- ELEMENT 422 -->
3

7

Agent B processes the payment

Having  received  the payment Agent D recognises the payment can not be

Agent B returns the settled covering

---

<!-- ELEMENT 423 -->
3

Agent C produces an end of day account statement report. An

Creditor determines that they wish

9

Agent B processes the payment

5

Agent B return of covering  funds to

---

<!-- ELEMENT 424 -->
1

2a

Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

2b

In parallel the Debtor Agent (A) initiates a covering  payment to credit the account of Agent (D) with their correspondent  (Agent C)

3

1

A

Debtor initiates a payment instruction to the Debtor Agent

Agent B processes the payment

5

2a

2b

11

+ Return Reason

4

Agent C receives  the payment and credits the account of Agent D

Agent C produces an end of day account statement report. An optional real time notifications e.g. credit notification

B

3

pacs.008

pacs.009 cov pacs.004

+ Return Reason

4

10

7

5

C

8

D

9

pacs.008

pacs.004

# + Return Reason

Creditor determines that they wish to return the payment e.g. they are unable to apply, and instructs their bank (Agent E) to return the payment together with the reason.

+ Return Reason

Agent E returns the original pacs.008 , using a pacs.004 together with the reason for return.

8

Agent D reconciles the covering funds and processes the payment onto Agent E

Agent E credits the account of the Creditor, and may optionally provide  a notification e.g., credit

Agent D returns the original pacs.009 cov , using a pacs.004 together with the

- 9 reason for return.

10

Agent C return of covering  funds to Agent B, together with the reason code for return.

6

E

7

---

<!-- ELEMENT 425 -->
1

2a

2b

1

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a payment using the cover  method to the Creditor  Agent (D)

In parallel the Debtor Agent (A) initiates a covering  payment to credit the account of Agent (D) with their correspondent  (Agent

A

2b

+ Return Reason

3

B

+ Reject Reason

3

Agent B processes the payment on Agent C

2a

6

5

pacs.008

camt.056

pacs.009 cov pacs.002

4

C

Agent C receives  the payment and recognises the payment can not be completed as requested e.g. the Agent D

D

See use case p.8.2.1 for the cover payment sample c.29.2.2 for case resolution and p.56.2.2 for payment return

4

5

6

Agent C rejects the covering  funds to Agent B, together with the reason code for rejection.

Agent B return of covering  funds to Agent A, together with the reason code for return.

Agent A initiates a Request for

---

<!-- ELEMENT 426 -->
# Financial Institution Direct Debit

---

<!-- ELEMENT 428 -->
The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor's account to the Creditor, where both Debtor and Creditor are

---

<!-- ELEMENT 429 -->
The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor's account to the Creditor, where both Debtor and Creditor are

---

<!-- ELEMENT 431 -->
# Min 1 - Max 1

Each ISO 20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

---

<!-- ELEMENT 432 -->
The pacs.010 message Creation Date Time captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 433 -->
The pacs.0010 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 435 -->
Min 1 - Max 1

The Financial  Institution  Direct Debit Credit Identification provides a mandatory element to identify the Direct Debit instruction.

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT Financial Markets Direct Debit message.

---

<!-- ELEMENT 436 -->
Instructing Agent and Instructed Agent represent the Agents involved  in the pacs point-to-point message exchange.  These roles therefore change on each message leg.

Instructing Agent and Instructed Agent elements are required in all pacs messages and is only available in the Credit Instruction.

---

<!-- ELEMENT 437 -->
Min 0 - Max 1

The Creditor Agent is a static role in the pacs messages. This agent maintain  a relationship  with their customer, the Creditor . Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial  Institutions) maintain  a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain  the account of both the Debtor and Creditor.

Min 0 - Max 1

Where the Creditor Agent is utilised  the Creditor Agent Account may optionally be used to capture the account of the Creditor Agent with the Agent immediate before them in the transaction chain  (the Agent Serving  their account)

This would only apply where the message includes a Creditor Agent , however CBPRplus does not recommend to use this element unless mandated within a community  or bilaterally agreed.

---

<!-- ELEMENT 438 -->
The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the Creditor . The Creditor sub elements describe the Creditor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Creditor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Creditor structured or unstructured

BICFI

Creditor

Postal

Address

---

<!-- ELEMENT 439 -->
Account

Min 0 - Max 1

The Financial  Institution  Direct Debit Creditor Account provides a optional element to identify the Creditor's Account for which the Direct Debit instruction  intends to instruct the movement  of money to.

# Min 1 - Max 1

a unique Identification for the account, between the Account Servicer and Account Owner. The element is further nested by choice of IBAN or Other to capture the account.

An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account.

Currency

The Currency for which the account is held. This is identified using the three characters ISO currency code.

The Name of the Account, as Assigned by the servicing institution.

Anested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 440 -->
The Financial  Institution  Direct Debit message Direct Debit Transaction Information nested element captures information  related to the Debit part of the transaction, such as the Debtor, the amount and settlement date.

It is important to recognise that the data elements contained in this part of the Direct Debit message are identical the pacs.009 Financial Institution Credit Transfer message which represents the next stage of the journey should the Direct Debit be accepted.

From a business perspective authorisation of a direct debit instruction can be predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit scheme). Either third party debt authority could be granted to the Agent instructing of the Direct Debit, or the Payment Identification could be used to

Direct Debit Transaction Information

---

<!-- ELEMENT 441 -->
Min 1 - Max 1

The pacs message Payment Identification provides a set of elements to identify the payment, of which several are mandatory elements

---

<!-- ELEMENT 442 -->
# (continued)

Min 1 - Max 1

The pacs message Payment Identification also provides a set of optional elements to identify the direct debit transaction.

---

<!-- ELEMENT 443 -->
Min 0 - Max 1

The Financial  Institution  Direct Debit message Payment Type Information provides a set of optional elements where the payment type can be described.

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point Instruction Priority Min 0 - Max 1 information may be used by the Instructed Agent to differentiate the processing priority.

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

Service Level Min 0 - Max 3

A nested element which may either use an external ISO

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a StandingOrder.

Note: the ISO instrument codes are registered by specific community group(capturedin the code list)

Credit Instruction

Payment Type Information

---

<!-- ELEMENT 444 -->
The pacs.010 message (unlike  the pacs.008) has one element to capture the amount  of the Transfer, Interbank Settlement Amount .

Min 1 - Max 1

Interbank Settlement Amount

A mandated currency amount moved between the Instructing Agent and the Instructed Agent. This therefore is the point-to-point currencyamount exchanged, comparable with the MT Field 32

Note: the Financial Institution Direct Debit (pacs.010) has no Instructed Amount element, Exchange Rate or Charger Bearer (like the pacs.009) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

---

<!-- ELEMENT 445 -->
Min 1 - Max 1

The Financial Institution Direct Debit message Interbank Settlement Date captures the Date the transaction is completed/effected.

This Date element use ISODate YYYY-MM-DD

For example: 2002-10-10 (10 October 2002)

---

<!-- ELEMENT 446 -->
Min 0  - Max 1

The Financial Institution Direct Debit message Settlement Time Request captures the requested settlement time as a choice of nested elements.

Where Settlement TimeRequest is used the nested:

- CLS Time

- Till Time

- From Time

- Reject Time

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

may be used to capture information related to this time.

---

<!-- ELEMENT 447 -->
The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the Debtor . The Debtor sub elements describe the Debtor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Debtor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Debtor structured or unstructured

BICFI

Debtor

Postal

Address

---

<!-- ELEMENT 448 -->
Account

# Min 0 - Max 1

The Financial  Institution  Direct Debit message Debtor Account also provides an number  of optional nested element to identify the account for which debit and credit entries have been made.

# Min 1 - Max 1

a unique Identification for the account, between the Account Servicer and Account Owner. The element is further nested by choice of IBAN or Other to capture the account.

An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account.

The Currency for which the account is held. This is identified using the three characters ISO currency code.

The Name of the Account, as Assigned by the servicing institution.

Anested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 449 -->
# Min 0 - Max 1

The Debtor Agent is a static role in the pacs messages. This agent maintain  a relationship  with their customer, the Debtor . Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial  Institutions) maintain  a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain  the account of both the Debtor and Creditor.

# Min 0 - Max 1

Where the Debtor Agent is utilised  the Debtor Agent Account may optionally be used to capture the account of the Debtor Agent with the Agent immediate after them in the transaction chain (the Agent Serving their account) This would only apply where the message includes a Debtor Agent , however CBPRplus does not recommend to use this element unless mandated within a community  or bilaterally agreed.

Credit Instruction

Debtor Agent

---

<!-- ELEMENT 450 -->
The Instruction for Debtor Agent elements within the pacs.010 Financial Institution Direct Debit optionally provides information related to the processing of the direct debit instruction.

Min 0 - Max 1

The Instruction for Debtor Agent element offers a occurrence of free format information.

The use of this element should be bilaterally agreed with the Debtor Agent to maximize  the ability to Straight Through  Process the instruction.

---

<!-- ELEMENT 451 -->
The Purpose elements within the pacs.010 Financial Institution Direct Debit capture the reason for the payment transaction which would result from a successful direct debit. This element may either use an external ISO Purpose code or a proprietary code.

The purpose is used by the capture the nature of the payment e.g. CORT Trade Settlement Payment, CFEE Cancellation Fees etc. and should not be confused with Regulatory Reporting codes.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCDis classified within the Collateral categorisation, with the Name OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

---

<!-- ELEMENT 452 -->
The optional Remittance Information element within the pacs.010 Financial  Institution  Direct Debit is nested to provide Unstructured information related to payment.

Min 0 - Max 1

Remittance Information enable the matching/reconciliation  of an entry that the payment is intended to settle

# Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: like the pacs.009 Remittance Information can only be captured in an Unstructured element.

Remittance Information is  however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using

---

<!-- ELEMENT 453 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Financial Institution Direct Debit

Use Case p.10.1.1 - High Level Payment of a Financial Institution  Direct Debit (pacs.010) Use Case p.10.1.1.a   - High Level Book movement of a Financial Institution  Direct Debit (pacs.010) Use Case p.10.1.2 - High Level Rejection of a Financial Institution  Direct Debit (pacs.010)

---

<!-- ELEMENT 454 -->
1

2

2a

3

Agent C processes the payment on Agent D

Debtor Agent (B) debits the Debtor (Agent A) optionally provide  a notification e.g. credit notification in addition to an account statement (camt.053)

4

Agent E initiates a Direct Debit instruction to debit Agent A's account

Debtor Agent (B) initiates a serial payment towards the Creditor Agent (E) using Agents B & C as intermediaries

Agent D credits the account of the Creditor (Agent E), and may optionally provide  a notification e.g. credit notification in addition to an account statement (camt.053)

---

<!-- ELEMENT 455 -->
1

2a

Debtor Agent (B) debits the Debtor (Agent A) optionally provide  a notification e.g. credit notification in addition to an account statement (camt.053)

2b

Agent B credits the account of the Creditor (Agent C), and may optionally provide  a notification e.g. credit notification in addition to an account statement (camt.053)

Agent E initiates a Direct Debit instruction to debit Agent A's account

---

<!-- ELEMENT 456 -->
1

Agent D initiates a Direct Debit instruction to debit Agent A's account

Debtor Agent (B) rejects the instruction, using a pacs.002, as no mandate agreement is in place.

pacs.010

pacs.002

---

<!-- ELEMENT 457 -->
# Financial Institution Direct Debit - Margin Collection

---

<!-- ELEMENT 459 -->
The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor's account to the Creditor, where both Debtor and Creditor are

---

<!-- ELEMENT 461 -->
# Min 1 - Max 1

Each ISO 20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

---

<!-- ELEMENT 462 -->
The pacs.010 message Creation Date Time captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 463 -->
The pacs.0010 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 465 -->
Min 1 - Max 1

The Financial  Institution  Direct Debit Credit Identification provides a mandatory element to identify the Direct Debit instruction.

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT Financial Markets Direct Debit message.

---

<!-- ELEMENT 466 -->
Min 0 - Max 1

The pacs message Payment Type Information provides a set of optional elements where the payment type can be described. These elements are applied to the pacs.009 which results from this message.

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-topoint information may be used by the Instructed Agent to differentiate the processing priority.

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, SECU Transactionis the payment of securities.

---

<!-- ELEMENT 467 -->
# Agents

Instructing Agent and Instructed Agent represent the Agents involved  in the pacs point-to-point message exchange.  These roles therefore change on each message leg.

Instructing Agent and Instructed Agent elements are required in all pacs messages and is only available in the Credit Instruction.

---

<!-- ELEMENT 468 -->
The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 - Max 1

The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 - Max 1

The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

# Min 0 - Max 1

The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

---

<!-- ELEMENT 469 -->
# Agent Account

The Creditor Agent is a static role in the pacs messages. This agent maintain  a relationship  with their customer, the Creditor . Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial  Institutions) maintain  a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain  the account of both the Debtor and Creditor.

Min 0 - Max 1

Where the Creditor Agent is utilised  the Creditor Agent Account may optionally be used to capture the account of the Creditor Agent with the Agent immediate before them in the transaction chain  (the Agent Serving  their account)

This would only apply where the message includes a Creditor Agent , however CBPRplus does not recommend to use this element unless mandated within a community  or bilaterally agreed.

---

<!-- ELEMENT 470 -->
The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the Creditor . The Creditor sub elements describe the Creditor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Creditor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Creditor structured or unstructured

BICFI

Creditor

Postal

Address

---

<!-- ELEMENT 471 -->
Account

Min 0 - Max 1

The Financial  Institution  Direct Debit Creditor Account provides an optional element to identify the Creditor's Account for which the Direct Debit instruction  intends to instruct the movement  of money to.

# Min 1 - Max 1

a unique Identification for the account, between the Account Servicer and Account Owner. The element is further nested by choice of IBAN or Other to capture the account.

An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account.

The Currency for which the account is held. This is identified using the three characters ISO currency code.

The Name of the Account, as Assigned by the servicing institution.

Anested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 472 -->
# Information

The Financial  Institution  Direct Debit message Direct Debit Transaction Information nested element captures information  related to the Debit part of the transaction, such as the Debtor, the amount and settlement date.

It is important to recognise that the data elements contained in this part of the Direct Debit message are identical the pacs.009 Financial Institution Credit Transfer message which represents the next stage of the journey should the Direct Debit be accepted.

From a business perspective authorisation of a direct debit instruction can be predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit scheme). Either third party debt authority could be granted to the Agent instructing of the Direct Debit, or the Payment Identification could be used to

Direct Debit Transaction Information

---

<!-- ELEMENT 473 -->
Min 1 - Max 1

The pacs message Payment Identification provides a set of elements to identify the payment, of which several are mandatory elements

---

<!-- ELEMENT 474 -->
# (continued)

Min 1 - Max 1

The pacs message Payment Identification also provides a set of optional elements to identify the direct debit transaction.

---

<!-- ELEMENT 475 -->
# Min 0 - Max 1

The Financial  Institution  Direct Debit message Payment Type Information provides a set of optional elements where the payment type can be described.  These elements apply to the debit transaction, whereby the Credit Instruction has it own Payment Type Information.

Instruction Priority

Min 0 - Max 1

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

Service Level Min 0 - Max 3

A nested element which may either use an external ISO

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a StandingOrder.

Note: the ISO instrument codes are registered by specific community group(capturedin the code list)

Credit Instruction

Payment Type Information

---

<!-- ELEMENT 476 -->
The pacs.010 message (unlike  the pacs.008) has one element to capture the amount  of the Transfer, Interbank Settlement Amount .

Min 1 - Max 1

Interbank Settlement Amount

A mandated currency amount moved between the Instructing Agent and the Instructed Agent. This therefore is the point-to-point currencyamount exchanged, comparable with the MT Field 32

Note: the Financial Institution Direct Debit (pacs.010) has no Instructed Amount element, Exchange Rate or Charger Bearer (like the pacs.009) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

---

<!-- ELEMENT 477 -->
Min 1 - Max 1

The Financial Institution Direct Debit message Interbank Settlement Date captures the Date the transaction is completed/effected.

This Date element use ISODate YYYY-MM-DD

For example: 2002-10-10 (10 October 2002)

---

<!-- ELEMENT 478 -->
Min 0  - Max 1

The Financial Institution Direct Debit message Settlement Time Request captures the requested settlement time as a choice of nested elements.

Where Settlement TimeRequest is used the nested:

- CLS Time

- Till Time

- From Time

- Reject Time

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

may be used to capture information related to this time.

---

<!-- ELEMENT 479 -->
The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the Debtor . The Debtor sub elements describe the Debtor in greater detail.

Information used to identify a Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Debtor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Debtor structured or unstructured

BICFI

Debtor

Postal

Address

---

<!-- ELEMENT 480 -->
Account

Min 0 - Max 1

The Financial  Institution  Direct Debit message Debtor Account also provides an number  of optional nested element to identify the account for which debit and credit entries have been made.

# Min 1 - Max 1

a unique Identification for the account, between the Account Servicer and Account Owner. The element is further nested by choice of IBAN or Other to capture the account.

An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account.

The Currency for which the account is held. This is identified using the three characters ISO currency code.

The Name of the Account, as Assigned by the servicing institution.

Anested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 481 -->
# Agent Account

The Debtor Agent is a static role in  the pacs messages. This agent maintain  a relationship  with their customer, the Debtor . Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial  Institutions) maintain  a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain  the account of both the Debtor and Creditor.

Min 0 - Max 1

Where the Debtor Agent is utilised  the Debtor Agent Account may optionally be used to capture the account of the Debtor Agent with the Agent immediate after them in the transaction chain (the Agent Serving their account) This would only apply where the message includes a Debtor Agent , however CBPRplus does not recommend to use this element unless mandated within a community  or bilaterally agreed.

Credit Instruction

Debtor Agent

---

<!-- ELEMENT 482 -->
The Instruction for Debtor Agent elements within the pacs.010 Financial Institution Direct Debit optionally provides information related to the processing of the direct debit instruction.

Min 0 - Max 1

The Instruction for Debtor Agent element offers a occurrence of free format information.

The use of this element should be bilaterally agreed with the Debtor Agent to maximize  the ability to Straight Through  Process the instruction.

---

<!-- ELEMENT 483 -->
The Purpose elements within the pacs.010 Financial Institution Direct Debit capture the reason for the payment transaction which would result from a successful direct debit. This element may either use an external ISO Purpose code or a proprietary code.

The purpose is used by the capture the nature of the payment e.g. CCPC CCP Cleared Initial Margin and should not be confused with Regulatory Reporting codes.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example:

OTCDis classified within the Collateral categorisation, with the Name OTC Derivatives described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.

---

<!-- ELEMENT 484 -->
The optional Remittance Information element within the pacs.010 Financial  Institution  Direct Debit is nested to provide Unstructured information related to payment.

Min 0 - Max 1

Remittance Information enable the matching/reconciliation  of an entry that the payment is intended to settle

# Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: like the pacs.009 Remittance Information can only be captured in an Unstructured element.

Remittance Information is  however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using

---

<!-- ELEMENT 485 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Financial Institution Direct Debit

Use Case p.10.2.1 - High Level Payment Of A Financial Institution  Direct Debit (pacs.010)

Use Case p.10.2.2 - High Level Rejection Of A Financial Institution  Direct Debit (pacs.010)

---

<!-- ELEMENT 486 -->
# (pacs.010)

1

2

3

4

Agent E initiates a Direct Debit instruction to debit Agent A's account

Debtor Agent (B) initiates a serial payment towards the Creditor Agent (E) using Agents B & C as intermediaries

Agent C processes the payment on Agent D

Agent D credits the account of the Creditor (Agent E), and may optionally provide  a notification e.g. credit notification in addition to an account statement (camt.053)

---

<!-- ELEMENT 487 -->
# (pacs.010)

1

B

Agent D initiates a Direct Debit instruction to debit Agent A's account

Debtor Agent (B) rejects the instruction, using a pacs.002, as no mandate agreement is in place.

pacs.010

pacs.002

D

1

E

---

<!-- ELEMENT 488 -->
Financial Institution to Financial Institution Customer Direct Debit

---

<!-- ELEMENT 490 -->
The Financial Institution To Financial Institution Customer Direct Debit message is sent by the Creditor Agent to the Debtor Agent, directly or through other agents and/or a payment clearing and settlement system. It is used to collect funds from a Debtor account for a Creditor, whereby one or both of these Parties are non-

---

<!-- ELEMENT 492 -->
# Min 1 - Max 1

Each ISO 20022 payment message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's Direct Debit Transaction Information contains a variety of nested Payment Identification elements to capture reference related to the individual transaction such as a UETR(UniqueEnd-to-endTransactionReference)

---

<!-- ELEMENT 493 -->
The pacs.003 message Creation Date captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 494 -->
The pacs.003 message Number of Transactions captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines  is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- ELEMENT 495 -->
The pacs.003 Settlement Method element within the Group Header Settlement Information , includes one of the embedded codes to indicate how the payment message will be settled.

D

2 7

The Settlement Method element in the pacs.003 allows a choice of an embedded code.

INDA indicate this Customer Direct Debit will be settled by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated Settlement Account element.

INGA indicate this Customer Direct Debit has already been settled by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification

---

<!-- ELEMENT 496 -->
The pacs.003 message Settlement Account is a nested element as part of Settlement Information, this element identifies information related to an account used to settle the direct debit instruction.

Min 0 - Max 1

The Settlement Account identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the Settlement Method )

Min 1  - Max 1

Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Account Servicing Institution

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 498 -->
Min 1 - Max 1

The pacs message Payment Identification provides a set of elements to identify the payment, of which several are mandatory elements

---

<!-- ELEMENT 499 -->
# Min 1 - Max 1

The pacs message Payment Identification also provides a set of optional elements to identify the direct debit transaction.

---

<!-- ELEMENT 500 -->
The pacs message can be described.

Min 0 - Max 1

# Payment Type Information provides a set of optional elements where the payment type

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point Instruction Priority Min 0 - Max 1 information may be used by the Instructed Agent to differentiate the processing priority.

a choice of imbedded codes representing the clearing channel to be used to process direct debits.

A nested element which may either use an external ISO Service Level code* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group(captured in the code list)

Anested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the

---

<!-- ELEMENT 501 -->
The pacs.003 message has two key element to capture the amount of the Credit Transfer, Interbank Settlement Amount and Interbank Settlement Date .

Min 1 - Max 1

Interbank Settlement Amount

Min 1 - Max 1

A mandated currency amount moved between the Instructing Agent and the Instructed Agent. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32B

Interbank Settlement Date

A mandated date on which the Interbank Settlement should be executed between the Instructing Agent and the Instructed Agent. This therefore is the value date comparable with the MT Field 30

Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important one. Instructed Amount relates to the amount Instructed to be debited from the Debtor's account and only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not the

---

<!-- ELEMENT 502 -->
The pacs.003 message has two optional elements to capture the information  related to the settlement of the instructions.

Min 0 - Max 1

The Settlement Priority provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused with the Instruction Priority.

Note: where Settlement Priority of the pacs.003 is 'URGT' (Urgent) means the highest priority possible to process the direct debit settlement and the amount of money becomes available to the Creditor Agent.

Min 0 - Max 1

The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.

This DateTimecan be captured in two nested elements, Debit Date Time and Credit Date Time .

---

<!-- ELEMENT 503 -->
# Min 0 - Max 1

The Instructed Amount captures currency and amount instructed by the Creditor. This conditional element is required when the Interbank Settlement Amount is not the same currency and/or amount as originally instructed by the Creditor. For example, a charge is taken, or the transactions is convertedto another currency. This element is comparable with the legacy Field 33B.

# Min 0 - Max 1

The Exchange Rate captures the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency.

Note: a number of Cross Element Rules exist which relate to the Instructed Amount element. For example, if the Instructed Amount is  present and the

---

<!-- ELEMENT 504 -->
Min 1 - Max 1

The mandated Charge Bearer element uses an embedded code that is used to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

Note: SLEV is removed from CBPR+ usage guideline specifications.

---

<!-- ELEMENT 505 -->
Min 0 - Max *

The Charges Information element provides information  on the charges to be paid by the Charge Bearer . This element is comparable with MT Fields: 71F 'Senders Charges' and 71G 'Receiver's Charges'

In addition to the legacy MT message the pacs.003 Charge Information mandate the Agent, this represent the Agent for who the Charges are either; due (pre-paid charges) or has taken a charge (deduct from the transaction)

CBPR+ best practice recommends the use of the structured Agent BIC.

As the Charges Information element is repetitive it can capture charges related to previous legs of the payment transaction.

Note: As the Charge Information element has the capability to capture both charges deducted and charges included i.e. pre-paid charges, the use of the Interbank Settlement Amount and Instructed Amount elements play an important role.

---

<!-- ELEMENT 506 -->
Min 1 - Max 1

The pacs.003 message mandatory Requested Collection Date element, captures the date on which the creditor requests that the amount  of money is to be collected from the debtor.

It is defined by ISO Date expressed in the YYYY-MM-DD format .

---

<!-- ELEMENT 507 -->
# Direct Debit Transaction

Pre Notification

Min 0 - Max 1

The pacs.003 Direct Debit Transaction component  provides information specific to the direct debit mandate.

Mandate Related Information Min 0 - Max 1

Provides further details of the direct debit mandate signed between the creditor and the debtor. E.g., Mandate Identification, Date of Signature and Electronic Signature.

Creditor Scheme Identification Min 0 - Max 1

Credit party that signs the mandate, may be used if supported by the Direct Debit Schema. (see next page for additional detail on this nested element)

Pre Notification Identification Min 0 - Max 1

Unique and unambiguous identification of the pre-notification which is sent separately from the direct debit instruction.

---

<!-- ELEMENT 508 -->
Min 0 - Max 1

The Creditor Scheme Identification element within the pacs.003 message optionally provides information related to the credit party that signs the mandate who is different from the Creditor.

The Creditor Scheme  Identification element offers the following options:

Name Postal Address: Not used often Identification Country of Residence Contact Details

CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit Scheme.

---

<!-- ELEMENT 509 -->
The ISO 20022 pacs messages describe the party credited for a transaction as the

the

Creditor

Creditor

. The in greater detail.

Flor

Roan

Coutry

Creditor

Min 1 - Max 1

Nested element capturing either

Creditor structured or unstructured

address details

Nested element capturing the various types of identifiers for

Identification the party e.g. BIC, LEI etc.

Optional element to capture the Creditor's ISO

sub elements describe

Mandatory

Name

,  where a BIC

identifier is not provided, by which the party is known

Postal

Address

Name

Creditor

Country of

Residence

---

<!-- ELEMENT 510 -->
Min 0 - Max 1

The pacs.003 Creditor Account is used to capture the account information  for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The Creditor Account uses a variety of nested elements to capture information  related to the account.

Min 1  - Max 1

Identification identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Currency identifies the currency if the account

Name identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 511 -->
Min 1 - Max 1

Min 1 - Max 1

The Debtor Agent and Creditor Agent are static roles in the pacs.003 FI to FI Customer Direct Debit. These agent maintain  a relationship  with their customers; the Debtor and Creditor .

Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the pacs messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

---

<!-- ELEMENT 513 -->
The pacs.003 message introduces ultimate parties to the FI to FI Customer Direct Debit message. The Ultimate Creditor element should not be confused with an Initiating Party who may send a direct debit initiation request on behalf of the Creditor. (see dedication section on Initiating Party )

Min 0 - Max 1

- CBPR+ premise is that an Ultimate Debtor has no financial regulated direct account relationship  with the corresponding Debtor .

# Min 0 - Max 1

- CBPR+ premise is that an Ultimate Creditor has no financial regulated direct account relationship  with the corresponding Creditor .

An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor depending on the payment scenario)

---

<!-- ELEMENT 514 -->
Min 0 - Max 1

Min 1 - Max 1

The Initiating Party of a direct debit is often the Creditor themselves and therefore this optional element is not necessary. More often the Initiating Party is a third party providing direct debit collection services on behalf of the Creditor (often referred to as a Third Party Provider) whereby the Creditor maintains an account with the Creditor Agent but the Third Party Provider has authority to initiate collection on behalf of the Creditor. This is distinctly different from an Ultimate Party (such as Ultimate Creditor ) who instructs the Creditor to initiate a collection on their behalf.

In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the Initiating Party is often the Creditor , however the same context of a Third Party Provider can exist where the third party is responsible for collecting funds on behalf of the Creditor .

---

<!-- ELEMENT 516 -->
The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 - Max 1

The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 - Max 1

The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

# Min 0 - Max 1

The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 - Max 1

---

<!-- ELEMENT 517 -->
The ISO 20022 pacs messages describe the party debited for a transaction as the Debtor . The Debtor sub elements describe the Debtor in greater detail. Min 1 - Max 1

Mandatory Name (where a BIC identifier is not provided) by which the party is known

Nested element capturing either

Debtor structured or unstructured

address details

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Name

Postal

Address

Identification

Optional element to capture the Debtor's ISO

Debtor

Country of

Residence

Fost Box

Courtry

Ccdb

---

<!-- ELEMENT 518 -->
Min 1 - Max 1

The pacs.003 mandatory Debtor Account is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The Debtor Account uses a variety of nested elements to capture information related to the account.

Min 1  - Max 1

Identification identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Currency identifies the currency of the account

Name identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 519 -->
1

A children sports clubs (Creditor), collects its monthly membership fee via direct debit, against the parents (Debtor) of one of it members (Ultimate Debtor).

- Agent A, the Creditor Agent, 2

initiates a direct debit instruction by sending a pacs.003 message to the Debtor Agent (B).

- account of the Debtor, credits Agent and confirms the direct 3

4

Sports club, the Creditor who has a mandate* with the Debtor, initiates a direct debit instruction by sending a pain.008 message to their bank, Creditor Agent (A).

Debtor Agent (B) debits the the account of the Creditor debit status using a pain.002.

Debtor, receives a statement from their bank confirming  the monthly Debt Debit, for their child (Ultimate Debtors) sports club membership fee, has debited either account,

---

<!-- ELEMENT 520 -->
Min 0 - Max 1

The Purpose element within the pacs.003 FI to FI Customer Direct Debit captures the reason for the direct debit transaction which may either use an external ISO Purpose code or a proprietary code.

The purpose is used to capture the nature of the payment e.g. IVPT Invoice Payment, FEES Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Creditor.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.

For example, LOAR is classified within the Finance categorisation, with the Name Loan Repayment described as a repayment of loan to lender.

Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger special processing e.g. Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

---

<!-- ELEMENT 521 -->
Min 0 - Max 10

The Regulatory Reporting element within the pacs.003 FI to FI Customer Direct Debit is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

# Min 0 - Max 1

The Debit Credit Reporting Indicator utilises  an embedded choice of code to indicate whether the regulatory reporting information applies to the:

- DEBT (debit)

- CRED (credit) or

- BOTH

# Min 0 - Max 1

The Authority element captures the Name and Country code of the Authority/Entity requiring the regulatory reporting information.

Min 0 - Max * The Details element provides the detail on the regulatory reporting information.

---

<!-- ELEMENT 522 -->
The Related Remittance Information element within the pacs.003 FI to FI Customer Direct Debit is nested to provide information related to the handling of remittance information. This information is typically provided by the Creditor in the direct debit initiation request.

Min 0 - Max 1

The Remittance Identification captures a unique reference assigned by the initiating party of the collection to identify the remittance information sent separately from the direct debit instruction.

# Min 0 - Max 2

The Remittance Location Details uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- Method requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. EMAL (email)

- Electronic Address provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.

- Postal Address provides the postal address to which an agent is to send the remittance information

Remittance advices are typically considered as a traditional value added service provided by the Creditor Agent to the Creditor, in order to facilitate reconciliation for the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting messages. Remittance Information is a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022. Related Remittance Information and Remittance Information are mutually exclusive (can't both be present)

Business examples are emerging where information is externalised using a URL repository solution.

---

<!-- ELEMENT 523 -->
The optional Remittance Information element within the pacs.003 FI to FI Customer Direct Debit is nested to provide either Structured or Unstructured information related to direct debit collections, such as invoices.

Min 0 - Max 1

Remittance Information enable the matching/reconciliation  of an entry that the direct debit is intended to settle

Min 0 - Max 1

The Unstructured sub element captures free format Remittance Information which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Min 0 - Max *

The Structured element is nested capturing rich structured Remittance Information, and is unlimited  in its multiplicity, but must not exceed 9,000 characters of business information  (does not include the xml element identification)

The use of this nested element should  be bilaterally/multilaterally end-to-end transportation of this data.

Related Remittance Information and Remittance Information are agreed, to ensure

---

<!-- ELEMENT 524 -->
The bilaterally/multilaterally agreed Remittance Information which is Structured must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

# Direct Debit Transaction Information

---

<!-- ELEMENT 525 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Serial Financial Institution to Financial Institution Customer Direct Debit

Use Case p.3.1.1 - High Level FI to FI Customer Direct Debit (pacs.003) successful settlement

Use Case p.3.1.2 - High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement

---

<!-- ELEMENT 526 -->
1

2

3

4

Creditor Agent (A) relays the status ACSC (accepted settlement completed) to the Initiating Party, based upon a bilateral agreement

Creditor initiates a direct debit instruction to the Creditor Agent

Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method 'INDA'

The Debtor Agent debits the account of the Debtor, and may optionally provide  a notification e.g. debit notification in addition to an account statement (camt.053). The Debtor Agent also provides  a status update ACSC (accepted settlement completed) to the Creditor  Agent.

---

<!-- ELEMENT 527 -->
1

2

Creditor initiates a direct debit instruction to the Creditor Agent

Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method 'INDA'

3

4

Creditor Agent (A) relays the status RJCT  (Rejected)  to the Initiating Party with the rejection reason information

The Debtor Agent fails to debit the account of the Debtor (e.g., account is closed). The Debtor Agent provides  a status update RJCT (Rejected) with the rejection reason information.

---

<!-- ELEMENT 528 -->
# messages

---

<!-- ELEMENT 529 -->
# Cash Management Reporting

camt.052 - Bank to Customer Account Report camt.053 - Bank to Customer Statement

camt.054 - Bank to Customer Debit Credit Notification camt.057 -Notification To Receive

camt.058 -Notification To Receive Cancellation Advice camt.060 -Account Report Request

---

<!-- ELEMENT 530 -->
# Bank to Customer Account Report

---

<!-- ELEMENT 532 -->
Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Account Report message to Account Servicer and Account Owner. Whereby the report is send by the Account Servicer to the Account Ownerandor authorisednartv Iced to inform theaccount owner or authorisedpartv of the entries

---

<!-- ELEMENT 534 -->
Each ISO 20022 cash management reporting message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the Message Identification has no exact equivalent in the legacy MT Customer Statement message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.

---

<!-- ELEMENT 535 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 536 -->
# Min 0 - Max 1

The Bank to Customer Account Report Message Recipient nested element provides details of the party authorised by the Account Owner to receive the Account Report.

This element should only be used to identify the Message Recipient when different from the account owner, which is implied by the usage of COPY in the Copy Duplicate Indicator within the nested Statement element.

Where MessageRecipient is used the nested:

- Name Min 0 - Max 1

- PostalAddress Min 0 - Max 1

- Identification

- Min 0 - Max 1

- ContactDetails Min 0 - Max 1

may be used to capture information related to this party.

Group Header

Recipient

Message

---

<!-- ELEMENT 537 -->
Min 0 - Max 1

The Bank to Customer Account Report Original Business  Query element identifies a query to generate a report, for example a camt.060 Account Reporting Request.

Where Original Business Query is used the original Message identification (i.e., the message identification of the camt.060 message) is required. Original Message Name identification and Original Creation Date Time may also be provided. Min 1 - Max 1 Min 0 - Max 1 Min 0 - Max 1

---

<!-- ELEMENT 538 -->
Min 0 - Max 1

The Bank to Customer Account Report Additional Information element represents further details related to the account statement.

In accordance to the usage in the camt.053 this element could be used to describe additional information  to distinguish  the different camt.052 usage i.e., where the report is only reporting an intraday balance, intraday entries or both. Unlike  the camt.053 there is no recommended  identification string to represent usage.

Additional Information is a textual element restricted in CBPR+ to 500 characters.

---

<!-- ELEMENT 540 -->
# Min 1 - Max 1

The Bank to Customer Account Report Report element provides information related to an account, most typically associated with intraday account entries and or accounting balances (where entries have been processed on the account). The report element can be used to advise entries reported to the account (Intraday Statement), account balance information (Account Balance Report) or both.

The Report element has been restricted to one account report. To report additional accounts to the Account Owner this would need to occur via a separate message in a similar way to the legacy MT 942.

It should also be noted the Account Report message is modelled identically to the Account Statement (camt.053) therefore where used as an intraday transaction report

---

<!-- ELEMENT 541 -->
Similar to the legacy MT Intraday Reporting message (i.e., 942) the camt.052 Bank to Customer Account Report is constrained in CBPR+ by the FINplus service's message size. Consideration therefore need to be given (when reporting transactional information) to identifying; the report order , the report correlation andthe last report page .

Report Order: identifying the order in which statements should be processed or reconstituted. Options:

2

Report Correlation: identifying statement which relate to each other for  a given statement period. Options:

Legal Sequence Number

Last Report: identifying when no further statements for a given period are expected i.e. period statement in finalised.  Options:

Report Pagination, Last Page Indicator

---

<!-- ELEMENT 542 -->
Min 1 - Max 1

The Bank to Customer Account Report message Identification provides a mandatory element to identify the statement

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT statement message.

---

<!-- ELEMENT 543 -->
Min 1 - Max 1

The Bank to Customer Account Report message Report Pagination element provides the page number of the report.

Min 1 - Max 1

Min 1 - Max 1

ReportPagination includes the Page Number and Last Page indicator elements.

For example, a Page Number of 2 represents the current account report, being the second page of the and implying a previous account report page had been sent. The Last Page indicator further implies whether more pages are expected

Noted: as Report Pagination is required, even if there is only one page to the report being sent. Both the Page Number and Last Page indicator will need to be provided

---

<!-- ELEMENT 544 -->
The Bank to Customer Account Report message Electronic Sequence Number allows the Account Servicer to assign a number  to each Report which should  increment by 1 for each electronic statement report sent.

This element allows easy recognition of the Report order, equivalent to the legacy Field 28C Statement Number. The sequence should increment for each camt.052 message sent to the Account Owner or Authorised Party this number must be the same value where the statement continues over multiple pages ( Report Pagination ) of the report for a give account.

Should this sequence number be reset by the Account Servicer , this should not occur more frequently than once a day. Likewise, this 18 digit counter could be incremented to its maximum value before it's reset.

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the Account Servicer andthe Account Owner

---

<!-- ELEMENT 545 -->
Min 0 - Max 1

The Bank to Customer Account Report message Reporting Sequence specifies the choice of identification sequences. This can be used as an alterative to the Report Pagination or Electronic Sequence Number as a way to identify the report order, which is not confined to numeric values.

Where used the Reporting Sequence mandate a choice of nested element:

- From Sequence identifies the start of a sequence range. Min 1 - Max 1

- To Sequence identifies the end of a sequence range. Min 1 - Max 1

- From To Sequence identifies the start and end of a sequence range. Min 1 - Max *

- Equal Sequence identifies a sequence. Min 1 - Max *

- Not Equal Sequence identifies a sequence to be excluded. Min 1 - Max *

The Reporting Sequence  may be provided in the camt.060 Account Reporting request to specify, for example, a range of Statements to be sent. Alternatively, Account Reports can often be produced on a bilaterally agreed period basis.

---

<!-- ELEMENT 546 -->
The Bank to Customer Account Report message Legal Sequence Number allows the Account Servicer to assign a number to each report which should  increment by 1 for each Report sent.

Where the Intraday Account Report uses multiple camt.052 messages for a given report period the Legal Sequence Number must be the same number in each report message during that reporting period. This element can be considered an equivalent to the legacy Field 28C Statement Number

Either Electronic Sequence Number or Legal Sequence Number should be provided to enablethe identification of a report number.

---

<!-- ELEMENT 547 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 548 -->
Min 0 - Max 1

The Bank to Customer Account Report message From to Date allows the Account Servicer to specify the start date time and end date time applicable to the intraday account entries and or accounting  balances being reported.

For intraday account reports this is an important attribute that allows the account owner to understand  the period for which the report applies. The element is not mandatory as the report may only contain the balance, whereby the report Creation DateTime may be used to identify the date and time associated to the balance. Min 1 - Max 1 Min 1 - Max 1

Where From to Date is used the From Date Time and To Date Time become mandatory elements.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 549 -->
The Bank to Customer Account Report message Copy Duplicate Indicator is used as a choice to identify additional reports from the original sent to the Account Owner.

COPY is used when a copy of the report is sent to an Authorised Third Party, such as a company headoffice,parent entity, or an institution providing additional service.

DUPL is used when a duplicate of the report is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request.

CODU is used when a duplicate of a report copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in place with the Account Servicer.

---

<!-- ELEMENT 550 -->
Min 0 - Max 1

The Bank to Customer Account Report message Reporting Source allows the Account Servicer to define the source of the intraday account entry and or account balance report, typically associated with an application.

Reporting Source utilises the external Reporting Source code list. For example ACCT represents a statement or report based on accounting data, whereas DEPT represents a cash or deposit system.

Where the source of the statement is functionally required by the consumer of the statement i.e., the Account Owner or authorised Third Party , the codes used should be bilaterally agreed.

---

<!-- ELEMENT 551 -->
# Min 1 - Max 1

The Bank to Customer Account Report message Account provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath Account .

---

<!-- ELEMENT 552 -->
Min 1 - Max 1

Min 0 - Max 1

The Bank to Customer Account Report message mandatory Account also provides a number  of optional nested element to identify the account for which debit and credit entries have been made.

---

<!-- ELEMENT 553 -->
# Min 0 - Max 1

The Bank to Customer Account Report message Related Account allows the identification of a related parent account for the account report. For example sweeping, pooling or virtual account for which the report is produced can identify the parent account they hierarchically  relate to.

Min 1 - Max 1

When Related Account is utilized, like Account , the Identification and Currency element become mandatory.

Additionally, the nested Type element, Name and nested Proxy element are optionally Min 0 - Max 1 Min 0 - Max 1 Min 0 - Max 1

available.

Related Account uses a variety of common elements described in more detail within the Account section.

---

<!-- ELEMENT 554 -->
Interest

Min 0 - Max *

The Bank to Customer Account Report message Interest provides interest information  that applies to the account.

Type

An element which may either use an embedded ISO Interest Type code; INDY (Intraday) OVRN (Over Night) or a proprietary code. It is used to identifier a particular interest type.

Rate

The type of interest Rate defined as a Percentage and in an Other form. Validity Range optionally defines an Amount , Credit Debit Indicator and Currency .

From To Date

The date range for which interest has been calculated. From Date Time and To Date Time must be representing when usingthis element.

Reason

Provides

Theoptional Reason for which interest is applied.

details on

any tax

applied to

the

Interest.

Where optional

---

<!-- ELEMENT 556 -->
Balance Type code are used within the nested Balance element to represent the type/s of balance being reported. In comparison the legacy MT 941 utilizes different Fields and Tag options to represent a number  of these Balance Types. The below extract from the externalised ISO Balance Type code list compares the code with the population of the equivalent  information in the Legacy MT 941 Balance Report.

---

<!-- ELEMENT 557 -->
The Bank to Customer Account Report message mandatory Balance also provides the optional set of nested element to define a Credit Line

The true/false Boolean of Included to clearly determine whether the Credit Line Amount is included in the balance is mandatory in the set of Credit Line element.

Additionally, the following optional nested element may be used to identify:

- The Type of Credit Line, which may either use an external ISO Credit Line Type code or a proprietary code.

- A set of elements to provide Credit Line details

- The Amount (Currency and Amount) of the Credit Line

- The Date (nested as Date, DateTime) of the Credit Line, provided to distinguish wheremultiple Credit Line exist.

The final optional nested element within Balance is the Availability of the booked amount i.e., when it is available to be accessed.

The Credit Line element is unlimited (Max *) whereby more that one Credit Line may be reported, the Date becomes an important element to distinguish between different Credit Lines.

---

<!-- ELEMENT 558 -->
Min 0 - Max 1

The Bank to Customer Account Report message optional Transaction Summary provides a set of nested element to summarize  entry information. Where the intraday account entries and or accounting  balances are reported using multiple  camt.052 messages for a given  reporting period the Transaction Summary should  only be included  on the first Report message ( Balance Type OPBD with no Balance Sub Type )  summarizing the whole Statement Report (entire statement period) This aligns with the Common Global Implementation (CGI) where a Transaction Summary ,  if provided, would appear before the first Entry elements.

Each of the following element allow an optional total of entries either as a Number of Entries and or as a Sum .

- Total Entries

- Total Credit Entries

- Total Debit Entries

- Total Entries Per Bank Transaction Code

Min 0 - Max *

In addition to the Number of Entries and Sum , the Total Entries Per Bank Transaction Code requires the Bank Transaction Code element and optionally allows a variety of other optional elements. Min 1 - Max 1

The Total Entries Per Bank Transaction Code element is unlimited (Max  *) whereby more that one Bank Transaction Code may be summarised.

---

<!-- ELEMENT 559 -->
Min 0 - Max *

The Bank to Customer Account Report message optional Entry provides a significant variety of nested elements to represent the details associated with each Entry . For active accounts which have intraday entries posted across them, this set of nested elements is arguably the most relevant for the account owner and in many way is comparable with the MT 942 Field 61 Statement Line.

---

<!-- ELEMENT 561 -->
Mandatory element representing the status using an external ISO Entry Status code for example BOOK is used to confirm the entry is booked.

Status BOOK is the only status that can be reversed using the Reverse Indicator

Mandatory choice of Date or Date Time the entry was posted to the Account .  This  can be compared to Field 61 subfield 2 of the legacy MT 942.

Mandatory choice of Date or Date Time the entry become available. This can be compared to Field 61 subfield 1 of the legacy MT 942.

Noting CBPR+ usage guidelines mandate the time zone that the Date Time represents as an offset against Universal Time Coordinated (UTC)

Additional optional Reference typically assigned by the Account Servicer's payment engine or accounting platform. This reference would be used to query an entry. This can be compared to Field 61 subfield 8 of the legacy MT 942.

Indicates when the booked amount is available i.e., when it is available to be accessed.

---

<!-- ELEMENT 562 -->
The Bank Transaction Code is designed to deliver a harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the account servicer to correctly report a transaction, which in its turn will help account owners to perform their cash management and reconciliation operations.

The structure of the Bank Transaction Code has three levels:

Domain :  Highest definition level to identify the subledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.) Family :  Medium definition level e.g. type of payment; credit transfer, direct debit etc. Sub-family :  Lowest definition level e.g. type of cheques; draft etc.

Bank Transaction Codes are an external code set defined in the Bank Transaction Code combinations external code sets.

---

<!-- ELEMENT 564 -->
Bank Transaction Codes are an external code set defined in the Bank Transaction Code combinations external code sets.

As an example a debit statement transaction which relates to a cross-border payment initiated from an account would be represented by:

---

<!-- ELEMENT 565 -->
Optional element indicating, as a Boolean, whether the entry is exempt from commission. This element is not typically associated with Correspondent Banking payments

Optional element indicating whether the underlying transaction details are provided through a separate message. Where the Message Name Identification represents the message used to provide the additional information and Message Identification specifies the reference of the message that provides the additional information.

Optional nested element which provides various elements to represent an aggregated (consolidated) original amount. Where individual transaction amounts can be represented, if required, within the Entry Detail set of elements.

This element is useful to capture original amount details where they are different to the Entry , Amount ,  for  example the Instructed Amount of the payment can be included, together with a potential Currency Exchange rate, where necessary.

Optional nested element to provide information on charges either pre-advised or taken from the entry.

---

<!-- ELEMENT 566 -->
Optional element which may either use an external ISO Technical Input Channel code or a proprietary code used to represent the technical channel used to input the entry.

Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry amount.

Optional nested element which provides details associated with a card transaction such as the card number, card brand etc.

Additional optional nested element containing details on the entry. See dedicated section on Entry Details .

Additional optional element to represent further information related to the account

---

<!-- ELEMENT 567 -->
Min 0 - Max *

The Bank to Customer Account Report message optional Entry Details provides a variety of nested elements to represent the details associated with each Entry .

Batch provides details on batched transactions such as the total Number of Transactions the batched entry (sometimes referred to as a consolidated entry) represents.

is a significant nested element which represents information on the

Transaction Details underlying  transaction.

---

<!-- ELEMENT 568 -->
Min 0 - Max *

When the Bank to Customer Account Report message optional Entry Details is utilized  the nested Details element is mandatory.

Transaction Details has a variety of nested elements closely associated with Entry level elements. The References element however is nested to include  a variety of references related to the entry including  for example the UETR

Credit Debit Indicator Min 1 - Max 1

Min 0 - Max 1

Bank

Transaction

Code

Additionally, Transaction Details also has a variety of elements capturing details from the underlying transaction, which amongst other business  transactions includes  payment transaction data. For example, Remittance Information and Related Parties

---

<!-- ELEMENT 569 -->
Min 0 - Max 1

Min 0 - Max 1

The Bank to Customer Account Report message Related Parties and Related Agents represents a set of optional nested elements related to the underlying  transaction. Where the Entry Details (the set of elements Related Parties/Agents belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message.

These Related Parties include  : These Related Agents include  :

- Instructing Party

- Debtor

- Debtor Account

- Ultimate Debtor

- Creditor

- Creditor Account

- Ultimate Creditor

- Instructing Agent

- Instructed Agent

- Debtor Agent

- Creditor Agent

- Intermediary Agent 1

- Intermediary Agent 2

- Intermediary Agent 3

Trading Party is also present in the Related Parties elements, and the following are present in the Related Agents elements: Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place . Although  these elements are not directly associated with a payment, as a Customer receiving an Account Report related to other Business Domains e.g. a Security

---

<!-- ELEMENT 570 -->
The Bank to Customer Account Report message Entry Details have a number  of additional elements beyond Related Parties and Related Agents to capture information  from the underlying  payment.

# These are:

- Local Instrument

- Purpose

- Related Remittance Information

- Remittance Information

- Related Dates such as the Interbank Settlement Date

- Tax

For Payment Return (pacs.004) it is also possible to capture Return Information which includes:

- The Original Bank Transaction Code of the original Entry

- The Originator of the return from the pacs.004

- And the Reason code.

Remittance Information as an end-to-end  element should be passed unaltered  from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account

---

<!-- ELEMENT 571 -->
It should also be mentioned  that the Bank to Customer Account Report message Entry Details have a number of additional elements which capture information  from transactions in other business  domains beyond payments, as well as have an element to capture Additional Transaction Information .

# These are:

- Related Quantity

- Financial Instrument Identification

- Corporate Action

- Safekeeping Account

- Cash Deposit

- Card Transactions

---

<!-- ELEMENT 572 -->
# Use case should be considered as a principal example whereby use case may be cross referenced

# Bank to Customer Reports

Use Case c.52.1.a - Bank to Customer Account Balance Report produced by the Creditor Agent

Use Case c.52.1.b - Bank to Customer Account Intraday  Transaction Report produced by the Creditor Agent

Use Case c.52.1.b.1 - Bank to Customer Account Intraday  Transaction Report/s and Account Statement produced by the Creditor Agent

Use Case c.52.1.c - Bank to Customer Account Intraday  Transaction and Balance Report produced by the Creditor Agent

Use Case camt.060 for requesting a Bank to Customer report

---

<!-- ELEMENT 573 -->
1

2

- Agent B processes the payment 3

on Agent C

- Agent C processes the payment 4

on Agent D

5

6

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Creditor Agent credits the account of the Creditor

Creditor Agent as the Account Servicer  produces and sends a balance report to either the Account Owner, or an authorised third party.

---

<!-- ELEMENT 574 -->
# Creditor Agent

1

2

- Agent B processes the payment 3

on Agent C

- Agent C processes the payment 4

on Agent D

5

6

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Creditor Agent credits the account of the Creditor

Creditor Agent as the Account Servicer  produces and sends a balance report to either the Account Owner, or an authorised third party.

---

<!-- ELEMENT 575 -->
# Statement produced by the Creditor Agent

---

<!-- ELEMENT 576 -->
# by the Creditor Agent

1

2

- Agent B processes the payment 3

on Agent C

- Agent C processes the payment 4

on Agent D

5

6

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Creditor Agent credits the account of the Creditor

Creditor Agent as the Account Servicer  produces and sends a intraday transaction and balance report to either the Account Owner, or an authorised third party.

---

<!-- ELEMENT 577 -->
# Bank to Customer Statement

---

<!-- ELEMENT 579 -->
Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Statement message to Account Servicer and Account Owner. Whereby the statement is send by the Account Servicer to the Account Iced to inform theaccount owner of the entries

---

<!-- ELEMENT 580 -->
Like the legacy MT Statement messages, the camt.053 Bank to Customer Account Statement is constrained in CBPR+ by the FINplus service's message size. Account Owner who needs to translate the camt.053 into the legacy MT 940 format has several considerations for the Account Serving Institution.

ISO 20022 message element

Statement Identification

Legal Sequence Number

Statement Pagination

- Account (Identification)

Balance Type

OPBD (with no Sub Type INTM)

OPBD (with Sub Type INTM )

Entry

Balance Type

CLBD (with no Sub Type INTM)

MT Field Name & (Tag option)

needed to create MT 940 Field 20 Transaction Reference Number needed to create MT 940 Field 28C Statement Number

needed to create MT 940 Field 28C Sequence Number needed to create MT 940 Field 25a  Account Identification

needed to create MT 940 Field 60F  (first) Opening Balance needed to create MT 940 Field 60M (intermediate) Opening Balance used to create MT 940 Field 61 Statement Line

Note up to 190 Entry occurrences will translate into a basic MT 940 (inside of the existing MT 940 message size)

needed to create MT 940 Field 62F  (final) Closing Balance

---

<!-- ELEMENT 581 -->
Interest rate changes on an account can be communicated using the camt.053. An Account Serving Institution who is considering the camt.053 to communicate such rate changes to the Account Owner may find the following comparison against the legacy MT 935 useful. However, compared the camt.053 to legacy MT, using the camt.053 is like combining the information of both the MT 935 and MT 940 together into one message.

# MT Field Name & (Tag option)

- Transaction Reference Number (Field 20) Sequence

- Further Identification (Field 13C)

- Account Identification (Field 25)

- Effective Date of New Rate (Field 30)

- New Interest Rate (Field 37H)

- Sender To Receiver Information (Field 72)

# NOT MAPPED

NOT MAPPED

ISO 20022 message element

- Group Header / Message Identification

- Statement / Account / Identification

- Statement / Interest / From Date

- Statement / Interest / Rate

---

<!-- ELEMENT 583 -->
Each ISO 20022 cash management reporting message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the Message Identification has no exact equivalent in the legacy MT Customer Statement message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.

---

<!-- ELEMENT 584 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 585 -->
# Min 0 - Max 1

The Bank to Customer Statement Message Recipient nested element provides details of the party authorised by the Account Owner to receive the Account Statement.

This element should only be used to identify the Message Recipient when different from the account owner, which is implied by the usage of COPY in the Copy Duplicate Indicator within the nested Statement element.

Where MessageRecipient is used the nested:

- Name Min 0 - Max 1

- PostalAddress Min 0 - Max 1

- Identification

- Min 0 - Max 1

- ContactDetails Min 0 - Max 1

may be used to capture information related to this party.

Group Header

Recipient

Message

---

<!-- ELEMENT 586 -->
Min 0 - Max 1

The Bank to Customer Statement Original Business  Query element identifies a query to generate a report, for example a camt.060 Account Reporting Request.

Where Original Business Query is used the original Message identification (i.e., the message identification of the camt.060 message) is required. Original Message Name identification and Original Creation Date Time may also be provided. Min 1 - Max 1 Min 0 - Max 1 Min 0 - Max 1

---

<!-- ELEMENT 587 -->
# Min 0 - Max 1

The Bank to Customer Statement Additional Information element represents further details related to the account statement.

Where the camt.053 is used for various end of cycle statement reporting (statement periods) the follow codes may be used to distinguish  the different camt.053 usage:

/EODY/ for End of Day - Daily Statement

/EOWK/ for End of Week - Weekly Statement

/EOMH/ for End of Month - Monthly Statement

/EOYR/ for End of Y ear - Y early Statement

Additional Information is a textual element restricted in CBPR+ to 500 characters.

---

<!-- ELEMENT 589 -->
The Bank to Customer Account Statement Statement nested element reports information  related to an account, most typically associated with account balances, and accounting  entries (where entries have been processed on the account).

The Statement element has been restricted to one statements. To report additional account statements to the Account Owner this would need to occur via a separate message in a similar way to the legacy MT 940 or MT 950.

It should also be noted the Account Statement message is modelled identically to the Account Report (camt.052) therefore where an intraday transaction report is used the

---

<!-- ELEMENT 590 -->
Similar to the legacy MT Statement messages the camt.053 Bank to Customer Account Statement is constrained in CBPR+ by the FINplus service's message size. Consideration therefore need to be given to identifying; the statement order , the statementcorrelation andthe last statement page .

Statement Order: identifying the order in which statements should be processed or reconstituted. Options:

identifying statement

Statement Correlation:

which relate to each other for  a given statement period. Options:

Legal Sequence Number

Last Statement: identifying when no further statements for a given period are expected i.e. period statement in finalised.  Options:

---

<!-- ELEMENT 591 -->
The Bank to Customer Statement message Identification provides a mandatory element to identify the statement

Unique reference assigned by the account servicer to unambiguously identify the account statement. Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT statement message.

---

<!-- ELEMENT 592 -->
Min1 - Max 1

The Bank to Customer Statement message Statement Pagination element provides the page number of the statement.

Min 1 - Max 1

Min 1 - Max 1

Statement Pagination includes the Page Number and Last Page indicator elements.

For example a Page Number of 2 represents the current account statement, being the second page of the and implying a previous account statement page had been sent. The Last Page indicator further implies whether more pages are expected

Note: Where Page Number is equal to 1 a Balance Type OPBD (Opening Booked)must be provided, without a sub type of INTM (Interim). Whereas if the Page Number is greater than 1 a Balance Type OPBD (Opening Booked) must be provided, with a sub type of INTM (Interim).

Where Last Page Indicator is true a Balance Type CLBD (Closing Booked) must be provided, without a sub type of INTM (Interim). Whereas if the Last Page Indicator is false a Balance Type CLBD (Closed Booked) must be provided, with a sub type of INTM (Interim).

---

<!-- ELEMENT 593 -->
The Bank to Customer Statement message Electronic Sequence Number allows the Account Servicer to assign a number to each statement which should increment  by 1 for each electronic statement report sent.

This element allows easy recognition of the statement order, equivalent to the legacy Field 28C Statement Number. The sequence should increment for each camt.053 electronic statement sent to the Account Owner or Authorised Party this number must be the same value where the statement continues over multiple pages ( Statement Pagination ) of the statement for a give account on a given day.

Should this sequence number be reset by the Account Servicer , this should not occur more frequently than once a year. Likewise, this 18 digit counter could be incremented to its maximum value before it's reset.

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the Account Servicer andthe Account Owner.

---

<!-- ELEMENT 594 -->
Min 0 - Max 1

The Bank to Customer Statement message Reporting Sequence specifies the choice of identification sequences. This can be used as an alterative to the Statement Pagination or Electronic Sequence Number as a way to identify the statement order, which is not confined to numeric values.

Where used the Reporting Sequence mandate a choice of nested element:

- From Sequence identifies the start of a sequence range. Min 1 - Max 1

- To Sequence identifies the end of a sequence range. Min 1 - Max 1

- From To Sequence identifies the start and end of a sequence range. Min 1 - Max *

- Equal Sequence identifies a sequence. Min 1 - Max *

- Not Equal Sequence identifies a sequence to be excluded. Min 1 - Max *

The Reporting Sequence  may be provided in the camt.060 Account Reporting request to specify, for example, a range of Statements to be sent. More traditionally Account Statements are generated automatically on an end of day cycle.

---

<!-- ELEMENT 595 -->
The Bank to Customer Statement message Legal Sequence Number allows the Account Servicer to assign a number to each statement which should increment by 1 for each statement report sent.

Where the statement is reported using multiple camt.053 messages for a given statement period the Legal Sequence Number must be the same number in each statement message,as it can be used to correlate the statements.

Where a paper statement is a legal requirement, it may have a number different from the electronic sequential number. In this case the Legal Sequence Number element represents the sequence number of the paper statement.

Either Electronic Sequence Number or Legal Sequence Number must be provided to enablethe identification of a statement number.

---

<!-- ELEMENT 596 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 597 -->
# Min 0 - Max 1

The Bank to Customer Statement message From to Date allows the Account Servicer to specify the start date time and end date time applicable to the statement.

Where From to Date is used the From Date Time and To Date Time become mandatory elements. Min 1 - Max 1 Min 1 - Max 1

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 598 -->
The Bank to Customer Statement message Copy Duplicate Indicator is used as a choice to identify additional statement from the original sent to the Account Owner.

COPY is used when a copy of the statement is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service such as liquidity sweeping or statement consolidation.

DUPL is used when a duplicate of the statement is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request.

CODU is used when a duplicate of a statement copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in place with the Account Servicer.

---

<!-- ELEMENT 599 -->
The Bank to Customer Statement message Reporting Source allows the Account Servicer to define the source of the statement, typically associated with an application.

Reporting Source utilises the external Reporting Source code list. For example ACCT represents a statement or report based on accounting data, whereas DEPT represents a cash or deposit system.

Where the source of the statement is functionally required by the consumer of the statement i.e., the Account Owner or Authorised Third Party , the codes used should be bilaterally agreed.

---

<!-- ELEMENT 600 -->
Min 1 - Max 1

The Bank to Customer Statement message Account provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath Account .

---

<!-- ELEMENT 601 -->
# Min 1 - Max 1

Min 0 - Max 1

The Bank to Customer Statement message mandatory Account also provides a number of optional nested element to identify the account for which debit and credit entries have been made.

An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account.

The Name of the Account, as Assigned by the servicing institution.

A nested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO Proxy Account Type code or a proprietary code.

A nest element that contains the Party that legally owns the account.

A nested element which identifies the Financial Institution who manages

---

<!-- ELEMENT 602 -->
# Min 0 - Max 1

The Bank to Customer Statement message Related Account allows the identification  of a related parent account for the account statement. For example, sweeping, pooling or virtual account for which the statement is produced can identify the parent account they hierarchically  relate to.

Min 1 - Max 1

When Related Account is utilized, like Account , the Identification and Currency element become mandatory.

Additionally the nested Type element, Name and nested Proxy element are optionally available. Min 0 - Max 1 Min 0 - Max 1 Min 0 - Max 1

Related Account uses a variety of common elements described in more detail within the Account section.

---

<!-- ELEMENT 604 -->
Min 1 - Max *

The Bank to Customer Statement message mandatory Balance provides nested element to define the account balance at a specific point in time. The following four elements nested beneath Balance are mandatory

---

<!-- ELEMENT 605 -->
Balance Type code are used within the nested Balance element to represent the type/s of balance being reported. In comparison the legacy MT 940 utilizes different Fields and Tag options to represent a number  of these Balance Types. The below extract from the externalised ISO Balance Type code list compares the code with the population of the equivalent  information in the Legacy MT 940 Customer Statement.

---

<!-- ELEMENT 606 -->
The Bank to Customer Statement message mandatory Balance also provides the optional set of nested element to define a Credit Line

The true/false Boolean of Included to clearly determine whether the Credit Line Amount is included in the balance is mandatory in the set of Credit Line element.

Additionally, the following optional nested element may be used to identify:

- The Type of Credit Line, which may either use an external ISO Credit Line Type code or a proprietary code.

- A set of elements to provide Credit Line details

- The Amount (Currency and Amount) of the Credit Line

- The Date (nested as Date, DateTime) of the Credit Line, provided to distinguish wheremultiple Credit Line exist.

The final optional nested element within Balance is the Availability of the booked amount i.e., when it is available to be accessed.

The Credit Line element is unlimited (Max *) whereby more that one Credit Line may be reported, the Date becomes an important element to distinguish between different Credit Lines.

---

<!-- ELEMENT 607 -->
Min 0 - Max 1

The Bank to Customer Statement message optional Transaction Summary provides a set of nested element to summarize  entry information. Where the statement is reported using multiple camt.053 messages for a given statement period the Transaction Summary should  only be included on the opening Statement message ( Balance Type OPBD with no Balance Sub Type )  summarizing the whole Statement Report (entire statement period) This aligns with the Common Global Implementation (CGI) where a Transaction Summary ,  if  provided,  would appear before the first Entry elements.

Each of the following element allow an optional total of entries either as a Number of Entries and or as a Sum .

- Total Entries

- Total Credit Entries

- Total Debit Entries

- Total Entries Per Bank Transaction Code

Min 0 - Max *

In addition to the Number of Entries and Sum , the Total Entries Per Bank Transaction Code requires the Bank Transaction Code element and optionally allows a variety of other optional elements. Min 1 - Max 1

The Total Entries Per Bank Transaction Code element is unlimited (Max  *) whereby more that one Bank Transaction Code may be summarised.

---

<!-- ELEMENT 608 -->
Unlike the legacy MT Statement messages, the camt.053 has a number of dedicated elements to capture a variety of entry level data.

It also has a number of enhancements on the legacy MT Statement message where parties in the payment and customer remittance information, as examples, can provided to the Account Owner.

# Min 0 - Max *

The Bank to Customer Statement message optional Entry provides a significant  variety of nested elements to represent the details associated with each Entry . For active accounts which have entries posted across them, this set of nested elements is arguably the most relevant for the account owner and in many way is comparable with the MT 940 Field 61 Statement Line.

Min 1 - Max 1

Credit Debit Indicator

Min 0 - Max 1

Account Servicer Reference

Min 0 - Max 1

Amount Details

Min 0 - Max *

Min 0 - Max 1

Reversal Indicator

Min 0 - Max 1

Min 1 - Max 1

Bank Transaction Code

Technical Input Channel Min 0 - Max 1

Min 0 - Max 1

Booking Date

Min 0 - Max 1

Commission Waiver Indicator

Min 0 - Max 1

Min 1 - Max 1

Value Date

Min 0 - Max 1

Additional Information Indicator

Min 0 - Max 1

---

<!-- ELEMENT 610 -->
Mandatory element representing the status using an external ISO Entry Status code for example BOOK is used to confirm the entry is booked.

Status BOOK is the only status that can be reversed using the Reverse Indicator

Mandatory choice of Date or Date Time the entry was posted to the Account .  This  can be compared to Field 61 subfield 2 of the legacy MT 940.

Mandatory choice of Date or Date Time the entry become available. This can be compared to Field 61 subfield 1 of the legacy MT 940.

Noting CBPR+ usage guidelines mandate the time zone that the Date Time represents as an offset against Universal Time Coordinated (UTC)

Additional optional Reference typically assigned by the Account Servicer's payment engine or accounting platform. This reference would be used to query an entry. This can be compared to Field 61 subfield 8 of the legacy MT 940.

Indicates when the booked amount is available i.e., when it is available to be accessed.

---

<!-- ELEMENT 611 -->
The Bank Transaction Code is designed to deliver a harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the account servicer to correctly report a transaction, which in its turn will help account owners to perform their cash management and reconciliation operations.

The structure of the Bank Transaction Code has three levels:

Domain :  Highest definition level to identify the subledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.) Family :  Medium definition level e.g. type of payment; credit transfer, direct debit etc. Sub-family :  Lowest definition level e.g. type of cheques; draft etc.

Bank Transaction Codes are an external code set defined in the Bank Transaction Code combinations external code sets.

---

<!-- ELEMENT 613 -->
Bank Transaction Codes are an external code set defined in the Bank Transaction Code combinations external code sets.

As an example a debit statement transaction which relates to a cross-border payment initiated from an account would be represented by:

---

<!-- ELEMENT 614 -->
Optional element indicating, as a Boolean, whether the entry is exempt from commission. This element is not typically associated with Correspondent Banking payments

Optional element indicating whether the underlying transaction details are provided through a separate message. Where the Message Name Identification represents the message used to provide the additional information and Message Identification specifies the reference of the message that provides the additional information.

Optional nested element which provides various elements to represent an aggregated required, within the Entry Detail set of elements.

This element is useful to capture original amount details where they are different to the Entry Amount ,  for  example the Instructed Amount potential Currency Exchange rate, where necessary.

(consolidated) original amount. Where individual transaction amounts can be represented, if , of the payment can be included, together with a

Optional nested element to provide information on charges either pre-advised or taken from the entry.

---

<!-- ELEMENT 615 -->
Optional element which may either use an external ISO Technical Input Channel code or a proprietary code used to represent the technical channel used to input the entry.

Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry amount.

Optional nested element which provides details associated with a card transaction such as the card number, card brand etc.

Additional optional nested element containing details on the entry. See dedicated section on Entry Details .

Additional optional element to represent further information related to the account

---

<!-- ELEMENT 616 -->
Min 0 - Max *

The Bank to Customer Statement message optional Entry Details provides a variety of nested elements to represent the details associated with each Entry .

Batch provides details on batched transactions such as the total Number of Transactions the batched entry (sometimes referred to as a consolidated entry) represents.

is a significant nested element which represents information on the

Transaction Details underlying  transaction.

---

<!-- ELEMENT 617 -->
Min 0 - Max *

When the Bank to Customer Statement message optional Entry Details is utilized  the nested Transaction Details element is mandatory.

Transaction Details has a variety of nested elements closely associated with Entry level elements. The References element however is nested to include  a variety of references related to the entry including  for example the UETR

Credit Debit Indicator Min 1 - Max 1

Min 0 - Max 1

Bank

Transaction

Code

Additionally, Transaction Details also has a variety of elements capturing details from the underlying transaction, which amongst other business  transactions includes  payment transaction data. For example, Remittance Information and Related Parties

Amount element within CBPR+ allows up to 18 digits unlike the payment messages. It allows entries reported for

---

<!-- ELEMENT 618 -->
Min 0 - Max 1

Min 0 - Max 1

The Bank to Customer Statement message Related Parties and Related Agents represents a set of optional nested elements related to the underlying  transaction. Where the Entry Details (the set of elements Related Parties/Agents belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management  (camt) message.

These Related Parties include  : These Related Agents include  :

- Instructing Party

- Debtor

- Debtor Account

- Ultimate Debtor

- Creditor

- Creditor Account

- Ultimate Creditor

- Instructing Agent

- Instructed Agent

- Debtor Agent

- Creditor Agent

- Intermediary Agent 1

- Intermediary Agent 2

- Intermediary Agent 3

Trading Party is also present in the Related Parties elements, and the following are present in the Related Agents elements: Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place . Although  these elements are not directly associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security

---

<!-- ELEMENT 619 -->
The Bank to Customer Statement message Entry Details have a number of additional elements beyond Related Parties and Related Agents to capture information  from the underlying  payment.

# These are:

- Local Instrument

- Purpose

- Related Remittance Information

- Remittance Information

- Related Dates such as the Interbank Settlement Date

- Tax

For Payment Return (pacs.004) it is also possible to capture Return Information which includes:

- The Original Bank Transaction Code of the original Entry

- The Originator of the return from the pacs.004

- And the Reason code.

Remittance Information as an end-to-end  element should be passed unaltered  from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account

---

<!-- ELEMENT 620 -->
It should also be mentioned  that the Bank to Customer Statement message Entry Details have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture Additional Transaction Information .

# These are:

- Related Quantity

- Financial Instrument Identification

- Corporate Action

- Safekeeping Account

- Cash Deposit

- Card Transactions

---

<!-- ELEMENT 621 -->
# Use case should be considered as a principal example whereby use case may be cross referenced

# Bank to Customer Statements

Use Case c.53.1.a - Bank to Customer Statement produced by the Creditor Agent

Use Case c.53.1.b - Bank to Customer Statement produced by the Debtor Agent

Use Case c.53.1.c - Bank to Customer Statement produced by an intermediary Agent

# Copy of Bank to Customer Statements

Use Case c.53.2 - Bank to Customer Statement sent as an additionally  copy to an authorised party

# Resent Bank to Customer Statements

Use Case c.53.3 - Bank to Customer Statement resent a previously  sent statement/s to the Account Owner

Use Case c.53.4 - Bank to Customer Statement resent a previously  sent copy statement/s to an authorised party

# Forwarding of Bank to Customer Statements

Use Case c.53.5 - Bank to Customer Statement sent to an authorised party who forward/provides  on to the Account Owner (commonly referred to as an account concentrating model)

Use Case camt.060 for requesting a Bank to Customer statement

Use Case for copy or duplicate reports refer to camt.053 use cases

---

<!-- ELEMENT 622 -->
1

2

- Agent B processes the payment 3

on Agent C

4

5

6

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent C processes the payment on Agent D

Creditor Agent credits the account of the Creditor

Creditor Agent as the Account Servicer  produces and sends a statement to either the Account Owner, or an authorised third party.

---

<!-- ELEMENT 623 -->
1

2

- 3

- Creditor Agent credits the account of the Creditor 5

6

Debtor Agent as the Account Servicer  produces and sends a statement to either the Account Owner, or an authorised third party.

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

- Agent B processes the payment

on Agent C

- Agent C processes the payment 4

on Agent D

---

<!-- ELEMENT 626 -->
# Account Owner

---

<!-- ELEMENT 627 -->
# authorised party

---

<!-- ELEMENT 628 -->
# the Account Owner (commonly referred to as an account concentrating model)

1

2

3

4

5

6

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (C) using Agents as an intermediary

Agent B processes the payment on Agent C

Creditor Agent credits the account of the Creditor

Creditor Agent as the Account Servicer  produces and sends a statement to an authorised third part.

Authorised third part provides  statement information  to the Account Owner. Which could be the forwarded Camt.053 statement or the details via an alternative  channel (e.g. host to host file, GUI etc.)

---

<!-- ELEMENT 629 -->
# Bank to Customer Debit Credit Notification

---

<!-- ELEMENT 631 -->
Role of the Agent/s, Debtor and Creditor in the payment changes by description in the Bank to Customer Debit Credit Notification message to Account Servicer and Account Owner. Whereby the notification is sent by the Account Servicer to the Account Ownerandor authorisednartv

---

<!-- ELEMENT 632 -->
The Customer Debit Credit Notification are optionally provided between the account servicing institution and the account owner, or authorised (third) party.

These messages:

- are used to inform on debit and/or credit entries reported to an account.

- and may also be complemented by:

- a Status Information message:

- pacs.002 in Payment Clearing and Settlement, or pain.002 in Payment Initiation.

- or by a bank statement such as the camt.053 Bank to

---

<!-- ELEMENT 634 -->
Each ISO 20022 cash management reporting message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the Message Identification has no exact equivalent in the legacy MT Customer Statement message. However the Transaction Reference Number (Field 20) could be considered a similar comparison.

---

<!-- ELEMENT 635 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 636 -->
# Min 0 - Max 1

The Bank to Customer Debit Credit Notification Message Recipient nested element provides details of the party authorised by the Account Owner to receive the Debit Credit Notification. This element should only be used to identify the Message Recipient when different from the account owner, which is implied by the usage of COPY in the Copy Duplicate Indicator within the nested Notification element.

Where MessageRecipient is used the nested:

- Name Min 0 - Max 1

- PostalAddress Min 0 - Max 1

- Identification

- Min 0 - Max 1

- ContactDetails Min 0 - Max 1

May be used to capture information related to this party.

Group Header

Recipient

Message

---

<!-- ELEMENT 637 -->
The Bank to Customer Debit Credit Notification Original Business  Query element identifies a query to generate a report, for example a camt.060 Account Reporting Request. Min 0 - Max 1

(i.e. the Min 1 - Max 1

Where Original Business Query is used the original Message identification message identification of the camt.060 message) is required.

Original Message Name identification and Original Creation Date Time may also be provided. Min 0 - Max 1 Min 0 - Max 1

---

<!-- ELEMENT 638 -->
# Min 0 - Max 1

The Bank to Customer Debit Credit Notification Additional Information element represents further details related to the account statement.

The camt.054 may be used to indicate a particular type of notification, recognizing all transactions within the notification belong to the type indicated below:

/LBOX/ Lock Box

/BULK/ Bulk reporting (batch transaction with underlying transaction)

/RTRN/ Return report

/CRED/ Notification with Credit entries ONLY

Additional Information is a textual element restricted in CBPR+ to 500 characters.

---

<!-- ELEMENT 640 -->
# Min 0 - Max *

The Bank to Customer Debit Credit Notification Notification nested element captures debit and credit entry information  for an account.

The Notification element has a couple of options to notify on multiple Debits and or Credits. This can be achieved at either the Notification element itself which could principally report on more than one account held by the account owner with the Account Servicer or can be achieved at an Entry level. Notification of multiple Debits and or Credits is perhaps more associated with a Credit notification on a single

timed or batch creation of the camt.054 Bank to Customer Debit Notification. Whereas the more common example of a real-time produced at the point of an account posting would typically notify Entry .

---

<!-- ELEMENT 641 -->
Min 1 - Max 1

The Bank to Customer Debit Credit Notification message Identification provides a mandatory element to identify the notification

Unique reference assigned by the account servicer to unambiguously identify the account statement. Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT statement message.

---

<!-- ELEMENT 642 -->
Min 0 - Max 1

The Bank to Customer Debit Credit Notification message Notification Pagination element provides the page number of the notification.

Min 1 - Max 1

Min 1 - Max 1

Where Notification Pagination is used the Page Number and Last Page indicator elements are both mandatory.

For example, a Page Number of 2 represents the current account statement, being the second page of the and implying a previous account statement page had been sent. The Last Page indicator further implies whether more pages are expected

Either Message Pagination (Group Header) or Notification Pagination (Notification) may used but not both

---

<!-- ELEMENT 643 -->
The Bank to Customer Debit Credit Notification message Electronic Sequence Number allows the Account Servicer to assign a number  to each notification which should increment by 1 for each electronic notification report sent.

As a good practice this element allows easy recognition of the notification order, if not recognisable by other data within the notification, such as the Notification > Identification element.

Should this sequence number be reset by the Account Servicer , this should not occur more frequently than once a year. Likewise, this 18 digit counter could be incremented to its maximum value before it's reset.

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the Account Servicer andthe Account Owner

---

<!-- ELEMENT 644 -->
Min 0 - Max 1

The Bank to Customer Debit Credit Notification message Reporting Sequence specifies the choice of identification sequences. This can be used as an alterative to the Statement Pagination or Electronic Sequence Number as a way to identify the statement order, which is not confined to numeric values.

Where used the Reporting Sequence mandate a choice of nested element:

- From Sequence identifies the start of a sequence range. Min 1 - Max 1

- To Sequence identifies the end of a sequence range. Min 1 - Max 1

- From To Sequence identifies the start and end of a sequence range. Min 1 - Max *

- Equal Sequence identifies a sequence. Min 1 - Max *

- Not Equal Sequence identifies a sequence to be excluded. Min 1 - Max *

Although the Reporting Sequence may be provided in a camt.060 Account Reporting Request, the use of this message to request a Bank to Customer Debit Credit Notification is less compelling, whereby such notifications are typically triggered as the result of an account posting, rather than being requested.

---

<!-- ELEMENT 645 -->
The Bank to Customer Debit Credit Notification message Legal Sequence Number allows the Account Servicer to assign a number  to each notification which should increment by 1 for each notification report sent.

In the case of a real-time notification the Legal Sequence Number element has little value, unlike its use in a statement message.

---

<!-- ELEMENT 646 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 647 -->
The Bank to Customer Debit Credit Notification message From to Date allows the Account Servicer specify the start date time and end date time applicable to the notification.

Where From to Date is used the From Date Time and To Date Time Min 1 - Max 1 Min 1 - Max 1

to become mandatory elements.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 648 -->
The Bank to Customer Debit Credit Notification message Copy Duplicate Indicator is used as a choice to identify additional notification from the original sent to the Account Owner.

COPY is used when a copy of the notification is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service such as liquidity sweeping or statement consolidation.

DUPL is used when a duplicate of the notification is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request.

CODU is used when a duplicate of a notification copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in place with the Account Servicer.

---

<!-- ELEMENT 649 -->
Min 0 - Max 1

The Bank to Customer Debit Credit Notification message Reporting Source allows the Account Servicer to define the source of the notification, typically associated with an application.

Reporting Source utilizes the external Reporting Source code list. For example, ACCT represents a notification based on accounting data, whereas DEPT represents a cash or deposit system.

Where the source of the notification is functionally required by the consumer of the notification i.e., the Account Owner or authorised Third Party , the codes used should be bilaterally agreed.

---

<!-- ELEMENT 650 -->
# Min 1 - Max 1

The Bank to Customer Debit Credit Notification message Account provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath Account .

---

<!-- ELEMENT 651 -->
Min 1 - Max 1

The Bank to Customer Debit Credit Notification message mandatory Account also provides a number of optional nested element to identify the account for which debit and credit entries have been made.

Min 0 - Max 1

---

<!-- ELEMENT 652 -->
Min 0 - Max 1

The Bank to Customer Debit Credit Notification message Related Account allows the identification of a related parent account for the account  notification. For example sweeping, pooling or virtual account for which the notification  is produced can identify the parent account they hierarchically  relate to.

Min 1 - Max 1

Min 1 - Max 1

When Related Account is utilized, like Account , the Identification and Currency element become mandatory.

Additionally, the nested Type element, Name and nested Proxy element are optionally available. Min 0 - Max 1 Min 0 - Max 1 Min 0 - Max 1

Related Account uses a variety of common elements described in more detail within the Account section.

---

<!-- ELEMENT 653 -->
Min 0 - Max *

The Bank to Customer Debit Credit Notification message Interest provides interest information  that applies to the account. Inclusion  of such interest information  is perhaps more common to the camt.053 Statement than a

Debit Credit Notification.

Interest

An element which may either use an embedded ISO Interest Type code; INDY (Intraday) OVRN (Over Night) or a proprietary code. It is used to identifier a particular interest type.

Rate

The type of interest Rate defined as a Percentage and in an Other form. Validity Range optionally defines an Amount , Credit Debit Indicator and Currency .

From To Date

Reason

The date range for which interest has been calculated. From Date Time and To Date Time must be representing when usingthis element.

Theoptional Reason for which interest is applied.

Provides details on any tax applied to the Interest. Where optional

---

<!-- ELEMENT 654 -->
Min 0 - Max 1

The Bank to Customer Debit Credit Notification message optional Transaction Summary provides a set of nested element to summarize  entry information. More commonly the Bank to Customer Debit Credit Notification is reporting a single Debit or Credit transaction, where understandably  the use of Transaction Summary provides little value.

Each of the following element allow an optional total of entries either as a Number of Entries and or as a Sum .

- Total Entries

- Total Credit Entries

- Total Debit Entries

- Total Entries Per Bank Transaction Code

In addition to the Number of Entries and Sum , the Total Entries Per Bank Transaction Code requires the Bank Transaction Code element and optionally allows a variety of other optional elements. Min 1 - Max 1

The Total Entries Per Bank Transaction Code element is unlimited (Max  *) whereby more that one Bank Transaction Code may be summarised.

---

<!-- ELEMENT 655 -->
Unlike the legacy MT 900 MT 910 confirmation messages, the camt.054 has a number of dedicated elements to capture a variety of entry level data. It also has an number of enhancements on the legacy MT confirmation message where parties in the payment and customer remittance information, as examples, can provided to the Account Owner.

Min 0 - Max *

The Bank to Customer Debit Credit Notification message optional Entry provides a significant variety of nested elements to represent the details associated with each Debit or Credit Entry .

Min 0 - Max 1

Entry Reference

Min 0 - Max 1

Booking Date

Min 0 - Max 1

Commission Waiver Indicator

Min 0 - Max 1

Min 1 - Max 1

Amount

Min 0 - Max 1

Value Date

Min 0 - Max 1

Additional Information Indicator

Min 0 - Max 1

Min 1 - Max 1

Credit Debit Indicator

Min 0 - Max 1

Account Servicer Reference

Min 0 - Max 1

Amount Details

Min 0 - Max *

Min 0 - Max 1

Reversal Indicator

Min 0 - Max 1

Charges

Min 0 - Max 1

Min 1 - Max 1

Bank Transaction Code

Min 0 - Max 1

Technical Input Channel

---

<!-- ELEMENT 658 -->
The Bank Transaction Code is designed to deliver a harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the account servicer to correctly report a transaction, which in its turn will help account owners to perform their cash management and reconciliation operations.

The structure of the Bank Transaction Code has three levels:

Domain :  Highest definition level to identify the subledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.) Family :  Medium definition level e.g. type of payment; credit transfer, direct debit etc. Sub-family :  Lowest definition level e.g. type of cheques; draft etc.

Bank Transaction Codes are an external code set defined in the Bank Transaction Code combinations external code sets.

---

<!-- ELEMENT 659 -->
# descriptions

---

<!-- ELEMENT 660 -->
# combinations

Bank Transaction Codes are an external code set defined in the Bank Transaction Code combinations external code sets.

As an example a debit notification which relates to a cross-border payment initiated from an account would be represented by:

---

<!-- ELEMENT 661 -->
Optional element indicating, as a Boolean, whether the entry is exempt from commission. This element is not typically associated with Correspondent Banking payments

Optional element indicating whether the underlying transaction details are provided through a separate message. Where the Message Name Identification represents the message used to provide the additional information and Message Identification specifies the reference of the message that provides the additional information.

Optional nested element which provides various elements to represent an aggregated (consolidated) original amount. Where individual transaction amounts can be represented, if required, within the Entry Detail set of elements.

This element is useful to capture original amount details where they are different to the Entry , Amount ,  for  example the Instructed Amount of the payment can be included, together with a potential Currency Exchange rate, where necessary.

Optional nested element to provide information on charges either pre-advised or taken from the entry.

---

<!-- ELEMENT 662 -->
Optional element which may either use an external ISO Technical Input Channel code or a proprietary code used to represent the technical channel used to input the entry.

Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry amount.

Optional nested element which provides details associated with a card transaction such as the card number, card brand etc.

Additional optional nested element containing details on the entry. See dedicated section on Entry Details .

Additional optional element to represent further information related to the account

---

<!-- ELEMENT 663 -->
Min 0 - Max *

The Bank to Customer Debit Credit Notification message optional Entry Details provides a variety of nested elements to represent the details associated with each Entry .

Batch provides details on batched transactions such as the total the batched entry (sometimes referred to as a consolidated entry) represents.

Transaction Details underlying  transaction.

Number of Transactions is a significant nested element which represents information on the

---

<!-- ELEMENT 664 -->
When the Bank to Customer Debit Credit Notification message optional Entry Details is utilized  the nested Transaction Details element is mandatory.

Transaction Details has a variety of nested elements closely associated with Entry level elements. The References element however is nested to include  a variety of references related to the entry including  for example the UETR

Credit Debit Indicator Min 1 - Max 1

Min 0 - Max 1

Bank

Transaction

Code

Additionally Transaction Details also has a variety of elements capturing details from the underlying transaction, which amongst other business  transactions includes  payment transaction data. For example Remittance Information and Related Parties

---

<!-- ELEMENT 665 -->
# Agents

Min 0 - Max 1

Min 0 - Max 1

The Bank to Customer Debit Credit Notification message Related Parties and Relegated Agents represents a set of optional nested elements related to the underlying  transaction. Where the Entry Details (the set of elements Related Parties/Agents belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management  (camt) message.

These Related Parties include  : These Related Agents include  :

- Instructing Party

- Debtor

- Debtor Account

- Ultimate Debtor

- Creditor

- Creditor Account

- Ultimate Creditor

- Instructing Agent

- Instructed Agent

- Debtor Agent

- Creditor Agent

- Intermediary Agent 1

- Intermediary Agent 2

- Intermediary Agent 3

Trading Party is also present in the Related Parties elements, and the following are present in the Related Agents elements: Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place . Although  these elements are not directly associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security

---

<!-- ELEMENT 666 -->
The Bank to Customer Debit Credit Notification message Entry Details have a number of additional elements beyond Related Parties and Related Agents to capture information  from the underlying  payment.

# These are:

- Local Instrument

- Purpose

- Related Remittance Information

- Remittance Information

- Related Dates such as the Interbank Settlement Date

- Tax

For Payment Return (pacs.004) it is also possible to capture Return Information which includes:

- The Original Bank Transaction Code of the original Entry

- The Originator of the return from the pacs.004

- And the Reason code.

Remittance Information as an end-to-end  element should be passed unaltered  from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account

---

<!-- ELEMENT 667 -->
It should also be mentioned  that the Bank to Customer Credit Debit Notification message Entry Details have a number of additional elements which capture information  from transactions in other business  domains beyond payments, as well as have an element to capture Additional Transaction Information .

# These are:

- Related Quantity

- Financial Instrument Identification

- Corporate Action

- Safekeeping Account

- Cash Deposit

- Card Transactions

---

<!-- ELEMENT 668 -->
# Use case should be considered as a principal example whereby use case may be cross referenced

# Debit/Credit Notification related to a Serial Customer Payments

Use Case c.54.1.1 - Customer Debit/Credit Notification  (camt.054) of a Customer Credit Transfer (pacs.008)

Debit/Credit Notification related to a Serial Financial  Institution Payments

Use Case c.54.2.1 - Customer Debit/Credit Notification  (camt.054) of a FI to FI Credit Transfer (pacs.009)

Debit/Credit Notification related to a Cover Method Payments

Use Case c.54.3.1 - Customer Debit/Credit Notification  (camt.054) of a payment using the cover method

---

<!-- ELEMENT 669 -->
# (pacs.008)

1

2

2b

3

4

5

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Agent A provides  a debit notification to the debtor using the camt.054 to confirm their account has been debited for the payment initiation request. This notification may compliment additional  status information  or statement report messages

Agent B processes the payment on Agent C

Agent C processes the payment on Agent D

Agent D credits the account of the Creditor, providing  a credit notification using the camt.054

---

<!-- ELEMENT 670 -->
# (pacs.009)

1

2

2b

Debtor Agent (Agent B) provides  a debit notification to the debtor using the camt.054 to confirm their account has been debited for the payment initiation request. This notification may be complimented by an additional status information message. But typically will be compliment by an end of business day statement report messages

3

Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent D) using Agents C as an intermediary.

Creditor Agent (C) credits the account of Agent D and provides  a credit notification (camt.054) in addition to an account statement (camt.053)

---

<!-- ELEMENT 671 -->
method

1

1

2a

2b

In parallel the Debtor Agent (A) initiates a coving  payment to credit the account of Agent (D) with their correspondent  (Agent C)

3a

Agent B processes the payment

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a payment using the cover  method to the Creditor  Agent (D)

A

3b pacs.008

pacs.002

pacs.009.cov

4

C

4

Agent B provides  a debit notification to Agent A using the camt.054 to confirm their account has been debited for the payment initiation request. This notification may be complimented by an additional  status information  message or statement report messages

Agent C receives  the payment and credits the account of Agent D and provides  a credit notification (camt.054)

Upon receipt of the credit notification

(camt.054) confirming  settlement of the covering  payment, Agent D may chose

to process the pacs.008 (if not already

2b

2a

3b

B

3a

5

6

D

5

6

camt.054

Agent C produces an end of day account statement report. An optional real time notifications e.g. advice of credit may have  also been created at the time of the credit posting

Intraday Credit Notification is required when using the cover

---

<!-- ELEMENT 672 -->
# Notification to Receive

---

<!-- ELEMENT 675 -->
# payment message (pacs.008/pacs.009) and the Notification to Receive (camt.057)

A

B

C

D

D

The Parties defined within the Notification to Receive (camt.0057) provide advance information to the Account Servicer of information included in the payment message. Noting a Debtor must always be present in the camt.057 (it is mandatory in the pacs payment message) but Debtor Agent may not be provided (Debtor Agent is

Party pacs

Debtor

Debtor Agent

Creditor Agent pacs

pacs.002

camt.057

Debtor

Debtor Agent

Account Servicer pacs

pacs.002

pacs pacs.002

camt.057

camt.053

---

<!-- ELEMENT 677 -->
Each ISO 20022 cash management reporting message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

Min 1 - Max 1

The Message Identification in the Cash Management (camt) messages is equivalent to field 20 Transaction Reference Number of the MT 210 in the legacy MT Notice to Receive.

---

<!-- ELEMENT 678 -->
The camt.057 message Creation Date Time captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 679 -->
Min 0 - Max 1

The Notification to Receive Message Sender nested element provides details of the party that is sending the message, where the Message Sender is different from the account owner.

Where MessageSender,Party is used the nested:

- Name

Min 0 - Max 1

- PostalAddress Min 0 - Max 1

- Identification

- Min 0 - Max 1

- ContactDetails Min 0 - Max 1

May be used to capture information related to this party.

Where MessageSender,Agent is used the nested Financial Institution :

- BICFI

- ClearingSystemMemberIdentification

- LEI

Min 1 - Max 1

Min 0 - Max 1

Min 0 - Max 1

May be used to capture information related to this Agent.

Group Header

Sender

Message

Name

---

<!-- ELEMENT 681 -->
# Min 1 - Max 1

The Notification to Receive Notification element contains nested elements to provide further details on the account notification such as the related parties, the expected amount  to be received and value date of the expected receipt.

The Notification nested element Item can contain multiple Credits. Where there is only one expected credit then only the Item element will contain the Item Identification andthe Amount .

Today the status of a camt.057 has no documented ISO 20022 reporting process, to the Account Owner by the Account Servicer.

Generally, if the Account Servicer does not require notification the message will be ignored.

---

<!-- ELEMENT 682 -->
The Notification to Receive message Notification Identification provides a mandatory element to identify the account notification.

Unique reference assigned by the account owner to unambiguously identify the account notification. There is no equivalent in the MT210. It is recommended that the Message Identification is repeated for the Notice to ReceiveIdentification.

---

<!-- ELEMENT 683 -->
Account

# Min 0 - Max 1

The Notification to Receive message Account element provides nested elements to identify the account for which the credit entry has been made. The following two mandatory elements are nested beneath Account .

# Min 1 - Max 1

a unique Identification for the account, between the Account Servicer and Account Owner. The element is further nested by choice of IBAN or Other to capture the account.

An element which may either use an external ISO Cash Account Type code or a proprietary code. It is used to identifier a particular type of account.

The Currency for which the account is held. This is identified using the three characters ISO currency code.

The Name of the Account, as Assigned by the servicing institution.

Anested element which contains a Proxy Identifier together with the Proxy

---

<!-- ELEMENT 684 -->
Min 0 - Max 1

Min 0 - Max 1

The Account Owner is the Creditor, and the Account Servicer is the Creditor Agent. They are static roles in the camt.057 Notification  to Receive.

The Account Owner must be identified either by the Party name and postal address or as an Agent using a Financial Institution identification. The Account Servicer must be identified as an Agent by using the Financial Institution identification.

The Account Owner and the Account Servicer are the Creditor and Creditor

Agent respectively in a pacs.008 FI to FI Customer. Whereutilised, it is recommended to use the element at the Item level.

---

<!-- ELEMENT 685 -->
The Notification to Receive message Related Account element allows the identification of a related parent account for the account notification. For example sweeping, pooling or virtual account for which the notification is produced can identify the parent account they hierarchically relate to.

In the context of a Notification to Receive this element provides little business value.

Min 1 - Max 1

When Related Account is utilized, like Account , the Identification and Currency element become mandatory.

Additionally, the nested Type element, Name and nested Proxy element are optionally available. Min 0 - Max 1 Min 0 - Max 1 Min 0 - Max 1

Related Account uses a variety of common elements described in more detail within the Account section.

---

<!-- ELEMENT 686 -->
Min 0 - Max 1

The Notification to Receive message Total Amount provides the sum of all the amounts of all the Item entries. Where utilised the Item element is a mandatory element which contains information about the expected receipt. The Notification to Receive can contain multiple items. Expected Value Date is the date on which the final receiving agent expects to receive the total amount. Min 0 - Max 1

The Total Amount provides a control total where there are multiple credits recorded within the Item element. The Total Amount element should not be used where there is a single expected credit.

The Expected Value Date takes the format YYYY-MM-DD

---

<!-- ELEMENT 687 -->
The Notification to Receive message describes the Party or Agent that owes the amount of money as the Debtor . The following describes the Debtor nested Party elements in greater detail.

Mandatory Name (where a BIC identifier is not provided) by which the party is known

Nested element capturing either structured or unstructured Debtor address details

Name

Postal

Address

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Identification

Optional element to capture the Debtor's ISO

Debtor

Country of

Residence

---

<!-- ELEMENT 688 -->
The Notification to Receive message describes the Party or Agent that owes the amount of money as the Debtor . The following describes the Debtor nested Agent elements in greater detail.

Information used to identify a

Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Debtor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Debtor structured or unstructured

BICFI

Debtor

Postal

Address

---

<!-- ELEMENT 689 -->
Min 0 - Max 1

The Debtor Agent element in the camt.057 Notification to Receive captures the Debtor Agent of the payment i.e., the Financial Institution servicing an account for the Debtor.

The Debtor Agent and Intermediary Agent elements allow the Treasury function at the Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time.

Min 0 - Max 1

The Intermediary Agent element in the camt.057 Notification to Receive capture the Intermediary agent between the Debtor Agent and the Account Servicer i.e. the Agent from whom the Creditor Agent expects to receive the payment from.

The Debtor Agent and Intermediary Agent elements allow the Treasury function at the Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time.

The Debtor Agent and Intermediary Agent elements allow the Account Servicing Institution's Treasury department to proactively follow up, as necessary, the actual payment if it fails to arrive by an expected time.

---

<!-- ELEMENT 690 -->
# Min 1 - Max *

The Notification to Receive message mandatory Item element provides details of the expected amount on the account serviced by the account servicer. There is no equivalent field in the legacy MT210 Notice to Receive.

The various nested elements within the Item element are very useful in the case where there are multiple credits. The Creditor Agent will be able to reconcile the incoming receipts against the list of expected receipts detailed in the Item element and will be check completeness of all expected receipts and identify any missing receipts.

Notification

Identification

---

<!-- ELEMENT 691 -->
Min 1 - Max *

The Notification to Receive message mandatory Item element provides details of the expected amount on the account serviced by the account servicer. There is no equivalent  field in the legacy MT210 Notice to Receive.

---

<!-- ELEMENT 692 -->
# Use case should be considered as a principal example whereby use case may be cross referenced

# Notification to Receive multiple receipts

Use Case c.57.1.1 - Notification  to Receive (camt.057) followed by Customer Credit Transfers (pacs.008)

Use Case c.57.1.2 - Notification  to Receive (camt.057) followed by FI Credit Transfers (pacs.009)

Use Case c.57.1.3 - Notification  to Receive (camt.057) where the receipt is settled by the cover method.

Use Case c.57.1.4 - Notification  to Receive (camt.057) for a FI Credit Transfers cover (pacs.009 cov).

---

<!-- ELEMENT 693 -->
# (pacs.008)

1

2

3

4

5

Creditor is expecting to receive  a payment from the Debtor. As the Account Owner sends a Notification to Receive  to Agent C as Account Servicer.

Debtor initiates a payment instruction to the Debtor Agent (A).

Debtor Agent (A) initiates a serial payment towards the Creditor Agent (C) using Agents B as an intermediary.

Agent (B) processes the payment on to the Creditor Agent (C).

Creditor Agent (C) as Account Servicer  sends and end of day statement to Creditor as Account Owner confirming accounting entries.

---

<!-- ELEMENT 694 -->
1

2

3

4

Creditor is expecting to receive  a payment from Debtor. As the Account Owner sends a Notification to Receive  to Agent C as Account Servicer.

Debtor (A) initiates a serial payment towards the Creditor Agent (C) using Agents (B) as an intermediary.

Agent (B) processes the payment on to the Creditor  Agent (C).

Creditor Agent (C) as Account Servicer  sends and end of day statement to Creditor as Account Owner confirming accounting entries.

---

<!-- ELEMENT 695 -->
method.

1

1

2a

2b

A

2a

2b

Debtor initiates a payment instruction to the Debtor Agent

B

Debtor Agent (A) initiates a payment using the cover  method to the Creditor Agent (D)

In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) who become the Creditor of the cover  payment (pacs.009 cov). Agent A's role also changes in the cover  payment where  it becomes the Debtor, whereby  Agent A's

4

pacs.008

pacs.009 cov

C

3

Upon receipt of the pacs.008 advising  settlement will occur via a cover  payment. Agent D sends a Notification to Receive  to Agent C.

Agent B processes the payment

4

5

D

3

5

Agent C receives  the payment and credits the account of Agent D as the Creditor, producing an end of day account statement report. An optional real time notifications e.g. advice  of credit may have  also been created at the time of the credit posting.

---

<!-- ELEMENT 696 -->
1

2a

2b

3a cov).

1

A

Debtor initiates a payment instruction to the Debtor Agent

Debtor Agent (A) initiates a payment using the cover  method towards the

Creditor Agent (D)

In parallel the Debtor Agent (A)

initiates a covering  payment to credit the account of Agent (D) who become

the Creditor of the cover  payment

(pacs.009 cov).

Agent B processes the cover  payment

2a

2b

B

pacs.009 cov

E

3b

3a pacs.008

pacs.009 cov

6

C

pacs.009 cov

F

5

4

5

6

D

3b

Agent B also sends a notification to receive  on behalf  of Agent D to notify

Agent C a credit is expect on their account.

Agent E processes the cover  payment on to Agent

F.

Agent F processes the cover  payment on to Agent

C.

Agent C receives  the cover payment (as the

Creditor Agent) recognising they have  also be

Notified they would receive  this payment (by

---

<!-- ELEMENT 697 -->
# Notification to Receive Cancelation Advice

---

<!-- ELEMENT 699 -->
Role of the Creditor Agent and Creditor in the payment changes description in the Notification to Receive message (camt.057). The Account Owner is typically the Creditor and the Account Servicer is typically the Creditor Agent. The Notification to Receive Cancellation Advice (camt.058) is used to request the cancellation of a previous Notification to Receive.

---

<!-- ELEMENT 701 -->
Each ISO 20022 cash management reporting message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

Min 1 - Max 1

The Message Identification in the Cash Management (camt) messages is equivalent to field 20 Transaction Reference Number of the MT 292 in the legacy MT Request for Cancellation.

---

<!-- ELEMENT 702 -->
The camt.058 message Creation Date Time captures the date and time which the message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 703 -->
Min 0 - Max 1

The Notification to Receive Cancellation Advice Message Sender nested element provides details of the Party or Agent that is sending the message, where the Message Sender is different from the account owner.

This element has no equivalent in the legacy MT 292 Request for Cancellation.

Where MessageSender,Agent is used the nested Financial Institution :

Group Header

Sender

Message

Name

---

<!-- ELEMENT 705 -->
Item

# Min 1 - Max 1

The Notification to Receive Cancellation  Advice Original Notification element contains nested elements to provide further details on the original camt.057 notification to receive. such as the related parties, the expected amount to be received and value  date of the expected receipt.

The Original Notification nested element enables the ability to reconcile this cancellation advice against the Notification originally received, so that appropriate action can be take to remove the advisedcurrency and amount from predicted currency positions at the Account Servicer.

# Group Header

- Message Identification

- Creation Date Time Notification

- Identification

- Debtor

- Identification

- End to End Identification

# Original Notification

- Original Message Identification

- Original Creation Date Time

- Original Notification Identification

- Original Notification Reference

- Debtor

- Original Item

- Original Item Identification

- Original End to End Identification

---

<!-- ELEMENT 706 -->
Min 1 - Max 1

The Notification to Receive Cancellation  Advice message Original Message Identification provides a mandatory element to identify the Message Identification from the original camt.057.

This 35 character identifier is a point-to-point reference used to unambiguously identify the Notification to Receive message, capture in its group header.

---

<!-- ELEMENT 707 -->
The camt.058 message Original Creation Date Time captures the date and time which the original Notification to Receive message was created.

CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 708 -->
The Notification to Receive Cancellation  Advice message Original Notification Identification provides a mandatory element to identify the account notification.

Unique reference assigned by the account owner to unambiguously identify the original account notification.

Original Notification

---

<!-- ELEMENT 709 -->
The Notification to Receive message describes the Party or Agent that owes the amount of money as the Debtor . The following describes the Debtor nested Party elements in greater detail.

Mandatory Name (where a BIC identifier is not provided) by which the party is known

Nested element capturing either structured or unstructured Debtor address details

Name

Postal

Address

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Identification

Optional element to capture the Debtor's ISO

Debtor

Country of

Residence

---

<!-- ELEMENT 710 -->
The Notification to Receive message describes the Party or Agent that owes the amount of money as the Debtor . The following describes the Debtor nested Agent elements in greater detail.

Information used to identify a

Debtor by a clearing system identifier.

Legal entity identifier of the financial institution.

Name by which the Agent is

known

LEI

The BIC which

Debtor identifies the

Clearing

System

Member Id

Name

Nested element capturing either

Debtor structured or unstructured

BICFI

Debtor

Postal

Address

---

<!-- ELEMENT 711 -->
Min 0 - Max 1

The Debtor Agent element in the camt.058 Notification to Receive Cancellation Advice captures the Debtor Agent provided in the original Notification to Receive (camt.057) i.e., the Financial Institution servicing an account for the Debtor.

Debtor Agent may be provided within the Original Notification

Original Notification

---

<!-- ELEMENT 712 -->
Min 1 - Max 1

The Notification to Receive Cancellation  Advice Original Item Reference nested element captures  the references of the Original Item in the original Notification  to Receive message.

Min 1 - Max *

The Original Item nested element is repetitive as the original Notification to Receive message has the ability to notify on more than one item i.e. currency and amount expect. The following elements are nested within Original Item ,  of which Identification and Amount are required.

Original Notification

---

<!-- ELEMENT 714 -->
Min 1 - Max 1

The Notification to Receive Cancellation Advice Cancellation Reason nested element captures information associated with the reason for the Cancellation request.

Min 0 - Max 1

the Originator element helps identify the party who issued the Cancellation request. Typically, this element would be used to identify the Account Owner as the Originator of the request, where the Notification to Receive Cancelation Advice message captured a Message Sender acting on the account owner's behalf.

Min 1 - Max 1

the Reason is mandatory and represented by an embedded CBPR+ Cancellation Code choice ( )

Min 0 - Max 2

The Additional Information element may also be included to provide further details on the Cancellation reason.

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

# Cancellation Reason

Originator

---

<!-- ELEMENT 715 -->
# Use case should be considered as a principal example whereby use case may be cross referenced

# Notification to Receive multiple receipts

Use Case c.58.1.1 - Cancellation Advice for a Notification  to Receive (camt.057) expecting a Customer Credit Transfers (pacs.008)

Use Case c.58.1.2 - Cancellation Advice for a Notification  to Receive (camt.057) expecting a FI Credit Transfers (pacs.009)

Use Case c.58.1.3 - Cancellation Advice for a Notification  to Receive (camt.057) where the receipt is settled by the cover method.

---

<!-- ELEMENT 716 -->
# Customer Credit Transfers (pacs.008)

1

Creditor is expecting to receive  a payment from the Debtor. As the Account Owner they send a Notification to Receive  to Agent C as Account Servicer.

2

Creditor subsequently understand the payment should no longer be expected for the given  amount. They issue a cancellation advice  to Agent C as Account Servicer,  providing  the reason NOLE (not longer expected).

5

---

<!-- ELEMENT 717 -->
# Transfers (pacs.009)

Creditor is expecting to receive  a payment from Debtor. As the Account Owner sends a Notification to Receive  to Agent C as Account Servicer.

1

2

Creditor subsequently understand the payment should no longer be expected for the given  amount. They issue a cancellation advice  to Agent C as Account Servicer,  providing  the reason NOLE (not longer expected).

4

---

<!-- ELEMENT 718 -->
is settled by the cover method.

Debtor Agent (A) initiates a payment using the cover  method to the Creditor Agent (D)

In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) who become the Creditor of the cover  payment (pacs.009 cov). Agent A's role also changes in the cover  payment where  it becomes the Debtor, whereby  Agent A's

2

3

1a

1b

Upon receipt of the pacs.008 advising  settlement will occur via a cover  payment. Agent D sends a Notification to Receive  to Agent C.

Agent B rejects the payment

5

Agent A send a Request for Cancellation to Agent D including the reason COVR to confirm the cover  payment was cancelled.

Agent D subsequently issue a cancellation advice  to Agent C as Account Servicer,  providing  the reason NOLE (not longer

---

<!-- ELEMENT 719 -->
# Account Reporting Request

---

<!-- ELEMENT 721 -->
Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Report Request message to Account Servicer and Account Owner. Whereby the report request is sent by the  Account Owner or authorised an account andlorto nrovide

---

<!-- ELEMENT 723 -->
Each ISO 20022 cash management reporting message has a Message Identification element, located in the Group Header. This 35 character identifier is a point to point reference used to unambiguously identify the message.

For Cash Management (camt) messages the Message Identification has no exact equivalent in the legacy MT Customer Statement message. However the Transaction Reference Number (Field 20) could be considered a similar comparison.

---

<!-- ELEMENT 724 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 725 -->
Min 0 - Max 1

The Account Report Request Message Sender nested element provides details of the party that is sending the request.

This element should only be used to identify the Message Sender when different from the account owner.

Where Message Sender is used, a choice of nested Party or Agent may be used to identify the Sender.

# Party :

- Name

- Postal Address

- Identification

- Countryof Residency

# Agent :

Take me to the Agent identification

---

<!-- ELEMENT 727 -->
The Account Reporting Request Reporting Request nested element capture the detail related the request.

Many Account Servicing Institutions service their Account Owner customers through statics account configuration/s. Whereby a variety of reports can be generated on either a time or event bases routine.

The Reporting Request may be used as either an alterative to a static configuration or to request ad hoc reports (whether that be an additional report to the statics configuration or to resend reports previous reported).

---

<!-- ELEMENT 728 -->
The Account Reporting Request message Identification provides a mandatory element to identify the Request

Unique reference assigned by the account owner (or Message Sender on behalf of the account owner) to unambiguously identify the account statement. Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT request message.

---

<!-- ELEMENT 729 -->
# Min 1 - Max 1

The Account Reporting Request message Requested Message Name Identification provides a mandatory element to identify the name of the report being request.

This element specifies which type of report is begin requested. The report is representedby its full name. For example:

camt.052.001.08 or camt.053.001.08 or camt.054.001.08

---

<!-- ELEMENT 730 -->
# Min 0 - Max 1

The Account Reporting Request message Account provides nested elements to identify the account for which the request relates to. A number of elements are nested beneath Account , of which the Identification element is mandatory.

# Min 1 - Max 1

a unique Identification for the account, between the Account Servicer and Account Owner. The element is further nested by choice of IBAN or Other to capture the account.

---

<!-- ELEMENT 732 -->
Min  - Max 1

The Account Reporting Request message Account Owner identifiers the mandatory owner of the account that the Account Report Request relates to.

Where Account Owner is used, a choice of nested Party or Agent may be used to identify the owner.

# Agent :

Typically  the Account Name (see the previous page) represents the Account Owner's Name in accordance with standard Know Your Customer (KYC). The mandatory Account Owner elements enables more detail to

---

<!-- ELEMENT 733 -->
# Min 0 - Max 1

The Account Reporting Request message Account Servicer provides an optional element to capture the Agent who is acting as an Account Servicing  Institution. Typically, this would be the same Agent the Account Reporting Request is sent to, who is also identified in the Business Application  Header.

# Financial InstitutionIdentification :

- BICFI

- Clearing SystemMemberIdentification

- LEI

- Name

- Postal Address

Take me to the Agent identification

---

<!-- ELEMENT 734 -->
Min 0 - Max 1

The Account Reporting Request message Report Period provides the ability to specify the period for which the request relates. Where used this nested element captures a mandatory From to Date and an optionally From to Time element. Min 1 - Max 1

Min 0 - Max 1

From to Date captures a mandatory From Date and an optional To Date . It allows the request to specify the date period for which the report is being requested.

---

<!-- ELEMENT 735 -->
Min 0 - Max 1

The Account Reporting Request message Reporting Sequence specifies the choice of identification sequences. This can be used as an alterative to the Reporting Period to request a sequence of reports, where the Account Servicing Institution uses this element within the reports they provide.

Where used the Reporting Sequence mandate a choice of nested element:

- From Sequence identifies the start of a sequence range. Min 1 - Max 1

- To Sequence identifies the end of a sequence range. Min 1 - Max 1

- From To Sequence identifies the start and end of a sequence range. Min 1 - Max *

- Equal Sequence identifies a sequence. Min 1 - Max *

- Not Equal Sequence identifies a sequence to be excluded. Min 1 - Max *

---

<!-- ELEMENT 736 -->
Min 0 - Max 1

The Account Reporting Request message Requested Transaction Type provides the ability to identify the specific type of transactions the request wishes to be reported.

Min 1 - Max 1

Min 1 - Max 1

Where used the Status element and Credit Debit Indicator elements are mandatory.

- Status is a nested element which may either use a choice of external ISO Entry Status code or a proprietary code. It is used to indicate the transaction entry status for which the requested reported should reflect.

- Credit Debit Indicator is a choice of embedded code to indicate whether Debit or Credit transaction entries should be reported.

Min 0 - Max 1

An optional Floor Limit element may also be used. This element requests a minimum value, for which transaction entries above this value  should be reported.

Where used the Amount and Credit Debit Indicator elements are mandatory.

As a request for specific transaction type/s to be reported, typically this request would relate to a camt.052 Bank to Customer Account Report where the specified balance information is an intraday report. The use of the camt.060 Account Reporting Request and the ability to specify specific reporting requirements in the

---

<!-- ELEMENT 737 -->
# Min 0 - Max *

The Account Reporting Request message Requested Balance Type provides the ability to identify the specific type of balances the request wishes to be reported.

# Min 1 - Max 1

Where used a choice of balance Code is mandatory which may either use a choice of external ISO Balance Type code or a proprietary code.

Min 0  - Max 1

An optional Sub Type element may also be used which a choice of external ISO Balance Sub Type code or a proprietary code.

As a request for specific balance type/s (or sub balance type/s) to be reported, typically this request would relate to a camt.052 Bank to Customer Account Report where the specified balance information is an intraday report. The use of the camt.060 Account Reporting Request and the ability to specify specific reporting requirements in the request is dependent on the Account Servicing Institution and should bilaterally agreed by

---

<!-- ELEMENT 738 -->
# Use case should be considered as a principal example whereby use case may be cross referenced

# Financial Institution Account  Reporting Request

Use Case c.60.1.1 - High Level Financial Institution  daily Account Reporting Request Use Case c.60.1.2 - Financial Institution  interim Account Reporting Request

---

<!-- ELEMENT 741 -->
# (camt) messages

---

<!-- ELEMENT 742 -->
camt.029 - camt.055 -

camt.056

Resolution of Investigation Customer Payment Cancellation Request -FI to FI Payment Cancellation Request

---

<!-- ELEMENT 743 -->
# Resolution of Investigation

---

<!-- ELEMENT 745 -->
The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any pavment nrevious settledis necessarv to trianer reversinaaccount nostinas

---

<!-- ELEMENT 746 -->
The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any pavment nrevious settledis necessarv to trianer reversinaaccount nostinas

---

<!-- ELEMENT 747 -->
The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview.

Cancel & return my payment

please

CASEABC

STATYXZ

Camt.056 Payment Cancellation Request

CASE545

STAT54X

OK, I can understand the

mistake.

camt.029 Resolution of Investigation

Customer Y

---

<!-- ELEMENT 749 -->
Min 1 - Max 1

The Payment Cancellation  Request message Identification provides a mandatory element to identify the Request

Unique reference assigned by the assigner unambiguously identify the Cancellation request.

to

For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.

Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT statement message.

---

<!-- ELEMENT 750 -->
Assigner and Assignee represent the Agents involved  in the point-to-point investigation  message exchange.  These roles therefore change on each message leg.

---

<!-- ELEMENT 751 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 753 -->
The Resolution  of Investigation Confirmation provides a mandatory element to specify the status of the Payment Cancellation  Request's investigation.

The Confirmation elementincludes a choice of three embedded confirmation codes:

- CNCL - The payment has been cancelled as requested. This status concludes the investigation, whereby a Payment Return may follow if funds need to be returned.

- PDCR - The Investigation of the Payment Cancellation Request is pending i.e. is under ongoing investigation to provide a final status confirmation. An addition Cancellation Status Reason Information should be provided to further clarify the current status. For example, a Status Reason code RQDA can be used to indicate debit authority has been requested from the Creditor.

- RJCR - The Payment Cancellation Request is rejected. A status concluding the investigation which must include additional Cancellation Status Reason Information to provide an explanation as to why the request was rejected.

---

<!-- ELEMENT 755 -->
# Min 1 - Max 1

The Resolution  of Investigation Transaction Information and Status is a mandatory nested element to capture information  related to the original payment and to provide further information  on the status reason Payment Cancellation  Request's investigation.

As part of this nested element, information is captured to reference; the case the investigation is attempting to resolve, various original references related to the original payment and the investigation status information.

---

<!-- ELEMENT 756 -->
The Resolution  of Investigation  message Cancellation Status Identification provides a mandatory element to identify the status update.

Unique reference assigned by the resolution assigner to unambiguously identify the Cancellation status.

For Exceptions and Investigations messages the Cancellation Status Identification can be considered an equivalent in the legacy MT Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT statement message.

---

<!-- ELEMENT 757 -->
The Resolution  of Investigation  message Resolved Case provides a mandatory nested element to identify the Resolved Case Identification and the Creator of the case.

# Min 1 - Max 1

The Identification element captures the unique case reference assigned by the Payment Cancellation Request Assigner to unambiguously identify the Cancellation investigation case being resolved.

For Exceptions and Investigations messages this Case Identification can be considered an equivalent of the Related Reference (Field 21) of the legacy MT Answer message.

# Min 1 - Max 1

The Creator element captures the party who created the Payment Cancellation Requestinvestigation (see camt.056 Case Creator).

This mandatory party can represent as either an Agent i.e., the Bank who created the case or as a Party i.e., the customer (for example the Debtor) who created the request. This element has no equivalent in the legacy MT Request for Cancellation message.

---

<!-- ELEMENT 758 -->
Min 1 - Max 1

The Resolution of Investigation uses elements in the Original Group Information to capture the message identifier and message name of the underlying payment for which the investigation relates to. The mandatory Original Message Identification contains the point-to-point reference from this payment, and the mandatory Original Message Name Identification contains the message name of the underlying payment. Optionally the Original Creation Date Time can also be captured.

# For example:

Original Message Name Identification 'pacs.008.001.08' confirms the investigation relates to a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as 'pacs.009.001.08' confirms the investigation relates to a pacs.009 Financial Institution Credit Transfer.

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 759 -->
The Resolution of Investigation also uses a number of other Original elements in the Transaction Information to capture information from the underlying payment that the Cancellation request relates to.

The Original elements enables the Assignee to identify the Payment which is being request to be cancelled. The following element (in addition to Original Message identification and Original Message Name Identification described on the previous page) are mandated:

Original UETR

Min 1 - Max 1

The following element (in addition to Original Message identification and Original Message Name Identification described on the previous page) are optional:

Original End to End Identification Original Instruction Identification Original Transaction Identification Original Clearing System Reference

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Cancellation Details     Transaction Information and Status

Original Group Information

Original Instruction Identification

Original End to End Identification

Original Transaction

---

<!-- ELEMENT 760 -->
5

Min 0 - Max 1

The Resolution of Investigation Cancellation Status Reason Information nested element captures the information related to the status reason of the Cancellation Resolution.

Min 0 - Max 1

the Originator element helps identify the party who provided the Cancellation status. This party would have been included in the underlying payment and is also included the pacs.004 Return Chain.

Min 0 - Max 1

the Reason for the Cancellation status, which is mandatory where the Resolution Status is RJCR, is represented by an embedded CBPR+ Cancellation Code choice ( )

Min 0 - Max 1

the Additional Information element may also be included to provide further details on the Cancellation reason.

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

In the event that an indemnity agreement is need to be established, INDM should be indicated at the beginning of the Additional

---

<!-- ELEMENT 761 -->
# Min 0 - Max 1

The Resolution of Investigation Reason element is optional. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded Code choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened after the coexistence period.

---

<!-- ELEMENT 763 -->
# Use case should be considered as a principal example whereby use case may be cross referenced

# Resolution of Investigation

Use Case c.29.1.1 - High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008) Use Case c.29.1.1.a - High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.29.1.2 - High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008) Use Case c.29.1.2.a - High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.29.2.1 - High Level Resolution of Investigation (camt.029) of a complete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.29.2.2 - High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.29.2.3 - High Level Resolution of Investigation (camt.029) of a Customer Credit Transfers (pacs.008) where the cover is returned Use Case c.29.3.1 - High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer (pacs.009) Use Case c.29.4.1 - High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer advice (pacs.009 adv)

---

<!-- ELEMENT 764 -->
# Transfer (pacs.008)

1

Agent D provides  a final outcome of the investigation  to Agent C using the camt.029.

- Debtor Agent (C) updates their outcome of the investigation  to 2

case history and relays the Agent B using the camt.029

3

Debtor Agent (B) updates their case history and relays the outcome of the investigation  to Agent A using the camt.029

- Debtor Agent (A) updates their case 4

history and informs the customer of the outcome of the investigation.

See use case p.8.1.1for the original payment, c.56.1.1 for case resolution and p.4.1.3. for an example payment return

---

<!-- ELEMENT 765 -->
# Transfer (pacs.008) using gpi Stop and Recall

See use case p.8.1.1for the original payment, c.29.1.1 for case resolution and p.4.1.3. for an example payment return

1

2

Agent D provides  an update on the investigation  to the gpi Tracker using the camt.029.

gpi Tracker forwards  the response to Agent A as the initiator of the original  camt.056

3

Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

---

<!-- ELEMENT 766 -->
# Credit Transfer (pacs.008)

- outcome of the investigation  to 1

2

3

Agent C provides  a final Agent B using the camt.029

Debtor Agent (B) updates their case history and relays the outcome of the investigation  to

Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

See use case p.8.1.1for the original payment, c.56.1.2 for case resolution and p.4.1.3. for an example payment return

---

<!-- ELEMENT 767 -->
# Credit Transfer (pacs.008) using gpi Stop and Recall

1

2

3

Agent C provides  an update on the investigation  to the gpi Tracker using the camt.029.

gpi Tracker forwards  the response to Agent A as the initiator of the original  camt.056

Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

---

<!-- ELEMENT 768 -->
# Transfer (pacs.008) settled using a cover method

---

<!-- ELEMENT 769 -->
# Credit Transfer (pacs.008) settled using a cover method.

---

<!-- ELEMENT 770 -->
# Transfers (pacs.008) where the cover is returned

1

2

Agent C receives  the payment and recognises the payment can not be completed as requested e.g. the Agent D does not maintain an account with them.

Debtor Agent (A) assigns a Cancellation Request to Agent D (assignee) requesting the original pacs.008 is considered null and void, using reason code COVR.

Agent D creates an investigation  case. Recognising the cover  payment will not be received  to settle the pacs.008. As the creditor has not been credited in advance  of cover settlement, a final resolution to the investigation  can be provided.  A payment return is not necessary.

---

<!-- ELEMENT 771 -->
# Credit Transfer (pacs.009)

Debtor Agent (B) updates their case history and informs the customer (Agent A) of the outcome of the investigation.

See use case p.9.1.1 for the cover payment sample c.56.3.1 for case resolution and p.4.2.3 for payment return

1

Agent C provides  a final outcome of the investigation  to Agent B using the camt.029.

2

---

<!-- ELEMENT 772 -->
# Credit Transfer advice (pacs.009 adv)

B

2

1

Debtor request their bank to recall a previous  instructed payment, as the amount was incorrect.

1

C

2

pacs.009 (ADV)

camt.056

camt.029

pacs.009

pacs.002

Debtor Agent (A) assigns a Cancellation Request to Agent E (assignee) requesting the original pacs.008 is returned, using reason code AM09.

3

D

See use case p.9.1.2 for the cover payment sample c.56.4.1 for case resolution and p.4.2.3 for payment return

Agent E creates an investigation  case. Recognising the payment has already been credited to the creditor. They request debit authority, proving  the reason specified for the return request and update Agent B.

Once the outcome to the debit authorisation is know a final resolution to the investigation  can be relayed and any necessary

E

F

3

camt.054

---

<!-- ELEMENT 773 -->
# Customer Payment Cancellation Request

---

<!-- ELEMENT 775 -->
The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This

---

<!-- ELEMENT 776 -->
# Initiation'

The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This

---

<!-- ELEMENT 777 -->
The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This

---

<!-- ELEMENT 778 -->
The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview.

Camt.055 Payment Cancellation Request

CASE545

STAT54X

OK, I can understand the

mistake.

camt.029 Resolution of Investigation

Customer Y

---

<!-- ELEMENT 780 -->
Min 1 - Max 1

The Payment Cancellation  Request message Identification provides a mandatory element to identify the Request

Unique reference assigned by the assigner unambiguously identify the Cancellation request.

to

For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.

Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT statement message.

---

<!-- ELEMENT 781 -->
Assigner and Assignee represent the Agents involved  in the point-to-point investigation  message exchange.  These roles therefore change on each message leg.

---

<!-- ELEMENT 782 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 783 -->
Information and Cancellation.

---

<!-- ELEMENT 784 -->
# Identification

The Payment Cancellation  Request message Original Payment Information Identification provides a mandatory element to identify the Original Payment Initiation Request

This Unique reference identifies the Payment Information Identification from the original Payment Initiation request.

Refer to the relevant Payment Information Identification element in the original message for details on that reference.

Link to Pain.001 Link to Pain.008

Underlying

Original Payment Information and Cancellation

---

<!-- ELEMENT 785 -->
Min 1 - Max 1

The Payment Cancellation Request uses elements in the Original Group Information to capture the message identifier and message name of the underlying payment for which the Cancellation is being requested. The mandatory Original Message Identification contains the point-to-point reference from this payment, and the mandatory Original Message Name Identification contains the message name of the underlying payment. Optionally the Original Creation Date Time can also be captured.

# For example:

Original Message Name Identification 'pain.001.001.09' confirms the Cancellation request is for a pain.001 Interbank Customer Credit Transfer Initiation.

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 786 -->
The Payment Cancellation  Request message Cancelation Identification provides an optional element to identify the Request

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.

For Exceptions and Investigations messages the Cancellation Identification can be considered an equivalent in the legacy MT Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT statement message.

Original Payment Information and Cancellation

---

<!-- ELEMENT 787 -->
Min 1 - Max 1

The Payment Cancellation  Request message Case provides a mandatory nested element to identify the Case Identification and the Creator of the case.

# Min 1 - Max 1

The Identification element captures a unique case reference assigned by the assigner to unambiguously identify the Cancellation investigation case.

For Exceptions and Investigations messages the Case Identification can be considered an equivalent of the Transaction Reference Number (Field 20) of the legacy MT Requestfor Cancellation message.

Min 1 - Max 1

The Creator element captures the party who created the investigation. This mandatory party can represent as either an Agent i.e., the Bank who created the case or as a Party i.e., the customer (for example the Debtor) who created the request. In CBPR+ the creator is always expected to be an Agent.

This element has no equivalent in the legacy MT Request for Cancellation message.

---

<!-- ELEMENT 788 -->
The Payment Cancellation Request also uses a number of other Original elements in the Transaction Information to capture information from the underlying payment that the Cancellation request relates to.

The Original elements enables the Assignee to identify the Payment which is being request to be cancelled. The following element (in addition to Original Message identification and Original Message Name Identification ) are mandated:

Original End to End Identification Original UETR

Original Instructed Amount

Min 1 - Max 1

Min 1 - Max 1

Min 1 - Max 1

One of the following elements is also required depending on the Date element in the original message, where Original Request Execution Date relates to the pain.001 and Original Request Collection Date relates to the pain.008 : Underlying Original Payment Information and Cancellation

Original Requested Execution Date Original Request Collection Date

The following element is optional:

---

<!-- ELEMENT 789 -->
5

Min 1 - Max 1

The Payment Cancellation Request Cancellation Reason Information nested element captures information associated with the reason for the Cancellation request.

Min 0 - Max 1

the Originator element helps identify the party who request the payment Cancellation. This party would have been included in the underlying payment and is also included the pacs.004 Return Chain as the Creditor.

Min 1 - Max 1

the Reason is mandatory and represented by an embedded CBPR+ Cancellation Code choice ( )

Min 0 - Max 2

the Additional Information element may also be included to provide further details on the Cancellation reason.

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

Underlying

Original Payment Information and Cancellation

Transaction Information     Cancellation Reason Info'

Originator

---

<!-- ELEMENT 790 -->
# Min 1 - Max 1

The Payment Cancellation Request Reason element is mandatory. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded Code choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened after the coexistence period.

---

<!-- ELEMENT 791 -->
# (continued)

---

<!-- ELEMENT 792 -->
# Use case should be considered as a principal example whereby use case may be cross referenced

# Payment Cancellation Request

Use Case c.55.1.1 -

---

<!-- ELEMENT 793 -->
In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collections of funds from the debtor's accounts for a creditor.

---

<!-- ELEMENT 794 -->
# Payment Market Infrastructure

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collection of funds from the debtor's accounts for a creditor (through a Payment Market Infrastructure).

---

<!-- ELEMENT 795 -->
Financial Institution to Financial Institution Payment

Cancellation Request

---

<!-- ELEMENT 797 -->
The FIToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The

---

<!-- ELEMENT 798 -->
The FIToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The

---

<!-- ELEMENT 799 -->
The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview.

Cancel & return my payment

please

CASEABC

STATYXZ

Camt.056 Payment Cancellation Request

CASE545

STAT54X

OK, I can understand the

mistake.

camt.029 Resolution of Investigation

Customer Y

---

<!-- ELEMENT 801 -->
Min 1 - Max 1

The Payment Cancellation  Request message Identification provides a mandatory element to identify the Request

Unique reference assigned by the assigner unambiguously identify the Cancellation request.

to

For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.

Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT statement message.

---

<!-- ELEMENT 802 -->
Assigner and Assignee represent the Agents involved  in the point-to-point investigation  message exchange.  These roles therefore change on each message leg.

---

<!-- ELEMENT 803 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 805 -->
The Payment Cancellation  Request message Cancellation Identification provides an optional element to identify the Request

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.

For Exceptions and Investigations messages the Cancellation Identification can be considered an equivalent in the legacy MT Directly comparable with the Transaction Reference Number (Field 20) of the legacy MT statement message.

WhereCancellation Identification is used this should represent the reference value as the Case Identification

---

<!-- ELEMENT 806 -->
# Min 1 - Max 1

The Payment Cancellation  Request message Case provides a mandatory nested element to identify the Case Identification and the Creator of the case.

# Min 1 - Max 1

The Identification element captures a unique case reference assigned by the assigner to unambiguously identify the Cancellation investigation case.

For Exceptions and Investigations messages the Case Identification can be considered an equivalent of the Transaction Reference Number (Field 20) of the legacy MT Requestfor Cancellation message.

Min 1 - Max 1

The Creator element captures the party who created the investigation. This mandatory party can represent as either an Agent i.e., the Bank who created the case or as a Party i.e., the customer (for example the Debtor) who created the request. In CBPR+ the creator is always expected to be an Agent.

This element has no equivalent in the legacy MT Request for Cancellation message.

---

<!-- ELEMENT 807 -->
Min 1 - Max 1

The Payment Cancellation Request uses elements in the Original Group Information to capture the message identifier and message name of the underlying payment for which the Cancellation is being requested. The mandatory Original Message Identification contains the point-to-point reference from this payment, and the mandatory Original Message Name Identification contains the message name of the underlying payment. Optionally the Original Creation Date Time can also be captured.

# For example:

Original Message Name Identification 'pacs.008.001.08' confirms the Cancellation request is for a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as 'pacs.009.001.08' confirms the Cancellation request for a pacs.009 Financial Institution Credit Transfer.

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- ELEMENT 808 -->
The Payment Cancellation Request also uses a number of other Original elements in the Transaction Information to capture information from the underlying payment that the Cancellation request relates to.

The Original elements enables the Assignee to identify the Payment which is being request to be cancelled. The following element (in addition to Original Message identification and Original Message Name Identification described on the previous page) are mandated:

Min 1 - Max 1

Min 1 - Max 1

Min 1 - Max 1

Min 1 - Max 1

Original End to End Identification Original UETR Original Interbank Settlement Amount Original Interbank Settlement Date

The following element (in addition to Original Message identification and Original Message Name Identification described on the previous page) are optional:

Original Instruction Identification Original Transaction Identification Original Clearing System Reference

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Underlying

Transaction Information

Original Instruction Identification

Original End to End Identification

Original Transaction

Original UETR

Original Clearing System Reference

- Original Interbank Settlement Amount

---

<!-- ELEMENT 809 -->
Min 1 - Max 1

The Payment Cancellation Request Cancellation Reason Information nested element captures information associated with the reason for the Cancellation request.

# Min 0 - Max 1

the Originator element helps identify the party who request the payment Cancellation. This party would have been included in the underlying payment and is also included the pacs.004 Return Chain as the Creditor.

Min 1 - Max 1

- Min 0 - Max 2 the Reason is mandatory and represented by an embedded CBPR+ Cancellation Code choice ( )

5

the

Additional

Information

Cancellation reason.

element may

also be

included to

provide further

details

- Note where Reason code NARR is used additional information must be

provided to describe the reason for the Cancellation request.

Underlying

In the event that the case assigner wishes it indicate a willingness to

Transaction Information     Cancellation Reason Info'

Originator on

the

---

<!-- ELEMENT 810 -->
Min 1 - Max 1

The Payment Cancellation Request Reason element is mandatory. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded Code choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened after the coexistence period.

---

<!-- ELEMENT 811 -->
# (continued)

---

<!-- ELEMENT 812 -->
# Use case should be considered as a principal example whereby use case may be cross referenced

# Payment Cancellation Request

Use Case c.56.1.1 - High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008) Use Case c.56.1.1.a  - High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.56.1.2 - High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008) Use Case c.56.1.2.a - High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall Use Case c.56.2.1 - High Level Payment Cancellation Request (camt.056) of a complete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.56.2.2 - High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method Use Case c.56.2.3 - High Level Payment Cancellation Request (camt.056) of a Customer Credit Transfers (pacs.008) where the cover is returned Use Case c.56.3.1 - High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer (pacs.009) Use Case c.56.4.1 - High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer advice (pacs.009 adv)

---

<!-- ELEMENT 813 -->
# Credit Transfer (pacs.008)

Debtor request their bank to recall a previous  instructed payment, as the amount was incorrect.

Debtor Agent (A) assigns a Cancellation Request to Agent B (assignee) requesting the

Agent B creates an investigation  case. Recognising the payment has already been onward  processed. They update Agent A and assign a Cancellation Request directly to Agent C.

Agent C creates an investigation  case. Recognising the payment has already been onward  processed. They update

See use case p.8.1.1for the original payment, c.29.1.1 for case resolution and p.4.1.3. for an example payment return

1

2

3

4

5

Agent D creates an investigation  case. Recognising the payment has already reason specified for the return request been credited to the creditor. They request debit authority, providing  the and updates Agent C. Once the outcome to the debit authorisation is know a final resolution to the investigation  can be relayed any necessary return payment is arrange.

---

<!-- ELEMENT 814 -->
# Credit Transfer (pacs.008) using gpi Stop and Recall

See use case p.8.1.1for the original payment, c.29.1.1 for case resolution and p.4.1.3. for an example payment return

Agent D creates an investigation  case. Recognising the payment has already been credited to the creditor. They request debit authority, providing  the reason specified for the return request and updates the gpi Tracker.

Once the outcome to the debit authorisation is know a final resolution to the investigation  can be provided  and any necessary return payment is arrange.

1

2

Debtor request their bank to recall a previous  instructed payment, as the amount was incorrect.

Debtor Agent (A) initiates a gpi Stop and Recall, requesting the original pacs.008 is

- complete and forwards  a camt.056 to 3

gpi Tracker identifies the payment is Agent D.

4

---

<!-- ELEMENT 815 -->
# Credit Transfer (pacs.008)

Debtor request their bank to recall a previous  instructed payment, as the amount was incorrect.

Debtor Agent (A) assigns a Cancellation Request to Agent B (assignee) requesting the

Agent B creates an investigation  case. Recognising the payment has already been onward  processed. They update Agent A and assign a Cancellation Request directly to Agent C.

1

2

3

See use case p.8.1.1for the original payment, c.29.1.2 for case resolution and p.4.1.3. for an example payment return

- Agent C creates an investigation  case. Recognising the payment has not been onward  processed. They update Agent 4

B that the Cancellation Request is accepted any necessary return payment is arrange.

---

<!-- ELEMENT 816 -->
# Credit Transfer (pacs.008) using gpi Stop and Recall

1

2

- incomplete and forwards  a camt.056 to 3

4

Agent C creates an investigation  case. Recognising the payment has not been onward processed. They updates the gpi Tracker any necessary return payment is arrange.

Debtor request their bank to recall a previous  instructed payment, as the amount was incorrect.

Debtor Agent (A) initiates a gpi Stop and Recall, requesting the original pacs.008 is gpi Tracker identifies the payment is Agent C.

---

<!-- ELEMENT 817 -->
# Transfer (pacs.008) settled using a cover method.

---

<!-- ELEMENT 818 -->
# Credit Transfer (pacs.008) settled using a cover method.

---

<!-- ELEMENT 819 -->
# Transfers (pacs.008) where the cover is returned

1

2

Agent C receives  the payment and recognises the payment can not be completed as requested e.g. the Agent D does not maintain an account with them.

Debtor Agent (A) assigns a Cancellation Request to Agent D (assignee) requesting the original pacs.008 is considered null and void, using reason code COVR.

Agent D creates an investigation  case. Recognising the cover  payment will not be received  to settle the pacs.008. As the creditor has not been credited in advance  of cover settlement, a final resolution to the investigation  can be provided.  A payment return is not necessary.

---

<!-- ELEMENT 820 -->
# Institution Credit Transfer (pacs.009)

1

2

3

Agent C creates an investigation  case. Recognising the payment has already been credited to the creditor. They request debit authority, proving  the reason specified for the return request and update Agent C. Once the outcome to the debit authorisation is know a final resolution to the investigation  can be relayed and

Debtor request their bank to recall a previous  instructed payment, as the amount was incorrect.

Debtor Agent (A) assigns a Cancellation Request to Agent C (assignee) requesting the original pacs.009 is returned, using reason code AM09.

---

<!-- ELEMENT 821 -->
# Credit Transfer advice (pacs.009 adv)

B

2

1

Debtor request their bank to recall a previous  instructed payment, as the amount was incorrect.

1

C

2

pacs.009 (ADV)

camt.056

camt.029

pacs.009

pacs.002

Debtor Agent (A) assigns a Cancellation Request to Agent E (assignee) requesting the original pacs.008 is returned, using reason code AM09.

3

D

See use case p.9.1.2 for the cover payment sample c.29.4.1 for case resolution and p.4.2.3 for payment return

Agent E creates an investigation  case. Recognising the payment has already been credited to the creditor. They request debit authority, proving  the reason specified for the return request and update Agent B.

Once the outcome to the debit authorisation is know a final resolution to the investigation  can be relayed and any necessary

E

F

3

camt.054

---

<!-- ELEMENT 822 -->
camt.107 -Cheque Presentment Notification camt.108 - Cheque Cancellation or Stop Request camt.109 -Cheque Cancellation or Stop Report

---

<!-- ELEMENT 823 -->
# Cheque Presentment Notification

---

<!-- ELEMENT 825 -->
The Agent A (drawer agent) sends a ChequePresentmentNotificationmessage to Agent B (the drawee agent). The ChequePresentmentNotificationmessage informs the drawee agent about the cheque submission. The notification message facilitates the drawee agent to follow up the cheque submission and relevant business process.

---

<!-- ELEMENT 827 -->
Each ISO 20022 cash management message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the Message Identification has no exact equivalent in the legacy MT Advice of Cheque message. However, the Sender's Reference (Field 20) could be considered a similar comparison.

---

<!-- ELEMENT 828 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 829 -->
The number of Cheques in CBPR+ cheque payment usage guidelines  is fixed to 1.

---

<!-- ELEMENT 831 -->
# Min 1 - Max 1

The Cheque Presentment  Notification Cheque nested element specifies the details of the Cheque.

This Cheque  element has been restricted to one cheque  occurrence.

---

<!-- ELEMENT 832 -->
Min 1 - Max 1

The Cheque Presentment  Notification Instruction Identification provides an optional element to identify unambiguously  the instruction

Point to point reference that can be used between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

---

<!-- ELEMENT 833 -->
Min 1 - Max 1

The Cheque Number Notification Cheque Number provides a mandatory element to identify unambiguously  the Cheque.

48

Unique and unambiguous number for a cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque

---

<!-- ELEMENT 834 -->
The Cheque Presentment  Notification has several element to capture a Date related to the cheque.

# Min 1 - Max 1

The Issue Date is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer

# Min 0 - Max 1

The Stale Date is an optional element and represents the date after which a cheque is no longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days' or may be determined in accordance with domestic banking practice. Not all countries will have a validity period.

---

<!-- ELEMENT 835 -->
# Min 0 - Max 1

The Value Date is an optional element, it is used to capture the Date , where different to the Issue Date , i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account.

Cheque

Amount

---

<!-- ELEMENT 836 -->
Min 1 - Max 1

The Cheque Presentment  Notification Payer captures the party that instructs the Drawee Agent to issues a cheque to pay a specific amount, upon presentment, to the payee. The Payer sub-element  describe the Payer in greater detail.

Nested element capturing either structured or unstructured Payer address details

Mandatory

Name

Postal

Address

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Identification

Optional element to capture the Payee's ISO

Payer

Country of

Residence

Name

---

<!-- ELEMENT 837 -->
The Cheque Presentment  Notification Payer Account is used to capture the account of the party that instructs the Drawee Agent to issues a cheque to pay a specific amount, upon presentment, to the payee.

The Payer Account uses a variety of nested elements to capture information related to the account.

Min 0  - Max 1 Identification identifies the account maintained at the Drawer Agent (Account Servicing Institution)

Min 0 - Max 1

Type uses the external Cash Account Type code list to identify the type of account

Min 0 - Max 1

Min 0 - Max 1

Min 0 - Max 1

Currency identifies the currency of the account

Name identifies the name of the account as assigned by the Drawer Agent (Account Servicing Institution)

Proxy captures an alternative identification of the account number such as an email address. This element has further nested Type which is a choice of external code list or proprietary code and Identification which are both mandatory where the Proxy element is used.

---

<!-- ELEMENT 838 -->
# Min 0 - Max 1

The Cheque Presentment  Notification Drawer Agent optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque  Presentment Notification is sent to the Drawee Agent .

Min 0 - Max 1

The Drawer Agent Account optionally captures the Drawer Agent's Account with the Drawee Agent and who would receive an order the pay the cheque upon presentment.

The Drawer Bank is typically identified on the cheque together with their Postal Address. The Drawer Agent's Account with the Drawee Agent is also often also identified on the cheque.

Cheque

---

<!-- ELEMENT 839 -->
Min 1 - Max 1

The Cheque Presentment  Notification Payee captures the party that should receive an amount  of money as specified in the cheque. The Payee sub-element  describe the Payee in greater detail.

Nested element capturing either structured or unstructured Payee address details

Mandatory

Name

Postal

Address

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Identification

Optional element to capture the Payee's ISO

Payee

Country of

Residence

Name

---

<!-- ELEMENT 840 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Serial Financial Institution to Financial Institution to Customer Credit Transfer

Use Case c.107.1 - High Level Drawer Agent Cheque issuance to Payee, on their account with the Drawer Agent

Use Case c.107.2 - High Level Drawer Agent Cheque issuance to Payee, on their head office's account with the Drawer Agent

---

<!-- ELEMENT 841 -->
1

2a

Drawer  Agent (A) issues a cheque to the Payee drawn  of their account at the Drawee Agent (B)

2b

In parallel the Drawer  Agent (A) initiates a Cheque  Presentment Notification to the Drawee  Agent (B)

# Drawee Agent

1

Payer

Drawer

Payer instructs the Drawer

Agent to issue a cheque to the

Payee

A

2a

2b

3

B

Drawee

The Drawee Agent (B) receives the Cheque  Presentment Notification and store the information  in anticipation for the cheque to be presented

3

6

12,000

5

5

C

4

Payee received  the cheque and present it to their bank (Agent C)

Agent C receives  the cheque deposit and present it into the domestic cheque clearing

4

12,000

6

Drawee  Agent (B) receives  the cheque presentment via the cheque clearing. They validate  the presented cheque details again the information  received  on the Cheque Presentment Notification to conclude whether  the cheque can be settled.

Payee

---

<!-- ELEMENT 842 -->
1

2a

Agent (A) issues a cheque to the Payee drawn of their head office's (HO) account at the Drawer  Agent (B)

2b

In parallel the Agent (A) initiates a Cheque  Presentment Notification to the Drawee  Agent (B)

# account with the Drawee Agent

1

HO

Drawer

Payer instructs their Bank

(Agent A) to issue a cheque to the Payer

2a

2b

Payer

A

B

Drawee

3

The Drawee Agent (B) receives the Cheque  Presentment Notification and store the information  in anticipation for the cheque to be presented

3

6

12,000

4

5

C

Payee received  the cheque and present it to their bank (Agent C)

Agent C receives  the cheque deposit and present it into the

domestic cheque clearing

5

4

12,000

6

Drawee  Agent (B) receives  the cheque presentment via the cheque clearing. They validate  the presented cheque details again the information  received  on the Cheque Presentment Notification to conclude whether  the cheque can be settled.

Payee

---

<!-- ELEMENT 843 -->
# Cheque Cancellation or Stop Request

---

<!-- ELEMENT 845 -->
The Agent A (Drawer Agent) sends a ChequeCancelationOrStopRequest message to Agent B (the Drawee Agent). The ChequeCancelationOrStopReques message requests the drawee agent to place a stop (refusal to settle) upon presentment of the cheque, effectively canceling the issued cheque.

---

<!-- ELEMENT 847 -->
Each ISO 20022 cash management message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the Message Identification has no exact equivalent in the legacy MT Advice of Cheque message. However, the Sender's Reference (Field 20) could be considered a similar comparison.

---

<!-- ELEMENT 848 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 849 -->
The number of Cheques in CBPR+ cheque payment usage guidelines  is fixed to 1.

---

<!-- ELEMENT 851 -->
Min 1 - Max 1

The Cheque Cancellation  or Stop Request Cheque nested element specifies the details of the Cheque.

This Cheque  element has been restricted to one cheque  occurrence.

---

<!-- ELEMENT 852 -->
Min 0 - Max 1

The Cheque Cancellation  or Stop Request Instruction Identification provides an optional element to identify unambiguously  the instruction

Point to point reference that can be used between the Agent instructing the Cheque Cancellation or Stop Request and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

---

<!-- ELEMENT 853 -->
The Cheque Cancellation  or Stop Request Original Instruction Identification provides an optional element to identify unambiguously  the original instruction

Point to point reference that can be used to identify the original Cheque Presentment Notification between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

---

<!-- ELEMENT 854 -->
Min 1 - Max 1

The Cheque Cancellation  or Stop Request Cheque Number provides a mandatory element to identify unambiguously  the Cheque.

48

Unique and unambiguous number for the cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque

---

<!-- ELEMENT 855 -->
The Cheque Cancellation  or Stop Request has several element to capture a Date related to the cheque.

# Min 1 - Max 1

The Issue Date is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer

# Min 0 - Max 1

The Stale Date is an optional element and represents the date after which a cheque is no longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days' or may be determined in accordance with domestic banking practice. Not all countries will have a validity period.

---

<!-- ELEMENT 856 -->
Min 0 - Max 1

The Effective Date is an optional element, it is used to capture the original Value Date (as provided in the camt.107), where different to the original Issue Date , i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account.

---

<!-- ELEMENT 857 -->
# Min 0 - Max 1

The Cheque Cancellation  or Stop Request Drawer Agent optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque  Presentment Notification is sent to the Drawee Agent.

The Drawer Agent Account optionally captures the Drawer Agent's Account with the Drawee Agent and who would receive an order the pay the cheque upon presentment.

The Drawer Agent and Drawer Account elements where present should match that of the original camt.107 ChequePresentmentNotification.

---

<!-- ELEMENT 858 -->
Min 0 - Max 1

The Cheque Cancellation  or Stop Request Payee captures the party that should receive an amount  of money as specified in the cheque. The Payee sub-element  describe the Payee in greater detail.

Nested element capturing either

Payee structured or unstructured

address details

Nested element capturing the various types of identifiers for

Mandatory

Name

Postal

Address

Identification the party e.g. BIC, LEI etc.

Optional element to capture the Payee's ISO

Payee

Country of

Residence

Name

---

<!-- ELEMENT 859 -->
5

Min 1 - Max 1

The Cheque Cancellation or Stop Request Cheque Cancellation or Stop Reason nested element captures information associated with the reason for the Cheque Cancellation or Stop request.

Min 0 - Max 1

the Originator element is a embedded code choice that helps identify the party who request the cheque cancellation or stop request. Where used this party would typically be the Payer (code PAYR ) of the cheque.

Min 1 - Max 1

the Reason is mandatory and represented by an embedded CBPR+ Cancellation Code choice ( )

Min 0 - Max 2

the Additional Information element may also be included to provide further details on the cancellation or stop reason.

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cheque Cancellation or Stop request.

Cheque     Cheque Cancellation or Stop Reason

Originator

---

<!-- ELEMENT 860 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Serial Financial Institution to Financial Institution to Customer Credit Transfer

Use Case c.108.1 - High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque

Use Case c.108.2 - High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.

---

<!-- ELEMENT 861 -->
# lost cheque.

1

Payer instructs the Drawer Agent they wish to cancel or stop a previously  issued cheque, as the Payee informs them the cheque has been lost.

2

3

Drawee  Agent (B) match the request to the previous  Cheque  Presentment Notification (camt.107). As the cheque has not been presented the status record is identified as not to be paid if presented, as a result of a cancellation/stop request. This is reported  back to the Drawer  Agent

Drawer  Agent (A) issues a cheque cancellation or stop request to the Drawee  Agent (B) with reason code LOST

---

<!-- ELEMENT 862 -->
of the Payer customer.

1

A

2

Drawer

3

Payer instructs the Drawer Agent they wish to cancel or stop a previously  issued cheque, as the Payer informs them they no longer wish to honour  the cheque.

Payer

1

B

Drawee

2

12,000

Drawer  Agent (A) issues a cheque cancellation or stop

request to the Drawee  Agent (B)

with reason code CUST

3

C

Drawee  Agent (B) match the request to the previous  Cheque  Presentment Notification (camt.107). As the cheque has already been presented and paid the cancellation/stop request can not be executed. This is reported  back to the Drawer  Agent (A) as rejected with additional

12,000

See use case c.109.1.2 for an example the

Cheque Cancellation or Stop Report

Payee

---

<!-- ELEMENT 863 -->
# Cheque Cancellation or Stop Report

---

<!-- ELEMENT 867 -->
Each ISO 20022 cash management message has a Message Identification element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the Message Identification has no exact equivalent in the legacy MT Advice of Cheque message. However, the Sender's Reference (Field 20) could be considered a similar comparison.

---

<!-- ELEMENT 868 -->
CBPR+ usage guidelines  mandate the time zone that the time represents as an offset against Universal  Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm

- For example: 2002-10-10T12:00:00-05:00 (noon/midday  on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- ELEMENT 869 -->
The number of Cheques in CBPR+ cheque payment usage guidelines  is fixed to 1.

---

<!-- ELEMENT 871 -->
# Min 1 - Max 1

The Cheque Cancellation  or Stop Report Cheque nested element specifies the details of the Cheque.

This Cheque  element has been restricted to one cheque  occurrence.

---

<!-- ELEMENT 872 -->
Min 0 - Max 1

The Cheque Cancellation  or Stop Report Instruction Identification provides an optional element to identify unambiguously  the instruction

Point to point reference that can be used between the Drawee Agent providing the Cheque Cancellation or Stop Report and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

---

<!-- ELEMENT 873 -->
The Cheque Cancellation  or Stop Request Original Instruction Identification provides an optional element to identify unambiguously  the original instruction

Point to point reference that can be used to identify the original Cheque Cancellation or Stop Request between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving the request message) to refer to the individual request.

---

<!-- ELEMENT 874 -->
The Cheque Cancellation  or Stop Request Cheque Number provides a mandatory element to identify unambiguously  the Cheque.

48

Unique and unambiguous number for the cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque

---

<!-- ELEMENT 875 -->
The Cheque Cancellation  or Stop Report has several element to capture a Date related to the cheque.

# Min 1 - Max 1

The Issue Date is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer

# Min 0 - Max 1

The Stale Date is an optional element and represents the date after which a cheque is no longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days' or may be determined in accordance with domestic banking practice. Not all countries will have a validity period.

---

<!-- ELEMENT 876 -->
Min 0 - Max 1

The Effective Date is an optional element, it is used to capture the original Value Date (as provided in the camt.107), where different to the original Issue Date , i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account.

---

<!-- ELEMENT 877 -->
# Min 0 - Max 1

The Cheque Cancellation  or Stop Request Drawer Agent optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque  Presentment Notification is sent to the Drawee Agent.

The Drawer Agent Account optionally captures the Drawer Agent's Account with the Drawee Agent and who would receive an order the pay the cheque upon presentment.

The Drawer Agent and Drawer Account elements where present should match that of the original camt.107 ChequePresentmentNotification.

---

<!-- ELEMENT 878 -->
Min 0 - Max 1

The Cheque Cancellation  or Stop Request Payee captures the party that should receive an amount  of money as specified in the cheque. The Payee sub-element  describe the Payee in greater detail.

Nested element capturing either

Payee structured or unstructured

address details

Nested element capturing the various types of identifiers for

Mandatory

Name

Postal

Address

Identification the party e.g. BIC, LEI etc.

Optional element to capture the Payee's ISO

Payee

Country of

Residence

Name

---

<!-- ELEMENT 879 -->
!

Min 1 - Max 1

The Cheque Cancellation or Stop Request Cheque Cancellation or Stop Reason nested element captures information associated with the reason for the Cheque Cancellation or Stop request.

Min 0 - Max 1

the Originator element helps identify the party who request the cheque cancellation or stop request. Where used this party would typically be the Payer of the cheque.

Min 1 - Max 1

the Status is mandatory and represented by an embedded status Code choice ( ) REJT (Rejected) or ACCP (Accepted)

Min 0 - Max 2

the Additional Information element may also be included to provide further details on the cancellation or stop reason.

Note where Status code REJT is used additional information must be provided to describe the reason for the rejection.

Cheque     Cheque Cancellation or Stop Reason

Originator

---

<!-- ELEMENT 880 -->
Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving  a Market Infrastructure can apply the Market  Infrastructure  legs to other use cases.

# Serial Financial Institution to Financial Institution to Customer Credit Transfer

Use Case c.109.1 - High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque

Use Case c.109.2 - High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.

---

<!-- ELEMENT 883 -->
www.swift.com

---

