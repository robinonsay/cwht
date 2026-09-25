# SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695473. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking

SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695473)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695473&showCommentArea=true&showComments=true#addcomment)

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

5.3.3 The project manager shall, for each planned software peer review or software inspection:

a. Use a checklist or formal reading technique (e.g., perspective-based reading) to evaluate the work products.  
b. Use established readiness and completion criteria.  
c. Track actions identified in the reviews until they are resolved.  
d. Identify the required participants.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-088 History

SWE-088 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.3.3 The project shall, for each planned software peer review/inspections:        a. Use a checklist to evaluate the work products.       b. Use established readiness and completion criteria.       c. Track actions identified in the reviews until they are resolved.       d. Identify required participants. |
| Difference between A and B | Included "formal reading technique" as mechanism for evaluating work products. |
| B | 5.3.3 The project manager shall, for each planned software peer review or software inspection:   1. 1. Use a checklist or formal reading technique (e.g., perspective based reading) to evaluate the work products.    2. Use established readiness and completion criteria.    3. Track actions identified in the reviews until they are resolved.    4. Identify required participants. |
| Difference between B and C | No change |
| C | 5.3.3 The project manager shall, for each planned software peer review or software inspection:   1. 1. Use a checklist or formal reading technique (e.g., perspective based reading) to evaluate the work products.    2. Use established readiness and completion criteria.    3. Track actions identified in the reviews until they are resolved.    4. Identify the required participants. |
| Difference between C and D | No change |
| D | 5.3.3 The project manager shall, for each planned software peer review or software inspection:  a. Use a checklist or formal reading technique (e.g., perspective-based reading) to evaluate the work products. b. Use established readiness and completion criteria. c. Track actions identified in the reviews until they are resolved. d. Identify the required participants. |

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

Checklists, criteria, and tracking of actions and participants are needed to conduct an effective peer review or inspection.  Peer reviews and inspections contribute to product and process quality, risk reduction, confirmation of approach, defect identification, and product improvements.

This requirement ensures that software peer reviews and inspections are conducted in a disciplined, rigorous, and productive manner, contributing to the overall quality, reliability, and compliance of the software products. Peer reviews and inspections are proactive measures that identify and address defects early in the development lifecycle, significantly reducing downstream costs and risks. Below is the rationale for each part of this requirement:

---

### **a. Use a checklist or formal reading technique (e.g., perspective-based reading) to evaluate the work products.**

#### **Rationale:**

Utilizing a checklist or formal reading technique ensures **consistency**, **focus**, and **thoroughness** during the review process. These methods standardize the review, reducing the likelihood of overlooking critical aspects of the work product. They also align the review process with organizational best practices and requirements.

* **Checklists Provide Guidance:** Checklists explicitly outline items to evaluate (e.g., requirements traceability, coding standards adherence, logic correctness, safety-critical functionality). This minimizes reliance on the reviewers' memory or subjective judgment.
* **Formal Techniques Increase Objectivity:** Techniques such as **perspective-based reading** enhance objectivity by enabling reviewers to evaluate the product from different viewpoints (e.g., developer, tester, end-user).
* **Improves Efficiency and Coverage:** A structured approach ensures that the review time is efficiently spent on relevant issues and that no important aspect of the work product is missed.
* **Supports Organizational Standards:** Checklists ensure compliance with NASA standards (e.g., NPR 7150.2, NASA-STD-8739.8) by embedding specific, measurable evaluation criteria.

---

### **b. Use established readiness and completion criteria.**

#### **Rationale:**

Established readiness and completion criteria ensure that peer reviews are conducted at the right time and can be closed out only when all objectives and requirements have been met.

* **Readiness Criteria Prevent Premature Reviews:** These criteria ensure that the product to be reviewed is sufficiently mature to provide meaningful feedback. Premature reviews waste time and resources while providing little value.
  + Example: Reviewing code that is incomplete or insufficiently documented could lead to superficial findings and missed critical issues.
* **Completion Criteria Define Success:** Clearly defined completion criteria ensure that peer reviews achieve their intended purpose (e.g., all defects are logged, critical defects are resolved or planned for resolution, participants agree on the product’s readiness to proceed to the next phase).
* **Promotes Process Discipline:** Readiness and completion criteria prevent the hurried or informal closure of reviews, which could result in unresolved defects progressing downstream in the development lifecycle. This disciplined approach reduces rework and mitigates risks later in the project.

---

### **c. Track actions identified in the reviews until they are resolved.**

#### **Rationale:**

Tracking and resolving actions identified during reviews ensures that the feedback provided in the review process leads to meaningful improvements in the product. This step is critical for addressing deficiencies effectively and ensuring that the peer review achieves its intended outcomes.

* **Prevents Defect Escape:** By tracking defects or issues to closure, this requirement minimizes the chances that unresolved defects propagate to later lifecycle stages, where they become more costly to fix.
* **Improves Product Quality:** Resolution of peer review findings helps create higher-quality software by ensuring that all identified issues, even minor ones, are addressed.
* **Accountability and Traceability:** Action tracking provides traceability, demonstrating that all identified issues were resolved or appropriately dispositioned (e.g., deferred or waived with rationale).
* **Supports Continuous Improvement:** Tracking resolution metrics (e.g., closure time, trends) highlights recurring problem areas or bottlenecks, enabling continuous improvement of processes and practices.
* **Builds Stakeholder Confidence:** Evidence of issue resolution ensures stakeholders that the peer review findings were implemented, instilling confidence in the quality and reliability of the reviewed product.

---

### **d. Identify the required participants.**

#### **Rationale:**

Identifying required participants ensures that the peer review team includes individuals with the expertise, perspective, and technical knowledge necessary to evaluate the work product thoroughly and holistically.

* **Diverse Perspectives:** Including stakeholders from multiple disciplines (e.g., developers, systems engineers, end-users, software assurance personnel) brings different viewpoints to the review, making it more comprehensive.
  + For example, developers focus on code correctness, systems engineers focus on integration, and end-users evaluate usability.
* **Subject Matter Expertise:** Peer reviews require expertise in the specific area being reviewed (e.g., safety-critical software, performance-critical algorithms). Required participants ensure that reviewers with the appropriate skills and experience contribute to the process.
* **Process Efficiency:** Required participant identification ensures that reviews are productive by avoiding unnecessary attendees while ensuring that no critical perspectives are missing.
* **Prevents Gaps in Coverage:** Without explicitly identifying required participants, reviews risk missing critical inputs (e.g., cybersecurity vulnerabilities overlooked due to the absence of a security expert).

---

### **Overall Benefits of the Requirement**

Enforcing these practices improves the efficiency, focus, and impact of software peer reviews, leading to high-quality, reliable products while reducing risks and costs throughout the software lifecycle. Specific benefits include:

1. **Improved Defect Detection and Prevention:**

   * Each part of this requirement contributes to identifying defects and preventing their propagation, reducing costs and risks during later lifecycle phases.
2. **Risk Mitigation for Complex or Mission-Critical Software:**

   * Structured and rigorous peer reviews help uncover flaws in crucial areas such as safety-critical functionality, requirements traceability, interface compatibility, and real-time performance.
3. **Increased Process Discipline and Compliance:**

   * These practices align peer reviews with **NASA’s software engineering standards (e.g., NPR 7150.2, NASA-STD-8739.8)** and help ensure the project adheres to organizational requirements.
4. **Enhancement of Stakeholder Confidence:**

   * Thorough documentation, comprehensive tracking of actions, and structured participation provide assurance to stakeholders that peer reviews contribute to software quality and mission success.
5. **Continuous Improvement of Processes and Products:**

   * Metrics and lessons learned from peer reviews feed into continuous process improvement, strengthening software engineering practices over time.

By ensuring that every peer review follows a standardized and disciplined approach, projects can deliver higher-quality software and successfully meet NASA’s mission objectives.

# 3. Guidance

Software peer reviews and inspections are critical tools for improving software quality, ensuring reliability, and fostering compliance with NASA standards. To meet the requirement for SWE-087, this guidance enhances the discussion of best practices associated with inspections by refining the points already outlined and adding practical insights. These practices emphasize precision, accountability, coverage, and stakeholder alignment to maximize the value of peer reviews.

---

### **3.1 Peer Review Checklist**

#### **Expanded Guidance:**

Using peer review checklists ensures structured and consistent evaluation of work products, enabling teams to address common defects and improve the overall efficiency of reviews.

1. **Benefits of Checklists:**

   * **Systematic Coverage:** Provides reviewers with a structured approach to evaluate artifacts comprehensively, minimizing missed issues.
   * **Continuous Improvement:** Evolve checklists over time by adding defect types that frequently escape early reviews and removing items that no longer yield meaningful findings.
   * **Customization:** Tailor checklists to the artifact type (requirements, design, code, test procedures) and ensure alignment with NASA standards (e.g., coding guidelines, safety-critical measures).
2. **Maintaining Checklists:**

   * **Dynamic Updates:** Regularly update checklists based on defect patterns and lessons learned from past reviews.
   * **Stakeholder Input:** Ensure key stakeholders (e.g., developers, systems engineers, software assurance personnel) contribute to checklist refinement.
   * **Examples of Checklist Items:**
     + Requirements: Are all requirements clear, consistent, complete, and traceable?
     + Design: Are interfaces properly defined and documented?
     + Code: Does the code adhere to coding standards and avoid common defect categories (e.g., logic errors, uninitialized variables)?
     + Tests: Do test procedures adequately cover functional, performance, and edge cases?

---

### **3.2 Readiness and Completion Criteria**

#### **Refined Guidance:**

Establishing readiness and completion criteria ensures that peer reviews are conducted efficiently and effectively, preventing wasted effort and ensuring confidence in outcomes.

1. **Readiness Criteria:**

   * **Artifact Maturity:** Verify the artifact being reviewed is sufficiently complete (e.g., requirements are finalized and approved, design is stable).
   * **Team Preparation:** Ensure participants are equipped with necessary tools, training (e.g., checklist use), and technical expertise.
   * **Quality Thresholds:** Specify minimum quality characteristics for artifacts before scheduling the review (e.g., static analysis results available, traceability established).
2. **Completion Criteria:**

   * **Defect Resolution:** All identified defects are logged, classified (e.g., major, minor), and addressed or dispositioned.
   * **Documentation:** Metrics collected, findings summarized, and follow-up actions recorded.
   * **Review Steps Finalized:** Confirm all planned review steps are performed as specified in the SMP/SDP.
3. **Entrance and Success Criteria Table (Modified):**

| **Entrance Criteria** | **Success Criteria** |
| --- | --- |
| Artifact is approved and finalized for review. |  |
| Reviewers with relevant expertise are onboarded. |  |
| Rules and instructions are agreed upon. |  |
| Preliminary agenda prepared, aligned with project goals. | **Artifact Integrity:** Peer review validates technical integrity, quality, and compliance. |
| Defects or risks identified, classified, and documented. |  |
| Results communicated, and action items tracked to resolution. |  |

**Table G-19 - Peer Review Entrance and Success Criteria**

|  |  |
| --- | --- |
| **Peer Review** | |
| **Entrance Criteria** | **Success Criteria** |
| 1. The product to be reviewed (e.g., document, process, model, design details) has been identified and made available to the review team. 2. Peer reviewers independent from the project have been selected for their technical background related to the product being reviewed. 3. A preliminary agenda, success criteria, and instructions to the review team have been agreed to by the technical team and project manager. 4. Rules have been established to ensure consistency among the team members involved in the peer-review process. 5. \*Spectrum (radio frequency) considerations addressed. | 1. Peer review has thoroughly evaluated the technical integrity and quality of the product. 2. Any defects have been identified and characterized. 3. The results of the peer review are communicated to the appropriate project personnel. 4. Spectrum-related aspects have been concurred to by the responsible Center spectrum manager. |

\*Required per NPD 2570.5.

### **3.3 Action Items**

#### **Refined Guidance:**

Tracking action items ensures that defects identified in peer reviews impact software quality effectively and are resolved in a timely manner.

