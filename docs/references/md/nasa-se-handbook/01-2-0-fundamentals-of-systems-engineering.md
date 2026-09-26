# 2.0 Fundamentals of Systems Engineering

> NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2. Printed pages 3–16. Machine conversion from PDF; tables and figures may be flattened. Cite as `SE HB §2.0`.

Fundamentals of Systems Engineering

technical manager, chief engineer—but for this document, the term “systems engineer” is used. The exact role and responsibility of the systems engineer may change from project to project depending on the size and complexity of the project and from phase to phase of the life cycle. For large projects, there may be one or more systems engineers. For small projects, the project manager may sometimes perform these practices. But whoever assumes those responsibilities, the systems engineering functions should be performed. The actual assignment of the roles and responsibilities of the named systems engineer may also therefore vary. The lead systems engineer ensures that the system technically fulfills the defined needs and requirements and that a proper systems engineering approach is being followed. The systems engineer oversees the project’s systems engineering activities as performed by the technical team and directs, communicates, monitors, and coordinates tasks. The systems engineer reviews and evaluates the technical aspects of the project to ensure that the systems/subsystems engineering processes are functioning properly and evolves the system from concept to product. The entire technical team is involved in the systems engineering process. The systems engineer usually plays the key role in leading the development of the concept of operations (ConOps) and resulting system architecture, defining boundaries, defining and allocating requirements, evaluating design tradeoffs, balancing technical risk between systems, defining and assessing interfaces, and providing oversight of verification and validation activities, as well as many other tasks. The systems engineer typically leads the technical planning effort and has the prime responsibility in documenting many of the technical plans, requirements and specification documents, verification and validation documents, certification packages, and other technical documentation.

In summary, the systems engineer is skilled in the art and science of balancing organizational, cost, and technical interactions in complex systems. The systems engineer and supporting organization are vital to supporting program and Project Planning and Control (PP&C) with accurate and timely cost and schedule information for the technical activities. Systems engineering is about tradeoffs and compromises; it uses a broad crosscutting view of the system rather than a single discipline view. Systems engineering is about looking at the “big picture” and not only ensuring that they get the design right (meet requirements) but that they also get the right design (enable operational goals and meet stakeholder expectations). Systems engineering plays a key role in the project organization. Managing a project consists of three main objectives: managing the technical aspects of the project, managing the project team, and managing the cost and schedule. As shown in FIGURE 2.0-1, these three functions are interrelated. Systems engineering is focused on the technical characteristics of decisions including technical, cost, and schedule and on providing these to the project manager. The Project Planning and Control (PP&C) function is responsible for identifying and controlling the cost and schedules of the project. The project manager has overall responsibility for managing the project team and ensuring that the project delivers a technically correct system within cost and schedule. Note that there are areas where the two cornerstones of project management, SE and PP&C, overlap. In these areas, SE provides the technical aspects or inputs whereas PP&C provides the programmatic, cost, and schedule inputs. This document focuses on the SE side of the diagram. The practices/processes are taken from NPR 7123.1, NASA Systems Engineering Processes and Requirements. Each process is described in much greater detail in subsequent chapters of this

PROJECT MANAGEMENT

PROJECT MANAGEMENT ACTIVITIES • • • •

Setting up Project Team Programmatic Stakeholders (non-technical, non-business) Programmatic Planning (non-technical, non-business) Identifying Programmatic (non-technical) requirements

• • • •

Identifying Programmatic Risks Technology Transfer and Commercialization Integration of technical and non-technical activities Overall Approver/Decider

Systems Engineering System Design Processes
- Stakeholder Expectations Definition
Common
- Technical Requirement’s Definition
Areas
- Logical Decomposition
- Design Solution Definition
- Stakeholders

Product Realization Processes
- Product Implementation
- Product Integration
- Product Verification
- Product Validation
- Product Transition

Technical Management Processes
- Technical Planning
- Requirements Management
- Interface Management
- Technical Risk Management
- Configuration Management
- Technical Data Management
- Technical Assessment
- Decision Analyses

- Risks
- Configuration
Management
- Data
Management
- Reviews
- Schedule

PP&C
- PP&C Integration
- Resource Management
- Scheduling
- Cost Estimation & Assessment
- Acquisition & Contract
Management
- Risk Management
- CM/DM

FIGURE 2.0-1 SE in Context of Overall Project Management

