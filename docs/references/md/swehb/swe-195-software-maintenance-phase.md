# SWE-195 - Software Maintenance Phase

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695530. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase

SWE-195 - Software Maintenance Phase

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695530)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695530&showCommentArea=true&showComments=true#addcomment)

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

4.6.5 The project manager shall maintain the software using standards and processes per the applicable software classification throughout the maintenance phase.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-195 History

SWE-195 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.6.5 The project manager shall maintain the software using standards and processes per the applicable software classification throughout the maintenance phase. |
| Difference between C and D | No change |
| D | 4.6.5 The project manager shall maintain the software using standards and processes per the applicable software classification throughout the maintenance phase. |

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
| * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) |

# 2. Rationale

Standards and processes are documented in the [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) or in a separate [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan).  Each software classification has a defined set of requirements and all software at that classification must meet those requirements for its lifetime or until its classification changes, therefore, the software is maintained according to processes and standards defined for its software classification.

The rationale behind Requirement 4.6.5 is to ensure that software used for NASA missions and programs is properly maintained to preserve its reliability, functionality, and quality throughout its lifecycle, including the maintenance phase. By adhering to applicable software standards and processes during maintenance, NASA ensures consistency, compliance, and mission readiness even as the software evolves post-delivery.

---

### **Rationale Components**

1. **Maintain Mission and Safety-Critical Performance**  
   Many NASA systems involve safety- and mission-critical software (Class A–D), where errors introduced during maintenance could result in catastrophic failures or jeopardize mission success. Adhering to classification-specific processes ensures proper control of software configurations, changes, and risk management in systems where failure is not an option.

   * For example, safety-critical software must continue to meet the highest quality and reliability standards, especially when it is deployed in environments where human life or high-value assets are at stake.
2. **Preserve Software Quality Over Time**  
   Software that enters the maintenance phase often faces operational use in a dynamic environment where requirements, hardware, or constraints may evolve. Continuous application of processes such as regression testing, verification, and audits ensures:

   * **Consistency:** That the quality remains at the required level.
   * **Robustness:** That changes and fixes preserve the software's integrity.
   * **Compliance:** That the delivered systems meet NASA's stringent engineering standards.

   Proper maintenance practices prevent software from degrading into an unmanageable or unreliable state (sometimes referred to as "software rot") over time.
3. **Enable Long-Term Sustainability and Reusability**  
   NASA's missions often span multiple decades, and the software must remain operable and maintainable across its operational lifetime. This includes:

   * **Legacy Systems Support:** Many projects require updates to older systems that may integrate with more modern ones. Maintaining consistent processes ensures such updates are handled systematically.
   * **Reusability of Algorithms and Systems:** Mission-classified software is often repurposed or adapted for future missions. Maintenance performed under clear standards ensures that the software remains understandable, modifiable, and reusable.
4. **Mitigate Risks Introduced in Maintenance**  
   The maintenance phase inherently involves changes to previously deployed and verified software, which can introduce the following risks:

   * New **defects** due to insufficient testing or analysis of the changes.
   * Unexpected **regression issues** that impact previously tested functionality.
   * Disruption of the system’s **functional, performance, and safety requirements.**  
     By maintaining the use of classification-specific processes during maintenance, these risks are mitigated, and the software's operability remains secured.
5. **Support Evolving Requirements and Operational Contexts**  
   Software must often undergo updates to meet new requirements or adapt to an evolving operational environment. For instance:

   * Correcting defects or addressing known vulnerabilities.
   * Adapting to hardware or platform updates (e.g., obsolescence of components).
   * Improving performance, increasing functionality, or adapting to customer-specified changes.  
     Adhering to well-defined maintenance processes ensures these adaptations align with the software's original design and performance goals, reducing the risk of introducing anomalies or degrading performance.
6. **Ensure Compliance with Standards and Regulations**  
   Maintenance phase adherence ensures the software is compliant with applicable standards, including:

   * **NASA-specific policies and NPR 7150.2 requirements.**
   * **Safety standards** such as NASA-STD-8719.13 and related hazard mitigation requirements.
   * **Cybersecurity requirements** to address evolving threats.  
     Adhering to these standards ensures that auditors, oversight committees, and stakeholders can trust the software’s integrity during critical phases of a mission's life.
7. **Ease Transition for Future Teams**  
   Long-lived software often outlasts its original development team. Consistently applying classification-specific maintenance standards reduces knowledge gaps and makes software more maintainable by future teams. Examples of benefits include:

   * Easier onboarding for new engineers or contractors.
   * Simplified understanding of development and maintenance history.
   * Predictable and repeatable workflows for implementing future changes.

---

### **Software Classification and Maintenance Standards**

NASA software classification (Class A–F) defines the applicable processes and standards during both development and maintenance phases. For example:

* **Class A (Human-rated software systems):** Requires the highest level of rigor since it may impact human life. Maintenance must follow formal testing, verification, and hazard analysis with extensive documentation.
* **Class C (Mission support software):** While not safety-critical, failure may result in significant mission risks, and maintenance must focus on functional integrity and operability.
* **Class E/F:** Used for less critical or research-oriented software, where fewer controls may apply, but maintaining software discipline reduces inefficiencies and redundant work.

Maintaining software using standards aligned with its classification ensures consistency and proportionality in resource usage—matching the effort to the risk and criticality of the software.

---

### **Key Activities During the Maintenance Phase**

Following classification-specific standards involves these essential activities:

1. **Change Review and Management:**
   * All software updates and fixes are formally reviewed, tested, and approved before implementation.
2. **Testing and Verification:**
   * All updates undergo regression testing to ensure changes do not break existing functionality.
3. **Configuration Management:**
   * All updates are tracked, versioned, and validated using proper configuration management practices.
