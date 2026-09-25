# 8.58 - Software Safety and Hazard Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695750. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis

8.58 - Software Safety and Hazard Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695750)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695750&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Software Safety Analysis](#tabs-2)
* [3. Hazard Analysis](#tabs-3)
* [4. Hazard Report Content](#tabs-4)
* [5. Resources](#tabs-5)

Return to [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products)

# 1. Introduction

This section deals with some of the special considerations that are necessary when working with software systems that have safety-critical software. According to the NASA Standard for Software Assurance and Software Safety, NASA-STD-8739.8[278](#_tabs-<p>5</p>), safety-critical software is defined as follows:

Software is considered safety-critical if it meets one of the following criteria:

1. Causes or contributes to a system hazardous condition/event,
2. Provides control or mitigation for a system hazardous condition/event,
3. Controls safety-critical functions,
4. Mitigates damage if a hazardous condition/event occurs,
5. Detects, report, and takes corrective action if the system reaches a potentially hazardous state.

A hazard is defined as: A state or set of conditions, internal or external to a system, that has the potential to cause harm. Hazard Analysis is the process of identifying and evaluating existing potential hazards and the recommended mitigations for the hazard sources found. The results of a hazard analysis are typically documented in hazard reports which capture a detailed description of the identified hazard, the planned mitigation or control of the hazard and the planned verification method that will be used to demonstrate that the hazard has been controlled to an acceptable safe level.

Tab 1 - Introduction

Tab 2 - The software safety analysis that may be performed in each life cycle phase to ensure safe, secure software

Tab 3 - The development of the hazard analysis throughout the life cycle

Tab 4 - Hazard Report Contents

Tab 5 - Resources

# 2. Software Safety Analysis

Safety Analysis is defined as a systematic and orderly process for the acquisition and evaluation of specific information pertaining to the safety of a system. Software safety analysis consists of a number of tools and techniques to identify safety risks and formulate effective controls. Some of these techniques are used to help identify the hazards during the Hazard Analysis process, which in turn identifies the software that is safety-critical. The Safety Analysis techniques often used to support the Hazard Analysis are the Software Fault Tree Analysis (SFTA) and the Software Failure Modes and Effects Analysis (SFMEA) which are used to help identify hazards, hazard causes and potential failure modes. The hazards, causes, and failure modes identified using these two techniques are captured in Hazard Reports during the Hazard Analysis.

The hazards identified and captured in the Hazard Reports in safety-critical components then need to be addressed by eliminating  the hazard, typically a design change to remove the hazard altogether or by incorporating hardware or software features ( e.g. monitoring to identify faults and potential failures, providing controls, or other mitigations) that will reduce the risk of a failure. See more information on Hazard Analysis in Tab 3 of this Topic and in [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software), Tab 7.4 in this Handbook.

The Software Fault Tree Analysis (SFTA) is a top-down approach to failure analysis which begins with thinking about potential failures or malfunctions (What could go wrong?) and then thinking through all the possible ways that such a failure or malfunction could occur. Fault Tree Analysis (FTA), is often used by the hardware teams to identify potential hazards that might be caused by failures in hardware components or systems, but with the SFTA, the software isn’t considered the hazard, but it can be a cause or contributor when considered in the context of the system. The SFTA can also be used to analyze the safety of the software design. It is a good way to determine when fault tolerant and fail safe procedures should be initiated. There is a description of how to perform a Fault Tree Analysis in the Assurance and Safety Topics, [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) in this Handbook.

The Software Failure Modes and Effects Analysis (SFMEA) is a bottom up approach where each component is examined and all the possible ways it can fail are listed. Each possible failure is traced through the system to see what effect it might have on the system and to determine if it results in a hazardous state. Then the likelihood of the failure and the severity of the system failure can be considered. This process is time-consuming and can be difficult in large systems, but it is very useful in designing a safe system. The Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) can identify design problems such as:

* Hidden failure modes, system interactions and dependencies
* Unanticipated failure modes
* Unstated assumptions
* Inconsistencies between the requirements and the design

There is a description of how to perform the SFMEA in the Assurance and Safety Topics, Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) in this Handbook.

In every phase of the software life cycle, there are other safety analysis activities and techniques that can be used to help ensure the resulting software system is as safe as possible and meets the primary goals towards that end:

* Ensure that all the hazards have been identified and eliminated or adequately addressed to prevent or safely handle failures
* Ensure that all requirements for the safety features needed to address the hazards have been specified and flowed down to the design
* Ensure that the safety features are correctly and completely defined in the design
* Ensure that the design has correctly captured the intent of the requirements and has developed a design that will produce the desired behavior
* Ensure that the implementation includes the complete design for the safety features
* Ensure that hazard inhibit capabilities have not been violated
* Ensure that hardware independence is not violated
* Ensure that the Fault Detection Isolation and Recovery (FDIR) works as intended

[8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) in the Assurance and Safety Topics section of this Handbook discusses how to ensure that the software and firmware associated with the hazards meets the needs and aligns with the risk of the hazards. This topic also provides some examples where the analysis shows the design is not adequate and needs modification.

* Other software safety analysis activities and techniques are discussed in separate tabs in the life cycle product analyses sections of Topic 8.16 in the Assurance and Safety Tab of Topics. In each of the analyses sections, there is an analysis tab which should be read by personnel working with non-safety-critical software as well as those working with the safety-critical software. There is another analysis tab for each life cycle phase analysis that discusses those techniques that apply more specifically to the safety-critical software analysis. Those personnel working with safety-critical software should be sure to read the safety-critical sections and choose the activities and techniques they feel would be most appropriate for their particular project, considering the risk in the various areas. The specific safety-critical tabs are in the Assurance and Safety Tab of Topics in Topic 8.16 in the analysis products for each phase listed below:
* [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis): Tab 3 – Safety Analysis During Requirements
* [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis): Tab 3 – Safety Analysis During Design
* [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis): Tab 4 – Safety Analysis During Code
* [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) - Tab 5 – Safety Analysis During Test

See also [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements), Topic [6.2 - Checklist for General Software Safety Requirements](/spaces/SWEHBVD/pages/102695554/6.2+-+Checklist+for+General+Software+Safety+Requirements),

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 3. Hazard Analysis

Hazard Analysis occurs throughout the life cycle of a safety-critical software project. The essential elements of each hazard are captured in a hazard report that is built up in stages during the development of the system/software project. Hazard analysis generally needs to be a joint effort with the safety personnel from both the systems and software safety teams. A good hazard analysis requires a thorough understanding of the system and how it will operate as well as an understanding of the software that may cause a hazard or act to monitor, mitigate  or control the hazard.

## 3.1 Relationship of the Safety Phases to Systems and Software Development:

The development of the hazard report is generally tied to the Safety Review phases which are intended to monitor the progress in identifying and addressing all of the hazards in the safety-critical system. There are four Safety Reviews at the end of Phases 0, 1, 2, and 3. The diagram 1.0 shows how these Safety Review Phases typically line up with the system and software life cycle phases.

Diagram 1.0

The following is a general description of what is expected in each of the System Safety Phases:

**Phase 0:** During Phase 0, the **Preliminary Hazard Analysis (PHA)** is developed for the system and:

* Uses a description of the system
* Identifies major high-level hazards, considering loss of control, loss of mission or loss of facilities
* This Safety Review occurs about the point where is system concept is complete and systems requirements are being developed

**Phase 1:** During Phase 1, the PHA is updated and expanded into initial **Hazard Analysis (HA)** and Hazards are recorded in **Hazard Reports**

* At this point, most of the system hazards have been identified, using potential causes and contributors
* Risk of the identified hazards has been identified
* The Phase 1 Safety Review occurs about the point where the system and software requirements are being completed

**Phase 2:** The Hazard Reports are updated

* Mitigations and controls for each hazard are identified
* Methods of verification for each mitigation and control are specified to ensure they will eliminate or reduce the impact of the hazard
* By the Phase 2 Safety Review, most of the system and software design are complete and implementation is underway.

**Phase 3:** Hazard Reports are completed

* By the Phase 3 Safety Review, the tests and hazard verifications identified in Phase 2 have been completed and the results have shown that the hazards are controlled to an acceptable safe level.

## 3.2 Software Involvement in the Hazard Reports/Software Hazard Reports:

(Also, see the detailed information found in [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software), Tab 7.4)

### 3.2.1 Understanding the System:

The first step in identifying software-related hazards or functions is developing a thorough **understanding of the system** to be built. Software Safety personnel should work with the Systems Safety  personnel during the Concepts Phase and Requirements Development Phase to get a better understanding of how the system or software could fail, how the failure might be prevented, and how to mitigate or prevent an accident if a failure occurs. The systems personnel will work with the documentation initially available to make determinations of how the system might fail and document the initial results in a Preliminary Hazard Analysis.

Early documentation  that might be reviewed includes:

* The Concept of Operation
* Generic Hazard Lists (including generic software causes)
* Critical Items List
* Preliminary System Reliability Analysis
* Project/System Risk Analyses
* Request for Proposals
* Computing System Safety Analysis
* Software Security Assessment
* Science Requirements Document
* Requirements and Specification Documents
* Safety analysis from previous similar projects (Often similar projects will have many of the same types of hazards.)
* Checklists

Establish a scope for the hazard analysis. Are there operational boundaries to be included? What phases need to be considered? What other items should be considered (e.g., human actions, software interfaces, utilities), Break the Preliminary Hazard Analysis into manageable groups. Analyze the interaction between the sub-elements. Typically, the PHA is done in teams including members from different roles in the project who have become familiar with the project operations. Using the system understanding they have gained, the team brainstorms possible hazards and records them as hazard statements. Hazard statements are often recorded in the form: Exposure to “something” causes “something undesirable to happen” or failure of “something” causes “something undesirable to happen”.

The **Preliminary Hazard Analysis** will result in a list of hazard causes and a set of possible hazard controls which are used as inputs to develop the initial safety requirements. There is a list of potential software causes in [8.21 - Software Hazard Causes](/spaces/SWEHBVD/pages/109969546/8.21+-+Software+Hazard+Causes) of the Assurance and Safety Topics in this Handbook.

### 3.2.2 Determine Software’s Role in the Hazards

Once there is an initial list of causes and initial safety requirements, more specific hazards can be defined for the systems level. Software safety personnel will help determine the role software has in the defined hazards—Will the software monitor the hazard or is the software a cause, a control or a mitigation of the hazard? Generally, the initial preliminary hazard analysis is followed by the identification of the high-level system hazards and their causes and controls. At this point, the software safety team will be reviewing the **identified hazards with their causes and controls** so they can help identify additional software safety-related hazards, causes and controls.

The software safety team assures that all the software controls identified are included in the set of requirements. These controls may include monitoring the health of equipment, sending alarms or warnings to the operators, identifying faults about to occur or that have occurred and taking mitigating actions, lockouts, verifying input values, error handling, barriers, procedures and many others.

The software related hazards at this point may be documented with the System Hazard analysis reports or they may be documented separately in Software Hazard Reports. Each hazard is documented in a separate hazard report along with its potential risk to the system. The software safety team often does a **Fault Tree Analysis** (FTA) at this point to try to identify any software related hazards that have been overlooked. A Fault Tree analysis is a top-down analysis to help identify the causes of presupposed hazards and is described in detail in Topic [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) of the Assurance and Safety Topics in this Handbook. Another method that can be used to help identify software hazards and failures is the **Software Failure Modes and Effects Analysis (FMEA)**, which is a bottoms-up structured analysis method. This method is covered in detail in Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) of the Assurance and Safety Topics in this Handbook. This method is more time-consuming and can be over-whelming in very large systems.

Hazard Analysis must consider the software’s ability, by design, to cause or control a given hazard. It is a best practice to include the software within the system hazard analysis. The general hazard analysis must consider software common-mode failures that can occur in instances of redundant flight computers running the same software. A common mode failure is a specific type of common cause failure where several subsystems fail in the same way for the same reason. The failures may occur at different times and the common cause could be a design defect or a repeated event.

There are several different perspectives that may be used to think about the specific hazards that may occur in a system. From a system perspective, there are 3 points of view to consider: 1) Physical – where the architectural view shows the system and how it is to be built 2) Functional – which describes what the system is supposed to do to obtain the required system behavior. This looks at the system broken into functions with inputs and outputs and 3) Operational – where the operator interface and the operation of the system are considered, including conditions, limitations, parameters, etc. Other perspectives that should be considered when identifying hazards are: 1) Software - that controls the computer systems 2) Environment – that looks at the various environments encountered by the software 3) Human - considers the human performance in the system and how any errors might affect the system and 4) Organizational -considers any organizational or management actions that might affect the hazards.

