# SWE-143 - Software Architecture Review

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695501. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695501/SWE-143+-+Software+Architecture+Review

SWE-143 - Software Architecture Review

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695501/SWE-143+-+Software+Architecture+Review#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695501)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695501&showCommentArea=true&showComments=true#addcomment)

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

4.2.4 The project manager shall perform a software architecture review on the following categories of projects: 

a. Category 1 Projects as defined in NPR 7120.5.  
b. Category 2 Projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-143 History

SWE-143 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | NEW |
| B | 4.2.4 The project manager shall perform a software architecture review on the following categories of projects:   1. 1. Category 1 Projects as defined in NPR 7120.5.    2. Category 2 Projects as defined in NPR 7120.5 that have Class A or Class B payload risk classification per NPR 8705.4. |
| Difference between B and C | No change |
| C | 4.2.4 The project manager shall perform a software architecture review on the following categories of projects:   1. 1. Category 1 Projects as defined in NPR 7120.5.    2. Category 2 Projects as defined in NPR 7120.5 that have Class A or Class B payload risk classification per NPR 8705.4. |
| Difference between C and D | No change |
| D | 4.2.4 The project manager shall perform a software architecture review on the following categories of projects:   a. Category 1 Projects as defined in NPR 7120.5. b. Category 2 Projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4. |

## 1.3 Applicability Across Classes

This requirement applies based on the selection criteria defined in this requirement.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |

# 2. Rationale

Software architecture deals with the fundamental organization of a system, as embodied in its components and their relationships to each other and the environment. [487](#_tabs-<p></p>)  Software architecture reviews are conducted to inspect quality attributes, principles of design, verifiability, and operability of a software system. The software architecture is reviewed to evaluate its effectiveness, efficiency, and robustness relative to the software requirements.  The software architecture review helps manage and/or reduce flight software complexity through improved software architecture, improved mission software reliability and cost savings.

The rationale for this requirement is built upon the critical role software architecture plays in ensuring mission success, mitigating risks, and maintaining safety in high-stakes projects. Conducting **software architecture reviews (SARs)** provides a proactive mechanism to identify and resolve issues early in the software development lifecycle, particularly for projects with significant consequences for failure.

---

### **Key Rationale Components:**

#### **1. Impact of Software Architecture on Mission Success**

Software architecture underpins the entire software development process by defining the structure, dependencies, quality attributes, and behaviors of software systems. An inadequate or flawed architecture can result in:

* **Integration Failures:** Software may be unable to interface correctly with other mission subsystems or hardware, leading to serious system-wide operational failures.
* **Scalability and Stability Issues:** Poor architectural design can result in systems that are unable to handle changing requirements, increased workloads, or environmental variability during operations.
* **Unanticipated Complexity:** Weak architecture drives incidental complexity, increasing costs, reducing reliability, and creating inefficiencies.

Reviews ensure the architecture can reliably and efficiently meet the mission's needs.

---

#### **2. Increased Risk Profile for Category 1 Projects**

**Category 1 Projects**, as defined in NPR 7120.5, typically involve missions or systems that are:

* **Critical to National Needs or Agency Goals:** These projects often support essential scientific discoveries, technological innovation, or national strategic objectives.
* **High Resource Investment:** Category 1 projects involve significant levels of funding and organizational resources.
* **High Risks and Consequences for Failure:** Failure of a Category 1 project may result in severe economic, scientific, political, or operational consequences.

Given the stakes, software architecture reviews are essential to confirm architectural robustness, traceability, safety, quality, and system-wide integrity.

---

#### **3. Payload Risk in Class A and Class B Missions**

**Category 2 Projects** with **Class A or Class B payload risk classification** per NPR 8705.4 represent missions with heightened importance and risk factors, specifically:

* **Class A Payloads:**

  + The highest priority payloads with minimal tolerance for loss. Examples include crewed missions, flagship missions, or major scientific endeavors (e.g., the James Webb Space Telescope).
  + Software failures in Class A projects can result in catastrophic mission loss or endanger lives.
* **Class B Payloads:**

  + High priority payloads where robust performance is mandatory, and failure would severely impact mission objectives. These projects often support valuable scientific research or large-scale capabilities (e.g., Mars rover missions).

Software plays a pivotal role in ensuring payload safety and operational success. Architecture reviews for these projects ensure that:

1. **Fault Tolerance:** Key mechanisms such as redundancy, health monitoring, and failover strategies are designed into the architecture.
2. **Safety-Critical Systems:** Architectural choices mitigate hazards and satisfy safety requirements.
3. **Mission Complexity:** Risks associated with increasing system size and complexity are mitigated through modularity, scalability, and strong interface design.

---

#### **4. Early Risk Identification and Mitigation**

Software architecture reviews occur early in the lifecycle, typically prior to implementation. They enable:

* **Proactive Risk Identification:** Reviews identify risks that can cascade into major problems later in the lifecycle, such as performance bottlenecks, scalability limitations, or interface mismatches.
* **Design Validation:** A review determines whether the architecture meets the driving requirements, addresses stakeholder concerns, and adheres to design principles that mitigate failure risk.
* **Reduction of Late-Stage Rework:** By validating and refining architectural choices early, reviews reduce the risk of expensive and disruptive rework during testing or operations.

For high-priority systems, this early intervention is vital to minimizing risk.

---

#### **5. Complexity of Systems Addressed in Category 1 and Class A/B Projects**

Category 1 and Category 2 (Class A/B payload) projects often involve systems of unprecedented scale and complexity:

* **Crewed Missions:** Systems supporting human spaceflight (e.g., ISS, Artemis) require software architectures capable of managing critical functions such as life support, navigation, and crew safety.
* **Interplanetary Missions:** Complex architectures are essential to handle signal delays, autonomous operations, and resource optimization for missions operating beyond Earth (e.g., Mars exploration, deep space probes).
* **Scientific Observatories:** Earth satellite and observatory missions (e.g., Kepler, JWST) depend on software to control hardware, process data streams, manage environmental factors, and handle precision tasks.

Software architecture reviews ensure these systems are resilient, scalable, and manageable even under extreme conditions.

---

#### **6. Governance and Compliance**

This requirement is closely tied to compliance with NASA's processes outlined in:

* **NPR 7120.5:** Comprehensive project management guidelines for NASA programs and projects.
* **NPR 8705.4:** Risk classification for payloads, emphasizing the need for rigorous standards for Class A and B payloads.

By performing architecture reviews, adherence to NASA’s governing policies is ensured, and the reviews serve as a checkpoint for project accountability and stakeholder engagement.

---

### **Why Software Architecture Reviews Are Mandatory for These Projects:**

1. **Criticality of Success:** These projects cannot afford architecture failures due to their high visibility, costs, and potential for catastrophic impact.
2. **Mitigation of Project Complexity:** Reviews provide a structured approach to managing software systems' unprecedented complexity, reducing risks related to scalability and system-wide interactions.
3. **Stakeholder Confidence:** Reviews validate architecture against driving requirements, giving stakeholders confidence that the project is on track to meet objectives.
4. **Alignment to NASA Standards:** Architecture reviews ensure compliance with NASA standards and policies, further verifying alignment with mission-critical processes.

---

### **Examples Supporting the Rationale**

* **James Webb Space Telescope (Category 1, Class A):**  
  Software architecture reviews ensured robust control systems for the telescope’s instruments and onboard operations, identifying risks early and reducing downstream issues during deployment.
* **Artemis Program (Category 1, Class A):**  
  Crewed lunar missions require software architecture explicitly designed to handle safety-critical functions such as navigation, life support, and interfaces between ground systems and spacecraft.
* **Mars Perseverance Rover (Category 2, Class B):**  
  Significant effort was invested in architecture reviews to validate autonomous operations, data collection mechanisms, and onboard fault monitoring systems.

---

### **Conclusion**

Software architecture reviews for Category 1 projects and Category 2/Class A or B payload classified projects are essential because of the critical role they play in ensuring mission reliability, safety, and operational success. By systematically identifying and mitigating risks early and adhering to standards of governance, these reviews reduce complexity, enhance system manageability, and safeguard NASA’s goals for high-priority missions. This requirement ensures that software architecture is treated as a centerpiece of project success for high-stakes projects.

# 3. Guidance

A software architecture review may be a peer review or may occur as part of a major milestone review (e.g., Mission/System Definition Review [MDR/SDR]). In either case, the architecture review conforms to [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) and [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements) for peer reviews.  See also Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists). Thus, to conduct an architecture review, the project must:

1. Identify required participants.
2. Use a checklist to evaluate the architecture description.
3. Use established readiness and completion criteria.
4. Track actions identified in the reviews until they are resolved.
5. Identify and record measurements for the review.

The Software Architecture Review Board sub-community of practice, accessible to NASA users on NASA Engineering Network (NEN), provides additional information, including guidance, checklists, and examples, for conducting software architecture reviews. Some of this information is summarized in the sections that follow.

## 3.1 When is an Architecture Review Required

SWE-143 states that an architecture review is required for projects meeting the following criteria:

1. Category 1 Projects as defined in NPR 7120.5.
2. Category 2 Projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4.

Here are expanded definitions for the criteria in SWE-143:

* NPR 7120.5E, NASA Space Flight Program and Project Management Requirements defines Category 1 projects as human space flight projects, projects with a life cycle cost exceeding $1B, or projects with significant radioactive material. [082](#_tabs-<p></p>)
* NPR 7120.5E  defines Category 2 projects as projects that have life cycle costs greater than $250M and less than $1B or have life cycle costs less than $250M with a high priority level based on “the importance of the activity to NASA, the extent of international participation (or a joint effort with other government agencies), the degree of uncertainty surrounding the application of new or untested technologies” and a Class A or Class B payload risk classification.[082](#_tabs-<p></p>)
* NPR 8705.4, Risk Classification for NASA Payloads defines the Class A payload risk classification as payloads with high priority, very low (minimized) risk, very high national significance, very high to high complexity, greater than 5 year mission lifetime, high cost, critical launch constraints, no alternative or re-flight opportunities, and/or payloads where “all practical measures are taken to achieve a minimum risk to mission success. The highest assurance standards are used.” [048](#_tabs-<p></p>)
* NPR 8705.4, Risk Classification for NASA Payloads defines the Class B payload risk classification as payloads with high priority, low risk, high national significance, high to medium complexity, two- to five-year mission lifetime, high to medium cost, medium launch constraints, infeasible or difficult in-flight maintenance, few or no alternative or re-flight opportunities, and/or payloads where “stringent assurance standards [are applied] with only minor compromises in application to maintain a low risk to mission success.”
* Per NPR 8705.4, “The importance weighting assigned to each consideration is at the discretion of the responsible Mission Directorate.”

## 3.2 When to Hold an Architecture Review

Software architecture reviews are held during the software architecture formulation phase before the software architecture is baselined.  Generally, a software architecture review should be held between the Mission or System Definition Review (MDR/SDR) and the preliminary design review (PDR). The earlier reviewers are involved in the software architecture development process, the more effective their inputs will be to the architecture development. (See reviews in Topic [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria))

## 3.3 Identifying Participants

Projects should select participants representing key stakeholders in the software.  This may include but is not limited to: engineers for the computing hardware running the software, engineers for other systems communicating with the software, software testers, software installers, software users, suppliers of input data, and consumers of output data. [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) suggests a minimum of three reviewers.

NPR 7150.2 does not require independent reviewers.  However, if the project seeks an independent review, the NASA Software Architecture Review Board (SARB) is a resource of experienced software architects.  Projects can request a review by the SARB [404](#_tabs-<p></p>).

## 3.4 Evaluation Criteria for Software Architecture Reviews

### 3.4.1 Criteria in ISO/IEC 12207

**Systems and software engineering - Software life cycle processes**

6.4.3.3.2.1 - “The system architecture and the requirements for the items shall be evaluated considering the criteria listed below. The results of the evaluations shall be documented.

a) Traceability to the system requirements.

b) Consistency with the system requirements.

c) Appropriateness of design standards and methods used.

d) Feasibility of the software items fulfilling their allocated requirements.

e) Feasibility of operation and maintenance.

NOTE System architecture traceability to the system requirements should also provide for traceability to the stakeholder requirements baseline.”

