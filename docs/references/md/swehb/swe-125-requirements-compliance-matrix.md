# SWE-125 - Requirements Compliance Matrix

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695489. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix

SWE-125 - Requirements Compliance Matrix

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695489)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695489&showCommentArea=true&showComments=true#addcomment)

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

3.1.13 Each project manager with software components shall maintain a requirements mapping matrix or multiple requirements mapping matrices against requirements in this NPR, including those delegated to other parties or accomplished by contract vehicles or Space Act Agreements. 

## 1.1 Notes

A project may have multiple software engineering requirements mapping matrices if needed for multiple software components on a given project.

Project relief from an applicable “X” requirement can be granted only by the designated TAs, Engineering, and SMA, or, for security issues, the NASA CIO. The record of their approval of the tailored requirements in a Requirements Mapping Matrix will be indicated by the Authority signature or signatures in the Requirements Mapping Matrix. The projects will document their related mitigations and risk acceptance in the approved Requirements Mapping Matrix. When the requirement and software class are marked with an “X,” the projects record the risk and rationale for any requirements that are entirely or partially relieved in the Requirements Mapping Matrix. The CIO has institutional authority on all Class F software projects.

## 1.2 History

Click here to view the history of this requirement: SWE-125 History

SWE-125 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 6.3.2 Each project with software components shall maintain a compliance matrix against requirements in this NPR, including those delegated to other parties or accomplished by contract vehicles. |
| Difference between A and B | No change |
| B | 2.2.5 Each project manager with software components shall maintain a compliance matrix or multiple compliance matrices against requirements in this NPR, including those delegated to other parties or accomplished by contract vehicles or Space Act Agreements. |
| Difference between B and C | Changed "compliance" to "requirements mapping";  otherwise, no change. |
| C | 3.1.13 Each project manager with software components shall maintain a requirements mapping matrix or multiple requirements mapping matrices against requirements in this NPR, including those delegated to other parties or accomplished by contract vehicles or Space Act Agreements. |
| Difference between C and D | No change |
| D | 3.1.13 Each project manager with software components shall maintain a requirements mapping matrix or multiple requirements mapping matrices against requirements in this NPR, including those delegated to other parties or accomplished by contract vehicles or Space Act Agreements. |

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

Compliance is commonly defined as the demonstration of adherence to the standard or the requirement applied to the project. The development and maintenance of a compliance matrix provide a management control tool for mutual understanding and agreement about the project software requirements. A properly maintained compliance matrix is an indicator of the state and progress of the project. Periodic reviews of achieved project compliance against that planned in the compliance matrix can help identify any needed deviations or waivers against the requirements of the NPR. The compliance matrix can also be a useful tool during an evaluation of project risk.

The requirement to maintain a **Requirements Mapping Matrix (RMM)** ensures that project managers actively document and track software compliance with NPR 7150.2 [083](#_tabs-<p></p>) requirements. This practice establishes **transparency**, **traceability**, and **accountability** for compliance with prescribed requirements, whether they are directly implemented, tailored, or delegated to external parties under contract or Space Act Agreements.

By maintaining an RMM, projects ensure that all applicable requirements are met or tailored (if approved by the appropriate Technical Authorities), including mitigation strategies and documented risk acceptance. This systematic approach safeguards NASA’s standards in software engineering, particularly in ensuring safety, mission success, and risk control.

The requirement to maintain a Requirements Mapping Matrix ensures that software development aligns with NASA’s policies and applicable standards. By requiring detailed documentation of each requirement's fulfillment, tailoring, or delegation, the RMM supports traceability, transparency, and accountability. This practice minimizes risks, fosters stakeholder accountability, and strengthens lifecycle oversight for all software projects, regardless of complexity or scope.

### **2.1 Key Reasons for Maintaining a Requirements Mapping Matrix**

### 2.1.1 Ensures Traceability of Requirements Throughout the Software Lifecycle

* The Requirements Mapping Matrix (RMM) acts as a **central reference** linking NPR 7150.2 requirements to how (and whether) they are fulfilled for each software component or system.
* By maintaining the RMM, project teams can track and document how requirements are satisfied, tailored, or delegated, enabling clear identification of:
  + Requirements fulfilled in-house.
  + Requirements accomplished through external contracts or agreements.
  + Requirements approved for relief, along with associated mitigations and risks.
* This traceability supports reviews, audits, and compliance evaluations throughout the software lifecycle, from development to deployment and maintenance.

#### Example:

For a flight system with both onboard control software and ground control software:

* An RMM provides clarity on which team or contractor is responsible for adhering to safety-critical requirements relevant to the onboard system and which Class D requirements apply solely to the ground system.

### 2.1.2 Facilitates Delegation Management and Accountability

Many NASA projects include software elements that are developed or managed by external entities, such as:

* **Contract vehicles (e.g., contractors or vendors).**
* **Space Act Agreements (e.g., partnerships with private organizations).**

The RMM ensures that **delegated requirements** are clearly documented and communicated:

* It identifies which party is responsible for fulfilling specific requirements.
* It provides clear expectations for contractors and partners to ensure consistent compliance with NASA’s policies.
* Centralized documentation in the RMM reduces ambiguity about shared responsibilities across organizational boundaries.

#### Example:

When developing Class C mission software, an RMM can ensure that a contractor's deliverables address applicable requirements, such as reliability testing and adherence to NASA coding standards.

### 2.1.3 Supports Tailoring Decision Documentation and Risk Mitigation

When a requirement is tailored (e.g., relieved, partially fulfilled, or modified), the RMM serves as **official documentation** for:

* The rationale for tailoring.
* The associated risks of tailoring the requirement.
* Mitigation strategies to reduce or manage those risks.
* The formal approval from the designated Technical Authorities (Engineering Technical Authority, Safety and Mission Assurance Technical Authority, or NASA CIO for cybersecurity-related requirements).

This record enables informed decision-making and provides transparency for both internal and external stakeholders. It also ensures that the **risk acceptance process** is thorough and well-documented.

#### Example:

A project may tailor a software testing requirement for a low-risk Class E administrative application. The RMM would document:

* The rationale for tailoring (e.g., resource constraints for extended testing).
* The mitigation strategy (e.g., additional peer reviews).
* Approval from the appropriate Technical Authorities.

### 2.1.4 Promotes Informed Risk Acceptance

The RMM requires that for every tailored or relieved requirement, the project:

* Specifies the associated risks.
* Records accepted risks and approval by Technical Authorities.

By enforcing detailed documentation, the RMM ensures:

* Risk awareness at all levels (from project management to governance authorities).
* Consensus on acceptable risks and the justification for tailoring decisions.

#### Example:

For a robotic mission component classified as Class C, the decision to reduce specific software validation steps must include:

* Detailed rationale (e.g., constrained project schedule).
* Risk acceptance backed by the Engineering and SMA TAs.
* An outline of risk mitigations (e.g., targeted testing for mission-critical features).

### 2.1.5 Supports Class-Specific Governance

Different classes of software (outlined in Appendix C of NPR 7150.2) have different requirements, depending on their criticality, complexity, or impact on mission success and safety. The RMM provides a mechanism to:

* Record class-specific requirements marked as "X" in the matrix.
* Justify and document tailoring decisions for specific software classes.
* Ensure that institutional authority, such as the Chief Information Officer (CIO) for Class F software, is consulted when applicable.

#### Example:

For Class F software (non-mission-critical tools), the RMM allows projects to record that the NASA CIO has approved the tailored requirements for cybersecurity-related provisions.

### 2.1.6 Ensures Adaptability for Complex Projects

Large or complex projects with **multiple software components** may use multiple RMMs, one for each system, subsystem, or software element. This ensures that:

* Each component’s compliance is individually tracked and documented.
* Tailoring or delegation at the component level is properly documented and governed.
* Systems engineers and managers maintain clear oversight of compliance across the integrated system.

#### Example:

For a satellite mission involving multiple payloads, each with its own software element, individual RMMs might be maintained for:

* The main spacecraft control software (Class B).
* Payload sensor software (Class C).
* Ground support tools for simulation and analysis (Class F).

## 2.2 Requirements Mapping Matrix and Authority Approvals

### 2.2.1 Designated Technical Authorities’ Role in Requirement Relief

* Relief from an “X” requirement applies only with **formal, documented approval** from the designated Technical Authorities.

  + **Engineering Technical Authority (ETA)**: Approves technical and performance-related tailoring.
  + **Safety and Mission Assurance (SMA) Technical Authority**: Approves tailoring for safety-critical requirements.
  + **NASA Chief Information Officer (CIO)**: Approves tailoring for Class F software.
* The TA’s approval is **recorded in the RMM** via signatures or electronic equivalent.

### 2.2.2 Documentation of Mitigations and Risk Acceptance

For requirements marked as relieved or tailored, the RMM must:

* Specify the associated risk.
* Document mitigations that reduce the potential impact.
* Record formal risk acceptance by the project.

This ensures that responsibility for tailoring decisions and associated mitigations is explicitly assigned and approved.

## 2.3 Benefits of Maintaining a Requirements Mapping Matrix

1. **Improves Compliance Oversight**: Centralized documentation ensures full visibility into requirement fulfillment and tailoring decisions.
2. **Ensures Consistent Governance**: Tracks Technical Authority involvement and assures compliance with NASA’s policies.
3. **Supports Future Audits and Reviews**: Provides a historical record of decisions, approvals, and mitigations for audits, post-launch reviews, or subsequent project reuse.
4. **Facilitates Transparent Delegation**: Documents how responsibilities are distributed across internal and external stakeholders.
5. **Enhances Risk Management**: Ensures risks associated with tailoring are systematically identified, mitigated, and accepted.

# 3. Guidance

The compliance matrix is a critical tool for tracking, managing, and demonstrating adherence to the NPR 7150.2 **NASA Software Engineering Requirements** throughout the software lifecycle. It provides a structured format for documenting applicable requirements, tailoring, waivers, deviations, planned compliance approaches, and evidence of compliance. By maintaining a compliance matrix, projects ensure traceability, accountability, and transparency, while enabling effective communication between the development team, contractors, and Technical Authorities (TAs).

This improved guidance expands on the original content by clarifying processes, aligning with best practices, and emphasizing the importance of tailoring and tracking compliance in different circumstances.

The compliance matrix is vital for ensuring adherence to NPR 7150.2 requirements, documenting tailoring decisions, and verifying compliance throughout the software lifecycle. By serving as both a checklist and a centralized repository of compliance information, the matrix enables teams to maintain accountability, manage risks effectively, and align with NASA’s governance framework. Expanding its role to include contractor deliverables, detailed tailoring records, and ongoing lifecycle updates transforms the compliance matrix into a dynamic tool that supports mission success and quality assurance across complex and evolving projects

## 3.1 The Role of the Compliance Matrix

### 3.1.1 Purpose and Use

A compliance matrix serves as a **centralized tracking mechanism** for meeting NPR 7150.2 requirements. It facilitates the consistent application of requirements and captures decisions related to tailoring, waivers, deviations, and delegation of responsibilities.

Key elements of the matrix include:

1. **Requirements Coverage**: Listing all requirements from NPR 7150.2 that apply to a project’s software based on its classification and safety criticality.
2. **Planned Compliance**: Documenting the approach or actions by the project team or contractors to meet each requirement.
3. **Tailoring Decisions**: Recording approvals for tailored, waived, or deviated requirements, including rationale and risk mitigations for changes.
4. **Compliance Evidence**: Tracking supporting documentation showing how requirements have been met, reviewed, or assessed.

### 3.1.2 Multiple Software Classes

Projects may have multiple software classes (e.g., Class B for the flight system and Class E for supporting ground tools). A single compliance matrix may include entries specific to those classes, or separate matrices may be created for distinct components as needed. Regardless of the approach, the matrix ensures that all necessary requirements are addressed per classification.

## 3.2 Developing the Compliance Matrix

### 3.2.1 Initial Development

The compliance matrix is first created during the project planning phase and incorporated into the **Software Development Plan (SDP)** or **Software Management Plan (SMP)**. The steps for initial development include:

1. Determining the **software classification and safety criticality** for each software component in the project (refer to SWE-020 - Software Classification).
2. Populating the compliance matrix using the requirements mapping matrix provided in **Appendix C** of NPR 7150.2 or an approved Center-level procedural mapping of NPR 7150.2.
3. Including the compliance matrix template, which is available to NASA users via the NASA Engineering Network (NEN) website.

### 3.2.2 Key Sections in a Compliance Matrix:

* **Requirement Statement**: Clearly defined, traceable requirement.
* **Applicability**: Indication of whether the requirement applies to specific software components.
* **Compliance Method**: A description of how the requirement will be met or tailored, including alternative solutions or strategies.
* **Risk and Rationale**: If tailored or waived, a record of associated risks and rationale for relief.
* **Applicable Document References**: Specific project documents (e.g., SDP, testing plans) where compliance is demonstrated.

## 3.3 Requesting Relief: Tailoring, Waivers, and Deviations

### 3.3.1 Requesting Relief

For requirements deemed inapplicable or needing relief (partial or complete), the compliance matrix itself serves as the streamlined mechanism for documenting tailoring, waivers, and deviations. The TA approvals are recorded in the matrix, making it a consolidated record for tracking compliance adjustments.

### 3.3.2 Approval Process

1. **Center-Level Authority**:

   * Tailoring or waivers for requirements governed by Center authorities (as listed in NPR 7150.2, Appendix C) can be handled at the Center level.
   * Justifications for relief are documented in the compliance matrix and submitted to the Center Engineering Technical Authority (ETA) and Safety and Mission Assurance (SMA) TA.
2. **Headquarters-Level Authority**:

   * Requirements governed by Headquarters authorities (e.g., the Office of the Chief Engineer (OCE) and the Office of Safety and Mission Assurance (OSMA)) must go through coordination at HQ for review and approval.
3. **Key Approvals**:

   * Every tailored, waived, or deviated requirement must have a signature (or electronic equivalent) from the designated ETA, SMA TA, and associated HQ offices, depending on authority ownership.

## 3.4 Role of Technical Authorities (TAs)

### 3.4.1 Responsibilities of TAs

The TAs (Engineering, SMA, OCE/OSMA at Headquarters) review compliance matrices to verify the following:

1. **Adequacy of Justifications**: The rationale provided for tailoring or relief must reflect acceptable risk and proper mitigation strategies.
2. **Coverage of Requirements**: Ensure that all requirements marked "Not Applicable (N/A)" have sufficient justification and, where needed, alternative paths for compliance.
3. **Evidence of Compliance**: Confirm that detailed references and supporting documents are included for each requirement checked off as completed.
4. **Risk Assessment and Mitigation**: Approve the risk acceptance process for changes or omitted requirements.

### 3.4.2 Delegation and Oversight

* When requirements are delegated to contractors or external entities through contract vehicles or Space Act Agreements, TAs ensure the compliance matrix reflects accountability for these entities.
* TAs regularly audit compliance matrices to maintain consistency between project teams, contractors, and NASA standards.

## 3.5 Contractor Involvement in Compliance Matrix

Contracts and agreements involving external development organizations must include the relevant requirements that are consistent with the project's compliance matrix. To ensure proper integration:

1. **Expand Compliance Matrix Entries**: Add fields to the matrix for contractor-specific details, such as:
   * The roles of contractors and subcontractors.
   * Approved tailoring or waiver rationale relevant to their deliverables.
2. **Data Sharing**: Use a secure, centralized repository (e.g., web-based platform or server database) to store compliance matrix updates so contractors, NASA personnel, and relevant stakeholders have consistent access.
3. **Coordination**: Ensure contractors are aligned with NASA TAs and obtain approval for any tailoring affecting their components or deliverables.

## 3.6 Using the Compliance Matrix as a Lifecycle Tracking Tool

### 3.6.1 Lifecycle Integration

The compliance matrix evolves throughout the project lifecycle as a dynamic tracking tool. It serves as a checklist to identify completed requirements, monitor progress, and highlight compliance gaps or tailored items. Key updates include:

1. **Evidence of Compliance**: Teams update the matrix with links or references to documentation verifying requirement fulfillment (e.g., test reports, peer review records).
2. **Revised Requirements**: Incorporate changes resulting from new tailoring requests, deviations, or waivers approved during later phases of the project.
3. **Risk Mitigation Tracking**: Document mitigation strategies and update progress on completed risk management actions.

### **3.6.2 Audits and Reviews**

TAs, project managers, or independent reviewers use the compliance matrix as an auditing tool to evaluate compliance status across key milestones in the project lifecycle (e.g., Preliminary Design Review (PDR), Critical Design Review (CDR), testing phases).

## 3.7 Compliance Matrix Quality Standards

### 3.7.1 Best Practices for Well-Formed Entries

1. **Requirement Statement**: Use clear and exact language from NPR 7150.2 to avoid ambiguity.
2. **Document Reference**: Specify project documents (e.g., SDP section number) as evidence of compliance.
3. **Tailoring Justification**: Provide adequate rationale for tailored or relieved requirements, including risk and mitigation details.
4. **Approval Signatures**: Ensure all approvals are properly recorded, including relevant TA signatures.
5. **Centralized Storage**: Save entries, evidence, and updates in a common, searchable system accessible to the entire team.

See also [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements), [SWE-152 - Review Requirements Mapping Matrices](/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices) , [SWE-212 - NASA-STD-8739 Mapping Matrices](/spaces/SWEHBVD/pages/102695331/SWE-212+-+NASA-STD-8739+Mapping+Matrices),

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) * [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements) * [SWE-152 - Review Requirements Mapping Matrices](/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices) * [SWE-212 - NASA-STD-8739 Mapping Matrices](/spaces/SWEHBVD/pages/102695331/SWE-212+-+NASA-STD-8739+Mapping+Matrices)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics). * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [PAT-028 - NPR 7150.2D Compliance Matrix](/spaces/SITE/pages/119242755/PAT-028+-+NPR+7150.2D+Compliance+Matrix) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). e

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Process Selection](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Process+Selection) |

