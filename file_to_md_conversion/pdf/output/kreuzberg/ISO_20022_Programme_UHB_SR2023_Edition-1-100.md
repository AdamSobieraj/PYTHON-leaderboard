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

• All party (agents and 
non-agents) Name and 
Address elements. 
• The Related Remittance 
Information element
• The Remittance 
Information (structured & 
unstructured) element
• The Email Address 
where included as part of 
a Proxy elements
• City of Birth and Province 
of Birth elements nested 
in Private Identification 
List of special characters: 
!#&%*=^_`{|}~";@[\] $ > <
Currency Codes only (3-
Characters, e.g. EUR)
!#&%*=^_`{|}~";@[\]$ >< 
into MT messages will be 
represented by a . (Full 
Stop)
which are defined (by data 
Type) as text are restricted 
to FIN X Characters: 
a-z A-Z 0-9 / - ? : ( ) . , ' + .
$
<
>
!
#
&
%
*
[ =
\
]
Note: While ISO 20022 base standards support non-Latin characters, CBPR+ will 
only support Latin characters in the initial service implementation.
20

data will not necessarily be passed in subsequent messages. 
➢ For example: the Instruction Identification element contains a reference 
meaningful to the party sending a message, subsequent messages in a payment 
transaction chain can expect the Instruction Identification to be replaced by a 
reference meaningful to the party sending that message leg. 
End-to-end refers to data passed throughout the transaction life cycle i.e. within a 
message from one party to the next and continued in subsequent messages.
➢ For example: the UETR element contains a Unique End-to-end Transaction 
Reference in accordance with the UUID version 4 standards. This same reference 
is used in all messages related to the payment transaction. 
21

Financial 
Institution 
Identification
BICFI
Clearing 
System 
Member Id
Clearing 
System Id
LEI
Name
Postal Address Various sub-element
ISO 20022 messages have a number of elements associated with Agents which allow for these
Agents to be referenced by a variety of Financial Institution identifiers.
More commonly the ISO 9362 Financial Institution BIC (BICFI) is considered the best practice de
facto standard for ‘many to many’ / correspondent banking payments. However other options
include:
Clearing System Member Identifiers when accompanied with the Clearing System Identification.
LEI (Legal Entity Identifier)
Name and either structured or unstructured Postal Address.
22
Back to previous page

23
CBPR+ usage guidelines DateTime elements mandate the time zone that the time 
represents as an offset against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
note - milliseconds are optional. 
10
The ISO 20022 Date elements allow the date to include an offset. As a data model, shared 
by other business domains, an offset date can provide great business clarify, such as 
something expiring at the end of a business date. However, in payments such a date offset 
provides little business value, whereby should an offset be include with the date, this offset 
should be ignored.

24
Austria Austrian Bankleitzahl AT ATBLZ 
Canada Canadian Payments Association Payment 
Routing Number 
CC CACPA 
China Bank Branch code used in China CN CNAPS
Germany German Bankleitzahl BL DEBLZ 
Greece Helenic Bank Identification Code GR GRBIC 
Hong Kong Hong Kong Bank Code HK HKNCC 
India Indian Financial System Code IN INFSC 
Ireland Irish National Clearing Code IE IENCC 
Italy Italian Domestic Identification Code IT ITNCC 
Japan Japan Zengin Clearing Code JP JPZGN
New Zealand New Zealand National Clearing Code NZ NZNCC 
Poland Polish National Clearing Code PL PLKNR 
Portugal Portuguese National Clearing Code PT PTNCC 
Russia Russian Central Bank Identification Code RU RUCBC 
South Africa South African National Clearing Code ZA ZANCC 
Spain Spanish Domestic Interbanking Code ES ESNCC 
Switzerland Swiss Clearing Code (BC Code) SW CHBCC 
Switzerland Swiss Clearing Code (SIC Code) SW CHSIC 
Taiwan Financial Institution Code TW TWNCC 
UK UK Domestic Sort Code SC GBDSC 
US CHIPS Participant Identifier CP USPID 
United States Routing Number FW USABA 
For translation rules and comparison
purposes this table provides a list of
published MT National Clearing
System codes again their equivalent
ISO 20022 Clearing System
Identification in the external code list.

25

gp
26
The Character Set element uses the UnicodeChartsCode string to declare an additional
character set, for example Cyrillic (Unicode range: 0400-04FF).
This allows the party for which the message is addressed To to know in advance the
additional character set contained within the Business Document. In this way the message
can be routed to a specific application to process the Character Set or handled as an
exception if the Character Set is not appropriate for that business transaction.
Character Set
Ж œ
ݒ 图
Extending character sets is not intended in CBPR+ from the initial implementation of the service.
This element is intended for use once extended character sets are implemented, whereby the
string represented in this element can enable any necessary network validations, such as a closed
user group for that character set.

(gp)ppy y p
this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.
From
27
A choice must be made for the BIC depending on the party it represents.
Financial Institution Identification which identifies a Financial Institution, and may
be further complemented with
• Clearing System Member Identification
• LEI
as an additional identification.
Organisation Identifier
Financial Institution Identifier

p(gp) ppy y 
captured within this nested element, where the BIC takes precedence should the information be inconsistent
with the BIC.
To
28
A choice must be made for the BIC depending on the party it represents.
Financial Institution Identification which identifies a Financial Institution, and may
be further complemented with
• Clearing System Member Identification
• LEI
as an additional identification.
Organisation Identifier
Financial Institution Identifier

pp 
match the Business Document to avoid incorrect routing by the recipient.
Business Message Identifier
29
Business Message
Identifier 1A245878.. 
Business
Application
Header
Business
Document
Message
Identification 1A245878..
Group Header

routing by the recipient.
Message Definition Identifier
30
Message Definition
Identifier pacs.009.001.08 
Business
Application
Header
Business
Document
Message
Identification <Document “pacs.009.001.08” >
Group Header