4. **Defect Management:**
   * Identified software defects are tracked, categorized, and prioritized for resolution with the same rigor as during development.
5. **Documentation Updates:**
   * All changes in maintenance must reflect in updated operational manuals, code comments, software descriptions, and design documents.
6. **Safety and Risk Assessment:**
   * Software updates are assessed for safety risks, especially in mission- or safety-critical systems.
7. **Audits:**
   * Regular audits of the maintenance process are conducted to ensure ongoing compliance with standards.

---

### **Summary**

Requirement 4.6.5 ensures that software maintenance is performed with the same rigor as earlier lifecycle phases, adhering to standards tailored to the software’s classification. Doing so:

* **Protects mission success** by ensuring quality and reliability.
* **Prevents regression risks** and ensures performance consistency.
* **Supports long-term sustainability** and system integrity.
* **Reduces operational risks** by adhering to safety and compliance standards.
* **Facilitates adaptability**, enabling software to keep pace with evolving demands.

By maintaining discipline in the maintenance phase, NASA ensures that its software is ready to support current and future missions while continuing to meet its high standards of safety, performance, and reliability.

# 3. Guidance

This improved guidance emphasizes a structured approach to maintaining software throughout its lifecycle, with specific attention to the maintenance phase. It builds upon the software life cycle phases and incorporates best practices for ensuring software quality and compliance with NASA's rigorous standards.

---

### **3.1 Software Life Cycle with Focus on Maintenance Phase**

The software development life cycle (SDLC) is an iterative, structured process guiding software development and maintenance. Each phase plays an essential role in ensuring the software achieves and sustains its intended functionality, quality, and reliability.

The **maintenance phase** requires continuous application of the same rigor and engineering discipline as prior phases. Additionally, during maintenance, the applicable software classification (per SWE-020) determines which standards and processes must be applied.

---

#### **Software Life Cycle Phases and Goals**

1. **Requirement Gathering and Analysis:**

   * **Objective:** Collect, evaluate, and validate customer needs and objectives.
   * Document the original requirements in a **Software Requirements Specification (SRS)**. During maintenance, this document must remain updated to address new requirements, customer modifications, or lessons learned from deployment.
   * For ongoing maintenance: Analyze new requirements against existing functionality and identify potential impact areas (including testing and operational risks).
   * **Outputs:**

     + Requirement Specification Document for baseline requirements.
     + Updated requirements traceability matrix during maintenance.
2. **System and Software Design:**

   * **Objective:** Translate requirements into a system architecture and detailed design.
   * Design artifacts should specify interfaces, system behaviors, and dependencies. These designs remain important during the maintenance phase when changes are introduced to ensure consistency with the system's architecture.
   * For new changes during maintenance: Ensure that the **Software Design Document (SDD)** is updated to reflect modifications.
   * Assess architectural updates required when moving the software to newer platforms or operating environments.
   * **Outputs:**

     + System and software architecture diagrams, system constraints, and updated design documentation for changes introduced during maintenance.
3. **Implementation / Coding:**

   * **Objective:** Develop code based on the approved designs and ensure adherence to coding standards defined in the Software Development/Management Plan (per SWE-013).
   * For the maintenance phase, follow configuration management procedures to ensure changes or patches do not negatively impact the baseline system.
   * Apply automated code analysis tools where feasible to maintain code quality throughout the project’s evolving software lifecycle.
   * **Outputs:**

     + New or modified code that meets quality and performance standards.
     + Code reviews and defect fixes logged in the version control or maintenance system.
4. **Testing:**

   * **Objective:** Validate that the software meets functional and non-functional requirements, especially after changes are introduced during maintenance.
   * Design and execute regression tests in the maintenance phase to verify new changes have not impacted previous functionality.
   * Testing during maintenance must include:

     + **Functional testing:** For new or changed functionality.
     + **Regression testing:** To ensure existing functionality remains unaffected.
     + **Performance testing:** For systems subject to high loads or real-time requirements.
     + **Hazard/safety testing:** For safety-critical software (Class A–C).
     + **Interface testing:** Targeting affected communication channels with external systems.
   * Testing coverage should align with the software classification, with stricter requirements for higher classifications.
   * **Outputs:**

     + Updated test plans, procedures, and reports reflecting maintenance-specific test cases.
     + Regression test results and defect tracking reports.
5. **Deployment/Release:**

   * **Objective:** Transition the software to the operational environment following defined release procedures.
   * In the maintenance phase, focus on deploying patches, updates, or enhancements in a controlled and documented manner.
   * Review system constraints, ensure compatibility with the deployment platform, and confirm adherence to defined configurations.
   * **Outputs:**

     + Controlled delivery of updates or patches.
     + Release notes describing enhancements, bug fixes, and known defects (if any).
     + Updated version description documents (VDD) and configuration management records.
6. **Maintenance:**

   * **Objective:** Preserve the software’s operational reliability and performance, while implementing approved changes systematically.
   * Maintenance includes activities such as:

     + **Corrective Maintenance:** Fixing defects not detected during testing or errors raised during operational use.
     + **Adaptive Maintenance:** Adapting the software to changes in the operating environment, such as hardware updates, new integrations, or platform migrations.
     + **Perfective Maintenance:** Adding or improving functionality to meet evolving user needs or operational requirements.
     + **Preventive Maintenance:** Addressing potential risks like outdated dependencies, cybersecurity vulnerabilities, or anticipated failures.
   * Revisit earlier SDLC phases as necessary to address these maintenance needs, ensuring a structured process is followed.
   * **Outputs:**

     + Updated system documentation reflecting all changes.
     + Maintenance test reports with defect resolutions and regression testing details.
     + Configuration management records detailing all changes and affected artifacts.
     + Ongoing risk assessments and updated documentation for unresolved residual risks.

