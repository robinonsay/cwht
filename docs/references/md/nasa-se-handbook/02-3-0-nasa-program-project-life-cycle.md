# 3.0 NASA Program/Project Life Cycle

> NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2. Printed pages 17–42. Machine conversion from PDF; tables and figures may be flattened. Cite as `SE HB §3.0`.

NASA Program/Project Life Cycle O

ne of the fundamental concepts used within NASA for the management of major systems is the program/project life cycle, which categorizes everything that should be done to accomplish a program or project into distinct phases that are separated by Key Decision Points (KDPs). KDPs are the events at which the decision authority determines the readiness of a program/project to progress to the next phase of the life cycle (or to the next KDP). Phase boundaries are defined so that they provide natural points for “go” or “no-go” decisions. Decisions to proceed may be qualified by liens that should be removed within an agreed-to time period. A program or project that fails to pass a KDP may be allowed to try again later after addressing deficiencies that precluded passing the KDP, or it may be terminated. All systems start with the recognition of a need or the discovery of an opportunity and proceed through various stages of development to the end of the project. While the most dramatic impacts of the analysis and optimization activities associated with systems engineering are obtained in the early stages, decisions that affect cost continue to be amenable to the systems approach even as the end of the system lifetime approaches.

Decomposing the program/project life cycle into phases organizes the entire process into more manageable pieces. The program/project life cycle should provide managers with incremental visibility into the progress being made at points in time that fit with the management and budgetary environments. For NASA projects, the life cycle is defined in the applicable governing document:
- For space flight projects: NPR 7120.5, NASA
Space Flight Program and Project Management Requirements
- For information technology: NPR 7120.7,
NASA Information Technology and Institutional Infrastructure Program and Project Management Requirements
- For NASA research and technology: NPR 7120.8,
NASA Research and Technology Program and Project Management Requirements
- For software: NPR 7150.2 NASA Software
Engineering Requirements

For example, NPR 7120.5 defines the major NASA life cycle phases as Formulation and Implementation. For space flight systems projects, the NASA life cycle phases of Formulation and Implementation divide into the following seven incremental pieces. The phases of the project life cycle are: Program Pre-Formulation:

- Pre-Phase A: Concept Studies
Program Formulation

- Phase A: Concept and Technology Development
- Phase B: Preliminary Design and Technology
Completion

- Phase D: System Assembly, Integration and Test,
Launch
- Phase E: Operations and Sustainment
- Phase F: Closeout
FIGURE 3.0-1 is taken from NPR 7120.5 and provides the life cycle for NASA space flight projects and identifies the KDPs and reviews that characterize the phases. More information concerning life cycles can be found in the NASA Expanded Guidance for SE document at https://nen.nasa.gov/web/se/doc-repository and in the SP-2014-3705, NASA Space Flight Program and Project Management Handbook. TABLE 3.0-1 is taken from NPR 7123.1 and represents

the product maturity for the major SE products developed and matured during the product life cycle.

Program Implementation:

- Phase C: Final Design and Fabrication
NASA Life-Cycle Phases

Approval for Formulation

Project Life-Cycle Phases

Pre-Phase A: Concept Studies

Project LifeCycle Gates, Documents, and Major Events

FAD Preliminary Project Requirements

Human Space Flight Project Life-Cycle Reviews1,2

KDP B

Phase C: Final Design and Fabrication

KDP C

KDP D

Phase F: Closeout

Phase E: Operations and Sustainment

Phase D: System Assembly, Integration & Test, Launch & Checkout

Phase B: Preliminary Design and Technology Completion

KDP E

KDP F

Launch

End of Mission

ORR FRR PLAR

CERR 4

FA Preliminary Project Plan

Baseline Project Plan

MCR

SRR SDR

CDR/ PRR3

PDR

SIR

Inspections and Refurbishment

Re-enters appropriate life-cycle phase if modifications are needed between flights MCR

SRR MDR5

PDR

Other Reviews Supporting Reviews

IMPLEMENTATION

Final Archival of Data

ASM7

Re-flights Robotic Mission Project Life Cycle Reviews1,2

Phase A: Concept and Technology Development

KDP A

Agency Reviews

Approval for

FORMULATION Implementation

DR

DRR

End of Flight PFAR

CDR/ PRR3

SIR

ORR MRR PLAR SAR 6

CERR 4

DR

DRR

SMSR,LRR (LV), FRR (LV)

Peer Reviews, Subsystem PDFs, Subsystem CDRs, and System Reviews

FOOTNOTES 1. Flexibility is allowed as to the timing, number, and content of reviews as long as the equivalent information is provided at each KDP and the approach is fully documented in the Project Plan. 2. Life-cycle review objectives and expected maturity states for these reviews and the attendant KDPs are contained in Table 2-5 and Appendix D Table D-3 of this handbook 3. PRR is needed only when there are multiple copies of systems. It does not require an SRB. Timing is notional. 4. CERRs are established at the discretion of program . 5. For robotic missions, the SRR and the MDR may be combined. 6. SAR generally applies to human space flight. 7. Timing of the ASM is determined by the MDAA. It may take place at any time during Phase A. Red triangles represent life-cycle reviews that require SRBs. The Decision Authority, Administrator, MDAA, or Center Director may request the SRB to conduct other reviews.

ACRONYMS ASM – Acquisition Strategy Meeting CDR – Critical Design Review CERR – Critical Events Readiness Review DR – Decommissioning Review DRR – Disposal Readiness Review FA – Formulation Agreement FAD – Formulation Authorization Document FRR – Flight Readiness Review KDP – Key Decision Point LRR – Launch Readiness Review LV – Launch Vehicle MCR – Mission Concept Review

MDR – Mission Definition Review MRR – Mission Readiness Review ORR – Operational Readiness Review PDR – Preliminary Design Review PFAR – Post-Flight Assessment Review PLAR – Post-Launch Assessment Review PRR – Production Readiness Review SAR – System Acceptance Review SDR – System Definition Review SIR – System Integration Review SMSR – Safety and Mission Success Review SRB – Standing Review Board SRR – System Requirements Review

FIGURE 3.0-1 NASA Space Flight Project Life Cycle from NPR 7120 .5E

TABLE 3.0-1 SE Product Maturity from NPR 7123.1

Products

Uncoupled/ Loosely Coupled

Formulation

Implementation

KDP 0

Periodic KDPs

KDP I

Tightly Coupled Programs Projects and Single Project Programs

KDP 0 PrePhase A

Phase A

KDP A MCR

KDP II

Phase B KDP B

SRR

KDP I

MDR/SDR

Phase C

Phase D