pg
For CBPR+ examples are provided below, these values may be used together with the Message Definition
Identifier to determine routing rules to specific applications without having to open the business document.
Business Service
31
Message Definition Identifier BusinessService Business Use Case
pacs.009.001.08 swift.cbprplus.cov.01 Financial Institution (Cover) Credit Transfer
pacs.009.001.08 swift.cbprplus.01 Serial Financial Institution Credit Transfer
pacs.008.001.08 swift.cbprplus.stp.01 STP Customer Credit Transfer
The Business Service is also intended to be incremented for the same message version, when an updated
Usage Guideline is released. For example a new restriction is applied to the pacs.009.001.08 Usage
Guideline, the Business Service swift.cbprplus.cov.02 and swift.cbprplus.02 will be used to reflect these
new Guidelines and allow network validate.
Note: when a new message (Message Definition Identifier) version is introduced the numeric value for the
Business Service is reset.
Take me to Message Name Identification overview

32
pain.008.001.03 sw ift.cbprplus.01
pacs.002.001.10 sw ift.cbprplus.02
pacs.003.001.08 sw ift.cbprplus.01
pacs.004.001.09 sw ift.cbprplus.02
pacs.008.001.08 sw ift.cbprplus.02
pacs.008.001.08 (STP/STP EU) sw ift.cbprplus.stp.02
pacs.009.001.08 (advice) sw ift.cbprplus.adv.02
pacs.009.001.08 (core) sw ift.cbprplus.02
pacs.009.001.08 (cov) sw ift.cbprplus.cov.02
pacs.010.001.03 sw ift.cbprplus.02
pacs.010.001.03 (Margin Collection) sw ift.cbprplus.col.01
camt.029.001.09 sw ift.cbprplus.02
camt.052.001.08 sw ift.cbprplus.02
camt.053.001.08 sw ift.cbprplus.02
camt.054.001.08 sw ift.cbprplus.02
camt.055.001.08 sw ift.cbprplus.01
camt.056.001.08 sw ift.cbprplus.02
camt.057.001.06 sw ift.cbprplus.02
The data represented in the Business Service, together with the
Message Definition Identifier has a number of roles, in addition to the
routing rules referred to on the previous page.
This data value:
▪ Identifiers explicitly the Usage Guideline within a library of
guideline. For example an application may have various pacs.008
libraries within a collection, for which only one of these is
appropriate to be used to identify data requirements or perform
validation.
• is also populated in the Request Header of the InterAct message
in the Request Sub Type element which allow the service
(FINplus for CBPR+) to apply network validation rules.
camt.107.001.01 sw ift.cbprplus.01
camt.108.001.01 sw ift.cbprplus.01
camt.109.001.01 sw ift.cbprplus.01

This element is currently not foreseen to be used by CBPR+.
Market Practice
33

pp
Creation Date
34
CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional.

gpy 
Copy Duplicate
35
COPY
DUPL
CODU
COPY is used to represent a copy of a message being sent to an additional party. This
scenario is only associated with camt reporting messages.
DUPL is used to represent a duplicate of a previously sent camt reporting message. To
receive a duplicate payment message, Interact message retrieval should be utilised.
CODU is used to represent a duplicate of a previously sent COPY message. This scenario
is only associated with camt reporting messages.
Where utilised in the Business Application Header of a camt message the content 
of this element should match the Copy Duplicate element within the camt message 
to avoid incorrect routing by the recipient.

py y p(gp) g
should perform necessary actions to avoid processing this Business Message again.
Possible Duplicate
36
This element is represented by a Yes/No Boolean, whereby true represent this is a
Possible Duplicate.
It is not necessary to represent false (No) the absence of this optional element itself
indicates that this is not considered a Possible Duplicate.
The FINplus Technical Header has an element PDIndicator(Possible Duplicate Indicator) which uses a 
Yes/No Boolean. This may be populated by the network interface to identify a message it considers may be 
a possible duplicate.

py y ppg
Priority
37
This element must represent the priority code of the business document (instance)
which is only applicable for pacs messages. The pacs message priority is captured
in the Payment Type Priority/Instruction Priority.

ppppy
Related Business Application Header from the original message can be included. This could allow the
receiver to apply specific routing to the message, based on the related information i.e., return of a pacs.009
cov may be routed to different payment engine than a core pacs.009.
Related
38
The following elements are nested within the Related element. Where used these
contain the original data from the related Business Application Header:
From
To
Business Message Identifier
Message Definition Identifier
Business Service
Creation Date
Copy Duplicate
Priority
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max 1

pain.002 – Interbank Customer Payment Status Report
pain.008 – Customer Direct Debit Initiation
39

Interbank Customer 
Credit Transfer Initiation
40

41
ISO MT
Group Header
➢ Message Identification
➢ Initiating Party – where different from Debtor
➢ Forwarding Agent 
Payment Information
➢ Payment Information Identification
➢ Requested Execution Date
➢ Debtor
➢ Debtor Agent
Credit Transfer Transaction Information
➢ Payment Identification 
➢ Amount
➢ Charge Bearer
➢ Creditor Agent
➢ Creditor
Sequence A – General Information:
➢ Sender’s Reference (Field 20)
➢ Instructing Party (Field 50 C or L)
Message Senderin a ‘relay’ scenario
Sequence A – General Information:
➢ Customer Specified Reference (Field 21R)
➢ Requested Execution Date (Field 30)
➢ Ordering Customer (Field 50 F, G or H)*
➢ Account Servicing Institution (Field 52 A or C)*
Sequence B – Transaction Details:
➢ Transaction Reference (Field 21)
➢ Currency/Transaction Amount (Field 32B)
➢ Details of Charges (Field 71A)
➢ Account With Institution (Field 57 A, C or D)
➢ Beneficiary (Field 59 no letter, A or F)
ISO 20022 message element MT Field Name & (Tag option)
*or in Sequence B – Transaction Detail

pain.001
Group Header
Payment 
Information
Credit Transfer 
Transaction 
Information Payment messages in a many-to-many payment are 
considered as a single transaction. 
The pain.001 message is composed of three blocks:
• Group Header contains a set of characteristics that relates 
to all individual transaction.
• Payment Information contains a set of characteristics that 
relates to the debit side of the transaction, such as Debtor 
and Debtor Agent.
• Credit Transfer Transaction Information contains, among 
others, elements related to the credit side of the transaction, 
such as Creditor and Creditor Agent.

FINplus pain.001
FINplus pain.002 pacs.008
pacs.002
F
A
B
FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to 
request movement of funds from the debtor account to a creditor. There are three common use cases: 
Relay: The pain.001 message is sent by the Initiating party (the Debtor or authorised party) to the Forwarding Agent which acts as a 
concentrating financial institution. It will forward the pain.001 message to the Debtor Agent
camt.053
Debtor Agent
1
Debtor
Noting in CGI–MP a pain.001 may also be sent by the Initiating Party/Debtor directly to the Debtor Agent which is outside of the scope of CBPR+, 
however the CBPR+ FINplus pain.001 message is interoperable with CGI-MP.
Creditor Agent Creditor Forwarding
Agent Initiating Party*
pain.001**
*Initiating Party may alternative represent an authorised party such as a head office 
**or other proprietary method for instructing a payment initiation request. 
pain.002
A Payment Initiation Rulebook, available in the Standards Documentation Centre, replaces the legacy MT 
Request for Transfer Service Level Agreement.

FINplus pain.001
FINplus pain.002 pacs.008
pacs.002
I A B
FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to 
request movement of funds from the debtor account to a creditor. There are three common use cases: 
Authorised Party Initiation: The pain.001 message is sent by the Financial Institution as an Initiating Party to the Debtor Agent to 
initiate a payment on behalf of the Debtor who is the account holder. For example, a FI Initiates; a liquidity sweep on behalf of a 
corporate customer or payment from the Debtor account based on Tri-party agreement (agreement from the Debtor with the Debtor 
Agent to provide authority that the Initiating Party is authorised to execute payments from their account) 
camt.053
Debtor Agent Initiating
Party
2
Debtor
Noting in CGI-MP a pain.001 may also be sent by the Initiating Party/Debtor directly to the Debtor Agent which is outside of the scope of CBPR+, 
however the CBPR+ FINplus pain.001 message is interoperable with CGI-MP. 
Creditor Agent Creditor
This use case may not apply to all Financial Institution, depending on the products and service 
provided by that Financial Institution to their customer

Interbank pain.001
pacs.008
Interbank pain.002
pacs.002
A B C
Interbank Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to 
request movement of funds from the debtor account to a creditor. There are three common use cases: 
Financial Institution Payment Initiation (to non-FI) : The pain.001 message is sent by the Financial Institution as both the Debtor 
and Initiating Party to initiate a payment from their account with the Debtor Agent to move funds to a non-Financial Institution Creditor
camt.053
3
Debtor Creditor Agent Creditor Initiating Party
I
pacs.008
pacs.002
Debtor Agent

46
Forwarding Agent - “Financial institution that receives the instruction from the initiating party and forwards it to the next 
agent in the payment chain for execution”. Applicable for pain.001 use case 1 only
Debtor Agent - “Financial institution servicing an account 
for the debtor.”
Initiating Party – “Party that initiates the payment.” which 
may be the Debtor or a Party acting on behalf of the 
Debtor e.g., the Agent initiating a liquidity sweep service
Debtor - “Party that owes an amount of money to the 
(ultimate) creditor.”
Creditor Agent - “Financial institution servicing an account 
for the creditor.”
Creditor - “Party to which an amount of money is due.”
Noting with the exception of the Forwarding Agent (which is only present in the ‘Relay’ use case) all of these Parties are applicable to each of the use 
case described in the high-level pain.001 Interbank Customer Credit Transfer Initiation serial message flow.

47

Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For the Payment Initiation (pain) messages the Message Identification has no exact equivalent
in the legacy MT payment message. However, the Sender’s Reference (Field 20) could be
considered as a similar comparison where a pain message contains a single Transaction.
For a relay scenario, Forwarding Agent should respect the Message ID provided 
by the Initiating Party (Debtor or authorized third party) of the pain.001.
Group Header Message Identification
Each transaction’s Credit Transfer Transaction Information contains a variety of nested 
Payment Identification elements to capture reference related to the individual transaction 
such as a UETR (Unique End-to-end Transaction Reference).
CGI

10
Group Header Creation Date Time
It is defined by ISO Date Time with mandatory date and time components expressed 
in the following formats:
1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
3. Local time format YYYY-MM-DDThh:mm:ss.sss
Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in
defining the date and time elements. The most recommended representation is Local time
with UTC offset which was mandated by CBPR+ (2nd option). Otherwise use UTC time
(1st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

Group Header Authorisation
For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for 
Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.
or Transaction Level approval by additional security provisions, such as digital signature or user key. The
Authorisation uses an embedded code set or free text form. It has no exact equivalent in the legacy MT
payment message, however, the Authorisation (Field 25) could be considered as a similar comparison.
Code Description Description
ILEV Instruction Level Authorisation File requires all customer transactions to be authorised or approved.
FDET File Level Authorisation Details Additional file level approval, with the ability to view both the payment information block 
and supporting transaction detail.
FSUM File Level Authorisation Summary Additional file level approval, with the ability to view only the payment information block.
AUTH PreAuthorised File File has been pre-authorised or approved within the originating customer environment 
and no further approval is required.

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 
Group Header Number of Transactions
51
contained within the message.
Single transactions in the CBPR+ payment usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant payments, supporting the next
generation of innovation.

The Initiating Party can either be the Debtor or an Authorised Party who initiates
payment transactions on behalf of the Debtor. The Initiating Party can be, for
example, the Head Office which has the authority to debit the account of its
subsidiary. In the centralization model, the Initiating Party can also be a payment
factory or shared service center or third-party agent, which has authority to send the
message on behalf of the Debtor.
There are three common use cases in the context of interbank pain.001 message:
1. Relay: The Initiating Party, which is either the Debtor themselves or authorised
party, sends the pain.001 message to the Forwarding Agent which acts as a
concentrating financial institution. It will forward the pain.001 message to the
Debtor Agent. This is commonly known as a relay scenario. Whereby the
Forwarding Agent is performing a technical role in the payment transaction, they
would not be represented in the payment, clearing and settlement message.
2. Authorised Party: The Initiating Party is the Financial Institution which has the
authority to send the pain.001 message on behalf of the Debtor, e.g., multi-bank
liquidity sweeps.
3. Financial Institution Payment Initiation: The Initiating Party is the Financial
Institution which is the Debtor who initiate a payment from their account to move
funds to a non-Financial Institution Creditor
52
For the second and the 
third use case, BIC of the 
Initiating Party is required. 
Group Header Initiating Party
Forwarding Agent / FI
Initiating Party
Debtor Authorised Party

Sub elements describe the Initiating Party in greater detail. 
Address is provided. 
Identification
Nested element capturing the 
various types of identifiers, e.g., 
BIC, LEI etc. BIC is mandatory 
for anAuthorised Party initiation 
and FI payment initiation.
Country of 
Residence
Optional element to 
capture the Initiating 
Party’s ISO country code 
of residence 
Postal 
Address
Nested element capturing 
structured Postal Address 
including at least Town Name and 
Country if used.
53
Initiating 
Party
Contact 
Details
Optional contact details
Group Header Initiating Party

Debtor or authorised third party) has to provide Business Identifier Code (BIC FI) of the 
Forwarding Agent in the original pain.001 message. The Forwarding Agent acts as a 
concentrating financial institution and forwards the pain.001 message to the Debtor Agent for 
execution.
Other options to identify the Forwarding Agent
include:
• Clearing System Member ID
• LEI (Legal Entity Identifier)
Group Header Forwarding Agent
For the use cases of Authorised Party initiation and FI payment initiation, Forwarding 
Agent is not required.
Financial 
Institution 
Identification
BICFI
Clearing 
System 
Member Id
Clearing 
System Id
LEI
Various sub-element

