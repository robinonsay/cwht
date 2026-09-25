# 8.55 - Software Design Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695748. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis

8.55 - Software Design Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695748)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695748&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Design Analysis Guidance](#tabs-2)
* [3. Safety Analysis During Design](#tabs-3)
* [4. Analysis Report Content](#tabs-4)
* [5. Resources](#tabs-5)

Return to [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products)

# 1. Introduction

The Software Design Analysis product focuses on analyzing the software design that has been developed from the requirements (software, system, and/or interface). This topic describes some of the methods and techniques Software Assurance and Software Safety personnel may use to evaluate the quality of the architecture and design elements that was developed.The Software Design Analysis product focuses on analyzing the software design that has been developed from the requirements (software, system, and/or interface). This topic describes some of the methods and techniques Software Assurance and Software Safety personnel may use to evaluate the quality of the architecture and design elements that was developed.

The software design process begins with a good understanding of the requirements and the system architecture and system design. The architectural design begins with the development of a basic architecture and a high-level preliminary design. The architectural design is then expanded into a low-level detailed design. By the time the detailed design is complete, software engineering should be able to implement it into the code of the desired software system or application.

Since the design primarily guides the code implementation, it is important to ensure that the architecture and design are correct, safe, secure, complete, understandable, and captures the intent of the requirements. The detailed design captures the low-level component-based approach to implementing the software requirements, including the requirements associated with fault management, security, and safety. When the detailed design is complete, the analysis of the requirements traceability documents should show the relationship between the software design components and the software requirements providing evidence that all requirements are accounted for. The information in this topic is divided into several tabs as follows:

* Tab 1 – Introduction
* Tab 2 – Software Design Analysis Guidance – provides general guidance for doing software design analysis
* Tab 3 – Safety Analysis During Design – provides additional guidance when safety-critical software is involved with analysis emphasis on safety features
* Tab 4 - Analysis Reporting Content – provides guidance on the analysis report product content
* Tab 5 – Resources for this topic

The following is a list of the applicable SWE requirements that relate to the generation of the software design analysis product:

|  |  |  |
| --- | --- | --- |
| **SWE #** | **NPR 7150.2 Requirement [083](#_tabs-<p>5</p>)** | **NASA-STD-8739.8 Software Assurance and Software Safety Tasks [278](#_tabs-<p>5</p>)** |
| 034 | 3.1.5 The project manager shall define and document the acceptance criteria for the software. | 1. Confirm software acceptance criteria are defined and assess the criteria based on guidance in the NASA Software Engineering Handbook, NASA-HDBK-2203. |
| 134 | 3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:   a. The software is initialized, at first start and restarts, to a known safe state. b. The software safely transitions between all predefined known states. c. Termination performed by software functions is performed to a known safe state. d. Operator overrides of software functions require at least two independent actions by an operator. e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard. f. The software detects inadvertent memory modification and recovers to a known safe state. g. The software performs integrity checks on inputs and outputs to/from the software system. h. The software performs prerequisite checks prior to the execution of safety-critical software commands. i. No single software event or action is allowed to initiate an identified hazard. j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event. k. The software provides error handling. l. The software can place the system into a safe state. | 1. Analyze the software requirements and the software design and work with the project to implement NPR 7150.2 requirement items "a" through "l."    4. Analyze the software design to ensure the following:    a. Use of partitioning or isolation methods in the           design and code,    b. That the design logically isolates the safety-critical           design elements and data from those that are           non-safety-critical.      5. Participate in software reviews affecting safety-critical software products.    6. Ensure the SWE-134 implementation supports and is consistent with the system hazard analysis. |
| 057 | 4.2.3 The project manager shall transform the requirements for the software into a recorded software architecture. | 1. Assess that the software architecture addresses or contains the software structure, qualities, interfaces, and external/internal components.  2. Analyze the software architecture to assess whether software safety and mission assurance requirements are met. |
| 143 | 4.2.4 The project manager shall perform a software architecture review on the following categories of projects:   a. Category 1 Projects as defined in NPR 7120.5. b. Category 2 Projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4. | 1. Assess the results of or participate in software architecture review activities held by the project. |
| 058 | 4.3.2 The project manager shall develop, record, and maintain a software design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested. | 1. Assess the software design against the hardware and software requirements and identify any gaps.  2. Assess the software design to verify that the design is consistent with the software architectural design concepts and that the software design describes the lower-level units to be coded, compiled, and tested.   3. Assess that the design does not introduce undesirable behaviors or unnecessary capabilities.  4. Confirm that the software design implements all of the required safety-critical functions and requirements.   5. Perform a software assurance design analysis. |
| 080 | 5.1.3 The project manager shall track and evaluate changes to software products. | 1. Analyze proposed software and hardware changes to software products for impacts, particularly safety and security. |
| 081 | 5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project. | 2. Assess that the software safety-critical items are configuration-managed, including hazard reports and safety analysis. |
| 203 | 5.5.3 The project manager shall implement mandatory assessments of reported non-conformances for all COTS, GOTS, MOTS, OSS, and/or reused software components. | 2. Assess the impact of non-conformances on the project software's safety, quality, and reliability. |

## 1.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 2. Software Design Analysis Guidance

In software design, software requirements are transformed into the architectural design with a software architecture and a high-level preliminary design followed by the more specific detailed software design. The architecture establishes the interfaces, overall layout/structure, and data flow of the software. The high-level preliminary design identifies the specific individual components (e.g., files, functions, subroutines, classes, modules) for each software program/application along with a description of what that piece does. In addition, it should include items such as the inputs, outputs, units, and data types along with databases and interfaces (e.g., hardware, operator/user, software program/applications, system and subsystems).

The detailed design takes the high-level components, files, functions, subroutines, classes, etc. and breaks them down to the point where they become pseudo-code with variable names and associated descriptions identified and the logic flow stubbed out. As project budgets tighten, more and more software organizations are embedding the detailed design in the source code and extracting it with tools like [Javadoc](https://www.oracle.com/java/technologies/javase/javadoc.html) and [Doxygen](https://www.doxygen.nl/index.html). (Note: This is not an endorsement of these tools.) So, Software Assurance and Software Safety personnel should be aware they may receive the detailed design documentation in a less traditional manner. For small software systems, the architectural and detailed design may be combined.

The design addresses the software architectural design and software detailed design.  The objective of doing design analysis is to ensure that the design:

* is a correct, accurate, and complete transformation of the software requirements that will meet the operational needs under nominal and off-nominal conditions,
* is safe,
* is secure with known weaknesses and vulnerabilities mitigated,
* introduces no unintended features, and
* does not result in unacceptable operational risk.

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

The design should also be created considering portability, performance, and maintainability so future changes can be made quickly without the need for significant redesign.

There are several **design techniques** described below that help with the analysis of the design. Each of these may be used by Software Assurance and Software Safety personnel to help ensure a more robust design. Additionally, these personnel should be aware of the [D. Topics](/spaces/SWEHBVD/pages/102695224/D.+Topics) section – [9.01 Software Design Principles](/spaces/SWEHBVD/pages/102695790/9.01+Software+Design+Principles) – that addresses specific aspects of the design.

Tab 3 (Safety Analysis During Design) contains a more extensive list of analysis techniques that may be used by the Software Safety personnel.

Software Assurance and Software Safety tasks in NASA-STD-8739.8[278](#_tabs-<p>5</p>) that relate to design analysis are found in [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability), [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design), [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software), [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements), and [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access).

## 2.1 Use of Checklists and Known Best Practices

As part of the design analysis, Software Assurance and Software Safety personnel review the design to ensure that general design best practices have been implemented (see below). The use of the **SADESIGN Checklist** [PAT-021](#_tabs-<p>5</p>)  (see below) is important when evaluating the software design as it highlights many best practices. There are other aids in this Handbook that may be used for evaluating the design. They are the Programming Checklists Topic: [6.1 - Design for Safety Checklist](/spaces/SWEHBVD/pages/102695551/6.1+-+Design+for+Safety+Checklist) and the Software Design Principles Topic: [9.01 Software Design Principles](/spaces/SWEHBVD/pages/102695790/9.01+Software+Design+Principles). This information should be considered during the analysis for both safety-critical software and non-safety-critical software. Teams may decide to formulate some of this information into a checklist that is applicable to their project.

**General Design Best Practices:**

Some general design best practices to consider are:

* Break the design into smaller chunks. Don’t try to design it all at once.
* Keep the design simple.
* Keep the design modular so it will be easier to test and maintain.
* Keep boundaries, interfaces, and constraints in mind.
* Strive for maximum cohesion and minimum coupling. (Cohesion groups together the things that make sense; coupling is the relative dependence between the modules)
* Use abstraction to increase the reusability of modules. (Abstraction is the reduction of a body of data to a simplified representation of the whole.)
* Consider how the users will use and interact with the system. Keep the user interface design user friendly.
* Include error handling in the designs.
* Don’t duplicate sections of code – if the sections of code need to be used repeatedly, put them into a function, a package, or subroutine that can be called.
* Prototype new approaches or designs for difficult requirements.
* Peer review designs, particularly interfaces, data flows, and logic flows.
* Use design practices such as documentation review, pseudo code, process diagrams, and logic diagrams to aid in evaluating the design.

See also Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists)

Additional guidance and some key design practices may also be found in [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design), tab 7.

SADESIGN Checklist [PAT-021](#_tabs-<p>5</p>)is included below:

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-021 - SADESIGN Checklist**

## 2.2 Use of peer reviews or inspections

Design items designated in the software management/development plans are peer reviewed or inspected. Some of the items to look for during these meetings are:

1. Assess the software design against the hardware and identify any gaps.
2. Assess the software design against the system requirements and design and identify any gaps.
3. Confirm that the detailed design is consistent with the architectural design and describes the program’s or application’s components at a low enough level for coding.
4. Confirm the design does not contain undesirable functionality.
5. Confirm the safety-related requirements (e.g., [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)) have been taken into account for safety-critical software.
6. Confirm the design addresses possible unauthorized access, vulnerabilities, and weaknesses.

## 2.3 Review of Traceability Matrices

Review the traces from requirements to design and design to requirements to ensure all requirements are completely accounted for. As the project moves into implementation, the bi-directional traceability matrices between design and code should also be checked.

## 2.4 Software Architecture Review Board (SARB) Analysis - applies to NASA projects only

The [Software Architecture Review Board](https://nen.nasa.gov/web/sarb) (SARB) is a NASA-wide board that engages with flight projects in the formative stages of the software architecture. The objectives of the SARB are to manage and/or reduce flight software complexity through better software architecture and help improve mission software reliability and save costs. NASA projects that meet certain criteria (for example, large projects, ones with safety-critical concerns, projects destined for considerable reuse, etc.) may request the SARB to do a review and assessment of their architecture. For more guidance on the focus areas of the SARB, see the [SWE-143 - Software Architecture Review](/spaces/SWEHBVD/pages/102695501/SWE-143+-+Software+Architecture+Review) – Tab 3 in this Handbook. For more information on the SARB or to request a review, please visit the [SARB site](https://nen.nasa.gov/web/sarb) on the NASA Engineering Network (NEN).

### 2.4.1 Preparing for a Software Architecture Review (SARB) Checklist [PAT-023](#_tabs-<p>5</p>)

The checklist below is checklist that can be used for projects to help prepare for a review by the Software Architecture Review Board. Note: Include below should include the attachment that has the name change to match the change in the PAT.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-023 - Preparing for a SARB Checklist**

### 2.4.2 Checklists used for an actual Software Architecture Review (with and without guidance)

The checklist below, the Software Architecture Review Board (SARB) Checklist, is the full checklist used by the SARB team. Two versions of this checklist are included – One with just the checklist questions and one that includes the corresponding guidance for each question, the SARB Review Checklist with Guidance. For each checklist you can click on the image to get a preview and the full checklists can be downloaded from the images. The checklist with the guidance is quite long, so only the first page will be shown below.

**Software Architecture Review Board Checklist** [PAT-029](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-029 - Software Architecture Review Board Checklist**

**SARB Review Checklist with Guidance** [PAT-030](#_tabs-<p>5</p>)

Only first page is shown here. This template is over 20 pages long. Download a copy of the Word doc to see all pages.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-030 - SARB Review Checklist with Guidance**

### **2.4.3 Evidence that Design Analysis has been performed**

In order to demonstrate that the Design Analysis has been performed, the checklist below should be completed and saved. This checklist contains the most critical activities that should be performed during design analysis.

**PAT-031 - Critical Design Analysis Checklist** [PAT-031](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-031 - Critical Design Analysis Checklist**

## 2.5 Problem/Issue Tracking System

Per [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) – Task 2, all analysis non-conformances, findings, defects, issues, concerns, and observations are documented in a problem/issue tracking system and tracked to closure. These items are communicated to the software development personnel and possible solutions discussed. The level of risk associated with the finding/issue should be reflected in the priority given in the tracking system. The analysis performed by Software Assurance and Software Safety may be reported in one combined report, if desired.

## 2.6 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 3. Safety Analysis During Design

The Safety Design Analysis is a portion of the overall Software Safety Analysis that is performed on all safety-critical software, as defined in NASA-STD-8739.8 [278](#_tabs-<p>5</p>). A full Software Safety Analysis encompasses all the aspects of the development life cycle (requirements, design, implementation, and test) for safety-critical software and focuses on the safety features (safety requirements, controls, mitigations, fault identification, isolation and recovery, etc.). During the Design phase, Software Safety personnel analyze the design to ensure that it will not adversely impact the safety of the system/software. This tab discusses the Software Safety Analysis activities during design.

## 3.1 Review Software Design Analysis Information

To begin the Safety Design Analysis, the Software Safety and SA personnel should collaborate on the activities on **Tab 2 – Software Design Analysis Guidance**. However, Software Safety personnel should perform an independent analysis to become familiar with the design. Both teams should review each other’s Software Design Analysis results to ensure that all safety aspects have been adequately considered and addressed in the software design. In addition to the techniques and activities on Tab 2, it may be useful to use any of the following information for analyzing safety-critical software:

1. Topic [6.1 - Design for Safety Checklist](/spaces/SWEHBVD/pages/102695551/6.1+-+Design+for+Safety+Checklist) found in this Handbook, under the “Programming Checklists” Tab of Topics   
   ([PAT-006 - Design Practices for Safety](/spaces/SITE/pages/114327707/PAT-006+-+Design+Practices+for+Safety))  
   and
2. “[9.01 Software Design Principles](/spaces/SWEHBVD/pages/102695790/9.01+Software+Design+Principles)” Tab of Topics in this Handbook.

After reviewing the analysis work done to date and the applicable checklists, examine the various operational scenarios (nominal and off-nominal) for what could go wrong with the mission or if the software (or hardware) fails. (This scenario information may be in a preliminary Hazard Report; however, some of the scenarios may not have been identified yet and are a product of this exercise.) Review the Software Design to see if the mishaps or failures are accounted for. It may be necessary to reverse engineer the scenarios to ensure that the software design accounts for them and has the proper hooks in place to deal with any faults or failures.

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

## 3.2 Design Peer Reviews or Walk-throughs

Peer reviews or walk-throughs for safety-critical components are recommended techniques to aid in identifying software design problems or issues in safety-critical components early. These meetings allow problems and issues to be revealed and worked prior to design rollout at Milestone Reviews (e.g., Preliminary, Critical). Software Safety personnel participate in these meetings to monitor and analyze the safety aspects of the software design including any changes, and to continue updating their hazard analysis (see [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) product).

One of the most important aspects of a design for safety-critical software is to design for minimum risk. “Minimum risk” includes the hazard risks (including loss of life, mission, and space assets), security risks, design choice risks, human errors, and other types of risk such as programmatic, cost, schedule, etc. When possible, the design should eliminate or mitigate identified hazards and risks or reduce the associated risk through design (e.g., redundancy, isolating safety-critical software).

Listed below are some ways to mitigate or reduce risks through software design. This list may be used by meeting attendees to help evaluate the design with respect to safety and risk considerations.

The checklist below provides: **Safety Considerations for Design Peer Reviews**  [PAT-008](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-008 - Safety Considerations for Design Peer Reviews Checklist**

## 3.3 Other Types of Design Analysis

There are other types of analyses that may be useful during design but require more time and effort to perform. The Safety Team should consider them and choose those they feel would provide the most value, depending on the areas where risk is highest in the design. Some of these design analysis methods are:

1. **Acceptable Level of Safety:**Once the design is fairly mature, a design safety analysis may be done to determine whether an **acceptable level of safety** will be attained by the designed system. This analysis involves analyzing the design of the safety components to ensure that all safety requirements are specified correctly. Check to assure the requirements are updated once the design has determined exactly what safety features will be included in the system/software. Review the design looking for places and conditions that lead to unacceptable hazards. Consider the credible faults or failure that could occur and evaluate their effects on the designed system. Does the designed system produce the desired result with respect to the hazards? Think about what the system will do for all the “what if” cases and trace through how the system would respond—Did it respond in a safe manner?
2. **Prototyping or simulating:**Prototyping or simulating parts of the design may show where the software can fail. In addition, this can demonstrate whether the software can meet the constraints it might have, such as response time, or data conversion speed. This could also be used to provide the operator’s inputs on the user interface. If the prototypes show that a requirement cannot be met, the requirement must be modified or the design revised.
3. **Independence Analysis:**To perform this analysis, map the safety-critical functions to the software components, and then map the software components to the hardware hosts and FCRs. All the input and output of each safety-critical component should be inspected.  Consider global or shared variables, as well as the parameters directly passed.  Consider “side effects” that may be included when a component is run. The goal is to verify there is separation between safety-critical and non-safety-critical functions.
4. **Design Logic Analysis:**Logic analysis examines the safety-critical areas of a software component by analyzing each function performed by that component.  If it responds to or has the potential to violate one of the safety requirements, it should be considered critical and undergo logic analysis. Design Logic Analysis (DLA) evaluates the equations, algorithms, and control logic in the software design of these safety-critical components. A technique for performing design logic analysis is to compare design descriptions and logic flows and then note the discrepancies. This is the most rigorous type of analysis and may be performed using Formal Methods. Formal Methods are the use of mathematical modelling for the specification, development, and verification of systems in both software and electronic hardware. The formal methods are used to ensure these systems are developed without error. Less formal DLA involves reviewing a relatively small quantity of critical software products (e.g., PDL, prototype code) and manually tracing the logic. Safety-critical logic can include failure detection and diagnosis, redundancy management, variable alarm limits, and command inhibit logical preconditions.
5. **Design Data Analysis:**Data analysis ensures that the structure and intended use of data will not violate a safety requirement by comparing the description to the use of each data item in the design logic. The Design Data Analysis evaluates the description and intended use of each data item in the software design. Interrupts and their effect on data must receive special attention in safety-critical areas. Analysis should verify that interrupts and interrupt handling routines do not alter critical data items used by other routines. The integrity of each data item should be evaluated with respect to its environment and host. Shared memory and dynamic memory allocation can affect data integrity. Data items should also be protected from being overwritten by unauthorized applications.
6. **Design Interface Analysis**: The Design Interface Analysis verifies the proper design of a software component's interfaces with other components of the software, system, or even hardware. This analysis will verify that the software component's interfaces, especially the control and data linkages, have been properly designed. Interface requirements specifications (which may be part of the requirements or design documents, or a separate document) are the sources against which the interfaces are evaluated. Interface characteristics to be addressed should include inter-process communication methods, data encoding, error checking (e.g., data entry validity, value/range, type checks), and synchronization.

   The analysis should consider the validity and effectiveness of checksums, cyclic redundancy checks (CRCs), and error correcting code. CRC is a type of error-detecting code used in digital networks and storage devices to detect unintentional changes to raw data. Blocks of data entering these systems get a short check value attached, based on the remainder of a polynomial division of their contents. When the data is retrieved, the calculation is repeated and if the check values do not match, the data is corrupt and corrective action can be taken.  
     
   The sophistication of error checking or correction that is implemented should be appropriate for the predicted bit error rate of the interface.  An overall system error rate should be defined and budgeted to each interface.

   Examples of some possible interface problems [PAT-020](#_tabs-<p>5</p>)  are below:

   Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

   **PAT-020 - Examples of Interface Problems**
7. **Design Traceability Analysis**: This analysis ensures that each safety-critical software requirement is included in the design. Tracing the safety requirements throughout the design (and eventually into the source code and test cases) is vital to making sure that no requirements are lost, that safety is “designed in”, that extra care is taken during the coding phase, and that all safety requirements are tested. A safety requirement traceability matrix is one way to implement this analysis.
8. Software **Element Analysis:** To perform this analysis, each software element that is not safety-critical is examined to ensure that it cannot cause or contribute to a hazard. When performing this analysis, consider, at a minimum, the questions in the **Software Component Design Analysis Checklist** [PAT-005](#_tabs-<p>5</p>)  shown below. If any items are discovered that may cause or contribute to a hazard, then the design should be revisited to remove the hazard potential or add a hazard control.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-005 - Software Component Design Analysis Checklist**

## 3.4 Evidence that Design Analysis has been performed

In order to provide evidence that the minimum critical analyses have been performed, complete and record the **Critical Design Analysis Checklist** [PAT-031](#_tabs-<p>5</p>)  shown in Tab 2.4.3 of this topic. For the safety critical software, it is recommended that as many of the other activities listed here also be performed.

## 3.5 Problem/Issue Tracking System

Per [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) – Task 2, all analysis non-conformances, findings, defects, issues, concerns, and observations are documented in a problem/issue tracking system and tracked to closure. These items are communicated to the software development personnel and possible solutions discussed. The level of risk associated with the finding/issue should be reflected in the priority given in the tracking system. The analysis performed by Software Assurance and Software Safety may be reported in one combined report, if desired.

## 3.6 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Analysis Reporting Content

### **Documenting and Reporting of Analysis Results**.

When the design is analyzed, the **Software Design Analysis** work product is generated to document results capturing the findings and corrective actions that need to be addressed to improve the overall design. It should include a detailed report of the design analysis results. Analysis results should also be reported in a high-level summary and conveyed as part of weekly or monthly SA Status Reports. The high-level summary should provide an overall evaluation of the analysis, any issues/concerns, and any associated risks. If a time-critical issue is uncovered, it should be reported to management immediately so that the affected organization may begin addressing it at once.

When a project has safety-critical software, analysis results should be shared with the Software Safety personnel. The results of analysis conducted by Software Assurance personnel and those done by Software Safety personnel may be combined into one analysis report, if desired.

## **4.1 High-Level Analysis Content for SA Status Report**

New or updated design analysis results Any design analysis since the last SA Status Report or project management meeting should be reported to project management and the rest of the Software Assurance team. When a project has safety-critical software, any analysis done by Software Assurance should be shared with the Software Safety personnel.

When reporting the results of an analysis in a SA Status Report, the following defines the minimum recommended contents:

* Identification of what was analyzed: Mission/Project/Application
* Period/Timeframe/Phase analysis performed during
* Summary of analysis techniques used
* Overall assessment of design, based on analysis
* Major findings and associated risk
* Current status of findings: open/closed; projection for closure timeframe

## **4.2 Detailed Content for Analysis Product:**

The Software Design Analysis product captures and documents all the detailed results of the analysis and descriptions of the techniques/methods used. The analysis techniques/methods that produced the most useful results should be highlighted for future use. The Software Design Analysis product is placed under configuration management and delivered to the project management team as the Software Assurance record for the activity. When a project has safety-critical software, this product should be shared with the Software Safety personnel.

When reporting the detailed results of the software design analysis, the following defines the minimum recommended content:

* Identification of what was analyzed: Mission/Project/Application
* Person(s) or group performing the analysis
* Period/Timeframe/Phase analysis performed
* Documents used in analysis (e.g., versions of the system and software requirements, interfaces document, architectural and detailed design)
* Description or identification of analysis techniques used. Include an evaluation of the techniques used.
* Overall assessment of design, based on analysis results
* Major findings and associated risk – The detailed reporting should include where the finding, issue, or concern was discovered and an assessment of the amount of risk involved with the finding.
* Minor findings
* Current status of findings: open/closed; projection for closure timeframe
  + Include counts for those discovered by SA and Software Safety
  + Include overall counts from the Project’s problem/issue tracking system.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-048)

  [Risk Classification for NASA Payloads](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=4A "Click to open in new window")

  NPR 8705.4A, Office of Safety and Mission Assurance, Effective Date: April 29, 2021, Expiration Date: April 29, 2026
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

Click on a link to download a usable copy of the template. (DesAn)       7/8/2025 - 16 items

**Design Analysis Process Asset Templates**

* (PAT-005 - )

  [PAT-005 - Software Component Design Analysis Checklist](https://swehb-pri.msfc.nasa.gov/download/attachments/114327589/Software%20Component%20Design%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.55 - Software Design Analysis, tab 3.3,
* (PAT-006 - )

  [PAT-006 - Design Practices for Safety](https://swehb.nasa.gov/download/attachments/114327707/Design%20Practices%20for%20Safety.docx?api=v2 "Click to open in new window")

  Topic 6.1, Topic Group: Programming Checklists
* (PAT-008 - )

  [PAT-008 - Safety Considerations for Design Peer Reviews Checklist](https://swehb.nasa.gov/download/attachments/114328132/Safety%20Considerations%20for%20Design%20Peer%20Reviews%20Checklist%20.docx?api=v2 "Click to open in new window")

  Software Design Analysis, tab 3.2,
* (PAT-014 - )

  [PAT-014 - Architecture Design Checklist](https://swehb.nasa.gov/download/attachments/114328318/Architecture%20Design%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.3, Also found in Peer Review and Design Analysis categories
* (PAT-015 - )

  [PAT-015 - Detailed Design Checklist](https://swehb.nasa.gov/download/attachments/114328341/Detailed%20Design%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.4, Also found in Peer Review and Design Analysis categories.
* (PAT-016 - )

  [PAT-016 - Functional Design Checklist](https://swehb.nasa.gov/download/attachments/114328352/Functional%20Design%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.5, Also found in Peer Review and Design Analysis categories.
* (PAT-020 - )

  [PAT-020 - Examples of Interface Problems](https://swehb.nasa.gov/download/attachments/115179572/Examples%20of%20Interface%20Problems.docx?api=v2 "Click to open in new window")

  Topic 8.16, Software Design Analysis, tab 3.3, Item 6, Also found in Design Analysis category.
* (PAT-021 - )

  [PAT-021 - SADESIGN Checklist](https://swehb.nasa.gov/download/attachments/115933188/SADESIGN%20%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.16 - Software Design Analysis, tab 2, Also in SWE-058, tab 7.4.1
* (PAT-023 - )

  [PAT-023 - Preparing for a SARB Checklist](https://swehb.nasa.gov/download/attachments/116293679/Preparing%20for%20a%20SARB%20Checklist.docx?api=v2 "Click to open in new window")

  SWE-143, tab 3, Also in Topic 8.55 - Software Design Analysis, Tab 2.4
* (PAT-029 - )

  [PAT-029 - Software Architecture Review Board Checklist](https://swehb.nasa.gov/download/attachments/120848418/Software%20Architecture%20Review%20Board%20Checklist.docx?api=v2 "Click to open in new window")

  8.55 - Software Design Analysis, tab 2.4.2, Also in SWE-143
* (PAT-030 - )

  [PAT-030 - SARB Review Checklist with Guidance](https://swehb.nasa.gov/download/attachments/120848457/SARB%20Review%20Checklist%20with%20Guidance.docx?api=v2 "Click to open in new window")

  Topic 8.55 - Software Design Analysis, Tab 2.4.2Also, in Category: DesAn
* (PAT-031 - )

  [PAT-031 - Critical Design Analysis Checklist](https://swehb.nasa.gov/download/attachments/123600967/Critical%20Design%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  Software Design Analysis, tab 2.4.3
* (PAT-036 - )

  [PAT-036 Software Architecture and Design Process Audit](https://swehb.nasa.gov/download/attachments/198770701/PAT-036%20-%20Architecture%20and%20Design%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Architecture and Design.
* (PAT-047 - )

  [PAT-047 - Architecture and Detailed Design Assessment](https://swehb.nasa.gov/download/attachments/198770765/PAT-047%20-%20Architecture%20and%20Detailed%20Design%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Architecture and Detailed Design in the Software Design Description document. Based on the minimum recommended content for a Software Design Description.
* (PAT-048 - )

  [PAT-048 - Interface Design Description Assessment](https://swehb.nasa.gov/download/attachments/198770866/PAT-048%20-%20Interface%20Design%20Description%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Interface Design Description document. Based on the minimum recommended content for an Interface Design Description.
* (PAT-055 - )

  [PAT-055 - Software Data Dictionary Assessment](https://swehb.nasa.gov/download/attachments/198770882/PAT-055%20-%20Software%20Data%20Dictionary%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Data Dictionary. Based on the minimum recommended content for a Software Data Dictionary.

## 5.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-143 - Software Architecture Review](/spaces/SWEHBVD/pages/102695501/SWE-143+-+Software+Architecture+Review) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access)       * [5.22 - Software Design Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641618/5.22+-+Software+Design+Analysis+Report+Minimum+Content) * [6.1 - Design for Safety Checklist](/spaces/SWEHBVD/pages/102695551/6.1+-+Design+for+Safety+Checklist) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [9.01 Software Design Principles](/spaces/SWEHBVD/pages/102695790/9.01+Software+Design+Principles) * [PAT-005 - Software Component Design Analysis Checklist](/spaces/SITE/pages/114327589/PAT-005+-+Software+Component+Design+Analysis+Checklist) * [PAT-006 - Design Practices for Safety](/spaces/SITE/pages/114327707/PAT-006+-+Design+Practices+for+Safety) * [PAT-008 - Safety Considerations for Design Peer Reviews Checklist](/spaces/SITE/pages/114328132/PAT-008+-+Safety+Considerations+for+Design+Peer+Reviews+Checklist) * [PAT-015 - Detailed Design Checklist](/spaces/SITE/pages/114328341/PAT-015+-+Detailed+Design+Checklist) * [PAT-016 - Functional Design Checklist](/spaces/SITE/pages/114328352/PAT-016+-+Functional+Design+Checklist) * [PAT-021 - SADESIGN Checklist](/spaces/SITE/pages/115933188/PAT-021+-+SADESIGN+Checklist) * [PAT-023 - Preparing for a SARB Checklist](/spaces/SITE/pages/116293679/PAT-023+-+Preparing+for+a+SARB+Checklist) * [PAT-029 - Software Architecture Review Board Checklist](/spaces/SITE/pages/120848418/PAT-029+-+Software+Architecture+Review+Board+Checklist) * [PAT-030 - SARB Review Checklist with Guidance](/spaces/SITE/pages/120848457/PAT-030+-+SARB+Review+Checklist+with+Guidance) * [PAT-031 - Critical Design Analysis Checklist](/spaces/SITE/pages/123600967/PAT-031+-+Critical+Design+Analysis+Checklist) |

## 5.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>5</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 5.6 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |
