# SWE-013 - Software Plans

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695397. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans

SWE-013 - Software Plans

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695397)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695397&showCommentArea=true&showComments=true#addcomment)

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

3.1.3 The project manager shall develop, maintain, and execute software plans, including security plans, that cover the entire software life cycle and, as a minimum, address the requirements of this directive with approved tailoring.

## 1.1 Notes

The recommended practices and guidelines for the content of different types of software planning activities (whether stand-alone or condensed into one or more project level or software documents or electronic files) are defined in [NASA-HDBK-2203](http://swehb.nasa.gov/). The project should include, or reference in the software development plans, procedures for coordinating the software development and design, and the system or project development life cycle.

## 1.2 History

Click here to view the history of this requirement: SWE-013 History

SWE-013 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.1.1 The project shall develop software plan(s). |
| Difference between A and B | Expanded scope of SW Plans to  align to software lifecycle, compliance with NPR requirements, after approval and tailoring of the requirements. |
| B | 3.1.2 The project manager shall develop, maintain, and execute software plans that cover the entire software life cycle and, as a minimum, address the requirements of this directive with approved tailoring. |
| Difference between B and C | No change |
| C | 3.1.3 The project manager shall develop, maintain, and execute software plans that cover the entire software life cycle and, as a minimum, address the requirements of this directive with approved tailoring. |
| Difference between C and D | Added security plans to what needed to be included |
| D | 3.1.3 The project manager shall develop, maintain, and execute software plans, including security plans, that cover the entire software life cycle and, as a minimum, address the requirements of this directive with approved tailoring. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

Because software development is a complex technical process that requires a lot of steps, having a project plan is extremely helpful to visualize and follow each step of its development, according to a timeline for the team's work.

This requirement ensures that software plans covering the entire life cycle—including security considerations—are developed, maintained, and executed to provide structure, compliance, and risk management across all phases of the software development process. By addressing the mandates of the directive with approved tailoring, the project manager ensures accountability, long-term sustainability, security, regulatory compliance, and mission success. In high-stakes environments like aerospace, such planning is essential to proactively manage the complexities of mission-critical software development.

This requirement ensures that aerospace software development, deployment, and maintenance follow a structured, comprehensive, and secure approach aligned with the organization’s mandates and mission-critical objectives. The presence of robust software plans—covering the full software life cycle—mitigates risks, ensures compliance, and promotes predictability and success throughout all phases of a project. Below is the rationale for this requirement broken down into key focus areas:

## 2.1 Ensuring a Systematic and Predictable Development Process

* **Why It Matters**:
  + Software development in aerospace involves multiple stages, each with distinct challenges and dependencies. Without clearly defined plans, the development process could become fragmented, inefficient, or disorganized.
  + Software plans provide a framework for managing requirements, resources, testing, and delivery milestones to ensure the project remains on schedule and aligned with mission goals.
* **Rationale**:
  + Developing and maintaining comprehensive plans ensures that each phase of the software life cycle is systematically addressed, resulting in higher predictability, reduced errors, improved resource allocation, and better alignment with project deadlines.

## 2.2 Addressing the Full Software Life Cycle

* **Why It Matters**:
  + Aerospace software systems must be managed across their entire life cycle—from conceptual design, development, and testing to deployment, operation, and eventual retirement. Plans must account for:
    - Early-phase needs: Requirements gathering, risk analysis, and strategic design.
    - Mid-phase needs: Implementation, testing, integration, and verification & validation.
    - Late-phase needs: Maintenance, updates, monitoring for defects, addressing cybersecurity threats, and safe retirement or replacement.
  + Failure to plan for later phases (e.g., post-deployment maintenance or end-of-life disposal) can lead to obsolescence risks, security vulnerabilities, and reduced system reliability.
* **Rationale**:
  + Comprehensive life cycle planning ensures that risks, resources, and responsibilities are addressed across all phases, enabling long-term sustainability, security, and operational readiness.

## 2.3 Enhancing Security in Every Life Cycle Phase

* **Why It Matters**:
  + Aerospace systems are high-value targets for cybersecurity threats, including attacks aimed at disrupting communications, stealing data, sabotaging missions, or endangering lives.
  + A dedicated and detailed software security plan integrated into the overall life cycle plan ensures that security measures are not overlooked but rather prioritized throughout:
    - Architecture design: Integrating secure design practices early.
    - Development: Incorporating secure coding practices and vulnerability monitoring.
    - Testing: Assessing system performance under potential attack vectors.
    - Operation and maintenance: Monitoring for emerging cyber threats and regularly updating software to remain secure.
* **Rationale**:
  + By mandating a security plan, this requirement ensures that cybersecurity risks are systematically analyzed and mitigated across the software life cycle, making the system resilient against evolving threats. Operating without such plans risks exposing the system to breaches that could endanger missions, hardware, or personnel.

## 2.4 Guaranteeing Compliance with Regulatory and Mission-Specific Requirements

* **Why It Matters**:
  + Aerospace software is subject to strict regulatory requirements, such as NASA NPR 7150.2D, DO-178C, and other standards for safety, security, functionality, and quality in mission-critical software. These guidelines require detailed management plans for:
    - Software engineering processes (e.g., requirements, design, development).
    - Configuration and quality control.
    - Verification, validation, and hazard management.
    - System security.
    - Documented tailoring (if deviations from standard directives are necessary).
  + Approved tailoring allows the project to adapt mandates to its specific needs while remaining compliant with core objectives.
* **Rationale**:
  + Developing plans aligned with regulatory requirements ensures compliance, which is critical for obtaining certifications, passing audits, and avoiding delays. Tailoring provides flexibility to meet project-specific needs without compromising standards.

## 2.5 Promoting Risk Management and Hazard Mitigation

* **Why It Matters**:
  + Aerospace software systems involve significant risks—such as software defects, operational failures, security breaches, and compatibility issues—that could jeopardize missions, equipment, or lives.
  + Software plans serve as a proactive risk management tool, ensuring that:
    - Risks are identified, analyzed, and addressed early.
    - Contingency plans are in place for identified hazards.
    - Testing, validation, and redundancy requirements are detailed and traceable to reduce risk.
* **Rationale**:
  + Comprehensive, well-maintained plans reduce uncertainties by providing structured processes for mitigating software-related risks, particularly those threatening safety and mission-critical functions. The absence of such plans could lead to reactive, ad-hoc risk management, which is far less reliable.

## 2.6 Ensuring Accountability and Clear Roles

* **Why It Matters**:
  + Aerospace software development often requires collaboration between multiple teams, departments, and contractors. Without detailed plans:
    - Roles and responsibilities could become unclear.
    - Accountability for execution (e.g., design testing or security monitoring) might fall through the cracks.
    - Disputes about scope, deliverables, or timelines can arise.
* **Rationale**:
  + Well-documented software plans ensure clarity around responsibilities, creating accountability for key deliverables at every stage. This formal structure also reduces ambiguity that could delay progress or lead to inefficiencies.

## 2.7 Improving Coordination Between Parallel Efforts

* **Why It Matters**:
  + Aerospace systems are highly integrated; software must interface seamlessly with hardware, other software modules, and ground or orbital systems. These efforts often proceed in parallel, and poor coordination leads to inefficiencies, rework, or integration failures during later stages.
* **Rationale**:
  + Software plans outline processes for synchronizing efforts, ensuring consistent communication between developers, hardware engineers, cybersecurity teams, and mission stakeholders. The result is a cohesive, integrated system with minimal last-minute fixes or compatibility issues.

## 2.8 Facilitating Maintenance and Continuous Improvement

* **Why It Matters**:
  + After deployment, software must be regularly monitored, maintained, and updated to address evolving needs, emerging cybersecurity threats, or potential defects. Failure to plan for this phase could leave the system unsupported, outdated, or vulnerable.
* **Rationale**:
  + Including maintenance and improvement in the life cycle plan ensures the software remains reliable, secure, and adaptable for the duration of its use, extending the return on development costs.

## 2.9 Supporting Auditability and Documentation

* **Why It Matters**:
  + Aerospace projects are highly scrutinized, requiring detailed audits to ensure compliance with regulations, safety protocols, and mission objectives. These audits require comprehensive documentation of strategies, processes, and changes made throughout the software life cycle.
* **Rationale**:
  + Software plans act as a living document that records the development and management of the project, providing evidence for certification or regulatory audits and ensuring traceability for every decision and process.

## 2.10 Tailoring to Mission-Specific Objectives

* **Why It Matters**:
  + Not all software projects are the same. Missions vary in size, complexity, safety-criticality, and resource availability. Tailoring software plans lets project managers adapt approved methodologies and processes to meet these unique needs while still adhering to the overarching requirements of the directive.
* **Rationale**:
  + Tailored plans provide the necessary flexibility without compromising safety, security, or compliance, resulting in a development process optimized for the project’s specific goals.

# 3. Guidance

Software plans describe the activities and processes that will be carried out and the products that will be produced to fulfill project requirements for the software. These plans are created to guide the work and increase the expectations of meeting project objectives and goals. To fulfill this purpose, the plans need to be followed and kept up-to-date as project requirements change. The Software Development Plan (SDP) describes a developer’s plans for conducting a software development effort. The SDP provides the acquirer insight and a tool for monitoring the processes to be followed for software development. It also details the methods to be used and the approach to be followed for each activity, organization, and resource.

As with any activity that involves multiple tasks and functions, software development requires thought before implementation.  The team documents and reviews those thoughts and plans before implementation to allow for consideration of all the tasks, methods, environments, tools, and related criteria needed to complete the work.  Planning helps the team efficiently produce what is needed and expected as well as provides a means for communications and partnering with customers and stakeholders on the implementation of the project.  Planning also allows a current project to improve based on lessons learned from previous projects, including using more appropriate or efficient techniques and avoiding previously experienced difficulties. See also Topic [7.05 - Work Breakdown Structures That Include Software](/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software).

Having plans also allows the team to review, improve, and verify software activities before implementation to ensure the outcome will meet the expectations and goals of the project.  Planning also helps to ensure the project is cost-efficient and timely.

Software plans are to be complete, correct, workable, consistent, and verifiable.

## 3.1 Plan Contents

Software plans include, but are not limited to:

1. Software development or management plan.
2. Software configuration management plan.
3. Software test plans.
4. Software maintenance plans.
5. Software assurance plans.
6. The software safety plan, if the project has safety-critical software.

When developing software plans for a project, consider using templates for the content of each required plan to ensure consistent content and application across projects.  Keep in mind that tailoring may be necessary for a particular project, especially given different safety and software classifications that may apply. See also Topic [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)

Plans should specify the standards and procedures for management, acquisition, engineering, and assurance activities.    This includes documenting the work products, tasks, resources, commitments, schedules, and risks for the project, as well as describing strategies for development or acquisition, data management, risk management, stakeholder management, and measurement and analysis.  See Topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) for recommended plans and content which support the activities that are required by NPR 7150.2.  Topic [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) also includes the recommended content for the [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) as well as additional references that may be used when developing each specific plan.

[7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) guides the maturity of several project plans at various life cycle reviews.

## 3.2 Plan Maintenance and Implementation

Once software plans have been baselined, consider the following guidelines for maintaining and implementing them.

While the Project Manager is responsible for executing the project plan, a software or development team lead may ensure the execution and maintenance of software plans.

Baseline plans before they are implemented to ensure that only approved plans are executed by the project team. For Space Flight Projects the expected maturity (draft, preliminary, baselined, updated, and final) of plans at the various milestone reviews are provided in this Handbook's Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) matrix. Once software plans are approved and baselined, projects are expected to follow these plans. To ensure plans are followed, projects typically implement project monitoring and control (see [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking)) and software assurance processes. Per NASA-STD-8739.8, Software Assurance and Software Safety Standard[278](#_tabs-<p></p>) software assurance and software safety are to be performed to assure that life cycle processes adhere to applicable project plans and that management, engineering, and assurance processes are audited for compliance with applicable plans.

Requirements and processes typically change as the project progresses and new information is obtained, issues are found, or planned solutions are found to be unsuitable. When this happens, the baselined plans need to be updated to reflect the new information, new processes, new solutions, or other project changes. In other words, plans need to be maintained such that they are current with project activities, decisions, and other factors that affect the processes described in those plans.

Possible reasons for updating software plans include, but are not limited to:

* In response to the results of progress or status reviews.
* Changes in resource levels, and availability (e.g., tools, facilities, personnel).
* Planned solutions are found to be unsuitable.
* Estimates are found to be inaccurate (e.g., cost, product size, effort).
* Changes in project scope.
* Requirements changes.
* Changes in timelines/schedules, especially for coordinated or linked activities.
* Missed milestones.
* In response to corrective actions.
* In response to new or revised risks.
* Budget changes.
* Regulatory changes.
* Changes in stakeholder commitments.

**CMMI for Development, Version 1.3: Improving processes for developing better products and services**

"Criteria are established for determining what constitutes a significant deviation from the project plan. A basis for gauging issues and problems is necessary to determine when corrective action should be taken. Corrective actions can lead to re-planning, which may include revising the original plan, establishing new agreements, or including mitigation activities in the current plan. The project plan defines when (e.g., under what circumstances, with what frequency) the criteria will be applied and by whom."[157](#_tabs-<p></p>)

When one of these situations occurs, its impact on the completion of project objectives is evaluated to determine if changes to software plans are required.

## 3.3 Reviews and Approval

Revised plans need to be reviewed and approved before they are implemented. Plans and progress against those plans are typically reviewed at life cycle milestone reviews, but approval of revisions need not wait for a scheduled review. Those reviews occur promptly to ensure continued progress toward project objectives and goals. Approved, revised software plans are distributed to affected stakeholders, such as the software development team, so they follow the most up-to-date plans. Periodic audits may be used to confirm team adherence to software plans.

See also Topic [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing).

Consult Center Process Asset Libraries (PALs) for Center-specific guidance and resources related to software plans, including responsibilities for producing software plans.

## 3.4 Software Assurance Plans

Software assurance plans should be based on the software assurance tasking identified in the Software Assurance Tasking Checklist Tool. See [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool)

The purpose of the Software Assurance (SA) Tasking Checklist Tool is to streamline the Software Assurance and Software Safety Tasks (a.k.a. SA Tasking) that must be performed on a NASA project. The tool allows the user to tailor the SA Tasking based on the needs of the project via Software Classification, Safety Criticality, and required Milestones.

The SA Tasking Checklist Tool assists in the planning, execution, and monitoring of the Software Assurance (SA) tasks provided in NASA-STD-8739.8A Requirement SASS-01, mapped to the NPR-7150.2C Software Engineering Requirements. The tool is designed with a user-friendly front end which integrates the engineering, software assurance, and safety requirements across the development life cycle to create SA tasking checklists based on milestones to plan and ensure compliance. While the default project information addresses a “typical” development project with full compliance to SASS-01, the tool is flexible in terms of tailoring the requirements, as well as providing the ability to map the SWE requirements to various milestones for different development life cycles to address Center or project-specific attributes. The tool may also be used to capture status when SA activities are performed throughout the development life cycle. The resulting checklist of SA Tasking may be filtered. Monitoring of the resulting SA Tasking may be performed using the generated checklist in the tool. Another option for monitoring is to export the checklist(s) in common formats compatible with other tools including Excel, JIRA, and MS Project (i.e., Excel, CSV, and XML).

The SA Tasking Checklist Tool has a comprehensive Users Guide embedded in the tool to assist the user with tool features and functionality. It also provides instruction on how to use the tool to generate a project-specific SA Tasking Checklist.

See tab 7 for additional SA Tasking and guidance.

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.17 - Software Assurance Plan Minimum Content](/spaces/SWEHBVD/pages/138707548/5.17+-+Software+Assurance+Plan+Minimum+Content) * [5.18 - Safety Plan Minimum Content](/spaces/SWEHBVD/pages/138707600/5.18+-+Safety+Plan+Minimum+Content) * [7.05 - Work Breakdown Structures That Include Software](/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool) * [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

# 4. Small Projects

For small projects, adhering to this requirement can be a challenging task due to limited resources, time, and scale. However, adopting a streamlined and pragmatic approach ensures compliance with the directive while maintaining focus and efficiency.

By tailoring processes, consolidating plans, and embedding security pragmatically, small projects can effectively meet this requirement without overwhelming the team, ensuring optimal use of available resources while maintaining compliance and quality.

Here's good guidance for small projects to satisfy this requirement effectively:

## 4.1. Understand and Tailor the Requirement

* Key Objective: Ensure that the software plans align with the project's size, complexity, and criticality while addressing all life cycle phases and the minimum requirements of the directive.
* Steps:
  1. Understand Mandatory Requirements: Analyze the directive (and its tailoring guide, if available) to identify non-negotiable requirements for your project (e.g., security, testing, assurance).
  2. Tailor the Plans for Small Projects:
     + Determine what is essential based on the scale, scope, and criticality of the software (e.g., low-risk or non-mission-critical projects may need simpler plans).
     + Tailoring should focus on reducing unnecessary effort while maintaining compliance with requirements.
     + Document the justification/rationale for tailored sections and obtain approval from stakeholders or compliance authorities.
  3. Define the level of detail in each plan to reflect the project size while avoiding excessive overhead.

## 4.2. Identify Required Software Plans

At a minimum, small projects will require core plans to cover the software life cycle, with an emphasis on security. Typical plans include:

### A. Software Development or Management Plan (SDP/SMP)

* Purpose: Outline the overall strategy and processes to develop, deliver, and maintain software.
* Key Components:
  + Software life cycle description (e.g., waterfall, agile, hybrid model).
  + Roles and responsibilities.
  + Resource allocation (people, tools, budget).
  + Tailored milestones and deliverables for each phase.

### B. Software Assurance Plan (SAP)

* Purpose: Define how verification, validation, quality, and broader assurance objectives will be achieved.
* Key Components:
  + Testing strategy.
  + Risk management and issue resolution.
  + Configuration management process.

### C. Software Configuration Management Plan (SCMP)

* Purpose: Establish control over versioning, baselines, changes, and documentation.
* Key Components:
  + How software changes will be tracked and approved.
  + Tools used (e.g., Git, Subversion, Jira).
  + Procedures for managing baselines and build processes.

### D. Software Security Plan (SSP)

* Purpose: Define how security will be embedded across the life cycle.
* Key Components:
  + Risk assessment of anticipated threats and vulnerabilities.
  + Secure coding practices.
  + Processes for vulnerability testing, data protection, and incident response.

### E. Maintenance and Operations Plan

* Purpose: Cover long-term maintenance and operational use of the software.
* Key Components:
  + Bug fixing and patching processes.
  + Who will provide technical support.
  + Procedures for software retirement or transfer.

Tip

For small projects, you can combine these plans into a single document for simplicity, provided all elements (e.g., assurance, security) are sufficiently addressed.

## 4.3. Develop Lightweight and Modular Plans

For small projects, the plans should be simple, concise, and modular. Over-documenting or creating overly detailed plans can cause unnecessary delays and complexity.

**Tips for Developing Plans for Small Projects**:

1. Use Templates:
   * Leverage existing organizational templates or adopt simplified templates for each plan.
   * Include tailored sections to align with the size and nature of the project.
2. Focus on Core Life Cycle Phases:
   * Address only the major life cycle phases your project needs—e.g., requirements, design, development, testing, and deployment.
3. Keep It to the Point:
   * Focus on what is strictly necessary to meet the directive. For small projects, a plan that is overly complex can slow down the team.
4. Combine and Consolidate:
   * Consider combining related plans into a single document (e.g., integrate security planning into the overall software development management plan).
   * This is particularly useful when team resources are limited.

**Example**: An integrated software plan for a small project could have sections such as: Project Overview, Development Approach, Assurance Activities, Configuration Management, and Security.

## 4.4. Maintain and Execute Plans Dynamically

Software plans aren’t static—they need regular monitoring and updates throughout the software life cycle.

**When Maintaining Plans**:

1. Perform Periodic Reviews:
   * Schedule brief (but regular) Plan-Review-Update cycles aligned with the project’s milestones.
   * Update the plans to reflect changing requirements, discovered risks, or testing results.
2. Keep Stakeholder Engagement:
   * Involve key stakeholders (project owner, team leads, quality assurance) when modifying plans. For security plans, engage security experts or system administrators.
3. Accessibility:
   * Store plans in a version-controlled repository (e.g., SharePoint, GitHub, or Confluence) that the team can easily reference and access.

**During Execution**:

1. Align Execution with Deliverables:
   * Tie actionable items in the plans to project deliverables or milestones.
     + Example: Security and testing plans should specify processes and deliverables (e.g., results of penetration testing during the testing phase).
2. Leverage Automation:
   * For repetitive assurance activities (e.g., testing, deployment configurations), small projects can benefit from lightweight automation tools (e.g., Jenkins for CI/CD pipelines).
3. Track Progress Sustainably:
   * Use simple tools (like Kanban boards, Trello, or Jira) to track the execution status of activities like testing, assurance, or risk analysis.

## 4.5. Ensure Security is Embedded

Security planning must be a top priority, even for small projects, and it should be baked into each phase of the software life cycle. Here’s how to integrate security effectively:

**In Early Phases**

* Secure Requirements and Design:
  + Conduct a quick, high-level threat model to identify high-risk areas and vulnerabilities.
  + Ensure security-related requirements (e.g., data encryption, access controls) are captured.

**In Development**

* Embed Secure Coding Standards:
  + Mandate the use of secure development practices (e.g., coding checklists like OWASP secure coding practices).
  + Use automated tools for static analysis and code reviews to catch security flaws early.

**In Testing and Integration**

* Perform Security-Specific Testing:
  + Include vulnerability scans, penetration tests, or fuzz testing as part of verification and validation.
* Iterative Testing for Updates:
  + For small projects, ensure that even minor changes are reviewed from a security perspective.

**In Deployment and Maintenance**

* Monitor Ongoing Security:
  + Plan for monitoring and patching systems for new vulnerabilities.
  + Implement routine security audits if the project extends into long-term use.

Tip

Document security assurance processes directly in your software security plan (or combined plan) for full coverage across the life cycle.

## 4.6. Approved Tailoring

For small projects, tailoring the plans to fit the scope of the directive is critical. Tailored plans should:

1. **Document the Tailoring Authority**:
   * Identify the authority responsible for approving plan tailoring (e.g., quality assurance or project sponsor).
2. **Specify What Was Tailored Out**:
   * Clearly document what requirements/activities were removed, substituted, or scaled down (e.g., opting for a single integrated plan instead of multiple detailed plans).
3. **Provide Rationale**:
   * Include justifications for tailoring decisions and emphasize how risks are still addressed effectively.

**Example**:

* Tailoring Justification: "Due to the small scale of the project and its low risk profile, the standalone software assurance plan has been integrated into the primary software management plan. Key assurance activities, such as peer reviews, will still be conducted as part of the regular project workflow."

## 4.7 Monitor Compliance

Ensure that all plans, tailored or otherwise, are reviewed and approved by appropriate stakeholders before implementation. For small projects, this may include:

* Project Manager
* Software Assurance Lead
* Risk or Security Officer
* Relevant Stakeholders or Review Boards

### Example Workflow for Small Projects

1. **Planning Phase**:

   * Develop a single integrated plan covering core life cycle areas and security assurance.
   * Conduct threat modeling for security risks.
   * Schedule plan reviews at key milestones.
2. **Execution Phase**:

   * Follow lightweight processes outlined in the plan.
   * Track adherence to assurance and security activities (e.g., using checklists or dashboards).
3. **Maintenance Phase**:

   * Update plans to reflect lessons learned or minor changes.
   * Finalize documentation for post-project handoff or archival.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Developing comprehensive software plans that span the entire software life cycle is critical to ensuring mission success. NASA's lessons learned on this topic highlight best practices, challenges encountered, and strategies to mitigate risks based on past missions, projects, and incidents.

---

### **Key NASA Lessons Learned for Software Life Cycle and Planning**

#### **1. Deficiencies in Life Cycle Planning Can Lead to Mission Failures**

**Incident:**  
On past missions (e.g., Mars Climate Orbiter, Genesis), insufficient planning for software design, testing, and maintenance resulted in catastrophic failures. For example:

* The **Mars Climate Orbiter (1999)** failed due to a mismatch in unit systems between software components that was not identified due to gaps in requirements verification planning.
* The **Genesis Mission (2004)** encountered a software planning flaw where the orientation sensors were improperly configured due to oversight in integration and testing planning.

**Lesson Learned:**

* **Comprehensive Planning:** The software development plan must address all phases of the software life cycle—from requirements definition to decommissioning—and anticipate risks related to integration, testing, and validation.
* **Regular Updates:** Plans must be updated as the system evolves through the life cycle, incorporating lessons learned from each phase.

**Implication:**  
Software plans must be detailed, regularly reviewed, and flexible enough to adapt to changes while maintaining full traceability to the directive's requirements.

---

#### **2. Importance of Security Planning in Software Life Cycle**

**Incident:**  
Cybersecurity vulnerabilities in NASA software systems have occasionally exposed sensitive mission data and jeopardized operational safety. For example:

* **NASA's cyber-attack incidents:** Undervalued software security planning and testing during development phases left systems susceptible. Adversarial simulations revealed critical flaws that could compromise mission integrity.

**Lesson Learned:**

* **Integrated Security Plans:** Security planning must be embedded as part of the software life cycle plan. Security plans should account for:
  + Threat modeling during design.
  + Regular vulnerability assessments during development and maintenance.
  + Realistic cyber-resilience testing scenarios.
* **Early Involvement of Security Teams:** Involve security personnel early to ensure security requirements are prioritized and integrated into software development processes.

**Implication:**  
Ensure the software plans include detailed sections for cybersecurity management and testing throughout the life cycle.

---

#### **3. Executive Oversight and Stakeholder Alignment**

**Incident:**  
On several missions, inadequate alignment between project management and software stakeholders led to failures and inefficiencies. For instance:

* The **James Webb Space Telescope (JWST) Development Delays** were partially attributed to misalignment between software planning and system engineering schedules, causing budget overruns and timeline delays.

**Lesson Learned:**

* **Collaborative Software Plans:** Software plans must align with system engineering plans, project schedules, and budget constraints to avoid integration and resource planning conflicts.
* **Stakeholder Buy-In:** Engage all relevant stakeholders from the beginning (project managers, system engineers, security teams, end-users) to ensure the software plan reflects mission goals and constraints.

**Implication:**  
Project managers must maintain stakeholder engagement throughout the planning process and establish mechanisms for frequent plan reviews and updates.

---

#### **4. Incomplete Testing Plans Lead to High Cost Defects**

**Incident:**  
The **Space Shuttle Program** encountered significant issues due to software defects that were not covered in test plans, requiring rework and cost escalation. For example:

* Early versions of the Space Shuttle flight software contained code errors that delayed mission-critical preparations. Gaps in testing phases were identified as a root cause.

**Lesson Learned:**

* **Comprehensive Test Coverage:** Software plans must thoroughly address testing requirements, ensuring:
  + Full coverage of all safety-critical paths and scenarios.
  + Testing in realistic mission environments (e.g., simulations for nominal and off-nominal conditions).
* **Embedded Verification and Validation (V&V):** Include independent V&V in the software plan to identify gaps in requirement implementation and test coverage early.

**Implication:**  
Ensure that testing strategies and V&V are explicitly defined within the software plan, tailored to mission-specific risks and goals.

---

#### **5. Tailoring of Software Plans**

**Incident:**  
Tailoring plans to meet specific mission requirements is critical for success, as demonstrated by missions like **Parker Solar Probe (2018)** which required unique software planning for high-temperature and close proximity operations near the Sun.

**Lesson Learned:**

* **Approved Tailoring:** While tailoring is necessary, it must meet the essential requirements of NASA directives and be documented in approval records.
* **Risk Management Through Tailoring:** Tailoring must be justified based on risk-benefit analyses and include fallback provisions in case tailored decisions introduce new risks.

**Implication:**  
Approved tailoring must be explicitly documented in the software plan, along with justifications and measures to mitigate any associated risks.

---

#### **6. Documentation Gaps in Software Life Cycle**

**Incident:**  
In cases such as **Mars Science Laboratory Curiosity Rover (2012)**, undocumented software changes during integration phases resulted in confusion and delays during testing.

**Lesson Learned:**

* **Detailed Documentation:** Software plans must include regular updates to documentation, covering:
  + Changes made during each life cycle stage.
  + Version control practices.
  + Configuration management processes.
* **Knowledge Transfer:** Plans must accommodate knowledge transfer between teams to ensure continuity through the software life cycle.

**Implication:**  
Document all software development, integration, testing, and maintenance activities comprehensively and maintain version-controlled repositories for plan artifacts.

---

#### **7. Agile Practices and Iterative Planning**

**Incident:**  
The transition to Agile development methodologies in projects such as **NASA’s Open Mission Control Technologies (Open MCT)** showed significant benefits in software adaptability but revealed challenges in maintaining consistent planning across iterations.

**Lesson Learned:**

* **Adaptive Plans:** In fast-paced iterative development environments, software plans must reflect current priorities and synchronize with incremental development milestones.
* **Phase-Specific Controls:** Divide life cycle planning into manageable phases, with checkpoints to review and refine plans.

**Implication:**  
Implement iterative planning methods in software plans while maintaining alignment with the directive’s requirements.

---

#### **8. Lessons from Software Risk Management**

**Incident:**  
In missions like **ICESat-2 (2018)**, unplanned risks arose from software defects detected late in development stages. These risks escalated project costs and reduced schedule flexibility.

**Lesson Learned:**

* **Proactive Risk Management:** Ensure risk management strategies are embedded in the software plan:
  + Identify top software risks early during development.
  + Allocate resources for mitigating risks through redundancy, fault tolerance, and rigorous testing.

**Implication:**  
Enhance the software plan to include risk monitoring and mitigation activities throughout all life cycle stages.

---

### 9. **Lesson Learned (Starliner CFT):** **Misaligned roles, fragmented authorities, and weak communication paths delay technical decisions and erode confidence.**

**Project Context:**  
Derived from the **Starliner Crew Flight Test (CFT) Investigation**.

**Problem/Observation:**  
Organizational integration was fragmented; accountability and insight expectations varied across NASA, provider, and subcontractors. Decision‑making was slowed, with inconsistent ownership for anomaly resolution.

**Contributing Factors:**

* Divergent interpretations of shared accountability and insight across organizations.
* Lack of structured, recurring technical forums with clear decision authority.
* Ambiguous interface responsibilities between NASA, prime contractor, and key subsystems.

**Impacts:**

* Delayed anomaly disposition, prolonged uncertainty, and reduced trust.
* Incomplete communication led to gaps in verification coverage and missed system interactions.

**Recommended Practices (Aligned to SWE‑013/014):**

* Establish a **clear RACI** (Responsible, Accountable, Consulted, Informed) covering software, avionics, propulsion interfaces, and anomaly resolution paths.
* Create **recurring cross‑functional technical boards** (software, systems, safety) with documented outcomes and clear authority.
* Define **communication cadences** (frequency, artifacts, participants) for anomaly tracking, data review, and risk decisions.

**Actionable Checks:**

* Charter and roster for decision boards exist and are current.
* RACI and interface control documentation are reviewed during major milestones.
* Meeting minutes capture decisions, dissenting opinions, and follow‑ups.

### 10. **Late and Incomplete Flight Software (FSW) Delivery**

**Incident:**  
The Psyche mission experienced an eight‑month late delivery of the final GNC flight software build, with hundreds of control parameters and fault protection behaviors still undefined. This delay, combined with numerous unresolved software issues, contributed directly to the missed 2022 launch opportunity.

**Lesson Learned:**

* **Early Software Definition & Maturity:** Mission‑critical software requirements, parameters, and behaviors must be fully defined and matured early to prevent cascading delays.
* **Rigorous Defect Disposition:** “Use‑as‑is” and unverified failure dispositions must undergo strict technical review to prevent acceptance of excessive residual risk.

**Implication:**  
Delays and ambiguity in software maturity directly threaten launch schedules, increasing cost, workforce strain, and mission‑risk exposure.

### 11. **Poor Metrics and Lack of Visibility into Software Health**

**Incident:**  
Psyche’s project metrics masked true software progress. Software risk was consistently under‑reported due to an aversion to categorizing issues as “red,” preventing leadership from recognizing schedule‑threatening problems.

**Lesson Learned:**

* **Objective Software Metrics:** Software maturity must be tracked using measurable indicators such as defect trends, verification progress, and test coverage.
* **Risk Transparency:** Leadership must encourage open reporting and avoid cultural pressures that suppress accurate risk assessments.

**Implication:**  
When metrics fail to reflect reality, management loses the ability to make timely decisions, creating preventable launch‑critical failures.

### **12. Additional NASA lessons**

**LLSW03 — Define Artifact Access vs. Delivery Expectations**

* **Context/Background:** It took ~6 months to obtain limited artifact “access,” insufficient for tool‑based analysis; effectiveness dropped sharply.
* **Lesson Learned:** Contracts must explicitly define **access** (portal read) vs. **delivery** (files for tooling), with rationale and intended use (traceability, FDIR analysis).
* **Evidence/Observation:** Tool‑driven analysis needs full artifacts to compute relationships across thousands of requirements; delays impede phase‑aligned feedback.
* **Cause(s):** Ambiguous contractual language; unclear IV&V needs.
* **Recommendation/Corrective Action:** Specify artifact delivery cadence, formats, and completeness (requirements snapshots, designs, code, tests) and repository permissions.
* **Implementation Guidance:** Tie to **SWE050** (requirements captured/maintained), **SWE052/072** (traceability), **SWE131/141** (IV&V planning/execution).
* **Success Criteria/Verification:** IV&V receives complete, tool‑readable baselines at defined intervals; measurable reduction in analysis latency.
* **Applicability/Scope:** All mission/safety‑critical developments.
* **Related Standards/Requirements:** SWE013, SWE050, SWE052, SWE072, SWE131, SWE141.

**LLSW04 — Provide Direct Read‑Only Access to Code Repositories**

* **Context/Background:** Teams granting IV&V read‑only repo access enabled near‑realtime analysis and reduced packaging delays.
* **Lesson Learned:** Use industry standard practice: **IV&V read‑only repo access** (e.g., GitLab) to current versions for in‑phase feedback and improved coverage.
* **Evidence/Observation:** Latency dropped from 6+ months to near realtime for VSM/CSM/MSM teams.
* **Cause(s):** Reliance on manual deliveries; limited visibility.
* **Recommendation/Corrective Action:** Require repo access in contracts; secure role‑based credentials; define branching/tagging schemes.
* **Implementation Guidance:** Align with **SWE131/141**; trace requirements to code (**SWE064/052**); ensure build artifacts support test traceability (**SWE072**).
* **Success Criteria/Verification:** IV&V confirms clean builds; timely defect reports aligned with sprints; reduced false positives.
* **Applicability/Scope:** All projects using SCM.
* **Related Standards/Requirements:** SWE064, SWE072, SWE131, SWE141.

**LLSW06 — Provide Design Artifacts Early and In‑Phase with Development**

* **Context/Background:** Early design visibility enables cheaper, timely feedback; late delivery limits IV&V value.
* **Lesson Learned:** Share evolving designs **before coding**; IV&V supports iterative updates and identifies issues when change costs are lowest.
* **Evidence/Observation:** Difficulties obtaining early design artifacts reduced synchronization and defect prevention.
* **Cause(s):** Perception that IV&V slows design.
* **Recommendation/Corrective Action:** Include design artifact delivery milestones in IV&V PEP; allow early access to drafts.
* **Implementation Guidance:** **SWE013** (planning), **SWE018** (reviews), **SWE131/141** (IV&V).
* **Success Criteria/Verification:** Reduced design‑phase rework; fewer late defects; on‑time IV&V reviews.
* **Applicability/Scope:** All mission/safety‑critical designs.
* **Related Standards/Requirements:** SWE013, SWE018, SWE131, SWE141.

**LLSW08 — Include Subcontractor Documentation in Deliveries**

* **Context/Background:** Prime docs lacked detail for subcontractor functionality; IV&V couldn’t assess low‑level designs.
* **Lesson Learned:** Require subcontractor **low‑level design/documentation** availability to IV&V (as legally permissible).
* **Evidence/Observation:** More complete documentation reduced false positives and improved issue identification.
* **Cause(s):** Undefined contractual expectations for lower‑tier artifacts.
* **Recommendation/Corrective Action:** Include flow‑downs mandating artifact delivery/access rights; define content/format.
* **Implementation Guidance:** Plans (**SWE013**), requirements (**SWE050**), and IV&V (**SWE131/141**) should specify subcontractor documentation scope.
* **Success Criteria/Verification:** IV&V can compile/build/analyze with full design context; decreased unactionable findings.
* **Applicability/Scope:** Multi‑tier development efforts.
* **Related Standards/Requirements:** SWE013, SWE050, SWE131, SWE141.

**LLSW10 — Early and Continuous IV&V Integration**

* **Context/Background:** IV&V entered post‑CDR; early defects were missed; rework and schedule churn increased.
* **Lesson Learned:** Integrate IV&V **from formulation** through test; deliver artifacts continuously to enable in‑phase analyses.
* **Evidence/Observation:** Early IV&V identifies requirements/design risks when changes are cheapest.
* **Cause(s):** Perception IV&V slows development; absent IV&V provisions in contracts.
* **Recommendation/Corrective Action:** Include IV&V requirements in acquisition; define PEP milestones; align sprint cadences.
* **Implementation Guidance:** **SWE131/141**, **SWE013**, **SWE018**.
* **Success Criteria/Verification:** Consistent, timely IV&V findings; reduced late rework; improved test readiness.
* **Applicability/Scope:** All mission/safety‑critical software.
* **Related Standards/Requirements:** SWE131, SWE141, SWE013, SWE018.

**LLSW15 — Early Safety Applicability to “Uncrewed” Systems that Interface with Crew**

* **Context/Background:** PPE initially excluded from human‑rating; later interfaces demanded safety compliance, causing costly remedies.
* **Lesson Learned:** Apply **safety requirements early** to any system that **interfaces** with crewed systems.
* **Evidence/Observation:** Delays/confusion in HR scope; expensive fixes to improve.
* **Cause(s):** Procurement/requirements processes lacked SMA inputs.
* **Recommendation/Corrective Action:** Engage SMA in procurement; include safety clauses in contracts; classify software appropriately (SWE020/160/133).
* **Implementation Guidance:** **SWE020**, **SWE133/134**, **SWE013**.
* **Success Criteria/Verification:** No late adds of safety requirements; HR scope correct at start; reduced variance requests.
* **Applicability/Scope:** All interfacing systems, crew‑adjacent.
* **Related Standards/Requirements:** SWE020, SWE133, SWE134, SWE013.

**LLSW16 — Evaluate Software for Security Vulnerabilities (CBCS Context)**

* **Context/Background:** Lack of L2 cybersecurity requirements led to insufficient security architecture implementation.
* **Lesson Learned:** Develop **Space Vehicle Cybersecurity Requirements** and **CONOPS**; evaluate software for vulnerabilities throughout lifecycle.
* **Evidence/Observation:** Modules/components did not implement security commensurate with system importance.
* **Cause(s):** Decisions to defer security; absent program‑level baseline.
* **Recommendation/Corrective Action:** Establish cybersecurity baselines; integrate security evaluation into IV&V and acceptance.
* **Implementation Guidance:** **SWE158**, **SWE013**, **SWE018**.
* **Success Criteria/Verification:** Documented scans/analyses; mitigations tracked; successful security reviews.
* **Applicability/Scope:** All CBCS and mission‑critical software.
* **Related Standards/Requirements:** SWE158, SWE013, SWE018.

**LLSW17 — Tool and Database Usability Drives Process Quality**

* **Context/Background:** Tools lacked features/automation; visibility leaks; usability issues degraded reviews and traceability.
* **Lesson Learned:** Select/configure tools based on **process needs**; mandate usability, automation, partitioning, and reporting capabilities.
* **Evidence/Observation:** Commenting, partitioning, PDF generation, and access governance weaknesses added workload and risk.
* **Cause(s):** Sustainment‑only funding; late tool development; ad‑hoc admin.
* **Recommendation/Corrective Action:** Conduct **analysis of alternatives**; fund capability expansion; embed operational architects; standardize partitions and role models.
* **Implementation Guidance:** Capture in **SWE013** (plans) and **SWE091** (measurement repositories) with defined KPIs.
* **Success Criteria/Verification:** Reduced manual auditing; reliable exports; secure access; KPI improvements (latency, completeness).
* **Applicability/Scope:** All assurance tools, requirements DBs, risk systems.
* **Related Standards/Requirements:** SWE013, SWE091.

**LLSW20 — Apply Software Assurance to Ground Segment Architecture**

* **Context/Background:** Integrated ground segment wasn’t defined early; delayed hazard reports; unclear responsibilities.
* **Lesson Learned:** Define **ground segment architecture early**, including hazard report ownership, requirements, ICDs, and integrated test plans.
* **Evidence/Observation:** MCC hazard report delivery delayed due to undefined overall architecture.
* **Cause(s):** Program‑level planning gap.
* **Recommendation/Corrective Action:** Fund an integrator; include simulations/test facilities; align with SA and IV&V processes.
* **Implementation Guidance:** **SWE013**, **SWE018**, **SWE050** (requirements/ICDs).
* **Success Criteria/Verification:** Architecture baselined; hazard reports on schedule; integrated test coverage achieved.
* **Applicability/Scope:** Programs with multi‑center ground segments.
* **Related Standards/Requirements:** SWE013, SWE018, SWE050.

### **Common Themes from NASA Lessons Learned**

| **Key Lesson Area** | **Lesson Summary** | **Implication/Action** |
| --- | --- | --- |
| Comprehensive Planning | Address all phases of the software life cycle with thorough preparation for integration and testing. | Develop detailed plans that include schedules, budgets, risks, and contingency measures. |
| Embedded Security Planning | Security planning must be proactive, covering design, testing, and operational phases. | Include detailed cybersecurity provisions in software plans, such as threat analysis and vulnerability assessments. |
| Stakeholder Alignment | Misalignment between software and system engineering plans can lead to delays and failures. | Ensure all stakeholders participate in planning activities to maintain alignment across disciplines. |
| Detailed Testing Plans | Testing gaps often result in costly defects and schedule slips. | Define test phases comprehensively, including safety-critical and off-nominal conditions for full coverage. |
| Tailoring with Risk Management | Tailoring must balance flexibility with risk mitigation and directive adherence. | Document tailoring decisions with risk analyses and fallback strategies. |
| Phase-Specific Documentation | Incomplete or unmaintained documentation can cause delays and confusion during testing/integration. | Maintain detailed records during each software life cycle stage, ensuring configuration management is robust. |
| Adaptive Planning | Agile and iterative environments require dynamic software plans. | Use iterative planning methodologies while ensuring traceability to directives and goals. |

---

### **Implementation**

NASA's lessons learned emphasize that a well-maintained software plan not only ensures compliance with directives but also mitigates risks, supports mission success, and reduces lifecycle costs. This guidance can support improved execution of requirement **3.1.3** through practical strategies based on historical successes and challenges.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* **[Incremental development and integration can save life cycle cost and reduce risk](https://software.gsfc.nasa.gov/lesson-details/2/)**. **Lesson Number 2** : The recommendation states: "Incremental development and integration requires money and coordination up-front, as it can save life cycle cost and reduce risks."
* **[In the FSW plan, include staffing for FSW GN&C requirements](https://software.gsfc.nasa.gov/lesson-details/69/)**. **Lesson Number 69** : The recommendation states: "In the FSW plan, include staffing for FSW GN&C requirements definition/refinement throughout the entire lifetime of FSW GNC development."
* **[Commitments for the resources needed for all levels of testing](https://software.gsfc.nasa.gov/lesson-details/89/)**. **Lesson Number 89** : The recommendation states: "Plan for and obtain commitments for the resources needed for all levels of testing."
* **[Leverage planned testing activities to verify ground system requirements](https://software.gsfc.nasa.gov/lesson-details/122/)**. **Lesson Number 122** : The recommendation states: "Leverage planned testing activities to verify ground system requirements."
* **[Allow the contractor to follow their own approach, when it's a proven approach](https://software.gsfc.nasa.gov/lesson-details/143/)**. **Lesson Number 143** : The recommendation states: "Allow the contractor to follow their own approach, when it's a proven approach."
* **[Each mission partner should identify a single assignee in the project management office](https://software.gsfc.nasa.gov/lesson-details/174/)**. **Lesson Number 174** : The recommendation states: "All stakeholders in end-to-end system testing should identify a person in their project management office responsible for the success of the end-to-end testing. These assignees should be at the proper level to assign resources and prioritize work of engineers, if necessary."
* **[Early project software review of SMP deliverables](https://software.gsfc.nasa.gov/lesson-details/298/)**. **Lesson Number 298** : The recommendation states: "The project's software management plan (SMP) should explain the delivery and review chain for all software products, especially when they are not being delivered directly to the project. If there are more than one or two organizations with separate configuration management systems between the developer and the project review, they should make plans to have the person who is eventually responsible for technical approval of SDP deliverables (e.g., project software engineer or project software lead) be involved in the review process earlier on."
* **[Daily stand-ups, Sprint Demos, and Sprint Planning meetings increase collaboration within the team](https://software.gsfc.nasa.gov/lesson-details/310/)**. **Lesson Number 310** : The recommendation states: "Agile/Scrum process can be used not only for software development but also during design phases of the project to increase collaboration among the team."
* **[GOLD Rule 1.43 provides end-to-end demonstration for each SW component that can be changed in flight](https://software.gsfc.nasa.gov/lesson-details/343/)****.** **Lesson Number 343** : The recommendation states: "There are multiple Observatory components with loadable flight software - demonstrating the code change process for each spacecraft and instrument FSW component can be very beneficial and useful. Incorporate into project plans and budgets and provide resources for the satisfaction of the GOLD Rule 1.43 requirement for pre-flight end-to-end code change demonstrations."

# 7. Software Assurance

**SWE-013 - Software Plans**

3.1.3 The project manager shall develop, maintain, and execute software plans, including security plans, that cover the entire software life cycle and, as a minimum, address the requirements of this directive with approved tailoring.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that all plans, including security plans, are in place and have expected content for the life cycle events, with proper tailoring for the classification of the software.

2. Develop and maintain a Software Assurance Plan following the content defined in NASA-HDBK-2203 for a software assurance plan, including software safety.

## 7.2 Software Assurance Products

#### **1. Plan Reviews**

* **Artifacts:**
  + **Plan Review Checklists:** Comprehensive checklists to verify all required software plans (e.g., Software Development Plan (SDP), Software Assurance Plan (SAP), Software Configuration Management Plan, Software Security Plan, etc.) are:
    - Developed for all life cycle stages.
    - Approved with required tailoring where applicable.
    - Fully compliant with NPR 7150.2 requirements and project-specific directives.
  + **Plan Review Reports:** Summarize the initial gaps, approved tailoring requests, and resolutions from plan reviews conducted during each life cycle phase.
* **Purpose:**
  + To provide verified assurance that all plans are in place, suitable for the mission, and meet agency directives.
  + To confirm that plan tailoring has been reviewed, justified, and approved, ensuring compliance is maintained.

#### **2. Software Assurance Plan (SAP)**

* **Artifacts:**
  + **Detailed SAP Document:** Specifies all software assurance processes, tasks, milestones, and responsibilities, mapped to NPR 7150.2 and associated standards (e.g., NASA-STD-8739.8).
    - Includes task mappings to relevant assurance standards (e.g., NASA software safety standards, cybersecurity requirements).
    - Explicitly defines acceptance criteria for assurance verification activities.
    - Details the approach to evaluate safety-critical and security-critical software components.
  + **SAP Updates:** Logs of updates made to the SAP as the software progresses through life cycle phases.
* **Purpose:**
  + To ensure software assurance is implemented consistently throughout the project, with clearly defined processes and accountability for all life cycle phases.

#### **3. Issue and Risk Records**

* **Artifacts:**
  + **Risk Identification Logs:** Documents identifying key risks related to software life cycle planning and execution, including:
    - Risks to implementation of NPR 7150.2 requirements.
    - Planning-related risks such as schedule misalignment, tailoring deviations, or unaddressed compliance gaps.
    - Software assurance-specific risks, like incomplete hazard analyses or inadequate testing for safety/security-critical components.
  + **Issues Records and Resolutions Report:** Tracks and resolves software issues (including defects, anomalies, and non-conformances) discovered during life cycle execution, with associated resolution timelines and evidence of closure.
  + **Risk Mitigation Plans:** Risk mitigation actions for unresolved risks and documentation of approvals for risk tolerance levels.
* **Purpose:**
  + To track, analyze, and address risks in both planning and execution phases, ensuring they are managed effectively to meet software assurance goals.

#### **4. Compliance Tracking Reports**

* **Artifacts:**
  + **Compliance Status Reports:** Regularly updated reports tracking the progress of software assurance activities, showing:
    - Status of assurance planning tasks (e.g., hazard analyses, test verification).
    - Milestone completion rates for deliverables such as Software Verification and Validation (V&V) plans.
    - Tailoring justifications and compliance audits to track deviations from standard requirements.
  + **Milestone Deliverable Reports:** Reports verifying major assurance deliverables (e.g., test results, safety analyses, and verification reviews) tied to project milestones.
  + **Gap Analysis Reports:** Results from compliance audits identifying gaps between NPR 7150.2 requirements and project execution, along with recommendations for remediation.
* **Purpose:**
  + To provide a structured overview of software assurance progress, ensuring all NPR 7150.2-mandated tasks and milestones are completed.

---

### **Refinements and Expansions to Improve Assurance:**

1. **Tailoring Assessment Reports:**

   * Newly added evidence to evaluate and document how software plans have been tailored, assessing risk impacts, and verifying alignment with required safety, security, and quality standards.
2. **Mapping of Plans to Risk Management:**

   * Clear inclusion of how each software plan links to identified risks and mitigations, ensuring that risks are addressed within the life cycle planning effort.
3. **Lifecycle Phase Completion Reports:**

   * Broaden compliance reports to include phase-specific assessments, such as how assurance tasks (e.g., validation, hazard assessment) were tailored and executed in alignment with software life cycle stages (e.g., planning, implementation, maintenance).
4. **Integration of Cybersecurity and Safety Plans with Assurance Goals:**

   * Ensure comprehensive integration of software cybersecurity requirements into the SAP and compliance tracking to demonstrate focus on both security and safety considerations.

---

#### **Summary of Key Products:**

| **Assurance Product** | **Purpose** | **Deliverables** |
| --- | --- | --- |
| **Plan Reviews** | Verifies all plans meet NPR 7150.2, tailoring is approved, and all life cycle stages are addressed. | Checklists, review reports, gap analyses, tailoring assessments. |
| **Software Assurance Plan** | Establishes, maintains, and validates software assurance processes and compliance. | Detailed SAP document, updated SAP versions, task mapping records. |
| **Issue and Risk Records** | Tracks risks and issues throughout life cycle, ensuring actions are verified and resolved. | Risk logs, resolution reports, mitigation plans. |
| **Compliance Tracking Reports** | Ongoing status tracking and closure of assurance tasks and milestones. | Compliance reports, milestone verifications, V&V task tracking. |

---

By implementing this refined structure, the project ensures that software assurance products are comprehensive, aligned with directives, and address all life cycle phases effectively. The improved detail provides greater clarity, traceability, and risk accountability in meeting the intent of the requirement.

## 7.3 Metrics

To measure the effectiveness of software assurance activities for this requirement, which mandates the development, maintenance, and execution of comprehensive software plans (including security plans) across the entire software life cycle, **metrics provide crucial data** on progress, compliance, risks, and performance. These metrics allow stakeholders to monitor assurance tasks, ensure alignment with directives, and identify areas for improvement.

By using these metrics, **software assurance teams** and project managers can monitor progress, assess compliance at each life cycle phase, and address risks proactively. Metrics also support effective communication with stakeholders and ensure alignment with the directive through actionable insights based on real-time data.

Below is a detailed list of **Software Assurance Metrics** specifically tailored to this requirement:

### 7.3.1 Metrics for Plan Development

#### **Metric 1: Plan Completeness**

**Definition**: Percentage of required software plans developed and approved.

* **Formula**: [ \text{Plan Completeness} = \left( \frac{\text{Number of Approved Plans}}{\text{Total Required Plans}} \right) \times 100 ]
* **Purpose**: Measure whether all necessary plans (e.g., Software Development Plan, Software Assurance Plan, IT Security Plan) are prepared and approved.
* **Target Value**: 100% of required plans by approved milestone deadlines.

#### **Metric 2: Tailoring Coverage**

**Definition**: Percentage of required tailoring activities completed and documented in plans.

* **Formula**: [ \text{Tailoring Coverage} = \left( \frac{\text{Number of Tailored Plans}}{\text{Total Plans Requiring Tailoring}} \right) \times 100 ]
* **Purpose**: Indicates that plans are correctly tailored to reflect software classification, safety-criticality, and project size.
* **Target Value**: 100% compliance to approved tailoring criteria.

#### **Metric 3: Plan Review Progress**

**Definition**: Percentage of plans reviewed on schedule for completeness and adherence to standards.

* **Formula**: [ \text{Review Progress} = \left( \frac{\text{Plans Reviewed}}{\text{Total Plans for Review}} \right) \times 100 ]
* **Purpose**: Tracks progress of reviews to validate compliance with NPR 7150.2 requirements and NASA-STD-8739.8 assurance standards.

### 7.3.2 Metrics for Plan Maintenance

#### **Metric 4: Plans Updated Per Milestone**

**Definition**: Percentage of software plans updated during interim reviews or life cycle milestones.

* **Formula**: [ \text{Plan Update Rate} = \left( \frac{\text{Number of Updated Plans}}{\text{Total Plans Requiring Updates}} \right) \times 100 ]
* **Purpose**: Measures alignment of plans with evolving project requirements or risks based on maturity guidance (NASA-HDBK-2203, Section 7.08).
* **Target Value**: Plans updated within baseline timelines for given milestones.

#### **Metric 5: Configuration Management Compliance**

**Definition**: Percentage of configuration-controlled plans and associated change records.

* **Formula**: [ \text{Configuration Compliance} = \left( \frac{\text{Number of Controlled Plans}}{\text{Total Plans Requiring Configuration Management}} \right) \times 100 ]
* **Purpose**: Ensures configuration management processes are applied to ensure integrity and version tracking of life cycle documents.

#### **Metric 6: Risk Resolution Rate for Plans**

**Definition**: Percentage of identified risks (in plans) resolved or mitigated on schedule.

* **Formula**: [ \text{Risk Resolution Rate} = \left( \frac{\text{Number of Resolved Risks}}{\text{Total Risks Identified}} \right) \times 100 ]
* **Purpose**: Tracks how effectively risks related to software assurance planning are mitigated before they impact development.

### **7.3.3 Metrics for Plan Execution**

#### **Metric 7: Assurance Task Completion**

**Definition**: Percentage of software assurance tasks completed versus planned.

* **Formula**: [ \text{Task Completion} = \left( \frac{\text{Assurance Tasks Completed}}{\text{Total Planned Assurance Tasks}} \right) \times 100 ]
* **Purpose**: Tracks execution of software assurance tasks (as documented in the Software Assurance Plan using the SA Tasking Checklist Tool).
* **Target Value**: 95-100% tasks completed on schedule.

#### **Metric 8: Testing Coverage**

**Definition**: Percentage of planned test cases executed successfully against test objectives.

* **Formula**: [ \text{Testing Coverage} = \left( \frac{\text{Test Cases Completed Successfully}}{\text{Total Planned Test Cases}} \right) \times 100 ]
* **Purpose**: Ensures V&V activities specified in plans (e.g., test plans) are executed and results are tracked.

#### **Metric 9: Issue Resolution and Closure Rate**

**Definition**: Percentage of identified plan execution issues tracked to closure.

* **Formula**: [ \text{Issue Resolution Rate} = \left( \frac{\text{Issues Closed}}{\text{Total Issues Identified}} \right) \times 100 ]
* **Purpose**: Tracks timely remediation of non-compliance or execution issues during plan implementation.

### 7.3.4 Metrics for Security Planning and Execution

#### **Metric 10: Security Plan Coverage**

**Definition**: Percentage of required security assurance activities covered in the IT Security Plan.

* **Formula**: [ \text{Security Plan Coverage} = \left( \frac{\text{Security Tasks Documented in Plan}}{\text{Total Required Security Tasks}} \right) \times 100 ]
* **Purpose**: Ensures the IT Security Plan comprehensively covers security assurance activities across the life cycle.

#### **Metric 11: Vulnerability Mitigation Rate**

**Definition**: Percentage of identified security vulnerabilities resolved during testing phases or risk management reviews.

* **Formula**: [ \text{Mitigation Rate} = \left( \frac{\text{Resolved Vulnerabilities}}{\text{Total Vulnerabilities Identified}} \right) \times 100 ]
* **Purpose**: Tracks how effectively software assurance mitigates security risks and vulnerabilities.

#### **Metric 12: Security Testing Coverage**

**Definition**: Percentage of planned security tests executed versus total tests planned (e.g., penetration testing, static/dynamic analysis).

* **Formula**: [ \text{Security Testing Coverage} = \left( \frac{\text{Security Tests Executed}}{\text{Total Security Tests Planned}} \right) \times 100 ]
* **Purpose**: Tracks completion of security assurance activities specified in the Software Assurance Plan or IT Security Plan.

### **7.3.5 Metrics for Risk Management**

#### **Metric 13: Risk Identification Rate**

**Definition**: Number of risks identified at each life cycle phase per the Software Risk Management Plan.

* **Formula**: No formula—count risks identified for each phase (e.g., requirements, design, testing).
* **Purpose**: Helps track proactive risk discovery and planning throughout the software life cycle.

#### **Metric 14: Risk Impact Reduction Rate**

**Definition**: Percentage reduction in the severity of risks associated with assurance planning.

* **Formula**: [ \text{Impact Reduction Rate} = \left( \frac{\text{Mitigated High-Impact Risks}}{\text{Total Identified High-Impact Risks}} \right) \times 100 ]
* **Purpose**: Tracks how risks impacting plan execution or life cycle elements are managed effectively.

### 7.3.6 Metrics for Independent Oversight

#### **Metric 15: Audit Coverage**

**Definition**: Percentage of required software assurance audits conducted on schedule.

* **Formula**: [ \text{Audit Coverage} = \left( \frac{\text{Audits Conducted}}{\text{Total Required Audits}} \right) \times 100 ]
* **Purpose**: Tracks assurance compliance through audits by independent oversight organizations (e.g., OSMA).

#### **Metric 16: Non-Compliance Incident Rate**

**Definition**: Number of non-compliance incidents per review identified by audit teams.

* **Formula**: No formula—log number of incidents found per milestone review.
* **Purpose**: Tracks adherence to approved assurance plans and standards.

### 7.3.7 Performance Targets

| **Metric** | **Target Value** | **Acceptable Threshold** |
| --- | --- | --- |
| Plan Completeness | 100% | ≥95% |
| Tailoring Coverage | 100% | ≥90% |
| Task Completion Rate | 95-100% | ≥90% |
| Testing Coverage | ≥95% | ≥85% |
| Security Testing Coverage | ≥95% | ≥85% |
| Risk Resolution Rate | ≥90% | ≥80% |
| Audit Coverage | 100% | ≥95% |

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance

Here is the **Software Assurance Guidance for Requirement 3.1.3**, incorporating the detailed process, tools, documents, and responsibility chain mentioned. It provides a clear and actionable breakdown, tailored for use by software assurance professionals tasked with ensuring compliance with this directive.

By following these steps, **Software Assurance (SA)** ensures that project software plans are not only compliant but also contribute to achieving high reliability, security, and mission success. **Tailored processes** and tools (e.g., the SA Tasking Checklist Tool) help streamline assurance efforts, especially on small or resource-limited projects.

### **Step 1: Confirm All Appropriate Software Plans Are in Place**

#### **Objective:**

Ensure that all software plans required for the project are appropriately developed, contain the expected content, and align with the software classification, safety criticality, and life cycle events specified. Proper tailoring must address the project’s size, complexity, and risk profile, and the plans must adhere to NPR 7150.2 and NASA-STD-8739.8 (Software Assurance Standard).

#### **Actions for Software Assurance:**

1. **Identify Required Plans**: Software assurance must confirm the existence of the following key software plans, ensuring their content matches project classifications and milestones:

   * **Software Development or Management Plan (SDP/SMP)**: Defines how software will be developed, managed, and delivered.
   * **Software Configuration Management Plan (SCMP)**: Details control mechanisms for change management, baselines, and documentation.
   * **Software Test Plans**: Details verification and validation approaches, including security and safety testing strategies.
   * **Software Maintenance Plans**: Explains long-term maintenance tasks for bug fixes, patches, and updates.
   * **Software Assurance Plans (SAP)**: Outlines assurance tasks, responsible personnel, and compliance monitoring processes.
   * **Software Safety Plan**: Required for safety-critical software; identifies strategies for hazard prevention, failure mitigation, and fault analysis.
   * **IT Security Plans**: Details how data protection, security testing, and compliance with cybersecurity standards will be addressed.
2. **Additional Plans to Consider**: Further refine the review by considering other key planning documents, ensuring proper tailoring and expected content:

   * **Software Risk Management Plan**: Outlines processes for identifying, assessing, and mitigating software-related risks.
   * **Verification and Validation (V&V) Plans**: Details strategies, methods, and tools for ensuring software functionality, quality, and reliability.
   * **Software Operations/Maintenance Plans**: Addresses system support, upgrades, and maintenance post-deployment.
   * **Software Retirement Plan**: Ensures an orderly decommissioning of software when it is no longer required.
3. **Recommended Guidance and Documentation**:

   * **Minimum Plan Contents**: Use NASA-HDBK-2203 Section 7.18 (Documentation Guidance) to verify the minimum recommended content for each type of software plan.
   * **Consistency with Maturity At Milestones**: Evaluate plan availability based on expected life cycle maturity as outlined in NASA-HDBK-2203 Section 7.08.
4. **Tailoring Considerations**:

   * Confirm that tailoring for the classification of the software (per NPR 7150.2) is properly justified, approved, and documented.
   * Verify that each tailored plan addresses all life cycle phases, including initiation, development, testing, deployment, operation, maintenance, and retirement.

#### **Outputs**:

* A checklist confirming the existence and alignment of required plans and identifying missing or inadequate content.
* A review report documenting tailoring justifications and compliance with relevant standards and classifications.

### **Step 2: Develop a Software Assurance Plan (SAP)**

#### **Objective**:

Ensure the creation of a robust Software Assurance Plan (SAP), tailored for project-specific requirements, to track and oversee all software assurance and software safety tasks throughout the life cycle.

#### **Key Actions for Developing the SAP**:

1. **Follow NASA-HDBK-2203 Content Guidance**:

   * Use Section **8.51 – Software Assurance Plan** as a reference to define the contents of the SAP.
   * Include a **mapping matrix** for software assurance and software safety requirements, linking tasks to NPR 7150.2 and NASA-STD-8739.8 guidelines.
2. **Use the SA Tasking Checklist Tool**:

   * The **SA Tasking Checklist Tool** streamlines the creation of a tailored list of software assurance and safety tasks.
   * How it works:
     + Tailor software assurance tasks based on software classification (e.g., safety-critical or high-risk classifications) and milestones.
     + Create project-specific checklists mapped to milestones (e.g., requirements reviews, design reviews) to ensure compliance and monitor progress.
   * Tool functionality includes:
     + SA task tracking
     + Reports exportable to Excel, JIRA, and MS Project.
     + Built-in User Guide for step-by-step instructions.
3. **Establish Dependencies and Tailoring Levels**: Document tailoring decisions in the SAP based on:

   * **Software Classification Decision**: Tailor assurance activities according to NPR 7150.2 classifications (A-E, safety criticality).
   * **Software Requirements Mapping Matrix**: Map assurance tasks directly to project-specific software requirements.
   * **SA-Specific Tailoring**: Define detailed tailoring within the assurance tasking checklist.
4. **Purpose of the SAP**:

   * Plan, execute, and monitor software assurance requirements tailored to each life cycle milestone.
   * Include coordination efforts with IV&V (if applicable) and risk mitigation activities.

### **Step 3: Assess Software Plans for Risks, Issues, Completeness, and Compliance**

#### **Objective**:

Evaluate the completeness, alignment, and compliance of all software plans with NPR 7150.2, NASA-STD-8739.8, and project-specific requirements.

#### **Assessment Areas**:

1. **Compliance and Completeness**:

   * Ensure plans satisfy their requirements based on software classification and risk profiles.
   * Confirm the plans cover all applicable life cycle events and critical development milestones.
2. **Consistency Across Plans**:

   * Analyze consistency among related plans (e.g., configuration management aligning with risk management) to prevent gaps or conflicts.
   * Verify alignment between system plans, deliverables, and software-specific plans.
3. **Identification of Dependencies and Risks**:

   * Ensure plans identify critical paths, dependencies, and coordination needs for smooth execution.
   * Highlight potential risks associated with plan omissions, mismatches, or inadequate content.
4. **Coverage of Critical Topics**:

   * Initial software safety criticality assessments.
   * Security risk evaluation (e.g., cybersecurity threats, vulnerabilities).
   * IV&V coordination and task definition (if applicable).
5. **Completeness for Each Life Cycle Phase**:

   * Plans must include required content and address deliverables for all phases, from initiation to retirement.
6. **Outputs**:

   * Identification of issues and risks during the review phase.
   * Reporting of risks, deficiencies, and recommendations to software management and project personnel.
   * Tracking and monitoring of identified risks/issues until closure.

### **Step 4: Oversight of Software Assurance Execution**

The **Office of Safety and Mission Assurance (OSMA)** oversees execution of software assurance requirements and ensures personnel responsible for these activities are properly trained and maintain independence from the development team.

#### **Key Principles**:

1. **Separation of Oversight and Development**:

   * Ensure that software assurance and software safety activities (e.g., safety analysis) conducted by development teams are independently verified by software assurance personnel.
   * Maintain reporting chains independent of the development organization.
2. **Assurance of Acquisition and Contracted Software**:

   * Confirm assurance processes account for vendor/software provider activities, ensuring compliance with NASA's documentation and assurance standards.
   * Evaluate vendor deliverables for completeness (if applicable).
3. **Documentation of Responsibilities**:

   * The SAP must explicitly define which personnel or groups (NASA, contractor, or center personnel) will perform each assurance activity.
4. **Monitoring and Reporting**:

   * Continuously monitor SA task lists for progress.
   * Report unresolved risks to the Safety and Mission Assurance (SMA) reporting chain.

## 7.4.1 Deliverables for Software Assurance Guidance

1. **Plan Reviews**: Checklists and reports verifying all plans are in place, tailored, and compliant.
2. **Software Assurance Plan**: Detailed SAP with mappings to NPR 7150.2 and SA Tasking results.
3. **Issue and Risk Reports**: Records of identified risks, tracked and resolved.
4. **Compliance Status Reports**: Reports tracking execution of assurance tasks and milestones.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.17 - Software Assurance Plan Minimum Content](/spaces/SWEHBVD/pages/138707548/5.17+-+Software+Assurance+Plan+Minimum+Content) * [5.18 - Safety Plan Minimum Content](/spaces/SWEHBVD/pages/138707600/5.18+-+Safety+Plan+Minimum+Content) * [7.05 - Work Breakdown Structures That Include Software](/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.15 - SA Tasking Checklist Tool](/spaces/SWEHBVD/pages/102695742/8.15+-+SA+Tasking+Checklist+Tool) * [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

# 8. Objective Evidence

Objective evidence for this requirement enables stakeholders to ensure compliance with the directive, verify the inclusion of required life cycle activities, and demonstrate that proper software plans—including security plans—are developed, tailored, and executed effectively. Objective evidence must be tangible, measurable, and traceable to the requirement, providing confidence that the software assurance process is conducted according to the directive, approved tailoring, classification, and project-specific needs.

By accumulating, assessing, and validating these objective evidence artifacts, Software Assurance can verify full compliance with this requirement and ensure that appropriate plans, practices, and tools are in place to achieve high-quality, secure, and mission-compliant outcomes.

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

Here is a structured breakdown of objective evidence for this requirement:

## 8.1 Objective Evidence for "Developing Software Plans"

### 8.1.1 Approved Software Plans

* Signed or approved versions of software plans that address the full life cycle, including tailoring for software classification and safety-criticality.
* Plans may include:
  + **Software Development or Management Plan (SDP/SMP):** Defines processes, timelines, deliverables, and resources. [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)
  + **Software Configuration Management Plan (SCMP)**: Outlines versioning, baseline control, and change approval workflows. [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan)
  + **Software Test Plans:** Details test cases, testing methodologies, and expected results. [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)
  + **Software Assurance Plan (SAP):** Documents assurance activities based on plans tailored to NPR 7150.2 and NASA-STD-8739.8 requirements. [5.17 - Software Assurance Plan Minimum Content](/spaces/SWEHBVD/pages/138707548/5.17+-+Software+Assurance+Plan+Minimum+Content)
  + **Software Safety Plan:**Addresses hazard assessment and mitigation (for safety-critical software). [5.18 - Safety Plan Minimum Content](/spaces/SWEHBVD/pages/138707600/5.18+-+Safety+Plan+Minimum+Content)
  + **IT Security Plan:**Defines processes for cybersecurity risk management, secure coding practices, and vulnerability testing.

### 8.1.2 Documentation of Tailoring

* Tailoring rationale and approval records.
  + **Software Classification Justification** (e.g., NPR 7150.2 classification decisions).
  + Documentation of tailored requirements removed, adjusted, or combined in project-specific plans.
  + Records demonstrating alignment with the Software Requirements Mapping Matrix and assurance/safety standards (NASA-STD-8739.8).

### 8.1.3 Plan Consistency Review Reports

* Records confirming consistency across plans (e.g., risk management aligning with safety measures) and proper coverage of life cycle phases.
* **Traceability Matrix:**
  + Maps project requirements (functional and assurance-related) to specific plans and life cycle activities.

### 8.1.4 Maturity Assessment Reports

* Reports showing readiness and baseline maturity of software plans at key milestones, referencing NASA-HDBK-2203 Section [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews)**.**

## 8.2 Objective Evidence for "Maintaining Software Plans"

### 8.2.1 Version Control Records

* Configuration management records detailing updates to software plans throughout the life cycle.
* Change logs documenting revisions to tailored plans, with approval signatures.

### 8.2.2 Plan Review and Approval Reports

* Records of periodic reviews to ensure plans remain current and aligned with project progress and risks.
* Evidence of stakeholder engagement in reviews (e.g., meeting minutes, review sign-offs).
* Results of audits or inspections confirming adequacy and compliance of the plans.

### 8.2.3 Risk Management Documentation

* Identified risks in software plans (e.g., omissions, conflicts between plans, misaligned assumptions).
* Risk mitigation strategies incorporated into plan updates and approved by stakeholders.

## 8.3 Objective Evidence for "Executing Software Plans"

### 8.3.1 Software Assurance Tasking Checklist Tool Outputs

* Tailored tasking checklists generated using the SA Tasking Checklist Tool, ensuring planned assurance tasks are appropriate for the software’s classification, safety-criticality, and milestones.
* Checklist outputs showing tracked progress on assurance tasks throughout the life cycle, including:
  + Initial planning stages.
  + Milestone reviews.
  + Testing and verification phases.

### 8.3.2 Records of Software Assurance Activities

* Evidence that software assurance plans are followed during development and testing.
  + Examples:
    - Verification results (e.g., review of requirements, designs, code).
    - Validation results (e.g., test execution reports).
    - Security testing results (e.g., vulnerability scans, penetration tests).
* Compliance audits checking adherence to planned processes outlined in the SAP.

### 8.3.3 Testing Reports

* Records demonstrating execution of test plans, including:
  + Test case pass/fail results.
  + Security and safety testing outcomes.
  + Defect tracking logs.

### 8.3.4 Configuration Management Records

* Evidence of planned baseline approvals for code, documentation, and testing artifacts.
* Audit verification of configuration management tasks being performed as specified.

## 8.4 Objective Evidence for "Security Planning and Execution"

### 8.4.1 IT Security Plan

* Approved version of the IT Security Plan tailored to address data protection, secure coding practices, and vulnerability testing.

### 8.4.2 Security Testing Results

* Evidence of security-related assurance activities being conducted:
  + Static analysis tool outputs (e.g., secure coding flaw identification from tools like SonarQube).
  + Dynamic analysis vulnerability reports.
  + Penetration testing reports.
  + Incident response testing results.

### 8.4.3 Security Risk Assessment Documentation

* Threat modeling reports identifying high-risk areas related to cybersecurity.
* Documentation of actions taken to mitigate vulnerabilities.

### 8.4.4 Secure Deployment and Maintenance Logs

* Records demonstrating post-deployment security monitoring and maintenance, as outlined in the IT Security Plan and SAP.
* Evidence of patch management and security updates being applied.

## 8.5 Objective Evidence for Key Measures of Compliance

### 8.5.1 Consistency Across Software Plans

* Evidence that plans were cross-checked for consistency:
  + Risk management aligning with configuration management.
  + Problem/discrepancy reporting embedded in all plans.

### 8.5.2 Traceability of Requirements in Plans

* Traceability matrix linking software assurance requirements to tailored plans and NPR 7150.2 standards.

### 8.5.3 Coverage of Life Cycle Phases in Plans

* Review reports verifying each plan includes all applicable life cycle phases:
  + Requirements definition.
  + Design and development.
  + Testing and verification.
  + Deployment, operations, and maintenance.
  + Retirement/decommissioning.

### 8.5.4 Identification of Risks in Plans

* Reports documenting risks associated with plans, such as:
  + Safety criticality.
  + Security vulnerabilities.
  + Incomplete or mismatched plan coverage.

### 8.5.5 Monitoring and Reporting

* Logs of risks and issues identified during plan execution with evidence of resolution and tracking to closure.
* Audit reports verifying compliance throughout life cycle milestones.

## 8.6 Objective Evidence for Independent Oversight

### 8.6.1 Training and Personnel Documentation

* Evidence that personnel performing software assurance activities (both internal and external) meet training and qualification requirements.

### 8.6.2 Independent Review Records

* Reports or audits from independent oversight organizations (e.g., OSMA) verifying software assurance activities were performed independently of the development team.

### 8.6.3 SMA Reporting Chain Records

* Documentation of independent reporting processes for SMA personnel, including escalation of unresolved risks to higher authorities.

## 8.7 Examples of Tangible Objective Evidence

| Category | Example Evidence |
| --- | --- |
| Approved Software Plans | Signed SDP, SAP, SCMP, IT Security Plan. |
| Tailoring Documentation | Justified tailoring rationale, Software Classification Decision. |
| Checklist Tool Output | SA Tasking Checklist tailored to project classification. |
| Testing Results | Unit/system test results, security validation reports. |
| Risk Assessment Reports | Identified risks and mitigation plans. |
| Maturity Review Reports | Reports tracking life cycle maturity for plans at milestones. |
| Configuration Management Records | Logs tracking changes to plans, software baselines. |
| Security Testing Results | Vulnerability assessment and penetration testing reports. |
| Independent Oversight Reports | Separation of assurance tasks from development, audit findings. |
| SMA Training and Qualifications | Records of trained personnel performing assurance duties. |
