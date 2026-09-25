# SWE-126 - Tailoring Considerations

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695490. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations

SWE-126 - Tailoring Considerations

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695490)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695490&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)

# 1. Requirements

2.1.8.2 The technical and institutional authorities for requirements in this directive shall: 

a. Assess projects’ requirements mapping matrices and tailoring from requirements in this directive by:

(1) Checking the accuracy of the project’s classification of software components against the definitions in Appendix D.  
(2) Evaluating the project’s Requirements Mapping Matrix for commitments to meet applicable requirements in this directive, consistent with software classification.  
(3) Confirming that requirements marked “Not-Applicable” in the project’s Requirements Mapping Matrix are not relevant or not capable of being applied.  
(4) Determining whether the project’s risks, mitigations, and related requests for relief from requirements designated with “X” in Appendix C are reasonable and acceptable.  
(5) Approving/disapproving requests for relief from requirements designated with “X” in Appendix C, which falls under this Authority’s scope of responsibility.  
(6) Facilitating the processing of projects’ requirements mapping matrices and tailoring decisions from requirements in this directive, which falls under the responsibilities of a different Authority (see column titled “Authority” in Appendix C).  
(7) Include the SAISO (or delegate) in all software reviews to ensure software cybersecurity is included throughout software development, testing, maintenance, retirement, operations, management, acquisition, and assurance activities.  
(8) Ensuring that approved requirements mapping matrices, including any tailoring rationale against this directive, are archived as part of retrievable project records.

b. Indicate the Technical Authority or Technical Authorities approval by signature(s) in the Requirements Mapping Matrix itself, when the Requirements Mapping Matrix is used to tailor from the applicable “X” requirement(s).

## 1.1 Notes

a. To effectively assess projects’ requirements mapping matrices, the designated Center Engineering Technical and Institutional Authorities for this NPR are recognized NASA software engineering experts or utilize recognized NASA software engineering experts in their decision processes. NASA-HDBK-2203 contains valuable information on each requirement, links to relevant NASA Lessons Learned, and guidance on tailoring. Center organizations or branches may also share frequently used tailoring and related common processes.

b. The Requirements Mapping Matrix documents the requirements that the project plans to meet, “not applicable” requirements, and any tailoring approved by designated Authorities with associated justification. If a project wants to tailor a requirement marked as HQ TA, then the project is required to get NASA HQ approval (e.g., OCE, OSMA, OCIO, or OCHMO) on a tailored request or a software Requirements Mapping Matrix.

## 1.2 History

Click here to view the history of this requirement: SWE-126 History

SWE-126 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 6.3.3 The Engineering Technical Authority(s) for this NPR shall consider the following information when assessing waivers and deviations from requirements in this NPR:   1. 1. The NASA software inventory data on the project.    2. The classification of systems and subsystems containing software, as defined in Appendix E.    3. Applicable Center-level software directives that meet the intent of this NPR.    4. Applicable contractor and subcontractor software policies and procedures that meet the intent of this NPR.    5. Potential impacts to NASA missions.    6. Potential impacts to health, medical concerns, or safety. |
| Difference between A and B | Re-write of the requirement |
| B | 2.1.3.6  Serving as Technical Authorities for requirements in this directive, Center Directors, or designees shall:  a. Assess project’s compliance matrices, tailoring, waivers, and deviations from requirements in this directive by:  (1)  Checking the accuracy of the project’s classification of software components against the definitions in Appendix D.  (2)  Evaluating the project’s compliance matrix for commitments to meet applicable requirements in this directive, consistent with software classification.  (3)  Confirming that requirements marked “Not-Applicable” in the project’s compliance matrix are not relevant or not capable of being applied.  (4)  Determining whether the project’s risks, mitigations, and related requests for relief from requirements designated with “X” in Appendix C, are reasonable and acceptable.  (5) Coordinate with the Center S&MA organization that the compliance matrix implementation approach does not impact safety and mission assurance on the project.  (6)  Approving/disapproving request for relief from requirements designated with “X” in Appendix C, which fall under this Technical Authority’s scope of responsibility.  (7)  Facilitating the processing of projects’ tailoring/compliance matrices, tailoring, waivers, or deviations from requirements in this directive, which fall under the responsibilities of a different Technical Authority (see column titled “Technical Authority” in Appendix C).  (8)  Ensuring that approved compliance matrices, including any waivers and deviations against this directive, are archived as part of retrievable project records. |
| Difference between B and C | - Added Institutional Authority(s) to the requirement; Changed "compliance" to "Requirements Mapping" matrix / matrices (RMM) everywhere;  - Removed "waivers, and deviations" in items a., (7) and (8);  - Removed item (5) in Rev B which is "Coordinate with the Center S&MA organization that the compliance matrix implementation approach does not impact safety and mission assurance on the project.";  - Removed "Technical" in Rev B items (6) and (7), which are items (5) and (6) in Rev C;  - Added requirement item (7) in Rev C;  - Changed "waivers, and deviations" to "tailoring rationale" in item (8); - Added requirement b. which requires the Technical Authority to approve tailoring of the RMM by signature - this merges SWE-145 into this SWE #. |
| C | 2.1.5.6 Serving as technical and institutional authorities for requirements in this directive, Center Director, or designee, shall:    a. Assess projects’ requirements mapping matrices and tailoring from requirements in this directive by:  (1) Checking the accuracy of the project’s classification of software components against the definitions in Appendix D.  (2) Evaluating the project’s Requirements Mapping Matrix for commitments to meet applicable requirements in this directive, consistent with software classification.  (3) Confirming that requirements marked “Not-Applicable” in the project’s Requirements Mapping Matrix are not relevant or not capable of being applied.  (4) Determining whether the project’s risks, mitigations, and related requests for relief from requirements designated with “X” in Appendix C are reasonable and acceptable.  (5) Approving/disapproving requests for relief from requirements designated with “X” in Appendix C, which falls under this Authority’s scope of responsibility.  (6) Facilitating the processing of projects’ requirements mapping matrices and tailoring decisions from requirements in this directive, which falls under the responsibilities of a different Authority (see the column titled “Authority” in Appendix C).  (7) Include the Center CIO and CISO (or delegate) in all software reviews to ensure software cybersecurity is included throughout software development, testing, maintenance, retirement, operations, management, acquisition and assurance activities.  (8) Ensuring that approved requirements mapping matrices, including any tailoring rationale against this directive, are archived as part of retrievable project records.    b. Indicate the Technical Authority or Technical Authorities approval by the signature(s) in the Requirements Mapping Matrix itself, when the Requirements Mapping Matrix is used to tailor from the applicable “X” requirement(s). |
| Difference between C and D | This requirement was moved to section 2.1.8 in the document, and item b. was added |
| D | 2.1.8.2 The technical and institutional authorities for requirements in this directive shall:   a. Assess projects’ requirements mapping matrices and tailoring from requirements in this directive by:  (1) Checking the accuracy of the project’s classification of software components against the definitions in Appendix D. (2) Evaluating the project’s Requirements Mapping Matrix for commitments to meet applicable requirements in this directive, consistent with software classification. (3) Confirming that requirements marked “Not-Applicable” in the project’s Requirements Mapping Matrix are not relevant or not capable of being applied. (4) Determining whether the project’s risks, mitigations, and related requests for relief from requirements designated with “X” in Appendix C are reasonable and acceptable. (5) Approving/disapproving requests for relief from requirements designated with “X” in Appendix C, which falls under this Authority’s scope of responsibility. (6) Facilitating the processing of projects’ requirements mapping matrices and tailoring decisions from requirements in this directive, which falls under the responsibilities of a different Authority (see column titled “Authority” in Appendix C). (7) Include the SAISO (or delegate) in all software reviews to ensure software cybersecurity is included throughout software development, testing, maintenance, retirement, operations, management, acquisition, and assurance activities. (8) Ensuring that approved requirements mapping matrices, including any tailoring rationale against this directive, are archived as part of retrievable project records.  b. Indicate the Technical Authority or Technical Authorities approval by signature(s) in the Requirements Mapping Matrix itself, when the Requirements Mapping Matrix is used to tailor from the applicable “X” requirement(s). |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