---

#### **Special Considerations for Maintenance Phase**

1. **Revisiting Earlier Phases:**

   * Changes or fixes made during the maintenance phase often require revisiting prior phases, specifically:
     + **Requirement Analysis:** Ensure changes align with mission objectives.
     + **Design:** Modify designs for new requirements.
     + **Testing:** Ensure adequate regression coverage for old and new functionality.
   * Update key documentation (e.g., requirements, architecture diagrams, configuration baselines) as part of the workflow to ensure traceability.
2. **Configuration and Change Control:**

   * All software modifications during maintenance must adhere to the project's configuration management plan (per SWE-109). This ensures:
     + Traceability of changes.
     + Correctness of integrated changes in the baseline software.
     + Controlled deployment in operational environments.
3. **Risk Assessments:**

   * Software in maintenance often inherits risks not foreseen in earlier phases, such as:
     + Workarounds impacting usability.
     + The introduction of defects through patches.
     + Evolving hardware/software dependencies.
   * Risk mitigation strategies and ongoing testing should address these challenges.
4. **Regression Testing:**

   * Any maintenance activity involving a software change must include regression testing to avoid introducing problems into previously verified functionality. For mission-/safety-critical software:
     + Prioritize testing of critical functions.
     + Automate tests where feasible to improve coverage and repeatability.
5. **Sustained Collaboration Between Teams:**

   * Maintenance frequently involves collaboration between:
     + Original development teams.
     + Software assurance personnel (ensuring applicable standards are maintained).
     + Operations and maintenance teams providing real-world feedback.
   * Processes must ensure clear communication and documentation between these groups.

---

### **Enhancing the Guidance**

* **Defined Maintenance Standards:** Emphasize using software classification-specific processes (aligned to SWE-020) to guide the rigor and scope of activities performed during maintenance.
* **Tailored Regression Plans:** Address varying levels of testing based on the impact and criticality of changes. For high-risk modifications, mandate end-to-end regression to reduce uncertainty.
* **Process Improvement:** Utilize metrics and lessons learned during development and maintenance to adapt and refine standards as the software evolves.

By maintaining a disciplined, classification-specific approach throughout the maintenance phase, NASA ensures the longevity, reliability, and safety of its software systems, enabling the success of both current and future missions.

Once the software classification is determined as defined in [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification), standards, and processes for the applicable software classification are defined in the Software Development/Management Plan (see [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)) to be used throughout the software life cycle. The software is maintained using the defined and documented processes and standards throughout the maintenance phase.

## 3.1 Software Life Cycle

The Software development life cycle model includes the following phases.

**1) Requirement gathering and analysis:**  Business requirements are gathered in this phase. After requirement gathering, these requirements are analyzed for their validity and the possibility of incorporating the requirements in the system to be developed is also studied. A Requirement Specification document is created which serves the purpose of guideline for the next phase of the model.

**2)  Design:**  In this phase, the system and software design are prepared from the requirement specifications which were studied in the first phase. System Design helps in specifying hardware and system/software requirements and also helps in defining overall system architecture. The software design specifications serve as input for the next phase of the model.

**3)  Implementation / Coding:**  On receiving system/software design documents, the work is divided into modules/units and actual coding is started. Since, in this phase, the code is produced so it is the main focus for the developer. This is the longest phase of the software development life cycle.

**4)****Testing****:**  After the code is developed it is tested against the requirements to make sure that the product is solving the needs addressed and gathered during the requirements phase. During this phase, all types of functional testing like unit testing, integration testing,  system testing,  acceptance testing are done as well as non-functional testing are also done.

**5)  Deployment****/Release****:** After successful testing, the product is delivered/deployed to the customer for their use.

**6) Maintenance:** Once when the customers start using the developed system then the actual problems come up and need to be solved from time to time. This process where the care is taken for the developed product is known as maintenance.

The Maintenance Phase is the last phase of the life cycle and occurs once the system is released to the customer and operational. It includes implementation of changes that software might undergo over some time, or implementation of new requirements after the software is deployed at the customer location. The maintenance phase also includes handling the residual errors that may exist in the software even after the testing phase. This phase also monitors system performance, rectifies bugs, and requested for changes to be made. Maintenance is what happens during the rest of the software’s life: changes, correction, additions, moves to a different computing platform, and more.

During the maintenance phase the previous phases in the software life cycle may need to be revisited as applicable.  Software changes should be analyzed to determine the level of regression testing to be performed. 

See also [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement), 

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

# 4. Small Projects

Small projects often have fewer resources, tighter deadlines, and smaller teams compared to larger projects. However, the need to maintain software using defined standards and processes remains crucial to ensure quality, reliability, and traceability—especially when software is mission-critical or has significant long-term implications. Below is tailored guidance for small projects to help effectively implement Requirement 4.6.5, focusing on simplicity, efficiency, and scalability.

---

### **Why This Requirement Still Matters for Small Projects**

1. Small projects often have limited redundancy, so introducing errors during maintenance can pose a disproportionate risk.
2. Minimal documentation or informal processes during development can lead to misunderstandings and inefficiencies during the maintenance phase.
3. Following lighter but clearly defined standards ensures small projects remain manageable, scalable, and compliant with NASA’s policies while balancing resource constraints.

---

### **Simplified Maintenance Process for Small Projects**

#### **1. Use Tailored Standards and Processes**

* **Leverage “Scaled-Down” Standards:**  
  Small projects can adopt simplified subsets of NASA’s larger standards (e.g., NPR 7150.2 and related guidelines). Focus on:
  + Critical software classification requirements.
  + Safety, quality, and configuration management.
  + Regression testing and verification for maintenance activities.