KDP C PDR

KDP D CDR

Stakeholder identification and

**Baseline

Update

Update

Update

Concept definition

**Baseline

Update

Update

Update

Update

Measure of effectiveness definition

**Approve

SIR

Cost and schedule for technical

Initial

Update

Update

Update

Update

SEMP1

Preliminary

**Baseline

**Baseline

Update

Update

Update

Requirements

Preliminary

**Baseline

Update

Update

Update

Technical Performance Measures definition

**Approve

Architecture definition

**Baseline

Allocation of requirements to next lower level

**Baseline

Required leading indicator trends

**Initial

Update

Update

Update

Design solution definition

Preliminary

**Preliminary

**Baseline

Update

Interface definition(s)

Preliminary

Baseline

Update

Update

Implementation plans (Make/ code, buy, reuse)

Preliminary

Baseline

Update

Preliminary

Baseline

Update

**Update

Preliminary

Baseline

Update

Update

Integration plans Verification and validation plans

Approach

Verification and validation results Transportation criteria and instructions Operations plans

Baseline

Operational procedures

KDP III

ORR

Update

Phase E KDP E

KDP F

FRR

DR

Update

Update

Phase F

DRR

Update

Update

**Initial

**Preliminary

Initial

Final

Update

Update

Update

**Update

Preliminary

Baseline

**Update

Update

Preliminary

**Final

Certification (flight/use)

Periodic KDPs

**Baseline

Decommissioning plans

Preliminary

Preliminary

Preliminary

**Baseline

Update

**Update

Disposal plans

Preliminary

Preliminary

Preliminary

**Baseline

Update

Update

**Update

** Item is a required product for that review 1 SEMP is baselined at SRR for projects, tightly coupled programs and single-project programs, and at MDR/SDR for uncoupled, and loosely coupled programs.

### 3.1 Program Formulation

The program Formulation Phase establishes a cost-effective program that is demonstrably capable of meeting Agency and mission directorate goals and objectives. The program Formulation Authorization Document (FAD) authorizes a Program Manager (PM) to initiate the planning of a new program and to perform the analyses required to formulate a sound program plan. The lead systems engineer provides the technical planning and concept development or this phase of the program life cycle. Planning includes identifying the major technical reviews that are needed and associated entrance and exit criteria. Major reviews leading to approval at KDP I are the SRR, SDR, PDR, and governing Program Management

Council (PMC) review. A summary of the required gate products for the program Formulation Phase can be found in the governing NASA directive (e.g., NPR 7120.5 for space flight programs, NPR 7120.7 for IT projects, NPR 7120.8 for research and technology projects). Formulation for all program types is the same, involving one or more program reviews followed by KDP I where a decision is made approving a program to begin implementation.

### 3.2 Program Implementation

During the program Implementation phase, the PM works with the Mission Directorate Associate Administrator (MDAA) and the constituent project

SPACE FLIGHT PROGRAM FORMULATION Purpose To establish a cost-effective program that is demonstrably capable of meeting Agency and mission directorate goals and objectives Typical Activities and Their Products for Space Flight Programs
- Identify program stakeholders and users
- Develop program requirements based on user expectations and allocate them to initial projects
- Identify NASA risk classification
- Define and approve program acquisition strategies
- Develop interfaces to other programs
- Start developing technologies that cut across multiple projects within the program
- Derive initial cost estimates and approve a program budget based on the project’s life cycle costs
- Perform required program Formulation technical activities defined in NPR 7120.5
- Satisfy program Formulation reviews’ entrance/success criteria detailed in NPR 7123.1
- Develop a clear vision of the program’s benefits and usage in the operational era and document it in a ConOps
Reviews
- MCR (pre-Formulation)
- SRR
- SDR

