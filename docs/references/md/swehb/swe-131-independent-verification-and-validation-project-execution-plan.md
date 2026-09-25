# SWE-131 - Independent Verification and Validation Project Execution Plan

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695492. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan

SWE-131 - Independent Verification and Validation Project Execution Plan

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695492)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695492&showCommentArea=true&showComments=true#addcomment)

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

3.6.3 If software IV&V is required for a project, the project manager, in consultation with NASA IV&V, shall ensure an IPEP is developed, approved, maintained, and executed in accordance with IV&V requirements in NASA-STD-8739.8.

## 1.1 Notes

The IV&V Advisory Board will review the scope of NASA IV&V activities on an annual basis as part of the budget planning process.

## 1.2 History

Click here to view the history of this requirement: SWE-131 History

SWE-131 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.1.3 If a project is selected for software Independent Verification and Validation (IV&V) by the NASA Chief, Safety and Mission Assurance, the NASA IV&V program shall develop an IV&V Project Execution Plan (IPEP). |
| Difference between A and B | Removes the requirement for the OSMA Chief selection of projects for IV&V;  otherwise, no change |
| B | 3.6.3 If software IV&V is performed on a project, the project manager shall ensure that an IV&V Project Execution Plan (IPEP) is developed. |
| Difference between B and C | Added to the requirement that the IPEP is "negotiated, approved, maintained, and executed." |
| C | 3.6.3 If software IV&V is performed on a project, the project manager shall ensure an IPEP is developed, negotiated, approved, maintained, and executed. |
| Difference between C and D | Clarified requirement and referenced the NASA standard for software safety and assurance. |
| D | 3.6.3 If software IV&V is required for a project, the project manager, in consultation with NASA IV&V, shall ensure an IPEP is developed, approved, maintained, and executed in accordance with IV&V requirements in NASA-STD-8739.8. |

## 1.3 Applicability Across Classes

This requirement applies to all NASA projects that have a software Independent Verification & Validation (IV&V) requirement.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 2. Rationale

Independent Verification and Validation (IV&V) is essential for ensuring the safety, reliability, and mission success of software systems in NASA projects. The IV&V Project Execution Plan (IPEP) serves as the foundational document that defines how IV&V activities will be planned, executed, and maintained throughout the software development life cycle. By requiring the creation, approval, and execution of an IPEP when software IV&V is mandated, this requirement ensures that IV&V efforts are systematically aligned with project-specific risks, objectives, and requirements.

The IPEP is a cornerstone of the IV&V process, providing clarity, structure, and accountability. This requirement ensures that the project manager, in consultation with the NASA IV&V team, establishes and maintains an IPEP to guide IV&V efforts in accordance with NASA standards. By doing so, projects can effectively address software-related risks, maintain alignment with mission assurance goals, and enhance the overall quality and reliability of mission-critical software systems.

## 2.1 Alignment with NASA's Risk Reduction Strategy:

* + Software IV&V is a risk mitigation activity, and its scope and rigor are guided by the unique software risks of a project. The IPEP acts as the roadmap for these activities, ensuring they are tailored to address the highest-priority risks identified in the project. Without a dedicated IPEP, there is a risk of misaligned or incomplete IV&V activities, potentially compromising the effectiveness of the risk mitigation strategy.

## 2.2 Clear Communication and Expectations:

* + The IPEP documents the objectives, methods, and deliverables of the IV&V effort, facilitating clear communication between the IV&V Provider, the project manager, and key stakeholders. This fosters a shared understanding of IV&V priorities, including the expected scope of analysis, timing of deliverables, and integration with project milestones. By having an IPEP in place, the project team ensures that IV&V efforts are well-coordinated with the project’s broader assurance activities.

## 2.3 Compliance with NASA Standards:

* + NASA-STD-8739.8 establishes the standard processes and expectations for IV&V activities, including the development of an IPEP. Adhering to this requirement ensures consistency with NASA's proven IV&V methodologies and policies, reducing variability in IV&V execution across projects. This consistency enhances the credibility, independence, and effectiveness of IV&V assessments.

## 2.4 Lifecycle Tailoring and Iterative Updates:

* + The IPEP is not a static document. It is designed to be maintained and updated throughout the project life cycle in response to changes in project scope, risks, or schedule adjustments. This flexibility ensures that IV&V activities remain dynamic and responsive to evolving project needs, particularly in the face of shifting risks or new information.

## 2.5 Approval and Oversight Enhance Accountability:

* + Requiring the IPEP to be approved by relevant authorities ensures its alignment with project objectives and IV&V best practices. This approval process strengthens oversight and accountability, providing confidence that the IV&V activities will be executed effectively and deliver valuable insights for decision-making.

## 2.6 Integrated and Effective Execution of IV&V:

* + Ensuring the IPEP is not only developed but also executed reinforces its role as a practical and operational tool. The execution of the IPEP ensures that IV&V activities, including defect tracking, risk analysis, and validation of critical system behaviors, are performed in a timely and comprehensive manner. This real-time integration between the IV&V Provider and the project team maximizes the impact of IV&V findings and recommendations.

## 2.7 Improved Decision Support:

* + Through its structured approach, the IPEP guides IV&V activities to generate evidence-based conclusions on the fitness of the software for nominal and off-nominal operations. These independent insights empower project managers and stakeholders to make informed, data-driven decisions, which is critical for reducing development risks and ensuring mission success.

# 3. Guidance

The IV&V IPEP is a critical tool that establishes the framework for effective IV&V execution, guiding activities to reduce software-related risks and achieve project objectives. With a focus on independence, rigorous analysis, risk-based prioritization, and close coordination with project teams, the IV&V process delivers high-confidence assurance that mission-critical software is developed safely, securely, and reliably. Proper application of this guidance ensures consistency with NASA standards and enhances the likelihood of mission success.

IV&V is a technical discipline of software assurance, which employs rigorous analysis and testing methodologies identifying objective evidence and conclusions to provide a second independent assessment of critical products and processes throughout the life cycle. The secondary evaluation of products and processes throughout the life cycle contributes to demonstrating whether the software is fit for nominal operations (required functionality, safety, dependability, etc.), and off-nominal conditions (response to faults, responses to hazardous conditions, etc.). The goal of the IV&V effort is to contribute to the assurance conclusions to the project and stakeholders based on evidence found in software development artifacts and risks associated with the intended behaviors of the software.

## 3.1 Rationale for IV&V

The primary purpose of Independent Verification and Validation (IV&V) in NASA projects is to reduce the risk of software-related failures, ensuring mission safety, reliability, and success. IV&V provides a comprehensive and independent review, analysis, and testing of software (and potentially software interactions with hardware) to confirm that:

1. **Requirements Verification**: The requirements are correctly defined and aligned with stakeholder and mission needs.
2. **Functionality and Security Validation**: The system/software correctly implements required functionality, safety, and security specifications.

## 3.2 Purpose and Role of the IV&V Project Execution Plan (IPEP)

#### **Dual Purpose of the IPEP**

1. **Communication Tool**:
   * The IPEP establishes clear expectations for collaboration between the IV&V Provider and the project stakeholders.
   * It documents interfaces, roles, responsibilities, deliverables, communication paths, and reporting methods, fostering transparency and accountability.
2. **Operational Document**:
   * The IPEP provides a strategic roadmap for IV&V activities, outlining the processes, schedules, and resources necessary to fulfill the requirements of NASA-STD-8739.8.
   * It serves as a living document, guiding the IV&V Provider’s work while remaining adaptable to evolving project needs, risks, and constraints.

#### **Key Components of the IPEP**:

The IPEP includes but is not limited to:

* Goals and objectives of IV&V for the specific project.
* IV&V approach, scope, and activities to be performed.
* Identification and prioritization of artifacts for review, driven by risk assessment.
* Description of milestones, deliverables, and schedules aligned with the project life cycle.
* Data exchange requirements, such as access to artifact repositories and risk management systems.
* Roles and responsibilities for coordination between the IV&V Provider, the project office, and the software development organization.

## 3.3 Key Principles of the IV&V Process

### 3.3.1 Independence in IV&V

For IV&V to remain credible and effective, it must adhere to the principles of independence:

1. **Technical Independence:**

   * The IV&V team operates autonomously from the development team, providing an unbiased assessment.
   * By establishing a unique perspective, the IV&V team is better equipped to detect subtle flaws that may be overlooked by those closely involved in development.
2. **Managerial Independence:**

   * The IV&V team is organizationally distinct from the program and development management, ensuring it can make independent decisions regarding its activities, focus areas, and reporting.
   * Findings are delivered directly to project management without any approval or influence from the development organization.
3. **Financial Independence:**

   * The IV&V team must have a budget that is controlled independently from the development organization.
   * This ensures that funding constraints do not compromise the scope or rigor of IV&V efforts.

### 3.3.2 Risk-Based Focus

Risk drives the allocation of IV&V resources and effort:

* Full IV&V across all software systems is often infeasible due to financial, schedule, or resource limitations.
* Instead, the scoping and prioritization of IV&V activities are **risk-based**, with a focus on:
  1. Safety-critical and mission-critical software.
  2. Components with high complexity or uncertainty.
  3. Areas prone to defects with significant potential impact.

### 3.3.3 IV&V throughout the Life Cycle

* IV&V activities begin **early in the software development life cycle (SDLC)** to identify and address issues during the requirements and design phases when fixes are less costly.
* IV&V continues through construction, integration, testing, and operations, ensuring that both nominal and off-nominal conditions are assessed.

### 3.3.4 Continuous Feedback and Adaptability

* IV&V activities evolve iteratively, leveraging feedback from milestone reviews, defect reports, and updated risk assessments to adjust scope and rigor as required.
* The IPEP itself is updated every six months or as significant mission or IV&V changes occur (e.g., schedule delays, budget modifications).

## 3.4 Guidelines for IV&V Coordination with Projects

### 3.4.1. Supporting IPEP Development

* The **IV&V Provider** is responsible for developing the IPEP, which includes coordination with the **Project Manager** and other stakeholders.
* Project teams must provide timely and complete access to:
  1. Relevant artifacts, such as requirements documents, design configurations, and test plans.
  2. Risk management tools and artifact repositories.
  3. Heritage review data from similar projects (if applicable).

### 3.4.2. Maintaining the IPEP

* The IPEP is reviewed and revised based on:
  + Changes to project milestones or schedules.
  + IV&V resource constraints or budget adjustments.
  + Emerging risks or changes to software/system requirements.
* Regular reviews (every six months or as needed) ensure the IPEP remains aligned with both project and IV&V objectives.

### 3.4.3. Integration with Milestones and Reviews

* Implementation of IV&V is integrated into the project's milestone reviews, ensuring findings are available to support informed decisions. These include:
  1. Life cycle reviews (e.g., SRR, PDR, CDR, TRR, and DR) where IV&V evaluates artifacts and provides analysis results.
  2. Peer reviews and software inspections, where IV&V identifies risks and defects before artifacts are finalized.

## 3.5 Responsibilities of the IV&V Provider

#### **Core IV&V Deliverables**

* Producing clear and actionable insights that address:
  1. Product correctness (Does the software do what it is supposed to do?).
  2. Product safety and security (Does the software avoid unsafe or unintended behaviors?).
  3. Response to off-nominal conditions (Is fault tolerance implemented effectively?).

#### **Access and Transparency**

* Ensuring proper data exchange and continued visibility into artifacts and project risks.
* Documenting and reporting findings and defects to the project in a timely manner, supporting quick mitigation and resolution.

#### **Continuous Improvement**

* Capturing metrics and lessons learned to refine IV&V processes.
* Conducting post-project reviews to evaluate and improve IV&V practices for future missions.

## 3.6 Guidelines for Effective Collaboration

1. **Clear Roles and Responsibilities:**

   * Ensure alignment between the IV&V Provider, project management, and software development teams regarding reporting structures, access rights, and interfaces.
2. **Efficient Communication:**

   * Establish communication protocols early, as outlined in the IPEP, to facilitate effective exchanges of information and timely issue resolution.
3. **Proactive Risk Management:**

   * Leverage IV&V insights to continuously monitor and mitigate evolving software risks.

## 3.7 Table of Contents for a Typical IPEP

The typical IPEP Table of Contents is shown below:

If any process in this document conflicts with any document in the NASA Online Directives Information System (NODIS), this document shall be superseded by the NODIS document.  Any reference document external to NODIS shall be monitored by the Process Owner for current versioning.

1. **Introduction**
   1. **Document Purpose** - Describe the overall IV&V project and define the basic agreements for the partnership between the IV&V Team and the Project.
   2. **Intended Audience** - Describe the intended audience of the document.
   3. **Document Organization** - Describe the document’s organization and structure.
2. **IV&V Overview**
   1. **IV&V Goals and Objectives** - Describe at a high level what the IV&V efforts are trying to accomplish overall for the mission.
   2. **IV&V Approach** - Describe the IV&V approach that will be used for validation- and verification-related analyses. Include the artifact types generally required for specific analysis objectives.
   3. **IV&V Scope and Focus** - Provide the scope and focus of the project. Scope is the parts of the project that should be considered for IV&V assurance services.  Focus is the set of in-scope items that will receive IV&V assurance services.
3. **Roles, Responsibilities, and Interfaces**
   1. **Roles, Responsibilities, and Interfaces** - Describe the various roles, responsibilities, and interfaces for the project. These roles and responsibilities may be described in terms of personnel within the IV&V Program and personnel within the Project. Include formal and informal lines of communication.
   2. **IV&V Team** - Describe the IV&V team with their associated roles and responsibilities. At a minimum, there should be an IV&V Project Manager and IV&V analysts. Provide contact information for the IV&V leadership team.
   3. **Project Personnel** - Establish that the project will provide an IV&V Point of Contact (POC) for formal interactions between the IV&V Team and the Project. At a minimum, there should be a Project Manager, IV&V POC, and Chief SMA Officer (CSO). Provide contact information for the Project leadership team.
4. **IV&V Products and Communication and Reporting Methods** - The IV&V Team generates various products and utilizes various communication and reporting methods/processes throughout the lifecycle. Describe the IV&V products and associated communication and reporting methods/processes.
   1. **IV&V Products**
      1. **Analysis Conclusions** - Briefly describe the process for documenting and communicating Assurance Conclusions. Provide a summary of the content to be included in the Assurance Conclusions. Assurance Conclusions should describe the analysis(es) performed and the results, including the associated assurance objectives, technical issues, risks, assumptions, forward work, and other caveats and limitations found or understood during the analysis(es).
      2. **Analysis Reports** - Briefly describe the process for documenting and communicating Analysis Reports. Provide a summary of the content to be included in the Analysis Reports. Analysis Reports should document the results of the analysis(es) performed and describe the Project artifacts used, a high-level description of the process, approach, tools used, results, and conclusions.)
      3. **Technical Issue Memorandums** - A TIM is the formal mechanism the IV&V Team uses to document one or more instances of defects (i.e., issues) identified within a development artifact, and subsequently formally communicates defects to the Project. Describe the processes for documenting, reviewing, and tracking TIMs to resolution. Include Impact and Severity Ratings with descriptions. See **S3105: Guidelines for Writing IV&V TIMs** [613](#tabs-4).
      4. **Risks** - Describe how the IV&V Team documents and tracks risks to resolution. Include how the Risks are formally communicated to the Project.
   2. **IV&V Communication and Reporting Methods** - Briefly describe the communication and reporting methods / processes (formal and informal) between the IV&V Team and the Project.
      1. **Item Tracking, Monitoring, and Escalation** - Briefly describe the IV&V team’s process for tracking, monitoring, and escalating all data (including issues, risks, presentations, reports) to the Project.
      2. **Lifecycle Review Presentations** - Briefly describe the IV&V team’s approach to supporting formal Project milestone reviews and communicating the status of IV&V assurance efforts.  Include the reviews to be supported and the responsible IV&V POC.
      3. **Agency/Mission Directorate/Center Management Briefings** - Briefly describe the IV&V team’s approach for providing status to the Project Stakeholders. Include the reviews and boards to be supported and the responsible IV&V POC.
      4. **Routine Tag-ups** - Briefly describe the IV&V team’s approach for supporting tag-ups (e.g., status, task requests, analysis results).
      5. **Development Reviews and Working Groups Support** - Briefly describe the IV&V team’s approach for supporting Project working groups or development reviews. Include how analysis results will be communicated through these forums.
      6. **NASA Audit, Assessment, and Review Support** - Briefly describe the IV&V team’s approach for supporting any NASA led review or audit functions.
5. **IV&V Capability-Level Software Risk Assessment Results** - Based on the mission objectives, provide the results and rationale of the capability-level risk assessment. For each Capability, include the Impact Score, Likelihood Score, and Risk Score.
6. **IV&V Entity-Level Software Risk Assessment Results** - Based on the Capability-Level Software Risk Assessment, provide the results of the software entity-level risk assessment, which extends the risk assessment to the software components (i.e., entities) that implement the system behaviors necessary to accomplish mission capabilities. For each Entity, include the Impact Score, Likelihood Score, and Risk Score.
7. **IV&V Heritage Review  & Applicable Lessons Learned** - Briefly describe the process for completing a heritage review and communicating the results.  Provide a summary of the content to be included. An IV&V heritage review is intended to survey prior IV&V projects for applicability of their results to the current project and to document references to applicable project results for use in planning and scoping activities, along with early IV&V analysis activities.  The process for completing an IV&V heritage review should include an assessment of the current project’s assertion of mission heritage, a survey of former IV&V projects for those missions and listing of missions with similar characteristics, and a survey of previous IV&V risk assessments, issues, risks, and lessons learned documented for each of these missions, where available, to determine their applicability to the current project.  
     
   The purpose of the Heritage Review (HR) process is to learn from our collective experiences to maximize the value of IV&V’s contributions to NASA and other stakeholders. It also ensures that a promotion of faults do not cascade from one project to another through inherited or reuse of hardware interfaces and software. IV&V’s promotion of due diligence necessitates this review in an effort to promote knowledge that understanding may be gained of previous faults, past developer assumptions and on-orbit anomaly impacts. It is with this foundational visage a more complete system understanding of the new project can be obtained, leading to higher fidelity planning and scoping, analysis and ultimately assurance provided to the mission and Agency. A Heritage Review template is available at: <https://www.nasa.gov/wp-content/uploads/2023/08/ivv-t2104-ver-basic-07-28-2022.docx?emrc=6e4e35>
8. **Assurance Design** - Define the assurance design. Include Assurance Objectives, an outline of focus areas, and the approaches considered for performing technical tasks. Provide a summary of each IV&V activity to be performed. The content for this section may be in a separate document or embedded directly into this one. Identify the relevant document(s) and include a link to the location.
9. **Reference Documentation** - Identify titles, numbers, locations, and/or versions of documentation specified in the plan. Also, include any other relevant Project documentation.
10. **Acronyms** - In alphabetic order, define all abbreviations and acronyms used in the plan.
11. **Fiscal Year <XX> IV&V Summary** - Recommended.
    1. **FY <XX> Assurance Goals and Objectives** - Identify at a high level the assurance goals and objectives of the IV&V efforts for the applicable FY.
    2. **FY <XX> Targeted External Milestones** - List the key development project milestones. Depending on the development project, this may include milestones such as SRR, PDR, CDR, MRR, ORR, Launch Date, etc.
    3. **FY<XX> Internal Milestones** - List key internal milestones for the IV&V efforts. These will vary depending on the project, but may include mid-year risk assessment update, IV&V kickoff meeting, next year planning meeting with development Project, etc.
    4. **FY <XX> Schedule** - Provide a snapshot or summary of the IV&V Schedule for the applicable FY efforts.
    5. **FY <XX> Risks** - Provide a listing of perceived risks associated with the execution of the plan for the applicable year. This data only needs to be at the summary level as these risks will be managed via the IV&V Risk Review Board.
    6. **FY <XX> IV&V Technical Reports** - List specific technical reports planned for the fiscal year. These should be included in the FY <XX> Schedule. For relative dates, use working days unless there is a true requirement for calendar days to be used, e.g., a contractual or legal requirement.  Regardless, be specific as to the type of days intended.

See the IV&V Project Execution Plan (IPEP) Template that’s available from the Templates section of the IV&V Management System (IMS) [411](#_tabs-<p></p>) site.  It’s available in Word and PDF formats.

See also Topic [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content), [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan), [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts), 

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts)        * [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Software Quality Assurance](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Software+Quality+Assurance) |

# 4. Small Projects

An IV&V Project Execution Plan (IPEP) is vital to ensuring the effective integration and management of Independent Verification and Validation (IV&V) activities within the project. For **small projects**, meeting this requirement can be challenging due to limited resources, tight schedules, or smaller-scale software systems. However, tailoring the IPEP to the scope and complexity of the project can ensure compliance while reducing unnecessary burdens.

By developing a **streamlined, manageable IPEP**, small projects can meet the compliance requirements of NASA-STD-8739.8 while tailoring IV&V efforts to their size, scope, and complexity. Close coordination with the NASA IV&V team, prioritization of mission-critical aspects, and the use of efficient tools and practices will allow small projects to effectively execute IV&V requirements within their constrained resources.

This approach ensures IV&V adds value to small projects without imposing unnecessary burdens, reducing risks while supporting successful mission outcomes.

## 4.1 What is an IPEP?

The **IV&V Project Execution Plan (IPEP)** is a document that defines the details of IV&V activities, outlining the scope, objectives, resources, schedule, deliverables, and communication processes between the project team and the IV&V team. It ensures alignment with **NASA-STD-8739.8**, which defines NASA’s IV&V requirements.

For small projects, the IPEP should be **right-sized** to reflect the project's size, budget, complexity, and criticality. The IPEP for small projects can be simplified while still describing how essential IV&V tasks will be planned, executed, and tracked.

## 4.2 Simplified Small Project Approach

The following guidance is tailored for small projects where resources and scope are limited but IV&V is still required:

### 4.2.1 Collaborate Closely with the NASA IV&V Team

The project manager must work collaboratively with the **NASA IV&V Program** to discuss resource constraints and tailoring options for the IPEP.

* **Initial Consultation:** Schedule a kick-off meeting with the NASA IV&V team as soon as IV&V is identified as a requirement (typically early, around **Key Decision Point A (KDP-A)**).
* **Define the Scope:** With the IV&V team, align on *which aspects* of the project’s software require IV&V. Small projects should focus primarily on:
  + Mission-critical and safety-critical software components.
  + High-risk functionalities or complex integrations.
* **Tailoring IV&V Processes:** Request guidance from the IV&V team on how to **scale** IV&V activities to fit the scope, budget, and risks of the project.

**Key Goal:** Avoid over-allocating resources to unnecessary IV&V activities while ensuring compliance with IV&V requirements.

### 4.2.2 Develop and Document an IPEP Tailored to a Small Project

Although an IPEP is required, it does not need to be a lengthy or overly complex document for small projects. The IPEP must establish the roles, responsibilities, and required IV&V activities in a streamlined manner.

1. **Essential Elements to Include in the IPEP:**

   * **Scope of IV&V:** Clearly outline the specific software components being subjected to IV&V. For small projects:
     + Prioritize safety-critical and mission-critical systems.
     + Include only the necessary objectives and analyses, such as requirement validation or safety assurance evaluation.
   * **Roles and Responsibilities:** Define the responsibilities of the project team and the IV&V team. Highlight communication protocols, reviewing authorities, and decision-making processes.
   * **IV&V Activities and Deliverables:**
     + Identify key IV&V tasks (e.g., code reviews, risk analysis, testing oversight).
     + Define deliverables, such as IV&V reports or risk assessments, and specify expected formats and timelines.
   * **Schedule and Milestones:** Create a high-level timeline for IV&V activities that aligns with the project schedule.
   * **Tailored Compliance to NASA-STD-8739.8:** Explain how compliance with IV&V requirements will be achieved in a streamlined manner.
   * **Resource Allocation:** Plan for budget and personnel resources devoted to IV&V.
2. **Use Simplified Templates:**

   * Request IPEP templates from the NASA IV&V Program that are designed for smaller projects.
   * Streamline sections to avoid unnecessary effort (e.g., fewer formal reviews, reduced reporting requirements).

### 4.2.3 Focus on Critical IV&V Tasks

Small projects may not need the full suite of IV&V activities typically performed on large, complex missions. Instead, focus the IPEP on the **minimum essential IV&V activities** required for compliance, such as:

1. **Requirements Analysis and Validation:**

   * Ensure requirements are complete, testable, and meet mission-critical needs.
   * Verify alignment between requirements, design, and test plans.
2. **Safety and Risk Analysis:**

   * Evaluate safety-critical functionality and identify high-risk areas where failure could harm mission goals.
3. **Code and Design Reviews (Selectively):**

   * Use IV&V to review high-priority software modules or interfaces essential to safety or mission success.
4. **End-to-End Testing Oversight:**

   * Validate that test plans and test cases cover all safety-critical and mission-critical requirements.

### 4.2.4 Simplify IPEP Approval, Maintenance, and Execution

1. **Approval Process:**

   * Submit the tailored IPEP to the **NASA IV&V Program** for **simplified review and approval**. Clearly articulate why the tailored approach is appropriate for the small project’s scope and risks.
   * Engage project stakeholders to review the key aspects of the IPEP (e.g., IV&V scope, milestones).
2. **Maintenance:**

   * Regularly review the IPEP, especially at key milestones (e.g., design reviews, integration events, testing).
   * Update the IPEP when:
     + Significant project changes occur.
     + New safety-critical risks are identified.
3. **Execution and Tracking:**

   * Assign a primary point of contact (POC) from both the project team and the IV&V team to oversee IPEP execution.
   * Track progress against the IPEP’s defined milestones and IV&V deliverables.
   * Simplify reporting by focusing on key outcomes (e.g., defect mitigation reports, risk closure summaries, or interim assessments).

### 4.2.5 Leverage Tools and Resources

For small projects, leveraging automated tools, shared IV&V resources, and NASA-provided infrastructure can streamline the IPEP process and reduce overhead.

* **Use NASA’s IV&V Tools:**  
  These include automated code review tools, static analysis tools, and requirement validation systems.
* **Shared Expertise:**  
  Request shared or part-time IV&V personnel who can divide time across multiple small projects, ensuring cost efficiency.
* **Lessons Learned and Best Practices:**  
  Incorporate guidance from NASA’s **Lessons Learned database (e.g., LL 723, 6656, and others)** to tailor the IPEP.

### 4.2.6 Document Outcomes and Lessons Learned

* For compliance purposes, maintain well-documented outcomes of IV&V activities specified in the IPEP.
* Record your lessons learned for future small projects, especially around tailoring efforts, budget allocation, and execution challenges.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-003)

  [NASA Independent Verification and Validation Technical Framework](https://www.nasa.gov/wp-content/uploads/2023/11/ivv-09-1-independent-verification-and-validation-technical-framework-ver-s-08-28-2023.pdf?emrc=201d9b "Click to open in new window")

  IVV 09-1, Revision S, NASA Independent Verification and Validation Program, Effective Date: October 18, 2023
* (SWEREF-028)

  [IV&V Project Execution Plan (IPEP) Template,](https://swehb.nasa.gov/download/attachments/16450397/t2103_-_ver_f.pdf?api=v2 "Click to open in new window")

  T2103, NASA Independent Verification and Validation Program, 2011.
* (SWEREF-045)

  [Project Management,](https://www.nasa.gov/sites/default/files/ivv_09-4_-_ver_ag.pdf "Click to open in new window")

  IVV 09-4, Version: AG, Effective Date: June 24, 2014
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-180)

  [The Role Of Independent V&V In Upstream Software Development Processes,](http://www.cs.toronto.edu/~sme/papers/1996/NASA-IVV-96-015.pdf "Click to open in new window")

  Easterbrook, Steve (1996), Proceedings from 2nd World Conference on Integrated Design and Process Technology (IDPT). Retrieved on February 28, 2012 from http://www.cs.toronto.edu/fm/pubs/pdf/easterbrook96c.pdf.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-257)

  [NASA Engineering and Program/Project Management Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=4E "Click to open in new window")

   NPD 7120.4E, NASA Office of the Chief Engineer, Effective Date: June 26, 2017, Expiration Date: June 26, 2022
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-411)

  [IV&V Management System (IMS)](https://www.nasa.gov/centers/ivv/ims/home/index.html "Click to open in new window")

  NASA IV&V Facility.
* (SWEREF-518)

  [Independent Verification and Validation of Embedded Software](https://llis.nasa.gov/lesson/723 "Click to open in new window")

  Public Lessons Learned Entry: 723.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

**LL‑SW‑02 — Heritage Knowledge vs. Heritage Code**

* **Source LL ID(s):** IVV‑10
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** Teams treated legacy code as “plug‑and‑play,” underestimating adaptation effort and verification for new architectures and interfaces.
* **Lesson Learned:** Leverage heritage **experience**, not **code** blindly; plan/budget as new development; invite IV&V **early** to requirements TIMs and merges to surface gaps sooner.
* **Evidence/Observation:** Late requirement updates and delivery slips affected dependent systems; IV&V participation earlier would have found gaps.
* **Cause(s):** Under‑scoped changes; late IV&V engagement.
* **Recommendation/Corrective Action:** Require **early IV&V engagement** (SWE‑141/131), define reuse criteria (LL‑SW‑01), and enforce full traceability from stakeholder needs through tests (SWE‑050/052/072).
* **Implementation Guidance:** Add IV&V coordination to contracts and schedules; include IV&V in requirements reviews; maintain authoritative baselines and snapshots.
* **Success Criteria/Verification:** Fewer late requirement changes; on‑schedule deliveries; reduced rework and nonconformances.
* **Applicability/Scope:** Any reuse effort across new mission contexts.
* **Related Standards/Requirements:** **SWE‑141, SWE‑131, SWE‑050, SWE‑052**.

**LL‑SW‑03 — Define Artifact Access vs. Delivery Expectations**

* **Source LL ID(s):** IVV‑07
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** It took ~6 months to obtain limited artifact “access,” insufficient for tool‑based analysis; effectiveness dropped sharply.
* **Lesson Learned:** Contracts must explicitly define **access** (portal read) vs. **delivery** (files for tooling), with rationale and intended use (traceability, FDIR analysis).
* **Evidence/Observation:** Tool‑driven analysis needs full artifacts to compute relationships across thousands of requirements; delays impede phase‑aligned feedback.
* **Cause(s):** Ambiguous contractual language; unclear IV&V needs.
* **Recommendation/Corrective Action:** Specify artifact delivery cadence, formats, and completeness (requirements snapshots, designs, code, tests) and repository permissions.
* **Implementation Guidance:** Tie to **SWE‑050** (requirements captured/maintained), **SWE‑052/072** (traceability across artifacts), **SWE‑131/141** (IV&V planning/execution).
* **Success Criteria/Verification:** IV&V receives complete, tool‑readable baselines at defined intervals; measurable reduction in analysis latency.
* **Applicability/Scope:** All mission/safety‑critical developments.
* **Related Standards/Requirements:** **SWE‑013, SWE‑050, SWE‑052, SWE‑072, SWE‑131, SWE‑141**.

**LL‑SW‑04 — Provide Direct Read‑Only Access to Code Repositories**

* **Source LL ID(s):** IVV‑04
* **Discipline(s):** Software Assurance, IV&V, Software Engineering
* **Context/Background:** Teams that granted IV&V read‑only repository access (e.g., GitLab) enabled near‑real‑time analysis and reduced packaging delays.
* **Lesson Learned:** Use industry‑standard practice: **IV&V read‑only repo access** to current versions for in‑phase feedback, ancillary build info, and improved coverage.
* **Evidence/Observation:** Latency dropped from 6+ months to near real‑time for VSM/CSM/MSM teams.
* **Cause(s):** Reliance on manual deliveries; limited visibility.
* **Recommendation/Corrective Action:** Require repo access in contracts; add secure, role‑based credentials; define supported branching and tagging schemes.
* **Implementation Guidance:** Align with **SWE‑131/141** (IV&V), trace requirements to code (**SWE‑064/052**), and ensure build artifacts support test traceability (**SWE‑072**).
* **Success Criteria/Verification:** IV&V confirms clean builds; timely defect reports aligned with development sprints; reduced false positives.
* **Applicability/Scope:** All projects using SCM.
* **Related Standards/Requirements:** **SWE‑064, SWE‑072, SWE‑131, SWE‑141**.
* **References:** Gateway S&MA LL deck; NASA SWEHB.

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

**LL‑SW‑07 — Share Requirement Implementation Status with IV&V**

* **Source LL ID(s):** IVV‑06
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** IV&V needs to know whether a requirement is implemented/in progress/to‑do to avoid premature findings and missed analyses.
* **Lesson Learned:** Provide IV&V **live implementation status** via JIRA/Jama (or equivalent) aligned to features/sprints.
* **Evidence/Observation:** Improved precision when IV&V had requirement‑level visibility.
* **Cause(s):** Limited visibility into development progress.
* **Recommendation/Corrective Action:** Grant read access to status dashboards; map requirement IDs to code/test tickets.
* **Implementation Guidance:** Maintain **SWE‑052/072** traceability across requirements and tests; capture status in plans (**SWE‑013**).
* **Success Criteria/Verification:** Fewer “false‑positive” IV&V issues; synchronized analyses; timely defect resolution.
* **Applicability/Scope:** All software with tracked requirements.
* **Related Standards/Requirements:** **SWE‑013, SWE‑050, SWE‑052, SWE‑072, SWE‑131, SWE‑141**.

**LL‑SW‑10 — Early and Continuous IV&V Integration**

* **Source LL ID(s):** IVV‑03
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** IV&V entered post‑CDR on HALO/PPE; early defects were missed; rework and schedule churn increased.
* **Lesson Learned:** Integrate IV&V **from formulation** through test; deliver artifacts continuously to enable in‑phase analyses.
* **Evidence/Observation:** Early IV&V identifies requirements/design risks when changes are cheapest.
* **Cause(s):** Perception IV&V slows development; absent IV&V provisions in contracts.
* **Recommendation/Corrective Action:** Include IV&V requirements in acquisition; define PEP milestones; align sprint cadences.
* **Implementation Guidance:** **SWE‑131/141** (IV&V planning/execution), **SWE‑013** (project plans), **SWE‑018** (reviews).
* **Success Criteria/Verification:** Consistent, timely IV&V findings; reduced late rework; improved test readiness.
* **Applicability/Scope:** All mission/safety‑critical software.
* **Related Standards/Requirements:** **SWE‑131, SWE‑141, SWE‑013, SWE‑018**.

#### **Independent Verification and Validation of Embedded Software (Use of IV&V Procedures)**

**Lesson Learned Number: 723**

* **Summary of the Lesson:**  
  The use of Independent Verification and Validation (IV&V) processes provides significant value in ensuring that software is developed in compliance with its original specifications, performs as intended in the operational mission environment for which it was designed, and avoids unintended behaviors that could jeopardize mission success. By identifying and addressing software errors early in the development lifecycle, IV&V reduces the cost and effort associated with correcting defects found in later phases, such as testing, integration, or operations. Incorporating IV&V early also improves the overall quality, safety, and reliability of the software systems by rigorously validating their functionality, performance, and alignment to mission objectives.
* **Relevance to the IV&V Plan (IPEP):**  
  This lesson underscores the importance of having a well-defined and effectively executed **IV&V Project Execution Plan (IPEP)**. A comprehensive IPEP ensures that IV&V activities are properly scoped, planned, and implemented early in the software development lifecycle when defect detection and correction are least costly and most impactful. The lesson highlights the value of a proactive IV&V process in managing risks for safety-critical and mission-critical systems, especially for embedded software where unintended behaviors can result in catastrophic outcomes.
* **Key Takeaways for IV&V Plans:**

  1. **Plan for Early Integration:**  
     The IPEP should prioritize IV&V activities during early lifecycle phases, such as requirements analysis and detailed design reviews, to enable the identification and correction of defects before they propagate downstream. Early IV&V intervention reduces overall project costs and prevents schedule delays.
  2. **Focus on Critical Functions:**  
     An effective IPEP will emphasize IV&V for high-risk areas, such as safety-critical software, mission-critical algorithms, and software interfaces, ensuring these components meet design specifications and perform reliably in operational conditions.
  3. **Maintain Rigorous Standards:**  
     The lesson aligns with NASA-STD-8739.8, which establishes that IV&V processes must rigorously verify compliance with software requirements, validate software behavior in intended mission environments, and confirm the absence of unintended outcomes.
* **Connection to Cost and Risk Mitigation:**  
  The lesson highlights a core driver for the IV&V plan: **error correction costs increase exponentially as the development lifecycle progresses**. By having a structured IPEP in place, project managers can promote early discovery of issues, minimize defect propagation, and manage risks proactively, significantly improving software quality and ensuring mission success.

---

### **Conclusion**

This lesson demonstrates the essential link between a well-executed IV&V plan and the achievement of high-quality, reliable software. For project managers, it serves as a reminder that the **IV&V Project Execution Plan (IPEP)** is not just a procedural document but a critical enabler for delivering safe, successful, and cost-effective mission software.

## 6.2 Other Lessons Learned

* **Software IV&V**
  + IV&V approaches and resources must align with the program risk posture.
  + A closed-loop, auditable, corrective action toolset and process must be used to manage all IV&V identified issues and risks.
* The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

  + [IV&V Project Execution Plan Development (IPEP) - timing when review comments are due](https://software.gsfc.nasa.gov/lesson-details/280/). **Lesson Number 280**: The recommendation states: "If IV&V is to provide support on your program, review the language carefully in the IPEP to ensure that IV&V is required to submit inputs/feedback within the regular Contract Data Requirement List (CDRL)  delivery or peer review timing cycle."

# 7. Software Assurance

**SWE-131 - Independent Verification and Validation Project Execution Plan**

3.6.3 If software IV&V is required for a project, the project manager, in consultation with NASA IV&V, shall ensure an IPEP is developed, approved, maintained, and executed in accordance with IV&V requirements in NASA-STD-8739.8.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the IV&V Project Execution Plan (IPEP) exists.

## 7.2 Software Assurance Products

To ensure proper implementation and oversight of Independent Verification and Validation (IV&V) activities for a project, the following software assurance products are critical:

1. **Evidence of Confirmation of the IPEP**

   * Verification that the **IV&V Project Execution Plan (IPEP)** has been developed, approved, and implemented is essential. This evidence demonstrates that IV&V activities are aligned with project requirements and risks.
   * Confirmation involves validating that the key elements of the IPEP address the project’s specific needs, as defined in **NASA-STD-8739.8** [278](#_tabs-<p></p>) , section 4.4, and that appropriate stakeholders are engaged in its development and execution.
2. **IV&V Planning and Risk Assessment**

   * Documentation of the IV&V planning and risk assessment is required to determine the **scope, priority, and rigor** of IV&V activities.
   * This includes identifying mission-critical and safety-critical software-dependent behaviors, high-risk areas, and in-scope artifacts to guide decision-making and allocation of resources. It ensures that IV&V focuses on areas of greatest risk, as outlined in [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation).
3. **IV&V Project Execution Plan (IPEP)**

   * The IPEP is the primary deliverable governing IV&V activities, describing the detailed plans, activities, levels of rigor, and roles applicable to the project. It provides traceability to risk assessments and prioritizes IV&V actions to meet project assurance goals.
   * The IPEP is both a **planning document** and an **accountability tool** that must reflect ongoing IV&V work and any significant IV&V scope changes.

## 7.3 Metrics

To measure compliance and effectiveness of executing the **Independent Verification and Validation (IV&V) Project Execution Plan (IPEP)**, the following software assurance metrics can be used. These metrics not only track adherence to the requirement but also provide insights into how well IV&V processes are achieving their intended objectives in terms of software quality, risk reduction, and project success.

These software assurance metrics provide a robust framework for measuring the effectiveness and compliance of IV&V processes in executing the IPEP. By tracking these metrics, project managers and IV&V teams can identify problem areas, optimize resource allocation, and ensure IV&V contributes meaningfully to the safety, reliability, and success of mission-critical software systems.

### 7.3.1 IPEP Development and Approval Metrics

#### **a. IPEP Timeliness**

* **Definition:** Measure the time taken to develop and approve the IPEP relative to project milestones (e.g., Key Decision Points [KDP-A, B, C, etc.]).
* **Formula:**  
  [ \text{IPEP Timeliness (%) = (Days IPEP Delivered Before Due Date / Days Allotted for IPEP Development)} \times 100 ]
* **Purpose:** Ensures the timely preparation of the IPEP, allowing IV&V activities to begin early in the lifecycle when they are most effective.

#### **b. Completeness of the IPEP**

* **Definition:** Percentage of required elements in NASA-STD-8739.8 that are fully addressed in the IPEP.
* **Formula:**  
  [ \text{Completeness (%) = (Number of Complete IPEP Sections / Total Required Sections)} \times 100 ]
* **Purpose:** Confirms the IPEP includes all critical elements such as scope, schedule, deliverables, roles, and communication processes.

### 7.3.2 Engagement Metrics

#### **a. IV&V Plan Execution Rate**

* **Definition:** Percentage of planned IV&V activities (as outlined in the IPEP) successfully executed within the project timeline.
* **Formula:**  
  [ \text{Execution Rate (%) = (Number of IV&V Activities Completed / Number of IV&V Activities Planned)} \times 100 ]
* **Purpose:** Tracks the alignment between planned and completed IV&V tasks, ensuring the project follows the IPEP as intended.

#### **b. IV&V Scope Coverage**

* **Definition:** Percentage of mission-critical software components explicitly subjected to IV&V.
* **Formula:**  
  [ \text{Scope Coverage (%) = (Number of Critical Components Reviewed by IV&V / Total Critical Components)} \times 100 ]
* **Purpose:** Ensures IV&V efforts focus on high-priority mission-critical and safety-critical components, maximizing impact.

### 7.3.3 Risk and Defect Metrics

#### **a. Defect Identification Effectiveness**

* **Definition:** Percentage of total software defects identified by IV&V during project development.
* **Formula:**  
  [ \text{Defect Identification (%)} = \left( \frac{\text{Defects Identified by IV&V}}{\text{Total Defects Identified}} \right) \times 100 ]
* **Purpose:** Measures the effectiveness of IV&V in identifying major defects, particularly in mission-critical systems.

#### **b. Risk Mitigation Rate**

* **Definition:** Percentage of risks identified by IV&V activities that were successfully mitigated.
* **Formula:**  
  [ \text{Risk Mitigation Rate (%) = (Number of IV&V Identified Risks Mitigated / Total IV&V Identified Risks)} \times 100 ]
* **Purpose:** Tracks how effectively the IPEP-guided IV&V activities reduce risks associated with software safety and mission success.

#### **c. Severity of Defects Detected by IV&V**

* **Definition:** Measure of the severity (low, medium, high, critical) of defects identified by IV&V to indicate the focus on mission-critical areas.
* **Purpose:** Demonstrates how IV&V prioritizes defect detection in high-risk components.

### 7.3.4 Compliance Metrics

#### **a. Compliance with NASA-STD-8739.8**

* **Definition:** Percentage of IV&V activities and processes successfully aligned to NASA’s IV&V standard requirements.
* **Formula:**  
  [ \text{Compliance Rate (%) = (Number of Compliant IV&V Activities / Total Planned IV&V Activities)} \times 100 ]
* **Purpose:** Documents adherence to NASA-STD-8739.8 as defined in the IPEP and ensures consistency with established standards.

#### **b. Test Result Verification**

* **Definition:** Percentage of test reports validated by IV&V that confirm software meets stated requirements.
* **Formula:**  
  [ \text{Verification Rate (%) = (Number of Requirements Verified by Testing / Total Requirements Validated by IV&V)} \times 100 ]
* **Purpose:** Verifies testing completeness and alignment between requirements and actual software performance.

### 7.3.5 Quality Metrics

#### **a. Requirements Validation Rate**

* **Definition:** Percentage of project requirements validated by IV&V through formal reviews and analyses.
* **Formula:**  
  [ \text{Validation Rate (%) = (Number of Validated Requirements / Total Number of Requirements)} \times 100 ]
* **Purpose:** Ensures that requirements validation is robust enough to identify gaps, ambiguities, and risks.

#### **b. Defect Density Reduction**

* **Definition:** The reduction in defect density (defects per KLOC) resulting from IV&V interventions during the software lifecycle.
* **Formula:**  
  [ \text{Defect Density Reduction (%) = \left( \frac{\text{Pre-IV&V Defect Density - Post-IV&V Defect Density}}{\text{Pre-IV&V Defect Density}} \right) \times 100} ]
* **Purpose:** Tracks the impact of IV&V in improving overall software quality and defect reduction.

#### **c. Enforceability of Safety-Critical Rules**

* **Definition:** Percentage of safety-critical rules enforced by IV&V identified as fully compliant.
* **Purpose:** Confirms compliance and stability for software components whose failure would impact mission or safety

### 7.3.6 Cost and Efficiency Metrics

#### **a. Cost Avoidance due to Early Defect Detection**

* **Definition:** Measures how much cost was avoided by detecting defects during early life-cycle phases through IV&V intervention compared to later stages (or post-launch).
* **Formula:**  
  [ \text{Cost Avoidance ($) = (Defects Detected Early \times Cost Savings per Defect Detected Early)} ]
* **Purpose:** Quantifies the financial benefits of early IV&V involvement.

#### **b. Overall IV&V Cost Efficiency**

* **Definition:** Percentage of total project budget spent on IV&V activities, compared to its planned allocation.
* **Formula:**  
  [ \text{Cost Efficiency (%) = \left( \frac{\text{Actual IV&V Costs}}{\text{Budgeted IV&V Costs}} \right) \times 100} ]
* **Purpose:** Ensures IV&V activities are performed efficiently within cost constraints.

### 7.3.7 Delivery Metrics

#### **a. Timeliness of IV&V Deliverables**

* **Definition:** Percentage of IV&V deliverables (reports, findings, risk logs) completed on or before the scheduled due dates.
* **Formula:**  
  [ \text{Timeliness (%) = \left( \frac{\text{Deliverables Completed on Time}}{\text{Total Scheduled Deliverables}} \right) \times 100} ]
* **Purpose:** Tracks adherence to the project timeline and ensures IV&V conclusions are delivered promptly for decision-making.

#### **b. Final IV&V Validation Coverage**

* **Definition:** Percentage of all IPEP-identified IV&V goals achieved by the end of the lifecycle.
* **Formula:**  
  [ \text{Validation Coverage (%) = \left( \frac{\text{IV&V Goals Met}}{\text{Total IPEP Goals}} \right) \times 100} ]
* **Purpose:** Ensures that IV&V activities align with the scope and deliverables outlined in the IPEP.

## 7.4 Guidance

### 7.4.1 Confirm if IV&V is Required for the Project ([SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) SWE-141):

* IV&V may be required for a project depending on factors such as its **Risk Classification, Software Classification (per NPR 7150.2), and mission-criticality**.
* Refer to **section 4.4 of NASA-STD-8739.8** for IV&V requirements. This section outlines the criteria and responsibilities associated with selecting and performing IV&V.
* Software assurance personnel must confirm that projects requiring IV&V follow all necessary processes, including the development of an IPEP and alignment with IV&V requirements.

### 7.4.2 Ensure the IV&V Planning and Assessment Process is Conducted:

* If IV&V is required, the **IV&V Provider** must conduct an initial **IV&V planning and risk assessment**. This critical step involves:
  + **Identifying Scope of Effort**: Defining the system/software behaviors, components, and interfaces to be reviewed.
  + **Risk Analysis**: Assessing mission complexity, safety-criticality, and areas where software defects might result in severe consequences.
  + **Sources of Risk**: Addressing risks related to software safety, performance, security, test coverage, reliability, and fault tolerance.

### 7.4.3 Oversee the Development and Maintenance of the IPEP:

* The **IV&V Provider** is responsible for creating and maintaining the IPEP in coordination with the project management team. The IPEP achieves the following objectives:
  + Documents activities, methods, and criteria for performing IV&V.
  + Establishes roles, responsibilities, and reporting paths between the IV&V team and project stakeholders.
  + Provides ongoing alignment with project milestones, deliverables, and data-exchange requirements.
* Software assurance should:
  + Ensure the IPEP is reviewed and approved in a timely manner.
  + Confirm the IPEP reflects all critical IV&V activities and accommodates any changes in project scope, timeline, or available resources.

### 7.4.4 Maintenance and Updates of the IPEP:

* As a **living document**, the IPEP requires regular updates to reflect evolving project needs and IV&V priorities. Updates are necessary under the following circumstances:
  + Changes in project milestones, schedules, or scope.
  + Significant changes in the IV&V Provider’s resource availability (e.g., budgetary constraints or personnel reassignments).
  + Revisions to IV&V tasks, deliverables, or methodologies based on new risks or findings.
* The IPEP must accurately document all planned and completed IV&V activities to ensure traceability and accountability.

### 7.4.5 Verify IV&V Provider Compliance with NASA Standards:

* Software assurance personnel should confirm that IV&V activity implementation aligns with the requirements outlined in **NASA-STD-8739.8**, section 4.4.
* The IV&V Provider must demonstrate adherence to these seven core activity areas:
  1. **Planning and Risk Assessment**: Crafting a structured approach informed by risk.
  2. **Development of the IPEP**: Ensuring thorough and project-specific documentation of IV&V activities.
  3. **Analysis Results and Reporting**: Delivering findings, risk assessments, and assurance data to stakeholders.
  4. **Participation in Project Reviews**: Providing insights into software development milestones.
  5. **Engagement in Peer Reviews and Inspections**: Contributing to early-stage defect detection efforts.
  6. **Risk Tracking and Communication**: Ensuring continuous monitoring and early reporting of emerging risks.
  7. **Defect and Issue Management**: Documenting, tracking, and ensuring remediation of defects identified by IV&V.

### 7.4.6 Validation of IV&V’s Analytical Focus:

* The IV&V Provider’s responsibilities encompass verification and validation of the following:
  + Software requirements (correctness, completeness, traceability).
  + Security mitigations and safety-critical functionality.
  + Compatibility between requirements, architecture, detailed design, and code.
  + Test artifacts (plans, test cases, environments, etc.) to ensure that all system capabilities undergo proper testing under both **nominal** and **off-nominal** conditions.
  + Verification of defect resolution and risk mitigation.

### 7.4.7 Monitor IV&V Execution:

* Once planning is complete and the IPEP is formally approved, software assurance teams must monitor execution to ensure:
  + The IV&V Provider adheres to the activities and timelines documented in the IPEP.
  + Analysis results are delivered in line with project needs and milestones.
  + Identified issues and risks are promptly communicated and addressed.

### 7.4.8 Assess Plan Maintenance and Accuracy:

* Regularly review the IPEP to confirm it reflects real-time IV&V progress.
* Maintenance of the IPEP ensures IV&V efforts remain agile and responsive to any changes in:
  + Project scope or mission priorities.
  + Identified risks or challenges.

### 7.4.9 IV&V and Software Assurance Relationship

Software assurance plays a critical role in supporting and overseeing IV&V activities. This includes:

* Verifying that the IPEP captures all required IV&V processes.
* Ensuring that IV&V findings are integrated into the project’s overall assurance and risk strategies.
* Auditing the execution of IV&V requirements to confirm compliance with NASA standards.

### 7.4.10 Conclusion

Software assurance ensures that IV&V activities are correctly scoped, implemented, and maintained throughout the life cycle of the project. The IPEP, as the cornerstone of IV&V planning and execution, is a critical tool for managing software risks, ensuring independent assessments, and safeguarding mission success. With proper oversight and alignment to standards, these activities enhance transparency, communication, and effectiveness, significantly reducing the likelihood of software-related failures.

Confirm that the IV&V plan contains the following items:

See the IV&V Project Execution Plan (IPEP) Template that’s available from the Templates section of the IV&V Management System (IMS) [411](#_tabs-<p></p>) site.  It’s available in Word and PDF formats.

Guidelines for the content of an IV&V Execution Plan are:

### 7.4.11 Table of Contents for a Typical IPEP

**The typical IPEP Table of Contents is shown below:

If any process in this document conflicts with any document in the NASA Online Directives Information System (NODIS), this document shall be superseded by the NODIS document.  Any reference document external to NODIS shall be monitored by the Process Owner for current versioning.

1. **Introduction**
   1. **Document Purpose** - Describe the overall IV&V project and define the basic agreements for the partnership between the IV&V Team and the Project.
   2. **Intended Audience** - Describe the intended audience of the document.
   3. **Document Organization** - Describe the document’s organization and structure.
2. **IV&V Overview**
   1. **IV&V Goals and Objectives** - Describe at a high level what the IV&V efforts are trying to accomplish overall for the mission.
   2. **IV&V Approach** - Describe the IV&V approach that will be used for validation- and verification-related analyses. Include the artifact types generally required for specific analysis objectives.
   3. **IV&V Scope and Focus** - Provide the scope and focus of the project. Scope is the parts of the project that should be considered for IV&V assurance services.  Focus is the set of in-scope items that will receive IV&V assurance services.
3. **Roles, Responsibilities, and Interfaces**
   1. **Roles, Responsibilities, and Interfaces** - Describe the various roles, responsibilities, and interfaces for the project. These roles and responsibilities may be described in terms of personnel within the IV&V Program and personnel within the Project. Include formal and informal lines of communication.
   2. **IV&V Team** - Describe the IV&V team with their associated roles and responsibilities. At a minimum, there should be an IV&V Project Manager and IV&V analysts. Provide contact information for the IV&V leadership team.
   3. **Project Personnel** - Establish that the project will provide an IV&V Point of Contact (POC) for formal interactions between the IV&V Team and the Project. At a minimum, there should be a Project Manager, IV&V POC, and Chief SMA Officer (CSO). Provide contact information for the Project leadership team.
4. **IV&V Products and Communication and Reporting Methods** - The IV&V Team generates various products and utilizes various communication and reporting methods/processes throughout the lifecycle. Describe the IV&V products and associated communication and reporting methods/processes.
   1. **IV&V Products**
      1. **Analysis Conclusions** - Briefly describe the process for documenting and communicating Assurance Conclusions. Provide a summary of the content to be included in the Assurance Conclusions. Assurance Conclusions should describe the analysis(es) performed and the results, including the associated assurance objectives, technical issues, risks, assumptions, forward work, and other caveats and limitations found or understood during the analysis(es).
      2. **Analysis Reports** - Briefly describe the process for documenting and communicating Analysis Reports. Provide a summary of the content to be included in the Analysis Reports. Analysis Reports should document the results of the analysis(es) performed and describe the Project artifacts used, a high-level description of the process, approach, tools used, results, and conclusions.)
      3. **Technical Issue Memorandums** - A TIM is the formal mechanism the IV&V Team uses to document one or more instances of defects (i.e., issues) identified within a development artifact, and subsequently formally communicates defects to the Project. Describe the processes for documenting, reviewing, and tracking TIMs to resolution. Include Impact and Severity Ratings with descriptions. See **S3105: Guidelines for Writing IV&V TIMs** [613](#tabs-4).
      4. **Risks** - Describe how the IV&V Team documents and tracks risks to resolution. Include how the Risks are formally communicated to the Project.
   2. **IV&V Communication and Reporting Methods** - Briefly describe the communication and reporting methods / processes (formal and informal) between the IV&V Team and the Project.
      1. **Item Tracking, Monitoring, and Escalation** - Briefly describe the IV&V team’s process for tracking, monitoring, and escalating all data (including issues, risks, presentations, reports) to the Project.
      2. **Lifecycle Review Presentations** - Briefly describe the IV&V team’s approach to supporting formal Project milestone reviews and communicating the status of IV&V assurance efforts.  Include the reviews to be supported and the responsible IV&V POC.
      3. **Agency/Mission Directorate/Center Management Briefings** - Briefly describe the IV&V team’s approach for providing status to the Project Stakeholders. Include the reviews and boards to be supported and the responsible IV&V POC.
      4. **Routine Tag-ups** - Briefly describe the IV&V team’s approach for supporting tag-ups (e.g., status, task requests, analysis results).
      5. **Development Reviews and Working Groups Support** - Briefly describe the IV&V team’s approach for supporting Project working groups or development reviews. Include how analysis results will be communicated through these forums.
      6. **NASA Audit, Assessment, and Review Support** - Briefly describe the IV&V team’s approach for supporting any NASA led review or audit functions.
5. **IV&V Capability-Level Software Risk Assessment Results** - Based on the mission objectives, provide the results and rationale of the capability-level risk assessment. For each Capability, include the Impact Score, Likelihood Score, and Risk Score.
6. **IV&V Entity-Level Software Risk Assessment Results** - Based on the Capability-Level Software Risk Assessment, provide the results of the software entity-level risk assessment, which extends the risk assessment to the software components (i.e., entities) that implement the system behaviors necessary to accomplish mission capabilities. For each Entity, include the Impact Score, Likelihood Score, and Risk Score.
7. **IV&V Heritage Review  & Applicable Lessons Learned** - Briefly describe the process for completing a heritage review and communicating the results.  Provide a summary of the content to be included. An IV&V heritage review is intended to survey prior IV&V projects for applicability of their results to the current project and to document references to applicable project results for use in planning and scoping activities, along with early IV&V analysis activities.  The process for completing an IV&V heritage review should include an assessment of the current project’s assertion of mission heritage, a survey of former IV&V projects for those missions and listing of missions with similar characteristics, and a survey of previous IV&V risk assessments, issues, risks, and lessons learned documented for each of these missions, where available, to determine their applicability to the current project.  
     
   The purpose of the Heritage Review (HR) process is to learn from our collective experiences to maximize the value of IV&V’s contributions to NASA and other stakeholders. It also ensures that a promotion of faults do not cascade from one project to another through inherited or reuse of hardware interfaces and software. IV&V’s promotion of due diligence necessitates this review in an effort to promote knowledge that understanding may be gained of previous faults, past developer assumptions and on-orbit anomaly impacts. It is with this foundational visage a more complete system understanding of the new project can be obtained, leading to higher fidelity planning and scoping, analysis and ultimately assurance provided to the mission and Agency. A Heritage Review template is available at: <https://www.nasa.gov/wp-content/uploads/2023/08/ivv-t2104-ver-basic-07-28-2022.docx?emrc=6e4e35>
8. **Assurance Design** - Define the assurance design. Include Assurance Objectives, an outline of focus areas, and the approaches considered for performing technical tasks. Provide a summary of each IV&V activity to be performed. The content for this section may be in a separate document or embedded directly into this one. Identify the relevant document(s) and include a link to the location.
9. **Reference Documentation** - Identify titles, numbers, locations, and/or versions of documentation specified in the plan. Also, include any other relevant Project documentation.
10. **Acronyms** - In alphabetic order, define all abbreviations and acronyms used in the plan.
11. **Fiscal Year <XX> IV&V Summary** - Recommended.
    1. **FY <XX> Assurance Goals and Objectives** - Identify at a high level the assurance goals and objectives of the IV&V efforts for the applicable FY.
    2. **FY <XX> Targeted External Milestones** - List the key development project milestones. Depending on the development project, this may include milestones such as SRR, PDR, CDR, MRR, ORR, Launch Date, etc.
    3. **FY<XX> Internal Milestones** - List key internal milestones for the IV&V efforts. These will vary depending on the project, but may include mid-year risk assessment update, IV&V kickoff meeting, next year planning meeting with development Project, etc.
    4. **FY <XX> Schedule** - Provide a snapshot or summary of the IV&V Schedule for the applicable FY efforts.
    5. **FY <XX> Risks** - Provide a listing of perceived risks associated with the execution of the plan for the applicable year. This data only needs to be at the summary level as these risks will be managed via the IV&V Risk Review Board.
    6. **FY <XX> IV&V Technical Reports** - List specific technical reports planned for the fiscal year. These should be included in the FY <XX> Schedule. For relative dates, use working days unless there is a true requirement for calendar days to be used, e.g., a contractual or legal requirement.  Regardless, be specific as to the type of days intended.**

See the IV&V Project Execution Plan (IPEP) Template that’s available from the Templates section of the IV&V Management System (IMS) [411](#_tabs-<p></p>) site.  It’s available in Word and PDF formats.

See also [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan)

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-178 - IV&V Artifacts](/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts)        * [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) * [8.06 - IV&V Surveillance](/spaces/SWEHBVD/pages/102695713/8.06+-+IV+V+Surveillance) * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |

# 8. Objective Evidence

To demonstrate compliance with this requirement, objective evidence must clearly document the planning, implementation, and oversight processes related to the **IV&V Project Execution Plan (IPEP)**. The evidence should show that IV&V activities were formally integrated into the project lifecycle and that the IPEP was executed as per the defined standards. Below are examples of specific objective evidence that satisfy this requirement.

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

## 8.1 Development of the IPEP

The first stage of compliance involves the creation of the IPEP, specifying the scope, schedule, and details of IV&V activities. **Objective evidence** includes:

* **Draft and Final IPEPs:**
  + The initial draft of the IPEP reviewed and updated by the project and IV&V teams.
  + The approved IPEP, signed and dated by relevant stakeholders (e.g., project manager, IV&V lead, safety engineer).
* **Approval Records:**
  + Documented approval of the IPEP by project leadership, the IV&V Program, and other required authorities (e.g., risk management office).
  + Email exchanges, meeting minutes, or approval forms validating that necessary reviews and sign-offs occurred.
* **IPEP Templates:**
  + Ensure the IPEP is developed using NASA-approved templates for compliance with IV&V requirements in NASA-STD-8739.8 [278](#_tabs-<p></p>) .

## 8.2 Scope and Tailoring of IV&V Activities

The IPEP must outline the scope of IV&V work, particularly for small projects where tailoring is allowed. Objective evidence includes:

* **Scope Documentation:**
  + Description of the specific software components included in the IV&V effort (e.g., mission-critical or safety-critical systems).
  + Tailoring decisions: A document or section in the IPEP describing how and why the IV&V process has been scaled to match the project’s size, risk profile, and criticality.
* **Statement of Work (SOW):**
  + A formalized agreement detailing the specific IV&V activities to be performed (e.g., requirements analysis, code review, safety-critical software validation).
* **Risk Assessment Documentation:**
  + Evidence identifying and prioritizing risks that informed the scope of IV&V activities (e.g., IV&V focusing on high-risk areas).

## 8.3 Maintenance of the IPEP

The IPEP must be maintained and updated throughout the project lifecycle to adapt to changes in the software, risks, or project plans. Evidence includes:

* **Version History and Changes:**
  + Version-controlled IPEPs, demonstrating updates for evolving project requirements, risks, or milestones.
  + Change logs or configuration management records showing when and why changes were made to the IPEP.
* **Meeting Records:**
  + Records of periodic meetings (e.g., IV&V status meetings, software development reviews) where IPEP updates were discussed.
* **Risk Review Reports:**
  + Evidence that periodic reviews of software risks were conducted, including records justifying the addition, removal, or modification of IV&V activities in the IPEP.

## 8.4 Execution of the IPEP

The project manager must provide evidence that IV&V activities outlined in the IPEP were successfully executed. Objective evidence includes:

* **Activity and Progress Reports:**
  + IV&V progress reports summarizing completed versus planned tasks (e.g., requirements reviews, test case validations).
  + Documentation of milestone achievements, such as verification of all safety-critical requirements or completion of high-risk software reviews.
* **Test Artifacts:**
  + Records of specific IV&V activities, such as:
    - Requirements analysis reports: Validation of complete, clear, and testable requirements.
    - Design and code review reports: Results of IV&V reviews of software designs and source code.
    - Test validation reports: Documentation showing that IV&V reviewed and verified critical test cases or simulation performance.
* **Defect Logs:**
  + Logs of defects or issues identified during IV&V activities, including their severity, resolution status, and timelines.
* **Risk Assessments:**
  + Validation that IV&V completed safety or mission-critical risk assessments and provided feedback to the project team.
* **Test Coverage Evidence:**
  + Documents or matrices demonstrating that IV&V verified test coverage for mission-critical and/or safety-critical software requirements.

## 8.5 Communication and Coordination Evidence

The project manager must show that effective communication was maintained with the IV&V team to execute the IPEP. Evidence includes:

* **Status Update Records:**
  + Meeting minutes, emails, or reports summarizing joint discussions between the project team and the IV&V team regarding IPEP execution and progress.
  + Communication logs documenting issue resolution, clarifications, or changes to IV&V tasks.
* **Risk Reviews and Mitigation Status:**
  + Evidence of cross-team discussions and decision-making on significant risks or concerns raised by IV&V tasks.
* **Sign-off Records from IV&V Team:**
  + Approval or acknowledgment from the IV&V team that specific planned activities were completed as defined in the IPEP.

## 8.6 Final Review and Delivery Evidence

At the conclusion of the IV&V effort, evidence should confirm the successful delivery and acceptance of IV&V outcomes:

* **Final IV&V Report:**
  + A formal report summarizing findings, defects, risks, mitigation actions, and validated areas based on the IPEP.
  + Documentation showing that project-critical and safety-critical software passed IV&V scrutiny.
* **Lessons Learned:**
  + A summary or analysis of lessons learned related to the execution of the IPEP that could inform future IV&V planning and execution for similar projects.
* **Closure Approvals:**
  + Final project or NASA IV&V Program approvals verifying that all planned IPEP activities were completed successfully.

## 8.7 Compliance with NASA-STD-8739.8

The IPEP must demonstrate alignment with the IV&V requirements laid out in NASA-STD-8739.8. Evidence includes:

* **Standard Compliance Checklist:**
  + A checklist or document explicitly mapping IPEP contents and IV&V processes to the corresponding sections in NASA-STD-8739.8, ensuring full compliance.
* **Audit Reports:**
  + Results of any internal or external audits confirming the extent to which the IPEP and IV&V execution comply with NASA-STD-8739.8 and the project’s software assurance plan.

## 8.8 Summary of Objective Evidence Categories

| **Evidence Category** | **Examples of Artifacts** |
| --- | --- |
| IPEP Approval/Maintenance | Approved IPEP, version history, configuration change logs |
| IPEP Execution | IV&V reports, test coverage records, defect logs, risk assessments |
| Communication/Coordination | Meeting minutes, email exchanges, IV&V status updates, issue resolution records |
| Results and Deliverables | Final IV&V summary report, validated requirements/design/test plans, defect resolution confirmations |
| Compliance and Oversight | NASA-STD-8739.8 compliance checklist, IV&V audit results |

By preparing and maintaining these artifacts, project managers can ensure robust compliance with Requirement 3.6.3 while providing clear evidence of the value and effectiveness of IV&V activities. This approach not only ensures alignment with NASA standards but also reduces risks and enhances the likelihood of mission success.
