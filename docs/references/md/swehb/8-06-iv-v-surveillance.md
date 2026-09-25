# 8.06 - IV V Surveillance

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695713. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance

8.06 - IV&V Surveillance

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695713)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695713&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Context](#tabs-1)
* [2. Surveillance](#tabs-2)
* [3. IV&V Requirements](#tabs-3)
* [4. Getting Started](#tabs-4)
* [5. Data Access](#tabs-5)
* [6. Relationships](#tabs-6)
* [7. Products](#tabs-7)
* [8. Objectives](#tabs-8)
* [9. TRR](#tabs-9)
* [10. Potential Outputs](#tabs-10)
* [11. Metrics](#tabs-11)
* [12. Challenges](#tabs-12)
* [13. Lessons Learned](#tabs-13)
* [14. Glossary](#tabs-14)
* [15. Resources](#tabs-15)

# 1. IV&V Surveillance in Context

This section will establish the rationale behind the creation of an IV&V Surveillance team.  It begins by describing the need for an IV&V Agent in general, and from there describes the specific circumstances that might lead NASA to stand-up an IV&V Surveillance effort for a particular project or program.  It broadly defines the need for a separate group (IV&V Surveillance) to provide insight to NASA stakeholders who have an oversight role with respect to making decisions and accepting risks for a given project or program.  Section 2.3.4 contains a ‘roadmap’ to the other sections of this topic based on the reader’s interests.

### 1.1 Importance of IV&V for Software Development

When software developers work on large systems like those designed for NASA, they face a substantial problem – the resulting system is ‘too big’ and ‘too complex’ for a single person to fully comprehend.  Handling this complexity (and the associated emergent behaviors, hazardous operations, and general errors in the development of the software) requires a team of competent, creative, and motivated engineers and analysts.  With enough people (and a management structure that can support them efficiently), a software developer can overcome the ‘scale’ and ‘complexity’ problems in order to build functioning software that NASA requires.  One significant problem remains, however, and the developer could never add enough people to the team to address it.

Software development teams cannot be completely objective when reviewing their own work.  The organization likely has a Verification and Validation (V&V) team or a Mission Assurance team to ensure that the original concept of the mission was realized, but these individuals are part of the team.  The software product is still ‘theirs’ in a sense, and they work with the software engineers who have a closer attachment to the product.  Being able to step outside of yourself (or your team) and consider what you could have done something wrong is at best difficult – even the idea of being wrong is uncomfortable enough, especially given the high stakes of space system software.  It is in this area that the value of an Independent Verification and Validation (IV&V) Agent becomes clear.

From the experiences of the NASA IV&V Program, even for major NASA projects like Shuttle and ISS, issues were found well into operations, despite the involvement of the Agency’s best systems engineers and software developers.  When new analysis approaches, new tools, and new perspectives are brought together to consider these large systems, new issues are discovered that could have severe consequences to the mission, including crew safety.

### 1.2 Role of IV&V in Software Assurance

An IV&V Agent is responsible for performing an independent assessment of the software in question.  There are various layers to this ‘independence’ (technical, managerial, cost).  One key aspect of this independence is the review of the inherent risk of the system, which results in a list of prioritized system/software capabilities.  With this risk assessment, the IV&V Agent determines which software capabilities or entities deserve the most attention.  The resulting IV&V analysis may cover the entire life cycle of the project (concept, requirements, design, code, and test) depending on the resources available.  The IV&V Agent delivers the results of these analyses to the Provider, which helps to mitigate the problem referenced in Section 1.1.  The IV&V Agent presents a more objective challenge to the software products developed by the Provider, which can lead to the identification of new issues that, once resolved, add confidence that the software will perform as expected and the mission goals will be achieved.

### 1.3 Acquirer Insight into IV&V Activities

For most NASA Missions, it is the responsibility of the NASA IV&V Facility to perform the IV&V analysis.  This is a useful arrangement because the Acquirer (NASA) has direct and easy access to the IV&V Agent (NASA IV&V) who is performing the work.  If there is a concern about the Provider’s products, NASA can go directly to a group that may be able to deliver some insight to support decision-making.

In some cases, however, the Provider may be given the option to select a third party to perform the IV&V analysis required by the NASA contract.  In this case, the IV&V Agent role moves outside of NASA’s direct sphere of influence.  This makes it more difficult for the Acquirer to stay informed on the results of the IV&V Agent, the associated quality of the findings, and the general health of their relationship with the Provider.  The third party, after all, is under contract to the Provider, not NASA.

The nature of IV&V efforts makes this distance between the IV&V Agent and the Acquirer concerning.  The difference in team size between the software developer and the IV&V Agent is measured in orders of magnitude, which means that the IV&V Agent cannot analyze all aspects of the software.  As mentioned in Section 1.2, IV&V performs a risk assessment that results in a prioritized list of areas for analysis.  In the interest of providing the most value to the Provider, an IV&V Agent will select the pieces of the software that they view as the riskiest.  This means that any IV&V analysis results/products relate to Computer Software Configuration Items (CSCIs) that are inherently risky or dangerous, and because the Acquirer has the responsibility to decide how much software risk they are taking on, they have an interest in the results of IV&V.

See also Topic [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance), [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones), [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight),

# 2. IV&V Surveillance

## 2.1 Purpose

In order to bridge the ‘gap’ between the Acquirer and the IV&V Agent identified in Section 1.3, NASA developed the concept of an IV&V Surveillance team.  This team interfaces with all stakeholders (Acquirer, Provider, IV&V Agent) to provide evidence that the IV&V analysis is taking place, that relationships are functional, and that findings from the IV&V Agent are reaching the right stakeholders.  Put more simply, the IV&V Surveillance team is a champion of the IV&V Agent (and all the associated expected benefits) and can make recommendations or raise concerns to enable the IV&V effort to be as effective as possible

## 2.2 Activities

The IV&V Surveillance team may choose from a wide variety of activities, based on the connections it is able to make and the resources available.  Typically, the surveillance effort begins by attending regular tag-ups between the Provider and the IV&V Agent, either status-focused or working discussions.  Outside of meetings, the team will carefully review the IV&V Plan to get a sense of how the IV&V Agent will conduct business.  Based on that, the IV&V Surveillance team will be able to ask more pertinent questions when things come up that appear to drift from the established plan.  Ideally, when the IV&V Agent delivers products to the Provider, the IV&V Surveillance team would be included in the distribution, and these products then trigger analysis activities to ensure that the execution of IV&V is reasonable.  If the IV&V Surveillance team is not included in the notification, they have a responsibility to ask for these products from either the Provider or IV&V Agent directly once they are aware they are available (from discussions in status tag-ups, for example).  These activities may result in any number of outputs detailed in Section 2.3.

## 2.3 Outputs

### 2.3.1 Risks

Risks are the primary output of an IV&V Surveillance effort.  They should clearly describe the potential problem along with a set of closure criteria to establish the scope of the risk.  Because an IV&V Surveillance effort does not perform technical analysis (that is why the IV&V Agent was selected), most risks focus on management or process concerns.  These types of concerns inevitably affect the technical products, so any risks should tie the underlying concern back to the higher-level safety and/or mission assurance objectives.

See also Topic [7.19 - Software Risk Management Checklists](/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists), [8.24 - Software Assurance Risk](/spaces/SWEHBVD/pages/150077537/8.24+-+Software+Assurance+Risk), [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management).

### 2.3.2 Reports

Reports are the secondary output of an IV&V Surveillance effort and may serve as supporting evidence for the risks identified during an analysis task.  In addition to describing the objective(s), approach, results, and conclusions of the analysis, and IV&V Surveillance report may be used to fill a communications gap between the IV&V Agent and other stakeholders (see “IV&V Surveillance as Information Broker” in Section 13).  The Provider is the target of IV&V analysis products, but others may benefit from the results produced by the IV&V Agent.  In cases where stakeholders may not have easy access to IV&V products (or adequate time to review), the IV&V Surveillance reports delivered to the Acquirer can serve as a summary of IV&V findings which may prompt further investigation.

### 2.3.3 Issues

In some cases, an IV&V Surveillance team may observe a systemic problem with the technical analysis performed by the IV&V Agent.  This could prompt the IV&V Surveillance team to do an analysis of the software products themselves.  In this instance, the team may deliver technical issues to the Provider directly (this would have to be negotiated with the Provider, along with access to the software products).  These issues may also be used as a ‘tuning’ device to ensure that IV&V Agent analysis gets back on track.

## 2.3.4 Roadmap

|  |  |
| --- | --- |
| “What could I learn from an IV&V Surveillance team? | See Section 3 “Relevance to Software Assurance Requirements” and Section 8 “Objectives to Consider” |
| “What do I need to do to set up an IV&V Surveillance team?” | See Section 4 “Getting Started” |
| “What kinds of problems might I encounter?” | See Section 12 “Challenges” |
| “What does an IV&V Surveillance activity look like?” | See Section 9 “Example: TRR” |
| “Who performs IV&V Surveillance work?” | See Section 4.2 “Staffing” |
| “Any good lessons?” | See Section 13 “Lessons Learned” |
| “What are some low-level goals of IV&V Surveillance?” | See Section 8 “Objectives to Consider” |

# 3. **The Independent Verification & Validation (IV&V) Requirements in Software Assurance and Software Safety Standard**

**The Independent Verification & Validation (IV&V) Requirements in Software Assurance and Software Safety Standard, NASA-STD-8739.8 [278](#_tabs-<p>15</p>), in section 4.4, are as follows:**

**NASA-STD-8739.8B - SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD**

4.4 Independent Verification &Validation

4.4.1 IV&V Overview

4.4.1.1 IV&V is a technical discipline of software assurance that employs rigorous analysis and testing methodologies to identify objective evidence and conclusions to provide an independent assessment of critical products and processes throughout the software development life cycle. The evaluation of products and processes throughout the life cycle demonstrates whether the software is fit for nominal operations (required functionality, safety, dependability, etc.) and off-nominal conditions (response to faults, responses to hazardous conditions, etc.). The goal of the IV&V effort is to contribute assurance conclusions provided to the project and stakeholders based on evidence found in software development artifacts and risks associated with the intended behaviors of the software.

4.4.1.2 Three parameters define the independence of IV&V: technical independence, managerial independence, and financial independence.  
a. Technical independence requires that the personnel performing the IV&V analysis are not involved in the development of the system or its elements. The IV&V team establishes an understanding of the problem and how the system addresses the problem. Through technical independence, the IV&V team’s different perspective allows it to detect subtle errors overlooked by personnel focused on developing the system.  
b. Managerial independence requires that the personnel performing the IV&V analysis are not in the same organization as the development and program management team. Managerial independence also means that the IV&V team makes its own decisions about which segments of the system and its software to analyze and test, chooses the IV&V analysis methods to apply, and defines the IV&V schedule of activities. While independent from the development and program management organization, the IV&V team provides its findings in a timely manner to both of those organizations. The submission of findings to the program management organization should not include any restrictions (e.g., requiring the approval of the development organization) or any other adverse pressures from the development group.  
c. Financial independence requires that the control of the IV&V budget be vested in a group independent of the software development organization. Financial independence does not necessarily mean that the IV&V team controls the budget but that the finances should be structured so that funding is available for the IV&V team to complete its analysis or test work. No adverse financial pressure or influence is applied.

4.4.1.3 The IV&V process starts early in the software development life cycle, providing feedback to the IV&V provider organization, allowing the IV&V team to modify products at optimal timeframes and in a timely fashion, thereby reducing overall project risk. The feedback also answers project stakeholders’ questions about system properties (correctness, robustness, safety, security, etc.) to make informed decisions with respect to the development and acceptance of the system and its software.

4.4.1.4 The IV&V provider performs two primary activities, often concurrently: verification and validation. Each of the activities provides a different perspective on the system/software.   
a. Verification is the process of evaluating a system and its software to provide objective evidence as to whether or not a product conforms to the build-to requirements and design specifications. Verification holds from the requirements through the design and code and into testing. Verification demonstrates that the products of a given development phase satisfy the conditions imposed at the start of or during that phase.   
b. Validation develops objective evidence that shows that the content of the engineering artifact is the right content for the developed system/software.   
The content is accurate and correct if the objective evidence demonstrates that it satisfies the system requirements (e.g., user needs, stakeholder needs, etc.), fully describes the required capability/functionality needed, and solves the right problem.

4.4.1.5 The main goal of the IV&V effort is to identify and generate objective evidence that supports the correct operation of the system or refutes the correct operation of the system. The IV&V provider typically works with the development team to understand this objective evidence, which provides artifacts such as concept studies, operations concepts, and requirements that define the overall project. The IV&V provider uses these materials to develop an independent understanding of the project’s commitment to NASA, which forms the basis for validating lower-level technical artifacts.

4.4.1.6 Two principles help guide the development and use of objective evidence.   
a. Performing IV&V throughout the entire development lifetime is the first principle; potential problems should be detected as early as possible in the development life cycle. Performing IV&V throughout the entire development lifetime provides the IV&V team with sufficient information to establish a basis for the analysis results and provides early objective evidence to the development and program management groups to help keep the development effort on track early in the life cycle.   
b. The second principle is “appropriate assurance.” Given that it is not possible to provide IV&V on all aspects of a project’s software, the IV&V provider and project should balance risks against available resources to define an IV&V program for each project that provides IV&V so that the software will operate correctly, safely, reliably, and securely throughout its operational lifetime. The IPEP documents this tailored approach and summarizes the cost/benefit trade-offs made in the scoping process.

4.4.1.7 The IV&V requirements are analyzed and partitioned according to the type of artifact. The requirements do not imply or require the use of any specific life cycle model. It is also important to understand that IV&V applies to any life cycle development process. The IV&V requirements document the potential scope of analysis performed by the IV&V provider and the key responsibility of the software project to provide the information needed to perform that analysis. Additionally, the risk assessment is used to scope the IV&V analysis to help determine the prioritization of activities and the level of rigor associated with performing those activities. The scoping exercise results are captured in the IV&V Project Execution Plan, as documented below.

4.4.2 IV&V Requirements   
The responsible project manager shall ensure the performance of the IV&V requirements, as defined in section 4.4.2 of this standard. The IV&V requirements in this section of the standard apply to any project required to have IV&V per the criteria defined in the NASA Software Engineering Requirements, NPR 7150.2. The IV&V requirements apply to all IV&V efforts performed on a software development project, as tailored by the IV&V Project Execution Plan. The IV&V requirements also serve as the definition of what NASA considers IV&V. IV&V is a risk mitigation activity, and as such, the application of IV&V analysis and the rigor of that analysis is driven by the IV&V provider’s assessment of software risk.  
4.4.2.1 The IV&V provider shall conduct planning and risk assessments to determine the specific system/software behaviors (including the software components responsible for implementing the behaviors) to be analyzed.  
Note: IV&V is a focused activity that prioritizes IV&V analysis to address the highest developmental and operational software risks. IV&V priority is based on the combination of the potential for software impacts on safety and mission success and the probability factors for latent defects. IV&V analysis activities provide coverage with a degree of rigor that reflects the priority level. The initial planning and scoping effort based on the risk assessment define the starting point for the IV&V analysis. During the life cycle of each IV&V project, continuous and iterative feedback, through the execution of analysis, identification of issues and risks, and the collection of deeper mission understanding, allows IV&V projects to “Follow The Risk” and adjust plans. The planning and scoping effort also aid in establishing the initial relationships between the IV&V provider, the Acquirer, and the Provider.  
4.4.2.2 The IV&V provider shall develop and negotiate an IV&V IPEP with the project.   
Note: The IPEP documents the activities, methods, level of rigor, environments, tailoring (if any) of the IV&V requirements, and criteria to be used in performing verification and validation of in-scope system/software behaviors (including responsible software components) determined by the planning and scoping effort. A Provider should use a documented analysis approach to track and manage the IV&V effort aligned with ongoing development project efforts. The IPEP documents which software products are subject to which analyses and which analysis requirements are wholly, partially, or not applied following the risk assessment and resource constraints. The IPEP also serves as a communication tool between the project and IV&V to set expectations for the IV&V products produced throughout the life cycle. The IPEP may require updating throughout the life cycle.  
4.4.2.3 The Project SMA Technical Authority (TA) shall review and concur with the IPEP.  
4.4.2.4 The IV&V provider shall provide analysis results, risks, and assurance statements and data to the responsible organizations’ project management, engineering, and software assurance personnel.  
Note: While independent, the IV&V provider is still a part of a project's overall safety and risk mitigation software assurance strategy. The results of IV&V analysis need to be incorporated into the overall software assurance assessment of the project and provided to the project management. The IV&V provider should support project milestone reviews and provide the project with an evaluation of the life cycle review artifacts to assist development management decisions on whether the review criteria have been met and how to proceed going forward.  
4.4.2.5 The IV&V provider shall participate in project reviews of software activities. Participation includes providing status and results of software IV&V activities including, but not limited to, upcoming analysis activities, artifacts needed from the project, the results of the current or completed analysis, defects, and risks to stakeholders, customers, and development project personnel.  
Note: The most significant positive impact of IV&V analysis is when the analysis results are in phase with the development effort. Communicating defects after development artifacts are baselined increases the cost to make the changes. Additionally, the inclusion of the IV&V provider in ongoing technical meetings keeps the IV&V provider informed of possible changes that may affect future IV&V tasking. Supporting the ongoing technical meetings allows the IV&V Provider an opportunity to provide real-time feedback on these changes.  
4.4.2.6 The IV&V provider shall provide the responsible organizations’ project management, engineering, and software assurance personnel insight into the software IV&V and IV&V test activities. As a minimum, the IV&V provider will be required to allow the responsible organizations’ project management, engineering, and software assurance personnel to perform the following activities:  
a. Monitor the IV&V activities and plans.  
b. Review the verification activities to ensure adequacy.  
c. Review IV&V studies and source data.  
d. Audit the software IV&V processes and practices.  
e. Participate in IV&V software reviews and technical interchange meetings  
4.4.2.7 The IV&V provider shall participate in planned software peer reviews or software inspections guided by the planning and scoping risk analysis documented in the IPEP and NASA-HDBK-2203.   
Note: The IV&V provider should be involved in the review/inspection process for all system/software items within the scope of their analysis.  
4.4.2.8 The IV&V provider shall establish, record, maintain, report, and utilize IV&V management and technical measurements.   
Note: The IV&V provider gathers and analyzes metrics on a periodic basis to perform continuous improvement of IV&V processes and identify indicators of IV&V and project risks.  
4.4.2.9 The IV&V provider shall assess and track software activities' actual results and performance against the software plans and identify and report any risks or findings to the responsible organizations’ project management, engineering, and software assurance personnel.  
4.4.2.10 The IV&V provider shall track and evaluate changes to software products to evaluate for possible changes in the IV&V provider’s risk analysis and potential adverse impacts to the software system and the development effort.   
4.4.2.11 The IV&V provider shall assess the software development life cycle for suitability for the problem to be solved and identify and communicate any risks associated with the chosen life cycle to the responsible organizations’ project management, engineering, and software assurance personnel.  
4.4.2.12 The IV&V provider shall identify, analyze, track, and record risks to the software and development project in accordance with NPR 8000.4, Agency Risk Management Procedural Requirements, and communicate the risks to the responsible organizations’ project management, engineering, and software assurance personnel.   
4.4.2.13 The IV&V provider shall verify the project implements the requirements for software listed in NPR 7150.2 and communicate any risks to the responsible organizations’ project management, engineering, and software assurance personnel.  
4.4.2.14 The IV&V provider shall track, record, and communicate defects/issues and other results found during the execution of IV&V analysis and independent IV&V testing to the responsible organizations’ project management, engineering, and software assurance personnel.  
4.4.2.15 The IV&V provider shall ensure that the identified defects and issues are addressed by the project.  
4.4.2.16 The IV&V provider shall ensure that software planned for reuse meets the fit, form, and function as a component within the new application.  
4.4.2.17 The IV&V provider shall ensure that the system architecture contains the computing-related items (subsystems, components, etc.) to carry out the system's mission and satisfy user needs and operational scenarios or use cases.  
4.4.2.18 The IV&V provider shall ensure that the basis for the computing-related functions reflects the planned operations and mission objectives.   
4.4.2.19 The IV&V provider shall ensure that feasibility and trade studies provide the results to support the critical decisions that drove the need for the study.  
4.4.2.20 The IV&V provider shall ensure that known software-based hazard causes, contributors, and controls are identified, documented, and traced to the project requirements.  
4.4.2.21 The IV&V provider shall ensure that known security threats and risks are identified, appropriately documented, and updated throughout the software development life cycle and communicated to the responsible organizations’ project management, engineering, and software assurance personnel.  
4.4.2.22 The IV&V provider shall verify and validate that the software requirements and system requirements are, as a minimum, correct, consistent, complete, accurate, readable, traceable, and testable.   
Note: Software usually provides the interface between the user and the system hardware and the interface between system hardware components and other systems. These interfaces are critical to the successful operation and use of the system.  
4.4.2.23 The IV&V provider shall verify and validate that the mitigations for identified security risks are in the software requirements.  
Note: Security is an essential aspect of any system development effort. In most systems, software provides the primary user interface. The user interface is an element of the system that can provide undesired access. A system concept design should address known security risks through various features in the system.   
4.4.2.24 The IV&V provider shall ensure that software requirements meet the dependability and fault tolerance required by the system.  
4.4.2.25 The IV&V provider shall ensure that software requirements provide the capability of controlling identified hazards and do not create hazardous conditions.  
4.4.2.26 The IV&V provider shall verify and validate that the relationship between the in-scope system/software requirements and the associated architectural elements is traceable, correct, consistent, and complete.  
Note: Architectural elements are responsible for implementing specific behaviors within the software and the overall system. The interactions between these architectural elements result in the realization of the desired behaviors as well as possible undesired behaviors.   
4.4.2.27 The IV&V provider shall verify and validate that the software architecture meets the user’s safety and mission-critical needs as defined in the requirements.   
Note: The architecture provides the foundation for the development of the software. It also significantly impacts how the software deals with faults and failures and how the software interfaces with the user and system components. Analysis of the architecture provides early insight into how the software is structured and how that structure can implement the requirements.  
4.4.2.28 The IV&V provider shall verify and validate that the detailed design products are traceable, consistent, complete, accurate, and testable.   
Note: Detailed design is the implementation of the algorithms that control and monitor the different parts of the system and allow for interaction between the system and the user and other systems. The detailed design defines how the architectural components behave to support the interactions defined in the architecture. Analysis of the detailed design includes looking at the low-level software components in the software system.  
4.4.2.29 The IV&V provider shall verify and validate that the interfaces between the detailed design components and the hardware, users, operators, other software, and external systems are correct, consistent, complete, accurate, and testable.  
Note: While the architecture defines the interactions between the architectural elements, each element is generally composed of lower-level components defined by the detailed design. The interfaces between these components are important in ensuring that the architectural element meets its assigned responsibilities.   
4.4.2.30 The IV&V provider shall verify and validate that the relationship between the software requirements and the associated detailed design components is correct, consistent, and complete.  
Note: The detailed design components capture the approach to implementing the software requirements, including the requirements associated with fault management, security, and safety. Analysis of the relationship between the detailed design and the software requirements provides evidence that all requirements are in the detailed design.  
4.4.2.31 The IV&V provider shall verify and validate that the software code and data products are consistent with architecture, complete with respect to requirements, and testable.  
4.4.2.32 The IV&V provider shall verify and validate that the software code meets the industry best practices and software coding standards.   
4.4.2.33 The IV&V provider shall verify and validate that the security risks in the software code are identified and mitigated.   
Note: This includes software developed by NASA, software developed for NASA, software maintained by or for NASA, COTS, GOTS, MOTS, OSS, reused software components, auto-generated code, embedded software, the software executed on processors embedded in programmable logic devices, legacy, heritage, applications, freeware, shareware, trial or demonstration software.  
4.4.2.34 The IV&V provider shall verify and validate the appropriate use of off-the-shelf software, including ensuring that the project has identified all OSS used and that the security risks are identified and mitigated by the use of the off-the-shelf software.  
4.4.2.35 The IV&V provider shall verify and validate that the project assesses the software systems for possible security vulnerabilities and weaknesses.  
4.4.2.36 The IV&V provider shall verify and validate that the project implements the required software security risk mitigations to ensure that security objectives for software are satisfied.  
4.4.2.37 The IV&V provider shall verify and validate the source code through the use of analysis tools (including but not limited to static, dynamic, composition, and formal analysis tools).   
Note: The use of analysis tools may include the verification and validation of the analysis tools used by the development project in the process of developing the software. The results may be from static code analysis, software composition analysis, dynamic code analysis, cyclomatic complexity, or other code quality analysis tools.  
4.4.2.38 The IV&V provider shall verify and validate that the relationship between the software design elements and the associated software units is correct, consistent, and complete.   
4.4.2.39 The IV&V provider shall verify and validate that the relationship between software code components and corresponding requirements is correct, complete, and consistent.   
Note: For all of the implementation requirements, it is with code that the development of software reaches its lowest level of abstraction and that the software capabilities are implemented. Evaluating the relationship between the source code and the design components and requirements provides evidence that only the specified requirements and components are in the system. Evaluating the relationship between the source code and the design components and requirements helps minimize one aspect of the emergence of unexpected behaviors: the inclusion of behaviors not specified in the requirements. The overall analysis of the code is essential in assuring that the code does implement the required software behaviors. From a safety perspective, it is important to evaluate the code and assure that known software safety and security issues such as buffer overflows and type mismatches, among many others, are not used in safety-critical aspects of the software.  
4.4.2.40 The IV&V provider shall verify and validate that test plans, test procedures, test cases, test environment (including simulations), and test design at all levels of testing (unit, integration, system, acceptance, etc.) are correct, complete, and consistent for verification and validation of the source code and system functions allocated to the software.  
4.4.2.41 The IV&V provider shall verify and validate the relationships between the test plans, test procedures, test cases, test design, source code. and system functions allocated to the software are correct, complete, and consistent.   
4.4.2.42 The IV&V provider shall verify that the test plans, test cases, test design, and test procedures contain objective acceptance criteria that support the verification of the associated requirements for both nominal and off-nominal conditions.   
4.4.2.43 The IV&V provider shall verify that the software test results meet the associated acceptance criteria to ensure that the software correctly implements the associated requirements.  
Note: The IV&V provider assesses the testing artifacts with respect to the desired capabilities and expected operational system environment. The assessment includes an examination of testing at system boundary conditions to include unexpected conditions. The testing analysis assures that the project tests all requirements and that the system does what the requirements state it should do. The testing analysis also includes an analysis of the traceability information between the tests and the requirements.  
4.4.2.44 The IV&V provider shall verify that the project tests the required software security risk mitigations to ensure that the security objectives for the software are satisfied.  
4.4.2.45 The IV&V provider shall verify that code coverage is measured by analysis of the results of the execution of tests.  
4.4.2.46 The IV&V provider shall verify through independent testing each of the software requirements that trace to a hazardous event, cause, or mitigation technique.  
4.4.2.47 The IV&V provider shall verify the project’s acceptance tests for loaded or uplinked data, rules, and code that affects software and software system behavior.  
4.4.2.48 The IV&V provider shall participate in all NASA quality audits, assessments, and reviews associated with the project.  
4.4.2.49 The IV&V provider shall assess the software maintenance and operational risks concerning software elements to support the planning of IV&V activities during the maintenance phase.  
Note 1: The approach to software development on some projects results in different parts of the software going into operation at different times in the overall project life cycle. For example, a lander mission to Mars may complete the software needed for the cruise phase to Mars while continuing to work on the entry, descent, landing, and surface operations software.   
Note 2: In some cases, software anomalies cause changes to the software. IV&V is important because software changes can often have ripple effects throughout the system and cause emergent behaviors. The IV&V analysis provides insight into these possible effects and provides an overall assessment of the impact of the change.

[278](#_tabs-<p>15</p>)

# 4. Getting Started

The following sections contain topics to consider when setting up an IV&V Surveillance effort.  The success of the IV&V Surveillance effort (and also a lot of the potential problems) is based on how well the following considerations are handled.

## 4.1 Scope

There are several options in terms of what an IV&V Surveillance effort can attempt to cover, and the effort should be related to the concerns that prompted the Acquirer’s (or other party’s) need for additional insight into the IV&V effort.  For example, if there is a concern about the technical quality of the IV&V Agent’s work, the IV&V Surveillance team may do some IV&V analysis alongside the IV&V Agent in order to show whether the IV&V effort is meeting expectations laid out in the IV&V Plan.  In most cases, however, the IV&V Surveillance role will be limited to analyzing the IV&V products that are generated, listening to meetings, and reviewing project management plans.  The team, in this case, takes the stance that the IV&V Agent is technically competent to perform the work – the IV&V Surveillance team is then interested in the health of the IV&V Agent / Provider relationship, ensuring that the IV&V Agent has everything it needs to be successful.

See also [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan), Topic [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan).

## 4.2 Staffing

Given the domain, the first requirement of an IV&V Surveillance team member would be a systems engineering background with experience in the analysis of software development.  Beyond that, it would be helpful for an analyst to have prior experience on multiple IV&V projects as an IV&V analyst.  They should be familiar with project management documentation (plans, schedules, etc.) and its relevance to the software development life cycle.  Access to historical data on IV&V project execution is a substantial plus because it allows the team to mine for potential questions to ask, common problems, and typical analysis activities an IV&V Agents may conduct.

In addition to the technical requirements, and IV&V Surveillance analyst must be willing to do analysis at the level of project management and not at the level of software artifacts.  For analysts moving from IV&V projects to IV&V Surveillance, it can be a significant ‘culture shock,’ so be prepared to ease that transition.  This role relies on openness, creativity, and flexibility as much as it relies on knowledge of IV&V.

# 5. Data Access

## 5.1 IV&V Plan

During the initial negotiations for getting IV&V Surveillance involved, it is important to secure access to a few items.  The IV&V Plan is a necessary input before any surveillance work can be done – the IV&V Agent is bound by certain agreements and expectations covered in the plan, and any assessment must begin with those details in mind.  The IV&V Agent typically updates the IV&V Plan once per year.  Depending on the point of contact, this may be easier to get directly from the IV&V Agent. See also [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan), Topic [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan).

## 5.2 Standard Meeting Materials

 Having secured the plan, the next requirement is to get invited to regular tag-ups where IV&V activities are discussed, as well as access to a repository where the meeting slides/minutes are stored.  If IV&V tag-ups are recorded, access to those would be helpful as well.

## 5.3 IV&V Products

The types of IV&V products required depends on how concerned IV&V Surveillance is about the technical competency of the work.  Nominally, the IV&V products that would be useful are all formal technical reports, problem reports, risks, and milestone presentations developed by the IV&V Agent.  It would be desirable for at least one member of the IV&V Surveillance team to have access to wherever these products are stored, but if that is not possible they should be on the distribution when these are delivered to the Provider (using whatever method adequately protects the sensitive nature of the document).

## 5.4 Relevant Standards

Many of the requirements imposed on the IV&V Agent are captured in the IV&V Plan, but there may be other sources of requirements that could assist in the development of IV&V Surveillance analysis activities.  For example, NASA projects are subject to a host of NPRs (ex. NPR 7150.2) that specify requirements for software engineering, software assurance, etc.  Depending on the terms of the contract, the Provider may be subject to those standards, or another set of “alternate standards” which have been determined to meet the intent of the NASA standards.  These standards will include requirements on both the Provider and the IV&V Agent with respect to IV&V.  It will also be important to get access to the Provider’s Software Development Plan (SDP), in order to, among other things, see what requirements the Provider has levied on the IV&V Agent.

### 5.4.1 IVV 09-1: Independent Verification and Validation Technical Framework

Section 15 in this topic contains a few references that may be useful when thinking about what to expect of an IV&V Agent.  Consider especially “IVV 09-1: Independent Verification and Validation Technical Framework,” which is a collection of principles and operating procedures related to delivering IV&V services.  This will not replace the need for the IV&V Agent’s IV&V Plan and other program/project-specific standards, but this could prove to be a useful benchmark for the IV&V Surveillance team.

# 6. Relationships

## 6.1 Provider

Because the IV&V Agent is under contract with the Provider, a relationship with the Provider is important for the surveillance team to build and maintain.  Access to the IV&V Agent will depend on this “gatekeeper” relationship – it may be the Provider’s decision to provide artifact and meeting access, but request that IV&V Surveillance not interact directly with the IV&V Agent.  This is less desirable, but the job of IV&V Surveillance would still be possible.  Either way, ensure that the IV&V Surveillance team engages with the Provider while minimizing disruption to the Provider.

## 6.2 IV&V Agent

Assuming that the Provider approves of direct communications with the IV&V Agent, this is an IV&V Surveillance team’s most valuable contact (for the obvious reason that they are doing the IV&V).  This is also the most potentially problematic relationship, for the very reason that IV&V Surveillance was conceived in the first place – the desire to not be wrong.  IV&V Surveillance could be seen in the same negative context that some Providers see the IV&V Agent (for pointing out problems or things that are “wrong”), and so special care should be taken to emphasize the shared goal of mission success.  It is also a good idea to socialize any potential risks or major findings with the IV&V Agent because they may have the information to address the concern and therefore make the risk unnecessary.

# 7. Products

The nature of the IV&V Surveillance products are up to the discretion of the team but should conform to the needs of the Acquirer with respect to the level of detail, format, etc.

## 7.1 Risks

As mentioned in Section 2.3.1, risks are the primary output of an IV&V Surveillance effort.  The team should consider any limitations on the kinds of risks they generate.  Risks may be constrained by the Acquirer in terms of applying only to Crew Safety, or only to certain CSCIs, or even only to process-based risks.  Preferably, all of these options are available, but the IV&V Surveillance team must negotiate with the Acquirer on specific needs.  Any constraints on IV&V Surveillance risks will also necessarily limit the types of activities performed.  It will also be necessary to establish a risk review board to ensure risks are clear, concise, of high quality, and conform to any Acquirer requirements.

## 7.2 Reports

These can be as varied as the risks, but there are a few types of reports to consider.  It would be helpful to create a report that communicates the IV&V Surveillance team’s assessment of the IV&V Plan in the context of the applicable IV&V requirements found in the governing documents, alternate standards, etc.  It would be helpful to develop a series of brief summary reports for all major deliveries from the IV&V Agent (such as a technical report).  Beyond that, consider what the Acquirer is looking for and adjust accordingly.

One other thing to consider beyond the communication of IV&V Surveillance results is the communication of IV&V results.  Just because the Provider has read the IV&V reports does not mean the Acquirer has, and even if the Acquirer has, they may not fully grasp the significance of the findings.  The IV&V Surveillance team may use its own reports as a vehicle to emphasize and magnify the key findings of the IV&V Agent to ensure that they have all the necessary support to overcome any challenges.

## 7.3 Briefings

Informal communications with the Acquirer may be sufficient to provide the necessary insight, but if there are standing meetings where several stakeholders meet regularly to discuss status, challenges, etc., consider using these forums as an opportunity to communicate findings and concerns about the nature of the Provider/IV&V Agent relationships.  Many groups are competing for attention at broader program tag-ups, and even software gets de-emphasized at times – so much more for the IV&V Agent.  If the organizers are willing to provide you a small slot to brief your concerns, this could be a useful way to bring software concerns to a group’s attention.

# 8. Objectives to Consider

The following table contains a list of potential objectives for IV&V Surveillance teams to consider and includes commentary on the importance of the question to the software assurance effort.  This list could never be exhaustive, but it is a good starting point for further objective definition.

|  |  |
| --- | --- |
| **Objective** | **Rationale** |
| Assure that IV&V has completed an independent risk assessment of the flight and/or ground software. | The larger purpose of IV&V is to be an objective reviewer of the software, which includes generating its own view of risk across the system.  This serves as a validation check on the Provider’s risk assumptions. |
| Assure that IV&V has an established mechanism to communicate and track external risks | Over the course of an IV&V analysis effort, IV&V may identify potential systemic concerns that do not quite count as an issue (yet) – stakeholders should be made aware of potential concerns as soon as possible. |
| Assure that IV&V has the necessary artifact and tool access to complete the planned work | These needs are covered in the IV&V Plan, with additional detail at periodic tag-ups between the IV&V Agent and the Provider.  Look for signs that an IV&V task continues to slip, or that the IV&V Agent keeps requesting the same access |
| Assure that IV&V is regularly reporting the status of open issues and risks | This should be covered in the regular tag-ups – if an issue disappears, check to see if it was closed.  If it was abandoned, check the rationale. |
| Assure that IV&V products are made available to stakeholders in a timely manner | IV&V results are no good if they do not reach stakeholders.  If IV&V Surveillance receives it, but the Acquirer does not consider socializing the availability of the IV&V products with the Acquirer and any other important stakeholders. |
| Assure that the IV&V Agent is invited to relevant technical reviews/discussions | IV&V has an interest in attending technical discussions, especially those related to the results of the risk assessment.  If they are not involved, understand why. |
| Assure that the IV&V Agent is consulted when major software issues are discovered | The Provider has hired the IV&V Agent to provide an independent assessment of the software.  They are a valuable resource that should be consulted when problems arise. |
| Assure that the IV&V Agent is clearly communicating their technical results | If an Acquirer reads a technical report, they should expect to find technical results.  Make sure the important details aren’t masked or hidden. |
| Assure that the path of dissenting opinion is clearly stated in the IV&V Plan (and associated documents) | Because IV&V focuses only on the most critical components of the system, any dissenting opinion should be given careful consideration.  The escalation path should be clear so that there is an established process to follow when disagreements between the Provider and the IV&V Agent occur. |
| Assure that the IV&V Plan reflects the reality of the relationship between the Provider and the IV&V Agent | It is understood that the details of a plan will change, but process changes should not change as frequently.  If you notice disarray in meetings, unreliable meeting invites, or a general lack of disciplined project management, this might warrant a risk. |
| Assure that the IV&V Agent is able to handle pushback from the Provider | In the end, the IV&V Agent sometimes has the unenviable task of delivering bad news.  If the Provider pushes back, the IV&V Agent should be able to substantiate their claims with evidence. |
| Assure that the Provider is able to handle pushback from the IV&V Agent | The Provider is ultimately responsible for safety and mission success.  If the IV&V Agent objects to action, there may be something there.  How they handle these situations may be an indicator of the success of IV&V more generally. |
| Assure that the IV&V Agent is willing to perform the “right” analysis over following the plan | If the IV&V Agent discovers, in the course of analysis, that the prior plan was incorrect (new data, bad assumptions, etc.), they should be willing to make a change.  If the IV&V Agent cannot make course corrections, this is a sign that IV&V analysis activities do not accurately track with the real risk of the system. |

# 9. Example of TRR

## 9.1 TRR Scenario

Suppose that the Provider has scheduled a TRR for a major CSCI and that the IV&V Agent has decided to perform an analysis of the test artifacts (for example, test cases) and the software test plan.  The IV&V Agent intends to develop a technical report to capture its analysis results/conclusions.  Given this information, what might the expected IV&V Surveillance task look like?

## 9.2 Entrance/Exit Criteria

Suppose that the Provider was required to adhere to NPR 7123.1B [041](#_tabs-<p>15</p>) “NASA Systems Engineering Processes and Requirements” with respect to entrance/exit criteria for all milestones.  Taken from Appendix G of this NPR, here are some of the Success Criteria that may be applicable to the IV&V Agent’s analysis.

|  |
| --- |
| 1. Adequate test plans are completed and approved for the system under test. |
| 3. The program/project has demonstrated compliance with the applicable NASA and implementing Center requirements, standards, processes, and procedures. |
| 5. Risks have been identified, credibly assessed, and appropriately mitigated. |
| 8. The objectives of the testing have been clearly defined and documented, and the review of all the test plans, as well as the procedures, environment, and configuration of the test item, provides a reasonable expectation that the objectives will be met. |
| 9. Test cases have been analyzed and are consistent with the test plans and objectives. |

## 9.3 Questions to Consider

Because it was supposed that the IV&V Agent would analyze the software test plan and the test cases, it is easy to see how Success Criteria 1 and 9 can be supported by IV&V.  There are other questions to consider which may provide insight into these areas, and the next step for an IV&V Surveillance analyst would do generate a list of questions that will help guide the investigation.  Depending on the size of the list of questions, it might be useful to sort them into ‘focus areas,’ and this can be used as a way to break up the task (and resulting conclusion statements).  In no particular order:

|  |
| --- |
| Success Criteria 5 checks that risks have been “credibly assessed” – what does IV&V have to say about this assessment and the risks identified in general?  Can they be validated by IV&V? |
| Are there any outstanding issues with requirements or standards compliance that should be taken into account for test readiness? |
| Does the IV&V Agent provide an assessment of the adequacy of test coverage for the most critical behaviors? (i.e., is behavior X fully exercised?) |
| Is there a clear trace from IV&V’s stated objectives to the analysis performed?  Is there a conclusion for every objective? |
| How does IV&V’s own analysis of the test cases compare with the Provider’s analysis? |
| Is the IV&V Agent providing an assessment of requirements coverage for this CSCI? |
| In IV&V’s view, is there a reasonable expectation that the test objectives will be met? (IV&V must answer this question) |
| Has the IV&V Agent clearly identified deficiencies (if any) in TRR “readiness” with sufficient detail? |

# 10. Potential Outputs

There are many options here, but a best practice for a task of this size is to create a set of outputs for multiple levels of abstraction.

## 10.1 Summary Report

The most detailed output would be a summary report (~10-15 pages) that includes an Executive Summary, a purpose statement (including rationale for the surveillance task), and a collection of ‘focus areas’ which are narrative descriptions of the surveillance analysis in each area (such as “Requirements Verification” or “Configuration Management”).  Within each focus area, develop a few paragraphs talking about the expectations of IV&V Surveillance in this area, the results of the surveillance analysis activity, any difficulties, and a conclusion statement.  This is also a good place to reflect the actual findings from the IV&V Agent’s TRR Technical Report.  If the Acquirer wants to dig into the details and evidence from the surveillance analysis, this would be the appropriate place to start.

## 10.2 Briefing

Another output would be a PowerPoint package with the information in Section 10.1 (excluding the narrative descriptions).  Each IV&V Surveillance focus area should be identified, along with its corresponding conclusion statement.  If there are open concerns, these might be pulled from all sections into a single slide.  This output is more appropriate for a status briefing at a stakeholder meeting unless there is a significant concern about, for example, test readiness on the project (which may require a more in-depth discussion).

## 10.3 Summary Statement

This is probably the least useful tool for communicating IV&V Surveillance analysis results, but sometimes a summary statement may be the only avenue available, so it is important to craft statements carefully to maximize value.  Past IV&V Surveillance teams have created a small PowerPoint package (1-2 slides) to capture the Summary Statement (this is the preferred method for large Acquirer tag-ups where many organizations present status).  Consider including a short description of the initial concern, the high-level task, the most significant findings, and stakeholder value or confidence gained from this activity.

## 10.4 Assurance Expectations

Given the TRR example, IV&V Surveillance should be prepared to talk about whether or not the test case analysis approach and corresponding IV&V results support the question “Is the software ready to be tested?”  It would be important to characterize whether or not the IV&V Agent has followed through on their analysis objectives, whether the supporting evidence in the report is sufficient to support their conclusions, and any explanations or rationale if objectives could not be met.  The IV&V Surveillance team should have some assessment of whether the test plan recommendations or suggestions are reasonable and reflect engineering and IV&V best practices.

# 11. Metrics

## 11.1 Monitor Information

Suppose that an IV&V Surveillance team has been invited to the bi-weekly tag-ups between the Provider and the IV&V Agent.  At this tag-up, the IV&V Agent briefs the attendees on the status of current activities, any open issues/risks, future work, and some relevant issue/risk metrics.  On the metrics slide, a chart shows the number of issues in ‘Created’ and ‘Resolved’ states (see below).

Metrics cannot tell the full story, of course, but looking at this chart, it appears that IV&V-generated issues do not linger in the ‘Created’ state for more than a month or so, which means the Provider is open to receiving and fixing these issues in a timely manner.  This would be a good sign that the IV&V Agent is able to have a positive impact on the Provider’s software.

## 11.2 Identify Trends

Software development is never quite so tidy, and sometimes the metrics charts can be a leading indicator.  Suppose that instead of the chart above, you saw something like the following:

It is clear that IV&V is still creating issues at a reasonably steady pace, but at the end of 2018, only a third of the issues have been resolved.  As stated in Section 11.1, metrics charts cannot tell the entire story, and there may be a valid reason why twenty issues are still unresolved.

## 11.3 Recognize the Problem

Now suppose that this trend continues into 2019, and the software Critical Design Review (CDR) is scheduled for February.  Given that the software CDR has likely been a target of IV&V analysis over the course of 2018, it is reasonable to assume these issues are directly relevant to whether the Provider can successfully pass CDR.  In this context, this metric looks like a leading indicator that there will be significant problems at CDR.

At this point, the IV&V Surveillance team should begin asking about the status of these issues, if it has not already come up in conversations.  It may be that the Provider intends to close them shortly and that the majority of these will disappear soon.  The team can confirm this by the presence of activity in the issue tracking tool(s) used by the Provider.  If these are actively being worked, this may not be a problem.

## 11.4 Raise Concerns

Depending on the degree to which the IV&V Agent is included in the overall software assurance team, this problem may not be well understood by the Provider.  Typically, the Provider assigns a single point of contact as the IV&V Liaison (in addition to their regular duties), and if this person does not transmit IV&V findings (for any number of reasons) to others in the Acquirer’s organization, this “bow wave” may come as a surprise to higher-level stakeholders.  This is where the IV&V Surveillance team can act as an information broker (see Section 13) to let those with more influence over resources and priorities know that there is a body of unresolved technical issues that should be addressed.  The IV&V Agent still has the responsibility to work with the Provider to close its issues, but the IV&V Surveillance team can play a role in facilitating that process by drawing the Acquirer’s attention to the problem.

# 12. Challenges

|  |
| --- |
| ***Artifact Availability***  It is possible to ‘starve’ an IV&V Surveillance team if IV&V products and other information are not available with some regularity.  There are many reasons for this, some of them contractual (see “Contractual Barriers to Information Sharing" Lesson Learned), some of them deal with the health of relationships (see Section 6.2 “IV&V Agent”), and still others may be due to circumstances on the project.  Unless the IV&V Surveillance team is given full access to the necessary repositories, this will likely be a reoccurring issue. |
| ***Terminology Overload***  Different groups have different expectations of what an IV&V Agent is supposed to do.  For some, this is limited to independent testing, and for others, IV&V encompasses full life cycle analysis.  This is further complicated by the specific contractual obligations that determine what IV&V is in this instance.  When using “IV&V” in reports, e-mails, and meeting conversations, be sure that there is a shared understanding (see “Shared Understanding of IV&V Surveillance” Lesson Learned). |
| ***Alternate Standards***  If alternate standards are approved by NASA, there is presumably evidence that they meet the intent of the replaced NASA standards.  In practice, this means that appeals to NASA standards on safety and mission assurance will have no effect (assuming those are the ones that have been replaced).  If an IV&V Surveillance analyst wishes to raise process concerns, they must do so with respect to these alternate standards.  This becomes problematic because “meets the intent” may be open to interpretation. |
| ***Outsider Status***  Some of the most valuable insight into the Provider / IV&V Agent relationship will come from those instances in which both parties are trying to resolve a dispute.  How dissent and disagreement are handled will indicate the strength (or weakness) of the underlying processes being followed.  The problem, however, is that no one enjoys a big audience when they have to deal with uncomfortable situations.  IV&V Surveillance is inherently in an outsider role, and this may mean that the team is excluded from some meetings.  The rationale given will likely be so that the attendees can be more “free” and frank in their discussions, and this may be the case.  The need to exclude IV&V Surveillance does indicate something, and so it will be up to the team to “read between the lines” to see if there is a real problem here. |

# 13. Lessons Learned

13.1 NASA Lessons Learned

No lessons learned have currently been identified for this topic.

### 13.2 Other Lessons Learned - IV&V

* **Shared Understanding of IV&V Surveillance:** One problem that even IV&V Agents encounter is the many disparate uses of “IV&V” and the associated meanings (see “Terminology Overload” Challenge).  If even the definition of “IV&V” is a problem, then it is much worse for a new effort like IV&V Surveillance.  If people do happen to know what IV&V is, they may erroneously assume IV&V Surveillance has a similar role, which explains why some surveillance teams have received questions from the Acquirer about the number of technical findings, or an assessment of the technical risks on the project.  Neither of these is part of the IV&V Surveillance purpose, but they are an indication that the purpose has not been well understood.  Ensuring that there is a common understanding among all stakeholders will help them ask the right questions, as well as understand exactly what kind of insight the IV&V Surveillance team can provide.

* **Contractual Barriers to Information Sharing:** If NASA requires insight into the IV&V effort (when a third party is chosen), and if the information-sharing requirements are muddled (see “Ambiguous IV&V Requirements”), then there is the possibility that NASA will be locked out of important insight.  IV&V Surveillance was created as a way to circumvent this problem, but unless it is backed up by specific contract language about information sharing, NASA (and, therefore, insight into mission assurance) is at the mercy of whoever happens to be the IV&V Agent and/or IV&V Liaison.

* **Ambiguous IV&V Requirements:** Because part of IV&V Surveillance’s role is to ensure that IV&V is being executed according to the plan (and associated requirements), there is a significant problem when those requirements are ambiguous.  For example, a requirement that states that the IV&V Agent is supposed to share products with stakeholders, but doesn’t identify those stakeholders, leaves the door open for IV&V Surveillance to be excluded from deliveries.  If an Acquirer wants insight from the IV&V Agent, it should be clearly reflected in any associated standards and contract vehicles.

* **IV&V Surveillance as Information Broker:** From the perspective of the IV&V Surveillance team, sometimes it seems like the IV&V Agent has everything it needs (in terms of artifact access, invitations to meetings, insight from other stakeholders), while the surveillance team is constantly asking itself “What am I missing?”  The truth is that everyone experiences these information access problems and this fact leads to an interesting function of IV&V Surveillance.  The team can act as an information broker between the stakeholders to ‘magnify’ the findings of the IV&V Agent to ensure that everyone is aware of the findings.  The IV&V Agent has a responsibility to ask for what it needs and advocate for its findings, but there are certain realities to being a third party contractor so far removed from the ultimate Acquirer.  If an IV&V Surveillance team was not performing this ‘information broker’ function, it would be worth investigating whether there is a need for it.

* **“The Sky is Falling” Fallacy:** Challenges such as limited artifact access and exclusion from certain meetings or tag-ups introduces an interesting problem for IV&V Surveillance teams.  In these cases, the lack of information encourages the creation of many risks that sound incredibly troubling at face value.  When information is limited, there is almost no constraint on the questions the IV&V Surveillance team might raise.  When a risk is drafted, it is helpful to ask the question “Are things really as bad as this risk makes it out to be?”  There may be another analysis activity or line of questioning that could temper the risk to something that is more reasonable (and more digestible by stakeholders).

# 14. Glossary

|  |  |
| --- | --- |
| Acquirer | The entity that contracts the software development work out to the Provider.  They have an interest in any insight from IV&V analysis. |
| IV&V Agent | The entity performing the IV&V analysis.  The report results to the Provider (and in other contexts, the Acquirer). |
| IV&V Liaison | The person working for the Provider who has been designated the point of contact for the IV&V Agent.  This individual monitor the progress of the IV&V Agent assists with artifact access requests and is the IV&V Agent’s immediate customer. |
| IV&V Surveillance | The entity that advocates for and facilitates the communication of IV&V analysis/results.  They provide insight directly to the Acquirer, but may also interface with the IV&V Agent and Provider. |
| Provider | The software development organization hired by the Acquirer.  They hire a 3rd party organization to perform IV&V analysis on their software. |

# 15. Resources

## 15.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-447)

  [IVV 09-1: Independent Verification and Validation Technical
  Framework](https://www.nasa.gov/sites/default/files/atoms/files/ivv_09-1_independent_verification_and_validation_technical_framework_-_ver_p_-_10-25-2017.pdf "Click to open in new window")

  IVV 09-1, Version: P, Effective Date: February 26, 2016, Based in NPR7150.2B.  The official version of this document is maintained in IV&V's internal IV&V Management System Website (https://confluence.ivv.nasa.gov:8445/display/IMS).
* (SWEREF-609)

  [IVV 09-4: Project Management](https://www.nasa.gov/sites/default/files/atoms/files/ivv_09-4_project_management_-_ver_ag_-_10-25-2017.pdf "Click to open in new window")

  IVV 09-4, Version: AG, Effective Date: June 24, 2014,   The official version of this document is maintained in IV&V's internal IV&V Management System Website (https://confluence.ivv.nasa.gov:8445/display/IMS).
* (SWEREF-610)

  [IVV 09-9: Safety and Mission Assurance](https://www.nasa.gov/sites/default/files/atoms/files/ivv_09-9_safety_and_mission_assurance_-_ver_d_-_10-25-2017.pdf "Click to open in new window")

  IVV 09-9, Version: D, Effective Date: January 27, 2016 The official version of this document is maintained in IV&V's internal IV&V Management System Website (https://confluence.ivv.nasa.gov:8445/display/IMS).
* (SWEREF-611)

  [IVV 22: Risk Management](https://www.nasa.gov/sites/default/files/atoms/files/ivv_22_risk_management_-_ver_h_-_10-25-2017.pdf "Click to open in new window")

  IVV 22, Version: H, Effective Date: October 16, 2017 The official version of this document is maintained in IV&V's internal IV&V Management System Website (https://confluence.ivv.nasa.gov:8445/display/IMS).
* (SWEREF-612)

  [S3001: Guidelines for Risk Management](https://www.nasa.gov/sites/default/files/atoms/files/s3001_guidelines_for_risk_management_-_ver_g_-_10-25-2017.pdf "Click to open in new window")

  S3001, Version: G, Effective Date: October 16, 2017 The official version of this document is maintained in IV&V's internal IV&V Management System Website (https://confluence.ivv.nasa.gov:8445/display/IMS).
* (SWEREF-613)

  [S3105: Guidelines for Writing IV&V TIMs,](https://www.nasa.gov/sites/default/files/atoms/files/s3105_guidelines_for_writing_ivv_tims_-_ver_k_-_10-25-2017.pdf "Click to open in new window")

  S3105, Version: K, Effective Date: March 20, 2017
   The official version of this document is maintained in IV&V's internal IV&V Management System Website (https://confluence.ivv.nasa.gov:8445/display/IMS).
* (SWEREF-614)

  [S3106: PBRA and RBA Process](https://www.nasa.gov/sites/default/files/atoms/files/s3106_pbra_and_rba_process_-_ver_d_-_10-25-2017.pdf "Click to open in new window")

  S3106, Version: D, Effective Date: October 4, 2012 The official version of this document is maintained in IV&V's internal IV&V Management System Website (https://confluence.ivv.nasa.gov:8445/display/IMS).

## 15.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan)        * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.19 - Software Risk Management Checklists](/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists) * [8.24 - Software Assurance Risk](/spaces/SWEHBVD/pages/150077537/8.24+-+Software+Assurance+Risk) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |

## 15.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>15</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 15.4 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |
