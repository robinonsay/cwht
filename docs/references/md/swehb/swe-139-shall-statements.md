# SWE-139 - Shall Statements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695497. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements

SWE-139 - Shall Statements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695497)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695497&showCommentArea=true&showComments=true#addcomment)

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

3.1.11 The project manager shall comply with the requirements in this NPR that are marked with an “X” in Appendix C consistent with their software classification.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-139 History

SWE-139 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 6.3.4 Centers and projects shall fully comply with the "shall" statements in this NPR that are marked with an "X" in Appendix D consistent with their software classification. |
| Difference between A and B | No change |
| B | 2.2.6 The projects shall comply with the requirements in this NPR that are marked with a “project” responsibility and an “X” in Appendix C consistent with their software classification. |
| Difference between B and C | Changed "projects" to "project manager"; Removed the text [a "project" responsibility and]. |
| C | 3.1.11 The project manager shall comply with the requirements in this NPR that are marked with an ”X” in Appendix C consistent with their software classification. |
| Difference between C and D | No change |
| D | 3.1.11 The project manager shall comply with the requirements in this NPR that are marked with an “X” in Appendix C consistent with their software classification. |

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

In this NPR, all mandatory actions (i.e., requirements) are denoted by statements containing the term “shall,” followed by a software engineering (SWE) requirement number.

**NPR7150.2D - NASA Software Engineering Requirements - P.2 APPLICABILITY**

b. This NPR applies to the complete software development life cycle, including software planning, development, testing, maintenance, retirement, operations, management, acquisition, and assurance activities. The requirements of this directive cover such software created, acquired, or maintained by NASA or for NASA to the extent specified or referenced in an appropriate contract, grant, or cooperative agreement. The applicability of these requirements to specific systems and subsystems within the Agency’s investment areas, programs, and projects is through the use of the NASA-wide definition of software classes, defined in Appendix D. Some projects may contain multiple software systems and software subsystems having different software classes. For this directive, software is defined in Appendix A, and includes software executing on processors embedded in programmable logic devices.

g. In this NPR, all mandatory actions (i.e., requirements) are denoted by statements containing the term “shall,” followed by a software engineering (SWE) requirement number. The terms “may” or “can” denote discretionary privilege or permission, “should” denotes a good practice and is recommended but not required, “will” denotes expected outcome, and “are/is” denotes descriptive material.

NPR 7150.2 was written to include the explicit statement in the requirement that full compliance with the requirement is necessary for those entries assigned an "X" in Appendix D.

The purpose of this requirement is to ensure that **project managers** understand and implement the specific software engineering requirements applicable to their project based on its **software classification** as defined in **NASA-STD-8739.8** and outlined in Appendix C of the NPR. This classification-based approach ensures the software processes, deliverables, and risks are scaled appropriately to the complexity, safety-criticality, and mission importance of the software.

By aligning project activities with requirements marked "X" in Appendix C, NASA ensures consistency in applying software engineering practices, minimizes risks, promotes compliance, and enables successful delivery of software systems tailored to programmatic constraints.

This requirement ensures that NASA projects comply with applicable NPR requirements tailored to the project's **software classification**. Aligning project activities with Appendix C allows project managers to scale resources effectively, mitigate risks, ensure NASA mission success, and maintain accountability throughout the software life cycle. By following this guidance, project managers can achieve proportional compliance that is both efficient and mission-focused.

## 2.1 Key Benefits of Compliance

### 2.1.1 Ensures Consistency Across NASA Projects

* Formalizing compliance with the requirements marked "X" in Appendix C aligns project management and software development efforts with NASA-wide standards for **quality**, **safety**, **traceability**, and **governance**.
* These standards ensure that NASA projects use repeatable, verifiable, and auditable processes, regardless of software classification.

#### Example:

A Class A software project (e.g., human-rated flight software) will have more stringent compliance needs than a Class F administrative tool. This requirement ensures each project adheres to appropriate standards consistently and proportionally.

### 2.1.2 Tailors Requirements to Software Risk Profiles

