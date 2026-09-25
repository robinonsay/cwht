# SWE-005 - Software Processes

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695395. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes

SWE-005 - Software Processes

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695395/SWE-005+-+Software+Processes#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695395)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695395&showCommentArea=true&showComments=true#addcomment)

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

2.1.5.3 Center Director, or designee, shall establish, document, execute, and maintain software processes per the requirements in this directive.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-005 History

SWE-005 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 1.2.4 Each Center shall establish, document, execute, and maintain software processes. |
| Difference between A and B | Center Directors, or designees, shall establish, document, execute, and maintain software processes. |
| B | 2.1.3.3 Center Directors, or designees, shall establish, document, execute, and maintain software processes. |
| Difference between B and C | Added "per the requirements in this directive." |
| C | 2.1.5.3 Center Director, or designee, shall establish, document, execute and maintain software processes per the requirements in this directive. |
| Difference between C and D | No change |
| D | 2.1.5.3 Center Director, or designee, shall establish, document, execute, and maintain software processes per the requirements in this directive. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

Software engineering is a core capability and a key enabling technology necessary for the support of NASA's missions. Ensuring the quality, safety, and reliability of NASA software is of paramount importance in achieving mission success. Additionally, the exponential growth in the scope, complexity, and importance of software within NASA systems experienced over the years is expected to continue, challenging our ability to manage it effectively. The Software processes define a set of technical and management frameworks for applying methods, tools, and people to the task of developing software products. Software processes:

* Ensure that NASA has the best available software engineering practices and techniques applied to its projects.
* Enable seamless multi-Center software development for NASA projects.
* Ensure quick and effective mobility of assignments for software engineering personnel.
* Establish a common understanding of the software engineering discipline.
* Maintain and improve NASA's software engineering capability, tools, principles/rules, and Capability Maturity Model Integration (CMMI®) **[689](#_tabs-<p></p>)** rating with reduced Center and project effort and cost.
* Reduce the risk in critical software development activities by use of a common set of software principles/rules.
* Enable a more affordable approach for NASA software development.

Software is critical to the success of NASA missions, ranging from spacecraft control and scientific data processing to safety-critical systems. Establishing and maintaining structured, repeatable software processes ensures software quality, reliability, and safety. This requirement places accountability on the Center Director to implement processes that comply with NASA’s software engineering standards. By meeting this requirement, Centers ensure alignment with NASA's overall mission objectives and safety protocols.

## 2.1 Key Rationale for the Requirement

### 1. Supports NASA’s Mission Safety, Goals, and Success

* NASA’s missions heavily rely on software for critical and non-critical functions. Errors or deficiencies in software processes can lead to catastrophic mission failures (e.g., spacecraft losses, safety risks, delays, or cost overruns).
* This requirement ensures the development of reliable, safe, and predictable software systems that contribute to NASA’s mission success.

**Example**:

* The **Mars Polar Lander (MPL) failure (1999)** resulted from an undetected software error that caused the landing engines to shut off prematurely. A robust software process might have identified this design flaw and prevented the failure, saving the mission.

### 2. Provides Consistency Across Software Development

* Establishing software processes ensures that all projects at the Center develop, manage, verify, and validate software using consistent standards, methodologies, and approaches. This consistency reduces risks, improves communication among teams, and helps in project integration and handoffs.

**Why This Is Crucial**:

* Different projects require collaboration across teams and sometimes across NASA Centers. Having defined processes ensures uniformity, which improves efficiency and reduces misunderstandings.
* Standardized processes reduce variability and discrepancies between contractors and internal teams, enabling better integration of software systems.

### 3. Ensures Compliance with NASA’s Standards and Regulation

* Software development at NASA must comply with requirements established in the NASA Software Engineering Handbook (SWEHB) and other directives like **NPR 7150.2** [083](#_tabs-<p></p>). This requirement ensures that Centers document and implement processes in alignment with Agency standards.
* By adhering to established standards:
  + Software development becomes auditable, ensuring accountability.
  + Non-compliance risks are avoided, enhancing safety and reliability.

### 4. Improves Software Quality and Reduces Defects

* Documented and implemented software processes emphasize good practices such as requirements engineering, peer reviews, testing, and risk management. These processes minimize software defects throughout the software lifecycle and help catch issues before deployment, where fixes become more expensive and time-consuming.

**Key Insight**:

* A lack of disciplined software processes often leads to defects escaping into operations. Correcting these defects can multiply costs by 10x or more once the software is deployed.

**Examples of Poor Software Processes Leading to Failures**:

* **Mars Climate Orbiter (1999)**: Unit mismatch between metric and imperial measurements in software interfaces caused loss of the spacecraft.
* **Ariane 5 Flight 501 (1996)**: Software overflow error caused the destruction of the launch vehicle.

### 5. Ensures Safety-Critical Software Excellence

* Many of NASA’s missions involve safety-critical software, where errors could result in loss of life, property, or mission objectives. Robust processes ensure that safety-critical elements are prioritized, verified, and validated to rigorous standards.

**Why This Matters**:

* Proper software processes ensure that safety-critical components are identified early, analyzed for hazards, and subjected to stricter requirements, reviews, and testing protocols.
* This requirement protects human lives during manned space missions (e.g., Artemis) and ensures the reliability of robotic missions that depend solely on software for autonomous operations.

### 6. Facilitates Process Improvement and Lessons Learned

* Documenting and executing software processes fosters continuous improvement. By monitoring, reviewing, and maintaining the processes, Centers can integrate lessons learned from past projects into current and future processes.
* Centers can establish feedback loops to optimize efficiency, identify bottlenecks, and mitigate recurring risks.

**Example**:

* Past software-related anomalies, like interface failures or insufficient requirements, can be addressed and incorporated into processes to ensure such issues are avoided in subsequent projects.

### 7. Reduces Overall Cost and Schedule Overruns

* Disciplined software processes reduce unexpected deviations and risks during software development and maintenance, leading to fewer schedule delays and cost overruns. They help forecast resource requirements accurately, monitor progress effectively, and identify risks early before they escalate.

**Cost-Saving Examples**:

* Catching and fixing software defects during development is significantly cheaper and easier than after deployment or during operations.
* Establishing and maintaining repeatable processes ensures that work productivity can scale across projects without sacrificing quality.

### 8. Enhances Collaboration With Contractors

* NASA relies heavily on contractors for the development of software components. By defining and documenting software processes, Centers can set clear expectations for contractor responsibilities, workflows, and deliverables. This ensures that contractor work aligns with NASA’s standards and integrates seamlessly into Center-developed systems.

**Why It’s Key**:

* Effective contractor oversight depends on well-defined processes. Contractors can be held accountable for meeting contractual requirements, and the Center can identify non-compliance or performance risks early.

### 9. Enables Traceability and Accountability

* By documenting software processes, Centers create a transparent and traceable framework that ensures accountability at every stage of software development. This helps in performing audits, troubleshooting failures, and demonstrating compliance with NASA guidelines.

**Example in Practice**:

* Software traceability allows teams to map every requirement to its implementation, test, and validation, ensuring that no functionality is missed and that software performs as expected.

### 10. Facilitates Adaptability to Future Requirements

* Maintaining software processes ensures adaptability when new NASA requirements, mission goals, or technologies are introduced. By having an established and reviewed baseline, Centers can more easily evolve their processes to meet NASA’s long-term strategic goals.

**Why This Matters**:

* As NASA adopts advanced technologies like AI/ML, autonomous systems, or hybrid cloud computing, Centers with robust processes will adapt faster without compromising quality or safety.

## 2.2 Specific Benefits of the Requirement

1. **Accountability at the Center Level**:
   * The Center Director ensures there is leadership and accountability behind maintaining compliance with NASA standards.
2. **Clear Expectations for the Workforce**:
   * Documenting software processes provides clarity to developers, software assurance personnel, and testers on their roles.
3. **Alignment Across NASA Centers**:
   * Uniformity of software engineering practices across Centers enables more efficient collaboration on cross-Center projects.
4. **Confidence in Deliverables**:
   * Established and repeatable processes ensure high-quality deliverables from both in-house teams and external contractors.

## 2.3 Relevant NASA Lessons Learned Relevant to the Rationale

* **Mars Climate Orbiter** (LLIS Number: 0938): The failure due to inconsistent engineering practices underlines the importance of having robust, repeatable processes.
* **Aries I-X Development Challenges** (LLIS Number: 2121): Lack of process alignment led to inefficiencies during development; improved process discipline across Centers would help mitigate such challenges.
* **Software Process Improvement Results in Measurable Benefits** (LLIS Number: 1489): Emphasizes the long-term cost and quality benefits of institutionalized software processes.

## 2.4 Conclusion

This requirement is foundational for ensuring that NASA software projects achieve mission success while mitigating risks and reducing costs. By establishing, executing, documenting, and maintaining software processes:

* Centers can deliver reliable, safe, and mission-critical software.
* They can ensure that both in-house and contractor-developed systems meet the highest standards.
* They set a foundation for continuous improvement, ensuring adaptability to NASA’s evolving missions and technologies.

This requirement protects NASA’s reputation, resources, and, ultimately, the safety of its personnel and assets.

# 3. Guidance

This improved guidance offers clarity, practicality, and scalability while enhancing alignment with NASA's organizational goals. It reflects the need for structured, repeatable, and efficient software processes that ensure quality, minimize risks, and contribute to mission success.

## 3.1. Fundamental Guidance

All software development efforts within NASA must adhere to documented and defined software processes appropriate to the size, complexity, and criticality of the project. These processes:

* Provide consistency and ensure compliance with the requirements established in **NPR 7150.2 [083](#_tabs-<p></p>)**.
* Can be derived from software processes documented at the Agency, Center, or organizational levels.
* Must be tailored to suit both the needs of the project and the organizational objectives specified by the Center.

**Responsibilities:**

* Engineering management and/or the project lead software engineer are accountable for:
  + Developing adequate processes for their project needs.
  + Training personnel to understand and execute these documented processes effectively.
  + Maintaining and evolving the processes to reflect lessons learned, technology advancements, and project-specific requirements.
  + Ensuring strict adherence to the organization's defined software processes throughout the complete software development lifecycle.

## 3.2. Establishing and Maintaining Processes at NASA Centers

### 3.2.1 Use of Software Engineering Process Groups (SEPGs)

Most NASA Centers have established **Software Engineering Process Groups (SEPGs)** responsible for developing, maintaining, and managing the organization's software processes. SEPGs:

* **Role:**
  + Create a set of actionable, tailored processes that meet the needs of the software engineering teams.
  + Ensure processes are documented, stored, and updated in a centralized repository, such as a **Process Asset Library (PAL)**[197](#_tabs-<p></p>).
* **Process Asset Library (PAL):**
  + PALs provide a structured repository for process documentation, templates, standards, and best practices.
  + PALs are typically integrated with the Center’s overall business management system, ensuring software processes align seamlessly with organizational policies.

### 3.2.2 Standard Processes

Centers are encouraged to develop and implement standard processes that guide software development through all lifecycle phases while satisfying mandatory entrance and exit criteria for reviews, milestones, and lifecycle transitions. These processes:

* **Interpret NPR 7150.2 Requirements:**
  + Reflect application of **NPR 7150.2** by incorporating best practices for developing quality software and systems.
* **Customization and Scaling:**
  + Tailor processes based on the software classification and criticality (e.g., Class A, B, C, D, or E software).
  + Align with frameworks, such as the **Capability Maturity Model Integration (CMMI) [689](#_tabs-<p></p>)**, for Classes A, B, and C software. The extent of alignment can include external appraisal activities if needed.

## 3.3. Process Flexibility

While Centers are not mandated to have a singular process for software development, they are required to ensure:

* **Consistency:** Processes should be applied uniformly within an organization or project to maintain quality and reduce variability during development.
* **Compliance:** All processes, regardless of variations between organizational units, must meet the requirements of **NPR 7150.2**.

**Key Considerations for Centers Adopting Multiple Processes:**

1. Document and maintain clear records of each version of the process.
2. Ensure processes across different organizations are fully compliant with **NPR 7150.2**.
3. Coordinate and communicate variations effectively among teams to avoid misalignment or redundancy.

## 3.4. Process Evaluation Questions

Centers should regularly evaluate the effectiveness of their software processes. Managers and engineers are encouraged to ask:

1. **Existence:**
   * Does the right process or procedure exist for all phases of software development?
2. **Effectiveness:**
   * Is the process effective, and how is this effectiveness measured?
3. **Awareness:**
   * Do staff members understand the desired outcomes and purpose of the process?
4. **Ownership:**
   * Does everyone understand their role in executing the process? Are they held accountable?
5. **Evaluation:**
   * How and when is the process reviewed, updated, and assessed for improvement?
6. **Corrective Actions:**
   * What mechanisms exist to address ineffective or outdated processes?

## 3.5. Resources for Developing and Maintaining Software Processes

### 3.5.1 Recommended Frameworks and Standards

NASA Centers can rely on several established frameworks and standards as references when developing their software processes:

* **Capability Maturity Model Integration for Development (CMMI-Dev) [689](#_tabs-<p></p>):**
  + Describes best practices for software development, including processes for maximizing quality at each stage of the lifecycle.
  + Centers are encouraged to align their processes with CMMI when working on Class A, B, and C software.
  + See also [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software).
* **NPR 7123.1 [041](#_tabs-<p></p>)**:
  + Provides Agency-level technical processes required to define, develop, realize, and integrate the quality of NASA systems and software products.
  + Centers may supplement its framework or tailor processes while remaining compliant.
* **AS9100D - Quality Management Systems - Requirements for Aviation, Space, and Defense Organizations** **[372](#_tabs-<p></p>)**:
  + Offers a process-based approach for aerospace applications, emphasizing linkages and interactions between processes to improve quality control across interdependent phases.
* **IEEE STD 12207 [224](#_tabs-<p></p>)**:
  + Establishes a common framework for software lifecycle processes, defining activities and tasks applicable to the acquisition, development, operation, maintenance, and disposal of software products.

### 3.5.2 Continuous Improvement Practices

Centers should regularly update their processes to reflect:

* Lessons learned from NASA projects and other Agency missions.
* Advances in tools, technology, and methodologies (e.g., DevOps, Agile, automated testing).
* Feedback from teams and stakeholders who execute processes daily.

### 3.6. Additional Guidance on Application

#### 3.6.1 Class-Specific Software Development

For software projects classified as Class A, B, and C, Centers should:

* Align their processes with CMMI®-Dev to ensure quality and process transparency.
* Engage in periodic external appraisals to validate compliance and identify areas for improvement. For Class D and Class E software, Centers should:
* Apply tailored processes that incorporate only essential elements of CMMI, depending on the criticality of the software.

#### 3.6.2 Related Guidance and Resources

Centers should consult and leverage existing NASA resources in process development and improvement:

* [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination): Guidance for determining appropriate software processes for a given project.
* [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans): Guidance for developing comprehensive software development plans aligned with organizational standards.
* [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans): Guidance for creating improvement plans to align processes with NASA’s long-term strategic goals.
* [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software): Guidance for determining the required maturity level based on software classification.

## 3.7. Practical Implementation Steps

To fulfill this requirement, Centers should:

1. **Establish SEPGs and PALs:**
   * Ensure their SEPG is well-staffed and maintains actionable software processes that are accessible to all stakeholders.
2. **Define Standard Processes:**
   * Implement lifecycle-wide standard processes, ensuring lifecycle phase transitions (entrance and exit criteria) are clearly documented and understood.
3. **Promote Training and Accountability:**
   * Provide necessary training to engineers on software processes and their applicability.
   * Emphasize individual accountability for executing processes effectively.
4. **Monitor and Adapt Processes:**
   * Regularly review processes using feedback loops, metrics, and lessons learned.
   * Introduce corrections or adaptations based on project-specific or organizational needs.

## 3.8 Conclusion

This improved guidance provides practical, flexible, and scalable solutions for NASA Centers to document, execute, and maintain software processes effectively. By leveraging best practices, resources, and standards (e.g., CMMI, **NPR 7123.1**), Centers can ensure software development activities are consistent, compliant, and of the highest quality. Structured processes foster safety, reliability, and efficiency, enabling NASA to meet its mission-critical objectives across all projects.

## 3.9 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans) * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination)        * [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) |

## 3.10 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

Small projects often face constraints due to limited budgets, schedules, and staff but must still maintain adequate software processes to ensure quality, reliability, and compliance with NASA’s requirements. This guidance focuses on practical, lightweight approaches that small projects can take to satisfy this requirement without overburdening their resources.

## 4.1 Guidance for Small Projects

### 4.1.1  What This Requirement Means for Small Projects

Small projects need to:

1. **Establish:** Define a minimum set of software processes tailored to the project’s scale, scope, and classification. Focus on simplicity and practicality.
2. **Document:** Maintain a lightweight but complete set of documentation for processes that supports traceability and compliance with NASA requirements.
3. **Execute:** Ensure that these processes are consistently followed throughout the project lifecycle using the minimal resources available.
4. **Maintain:** Periodically assess, update, and refine these processes, as needed, to reflect lessons learned and improvements.

### 4.1.2  Small-Scale Approach by Lifecycle Phase

#### 4.1.2.1. Establishing Processes

To meet this component for a small project:

* + Start simple—focus on the core processes required to manage project risks, meet quality requirements, and comply with **NPR 7150.2**[083](#_tabs-<p></p>).
  + **Key Processes to Establish**:
    - Requirements definition and management process.
    - Configuration and version control.
    - Software verification and testing.
    - Issue tracking and defect management.
  + Use NASA-approved templates (e.g., from the Software Engineering Process Group (SEPG) or **Process Asset Library (PAL)**[197](#_tabs-<p></p>)) to avoid creating processes from scratch.

**Suggested Steps**:

* + Review similar, completed small projects at your Center to identify their processes and adapt as necessary.
  + Engage with the Center’s SEPG for pre-existing and tailored processes that can be applied to your project.
  + Define clear entry and exit criteria for major lifecycle transitions (e.g., requirements review, testing, and deployment milestones).

#### 4.1.2.2. Documenting Processes

For small projects, process documentation must be lightweight but sufficient to ensure consistency and compliance across project phases.

**Guidelines for Small Projects**:

* + Avoid complexity: Documentation should be actionable and easy to implement.
  + Practical options for documentation:
    - **A Process Checklist**: A simple checklist covering the key development phases (e.g., requirements, design, implementation, testing, and maintenance) can serve as documentation for your processes.
    - **A One-Page Development Plan**: Summarize the project's processes, roles, and responsibilities in a single document (e.g., how your team manages requirements, conducts reviews, and completes testing).
    - **Tool-Integrated Processes**: Use tools (e.g., issue trackers, version control software) to document processes implicitly (e.g., automated workflows in GitHub for software releases).

**Key Deliverables**:

* + A lightweight project software development plan that aligns with **NPR 7150.2**.
  + Minimal yet clear records of any tailoring of processes or justifications for exclusion of certain steps (as applicable to the classification of the software being developed).

#### 4.1.2.3. Executing and Implementing Processes

Execution in small projects often involves practical, focused implementation of processes throughout the software lifecycle.

**Tips for Effective Execution**:

* + **Keep it simple**: Implement only the processes necessary to manage risks and deliver the required functionality.
  + **Focus on high-risk areas**: Pay particular attention to areas that are safety-critical, mission-critical, or essential for meeting quality standards.
  + **Use tools to automate**: Leverage tools to support execution, such as:
    - Automated testing frameworks to simplify verification.
    - Issue tracking systems to monitor and close risks/bugs.
    - Version control tools (e.g., Git) to ensure rigorous configuration management.
  + **Assign clear responsibilities**: Ensure team roles (e.g., software developer, tester, reviewer) and their responsibilities within processes are well understood.

**Example Practices**:

* + When conducting small-scale code reviews, you can replace large committee reviews with lightweight peer reviews.
  + Instead of writing separate unit or integration test plans, embed testing activities into your sprint or build plan (if using Agile or iterative development).

#### 4.1.2.4. Maintaining Processes

Even for small projects, maintaining processes ensures they remain relevant, effective, and efficient.

**Practical Steps for Maintenance**:

* + Gather input from the team: Include regular discussions in team meetings to review how well processes are working.
  + Use lessons learned: Capture feedback after key milestones (e.g., design reviews, integration testing) and incorporate those lessons into future processes.
  + Simplify whenever possible: Periodically reassess if certain processes can be improved or streamlined based on team feedback.
  + Maintain a feedback loop with your SEPG (if applicable): Use their expertise for process refinement.

**Suggested Approach for Small Projects**:

* + Perform a lightweight process review at key life cycle milestones (e.g., at the end of the requirements phase and after final testing).
  + Make only incremental updates to processes for small projects unless significant inefficiencies or issues are found.

### 4.1.3  Other Key Considerations for Small Projects

1. **Tailoring Processes**:
   * Small projects often do not require the full range of processes used by large-scale or high-risk missions.
   * Focus on tailoring only the processes applicable to the software’s classification and criticality. For example:
     + Class D and E software may focus primarily on basic requirements management, unit testing, and version control.
     + Class C software requires more rigor but may still not need processes for external appraisals (e.g., against CMMI metrics).
2. **SEPG and PAL Alignment**:
   * Engage with the Center’s SEPG for pre-defined templates, workflows, or streamlined processes specific to small or moderate-sized projects.
   * Utilize the Process Asset Library (PAL) for immediate access to resources you can customize for your project.
3. **Training and Awareness**:
   * Provide a brief but focused introduction to team members on project-specific software processes.
   * Use periodic training sessions or Center-supplied resources like lessons learned databases to reinforce understanding.

### 4.1.4  Tool Recommendations for Small Projects

Small projects may not have the resources for large-scale process management systems. Instead, consider lightweight tools:

* **Version control**: Git, GitLab, GitHub.
* **Issue tracking and management**: Jira, Trello, or a simple spreadsheet.
* **Documentation tools**: Confluence, Google Docs, or Microsoft Word for lightweight documentation.
* **Testing automation**: Open-source tools like JUnit (for Java), Pytest (for Python), or Selenium (for web applications).

Use these tools to create a streamlined workflow where process adherence is integrated rather than treated as a separate activity.

### 4.1.5  Checklist for Small Projects

Below is a simple checklist to ensure compliance with this requirement:

1. **Establishing Processes**
   * Defined minimum processes required for software development (e.g., configuration management, testing, and defect tracking).
   * Tailored processes to match the classification and criticality of the software.
2. **Documenting Processes**
   * Developed a lightweight software plan or process checklist.
   * Specified roles, responsibilities, entry/exit criteria, and key deliverables.
3. **Executing Processes**
   * Processes are implemented consistently across the team.
   * Practical tools and automation are used to simplify process execution.
4. **Maintaining Processes**
   * Periodically reviewed process effectiveness.
   * Captured lessons learned and updated processes as needed.

### 4.1.6  Examples of Small Project Process Activities

1. **Developing a Research Data Analysis Tool**

   * Focus on lightweight processes: Requirements walkthrough, unit testing, and peer reviews.
   * Use Git for version control and a shared Trello board for risk/defect tracking.
2. **Delivering Prototype Software for a Science Experiment**

   * Tailor processes: Basic requirements validation, test-driven development, and configuration management.
   * Document processes in a one-page Software Development Plan.

## 4.2 Conclusion

Small projects should take a pragmatic and risk-based approach to defining, documenting, executing, and maintaining software processes. By focusing on simplicity, leveraging existing resources (e.g., SEPG and PAL), and prioritizing high-risk areas, small projects can achieve compliance with **NPR 7150.2** while staying within their resource constraints. A lightweight and adaptable process ensures small projects maintain software quality, meet delivery goals, and contribute successfully to NASA’s objectives.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-372)

  [Quality Management Systems - Requirements for Aviation, Space and Defense Organizations,](http://standards.sae.org/as9100d/ "Click to open in new window")

  SAE AS9100D, ", 2016. NASA users can access standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of standards.
* (SWEREF-572)

  [Flight Software Engineering Lessons](https://llis.nasa.gov/lesson/2218 "Click to open in new window")

  Public Lessons Learned Entry: 2218.
* (SWEREF-689)

  [CMMI Model - Overview](https://cmmiinstitute.com/dashboard "Click to open in new window")

  Capability Maturity Model Integration (CMMI) Model V3.0, ISACA, April 6, 2023,  NASA users can access the CMMI models with a CMMI Institute account at: https://cmmiinstitute.com/dashboard. Non-NASA users may purchase the document from: https://cmmiinstitute.com

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** is a rich source of experience-based knowledge, providing guidance on best practices, strategies, and improvements that have been derived from past projects. These lessons are crucial to establishing and maintaining effective software development processes at both program and project levels, allowing NASA to continually advance its system reliability and performance while mitigating risks.

### 6.1.1  Relevant NASA Lessons Learned

#### Flight Software Engineering Lessons – Lesson Number 2218 [572](#_tabs-<p></p>)

The NASA Software Engineering Improvement Initiative (NSEII) (see [SWE-002 - Software Engineering Initiative](https://swehb.nasa.gov/display/SWEHBVD/SWE-002+-+Software+Engineering+Initiative) and Topic [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](https://swehb.nasa.gov/display/SWEHBVD/7.01++-+History+and+Overview+of+the+Software+Process+Improvement+%28SPI%29+Effort)), provides an insightful example of how software process improvements can significantly reduce risks and ensure the success of mission-critical software systems. Specifically, the Jet Propulsion Laboratory (JPL) reviewed its software engineering processes and identified several key strategies to address risks related to flight software (FSW) development. The lessons learned are outlined below, with actionable improvements added to enhance their clarity and applicability.

#### 6.1.1.1  Key Lessons and Practices from the Flight Software Process:

1. **Adopt a Risk-Based Approach to Software Engineering**
   * **Guidance**:
     + Focus resources on the riskiest components of the software lifecycle by assessing the software’s safety-criticality, mission-criticality, and complexity.
     + Prioritize testing and verification efforts for high-risk areas.
   * **Actionable Tip**:
     + Implement a lightweight risk management plan that continuously identifies, evaluates, and mitigates software risks throughout the lifecycle.
     + Use Failure Modes and Effects Analysis (FMEA) or Hazard Analysis tools to target risk-driven work on software components.
2. **Engage Software Engineers During Early Project Decisions**
   * **Guidance**:
     + Involve software engineers in early system-level decision-making to ensure that the characteristics and architecture of the flight system align with software capabilities and constraints.
   * **Why This Matters**:
     + Early involvement ensures software-related constraints (e.g., real-time requirements, performance needs, secure communication protocols) are addressed in the conceptual phase.
   * **Actionable Tip**:
     + Assign a software lead engineer to participate in system design trade studies, Integrated Product Teams (IPTs), and high-level architecture design reviews.
     + Create an interface control document (ICD) during the system conceptualization to capture critical system/software interactions.
3. **Provide Essential Development Infrastructure Prior to Project Commencement**
   * **Guidance**:
     + Establish the foundational infrastructure (e.g., development environments, version controls, testing frameworks) before the project starts.
   * **Why This Matters**:
     + Lack of proper infrastructure early in the lifecycle can lead to delays, inefficient workflows, and defects being introduced due to ad-hoc setups.
   * **Actionable Tip**:
     + Standardize tools and repositories across projects (e.g., Center-specific DevOps pipelines).
     + Conduct a setup readiness review for software infrastructure before the development cycle begins.
4. **Develop Simulations and Emulators Early**
   * **Guidance**:
     + Create simulations of instruments, subsystems, or other hardware that interact with flight software as soon as their operational characteristics are understood.
   * **Why This Matters**:
     + Early simulations allow for flight software tests to begin sooner, mitigate integration risks, and uncover hardware-software compatibility problems earlier in the lifecycle.
   * **Actionable Tip**:
     + Use emulators to test hardware-software integration in parallel with hardware assembly to avoid "big-bang" system integration.
     + Gradually refine simulations as instrument and hardware specifications evolve.
5. **Prepare a Flight Software (FSW) Architecture Specification Before Coding**
   * **Guidance**:
     + Define the FSW architecture clearly before implementation begins to align development with high-level system goals.
   * **Why This Matters**:
     + A strong architecture reduces redesigns and ensures flexibility for handling requirements changes.
   * **Actionable Tip**:
     + Include key elements such as modularization, interface definitions, hardware coupling, and data flow diagrams in the architecture specification.
     + Conduct peer reviews to vet the architecture document.
6. **Define Reusable Flight System Architectures**
   * **Guidance**:
     + Develop and maintain a suite of reusable flight software and subsystem architectures that support common mission types undertaken by the Center.
   * **Why This Matters**:
     + Standardized reusable architectures speed up development timelines and reduce design variability.
   * **Actionable Tip**:
     + Develop core libraries and templates that can serve classes of missions (e.g., Earth observation, interplanetary probes).
     + Invest in modular designs that allow plug-and-play capabilities for different hardware and mission objectives.
7. **Implement a Robust Systems Engineering Process**
   * **Guidance**:
     + Use systems engineering practices to define, trace, review, and assess requirements across the lifecycle.
   * **Essential Practices**:
     + Clearly trace requirements from higher levels (system-level) to lower levels (software module-level).
     + Review requirements with key stakeholders and with individuals independent of the development to reveal blind spots.
     + Use checklists to assess the clarity, feasibility, and completeness of requirements.
   * **Actionable Tip**:
     + Incorporate digital tools such as DOORS or Jama Connect for requirement traceability, linking stages from inception to verification.
8. **Use Objective Measures to Monitor Progress and Verification**
   * **Guidance**:
     + Employ objective metrics to gauge software development progress and verification adequacy.
   * **Why This Matters**:
     + Metrics provide a data-driven way to assess the health of the software effort and identify risks or deficiencies early.
   * **Actionable Metrics**:
     + Requirements coverage.
     + Defect density.
     + Code churn (frequency and size of codebase changes).
     + Test coverage and defect discovery rates.
   * **Actionable Tip**:
     + Establish a dashboard to monitor progress using automation tools (e.g., Jenkins, Gitlab CI/CD) that generate on-demand metrics.
9. **Manage Development Using an Integrated System**
   * **Guidance**:
     + Manage FSW development within an integrated ecosystem of tools, teams, and workflows where all artifacts (e.g., requirements, tests, codes) are linked and accessible.
   * **Why This Matters**:
     + Integrated systems streamline communication, reduce silos, and improve transparency.
   * **Actionable Tip**:
     + Consolidate platforms for development, issue tracking, configuration management, and testing into a cohesive package (e.g., use Atlassian’s Jira, Bitbucket, and Confluence in tandem).

#### 6.1.1.2  Additional Takeaways from Lesson 2218

1. **Lessons Applicable to Small Projects**:

   * Small projects can replicate these lessons in a scaled-down manner by prioritizing high-risk areas, leveraging reusable components, and employing lightweight simulations.
2. **Center-Level Guidance**:

   * Steps like early FSW architecture specification, simulations, and early engagement of software engineers can be driven by Center-wide policies even for small-medium-sized teams.

### 6.1.2  Related Lessons and Guidance

The following NASA lessons also align with and supplement Lesson 2218:

* **Mars Climate Orbiter Lessons** (LLIS 0938):
  + Emphasizes the critical importance of avoiding ambiguous or poorly validated requirements.
* **Software Deficiencies in Mars Polar Lander** (LLIS 1778):
  + Highlights the necessity of early FSW testing with simulated mission environments.
* **Software Process Improvement** (LLIS 1489):
  + Describes measurable benefits of adopting a well-defined software improvement process at every project size.

### 6.1.3  Conclusion

The lessons learned captured by Lesson 2218 highlight the importance of following disciplined, risk-based, and architecture-driven approaches to flight software development. By integrating systems thinking, robust simulations, and objective metrics, NASA Centers can ensure that their processes are aligned with achieving high-quality outcomes and reducing developmental defects and risks. These principles—aided by modern tools, continuous process improvement, and a commitment to early systems engineering—form the cornerstone of consistent, repeatable success in software engineering, which is vital for all projects, from small scientific missions to flagship programs.

### 6.2 Other Lessons Learned

* No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-205 - Determination of Safety-Critical Software**

3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each software component is considered to be safety-critical per the criteria defined in NASA-STD-8739.8.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

None identified at this time.

## 7.2 Software Assurance Products

Software Assurance (SA) products are tangible outputs created by Software Assurance personnel to support oversight, validate compliance, manage risks, and ensure the quality of delivered products. These products are essential to demonstrate that SA objectives are being met, and they serve as evidence of the thoroughness and effectiveness of the assurance activities performed.

No specific deliverables are currently identified.

## 7.3 Metrics

No standard metrics are currently specified.

## 7.4 Guidance

### 7.4.1  Objective of the Guidance

The goal of this requirement is to ensure that NASA Centers establish, document, and implement standardized software processes that comply with the requirements outlined in NASA directives (such as **NPR 7150.2** [083](#_tabs-<p></p>) and related standards, including **NASA-STD-8739.8 [278](#_tabs-<p></p>)**). These processes must be robust, effective, and consistently maintained to ensure high software quality, compliance, and reliability for NASA missions.

Software Assurance (SA) personnel play a critical role in supporting Centers to fulfill this requirement through the evaluation, monitoring, and improvement of software processes.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Support the Establishment of Software Processes

1. **Evaluate Compliance Requirements**
   * Understand the applicable requirements outlined in **NPR 7150.2**, **NASA-STD-8739.8**, and any related directives.
   * Identify the specific software classification levels (A, B, C, etc.) and criticality considerations that apply to each software process.
2. **Collaborate on Process Design**
   * Work with the Center Director’s designee and engineering teams to ensure software assurance activities are integrated into the designed processes. This includes:
     + Verification and validation (V&V) activities.
     + Risk analysis and safety considerations for safety-critical software.
     + Metrics collection and defect tracking.
3. **Include Software Assurance Requirements**
   * Ensure that software assurance processes are explicitly documented as part of the overarching software processes. These may include:
     + Peer reviews and inspections.
     + Software test planning and execution.
     + Tracking and mitigation of risks related to quality and safety-critical operations.

#### 7.4.2.2. Support Documentation of Software Processes

1. **Assist in Process Documentation**
   * Collaborate with engineering and project teams to create clear and comprehensive process documentation, ensuring it includes:
     + Standard operating procedures (SOPs) for software development and assurance activities.
     + Metrics and quality benchmarks for compliance.
     + Tailoring guidance for specific requirements, where applicable.
2. **Document Assurance Activities**
   * Ensure all assurance-related tasks, tools, and methods are included in the process documentation, providing traceability to requirements in **NPR 7150.2** and **NASA-STD-8739.8**.
3. **Align Documentation with Standards**
   * Verify that process documentation aligns with NASA policies, standards, and directives to ensure compliance.

#### 7.4.2.3  Monitor Process Execution

1. **Perform Implementation Reviews**
   * Periodically review the execution of established software processes to ensure they are followed correctly.
   * Confirm that assurance activities such as testing, verification, validation, and defect tracking are appropriately implemented.
2. **Verify Compliance**
   * Ensure executed processes comply with all applicable NASA directives, including tailoring requirements and safety-critical software considerations.
3. **Collect Evidence**
   * Gather evidence such as process artifacts, test results, peer review records, and software assurance metrics to confirm that processes are executed as documented.

#### 7.4.2.4  Maintain and Continuously Improve Software Processes

1. **Monitor Process Effectiveness**
   * Use metrics, process audits, and lessons learned to identify strengths and weaknesses in the software processes.
   * Confirm that assurance activities are achieving their intended impact on software reliability, safety, and mission success.
2. **Recommend Adjustments**
   * Collaborate with the Center designee to recommend process improvements based on:
     + Evolving project needs.
     + Changes in applicable NASA standards.
     + Emerging technologies (e.g., tools for automated testing, model-based engineering, or DevSecOps).
3. **Support Updates**
   * Ensure process documentation is updated when improvements are implemented to reflect changes and maintain compliance.

#### 7.4.2.5  Engage in Training and Communication

1. **Educate Teams**
   * Provide training to relevant personnel (engineers, assurance staff, project managers) to ensure all stakeholders understand the established software processes and their role in executing them.
2. **Promote Communication**
   * Foster clear communication between software assurance teams, engineering teams, and Center leadership regarding software process status, issues, and improvements.

### 7.4.3  Key Focus Areas for Software Assurance

To effectively support this requirement, SA personnel should prioritize the following:

1. **Integration of Assurance Activities**
   * Ensure verification, validation, and safety assessments are built into all stages of the software lifecycle.
2. **Metrics and Accountability**
   * Establish clear metrics for software assurance (e.g., defect tracking, test coverage) and ensure these are regularly collected and reviewed.
3. **Tailoring Guidance**
   * Verify that documented software processes include proper procedures for tailoring and handling deviations from requirements.
4. **Risk Management**
   * Support the tracking and mitigation of risks related to software quality and safety-critical systems.
5. **Compliance**
   * Regularly assess processes for adherence to **NPR 7150.2** and related directives.

### 7.4.4  Expected Outcomes

By supporting this requirement:

1. **Processes Are Compliant**
   * Centers establish and maintain software processes that adhere to NASA’s policies and directives.
2. **Assurance Activities Are Effective**
   * Software assurance tasks are fully integrated into documented processes and executed rigorously.
3. **Continuous Improvement**
   * Processes evolve to reflect best practices, lessons learned, and technological advancements, improving quality and reducing risks.
4. **Mission Success**
   * Standardized, high-quality software processes contribute to increased reliability and safety, supporting overall mission objectives.

### 7.4.5  Summary

Software Assurance personnel must actively support the Center Director’s designee in establishing, documenting, executing, and maintaining software processes. This requires ensuring compliance with NASA policies, integrating comprehensive assurance activities into processes, monitoring implementation, and driving continuous improvement. Through these efforts, SA personnel help ensure that NASA’s software engineering practices consistently achieve high standards of quality, safety, and mission success.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-002 - Software Engineering Initiative](/spaces/SWEHBVD/pages/102695392/SWE-002+-+Software+Engineering+Initiative) * [SWE-003 - Center Improvement Plans](/spaces/SWEHBVD/pages/102695393/SWE-003+-+Center+Improvement+Plans) * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination)        * [7.01 - History and Overview of the Software Process Improvement (SPI) Effort](/spaces/SWEHBVD/pages/102695611/7.01+-+History+and+Overview+of+the+Software+Process+Improvement+SPI+Effort) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) |
