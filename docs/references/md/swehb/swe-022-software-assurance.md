# SWE-022 - Software Assurance

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695407. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance

SWE-022 - Software Assurance

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695407)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695407&showCommentArea=true&showComments=true#addcomment)

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

3.6.1 The project manager shall plan and implement software assurance, software safety, and IV&V (if required) per NASA-STD-8739.8, Software Assurance and Software Safety Standard.

## 1.1 Notes

Software assurance activities occur throughout the life of the project. Some of the actual analyses and activities may be performed by engineering or the project. Software Assurance directions, requirements, and guidance can be found in the NASA-STD-8739.8.

## 1.2 History

Click here to view the history of this requirement: SWE-022 History

SWE-022 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.10 The project shall implement software assurance per NASA-STD-8739.8, NASA Software Assurance Standard. |
| Difference between A and B | Added requirement to plan SA |
| B | 3.6.1 The project manager shall plan and implement software assurance per NASA-STD-8739.8. |
| Difference between B and C | No change |
| C | 3.6.1 The project manager shall plan and implement software assurance per NASA-STD-8739.8. |
| Difference between C and D | Expanded coverage to include "software safety and IV&V". |
| D | 3.6.1 The project manager shall plan and implement software assurance, software safety, and IV&V (if required) per NASA-STD-8739.8, Software Assurance and Software Safety Standard. |

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
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |

# 2. Rationale

Software Assurance (SA), Software Safety, and Independent Verification and Validation (IV&V) activities provide a structured, systematic approach to ensuring that mission and system software is **safe, secure, reliable, and performs as intended**. These processes mitigate software-related risks by proactively addressing vulnerabilities, hazards, and defects throughout the software life cycle—from requirements definition to design, implementation, testing, and maintenance. By adhering to NASA-STD-8739.8, these activities ensure compliance with NASA’s established standards, strengthen mission success, and prioritize both human safety and system reliability.

NASA missions rely on increasingly complex software systems, often embedded in safety-critical environments, such as spacecraft control systems, propulsion safety mechanisms, and mission data processing pipelines. Software assurance and software safety activities protect against two key risks:

1. **Designed or Accidental Vulnerabilities:** Ensuring that malicious or unintentional flaws do not compromise performance, safety, or security.
2. **Functional Reliability:** Guaranteeing that the software performs its intended functions under nominal and off-nominal conditions and avoids erroneous or unintended behaviors.

Through planned and systematic activities outlined in NASA-STD-8739.8, software assurance ensures **conformance**, while IV&V (when required) provides **independent oversight** to affirm that the mission objectives are met rigorously. These assurance processes create a **robust confidence framework** for software systems critical to NASA's mission success.

---

### **Purpose and Objectives of Software Assurance and Software Safety**

The primary purpose of software assurance and software safety is to ensure that:

1. **Software Vulnerabilities**: Systems are free from vulnerabilities—whether maliciously introduced or unintentionally added during development or maintenance.
2. **Intended Functionality**: The software performs its intended functions correctly and consistently.
3. **Unintended Functionality**: The software does not exhibit unintended or erroneous behavior that could jeopardize the mission or pose safety risks.

**Detailed Objectives of Software Assurance and Software Safety Activities:**

1. **Conformance to Requirements and Standards**:  
   Ensuring that the processes, procedures, and products used in developing or sustaining software conform to all specified requirements and standards governing those activities.
2. **Process Evaluation**:  
   Assessing the adequacy of software development and maintenance processes to verify adherence to best practices that ensure quality, compliance, and safety.
3. **Confidence in Processes and Products**:  
   Defining and assessing processes to establish evidence that the software:

   * Meets quality standards suitable for its intended purposes.
   * Produces outputs (software products) consistent with requirements and mission objectives.
4. **Software Quality Determination**:  
   Measuring and evaluating the degree of quality achieved by the software, ensuring it meets safety-critical and mission-critical performance levels.
5. **Safety Assurance**:  
   Ensuring that the software systems are safe by verifying compliance with safety-critical requirements and identifying/mitigating risks that could lead to hazardous software behavior.
6. **System Security**:  
   Ensuring that the software systems are secure by addressing cybersecurity risks at each stage of the software development life cycle.

---

### **Importance of Adhering to NASA-STD-8739.8**

The planning and implementation of software assurance, software safety, and IV&V (when applicable) in accordance with **NASA-STD-8739.8** ensure that software-related risks are systematically identified, mitigated, and managed. Compliance with this standard provides the project manager with a framework for guiding assurance activities and maintaining accountability. This adherence is critical for the following key areas:

#### **1. Mission Success**

Software assurance directly supports mission objectives by ensuring that:

* Mission software performs reliably and fulfills its specified requirements even under extreme conditions and stress scenarios.
* High-consequence systems (e.g., launch sequencing software, automated abort systems) exhibit robust fault tolerance and failure recovery mechanisms.

**Why It Matters:**  
Failures in software systems can result in catastrophic mission consequences and significant financial losses. For example, the Mars Climate Orbiter loss demonstrates the importance of verification and validation processes to prevent undetected defects.

---

#### **2. Safety Assurance**

Software safety activities focus on preserving human safety, protecting physical systems, and preventing accidents or system failures caused by software hazards. This includes:

* Identifying safety-critical requirements early in the development cycle.
* Implementing hazard analysis, redundancy mechanisms, and fail-safe designs in line with NASA safety standards.
* Verifying compliance through assurance activities to prevent catastrophic consequences (e.g., unintended software-triggered detonations).

**Why It Matters:**  
In crewed missions, such as Artemis and the International Space Station, software failures can result in loss of life or critical mission assets. Safety assurance mitigates risks to ensure human and equipment safety under all mission conditions.

---

#### **3. Regulatory Compliance**

Adhering to NASA-STD-8739.8 ensures conformance to NASA's rigorous standards for software safety and quality. This compliance:

* Establishes accountability and consistency across all projects, ensuring software products meet agency-wide expectations.
* Prevents inconsistencies in processes and practices that could lead to non-conformance and mission risks.

**Why It Matters:**  
Using standardized practices across NASA projects allows teams to continuously apply lessons learned from prior missions, driving improvement in software assurance practices while reducing risks.

---

#### **4. Risk Reduction**

Software assurance and IV&V activities strengthen risk reduction strategies by:

* Identifying and resolving defects early in the software life cycle, reducing costs and schedule risks.
* Providing independent analysis of software systems through IV&V, detecting risks that may go unnoticed by the development team.
* Mitigating risks in both development and operational phases, ensuring long-term reliability and maintainability of software systems.