* **Document Key Processes Minimally:**  
  Use lightweight templates for maintenance-related documentation such as a **Maintenance Log**, **Change Control Record**, and **Risk Register**.
* **Emphasize NASA Software Classifications (SWE-020):**  
  Ensure the classification of the software determines the level of rigor for applying standards, focusing on safety and critical functionality in proportion to the software's mission-critical nature (Class A–F).

**Key Tip:**  
Adopt reusable and easily customizable templates (NASA or project-specific) for documentation to save time and effort.

---

#### **2. Revisit the Software Lifecycle as Needed**

Follow the software development lifecycle (SDLC) phases outlined in the previous guidance, but light-scale them for maintenance:

1. **Requirement Gathering and Analysis:**
   * Simplify requirements gathering for new changes or patches during maintenance.
   * Use a single **Requirement Change Log** to track newly added, deleted, or modified requirements.
2. **Design:**
   * Create lightweight design documents for small fixes or enhancements. Focus only on what impacts interfaces, algorithms, or performance.
3. **Implementation:**
   * Prioritize modularized changes and document updates minimally in plain-text logs (e.g., GitHub issues, Jira tickets, etc.) to keep track of changes systematically.
4. **Testing:**
   * Focus on **automating** the most critical regression and functional tests wherever possible for efficiency. Use free or low-cost tools (e.g., Python with `pytest`, JUnit for Java).
   * Scale testing based on criticality (e.g., higher focus on mission-critical systems).
5. **Configuration Management:**
   * Use simple version control tools (e.g., Git) to manage changes to the software baseline.
6. **Delivery / Deployment:**
   * Utilize a lightweight release process (e.g., automated builds and deployment pipelines using GitHub Actions, Jenkins) to streamline maintenance.

---

#### **3. Testing During Maintenance: Prioritize What’s Necessary**

Since testing can consume significant resources, small projects should prioritize testing while maintaining compliance with critical quality standards:

* **Focus on Risk-Based Testing:**
  + Identify high-risk areas (e.g., safety-critical and mission-critical functions).
  + Test these areas extensively while applying a lighter approach to low-risk components.
  + If small teams lack safety expertise, involve software assurance personnel in identifying critical areas for testing.
* **Regression Testing:**
  + Select only essential tests to confirm existing parts of the system remain functional after changes. Automate regression testing for critical functionality if possible.
* **Document Key Test Results:**
  + Maintain a simple record of completed tests using a checklist or lightweight report format.

---

#### **4. Change Control and Configuration Management**

Small projects often encounter changes during maintenance, such as hardware updates, defect fixes, or customer-driven enhancements, and need simple processes to manage them:

1. **Define a Clear Change Process:**
   * Create a lightweight change request workflow:
     1. Request the change (e.g., add new functionality, fix a defect).
     2. Analyze the impact of the change on software requirements and risk.
     3. Approve the change (team leader/project manager).
     4. Implement and verify the change.
   * Document approvals using a spreadsheet or a simple change log tool.
2. **Track Configurations Simply:**
   * Use tools such as Git for version control and ensure that every approved change is linked to a specific configuration "tag" or version.
   * Tie change requests to specific commits in your version control system for traceability.

---

#### **5. Prioritize Documentation (Lightweight and Practical)**

Documentation in small projects should be concise but sufficient to ensure traceability and reuse. Focus on maintaining:

* **A Maintenance/Change Log:**
  + A single log file or spreadsheet that serves as the source for:
    - What changes were made.
    - Why they were made (reason, risk assessment).
    - Who approved them.
* **Updated Requirements and System Documentation:**
  + Use short, simple addenda to the original requirements or design documents instead of completely rewritten versions.
* **Testing Records:**
  + Use concise formats in a table or spreadsheet to track test results.

---

#### **6. Metrics for Small Projects**

Small projects often don’t have extensive data collection mechanisms. Use a small set of metrics to monitor quality during maintenance, such as:

* **# of changes/patches implemented vs. # planned.**
* **# of defects identified vs. corrected.**
* **# of requirements impacted in each maintenance cycle.**
* **# of regression tests passed vs. total tests executed.**
* **Time spent resolving each defect.**
* These metrics help monitor trends and focus improvement efforts over time.

---

#### **7. Collaboration and Knowledge Management**

Small teams are often stretched thin, so maintaining clarity in team communication during maintenance is critical:

* **Define Clear Roles:**
  + Assign specific team members responsibility for testing, documentation, and coding.
* **Share Knowledge Updates:**
  + Use shared tools (e.g., Confluence pages, GitHub or Google Drive) to store and share updated documents.
  + Ensure all team members understand how changes impact the system functionality.

---

#### **8. Risk and Resource Management**

* **Minimize Unnecessary Work:**
  + Avoid overdocumentation or unnecessary low-priority tests; instead, focus resources where they matter (e.g., high-risk areas).
* **Proactively Address Risks:**
  + Review risks associated with deferred defects or maintenance scope creep. Maintain a simple risk register.

---

### **Checklist for Small Project Maintenance Compliance with 4.6.5**

1. Is the software classification per SWE-020 applied to guide maintenance rigor?
2. Are maintenance artifacts like change logs, updated requirements, and simplified testing results documented?
3. Are smaller-scale testing (including regression) and configuration management controls in place?
4. Are changes formally approved, and is traceability between changes and system updates maintained?
5. Are risks identified, tracked, and mitigated within the maintenance scope?
6. Is the system documentation (e.g., requirements and design) updated proportionally for the changes made?

---

### **Final Note**

