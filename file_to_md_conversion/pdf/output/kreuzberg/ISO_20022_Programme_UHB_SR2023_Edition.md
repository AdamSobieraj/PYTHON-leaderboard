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

Agent I receives intraday 
balance report from Debtor 
Agent (A) on behalf of their 
mutual customer.
pacs.008
Agent to sweep excess cash from the account of the Debtor and consolidate the cash for a Corporate.
I B
101
Interbank pain.001
Interbank pain.002
2
3a
camt.052
Agent (I) initiates a sweep on 
behalf of the Corporate by 
sending pain.001 to the Debtor 
Agent
camt.053
Sweep 
Contract
A pacs.002
1
1
4
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
See use case p.8.1.2 for a sweeping contract with 
a short position
Creditor Agent (B) receives credit transfer 
message, credits the Creditor, and sends 
a camt.053 (statement) at the end of the 
business day to the Creditor. An optional 
status report is sent to the previous Agent 
based upon a bilateral agreement

As a pre-requisite the Debtor 
provides Debit Authorisation to 
Agent I to Initiate Payment from their 
account with the Debtor Agent (A)
pacs.008
account based on Debit Authorisation already in place to move money to themselves as the Creditor
I B
102
Interbank pain.001
Interbank pain.002
2
3a
Agent (I) initiates a payment request 
(pain.001) to the Debtor Agent (A) to 
move fund from the Debtor’s 
account, as an authorised party, to 
themselves as the Creditor
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
Creditor Agent (B) receives the credit transfer 
message, credits the Creditor, and sends a 
camt.053 (statement) at the end of the 
business day to the Creditor. An optional 
status report is sent to the previous Agent 
based upon a bilateral agreement
DA
I

pacs.008
funds to a nonFinancial Institution Creditor
I B
103
Interbank pain.001
Interbank pain.002
1
2a
Agent (I), the Debtor, initiates a 
payment request (pain.001) to 
the Debtor Agent (A) to move 
funds from their own account
camt.053
A pacs.002
3
3
1
2
Debtor Agent (A) optionally provides a 
status update to the Initiating Party 
(Agent I), based upon a bilateral 
agreement
Debtor Agent (A) debits the account of 
Agent (I), the Debtor and initiates a 
credit transfer
2
2a
Creditor Agent (B) receives credit 
transfer message, credits the Creditor, 
and sends the camt.053 (statement) at 
the end of the business day to the non-FI Creditor. An optional status report is 
sent to the previous Agent based upon a 
bilateral agreement

104
Interbank Customer 
Payment Status Report

pain.002
Group Header
Original Group 
Information And Status
Original Payment 
Information And Status
Transaction Information
and Status
105
• Group Header which contains a set of characteristics shared by all 
individual transactions in the message. 
• Original Group Information and Status contains the group of 
transactions, to which the status report message refers to. 
• Original Payment Information And Status contains information 
about the original payment information, to which the status report 
message refers.
• Transaction Information And Status provides information on the 
original transactions to which the status report message refers. 
It is used to inform the previous party in the payment chain about the 
positive or negative status of an instruction. It is also used to report on 
a pending instruction.

Interbank pain.001
Interbank pain.002 pacs.008
pacs.002
F A B
Interbank Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to 
provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the 
agents. There are three common use cases: 
Relay: The pain.002 message is sent by the Debtor Agent to the Forwarding Agent which acts as a concentrating financial institution. It
will forward the pain.002 message to the Initiating Party.
camt.053
Debtor Agent*
1
Debtor
Noting in CGI-MP a pain.002 may also be sent by the Debtor Agent directly to the Initiating Party/Debtor which is outside of the scope of CBPR+, 
however the CBPR+ interbank pain.001 message is interoperable with CGI-MP. 
Creditor Agent Creditor Forwarding
Agent Initiating Party
pain.001
*Debtor Agent is the same as the Initiating Party who initiates the payment status report message. 
**or other proprietary method for informing about the status of an instruction
pain.002**

FINplus pain.001
FINplus pain.002 pacs.008
pacs.002
F A B
FINplus Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to 
provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the 
agents. There are three common use cases: 
Relay: The pain.002 message is sent by the Debtor Agent to the Forwarding Agent which acts as a concentrating financial institution. It
will forward the pain.002 message to the Initiating Party.
camt.053
Debtor Agent*
1
Debtor
Noting in CGI-MP a pain.002 may also be sent by the Debtor Agent directly to the Initiating Party/Debtor which is outside of the scope of CBPR+, 
however the CBPR+ FINplus pain.001 message is interoperable with CGI-MP. 
Creditor Agent Creditor Forwarding
Agent Initiating Party
pain.001
*Debtor Agent is the same as the Initiating Party who initiates the payment status report message. 
**or other proprietary method for informing about the status of an instruction
pain.002**
A Payment Initiation Rulebook, available in the Standards Documentation Centre, replaces the legacy MT 
Request for Transfer Service Level Agreement.

Interbank pain.001
pacs.008
Interbank pain.002
pacs.002
B C D
Interbank Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to 
provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the 
agents. There are three common use cases: 
Financial Institution Payment Initiation (to non-FI) : The pain.002 message is sent by the Debtor Agent to the Debtor (Financial 
Institution) who requested to initiate a payment from their account with the Debtor Agent to move funds to a non-Financial Institution 
Creditor.
camt.053
Debtor Agent
3
Debtor Creditor Agent Creditor Initiating Party
A
pacs.008
pacs.002

pacs.002
B A F
Interbank Customer Direct Debit Initiation message is sent by the Initiating Party to the Forwarding Agent or the Creditor Agent. It is used to 
request single or bulk collection(s) of funds from one or various debtor’s account(s) to a creditor. 
Relay: Interbank pain.008 message is sent by the Initiating party (the Creditor or authorised party) to the Forwarding Agent which acts as a 
concentrating financial institution. It will forward the pain.008 message to the Creditor Agent to initiate the direct debit instruction(s)..
Debtor Creditor Agent
*Noting in CGI-MP pain.008 may also be sent by the Initiating Party/Creditor directly to the Creditor Agent which is outside of the scope of CBPR+.
Forwarding Creditor
Agent
*Initiating Party may alternative represent an authorised party such as a head office 
**or other proprietary method for instructing a direct debit initiation request. 
pain.002
camt.053
pacs.003
Debtor Agent
Interbank pain.008
Interbank pain.002
pain.008**
Initiating Party*

110

Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For Payment Initiation (pain) messages the Message Identification has no exact equivalent in
the legacy MT payment message. However, the Sender’s Reference (Field 20) could be
considered as a similar comparison where a pain message contains a single Transaction.
Group Header Message Identification
Each transaction’s Credit Transfer Transaction Information contains a variety of nested 
Payment Identification elements to capture reference related to the individual transaction 
such as a UETR (Unique End-to-end Transaction Reference).
For a relay scenario, Forwarding Agent should respect the Message ID provided by the 
Initiating Party (Debtor Agent) of the pain.002. CGI

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

The Initiating Party in the context of interbank payment initiation report is 
always the Debtor Agent which initiates the pain.002 message. Business 
Identifier Code (BIC FI) is mandated to identify the Initiating Party in the 
pain.002 message. There are three use cases below:
1. Relay: The Debtor Agent sends the pain.002 message to the 
Forwarding Agent which acts as a concentrating financial institution. 
It will forward the pain.002 message to the original Initiating Party who 
can be the Debtor themselves or the Authorised Party. This is 
commonly known as a relay scenario.
2. Authorised Party: The Debtor Agent sends the pain.002 to the 
Financial Institution (Initiating Party) which has the authority to initiate 
a payment on behalf of the Debtor, e.g., multi-bank liquidity sweeps
3. Financial Institution Payment Initiation: The Debtor Agent sends 
the pain.002 to the Financial Institution which is the Debtor who 
initiate a payment from their account to move funds to a non-Financial 
Institution Creditor
113
Initiating Party = Debtor Agent
Forwarding 
Agent
Group Header Initiating Party
Authorised FI Debtor
Party

message is not the original Debtor. In this case, the Initiating Party (the Debtor Agent) has to 
provide Business Identifier Code (BIC FI) of the Forwarding Agent in the pain.002 message. 
The Forwarding Agent acts as a concentrating financial institution and forwards the pain.002 
message to the Debtor or the Initiating Party. 
Other options to identify the Forwarding Agent
include:
• Clearing System Member ID
• LEI (Legal Entity Identifier)
Group Header Forwarding Agent
For the use case of multi-bank liquidity sweeps, Forwarding Agent is not required. 
114
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

115

Report relates to. The mandatory Original Message Identification contains the point-to-point reference,
and the mandatory Original Message Name Identification contains the message name of the underlying
payment being reported upon. Optionally the Original Creation Date Time can also be captured.
Original Message Identification must transport the 
Message Identification of the underlying payment 
(e.g., pain.001).
For a relay scenario, Forwarding Agent (F) should 
respect the Message ID provided by the Initiating 
Party of the pain.001 and pain.002. 
Interbank pain.002
F A
For example:
Original Message Name Identification
“pain.001.001.09” confirms the Status Report is of
a pain.001 Customer Credit Transfer Initiation.
Message 
Identification abcd1234
pain.001.001.09 Original Message 
Name Identification
Original Message 
Identification abcd1234
Message 
Identification xyz9875
Interbank pain.001
Original Group Information and Status 116
pain.001
Message 
Identification abcd1234
pain.002
Message 
Identification xyz9875
pain.001.001.09 Original Message 
Name Identification
Original Message 
Identification abcd1234
CGI

Identification, located in the Original Group Information and Status. This 35 character identifier 
is a point-to-point reference used to unambiguously identify the payment information group or 
batch reference if the message contains multiple transactions. 
Original Payment Information and Status
Original Payment Information Identification
Since the interbank pain.001 and pain.002 usage guidelines are restricted to one 
single transaction, this value is the same as the Original Message ID of the 
Original Group Information And Status.

pyg pyyp
Transaction Information and Status
Mandatory element (in addition to Original Message identification and Original
Message Name Identification described on the previous pages) include:
Original End to End Identification
Original UETR
The following element is optional:
Original Instruction Identification
These Original elements enable the Initiating Party to associate the Payment
Status with the payment they originally sent.
Min 0 – Max 1
Min 1 – Max 1
Min 1 – Max 1
118
Original Payment Information and Status
Original End to End Identification
Original UETR
Original Instruction Identification

pppgpy 
Transaction Status element is arguable the most significant/core parts of the pain.002 and optionally may
further be complimented with Status Reason Information.
The nested Status Reason Information enable the optional inclusion of:
Originator – the party that issues the status. Typically, the pain.002 Initiating Party and 
therefore Originator is not necessary.
Reason – which utilises an ISO external Status Reason code. For example, AC04 ‘Closed 
Account Number’ would compliment a RJCT (Reject) Transaction Status.
Additional Information – a text element to provide further status reason information, 
necessary where the Reason code is NARR 
Min 0 – Max 1
Status Reason Information
Transaction Status
Transaction Information and Status
Note: A Reason code must be provided where the Transaction Status RJCT (Reject) code is used. 
119

120
ACCP AcceptedCustomerProfile Preceding check of technical validation was successful. Customer 
profile check was also successful.
Sent by any Agent in the payment chain to confirm acceptance prior to 
technical validation. 
ACFC AcceptedFundsChecked Preceding check of technical validation and customer profile was 
successful and an automatic funds check was positive.
Sent by any Agent in the payment chain to confirm the technical validation/ 
profile w as positive and automatic funds check w as positive.
ACIS AcceptedandChequeIssued Payment instruction to issue a cheque has been accepted, and the 
cheque has been issued but not yet been deposited or cleared.
Sent by any Agent in the payment chain to confirm a cheque has been issued 
as requested.
ACSC AcceptedSettlementCompleted Settlement has been completed. Sent by the Any Agent to confirm settlement of a payment message leg.
ACSP AcceptedSettlementInProcess All preceding checks such as technical validation and customer 
profile were successful and therefore the payment initiation has been 
accepted for execution.
Sent by any Agent to the to confirm the payment is accepted follow ing 
technical validations being successfully completed. 
ACTC AcceptedTechnicalValidation Authentication and syntactical and semantical validation are 
successful
Sent by any Agent in the payment chain to the previous Agent to confirm the 
payment is accepted follow ing technical validations being successfully 
completed. 
ACWC AcceptedWithChange Instruction is accepted but a change will be made, such as date or 
remittance not sent.
Sent by any Agent in the payment chain to the previous Agent to confirm the 
payment is accepted follow ing amendments being made. 
ACWP AcceptedWithoutPosting Payment instruction included in the credit transfer is accepted 
without being posted to the creditor customer’s account.
Sent by Creditor Agent to the previous Agent to confirm the acceptance of 
payment w ithout settlement on the creditor’s account,
CPUC CashPickedUpByCreditor Cash has been picked up by the Creditor. Sent by Creditor Agent to the previous Agent to confirm that the cash 
collection has been picked up by the Creditor,
PDNG Pending Payment initiation or individual transaction included in the payment 
initiation is pending. Further checks and status update will be 
performed.
Sent by any Agent in the payment chain to the previous Agent as an interim 
status w hilst other validations are performed.
RCVD Received Payment initiation has been received by the receiving agent. Sent by Any Agent to the previous Agent as confirmation that their Customer 
Credit Transfer initiation request has been received by the payment engine.
RJCT Rejected Payment initiation or individual transaction included in the payment 
initiation has been rejected.
Sent by Any Agent to inform the previous Agent that their Customer Credit 
Transfer has been rejected.

y
element facilitates updates from the 
Debtor Agent to the previous Agent, 
e.g., the Forwarding Agent or the 
payment originator (the Debtor / the 
Initiating Party) on changes to the 
status of the payment. Such Status 
Information messages (pain.002), 
with the exception of reject code 
RJCT which is mandatory in 
CBPR+, are bilateral agreed, where 
upon a variety of these Transaction 
Statuses may be used by the 
Instructed Agent at different stages 
of the payment processing.
And Settlement message (pacs) and the role of the Agents in providing these status. 
121
Transaction Information and Status
Transaction Status
Forwarding/Debtor Agent
PDNG
ACWP
ACFC
ACCP
ACWC
ACSC
ACTC
ACCC
Creditor
Agent
Any RCVD
Agent
RJCT
ACIS
CPUC
ACSP

g
Interbank Customer Payment Status Report – Relay
Use Case pn.2.1.1 – High Level Payment Initiation Interbank ‘relay’ status report 
Use Case pn.2.1.1.a – High Level Payment Initiation Interbank ‘relay’ status report Multi-bank Sweep 
Use Case pn.2.1.2 – High Level Payment Initiation Interbank ‘relay’ status report involving a Payment Market Infrastructure
Use Case pn.2.1.3 – High Level Direct Debit Initiation Interbank ‘relay’ status report involving a Payment Market Infrastructure
Interbank Customer Payment Status Report – Authorised Party
Use Case pn.2.2.1 – High Level Payment Initiation Interbank status report for Authorised Party
Use Case pn.2.2.1.a. – High Level Payment Initiation Interbank status report for FI-Initiated Sweep (Long position at the Secondary Account)
Use Case pn.2.2.1.b. – High Level Payment Initiation Interbank status report for Authorised Party to pay themselves as the Creditor.
Interbank Customer Payment Status Report – Financial Institution
Use Case pn.2.3.1 – High Level Payment Initiation Interbank status report for Financial Institution Payment Initiation
Interbank multiple Payment Status Reports
Use Case pn.2.4.1 – High Level Payment Initiation Interbank ‘relay’ multiple status reports
Use Case pn.2.4.2 – High Level Rejection of an incomplete ‘relay’ Payment
Use Case pn.2.4.3 – High Level Direct Debit Initiation Interbank ‘relay’ multiple status reports involving a Payment Market Infrastructure
122

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
relays the same information to the Initiating Party.
F A B
123
Interbank pain.001
Interbank pain.002
1
pain.001
pain.002
Creditor Agent (B) receives the 
credit transfer message, credits the 
Creditor, and sends a camt.053 
(statement) at the end of the 
business day
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
relays the same information to the Initiating Party.
A
F B
124
Interbank pain.001
Interbank pain.002
1
pain.001
pain.002
Creditor Agent (B) receives 
the credit transfer message, credits 
the Creditor, and sends a 
camt.053 (statement) at the end of 
the business day
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
relays the same information to the Initiating Party.
F A B
125
Interbank pain.001
Interbank pain.002
1
pain.001
pain.002
Creditor Agent (B) receives local 
credit transfer message via the 
Payment Market Infrastructure and 
credits the Creditor
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

1
which relays the same information to the Initiating Party.
B A F
126
Interbank pain.008
Interbank pain.002
pain.008
pain.002
Debtor Agent (B) receives a local 
direct debit message via the 
Payment Market Infrastructure and 
debits the account of the Debtor 
pacs.003
Market Infrastructure will establish their own usage guidelines based on the ISO 
20022 standard.
1
Initiating Party sends a direct 
debit instruction to the 
Forwarding Agent
Forwarding Agent (F) forwards 
the payment instruction to the 
Creditor Agent (A)
2
2
Creditor Agent (A) provides a 
status update ACSP (accepted 
settlement in progress) to the 
Forwarding Agent (F), based upon 
a bilateral agreement
Creditor Agent (A) instructs a 
direct debit transaction by 
sending a local direct debit 
message pacs.003 to a Payment 
Market Infrastructure
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
pacs.003
3b

As a pre-requisite the Debtor 
provides Debit Authorisation to 
Agent I to Initiate Payment from 
their account with the Debtor 
Agent (A)
pacs.008
Institution which initiated a payment based on Debit Authorisation with the Debtor and the Debtor Agent.
I B
127
Interbank pain.001
Interbank pain.002
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
DA 3 4
Debtor Agent (A) optionally provides a 
status update to the Initiating Party 
(Agent I), based upon a bilateral 
agreement
Debtor Agent (A) debits the account of 
Debtor and initiates a credit transfer
DA 3
2
2
3a
Creditor Agent (B) receives credit transfer 
message, credits the Creditor and 
optionally provided a status report to 
Debtor Agent based upon a bilateral 
agreement. It also sends the result of the 
sweep by camt.052 (intraday sweep) and 
or camt.053 (statement) to the Corporate
4

Agent I receives intraday 
balance report from the
Debtor Agent (A) on behalf 
of their mutual customer
pacs.008
Institution which initiated a liquidity sweep on behalf of a corporate customer based on the sweep contract
I B
128
Interbank pain.001
Interbank pain.002
camt.052
Agent (I) initiates a sweep on 
behalf of the Corporate by 
sending pain.001 to the Debtor 
Agent
camt.053
Sweep 
Contract
A pacs.002
1
1
4
4
3
Debtor Agent (A) optionally provides a 
status update to the Initiating Party 
(Agent I), based upon a bilateral 
agreement
Debtor Agent (A) debits the account of 
Debtor and initiates a credit transfer
3
See use case p.8.1.2 for a sweeping contract with 
a short position
Creditor Agent (B) receives credit transfer 
message, credits the Creditor, and sends 
a camt.053 (statement) at the end of the business 
day to the Creditor. An optional status report is sent 
to the previous Agent based upon a bilateral 
agreement
2
2
3a
3a

As a pre-requisite the Debtor 
provides Debit Authorisation to 
Agent I to Initiate Payment from their 
account with the Debtor Agent (A)
pacs.008
account based on Debit Authorisation already in place to move money to themselves as the Creditor
I B
129
Interbank pain.001
Interbank pain.002
Agent (I) initiates a payment request 
(pain.001) to the Debtor Agent (A) to 
move fund from the Debtor’s 
account, as an authorised party, to 
themselves as the Creditor
camt.053
Debit 
Authorisation
A pacs.002
DA 4
4
3
Debtor Agent (A) optionally provides a 
status update to the Initiating Party 
(Agent I), based upon a bilateral 
agreement
Debtor Agent (A) debits the account of 
Debtor and initiates a credit transfer
3
Creditor Agent (B) receives the credit transfer 
message, credits the Creditor, and sends a 
camt.053 (statement) at the end of the 
business day to the Creditor. An optional 
status report is sent to the Debtor Agent based 
upon a bilateral agreement
DA
I
2
2
3a
3a

pacs.008
Financial Institution which initiated a payment to a nonFinancial Institution Creditor using their own account
I B
130
Interbank pain.001
Interbank pain.002 2a
1
Agent (I), the Debtor, initiates a 
payment request (pain.001) to 
the Debtor Agent (A) to move 
funds from their own account
camt.053
A pacs.002
3
3
2
Debtor Agent (A) optionally provides a 
status update to the Initiating Party 
(Agent I), based upon a bilateral 
agreement
Debtor Agent (A) debits the account of 
Agent (I), the Debtor and initiates a 
credit transfer
1 2
2a
Creditor Agent (B) receives credit transfer 
message, credits the Creditor, and 
optionally returns a status report to Debtor 
Agent based upon a bilateral agreement. 
It also sends camt.053 (statement) to the 
non-FI Creditor

1
1
Initiating Party sends a 
payment instruction to the 
Forwarding Agent
Forwarding Agent (F) forwards
the payment instruction to the 
Debtor Agent (A)
Debtor Agent (A) processes the 
payment and sends to the 
Creditor Agent (B)
4
4a
Debtor Agent (A) optionally 
provides a status update ACTC 
(accepted technical validations 
are successful) to the 
Forwarding Agent (F), based 
upon a bilateral agreement.
3
pacs.008
4
Debtor Agent (A) optionally 
provides a further status update 
ACSP (accepted settlement in 
progress) to the Forwarding Agent 
(F), based upon a bilateral 
agreement.
(with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle.
F A B
131
Interbank pain.001
Interbank pain.002
pain.001
pain.002
Interbank pain.002
Forwarding Agent (F) relays a 
further status update ACSP 
(accepted settlement in 
progress), to the Initiating Party, 
based upon a bilateral 
agreement.
pain.002
Forwarding Agent (F) relays the 
status ACTC (accepted technical 
validations are successful) to the 
Initiating Party, based upon a 
bilateral agreement.
3a
4b
2
3
3a
4b
4a
5
5
Creditor Agent (B) processes the 
payment and sends the statement to 
Creditor
2
camt.053

1
Initiating Party sends a 
payment instruction to the 
Forwarding Agent
(with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle.
132
Debtor Agent refund the Debtor’s 
account and update the status 
RJCT with the reason code to the 
Forwarding Agent 
+ Reject 
Reason 
Having received the payment the 
Creditor Agent recognises the payment 
cannot be completed e.g., the 
Creditor’s account is closed. Agent B 
rejects the payment and send pacs.002 
to the Debtor Agent
+ Reject 
Reason 
+ Reject 
Reason Where a payment is rejected, the use of 
the pain.002 status RJCT (Reject) with the 
ISO Status Reason Code is mandatory.
1
4a
3a
pacs.008
3
F A B
Interbank pain.001
Interbank pain.002
pain.001
pain.002
pain.002 Interbank pain.002
3b
4b
2
Forwarding Agent (F) relays 
the payment to the Debtor 
Agent (A)
2
Debtor Agent (A) processes the 
payment and sends to the 
Creditor Agent (C)
3
Debtor Agent (A) optionally 
provides a status update ACSP 
(accepted settlement in progress) 
to the Forwarding Agent (F), 
based upon a bilateral 
agreement.
3a
Forwarding Agent (F) relays the status 
ACSP (accepted settlement in 
progress) to the Initiating Party, based 
upon a bilateral agreement.
3b
pacs.002
4a
Forwarding Agent (F) relays a 
further status update RJCT with 
the reason code to the Initiating 
Party
4b

1
which relays the same information to the Initiating Party.
B A F
133
Interbank pain.008
Interbank pain.002
pain.008
pain.002
Having received the direct debit, PMI 
recognises the transaction cannot be 
completed, e.g., insufficient funds in 
the debtor’s account and sends back
pacs.002 Reject
pacs.003
1
Initiating Party sends a direct 
debit instruction to the 
Forwarding Agent
Forwarding Agent (F) forwards 
the payment instruction to the 
Creditor Agent (A)
2
Creditor Agent (A) provides a 
status update ACSP (accepted 
settlement in progress) to the 
Forwarding Agent (F), based upon 
a bilateral agreement
Creditor Agent (A) instructs a direct 
debit transaction by sending a local 
direct debit message pacs.003 to a 
Payment Market Infrastructure 
(PMI)
Forwarding Agent (F) relays the 
status ACSP (accepted settlement 
in progress) to the Initiating Party, 
based upon a bilateral agreement
3
3
3a 3b
3a
pacs.003
pain.002 4b
Interbank pain.002 4a
pacs.002
pacs.002
2
Where a direct debit is rejected/ 
returned, the use of the pain.002 
status RJCT (Reject) with the ISO 
Status Reason Code is mandatory.
+ Reject 
Reason 
Forwarding Agent (F) relays a 
further status update RJCT with the 
reason code to the Initiating Party
Creditor Agent update the status 
RJCT with the reason code to the 
Forwarding Agent
4
3b 4a
pacs.002
+ Reject 
Reason 
+ Reject 
Reason

Interbank Customer 
Direct Debit Initiation
134

135
ISO MT
Group Header
➢ Message Identification
➢ Initiating Party – where different from Creditor
➢ Forwarding Agent 
Payment Information
➢ Payment Information Identification
➢ Requested Collection Date
➢ Creditor
➢ Creditor Agent
Direct Debit Transaction Information
➢ Payment Identification 
➢ Instructed Amount
➢ Charge Bearer
➢ Mandate Identification
➢ Debtor Agent
➢ Debtor
Sequence A – General Information:
➢ Sender’s Reference (Field 20)
➢ Instructing Party (Field 50 C or L)
Message Senderin a ‘relay’ scenario
Sequence A – General Information:
➢ Customer Specified Reference (Field 21R)
➢ Requested Execution Date (Field 30)
➢ Creditor (Field 50 A or K)*
➢ Creditor’s Bank (Field 52 A, C or D)*
Sequence B – Transaction Details:
➢ Transaction Reference (Field 21)
➢ Currency and Transaction Amount (Field 32B)
➢ Details of Charges (Field 71A)
➢ Mandate Reference (Field 21C)
➢ Debtor’s Bank (Field 57 A, C or D)
➢ Debtor(Field 59 no letter or A)
ISO 20022 message element MT Field Name & (Tag option)
*or in Sequence B – Transaction Details

pain.008
Group Header
Payment 
Information
Direct Debit 
Transaction 
Information
Direct Debit Initiation relay messages in a many-to-many 
space allow for multiple transactions as they will be typically 
cleared by Automated Clearing House (ACH) batch 
processing system. 
The pain.008 message is composed of three blocks:
• Group Header contains a set of characteristics that relates 
to all individual transaction.
• Payment Information contains a set of characteristics that 
relates to the credit side of the transaction, such as Creditor 
and Creditor Agent.
• Direct Debit Transaction Information contains, among 
others, elements related to the debit side of the transaction, 
such as Debtor and Debtor Agent and optionally mandate 
related information.

pacs.002
B A F
Interbank Customer Direct Debit Initiation message is sent by the Initiating Party to the Forwarding Agent or the Creditor Agent. It is used to 
request single or bulk collection(s) of funds from one or various debtor’s account(s) to a creditor. 
Relay: Interbank pain.008 message is sent by the Initiating party (the Creditor or authorised party) to the Forwarding Agent which acts as a 
concentrating financial institution. It will forward the pain.008 message to the Creditor Agent to initiate the direct debit instruction(s)..
Debtor Creditor Agent
*Noting in CGI-MP pain.008 may also be sent by the Initiating Party/Creditor directly to the Creditor Agent which is outside of the scope of CBPR+.
Forwarding Creditor
Agent
*Initiating Party may alternative represent an authorised party such as a head office 
**or other proprietary method for instructing a direct debit initiation request. 
pain.002
camt.053
pacs.003
Debtor Agent
Interbank pain.008
Interbank pain.002
pain.008**
Initiating Party*

138

Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For the Payment Initiation (pain) messages the Message Identification has no exact equivalent
in the legacy MT payment message. However, the Sender’s Reference (Field 20) could be
considered as a similar comparison where a pain message contains a single Transaction.
For a relay scenario, Forwarding Agent should respect the Message ID provided 
by the Initiating Party (Creditor or authorized third party) of the pain.008.
Group Header Message Identification
Each transaction’s Direct Debit Transaction Information contains a variety of nested 
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
Unlike other CBPR+ messages, the interbank pain.008 message is more flexible in
defining the date and time elements. The most recommended representation is Local time
with UTC offset which was mandated by CBPR+ (2nd option). Otherwise use UTC time
(1st option). Decimal fractions of milliseconds with 3 digits are optional.

Group Header Authorisation
For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for 
Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.
or Transaction Level approval by additional security provisions, such as digital signature or user key. The
Authorisation uses an embedded code set or free text form. It has no equivalent in the legacy MT direct debit
message.
Code Description Description
ILEV Instruction Level Authorisation File requires all customer transactions to be authorised or approved.
FDET File Level Authorisation Details Additional file level approval, with the ability to view both the payment information block 
and supporting transaction detail.
FSUM File Level Authorisation Summary Additional file level approval, with the ability to view only the payment information block.
AUTH PreAuthorised File File has been pre-authorised or approved within the originating customer environment 
and no further approval is required.

Multiple transactions are allowed in CBPR+ direct debit usage guidelines. However, it is 
recommended to have only one single direct debit transaction unless bilaterally 
determined. 
Group Header Number of Transactions
142
contained within the message.
Single transactions in the CBPR+ direct debit usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant collection, supporting the next
generation of innovation.

The Initiating Party can either be the Creditor or an AuthorisedParty who initiates 
direct debit transactions on behalf of the Creditor. The Initiating Party can be, for 
example, the Head Office which is authorised by its subsidiary to request for payment 
amount to be collected from the Debtor. In the centralization model, the Initiating 
Party can also be a payment factory or shared service centre or third party agent, 
which has authority to send the message on behalf of the Creditor.
In the interbank pain.008 ‘Relay’ message use case: The Initiating Party sends the 
pain.008 message to the Forwarding Agent which acts as a concentrating financial 
institution. It will forward the pain.008 message to the Creditor Agent. 
Forwarding Agent / FI
Initiating Party
Creditor Authorised Party
143
Group Header Initiating Party
Initiating Party has a mandate (debit authority agreement) to debit the account of the Debtor.

Sub elements describe the Initiating Party in greater detail. 
Address is provided. 
Identification
Nested element capturing the 
various types of identifiers, e.g. 
BIC, LEI etc.
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
144
Initiating 
Party
Contact 
Details
Optional contact details
Group Header Initiating Party

Creditor or authorised third party) has to provide Business Identifier Code (BICFI) of the 
Forwarding Agent in the pain.008 message. The Forwarding Agent acts as a concentrating 
financial institution and forwards the pain.008 message to the Creditor Agent for execution.
Other options to complement the identity of the 
Forwarding Agent include:
• Clearing System Member ID
• LEI (Legal Entity Identifier)
Group Header Forwarding Agent
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

146

147
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
pain.008

This 35 character identifier is a point-to-point reference used to unambiguously 
identify the payment information group within the message. It is also known as a 
batch reference number if the message contains multiple transactions. 
Payment Information Payment Information Identification
For a single batch in the CBPR+ usage guidelines, the value in Payment Information 
Identification is the same as the Message Identification of the Group Header. 
y pygp g

amount of money. The payment method code “DD” Direct Debit must be used.
Code Name Definition
DD Direct Debit Collection of an amount of money from the Debtor’s 
bank account by the Creditor. The amount of money 
and dates of collections may vary.
Payment Information Payment Method

entry for the sum of the amounts of all transactions within the group of a message is requested.
Payment Information Batch Booking
Batch booking is used to request for a consolidated credit entry on the Creditor’s account.
Where this optional element is not used, the default of single credit entries is applied on the 
Creditor’s account.

It is defined by ISO Date expressed in the YYYY-MM-DD format. 10
Payment Information Requested Collection Date
creditor requests that the amount of money is to be collected from the debtor.

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
Payment Information Creditor
In order to process the pain.008 interbank into a CBPR+ payment, CBPR+ 
requires either structured or unstructured postal address.
Take me to an explanation of CGI Postal Address

153
made as a result of the transaction, which will be also reflected in their account Statement.
The Creditor Account uses a variety of nested elements to capture information related to 
the account.
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account, recommended.
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
Indication of Currency of the Creditor Account is recommended in case of multi-currency accounts 
whereby a single account number is allocated to the Creditor Account
Payment Information Creditor Account
CGI
153

relationship with their customers, the Creditor. 
Note: Although the Creditor Agent, Debtor Agent, Creditor and Debtor all maintain static roles in the
pain messages, the description of these parties change in the reporting messages (camt) where the
Creditor Agent and Debtor Agent become the Statement Account Servicer and the Creditor and the Debtor
become the Statement Account Owner. This will be explored further in the camt Cash Management
Reporting section.
154
Payment Information Creditor Agent
For Agent Identification, BIC is preferred, alternatively Clearing Member 
ID together with Name and Address may be provided.

155
Agent. 
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
Creditor Agent and Debtor Agent are Financial Institutions, therefore
the nested elements Name and Proxy are unlikely to be used.
Payment Information Creditor Agent Account

Charges account should be used when charges have to be booked to an account different 
from the account identified in debtor’s account.
Payment Information Charges Account
transaction.
This element is not widely used in the payment industry.

Charges account agent should only be used when the charges account agent is different 
from the creditor agent.
Payment Information Charges Account Agent
charges account.
This element is not widely used in the payment industry.

158

a point-to-point reference of 35 characters long will be returned
to account statements if provided by the initiating party.
an end-to-end reference provided by the Initiating Party
which must be passed unchanged throughout the
payment and reported to the Creditor.
note: if the Initiating Party has not provided an end-to-end
identifier, the Creditor Agent may populate “NOTPROVIDED” to
comply the mandatory need of this element.
the Unique End-to-end Transaction Reference created using the
UUID v4 standard. This reference must be passed unchanged
throughout the payment, it may also be created by the Creditor
within their Payment Initiation request, and also included in
reporting messages.
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
159
Payment Identification
Direct Debit Transfer Transaction Information

Anested element which may either use an external ISO Service Level
code or a proprietary code. It is used to identify a particular agreed
service level which should be applied to the payment.
Payment
Type 
Information
A nested element which may either use an external ISO
Local Instrument code or a proprietary code. It can be
used in combination with Service Level to identify the
type of local instrument. For example, CORE is a
transaction related to SEPADirect Debit Core.
A nested element which may either use an external ISO Category Purpose code or a
proprietary code. It is used to identify the category of payment.
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
Sequence
Type
Min 0 – Max 1
A nested element which uses an embedded code to identify the
direct debit sequence, such as first, recurrent, final or one-off
Payment Type Information
Direct Debit Transfer Transaction Information

The Instructed Amount captures currency and amount of money to be moved
between the Debtor and Creditor, before deduction of charges, expressed in the
currency as ordered by the initiating party. This amount has to be transported
unchanged through the transaction chain. This element is comparable with both the
legacy Field 33B and Field 32B.
g
Instructed
Amount
£
$
¥
For multiple transactions, the currency must be the same 
for each transaction.
Instructed Amount
Direct Debit Transfer Transaction Information

py pypy gpg py
transaction. This element is comparable with MT Field 71A ‘Details of Charges’
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
SLEV Following Service Level
162
Charge Bearer Code SLEV (Following Service Level) is not allowed in the CBPR+ pain.008 interbank.
Charge Bearer
Direct Debit Transaction Information

Credit party that signs the mandate, may be used if
supported by the Direct Debit Schema. (see next page for
additional detail on this nested element)
Unique and unambiguous identification of the pre-notification which is
sent separately from the direct debit instruction.
Direct 
Debit 
Transaction
Pre 
Notification 
Date
Provides further details of the direct debit mandate signed between 
the creditor and the debtor. E.g., Mandate Identification, Date of 
Signature and Electronic Signature.
Date on which the creditor notifies the debtor about the amount and date on
which the direct debit instruction will be presented to the debtor's agent.
Direct Debit Transaction
Direct Debit Transaction Information
Pre 
Notification 
Identification
Creditor 
Scheme 
Identification
Mandate 
Related 
Information
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

related to the credit party that signs the mandate who is different from the Creditor.
The Creditor Scheme Identification element offers the following options:
Name
Postal Address: Not used often
Identification
Country of Residence
Contact Details
164
CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit 
Scheme.
Direct Debit Transaction
Direct Debit Transaction Information
Creditor Scheme Identification
CGI

The Ultimate Creditor element should not be confused with an Initiating
Party who may send a direct debit initiation request on behalf of the
Creditor, for example, Payment Factory.
CBPR+ premise is that an Ultimate Creditor has no financial regulated
direct account relationship with the corresponding Creditor. Likewise, an
Ultimate Debtor has no financial regulated account relationship with the
corresponding Debtor.
Party
Ultimate
Creditor
Ultimate
Debtor
The Ultimate Creditor and Ultimate Debtor can be identified by a combination of Name and structured 
address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.
165
Ultimate Creditor
Direct Debit Transaction Information
Ultimate Debtor
In the context of direct debit, Ultimate Creditor and Ultimate Debtor are not commonly used.

relationship with their customers, the Debtor. 
Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the
pain messages, the description of these parties change in the reporting messages (camt) where the
Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor
become the Statement Account Owner. This will be explored further in the camt Cash Management
Reporting section.
166
CGI Debtor Agent
Direct Debit Transaction Information
For Agent Identification, BIC is preferred, alternatively Clearing Member 
ID together with Name and Address may be provided.

167
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
the nested elements Name and Proxy are unlikely to be used. Debtor Agent Account
Direct Debit Transaction Information

elements describe the Debtor in greater detail.
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
Note: Structured address is
strongly recommended with
mandatory Town Name and
Country
In order to process the pain.008 interbank into a CBPR+ payment, CBPR+ 
requires either structured or unstructured postal address.
Take me to an explanation of CGI Postal Address Debtor
Direct Debit Transaction Information
the Postal Address together with
the Name

made as a result of the transaction, which will be also reflected in their account Statement.
The Debtor Account uses a variety of nested elements to capture information related to 
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
169
Debtor Account
Direct Debit Transaction Information

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
170
Ultimate Creditor
Direct Debit Transaction Information
In the context of direct debit, Ultimate Creditor and Ultimate Debtor are not commonly used.

related to the processing of the direct debit.
The Instruction for Creditor Agent element offers a maximum of 140 characters to
provide further information related to the processing of the direct debit instruction, that 
may need to be acted upon by the Creditor Agent, depending on bilateral agreement. 
171
Instruction for Creditor Agent
Direct Debit Transaction Information

The purpose is used to capture the nature of the payment, e.g., IVPT Invoice Payment, FEES Payment of
Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is
typically defined by the Debtor.
The externalised Purpose code set is classified by the purpose, for example commercial, for 
which the numerous codes within the classification are each described by Name and 
Definition. For example, LOAR is classified within the Finance categorisation, with the Name
Loan Repayment described as a repayment of loan to lender. 
Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can
trigger special processing e.g. Category Purpose code RPRE ‘Represented’ may trigger a representation
of previously reversed or returned direct debit transactions.
172
Direct Debit Transaction Information
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
Direct Debit Transaction Information Regulatory Reporting
Debit Credit Reporting Indicator
Authority
Details
173
For the purpose of direct debit, Regulatory Reporting is not commonly used.

when tax information is used by the clearing or the local regulatory authority(s). 
Tax information block is also available within the Structured Remittance Information block which is applicable 
when tax information is used by the creditor as part of remittance information.
Tax Information is not commonly used.
Direct Debit Transaction Information
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
174

The Remittance Identification captures a unique reference assigned by the initiating party of the direct 
debit to identify the remittance information sent separately from the direct debit instruction.
The Remittance Location Details uses a set of nested elements to provide information on either the 
location of or the delivery of remittance information.
• Method requires a code from an embedded list to detail the method used to deliver the remittance 
advise information e.g. EMAL (email)
• Electronic Address provides an electronic address for which an agent is to send the remittance 
information to e.g. the email address. It may also reference a URL where remittance information 
maybe deposited or retrieved.
• Postal Address provides the postal address to which an agent is to send the remittance information
Unlike CBPR+ pacs messages, in the interbank pain.008 message, Related Remittance Information and 
Remittance Information are non-mutually exclusive due to a corporate use case of populating both information 
blocks for detailing remittance advices which are part of value-added service offered by the CreditorAgent.
Min 0 – Max 1
Min 0 – Max *
Direct Debit Transaction Information
Related Remittance Information
175

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
Direct Debit Transaction Information
Remittance Information
Structured
Unstructured
176

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
The Creditor Remittance Information is provided by
the Creditor in the Cash Management Reporting
messages’ Remittance Information component, for
example, the camt.053 Bank to Customer Statement.
Remittance Information
Structured
Direct Debit Transaction Information
177

reconciliation by the Creditor upon receipt of the amount of money.
Creditor Reference in the Structured Remittance Information can be based on ISO 11649
• 2 letters “RF”
• 2 digits check digit
• 21 letters/digits creditor reference
By providing the Creditor Reference in the pain.008, such as invoice number for collection, it will facilitate STP and 
auto-match the incoming credit entry. The Creditor Reference can be extracted from the statement (e.g., camt.053 
Structured Remittance information within the Transaction Details or MT 940 Field 61 or Field 86).
Equally the End-To-End Identification could perform a similar function
SCORE Guideline: For Creditor Reference information, in instances where the 
Creditor Reference Type code is SCOR (Structured Communication Reference) 
and the Creditor Reference is structured in accordance with ISO 11649, the 
Issuer should be specified with the text ‘ISO’ (without the quote marks)
Remittance Information
Structured
Direct Debit Transaction Information
178

g
Interbank Customer Direct Debit Initiation - Relay
Use Case pn.8.1.1 – High Level Direct Debit Initiation Interbank ‘relay’ (pain.008)
Use Case pn.8.1.2 – High Level Direct Debit Initiation Interbank ‘relay’ (pain.008) involving a Payment Market Infrastructure
179

camt.053
1
1
Initiating Party sends a direct 
debit instruction to the 
Forwarding Agent
Forwarding Agent (F) forwards 
the direct debit instruction to 
the Creditor Agent (A)
2
Creditor Agent (A) provides a 
status update ACSP (accepted 
settlement in progress) to the 
Forwarding Agent (F), based 
upon a bilateral agreement
pacs.003
Forwarding Agent (F) relays the 
status ACSP (accepted settlement 
in progress) to the Initiating Party, 
based upon a bilateral agreement
request the collections of funds from the debtors accounts for a creditor.
B A
180
Interbank pain.008
Interbank pain.002
pain.008
pain.002
Debtor Agent (B) processes the 
direct debit and sends the statement 
to Debtor
Creditor Agent (A) instructs 
Debtor Agent (B) to perform a 
direct debit transaction by 
sending a local direct debit 
message or pacs.003
2
3
4
4
3a
3a
3b
F
3
camt.053 3b

1
request the collection of funds from the debtors accounts for a creditor (through a Payment Market
Infrastructure).
B A F
181
Interbank pain.008
Interbank pain.002
pain.008
pain.002
Debtor Agent (B) receives a local 
direct debit message via the 
Payment Market Infrastructure 
(PMI) and debits the account of the 
Debtor 
pacs.003
Market Infrastructure will establish their own usage guidelines based on the ISO 
20022 standard.
1
Initiating Party sends a direct 
debit instruction to the 
Forwarding Agent
Forwarding Agent (F) forwards 
the payment instruction to the 
Creditor Agent (A)
2
2
Creditor Agent (A) provides a 
status update ACSP (accepted 
settlement in progress) to the 
Forwarding Agent (F), based upon 
a bilateral agreement
Creditor Agent (A) instructs a 
direct debit transaction by 
sending a local direct debit 
message or pacs.003 to a 
Payment Market Infrastructure
Forwarding Agent (F) relays the 
status ACSP (accepted settlement 
in progress) to the Initiating Party, 
based upon a bilateral agreement
3
3
4
3a
3a
3b
pacs.003
4
camt.053
camt.053 3b

g
182

pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer
pacs.009 - Financial Institution Credit Transfer
pacs.009 (cov)- Financial Institution ‘Cover’ Credit Transfer
pacs.009 (adv) – Financial Institution ‘advice’ of Credit Transfer
Payment Rejection and Return
pacs.002 – Financial Institution To Financial Institution Payment Status Report
pacs.004 – Payment Return
Direct Debit Payments
pacs.010 - Interbank Direct Debit
pacs.010 (col) - Interbank Direct Debit Margin Collection
pacs.003 - Financial Institution to Financial Institution Customer Direct Debit
183

Financial Institution to 
Financial Institution 
Customer Credit Transfer
184

pacs.008
Group Header
Credit Transfer 
Transaction Information Payment messages in a many-to-many payment are considered as a 
single transaction. 
nested elements:
• Group Header which contains a 
set of characteristics that relates to 
all individual transaction
• Credit Transfer Transaction 
Information which contains 
elements providing information 
specific to the individual credit 
transfer transaction. 
185

pacs.008
pacs.008
pacs.008
pacs.002
pacs.002
pacs.002
A B C D
The Financial Institution To Financial Institution Customer 
Credit Transfer message is sent by the Debtor Agent to 
the Creditor Agent, directly or through other agents and/or 
a payment clearing and settlement system. 
It is used to move funds from a Debtor account to a 
Creditor, whereby one or both of these Parties are non-Financial Institutions. 186

187

pygg, 
Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
For Payment Clearing and Settlement (pacs) messages the Message Identification has no
exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field
20) could be considered a similar comparison where a pacs message contains a single
Transaction.
Group Header Message Identification
188
Each transaction’s Credit Transfer Transaction Information contains a variety of nested
Payment Identification elements to capture reference related to the individual transaction such
as a UETR (Unique End-to-endTransactionReference)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
189

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 
Group Header Number of Transactions
190
g
Single transactions in the CBPR+ payment usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant payments, supporting the next
generation of innovation.

D
27
191
The Settlement Method element in the pacs.008 allows a choice of an embedded code.
COVE indicate this Customer Credit Transfer will be settlement using a covering pacs.009 (COV). The 
Agents being used in the covering payment to reimburse the Instructed Agent can be provided in the 
dedicated Reimbursement Agent elements. This allows the Instructed Agent to identify the debit account 
on their books from the Reimbursement Agent account or look up the account related to the 
reimbursement agent.
INDA indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account 
Servicing Institution) The account held at the Instructed Agent may captured in the dedicated Settlement 
Account element.
INGA indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who 
has credited the Account they service for the Instructed Agent (as an Account Owner). The account held 
by the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account 
element.
$
€
Settlement Method code CLRG is not part of CBPR+ specifications but instead used in 
Market Infrastructure specification (HVPS+)
Group Header Settlement Information

D
27
Account Servicing Institution i.e. owns the account and provides service to the customer
(Account Owner).
TheAccount Owner can be an Agent or anotherParty.
Traditionally an interbank account relationship may have been referred to as a
Nostro/Vostro relationship or an Agent’s account held on another Agent’s books/ another
Agent’s account held on my books.
Typically the commonality of this can be simplified to the Agent who provides the official
Account statement is servicing the account and therefore is the Agent responsible for
performing the settlement.
Why is it so important to understand which Agent Services the account ?
In ISO 20022, much like the legacy FIN process, each leg of a payment has a settlement component. Commonly one of these
settlement legs occurs over a Market Infrastructure, who typically owns or instructs the settlement between the two Market
Infrastructure participant Agents at a national Central Bank. In this case the Central Bank services both the Instructing Agent
and Instructed Agent accounts which is represented by CLRG in the Settlement Method of a pacs message.
In a number of business Use Cases there are examples of additional legs, which may occur prior to or after a potential Market
Infrastructure, where anAgent is responsible forthe role to service an account and perform settlement of that leg.
This role is important as it determines the subsequencemessage behaviour.
A
Group Header Settlement Information Settlement Method192

D
27
(serviced) on the books of the Instructed Agent or is the Instructing Agent holding
(servicing) the account of the Instructed Agent.
Depending on the answer to this question, this determines the Settlement Method in a
serial payment process.
Where the INstructinG Agent services the account and is responsible for settling the
payment leg, the Settlement Method code INGA is used.
Where the INstructeD Agent services the account and is responsible for settling the
payment leg, the Settlement Method code INDA is used.
A
B
My account with you
OR
pacs.008 pacs.008 pacs.008
A B C D
pacs.008
INDA CLRG CLRG INGA
C
Payment transaction lifecycle
Cash Management Reporting
B
Group Header Settlement Information Settlement Method193

D
27
INGA
The pacs message sent by the Instructing Agent to the Instructed Agent has already been settled.
Instructing Agent may (for example) send
• a pacs.002 to the Previous Agent with status ACSC Accepted Settlement Complete.
• a camt.053 Customer Statement to the Instructed Agent (as Account Owner)
Instructed Agent can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the
Instructed Agent must result in a pacs.004 Payment Return (which in turn triggers a Reverse Indicator on the Account Owners statement).
Creditor Agent having performed the settlement on the Creditor’s account, camt reporting message may be used to report or notify on this credit
entry.
INDA
The pacs message sent by the Instructing Agent to the Instructed Agent has not been settled.
Instructing Agent may (for example) send
• a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress
Instructed Agent may
• Reject the pacs message received, using a pacs.002, as it has not been settled.
• a camt.053 Customer Statement to the Instructing Agent (as Account Owner) Although an rejected entry will not appear in the camt.053
Creditor Agent of a pacs.009 (particularly in the cover scenario) may forward the pacs.009 to the Creditor, as the Creditor will perform the settlement
(they are the Account Servicing Institution)
CLRG
The pacs message sent by the Instructing Agent to the Instructed Agent has not been settled. Settlement is performed by the Market Infrastructure.
Instructing Agent may (for example) send
• a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress
Instructed Agent may
• can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the Instructed
Agent must result in a pacs.004 Payment Return.
Market Infrastructure may
• Reject the pacs message received, using a pacs.002, as it has not been settled.
• a camt.053 Customer Statement to the Instructing Agent and Instructed Agent (as Account Owners)
Group Header Settlement Information Settlement Method194

pacs.008
pacs.008
camt.053
A B C
Agent C is unable to process the 
payment. As the payment was 
already settled by the Instructing 
Agent (Settlement Method INGA) 
Agent C must use a pacs.004 to 
instruct the return of the payment
195
Instructing
Agent: Agent A
Instructed
Agent: Agent B Instructing
Agent: Agent B
Instructed
Agent: Agent C
Settlement Method
INGA
pacs.004
pacs.004
Return 
Reason 
Return 
Reason 
camt.053
Note: return of a payment would involve a booked entry. In this example Agent B would capture the
original booked entry and a separate reversed entry in the statement for Agent A and Agent C. Detail on
statement entry can be found in the camt.053 section.
Group Header Settlement Information Settlement Method
Settlement Method
INDA

pacs.008
pacs.008
camt.053
A B C
Agent D is unable to process the 
payment. As the payment has not 
been settled by themselves Instructed 
Agent (Settlement Method INDA) 
Agent D must use a pacs.002 to 
instruct the return of the payment
196
Instructing
Agent: Agent A
Instructed
Agent: Agent B Instructing
Agent: Agent B
Instructed
Agent: Agent C
pacs.004
pacs.004
Return 
Reason 
Return 
Reason 
camt.053
D
pacs.008
Instructing
Agent: Agent C
Instructed
Agent: Agent D
pacs.002
Reject 
Reason 
Note: rejection of a payment would not involve a booking entry. In this example
Agent D would still produce a customer statement for Agent C, this rejected
payment transaction would however not appear as an entry in this statement
Group Header Settlement Information Settlement Method
196
Settlement Method
INDA
Settlement Method
INGA
Settlement Method
INDA

Group Header Settlement Information
197
The Settlement Account identifies the account details maintained at the account
servicing institution (Agent responsible for the settlement of the instruction as
indicated in the Settlement Method)
Min 0 – Max 1
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
Name identifies the name of the account as assigned by the Account Servicing
Institution
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as
The Instructing Reimbursement Agent, Instructed Reimbursement Agent and Third Reimbursement
Agent. Each of these reimbursement agents also has a dedicated account element to optionally capture their
related account details.
The Instructing Reimbursement Agent captures the Agent who will execute a covering payment (i.e. pacs.009
COV or domestic equivalent) often referred to as the currency correspondent. This optional element is
comparable with the Field 53a in the legacy FIN message.
$
Min 0 – Max 1
Min 0 – Max 1
Group Header Settlement Information
198
The Instructing Reimbursement Agent Account captured the account related to this Reimbursement Agent.
This element can be compared to the Party Identifier of the legacy Field 53.

Min 0 – Max 1
199
The Instructed Reimbursement Agent Account captured the account related to this Reimbursement Agent.
This element can be compared to the Party Identifier of the legacy Field 54.
The Instructed Reimbursement Agent captures the Agent who will receive the covering payment (i.e.,
pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer
$ Instructed Agent. This optional element is comparable with the Field 54a in the legacy FIN message.
€
The Third Reimbursement Agent captures an additional Agent who will receive the covering payment, where
this is not the Agent detailed in the Instructed Reimbursement Agent. This optional element is comparable with
the Field 55a in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Third Reimbursement Agent Account captured the account related to this Reimbursement Agent. This
element can be compared to the Party Identifier of the legacy Field 55.
Group Header Settlement Information

200

Payment
Identification
$
y 
Credit Transfer Transaction Info’ Payment Identification
a point-to-point reference restricted in CBPR+ to 16
character and directly comparable with the Sender’s
Reference (Field 20) of the legacy MT payment message.
Instruction
Identification
Min 1 – Max 1
an end-to-end reference provided by the Debtor
which must be passed unchanged throughout the
payment and reported to the Creditor.
note: if the Debtor has not provide an end-to-end identifier, the Debtor Agent may populate
“NOTPROVIDED” to comply the mandatory
need of this element.
End to End
Identification
Min 1 – Max 1
the end-to-end Transaction Reference created using the UUIDv4
standard. This reference must be passed unchanged throughout
the payment, it may also be created by the Debtor within their
Payment Initiation request, and also included in reporting
messages.
UETR
Min 1 – Max 1
201

Payment
Identification
$
pgyppy py
Credit Transfer Transaction Info’ Payment Identification
an end-to-end reference assigned by the first Instructing
Agent to identify the transaction.
Transaction
Identification
Min 0 – Max 1
a point-to-point reference populated by a Payment
Market Infrastructure, typically to the settlement leg of a
clearing system transaction as a reference to the settled
clearing transaction.
Clearing 
System 
Reference
Min 0 – Max 1
202

Payment
Type 
Information
i
Credit Transfer Transaction Info’ Payment Type Info’
A nested element which may either use an external ISO
Service Level code or a proprietary code. It is used to
identify a particular agreed* service level which should
be applied to the payment.
For example, code G001 can be used to identify a gpi Tracked
Customer Credit Transfer similarly to Field 111 value 001 in the
MT 103
Service
Level 
Min 0 – Max 3
A nested element which may either use an
external ISO Local Instrument code or a
proprietary code. It is used to identify the
type of payment local instrument such as a
Standing Order.
Note: the ISO instrument codes are
registered by specific community
group (captured in the code list)
Local 
Instrument 
Min 0 – Max 1
A nested element which may either use an external ISO
Category Purpose code or a proprietary code. It is used to
identify the category of payment. For example, SECU
Transactionis the payment of securities.
Category 
Purpose 
Min 0 – Max 1
Clearing
Channel
Min 0 – Max 1
a choice of imbedded
codes representing
the clearing channel
to be used to process
the payment.
e.g., RTGS
203
a choice of imbedded
codes representing the
urgency considered by
the Instructing Agent,
this point-to-point
Instruction 
Priority 
Min 0 – Max 1
information may be used by the 
Instructed Agent to differentiate 
the processing priority.
*note - where a service level is not bilaterally agreed, it may be ignored.

Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important 
one. Instructed Amount relates to the amount Instructed to be executed from the Debtor’s account 
and only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not 
the same currency amount. 
£
$
¥
Credit Transfer Transaction Information
Interbank Settlement Date 
Interbank Settlement Amount 
Min 1 – Max 1 Min 1 – Max 1
204
A mandated currency amount moved between the Instructing Agent and the Instructed Agent. This
therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A
Interbank
Settlement
Amount
Interbank
Settlement
Date
A mandated date on which the Interbank Settlement should be executed between the
Instructing Agent and the Instructed Agent. This therefore is the value date comparable with
the MT Field 32A

of the instructions. 
Credit Transfer Transaction Information
205
Min 0 – Max 1
Min 0 – Max 1
The Settlement Priority provides an optional choice of embedded codes to indicate the instruction’s 
settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by 
the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused 
with the Instruction Priority. 
Note: where Settlement Method of the pacs.008 is ‘COVE’ (settled via a covering pacs.009 COV)
SettlementPriority is relevant to the covering payment not the pacs.008
Min 0 – Max 1
The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator 
such as a Market Infrastructure. 
This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time. 
The Settlement Time Request optionally captures the time settlement is requested for the payment instruction 
by the Instructing Agent. This Time can be capture in four nested elements:
• CLS Time the time the amount must be credit to CLS Bank
• Till Time the time until which the payment may be settled
• From Time the time from which the payment may be settled
• Reject Time the time from which the payment must be settled (to avoid reject)

206
Note: a number of Cross Element Rules exist which relate to the Instructed 
Amount element. For example if the Instructed Amount is present and the 
currency is different from the currency in Interbank Settlement Amount, 
then Exchange Rate must be present.
The Instructed Amount captures currency and amount instructed by the Debtor. This conditional
element is required when the Interbank Settlement Amount is not the same currency and/or
amount as originally instructed by the Debtor. For example, a charge is taken, or the transactions is
converted to another currency. This element is comparable with the legacy Field 33B.
The Exchange Rate capture the factor (rate) used to convert an amount from one currency into 
another. This reflects the currency pair price at which one currency was bought with another 
currency.
Min 0 – Max 1
Min 0 – Max 1
$100
£
¥ As a best practice to provide consistency and transparency the Exchange Rate used to convert the 
Instructed Amount (base currency) to the Interbank Settlement Amount (quote currency) should use the 
Instructed currency as the whole unit to perform the exchange. 
For example if Instructed Amount currency is CAD and the Interbank Settlement currency is USD the 
rate should reflected as 0.83 (CAD 1 equals USD 0.83)
Credit Transfer Transaction Information
Instructed Amount
Exchange Rate

y gpg pyp
with MT Field 71A ‘Details of Charges’
71A: Details 
of Charges 
Code Description
BEN Beneficiary
OUR Our Customer Charges
SHA Shared Charges
Charge 
Bearer
(1.1)
Code Description
CRED Creditor
DEBT Debtor
SHAR Shared
SLEV Service Level
Note: Charge Bearer codeSLEV applies following rules agreed as part of a bilateral agreed Service Level 
or as part of a scheme (commonly used in Instant Payment schemes) This code has no equivalent in legacy 
MT messages. SLEV is removed from CBPR+ usage guideline specifications for the beginning of the 
coexistence period.
Credit Transfer Transaction Info’ Charge Bearer
207

Charge 
Information
(0.*)
Amount
Currency
Agent BICFI
Name
StructuredPostal Address
pgg
In addition to the legacy MT message the pacs.008 Charge
Information mandate the Agent, this represent the Agent for
who the Charges are either; due (pre-paid charges) or has
taken a charge (deduct from the transaction)
CBPR+ best practice recommends the use of the
structured Agent BIC.
Note: As the Charge Information element has the capability to capture both charges deducted and charges 
included i.e. pre-paid charges, the use of the Interbank Settlement Amount and Instructed Amount elements 
play an important role. 
Also note: If Charge Bearer DEBT is provided only one optional occurrence of pre-paid charges is allowed.
Deducted Charges are not appropriate with Charge Bearer DEBT. 
As the Charges Information element is repetitive it can capture charges related to previous legs of the 
payment transaction.
Credit Transfer Transaction Info’ Charge Information
208

2
pacs.008
3
pacs.008 pacs.008
A B C D
1
Debtor requests a payment for 
USD 100 specifying the 
charges should be shared
1
Debtor Agent executes the USD 
100 payment charging the 
Debtor as commercially agreed. 
2
Agent B processes the 
payment deducting their fee of 
USD 10 
3
4
Agent C processes the 
payment deducting their fee of 
USD 5
4
209

2
pacs.008
3
pacs.008 pacs.008
A B C D
1
Debtor requests a 
payment for USD 100 
specifying any charges 
will be borne by them, 
in accordance with their
banking agreement.
1
Debtor Agent executes the USD 100 
payment including a previous negotiated 
pre-payment of charges (USD 30). The 
Debtor is debited for USD 100 plus the 
Charges in accordance with their 
account agreement.
2
Agent B identifies the pre-payment of 
charges by the inclusion of their BIC in the 
Charge Information Agent element. 
Removing charge (USD 30), they forward 
the payment to the next Agent. The next 
Agent many request a charge.
3
Pre-payment of 
charges are identified 
by the instructed Agent 
by the inclusion of their 
BIC in the Charge 
Information Agent 
element of the payment 
message they receive pre-payment of charge versus 
bearing the cost of claimed charges, 
may be various combinations 
210

2
pacs.008
3
pacs.008 pacs.008
A B C D
1
Debtor requests a 
payment for USD 100 
specifying any charges 
will be taken by them, in 
accordance with their
banking agreement.
1
Debtor Agent executes the USD 100 
payment including a previous negotiated 
pre-payment of charges (USD 30). The 
Debtor is debited for USD 100 plus the 
Charges in accordance with their 
account agreement.
2
Agent B identifies the pre-payment of 
charges by the inclusion of their BIC in the 
Charge Information Agent element. 
Removing charge (USD 30), they forward 
the payment, including USD 20 of pre-payment of charges of the next Agent. 
3
Agent C identifies the pre-payment of charges 
by the inclusion of their BIC in the Charge 
Information Agent element. Removing this 
pre-payment of charges they forward the 
payment to the Next Agent and indicate they 
will bear the cost of any charge claims.
4
4
Pre-payment of 
charges are identified 
by the instructed Agent 
by the inclusion of their 
BIC in the Charge 
Information Agent 
element of the payment 
message they receive pre-payment of charge versus 
bearing the cost of claimed charges, 
may be various combinations

of ChargesInformation/ChargesAmount is recommended to be the same as the currency of 
InterbankSettlementAmount”
Interbank Settlement 
Amount received
Interbank Settlement 
Amount forwarded
Currency of Charge 
Information (where a 
charge occurs)
USD USD USD
USD EUR EUR
ISO 20022 does not prevent Charges from being booked in a different currency, but for
transparency the Charge should be represented within the Charge Information in the
Interbank Settlement Amount Currency.
Credit Transfer Transaction Info’ Charge Information
212

2
pacs.008
3
pacs.008 pacs.008
A B C D
1
Debtor requests a payment for GBP
100 to be initiated from their USD 
account, specifying the charges should 
be borne by the Creditor
1
Debtor Agent executes a payment for 
GBP 95 (GBP 100 minus a 5 GBP charge 
deducted as this is borne by the Creditor.
2
Agent B processes the payment 
deducting their fee of GBP 10 
3
213

Credit Transfer Transaction Information
214
The Previous Instructing 2 captures the second Previous Instructing Agent between the Previous Instructing
Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element
is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Previous Instructing 2 Account captured the account related between this Agent and Previous
Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in
the legacy FIN message.
The Previous Instructing Agent 1 captures the first historic Agent between the Debtor Agent and the Previous
Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the
Field 72 first /INS/ occurrence in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Previous Instructing 1 Account captured the account related between this Agent and Previous
Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in
the legacy FIN message
The Previous Instructing 3 captures the third Previous Instructing Agent between the Agent and the
Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN
message.
Min 0 – Max 1
Min 0 – Max 1
The Previous Instructing 3 Account captured the account related between this Agent and Previous
Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in
the legacy FIN message

pacs.008
Instructing pacs.008
Agent: Agent A
Instructed
Agent: Agent B
Instructing
Agent: Agent B
Instructed
Agent: Agent C
Instructing Agent and Instructed Agent
represent the Agents involved in the pacs 
point-to-point message exchange. These 
roles therefore change on each payment 
leg.
A B C D
Instructing Agent and Instructed Agent elements are required in all pacs messages
and are only available in the Credit Transfer Information Credit Transfer Transaction Information
Instructing Agent
Instructed Agent
215

A B C D E
Instructing Agent & 
Debtor Agent
Debtor Instructed Agent Intermediary Agent 1 Intermediary Agent 2 Creditor Agent Creditor
Debtor Agent Creditor Agent & 
Instructed Agent
Debtor Creditor Previous Instructing 
Agent 1
Instructing Agent Previous Instructing 
Agent 2
Debtor Debtor Agent Instructing Agent Instructed Agent Intermediary Agent 1 Creditor Agent Creditor
Debtor Debtor Agent Creditor Agent Creditor Previous Instructing 
Agent 1 Instructing Agent Instructed Agent
pyy gp, g(y g
1) Previous Instructing Agent however is a static role which allows additional Previous Instructing Agent to be appended to
the history of the payment.
The below diagram visualizes the change ofAgent role at different stages of the payment transaction life cycle.
Note: the statics roles of Previous Instructing Agent transition into
Intermediary Agents in the potential return chain (refer to the pacs.004
section for Payment Returns)
216

Credit Transfer Transaction Information
217
The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the
CreditorAgent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.
The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent
for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the
Field 56a in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the
Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.
The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the
Creditor Agent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 3 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 2. This optional element has not comparable field in the legacy FIN message.
1
2
3
Note: should all Previous Instructing Agents (1, 2 and 3) be utilised, Intermediary
Agent should not be used.A direct and cover message would be needed instead.

1 2
pacs.008
A B C D
Interbank Settlement 
Amount
USD 100
Debtor Agent executes the 
payment using their Headquarters 
as the settlement account
1
Interbank Settlement 
Amount
USD 100
Agent B processes the payment debiting the 
account of Agent A Headquarters, and including 
them as the Previous Instructing Agent in the 
payment transaction.
2
218
(Agent A) may be given Debit Authority to instruct payment from their Headquarters (Agent HQ) account with its currency
correspondent (Agent B). In much the same way as if this had occurred serially, it is important that the payment instructed by
Agent B correctly reflectAgent HQ as anAgent participating in the transaction, particularly if the payment is returned.
Settlement Account Id 12345
Debtor Agent AAAAGB2LABC
Settlement Account 12345
Debtor Agent AAAAGB2LABC
Previous Instructing 
Agent 1
AAAAGB2L
pacs.008 pacs.008
HQ
A
For transparency purpose Agent C (in
this use case) has a responsibility to
ensure the Agent associated with the
Settlement Account is captured in the
next payment leg as a Previous
Instructing Agent. This also ensures,
should a Payment Return occur, all
the Agents can be correctly reflected
in the Return Chain.

➢ CBPR+ premise is that an Ultimate Debtor has no financial
regulated direct account relationship with the corresponding Debtor.
➢ CBPR+ premise is that an Ultimate Creditor has no financial 
regulated direct account relationship with the corresponding 
Creditor.
Ultimate Debtor element should not be confused with an Initiating Party who may send a payment initiation
request on behalf of the Debtor. (see dedication section on Initiating Party)
Note: Ultimate Debtor and Ultimate Creditor are removed 
from the pacs.009 Financial Institution Credit Transfer.
Ultimate
Party
Ultimate
Creditor
Ultimate
Debtor
Credit Transfer Transaction Information
Ultimate Creditor
Ultimate Debtor
Min 0 – Max 1
Min 0 – Max 1
219
An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not 
bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a 
payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor 
depending on the payment scenario)

1
Ultimate Debtor requests a 
payment to be initiated on their 
behalf to the Creditor
3
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
pacs.008
3
equess a payeo be pad oebeao a Cedoag acceped payeoe asaco, e
Money Transfer Bureau executes a payment initiation request to their Agent (Bank) as the Debtor, on behalf of
the individual who is represented as the Ultimate Debtor.
pacs.008 pacs.008
2
2
Debtor requests a payment to 
be initiated on behalf of the 
Ultimate Debtor to the Creditor
1
A B C D
220

2
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
pacs.008
2
facility is the Creditor of the payment transaction, whereby the resident of the facility is represented as the
Ultimate Creditor (beneficiary of the services the fee is paying for)
pacs.008 pacs.008
1
1
Debtor initiates a payment 
instruction to the Debtor Agent
A B C D
221

g y py
therefore this optional element is not necessary. More often the Initiating
Party is a third party providing payment initiation services on behalf of the
Debtor (often referred to as a Third Party Provider) whereby the Debtor
maintains an account with the Debtor Agent but the Third Party Provider has
authority to initiate payment on behalf of the Debtor. This is distinctly
different from an Ultimate Party (such as Ultimate Debtor) who instructs the
Debtor to initiate a payment on their behalf.
In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the Initiating Party is often the
Creditor, however the same context of a Third Party Provider can exist where the third party is responsible
for collecting funds on behalf of the Creditor.
A
Debtor Agent
g y
Debtor Third Party
Credit Transfer Transaction Info’ Initiating Party
222

Debtor in greater detail. 
Debtor
Identification
Nested element capturing the 
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
address details
Credit Transfer Transaction Info’ Debtor 223

224
applied to the Debtors account, which are also reflected in their account Statement.
The Debtor Account uses a variety of nested elements to capture information related to 
the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account
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

Debtor Name JOHN HECTOR 
JOSEPH SMITH -
MASTERSONS
:50K:/BE3000121637141
JOHN HECTOR JOSEPH SMITH - MASTERSO 
HOOGSTRAAT 6 BRUSSELS 1000 BELGIUM
PASSPORT 1111111111
Postal 
Address
Department
Sub Department
Street Name HOOGSTRAAT
Building Number 6
Post Code 1000 MT – structured option with risk of potential truncation & loss of info
Town Name BRUSSELS :50F:/BE3000121637141
1/JOHN HECTOR JOSEPH SMITH - MASTER
1/SONS
2/HOOGSTRAAT 6
3/BE/BRUSSELS 1000
Country BE
Identification Private
Id
Other Id 1111111111
Scheme 
Name
Code CCPT
Debtor 
Account
Identification IBAN BE3000121637141
Note: The richness of ISO 20022 allows more granular data 
structures compared to the legacyFIN formatting options 225

These agent maintain a relationship with their customers; the Debtor and Creditor. 
Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the
pacs messages, the description of these parties change in the reporting messages (camt) where the
Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor
become the Statement Account Owner. This will be explored further in the camt Cash Management
Reporting section.
Credit Transfer Transaction Information
Debtor Agent
Creditor Agent
226

227
information related to these Agents. The nature of this element implies there is an Agent or Agent in 
between the Debtor Agent and Creditor Agent in the payment transaction.
The Debtor Agent Account and Creditor Agent Account uses a variety of nested 
elements to capture information related to the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identificationidentifies the account maintained at theAccount Servicing Institution
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account
Name identifies the name of the account as assigned by the Account Servicing
Institution
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Debtor Agent and Creditor Agent are a Financial Institution, therefore
the nested elements Name and Proxy are unlikely to be used.

the Creditor in greater detail.
Creditor
Country of 
Residence
Optional element to 
capture the Creditor’s ISO 
country code of residence 
Identification
Nested element capturing the 
various types of identifiers for 
the party e.g. BIC, LEI etc.
Postal 
Address
Nested element capturing either 
structured or unstructured Creditor
address details
Credit Transfer Transaction Info Creditor
228

229
intended to be applied to the Creditors account, which are also reflected in their account Statement.
The Creditor Account uses a variety of nested elements to capture information related to 
the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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

230
information related to these Agents. The nature of this element implies there is an Agent or Agent in 
between the Debtor Agent and Creditor Agent in the payment transaction.
The Debtor Agent Account and Creditor Agent Account uses a variety of nested 
elements to capture information related to the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identificationidentifies the account maintained at theAccount Servicing Institution
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account
Name identifies the name of the account as assigned by the Account Servicing
Institution
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Debtor Agent and Creditor Agent are a Financial Institution, therefore
the nested elements Name and Proxy are unlikely to be used.

Agents.
Credit Transfer Transaction Information
Instruction for Creditor Agent
Instruction for Next Agent
The Instruction for Creditor Agent element offers a multiplicity of up to 2 occurrences of 
information. This element enables:
➢ the use of 2 embedded codes to describe the instruction
➢ free format instruction information
➢ or both, where the free format complements the code.
The use of this element may be bilaterally agreed with the Creditor Agent. It must be passed 
on throughout the life cycle of the transaction until the payment reaches the Credit Agent.
Min 0 – Max 2
The Instruction for Next Agent element offers a multiplicity of up to 6 occurrences of 
information. This element is restricted to free format instruction information in CBPR+. 
The element is used to provide instruction to the next Agent (which may not be the Creditor
Agent)
Min 0 – Max 6
231

The purpose is used to capture the nature of the payment e.g. IVPT Invoice Payment, FEES Payment of Fees
etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically
defined by the Debtor.
Credit Transfer Transaction Information
Purpose
The externalised Purpose code set is classified by the purpose, for example commercial, for 
which the numerous codes within the classification are each described by Name and 
Definition.
For example: GDSVis classified within the Commercial categorisation, with the Name
Purchase Sale of Goods and Services described as a Transaction is related to purchase and 
sale of goods.
232
Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger
special processing e.g. Category Purpose code SALA ‘Salary Payment’ may trigger a reporting process
which restricts sensitive data i.e., individual salary names.

Credit Transfer Transaction Information Regulatory Reporting
Debit Credit Reporting Indicator
Authority
Details
The Debit Credit Reporting Indicator utilises an embedded choice of code 
to indicate whether the regulatory reporting information applies to the:
• DEBT (debit)
• CRED (credit) or 
• BOTH
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max *
The Authority element captures the Name and Country code of the 
Authority/Entity requiring the regulatory reporting information.
The Details element provides the detail on the regulatory reporting 
information.
233

the Debtor in the payment initiation request.
Credit Transfer Transaction Info’ Related Remittance Information
Remittance Identification
Remittance Location Details
Remittance advices are typically considered as a traditional value added service provided by the Debtor Agent to the Debtor, in order to
provide Remittance Information to the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting
messages.
Remittance Information is a dedicated element used both within the pacs and camt reporting messages, whereby this information can
travel end-to-end using ISO 20022. Related Remittance Information and Remittance Information are mutually exclusive (can’t both be
present)
Business examples are emerging where information is externalised using a URL repository solution.
The Remittance Identification captures a unique reference assigned by the initiating party of the payment to
identify the remittance information sent separately from the payment instruction.
The Remittance Location Details uses a set of nested elements to provide information on either the location
of or the delivery of remittance information.
• Method requires a code from an embedded list to detail the method used to deliver the remittance
advise information e.g. EMAL (email)
• Electronic Address provides an electronic address for which an agent is to send the remittance
information to e.g. the email address. It may also reference a URL where remittance information may
be deposited or retrieved.
• Postal Address provides the postal address to which an agent is to send the remittance information
Min 0 – Max 1
Min 0 – Max 2
234

Credit Transfer Transaction Info’ Remittance Information
Structured
Unstructured
Remittance Information enable the matching/reconciliation of an entry that the payment 
is intended to settle
Min 0 – Max 1
The Unstructured sub element captures free format Remittance Information which 
is restricted in CBPR+ to 140 characters to ensure backward compatibility with the 
legacy MT message during coexistence. 
Min 0 – Max 1
The Structured element is nested capturing rich structured Remittance Information, 
and is unlimited in its multiplicity, but must not exceed 9,000 characters of business 
information (does not include the xml element identification) 
The use of this nested element should be bilaterally/multilaterally agreed, to ensure 
end-to-end transportation of this data.
Min 0 – Max *
235
Related Remittance Informationand Remittance Information are 
mutually exclusive (can’t both be present)

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
Information and it nested elements has
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
236

g
Serial Financial Institution to Financial Institution to Customer Credit Transfer 
Use Case p.8.1.1 – High Level FI to FI Customer Credit Transfer (pacs.008) settled over a Payment Market Infrastructure
Use Case p.8.1.2 – High Level FI to FI Customer Credit Transfer (pacs.008) Sweeps (Short position at the Secondary Account)
Cover Method Financial Institution to Financial Institution to Customer Credit Transfer 
Use Case p.8.2.1 - High Level FI to FI Customer Credit Transfer settled using the cover method (pacs.009 COV) over a Payment Market 
Infrastructure
Use Case p.8.2.2 - High Level FI to FI Customer Credit Transfer involved a serial leg into a cover method (pacs.009 COV)
Use Case p.8.2.3 - High Level FI to FI Customer Credit Transfer involved a serial leg in and out of a cover method (pacs.009 COV)
Use Case p.8.2.4 - High Level FI to FI Customer Credit Transfer involved a serial leg out of a cover method (pacs.009 COV)
237

Agent D credits the account of the 
Creditor, and may optionally 
provide a notification e.g. credit 
notification in addition to an 
account statement (camt.053).
pacs.008
pacs.002
1
1
Debtor initiates a payment 
instruction to the Debtor Agent.
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as 
intermediaries, who are direct 
participants of the Payment 
Market Infrastructure.
3
Agent B processes the payment 
on Agent C, via the Payment 
Market Infrastructure.
4
Payment Market Infrastructure, 
settles the payment between Agent 
B and Agent C as direct 
participants of the Market 
Infrastructure, and provides a 
settlement confirmation to Agent B.
pacs.008 pacs.008 pacs.008
pacs.002 pacs.002
2
2 3 4 5
Settlement 
Complete
6
5
Agent C processes the payment 
onto Agent D.
6
A B C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
238

239
See use case pn.1.2.1 for an Authorised Party 
Payment.
As a pre-requisite the Debtor 
provides Debit Authorisation to 
Agent I to Initiate Payment from 
their account with the Debtor 
Agent (A)
pacs.008
I B
Interbank pain.001
Interbank pain.002
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
2
2

Agent C produces an end of day 
account statement report. An 
optional real time notification e.g. 
advice of credit may have also been 
created at the time of the credit 
posting
Agent C receives the payment and 
credits the account of Agent D
Agent B processes the payment 
on Agent C, via the Payment 
Market Infrastructure.
pacs.002
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover method 
to the Creditor Agent (D)
2a
2b
2b
In parallel the Debtor Agent (A) 
initiates a covering payment to 
credit the account of Agent (D) 
with their correspondent (Agent 
C)
3
5
6
6
3 4
pacs.009 cov
Settlement 
Complete
pacs.002
Agent D reconciles the covering 
funds and credits the account of the 
Creditor, and may optionally 
provide a notification e.g. credit 
notification.
7
Payment Market Infrastructure, 
settles the payment between Agent 
B and Agent C as direct 
participants of the Market 
Infrastructure, and provides a 
settlement confirmation to Agent B
4
5
A D
B C
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
240

Agent E receives the payment 
instruction and credits the account of 
the Creditor, and may optionally 
provide a notification e.g. credit 
notification. Alternatively, they may 
have chosen to await until settlement 
occurred in Step 6 based upon their 
risk appetite.
Agent C processes the payment on 
Agent D, using a correspondent 
banking business relationship
pacs.002
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the serial method 
towards the Creditor Agent (E)
2
3a
3b
In parallel the Agent (B) initiates a 
covering payment to credit the account 
of Agent (E) with their correspondent 
(Agent D)
3b
5
pacs.002
5
A E
C
Note settlement of step 5 could alternative occur between Agent C and D using a 
Market Infrastructure..
241
B
pacs.008
pacs.002
D
Agent B initiates a payment 
using the cover method towards 
the Creditor Agent (E) by 
sending a direct pacs.008 to 
Agent E who they have business 
relationship with.
Agent D receives the payment and 
credits the account of Agent E. 
Agent D produces an end of day 
account statement report. An 
optional real time notification e.g. 
advice of credit may have also been 
created at the time of the credit 
posting
6
6
4

Agent E receives the payment 
instruction and process the payment 
on to Agent F. Alternatively they may 
have chosen to await until settlement 
occurred in Step 6 based upon their 
risk appetite.
Agent C processes the payment on 
Agent D, using a correspondent 
banking business relationship
pacs.002
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the serial method 
towards the Creditor Agent (F)
2
3a
3b
In parallel the Agent (B) initiates a 
covering payment to credit the account 
of Agent (E) with their correspondent 
(Agent D)
3b
5
pacs.002
Agent F receives the payment and 
credits the account of the Creditor, 
and may optionally provide a 
notification e.g. credit notification.
7
5
A E
C
Note settlement of step 5 could alternative occur between Agent C and D using a 
Market Infrastructure..
242
B
pacs.008
pacs.002
pacs.002 F
D
Agent B initiates a payment using 
the cover method towards the 
Creditor Agent (F) by sending a 
direct pacs.008 to Agent E who they 
have business relationship with.
Agent D receives the payment and 
credits the account of Agent E. 
Agent D produces an end of day 
account statement report. An 
optional real time notification e.g. 
advice of credit may have also been 
created at the time of the credit 
posting
6
6
4

Agent D receives the payment 
instruction and process the payment 
on to Agent E. Alternatively they may 
have chosen to await until settlement 
occurred in Step 6 based upon their 
risk appetite.
Agent B processes the payment on 
Agent C, using a correspondent 
banking business relationship
pacs.002
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
2a
2b
In parallel the Agent (A) initiates a 
covering payment to credit the account 
of Agent (D) with their correspondent 
(Agent C)
2b
5
pacs.002
Agent E receives the payment and 
credits the account of the Creditor, 
and may optionally provide a 
notification e.g. credit notification.
4
5
A D
Note settlement of step 5 could alternative occur between Agent B and C using a 
Market Infrastructure..
243
pacs.002 E
B
Debtor Agent (A) initiates a 
payment using the cover 
method towards the Creditor 
Agent (E) by sending a direct 
pacs.008 to Agent D who they 
have business relationship with.
Agent C receives the payment and 
credits the account of Agent D. 
Agent C produces an end of day 
account statement report. An 
optional real time notification e.g. 
advice of credit may have also been 
created at the time of the credit 
posting
6
6
3
C

Financial Institution to 
Financial Institution 
Customer Credit Transfer
244

pacs.008
Group Header
Credit Transfer 
Transaction Information
nested elements:
• Group Header which contains a 
set of characteristics that relates to 
all individual transaction
• Credit Transfer Transaction 
Information which contains 
elements providing information 
specific to the individual credit 
transfer transaction. 
245
Payment messages in a many-to-many payment are considered as a 
single transaction. The pacs.008 STP is a message who’s Usage 
Guideline has been further restricted by remove elements considered 
to inhibit Straight Through Processing (STP)

pacs.008 STP
pacs.008 STP
pacs.008 STP
pacs.002
pacs.002
pacs.002
A B C D
246
The Financial Institution To Financial Institution Customer 
Credit Transfer message is sent by the Debtor Agent to 
the Creditor Agent, directly or through other agents and/or 
a payment clearing and settlement system. 
It is used to move funds from a Debtor account to a 
Creditor, whereby one or both of these Parties should be 
a non-Financial Institution.

247
swift.cbprplus.02 swift.cbprplus.stp.02
Addition Debtor and Creditor 
IBAN rules
Account mandatory
Instruction for Next Agent removed
Instruction for Creditor Agent removed
Business Application Header
Business Service
Credit Transfer Transaction Information
Previous Instructing Agent 1
Previous Instructing Agent 2
Previous Instructing Agent 3
Intermediary Agent 1
Intermediary Agent 2
Intermediary Agent 3
Debtor Agent
Creditor Agent
Debtor 
Creditor
Creditor Account
Instruction for Next Agent
Instruction for Creditor Agent
Purpose
Remittance information
pacs.008 pacs.008
STP
Financial Institution identifiers:
• BIC
• Clearing System Member Id
• LEI
• Name
• Postal Address
Financial Institution identifiers:
• BIC
• Clearing System Member Id
• LEI
Name removed
Postal Address removed
Account optional
Elements optional
ISO Code or Proprietary
Unstructured or Structured Unstructured only (structured removed)
ISO Code or Proprietary removed

Financial Institution 
Credit Transfer
248

pacs.009
Group Header
Credit Transfer 
Transaction 
Information
pacs.009 (COV)
Group Header
Credit Transfer 
Transaction 
Information
Underlying 
Customer Credit 
Transfer
• as a core Financial Institution 
Credit Transfer message. 
• As a COV where it is used as cover 
of (to settle) a pacs.008.
The pacs.009 therefore contain 
information of the underlying Customer 
Credit Transfer (pacs.008) for use in 
the cover scenario, which is the key 
attribute to differentiate between these 
two use cases.
The pacs.009 may also be used as a 
ADV where it is sent as an advice and 
is settled using the pacs.009 as a core 
message.
249

pacs.009
pacs.009
camt.053
pacs.002
pacs.002
A B C D
The Financial Institution Credit Transfer message is sent by a Debtor 
Financial Institution to a Creditor Financial Institution, directly or 
through other agents and/or a payment clearing and settlement 
system. It is used to move funds from a debtor account to a creditor, 
where both Debtor and Creditor are Financial Institutions.
250

251

pygg, 
Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact
equivalent in the legacy MT payment message. However, the MT 202 Sender’s Reference (Field
20) could be considered a similar comparison where a pacs message contains a single
Transaction.
Each transaction’s Credit Transfer Transaction Information contains a variety of nested
Payment Identification elements to capture reference related to the individual transaction such
as a UETR (Unique End-to-endTransactionReference)
Group Header Message Identification
252

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
253

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 
Group Header Number of Transactions
254
g
Single transactions in the CBPR+ payment usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant payments, supporting the next
generation of innovation.

Group Header Settlement Information Settlement Method
D
27
255
The Settlement Method element in the pacs.009 allows a choice of an embedded code.
INDA indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account 
Servicing Institution) The account held at the Instructed Agent may captured in the dedicated Settlement 
Account element.
INGA indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who 
has credited the Account they service for the Instructed Agent (as an Account Owner). The account held 
by the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account 
element.
$
€
Settlement Method code CLRG is not part of CBPR+ specifications but instead used in 
Market Infrastructure specification (HVPS+)

Group Header Settlement Information
256
The Settlement Account identifies the account details maintained at the account
servicing institution (Agent responsible for the settlement of the instruction as
indicated in the Settlement Method)
Min 0 – Max 1
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
Name identifies the name of the account as assigned by the Account Servicing
Institution
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

257

Payment
Identification
$
y 
Credit Transfer Transaction Info’ Payment Identification
a point-to-point reference restricted in CBPR+ to 16 character
and directly comparable with the Sender’s Reference (Field
20) of the legacy MT payment message.
Instruction
Identification
Min 1 – Max 1
an end-to-end reference provided by the Debtor which must
be passed unchanged throughout the payment and reported
to the Creditor.
note: for a pacs.009 COV the end-to-end id is provided
by the Debtor from the pacs.008 Instruction id.
In a pacs.009 COR if the Debtor has not provide an
end-to-end identifier, the Debtor Agent may populate
“NOTPROVIDED” to comply the mandatory need of this
element.
End to End
Identification
Min 1 – Max 1
the end-to-end Transaction Reference created using the UUIDv4
standard. This reference must be passed unchanged throughout
the payment, it may also be created by the Debtor within their
Payment Initiation request, and also included in reporting
messages.
UETR
Min 1 – Max 1
258

Payment
Identification
$
pgyppy py
Credit Transfer Transaction Info’ Payment Identification
an end-to-end reference assigned by the first Instructing
Agent to identify the transaction.
Transaction
Identification
Min 0 – Max 1
a point-to-point reference populated by a Payment
Market Infrastructure, typically to the settlement leg of a
clearing system transaction as a reference to the settled
clearing transaction.
Clearing 
System 
Reference
Min 0 – Max 1
259

Payment
Type 
Information
i
Credit Transfer Transaction Info’ Payment Type Info’
A nested element which may either use an external ISO
Service Level code* or a proprietary code. It is used to
identify a particular agreed service level which should be
applied to the payment.
For example, code G001 can be used to identify a gpi Tracked
Cover Transfer similarly to Field 111 value 001 in the MT 202
COV
Service
Level 
Min 0 – Max 3
A nested element which may either use an
external ISO Local Instrument code or a
proprietary code. It is used to identify the
type of payment local instrument such as a
Standing Order.
Note: the ISO instrument codes are
registered by specific community
group (captured in the code list)
Local 
Instrument 
Min 0 – Max 1
A nested element which may either use an external ISO
Category Purpose code or a proprietary code. It is used to
identify the category of payment. For example, SECU
Transactionis the payment of securities.
Category 
Purpose 
Min 0 – Max 1
Clearing
Channel
Min 0 – Max 1
a choice of imbedded
codes representing
the clearing channel
to be used to process
the payment.
e.g., RTGS
260
Instruction 
Priority 
Min 0 – Max 1
a choice of imbedded
codes representing the
urgency considered by
the Instructing Agent,
this point-to-point
information may be used by the 
Instructed Agent to differentiate 
the processing priority.
*note - where a service level is not bilaterally agreed, it may be ignored.

A mandated currency amount moved between the Instructing Agent and the Instructed Agent.
This therefore is the point-to-point currency amount exchanged, comparable with the MT Field
32A
Note: the Financial Institution Credit Transfer (pacs.009) has no Instructed Amount
element, Exchange Rate or Charger Bearer (unlike the pacs.008) as the Instructed 
Settlement Amount is expected to be transferred across the end-to-end payment chain 
without any charges being applied or currency conversions.
Interbank
Settlement £ Amount
$
¥
Credit Transfer Transaction Information
Interbank Settlement Amount 
Min 1 – Max 1
261
Interbank
Settlement
Date
A mandated date on which the Interbank Settlement should be executed between the
Instructing Agent and the Instructed Agent. This therefore is the value date comparable with
the MT Field 32A
Min 1 – Max 1

of the instructions. 
Credit Transfer Transaction Information
262
Min 0 – Max 1
Min 0 – Max 1
The Settlement Priority provides an optional choice of embedded codes to indicate the instruction’s 
settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by 
the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused 
with the Instruction Priority. 
Note: Where the Settlement Method of the pacs.009 is ‘INDA’ (settled performed by the Instructed
Agent) this indicates the Settlement Priority. Code ‘INGA’ implies settlement has already occurred
for this point-to-point payment and therefore the Settlement Priority is not necessary.
Min 0 – Max 1
The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator 
such as a Market Infrastructure. 
This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time. 
The Settlement Time Request optionally captures the time settlement is requested for the payment instruction 
by the Instructing Agent. This Time can be capture in four nested elements:
• CLS Time the time the amount must be credit to CLS Bank
• Till Time the time until which the payment may be settled
• From Time the time from which the payment may be settled
• Reject Time the time from which the payment must be settled (to avoid reject)

Credit Transfer Transaction Information
Debtor Agent and Creditor Agent elements must be present before the previous 
Instructing Agent 1 element can be used 263
The Previous Instructing Agent 2 captures the second Previous Instructing Agent between the Previous
Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This
optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Previous Instructing Agent 2 Account captured the account related between this Agent and Previous
Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in
the legacy FIN message.
The Previous Instructing Agent 1 captures the first historic Agent between the Debtor Agent and the Previous
Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the
Field 72 first /INS/ occurrence in the legacy FIN message.
Min 0 – Max 1
The Previous Instructing Agent 1 Account captured the account related between this Agent and Previous
Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in
the legacy FIN message
The Previous Instructing Agent 3 captures the third Previous Instructing Agent between the Agent and the
Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN
message.
Min 0 – Max 1
Min 0 – Max 1
The Previous Instructing Agent 3 Account captured the account related between this Agent and Previous
Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in
the legacy FIN message

pacs.009
Instructing pacs.009
Agent: Agent A
Instructed
Agent: Agent B
Instructing
Agent: Agent B
Instructed
Agent: Agent C
Instructing Agent and Instructed Agent
represent the Agents involved in the pacs 
point-to-point message exchange. These 
roles therefore change on each payment 
leg.
A B C D
Instructing Agent and Instructed Agent elements are required in all pacs messages 
and are only available in the Credit Transfer Information Credit Transfer Transaction Information
Instructing Agent
Instructed Agent
264

Instructing Agent & 
Debtor Agent
Debtor Instructed Agent Intermediary Agent 1 Intermediary Agent 2 Creditor Agent Creditor
Debtor Agent Creditor Agent & 
Instructed Agent
Debtor Creditor Previous Instructing 
Agent 1
Instructing Agent Previous Instructing 
Agent 2
Debtor Debtor Agent Instructing Agent Instructed Agent Intermediary Agent 1 Creditor Agent Creditor
Debtor Debtor Agent Creditor Agent Creditor Previous Instructing 
Agent 1 Instructing Agent Instructed Agent
pyy gp, g(y g
1) Previous Instructing Agent however is a static role which allows additional Previous Instructing Agent to be appended to
the history of the payment.
The below diagram visualizes the change ofAgent role at different stages of the payment transaction life cycle.
Note: the statics roles of Previous Instructing Agent transition into
Intermediary Agents in the potential return chain (refer to the pacs.004
section for Payment Returns)
A B C D E F G
265

Credit Transfer Transaction Information
266
The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the
CreditorAgent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.
The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent
for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the
Field 56a in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the
Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.
The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the
Creditor Agent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 3 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 2. This optional element has not comparable field in the legacy FIN message.
1
2
3
Debtor Agent and Creditor Agent elements must be present before the Intermediary 
Agent 1 element can be used

elements describe the Debtor in greater detail. 
Debtor
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
Credit Transfer Transaction Info’ Debtor 267
Legal entity identifier of the LEI
financial institution.
The Debtor of the pacs.009 where used to settle a pacs.009 ADV remains 
the original Debtor of the pacs.009 ADV to provide party transparency.

268
been applied to the Debtors account, which are also reflected in their account Statement.
The Debtor Account uses a variety of nested elements to capture information related to 
the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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
the pacs.009 the Debtor is a Financial Institution, therefore the nested
elements Name and Proxy are unlikely to be used.

These agent maintain a relationship with their customers; the Debtor and Creditor. However, unlike the 
pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and 
Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship. 
Note: Where the Debtor and Creditor maintain a relationship with the same intermediary counterpart. It
is recommended that this Agent is captured in the Creditor Agent element to align with translation from
the legacy MT message.
Credit Transfer Transaction Information
Debtor Agent
Creditor Agent
269

270
related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor 
Agent and Creditor Agent in the payment transaction.
The Debtor Agent Account and Creditor Agent Account uses a variety of nested 
elements to capture information related to the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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
Debtor Agent and Creditor Agent are a Financial Institutions, therefore
the nested elements Name and Proxy are unlikely to be used.

elements describe the Creditor in greater detail.
Creditor
Credit Transfer Transaction Info Creditor 271
Certain legacy MT messages, such as the MT 200, identify 
the Creditor from the message sender, whereas this party 
would need to be repeated in the pacs.009
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
LEI
Legal entity identifier of the 
financial institution.

272
intended to be applied to the Creditors account, which are also reflected in their account Statement.
The Creditor Account uses a variety of nested elements to capture information related to 
the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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
the pacs.009 the Creditor is a Financial Institution, therefore the
nested elements Name and Proxy are unlikely to be used.

Agents.
Credit Transfer Transaction Information
Instruction for Creditor Agent
Instruction for Next Agent
The Instruction for Creditor Agent element offers a multiplicity of up to 2 occurrences of 
information. This element enables:
➢ the use of 2 embedded codes to describe the instruction
➢ free format instruction information
➢ or both, where the free format complements the code.
The use of this element may be bilaterally agreed with the Creditor Agent. It must be passed 
on throughout the life cycle of the transaction until the payment reaches the Credit Agent.
Min 0 – Max 2
The Instruction for Next Agent element offers a multiplicity of up to 6 occurrences of 
information. This element is restricted to free format instruction information in CBPR+. 
The element is used to provide instruction to the next Agent (which may not be the Creditor
Agent)
Min 0 – Max 6
273
The Creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) Instruction 
for Creditor Agent, Instruction Information element preceded by /UDLC/ (UnDerLying Creditor) to provide 
party transparency in the settlement message.

in the advice message (Underlying Creditor).
274
pacs.009 Instruction for Creditor Agent/Instruction 
Information.
Up to 2 occurrences of Instruction Information may be 
provided. The last available occurrence of Instruction 
Information, preceded by /UDLC/, must be used to capture 
the Underlying Creditor provided in the pacs.009 ADV.
The Creditor of the pacs.009 ADV are commonly 
captured in one of the following ways:
• As a BIC (BICFI) either on its own, or 
• As a Clearing System Member Identification or a
LEI with Name, and Postal Address
pacs.009 ADV
Creditor/Financial Institution 
Data example
BICFI ABCDGB22
Clearing
System 
Member 
Identification
Clearing Sy stem 
Identif ication
GBDSC
Member 
Identif ication
205050
LEI 123456A1BCDEFG2T54
Name ABC BANK 
Address Various 
Structured
elements
252
HIGH STREET
LONDON
EC1 1WX
GB
Address Line 
(unstructured)
252 HIGH STREET
LONDON EC1 1WX
GB BICFI is preferred, alternatively, Name and Postal Address should 
be prioritised.
pacs.009 
Instruction for Creditor Agent/Instruction Information 
/UDLC/ABCDGB22
OR
/UDLC/ABC BANK LONDON GB
OR
/UDLC/ABC BANK LONDON EC1 1WX GB
BICFI only.
Name and structured Postal Address 
(TownName and Country Code should be 
prioritised).
Name and unstructured Address Line
(TownName and Country Code should be 
prioritised, where possible).

The purpose is used by the capture the nature of the payment e.g., CORT Trade Settlement Payment, CFEE
Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.
Credit Transfer Transaction Information
Purpose
The externalised Purpose code set is classified by the purpose, for example commercial, for 
which the numerous codes within the classification are each described by Name and 
Definition.
For example:
OTCD is classified within the Collateral categorisation, with the Name OTC Derivatives 
described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for 
example contracts which are traded and privately negotiated.
275
Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger
special processing e.g., Category Purpose code SECU ‘Securities’ may trigger pacs.002 Payment Status
Report to provide update on the progress of the payment to the previous Agent.

Credit Transfer Transaction Info’ Remittance Information
Unstructured
Remittance Information enable the matching/reconciliation of an entry that the payment 
is intended to settle
Min 0 – Max 1
The Unstructured sub element captures free format Remittance Information which 
is restricted in CBPR+ to 140 characters to ensure backward compatibility with the 
legacy MT message during coexistence. 
Min 0 – Max 1
Note: unlike the pacs.008 Remittance Information can only be captured in an 
Unstructured element in the pacs.009 Financial Institution Credit Transfer. 
Remittance Information is however a dedicated element used both within the pacs 
and camt reporting messages, whereby this information can travel end-to-end using 
ISO 20022.
276

g
Serial Financial Institution Payments
Use Case p.9.1.1 – High Level Financial Institution Credit Transfer (pacs.009) settled over a Payment Market Infrastructure
Use Case p.9.1.2 - High Level Financial Institution Credit Transfer (pacs.009) pre-advised settled using pacs.009.
277

Agent C credits the account of the 
Creditor (Agent D), and may 
optionally provide a notification 
e.g. credit notification in addition to 
an account statement (camt.054) 
in addition to a customer statement 
(camt.053)
1
Debtor initiates a payment 
instruction to the Debtor Agent
2
Agent B processes the payment 
on Agent C, via the Payment 
Market Infrastructure.
3
Payment Market Infrastructure, 
settles the payment between 
Agent B and Agent C as direct 
participants of the Market 
Infrastructure, and provides a 
settlement confirmation to Agent B
pacs.009 pacs.009 camt.053
pacs.002
2 3
Settlement 
Complete
4
4
1
pacs.002 A B C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their 
own usage guidelines based on the ISO 20022 standard.
camt.054
278
pacs.009

Agent E receives the payment and 
credits the account of Agent F as 
the Creditor, and may optionally 
provide a notification e.g. credit 
notification.
Agent C processes the payment on to 
Agent D
(ADV)
pacs.009
1
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (B) provided a notification to
Creditor Agent (E) using a pacs.009 advice to
indicate a ‘pre-advise and provides the related
payment details (in step 2b) This provides Agent
E the ability to take the payment amount into
their position, particularly where final settlement
in step 5 occur after their business day. (i.e. time
zone differences between the various Agent in
the payment chain.
2a
2b
In parallel the Debtor Agent (B) initiates a 
payment to credit the account of Agent (E)
as the creditor in the pacs.009 settlement 
message
pacs.002
3
4
2b
3
4
B E
C D
A F
279
Agent D credits the account of 
Agent E and should provide a 
notification e.g. credit notification 
(camt.054) in addition to a 
customer statement (camt.053)
5
Note: the pacs.009 ADV only operates in a direct advice message to the Creditor Agent
(Agent E above) with the pacs.009 used to settle this Agent.

Financial Institution 
Credit Transfer
280

pacs.009 (ADV)
Group Header
Credit Transfer 
Transaction Information
The pacs.009 advice is used to pre
advice an Agent of a fund movement 
toward the Creditor.
The core pacs.009 is used to perform 
the settlement of this pre-advice 
message.
281

pacs.009
pacs.009
pacs.002 camt.053
A B C D
The Financial Institution Credit Transfer (advice) message is sent by a Debtor Agent 
to a Creditor Agent, directly. In this context the pacs.009 ADV is used as a direct 
advice message.
It is used to move funds from a debtor account to a creditor, where both Debtor and 
Creditor are Financial Institutions.
282
pacs.009 ADV
pacs.002
To provide party transparency in the pacs.009 ADV, the Debtor of the pacs.009 ADV remains the Debtor of 
the pacs.009 used to settled the pacs.009 ADV.
The Creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) Instruction 
for Creditor Agent, Instruction Information element preceded by /UDLC/ (UnDerLying Creditor.

283

pygg, 
Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact
equivalent in the legacy MT payment message. However, the MT 202 Sender’s Reference (Field
20) could be considered a similar comparison where a pacs message contains a single
Transaction.
Each transaction’s Credit Transfer Transaction Information contains a variety of nested
Payment Identification elements to capture reference related to the individual transaction such
as a UETR (Unique End-to-endTransactionReference)
Group Header Message Identification
284

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
285

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 
Group Header Number of Transactions
286
g
Single transactions in the CBPR+ payment usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant payments, supporting the next
generation of innovation.

Group Header Settlement Information Settlement Method
D
27
287
The Settlement Method element in the pacs.009 ADV is fixed to COVE. This indicate this advice of 
Financial Institution Credit Transfer will be settlement using a covering pacs.009.
Like the pacs.008, the Agents being used in the covering payment to reimburse the Instructed Agent 
can be provided in the dedicated Reimbursement Agent elements. This allows the Instructed Agent to 
identify the debit account on their books from the Reimbursement Agent account or look up the account 
related to the reimbursement agent.
$
€

These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as
The Instructing Reimbursement Agent, and Instructed Reimbursement Agent. Each of these
reimbursement agents also has a dedicated account element to optionally capture their related account
details.
The Instructing Reimbursement Agent captures the Agent who will execute a covering payment (i.e. pacs.009
COV or domestic equivalent) often referred to as the currency correspondent. This optional element is
comparable with the Field 53a in the legacy FIN message.
$
Min 0 – Max 1
Min 0 – Max 1
Group Header Settlement Information
288
The Instructing Reimbursement Agent Account captured the account related to this Reimbursement Agent.
This element can be compared to the Party Identifier of the legacy Field 53.
Min 0 – Max 1
The Instructed Reimbursement Agent Account captured the account related to this Reimbursement Agent.
This element can be compared to the Party Identifier of the legacy Field 54.
The Instructed Reimbursement Agent captures the Agent who will receive the covering payment (i.e.,
pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer
InstructedAgent. This optional element is comparable with the Field 54a in the legacy FIN message.
$
€
Min 0 – Max 1

289

an end-to-end reference provided by the Debtor which must
be passed unchanged throughout the payment and reported
to the Creditor.
note: In a pacs.009 ADV if the Debtor has not provide
an end-to-end identifier, the Debtor Agent may
populate “NOTPROVIDED” to comply the mandatory
need of this element.
End to End
Identification
Payment
Identification
$
y 
Credit Transfer Transaction Info’ Payment Identification
a point-to-point reference restricted in CBPR+ to 16 character
and directly comparable with the Sender’s Reference (Field
20) of the legacy MT payment message.
Note: this reference must be transported in the End-to-End Identification of the pacs.009 message used to
settle the pacs.009 ADV
Instruction
Identification
Min 1 – Max 1
Min 1 – Max 1
the end-to-end Transaction Reference created using the UUIDv4
standard. This reference must be passed unchanged throughout
the payment, it may also be created by the Debtor within their
Payment Initiation request, and also included in reporting
messages.
UETR
Min 1 – Max 1
290

Payment
Identification
$
pgyppy py
Credit Transfer Transaction Info’ Payment Identification
an end-to-end reference assigned by the first Instructing
Agent to identify the transaction.
Transaction
Identification
Min 0 – Max 1
a point-to-point reference populated by a Payment
Market Infrastructure, typically to the settlement leg of a
clearing system transaction as a reference to the settled
clearing transaction.
Clearing 
System 
Reference
Min 0 – Max 1
291

Payment
Type 
Information
i
Credit Transfer Transaction Info’ Payment Type Info’
A nested element which may either use an external ISO
Service Level code* or a proprietary code. It is used to
identify a particular agreed service level which should be
applied to the payment.
For example, code G001 can be used to identify a gpi Tracked
Cover Transfer similarly to Field 111 value 001 in the MT 202
COV
Service
Level 
Min 0 – Max 3
A nested element which may either use an
external ISO Local Instrument code or a
proprietary code. It is used to identify the
type of payment local instrument such as a
Standing Order.
Note: the ISO instrument codes are
registered by specific community
group (captured in the code list)
Local 
Instrument 
Min 0 – Max 1
A nested element which may either use an external ISO
Category Purpose code or a proprietary code. It is used to
identify the category of payment. For example, SECU
Transactionis the payment of securities.
Category 
Purpose 
Min 0 – Max 1
Clearing
Channel
Min 0 – Max 1
a choice of imbedded
codes representing
the clearing channel
to be used to process
the payment.
e.g., RTGS
292
Instruction 
Priority 
Min 0 – Max 1
a choice of imbedded
codes representing the
urgency considered by
the Instructing Agent,
this point-to-point
information may be used by the 
Instructed Agent to differentiate 
the processing priority.
*note - where a service level is not bilaterally agreed, it may be ignored.

A mandated currency amount moved between the Instructing Agent and the Instructed Agent.
This therefore is the point-to-point currency amount exchanged, comparable with the MT Field
32A
Note: the Financial Institution Credit Transfer (pacs.009) has no Instructed Amount
element, Exchange Rate or Charger Bearer (unlike the pacs.008) as the Instructed 
Settlement Amount is expected to be transferred across the end-to-end payment chain 
without any charges being applied or currency conversions.
Interbank
Settlement £ Amount
$
¥
Credit Transfer Transaction Information
Interbank Settlement Amount 
Min 1 – Max 1
293
Interbank
Settlement
Date
A mandated date on which the Interbank Settlement should be executed between the
Instructing Agent and the Instructed Agent. This therefore is the value date comparable with
the MT Field 32A

of the instructions. 
Credit Transfer Transaction Information
294
Min 0 – Max 1
Min 0 – Max 1
The Settlement Priority provides an optional choice of embedded codes to indicate the instruction’s 
settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by 
the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused 
with the Instruction Priority. 
Note: As the Settlement Method of the pacs.009 (ADV) is ‘COVE’ (settled via a covering
pacs.009) SettlementPriority is relevant to the covering payment not the pacs.009ADV
Min 0 – Max 1
The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator 
such as a Market Infrastructure. 
This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time. 
The Settlement Time Request optionally captures the time settlement is requested for the payment instruction 
by the Instructing Agent. This Time can be capture in four nested elements:
• CLS Time the time the amount must be credit to CLS Bank
• Till Time the time until which the payment may be settled
• From Time the time from which the payment may be settled
• Reject Time the time from which the payment must be settled (to avoid reject)

pacs.009
Instructing pacs.009
Agent: Agent A
Instructed
Agent: Agent B
Instructing
Agent: Agent B
Instructed
Agent: Agent C
Instructing Agent and Instructed Agent
represent the Agents involved in the pacs 
point-to-point message exchange. These 
roles therefore change on each payment 
leg.
A B C D
Instructing Agent and Instructed Agent elements are required in all pacs messages 
and are only available in the Credit Transfer Information Credit Transfer Transaction Information
Instructing Agent
Instructed Agent
295

Instructing Agent & 
Debtor Agent
Debtor Instructed Agent Intermediary Agent 1 Intermediary Agent 2 Creditor Agent Creditor
Debtor Agent Creditor Agent & 
Instructed Agent
Debtor Creditor Previous Instructing 
Agent 1
Instructing Agent Previous Instructing 
Agent 2
Debtor Debtor Agent Instructing Agent Instructed Agent Intermediary Agent 1 Creditor Agent Creditor
Debtor Debtor Agent Creditor Agent Creditor Previous Instructing 
Agent 1 Instructing Agent Instructed Agent
directly between the Debtor Agent (as an InstructingAgent) and Creditor Agent (as an Instructed Agent).
The roles of previous Instructing Agents and Intermediary Agents are therefore irreverent in the pacs.009
(ADV)
A B C D E F G
296

elements describe the Debtor in greater detail. 
Debtor
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
Credit Transfer Transaction Info’ Debtor 297
Legal entity identifier of the LEI
financial institution.
The Debtor of the pacs.009 ADV remains the Debtor of the pacs.009 used 
to settled the pacs.009 ADV to provide party transparency.

298
been applied to the Debtors account, which are also reflected in their account Statement.
The Debtor Account uses a variety of nested elements to capture information related to 
the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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
the pacs.009 the Debtor is a Financial Institution, therefore the nested
elements Name and Proxy are unlikely to be used.

These agent maintain a relationship with their customers; the Debtor and Creditor. However, unlike the 
pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and 
Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship. 
Note: Where the Debtor and Creditor maintain a relationship with the same intermediary counterpart. It
is recommended that this Agent is captured in the Creditor Agent element to align with translation from
the legacy MT message.
Credit Transfer Transaction Information
Debtor Agent
Creditor Agent
299

300
information related to these Agents. The nature of this element implies there is an Agent or Agent in 
between the Debtor Agent and Creditor Agent in the payment transaction.
The Debtor Agent Account and Creditor Agent Account uses a variety of nested 
elements to capture information related to the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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
Debtor Agent and Creditor Agent are a Financial Institutions, therefore
the nested elements Name and Proxy are unlikely to be used.

elements describe the Creditor in greater detail.
Creditor
Certain legacy MT messages, such as the MT 200, identify the Creditor from the Credit Transfer Transaction Info Creditor 301
message sender, whereas this party would need to be repeated in the pacs.009
Name Name by which the 
Agent is known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
LEI
Legal entity identifier of 
the financial institution.
The Creditor of the pacs.009 ADV is captured 
in the pacs.009 (used to settle the pacs.009 
ADV) Instruction for Creditor Agent, Instruction 
Information element preceded by /UDLC/ 
(UnDerLying Creditor) to provide party 
transparency in the settlement message.

302
intended to be applied to the Creditors account, which are also reflected in their account Statement.
The Creditor Account uses a variety of nested elements to capture information related to 
the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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
For the pacs.009 the Creditor is a Financial Institution, therefore the
nested elements Name and Proxy are unlikely to be used.

Agents.
Credit Transfer Transaction Information
Instruction for Creditor Agent
Instruction for Next Agent
The Instruction for Creditor Agent element offers a multiplicity of up to 2 occurrences of 
information. This element enables:
➢ the use of 2 embedded codes to describe the instruction
➢ free format instruction information
➢ or both, where the free format complements the code.
The use of this element may be bilaterally agreed with the Creditor Agent. It must be passed 
on throughout the life cycle of the transaction until the payment reaches the Credit Agent.
Min 0 – Max 2
The Instruction for Next Agent element offers a multiplicity of up to 6 occurrences of 
information. This element is restricted to free format instruction information in CBPR+. 
The element is used to provide instruction to the next Agent (which may not be the Creditor
Agent)
Min 0 – Max 6
303

The purpose is used by the capture the nature of the payment e.g. CORT Trade Settlement Payment, CFEE
Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.
Credit Transfer Transaction Information
Purpose
The externalised Purpose code set is classified by the purpose, for example commercial, for 
which the numerous codes within the classification are each described by Name and 
Definition.
For example:
OTCD is classified within the Collateral categorisation, with the Name OTC Derivatives 
described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for 
example contracts which are traded and privately negotiated.
304
Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger
special processing e.g. Category Purpose code SECU ‘Securities’ may trigger pacs.002 Payment Status
Report to provide update on the progress of the payment to the previous Agent.

Credit Transfer Transaction Info’ Remittance Information
Unstructured
Remittance Information enable the matching/reconciliation of an entry that the payment 
is intended to settle
Min 0 – Max 1
The Unstructured sub element captures free format Remittance Information which 
is restricted in CBPR+ to 140 characters to ensure backward compatibility with the 
legacy MT message during coexistence. 
Min 0 – Max 1
Note: unlike the pacs.008 Remittance Information can only be captured in an 
Unstructured element in the pacs.009 Financial Institution Credit Transfer. 
Remittance Information is however a dedicated element used both within the pacs 
and camt reporting messages, whereby this information can travel end-to-end using 
ISO 20022.
305

g
Financial Institution Advice Payments
Use Case p.9.1.2.a - High Level Financial Institution Credit Transfer (pacs.009) pre-advised using pacs.009 (advice)
Use Case p.9.1.2.b - High Level Financial Institution Credit Transfer (pacs.009) pre-advised using pacs.009 (advice)
306

Agent C processes the payment on to 
Agent D
pacs.009
1
1
Debtor initiates a payment 
instruction to the Debtor Agent
2b
Debtor Agent (B) provided a notification to
Creditor Agent (E) using a pacs.009 advice to
indicate a ‘pre-advise and provides the related
payment details (in step 2b) This provides Agent
E the ability to take the payment amount into
their position, particularly where final settlement
in step 5 occur after their business day. (i.e. time
zone differences between the various Agent in
the payment chain.
In parallel the Debtor Agent (B) initiates a 
payment to credit the account of Agent (E) 
as the creditor in the pacs.009 settlement 
message
pacs.002
B E
C D
A F
307
3
4
2a
3
2b
Agent E receives the payment and 
credits the account of Agent F as 
the Creditor, and may optionally 
provide a notification e.g. credit 
notification.
4
Agent D credits the account of 
Agent E and should provide a 
notification e.g. credit notification 
(camt.054) in addition to a 
customer statement (camt.053)
5
camt.053
Note: the pacs.009 ADV only operates in a direct advice message to the Creditor Agent
(Agent E above) with the pacs.009 used to settle this Agent.

Agent C processes the payment on to 
Agent D
pacs.009
1
1
Debtor initiates a payment 
instruction to the Debtor Agent
2b
Debtor Agent (B) provided a notification to
Creditor Agent (E) using a pacs.009 advice to
indicate a ‘pre-advise and provides the related
payment details (in step 2b) This provides Agent
E the ability to take the payment amount into
their position, particularly where final settlement
in step 5 occur after their business day. (i.e. time
zone differences between the various Agent in
the payment chain.
In parallel the Debtor Agent (B) initiates a 
payment to credit the account of Agent (E)
as the creditor in the pacs.009 settlement 
message
pacs.002
B E
C D
A F
308
3
4
2a
3
2b
Agent E receives the payment and 
credits the account of Agent F as 
the Creditor, and may optionally 
provide a notification e.g. credit 
notification.
4
Agent D processes the payment 
on to Agent E (as the Account 
Servicing Institution, Settlement 
method INDA)
5
camt.053
Note: the pacs.009 ADV only operates in a direct advice message to the Creditor Agent
(Agent E above) with the pacs.009 used to settle this Agent.

Financial Institution 
Credit Transfer (Cover)
309

pacs.009
Group Header
Credit Transfer 
Transaction 
Information
pacs.009 (COV)
Group Header
Credit Transfer 
Transaction 
Information
Underlying 
Customer Credit 
Transfer
The pacs.009 has two main use cases: 
• as a core Financial Institution 
Credit Transfer message
• As a COV where it is used as cover 
of (to settle) a pacs.008.
The pacs.009 therefore contain 
information of the underlying Customer 
Credit Transfer (pacs.008) for use in 
the cover scenario, which is the key 
attribute to differentiate between these 
two use cases.
310

pacs.009
pacs.009
camt.053
pacs.002
pacs.002
A B C D
The Financial Institution Credit Transfer message is sent by a Debtor 
Financial Institution to a Creditor Financial Institution, directly or 
through other agents and/or a payment clearing and settlement 
system. It is used to move funds from a debtor account to a creditor, 
where both Debtor and Creditor are Financial Institutions.
311

pacs.009 cov
pacs.009 cov
The Financial Institution Credit Transfer cover message is sent by a 
Debtor Financial Institution to a Creditor Financial Institution, directly 
or through other agents and/or a payment clearing and settlement 
system. It is important to recognise that some roles change between 
these parallel messages.
camt.053
pacs.002
pacs.002
pacs.008
pacs.002
A B C D
Party pacs.008 pacs.009 cov
Debtor
Debtor
Creditor
Creditor Agent Creditor
Debtor Agent
Underlying Debtor
Underlying Creditor
camt.054
312

The correspondent banking cover payment method utilises
both the pacs.008 and pacs.009 cov as a whole transaction,
whereby the UETR element within these messages contain the
same UETRwhich effectively interlink the messages.
As an interlinked message it is important to understand the
way certain parties change their role in the pacs.009 cov This
is demonstrated in the example
pacs.008
pacs.002
pacs.009 cov pacs.009 cov
pacs.002
D DA 
C
D
DA CA
A D
B
C
Party pacs.008 pacs.009 cov
Debtor
Debtor
Creditor
Creditor Creditor 
Agent
Debtor 
Agent
Underlying Debtor
Underlying Creditor 313

314

pygg, 
Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact
equivalent in the legacy MT payment message. However, the MT 202 Sender’s Reference (Field
20) could be considered a similar comparison where a pacs message contains a single
Transaction.
Each transaction’s Credit Transfer Transaction Information contains a variety of nested
Payment Identification elements to capture reference related to the individual transaction such
as a UETR (Unique End-to-endTransactionReference)
Group Header Message Identification
315

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
316

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 
Group Header Number of Transactions
317
g
Single transactions in the CBPR+ payment usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant payments, supporting the next
generation of innovation.

Group Header Settlement Information Settlement Method
D
27
318
The Settlement Method element in the pacs.009 allows a choice of an embedded code.
INDA indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account 
Servicing Institution) The account held at the Instructed Agent may captured in the dedicated Settlement 
Account element.
INGA indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who 
has credited the Account they service for the Instructed Agent (as an Account Owner). The account held 
by the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account 
element.
$
€
Settlement Method code CLRG is not part of CBPR+ specifications but instead used in 
Market Infrastructure specification (HVPS+)

Group Header Settlement Information
319
The Settlement Account identifies the account details maintained at the account
servicing institution (Agent responsible for the settlement of the instruction as
indicated in the Settlement Method)
Min 0 – Max 1
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
Name identifies the name of the account as assigned by the Account Servicing
Institution
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

320

Payment
Identification
$
y 
Credit Transfer Transaction Info’ Payment Identification
a point-to-point reference restricted in CBPR+ to 16 character
and directly comparable with the Sender’s Reference (Field
20) of the legacy MT payment message.
Instruction
Identification
Min 1 – Max 1
an end-to-end reference provided by the Debtor which must
be passed unchanged throughout the payment and reported
to the Creditor.
note: for a pacs.009 COV the end-to-end id is provided
(by the Debtor) from the pacs.008 Instruction id.
In a pacs.009 COR if the Debtor has not provided an
end-to-end identifier, the Debtor Agent may populate
“NOTPROVIDED” to comply the mandatory need of this
element.
End to End
Identification
Min 1 – Max 1
the end-to-end Transaction Reference created using the UUIDv4
standard. This reference must be passed unchanged throughout
the payment, it may also be created by the Debtor within their
Payment Initiation request, and also included in reporting
messages.
UETR
Min 1 – Max 1
321

Payment
Identification
$
pgyppy py
Credit Transfer Transaction Info’ Payment Identification
an end-to-end reference assigned by the first Instructing
Agent to identify the transaction.
Transaction
Identification
Min 0 – Max 1
a point-to-point reference populated by a Payment
Market Infrastructure, typically to the settlement leg of a
clearing system transaction as a reference to the settled
clearing transaction.
Clearing 
System 
Reference
Min 0 – Max 1
322

Payment
Type 
Information
i
Credit Transfer Transaction Info’ Payment Type Info’
A nested element which may either use an external ISO
Service Level code or a proprietary code. It is used to
identify a particular agreed service level which should be
applied to the payment.
For example, code G001 can be used to identify a gpi Tracked
Cover Transfer similarly to Field 111 value 001 in the MT 202
COV
Service
Level 
Min 0 – Max 3
A nested element which may either use an
external ISO Local Instrument code or a
proprietary code. It is used to identify the
type of payment local instrument such as a
Standing Order.
Note: the ISO instrument codes are
registered by specific community
group (captured in the code list)
Local 
Instrument 
Min 0 – Max 1
A nested element which may either use an external ISO
Category Purpose code or a proprietary code. It is used to
identify the category of payment. For example, SECU
Transactionis the payment of securities.
Category 
Purpose 
Min 0 – Max 1
Clearing
Channel
Min 0 – Max 1
a choice of imbedded
codes representing
the clearing channel
to be used to process
the payment.
e.g., RTGS
323
Instruction 
Priority 
Min 0 – Max 1
a choice of imbedded
codes representing the
urgency considered by
the Instructing Agent,
this point-to-point
information may be used by the 
Instructed Agent to differentiate 
the processing priority.

A mandated currency amount moved between the Instructing Agent and the Instructed Agent.
This therefore is the point-to-point currency amount exchanged, comparable with the MT Field
32A
Note: the Financial Institution Credit Transfer (pacs.009) has no Instructed Amount
element, Exchange Rate or Charger Bearer (unlike the pacs.008) as the Instructed 
Settlement Amount is expected to be transferred across the end-to-end payment chain 
without any charges being applied or currency conversions.
Interbank
Settlement £ Amount
$
¥
Credit Transfer Transaction Information
Interbank Settlement Amount 
Min 1 – Max 1
324
Interbank
Settlement
Date
A mandated date on which the Interbank Settlement should be executed between the
Instructing Agent and the Instructed Agent. This therefore is the value date comparable with
the MT Field 32A
Min 1 – Max 1

of the instructions. 
Credit Transfer Transaction Information
325
Min 0 – Max 1
Min 0 – Max 1
The Settlement Priority provides an optional choice of embedded codes to indicate the instruction’s 
settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by 
the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused 
with the Instruction Priority. 
Note: Where the Settlement Method of the pacs.009 is ‘INDA’ (settled performed by the Instructed
Agent) this indicates the Settlement Priority. Code ‘INGA’ implies settlement has already occurred
for this point-to-point payment and therefore the Settlement Priority is not necessary.
Min 0 – Max 1
The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator 
such as a Market Infrastructure. 
This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time. 
The Settlement Time Request optionally captures the time settlement is requested for the payment instruction 
by the Instructing Agent. This Time can be capture in four nested elements:
• CLS Time the time the amount must be credit to CLS Bank
• Till Time the time until which the payment may be settled
• From Time the time from which the payment may be settled
• Reject Time the time from which the payment must be settled (to avoid reject)

pacs.009
Instructing pacs.009
Agent: Agent A
Instructed
Agent: Agent B
Instructing
Agent: Agent B
Instructed
Agent: Agent C
Instructing Agent and Instructed Agent 
represent the Agents involved in the pacs 
point-to-point message exchange. These 
roles therefore change on each payment 
leg.
A B C D
Instructing Agent and Instructed Agent elements are required in all pacs messages 
and are only available in the Credit Transfer Information Credit Transfer Transaction Information
Instructing Agent
Instructed Agent
326

Credit Transfer Transaction Information
327
Debtor Agent and Creditor Agent elements must be present before the previous 
Instructing Agent 1 element can be used
327
The Previous Instructing Agent 2 captures the second Previous Instructing Agent between the Previous
Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This
optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Previous Instructing Agent 2 Account captured the account related between this Agent and Previous
Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in
the legacy FIN message.
The Previous Instructing Agent 1 captures the first historic Agent between the Debtor Agent and the Previous
Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the
Field 72 first /INS/ occurrence in the legacy FIN message.
Min 0 – Max 1
The Previous Instructing Agent 1 Account captured the account related between this Agent and Previous
Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in
the legacy FIN message
The Previous Instructing Agent 3 captures the third Previous Instructing Agent between the Agent and the
Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN
message.
Min 0 – Max 1
Min 0 – Max 1
The Previous Instructing Agent 3 Account captured the account related between this Agent and Previous
Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in
the legacy FIN message

Instructing Agent & 
Debtor Agent
Debtor Instructed Agent Intermediary Agent 1 Intermediary Agent 2 Creditor Agent Creditor
Debtor Agent Creditor Agent & 
Instructed Agent
Debtor Creditor Previous Instructing 
Agent 1
Instructing Agent Previous Instructing 
Agent 2
Debtor Debtor Agent Instructing Agent Instructed Agent Intermediary Agent 1 Creditor Agent Creditor
Debtor Debtor Agent Creditor Agent Creditor Previous Instructing 
Agent 1 Instructing Agent Instructed Agent
pyy gp, g(, y
Agent 1) Previous Instructing Agent however is a static role which allows additional Previous Instructing Agent to be
appended to the history of the payment.
The below diagram visualizes the change ofAgent role at different stages of the payment transaction life cycle.
Note: the statics roles of Previous Instructing Agent transition into
Intermediary Agents in the potential return chain (refer to the pacs.004
section for Payment Returns)
A B C D E F G
328

Credit Transfer Transaction Information
329
The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the
CreditorAgent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.
The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent
for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the
Field 56a in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the
Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.
The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the
Creditor Agent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 3 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 2. This optional element has not comparable field in the legacy FIN message.
1
2
3
Debtor Agent and Creditor Agent elements must be present before the Intermediary 
Agent 1 element can be used

elements describe the Debtor in greater detail. 
Debtor
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
Credit Transfer Transaction Info’ Debtor 330
Legal entity identifier of the LEI
financial institution.

331
been applied to the Debtors account, which are also reflected in their account Statement.
The Debtor Account uses a variety of nested elements to capture information related to 
the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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
the pacs.009 the Debtor is a Financial Institution, therefore the nested
elements Name and Proxy are unlikely to be used.

These agent maintain a relationship with their customers; the Debtor and Creditor. However, unlike the 
pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and 
Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship. 
Note: Where the Debtor and Creditor maintain a relationship with the same intermediary counterpart. It
is recommended that this Agent is captured in the Creditor Agent element to align with translation from
the legacy MT message.
Credit Transfer Transaction Information
Debtor Agent
Creditor Agent
332

333
related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor 
Agent and Creditor Agent in the payment transaction.
The Debtor Agent Account and Creditor Agent Account uses a variety of nested 
elements to capture information related to the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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
Debtor Agent and Creditor Agent are Financial Institutions, therefore
the nested elements Name and Proxy are unlikely to be used.

elements describe the Creditor in greater detail.
Creditor
Credit Transfer Transaction Info Creditor 334
Certain legacy MT messages, such as the MT 200, identify 
the Creditor from the message sender, whereas this party 
would need to be repeated in the pacs.009
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
LEI
Legal entity identifier of the 
financial institution.

335
intended to be applied to the Creditors account, which are also reflected in their account Statement.
The Creditor Account uses a variety of nested elements to capture information related to 
the account.
Credit Transfer Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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
the pacs.009 the Creditor is a Financial Institution, therefore the
nested elements Name and Proxy are unlikely to be used.

Agents.
Credit Transfer Transaction Information
Instruction for Creditor Agent
Instruction for Next Agent
The Instruction for Creditor Agent element offers a multiplicity of up to 2 occurrences of 
information. This element enables:
➢ the use of 2 embedded codes to describe the instruction
➢ free format instruction information
➢ or both, where the free format complements the code.
The use of this element may be bilaterally agreed with the Creditor Agent. It must be passed 
on throughout he life cycle of the transaction until the payment reaches the Credit Agent.
Min 0 – Max 2
The Instruction for Next Agent element offers a multiplicity of up to 6 occurrences of 
information. This element is restricted to free format instruction information in CBPR+. 
The element is used to provide instruction to the next Agent (which may not be the Creditor
Agent)
Min 0 – Max 6
336

The purpose is used by the capture the nature of the payment e.g. CORT Trade Settlement Payment, CFEE
Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.
Credit Transfer Transaction Information
Purpose
The externalised Purpose code set is classified by the purpose, for example commercial, for 
which the numerous codes within the classification are each described by Name and 
Definition.
For example:
OTCD is classified within the Collateral categorisation, with the Name OTC Derivatives 
described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for 
example contracts which are traded and privately negotiated.
337
Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger
special processing e.g. Category Purpose code SECU ‘Securities’ may trigger pacs.002 Payment Status
Report to provide update on the progress of the payment to the previous Agent.

Credit Transfer Transaction Info’ Remittance Information
Unstructured
Remittance Information enable the matching/reconciliation of an entry that the payment 
is intended to settle.
Min 0 – Max 1
The Unstructured sub element captures free format Remittance Information which 
is restricted in CBPR+ to 140 characters to ensure backward compatibility with the 
legacy MT message during coexistence. 
Min 0 – Max 1
Note: the pacs.008 Remittance Information is captured in the pacs.009 COV within 
the Underlying Customer Credit Transfer, Remittance Information element. 
The Remittance Information in the pacs.009 COV is for Creditorthis message (often 
the Creditor Agent of the pacs.008) As this information is not present in the pacs.008 it 
is unlikely the pacs.009 COV remittance information will be used.
338

contained within this nested element relates directly to the information exchanged between the Instructing 
Agent and Instructed Agent of the pacs.008 FI to FI Customer Credit Transfer and can be compared with 
Sequence B of the legacy MT 202 COV.
pacs.008
Group 
Header
Credit 
Transfer 
Transaction 
Information
pacs.009 
(cov)
Group 
Header
Credit 
Transfer 
Transaction 
Information
Underlying 
Customer 
Credit 
Transfer
Credit Transfer Transaction Information
Underlying Customer Credit Transfer
339
When utilizing the Underlying Customer 
Credit Transfer nested element as part of a 
pacs.009 Financial Institution Credit 
Transfer cover message the:
➢ Debtor 
➢ Debtor Agent 
➢ Creditor Agent
➢ Creditor
are all mandatory elements.
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max 1
Note: Instruction for Creditor 
Agent from the Underlying 
Customer Credit Transfer does 
not need to be included

g
Cover Method Financial Institution Payments
Use Case p.9.2.1 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) 
Use Case p.9.2.2 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) over a Payment Market 
Infrastructure
Use Case p.9.2.3 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) where an incorrect intermediary 
is used
Use Case p.9.2.4 – High Level FI to FI Customer Credit Transfer involved a serial leg into a cover method (pacs.009 COV)
Use Case p.9.2.5 – High Level FI to FI Customer Credit Transfer involved a serial leg in and out of a cover method (pacs.009 COV)
Use Case p.9.2.6 - High Level FI to FI Customer Credit Transfer involved a serial leg out of a cover method (pacs.009 COV)
340

Agent C produces an end of day 
account statement report. An 
optional real time notifications e.g. 
advice of credit may have also been 
created at the time of the credit 
posting
Agent C receives the payment and 
credits the account of Agent D as 
the Creditor 
Agent B processes the payment 
on to Agent C
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a payment using 
the cover method to the Creditor Agent (D)
2a
2b
In parallel the Debtor Agent (A) initiates a covering 
payment to credit the account of Agent (D) who become 
the Creditor of the cover payment (pacs.009 cov). 
Agent A’s role also changes in the cover payment 
where it becomes the Debtor, whereby Agent A’s 
account with their correspondent (Agent B) is debited.
5
5
pacs.002
Agent D reconciles the covering 
funds and credits the account of the 
Creditor, and may optionally 
provide a notification e.g. credit 
notification.
6
pacs.002
3 4
2b
3
4
A D
B C
341

Agent C produces an end of day 
account statement report. An 
optional real time notifications e.g. 
advice of credit may have also been 
created at the time of the credit 
posting
Agent C receives the payment and 
credits the account of Agent D
Agent B processes the payment 
on Agent C, via the Payment 
Market Infrastructure.
pacs.002
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover method 
to the Creditor Agent (D)
2a
In parallel the Debtor Agent (A) 
initiates a covering payment to 
credit the account of Agent (D) 
with their correspondent (Agent 
C)
6
6
pacs.009 cov
Settlement 
Complete
pacs.002
Agent D reconciles the covering 
funds and credits the account of the 
Creditor, and may optionally 
provide a notification e.g. credit 
notification.
7
Payment Market Infrastructure, 
settles the payment between Agent 
B and Agent C as direct 
participants of the Market 
Infrastructure, and provides a 
settlement confirmation to Agent B
4
4
5
5
3
3
2b
2b
A D
B
C
Market Infrastructure will either conform to HVPS+ guidelines or establish their 
own usage guidelines based on the ISO 20022 standard.
342

Agent C receives the payment and 
credits the account of Agent D. Agent C 
produces an end of day account 
statement report. An optional real time 
notifications e.g. advice of credit may 
have also been created at the time of the 
credit posting
Agent Z receives the payment and 
recognises they do not hold the account of 
Agent D as the Creditor. Agent Z reject the 
cover payment (pacs.009 cov) using a 
pacs.002 include the reject reason code 
Agent B processes the payment on to 
Agent Z
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a payment using 
the cover method to the Creditor Agent (D)
2a
In parallel the Debtor Agent (A) initiates a covering 
payment to credit the account of Agent (D) who become 
the Creditor of the cover payment (pacs.009 cov). 
Agent A’s role also changes in the cover payment 
where it becomes the Debtor, whereby Agent A’s 
account with their correspondent (Agent B) is debited.
5
5
pacs.002
Agent D reconciles the covering funds 
and credits the account of the Creditor, 
and may optionally provide a notification 
e.g. credit notification.
6
pacs.002
pacs.009 cov
2b
2b
3
4
3
Recognising the error Agent B re-processes the payment on to 
Agent C using the same UETR 
(correcting the error in step 3)
4
A D
B Z
C
343

Agent E receives the payment 
instruction and credits the account of 
the Creditor, and may optionally 
provide a notification e.g. credit 
notification. Alternatively, they may 
have chosen to await until settlement 
occurred in Step 6 based upon their 
risk appetite.
Agent C processes the payment on 
Agent D, using a correspondent 
banking business relationship
pacs.002
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the serial method 
towards the Creditor Agent (E)
2
3a
3b
In parallel the Agent (B) initiates a 
covering payment to credit the account 
of Agent (E) with their correspondent 
(Agent D)
3b
5
pacs.002
5
A E
C
Note settlement of step 5 could alternative occur between Agent C and D using a 
Market Infrastructure..
344
B
pacs.008
pacs.002
D
Agent B initiates a payment 
using the cover method towards 
the Creditor Agent (E) by 
sending a direct pacs.008 to 
Agent E who they have business 
relationship with.
Agent D receives the payment and 
credits the account of Agent E. 
Agent D produces an end of day 
account statement report. An 
optional real time notification e.g. 
advice of credit may have also been 
created at the time of the credit 
posting
6
6
4

Agent E receives the payment 
instruction and process the payment 
on to Agent F. Alternatively they may 
have chosen to await until settlement 
occurred in Step 6 based upon their 
risk appetite.
Agent C processes the payment on 
Agent D, using a correspondent 
banking business relationship
pacs.002
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the serial method 
towards the Creditor Agent (F)
2
3a
3b
In parallel the Agent (B) initiates a 
covering payment to credit the account 
of Agent (E) with their correspondent 
(Agent D)
3b
5
pacs.002
Agent F receives the payment and 
credits the account of the Creditor, 
and may optionally provide a 
notification e.g. credit notification.
7
5
A E
C
Note settlement of step 5 could alternative occur between Agent C and D using a 
Market Infrastructure..
345
B
pacs.008
pacs.002
pacs.002 F
D
Agent B initiates a payment using 
the cover method towards the 
Creditor Agent (F) by sending a 
direct pacs.008 to Agent E who they 
have business relationship with.
Agent D receives the payment and 
credits the account of Agent E. 
Agent D produces an end of day 
account statement report. An 
optional real time notification e.g. 
advice of credit may have also been 
created at the time of the credit 
posting
6
6
4

Agent D receives the payment 
instruction and process the payment 
on to Agent E. Alternatively they may 
have chosen to await until settlement 
occurred in Step 6 based upon their 
risk appetite.
Agent B processes the payment on 
Agent C, using a correspondent 
banking business relationship
pacs.002
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
2a
2b
In parallel the Agent (A) initiates a 
covering payment to credit the account 
of Agent (D) with their correspondent 
(Agent C)
2b
5
pacs.002
Agent E receives the payment and 
credits the account of the Creditor, 
and may optionally provide a 
notification e.g. credit notification.
4
5
A D
Note settlement of step 5 could alternative occur between Agent B and C using a 
Market Infrastructure..
346
pacs.002 E
B
Debtor Agent (A) initiates a 
payment using the cover 
method towards the Creditor 
Agent (E) by sending a direct 
pacs.008 to Agent D who they 
have business relationship with.
Agent C receives the payment and 
credits the account of Agent D. 
Agent C produces an end of day 
account statement report. An 
optional real time notification e.g. 
advice of credit may have also been 
created at the time of the credit 
posting
6
6
3
C

FI to FI Payment 
Status Report
347

pacs.002
Group Header
Transaction Information 
And Status
Institution Payment Status Report 
message is sent by an instructed agent 
to the previous party in the payment 
chain. It is used to inform this party 
about the positive or negative status of 
an instruction. It is also used to report 
on a pending instruction
348

The FIToFIPaymentStatusReport
message is sent by an instructed agent 
to the previous party in the payment 
chain. It is used to inform this party about 
the positive or negative status of an 
instruction. It is also used to report on a 
pending instruction.
pain.001
pain.002
pacs.008
pacs.002
pacs.008
pacs.002
pacs.004
pacs.002
Reject & 
Reason 
The code list representing the 
Payment Transaction Status is part 
of the ISO 20022 external code list
A B C
Return & 
Reason 
CBPR+ restricted 
the pacs.002 to a 
single transaction
349

pacs.002
A
B
Debtor
*Noting in CGI-MP pain.008 may also be sent by the Initiating Party/Creditor directly to the Creditor Agent which is outside of the scope of CBPR+.
Creditor Agent Creditor
*Initiating Party may alternative represent an authorised party such as a head office 
**or other proprietary method for instructing a direct debit initiation request. 
pain.002
camt.053
pacs.003
Debtor Agent
pain.008**
Initiating Party*
The FIToFIPaymentStatusReport message is sent by an instructed agent to the previous party in the payment 
chain. It is used to inform this party about the positive or negative status of an instruction. It is also used to 
report on a pending instruction.

351

Group Header Message Identification
352
Each ISO 20022 payment message has a Message Identification element, located in the
Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact
equivalent in the legacy MT payment message. However, the Sender’s Reference (Field 20)
could be considered a similar comparison where a pacs message contains a single Transaction.
Min 1 – Max 1

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Date Time
353

354

Transaction Information and Status
Original Group Information
ggyg pyyp
The mandatory Original Message Identification contains the point-to-point reference, and the mandatory
Original Message Name Identification contains the message name of the underlying payment being
reported upon. Optionally the Original Creation Date Time can also be captured.
Note: the xx in the CBPR+ Usage Guideline 
represents the message version of the message 
received for example pacs.008.001.08 
pacs.002
A B For example:
Original Message Name Identification “pacs.008.001.08” confirms the
Status Report is of a pacs.008 Financial Institution to Financial
Institution Customer Credit Transfer. Where as “pacs.009.001.08”
confirms the Status Report is of a pacs.009 Financial Institution Credit
Transfer.
Message 
Identification abcd1234
pacs.008.001.08 Original Message 
Name Identification
Original Message 
Identification abcd1234
Message 
Identification xyz9875
Original Group
Information 
Group Header
pacs.008
355

pyg pyy
Status Report relates to.
Original 
UETR
Original 
Transaction
Identification
Original 
End to End
Identification
Original 
Instruction
Identification
Transaction Information and Status
Original Instruction Identification
Original End to End Identification
Original UETR
Original Transaction 
Mandatory element (in addition to Original Message identification
and Original Message Name Identification described on the previous
page) include:
Original End to End Identification
Original UETR
Optionally Original Transaction Identification and Original
Instruction Identification may also be used.
These Original elements enables the Instructed Agent in the
pacs.002 Payment Status Report to associate the Payment Status
with the payment they originally sent.
Min 1 – Max 1
Min 1 – Max 1
Min 0 – Max 1 Min 0 – Max 1
356

pppgpy 
Transaction Status element is arguable the most significant/core parts of the pacs.002 and optionally may
further be complimented with Status Reason Information.
The nested Status Reason Information enable the optional inclusion of:
Originator – the party that issues the status. Typically, the pacs.002 Instructing Agent and 
therefore Originator is not necessary.
Reason – which utilizes either an ISO external Status Reason code or a proprietary 
reason. For example, AC04 ‘Closed Account Number’ would compliment a RJCT (Reject) 
Transaction Status.
Additional Information – a text element to provide further status reason information, 
necessary where the Reason code is NARR 
The next two slides take a look at:
• The code relevant to CBPR+ Payment Statuses, the codes description and the High Level Use Case.
• Logical order in which these codes may be used in one or multiple Payment Status Report updates.
Min 0 – Max 1
Original Group Information
Transaction Status
Transaction Information and Status
Note: A Reason code must be provided where the Transaction Status RJCT (Reject) code is used. 
357

358
ACCP AcceptedCustomerProfile Preceding check of technical validation was successful. Customer 
profile check was also successful.
Sent by any Agent in the payment chain to confirm acceptance prior to 
technical validation. 
ACFC AcceptedFundsChecked Preceding check of technical validation and customer profile was 
successful and an automatic funds check was positive.
Sent by any Agent in the payment chain to confirm the technical validation/ 
profile w as positive and automatic funds check w as positive.
ACIS AcceptedandChequeIssued Payment instruction to issue a cheque has been accepted, and the 
cheque has been issued but not yet been deposited or cleared.
Sent by any Agent in the payment chain to confirm a cheque has been issued 
as requested.
ACSC AcceptedSettlementCompleted Settlement has been completed. Sent by the Any Agent to confirm settlement of a payment message leg.
ACSP AcceptedSettlementInProcess All preceding checks such as technical validation and customer 
profile were successful and therefore the payment initiation has been 
accepted for execution.
Sent by any Agent to the to confirm the payment is accepted follow ing 
technical validations being successfully completed. 
ACTC AcceptedTechnicalValidation Authentication and syntactical and semantical validation are 
successful
Sent by any Agent in the payment chain to the previous Agent to confirm the 
payment is accepted follow ing technical validations being successfully 
completed. 
ACWC AcceptedWithChange Instruction is accepted but a change will be made, such as date or 
remittance not sent.
Sent by any Agent in the payment chain to the previous Agent to confirm the 
payment is accepted follow ing amendments being made. 
ACWP AcceptedWithoutPosting Payment instruction included in the credit transfer is accepted 
without being posted to the creditor customer’s account.
Sent by Creditor Agent to the previous Agent to confirm the acceptance of 
payment w ithout settlement on the creditor’s account,
CPUC CashPickedUpByCreditor Cash has been picked up by the Creditor. Sent by Creditor Agent to the previous Agent to confirm that the cash 
collection has been picked up by the Creditor,
PDNG Pending Payment initiation or individual transaction included in the payment 
initiation is pending. Further checks and status update will be 
performed.
Sent by any Agent in the payment chain to the previous Agent as an interim 
status w hilst other validations are performed.
RCVD Received Payment initiation has been received by the receiving agent. Sent by Any Agent to the previous Agent as confirmation that their Customer 
Credit Transfer initiation request has been received by the payment engine.
RJCT Rejected Payment initiation or individual transaction included in the payment 
initiation has been rejected.
Sent by Any Agent to inform the previous Agent that their Customer Credit 
Transfer has been rejected.

the previous Agent on changes to 
the status of the payment. Such 
Status Information messages 
(pacs.002), with the exception of 
reject code RJCT which is 
mandatory in CBPR+, are bilateral 
agreed, where upon a variety of 
these Transaction Statuses may be 
used by the Instructed Agent at 
different stages of the payment 
processing.
(pacs) and the role of the Agent in providing these status. 
Transaction Information and Status Transaction Status 359
PDNG
ACWP
ACFC
ACCP
ACWC
ACSC
ACTC
ACCC
Creditor
Agent
Any RCVD
Agent
RJCT
ACIS
CPUC
ACSP

360
IncorrectAccountNumber
number is missing
AC02
InvalidDebtorAccountNumber Debtor account number invalid or missing
Sent by Instructed Agent w hen Debtor account number is incomplete
AC04
ClosedAccountNumber
Account number specified has been closed on the bank of 
account's books
Sent by Creditor Agent w hen the Creditor account number is closed
AC06
BlockedAccount
Account specified is blocked, prohibiting posting of transactions 
against it.
Sent by Creditor Agent w hen Creditor account is blocked from posting 
credit entries.
Sent by Instructed Agent w hen a settlement account is blocked
AC07
ClosedCreditorAccountNumber Creditor account number closed
Sent by Creditor Agent w hen account number is closed. 
CBPRplus recommend using AC04, but support AC07 to remain 
interoperable with other clearing systems.
AC13 InvalidDebtorAccountType Debtor account type is missing or invalid
Sent by Instructed Agent w hen Debtor account type element is incorrect
AGNT
IncorrectAgent Agent in the payment w orkflow is incorrect
Sent by Instructed Agent w hen an agent in the payment transaction has 
an incorrect identification element
AG01
TransactionForbidden
Transaction forbidden on this type of account (formerly 
NoAgreement)
Sent by Instructed Agent w hen the type of payment transaction is not 
allow ed for the specified account
AG07
UnsuccesfulDirectDebit
Debtor account cannot be debited for a generic reason.
Code value may be used in general purposes and as a 
replacement for AM04 if debtor bank does not reveal its 
customer's insufficient funds for privacy reasons
Sent by Debtor Agent of a Direct Debit message, w hen debtor account 
can not be debited
AM02
NotAllow edAmount
Specific transaction/message amount is greater than allow ed 
maximum
Sent by Instructed Agent w hen payment amount is above an allow ed 
amount. For example the clearing system w ith a upper amount threshold

361
AM03 NotAllowedCurrency 
outside of existing agreement
w ithin the existing business agreement
AM04 InsufficientFunds Amount of funds available to cover specified message 
amount is insufficient.
Sent by Instructed Agent w hen there is not sufficient funds to settle the 
payment transaction.
AM05 Duplication Payment is a duplicate of another payment
Sent by Instructed Agent w hen the payment is a duplicate. CBPRplus 
recommend using DUPL, but support AM05 to remain interoperable with other 
clearing systems.
AM06 TooLowAmount Specified transaction amount is less than agreed 
minimum.
Sent by Instructed Agent w hen the payment amount is below a minimum 
amount.
AM07 BlockedAmount Amount specified in message has been blocked by 
regulatory authorities Sent by Instructed Agent w hen the payment amount is blocked by regulators
AM09 WrongAmount Amount received is not the amount agreed or expected Sent by Instructed Agent w hen the payment amount is incorrect
BE01 InconsistenWithEndCustomer
Identification of end customer is not consistent with 
associated account number (formerly 
CreditorConsistency).
Sent by Creditor Agent w hen there is an inconsistency betw een the Creditor’s 
identification and the account number
BE04 MissingCreditorAddress
Specification of creditor's address, which is required for 
payment, is missing/not correct (formerly 
IncorrectCreditorAddress).
Sent by Instructed Agent w hen the Creditor’s address is missing
Sent by Creditor Agent w hen the Creditor’s address is incorrect
BE05 UnrecognisedInitiatingParty Party who initiated the message is not recognised by the 
end customer
Sent by Creditor Agent w hen the initiating party is unknow n to the beneficiary
BE07 MissingDebtorAddress Specification of debtor's address, which is required for 
payment, is missing/not correct.
Sent by Instructed Agent w hen the address of the Debtor is missing or 
incorrect

362
BE10 InvalidDebtorCountry Debtor country code is missing or invalid 
y gy g 
incorrect
BE11 InvalidCreditorCountry Creditor country code is missing or invalid Sent by Instructed Agent w hen the country code of the Creditor is missing or 
incorrect
BE16 InvalidDebtorIdentificationCode Debtor or Ultimate Debtor identification code missing or 
invalid
Sent by Instructed Agent w hen the identification of the Debtor or Ultimate
Debtor is missing or incorrect
BE17 InvalidCreditorIdentificationCode Creditor or Ultimate Creditor identification code missing 
or invalid
Sent by the Instructed Agent w hen the identification of the Creditor or 
Ultimate Creditor is missing or incorrect
CN01 AuthorisationCancelled Authorisation is cancelled. Sent by Instructed Agent w hen a third party debit authorisation has been 
cancelled or is not in place.
CNOR Creditor bank is not registered Creditor bank is not registered under this BIC in the 
Clearing Settlement Mechanism (CSM)
Sent by Instructed Agent w hen the Creditor Agent is not reachable in the 
Market Infrastructure (CSM) and an appropriate correspondent can not be 
determined.
CURR IncorrectCurrency Currency of the payment is incorrect
Sent by the Creditor Agent w hen the Interbank Settlement Amount 
Currency is not the same as the Creditor account currency and a currency 
conversion is not accepted on the Creditor’s account. 
CUST RequestedByCustomer Cancellation requested by the Debtor
Sent by Instructed Agent upon request by Debtor. CBPRplus recommend 
using FOCR, but support CUST to remain interoperable with other clearing 
systems.
DT01 InvalidDate Invalid date (eg, wrong or missing settlement date) Sent by Instructed Agent w hen the settlement date is in the past and an 
agreement is in place to reject rather than apply the next possible value date.
DT04 FutureDateNotSupported Future date not supported Sent by Instructed Agent w hen a future settlement date is not supported or 
appear to be an error e.g. is the w rong year.

363
DUPL DuplicatePayment Payment is a duplicate of another payment 
y gpyp
ERIN ERIOptionNotSupported The Extended Remittance Information (ERI) option is not 
supported.
Sent by Instructed Agent w hen extended Remittance information (Related 
Remittance Information) is not supported or bilaterally/multilaterally agreed
ED05 SettlementFailed Settlement of the transaction has failed. Sent by Instructed Agent w hen the settlement of payment has failed or been 
unsuccessful. 
FF03 InvalidPaymentTypeInformation
Payment Type Information is missing or invalid.
Generic usage if cannot specify Service Level or Local 
Instrument code
Sent by Instructed Agent w hen the Payment Type Information (Instruction 
Priority, Clearing Channel) provided for the payment is incorrect or not 
supported. 
FF04 InvalidServiceLevelCode Service Level code is missing or invalid
Sent by Instructed Agent w hen the Payment Type Information Service Level
provided for the payment is incorrect or not supported
FF05 InvalidLocalInstrumentCode Local Instrument code is missing or invalid
Sent by Instructed Agent w hen the Payment Type Information Local 
Instrument provided for the payment is incorrect or not supported
FF06 InvalidCategoryPurposeCode Category Purpose code is missing or invalid
Sent by Instructed Agent w hen the Payment Type Information Category 
Purpose provided for the payment is incorrect or not supported
FF07 InvalidPurpose Purpose is missing or invalid Sent by Instructed Agent w hen the Purpose provided for the payment is 
either missing or incorrect
FOCR FollowingCancellationRequest Return following a cancellation request Sent by Instructed Agent that has accepted a payment cancellation request 
(camt.056) and subsequently is rejecting the unsettled payment instruction.
FR01 Fraud Returned as a result of fraud. Sent by Instructed Agent w hen the payment is identified as fraudulent.
MD01 NoMandate No Mandate Sent by Instructed Agent w hen a Direct Debit message has no mandate in 
place.

364
MD02 
Mandatescheme is missing.
is missing.
MD05 CollectionNotDue Creditor or creditor's agent should not have collected the 
direct debit
Sent by Instructed Agent w hen a Direct Debit collection w as not due
MD07 EndCustomerDeceased End customer is deceased. Sent by Creditor Agent w hen the Creditor or Ultimate Creditor is deceased
MS02 NotSpecifiedReasonCustomer 
Generated Reason has not been specified by end customer Sent by Creditor Agent w here instructed to reject by the Creditor, but no 
reason w as specified
MS03 NotSpecifiedReasonAgent 
Generated Reason has not been specified by agent. Sent by Instructed Agent but no reason is specified
NARR Narrative Reason is provided as narrative information in the 
additional reason information.
Sent by Instructed Agent the reason is provided as narrative information. 
Only to be used where no other code is appropriate! (i.e. exceptional 
circumstances)
NOAS NoAnswerFromCustomer No response from Beneficiary
Sent by Instructed Agent w hen the Creditor did not respond to query for 
additional information in order that the payment could be credited e.g. currency 
control documentation.
NOCM Not compliant (more generic)
Customer account is not compliant with regulatory 
requirements, for example FICA (in South Africa) or any 
other regulatory requirements which render an account 
inactive for certain processing.
Sent by Instructed Agent w hen the Creditor account is not compliant w ith 
certain regulatory requirements.
RC01 BankIdentifierIncorrect
Bank Identifier code specified in the message has an 
incorrect format (formerly 
IncorrectFormatForRoutingCode).
Sent by Instructed Agent w hen an incorrect BIC has been used in the 
payment
RC03 InvalidDebtorBankIdentifier Debtor bank identifier is invalid or missing Sent by Instructed Agent w hen the Debtor Agent identification is incorrect or 
missing

365
RC04 InvalidCreditorBankIdentifier Creditor bank identifier is invalid or missing Sent by Instructed Agent w hen the Creditor Agent identification is incorrect or 
missing
RC08 InvalidClearingSystemMemberIden
tifier
ClearingSystemMemberidentifier is invalid or missing.
Generic usage if cannot specify between debit or credit 
account
Sent by Instructed Agent w hen the clearing system member identification for 
an Agent is incorrect
RC11 InvalidIntermediaryAgent Intermediary Agent is invalid or missing Sent by Instructed Agent w hen the intermediary agent identification is 
incorrect
RF01 NotUniqueTransactionReference Transaction reference is not unique within the 
message.
Sent by Instructed Agent w hen the transaction reference (UETR and 
Instruction Identification) are not unique
RR01 Missing Debtor Account or 
Identification
Specification of the debtor’s account or unique 
identification needed for reasons of regulatory 
requirements is insufficient or missing
Sent by Instructed Agent w hen the Debtor identification or debtor account is 
missing, or the information provided are not sufficient
RR02 Missing Debtor Name or Address Specification of the debtor’s name and/or address needed for 
regulatory requirements is insufficient or missing.
Sent by Instructed Agent since the Debtor name or Address is missing, or 
information provided is not sufficient
RR03 Missing Creditor Name or Address Specification of the creditor’s name and/or address needed 
for regulatory requirements is insufficient or missing.
Sent by Instructed Agent since the Creditor name or Address is missing, or 
information provided is not sufficient
RR04 Regulatory Reason Regulatory Reason Sent by Instructed Agent due to any unspecified regulatory reason
RR05 RegulatoryInformationInvalid Regulatory or Central Bank Reporting information missing, 
incomplete or invalid.
Sent by Instructed Agent w hen the reporting information required by the 
central bank or reporting authority is missing or not complete
RR06 TaxInformationInvalid Tax information missing, incomplete or invalid. Sent by Instructed Agent w here required tax information is missing, not valid 
or not complete

366
for payment type.
RR08 RemittanceInformationTruncated Remittance information truncated to comply w ith rules for 
payment type.
Sent by Instructed Agent w here the Structured Remittance Information 
has not been bilaterally or multilaterally agreed, w hich or has resulted in 
truncation
RR09 InvalidStructuredCreditorReference Structured creditor reference invalid or missing.
Sent by Instructed Agent w hen the structure of the creditor reference in 
the remittance information is invalid or missing
RR11 InvalidDebtorAgentServiceID Invalid or missing identification of a bank proprietary service. Sent by Instructed Agent w here the proprietary identification for the Debtor 
is invalid or not understood
RR12 InvalidPartyID Invalid or missing identification required w ithin a particular 
country or payment type.
Sent by Instructed Agent w here a proprietary party identification is 
considered invalid or not understood
RUTA ReturnUponUnableToApply Return following investigation request and no remediation 
possible.
Sent by Instructed Agent that is unsatisfied w ith the outcome of the unable 
to apply request and is subsequently rejecting the payment instruction.
Alternatively it can be used by the original Creditor Agent w hen the creditor 
is unable to apply the transaction
TM01 Invalid Cut off time
Associated message, payment information block, or 
transaction was received after agreed processing cut-off 
time.
Sent by Instructed Agent w hen the message w as received after the 
agreed processing cut off time and an agreement is in place to reject rather 
than apply the next possible value date.
UPAY UnduePayment Payment is not justified. Sent by Instructed Agent the payment is undue

367
G004 CreditPendingFunds
In a FIToFI Customer Credit Transfer: Credit to the 
creditor’s account is pending, status Originator is waiting 
for funds provided via a cover. Update will follow from the 
Status Originator.
Optionally sent by the Creditor Agent w ent the cover has not been settled at 
the creditor agent account at the reimbursement agent

Transaction Information and Status
Effective Interbank Settlement Date
ppp
When Date Time is chosen CBPR+ usage guidelines mandate the time zone that the time 
represents as an offset against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
368

pacs.008
pacs.008
Instructed
Agent: Agent A
Instructing
Agent: Agent B
Instructing
Agent: Agent A
Instructed
Agent: Agent B
Instructing Agent and Instructed Agent
represent the Agents involved in the pacs 
point-to-point message exchange. These 
roles therefore change on each payment 
leg.
A B C D
Instructing Agent and Instructed Agent elements are required in all pacs messages
Credit Transfer Transaction Information
Instructing Agent
Instructed Agent
pacs.004
Instructing
Agent: Agent B
Instructed
Agent: Agent C
pacs.002
Instructed
Agent: Agent B
Instructing
Agent: Agent C
369

g
Serial Financial Institution to Financial Institution to Customer Credit Transfer 
Use Case p.2.1.1 – High Level Payment Status Information (pacs.002) of multiple Payment Transaction Status updates
Use Case p.2.1.2 – High Level Rejection of an incomplete Customer Credit Transfer (pacs.008)
Serial Financial Institution Credit Transfer 
Use Case p.2.2.1 – High Level Rejection of an incomplete Financial Institution Credit Transfer (pacs.009)
Cover Method Financial Institution to Financial Institution to Customer Credit Transfer 
Use Case p.2.3.1.a – High Level Rejection of an incomplete payment using the cover method
Use Case p.2.3.1.b – High Level Rejection of an incomplete payment using the cover method
Financial Institution Direct Debit 
Use Case p.2.4.1 – High Level Status Information of a Financial Institution Direct Debit
Use Case p.2.4.2 – High Level Rejection of a Financial Institution Direct Debit
Financial Institution to Financial Institution Customer Direct Debit 
Use Case p.2.5.1 – High Level FI to FI Customer Direct Debit (pacs.003) successful settlement 
Use Case p.2.5.2 – High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement 
370

Agent B processes the payment 
on Agent C
pacs.008
pacs.002
1
1
Debtor initiates a payment 
instruction to the Debtor Agent
2
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
5
4
3
Agent B provides a status update 
ACTC (accepted technical 
validations are successful) to 
Agent A, based upon a bilateral 
agreement.
4
3
pacs.008 pacs.008
2
5
pacs.002
Agent B provides a further status 
update ACSP (accepted 
settlement in progress) to Agent 
A, based upon a bilateral 
agreement.
where bilaterally agreed, throughout the payment processing lifecycle i.e. from receipt through to onward
processing.
A B C D
Where a payment is rejected, the use of the pacs.002 
with the RJCT (Reject) status code is mandatory.
371

Having received the payment Agent 
D recognises the payment can not 
be completed as requested e.g. the 
Creditor’s account is closed. Agent 
D rejects the payment to Agent C 
using a Status information message 
(pacs.002) also including the return 
reason code.
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
pacs.008
pacs.004 pacs.004
1
Debtor initiates a payment 
instruction to the Debtor Agent
2
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
4
5
5
Agent C return funds to Agent B, 
together with the reason code for 
return.
Agent B return funds to Agent A, 
together with the reason code for 
return.
6
6
pacs.008 pacs.008
+ Return 
Reason 
+ Return 
Reason 
2
3 
pacs.002
+ Reject 
Reason 
A B C D
372

Having received the payment Agent 
D recognises the payment can not 
be completed as requested e.g. the 
Creditor’s account is closed. Agent 
D rejects the payment to Agent C 
using a Status Information message 
(pacs.002) also including the reject 
code.
pacs.004
1
1
Agent A as the Debtor initiates 
a payment instruction to the 
Debtor Agent (Agent B)
2
Agent C processes the 
payment onto Agent D
4
4 Agent C return funds to Agent B, 
together with the reason code for 
return.
Agent B advises Agent A of the return 
of payment together with the reason
using the camt.053 and may optionally 
provide a notification e.g. credit 
notification.
pacs.009
+ Return 
Reason 
2
5
pacs.009
pacs.002
3
Debtor Agent (B) debits the 
account of Agent A and 
initiates a serial payment 
towards the Creditor (Agent E) 
using Agents C as an 
intermediary.
2
+ Reject 
Reason 
A B C D E
5
373

Agent D requests the return of covering 
funds, together with the reason for 
return, having already rejected the 
pacs.008
Agent C produces an end of day account statement report. 
An optional real time notifications e.g. credit notification
(camt.054) may have also been created at the time of the 
credit posting
Agent C receives the payment 
and credits the account of 
Agent D
Agent B processes the 
payment on Agent C
pacs.004
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover method 
to the Creditor Agent (D)
2a
2b
2b
In parallel the Debtor Agent (A) initiates a covering 
payment to credit the account of Agent (D) with their 
correspondent (Agent C) 4 3
5
5
7
Agent C return of covering funds to 
Agent B, together with the reason code 
for return.
Agent B return of covering funds to 
Agent A, together with the reason code 
for return.
8
6b
+ Return 
Reason 
+ Return 
Reason 
3 4
A
B C
D
Having received the payment with settlement method 
COVE Agent D recognises (prior to the settlement via 
pacs.009 COV) the payment can not be completed as 
requested e.g. the Creditor’s account is closed. Agent 
D rejects the pacs.008 and will arrange the return of 
covering funds, when they arrive.
6b
7
8
+ Return 
Reason 
post-settlement returns see 
pacs.004 use case p.4.3.1.a 
and p.4.3.1.b
374
pacs.002
+ Reject 
Reason

Having not settled the pacs.009 cov 
Agent D rejects the covering funds, 
together with the reason for rejection.
Agent C receives the payment and credits their internal account with Agent D. 
Agent C forwards a pacs.009 cov with Settlement Method INDA (indicating 
Agent D is responsible for the settlement of this leg of the payment transaction.
Agent B processes the payment 
on to Agent C
pacs.004
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover method 
to the Creditor Agent (D)
2a
2b
2b
In parallel the Debtor Agent (A) 
initiates a covering payment to 
Agent (D) as the Creditor of the 
pacs.009 cov
3
4
6
Agent C returns the settled covering 
funds to Agent B, together with the 
reason code for return.
Agent C returns the settled covering 
funds to Agent B, together with the 
reason code for return.
7
7
5
+ Return 
Reason 
+ Return 
Reason 
3 4
5
A
B C
D
6
Having received the payment Agent D recognises the payment can not be 
completed as requested e.g. the Creditor’s account is closed. Having not 
settled the pacs.009 cov (or completed any accounting to the Creditor), 
Agent D rejected the pacs.008 providing the reject reason code.
375
+ Reject 
Reason 
pacs.002
post-settlement return see 
pacs.004 use case p.4.3.1.a

Agent C processes the payment 
on Agent D
pacs.009
Agent E initiates a Direct Debit
instruction to debit Agent A’s 
account
2
Debtor Agent (B) initiates a 
serial payment towards the 
Creditor Agent (E) using 
Agents B & C as intermediaries
3
pacs.009 camt.053
2
3
A
C D
E
376
1
B
Agent D credits the account of the 
Creditor (Agent E), and may 
optionally provide a notification 
e.g. credit notification in addition to 
an account statement (camt.053)
4
4
1a pacs.002
Agent B provides a positive 
status update to Agent E
1a

pacs.010
Agent D initiates a Direct Debit
instruction to debit Agent A’s 
account
Debtor Agent (B) rejects the 
instruction, using a pacs.002, 
as no mandate agreement is in
place.
A
C
D
E
377
1
B
pacs.002

camt.053
1
1
Creditor initiates a direct debit 
instruction to the Creditor Agent
Creditor Agent (A) initiates a 
direct debit collection by 
sending a pacs.003 message to 
the Debtor Agent with the 
settlement method “INDA”
3
The Debtor Agent debits the account 
of the Debtor, and may optionally 
provide a notification e.g. debit 
notification in addition to an account 
statement (camt.053). The Debtor 
Agent also provides a status update 
ACSC (accepted settlement 
completed) to the Creditor Agent. 
pacs.003 pain.008
pain.002
3
Settlement 
Complete
Creditor Agent (A) relays the status 
ACSC (accepted settlement 
completed) to the Initiating Party, 
based upon a bilateral agreement
A
378
pacs.002
4
4
B
2
2

1
1
Creditor initiates a direct debit 
instruction to the Creditor Agent
Creditor Agent (A) initiates a 
direct debit collection by 
sending a pacs.003 message to 
the Debtor Agent with the 
settlement method “INDA”
3
The Debtor Agent fails to debit the 
account of the Debtor (e.g., account 
is closed). The Debtor Agent 
provides a status update RJCT 
(Rejected) with the rejection reason 
information. 
pacs.003 pain.008
pain.002
3
Creditor Agent (A) relays the status 
RJCT (Rejected) to the Initiating 
Party with the rejection reason 
information
A
379
pacs.002
4
4
B
Reject 
Reason 
2
2

Payment Return
380

pacs.008
Group Header
Credit Transfer 
Transaction 
Information
pacs.009 cov
Group Header
Credit Transfer 
Transaction 
Information
Underlying 
Customer 
Credit
pacs.004
Group Header
Transaction 
Information
Original Group 
Information
Original 
Transaction 
Reference
underlying Customer Credit Transfer, the 
pacs.004 Payment Return message has amongst 
other elements Original Group Information which 
captures original information such as the Original 
UETR and Original Interbank Settlement Amount 
etc. and an Original Transaction Reference which 
contain the key elements of the original payment 
e.g. Debtor, Creditor etc. 
381

pacs.008
pacs.002
pacs.008
pacs.004
pacs.002 Return & 
Reason 
pacs.002
Reject & 
Reason 
A B C
The PaymentReturn 
message is sent by 
an agent to the 
previous agent in the 
payment chain to 
undo a payment 
previously settled. 
382
In the unlikely event that a pacs.004 is instructed by mistake, the best practice is to allow the Payment Return 
to complete and request (using Exceptions and Investigations) the instruction to be re-initiated. The Payment 
Return of a Payment Return should be avoided, as should the Rejection Status Notification of Payment Return.

383

pygg, 
Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact
equivalent in the legacy MT payment message. However, the MT 202 Sender’s Reference (Field
20) could be considered a similar comparison where a pacs message contains a single
Transaction.
Each transaction’s Credit Transfer Transaction Information contains a variety of nested
Payment Identification elements to capture reference related to the individual transaction such
as a UETR (Unique End-to-endTransactionReference)
Group Header Message Identification
384

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
385

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 
Group Header Number of Transactions
386
g
Single transactions in the CBPR+ payment usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant payments, supporting the next
generation of innovation.

Group Header Settlement Information Settlement Method
D
27
387
The Settlement Method element in the pacs.004 allows a choice of an embedded code.
INDA indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account 
Servicing Institution) The account held at the Instructed Agent may captured in the dedicated Settlement 
Account element.
INGA indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who 
has credited the Account they service for the Instructed Agent (as an Account Owner). The account held 
by the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account 
element.
$
€
Settlement Method code CLRG is not part of CBPR+ specifications but instead used in 
Market Infrastructure specification (HVPS+)

Group Header Settlement Information
388
The Settlement Account identifies the account details maintained at the account
servicing institution (Agent responsible for the settlement of the instruction as
indicated in the Settlement Method)
Min 0 – Max 1
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
Name identifies the name of the account as assigned by the Account Servicing
Institution
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

389

The 35 character return identifier could be considered similar to the legacy Sender’s
Reference (Field 20) of an MT return payment message.
390
Transaction Information Return Identification

gyg pyyy
Original Message Identification contains the point-to-point reference, and the mandatory Original
Message Name Identification contains the message name of the underlying payment being returned.
Optionally the Original Creation Date Time can also be captured.
pacs.004
A B For example:
Original Message Name Identification “pacs.008.001.xx” confirms the
return is of a pacs.008 Financial Institution to Financial Institution
Customer Credit Transfer. Where as “pacs.009.001.xx” confirms the
return is of a pacs.009 Financial Institution Credit Transfer.
Message 
Identification abcd1234
pacs.008.001.08 Original Message 
Name Identification
Original Message 
Identification abcd1234
Message 
Identification xyz9875
Original Group
Information 
Group Header
Transaction Information Original Group Information
pacs.008
391
Note: the xx in the CBPR+ Usage Guideline 
represents the message version of the message 
received for example pacs.008.001.08

pyg pyy
Mandatory element examples of this (in addition to Original Message identification and Original Message
Name Identification described on the previous page) include:
Original 
Interbank 
Settlement
Date
Original 
Interbank 
Settlement
Amount
Original 
UETR
Original 
End to End
Identification These Original elements enables the Instructed Agent in the
pacs.004 Payment Return to re-associate the Return with the
payment they originally sent.
Transaction Information
Original End to end Identification
Original UETR
Original Interbank Settlement Amount
Original Interbank Settlement Date
392

The Returned Interbank Settlement Amount and subsequent Interbank Settlement
Date are mandatory elements in the pacs.004 Payment Return, these elements are
used to capture the currency and amount being returned together with the settlement
date of the Payment Return.
The Returned Interbank Settlement Amount may be a different amount than the Original Interbank 
Settlement Amount (amount received the Agent instructing the Payment Return) for example a charge may 
have been levied for processing the Payment Return or the Payment Return is a partial amount for 
overpayment or partial refund
In this case the Returned Instructed Amount should be equal to the Interbank Settlement Amount, on the 
first leg of the Payment Return. Charge levied should also be captured in the Charge Information element.
$
Transaction Information
Returned Interbank Settlement Amount
Interbank Settlement Date
393

of the instructions. 
394
Min 0 – Max 1
The Settlement Priority provides an optional choice of embedded codes to indicate the instruction’s 
settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by 
the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused 
with the Instruction Priority. 
Min 0 – Max 1
The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator 
such as a Market Infrastructure. 
This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time. 
Note: Where the Settlement Method of the pacs.004 is ‘INDA’ (settled performed by the Instructed
Agent) this indicates the Settlement Priority. Code ‘INGA’ implies settlement has already occurred
for this point-to-point payment and therefore the SettlementPriority is not necessary.
Transaction Information

395
The Returned Instructed Amount captures currency and amount instructed by the Debtor in the
Return Chain. This conditional element is required when the Returned Interbank Settlement
Amount is not the same currency and/or amount as originally instructed by the Debtor. For example
a charge is taken or the transactions is converted to another currency.
The Exchange Rate capture the factor (rate) used to convert an amount from one currency into 
another. This reflects the currency pair price at which one currency was bought with another 
currency.
Min 0 – Max 1
Min 0 – Max 1
£
$100
¥
Transaction Information

y gpg pyp
with MT Field 71A ‘Details of Charges’
71A: Details 
of Charges 
Code Description
BEN Beneficiary
SHA Shared Charges
Charge 
Bearer
(1.1)
Code Description
CRED Creditor
SHAR Shared
Note: Charge Bearer code DEBT (implying the Return Chain, Debtor will bear any charges) is removed from 
the CBPR+ pacs.004. Should a non-CBPR+ Payment Return be received with Charge Bearer DEBT, it is 
recommended to use SHAR in any onward processed Payment Return.
Transaction Information Charge Bearer
396

Charge 
Information
(0.*)
Amount
Currency
Agent BICFI
Name
StructuredPostal Address
pgg
although pre-paid charges (legacy 71G ‘Receiver’s Charges’ are an unlikely use case for Payment Returns 
In addition to the legacy MT message the pacs.004 Charge
Information mandate the Agent, this represent the Agent
who has taken a charge (deduct from the transaction)
CBPR+ best practice recommends the use of the structured
Agent BIC.
Note: Charge Information element is required where a charge is taken on the Payment Return. A charge for 
returning an incomplete payment by the originator of the Payment Return (Return Chain Debtor) is common 
practice. It is encouraged that Agents who processed the original payment transaction consider the total 
operation cost when defining their payment cost recovery model. Whereby further charges on Return Payments 
should be avoided.
As the Charges Information element is repetitive it can capture charges related to previous legs of the 
Payment Return transaction chain.
Transaction Information Charge Information
397

pacs.008
pacs.008
Instructed
Agent: Agent A
Instructing
Agent: Agent B
Instructing
Agent: Agent A
Instructed
Agent: Agent B
Instructing Agent and Instructed Agent
represent the Agents involved in the pacs 
point-to-point message exchange. These 
roles therefore change on each payment 
leg.
A B C D
Transaction Information
Instructing Agent
Instructed Agent
pacs.004
Instructing
Agent: Agent B
Instructed
Agent: Agent C
pacs.004
Instructed
Agent: Agent B
Instructing
Agent: Agent C
398
pacs.008
Instructing
Agent: Agent C
Instructed
Agent: Agent D
pacs.002
Instructed
Agent: Agent C
Instructing
Agent: Agent D

A B C E
Debtor Debtor Agent Instructed Agent & 
Creditor Agent Creditor Previous Instructing 
Agent 1
Instructing Agent
A B C E
Creditor Creditor Agent Debtor Agent &
Instructing Agent
Debtor Intermediary
Agent 2
Instructed Agent 
D
Previous Instructing 
Agent 2
D
Intermediary
Agent 1
Note: the static Previous Instructing Agent roles in the original payment transition to 
Intermediary Agent roles in the return chain.
Account for parties in the return chain are not enable in version 9 of the pacs.004 
therefore any Return Chain account TextualRules can be ignored 399
In this element the role of the various parties change, to reflect the fact the payment is now a Payment Return, for example,
the CreditorAgent of the underlying payment may become the Debtor Agent of the Payment Return.
Although Ultimate Debtor and Ultimate Creditor are present in the Return chain it is extremely unlikely one of these Parties 
would be involved in the return chain and can only do so if present as an Ultimate Party in the original payment.
original return chain
Transaction Information

gpy, gy (y
owe the money to the party the return is intended for).
Recognising that the original Creditor is not party to the return, for example, they might be a known customer
of the original Creditor Agent whereby a reject or return code ‘AC01’ may be used. In this way the original
Creditor was not involved in the Payment Return.
A B C E
Debtor Debtor Agent Instructed Agent & 
Creditor Agent Creditor Previous Instructing
Agent 1
Instructing Agent
A B C
Creditor Creditor Agent Intermediary Agent 2 Intermediary Agent 1
D
Previous Instructing
Agent 2
400
Debtor &
Instructing Agent
Debtor Agent &
Instructed Agent
D E
original return chain
Transaction Information
Note: the static Previous Instructing Agent roles in the original payment transition to Intermediary 
Agent roles in the return chain

y (y y py
the return is intended for). And the mandatory Creditor in the Return Chain element is the party the payment
is being returned to.
A B C E
Debtor Debtor Agent Instructed Agent Creditor Instructing Agent
A B C
Creditor Creditor Agent
D
401
Debtor &
Instructing Agent
Debtor Agent &
Instructed Agent
original return chain
Transaction Information
Note: a party Rejecting the payment using a pacs.002 would not be considered to be involved in 
the Payment Return as they would not owe money to the party the return is intended for.
Intermediary Agent 1 Creditor Agent

p
element:
The code list representing the 
Return Reason is part of the 
ISO 20022 external code list
Transaction Information Return Reason Information
Originator
Reason
Additional Information
• the Originator element helps identify the party who initiated the request to return the
payment. This party would have been included in the underlying payment and may also be
included the pacs.004 Return Chain.
• the Reason is mandatory and is represented by an externalised Code choice ( )
• the Additional Information element may also be included to provide further details on the
reason for return.
402 Take me to the external code list section
?

403
Account number is missing
AC02 InvalidDebtorAccountNumber Debtor account number invalid or missing Sent by any Agent w hen Debtor account number is incomplete
AC04 ClosedAccountNumber Account number specified has been closed on the bank of 
account's books
Sent by Creditor Agent w hen the Creditor account number is closed
AC06 BlockedAccount Account specified is blocked, prohibiting posting of transactions 
against it.
Sent by Creditor Agent w hen Creditor account is blocked from posting credit 
entries.
Sent by any Agent w hen a settlement account is blocked
AC07 ClosedCreditorAccountNumber Creditor account number closed
Sent by Creditor Agent w hen account number is closed. 
CBPRplus recommend using AC04, but support AC07 to remain interoperable 
with other clearing systems.
AC13 InvalidDebtorAccountType Debtor account type is missing or invalid Sent by any Agent w hen Debtor account type element is incorrect
AGNT IncorrectAgent Agent in the payment w orkflow is incorrect
Sent by any Agent w hen an agent in the payment transaction has an incorrect 
identification element
AG01 TransactionForbidden Transaction forbidden on this type of account (formerly 
NoAgreement)
Sent by any Agent w hen the type of payment transaction is not allow ed for the 
specified account
AG07 UnsuccesfulDirectDebit
Debtor account cannot be debited for a generic reason.
Code value may be used in general purposes and as a 
replacement for AM04 if debtor bank does not reveal its 
customer's insufficient funds for privacy reasons
Sent by Debtor Agent of a Direct Debit message, w hen debtor account can not 
be debited.
AM02 NotAllow edAmount Specific transaction/message amount is greater than allow ed 
maximum
Sent by any Agent w hen payment amount is above an allow ed amount. For 
example the clearing system w ith a upper amount threshold.

404
AM03 NotAllowedCurrency 
outside of existing agreement
existing business agreement
AM04 InsufficientFunds Amount of funds available to cover specified message 
amount is insufficient.
Sent by any Agent w hen there is not sufficient funds to settle the payment 
transaction.
AM05 Duplication Payment is a duplicate of another payment
Sent by any Agent w hen the payment is a duplicate. CBPRplus recommend 
using DUPL, but support AM05 to remain interoperable with other clearing 
systems.
AM06 TooLowAmount Specified transaction amount is less than agreed 
minimum.
Sent by any Agent w hen the payment amount is below a minimum amount.
AM07 BlockedAmount Amount specified in message has been blocked by 
regulatory authorities Sent by any Agent w hen the payment amount is blocked by regulators
AM09 WrongAmount Amount received is not the amount agreed or expected Sent by any Agent w hen the payment amount is incorrect
BE01 InconsistenWithEndCustomer
Identification of end customer is not consistent with 
associated account number (formerly 
CreditorConsistency).
Sent by Creditor Agent w hen there is an inconsistency betw een the Creditor’s 
identification and the account number
BE04 MissingCreditorAddress
Specification of creditor's address, which is required for 
payment, is missing/not correct (formerly 
IncorrectCreditorAddress).
Sent by any Agent w hen the Creditor’s address is missing
Sent by Creditor Agent w hen the Creditor’s address is incorrect
BE05 UnrecognisedInitiatingParty Party who initiated the message is not recognised by the 
end customer
Sent by Creditor Agent w hen the initiating party is unknow n to the beneficiary
BE07 MissingDebtorAddress Specification of debtor's address, which is required for 
payment, is missing/not correct.
Sent by any Agent w hen the address of the Debtor is missing or incorrect

405
BE10 InvalidDebtorCountry Debtor country code is missing or invalid Sent by any Agent w hen the country code of the Debtor is missing or incorrect
BE11 InvalidCreditorCountry Creditor country code is missing or invalid Sent by any Agent w hen the country code of the Creditor is missing or 
incorrect
BE16 InvalidDebtorIdentificationCode Debtor or Ultimate Debtor identification code missing or 
invalid
Sent by any Agent w hen the identification of the Debtor or Ultimate Debtor is 
missing or incorrect
BE17 InvalidCreditorIdentificationCode Creditor or Ultimate Creditor identification code missing 
or invalid
Sent by the any Agent w hen the identification of the Creditor or Ultimate
Creditor is missing or incorrect
CN01 AuthorisationCancelled Authorisation is cancelled. Sent by any Agent w hen a third party debit authorisation has been cancelled 
or is not in place.
CNOR Creditor bank is not registered Creditor bank is not registered under this BIC in the 
Clearing Settlement Mechanism (CSM)
Sent by any Agent w hen the Creditor Agent is not reachable in the Market 
Infrastructure (CSM) and an appropriate correspondent can not be determined.
CURR IncorrectCurrency Currency of the payment is incorrect
Sent by the Creditor Agent w hen the Interbank Settlement Amount 
Currency is not the same as the Creditor account currency and a currency 
conversion is not accepted on the Creditor’s account. 
CUST RequestedByCustomer Cancellation requested by the Debtor Sent by any Agent upon request by Debtor. CBPRplus recommend using 
FOCR, but support CUST to remain interoperable with other clearing systems.
DT01 InvalidDate Invalid date (eg, wrong or missing settlement date) Sent by any Agent w hen the settlement date is in the past and an agreement 
is in place to reject rather than apply the next possible value date.
DT04 FutureDateNotSupported Future date not supported Sent by any Agent w hen a future settlement date is not supported or appear to 
be an error e.g. is the w rong year.

406
DUPL DuplicatePayment Payment is a duplicate of another payment 
y y gpyp
ERIN ERIOptionNotSupported The Extended Remittance Information (ERI) option is not 
supported.
Sent by any Agent w hen extended Remittance information (Related 
Remittance Information) is not supported or bilaterally/multilaterally agreed
ED05 SettlementFailed Settlement of the transaction has failed. Sent by any Agent w hen the settlement of payment has failed or been 
unsuccessful. 
FF03 InvalidPaymentTypeInformation
Payment Type Information is missing or invalid.
Generic usage if cannot specify Service Level or Local 
Instrument code
Sent by any Agent w hen the Payment Type Information (Instruction Priority, 
Clearing Channel) provided for the payment is incorrect or not supported. 
FF04 InvalidServiceLevelCode Service Level code is missing or invalid
Sent by any Agent w hen the Payment Type Information Service Level
provided for the payment is incorrect or not supported
FF05 InvalidLocalInstrumentCode Local Instrument code is missing or invalid
Sent by any Agent w hen the Payment Type Information Local Instrument
provided for the payment is incorrect or not supported
FF06 InvalidCategoryPurposeCode Category Purpose code is missing or invalid
Sent by any Agent w hen the Payment Type Information Category Purpose
provided for the payment is incorrect or not supported
FF07 InvalidPurpose Purpose is missing or invalid Sent by any Agent w hen the Purpose provided for the payment is either 
missing or incorrect
FOCR FollowingCancellationRequest Return following a cancellation request Sent by any Agent that has accepted a payment cancellation request 
(camt.056) and subsequently is rejecting the unsettled payment instruction.
FR01 Fraud Returned as a result of fraud. Sent by any Agent w hen the payment is identified as fraudulent.
MD01 NoMandate No Mandate Sent by any Agent w hen a Direct Debit message has no mandate in place.

407
MD02 
Mandatescheme is missing.
missing.
MD05 CollectionNotDue Creditor or creditor's agent should not have collected the 
direct debit
Sent by any Agent w hen a Direct Debit collection w as not due
MD07 EndCustomerDeceased End customer is deceased. Sent by Creditor Agent w hen the Creditor or Ultimate Creditor is deceased
MS02 NotSpecifiedReasonCustomer 
Generated Reason has not been specified by end customer Sent by Creditor Agent w here instructed to reject by the Creditor, but no 
reason w as specified
MS03 NotSpecifiedReasonAgent 
Generated Reason has not been specified by agent. Sent by any Agent but no reason is specified
NARR Narrative Reason is provided as narrative information in the 
additional reason information.
Sent by any Agent the reason is provided as narrative information. Only to be 
used where no other code is appropriate! (i.e. exceptional circumstances)
NOAS NoAnswerFromCustomer No response from Beneficiary
Sent by any Agent w hen the Creditor did not respond to query for additional 
information in order that the payment could be credited e.g. currency control 
documentation.
NOCM Not compliant (more generic)
Customer account is not compliant with regulatory 
requirements, for example FICA (in South Africa) or any 
other regulatory requirements which render an account 
inactive for certain processing.
Sent by any Agent w hen the Creditor account is not compliant w ith certain 
regulatory requirements.
RC01 BankIdentifierIncorrect
Bank Identifier code specified in the message has an 
incorrect format (formerly 
IncorrectFormatForRoutingCode).
Sent by any Agent w hen an incorrect BIC has been used in the payment
RC03 InvalidDebtorBankIdentifier Debtor bank identifier is invalid or missing Sent by any Agent w hen the Debtor Agent identification is incorrect or missing

408
RC04 InvalidCreditorBankIdentifier Creditor bank identifier is invalid or missing Sent by any Agent w hen the Creditor Agent identification is incorrect or 
missing
RC08 InvalidClearingSystemMemberIden
tifier
ClearingSystemMemberidentifier is invalid or missing.
Generic usage if cannot specify between debit or credit 
account
Sent by any Agent w hen the clearing system member identification for an 
Agent is incorrect
RC11 InvalidIntermediaryAgent Intermediary Agent is invalid or missing Sent by any Agent w hen the intermediary agent identification is incorrect
RF01 NotUniqueTransactionReference Transaction reference is not unique within the 
message.
Sent by any Agent w hen the transaction reference (UETR and Instruction 
Identification) are not unique
RR01 Missing Debtor Account or 
Identification
Specification of the debtor’s account or unique 
identification needed for reasons of regulatory 
requirements is insufficient or missing
Sent by any Agent w hen the Debtor identification or debtor account is 
missing, or the information provided are not sufficient
RR02 Missing Debtor Name or Address Specification of the debtor’s name and/or address needed for 
regulatory requirements is insufficient or missing.
Sent by any Agent since the Debtor name or Address is missing, or 
information provided is not sufficient
RR03 Missing Creditor Name or Address Specification of the creditor’s name and/or address needed 
for regulatory requirements is insufficient or missing.
Sent by any Agent since the Creditor name or Address is missing, or 
information provided is not sufficient
RR04 Regulatory Reason Regulatory Reason Sent by any Agent due to any unspecified regulatory reason
RR05 RegulatoryInformationInvalid Regulatory or Central Bank Reporting information missing, 
incomplete or invalid.
Sent by any Agent w hen the reporting information required by the central 
bank or reporting authority is missing or not complete
RR06 TaxInformationInvalid Tax information missing, incomplete or invalid. Sent by any Agent w here required tax information is missing, not valid or not 
complete

409
for payment type.
RR08 RemittanceInformationTruncated Remittance information truncated to comply w ith rules for 
payment type.
Sent by any Agent w here the Structured Remittance Information has not 
been bilaterally or multilaterally agreed, w hich or has resulted in truncation
RR09 InvalidStructuredCreditorReference Structured creditor reference invalid or missing.
Sent by any Agent w hen the structure of the creditor reference in the 
remittance information is invalid or missing
RR11 InvalidDebtorAgentServiceID Invalid or missing identification of a bank proprietary service. Sent by any Agent w here the proprietary identification for the Debtor is 
invalid or not understood
RR12 InvalidPartyID Invalid or missing identification required w ithin a particular 
country or payment type.
Sent by any Agent w here a proprietary party identification is considered 
invalid or not understood
RUTA ReturnUponUnableToApply Return following investigation request and no remediation 
possible.
Sent by any Agent that is unsatisfied w ith the outcome of the unable to 
apply request and is subsequently rejecting the payment instruction.
Alternatively it can be used by the original Creditor Agent w hen the creditor 
is unable to apply the transaction
TM01 Invalid Cut off time
Associated message, payment information block, or 
transaction was received after agreed processing cut-off 
time.
Sent by any Agent w hen the message w as received after the agreed 
processing cut off time and an agreement is in place to reject rather than 
apply the next possible value date.
UPAY UnduePayment Payment is not justified. Sent by any Agent the payment is undue

gpy pg
The inclusion of this element is particularly useful where the Payment Return includes an Agent not party to
the original transaction, or where a significant time lapse has occurred between the original payment and the
Payment Return i.e., information may have been archived by Agent in the Return chain.
CBPR+ has two rules describing when the Original Transaction Reference should be used.
The Amount within the nesting of this Original Transaction Reference element only allows for the Instructed
Amount, as instructed by the Debtor in the original payment initiation request. If the Instructed Amount was
present in the original payment, populating this data is simple. However, we should also recognise the
Instructed Amount is not always present (and in fact is not available in the pacs.009), whereby this value
should represent the amount in the Interbank Settlement Amount of the pacs message being returned. The
use of Instructed Amount is best described in the pacs.008 Currency and Amount section.
Transaction Information Original Transaction Reference
410
Note: the role of Parties and Agent in Original element remain unchanged 
unlike elements such as the Return chain

Within the Payment Return (pacs.004)
• the Original Group Information element is used to refers to original message for which the return relates to. 
e.g. based upon the above example pacs.008 as the original message would be included in the pacs.004 
• the Transaction Information > Original UETR element would include UETR of the payment message 
received. i.e. the same UETR is used on the Payment Return.
• the Original Transaction Reference element includes detail from the Original Message Name Identification
e.g. the Debtor of the original pacs.008.001.xx 
• the Return Chain element includes the parties in the return payment chain, noting the parties reverse (i.e.
change role) from the original payment whereby the Debtor of the original payment becomes the Creditor
in the Return Chain.
pacs.008
pacs.004 pacs.004
pacs.008 pacs.008
+ Return 
Reason 
+ Return 
Reason 
pacs.002
+ Reject 
Reason 
A B C D
411

Serial Customer Payments
Use Case p.4.1.1 – Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008)
Use Case p.4.1.2 – Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008)
Use Case p.4.1.2.a – Partial Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008)
Use Case p.4.1.2.b – Refund Payment of a complete Customer Credit Transfer (pacs.008)
Use Case p.4.1.3 - Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008) involving a Market Infrastructure
Serial Financial Institution Payments
Use Case p.4.2.1 - Payment Return (pacs.004) of an incomplete Financial Institution Credit Transfer (pacs.009)
Use Case p.4.2.2 - Payment Return (pacs.004) of a complete Financial Institution Credit Transfer (pacs.009)
Use Case p.4.2.3 - Payment Return (pacs.004) of an incomplete Financial Institution Credit Transfer (pacs.009) involving a Market Infrastructure
Cover Method Payments
Use Case p.4.3.1.a - Payment Return (pacs.004) of an incomplete payment using the cover method
Use Case p.4.3.1.b - Payment Return (pacs.004) of an incomplete payment using the cover method
Use Case p.4.3.2 - Payment Return (pacs.004) of a complete payment using the cover method
Use Case p.4.3.2.a - Payment Return (pacs.004) of a complete payment using the cover method
Use Case p.4.3.3 - Payment Return (pacs.004) of an incomplete cover payment
412

Having received the payment Agent 
D recognises the payment can not 
be completed as requested e.g. the 
Creditor’s account is closed. Agent 
D return the payment to Agent C 
(as the original payment had 
already settled) together with the 
return reason.
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
pacs.008
pacs.004 pacs.004
1
Debtor initiates a payment 
instruction to the Debtor Agent
2
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
4
5
5
Agent C return funds to Agent B, 
together with the reason code for 
return.
Agent B return funds to Agent A, 
together with the reason code for 
return.
6
6
pacs.008 pacs.008
+ Return 
Reason 
+ Return 
Reason 
2
3 
pacs.004
+ Return 
Reason 
A B C D
413

Creditor determines that they wish 
to return the payment e.g. they are 
unable to apply, and instructs their 
bank (Agent D) to return the 
payment together with the reason.
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
pacs.008
pacs.004 pacs.004
1
Debtor initiates a payment 
instruction to the Debtor Agent
2
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
4
7
Agent C return funds to Agent B, together 
with the reason code for return.
Agent B return funds to Agent A, 
together with the reason code for return.
8
8
pacs.008 pacs.008
+ Return 
Reason 
+ Return 
Reason 
2
3 
pacs.004
+ Return 
Reason 
5
6
Agent D credits the account of 
the Creditor, and may optionally 
provide a notification e.g. credit 
notification in addition to an 
account statement (camt.053)
5
6
Agent D returns the payment to 
Agent C using a Payment Return 
message (pacs.004) also 
including the return reason code.
.
A B C D
7
414

Creditor determines that they wish 
to partially return the payment e.g. 
they were over paid or provide a 
partial refund, and instructs their 
bank (Agent D) to partially return 
the payment together with the 
reason.
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
pacs.008
pacs.004 pacs.004
1
Debtor initiates a payment 
instruction to the Debtor Agent
2
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
4
7
Agent C return funds to Agent B, together 
with the reason code for return.
Agent B return funds to Agent A, 
together with the reason code for return.
8
8
pacs.008 pacs.008
+ Return 
Reason 
+ Return 
Reason 
2
3 
pacs.004
+ Return 
Reason 
5
6
Agent D credits the account of 
the Creditor, and may optionally 
provide a notification e.g. credit 
notification in addition to an 
account statement (camt.053)
5 6
Agent D returns the payment to 
Agent C using a Payment Return 
message (pacs.004) also 
including the return reason code.
.
A B C D
7
415

Creditor determines that they wish 
to refund the payment e.g. they 
could not provide the goods or 
services paid for. They instruct a 
new payment from their bank 
Agent C processes the payment account.
on Agent D
Agent B processes the payment 
on Agent C
pacs.008
1
Debtor initiates a payment 
instruction to the Debtor Agent
2
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
4
pacs.008 pacs.008
2
3 
5
Agent D credits the account of 
the Creditor, and may optionally 
provide a notification e.g. credit 
notification in addition to an 
account statement (camt.053)
5
A B C D
416
In some circumstances the Creditor may take it upon themselves to provide a refund, using a new 
payment. Equally the period the original payment is store prior to data archive, particularly by the Creditor 
Agent, is not indefinite. Whereby a new payment may be used as a refund. Due to the nature of this 
refund not being identified as a Payment Return, reversal indicatory in the statement entry and reason 
codes describing the nature of the refund are unlikely.

Having received the payment Agent 
B recognises the payment can not 
be completed as requested e.g. the 
Creditor’s account is closed. Agent 
B returns the payment to Agent A 
using a Payment Return message 
(pacs.004) also including the return 
reason code.
The payment is settled via the 
local ISO 20022 Market 
Infrastructure, whereby the 
payment is forwarded to the 
Creditor Agent (B)
pacs.008
pacs.004
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (B) using the 
local currency ISO 20022 
Market Infrastructure
3 4
The Market Infrastructure returns the 
payment performing the necessary 
settlement posting between Agent B 
and Agent A.
4
pacs.008
+ Return 
Reason 
2
+ Return 
Reason 
A pacs.004 B
pre-settlement reject see 
pacs.002 section
Market Infrastructure will either conform to HVPS+ guidelines or establish their 
own usage guidelines based on the ISO 20022 standard.
417

Having received the payment 
instruction Agent D recognises the 
payment can not be completed as 
requested e.g. the Creditor’s account 
is closed. Agent D rejects the 
payment to Agent C using a Status 
Information message (pacs.002) also 
including the return reject code.
pacs.004
1
1
Agent A as the Debtor initiates 
a payment instruction to the 
Debtor Agent (Agent B)
2
Agent C processes the 
payment onto Agent D
4
4 Agent C return funds to Agent B, 
together with the reason code for 
return.
Agent B advises Agent A of the return 
of payment together with the reason
using the camt.053 and may optionally 
provide a notification e.g. credit 
notification.
pacs.009
+ Return 
Reason 
3
5
pacs.009
pacs.002
3
Debtor Agent (B) debits the 
account of Agent A and 
initiates a serial payment 
towards the Creditor (Agent E) 
using Agents C as an 
intermediary.
2
+ Reject 
Reason 
A B C D E
5
418
camt.053
pacs.009

Having received the payment Agent 
D recognises the payment is 
incorrect e.g. the wrong amount 
was received . Agent D sends a 
Payment Return to Agent C 
including the return reason.
pacs.004
1
1
Agent A as the Debtor initiates 
a payment instruction to the 
Debtor Agent (Agent B)
2
Debtor Agent (B) debits the 
account of Agent A and 
initiates a serial payment 
towards the Creditor (Agent D) 
using Agents C as an 
intermediary.
4
4 Agent C return funds to Agent B, 
together with the reason code for 
return.
Agent B advises Agent A of the return 
of payment together with the reason 
using the camt.053 and may optionally 
provide a notification e.g. credit 
notification.
pacs.009
+ Return 
Reason 
2
camt.053
3
Creditor Agent (C) credits the 
account of Agent D and may 
optionally provide a notification 
e.g. credit notification, in 
addition to an account 
statement (camt.053)
3
A B C pacs.004 D
5
5
+ Return 
Reason 
419
camt.053
pacs.009

Having received the payment Agent 
C recognises the payment can not 
be completed as requested e.g. the 
Creditor’s account is closed. Agent 
C returns the payment towards 
Agent B using a Payment Return 
message (pacs.004) also including 
the return reason code.
pacs.004
1
Agent A as the Debtor initiates 
a payment instruction to the 
Debtor Agent (Agent B)
2
Debtor Agent (B) debits the 
account of Agent A and 
initiates a serial payment 
towards the Creditor (Agent D) 
using the local currency ISO 
20022 Market Infrastructure.
4
Agent B advises Agent A of the return 
of payment together with the reason 
using the camt.053 and may optionally 
provide a notification e.g. credit 
notification.
pacs.009
+ Return 
Reason 
2
pacs.009
+ Return 
Reason 
pacs.004
The payment is settled via the 
local ISO 20022 Market 
Infrastructure, whereby the 
payment is forwarded to the 
Creditor Agent (C)
3
5
5
The payment return is settled via the 
local ISO 20022 Market Infrastructure, 
whereby the payment return is 
forwarded to the Creditor Agent (B)
4 Agent C returns the payment to 
Agent B, together with the reason 
code for return via the local currency 
ISO 20022 Market Infrastructure.
A B C
6
6
Market Infrastructure will either conform to HVPS+ guidelines or establish their 
own usage guidelines based on the ISO 20022 standard.
D
420
camt.053
pacs.009

Agent D instructs the return of settled 
covering funds, together with the 
reason for return.
Agent C produces an end of day account 
statement report. An optional real time 
notifications e.g. credit notification
(camt.054) may have also been created 
at the time of the credit posting
Agent C receives the payment 
and credits the account of 
Agent D
Agent B processes the payment 
on to Agent C
pacs.004
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover method 
to the Creditor Agent (D)
2a
2b
2b
In parallel the Debtor Agent (A) 
initiates a covering payment to 
credit the account of Agent (D) 
with their correspondent (Agent 
C)
3
4 5
5
7
Agent C returns the settled covering 
funds to Agent B, together with the 
reason code for return.
Agent C returns the settled covering 
funds to Agent B, together with the 
reason code for return.
8
8
6
+ Return 
Reason 
+ Return 
Reason 
3 4
6
A
B C
D
7
Having received the payment, Agent D recognises the payment can not be 
completed as requested e.g. the Creditor’s account is closed. Having not 
completed any accounting to the Creditor, but with the payment having 
settled Agent D can only return the payment also providing the return
reason code.
421
+ Return 
Reason 
pre-settlement rejects see 
pacs.004 use case p.2.3.1

Having not settled the pacs.009 cov 
Agent D rejects the covering funds, 
together with the reason for rejection.
Agent C receives the payment and credits their internal account with Agent D. 
Agent C forwards a pacs.009 cov with Settlement Method INDA (indicating 
Agent D is responsible for the settlement of this leg of the payment transaction.
Agent B processes the payment 
on to Agent C
pacs.004
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover method 
to the Creditor Agent (D)
2a
2b
2b
In parallel the Debtor Agent (A) 
initiates a covering payment to 
Agent (D) as the Creditor of the 
pacs.009 cov
3
4
6
Agent C returns the settled covering 
funds to Agent B, together with the 
reason code for return.
Agent B returns the settled covering 
funds to Agent A, together with the 
reason code for return.
7
7
5
+ Return 
Reason 
+ Return 
Reason 
3 4
5
A
B C
D
6
Having received the payment Agent D recognises the payment can not be 
completed as requested e.g. the Creditor’s account is closed. Having not 
settled the pacs.009 cov (or completed any accounting to the Creditor), 
Agent D rejected the pacs.008 providing the reject reason code.
422
+ Reject 
Reason 
pacs.002
post-settlement return see 
pacs.004 use case p.4.3.1.a

Agent D requests the return of 
covering funds, together with the return 
reason.
Agent C produces an end of day 
account statement report. An 
optional real time notifications e.g. 
credit notification may have also 
been created at the time of the 
credit posting
Agent C receives the payment and 
credits the account of Agent D
Agent B processes the payment 
on Agent C
pacs.004
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover method 
to the Creditor Agent (D)
2a
2b
2b
In parallel the Debtor Agent (A) 
initiates a covering payment to 
credit the account of Agent (D) 
with their correspondent (Agent 
C)
3
4
5
5
8
Agent C return of covering funds to 
Agent B, together with the reason code 
for return.
Agent B return of covering funds to 
Agent A, together with the reason code 
for return.
9
9
7
+ Return 
Reason 
+ Return 
Reason 
3 4
Creditor determines that they wish 
to return the payment e.g. they are 
unable to apply, and instructs their 
bank (Agent D) to return the 
payment together with the reason.
Agent D reconciles the covering 
funds and credits the account of the 
Creditor, and may optionally 
provide a notification e.g., credit 
notification (camt.054)
6
7
A
B C
D
8
423
+ Return 
Reason

Agent E returns the original pacs.008, using a 
pacs.004 together with the reason for return.
Agent C produces an end of day account 
statement report. An optional real time 
notifications e.g. credit notification
(camt.054) may have also been created 
at the time of the credit posting
Agent C receives the payment and credits 
the account of Agent D
Agent B processes the payment 
on Agent C
pacs.004
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover 
method to the Creditor Agent 
(D)
2a
2b
2b
In parallel the Debtor Agent (A) 
initiates a covering payment to 
credit the account of Agent (D) 
with their correspondent (Agent 
C)
3
4
5
5
8
10
11
+ Return 
Reason 
3 4
A
B C
D
9
pacs.004
9
10
Agent D reconciles the covering 
funds and processes the payment 
onto Agent E 
Agent E credits the account of 
the Creditor, and may optionally 
provide a notification e.g., credit 
notification in addition to an 
account statement (camt.053)
E
7
Creditor determines that they wish to return the payment 
e.g. they are unable to apply, and instructs their bank 
(Agent E) to return the payment together with the reason.
8
Agent D returns the original pacs.009
cov, using a pacs.004 together with the 
reason for return.
Agent C return of covering funds to 
Agent B, together with the reason code 
for return.
11 Agent B return of covering funds to 
Agent A, together with the reason code 
for return.
+ Return 
Reason 
+ Return 
Reason 
+ Return 
Reason 
424

Agent C receives the payment and 
recognises the payment can not be 
completed as requested e.g. the Agent D 
does not maintain an account with them. 
Agent B processes the payment 
on Agent C
pacs.002
pacs.009 cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover method 
to the Creditor Agent (D)
2a
2b
2b
In parallel the Debtor Agent (A) 
initiates a covering payment to 
credit the account of Agent (D) 
with their correspondent (Agent 
C)
3
4
4
Agent C rejects the covering funds to 
Agent B, together with the reason code 
for rejection.
Agent B return of covering funds to 
Agent A, together with the reason code 
for return.
5
5
+ Reject 
Reason 
+ Return 
Reason 
Agent A initiates a Request for 
Cancellation include the Cancellation 
reason code
3
6 camt.056
6
A
B C
D
425
See use case p.8.2.1 for the cover payment sample
c.29.2.2 for case resolution and p.56.2.2 for 
payment return

Financial Institution 
Direct Debit
426

pacs.010
Group Header
Credit Instruction
nested elements:
• Group Header which contains a 
set of characteristics that relates to 
the transaction
• Credit Instruction which contains 
elements providing information 
specific to direct debit transaction 
information and credit instruction. 
427
Typically a Direct Debit message in a many-to-many payment (FINplus 
service) would be considered a point-to-point message, successfully 
resulting in a payment transaction which may be exchange over 
various messages.

camt.053
pacs.002
A B C
The Financial Institution Direct Debit message (pacs.010) is sent by a 
Financial Institution, directly or through another agent, to the Debtor 
Agent. It is used to instruct the Debtor Agent to move funds from the 
Debtor’s account to the Creditor, where both Debtor and Creditor are 
financial institutions.
428
pacs.010
secl.010
camt.053

pacs.009
camt.053
pacs.002
A B C D
The Financial Institution Direct Debit message (pacs.010) is sent by a 
Financial Institution, directly or through another agent, to the Debtor 
Agent. It is used to instruct the Debtor Agent to move funds from the 
Debtor’s account to the Creditor, where both Debtor and Creditor are 
financial institutions.
429
pacs.010
secl.010
camt.053

430

Each ISO 20022 payment message has a Message Identification element, located in the
Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact
equivalent in the legacy MT payment message. However, the Sender’s Reference (Field 20)
could be considered a similar comparison where a pacs message contains a single Transaction.
Group Header Message Identification
431
Min 1 – Max 1

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
432

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 
Group Header Number of Transactions
433
g
Single transactions in the CBPR+ payment usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant payments, supporting the next
generation of innovation.

434

Unique reference assigned by the account servicer to
unambiguously identify the account report. Directly
comparable with the Transaction Reference Number
(Field 20) of the legacy MT Financial Markets Direct Debit
message.
Credit Instruction Credit Identifier
435

pacs.009
pacs.009
Instructing Agent and Instructed Agent 
represent the Agents involved in the pacs 
point-to-point message exchange. These 
roles therefore change on each message 
leg.
A B C D
Instructing Agent and Instructed Agent elements are required in all pacs messages
and is only available in the Credit Instruction.
Credit Instruction
Instructing Agent
Instructed Agent
436
pacs.010
Instructing
Agent: Agent D
Instructed
Agent: Agent B

customer, the Creditor. Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the 
Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where 
the Debtor Agent maintain the account of both the Debtor and Creditor.
Credit Instruction
Creditor Agent
437
Where the Creditor Agent is utilised the Creditor Agent Account may 
optionally be used to capture the account of the Creditor Agent with the Agent 
immediate before them in the transaction chain (the Agent Serving their 
account)
This would only apply where the message includes a Creditor Agent, however 
CBPRplus does not recommend to use this element unless mandated within a 
community or bilaterally agreed.
Min 0 – Max 1
Creditor Agent Account

elements describe the Creditor in greater detail.
Creditor
438
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Creditor
address details
LEI
Legal entity identifier of the 
financial institution.
Credit Instruction Creditor

Min 1 – Max 1
Credit Instruction Creditor Account 439
An element which may either use an external ISO Cash Account
Type code or a proprietary code. It is used to identifier a particular
type of account.
Anested element which contains a Proxy Identifier together with the Proxy
Type represented by either use an external ISO Proxy Account Type code
or a proprietary code.
Account
Currency The Currency for which the account is held. This is identified
using the three characters ISO currency code.
The Name of the Account, as Assigned by the servicing
institution.
Type
Name
Proxy
a unique Identification for the account, between the Account Servicer and
Account Owner. The element is further nested by choice of IBAN or Other to
capture the account.
Identification

captures information related to the Debit part of the transaction, such as the Debtor, the amount and 
settlement date. 
Direct Debit Transaction Information
It is important to recognise that the data elements contained in this part of the
Direct Debit message are identical the pacs.009 Financial Institution Credit
Transfer message which represents the next stage of the journey should the
Direct Debit be accepted.
440
i
Credit Instruction
From a business perspective authorisation of a direct debit instruction can be
predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit
scheme). Either third party debt authority could be granted to the Agent
instructing of the Direct Debit, or the Payment Identification could be used to
capture a static or incremental value (i.e., a mandate) to determine if the
Agent instructing the Direct Debit has been authorised to debit the account.

the end-to-end Transaction Reference created using the UUIDv4
standard. This reference must be passed unchanged throughout
the payment, it may also be created by the Creditor within their
Direct Debit Initiation request, and also included in reporting
messages.
UETR
Min 1 – Max 1
Payment
Identification
$
y 
Direct Debit Transaction Info’ Payment Identification
a point-to-point reference restricted in CBPR+ to 16
character and directly comparable with the Sender’s
Reference (Field 20) of the legacy MT payment message.
Instruction
Identification
Min 1 – Max 1
an end-to-end reference provided by the Creditor
which must be passed unchanged throughout the
payment and reported back to the Creditor.
note: if the Creditor has not provide an end-to-end identifier, the Creditor Agent may
populate “NOTPROVIDED” to comply the
mandatory need of this element.
End to End
Identification
Min 1 – Max 1
441

Payment
Identification
$
pgyppy 
debit transaction.
Direct Debit Transaction Info’ Payment Identification
an end-to-end reference assigned by the first Instructing
Agent to identify the transaction.
Transaction
Identification
Min 0 – Max 1
a point-to-point reference populated by a Payment
Market Infrastructure, typically to the settlement leg of a
clearing system transaction as a reference to the settled
clearing transaction.
Clearing 
System 
Reference
Min 0 – Max 1
442

pyyp
Payment Type Info’
443
Credit Instruction
Direct Debit Transaction Information
Payment
Type 
Information
A nested element which may either use an external
ISO Service Level code or a proprietary code. It is
used to identify a particular agreed service level which
should be applied to the payment.
Service
Level 
Min 0 – Max 3
A nested element which may either use an
external ISO Local Instrument code or a
proprietary code. It is used to identify the
type of payment local instrument such as a
Standing Order.
Note: the ISO instrument codes are
registered by specific community
group (captured in the code list)
Local 
Instrument 
Min 0 – Max 1
A nested element which may either use an external ISO
Category Purpose code or a proprietary code. It is used to
identify the category of payment. For example, SECU
Transactionis the payment of securities.
Category 
Purpose 
Min 0 – Max 1
a choice of imbedded
codes representing the
urgency considered by
the Instructing Agent,
this point-to-point
Instruction 
Priority 
Min 0 – Max 1
information may be used by the 
Instructed Agent to differentiate 
the processing priority.

A mandated currency amount moved between the Instructing Agent and the Instructed Agent.
This therefore is the point-to-point currencyamount exchanged, comparable with the MT Field 32
Note: the Financial Institution Direct Debit (pacs.010) has no Instructed Amount
element, Exchange Rate or Charger Bearer(like the pacs.009) as the Instructed 
Settlement Amount is expected to be transferred across the end-to-end payment chain 
without any charges being applied or currency conversions.
Interbank
Settlement
Amount
Interbank Settlement Amount 
Min 1 – Max 1
444
Credit Instruction
Direct Debit Transaction Information

Interbank Settlement Date
p
This Date element use ISODate YYYY-MM-DD
10 For example: 2002-10-10 (10 October 2002) 
445
Credit Instruction
Direct Debit Transaction Information

Settlement Time Request
446
Credit Instruction
Direct Debit Transaction Information
Where Settlement Time Request is used the nested:
• CLS Time
• Till Time
• From Time
• Reject Time
may be used to capture information related to this time.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

elements describe the Debtor in greater detail. 
Debtor
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
Credit Payment Direct Debit Transaction Information Debtor447
Legal entity identifier of the LEI
financial institution.

Min 1 – Max 1
Credit Instruction Debtor Account 448
An element which may either use an external ISO Cash Account
Type code or a proprietary code. It is used to identifier a particular
type of account.
Anested element which contains a Proxy Identifier together with the Proxy
Type represented by either use an external ISO Proxy Account Type code
or a proprietary code.
Account
Currency The Currency for which the account is held. This is identified
using the three characters ISO currency code.
The Name of the Account, as Assigned by the servicing
institution.
Type
Name
Proxy
a unique Identification for the account, between the Account Servicer and
Account Owner. The element is further nested by choice of IBAN or Other to
capture the account.
Identification

customer, the Debtor. Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the 
Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where 
the Debtor Agent maintain the account of both the Debtor and Creditor.
Credit Instruction
449
Debtor Agent
Debtor Agent Account
Where the Debtor Agent is utilised the Debtor Agent Account may optionally 
be used to capture the account of the Debtor Agent with the Agent immediate 
after them in the transaction chain (the Agent Serving their account)
This would only apply where the message includes a Debtor Agent, however 
CBPRplus does not recommend to use this element unless mandated within a 
community or bilaterally agreed.
Min 0 – Max 1

Instruction for Debtor Agent
The Instruction for Debtor Agent element offers a occurrence of free format information. 
The use of this element should be bilaterally agreed with the Debtor Agent to maximize the 
ability to Straight Through Process the instruction.
Min 0 – Max 1
450
Credit Instruction

ISO Purpose code or a proprietary code.
The purpose is used by the capture the nature of the payment e.g. CORT Trade Settlement Payment, CFEE
Cancellation Fees etc. and should not be confused with Regulatory Reporting codes.
Purpose
The externalised Purpose code set is classified by the purpose, for example commercial, for 
which the numerous codes within the classification are each described by Name and 
Definition.
For example:
OTCD is classified within the Collateral categorisation, with the Name OTC Derivatives 
described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for 
example contracts which are traded and privately negotiated.
451
Credit Instruction

Credit Instruction Remittance Information
Unstructured
Remittance Information enable the matching/reconciliation of an entry that the payment 
is intended to settle
Min 0 – Max 1
The Unstructured sub element captures free format Remittance Information which 
is restricted in CBPR+ to 140 characters to ensure backward compatibility with the 
legacy MT message during coexistence. 
Min 0 – Max 1
Note: like the pacs.009 Remittance Information can only be captured in an 
Unstructured element. 
Remittance Information is however a dedicated element used both within the pacs 
and camt reporting messages, whereby this information can travel end-to-end using 
ISO 20022.
452

Financial Institution Direct Debit
Use Case p.10.1.1 - High Level Payment of a Financial Institution Direct Debit (pacs.010)
Use Case p.10.1.1.a - High Level Book movement of a Financial Institution Direct Debit (pacs.010)
Use Case p.10.1.2 - High Level Rejection of a Financial Institution Direct Debit (pacs.010)
453

Agent C processes the payment 
on Agent D
pacs.009
Agent E initiates a Direct Debit 
instruction to debit Agent A’s 
account
2
Debtor Agent (B) initiates a 
serial payment towards the 
Creditor Agent (E) using 
Agents B & C as intermediaries
3
pacs.009 camt.053
2
3
A
C D
E
454
1
B
Agent D credits the account of the 
Creditor (Agent E), and may 
optionally provide a notification 
e.g. credit notification in addition to 
an account statement (camt.053)
4
4
pacs.002
2a
camt.053
Debtor Agent (B) debits the 
Debtor (Agent A) optionally 
provide a notification e.g. credit 
notification in addition to an 
account statement (camt.053)
2a

Agent E initiates a Direct Debit
instruction to debit Agent A’s 
account
Debtor Agent (B) debits the 
Debtor (Agent A) optionally 
provide a notification e.g. credit 
notification in addition to an 
account statement (camt.053)
camt.053 A C
455
1
B
Agent B credits the account of the 
Creditor (Agent C), and may 
optionally provide a notification 
e.g. credit notification in addition to 
an account statement (camt.053)
2a
pacs.002
camt.053
2b
2a 2b

pacs.010
Agent D initiates a Direct Debit
instruction to debit Agent A’s 
account
Debtor Agent (B) rejects the 
instruction, using a pacs.002, 
as no mandate agreement is in
place.
A
C
D
E
456
1
B
pacs.002

Financial Institution Direct 
Debit – Margin Collection
457

pacs.010
Group Header
Credit Instruction
nested elements:
• Group Header which contains a 
set of characteristics that relates to 
the transaction
• Credit Instruction which contains 
elements providing information 
specific to direct debit transaction 
information and credit instruction. 
458
The Financial Institution Direct Debit Margin Collection is designed to 
allow a Central Counterpart to collect money by triggering a payment. 
Whereby the pacs.010 Debit transfer the money to the Creditor using a 
pacs.009. Unlikely the pacs.010 Financial Institution Direct Debit 
additional Credit Instruction elements are allowed in this Usage 
Guideline. 
The Financial Institution Direct Debit Margin Collection can be used for 
collection using the same message model.

pacs.009
camt.053
pacs.002
A B C D
The Financial Institution Direct Debit message (pacs.010) is sent by a 
Financial Institution, directly or through another agent, to the Debtor 
Agent. It is used to instruct the Debtor Agent to move funds from the 
Debtor’s account to the Creditor, where both Debtor and Creditor are 
financial institutions.
459
pacs.010
secl.010

460

Each ISO 20022 payment message has a Message Identification element, located in the
Group Header. This 35 character identifier is a point-to-point reference used to unambiguously
identify the message.
For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact
equivalent in the legacy MT payment message. However, the Sender’s Reference (Field 20)
could be considered a similar comparison where a pacs message contains a single Transaction.
Group Header Message Identification
461
Min 1 – Max 1

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
462

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 
Group Header Number of Transactions
463
g
Single transactions in the CBPR+ payment usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant payments, supporting the next
generation of innovation.

464

Unique reference assigned by the account servicer to
unambiguously identify the account report. Directly
comparable with the Transaction Reference Number
(Field 20) of the legacy MT Financial Markets Direct Debit
message.
Credit Instruction Credit Identifier
465

Payment
Type 
Information
pppg
Credit Instruction Payment Type Info’
A nested element which may either use an external ISO
Category Purpose code or a proprietary code. It is used to
identify the category of payment. For example, SECU
Transactionis the payment of securities.
Category 
Purpose 
Min 0 – Max 1
466
a choice of imbedded codes
representing the urgency considered
by the Instructing Agent, this point-to-point information may be used by the
Instructed Agent to differentiate the
processing priority.
Instruction 
Priority 
Min 0 – Max 1

pacs.009
pacs.009
Instructing Agent and Instructed Agent 
represent the Agents involved in the pacs 
point-to-point message exchange. These 
roles therefore change on each message 
leg.
A B C D
Instructing Agent and Instructed Agent elements are required in all pacs messages
and is only available in the Credit Instruction.
Credit Instruction
Instructing Agent
Instructed Agent
467
pacs.010
Instructing
Agent: Agent D
Instructed
Agent: Agent B

Credit Instruction
468
The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the
CreditorAgent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.
The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent
for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the
Field 56a in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the
Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.
The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the
Creditor Agent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 3 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 2. This optional element has not comparable field in the legacy FIN message.
1
2
3
Debtor Agent and Creditor Agent elements must be present before the Intermediary 
Agent 1 element can be used

customer, the Creditor. Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the 
Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where 
the Debtor Agent maintain the account of both the Debtor and Creditor. 
Credit Instruction
Creditor Agent
469
Where the Creditor Agent is utilised the Creditor Agent Account may 
optionally be used to capture the account of the Creditor Agent with the Agent 
immediate before them in the transaction chain (the Agent Serving their 
account) 
This would only apply where the message includes a Creditor Agent, however 
CBPRplus does not recommend to use this element unless mandated within a 
community or bilaterally agreed. 
Min 0 – Max 1
Creditor Agent Account

elements describe the Creditor in greater detail.
Creditor
470
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Creditor
address details
LEI
Legal entity identifier of the 
financial institution.
Credit Instruction Creditor

Min 1 – Max 1
Credit Instruction Creditor Account 471
An element which may either use an external ISO Cash Account
Type code or a proprietary code. It is used to identifier a particular
type of account.
Anested element which contains a Proxy Identifier together with the Proxy
Type represented by either use an external ISO Proxy Account Type code
or a proprietary code.
Account
Currency The Currency for which the account is held. This is identified
using the three characters ISO currency code.
The Name of the Account, as Assigned by the servicing
institution.
Type
Name
Proxy
a unique Identification for the account, between the Account Servicer and
Account Owner. The element is further nested by choice of IBAN or Other to
capture the account.
Identification

captures information related to the Debit part of the transaction, such as the Debtor, the amount and 
settlement date. 
Direct Debit Transaction Information
It is important to recognise that the data elements contained in this part of the
Direct Debit message are identical the pacs.009 Financial Institution Credit
Transfer message which represents the next stage of the journey should the
Direct Debit be accepted.
472
i
Credit Instruction
From a business perspective authorisation of a direct debit instruction can be
predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit
scheme). Either third party debt authority could be granted to the Agent
instructing of the Direct Debit, or the Payment Identification could be used to
capture a static or incremental value (i.e., a mandate) to determine if the
Agent instructing the Direct Debit has been authorised to debit the account.

the end-to-end Transaction Reference created using the UUIDv4
standard. This reference must be passed unchanged throughout
the payment, it may also be created by the Creditor within their
Direct Debit Initiation request, and also included in reporting
messages.
UETR
Min 1 – Max 1
Payment
Identification
$
y 
Direct Debit Transaction Info’ Payment Identification
a point-to-point reference restricted in CBPR+ to 16
character and directly comparable with the Sender’s
Reference (Field 20) of the legacy MT payment message.
Instruction
Identification
Min 1 – Max 1
an end-to-end reference provided by the Creditor
which must be passed unchanged throughout the
payment and reported back to the Creditor.
note: if the Creditor has not provide an end-to-end identifier, the Creditor Agent may
populate “NOTPROVIDED” to comply the
mandatory need of this element.
End to End
Identification
Min 1 – Max 1
473

Payment
Identification
$
pgyppy 
debit transaction.
Direct Debit Transaction Info’ Payment Identification
an end-to-end reference assigned by the first Instructing
Agent to identify the transaction.
Transaction
Identification
Min 0 – Max 1
a point-to-point reference populated by a Payment
Market Infrastructure, typically to the settlement leg of a
clearing system transaction as a reference to the settled
clearing transaction.
Clearing 
System 
Reference
Min 0 – Max 1
474

pyypppy y 
Instruction has it own Payment Type Information.
Payment Type Info’
475
Credit Instruction
Direct Debit Transaction Information
Payment
Type 
Information
A nested element which may either use an external
ISO Service Level code or a proprietary code. It is
used to identify a particular agreed service level which
should be applied to the payment.
Service
Level 
Min 0 – Max 3
A nested element which may either use an
external ISO Local Instrument code or a
proprietary code. It is used to identify the
type of payment local instrument such as a
Standing Order.
Note: the ISO instrument codes are
registered by specific community
group (captured in the code list)
Local 
Instrument 
Min 0 – Max 1
A nested element which may either use an external ISO
Category Purpose code or a proprietary code. It is used to
identify the category of payment. For example, SECU
Transactionis the payment of securities.
Category 
Purpose 
Min 0 – Max 1
a choice of imbedded
codes representing the
urgency considered by
the Instructing Agent,
this point-to-point
Instruction 
Priority 
Min 0 – Max 1
information may be used by the 
Instructed Agent to differentiate 
the processing priority.

A mandated currency amount moved between the Instructing Agent and the Instructed Agent.
This therefore is the point-to-point currencyamount exchanged, comparable with the MT Field 32
Note: the Financial Institution Direct Debit (pacs.010) has no Instructed Amount
element, Exchange Rate or Charger Bearer(like the pacs.009) as the Instructed 
Settlement Amount is expected to be transferred across the end-to-end payment chain 
without any charges being applied or currency conversions.
Interbank
Settlement
Amount
Interbank Settlement Amount 
Min 1 – Max 1
476
Credit Instruction
Direct Debit Transaction Information

Interbank Settlement Date
p
This Date element use ISODate YYYY-MM-DD
10 For example: 2002-10-10 (10 October 2002) 
477
Credit Instruction
Direct Debit Transaction Information

Settlement Time Request
478
Credit Instruction
Direct Debit Transaction Information
Where Settlement Time Request is used the nested:
• CLS Time
• Till Time
• From Time
• Reject Time
may be used to capture information related to this time.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

elements describe the Debtor in greater detail. 
Debtor
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
Credit Payment Direct Debit Transaction Information Debtor479
Legal entity identifier of the LEI
financial institution.

Min 1 – Max 1
Credit Instruction Debtor Account 480
An element which may either use an external ISO Cash Account
Type code or a proprietary code. It is used to identifier a particular
type of account.
Anested element which contains a Proxy Identifier together with the Proxy
Type represented by either use an external ISO Proxy Account Type code
or a proprietary code.
Account
Currency The Currency for which the account is held. This is identified
using the three characters ISO currency code.
The Name of the Account, as Assigned by the servicing
institution.
Type
Name
Proxy
a unique Identification for the account, between the Account Servicer and
Account Owner. The element is further nested by choice of IBAN or Other to
capture the account.
Identification

customer, the Debtor. Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the 
Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where 
the Debtor Agent maintain the account of both the Debtor and Creditor. 
Credit Instruction
481
Debtor Agent
Debtor Agent Account
Where the Debtor Agent is utilised the Debtor Agent Account may optionally 
be used to capture the account of the Debtor Agent with the Agent immediate 
after them in the transaction chain (the Agent Serving their account) 
This would only apply where the message includes a Debtor Agent, however 
CBPRplus does not recommend to use this element unless mandated within a 
community or bilaterally agreed. 
Min 0 – Max 1

Instruction for Debtor Agent
The Instruction for Debtor Agent element offers a occurrence of free format information. 
The use of this element should be bilaterally agreed with the Debtor Agent to maximize the 
ability to Straight Through Process the instruction.
Min 0 – Max 1
482
Credit Instruction

ISO Purpose code or a proprietary code.
The purpose is used by the capture the nature of the payment e.g. CCPC CCP Cleared Initial Margin and
should not be confused with Regulatory Reporting codes.
Purpose
The externalised Purpose code set is classified by the purpose, for example commercial, for 
which the numerous codes within the classification are each described by Name and 
Definition.
For example:
OTCD is classified within the Collateral categorisation, with the Name OTC Derivatives 
described as a Cash collateral related to over-the-counter (OTC) Derivatives - in general for 
example contracts which are traded and privately negotiated.
483
Credit Instruction

Credit Instruction Remittance Information
Unstructured
Remittance Information enable the matching/reconciliation of an entry that the payment 
is intended to settle
Min 0 – Max 1
The Unstructured sub element captures free format Remittance Information which 
is restricted in CBPR+ to 140 characters to ensure backward compatibility with the 
legacy MT message during coexistence. 
Min 0 – Max 1
Note: like the pacs.009 Remittance Information can only be captured in an 
Unstructured element. 
Remittance Information is however a dedicated element used both within the pacs 
and camt reporting messages, whereby this information can travel end-to-end using 
ISO 20022.
484

Financial Institution Direct Debit
Use Case p.10.2.1 - High Level Payment Of A Financial Institution Direct Debit (pacs.010)
Use Case p.10.2.2 - High Level Rejection Of A Financial Institution Direct Debit (pacs.010)
485

Agent C processes the payment 
on Agent D
pacs.009
Agent E initiates a Direct Debit 
instruction to debit Agent A’s 
account
2
Debtor Agent (B) initiates a 
serial payment towards the 
Creditor Agent (E) using 
Agents B & C as intermediaries
3
pacs.009 camt.053
2
3
A
C D
E
486
1
B
Agent D credits the account of the 
Creditor (Agent E), and may 
optionally provide a notification 
e.g. credit notification in addition to 
an account statement (camt.053)
4
4
pacs.002

pacs.010
Agent D initiates a Direct Debit 
instruction to debit Agent A’s 
account
Debtor Agent (B) rejects the 
instruction, using a pacs.002, 
as no mandate agreement is in 
place.
A
C
D
E
487
1
B
pacs.002

Financial Institution to 
Financial Institution 
Customer Direct Debit
488

pacs.003
Group Header
Direct Debit Transaction 
Information Payment messages in a many-to-many payment are considered as a 
single transaction. 
nested elements:
• Group Header which contains a 
set of characteristics that relates to 
all individual transaction
• Direct Debit Transaction 
Information which contains 
elements providing information 
specific to the individual direct debit 
transaction. 
489

pacs.002
A
B
Debtor
*Noting in CGI-MP pain.008 may also be sent by the Initiating Party/Creditor directly to the Creditor Agent which is outside of the scope of CBPR+.
Creditor Agent Creditor
*Initiating Party may alternative represent an authorised party such as a head office 
**or other proprietary method for instructing a direct debit initiation request. 
pain.002
camt.053
pacs.003
Debtor Agent
pain.008**
Initiating Party*
The Financial Institution To Financial Institution Customer Direct Debit message is sent by the Creditor Agent to 
the Debtor Agent, directly or through other agents and/or a payment clearing and settlement system. 
It is used to collect funds from a Debtor account for a Creditor, whereby one or both of these Parties are non-Financial Institutions.

491

pygg, 
Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
For Payment Clearing and Settlement (pacs) messages the Message Identification has no
exact equivalent in the legacy MT payment message. However, the Sender’s Reference (Field
20) could be considered a similar comparison where a pacs message contains a single
Transaction.
Group Header Message Identification
492
Each transaction’s Direct Debit Transaction Information contains a variety of nested Payment
Identification elements to capture reference related to the individual transaction such as a
UETR (Unique End-to-end Transaction Reference)

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
493

The number of transactions in CBPR+ payment usage guidelines is fixed to 1. 
Group Header Number of Transactions
494
g
Single transactions in the CBPR+ payment usage guidelines enable a transaction to be
managed and unlocks highly automated, frictionless, instant payments, supporting the next
generation of innovation.

D
27
495
The Settlement Method element in the pacs.003 allows a choice of an embedded code.
INDA indicate this Customer Direct Debit will be settled by the Instructed Agent (as the Account Servicing 
Institution) The account held at the Instructed Agent may captured in the dedicated Settlement Account 
element.
INGA indicate this Customer Direct Debit has already been settled by the Instructing Agent, who has 
credited the Account they service for the Instructed Agent (as an Account Owner). The account held by 
the Instructed Agent with the Instructing Agent may captured in the dedicated Settlement Account 
element.
$
€
Settlement Method code CLRG is not part of CBPR+ specifications but instead used in 
Market Infrastructure specification
Group Header Settlement Information
In the context of customer direct debit, INDA is a logical choice for the settlement
with the customer because the INDA is the agent that owns the account of the
Debtor, and the debit must be made first.

Group Header Settlement Information
496
The Settlement Account identifies the account details maintained at the account
servicing institution (Agent responsible for the settlement of the instruction as
indicated in the Settlement Method)
Min 0 – Max 1
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
Name identifies the name of the account as assigned by the Account Servicing
Institution
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

497

the end-to-end Transaction Reference created using the UUIDv4
standard. This reference must be passed unchanged throughout
the payment, it may also be created by the Creditor within their
Direct Debit Initiation request, and also included in reporting
messages.
UETR
Min 0 – Max 1
Payment
Identification
$
y 
Direct Debit Transaction Info’ Payment Identification
a point-to-point reference restricted in CBPR+ to 16
character and directly comparable with the Sender’s
Reference (Field 20) of the legacy MT payment message.
Instruction
Identification
Min 1 – Max 1
an end-to-end reference provided by the Creditor
which must be passed unchanged throughout the
payment and reported back to the Creditor.
note: if the Creditor has not provide an end-to-end identifier, the Creditor Agent may
populate “NOTPROVIDED” to comply the
mandatory need of this element.
End to End
Identification
Min 1 – Max 1
498

Payment
Identification
$
pgyppy 
debit transaction.
Direct Debit Transaction Info’ Payment Identification
an end-to-end reference assigned by the first Instructing
Agent to identify the transaction.
Transaction
Identification
Min 0 – Max 1
a point-to-point reference populated by a Payment
Market Infrastructure, typically to the settlement leg of a
clearing system transaction as a reference to the settled
clearing transaction.
Clearing 
System 
Reference
Min 0 – Max 1
499

A nested element which may either use an external ISO Category
Purpose code or a proprietary code. It is used to identify the
category of payment. For example, RPRE means to re-present
previously reversed or returned direct debit transaction.
Category 
Purpose 
Min 0 – Max 1
Payment
Type 
Information
i
Direct Debit Transaction Info’ Payment Type Info’
A nested element which may either use an external ISO
Service Level code* or a proprietary code. It is used to
identify a particular agreed service level which should be
applied to the payment.
Service
Level 
Min 0 – Max 3
A nested element which may either use an
external ISO Local Instrument code or a
proprietary code. It is used to identify the
type of payment local instrument such as a
Standing Order.
Note: the ISO instrument codes are
registered by specific community
group (captured in the code list)
Local 
Instrument 
Min 0 – Max 1
Clearing
Channel
Min 0 – Max 1
a choice of imbedded
codes representing
the clearing channel
to be used to process
direct debits.
500
a choice of imbedded
codes representing the
urgency considered by
the Instructing Agent,
this point-to-point
Instruction 
Priority 
Min 0 – Max 1
information may be used by the 
Instructed Agent to differentiate 
the processing priority.
*note - where a service level is not bilaterally agreed, it may be ignored.

Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important 
one. Instructed Amount relates to the amount Instructed to be debited from the Debtor’s account and 
only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not the 
same currency amount. 
£
$
¥
Direct Debit Transaction Information
Instructed Amount 
Interbank Settlement Amount 
Min 1 – Max 1 Min 1 – Max 1
501
A mandated currency amount moved between the Instructing Agent and the Instructed Agent. This
therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32B
Interbank
Settlement
Amount
Interbank
Settlement
Date
A mandated date on which the Interbank Settlement should be executed between the
Instructing Agent and the Instructed Agent. This therefore is the value date comparable with
the MT Field 30

instructions. 
502
Min 0 – Max 1
The Settlement Priority provides an optional choice of embedded codes to indicate the instruction’s 
settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by 
the Instructed Agent to identify the priority associated with the Settlement Method and should not be confused 
with the Instruction Priority. 
Note: where Settlement Priority of the pacs.003 is ‘URGT’ (Urgent) means the highest priority
possible to process the direct debit settlement and the amount of money becomes available to the
Creditor Agent.
Min 0 – Max 1
The Settlement Time Indication optionally captures the time settlement occurred at a transaction administrator 
such as a Market Infrastructure. 
This DateTime can be captured in two nested elements, Debit Date Time and Credit Date Time. 
Direct Debit Transaction Information
Settlement Time Indication
Settlement Priority

503
Note: a number of Cross Element Rules exist which relate to the Instructed 
Amount element. For example, if the Instructed Amount is present and the 
currency is different from the currency in Interbank Settlement Amount, 
then Exchange Rate must be present.
The Instructed Amount captures currency and amount instructed by the Creditor. This conditional
element is required when the Interbank Settlement Amount is not the same currency and/or
amount as originally instructed by the Creditor. For example, a charge is taken, or the transactions is
converted to another currency. This element is comparable with the legacy Field 33B.
The Exchange Rate captures the factor (rate) used to convert an amount from one currency into 
another. This reflects the currency pair price at which one currency was bought with another 
currency.
Min 0 – Max 1
Min 0 – Max 1
$100
£
¥
Direct Debit Transaction Information
Exchange Rate 
Instructed Amount

y gpg pyp
with MT Field 71A ‘Details of Charges’
71A: Details 
of Charges 
Code Description
BEN Beneficiary
OUR Our Customer Charges
SHA Shared Charges
Charge 
Bearer
(1.1)
Code Description
CRED Creditor
DEBT Debtor
SHAR Shared
SLEV Service Level
Note: SLEV is removed from CBPR+ usage guideline specifications.
Direct Debit Transaction Info’ Charge Bearer
504

Charge 
Information
(0.*)
Amount
Currency
Agent BICFI
Name
StructuredPostal Address
pgg
In addition to the legacy MT message the pacs.003 Charge
Information mandate the Agent, this represent the Agent for
who the Charges are either; due (pre-paid charges) or has
taken a charge (deduct from the transaction)
CBPR+ best practice recommends the use of the
structured Agent BIC.
Note: As the Charge Information element has the capability to capture both charges deducted and charges 
included i.e. pre-paid charges, the use of the Interbank Settlement Amount and Instructed Amount elements 
play an important role. 
As the Charges Information element is repetitive it can capture charges related to previous legs of the 
payment transaction.
Direct Debit Transaction Info’ Charge Information
505

It is defined by ISO Date expressed in the YYYY-MM-DD format. 10
creditor requests that the amount of money is to be collected from the debtor.
Requested Collection Date
Direct Debit Transaction Information

Credit party that signs the mandate, may be used if
supported by the Direct Debit Schema. (see next page for
additional detail on this nested element)
Unique and unambiguous identification of the pre-notification which is
sent separately from the direct debit instruction.
Direct 
Debit 
Transaction
Pre 
Notification 
Date
Provides further details of the direct debit mandate signed between 
the creditor and the debtor. E.g., Mandate Identification, Date of 
Signature and Electronic Signature.
Date on which the creditor notifies the debtor about the amount and date on
which the direct debit instruction will be presented to the debtor's agent.
Direct Debit Transaction
Direct Debit Transaction Information
Pre 
Notification 
Identification
Creditor 
Scheme 
Identification
Mandate 
Related 
Information
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

related to the credit party that signs the mandate who is different from the Creditor.
The Creditor Scheme Identification element offers the following options:
Name
Postal Address: Not used often
Identification
Country of Residence
Contact Details 
508
CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit 
Scheme.
Direct Debit Transaction
Direct Debit Transaction Information
Creditor Scheme Identification
CGI

the Creditor in greater detail.
Creditor
Country of 
Residence
Optional element to 
capture the Creditor’s ISO 
country code of residence 
Identification
Nested element capturing the 
various types of identifiers for 
the party e.g. BIC, LEI etc.
Postal 
Address
Nested element capturing either 
structured or unstructured Creditor
address details
Direct Debit Transaction Info Creditor
509
Min 1 – Max 1

510
intended to be applied to the Creditors account, which are also reflected in their account Statement.
The Creditor Account uses a variety of nested elements to capture information related to 
the account.
Direct Debit Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Creditor Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency if the account
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

agent maintain a relationship with their customers; the Debtor and Creditor. 
Note: Although the Debtor Agent, Creditor Agent, Debtor and Creditor all maintain static roles in the
pacs messages, the description of these parties change in the reporting messages (camt) where the
Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor
become the Statement Account Owner. This will be explored further in the camt Cash Management
Reporting section.
Direct Debit Transaction Information
Debtor Agent
Creditor Agent
511

512
information related to these Agents. The nature of this element implies there is an Agent or Agent in 
between the Debtor Agent and Creditor Agent in the direct debit transaction.
The Debtor Agent Account and Creditor Agent Account use a variety of nested 
elements to capture information related to the account.
Direct Debit Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Account Servicing
Institution
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account
Name identifies the name of the account as assigned by the Account Servicing
Institution
Proxy captures an alternative identification of the account number such as an
email address. This element has further nested Type which is a choice of external
code list or proprietary code and Identification which are both mandatory where
the Proxy element is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Debtor Agent and Creditor Agent are a Financial Institution, therefore
the nested elements Name and Proxy are unlikely to be used.

➢ CBPR+ premise is that an Ultimate Debtor has no financial 
regulated direct account relationship with the corresponding Debtor.
➢ CBPR+ premise is that an Ultimate Creditor has no financial 
regulated direct account relationship with the corresponding 
Creditor.
Ultimate Creditor element should not be confused with an Initiating Party who may send a direct debit
initiation request on behalf of the Creditor. (see dedication section on Initiating Party)
Note: Ultimate Debtor and Ultimate Creditor are removed 
from the pacs.010 Financial Institution Direct Debit.
Ultimate
Party
Ultimate
Creditor
Ultimate
Debtor
Direct Debit Transaction Information
Ultimate Creditor
Ultimate Debtor
Min 0 – Max 1
Min 0 – Max 1
513
An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not 
bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a 
payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor 
depending on the payment scenario)

g y 
therefore this optional element is not necessary. More often the Initiating
Party is a third party providing direct debit collection services on behalf of the
Creditor (often referred to as a Third Party Provider) whereby the Creditor
maintains an account with the Creditor Agent but the Third Party Provider
has authority to initiate collection on behalf of the Creditor. This is distinctly
different from an Ultimate Party (such as Ultimate Creditor) who instructs the
Creditor to initiate a collection on their behalf.
In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the Initiating Party is often the
Creditor, however the same context of a Third Party Provider can exist where the third party is responsible
for collecting funds on behalf of the Creditor.
A
Debtor Agent
g y
Debtor Third Party
Direct Debit Transaction Info’ Initiating Party
514

pacs.003
Instructed
Agent: Agent B
Instructing
Agent: Agent A
Instructing Agent and Instructed Agent 
represent the Agents involved in the pacs 
point-to-point message exchange. These 
roles therefore change on each payment 
leg.
B A
Instructing Agent and Instructed Agent elements are required in all pacs messages 
and are available in the Direct Debit Transaction Information Direct Debit Transaction Information
Instructing Agent
Instructed Agent
515

Direct Debit Transaction Information
516
The Intermediary Agent 2 captures the second Intermediary Agent between the Intermediary Agent 1 and the
CreditorAgent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 2 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.
The Intermediary Agent 1 captures the first Intermediary Agent between the Debtor Agent and Creditor Agent
for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the
Field 56a in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 1 Account captured the account related to this Intermediary Agent, with the
Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.
The Intermediary Agent 3 captures the third Intermediary Agent between the Intermediary Agent 2 and the
Creditor Agent. This optional element has not comparable field in the legacy FIN message.
Min 0 – Max 1
Min 0 – Max 1
The Intermediary Agent 3 Account captured the account related to this Intermediary Agent, with the
Intermediary Agent 2. This optional element has not comparable field in the legacy FIN message.
1
2
3

Debtor in greater detail. 
Debtor
Identification
Nested element capturing the 
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
address details
Direct Debit Transaction Info’ Debtor 517
Min 1 – Max 1

518
is/has been applied to the Debtors account, which are also reflected in their account Statement.
The Debtor Account uses a variety of nested elements to capture information related to 
the account.
Direct Debit Transaction Information
Min 1 – Max 1 Identification identifies the account maintained at the Debtor Agent (Account Servicing
Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account
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

2
Agent A, the Creditor Agent, 
initiates a direct debit 
instruction by sending a 
pacs.003 message to the 
Debtor Agent (B).
3
Debtor, receives a statement 
from their bank confirming the 
monthly Debt Debit, for their 
child (Ultimate Debtors) sports 
club membership fee, has 
debited either account, 
(ebo) ooe oebes (Uae ebo)
pacs.003
4
4
Debtor Agent (B) debits the 
account of the Debtor, credits 
the account of the Creditor 
Agent and confirms the direct 
debit status using a pain.002.
2
B A
519
*Mandate: the Creditor has a mandate, the right to collect funds from the Debtor’s account which is pre-defined for debits. 
pacs.002
DR / CR
3
pain.008
pain.002
Sports club, the Creditor who 
has a mandate* with the 
Debtor, initiates a direct debit 
instruction by sending a 
pain.008 message to their 
bank, Creditor Agent (A).
1
1
camt.053

The purpose is used to capture the nature of the payment e.g. IVPT Invoice Payment, FEES Payment of Fees
etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically
defined by the Creditor.
Direct Debit Transaction Information
Purpose
The externalised Purpose code set is classified by the purpose, for example commercial, for 
which the numerous codes within the classification are each described by Name and 
Definition.
For example, LOAR is classified within the Finance categorisation, with the Name Loan 
Repayment described as a repayment of loan to lender. 
520
Category Purpose also captures a high level purpose, which unlike Purpose is less granular but can trigger
special processing e.g. Category Purpose code SALA ‘Salary Payment’ may trigger a reporting process
which restricts sensitive data i.e., individual salary names.

Direct Debit Transaction Information Regulatory Reporting
Debit Credit Reporting Indicator
Authority
Details
The Debit Credit Reporting Indicator utilises an embedded choice of code 
to indicate whether the regulatory reporting information applies to the:
• DEBT (debit)
• CRED (credit) or 
• BOTH
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max *
The Authority element captures the Name and Country code of the 
Authority/Entity requiring the regulatory reporting information.
The Details element provides the detail on the regulatory reporting 
information.
521

the Creditor in the direct debit initiation request.
Direct Debit Transaction Info’ Related Remittance Information
Remittance Identification
Remittance Location Details
Remittance advices are typically considered as a traditional value added service provided by the Creditor Agent to the Creditor, in order to
facilitate reconciliation for the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting messages.
Remittance Information is a dedicated element used both within the pacs and camt reporting messages, whereby this information can
travel end-to-end using ISO 20022. Related Remittance Information and Remittance Information are mutually exclusive (can’t both be
present)
Business examples are emerging where information is externalised using a URL repository solution.
The Remittance Identification captures a unique reference assigned by the initiating party of the collection to
identify the remittance information sent separately from the direct debit instruction.
The Remittance Location Details uses a set of nested elements to provide information on either the location
of or the delivery of remittance information.
• Method requires a code from an embedded list to detail the method used to deliver the remittance
advise information e.g. EMAL (email)
• Electronic Address provides an electronic address for which an agent is to send the remittance
information to e.g. the email address. It may also reference a URL where remittance information may
be deposited or retrieved.
• Postal Address provides the postal address to which an agent is to send the remittance information
Min 0 – Max 1
Min 0 – Max 2
522

Direct Debit Transaction Info’ Remittance Information
Structured
Unstructured
Remittance Information enable the matching/reconciliation of an entry that the direct 
debit is intended to settle
Min 0 – Max 1
The Unstructured sub element captures free format Remittance Information which 
is restricted in CBPR+ to 140 characters to ensure backward compatibility with the 
legacy MT message during coexistence. 
Min 0 – Max 1
The Structured element is nested capturing rich structured Remittance Information, 
and is unlimited in its multiplicity, but must not exceed 9,000 characters of business 
information (does not include the xml element identification) 
The use of this nested element should be bilaterally/multilaterally agreed, to ensure 
end-to-end transportation of this data.
Min 0 – Max *
523
Related Remittance Informationand Remittance Information are 
mutually exclusive (can’t both be present)

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
Information and it nested elements has
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
Direct Debit Transaction Information
524

g
Serial Financial Institution to Financial Institution Customer Direct Debit 
Use Case p.3.1.1 – High Level FI to FI Customer Direct Debit (pacs.003) successful settlement 
Use Case p.3.1.2 – High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement 
525

camt.053
1
1
Creditor initiates a direct debit 
instruction to the Creditor Agent
Creditor Agent (A) initiates a 
direct debit collection by 
sending a pacs.003 message to 
the Debtor Agent with the 
settlement method “INDA”
The Debtor Agent debits the account 
of the Debtor, and may optionally 
provide a notification e.g. debit 
notification in addition to an account 
statement (camt.053). The Debtor 
Agent also provides a status update 
ACSC (accepted settlement 
completed) to the Creditor Agent. 
pacs.003 pain.008
pain.002
2
Settlement 
Complete
Creditor Agent (A) relays the status 
ACSC (accepted settlement 
completed) to the Initiating Party, 
based upon a bilateral agreement
A
526
pacs.002
4
4
B
3 2
3

1
1
Creditor initiates a direct debit 
instruction to the Creditor Agent
Creditor Agent (A) initiates a 
direct debit collection by 
sending a pacs.003 message to 
the Debtor Agent with the 
settlement method “INDA”
3
The Debtor Agent fails to debit the 
account of the Debtor (e.g., account 
is closed). The Debtor Agent 
provides a status update RJCT 
(Rejected) with the rejection reason 
information. 
pacs.003 pain.008
pain.002
2
3 2
Creditor Agent (A) relays the status 
RJCT (Rejected) to the Initiating 
Party with the rejection reason 
information
A
527
pacs.002
4
4
B
Reject 
Reason

g
528

camt.052 -Bank to Customer Account Report 
camt.053 -Bank to Customer Statement
camt.054 -Bank to Customer Debit Credit Notification
camt.057 – Notification To Receive
camt.058 – Notification To Receive Cancellation Advice 
camt.060 –Account Report Request
529

Bank to Customer 
Account Report
530

camt.052
Group Header
Report
message is sent by the account servicer to 
an account owner or to a party authorised by 
the account owner to receive the message. 
It can be used to inform the account owner, 
or authorised party, of: 
• entries reported to the account (Intraday 
Statement)
• account balance information (Account 
Balance Report)
• or both. 
for a given point in time.
The Bank to Customer Account Report is restricted to a single account 
statements per InterAct message (100,000 bytes)
This message must be bilaterally agreed between the Account Servicing 
Institution and the Account owner, and is establish by an RMA business profile.
531

Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Account Report 
message to Account Servicer and Account Owner. Whereby the report is send by the Account Servicer to the Account 
Owner and or authorised party. This message is used to inform the account owner, or authorised party, of the entries 
reported to the account, and/or to provide the owner with balance information on the account at a given point in time.
pacs.008
pacs.002
pacs.008
camt.052
camt.052
camt.052
camt.052
A B C
532

533

gpg gg,
located in the Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
For Cash Management (camt) messages the Message Identification has no exact equivalent in
the legacy MT Customer Statement message. However, the Transaction Reference Number
(Field 20) could be considered a similar comparison.
Group Header Message Identification
534

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
535

authorised by the Account Owner to receive the Account Report. 
This element should only be used to identify the Message Recipient when different from the account 
owner, which is implied by the usage of COPY in the Copy Duplicate Indicator within the nested 
Statement element.
Group Header Message Recipient
Name
Postal Address
Identification
Contact Details
Where Message Recipient is used the nested:
• Name
• Postal Address
• Identification
• Contact Details
may be used to capture information related to this party.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
536

a report, for example a camt.060 Account Reporting Request.
Where Original Business Query is used the original Message identification (i.e.,
the message identification of the camt.060 message)is required.
Original Message Name identification and Original Creation Date Time may also be
provided.
Min 1 – Max 1
Min 0 – Max 1
Group Header Original Business Query
Message Identification
? Min 0 – Max 1
Message Name Identification
Creation Date Time
537

related to the account statement.
In accordance to the usage in the camt.053 this element could be used to 
describe additional information to distinguish the different camt.052 usage i.e., 
where the report is only reporting an intraday balance, intraday entries or both.
Unlike the camt.053 there is no recommended identification string to represent 
usage.
Group Header Additional Information
Additional Information is a textual element restricted in CBPR+ to 500 
characters.
538

539

typically associated with intraday account entries and or accounting balances (where entries have been
processed on the account). The report element can be used to advise entries reported to the account
(Intraday Statement), account balance information (Account Balance Report) or both.
Report
The Report element has been restricted to one account report. To report additional accounts to
the Account Owner this would need to occur via a separate message in a similar way to the
legacy MT 942.
It should also be noted the Account Report message is modelled identically to the
Account Statement (camt.053) therefore where used as an intraday transaction report
the content can be capture identically to the statement at the close of the business day,
in the Account Statement(camt.053)
540

reporting transactional information) to identifying; the report order, the report
correlationand the last report page.
D
3 camt.052
When reporting the Balance together with Transaction entries, it is recommended to include the balance detail/s on the last report. 
Of course, where reporting only balance/s i.e. only a balance report (no entries) the data content will be contain in a single message. 
Report Pagination Legal Sequence Number
Electronic Sequence Number
Account (Identifier and Currency)
Report Pagination, Last Page Indicator
Balance Type ITAV (where balance 
information is also reported)
1 Report Pagination
Page 1
Last Page No
Electronic Sequence Number 16
Legal Sequence Number 3
Account
Id 12345
Currency EUR 
Entry
…..
2
Report Pagination
Page 2
Last Page No
Electronic Sequence Number 16
Legal Sequence Number 3
Account
Id 12345
Currency EUR 
Entry
….
3 Report Pagination
Page 3
Last Page Yes
Electronic Sequence Number 16
Legal Sequence Number 3
Account 
Id 12345
Currency EUR 
Balance
ITAV Interim Available
Entry
……
Report Order: identifying the order in which 
statements should be processed or 
reconstituted. Options:
Report Correlation: identifying statement 
which relate to each other for a given statement 
period. Options:
Last Report: identifying when no further 
statements for a given period are expected i.e. 
period statement in finalised. Options:
541

Unique reference assigned by the account servicer to
unambiguously identify the account report. Directly
comparable with the Transaction Reference Number
(Field 20) of the legacy MT statement message.
Report Identifier
542

p
Report Report Pagination
Page Number
Last Page indicator
Report Pagination includes thePage Number and Last Page indicator elements.
For example, a Page Number of 2 represents the current account report, being the
second page of the and implying a previous account report page had been sent. The
Last Page indicatorfurtherimplies whether more pages are expected
Min 1 – Max 1 Min 1 – Max 1
543
Noted: as Report Pagination is required, even if there is only one page to the report
being sent. Both the Page Number and Last Page indicator will need to be provided
i.e., 1 and Yes.

gpy p
This element allows easy recognition of the Report order, equivalent to the legacy Field
28C Statement Number. The sequence should increment for each camt.052 message sent
to the Account Owner or Authorised Party this number must be the same value where the
statement continues over multiple pages (Report Pagination) of the report for a give
account.
Should this sequence number be reset by the Account Servicer, this should not occur
more frequently than once a day. Likewise, this 18 digit counter could be incremented to
its maximum value before it’s reset.
1
2
345
The use of Electronic Sequence Number and the sequence reset logic should be
bilaterally agreed been the Account Servicer and the Account Owner
EitherElectronic Sequence Number or LegalSequence Number
Should be provided to enable the identification of a statement number.
Report Electronic Sequence Number
544

qpgq
way to identify the report order, which is not confined to numeric values.
Report Report Sequence
545
camt.060
camt report
The Reporting Sequence may be provided in the camt.060 
Account Reporting request to specify, for example, a range 
of Statements to be sent. Alternatively, Account Reports 
can often be produced on a bilaterally agreed period basis.
Where used the Reporting Sequence mandate a choice of nested element: 
• From Sequence identifies the start of a sequence range.
• To Sequence identifies the end of a sequence range.
• From To Sequence identifies the start and end of a sequence range.
• Equal Sequence identifies a sequence.
• Not Equal Sequence identifies a sequence to be excluded.
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max *
Min 1 – Max *
Min 1 – Max *
A B
D C

gpy p
Where the Intraday Account Report uses multiple camt.052 messages for a given report
period the Legal Sequence Number must be the same number in each report message
during that reporting period. This element can be considered an equivalent to the legacy
Field 28C Statement Number
Report Legal Sequence Number
546
Either Electronic Sequence Number or Legal Sequence Number should be provided to
enable the identification of a report number.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Report Creation Date Time
547

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
ppy g 
being reported.
For intraday account reports this is an important attribute that allows the account owner to understand the 
period for which the report applies. The element is not mandatory as the report may only contain the 
balance, whereby the report Creation DateTime may be used to identify the date and time associated to the 
balance.
Where From to Date is used the From Date Time and To Date Time become mandatory elements. 
10
Min 1 – Max 1 Min 1 – Max 1
Report
From to Date
To Date Time548

pg
COPY
DUPL
CODU
COPY is used when a copy of the report is sent to an Authorised Third Party, such as a
company head office, parent entity, or an institution providing additional service.
DUPL is used when a duplicate of the report is sent to the Account Owner, this
resubmission may have been requested using the camt.060 or an alternative channel
such as via internet banking or customer service request.
CODU is used when a duplicate of a report copy is sent to an Authorised Third Party, this
resubmission may have been requested using the camt.060 or an alternative channel
such as via internet banking or customer service request. It may also be requested by the
Account Owner on behalf of the Authorised Third Party, depending on the arrangement in
place with the Account Servicer.
Report Copy Duplicate Indicator
549

y y pypy 
application.
Reporting Source utilises the external Reporting Source code list. For example ACCT
represents a statement or report based on accounting data, whereas DEPT represents a
cash or deposit system.
Where the source of the statement is functionally required by the consumer of the
statement i.e., the Account Owner or authorised Third Party, the codes used should be
bilaterally agreed.
Report Reporting Source
550

Account
g y 
beneath Account.
Report Account
a unique Identification for the account, between the
Account Servicer and Account Owner. The element is
further nested by choice of IBAN or Other to capture the
account.
Min 1 – Max 1
Identification
Currency
The Currency for which the account is held. This is
identified using the three characters ISO currency
code.
Min 1 – Max 1
551

Account
y 
Name
The Name of the Account, as Assigned by the servicing
institution.
Report Account
An element which may either use an external ISO Cash Account Type code or
Type a proprietary code. It is used to identifier a particular type of account.
A nested element which contains a Proxy Identifier
together with the Proxy Type represented by either use an
external ISO Proxy Account Type code or a proprietary
code.
Proxy
A nest element that contains the Party that legally owns the
account.
Owner
A nested element which identifies the Financial Institution who manages the
account, booking entries, balances etc.
Servicer
552

pppgpg p
produced can identify the parent account they hierarchically relate to.
Report Related Account
When Related Account is utilized, like Account, the Identification and Currency
element become mandatory.
Additionally, the nested Type element, Name and nested Proxy element are optionally
available.
Min 1 – Max 1 Min 1 – Max 1
Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1
Type
Identification
Currency
Name
Proxy
Related Account uses a variety of common elements described in more detail 
within the Account section.
553

Report Interest
Interest
Reason
An element which may either use an embedded ISO Interest Type code; INDY
(Intraday) OVRN (Over Night) or a proprietary code. It is used to identifier a
particular interest type.
The optional Reason for which interest is applied.
The type of interest Rate defined as a Percentage and in an
Other form. Validity Range optionally defines an Amount, Credit
Debit Indicatorand Currency.
The date range for which interest has been calculated.
From Date Time and To Date Time must be representing
when using this element.
Provides details on any tax applied to the Interest. Where optional
Identification describes the tax levied, additionally with a Rate and or
Amount as necessary.
+
-
Type
Rate
From
To
Date
Tax
554

Balance
Balance amount.
Embedded code CRDT (Credit balance) DBIT (Debit balance)
ppg y
A nested element which may either use an external ISO Balance Type
code or a proprietary code. For example, OPAV – OpeningAvailable.
Additionally, a Sub Type represented by either use an external ISO
BalanceSub Type code or a proprietary code, may be used.
The Balance element is unlimited (Max *) whereby more that one Type of 
balance may be reported
A nested element representing the Date and the DateTime (with UTC
offset) of the balance
Min 1 – Max 1
Report Balance
Type
Amount
Credit 
Debit 
Indicator
Date
555

Code Name Definition MT 941
Comparison
CLAV ClosingAvailable Closing balance of amount of money that is at the disposal of the account owner on the date specified. Field 64
CLBD ClosingBooked 
Balance of the account at the end of the pre-agreed account reporting period. It is the sum of the opening 
booked balance at the beginning of the period and all entries booked to the account during the pre -agreed 
account reporting period. 
Field 62F
FWAV Forw ardAvailable Forward available balance of money that is at the disposal of the account owner on the date specified. Field 65
INFO Information Balance for informational purposes. No equivalent 
ITAV InterimAvailable 
Available balance calculated in the course of the account servicer's business day, at the time specified, and 
subject to further changes during the business day. The interim balance is calculated on the basis of booked 
credit and debit items during the calculation time/period specified. 
Field 64
ITBD InterimBooked 
Balance calculated in the course of the account servicer's business day, at the time specified, and subject to 
further changes during the business day. The interim balance is calculated on the basis of booked credit and 
debit items during the calculation time/period specified. 
Field 62F
OPAV OpeningAvailable Opening balance of amount of money that is at the disposal of the account owner on the date specified. No equivalent 
OPBD OpeningBooked Book balance of the account at the beginning of the account reporting period. It always equals the closing 
book balance from the previous report. Field 60F
PRCD PreviouslyClosedBooked 
Balance of the account at the previously closed account reporting period. The opening booked balance for the 
new period has to be equal to this balance.
Usage: the previously booked closing balance should equal (inclusive date) the booked closing balance of the 
date it references and equal the actual booked opening balance of the current date.
No equivalent
XPCD Expected Balance, composed of booked entries and pending items known at the time of calculation, which projects the 
end of day balance if everything is booked on the account and no other entry is posted. No equivalent 
ppgy g pp
these Balance Types. The below extract from the externalised ISO Balance Type code list compares the code 
with the population of the equivalent information in the Legacy MT 941 Balance Report. 
Report Balance Type
Take me to an implementation example involving Balance Type codes 
556

The true/false Boolean of Included to clearly determine whether the Credit Line Amount is
included in the balance is mandatory in the set of Credit Line element.
Additionally, the following optional nested element may be used to identify:
• The Type of Credit Line, which may either use an external ISO Credit Line Type
code or a proprietary code.
• A set of elements to provide Credit Line details
• The Amount(Currency and Amount) of the Credit Line
• The Date (nested as Date, DateTime) of the Credit Line, provided to distinguish
where multiple Credit Line exist.
The Credit Line element is unlimited (Max *) whereby more that one Credit Line 
may be reported, the Date becomes an important element to distinguish between 
different Credit Lines. 
Report Balance
The final optional nested element within Balance is the Availability of the booked amount i.e., when it is available to be 
accessed.
Credit Line
Type
Amount
Credit Debit Indicator
Date
Availability
Min 0 – Max *
557

y y g 
reported using multiple camt.052 messages for a given reporting period the Transaction Summary should only 
be included on the first Report message (Balance Type OPBD with no Balance Sub Type) summarizing the whole 
Statement Report (entire statement period) This aligns with the Common Global Implementation (CGI) where a Transaction 
Summary, if provided, would appear before the first Entry elements.
The Total Entries Per Bank Transaction Code element is unlimited (Max *) 
whereby more that one Bank Transaction Code may be summarised.
Report Transaction Summary
Total Credit Entries
Total Entries
Total Debit Entries
Total Entries per Bank 
Transaction Code
Each of the following element allow an optional total of entries either as a Number of
Entries and or as a Sum.
➢ Total Entries
➢ Total Credit Entries
➢ Total Debit Entries
➢ Total EntriesPer Bank Transaction Code
In addition to the Number of Entries and Sum, the Total Entries Per Bank Transaction
Code requires the Bank Transaction Code element and optionally allows a variety of
other optional elements.
Min 0 – Max *
Min 1 – Max 1
558

pyy 
posted across them, this set of nested elements is arguably the most relevant for the account owner and in 
many way is comparable with the MT 942 Field 61 Statement Line.
Unlike the legacy MT Interim 
Transaction Report message, the 
camt.052 has a number of 
dedicated elements to capture a 
variety of entry level data. 
It also has a number of 
enhancements on the legacy MT 
Interim Transaction Report 
message where parties in the 
payment and customer remittance 
information, as examples, can 
provided to the Account Owner. 
Report Entry
Entry
Reference
Min 0 – Max 1
Amount
Min 1 – Max 1
Credit
Debit
Indicator
Min 1 – Max 1
Reversal
Indicator
Min 0 – Max 1
Status
Min 1 – Max 1
Booking
Date
Min 0 – Max 1
Value
Date
Min 1 – Max 1
Account
Servicer
Reference
Min 0 – Max 1
Availability
Min 0 – Max *
Bank
Transaction
Code
Min 1 – Max 1
Commission
Waiver
Indicator
Min 0 – Max 1
Additional
Information
Indicator
Min 0 – Max 1
Amount
Details
Min 0 – Max 1
Charges
Min 0 – Max 1
Technical
Input
Channel
Min 0 – Max 1
Interest
Min 0 – Max 1
Card
Transactions
Min 0 – Max 1
Entry
Details
Min 0 – Max *
Additional
Statement
Information
Min 0 – Max 1
559

Report Entry
y
Reference
assign to identify the entry posted to the account. 
Amount Mandatory element representing the currency and amount of the entry. This can be compared 
to Field 61 subfield 4 and 5 of the legacy MT 942.
Min 1 – Max 1
Credit
Debit
Indicator
Mandatory element indicating whether the Amount entry is a DBIT (Debit) or CRDT (Credit) to 
the account. This can be compared to Field 61 subfield 3 of the legacy MT 942.
Min 1 – Max 1
Reversal
Indicator
Indicates whether the entry is a result of a reversal. for example, an entry related to a pacs.004 
Payment Return or reverses an error such as an incorrect value date applied to the entry.
Where the Reversal Indicator is Yes, the Credit Debit Indicator should be the opposite of the 
original entry, for example original Credit Debit Indicator of CRDT would expect a reversal entry 
Credit Debit Indicator of DBIT. This can be compared to Field 61 subfield 3 of the legacy MT 942 
where a reversal code may be used.
Min 0 – Max 1
560

Report Entry
Noting CBPR+ usage guidelines 
mandate the time zone that the 
Date Time represents as an 
offset against Universal Time 
Coordinated (UTC)
used to confirm the entry is booked. 
Status BOOK is the only status that can be reversed using the Reverse Indicator 
Status
Mandatory choice of Date or Date Time the entry was posted to the Account. This can be 
compared to Field 61 subfield 2 of the legacy MT 942.
Booking
Date
Min 0 – Max 1
Mandatory choice of Date or Date Time the entry 
become available. This can be compared to Field 61 
subfield 1 of the legacy MT 942.
Value
Date
Min 1 – Max 1
Additional optional Reference typically assigned by the Account Servicer’s payment engine or 
accounting platform. This reference would be used to query an entry. This can be compared to 
Field 61 subfield 8 of the legacy MT 942.
Account
Servicer
Reference
Min 0 – Max 1
Availability Indicates when the booked amount is available i.e., when it is available to be accessed.
Min 0 – Max *
561

Report Entry Bank Transaction Code
Transaction
Code
is designed to deliver a 
harmonized set of codes, 
which should be applied in 
bank-to-customer cash account 
reporting information. The bank 
transaction code information 
allows the account servicer to 
correctly report a transaction, 
which in its turn will help 
account owners to perform 
their cash management and 
reconciliation operations. Domain
Family
Sub-Family
Transaction Code has three levels:
Domain: Highest definition 
level to identify the sub-ledger. The domain defines 
the business area of the 
underlying transaction e.g., 
payment, securities etc.)
Family: Medium definition 
level e.g. type of payment; 
credit transfer, direct debit etc.
Sub-family: Lowest definition 
level e.g. type of cheques; 
draft etc. 
Bank Transaction Codes are an 
external code set defined in the Bank 
Transaction Code combinations 
external code sets.
Family
Domain
Sub Family
562

available to download from the ISO20022.org external 
code list page. These include the descriptions for 
Payments Domain Families and sub-families for both 
Received and Issued Credit Transfers. 
https://www.iso20022.org/external_code_list.page
563

All codes in light grey are defined as the generic codes available for all Domains and Families
Domain Family SubFamily Domain Code
ExternalBankTransactionDomain1Code
Family Code
ExternalBankTransactionFamily1Code
SubFamily Code
ExternalBankTransactionSubFamily1Code
Status
Status Date
Payments Issued Credit Transfers Cross-Border Credit Transfer PMNT ICDT XBCT New 27/4/2009
Payments Received Credit 
Transfers
Cross-Border Credit Transfer PMNT RCDT XBCT New 27/4/2009
Bank Transaction Codes are an external code set defined in the Bank Transaction Code combinations external 
code sets.
As an example a debit statement transaction which relates to a cross-border payment initiated from an account 
would be represented by: 
Domain Family Sub-Family
PMNT (Payment) ICDT (Issued Credit Transfer) XBCT (Cross-Border Credit Transfer
564

Report Entry
Waiver
Indicator
not typically associated with Correspondent Banking payments
Optional element indicating whether the underlying transaction details are provided through a 
separate message. Where the Message Name Identification represents the message used to 
provide the additional information and Message Identification specifies the reference of the 
message that provides the additional information. 
Additional
Information
Indicator
Min 0 – Max 1
Optional nested element which provides various elements to represent an aggregated 
(consolidated) original amount. Where individual transaction amounts can be represented, if 
required, within the Entry Detail set of elements.
This element is useful to capture original amount details where they are different to the Entry, 
Amount, for example the Instructed Amount of the payment can be included, together with a 
potential Currency Exchange rate, where necessary.
Amount
Details
Min 0 – Max 1
Optional nested element to provide information on charges either pre-advised or taken from the 
entry.
Charges
Min 0 – Max 1
565

Report Entry
used to represent the technical channel used to input the entry. 
Input
Channel
Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry 
amount.
Interest
Min 0 – Max 1
Optional nested element which provides details associated with a card transaction such as the 
card number, card brand etc. 
Card
Transactions
Min 0 – Max 1
Additional optional nested element containing details on the entry. See dedicated section on 
Entry Details.
Entry
Details
Min 0 – Max *
Additional
Statement
Information
Additional optional element to represent further information related to the account 
statement.
Min 0 – Max 1
566

py
Report Entry Entry Details
Transaction Details
Batch
567
Batch provides details on batched transactions such as the total Number of Transactions 
the batched entry (sometimes referred to as a consolidated entry) represents.
Transaction Details is a significant nested element which represents information on the 
underlying transaction.

y
Transaction Details has a variety of nested elements closely associated with Entry level
elements. The References element however is nested to include a variety of references 
related to the entry including for example the UETR
Report Entry Entry Details Transaction Details
$
Additionally, Transaction Details also has a variety of elements capturing details from the underlying 
transaction, which amongst other business transactions includes payment transaction data. For example, 
Remittance Information and Related Parties
References
Min 1 – Max 1
Amount
Min 1 – Max 1
Credit
Debit
Indicator
Min 1 – Max 1
Amount
Details
Min 0 – Max 1
Availability
Min 0 – Max*
Bank
Transaction
Code
Min 0 – Max 1
Charges
Min 0 – Max 1
Interest
Min 0 – Max 1
568

pyg y (
Related Parties/Agents belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in 
the pacs messages can be transferred into the Cash Management (camt) message.
These Related Parties include :
• Instructing Party
• Debtor 
• Debtor Account
• Ultimate Debtor
• Creditor
• Creditor Account
• Ultimate Creditor
These Related Agents include :
• Instructing Agent
• Instructed Agent
• Debtor Agent
• Creditor Agent
• Intermediary Agent 1
• Intermediary Agent 2
• Intermediary Agent 3
Trading Party is also present in the Related Parties elements, and the following are present in the Related Agents elements: 
Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place. Although these elements are not directly 
associated with a payment, as a Customer receiving an Account Report related to other Business Domains e.g. a Security 
Settlement, it could be conceivable that these optional CBPR+ element may be populated
Report Entry Entry Details Transaction Details
Related Agents
Related Parties
569

gpyg py
Report Entry Entry Details Transaction Details
These are: 
• Local Instrument
• Purpose
• Related Remittance Information
• Remittance Information
• Related Dates such as the Interbank Settlement Date
• Tax
Remittance Information as an end-to-end element should be passed unaltered from Payment Initiation 
(pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account 
Statement/Account Report (camt) The Remittance Information element is common to these message sets.
For Payment Return (pacs.004) it is also possible to capture Return Information which 
includes:
• The Original Bank Transaction Code of the original Entry
• The Originatorof the return from the pacs.004
• And the Reason code.
570

py
payments, as well as have an element to capture Additional Transaction Information.
Report Entry Entry Details Transaction Details
These are: 
• Related Quantity
• Financial Instrument Identification
• Corporate Action
• Safekeeping Account
• Cash Deposit
• Card Transactions
571

Bank to Customer Reports 
Use Case c.52.1.a – Bank to Customer Account Balance Report produced by the Creditor Agent
Use Case c.52.1.b – Bank to Customer Account Intraday Transaction Report produced by the Creditor Agent
Use Case c.52.1.b.1 – Bank to Customer Account Intraday Transaction Report/s and Account Statement produced by the Creditor Agent
Use Case c.52.1.c – Bank to Customer Account Intraday Transaction and Balance Report produced by the Creditor Agent
Use Case camt.060 for requesting 
a Bank to Customer report
572
Use Case for copy or duplicate 
reports refer to camt.053 use cases

pacs.008
pacs.008 pacs.008
3 
camt.052
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
2 4
Creditor Agent credits the 
account of the Creditor
5
Creditor Agent as the Account 
Servicer produces and sends a 
balance report to either the 
Account Owner, or an 
authorised third party.
6
6
A B C
D
573

pacs.008
pacs.008 pacs.008
3 
camt.052
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
2 4
Creditor Agent credits the 
account of the Creditor
5
Creditor Agent as the Account 
Servicer produces and sends a 
balance report to either the 
Account Owner, or an 
authorised third party.
6
6
A B C
D
574

pacs.008
pacs.008 pacs.008
3
camt.052
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
32
4
Creditor Agent credits the 
account of the Creditor
5
Creditor Agent as the Account 
Servicer produces and sends 
several intraday transaction 
reports throughout the business 
day to either the Account 
Owner, or an authorised third 
party.
6
A
B
C
D
575
camt.053
Creditor Agent C as the 
Account Servicer produces an 
Account Statement at the close 
of the business day reflecting all 
the transaction entries, include 
those provide in the Intraday 
Transaction Report
7
7

pacs.008
pacs.008 pacs.008
3 
camt.052
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
2 4
Creditor Agent credits the 
account of the Creditor
5
Creditor Agent as the Account 
Servicer produces and sends a 
intraday transaction and 
balance report to either the 
Account Owner, or an 
authorised third party.
6
6
A B C
D
576

Bank to Customer 
Statement
577

camt.053
Group Header
Statement
message is sent by the account 
servicer to an account owner or to a 
party authorised by the account owner 
to receive the message. It is used to 
inform the account owner, or 
authorised party, of the entries booked 
to the account, and to provide the 
owner with balance information on the 
account at a given point in time 
The Bank to Customer Account Statement is restricted to a single
account statements per InterAct message (100,000 bytes)
This message must be bilaterally agreed between the Account 
Servicing Institution and the Account owner, and is establish by an 
RMA business profile.
578

Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Statement 
message to Account Servicer and Account Owner. Whereby the statement is send by the Account Servicer to the Account 
Owner and or authorised party. This message is used to inform the account owner, or authorised party, of the entries 
booked to the account, and to provide the owner with balance information on the account at a given point in time.
pacs.008
pacs.002
pacs.008
camt.053
camt.053
camt.053
camt.053
A B C
579

has several considerations fortheAccount Serving Institution.
Statement Pagination
Account (Identification)
needed to create MT 940 Field 28C Sequence Number
580
Legal Sequence Number needed to create MT 940 Field 28C Statement Number
needed to create MT 940 Field 25a Account Identification
Statement Identification needed to create MT 940 Field 20 Transaction Reference Number
Balance Type 
OPBD (with no Sub Type INTM)
OPBD (with Sub Type INTM)
needed to create MT 940 Field 60F (first) Opening Balance
needed to create MT 940 Field 60M (intermediate) Opening Balance
Balance Type 
CLBD (with no Sub Type INTM)
CLBD (with Sub Type INTM)
needed to create MT 940 Field 62F (final) Closing Balance
needed to create MT 940 Field 62M (intermediate) Closing Balance
ISO MT
ISO 20022 message element MT Field Name & (Tag option)
Entry used to create MT 940 Field 61 Statement Line
Note up to 190 Entry occurrences will translate into a basic MT 940 
(inside of the existing MT 940 message size)

581
ISO
ISO 20022 message element
MT
MT Field Name & (Tag option)
➢ Transaction Reference Number (Field 20)
Sequence 
➢ Further Identification (Field 13C)
➢ Account Identification (Field 25)
➢ Effective Date of New Rate (Field 30)
➢ New Interest Rate (Field 37H)
➢ Sender To Receiver Information (Field 72)
Note - various other elements are mandatory in the camt.053 which are not derived from the payment instruction including ; Message Identification, Creation Date Time, Statement Identification, Statement 
Pagination, Balance, Credit Debit Indicator, Status, Bank Transaction Code/.. often these data elements and potentially other optional elements will be generated by the bank application when creating th e 
reporting message.
➢ Group Header / Message Identification
➢ Statement / Account / Identification
➢ Statement / Interest / From Date
➢ Statement / Interest / Rate 
NOT MAPPED
against the legacy MT 935 useful. However, compared the camt.053 to legacy MT, using the camt.053 is like combining
the information of both the MT 935 and MT 940 together into one message.
NOT MAPPED

582

gpg gg,
located in the Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
For Cash Management (camt) messages the Message Identification has no exact equivalent in
the legacy MT Customer Statement message. However, the Transaction Reference Number
(Field 20) could be considered a similar comparison.
Group Header Message Identification
583

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
584

authorised by the Account Owner to receive the Account Statement. 
This element should only be used to identify the Message Recipient when different from the account 
owner, which is implied by the usage of COPY in the Copy Duplicate Indicator within the nested 
Statement element.
Group Header Message Recipient
Name
Postal Address
Identification
Contact Details
Where Message Recipient is used the nested:
• Name
• Postal Address
• Identification
• Contact Details
may be used to capture information related to this party.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
585

report, for example a camt.060 Account Reporting Request.
Where Original Business Query is used the original Message identification (i.e.,
the message identification of the camt.060 message)is required.
Original Message Name identification and Original Creation Date Time may also be
provided.
Min 1 – Max 1
Min 0 – Max 1
Group Header Original Business Query
Message Identification
? Min 0 – Max 1
Message Name Identification
Creation Date Time
586

the account statement.
Where the camt.053 is used for various end of cycle statement reporting 
(statement periods) the follow codes may be used to distinguish the 
different camt.053 usage: 
/EODY/ for End of Day - Daily Statement 
/EOWK/ for End of Week - Weekly Statement 
/EOMH/ for End of Month - Monthly Statement 
/EOYR/ for End of Year - Yearly Statement
Group Header Additional Information
Additional Information is a textual element restricted in CBPR+ to 500 
characters.
587

588

account, most typically associated with account balances, and accounting entries (where entries have 
been processed on the account).
Statement
The Statement element has been restricted to one statements. To report additional
account statements to the Account Owner this would need to occur via a separate
message in a similar way to the legacy MT 940 or MT 950.
589
It should also be noted the Account Statement message is modelled identically to the
Account Report (camt.052) therefore where an intraday transaction report is used the
content can be capture identically to the statement at the close of the business day, in
theAccount Statement (camt.053)

size. Consideration therefore need to be given to identifying; the statement
order, the statement correlation and the last statement page.
D
3 camt.053
Balance Sub Type code INTM is essential for identifying Interim Opening and Interim Closing balances in a statement sent over more than 
one message. Balance Type OPBD and CLBD without Sub Type code identify the first (OPBD) and last (CLBD) statement page..
Statement Pagination Statement Pagination, Last Page Indicator
Balance Type CLBD (with no Sub Type INTM)
1 Statement Pagination
Page 1
Last Page No
Electronic Sequence Number 16
Legal Sequence Number 3
Account
Id 12345
Currency EUR 
Balance
OPBD (Opening Booked) 
CLBD (Closing Booked) 
Sub Type INTM (Interim)
2
Statement Pagination
Page 2
Last Page No
Electronic Sequence Number 16
Legal Sequence Number 3
Account
Id 12345
Currency EUR 
Balance
OPBD (Opening Booked) 
Sub Type INTM (Interim)
CLBD (Closing Booked) 
Sub Type INTM (Interim)
3 Statement Pagination
Page 3
Last Page Yes
Electronic Sequence Number 16
Legal Sequence Number 3
Account 
Id 12345
Currency EUR 
Balance
OPBD (Opening Booked)
Sub Type INTM (Interim)
CLBD Closing Booked 
Statement Order: identifying the order in 
which statements should be processed or 
reconstituted. Options:
Statement Correlation: identifying statement 
which relate to each other for a given statement 
period. Options:
Last Statement: identifying when no further 
statements for a given period are expected i.e. 
period statement in finalised. Options:
Closing Interim 
=
Opening Interim
of next statement
Closing Interim 
=
Opening Interim
of next statement
590
Legal Sequence Number
Electronic Sequence Number
Account (Identifier and Currency)

Unique reference assigned by the account servicer to
unambiguously identify the account statement. Directly
comparable with the Transaction Reference Number
(Field 20) of the legacy MT statement message.
Statement Identifier
591

Statement Statement Pagination
Page Number
Last Page indicator
Statement Pagination includes the Page Number and Last Page indicator
elements.
For example a Page Number of 2 represents the current account statement, being the
second page of the and implying a previous account statement page had been sent.
The Last Page indicatorfurtherimplies whether more pages are expected
Min 1 – Max 1 Min 1 – Max 1
592
Note: Where Page Number is equal to 1 a Balance Type OPBD (Opening Booked)must be provided, 
without a sub type of INTM (Interim). Whereas if the Page Number is greater than 1 a Balance Type 
OPBD (Opening Booked) must be provided, with a sub type of INTM (Interim). 
Where Last Page Indicator is true a Balance Type CLBD (Closing Booked) must be provided, without 
a sub type of INTM (Interim). Whereas if the Last Page Indicator is false a Balance Type CLBD 
(Closed Booked) must be provided, with a sub type of INTM (Interim).

gy p
This element allows easy recognition of the statement order, equivalent to the legacy Field
28C Statement Number. The sequence should increment for each camt.053 electronic
statement sent to the Account Owner or Authorised Party this number must be the same
value where the statement continues over multiple pages (Statement Pagination) of the
statement for a give account on a given day.
Should this sequence number be reset by the Account Servicer, this should not occur
more frequently than once a year. Likewise, this 18 digit counter could be incremented to
its maximum value before it’s reset.
1
2
345
The use of Electronic Sequence Number and the sequence reset logic should be
bilaterally agreed been the Account Servicer and the Account Owner.
EitherElectronic Sequence Number or LegalSequence Number
Should be provided to enable the identification of a statement number.
Statement Electronic Sequence Number
593

qgq
as a way to identify the statement order, which is not confined to numeric values.
Statement Report Sequence
594
camt.060
camt report
The Reporting Sequence may be provided in the camt.060 
Account Reporting request to specify, for example, a range of 
Statements to be sent. More traditionally Account Statements 
are generated automatically on an end of day cycle.
Where used the Reporting Sequence mandate a choice of nested element: 
• From Sequence identifies the start of a sequence range.
• To Sequence identifies the end of a sequence range.
• From To Sequence identifies the start and end of a sequence range.
• Equal Sequence identifies a sequence.
• Not Equal Sequence identifies a sequence to be excluded.
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max *
Min 1 – Max *
Min 1 – Max *
A B
D C

y p
Where the statement is reported using multiple camt.053 messages for a given statement
period the Legal Sequence Number must be the same number in each statement
message, as it can be used to correlate the statements.
Where a paper statement is a legal requirement, it may have a number different from the
electronic sequential number. In this case the Legal Sequence Number element
represents the sequence number of the paper statement.
Statement Legal Sequence Number
595
Either Electronic Sequence Number or Legal Sequence Number must be provided to
enable the identification of a statement number.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Statement Creation Date Time
596

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
pp
Where From to Date is used the From Date Time and To Date Time become mandatory elements. 
10
Min 1 – Max 1 Min 1 – Max 1
Statement
From to Date
To Date Time597

g
COPY
DUPL
CODU
COPY is used when a copy of the statement is sent to an Authorised Third Party, such as
a company head office, parent entity, or an institution providing additional service such as
liquidity sweeping or statement consolidation.
DUPL is used when a duplicate of the statement is sent to the Account Owner, this
resubmission may have been requested using the camt.060 or an alternative channel
such as via internet banking or customer service request.
CODU is used when a duplicate of a statement copy is sent to an Authorised Third Party,
this resubmission may have been requested using the camt.060 or an alternative channel
such as via internet banking or customer service request. It may also be requested by the
Account Owner on behalf of the Authorised Third Party, depending on the arrangement in
place with the Account Servicer.
Statement Copy Duplicate Indicator
598

ypy pp
Reporting Source utilises the external Reporting Source code list. For example ACCT
represents a statement or report based on accounting data, whereas DEPT represents a
cash or deposit system.
Where the source of the statement is functionally required by the consumer of the
statement i.e., the Account Owner or Authorised Third Party, the codes used should be
bilaterally agreed.
Statement Reporting Source
599

Account
g y 
Account.
Statement Account
a unique Identification for the account, between the
Account Servicer and Account Owner. The element is
further nested by choice of IBAN or Other to capture the
account.
Min 1 – Max 1
Identification
Currency
The Currency for which the account is held. This is
identified using the three characters ISO currency
code.
Min 1 – Max 1
600

Account
y 
Name
The Name of the Account, as Assigned by the servicing
institution.
Statement Account
An element which may either use an external ISO Cash Account Type code or
Type a proprietary code. It is used to identifier a particular type of account.
A nested element which contains a Proxy Identifier
together with the Proxy Type represented by either use an
external ISO Proxy Account Type code or a proprietary
code.
Proxy
A nest element that contains the Party that legally owns the
account.
Owner
A nested element which identifies the Financial Institution who manages
Servicer the account, booking entries, balances etc.
601
In an account concentrator use case, this element should be utilised to capture the 
account servicer details.

ppgpg 
is produced can identify the parent account they hierarchically relate to.
Statement Related Account
When Related Account is utilized, like Account, the Identification and Currency
element become mandatory.
Additionally the nested Type element, Name and nested Proxy element are optionally
available.
Min 1 – Max 1 Min 1 – Max 1
Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1
Type
Identification
Currency
Name
Proxy
Related Account uses a variety of common elements described in more detail 
within the Account section.
602

Statement Interest
Interest
Reason
An element which may either use an embedded ISO Interest Type code; INDY
(Intraday) OVRN (Over Night) or a proprietary code. It is used to identifier a
particular interest type.
The optional Reason for which interest is applied.
The type of interest Rate defined as a Percentage and in an
Other form. Validity Range optionally defines an Amount, Credit
Debit Indicatorand Currency.
The date range for which interest has been calculated.
From Date Time and To Date Time must be representing
when using this element.
Provides details on any tax applied to the Interest. Where optional
Identification describes the tax levied, additionally with a Rate and or
Amount as necessary.
+
-
Type
Rate
From
To
Date
Tax
603 Note interest reported on an account is 
commonly associated to the legacy MT 935

Balance
Balance amount.
Embedded code CRDT (Credit balance) DBIT (Debit balance)
ppg 
mandatory
A nested element which may either use an external ISO Balance Type
code or a proprietary code. For example, OPAV – OpeningAvailable.
Additionally, a Sub Type represented by either use an external ISO
BalanceSub Type code or a proprietary code, may be used.
The Balance element is unlimited (Max *) whereby more that one Type of 
balance may be reported
A nested element representing the Date and the DateTime (with UTC
offset) of the balance
Min 1 – Max 1
Statement Balance
Type
Amount
Credit 
Debit 
Indicator
Date
Balance Sub Type code INTM is essential for identifying opening and closing 
balances in a statement sent over more than one message. 
604

Code Sub 
Type Name Definition MT 940 
Comparison
CLAV ClosingAvailable Closing balance of amount of money that is at the disposal of the account owner on the date specified. Field 64
CLBD
ClosingBooked Balance of the account at the end of the pre-agreed account reporting period. It is the sum of the opening booked balance at the beginning 
of the period and all entries booked to the account during the pre-agreed account reporting period. Field 62F
INTM ClosingBooked (Interim) Interim Balance of the account at the end of the pre-agreed account reporting page. It is the sum of the opening booked 
balance at the beginning of the period and all entries booked to the account during the pre-agreed account reporting page. Field 62M
FWAV Forw ardAvailable Forward available balance of money that is at the disposal of the account owner on the date specified. Field 65
INFO Information Balance for informational purposes. No equivalent 
ITAV InterimAvailable 
Available balance calculated in the course of the account servicer's business day, at the time specified, and subject to further changes 
during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period 
specified. 
No equivalent 
ITBD InterimBooked Balance calculated in the course of the account servicer's business day, at the time specified, and subject to further changes during the 
business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified. No equivalent 
OPAV OpeningAvailable Opening balance of amount of money that is at the disposal of the account owner on the date specified. No equivalent 
OPBD
OpeningBooked Book balance of the account at the beginning of the account reporting period. It always equals the closing book balance from the previous 
report. Field 60F
INTM OpeningBooked (Interim) Interim Book balance of the account at the beginning of the account reporting page. It alw ays equals the closing book 
balance from the previous report page. Field 60M
PRCD PreviouslyClosedBooked 
Balance of the account at the previously closed account reporting period. The opening booked balance for the new period has to be equal 
to this balance.
Usage: the previously booked closing balance should equal (inclusive date) the booked closing balance of the date it references and equal 
the actual booked opening balance of the current date.
Field 60F
XPCD Expected Balance, composed of booked entries and pending items known at the time of calculation, which projects the end of day balanceif
everything is booked on the account and no other entry is posted. No equivalent 
ppgy g pp
these Balance Types. The below extract from the externalised ISO Balance Type code list compares the code 
with the population of the equivalent information in the Legacy MT 940 Customer Statement. 
Statement Balance Type
Take me to an implementation example involving Balance Type codes 605

The true/false Boolean of Included to clearly determine whether the Credit Line Amount is
included in the balance is mandatory in the set of Credit Line element.
Additionally, the following optional nested element may be used to identify:
• The Type of Credit Line, which may either use an external ISO Credit Line Type
code or a proprietary code.
• A set of elements to provide Credit Line details
• The Amount(Currency and Amount) of the Credit Line
• The Date (nested as Date, DateTime) of the Credit Line, provided to distinguish
where multiple Credit Line exist.
The Credit Line element is unlimited (Max *) whereby more that one Credit Line 
may be reported, the Date becomes an important element to distinguish between 
different Credit Lines. 
Statement Balance
The final optional nested element within Balance is the Availability of the booked amount i.e., when it is available to be 
accessed.
Credit Line
Type
Amount
Credit Debit Indicator
Date
Availability
Min 0 – Max *
606

y pg pg
given statement period the Transaction Summary should only be included on the opening Statement message 
(Balance Type OPBD with no Balance Sub Type) summarizing the whole Statement Report (entire statement period) This 
aligns with the Common Global Implementation (CGI) where a Transaction Summary, if provided, would appear before the first 
Entry elements.
The Total Entries Per Bank Transaction Code element is unlimited (Max *) 
whereby more that one Bank Transaction Code may be summarised.
Statement Transaction Summary
Total Credit Entries
Total Entries
Total Debit Entries
Total Entries per Bank 
Transaction Code
Each of the following element allow an optional total of entries either as a Number of
Entries and or as a Sum.
➢ Total Entries
➢ Total Credit Entries
➢ Total Debit Entries
➢ Total EntriesPer Bank Transaction Code
In addition to the Number of Entries and Sum, the Total Entries Per Bank Transaction
Code requires the Bank Transaction Code element and optionally allows a variety of
other optional elements.
Min 0 – Max *
Min 1 – Max 1
607

pyp
this set of nested elements is arguably the most relevant for the account owner and in many way is comparable 
with the MT 940 Field 61 Statement Line.
Unlike the legacy MT Statement 
messages, the camt.053 has a 
number of dedicated elements to 
capture a variety of entry level 
data. 
It also has a number of 
enhancements on the legacy MT 
Statement message where parties 
in the payment and customer 
remittance information, as 
examples, can provided to the 
Account Owner. 
Statement Entry
Entry
Reference
Min 0 – Max 1
Amount
Min 1 – Max 1
Credit
Debit
Indicator
Min 1 – Max 1
Reversal
Indicator
Min 0 – Max 1
Status
Min 1 – Max 1
Booking
Date
Min 0 – Max 1
Value
Date
Min 1 – Max 1
Account
Servicer
Reference
Min 0 – Max 1
Availability
Min 0 – Max *
Bank
Transaction
Code
Min 1 – Max 1
Commission
Waiver
Indicator
Min 0 – Max 1
Additional
Information
Indicator
Min 0 – Max 1
Amount
Details
Min 0 – Max 1
Charges
Min 0 – Max 1
Technical
Input
Channel
Min 0 – Max 1
Interest
Min 0 – Max 1
Card
Transactions
Min 0 – Max 1
Entry
Details
Min 0 – Max *
Additional
Statement
Information
Min 0 – Max 1
608

Statement Entry
y
Reference
assign to identify the entry posted to the account. 
Amount Mandatory element representing the currency and amount of the entry. This can be compared 
to Field 61 subfield 4 and 5 of the legacy MT 940.
Min 1 – Max 1
Credit
Debit
Indicator
Mandatory element indicating whether the Amount entry is a DBIT (Debit) or CRDT (Credit) to 
the account. This can be compared to Field 61 subfield 3 of the legacy MT 940.
Min 1 – Max 1
Reversal
Indicator
Indicates whether the entry is a result of a reversal. for example, an entry related to a pacs.004 
Payment Return or reverses an error such as an incorrect value date applied to the entry.
Where the Reversal Indicator is Yes, the Credit Debit Indicator should be the opposite of the 
original entry, for example original Credit Debit Indicator of CRDT would expect a reversal entry 
Credit Debit Indicator of DBIT. This can be compared to Field 61 subfield 3 of the legacy MT 940 
where a reversal code may be used.
Min 0 – Max 1
609
Amount element within CBPR+ allows up to 18 digits unlike the payment messages. It allows entries reported for 
non CBPR+ transactions to be reported.
y
Reference

Statement Entry
Noting CBPR+ usage guidelines 
mandate the time zone that the 
Date Time represents as an 
offset against Universal Time 
Coordinated (UTC)
used to confirm the entry is booked. 
Status BOOK is the only status that can be reversed using the Reverse Indicator 
Status
Mandatory choice of Date or Date Time the entry was posted to the Account. This can be 
compared to Field 61 subfield 2 of the legacy MT 940.
Booking
Date
Min 0 – Max 1
Mandatory choice of Date or Date Time the entry 
become available. This can be compared to Field 61 
subfield 1 of the legacy MT 940.
Value
Date
Min 1 – Max 1
Additional optional Reference typically assigned by the Account Servicer’s payment engine or 
accounting platform. This reference would be used to query an entry. This can be compared to 
Field 61 subfield 8 of the legacy MT 940.
Account
Servicer
Reference
Min 0 – Max 1
Availability Indicates when the booked amount is available i.e., when it is available to be accessed.
Min 0 – Max *
610

Statement Entry Bank Transaction Code
Transaction
Code
is designed to deliver a 
harmonized set of codes, 
which should be applied in 
bank-to-customer cash account 
reporting information. The bank 
transaction code information 
allows the account servicer to 
correctly report a transaction, 
which in its turn will help 
account owners to perform 
their cash management and 
reconciliation operations. Domain
Family
Sub-Family
Transaction Code has three levels:
Domain: Highest definition 
level to identify the sub-ledger. The domain defines 
the business area of the 
underlying transaction e.g., 
payment, securities etc.)
Family: Medium definition 
level e.g. type of payment; 
credit transfer, direct debit etc.
Sub-family: Lowest definition 
level e.g. type of cheques; 
draft etc. 
Bank Transaction Codes are an 
external code set defined in the Bank 
Transaction Code combinations 
external code sets.
Family
Domain
Sub Family
611

available to download from the ISO20022.org external 
code list page. These include the descriptions for 
Payments Domain Families and sub-families for both 
Received and Issued Credit Transfers. 
https://www.iso20022.org/external_code_list.page
612

All codes in light grey are defined as the generic codes available for all Domains and Families
Domain Family SubFamily Domain Code
ExternalBankTransactionDomain1Code
Family Code
ExternalBankTransactionFamily1Code
SubFamily Code
ExternalBankTransactionSubFamily1Code
Status
Status Date
Payments Issued Credit Transfers Cross-Border Credit Transfer PMNT ICDT XBCT New 27/4/2009
Payments Received Credit 
Transfers
Cross-Border Credit Transfer PMNT RCDT XBCT New 27/4/2009
Bank Transaction Codes are an external code set defined in the Bank Transaction Code combinations external 
code sets.
As an example a debit statement transaction which relates to a cross-border payment initiated from an account 
would be represented by: 
Domain Family Sub-Family
PMNT (Payment) ICDT (Issued Credit Transfer) XBCT (Cross-Border Credit Transfer
613

Statement Entry
Waiver
Indicator
not typically associated with Correspondent Banking payments
Optional element indicating whether the underlying transaction details are provided through a 
separate message. Where the Message Name Identification represents the message used to 
provide the additional information and Message Identification specifies the reference of the 
message that provides the additional information. 
Additional
Information
Indicator
Min 0 – Max 1
Optional nested element which provides various elements to represent an aggregated 
(consolidated) original amount. Where individual transaction amounts can be represented, if 
required, within the Entry Detail set of elements.
This element is useful to capture original amount details where they are different to the Entry, 
Amount, for example the Instructed Amount of the payment can be included, together with a 
potential Currency Exchange rate, where necessary.
Amount
Details
Min 0 – Max 1
Optional nested element to provide information on charges either pre-advised or taken from the 
entry.
Charges
Min 0 – Max 1
614

Statement Entry
used to represent the technical channel used to input the entry. 
Input
Channel
Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry 
amount.
Interest
Min 0 – Max 1
Optional nested element which provides details associated with a card transaction such as the 
card number, card brand etc. 
Card
Transactions
Min 0 – Max 1
Additional optional nested element containing details on the entry. See dedicated section on 
Entry Details.
Entry
Details
Min 0 – Max *
Additional
Statement
Information
Additional optional element to represent further information related to the account 
statement.
Min 0 – Max 1
615

py
Statement Entry Entry Details
Transaction Details
Batch
616
Batch provides details on batched transactions such as the total Number of Transactions 
the batched entry (sometimes referred to as a consolidated entry) represents.
Transaction Details is a significant nested element which represents information on the 
underlying transaction.

y
Transaction Details has a variety of nested elements closely associated with Entry level
elements. The References element however is nested to include a variety of references 
related to the entry including for example the UETR
Statement Entry Entry Details Transaction Details
$
Additionally, Transaction Details also has a variety of elements capturing details from the underlying 
transaction, which amongst other business transactions includes payment transaction data. For example, 
Remittance Information and Related Parties
References
Min 1 – Max 1
Amount
Min 1 – Max 1
Credit
Debit
Indicator
Min 1 – Max 1
Amount
Details
Min 0 – Max 1
Availability
Min 0 – Max*
Bank
Transaction
Code
Min 0 – Max 1
Charges
Min 0 – Max 1
Interest
Min 0 – Max 1
617
Amount element within CBPR+ allows up to 18 digits unlike the payment messages. It allows entries reported for 
non CBPR+ transactions to be reported.

yg y (
Parties/Agents belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs 
messages can be transferred into the Cash Management (camt) message.
These Related Parties include :
• Instructing Party
• Debtor 
• Debtor Account
• Ultimate Debtor
• Creditor
• Creditor Account
• Ultimate Creditor
These Related Agents include :
• Instructing Agent
• Instructed Agent
• Debtor Agent
• Creditor Agent
• Intermediary Agent 1
• Intermediary Agent 2
• Intermediary Agent 3
Trading Party is also present in the Related Parties elements, and the following are present in the Related Agents elements: 
Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place. Although these elements are not directly 
associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security 
Settlement, it could be conceivable that these optional CBPR+ element may be populated
Statement Entry Entry Details Transaction Details
Related Agents
Related Parties
618

gpyg py
Statement Entry Entry Details Transaction Details
These are: 
• Local Instrument
• Purpose
• Related Remittance Information
• Remittance Information
• Related Dates such as the Interbank Settlement Date
• Tax
Remittance Information as an end-to-end element should be passed unaltered from Payment Initiation 
(pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account 
Statement (camt) The Remittance Information element is common to these message sets.
For Payment Return (pacs.004) it is also possible to capture Return Information which 
includes:
• The Original Bank Transaction Code of the original Entry
• The Originatorof the return from the pacs.004
• And the Reason code.
619

pypy
as well as have an element to capture Additional Transaction Information.
Statement Entry Entry Details Transaction Details
These are: 
• Related Quantity
• Financial Instrument Identification
• Corporate Action
• Safekeeping Account
• Cash Deposit
• Card Transactions
620

Bank to Customer Statements 
Use Case c.53.1.a – Bank to Customer Statement produced by the Creditor Agent
Use Case c.53.1.b – Bank to Customer Statement produced by the Debtor Agent
Use Case c.53.1.c – Bank to Customer Statement produced by an intermediary Agent
Copy of Bank to Customer Statements 
Use Case c.53.2 – Bank to Customer Statement sent as an additionally copy to an authorised party
Resent Bank to Customer Statements 
Use Case c.53.3 – Bank to Customer Statement resent a previously sent statement/s to the Account Owner
Use Case c.53.4 – Bank to Customer Statement resent a previously sent copy statement/s to an authorised party
Forwarding of Bank to Customer Statements 
Use Case c.53.5 – Bank to Customer Statement sent to an authorised party who forward/provides on to the Account Owner (commonly referred to as 
an account concentrating model) 
Use Case camt.060 for requesting 
a Bank to Customer statement
621
Use Case for copy or duplicate 
reports refer to camt.053 use cases

pacs.008
pacs.008 pacs.008
3 
camt.053
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
2 4
Creditor Agent credits the 
account of the Creditor
5
Creditor Agent as the Account 
Servicer produces and sends a 
statement to either the Account 
Owner, or an authorised third 
party.
6
6
A B C
D
622

pacs.008
pacs.008 pacs.008
3 
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
2 4
Creditor Agent credits the 
account of the Creditor
5
Debtor Agent as the Account 
Servicer produces and sends a 
statement to either the Account 
Owner, or an authorised third 
party.
6
camt.053
6
B C D
A
623

pacs.008
pacs.008 pacs.008
3 
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
2 4
Creditor Agent credits the 
account of the Creditor
5
Intermediary Agent as the 
Account Servicer produces and 
sends a statement to either the 
Account Owner, or an 
authorised third party.
6
camt.053
6
A B C D
624

pacs.008
2
pacs.008 pacs.008
3 
camt.053
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
2 4
Creditor Agent credits the 
account of the Creditor
5
Creditor Agent as the Account Servicer 
produces and sends a statement to the 
Account Owner.
6
camt.053
7
Creditor Agent as the Account Servicer 
sends an additional copy of the 
statement to an authorised third part. 
COPY is populated in the Copy 
Duplicate Indicator element within the 
Bank to Customer Statement message 
(camt.053)
7
A B C
D
625

pacs.008
2
pacs.008 pacs.008
3 
camt.053
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
4
2
Creditor Agent credits the 
account of the Creditor
5
Creditor Agent as the Account 
Servicer produces and sends a 
statement to the Account 
Owner.
6
camt.053
8
Creditor Agent as the Account Servicer 
re-sends a duplicate statement to the 
account owner. DUPL is populated in 
the Copy Duplicate Indicator element 
within the Bank to Customer Statement 
message (camt.053)
8
Creditor as the Account Owner 
requests a previously sent statement 
message/s to be resent to them.
7
A B C
D
626

pacs.008
2
pacs.008 pacs.008
3 
camt.053
Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
4
2
Creditor Agent credits the 
account of the Creditor
5
Creditor Agent as the Account 
Servicer produces and sends a 
statement to an authorised 
third part.
6
6
camt.053 8
Creditor Agent as the Account Servicer 
re-sends a duplicate statement to the 
authorised third party. CODU is 
populated in the Copy Duplicate 
Indicator element within the Bank to 
Customer Statement message 
(camt.053)
8
Authorised third party requests a 
previously sent statement message/s to 
be resent to them.
7
A B C
D
7
627

pacs.008
pacs.008
3
Agent B processes the payment 
on Agent C
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (C) using 
Agents as an intermediary
3
2
Creditor Agent credits the 
account of the Creditor
4
Creditor Agent as the Account 
Servicer produces and sends a 
statement to an authorised 
third part.
5
Authorised third part provides statement 
information to the Account Owner. 
Which could be the forwarded 
Camt.053 statement or the details via 
an alternative channel (e.g. host to host 
file, GUI etc.)
6
camt.053
A B
C
628

Bank to Customer Debit 
Credit Notification
629

camt.054
Group Header
Notification
Notification message is sent by the 
account servicer to an account owner 
or to a party authorised by the account 
owner to receive the message. It can 
be used to inform the account owner, 
or authorised party, of single or multiple 
debit and/or credit entries reported to 
the account
630
The Bank to Customer Debit Credit Notification allows multiple 
Notifications per InterAct message (100,000 bytes) It is however 
recommended to report single notifications per transaction.
This message must be bilaterally agreed between the Account 
Servicing Institution and the Account owner, and is establish by an 
RMA business profile.

Role of the Agent/s, Debtor and Creditor in the payment changes by description in the Bank to Customer Debit Credit 
Notification message to Account Servicer and Account Owner. Whereby the notification is sent by the Account Servicer to 
the Account Owner and or authorised party.
pacs.008
pacs.002
pacs.008
camt.054
camt.054
camt.054
camt.054
A B C
631

account servicing institution and the 
account owner, or authorised (third) 
party. 
These messages: • are used to inform on debit and/or 
credit entries reported to an 
account.
• and may also be complemented 
by:
• a Status Information 
message: • pacs.002 in Payment 
Clearing and 
Settlement, or 
pain.002 in Payment 
Initiation. 
• or by a bank statement such 
as the camt.053 Bank to 
Customer Statement Report
camt.054
pain.002
pain.001
camt.053
camt.054
camt.053
camt.054
camt.053
pacs.002
pacs.008/pacs.009
camt.054
camt.053
632

633

gpg gg,
located in the Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
For Cash Management (camt) messages the Message Identification has no exact equivalent in
the legacy MT Customer Statement message. However the Transaction Reference Number
(Field 20) could be considered a similar comparison.
Group Header Message Identification
634

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
635

the party authorised by the Account Owner to receive the Debit Credit Notification.
This element should only be used to identify the Message Recipient when different from the account 
owner, which is implied by the usage of COPY in the Copy Duplicate Indicator within the nested 
Notification element.
Group Header Message Recipient
Name
Postal Address
Identification
Contact Details
Where Message Recipient is used the nested:
• Name
• Postal Address
• Identification
• Contact Details
May be used to capture information related to this party.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
636

generate a report, for example a camt.060 Account Reporting Request.
Where Original Business Query is used the original Message identification (i.e. the
message identification of the camt.060 message) is required.
Original Message Name identification and Original Creation Date Time may also be
provided.
Min 1 – Max 1
Min 0 – Max 1
Group Header Original Business Query
Message Identification
? Min 0 – Max 1
Message Name Identification
Creation Date Time
637

details related to the account statement.
Group Header Additional Information
Additional Information is a textual element restricted in CBPR+ to 500 
characters.
The camt.054 may be used to indicate a particular type of notification, recognizing 
all transactions within the notification belong to the type indicated below: 
/LBOX/ Lock Box
/BULK/ Bulk reporting (batch transaction with underlying transaction)
/RTRN/ Return report
/CRED/ Notification with Credit entries ONLY
638

639

entry information for an account.
Notification
1
The Notification element has a couple of options to notify on multiple Debits and or
Credits. This can be achieved at either the Notification element itself which could
principally report on more than one account held by the account owner with the
Account Servicer or can be achieved at an Entry level.
Notification of multiple Debits and or Credits is perhaps more associated with a
timed or batch creation of the camt.054 Bank to Customer Debit Credit
Notification. Whereas the more common example of a real-time notification
produced at the point of an account posting would typically notify on a single
Entry.
640

y 
Unique reference assigned by the account servicer to
unambiguously identify the account statement. Directly
comparable with the Transaction Reference Number
(Field 20) of the legacy MT statement message.
Statement Identification
641

pg
Where Notification Pagination is used the Page Number and Last Page indicator
elements are both mandatory.
For example, a Page Number of 2 represents the current account statement, being
the second page of the and implying a previous account statement page had been
sent. The Last Page indicator further implies whether more pages are expected
Min 1 – Max 1
Notification Notification Pagination
Page Number
Last Page indicator
Either Message Pagination (Group Header) or Notification Pagination 
(Notification) may used but not both
Min 1 – Max 1
642

gy 
report sent. 
As a good practice this element allows easy recognition of the notification order, if not
recognisable by other data within the notification, such as the Notification >
Identificationelement.
Should this sequence number be reset by the Account Servicer, this should not occur
more frequently than once a year. Likewise, this 18 digit counter could be incremented to
its maximum value before it’s reset.
1
2
345
The use of Electronic Sequence Number and the sequence reset logic should be
bilaterally agreed been the Account Servicer and the Account Owner
Notification Electronic Sequence Number
643

qg
Sequence Number as a way to identify the statement order, which is not confined to numeric values.
Notification Report Sequence
644
Where used the Reporting Sequence mandate a choice of nested element: 
• From Sequence identifies the start of a sequence range.
• To Sequence identifies the end of a sequence range.
• From To Sequence identifies the start and end of a sequence range.
• Equal Sequence identifies a sequence.
• Not Equal Sequence identifies a sequence to be excluded.
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max *
Min 1 – Max *
Min 1 – Max *
A B
D C
Although the Reporting Sequence may be provided in a camt.060 Account Reporting Request, the
use of this message to request a Bank to Customer Debit Credit Notification is less compelling,
whereby such notifications are typically triggered as the result of an account posting, rather than being
requested.

gy p
sent.
In the case of a real-time notification the Legal Sequence Number element has little
value, unlike its use in a statement message.
Notification Legal Sequence Number
645

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Notification Creation Date Time
646

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
py pp
Where From to Date is used the From Date Time and To Date Time become mandatory elements. 
10
Min 1 – Max 1 Min 1 – Max 1
Notification
From to Date
To Date Time647

y g
COPY
DUPL
CODU
COPY is used when a copy of the notification is sent to an Authorised Third Party, such as
a company head office, parent entity, or an institution providing additional service such as
liquidity sweeping or statement consolidation.
DUPL is used when a duplicate of the notification is sent to the Account Owner, this
resubmission may have been requested using the camt.060 or an alternative channel
such as via internet banking or customer service request.
CODU is used when a duplicate of a notification copy is sent to an Authorised Third Party,
this resubmission may have been requested using the camt.060 or an alternative channel
such as via internet banking or customer service request. It may also be requested by the
Account Owner on behalf of the Authorised Third Party, depending on the arrangement in
place with the Account Servicer.
Notification Copy Duplicate Indicator
648

ypy pp
Reporting Source utilizes the external Reporting Source code list. For example, ACCT
represents a notification based on accounting data, whereas DEPT represents a cash or
deposit system.
Where the source of the notification is functionally required by the consumer of the
notification i.e., the Account Owner or authorised Third Party, the codes used should be
bilaterally agreed.
Notification Reporting Source
649

Account
g y 
nested beneath Account.
Notification Account
a unique Identification for the account, between the
Account Servicer and Account Owner. The element is
further nested by choice of IBAN or Other to capture the
account.
Min 1 – Max 1
Identification
Currency
The Currency for which the account is held. This is
identified using the three characters ISO currency
code.
Min 1 – Max 1
650

An element which may either use an external ISO Cash Account Type code or
a proprietary code. It is used to identifier a particular type of account.
A nest element that contains the Party that legally owns the
account.
Account
py 
Name
The Name of the Account, as Assigned by the servicing
institution.
A nested element which contains a Proxy Identifier
together with the Proxy Type represented by either use an
external ISO Proxy Account Type code or a proprietary
code.
A nested element which identifies the Financial Institution who manages
the account, booking entries, balances etc.
Min 0 – Max 1
Notification Account
Type
Proxy
Owner
Servicer
651

pppgpg 
the notification is produced can identify the parent account they hierarchically relate to.
Notification Related Account
When Related Account is utilized, like Account, the Identification and Currency
element become mandatory.
Additionally, the nested Type element, Name and nested Proxy element are optionally
available.
Min 1 – Max 1 Min 1 – Max 1
Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1
Type
Identification
Currency
Name
Proxy
Related Account uses a variety of common elements described in more detail 
within the Account section.
652

Debit Credit Notification.
Notification Interest
Interest
Reason
An element which may either use an embedded ISO Interest Type code; INDY
(Intraday) OVRN (Over Night) or a proprietary code. It is used to identifier a
particular interest type.
The optional Reason for which interest is applied.
The type of interest Rate defined as a Percentage and in an
Other form. Validity Range optionally defines an Amount, Credit
Debit Indicatorand Currency.
The date range for which interest has been calculated.
From Date Time and To Date Time must be representing
when using this element.
Provides details on any tax applied to the Interest. Where optional
Identification describes the tax levied, additionally with a Rate and or
Amount as necessary.
+
-
Type
Rate
From
To
Date
Tax
653

y y 
Notification is reporting a single Debit or Credit transaction, where understandably the use of Transaction 
Summary provides little value.
Each of the following element allow an optional total of entries either as a Number of
Entries and or as a Sum.
➢ Total Entries
➢ Total Credit Entries
➢ Total Debit Entries
➢ Total EntriesPer Bank Transaction Code
In addition to the Number of Entries and Sum, the Total Entries Per Bank Transaction
Code requires the Bank Transaction Code element and optionally allows a variety of
other optional elements.
The Total Entries Per Bank Transaction Code element is unlimited (Max *) 
whereby more that one Bank Transaction Code may be summarised.
Notification Transaction Summary
Total Credit Entries
Total Entries
Total Debit Entries
Total Entries per Bank 
Transaction Code
Min 0 – Max *
Min 1 – Max 1
654

py
Unlike the legacy MT 900 MT 910 
confirmation messages, the 
camt.054 has a number of 
dedicated elements to capture a 
variety of entry level data. 
It also has an number of 
enhancements on the legacy MT 
confirmation message where 
parties in the payment and 
customer remittance information, 
as examples, can provided to the 
Account Owner. 
Notification Entry
Entry
Reference
Min 0 – Max 1
Amount
Min 1 – Max 1
Credit
Debit
Indicator
Min 1 – Max 1
Reversal
Indicator
Min 0 – Max 1
Status
Min 1 – Max 1
Booking
Date
Min 0 – Max 1
Value
Date
Min 0 – Max 1
Account
Servicer
Reference
Min 0 – Max 1
Availability
Min 0 – Max *
Bank
Transaction
Code
Min 1 – Max 1
Commission
Waiver
Indicator
Min 0 – Max 1
Additional
Information
Indicator
Min 0 – Max 1
Amount
Details
Min 0 – Max 1
Charges
Min 0 – Max 1
Technical
Input
Channel
Min 0 – Max 1
Interest
Min 0 – Max 1
Card
Transactions
Min 0 – Max 1
Entry
Details
Min 0 – Max *
Additional
Statement
Information
Min 0 – Max 1
655

Notification Entry
y
Reference
Mandatory element representing the currency and amount of the entry. This can be compared 
to Field 32A of the legacy MT 900 and MT 910. Amount
Min 1 – Max 1
Mandatory element indicating whether the Amount entry is a DBIT (Debit) or CRDT (Credit) to 
the account.
Credit
Debit
Indicator
Min 1 – Max 1
Indicates whether the entry is a result of a reversal. for example, an entry related to a pacs.004 
Payment Return or reverses an error such as an incorrect value date applied to the entry.
Where the Reversal Indicator is Yes, the Credit Debit Indicator should be the opposite of the 
original entry, for example original Credit Debit Indicator of CRDT would expect a reversal entry 
Credit Debit Indicator of DBIT
Reversal
Indicator
Min 0 – Max 1
656
y
Reference
assign to identify the entry posted to the account.

Notification Entry
Status BOOK is the only status that can be reversed using the Reverse Indicator 
Noting CBPR+ usage guidelines 
mandate the time zone that the 
Date Time represents as an 
offset against Universal Time 
Coordinated (UTC)
used to confirm the entry is booked. Status
Booking Mandatory choice of Date or Date Time the entry was posted to the Account. 
Date
Min 0 – Max 1
Mandatory choice of Date or Date Time the entry 
become available. This can be compared to Field 32A of 
the legacy MT 900 and MT 910.
Value
Date
Min 0 – Max 1
Additional optional Reference typically assigned by the Account Servicer’s payment engine or 
accounting platform. This reference would be used to query an entry.
Account
Servicer
Reference
Min 0 – Max 1
Availability Indicates when the booked amount is available i.e., when it is available to be accessed.
Min 0 – Max *
657

Notification Entry Bank Transaction Code
Transaction
Code
is designed to deliver a 
harmonized set of codes, 
which should be applied in 
bank-to-customer cash account 
reporting information. The bank 
transaction code information 
allows the account servicer to 
correctly report a transaction, 
which in its turn will help 
account owners to perform 
their cash management and 
reconciliation operations. Domain
Family
Sub-Family
Transaction Code has three levels:
Domain: Highest definition 
level to identify the sub-ledger. The domain defines 
the business area of the 
underlying transaction e.g., 
payment, securities etc.)
Family: Medium definition 
level e.g. type of payment; 
credit transfer, direct debit etc.
Sub-family: Lowest definition 
level e.g. type of cheques; 
draft etc. 
Bank Transaction Codes are an 
external code set defined in the Bank 
Transaction Code combinations 
external code sets.
Family
Domain
Sub Family
658

available to download from the ISO20022.org external 
code list page. These include the descriptions for 
Payments Domain Families and sub-families for both 
Received and Issued Credit Transfers. 
https://www.iso20022.org/external_code_list.page
659

All codes in light grey are defined as the generic codes available for all Domains and Families
Domain Family SubFamily Domain Code
ExternalBankTransactionDomain1Code
Family Code
ExternalBankTransactionFamily1Code
SubFamily Code
ExternalBankTransactionSubFamily1Code
Status
Status Date
Payments Issued Credit Transfers Cross-Border Credit Transfer PMNT ICDT XBCT New 27/4/2009
Payments Received Credit 
Transfers
Cross-Border Credit Transfer PMNT RCDT XBCT New 27/4/2009
Bank Transaction Codes are an external code set defined in the Bank Transaction Code combinations external 
code sets.
As an example a debit notification which relates to a cross-border payment initiated from an account would be 
represented by: 
Domain Family Sub-Family
PMNT (Payment) ICDT (Issued Credit Transfer) XBCT (Cross-Border Credit Transfer
660

Notification Entry
not typically associated with Correspondent Banking payments
Optional element indicating whether the underlying transaction details are provided through a 
separate message. Where the Message Name Identification represents the message used to 
provide the additional information and Message Identification specifies the reference of the 
message that provides the additional information. 
Optional nested element which provides various elements to represent an aggregated 
(consolidated) original amount. Where individual transaction amounts can be represented, if 
required, within the Entry Detail set of elements.
This element is useful to capture original amount details where they are different to the Entry, 
Amount, for example the Instructed Amount of the payment can be included, together with a 
potential Currency Exchange rate, where necessary.
Optional nested element to provide information on charges either pre-advised or taken from the 
entry.
Waiver
Indicator
Additional
Information
Indicator
Min 0 – Max 1
Amount
Details
Min 0 – Max 1
Charges
Min 0 – Max 1
661

Notification Entry
used to represent the technical channel used to input the entry. 
Input
Channel
Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry 
amount.
Interest
Min 0 – Max 1
Optional nested element which provides details associated with a card transaction such as the 
card number, card brand etc. 
Card
Transactions
Min 0 – Max 1
Additional optional nested element containing details on the entry. See dedicated section on 
Entry Details.
Entry
Details
Min 0 – Max *
Additional
Statement
Information
Additional optional element to represent further information related to the account 
statement.
Min 0 – Max 1
662

py
Notification Entry Entry Details
Transaction Details
Batch
663
Batch provides details on batched transactions such as the total Number of Transactions 
the batched entry (sometimes referred to as a consolidated entry) represents.
Transaction Details is a significant nested element which represents information on the 
underlying transaction.

y
Transaction Details has a variety of nested elements closely associated with Entry level
elements. The References element however is nested to include a variety of references 
related to the entry including for example the UETR
Notification Entry Entry Details Transaction Details
$
Min 1 – Max 1
Additionally Transaction Details also has a variety of elements capturing details from the underlying 
transaction, which amongst other business transactions includes payment transaction data. For example 
Remittance Information and Related Parties
Reference
Min 1 – Max 1
Amount
Min 1 – Max 1
Credit
Debit
Indicator
Min 1 – Max 1
Amount
Details
Min 0 – Max 1
Availability
Min 0 – Max*
Bank
Transaction
Code
Min 0 – Max 1
Charges
Min 0 – Max 1
Interest
Min 0 – Max 1
664

pyg y (
elements Related Parties/Agents belongs to) relate to a Payment, Clearing and Settlement (pacs) message, 
parties in the pacs messages can be transferred into the Cash Management (camt) message.
These Related Parties include :
• Instructing Party
• Debtor 
• Debtor Account
• Ultimate Debtor
• Creditor
• Creditor Account
• Ultimate Creditor
These Related Agents include :
• Instructing Agent
• Instructed Agent
• Debtor Agent
• Creditor Agent
• Intermediary Agent 1
• Intermediary Agent 2
• Intermediary Agent 3
Trading Party is also present in the Related Parties elements, and the following are present in the Related Agents elements: 
Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place. Although these elements are not directly 
associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security 
Settlement, it could be conceivable that these optional CBPR+ element may be populated
Notification Entry Entry Details Transaction Details
Related Agents
Related Parties
665

ygpyg py
Notification Entry Entry Details Transaction Details
These are: 
• Local Instrument
• Purpose
• Related Remittance Information
• Remittance Information
• Related Dates such as the Interbank Settlement Date
• Tax
Remittance Information as an end-to-end element should be passed unaltered from Payment Initiation 
(pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account 
Statement (camt) The Bank to Customer Debit Credit Notification may also capture this information. The 
Remittance Information element is common to these message sets.
For Payment Return (pacs.004) it is also possible to capture Return Information which 
includes:
• The Original Bank Transaction Code of the original Entry
• The Originatorof the return from the pacs.004
• And the Reason code.
666

p
beyond payments, as well as have an element to capture Additional Transaction Information.
Notification Entry Entry Details Transaction Details
These are: 
• Related Quantity
• Financial Instrument Identification
• Corporate Action
• Safekeeping Account
• Cash Deposit
• Card Transactions
667

Debit/Credit Notification related to a Serial Customer Payments
Use Case c.54.1.1 – Customer Debit/Credit Notification (camt.054) of a Customer Credit Transfer (pacs.008)
Debit/Credit Notification related to a Serial Financial Institution Payments
Use Case c.54.2.1 – Customer Debit/Credit Notification (camt.054) of a FI to FI Credit Transfer (pacs.009)
Debit/Credit Notification related to a Cover Method Payments
Use Case c.54.3.1 – Customer Debit/Credit Notification (camt.054) of a payment using the cover method
668

Agent C processes the payment 
on Agent D
Agent B processes the payment 
on Agent C
pacs.008
camt.054
1
Debtor initiates a payment 
instruction to the Debtor Agent
2a
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (D) using 
Agents B & C as intermediaries
3
4
2b
pacs.008 pacs.008
2 Agent D credits the account of 
the Creditor, providing a credit 
notification using the camt.054
camt.054
3 
5
2b
Agent A provides a debit 
notification to the debtor using the 
camt.054 to confirm their account 
has been debited for the payment 
initiation request. This notification 
may compliment additional status 
information or statement report 
messages
5
A B C D
669

1
1
Agent A as the Debtor initiates 
a payment instruction to the 
Debtor Agent (Agent B)
2a
Debtor Agent (B) debits the 
account of Agent A and 
initiates a serial payment 
towards the Creditor (Agent D) 
using Agents C as an 
intermediary.
2b
pacs.009
2
camt.053
Creditor Agent (C) credits the 
account of Agent D and 
provides a credit notification 
(camt.054) in addition to an 
account statement (camt.053)
camt.054
camt.054
3
Debtor Agent (Agent B) 
provides a debit notification to 
the debtor using the camt.054 
to confirm their account has 
been debited for the payment 
initiation request. This 
notification may be 
complimented by an additional 
status information message. 
But typically will be compliment 
by an end of business day 
statement report messages
2b
B C
670
A
D

Upon receipt of the credit notification 
(camt.054) confirming settlement of the 
covering payment, Agent D may chose 
to process the pacs.008 (if not already 
done so) and apply a credit to the 
Creditor. 
Agent D may also provide a credit 
notification (camt.054) to the Creditor. 
Agent C produces an end of day 
account statement report. An optional 
real time notifications e.g. advice of 
credit may have also been created at 
the time of the credit posting
Agent C receives the payment and 
credits the account of Agent D and 
provides a credit notification (camt.054) 
Agent B processes the payment 
on Agent C
pacs.002
pacs.009.cov
1
Debtor initiates a payment 
instruction to the Debtor Agent
Debtor Agent (A) initiates a 
payment using the cover method 
to the Creditor Agent (D)
2a
2b
2b
In parallel the Debtor Agent (A) 
initiates a coving payment to 
credit the account of Agent (D) 
with their correspondent (Agent 
C)
3a
6
6
3b 4
3a
5
Agent B provides a debit notification 
to Agent A using the camt.054 to 
confirm their account has been 
debited for the payment initiation 
request. This notification may be 
complimented by an additional status 
information message or statement 
report messages
3b
4
A D
B C
Intraday Credit Notification is 
required when using the cover 
method unless an alternative 
mechanism of confirming the 
credit to the pacs.009 cov 
Creditor is agreed e.g. gpi 
Tracker update. 
671

Notification to Receive
672

camt.057
Group Header
Notification
sent by an account owner or by a party 
acting on the account owner's behalf to 
one of the account owner's account 
servicing institutions. It is an advance 
notice that the account servicing 
institution will receive funds to be credited 
to the account of the account owner. The 
NotificationToReceivemessage is used 
to advise the account servicing institution 
of funds that the account owner expects 
to have credited to its account.
The Notification to Receive message is the ISO 20022 equivalent of 
the legacy MT210 Notice to Receive. It can be cancelled using the 
camt.058 where in the meantime the legacy MT 292 can be used to 
request its cancelation.
673

Role of the Creditor Agent and Creditor in the payment changes description in the Notification to Receive message 
(camt.057). The Account Owner is typically the Creditor and the Account Servicer is typically the Creditor Agent. This will 
be followed up with a pacs transferring the funds to the Account Servicer on the expected value date.
674
B A
pacs
camt.057
camt.058

The Parties defined within the Notification to Receive (camt.0057) 
provide advance information to the Account Servicer of information 
included in the payment message. Noting a Debtor must always be 
present in the camt.057 (it is mandatory in the pacs payment 
message) but Debtor Agent may not be provided (Debtor Agent is 
mandatory in the pacs..08 but not he pacs.009)
camt.053
pacs.002
camt.057
A B C
Party pacs camt.057
Debtor
Debtor Agent
Creditor
Creditor Agent Account Servicer
Debtor Agent
Debtor
Account Owner
675
D
pacs
pacs.002
pacs
pacs.002
pacs
D

676

gpg gg,
located in the Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
The Message Identification in the Cash Management (camt) messages is equivalent to field 20
Transaction Reference Number of the MT 210 in the legacy MT Notice to Receive.
Group Header Message Identification
677
Min 1 – Max 1

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
678

message, where the Message Sender is different from the account owner.
Group Header Message Sender
Name
Postal Address
Identification
Contact Details
679
Where MessageSender, Party is used the nested:
• Name
• Postal Address
• Identification
• Contact Details
May be used to capture information related to this party.
Where MessageSender, Agent is used the nested Financial Institution:
• BICFI
• ClearingSystem MemberIdentification
• LEI
May be used to capture information related to thisAgent.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 1 – Max 1
Min 0 – Max 1

680

the account notification such as the related parties, the expected amount to be received and value date 
of the expected receipt.
Notification
1
The Notification nested element Item can contain multiple Credits. Where there is
only one expected credit then only the Item element will contain the Item
Identificationand the Amount.
681
Today the status of a camt.057 has no documented ISO 20022 reporting
process, to theAccount Owner by theAccount Servicer.
Generally, if the Account Servicer does not require notification the message
will be ignored.

Unique reference assigned by the account owner to
unambiguously identify the account notification. There is
no equivalent in the MT210. It is recommended that the
Message Identification is repeated for the Notice to
Receive Identification.
Notification Identification
682

Min 1 – Max 1
683
An element which may either use an external ISO Cash Account
Type code or a proprietary code. It is used to identifier a particular
type of account.
Anested element which contains a Proxy Identifier together with the Proxy
Type represented by either use an external ISO Proxy Account Type code
or a proprietary code.
Account
Currency The Currency for which the account is held. This is identified
using the three characters ISO currency code.
The Name of the Account, as Assigned by the servicing
institution.
Type
Name
Proxy
a unique Identification for the account, between the Account Servicer and
Account Owner. The element is further nested by choice of IBAN or Other to
capture the account.
Identification
Notification Account

the camt.057 Notification to Receive. 
The Account Owner must be identified either by the Party name and postal address or as an Agent using a
Financial Institution identification. The Account Servicer must be identified as an Agent by using the
Financial Institution identification.
Notification
Account Owner
Account Servicer
684
The Account Owner and the Account Servicer are the Creditor and Creditor
Agent respectively in a pacs.008 FI to FI Customer.
Where utilised, it is recommended to use the element at the Item level.

ppgpg 
is produced can identify the parent account they hierarchically relate to.
In the context of a Notification to Receive this element provides little business value.
Notification Related Account
When Related Account is utilized, like Account, the Identification and Currency
element become mandatory.
Additionally, the nested Type element, Name and nested Proxy element are optionally
available.
Min 1 – Max 1 Min 0 – Max 1
Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1
Type
Identification
Currency
Name
Proxy
Related Account uses a variety of common elements described in more detail 
within the Account section.
685

y 
expected receipt. The Notification to Receive can contain multiple items. Expected Value Date is the date on
which the final receiving agent expects to receive the total amount.
Notification Total Amount
TheExpected Value Date takes the format YYYY-MM-DD
686
Notification Expected Date
Min 0 – Max 1
The Total Amount provides a control total where there are multiple credits
recorded within the Item element. The Total Amount element should not be
used where there is a single expected credit.
10
$

describes the Debtor nested Party elements in greater detail. 
Debtor
Identification
Nested element capturing the 
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
address details
687
Notification to Receive Debtor
Party

Debtor nested Agent elements in greater detail. 
Debtor
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
688
Legal entity identifier of the LEI
financial institution.
Notification to Receive Debtor
Agent

of the payment i.e., the Financial Institution servicing an account for the Debtor.
The Debtor Agent and Intermediary Agent elements allow the Treasury function at the
Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time.
Notification
Debtor Agent
Creditor Agent
Min 0 – Max 1
689
The Intermediary Agent element in the camt.057 Notification to Receive capture the
Intermediary agent between the Debtor Agent and the Account Servicer i.e. the Agent from
whom the Creditor Agent expects to receive the payment from.
The Debtor Agent and Intermediary Agent elements allow the Treasury function at the
Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time.
The Debtor Agent and Intermediary Agent elements allow the Account Servicing
Institution’s Treasury department to proactively follow up, as necessary, the actual payment if
it fails to arrive by an expected time.

y qgy 
Notification Item
Type
Identification
Currency
690
The various nested elements within the Item element are very useful in the case where
there are multiple credits. The Creditor Agent will be able to reconcile the incoming
receipts against the list of expected receipts detailed in the Item element and will be
check completeness of all expected receipts and identify any missing receipts.
A single occurrence of Item should be used unless bilaterally agreed.

y qgy 
Only the Identification and 
Amount elements are mandatory. 
Notification Item
Identification
Min 1 – Max 1
UETR
Min 0 – Max 1
Account
Min 0 – Max 1
Account
Owner
Min 0 – Max 1
Account
Servicer
Min 0 – Max 1
Related
Account
Min 0 – Max 1
Amount
Min 1 – Max 1
Expected
Value
Date
Min 0 – Max *
Debtor
Min 0 – Max 1
Debtor
Agent
Min 0 – Max 1
Intermediary
Agent
Min 0 – Max 1
Purpose
Min 0 – Max 1
691
End to End
Identification
Min 0 – Max 1

Notification to Receive multiple receipts
Use Case c.57.1.1 – Notification to Receive (camt.057) followed by Customer Credit Transfers (pacs.008)
Use Case c.57.1.2 – Notification to Receive (camt.057) followed by FI Credit Transfers (pacs.009)
Use Case c.57.1.3 – Notification to Receive (camt.057) where the receipt is settled by the cover method.
Use Case c.57.1.4 – Notification to Receive (camt.057) for a FI Credit Transfers cover (pacs.009 cov).
692

pacs.008
2
2
Debtor initiates a payment 
instruction to the Debtor Agent (A).
Debtor Agent (A) initiates a 
serial payment towards the 
Creditor Agent (C) using 
Agents B as an intermediary.
Agent (B) processes the 
payment on to the Creditor 
Agent (C).
camt.053
pacs.008
Creditor is expecting to receive a 
payment from the Debtor. As the 
Account Owner sends a 
Notification to Receive to Agent 
C as Account Servicer.
A B
693
C camt.057
5
Creditor Agent (C) as Account 
Servicer sends and end of day 
statement to Creditor as 
Account Owner confirming 
accounting entries.
5
3 4
1
1
3
4

pacs.009
Debtor (A) initiates a serial payment 
towards the Creditor Agent (C) using 
Agents (B) as an intermediary.
Agent (B) processes the payment on 
to the Creditor Agent (C).
camt.053
pacs.009
A B
694
C camt.057
Creditor is expecting to receive a 
payment from Debtor. As the 
Account Owner sends a 
Notification to Receive to Agent C 
as Account Servicer.
4
4
Creditor Agent (C) as Account 
Servicer sends and end of day 
statement to Creditor as 
Account Owner confirming 
accounting entries.
1
1 2
2 3
3
4

pacs.009 cov
Debtor Agent (A) initiates a payment using 
the cover method to the Creditor Agent (D)
2a
In parallel the Debtor Agent (A) initiates a covering 
payment to credit the account of Agent (D) who become 
the Creditor of the cover payment (pacs.009 cov). 
Agent A’s role also changes in the cover payment 
where it becomes the Debtor, whereby Agent A’s 
account with their correspondent (Agent B) is debited.
Agent B processes the payment 
on to Agent C
Agent C receives the payment and 
credits the account of Agent D as 
the Creditor, producing an end of 
day account statement report. An 
optional real time notifications e.g. 
advice of credit may have also 
been created at the time of the 
credit posting.
A D
B C
695
1
Debtor initiates a payment 
instruction to the Debtor Agent
Upon receipt of the pacs.008 
advising settlement will occur 
via a cover payment. Agent D 
sends a Notification to 
Receive to Agent C.
2b
2b
3
4
4
5
5
3

pacs.009 cov
Debtor Agent (A) initiates a payment 
using the cover method towards the 
Creditor Agent (D)
2a
In parallel the Debtor Agent (A) 
initiates a covering payment to credit 
the account of Agent (D) who become 
the Creditor of the cover payment 
(pacs.009 cov). 
Agent B processes the cover payment 
on to Agent E
Agent E processes the cover payment on to Agent 
F.
A
D
B
C
696
1
Debtor initiates a payment 
instruction to the Debtor Agent
Agent B also sends a notification to 
receive on behalf of Agent D to notify 
Agent C a credit is expect on their 
account.
2b
2b
3b
3a
4
5
4
3b
E
F
pacs.009 cov
pacs.009 cov 6
3a
Agent F processes the cover payment on to Agent 
C.
5
Agent C receives the cover payment (as the 
Creditor Agent) recognising they have also be 
Notified they would receive this payment (by 
camt.057) They apply value to Agent D.
6

Notification to Receive 
Cancelation Advice
697

camt.058
Group Header
Original 
Notification
Cancellation 
Reason
Advice message is sent by an account 
owner or by a party acting on the account 
owner's behalf to one of the account 
owner's account servicing institutions. It 
is used to advise the account servicing 
institution about the cancellation of a 
notification sent in a previous Notification 
To Receive message.
698

Role of the Creditor Agent and Creditor in the payment changes description in the Notification to Receive message 
(camt.057). The Account Owner is typically the Creditor and the Account Servicer is typically the Creditor Agent. The 
Notification to Receive Cancellation Advice (camt.058) is used to request the cancellation of a previous Notification to 
Receive. 
699
B A
pacs
camt.057
camt.058

700

gpg gg,
located in the Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
The Message Identification in the Cash Management (camt) messages is equivalent to field 20
Transaction Reference Number of the MT 292 in the legacy MT Request for Cancellation.
Group Header Message Identification
701
Min 1 – Max 1

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
702

Party or Agent that is sending the message, where the Message Sender is different from the account
owner.
This element has no equivalent in the legacy MT 292 Request for Cancellation.
Group Header Message Sender
Name
Postal Address
Identification
Contact Details
703
Where MessageSender, Party is used the nested:
• Name
• Postal Address
• Identification
• Contact Details
May be used to capture information related to this party.
Where MessageSender, Agent is used the nested Financial Institution:
• BICFI
• ClearingSystem MemberIdentification
• LEI
May be used to capture information related to thisAgent.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 1 – Max 1
Min 0 – Max 1

704

provide further details on the original camt.057 notification to receive. such as the related parties, the expected 
amount to be received and value date of the expected receipt.
Original Notification
1
The Original Notification nested element enables the ability to reconcile this cancellation advice
against the Notification originally received, so that appropriate action can be take to remove the
advised currency and amount from predicted currency positions at theAccount Servicer.
705
ISO
Group Header
➢ Message Identification
➢ Creation Date Time
Notification
➢ Identification
➢ Debtor
Item
➢ Identification 
➢ End to End Identification
➢ UETR
➢ Amount
➢ Expected Value Date
➢ Debtor
Camt.057 ISO
Camt.058
Original Notification
➢ Original Message Identification
➢ Original Creation Date Time
➢ Original Notification Identification
➢ Original Notification Reference
➢ Debtor
➢ Original Item
➢ Original Item Identification
➢ Original End to End Identification
➢ UETR
➢ Amount
➢ Expected Value Date
➢ Debtor

This 35 character identifier is a point-to-point reference used to unambiguously identify the
Notification to Receive message, capture in its group header.
706
Original Message Identification
Original Notification
y y gg

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
707
g
Original Creation DateTime
Original Notification

y y 
Unique reference assigned by the account owner to
unambiguously identify the original account notification.
Original Notification Identification
708
Original Notification

describes the Debtor nested Party elements in greater detail. 
Debtor
Identification
Nested element capturing the 
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
address details
709
Original Notification Original Notification Reference Debtor
Party Debtor is required either within the Original Notification Reference 
nested element or within the Original Item nested element

Debtor nested Agent elements in greater detail. 
Debtor
Name by which the Agent is Name
known
Postal 
Address
Information used to identify a 
Debtor by a clearing system 
identifier. 
Clearing
System
Member Id
Nested element capturing either 
structured or unstructured Debtor
address details
710
Legal entity identifier of the LEI
financial institution.
Agent
Original Notification Original Notification Reference Debtor Debtor is required either within the Original Notification Reference 
nested element or within the Original Item nested element

The Debtor Agent element in the camt.058 Notification to Receive Cancellation Advice
captures the Debtor Agent provided in the original Notification to Receive (camt.057) i.e., the
Financial Institution servicing an account for the Debtor.
Min 0 – Max 1
711
Original Notification Reference
Debtor Agent may be provided within the Original Notification Original Notification
Reference nested element or within the Original Item nested element.

ggg
The Original Item nested element is repetitive as the original Notification to Receive 
message has the ability to notify on more than one item i.e. currency and amount expect.
The following elements are nested within Original Item, of which Identification and 
Amount are required. 
712
Original Notification Reference
Original Notification
Original Item
Min 1 – Max *
Identification
Min 1 – Max 1
UETR
Min 0 – Max 1
Amount
Min 1 – Max 1
Expected
Value
Date
Min 0 – Max *
End to End
Identification
Min 0 – Max 1
Debtor
Min 0 – Max 1
Debtor
Agent
Min 0 – Max 1
Debtor is required either within the Original Notification Reference 
nested element or within the Original Item Reference nested element.

713

the Originator element helps identify the party who issued the Cancellation request. Typically, this
element would be used to identify the Account Owner as the Originator of the request, where the
Notification to Receive Cancelation Advice message captured a Message Sender acting on the
account owner’s behalf.
the Reason is mandatory and represented by an embedded CBPR+ Cancellation Code choice ( )
The Additional Information element may also be included to provide further details on the
Cancellation reason.
q
Additional Information
Min 1 – Max 1
714
Min 0 – Max 2
Originator
Reason
?
Min 0 – Max 1
Note where Reason code NARR is used additional information must be 
provided to describe the reason for the Cancellation request.
Cancellation Reason

Notification to Receive multiple receipts
Use Case c.58.1.1 – Cancellation Advice for a Notification to Receive (camt.057) expecting a Customer Credit Transfers (pacs.008)
Use Case c.58.1.2 – Cancellation Advice for a Notification to Receive (camt.057) expecting a FI Credit Transfers (pacs.009)
Use Case c.58.1.3 – Cancellation Advice for a Notification to Receive (camt.057) where the receipt is settled by the cover method.
715

Creditor subsequently understand the 
payment should no longer be expected 
for the given amount. They issue a 
cancellation advice to Agent C as 
Account Servicer, providing the reason 
NOLE (not longer expected). 
Creditor is expecting to receive a 
payment from the Debtor. As the 
Account Owner they send a 
Notification to Receive to Agent 
C as Account Servicer.
A B
716
C camt.057
5
2
2
camt.058
1
1

A B
717
C camt.057
Creditor is expecting to receive a 
payment from Debtor. As the 
Account Owner sends a 
Notification to Receive to Agent C 
as Account Servicer.
4
Creditor subsequently understand the 
payment should no longer be expected 
for the given amount. They issue a 
cancellation advice to Agent C as 
Account Servicer, providing the reason 
NOLE (not longer expected). 
2
2
camt.058
1
1

Debtor Agent (A) initiates a payment using 
the cover method to the Creditor Agent (D)
1a
In parallel the Debtor Agent (A) initiates a covering 
payment to credit the account of Agent (D) who become 
the Creditor of the cover payment (pacs.009 cov). 
Agent A’s role also changes in the cover payment 
where it becomes the Debtor, whereby Agent A’s 
account with their correspondent (Agent B) is debited.
Agent B rejects the payment 
advising Agent A
Agent D subsequently issue a 
cancellation advice to Agent C as 
Account Servicer, providing the 
reason NOLE (not longer 
expected). 
A D
B C
718
Upon receipt of the pacs.008 
advising settlement will occur 
via a cover payment. Agent D 
sends a Notification to 
Receive to Agent C.
1b
1b
3
3
5
5
camt.056
Rejected 
+Reason 
4
Agent A send a Request for 
Cancellation to Agent D including 
the reason COVR to confirm the 
cover payment was cancelled.
2
2
4

Account Reporting Request
719

camt.060
Group Header
Reporting Request
account owner, either directly or through a forwarding 
agent, to one of its account servicing institutions. 
It is used to ask the account servicing institution to 
send a report for the account owner's account: 
▪ BankToCustomerAccountReport (camt.052) or
▪ BankToCustomerStatement (camt.053) or 
▪ BankToCustomerDebitCreditNotification 
(camt.054).
Account reports are often configured by the Account Servicing Institution as 
part of a static configuration. The Account Report Request could however be 
used as an alternative mechanism to request reports on a frequent or ad hoc 
basis.
Account Report Request can contain multiple Reporting Request elements as 
the maximum multiplicity is unbounded. This effectively allows multiple 
requests within a single message up to the maximum size limitation of an 
InterAct message (100,000 bytes) It is however recommended only include 
one request per message.
720

Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Report Request 
message to Account Servicer and Account Owner. Whereby the report request is sent by the Account Owner or authorised 
party to the Account Servicer. This message is used to request a report/s of the entries on an account, and/or to provide 
the owner with balance information on the account at a given point in time.
pacs.008
pacs.002
pacs.008
camt.060
camt.060
camt.060
camt.060
A B C
721
camt report
camt report
camt report camt report

722

gpg gg,
located in the Group Header. This 35 character identifier is a point to point reference used to
unambiguously identify the message.
For Cash Management (camt) messages the Message Identification has no exact equivalent in
the legacy MT Customer Statement message. However the Transaction Reference Number
(Field 20) could be considered a similar comparison.
Group Header Message Identification
723

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
724

sending the request.
This element should only be used to identify the Message Sender when different from the account 
owner.
Group Header Message Sender
Party
Agent
Where Message Sender is used, a choice of nested Party or Agent may be used to
identify the Sender.
Party: Agent:
• Name
• Postal Address
• Identification
• Country of Residency
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
725
Take me to the Agent identification

726

Reporting Request
Many Account Servicing Institutions service their Account Owner
customers through statics account configuration/s. Whereby a variety of
reports can be generated on either a time or event bases routine.
The Reporting Request may be used as either an alterative to a static
configuration or to request ad hoc reports (whether that be an additional
report to the statics configuration or to resend reports previous
reported).
727

q
Unique reference assigned by the account owner (or
Message Sender on behalf of the account owner) to
unambiguously identify the account statement. Directly
comparable with the Transaction Reference Number
(Field 20) of the legacy MT request message.
Reporting Request Identification
728

y pg q
This element specifies which type of report is begin
requested. The report is representedby its full name.
For example:
camt.052.001.08 or
camt.053.001.08 or
camt.054.001.08
Reporting Request
729
Requested Message Name Identification

q
element is mandatory.
Reporting Request Account
730
a unique Identification for the account, between the
Account Servicer and Account Owner. The element is
further nested by choice of IBAN or Other to capture the
account.
Min 1 – Max 1

An element which may either use an external ISO Cash Account Type code or
a proprietary code. It is used to identifier a particular type of account.
Anested element which contains a Proxy Identifier together with
the Proxy Type represented by either use an external ISO Proxy
Account Type code or a proprietary code.
Account
y q
Currency
The Currency for which the account is held. This is identified
using the three characters ISO currency code.
The Name of the Account, as Assigned by the servicing
institution.
Type
Name
Proxy
731
Reporting Request Account

pq
Reporting Request Account Owner
732
Where Account Owner is used, a choice of nested Party or Agent may be used to
identify the owner.
Party: Agent:
• Name
• Postal Address
• Identification
• Country of Residency
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Take me to the Agent identification
Typically the Account Name (see the previous page) represents the Account Owner’s Name in accordance 
with standard Know Your Customer (KYC). The mandatory Account Owner elements enables more detail to 
be captured such as an address for a Party or a BIC for an Agent.

gg g ypyg
Reporting Request is sent to, who is also identified in the Business Application Header.
Reporting Request Account Servicer
733
Take me to the Agent identification
Financial InstitutionIdentification:
• BICFI
• Clearing System MemberIdentification
• LEI
• Name
• Postal Address

qpy py 
From to Time element.
Reporting Request Report Period
From to Date captures a mandatory From Date and an optional To Date. It allows the 
request to specify the date period for which the report is being requested. 
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
10
Min 1 – Max 1
Min 0 – Max 1
From to Date
To Date Time
734

qpg qqp
the Account Servicing Institution uses this element within the reports they provide.
Report Request Report Sequence
735
Where used the Reporting Sequence mandate a choice of nested element: 
• From Sequence identifies the start of a sequence range.
• To Sequence identifies the end of a sequence range.
• From To Sequence identifies the start and end of a sequence range.
• Equal Sequence identifies a sequence.
• Not Equal Sequence identifies a sequence to be excluded.
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max *
Min 1 – Max *
Min 1 – Max *
A B
D C

pypqp
Reporting Request Requested Transaction Typ
736
Where used the Status element and Credit Debit Indicator elements are mandatory.
• Status is a nested element which may either use a choice of external ISO Entry Status 
code or a proprietary code. It is used to indicate the transaction entry status for which 
the requested reported should reflect.
• Credit Debit Indicator is a choice of embedded code to indicate whether Debit or 
Credit transaction entries should be reported.
An optional Floor Limit element may also be used. This element requests a minimum 
value, for which transaction entries above this value should be reported. 
Where used the Amount and Credit Debit Indicator elements are mandatory.
Min 1 – Max 1 Min 1 – Max 1
Min 0 – Max 1
As a request for specific transaction type/s to be reported, typically this request would relate to a camt.052 
Bank to Customer Account Report where the specified balance information is an intraday report. The use of 
the camt.060 Account Reporting Request and the ability to specify specific reporting requirements in the 
request is dependent on the Account Servicing Institution and should bilaterally agreed by Account Owner 
with them.

pypqp
Reporting Request Requested Balance Type
737
Where used a choice of balance Code is mandatory which may either use a choice of 
external ISO Balance Type code or a proprietary code. 
An optional Sub Type element may also be used which a choice of external ISO Balance 
Sub Type code or a proprietary code. 
Min 1 – Max 1
Min 0 – Max 1
As a request for specific balance type/s (or sub balance type/s) to be reported, typically this request would 
relate to a camt.052 Bank to Customer Account Report where the specified balance information is an intraday 
report. The use of the camt.060 Account Reporting Request and the ability to specify specific reporting 
requirements in the request is dependent on the Account Servicing Institution and should bilaterally agreed by 
Account Owner with them.

Financial Institution Account Reporting Request 
Use Case c.60.1.1 – High Level Financial Institution daily Account Reporting Request 
Use Case c.60.1.2 – Financial Institution interim Account Reporting Request 
738

Agent C credits the account of the 
Creditor (Agent D)
1
Debtor initiates a payment 
instruction to the Debtor Agent
2
Agent B processes the payment 
on Agent C, via the Payment 
Market Infrastructure.
3
Payment Market Infrastructure, 
settles the payment between 
Agent B and Agent C as direct 
participants of the Market 
Infrastructure, and provides a 
settlement confirmation to Agent B
pacs.009
camt.053
pacs.009
pacs.002
2 3
Settlement 
Complete
4
4
1
pacs.002 A B C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their 
own usage guidelines based on the ISO 20022 standard.
739
camt.060
Agent D requests a daily statement 
using a camt.060 (not having an 
automatic statement produced by 
their account servicing institution
5
Agent C produces a customer
statement (camt.053) following the 
request from Agent D
5

Agent C credits the account of the 
Creditor (Agent D)
1
Debtor initiates a payment 
instruction to the Debtor Agent
2
Agent B processes the payment 
on Agent C, via the Payment 
Market Infrastructure.
3
Payment Market Infrastructure, 
settles the payment between 
Agent B and Agent C as direct 
participants of the Market 
Infrastructure, and provides a 
settlement confirmation to Agent B
pacs.009
camt.053
pacs.009
pacs.002
2 3
Settlement 
Complete
4
4
1
pacs.002 A B C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their 
own usage guidelines based on the ISO 20022 standard.
740
camt.060
Agent D requests an interim 
statement using a camt.060 (not 
having an automatic interim statement 
produced by their account servicing 
institution
5
Agent C produces a customer statement 
(camt.052) following the request from 
Agent D
5
camt.052

() g
741

camt.055 – Customer Payment Cancellation Request
camt.056 – FI to FI Payment Cancellation Request
742

Resolution of 
Investigation
743

camt.029
Assignement
Status
Cancellation 
Details
Agent to respond to the Cancellation Request, either 
directly or serially through other agents.
The message is used to provide: 
▪ final outcome of the case, whether positive or 
negative, or
▪ an interim update prior to the final outcome.
744
Following a positive acceptance of the Cancellation 
request. The appropriate payment message 
(pacs.002 or pacs.004) is used to reject or return a 
previously received payment.

The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide 
a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any 
payment previous settled is necessary to trigger reversing account postings.
pacs.008
pacs.002 pacs.008
camt.056
camt.029
A B C
745
camt.055
camt.056
camt.029
camt.053

The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide 
a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any 
payment previous settled is necessary to trigger reversing account postings.
pacs.008
pacs.002 pacs.008
camt.056
A B C
746
camt.055
camt.029
camt.053

747
element description example element description example
Assigner Sender of the camt.056 Agent B Assigner Sender of the camt.029 Agent C
Assignee Receiver of the camt.056 Agent C Assignee Receiver of the camt.029 Agent B
Assignment 
Identification
Unique Id generated by the assigner 
to identify the Payment Cancellation 
Request message
CASE123/1 Assignment 
Identification
Unique Id generated by the assigner 
to identify the Resolution of 
Investigation message
STAT789/1
Cancellation 
identification
Optional Cancellation Id of the Agent 
sending (assigner) the Payment 
Cancellation Request message.
CASE123 Cancellation 
Status 
Identification
Case Reference of the Agent 
sending (assigner) the Resolution of 
Investigation message.
STAT789
Case 
Identification
Case Id of the Agent sending 
(assigner) the Payment Cancellation 
Request message.
CASE123 Resolved 
(Original) Case 
Identification
Case Id of the original case the 
Resolution of Investigation is 
responding to.
CASE123
Case 
Creator
Party w ho created the original 
cancellation request (w hich may be 
another Agent other than the current 
Assigner. 
Agent A Case Creator Party w ho created the original 
cancellation request (w hich is the 
same original case creator in the 
Payment Cancellation Request)
Agent A
Cancellation
Reason…
Originator
Party w ho provide the original 
Payment Cancellation Request 
(w hich may be another Party other 
than the current Assigner. 
Customer X Cancellation 
Status…
Originator
Party w ho provide the original
Cancellation response (w hich may 
be another Party other than the 
current Assigner. 
Customer Y
ISO camt.029 Resolution of Investigation 
Camt.056 Payment Cancellation Request ISO
CASE123
STAT789
Customer X Customer Y
my payment 
please
OK, I can 
understand the 
mistake.
CASEABC
STATYXZ
CASE545
STAT54X

748

q
Unique reference assigned by the assigner to
unambiguously identify the Cancellation request.
For Exceptions and Investigations messages the
Identification has no exact equivalent in the legacy MT
Exceptions and Investigations message. However, the
Transaction Reference Number (Field 20) could be
considered a similar comparison.
Directly comparable with the Transaction Reference
Number (Field 20) of the legacy MT statement message.
Assignment Identification
749

pacs.008
pacs.008
Assignee 
Agent: Agent A
Assigner
Agent: Agent B
Assignee
Agent: Agent B
Assigner
Agent: Agent C
Assigner and Assignee represent the 
Agents involved in the point-to-point 
investigation message exchange. These 
roles therefore change on each message 
leg.
A B C D
Assignment
Assigner
Assignee
750
camt.056
camt.056
camt.029
camt.029

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
751

752

yqg
The Confirmationelement includes a choice of three embedded confirmation codes:
• CNCL – The payment has been cancelled as requested. This status concludes the
investigation, whereby aPayment Return may follow if funds need to be returned.
• PDCR – The Investigation of the Payment Cancellation Request is pending i.e. is
under ongoing investigation to provide a final status confirmation. An addition
Cancellation Status Reason Information should be provided to further clarify the
current status. For example, a Status Reason code RQDA can be used to indicate
debit authority has been requested from the Creditor.
• RJCR – The Payment Cancellation Request is rejected. A status concluding the
investigation which must include additional Cancellation Status Reason
Information to provide an explanation as to why the request was rejected.
753
Assignment Status
Confirmation
X
?
✓

754

pgpyp
Payment Cancellation Request’s investigation.
As part of this nested element, information is captured to reference; the case the
investigation is attempting to resolve, various original references related to the original
payment and the investigation status information.
755
Cancellation Details Transaction Information and Status

756
Cancellation Details Transaction Information and Status
y p
Unique reference assigned by the resolution assigner to unambiguously
identify the Cancellation status.
For Exceptions and Investigations messages the Cancellation Status
Identification can be considered an equivalent in the legacy MT Directly
comparable with the Transaction Reference Number (Field 20) of the
legacy MT statement message.
Cancellation Identification
!

The Identification element captures the unique case reference assigned by the
Payment Cancellation Request Assigner to unambiguously identify the Cancellation
investigation case being resolved.
For Exceptions and Investigations messages this Case Identification can be
considered an equivalent of the Related Reference (Field 21) of the legacy MT
Answer message.
757
id
Min 1 – Max 1
The Creator element captures the party who created the Payment Cancellation
Request investigation (see camt.056 Case Creator).
This mandatory party can represent as either an Agent i.e., the Bank who created
the case or as a Party i.e., the customer (for example the Debtor) who created the
request. This element has no equivalent in the legacy MT Request for Cancellation
message.
Min 1 – Max 1
Cancellation Details Transaction Information and Status
Resolved Case
X
✓

Original Group Information
Original Message Identification contains the point-to-point reference from this payment, and the
mandatory Original Message Name Identification contains the message name of the underlying payment.
Optionally the Original Creation Date Time can also be captured.
Note: the xx in the CBPR+ Usage Guideline 
represents the message version of the message 
received for example pacs.008.001.08 
camt.029
A B For example:
Original Message Name Identification “pacs.008.001.08” confirms the
investigation relates to a pacs.008 Financial Institution to Financial
Institution Customer Credit Transfer. Where as “pacs.009.001.08”
confirms the investigation relates to a pacs.009 Financial Institution
Credit Transfer.
Message 
Identification abcd1234
pacs.008.001.08 Original Message 
Name Identification
Original Message 
Identification abcd1234
Identification xyz9875
Original 
Group
Information 
Assignment
pacs.008
758
Cancellatio
n Details
Cancellation Details Transaction Information and Status
camt.056

The following element (in addition to Original Message identification and Original Message
Name Identification described on the previous page) are optional:
Original End to End Identification
Original Instruction Identification
Original Transaction Identification
Original Clearing System Reference
The Original elements enables the Assignee to identify the Payment which is being request
to be cancelled. The following element (in addition to Original Message identification and
Original Message Name Identification described on the previous page) are mandated:
Original UETR
pyg pyq
Original Instruction Identification
Original End to End Identification
Original UETR
Original Transaction 
Min 1 – Max 1
Min 0 – Max 1
759
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Original Clearing System Reference
Cancellation Details Transaction Information and Status
Original Group Information

the Originator element helps identify the party who provided the Cancellation status. This party
would have been included in the underlying payment and is also included the pacs.004 Return
Chain.
the Reason for the Cancellation status, which is mandatory where the Resolution Status is RJCR, is
represented by an embedded CBPR+ Cancellation Code choice ( )
the Additional Information element may also be included to provide further details on the
Cancellation reason.
Additional Information
Min 0 – Max 1
760
Min 0 – Max 1
Originator
Reason
?
Min 0 – Max 1
Note where Reason code NARR is used additional information must be 
provided to describe the reason for the Cancellation request.
Cancellation Details Transaction Information and Status
In the event that an indemnity agreement is need to be established, Original Group Information
INDM should be indicated at the beginning of the Additional
Information element. Any subsequent additional information may then
be included.

Cancellation message, which can be broadened afterthe coexistence period.
761
Code Name Definition Use Case
AC04 Closed Account 
Number
Account number specified has been 
closed on the receiver’s books.
Complimenting a Reject Status. Payment Cancellation Request can not be 
accepted as the Creditor has since closed their account.
AGNT Agent Decision Reported when the cancellation 
cannot be accepted because of an 
agent refuses to cancel.
Complimenting a Reject Status. Payment Cancellation Request can not be 
accepted as an Agent in the payment transaction does not accept the 
request.
AM04 Insufficient Funds Amount of funds available to cover 
specified message amount is 
insufficient.
Complimenting a Reject Status. Payment Cancellation Request can not be 
accepted as the Creditor has insufficient funds to perform the return payment.
ARDT Already Returned Cancellation not accepted as the 
transaction has already been returned.
Complimenting a Reject Status. Payment Cancellation Request can not be 
accepted as the payment has already return payment.
CUST Customer Decision Reported when the cancellation 
cannot be accepted because of a 
customer decision (Creditor).
Complimenting a Reject Status. Payment Cancellation Request can not be 
accepted as the Creditor does not provide authority to return the payment. i.e. 
believe the payment was justified. 
INDM Indemnity Request Indemnity is required before funds can 
be returned
Complimenting a Pending or Reject Status. Payment Cancellation Request 
can not be accepted until an indemnity agreement is established.

762
NAAR Narrative Reason is provided as narrative information in the 
additional reason information.
Complimenting a Reject or Pending Status to provide further 
narrative Additional Information. 
NOAS No Answer From 
Customer
No response from beneficiary (to the cancellation 
request).
Complimenting a Reject Status. Payment Cancellation Request 
can not be accepted as the Creditor has not responded to a 
Debit Authority request to return the payment.
NOOR No Original 
Transaction 
Received
Original transaction (subject to cancellation) never 
received.
Complimenting a Reject Status. Payment Cancellation Request 
can not be accepted as it is believed that the original payment 
was never received for the UETR and references provided.
PTNA Passed To The 
Next Agent
Reported when the cancellation request cannot be 
accepted because the payment instruction has been 
passed to the next agent.
Complimenting a Pending Status. Payment has been onward 
processed to the next agent in the transaction. The Payment 
Cancellation Request has therefore been forward to this Agent,
a further resolution message will be sent once this Agent 
provides a response.
RQDA Requesting Debit 
Authority
Reported when authority is required by the Creditor to 
return the payment.
Complimenting a Pending Status. Payment has been credited 
to the creditor, Authority to Debit the Creditor and return the 
payment is being request. A further resolution message will be 
sent once the Creditor provides a response.

Resolution of Investigation
Use Case c.29.1.1 – High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008)
Use Case c.29.1.1.a – High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008) using gpi Stop and Recall
Use Case c.29.1.2 – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008)
Use Case c.29.1.2.a – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall
Use Case c.29.2.1 – High Level Resolution of Investigation (camt.029) of a complete Customer Credit Transfers (pacs.008) settled using the cover method
Use Case c.29.2.2 – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method
Use Case c.29.2.3 – High Level Resolution of Investigation (camt.029) of a Customer Credit Transfers (pacs.008) where the cover is returned
Use Case c.29.3.1 – High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer (pacs.009)
Use Case c.29.4.1 – High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer advice (pacs.009 adv)
763

pacs.008
Agent D provides a final 
outcome of the investigation to 
Agent C using the camt.029.
Debtor Agent (B) updates their case 
history and relays the outcome of the 
investigation to Agent A using the 
camt.029
Debtor Agent (A) updates their case 
history and informs the customer of 
the outcome of the investigation.
pacs.008 pacs.008 pacs.008
A C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
764
1
3 2
4
camt.056 camt.056 camt.056
camt.029 camt.029 camt.029
B
1
Debtor Agent (C) updates their 
case history and relays the 
outcome of the investigation to 
Agent B using the camt.029
2
3
4
See use case p.8.1.1 for the original payment,
c.56.1.1 for case resolution and p.4.1.3. for an 
example payment return

pacs.008
Agent D provides an update on
the investigation to the gpi
Tracker using the camt.029.
Debtor Agent (A) updates their case 
history and informs the customer of the 
outcome of the investigation. 
pacs.008 pacs.008 pacs.008
A C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
765
3
camt.029
B
1
gpi Tracker forwards the 
response to Agent A as the 
initiator of the original camt.056
2
3
See use case p.8.1.1 for the original payment,
c.29.1.1 for case resolution and p.4.1.3. for an 
example payment return
camt.029

pacs.008
Debtor Agent (B) updates their 
case history and relays the 
outcome of the investigation to 
Agent A using the camt.029
Debtor Agent (A) updates their case 
history and informs the customer of 
the outcome of the investigation.
pacs.008 pacs.008
A C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
766
1
2 1
3
camt.056 camt.056
camt.029 camt.029
B
Agent C provides a final 
outcome of the investigation to 
Agent B using the camt.029
1
2
3
See use case p.8.1.1 for the original payment,
c.56.1.2 for case resolution and p.4.1.3. for an 
example payment return

pacs.008 pacs.008 pacs.008
A C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
767
3
1
camt.029
B
camt.029
Agent C provides an update on
the investigation to the gpi
Tracker using the camt.029.
Debtor Agent (A) updates their case 
history and informs the customer of the 
outcome of the investigation. 
1
gpi Tracker forwards the 
response to Agent A as the 
initiator of the original camt.056
2
3

pacs.008
pacs.002
pacs.009 cov pacs.009 cov
Settlement 
Complete
A pacs.002 D
B C
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
768
2 camt.056
camt.029
1
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
1
Debtor Agent (A) assigns a 
Cancellation Request to Agent 
D (assignee) requesting the 
original pacs.008 is returned, 
using reason code AM09.
2
3
Agent D creates an investigation case. Recognising the 
payment has already been credited to the creditor. They request 
debit authority, proving the reason specified for the return 
request and update Agent A. 
Once the outcome to the debit authorisation is know a final 
resolution to the investigation can be relayed and any necessary 
return payment can be initiated.
3
See use case p.8.2.1 for the original payment,
c.56.2.1 for case resolution and p.4.3.2 for an 
example payment return

pacs.008
pacs.002
pacs.009 cov pacs.009 cov
Settlement 
Complete
A D
B C
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
769
2 camt.056
1 camt.029
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
1
Debtor Agent (A) assigns a 
Cancellation Request to Agent 
D (assignee) requesting the 
original pacs.008 is returned, 
using reason code AM09.
2
3
Agent D creates an investigation case. Recognising the 
payment has not been credited to the creditor. They update 
Agent A that the Cancellation Request is accepted and arrange 
the necessary return payment once the pacs.009 cov settlement 
is confirmed by Agent C
3
See use case p.8.2.1 for the original payment,
c.29.2.1 for case resolution and p.4.3.2 for an 
example payment return

pacs.002
pacs.009 cov
+ Reject 
Reason 
+ Return 
Reason 
1 camt.056
Agent C receives the payment and 
recognises the payment can not be 
completed as requested e.g. the Agent D 
does not maintain an account with them. 
A
B C
D
770
camt.029
Debtor Agent (A) assigns a 
Cancellation Request to Agent D 
(assignee) requesting the original 
pacs.008 is considered null and 
void, using reason code COVR.
1 Agent D creates an investigation case. Recognising the 
cover payment will not be received to settle the pacs.008. 
As the creditor has not been credited in advance of cover 
settlement, a final resolution to the investigation can be 
provided. A payment return is not necessary. 
2
2
See use case p.8.2.1 for an example of a cover 
payment c.56.2.1 for case resolution and p.4.3.3for 
payment return

pacs.009 camt.053 pacs.009
A pacs.002 pacs.002 B C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their 
own usage guidelines based on the ISO 20022 standard.
camt.054
771
See use case p.9.1.1 for the cover payment sample
c.56.3.1 for case resolution and p.4.2.3 for payment 
return
camt.056 camt.056
camt.029 2 camt.029 1
Agent C provides a final 
outcome of the investigation to 
Agent B using the camt.029.
1
Debtor Agent (B) updates their case 
history and informs the customer 
(Agent A) of the outcome of the 
investigation.
2
pacs.009

pacs.009
pacs.002
B E
C D
A F
772
See use case p.9.1.2 for the cover payment sample
c.56.4.1 for case resolution and p.4.2.3 for payment 
return
2 camt.056
1 camt.029
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
1
Debtor Agent (A) assigns a 
Cancellation Request to Agent 
E (assignee) requesting the 
original pacs.008 is returned, 
using reason code AM09.
2
3
Agent E creates an investigation case. Recognising the payment 
has already been credited to the creditor. They request debit 
authority, proving the reason specified for the return request and 
update Agent B. 
Once the outcome to the debit authorisation is know a final 
resolution to the investigation can be relayed and any necessary 
return payment can be initiated.
3

Customer Payment
Cancellation Request
773

camt.055
Assignment
Underlying
message is sent by an Agent to request the 
Cancellation of a payment initiation request previous 
sent.
The message is sent either: 
• directly to the Agent a previous Payment initiation 
request was sent to. 
774

Interbank pain.001
Interbank pain.002 pacs.008
pacs.002
F
A
B
camt.053
Debtor Debtor Agent Creditor Agent Creditor Forwarding
Agent Initiating Party
pain.001
pain.002
camt.055
camt.029
camt.055
camt.029 camt.056
camt.029
The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This 
message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The 
CustomerPaymentCancellationRequestmessage is issued by the initiating party to request the cancellation of an initiation 
payment message previously sent.

Interbank pain.001
Interbank pain.002 pacs.008
pacs.002
I A B
camt.053
Debtor Agent Initiating
Party
Debtor Creditor Agent Creditor
camt.055
camt.029 camt.056
camt.029
The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This 
message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The 
CustomerPaymentCancellationRequestmessage is issued by the initiating party to request the cancellation of an initiation 
payment message previously sent.

Interbank pain.001
pacs.008
Interbank pain.002
pacs.002
A B C
camt.053
Debtor Creditor Agent Creditor Initiating Party
I
pacs.008
pacs.002
Debtor Agent
camt.055
camt.029
camt.056
camt.029
camt.056
camt.029
The CustomerPaymentCancellationRequestmessage is sent by a case creator/case assigner to a case assignee. This 
message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The 
CustomerPaymentCancellationRequestmessage is issued by the initiating party to request the cancellation of an initiation 
payment message previously sent.

778
element description example element description example
Assigner Sender of the camt.055 Agent A Assigner Sender of the camt.029 Agent 
Assignee Receiver of the camt.055 Agent B Assignee Receiver of the camt.029 Agent A
Assignment 
Identification
Unique Id generated by the assigner 
to identify the Payment Cancellation 
Request message
CASE123/1 Assignment 
Identification
Unique Id generated by the assigner 
to identify the Resolution of 
Investigation message
STAT789/1
Cancellation 
identification
Optional Cancellation Id of the Agent 
sending (assigner) the Payment 
Cancellation Request message.
CASE123 Cancellation 
Status 
Identification
Case Reference of the Agent 
sending (assigner) the Resolution of 
Investigation message.
STAT789
Case 
Identification
Case Id of the Agent sending 
(assigner) the Payment Cancellation 
Request message.
CASE123 Resolved 
(Original) Case 
Identification
Case Id of the original case the 
Resolution of Investigation is 
responding to.
CASE123
Case 
Creator
Party w ho created the original 
cancellation request (w hich may be 
another Agent other than the current 
Assigner. 
Agent A Case Creator Party w ho created the original 
cancellation request (w hich is the 
same original case creator in the 
Payment Cancellation Request)
Agent A
Cancellation
Reason…
Originator
Party w ho provide the original 
Payment Cancellation Request 
(w hich may be another Party other 
than the current Assigner. 
Customer X Cancellation 
Status…
Originator
Party w ho provide the original
Cancellation response (w hich may 
be another Party other than the 
current Assigner. 
Customer Y
ISO camt.029 Resolution of Investigation 
Camt.055 Payment Cancellation Request ISO
CASE123
STAT789
Customer X Customer Y
my payment 
please
OK, I can 
understand the 
mistake.
CASE545
STAT54X

779

q
Unique reference assigned by the assigner to
unambiguously identify the Cancellation request.
For Exceptions and Investigations messages the
Identification has no exact equivalent in the legacy MT
Exceptions and Investigations message. However, the
Transaction Reference Number (Field 20) could be
considered a similar comparison.
Directly comparable with the Transaction Reference
Number (Field 20) of the legacy MT statement message.
Assignment Identification
780

pain.001
pacs.008 Assigner and Assignee represent the 
Agents involved in the point-to-point 
investigation message exchange. These 
roles therefore change on each message 
leg.
A B C D
Assignment
Assigner
Assignee
781
camt.055
camt.056
camt.029
camt.029
Assignee
Agent: Agent B
Assignee
Agent: Agent C
Assigner
Agent: Agent B
Assigner 
Agent: Agent A

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
782

783

y y gyq
This Unique reference identifies the Payment Information Identification from
the originalPayment Initiation request.
Refer to the relevant Payment Information Identification element in the
original message for details on that reference.
Link to Pain.001
Link to Pain.008
Original Payment Information Identification
784
Underlying Original Payment Information and Cancellation
camt.055
A B
Message 
Identification abcd1234
pain.001.001.09 Original Message 
Name Identification
Original Message 
Identification abcd1234
Identification xyz9875
Original 
Group
Information 
Assignment
pain.001
Underlying
Original Payment Infomation
Identification
Payment Information
Identification abcd1234
abcd1234

Original Group Information
requested. The mandatory Original Message Identification contains the point-to-point reference from this
payment, and the mandatory Original Message Name Identification contains the message name of the
underlying payment. Optionally the Original Creation Date Time can also be captured.
Note: the xx in the CBPR+ Usage Guideline 
represents the message version of the message 
received for example pacs.008.001.08 
For example:
Original Message Name Identification “pain.001.001.09” confirms the
Cancellation request is for a pain.001 Interbank Customer Credit
Transfer Initiation.
Underlying Original Payment Information and Cancellation 785
camt.055
A B
Message 
Identification abcd1234
pain.001.001.09 Original Message 
Name Identification
Original Message 
Identification abcd1234
Identification xyz9875
Original 
Group
Information 
Assignment
pain.001
Underlying
Original Payment Infomation
Identification
Payment Information
Identification abcd1234
abcd1234

y q
Unique reference assigned by the assigner to unambiguously identify the
Cancellation request.
For Exceptions and Investigations messages the Cancellation Identification
can be considered an equivalent in the legacy MT Directly comparable with
the Transaction Reference Number (Field 20) of the legacy MT statement
message.
Transaction Identification Cancellation Identification
786
!
Underlying Original Payment Information and Cancellation

The Identification element captures a unique case reference assigned by the
assigner to unambiguously identify the Cancellation investigation case.
For Exceptions and Investigations messages the Case Identification can be
considered an equivalent of the Transaction Reference Number (Field 20) of the
legacy MT Request for Cancellation message.
787
Transaction Identification Case
id
Min 1 – Max 1
The Creator element captures the party who created the investigation. This
mandatory party can represent as either an Agent i.e., the Bank who created the
case or as a Party i.e., the customer (for example the Debtor) who created the
request. In CBPR+ the creatoris always expected to be an Agent.
This element has no equivalent in the legacy MT Request for Cancellation message.
Min 1 – Max 1
Underlying Original Payment Information and Cancellation

One of the following elements is also required depending on the Date element in the original
message, where Original Request Execution Date relates to the pain.001 and Original Request
Collection Date relates to the pain.008 :
Original Requested Execution Date
Original Request Collection Date
The Original elements enables the Assignee to identify the Payment which is being request
to be cancelled. The following element (in addition to Original Message identification and
Original Message Name Identification) are mandated:
Original End to End Identification
Original UETR
Original Instructed Amount
pyg pyq
Original Instruction Identification
Original End to End Identification
Original UETR
Min 1 – Max 1
Min 0 – Max 1
Min 1 – Max 1
788
Transaction Information
Min 1 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Original Requested Collection Date
Original Requested Execution Date
Underlying Original Payment Information and Cancellation
Original Instructed Amount The following element is optional:
Original Instruction Identification

the Originator element helps identify the party who request the payment Cancellation. This party
would have been included in the underlying payment and is also included the pacs.004 Return
Chain as the Creditor.
the Reason is mandatory and represented by an embedded CBPR+ Cancellation Code choice ( )
the Additional Information element may also be included to provide further details on the
Cancellation reason.
q
Additional Information
Min 1 – Max 1
789
Transaction Information Cancellation Reason Info’ 
Min 0 – Max 2
Originator
Reason
?
Min 0 – Max 1
Note where Reason code NARR is used additional information must be 
provided to describe the reason for the Cancellation request.
Underlying Original Payment Information and Cancellation

Cancellation message, which can be broadened afterthe coexistence period.
790
Code Name Definition Use Case
AGNT Incorrect Agent Agent in the payment workflow is 
incorrect.
A payment previous executed is identified as containing an incorrect 
correspondent (Agent) within the payment flow. A Cancellation request is 
generated so that the payment can be remediated following the successful 
return.
AM09 Wrong Amount Amount is not the amount agreed or 
expected.
The customer (Debtor) requests the initiation of a payment from their bank 
account, but subsequently realizes they had provided an incorrect amount.
CURR Incorrect 
Currency
Currency of the payment is incorrect. The customer (Debtor) requests the initiation of a payment from their bank 
account, but subsequently realizes they requested the wrong currency, as the 
payment has been executed. They request their bank to recall
the funds so that the payment can be re-executed in the correct currency
CUST Requested By 
Customer
Cancellation requested by the Debtor. The customer (Debtor) requests the initiation of a payment from their bank 
account, but subsequently wishes to recall the payment. The exactly 
underlying reason for the customer request is either not specified by the
customer or is not aligned to a more specific reason and therefore is not 
appropriate.

791
CUTA Cancel Upon 
Unable To Apply
Cancellation requested because an investigation 
request has been received and no remediation is 
possible.
An error occurred in the original payment (such as incorrect 
information) which was highlighted as part of an Investigation 
query. The request to cancel complements a response to the 
Investigation. 
DUPL Duplicate 
Payment
Payment is a duplicate of another payment. A customer (Debtor) requests the initiation of a payment from 
their bank account, but subsequently initiates
a new (separate) payment request in duplication of a previous 
payment. Having realized the error, the customer requests the 
recall of the duplicate transaction.
FRAD Fraudulent Origin Cancellation requested following a transaction that was 
originated fraudulently. The use of the Fraudulent 
Origin code should be governed by jurisdictions.
Either the customer (Debtor) or a bank (Agent) in the payment 
transaction experiences an activity which causes a payment to 
be executed by alleged fraudulent means. 
NARR Narrative Narrative reason provided in the Additional Information. Used only where a more specific reason is not appropriate. 
Narrative description is provided.
TECH Technical 
Problem
Cancellation requested following technical problems 
resulting in an erroneous transaction.
Either the customer (Debtor) or a bank (Agent) in the payment 
flow experiences a technology issue which causes data within 
a payment to be incorrect. 
UPAY Undue Payment Payment is not justified. Either the customer (Debtor) or a bank (Agent) in the payment 
flow experiences an activity which causes a
payment to be executed under unexpected circumstances.

Payment Cancellation Request
Use Case c.55.1.1 –
792

camt.053
pacs.003
request the collections of funds from the debtors accounts for a creditor.
B A
793
Interbank pain.008
Interbank pain.002
pain.008
pain.002
Forwarding Agent (F) assigns 
a Customer Cancellation 
Request to Agent A 
(assignee) requesting the 
original pain.008 is cancelled, 
using reason code AM09.
2
F
camt.056 camt.055 camt.055 1
1
3
2 3
Creditor request the recall a 
previous instructed Direct 
Debit collection, as the amount 
was incorrect.
Creditor Agent (A) assigns a 
Cancellation Request to Agent B 
(assignee) requesting the original 
pacs.003 is cancelled, using 
reason code AM09.
camt.029 camt.029 camt.029

request the collection of funds from the debtors accounts for a creditor (through a Payment Market
Infrastructure).
B A F
794
Interbank pain.008
Interbank pain.002
pain.008
pain.002
pacs.003
Market Infrastructure will establish their own usage guidelines based on the ISO 
20022 standard.
pacs.003
Forwarding Agent (F) assigns 
a Customer Cancellation 
Request to Agent A 
(assignee) requesting the 
original pain.008 is cancelled, 
using reason code AM09.
camt.056 camt.055 2 camt.055 1
1
3
2 3
Creditor request the recall a 
previous instructed Direct 
Debit collection, as the amount 
was incorrect.
Creditor Agent (A) assigns a 
Cancellation Request to Agent B 
(assignee) requesting the original 
pacs.003 is cancelled, using 
reason code AM09.
camt.029 camt.029 camt.029

Financial Institution to 
Financial Institution Payment 
Cancellation Request
795

camt.056
Assignment
Underlying
is sent by an Agent to request the Cancellation of a 
payment previous sent.
The message is sent either: 
• directly (through the SWIFT Community CASE 
solution), or 
• serially through other agents. 
796
It is not recommended to request a Payment 
Cancellation Request (camt.056) of a Payment 
Return (pacs.004) instead an Exception and 
Investigation should be initiated to resolve this 
exertional use case

The FIToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This 
message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The 
FIToFIPaymentCancellationRequest message is exchanged between the payment Instructing Agent and the Instructed 
Agent to request the cancellation of an interbank payment message previously sent. 
pacs.008
pacs.002 pacs.008
camt.056
camt.029
A B C
797
camt.055
camt.056
camt.029
camt.053

The FIToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This 
message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The 
FIToFIPaymentCancellationRequest message is exchanged between the payment Instructing Agent and the Instructed 
Agent to request the cancellation of an interbank payment message previously sent. 
pacs.008
pacs.002 pacs.008
camt.056
A B C
798
camt.055
camt.029
camt.053

799
element description example element description example
Assigner Sender of the camt.056 Agent B Assigner Sender of the camt.029 Agent C
Assignee Receiver of the camt.056 Agent C Assignee Receiver of the camt.029 Agent B
Assignment 
Identification
Unique Id generated by the assigner 
to identify the Payment Cancellation 
Request message
CASE123/1 Assignment 
Identification
Unique Id generated by the assigner 
to identify the Resolution of 
Investigation message
STAT789/1
Cancellation 
identification
Optional Cancellation Id of the Agent 
sending (assigner) the Payment 
Cancellation Request message.
CASE123 Cancellation 
Status 
Identification
Case Reference of the Agent 
sending (assigner) the Resolution of 
Investigation message.
STAT789
Case 
Identification
Case Id of the Agent sending 
(assigner) the Payment Cancellation 
Request message.
CASE123 Resolved 
(Original) Case 
Identification
Case Id of the original case the 
Resolution of Investigation is 
responding to.
CASE123
Case 
Creator
Party w ho created the original 
cancellation request (w hich may be 
another Agent other than the current 
Assigner. 
Agent A Case Creator Party w ho created the original 
cancellation request (w hich is the 
same original case creator in the 
Payment Cancellation Request)
Agent A
Cancellation
Reason…
Originator
Party w ho provide the original 
Payment Cancellation Request 
(w hich may be another Party other 
than the current Assigner. 
Customer X Cancellation 
Status…
Originator
Party w ho provide the original
Cancellation response (w hich may 
be another Party other than the 
current Assigner. 
Customer Y
ISO camt.029 Resolution of Investigation 
Camt.056 Payment Cancellation Request ISO
CASE123
STAT789
Customer X Customer Y
my payment 
please
OK, I can 
understand the 
mistake.
CASEABC
STATYXZ
CASE545
STAT54X

800

q
Unique reference assigned by the assigner to
unambiguously identify the Cancellation request.
For Exceptions and Investigations messages the
Identification has no exact equivalent in the legacy MT
Exceptions and Investigations message. However, the
Transaction Reference Number (Field 20) could be
considered a similar comparison.
Directly comparable with the Transaction Reference
Number (Field 20) of the legacy MT statement message.
Assignment Identification
801

pacs.008
pacs.008 Assigner and Assignee represent the 
Agents involved in the point-to-point 
investigation message exchange. These 
roles therefore change on each message 
leg.
A B C D
Assignment
Assigner
Assignee
802
camt.056
camt.056
camt.029
camt.029
Assignee
Agent: Agent B
Assignee
Agent: Agent C
Assigner
Agent: Agent B
Assigner 
Agent: Agent A

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
803

804

y q
Unique reference assigned by the assigner to unambiguously identify the
Cancellation request.
For Exceptions and Investigations messages the Cancellation Identification
can be considered an equivalent in the legacy MT Directly comparable with
the Transaction Reference Number (Field 20) of the legacy MT statement
message.
Cancellation Identification
805
!
Underlying Transaction Information
Where Cancellation Identification is used this should represent the 
reference value as the Case Identification

The Identification element captures a unique case reference assigned by the
assigner to unambiguously identify the Cancellation investigation case.
For Exceptions and Investigations messages the Case Identification can be
considered an equivalent of the Transaction Reference Number (Field 20) of the
legacy MT Request for Cancellation message.
806
Case
Underlying Transaction Information
id
Min 1 – Max 1
The Creator element captures the party who created the investigation. This
mandatory party can represent as either an Agent i.e., the Bank who created the
case or as a Party i.e., the customer (for example the Debtor) who created the
request. In CBPR+ the creatoris always expected to be an Agent.
This element has no equivalent in the legacy MT Request for Cancellation message.
Min 1 – Max 1

Original Group Information
requested. The mandatory Original Message Identification contains the point-to-point reference from this
payment, and the mandatory Original Message Name Identification contains the message name of the
underlying payment. Optionally the Original Creation Date Time can also be captured.
Note: the xx in the CBPR+ Usage Guideline 
represents the message version of the message 
received for example pacs.008.001.08 
camt.056
A B For example:
Original Message Name Identification “pacs.008.001.08” confirms the
Cancellation request is for a pacs.008 Financial Institution to Financial
Institution Customer Credit Transfer. Where as “pacs.009.001.08”
confirms the Cancellation request for a pacs.009 Financial Institution
Credit Transfer.
Message 
Identification abcd1234
pacs.008.001.08 Original Message 
Name Identification
Original Message 
Identification abcd1234
Identification xyz9875
Original 
Group
Information 
Assignment
pacs.008
807
Underlying
Underlying Transaction Information
camt.029

pyg pyq
Original Instruction Identification
Original End to End Identification
Original UETR
Original Transaction 
Min 1 – Max 1
Min 1 – Max 1
Min 1 – Max 1
808
Underlying Transaction Information
Min 1 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
The Original elements enables the Assignee to identify the Payment which is being request
to be cancelled. The following element (in addition to Original Message identification and
Original Message Name Identification described on the previous page) are mandated:
Original End to End Identification
Original UETR
Original Interbank Settlement Amount
Original Interbank Settlement Date
The following element (in addition to Original Message identification and Original Message
Name Identification described on the previous page) are optional:
Original Instruction Identification
Original Transaction Identification
Original Clearing System Reference
Original Clearing System Reference
Original Interbank Settlement Date
Original Interbank Settlement Amount

q
Additional Information
Min 1 – Max 1
809
Underlying Transaction Information Cancellation Reason Info’ 
Min 0 – Max 2
Originator
Reason
?
the Originator element helps identify the party who request the payment Cancellation. This party
would have been included in the underlying payment and is also included the pacs.004 Return Chain
as the Creditor.
the Reason is mandatory and represented by an embedded CBPR+ Cancellation Code choice ( )
the Additional Information element may also be included to provide further details on the
Cancellation reason.
Min 0 – Max 1
Note where Reason code NARR is used additional information must be 
provided to describe the reason for the Cancellation request.
In the event that the case assigner wishes it indicate a willingness to
establish an indemnity agreement, INDM should be indicated at the
beginning of the Additional Information element. Any subsequent
additional information may then be included.

Cancellation message, which can be broadened afterthe coexistence period.
810
Code Name Definition Use Case
AGNT Incorrect Agent Agent in the payment workflow is 
incorrect.
A payment previous executed is identified as containing an incorrect 
correspondent (Agent) within the payment flow. A Cancellation request is 
generated so that the payment can be remediated following the successful 
return.
AM09 Wrong Amount Amount is not the amount agreed or 
expected.
The customer (Debtor) requests the initiation of a payment from their bank 
account, but subsequently realizes they had provided an incorrect amount.
COVR Cover Cancelled 
Or Returned
Cover payments has either been 
returned or cancelled.
Identifies an Agent to request the Cancellation of a pacs message where 
settlement method was COVE and the covering payment has been cancelled 
or returned.
CURR Incorrect 
Currency
Currency of the payment is incorrect. The customer (Debtor) requests the initiation of a payment from their bank 
account, but subsequently realizes they requested the wrong currency, as the 
payment has been executed. They request their bank to recall
the funds so that the payment can be re-executed in the correct currency
CUST Requested By 
Customer
Cancellation requested by the Debtor. The customer (Debtor) requests the initiation of a payment from their bank 
account, but subsequently wishes to recall the payment. The exactly 
underlying reason for the customer request is either not specified by the
customer or is not aligned to a more specific reason and therefore is not 
appropriate.

811
CUTA Cancel Upon 
Unable To Apply
Cancellation requested because an investigation 
request has been received and no remediation is 
possible.
An error occurred in the original payment (such as incorrect 
information) which was highlighted as part of an Investigation 
query. The request to cancel complements a response to the 
Investigation. 
DUPL Duplicate 
Payment
Payment is a duplicate of another payment. A customer (Debtor) requests the initiation of a payment from 
their bank account, but subsequently initiates
a new (separate) payment request in duplication of a previous 
payment. Having realized the error, the customer requests the 
recall of the duplicate transaction.
FRAD Fraudulent Origin Cancellation requested following a transaction that was 
originated fraudulently. The use of the Fraudulent 
Origin code should be governed by jurisdictions.
Either the customer (Debtor) or a bank (Agent) in the payment 
transaction experiences an activity which causes a payment to 
be executed by alleged fraudulent means. 
NARR Narrative Narrative reason provided in the Additional Information. Used only where a more specific reason is not appropriate. 
Narrative description is provided.
TECH Technical 
Problem
Cancellation requested following technical problems 
resulting in an erroneous transaction.
Either the customer (Debtor) or a bank (Agent) in the payment 
flow experiences a technology issue which causes data within 
a payment to be incorrect. 
UPAY Undue Payment Payment is not justified. Either the customer (Debtor) or a bank (Agent) in the payment 
flow experiences an activity which causes a
payment to be executed under unexpected circumstances.

Payment Cancellation Request
Use Case c.56.1.1 – High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008)
Use Case c.56.1.1.a – High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008) using gpi Stop and Recall
Use Case c.56.1.2 – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008)
Use Case c.56.1.2.a – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall
Use Case c.56.2.1 – High Level Payment Cancellation Request (camt.056) of a complete Customer Credit Transfers (pacs.008) settled using the cover method
Use Case c.56.2.2 – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method
Use Case c.56.2.3 – High Level Payment Cancellation Request (camt.056) of a Customer Credit Transfers (pacs.008) where the cover is returned
Use Case c.56.3.1 – High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer (pacs.009)
Use Case c.56.4.1 – High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer advice (pacs.009 adv)
812

pacs.008
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
Agent B creates an investigation case. 
Recognising the payment has already
been onward processed. They update 
Agent A and assign a Cancellation 
Request directly to Agent C.
Agent C creates an investigation case. 
Recognising the payment has already 
been onward processed. They update 
Agent B and assign a Cancellation 
Request directly to Agent D.
pacs.008 pacs.008 pacs.008
Agent D creates an investigation case. 
Recognising the payment has already 
been credited to the creditor. They 
request debit authority, providing the 
reason specified for the return request 
and updates Agent C. 
Once the outcome to the debit 
authorisation is know a final resolution 
to the investigation can be relayed any 
necessary return payment is arrange.
A C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
813
1 2 3 4
camt.056 camt.056 camt.056
camt.029 camt.029 camt.029 5
B
1
Debtor Agent (A) assigns a 
Cancellation Request to Agent 
B (assignee) requesting the 
original pacs.008 is returned, 
using reason code AM09.
2
3
4
5
example payment return

pacs.008
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
gpi Tracker identifies the payment is 
complete and forwards a camt.056 to 
Agent D.
pacs.008 pacs.008 pacs.008
Agent D creates an investigation case. 
Recognising the payment has already been 
credited to the creditor. They request debit 
authority, providing the reason specified for 
the return request and updates the gpi
Tracker. 
Once the outcome to the debit authorisation is 
know a final resolution to the investigation can 
be provided and any necessary return 
payment is arrange.
A C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
814
1
2
camt.029
B
1
Debtor Agent (A) initiates a gpi
Stop and Recall, requesting
the original pacs.008 is 
returned, using reason code 
AM09.
2
3 4
See use case p.8.1.1 for the original payment,
c.29.1.1 for case resolution and p.4.1.3. for an 
example payment return
camt.029

pacs.008
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
Agent B creates an investigation case. 
Recognising the payment has already
been onward processed. They update 
Agent A and assign a Cancellation 
Request directly to Agent C.
Agent C creates an investigation case. 
Recognising the payment has not been 
onward processed. They update Agent 
B that the Cancellation Request is 
accepted any necessary return 
payment is arrange.
pacs.008 pacs.008
A C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
815
1 2 3 4
camt.056 camt.056
camt.029 camt.029
B
1
Debtor Agent (A) assigns a 
Cancellation Request to Agent 
B (assignee) requesting the 
original pacs.008 is returned, 
using reason code AM09.
2
3 4
example payment return

pacs.008
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
gpi Tracker identifies the payment is 
incomplete and forwards a camt.056 to 
Agent C.
pacs.008 pacs.008
Agent C creates an investigation case. 
Recognising the payment has not been onward 
processed. They updates the gpi Tracker any 
necessary return payment is arrange.
A C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
816
1
2
4
camt.029
B
1
Debtor Agent (A) initiates a gpi
Stop and Recall, requesting
the original pacs.008 is 
returned, using reason code 
AM09.
2
3 4
camt.029

pacs.008
pacs.002
pacs.009 cov pacs.009 cov
Settlement 
Complete
A D
B C
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
817
2 camt.056
1 camt.029
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
1
Debtor Agent (A) assigns a 
Cancellation Request to Agent 
D (assignee) requesting the 
original pacs.008 is returned, 
using reason code AM09.
2
3
Agent D creates an investigation case. Recognising the 
payment has already been credited to the creditor. They request 
debit authority, proving the reason specified for the return 
request and update Agent A. 
Once the outcome to the debit authorisation is know a final 
resolution to the investigation can be relayed and any necessary 
return payment can be initiated.
3
See use case p.8.2.1 for the original payment,
c.29.2.1 for case resolution and p.4.3.2 for an 
example payment return

pacs.008
pacs.002
pacs.009 cov pacs.009 cov
Settlement 
Complete
A D
B C
Market Infrastructure will either conform to HVPS+ guidelines or establish their own 
usage guidelines based on the ISO 20022 standard.
818
2 camt.056
1 camt.029
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
1
Debtor Agent (A) assigns a 
Cancellation Request to Agent 
D (assignee) requesting the 
original pacs.008 is returned, 
using reason code AM09.
2
3
Agent D creates an investigation case. Recognising the 
payment has not been credited to the creditor. They update 
Agent A that the Cancellation Request is accepted and arrange 
the necessary return payment once the pacs.009 cov settlement 
is confirmed by Agent C
3
See use case p.8.2.1 for the original payment,
c.29.2.1 for case resolution and p.4.3.2 for an 
example payment return

pacs.002
pacs.009 cov
+ Reject 
Reason 
+ Return 
Reason 
1 camt.056
Agent C receives the payment and 
recognises the payment can not be 
completed as requested e.g. the Agent D 
does not maintain an account with them. 
A
B C
D
819
camt.029
Debtor Agent (A) assigns a 
Cancellation Request to Agent D 
(assignee) requesting the original 
pacs.008 is considered null and 
void, using reason code COVR.
1 Agent D creates an investigation case. Recognising the 
cover payment will not be received to settle the pacs.008. 
As the creditor has not been credited in advance of cover 
settlement, a final resolution to the investigation can be 
provided. A payment return is not necessary. 
2
2
See use case p.8.2.1 for the cover payment sample
c.29.2.2 for case resolution and p.4.3.3 for payment 
return

pacs.009 camt.053 pacs.009
A pacs.002 pacs.002 B C D
Market Infrastructure will either conform to HVPS+ guidelines or establish their 
own usage guidelines based on the ISO 20022 standard.
camt.054
820
See use case p.9.1.1 for the cover payment sample
c.29.3.1 for case resolution and p.4.2.3 for payment 
return
1 camt.056 camt.056
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
1
2 3
Agent C creates an investigation case. Recognising the 
payment has already been credited to the creditor. They 
request debit authority, proving the reason specified for 
the return request and update Agent C. 
Once the outcome to the debit authorisation is know a 
final resolution to the investigation can be relayed and 
any necessary return payment can be initiated.
Debtor Agent (A) assigns a 
Cancellation Request to Agent 
C (assignee) requesting the 
original pacs.009 is returned, 
using reason code AM09.
2 3
camt.029 camt.029
pacs.009

pacs.009
pacs.002
B E
C D
A F
821
See use case p.9.1.2 for the cover payment sample
c.29.4.1 for case resolution and p.4.2.3 for payment 
return
2 camt.056
1 camt.029
Debtor request their bank to 
recall a previous instructed 
payment, as the amount was 
incorrect.
1
Debtor Agent (A) assigns a 
Cancellation Request to Agent 
E (assignee) requesting the 
original pacs.008 is returned, 
using reason code AM09.
2
3
Agent E creates an investigation case. Recognising the payment 
has already been credited to the creditor. They request debit 
authority, proving the reason specified for the return request and 
update Agent B. 
Once the outcome to the debit authorisation is know a final 
resolution to the investigation can be relayed and any necessary 
return payment can be initiated.
3

camt.108 - Cheque Cancellation or Stop Request
camt.109 – Cheque Cancellation or Stop Report
822

Cheque Presentment Notification
823

camt.107
Group Header
Cheque
by a drawer bank, or a bank acting on behalf of the 
drawer bank to the bank on which a cheque has been 
drawn (the drawee bank).
It is used to advise the drawee bank, or confirm to an 
enquiring bank, the details concerning the cheque 
referred to in the message.
824
The Cheque Presentment Notification is restricted to a single cheque 
per InterAct message.

The Agent A (drawer agent) sends a ChequePresentmentNotificationmessage to Agent B (the drawee agent). 
The ChequePresentmentNotificationmessage informs the drawee agent about the cheque submission. 
The notification message facilitates the drawee agent to follow up the cheque submission and relevant business process.
B
CBPR+ Workshop – June 21,22,23 2022 825
camt.107
Drawer Agent Drawee Agent

826

ggg, 
the Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
For Cash Management (camt) messages the Message Identification has no exact equivalent in
the legacy MT Advice of Cheque message. However, the Sender’s Reference (Field 20) could be
considered a similar comparison.
Group Header Message Identification
827

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
828

Group Header Number Of Cheques
829
The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1. 
12,000

830

Cheque
831
This Cheque element has been restricted to one cheque occurrence.
12,000

Cheque Instruction Identification
832
Point to point reference that can be used between the Agent instructing the
Cheque Presentment Notification and the Drawee Agent (Agent receiving this
message) to refer to the individual instruction.
unambiguously the instruction

Cheque Cheque Number
833
Unique and unambiguous number for a cheque as assigned by the Drawee
Agent. This cheque number is often found as part of the Magnetic Ink Character
Recognition (MICR) encoding at the bottom of a cheque
unambiguously the Cheque.

Cheque
834
The Issue Date is a mandatory element, and represents the date when the cheque was
issued by the payer, or on behalf of the payer
The Stale Date is an optional element and represents the date after which a cheque is no
longer valid. The validity period of a cheque is calculated from the issue date on the face
of the cheque. The period may be indicated on the face of the cheque itself such as "Valid
for 90 days” or may be determined in accordance with domestic banking practice.
Not all countries will have a validity period.
Min 1 – Max 1
10
Min 0 – Max 1
10
Issue Date
Stale Date

835
The Value Date is an optional element, it is used to capture the Date, where different to
the Issue Date, i.e., represents a date on the cheque in the future. The cheque Value
Date describes the date in which the cheque amount becomes available to be deposited
on the payee account.
10
Min 0 – Max 1
Cheque
Value Date Date
Amount
A mandated currency Amount of the cheque to be paid to the payee. £ $ Min 1 – Max 1
¥
The Value Date captured in the camt.107 is referred to as Effective Date in the camt.108
Cheque Cancellation orStop Request and camt.109 Cheque Cancellation or Stop Report

Cheque Payer
836
upon presentment, to the payee. The Payer sub-element describe the 
Payer in greater detail. 
Country of 
Residence
Optional element to 
capture the Payee’s ISO 
country code of residence 
Identification
Nested element capturing the 
various types of identifiers for 
the party e.g. BIC, LEI etc.
Postal 
Address
Nested element capturing either 
structured or unstructured Payer
address details
Payer

Cheque Payer Account
837
The Payer Account uses a variety of nested elements to capture information related to 
the account.
Min 0 – Max 1 Identification identifies the account maintained at the Drawer Agent (Account
Servicing Institution)
Type uses the external CashAccount Type code list to identify the type of account
Currency identifies the currency of the account
Name identifies the name of the account as assigned by the Drawer Agent (Account
Servicing Institution)
Proxy captures an alternative identification of the account number such as an email
address. This element has further nested Type which is a choice of external code list or
proprietary code and Identification which are both mandatory where the Proxy element
is used.
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1
Min 0 – Max 1

838
been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification is 
sent to the Drawee Agent.
Cheque
Drawer Agent
Drawer Agent Account
12,000
The Drawer Bank is typically identified on the cheque together with their Postal Address. The Drawer
Agent’s Account with the DraweeAgent is also often also identified on the cheque.
The Drawer Agent Account optionally captures the Drawer Agent’s Account with the Drawee Agent 
and who would receive an order the pay the cheque upon presentment.
Min 0 – Max 1
DRAWEE AGENT ID 
DRAWER AGENT ACCOUNT 1234

Cheque Payee
839
Payee sub-element describe the Payee in greater detail. 
Country of 
Residence
Optional element to 
capture the Payee’s ISO 
country code of residence 
Identification
Nested element capturing the 
various types of identifiers for 
the party e.g. BIC, LEI etc.
Postal 
Address
Nested element capturing either 
structured or unstructured Payee
address details
Payee

g
Serial Financial Institution to Financial Institution to Customer Credit Transfer 
Use Case c.107.1 – High Level Drawer Agent Cheque issuance to Payee, on their account with the Drawer Agent
Use Case c.107.2 - High Level Drawer Agent Cheque issuance to Payee, on their head office’s account with the Drawer Agent
840

Drawee Agent (B) receives the 
cheque presentment via the cheque 
clearing. They validate the 
presented cheque details again the 
information received on the Cheque 
Presentment Notification to 
conclude whether the cheque can 
be settled. 
Agent C receives the cheque 
deposit and present it into the 
domestic cheque clearing
The Drawee Agent (B) receives 
the Cheque Presentment 
Notification and store the 
information in anticipation for 
the cheque to be presented
1
Payer instructs the Drawer 
Agent to issue a cheque to the 
Payee 
Drawer Agent (A) issues a 
cheque to the Payee drawn of 
their account at the Drawee 
Agent (B) 
In parallel the Drawer Agent (A) 
initiates a Cheque Presentment 
Notification to the Drawee Agent 
(B)
Payee received the cheque and 
present it to their bank (Agent C)
5
A
B C
841
12,000
2b
3
4
2a
2b
3
4
5
6
6
Drawer
Drawee
Payer Payee

HO
Drawee Agent (B) receives the 
cheque presentment via the cheque 
clearing. They validate the 
presented cheque details again the 
information received on the Cheque 
Presentment Notification to 
conclude whether the cheque can 
be settled. 
Agent C receives the cheque 
deposit and present it into the 
domestic cheque clearing
The Drawee Agent (B) receives 
the Cheque Presentment 
Notification and store the 
information in anticipation for 
the cheque to be presented
1
Payer instructs their Bank 
(Agent A) to issue a cheque to 
the Payer 
Agent (A) issues a cheque to the 
Payee drawn of their head 
office’s (HO) account at the 
Drawer Agent (B) 
In parallel the Agent (A) initiates 
a Cheque Presentment 
Notification to the Drawee Agent 
(B)
Payee received the cheque and 
present it to their bank (Agent C)
5
A
B C
842
12,000
2b
3
4
2a
2b
3
4
5
6
6
Drawer
Drawee
Payer Payee

Cheque Cancellation or Stop Request
843

camt.108
Group Header
Cheque
is sent by a drawer bank, or a bank acting on behalf of 
the drawer bank, to the agent on which a cheque has 
been drawn (the drawee bank) to request for the 
cancellation of the presentment and/or stop the 
payment of the cheque referred to in the message.
844
The Cheque Cancelation or Stop Report is restricted to a single
cheque per InterAct message.

The Agent A (Drawer Agent) sends a ChequeCancelationOrStopRequest message to Agent B (the Drawee Agent). 
The ChequeCancelationOrStopReques message requests the drawee agent to place a stop (refusal to settle) upon 
presentment of the cheque, effectively canceling the issued cheque.
B
CBPR+ Workshop – June 21,22,23 2022 845
camt.107
Drawer Agent Drawee Agent
camt.108
camt.109

846

ggg, 
the Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
For Cash Management (camt) messages the Message Identification has no exact equivalent in
the legacy MT Advice of Cheque message. However, the Sender’s Reference (Field 20) could be
considered a similar comparison.
Group Header Message Identification
847

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
848

Group Header Number Of Cheques
849
The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1. 
12,000

850

Cheque
851
This Cheque element has been restricted to one cheque occurrence.
12,000

Cheque Instruction Identification
852
Point to point reference that can be used between the Agent instructing the
Cheque Cancellation or Stop Request and the Drawee Agent (Agent receiving
this message) to refer to the individual instruction.
identify unambiguously the instruction

Cheque Original Instruction Identification
853
Point to point reference that can be used to identify the original Cheque
Presentment Notification between the Agent instructing the Cheque Presentment
Notification and the Drawee Agent (Agent receiving this message) to refer to the
individual instruction.
element to identify unambiguously the original instruction

Cheque Cheque Number
854
Unique and unambiguous number for the cheque as assigned by the Drawee
Agent. This cheque number is often found as part of the Magnetic Ink Character
Recognition (MICR) encoding at the bottom of a cheque
unambiguously the Cheque.

Cheque
855
The Issue Date is a mandatory element, and represents the date when the cheque was
issued by the payer, or on behalf of the payer
The Stale Date is an optional element and represents the date after which a cheque is no
longer valid. The validity period of a cheque is calculated from the issue date on the face
of the cheque. The period may be indicated on the face of the cheque itself such as "Valid
for 90 days” or may be determined in accordance with domestic banking practice.
Not all countries will have a validity period.
Min 1 – Max 1
10
Min 0 – Max 1
10
Issue Date
Stale Date

856
10
Min 0 – Max 1
Cheque
Value Date Date
Amount
A mandated currency Amount of the cheque to be paid to the payee. £ $ Min 1 – Max 1
¥
The Effective Date is an optional element, it is used to capture the original Value Date
(as provided in the camt.107), where different to the original Issue Date, i.e., represents a
date on the cheque in the future. The cheque Value Date describes the date in which the
cheque amount becomes available to be deposited on the payee account.

857
has been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification 
is sent to the Drawee Agent. 
Cheque
Drawer Agent
Drawer Agent Account
12,000
The Drawer Agent and Drawer Account elements where present should match that of the original
camt.107 Cheque Presentment Notification.
The Drawer Agent Account optionally captures the Drawer Agent’s Account with the Drawee Agent 
and who would receive an order the pay the cheque upon presentment.
DRAWEE AGENT ID 
DRAWER AGENT ACCOUNT 1234

Cheque Payee
858
The Payee sub-element describe the Payee in greater detail. 
Country of 
Residence
Optional element to 
capture the Payee’s ISO 
country code of residence 
Identification
Nested element capturing the 
various types of identifiers for 
the party e.g. BIC, LEI etc.
Postal 
Address
Nested element capturing either 
structured or unstructured Payee
address details
Payee
The Payee element where present should match that of the original camt.107
ChequePresentment Notification.

the Originator element is a embedded code choice that helps identify the party who request the
cheque cancellation or stop request. Where used this party would typically be the Payer (code PAYR)
of the cheque.
the Reason is mandatory and represented by an embedded CBPR+ Cancellation Code choice ( )
the Additional Information element may also be included to provide further details on the
cancellation or stop reason.
qp q
Additional Information
Min 1 – Max 1
859
Cheque Cheque Cancellation or Stop Reason
Min 0 – Max 2
Originator
Reason
?
Min 0 – Max 1
Note where Reason code NARR is used additional information must be 
provided to describe the reason for the Cheque Cancellation or Stop 
request.

g
Serial Financial Institution to Financial Institution to Customer Credit Transfer 
Use Case c.108.1 – High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque
Use Case c.108.2 – High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.
860

1
Payer instructs the Drawer 
Agent they wish to cancel or 
stop a previously issued 
cheque, as the Payee informs 
them the cheque has been lost.
Drawee Agent (B) match the request 
to the previous Cheque Presentment 
Notification (camt.107). As the 
cheque has not been presented the 
status record is identified as not to be 
paid if presented, as a result of a 
cancellation/stop request. This is 
reported back to the Drawer Agent 
(A) as accepted.
A
B C
861
2
Drawer Agent (A) issues a 
cheque cancellation or stop 
request to the Drawee Agent (B) 
with reason code LOST
2
3
3
See use case c.109.1.1 for an example the Cheque 
Cancellation or Stop Report
Drawer
Drawee
Payer Payee

1
Payer instructs the Drawer 
Agent they wish to cancel or 
stop a previously issued 
cheque, as the Payer informs 
them they no longer wish to 
honour the cheque.
Drawee Agent (B) match the request 
to the previous Cheque Presentment 
Notification (camt.107). As the 
cheque has already been presented 
and paid the cancellation/stop 
request can not be executed. This is 
reported back to the Drawer Agent 
(A) as rejected with additional 
information to explain the cheque has 
already been paid.
A
B C
862
2
Drawer Agent (A) issues a 
cheque cancellation or stop 
request to the Drawee Agent (B) 
with reason code CUST
2
3
3
12,000
See use case c.109.1.2 for an example the 
Cheque Cancellation or Stop Report
Drawer
Drawee
Payer Payee

Cheque Cancellation or Stop Report
863

camt.109
Group Header
Cheque
sent by the drawee agent (on which a cheque is 
drawn) to the drawer agent, or the agent acting on 
behalf of the drawer agent, to indicate what actions 
have been taken in attempting to cancel the 
presentment and/or stop the payment of the cheque 
referred to in the message.
864
The Cheque Cancelation or Stop Request is restricted to a single
cheque per InterAct message.

The Agent B (Drawee Agent) sends a ChequeCancelationOrStopReport message to Agent A (the Drawer Agent). 
The ChequeCancelationOrStopReport message reports the outcome of a Cheque Cancellation or Stop Request.
B
CBPR+ Workshop – June 21,22,23 2022 865
camt.107
Drawer Agent Drawee Agent
camt.108
camt.109

866

ggg, 
the Group Header. This 35 character identifier is a point-to-point reference used to
unambiguously identify the message.
For Cash Management (camt) messages the Message Identification has no exact equivalent in
the legacy MT Advice of Cheque message. However, the Sender’s Reference (Field 20) could be
considered a similar comparison.
Group Header Message Identification
867

CBPR+ usage guidelines mandate the time zone that the time represents as an offset 
against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, 
Central Daylight Savings Time as well as Eastern Standard Time in the U.S.) 
10
All CBPR+ time elements need offset against UTC. Milliseconds are 
optional. 
Group Header Creation Date Time
868

Group Header Number Of Cheques
869
The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1. 
12,000

870

Cheque
871
This Cheque element has been restricted to one cheque occurrence.
12,000

Cheque Instruction Identification
872
Point to point reference that can be used between the Drawee Agent providing
the Cheque Cancellation or Stop Report and the Drawee Agent (Agent receiving
this message) to refer to the individual instruction.
identify unambiguously the instruction

Cheque Original Instruction Identification
873
Point to point reference that can be used to identify the original Cheque
Cancellation or Stop Request between the Agent instructing the Cheque
Presentment Notification and the Drawee Agent (Agent receiving the request
message) to refer to the individual request.
element to identify unambiguously the original instruction

Cheque Cheque Number
874
Unique and unambiguous number for the cheque as assigned by the Drawee
Agent. This cheque number is often found as part of the Magnetic Ink Character
Recognition (MICR) encoding at the bottom of a cheque
unambiguously the Cheque.

Cheque
875
The Issue Date is a mandatory element, and represents the date when the cheque was
issued by the payer, or on behalf of the payer
The Stale Date is an optional element and represents the date after which a cheque is no
longer valid. The validity period of a cheque is calculated from the issue date on the face
of the cheque. The period may be indicated on the face of the cheque itself such as "Valid
for 90 days” or may be determined in accordance with domestic banking practice.
Not all countries will have a validity period.
Min 1 – Max 1
10
Min 0 – Max 1
10
Issue Date
Stale Date

876
The Effective Date is an optional element, it is used to capture the original Value Date
(as provided in the camt.107), where different to the original Issue Date, i.e., represents a
date on the cheque in the future. The cheque Value Date describes the date in which the
cheque amount becomes available to be deposited on the payee account.
10
Min 0 – Max 1
Cheque
Value Date Date
Amount
A mandated currency Amount of the cheque to be paid to the payee. £ $ Min 1 – Max 1
¥

877
has been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification 
is sent to the Drawee Agent. 
Cheque
Drawer Agent
Drawer Agent Account
12,000
The Drawer Agent and Drawer Account elements where present should match that of the original
camt.107 Cheque Presentment Notification.
The Drawer Agent Account optionally captures the Drawer Agent’s Account with the Drawee Agent 
and who would receive an order the pay the cheque upon presentment.
DRAWEE AGENT ID 
DRAWER AGENT ACCOUNT 1234

Cheque Payee
878
The Payee sub-element describe the Payee in greater detail. 
Country of 
Residence
Optional element to 
capture the Payee’s ISO 
country code of residence 
Identification
Nested element capturing the 
various types of identifiers for 
the party e.g. BIC, LEI etc.
Postal 
Address
Nested element capturing either 
structured or unstructured Payee
address details
Payee
The Payee element where present should match that of the original camt.107
ChequePresentment Notification.

the Originator element helps identify the party who request the cheque cancellation or stop request.
Where used this party would typically be the Payer of the cheque.
the Status is mandatory and represented by an embedded status Code choice ( )
REJT (Rejected) or ACCP (Accepted)
the Additional Information element may also be included to provide further details on the
cancellation or stop reason.
qp q
Additional Information
Min 1 – Max 1
879
Cheque Cheque Cancellation or Stop Reason
Min 0 – Max 2
Originator
Reason
!
Min 0 – Max 1
Note where Status code REJT is used additional information must be 
provided to describe the reason for the rejection.

g
Serial Financial Institution to Financial Institution to Customer Credit Transfer 
Use Case c.109.1 – High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque
Use Case c.109.2 – High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.
880

Drawee Agent (B) reports to the 
Drawer Agent (A) that the Cheque 
Cancellation or Stop request has 
been accepted.
A
B C
881
1
1
See use case c.108.1.1 for an example the Cheque 
Cancellation or Stop Request
Drawer
Drawee
Payer Payee

Drawee Agent (B) reports to the 
Drawer Agent (A) that the Cheque 
Cancellation or Stop request has 
been rejected. Additional Information 
is provided to explain that the cheque 
has already been presented and paid. 
A
B C
882
1
12,000
1
See use case c.108.1.2 for an example the Cheque 
Cancellation or Stop Request
Drawer
Drawee
Payer Payee

www.swift.com

head.001 The head.001 services This element Business Business on the SWIFT is currently Application Application network. not foreseen Header Header to be used – Market Market by CBPR+. Min 0 – Max 1 Practice Practice element is used to identify administered 
Market Practice 
  33

pain.001 pain.002 Payment - Interbank – Interbank Initiation Customer Customer - Messages Credit Transfer Payment index initiation Status Report U
pain.008 -Customer Direct Debit Initiation 
    39

 and the Creditor Issuer should Reference be specified is with structured the text ‘ISO’ in accordance with (without the ISO 11649, quote marks) the Remittance Information Structured 
ISO 20022 Programme 2021 Corporate Work Group Confidentiality: Restricted 95

camt.052 Bank to Customer Account Report – Bank Transaction The description available code list Code of Bank to download page. These descriptions Transaction from the ISO20022.org include the descriptions Codes Min 1 – Max 1 are external for
Payments Domain Families and sub-families for both
Received and Issued Credit Transfers. 
https://www.iso20022.org/external_code_list.page   
   563

Index Use case Payment of camt.055 should Cancellation be considered Request Use Cases as a principal example whereby use case may be cross referenced 
Use Case c.55.1.1  
   792

camt.107 camt.108 Cheque – Cheque - Cheque - Messages Presentment Cancellation index Notification or Stop Request 
camt.109 -Cheque Cancellation or Stop Report 
    822

The ChequePresentmentNotificationmessage The notification message facilitates the drawee informs agent the drawee to follow agent up the cheque about the cheque submission submission. and relevant business process. 
CBPR+ Workshop -June 21,22,23 2022 825

The ChequeCancelationOrStopReques presentment of the cheque, effectively message canceling the requests the drawee issued cheque. agent to place a stop (refusal to settle) upon 
CBPR+ Workshop -June 21,22,23 2022 845

The Agent The ChequeCancelationOrStopReport B (Drawee Agent) sends a ChequeCancelationOrStopReport message reports the outcome message of a Cheque to Agent Cancellation A (the Drawer or Stop Agent). Request. 
CBPR+ Workshop -June 21,22,23 2022 865

---