**Why It Matters:**  
Unaddressed software risks have the potential to escalate into mission jeopardizing events, as shown by past failures such as the Ariane 5 explosion due to programming errors.

---

### **Role of IV&V in Enhancing Confidence**

Independent Verification and Validation (IV&V) serves as a critical complement to software assurance and safety activities by providing a high level of confidence in software quality and functionality. The independent nature of IV&V ensures:

1. **Unbiased Evaluation**: Teams conducting IV&V have no vested interest in the software development outcomes, ensuring thorough assessments without project pressures.
2. **Detection of Overlooked Risks**: IV&V identifies risks, defects, and vulnerabilities that may be missed during regular assurance activities, offering critical insights into system performance and issues.
3. **Safety-Critical System Focus**: IV&V is particularly valuable for safety-critical systems, verifying that all mission dependencies and constraints are met.

---

### **Conclusion**

**Summary of Rationale:** Software assurance, software safety, and IV&V activities are indispensable for ensuring NASA's mission software meets its intended goals. These activities provide confidence that software systems:

* Perform reliably under all mission conditions.
* Satisfy safety-critical and security-critical requirements.
* Adhere to NASA’s standards for quality, safety, and regulatory compliance.

**Benefits of Implementation Per NASA-STD-8739.8:**

* **Mission Reliability:** Reduced risk of mission-critical failures through robust assurance processes.
* **Safety Protection:** Secured safety for both personnel and equipment in space and ground operations.
* **Quality Control:** Consistent adherence to NASA’s directives for software safety and assurance.
* **Risk Mitigation:** Comprehensive risk identification and resolution across the software life cycle.

By planning and implementing these activities systematically, project managers promote mission success and deliver confidence in the safety, security, and reliability of software systems integral to NASA’s high-stakes missions.

# 3. Guidance

**SWE-022 - Software Assurance**

3.6.1 The project manager shall plan and implement software assurance, software safety, and IV&V (if required) per NASA-STD-8739.8, Software Assurance and Software Safety Standard.

This requirement ensures that NASA projects apply a systematic and consistent approach to **software assurance (SA)**, **software safety**, and **Independent Verification and Validation (IV&V)** (if required) using **NASA-STD-8739.8** as the governing standard. This requirement applies to all NASA software created, acquired, or maintained, and ensures confidence in the software’s safety, security, quality, and reliability across its life cycle.

This requirement mandates the systematic planning and implementation of **software assurance**, **software safety**, and **IV&V** in accordance with **NASA-STD-8739.8**. Projects must:

1. Develop a clear **Software Assurance Plan (SAP)** tailored to the software classification and scope.
2. Implement SA activities proportionally based on classification and risk profile.
3. Conduct regular audits and reviews to verify compliance and resolve deficiencies.
4. Track metrics to measure effectiveness and drive improvement.

By following this systematic approach, projects can ensure software meets NASA’s safety, reliability, and mission-critical standards while minimizing risks.

## 3.1 Purpose: Why Software Assurance is Mandatory

* **Risk Mitigation**: Software assurance helps identify and mitigate risks early by exposing potential defects in software products and processes.
* **Safety and Security**: Ensures that safety-critical functions are implemented correctly, and software vulnerabilities are minimized.
* **Improvement and Lessons Learned**: Metrics, tracking, and analysis activities drive continuous improvement in future projects.

## 3.2 Objectives of Software Assurance

Software assurance provides confidence that the following objectives are achieved for all software projects:

1. **Compliance**: Processes, products, and procedures conform to specified requirements, standards, and regulations.
2. **Safety**: Safety-critical system requirements and processes are implemented and verified.
3. **Security**: Software is free from vulnerabilities that could compromise mission success.
4. **Reliability**: The software functions as intended and avoids unintended behaviors or failures.

## 3.3 Context and Tailoring

### 3.3.1 Software Classification

* Software assurance activities must align with the software classification level defined in **NPR 7150.2** (Appendix D). Use the classification to scale software assurance activities proportionately:
  + **Class A** (Highest safety and mission-criticality): Full SA, software safety, and IV&V rigor required.
  + **Class D/E** (Lower risk/scope): Tailored SA and minimal IV&V or safety activities.

### 3.3.2 Tailoring

* Tailor SA activities in coordination with Safety and Mission Assurance (SMA) personnel to suit project size, complexity, and risk profile.
  + Example: Lighter reviews for Class D software vs. full lifecycle IV&V for Class A.
* Document all tailoring decisions within the **Software Assurance Plan (SAP)**, including rationale and risk acceptance approvals by the project manager and SMA technical authority.

## 3.4 Responsibilities

### 3.4.1 Project Manager Responsibilities

The project manager is responsible for:

1. **Planning**:
   * Establish the Software Assurance Plan (SAP) per NASA-STD-8739.8, defining SA, software safety, and IV&V activities based on the software classification and scope.
   * Ensure software assurance tasks are clearly integrated into the lifecycle (requirements, design, implementation, testing, operations, maintenance, and retirement).
2. **Resource Allocation**:
   * Provide skilled personnel, tools, facilities, and budget to enable successful execution of SA, safety, and IV&V tasks.
3. **Action on Findings**:
   * Act on issues, risks, and recommendations identified during audits or reviews to resolve non-conformances promptly.

### 3.4.2 SMA and Software Assurance Team Responsibilities

The SMA and SA teams assist the project manager in:

1. **Performing SA Activities**:
   * Execute the planned SA, software safety, and IV&V activities and document progress.
   * Minimize duplication by coordinating efforts with related disciplines, such as system safety, hardware reliability, and software engineering.
2. **Delivering Reports**:
   * Provide actionable findings from audits, reviews, and metrics to project management.
3. **Tracking Metrics**:
   * Log key metrics (e.g., defect rates, testing coverage) to measure SA and software safety effectiveness.

## 3.5 Practical Steps for Implementation

### Step 1: Develop the Software Assurance Plan (SAP)

* Collaborate with SMA personnel to develop the **SAP** based on NASA-STD-8739.8. For small or medium projects, this plan can be simplified but must include:
  + Description of SA activities across the lifecycle.
  + Software classification and tailoring decisions.
  + Safety-critical software tasks for hazard analysis, fault detection, and recovery.
  + Metrics for tracking software assurance performance (e.g., non-conformance trends).

### Step 2: Implement Software Assurance Processes