For small projects, simplicity and adaptability are key. By focusing on lightweight processes, prioritizing critical activities, and reusing existing tools/templates, small projects can achieve compliance with Requirement 4.6.5 efficiently while maintaining software that meets NASA’s standards of quality and reliability over its lifetime.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA’s Lessons Learned database contains valuable insights from past projects, programs, and missions across various disciplines, including software engineering. These lessons highlight best practices, challenges, and pitfalls that are directly relevant to maintaining software using standards and processes, especially during the maintenance phase of the software life cycle. Below are key lessons learned associated with Requirement 4.6.5 and how they can inform better practices.

---

### **1. Inadequate Documentation During Maintenance**

* **Lesson Learned:**  
  In some cases, inadequate documentation during the maintenance phase led to significant challenges in understanding, troubleshooting, and modifying the software. Teams failed to update requirements, design artifacts, and test cases after implementing changes, leaving future teams with limited visibility into the system impacts of maintenance activities.
* **Example:**  
  A project experienced severe complications when replacing legacy software components in older systems. Documentation was outdated or inconsistent, leading to prolonged periods of redevelopment and retesting.
* **Recommended Actions:**

  + Ensure that all software changes are well-documented, including updates to:
    - Requirements documentation.
    - Design documents for changed components.
    - Version control systems and configuration logs.
  + Use the Software Development/Management Plan to enforce documentation standards during the maintenance phase.

---

### **2. Lack of Adequate Regression Testing**

* **Lesson Learned:**  
  Some projects did not perform sufficient regression testing during the maintenance phase, leading to unintended functionality issues when updates were applied. Insufficient resources were allocated to ensure regression tests for software changes, and defects introduced by those changes created failure points that were not detected until later stages.
* **Example:**  
  On a flight system project, a software update to correct errors inadvertently removed essential logic for handling hardware exceptions. The issue was only discovered after deployment, requiring an emergency patch to prevent mission disruption.
* **Recommended Actions:**

  + Ensure that regression testing is prioritized and adequately funded during maintenance activities.
  + Implement automated regression testing tools to minimize manual effort, especially for safety-critical systems.
  + Analyze changes to determine the scope of testing required, leveraging risk-based testing practices.

---

### **3. Mismanagement of Software Configuration**

* **Lesson Learned:**  
  Configuration management failures during the maintenance phase resulted in discrepancies between the operational software and documented versions. These mismatches led to confusion about the correct version to use and increased the likelihood of introducing errors when modifications were made.
* **Example:**  
  A control system software update lacked proper version control, and teams inadvertently reverted to an earlier version of code, introducing previously fixed defects back into the system.
* **Recommended Actions:**

  + Use robust configuration management processes, including tools like Git, SVN, or others appropriate for your project size and scale.
  + Implement version control tags and audit trails to ensure that every change is traceable and integrated into the correct baseline.
  + Enforce regular audits of configuration records during maintenance.

---

### **4. Insufficient Risk Assessment for Maintenance Activities**

* **Lesson Learned:**  
  Decisions made during the maintenance phase without thorough risk assessment led to unanticipated consequences. Many software changes were implemented without fully understanding their downstream impact on the system, leading to degraded performance or safety issues.
* **Example:**  
  In a planetary science mission, a minor update to communication protocols resulted in end-to-end system delays during critical data transmission periods because the interactions with other subsystems were not fully tested.
* **Recommended Actions:**

  + Perform risk assessments for all software changes during maintenance, focusing on potential impacts to safety, systems integration, and performance.
  + Maintain a risk register to track, mitigate, and resolve risks systematically.
  + Involve software assurance personnel in reviewing high-priority or high-impact changes.

---

### **5. Legacy System Maintenance Challenges**

* **Lesson Learned:**  
  Maintaining legacy software has proven difficult when there was a lack of personnel familiar with the original system design or when the software was built without modern standards. Maintenance costs and effort increased significantly because systems had to be reverse-engineered or redeveloped.
* **Example:**  
  In the Space Shuttle program, some legacy software components required extensive work by specialized teams to adapt code to newer hardware environments. This process delayed mission readiness, and only limited resources were available for long-term support personnel.
* **Recommended Actions:**

  + Ensure original system documentation is thorough and preserved for future teams.
  + Plan for legacy system transitions by allocating resources for knowledge management and training on older systems.
  + Use flexible architectures and modern development standards during initial phases to simplify future maintenance.

---

### **6. Deferred Defect Resolutions**

* **Lesson Learned:**  
  Defects that were deferred during development and subsequently scheduled for resolution during the maintenance phase were often overlooked or deprioritized. This led to cumulative technical debt, which negatively impacted performance and reliability over time.
* **Example:**  
  Defects identified during unit testing in a navigation system were deferred, with the understanding that they would be corrected during maintenance. When the defects were finally addressed, they caused regression issues and increased rework costs.
* **Recommended Actions:**

  + Create a well-prioritized defect backlog and address high-priority issues immediately during the maintenance phase.
  + Continuously monitor and update defect resolution plans to avoid accrual of technical debt.
  + Ensure stakeholder/customer acceptance for deferred defects, with clear rationale and risk documentation.

---

### **7. Cybersecurity Vulnerabilities During Maintenance**

* **Lesson Learned:**  
  Many systems faced cybersecurity vulnerabilities due to inadequate patch management during maintenance. Projects were unable to keep pace with evolving cybersecurity threats, exposing operational systems to risk.
* **Example:**  
  A project involving ground operations software failed to patch known vulnerabilities in older library dependencies, leaving the software exposed to potential attacks during critical mission support activities.
* **Recommended Actions:**

  + Regularly assess system dependencies for vulnerabilities and perform security patches as part of routine maintenance.
  + Implement cybersecurity testing (e.g., penetration testing or static code analysis tools) for systems during maintenance cycles.
  + Coordinate with NASA’s Office of the Chief Information Officer (OCIO) to ensure compliance with evolving cybersecurity policies.

---

### **8. Resource Constraints for Maintenance**