document, but an overview is given in the following subsections of this chapter.

### 2.1 The Common Technical

Processes and the SE Engine There are three sets of common technical processes in NPR 7123.1, NASA Systems Engineering Processes and Requirements: system design, product realization, and technical management. The processes in each set and their interactions and flows are illustrated

by the NPR systems engineering “engine” shown in FIGURE 2.1-1. The processes of the SE engine are used to develop and realize the end products. This chapter provides the application context of the 17 common technical processes required in NPR7123.1. The system design processes, the product realization processes, and the technical management processes are discussed in more detail in Chapters 4.0, 5.0, and 6.0, respectively. Processes 1 through 9 indicated in FIGURE 2.1-1 represent the tasks in the execution of a project. Processes 10 through17 are crosscutting tools for carrying out the processes.

Realized Products to Level above

Requirements Flow Down from Level above Technical Management Processes System Design Processes

10. Technical Planning

Requirements Definition Processes 1. Stakeholders Expectations Definition 2. Technical Requirements Definition

Technical Solution Definition Processes 3. Logical Decomposition 4. Design Solution Definition

Product Realization Processes

Technical Planning Processes

Cross cutting

Technical Control Processes 11. Requirement Management 12. Interface Management 13. Technical Risk Management 14. Configuration Management 15. Technical Data Management

Technical Assessment Processes 16. Technical Assessment

Product Transition Processes 9. Product Transition Crosscutting

Evaluation Processes 8. Product Validation 7. Product Verification

Design Realization Processes 6. Product Integration 5. Product Implementation

Technical Decision Analysis Process 17. Decision Analysis

Requirements Flow Down To Level below

Realized Products From Level below

System Design Processes applied to each product layer down through system structure

Product Realization Processes applied to each product layer up through system structure

FIGURE 2.1-1 The Systems Engineering Engine (NPR 7123.1)

- System Design Processes: The four system
design processes shown in FIGURE 2.1-1 are used to define and baseline stakeholder expectations, generate and baseline technical requirements, decompose the requirements into logical and behavioral models, and convert the technical requirements into a design solution that will satisfy the baselined stakeholder expectations. These processes are applied to each product of the system structure from the top of the structure to the bottom until the lowest products in any system structure branch are defined to the point where they can be built, bought, or reused. All other products in the

system structure are realized by implementation or integration.
- Product Realization Processes: The product realization processes are applied to each operational/
mission product in the system structure starting from the lowest level product and working up to higher level integrated products. These processes are used to create the design solution for each product (through buying, coding, building, or reusing) and to verify, validate, and transition up to the next hierarchical level those products that satisfy their design solutions and meet stakeholder

expectations as a function of the applicable life cycle phase.
- Technical Management Processes: The technical management processes are used to establish
and evolve technical plans for the project, to manage communication across interfaces, to assess progress against the plans and requirements for the system products or services, to control technical execution of the project through to completion, and to aid in the decision-making process. The processes within the SE engine are used both iteratively and recursively. As defined in NPR 7123.1, “iterative” is the “application of a process to the same

product or set of products to correct a discovered discrepancy or other variation from requirements,” whereas “recursive” is defined as adding value to the system “by the repeated application of processes to design next lower layer system products or to realize next upper layer end products within the system structure. This also applies to repeating application of the same processes to the system structure in the next life cycle phase to mature the system definition and satisfy phase success criteria.” The technical processes are applied recursively and iteratively to break down the initializing concepts of the system to a level of detail concrete enough that the technical team can implement a product from the information. Then the processes are applied recursively and iteratively to

TABLE 2.1-1 Alignment of the 17 SE Processes to AS9100

SE Process

AS9100 Requirement

Stakeholder Expectations

Customer Requirements

Technical Requirements Definition

Planning of Product Realization

Logical Decomposition

Design and Development Input

Design Solution Definition

Design and Development Output

Product Implementation

Control of Production

Product Integration

Control of Production

Product Verification

Verification

Product Validation

Validation

Product Transition

Control of Work Transfers; Post Delivery Support, Preservation of Product

Technical Planning

Planning of Product Realization; Review of Requirements; Measurement, Analysis and Improvement

Requirements Management

Design and Development Planning; Purchasing

Interface Management

Configuration Management

Technical Risk Management

Risk Management

Configuration Management

