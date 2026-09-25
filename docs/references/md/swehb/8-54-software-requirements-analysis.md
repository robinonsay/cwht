# 8.54 - Software Requirements Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695749. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis

8.54 - Software Requirements Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695749)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695749&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. SW Requirements Analysis Techniques](#tabs-2)
* [3. Safety Analysis During Requirements](#tabs-3)
* [4. Requirements Analysis Report](#tabs-4)
* [5. Resources](#tabs-5)

Return to [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products)

# 1. Introduction

The Software Requirements Analysis product focuses on analyzing the software requirements that have been developed from the system requirements. This topic describes some of the methods and techniques Software Assurance and Software Safety personnel may use to evaluate the quality of the software requirements that were developed.

The software requirements process begins with a good understanding of the operational concept, system architecture, and system design. From there, software engineering can begin to derive the requirements for the application, component, feature, etc.

Since the software requirements provide the roadmap for software engineering to build a correct, robust software system/application that meets or exceeds the operational needs of the system, it is key that the requirements adequately reflect what is being requested. It is the role of the Software Assurance and Software Safety (if applicable) Teams to ensure the documented set of requirements is the “best set” of requirements that can be defined by performing a software requirements analysis.

During the software requirements analysis activity, all aspects of the requirements are examined carefully to determine if any improvements are needed before design and implementation begin. There are many tools and techniques that may be used to perform a thorough analysis of the requirements and these are discussed on the various tabs of this topic. NPR 7150.2[083](#_tabs-<p>5</p>)  and NASA-STD-8739.8[278](#_tabs-<p>5</p>) require some specific methods be used for the analysis. Those are listed in the table below.

Many other techniques are available and aid in locating various types of requirements problems. The Software Engineering, Software Assurance, and Software Safety teams should use some of those techniques/methods to supplement the required methods by choosing any of the techniques listed that would benefit their project. Note: Safety Analysis during the requirements development phase is an important part of the requirements analysis for safety-critical systems and as such, it is included in this topic (see tab 3.) Each team performs the required SWEs or SA/Safety activities and then should choose other listed techniques/methods that would help the team do a more thorough job of analyzing the requirements. The results of the analysis and the techniques/methods used are documented in a Software Requirements Analysis Report (including the Software Safety Requirements Analysis).

For safety-critical software, the requirements portion of the Software Safety Analysis should be done in conjunction with the Software Requirements Analysis. See tab **3. Safety Analysis During Requirements** for items to be included.

Many characteristics of the software requirements are considered. Requirements should be: complete, correct, understandable, unambiguous, testable, traceable to the higher-level requirements, consistent, able to meet the user’s expectations, and detailed enough to include boundary conditions, constraints, desired controls, etc.

The information in this topic is divided into several tabs as follows:

* Tab 1 – Introduction
* Tab 2 – SW Requirements Analysis Techniques – lists required and some other possible methods/techniques for requirements analysis
* Tab 3 – Safety Analysis During Requirements – provides additional guidance when safety-critical software is involved with analysis emphasis on safety features
* Tab 4 – Requirements Analysis Report – guidance on reporting the results of the requirements analysis performed
* Tab 5 – Resources for this topic

The following is a list of the applicable SWE requirements that relate to the generation of the Software Requirements Analysis product:

|  |  |  |
| --- | --- | --- |
| **SWE #** | **NPR 7150.2 Requirement [083](#_tabs-<p>5</p>)** | **NASA-STD-8739.8 Software Assurance and Software Safety Tasks [278](#_tabs-<p>5</p>)** |
| 051 | 4.1.3 The project manager shall perform software requirements analysis based on flowed down and derived requirements from the top-level systems engineering requirements, safety and reliability analyses, and the hardware specifications and design. | 1. Perform a software assurance analysis on the detailed software requirements to analyze the software requirement sources and identify any incorrect, missing, or incomplete requirements. |
| 210 | 3.11.8 The project manager shall identify software requirements for the collection, reporting, and storage of data relating to the detection of adversarial actions. | 1. Confirm that the software requirements exist for collecting, reporting, and storing data relating to the detection of adversarial actions. |
| 052 | 3.12.1 The project manager shall perform, record, and maintain bi-directional traceability between the following software elements:   |  |  |  |  | | --- | --- | --- | --- | | Bi-directional Traceability | Class A, B, and C | Class D | Class F | | Higher-level requirements to the software requirements | X |  | X | | Software requirements to the system hazards | X | X |  | | Software requirements to the software design components | X |  |  | | Software design components to the software code | X |  |  | | Software requirements to the software verification(s) | X | X | X | | Software requirements to the software non-conformances | X | X | X | | 1. Confirm that bi-directional traceability has been completed, recorded, and maintained.  2. Confirm that the software traceability includes traceability to any hazard that includes software. |
| 080 | 5.1.3 The project manager shall track and evaluate changes to software products. | 1. Analyze proposed software and hardware changes to software products for impacts, particularly safety and security. |
| 081 | 5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project. | 2. Assess that the software safety-critical items are configuration-managed, including hazard reports and safety analysis. |
| 087 | 5.3.2 The project manager shall perform and report the results of software peer reviews or software inspections for:   a. Software requirements. b. Software plans, including cybersecurity. c. Any design items that the project identified for software peer review or software inspections according to the software development plans. d. Software code as defined in the software and or project plans. e. Software test procedures. | 1. Confirm that software peer reviews are performed and reported on for project activities.   2. Confirm that the project addresses the accepted software peer review findings. |
| 134 | 3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:   a. The software is initialized, at first start and restarts, to a known safe state. b. The software safely transitions between all predefined known states. c. Termination performed by software functions is performed to a known safe state. d. Operator overrides of software functions require at least two independent actions by an operator. e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard. f. The software detects inadvertent memory modification and recovers to a known safe state. g. The software performs integrity checks on inputs and outputs to/from the software system. h. The software performs prerequisite checks prior to the execution of safety-critical software commands. i. No single software event or action is allowed to initiate an identified hazard. j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event. k. The software provides error handling. l. The software can place the system into a safe state. | 1. Analyze the software requirements and the software design and work with the project to implement NPR 7150.2 requirement items "a" through "l."    5. Participate in software reviews affecting safety-critical software products. |
| 184 | 4.1.4 The project manager shall include software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and software in the software requirements documentation. | 1. Analyze and confirm that the software requirements documentation contains the software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and the software. |
| 203 | 5.5.3 The project manager shall implement mandatory assessments of reported non-conformances for all COTS, GOTS, MOTS, OSS, and/or reused software components. | 2. Assess the impact of non-conformances on the project software's safety, quality, and reliability. |

## 1.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 2. SW Requirements Analysis Techniques

NASA Missions go through a logical decomposition in defining their requirements. Software Requirements Analysis addresses a system’s or application’s software requirements including analysis of the functional and performance requirements, hardware requirements, interfaces external to the software, and requirements for qualification, quality, safety, security, dependability, human interfaces, data definitions, user requirements, installation, acceptance, user operation, and user maintenance.

There are several techniques that may be used by either Software Assurance or Software Safety personnel to aid in analyzing these software requirements. NPR 7150.2 [083](#_tabs-<p>5</p>)  and NASA-STD-8739.8 [278](#_tabs-<p>5</p>)  requires some specific techniques be used for the analysis and those are listed in the table on Tab 1. Introduction. It is recommended that at least one other method or technique be selected to supplement the required techniques. Consider the areas where the software requirements are typically weak or where  issues have been found previously and tailor the approach.

This tab contains some checklists and guidance for Software Requirements Analysis. Other guidance to consider while analyzing requirements may be found in this SWE Handbook in tabs 3 and 7 of the following requirements:

* [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability)
* [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)
* [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements)
* [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis)
* [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)

Some methods and techniques are:

## 2.1 Walk-throughs

Walk-throughs establish a common understanding of the system/software requirements and/or operations concept.

1. The following roles are recommended for attendance/participation in the walk-throughs: System Engineers, Software Developers, Software Testers (including IV&V), Software Assurance, Software Safety, System Safety, Operations people, and users.
2. Walk-throughs are intended to give participants a good understanding of the expected data flows through the system/software and the activities to be performed for each operational scenario. This helps determine whether the correct requirements are in place to support all the operational scenarios, data management needs, and helps identify potential system/software hazards.
3. Walk-throughs also provide an opportunity for open discussion of the requirements. These in-depth discussions may lead to the identification of additional requirements as the requirements and their intent are better understood.

## 2.2 Peer Reviews or Formal Inspections

Peer Reviews or Formal Inspections can be used to focus on small sections of concern or to look at potential problem areas of the requirements. For example, a peer review could focus on just correctness or consistency. Here is what is meant by these terms:

**Determine correctness**

Requirements are considered correct if they "respond properly to situations" [001](#_tabs-<p>5</p>)  and are appropriate to meet the objectives of higher-level requirements. A technique for determining correctness is to compare the requirements set against operational scenarios developed for the system/software.

**Determine consistency**

Requirements are consistent if they do not conflict with each other within the same requirements set and if they do not conflict with system (or higher-level) requirements. It is helpful to have at least one person read through the entire set of requirements to confirm the use of consistent terms/terminology throughout.

Peer reviews or formal inspections are particularly important for the areas where software requirements are typically weak and where there is a history of issues found previously. See also Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists), [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures)

## 2.3 Checklists

Several checklists can be used to help analyze requirements. It is often useful to consider using one or more of these to supplement other analysis methods.

### 2.3.1 SA Requirements Analysis Checklist (formerly SAANALYSIS)

**PAT-034 - SA Requirements Analysis Checklist** shown below (previously located in 7.18) is a good general checklist that covers many areas to be considered when performing a requirements analysis.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-034 - SA Requirements Analysis Checklist**

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

Additional checklists below may be used to assist in checking for content, editorial issues and other general requirements issues. Each checklist maybe downloaded by clicking on the thumbnail.

### 2.3.2 Requirements Quality Checklist (PAT-079)

**PAT-079 - Requirements Quality Checklist** shown below contains a number of suggestions to improve the clarity, understandability, and general quality of the requirements. Click on the thumbnail to view the entire set of questions.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-079 - Requirements Quality Checklist**

### 2.3.3 Requirements Contents Checklist (PAT-080)

**PAT-080 - Requirements Contents Checklist** shown below contains questions on various requirements attributes (e.g., clarity, completeness, compliance, consistency, traceability, correctness, feasibility, functionality, performance, interfaces, maintainability, reliability, and verifiability) for consideration. Click on the thumbnail to view the entire set of questions.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-080 - Requirements Contents Checklist**

### 2.3.4 Requirements Editorial Checklist (PAT-081)

**PAT-081 - Requirements Editorial Checklist** contains questions on the proper usage of terms in requirements and some of the common editorial issues in requirements. Click on the thumbnail to view the entire set of questions.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-081 - Requirements Editorial Checklist**

### 2.3.5 Additional Requirements Checklists

When evaluating the software requirements, consider using these additional checklists:

* **[PAT-003 - Functional Requirements Checklist](/spaces/SITE/pages/112656804/PAT-003+-+Functional+Requirements+Checklist)**
* **[PAT-004 - Safety Requirements Analysis Checklist](/spaces/SITE/pages/112656824/PAT-004+-+Safety+Requirements+Analysis+Checklist)**
* **[PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements)**
* **[PAT-013 - Software Requirements Checklist](/spaces/SITE/pages/114328303/PAT-013+-+Software+Requirements+Checklist)**

## 2.4 Bidirectional Traceability

For the basic requirements on bi-directional traceability**,**see[SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) in NASA-STD-8739.8 [278](#_tabs-<p>5</p>). Software Assurance should be confirming that the bi-directional trace is complete and includes traces for all the levels specified in SWE-052.

The requirements traceability matrix identifies all of the system-level and higher-level requirements assigned to the software to be coded. It will also identify the parent requirements.  If a software requirement doesn’t have a parent, it may not be necessary. Traceability is important throughout the full life cycle tracing the requirements allocation to the design, implementation, and test phases. Traceability is particularly important in support of the system/software change or configuration management process. For example, if there is a requirement change during code development, the traceability matrix will help identify the design impacts in the code. The traceability between the requirements and the tests determines whether all the requirements in the system/software are being tested. Similarly, the traceability between the system and software hazards to the software requirements will help determine whether all the hazards are being addressed.

## 2.5 Verify Accuracy of Mathematical Specifications

During the requirements analysis process, the algorithms and mathematical specifications need to be verified to ensure that the inputs to the system/software are computed correctly, and that the specifications and algorithms produce the correct values.

* Ensure that correct units have been specified for all components in the specifications/algorithms.
* Any type conversion limitations should be identified.
* The range of values that are valid for inputs should be specified.

## 2.6 Models and Diagrams

Models and diagrams are techniques that can be used in requirements analysis to assist in getting the best requirements set possible from both the end-user, customer and product perspective. Some are:

* Modeling of inputs and outputs
* Activity Diagram
* Data Flow Diagrams,
* Control Flow Diagrams,
* Scenario-Based/Use Case Models,
* Behavioral-Based Modeling
* Architectural Diagram
* State/Mode Diagram

## 2.7 Reviewing Requirements in Agile - Use Cases, User Stories

(Typically used in Agile)

When using Agile Methodologies, use cases and user stories are used to generate and build the system/software requirements. The user stories/use cases are analyzed to extract the requirements to ensure all of the details are captured. Well written user stories/use cases will contain information that may be used to build the software as well as the Software Requirements Specification (SRS). It is assumed the Product Owner will not provide an SRS. Their mechanism for providing requirements is via user stories/use cases. Note: NASA organizations may develop their higher level requirements in a more traditional Waterfall fashion with the lower-level requirements generated using Agile methodologies.

a. To analyze the requirements in an Agile software development environment, it is important to understand the relationship between user stories and requirements and where use cases fit in.

i. Agile User Stories:

The Agile Alliance describes a user story as work to be done divided into functional increments.

A more simplified definition can be attributed to [Atlassian](https://www.atlassian.com/agile/project-management/user-stories): “A user story is an informal, general explanation of a software feature written from the perspective of the end-user. Its purpose is to articulate how a software feature will provide value to the customer.”

User stories are often used to plan the work in an Agile software development environment. They usually consist of one or two sentences in a specific structure to identify the user, what they want, and why. User stories are all about providing value to the customer. It’s what the user wants (the “results”). Typically, the low-level details will be derived from conversations at Sprint Planning and/or scrum meetings. These details should be captured in the SRS.

ii. Agile Use Cases

Per [Wikipedia](https://en.wikipedia.org/wiki/Use_case), a use case is a list of actions or event steps typically defining the interactions between a role and a system to achieve a goal.

Use cases are often more detailed than user stories. They are all about the “behavior” that is built into the software to meet the customer/user’s needs/goals. Use cases focus on all of the ways the system/software will be used and describe the process/procedures the user takes to accomplish the goal.

iii. When Agile use stories/use cases are used, analysis is still required but may take on a different flavor. They give context to the requirements. When doing requirements analysis in Agile systems, include the following activities:

-Ensure the User Stories are well formulated. To convey the appropriate information, [User Stories](https://www.agilealliance.org/glossary/user-story-template/) are commonly in the form of:

-As a <role>,

-I want <requirement>

-so that <rationale/goal>.

-Ensure that the set of user stories/use cases capture all of the information that may exist in the more traditional forms of requirements.

-Consider how the user stories can be tested and ensure that all the required capabilities can be tested through the user stories.

-Perform bidirectional traces between the traditional Waterfall requirements and the user stories/use cases. Ensure that all safety-critical hazard controls trace to user stories and use cases.

-Review Appendix A in NASA-STD-8739.8 to ensure that all applicable software hazard causes have been considered for inclusion in the user stories and use cases.

b. Requirements have been traditionally used for the NASA systems and software development.

Requirements describe the features of the system being built and convey the user’s expectations. They tend to be very specific and go into detail on how the software should work. Traditionally, the requirements are written by the product manager, the systems engineer, software engineer, or the technical lead. Projects using many of the traditional development methodologies use the written requirements and go directly into the design phase after their requirements analysis. In Agile development where they are provided with high-level NASA requirements, the Product Owner typically breaks the requirements into agile user stories and/or use cases. It is up to Software Engineering to work with the Product Owner to derive the detailed requirements and develop an SRS.

## 2.8 Requirements Analysis Tools

The use of requirements analysis tools (e.g., Innoslate, DOORS) or requirements modeling tools (e.g., Xplenty, IBM Rational, SQL DBM) may be helpful in some analysis activities. Some tools can be used to check the attributes being reviewed.

In FY21, the Software Assurance Research Program (SARP) has two projects researching different aspects of doing requirements analysis including the development of tools. This research may be available for NASA use shortly.

## 2.9 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 3. SW Safety Analysis During Requirements

There are requirements analysis activities that apply specifically to software with safety-critical components. The safety team needs to focus on safety considerations while the requirements analysis is being performed and ensure that these safety-critical aspects have been addressed. The safety requirements analysis portion should be done in conjunction with the software requirements analysis and the results combined in reporting on the analyses results. For additional information on identifying safety related requirements, see the [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) topic. See also [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements),

Software Safety personnel should:

1. Ensure that the requirements analysis discussed in Topic [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) has been performed.
2. Consider using the **Safety Requirements Analysis Checklist**  [PAT-004](#_tabs-<p>5</p>)  below, in addition to the other requirements analysis methods/techniques listed on Tab 2 of this page,  during the safety requirements analysis.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-004 - Safety Requirements Analysis Checklist**

3. Perform a **Fault Tree Analysis** (See Topic [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) for information on performing a Fault Tree Analysis))

4. Consider performing a **Software Failure Modes and Effects Analysis (SFMEA)**or a **Software Failure Modes, Effects and Criticality (SFMECA).** (See Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) for information on performing a **SFMEA**.)

See also [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements), Topic [6.2 - Checklist for General Software Safety Requirements](/spaces/SWEHBVD/pages/102695554/6.2+-+Checklist+for+General+Software+Safety+Requirements),

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Requirements Analysis Report

**Documenting and Reporting of Analysis Results**.

When the requirements are analyzed, the Software Requirements Analysis work product is generated to document results capturing the findings and corrective actions that need to be addressed to improve the overall requirements set. It should include a detailed report of the requirements analysis results. Analysis results should also be reported in a high-level summary and conveyed as part of weekly or monthly SA Status Reports. The high-level summary should provide an overall evaluation of the analysis, any issues/concerns, and any associated risks. If a time-critical issue is uncovered, it should be reported to management immediately so that the affected organization may begin addressing it at once.

When a project has safety-critical software, analysis results should be shared with the Software Safety personnel. The results of analysis conducted by Software Assurance personnel and those done by Software Safety personnel may be combined into one analysis report, if desired.

## **4.1 High-Level Analysis Content for SA Status Report**

Any requirements analysis performed since the last SA Status Report or project management meeting should be reported to project management and the rest of the Software Assurance team. When a project has safety-critical software, any analysis done by Software Assurance should be shared with the Software Safety personnel.

When reporting the results of an analysis in a SA Status Report, the following defines the minimum recommended contents:

* Identification of what was analyzed: Mission/Project/Application
* Period/Timeframe/Phase analysis performed during
* Summary of analysis techniques used
* Overall assessment of design, based on analysis
* Major findings and associated risk
* Current status of findings: open/closed; projection for closure timeframe

## **4.2 Detailed Content for Analysis Product:**

The detailed results of all software requirements analysis activities are captured in the Software Requirements Analysis product along with the types of analysis techniques used to provide information on the robustness of the analysis done. The techniques/methods used provide information on those that produced the most useful results . This document is placed under configuration management and delivered to the project management team as the Software Assurance record for the activity. When a project has safety-critical software, this product should be shared with the Software Safety personnel.

When reporting the detailed results of the software requirements analysis, the following defines the minimum recommended content:

* Identification of what was analyzed: Mission/Project/Application
* Person(s) or group/role performing the analysis
* Period/Timeframe/Phase analysis performed
* Documents used in analysis (e.g., versions of the system and software requirements, interfaces document, Concept of Operations)
* A high-level scope and description of the techniques/methodologies used in the analysis
  + Use the list of possible analysis techniques/methodologies listed in Tab 2 as a starting point.
  + For each technique/methodology on the list, state why/or why not it was used.
  + List any additional techniques/methodologies used that were not included in the Tab 2 list.
* Summary of results found using each technique/methodology
  + How many findings resulted from each technique/methodology?
  + Difficulty/Ease of technique/methodology used
  + The general assessment of the technique/methodology
  + High-Level Summary of the findings
* Results, major findings, and associated risk:
  + Overall assessment of the quality/completeness of the requirements, based on the analysis
  + Either list each result, finding, or corrective action or summarize them and list the links to the detailed findings.
  + Assessment of the overall risk involved with the findings.
* Documentation should include types of findings:
  + Missing requirements
  + Requirements that need rewriting: because they are incomplete, incorrect, unclear, not testable/verifiable, etc.
  + Requirement with safety concerns
  + Requirements with security concerns (e.g., access control, vulnerabilities, weaknesses, etc.)
  + Incompatibilities in interfaces not clearly defined
  + Issues in traceability (Child with no parent, parent with no children, etc.)
  + Requirements with unnecessary functions
  + Requirements are not detailed enough to provide the information needed to develop a detailed design that can be implemented in the code
  + Hazards and safety-related software controls, constraints, features not included in the requirements
  + Any other requirements issues discovered during the analyses
* Minor findings
* Current status of findings: open/closed; projection for closure timeframe
  + Include counts for those discovered by SA and Software Safety
  + Include overall counts from the Project’s problem/issue tracking system.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Process Asset Templates

Click on a link to download a usable copy of the template.

* (PAT-003 - )

  [PAT-003 - Functional Requirements Checklist,](https://swehb.nasa.gov/download/attachments/112656804/PAT-003%20-%20Functional%20Requirements%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, Tab 4,
* (PAT-004 - )

  [PAT-004 - Safety Requirements Analysis Checklist](https://swehb.nasa.gov/download/attachments/112656824/PAT-004%20-%20Safety%20Requirements%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  8.54 - Software Requirements Analysis, tab 3, Also used in Peer Review Checklists (A.10).
* (PAT-007 - )

  [PAT-007 - Checklist for General Software Safety Requirements](https://swehb.nasa.gov/download/attachments/114327720/PAT-007%20-%20Checklist%20for%20General%20Software%20Safety%20Requirements.docx?api=v2 "Click to open in new window")

  Topic 6.2, Topic Group: Programming Checklists
* (PAT-013 - )

  [PAT-013 - Software Requirements Checklist,](https://swehb.nasa.gov/download/attachments/114328303/PAT-013%20-%20Software%20Requirements%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.1, Also in Peer Review and Requirements Analysis categories.
* (PAT-034 - )

  [PAT-034 - SA Requirements Analysis Checklist](https://swehb.nasa.gov/download/attachments/154501148/PAT-034%20-%20SA%20Requirements%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, Tab 2.3.1 - SA Requirements Analysis Checklist
* (PAT-079 - )

  [PAT-079 - Requirements Quality Checklist](https://swehb.nasa.gov/download/attachments/207290572/PAT-079%20-%20Requirements%20Quality%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.2 Requirements Quality Checklist
* (PAT-080 - )

  [PAT-080 - Requirements Contents Checklist](https://swehb.nasa.gov/download/attachments/207290574/PAT-080%20-%20Requirements%20Content%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.3 Requirements Contents Checklist
* (PAT-081 - )

  [PAT-081 - Requirements Editorial Checklist](https://swehb.nasa.gov/download/attachments/207290577/PAT-081%20-%20Requirements%20Editorial%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.4 Requirements Editorial Checklist The purpose of this checklist is to aid the analyst when reviewing the software requirements from an editorial perspective.

## 5.4 Checklists and Guidance

There are many lists of guidance items and checklists in this Handbook, but sometimes they are very difficult to locate. The table below is intended to help users find the assets they need more easily. Most of the lists provided here are intended to be guidance for activities and could be used as a self-check to see whether all the expected items have been included in the activity. The items that are noted as checklists can be used as audit checklists. Some are already formatted and can be downloaded directly for tailoring and use. Others are in the process of being formatted so they can be downloaded. Note: Currently, this list does not include every guidance list in the Handbook, but it has a good sampling of them.

## Checklists and Guidance Lists in SWEHB

| **Asset Name** | **Location** | **Format** | **Category** |
| --- | --- | --- | --- |
| Maintenance, Operations, Retirement Planning | [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement), Tab 3, (7.4 -Retirement) | List | Late Phase Planning Considerations |
| Auto-generated Code | [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code), Tab 3 | List | Implementation, Planning |
| Selection of Real Time Operating System (RTOS) | [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software), Tab 3 | Checklist | Commercial & Legacy SW |
| Selection of Real Time Operating System (RTOS) | [6.3 - Checklist for Choosing a Real Time Operating System (RTOS)](/spaces/SWEHBVD/pages/102695560/6.3+-+Checklist+for+Choosing+a+Real+Time+Operating+System+RTOS) Programming Practices Topic,  6.3 | Checklist | Programming Checklists, Planning, Commercial SW |
| Choosing Off-the Shelf (OTS) Software | [6.4 - Checklist for Choosing Off-The Shelf Software (OTS)](/spaces/SWEHBVD/pages/102695563/6.4+-+Checklist+for+Choosing+Off-The+Shelf+Software+OTS) - Assurance & Safety Topics, Programming Tab, 6.4 | Checklist | Commercial & Legacy SW |
| Selection of Commercial & Legacy SW | [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software), Tab 3 | Questions | Commercial & Legacy SW |
| Assurance of models, simulations, analysis tools | [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools).  Tab 7.4 | List | Models, Sims, Tools |
| Requirements Development/Assessment (SRS contents) | [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) , Tab 7.4 | Questions (2 sets) | Requirements development |
| Requirements Analysis | [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis), Tab 3;  Topic 8.16: [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis), tab 2 | Checklist: SAANALYSIS | Requirements Analysis |
| Requirements Development/Assessment | [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements), Tab 7.4 | List of SRS contents, Questions (2 sets) for requirements considerations | Requirements development |
| Analysis of Requirements Changes | [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes), Tabs 3, 7.4 | List | Requirements practices |
| Checklist for General SW Safety Requirements | [6.2 - Checklist for General Software Safety Requirements](/spaces/SWEHBVD/pages/102695554/6.2+-+Checklist+for+General+Software+Safety+Requirements)  Topics, Programming Practices Tab, 6.2 | Checklist | Safety Requirements |
| Configuration Items for Consideration | [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan), Tab 3 | List | Configuration Management |
| Functional Configuration Audit Checklist (FCA) | [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits), Tab 7 | Checklist | Configuration Management |
| Physical Configuration Audit (PCA) | [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits), Tab 7 (Not currently there) | Checklist | Configuration Management |
| Peer Review Best Practices | [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), Tab 3 | List | Peer Review Guidance |
| SA Non-Conformance Activities | [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances), Tab 7.4 | List | Non-Conformance Handling Guidance |
| Change Evaluation | [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes), tab 3 | List | Guidance for handling changes |
| Design Considerations | [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design), Tab 3, 7.4 | Checklist | Design Practices |
| Design Evaluation (SARB) | [SWE-143 - Software Architecture Review](/spaces/SWEHBVD/pages/102695501/SWE-143+-+Software+Architecture+Review), Tab 3, 7.4 | Questions | Design Practices |
| Software Design Analysis | [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis)  Assurance & Safety Topics, 8.16, Tab Software Design Analysis | Checklist | Design Practices |
| Design for Safety | [6.1 - Design for Safety Checklist](/spaces/SWEHBVD/pages/102695551/6.1+-+Design+for+Safety+Checklist)  Assurance & Safety Topics, 6.1 | Questions | Design Practices |
| C Programming Practices for Safety | [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software), Tab 3, 7.4 | Checklist | Safety Coding Practices |
| C Programming Practices for Safety | [6.5 - Checklist for C Programming Practices](/spaces/SWEHBVD/pages/102695570/6.5+-+Checklist+for+C+Programming+Practices)  Programming Practices Topic, 6.5 | Checklist | Safety, Coding Practices |
| C++ Programming Practices for Safety | [6.6 - Checklist for C++ Programming Practices](/spaces/SWEHBVD/pages/102695576/6.6+-+Checklist+for+C+Programming+Practices)  Programming Practices Topic, 6.6 | Checklist | Safety, Coding Practices |
| Ada Programming Practices for Safety | [6.7 - Checklist for Ada Programming Practices](/spaces/SWEHBVD/pages/102695582/6.7+-+Checklist+for+Ada+Programming+Practices)  Programming Practices Topic, 6.7 | Checklist | Safety, Coding Practices |
| FORTRAN Programming Practices for Safety | [6.8 - Checklist for Fortran Programming Practices](/spaces/SWEHBVD/pages/102695586/6.8+-+Checklist+for+Fortran+Programming+Practices)  Programming Practices Topic, 6.8 | Checklist | Safety, Coding Practices |
| Generic (Non-Language Specific) Programming Practices for Safety | [6.9 - Checklist for Generic (Non-Language-Specific) Programming Practices](/spaces/SWEHBVD/pages/102695593/6.9+-+Checklist+for+Generic+Non-Language-Specific+Programming+Practices)  Programming Practices Topic, 6.9 | Checklist | Safety, Coding Practices |
| General Good Programming Practices for Safety | [6.10 - Checklist for General Good Programming Practices](/spaces/SWEHBVD/pages/102695600/6.10+-+Checklist+for+General+Good+Programming+Practices)  Programming Practices Topic, 6.10 | Checklist | Safety, Coding Practices |
| ISO 27001-2013 Audit Checklist | Assurance & Safety Topics, 8.16, 5.2.2 | Checklist | Audit |
| Software Safety Process Audit | [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists)  Assurance & Safety Topics -8.17, Tab 2 | Checklist | Safety, Audits |
| Software Safety Activities for Internal Audit | [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists)  Assurance & Safety Topics – 8.17, Tab 3 | Checklist | Safety, Audits |
| Software Safety-Specific Activities in Each Phase | [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase)  Assurance & Safety Topics – 8.20, Tab 1 | List | Safety |
| Hazard Reports | [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software), Tab 7.4 | Steps in hazard Analysis | Safety |
| Potential Software Hazard Causes | [8.21 - Software Hazard Causes](/spaces/SWEHBVD/pages/109969546/8.21+-+Software+Hazard+Causes)  Assurance & Safety Topics – 8.21, Tab 1 | Table | Safety, Hazard Analysis |
| Considerations for identifying SW Hazard Causes | [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software), Tab 7.4 | Checklist | Safety, Hazard Analysis |
| Considerations for Identifying SW Causes in a General SW-Centric HA | [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software), Tab 7.4 | List | Safety, Hazard Analysis |
| Updates to Test Documents | [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures), Tabs, 3, 7.4 | List | Testing Guidance |
| Analysis of test results | [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results), Tab 3 | List | Test Analysis |
| Test Practices (incl. safety) | [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), Tab 3, | List | Test Analysis |
| Test Documentation Changes | [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) | List | Test Documentation |
| Unit test guidance | [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability), Tabs 3, 7.4  Repeated in [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) | List | Test Results, Unit Testing |
| Release Package Activities | [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management), Tab 3 | List | Release Guidance |
| Confirmation of Delivery Activities | [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products), Tab 7 | List | Delivery Activities |

## 5.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements)       * [5.21 - Software Requirements Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641581/5.21+-+Software+Requirements+Analysis+Report+Minimum+Content) * [6.2 - Checklist for General Software Safety Requirements](/spaces/SWEHBVC/pages/96174147/6.2+-+Checklist+for+General+Software+Safety+Requirements) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis)  * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [PAT-004 - Safety Requirements Analysis Checklist](/spaces/SITE/pages/112656824/PAT-004+-+Safety+Requirements+Analysis+Checklist) * [PAT-007 - Checklist for General Software Safety Requirements](/spaces/SITE/pages/114327720/PAT-007+-+Checklist+for+General+Software+Safety+Requirements) * [PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist) |

## 5.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>5</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements) |

## 5.7 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) |