# 4. Small Projects

Small projects often face constraints in personnel, funding, and time that limit their ability to fully implement all NPR 7150.2 requirements in an exhaustive manner. While all requirements must be listed in the compliance matrix to ensure proper documentation and traceability, projects have the flexibility to identify **critical entries** and prioritize efforts based on risk, complexity, and impact. This guidance helps small projects balance compliance with available resources by focusing on essential requirements and identifying candidates for waivers or deviations during the development of the compliance matrix.

For small projects where personnel or funding constraints limit activities, the ability to proactively identify critical requirements and waiver/deviation candidates within the compliance matrix allows for efficient risk-balancing and streamlined efforts. By focusing on essential activities, documenting tailoring decisions clearly, and coordinating approvals with Technical Authorities, small projects can meet NASA’s software engineering standards while optimizing resources and maintaining mission and safety priorities.

## **4.1 Flexibility for Small Projects**

### 4.1.1 Balancing Compliance with Constraints

Small projects, especially those classified as low-risk (e.g., Class E or F software), typically have less stringent requirements compared to higher-class mission-critical software. Identifying critical entries upfront allows project teams to focus their limited resources on requirements that pose the most significant risks or have the greatest impact on safety, mission success, or cybersecurity.

#### **Key Objectives:**

* **Risk-Based Prioritization:** Focus on areas with the highest risk to minimize potential issues during development and deployment.
* **Resource Optimization:** Ensure compliance in crucial areas without overloading teams with documentation or activities that may be less critical.
* **Streamlined Approval Process:** Identify waiver or deviation opportunities early to simplify review and approval by Technical Authorities (TAs).