### 3.2.3 Analysis Updates During Design

By the time the majority of the design has been completed, the safety teams will be focusing on two primary activities. Each of the hazards must have a **verification method identified** that can be used to show the hazard has been eliminated or mitigated to an acceptable safety level, depending on the risk associated with the hazard. During the design period each hazard should updated to include a verification method that can be used to ensure that the hazard can be controlled by the software mitigation or control. The design should be carefully reviewed to assure that all the hazards identified have been eliminated or controlled by the design. Any changes in the design should be examined to determine whether the changes have caused or exposed any new hazards that had not been captured previously or if any of the changes in design would prevent a control or mitigation to be by-passed or fail. Software is often relied on to work around hardware problems encountered which results in additions and/or changes to functionality. The Hazard Analysis Reports should be updated with any new information.

### 3.2.4 Hazard Analysis Updates During Implementation and Testing

Each Hazard Analysis Report will be updated again during the implementation and testing phases to capture the results of running the verification methods and determining whether the results show that are the controls, mitigations, barriers, etc. are adequate to eliminate or control the hazards they were designed for. Many of the verifications will probably be run during unit testing since many of the functions being tested would be difficult to test in integrated system testing. As in the design phase, any changes to the requirements, design or code during implementation and testing should be analyzed to determine if there is any impact to the safety features or if any new hazards have emerged. Hazard reports (as well as any software documentation, i.e., requirements, design, etc.) need to be updated with any new information. The software should be reassessed during implementation and testing if there are any new concerns that need to be considered (e.g., previously unidentified security concerns). Such changes can easily ripple through the system and impact the safety requirements or features.

