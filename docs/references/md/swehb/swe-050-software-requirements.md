# SWE-050 - Software Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695421. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements

SWE-050 - Software Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695421)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695421&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. The Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)
* [8. Objective Evidence](#tabs-8)

# 1. Requirements

4.1.2 The project manager shall establish, capture, record, approve, and maintain software requirements, including requirements for COTS, GOTS, MOTS, OSS, or reused software components, as part of the technical specification. 

## 1.1 Notes

The software technical requirements definition process is used to transform the baselined stakeholder expectations into unique, quantitative, and measurable technical software requirements that can be used for defining a design solution for the software end products and related enabling products. This process also includes validation of the requirements to ensure that the requirements are well-formed (clear and unambiguous), complete (agrees with customer and stakeholder needs and expectations), consistent (conflict free), and individually verifiable and traceable to a higher level requirement. Recommended content for a software specification can be found in NASA-HDBK-2203.

## 1.2 History

Click here to view the history of this requirement: SWE-050 History

SWE-050 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.1.1.2 The project shall identify, develop, document, approve, and maintain software requirements based on analysis of customer and other stakeholder requirements and the operational concepts. |
| Difference between A and B | Descoped the source of software requirements.  No longer specific to the customer, stakeholder, and Ops Concept.  Added a software quality requirement. |
| B | 4.1.2.1 The project manager shall establish, capture, record, approve, and maintain software requirements, including the software quality requirements, as part of the technical specification. |
| Difference between B and C | Added requirements for COTS, GOTS, MOTS, OSS, or reused software components;  Removed software quality requirements. |
| C | 4.1.2 The project manager shall establish, capture, record, approve, and maintain software requirements, including requirements for COTS, GOTS, MOTS, OSS or reused software components, as part of the technical specification. |
| Difference between C and D | No change |
| D | 4.1.2 The project manager shall establish, capture, record, approve, and maintain software requirements, including requirements for COTS, GOTS, MOTS, OSS, or reused software components, as part of the technical specification. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) |

# 2. Rationale

Requirements are the basis for a software product. They identify the needs to be addressed by the software, its functionality and behavior within the system where it executes, the desired quality of the software, and the constraints under which the request is to be solved. They specify the product the provider is to deliver to a customer.  Requirements serve as the basis for verification activities allowing the developing organization and the customer to assess the completeness and acceptability of the product.

**Key reasons for this requirement:**

**1. Ensures Clear Understanding of System Behavior and Goals**  
Establishing and maintaining software requirements helps define what the software should achieve, how it will function, and what constraints must be adhered to. It provides a clear and shared understanding across stakeholders (developers, testers, project sponsors, and users) regarding the scope and purpose of the software. This ensures alignment between business needs, technical implementation, and project goals.

**2. Reduces Risks Related to Miscommunication**  
Capturing and recording requirements in a structured and approved format minimizes the risks of misunderstanding between stakeholders. Clearly documented requirements act as a contract between users and developers, enabling the project team to meet expectations and avoid costly rework due to missing, incorrect, or misunderstood requirements.

**3. Accommodates Unique Considerations for Various Software Types**  
The inclusion of requirements for specialized software categories—such as Commercial Off-The-Shelf (COTS), Government Off-The-Shelf (GOTS), Modified Off-The-Shelf (MOTS), Open Source Software (OSS), or reused components—ensures that each type is appropriately accounted for based on its specific characteristics:

* **COTS**: May require vendor evaluation, licensing constraints, integration requirements, and compatibility assessments.
* **GOTS**: May involve government-specific compliance and security requirements.
* **MOTS**: May need additional modifications and testing to meet project-specific needs.
* **OSS**: May include considerations for dependency management, licensing issues, and community support.
* **Reused Software Components**: Ensures proper compatibility, risk assessments for legacy systems, and testing requirements.

By explicitly including these types of software in the requirements process, the project manager ensures no key considerations are overlooked during development and deployment.

**4. Provides a Foundation for Technical Specifications**  
Documenting and approving software requirements lays the foundation for the technical specification, which guides the design and implementation phases. Requirements flow down into detailed design specifications, ensuring that the software architecture aligns with the intended functionality, performance, and constraints.

**5. Promotes Traceability and Accountability**  
Recording and maintaining requirements creates traceability throughout the software development lifecycle. Every requirement can be linked to its source (user need, regulation, contract, etc.), design implementation, and verification/validation. This promotes accountability by ensuring every decision and deliverable aligns with approved requirements.

**6. Facilitates Change Management**  
Software projects often evolve due to changing stakeholder needs, technical discoveries, or external factors. Establishing requirements and maintaining them throughout the lifecycle allows the project manager to manage changes systematically:

* Evaluate the impact of changes to requirements.
* Update associated technical specifications and development plans.
* Communicate changes to all stakeholders to preserve alignment.

**7. Enhances Quality and Performance**  
Properly established and maintained requirements improve the quality and performance of the software.

* Requirements that are clear, complete, and testable enable effective validation, ensuring the software meets user needs.
* Requirements maintenance ensures critical needs (e.g., scalability, security, compliance) are consistently adhered to during development and maintenance.

**8. Ensures Long-Term Viability of Reused and Existing Components**  
When using COTS, GOTS, MOTS, OSS, or reused components, requirements serve to verify that these components:

* Meet current system needs.
* Continue to remain viable, secure, and maintainable over time.  
  Documentation of requirements helps ensure that future upgrades, support, and integration challenges are addressed systematically.

**9. Facilitates Compliance with Standards and Regulations**  
Governments, organizations, and industries often mandate adherence to specific regulations, standards, or contractual obligations. Documenting software requirements provides evidence that the project complies with these rules, especially for COTS/GOTS software, reused components, or OSS where licensing, cybersecurity, or procurement standards may apply.

**10. Enables Verification and Validation (V&V)**  
Establishing, capturing, and approving requirements ensures they are testable and measurable. Requirements serve as the basis for verification (did we build it right?) and validation (did we build the right thing?). This ensures the final software product aligns with user needs, technical specifications, and operational goals.

**11. Reduces Integration and Maintenance Challenges**  
In projects involving mixed software types, integration is often a critical challenge. Documenting requirements specific to each type ensures compatibility and functionality when integrating diverse software components into a unified system. Additionally, proper documentation simplifies future maintenance and upgrades.

**12. Improves Decision-Making During the Software Lifecycle**  
Maintaining up-to-date requirements ensures that project decisions (such as change requests, enhancements, or replacements) are made based on a solid understanding of system needs and constraints. Decisions can be traced back to requirements, improving transparency and reducing errors caused by lack of information.

By establishing, capturing, recording, approving, and maintaining software requirements—including for specialized software types—the project manager ensures alignment, reduces risks, and provides a robust foundation for successful software development and deployment. This process ultimately drives quality, compliance, and delivery of software that meets stakeholder expectations.

# 3. Guidance

**Deficient requirements are the largest single factor in software and computing system project failure, and deficient requirements have led to a number of software-related aerospace failures and accidents.**

Faults in requirements can originate from the adoption of requirements that are incomplete, unnecessary, contradictory, unclear, unverifiable, untraceable, incorrect, in conflict with system performance requirements, otherwise poorly written, or undocumented. It is important that operators properly identify and document safety requirements, and per industry standards, ensure that safety requirements are internally consistent and valid at the system level for the resulting computing system to work safely throughout its lifecycle.

## 3.1 Requirements Definition

Software requirements have their basis in customer requirements, system-level parent requirements, and operational concepts. The decomposition of these higher-level requirements and concepts is required to develop and document the requirements for the software. Clearly defined, well-written, and accurately captured requirements reduce "costly redesign, remanufacture, recoding, and retesting in later life cycle phases."  [273](#_tabs-<p></p>) Well-written requirements also provide "a realistic basis for estimating project costs and can be used to evaluate bids or price estimates" and "provide the stakeholders with a basis for acceptance of the system." [273](#_tabs-<p></p>)

The requirements definition activity provides a common understanding of the derived technical requirements, a logical decomposition model, traceability to technical requirements, and an understanding of the stakeholder's expectations.

The software technical requirements definition process is used to transform the baselined stakeholder expectations into unique, quantitative, and measurable technical software requirements that can be used for defining a design solution for the software end products and related enabling products. This process also includes validation of the requirements to ensure that the requirements are well-formed (clear and unambiguous), complete (agrees with customer and stakeholder needs and expectations), consistent (conflict free), and individually verifiable and traceable to a higher level requirement. Recommended content for a software specification can be found in this NASA-HDBK-2203 under Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)[.](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)