To reduce the risk and cost associated with the software development and use on NASA projects.

This requirement emphasizes the role of the technical and institutional authorities in reviewing, approving, and managing a project's **Requirements Mapping Matrix** (RMM) and tailoring decisions from the directive. By ensuring that software classification and requirements are properly assessed, risks are addressed, and deviations or tailoring are justified, this process ensures a structured, traceable, and rigorous approach to software development for NASA missions. Here’s the rationale for the specific components of this requirement:

---

### **General Rationale for the Requirement**

* **Consistency with NASA’s Practices for Mission Success**: The proper mapping and tailoring of requirements ensure consistency between the project’s specific software needs and NASA’s overarching directives, policies, and standards. This is critical for reducing risks, improving quality, and enhancing mission success.
* **Accountability and Risk Mitigation**: The provision of formal authority to assess the accuracy of requirements, validate mitigations, and approve tailoring or deviations ensures responsibility and accountability. By having checks and balances in this process, NASA reduces the potential for oversight or noncompliance that could jeopardize safety, cybersecurity, or mission objectives.
* **Lifecycle Integration**: Including cybersecurity and maintaining retrievable records directly supports informed decision-making, continual risk management, and compliance auditing throughout the software lifecycle.

---

### **Detailed Rationale for Subcomponents**

#### **a. Assess projects’ requirements mapping matrices and tailoring from requirements in this directive**

This section ensures that projects critically and rigorously evaluate their compliance with applicable requirements and document their decisions in a way that aligns with NASA’s broader mission objectives.

1. **(1) Checking the accuracy of the project’s classification of software components against the definitions in Appendix D**

   * **Why this matters**: Proper software classification drives the applicability and stringency of requirements. Misclassifying software could lead to applying insufficient controls (potentially exposing a project to avoidable risks) or overly stringent controls (causing unnecessary resource strain and inefficiencies). Ensuring accuracy ensures that each component’s criticality is evaluated objectively based on documented definitions.
   * **Preventive Value**: This reduces the risk of underestimating the importance of mission-critical software while ensuring resources are appropriately aligned with the software’s scope.
2. **(2) Evaluating the project’s Requirements Mapping Matrix for commitments to meet applicable requirements in this directive, consistent with software classification**

   * **Why this matters**: The RMM prioritizes clarity and visibility of the project’s commitment to applicable requirements. Each commitment ensures adherence to a structured framework that balances project needs with NASA’s safety, quality, and information assurance requirements.
   * **Consistency Check**: This step ensures that all applicable requirements based on software classification are explicitly considered and not inadvertently excluded, confirming consistency between classification and tailoring decisions.
3. **(3) Confirming that requirements marked “Not-Applicable” in the project’s Requirements Mapping Matrix are not relevant or not capable of being applied**

   * **Why this matters**: Incorrectly marking requirements as “Not-Applicable” can create critical gaps in compliance and safety. Validating “Not-Applicable” decisions ensures that requirements are excluded only when they are demonstrably irrelevant or impossible to apply to the particular project or software functionality.
   * **Support for Audits**: This confirmation avoids misuse of the “Not-Applicable” status, thus ensuring accountability and proper documentation in case of audits or reviews.
4. **(4) Determining whether the project’s risks, mitigations, and related requests for relief from requirements designated with “X” in Appendix C are reasonable and acceptable**

   * **Why this matters**: Certain “X” requirements are mandatory unless compelling justification is provided for tailored relief. An evaluation of the risks and mitigations allows decision-makers to ensure that any proposed deviation from these requirements does not jeopardize safety, cybersecurity, functionality, or the mission. This gives technical authorities confidence that the risks are understood and well-managed.
5. **(5) Approving/disapproving requests for relief from requirements designated with "X" in Appendix C, which falls under this Authority’s scope of responsibility**

   * **Why this matters**: Granting formal authority to approve or disapprove deviations ensures that critical system safeguards remain intact. It allows stakeholders to balance flexibility for innovation with the need for adherence to NASA’s rigorous software standards and practices.
   * **Accountability**: By formally empowering technical authorities to approve or reject these requests, it reinforces accountability and provides a clear chain of responsibility for decisions.
6. **(6) Facilitating the processing of projects’ requirements mapping matrices and tailoring decisions from requirements in this directive, which falls under the responsibilities of a different Authority (see column titled “Authority” in Appendix C)**

   * **Why this matters**: Some requirements or tailoring decisions fall outside the direct authority of the technical authority (e.g., cybersecurity requirements overseen by the SAISO). The facilitation role ensures proper coordination between different authorities, ensuring smooth decision-making without confusion over jurisdiction.
   * **Supports Collaboration**: This ensures that all necessary authorities are involved in tailoring decisions, preventing organizational silos and unaddressed compliance gaps.