* **Software classification** (Class A through F) is based on the project’s complexity, mission-essential role, risk profile, and safety implications. Requirements marked "X" in Appendix C are tailored to eliminate unnecessary overhead for less critical software while rigorously enforcing controls on high-priority mission or safety-critical software.

#### Example:

Class C or D software might not require full certification or independent validation and verification (IV&V), but Class A software will. Appendix C helps teams identify and prioritize only the relevant activities based on their classification, thus optimizing resources.

### 2.1.3 Promotes Risk Mitigation and Safety

* The classification system prioritizes risk and safety management for software that could directly impact human life, system integrity, or mission success.
* Complying with NPR requirements ensures that safety-critical software receives the necessary attention at every stage of the project, from requirements definition to testing and deployment.

#### Example:

Flight software for spacecraft operations (Class A) must meet every requirement marked "X," including robust testing, safety assurance, and fault tolerance. Class E or F software, however, needs fewer compliance steps.

### 2.1.4 Supports Effective Lifecycle Management

* Complying with NPR requirements helps project managers plan, execute, and oversee software development at every stage of the lifecycle, including:
  + Requirements derivation.
  + Design and development.
  + Validation and verification.
  + Maintenance and retirement.
* Alignment with Appendix C highlights the specific activities required at each lifecycle phase, ensuring no critical processes are skipped, especially for software with long-term operational demands.

#### Example:

Ground control software (Class B) may require robust configuration management and long-term maintenance considerations to support operations over multiple missions.

### 2.1.5 Enables Clear Accountability

* The requirement provides project managers with **clear guidance** on their responsibilities concerning NPR compliance based on software classification.
* By explicitly addressing the requirements marked "X" in Appendix C, project managers can:
  + Track compliance progress.
  + Justify resource allocation decisions.
  + Establish auditable evidence of adherence to best practices.

#### Example:

A Class D scientific analysis tool might only require documentation-focused processes, while Class A human-rated software will require evidence of rigorous testing and independent verification. Appendix C ensures accountability for applying the necessary processes.

### 2.1.6 Saves Time and Resources through Scalability

* Appendix C eliminates guesswork by clearly identifying which NPR requirements apply to each class of software. This approach ensures project teams and contractors focus only on relevant processes, reducing unnecessary effort or expenditure.

#### Example:

A Class F administrative tool might only need basic testing and documentation, while fulfilling unnecessary safety or mission assurance steps could waste time and resources. This requirement prevents over-engineering for proportionally simple software.

## 2.2 Relationship Between Software Classification and Appendix C

### Software Classification System

NASA classifies software into categories (A through F) based on the following criteria:

* **Class A:** Human-rated software (e.g., flight control systems).
* **Class B:** Mission-essential software with significant risk implications (e.g., ground control software).
* **Class C:** Mission support software with limited risk (e.g., simulations or scientific processing software).
* **Class D:** Research and development applications with minimal risk.
* **Class E:** Small-scale or general-purpose software used internally.
* **Class F:** Administrative software or tools unrelated to mission-critical functions.

### Appendix C Simplifies Compliance

* Appendix C explicitly maps NPR requirements to each software classification using an "X" designation for applicable requirements.
* By following this matrix, project managers avoid costly misinterpretations or overlooking critical compliance steps.

## 2.3 Implementation Steps for Project Managers

### 2.3.1 Understand Software Classification

* Determine your software classification based on project characteristics using guidelines.
* Use Appendix C to identify applicable requirements marked "X."

### 2.3.2 Tailor Project Plans

* Incorporate each identified "X" requirement into **project plans**, **SOWs**, and task agreements.
* Ensure requirements are clearly communicated to all contractors and subcontractors.

### 2.3.3 Allocate Resources Based on Classification

* Invest resources in proportion to software classification.
  + High-risk software (Class A) requires significant testing, validation, and safety assurance.
  + Low-risk software (Class F) may need minimal oversight and documentation.

### 2.3.4 Monitor and Track Compliance

* Use Appendix C as a checklist for compliance throughout the lifecycle, ensuring all required activities are completed.
* Maintain auditable evidence demonstrating adherence to relevant NPR requirements.

### 2.3.5 Engage Stakeholders

