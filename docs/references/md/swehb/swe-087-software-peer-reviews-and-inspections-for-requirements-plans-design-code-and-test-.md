# SWE-087 - Software Peer Reviews and Inspections for Requirements Plans Design Code and Test Procedures

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695472. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures

SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695472)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695472&showCommentArea=true&showComments=true#addcomment)

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

5.3.2 The project manager shall perform and report the results of software peer reviews or software inspections for: 

a. Software requirements.  
b. Software plans, including cybersecurity.  
c. Any design items that the project identified for software peer review or software inspections according to the software development plans.  
d. Software code as defined in the software and or project plans.  
e. Software test procedures.

## 1.1 Notes

Software peer reviews or software inspections are recommended best practices for all safety and mission-success related software components. Recommended best practices and guidelines for software formal inspections are contained in NASA-STD-8739.9, Software Formal Inspection Standard.[277](#_tabs-<p></p>)

## 1.2 History

Click here to view the history of this requirement: SWE-087 History

SWE-087 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.3.1 The project shall perform and report on software peer reviews/inspections for:   1. 1. Software requirements.    2. Software Test Plan.    3. Any design items that the project identified for software peer review/inspections according to the software development plans.    4. Software code as defined in the software and or project plans. |
| Difference between A and B | Added item e. Software test procedures to the requirement.  Broadened the scope of the plans to be reviewed to include all Plans, not just the Test Plan. |
| B | 5.3.2 The project manager shall perform and report the results of software peer reviews or software inspections for:   1. 1. Software requirements.    2. Software plans.    3. Any design items that the project identified for software peer review or software inspections according to the software development plans.    4. Software code as defined in the software and or project plans.    5. Software test procedures. |
| Difference between B and C | No change |
| C | 5.3.2 The project manager shall perform and report the results of software peer reviews or software inspections for:   1. 1. Software requirements.    2. Software plans.    3. According to the software development plans, any design items that the project identified for software peer review or software inspections.    4. Software code as defined in the software and or project plans.    5. Software test procedures. |
| Difference between C and D | Added cybersecurity plans to part b. |
| D | 5.3.2 The project manager shall perform and report the results of software peer reviews or software inspections for:   a. Software requirements. b. Software plans, including cybersecurity. c. Any design items that the project identified for software peer review or software inspections according to the software development plans. d. Software code as defined in the software and or project plans. e. Software test procedures. |

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
| * [A.10 Software Peer Reviews and Inspections](/spaces/SWEHBVD/pages/133235386/A.10+Software+Peer+Reviews+and+Inspections) |

# 2. Rationale

Software peer reviews or inspections are performed to ensure product and process quality, add value, and reduce risk through expert knowledge infusion, confirmation of approach, identification of defects, and specific suggestions for product improvements.

Requirement 5.3.2 mandates the performance and reporting of software peer reviews or inspections for critical software artifacts, including requirements, plans, design, code, and test procedures. These peer reviews or inspections are an integral part of verifying software work products’ quality, detecting defects early, ensuring compliance with standards, and addressing risks before they lead to significant issues like rework, schedule delays, cost overruns, or mission failure.

Peer reviews are essential checkpoints throughout the software development lifecycle, serving as a systematic and structured way to ensure software integrity, reliability, and adherence to project goals, particularly in NASA's high-stakes environments.

---

### **Why This Requirement is Important**

1. **Defect Prevention and Early Detection:**

   * Software peer reviews are proven mechanisms for identifying defects early in the development lifecycle. Multiple studies show that the earlier defects are identified, the lower the cost and effort required to correct them. For example:
     + Defects found during peer reviews in the requirements or design phases are significantly less expensive to fix than those discovered during testing or operations.
     + NASA statistics from previous projects demonstrate that on average, **60-90% of defects** can be detected during substantive peer inspections.
2. **Improved Quality and Reliability:**

   * NASA missions rely on software systems functioning as intended because of the mission-critical nature of operations (e.g., deep space, crew safety, planetary exploration). Peer reviews improve software quality and reduce the likelihood of errors propagating to later stages.
   * Peer reviews foster alignment between engineering, assurance, mission requirements, and system-level objectives.
3. **Verification of Compliance:**

   * Peer reviews help ensure alignment between software artifacts (requirements, design, code, and tests) and industry or NASA-specific standards, including safety-critical and cybersecurity requirements.
   * They confirm that the work products meet both functional and non-functional requirements, especially when meeting NASA's unique system standards.
4. **Risk Mitigation and Safety Assurance:**

   * Unreviewed artifacts can lead to latent errors that evolve into significant risks during later lifecycle phases, including launch, operation, and decommissioning.
   * Peer reviews offer the opportunity to mitigate risks before defects manifest in critical mission phases.
   * For example, overlooked cybersecurity gaps in software plans may leave systems vulnerable to external threats or internal breaches.
5. **Ensuring Thoroughness:**

   * Peer inspections provide a structured framework for evaluating technical completeness, accuracy, and logical coherence of software work products.
   * Such diligence ensures nothing is overlooked or assumed during development, especially in complex, multidisciplinary software projects.
6. **Team Collaboration and Knowledge Sharing:**

   * Peer reviews foster collaboration and shared understanding of project goals, design decisions, implementation, and testing approaches.
   * They encourage cross-functional input, enabling team members with diverse expertise to identify concerns and suggest improvements.
   * This collaboration reduces reliance on an individual developer's knowledge and increases the overall team accountability for quality.
7. **Transparency and Traceability:**

   * Reporting the results of peer reviews ensures that all relevant stakeholders are aware of the findings, decisions, and actions identified during reviews.
   * Traceability improves by documenting the artifacts reviewed, findings from the peer review process, and subsequent actions taken to address the findings.
8. **Cost and Schedule Containment:**

   * Peer reviews help catch issues early, reducing costly late-phase fixes that can snowball into extended delays or even mission redesign.
   * Early defect detection helps preserve both budget and schedule containment by minimizing cascading effects on dependent tasks.

---

### **Rationale for Performing Peer Reviews/Inspections by Artifact**

#### **a. Software Requirements:**

**Why Review Requirements?**

* Software requirements are the foundation upon which the entire software system is built. Errors in requirements propagate throughout the development lifecycle, leading to defects in design, code, and testing. For example, ambiguous or poorly defined requirements can result in code that does not meet mission-critical needs.
* Peer reviews ensure that software requirements:
  + Are clear, specific, and measurable.
  + Align with system and mission requirements.
  + Are free from contradictions or ambiguities.
  + Include non-functional requirements such as performance, scalability, and cybersecurity.

#### **b. Software Plans (Including Cybersecurity):**

**Why Review Plans?**

* Software plans (e.g., Software Development Plan, Risk Management Plan, Software Assurance Plan) document the approach for building, testing, managing, and maintaining the software.
* Errors or gaps in these plans can lead to misaligned execution, missed risk mitigations, and non-conformance to project goals.
* Cybersecurity plans, in particular, require detailed peer reviews to ensure resilience against internal and external threats, compliance with NASA's cybersecurity standards, and thorough risk management.

---

#### **c. Design Items Defined for Peer Review:**

**Why Review Design?**

* Design is the roadmap for how the software will be implemented. Poor design decisions lead to implementation inefficiencies, technical debt, and increased risks of system failure.
* Design reviews verify:
  + Logical and structural coherence with the requirements.
  + Completeness and quality of software architecture, algorithms, and component interfaces.
  + Scalability, maintainability, testability, and performance considerations.

#### **d. Code as Defined in Software and Project Plans:**

**Why Review Code?**

* Code review ensures that the implementation not only adheres to the requirements and design but also follows proper coding standards, practices, and quality benchmarks.
* Unreviewed code can introduce defects, vulnerabilities, and inefficiencies. Inspections:
  + Detect logic errors, non-conformances, and inefficiencies.
  + Ensure adherence to coding standards (e.g., MISRA or NASA-specific guidelines).
  + Strengthen cybersecurity by eliminating vulnerabilities such as injections or buffer overflows.

---

#### **e. Software Test Procedures:**

**Why Review Test Procedures?**

* The thoroughness of software test plans and procedures significantly impacts the ability to detect defects before deployment.
* Peer review of test plans ensures:
  + Test coverage aligns with software requirements (traceability).
  + Test cases address nominal and off-nominal conditions, boundary values, and failure modes.
  + Adequate focus on verification of safety-critical and mission-critical functions.
  + The inclusion of cybersecurity testing in sensitive software systems.

---

### **The Role of Reporting Results**

Documenting and reporting the results of peer reviews provides several critical benefits:

1. **Accountability and Transparency:**

   * Ensures all findings and decisions are clearly recorded and accessible to stakeholders.
   * Tracks how peer review observations are resolved.
2. **Continuous Improvement:**

   * Enables the team to identify patterns in recurring errors and enact process improvements to prevent them in the future.
3. **Compliance Checkpoint:**

   * Provides assurance that the project adheres to NASA’s standards and guidelines for peer reviews (NPR 7150.2) and risk management.
4. **Audit Readiness:**

   * Ensures peer reviews can be referenced during software assurance or external audit processes.

---

### **Conclusion**

Requirement 5.3.2 underscores the importance of peer reviews as a critical quality management activity throughout the software lifecycle. By systematically conducting and documenting peer reviews for software requirements, plans, design, code, and testing, projects can identify and resolve defects early, enhance software quality and reliability, and safeguard mission success. For NASA’s high-stakes missions, where failure is not an option, disciplined peer reviews form an indispensable line of defense in ensuring mission-critical software meets its objectives.

**NPR 7123.1D - NASA Systems Engineering Processes and Requirements (w/Change 1)**

G.20 Peer Reviews  
“Peer reviews are focused, in-depth technical reviews that support the evolving design and development of a product, including critical documentation or data packages. The participants in a peer review are the technical experts and key stakeholders for the scope of the review.”[041](#_tabs-<p></p>)

# 3. Guidance

Peer reviews are among the most effective mechanisms for improving software quality and reducing lifecycle costs by identifying defects early. Rooted in thorough collaboration and disciplined processes, peer reviews not only uncover technical deficiencies but also enhance team-wide communication and understanding. The following revised guidance refines the current recommendations and best practices for conducting effective software peer reviews.

---

### **3.1 Peer Review Defined**

NASA-STD-8709.22 provides dual definitions for peer reviews, emphasizing structured and systematic evaluations of software artifacts. These definitions focus on:

1. **Technical Review by Peers:** A review of a software work product using defined procedures, conducted by peers of the product’s creators, to identify defects and provide feedback for improvements.
2. **Independent Expert Review:** A focused evaluation by internal or external subject matter experts without vested interest in the product being reviewed, creating an unbiased corrective mechanism that can complement peer perspectives.

Peer reviews are proactive reviews of specific work products, taking place before those artifacts move forward to key milestones or approval cycles. They follow **planned, disciplined processes** that include:

* Preparation,
* Conducting the review,
* Analyzing outcomes,
* Resolving defects found, and
* Implementing corrective actions.

---

#### **Why Peer Reviews Matter Early in Development**

A key advantage of software peer reviews is their ability to validate critical artifacts — such as requirements, plans, design elements, code, and test procedures — long before testing begins. This makes peer reviews one of the few **early-stage Verification & Validation (V&V) options** to address potential defects before costly downstream fixes occur. For example:

* Reviews of requirements documents reduce ambiguities or incorrect assumptions early.
* Defects that are caught early (e.g., in requirements or design) are exponentially cheaper to fix than defects caught during implementation or system-level testing.

Peer reviews are a required part of sound engineering practice, especially for requirements documents. Furthermore, NASA has found that rigorous peer reviews enhance communication across technical teams and stakeholders while delivering measurable improvements in software success rates.

**NASA-STD-8709.22**

NASA-STD-8709.22 provides two definitions for peer reviews.

[1] A review of a software work product, following defined procedures, by peers of the product producers to identify defects and improvements.

[2] Independent evaluation by internal or external subject matter experts who do not have a vested interest in the work product under review. Projects can plan peer reviews, and focused reviews conducted on selected work products by the producer’s peers to identify defects and issues before that work product moves into a milestone review or approval cycle.[274](#_tabs-<p></p>)

## 3.2 Advantages of Peer Reviews

#### **3.2.1 Stakeholder Buy-In**

Software plans, such as the Software Development Plan (SDP), are strategic documents critical to project success. Plans peer-reviewed with **stakeholder involvement**:

* Establish credibility and accountability for team members involved in project execution.
* Reduce risks of misaligned objectives, dependencies, or misinterpretations by ensuring all stakeholders have visibility and influence in improving key deliverables.

Thorough peer reviews of software plans improve buy-in and alignment, ensuring that all parties are equipped to meet project goals while maintaining technical rigor and compliance.

#### **3.2.2 Improving Software Quality**

Peer reviews enhance software quality by:

* Ensuring test procedures address **functionality, edge cases, and off-nominal conditions**, yielding comprehensive coverage for verification activities.
* Validating critical software test behavior or expectation mismatches before tests are executed, improving downstream efficacy.

While automated testing plays a key role, **human judgment in peer reviews extends deeper into context, clarity, and intent**—particularly where manual reviews are appropriate (e.g., assessing design or mission-critical code functionality).

##### **Code and Design Artifacts:**

* Even though testing and simulation techniques apply to design/code stages, a project must **prioritize peer reviews for high-risk items:**
  + Areas of high complexity, failure modes, and system-critical functions.
  + Segments related to safety-critical design or cybersecurity considerations.

Efficient peer reviews help prioritize manual review where automation cannot accommodate qualitative decisions, such as solution modularity, safe error handling, and maintainability.

## 3.3 Additional Benefits

Peer reviews deliver measurable benefits beyond defect detection and corrective actions:

1. **Applicable to Any Software Work Product:** Peer reviews are beneficial not only for requirements and code but also for plans and other system-level documents.
2. **Enhances Knowledge Sharing:** By bringing together different participants, peer reviews foster collaboration, spreading best practices across disciplines.
3. **Reduces Latent Risk:** Early identification of issues lowers defect escape rates, reducing costly rework late in the project lifecycle.
4. **Improves Team Cohesion:** Peer reviews align understanding across diverse team members, ensuring unified perspectives on deliverables.
5. **Promotes Continuous Improvement:** By tracking and analyzing peer review outcomes, teams can refine the process, reducing defects over time.

Peer reviews provide the following additional benefits:

|  |  |
| --- | --- |
| Useful for many types of products: documentation, requirements, designs, code | Simple to understand |
| Provide a way for sharing/learning good product development techniques | Serve to bring together human judgment and analysis from diverse stakeholders in a constructive way |
| This can result in a very efficient method of identifying defects early in the product’s life cycle | Use a straightforward, organized approach for evaluating a work product  -          To detect potential defects in a product  To methodically evaluate each defect to identify solutions and track the incorporation of these solutions into the product |

## 3.4 Preparing for Peer Reviews

#### **3.4.1 Peer Review Process Essentials**

When conducting peer reviews, adhere to the following principles:

* Focus on the **technical integrity** and quality of the work product, avoiding subjective or non-constructive criticism.
* Keep reviews structured but efficient. Establish specific objectives and provide preparation time for reviewers to understand the product under review.
* Leverage **checklists.** Specific checklists improve focus and consistency for evaluating documents, design, or code.

##### **Key Process Elements:**

* Use **readiness and completion criteria** to ensure the review is timely, purposeful, and conclusive.
* Develop an inspection strategy tailored to the type of work product, emphasizing defect detection.
* Plan reviews for **round-table collaboration,** not presentations, to foster open communication.
* Capture **action items** comprehensively, managing findings and ensuring corrective actions are implemented.

#### **3.4.2 Checklist Highlights for Work Products**

A tailored checklist should accompany each peer review. Examples include:

* **Requirements:** Traceability, correctness, completeness, verifiability, and alignment with system-level safety and reliability goals.
* **Code:** Logic correctness, adherence to standards, error-handling mechanisms, absence of latent errors (e.g., divide-by-zero, buffer overflows).
* **Test Plans:** Completeness, coverage per requirements, predefined expected outcomes, alignment with safety-critical verifications.

#### **3.4.3 Roles and Responsibilities**

Key roles and responsibilities ensure that the peer review process is collaborative, efficient, and free from bias. Best practices include:

* **Moderators:** Lead and sustain focus in the meeting without managerial bias.
* **Authors:** Clarify the artifact but do not dominate the review.
* **Peers (Inspectors):** Provide technical scrutiny while following process guidelines.

A diverse review team ensures that multiple perspectives (e.g., software, hardware, systems engineering) are accounted for to enhance product robustness.

When putting a software peer review team together, use the following best practices:

* The team consists of a minimum of four inspectors.  
  + Diverse viewpoints and objectivity are required.
* Inspection team members are based on the analysis of key stakeholders in the item under inspection.
* The author should not be the reader, recorder, or moderator.
* The moderator should not be a manager.
* At a minimum, the moderator should be formally trained in the process, but all participants may be trained.
* Management presence/participation discouraged.
* Each role has a specific responsibility, as shown in the table below:

|  |  |
| --- | --- |
| **Role** | **Responsibility** |
| **Moderator** | Conducts and controls the inspection |
| **Author** | The producer of the product under inspection, answers technical questions |
| **Reader** | Presents (reads, paraphrases) the inspection product to the inspection team |
| **Recorder** | Documents defects identified during the inspection as well as open issues and action items |
| **Software Peers** | Look for software and software coding defects in the product under inspection. |
| **Hardware Engineer(s)** | Look for defects in the product under inspection, and ensure software control of hardware is correct. |
| **System Engineer(s)** | Look for defects in the product under inspection, and ensure software control of the system is correct, including fault detection, fault isolation, and fault recoveries. |

---

#### **3.4.4 Best Practices**

* **Data-Driven Analysis:** Track metrics like defect trends by artifact type or inspection phase (e.g., planning, rework).
* **Review Limits:** Adhere to time-boxes such as keeping inspection meetings productive (e.g., under 2 hours).
* **Author Accountability Without Judgment:** Avoid using defects as a performance metric for authors. Instead, reinforce improvements in product quality.

Software peer reviews are conducted using the following steps:

|  |  |
| --- | --- |
| **Step** | **Description** |
| Planning | Organize inspection, inspection package contents, required support, and schedule. |
| Overview | Educational briefing at the time of package distribution to explain materials at a high level |
| Preparation | Inspectors individually look for and document defects and develop questions |
| Inspection Meeting | Inspectors examine the product as a group to classify and record defects and capture open issues and action items. |
| Third Hour | Optional informal meeting to resolve open issues and discuss solutions |
| Rework | The author corrects major defects (others when cost and schedule allow) |
| Follow-up | The moderator verifies all major and other dispositioned defects have been corrected; no new defects introduced; and all action items/open issues are closed. |

### 3.4.5 Entrance and Exit Criteria

The table below is from the NASA System Engineering Processes and Requirements, NPR 7123.1, and shows the entrance criteria and success criteria for a peer review activity.

**Table G-19 - Peer Review Entrance and Success Criteria**

|  |  |
| --- | --- |
| **Peer Review** | |
| **Entrance Criteria** | **Success Criteria** |
| 1. The product to be reviewed (e.g., document, process, model, design details) has been identified and made available to the review team. 2. Peer reviewers independent from the project have been selected for their technical background related to the product being reviewed. 3. A preliminary agenda, success criteria, and instructions for the review team have been agreed to by the technical team and project manager. 4. Rules have been established to ensure consistency among the team members involved in the peer-review process. 5. \*Spectrum (radio frequency) considerations addressed. | 1. Peer review has thoroughly evaluated the technical integrity and quality of the product. 2. Any defects have been identified and characterized. 3. The results of the peer review are communicated to the appropriate project personnel. 4. Spectrum-related aspects have been concurred on by the responsible Center spectrum manager. 5. A code peer review checks to verify that the code meets the software requirements |

\*Required per NPD 2570.5.

## 3.5 Required Peer Reviews by Artifact

Peer reviews are required and scoped according to software classification and artifact criticality. For each artifact type, the classification determines scope:

* Mandatory peer reviews for Class A, B, and C software work products, including safety-critical artifacts.
* Defer to Center-specific process guidance for Class D/E artifacts, focusing reviews on risk-prone areas.

### **Summary**

Peer reviews are indispensable elements of NASA’s software engineering process. They:

1. Provide early defect detection.
2. Foster communication and collaborative improvement.
3. Align work products with project goals, quality standards, and mission-critical needs.

For optimal project outcomes, ensure peer reviews are appropriately scoped, executed, and tracked, prioritizing high-risk or complex areas while leveraging automation for efficiency. Regular application of data from peer reviews ensures future refinements in the software engineering discipline.

Refer to **NASA-STD-8739.9** for specialized inspection guidelines and best practices for peer reviews tailored to mission-critical systems. Additional checklist libraries and process assets are accessible for tailoring reviews to specific project needs.

Some best practices related to performing peer reviews on different work products:

1. **Checklists for system requirement inspections** should contain items that:
   1. Describe the proper allocation of functions to software, firmware, hardware, and operations.
   2. Address the validation of all external user interfaces.
   3. Check that all the software system functions are identified and broken into configuration items and that the boundary between components is well-defined.
   4. Check that all configuration items within the software system are identified.
   5. Check that the identified configuration items provide all functions required of them.
   6. Check that all interfaces between configuration items within the software system are identified.
   7. Address the correctness of the software system structure.
   8. Check that all quantifiable requirements and requirement attributes have been specified.
   9. Address the verifiability of the requirements.
   10. Check for the traceability of requirements from mission needs (e.g., use cases, etc.).
   11. Check for the traceability of requirements from system safety and reliability analyses (e.g., Preliminary Hazard Analysis (PHA), Fault Tree Analysis (FTA), Failure Modes and Effects Analysis (FMEA), hazard reports, etc.).  
       See also Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis).
2. **Check that the software requirements specification** of each of the following is complete and accurate:
   1. Software functions.
   2. Input and output parameters.
   3. States and modes.
   4. Timing and sizing requirements for performance.
   5. Interfaces.
   6. Use Cases if available.
   7. Check that specifications are included for error detection and recovery, reliability, maintainability, performance, safety, and accuracy.
   8. Check that safety-critical modes and states, and any safety-related constraints, are identified.
   9. Address the traceability of requirements from higher-level documents.
   10. Check that the requirements provide a sufficient base for the software design.
   11. Check that the requirements are measurable, consistent, complete, clear, concise, and testable.
   12. Check that the content of the software requirement specification fulfills the NPR 7150.2 recommendations, found in NASA-HDBK-2203A, NASA Software Engineering Handbook.
3. **Checklists for architectural (preliminary) design** should contain items that:
   1. Check that the design meets approved requirements.
   2. Address the validation of all interfaces among modules within each component.
   3. Address the completeness of the list of modules and the general function(s) of each module.
   4. Address the validation of fault detection, identification, and recovery requirements.
   5. Check that the component structure meets the requirements.
   6. Address the validation of the selection of reusable components.
   7. Address the traceability of the design to the approved requirements.
   8. Address the validation of the input and output interfaces.
   9. Check that each design decision is a good match to the system’s goal.
   10. Check that the content of the design description fulfills the NPR 7150.2 recommendation, found in NASA-HDBK-2203A, NASA Software Engineering Handbook.
   11. Check that safety controls and mitigations are identified in the design document when a safety-critical system is under inspection (Review system safety analyses in supporting documentation).
   12. When inspecting object-oriented or other design models:
       1. Check that the notations used in the diagram comply with the agreed-upon model standard notation (e.g., UML notations).
       2. Check that the design is modular.
       3. Check that the cohesion and coupling of the models are appropriate.
       4. Check that architectural styles and design patterns are used where possible. If design patterns are applied, validate that the selected design pattern is suitable.
       5. Check the output of any self or external static analysis tool outputs.
4. **Checklists for detailed design** should contain items that:
   1. Check that the design meets the approved requirements.
   2. Address the validation of the choice of data structures, logic algorithms (when specified), and relationships among modules.
   3. Check that the detailed design is complete for each module.
   4. Address the traceability of the design to the approved requirements.
   5. Check that the detailed design meets the requirements and is traceable to the architectural software system design.
   6. Check that the detailed design is testable.
   7. Check that the design can be successfully implemented within the constraints of the selected architecture.
   8. Check the output from any static analysis tools available.
5. **Checklists for source code** should contain items that:
   1. Address the technical accuracy and completeness of the code concerning the requirements.
   2. Check that the code implements the detailed design.
   3. Check that all required standards (including coding standards) are satisfied.
   4. Check that latent errors are not present in the code, including errors such as index out-of-range errors, buffer overflow errors, or divide-by-zero errors.
   5. Address the traceability of the code to the approved requirements.
   6. Address the traceability of the code to the detailed design.
   7. When static or dynamic code analysis is available, check the results of these tools.
6. **Checklists for the test plan** should contain items that:
   1. Check that the purpose and objectives of testing are identified in the test plan and they contribute to the satisfaction of the mission objectives.
   2. Check that all new and modified software functions will be verified to operate correctly within the intended environment and according to approved requirements.
   3. Check that the resources and environments needed to verify software functions and requirements correctly are identified.
   4. Check that all new and modified interfaces will be verified.
   5. Address the identification and elimination of extraneous or obsolete test plans.
   6. Check that each requirement will be tested.
   7. Check that the tester has determined the expected results before executing the test(s).
   8. For safety-critical software systems:
      1. Check that all software safety-critical functions or hazard controls and mitigations will be tested. This testing should include ensuring that the system will enter a safe state when unexpected anomalies occur.
      2. Check that safety and reliability analyses have been used to determine which failures and failure combinations to test for.
   9. Check that the content of the test plan fulfills NPR 7150.2 recommendations, found in NASA-HDBK-2203A, NASA Software Engineering Handbook.
7. **Checklists for test procedures** should contain items that:
   1. Check that the set of test procedures meets the objective of the test plan.
   2. Check that each test procedure provides:
      1. A complete and accurate description of its purpose
      2. A description of how it executes
      3. All expected results.
   3. Check that each test procedure identifies which requirement(s) it is testing and correctly tests the listed requirement(s).
   4. Check that each test procedure identifies the required hardware and software configurations.
   5. Check that test procedures exist to verify the correctness of the safety critical controls as well as any software controls or mitigations of hazards (HW, SW, or CPLD) and that the system can obtain a safe state from different modes, states, and conditions.
   6. Check that each test procedure will objectively verify the implementation of the requirement with the expected outcome.
   7. Check that the content of the software test procedure fulfills NPR 7150.2 recommendations, found in NASA-HDBK-2203A, NASA Software Engineering Handbook.

See also [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements).

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements) * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [5.15 - Train - Software Training Plan](/spaces/SWEHBVD/pages/102695676/5.15+-+Train+-+Software+Training+Plan) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [7.19 - Software Risk Management Checklists](/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.24 - Software Assurance Risk](/spaces/SITE/pages/146538591/8.24+-+Software+Assurance+Risk) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Peer Review](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Peer+Review) |

# 4. Small Projects

Small projects, while smaller in scale than larger endeavors, are no less critical to NASA’s mission success and must adhere to the same rigorous standards of quality and reliability. Peer reviews and inspections are essential tools for safeguarding the integrity of key artifacts, ensuring that small projects achieve their objectives within constrained resources. This guidance outlines strategies for small projects to make peer reviews and inspections both effective and manageable.

---

### **Leveraging Peer Reviews Effectively in Small Projects**

To ensure peer reviews remain practical within the constraints of small project teams, the following strategies are recommended:

1. **Adapt the Inspection Team to Project Scale:**

   * While maintaining the core principles of thorough peer reviews, small projects can **adjust the size of the inspection team** to make the process more scalable.
   * **Key Stakeholders Must Be Represented:** Ensure that representatives with essential expertise, including technical, interfacing, and operational contexts, are part of the inspection team.
   * Examples of smaller team configurations:
     + A **three-person team** comprising a moderator, author, and one technical expert.
     + Focused reviewers who specialize in high-risk or mission-critical areas (e.g., cybersecurity, interfaces, or performance-critical functions).
2. **Expand Beyond Internal Resources:**  
   When a small team lacks all necessary expertise, it can **reach outside the immediate project to acquire essential skills**, ensuring a well-rounded evaluation. Consider personnel from:

   * **Interface Areas:** Experts who work with interfacing components or systems (e.g., hardware or user interfaces).
   * **Related Projects:** Leverage individuals working on similar or related projects to gain insights into shared challenges or lessons learned.
   * **Functional Organizations:** Seek experts from within the Center’s broader functional organizations who specialize in relevant domains (e.g., software assurance, cybersecurity, systems engineering).
   * **User Organizations:** Involving end-users or customer stakeholders ensures alignment between the final product and mission needs.
3. **Engage Center Quality Assurance Personnel, If Available:**

   * Small projects should determine whether Center **Quality Assurance (QA) personnel** can assist with peer reviews or inspections.
   * QA staff can often provide:
     + A **trained moderator** to oversee and organize the inspection logistics, ensuring the process adheres to accepted standards while managing time effectively.
     + Technical expertise in areas specific to risk mitigation or compliance, adding value through independent perspectives.
   * If center-level QA resources are constrained, make use of Center Process Asset Libraries (PALs) for templates and checklists to guide the process.

---

### **Additional Best Practices for Small Projects**

Small projects face unique challenges related to resource constraints, expertise gaps, and time limitations. The following practices can help streamline the peer review process without sacrificing rigor:

1. **Tailor the Scope of the Review to the Artifact’s Criticality:**

   * Prioritize peer reviews for artifacts with the most potential to impact mission success:
     + **Requirements documents.** These should always be peer-reviewed because of their foundational influence on all subsequent phases.
     + **Critical design components.** Focus reviews on areas where complexity, safety-critical functionality, or a high rate of change is present.
     + **Code implementing key functionality.** Apply reviews to high-risk or mission-critical code segments identified in the software development plan.
   * Use **checklists** to focus reviewers’ attention on specific aspects of the artifact most relevant to the project’s goals.
2. **Focus Efforts on Key Outcomes:**

   * The goal of peer reviews is identifying **defects and improvement opportunities**, so keep the process efficient:
     + Limit meeting duration to avoid fatigue while maintaining productivity (e.g., 1-2 hours maximum).
     + Use pre-distributed review materials so the team spends meeting time discussing issues, not understanding the artifact.
3. **Combine Roles When Appropriate:**

   * For very small teams, individual reviewers may take on more than one role as long as the review remains impartial and productive. For example:
     + The moderator may also act as the recorder.
     + A reviewer from a related project may provide external expertise while checking for alignment with broader organizational goals.
4. **Incorporate Peer Review as Part of Routine Workflows:**

   * Integrate peer reviews into the project’s natural rhythms, such as sprint reviews in agile methodologies or phase transitions in waterfall processes, to reduce disruptions.
   * Short and focused “mini-reviews” of high-priority artifacts can prevent process bottlenecks while maintaining quality.
5. **Leverage Technology to Address Resource Limitations:**

   * Use virtual tools or software engineering platforms to broaden reviewer participation, especially for small or geographically distributed teams.
     + Example tools for review: JIRA, GitHub, or dedicated review platforms like Crucible.
   * Employ automated static analysis tools to address some review aspects (e.g., coding standards, syntax correctness), reserving manual peer reviews for higher-level issues.

---

### **Benefits of Tailored Peer Reviews for Small Projects**

Adapting the peer review process to meet the constraints and realities of small projects enables:

1. **Efficient Use of Resources:** Smaller team configurations or leveraging expertise externally helps optimize capacity without overburdening the team.
2. **Comprehensive Risk Mitigation:** Focused efforts on high-priority artifacts ensure that quality and mission-critical risks are addressed, leading to more reliable deliverables.
3. **Increased Collaboration Across Projects and Teams:** Engaging personnel from related projects or the user organization provides diverse insights, breaking down silos and increasing organizational knowledge-sharing.

---

### **Conclusion**

While small projects have unique constraints, effective peer reviews remain critical to delivering high-quality, reliable software artifacts. By scaling the team, leveraging external expertise when required, and focusing their efforts on high-priority areas, small projects can maintain compliance with NASA’s peer review standards without overextending their resources. Using trained moderators, adapting checklists, and incorporating QA personnel or automation where possible provides additional layers of rigor and accountability. Small projects can thus ensure that peer reviews serve their intended purpose as an agile, scalable quality assurance tool.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-274)

  [Safety and Mission Assurance Acronyms, Abbreviations, and Definitions,](https://standards.nasa.gov/standard/nasa/nasa-hdbk-870922 "Click to open in new window")

  NASA-HDBK-8709.22. Baseline, 2018-03-08, Change 5: 2019-05-14
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-277)

  [Software Formal Inspections Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-87399 "Click to open in new window")

  NASA-STD-8739.9, NASA Office of Safety and Mission Assurance, 2013. Change Date:
  2016-10-07, Change Number: 1
