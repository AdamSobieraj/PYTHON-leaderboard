<!-- ELEMENT 1 -->
core topics where other 
relevant messages may 
also be referred to within 
the use case, it may also be 
necessary to consider other 
documented use cases, in 
order to capture a wider 
variation of scenarios.
This document jointly 
developed with the CBPR+ 
group continues to evolve 
inline with the Standards 
Release as: • CBPR+ continue to 
develop market practice 
guidelines for additional 
message.
• Inaccuracies are 
identified and corrected.
• Further use cases 
and/or explanation 
needs are identified
Reporting plus (CBPR+) User 
Handbook is intended to 
document and explain a 
variety of ISO 20022 payment 
related topics, as well as 
provide practical use cases to 
ensure a common 
understanding and adoption of 
ISO 20022 within the payment 
industry.
The SWIFT FINplus service 
will support CBPR+ messages 
on the SWIFT network 
traditionally associated with 
correspondent banking (many-
to-many). These messages 
may be exchanged either 
between Agents in the same 
country or between Agents in 
different countries.
1

New slide since last iteration U Slide updated since last iteration
The following icons dignify changes to slide from the previous itineration. 
Updates to text on a slide are captured in gold.
Page 33 Updated – new messages and Usage Ids added
Page 40 Updated – new pain message added to index
Page 45 Updated – recognition of Payment Initiation relay rulebook
Page 107 Updated – recognition of Payment Initiation relay rulebook
Page 122 Updated – additional use cases in the index
Page 126 New –use case
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
Page 764 Updated - use case id correction
Page 774-795 New – Customer Cancellation Request section
Page 823-883 New – Cheque message sections 
Page 880 Updated - use case id correction
2

Focal Message type and direction
Agent
Legacy FIN MT message
Cash Management Reporting (camt)
Cash Management Exception & 
Investigations (camt)
Focus message
Market Infrastructure
Exceptional circumstance
Statement Authorised Party
Exception & Investigation Case Assignee
pacs.008 Ultimate Debtor
pacs.008 Ultimate Creditor
Use Case variation
MT
pacs Debtor
pacs Creditor
Agent processing legacy format 
during a coexistence period
Statement Account Servicer
Extra attention is needed
Initiating party on behalf of the Debtor
New slide since last iteration
U Slide updated since last iteration
Nested Element
Element Hierarchy Path
Element Choice
Nested Element involving a choice
Shortcut to other part of document
Best practice
3
Statement Account Owner
gpi Tracker

3. Payment Initiation (pain)
pain.001 - Interbank Customer Credit Transfer Initiation
pain.002 - Interbank Customer Payment Status Report
pain.008 – Customer Direct Debit Initiation
4. Payment, Clearing and Settlement (pacs) messages
pacs.002 – Financial Institution to Financial Institution Payment Status Report 
pacs.004 – Payment Return
pacs.003 – Financial Institution to Financial Institution Customer Direct Debit
pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer 
pacs.009 (core) - Financial Institution Credit Transfer 
pacs.009 (cov) - Financial Institution ‘Cover’ Credit Transfer
pacs.009 (adv) – Financial Institution ‘Advice’ Credit Transfer 
pacs.010 – Financial Institution Direct Debit
pacs.010 – Financial Institution Direct Debit – Margin Collection 4
new for SR2023
new for SR2023
new for SR2023

camt.053 - Bank to Customer Statement
camt.054 - Bank to Customer Debit Credit Notification
camt.057 – Notification to Receive
camt.058 – Notification to Receive Cancelation Advice 
6. Cash Management Exception & Investigation (camt) messages
camt.029 - Resolution of Investigation
camt.055 – Customer Payment Cancelation Request
camt.056 - FI to FI Cancellation Request
7. Cheques
camt.107 – Cheque Presentment Notification
camt.108 – Cheque Cancellation or Stop Notification
camt.109 – Cheque Cancellation or Stop Report
5
new for SR2023
new for SR2023
new for SR2023
new for SR2023
new for SR2023

6

fundamental change to the 
traditional language used by the 
payments industry for several 
decades. It also describes 
participants (i.e., parties) to a 
business transaction differently 
based upon the business domain 
(area) being described, in a similar 
way you may describe a person as a 
colleague, parent or sibling 
depending upon the context you 
wish to describe them. This section 
is designed to capture and explain 
some of the differences. 
7

acmt Account Management
auth Authorities
camt Cash Management
pacs Payment Clearing and Settlement
pain Payment Initiation
remt Payment Remittance Advice
Message Definitions
ISO 20022 catalogue messages hierarchically beginning with a 
Business Domain, contain a various sets of Message Definitions, which 
in turn contain a variety of Message Sets.
for example:
➢ Payment and Cash Management 
➢ Payments Clearing and Settlement
➢ FI to FI Customer Credit Transfer (pacs.008)
Payment and Cash Management
Securities
Trade Services
Foreign Exchange
Card Payment
camt.052 Bank to Customer Account Report
camt.053 Bank to Customer Statement
camt.054 Bank to Customer Debit Credit Notification
camt.056 FI to FI Payment Cancellation Request
camt.057 Notification to Receive
pacs.002 FI to FI Payment Status Report
pacs.004 Payment Return
pacs.008 FI to FI Customer Credit Transfer
pacs.009 Financial Institution Credit Transfer
pain.001 Customer Credit Transfer initiation
pain.002 Customer Payment Status Report
pain.012 Creditor Payment Activation Request
Domain
Message
Definition
8