### 4.1.2. Critical Entries in the Compliance Matrix

All requirements listed in NPR 7150.2 must be included in the compliance matrix. However, small projects can categorize these requirements for efficient management:

* **Critical Requirements:**  
  Select requirements essential to **safety**, **mission success**, **cybersecurity**, or the fundamental functionality of the software. Critical entries require full compliance with supporting evidence, even for resource-constrained projects.
* **Tailoring/Relief Candidates:**  
  Identify non-critical requirements that may be tailored, omitted, or modified without introducing significant risk to the project. These entries can be flagged for waiver or deviation requests.

#### Examples:

* **Critical Requirements:**
  + Safety assurance (e.g., NPR 7150.2, Section 3.10) for software supporting human spaceflight.
  + Cybersecurity compliance (e.g., Section 3.11) for Class F software if sensitive data is processed.
* **Tailoring/Relief Candidates:**
  + Documentation requirements for low-risk Class F administrative tools where reduced deliverables are justified.
  + Comprehensive performance testing for exploratory or prototype software.

### 4.1.3 Proactive Identification of Waiver/Deviation Candidates

During the development of the compliance matrix, small projects should analyze requirements to proactively identify candidates for waivers or deviations with adequate justification, balancing risks with available resources.

#### Steps for Identifying Waiver/Deviation Candidates:

1. **Assess Applicability:** Determine whether a requirement fully applies to the small project based on its classification and criticality (SWE-020).
2. **Evaluate Risks:** Conduct a risk evaluation for partially tailored or relieved requirements to ensure mitigations are in place and risks are acceptable.
3. **Document Rationale:** Record the rationale for proposing relief, including how constraints such as personnel or funding affect compliance.
4. **Seek Authority Approval:** Obtain signatures from designated TAs (Engineering TA and SMA TA.

#### Example:

For a small Class E software tool supporting ground operations:

* The compliance matrix may request relief from exhaustive code documentation in favor of simplified functional descriptions.
* Rationale: The tool is temporary, non-safety-critical, and used internally within a limited timeframe.

### 4.1.4 Risk Balancing Through the Compliance Matrix

#### **Streamlined Documentation Process**

Small projects can use the compliance matrix not only to track requirements but also to demonstrate risk mitigation strategies and resource-aware compliance. By documenting tailored requirements and relaxed activities in the matrix:

* Risk is explicitly acknowledged and mitigated upfront.
* Relief approvals are centralized, simplifying communication and traceability.
* Compliance efforts are balanced with available personnel and funding.

#### **Focus on High-Impact Activities**

Allocate project resources where risks are highest, such as:

* Safety-critical requirements (e.g., Section 3.2: Software Safety and Assurance).
* Security-critical requirements (e.g., Section 3.11: Software Cybersecurity).
* Testing or validation for mission-critical or operationally significant components.

For less critical areas (e.g., documentation or performance tuning for exploratory software), acceptable risks may justify deviations or waivers.

### 4.1.5 Technical Authority Coordination

TAs play a pivotal role in approving tailored requirements for small projects:

1. **Engineering Technical Authority (ETA):** Reviews technical aspects of compliance and tailoring.
2. **Safety and Mission Assurance Technical Authority (SMA TA):** Approves relief for safety-critical requirements.
3. **NASA Chief Information Officer (CIO):** Reviews cybersecurity-related relief or tailoring for Class F software.

Small projects should streamline communication with TAs by grouping waiver requests directly within the compliance matrix, enabling faster approvals and better alignment with governance policies.

### 4.1.6 Implementation Mechanics

#### **Step-by-Step Guidance for Small Projects:**

1. **Draft the Compliance Matrix:** List all NPR 7150.2 requirements based on Appendix C and software classification from SWE-020.
2. **Categorize Requirements:**
   * Critical entries requiring full compliance.
   * Non-critical entries flagged for relief requests.
3. **Risk Assessment:** Evaluate the impact of tailoring candidates on safety, mission success, and functionality.
4. **Document Rationale:** For flagged entries, provide justification for proposed tailoring or waivers, including personnel or funding limitations and risk mitigations.
5. **Obtain TA Approvals:** Submit the compliance matrix to the appropriate TAs (ETA, SMA TA) for signatures.
6. **Monitor Updates:** Track compliance matrix revisions throughout the project lifecycle (PDR, CDR, and operational phases).

### 4.1.7 Best Practices for Compliance Matrix Development

#### **Efficient Use of Resources**

1. **Leverage Center-Level Compliance Templates:** Use templates provided on the NASA Engineering Network (NEN) to streamline development and ensure consistency.
2. **Centralize Documentation Storage:** Store compliance matrix updates in a server-based or centralized platform accessible to the project team and TAs.
3. **Focus on Priorities:** Dedicate resources to requirements with higher risk impact, while streamlining documentation or activities for less critical entries.

#### **Transparency and Communication**

* Ensure compliance matrix entries provide **sufficient detail** for auditors or stakeholders to locate evidence demonstrating compliance.
* Establish clear communication pathways with contractors and external partners to streamline validation efforts for delegated requirements

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

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
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-284)

  [NPR 7150.2D Compliance Matrices by Class Templates. SWEHB Topic 7.16](https://swehb.nasa.gov/display/SWEHBVD/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix "Click to open in new window")

  This topic contains spreadsheets for each class of software.
   For older versions of SWEHB, see SWE-125 and Topic 7.16 in the appropriate version.

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

**SWE-125 - Requirements Compliance Matrix**

3.1.13 Each project manager with software components shall maintain a requirements mapping matrix or multiple requirements mapping matrices against requirements in this NPR, including those delegated to other parties or accomplished by contract vehicles or Space Act Agreements.

This requirement ensures that all software projects maintain a clear, updated mapping of invoked requirements from NPR 7150.2, including any tailoring, delegation, or contractually executed obligations. The matrix provides traceability, accountability, and compliance assurance across all stages of software development and acquisition.

This enhanced framework for this requirement ensures that Software Assurance personnel verify accurate, traceable, and properly maintained **Requirements Mapping Matrices (RMM)**, while addressing tailoring and delegation risks effectively. Through proactive reviews, clear metrics, and robust oversight, compliance with NPR 7150.2 and NASA-STD-8739.8 is strengthened, ensuring successful outcomes for NASA software projects.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project maintains a requirements mapping matrix (matrices) for all requirements in NPR 7150.2.

2. Maintain the requirements mapping matrix (matrices) for requirements in NASA-STD-8739.8.

Below is an improved and detailed Software Assurance (SA) framework for addressing this requirement, including updates to **Software Assurance Products, Objective Evidence, Metrics, and Guidance** based on best practices.

## 7.2 Software Assurance Products

### 7.2.1 Software Assurance and Software Safety Requirements Mapping Matrix (RMM)

**Purpose**: Documents the mapping and tailoring of software assurance and software safety requirements from **NPR 7150.2** and **NASA-STD-8739.8**, ensuring compliance, traceability, and delegation (if applicable).  
**Contents**:

* A complete list of all NPR 7150.2 and NASA-STD-8739.8 software assurance and safety requirements applicable for the software classification.
* Status indicators for each requirement:
  + **Standard** (invoked as is).
  + **Tailored** (modified with justification; linked to approval signatures).
  + **Delegated** (executed by a third party, e.g., contractors or international collaborators).
* Tailoring justifications linked to risk assessments and project plans.
* Signatures from the **Engineering Technical Authority (TA)**, **Software Assurance TA**, and **Chief Information Officer (CIO)** (where applicable, e.g., cybersecurity requirements).
* Cross-references to project plans (e.g., SMP, SAP) and lifecycle phases where requirements apply or are delegated.

### 7.2.2 RMM Review and Change Log

**Purpose**: Tracks all updates, reviews, and approvals of the Requirements Mapping Matrix (RMM) throughout the project lifecycle.  
**Contents**:

* Chronological log of updates and version history of the RMM.
* Records of all formal reviews, including change triggers (e.g., changes in software classification, new contract terms, etc.).
* Notes on discussions of SA/SS requirements tailoring decisions, approvals, and open issues.
* Documentation of changes communicated across teams (e.g., to contractors or collaborating organizations).
* Risks or pending issues associated with maintaining the RMM.

### 7.2.3 Tailored Software Assurance and Safety Requirements List

**Purpose**: Identifies all software assurance and safety requirements from **NPR 7150.2** and **NASA-STD-8739.8** that have been tailored.  
**Contents**:

* Tailored requirement details, including explicit references to:
  + Section of NPR 7150.2 or NASA-STD-8739.8 being tailored.
  + Specific tailoring actions (e.g., omission, partial application, alternative implementation).
  + Tailoring justifications and associated risks.
* Cross-referenced location of tailored requirements in project plans and procedures (e.g., SAP, SDP).
* Signed tailoring approvals from relevant technical authorities.

### 7.2.4 Delegated or Contracted Requirements Responsibility Matrix

**Purpose**: Tracks requirements delegated to contractors or managed through other agreements (e.g., Space Act Agreements).  
**Contents**:

* List of tailored or delegated SA/SS requirements.
* Contract vehicles, vendors, or collaborating organizations responsible for delegated requirements.
* Compliance mechanisms (e.g., audits, reviews, deliverables) to confirm fulfillment of delegated requirements.
* Approved mechanisms for tracking compliance by contractors or external entities.

### 7.2.5 Risk Assessment and Issues Tracking Report

**Purpose**: Documents risks and open issues related to maintaining the RMM and the fulfillment of tailored, delegated, or standard software assurance and safety requirements.  
**Contents**:

* Identified risks (e.g., unclear delegation responsibilities, conflicts in tailored requirements).
* Associated mitigation plans and responsible owners.
* Assessment of potential lifecycle impacts for unresolved issues.

## 7.3 Metrics

### 7.3.1 Project-Specific Metrics

1. **# of Software Work Product Non-Conformances Identified by Lifecycle Phase:**

   * Tracks non-conformances for SA/SS-related requirements, categorized by phase (e.g., requirements, design, implementation, testing).
   * Indicates areas where tailored or delegated requirements might introduce risk.
2. **% of Requirements Tailored Per Project:**

   * Tracks the ratio of tailored requirements to total requirements invoked from NPR 7150.2 and NASA-STD-8739.8.
   * Identifies projects with significant tailoring activity that might require additional oversight or risk assessment.
3. **# of Delegated Requirements Per Project:**

   * Tracks the delegated SA/SS requirements for third parties by lifecycle phase.
   * Provides visibility into compliance accountability for contractors or other delegated entities.

### 7.3.2 Organizational Metrics

1. **Identify Specific Requirements Tailored from NASA-STD-8739.8:**

   * Tracks specific tailored sections to determine patterns or recurring tailoring across projects.
2. **# of Projects Tailoring Each Requirement:**

   * Tracks which NPR 7150.2 or NASA-STD-8739.8 requirements are most frequently tailored across multiple projects to identify challenges, common risks, or process inefficiencies.
3. **Risk Trends Related to Tailored or Delegated Requirements:**

   * Monitors recurring risks associated with tailoring or delegation, providing insight into areas needing additional policies or management focus.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

### Software Assurance Actions:

1. **Maintain Updated RMM at Key Milestones:**

   * Confirm that the project maintains an accurate RMM for all software requirements from NPR 7150.2, with updates documented at key lifecycle points (SDR, PDR, CDR, TRR):
     + **Collect Matrix Before Development Plan Approval:** Obtain a copy before the SDP or SMP is formally approved to ensure that all requirements (tailored or standard) are accounted for.
     + **Maintain Signatory Approvals:** Verify that the Engineering TA, Software Assurance TA, and CIO (if applicable) have signed the RMM or approved tailored requirements.
2. **Assess Tailored SA Requirements in the Software Assurance Plan (SAP):**

   * Ensure the SAP explicitly documents tailored SA/SS requirements and their justification.
   * Confirm tailored requirements are integrated into the SA audit schedule, reviews, and deliverables.
3. **Verify Delegation and Responsibility for Requirements Fulfilled by Contractors:**

   * Ensure delegated requirements are explicitly reflected in contracts or agreements.
   * Confirm mechanisms exist for verifying compliance (e.g., deliverables, audits, reviews).
4. **Conduct Regular RMM Audits:**

   * Audit the accuracy of the RMM periodically to ensure it reflects the latest requirements and lifecycle changes.
5. **Address Tailoring and Delegation Risks:**

   * Identify risks and gaps in tailored or delegated requirements early.
   * Mitigate risks through regular communication with project stakeholders, contractors, and teams assuming delegation responsibilities.
6. **Define Responsibility for SA/SS Requirements:**

   * Ensure the RMM and supporting documentation clearly define who is responsible for meeting delegated or tailored software assurance and software safety requirements.

See also Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan),

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) * [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements) * [SWE-152 - Review Requirements Mapping Matrices](/spaces/SWEHBVD/pages/102695508/SWE-152+-+Review+Requirements+Mapping+Matrices) * [SWE-212 - NASA-STD-8739 Mapping Matrices](/spaces/SWEHBVD/pages/102695331/SWE-212+-+NASA-STD-8739+Mapping+Matrices)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics). * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [PAT-028 - NPR 7150.2D Compliance Matrix](/spaces/SITE/pages/119242755/PAT-028+-+NPR+7150.2D+Compliance+Matrix) |

