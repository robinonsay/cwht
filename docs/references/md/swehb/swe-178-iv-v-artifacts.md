# SWE-178 - IV V Artifacts

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695518. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts

SWE-178 - IV&V Artifacts

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695518/SWE-178+-+IV+V+Artifacts#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695518)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695518&showCommentArea=true&showComments=true#addcomment)

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

3.6.4 If software IV&V is performed on a project, the project manager shall ensure that IV&V is provided access to development artifacts, products, source code, and data required to perform the IV&V analysis efficiently and effectively. 

## 1.1 Notes

The artifacts and products should be provided electronically in original format (i.e., non-pdf) and, where possible, direct read-only electronic access to project document repositories and data stores should be provided. Appropriate security products should be completed and transferred as part of the overall package.

## 1.2 History

Click here to view the history of this requirement: SWE-178 History

SWE-178 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 3.6.4 If software IV&V is performed on a project, the project manager shall ensure that IV&V is provided access to development artifacts, products, source code, and data required to perform the IV&V analysis efficiently and effectively. |
| Difference between C and D | No change. |
| D | 3.6.4 If software IV&V is performed on a project, the project manager shall ensure that IV&V is provided access to development artifacts, products, source code, and data required to perform the IV&V analysis efficiently and effectively. |

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

Independent Verification and Validation (IV&V) plays a critical role in identifying and mitigating software-related risks to ensure mission success, safety, and reliability. The ability of the IV&V team to efficiently and effectively carry out analysis depends on timely and comprehensive access to the necessary development artifacts, products, source code, and data. This requirement ensures that the project manager facilitates such access, enabling the IV&V team to fulfill its purpose as an objective assessor of software and system quality.

This requirement ensures the IV&V team has unrestricted access to all development artifacts, products, source code, and data needed to fulfill its responsibilities. Such access enables the IV&V team to:

* Conduct efficient and accurate analysis.
* Detect defects early in the software development lifecycle.
* Provide independent, evidence-based assurance regarding software quality, safety, and security.

This access is vital for enabling robust software assurance practices, achieving compliance with NASA standards, and supporting mission success by reducing software risks. By ensuring timely access to artifacts, the project manager enhances the effectiveness of IV&V and helps safeguard against costly software errors and mission-critical failures.

## 2.1 Enables Comprehensive Risk Assessment and Mitigation:

* IV&V relies on rigorous analysis of development artifacts (e.g., requirements documents, design specifications, testing plans) to uncover defects, inconsistencies, or gaps that could lead to software failure.
* Without access to critical elements like source code or test results, the IV&V team cannot perform meaningful analysis, which jeopardizes the identification and mitigation of high-risk areas—especially for safety-critical and mission-critical software.

## 2.2 Supports Objective and Independent Assessments:

* IV&V operates independently as a safeguard against potential blind spots in the development process. Proper access to all relevant artifacts ensures the IV&V team can verify and validate the accuracy, completeness, and consistency of the products being created without undue reliance on developer-provided summaries or interpretations.
* Lack of access could compromise technical independence, as the IV&V team would lack the data needed to form independent conclusions.

## 2.3 Ensures Timeliness and Effectiveness of IV&V Activities:

* Delays or restrictions in accessing development artifacts can impede IV&V activities, causing bottlenecks that affect the alignment of IV&V findings with project milestones.
* Completeness and timeliness in providing data ensure that IV&V feedback is delivered during critical development phases, enabling early identification of defects and reducing the cost of late-stage corrections.

## 2.4 Improves Traceability and Coverage of Software Assurance:

* IV&V requires a full picture of the development lifecycle to ensure that all software behaviors (nominal and off-nominal) and requirements are verified and validated.
* Comprehensive access to artifacts, including subsystem designs, test reports, and source code, ensures that the IV&V team can build traceability matrices and identify any gaps that could lead to system failures.

## 2.5 Mitigates Risks Associated with Miscommunication or Missing Context:

* Development artifacts often contain the detailed context and rationale that underpins design and implementation decisions. Without access to these artifacts, the IV&V team risks making incomplete assessments based on partial or out-of-context information.
* Access to source code, interface descriptions, and testing outcomes ensures that assumptions used during analysis align with the actual system under development.

## 2.6 Enables Evaluation of Compliance with Standards and Security:

* NASA software is developed to rigorous standards, including safety-critical and mission-critical software requirements. Providing access to development artifacts ensures that the IV&V team can verify compliance with **NPR 7150.2** (Software Engineering Requirements) and NASA-STD-8739.8 requirements.
* Access to the source code is particularly important for security assessments, facilitating the identification of vulnerabilities like buffer overflows, insecure coding practices, or unmet safety/security requirements.

## 2.7 Supports the Discovery of Emergent Risks:

* Software systems are complex, and risks can emerge late in the development lifecycle due to interactions between components or unexpressed constraints. The IV&V team’s ability to analyze the full range of artifacts helps uncover these emergent risks and reduces the likelihood of post-deployment issues.

## 2.8 Fosters Collaboration Without Hampering Independence:

* While IV&V is independent, collaboration and data-sharing with the project team are essential. Ensuring that the IV&V team has easy access to required data streamlines communication and avoids unnecessary delays.
* Facilitating access demonstrates the project’s commitment to transparency and risk reduction, reinforcing a positive working relationship between IV&V and development teams.

# 3. Guidance

Implementing these guidance principles helps ensure that IV&V contributions to NASA projects are efficient, robust, and meaningful. By facilitating access to critical artifacts, integrating IV&V into risk management strategies, and leveraging the communication and operational structure provided by the IPEP, projects can maximize the value added by IV&V. These measures ultimately help reduce risk, improve quality, and increase the likelihood of mission success.

## 3.1 IV&V Artifact Availability

To ensure that Independent Verification and Validation (IV&V) processes are efficient, comprehensive, and cost-effective, it is critical to make all necessary artifacts, products, source code, and data accessible to the IV&V team in electronic format. This includes access to **original, non-pdf formats** whenever possible, as these retain editable properties and metadata that are key for analysis. Additionally, **read-only access** to project document repositories and data stores should be provided wherever feasible to enable streamlined, real-time access to up-to-date project information.

#### **Key Benefits of Artifact Availability:**

1. **Facilitates Post-Delivery Updates and Maintenance**:  
   Electronic availability ensures that IV&V teams can continue performing analysis following software updates or changes to project artifacts, especially during post-delivery phases where maintenance and upgrades are inevitable.
2. **Reduces Project Costs and Time Delays**:  
   Accessible electronic artifacts eliminate unnecessary delays related to recurring manual submissions and updates while avoiding costs from redundant data delivery processes.
3. **Supports Long-Term IV&V Activities**:  
   The ongoing availability of artifacts enables the IV&V team to assist with long-term software maintenance and risk analysis, critical for mission sustainment.

#### **Best Practices for Artifact Sharing:**

* **Electronic Repositories**: Use centralized, secure repositories (e.g., configuration management tools) to store and share artifacts. This allows the IV&V team real-time access to the latest version of deliverables.
* **Collaboration Tools**: Facilitate communication through integrated tools for accessing artifacts and ensuring transparency in artifact revisions.
* **System Access**: Grant IV&V teams access to project systems and personnel, enabling a deeper understanding of operational and non-functional aspects of the software.

#### **References**:

* Refer to [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) for additional requirements on artifact accessibility.

## 3.2 IV&V Risk Mitigation Strategy

IV&V is an integral element of NASA's **Software Assurance Risk Mitigation Strategy**, offering an objective, independent examination of the processes, products, and risks associated with safety- and mission-critical software.

1. **Role of IV&V in Risk Mitigation**:  
   IV&V rigorously evaluates whether:

   * The system’s software will function as intended under nominal conditions.
   * The software will **not exhibit unintended behaviors** that could compromise safety or mission objectives.
   * The software will respond as required under **adverse conditions**, such as faults or hazardous scenarios.
2. **Key Principles of Independence**:  
   IV&V independence is characterized by three parameters:

   * **Technical Independence**: The IV&V team is not involved in software development, maintaining an impartial perspective.
   * **Managerial Independence**: The IV&V team operates outside the development or program management hierarchy, enabling unbiased reporting.
   * **Financial Independence**: IV&V budgets are independent of the development organization, ensuring there are no undue financial constraints or influence on IV&V scope.

#### **Questions Addressed by IV&V**:

IV&V analysis is structured to answer these critical assurance questions:

1. **Functionality**: Does the software do what it is supposed to do?
2. **Boundary Behavior**: Does the software avoid performing unintended actions?
3. **Error Resilience**: Can the software handle off-nominal conditions and faults appropriately?

#### **References**:

* Refer to [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks) for further details on how IV&V supports risk management.

## 3.3 Additional Value Added by IV&V

Beyond identifying and mitigating risks, IV&V delivers added benefits to NASA projects:

#### **Key Benefits:**

1. **Improves Product Quality**:  
   By identifying high-risk areas, defects, and design flaws early in the lifecycle, IV&V significantly enhances software reliability, safety, and performance.
2. **Provides Greater Insight**:  
   IV&V offers detailed, independent analysis that uncovers issues often missed by development teams due to competing priorities or familiarity with the system.
3. **Leads to Cost Reduction**:  
   Early defect detection and mitigation reduce the cost of rework and minimize the risk of expensive post-delivery corrections or mission failures.
4. **Facilitates Knowledge Transfer**:  
   IV&V fosters the dissemination of **system and software engineering best practices**, enhancing the overall technical capabilities of teams.
5. **Supports Decision-Making**:  
   IV&V status reports provide decision-makers (e.g., program managers) with unbiased assessments of project health, risks, and progress, offering an additional layer of **assurance visibility**.

#### **Operational Scope**:

The scope of IV&V services is defined in the **IV&V Project Execution Plan (IPEP)**, which:

* Outlines planned IV&V efforts.
* Reflects project risk priorities.
* Is approved by the NASA IV&V Program.

## 3.4 IPEP - IV&V Project Execution Plan

