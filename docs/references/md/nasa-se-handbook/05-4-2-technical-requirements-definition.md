# 4.2 Technical Requirements Definition

> NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2. Printed pages 54–61. Machine conversion from PDF; tables and figures may be flattened. Cite as `SE HB §4.2`.

Technical Requirements Definition Process transforms the stakeholder expectations into a definition of the problem and then into a complete set of validated technical requirements expressed as “shall” statements that can be used for defining a design solution for the Product Breakdown Structure (PBS) and related enabling products. The process of requirements definition is a recursive and iterative one that develops the stakeholders’ requirements, product requirements, and lower level product/component requirements. The requirements should enable the description of all inputs, outputs, and required relationships between inputs and outputs, including constraints, and system interactions with operators, maintainers, and other systems. The requirements documents organize and communicate requirements to the customer and other stakeholders and the technical community.

NOTE: It is important to note that the team must not rely solely on the requirements received to design and build the system. Communication and iteration with the relevant stakeholders are essential

#### 4.2.1 Process Description

FIGURE 4.2-1 provides a typical flow diagram for the

Technical Requirements Definition Process and identifies typical inputs, outputs, and activities to consider in addressing technical requirements definition.
##### 4.2.1.1 Inputs

Typical inputs needed for the requirements process include the following:
- Baselined Stakeholder Expectations: This is the
agreed-to set of stakeholder expectations (e.g., needs, goals, objectives, assumptions, constraints, external interfaces) for the product(s) of this product layer.
- Baselined Concept of Operations: This describes
how the system will be operated during the life cycle phases to meet stakeholder expectations. It describes the system characteristics from an operational perspective and helps facilitate an understanding of the system goals, objectives, and constraints. It includes scenarios, use cases, and/or Design Reference Missions (DRMs) as appropriate for the project. It may be in the form of a document, graphics, videos, models, and/or simulations.

to ensure a mutual understanding of each requirement. Otherwise, the designers run the risk of misunderstanding and implementing an unwanted solution to a different interpretation of the requirements. This iterative stakeholder communication is a critically important part of project validation. Always confirm that the right products and results are being developed.

Technical requirements definition activities apply to the definition of all technical requirements from the program, project, and system levels down to the lowest level product/component requirements document.

- Baselined Enabling Support Strategies: These
describe the enabling products that were identified in the Stakeholder Expectations Definition Process as needed to develop, test, produce, operate, or dispose of the end product. They also include descriptions of how the end product will be supported throughout the life cycle.
- Measures of Effectiveness: These MOEs were
identified during the Stakeholder Expectations Definition Process as measures that the stakeholders deemed necessary to meet in order for the project to be considered a success (i.e., to meet success criteria).

Analyze scope of problem From Stakeholder Expectations Definition and Configuration Management Processes

Define design and product constraints

Baselined Stakeholder Expectations

Define performance requirements for each defined functional and behavioral expectation

Baselined Concept of Operations

Baselined Enabling Support Strategies

Measures of Effectiveness

Define functional and behavioral expectation in technical terms

To Logical Decomposition and Requirements and Interface Management Processes Validated Technical Requirements To Logical Decomposition and Technical Data Management Processes Measures of Performance

Define technical requirements in acceptable “shall” statements

To Technical Assessment Process

Validate technical requirements

Define measures of performance for each measure of effectiveness

Establish technical requirements baseline

Define technical performance measures

Technical Performance Measures

Capture work products from technical requirements definition activities

FIGURE 4.2‑1 Technical Requirements Definition Process

Other inputs that might be useful in determining the technical requirements:
- Human/Systems Function Allocation: This
describes the interaction of the hardware and software systems with all personnel and their supporting infrastructure. When human operators are a critical total-system component, the roles and responsibilities of the humans-in-the-system should be clearly understood. This should include all human/system interactions required for a mission including assembly, ground operations, logistics, in-flight and ground maintenance, in-flight operations, etc.

##### 4.2.1.2 Process Activities

4.2.1.2.1  Define Constraints, Functional and

Behavioral Expectations The top-level requirements and expectations are initially assessed to understand the technical problem to be solved (scope of the problem) and establish the design boundary. This boundary is typically established by performing the following activities:

- Defining constraints that the design needs to
adhere to or that limit how the system will be used. The constraints typically cannot be changed based on trade-off analyses.
- Identifying those elements that are already under
design control and cannot be changed. This helps

establish those areas where further trades will be made to narrow potential design solutions.
- Identifying external and enabling systems with
which the system should interact and establishing physical and functional interfaces (e.g., mechanical, electrical, thermal, human, etc.).
- Defining functional and behavioral expectations
for the range of anticipated uses of the system as identified in the ConOps. The ConOps describes how the system will be operated and the possible use-case scenarios.

interaction requirements). Crosscutting requirements include environmental, safety, human factors, and those that originate from the “-ilities” and from Design and Construction (D&C) standards. FIGURE 4.2-2 is a general overview on the flow of requirements, what they are called, and who is responsible (owns) for approving waivers.

•

Functional requirements define what functions need to be performed to accomplish the objectives.

•

Performance requirements define how well the system needs to perform the functions.

4.2.1.2.2 Define Requirements

A complete set of project requirements includes those that are decomposed and allocated down to design elements through the PBS and those that cut across product boundaries. Requirements allocated to the PBS can be functional requirements (what functions need to be performed), performance requirements (how well these functions should be performed), and interface requirements (product to product

With an overall understanding of the constraints, physical/functional interfaces, and functional/behavioral expectations, the requirements can be further defined by establishing performance and other technical criteria. The expected performance is expressed as a quantitative measure to indicate how well each product function needs to be accomplished.

EXAMPLE OF FUNCTIONAL AND PERFORMANCE REQUIREMENTS Initial Function Statement The Thrust Vector Controller (TVC) shall provide vehicle control about the pitch and yaw axes. This statement describes a high-level function that the TVC must perform. The technical team needs to transform this statement into a set of design-to functional and performance requirements. Functional Requirements with Associated Performance Requirements
- The TVC shall gimbal the engine a maximum of 9 degrees, ± 0.1 degree.
- The TVC shall gimbal the engine at a maximum rate of 5 degrees/second ± 0.3 degrees/second.
- The TVC shall provide a force of 40,000 pounds, ± 500 pounds.
- The TVC shall have a frequency response of 20 Hz, ± 0.1 Hz.

Flow

Type

Ownership

Mission Directorate Imposed Requirements

Self-Imposed Derived Requirements

Program Requirements Program Imposed Requirements

Self-Imposed Derived Requirements

“Programmatic” Requirements Ex: At least one major element shall be provided by the international community.

Project Requirements Likewise flow to Lower Level Systems

Technical Requirements

Owned by Program/ Project

All

Ex: The spacecraft shall provide a direct Earth entry capability for 11500 m/s or greater.

Owned by Technical Authority

See note*

Ex: The spacecraft shall provide a direct Earth entry capability for 11500 m/s or greater.

Ex: The system shall have a 1.4 factor of safety

* Requirements invoked by OCE, OSMA and OCHMO directives, technical standards and Center institutional requirements

FIGURE 4.2-2 Flow, Type and Ownership of Requirements

NOTE: Requirements can be generated from non-obvious stakeholders and may not directly support the current mission and its objectives, but

technical requirements from which the system will be architected and designed. FIGURE 4.2-3 shows an example of parent and child requirement flowdown.

instead provide an opportunity to gain additional benefits or information that can support the Agency

4.2.1.2.3  Define Requirements in Acceptable

or the Nation. Early in the process, the systems

Statements Finally, the requirements should be defined in acceptable “shall” statements, which are complete sentences with a single “shall” per statement. Rationale for the requirement should also be captured to ensure the reason and context of the requirement is understood. The Key Driving Requirements (KDRs) should be identified. These are requirements that can have a large impact on cost or schedule when implemented. A KDR can have any priority or criticality. Knowing the impact that a KDR has on the design allows better management of requirements.

engineer can help identify potential areas where the system can be used to collect unique information that is not directly related to the primary mission. Often outside groups are not aware of the system goals and capabilities until it is almost too late in the process.

Technical requirements come from a number of sources including functional, performance, interface, environmental, safety, human interfaces, standards and in support of the “’ilities” such as reliability, sustainability, producibility and others. Consideration and inclusion of all types of requirements is needed in order to form a complete and consistent set of

See Appendix C for guidance and a checklist on how to write good requirements and Appendix E for validating requirements. A well-written requirements

Mission Authority Mission Objectives Programmatics:
- Cost
- Schedule
- Constraints
- Mission Classification

Mission Requirements Customer Implementing Organizations

System Functional Requirements Environmental and Other Design Requirements and Guidelines

Institutional Constraints Assumptions System Performance Requirements

Subsystem A Functional and Performance Requirements

Allocated Requirements

Subsystem B

Derived Requirements

...

Subsystem C

Subsystem X Functional and Performance Requirements

Allocated Requirements

Derived Requirements

FIGURE 4.2‑3 The Flowdown of Requirements

document provides several specific benefits to both the stakeholders and the technical team as shown in TABLE 4.2-1.

request or have options for storing this type of information. TABLE 4.2-2 provides examples of the types of metadata that might be useful.

It is useful to capture information about each of the requirements, called metadata, for future reference and use. Many requirements management tools will

4.2.1.2.4 Validate Technical Requirements

An important part of requirements definition is the validation of the requirements against the stakeholder

TABLE 4.2-1 Benefits of Well-Written Requirements

Benefit

Rationale

Establish the basis for agreement between the stakeholders and the developers on what the product is to do

The complete description of the functions to be performed by the product specified in the requirements will assist the potential users in determining if the product specified meets their needs or how the product should be modified to meet their needs. During system design, requirements are allocated to subsystems (e.g., hardware, software, and other major components of the system), people, or processes.

Reduce the development effort because less rework is required to address poorly written, missing, and misunderstood requirements

The Technical Requirements Definition Process activities force the relevant stakeholders to rigorously consider all of the requirements before design begins. Careful review of the requirements can reveal omissions, misunderstandings, and inconsistencies early in the development cycle when these problems are easier to correct thereby reducing costly redesign, remanufacture, recoding, and retesting in later life cycle phases.

Provide a basis for estimating costs and schedules

The description of the product to be developed as given in the requirements is a realistic basis for estimating project costs and can be used to evaluate bids or price estimates.

Provide a baseline for verification and validation

Organizations can develop their verification and validation plans much more productively from a good requirements document. Both system and subsystem test plans and procedures are generated from the requirements. As part of the development, the requirements document provides a baseline against which compliance can be measured. The requirements are also used to provide the stakeholders with a basis for acceptance of the system.

Facilitate transfer

The requirements make it easier to transfer the product. Stakeholders thus find it easier to transfer the product to other parts of their organization, and developers find it easier to transfer it to new stakeholders or reuse it.

Serve as a basis for enhancement

The requirements serve as a basis for later enhancement or alteration of the finished product.

TABLE 4.2‑2 Requirements Metadata

Item

Function

Requirement ID

Provides a unique numbering system for sorting and tracking.

Rationale

Provides additional information to help clarify the intent of the requirements at the time they were written. (See “Rationale” box below on what should be captured.)

Traced from

Captures the bidirectional traceability between parent requirements and lower level (derived) requirements and the relationships between requirements.

Owner

Person or group responsible for writing, managing, and/or approving changes to this requirement.

Verification method

Captures the method of verification (test, inspection, analysis, demonstration) and should be determined as the requirements are developed.

Verification lead

Person or group assigned responsibility for verifying the requirement.

Verification level

Specifies the level in the hierarchy at which the requirements will be verified (e.g., system, subsystem, element).

RATIONALE The rationale should be kept up to date and include the following information:
- Reason for the Requirement: Often the reason for the requirement is not obvious, and it may be lost if
not recorded as the requirement is being documented. The reason may point to a constraint or concept of operations. If there is a clear parent requirement or trade study that explains the reason, then it should be referenced.
- Document Assumptions: If a requirement was written assuming the completion of a technology
development program or a successful technology mission, the assumption should be documented.
- Document Relationships: The relationships with the product’s expected operations (e.g., expectations
about how stakeholders will use a product) should be documented. This may be done with a link to the ConOps.
- Document Design Constraints: Constraints imposed by the results from decisions made as the design
evolves should be documented. If the requirement states a method of implementation, the rationale should state why the decision was made to limit the solution to this one method of implementation.

expectations, the mission objectives and constraints, the concept of operations, and the mission success criteria. Validating requirements can be broken into six steps:

3.

All relevant stakeholder groups identify and remove defects. 4.

1.

Are

the

Requirements

Written

5.

Are the Requirements Verifiable? All requirements should be stated in a fashion and with enough information that it will be possible to verify the requirement after the end product is implemented.

6.

Are the Requirements Redundant or Over-

Are the Requirements Technically Correct? A

few trained reviewers from the technical team identify and remove as many technical errors as possible before having all the relevant stakeholders review the requirements. The reviewers should check that the requirement statements (a) have bidirectional traceability to the baselined stakeholder expectations; (b) were formed using valid assumptions; and (c) are essential to and consistent with designing and realizing the appropriate product solution form that will satisfy the applicable product life cycle phase success criteria.

Are the Requirements Feasible? All require-

ments should make technical sense and be possible to achieve.

Correctly?

Identify and correct requirements “shall” statement format errors and editorial errors. 2.

Do the Requirements Satisfy Stakeholders?

specified? All requirements should be unique

(not redundant to other requirements) and necessary to meet the required functions, performance, or behaviors.

Requirements validation results are often a deciding factor in whether to proceed with the next process of Logical Decomposition or Design Solution Definition. The project team should be prepared to: (1) demonstrate that the project requirements are complete and understandable; (2) demonstrate that evaluation criteria are consistent with requirements and the operations and logistics concepts; (3) confirm that requirements and MOEs are consistent with stakeholder needs; (4) demonstrate that operations and architecture concepts support mission needs, goals, objectives, assumptions, guidelines, and constraints; and (5) demonstrate that the process for managing change in requirements is established, documented in the project information repository, and communicated to stakeholders.

For additional information on MOPs and TPMs, their relationship to each other and MOEs, and examples of each, see Section 6.7.2.6.2 of the NASA Expanded Guidance for SE document at https://nen. nasa.gov/web/se/doc-repository. 4.2.1.2.6 Establish Technical Requirement Baseline

Once the technical requirements are identified and validated to be good (clear, correct, complete, and achievable) requirements, and agreement has been gained by the customer and key stakeholders, they are baselined and placed under configuration control. Typically, a System Requirements Review (SRR) is held to allow comments on any needed changes and to gain agreement on the set of requirements so that it may be subsequently baselined. For additional information on the SRR, see Section 6.7.

4.2.1.2.5 Define MOPs and TPMs

Measures of Performance (MOPs) define the performance characteristics that the system should exhibit when fielded and operated in its intended environment. MOPs are derived from the MOEs but are stated in more technical terms from the supplier’s point of view. Typically, multiple MOPs, which are quantitative and measurable, are needed to satisfy a MOE, which can be qualitative. From a verification and acceptance point of view, MOPs reflect the system characteristics deemed necessary to achieve the MOEs. Technical Performance Measures (TPMs) are physical or functional characteristics of the system associated with or established from the MOPs that are deemed critical or key to mission success. The TPMs are monitored during implementation by comparing the current actual achievement or best estimate of the parameters with the values that were anticipated for the current time and projected for future dates. They are used to confirm progress and identify deficiencies that might jeopardize meeting a critical system requirement or put the project at cost or schedule risk.

4.2.1.2.7 Capture Work Products

The work products generated during the above activities should be captured along with key decisions that were made, any supporting decision rationale and assumptions, and lessons learned in performing these activities.
##### 4.2.1.3 Outputs

- Validated Technical Requirements: This is the
approved set of requirements that represents a complete description of the problem to be solved and requirements that have been validated and approved by the customer and stakeholders. Examples of documents that capture the requirements are a System Requirements Document (SRD), Project Requirements Document (PRD), Interface Requirements Document (IRD), and a Software Requirements Specification (SRS).
- Measures of Performance: These are the identified quantitative measures that, when met
by the design solution, help ensure that one or more MOEs will be satisfied. There may be