55

56
ppg
be captured as both structured and unstructured (address line) data, of which the Country Code within the
Postal Address is mandatory.
As a payment initiation could instruct various types of Payment Methods settled across various Clearing
Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be
adhered to, which may need some enrichment or repair of the data from the payment initiation message.
Postal Address is a good example of such data enrichment or repair, where many domestic payment methods
exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured
and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used.
Structured Unstructured
Structured Unstructured
CGI-MP payment Initiation/
CBPR+ payment initiation interbank
CBPR+ payments
HVPS+ payments
Many domestic proprietary 
payments
or
Unstructured
pain.001

This 35 character identifier is a point-to-point reference used to unambiguously 
identify the payment information group within the message. It is also known as a 
batch reference number if the message contains multiple transactions. 
Payment Information Payment Information Identification
For single transactions in the CBPR+ usage guidelines, the value in Payment Information 
Identification is the same as the Message Identification of the Group Header. 
y y py

amount of money. One of the following payment method codes must be used: 
Code Name Definition
CHK Cheque Written order to a bank to pay a certain amount of 
money from one person to another person.
TRF Credit Transfer Transfer of an amount of money in the books of the 
account servicer.
Payment Information Payment Method

Anested element which may either use an external ISO Service Level
code or a proprietary code. It is used to identify a particular agreed
service level which should be applied to the payment. Where a
service level is not agreed, it may be ignored.
Payment
Type 
Information
Anested element which may either use an external ISO
Local Instrument code or a proprietary code. It can be
used in combination with Service Level to identify the
type of local instrument. For example, INST – Instant
Credit Transfer forSEPAService Level.
Anested element which may either use an external ISO Category Purpose code or
a proprietary code. It is used to identify the category of payment. For example, DIVI
is the payment of dividends.
i
Instruction 
Priority 
Service
Level 
Local 
Instrument 
Category 
Purpose 
Payment Information Payment Type Information
Min 0 – Max 3
Min 0 – Max 1
Note: the ISO instrument codes are registered by
specific community group (captured in the code list)
Min 0 – Max 1
A choice of 
imbedded codes 
representing the 
urgency 
considered by the 
instructing party. 
This point-to-point 
information may 
be used by the 
instructed party to 
differentiate the 
processing 
priority. 
Min 0 – Max 1
Payment Type Information at Payment Information Level and Transaction Level is mutually 
exclusive. It should be used at the Transaction Level unless bilaterally determined.