The **IV&V Project Execution Plan (IPEP)** serves as the foundational document for coordinating and implementing IV&V activities. It is a dual-purpose tool that ensures alignment between the IV&V Provider and the project team.

#### **Primary Objectives of the IPEP**:

1. **Facilitating Communication and Coordination**:  
   The IPEP defines clear interaction paths between the IV&V team and the project, including:

   * Roles and responsibilities.
   * Interfaces for communication.
   * Deliverables and reporting methods.
2. **Documenting Operational Plans**:  
   As a living document, the IPEP provides detailed instructions and plans for IV&V activities, including:

   * **IV&V Scope**: Activities, coverage, and prioritization determined by risk and resource availability.
   * **Artifacts to Be Shared**: Specific project documents, source code, and test data needed for IV&V assessments.
   * **Technical Products**: Key IV&V deliverables, such as risk analyses and defect reports.
   * **Milestones**: Schedules aligned with project technical and programmatic milestones.
3. **Serving as an Agreement Framework**:  
   The IPEP formalizes roles, responsibilities, and expectations between the IV&V team and the project. It ensures transparency and accountability, minimizing misunderstandings and aligning both parties on shared goals.

#### **IPEP Development and Maintenance**:

* The IPEP is created by the **IV&V Provider** and reviewed with the project team to ensure alignment with both IV&V requirements (per **NASA-STD-8739.8**) and project needs.
* Updates to the IPEP are required when significant changes occur, such as scope redefinition, milestone adjustments, or resource constraints.

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks)        * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Software Quality Assurance](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Software+Quality+Assurance) |

# 4. Small Projects

For small projects, meeting this requirement may involve unique challenges due to resource limitations, fewer personnel, or less formalized processes. However, ensuring that the Independent Verification and Validation (IV&V) team has comprehensive, timely access to the necessary materials is critical for effective IV&V execution. For small projects, access management should be **streamlined, well-coordinated, and deliberate**, focusing on enabling IV&V to perform its mandated tasks without introducing unnecessary overhead.

This guidance provides a simplified and efficient strategy for fulfilling this requirement while ensuring that small projects remain compliant and IV&V activities are effective.

Small projects typically operate within limited constraints compared to larger missions. To ensure compliance with this requirement, the focus should be on:

1. **Establishing an Access Plan Early:** Define the process for granting IV&V access to artifacts, tools, and environments early in the project timeline to minimize disruptions during project execution.
2. **Tailoring Access to Project Risks and Needs:** Prioritize access to artifacts related to mission-critical, safety-critical, or high-risk software components.
3. **Streamlining Processes and Communication Channels:** Minimize delays in granting access by clearly defining roles, responsibilities, and procedures early in the project lifecycle.
4. **Ensuring Security and Intellectual Property Protections:** Establish streamlined agreements that safeguard sensitive project information while ensuring IV&V can function effectively.

## 4.1. Identify, Document, and Plan for Artifacts Needed by IV&V

On small projects, identifying the specific development artifacts and other resources required for IV&V ensures efficient execution.

* **Action:** Conduct an **artifact access planning session** with the IV&V team during the formation of the IV&V Project Execution Plan (IPEP). During this meeting:

  + Define the **list of required artifacts** essential for IV&V.
  + Specify development stages when access is required.
  + Plan for **prioritized access** to mission-critical and safety-critical artifacts (e.g., requirements documents, test plans, designs, and source code).
* **Example Artifacts:**

  + Requirements specifications (including safety-critical requirements).
  + Design documents (high-level design, detailed design, interface design specifications).
  + Source code for all mission-critical/safety-critical modules.
  + Test artifacts (test plans, test procedures, coverage analysis).
  + Risk assessment data identifying critical risks.
  + Verification/validation results, logs, and defect reports.
  + Data used in operational environments (e.g., test inputs, user workflows).
* **Document the Plan:** Include these details in the IPEP and the project communication plan to ensure transparency and alignment about what IV&V needs at each stage.

## 4.2. Coordinate IV&V Access Roles and Responsibilities

For small projects, roles around coordination, security, and technical access may be handled by limited personnel, so creating a clear process for granting access is essential.

* **Define the Collaboration Model:**

  + Identify a **single point of contact (POC)** from the development team to coordinate with the IV&V team on granting access to artifacts.
  + Designate a **data access or configuration POC** to manage source code repositories and version-controlled system artifacts.
  + Assign **IV&V liaisons** from the software team to oversee artifact requests and address any issues that arise.
* **Develop an Access Process:**

  + Define how IV&V will request, receive, and validate access to the needed items.
  + Specify timelines for fulfilling these requests. For example:
    - Artifacts from initial project phases (e.g., requirements, designs) are provided as soon as those packages are baselined.
    - Code and test evidence are provided incrementally as development progresses.

## 4.3. Provide Secure Access to Development Artifacts

Small projects often utilize shared development environments or external tools, making security and access control crucial to maintaining integrity and protecting sensitive information.

* **Establish Repository Access:**

  + If using version control tools (e.g., Git, Bitbucket, Subversion), provide IV&V with **read-only access** to the repositories containing source code, configuration files, and version histories.
  + Ensure IV&V has access to the **correct branches** (e.g., baselined code or working code).
* **Centralized Artifact Repository:**

  + Provide a centralized repository (e.g., SharePoint, Confluence, JIRA, or similar tools) for IV&V to access all non-code-related artifacts, including:
    - Requirements documents.
    - Test plans and evidence.
    - Design records.
  + Allow the IV&V team to download, review, and annotate artifacts within this secured environment.
* **Secure Data Sharing:** If sensitive data must be shared:

  + Use encrypted file transfers, access tokens, or secure file-sharing platforms.
  + Set up data partitioning or limited visibility for certain sensitive data or IP-protected artifacts.
* **Access Logging:** Log all access to critical development artifacts to ensure proper tracking and accountability, especially for small teams where roles may overlap.

## 4.4. Mitigate Delays by Implementing Automated/Real-Time Access Where Possible

Small projects can benefit from automation or self-service access mechanisms to prevent IV&V delays.

* **Automate Artifact Delivery:**

  + Use **Continuous Integration/Continuous Delivery (CI/CD) pipelines** to automate providing IV&V with updated software artifacts, test results, and defect reports after each build or release.
  + Notify the IV&V team automatically when new deliveries are prepared, ensuring prompt access.
* **Real-Time Dashboarding:**

  + Set up collaborative tools for real-time tracking of project progress. For example:
    - IV&V can monitor defect or test case status in JIRA or TestRail.
    - IV&V can review code iterations in real time using GitHub/GitLab.

## 4.5. Track and Monitor Access for Effectiveness

Small projects must ensure that artifact access is not only granted but also productive for IV&V.

* **Track Progress:**

  + Use an artifact tracking log to confirm when artifacts were requested, delivered, and reviewed by IV&V.
  + Regularly update this log and discuss concerns during project/IV&V coordination meetings.
* **Conduct Periodic Reviews:**

  + Hold weekly or bi-weekly meetings with the IV&V team to ensure access needs are being met on time.
  + Regularly review the effectiveness of artifact access and adjust the process as necessary.
* **Feedback Collection:**

  + Collect feedback from the IV&V team: Were access provisions timely and sufficient? Which artifacts were most useful or critical?

## 4.6. Lessons Learned for Future Small Projects

Document lessons learned to improve access management processes for future small projects:

* Identify bottlenecks that occurred due to artifact access delays and how they were mitigated.
* Record which tools and processes were most effective for managing access, especially for small project teams.

## 4.7 Summary of Small Project Guidance

| **Step** | **Action** |
| --- | --- |
| **Plan Artifact Needs** | Define and document the artifacts required by IV&V (e.g., requirements, source code, test results). |
| **Assign Roles** | Assign a dedicated POC for access coordination and technical repository management. |
| **Grant and Secure Access** | Provide timely, secure access to repositories, artifacts, and tools required by IV&V. |
| **Automate Delivery** | Use CI/CD pipelines and real-time dashboards for automated artifact delivery and visibility. |
| **Monitor and Feedback** | Track artifact access requests and collect feedback to ensure IV&V needs are met efficiently. |
| **Document Lessons Learned** | Capture lessons learned to refine access processes on future small projects. |

