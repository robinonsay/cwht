# SWE-121 - Document Tailored Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695487. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements

SWE-121 - Document Tailored Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695487)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695487&showCommentArea=true&showComments=true#addcomment)

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

3.1.12 Where approved, the project manager shall document and reflect the tailored requirement in the plans or procedures controlling the development, acquisition, and deployment of the affected software.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-121 History

SWE-121 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 6.1.2 Where approved, the requesting Center or project shall document the approved alternate requirement in the procedure controlling the development, acquisition, and/ or deployment of the affected software. |
| Difference between A and B | No change |
| B | 2.2.4 Where approved, the project manager shall document and reflect the tailored requirement in the plans or procedures controlling the development, acquisition, and/or deployment of the affected software |
| Difference between B and C | Changed "and/or" to "and". |
| C | 3.1.12 Where approved, the project manager shall document and reflect the tailored requirement in the plans or procedures controlling the development, acquisition, and deployment of the affected software. |
| Difference between C and D | No change |
| D | 3.1.12 Where approved, the project manager shall document and reflect the tailored requirement in the plans or procedures controlling the development, acquisition, and deployment of the affected software. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

Everyone working on the project has to understand what is required to be done and understand the risk associated with not performing an activity. This action assures the proper implementation of the alternate requirement throughout the various stages of the software life cycle.

This requirement ensures tailoring decisions are formalized and reflected in controlling plans and procedures to strengthen traceability, accountability, and communication throughout the software lifecycle. By documenting tailored requirements in the compliance matrix and integrating them into project plans, NASA ensures tailored processes are properly implemented, risks are mitigated, and governance standards are maintained. This approach promotes sustainability, transparency, and alignment with NASA’s mission-critical objectives.

## 2.1 Purpose of the Requirement:

This requirement ensures that **approved tailoring decisions** are formally documented and embedded in the plans and procedures that govern the development, acquisition, and deployment of software systems. Tailoring involves modifying a prescribed requirement to better align with the specific needs, objectives, constraints, and risk profile of a project. By mandating documentation, NASA ensures that tailored requirements are clearly understood, traceable, and integrated into the project's processes and practices.

This approach minimizes ambiguity, promotes accountability, mitigates risks, and aligns project activities with NASA policies, ensuring tailored requirements are appropriately managed throughout the software lifecycle.

## 2.2 Key Reasons for Documenting Tailored Requirements

### 2.2.1 Accountability and Traceability

* By documenting tailored requirements, project teams can ensure that the deviations from the baseline requirements are **explicitly acknowledged** and agreed upon by all relevant stakeholders (e.g., Technical Authorities, managers, and risk owners).
* Documentation provides a clear record of **what was tailored**, **why tailoring was allowed**, **how risks were mitigated**, and **who approved the tailoring**.

#### Example:

Tailored cybersecurity requirements (Section 3.11 of NPR 7150.2) might involve reduced testing due to limited sensitivity of data. Documenting this ensures that the decision is traceable in case of later security incidents or audits.

### 2.2.2 Alignment with Governance Standards

* NASA Technical Authorities require that tailored requirements be formally approved and documented to enforce consistency with the Agency’s **risk mitigation framework** and governance standards (e.g., NPR 7120.5, NPR 8715.3, NPD 2800.1).
* Proper documentation establishes alignment with organizational policies and prevents unauthorized or informal tailoring that may compromise software safety, security, or functionality.

#### Example:

When tailoring requirements for a Class D scientific tool, the compliance matrix can explicitly specify mitigations for reduced reliability verification due to limited mission-critical importance.

### 2.2.3 Integration into Project Plans and Procedures

* Approved tailoring decisions must be embedded in **plans and procedures** to ensure all project personnel are aware of adjustments, and the tailored requirements are consistently implemented during development, acquisition, and deployment.
* Reflecting tailored requirements in controlling documents ensures:
  + **Clear communication** of tailored processes.
  + **Operational consistency** across teams (development, testing, acquisition, and operations).
  + **Avoidance of misunderstandings** or misapplication of requirements.

#### Example:

If testing requirements for embedded telemetry software are tailored for reduced effort (due to low mission risk), ensuring this adjustment is reflected in testing procedures avoids over- or under-testing during subsequent phases.

### 2.2.4 Supports Risk Assessment and Mitigation