* Collaborate with software developers, subcontractors, and assurance teams to ensure alignment with NPR requirements for the appropriate classification.
* Ensure robust communication of safety-critical requirements and data rights.

### 2.3.6 Document Deviations or Tailoring

* For any deviations from NPR requirements or tailored activities based on scalability, document the justification, risks addressed, and mitigations planned.

# 3. Guidance

## 3.1 Tailoring

**Tailoring Overview:**  
Tailoring is the process of adjusting, modifying, or seeking relief from prescribed requirements to align with the specific objectives, risks, and constraints of a task, program, or project. Tailoring may involve **additions, subtractions, or changes** to standard implementation practices to ensure effective application to specific software development efforts.

Tailoring is essential to accommodate NASA's vast diversity of software systems, which range from **highly safety-critical flight software** to **low-risk administrative tools**. By appropriately modifying requirements while maintaining effective mitigation for associated risks, tailoring enables projects to operate more efficiently while preserving compliance with NASA's objectives and policies. The **Key Principles of Tailoring** are:

1. **Align Tailoring with Risk and Scope:**  
   Tailoring should reflect the **acceptable risk posture** of the project, technical and programmatic constraints, and the software classification. NASA requires that tailoring decisions focus on minimizing risks while achieving program objectives.
2. **Requirements Governance:**  
   Tailoring decisions must comply with Technical Authority governance, which is detailed in **Appendix C** of NPR 7150.2 [083](#_tabs-<p></p>) . Tailoring is controlled under established NASA governance documents like **NPD 1000.3 [066](#_tabs-<p></p>)** , **NPR 7120.5** [082](#_tabs-<p></p>) , and **NPR 8715.3** [267](#_tabs-<p></p>) , which cover programmatic, cybersecurity, institutional, and health safety considerations.
3. **Consultation and Approval:**  
   At every level of NASA (Centers or Headquarters), tailoring decisions require consultation with appropriate Technical Authorities and alignment with their delegated responsibilities:

   * **Center-Level Tailoring:** Requires consultation with the **Center Engineering Technical Authority**, **Safety and Mission Assurance (SMA) Technical Authority**, and the **Health and Medical Technical Authority (if needed)**.
   * **Headquarters Tailoring:** Requires co-approval by the **Office of the Chief Engineer and the** **Office of Safety and Mission Assurance (OSMA)** for software-related tailoring and the **Office of the Chief Medical Officer (OCHMO)** when health or medical risks are involved.
4. **Human Safety Risk Implications:**  
   For tailoring involving human safety concerns, NASA mandates formal acceptance of risk from the **actual risk takers** or their representatives, along with the relevant supervisory chain.

Tailoring provides an effective way to adjust software requirements while maintaining control over risk and compliance. It ensures scalability for projects of varying sizes and complexities across NASA. Through thorough consultation, documentation, and approval processes, tailoring emphasizes flexibility without compromising governance, safety, or quality standards. By leveraging the Requirements Mapping Matrix, compliance matrix, and Technical Authority oversight, project teams can efficiently manage NPR 7150.2 requirements to align with mission and project needs.

## 3.2 Baseline Set of Requirements

**Purpose:**  
The directive establishes a baseline set of requirements to reduce **software engineering risks** for all NASA projects. These requirements serve as standardized practices to ensure quality, reliability, and safety of software systems corresponding to their **classification** in Appendix C.

**Applying Tailoring:**  
While Appendix C defines default applicability across software classifications, tailoring allows project teams to adjust requirements based on:

* **Technical and Programmatic Risk Posture:** Balancing risk acceptance with technical feasibility.
* **Agency Priorities:** Ensuring compliance aligns with NASA’s mission objectives.
* **Size and Complexity:** Scaling requirements proportionally to smaller or simpler efforts.  
  Tailoring can also be applied collectively to **groups of similar projects, programs, or organizations** per Section 3.5.5 of **NPR 7120.5**.

## 3.3 Requirements Mapping Matrix

### Purpose of the Matrix:

The **Requirements Mapping Matrix** (Appendix C of NPR 7150.2) serves as NASA’s foundation for pre-tailoring requirements based on the **software classification**. It eliminates unnecessary requirements for **less critical software systems** while maintaining comprehensive coverage for **highly critical systems**.

Class-by-class reductions in requirements (e.g., reduced requirements for Class E software) ensure proportional application of processes while preserving compliance for critical systems like **Class A human-rated flight software**.

**Clarifications in the Matrix:**  
The **"X" label** explicitly defines the invoked requirements for each software classification. This label exists to:

* Eliminate potential ambiguity or alternate interpretations of requirements.
* Standardize the understanding of applicable processes across projects.

### Key Rule:

Requirements marked with an "X" in the matrix **must** be fulfilled by the responsible party listed in the **Responsibility column** of the matrix unless formally tailored.

### Tailoring Process

1. **Formal Approval:**  
   Relief from invoked requirements can only be granted by the **designated Technical Authority** for each requirement as specified in Appendix C.
2. **Tailoring Documentation:**

   * **Risk Acceptance:** Tailoring must include documentation of the associated risks and their acceptance by project stakeholders.
   * **Compliance Matrix:** Use the **compliance matrix** as the central tool for tailoring documentation. This ensures:
     + Requirements to be fulfilled are listed.
     + Deviations or waivers are identified along with mitigation plans.
     + Justification for tailoring decisions is clearly described.
   * **Technical Authority Approval:** Tailoring decisions must be reviewed and approved by the applicable Technical Authority to ensure proper management of risks and compliance.
3. **Final Tailoring Decisions:**

   * Capturing the final tailoring status in the compliance matrix consolidates the project’s software requirements plans into a single authoritative document, including:
     + Requirements intended to be met.
     + Approved deviations or waivers.
     + Associated background and rationale.
4. **Broader Tailoring (Program/Portfolio):**  
   Where tailoring broadly impacts **groups of projects or programs**, follow processes outlined in **NPR 7120.5 Section 3.5.5**.

## 3.4 Responsibilities

While NPR 7150.2 typically states, **“The project manager shall...”**, the execution of requirements and responsibilities may be further delegated based on **scope, scale, and complexity** of the system. However, the project manager retains ultimate accountability for ensuring compliance with all invoked requirements in NPR 7150.2 and **NASA-STD-8739.8** [278](#_tabs-<p></p>) .

### Best Practices for Tailoring

1. **Collaborate Early with Technical Authority:**  
   Establish open communication with the designated Technical Authorities to ensure alignment on requirements tailoring and risk mitigation.
2. **Document Tailoring Decisions Thoroughly:**  
   Use the **compliance matrix** to centralize all tailoring actions, including relief justifications, risk mitigation plans, and approvals.
3. **Align Tailoring to Software Classification:**  
   Follow the **pre-tailored guidance** in Appendix C to streamline unnecessary requirements for less critical software systems while preserving rigor for mission-critical or safety-critical systems.
4. **Engage Stakeholders and Risk Owners:**  
   For tailoring decisions involving risk acceptance, ensure appropriate stakeholders (i.e., human safety risk takers, OCHMO, or supervisory chains) formally document their agreement.
5. **Prioritize Scalability:**  
   For smaller or lower complexity efforts, scale application of NPR requirements proportionally to avoid unnecessary overhead.
6. **Mitigate Cybersecurity Concerns:**  
   Tailoring of cybersecurity requirements must adhere to **Section 3.11** of NPR 7150.2 and coordination with the SAISO/designee for approval.

### Additional References

* [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) - for risk mitigation and rationale
* [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) - capture approvals and deviations
* [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) - Ensure fulfillment of invoked requirements per software classification
* [SWE-216 - Internal Software Sharing List](/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List) - Document internal software sharing for transparency

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) * [SWE-216 - Internal Software Sharing List](/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Process Selection](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Process+Selection) |

# 4. Small Projects

Small projects within NASA—such as those developing tools for administrative use, research prototypes, or simple mission support software—have distinct characteristics that make a tailored approach essential for efficient compliance with software engineering requirements. These projects typically involve less complex systems, limited budgets, smaller teams, and reduced risk profiles compared to large-scale or safety-critical efforts.

This guidance outlines how small projects can effectively comply with the NPR 7150.2 requirements, scaled appropriately to their scope and constraints, while maintaining quality and NASA standards.

Small NASA projects can efficiently comply with NPR 7150.2 while avoiding unnecessary overhead by leveraging tailoring processes and documentation simplifications. By scaling requirements based on software classification, prioritizing essential deliverables, and engaging Technical Authorities for approvals, small projects can meet compliance efficiently and align with NASA's goals of quality, reliability, and cost-effectiveness.

## 4.1 Key Principles for Small Projects

### 4.1.1 Scale Requirements to Match Risk and Complexity

Small projects typically involve non-critical systems (e.g., Class E or Class F software) that do not impact mission-critical operations, human safety, or long-term mission goals.

* Focus on **essential compliance activities** rather than exhaustive application of requirements.
* Prioritize simplicity, effectiveness, and resource efficiency in tailoring decisions.

### 4.1.2 Leverage Pre-Tailoring in Appendix C

The **Requirements Mapping Matrix** (Appendix C) already pre-tailors requirements for less critical software systems (e.g., Class E or F).

* For small projects with low-risk software, fewer requirements (marked "X" in the matrix) need to be addressed explicitly.
* Focus your attention on fulfilling only the applicable requirements listed for your software classification.

### 4.1.3 Minimize Documentation Burden

Small projects often have limited staffing and scope, so they should consolidate documentation efforts. Use a **single, centralized compliance matrix** to track tailored requirements, mitigations, and approvals.

### 4.1.4 Focus on Risk Management

While small projects may involve systems with lower complexity, risk management is still critical to avoid cost overruns or schedule delays.

* Tailoring decisions should explicitly define acceptable **technical and programmatic risk** and include appropriate mitigations.
* Ensure all tailoring decision-making is documented to satisfy governance requirements.

## 4.2 Tailoring Processes for Small Projects

### 4.2.1 Identify Applicable Software Classification

Use the NASA software classification system (Classes A through F, as defined in **NASA-STD-8739.8**) to determine your project's classification:

* Most small projects fall into **Class E** or **Class F**, which have limited NPR 7150.2 requirements due to their low-risk nature.
* Once classified, refer to Appendix C to review the requirements applicable to your software classification.

### 4.2.2 Use the Requirements Mapping Matrix for Pre-Tailoring

Appendix C simplifies compliance by pre-tailoring requirements. For small projects:

* Focus only on those requirements marked "X" in the matrix for your software classification.
* Avoid unnecessary processes tied to higher-risk classifications (e.g., Classes A or B).

### 4.2.3 Document Tailoring Actions in a Compliance Matrix

For small projects, ensure tailoring actions are documented in the NPR 7150.2 compliance matrix, including:

* **Requirements to be fulfilled:** Clearly indicate which "X" requirements from Appendix C the project will meet.
* **Approved deviations or waivers:** Document any tailoring requests that seek relief from specific requirements, including:
  + Risk acceptance by the designated Technical Authority.
  + Justification for the deviation (e.g., extra burdens for low-risk software).
  + Mitigation strategies for the associated risks.

Using the compliance matrix consolidates all tailoring decisions, risks, and mitigations, making it easier for small teams to track their software plans in one place.

### 4.2.4 Engage Technical Authority for Review and Approval

Even for small projects, tailoring requires formal review and approval from the designated Technical Authority for each requirement.

* **Center-Level Tailoring:** Consult the Center's Engineering Technical Authority, SMA Technical Authority, Health and Medical Technical Authority, and Center CIO IT Authority, as needed.
* Ensure risk acceptance for tailoring decisions is formally documented and approved.

### 4.2.5 Use Simple Access and Reporting Methods

Small projects can streamline compliance by using simplified tools and reporting mechanisms aligned with their size and scope. Examples include:

* **Centralized Compliance Matrix:** Consolidate tailoring and compliance tracking in a single document (e.g., a lightweight spreadsheet or template).
* **Periodic Reporting:** Limit progress updates to milestone reviews rather than continuous tracking.
* **Electronic Access Systems:** Use low-cost solutions like chat platforms, shared drives, or secure file-sharing systems for access and progress assessment.

### 4.2.6 Focus on Core Deliverables

Small projects should emphasize the following deliverables aligned to their scope:

* **Source Code (Modifiable Format):** Ensure NASA has access to the software source code for review and potential reuse.
* **Minimal Documentation:** Deliver basic configuration files, user manuals, integration testing results, and safety-critical notes only if directly applicable.
* **Risk Mitigation Plans:** Include a brief summary of risks associated with tailored decisions and the acceptance rationale.

## 4.3  Examples of Tailoring for Small Projects

### Scenario 1: Class F Administrative Tool

A small project developing a tool for internal document tracking at NASA:

* **Software Classification:** Class F (low risk, non-critical).
* **Applicable Requirements:** Fulfill only minimal testing, documentation, and configuration requirements marked "X" in Appendix C.
* **Tailoring Action:** Request relief from overly stringent requirements for independent validation and verification (IV&V) given low-risk nature, documenting rationale in the compliance matrix.
* **Oversight Approach:** Engage Center CIO IT Authority to ensure cybersecurity compliance for the tool.

### Scenario 2: Class E Simulation Software

A small project developing simulation software for testing non-safety-critical spacecraft models:

* **Software Classification:** Class E (low risk but mission-supportive).
* **Applicable Requirements:** Focus on source code access, basic testing, and validation activities.
* **Tailoring Action:** Reduce documentation requirements to cover only configurations, testing results, and coding standards alignment.
* **Oversight Approach:** Collaborate with Center Engineering Technical Authority for approval of tailored testing plans.

## 4.4 Best Practices for Small Project Tailoring

1. **Start Small:**  
   Begin tailoring by focusing only on requirements marked "X" in Appendix C. Avoid over-complicating compliance processes.
2. **Coordinate Early:**  
   Collaborate with the Technical Authority early to identify possible tailoring actions and ensure alignment.
3. **Simplify Documentation:**  
   Use centralized tools like a compliance matrix to document all requirements and tailoring rationale, reducing paperwork burden.
4. **Focus on Core Needs:**  
   Emphasize mission-critical processes and deliverables, skipping unnecessary steps tied to higher-risk projects.
5. **Engage Internal Expertise:**  
   Leverage center-based authorities for cybersecurity, technical, and SMA oversight, as applicable to your project scope.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-034)

  [NASA Complex Electronics Handbook for Assurance Professionals,](https://standards.nasa.gov/standard/nasa/nasa-hdbk-873923 "Click to open in new window")

   NASA-HDBK 8739.23A, Approved: 02-02-2016,  Superseding: NASA-HDBK-8739.23
  With Change 1,
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
* (SWEREF-229)

  [NASA Health and Medical Technical Authority (HMTA) Implementation,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=11A "Click to open in new window")

  NPR 7120.11A - Effective Date: September 08, 2020, Expiration Date: September 08, 2025
* (SWEREF-264)

  [NASA Information Technology Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=7A "Click to open in new window")

  NPR 7120.7A, Office of the Chief Information Officer, Effective Date: August 17, 2020,
  Expiration Date: August 17, 2025
  .
* (SWEREF-267)

  [NASA General Safety Program Requirements (Updated w/Change 3)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8715&s=3D "Click to open in new window")

  NASA Procedural Requirements, NPR8715.3D, Effective Date: August 01, 2017, Expiration Date: August 01, 2022
* (SWEREF-269)

  [NASA Research and Technology Program and Project Management Requirements (Updated w/Change 5)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7120_008A_&page_name=main "Click to open in new window")

  NPR 7120.8A, NASA Office of the Chief Engineer, 2018, Effective Date: September 14, 2018, Expiration Date: September 14, 2028
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-283)

  [NPR 7150.2B Appendix C. Requirements Mapping Matrix](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002C_&page_name=AppendixC "Click to open in new window")

  NPR 7150.2C, Effective Date: August 02, 2019, Expiration Date: August 02, 2024
* (SWEREF-286)

  [NASA General Safety Program Requirements,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8715&s=3D "Click to open in new window")

  NPR 8715.3D, Effective Date: December 16, 2021, Expiration Date: December 21, 2026
* (SWEREF-403)

  [Security of Information and Information Systems](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2810&s=1F "Click to open in new window")

  NPR 2810.1F, Office of the Chief Information Officer, Effective Date: January 03, 2022, Expiration Date: January 03, 2027,
* (SWEREF-598)

  [Managing Information Technology](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=2800&s=1E "Click to open in new window")

  NPD 2800.1E, Office of the Chief Information Officer, Effective Date: December 09, 2019, Expiration Date: December 09, 2024,
* (SWEREF-686)

  [Programmable Logic Devices (PLD) Handbook](https://standards.nasa.gov/standard/nasa/nasa-hdbk-4008 "Click to open in new window")

  NASA-HDBK-4008, Revision: Baseline w/CHANGE 1, Document Date: 2013-12-02

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-139 - Shall Statements**

3.1.11 The project manager shall comply with the requirements in this NPR that are marked with an “X” in Appendix C consistent with their software classification.

This requirement ensures full compliance with NPR 7150.2 and the NASA Software Assurance and Software Safety Standard, **NASA-STD-8739.8** [278](#_tabs-<p></p>) , based on the classification of the software. The compliance assessments and audits serve to verify that the project personnel meet all required mandates, either directly invoked by NPR 7150.2 or tailored with documented and approved justification in the **Requirements Mapping Matrix** (RMM).

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess that the project's software requirements, products, procedures, and processes are compliant with the NPR 7150.2 requirements per the software classification and safety criticality for software.

## 7.2 Software Assurance Products

### 7.2.1 Software Compliance Assessment Report

**Purpose**: Provides a comprehensive evaluation of the project’s compliance with NPR 7150.2 and NASA-STD-8739.8, identifying gaps, tailoring approvals, and confirmed actions to ensure software adherence.  
**Contents**:

* Summary of compliance status for each mapped requirement in the RMM.
* Itemized exceptions or tailoring approvals, along with justification.
* Traceability of non-conformances identified during audits (by software classification and lifecycle phase).
* Risk assessment mapping non-conformance to potential impacts on schedule, safety, cost, or quality.

### 7.2.2 Compliance Audit Reports

**Purpose**: Documents the results of software compliance audits for both product and process adherence to the requirements outlined in NPR 7150.2 and NASA-STD-8739.8.  
**Contents**:

* Types of audits (e.g., product audits, process audits, standards audits, safety-related evaluations).
* Findings classified as **non-conformances or observations**, including severity ratings.
* Specific references to unfulfilled requirements or gaps in evidence (e.g., missing documentation, incomplete testing, lack of traceability).
* Recommendations for corrective actions and timelines.

### 7.2.3 Requirements Compliance Checklist

**Purpose**: Tracks the verification of compliance for each requirement based on software classification and Appendix C of NPR 7150.2.  
**Contents**:

* A checklist of invoked requirements for the relevant software classification, marked with:
  + Compliance status: **Compliant / Not Compliant / Tailored**.
  + Objective evidence references and audit tracking number.
* Signatures and approval status for requirements marked as “tailored.”

### 7.2.4 Non-Conformance Tracking Log

**Purpose**: Tracks all software-related non-conformance issues identified during audits and assessments.  
**Contents**:

* A detailed list of non-conformances, including:
  + Affected requirement(s) (per Appendix C).
  + Description of the issue (e.g., incomplete artifacts, software non-compliance, process deviations).
  + Severity (critical, major, minor, observation).
  + Responsible owner for resolution.
  + Tracking status (Open, Resolved, Closed).
* Metrics for tracking trends (e.g., open vs. closed issues over time).

### 7.2.5 Approved Tailoring Matrix

**Purpose**: Documents tailoring of requirements in Appendix C and verifies approval from appropriate technical or project authorities.  
**Contents**:

* + List of tailored requirements with rationales.
  + Approval status and signatures for required tailoring (based on software classification):
    - Class A–E: Center Director or designated Engineering and SMA Technical Authorities.
    - Class F: Center Chief Information Officer (CIO).

## 7.3 Metrics

Tracking metrics helps SA personnel identify trends, monitor compliance, and resolve non-conformances. Metrics for this requirement include:

### 7.3.1 Compliance Tracking Metrics

1. **# of Requirements Met vs. Total Requirements**

   * Tracks project adherence to NPR 7150.2 requirements applicable for the project’s classification.
2. **# of Invoked Requirements Tailored vs. Total Requirements**

   * Tracks tailoring activities to ensure tailoring justification is minimal and appropriately approved.
3. **# of Open vs. Closed Requirements Non-Conformances**

   * Monitors the timely resolution of identified project issues.

### 7.3.2 Audit Metrics

1. **# of Compliance Audits Planned vs. Performed**

   * Tracks if the project’s audit schedule was executed as planned.
2. **# of Non-Conformances Identified in Process vs. Product Audits**

   * Provides insight into high-risk areas or differences between lifecycle phases.
3. **Trends Over Time for Open Non-Conformances**

   * Enables early identification of persistent risks impacting project compliance and deadlines.

### 7.3.3 Software Safety Metrics

1. 1. **# of Safety-Related Requirement Issues (Open vs. Closed)**

      * Tracks compliance with safety-specific NPR 7150.2 sections and NASA-STD-8739.8.
   2. **# of Safety-Related Non-Conformances by Lifecycle Phase**

      * Indicates areas of the lifecycle (e.g., design, implementation) with significant safety risks requiring attention.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

**Key Actions for SA Personnel**:

1. **Verify Requirements Mapping Matrix (RMM):**

   * Confirm the project’s matrix is aligned with NPR 7150.2 Appendix C and addresses the correct software classification.
2. **Audit Compliance with Tailored Requirements:**

   * Focus audits on tailored items to ensure justified exclusions don’t introduce risks.
3. **Regular Audit Activities:**

   * Conduct audits at major lifecycle milestones (e.g., SDR, CDR, TRR).
   * Use checklists to evaluate both process and product compliance.
4. **Non-Conformance Resolution:**

   * Collaborate with the project team to resolve audit findings promptly.
   * Track closure rates and escalate unresolved critical issues.
5. **Coverage of Programmable Logic Devices (PLDs):**

   * Ensure standards for PLDs are followed per:
     + **PLD Handbook (NASA-HDBK-4008)**
6. **Documentation Validation:**

   * Verify compliance-related documents (SMP, SAP, SDP, etc.) reflect accurate tailoring, approval, and implementation of software requirements.

With this improved framework, Software Assurance personnel can evaluate compliance with the requirement effectively, using robust audits, clear metrics, organized evidence, and actionable reporting to ensure project success.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) * [SWE-216 - Internal Software Sharing List](/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List)        * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence provides tangible deliverables and artifacts to support compliance with invoked requirements. These deliverables allow Software Assurance to verify compliance through documented, auditable proof.

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

## 8.1 Requirements Mapping Matrix (RMM):

* Approved RMM signed by the required technical authorities:
  + Center Director or designee.
  + Engineering Technical Authority (ETA).
  + Safety and Mission Assurance (SMA) Technical Authority.
  + Chief Health and Medical Officer (CHMO), if applicable.
* Matrix validation showing correct alignment with software classification and Appendix C.

## 8.2 Audit Results:

* Results of NPR 7150.2 and NASA-STD-8739.8 compliance audits.
* Completed checklists referencing lifecycle compliance, including discrepancies flagged during product and process audits.

## 8.3 Non-Conformance Records:

* Documentation of identified non-conformances during audits:
  + Tracking logs.
  + Root cause analyses (RCA).
  + Resolution records.

## 8.4 Process Documentation and Plans:

* Signed, approved versions of all software plans (e.g., Software Development Plan (SDP), Software Management Plan (SMP), Software Assurance Plan (SAP)).
* Requirements allocation and traceability documentation.

## 8.5 Meeting Logs or Review Records:

* Records from configuration review boards (CRBs) or other project-level reviews reflecting compliance updates, approvals, and tailoring discussions.

## 8.6 Independent Verification and Validation (IV&V) Records:

* Summary reports of IV&V activities, if applicable, tied to specific compliance goals.