SPACE FLIGHT PROGRAM IMPLEMENTATION Purpose To execute the program and constituent projects and ensure that the program continues to contribute to Agency goals and objectives within funding constraints Typical Activities and Their Products
- Initiate projects through direct assignment or competitive process (e.g., Request for Proposal (RFP),
Announcement of Opportunity (AO)
- Monitor project’s formulation, approval, implementation, integration, operation, and ultimate
decommissioning
- Adjust program as resources and requirements change
- Perform required program Implementation technical activities from NPR 7120.5
- Satisfy program Implementation reviews’ entrance/success criteria from NPR 7123.1
Reviews
- PSR/PIR (uncoupled and loosely coupled programs only)
- Reviews synonymous (not duplicative) with the project reviews in the project life cycle (see FIGURE 3.0-4)
through Phase D (single-project and tightly coupled programs only)

managers to execute the program plan cost-effectively. Program reviews ensure that the program continues to contribute to Agency and mission directorate goals and objectives within funding constraints. A summary of the required gate products for the program Implementation Phase can be found in the governing NASA directive; e.g., NPR 7120.5 for space flight programs. The program life cycle has two different implementation paths, depending on program type. Each implementation path has different types of major reviews. It is important for the systems engineer to know what type of program a project falls under so that the appropriate scope of the technical work, documentation requirements, and set of reviews can be determined.

### 3.3 Project Pre-Phase A:

Concept Studies The purpose of Pre-Phase A is to produce a broad spectrum of ideas and alternatives for missions from which new programs/projects can be selected. During Pre-Phase A, a study or proposal team analyses a broad range of mission concepts that can fall within technical, cost, and schedule constraints and that contribute to program and Mission Directorate goals and objectives. Pre-Phase A effort could include focused examinations on high-risk or high technology development areas. These advanced studies, along with interactions with customers and other potential stakeholders, help the team to identify promising mission concept(s). The key stakeholders (including the customer) are determined and

SPACE FLIGHT PRE‑PHASE A: CONCEPT STUDIES Purpose To produce a broad spectrum of ideas and alternatives for missions from which new programs and projects can be selected. Determine feasibility of desired system; develop mission concepts; draft system-level requirements; assess performance, cost, and schedule feasibility; identify potential technology needs and scope. Typical Activities and Products
- Review/identify any initial customer requirements or scope of work, which may include:
>> Mission >> Science >> Top-level system
- Identify and involve users and other stakeholders
>> Identify key stakeholders for each phase of the life cycle >> Capture and baseline expectations as Needs, Goals, and Objectives (NGOs) >> Define measures of effectiveness
- Develop and baseline the Concept of Operations
>> Identify and perform trade-offs and analyses of alternatives (AoA) >> Perform preliminary evaluations of possible missions
- Identify risk classification
- Identify initial technical risks
- Identify the roles and responsibilities in performing mission objectives (i.e., technical team, flight, and
ground crew) including training
- Develop plans
>> Develop preliminary SEMP >> Develop and baseline Technology Development Plan >> Define preliminary verification and validation approach
- Prepare program/project proposals, which may include:
>> Mission justification and objectives; >> A ConOps that exhibits clear understanding of how the program’s outcomes will cost-effectively satisfy mission objectives; >> High-level Work Breakdown Structures (WBSs); >> Life cycle rough order of magnitude (ROM) cost, schedule, and risk estimates; and >> Technology assessment and maturation strategies.
- Satisfy MCR entrance/success criteria from NPR 7123.1
Reviews
- MCR
- Informal proposal review

expectations for the project are gathered from them. If feasible concepts can be found, one or more may be selected to go into Phase A for further development. Typically, the system engineers are heavily involved in the development and assessment of the concept options. In projects governed by NPR 7120.5, the descope options define what the system can accomplish if the resources are not available to accomplish the entire mission. This could be in the form of fewer instruments, a less ambitious mission profile, accomplishing only a few goals, or using cheaper, less capable technology. Descope options can also reflect what the mission can accomplish in case a hardware failure results in the loss of a portion of the spacecraft architecture; for example, what an orbiter can accomplish after the loss of a lander. The success criteria are reduced to correspond with a descoped mission. Descope options are developed when the NGOs or other stakeholder expectation documentation is developed. The project team develops a preliminary set of mission descope options as a gate product for the MCR, but these preliminary descope options are not baselined or maintained. They are kept in the documentation archive in case they are needed later in the life cycle. It is important in Pre-Phase A to define an accurate group of stakeholders and users to help ensure that mission goals and operations concepts meet the needs and expectations of the end users. In addition, it is important to estimate the composition of the technical team and identify any unique facility or personnel requirements. Advanced studies may extend for several years and are typically focused on establishing mission goals and formulating top-level system requirements and ConOps. Conceptual designs may be developed to demonstrate feasibility and support programmatic estimates. The emphasis is on establishing feasibility

and desirability rather than optimality. Analyses and designs are accordingly limited in both depth and number of options, but each option should be evaluated for its implications through the full life cycle, i.e., through Operations and Disposal. It is important in Pre-Phase A to develop and mature a clear vision of what problems the proposed program will address, how it will address them, and how the solution will be feasible and cost-effective.

### 3.4 Project Phase A: Concept

and Technology Development The purpose of Phase A is to develop a proposed mission/system architecture that is credible and responsive to program expectations, requirements, and constraints on the project, including resources. During Phase A, activities are performed to fully develop a baseline mission concept, begin or assume responsibility for the development of needed technologies, and clarify expected reliance on human elements to achieve full system functionality or autonomous system development. This work, along with interactions with stakeholders, helps mature the mission concept and the program requirements on the project. Systems engineers are heavily involved during this phase in the development and assessment of the architecture and the allocation of requirements to the architecture elements. In Phase A, a team—often associated with a program or informal project office—readdresses the mission concept first developed in Pre-Phase A to ensure that the project justification and practicality are sufficient to warrant a place in NASA’s budget. The team’s effort focuses on analyzing mission requirements and establishing a mission architecture. Activities become formal, and the emphasis shifts toward optimizing the concept design. The effort addresses more depth and considers many alternatives. Goals and objectives are

SPACE FLIGHT PHASE A: CONCEPT AND TECHNOLOGY DEVELOPMENT Purpose To determine the feasibility and desirability of a suggested new system and establish an initial baseline compatibility with NASA’s strategic plans. Develop final mission concept, system-level requirements, needed system technology developments, and program/project technical management plans. Typical Activities and Their Products
- Review and update documents baselined in Pre-Phase A if needed
- Monitor progress against plans
- Develop and baseline top-level requirements and constraints including internal and external interfaces,
integrated logistics and maintenance support, and system software functionality
- Allocate system requirements to functions and to next lower level
- Validate requirements
- Baseline plans
>> Systems Engineering Management Plan >> Human Systems Integration Plan >> Control plans such as the Risk Management Plan, Configuration Management Plan, Data Management Plan, Safety and Mission Assurance Plan, and Software Development or Management Plan (See NPR 7150.2) >> Other crosscutting and specialty plans such as environmental compliance documentation, acquisition surveillance plan, contamination control plan, electromagnetic interference/ electromagnetic compatibility control plan, reliability plan, quality control plan, parts management plan, logistics plan
- Develop preliminary Verification and Validation Plan
- Establish human rating plan and perform initial evaluations
- Develop and baseline mission architecture
>> Develop breadboards, engineering units or models identify and reduce high risk concepts >> Demonstrate that credible, feasible design(s) exist >> Perform and archive trade studies >> Initiate studies on human systems interactions
- Initiate environmental evaluation/National Environmental Policy Act process
- Develop initial orbital debris assessment (NASA-STD-8719.14)
- Perform technical management
>> Provide technical cost estimate and range and develop system-level cost-effectiveness model >> Define the WBS >> Develop SOWs >> Acquire systems engineering tools and models

(continued)

>> Establish technical resource estimates
- Identify, analyze and update risks
- Perform required Phase A technical activities from NPR 7120.5 as applicable
- Satisfy Phase A reviews’ entrance/success criteria from NPR 7123.1
Reviews
- SRR
- MDR/SDR

solidified, and the project develops more definition in the system requirements, top-level system architecture, and ConOps. Conceptual designs and analyses (including engineering units and physical models, as appropriate) are developed and exhibit more engineering detail than in Pre-Phase A. Technical risks are identified in more detail, and technology development needs become focused. A Systems Engineering Management Plan (SEMP) is baselined in Phase A to document how NASA systems engineering requirements and practices of NPR 7123.1 will be addressed throughout the program life cycle. In Phase A, the effort focuses on allocating functions to particular items of hardware, software, and to humans. System functional and performance requirements, along with architectures and designs, become firm as system tradeoffs and subsystem tradeoffs iterate back and forth, while collaborating with subject matter experts in the effort to seek out more cost-effective designs. A method of determining life cycle cost (i.e., system-level cost-effectiveness model) is refined in order to compare cost impacts for each of the different alternatives. (Trade studies should precede—rather than follow—system design decisions.) Major products to this point include an accepted functional baseline for the system and its major end items. The project team conducts the security categorization of IT systems required by NPR 2810.1 and Federal Information Processing Standard

Publication (FIPS PUB) 199. The effort also produces various engineering and management plans to prepare for managing the project’s downstream processes such as verification and operations.

### 3.5 Project Phase B:

Preliminary Design and Technology Completion The purpose of Phase B is for the project team to complete the technology development, engineering prototyping, heritage hardware and software assessments, and other risk-mitigation activities identified in the project Formulation Agreement (FA) and the preliminary design. The project demonstrates that its planning, technical, cost, and schedule baselines developed during Formulation are complete and consistent; that the preliminary design complies with its requirements; that the project is sufficiently mature to begin Phase C; and that the cost and schedule are adequate to enable mission success with acceptable risk. It is at the conclusion of this phase that the project and the Agency commit to accomplishing the project’s objectives for a given cost and schedule. For projects with a Life Cycle Cost (LCC) greater than $250 million, this commitment is made with the Congress and the U.S. Office of Management and Budget (OMB). This external commitment is the Agency Baseline Commitment (ABC). Systems

SPACE FLIGHT PHASE B: PRELIMINARY DESIGN AND TECHNOLOGY COMPLETION Purpose To define the project in enough detail to establish an initial baseline capable of meeting mission needs. Develop system structure end product (and enabling product) requirements and generate a preliminary design for each system structure end product. Typical Activities and Their Products
- Review and update documents baselined in previous phases
- Monitor progress against plans
- Develop the preliminary design
>> Identify one or more feasible preliminary designs including internal and external interfaces >> Perform analyses of candidate designs and report results >> Conduct engineering development tests as needed and report results >> Perform human systems integration assessments >> Select a preliminary design solution
- Develop operations plans based on matured ConOps
>> Define system operations as well as Principal Investigator (PI)/contract proposal management, review, and access and contingency planning
- Report technology development results
- Update cost range estimate and schedule data (Note that after PDR changes are incorporated and
costed, at KDP C this will turn into the Agency Baseline Commitment)
- Improve fidelity of models and prototypes used in evaluations
- Identify and update risks
- Develop appropriate level safety data package and security plan
- Develop preliminary plans
>> Orbital Debris Assessment >> Decommissioning Plan >> Disposal Plan
- Perform required Phase B technical activities from NPR 7120.5 as applicable
- Satisfy Phase B reviews’ entrance/success criteria from NPR 7123.1
Reviews
- PDR
- Safety review

engineers are involved in this phase to ensure the preliminary designs of the various systems will work together, are compatible, and are likely to meet the customer expectations and applicable requirements. During Phase B, activities are performed to establish an initial project baseline, which (according to NPR 7120.5 and NPR 7123.1) includes “a formal flow down of the project-level performance requirements to a complete set of system and subsystem design specifications for both flight and ground elements” and “corresponding preliminary designs.” The technical requirements should be sufficiently detailed to establish firm schedule and cost estimates for the project. It also should be noted, especially for AO-driven projects, that Phase B is where the toplevel requirements and the requirements flowed down to the next level are finalized and placed under configuration control. While the requirements should be baselined in Phase A, changes resulting from the trade studies and analyses in late Phase A and early Phase B may result in changes or refinement to system requirements. It is important in Phase B to validate design decisions against the original goals and objectives and ConOps. All aspects of the life cycle should be considered, including design decisions that affect training, operations resource management, human factors, safety, habitability and environment, and maintainability and supportability. The Phase B baseline consists of a collection of evolving baselines covering technical and business aspects of the project: system (and subsystem) requirements and specifications, designs, verification and operations plans, and so on in the technical portion of the baseline, and schedules, cost projections, and management plans in the business portion. Establishment of baselines implies the implementation of configuration management procedures. (See Section 6.5.)

Phase B culminates in a series of PDRs, containing the system-level PDR and PDRs for lower level end items as appropriate. The PDRs reflect the successive refinement of requirements into designs. Design issues uncovered in the PDRs should be resolved so that final design can begin with unambiguous design-to specifications. From this point on, almost all changes to the baseline are expected to represent successive refinements, not fundamental changes. As noted in FIGURE 2.5-1, significant design changes at and beyond Phase B become increasingly expensive.

### 3.6 Project Phase C:

Final Design and Fabrication The purpose of Phase C is to complete and document the detailed design of the system that meets the detailed requirements and to fabricate, code, or otherwise realize the products. During Phase C, activities are performed to establish a complete design (product baseline), fabricate or produce hardware, and code software in preparation for integration. Trade studies continue and results are used to validate the design against project goals, objectives, and ConOps. Engineering test units more closely resembling actual hardware are built and tested to establish confidence that the design will function in the expected environments. Human subjects representing the user population participate in operations evaluations of the design, use, maintenance, training procedures, and interfaces. Engineering specialty and crosscutting analysis results are integrated into the design, and the manufacturing process and controls are defined and valid. Systems engineers are involved in this phase to ensure the final detailed designs of the various systems will work together, are compatible, and are likely to meet the customer expectations and applicable requirements. During fabrication, the systems engineer is available to answer questions and work any interfacing issues that might arise.

SPACE FLIGHT PHASE C: FINAL DESIGN AND FABRICATION Purpose To complete the detailed design of the system (and its associated subsystems, including its operations systems), fabricate hardware, and code software. Generate final designs for each system structure end product. Typical Activities and Their Products
- Review and update documents baselined in previous phases
- Monitor progress against plans
- Develop and document hardware and software detailed designs
>> Fully mature and define selected preliminary designs >> Add remaining lower level design specifications to the system architecture >> Perform and archive trade studies >> Perform development testing at the component or subsystem level >> Fully document final design and develop data package
- Develop/refine and baseline plans
>> Interface definitions >> Implementation plans >> Integration plans >> Verification and validation plans >> Operations plans
- Develop/refine preliminary plans
>> Decommissioning and disposal plans, including human capital transition >> Spares >> Communications (including command and telemetry lists)
- Develop/refine procedures for
>> Refine integration >> Manufacturing and assembly >> Verification and validation
- Fabricate (or code) the product
- Identify and update risks
- Monitor project progress against project plans
- Prepare launch site checkout and post launch activation and checkout
- Finalize appropriate level safety data package and updated security plan
- Identify opportunities for preplanned product improvement
- Refine orbital debris assessment
- Perform required Phase C technical activities from NPR 7120.5 as applicable
- Satisfy Phase C review entrance/success criteria from NPR 7123.1

(continued)

Reviews
- CDR
- PRR
- SIR
- Safety review

All the planning initiated back in Phase A for the testing and operational equipment, processes and analysis, integration of the crosscutting and engineering specialty analysis, and manufacturing processes and controls is implemented. Configuration management continues to track and control design changes as detailed interfaces are defined. At each step in the successive refinement of the final design, corresponding integration and verification activities are planned in greater detail. During this phase, technical parameters, schedules, and budgets are closely tracked to ensure that undesirable trends (such as an unexpected growth in spacecraft mass or increase in its cost) are recognized early enough to take corrective action. These activities focus on preparing for the CDR, Production Readiness Review (PRR) (if required), and the SIR. Phase C contains a series of CDRs containing the system-level CDR and CDRs corresponding to the different levels of the system hierarchy. A CDR for each end item should be held prior to the start of fabrication/production for hardware and prior to the start of coding of deliverable software products. Typically, the sequence of CDRs reflects the integration process that will occur in the next phase; that is, from lower level CDRs to the system-level CDR. Projects, however, should tailor the sequencing of the reviews to meet the needs of the project. If there is a production run of products, a PRR will be performed to ensure the production plans, facilities, and personnel are ready to begin production. Phase C culminates with an SIR. Training requirements and preliminary

mission operations procedures are created and baselined. The final product of this phase is a product ready for integration.

### 3.7 Project Phase D:

System Assembly, Integration and Test, Launch The purpose of Phase D is to assemble, integrate, verify, validate, and launch the system. These activities focus on preparing for the Flight Readiness Review (FRR)/Mission Readiness Review (MRR). Activities include assembly, integration, verification, and validation of the system, including testing the flight system to expected environments within margin. Other activities include updating operational procedures, rehearsals and training of operating personnel and crew members, and implementation of the logistics and spares planning. For flight projects, the focus of activities then shifts to prelaunch integration and launch. System engineering is involved in all aspects of this phase including answering questions, providing advice, resolving issues, assessing results of the verification and validation tests, ensuring that the V&V results meet the customer expectations and applicable requirements, and providing information to decision makers for go/no-go decisions. The planning for Phase D activities was initiated in Phase A. For IT projects, refer to the IT Systems Engineering Handbook. The planning for the activities should be performed as early as possible since

SPACE FLIGHT PHASE D: SYSTEM ASSEMBLY, INTEGRATION AND TEST, LAUNCH Purpose To assemble and integrate the system (hardware, software, and humans), meanwhile developing confidence that it will be able to meet the system requirements. Launch and prepare for operations. Perform system end product implementation, assembly, integration and test, and transition to use. Typical Activities and Their Products
- Update documents developed and baselined in previous phases
- Monitor project progress against plans
- Identify and update risks
- Integrate/assemble components according to the integration plans
- Perform verification and validation on assemblies according to the V&V Plan and procedures
>> Perform system qualification verifications, including environmental verifications >> Perform system acceptance verifications and validation(s) (e.g., end-to-end tests encompassing all elements; i.e., space element, ground system, data processing system) >> Assess and approve verification and validation results >> Resolve verification and validation discrepancies >> Archive documentation for verifications and validations performed >> Baseline verification and validation report
- Prepare and baseline
>> Operator’s manuals >> Maintenance manuals >> Operations handbook
- Prepare launch, operations, and ground support sites including training as needed
>> Train initial system operators and maintainers >> Train on contingency planning >> Confirm telemetry validation and ground data processing >> Confirm system and support elements are ready for flight >> Provide support to the launch and checkout of the system >> Perform planned on-orbit operational verification(s) and validation(s)
- Document lessons learned. Perform required Phase D technical activities from NPR 7120.5
- Satisfy Phase D reviews’ entrance/success criteria from NPR 7123.1
Reviews
- Test Readiness Reviews (TRRs)
- System Acceptance Review (SAR) or pre-Ship Review
- ORR

(continued)

- FRR
- System functional and physical configuration audits
- Safety review

changes at this point can become costly. Phase D concludes with a system that has been shown to be capable of accomplishing the purpose for which it was created.

### 3.8 Project Phase E:

Operations and Sustainment The purpose of Phase E is to conduct the prime mission to meet the initially identified need and to maintain support for that need. The products of the phase are the results of the mission and performance of the system. Systems engineering personnel continue to play a role during this phase since integration often overlaps with operations for complex systems. Some programs have repeated operations/flights which require configuration changes and new mission objectives with each occurrence. And systems with complex sustainment needs or human involvement will likely require evaluation and adjustments that may be beyond the scope of operators to perform. Specialty engineering disciplines, like maintainability and logistics servicing, will be performing tasks during this phase as well. Such tasks may require reiteration and/or recursion of the common systems engineering processes. Systems engineering personnel also may be involved in in-flight anomaly resolution. Additionally, software development may continue well into Phase E. For example, software for a planetary probe may be developed and uplinked while in-flight. Another example would be new hardware developed for space station increments.

This phase encompasses the evolution of the system only insofar as that evolution does not involve major changes to the system architecture. Changes of that scope constitute new “needs,” and the project life cycle starts over. For large flight projects, there may be an extended period of cruise, orbit insertion, on-orbit assembly, and initial shakedown operations. Near the end of the prime mission, the project may apply for a mission extension to continue mission activities or attempt to perform additional mission objectives. For additional information on systems engineering in Phase E, see Appendix T.

### 3.9 Project Phase F: Closeout

The purpose of Phase F is to implement the systems decommissioning and disposal planning and analyze any returned data and samples. The products of the phase are the results of the mission. The system engineer is involved in this phase to ensure all technical information is properly identified and archived, to answer questions, and to resolve issues as they arise. Phase F deals with the final closeout of the system when it has completed its mission; the time at which this occurs depends on many factors. For a flight system that returns to Earth after a short mission duration, closeout may require little more than de-integrating the hardware and returning it to its owner. On flight projects of long duration, closeout may proceed according to established plans or may begin as a result of unplanned events, such as failures. Refer to NASA Policy Directive (NPD) 8010.3, Notification of Intent to Decommission or Terminate Operating Space Systems and Terminate Missions,

SPACE FLIGHT PHASE E: OPERATIONS AND SUSTAINMENT Purpose To conduct the mission and meet the initially identified need and maintain support for that need. Implement the mission operations plan. Typical Activities and Their Products
- Conduct launch vehicle performance assessment. Commission and activate science instruments
- Conduct the intended prime mission(s)
- Provide sustaining support as planned
>> Implement spares plan >> Collect engineering and science data >> Train replacement operators and maintainers >> Train the flight team for future mission phases (e.g., planetary landed operations) >> Maintain and approve operations and maintenance logs >> Maintain and upgrade the system >> Identify and update risks >> Address problem/failure reports >> Process and analyze mission data >> Apply for mission extensions, if warranted
- Prepare for deactivation, disassembly, decommissioning as planned (subject to mission extension)
- Capture lessons learned
- Complete post-flight evaluation reports
- Develop final mission report
- Perform required Phase E technical activities from NPR 7120.5
- Satisfy Phase E reviews’ entrance/success criteria from NPR 7123.1
Reviews
- Post-Launch Assessment Review (PLAR)
- Critical Event Readiness Review (CERR)
- Post-Flight Assessment Review (PFAR) (human space flight only)
- DR
- System upgrade review
- Safety review

PHASE F: CLOSEOUT Purpose To implement the systems decommissioning/disposal plan developed in Phase E and perform analyses of the returned data and any returned samples. Typical Activities and Their Products
- Dispose of the system and supporting processes
- Document lessons learned
- Baseline mission final report
- Archive data
- Capture lessons learned
- Perform required Phase F technical activities from NPR 7120.5
- Satisfy Phase F reviews’ entrance/success criteria from NPR 7123.1
Reviews
- DRR

for terminating an operating mission. Alternatively, technological advances may make it uneconomical to continue operating the system either in its current configuration or an improved one. To limit space debris, NPR 8715.6, NASA Procedural Requirements for Limiting Orbital Debris, provides requirements for removing Earth-orbiting robotic satellites from their operational orbits at the end of their useful life. For Low Earth Orbit (LEO) missions, the satellite is usually deorbited. For small satellites, this is accomplished by allowing the orbit to slowly decay until the satellite eventually burns up in Earth’s atmosphere. Larger, more massive satellites and observatories should be designed to demise or deorbit in a controlled manner so that they can be safely targeted for impact in a remote area of the ocean. The Geostationary (GEO) satellites at 35,790 km above the Earth cannot be practically deorbited,

so they are boosted to a higher orbit well beyond the crowded operational GEO orbit. In addition to uncertainty about when this part of the phase begins, the activities associated with safe closeout of a system may be long and complex and may affect the system design. Consequently, different options and strategies should be considered during the project’s earlier phases along with the costs and risks associated with the different options.

3.10 Funding: The Budget Cycle For a description of the NASA Budget Cycle, refer to the NASA Expanded Guidance for Systems Engineering document found at https://nen.nasa.gov/ web/se/doc-repository. See also Section 5.8 of NASA/ SP-2014-3705, NASA Space Flight Program and Project Management Handbook.

3.11 Tailoring and Customization of NPR 7123.1 Requirements In this section, the term requirements refers to the “shall” statements imposed from Agency directives. This discussion focuses on the tailoring of the requirements contained in NPR 7123.1.

3.11.1 Introduction NASA policy recognizes the need to accommodate the unique aspects of each program or project to achieve mission success in an efficient and economical manner. Tailoring is a process used to accomplish this. NPR 7123.1 defines tailoring as “the process used to seek relief from SE NPR requirements consistent with program or project objectives, allowable risk, and constraints.” Tailoring results in deviations or waivers (see NPR 7120.5, Section 3.5) to SE requirements and is documented in the next revision of the SEMP (e.g., via the Compliance Matrix). Since NPR 7123.1 was written to accommodate programs and projects regardless of size or complexity, the NPR requirements leave considerable latitude for interpretation. Therefore, the term “customization” is introduced and is defined as “the modification of recommended SE practices that are used to accomplish the SE requirements.” Customization does not require waivers or deviations, but significant customization should be documented in the SEMP. Tailoring and customization are essential systems engineering tools that are an accepted and expected part of establishing the proper SE NPR requirements for a program or project. Although tailoring is expected for all sizes of projects and programs, small projects present opportunities and challenges that are different from those of large, traditional projects such as the Shuttle, International Space Station, Hubble Space Telescope, and Mars Science Laboratory.

While the technical aspects of small projects are generally narrower and more focused, they can also be challenging when their objectives are to demonstrate advanced technologies or provide “one of a kind” capabilities. At the same time, their comparatively small budgets and restricted schedules dictate lean and innovative implementation approaches to project management and systems engineering. Tailoring and customization allow programs and projects to be successful in achieving technical objectives within cost and schedule constraints. The key is effective tailoring that reflects lessons learned and best practices. Tailoring the SE requirements and customizing the SE best practices to the specific needs of the project helps to obtain the desired benefits while eliminating unnecessary overhead. To accomplish this, an acceptable risk posture must be understood and agreed upon by the project, customer/stakeholder, Center management, and independent reviewers. Even with this foundation, however, the actual process of appropriately tailoring SE requirements and customizing NPR 7123.1 practices to a specific project can be complicated and arduous. Effective approaches and experienced mentors make the tailoring process for any project more systematic and efficient. Chapter 6 of the NASA Software Engineering Handbook provides guidance on tailoring SE requirements for software projects.

3.11.2 Criteria for Tailoring NPR 8705.4, Risk Classification for NASA Payloads, is intended for assigning a risk classification to projects and programs. It establishes baseline criteria that enable users to define the risk classification level for NASA payloads on human or non-human-rated launch systems or carrier vehicles. It is also a starting point for understanding and defining criteria for tailoring. The extent of acceptable tailoring depends on several characteristics of the program/project such as the following:

1.

Type of mission. For example, the requirements

for a human space flight mission are much more rigorous than those for a small robotic mission. 2.

Criticality of the mission in meeting the Agency Strategic Plan. Critical missions that absolutely must be successful may not be able to get relief from NPR requirements.

3.

Acceptable risk level. If the Agency and the

customer are willing to accept a higher risk of failure, some NPR requirements may be waived. 4.

National significance. A project that has great national significance may not be able to get relief from NPR requirements.

5.

Complexity.

6.

Highly complex missions may require more NPR requirements in order to keep systems compatible, whereas simpler ones may not require the same level of rigor.

Mission lifetime. Missions with a longer lifetime

need to more strictly adhere to NPR requirements than short-lived programs/projects. 7.

Cost of mission. Higher cost missions may require stricter adherence to NPR requirements to ensure proper program/project control.

8.

Launch constraints. If there are several launch

constraints, a project may need to be more fully compliant with Agency requirements.

3.11.3  Tailoring SE NPR Requirements Using the Compliance Matrix NPR 7123.1 includes a Compliance Matrix (Appendix H.2) to assist programs and projects in verifying that they meet the specified NPR requirements. The Compliance Matrix documents the program/project’s compliance or intent to comply with

the requirements of the NPR or justification for tailoring. The Compliance Matrix can be used to assist in identifying where major customization of the way (e.g., formality and rigor) the NPR requirements will be accomplished and to communicate that customization to the stakeholders. The tailoring process (which can occur at any time in the program or project’s life cycle) results in deviations or waivers to the NPR requirements depending on the timing of the request. Deviations and waivers of the requirements can be submitted separately to the Designated Governing Authority or via the Compliance Matrix. The Compliance Matrix is attached to the Systems Engineering Management Plan (SEMP) when submitted for approval. Alternatively, if there is no stand-alone SEMP and the contents of the SEMP are incorporated into another document such as the project plan, the Compliance Matrix can be captured within that plan. FIGURE 3.11-1 illustrates a notional tailoring process

for a space flight project. Project management (such as the project manager/the Principal Investigator/ the task lead, etc.) assembles a project team to tailor the NPR requirements codified in the Compliance Matrix. To properly classify the project, the team (chief engineer, lead systems engineer, safety and mission assurance, etc.) needs to understand the building blocks of the project such as the needs, goals, and objectives as well as the appropriate risk posture. Through an iterative process, the project team goes through the NPR requirements in the Compliance Matrix to tailor the requirements. A tailoring tool with suggested guidelines may make the tailoring process easier if available. Several NASA Centers including LaRC and MSFC have developed tools for use at their Centers which could be adapted for other Centers. Guidance from Subject Matter Experts (SMEs) should be sought to determine the appropriate amount of tailoring for a specific project.

Inputs

Project Needs, Goals, Objectives

Outputs

Program Office N

Engineering/Projects Directorate Tailoring Tool(s)

PM S&MA

Risk Posture

N

Review/ Approve

N

Review/ Approve

Y

Review/ Approve

Y

Center-level

CE

Suggest Tailoring

Finalize/ Update ProjectSpecific Tailoring and Capture Waiver Rationales

Project Team Review and Refine Tailoring

LSE

Y

Approved Compliance Matrix Attached to SEMP or Project Plan

Advisory Teams as Necessary

FIGURE 3.11-1 Notional Space Flight Products Tailoring Process

The Compliance Matrix provides rationales for each of the NPR requirements to assist in understanding. Once the tailoring is finalized and recorded in the Compliance Matrix with appropriate rationales, the requested tailoring proceeds through the appropriate governance model for approval.

3.

Customizing SE practices can include the following: 1.

Adjusting the way each of the 17 SE processes is implemented.

2.

Adjusting the formality and timing of reviews.

3.11.4  Ways to Tailor a SE Requirement Tailoring often comes in three areas: 1.

2.

Eliminating a requirement that does not apply to the specific program/project. Eliminating a requirement that is overly burdensome (i.e., when the cost of implementing the requirement adds more risk to the project by diverting resources than the risk of not complying with the requirement).

Scaling the requirement in a manner that better balances the cost of implementation and the project risk.

3.11.4.1  Non-Applicable NPR Requirements

Each requirement in NPR 7123.1 is assessed for applicability to the individual project or program. For example, if the project is to be developed completely in-house, the requirements of the NPR’s Chapter 4 on contracts would not be applicable. If a system does not contain software, then none of the NPR requirements for developing and maintaining software would be applicable.

3.11.4.2  Adjusting the Scope

Depending on the project or program, some relief on the scope of a requirement may be appropriate. For example, although the governing project management directive (e.g., NPR 7120.5, 7150.2, 7120.7, 7120.8) for a program/project may require certain documents to be standalone, the SE NPR does not require any additional stand-alone documents. For small projects, many of the plans can be described in just a few paragraphs or pages. In these types of projects, any NPR requirements stating that the plans need to be stand-alone document would be too burdensome. In these cases, the information can simply be written and included as part of the project plan or SEMP. If the applicable project management directive (e.g., NPR 7120.5 or NPR 7120.8) requires documents to be stand-alone, a program/project waiver/deviation is needed. However, if there is no requirement or Center expectation for a stand-alone document, a project can customize where that information is recorded and no waiver or deviation is required. Capturing where this information is documented within the systems engineering or project management Compliance Matrix would be useful for clarity. 3.11.4.3  Formality and Timing of Reviews

The governing project management directive identifies the required or recommended life cycle for the specific type of program/project. The life cycle defines the number and timing of the various reviews; however, there is considerable discretion concerning the formality of the review and how to conduct it. NPR 7123.1, Appendix G, provides extensive guidance for suggested review entrance and success criteria. It is expected that the program/ project will customize these criteria in a manner that makes sense for their program/project. The SE NPR does not require a waiver/deviation for this customization; however, departures from review elements required by other NPRs need to be addressed by tailoring those documents.

If a program/project decides it does not need one of the required reviews, a waiver or deviation is needed. However, the SE NPR does not specify a minimum amount of spacing for these reviews. A small project may decide to combine the SRR and the SDR (or Mission Definition Review (MDR)) for example. As long as the intent for both reviews is accomplished, the SE NPR does not require a waiver or deviation. (Note that even though the SE NPR does not require it, a waiver or deviation may still be required in the governing project management NPR.) This customization and/or tailoring should be documented in the Compliance Matrix and/or the review plan or SEMP. Unless otherwise required by the governing project management directives, the formality of the review can be customized as appropriate for the type of program/project. For large projects, it might be appropriate to conduct a very formal review with a formal Review Item Discrepancy (RID)/Request for Action (RFA) process, a summary, and detailed presentations to a wide audience including boards and pre-boards over several weeks. For small projects, that same review might be done in a few hours across a tabletop with a few stakeholders and with issues and actions simply documented in a word or PowerPoint document. The NASA Engineering Network Systems Engineering Community of Practice, located at https://nen.nasa.gov/web/se includes document templates for milestone review presentations required by the NASA SE process.

3.11.5  Examples of Tailoring and Customization TABLE 3.11-1 shows an example of the types of missions that can be defined based on a system that breaks projects into various types ranging from a very complex type A to a much simpler type F. When tailoring a project, the assignment of specific projects to

TABLE 3.11-1 Example of Program/Project Types

Criteria

Type A

Type B

Type C

Type D

Type E

Type F

Description of the Types of Mission

Human Space Flight or Very Large Science/ Robotic Missions

Non-Human Space Flight or Science/Robotic Missions

Small Science or Robotic Missions

Smaller Science or Technology Missions (ISS payload)

Suborbital or Aircraft or Large Ground based Missions

Aircraft or Ground based technology demonstrations

Priority (Criticality to Agency Strategic Plan) and Acceptable Risk Level

High priority, very low (minimized) risk

High priority, low risk

Medium priority, medium risk

Low priority, high risk

Low priority, high risk

Low to very low priority, high risk

National Significance

Very high

High

Medium

Medium to Low

Low

Very Low

Complexity

Very high to high

High to Medium

Medium to Low

Medium to Low

Low

Low to Very Low

Mission Lifetime (Primary Baseline Mission)

Long. >5 years

Medium. 2–5 years

Short. <2 years

Short. <2 years

N/A

N/A

Cost Guidance (estimate LCC)

High (greater than ~$1B)

High to Medium (~$500M–$1B)

Medium to Low (~$100M–$500M)

Low (~$50M–$100M)

(~$10–50M)

(less than $10–15M)

Launch Constraints

Critical

Medium

Few

Few to none

Few to none

N/A

Alternative Research Opportunities or Re-flight Opportunities

No alternative or re-flight opportunities

Few or no alternative or re-flight opportunities

Some or few alternative or re-flight opportunities

Significant alternative or re-flight opportunities

Significant alternative or re-flight opportunities

Significant alternative or re-flight opportunities

Achievement of Mission Success Criteria

All practical measures are taken to achieve minimum risk to mission success. The highest assurance standards are used.

Stringent assurance standards with only minor compromises in application to maintain a low risk to mission success.

Medium risk of not achieving mission success may be acceptable. Reduced assurance standards are permitted.

Medium or significant risk of not achieving mission success is permitted. Minimal assurance standards are permitted.

Significant risk of not achieving mission success is permitted. Minimal assurance standards are permitted.

Significant risk of not achieving mission success is permitted. Minimal assurance standards are permitted.

Examples

HST, Cassini, JIMO, JWST, MPCV, SLS, ISS

MER, MRO, Discovery payloads, ISS Facility Class payloads, Attached ISS payloads

ESSP, Explorer payloads, MIDES, ISS complex subrack payloads, PA-1, ARES 1-X, MEDLI, CLARREO, SAGE III, Calipso

SPARTAN, GAS Can, technology demonstrators, simple ISS, express middeck and subrack payloads, SMEX, MISSE-X, EV-2

IRVE-2, IRVE‑3, HiFIRE, HyBoLT, ALHAT, STORRM, Earth Venture I

DAWNAir, InFlame, Research, technology demonstrations

particular types should be viewed as guidance, not as rigid characterization. Many projects will have characteristics of multiple types, so the tailoring approach may permit more tailoring for those aspects of the project that are simpler and more open to risk and less tailoring for those aspects of the project where

complexity and/or risk aversion dominate. These tailoring criteria and definitions of project “types” may vary from Center to Center and from Mission Directorate to Mission Directorate according to what is appropriate for their missions. TABLE 3.11-2 shows an example of how the documentation required of

TABLE 3.11-2 Example of Tailoring NPR 7120.5 Required Project Products

Type A

Type B

Type C

Type D

Type E

Type F

Example Project Technical Products Concept Documentation

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Mission, Spacecraft, Ground, and Payload Architectures

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Project-Level, System and Subsystem Requirements

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Design Documentation

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Operations Concept

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Technology Readiness Assessment Documentation

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Human Systems Integration Plan

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Heritage Assessment Documentation

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Safety Data Packages

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

ELV Payload Safety Process Deliverables

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Not Applicable

Verification and Validation Report

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Operations Handbook

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Not Applicable

End of Mission Plans

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Mission Report

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Tailor

(continued)

Type A

Type B

Type C

Type D

Type E

Type F

Example Project Plan Control Plans Risk Management Plan

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Not Applicable

Technology Development plan

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Not Applicable

Not Applicable

Systems Engineering Management Plan

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Software Management plan

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Tailor

Verification and Validation Plan

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Tailor

Review Plan

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Tailor

Integrated Logistics Support Plan

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Not Applicable

Science Data Management Plan

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Not Applicable

Integration Plan

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Configuration Management Plan

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Technology Transfer (formerly Export) Control Plan

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Lessons Learned Plan

Fully Compliant

Fully Compliant

Fully Compliant

Fully Compliant

Tailor

Tailor

Human Rating Certification Package

Fully Compliant

Not Applicable

Not Applicable

Not Applicable

Not Applicable

Not Applicable

a program/project might also be tailored or customized. The general philosophy is that the simpler, less complex projects should require much less documentation and fewer formal reviews. Project products should be sensibly scaled.

3.11.6  Approvals for Tailoring Deviations and waivers of the requirements for the SE NPR can be submitted separately to the requirements owners or in bulk using the appropriate Compliance Matrix found in NPR 7123.1 Appendix

H. If it is a Center that is requesting tailoring of the NPR requirements for standard use at the Center, Appendix H.1 is completed and submitted to the OCE for approval upon request or as changes to the Center processes occur. If a program/project whose responsibility has been delegated to a Center is seeking a waiver/deviation from the NPR requirements, the Compliance Matrix in Appendix H.2 is used. In these cases, the Center Director or designee will approve the waiver/deviation.

The result of this tailoring, whether for a Center or for a program/project, should also be captured in the next revision of the SEMP along with supporting rationale and documented approvals from the requirement owner. This allows communication of the approved waivers/deviations to the entire project

team as well as associated managers. If an independent assessment is being conducted on the program/ project, this also allows appropriate modification of expectations and assessment criteria. TABLE 3.11-3 provides some examples of tailoring captured within the H.2 Compliance Matrix.

TABLE 3.11-3 Example Use of a Compliance Matrix

Req ID

SE NPR Section

Requirement Statement

Rationale

Req. Owner

Comply?

SE-05

2.1.5.2

For those requirements owned by Center Directors, the technical team shall complete the Compliance Matrix in Appendix H.2 and include it in the SEMP.

For programs and projects, the Compliance Matrix in Appendix H.2 is filled out showing that the program/project is compliant with the requirements of this NPR (or a particular Center’s implementation of NPR 7123.1, whichever is applicable) or any tailoring thereof is identified and approved by the Center Director or designee as part of the program/project SEMP.

CD

Fully Compliant

SE-06

2.1.6.1

The DGA shall approve the SEMP, waiver authorizations, and other key technical documents to ensure independent assessment of technical content.

The DGA, who is often the TA, provides an approval of the SEMPs, waivers to technical requirements and other key technical document to provide assurance of the applicability and technical quality of the products.

CD

Fully Complaint

SE-24

4.2.1

The NASA technical team shall define the engineering activities for the periods before contract award, during contract performance, and upon contract completion in the SEMP.

It is important for both the government and contractor technical teams to understand what activities will be handled by which organization throughout the product life cycle. The contractor(s) will typically develop a SEMP or its equivalent to describe the technical activities in their portion of the project, but an overarching SEMP is needed that will describe all technical activities across the life cycle whether contracted or not.

CD

Not Applicable

Justification

Project is conducted entirely in-house and therefore there are no contracts involved