* (SWEREF-319)

  [What We Have Learned About Fighting Defects,](http://www.cs.umd.edu/~mvz/pub/eworkshop02.pdf "Click to open in new window")

  Shull, F., Basili, V. R., Boehm, B., Brown, A. W., Costa, P., Lindvall, M., Port, D., Rus, I., Tesoriero, R., and Zelkowitz, M. V., Proc. IEEE International Symposium on Software Metrics (METRICS02), pp. 249-258. Ottawa, Canada, June 2002.
* (SWEREF-421) "A collection of checklists for different purposes," Fraunhofer USA, The University of Maryland. This web page contains several resources for performing software inspections.
* (SWEREF-521)

  [Deficiencies in Mission Critical Software Development for Mars Climate Orbiter (1999)](https://llis.nasa.gov/lesson/740 "Click to open in new window")

  Public Lessons Learned Entry: 740.
* (SWEREF-685)

  [The Inquiry Board's Recommendations](https://www.esa.int/esapub/bulletin/bullet89/recom89.htm "Click to open in new window")

  Arianne 5 Inquiry Board - European Space Agency
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The importance of software peer reviews and inspections is underscored by documented lessons learned from past NASA projects, as well as broader aerospace incidents. These lessons highlight the consequences of deficiencies, the value of cross-functional collaboration, and the necessity of thorough reviews in preventing mission failures. Incorporating these lessons into project workflows offers invaluable guidance for safeguarding mission-critical software systems.

---

### **Lesson Learned (Starliner CFT):** **Independent reviews must enforce evidence completeness and cross‑functional insight.**

**Project Context:**  
Derived from Starliner CFT Investigation.

**Problem/Observation:**  
Review packages sometimes lacked sufficient V&V data; communication barriers prevented timely cross‑functional scrutiny.

**Contributing Factors:**

* Limited supplier participation or access to detailed artifacts.
* Reviews focused on procedural compliance rather than evidentiary sufficiency and system interactions.

**Impacts:**

* Gaps in coverage and late discovery of cross‑subsystem issues.
* Reduced confidence in readiness decisions.

**Recommended Practices (Aligned to SWE‑087/088):**

* Implement **evidence‑based review checklists** (requirements→tests→results→defects→resolutions).
* Include **cross‑functional reviewers** (software, systems, safety, ops) with authority to block.
* Track **review action items** to closure with verification evidence.

**Actionable Checks:**

* Review checklists are completed and archived with artifacts.
* Reviewer rosters include required disciplines; dissenting views recorded.
* Action item logs show closure and verification references.

### **Lessons Learned: Class D Staffing Model Leading to Insufficient Software Assurance Depth**

**Problem/Observation:**  
Class D mission constraints resulted in limited staffing depth and gaps in key technical and assurance roles. The Anomaly Review Board (ARB) identified several resourcing shortfalls that directly affected flight software (FSW), fault protection (FP), and mission assurance readiness.

**Contributing Factors:**  
• Junior engineers were placed in critical FSW and FP roles without senior technical backstops.  
• Chief Engineer and FSW Lead positions remained vacant for extended periods.  
• Mission operations staffing relied heavily on students rather than experienced operators.  
• No dedicated Anomaly Response Team (ART) was established.

**Resulting Impacts:**  
Resourcing gaps reduced the mission’s ability to maintain technical rigor, ensure independent oversight, and execute timely issue resolution. Critical analyses, reviews, and test preparation activities were delayed or completed without adequate depth, increasing mission risk.

**Relevant SWEHB Guidance:**  
While Class D missions may tailor processes and operate with small teams, certain competencies and roles cannot be reduced or left unfilled.  
• SWE‑017 (Training) requires personnel to be trained and qualified for their assigned roles—tailoring does not waive the requirement for demonstrated competency.  
• SWE‑087 and SWE‑088 (Peer Reviews/Inspections) reinforce the need for independent review, even in resource‑limited environments, to ensure defects are identified early.

**Lesson Learned:**  
Tailoring for Class D missions must not come at the expense of essential systems engineering and software assurance expertise. Critical leadership roles—such as FSW Lead, FP Architect, and Mission Assurance—require experienced personnel, and their absence cannot be offset by junior staff or temporary support. Adequate staffing depth is foundational to maintaining software quality, executing independent reviews, and ensuring readiness throughout the life cycle.

### **Deficiencies in Mission-Critical Software Development: Mars Climate Orbiter (1999)**

**Lesson Number 0740** from the NASA Lessons Learned database provides harsh yet instructive insights into the consequences of non-compliance with software review standards, which contributed significantly to the loss of the Mars Climate Orbiter.

#### **Key Takeaways:**

1. **Non-Compliance with Software Review Practices Can Lead to Mission Loss:**  
   The failure of the Mars Climate Orbiter revealed how gaps in software requirements walk-throughs and downstream validation activities can cause errors to propagate undetected, ultimately leading to catastrophic failure.

   * **Example:** Contradictions in software interfaces between teams led to metric-to-imperial conversion errors that caused navigation failure.
2. **Identifying Mission-Critical Software Requires Concurrent Engineering and Collaboration:**  
   Defining and reviewing mission-critical software cannot be left to individual teams working in isolation. Success demands a **cross-functional approach**, merging contributions from systems engineers, developers, and end-users early in requirements definition and design.

   * **Solution:** Ensure collective walk-throughs during requirements, design, and acceptance reviews, combining broad expertise to address implicit assumptions, risks, and integrations.
3. **Cross-Disciplinary Reviews of Software Interfaces are Critical:**  
   Interfaces between software, systems, and organizational boundaries must undergo formal reviews involving **developers, systems engineers, and end-users.** This ensures end-to-end functionality and identifies risks related to assumptions, data transformations, and constraints.

These hard-learned lessons emphasize that software peer reviews are not merely a recommendation—they are a safeguard for mission success.

---

**LL‑SW‑01 — Standards for Heritage Software Reuse and Testing**

* **Source LL ID(s):** IVV‑01
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** Program teams planned to reuse “legacy” flight software; significant defects emerged late, revealing the misconception that heritage code needs minimal testing.
* **Lesson Learned:** Treat heritage software **as if new**—perform full requirements validation, interface verification, regression testing, and environmental qualification for the new mission context.
* **Evidence/Observation:** PPE planned legacy reuse; issues were still open at the pause; reuse assumptions delayed defect discovery and correction.
* **Cause(s):** Belief that prior flight history obviates testing; lack of program‑level reuse standards.
* **Recommendation/Corrective Action:** Establish **project‑level reuse standards** specifying test scope (regression, interface, environment), verification criteria, and acceptance gates for heritage software.
* **Implementation Guidance:** Embed reuse criteria in plans (SWE‑013), trace reused functionality to requirements/design/tests (SWE‑052/059/064/072), and determine safety classification impacts (SWE‑133/134).
* **Success Criteria/Verification:** Documented reuse plan; executed test campaigns; evidence of bidirectional traceability and IV&V closure; defect rates comparable to new development baselines.
* **Applicability/Scope:** All mission/safety‑critical software; heritage and third‑party components.
* **Related Standards/Requirements:** **SWE‑027 (COTS/legacy use), SWE‑013 (Plans), SWE‑050 (Requirements), SWE‑052/059/064/072 (Traceability), SWE‑133/134 (Safety)**.

**LL‑SW‑06 — Provide Design Artifacts Early and In‑Phase with Development**

* **Source LL ID(s):** IVV‑02
* **Discipline(s):** Software Assurance, IV&V, Software Design
* **Context/Background:** Early design visibility enables cheaper, timely feedback; late delivery limits IV&V value.
* **Lesson Learned:** Share evolving designs **before coding**; IV&V supports iterative updates and identifies issues when change costs are lowest.
* **Evidence/Observation:** Difficulties obtaining early design artifacts on HALO/PPE reduced synchronization and defect prevention.
* **Cause(s):** Perception that IV&V slows design.
* **Recommendation/Corrective Action:** Include design artifact delivery milestones in IV&V PEP; allow early access to drafts.
* **Implementation Guidance:** **SWE‑013** (planning), **SWE‑018** (reviews), **SWE‑131/141** (IV&V).
* **Success Criteria/Verification:** Reduced design‑phase rework; fewer late defects; on‑time IV&V reviews.
* **Applicability/Scope:** All mission/safety‑critical designs.
* **Related Standards/Requirements:** **SWE‑013, SWE‑018, SWE‑131, SWE‑141**.
* **References:** Gateway S&MA LL deck.

**LL‑SW‑08 — Include Subcontractor Documentation in Deliveries**

* **Source LL ID(s):** IVV‑08
* **Discipline(s):** Software Assurance, IV&V, Acquisition
* **Context/Background:** Prime docs lacked detail for subcontractor‑developed functionality; IV&V couldn’t assess low‑level designs.
* **Lesson Learned:** Require subcontractor **low‑level design/documentation** availability to IV&V (as legally permissible).
* **Evidence/Observation:** More complete documentation reduced false positives and improved issue identification.
* **Cause(s):** Undefined contractual expectations for lower‑tier artifacts.
* **Recommendation/Corrective Action:** Include flow‑downs mandating artifact delivery/access rights; define content/format.
* **Implementation Guidance:** Plans (**SWE‑013**), requirements (**SWE‑050**), and IV&V (**SWE‑131/141**) should specify subcontractor documentation scope.
* **Success Criteria/Verification:** IV&V can compile/build/analyze with full design context; decreased unactionable findings.
* **Applicability/Scope:** Multi‑tier development efforts.
* **Related Standards/Requirements:** **SWE‑013, SWE‑050, SWE‑131, SWE‑141**.

**LL‑SW‑17 — Tool and Database Usability Drives Process Quality**

* **Source LL ID(s):** CP‑Hazard/SharePoint/ARM usability LLs (GW‑SMA‑LL‑019/026/036/048‑054/084)
* **Discipline(s):** Software Tools/Process, Assurance Data Mgmt
* **Context/Background:** Tools lacked features/automation; partitions caused visibility leaks; usability issues degraded reviews and traceability.
* **Lesson Learned:** Select/configure tools based on **process needs**; mandate usability, automation, partitioning, and reporting capabilities.
* **Evidence/Observation:** Commenting, partitioning, PDF generation, and access governance weaknesses added workload and risk.
* **Cause(s):** Sustainment‑only funding; late tool development; ad‑hoc admin.
* **Recommendation/Corrective Action:** Conduct **analysis of alternatives**; fund capability expansion; embed operational architects; standardize partitions and role models.
* **Implementation Guidance:** Capture in **SWE‑013** (plans) and **SWE‑091** (measurement repositories) with defined KPIs for tool performance.
* **Success Criteria/Verification:** Reduced manual auditing; reliable exports; secure access; KPI improvements (latency, completeness).
* **Applicability/Scope:** All assurance tools, requirements DBs, risk systems.
* **Related Standards/Requirements:** **SWE‑013, SWE‑091**.

### **Ariane 5 Incident: Inquiry Board Recommendations**

The loss of the Ariane 5 rocket emphasized the catastrophic impact of overlooked assumptions, software vulnerabilities, and insufficient testing coverage in mission-critical systems. The subsequent recommendations from the Inquiry Board provide actionable insights for preventing similar failures.

#### **Key Recommendations:**

1. **Review All Flight Software, Including Embedded Software:**  
   Ensure comprehensive reviews of all mission software, particularly embedded systems, which are often tightly coupled with hardware components. These reviews should:

   * **Identify Implicit Assumptions Made by Code:** Document all embedded assumptions about the values provided by equipment, restrictions on equipment use, and external system behavior.
   * **Check Assumptions Against Equipment Constraints:** Explicitly validate assumptions during the review and test them against each component's operational limits.
2. **Verify All Communication and Internal Variables:**  
   For software variables that either transmit data or influence internal processes:

   * Confirm the **range of values** they may take, ensuring compatibility with equipment constraints and preventing catastrophic errors such as overflows or invalid state transitions.
   * Conduct formal reviews of variable initialization and handling under off-nominal conditions.
3. **Proposal and External Review:**  
   Require development teams to **propose solutions to potential onboard computer problems**, especially switchover events that could induce unpredictable behavior.

   * These solutions should be rigorously reviewed by **external experts** before being presented to onboard computer Qualification Boards.
   * External reviewers provide unbiased perspectives, ensuring coverage of risks the internal project team may overlook.
4. **Include External Expertise in Software Reviews:**  
   External (to the project) participants should be involved in peer reviews, walk-throughs, and approval processes for specifications, code, and justification documents. These experts, unencumbered by project biases, should focus on **substance rather than procedural checks** to ensure that software logic and assumptions are technically sound.

---

### **Additional Lessons from Aerospace and Software Incidents**

In addition to NASA-specific examples, broader aerospace and software failures reinforce the necessity of implementing rigorous software peer review processes.

#### **Therac-25 Radiation Therapy Accidents:**

The failures of the Therac-25 software led to massive overdoses of radiation due to overlooked code errors. Lessons learned include:

1. **Conduct Rigorous Peer Reviews of Safety-Critical Software:**  
   Every line of code in safety-critical systems should be reviewed for correctness, error handling, and failover functionality. Peer reviews should prioritize issues that could lead to catastrophic outcomes.
2. **Test System Interactions at Boundaries:**  
   Review how different parts of the system interact, particularly where software interfaces hardware or human inputs. Peer reviews must verify assumptions about state transitions, inputs, and limits.

#### **Boeing 737 Max Incident (MCAS Software):**

Critical lessons from the flawed implementation of the Maneuvering Characteristics Augmentation System (MCAS) software revolve around insufficient peer reviews and lack of redundancy analysis:

1. **Ensure Thorough Reviews of Cross-System Interactions:**  
   Software interacting with autopilot, sensors, and flight control mechanisms must be peer-reviewed to validate assumptions about data inputs and states under off-nominal scenarios.
2. **Examine Failover Logic Through Peer Reviews:**  
   Peer reviews should confirm that failover procedures and fallback mechanisms can handle erroneous or unexpected inputs gracefully.

---

### **Key Actions for Future Projects**

Based on these lessons, NASA and similar organizations can further enhance their peer review processes to mitigate risks:

1. **Formalize Peer Review Coverage for Mission-Critical Software:**

   * Require all artifacts (requirements, design, code, interfaces) related to mission-critical systems to undergo structured peer reviews using tailored checklists for critical areas such as safety, reliability, performance, and cybersecurity.
2. **Integrate External Expertise Early and Often:**

   * Leverage external experts or reviewers with no vested interest in the project to provide unbiased evaluation during major peer review stages.
3. **Strengthen Interface Documentation and Validation:**

   * Focus peer reviews on system interfaces and operational assumptions, especially for software interfacing hardware, cross-organizational platforms, or mission-critical sensors.
4. **Document Assumptions and Validate Influence Across Artifacts:**

   * Require peer reviews to explicitly capture and validate assumptions made during requirements definition, design, and code development. Each assumption must be thoroughly vetted for alignment with equipment, safety constraints, and mission goals.

---

### **Conclusion**

NASA’s past projects and lessons learned illustrate the catastrophic consequences of lacking robust peer review processes. Conversely, implementing focused reviews of software artifacts and emphasizing collaboration between system engineers, developers, end-users, and external reviewers enhances the reliability of mission-critical systems. Incorporating these lessons into peer review practices will significantly increase NASA’s ability to mitigate risks and deliver successful missions. For every project, large or small, prioritizing rigorous peer reviews ensures that errors are caught systematically—before they threaten the success of the mission.

## 6.2 Other Lessons Learned

* A substantial body of data and experience justifies the use of inspections on requirements. Finding and fixing requirements problems during requirements analysis is cheaper than doing so later in the life cycle and is substantially cheaper than finding and fixing the same defects after delivering the software. Data from NASA and numerous other organizations (such as IBM, Toshiba, and the Defense Analysis Center for Software) all confirm this effect. [319](#_tabs-<p></p>)
* The effectiveness of inspections for defect detection and removal in any artifact has also been amply demonstrated. Data from numerous organizations have shown that a reasonable rule of thumb is that a well-performed inspection typically removes between 60 percent and 90 percent of the existing defects, regardless of the artifact type. [319](#_tabs-<p></p>)
* Ensure peer review participation by key stakeholders including Systems Engineering, and all affected Responsible Engineers.
* Perform requirements checks as part of Implementation or code peer reviews.
* The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

  + [Requirements should be documented and peer reviewed](https://software.gsfc.nasa.gov/lesson-details/53/). **Lesson Number 53**: The recommendation states: "Requirements should be documented and peer reviewed."
  + [Peer Reviews should be used on documentation as well as code](https://software.gsfc.nasa.gov/lesson-details/66/). **Lesson Number 66**: The recommendation states: "Peer Reviews should be used on documentation as well as code."
  + [Early project software review of SMP deliverables](https://software.gsfc.nasa.gov/lesson-details/298/). **Lesson Number 298**: The recommendation states: "The project's software management plan (SMP) should explain the delivery and review chain for all software products, especially when they are not being delivered directly to the project. If there are more than one or two organizations with separate configuration management systems between the developer and the project review, they should make plans to have the person who is eventually responsible for technical approval of SDP deliverables (e.g., project software engineer or project software lead) be involved in the review process earlier on."
  + [Consider a streamlined review process for lower maturity products](https://software.gsfc.nasa.gov/lesson-details/332/). **Lesson Number 332**: The recommendation states: "Start with a small group for initial review, and then add reviewers later."

# 7. Software Assurance

**SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures**

5.3.2 The project manager shall perform and report the results of software peer reviews or software inspections for:

a. Software requirements.  
b. Software plans, including cybersecurity.  
c. Any design items that the project identified for software peer review or software inspections according to the software development plans.  
d. Software code as defined in the software and or project plans.  
e. Software test procedures.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that software peer reviews are performed and reported on for project activities. 

2. Confirm that the project addresses the accepted software peer review findings.

3. Perform peer reviews on software assurance and software safety plans.

4. Confirm that the source code satisfies the conditions in the NPR 7150.2 requirement SWE-134, "a" through "l," based upon the software functionality for the applicable safety-critical requirements at each code inspection/review.

## 7.2 Software Assurance Products

Software Assurance (SA) delivers and monitors the following core products for peer reviews and inspections:

* **SA Peer Review Records:** These include findings related to software assurance and software safety plans, ensuring documentation of SA insights and corrective actions across review activities.
* **Peer Review Metrics, Reports, Data, or Findings:** SA tracks metrics and generates summary reports to provide insight into the effectiveness of peer reviews and identify areas for continuous improvement. Examples of findings include defect patterns, non-conformance types, and closure durations.
* **List of Participants in Software Peer Reviews:** Ensures that all necessary stakeholders — including developers, systems engineers, assurance personnel, and end-users — participated in the reviews, promoting cross-disciplinary validation of work products.

## 7.3 Metrics

Metrics are critical for tracking the effectiveness of peer reviews, highlighting trends, and ensuring accountability. Suggested metrics include:

1. **Defect/Non-Conformance Metrics:**

   * Total **number of non-conformances identified in each peer review.**
   * Number of **safety-related non-conformances** identified by lifecycle phase and over time.
   * Time required to close review non-conformances and total trends of **open vs. closed non-conformances over time.**
   * Number of **non-conformances identified by SA during each peer review.**
2. **Process Metrics:**

   * Total **peer reviews performed vs. peer reviews planned.**
   * Number of **SA resources used vs. proposed participation.**
   * Percentage of peer reviews that successfully implement requirements, design, or testing best practices.
3. **Software Lifecycle Metrics:**

   * Total **# of software work product non-conformances identified by lifecycle phase.**
   * Number of **non-conformances accepted by the project** after SA evaluation.
   * Trends of **safety requirement issues (open/closed) over time,** particularly for safety-critical software.
4. **Code-Specific Metrics:**

   * Percentage of **source code classified for peer review (per Software Classification).**
   * Number of issues from **code review findings mapped to the error taxonomy (e.g., logic, timing, standards violations).**

> See also **Topic 8.18 - SA Suggested Metrics.**

## 7.4 Guidance

**1. Ensure Peer Reviews Are Planned and Targeted:**

* Confirm that peer reviews are scheduled for critical products as outlined in **SWE-087**, particularly for:
  + **Requirements.**
  + Software plans (e.g., cybersecurity, assurance, V&V).
  + Test procedures.
* Check early in the project (e.g., before **SRR or PDR**) that peer reviews are applied to high-priority items and documented in the software management or development plan.
* Ensure design and code reviews target key areas:
  + **Mission-critical software.**
  + Code or design segments addressing **safety-critical, complex, or high-risk functions.**

**2. Attend Scheduled Reviews and Track Results:**

* SA personnel must attend peer reviews identified in the software management plan to ensure active oversight.
* Verify that peer reviews close issues and defects before moving products forward. SWE-088 contains additional guidance on checklist criteria for tracking issues.

**3. Address Peer Reviews of Software Assurance Products:**

* SA teams should also ensure their products (e.g., SA plans, requirement assessments) are subjected to peer reviews:
  + Address and resolve defects found during these reviews.
  + Track SA product review metrics (e.g., SA-driven issues identified per review).

**4. Promote Stakeholder Representation:**

* Ensure peer review participation includes key stakeholders such as software developers, systems engineers, responsible engineers (RE), safety personnel, and cybersecurity experts.
* Incorporate **independent reviewers (if possible)** to reduce blind spots and enhance objectivity.

**5. Validate Compliance with NPR 7150.2 and NASA-STD-8739.8:**

* Verify alignment with all requirements and standards, including:
  + Implementation of **error detection, fault recovery, and safety-critical mitigations.**
  + Validation of fault detection, identification, and resolution measures within software and system designs.

**6. Confirm Requirements Checks in Code Reviews:**

* Ensure code or design peer reviews verify that products meet the software requirements and trace them effectively.

---

### **Role of Software Assurance Personnel**

SA personnel help ensure peer reviews are executed rigorously and effectively. Key responsibilities include:

1. **Compliance Verification:**

   * Review peer review packages for required documentation and validate participation by all relevant personnel.
   * Ensure adherence to checklist criteria and processes outlined in peer review procedures.
2. **Process Participation:**

   * Actively participate in peer reviews, sometimes filling inspection roles such as moderator, recorder, or reviewer.
   * Independently evaluate the effectiveness of inspection processes and the quality of products reviewed.
3. **Outcome Validation:**

   * Confirm that all outcomes from peer reviews — including defects, action items, and risks — are documented, tracked, and resolved before the review is closed.
4. **Safety Implementation Oversight:**

   * Verify safety-related requirements, including:
     + Error detection and correction strategies.
     + Fault isolation, identification, and recovery implementation.

---

### **Error Taxonomy for Peer Reviews**

SA personnel should use the following taxonomy to classify issues found during code reviews. This systematic classification fosters consistent defect tracking and better targeting of corrective actions.

* **Algorithm or Method:** Errors in the sequence of operations, computations, or implementation logic.
* **Initialization or Assignment:** Incorrect initialization or assignment of variables, e.g., mishandled memory or I/O.
* **Checking:** Inadequate handling or response to error conditions.
* **Internal/External Interfaces:** Mismatches in system or module interfaces, such as incorrect parameter passing or boundary violations.
* **Logic and Conditions:** Errors in loops, branches, or boundary conditions, including “off-by-one” errors.
* **Standards Compliance:** Violations of coding or design standards.
* **Non-Functional Issues:** Failures related to performance, scalability, or code readability.
* **Timing or Optimization:** Issues causing race conditions, deadlocks, or poor performance.

---

### **Best Practices for Peer Reviews**

To ensure peer reviews are comprehensive and effective:

* Use tailored **checklists** for all software products (e.g., requirements, design, code, test plans/procedures).
* Limit inspection sessions to **2 hours** to maintain reviewer focus while ensuring adequate preparation.
* Prioritize high-risk areas (e.g., **safety-critical or complex interfaces**) for manual peer reviews.
* Track detailed metrics on peer reviews, including defect categories, lifecycle phase metrics, open/closed issues, and SA-specific contributions.
* Assess trends using historical peer review data to improve future reviews and identify recurring project risks.

---

### **See Also:**

* SWE-134 – **Safety-Critical Software Design Requirements.**
* SWE-088 – **Peer Review Checklist Criteria.**
* Topic 7.10 – **Peer Review and Inspections Including Checklists.**
* Topic 8.18 – **SA Suggested Metrics.**

This guidance reinforces the value of structured and comprehensive peer reviews as a cornerstone of software assurance, ensuring that NASA delivers high-quality, reliable, and mission-critical software.

**Assure that all code peer reviews have verified that the code or code changes meet the software requirements.**

See [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) for additional guidance associated with cyclomatic complexity assessments.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements) * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [5.15 - Train - Software Training Plan](/spaces/SWEHBVD/pages/102695676/5.15+-+Train+-+Software+Training+Plan) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [7.19 - Software Risk Management Checklists](/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.24 - Software Assurance Risk](/spaces/SITE/pages/146538591/8.24+-+Software+Assurance+Risk) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical for demonstrating compliance with NASA's software engineering requirements, specifically regarding the application of peer reviews and inspections. This evidence provides tangible proof that the software peer review processes were effectively planned, executed, and documented, as required by NPR 7150.2 and related standards (e.g., NASA-STD-8739.8).

Below is a list of artifacts and documentation that serve as **objective evidence** for satisfying this requirement:

---

### **1. Peer Review Planning Evidence**

* **Peer Review Schedule:**  
  Documentation of planned peer reviews, including timelines, milestones, and artifacts to be reviewed (e.g., requirements, design, code, test plans). These schedules should integrate reviews within the project's overall software lifecycle.
* **Software Management/Development Plan (SMP/SDP):**  
  Evidence that the peer review process is planned and explicitly defined in the SMP/SDP. This includes identification of review activities for all software work products as applicable (e.g., requirements, designs, test cases).
* **Checklists for Peer Reviews:**  
  Checklists used to guide peer reviews for specific artifacts, customized to the artifact type (e.g., code checklists, requirements checklists). These serve as predefined criteria for reviewers and ensure that all necessary aspects of the software artifact are scrutinized.
* **Trained Personnel Participation Plan:**  
  Confirmation that key stakeholder roles (e.g., systems engineers, developers, test engineers, software assurance professionals) have been identified and assigned for review activities. Evidence of training for reviewers (e.g., peer review process training, checklist preparation) may also be provided.

---

### **2. Peer Review Execution Evidence**

* **Peer Review Meeting Records:**  
  Records of all peer review meetings, including agendas, attendance lists, action items, and detailed meeting notes from walkthroughs or inspections. This includes the involvement of software developers, software assurance, systems engineers, and other stakeholders.
* **Sign-In Logs or Attendance Lists:**  
  Documentation showing that all required peer review participants (e.g., author, moderator, recorder, and reviewers) participated in each review as planned.
* **Inspection Packages/Materials:**  
  Copies of materials shared with reviewers prior to the peer review meeting, such as requirements documents, design diagrams, code segments, or test cases. These materials should be aligned with the project’s approved peer review checklists.
* **SA Participation Evidence:**  
  Records confirming software assurance (SA) personnel presence during reviews to oversee and verify adherence to process.

---

### **3. Metrics Documentation**

* **Peer Review Metrics Reports:**  
  Documentation of all peer review metrics collected during the project. Common metrics include:

  + Number of peer reviews completed versus planned.
  + Non-conformance counts (open, closed, total).
  + Trends of defect identification across work products or lifecycle phases.
  + Time required to close non-conformances.
  + Number of defects identified during each peer review and by artifact type.
  + Percentage of non-conformance resolution carried out prior to the artifact’s next lifecycle phase.
* **Non-Conformance Tracking Logs:**  
  Logs showing identified defects, their classification (e.g., safety-critical, coding standards violations), and their current status (open or closed). These logs should align with project tools for defect tracking (e.g., JIRA, Bugzilla, or other repositories).
* **SA-Specific Findings Metrics:**  
  Evidence of defects or risks identified by software assurance during peer reviews, showing SA’s contribution to quality improvements.

---

### **4. Compliance Verification Evidence**

* **Checklists with Annotations:**  
  Completed checklists showing that reviewers scrutinized work products to ensure they adhered to the planned criteria for quality, completeness, and compliance. Checklists are critical for verifying work product attributes such as:
  + Requirements traceability and clarity.
  + Safety-critical fault detection and mitigation.
  + Coding standards adherence.
* **Requirements Verification Evidence:**  
  Documentation of peer review findings confirming that requirements align with system needs, safety constraints, and stakeholder input.
* **Reviewed Software Products:**  
  Artifacts showing that reviewed and revised versions of work products incorporated all action items assigned during peer reviews. Examples include:
  + Updated requirements documents after a peer review highlighted errors.
  + Revised source code reflecting corrections for logic or safety-critical defects.

---

### **5. Issue Tracking and Resolution**

* **Action Item Logs:**  
  Complete logs of all action items and open issues identified during peer reviews, including plans for addressing each issue. Every log entry should track the following:

  + Description of the defect/issue.
  + Non-conformance category (e.g., logic error, unverified assumption, interface mismatch).
  + Priority or criticality level.
  + Assigned personnel for resolution.
  + Status (e.g., open, in progress, or closed).
* **Defect Management Records:**  
  Documentation of detected non-conformances, their resolution process, and the status of their closure (e.g., via defect tracking systems like JIRA). Records should show that defects were tracked to closure in accordance with internal corrective action procedures.
* **Rework Validation Reports:**  
  Evidence that all peer review findings and defects were corrected in the work product and validated as part of the post-review follow-up process.

---

### **6. Higher-Level Compliance/Review Evidence**

* **Evidence of Safety Assurance Reviews:**  
  Verification that safety-critical issues, such as fault detection or hazard mitigations, were reviewed and addressed.
* **Evidence of External or Independent Participation:**  
  Records demonstrating external (to the project) reviewers’ involvement in peer reviews for mission-critical components. This ensures unbiased feedback on requirements, designs, or code. For example:

  + Participation logs or results from external safety reviewers.
  + Reports from independent verification and validation (IV&V) teams confirming their contributions to the reviews.
* **Summary Reports for Key Milestones:**  
  Peer review summary reports highlighting the artifacts reviewed, defects identified, actions taken, and final disposition of findings. These should be prepared for key project lifecycle reviews such as SRR, PDR, and CDR.

---

### **7. Tool and Automation Evidence**

* **Static Analysis Tool Outputs:**  
  Evidence from automated tools (e.g., for code compliance, security checks) used as part of the peer review process. Reports from these tools should show that peer reviews leveraged automation to identify potential coding or design flaws.
* **Issue/Defect Logs from Tracking Tools:**  
  Documentation from defect tracking systems (e.g., JIRA, GitHub) showing peer review findings that align with logged issues and confirm follow-up.

---

### **8. Training and Process Documentation**

* **Peer Review Plans and Procedures:**  
  Documentation describing the peer review process, roles, responsibilities, checklists, and criteria. Evidence should demonstrate that all peer reviews adhered to these approved processes.
* **Training Records for SA Personnel:**  
  Evidence (e.g., certificates, course completions) that SA personnel and other participants were trained in peer review processes.

---

### **Summary of Objective Evidence Types:**

| **Evidence Type** | **Description** |
| --- | --- |
| Peer Review Schedule | Review plans integrated into the lifecycle. |
| Attendance Logs | Participant records demonstrating stakeholder involvement. |
| Peer Review Checklists | Completed peer review checklists with annotations for every artifact. |
| Metrics Reports & Summaries | Non-conformance trends, closure rates, SA contributions. |
| Issue Tracking Logs | Action items, defect statuses logged and tracked. |
| Software Artifacts | Reviewed and corrected work (e.g., updated requirements, revised code). |
| Static Analysis Reports | Automated tool findings as part of reviews. |
| Summary Reports for Lifecycle Reviews | Peer review findings summarized for SRR, PDR, CDR, and other milestones. |
| Training Records | Proof of training for SA and peer review participants. |

---

Providing this objective evidence ensures that peer reviews are executed consistently, documented thoroughly, and auditable for compliance with both NASA's internal standards and external accountability measures. This builds confidence that defects are identified and addressed promptly, safeguarding mission success.

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
