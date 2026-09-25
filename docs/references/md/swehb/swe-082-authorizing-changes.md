# SWE-082 - Authorizing Changes

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695463. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes

SWE-082 - Authorizing Changes

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695463)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695463&showCommentArea=true&showComments=true#addcomment)

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

5.1.5 The project manager shall establish and implement procedures to:

a. Designate the levels of control through which each identified software configuration item is required to pass.  
b. Identify the persons or groups with authority to authorize changes.  
c. Identify the persons or groups to make changes at each level.

## 1.1 Notes

IEEE 828-2012, IEEE Standard for Configuration Management in Systems and Software Engineering describes configuration management processes to be established, how they are to be accomplished, who is responsible for doing specific activities, when they are to happen, and what specific resources are required. It addresses configuration management activities over a product's life cycle. Configuration management in systems and software engineering is a specialty discipline within the larger discipline of configuration management. Configuration management is essential to systems engineering and software engineering.

## 1.2 History

Click here to view the history of this requirement: SWE-082 History

SWE-082 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.1.4 The project shall establish and implement procedures designating the levels of control each identified configuration item must pass through; the persons or groups with authority to authorize changes and to make changes at each level; and the steps to be followed to request authorization for changes, process change requests, track changes, distribute changes, and maintain past versions. |
| Difference between A and B | Removed the requirement to identify the "steps to be followed  to request authorization for changes, process change requests, track changes, distribute changes, and maintain past versions". |
| B | 5.1.5 The project manager shall establish and implement procedures to:   1. 1. Designate the levels of control through which each identified configuration item is required to pass.    2. Identify the persons or groups with authority to authorize changes.    3. Identify the persons or groups to make changes at each level. |
| Difference between B and C | No change |
| C | 5.1.5 The project manager shall establish and implement procedures to:   1. 1. Designate the levels of control through which each identified software configuration item is required to pass.    2. Identify the persons or groups with authority to authorize changes.    3. Identify the persons or groups to make changes at each level. |
| Difference between C and D | No change |
| D | 5.1.5 The project manager shall establish and implement procedures to:  a. Designate the levels of control through which each identified software configuration item is required to pass. b. Identify the persons or groups with authority to authorize changes. c. Identify the persons or groups to make changes at each level. |

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
| * [A.08 Software Configuration Management](/spaces/SWEHBVD/pages/133235384/A.08+Software+Configuration+Management) |

# 2. Rationale

Configuration control helps ensure that changes are managed in a structured way, that the impact of changes is assessed before those changes are implemented, and that changes are authorized before being implemented. Using various levels of control can reduce the time and effort it takes to disposition a change request based on the criticality and range of the effect of the change. Less critical or risky changes can use a lower level of authority to make decisions about those changes while more critical or far-reaching changes can require authorization from a more formal body with a broader view of the system.

Establishing and implementing robust procedures for managing **software configuration control** is critical to ensuring the integrity, traceability, and accountability of software artifacts throughout a project's lifecycle. This requirement ensures that changes to software configuration items (CIs) are implemented in a structured, transparent, and well-governed manner to minimize errors, reduce risks, and support the delivery of reliable, safe, and maintainable software.

The rationale for each sub-requirement is outlined below:

### **5.1.5.a: Designate the Levels of Control Through Which Each Identified Software Configuration Item (SCI) is Required to Pass**

#### **Why This Is Important:**

1. **Lifecycle and Risk Management**:

   * Software artifacts often evolve through multiple stages (e.g., development, review, testing, deployment). Establishing levels of control ensures that each software CI passes through critical checks and validations at appropriate lifecycle stages to prevent errors from propagating downstream.
2. **Adaptation to Complexity**:

   * Different software artifacts (e.g., code, test scripts, documentation) and safety-critical components may require varying levels of scrutiny. Defining control levels ensures that high-risk or mission-critical items are subjected to more rigorous monitoring and review, while routine items can follow simplified processes.
3. **Auditability and Compliance**:

   * Defined levels of control help demonstrate compliance with internal standards, contractual obligations, and external requirements (e.g., standards like ISO, IEEE, CMMI, or NASA's software engineering processes) during reviews or audits.

#### **Benefits of Compliance**:

* Improves the quality and reliability of software products by ensuring items are thoroughly reviewed and validated at each control level.
* Reduces the likelihood of defects or integration issues by enforcing validation steps between design, implementation, and release.
* Provides confidence that all required checks (e.g., safety, performance, and testing milestones) are met before deployment or release.

### **5.1.5.b: Identify the Persons or Groups with Authority to Authorize Changes**

#### **Why This Is Important:**

1. **Accountability and Governance**:

   * Clearly defining the authorization authority ensures that changes are reviewed, justified, and approved by appropriate personnel (e.g., project leads, safety officers, or Change Control Boards), reducing the risk of unauthorized or unsuitable modifications.
2. **Change Risk Mitigation**:

   * Software changes, particularly in safety-critical or mission-critical environments, can introduce risks such as bugs, system failures, or safety hazards. Assigning approval authority to qualified individuals reduces the likelihood of inappropriate or unnecessary changes being implemented.
3. **Clear Separation of Responsibilities**:

   * This sub-requirement supports the principle of segregation of duties, ensuring that the individuals who design or propose changes are not the same as those authorizing them. This separation enhances both quality assurance and compliance with safety, security, and governance standards.

#### **Benefits of Compliance**:

* Prevents unauthorized or unintended changes by establishing a clear chain of approval.
* Provides traceability for all changes, enabling effective audits and investigations when needed.
* Ensures that changes to software artifacts align with project priorities, safety goals, and stakeholder expectations.

### **5.1.5.c: Identify the Persons or Groups to Make Changes at Each Level**

#### **Why This Is Important:**

1. **Efficiency and Accuracy**:

   * Designating specific individuals or teams to implement changes ensures that the tasks are performed by qualified personnel who are knowledgeable about the software item, its dependencies, and the impact of the changes.
2. **Prevention of Errors**:

   * Assigning change responsibility focuses expertise where it is most critical, reducing the occurrence of configuration errors or unintended side effects caused by incomplete or improperly executed updates.
3. **Alignment With Governance**:

   * This sub-requirement ensures that the individuals responsible for making changes are different from those approving the changes, maintaining a chain of accountability and compliance with standards that require change control.
4. **Supporting Configuration Control Levels**:

   * At different levels of control (e.g., developmental, testing, release), different teams or individuals may need to implement changes to CIs. This distinction ensures that lower-level development changes and higher-level integration or operational changes are handled appropriately.

#### **Benefits of Compliance**:

* Supports a controlled process for applying changes, ensuring quality and reliability are maintained.
* Reduces potential delays by ensuring that the appropriate teams can quickly respond to approved changes within their areas of expertise.
* Maintains the integrity of the software baseline by ensuring updates are implemented properly and tracked rigorously, especially for safety-critical or high-risk items.

### **Overall Importance of Requirement 5.1.5**

This requirement addresses the **core principles of software configuration management (SCM)** by enforcing structured processes, accountability, and governance over how changes to configuration items are handled. Here are some overarching justifications:

1. **Enhances Traceability**:

   * The requirement ensures that all changes to software CIs are fully traceable, from initiation to implementation. This is vital for debugging, auditing, and improving future processes.
2. **Supports Safety-Critical Missions**:

   * For safety-critical systems (e.g., in aerospace, medical, or defense applications), rigorously controlling changes ensures that no unauthorized, unverified, or undocumented change compromises system safety or reliability.
3. **Manages Scope Creep and Unintended Consequences**:

   * Clearly defined control levels and responsibilities prevent ad hoc changes or scope creep that might disrupt the project schedule, introduce new risks, or degrade performance.
4. **Improves Communication**:

   * Designating roles and responsibilities improves communication among stakeholders, ensuring everyone understands who can approve or perform certain types of changes, as well as the process for escalating risks or issues.
5. **Ensures Process Consistency**:

   * Projects must manage diverse software work products across teams and partners. This requirement enforces consistency in how changes are authorized and implemented, even in multi-team projects or during extended mission phases.

### **Closing Remark**

Requirement 5.1.5 is designed to enforce structured, transparent, and accountable software configuration control processes. By establishing levels of control, defining authorization responsibilities, and assigning implementation tasks to qualified individuals or groups, the project manager creates a governance framework that supports software quality, mitigates risks, aligns with safety standards, and achieves mission success. Good compliance practices for this requirement result in greater project stability, reduced rework costs, and safer, more reliable software systems.

# 3. Guidance

## 3.1 Control Procedures

Configuration control procedures are critical for ensuring consistency, integrity, and accountability during the software development lifecycle. They minimize the risk of arbitrary or unauthorized changes, support traceability, and maintain reliable project artifacts. This guidance expands on approaches for establishing control procedures, managing change authority, and implementing a robust and efficient change control process. Meant to provide practical steps and enhance clarity, the following refined sections ensure full compliance with the expectation of Requirement 5.1.5.

#### **Why Configuration Control Procedures Are Important**

Configuration control procedures formalize the process of managing changes across all software configuration items (CIs). Without clear procedures, teams risk introducing uncoordinated changes that can lead to inconsistencies, errors, and compliance failures. Proper control ensures that changes are authorized, documented, and implemented in a coordinated and predictable manner.

The **Software Configuration Management Plan (SCMP)** is the controlling document for defining these procedures (see **SWE-079 - Develop CM Plan**) and should include:

* **Levels of control:** The oversight depth required for CIs based on their criticality and lifecycle stage.
* **Change authority:** The individuals or groups empowered to approve, reject, or escalate changes.
* **Authorization request process:** The steps for submitting and approving requests.
* **Change request process:** The end-to-end workflow for handling change requests, from initiation to final approval.
* **Version maintenance:** Processes for tracking and managing approved software versions, ensuring consistent access to historical data.

#### **Best Practice Resource**

The **STEP Software Configuration Management and Data Management course**, available via SATERN and created by the Westfall Team, offers best practices for managing configuration control. Some excerpts are incorporated into this guidance, providing practical recommendations.

## 3.2 Levels of Control

Each software CI requires a defined **level of control** based on its significance to the project and its lifecycle stage. For example:

1. **Documentation** might require one level of review and approval, while
2. **Source code or safety-critical items** may require more stringent, multilayered approval.

#### **Guidelines for Defining Levels of Control**

1. **Ownership Assignment**:

   * Assign an "owner" to each CI or class of items. This owner is responsible for approving changes. Examples:
     + The **Change Control Board (CCB)** may oversee all software libraries.
     + A peer review team might control product documentation.
   * Ensure that CI "ownership" responsibilities are clearly documented in the SCMP.
2. **Impact-Driven Control**:

   * Establish levels based on the impact of changes. For example:
     + Changes to **shared libraries** might require approval from multiple change authorities across projects.
     + Changes isolated to a specific project may require only project-level authorization.
3. **Lifecycle-Specific Control**:

   * Adjust control levels dynamically based on the project’s lifecycle.
     + Example: Changes to code during initial development could use simplified change controls compared to post-launch modifications of the same artifact.
4. **Origin of the Change**:

   * Changes requested by external parties (e.g., end-users, customers) may require additional scrutiny compared to developer-initiated changes.

#### **Flexibility vs. Rigor**

The goal is to balance **control efficiency** (to reduce delays) with **process rigor** (to ensure reliability). Each level of control should be optimized to account for cost, risk, and operational criticality.

## 3.3 Change Authority

Defining **change authority** is a cornerstone of configuration management. This authority ensures that changes are rigorously reviewed and implemented under the oversight of qualified individuals or groups.

#### **Categories of Change Authorities**

1. **Primary Change Authorities**:

   * **Configuration Control Boards (CCBs):** Typical decision-makers for changes within software projects, organized at different levels:
     + **Product Level CCB:** Responsible for system-level baselines affecting fielded software, functionality, and products.
     + **Project Level CCB:** Oversees project-specific updates with isolated impacts.
     + **Software Development CCB:** Focuses on development-level changes (e.g., builds, testing fixes).
   * **Examples Include**:
     + Change Authorization Boards (CABs), Engineering Change Boards (ECBs), and other review bodies.
2. **Stakeholders and Experts**:

   * Safety assurance engineers for assessing safety-critical impacts.
   * Domain experts (e.g., software engineers, hardware engineers) to evaluate technical feasibility and risks.
   * Systems engineers for impacts to integrated components.
   * Customers and operational stakeholders for user-requested changes.

#### **Considerations When Defining Change Authority**

1. **Levels of Approval**:

   * Establish hierarchical chains for escalating approvals:
     + Smaller, experienced groups for low-level developmental changes.
     + Larger, cross-functional boards for significant or system-level changes.
   * Define **escalation plans** for unresolved or high-stakes decisions.
2. **Meeting Frequencies**:

   * Higher-level boards typically convene less frequently to save time and cost. Develop temporary actions for urgent change requests.
3. **Responsibility Documentation**:

   * Document tasks, jurisdiction, and decision-making criteria for each authority level.

## 3.4 Authorization Requests

#### **Key Elements of the Authorization Request Process**

1. **Proper Request Forms**:

   * Include appropriate documentation forms for change requests (e.g., **Engineering Change Proposals (ECPs)**, Problem Reports (PRs), or Change Requests (CRs)).
2. **Instructions for Completion**:

   * Ensure that the **change request form** gathers all critical information for informed decision-making:
     + Clear description and rationale for the request.
     + Affected configuration items.
     + Cost, risk, and schedule impact assessment.
3. **Submission Guidelines**:

   * Provide instructions on selecting the **appropriate change authority** and routing requests effectively.
4. **Response and Disposition Timelines**:

   * Define when requesters can expect disposition decisions and ensure tracking compliance to timelines.

## 3.5 Change Request Process

The change request process comprises three main steps:

1. **Processing Requests**:

   * Introduce pre-screeners to verify that requests are complete and within the project’s scope.
   * Provide clear disposition options for approval, deferral, or rejection.
2. **Tracking Changes**:

   * Use CM tools to track:
     + Change status (e.g., open, approved, closed).
     + Status change dates.
     + Verification results for implemented changes.
   * Maintain traceability between approved changes and related artifacts (e.g., requirements, code, test data).
3. **Distributing Updates**:

   * Ensure changes are verified before release.
   * Release changes through controlled mechanisms, e.g., baselines or updates.
   * Use a **Version Description Document (VDD)** to communicate release contents.

## 3.6 Version Maintenance

#### **Best Practices for Managing Software Versions**

* **Tagging Versions**: Use CM tools to "tag" software baselines, making retrieval and rollback easier.
* **Traceability to Releases**: Link versions of CIs to the fielded versions they impact.
* **Record Retention**: Store historical versions for debugging and post-release maintenance.

#### **Importance of Version Maintenance**

* Enables faster response to issues in the field.
* Ensures fixes are rolled out consistently across all impacted versions of the software.

### **Conclusion**

The enhanced guidance for **Requirement 5.1.5** provides software engineering teams with a structured roadmap to establish and implement strong configuration control procedures. These recommendations guide teams in defining levels of control, assigning change authorities, structuring authorization workflows, and creating efficient change request systems. The goals are to ensure software integrity, mitigate risks, enhance process transparency, and maintain compliance with safety and quality standards throughout the software lifecycle.

Configuration control procedures are important because they help ensure that arbitrary changes are avoided and that the team understands how changes are to be managed for the project.

A sample process flow might look like this chart adapted from the STEP Level 2 Software Configuration Management and Data Management course: [343](#_tabs-<p></p>)

See also [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking),

[SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan).

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Configuration Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Configuration+Management) |

# 4. Small Projects

For smaller projects with limited staff size, resources, or budgets, it is imperative to simplify configuration control and change management processes while ensuring they remain effective, scalable, and compliant with project goals. The following enhanced guidance addresses the unique needs of small projects, balancing simplicity with rigor to maintain software integrity, traceability, and accountability.

### **Change Authority and Change Control Board (CCB)**

#### **Role Consolidation in Small Projects**

* In small projects with fewer personnel, the **Change Control Board (CCB)** may be represented by a single individual who has the oversight and expertise required to manage configuration control. This role should be designated to someone with:
  + **Broad Project Knowledge**: An understanding of the project’s goals, constraints, and requirements.
  + **Technical Competence**: The ability to assess the impact of proposed changes to software, systems, and interfaces.
  + **Leadership Oversight**: The authority to make decisions across configuration baselines and software lifecycle stages.

#### **Examples of Possible Change Authorities (Single Point of Control)**

* **Software Manager**: Oversees the development and ensures changes align with software goals and processes.
* **Systems Manager**: Manages changes that impact the software’s integration with hardware or other systems.
* **Product Development Lead or Technical Lead**: Handles changes directly tied to product development, focusing on delivering functional baselines.

#### **Best Practices for a Single-Person CCB in Small Projects**

1. **Document Authority Delegation**:

   * Clearly define and document the authority of the designated change controller in the project’s **Configuration Management Plan (SCMP)** or equivalent document.
   * Include details about the decision-making boundaries for the designated individual, such as when escalation is required.
2. **Ensure Independent Review of High-Risk Changes**:

   * For safety-critical or project-wide changes, include at least one peer or stakeholder (e.g., software assurance personnel, safety engineer, primary customer) in the review process before final disposition.
   * This ensures that the single-person change authority is supported with checks and balances for significant decisions.
3. **Use Simplified Procedures**:

   * Streamline the approval and documentation processes as much as possible without compromising the quality of decision-making.
   * Focus on maintaining traceability with simple workflows that are proportionate to the project’s scale.

### **Simple Tools for Small Projects**

#### **Tool Selection for Managing Changes**

Small projects often lack access to complex or expensive tools for managing change requests, approvals, and metrics. To adapt, smaller teams can implement low-cost, but effective solutions, such as:

1. **Spreadsheet-Based Tools**:

   * **Problem Report Tool (PRT)**: A simple spreadsheet or shared document (e.g., Excel, Google Sheets) can be used to:
     + Log and track change requests.
     + Document approvals and decisions.
     + Capture important details like CI names, request origins, impact analysis, and resolution status.
   * Example Columns in the Spreadsheet:
     + Change Request ID.
     + CI(s) Affected.
     + Description of Change.
     + Rationale for Change.
     + Impact Assessment.
     + Approval Status (Pending, Approved, Deferred, Rejected).
     + Implementation Date.
     + Assigned Person/Group.
     + Closure Notes/Verification Status.
   * Maintain a shared version to ensure transparency across the team.
2. **Cloud Collaboration Tools**:

   * Use lightweight project management tools such as **Trello**, **Asana**, or **[Monday.com](http://Monday.com)** to track changes, tasks, and approvals.
   * These tools can function as digital boards, where change requests are logged and tracked through simple workflows.

#### **Core Features of a Simple Change Request Tool**

* **Centralized Record**: All change requests and their details should be stored in a single source of truth (spreadsheet or tool).
* **Version Control**: If possible, integrate the tool with a file or software version control system (e.g., Git, SVN) to ensure alignment between the approved changes and the corresponding configurations.
* **Metric Reporting Capability**:
  + Collect counts and statuses of change requests:
    - Number of open, closed, deferred, and rejected requests.
    - Types of changes (e.g., corrective, adaptive, preventive).
  + Calculate simple metrics, such as the average time to resolve a change request, to monitor improvement opportunities.

### **Tailored Process for Small Projects**

#### **Change Request Workflow**

Define a lightweight change request workflow tailored for the small project environment:

1. **Initiation**:

   * The change requestor submits the change request (using the spreadsheet/tool) and provides necessary information, including CI name, description, rationale, and impact.
2. **Review and Assignment**:

   * The single-person CCB reviews the change request for technical accuracy and scope.
   * Conduct a quick impact analysis focusing on cost, schedule, and risks.
   * Assign responsibility for implementing the change if approved.
3. **Approval or Escalation**:

   * For minor changes, the single-person CCB authorizes the request directly.
   * For complex or high-risk changes, escalate the decision to an independent reviewer or supervisor.
4. **Implementation**:

   * Assign the change to a team member or implement it directly as appropriate for the small staff size.
   * Ensure all impacted artifacts (e.g., source code, documentation, test cases) are aligned with the approved change.
5. **Verification and Closure**:

   * Confirm that the change has been implemented and verified properly (e.g., through reviews or testing).
   * Update the tool or log to reflect closure, including final verification results.

### **Version Control and Release Management**

#### **Version Control in Small Projects**

* Use lightweight version control tools like **Git** or **SVN** for tracking software changes, even in small teams. Define processes for:
  + **Branching Strategies**: For example, use a "main" branch for approved baselined code and separate branches for changes in progress.
  + **Change Tracking**: Associate each change request with specific commits using commit messages.

#### **Release Management with Limited Resources**

* Maintain a simple **Version Description Document (VDD)** for each release, listing:

  + Changes included in the release.
  + Affected CIs.
  + Updated versions of affected items.
  + Testing or verification results that confirm the changes.
* Release software in an incremental, controlled manner, ensuring proper documentation accompanies every update.

### **Summary and Key Considerations for Small Projects**

#### **Why Adapt These Processes?**

* Smaller projects do not have the luxury of extensive staff or expensive tools, but the need for configuration control and traceability remains critical.
* Using simplified processes, clear documentation, and scalable tools ensures that smaller projects retain control while avoiding inefficiencies or unnecessary overhead.

#### **Key Steps for Success**:

* Assign a **qualified individual** as the centralized change authority (e.g., project manager, software lead).
* Use **simple, low-cost tools** (e.g., spreadsheets) to document and manage changes and track associated metrics.
* Define **clear and streamlined procedures**, scaling complexity based on the importance of the CIs.
* Build in flexibility for changes while maintaining essential governance to avoid the risks of uncontrolled modifications.

By adopting this guidance, small projects can effectively manage configuration control and change requests, ensuring consistent software quality and compliance with project requirements.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-011) Change Request Log Template,  NASA Goddard Space Flight Center, 2015.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-212)

  [IEEE Guide to Software Configuration Management,](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=89631&tag=1 "Click to open in new window")

  IEEE Computer Society, IEEE STD 1042-1987, 1987.  This link requires an account on the NASA START (AGCY NTSS) system (https://standards.nasa.gov ). Once logged in, users can access Standards Organizations, IEEE and then search to get to authorized copies of IEEE standards.
* (SWEREF-216)

  [828-2012 - IEEE Standard for Configuration Management in Systems and Software Engineering](https://ieeexplore.ieee.org/document/6197683 "Click to open in new window")

  IEEE STD IEEE 828-2012, 2012.,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-337)

  [Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf "Click to open in new window")

  Souppaya, Murugiah, Scarfone, Karen, NIST Special Publication NIST SP 800-40r4, April, 2022
* (SWEREF-343)

  [STEP Level 2 Software Configuration Management and Data Management course, SMA-SA-WBT-204, SATERN (need user account to access SATERN courses).](https://saterninfo.nasa.gov/ "Click to open in new window")

  This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-357)

  [Risk-Based Configuration Control - Balancing Flexibility with Stability,](http://www.westfallteam.com/node/56 "Click to open in new window")

  Westfall, Linda, The Westfall Team (2007),  Contains video slide presentation and copy companion paper.
* (SWEREF-546)

  [Configuration Control at All Levels of Change](https://llis.nasa.gov/lesson/1213 "Click to open in new window")

  Public Lessons Learned Entry: 1213.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Configuration control is a critical aspect of ensuring consistency, traceability, and accountability across project artifacts. While the lesson highlighted from the **NASA Lessons Learned database (Lesson Number 1213)** emphasizes hardware configuration control, the underlying principle of accounting for all levels of authorized changes and providing feedback applies equally to software development. This enhanced section expands upon the lesson and includes additional insights and actionable recommendations for software projects.

---

### **Lesson: Configuration Control at All Levels of Change**

#### **Lesson Summary from NASA LL Database**

* **Lesson Number 1213**: "Configuration control processes must account for all levels of authorized changes and provide feedback to affected program elements, including training and operations."
* **Key Takeaways**:
  + Configuration control must span **all levels of change**—from the smallest software module to the system-wide operational elements—in order to avoid gaps that could lead to failures or inconsistencies.
  + Effective change management requires **continuous communication and feedback** to ensure all impacted elements, including personnel, are updated appropriately (e.g., training teams, operation teams, testing teams).

---

### **Expanded Application to Software Configuration Control**

#### **1. Configuration Control Across All Levels**

Software configuration control must ensure comprehensive coverage of changes across all levels of the project, including:

1. **Individual Artifacts**:

   * Source code files, test scripts, documentation, libraries, models, safety-critical components, interfaces, and more.
   * Changes at the artifact level must be tracked and validated to prevent incorrect versions from propagating to higher-level integrations.
2. **Subsystems and Integrated Components**:

   * Changes at the subsystem level (e.g., APIs, shared libraries, control frameworks) must factor in dependencies and impacts on other components or subsystems.
3. **System-Level Impact**:

   * Large-scale software modifications that affect operational requirements (e.g., commanding systems or mission-critical algorithms) must undergo rigorous change control and require approval from higher-level authorities.
4. **Operational and Training Feedback**:

   * Changes impacting user interfaces, workflows, or automated processes must be reconciled with end-user training, operational procedures, and systems testing to ensure usability and correctness.

#### **Key Principles**:

* **Granularity**: Each change should be documented and managed at its most granular level, ensuring that no dependency is overlooked.
* **Top-down and Bottom-up Traceability**: Changes must trace from requirements through implementation artifacts and operational deployment, safely propagating from affected lower-level items to higher-level systems and vice versa.

---

#### **2. Feedback to All Affected Stakeholders**

Effective configuration control extends beyond technical changes to include interaction with affected stakeholders. Feedback loops ensure that all related teams remain aligned and can act appropriately. Key areas for stakeholder involvement:

* **Training Teams**:

  + Document changes that affect end-user or operator behaviors. Ensure training materials reflect updated workflows or system features.
  + Provide timely training updates for personnel managing or interacting with altered configurations.
* **Operations Teams**:

  + Communicate changes impacting operational processes or tools to ensure continuity and prevent errors in real-world scenarios.
  + Include operators in reviews for system-wide changes to identify usability issues before deployment.
* **Testing Teams**:

  + Supply feedback from testing activities to verify the validity and robustness of the implemented changes.
  + Ensure testing procedures reflect updates to safety-critical components or functional configurations.
* **Project-Level Leadership**:

  + Inform leadership (e.g., Project Manager, Change Control Board (CCB)) about significant impacts on cost, schedule, or risks due to changes.

---

### **Lessons Learned for Improved Software Configuration Control**

Here are additional lessons derived from real-world software projects and NASA practices:

---

#### **Lesson 1: Avoid Overlooked Impacts of Small Changes**

* Small, localized changes to individual configuration items can have far-reaching effects, especially in safety-critical or high-complexity systems.
* **Best Practices**:
  + Conduct thorough **impact analyses** before authorizing even minor changes.
  + Consider how changes could cascade into interfaces, dependent systems, or downstream workflows.
* **Example**: In a space mission, updating a communications protocol for a specific subsystem led to unintended delays in telemetry for unrelated mission systems due to unanticipated compatibility issues.

---

#### **Lesson 2: Establish Multi-Level Approval Processes**

* Changes should not bypass appropriate levels of authority. Higher-level approval processes reduce risks associated with incomplete analysis for medium to large-scale modifications.
* **Best Practices**:
  + Implement tiered approval levels based on the severity, scope, and risk of the change.
  + Lower-level changes can be handled by development teams, while critical system-level changes require approvals from CCBs or mission directors.
* **Example**: A software module affecting spacecraft trajectory control required escalation to mission engineering leadership for approval after the subsystem CCB flagged potential mission-wide ramifications.

---

#### **Lesson 3: Maintain Flexibility Within Formal Processes**

* While formalized processes are essential, adaptability is equally important when dealing with project deadlines, rapid changes, or evolving requirements.
* **Best Practices**:
  + Include provisions for expedited reviews of urgent changes (e.g., emergency fixes to remove critical bugs).
  + Incorporate mechanisms for prioritizing and deferring non-critical changes appropriately.
* **Example**: An urgent patch for real-time data processing during a mission allowed immediate testing and deployment by an expedited review panel, while minor interface updates were deferred until the next development cycle.

---

#### **Lesson 4: Communicate Change Traceability**

* Traceability gaps in change history can lead to confusion during audits, deployment, or system operations.
* **Best Practices**:
  + Ensure that changes are consistently linked to their originating requirements, impacted configurations, and affected baselines.
  + Use configuration tools capable of automatic logging and traceability mapping across artifacts, such as Git, Redmine, or JIRA integrated with CM workflows.
* **Example**: A lessons-learned report noted that failure to adequately trace a minor bug fix to its corresponding requirement introduced a preventable regression in the next software update.

---

#### **Lesson 5: Include End-to-End Coordination**

* Coordinate changes across development, testing, validation, and fielded operations to prevent mismatched configurations and ineffective implementations.
* **Best Practices**:
  + Configuration control processes must synchronize training plans, operational procedures, and software versions with approved changes.
  + Perform integration testing to ensure affected subsystems work cohesively after modifications.
* **Example**: A delay in updating training materials for operators handling onboard mission systems led to misinterpretations of new system behaviors, causing operational anomalies.

---

#### **Lesson 6: Continuous Monitoring of Baselines**

* Once a baseline is established, changes must be continuously monitored and feedback provided to project teams.
* **Best Practices**:
  + Regularly audit baselines to ensure configuration settings align with approved changes, even in long operational phases.
  + Prevent baseline creep by limiting unauthorized updates or untracked revisions.
* **Example**: Failure to monitor baseline drift during extended operations of a space-based system resulted in outdated mission parameter sets being deployed in subsequent updates.

---

### **Conclusion**

The lessons learned emphasize the importance of **comprehensive configuration control**, including feedback loops, multi-level approval processes, and stakeholder involvement. Small changes can have wide-ranging impacts, and both technical and operational feedback ensure the entire project ecosystem adapts successfully. These lessons, when applied rigorously, enable projects to mitigate risks, maintain integrity in their software systems, and deliver robust and reliable results.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Test plans should cover all aspects of testing](https://software.gsfc.nasa.gov/lesson-details/56/). **Lesson Number 56**: The recommendation states: "Test plans should cover all aspects of testing, including specific sequencing and/or data flow requirements."
* [Have more responsive CCBs during IOC](https://software.gsfc.nasa.gov/lesson-details/81/). **Lesson Number 81**: The recommendation states: "Have more responsive CCBs during Initial On-Orbit Checkout (IOC),  quickly assembled in response to events with stakeholders with technical expertise and decision authority."
* [Simulations/rehearsals with the SC and execute re cover prior to launch](https://software.gsfc.nasa.gov/lesson-details/94/). **Lesson Number 94**: The recommendation states: "Execute simulations/rehearsals with the SC where EEPROM is loaded (to all available processors/banks of EEPROM) and execute recovery prior to launch."

# 7. Software Assurance

**SWE-082 - Authorizing Changes**

5.1.5 The project manager shall establish and implement procedures to:

a. Designate the levels of control through which each identified software configuration item is required to pass.  
b. Identify the persons or groups with authority to authorize changes.  
c. Identify the persons or groups to make changes at each level.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that software assurance has participation in software control activities.

2. Perform an audit against the configuration management procedures to confirm that the project follows the established procedures.

## 7.2 Software Assurance Products

This guidance provides a clearer structure, actionable recommendations, and additional details to properly assess and support software configuration management activities. The goal is to ensure compliance with NASA’s **NPR 7150.2** requirements, Center-specific procedures, and sound configuration management practices.

#### **Deliverables for Effective Software Assurance**

1. **Software Configuration Management Procedure Audit Report**:

   * Audit results should detail:
     1. **Findings**: Issues, non-conformances, and areas of improvement identified during the audit.
     2. **Risks and Issues**: Description of risks posed by non-compliance, such as potential mission impact, schedule delays, or quality issues.
     3. **Recommendations**: Actions the project should take to address identified deficiencies or enhance the process.
     4. **Evidence**: Links to supporting artifacts, such as SCMPs or change logs, to justify findings.
   * Analysis should highlight whether the configuration management (CM) process is compliant, effective, and scalable for the project’s needs.
2. **Key Configuration Management Artifacts for Review**:

   * **Software Configuration Management Plan (SCMP)**:
     + Evaluate whether it reflects configuration management objectives, control processes, roles and responsibilities, and tools used.
     + Ensure NPR 7150.2 configuration management requirements are covered in the plan.
   * **Software Configuration Management System Data**:
     + Review system logs, change histories, and versioning information to verify transparency and traceability.
     + Confirm records reflect proper control over modifications, including approvals and rollbacks.
   * **Audit Findings of the Change Management Process**:
     + Provide documented results showing compliance levels of the project’s change management process.
     + Identify discrepancies between procedure design and practice (e.g., unauthorized changes, incomplete records).
3. **Required Documentation Reviews for Compliance**:

   * Verify establishment of **Change Control Boards (CCBs)**, including:
     + Defined membership, roles, and authority levels.
     + Software assurance (SA) personnel participation as mandated.
   * Examine **change authorization guidelines** to confirm:
     + Control levels and approval workflows are adequate, even for small projects with simplified procedures.
     + Authorized personnel and the chain of authority are explicitly defined.
   * Validate **CM traceability**:
     + Confirm all CIs are uniquely identified, controlled, and traceable across baselines, lifecycle phases, and versions.

## 7.3 Metrics

#### **Key Metrics for Software Assurance of Configuration Management**

The following metrics can be used to measure the effectiveness of configuration management processes and identify improvement opportunities:

1. **Audit Findings**:

   * **Findings Open vs. Identified**: Ratio of unresolved findings to total findings raised during audits.
   * **Trends of Open vs. Closed Findings Over Time**: Indicate the responsiveness of the project to resolving audit issues and improving over time.
   * **# of Process Non-Conformances by Lifecycle Phase**: Track where in the lifecycle most process issues arise (e.g., development vs. operations).
   * **Process Non-Conformances Identified by SA vs. Accepted by Project**: Measure alignment between the assurance team and the project on recognizing and addressing non-compliance issues.
2. **Configuration Audit Metrics**:

   * **# of Configuration Management Audits**:
     + Planned vs. Actual audits conducted to ensure audit scope is fully executed.
   * **# of Non-Conformances per Audit**: Examine compliance levels across multiple audits for trends.
   * **Trends of Non-Conformances Over Time**:
     + Track whether repeated issues persist.
     + Identify improvements or regressions in practices.
3. **Compliance and Reporting Metrics**:

   * **Audit Compliance Trends**:
     + **# of Compliance Audits Planned vs. Performed**: Ensure adherence to assurance plans.
   * **Open vs. Closed Non-Conformances**:
     + Monitor remaining issues vs. those resolved to track process maturity.

#### **Additional Notes on Metrics**:

* Use historical metric trends to guide management decisions for strengthening processes.
* Incorporate lessons learned into **SCMP updates** to prevent repeat findings.
* Refer to **SWE-080 - Track and Evaluate Changes**, which provides additional tracking metrics aligned with software change control.

## 7.4 Guidance

#### **Steps for Assessing Compliance with Configuration Management Procedures**

**Preparation**:

1. **Understand Requirements**:

   * Collect relevant documents, including Center-specific CM procedures, NPR 7150.2 requirements, and project SCMPs.
   * Identify CM activities mandated in NPR 7150.2—such as baseline control, change tracking, and authorization.
2. **Compare Procedures**:

   * Review the project’s documented CM procedures for alignment with NPR 7150.2 and Center-specific rules.
   * Verify alignment between project-specific SCMPs (or equivalent) and required CM processes.

**Execution**:

1. **Documentation Review**:

   * Ensure CM plans cover:
     + Change control procedures (including CCBs and authorization levels).
     + Data management plans (can be a separate plan or integrated into the SCMP).
   * Check procedures for:
     + Identifying authorized personnel (roles, responsibility assignments).
     + Specific levels of control described for configuration items (CIs).
     + CCB workflows, including membership and decision-making authority.
2. **Audit Validation**:

   * Assess whether audits are being conducted as defined in the CM procedures.
   * Confirm audits track whether CCBs follow documented workflows and processes (e.g., proper reviews occur for each CI change).

**Findings and Feedback**:

1. **Collaboration with the Project Team**:

   * Promptly share audit findings with the project team and provide clear recommendations for remediation.
   * Ensure the project commits to addressing findings in a timely manner, and track closure of corrective actions.
2. **Highlight Positive Practices**:

   * Report successes or innovative CM practices beneficial for future projects.

#### **Best Practices to Enhance Software Assurance Activities**

* **Include SA Personnel in Decision-Making**:

  + SA representatives should actively participate in all control boards to provide insights into risks and compliance.
  + Their role ensures safety concerns and assurance goals remain central to change control discussions.
* **Track Process Maturity**:

  + Use audit results and trend metrics to determine whether the project’s CM approach is improving over time.
  + Provide feedback for iterative refinement of processes.
* **Engage Stakeholders Early**:

  + Collaborate with CCBs and project leadership early in the lifecycle to enforce adoption of best practices.
  + Address discrepancies in scope, timing, or resource allocation for CM activities before they escalate into risks.

## 7.5 Additional Lessons and Considerations

1. **Continuous Process Evaluation**:
   * Even robust plans can fail if not periodically validated against actual practices. Include CM verification activities throughout the lifecycle.
2. **Automated Tools**:
   * Leverage CM tools (e.g., Git, Jira, or Polarion) to generate real-time data for audits, ensuring efficiency and accuracy.
3. **Small Projects**:
   * Small-scale projects can simplify CM processes but should still ensure traceability and proper approvals at all levels.
4. **Documentation Maintenance**:
   * Projects should actively update SCMPs and associated procedures to reflect lessons learned, audit feedback, and evolving requirements.

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence refers to documented artifacts, activities, or outcomes that demonstrate compliance with the requirement. In this case, the evidence for software configuration control should validate that procedures are established, implemented, and adhered to throughout the lifecycle of a project. Below is a comprehensive list of objective evidence categorized by the aspects of Requirement 5.1.5:

---

### **1. Evidence of Established Configuration Control Procedures**

This category demonstrates the existence of documented configuration control procedures addressing change levels, authority, and implementation.

#### **Artifacts to Provide:**

1. **Software Configuration Management Plan (SCMP)**:

   * Contains detailed instructions on levels of control, change authorization, approval processes, roles, and responsibilities.
   * References established procedures for configuration control and configuration audits.
2. **Center-Specific or Organizational Procedures**:

   * Any applicable guidelines or standards that the project follows for software configuration management.
3. **Configuration Identification Documents**:

   * List of software configuration items (CIs) with associated control levels and baselines.
   * Documentation should indicate which items require higher approval processes (e.g., safety-critical items).
4. **Change Control Board (CCB) Documentation**:

   * Policies, charters, or procedures defining the roles, responsibilities, and structure of the CCB or its equivalents at different control levels.
5. **Configuration Control Workflow Diagrams**:

   * Visual representations of how changes are proposed, reviewed, approved, and implemented.
   * Include the paths for typical change request lifecycle scenarios.

---

### **2. Evidence of Implementation (Process Execution)**

#### **Artifacts to Provide:**

1. **Change Control Records**:

   * Approved **software change requests (SCRs)**, **problem reports (PRs)**, or **engineering change proposals (ECPs)** showing evidence of:
     + Identification and categorization of changes.
     + Impact assessment (cost, schedule, risk, safety considerations).
     + CCB or designated authority’s approval (signatures, timestamps, or tool-generated logs).
   * Clearly indicate the CIs being changed.
2. **Change Control Board (CCB) Meeting Minutes**:

   * Records and minutes of CCB meetings showing discussion, decisions, and approvals for significant software changes.
   * Include lists of participants, votes, and justifications for decisions.
3. **Audit Reports (Configuration Management Audits)**:

   * Results of process and compliance audits showing adherence to configuration management procedures.
   * List of findings, discrepancies, or non-conformances with actions taken to resolve them.
4. **Implementation Logs**:

   * Logs showing the execution of changes, including who made the changes, their verification status, and when the changes were applied to baselines.
5. **Communication Logs**:

   * Evidence of communication with stakeholders about changes (e.g., safety teams, testing teams, or operations personnel).
6. **Training Logs (if updates affect operators or users)**:

   * Documentation of training updates for personnel impacted by the changes.

---

### **3. Evidence of Authorization Levels and Authority**

Objective evidence showing that designated individuals or groups reviewed and authorized changes appropriately.

#### **Artifacts to Provide:**

1. **Roles and Responsibilities Assignments**:

   * Documentation assigning specific individuals or teams the authority to approve changes (e.g., Software Manager, Safety Engineer, Project Manager).
   * Examples:
     + SCMP sections on roles and responsibilities.
     + Organizational charts showing change authorities.
     + Internal charters defining authorized personnel for specific workflows.
2. **Approval Evidence**:

   * Individually tracked changes demonstrating:
     + The level of authorization required and obtained.
     + Signatures, electronic approvals, or meeting evidence documenting the process.
3. **Escalation Logs**:

   * Records for changes that required reviews from higher-level authorities (e.g., project-wide CCB or product-focused CCB).
   * Evidence showing the issues raised, actions taken, and final decisions, including any escalations (e.g., from project-level to enterprise-level boards).

---

### **4. Data for Verifying Process and Compliance**

Metrics and tracking data to demonstrate that the configuration control process is effectively monitored and measured.

#### **Artifacts to Provide:**

1. **Metrics Reports or Dashboards**:

   * Example metrics for configuration control:
     + Open vs. closed change requests.
     + Time required to process a change request.
     + Number of unauthorized changes caught by audits.
     + Number of recurring non-conformances from process reviews or audits.
   * Reports generated using CM tools or project tracking systems.
2. **Configuration Baseline and Version Tracking Logs**:

   * Logs showing the traceability of change iterations (e.g., version numbers, Git commits, or other baselined data).
3. **Trend Analysis Reports**:

   * Historical data showing improvements in configuration control processes or response times based on prior audit results or metrics.
4. **Compliance Findings Reports**:

   * Summaries of compliance reviews or audits documenting whether the project’s CM procedures align with NPR 7150.2 or project-specific goals.

---

### **5. Evidence of Planned and Conducted Audits**

Audits and reviews provide objective evaluations of the compliance and integrity of the configuration control process.

#### **Artifacts to Provide**:

1. **Audit Plans**:

   * Evidence that configuration management audits were planned and scheduled during the project lifecycle (list of timelines, goals, planned scope, etc.).
2. **Audit Findings Reports**:

   * Documentation detailing non-conformance issues, risks, and opportunities for improvement.
   * Include actions taken (tracked to closure) or plans for remediation.
3. **Process Improvement Logs**:

   * Evidence that lessons learned from configuration management audits were implemented.
4. **Configuration Tools Review**:

   * Logs or findings related to assessments of CM tools (e.g., Git, Jira, or Polarion) demonstrating their reliability and usage.

---

### **6. Specific Evidence for Small Projects**

Small projects often use simplified approaches for configuration control. Appropriate objective evidence may include:

#### **Artifacts to Provide**:

1. **Simplified Procedure Documentation**:

   * Single-page or reduced-scale SCMP adapted for small projects.
   * Defined single-person CCB authority with documented roles and escalation paths.
2. **Spreadsheets or Lightweight Tools**:

   * If formal CM tooling is absent, provide spreadsheets or task trackers (e.g., Excel, Trello) to show:
     + Change logging.
     + Decisions and tracking data.
3. **Manual Logs or Annotations**:

   * Manually updated documents showing how changes were managed (e.g., development notes linked to specific baselines).

---

### **7. Configuration Control Readiness Evidence**

Finally, ensure evidence that configuration control processes are operational and capable of immediate application:

1. **Simulation or Walkthrough Evidence**:

   * Conduct walkthroughs of the CM process and record step-by-step validations of control procedures.
   * Show how a hypothetical change request passes through levels of control.
2. **Test Case Results for CM Procedures**:

   * Results from testing or auditing the CM processes (e.g., confirm request tracking identified the proper CIs).
3. **Stakeholder Feedback or Risk Reports**:

   * Feedback from CM procedure reviews to ensure it aligns with stakeholder or systems engineering expectations.

---

By providing the above evidence, a project can confidently demonstrate full compliance with Requirement 5.1.5, ensuring the integrity and accountability of software configuration management processes. Documentation, artifact traceability, audit results, and metrics will collectively validate the implementation and efficiency of configuration control systems.

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