* Documenting and reflecting tailored requirements is critical for **risk assessment**, ensuring that any changes to baseline requirements have been properly evaluated, mitigated, and accepted.
* Risks associated with tailoring (e.g., reduced testing or documentation) are captured in technical plans and tracked throughout the project lifecycle.

#### Example:

For software requiring reduced IV&V due to resource constraints, documenting tailored requirements ensures that alternative risk mitigation strategies (e.g., increased peer reviews or testing rigor) are incorporated into controlling documents.

### 2.2.5 Facilitates Long-Term Visibility

* For projects with **long lifecycles**, documentation ensures future teams or successors (e.g., operations or maintenance personnel) have visibility into tailoring decisions that might impact later phases of the software lifecycle (e.g., post-deployment maintenance or reuse on future missions).
* This promotes sustainable software engineering practices and improves readiness for audits or reviews.

#### Example:

A tailored requirement involving reduced documentation during initial development must be reflected in the project documentation plan, ensuring follow-on teams understand the gaps and rationale when planning upgrades or maintenance.

### 2.2.6 Enables Effective Approval Oversight

* Reflecting tailored requirements in controlling documents ensures compliance with the **requirements approval process**. Technical Authorities need detailed information about:
  + **Why tailoring was needed** (e.g., cost, complexity, risk).
  + **How risks are addressed** (e.g., mitigations and alternative approaches).
  + **Who accepted the risks** (e.g., program manager, Technical Authority, relevant risk-taker).  
    Proper documentation consolidates this information and supports informed approvals.

#### Example:

If the project manager tailors documentation requirements, the Technical Authority can review the compliance matrix to ensure that risk mitigations (e.g., providing supplementary peer reviews) are formalized in the software plans.

## 2.3 Benefits of Proper Documentation

#### **1. Organizational Continuity**

Embedding tailored requirements in controlling documents ensures all personnel working on the project, including contractors and subcontractors, fully understand the modified process. This prevents confusion and ensures consistent workflow across multiple teams.

#### **2. Avoiding Mission Impacts**

Poorly documented tailoring can result in missed critical steps or miscommunication, potentially jeopardizing mission success. Properly reflecting tailoring in the software plan ensures that all modifications are executed without compromising safety or functionality.

#### **3. Meeting Audit and Review Standards**

NASA projects are subject to **internal audits, reviews, and inspections**. Documenting tailored requirements in plans and procedures ensures that projects meet compliance and governance standards and are prepared for external scrutiny.

## 2.4 Implementation Guidance

### 2.4.1 Use the Compliance Matrix for Documentation

* Tailored requirements should be documented in the NPR 7150.2 compliance matrix, which serves as a unified tool for tracking:
  + Approved requirements.
  + Deviations or waivers.
  + Associated risks and mitigations.
  + Sign-offs by the Technical Authority.  
    Using the compliance matrix simplifies documentation and serves as a reference for controlling processes.

### 2.4.2 Reflect Adjustments in Applicable Plans

Document tailoring decisions and any adjustments in controlling project plans, including:

* **Software Development Plan (SDP):** Address changes to lifecycle activities (e.g., testing, reviews, IV&V).
* **Acquisition Plan:** Reflect any tailoring decisions impacting external contracts.
* **Configuration Management Plan:** Track modifications associated with tailored requirements.
* **Testing Procedures:** Adjust testing rigor or scope when tailoring limitations are approved.

### 2.4.3 Communicate Tailored Requirements Across Teams

* Ensure all stakeholders (developers, testers, assurance personnel, etc.) are aware of tailoring decisions by distributing updated plans and procedures.
* Highlight tailored requirements during milestone reviews and readiness assessments.

### 2.4.4 Maintain Audit-Ready Documentation

* Align tailored requirement documentation with NASA's policies on **requirements management and risk acceptance**.
* Include justification, mitigations, and approvals in readiness packages for evaluations, including design reviews, operations assessments, or safety audits.

# 3. Guidance

## 3.1 Recording Tailored Requirements

Properly documenting and managing tailored requirements is critical for ensuring transparency, consistency, and accountability throughout the software lifecycle. When tailoring software development, acquisition, and deployment requirements, the approved changes must be recorded in all relevant program and project documentation. This ensures that the entire project team—including software engineers, assurance personnel, and management—has a clear understanding of the adjustments, associated risks, and required mitigation strategies. The **Key Objectives of Recording Tailored Requirements** are**:**

1. **Ensure Effective Communication**:  
   Recording tailored requirements in the program and project documentation guarantees that all affected personnel are aware of the modifications. This reduces the risk of miscommunication and ensures that tailored requirements are appropriately implemented across development and deployment phases.
2. **Provide Traceability**:  
   Documenting approved tailoring and alternative requirements creates a clear traceable record of deviations from standard requirements. This record supports future audits, process reviews, and evaluations, especially for mission-critical or safety-critical systems.
3. **Support Long-Term Continuity**:  
   Including tailored requirements in a configuration-managed system ensures that future stakeholders, developers, and project managers are informed of the adjustments. This is particularly valuable for projects with extended operations lifespans or for reusing software in other programs.
4. **Enable Risk Mitigation and Acceptance**:  
   Recording tailoring decisions ensures the project team identifies and tracks associated risks, and that these risks are formally reviewed and accepted by the appropriate Technical Authorities (TAs).

Recording tailored requirements ensures traceability, accountability, and compliance with NASA’s software engineering policies and governance. The structured documentation of tailored requirements in a compliance matrix, risk rationale, and project documentation allows effective integration into program plans and ensures consistency throughout the software life cycle. By embedding tailored requirements in a configuration-managed system, NASA projects preserve alignment with technical objectives and provide clarity for stakeholders both now and in the future.

## 3.2 Action Plan for Recording Tailored Requirements

### Step 1: Develop and Maintain a Requirements Compliance Matrix

* A **Requirements Mapping and Compliance Matrix** (see Appendix C) is the primary tool for capturing and documenting compliance and tailoring for all requirements.
* The compliance matrix should:
  1. Track all requirements applicable to the project based on **software classification**.
  2. Clearly indicate which requirements are tailored, deleted, or marked as **Not Applicable (N/A)**.
  3. Include detailed justifications and approvals for any tailored requirements.

### Step 2: Create Tailoring Matrices for Specific Areas

* **Software Assurance and Safety Requirements (NASA-STD-8739.8)**:  
  Projects should develop a **tailoring matrix** to document adjustments to software assurance and safety requirements.
  + Include this tailoring matrix in the **Software Assurance Plan (SAP)**.
  + Update the project schedule to reflect changes in assurance and safety activities.

### Step 3: Incorporate Tailored Requirements into Program and Project Plans

* Tailored requirements should be integrated into controlling documentation to clearly define their implementation. These documents may include:
  + **Software Development Plans (SDP):** Include the tailored requirements and their impact on lifecycle processes.
  + **Testing Plans:** Document tailored adjustments (e.g., reduced testing scope or alternative validation methods).
  + **Acquisition Plans:** Incorporate tailored requirements in contracts and procurement documents.

### Step 4: Configuration Management

* Store tailored requirements in a **configuration-managed system** to ensure traceability and accessibility.
* Configuration management ensures current and future project stakeholders can refer to the correct, approved set of requirements.

## 3.3 Updates to the Compliance Matrix

When tailoring requirements, updates to the compliance matrix must reflect:

* **Baseline Requirements:** The original requirements applicable to the software project, based on NPR 7150.2 and the software classification.
* **Tailored Status:** The status of any requirements marked as tailored, deleted, or not applicable (N/A), along with the rationale for these changes and mitigating actions.
* **Technical Authority Approvals:** Include formal approvals from the appropriate NASA Technical Authorities.

### 3.3.1 Governance Process for Tailoring NPR 7150.2 Requirements

To ensure tailored requirements are effectively managed, all updates to the compliance matrix must follow these steps:

1. Mark all requirements applicable to the project’s software classification (Appendix C).
2. Tailor requirements only where justified by program/project objectives, constraints, and acceptable risks.
3. Ensure the compliance matrix with any tailored, deleted, or N/A requirements is approved by:
   * The Center Engineering Technical Authority (ETA).
   * The Center Safety and Mission Assurance (SMA) Technical Authority.
   * The Chief Health and Medical Officer (CHMO) Technical Authority, if applicable.
4. Seek additional approval from the **NASA Chief Information Officer (CIO)** for any tailored cybersecurity requirements (Section 3.11).
5. Submit compliance matrices involving [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) or [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) requirements to the **Office of the Chief Engineer (OCE)** and the **Office of Safety and Mission Assurance (OSMA)** for review and approval.

## 3.4 Baselined Tailoring