7. **(7) Include the SAISO (or delegate) in all software reviews to ensure software cybersecurity is included throughout software development, testing, maintenance, retirement, operations, management, acquisition, and assurance activities**

   * **Why this matters**: Software cybersecurity is critical to safeguarding NASA’s missions and data assets from threats and vulnerabilities. Including the **Senior Agency Information Security Officer (SAISO)** ensures expert oversight and consistent implementation of security measures across all lifecycle phases.
   * **Comprehensive Coverage**: Cybersecurity challenges evolve over time, and ongoing oversight supports proactive mitigation strategies throughout the entire software lifecycle.
8. **(8) Ensuring that approved requirements mapping matrices, including any tailoring rationale against this directive, are archived as part of retrievable project records**

   * **Why this matters**: Archiving approved RMMs and tailoring rationales enables traceability and transparency. This allows future stakeholders to understand the decision-making process, verify compliance, and audit decisions made during the software lifecycle.
   * **Facilitates Knowledge Management**: Archived records are also valuable historical tools for lessons learned, enabling continuous improvement for future projects.

---

#### **b. Indicating Technical or Institutional Authority Approval**

1. **Why this matters**: Approval by signature signifies accountability and concurrence by the Technical Authority, demonstrating that the tailoring process has been thoroughly vetted and approved.
2. **Legal and Documentation Requirement**: By requiring signatures on the Requirements Mapping Matrix (where applicable), the directive ensures all deviations are officially documented, demonstrating compliance with NASA’s governance and quality control processes, thus protecting against issues during audits or reviews.

---

### **Benefits of This Requirement**

The structured review and approval of the RMM provides significant advantages:

1. **Risk Management**: It ensures meaningful oversight to manage risks associated with tailoring or noncompliance while identifying and evaluating mitigations.
2. **Consistency and Compliance**: Formal mapping and approval of requirements ensure consistency with NASA’s software classification guidelines, reducing opportunities for gaps or errors.
3. **Efficient Oversight**: By involving applicable authorities (e.g., SAISO for cybersecurity), this avoids siloed decision-making and ensures a holistic view of the software project.
4. **Accountability**: Signatures and documentation create a clear audit trail that holds stakeholders accountable for tailoring and compliance decisions.
5. **Promotes Adaptability**: Formal tailoring processes allow small deviations where justified by project-specific needs without jeopardizing safety, quality, or mission performance.

---

### **Summary**

This requirement ensures that all software projects at NASA meet applicable requirements, properly classify software, and tailor only when justified through a transparent and accountable process. By empowering technical and institutional authorities, enforcing sound risk management, and involving cybersecurity experts, this requirement aligns projects to NASA’s mission-critical safety and quality standards while facilitating flexibility for diverse project needs.

# 3. Guidance

## 3.1 Requesting Deviations or Waivers

NASA’s **NPR 7150.2** establishes baseline requirements for software developed by or for the agency. When deviations or waivers are required, a formal process must be followed, ensuring that requested relief is assessed, justified, and approved by the appropriate **Technical Authorities (TAs)**. This action balances the project's specific needs with NASA’s standards and mission assurance.

**Definitions**:

* **Deviation**: A documented authorization releasing a program or project from meeting a requirement *before* the requirement is placed under configuration control.
* **Waiver**: A documented authorization releasing a program or project from meeting a requirement *after* the requirement has been placed under configuration control.

---

#### **Key Stakeholders and Responsibilities**:

* **Engineering Technical Authority (ETA)**: Ensures technical rigor and alignment with mission objectives.
* **Safety and Mission Assurance Technical Authority (SMA TA)**: Evaluates safety and mission completion risks.
* **Health and Medical Technical Authority (where applicable)**: Assesses impacts on health and safety.
* **Project Team**: Prepares deviation/waiver requests with complete justifications, including risks, mitigations, and rationale.

Requests for relief, including tailoring, compliance matrices, waivers, and deviations, must follow the authority listings in **Appendix C** of NPR 7150.2. All relief requests require approval by both Engineering TA (ETA) and Safety & Mission Assurance TA (SMA TA).

**NPR 7150.2 NASA Software Engineering Requirements**