9
4!a . 3!c . 3!n . 2!n
Version
Variant
Message identifier/functionality
Business area
pacs.008.001.08
Version 8
Variant 1
FI To FI Customer 
Credit Transfer
Payments Clearing and 
Settlement
Example

Payment Initiation (pain) Payments Clearing & Settlement (pacs) Cash Management 
(camt)
Ultimate 
Debtor
Forwarding 
Agent
Debtor Initiating 
Party
:50a
Debtor 
Agent
:52a
1 2 3 1 2 3 1 2 3
Ultimate 
Creditor
Creditor
Previous Instructing 
Agents 
Instructing
Agent
Instructed
Agent
Creditor 
Agent
Reimbursement
Agents 
Intermediary
Agents 
:57a :59a
:72:/INS/ :53a :54a :55a :56a :72:/INTA/
Sender Receiver
10

11
<AppHdr> …
</AppHdr>
<Document> …
</Document>
ISO 20022
Business 
Application Header
ISO 20022
Message
Business
Message
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

relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example in a pacs.008 Customer Credit Transfer
the Interbank Settlement Date is a sub-element (Level 2) of the Credit Transfer Transaction Information element (Level 1).
Naming conventions
An XML element is named according to the following rules:
• The name can contain letters, numbers, and other characters, but must not start with a number or punctuation mark.
• The name must not start with XML, xml, or Xml.
• The name must not contain any spaces.
MX naming conventions
There are some generic naming rules that apply to most items in the database.
• The names of all items in the database use the upper CamelCase convention, as follows:
• Each word starts with a capital letter.
• There are no white spaces between words.
• A name may be made up of multiple words, each consisting of alphanumeric characters.
• Words use British English vocabulary.
• All names must start with an alphabetic character.
• All characters that follow the first characters must be letters or numbers.
Example of a Street Name element: <StrtNm>Oxford Street</StrtNm>
MX message element multiplicity (occurrences)
An MX message element specifies its cardinality (number of elements in a set) using minimum (min) & maximum (max) to describe the occurrences.
Required element
Optional element
Unlimited element occurrences
Element Multiplicity 
12

not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested
element.
A common example of this is in payment message is Financial Institution.
Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e.,
<FinInstnId></FinInstnId>
In the FINplus service Message Validation (MVal) will validate the messages to ensure empty XML elements are not provided. i.e., ensure where
business data should be provided within a nested element, it is provided.
13

Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing
the element in an XML naming convention.
For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment
Identification is an element below Credit Transfer Transaction Information.
Credit Transfer Transaction Info’ Payment Identification
In this way the CBPR+ User Hand Book uses three main icon to explain the relationships between element, by display the icon after the element
name.
To visualise an element which has nested elements beneath it
To visualise an element which has a choice associated with it i.e., a Code where a choice of which code can be determined
To visualise an element which is nested and has a choice associated with it. For example, an Identification where a choice must be
made between an Organisation Identification and a Private Identification element which is nested, but where both cannot be used
together.
14

https://www2.swift.com/mystandards/#/c/cbpr/landing
15

16
Many of the CBPRplus Usage
Guidelines have useful key principals
and additional information. These can
be expanded in MyStandards by clicking
on ‘show details’ in the middle of the
Usage Guideline description pane.

Guidelines guideline to recommend a best practice.
In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated
Usage Guideline (e.g. CBPR plus)
Within CBPR+ Usage Guideline specification the rules dedicate to CBPR+ are often described as:
Formal Rules which are validated on the network, these are identified by the word Rule appended to the rule
description. For example:
Textual Rules which are not validated on the network, these are identified by with the word TextualRule
appended to the rule description. For example:
Guideline Rules which provide recommended best practice, these are identified by the word Guideline
appended to the rule description. For example:
Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a 
CrossElementSimpleRule and a CrossElementComplexRule
17
Rule “CBPR_Party_Name_Any_BIC_FormalRule”
Rule “CBPR_Agent_Option_1_TextualRule”
Rule “CBPR_Purpose_Guideline”

18
• Type: String
• Max allowed size: 35 characters
• Structure:
o Must contain minimum A & B, optionally followed by 1 or more additional business context elements (C, D, …).
o Always ends with version element E (format “nn”, e.g., “01”)
o Each element is separated by a period “.”
o Length of each text element can vary up to max 10 characters. Total length, including periods, cannot exceed 35 chars.
o Consistency enforced by lightweight SWIFT review/registration: E.g., “ecb” to represent the ECB, not “eucb” 
o Lowercase alphanumerical characters only
C, D,…
1-10 chars
B 1 char 1 char
1-10 chars
E
2 chars
A
1-10 chars
1 char
Total max 35 char
In CBPR+ the Usage Identifier is captured within the Business Application Header, Business
Service element. More detail can be found in the dedicated Business Application Header chapter
of this document,

y gpy 
externalised from the message itself, enabling maintenance of the code list on a quarterly basis 
without requiring a new message version. 
Some data element may also be embedded in the message.
example of Charge Bearer in pacs.008 v8 
which uses embedded codes
example of Return Reason Information in 
pacs.004 v9 which uses externalised codes
Proprietary Codes may also be available for certain data elements. 
These are typically inherited from legacy formats and require 
definitions in user documentation as these are not captured in the 
baseline ISO 20022 standards
https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets
XLSX format is readable in MS Excel 19

---