Configuration Management; Identification and Traceability; Control of Nonconforming Product

Technical Data Management

Control of Documents; Control of Records; Control of Design and Development Changes

Technical Assessment

Design and Development Review

Decision Analysis

Measurement, Analysis and Improvement; Analysis of Data

### 2.2 An Overview of the SE

Engine by Project Phase

integrate the smallest product into greater and larger systems until the whole of the system or product has been assembled, verified, validated, and transitioned.

FIGURE 2.2-1 conceptually illustrates how the SE engine is used during each phase of a project (PrePhase A through Phase F). The life cycle phases are described in TABLE 2.2-1. FIGURE 2.2-1 is a conceptual diagram. For full details, refer to the poster version of this figure, which is located at https://nen.nasa.gov/ web/se/doc-repository.

For a detailed example of how the SE Engine could be used, refer to the NASA Expanded Guidance for SE document at https://nen.nasa.gov/web/se/ doc-repository. AS9100 is a widely adopted and standardized quality management system developed for the commercial aerospace industry. Some NASA Centers have chosen to certify to the AS9100 quality system and may require their contractors to follow NPR 7123.1. TABLE 2.1-1 shows how the 17 NASA SE processes align with AS9100.

Formulation Pre-Phase A: Concept Studies

Feasible Concept

The uppermost horizontal portion of this chart is used as a reference to project system maturity, as the project progresses from a feasible concept to an as-deployed system; phase activities; Key Decision Points (KDPs); and major project reviews. The next major horizontal band shows the technical development

Phase A: Concept & Technology Development

Approval Phase C: Phase B: Final Design & Preliminary Design & Fabrication Technology Completion

Top-Level Architecture

Functional Baseline

Allocated Baseline

Implementation Phase D: System Assembly, Integration & Test, Launch

Product Baseline

Phase E: Operations & Sustainment

Phase F: Closeout

As-Deployed Baseline

Key Decision Points:

Technical Development

Major Reviews: ?

?

4.2

5.5

4.2

5.5

4.3

5.4

4.3

5.4

4.4

5.3

?

5.1

6.1 Technical Management

?

?

4.1

5.2

4.1

?

4.4 ?

?

?

5.3

?

5.2

5.1

6.1

6.1

6.1

6.1

6.1

6.1

6.8

6.8

6.8

6.8

6.8

6.8

6.2 6.3 6.4 6.5 6.6 6.7 6.8

FIGURE 2.2-1 Miniature Version of the Poster-Size NASA Project Life Cycle Process Flow for Flight and Ground Systems Accompanying this Handbook

TABLE 2.2-1 Project Life Cycle Phases

Formulation

Pre-Formulation

Phase

Purpose

Typical Outcomes

Pre-Phase A

To produce a broad spectrum of ideas and alternatives for missions from which new programs/projects can be selected. Determine feasibility of desired system, develop mission concepts, draft system-level requirements, assess performance, cost, and schedule feasibility; identify potential technology needs, and scope.

Feasible system concepts in the form of simulations, analysis, study reports, models, and mock-ups

Phase A

To determine the feasibility and desirability of a suggested new system and establish an initial baseline compatibility with NASA’s strategic plans. Develop final mission concept, system-level requirements, needed system technology developments, and program/project technical management plans.

System concept definition in the form of simulations, analysis, engineering models and mock-ups, and trade study definition

Phase B

To define the project in enough detail to establish an initial baseline capable of meeting mission needs. Develop system structure end product (and enabling product) requirements and generate a preliminary design for each system structure end product.

End products in the form of mock-ups, trade study results, specification and interface documents, and prototypes

Phase C

To complete the detailed design of the system (and its associated subsystems, including its operations systems), fabricate hardware, and code software. Generate final designs for each system structure end product.

End product detailed designs, end product component fabrication, and software development

Phase D

To assemble and integrate the system (hardware, software, and humans), meanwhile developing confidence that it is able to meet the system requirements. Launch and prepare for operations. Perform system end product implementation, assembly, integration and test, and transition to use.

Operations-ready system end product with supporting related enabling products

Phase E

To conduct the mission and meet the initially identified need and maintain support for that need. Implement the mission operations plan.

Desired system

Phase F

To implement the systems decommissioning/disposal plan developed in Phase E and perform analyses of the returned data and any returned samples.

Product closeout

Concept Studies

Concept and Technology Development