[224](#_tabs-<p></p>)

### 3.4.2 Criteria Defined by the Software Architecture Review Board

The FAQ for the Software Architecture Review Board summarizes the criteria for a good architecture review as follows:

“*Software architecture should be evaluated concerning the problem it is trying to solve. That's why a project's problem statement* *is an essential part of review preparation; it describes the problem to be solved and lists success criteria held by various stakeholders. Software architecture should also be evaluated concerning common concerns within its problem domain e.g., flight software...*

*During a review, it's important to keep in mind the distinction between software architecture and software architecture description. A system can have great architecture and a poor description, or vice versa, or any of the other two combinations. In a review, it's important to note where each weakness lies: in architecture or description.*" [323](#_tabs-<p></p>)

The SARB provides a detailed checklist on the SARB sub-community of practice, accessible to NASA users on NEN. **Preparing for a SARB Checklist** [PAT-023](#_tabs-<p></p>) provides the following advice for software architecture reviews - :

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-023 - Preparing for a SARB Checklist**

The SARB has also authored a detailed "Software Architecture Review Board (SARB) Checklist" [407](#_tabs-<p></p>) and a "Candidate Questions for Reference Architectures" [410](#_tabs-<p></p>) (such as product lines).

See also [PAT-029 - Software Architecture Review Board Checklist](/spaces/SITE/pages/120848418/PAT-029+-+Software+Architecture+Review+Board+Checklist), [PAT-030 - SARB Review Checklist with Guidance](/spaces/SITE/pages/120848457/PAT-030+-+SARB+Review+Checklist+with+Guidance),

### 3.4.3 Criteria Defined by the Office of Safety and Mission Assurance

The Office of Safety and Mission Assurance compiled the following list of criteria for a software architecture review (edited):

* Is it clear what the architecture needs to do?
* Is the architecture capable of supporting what the system must do?
* How does the architecture compare with previously implemented architectures, both successful and unsuccessful?  In particular, does the architecture display superior qualities that should be incorporated on other missions and/or at other Centers?
* Have all system requirements allocated to software been identified? Has the project identified which of these allocated requirements drive the architecture?
* Have all the stakeholders been identified to provide the essential design input specifying how the software is to be operated, how it is to execute its functions, and how it is to provide its products?
* Have all the relevant quality attributes been identified and prioritized, and have they been characterized relative to the nature of the mission?
* Has the source of all software elements been identified? Is it clear which portions of the system are custom-built, which are heritage/reused, which are commercial off-the-shelf (COTS), and which are open-source software (OSS)?  Does the rationale exist explaining the project’s respective choices?
* Is it clear whether the architecture will be compatible with the other system components?
* Has the architecture been properly documented for future reference?
* Does the architecture induce unnecessary complexity when addressing what must be done?
* Is the proposed fault management approach appropriate for the software and system?
* Is the architecture flexible enough to support the maturation of the architects’ understanding of what the software must do?
* Does the architecture support efficient code development and testing?
* Have safety-critical requirements been properly allocated to the software architecture?
* Have safety-critical elements of the architecture been identified properly?
* Will the architecture support future systems that are natural extensions or expansions of the current system?
* Does the architecture support performance requirements, including processing rates, data volumes, downlink constraints, etc.?
* To enable effective reuse, does the proposed architecture support some degree of scalability?
* Have the appropriate hazards been traced to the software architecture components?
* Are the software architecture rules defined and documented?
  + Patterns, abstractions, algorithms
  + Monitoring and control
  + Data representation and data management
  + Concurrent threads, processes, memory management
  + Real-time execution, throughput
  + Synchronization
  + Inter-process communication
  + Languages, libraries, operating systems
  + Verification and validation
* Confirm that the documentation of the architectural concept includes at least the minimum information listed below:
  + An assessment of architectural alternatives.
  + A description of the chosen architecture.
  + Adequate description of the subsystem decomposition.
  + Definition of the dependencies between the decomposed subsystems.
  + Methods to measure and verify architectural conformance.
  + Characterization of risks inherent to the chosen architecture.
  + The documented rationale for architectural changes (if made).
  + Evaluation and impact of proposed changes.

* Is the format of the architecture description acceptable? Is the content clear and understandable?
* Is the software architecture description more than a high-level design? Does it include quality attributes, rationale, and principles?

## 3.5 Record Results and Track Actions to Closure

The results of the software architecture review, including findings, concerns, best practices, etc. are captured in a report and presented by the review board to management and others who can improve future processes and ensure that identified concerns are addressed.  Problems found during the software architecture review should be addressed in the project’s closed-loop problem tracking system or corrective action system to ensure they are addressed.

## 3.6 Measurements for Software Architecture Reviews

Projects can use the same measurement process for software architecture reviews as for other peer reviews.  See the [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements).

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)        * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-023 - Preparing for a SARB Checklist](/spaces/SITE/pages/116293679/PAT-023+-+Preparing+for+a+SARB+Checklist) * [PAT-029 - Software Architecture Review Board Checklist](/spaces/SITE/pages/120848418/PAT-029+-+Software+Architecture+Review+Board+Checklist) * [PAT-030 - SARB Review Checklist with Guidance](/spaces/SITE/pages/120848457/PAT-030+-+SARB+Review+Checklist+with+Guidance) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

# 4. Small Projects

Although software architecture reviews are typically rigorous for large-scale missions like Category 1 and Category 2 projects, **small projects** (with limited scope, budget, or resources) can still meet the intent of this requirement by adopting **lean practices** that ensure architectural quality without overloading project constraints. Below is specific guidance on tailoring software architecture reviews for small projects, especially those that fall under high-risk classifications.

---

### **Why Architectural Reviews Are Necessary for Small Projects**

Even for small projects, the architecture serves as the foundation for software success and mission reliability. Small projects often face constraints that amplify risks if architectural flaws are not identified early. For instance:

* **High-Impact Risk:** A small project may still carry mission-critical functions (e.g., controlling payloads, processing scientific data), where a software failure could cause mission failure.
* **Limited Resources:** Small projects typically operate under tighter budgets and may lack redundancy, making it essential to avoid design flaws from the outset.
* **Interdependence:** Small systems often integrate tightly with larger mission systems, meaning flaws in the smaller software architecture could propagate into broader mission failures.

Despite the reduced size/complexity of small projects, **software architecture reviews** ensure:

1. Compliance with NASA standards for safety and assurance.
2. Early identification and rectification of design flaws.
3. Alignment of architecture to mission and payload requirements.

---

### **Tailoring Software Architecture Reviews for Small Projects**

#### **1. Perform a Lightweight Software Architecture Review**

For small projects, simplify the review process to match project complexity and scope:

1. **Focus Areas of Review:**  
   Concentrate on key aspects of the software architecture that are most critical to mission success, including:

   * **Structure:** Ensure modularity and scalability of subsystems even in smaller architectures.
   * **Safety:** Verify safety-critical components, fault tolerance mechanisms, and error isolation.
   * **Interfaces:** Validate internal/external interfaces for compatibility and performance.
   * **Constraints:** Assess resource constraints such as memory usage, timing, and real-time execution.
2. **Perform Functional Workshops:**

   * Replace detailed review boards with **functional team workshops** or small-scale peer reviews, where system engineers and software assurance specialists collaboratively analyze architecture concerns over shorter sessions.
3. **Document Key Findings:**  
   Create a simplified report emphasizing:

   * Major risks identified.
   * Mitigations planned or implemented.
   * Unresolved issues requiring follow-up (e.g., through prototyping or validation testing).

---

#### **2. Leverage Existing Processes and Tools**

Small projects can reduce the burden by using pre-existing tools or methods:

1. **Reuse Architectural Patterns:**  
   Where feasible, adopt proven architectural patterns or frameworks used in similar projects to minimize design complexity and review scope.
2. **Simplified Models and Diagrams:**  
   Use lightweight diagrams (e.g., basic UML diagrams—component interfaces, data flows) to document and communicate architectural structure without requiring formal representations.
3. **Automated Analysis Tools:**  
   Utilize automated tools for architecture verification, such as static analysis tools, dependency-checkers, or flow analyzers. These tools assist in identifying critical design flaws early.

---

#### **3. Focus on Risk-Driven Analysis**

Small projects often face resource limitations, making it impractical to perform exhaustive architecture reviews. A **risk-driven approach** ensures resources are concentrated on areas of highest importance:

1. **Identify Critical Risks and Features:**  
   Evaluate components of the architecture with the highest potential impact on mission success and assurance. For example:
   * Are there safety-critical subsystems?
   * Are there interface dependencies with external systems (e.g., payload hardware)?
   * Are there concurrency or timing considerations (e.g., real-time systems)?
2. **Mitigate Major Architectural Risks:**  
   Apply known methods, like modular design or strict isolation of critical subsystems, to reduce risk in high-impact areas.

---

#### **4. Streamline Stakeholder Engagement**

Small projects typically have fewer stakeholders than large ones:

1. **Stakeholder Identification:**  
   Identify relevant stakeholders for the architecture review, which may include:
   * Systems engineers.
   * Project manager.
   * Software assurance representative.
   * Payload experts (for Category 2/Class A or B payload risk classification).
2. **Simplify Feedback Mechanisms:**  
   Use informal methods (e.g., team meetings, short review sessions) to gather feedback, as opposed to larger, formal review boards.

---

#### **5. Use Iterative and Incremental Review Techniques**

For small projects, software architecture reviews can be iterative rather than exhaustive:

1. **Incremental Reviews:**  
   Conduct smaller reviews focused on individual sections of the architecture (e.g., interfaces, safety-critical features). This reduces upfront review scope and allows for iterative improvements.
2. **Early Prototyping or Simulation:**  
   Validate critical architectural components early using prototypes or lightweight simulations to confirm assumptions and design feasibility.

---

#### **6. Focus on Core Documentation**

Given the resource limitations of small projects, focus on producing streamlined documentation that supports future maintenance and scaling:

1. **Key Deliverables for Architecture Review:**  
   For small projects, ensure the following artifacts are available for review:
   * High-level architecture diagram (e.g., component decomposition, data flow diagrams).
   * Software requirements traceability matrix to architecture components.
   * Interface definitions (internal and external).
   * Risk mitigation reports focused on architectural risks (e.g., handling safety-critical subsystems).
   * Simplified architecture validation reports.
2. **Documentation Maintenance:**  
   Ensure all documentation is stored and versioned properly to allow for maintenance and scalability.

---

### **Example Process for Small Projects**

Small projects can use the following streamlined software architecture review process:

#### **Step 1: Define Review Scope**

* Identify high-risk areas of the architecture to focus on (e.g., safety features, real-time execution, external interfaces).

#### **Step 2: Perform Architecture Walkthrough**

* Conduct workshops or small-team collaborations to evaluate architectural choices and identify risks.

#### **Step 3: Validate Interfaces**

* Ensure that internal and external interfaces are well-defined and compatible with other mission systems.

#### **Step 4: Document Results**

* Create a short report summarizing findings, including identified concerns, mitigation plans, and follow-up actions.

#### **Step 5: Monitor Metrics**

* Use simple metrics to track risks closed, safety-related issues identified, and architectural non-conformances resolved.

---

### **Metrics for Small Projects**

Even small projects should monitor the following metrics during architecture reviews:

1. **# of architectural risks identified vs. resolved:**  
   Ensure that risks identified in the review process are resolved through appropriate actions.
2. **Compliance with requirements:**  
   Track coverage of requirements by architecture components.
3. **Safety-critical issues:**  
   Monitor the number of safety-related issues that trace to architectural components.

---

### **Conclusion**

Small projects must still address software architecture reviews to ensure compliance with NASA standards, especially for Category 1 or Category 2 (Class A/B) missions. By using lightweight review techniques, focusing on risk-driven assessments, and streamlined documentation practices, small projects can meet the intent of the requirement without overburdening limited resources. This tailored approach ensures architectural quality, mitigates risks, and supports safety and mission assurance objectives in a cost-effective and efficient manner.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-048)

  [Risk Classification for NASA Payloads](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=4A "Click to open in new window")

  NPR 8705.4A, Office of Safety and Mission Assurance, Effective Date: April 29, 2021, Expiration Date: April 29, 2026
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-323)

  [Software Architecture Review Board sub-community of practice.](https://nen.nasa.gov/web/sarb "Click to open in new window")

  The objectives of SARB are to manage and/or reduce flight software complexity through better software architecture and help improve mission software reliability and save costs.
* (SWEREF-407)

  [Software Architecture Review Board (SARB) Checklist,](https://nen.nasa.gov/documents/827631/1456145/SARB+Checklist+11-1-17.docx/b80b6e8c-6884-00fe-852f-31f59a70d5ab "Click to open in new window")

  NASA Software Architecture Review Board,  Checklist for general software architecture reviews.
* (SWEREF-410)

  [Candidate Questions for Reference Architectures,](https://nen.nasa.gov/documents/827631/1028210/Reference+Architecture+Questions/914af1ea-7a0a-4a2f-982b-d2e8470d3707 "Click to open in new window")

  NASA Software Architecture Review Board, February 9, 2011,  Supplemental checklist for reference architectures.
* (SWEREF-487)

  [IEEE Computer Society, “Systems and software engineering — Architecture description,”](http://www.iso-architecture.org/ieee-1471/ "Click to open in new window")

  ISO/IEC/IEEE 42010:2011, 2011. Accessed at 10:19 on August 27, 2015 from http://www.iso-architecture.org/ieee-1471/.
* (SWEREF-557)

  [MER Spirit Flash Memory Anomaly (2004)](https://llis.nasa.gov/lesson/1483 "Click to open in new window")

  Public Lessons Learned Entry: 1483.
* (SWEREF-571)

  [NASA Study of Flight Software Complexity](https://llis.nasa.gov/lesson/2050 "Click to open in new window")

  Public Lessons Learned Entry: 2050.

### 5.2 Tools

  

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

  

### 5.3 Process Asset Templates

**SWE-143 Process Asset Templates**

Click on a link to download a usable copy of the template.

* (PAT-023 - )

  [PAT-023 - Preparing for a SARB Checklist](https://swehb.nasa.gov/download/attachments/116293679/Preparing%20for%20a%20SARB%20Checklist.docx?api=v2 "Click to open in new window")

  SWE-143, tab 3, Also in Topic 8.55 - Software Design Analysis, Tab 2.4
* (PAT-029 - )

  [PAT-029 - Software Architecture Review Board Checklist](https://swehb.nasa.gov/download/attachments/120848418/Software%20Architecture%20Review%20Board%20Checklist.docx?api=v2 "Click to open in new window")

  8.55 - Software Design Analysis, tab 2.4.2, Also in SWE-143
* (PAT-030 - )

  [PAT-030 - SARB Review Checklist with Guidance](https://swehb.nasa.gov/download/attachments/120848457/SARB%20Review%20Checklist%20with%20Guidance.docx?api=v2 "Click to open in new window")

  Topic 8.55 - Software Design Analysis, Tab 2.4.2Also, in Category: DesAn
* (PAT-036 - )

  [PAT-036 Software Architecture and Design Process Audit](https://swehb.nasa.gov/download/attachments/198770701/PAT-036%20-%20Architecture%20and%20Design%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Architecture and Design.
* (PAT-045 - )

  [PAT-045 - Software Peer Review Inspection Report Audit](https://swehb.nasa.gov/download/attachments/198770772/PAT-045%20-%20Software%20Peer%20Review%20Inspection%20Report%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Peer Review Inspection Report Process.
* (PAT-047 - )

  [PAT-047 - Architecture and Detailed Design Assessment](https://swehb.nasa.gov/download/attachments/198770765/PAT-047%20-%20Architecture%20and%20Detailed%20Design%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Architecture and Detailed Design in the Software Design Description document. Based on the minimum recommended content for a Software Design Description.
* (PAT-048 - )

  [PAT-048 - Interface Design Description Assessment](https://swehb.nasa.gov/download/attachments/198770866/PAT-048%20-%20Interface%20Design%20Description%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Interface Design Description document. Based on the minimum recommended content for an Interface Design Description.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

This section includes an enhanced explanation and added context for existing lessons learned, as well as additional NASA Lessons Learned related to the importance of software architecture reviews. These lessons emphasize the role of architectural analysis and proactive reviews in mitigating risks, reducing complexity, and ensuring mission success.

---

### **1. MER Spirit Flash Memory Anomaly (2004) – Lesson Learned 1483**

**Summary of Incident:**  
Shortly after the start of science activities on Mars, the MER (Mars Exploration Rover) Spirit encountered a critical anomaly in its flight software. The rover lost the ability to perform tasks that required memory from the onboard flight computer. This failure was traced to **misconfigured parameters in two COTS (Commercial Off-The-Shelf) operating system software modules**, which controlled file storage in system and flash memory. This issue revealed weaknesses in the software architecture's handling of system resources and internal behaviors.

**Key Contributing Factors:**

1. Incorrect configuration parameters in software modules.
2. Insufficient architectural safeguards for managing memory.
3. Complex directory and file system structures that the architecture did not adequately validate or test.

**Recommendations (Lessons Learned):**

* Enforce design guidelines for integrating and configuring COTS software components to ensure they meet system requirements.
* Verify assumptions about software behavior in architectural planning and analysis.
* Maintain and prioritize lists of potential lower priority software risks or action items before system deployment.
* Develop comprehensive suites of tests, including tests specifically targeting internal flight software functions.
* Create automated analysis tools to track critical architectural elements such as memory use, resource allocation, and module interactions.
* Implement detailed telemetry and downlinked data to monitor the health, use, and state of system resources.
* Avoid complex or problematic file systems in software architectures where possible, particularly in resource-constrained systems, such as spacecraft.

**Relevance to Software Architecture Reviews:**  
This lesson highlights the necessity of validating architectural assumptions about memory management, COTS software behavior, and resource handling during **software architecture reviews.** Reviews must include:

* The evaluation of integration risks associated with COTS components.
* Simulated or scenario-based analysis of resource-intensive operations.
* Early identification of potential failure points in how the architecture handles resources.

---

### **2. NASA Study of Flight Software Complexity (2009) – Lesson Learned 2050**

**Summary of Study:**  
NASA conducted an in-depth study of flight software complexities after encountering recurring development problems across multiple projects. The study revealed that accelerating software size and growing architectural complexity created major obstacles for system performance, maintainability, and testing. These challenges often led to costly project delays and rework.

**Key Findings:**

* A significant percentage of failures were traced to insufficient investment in early architecture design and analysis.
* Lack of dedicated architectural expertise and a formal governance process contributed to downstream implementation issues.
* Projects underestimated the consequences of complex and tightly coupled designs, resulting in reduced testing effectiveness.

**Recommendations (Lessons Learned):** The study provided the following actionable recommendations for mitigating software complexity:

1. **Increase Investment in Up-Front Architecture Analysis:**  
   Allocate a larger percentage of project budgets toward early architectural planning, risk analysis, and validation. This would result in long-term project cost savings by preventing integration problems and late design errors.
2. **Expand the Role of Software Architects:**  
   Increase the number of skilled software architects on projects and give them greater decision-making authority. Skilled architects are critical for ensuring decisions align with long-term project goals, safety, and mission assurance.
3. **Establish Professional Architecture Review Boards (ARBs):**  
   Create formalized, independent boards to conduct early-stage software architecture reviews. ARBs should provide constructive and informed feedback to improve architectural quality, identify risks, and deliver recommendations before significant implementation begins.

**Relevance to Software Architecture Reviews:**  
This lesson underscores the importance of a structured and continuous approach to architectural reviews, including:

* Early investment in architecture ensures fewer issues emerge during the development lifecycle.
* Independent reviews by ARBs provide an additional layer of assurance and accountability.
* Decision authority for architects is essential for addressing complexity and aligning architecture with project objectives.

---

### **3. Mars Climate Orbiter Failure (1999) – Lesson Learned 0641**

**Summary of Incident:**  
The Mars Climate Orbiter was lost due to a software error arising from a mismatch between metric and imperial units. This error was rooted in poor architectural oversight and the lack of a unified system for managing unit conventions across software and hardware.

**Key Contributing Factors:**

* Insufficient architectural governance to enforce standards across subsystems.
* Lack of rigorous validation during software and systems integration.
* Absence of cross-team communication and understanding of underlying assumptions across architectural components.

**Recommendations (Lessons Learned):**

* Establish system-wide architecture-level standards to align all teams on critical attributes such as units, data conventions, and assumptions.
* Include unit validation as part of integration and architecture reviews to prevent mismatches between software components.
* Improve cross-disciplinary communication to ensure alignment of architectural assumptions between software, hardware, and ground systems.

**Relevance to Software Architecture Reviews:**  
This incident highlights the importance of architecture reviews as an opportunity to:

* Validate standardized conventions and assumptions across the system early in the lifecycle.
* Assess integration risks caused by ill-defined internal and external interfaces.
* Ensure complete communication coverage between engineering disciplines.

---

### **4. International Space Station (ISS) Software Integration Delays (2008) – Lesson Learned 1586**

**Summary of Lessons Learned:**  
The ISS software development suffered extensive delays due to insufficient architectural planning and poorly managed integration risks. The complexity of integrating software components developed by teams from multiple international partners caused compatibility and performance issues.

**Key Contributing Factors:**

* Inadequate architectural support for managing software developed across multiple teams and nations.
* Misaligned interfaces and mismatches in data handling protocols between subsystems.
* Late identification of integration and compatibility issues.

**Recommendations (Lessons Learned):**

* Ensure architecture reviews capture and validate integration points between all subsystems, particularly in multi-team projects.
* Define precise internal and external interfaces early in the lifecycle and enforce their consistent use.
* Perform incremental integration testing to reduce late-stage surprises and validate subsystem interoperability before large-scale integration.

**Relevance to Software Architecture Reviews:**  
This emphasizes the role of architecture reviews in large, distributed projects:

* Focus reviews on validating well-defined interfaces, protocols, and data flow paths.
* Identify and mitigate risks associated with integrating components developed by different teams or entities.
* Ensure architectural documentation is clear, centrally stored, and accessible across team boundaries.

---

### **5. Orbital Maneuvering System Software (1981) – Lesson Learned 0070**

**Summary of Incident:**  
A significant software bug in the Space Shuttle’s Orbital Maneuvering System caused a malfunction during testing due to inadequate fault tolerance mechanisms in the software. The missing fault tolerance features could have jeopardized the mission had the error occurred during flight.

**Key Contributing Factors:**

* No architectural redundancy or mechanisms to detect and recover from faults.
* Failure to anticipate and mitigate system-level risks during architectural design.
* Insufficient testing of architectural failure scenarios.

**Recommendations (Lessons Learned):**

* Incorporate fault tolerance mechanisms (e.g., error monitoring, redundancy, recovery protocols) into the software architecture as early as possible.
* Assess architecture safety risks and verify their mitigation through architecture reviews and fault simulations.
* Test software against failure scenarios to validate architectural fault-handling capabilities.

**Relevance to Software Architecture Reviews:**  
Architecture reviews should explicitly evaluate:

* Fault tolerance mechanisms at the architectural level.
* Safety-critical subsystems for resilience and error recovery.
* Potential fault propagation risks across architectural boundaries.

---

### **Conclusion**

NASA’s Lessons Learned database demonstrates that software architecture reviews are critical for managing complexity, mitigating risks, and ensuring mission success. From the MER Spirit anomaly to the Mars Climate Orbiter failure, these lessons emphasize the importance of early, rigorous, and independent architectural analysis. By incorporating targeted recommendations like enforcing COTS guidelines, validating interfaces, testing fault tolerance, and establishing architecture review boards, projects can significantly improve the quality and resiliency of their software architectures.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-143 - Software Architecture Review**

4.2.4 The project manager shall perform a software architecture review on the following categories of projects:

a. Category 1 Projects as defined in NPR 7120.5.  
b. Category 2 Projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess the results of or participate in software architecture review activities held by the project.

## 7.2 Software Assurance Products

Software Assurance ensures the software architecture is capable of meeting mission needs, safety requirements, and quality expectations. Key outputs of software assurance activities for architecture reviews include:

#### **Key Artifacts:**

1. **Software Architecture Review Assessment Report:**

   * Assessment of the adequacy of the architecture against allocated requirements, system goals, and identified quality attributes.
   * Confirmation of architectural compliance with NASA standards and guidelines.
   * Findings summarizing strengths, weaknesses, risks, and areas for improvement.
2. **Software Assurance Status Report:**

   * Summary of SA participation in architecture review meetings, including key issues observed and their status.
   * Open and resolved risks or non-conformances related to the software architecture.
3. **Assessment of Architecture Review Results:**

   * Independent evaluation of the outcomes from software architecture reviews (e.g., adherence to defined objectives and resolution of identified concerns).
   * Adequacy of corrective actions to address issues raised in architecture reviews.
4. **Risk and Issue Log Related to Architecture:**

   * Identified architectural risks and issues (e.g., complexity, performance impact, safety gaps).
   * Detailed analysis of how the architecture mitigates identified hazards.
5. **Software Design Analysis Results:**

   * Analysis confirming alignment of design decisions with the top-level software architecture.
   * Evaluation of architectural trade-offs and their long-term implications for safety, maintainability, and scalability.
6. **Review Findings and Resolution Status (if applicable):**

   * Items raised during architecture reviews and their closure status, with a timeline for addressing unresolved issues.

---

## 7.3 Metrics

Metrics provide feedback on the quality of the architecture and the effectiveness of the review process. Relevant metrics include:

1. **Architectural Issues Identified vs. Resolved:**

   * Tracks the number of issues identified during reviews against the number successfully closed and tracks trends through the lifecycle.
2. **Non-Conformances from Reviews:**

   * Total count of architectural non-conformances identified, categorized as open vs. closed.
   * Measure the **average resolution time** (in days) for non-conformances.
3. **Architecture Risk Closure Rate:**

   * Percentage of identified architecture-related risks successfully mitigated within the established timeframe.
4. **Test Coverage of Architecture:**

   * Percentage of architectural components tested or prototyped to verify conformance with requirements and constraints.
5. **Review Findings and Follow-Up Rate:**

   * Number of review findings addressed within a specified period, ensuring minimal delays in resolving critical issues.

**Reference:** See *Topic 8.18 – SA Suggested Metrics* for additional measurement guidelines.

---

## 7.4 Guidance for Software Architecture Reviews

**Software Assurance (SA)** personnel and **Software Safety (SS)** experts contribute to the success of the software architecture by evaluating it critically to ensure quality, safety, and compliance with standards. This section provides structured guidance for conducting software architecture reviews.

---

#### **1. SA and SS Participation During Reviews**

* Participate actively in the formulation and review of the architecture throughout its development lifecycle.
  + Ensure reviews occur **before the software Preliminary Design Review (PDR)** to allow for early corrections.
  + Advocate for **early involvement** of the architecture review board, as earlier inputs prevent reworks and reduce downstream risks.

#### **2. Use of Architecture Review Checklists**

Ensure the following checklist items are part of every software architecture review:

1. **General Questions:**

   * Are the architectural requirements clearly defined?
   * Can the architecture fulfill allocated system requirements?
   * Are previously implemented architectures (both successful and unsuccessful) reviewed to build lessons learned into the design?
2. **Requirements and Quality Attributes Verification:**

   * Has the project identified system requirements driving the architecture design?
   * Have **all stakeholders** been involved in defining user needs, operating constraints, and mission goals?
   * Are relevant **quality attributes** (e.g., reliability, fault tolerance, scalability) identified, prioritized, and addressed?
3. **Source and Component Analysis:**

   * Are the sources of all software components (new, reused, heritage, and COTS) explicitly defined?
   * Is a rationale provided for architectural decisions such as COTS vs. custom-built?
4. **Documentation and Traceability:**

   * Is the architecture sufficiently documented for future reference, maintainability, reuse, or upgrades?
   * Is each subsystem and its dependency clearly defined, traceable, and understandable?
5. **Risk Evaluation:**

   * Have fault management approaches been defined and validated against architectural objectives?
   * Does the architecture induce unnecessary complexity, making failure modes or runtime behavior less predictable?
6. **Performance Evaluation and Future Readiness:**

   * Does the architecture meet performance requirements (e.g., throughput, processing rates, and bandwidth)?
   * Is the architecture scalable and reusable for future extensions of the system, mission, or project?
7. **Safety-Critical Attributes and Hazards:**

   * Have safety-critical components been identified, traced, and aligned with hazard analysis results?
   * Are appropriate fault recovery strategies and monitoring mechanisms (e.g., health monitoring, watchdogs) integrated?

---

#### **3. Architectural Design Considerations**

Ensure that the review investigates architectural design principles, rules, and critical attributes, including but not limited to:

* Patterns, abstractions, and algorithms.
* Resource management (e.g., data management, memory, CPU utilization).
* Concurrency and synchronization (e.g., threads, inter-process communication).
* Real-time execution and latency considerations.
* Verification and validation methods to confirm compliance with requirements.

---

#### **4. Documentation Standards**

Ensure that the architectural concept is recorded with at least the following:

1. **Architectural Alternatives:**
   * Assessment and comparison of design alternatives with their trade-offs.
2. **Chosen Architecture Description:**
   * Clear and complete documentation of the selected architecture, including diagrams and rationale.
3. **Decomposition and Dependencies:**
   * Subsystem breakdown, with clear dependencies defined between components.
4. **Risk Evaluation:**
   * Analysis of risks inherent in the chosen architecture and mitigation strategies.

**Evaluate Documentation:** Confirm that the format is **clear, understandable, and standardized** for future reference.

---

#### **5. Addressing Weak Architecture Risks**

* Weak architecture should be identified early during **architecture formulation**—it can result in:
  + **Inflexibility to Change:** Errors become costly and risky to fix during later phases.
  + **Poor Reusability:** Architecture cannot be leveraged for future missions.
  + **Reduced Confidence:** Neither testing nor operations fully validate unstructured designs.

**Software Assurance Response:**

* Advocate for well-defined subsystems, minimal complexity, and alignment with modern best practices in software architecture (e.g., modularity, isolation).
* Ensure the architecture provides clear pathways for **testing, verification, and validation.**

---

### **Confirming the Scope of Reviews**

1. Software architects must ensure that designs align with mission needs while balancing complexity and constraints.
2. Projects must treat software architecture as **iterative**—not a one-time task.
3. Make architecture a **long-term asset** that drives disciplined implementation, testing, and operational planning.
4. Document emerging issues during the architecture review and ensure added risks are adequately addressed and overseen in subsequent updates.

---

### **Conclusion**

The software architecture review allows SA teams to reduce architectural risks, verify quality attributes, and ensure alignment with system goals. Early involvement in the formulation phase, supported by well-structured checklists and metrics, ensures that review findings will provide actionable inputs to the project. Robust documentation, architectural alternatives, and risk management are critical for ensuring safety, maintainability, and scalability across the lifecycle.

By integrating lessons learned and structured review practices, NASA missions can achieve architectures that ensure long-term reliability, adaptability, and mission success.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)        * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-023 - Preparing for a SARB Checklist](/spaces/SITE/pages/116293679/PAT-023+-+Preparing+for+a+SARB+Checklist) * [PAT-029 - Software Architecture Review Board Checklist](/spaces/SITE/pages/120848418/PAT-029+-+Software+Architecture+Review+Board+Checklist) * [PAT-030 - SARB Review Checklist with Guidance](/spaces/SITE/pages/120848457/PAT-030+-+SARB+Review+Checklist+with+Guidance) |

# 8. Objective Evidence

Objective Evidence

**Objective evidence** refers to documented, verifiable materials that demonstrate compliance with the requirements of a software architecture review for applicable software lifecycle phases. Below are examples of **good objective evidence** for Requirement 4.2.4 categorized by **planning, execution, findings, and closure** to align with review activities and outcomes.

---

### **1. Evidence of Software Architecture Review Planning**

#### **1.1 Review Plan and Procedures**

* **Artifact:** A **Software Architecture Review Plan** (or integrated software lifecycle review plan).
  + Describes the purpose, scope, schedule, and participants of the review, aligning with the project's risk classification.
  + Specifies entry/exit criteria, deliverable requirements, and what constitutes review success.
  + Compliance references to NPR 7120.5, NPR 7150.2, and NPR 8705.4, if applicable.

#### **1.2 Review Schedule**

* **Artifact:** A detailed schedule showing when software architecture reviews are planned relative to project milestones (e.g., before the Software Preliminary Design Review (PDR)).
  + Evidence of alignment with major lifecycle checkpoints for Category 1 and Class A/B Category 2 projects.

#### **1.3 Review Checklists**

* **Artifact:** **Software Architecture Review Checklists** that specify review criteria and focus areas:
  + Stakeholder requirements traceability to architectural components.
  + Risk management (e.g., fault tolerance strategies, hazardous software behaviors).
  + Quality attributes (safety, scalability, maintainability).
  + Compliance with standards, including NASA-specific requirements (e.g., SWE-057).

---

### **2. Evidence of Software Architecture Review Execution**

#### **2.1 Review Meeting Records**

* **Artifact:** Review event documentation (e.g., **meeting agendas, minutes, attendance lists**) indicating that:
  + The required stakeholders participated (e.g., software assurance, software architect(s), systems engineering, safety, mission assurance teams).
  + The review included discussions of system architecture, key design decisions, and quality attributes.
  + Respective questions raised during the review were addressed.

#### **2.2 Architecture Artifacts Presented**

* **Artifacts:** Records of architecture artifacts submitted for review, such as:
  + **Software Architecture Description Document (SWE-057):**
    - High-level architecture diagrams (e.g., component diagrams, data flow diagrams).
    - Subsystem decomposition and dependency maps.
    - Interfaces definition documents (both internal and external).
    - Descriptions of fault management mechanisms and redundancy to handle failure scenarios.
  + **Traceability Matrices:**
    - Linking architectural components to system/software requirements, safety-critical requirements, and hazard analyses.
  + **Alternatives Analysis Report:**
    - Description of evaluated architectural solutions, justifications for the selected solution, trade-offs, and performance impacts.

#### **2.3 Risk Assessment Evidence**

* **Artifacts:** Risk analysis and architecture-specific risk logs:
  + Evidence of identified architectural risks, such as scalability limitations, performance bottlenecks, integration concerns, or software safety issues.
  + Risk mitigation plans, strategies, and initial closure status (e.g., plans to address fault-prone areas such as COTS integration).
  + Safety-critical hazard assessments linking hazards to software architecture elements.

---

### **3. Evidence of Findings from Software Architecture Reviews**

#### **3.1 Review Results and Reports**

* **Artifacts:** **Software Architecture Review Results Document** summarizing:
  + Strengths, risks, and weaknesses of the proposed architecture.
  + Compliance with allocated system/software requirements and NASA standards.
  + Final assessment of the architecture’s readiness to proceed to the next phase (e.g., Software PDR).
  + Actions to address identified gaps in the architecture.

#### **3.2 Action Item Summary**

* **Artifacts:** **Action Item and Issue Log:**
  + Open and closed action items/tracking records from review meetings.
  + Resolutions for identified deficiencies, including deadlines and accountability.
  + Cross-referencing of corrective actions with risks identified in related hazard or safety analyses.

#### **3.3 Metrics Evidence**

* **Artifacts:** Metrics tracking data:
  + Number of architectural issues identified vs. issues resolved at project checkpoints.
  + Schedule compliance for closing non-conformances or risks emerging during the review.
  + Number of quality attributes validated in architecture evaluation compared to those missed or postponed.

---

### **4. Evidence of Closure and Follow-Up**

#### **4.1 Corrective Action Evidence**

* **Artifacts:** Risk/issue closure documentation:
  + Evidence showing that all review findings were either resolved, mitigated, or accepted with justification prior to entering the next lifecycle phase.
  + Results of re-evaluated architecture following updates made in response to review feedback.

#### **4.2 Configuration Management Evidence**

* **Artifacts:** Configuration management records confirming:
  + Approved architecture baseline, post-review updates, and archival of deliverables.
  + Traceable documentation from the review process stored in the project repository for future use.

#### **4.3 Safety Assurance Follow-Up**

* **Artifacts:** Safety verifications:
  + Documentation verifying that safety-critical elements evaluated in the architecture review align with the corresponding hazard analyses, fault tolerance designs, and operational safety requirements.

---

### **Summary of Good Objective Evidence**

The following artifacts collectively demonstrate compliance with Requirement 4.2.4:

1. **Planning Documentation:**
   * Review plans, schedules, and stakeholder engagement strategies.
2. **Review Execution Records:**
   * Meeting minutes, architecture baselines, risk lists, and alternatives analysis.
3. **Review Findings:**
   * Risk assessments, traceability documents, and reports summarizing strengths, weaknesses, and corrective actions.
4. **Metrics and Closure:**
   * Metrics tracking resolution rates, corrective action tracking logs, and evidence of post-review updates to architecture documents.

---

### **Final Note**

Good objective evidence ensures that software architecture reviews are not just a compliance formality but a constructive and proactive process. These artifacts enable auditors, stakeholders, and project teams to trace decisions, successes, and risks, ensuring that the architecture is capable of meeting the mission’s goals, safety standards, and operational constraints.

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