2.2.1 Software requirements tailoring is the process used to seek relief from NPR requirements consistent with program or project objectives, acceptable risk, and constraints. To accommodate the wide variety of software systems and subsystems, application of these requirements to specific software development efforts may be tailored where justified and approved. To effectively maintain control over the application of requirements in this directive and to ensure proposed tailoring from specific requirements are appropriately mitigated, NASA established TA governance. Tailoring from requirements in this directive are governed by the following requirements, as well as those defined in NPD 1000.3, The NASA Organization NPD 2800.1, NPR 2810.1, NPR 7120.5, NPR 7120.7, NPR 7120.8, NPR 7120.11 and NPR 8715.3 for all of the Agency’s investment areas. The Technical and Institutional Authority for each requirement in this NPR is documented in the “Authority” column of Appendix C. The responsible program, project, or operations manager need to formally accept the tailoring risk. Tailoring decided at the Center level are to consult the Center ETA, Center SMA TA, Center Health and Medical TA, and the NASA CIO’s Center IT Authority designee as defined in the requirements mapping matrix. The OSMA has co-approval on any tailoring decided at the HQ level that involves software. The Office of the Chief Medical Officer (OCHMO) has co-approval on any tailoring decided that involves software with health and medical implications. The SAISO, or designee, has co-approval on any tailoring of the cybersecurity requirements in Section 3.11. For tailoring involving human safety risk, the actual risk taker(s) (or official spokesperson[s] and appropriate supervisory chain) need to formally agree to assume the risk. ’[083](#_tabs-<p></p>)

## 3.2 Preparing Deviations or Waiver Requests

Preparing deviation/waiver requests is a critical process requiring detailed documentation and rigorous assessment. The following steps guide project teams and Technical Authorities to ensure proper evaluations:

#### **1. Start with NPR 7150.2 and NPR 7120.5**

* **Overview**: NPR 7150.2, Chapter 2, provides software-specific instructions for tailoring, deviation, or waiver requests.
* **General Context**: Refer to **NPR 7120.5**, which provides overarching guidance for managing deviations and waivers at the program and project levels.

#### **2. Classify the Software**

* **Why This Is Important**: Correct software classification ensures proportional evaluation of requirements.
  + Definitions and examples of software classifications (A-D) in Appendix D of NPR 7150.2 help categorize systems properly.
  + High-criticality software (*e.g., Class A or B*) and safety-critical systems require heightened scrutiny.
* **What to Confirm**: Ensure the system or subsystem classification is correct since requirements vary significantly across classifications.

#### **3. Develop a Clear and Detailed Justification**

* **Critical Elements to Include in Requests**:

  + Relevant **requirement number(s)**.
  + Project-specific rationale for the waiver/deviation request.
  + Risk assessments, potential mission impacts, and proposed mitigations.
  + How granting relief maintains alignment with NASA’s mission goals.
* **Higher Scrutiny for Safety-Critical or Future Software Reuse**: If waiving a safety-related or high-criticality requirement, consider not only the current project but also the potential impact on future missions. Software often evolves or is reused, and relief granted today could cause negative consequences in the future.

#### **4. Build an Updated Compliance Matrix**

* Compare the project’s **NPR 7150.2 compliance matrix** with **Appendix C** of NPR 7150.2:
  + Clearly identify tailored requirements or requests for “Not Applicable” status.
  + Justify any requirements marked “Not Applicable” with documented rationale to ensure the requirement truly cannot be applied.
  + Validate that all required "X" requirements for the software’s classification are being addressed properly.

#### **5. Address Coordination Requirements**

* Collaborate with the **Center Safety & Mission Assurance (SMA) organization (CSMA)** to ensure deviated or waived requirements do not adversely impact safety, mission success, or mission assurance processes.
* Resolve disagreements via the Center’s Technical Authority process.

## 3.3 Reviewing and Approving Deviations or Waivers

The roles of the **Technical Authorities** (Engineering TA and SMA TA) in assessing waiver/deviation requests are critical in ensuring compliance and reducing risks.

#### **Key Functions:**

1. **Evaluate Software Classification Accuracy**:

   * Confirm the system’s software classification per Appendix D to ensure the level of scrutiny is consistent with the software’s criticality.
2. **Assess Compliance Matrix Entries**:

   * Ensure requirements with “Not Applicable” or requests for relief include supporting justification to confirm their exclusion is appropriate.
3. **Weigh Risks and Mitigations**:

   * Analyze whether the risks, mitigations, and rationale associated with the waiver/deviation are clear, complete, reasonable, and mission-aligned.
   * Consider impacts not only on this mission but also on potential future uses of the software.
4. **Coordinate with Stakeholders**:

   * Ensure all stakeholders, including **Health, Safety**, and **Medical TAs**, are involved in requests with cross-disciplinary implications.
   * Facilitate coordination across authorities when relief requests fall outside a single TA’s scope.
5. **Approve/Disapprove Requests Based on NPR 7150.2 Appendix C**:

   * For "X" requirements, validate whether the justification aligns with the specific authority’s evaluation criteria.
   * Consult **SWE-139** for guidance on “shall” statement adherence.
   * Communicate decisions clearly, documenting approvals or disapprovals with rationale.

## 3.4 Archiving Deviation and Waiver Decisions

Archiving approved compliance matrices and deviation/waiver rationales in a **retrievable project repository** is critical for project continuity and future reference.

#### **Why This Is Important**:

* Supports audit readiness.
* Provides traceability during reviews throughout the project lifecycle.
* Ensures future missions can learn from previous decisions tied to software requirements.

## 3.5 Tracking and Reporting Requirements Tailoring

* Track **deviations** and **waiver requests** in the project’s **configuration management system**, ensuring all activities are documented and accessible.
* Include documentation for:
  + Submission and evaluation procedures.
  + Risk mitigation strategies.
  + Approvals and final outcomes (including technical rationales for granted relief).

#### **Resources for Configuration Management**:

* Reference configuration management systems used across NASA for templates and tools.
* Ensure tracking aligns with **NPR 7120.5** process guidelines.

---

### **ETA and SMA TA Considerations During Review**

In addition to the technical evaluation, the following areas should be reviewed:

* **Impacts on Health and Safety**: Ensure the inclusion of **Health and Medical TA** for human-rated systems or projects with medical implications.
* **Failure Mode Analysis**: Evaluate **Failure Mode Effects Analysis (FMEA)** findings for potential risks.
* **Hazard Reports and Safety Risks**: Review safety-focused reports to determine if the waived requirement impacts safety-critical functions.

## 3.6 Best Practices for Compliance Matrices

* **Plan Early**: Involve the TAs during the requirements definition process to minimize adjustments (waivers or deviations) later in the project lifecycle.
* **Leverage Lessons Learned**: Document lessons from processing deviations and waivers, and reference historical waiver cases where applicable.
* **Use Software Release Authority Guidance**: Ensure compliance matrix information satisfies both NPR 7150.2 and software release authority needs (NPR 2210.1C).

---

### **Related Resources**

* **SWE-140 - Comply with Requirements**
* **SWE-150 - Review Changes to Tailored Requirements**
* **SWE-216 - Internal Software Sharing List**
* **7.04 - Flow Down of NPR Requirements to Contracts**
* **7.16 - Appendix C Requirements Mapping and Compliance Matrix**

This guidance ensures that deviation and waiver processes are consistent, thorough, and well-documented, minimizing risks while allowing flexibility to tailor software requirements safely.

Requests for relief from software requirements can take a variety of forms, including tailoring, compliance matrices, waivers, and deviations. Per NPR 7150.2D,

**NPR 7150.2 NASA Software Engineering Requirements**

2.2.6 Requests for software requirements relief at either the Center or HQ TA level (i.e., partial or complete relief) may be submitted in the streamlined form of a Requirements Mapping Matrix. The required signatures from engineering, NASA CIO, and SMA authorities are to be obtained. A required signature from designated SAISO is required for relief of cybersecurity requirements. If the Requirements Mapping Matrix is completed and approved in accordance with NPR 7120.5’s direction on Authority and this directive, it meets the requirements for requesting tailoring.[083](#_tabs-<p></p>)

See also [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements), [SWE-216 - Internal Software Sharing List](/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List),

See also Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis)

Additional guidance on deviations and waivers related to contracts may be found in the following related topic in this Handbook: [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects).

See also [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix),

See also [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements),

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-140 - Comply with Requirements](/spaces/SWEHBVD/pages/102695498/SWE-140+-+Comply+with+Requirements) * [SWE-150 - Review Changes To Tailored Requirements](/spaces/SWEHBVD/pages/102695506/SWE-150+-+Review+Changes+To+Tailored+Requirements) * [SWE-216 - Internal Software Sharing List](/spaces/SWEHBVD/pages/102695547/SWE-216+-+Internal+Software+Sharing+List)        * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

