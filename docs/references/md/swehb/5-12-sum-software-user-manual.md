# 5.12 - SUM - Software User Manual

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695673. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual

5.12 - SUM - Software User Manual

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695673)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695673&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Minimum Recommended Content](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)

Return to [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)

# 1. Minimum Recommended Content

Minimum recommended content for the Software User Manual. 

1. Software summary, including:  application, inventory, environment, organization, overview of operation, contingencies, alternate states, and modes of operation, security, privacy, assistance, and problem reporting.
2. Access to the software:  first-time user of the software, initiating a session, and stopping and suspending work.
3. Processing reference guide:  capabilities, conventions, processing procedures, related processing, data backup, recovery from errors, malfunctions, emergencies, and messages.
4. Assumptions, limitations, and safety-related items/concerns or constraints.
5. Information that is unique or specific for each version of the software (e.g., new and modified features, new and modified interfaces).

# 2. Rationale

Very few software projects result in a product that users understand and can use efficiently, completely, and successfully without some guidance. Software documentation "explains the capabilities of the software or provides operating instructions for using the software to obtain the desired results." [373](#_tabs-<p></p>)  Along with software and other documentation, the final delivered package for software projects, including contracted projects, includes operational instructions for the delivered software. These instructions are typically provided by a Software User Manual, which contains both user instructions and a description of the functions and features provided by the software.

# 3. Guidance

**NASA STD 8719.13 (Rev C ) - NASA Software Safety Standard**

7.7.8 Operational documentation, including user manuals and procedures, will describe all safety related commands, data, input sequences, options, error messages, corrective actions, and other items necessary for the safe operation of the system which software implements.

7.7.9 The provider SMA responsible for operations and maintenance shall evaluate user manuals and procedures (including updates) for safety-related commands, data, input sequences, options, error messages, corrective actions, and other items implemented in software which are necessary for the safe operation of the system, and for any safety impacts. This will ensure that any software-related hazard closures that depend on operational workarounds are properly documented.

[271](#_tabs-<p></p>)

Software User Manuals are written with the user in mind. Software User Manuals may be used as tutorials, introductions to the software, or just as reference guides. Regardless of how often the user will pick up the manual, it needs to be complete, accurate, and written with easy-to-find information that is concise, yet detailed enough to be clearly understood. Depending on the intended audience, it may also be helpful to organize the manual by tasks that the user is expected to perform using the software.

The Software User Manual is typically created before software system testing so that the manual can be verified during this test phase for accuracy and completeness. In accordance with SEL-81-305 [047](#_tabs-<p></p>), Revision 3, Recommended Approach to Software Development, "The development team begins preparation of the user's guide during the implementation phase... A draft is completed by the end of the implementation phase and is evaluated during system testing. At the beginning of the acceptance test phase, an updated version is supplied to the acceptance test team for evaluation. Corrections are incorporated, and a final revision is produced at the end of the phase."

For NASA flight projects, the Software User Manual is baselined by the Operational Readiness Review (ORR). See also [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design), Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews), [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products).

A complete user manual contains:

* a summary of the software
* instructions for starting and using that software
* a processing reference guide
* assumptions, limitations, and safety information
* any information unique to this version of the software

Assistance for completing each of these elements of a Software User Manual is provided below.

## 3.1 Software Summary

The software summary provides an overview of the software, including:

* Application – explanation of specific tasks for which the software is intended; the software's purpose and background; benefits from use of the software.
* Inventory – a list of all elements included in the software package; elements required to successfully install and run the software, including databases and data files.
* Environment – hardware (e.g., computer equipment and communications equipment); other software (e.g., operating systems, databases, utilities, data files; physical conditions); and setup necessary for the successful operation of the software and in which the software was designed to operate. If applicable, include "high-level diagrams of system showing hardware interfaces, external data interfaces, software architecture, and data flow." [047](#_tabs-<p></p>)
* Organization – user's perspective of software organization; logical components with purpose and operation relevant to the user as opposed to the developer.
* Overview of operation – summary of the features and functions available from the software, including displays, windows, menus, reports, and system performance considerations; performance characteristics (e.g., rate of input that is accepted, rate of output, response time, error rate); relationship of the functions performed by the software with interfacing systems, organizations, or positions; supervisory controls that are available to manage the software.
* Contingencies, alternate states, modes of operation – a list and description of modes in which software operates (e.g., normal, emergency, critical, launch, and on-orbit), along with available and restricted operations and functions in each mode; differences between normal operation and operation in times of emergency.
* Security and privacy – description of security and privacy considerations associated with the software, including, as applicable, making unauthorized copies of the software.
* Assistance – contact information when assistance is needed to operate the software.
* Problem reporting – steps to perform to report a software problem for correction.

## 3.2 Access To the Software

The software access portion of the user manual needs to be written for a first-time user of the software and provide instructions for:

* Initiating a session – obtaining a password, changing a password, starting the software, logging in, and any other steps to begin using the software.
* Stopping and suspending work – steps for saving work, logging off, shutting down, and any other steps for cleanly ending a session.
* Equipment familiarization – powering on the system, expected initialization screens, and expected user responses/actions, using the keyboard and pointing device, powering down the system.
* Installation and setup – equipment setup; loading software; system initialization, including files, variables, and data; tailoring and reconfiguration; re-initialization.
* Software access under abnormal conditions – determining if abnormal termination occurred; restarting after abnormal termination; recovery procedures, as applicable.
* Security and privacy for storing and marking reports generated by the system.

## 3.3 Processing Reference Guide

The processing reference guide needs to provide the following reference information:

* Capabilities – "the interrelationships of the transactions, menus, functions, or other processes." [063](#_tabs-<p></p>)
* Conventions – meaning of colors in displays, audible alarms, abbreviations, and any other conventions used in the software; "rules for assigning names or codes." [063](#_tabs-<p></p>)
* Processing procedures – "Detailed description of processing keyed to operator-specified input and actions in terms of points of control, functions performed, and results obtained (both normal and abnormal, i.e., error processing and recovery)" [047](#_tabs-<p></p>), including:

* Purpose of menus, functions, transactions, processes.
* Step-by-step procedures.
* User inputs.
* User commands, including data entry, save, print, update, and delete; and operation cancellation, interruption, and restart.
* Expected results.
* Images of menus, icons, forms, diagnostic messages, as applicable, with explanations.
* Software navigation.
* Help or information for accessing on-line help.
* If appropriate, a tutorial.

* Related processing – "identify and describe any related batch, offline, or background processing performed by the software that is not invoked directly by the user and is not described in [processing procedures]...user responsibilities to support this processing shall be specified." [063](#_tabs-<p></p>)
* Data backup – steps the user is to perform to back up any data collected or generated by the software such that it can be used to replace data in case of system error.
* Recovery from errors, malfunctions, emergencies – steps the user is to perform if an error condition occurs in the software; steps to ensure continuity of operations in the event of an emergency.
* Messages – a list of informational, diagnostic, error, and warning messages that can be generated by the software and any associated actions required by the user; may be an appendix that contains this information.

## 3.4 Assumptions, Limitations, and Safety-Related Items/Concerns or Constraints

This portion of the Software User Manual describes any operating assumptions, limitations, constraints, or safety-related concerns not described elsewhere in the manual. Providing this information allows the user to understand the bounds of the software and its operation, including limitations and safety-related concerns that can be affected by user input and actions.

## 3.5 Information That Is Unique Or Specific For Each Version Of the Software

Each version of software is unique in some way, e.g., new and modified features and/or new and modified interfaces. It is important for the author to include in the Software User Manual descriptions of the items that make a particular version of software unique from previous versions, if there are previous versions of the software.

## 3.6 Additional Content

Additional content to consider for inclusion in the Software User Manual includes:

* Identifying information for the software, such as software name, system name, identification number, version number, release number, release date, issuing organization.
* High-level description of input and output.

1. Resources — discussion, high-level diagrams, and tables for system and subsystems.
   1. Hardware.
   2. Data definitions, i.e., data groupings and names.
   3. Peripheral space considerations — data storage and printout.
   4. Memory considerations — program storage, array storage, and data set buffers.
   5. Timing considerations.  
      1. Central Processing Unit time in terms of samples and cycles processed.
      2. Input/output time in terms of data sets used and type of processing.
      3. Wall-clock time in terms of samples and cycles processed.
2. Run information — control statements for various processing modes.
3. Control parameter information — by subsystem, detailed description of all control parameters, e.g., NAMELISTs, including name, data type, length, representation, function, valid values, default value, units, and relationship to other parameters" [047](#_tabs-<p></p>)

* Summary of history of system development, operation, maintenance. [063](#_tabs-<p></p>)
* System in which software is intended to be used or in which the software is a part. [063](#_tabs-<p></p>)
* Project sponsor, acquirer, user, developer, and support agencies. [063](#_tabs-<p></p>)
* Current and planned operating sites. [063](#_tabs-<p></p>)
* Quick reference guide.
* Glossary of terms, acronyms, and abbreviations.

## 3.7 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

No additional guidance is available for small projects. The community of practice is encouraged to submit guidance candidates for this paragraph.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-047)

  ["Recommended Approach to Software Development,"](http://everyspec.com/NASA/NASA-GSFC/GSFC-General/SEL-81-305_REV-3_2419/ "Click to open in new window")

  SEL-81-305, Revision 3, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1992.
* (SWEREF-063) Software User Manual (SUM) Template,  GRC-SW-TPLT-SUM, NASA Glenn Research Center (GRC), 2011.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-221)

  [IEEE Computer Society, "IEEE Standard for Software User Documentation,"](http://standards.ieee.org/findstds/standard/1063-2001.html "Click to open in new window")

  IEEE STD 1063-2001, 2001. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022

  

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products)        * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design)      * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