1. **Tracking Systems:**

   * Maintain a central repository (e.g., an issue tracker like JIRA or an equivalent system) for all peer review action items, defects, and follow-up tasks.
   * Include fields such as defect description, priority, assignee, resolution status, and date of closure.
2. **Impact on Quality:**

   * **Defect Resolution:** Addressing defects improves software quality and reduces risks during later lifecycle phases.
   * **Team Morale:** Demonstrates that the team's efforts lead to actionable improvements, maintaining enthusiasm for participation in peer review processes.
3. **Verification of Closure:**

   * Defects should undergo independent verification to ensure the resolution meets project requirements.

### **3.4 Planning Phase**

#### **Expanded Guidance:**

An effective planning phase lays the foundation for productive peer reviews by establishing the scope, objectives, participants, and methods.

1. **Scope Definition:**

   * Clearly define the boundaries of the review (e.g., specific sections of the requirements document, code modules under review).
   * Prioritize high-risk or safety-critical areas of the product.
2. **Stakeholder Perspectives:**

   * Analyze which perspectives must be represented (e.g., developer, tester, user, systems engineer).
   * Pay special attention to areas requiring unique expertise (e.g., cybersecurity for network systems, usability for end-user interfaces).
3. **Time and Resource Allocation:**

   * Allocate sufficient time for preparation, review sessions, and follow-up activities.
   * Ensure access to resources (e.g., tools for static analysis and traceability assessment).

### **3.5 Use of Checklists**

#### **Expanded Guidance:**

NASA-STD-8739.9 calls out the importance of checklists for structured inspections. Enhanced best practices include:

1. **Customization:**

   * Create specialized checklists for different artifacts (e.g., requirements checklists, safety-critical code checklists).
   * Ensure items are relevant to the type of document under review as well as the perspective each participant represents.
2. **Team-wide Preparation:**

   * Distribute the checklist to all reviewers in advance, ensuring they are familiar with the evaluation criteria before the review meeting.
3. **Checklist Review Cycle:**

   * Periodically evaluate and update checklists based on defect trends, keeping them relevant and efficient.

### **3.6 Inspecting Quality**

#### **Expanded Guidance:**

Peer reviews should focus on inspecting critical quality aspects that align with the goals of the artifact under review.

1. **Quality Focus Areas:**

   * **Requirements:** Completeness, consistency, clarity, and traceability to system needs.
   * **Design:** Modularization, interface definitions, and alignment with requirements.
   * **Code:** Logic correctness, adherence to coding standards, exception handling, and resource management.
2. **Safety and Security Checks:**

   * Evaluate fault detection and mitigation mechanisms, particularly for safety-critical software or cybersecurity measures.

### **3.7 Selecting Stakeholder Representation**

#### **Expanded Guidance:**

Choosing key stakeholders ensures diverse perspectives, unbiased evaluations, and technical expertise.

1. **Representation Principles:**

   * Select reviewers based on technical expertise, domain knowledge, and independence from the artifact author.
   * Ensure participation from disciplines critical to the artifact’s function (e.g., systems engineering for interfaces, software assurance for safety-critical reviews).
2. **Role Assignments:**

   * Inspectors may represent multiple perspectives if team size is limited, but all critical viewpoints should be covered.

### **3.8 Readiness and Completion Criteria**

#### **Expanded Guidance:**

Entrance and exit criteria must be rigorously defined and enforced:

1. **Readiness:** Validate that the artifact and review team meet entrance criteria before initiating the review.
2. **Completion:** Confirm that all planned activities and close-out tasks are completed before declaring the review closed.

### **3.9 Tracking Actions to Resolution**

#### **Expanded Guidance:**

Establish robust processes to track, address, and verify all issues raised during the review:

1. **Documentation:** Maintain a log of all identified actions, including priorities and resolution deadlines.
2. **Verification Process:** Ensure that fixes are independently verified before closing action items.

### **3.10 Identification of Participants**

#### **Expanded Guidance:**

Best practices for participant identification include:

1. **Diversity:** Ensure inspectors reflect diverse viewpoints and technical backgrounds.
2. **Objectivity:** Select participants independently of the artifact author to maintain unbiased evaluations.

By applying these expanded best practices, NASA teams can ensure that software peer reviews and inspections are systematic, impactful, and aligned with mission-critical objectives. These practices strengthen software reliability, safety, and compliance with NPR 7150.2 and NASA-STD-8739.9.

See also [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements).

## 3.11 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)        * [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.12 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Peer Review](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Peer+Review) |

# 4. Small Projects

For small projects, efficiently conducting software inspections is critical to identify defects and improve product quality without overextending resources. Leveraging checklists and tools can streamline the inspection process, reduce manual effort, and ensure consistent results. The following expanded guidance provides actionable recommendations for meeting the requirements for checklists and inspection tools.

---

### **1. Using Inspection Checklists**

#### **Importance of Checklists:**

Checklists serve as essential tools to ensure thorough and consistent inspections of software products. They act as structured memory aids, guiding reviewers to evaluate critical aspects of the product under review while maintaining focus on quality objectives.

1. **Tailored Checklists:**

   * Customize checklists to suit specific inspection artifacts (e.g., requirements, designs, code, or test procedures).
   * Use the comprehensive checklists available at the **Fraunhofer Center website** as a starting point, tailoring them to the needs of your project.
   * Ensure checklists align with NASA standards, such as NPR 7150.2 and NASA-STD-8739.9, and any domain-specific safety or security requirements.
2. **Checklist Maintenance and Continuous Improvement:**

   * Update checklists based on lessons learned from earlier inspections. For instance:
     + Add common defect types that were overlooked in past inspections.
     + Remove items that no longer provide value or are overly redundant.
   * Encourage team feedback on checklist effectiveness after each inspection to refine and improve them.
3. **Examples of Items for Checklists:**

   * **Requirements Inspection:**
     + Are all requirements traceable to higher-level system goals?
     + Are requirements clear, complete, and unambiguous?
   * **Code Inspection:**
     + Does the code comply with organizational coding standards?
     + Are common error types (e.g., logic errors, uninitialized variables) addressed?
   * **Design Inspection:**
     + Are interfaces defined and documented correctly?
     + Are high-complexity modules justified and tested?
4. **Simplified Usage for Small Teams:**

   * Use lightweight checklists that focus on high-risk areas for small projects. Emphasize critical elements to save time while ensuring quality.
   * Assign specific portions of the checklist to different team members to divide the workload efficiently.

---

### **2. Leveraging Tools for Inspections**

#### **Streamlining Inspections with Tools:**

Inspection tools can automate and simplify key aspects of the inspection process, such as defect tracking, documentation, and reporting. Small projects can benefit significantly from using these tools to reduce manual effort and improve accuracy in tracking inspection outcomes.

1. **Tool Selection:**

   * Visit the **"Tools" section** of the **Resources tab** for a curated list of tools suitable for conducting and tracking inspections.
   * Look for tools that fit the scope and budget constraints of small projects. Free or open-source tools can be excellent solutions for smaller teams.
     + Examples:
       - **Defect Tracking Tools:** Jira, Bugzilla, Redmine.
       - **Collaborative Code Review Tools:** GitHub Code Review, Phabricator, Crucible.
       - **Static Analysis Tools:** SonarQube, Coverity, or NASA-specific custom tools.
2. **Key Features to Look For in Inspection Tools:**

   * Ability to log and track defects or issues from identification to closure.
   * Automatic generation of reports for peer review metrics (e.g., number of defects, resolution time).
   * Integration with static analysis and traceability tools for added efficiency.
   * Customization options for adapting workflows and fields to align with peer review procedures.
3. **Recommended Usage Approaches for Small Projects:**

   * **Simplify Integration**: Use tools that integrate well with the existing workflows or software lifecycle tools already in use (e.g., Version Control Systems like Git).
   * **Automate Repetitive Tasks**: Automate data collection and tracking processes where feasible, such as defect entry or status updates.
   * **Provide Lightweight Reports**: Produce short, focused reports from the tool that summarize findings, action items, and next steps to save time during follow-up.

---

### **3. Combining Checklists and Tools: Best Practices**

1. **Checklist Digitization:**

   * Incorporate the checklist framework into a tool of choice, enabling reviewers to collaboratively check off items during the inspection process and track progress.
   * Tools like Microsoft Excel, Google Forms, or dedicated checklist apps for small teams can be used to ensure version control and accessibility.
2. **Integration with Tools:**

   * Use inspection tools to embed checklist items alongside code or document reviews, allowing reviewers to directly link defects to checklist criteria.
   * Track practices such as "checklist coverage" to measure how thoroughly team efforts align with the defined checklist items.
3. **Metrics and Reporting Enhancement:**

   * Integrate results of checklist-based inspections with defect tracking tools to analyze metrics such as:
     + Percentage of checklist items leading to defect identification.
     + Types of defects identified and resolved over time.
   * Use this data to track trends, improve efficiency, and create actionable plans for enhanced inspections.

---

### **4. Practical Examples for Small Projects**

Examples of using checklists and tools:

* **Example 1: Code Inspection**

  + Select a code review tool such as GitHub Code Review or Crucible and integrate a customized checklist for NASA coding standards.
  + Track peer review comments and raise automated issues for identified defects through the tool’s issue tracking system.
  + Use the tool’s metrics feature to generate reports on peer review outcomes and track open/closed defects.
* **Example 2: Requirements Review**

  + Use a shared document tool (e.g., Google Docs, OneDrive) with a checklist for reviewing requirements quality (e.g., completeness, traceability, ambiguity).
  + Log defects directly into a simple defect tracking tool like Redmine or Trello for monitoring during follow-up resolution.
* **Example 3: Lightweight Manual Reviews**

  + If tooling options are limited, leverage spreadsheets for checklist completion and manually input results into a free defect tracking tool or a shared repository. This approach ensures proper documentation even in low-resource environments.

---

### **5. Additional Resources**