# 8. Objective Evidence

Objective evidence verifies that the Requirements Mapping Matrix is accurate, traceable, and updated throughout the software lifecycle.

## 8.1 Objective Evidence to Be Collected

1. **Approved Requirements Mapping Matrix (RMM):**

   * Signed and approved RMM specific to the project’s NPR 7150.2 requirements and software classification.
   * Tailoring details, including justifications and required signatures.
   * Records of delegated requirements, including signed agreements/contracts for third-party or contractor-fulfilled obligations.
2. **Software Development Plans Incorporating Requirements:**

   * Confirmation that the tailored and standard requirements are reflected in:
     + Software Development Plan (SDP).
     + Software Assurance Plan (SAP).
     + Software Management Plan (SMP).
     + Other plans impacted by tailored or delegated requirements.
3. **Review Records and Updates:**

   * Records of RMM reviews conducted at key lifecycle points (e.g., SDR, CDR, TRR).
   * Meeting minutes and documentation of tailoring or delegation decisions.
4. **Contractual Documentation:**

   * Details of Space Act Agreements, contracts, or delegated agreements outlining compliance with specific SA/SS requirements.
5. **Risk and Issue Tracking:**

   * Logs documenting identified risks or issues with tailored or delegated requirements, including mitigation plans.

## 8.2 Definition of Objective Evidence:

Objective evidence includes signed documents, review records, linked project artifacts, and observed activities that demonstrate the maintenance and applicability of the RMM and delegated requirements.

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