It is the date on which the debtor’s account is debited. If payment by cheque, the date when 
the cheque must be generated by the bank. It is defined by either ISO Date expressed in 
the YYYY-MM-DD format or ISO Date Time below:
1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
3. Local time format YYYY-MM-DDThh:mm:ss.sss
10
Payment Information Requested Execution Date
which the initiating party requests the clearing agent to process the payment. 
Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in
defining the date and time elements. The most recommended representation is Local time
with UTC offset which was mandated by CBPR+ (2nd option). Otherwise use UTC time
(1
st option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

It is defined by ISO Date expressed in the YYYY-MM-DD format
10
Payment Information Pooling Adjustment Date
date of a cash pool movement that has been posted with a different value date. 
This element is not widely used in the payment industry. For
the use case of interbank, it is even less likely to be utilized.

The Debtor sub elements describe the Debtor in greater detail.
Debtor
Identification Nested element capturing the 
various types of identifiers for 
the party e.g. BIC, LEI etc.
Country of 
Residence
Optional element to 
capture the Debtor’s ISO 
country code of residence 
Postal 
Address
Nested element capturing either 
structured or unstructured Debtor
address details. 
Payment Information Debtor
Note: Structured address is
strongly recommended with
mandatory Town Name and
Country
In order to process the pain.001 interbank into a CBPR+ payment, CBPR+ 
requires either structured or unstructured postal address.
Take me to an explanation of CGI Postal Address

63
made as a result of the transaction, which will be also reflected in their account Statement.
The Debtor Account uses a variety of nested elements to capture information related to 
the account.
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account, recommended.
Name identifies the name of the account as assigned by the Debtor Agent (Account
Servicing Institution)
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Indication of Currency of the Debtor Account is recommended in case of multi-currency 
accounts whereby a single account number is allocated to the Debtor Account. 
Payment Information Debtor Account
CGI
63

relationship with their customers, the Debtor. 
Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the
pain messages, the description of these parties change in the reporting messages (camt) where the
Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor
become the Statement Account Owner. This will be explored further in the camt Cash Management
Reporting section.
64
For Agent Identification, BIC is preferred, alternatively Clearing Member 
ID together with Name and Address may be provided. 
Payment Information Debtor Agent

65
Agent. 
The Debtor Agent Account uses a variety of nested elements to capture information 
related to the account.
Min 1 – Max 1 Identificationidentifies the account maintained at theAccount Servicing Institution
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account
Name identifies the name of the account as assigned by theAccount Servicing Institution
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element is
used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Debtor Agent and Creditor Agent are Financial Institutions, therefore
the nested elements Name and Proxy are unlikely to be used.
Payment Information Debtor Agent Account

related to the processing of the payment.
The Instruction for Debtor Agent element offers a maximum of 140 characters to 
further information related to the processing of the payment instruction, that may need to 
be acted upon by the Debtor Agent, depending on bilateral agreement. 
66
Payment Information Instruction For Debtor Agent

The Ultimate Debtor element should not be confused with an Initiating
Party who may send a payment initiation request on behalf of the Debtor,
for example, Payment Factory.
CBPR+ premise is that an Ultimate Debtor has no financial regulated direct
account relationship with the corresponding Debtor. Likewise, an Ultimate
Creditor has no financial regulated account relationship with the
corresponding Creditor.
Party
Ultimate
Creditor
Ultimate
Debtor
The Ultimate Debtor and Ultimate Creditor can be identified by a combination of Name and structured 
address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.
Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ 
interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction 
Level unless bilaterally determined. 
67
Payment Information Ultimate Debtor

py pypy gpg 
payment transaction. This element is comparable with MT Field 71A ‘Details of Charges’
71A: Details 
of Charges 
Code Description
BEN Beneficiary
OUR Our Customer Charges
SHA Shared Charges
Charge 
Bearer
(0.1)
Code Description
CRED Creditor
DEBT Debtor
SHAR Shared
68
Charge Bearer at the Payment Information Level and the Transaction Level is mutually 
exclusive. It should be used at the Transaction Level unless bilaterally determined. 
Payment Information Charges Account

Charges account should be used when charges have to be booked to an account different 
from the account identified in debtor's account.
Payment Information Charges Account
transaction.
This element is not widely used in the payment industry.

Charges account agent should only be used when the charges account agent is different 
from the debtor agent.
Payment Information Charges Account Agent
charges account.
This element is not widely used in the payment industry. It should also be noted that the
ChargesAccountAgentRule inherited from the base message should be ignored as the optional
Branch of DebtorAgent is removed from this Usage Guideline.

71

a point-to-point reference of 35 characters long will be returned
to account statements if provided by the initiating party.
an end-to-end reference provided by the Debtor which
must be passed unchanged throughout the payment and
reported to the Creditor.
note: if the Debtor has not provide an end-to-end identifier, the
Debtor Agent may populate “NOTPROVIDED” to comply the
mandatory need of this element.
the Unique End-to-end Transaction Reference created using the
UUID v4 standard. This reference must be passed unchanged
throughout the payment, it may also be created by the Debtor within
their Payment Initiation request, and also included in reporting
messages.
Payment
Identification
$
Instruction
Identification
pyy 
End to End
Identification
UETR
Note: Instruction Id is mandatory in other CBPR+ messages as it
maps directly with the mandatory Sender’s Reference (Field 20)
of the legacy MT payment messages.
Min 0 – Max 1
Min 1 – Max 1
Min 1 – Max 1
72
Payment Identification
Credit Transfer Transaction Information

Anested element which may either use an external ISO Service Level
code or a proprietary code. It is used to identify a particular agreed
service level which should be applied to the payment. Where a
service level is not agreed, it may be ignored.
Payment
Type 
Information
A nested element which may either use an external ISO
Local Instrument code or a proprietary code. It can be
used in combination with Service Level to identify the
type of local instrument. For example, INST – Instant
Credit Transfer forSEPA Service Level.
Anested element which may either use an external ISO Category Purpose code or
a proprietary code. It is used to identify the category of payment. For example, DIVI
is the payment of dividends.
i
Instruction 
Priority 
Service
Level 
Local 
Instrument 
Category 
Purpose 
Min 0 – Max 3
Min 0 – Max 1 Note: the ISO instrument codes are registered by
specific community group (captured in the code list)
Min 0 – Max 1
A choice of 
imbedded codes 
representing the 
urgency 
considered by the 
instructing party. 
This point-to-point 
information may 
be used by the 
instructed party to 
differentiate the 
processing 
priority. 
Min 0 – Max 1
Payment Type Information at the Payment Information Level and Transaction Level is 
mutually exclusive. It should be used at the Transaction Level unless bilaterally determined. 
CGI
Payment Type Information
Credit Transfer Transaction Information

The Instructed Amount captures currency and amount of money to be moved
between the Debtor and Creditor, before deduction of charges, expressed in the
currency as ordered by the initiating party. This amount has to be transported
unchanged through the transaction chain. This element is comparable with the
legacy Field 33B.
py 
Instructed
Amount
Equivalent
Amount
The Equivalent Amount nested element captures currency and Amount of
money to be moved between the Debtor and Creditor, before deduction of
charges, and is expressed in the currency of the Debtor's account. The
Currency Of Transfer element capture the equivalent currency to be
transferred which the first agent will convert the credit transfer into.
Instructed Amount
Equivalent Amount
£
$
¥
Credit Transfer Transaction Information Currency and Amount

The factor used for conversion of an amount from one
currency to another. This reflects the price at which one
currency was bought with another currency.
Specifies the type used to complete the currency
exchange, such as SPOT, SALE or AGRD (Agreed).
Exchange
Rate 
Information
Unit 
Currency
Exchange 
Rate
Rate Type
Contract 
Identification
Currency in which the rate of exchange is expressed in a currency 
exchange. For example, 1GBP = xxxCUR, the unit currency is GBP.
Unique and unambiguous reference to the foreign
exchange contract agreed between the Initiating
Party/Debtor and the Debtor Agent.
Exchange Rate Information
Credit Transfer Transaction Information

py pypy gpg 
payment transaction. This element is comparable with MT Field 71A ‘Details of Charges’
71A: Details 
of Charges 
Code Description
BEN Beneficiary
OUR Our Customer Charges
SHA Shared Charges
Charge 
Bearer
(0.1)
Code Description
CRED Creditor
DEBT Debtor
SHAR Shared
76
Charge Bearer at the Payment Information Level and the Transaction Level is 
mutually exclusive. It should be used at the Transaction Level unless bilaterally 
determined. 
Charge Bearer
Credit Transfer Transaction Information

77
Cheque
Type
Code Description
Bank 
Cheque
BCHQ Cheque drawn on the account of the debtor's financial institution, which is debited 
on the debtor's account when the cheque is issued. These cheques are printed by 
the debtor's financial institution and payment is guaranteed by the financial 
institution. Synonym is 'cashier's cheque'.
Customer 
Cheque
CCHQ Cheque drawn on the account of the debtor and debited on the debtor's account 
when the cheque is cashed. Synonym is 'corporate cheque'.
Draft DRFT A guaranteed bank cheque with a future value date (do not pay before], which in 
commercial terms is a 'negotiatable instrument': the beneficiary can receive early 
payment from any bank under subtraction of a discount. The ordering customer's 
account is debited on value date.
ypqy 
The Delivery Method element specifies the method to be used in delivering the cheque by the Debtor Agent. 
For example, a code CRCD is used to courier the cheque to the Creditor. 
12,000
Cheque Instruction
Credit Transfer Transaction Information

The Ultimate Debtor element should not be confused with an Initiating
Party who may send a payment initiation request on behalf of the Debtor,
for example, Payment Factory.
CBPR+ premise is that an Ultimate Debtor has no financial regulated direct
account relationship with the corresponding Debtor. Likewise, an Ultimate
Creditor has no financial regulated account relationship with the
corresponding Creditor.
Party
Ultimate
Creditor
Ultimate
Debtor
The Ultimate Debtor and Ultimate Creditor can be identified by a combination of Name and structured 
address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.
Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ 
interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction 
Level unless bilaterally determined. 
78
Ultimate Debtor
Credit Transfer Transaction Information

• If more than one intermediary agent is present, then Intermediary Agent 1 identifies the 
agent between the Debtor Agent and the Intermediary Agent 2. 
• If more than two intermediary agents are present, then Intermediary Agent 2 identifies the 
agent between the Intermediary Agent 1 and the Intermediary Agent 3. 
• If Intermediary Agent 3 is present, then it identifies the agent between the Intermediary 
Agent 2 and the Creditor Agent. 
More commonly the ISO 9362 Financial Institution Business Identifier Code is considered the 
best practice de factor standard for ‘many to many’ / correspondent banking payments. 
Other options to identify the Intermediary Agent
include:
• Clearing System Member ID
• LEI (Legal Entity Identifier)
• Name and either structured, or unstructured 
Postal Address
1
2
3
79
Intermediary Agent 1
Credit Transfer Transaction Information
Intermediary Agent 2
Intermediary Agent 3
In order to process the pain.001 interbank into a CBPR+ payment, CBPR+ 
requires either structured or unstructured postal address.
Take me to an explanation of CGI Postal Address

80
related to these Agents. 
The Intermediary Agent Account uses a variety of nested elements to capture 
information related to the account.
Min 1 – Max 1 Identificationidentifies the account maintained at theAccount Servicing Institution.
Type uses the external CashAccount Type code list to identify the type of account.
Currency identifies the currency of the account.
Name identifies the name of the account as assigned by theAccount Servicing Institution.
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element is
used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Intermediary Agent is a Financial Institution, therefore the nested
elements Name and Proxy are unlikely to be used.
Intermediary Agent Account 1
Credit Transfer Transaction Information
Intermediary Agent Account 2
Intermediary Agent Account 3

relationship with their customers, the Creditor. 
Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the
pain messages, the description of these parties change in the reporting messages (camt) where the
Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor
become the Statement Account Owner. This will be explored further in the camt Cash Management
Reporting section.
81
Creditor Agent
Credit Transfer Transaction Information
For Agent Identification, BIC is preferred, alternatively Clearing Member 
ID together with Name and Address may be provided.

82
The Creditor Agent Account uses a variety of nested elements to capture information 
related to the account.
Min 1 – Max 1 Identificationidentifies the account maintained at theAccount Servicing Institution
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account
Name identifies the name of the account as assigned by theAccount Servicing Institution
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element is
used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Debtor Agent and Creditor Agent are Financial Institutions, therefore
the nested elements Name and Proxy are unlikely to be used. Creditor Agent Account
Credit Transfer Transaction Information

elements describe the Creditor in greater detail.
Creditor
Identification Nested element capturing the 
various types of identifiers for 
the party e.g. BIC, LEI etc.
Country of 
Residence
Optional element to 
capture the Creditor’s ISO 
country code of residence 
Postal 
Address
Nested element capturing either 
structured or unstructured Creditor
address details. 
Note: Structured address is
strongly recommended with
mandatory Town Name and
Country
Credit Transfer Transaction Information
Creditor
In order to process the pain.001 interbank into a CBPR+ payment, CBPR+ 
requires either structured or unstructured postal address.
Take me to an explanation of CGI Postal Address

made as a result of the transaction, which will be also reflected in their account Statement.
The Creditor Account uses a variety of nested elements to capture information related to 
the account.
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account
Name identifies the name of the account as assigned by the Creditor Agent (Account
Servicing Institution)
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Creditor Account is not required for cheque payments.
84
Creditor Account
Credit Transfer Transaction Information

The Ultimate Debtor element should not be confused with an Initiating
Party who may send a payment initiation request on behalf of the Debtor,
for example, Payment Factory.
CBPR+ premise is that an Ultimate Debtor has no financial regulated direct
account relationship with the corresponding Debtor. Likewise, an Ultimate
Creditor has no financial regulated account relationship with the
corresponding Creditor.
Ultimate
Party
Ultimate
Creditor
Ultimate
Debtor
The Ultimate Debtor and Ultimate Creditor can be identified by a combination of Name and structured 
address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.
85
Credit Transfer Transaction Information
Ultimate Creditor

The Instruction for Creditor Agent element offers a multiplicity of up to 2 occurrences of 
information. This element enables:
➢ the use of an embedded choice of code to describe the instruction (e.g. CHQB – Pay
Creditor by Cheque)
➢ free format instruction information
➢ or both, where the free format complements the code.
The use of this element may be bilaterally agreed with the Creditor Agent. It must be passed 
on throughout the life cycle of the transaction until the payment reaches the Credit Agent.
Instruction for Creditor Agent
Credit Transfer Transaction Information
Note that usage of these codes may trigger non-STP with potential 
additional costs involved or potential rejects of payments. 86

ISO 20022 Programme
Quality data, quality payments
CBPR+ User Handbook
SR 2023 Edition
March 2023

related to the processing of the payment.
The Instruction for Debtor Agent element offers a maximum of 140 characters to 
further information related to the processing of the payment instruction, that may need to 
be acted upon by the Debtor Agent, depending on bilateral agreement. 
88
Credit Transfer Transaction Information
Instruction for Debtor Agent

The purpose is used to capture the nature of the payment, e.g., IVPT Invoice Payment, FEES Payment of
Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is
typically defined by the Debtor.
The externalised Purpose code set is classified by the purpose, for example commercial, for 
which the numerous codes within the classification are each described by Name and 
Definition.
For example, LIMAis classified within the Cash Management categorisation, with the Name
Liquidity Management described as a Bank initiated account transfer to support zero target 
balance management, pooling or sweeping.
Category Purpose also captures a high-level purpose, which unlike Purpose is less granular but can
trigger special processing e.g., Category Purpose code SALA ‘Salary Payment’ may trigger a reporting
process which restricts sensitive data i.e., individual salary names.
89
Credit Transfer Transaction Information
Purpose

The Debit Credit Reporting Indicator utilises an embedded choice 
of code to indicate whether the regulatory reporting applies to the:
• DEBT (debit) 
• CRED (credit)
• BOTH
The Authority element captures the Name and Country code of the 
Authority/Entity requiring the regulatory reporting information.
The Details element provides the detail on the regulatory reporting 
information.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max *
Credit Transfer Transaction Information Regulatory Reporting
Debit Credit Reporting Indicator
Authority
Details
90

when tax information is used by the clearing or the local regulatory authority(s). 
Tax information block is also available within the Structured Remittance Information block which is applicable 
when tax information is used by the creditor as part of remittance information.
Credit Transfer Transaction Information
Tax
This element caters for two main types of tax related payments: 
• Tax payment obligation that is required to be transmitted with a payment
• Information that accompanies an actual payment of a tax obligation
The follow nested elements may be used to capture detailed tax information:
Debtor
Min 0 – Max 1
Administration
Zone
Min 0 – Max 1
Reference
Number
Min 0 – Max 1
Method
Min 0 – Max 1
Creditor
Min 0 – Max 1
Total
Taxable
Base Amount
Min 0 – Max 1
Date
Min 0 – Max 1
Total Tax 
Amount
Min 0 – Max 1
Sequence
Number
Min 0 – Max 1
Record
Min 0 – Max *
91

The Remittance Identification captures a unique reference assigned by the initiating party of the payment 
to identify the remittance information sent separately from the payment instruction.
The Remittance Location Details uses a set of nested elements to provide information on either the 
location of or the delivery of remittance information. 
• Method requires a code from an embedded list to detail the method used to deliver the remittance 
advise information e.g. EMAL (email)
• Electronic Address provides an electronic address for which an agent is to send the remittance 
information to e.g. the email address. It may also reference a URL where remittance information 
may be deposited or retrieved.
• Postal Address provides the postal address to which an agent is to send the remittance information
Unlike CBPR+ pacs messages, in the interbank pain.001 message, Related Remittance Information and 
Remittance Information are non-mutually exclusive due to a corporate use case of populating both information 
blocks for detailing remittance advices which are part of value-added service offered by the Debtor Agent.
Min 0 – Max 1
Min 0 – Max *
SCORE Guideline: If the Related Remittance Information is used, and a Remittance Identification is 
provided, it is recommended that the Remittance Identification equal the End To End Identification. 
Credit Transfer Transaction Information
Related Remittance Information
92

y
Remittance Information enables the matching/reconciliation of an entry that the payment is intended to settle.
The Unstructured sub element captures free format Remittance Information which is 
restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the 
legacy MT message during coexistence. 
The Structured element is nested capturing rich structured Remittance Information, and is 
unlimited in its multiplicity, but must not exceed 9,000 characters of business information 
(does not include the xml element identification)
The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-to-end transportation of this data.
Min 0 – Max 1
Min 0 – Max *
Recommend to refer to CGI-MP Document Centre for Country 
requirements on Remittance Information.
Credit Transfer Transaction Information
Remittance Information
Structured
Unstructured
93

Structured <Strd>
Reference Document 
Information
<Rf rdDocInf>
Type <Tp>
Code Or Proprietary <CdOrPrtry >
Code <Cd> CINV
Number <Nb> A0000101
Related Date <Dt> 2019-10-29
In this example Referred Document
Information and its nested elements have
multiplicity which support up to 9,000
character of information. Whereby this
element can be repeated to include more
coded information such as another invoice.
element names
xml tag
business 
information
example of Structured invoice information
The Creditor Remittance Information is provided to
the Creditor in the Cash Management Reporting
messages’ Remittance Information component, for
example, the camt.053 Bank to Customer Statement.
Remittance Information
Structured
Credit Transfer Transaction Information
94

Information component of the pain.001. 
Creditor Reference in the Structured Remittance Information is based on ISO 11649
• 2 letters “RF”
• 2 digits check digit
• 21 letters/digits creditor reference
Facilitates STP and auto-match with the creditor reference and its account receivable
• A vendor can add the creditor reference to its invoice. When a customer pays the invoice, they write the creditor 
reference instead of the invoice number in the payment message (e.g., MT 101 F70 which will be carried in MT 
103) 
• When the vendor receives the payment, it can auto-match the incoming credit entry and the creditor reference 
extracted from the statement (e.g., MT 940 F61/86) 
ISO 20022 Programme 2021 Corporate Work Group Confidentiality: Restricted
SCORE Guideline: For Creditor Reference information, in instances where the 
Creditor Reference Type code is SCOR (Structured Communication Reference) 
and the Creditor Reference is structured in accordance with ISO 11649, the 
Issuer should be specified with the text ‘ISO’ (without the quote marks)
Remittance Information
Structured
Credit Transfer Transaction Information
95

g
Interbank Customer Credit Transfer Initiation - Relay 
Use Case pn.1.1.1 – High Level Payment Initiation Interbank ‘relay’ (pain.001)
Use Case pn.1.1.1.a – High Level Payment Initiation Interbank ‘relay’ (pain.001) Multi-bank Sweep 
Use Case pn.1.1.2 – High Level Payment Initiation Interbank ‘relay’ (pain.001) involving a Payment Market Infrastructure
Interbank Customer Credit Transfer Initiation – Authorised Party
Use Case pn.1.2.1 – High Level Payment Initiation Interbank (pain.001) by an Authorised Party
Use Case pn.1.2.1.a. – High Level Payment Initiation Interbank (pain.001) FI-Initiated Sweep (Long position at the Secondary Account)
Use Case pn.1.2.1.b. – High Level Payment Initiation Interbank (pain.001) by an Authorised Party to pay themselves as the Creditor
Interbank Customer Credit Transfer Initiation – Financial Institution 
Use Case pn.1.3.1 – High Level Payment Initiation Interbank (pain.001) Financial Institution Payment Initiation
96

camt.053
1
1
Initiating Party sends a 
payment instruction to the 
Forwarding Agent
Forwarding Agent (F) forwards 
the payment instruction to the 
Debtor Agent (A)
2
Debtor Agent (A) provides a 
status update ACSP (accepted 
settlement in progress) to the 
Forwarding Agent (F), based 
upon a bilateral agreement
pacs.008
Forwarding Agent (F) relays the 
status ACSP (accepted settlement 
in progress) to the Initiating Party, 
based upon a bilateral agreement
will debit the account of the Debtor and initiate a credit transfer.
F A B
97
Interbank pain.001
Interbank pain.002
1
pain.001
pain.002
Creditor Agent (B) processes the 
payment and sends the statement to 
Creditor
Debtor Agent (A) debits the 
account of Debtor and 
initiates a credit transfer by 
forwarding a local credit 
transfer message pacs.008
2 3
3
4
4
3b 3a
3a
3b

camt.053
1
1
Initiating Party sends a payment 
instruction to the Forwarding 
Agent to sweep excess funds 
from its subsidiary’s account to 
the master account with Bank B
Forwarding Agent (F) forwards 
the payment instruction to the 
Debtor Agent (A)
2 Debtor Agent (A) provides a 
status update ACSP (accepted 
settlement in progress) to the 
Forwarding Agent (F), based 
upon a bilateral agreement
pacs.008
Forwarding Agent (F) relays the 
status ACSP (accepted settlement 
in progress) to the Initiating Party, 
based upon a bilateral agreement
in this case to sweep excess cash from the account of the Debtor and consolidate cash for a Corporate.
A
F B
98
Interbank pain.001
Interbank pain.002
1
pain.001
pain.002
Creditor Agent (B) processes the 
payment and notifies Creditor of a 
successful sweep through the 
statement
Debtor Agent (A) debits the 
account of Debtor and 
initiates a credit transfer by 
forwarding a local credit 
transfer message pacs.008
2 3
3
4
4
3b 3a
3a
3b

1
pacs.008
will debit the account of the Debtor initiate a credit transfer through a Payment Market Infrastructure.
F A B
99
Interbank pain.001
Interbank pain.002
1
pain.001
pain.002
Creditor Agent (B) receives local 
credit transfer message via the 
Payment Market Infrastructure 
(PMI) and credits the Creditor
pacs.008
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
1
Initiating Party sends a 
payment instruction to the 
Forwarding Agent
Forwarding Agent (F) forwards 
the payment instruction to the 
Debtor Agent (A)
2
2
Debtor Agent (A) provides a status 
update ACSP (accepted settlement 
in progress) to the Forwarding 
Agent (F), based upon a bilateral 
agreement
Debtor Agent (A) debits the account 
of Debtor and initiates a credit 
transfer by forwarding a local credit 
transfer message pacs.008 to a 
Payment Market Infrastructure 
(PMI)
Forwarding Agent (F) relays the 
status ACSP (accepted settlement 
in progress) to the Initiating Party, 
based upon a bilateral agreement
3
3
4
4
3a 3b
3a
3b

As a pre-requisite the Debtor 
provides Debit Authorisation to 
Agent A, which allows Agent I 
to Initiate Payment from their 
account
pacs.008
account based on Debit Authorisation already in place between the Debtor and the Debtor Agent
I B
100
Interbank pain.001
Interbank pain.002
2
3a
Agent (I) initiates a payment 
request (pain.001) to the Debtor 
Agent (A) to move fund from the 
Debtor’s account, as an 
authorised party.
camt.053
Debit 
Authorisation
A pacs.002
DA 4
4
2
3
Debtor Agent (A) optionally provides a 
status update to the Initiating Party 
(Agent I), based upon a bilateral 
agreement
Debtor Agent (A) debits the account of 
Debtor and initiates a credit transfer
3
3a
DA
Creditor Agent (B) receives the credit 
transfer message, credits the Creditor, and 
sends a camt.053 (statement) at the end of 
the business day to the Creditor. An optional 
status report is sent to the previous Agent 
based upon a bilateral agreement

head.001 The head.001 services This element Business Business on the SWIFT is currently Application Application network. not foreseen Header Header to be used – Market Market by CBPR+. Min 0 – Max 1 Practice Practice element is used to identify administered 
Market Practice 
  33

pain.001 pain.002 Payment - Interbank – Interbank Initiation Customer Customer - Messages Credit Transfer Payment index initiation Status Report U
pain.008 -Customer Direct Debit Initiation 
    39

 and the Creditor Issuer should Reference be specified is with structured the text ‘ISO’ in accordance with (without the ISO 11649, quote marks) the Remittance Information Structured 
ISO 20022 Programme 2021 Corporate Work Group Confidentiality: Restricted 95

---