* **Requirements Phase**:
  + Validate requirements for completeness, traceability, and alignment with mission objectives.
  + Identify safety-critical requirements.
* **Design Phase**:
  + Review design for compliance with approved requirements and standards.
  + Include fail-safe mechanisms for safety-critical functions.
* **Implementation Phase**:
  + Enforce adherence to coding standards (e.g., MISRA, NASA coding rules).
  + Perform static/dynamic code analysis to identify weaknesses (e.g., memory leaks, race conditions).
* **Testing Phase**:
  + Ensure tests cover all functional and safety-critical requirements.
  + Log test results and defects in audit-ready documentation.
* **Operational Phase**:
  + Track issues and corrective actions to closure for ongoing software assurance.

### Step 3: Conduct Audits and Reviews

* **Frequency**:
  + Implement planned software audits at least **once per lifecycle milestone** or **biennially** for long-term projects.
* **Scope**:
  + Verify SA and software safety activities meet NASA-STD-8739.8 requirements.
  + Confirm deliverables (e.g., requirement traceability matrix, test results, risk mitigations) are complete and accurate.
* **Corrective Actions**:
  + Track non-conformances and ensure timely resolution to prevent delays or failures.

### Step 4: Monitor Metrics and Outcomes

* Use simple metrics to track progress and identify improvement areas. Examples:
  + Defect rates and corrective actions.
  + Software safety issues tracked to closure.
  + Requirements coverage achieved during testing.

### Step 5: Tailoring and Risk Acceptance

* Obtain SMA technical authority approval for all tailoring decisions and ensure the project manager formally accepts any risks associated with tailored requirements.
* Maintain documentation of tailoring rationale and associated risks for audit purposes.

## 3.6 Collaborative Approach

Effective software assurance requires collaboration between the **project team**, SMA personnel, and software engineers. To ensure SA activities are consistent and meaningful:

1. **Communication**:
   * Establish regular communication paths between engineering, SMA, and project management to coordinate SA tasks, reviews, and metrics.
2. **Alignment**:
   * Align SA metrics with broader project performance goals to track and manage risks in real time.
3. **Tools**:
   * Provide access to SA checklists, templates, and documented procedures to ensure consistent execution of tasks.

## 3.7 Metrics

* **Examples of Useful Metrics**:
  + Number of deficiencies identified during requirements, design, and testing phases.
  + Percentage of test coverage for safety-critical functions.
  + Trends in defect rates across lifecycle phases.

This refined guidance simplifies the implementation process and organizes it in clear, actionable steps, making it accessible for projects of varying complexity and scale.

See also Topic [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report),

See also [SWE-045 - Project Participation in Audits](/spaces/SWEHBVD/pages/102695419/SWE-045+-+Project+Participation+in+Audits),

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-045 - Project Participation in Audits](/spaces/SWEHBVD/pages/102695419/SWE-045+-+Project+Participation+in+Audits)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Software Quality Assurance](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Software+Quality+Assurance) |

# 4. Small Projects