* **Lesson Learned:**  
  Small teams often struggled to maintain software systems due to limited resources available for maintenance compared to development. Maintenance was treated as an afterthought, leading to rushed updates and incomplete evaluations.
* **Example:**  
  A smaller project supporting scientific data analysis attempted to implement multiple updates but failed to follow proper testing cycles due to insufficient personnel and timeline constraints. This resulted in flawed outputs that required emergency corrections.
* **Recommended Actions:**

  + Plan and budget specific resources for maintenance tasks during project lifecycle planning.
  + Use automation tools (e.g., testing frameworks, CI/CD pipelines) to reduce resource burden for testing and deployment.
  + Scale maintenance processes proportionally to the scope and criticality of the software.

---

### **9. Lack of Customer Engagement During Maintenance**

* **Lesson Learned:**  
  Some projects failed to involve stakeholders and users during the maintenance phase, leading to misaligned priorities and dissatisfaction with updates. Customers were unaware of deferred defects or updates that impacted how the system was used operationally.
* **Example:**  
  A mission-critical ground system deployed an operational patch without consulting end-users, only for the patch to disrupt workflows and lead to unexpected downtime.
* **Recommended Actions:**

  + Involve stakeholders and users during maintenance discussions to ensure priorities align.
  + Hold regular maintenance reviews to brief stakeholders on changes, deferred features, and system status.
  + Implement transparent communication policies through updates like delivery notes and risk assessments.

---

### **Summary of Lessons Learned**

**Key Themes:**

1. Ensure comprehensive documentation during all phases of maintenance.
2. Prioritize regression testing and risk assessment for all changes.
3. Use robust configuration management practices.
4. Manage cybersecurity threats proactively during ongoing maintenance.
5. Allocate resources and plan realistically for long-term software maintenance.