NASA projects vary greatly in size and complexity, but even small projects must follow the necessary processes for requesting deviations or waivers from NPR 7150.2 software requirements. The following guidance is tailored specifically to small projects, helping teams ensure compliance, maintain accountability, and balance flexibility with governance.

---

### **Understanding the Importance for Small Projects**

Small projects often operate with limited resources, smaller teams, and tighter timelines. However, rigorous processes for deviations and waivers remain essential for ensuring:

1. **Alignment with NASA’s Standards**: Even small-scale software can be critical for mission success or safety. Relief from requirements must be justified and evaluated for potential risks to current and future NASA objectives.
2. **Effective Resource Use**: By following a structured process, small projects can avoid wasting time and effort addressing requirements that may not apply.
3. **Traceability and Documentation**: Properly documenting decisions ensures transparency and aids lessons learned for subsequent projects.

---

### **Tailored Steps for Small Projects**

#### **1. Determine if a Deviation or Waiver Is Necessary**

Before initiating a deviation or waiver request, perform a quick review of the requirement to determine if it applies or if tailoring can resolve the issue without a formal request.

* **Ask the following questions**:

  + Does the requirement apply to your software classification? (Refer to **Appendix D of NPR 7150.2** for classification definitions.)
  + Can the requirement be tailored (adjusted) without requiring a formal deviation or waiver? Tailoring is typically defined in the **Requirements Mapping Matrix (RMM)** without further approval.
* **Qualifications for Deviation/Waiver**:

  + **Deviation**: If the project cannot meet the requirement *before* it’s under configuration control, request a deviation.
  + **Waiver**: If the project identifies the inability to meet the requirement *after* it’s been placed under configuration control, request a waiver.
* **Checklist for Small Teams**:

  + Confirm the software classification is correctly assigned.
  + Consult with your **Engineering TA (ETA)** or **Safety and Mission Assurance TA (SMA TA)** early to validate whether a formal deviation or waiver request is necessary.

---

#### **2. Prepare the Simplified Deviation or Waiver Request**

Small projects need to balance thoroughness with simplicity. A clear and concise request for relief is key to minimizing bottlenecks in the review and approval process.

* **Include the following in your request (lean version)**:

  1. **Requirement Information**:
     + State the specific requirement number (from **Appendix C** of NPR 7150.2).
     + Indicate whether this is a deviation or waiver.
  2. **Software Classification**:
     + Refer to Appendix D for your software’s class (A, B, C, D, safety-critical, etc.).
     + Explain why this classification applies to your software.
  3. **Rationale**:
     + Clearly explain why the requirement cannot be met. Use simple, project-specific language.
  4. **Risk Assessment**:
     + Outline the risks associated with not meeting the requirement and how those risks will be mitigated.
     + Use a lightweight qualitative or semi-quantitative risk analysis if formal tools are not available (e.g., low, medium, high probability/impact ratings).
  5. **Mission Impact**:
     + Address how this deviation/waiver will affect your project and future reuse of the software.
  6. **Proposed Mitigations**:
     + Describe specific actions the project will take to reduce risks or mitigate the effects of not fully meeting the requirement.
* **Templates for Small Projects**:

  + Use pre-existing deviation/waiver templates (often accessible through your Center’s TA or safety office).
  + Limit unnecessary complexity in explanations while meeting the basic guidelines in **NPR 7120.5 and NPR 7150.2**.

---

#### **3. Collaborate with Technical Authorities**

For small projects, the **Engineering Technical Authority (ETA)** and **Safety & Mission Assurance Technical Authority (SMA TA)** are your primary reviewers. Early and ongoing communication helps smooth and expedite the approval process.

* **Early Consultation**:

  + Discuss the deviation/waiver request draft with your TAs. They can help identify issues and ensure the request includes all necessary details.
  + Include Center Safety & Mission Assurance (CSMA) staff if safety-related risks are involved.
* **For cross-disciplinary issues**:

  + If the request impacts health, safety, or mission assurance, or if the project is human-rated, work with the **Health & Medical TA** or other relevant authorities to address multidisciplinary concerns (e.g., cybersecurity, environment).

---

#### **4. Simplify the Compliance Matrix**

Small projects must still provide a **Requirements Mapping Matrix (RMM)** to demonstrate compliance with NPR 7150.2. However, the complexity of the RMM can be scaled to match the scope and classification of your project.

* **Steps to Tailor Your Compliance Matrix**:
  + Use a pre-existing RMM template to avoid recreating the structure from scratch.
  + Clearly mark requirements that are:
    - **Fully met**: Provide a short description (e.g., "Requirement implemented during design").
    - **Not applicable**: Justify why the requirement does not apply to your project.
    - **Relief requested (waiver or deviation)**: Reference the associated request and provide the status (e.g., "Pending approval").
  + Keep justifications brief while meeting the required level of detail.

---

#### **5. Document and Archive Decisions**

It’s critical to properly document and archive all deviation/waiver requests and decisions, even for small projects, to ensure future teams have access to the project’s decision history.

* **How to Archive for Small Projects**:
  + Store all approved compliance matrices, waivers, and deviations in the **project’s configuration management system**.
  + Maintain a simple, well-organized repository (e.g., a shared folder, SharePoint site, or cloud storage) with the:
    - Approved requests.
    - Decision rationale.
    - Corresponding risk mitigation plans.

---

#### **6. Coordinate Reviews, Tracking, and Approvals**

Small projects may involve fewer layers of review, but the same principles apply. Coordinate relief requests and approval workflows carefully.

* **Tracking**:

  + Assign responsibility to a small project team member to track the status of all waiver and deviation requests. A simple spreadsheet or low-maintenance issue tracker (e.g., Jira, Trello) works well for this purpose.
* **Risks and Updates**:

  + As software evolves, outdated relief requests may need updates, especially if the software is reused for other missions or repurposed. Ensure ongoing compliance reviews at major lifecycle milestones.

---

#### **7. Tailored Risk Assessments for Small Projects**

Risk management plays a central role in approving deviations or waivers, but small projects often have fewer resources for formal risk assessments.