Software assurance is required regardless of project size. Since NASA-STD-8739.8 [278](#_tabs-<p></p>) defines roles, not individuals, projects with limited personnel resources, can use one person to fulfill multiple roles and perform multiple software assurance functions, as long as the proper independence for the specific requirement is maintained. In small project situations, sometimes it will be necessary for a project to have software assurance conducted by someone not on the project, but potentially from the same organization. This is not the preferred approach, but better than having no software assurance done at all.

Additionally, for acquired software, software assurance is performed by both the acquirer and the provider, so projects with small acquirer staff could consider doing more "insight" (Surveillance mode requiring the monitoring of customer identified metrics and contracted milestones) per NASA-STD-8739.8, "Tailoring the implementation of software assurance requirements is acceptable commensurate with the program/project classification as well as size, complexity, criticality, and risk."

For small projects, the **project manager** must ensure that:

1. A **Software Assurance Plan** is created and fully implemented.
2. Key metrics are tracked throughout software development.
3. Periodic audits verify compliance and detect risks early.
4. Tailoring is justified, documented, and approved, ensuring acceptable risk posture.

By scaling down processes while maintaining compliance with **NASA-STD-8739.8**, small projects can achieve proper software assurance without being overwhelmed.

This guidance consolidates the requirement into manageable actions for small projects while maintaining alignment with NASA's standards.

The requirement states that "The project manager shall plan and implement software assurance, software safety, and IV&V (if required) per NASA-STD-8739.8, Software Assurance and Software Safety Standard."

To simplify and clarify this requirement for **small projects**, the following step-by-step guidance is provided, aligned with the requirements of **NASA-STD-8739.8** and tailored for smaller scale efforts:

### Step 1: Define the Plan

**Objective:** Lay out a simple and actionable plan for software assurance (SA), software safety, and Independent Verification & Validation (IV&V) (if required) based on the project’s software classification and scope.

#### Actions:

1. **Determine Software Classification**:

   * Refer to **NPR 7150.2, Appendix D** to classify your software (Class A–E, or Safety Critical).
   * For small projects, the classification typically falls in Class C-D (non-mission critical) with minimal IV&V requirements unless the software is safety-critical.
2. **Draft a Software Assurance Plan (SAP)**:

   * Create a short, tailored plan that defines:
     + Key software assurance activities.
     + Safety-critical software tasks (if applicable).
     + Metrics to monitor progress.
     + Deliverables (audit reports, risk assessments, etc.).
     + Roles and responsibilities of personnel (SA point-of-contact).
   * For small projects, this plan can be lightweight but should address all life-cycle phases (requirements, design, implementation, testing, operations, and maintenance).
3. **Decide on IV&V Applicability**:

   * Confirm with relevant **Safety and Mission Assurance (SMA)** personnel whether IV&V is required for your software.
   * If IV&V is not required, document this decision within the SAP and focus on internal assurance and safety checks.

### Step 2: Implement Software Assurance Activities

**Objective:** Ensure that software assurance processes are integrated into the software lifecycle using NASA-STD-8739.8 as a guide.

#### Actions:

1. **Follow Software Assurance Processes**:

   * Perform the following activities across the lifecycle:
     + **Requirements phase**: Validate requirements for correctness, completeness, and traceability to system objectives.
     + **Design phase**: Review designs for alignment with requirements and safety-critical considerations.
     + **Implementation phase**:
       - Conduct code reviews for adherence to coding standards (ensure MISRA or NASA-specific coding rules compliance).
       - Use static analysis tools to identify errors early.
     + **Testing phase**: Ensure:
       - All requirements are verified via test cases.
       - Adequate test coverage (e.g., 100% functional requirements and >90% line coverage).
       - Safety-critical conditions (failure modes, boundary cases) are tested.
     + **Operations/Maintenance phase**: Track issues, perform risk assessments, and monitor corrective actions.
2. **Address Software Safety**:

   * Identify and mitigate software hazards through techniques like **Fault Tree Analysis (FTA)** or **Failure Modes and Effects Analysis (FMEA)**.
   * Ensure safety-critical software includes:
     + Fault detection, isolation, and recovery (FDIR) mechanisms.
     + Fail-safe operations for unpredictable conditions.
3. **Simplify Metrics Tracking**:

   * For small projects, focus on tracking key metrics:
     + Number of non-conformances and corrective actions.
     + Code coverage during testing (e.g., functional, branch coverage).
     + Results of safety analyses.
4. **Tailoring Assurance Activities**:

   * For small projects, **tailor assurance activities** to reduce unnecessary complexity while maintaining compliance. Examples:
     + Downscale the depth of design reviews for non-critical subsystems.
     + Use automated tools to streamline code reviews and static analysis.
     + Consolidate audits into milestone-based reviews instead of frequent checkpoints.

### Step 3: Conduct Audits and Reviews

**Objective:** Verify compliance with software assurance and safety requirements.

#### Actions:

1. **Periodic Internal Audit**:

   * Conduct lightweight audits using checklists derived from **NASA-STD-8739.8** to ensure:
     + Requirements are properly implemented and verified.
     + Risks are being tracked and mitigated effectively.
     + Corrective actions for deficiencies are implemented.
2. **Documentation Deliverables**:

   * Maintain the following evidence as part of the audit:
     + Requirements traceability matrix (RTM).
     + Risk register for tracking safety concerns.
     + Test and verification results, especially for critical systems.
     + Records of issues and their resolutions.
3. **Collaborate with SMA**:

   * Share audit findings with SMA and engineering leadership.
   * SMA personnel can assist in confirming compliance or suggesting improvements to assurance activities.

### Step 4: Manage Tailoring

**Objective:** Ensure risk-based tailoring is applied to meet project objectives without compromising safety or reliability.

#### Actions:

1. **Understand Tailoring Exceptions**:

   * Consult **NASA-STD-8739.8 and NPR 8715.3** for allowances regarding tailoring of requirements.
   * Tailoring is acceptable for small projects where justified by:
     + Low software complexity.
     + Minimal safety risk.
     + Size or resource constraints.
2. **Obtain Approval**:

   * Request approval for any tailored requirements or exemptions via:
     + Defined processes in the **Requirements Mapping Matrix**.
     + SMA Technical Authority and project manager concurrence.
   * Provide clear documentation of:
     + Rationale for tailoring.
     + Risk assessment of tailored requirements.

### Step 5: Monitor Corrective Actions

**Objective:** Track and resolve software assurance issues to closure.

#### Actions:

1. **Log Issues and Actions**:

   * Track non-conformances identified through audits, reviews, or testing.
   * Record corrective actions against their associated risks.
2. **Verify Closure**:

   * Confirm all issues have been resolved effectively and documented.
   * Use safety and mission assurance reviews to sign off on updates before proceeding to the next lifecycle phase.

## 4.1 Essential Deliverables for Small Projects

1. **Software Classification Documentation** (per NPR 7150.2).
2. **Software Assurance Plan (SAP)**.
3. **Requirements Mapping Matrix** (indicating compliance and tailoring decisions).
4. **Audit Reports** (results and corrective actions tracked for closure).
5. **Safety Analysis Documentation** (if software is classified as safety-critical).
6. **Risk Register** to manage and mitigate software risks.

## 4.2 Periodic Tools and Techniques for Small Projects

* **Lightweight Code Reviews and Static Analysis**:
  + Tools like **Clang Static Analyzer**, **SonarQube**, or **Coverity**.
* **Automated Testing Frameworks**:
  + Use tools like **JUnit**, **Pytest**, or **CI/CD pipelines** to save time and ensure quality.
* **Simplified Risk and Safety Analysis**:
  + Focus on higher-level approaches like checklist assessments for hazards.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-033)

  [STEP Level 2 NASA Basics of Software Assurance for Practitioners course,](https://saterninfo.nasa.gov/ "Click to open in new window")

  SMA-SA-WBT-100 SATERN. System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
   User needs account to access SATERN courses. This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-050)

  [STEP Level 2 NASA Software Auditor Skills course,](https://satern.nasa.gov/ "Click to open in new window")

  SMA-SA-WBT-203 SATERN. System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
   User needs account to access SATERN courses. This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
* (SWEREF-055)

  [STEP Level 3 NASA Software Assurance Planning and Management course,](https://satern.nasa.gov/ "Click to open in new window")

  SMA-SA-WBT-320 SATERN. System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
   User needs account to access SATERN courses. This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://satern.nasa.gov/.
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-270)

  [NASA Office of Safety and Mission Assurance (OSMA) (2011, February 17).](https://sma.nasa.gov/home "Click to open in new window")

  OSMA Website
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-433)

  [Lessons Learned in Software Quality Assurance.](https://link.springer.com/chapter/10.1007/978-3-662-05129-0_12 "Click to open in new window")

  Rosenberg, Dr. Linda H. NASA Goddard Space Flight Center (GSFC). In Journal of Software Technology, Vol. 6, Number 2. October, 2003. Lessons Learned Reference.
* (SWEREF-444)

  [Lessons Learned in Software Quality Assurance](http://www.eng.auburn.edu/~kchang/comp6710/readings/lessons.learned.in.SQA.htm "Click to open in new window")

  Rosenberg, Linda H. (Oct, 2003). Journal of Software Technology.
* (SWEREF-468)

  [NASA’s Approach to Software Assurance,](http://www.crosstalkonline.org/storage/flipbooks/2015/201509/index.html "Click to open in new window")

  Wetherholt, Martha. CrossTalk - Journal of Defense Software Engineering, Sep/Oct, 2015. Retrieved October 08, 2015 from http://www.crosstalkonline.org/storage/flipbooks/2015/201509/index.html. See page 31.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA lessons learned associated with the requirement to plan and implement **software assurance (SA)**, **software safety**, and **Independent Verification and Validation (IV&V)** per NASA-STD-8739.8. These lessons emphasize the importance of proactive assurance and safety practices throughout the software development lifecycle to prevent costly and, in some cases, catastrophic failures during critical missions. Below is a consolidation of relevant NASA lessons learned that align with **Requirement 3.6.1**:

### **Relevant NASA Lessons Learned**

#### **1. Lesson ID: 0330 – Mars Climate Orbiter Loss**

**Summary:**  
The Mars Climate Orbiter was lost in 1999 due to a mismatch in units (imperial vs. metric) in the spacecraft's software, which caused it to enter an incorrect orbital trajectory. The failure was directly linked to inadequate software assurance during the development process.

**Relevance to 3.6.1:**

* This failure highlighted the critical need for robust **software assurance and IV&V** to identify and resolve such discrepancies before launch.
* Assurance and safety processes should include thorough requirements validation, interface verification, and testing for data consistency.

**Lesson Learned:**

* Ensure comprehensive software assurance activities, including independent requirements verification and validation of interfaces, as part of the project planning and implementation process.

#### **2. Lesson ID: 0792 – Mars Polar Lander Loss**

**Summary:**  
The Mars Polar Lander was lost during its descent in 1999 due to premature shutdown of descent engines, caused by software misinterpreting noise generated by landing leg sensors. This error was tied to insufficient software assurance and incomplete hazard analyses.

**Relevance to 3.6.1:**

* Lack of a fully implemented **software safety program** contributed to untested failure scenarios, where the software did not account for sensor noise during critical mission phases.
* Independent verification could have helped identify this oversight.

**Lesson Learned:**

* Fully implement **software safety** processes, including fault-tree analyses and testing of all hazardous conditions.
* Plan IV&V for complex or high-risk systems to independently validate critical components and failure scenarios.

#### **3. Lesson ID: 1281 – OrbView-3 Satellite Power System Failure**

**Summary:**  
The OrbView-3 satellite experienced a mission-ending failure due to a combination of hardware and software issues. Insufficient software assurance during testing allowed defects in safety-critical software to go undetected.

**Relevance to 3.6.1:**

* Software assurance processes, such as static analysis, independent reviews, and unit-level test coverage, were insufficiently implemented.
* A robust assurance plan, following NASA-STD-8739.8, would have required better risk mitigation during the planning phase.

**Lesson Learned:**

* Early and comprehensive **software assurance and IV&V planning** should be established to identify latent software risks and defects, particularly in safety-critical systems.

#### **4. Lesson ID: 0732 – Galileo Spacecraft Antenna Deployment Failure**

**Summary:**  
The Galileo spacecraft experienced a failure to fully deploy its high-gain antenna due to unanticipated on-orbit conditions. Software assurance efforts failed to identify software issues related to on-orbit deployment scenarios.

**Relevance to 3.6.1:**

* Robust assurance and hazard analysis planning during development could have uncovered untested deployment scenarios.
* Both software testing and IV&V activities should validate the software's ability to handle critical failure scenarios.

**Lesson Learned:**

* Ensure **software hazard analysis and safety planning** address on-orbit anomalies and scenarios.
* Allocate sufficient time and resources for IV&V or independent assessments of safety-critical software functions.

#### **5. Lesson ID: 0371 – Software Oversight in the Ares I-X Flight Test Development**

**Summary:**  
During the Ares I-X flight test in 2009, software oversight was noted as a key challenge. Insufficient independent review and late risk mitigation delayed detection of software integration issues that could have impacted mission outcomes.

**Relevance to 3.6.1:**

* This lesson underscores the importance of **planning independent software oversight**, such as IV&V, early in the project lifecycle for complex systems. IV&V would have helped uncover risks earlier.

**Lesson Learned:**

* Proactive IV&V involvement during the development lifecycle ensures early identification of software integration issues. Planning assurance and IV&V from project inception reduces risk in complex projects.

#### **6. General Observation: Lack of Formal Software Assurance Planning**

**Summary:**  
Several NASA projects have identified software assurance lapses caused by improper or incomplete planning during the early stages of development. This includes overlooking critical components or failing to implement tailored assurance processes for safety-critical systems.

**Relevance to 3.6.1:**

* NASA-STD-8739.8 emphasizes creating and implementing a formal software assurance and safety plan that accounts for complexity and project-specific risks.
* Case studies show that failure to integrate assurance into project planning results in post-launch defects, mission delays, or failures.

**Lesson Learned:**

* Explicitly plan and implement **software assurance** activities tailored to project risks, addressing critical safety and reliability requirements.

### **Why NASA-STD-8739.8 is Critical**

The failures cited above demonstrate the importance of adhering to **NASA-STD-8739.8**, which provides a standardized framework for software assurance and software safety. This requirement ensures that:

1. **Hazard Analyses**:
   * Potential software issues are identified and mitigated before deployment.
2. **Requirements and Interface Validation**:
   * All software aligns with mission and system requirements, reducing the likelihood of integration issues.
3. **Independent Verification & Validation (IV&V)**:
   * High-risk and high-complexity software is evaluated independently to uncover risks and defects that may be missed by development teams.

IV&V, if required, provides a second layer of confidence by ensuring that safety-critical software meets its intended purpose under all conditions, including edge cases.

### **Key Takeaways from NASA Lessons Learned**

1. **Early Planning is Essential**:

   * Software assurance, safety, and IV&V activities must be planned from the earliest stages of the project. Late integration of these activities increases costs and risks of mission failure.
2. **Tailor Assurance Activities to Safety-Critical Functions**:

   * Not all software requires the same level of assurance or IV&V. Focus efforts on components with the greatest safety impact or complexity.
3. **Hazard Analysis and Safety Integration**:

   * Undetected hazardous scenarios in software (e.g., sensor noise, invalid inputs, untested interface conditions) frequently contribute to failures. Incorporate hazard analyses to address these risks comprehensively.
4. **Independent Reviews and IV&V**:

   * Independent assessments, when planned and executed appropriately, significantly enhance confidence in software quality, particularly for safety-critical systems.
5. **NASA-STD-8739.8 Compliance**:

   * Following the processes in this standard ensures comprehensive and consistent assurance practices, reducing risks at every stage of the lifecycle.

### **Conclusion**

NASA's lessons reinforce the criticality of Requirement 3.6.1: planning and implementing **software assurance, safety, and IV&V** for safety-critical systems. By incorporating the guidance of **NASA-STD-8739.8**, project managers can ensure proper oversight and risk mitigation, leading to safer, more reliable mission outcomes.

For further exploration:

* Consult the NASA Lessons Learned database (<https://llis.nasa.gov/>).
* Review NASA-STD-8739.8 for detailed directives regarding assurance implementation.
* Use NPR 7150.2 as a complementary reference for software engineering practices tied to assurance and IV&V activities.

### 6.2 Other Lessons Learned

* **Software quality assurance implementation is a balancing activity that must be tailored as project appropriate[444](#_tabs-<p></p>): (Lesson 2 of 12)**

Software Quality Assurance engineers must determine, based on experience, what trade-offs are to be made within the specific project since each project has different objectives. Gilles defined some of these relationships between the quality assurance criteria e.g., an inverse relationship between usability and efficiency; a direct relationship between maintainability and reusability 2. To make the best trade-offs, all relationships must be understood and experience used to interpret the impact."

* **Software quality assurance (SQA) must evaluate the process as well as the products[444](#_tabs-<p></p>): (Lesson 3 of 12)**

Within NASA, SA tends to focus on the products produced, such as the requirements documents, design, code listing, and test plans. But the focus of SA is to monitor continuously throughout the Software Development Life Cycle to ensure the quality of the delivered products. This requires monitoring both the processes and the products. In process assurance, SA provides management with objective feedback regarding compliance with approved plans, procedures, standards, and analyses. Product assurance activities focus on the changing level of product quality within each phase of the life cycle, such as the requirements, design, code, and test plan. The objective is to identify and eliminate defects throughout the life cycle as early as possible, thus reducing test and maintenance costs.

* **There must be a software assurance plan[444](#_tabs-<p></p>): (Lesson 4 of 12)**

The plan will specify the goals, what is to be performed, standards against which the development work is to be measured, all relevant procedures, and the organizational structure of the Quality Assurance within the project. 

* **Software quality assurance must span the entire software development life cycle[444](#_tabs-<p></p>): (Lesson 5 of 12)**

Software Development starts at the concept phase and continues through maintenance. SA activities and funding should also start at the concept definition and continue through the entire life cycle. At each phase, some activities could be performed 4. The project and the quality assurance office must work together to negotiate what activities are appropriate at each phase based on risks and resources. 

* **Requirements are the birthplace of successful projects[444](#_tabs-<p></p>): (Lesson 6 of 12)**

Although SA is performed across the entire life cycle, the success of a project can often be determined by the attention paid to requirements. The earlier in the life cycle potential risks are identified, the easier it is to eliminate or at least manage the conditions that introduce that risk. Problems not found until the testing phase are approximately 14 times more costly to fix than if found and fixed earlier in the requirements phase. The first tangible representation of the capabilities produced is the requirements specification document, be it system, hardware, software, or operational requirements. The document also serves to establish the basis for all the project's engineering management and assurance functions. If the quality of the requirements specification is poor, the project is at risk even before work begins.7 Therefore, a specific lesson in SA is the emphasis on requirements.

* **Software quality assurance does not equal testing[444](#_tabs-<p></p>): (Lesson 7 of 12)**

From the aspect of quality assurance, the purpose of testing is to:

* + - Assure problems are documented, corrected, and used for process improvement.
    - Assure problem reports are assessed for their validity.
    - Assure reported problems and their associated corrective actions are implemented following customer-approved solutions.
    - Provide feedback to the developer and the user on the problem status.
    - Provide data for measuring and predicting Software Quality and Software Reliability."

* **Metrics are a necessity[444](#_tabs-<p></p>): (Lesson 8 of 12)**

Software Metrics are often ignored during the early Software Development Life Cycle phases and are not actively associated with SA - but should be. For SA practitioners, with their responsibility for assuring both the processes and the products of the Software Development, measurement is critical. Throughout each of the life cycle phases metrics have proven invaluable in the evaluation of the quality of the products and processes.

* **Safety and reliability are critical aspects of SQA[444](#_tabs-<p></p>): (Lesson 9 of 12)**

Safety is a team effort and everyone's responsibility. Software within NASA is a vital part of the system and can impact the safety of the mission. Project managers, Systems Engineers, Software Leads and engineers, Software Assurance or Quality Assurance, and System Safety Personnel all play a part in creating a safe system. Reliability and safety cannot be tested at the end of a project; they must be built in as the software is being Developed.  
Reliability impacts safety - a system cannot be deemed safe if it is not reliable.

* **Independent verification and validation (IV&V) is an important tool within SQA[444](#_tabs-<p></p>): (Lesson 10 of 12)**

NASA defines Software IV&V as a Systems Engineering Process employing rigorous methodologies for evaluating the correctness and quality of the software product throughout the Software Development Life Cycle.  

* **Hardware does not equal software[444](#_tabs-<p></p>)! (Lesson 11 of 12)**

The influence of Hardware Quality Assurance is evident in the Software Quality Assurance practitioner community, where hardware-intensive systems and typical hardware-related concerns predominate. Two issues that dominate discussions about hardware are time and operating conditions. Software, however, is built with different constraints and considerations.

* **Risk Management is not optional[444](#_tabs-<p></p>): (Lesson 12 of 12)**

Risk is a daily reality in all projects, and Continuous Risk Management should become just as routine. It should be ongoing and comfortable and neither imposed nor forgotten. Like any good habit, it should seamlessly fit into daily work.

*Software Risk Management is important because it helps avoid disasters, rework, and overkill.* The objectives of Software Risk Management are to identify, address, and eliminate software risk items before they become threats to success or major sources of rework. Good project managers are also good managers of risk. It makes good business sense for all software development projects to incorporate risk management as part of project management.

# 7. Software Assurance

**SWE-022 - Software Assurance**

3.6.1 The project manager shall plan and implement software assurance, software safety, and IV&V (if required) per NASA-STD-8739.8, Software Assurance and Software Safety Standard.

This guidance is intended to ensure rigorous implementation of **NASA-STD-8739.8** and **NPR 7150.2** requirements throughout the software assurance lifecycle for NASA projects, with detailed steps for audits, process evaluations, tailoring requests, and metrics tracking.

This guidance outlines systematic software assurance activities, from planning and tailoring to audits and risk management. The goal is to ensure NASA projects achieve conformance, safety, and reliability expectations per **NASA-STD-8739.8** and **NPR 7150.2**, with robust processes for continuous improvement.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Perform software assurance, software safety, and IV&V (if required) according to the software assurance and software safety standard requirements in NASA-STD-8739.8, Software Assurance and Software Safety Standard, and the Project’s software assurance plan.

## 7.2 Software Assurance Products

**Objective:** Provide evidence that software assurance has been implemented effectively and in compliance with the requirements of **NASA-STD-8739.8**.

**Software Assurance and Software Safety (Key Items)**

1. **Software Requirements (quality and coverage)**
2. **Fault Tolerance**
3. **Code Quality**
4. **Following Good Software Processes and practices**
5. **Software Metric Data**

### 7.2.1 Key Products and Evidence

1. **Software Assurance Process Audit Report**:

   * Includes audit results on compliance against requirements defined in **NASA-STD-8739.8**, findings, and corrective action plans.
   * Focuses on verifying conformance to mandated standards, the completeness of audit processes, and resolution of gaps.

**2. References**:

* + See **Topic 8.59 - Audit Reports** for additional details on process audit methodologies.

## 7.3 Metrics

**Objective:** Track quantitative data to measure compliance and identify areas for improvement and early risk mitigation.

#### **Suggested Metrics**

1. **Non-Conformance Metrics**:

   * Number of non-conformances identified during audits, including findings from both process and compliance audits as well as assessments of process maturity.
   * Focus on identifying recurring patterns to improve corrective action efficiency.
2. **Lifecycle Phase Metrics**:

   * Number of software work product non-conformances identified by lifecycle phase (e.g., requirements, design, implementation, testing, and maintenance).
   * Trends over time to monitor improvements or degradation in conformance.
3. **References**:

   * Detailed metrics examples can be found in **Topic 8.18 - SA Suggested Metrics**.

## 7.4 Guidance

### Step 1: Develop Software Assurance Plans and Requirement Mapping

* Create a **Software Assurance Plan (SAP)** that aligns with:

  + Software classification per NPR 7150.2.
  + Requirements outlined in NASA-STD-8739.8.
  + Engineering requirements mapping matrix to identify specific methods to fulfill assurance requirements for the given software lifecycle.
* Include in the SAP:

  + Defined metrics for tracking compliance.
  + Roles and responsibilities of engineering, SMA, and IV&V organizations.

### Step 2: Conduct Software Assurance Audits

* **Audit Frequency**:

  + Perform an audit of the software assurance process at least every two years or upon request from the project office or technical authority.
  + Ensure compliance against the Software Assurance and Software Safety requirements defined in NASA-STD-8739.8.
* **Audit Scope**:

  + Verify adherence to software assurance processes and safety standards.
  + Ensure all mandated products (e.g., test reports, requirements matrices, risk assessments) have been developed, reviewed, and submitted.
  + Evaluate metrics provided to engineering and project management to identify compliance trends.

### Step 3: Monitor Issues and Track Corrective Actions

* **Monitor Findings**:

  + Continuously monitor issues and corrective actions identified during audits and routine reviews. Ensure closure of findings by verifying root cause analysis and resolution activities.
  + Assess risks associated with non-conformance, including impacts to safety, performance, mission objectives, or schedule.
* **Roles and Responsibilities**:

  + Engineering and SMA teams must collaborate to address corrective actions efficiently.
  + Monitor the progress and effectiveness of corrective actions during the project lifecycle.
* **Benefits**:

  + Periodic audits and daily status monitoring with engineering teams help establish a feedback loop for identifying unmet requirements and associated risks early.

### 7.4.1 Tailoring Requirements

Tailoring is the process of modifying requirements to balance program objectives, acceptable risks, and operational constraints. NASA established a clear Technical Authority governance model to approve and manage tailored requirements in **NASA-STD-8739.8**.

#### **Tailoring Levels**

1. **Software Classification Decision**:

   * First level tailoring occurs per NPR 7150.2.083, where system-specific classification determines applicable requirements.
2. **Software Requirements Mapping Matrix**:

   * Second level tailoring is applied in the project’s Software Requirements Mapping Matrix. This governs exceptions and adjustments to NPR 7150.2-based requirements.
3. **Software Assurance, Safety, and IV&V Requirements**:

   * Third level tailoring involves adjustments by the SMA Technical Authority based on project-specific needs and risks.

Tailoring decisions must:

* Be documented with clear rationale, risk evaluations, and references to supporting justification.
* Include concurrence from affected organizations such as safety, cybersecurity, quality, and technical teams.

### 7.4.2 Approval and Governance

* **Approval Authority**:

  + Center-level SMA Technical Authority reviews and approves all tailoring requests.
  + Requests must obtain formal acceptance of associated risks by program/project managers and relevant Technical Authorities.
* **Notification Responsibility**:

  + Organizations requesting tailoring must promptly inform the next higher level of management and all impacted teams and functions.

### 7.4.3 Risk Assessment and Plans

#### Comprehensive Risk Assessment

* Conduct risk assessments to determine the rigor of software assurance, safety, and IV&V tasks.
* Adjust plans accordingly to match software classification, organizational priorities, technical risk posture, and system complexity.

#### Adjustments for Evolving Classification

If software evolves to meet a higher or lower classification, organizations shall:

1. Update assurance plans to fulfill applicable requirements.
2. Modify contracts to align with the revised requirements mapping matrix and approved changes.

### 7.4.4 Periodic Audit and Reporting Flow

#### Audit Procedure

1. **Plan** and schedule audits at least biennially or upon request from technical authorities.
2. **Conduct Audits** to verify:
   * Adherence to requirements, processes, and procedures defined in the SAP.
   * Completion of mandated assurance products.
3. **Report Findings**:
   * Document results, highlighting non-conformances, risks, and corrective actions.

#### Monitor and Close Findings

* Track all findings to closure, ensuring risks are mitigated and corrective actions address root causes effectively.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-045 - Project Participation in Audits](/spaces/SWEHBVD/pages/102695419/SWE-045+-+Project+Participation+in+Audits)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

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

## 8.1 Objective Evidence:

Objective evidence is crucial for demonstrating that the requirement has been satisfied through planning, execution, and verification of software assurance, software safety, and IV&V activities as mandated by NASA-STD-8739.8. This evidence must be traceable, auditable, documented, and include both direct artifacts and analysis results.

---

### **Categories of Objective Evidence**

#### **1. Planning Artifacts**

Planning evidence ensures comprehensive software assurance and software safety processes are defined upfront and tailored appropriately for the mission.

1. **Software Assurance Plan (SAP):**

   * **Evidence:** A detailed SAP document outlining all assurance activities, tasks, schedules, tools, responsibilities, and compliance strategies mapped to NASA-STD-8739.8.
   * **Purpose:** Verifies that all assurance activities are planned, documented, and consistent with directives.
2. **Software Safety Plan:**

   * **Evidence:** A detailed safety plan articulating processes for identifying and mitigating software hazards, verifying safety-critical requirements, and auditing compliance.
   * **Purpose:** Confirms the implementation of software safety activities in alignment with NASA-STD-8739.8 standards.
3. **IV&V Implementation Plan (if applicable):**

   * **Evidence:** A dedicated plan documenting how Independent Verification and Validation (IV&V) will be integrated into the software assurance process, including scope, methodologies, and deliverables.
   * **Purpose:** Establishes IV&V as an independent activity with clear objectives (for safety-critical or mission-critical software).
4. **Requirements Mapping Documents:**

   * **Evidence:** A requirements traceability matrix mapping all software assurance and software safety requirements to corresponding activities, processes, and standards (NASA-STD-8739.8 and NPR 7150.2).
   * **Purpose:** Provides traceability for assurance requirements to their implementation, ensuring coverage of all necessary compliance elements.
5. **Risk Management Plan:**

   * **Evidence:** Documented risk management plan identifying potential software-related risks (e.g., safety hazards, vulnerabilities) and defining mitigation strategies.
   * **Purpose:** Demonstrates proactive planning for risk identification and resolution.

---

#### **2. Execution Artifacts**

Execution evidence reflects the actual implementation of planned software assurance, safety, and IV&V processes.

1. **Process Assessment Reports (Conformance Testing):**

   * **Evidence:** Reports from audits or assessments verifying that the software development and safety processes conform to NASA-STD-8739.8 standards.
   * **Purpose:** Confirms adherence to planned assurance activities.
2. **Software Safety Hazard Analysis:**

   * **Evidence:** Documentation detailing identified software hazards, risk classifications, and mitigations. Includes:
     + Failure Modes and Effects Analysis (FMEA).
     + Fault tree analysis (FTA).
   * **Purpose:** Ensures hazards are identified and addressed systematically during the life cycle.
3. **IV&V Progress Reports:**

   * **Evidence:** Periodic reports from IV&V teams summarizing verification/validation activities, findings, defect identification, and resolutions.
   * **Purpose:** Provides independent documentation of software quality, functionality, and adherence to critical requirements.
4. **Test Results for Safety-Critical Software:**

   * **Evidence:** Test reports verifying the performance of safety-critical software against safety-specific requirements under nominal and off-nominal conditions.
   * **Includes:**
     + Validation tests for hazardous event scenarios.
     + Functional safety tests.
   * **Purpose:** Demonstrates the software's ability to operate safely and avoid unintended functions in hazardous conditions.
5. **Code Inspection and Review Logs:**

   * **Evidence:** Results of code reviews and static/dynamic analysis performed to detect bugs, vulnerabilities, or non-conformance in implementation.
   * **Purpose:** Confirms that all discrepancies were identified, logged, and resolved according to NASA's assurance standards.
6. **Cybersecurity Testing Results:**

   * **Evidence:** Reports documenting penetration testing, security vulnerability scans, and compliance with security standards for safe software operation.
   * **Purpose:** Ensures software security, particularly in response to NASA-STD-8739.8 requirements for safety-critical systems.
7. **Configuration Management Records:**

   * **Evidence:** Records verifying that all changes to assurance-related processes, plans, and artifacts are managed, tracked, and approved.
   * **Purpose:** Validates that plans and products are consistent throughout the software life cycle.

---

#### **3. Verification Activities**

Verification evidence ensures that assurance activities comply with the requirement and that all defects and risks are addressed.

1. **Verification and Validation (V&V) Strategy Reports:**

   * **Evidence:** Documents describing the implemented verification processes, results, and validation activities performed to confirm compliance with requirements.
   * **Purpose:** Provides confidence in software correctness and adherence to specifications.
2. **Safety-Critical System Validation Reports:**

   * **Evidence:** Reports validating safety-critical systems, focusing on risk mitigation (e.g., redundancy, fault tolerance) and correct implementation of safety-critical requirements.
   * **Purpose:** Confirms safety goals have been achieved through thorough testing and validation.
3. **IV&V Final Report (if applicable):**

   * **Evidence:** Final reports independently assessing overall software quality, compliance with requirements, and assurance of safety/security-critical functionality.
   * **Purpose:** Provides independent confirmation of readiness for deployment.
4. **Certification of Compliance:**

   * **Evidence:** Signed certification documents confirming conformance to NASA-STD-8739.8 and related standards.
   * **Purpose:** Provides formal evidence that the requirement has been fully satisfied.

---

#### **4. Continuous Monitoring Evidence**

Continuous assurance and monitoring during and after deployment are essential for life cycle compliance and risk mitigation.

1. **Anomaly Tracking Logs:**

   * **Evidence:** Logs of software anomalies identified during post-deployment monitoring, including resolution status and lessons learned reports.
   * **Purpose:** Ensures continuous identification and resolution of risks after software deployment.
2. **Maintenance and Sustainment Reports:**

   * **Evidence:** Reports documenting the sustainment of safety-critical software, including regular updates to assurance plans based on operational lessons learned.
   * **Purpose:** Demonstrates lifecycle coverage of assurance goals from development to operation and decommissioning.

---

### **Objective Evidence Summary Table**

| **Category** | **Artifacts** | **Purpose** |
| --- | --- | --- |
| **Planning Artifacts** | SAP, Software Safety Plan, IV&V Plan, Requirements Mapping, Risk Management Plan | Ensures all assurance processes are defined, tailored, and compliant before execution begins. |
| **Execution Artifacts** | Process Assessment Reports, Hazard Analyses, Test Results, IV&V Progress Reports, Security Testing Logs | Demonstrates implementation of assurance activities and compliance with NASA-STD-8739.8. |
| **Verification Activities** | V&V Strategy Report, Safety-Critical Validation Reports, IV&V Final Report, Compliance Certification | Confirms the software meets safety, security, and quality requirements through testing and validation. |
| **Continuous Monitoring Evidence** | Anomaly Logs, Maintenance Reports, Lessons Learned | Ensures assurance coverage and risk mitigation throughout software deployment and sustainment. |

---

### **Conclusion**

Objective evidence for **Requirement 3.6.1** confirms that the project manager has successfully planned, implemented, and verified all software assurance, software safety, and IV&V tasks as required by NASA-STD-8739.8. This evidence provides traceable documentation of compliance, facilitates audits, and establishes confidence that mission-critical software is safe, secure, and reliable.