Preliminary Design and Technology Completion

Implementation

Final Design and Fabrication

System Assembly, Integration and Test, Launch

Operations and Sustainment Closeout

processes (steps 1 through 9) in each project phase. The SE engine cycles five times from Pre-Phase A through Phase D. Note that NASA’s management has structured Phases C and D to “split” the technical development processes in half in Phases C and D to ensure closer management control. The engine is bound by a dashed line in Phases C and D. Once a project enters into its operational state (Phase E)

and closes out (Phase F), the technical work shifts to activities commensurate with these last two project phases. The next major horizontal band shows the eight technical management processes (steps 10 through 17) in each project phase. The SE engine cycles the technical management processes seven times from Pre-Phase A through Phase F.

### 2.3 Example of Using the SE Engine

In Pre-Phase A, the SE engine is used to develop the initial concepts; clearly define the unique roles of humans, hardware, and software in performing the missions objectives; establish the system functional and performance boundaries; develop/identify a preliminary/draft set of key high-level requirements, define one or more initial Concept of Operations (ConOps) scenarios; realize these concepts through iterative modeling, mock-ups, simulation, or other means; and verify and validate that these concepts and products would be able to meet the key high-level requirements and ConOps. The operational concept must include scenarios for all significant operational situations, including known off-nominal situations. To develop a useful and complete set of scenarios, important malfunctions and degraded-mode operational situations must be considered. The importance of early ConOps development cannot be underestimated. As system requirements become more detailed and contain more complex technical information, it becomes harder for the stakeholders and users to understand what the requirements are conveying; i.e., it may become more difficult to visualize the end product. The ConOps can serve as a check in identifying missing or conflicting requirements. Note that this Pre-Phase A initial concepts development work is not the formal verification and validation program that is performed on the final product, but rather it is a methodical run through ensuring that the concepts that are being developed in this Pre-Phase A are able to meet the likely requirements and expectations of the stakeholders. Concepts are developed to the lowest level necessary to ensure that they are feasible and to a level that reduces the risk low enough to satisfy the project. Academically, this process could proceed down to the circuit board level for every system; however, that would involve a great deal of time and money. There may be a higher level or tier of product than circuit board level that would

enable designers to accurately determine the feasibility of accomplishing the project, which is the purpose of Pre-Phase A. During Phase A, the recursive use of the SE engine is continued, this time taking the concepts and draft key requirements that were developed and validated during Pre-Phase A and fleshing them out to become the set of baseline system requirements and ConOps. During this phase, key areas of high risk might be simulated to ensure that the concepts and requirements being developed are good ones and to identify verification and validation tools and techniques that will be needed in later phases. During Phase B, the SE engine is applied recursively to further mature requirements and designs for all products in the developing product tree and perform verification and validation of concepts to ensure that the designs are able to meet their requirements. Operational designs and mission scenarios are evaluated and feasibility of execution within design capabilities and cost estimates are assessed. Phase C again uses the left side of the SE engine to finalize all requirement updates, finalize the ConOps validation, develop the final designs to the lowest level of the product tree, and begin fabrication. Phase D uses the right side of the SE engine to recursively perform the final implementation, integration, verification, and validation of the end product, and at the final pass, transition the end product to the user. The technical management processes of the SE engine are used in Phases E and F to monitor performance; control configuration; and make decisions associated with the operations, sustaining engineering, and closeout of the system. Any new capabilities or upgrades of the existing system reenter the SE engine as new developments.

### 2.4 Distinctions between

Product Verification and Product Validation From a process perspective, the Product Verification and Product Validation processes may be similar in nature, but the objectives are fundamentally different:
- Verification of a product shows proof of compliance with requirements—that the product can
meet each “shall” statement as proven though performance of a test, analysis, inspection, or demonstration (or combination of these).
- Validation of a product shows that the product accomplishes the intended purpose in the
intended environment—that it meets the expectations of the customer and other stakeholders as shown through performance of a test, analysis, inspection, or demonstration. Verification testing relates back to the approved requirements set and can be performed at different stages in the product life cycle. The approved specifications, drawings, parts lists, and other configuration documentation establish the configuration baseline of that product, which may have to be modified at a later time. Without a verified baseline and appropriate configuration controls, later modifications could be costly or cause major performance problems. Validation relates back to the ConOps document. Validation testing is conducted under realistic conditions (or simulated conditions) on end products for the purpose of determining the effectiveness and suitability of the product for use in mission operations by typical users. Validation can be performed in each development phase using phase products (e.g., models) and not only at delivery using end products.