**Takeaway:**  
By addressing these lessons learned proactively, projects can avoid common pitfalls, ensure high-quality software performance over its lifecycle, and maintain compliance with Requirement 4.6.5 across NASA’s diverse portfolio of missions and programs.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Provide template(s) to facilitate developing documentation](https://software.gsfc.nasa.gov/lesson-details/61/).**Lesson Number 61**: The recommendation states: "Use of template(s) and a delivery schedule can help with required documentation."
* [Engage early with experts from previous missions](https://software.gsfc.nasa.gov/lesson-details/135/).**Lesson Number 135**: The recommendation states: "Engage early with experts from previous missions to understand their data standards."
* [Establish processes early in development](https://software.gsfc.nasa.gov/lesson-details/331/). **Lesson Number 331**: The recommendation states: "Establish development and testing methodology and process early in the lifecycle."

# 7. Software Assurance

**SWE-195 - Software Maintenance Phase**

4.6.5 The project manager shall maintain the software using standards and processes per the applicable software classification throughout the maintenance phase.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Perform audits on the standards and processes used throughout maintenance based on the software classification.

## 7.2 Software Assurance Products

This improved guidance provides clarity on the essential role of Software Assurance (SA) during the maintenance phase and strengthens the elements of audits, metrics, and processes required for compliance with Requirement 4.6.5. It emphasizes how SA ensures that standards and processes remain effective, that non-conformances are identified and addressed, and that maintenance efforts align with NASA's quality and safety expectations.

#### **Standards and Processes Audit Report**

The **Standards and Processes Audit Report** is a key deliverable from SA, summarizing:

* The results of audits on all standards and processes used during the maintenance phase.
* Identification of findings, issues, and non-conformances.
* Corrective actions and recommendations for resolving issues and bringing processes into compliance.

The report must:

1. **Assess Compliance:** Ensure that the processes and standards being used align with NASA software policies, the applicable software classification (per SWE-020), and the Software Development/Management Plan.
2. **Evaluate Process Effectiveness:** Highlight any inefficiencies or gaps that may lead to risks, unnecessary delays, or loss of software functionality.
3. **Trace to Outcomes:** Map audit findings directly to observed or potential impacts on software quality and identify actions to prevent defects.

**Enhanced Areas of Focus for Audit Reports:**

* **Configuration Management:** Ensure all software changes, versions, and baselines are tracked and verified for completeness.
* **Change Control Processes:** Audit whether all changes were approved, tested, and implemented in line with change management procedures.
* **Safety-Critical Testing:** Review that safety-critical functions and non-functional requirements (e.g., performance, reliability) were adequately tested during maintenance.
* **Regression Testing:** Verify that regression testing covered all potentially affected areas and that results were thoroughly validated.
* **Operational Transition Process:** Confirm that processes for transitioning changed software into the operational environment are robust and free of gaps.

---

## 7.3 Metrics for Software Assurance

Measuring the effectiveness of maintenance practices requires actionable metrics that allow SA to track trends, evaluate compliance, and provide insights for improvement. Metrics should focus on non-conformances, process compliance, and audit effectiveness.

#### **Core Metrics for Maintenance Phase Audits**

1. **# of Non-Conformances Identified in the Software After Delivery:**

   * Tracks defects discovered during operational use after software was released. A high count may indicate gaps in maintenance testing or verification processes.
   * Allows differentiation between corrective, adaptive, and perfective maintenance needs.
2. **# of Process Non-Conformances Identified by SA vs. # Accepted by the Project:**

   * Measures the project's responsiveness to issues raised by SA, identifying instances where issues may have been dismissed without adequate justification.
   * Provides insight into SA's collaboration with the project team.
3. **Trends of # Open vs. # Closed Non-Conformances Over Time:**

   * Monitors the efficiency of resolving findings over the course of maintenance.
   * Helps ensure closure rates are balanced with discovery rates.
4. **# of Non-Conformances per Audit:**

   * Quantifies the scope and severity of issues identified in audits (including standards/process compliance issues and work product defects).
   * Identify trends to focus attention on recurring process deficiencies.
5. **Trends of # of Non-Conformances from Audits Over Time:**

   * Tracks long-term process health and monitors improvement or deterioration in compliance over successive audits.
6. **# of Open vs. Closed Audit Non-Conformances Over Time:**

   * Provides a granular view of audit findings and how effectively the project addresses them.
7. **# of Compliance Audits Planned vs. # Performed:**

   * Measures alignment with planned SA audit activity to ensure audit coverage is not neglected during resource-constrained periods.
8. **# of Software Process Non-Conformances by Life Cycle Phase Over Time:**

   * Tracks maintenance-specific process issues, such as inadequate testing, insufficient configuration management, or weak operational readiness processes.

**Additional Considerations:**

* Break down metrics by **software classification**, as higher-class systems (e.g., Class A/B) require greater attention to safety and quality.
* Emphasize **defect origin analysis** for issues identified during maintenance to determine root causes (e.g., testing gaps, missed requirements, underreviewed changes).

#### **Reasons for These Metrics:**

These metrics keep SA aligned with Requirement 4.6.5 by identifying where processes and standards are being followed or deviated from, promoting a culture of accountability and improvement during the software maintenance phase.

---

## 7.4 Software Assurance Maintenance Process Guidance

#### **Key Role of Software Assurance During Maintenance**

During the maintenance phase, SA plays a critical role in auditing and verifying processes, ensuring that all software updates, patches, and fixes comply with NASA standards, processes, and checks, particularly for critical and safety-related systems. For small and large projects alike, SA ensures adherence to classification-appropriate standards that prevent regression, minimize risks, and maintain mission success.

---

#### **1. Auditing the Maintenance Processes**

SA will perform routine and targeted audits on the maintenance processes and procedures in use. The audits should focus on:

* **Configuration Management Processes:**
  + Are all modifications, patches, and updates tracked using version control systems?
  + Are processes in place to track the impact of changes and manage baselines effectively?
* **Change Management:**
  + Verify that all proposed changes pass formal review and are validated for safety and quality impacts before implementation.
  + Review all deferred defect fixes to ensure they are tracked and appropriately prioritized.
* **Operational Transition of Updated Software:**
  + Test and audit the transition process for changes pushed to the operational environment. Ensure adequate stakeholder coordination and formal acceptance are obtained.
* **Testing Procedures for Maintenance Changes:**
  + Ensure regression testing and safety-critical testing address all impacted areas of the software.
  + Review test adequacy for all updated functional, performance, and interface requirements.

---

#### **2. Tracking Audit Findings and Non-Conformances**

* All findings, including non-conformances identified during audits, must be **immediately recorded** in a formal tracking system. A comprehensive tracking process should include:
  + Non-conformance description and severity classification.
  + Actions required to resolve findings (including corrective and preventive measures).
  + Assigned responsibility and due dates for resolution.
  + Regular updates on resolution status (open, in-progress, closed).
* **Escalate Safety-Critical Issues Early:**
  + For findings involving safety-critical software, escalate issues promptly to project leadership to prevent operational risk.

---

#### **3. Engaging the Project Team**

* **Collaborative Resolution of Findings:**
  + SA should work closely with the project team to address audit findings promptly. Ensure findings are not ignored or deprioritized, particularly those related to safety and compliance.
  + Frequent communication, in the form of collaborative reviews or working sessions, can reduce the friction between SA and development teams.
* **Timely Sharing of Audit Results:**
  + Ensure audit results are shared with the project team and stakeholder groups immediately after the audit. Clear details regarding non-conformances, risks, and recommended actions must be included.

---

#### **4. Strengthening Process Improvements**

SA should also focus on **continuous improvement** of the maintenance process by:

* Analyzing all non-conformances during audits to identify **systemic process weaknesses.**
* Providing actionable recommendations to mitigate repeat findings and improve ongoing adherence to standards and processes.
* Tracking the implementation of effective improvements year over year.

---

#### **5. Automation and Tools**

Encourage the use of tools to improve the efficiency of SA during the maintenance phase:

* Automate validation of configuration management processes and tracking of changes via tools like GitHub, GitLab, or specialized NASA tools.
* Use automated regression testing tools to confirm thorough test coverage during maintenance.
* Leverage dashboards for real-time tracking of audit non-conformance metrics.

---

#### **6. Focus on Risk Management for Maintenance**

* SA should continually assess how effective the project's maintenance phase is in mitigating risks:
  + Are safety-critical functions still meeting standards after changes?
  + Are vulnerabilities (e.g., cybersecurity risks) promptly addressed?
  + Are deferred issues being handled before they pose long-term risks?

---

### **Final Note**

This guidance ensures that SA responsibilities for Requirement 4.6.5 are clear, practical, and effective. By combining targeted audits, relevant metrics, collaboration with project teams, and continuous improvement, SA ensures software maintenance meets NASA’s standards for quality, safety, and mission success.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is documentation, artifacts, or records that verify that the activities and outcomes associated with maintaining software are compliant with defined processes, standards, and requirements in alignment with the software classification per SWE-020. Below is a detailed list of recommended objective evidence that ensures compliance with Requirement 4.6.5 during the maintenance phase.

---

### **1. Evidence of Standards and Processes**

The following items should demonstrate that standards and processes were defined, documented, and adhered to throughout the maintenance phase:

* **Signed and Approved Software Development/Management Plan (SDMP):**

  + A plan that explicitly defines the maintenance standards and processes to be used, tailored to the software classification.
  + Includes processes for configuration management, change control, regression testing, cybersecurity, and artifact updates.
* **Updated and Signed Software Maintenance Plan:**

  + Includes instructions for managing maintenance activities, safety-critical testing, defect resolution, and decision-making for ongoing changes.
* **Audit Reports:**

  + Completed audit reports from software assurance (SA) team demonstrating compliance with applicable standards and processes.
  + Includes results of audits on change management, testing, configuration management, and operational readiness processes.

---

### **2. Evidence of Change Management**

Demonstrating that all software updates, patches, and modifications are handled systematically:

* **Change Requests and Approval Records:**

  + Completed and signed Change Request Forms for all software changes, including impact analysis and risk assessments.
  + Includes the priority, rationale, and traceability back to customer requirements.
* **Configuration Management Records:**

  + Version history tracking all changes, including baseline updates, tagged releases, and rollback records.
  + Logs showing successful integration of changes into the operational environment.
* **Defect Resolution Records:**

  + Comprehensive tracking of defects identified and resolved during the maintenance phase.
  + Records showing how deferred issues are reviewed, prioritized, and eventually resolved.

---

### **3. Evidence of Testing**

Ensuring that all changes introduced during maintenance were properly verified and validated:

* **Regression Testing Reports:**

  + Records of all regression testing performed, including the specific test cases, results, and coverage metrics.
  + Documentation of testing for previously validated functionality impacted by changes.
* **Safety-Critical Test Plans and Results:**

  + Evidence of tests performed on safety-critical software components and interfaces to confirm compliance with safety requirements (especially for class A–C software).
  + Includes unit testing, interface testing, hazard testing, and acceptance testing results.
* **Test Results for Maintenance Changes:**

  + Logs showing testing results specific to new features, patches, or bug fixes implemented during maintenance.
  + Verification results for platform/environment migration or adaptations.

---

### **4. Evidence of Documentation Updates**

Confirming that all relevant documentation was kept up-to-date during maintenance:

* **Updated Requirements Documentation:**

  + Updated Software Requirements Specification (SRS) showing changes to user and system requirements during maintenance.
  + Traceability matrix linking updated requirements to test cases.
* **Updated Design Documents:**

  + Revised Software Design Description (SDD) that reflects modifications made to system architecture, interfaces, or algorithms during maintenance.
  + Includes new diagrams or explanations related to affected system components.
* **Updated Testing Documentation:**

  + Revised test plans and test procedures based on maintenance-related functional and non-functional changes.
  + Includes validation of impact analysis results and regression testing strategies.
* **Release Notes:**

  + Document outlining what maintenance updates were applied, including defect fixes, feature enhancements, deprecated elements, and known issues.

---

### **5. Evidence of Compliance**

Verification that processes were aligned with software classification and NASA standards:

* **Compliance Checklists:**

  + Checklists verifying whether maintenance processes adhered to standards as defined in the SDMP and software classification guidelines (SWE-020).
* **Software Assurance Audit Findings and Resolutions:**

  + Records from SA audits highlighting non-conformances discovered during the maintenance phase and evidence of corrective actions taken to resolve them.
* **Performance Metrics Reports:**

  + Data showing adherence to planned key metrics associated with maintenance tasks, such as defect resolution rates, percentage of regression tests passed, and patch deployment success rates.

---

### **6. Evidence of Configuration and Operational Readiness**

Demonstrating proper integration and validation of updates in the operational environment:

* **Configuration Management System Output:**

  + Logs or reports from version control systems (e.g., Git, SVN) demonstrating proper tracking and approval of software delivery during maintenance.
* **Deployment/Transition Records:**

  + Documentation demonstrating successful deployment of updates to the operational environment.
  + Includes verification of environment compatibility and successful execution of transition plans.
* **Operational Testing Results:**

  + Test results from the operational environment confirming system functionality and stability after updates.

---

### **7. Evidence of Risk Management**

Confirming that risks associated with maintenance activities were identified and mitigated:

* **Risk Register:**

  + Records of risks identified during the maintenance phase, including cybersecurity, operational, and performance risks.
  + Evidence of mitigation efforts, such as corrective testing and documentation updates.
* **Impact Analysis Results:**

  + Analysis reports showing the impact of maintenance changes on system requirements, interfaces, and performance.

---

### **8. Evidence of Metrics Utilization**

Demonstrating how metrics tracked during the maintenance phase were used to improve processes:

* **Maintenance Phase Metrics Report:**

  + Includes reports on non-conformance trends, testing results, and open vs. closed issues over time.
  + Demonstrates measurable improvements (e.g., reduction in defects or increased testing coverage).
* **Software Process Metrics:**

  + Records showing metrics by life cycle phase and evidence of SA tracking compliance and providing feedback.

---

### **9. Evidence from Communication and Collaboration**

Showing how audit findings, results, and issues were shared among teams:

* **Audit Findings Log and Meeting Minutes:**

  + Logs showing timely reporting and resolution of audit findings, including the identification, discussion, and corrective actions for process gaps or deficiencies.
  + Meeting records from reviews between SA personnel, project managers, and stakeholders.
* **Stakeholder Acceptance Records:**

  + Evidence of stakeholder/customer feedback or sign-off on maintenance updates.

---

### **Objective Evidence Summary**

For Requirement 4.6.5, objective evidence needs to demonstrate that standards and processes defined for the applicable software classification were adhered to during maintenance. This includes:

1. Audit records of maintenance processes and standards compliance.
2. Defect tracking and issue resolution documentation.
3. Updated system documentation, including requirements, designs, and test plans.
4. Configuration management logs and deployment reports.
5. Records of regression and safety-critical testing during maintenance.
6. Metrics tracking process effectiveness and non-conformances.
7. Risk assessments for all changes made during maintenance.

By collecting the above evidence systematically, NASA ensures traceability, accountability, and reliability during the maintenance phase while complying with Requirement 4.6.5.

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