When determining if the verifications are adequate, the goal is to confirm  that the accepted hazard controls produce the expected result and do not cause unexpected problems.

### 3.2.5 Hazard Analysis Report Contents

The minimum recommended Hazard Analysis Report Contents detail is found in Tab 4 of this topic.

## 3.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

The following SWEs also have links to this topic:

* [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis)
* [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability)
* [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design)

# 4. Hazard Report Content

The following minimum information on software related hazards will be collected over the phases of the safety analyses and captured in the Hazard Analysis Report (Sometimes called the Safety Data Package)

1. **Description of software incident** scenarios depicting the event(s) or causations **leading to a hazard**, when software is one of the causes or events leading to one or more hazards,
   * Any additional environmental or causational conditions,
   * Any state or mode conditions,
   * Any thresholds or ranges of operation which would trigger a software and/or hardware response
2. **Risk related to the hazard**,
   * The likelihood of each scenario,
   * The potential severity of each scenario,
   * Overall potential risk,
3. **Controls and mitigations,** (including any possible fault or failure tolerance levels to be met)
   * Any barriers, alerts or warnings that are needed
   * Any operational workarounds or controls or other human interactions needed
4. **Verifications needed to prove controls and mitigations work**
   * Proof that the necessary verifications were executed and the results were satisfactory
     + Hazard reports are usually divided into at least 3, often 4, deliveries over the course of project development. These are called “Safety Phases.” Phase 0 delivery includes an introduction to the project and the top hazards and causes. Phase 1 has all known, derived, hazards along with their causes, controls, mitigations and risk assignments.  Phase 2 Hazard Analyses deliveries have the approved controls and mitigations along with the verification and testing methods needed to prove that the controls and mitigations work and that the accepted hazards do not cause problems beyond the expected.  The last delivery of the Hazard Analyses Reports, Phase 3, shows where the planned verifications have been performed and that the controls, mitigations, warnings, barriers, or other safety designs put in place have successfully worked.  For small projects, Phases 0 & 1 are often combined.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-342)

  [STEP Level 2 Overview of Software Safety course,](https://saterninfo.nasa.gov/ "Click to open in new window")

  SMA-SA-WBT-230 SATERN (need user account to access SATERN courses). This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-568)

  [Erroneous Onboard Status Reporting Disabled IMAGE's Radio](https://llis.nasa.gov/lesson/1799 "Click to open in new window")

  Public Lessons Learned Entry: 1799.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Process Asset Templates

**Safety-Specific Process Asset Templates**

Click on a link to download a usable copy of the template. (SftySp)      7/8/2025 - 9 items

**Safety-Specific Process Asset Templates**

* (PAT-004 - )

  [PAT-004 - Safety Requirements Analysis Checklist](https://swehb.nasa.gov/download/attachments/112656824/PAT-004%20-%20Safety%20Requirements%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  8.54 - Software Requirements Analysis, tab 3, Also used in Peer Review Checklists (A.10).
* (PAT-006 - )

  [PAT-006 - Design Practices for Safety](https://swehb.nasa.gov/download/attachments/114327707/Design%20Practices%20for%20Safety.docx?api=v2 "Click to open in new window")

  Topic 6.1, Topic Group: Programming Checklists
* (PAT-007 - )

  [PAT-007 - Checklist for General Software Safety Requirements](https://swehb.nasa.gov/download/attachments/114327720/PAT-007%20-%20Checklist%20for%20General%20Software%20Safety%20Requirements.docx?api=v2 "Click to open in new window")

  Topic 6.2, Topic Group: Programming Checklists
* (PAT-008 - )

  [PAT-008 - Safety Considerations for Design Peer Reviews Checklist](https://swehb.nasa.gov/download/attachments/114328132/Safety%20Considerations%20for%20Design%20Peer%20Reviews%20Checklist%20.docx?api=v2 "Click to open in new window")

  Software Design Analysis, tab 3.2,
* (PAT-009 - )

  [PAT-009 - Software Safety Process Audit](https://swehb.nasa.gov/download/attachments/102695755/Software%20Safety%20Process%20Audit%20Checklist%20Final%20v3.docx?api=v2 "Click to open in new window")

  Topic 8.17, tab 2. This checklist is designed to check the processes in place for performing software safety activities, either in the contract organization or in the in-house organization.
* (PAT-010 - )

  [PAT-010 - Software Safety Activities for Internal Audit](https://swehb.nasa.gov/download/attachments/102695755/SW%20Safety%20Activities%20Checklist%20for%20Internal%20Audits%20Final_v3.docx?api=v2 "Click to open in new window")

  Topic 8.17, tab 3 The Software Safety Activities Checklist for Internal Audits is intended to be used when the software safety personnel are in-house and focuses more on the compliance with the specific required activities for safety-critical software.
* (PAT-032 - )

  [PAT-032 - Considerations When Using Interrupts](https://swehb.nasa.gov/download/attachments/123600994/Considerations%20for%20Interrupt%20Analysis.docx?api=v2 "Click to open in new window")

  Source Code Quality Analysis, tab 4, Also found in Hazard Analysis Assets Process Asset Templates, Implementation Assets Process Asset Templates, and Safety Specific Assets Process Asset Templates
* (PAT-035 - )

  [PAT-035 - Checklist for Safety-Critical or Mission-Critical Software](https://swehb.nasa.gov/download/attachments/180584532/PAT-035%20-%20Checklist%20for%20Safety-Critical%20or%20Mission-Critical%20Software.xlsx?api=v2 "Click to open in new window")

  SWE-134, For use in checking aspects of Safety-Critical or Mission-Critical Software.
* (PAT-044 - )

  [PAT-044 - Software Hazard Development Process Audit](https://swehb.nasa.gov/download/attachments/198770763/PAT-044%20-%20Software%20Hazard%20Development%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Hazard Development Process.

## 5.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [6.2 - Checklist for General Software Safety Requirements](/spaces/SWEHBVC/pages/96174147/6.2+-+Checklist+for+General+Software+Safety+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.21 - Software Hazard Causes](/spaces/SWEHBVD/pages/109969546/8.21+-+Software+Hazard+Causes) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements) |

## 5.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>5</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

## 5.6 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