It is appropriate for verification and validation methods to differ between phases as designs advance. The ultimate success of a program or project may relate to the frequency and diligence of validation efforts during the design process, especially in Pre-Phase A and Phase A during which corrections in the direction of product design might still be made cost-effectively. The question should be continually asked, “Are we building the right product for our users and other stakeholders?” The selection of the verification or validation method is based on engineering judgment as to which is the most effective way to reliably show the product’s conformance to requirements or that it will operate as intended and described in the ConOps.

### 2.5 Cost Effectiveness

Considerations The objective of systems engineering is to see that the system is designed, built, and can be operated so that it accomplishes its purpose safely in the most cost-effective way possible considering performance, cost, schedule, and risk. A cost-effective and safe system should provide a particular kind of balance between effectiveness and cost. This causality is an indefinite one because there are usually many designs that meet the cost-effective condition. Design trade studies, an important part of the systems engineering process, often attempt to find designs that provide the best combination of cost and effectiveness. At times there are alternatives that either reduce costs without reducing effectiveness or increase effectiveness without increasing cost. In such “win-win” cases, the systems engineer’s decision is easy. When the alternatives in a design trade study require trading cost for effectiveness, the decisions become harder.

THE SYSTEMS ENGINEER’S DILEMMA At each cost-effective solution:
- To reduce cost at constant risk, performance must be reduced.
- To reduce risk at constant cost, performance must be reduced.
- To reduce cost at constant performance, higher risks must be accepted.
- To reduce risk at constant performance, higher costs must be accepted.
In this context, time in the schedule is often a critical resource, so that schedule behaves like a kind of cost.

FIGURE 2.5-1 shows that the life cycle costs of a

program or project tend to get “locked in” early in design and development. The cost curves clearly show that late identification of and fixes to problems cost considerably more later in the life cycle. Conversely, descopes taken later versus earlier in the project life cycle result in reduced cost savings. This figure, obtained from the Defense Acquisition University, is an example of how these costs are determined by the early concepts and designs. The numbers will vary from project to project, but the general shape of the curves and the message they send will be similar. For example, the figure shows that during design, only about 15% of the costs might be expended, but the design itself will commit about 75% of the life cycle costs. This is because the way the system is designed will determine how expensive it will be to test, manufacture, integrate, operate, and sustain. If these factors have not been considered during design, they pose significant cost risks later in the life cycle. Also note that the cost to change the design increases as you get later in the life cycle. If the project waits until verification to do any type of test or analysis, any problems found will have a significant cost impact to redesign and reverify.

The technical team may have to choose among designs that differ in terms of numerous attributes. A variety of methods have been developed that can be used to help uncover preferences between attributes and to quantify subjective assessments of relative value. When this can be done, trades between attributes can be assessed quantitatively. Often, however, the attributes are incompatible. In the end, decisions need to be made in spite of the given variety of attributes. There are several decision analysis techniques (Section 6.8) that can aid in complex decision analysis. The systems engineer should always keep in mind the information that needs to be available to help the decision-makers choose the most cost-effective option.

### 2.6 Human Systems Integration