* **Scalable Risk Analysis**:
  + Focus on the essentials:
    - What *exactly* will happen if the requirement is not met?
    - How likely is this risk to occur?
    - How severe are the consequences if it happens?
  + Use qualitative analyses (e.g., "low, medium, high" risk ratings) for simplicity.
  + Document your mitigations in clear, straightforward language.

---

### **Final Checklist for Small Projects**

1. **Understand the Requirement**:
   * Confirm the requirement’s applicability and identify if a deviation or waiver is necessary.
2. **Prepare the Request**:
   * Provide a concise, thorough rationale while focusing on the risk, justification, and impact.
3. **Work with Technical Authorities**:
   * Collaborate early with the ETA, SMA TA, and other relevant authorities.
4. **Simplify and Document**:
   * Use readily available templates and tools and maintain an organized repository for waivers/deviations.
5. **Track Decisions**:
   * Ensure all approval statuses, risks, and justifications are up-to-date and accessible for audits or future projects.

---

### **Conclusion**

Small projects can implement efficient processes for deviations and waivers by using simplified templates, collaborating with technical authorities early, and tailoring compliance matrices to match the project's scope. While lighter in execution, the outcomes still align with NPR 7150.2 requirements, ensuring that small projects remain safe, compliant, and effective while minimizing unnecessary burden.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-023)

  [Health and Medical Requirements for Human Space Exploration,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8900&s=1 "Click to open in new window")

  NPR 8900.1B, NASA Office of the Chief Health & Medical Officer, 2008., Effective Date: December 16, 2016, Expiration Date: December 16, 2021
* (SWEREF-024)

  [Human-Rating Requirements for Space Systems (Updated w/Change 2)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=2C "Click to open in new window")

  NPR 8705.2C, NASA Office of Safety and Mission Assurance, 2008.,
  Effective Date: July 10, 2017, Expiration Date: July 10, 2025