When approved tailoring or adjustments are granted, add the following to the **baselined project/program documentation**:

1. **Rationale for Tailoring Decisions**: Document the justification for tailoring, such as constraints, technical tradeoffs, or programmatic risks.
2. **Approved Adjustments**: Clearly specify any modifications to the initial tailoring request made during the approval process.
3. **Governance Record**: Include evidence of approvals from relevant Technical Authorities (e.g., ETA, SMA, OCE, OSMA).

All tailoring approvals and accompanying justification should be reflected in the project’s configuration-managed documentation for future reference.

## 3.5 Important Considerations for Tailoring Process

### 3.5.1 NASA Governance Policies

* Ensure compliance with NASA governance policies, including:
  + **NPR 7120.5** [082](#_tabs-<p></p>) : Governs program and project management.
  + **NPR 7123.1 [041](#_tabs-<p></p>)** Governs system engineering
  + **NPR 2810.1** [403](#_tabs-<p></p>) : Covers cybersecurity management.
  + **NPD 2800.1 [598](#_tabs-<p></p>)** : Addresses system and technology policy.

### 3.5.2 Tailoring for Software Classification

* Tailoring varies based on **software classification** (A through F) as defined in **NASA-STD-8739.8**.
* Requirements applicable to lower-risk projects (e.g., Class E or F software) are already pre-tailored in Appendix C, streamlining adjustments.

### 3.5.3 Focus on Risk Management

* Every tailoring decision must assess associated risks, implement mitigations, and formally document risk acceptance by the appropriate Technical Authorities.

## 3.6 Key Outputs from the Tailoring Process

For each tailoring request that is approved, the project should produce:

1. **Updated Compliance Matrix**: Reflecting all tailored requirements, justifications, mitigations, and approvals.
2. **Tailoring Records**: Detailed documentation of why tailoring was requested, how risks are mitigated, and who approved the changes.
3. **Revised Project Documentation**: Include tailored requirements in controlling documents such as the Software Assurance Plan (SAP), Software Development Plan (SDP), and Testing Procedures.
4. **Configuration-Managed Records**: A central repository for all tailoring decisions and supporting documentation for present and future reference.

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements)       * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.17 - Software Assurance Plan Minimum Content](/spaces/SWEHBVD/pages/138707548/5.17+-+Software+Assurance+Plan+Minimum+Content) * [5.18 - Safety Plan Minimum Content](/spaces/SWEHBVD/pages/138707600/5.18+-+Safety+Plan+Minimum+Content) * [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics). * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Process Selection](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Process+Selection) |

# 4. Small Projects

Small projects often face unique challenges when attempting to comply with NPR 7150.2, such as limited resources, smaller teams, compressed schedules, and reduced budgets. These constraints can make it impractical for each small project to individually apply for waivers or relief from specific NPR 7150.2 requirements. To address this efficiently, **Centers have the option to request a generic waiver** that applies to multiple small projects. This approach streamlines compliance, reduces administrative burden, and ensures that small projects meet NASA’s safety and quality standards without unnecessary overhead.

Generic waivers provide an efficient mechanism for Centers to support small projects by tailoring NPR 7150.2 requirements consistently and effectively without requiring individual waiver applications. By addressing shared resource constraints, leveraging scalability, and maintaining proper oversight from Technical Authorities, this approach enables small projects to focus on delivering quality software products while meeting NASA’s safety, mission, and technical standards.

## 4.1 Why Generic Waivers are Important for Small Projects

### 4.1.1 Simplified Processes for Limited Resources

Small projects often lack the personnel, time, or funding to conduct a robust review or submission process for individual waivers. A **generic waiver** eliminates the need to conduct repetitive, resource-intensive tailoring requests for multiple similar small-scale efforts while maintaining quality and compliance.

### 4.1.2 Efficiency Across Similar Projects

Many small projects share similar characteristics such as low risk, simpler architectures, or non-mission-critical roles (e.g., administrative tools, prototypes, or experiments). A **generic waiver** covers these commonalities, enabling consistent tailoring across multiple small projects with shared constraints.

### 4.1.3 Standardized Risk Management

A generic waiver allows Centers to predefine **acceptable risks** and align mitigation strategies for small projects in compliance with overarching safety and software engineering policies. This centralized approach prevents inconsistencies and ensures all applicable small projects are treated equitably.

### 4.1.4 Reduces Tailoring Overhead

Individually tailoring requirements or applying for waivers repeatedly can create an unnecessary administrative burden for NASA Centers. By submitting a **Center-level waiver** applicable to multiple small projects, administrative load is reduced and resources can focus on higher-priority mission work.

## 4.2 Key Steps for Centers Requesting a Generic Waiver for Small Projects

### Step 1: Identify the Scope of the Generic Waiver

Clearly define the types of projects that will fall under the scope of the generic waiver. Common characteristics for small projects may include:

* **Software Classification:** Low-criticality classifications (e.g., Class E or F, potentially Class D for low-risk efforts).
* **Common Features:** Examples include ground support software, research tools, simulations, or administrative applications.
* **Constraints:** Small scope, limited resources, short duration, and non-safety-critical applications.

### Step 2: Justify the Waiver

The waiver request should provide a clear justification for why certain NPR 7150.2 requirements are not applicable or require tailoring for small projects, such as:

* **Low risk:** Identify why the risks associated with non-compliance are minimal.
* **Limited impact:** Demonstrate that the waiver will not impact safety, mission success, or system integrity.
* **Consistent needs:** Highlight how similar requirements or reliefs apply across multiple small projects.

### Step 3: Establish Tailored Requirements

Replace waived requirements with simplified or alternative processes that still address core objectives. Tailored alternatives may include:

* **Simplified documentation requirements:** Minimize deliverables to only what is critical (e.g., reduced or consolidated development and assurance documentation).
* **Streamlined testing procedures:** For small projects, scaled-down testing (e.g., targeted unit testing) can replace exhaustive validation steps.
* **Configuration management simplifications:** Adjust configuration control protocols to reflect the smaller system complexity.

### Step 4: Submit Generic Waiver to the Appropriate Technical Authorities

Centers must submit the generic waiver to the relevant Technical Authorities for review and approval:

* **Engineering Technical Authority (ETA):** Ensures tailored requirements meet technical needs.
* **Safety and Mission Assurance (SMA) Technical Authority:** Validates that safety protocols are preserved.
* **Health and Medical Technical Authority (if applicable):** Approves waivers for projects impacting healthcare or human safety.
* **NASA Chief Information Officer (CIO):** Reviews and approves generic waivers that involve Class F software or Section 3.11 cybersecurity requirements.

### Step 5: Apply the Waiver Across Eligible Small Projects

Once the waiver is approved, Centers can apply it consistently to eligible small projects:

* Center-level project managers should maintain adherence to the scope and bounds defined in the waiver.
* Document the use of the generic waiver in each project’s compliance matrix and ensure configuration-managed systems reflect the tailored requirements.

## 4.3 Best Practices for Utilizing Generic Waivers

### 4.3.1. Focus on Scalable Risk Mitigation

A generic waiver should specify how generic risks—if low—are managed without full compliance. For example:

* Substitute exhaustive testing standards (e.g., IV&V) with simpler peer reviews or targeted tests.
* Minimize technical reviews to critical activity checkpoints that align with project milestones.

### 4.3.2. Ensure Consistency

By applying a generic process for tailoring at the Center level, small projects benefit from consistent assumptions around risk posture, tailoring rationale, and implementation. Consistency reduces confusion and provides standard operating procedures for projects with similar profiles.

### 4.3.3. Centralize Waiver Usage Tracking

Maintain records of all small projects that use the approved generic waiver in a **Center-specific software compliance matrix**. This provides traceability for audits and ensures compliance with governance policies.

### 4.3.4. Periodic Review of Generic Waiver Applicability

Centers should periodically assess the applicability of their generic waivers to ensure they remain valid and consistent with evolving NPR 7150.2 updates, mission needs, and lessons learned from prior projects.

### 4.3.5. Train Teams on Generic Waiver Implementation

Center personnel, including project managers and software engineers, should be trained on the conditions and requirements of using a generic waiver. Ensure teams understand any remaining requirements that still need to be fulfilled under the waiver.

## 4.4 When to Use a Generic Waiver for Small Projects

Generic waivers are most effective when used for projects that:

1. Have **low software classification levels** (Class D, E, or F).
2. Are **non-safety-critical** or have minimal mission impact.
3. Share **consistent constraints** such as staffing, budget, and duration limitations.
4. Do not require individual tailoring but share a **common approach** to tailoring specific NPR 7150.2 requirements.
5. Fall under Center-level domains focused on administrative, experimental, proof-of-concept, or internal support software.

## 4.5 Example: Generic Waiver Application

#### Scenario:

A NASA Center regularly manages small software projects to develop internal administrative tools and data analysis software (Class F systems). These tools require only minimal configuration control, testing, and documentation. Applying for individual waivers each time creates an unnecessary administrative burden.

#### Generic Waiver:

The Center requests a **generic waiver** to streamline compliance for Class F administrative software. Under the waiver:

* **Relieved Requirements:** Software plans and documentation are reduced to minimal deliverables (e.g., basic configuration and testing procedures).
* **Tailored Requirements:** Testing standards are scaled down to validate only key functionality. Peer reviews replace rigorous testing protocols.
* **Approval Process:** The waiver is reviewed and approved by the CIO (institutional authority for Class F software) and Center Technical Authorities.
* **Consistency Across Projects:** All similar small administrative tools benefit from using the same streamlined approval and compliance process.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-066)

  [The NASA Organization w/Change 85](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=3E "Click to open in new window")

  NPD 1000.3E, Associate Administrator, April 15, 2015, Expiration Date: April 15, 2026
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-256)

  [NASA Directives and Charters Procedural Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_1400_001H_&page_name=main "Click to open in new window")

  NPR 1400.1H, NASA Office of Internal Controls and Management Systems, Effective Date: March 29, 2019, Expiration Date: March 29, 2024
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-262)

  [NASA Headquarters NASA Office of the Chief Engineer engineering deviations and waivers website.](https://nen.nasa.gov/web/oce/ta "Click to open in new window")

  NASA Headquarters NASA Office of the Chief Engineer engineering deviations and waivers website.
* (SWEREF-263)

  [Delegation of Authority for Granting Relief from OCE Requirements](https://nen.nasa.gov/c/document_library/get_file?uuid=cc0b84fb-f291-4ec7-bd89-0da93eec014a&groupId=13035 "Click to open in new window")

  NASA HQ OCE Letter. August 15, 2012.
* (SWEREF-264)

  [NASA Information Technology Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=7A "Click to open in new window")

  NPR 7120.7A, Office of the Chief Information Officer, Effective Date: August 17, 2020,
  Expiration Date: August 17, 2025
  .
* (SWEREF-269)

  [NASA Research and Technology Program and Project Management Requirements (Updated w/Change 5)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7120_008A_&page_name=main "Click to open in new window")

  NPR 7120.8A, NASA Office of the Chief Engineer, 2018, Effective Date: September 14, 2018, Expiration Date: September 14, 2028
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-403)

  [Security of Information and Information Systems](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2810&s=1F "Click to open in new window")

  NPR 2810.1F, Office of the Chief Information Officer, Effective Date: January 03, 2022, Expiration Date: January 03, 2027,
* (SWEREF-566)

  [The Pitfalls of "Engineering-by-Presentation" (2005)](https://llis.nasa.gov/lesson/1715 "Click to open in new window")

  Public Lessons Learned Entry: 1715.
* (SWEREF-598)

  [Managing Information Technology](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=2800&s=1E "Click to open in new window")

  NPD 2800.1E, Office of the Chief Information Officer, Effective Date: December 09, 2019, Expiration Date: December 09, 2024,

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

A documented lesson from the NASA Lessons Learned database notes the following:

* **The Pitfalls of "Engineering-by-Presentation" (2005). Lesson Number 1715[566](#_tabs-<p></p>)**: Without documenting and, thereby, capturing details of the rationale for decisions affecting systems designs (requirements) "...project staff found themselves repeatedly revisiting the same technical issues. "Now why did we decide..." This is a good indication that why it was done is as important, at times, as what was done. Office of the Chief Engineer (OCE) personnel and future projects or Center personnel will be able to avoid reevaluating this general exclusion or alternate requirement approvals if they have appropriate access to the rationale so they can properly understand the basis on which the exclusions were granted in the first place.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-121 - Document Tailored Requirements**

3.1.12 Where approved, the project manager shall document and reflect the tailored requirement in the plans or procedures controlling the development, acquisition, and deployment of the affected software.

This requirement ensures that any tailored software requirements approved by the appropriate technical authorities are properly documented and accurately reflected in project plans, procedures, and related artifacts. Software Assurance (SA) guidance must ensure tailoring is authorized, traceable, and its impacts understood and communicated across the project lifecycle.

With this structured guidance, Software Assurance personnel can ensure tailored requirements under this requirement are appropriately approved, tracked, reflected, and verified throughout the project lifecycle. Proper oversight ensures alignment with NPR 7150.2[083](#_tabs-<p></p>) and NASA-STD-8739.8 [278](#_tabs-<p></p>)  while mitigating risks introduced by tailoring.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that any requirement tailoring in the Requirements Mapping Matrix has the required approvals.

2. Develop a tailoring matrix of software assurance and software safety requirements.

## 7.2 Software Assurance Products

### 7.2.1 Tailoring Approval Tracking Matrix

**Purpose**: Documents tailored requirements from NPR 7150.2 and NASA-STD-8739.8, along with authorization by technical authorities and their incorporation into project plans and processes.  
**Contents**:

* A tailored requirements summary, with columns for:
  + Requirement reference (e.g., NPR 7150.2 Appendix C, NASA-STD-8739.8 section).
  + Tailoring justification (why the requirement was tailored).
  + Approval authority (Engineering Technical Authority, Software Assurance Technical Authority, CIO for cybersecurity requirements).
  + Status of approval (approved/rejected/pending).
  + Links to project plans, procedures, or work products where tailoring is reflected.
* Risk assessment for tailored requirements (technical, schedule, safety, or cost impacts).

### 7.2.2 Requirements Mapping Matrix (RMM)

**Purpose**: Tracks compliance with both tailored and standard requirements across NPR 7150.2 and NASA-STD-8739.8 for the project’s software classification.  
**Contents**:

* Mapping of all requirements (invoked and tailored) by lifecycle phase.
* Classification alignment with Appendix C from NPR 7150.2.
* Tailoring indicators: standard requirement (default), tailored requirement (with justification and signature).
* Signed approval from appropriate technical authorities.
* Changes or communications updates shared among Software Assurance, Engineering, and the project team.

### 7.2.3 Tailored Software Assurance and Safety Requirements Matrix

**Purpose**: Documents detailed tailoring of NASA-STD-8739.8 requirements specific to software assurance, software safety, and IV&V for the project.  
**Contents**:

* Tailored Software Assurance and Software Safety requirements, organized by section within NASA-STD-8739.8.
* Linkage to project’s Software Assurance Plan (SAP), Software Development Plan (SDP), and IV&V plan.
* Justification and approval status for tailoring.
* Cross-reference to impacted work products and processes (e.g., test plans, schedules, artifacts).

### 7.2.4 Tailoring Impact Assessment Report

**Purpose**: Provides an analysis of the implications of tailored requirements on project activities, deliverables, and risks.  
**Contents**:

* Summary of tailored requirements by lifecycle phase.
* Assessment of tailoring impacts on development products (design, test, configuration management, etc.), schedules, and procedures.
* Potential risks associated with tailoring (e.g., gaps in traceability, safety concerns).
* Recommendations for mitigation of tailoring-related risks.

### 7.2.5 Audit and Compliance Review Report

**Purpose**: Documents audits and reviews conducted to confirm tailored requirements are properly implemented, reflected, and traceable in project plans and deliverables.  
**Contents**:

* Results of audits on project plans and artifacts (e.g., SMP, SAP, SDP, test plans, procedures).
* Verification of tailoring documentation in Requirements Mapping Matrix (RMM) and its reflection in applicable lifecycle phases.
* Non-conformance findings associated with omitted or inconsistently applied tailoring.

## 7.3 Metrics

Tracking metrics allows Software Assurance personnel to monitor tailoring activities, compliance, and impacts across projects. Metrics for this requirement include:

### 7.3.1 Project-Specific Metrics

1. **# of Tailored Requirements Approved vs. Total Requirements Invoked:**

   * Tracks tailoring frequency and ensures regular assessment of justification and authorization.
2. **% of Requirements Tailored Per Project:**

   * Provides insight into tailoring practices project-wide and facilitates alignment with organizational goals.
3. **# of Non-Conformances Related to Tailored Requirements:**

   * Tracks compliance failures attributed to tailoring decisions across lifecycle phases.

### 7.3.2 Organizational Metrics

1. **# of Projects Tailoring Requirements from NPR 7150.2 and NASA-STD-8739.8:**

   * Organizational-level trend analysis on tailoring activities by type of software classification.
2. **Trends of Tailoring Approvals Over Time:**

   * Tracks trends for tailored approvals across projects to identify whether tailoring is increasing, stabilizing, or decreasing.
3. **# of Safety-Related Tailoring Decisions:**

   * Monitors tailoring approvals specific to safety-related requirements and impacts.

### 7.3.3 Audit Metrics

1. 1. **# of Compliance Audits Planned vs. Performed to Verify Tailoring Implementation:**

      * Tracks audit schedules to ensure tailored requirements are assessed regularly.
   2. **# of Non-Conformances Found During Audits of Tailored Requirements:**

      * Tracks issues identified during audits specific to approved tailoring.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

### **7.4.1 Actions for Software Assurance Personnel**:

1. **Verify Tailoring Approvals:**

   * Confirm tailoring approvals are documented in the **Requirements Mapping Matrix (RMM)**, with signatures from appropriate technical authorities:
     + Engineering Technical Authority.
     + Software Assurance Technical Authority.
     + CIO (for tailored cybersecurity requirements in NPR 7150.2 section 3.11).
2. **Analyze Tailoring Impact:**

   * Assess how tailored requirements affect project deliverables, schedules, test plans, and other lifecycle elements.
   * Document any risks associated with tailoring decisions in risk management and tracking systems.
3. **Update Plans and Procedures:**

   * Ensure tailored requirements are reflected in project plans, procedures, and specifications, including:
     + SDP, SAP, IV&V Plan (if applicable), Test Plans, SCMP, Safety Plans, SMA Plans.
   * Verify updates are clear, documented, and traceable.
4. **Audit Tailored Requirements Implementation:**

   * Develop tailored audit checklists to confirm approved tailoring is properly applied in lifecycle activities.
   * Track non-conformances associated with inconsistently applied tailoring decisions.
5. **Develop Tailoring Matrix for NASA-STD-8739.8:**

   * Create a matrix specific to Software Assurance, Software Safety, and IV&V tailoring requirements from **NASA-STD-8739.8** as needed.
   * Include justification, signed approvals, and plans for reflection.
6. **Coordinate Communication of Tailoring Decisions:**

   * Ensure tailoring updates are shared among Engineering, Software Assurance, and the project team.
   * Document all communications for traceability.

See also Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan),

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements)       * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.17 - Software Assurance Plan Minimum Content](/spaces/SWEHBVD/pages/138707548/5.17+-+Software+Assurance+Plan+Minimum+Content) * [5.18 - Safety Plan Minimum Content](/spaces/SWEHBVD/pages/138707600/5.18+-+Safety+Plan+Minimum+Content) * [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics). * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

# 8. Objective Evidence

Objective evidence provides tangible artifacts that verify tailored requirements are approved, communicated, documented, and appropriately reflected in project plans, procedures, and deliverables.

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

## 8.1 Objective Evidence to Be Collected

### 8.1.1 Approved Tailoring Documentation:

* Signed **Requirements Mapping Matrix (RMM)** with tailoring agreement, including justification and technical authority approval (Engineering Technical Authority, Software Assurance Technical Authority, CIO for cybersecurity requirements).
* Tailoring matrices or records specific to requirements in NPR 7150.2 [083](#_tabs-<p></p>) and NASA-STD-8739.8 [278](#_tabs-<p></p>) .

### 8.1.2 Plans and Procedures Reflecting Tailored Requirements:

* Updated versions of project plans, including:
  + [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)
  + [5.17 - Software Assurance Plan Minimum Content](/spaces/SWEHBVD/pages/138707548/5.17+-+Software+Assurance+Plan+Minimum+Content)
  + [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan)
  + [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)
  + [5.18 - Safety Plan Minimum Content](/spaces/SWEHBVD/pages/138707600/5.18+-+Safety+Plan+Minimum+Content)
  + [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content)
* Adjusted procedures, schedules, and documentation reflecting tailored requirements.

### 8.1.3 Non-Conformance Records Related to Tailored Requirements:

* Logs and documentation of non-conformances during audits related to omitted or misaligned tailoring.

### 8.1.4 Communication Records for Tailoring Approvals:

* Meeting minutes and action plans documenting tailoring updates shared with Engineering, Software Assurance, and project teams.

### 8.1.5 Project Artifacts Impacted by Tailoring:

* Test designs, metrics, and configuration artifacts reflecting tailored requirements.
* Specific modifications to deliverables based on tailored requirements.