* **Fraunhofer Center Checklists:**  
  A comprehensive collection of domain-specific checklists for various work products (requirements, code, design, etc.). Small projects can leverage these as templates instead of creating checklists from scratch.
  + Website: **Fraunhofer Center Maryland ([https://www.fraunhofer.org](https://www.fraunhofer.org/))**
* **Resources Tab - Tools Section:**  
  A curated list of tools for inspections and peer reviews. Regularly updated to include both free and paid tools appropriate for projects of different scales.

---

### **Summary of Best Practices for Small Projects**

* Use **lightweight checklists** tailored to small projects, incorporating only key, high-priority artifact attributes.
* Take advantage of affordable or free **tools for tracking inspections** to save time and reduce manual effort.
* Document findings and defect resolutions systematically to maintain traceability and improve future peer reviews.
* Continuously improve checklists and refine processes based on inspection outcomes and lessons learned.

By effectively using checklists and tools, small projects can maximize the impact of inspections while staying within resource and time constraints. These practices ensure consistent quality control, effective defect identification, and adherence to NASA standards.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-179)

  [Dr. Forrest Shull, at the Fraunhofer Center - Maryland, is a SME on the subject of inspection checklists. He has worked with NASA teams on inspections for several years and can be reached at fshull@fc-md.umd.edu.](https://scholar.google.com/citations?user=S3KDFHEAAAAJ&hl=en "Click to open in new window")

  A variety of articles from Dr. Forrest Shull is available on this cite.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-235)

  [An analysis of defect densities found during software inspections](https://ntrs.nasa.gov/search.jsp?R=19920010193 "Click to open in new window")

  John C. Kelly, Joseph S. Sherif, Jonathan Hops, NASA. Goddard Space Flight Center, Proceedings of the 15th Annual Software Engineering Workshop; 35 p
* (SWEREF-277)

  [Software Formal Inspections Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-87399 "Click to open in new window")

  NASA-STD-8739.9, NASA Office of Safety and Mission Assurance, 2013. Change Date:
  2016-10-07, Change Number: 1
* (SWEREF-421) "A collection of checklists for different purposes," Fraunhofer USA, The University of Maryland. This web page contains several resources for performing software inspections.
* (SWEREF-474)

  [The Empirical Investigation of Perspective-Based Reading,](http://link.springer.com/article/10.1007%2FBF00368702#page-1 "Click to open in new window")

  Basili, V., Green , S., Laitenberger, O., Lanubile, F., Shull, F., Soerumgaard, S., and Zelkowitz, M. Empirical Software Engineering: An International Journal, 1(2): 133-164, 1996.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Peer reviews and inspections play a critical role in improving software quality and ensuring successful mission outcomes. Over time, NASA has accumulated valuable lessons learned from applying these practices on projects of varying complexity and scale. These lessons provide insights into practical challenges, effective strategies, and areas for continuous improvement. The following summarizes key lessons learned related to SWE-087:

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

### **Lesson: (Starliner CFT):****Independent reviews must enforce evidence completeness and cross‑functional insight.**

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

### **Lesson: Early and Frequent Peer Reviews Reduce Costly Rework**

#### **Source:** NASA studies on defect detection rates in early lifecycle phases

#### **Key Insight:**

Conducting peer reviews early in the software development lifecycle (e.g., during requirements and design phases) is significantly more cost-effective than detecting and fixing defects during later phases (e.g., during testing or post-deployment).

* **Details:**

  + Defects left unresolved until later phases can multiply in cost due to ripple effects (e.g., faulty requirements leading to flawed designs, which compound coding errors).
  + Peer reviews of **requirements and design documents** can catch ambiguities, traceability issues, and safety-critical gaps before they cascade into larger problems.
* **Recommendations:**

  + Implement readiness criteria to ensure early-phase work products are mature enough to review effectively.
  + Conduct early reviews of safety-critical requirements to identify areas requiring redundancy, fault isolation, or error mitigation mechanisms.

---

### **Lesson: Checklist Usage is Vital but Must Be Adapted**

#### **Source:** NASA projects reporting inconsistent review results due to generic checklists

#### **Key Insight:**

Generic checklists may miss project-specific risks or critical quality traits. Checklists should be tailored to the specific artifact under review and the unique context of the project.

* **Details:**

  + NASA found that solely relying on standard, unadjusted checklists for safety-critical systems often led to defects escaping detection due to the lack of customized checklist items for specific areas such as real-time constraints or cybersecurity.
  + On smaller projects, overly comprehensive checklists sometimes led to reviews getting bogged down by non-critical items, wasting effort.
* **Recommendations:**

  + **Customization:** Tailor checklists to address mission-specific priorities. For example:
    - Safety-critical software: Add items for fault detection, mitigation logic, and compliance with NASA-STD-8739.8.
    - Interface-heavy software: Ensure checks for parameter mismatch, API issues, and boundary conditions.
  + **Continuous Improvement:** Update checklists based on defect patterns (e.g., recurring issues) identified in past reviews.

---

### **Lesson: Diverse Perspectives Enhance Review Effectiveness**

#### **Source:** Lessons learned from multi-disciplinary peer reviews

#### **Key Insight:**

Inspections that include participants with diverse roles and perspectives (e.g., developer, tester, systems engineer, safety expert) result in better defect detection compared to homogeneous teams.

* **Details:**

  + Peer review effectiveness is significantly enhanced when participants represent both **technical** and **operational viewpoints**. For example, testers can focus on scenarios and edge cases often overlooked by developers.
  + NASA found that reviews without representation from key stakeholders (e.g., systems engineers) frequently missed defects in requirements traceability and interface definitions.
* **Recommendations:**

  + Ensure review teams include members with varying perspectives, including **independent reviewers** for objectivity.
  + Perspective-based reading techniques can be used to simulate the viewpoints of different stakeholders (e.g., user, developer, tester).
  + Establish roles explicitly during planning to avoid oversight of critical areas.

---

### **Lesson: Action Item Tracking is Essential for Review Success**

#### **Source:** NASA experiences where unresolved defects created operational issues

#### **Key Insight:**

Failure to track and resolve action items undermines the impact of peer reviews. Unresolved findings can lead to mission failures or costly rework during later phases.

* **Details:**

  + In some NASA projects, reviews identified critical defects, but follow-up documentation and resolution tracking were insufficient, leading to recurrence of issues in later stages.
  + In complex systems, unaddressed minor defects contributed to cascading failures (e.g., timing delays leading to synchronization errors).
* **Recommendations:**

  + Create a **tracking system** (e.g., defect tracking tool or issue log) to ensure all review findings are resolved before the artifact progresses to the next lifecycle phase.
  + Monitor the status of open defects regularly and verify resolution through independent validation.
  + Close peer reviews only when readiness criteria are satisfied, ensuring no unresolved action items remain.

---

### **Lesson: Readiness Criteria Prevent Premature Reviews**

#### **Source:** NASA projects wasting effort on early peer reviews of incomplete products

#### **Key Insight:**

Without readiness criteria, reviews can be conducted on work products that are incomplete or immature, reducing their effectiveness and wasting time.

* **Details:**

  + On several projects, documents such as requirements specifications or design diagrams were reviewed before they had reached an acceptable level of detail or completeness. This resulted in superficial reviews and missed defects.
  + The increased rework effort outweighed the benefits of early feedback.
* **Recommendations:**

  + Define clear readiness criteria for all work products before scheduling reviews. Criteria might include:
    - Requirements: Fully documented, reviewed for clarity.
    - Code: Built and tested locally, adherence to coding standards.
    - Test Plans: Includes traceability to requirements and coverage of edge cases.
  + Implement automated static analysis tools where feasible to enforce baseline readiness criteria (e.g., code syntax compliance).

---

### **Lesson: Small Projects Benefit from Lean Review Processes**

#### **Source:** Lessons from resource-constrained NASA projects

#### **Key Insight:**

Small projects often lack the resources or time for exhaustive reviews. NASA has observed that focusing review efforts on high-risk areas can maximize impact with minimal resource expenditure.

* **Details:**

  + Resource-constrained projects using "lean peer reviews" focused on mission-critical areas (e.g., interfaces, fault handling), achieving significantly improved defect detection without exhaustive reviews.
  + Applying tools (e.g., static analysis, collaborative code review tools) reduced manual effort for tracking defects.
* **Recommendations:**

  + For small projects: Prioritize peer reviews for:
    - Areas that pose high mission risk (e.g., interfaces, safety-critical functionality).
    - Highly complex or error-prone artifacts (e.g., algorithms with timing constraints).
  + Use automated tools for initial defect detection to streamline the process.
  + Focus reviews on key checklist items rather than all potential issues to save time and resources.

---

### **Lesson: Metrics Drive Process Improvement**

#### **Source:** NASA use of metrics for continuous improvement

#### **Key Insight:**

Collecting and analyzing metrics from peer reviews allows teams to identify trends, improve processes, and reduce recurring defects.

* **Details:**

  + Metrics such as defect density, issue closure rate, and review completion time highlighted recurring problem areas and bottlenecks in defect resolution workflows.
  + Projects using metrics to enhance checklists and peer review process definitions saw reductions in defect rates over time.
* **Recommendations:**

  + Track metrics like:
    - Number and types of defects identified per review.
    - Defect closure rates (time taken to resolve issues).
    - Checklist coverage metrics (percentage of checklist items contributing to findings).
  + Use metrics to refine readiness and completion criteria, review templates, and checklists.

---

### **Lesson: Documentation Enables Successful Follow-Up**

#### **Source:** NASA projects failing follow-up activities due to incomplete review records

#### **Key Insight:**

Thorough documentation is essential to ensure defects and action items are tracked, resolved, and auditable for future reference.

* **Details:**

  + Peer reviews that lacked proper documentation (e.g., incomplete defect logs or missing meeting minutes) resulted in missed follow-up actions or repeating earlier review cycles.
  + The absence of proper documentation also hindered project audits.
* **Recommendations:**

  + Standardize documentation practices for peer reviews, including defect records, action items, participant lists, checklist results, and resolutions.
  + Ensure all documentation is stored in accessible repositories, version-controlled, and auditable as per project management practices.

---

### **Lesson:**  Class D Staffing Model Leading to Insufficient Software Assurance Depth

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

### **Conclusion: Key Takeaways**

NASA's lessons learned emphasize the importance of structured preparation, disciplined execution, and thorough follow-up for peer reviews and inspections. Incorporating these lessons supports defect detection during early lifecycle stages, improves overall software quality, and ensures compliance with NASA standards like NPR 7150.2.

## 6.2 Other Lessons Learned

* Throughout hundreds of inspections and analyses of their results, the Jet Propulsion Laboratory (JPL) has identified key lessons learned which lead to more effective inspections[235](#_tabs-<p></p>), including:
  + Inspections are carried out by peers representing the areas of the life cycle affected by the material being inspected. Everyone participating should have a vested interest in the work product.
  + Management is not present during inspections.
  + Checklists of questions are used to define the task and to stimulate defect findings.
* The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

  + [Static analysis tools should be run not only on flight code (or production code in non-flight cases), but also on code developed for unit test. The issues identified for all code should be properly dispositioned and resolved](https://software.gsfc.nasa.gov/lesson-details/217/). **Lesson Number 217**: The recommendation states: "cFS uses “unit test code” for performing unit testing, as other projects do. This is different than the “flight code” and is used only for unit testing purpose. During the process of updating cFS applications for Gateway, both the flight code and the unit test code were updated. Static analysis (using CodeSonar) was run on all flight code and unit test code, however only the static analysis findings for the flight code were resolved (the findings for the unit test code were not addressed). When the delivery was made to the customer and the customer re-ran the unit tests, they noticed a number of intermittent failures in the tests. These were traced back to uninitialized variables in the unit test code that had been flagged by CodeSonar but never resolved."
  + [Early project software review of SMP deliverables](https://software.gsfc.nasa.gov/lesson-details/298/). **Lesson Number 298**: The recommendation states: "The project's software management plan (SMP) should explain the delivery and review chain for all software products, especially when they are not being delivered directly to the project. If there are more than one or two organizations with separate configuration management systems between the developer and the project review, they should make plans to have the person who is eventually responsible for technical approval of SDP deliverables (e.g., project software engineer or project software lead) be involved in the review process earlier on."

# 7. Software Assurance

**SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking**

5.3.3 The project manager shall, for each planned software peer review or software inspection:

a. Use a checklist or formal reading technique (e.g., perspective-based reading) to evaluate the work products.  
b. Use established readiness and completion criteria.  
c. Track actions identified in the reviews until they are resolved.  
d. Identify the required participants.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project meets the NPR 7150.2 criteria in "a" through "d" for each software peer review.

2. Confirm that the project resolves the actions identified from the software peer reviews.

3. Perform audits on the peer-review process.

## 7.2 Software Assurance Products

Software assurance (SA) personnel play a critical role in evaluating the effectiveness and compliance of peer review processes to ensure high software quality, reliability, and adherence to NASA standards. This improved guidance refines key tasks, metrics, and considerations relevant to SWE-087, and provides additional practical details to enhance the value of software assurance activities.

SA outcomes and deliverables should be well-documented and actionable to ensure that peer reviews improve software quality, trace defects and non-conformances, and address process compliance.

1. **Peer Review Process Audit Report**:

   * Document findings from process audits annually, including observations, areas of improvement, and best practices. Include evidence of compliance with peer review requirements, such as adherence to checklists, entrance/exit criteria, and participant roles.
   * Highlight recurring process gaps or risks, and recommend corrective actions or process improvements.
2. **Peer Review Metrics, Reports, and Data**:

   * Collect peer review performance metrics (e.g., defect detection rates, resolution time, participant preparation effort).
   * Compile peer review results and track trends in metrics to identify recurring issues or inefficiencies.
3. **List of Participants**:

   * Maintain detailed records of attendees for each peer review, including roles (e.g., lead, author, recorder).
   * Verify diverse perspectives and technical expertise are represented, ensuring comprehensive reviews.
4. **Defect/Problem Reporting and Tracking Data**:

   * Use a centralized defect tracking system to monitor, log, and resolve non-conformances identified during peer reviews. Include detailed descriptions and priorities for each defect.
5. **Process Audit Reports**:

   * Conduct and document yearly peer review audits to evaluate compliance, effectiveness, and process maturity. Identify process weaknesses and recommend changes to review structure, checklist usage, or participant selection.

## 7.3 Metrics

Effective metrics provide insight into the quality and efficiency of the peer review process and help establish actionable improvements. Use these metrics to track trends, identify bottlenecks, and ensure project adherence to NASA standards:

1. **Process Non-Conformances**:

   * Track the number of process non-conformances identified during peer reviews by lifecycle phase (e.g., requirements, design, code, test). Analyze trends over time to detect recurring issues or phase-specific bottlenecks.
2. **Participant Preparation Time**:

   * Record preparation time for review and audit participants. Ensure that participants are reviewing materials adequately while optimizing effort allocation.
3. **Defect Closure Time**:

   * Measure the time required to close peer review and audit non-conformances by priority level (e.g., high, medium, low). Trends in closure rates can indicate the efficiency of defect resolution processes.
4. **Participation Metrics**:

   * Compare the number of participants who were invited to reviews versus those who attended. Evaluate their technical preparation and contributions using pre-defined checklists and post-review summaries.
5. **Defect Density and Classification**:

   * Analyze the number of non-conformances identified per work product, categorized by type (e.g., logic errors, traceability issues, standards violations). Compare findings with team size to ensure work product coverage.
6. **Trends Analysis**:

   * Monitor trends such as open vs. closed action items, lifecycle phase defect ratios, and audit findings over time. Use this data to improve the peer review process, optimize checklists, and establish metrics thresholds for compliance audits.
7. **Compliance Audits Metrics**:

   * Track the number of audits planned versus performed to ensure auditing occurs regularly and comprehensively. Review audit non-conformance resolution trends to identify process maturity improvements.

## 7.4 Guidance

#### **Task 1: Verify the Project Meets Key Peer Review Conditions**

Software assurance personnel must ensure that the project complies with four key activities that define the effectiveness of peer reviews and inspections.

1. **Use of Checklists**:

   * Confirm checklists are prepared in advance and tailored to the specific artifact being reviewed (e.g., requirements, design, code).
   * Validate that checklists represent diverse stakeholder perspectives (e.g., requirements developer, designer, tester, operations team).
   * Ensure checklists are used during reviews as a guide for defect identification and compliance verification.
2. **Entrance and Exit Criteria**:

   * **Entrance Criteria:** Verify that preconditions for review are satisfied:
     + Review materials are distributed, checklist prompt questions are provided, and participants have reviewed the material in advance.
     + Participants with relevant technical expertise and diverse roles are selected, and resources/logistics for review are prepared.
   * **Exit Criteria:** Confirm peer reviews meet closure conditions:
     + All defects and issues are recorded, prioritized, and tracked.
     + Metrics are collected, and decisions regarding re-inspection or closure are documented.
     + Action items are assigned and tracked until resolution.
3. **Resolution Tracking**:

   * Ensure software assurance independently tracks peer review action items and verifies their closure. Use metrics to monitor the resolution timeline and efficiency and identify delays or bottlenecks.
4. **Participant Selection**:

   * Validate that participants are selected based on technical knowledge, familiarity with the asset, and representation of diverse perspectives.
   * Ensure optimal team size (5–9 participants) for efficiency and thoroughness. Avoid including direct managers of the artifact to reduce hesitation in reporting defects.

---

#### **Task 2: Verify Action Item Closure**

Ensure all issues identified during peer reviews are closed before review completion. Follow steps for independent verification of defect resolutions:

1. **Tracking Tools:**

   * Recommend using a defect tracking tool to document non-conformances systematically (e.g., JIRA, GitHub Issues). Include status updates, priority levels, assigned personnel, and deadlines.
2. **Follow-Up Meetings:**

   * Conduct post-review meetings with the review lead to confirm action item closures and verify no outstanding issues remain.

---

#### **Task 3: Conduct Annual Peer Review Process Audits**

SA personnel must audit the peer review process annually to evaluate compliance, effectiveness, and identify areas for improvement.

1. **Audit Execution:**

   * Confirm compliance with peer review protocols outlined in SWE-087 (e.g., checklists usage, entrance/exit criteria, participant selection).
   * Identify any activities not performed and analyze their impact on defect detection efficiency.
2. **Audit Follow-Up:**

   * Share audit findings promptly with the project team and recommend improvements (e.g., new checklist items, process adjustments, tool integration).
   * Track responses to recommendations and verify implementation over time.
3. **Process Maturity Evaluation:**

   * Monitor trends in compliance audit metrics (i.e., open versus closed audit non-conformances, recurring audit findings) to identify process maturity improvements.

---

### **See Also**

Refer to the following related guidance and resources:

* **Topic 8.18 – SA Suggested Metrics:** Guidance on meaningful measurements to enhance SA activities.
* **Topic 8.12 – Basics of Software Auditing:** Best practices for effective audits across project workflows.
* **NASA SPAN Tools:** Inspection tools, templates, and checklists for streamlined peer review processes.

---

### **Key Takeaways**

Software assurance personnel are essential in ensuring that peer reviews meet SWE-087 requirements and enhance software quality. By focusing on tailored metrics, rigorous task verification, independent defect tracking, and annual audits, software assurance can drive continuous improvement and compliance in peer review processes, ensuring high-quality deliverables for NASA missions.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)        * [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is required to demonstrate compliance with the requirements of SWE-087. This evidence should be documented, organized, and readily available to ensure transparency and to support auditing, verification, and project reviews. Below is a breakdown of the types of objective evidence typically required to demonstrate adherence to the practices outlined in this requirement.

---

### **1. Peer Review Planning Evidence**

This evidence demonstrates that peer reviews were well-planned in accordance with SWE-087 requirements.

* **Artifacts:**
  + Peer review plan or schedule, including roles, timelines, and planned work products for review.
  + Entrance and exit criteria for each peer review.
  + Documentation of the work product type being reviewed (e.g., requirements specification, design document, code module, test plan).
  + List of participants, including their roles (e.g., moderator, recorder, reviewer) and qualifications.

---

### **2. Checklist Usage Evidence**

This evidence shows that appropriate checklists were developed, used, and maintained during peer reviews.

* **Artifacts:**
  + Copies of checklists used during each peer review (e.g., requirements inspection checklist, design checklist, code review checklist).
  + Historical versions of checklists to show evidence of continuous improvement (e.g., items added or removed based on lessons learned).
  + Completed checklists for each peer review, identifying areas checked and any issues recorded.

---

### **3. Evidence of Review Preparation**

This evidence demonstrates that participants prepared for the peer review effectively.

* **Artifacts:**
  + Confirmation that work products were distributed to all participants prior to the peer review.
  + Evidence of participant preparation, such as annotations or notes made by reviewers.
  + Meeting invitations and materials (e.g., background materials, review announcements).

---

### **4. Peer Review Meeting Minutes and Records**

This evidence documents the activities and outcomes of peer review sessions.

* **Artifacts:**
  + Meeting minutes or detailed summaries of each peer review session, including:
    - Topics discussed.
    - Issues raised and defects identified.
    - Actions taken during the review.
  + Attendance records confirming participant involvement.

---

### **5. Defect Identification and Tracking Evidence**

This evidence shows that defects were identified, classified, and tracked to closure.

* **Artifacts:**
  + Defect logs or issue tracking reports, showing:
    - Summary and description of defects or issues.
    - Classification of defects (e.g., major, minor).
    - Assigned personnel for resolution.
    - Current status (e.g., open, in progress, closed).
    - Date of detection and closure.
  + Trend analysis reports on defect metrics (e.g., open vs. closed defects over time, severity of defects by artifact type).

---

### **6. Entrance and Exit Criteria Compliance Evidence**

This evidence demonstrates that entrance and exit criteria were consistently applied for all peer reviews.

* **Artifacts:**
  + Completed entrance criteria checklists, confirming readiness of the work product and the review team.
  + Completed exit criteria checklists or validation reports, confirming the following:
    - All defects were logged and prioritized.
    - Metrics were collected and reported.
    - Any required re-inspection was planned and scheduled, if necessary.
    - All action items were resolved or appropriately dispositioned.

---

### **7. Peer Review Metrics and Reports**

This evidence ensures that appropriate metrics were collected, analyzed, and used for process improvement.

* **Artifacts:**
  + Peer review metrics reports, showing:
    - Number of defects, classified by type (e.g., requirements, design, code).
    - Number of defects per work product reviewed.
    - Number of defects per participant.
    - Time to close defects or action items.
    - Effort metrics (e.g., preparation time, time spent in the review meeting).
  + Trend analysis reports highlighting process strengths and areas for improvement.
  + Graphs or charts summarizing metrics for lifecycle phases or review types.

---

### **8. Action Item Tracking and Closure**

This evidence shows that action items and issues from peer reviews were resolved in a timely manner.

* **Artifacts:**
  + Action item logs, including:
    - Description of actions identified during the review.
    - Assigned personnel and deadlines.
    - Evidence of closure (e.g., updated work products showing issue resolution).
  + Verification logs from software assurance ensuring closure of all action items.
  + Status reports or dashboards showing open vs. closed actions over time.

---

### **9. Audit and Process Compliance Evidence**

This evidence demonstrates that the peer review process was audited, and compliance was evaluated.

* **Artifacts:**
  + Peer review process audit reports, including findings, non-conformances, and recommendations for improvement.
  + Evidence that findings from audits were addressed, such as process revisions or checklist updates.
  + Compliance audit records showing adherence to NASA-STD-8739.9 and NPR 7150.2.

---

### **10. Participant Selection Evidence**

This evidence documents that appropriate participants were selected for peer reviews to ensure diverse perspectives and expertise.

* **Artifacts:**
  + Documentation of participant roles (e.g., requirements engineer, coder, tester, software assurance personnel).
  + Participant qualifications (e.g., relevant experience, domain knowledge).
  + Evidence of diverse stakeholder representation in the peer review team (e.g., independent reviewers, cross-functional team members).

---

### **11. Process Improvement Evidence**

This evidence demonstrates that lessons learned from peer reviews were implemented to improve review processes.

* **Artifacts:**
  + Lessons learned reports documenting key takeaways from peer reviews.
  + Updates made to checklists, processes, or training materials based on findings from reviews.
  + Evidence of process refinements, such as updated peer review procedures or tools.

---

### **12. Tool Usage Evidence**

This evidence demonstrates that tools were used to streamline peer review processes, track defects, and analyze metrics.

* **Artifacts:**
  + Tool reports, such as:
    - Static analysis logs.
    - Defect tracking system outputs (e.g., JIRA, GitHub Issues).
    - Metrics collected by process automation tools.
  + Configuration control reports showing how tools were used during the peer review lifecycle.

---

### **Summary of Objective Evidence**

The table below summarizes key categories of evidence for SWE-087 compliance:

| **Category** | **Examples of Artifacts** |
| --- | --- |
| Peer Review Planning Evidence | Peer review plan, entrance/exit criteria, participant list, logistics. |
| Checklist Usage Evidence | Completed checklists, tailored templates, checklist version history. |
| Defects and Action Items | Defect logs, action item tracking reports, verification evidence. |
| Metrics and Reporting | Metrics reports, trends analysis, participant engagement analysis. |
| Audit Evidence | Audit reports, findings, and process improvement plans. |
| Process Refinement | Lessons learned, updated procedures, and checklist refinements. |
| Tool Usage Evidence | Reports/logs from peer review tools (e.g., JIRA, static analysis reports, dashboards). |

---

By maintaining comprehensive objective evidence for SWE-087, you can demonstrate that peer reviews and inspections are thorough, effective, and aligned with NASA's software engineering standards and mission-critical needs. This evidence is essential for audits, stakeholder confidence, and project success.

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