* (SWEREF-036)

  [NASA Policy for Safety and Mission Success,](http://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=8700&s=1E "Click to open in new window")

  NPD 8700.1E, NASA Office of Safety and Mission Assurance, 2008. Effective Date: October 28, 2008, Expiration Date: April 28, 2020
* (SWEREF-037)

  [NASA Records Management Program Requirements (Updated w/Change 3),](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=1441&s=1E "Click to open in new window")

  NPR 1441.1E, NASA Office of the Chief Information Officer, Effective Date: January 29, 2015, Expiration Date: January 29, 2024
* (SWEREF-066)

  [The NASA Organization w/Change 85](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=3E "Click to open in new window")

  NPD 1000.3E, Associate Administrator, April 15, 2015, Expiration Date: April 15, 2026
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-144)

  [A Renewed Commitment to Excellence: An Assessment of the NASA Agency-wide Applicability of the Columbia Accident Investigation Board Report.](http://www.nasa.gov/pdf/55691main_Diaz_020204.pdf "Click to open in new window")

   Diaz, Al,NASA Goddard Space Flight Center (Jan, 2004). CAIB Columbia Accident Investigation Board Report. (August 2003). Vol. 1. PB2005-100968
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
* (SWEREF-268)

  [NASA Records Management,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1440&s=6I "Click to open in new window")

  NPD 1440.6I, 2008. Effective Date: September 10, 2014
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022
* (SWEREF-403)

  [Security of Information and Information Systems](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2810&s=1F "Click to open in new window")

  NPR 2810.1F, Office of the Chief Information Officer, Effective Date: January 03, 2022, Expiration Date: January 03, 2027,
* (SWEREF-406)

  [NASA Requirement Waivers.](http://nodis3.gsfc.nasa.gov/Waivers/Waiver_list.cfm "Click to open in new window")

  January, 2012. This is a list of the NASA Requirement Waivers. Instructions for submitting requirement waivers are outlined in Chapter 4 of NPR 1400.1, NASA Directives Procedural Requirements.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The **Columbia Accident Investigation Board (CAIB)** provided critical lessons for NASA regarding the importance of establishing a robust, independent system of oversight for technical requirements and waivers. This recommendation underscores both the necessity and the responsibility of an independent Technical Authority in ensuring that waivers, deviations, and requirements tailoring are rigorously reviewed, justified, and aligned with safety and mission assurance objectives. Below is an enhanced analysis of the CAIB recommendation and additional relevant NASA lessons learned:

---

#### **Columbia Accident Investigation Board, Report Vol 1, Aug 2003, Recommendation R7.5-1**

**Recommendation R7.5-1**:  
*"Establish an independent Technical Engineering Authority that is responsible for technical requirements and all waivers to them, and will build a disciplined, systematic approach to identifying, analyzing, and controlling hazards throughout the life of the Shuttle System."*

##### **Relevant Insights for Current NASA Software Waiver/Deviation Processes**:

* **Independence and Objectivity**: The recommendation highlights the importance of an independent Technical Engineering Authority (TA) that is not directly influenced by project management or schedule pressures. This independence ensures that the assessment of waivers and deviations is technically objective, without undue influence from cost or timeline constraints—a critical factor in small and large projects alike.

  + For software, this independence translates to ensuring Engineering Technical Authorities (ETAs), Safety and Mission Assurance Technical Authorities (SMA TAs), and any associated authorities make decisions based solely on safety, cybersecurity, mission objectives, and program impact.
* **Rigorous Review of Waivers and Tailoring**: All waivers and deviations must undergo a **disciplined and systematic process of evaluation** to identify hazards, analyze risks, verify mitigations, and ensure compliance is maintained at an acceptable level. The lack of a systematic approach (or improper tailoring of requirements) allowed deficiencies in risk identification for the Shuttle Program, directly contributing to the Columbia disaster.
* **Life-Cycle Responsibility**: Technical Authorities must exercise consistency in oversight across the entire system lifecycle—design, development, operation, and end-of-life—accounting for the evolving and cumulative risks associated with waiving or deviating from performance and safety-related requirements. For software projects, this means maintaining a strong awareness of how deviations could affect future reuse, upgrades, integration with new systems, and risks to cybersecurity as technology evolves.

##### **Lessons to Apply for Software Projects**:

1. **Thorough Hazard Analysis**:
   * Software deviations or waivers must undergo a hazard analysis to understand how tailoring or not meeting a given requirement could introduce risks: operational, safety, cybersecurity, and integration risks.
   * This approach directly applies the CAIB’s focus on systematic hazard control processes, even for decisions that seem minor at the project level.
2. **Integrating Disciplined Decision-Making**:
   * Approval of deviations and waivers requires rigorous data-driven decision-making, considering short- and long-term ramifications (e.g., software reuse and broader mission impact).
3. **Unified and Archivable Processes**:
   * The call for "disciplined, systematic approaches" also applies to **archiving formal documentation of deviations/waivers**, ensuring lessons are captured for current and future projects.

---

### **Lessons Learned: Class D Tailoring Does Not Exempt End‑to‑End System Responsibility**

**Problem/Observation:**  
Misaligned expectations among JPL, Caltech, and Lockheed Martin regarding what “Class D” entailed led to inconsistent assumptions about required rigor. The Anomaly Review Board (ARB) noted that these differing interpretations contributed to gaps in verification, coordination, and system‑level readiness.

**Context from the ARB:**  
Some stakeholders interpreted Class D as “reduced rigor overall,” while others assumed it meant “leaner processes but unchanged mission success standards.”  
This lack of shared understanding resulted in inconsistent application of engineering and assurance practices.

**Resulting Impacts:**  
• Unverified system‑level assumptions persisted into late phases.  
• Safing logic remained under‑tested, with incomplete validation of interactions and contingencies.  
• Fault management behavior was split across sequences and FSW, without holistic system‑level analysis or assurance.

**Relevant SWEHB Guidance:**  
Tailoring for Class D missions must still follow the NPR 7150.2D tailoring process, which requires clear documentation and agreement across all stakeholders.  
Key principles include:  
• Requirements may be tailored when justified,  
• But mission success criteria remain unchanged,  
• And all teams must share a common understanding of what is being tailored and why.

**Lesson Learned:**  
Class D flexibility does not remove system‑level engineering responsibility. Tailoring must be deliberate, documented, coordinated, and agreed upon—not assumed. When expectations differ across institutions, the result is fragmented verification, incomplete fault management coverage, and gaps in system assurance. Clear alignment on tailoring is essential to preserving end‑to‑end mission integrity.

### **Additional Relevant NASA Lessons Learned**

#### **Lesson 1: Importance of Risk Management in Tailoring Decisions**

**Source**: **Lesson Number: 0838, “Risk Management Lessons Learned”**  
**Summary**: A NASA lesson learned highlighted that projects often fail due to inadequate risk assessments during requirements tailoring. In past missions, teams underestimated the downstream impact of relaxed requirements, failing to identify hidden hazards introduced by incomplete compliance.

##### **Relevance to Waivers/Deviations**:

* Requirements not fully implemented or deferred require robust evaluation of risks and mitigations. Deviation reviews must assess how the proposed changes impact **mission assurance, safety-critical functionality, and system dependencies.**
* Tailoring decisions without full risk assessments (qualitative or quantitative) can result in gaps that are only discovered during software integration or operation.

##### **Application**:

Projects—especially small ones—should perform basic qualitative risk assessments for all requests for relief, including input from SMEs, TAs, and safety staff. Requirements marked Not Applicable, tailored, or waived must include corresponding justifications in project risk documentation.

---

#### **Lesson 2: Documentation and Traceability for Waivers/Deviations**

**Source**: **Lesson Number: 1122, “Decision Documentation is Critical for Reuse and Project Understanding”**  
**Summary**: On past projects, inadequate documentation of decisions related to waivers or deviations led to confusion during project handovers, integration with other systems, and potential reuse of assets (such as software or hardware). Unclear records around why requirements were waived or tailored resulted in unnecessary workarounds and integration delays.

##### **Relevance to Waivers/Deviations**:

* A lack of documentation around waivers or deviations makes it difficult for downstream users or future projects to understand limitations or unique risks. Poor traceability of relief decisions undermines accountability and impedes reuse.
* Software often persists beyond its original mission, and deviations granted at the program or project level can carry over unexamined to follow-on systems.

##### **Application**:

Ensure **approved compliance matrices, justifications, and decisions** (rationale, risks, mitigation strategies) are archived in a **retrievable project repository** as permanent records. Small projects can use accessible tools (e.g., simple shared document repositories or automated tracking systems) to maintain this information.

---

#### **Lesson 3: Tailoring High-Criticality Systems and Software**

**Source**: Technical Tailoring Lessons from the **Mars Climate Orbiter Loss Report (1999)**  
**Summary**: The loss of the Mars Climate Orbiter was partially attributed to misalignment in technical assumptions, overlooked constraints, and a failure to adhere to required engineering processes. The lack of adequate review and tailoring documentation for systems-level integration was a major contributor to the failure.

##### **Relevance to Waivers/Deviations**:

* Tailoring or deviating from requirements in high-criticality systems (e.g., safety-critical software or systems dedicated to high-priority missions) requires additional review rigor and independent verification/validation.
* When software is relied upon for critical systems, such as payload navigation or human-rated operations, the downstream impacts of waivers can have catastrophic consequences if not properly analyzed.

##### **Application**:

Projects involving **Class A or B software** should subject deviation requests to additional layers of scrutiny, particularly when the deviation involves integration risks or areas critical to mission success. Independent review by systems engineers and SMEs is highly recommended before approval.

---

#### **Lesson 4: Proactive Organizational Processes—Technical Authority Insights from Constellation Program**

**Source**: **NASA LLIS - Constellation Program**  
**Summary**: The Constellation Program identified significant benefits of having early and sustained interaction with the Technical Authorities, preparing for tailoring discussions, deviation requests, and hazard analysis well before critical design or operational deadlines.

##### **Relevance to Waivers/Deviations**:

* Early engagement with TAs reduces delays in securing approvals for deviations/waivers and facilitates alignment between project teams, engineering, and safety stakeholders.
* Establishing clear timelines and processes for tailoring ensures relief requests are processed in the context of evolving project designs.

##### **Application**:

Small projects should include **early planning for tailoring, deviation, and waiver reviews** when developing project schedules, ensuring TAs (ETA, SMA, others) are collaborative partners from the planning stage through final decisions.

---

### **Closing Summary**

Through lessons like those drawn from the Columbia Accident Investigation Board, Mars Climate Orbiter, and NASA risk management strategies, it is clear that rigorous processes and independent oversight for waivers and deviations are necessary for project success. Using systematic approaches—grounded in risk analysis, clear documentation, and lifecycle-wide traceability—small and large projects can balance the need for flexibility with the assurance of meeting NASA’s safety and mission goals. For projects seeking relief from NPR 7150.2 requirements, the lessons learned provide valuable guidance to strengthen decision-making and foster accountability.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

### **Objective of the Guidance**

The purpose of this requirement is to ensure the proper evaluation, tailoring, and documentation of project-specific software requirements in compliance with the directive, including assessment of software classifications and cybersecurity. It also establishes procedures for ensuring risks and mitigations related to tailored requirements are acceptable before approval is granted.

**Software Assurance (SA)** personnel must verify that all requirements mapping matrices and associated tailoring processes are handled in a compliant, consistent, and traceable manner. This includes accuracy in software classification, justification for tailoring, cybersecurity inclusion, and proper archiving.

---

### **Software Assurance Responsibilities**

---

#### **1. Verify Software Classification Accuracy**

1. **Review Software Classification**

   * Verify that the project has appropriately classified its software components according to the definitions in **Appendix D** of the directive. Common classifications (e.g., Class A, B, C, etc.) are tied to software’s criticality, purpose, and impact on safety, mission, or operations.
2. **Assess Classification Logic**

   * Confirm that the classification aligns with project goals and the associated risks.
   * Provide feedback if discrepancies exist or if reclassification is necessary.
3. **Document Findings**

   * Ensure classification validation is documented, with any corrections approved by the Technical Authority.

---

#### **2. Review and Evaluate the Requirements Mapping Matrix (RMM)**

1. **Evaluate Completeness and Accuracy**

   * Ensure the project’s **Requirements Mapping Matrix (RMM)** includes all requirements applicable to the project (per the directive).
2. **Check Consistency Against Software Classification**

   * Verify that the project’s commitments align with the classification of each software component. For example, all “X” (mandatory) requirements from **Appendix C** must be addressed or justified.
3. **Examine Marked ‘Not-Applicable’ Requirements**

   * Confirm that any requirements marked “Not-Applicable” in the RMM:
     + Are genuinely not relevant or cannot reasonably be applied to the project.
     + Have appropriate justifications that are clear, accurate, and consistent.
4. **Assess Tailoring Rationale**

   * Evaluate the rationale provided for requirements marked for tailoring based on risks, mitigations, and project-specific needs.
   * Identify any tailoring that does not include adequate justification or support and collaborate with the Technical Authority to address gaps.

---

#### **3. Verify and Assess Risk and Relief Requests**

1. **Evaluate Risks and Mitigations for Relief Requests**

   * Assess the project’s identified risks, mitigations, and justification for any request for relief from “X” requirements in Appendix C.
   * Ensure proposed mitigations sufficiently address potential risks associated with waiving or tailoring specific requirements.
2. **Ensure Relief Requests are Reasonable**

   * Collaborate with the Technical Authorities to determine whether risks and requests for tailoring are acceptable based on industry and agency best practices.
3. **Support Approval Processes**

   * Verify that requests for relief are processed efficiently and approvals/disapprovals are officially documented.

---

#### **4. Ensure Cybersecurity Inclusion**

1. **Involve the SAISO in Software Reviews**

   * Verify that the **Senior Agency Information Security Officer (SAISO)** or their delegate is included in all software reviews.
   * Confirm that cybersecurity considerations are integrated into:
     + Software development.
     + Verification and validation (V&V).
     + Maintenance, operations, retirement, and management.
2. **Review Cybersecurity Provisions**

   * Ensure the RMM includes cybersecurity requirements that address software vulnerabilities, safeguards, and data protection mechanisms.
3. **Track Cybersecurity Risks**

   * Verify that any cybersecurity risks, along with proposed mitigation strategies, are documented, approved, and tracked throughout the software lifecycle.

---

#### **5. Facilitate Archiving and Traceability**

1. **Archive Approved Requirements Mapping Matrices**

   * Ensure that all approved RMMs, including tailoring justifications and approvals, are stored in the project’s official records repository.
2. **Confirm Ease of Retrieval**

   * Verify that approved matrices are retrievable and properly organized for audits, reviews, and future reference.
3. **Establish Traceability**

   * Ensure the project’s RMM traceability clearly connects software requirements to their respective classifications, tailoring approvals, and risk mitigations.

---

#### **6. Verify Authority Approvals**

1. **Ensure Proper Technical Authority Approvals**

   * Confirm the designated **Technical Authority** has reviewed, approved (or disapproved), and signed the RMM for any tailored requirements.
2. **Signature Confirmation**

   * Check that all approvals are formally documented by obtaining Technical Authority signatures directly on the RMM.
3. **Address Any Missing Approvals**

   * Follow up on incomplete or missing approvals before finalizing the RMM.

---

### **Audit and Oversight**

1. **Conduct Periodic Audits of RMMs**

   * Regularly review project RMMs to ensure compliance with the directive, appropriate documentation of tailoring, and adequate cybersecurity inclusion.
2. **Identify and Report Gaps**

   * Provide feedback to the project and Technical Authority on any inconsistencies or gaps within the RMM.
3. **Document and Track Findings**

   * Maintain records of findings, corrective actions, and outcomes of RMM reviews.

---

### **Provide Feedback and Process Improvements**

1. **Standardize the RMM Process**

   * Recommend templates and best practices for simplifying the creation, assessment, and approval of RMMs.
2. **Provide Tailoring Guidance**

   * Educate projects and Technical Authorities on tailoring procedures to minimize unnecessary risks while ensuring compliance with the directive.
3. **Promote Cybersecurity Awareness**

   * Advocate for consistent inclusion of the SAISO or cybersecurity experts in software assurance workflows.

---

### **Expected Outcomes**

1. **Accurate Classification**

   * All software components are accurately classified according to Appendix D.
2. **Compliant RMMs**

   * Projects develop RMMs that accurately reflect applicable requirements for their software classification, with proper rationale for tailoring or exclusions.
3. **Cybersecurity Assurance**

   * Cybersecurity requirements are incorporated into all phases of the software development lifecycle.
4. **Traceability and Documentation**

   * Approved RMMs and tailoring justifications are archived in retrievable project records.
5. **Approval Accountability**

   * Technical Authority approvals are recorded directly on the RMM with appropriate signatures.

---

### **Summary**

**Software Assurance (SA)** personnel are responsible for ensuring that project requirements mapping matrices (RMMs) and tailoring processes conform to the directive. This includes verifying software classification accuracy, assessing risks, evaluating tailoring justifications, and ensuring cybersecurity is addressed throughout the process. SA also ensures all approvals are formally documented and archived for traceability and compliance, while providing feedback and facilitating continuous improvement.