By implementing these steps, small projects can meet Requirement 3.6.4 while enabling IV&V to operate efficiently and effectively, ultimately contributing to higher-quality software and mission success.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-028)

  [IV&V Project Execution Plan (IPEP) Template,](https://swehb.nasa.gov/download/attachments/16450397/t2103_-_ver_f.pdf?api=v2 "Click to open in new window")

  T2103, NASA Independent Verification and Validation Program, 2011.
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

The **NASA Lessons Learned database** contains valuable insights from previous projects that highlight the importance of timely and effective access to development artifacts for IV&V activities. Below are relevant lessons learned that emphasize the criticality of granting IV&V teams full access to ensure software quality, reduce risks, and improve overall system reliability.

---

### **Lesson No. 708: Incomplete Access to Development Data Impacts IV&V Effectiveness**

**Context:**  
In a high-profile NASA mission, the IV&V team experienced significant challenges due to limited or delayed access to critical design and test artifacts. This limitation resulted in missed deadlines for identifying software defects and inaccuracies, leading to a compressed timeline for resolving issues.

**Key Insights:**

* **Direct Impact on Software Quality:** Restricted or untimely access to source code and design documents prevented IV&V from performing in-depth analysis, increasing the risk of undetected design flaws.
* **Reactive vs. Proactive Identification:** When artifact access is delayed, IV&V becomes more reactive and less effective at identifying critical software defects early in the lifecycle, where fixes are less costly and time-consuming.

**Relevance to Requirement 3.6.4:**  
This lesson demonstrates the criticality of providing **timely and complete access** to all development artifacts as described in NASA-STD-8739.8. Ensuring real-time or automated access alleviates delays and allows IV&V to efficiently identify and address risks, reducing technical debt.

---

### **Lesson No. 3436: Early Involvement of IV&V Reduces Risk to Software Success**

**Context:**  
During the development of a flight software system, IV&V was engaged later in the development lifecycle, which limited its ability to provide meaningful intervention. This issue was compounded by the lack of direct access to artifacts (requirements, test data, and early design iterations) until system integration and testing had already commenced.

**Key Insights:**

* **Early Access = Early Risk Mitigation:** The earlier IV&V has access to requirements, test cases, and source code, the better positioned it is to uncover gaps, ambiguities, or omissions that could escalate during later project phases.
* **Access Affects Cost and Schedule:** Without proper access to key documents during requirements development or the design phase, software risks were identified too late, resulting in costly re-designs and implementation delays.

**Relevance to Requirement 3.6.4:**  
To efficiently execute their responsibilities, IV&V must not only be involved in the early phases of software development but also access relevant artifacts as soon as they are baselined. Failing to provide early and consistent access undermines the cost and schedule advantages of IV&V involvement.

---

### **Lesson No. 1712: Oversights in Security Delayed IV&V Access to Mission Data**

**Context:**  
In a mission-critical ground control software system, IV&V was denied timely access to operational test data due to oversight in the configuration of security credentials. This resulted in unnecessary delays and incomplete test coverage for critical software components.

**Key Insights:**

* **Proactive Planning for Access Permissions:** Lack of forethought in managing access credentials delayed IV&V progress and caused schedule risks for the operational readiness reviews.
* **Automated Access Solutions:** Security protocols should strike a balance between protecting sensitive data and ensuring IV&V has automated or streamlined access to artifacts, such as encrypted repositories or centralized data portals.

**Relevance to Requirement 3.6.4:**  
Projects must proactively address security and access control concerns to avoid unnecessary delays for IV&V teams. Ensuring **read-only access**, credential management, and proper permissions from the project outset would have prevented delays, enabling the IV&V team to meet its analysis deadlines.

---

### **Lesson No. 5458: Dependency on Third-Party Teams Can Create IV&V Barriers**

**Context:**  
For a software system with components provided by third-party contractors, IV&V was unable to access critical proprietary design documentation and test data. This lack of access resulted in gaps in IV&V coverage and risks to software quality.

**Key Insights:**

* **Clear Access Agreements Needed for Contractors:** Projects that engage third-party vendors must negotiate provisions in the contracts that grant IV&V teams access to the necessary proprietary data.
* **Transparency Improves Validation:** Restricted access to proprietary components limited IV&V’s ability to identify issues or confirm integration across the system.

**Relevance to Requirement 3.6.4:**  
For projects dependent on third-party teams, **access agreements** must be explicitly included in vendor contracts to ensure IV&V has the same level of access to development products, source code, and artifacts as the software development team.

---

### **Lesson No. 723: Early Defect Resolution and IV&V Value**

**(Referenced in previous discussions)**  
**Context:**  
This lesson highlights the importance of using IV&V to identify and resolve defects early in the software development lifecycle. If artifact access is delayed, IV&V cannot assess requirements and designs early, which negates cost and schedule benefits.

**Key Insights:**

* **Focus on Early Deliverables:** Projects that grant IV&V timely access to early artifacts (requirements, use cases, and preliminary designs) allow IV&V to identify and mitigate risks early when fixes cost less.
* **Integrated Access Approach:** Providing automated or real-time access to all baselined artifacts improves IV&V efficiency.

**Relevance to Requirement 3.6.4:**  
Projects should integrate IV&V artifact access into planning from the beginning, ensuring early and ongoing visibility into development products.

---

### **Lesson No. 4847: Test Environment and Dataset Access**

**Context:**  
A spacecraft software project faced delays and risks when IV&V requested access to the testing environment and datasets but was denied due to incomplete coordination with the development team. The lack of access reduced IV&V’s ability to validate test cases and assess software behavior under simulated operational conditions.

**Key Insights:**

* **IV&V in Testing Environments:** IV&V teams must have access to the same test environments, tools, and datasets used by the developer. Incomplete access creates blind spots in the validation process.
* **Collaborative Early Planning:** Collaborative planning with the test team ensures datasets and tools are available and accessible for IV&V.

**Relevance to Requirement 3.6.4:**  
Projects must ensure IV&V has full integration into testing environments and provide the same datasets, configurations, and logs used during system validation.

---

### **Summary of Lessons Learned for Requirement 3.6.4**

| **Lesson** | **Key Takeaway** | **Guidance for Small Projects** |
| --- | --- | --- |
| **Incomplete Access to Development Data (Lesson 708)** | Delayed or restricted access reduces IV&V effectiveness and leads to higher risks. | Streamline artifact access and prioritize mission-critical documents and source code. |
| **Early Involvement Reduces Risk (Lesson 3436)** | IV&V must receive early access to artifacts to mitigate risks proactively. | Grant access to baselined requirements, designs, and source code as soon as they are available. |
| **Security Delays IV&V Progress (Lesson 1712)** | Security concerns often hamper IV&V access unnecessarily. | Proactively plan credentials and implement automated access to secure repositories. |
| **Third-Party Vendor Barriers (Lesson 5458)** | IV&V access must be built into contractor/vendor agreements to avoid gaps. | Include access provisions in third-party contracts for proprietary data, tools, and documentation. |
| **Early Defect Identification (Lesson 723)** | IV&V artifact access enables early defect detection, saving cost and time. | Allow IV&V visibility into requirements, design documents, and test cases early in the lifecycle. |
| **Test Environment Access Issues (Lesson 4847)** | IV&V must replicate the environment used by developers for accurate validation. | Plan full access for IV&V to testing tools, datasets, and logs used in validation and operations. |

---

By incorporating these lessons into small project planning and execution, the risks associated with artifact access delays can be minimized, ensuring effective and efficient IV&V. Providing comprehensive and early access is key to successful IV&V integration and compliance with Requirement 3.6.4.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Benefits of receiving GN&C algorithm in HiFi code](https://software.gsfc.nasa.gov/lesson-details/72/). **Lesson Number 72**: The recommendation states: "Receiving GN&C algorithm in HiFi code facilitates configuration management and updates to FSW based on algorithm changes."

# 7. Software Assurance

**SWE-178 - IV&V Artifacts**

3.6.4 If software IV&V is performed on a project, the project manager shall ensure that IV&V is provided access to development artifacts, products, source code, and data required to perform the IV&V analysis efficiently and effectively.

Providing the IV&V team with timely, electronic access to the full range of required development artifacts, source code, test data, and analysis tools is essential for ensuring efficient and effective IV&V activities. This access helps identify potential risks early, reduces costs, and ultimately helps NASA achieve the mission assurance goals. By following the outlined guidance and best practices, the project manager ensures that IV&V teams are equipped to deliver independent, high-quality assessments throughout the software development lifecycle.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that IV&V has access to the software development artifacts, products, source code, and data required to perform the IV&V analysis efficiently and effectively.

## 7.2 Software Assurance Products

**Product Deliverables:**  
While no specific deliverables are identified at this time, the following evidence should be provided:

* **Confirmation that IV&V has the necessary access**: This includes confirmation that all required development artifacts, products, source code, and other relevant data are made available to the IV&V Provider in a timely, electronic, and usable format. Availability records or approvals should be documented to ensure traceability.

The purpose of this evidence is to verify compliance with the requirement to provide the IV&V team with all needed resources to perform their analysis efficiently and effectively.

## 7.3 Metrics

**Metrics Not Currently Identified:**  
Although no standard metrics are currently specified, projects may benefit from tracking the following custom metrics to assess compliance and effectiveness of IV&V access:

1. **Percentage of Requested Artifacts Delivered on Time:** The percentage of development artifacts delivered to the IV&V team by the requested deadlines.
2. **Time to Provide Artifact Access:** The average time taken to grant IV&V the requested access to repositories or development environments.
3. **Artifact Completeness Index:** The percentage of required artifacts made available to the IV&V team compared to the total number of artifacts requested.
4. **Changes in Access over Time:** A metric to track if updates to required artifacts or repositories are regularly made available as the software evolves.

## 7.4 Guidance

### 7.4.1 Confirmation of IV&V Access:

* Confirm that IV&V has full access to the development lifecycle artifacts, products, source code, data, and environments necessary for their analysis. Without full and timely access to software artifacts, the IV&V team may be unable to provide robust and complete assurance, resulting in critical software risks being overlooked.
* The project must ensure that access is **unrestricted (read-only)** and direct, enabling the IV&V team to interact with up-to-date software artifacts in real time, where possible.

### 7.4.2 Why Electronic Access Is Crucial:

1. **Accuracy in Deliveries**: All software products acquired for NASA projects must be provided in an **electronic format** (preferably original data formats, not PDF or locked formats). This ensures that the content is delivered accurately, retains metadata, and can be used efficiently.
2. **Post-Delivery Utility**: Electronic access supports post-delivery analysis for defect repairs, software extensions, operational assessments, hardware/software workarounds, and potential software reuse in other NASA missions.
3. **Cost-Efficiency**: Timely electronic access streamlines effort, reduces project handling and delivery costs, and provides IV&V teams the tools for highly efficient assessments.
4. **Lifecycle Monitoring**: Providing access during **all phases of the software development life cycle (SDLC)** ensures that IV&V can monitor supplier activities and confirm that end products align with project requirements.

### 7.4.3 What Needs to Be Accessible to the IV&V Team

#### **Key Artifacts to Provide:**

1. **Source and Executable Components:**
   * Source code, compiled executables, and associated build tools.
2. **Software Models and Simulations:**
   * System behavioral models (e.g., UML models, Simulink models) and simulation tools.
3. **Trade Studies and Prototypes:**
   * Results of trade-off analyses and any prototype software, including prototype designs and architectures.
4. **Testing Artifacts:**
   * Test cases, test scripts, results of software testing (unit, integration, and system-level), and test environment setups.
5. **Static Analysis Results:**
   * Any reports or data produced during code analysis, compliance checks (e.g., coding standards), and security scans.
6. **Requirements and Design Data:**
   * Requirements documentation (epics, stories, use cases, etc.), traceability matrices, Software Design Descriptions (SDDs), and any summaries/status of major changes and deviations.
7. **Process and Change Records:**
   * Problem reports, change requests, accepted deviations or waivers, and quality metrics for the software development process.
8. **Configuration Management and Build Records:**
   * Detailed logs of software builds, dependencies, configurations, and the software version description document(s).
9. **Data and Data Definitions:**
   * Data models, data sets, data dictionaries, and database schemas used in the software development.
10. **Maintenance and Risks:**
    * Summaries of open software issues, ongoing maintenance work, and associated risk definitions.

#### **Supporting Documents:**

In addition to the technical artifacts and tools, IV&V providers should have access to the following:

1. **Final System Documentation**:  
   Delivered software manuals, including configuration and operating instructions, as well as the Software Requirements Specification (SRS).
2. **Change History and Status Reports**:  
   Comprehensive records of all major changes applied to the software since the Software Design Document baseline.
3. **Problem Resolution and Test Summaries**:  
   Records of all defect fixes, their resolutions, and associated verification tests.
4. **Software Reusability Analyses**:  
   Final assessments on software's reusability for future NASA projects.
5. **Open Risks and Planned Mitigations**:  
   Documentation that lists any unresolved software-related risks, along with plans for addressing or tracking them.

## 7.5 Additional Long-term Benefits of Artifact Access

1. **Facilitates Knowledge Retention**: Comprehensive access ensures that project and software data remain available for knowledge transfer—even after project personnel or team members transition out of the project.
2. **Supports System Augmentation**: Allows NASA to effectively build upon existing software components for future missions or projects.
3. **Enhances System Reliability**: Continuous artifact access enables retrospective analysis, defect mitigation, and operational optimization of the system post-launch or deployment.

## 7.6 Electronic Access Management Best Practices

1. **Data Centralization**: Use centralized, secure repositories for artifact storage and sharing.
2. **Access Controls**: Provide **read-only access** to IV&V teams to avoid unintentional changes while ensuring they can access real-time data.
3. **Integrity Assurance**: Adopt secure file protocols to ensure the integrity and authenticity of shared artifacts.
4. **Periodic Access Verification**: Ensure that the IV&V team maintains access throughout the development lifecycle, updating and renewing permissions as necessary.

## 7.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks)        * [8.53 - IV&V Project Execution Plan](/spaces/SWEHBVD/pages/102695746/8.53+-+IV+V+Project+Execution+Plan) |

# 8. Objective Evidence

To demonstrate compliance with this requirement, **objective evidence** must be collected throughout the project lifecycle. This evidence should show that **timely, complete, and appropriate access** to all relevant development artifacts was provided to the IV&V team to ensure effective analysis and validation.

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

By collecting and organizing these forms of objective evidence, the project manager can demonstrate compliance with this requirement  ensuring that IV&V was given the necessary access to analyze the software effectively, efficiently, and on time. Completing these documentation efforts reinforces transparency, accountability, and alignment with NASA standards.

Below is a list of objective evidence categories along with specific examples:

## 8.1 Access Planning and Management

#### **a. Artifact Access Plan**

* **Description:** A formal plan that outlines how and when access to development artifacts will be granted to the IV&V team.
* **Examples of Evidence:**
  + IV&V Project Execution Plan (IPEP) with a section dedicated to artifact access.
  + List of agreed-upon artifacts required for IV&V (e.g., requirements, source code, test data).
  + Timeline outlining when artifacts will be baselined and when IV&V will be provided access to these materials.

#### **b. Access Procedures**

* **Description:** Documentation describing the processes and tools used to provide IV&V access to project artifacts in a secure and timely manner.
* **Examples of Evidence:**
  + Procedures for granting IV&V access to repositories (e.g., source code, test management systems).
  + A flowchart or checklist describing steps for artifact production, delivery, and retrieval for IV&V.

#### **c. Meeting Records**

* **Description:** Evidence of meetings between the project manager, development team, and IV&V personnel to discuss and approve access to artifacts.
* **Examples of Evidence:**
  + Meeting minutes discussing artifact access procedures.
  + Email exchanges confirming approvals for IV&V access to specific tools or artifacts.

## 8.2 Artifact Availability Monitoring

#### **a. Artifact Delivery/Access Logs**

* **Description:** Logs or records demonstrating when artifacts were made available to the IV&V team and when they were accessed.
* **Examples of Evidence:**
  + Repository access logs showing when IV&V retrieved or reviewed specific artifacts (e.g., GitHub, JIRA, or database logs).
  + Records of file transfers via secure sharing tools (e.g., encryption key logs, SFTP server logs).
  + Artifact access summary sheets listing:
    - Artifact type.
    - Date the artifact was uploaded/shared.
    - Access confirmation date by the IV&V team.

#### **b. IV&V Access Tracker**

* **Description:** A tracker documenting all artifacts provided to the IV&V team, along with access rights and any issues encountered.
* **Examples of Evidence:**
  + Access tracker spreadsheet or tool showing:
    - Artifact names and versions.
    - Delivery date to IV&V.
    - Feedback or comments from IV&V indicating receipt and usability.
  + Audit results demonstrating timely artifact deliveries and that no requested artifacts were delayed.

## 8.3 Systems and Tools Access

#### **a. IV&V Access Permissions**

* **Description:** Documentation proving that the IV&V team was granted access to specific tools, repositories, and environments used by the development team.
* **Examples of Evidence:**
  + Repository permissions logs (e.g., screenshots showing read-only or restricted access granted to the IV&V team).
  + User role assignments for tools like Git, Bitbucket, Confluence, or Azure DevOps showcasing that IV&V team members had appropriate privileges.
  + Test environment access logs verifying that IV&V was assigned credentials to validate or replicate the developer's test setup.

#### **b. Secure Data Sharing Records**

* **Description:** Evidence of secure methods used to transmit sensitive artifacts to the IV&V team.
* **Examples of Evidence:**
  + Records of artifact delivery through secure tools (e.g., Microsoft OneDrive, Google Workspace, encrypted email).
  + Encryption and decryption logs showing secured access by the IV&V team for proprietary or sensitive materials.
  + Digital transaction tracking for software licenses, proprietary simulators, or data sets used by IV&V.

## 8.4 Compliance with Artifact Content/Quality Standards

#### **a. Artifact Validation Reports**

* **Description:** Evidence that the artifacts provided to IV&V meet agreed-upon content and quality expectations.
* **Examples of Evidence:**
  + IV&V feedback logs or reports confirming that the received artifacts are complete, accurate, and usable.
  + Corrective action or change requests from the IV&V team identifying any missing or insufficient artifacts and how the project addressed those concerns.
  + Validation checklists completed by IV&V to confirm the sufficiency of delivered artifacts (e.g., requirements compliance, code quality, test case definitions).

## 8.5 Communication and Coordination Evidence

#### **a. Artifact Requests and Fulfillment**

* **Description:** Records of artifact requests made by IV&V and the responses from the project team confirming delivery.
* **Examples of Evidence:**
  + IV&V request logs, including the dates artifacts were requested and when the requests were fulfilled.
  + Email correspondence showing the fulfillment of requests or discussions of access issues.
  + Documented clarification or waiver requests for artifacts that were unavailable or not applicable.

#### **b. Collaboration Meeting Records**

* **Description:** Evidence of consistent communications between project managers, IV&V, and development teams to ensure timely artifact delivery.
* **Examples of Evidence:**
  + Meeting agendas and minutes focused on IV&V artifact needs.
  + Action item status from milestone review meetings indicating artifact readiness for IV&V access.
  + Risk or mitigation plans discussed during meetings if delayed artifact access impacted IV&V analysis timelines.

## 8.6 Risk Management Evidence

#### **a. Risk Identification and Mitigation Logs**

* **Description:** Records showing how risks related to artifact access were managed during the project lifecycle.
* **Examples of Evidence:**
  + Risk logs identifying potential delays in artifact access and corresponding mitigation actions (e.g., early baselining, staggered delivery).
  + Evidence of corrective actions taken to resolve IV&V access issues or bottlenecks during the project.

#### **b. Lessons Learned Reports**

* **Description:** Documentation capturing lessons learned from the project, specifically related to IV&V artifact access.
* **Examples of Evidence:**
  + Post-project evaluation reports with feedback on improving artifact access for future projects.
  + Retrospectives highlighting delays or access issues and recommendations for better compliance practices.

## 8.7 Final Verification and Closure

#### **a. IV&V Compliance Reports**

* **Description:** Reports summarizing the IV&V team’s findings, including their assessment of access to artifacts.
* **Examples of Evidence:**
  + IV&V final summary report documenting any access-related issues and their resolutions.
  + Closure statement from the IV&V team confirming they received all necessary artifacts to perform their analysis.

#### **b. Approval Records**

* **Description:** Sign-off from both the IV&V and project team indicating that all artifacts were shared as required at various project milestones.
* **Examples of Evidence:**
  + Documented approvals from IV&V on artifact delivery readiness (e.g., a signoff matrix).
  + Schedule performance data confirming IV&V requirements were met within the timeline.

## 8.8 Summary Table of Objective Evidence

| **Category** | **Sample Evidence** |
| --- | --- |
| **Planning** | IV&V Project Execution Plan (IPEP), artifact access plan, meeting minutes. |
| **Artifact Access Logs** | Repository logs, secure file transfer logs, artifact tracking spreadsheets. |
| **System Access Permissions** | Repository credentials, test system logs, user role assignment screenshots. |
| **Validation of Artifacts** | Feedback reports, usability confirmations, checklists for completeness and sufficiency. |
| **Communication** | Email correspondence, fulfilled request logs, IV&V coordination meeting agendas and minutes. |
| **Risk Management** | Risk logs, mitigation plans for delayed or restricted access, lessons learned reports. |
| **Verification and Closure** | Final reports from IV&V confirming artifact sufficiency, IV&V approval/sign-off documents. |