A general process flow for capturing, approving, and maintaining software requirements is shown below:

General Process Flow for Capturing, Approving, and Maintaining Software Requirements

Requirements are allocated or derived.

***Allocated requirements***: A requirement that is established by analyzing and decomposing a high-level requirement into multiple lower-level requirements.

***Derived Requirements***: Requirements arising from constraints, consideration of issues implied but not explicitly stated in the high-level direction provided by NASA Headquarters and Center institutional requirements, factors introduced by the selected architecture, and the design. These requirements are finalized through requirements analysis as part of the overall systems engineering process and become part of the program or project requirements baseline. (NASA/SP-2016-6105)

## 3.2 Requirements Decomposition and Flowdown

According to the NASA Systems Engineering Handbook [273](#_tabs-<p></p>) , requirements are decomposed in a hierarchical structure starting with the highest level requirements imposed by Presidential directives, mission directorates, programs, NASA Agency, customers, and other stakeholders. These high-level requirements are decomposed into functional and performance requirements and allocated across the system. These are then further decomposed and allocated among the elements and subsystems. This decomposition and allocation process continues until a complete set of design-to requirements is achieved. At each level of decomposition (system, subsystem, component, etc.), the total set of allocated and derived requirements must be validated against the stakeholder expectations or higher-level parent requirements before proceeding to the next level of decomposition. The traceability of requirements to the lowest level ensures that each requirement is necessary to meet the stakeholder's expectations. Requirements that are not allocated to lower levels or are not implemented at a lower level can result in a design that does not meet objectives/expectations and is, therefore, not valid. Conversely, lower-level requirements that are not traceable to higher-level requirements may result in an overdesign that is not justified (i.e., the term “gold plating”).   The figure below from the NASA Systems Engineering Handbook illustrates this hierarchical flow down.

NASA/SP-2016-6105: NASA Systems Engineering Handbook - FIGURE 4.2-3 The Flow Down of Requirements

**NASA/SP-2016-6105: NASA Systems Engineering Handbook - FIGURE 4.2-3 The Flow Down of Requirements**

This flow addresses requirements development via the nominal system flow-down process. However, software requirements can also be developed /matured with the system (i.e., in a spiral/incremental/agile fashion), especially when software plays a key role in the integration and buildup of the system.

Tips for the decomposition of requirements – Figure 3.2 below illustrates some of the concepts presented here:

* System requirements are general requirements; allocated, flowed-down requirements are more detailed as the levels progress.
* Decompose or partition the system into finer and finer (more detailed) elements (into a functional, physical, data-driven, or object-oriented hierarchy); each element in this hierarchy has its requirements that work together to meet the higher-level requirements. [178](#_tabs-<p></p>)
* All top-level requirements must be allocated to at least one element at the next level and have at least one flowed down requirement associated with it at that lower level. [178](#_tabs-<p></p>)
* The Software Lead works with the Systems Lead to identifying system requirements that are allocated to the software development effort.
* Examine each top-level requirement to identify the software requirements necessary to accomplish that requirement and fulfill the function it describes.
* After systems engineers allocate system requirements to subsystems, such as the software subsystem, software engineers develop the requirements for those elements.
* Identify input, output, and processing needed to satisfy the high-level requirements using an analysis method focusing on what the software needs to do rather than specific 'how-to' details.
* Decompose requirements into a "set of make-to, buy-to, code-to, and other requirements from which design solutions can be accomplished." [273](#_tabs-<p></p>)
* The lowest level may be the module level for software. [178](#_tabs-<p></p>)
* Typically, an iterative process as successive lower-level functional and performance requirements are defined at ever-increasing levels of detail; this can point out additions, changes, and deletions that need to occur in parent requirements   [178](#_tabs-<p></p>)
* Iteratively repeat allocation and requirements development (flow down) at each successively lower level.
* May need to revise parent requirements as new information is obtained at the lower, more detailed levels [178](#_tabs-<p></p>)
* Maintain a link to parent requirement (i.e., lower-level requirements need to support requirements at the next higher level, and it may be helpful to document in the rationale what the lower-level requirement does to support the parent requirement).
* Derived requirements will be created during this process; derived requirements are requirements that differ from the parent requirement, but state a capability the lower-level element (subsystem or lower) must have to meet the parent requirement. [178](#_tabs-<p></p>)
* Consider constraints (e.g., cost, standards, regulations).
* Decomposition may be based on or influenced by a project hierarchy for the software subsystem.
* Resolve requirements conflicts.
* Lessons learned from previous decomposition activities may be helpful; SEI’s Requirements Engineering [178](#_tabs-<p></p>) article also provides a good overview of requirements allocation and flow down.

Requirements Decomposition Process

**Figure 3.2: Requirements Decomposition Process**

## 3.3 Requirements identification, development, documentation

Requirements are typically documented in a Software Requirements Specification (SRS) and a Software Data Dictionary (SDD) document. Additionally, software interface requirements may be captured in an Interface Control Document (ICD) or an Interface Design Document (IDD), along with hardware interface requirements. If an ICD or IDD is used, the SRS references that document. Guidance for the content and development of these documents, including requirements identification and development based on operational concepts and customer and stakeholder requirements, is located in topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance).

* [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
* [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary)
* [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description)

The following roles may be involved in establishing and documenting software requirements, including quality requirements, as appropriate for the project:

* Project stakeholders, including customers and senior management
* Software Lead
* Software Requirements Engineer
* Systems Engineer
* Software Architects
* Software Assurance Engineer

Note: For small projects, an engineer or software developer may fulfill multiple roles.

Projects that use modeling and simulation as part of the development process may choose to develop and document requirements using models or both text and models. The use of models augments the text forms by providing computer executable and transformable information that is free from ambiguity and needed by the engineers who will design according to the specifications." [292](#_tabs-<p></p>)

Requirements documentation includes bidirectional traceability through the software life cycle phases. See guidance in [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) for a discussion of requirements traceability.

When capturing software requirements, it is important to:

* Document key decisions and the person(s) who made them, for example:
  + Which requirements are "must-have."
  + Prioritization of requirements.
  + Stakeholder decisions that form the basis for requirements.
  + Resolutions to conflicting requirements.
  + How High-level design choices affect low-level requirements.
* Develop and document requirement rationales, for example:
  + Reasons why one feature or performance requirement was chosen over another.
  + Originating document or basis for a requirement, e.g., operational concepts document, trade study, parent requirement.
  + Stakeholder expectations.
  + Risks that are the basis for a requirement.
  + Technology limitations.
  + Time constraints.
  + Regulations and laws.
* Define assumptions and limitations, for example:
  + Environmental or any other constraints (e.g., O/S – Unix/Linux vs PC, endianness)
  + Mission type (e.g., human-rated vs. robotic).
  + Assumed technology availability (e.g., hardware – PLDs, PC; O/S; programming language; simulators)
  + Preset budgetary restrictions and schedule constraints.
* Logically decompose the requirements.
* Document requirements for COTS, GOTS, MOTS, OSS, or reused software components, as part of the technical specification.

## 3.4 Information Sources

Defining software requirements involves eliciting, generating, and analyzing customer, product, and product component requirements. Inputs to this process may include:

* System and subsystem requirements documents, hardware schematics, and specifications. System architecture.
* System models and simulations.
* System safety analyses, including the preliminary hazard analysis (PHA), subsequent system hazard analyses, and software safety analyses. Environmental requirements, including operations and hardware requirements, vehicle, or facility requirements. Standards.
* External regulations.
* Program/project specification.
* Operational concepts document.
* Interface requirements.
* Legacy products.
* Organizational requirements.
* Quality attributes (e.g., reliability, availability, security, safety, maintainability, portability, usability).
* Stakeholder input or user needs (provided or elicited via interviews, brainstorming sessions, prototypes, questionnaires, surveys, or other techniques).
  + Structured interviews with customers, users, and other subsystem engineers (e.g., electrical/electronic and data; thermal; Guidance, Navigation, and Control (GN&C); mechanical). may include the development of scenarios, the examination of reports, and analysis of competing products.

See also Topic [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009)

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Product Requirements related to Human Rated Software.

## 3.5 General Guidance

Some general guidelines to follow when establishing and documenting software requirements include:

* Provide a unique identifier for each requirement.
* Express requirements as "shall" statements (avoiding words like "could," "should," "must," and "will").
* Identify software safety requirements.
* Write the requirements so they are:

* + Complete, correct, and consistent
  + Traceable
  + Independent
  + Unambiguous
  + Modifiable
  + Understandable
  + Necessary
  + Measurable
  + Quantitative
  + Finite (establish limits or bounds in the requirement)
  + Testable
  + Maintainable
  + Feasible
* Refine the initial set of requirements into a manageable set (e.g., remove duplicates, remove unnecessary requirements, combine requirements, clarify requirements, keep "must-haves", and drop some "nice-to-haves").
* Have requirements reviewed by stakeholders (to identify and address ambiguous, conflicting, incomplete requirements; peer reviews/inspections are one technique that can be used for this purpose).
* Capture software requirements in the required documents and a requirements management tool for easy access, modification, and management; some tools may allow for the generation of the requirements documents directly from the tool.
* State the requirements, not how to fulfill them.
* State only one requirement per statement (i.e., avoid compound requirements). Use short, direct, complete sentences.
* Make requirements internally and externally consistent.
* Define a testing strategy for each requirement as soon as it is specified.

See also [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices), [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access),

See also [PAT-013 - Software Requirements Checklist](/spaces/SITE/pages/114328303/PAT-013+-+Software+Requirements+Checklist),

Good Software Requirements

A good software requirement should have the following characteristics:

* Implementation-Neutral: Functional requirements should not restrict design engineers to a particular implementation. They should be free of design details and focus on what the system must do rather than how it must do it.
* Testable: Each requirement should be stated so that an objective test can be defined for it. This ensures that both design and test engineers understand exactly what to do and how to verify successful implementation.
* Consistent with Imperatives: Use imperative terms like "shall" for binding provisions, "must" for expressing constraints and non-functional requirements, and "will" for declarations of purpose. Consistency in using these terms helps in clear communication and understanding of the requirements.
* Hierarchical Organization: Organize requirements hierarchically to focus on specific domains and ensure comprehensive coverage. This also helps in easily finding and modifying areas in the baseline specification when adding functionality.
* Standardized Language: Standardize the language used in requirements to reduce ill-definition and misinterpretation. Define how terms like "shall," "will," and "should" are used within the document.
* Unique Identifiers: Tag each requirement with a project-unique identifier to improve and simplify traceability between requirements and verification tests. This helps in demonstrating compliance with top-level requirements and makes it easier to reference requirements within the document.
* Concise: Requirements should be concise and use accepted requirement sentence structures. This includes a unique ID, object, provision/imperative, action, condition, and optional declaration of purpose or expected occurrence.

By adhering to these principles, software requirements can be clear, comprehensive, and manageable, facilitating better design, implementation, and testing processes.

## 3.6 Common Problems

Establishing and documenting requirements is not a simple task. According to Kandt, Ronald Kirk, Jet Propulsion Lab, "Software Quality Improvement, Software Requirements Engineering: Practices and Techniques", (JPL Document D-24994, 2003) 061, common problems that occur during or because of this activity and which are to be avoided, include:  
•    Failing to define needed requirements, including safety requirements.  
•    Writing requirements inconsistently or ambiguously.  
•    Using inexperienced personnel or personnel with insufficient domain knowledge to define the requirements.  
•    Incorrect understanding of underlying assumptions or constraints.  
•    Including unneeded features or capabilities.  
•    No clear method for allocating requirements to software subsystems.  
•    Choosing solutions before defining the requirements and/or user needs.  
•    Failing to spend enough time or resources on requirements definition.

To help detect and avoid some of these common problems, there are tools available to aid in the detection of requirements quality issues. One such tool that NASA has acquired licensing for is [QVScribe](https://qracorp.com/take-the-tour/try-qvscribe/). QVScribe analyzes the requirements (Word, Excel, or Doors) and provides feedback to the user on their quality. Access to QVScribe is available via a NAMS request.

Guidance for baselining and updating the SRS in preparation for life cycle milestone reviews can be found in topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) in this Handbook.

## 3.7 Benefits of Well-Written Requirements

A well-written requirements document provides several specific benefits to both the stakeholders and the technical team as shown in TABLE 4.2-1 from NASA SP-2016-6105 Rev2: Systems Engineering Handbook.

## 3.8 Requirements Metadata

It is useful to capture information about each of the requirements, called metadata, for future reference and use. Many requirements management tools will request or have options for storing this type of information. TABLE 4.2-2 from NASA SP-2016-6105 Rev2: Systems Engineering Handbook provides examples of the types of metadata that may be useful.

Recommended practice is to include a rationale for eachrequirement or group of requirements. The rationale should be captured to ensure the reason and context of the requirement is understood. The following reasoning was captured from NASA SP-2016-6105 Rev2: Systems Engineering Handbook:

  

A requirements database (e.g., DOORS) is an extremely useful tool for capturing the requirements and the associated metadata and for showing the bidirectional traceability between requirements. The database evolves and could be used for tracking status information related to requirements such as To Be Determined (TBD)/To Be Resolved (TBR) status, resolution date, and verification status. Each project should decide what metadata will be captured. The database is usually in a central location that is made available to the entire project team. For small projects, an acceptable alternative would be to use a spreadsheet.

## 3.9 Requirements Approval

Requirements review and approval is necessary to ensure that they accurately capture user needs and project goals and objectives.  Once requirements are identified, developed, and documented, they are evaluated, analyzed ([SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis)), and approved in light of stakeholder requirements and operational concepts by one or more of the following, based on project procedures:

* Project management: Approves formalized requirements (as documented in the SRS, Data Dictionary, and/or ICD.
* Customer/Stakeholders: Approve formalized requirements.
* Systems engineering: Reviews software requirements under the direction of project management.
* Software Assurance: Analyzes the requirements and assesses their quality, and audits the requirements document(s) against software engineering requirements.
* Review board: A milestone review, such as the Software Requirements Review (SwRR), a Technical Exchange Meeting (TIM), or both, is conducted; if both are performed, the TIM should precede the SwRR.

Changes from any of these reviews or approval processes should be incorporated into the software requirements work product before they proceed to the next step in the project life cycle.  Approved requirements are baselined and maintained in the project’s configuration management system. The approved requirements establish the agreement between the developing organization and customer on what the software must do when it is delivered.

See also [PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist),

## 3.10 Requirements Maintenance

Maintenance of software requirements is needed because they typically change throughout the project based on information and experiences obtained during the project life cycle.

Managing requirements change is a critical aspect of requirements maintenance because changes to requirements can be an indicator of software instability and often mean increased costs, longer schedules, rework, and can affect software safety. Guidance for [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) addresses managing requirements changes throughout the project and guidance for [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) addresses correcting inconsistencies among requirements and project products.

Requirements must be updated in the requirements management tool (if one is used) as well as the requirements documents (e.g., SRS, Data Dictionary, ICD). Those updated requirements are made available to all stakeholders, including developers, testers, managers, and anyone else making decisions or performing work based on software requirements.

## 3.11 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices)        * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.21 - Software Requirements Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641581/5.21+-+Software+Requirements+Analysis+Report+Minimum+Content) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [PAT-013 - Software Requirements Checklist](/spaces/SITE/pages/114328303/PAT-013+-+Software+Requirements+Checklist) * [PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist) |

## 3.12 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements) |

# 4. Small Projects

Any small projects with limited resources, it is critical to prioritize features, functional requirements, or use cases to ensure efficient project execution. Here is clear and concise guidance to help small project teams manage requirements effectively, make trade-offs, and maintain alignment with project goals. This approach minimizes the risks of scope creep and last-minute de-scoping, which can compromise both quality and delivery timelines.

### **1.** **Prioritization of Requirements**

In resource-constrained environments, prioritizing the requested features, use cases, or functional requirements helps the project team focus on delivering the most critical objectives. Prioritization enables the project manager to plan effectively for:

* **Staged Releases**: Ensuring that high-priority features are implemented first, delivering incremental value to stakeholders.
* **Trade-Off Decisions**: Providing a basis for deciding which items take precedence when conflicts arise.
* **Scope Control**: Preventing last-minute “fire drills” by clearly identifying which features can be deferred, removed, or re-scoped based on available resources.

#### Practical Tip:

* Use simple prioritization techniques, such as **MoSCoW** (Must-have, Should-have, Could-have, Won't-have) analysis or a **priority scale (e.g., 1-5)**, to rank features by their importance and impact.
* Engage stakeholders early and often to validate the prioritization.

### **2.** **Role Assignment in Small Projects**

In small projects, team members often take on multiple roles to minimize resource overhead and increase efficiency. For instance:

* A software engineer might also serve as the Requirements Analyst or Test Engineer.
* A single team member may oversee both software design and implementation.

#### Guidance for Role Assignment:

* The **Project Manager has the discretion** to assign roles as appropriate to each team member’s skills and project needs.
* Ensure that the responsibility for critical project functions (e.g., requirements management, quality assurance, and configuration management) is clearly assigned—even if combined roles are being fulfilled.

### **3.** **Simplified Documentation Strategy**

To reduce the overhead associated with generating multiple documents, small projects may consolidate work products into a **single comprehensive document**. However, the content requirements for each document type should still be addressed to ensure no critical information is omitted.

#### Consolidated Documentation Tips:

* Include distinct **sections** that align with the required content for each document type (see *Topic 7.18 - Documentation Guidance* for recommended structure).
* Use a clear Table of Contents or section headers to differentiate document content.
* Avoid excessive formality—keep the document lean, focusing only on what is necessary to guide the project team.

### **4. Using Tools for Requirements Management**

A requirements management system is a valuable tool for capturing, tracking, and maintaining bidirectional traceability between requirements. For small projects, adopting lightweight tools is often a more practical approach than using enterprise-level systems like DOORS.

#### Small Project Tool Options:

* **Excel Spreadsheets or Word Files**: These tools offer a simple, cost-effective way to:
  + Track requirements and their metadata.
  + Maintain traceability between requirements, design, verification, and testing.
  + Record status fields such as *To Be Determined (TBD)*, *To Be Resolved (TBR)*, resolution dates, and verification status.
* **Guidance for Traceability**:
  + Create a column-based structure in Excel for metadata fields (e.g., ID, Requirement Description, Priority, Traceability, Status, etc.).
  + Use tables in Word to create simple requirement-traceability matrices.

### **Conclusion**

Adopting these streamlined practices enables small projects to efficiently manage their constraints while maintaining high-quality deliverables. Prioritization ensures resource focus on the most critical outcomes, flexible role assignment reduces unnecessary overhead, consolidated documentation saves time while maintaining structure, and simple tools (such as Excel or Word) provide practical solutions for requirements tracking and traceability. Through these strategies, small projects can deliver success without over-complicating their processes.

Additional guidance specific to small projects may be found in the following related requirements in this Handbook:

|  |
| --- |
| [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) |
| [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) |
| [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) |

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-061)

  [Software Requirements Engineering: Practices and Techniques,](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=875d04783add30ea3ed1381f682207a992169ebc "Click to open in new window")

  JPL Document D-24994, NASA Jet Propulsion Laboratory, 2003.
   See Page 20.
  Approved for U.S. and foreign release.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-178)

  ["Requirements Engineering." News at SEI,](https://resources.sei.cmu.edu/library/ "Click to open in new window")

  Dorfman, Merlin, Software Engineering Institute. (March, 1999).  Multiple resources are available by searching Requirements Engineering at this site.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-292)

  [Engineering Complex Systems with Models and Objects,](https://books.google.com/books/about/Engineering_Complex_Systems_with_Models.html?id=KuoeAQAAIAAJ "Click to open in new window")

  Oliver, D., Kelliher, T., Keegan, J., New York: McGraw-Hill, 1997.
* (SWEREF-358)

  [When Telepathy Won't Do: Requirements Engineering Key Practices,](http://www.processimpact.com/articles/telepathy.html "Click to open in new window")

  Wiegers, K. E. (May, 2000).  Cutter IT Journal. Retrieved November 3, 2014 from http://www.processimpact.com/articles/telepathy.html.
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.
* (SWEREF-531)

  [Chandra X-ray Observatory (CXO) Development Program Programmatic "Lessons Learned"](https://llis.nasa.gov/lesson/987 "Click to open in new window")

  Public Lessons Learned Entry: 987.
* (SWEREF-549)

  [Risk Assessment in Software Development Projects](https://llis.nasa.gov/lesson/1321 "Click to open in new window")

  Public Lessons Learned Entry: 1321.
* (SWEREF-551)

  [Lessons Learned From Flights of ?Off the Shelf? Aviation Navigation Units on the Space Shuttle, GPS](https://llis.nasa.gov/lesson/1370 "Click to open in new window")

  Public Lessons Learned Entry: 1370.
* (SWEREF-566)

  [The Pitfalls of "Engineering-by-Presentation" (2005)](https://llis.nasa.gov/lesson/1715 "Click to open in new window")

  Public Lessons Learned Entry: 1715.
* (SWEREF-572)

  [Flight Software Engineering Lessons](https://llis.nasa.gov/lesson/2218 "Click to open in new window")

  Public Lessons Learned Entry: 2218.
* (SWEREF-576)

  [Software Requirements Management](https://llis.nasa.gov/lesson/3377 "Click to open in new window")

  Public Lessons Learned Entry: 3377.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Process Asset Templates

**SWE-050 Process Asset Templates**

Click on a link to download a usable copy of the template.

* (PAT-013 - )

  [PAT-013 - Software Requirements Checklist,](https://swehb.nasa.gov/download/attachments/114328303/PAT-013%20-%20Software%20Requirements%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.1, Also in Peer Review and Requirements Analysis categories.
* (PAT-034 - )

  [PAT-034 - SA Requirements Analysis Checklist](https://swehb.nasa.gov/download/attachments/154501148/PAT-034%20-%20SA%20Requirements%20Analysis%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, Tab 2.3.1 - SA Requirements Analysis Checklist
* (PAT-042 - )

  [PAT-042 - Requirements Development and Mgmt Audit](https://swehb.nasa.gov/download/attachments/198770759/PAT-042%20-%20Requirements%20Development%20and%20Mgmt%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to Software Requirements Development and Management.
* (PAT-055 - )

  [PAT-055 - Software Data Dictionary Assessment](https://swehb.nasa.gov/download/attachments/198770882/PAT-055%20-%20Software%20Data%20Dictionary%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Data Dictionary. Based on the minimum recommended content for a Software Data Dictionary.
* (PAT-056 - )

  [PAT-056 - Software Development Management Plan Assessment](https://swehb.nasa.gov/download/attachments/198770884/PAT-056%20-%20Software%20Development%20Management%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Development - Management Plan. Based on the minimum recommended content for a Software Development - Management Plan.
* (PAT-059 - )

  [PAT-059 - Software Requirements Specification Assessment](https://swehb.nasa.gov/download/attachments/198770890/PAT-059%20-%20Software%20Requirements%20Specification%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Requirements Specification. Based on the minimum recommended content for a Software Requirements Specification.

**Requirements Development and Analysis Process Asset Templates**

Click on a link to download a usable copy of the template. (ReqAn)       10/2/2025 - 10 items

**Requirements Development and Analysis Process Asset Templates**

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
* (PAT-042 - )

  [PAT-042 - Requirements Development and Mgmt Audit](https://swehb.nasa.gov/download/attachments/198770759/PAT-042%20-%20Requirements%20Development%20and%20Mgmt%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to Software Requirements Development and Management.
* (PAT-059 - )

  [PAT-059 - Software Requirements Specification Assessment](https://swehb.nasa.gov/download/attachments/198770890/PAT-059%20-%20Software%20Requirements%20Specification%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Requirements Specification. Based on the minimum recommended content for a Software Requirements Specification.
* (PAT-079 - )

  [PAT-079 - Requirements Quality Checklist](https://swehb.nasa.gov/download/attachments/207290572/PAT-079%20-%20Requirements%20Quality%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.2 Requirements Quality Checklist
* (PAT-080 - )

  [PAT-080 - Requirements Contents Checklist](https://swehb.nasa.gov/download/attachments/207290574/PAT-080%20-%20Requirements%20Content%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.3 Requirements Contents Checklist
* (PAT-081 - )

  [PAT-081 - Requirements Editorial Checklist](https://swehb.nasa.gov/download/attachments/207290577/PAT-081%20-%20Requirements%20Editorial%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.54, 2.3.4 Requirements Editorial Checklist The purpose of this checklist is to aid the analyst when reviewing the software requirements from an editorial perspective.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following lessons learned from the NASA Lessons Learned database highlight best practices and potential pitfalls in the areas of software requirements identification, development, documentation, approval, and maintenance. These lessons are derived from historical experiences, emphasizing the critical role of understanding and managing customer/stakeholder requirements and operational concepts. Additional relevant lessons have been integrated to offer a more comprehensive perspective.

### **1. Customer Collaboration in Requirements Definition**

**[Software Requirements Management (Customer Role in Requirements Definition)] - Lesson Number 3377 [576](#_tabs-<p></p>)**

* **Lesson:** A collaborative relationship between the users/customers of the software and the development team is paramount for project success. Customers should:
  + Effectively define and communicate their requirements.
  + Provide requirements that are: **clear, concise, unambiguous, complete, independent, implementable, and testable**.
* **Key Takeaway:** Active involvement of the customer ensures accurate requirements that reduce miscommunication, rework, and project risks. Establishing clear communication channels and iterative reviews fosters a shared vision and better alignment.

### **2. Risks of Informal Communication and "Engineering-by-Presentation"**

**[The Pitfalls of "Engineering-by-Presentation"] - Lesson Number 1715 [566](#_tabs-<p></p>)**

* **Lesson:** Relying on informal documentation, such as presentation slides and emails, compromises the ability to reference, verify, and validate critical requirements and technical decisions. Formal documentation of requirements, resolutions, and decisions—along with the basis and justification for each engineering choice—is essential.
* **Key Takeaway:** Maintain formal records of all requirements and engineering decisions to support traceability, long-term project understanding, and the ability to adapt to unforeseen changes.

### **3. Uncertainty Due to Changing Requirements**

**[Risk Assessment in Software Development Projects] - Lesson Number 1321 [549](#_tabs-<p></p>)**

* **Lesson:** Requirements uncertainty, such as changes during the design phase, introduces risks and technical challenges, even with an experienced development team. This can lead to delays, resource overruns, and quality issues.
* **Key Takeaway:** Stabilize and manage requirements change by implementing a robust change management process. Focus on identifying and addressing potential areas of uncertainty early in the software lifecycle to reduce risks.

### **4. Importance of Complete and Consistent Requirements**

**[Flight Software Engineering Lessons] - Lesson Number 2218 [572](#_tabs-<p></p>)**

* **Lesson:** Developing a complete and consistent set of engineering requirements relies on a robust systems engineering process. Key elements include:
  + Defining clear performance and resource utilization requirements.
  + Tracing requirements to higher and lower levels.
  + Engaging key stakeholders and independent reviewers.
  + Using a checklist to address quality concerns.
* **Key Takeaway:** A comprehensive and systematic approach to requirements ensures that all functional, operational, and technical aspects are addressed, reducing the risk of gaps or inconsistencies.

### **5. Prioritizing COTS/GOTS/MOTS Software Requirements**

**[Lessons Learned From Flights of "Off the Shelf" Aviation Navigation Units on the Space Shuttle GPS] - Lesson Number 1370 [551](#_tabs-<p></p>)**

* **Lesson:** When working with commercially sourced software (COTS), government off-the-shelf software (GOTS), or modified off-the-shelf software (MOTS), prioritize requirements as follows:
  + **Must meet**: Essential requirements for mission success.
  + **Highly desirable**: Non-essential but beneficial features.
  + **Nice to have**: Optional features that improve performance or usability.
* **Key Takeaway:** Clear prioritization of requirements helps evaluate the suitability of off-the-shelf solutions and guides procurement decisions considering cost, feasibility, and performance.

### **6. Including Hardware-Driven Software Requirements**

**[Probable Scenario for Mars Polar Lander Mission Loss] - Lesson Number 0938 [529](#_tabs-<p></p>)**

* **Lesson:** Software requirements must incorporate known hardware operational characteristics, including transients, spurious signals, and other hardware-specific behavior. These interactions must be validated and verified through thorough testing.
* **Key Takeaway:** Ensure close collaboration between hardware and software teams to capture dependencies, prevent conflicts, and verify that software requirements account for all operational scenarios.

### **7. Stable Requirements for Program Stability**

**[Chandra X-ray Observatory (CXO) Development Program Programmatic "Lessons Learned"] - Lesson Number 0987 [531](#_tabs-<p></p>)**

* **Lesson:** Stable requirements are critical for program stability. To avoid scope creep:
  + Involve all stakeholders—developers, operations teams, contractors, and NASA Headquarters—in developing and finalizing the requirements.
  + Incorporate strong systems engineering practices for requirements traceability and verification.
  + Include operations in the early stages of requirements definition and design.
* **Key Takeaway:** Stability in requirements fosters consistency, reduces risk, and aligns cross-functional stakeholders. Early engagement of all relevant parties minimizes the risk of downstream changes that disrupt the project.

### **8.**In Class D, Fault Protection Becomes the Safety Net—So It Must Be Excellent

**Problem/Observation:**  
Class D missions accept higher hardware and redundancy risk, which places greater reliance on software‑based fault protection (FP). The Anomaly Review Board (ARB) emphasized that FP must be robust enough to compensate for these elevated risks. For LTB, several FP weaknesses emerged that limited the system’s ability to autonomously protect itself.

**ARB Context:**  
The ARB explicitly stated:  
“On a Class D mission that assumes risk, ensure that the safety net of fault protection can adequately mitigate some of the risks.”

**Contributing Factors:**  
• Incorrect or insufficiently validated FP thresholds.  
• Fault protection logic split across multiple authorities and implementation paths.  
• Sequence‑based safing behaviors and FSW‑based safing behaviors were never tested together end‑to‑end.  
• Missing telemetry limited situational awareness and inhibited on‑orbit diagnosis.  
• Reset behavior and recovery paths were not fully characterized or validated.

**Resulting Impacts:**  
The spacecraft’s ability to safely respond to anomalies was compromised. Fragmented FP design, incomplete testing, and unclear behavior under reset conditions reduced system resilience during off‑nominal events.

**Relevant SWEHB Guidance:**  
Core SWEHB requirements remain applicable even when tailored for Class D:  
• SWE‑057 (Software Architecture) requires the design and documentation of fault management behavior.  
• SWE‑050, SWE‑051, and SWE‑055 require verifiable, traceable FP‑related requirements and logic.  
• SWE‑070 and SWE‑073 require modeling, simulation, and end‑to‑end testing to validate FP behavior under nominal and off‑nominal conditions.

**Lesson Learned:**  
Class D missions rely disproportionately on software fault protection because hardware redundancy is limited. For this reason, FP must be designed, validated, and tested with exceptional rigor. Software fault protection is a mission‑critical system—not an optional enhancement—and must be treated as such from architecture through ATLO and operations.

### **9.** **Lesson Learned (Starliner CFT):** **High‑level requirements invite misinterpretation; safety‑critical behavior must be fully specified and traceable.**

**Project Context:**  
Derived from Starliner CFT Investigation.

**Problem/Observation:**  
Key propulsion/command requirements were high‑level; hazard analyses and safety requirements were not fully decomposed into verifiable software behavior with end‑to‑end traceability.

**Contributing Factors:**

* Ambiguity in expected behaviors (thresholds, timing, reset handling, telemetry fidelity).
* Weak linkage between hazard mitigations and software requirements/tests.

**Impacts:**

* Misinterpretation across teams; gaps persisted into integrated test.
* Incomplete verification evidence for safety‑critical functions.

**Recommended Practices (Aligned to SWE‑050/051/055):**

* Perform **behavioral decomposition**: translate safety requirements into concrete, measurable software requirements (thresholds, timing, state transitions, telemetry).
* Maintain **bidirectional traceability** from hazards → safety requirements → software requirements → test evidence.
* Use **structured requirement reviews** with SA participation and defect tracking.

**Actionable Checks:**

* RTM (Requirements Traceability Matrix) shows full chain from hazards to evidence.
* Safety requirements include quantitative parameters and acceptance criteria.
* Review minutes capture issues and resolutions with SA sign‑off.

### **Additional Relevant Lessons**

### **1. Importance of Cross-Disciplinary Reviews**

* **Lesson:** Requirements development must involve subject matter experts (SMEs) across all disciplines to identify edge cases, constraints, and hidden assumptions. These reviews also help uncover integration challenges and risks early.
* **Key Takeaway:** Incorporate periodic cross-disciplinary reviews to ensure that requirements are complete, feasible, and aligned across system, software, and hardware domains.

### **2. Continuous Maintenance of Requirements**

* **Lesson:** Requirements documents and their traceability matrices must evolve throughout the project lifecycle to reflect changes, traceability adjustments, and lessons learned during development. Stagnant requirements lead to outdated designs and misalignment.
* **Key Takeaway:** Develop a maintenance plan for updating requirements artifacts as the project progresses—addressing changes resulting from testing, user feedback, and evolving mission needs.

### **3. Test-Driven Requirements Validation**

* **Lesson:** Validating requirements through test cases ensures that they are implementable, measurable, and verifiable. Poorly defined requirements lead to gaps in testing, creating risks in system performance and functionality.
* **Key Takeaway:** Align test development with requirements definition to ensure that every requirement is properly validated.

### **4.** **LLSW05 — Deliver Periodic Requirements Snapshots from Authoritative Source**

* **Context/Background: IV&V analyzed deleted requirements due to delta‑only updates and unsynchronized extractions.**
* **Lesson Learned: Provide complete, periodic baselines (not deltas) from the authoritative repository to keep analyses aligned and traceability intact.**
* **Evidence/Observation: Confusion when parent requirements disappeared while traced children remained.**
* **Cause(s): Unclear CM plans; tool extraction difficulties.**
* **Recommendation/Corrective Action: Contract for monthly snapshots; define canonical source; include change logs.**
* **Implementation Guidance: SWE050/052/072 for traceability across levels/tests.**
* **Success Criteria/Verification: No IV&V findings tied to stale/missing requirements; traceability reports pass audits.**
* **Applicability/Scope: All software classes with formal requirements.**
* **Related: SWE050, SWE052, SWE072.**

**5. LLSW12 — Consistent Allocation of CBCS Requirements**

* **Context/Background: Inconsistent CBCS requirement allocation created design/safety issues and contractual resistance.**
* **Lesson Learned: Apply consistent CBCS requirements across all providers to avoid design discrepancies and integration gaps.**
* **Evidence/Observation: Partial applicability led to resistance and unresolved safety concerns.**
* **Cause(s): Uneven contract language; fragmented ownership.**
* **Recommendation/Corrective Action: Centralize CBCS requirements, clarify ownership, enforce uniform flow‑down.**
* **Implementation Guidance: SWE050, SWE052, SWE013.**
* **Success Criteria/Verification: Contracts reflect identical CBCS requirements; traceability shows complete coverage.**
* **Applicability/Scope: Multi‑provider CBCS developments.**
* **Related: SWE050, SWE052, SWE013.**

**6. LLSW13 — Centralize Safety Requirements and Clarify Verification Closeout**

* **Context/Background: Safety requirements scattered across subsystem specs; unclear verification responsibilities/closure at L3.**
* **Lesson Learned: Maintain a single S&MA requirements document with clear verification strategies, roles, and cross‑level closure definitions.**
* **Evidence/Observation: L3 compliance and verification closure not understood; differences for hardware delivery vs integrated configuration.**
* **Cause(s): Distributed ownership; late/immature TVV tools/processes.**
* **Recommendation/Corrective Action: Decompose L2→L3 requirements; define verification terminology/responsibilities early; maintain numbering/titles/types.**
* **Implementation Guidance: SWE050, SWE052/072, SWE018.**
* **Success Criteria/Verification: Auditable verification closure at provider and integrated levels; consistent numbering and traceability reports.**
* **Applicability/Scope: All elements and interfaces.**
* **Related: SWE050, SWE052, SWE072, SWE018.**

**7. LLSW14 — Strengthen Fault Tolerance Requirements *(full content above)***

* **Context/Background: Wording emphasized single‑fault tolerance; permanent crew goals argue for dual‑fault tolerance in many cases.**
* **Lesson Learned: Encourage dual+ fault tolerance for systems supporting crewed missions.**
* **Evidence/Observation: Gateway’s short crewed periods vs Moon Base permanence; ISS practices emphasize dual FT.**
* **Cause(s): Ambiguous FT wording; provider minimal compliance.**
* **Recommendation/Corrective Action: Update safety requirement language; define explicit FT targets and verification.**
* **Implementation Guidance: SWE133/134, SWE050.**
* **Success Criteria/Verification: Documented FT analyses; verification across nominal/off‑nominal.**
* **Applicability/Scope: Safety‑critical software and interfaces.**
* **Related: SWE133, SWE134, SWE050.**

**8. LLSW19 — Security of Interfaces that Are Hazard Controls**

* **Context/Background: DNG lacked attribute to flag when interface requirement/verification implements a hazard control; gaps and IHCRs increased.**
* **Lesson Learned: Add explicit tool attributes/flags to mark interface requirements/verifications that serve as hazard controls; set early.**
* **Evidence/Observation: Reduces IHCRs; clarifies cross‑element dependencies.**
* **Cause(s): Attribute never implemented; ICD/IDD artifacts were outside DNG.**
* **Recommendation/Corrective Action: Implement DNG attribute; set flags prior to hazard Phase****II.**
* **Implementation Guidance: SWE052/072 (traceability), SWE050 (requirements).**
* **Success Criteria/Verification: Interface hazard controls discoverable via reports; fewer transfer requests; clearer verification ownership.**
* **Applicability/Scope: Interface‑heavy systems.**
* **Related: SWE050, SWE052, SWE072.**

**9. LLSW15 — Apply Early Safety Requirements to Interfacing Systems *(full content above)***

* **Context/Background: PPE initially excluded from human‑rating; later interfaces demanded safety compliance, causing costly remedies.**
* **Lesson Learned: Apply safety requirements early to any system that interfaces with crewed systems.**
* **Evidence/Observation: Delays/confusion in HR scope; expensive fixes to improve.**
* **Cause(s): Procurement/requirements processes lacked SMA inputs.**
* **Recommendation/Corrective Action: Engage SMA in procurement; include safety clauses in contracts; classify software appropriately (SWE020/160/133).**
* **Implementation Guidance: SWE020, SWE133/134, SWE013.**
* **Success Criteria/Verification: No late adds of safety requirements; HR scope correct at start; reduced variance requests.**
* **Applicability/Scope: All interfacing systems, crew‑adjacent.**
* **Related Standards/Requirements: SWE020, SWE133, SWE134, SWE013.**

### **Conclusion**

The lessons learned from NASA projects underscore the criticality of systematic, collaborative, and disciplined approaches to software requirements management. Whether through formal documentation, stakeholder engagement, prioritization of COTS/GOTS or MOTS requirements, or addressing hardware dependencies, these best practices offer valuable guidance for building requirements processes that support mission success. By continuously learning and improving from historical challenges, projects can avoid common pitfalls and deliver reliable, high-quality software solutions.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Requirements should be documented and peer reviewed](https://software.gsfc.nasa.gov/lesson-details/53/). **Lesson Number 53**: The recommendation states: "Requirements should be documented and peer reviewed."
* [A single requirements repository should be used on a project](https://software.gsfc.nasa.gov/lesson-details/88/). **Lesson Number 88**: The recommendation states: "A single requirements repository should be used on a project (or closely coordinate when requirements must appear in multiple specs, such as GN&C)."
* [Systems Engineer should revisit requirements every build](https://software.gsfc.nasa.gov/lesson-details/285/). **Lesson Number 285**: The recommendation states: "Software Systems Engineer should work with the customer stakeholder to fully understand the Parent REQ (i.e. the original reason/purpose of REQ) when writing the related Child REQ. This should be captured in the Child REQ Rationale for use by the software developer during implementation.  Refer to GPR 7123.1C: Systems Engineering. Section 4, Key Systems Engineering Functions, addresses this Lesson, particularly Sections 4.1.1, Understanding the Objectives, and 4.1.4, Requirements Identification, where it states, “Rationale should be documented for each requirement. Capturing the reasoning behind requirements is critical to future management of requirement changes.”"
* [Near Space Network (NSN) Cloud transition challenges](https://software.gsfc.nasa.gov/lesson-details/300/). **Lesson Number 300**: The recommendation states: "When considering a transition to Cloud platform/services, keep these in mind: A delivered cloud service capability may not be as robust as needed for operations. Don't take on a Cloud instance if you don't have to; use the Cloud as a giant Network-attached storage and just pay data egress. Hire a Cloud expert even before inheriting the Cloud Concepts. Write requirements for the Cloud up front; everything should have a requirement, no matter if it needs to be built or already works; never let your management agree to accepting an operational component of the ground segment without having agreed upon requirements. A proper communication between the Project leadership and the Ground Segment Manager and PDLs is crucial. Near Space Network (NSN) services have “hidden” fees, so make sure you have a good understanding of all cost implications upfront."

# 7. Software Assurance

**SWE-050 - Software Requirements**

4.1.2 The project manager shall establish, capture, record, approve, and maintain software requirements, including requirements for COTS, GOTS, MOTS, OSS, or reused software components, as part of the technical specification.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that all software requirements are established, captured, and documented as part of the technical specification, including requirements for COTS, GOTS, MOTS, OSS, or reused software components.

## 7.2 Software Assurance Products

Software assurance is integral to ensuring the quality, safety, and reliability of software requirements. Independent SA analysis provides critical oversight for early detection and correction of deficiencies in requirements. The results of these analyses, including actionable feedback, serve as key evidence of SA’s involvement in requirement quality assurance.

#### **Key Outputs:**

* **SA Awareness Evidence:**  
  Evidence of SA’s engagement with software requirements can include:
  + A documented **feedback log** capturing SA observations, comments, and concerns regarding detailed software requirements.
  + **Meeting attendance records** indicating SA participation in requirement discussions, risk reviews, and validation activities.
  + **Requirements specification annotations** reflecting SA concerns or changes recommended for requirement clarity, safety, and completeness.
* **SA Analysis Reports:**  
  Results of SA independent analyses of software requirements. Reports should focus on:
  + Identified deficiencies (e.g., unclear, unverifiable, or unnecessary requirements).
  + Required corrective actions or recommendations to address deficiencies.
  + Confirmation of safety, security, and quality-related requirements.
  + Traceability assessments, ensuring requirements flow down accurately from parent/system-level requirements.
* **COTS/GOTS/MOTS/OSS Component Assurance:**  
  SA must confirm that detailed software requirements address any dependencies on third-party components (e.g., Commercial Off-The-Shelf - COTS, Government Off-The-Shelf - GOTS, etc.) by verifying explicit requirements for compatibility, safety, security, licensing, and integration.

## 7.3 Metrics

Metrics enable project teams to measure requirement quality, traceability, and alignment, providing an objective basis for improvement. Software assurance can leverage the following metrics to monitor and assess the quality of detailed software requirements:

#### **Suggested SA Metrics:**

1. **Total Number of Software Requirements:**  
   Track the number of software requirements at different levels of granularity (e.g., project, subsystem, application-level) to ensure full requirement coverage for the software system.
2. **Number of Software Requirements Without Parent Traceability:**
   * Metric Purpose: Identify "orphaned" requirements that do not trace back to a parent/system-level requirement and address them to maintain consistent requirement flow-down.
   * Example: If there's a requirement for a software function that does not align with the system architecture or operational concept, it must be flagged and reconciled.
3. **Ratio: Detailed Software Requirements vs. Estimated SLOC:**
   * Analyze the ratio of requirements to software lines of code (SLOC). Larger ratios may indicate excessive granularity or over-specification, while smaller ratios may indicate insufficiently detailed requirements.
   * Metric Purpose: Detect inconsistencies between requirement volume and code development scope to avoid gaps or misalignment.
4. **Deficiency Rate:**  
   Track the percentage of requirements flagged by SA as deficient (e.g., unclear, conflicting, unverifiable, or incomplete). Monitor trends during requirement reviews to improve requirement development practices over time.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) for additional metrics.

## 7.4 Guidance for Software Assurance Involvement

This guidance refines the role of Software Assurance (SA) in analyzing, documenting, and maintaining awareness of detailed software requirements and emphasizes techniques, metrics, and best practices to prevent deficient requirements from undermining software projects. It provides actionable insights into how SA can drive requirement quality, traceability, and safety throughout the software lifecycle.

**Deficient requirements are the largest single factor in software and computing system project failure, and deficient requirements have led to a number of software-related aerospace failures and accidents.**

Faults in requirements can originate from the adoption of requirements that are incomplete, unnecessary, contradictory, unclear, unverifiable, untraceable, incorrect, in conflict with system performance requirements, otherwise poorly written, or undocumented. It is important that operators properly identify and document safety requirements, and per industry standards, ensure that safety requirements are internally consistent and valid at the system level for the resulting computing system to work safely throughout its lifecycle.

#### **1. Ensure that Deficient Requirements are addressed early**

Deficient requirements are the single largest causal factor for software project failure. Issues—such as incompleteness, ambiguity, contradiction, or unverifiability—must be identified and corrected early through SA’s independent analysis. Left unresolved, deficient requirements can lead to:

* Software defects during development.
* Compromised system performance.
* Safety-related failures that impact mission success (e.g., aerospace accidents caused by poorly written or missing software requirements).

#### **2. System-Level Validation of Safety Requirements**

Safety-related requirements must:

* Be internally consistent across the software system and hardware interfaces.
* Address all known operational hazards (e.g., hardware transients, spurious signals, and environmental scenarios).
* Be validated to ensure the system operates safely throughout its lifecycle.

#### **3. Independent Software Assurance Software Requirement Analysis:**

Software Assurance entities must perform independent requirement analyses using industry-standard techniques. Key activities should include:

* **Technique Usage**: Apply techniques outlined in Topic [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products), [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis)*,* with tools such as checklists, traceability verification, and completeness assessments.
* **Traceability Verification**: Verify bi-directional traceability between higher- and lower-level requirements, ensuring all functionality has parent requirements and safety requirements cascade correctly.
* **Requirement Quality Assessment**:
  + Check for clarity, correctness, completeness, and consistency.
  + Identify overlapping requirements or avoidable complexity.

#### **4. Requirements for COTS/GOTS/MOTS/OSS Components:**

Software assurance must verify that detailed requirements adequately address:

* **Compatibility** with external software and hardware systems.
* **Safety and security concerns**, including compliance with standards and the mitigation of vulnerabilities.
* **Licensing and support considerations** for OSS components.
* **Modification requirements** for MOTS software, ensuring that changes are captured as defined software requirements.

#### **5. Comprehensive Scope of Software Assurance Software Analysis:**

NASA missions rely on logical decomposition in defining requirements. SA analysis must address all aspects of software requirements, including:

* **Functional and performance requirements:** Verification of mission functionality and desired operational performance.
* **Hardware-dependent requirements:** Validation of software-hardware interactions, addressing compatibility and safety challenges.
* **Interface requirements:** Explicit requirements for interfacing with external systems, hardware, and data sources.
* **Safety and reliability requirements:** Identification and validation of requirements addressing risks, fault tolerance, and dependability.
* **Security requirements:** Validation of measures to address threats such as unauthorized access, data breaches, and cyber vulnerabilities.
* **Operational requirements:** Definition of user interfaces, installation, acceptance, and maintenance processes that align with mission goals.

#### **6. Continuous Requirement Maintenance:**

SA must ensure that requirements evolve and remain valid throughout the software lifecycle. Requirements documentation must reflect changes driven by:

* New stakeholder needs.
* Safety reviews.
* Implementation discoveries during design and development.  
  Proper version control and frequent stakeholder reviews are essential for maintaining requirement relevance.

### **Conclusion:**

Software Assurance plays a pivotal role in detecting and preventing requirement deficiencies. By rigorously analyzing requirements, evaluating traceability, ensuring safety and security alignment, and using metrics to monitor quality, SA minimizes project risks tied to incomplete or faulty requirements. These practices, combined with robust documentation and ongoing engagement with stakeholders, ensure the reliability and mission success of software systems in NASA projects.

Note: Independent SA requirements analysis techniques are detailed in Topic [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products), including [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) on the Detailed Software Requirements.

## 7.5 SA Requirements Analysis Checklists

When evaluating the software requirements, use the list of items in the **[PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist).** [PAT-034](#tabs-5):

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-034 - SA Requirements Analysis Checklist**

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Product Requirements related to Human Rated Software.

Consider if the requirements being analyzed are SMART requirements “specific, measurable, attainable (achievable/actionable/appropriate), realistic, time-bound (timely, traceable)”.

To confirm that the software requirements satisfy the conditions in [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) make sure that the flowed down and derived requirements are from the top-level systems engineering requirements, safety and reliability analyses, and the hardware specifications and design.

Software safety personnel need to be involved in the analysis of software requirements to determine their safety-criticality. Any software requirements that trace are determined to have safety implications. Those requirements with safety implications are tracked as "safety-critical."

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices)        * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.21 - Software Requirements Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641581/5.21+-+Software+Requirements+Analysis+Report+Minimum+Content) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [PAT-013 - Software Requirements Checklist](/spaces/SITE/pages/114328303/PAT-013+-+Software+Requirements+Checklist) * [PAT-034 - SA Requirements Analysis Checklist](/spaces/SITE/pages/154501148/PAT-034+-+SA+Requirements+Analysis+Checklist) |

# 8. Objective Evidence

To demonstrate compliance with **Requirement 7.2:** *Ensure that Software Assurance (SA) performs independent analysis of detailed software requirements, captures their results, and addresses concerns such as safety and quality*, it is critical to provide well-documented, traceable, and objective evidence.

Definition of objective evidence

Objective evidence is an unbiased, documented fact showing that an activity was confirmed or performed by the software assurance/safety person(s). The evidence for confirmation of the activity can take any number of different forms, depending on the activity in the task. Examples are:

* Observations, findings, issues, risks found by the SA/safety person and may be expressed in an audit or checklist record, email, memo or entry into a tracking system (e.g. Risk Log).
* Meeting minutes with attendance lists or SA meeting notes or assessments of the activities and recorded in the project repository.
* Status report, email or memo containing statements that confirmation has been performed with date (a checklist of confirmations could be used to record when each confirmation has been done!).
* Signatures on SA reviewed or witnessed products or activities, or
* Status report, email or memo containing a short summary of information gained by performing the activity. Some examples of using a “short summary” as objective evidence of a confirmation are:
  + To confirm that: “IV&V Program Execution exists”, the summary might be: IV&V Plan is in draft state. It is expected to be complete by (some date).
  + To confirm that: “Traceability between software requirements and hazards with SW contributions exists”, the summary might be x% of the hazards with software contributions are traced to the requirements.
* The specific products listed in the Introduction of 8.16 are also objective evidence as well as the examples listed above.

Below are examples of strong objective evidence for this requirement, aligned with best practices in software assurance and systems engineering.

## 8.1 Objective Evidence for Software Assurance (SA) Products

#### 1. **SA Analysis Reports/Results**

* A documented **SA Requirements Analysis Report** that:
  + Summarizes the findings of the SA review of detailed software requirements.
  + Includes identified issues such as incomplete, vague, or inconsistent requirements.
  + Provides clear recommendations or corrective actions to resolve requirement deficiencies.
  + Evidence of updates to the requirements specification based on SA findings, including acceptance or rejection of SA recommendations.
* **Artifacts:**
  + SA review findings document.
  + Comments matrix linking SA findings to specific requirements.

#### 2. **Traceability Analysis/Verification Results**

* Evidence that SA performed traceability analysis ensuring:
  + All detailed software requirements map to higher-level (system, subsystem, or mission) requirements and stakeholder needs.
  + Bi-directional traceability exists (requirements ↔ test cases ↔ hazards).
  + Traceability gaps flagged in the analysis, with documented resolutions or actions.
* **Artifacts:**
  + Traceability matrix or tool export showing parent-child relationships (e.g., system to software requirement trace).
  + SA validation checklists for traceability.

#### 3. **Software Assurance Participation in Software Requirements Activities**

* Records showing SA’s involvement in requirements development and analysis processes, such as:
  + Agendas, attendance logs, or meeting minutes from requirements walkthroughs, working group discussions, or joint reviews where SA personnel provided input.
  + Evidence of SA comments, questions, concerns, and their resolution from requirement reviews or discussions.
* **Artifacts:**
  + Annotated requirements documents with SA comments/resolutions.
  + Recorded meeting artifacts (e.g., minutes, screenshots from virtual sessions showing SA participation, presentation slides shared by SA).
  + Software Assurance Status presentations

#### 4. **Software Assurance Comments, Annotations, and Feedback**

* Software Assurance-provided comments on the draft and final versions of the software requirements specification (SRS). Examples include:
  + Highlighted sections or annotations identifying unclear or unverifiable requirements.
  + Comment resolution log showing the outcomes of Software Assurance feedback (e.g., accepted, adjusted, or rejected with rationale).
* **Artifacts:**
  + A marked-up copy of the SRS.
  + A collaborative feedback log showing SA contributions and their resolution.

#### 5. **Software Assurance Validation of COTS/GOTS/MOTS/OSS Requirements**

* Documentation of Software Assurance analysis for software components involving COTS, GOTS, MOTS, OSS, or reused software. Ensure that:
  + Detailed requirements for third-party software (e.g., compatibility, licensing, functionality) are adequately addressed and verified.
  + Risks or limitations of using such components are noted in SA assessments.
* **Artifacts:**
  + Component review document detailing constraints and risks (e.g., COTS compliance report).
  + Evaluation reports of third-party software against project-specific requirements.

#### 6. **Safety and Risk-Driven Requirements Review Evidence**

* Software Assurance analysis documents verifying that:
  + Safety-critical requirements are clearly identified and meet industry safety standards.
  + Identified risks related to unclear or inconsistent safety requirements have been raised and addressed.
  + Evidence of Software Assurance’s review of risk analysis results and hazard reports related to requirements.
* **Artifacts:**
  + Safety requirements checklist used by Software Assurance.
  + Review of hazard analyses and fault trees to verify safety requirement completeness.

#### 7. **Requirements Change Management Documentation**

* Evidence of Software Assurance participation in managing requirement changes across the lifecycle, including:
  + Impact assessments of requirement changes on software design, testing, and certification.
  + Verification of updated traceability and safety assurance following changes.
* **Artifacts:**
  + Documented assessments of requirement change requests (CRs).
  + Updated requirements traceability analysis (if significant changes impact the original trace).

## 8.2 Objective Evidence for Metrics (See 7.3)

To support the prescribed metrics and demonstrate their effective use, the following data and documentation can be provided:

1. **Number of Software Requirements by Category**:
   * A report or tool output listing the total software requirements categorized by scope (e.g., project-level, subsystem-level).
   * Spreadsheet or summary showing:
     + Total counts.
     + The breakdown of critical vs. non-critical requirements.
2. **Software Requirements Without Parent Traceability**:
   * SA identification of "orphaned" requirements (requirements without a parent in the traceability hierarchy) and evidence of actions taken to resolve them.
   * Percentage/quantity of traced vs. untraced detailed software requirements.
3. **Detailed Requirements vs. Estimated Source Lines of Code (SLOC)**:
   * Evidence of analysis linking requirements to estimated SLOC, highlighting mismatched ratios or abnormal trends that could indicate over-specification (too many requirements) or under-specification (too few requirements).

**Artifacts:**

* + Metrics reports or dashboards showing:
    - Total count of requirements.
    - Parent-child traceability analysis outputs.
    - Requirements vs. SLOC ratio evaluation.

## 8.3 General Software Assurance Guidance Evidence (See 7.4)

#### **Evidence of Addressing Deficient Requirements**

* Report or spreadsheet documenting requirement deficiencies identified by SA:
  + Incomplete or ambiguous statements flagged.
  + Corrective actions and their implementation status.
* Evidence of requirement rework or updates based on issue resolution.

#### **SA Use of Formal Analysis Techniques**

* Documentation showing the application of techniques from Topic [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products), including [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis):
  + Completeness review checklists.
  + Consistency checks for conflicted requirements (e.g., tools like peer review forms or quality checklists).
  + Safety and security reviews.
* **Artifacts:**
  + Completed SA checklists for requirement analysis.
  + Requirement gap analysis results.

#### **Evidence of Systems-Level Considerations in Software Requirements**

* Traceability evidence that software requirements address system-level considerations, including:
  + Hardware dependencies.
  + External interfaces.
  + Performance, safety, and dependability requirements.
* **Artifacts:**
  + Independent requirements validation results showing alignment between software and system-level requirements.
  + Examples of resolved hardware-software integration issues.

## 8.4 Conclusion

Providing strong, verifiable artifacts as objective evidence for this requirement ensures that Software Assurance activities are effective, traceable, and compliant with processes. The evidence confirms the identification, analysis, correction, and validation of software requirements, ensuring quality, safety, and success across projects and programs.