(HSI) in the SE Process As noted at the beginning of NPR 7123.1, the “systems approach is applied to all elements of a system (i.e., hardware, software, human systems integration. In short, the systems engineering approach must equally address and integrate these three key elements: hardware, software, and human systems

Cumulative Percentage Life Cycle Cost against Time

100%

90%

90% 75%

80%

i fe d L ts e i t t os m m le C o C C yc 20–100×

70% 60% 50%

45% 3–6×

40%

C

30% 20% 10% 0%

C to

h

Design

Concept

SRR

SDR

eD

e

100%

n

Operations through Disposal

n sig

Di

re

o c ti

ed ) 50% et e d pl end m p Co E x Prod/Test % ts s o (C

20% Develop

15%

8% MCR

t os

g an

500–1000×

PDR

CDR

SIR

ORR

DR/DRR

Time

MCR

Mission Concept Review

CDR

Critical Design Review

SRR

System Requirements Review

SIR

System Integration Review

SDR

System Definition Review

ORR

Operational Readiness Review

PDR

Preliminary Design Review

DR/DRR

Decommissioning/Disposal Readiness Review

Adapted from INCOSE-TP-2003-002-04, 2015

FIGURE 2.5-1 Life-Cycle Cost Impacts from Early Phase Decision-Making

integration. Therefore, the human element is something that integration and systems engineering processes must address. The definition of “system” in NPR 7123.1 is inclusive; i.e., a system is “the combination of elements that function together to produce the capability required to meet a need. The elements include all hardware, software, equipment, facilities, personnel, processes, and procedures needed for this purpose. For additional information and guidance on his, refer to Section 2.6 of the NASA Expanded Guidance for Systems Engineering at https://nen. nasa.gov/web/se/doc-repository.

### 2.7 Competency Model for

Systems Engineers TABLE 2.7-1 provides a summary of the Competency

Model for Systems Engineering. For more information on the NASA SE Competency model refer to: http://appel.nasa.gov/competency-model/. There are four levels of proficiencies associated with each of these competencies: • • • •

Team Practitioner/Technical Engineer Team Lead/Subsystem Lead Project Systems Engineer Chief Engineer

TABLE 2.7-1 NASA System Engineering Competency Model

Competency Area

Competency

Description

SE 1.0

SE 1.1

Eliciting and defining use cases, scenarios, concept of operations and stakeholder expectations. This includes identifying stakeholders, establishing support strategies, establishing a set of Measures of Effectiveness (MOEs), validating stakeholder expectation statements, and obtaining commitments from the customer and other stakeholders, as well as using the baselined stakeholder expectations for product validation during product realization

SE 1.2

Transforming the baseline stakeholder expectations into unique, quantitative, and measurable technical requirements expressed as “shall” statements that can be used for defining the design solution. This includes analyzing the scope of the technical problems to be solved, defining constraints affecting the designs, defining the performance requirements, validating the resulting technical requirement statements, defining the Measures of Performance (MOPs) for each MOE, and defining appropriate Technical Performance Measures (TPMs) by which technical progress will be assessed.

SE 1.3

Transforming the defined set of technical requirements into a set of logical decomposition models and their associated set of derived technical requirements for lower levels of the system, and for input to the design solution efforts. This includes decomposing and analyzing by function, time, behavior, data flow, object, and other models. It also includes allocating requirements to these decomposition models, resolving conflicts between derived requirements as revealed by the models, defining a system architecture for establishing the levels of allocation, and validating the derived technical requirements.

SE 1.4

Translating the decomposition models and derived requirements into one or more design solutions, and using the Decision Analysis process to analyze each alternative and for selecting a preferred alternative that will satisfy the technical requirements. A full technical data package is developed describing the selected solution. This includes generating a full design description for the selected solution; developing a set of ‘make-to,’ ‘buy-to,’ ‘reuse-to,’ specifications; and initiating the development or acquisition of system products and enabling products.

SE 2.1

Generating a specific product through buying, making, or reusing so as to satisfy the design requirements. This includes preparing the implementation strategy; building or coding the produce; reviewing vendor technical information; inspecting delivered, built, or reused products; and preparing product support documentation for integration.

SE 2.2

Assembling and integrating lower-level validated end products into the desired end product of the higher-level product. This includes preparing the product integration strategy, performing detailed planning, obtaining products to integrate, confirming that the products are ready for integration, preparing the integration environment, and preparing product support documentation.

SE 2.3

Proving the end product conforms to its requirements. This includes preparing for the verification efforts, analyzing the outcomes of verification (including identifying anomalies and establishing recommended corrective actions), and preparing a product verification report providing the evidence of product conformance with the applicable requirements.

System Design

Stakeholder Expectation Definition & Management

Technical Requirements Definition

Logical Decomposition

Design Solution Definition

SE 2.0

Product Realization

Product Implementation

Product Integration

Product Verification

(continued)

Competency Area SE 2.0

Product Realization

Competency

Description

SE 2.4

Confirming that a verified end product satisfies the stakeholder expectations for its intended use when placed in its intended environment and ensuring that any anomalies discovered during validation are appropriately resolved prior to product transition. This includes preparing to conduct product validation, performing the product validation, analyzing the results of validation (including identifying anomalies and establishing recommended corrective actions), and preparing a product validation report providing the evidence of product conformance with the stakeholder expectations baseline.

SE 2.5

Transitioning the verified and validated product to the customer at the next level in the system structure. This includes preparing to conduct product transition, evaluating the product and enabling product readiness for product transition, preparing the product for transition (including handling, storing, and shipping preparation), preparing sites, and generating required documentation to accompany the product

SE 3.1

Planning for the application and management of each common technical process, as well as identifying, defining, and planning the technical effort necessary to meet project objectives. This includes preparing or updating a planning strategy for each of the technical processes, and determining deliverable work products from technical efforts; identifying technical reporting requirements; identifying entry and success criteria for technical reviews; identifying product and process measures to be used; identifying critical technical events; defining cross domain interoperability and collaboration needs; defining the data management approach; identifying the technical risks to be addressed in the planning effort; identifying tools and engineering methods to be employed; and defining the approach to acquire and maintain technical expertise needed. This also includes preparing the Systems Engineering Management Plan (SEMP) and other technical plans; obtaining stakeholder commitments to the technical plans; and issuing authorized technical work directives to implement the technical work

SE 3.2

Managing the product requirements, including providing bidirectional traceability, and managing changes to establish requirement baselines over the life cycle of the system products. This includes preparing or updating a strategy for requirements management; selecting an appropriate requirements management tool; training technical team members in established requirement management procedures; conducting expectation and requirements traceability audits; managing expectation and requirement changes; and communicating expectation and requirement change information

SE 3.3

Establishing and using formal interface management to maintain internal and external interface definition and compliance among the end products and enabling products. This includes preparing interface management procedures, identifying interfaces, generating and maintaining interface documentation, managing changes to interfaces, disseminating interface information, and conducting interface control

SE 3.4

Examining on a continual basis the risks of technical deviations from the plans, and identifying potential technical problems before they occur. Planning, invoking, and performing risk-handling activities as needed across the life of the product or project to mitigate impacts on meeting technical objectives. This includes developing the strategy for technical risk management, identifying technical risks, and conducting technical risk assessment; preparing for technical risk mitigation, monitoring the status of each technical risk, and implementing technical risk mitigation and contingency action plans when applicable thresholds have been triggered.

Product Validation

Product Transition

SE 3.0

Technical Management

Technical Planning

Requirements Management

Interface Management

Technical Risk Management

(continued)

Competency Area

Competency

Description

SE 3.0

SE 3.5

Identifying the configuration of the product at various points in time, systematically controlling changes to the configuration of the product, maintaining the integrity and traceability of product configuration, and preserving the records of the product configuration throughout its life cycle. This includes establishing configuration management strategies and policies, identifying baselines to be under configuration control, maintaining the status of configuration documentation, and conducting configuration audits

SE 3.6

Identifying and controlling product-related data throughout its life cycle; acquiring, accessing, and distributing data needed to develop, manage, operate, support, and retire system products; managing and disposing data as records; analyzing data use; obtaining technical data feedback for managing the contracted technical efforts; assessing the collection of appropriate technical data and information; maintaining the integrity and security of the technical data, effectively managing authoritative data that defines, describes, analyzes, and characterizes a product life cycle; and ensuring consistent, repeatable use of effective Product Data and Life-cycle Management processes, best practices, interoperability approaches, methodologies, and traceability. This includes establishing technical data management strategies and policies; maintaining revision, status, and history of stored technical data and associated metadata; providing approved, published technical data; providing technical data to authorized parties; and collecting and storing required technical data.

SE 3.7

Monitoring progress of the technical effort and providing status information for support of the system design, product realization, and technical management efforts. This includes developing technical assessment strategies and policies, assessing technical work productivity, assessing product quality, tracking and trending technical metrics, and conducting technical, peer, and life cycle reviews.

SE 3.8

Evaluating technical decision issues, identifying decision criteria, identifying alternatives, analyzing alternatives, and selecting alternatives. Performed throughout the system life cycle to formulate candidate decision alternatives, and evaluate their impacts on health and safety, technical, cost, and schedule performance. This includes establishing guidelines for determining which technical issues are subject to formal analysis processes; defining the criteria for evaluating alternative solutions; identifying alternative solutions to address decision issues; selecting evaluation methods; selecting recommended solutions; and reporting the results and findings with recommendations, impacts, and corrective actions.

Technical Management

Configuration Management

Technical Data Management

Technical Assessment

Technical Decision Analysis
