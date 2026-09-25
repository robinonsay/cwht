# SWE-040 - Access to Software Products

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695417. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products

SWE-040 - Access to Software Products

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695417)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695417&showCommentArea=true&showComments=true#addcomment)

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

3.1.9 The project manager shall require the software developer(s) to provide NASA with software products, traceability, software change tracking information, and non-conformances in electronic format, including software development and management metrics.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-040 History

SWE-040 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.6.1.2 The project shall require the software supplier(s) to provide NASA with all software products and software process tracking information, in electronic format, including software development and management metrics. |
| Difference between A and B | No change |
| B | 3.12.9 The project manager shall require the software supplier(s) to provide NASA with software products and software process tracking information, in electronic format, including software development and management metrics. |
| Difference between B and C | Changed "supplier(s)" to "developer(s)";  Added requirement to provide traceability and non-conformances;  Changed "process" tracking to "change" tracking.  SWE-047 and SWE-043 merged into this requirement. |
| C | 3.1.9 The project manager shall require the software developer(s) to provide NASA with software products, traceability, software change tracking information, and nonconformances, in electronic format, including software development and management metrics. |
| Difference between C and D | No change |
| D | 3.1.9 The project manager shall require the software developer(s) to provide NASA with software products, traceability, software change tracking information, and non-conformances in electronic format, including software development and management metrics. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

All software products acquired for NASA projects are to be made available in electronic format so they can be delivered accurately and used efficiently as part of the project. The electronic availability of the software work products, and associated process information, facilitates post-delivery testing that is necessary for assessing as-built work product quality, and for the porting of products to the appropriate hosts. Electronic access to software projects reduces NASA's project costs.

This access also accommodates the longer-term needs for performing maintenance, including defect repairs and software component augmentations, assessing operation or system errors, addressing hardware and software workarounds, and allowing for the potential reuse of the software on future NASA projects.

Electronic access is needed during all phases of the software development life cycle. This enables software supplier activities to be monitored to assure the software work products are being developed efficiently and that the end products that are called for in the project and software requirements are produced. Appropriate use of software project insight (see [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight)), which is in part enabled by electronic access to the in-process products, allows NASA to detect problems early and to take corrective action if necessary.

This requirement ensures NASA receives critical software products, traceability data, change tracking information, non-conformance reports, and metrics in electronic format to enable:

1. **Transparency and Progress Monitoring:** Provides full visibility into software development activities, ensuring alignment with project requirements and milestones.
2. **Traceability and Risk Management:** Facilitates smooth tracking of requirements, changes, and non-conformances throughout the system lifecycle.
3. **Data-Driven Decisions:** Promotes efficient decision-making and risk mitigation by relying on robust metrics and electronic data.
4. **Efficient Collaboration and Auditing:** Streamlines collaboration with developers and supports oversight activities using readily accessible electronic data.

This requirement ultimately strengthens NASA’s ability to oversee software development projects, ensuring quality, reliability, and efficiency while enabling projects to deliver mission-critical outcomes.

This requirement emphasizes the importance of obtaining essential software artifacts and related information in **electronic format** to ensure effective communication, oversight, and management of software development activities. The rationale behind this requirement is to establish accountability, ensure transparency, enable efficient tracking and auditing, and facilitate data-driven decision-making throughout the software development lifecycle. These activities support both internal project monitoring and the broader mission assurance goals of NASA.

## 2.1 Ensures Transparency and Accessibility

The provision of software products, traceability, and development metrics in electronic format allows NASA to have continual visibility into the **state and quality of the software development process**. Transparency ensures:

* NASA can monitor progress at every stage of development.
* Project managers, software assurance personnel, and stakeholders gain easy access to software status and history, improving the ability to manage risks and make informed decisions.

#### **Why Electronic Format Matters:**

* Electronic delivery ensures software artifacts are consistently organized, searchable, and transferable between stakeholders and project phases (e.g., requirements analysis, design, implementation, testing, deployment).
* It facilitates automated tools and workflows for evaluating software traceability, non-conformance reports, and metrics without relying on manual review processes.

## 2.2 Promotes Traceability Across the Lifecycle

**Traceability** refers to tracking how software requirements are mapped throughout the design, development, testing, and deployment phases. This ensures:

* Every software component aligns with its corresponding system, subsystem, and mission-level requirements.
* Gaps in requirement fulfillment are identified early and corrected efficiently.

Tracking information in **electronic format** provides assurance that:

* Requirements are properly traced throughout the lifecycle, enabling verification and validation processes to confirm compliance.
* Design decisions align with mission objectives and goals, and their rationale remains documented for future reference.

#### **Implications of Traceability:**

Traceability data helps NASA:

* Detect incomplete or inconsistent requirements implementation early.
* Maintain alignment between requirements changes and corresponding code, tests, or documentation updates during development.

## 2.3 Facilitates Software Change Tracking

Software systems are dynamic, evolving with new requirements, bug fixes, and design changes. These updates must be tracked through **change management processes** to:

* Ensure the integrity of the software product during development.
* Limit unintended consequences arising from modifications (e.g., introducing regressions or breaking dependencies).
* Provide a documented record of all changes for auditing purposes.

Change tracking data in **electronic format** allows:

* Review of changes in real-time.
* Faster identification of potential risks from particular modifications.
* Better communication between NASA project teams and software developers.

#### **Why This Matters:**

* Electronic storage ensures version histories, impact assessments, and rationale for changes are instantly available for review, even across distributed teams.
* Centralized change tracking enhances collaboration and minimizes confusion between development teams and stakeholders.

## 2.4 Tracks Defects and Non-Conformances

Non-conformance reports (NCR) document deviations from requirements, specifications, or standards and often hold key insights into software quality and reliability. By requiring non-conformance data in electronic format, NASA ensures:

* Defects and issues are captured systematically.
* Impact assessments, root cause analyses, and corrective actions are consistently documented and accessible.
* Historical records of non-conformances are maintained for future audits or lessons learned.

#### **Benefits of Electronic Non-Conformance Reports:**

* Enables better prioritization of critical defects and issues based on severity, frequency, or impact on mission requirements.
* Supports analysis efforts by allowing NASA to identify recurring patterns or systemic process deficiencies.

## 2.5 Enables Data-Driven Decision-Making Using Metrics

Software development and management metrics provide **quantitative insights** into the performance, progress, and quality of the development effort. Key examples include:

* Defect density.
* Requirements coverage.
* Code churn (changes to code over time).
* Schedule adherence (tracking progress against planned timelines).
* Effort expenditure (resource utilization).

#### **Why Metrics Are Essential:**

* Metrics provide the baseline for monitoring progress, identifying risks, and determining where corrective actions may be necessary.
* When consistently reported in electronic format, metrics can be:
  + Easily aggregated for project-level overviews.
  + Integrated into automated dashboards for real-time monitoring.

## 2.6 Streamlines Collaboration Between NASA and Developers

The ability to share software products and associated information in electronic format enhances collaboration by:

* Reducing delays caused by manual data sharing or review processes.
* Ensuring alignment between NASA, developers, and suppliers on project milestones and deliverables.
* Creating a unified record of the software lifecycle that can be used across distributed teams.

For example:

* Electronic traceability matrices reduce the effort required to manually check requirements coverage.
* Sharing change tracking files or defect reports electronically avoids communication bottlenecks and enables rapid resolution of outstanding issues.

## 2.7 Enables Efficient Auditing and Oversight

The electronic availability of software products, traces, change tracking information, and metrics supports both **internal audits** and **external surveillance activities.** Auditors and project managers can:

* Perform gap analyses using well-organized data files without requiring additional manual intervention.
* Use automated tools for checking compliance with project requirements and NASA standards.
* Verify contract deliverables against agreed milestones and traceability information.

#### **Why Auditing is Important:**

Efficient audits improve project accountability, identify process deficiencies, and ensure deliverables meet mission-critical requirements.

## 2.8 Aligns with NASA Requirements and Standards

Requiring electronic delivery of artifacts supports compliance with NASA document standards, such as **NPR 7150.2** [083](#_tabs-<p></p>) and **NASA Procedural Requirements for Software Engineering.** It ensures data is provided in formats compatible with tools and workflows approved by NASA.

#### **Applicable Standards:**

* [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) -  Mandates electronic access for source code and associated data.

# 3. Guidance

This requirement highlights the critical need for NASA project teams to gain **appropriate levels of electronic access** to the software supplier's work products, tools, and processes. This access is essential for NASA to exercise its **insight** and **oversight** responsibilities effectively during procurement, development, and life cycle management of software. Proper electronic access facilitates transparency, traceability, auditing, and collaboration, enabling successful delivery of mission-critical software.

This requirement ensures NASA can access software work products in electronic format, enabling better collaboration, monitoring, and oversight responsibilities throughout software development. By tailoring the access methods to project size and scope, carefully defining contract requirements, and maintaining strong security controls, NASA can ensure full traceability, compliance, and informed decision-making while minimizing risks. The electronic provision of software artifacts is an essential enabler for completing projects efficiently and improving mission success.

This improved guidance refines the content and provides actionable advice for implementing this requirement in small projects, contracted developments, and inter-Center collaborations.

## 3.1 Key Importance of this requirement

### 3.1.1 Supports Insight and Oversight Roles:

Electronic access ensures that NASA teams can monitor and evaluate supplier activities without unnecessary delays or disruptions. By providing tools and documentation in electronic format, suppliers enable:

* **Insight** into work products and processes (e.g., viewing progress, metrics, and compliance).
* **Oversight** responsibilities, such as reviews, audits, testing validations, and decision-making during critical phases.

### 3.1.2 Safeguards Accountability:

Providing work products electronically aids the traceability of requirements, decisions, and software artifacts. NASA can clearly link software outputs to project specifications and assess compliance with system requirements.

### 3.1.3 Streamlines Collaboration:

Electronic access reduces administrative bottlenecks, improves communication flow, and enables real-time data sharing between NASA teams and external suppliers, or among internal development teams.

## 3.2 Considerations in Implementing this requirement

When establishing requirements for electronic access, the following factors must be considered:

### 3.2.1 Nature of Software Acquisition:

This requirement applies to software procurement efforts, including:

* **Reuse of existing software** (legacy systems or COTS—Commercial Off-the-Shelf software).
* **Modification of existing software.**
* **Development of new software.**
* **Subcontracted software elements.**

### 3.2.2 Security and Risk Mitigation:

Suppliers and NASA teams must collaborate to assess risks associated with electronic access. The methods chosen should protect:

* **Proprietary supplier information.**
* **Mission-sensitive data.**
* **Safety-critical software components and their data.** Ensure chosen methods are compliant with NASA's data security standards.

## 3.3 Recommended Methods for Providing Electronic Access

Suppliers can satisfy electronic access requirements in various ways, each suited to different project complexities and risks:

### 3.3.1 Direct Access to Supplier Repositories:

* Access the supplier’s **configuration management system** or document repositories.
* Benefits:
  + Minimal setup effort, as suppliers can provide controlled access using existing permission protocols (e.g., passwords and roles).
  + Real-time updates to software products, metrics, and documents.
* Risks:
  + Requires strong security controls to prevent unauthorized access or inadvertent alterations by NASA personnel.

### 3.3.2 Dedicated Server for NASA Access:

* Suppliers may establish a **dedicated server** accessible only to NASA personnel.
* Benefits:
  + Limits access to specific files, code, and documents aligned with NASA's monitoring and oversight needs.
  + Reduces concerns about exposing unrelated or proprietary supplier data.
* Drawbacks:
  + The supplier must invest additional resources to set up, maintain, and update server contents.

### 3.3.3 Periodic Updates via Magnetic Media:

* Provide access at designated intervals through portable media (e.g., thumb drives, external storage devices).
* Benefits:
  + Useful for projects with limited connectivity or lower volumes of information transfer.
* Drawbacks:
  + Risk of outdated data due to infrequent updates.
  + Limited applicability for large-scale projects requiring continuous monitoring.

## 3.4 Controls and Protections

To ensure the proper use and protection of electronically accessed information, both the supplier and NASA must implement adequate controls:

1. **Access Restrictions:**
   * Use role-based permissions to control NASA's access to sensitive or proprietary supplier data.
2. **Update Management:**
   * Include provisions in the contract or agreement to ensure that electronic access points (repositories or servers) are updated regularly with the latest versions of files and data.
3. **Confidentiality Protections:**
   * Address concerns about proprietary COTS and embedded software using well-negotiated clauses in the contract. Ensure access rights cover required data without breaching third-party license agreements.

## 3.5 Suggested List of Items for Electronic Access

When preparing the contract SOW or internal agreement, include the following items (as applicable based on project needs):

### 3.5.1 Software, Executable, and Source Code:

* Provide access to the delivered code (source and executable) along with the necessary build tools.
* Include delivery schedules and documentation to ensure correct execution.
* Reference [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) for further details.

### 3.5.2 Data Definitions and Data Sets:

* Provide clear descriptions, formats, and filing standards for data (e.g., names, types, units).
* Include usage conventions as outlined in Topic [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary)**.**

### 3.5.3 Ground and Build Products:

* Differentiate between:
  + **Ground products:** Software for lab or testing environments.
  + **Build products:** Incremental builds and final product including descriptions of future additions.
* Reference relevant documentation like Topic [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)**.**

### 3.5.4 Build Tools and Environments:

* Deliver descriptions of tools necessary to operate the builds, including proprietary, sole-source, or COTS tools.
* See [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) for accreditation guidance.

### 3.5.5 Software Documentation:

* Include User Manuals and Version Description Documents sufficient for software operation in flight and ground environments.
* See [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) and [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document)**.**

### 3.5.6 Metric Data:

* Provide access to software progress and management metrics (e.g., defect density, requirements coverage, schedule adherence).
* See details in:
  + [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data)
  + [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)
  + [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)
  + [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report)

### 3.5.7 Software Cost Data:

* Supply cost parameters in both structured financial reports and summary formats.
* This data must support future planning activities for updates and maintenance.

### 3.5.8 Software Database(s):

* Include parameters, definitions, data sources, and lifecycle update plans as appropriate.

### 3.5.9 Results and Procedures for Software Testing:

* Deliver comprehensive **test plans**, reports, and results, including any additional validation and verification activities.
* Reference testing requirements in
  + [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test)
  + [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports)
  + [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)
  + [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing)
  + [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures)

### 3.5.10 Code Static Analysis Results:

* Provide access to results of static analysis activities performed on the developed code.
* See [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis)**.**

## 3.6 Tailoring for Small Projects

For small-scale projects, simplify the list of items for electronic access by prioritizing high-value deliverables:

* Focus on essentials like source code, executable files, key metrics, test reports, and documentation tied to mission-critical components.
* Leverage existing tools and collaboration platforms (e.g., cloud repositories) for effective data sharing without heavy resource overhead.

## 3.7 Additional Guidance

Additional guidance related to software product and software process information and reporting can be found in the following related requirements in this Handbook. As you decide how to capture, format, and store the software product and process information, consider how your decisions will satisfy or impact the need to provide electronic access to the information to NASA. 

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Project Monitoring and Control](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Monitoring+and+Control)      * [Contracting](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Contracting) |

# 4. Small Projects

Electronic access to software work products and software process tracking information is required for every project. However, access plans need to be written to a level of detail (e.g., limited schedules, minimum deliveries) appropriate for and commensurate with the size, complexity, risk, and safety aspects of the project.

For small projects, this requirement's access plans should balance the need for transparency with the project’s scale and risk level. By limiting deliverables, simplifying access mechanisms, and tailoring to the project’s nature, you can ensure compliance with NASA’s requirements while optimizing team efficiency. Proportional and focused electronic access plans enable small projects to meet their goals without unnecessary complexity or resource strain.

Electronic access to software work products and process tracking information is **required for all projects**, regardless of size. For small projects, it is critical to tailor the access plans and delivery mechanisms to align with the **project’s scope, complexity, risk profile**, and **safety-criticality**, while avoiding unnecessary overhead. This improved guidance outlines how access requirements can be optimized for small-scale projects, ensuring compliance with NASA standards while maintaining efficiency and resource balance.

## 4.1 Key Principles for Small Projects

1. **Simplify Access Plans:**

   * Develop plans that are proportional to the size and scope of the project. For smaller projects, **limit schedules, focus on minimal yet essential deliverables**, and avoid overly complex access mechanisms.
2. **Prioritize Mission-Critical Elements:**

   * Focus on electronic access for **critical components** of the software, including safety-critical and high-risk items that directly impact mission success.
3. **Ensure Transparency Without Excessive Overhead:**

   * Electronic access should provide NASA with necessary visibility into work products and processes, but avoid unnecessary complexities (e.g., over-engineered access systems).
4. **Leverage Existing and Scalable Tools:**

   * Use simple yet reliable mechanisms for access, such as cloud-based repositories, direct system access, or periodic deliveries via magnetic media, tailored to the project’s needs.

## 4.2 Strategies for Electronic Access in Small Projects

### 4.2.1 Simplified Access Plans

* Access plans should include only the **essential elements** needed to monitor progress and verify requirements compliance.
* **Examples of essential items:**

  + Final executable and source code.
  + Traceability matrix for requirements.
  + Results of key testing procedures (e.g., unit tests, integration tests).
  + Basic metrics (e.g., defect tracking, schedule adherence).
* **Approach:** Focus on **reduced quantity** of deliverables and limit reporting frequency to the project's critical points (e.g., milestone completions).

### 4.2.2 Practical Delivery Mechanisms

Small projects can benefit from simplified electronic access methods that reduce setup and maintenance efforts:

* **Direct Access to Repository:** If the supplier is using an existing configuration management or document repository, provide NASA teams restricted access to the relevant files.

  + Example: Tools like GitHub, Bitbucket, or cloud storage solutions that have minimal setup requirements.
* **Periodic Deliveries via Magnetic Media:** For projects that do not require continuous access or frequent updates, suppliers can deliver data using thumb drives or secure external storage devices at designated intervals (e.g., milestone completions).
* **Dedicated Cloud-Based Collaboration Tools:** Use collaboration platforms (e.g., SharePoint, Google Drive) for sharing files without the overhead of setting up dedicated servers.

### 4.2.3 Proportional Scope of Deliverables

For small projects, focus on **core elements** and avoid requiring extensive items unless absolutely necessary:

* **Minimum Deliverables:**

  + Final source code and executable files.
  + Testing results for key functionalities or high-priority components.
  + Summary-level metrics tracking (e.g., defects resolved, testing coverage, adherence to schedule).
  + Documentation sufficient for software operation (e.g., basic user manual for delivered software).
* **Optional Deliverables:**

  + Static code analysis results (if safety-critical or mission-critical software).
  + Full traceability matrices for requirements (only for projects with significant risk or safety-critical implications).

### 4.2.4 Risk-Based Access Plans

In small projects, the complexity and criticality of the system being developed drive the level of access:

* **Low-Risk Projects:**

  + Focus on occasional reporting (e.g., via periodic snapshots of progress and simple access mechanisms like monthly updates).
  + Use shared repositories or delivered reports.
* **High-Risk or Safety-Critical Projects:**

  + Prioritize real-time electronic access to critical information (e.g., online access to build progress or defect tracking systems).
  + Increase access frequency and require traceability matrices in electronic formats.

## 4.3 Examples of Tailored Plans for Small Projects

### Example 1: Internal Tool Development (Non-Safety Critical)

A project developing internal administration tools:

* **Critical Deliverables:**
  + Final source code and executable files.
  + Progress metrics (e.g., adherence to schedule, defect counts).
  + User manual/documentation.
* **Access Method:**
  + Periodic deliveries via thumb drives or email file-sharing tools.
  + No need for real-time repository access or extensive testing procedures.

### Example 2: Safety-Critical Lab Software

A project creating a software tool for simulations in a lab setting:

* **Critical Deliverables:**
  + Source code and executable files synchronized to key milestones.
  + Verification and testing results (e.g., lab performance tests).
  + Traceability matrix for top-level requirements associated with safety-critical components.
* **Access Method:**
  + Direct access to a secure cloud-based repository for continuous updates.
  + Monthly sharing of testing and defect resolution reports.

## 4.4 Implementation Tips

1. **Define Reasonable Access Schedules:**

   * For small projects, establish milestone-based electronic access deadlines rather than continuous or real-time monitoring.
2. **Collaborate with Stakeholders:**

   * Work closely with suppliers and stakeholders to assess the project’s size and criticality before finalizing access plans.
3. **Integration with SOW:**

   * Include the access plan and minimum deliverables in the contract Statement of Work (SOW) with clear scope and provisions for updates.
4. **Emphasize Simplicity:**

   * Avoid excess reporting or redundant deliverables by focusing on essential project artifacts.

## 4.5 Tailoring for Small Projects

For small-scale projects, simplify the list of items for electronic access by prioritizing high-value deliverables:

* Focus on essentials like source code, executable files, key metrics, test reports, and documentation tied to mission-critical components.
* Leverage existing tools and collaboration platforms (e.g., cloud repositories) for effective data sharing without heavy resource overhead.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-018)

  [Information and Communication Technology Accessibility](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2800&s=2A "Click to open in new window")

  NPR 2800.2A, Office of the Chief Information Officer, Effective Date: August 05, 2020, Expiration Date: August 05, 2025
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
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-329)

  [Software Measurement Guidebook,](https://ntrs.nasa.gov/search.jsp?R=19980228474 "Click to open in new window")

  Technical Report - NASA-GB-001-94 - Doc ID: 19980228474 (Acquired Nov 14, 1998), Software Engineering Program,
* (SWEREF-336)

  [Software Metrics Capability Evaluation Guide,](http://www.dtic.mil/docs/citations/ADA325385 "Click to open in new window")

  Software Technology Support Center (STSC) (1995), Hill Air Force Base. Accessed 6/25/2019.
* (SWEREF-554)

  [Accident Investigations/Information Technology and Database Security](https://llis.nasa.gov/lesson/1448 "Click to open in new window")

  Public Lessons Learned Entry: 1448.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

A documented lesson from the NASA Lessons Learned database illustrates the value of having appropriate electronic access to the necessary software products and processes and their results:

* **Lesson Learned (Starliner CFT):** **Deep insight into suppliers and subcontractors is essential; shared accountability must be consistently applied.**

  **Project Context:**  
  Derived from Starliner CFT Investigation.

  **Problem/Observation:**  
  Limited access to subcontractor data and decisions reduced NASA’s ability to identify emerging risks; shared accountability and oversight were inconsistently understood.

  **Contributing Factors:**

  + Contract structures did not guarantee access to engineering artifacts (logs, design rationales, hazard analyses).
  + Variability in supplier reporting cadence and technical forum participation.

  **Impacts:**

  + Delayed discovery of risks and slowed anomaly resolution.
  + Reduced confidence in subsystem readiness and interactions.

  **Recommended Practices (Aligned to SWE‑039/040):**

  + Define **supplier insight plans** (artifacts, cadence, forums, liaisons).
  + Require **data‑access clauses** for engineering logs, design reviews, anomalies, and RCCA artifacts.
  + Maintain **joint technical boards** with clear decision authority and escalation paths.

  **Actionable Checks:**

  + Insight plans and schedules are baselined and audited.
  + Contracts include explicit data/insight language; access is exercised.
  + Joint boards’ minutes document supplier actions and accountability.

* ### **Lessons Learned: Class D Lean SMA Resulting in Reduced Insight and Oversight Into Software Engineering**

  **Problem/Observation:**  
  Lean Safety and Mission Assurance (SMA) resourcing on a Class D mission led to reduced institutional insight and oversight into software engineering activities. The Anomaly Review Board (ARB) noted that insufficient SMA presence contributed to unrecognized risks in flight software (FSW), fault protection (FP), and COTS integration.

  **ARB Context:**  
  The ARB explicitly stated that:  
  “Achieving appropriate institutional oversight of Class D missions is a challenge… and needs to be explicitly planned for, addressed, and right sized.”

  **Contributing Factors:**  
  • FP and FSW were never elevated as major risks to project management, limiting visibility and engineering attention.  
  • Monthly status reviews were discontinued to save cost, reducing opportunities for institutional insight.  
  • JPL’s onsite resident at Lockheed Martin was removed and never replaced, eliminating a key source of direct oversight.  
  • COTS subsystems were integrated with insufficient SMA rigor, limiting understanding of behavioral risks.

  **Resulting Impacts:**  
  Reduced insight limited the project’s ability to detect emerging software risks, independently assess contractor activities, and ensure engineering completeness. Several issues surfaced late or only after anomalies occurred, increasing mission risk during integration and operations phases.

  **Relevant SWEHB Guidance:**  
  Even when tailoring for Class D, the SWEHB maintains core expectations for software insight and supplier oversight.  
  • SWE‑039 and SWE‑040 (Supplier Insight/Monitoring) require oversight proportional to risk, even when processes are tailored.  
  • Projects must ensure adequate engineering insight into outsourced, subcontracted, or COTS-based FSW components regardless of mission class.

  **Lesson Learned:**  
  Class D tailoring should not eliminate essential SMA insight mechanisms. Institutional oversight, supplier monitoring, and direct engagement with development teams must be right‑sized—but not removed. Ensuring that FP, FSW, and COTS software risks are actively identified, reviewed, and monitored is critical to maintaining mission readiness and preventing late‑phase discoveries.
* **Accident Investigations/Information Technology and Database Security. Lesson No. 1448**[554](#_tabs-<p></p>): "Electronic tools ... should have a secure, automated, user-friendly access system". While this lesson was derived from the Columbia Accident Investigation activities, the recommendations are perceived as applicable in many situations. Consider the use of the following recommendations when securing electronic access to the projects' products and processes:
  + "Do not allow computer connectivity and cross-platform issues to prevent efficient access between dispersed members.
  + "Identify a single authority to integrate and manage security systems and make sure they are compatible.
  + "Maximize the use of COTS tools to enhance product support and rapid startup."
  + ...
  + "Identify which tools will contain ITAR data and, therefore, require 2-factor security.
  + "Define the...Security Policy upfront – some items may require more security than others.
  + "Make the security access tool web-enabled with sufficient security protection so ...(users)...can have remote access...."

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Communicate FSW problems found in BVT to the I&T team](https://software.gsfc.nasa.gov/lesson-details/113/). **Lesson Number 113**: The recommendation states: "Communicate FSW problems found in Build Verification Testing (BVT) to the I&T team."

# 7. Software Assurance

**SWE-040 - Access to Software Products**

3.1.9 The project manager shall require the software developer(s) to provide NASA with software products, traceability, software change tracking information, and non-conformances in electronic format, including software development and management metrics.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that software artifacts are available in electronic format to NASA.

## 7.2 Software Assurance Products

Software Assurance (SA) products are the deliverables created from SA activities to provide oversight, document compliance, and evaluate risks associated with this requirement. The goal of these products is to ensure that developers meet the project's reporting obligations and that all artifacts, traceability, change tracking, non-conformance data, and metrics meet NASA’s requirements and standards.

Below is a comprehensive list of the software assurance products and their descriptions, categorized by the primary elements within this requirement.

### 7.2.1 SA Review Documentation for Software Products

**SA Product:**

* **Software Deliverables Evaluation Report**
  + **Purpose**: Evaluates the completeness, correctness, and compliance of all software deliverables submitted by the developer.
  + **Contents**:
    - A checklist of required deliverables (e.g., source code, design documentation, test artifacts, plans, operational manuals).
    - Findings from SA reviews of deliverables for compliance with NASA standards (e.g., NPR 7150.2 [083](#_tabs-<p></p>) , NASA-STD-8739.8 [278](#_tabs-<p></p>) ).
    - Identified discrepancies or quality issues, with recommendations for improvement.

**SA Product:**

* **Deliverables Compliance Tracking Matrix**
  + **Purpose**: Tracks the status of all delivered software products against project requirements.
  + **Contents**:
    - A matrix mapping required software products/deliverables to their respective due dates and submission status.
    - Delivery timeline compliance information (on-time vs. late submissions, missing products).
    - Status of non-compliant or incomplete software products.

**SA Product:**

* **SA Acceptance Records**
  + **Purpose**: Includes the SA team's acceptance or conditional acceptance of software deliverables.
  + **Contents**:
    - Confirmation of whether deliverables met the project's electronic format and quality requirements.
    - A log of any rework or follow-up actions required for incomplete deliverables.

### 7.2.2 SA Analysis of Requirements Traceability

**SA Product:**

* **Traceability Matrix Review Report**
  + **Purpose**: Evaluates the completeness and accuracy of the software developer's traceability matrix.
  + **Contents**:
    - Verification of forward and backward traceability (requirements → design → code → test → verification).
    - Identification of existing traceability gaps, orphaned requirements, or extraneous design/code artifacts with no requirement.
    - Risk analysis for unresolved traceability issues.

**SA Product:**

* **Traceability Audit Findings Log**
  + **Purpose**: Documents findings from traceability audits conducted by SA personnel.
  + **Contents**:
    - Gaps found in the traceability matrix and corrective actions assigned to developers.
    - Tracked resolution status of identified gaps or incomplete mapping of requirements.
    - Metrics on traceability coverage, such as the percentage of requirements fully traced.

### 7.2.3 SA Oversight of Software Change Tracking

**SA Product:**

* **Software Change Request Review Report**
  + **Purpose**: Evaluates the adequacy of the software developer's change tracking processes and artifacts.
  + **Contents**:
    - Review of change requests (CRs) logs to verify detail, completeness, and impact analysis.
    - Assessment of the effectiveness of the developer’s configuration management (CM) and change tracking systems (e.g., Git, JIRA).
    - Findings from audits of change processes, including unauthorized or undocumented changes.

**SA Product:**

* **Change Request Closure Status Report**
  + **Purpose**: Summarizes the rates of change request approval and closure during the project lifecycle.
  + **Contents**:
    - Metrics: Number of CRs submitted, approved, rejected, open, closed, or overdue.
    - Average time to approve and resolve change requests.
    - Trends observed in change requests, particularly in safety-critical areas.

**SA Product:**

* **Configuration Management Audit Report**
  + **Purpose**: Audits compliance with software configuration management (CM) plans, including the integrity of baselines and CM records.
  + **Contents**:
    - Findings on whether configuration baselines are complete and properly version-controlled.
    - Review outcomes of software versioning and documentation updates linked to change requests.
    - Metrics on configuration audit compliance rates (e.g., CM plan adherence).

### 7.2.4 SA Oversight of Non-Conformance Management

**SA Product:**

* **Non-Conformance Report (NCR) Review Log**
  + **Purpose**: Tracks and evaluates non-conformance reports (NCRs) logged by the software developer.
  + **Contents**:
    - A log of NCR details, including description, root cause analysis (RCA), resolution status, and closure status.
    - Metrics summarizing NCR status (e.g., resolved, unresolved, deferred, overdue).
    - Analysis of recurring issues or patterns, and associated risks.

**SA Product:**

* **Non-Conformance Root Cause Analysis Assessment**
  + **Purpose**: Reviews the adequacy of the developer’s root cause analyses for non-conformance issues.
  + **Contents**:
    - Assessment of RCA depth and documentation of corrective actions.
    - SA findings on whether similar non-conformances can be mitigated in the future (lessons learned).
    - Recommendations for non-conformance process improvements.

**SA Product:**

* **Non-Conformance Resolution Metrics Report**
  + **Purpose**: Tracks the resolution of non-conformance reports to assess developer responsiveness.
  + **Contents**:
    - Metrics: Percentage of resolved NCRs, average time to closure, recurring issues.
    - Trends in NCRs (e.g., criticality of issues, recurrence frequency).
    - Any open NCRs flagged as project risks by SA.

### 7.2.5 SA Review of Software Metrics

**SA Product:**

* **Software Metrics Evaluation Report**
  + **Purpose**: Reviews and evaluates software development and management metrics provided by the developer.
  + **Contents**:
    - Review of provided metrics, such as defect density, test coverage, requirement completion rates, and iteration velocity.
    - Analysis of metric trends indicating risks, such as delays, unaddressed defects, or incomplete testing.
    - Comparisons of reported metrics to project plans and baselines, highlighting deviations.

**SA Product:**

* **Software Project Health Dashboard**
  + **Purpose**: Summarizes key software metrics and provides a high-level view of project health for management.
  + **Contents**:
    - Key metrics displayed in an easy-to-read format (e.g., defect density, on-time delivery rates, testing coverage).
    - Identified risks or metrics-related concerns requiring management attention (e.g., high open defect rates).

**SA Product:**

* **Recommendations Report for Metrics Improvement**
  + **Purpose**: Provides actionable recommendations to the developers for improving the quality and consistency of reported metrics.
  + **Contents**:
    - Findings on gaps or inconsistencies in provided metrics.
    - Suggestions for implementing automated metric generation or improved collection practices.

### 7.2.6 SA Products Summary by Category

| **Category** | **SA Product** | **Purpose** |
| --- | --- | --- |
| **Software Products** | Deliverables Evaluation Report, Compliance Tracking Matrix, SA Acceptance Records | Ensure completeness and compliance of delivered software products. |
| **Traceability** | Traceability Matrix Review Report, Traceability Audit Findings Log | Ensure end-to-end requirement, design, and test case coverage and address traceability gaps. |
| **Change Tracking** | Software Change Request Review Report, Change Request Closure Status, Configuration Management Audit Report | Ensure proper tracking, approval, and resolution of software changes. |
| **Non-Conformance Management** | NCR Review Log, RCA Assessment Report, NCR Resolution Metrics Report | Track and evaluate the lifecycle of non-conformance issues. |
| **Software Metrics** | Software Metrics Evaluation Report, Software Project Health Dashboard, Recommendations Report | Provide a high-level summary and analysis of development metrics, highlighting risks and trends. |

  

### **Goals of SA Product Development**

1. **Evaluate compliance:** Ensure developers provide all software products, tracking logs, non-conformance data, and metrics in accessible, electronic formats.
2. **Monitor quality:** Assess traceability, change tracking, and non-conformance management processes to confirm quality and integrity.
3. **Identify risks:** Flag issues or discrepancies detected during SA reviews of deliverables and metrics for mitigation.
4. **Provide visibility:** Deliver actionable and comprehensive assessments to project managers and stakeholders.

By generating these products, SA personnel fulfill their oversight responsibilities and provide credible evidence of compliance with this requirement.

## 7.3 Metrics

Software assurance (SA) metrics for this requirement are designed to measure compliance, monitor software product quality, ensure traceability, assess the effectiveness of process controls (e.g., configuration management and change tracking), and capture trends related to non-conformances and development metrics. These metrics provide insight into how well the software developer is meeting this requirement.

1. **Software Deliverables and Product Compliance**
2. **Traceability Metrics**
3. **Change Tracking and Configuration Management Metrics**
4. **Non-Conformance Management Metrics**
5. **Software Development and Management Metrics**
6. **Metrics Oversight Performance**

### 7.3.1 Software Deliverables and Product Compliance

#### 7.3.1.1 Deliverable Completeness Rate

* **Definition**: Measures the percentage of required software products (artifacts, documentation, code, etc.) delivered by the software developer.
* **Formula**:  
  [ \text{Deliverable Completeness Rate} = \left( \frac{\text{Delivered Products}}{\text{Required Products}} \right) \times 100 ]
* **Purpose**: Ensures that all required software products are received on time and in electronic format.
* **Target**: ≥ 95%.

#### 7.3.1.2 Delivery Timeliness

* **Definition**: Percentage of required software products submitted by the software developer on or before their due dates.
* **Formula**:  
  [ \text{Delivery Timeliness} = \left( \frac{\text{Products Delivered On Time}}{\text{Total Products Due}} \right) \times 100 ]
* **Purpose**: Ensures developers are adhering to submission deadlines.
* **Target**: ≥ 90%.

#### 7.3.1.3 Deliverable Quality Compliance Rate

* **Definition**: Measures the percentage of software products reviewed and found compliant with project requirements and standards.
* **Formula**:  
  [ \text{Quality Compliance Rate} = \left( \frac{\text{Compliant Deliverables}}{\text{Total Deliverables Reviewed}} \right) \times 100 ]
* **Purpose**: Monitors the quality and compliance of delivered software products.
* **Target**: ≥ 95%.

### 7.3.2 Traceability Metrics

#### 7.3.2.1 Traceability Matrix Coverage Completeness

* **Definition**: Tracks the percentage of requirements traced to design, code, and tests in the traceability matrix.
* **Formula**:  
  [ \text{Traceability Coverage} = \left( \frac{\text{Requirements Properly Traced}}{\text{Total Requirements Traced}} \right) \times 100 ]
* **Purpose**: Ensures that all requirements are fully traceable through the software lifecycle.
* **Target**: ≥ 100% of all requirements.

#### 7.3.2.2 Traceability Gap Rate

* **Definition**: Measures the number of gaps or deviations (missing mappings) in the traceability matrix.
* **Formula**:  
  [ \text{Traceability Gap Rate} = \left( \frac{\text{Number of Gaps Found}}{\text{Total Requirements Traced}} \right) \times 100 ]
* **Purpose**: Identifies gaps in requirement-to-design-to-verification traceability to ensure completeness.
* **Target**: ≤ 5%.

### 7.3.3 Change Tracking and Configuration Management Metrics

#### 7.3.3.1 Change Request Closure Rate

* **Definition**: Tracks the percentage of submitted change requests (CRs) that are reviewed, processed, and closed.
* **Formula**:  
  [ \text{Change Request Closure Rate} = \left( \frac{\text{Closed Change Requests}}{\text{Total Submitted Change Requests}} \right) \times 100 ]
* **Purpose**: Monitors how effectively and efficiently the project responds to change requests.
* **Target**: ≥ 90% within a reasonable timeframe.

#### 7.3.3.2 Average Time to Close Change Requests

* **Definition**: Measures the average time taken to resolve and close software change requests.
* **Formula**:  
  [ \text{Average Closure Time} = \frac{\sum{\text{Time Taken to Close Each CR}}}{\text{Total Number of Closed CRs}} ]
* **Purpose**: Ensures timely resolution of CRs to avoid delays in development or delivery.
* **Target**: Defined by project-specific thresholds.

#### 7.3.3.3 Configuration Management Audit Compliance Rate

* **Definition**: Measures the percentage of configuration-related artifacts (e.g., baselines, logs) that comply with configuration management (CM) plans.
* **Formula**:  
  [ \text{CM Compliance Rate} = \left( \frac{\text{Compliant Artifacts}}{\text{Total Audited Artifacts}} \right) \times 100 ]
* **Purpose**: Validates adherence to CM processes and ensures integrity of tracked software artifacts.

### 7.3.4 Non-Conformance Management Metrics

#### 7.3.4.1 Non-Conformance Closure Rate

* **Definition**: Tracks the percentage of identified non-conformances that are resolved and closed.
* **Formula**:  
  [ \text{Non-Conformance Closure Rate} = \left( \frac{\text{Closed Non-Conformances}}{\text{Total Non-Conformances}} \right) \times 100 ]
* **Purpose**: Measures the effectiveness of identifying and resolving software issues.
* **Target**: ≥ 90%.

#### 7.3.4.2 Average Time to Resolve Non-Conformances

* **Definition**: Measures the average time taken to resolve and close non-conformance reports (NCRs).
* **Formula**:  
  [ \text{Average Resolution Time} = \frac{\sum{\text{Time Taken to Resolve NCRs}}}{\text{Total NCRs Resolved}} ]
* **Purpose**: Monitors the responsiveness of the development team in resolving issues.

#### 7.3.4.3 Recurring Issue Rate

* **Definition**: The percentage of recurring issues flagged as non-conformances (i.e., issues resolved but reoccurred).
* **Formula**:  
  [ \text{Recurring Issue Rate} = \left( \frac{\text{Recurring Issues}}{\text{Total NCRs}} \right) \times 100 ]
* **Purpose**: Identifies systemic problems in development processes or issue resolution.
* **Target**: ≤ 5%.

### 7.3.5 Software Development and Management Metrics

#### 7.3.5.1 Defect Density

* **Definition**: Measures the number of defects identified per unit of software size (e.g., KLOC or function point).
* **Formula**:  
  [ \text{Defect Density} = \frac{\text{Number of Defects Identified}}{\text{Software Size (KLOC)}} ]
* **Purpose**: Tracks the quality and stability of the software based on defect rates.

#### 7.3.5.2 Test Coverage Rate

* **Definition**: The percentage of code or requirements that have been tested successfully.
* **Formula**:  
  [ \text{Test Coverage Rate} = \left( \frac{\text{Tested Elements}}{\text{Total Testable Elements}} \right) \times 100 ]
* **Purpose**: Evaluates the completeness of testing efforts and identifies untested areas.

#### 7.3.5.3 Defect Resolution Efficiency

* **Definition**: Measures the effectiveness in resolving defects relative to the total number of reported defects.
* **Formula**:  
  [ \text{Defect Resolution Efficiency} = \left( \frac{\text{Resolved Defects}}{\text{Total Reported Defects}} \right) \times 100 ]
* **Purpose**: Tracks the speed and effectiveness of addressing software issues.

### 7.3.6 Metrics Oversight Performance

#### 7.3.6.1 Metrics Reporting Accuracy

* **Definition**: Percentage of reported software metrics that are complete and adhere to measurement criteria.
* **Formula**:  
  [ \text{Metrics Reporting Accuracy} = \left( \frac{\text{Accurate Metrics Reports}}{\text{Total Submitted Metrics Reports}} \right) \times 100 ]
* **Purpose**: Ensures accurate communication of project metrics used for decision-making.

#### 7.3.6.2 Metrics Timeliness Rate

* **Definition**: Percentage of software metrics reports submitted on or before the reporting deadlines.
* **Formula**:  
  [ \text{Metrics Timeliness Rate} = \left( \frac{\text{On-Time Metrics Reports}}{\text{Total Metrics Reports}} \right) \times 100 ]
* **Purpose**: Tracks whether metrics reporting is timely and consistent.

### 7.3.7 Summary of Metrics by Key Aspect

| **Metric Category** | **Examples of Metrics** |
| --- | --- |
| Software Deliverables Compliance | Deliverable Completeness Rate, Delivery Timeliness, Deliverable Quality Compliance Rate |
| Traceability | Traceability Matrix Coverage, Traceability Gap Rate |
| Change Tracking | Change Request Closure Rate, Average Time to Close CRs, Configuration Management Audit Compliance Rate |
| Non-Conformance Management | NCR Closure Rate, Average Time to Resolve NCRs, Recurring Issue Rate |
| Development and Management | Defect Density, Test Coverage Rate, Defect Resolution Efficiency |
| Oversight Performance | Metrics Reporting Accuracy, Metrics Timeliness Rate |

  

Using these Software Assurance metrics, NASA projects can **evaluate compliance** with this requirement ,**track progress**, **identify risks**, and **assess developer consistency** in providing high-quality software products, **change logs**, **non-conformance data**, and **metrics**.

## 7.4 Guidance

**SWE-040 - Access to Software Products**

3.1.9 The project manager shall require the software developer(s) to provide NASA with software products, traceability, software change tracking information, and non-conformances in electronic format, including software development and management metrics.

This requirement ensures that all critical software-related artifacts and data are provided by the software developer in an accessible and electronically managed format. This includes all deliverables such as traceability matrices, change logs, non-conformance reports, and metrics. Software Assurance (SA) personnel play a key role in overseeing the adequacy, completeness, accuracy, and consistency of these artifacts and ensuring compliance with contractual obligations and standards.

Below is an enhanced **SA guidance** for this requirement to ensure effective oversight, traceability, and the delivery of high-quality software products.

1. Confirm that **all software products and process artifacts** required under the project are submitted in the correct formats and contain required information.
2. Ensure the **traceability matrix** is complete, showing clear links between requirements, design, implementation, and verification activities.
3. Verify the accuracy, integrity, and completeness of **software change tracking information**, including configuration management records.
4. Ensure that **non-conformance data** and metrics provided by the developer are reported in standard formats and are actionable.
5. Monitor the collection, review, and analysis of **software development and management metrics** for compliance and project insight.

### 7.4.1 Ensure Delivery and Content Completeness of Software Products

* **Activity**:
  + Verify that software developers provide all required software products in the specified **electronic format** (e.g., PDF, Excel, XML, or project-specific tool-based platforms such as DOORS, JIRA, Git, etc.).
  + Ensure that all deliverables include the necessary supporting documentation, such as development plans, test plans, hazard analyses, software assurance artifacts, etc.
  + Confirm that all submitted products align with NASA’s applicable standards (e.g., **NPR 7150.2** [083](#_tabs-<p></p>) , **NASA-STD-8739.8** [278](#_tabs-<p></p>) ) and contractual requirements.
* **SA Actions**:
  + Perform **checklist-based reviews** to verify the completeness and correctness of all submitted software products and documentation.
  + Cross-check developer deliverables against **contract requirements** to ensure nothing is missing.
  + Communicate discrepancies via findings logs, Review Item Discrepancies (RIDs), or audits as required.
  + Track the delivery schedule for each product and ensure on-time submission.

### 7.4.2 Assess and Analyze Traceability Matrices

* **Activity**:
  + Require the developer to provide an up-to-date **requirements traceability matrix (RTM)** in electronic format that maps all requirements through design, code, testing, and verification.
  + Verify that all **high-level system and subsystem requirements** are traced through all development phases, ensuring:
    - Bi-directional traceability for each requirement.
    - Traceability gaps (e.g., orphaned requirements or missing links) are identified and resolved.
* **SA Actions**:
  + Confirm that traceability matrices fully cover:
    - Requirement-to-design mapping.
    - Requirement-to-code mapping.
    - Test-to-requirement mapping.
  + Perform **spot checks** or full reviews of RTM data to validate completeness and trace back non-conformances to related requirements.
  + Report and track open issues or gaps in traceability until closure.

### 7.4.3 Oversee Software Change Tracking and Configuration Management

* **Activity**:
  + Confirm that the software developer provides **change tracking information** relevant to software updates, defect resolutions, and other modifications.
  + Ensure that changes are logged in a **configuration management tool** and include details such as:
    - Description of the change.
    - Rationale for the change.
    - Approvals and impact analysis.
    - Linkage to affected areas (e.g., design, code, documentation).
  + Monitor adherence to change control processes as specified in the Configuration Management (CM) plan.
* **SA Actions**:
  + Review change requests and audit the change tracking logs periodically to ensure:
    - Each entry is complete and accurate.
    - Changes are evaluated for their impact on safety, functionality, and performance.
  + Confirm that version management and baseline updates are properly maintained and documented.
  + Identify and report inconsistencies or deviations from the change control process.

### 7.4.4 Verify Non-Conformance Reports

* **Activity**:
  + Ensure the developer provides **non-conformance information** in electronic form, including:
    - A description of the non-conformance.
    - Root cause analysis (RCA) and resolution status.
    - Impact on system requirements, design, operations, and safety-critical areas.
  + Confirm that non-conformances are logged in an issue-tracking system and are updated throughout the development lifecycle.
  + Verify that discrepancies align with applicable standards (e.g., **NASA-STD-8739.8**) and are resolved as planned.
* **SA Actions**:
  + Review, approve, and track **non-conformance reports (NCRs)**, verifying:
    - Quality of root cause analysis.
    - Timely resolution of the issues.
    - Updates of related artifacts (e.g., RTMs, design documents) after non-conformance fixes.
  + Communicate unresolved critical issues to project management immediately.

### 7.4.5 Review and Analyze Software Development and Management Metrics

* **Activity**:
  + Ensure that the software developer submits **software development and management metrics**, including (but not limited to):
    - Defect density.
    - Test effectiveness (percentage of requirements verified and validated).
    - Release frequency or iteration velocity.
    - Lines of code (LOC) metrics (e.g., added, modified, removed).
    - Change request resolution rates.
  + Confirm that metrics are provided in consistent digital formats (spreadsheets, dashboards, or tools).
  + Evaluate metrics for completeness, accuracy, timeliness, and trends that might indicate project risks or non-compliance.
* **SA Actions**:
  + Analyze received metrics for trends, potential delays, or risks (e.g., defect resolution stagnation).
  + Compare reported metrics against project standards, historical performance, and planned baselines.
  + Feed insights from metric data into SA status reports.

### 7.4.6 Assess Compliance with Standards and Deliverable Formats

* **Activity**:
  + Ensure compliance with **electronic format requirements** specified in NASA standards (e.g., **NPR 7150.2**, **NASA-STD-8739.8**). Required formats may include:
    - Tool-based (e.g., DOORS for traceability, JIRA for change tracking, Git for software configuration files).
    - Documents (e.g., PDF for plans, Excel for metrics).
    - Machine-readable data (e.g., JSON, XML for logs or processes tracked in tools).
  + Verify that all submissions are organized, accessible, and compatible with project tools/systems.
* **SA Actions**:
  + Validate delivered formats for compliance with the project data standards and update the SA checklist for future submissions.
  + Flag non-compliance issues for correction and resolution timelines.

### 7.4.7 Monitor Communication and Report Oversight Findings

* **Activity**:
  + Communicate discrepancies or gaps identified (e.g., missing data points, incomplete traceability).
  + Document oversight results and provide project-level insights on the adequacy of processes and products.
* **SA Actions**:
  + Provide comprehensive **SA status reports** periodically, summarizing:
    - Current status of developer-provided products (traceability, change logs, non-conformances, metrics).
    - Open issues and risks tied to deliverable submissions.
    - Recommendations to improve deliverable quality and traceability.

### 7.4.8 Expected Products and Objective Evidence for Assurance

| **Deliverable** | **Objective Evidence** | **Purpose** |
| --- | --- | --- |
| **All software products** | Electronic files for submitted software products, version-controlled configuration records. | Confirm completeness, correctness, and compliance of software deliverables. |
| **Requirements Traceability Matrix (RTM)** | RTM documents, bi-directional trace checks (requirements → design → test cases). | Ensure end-to-end traceability for requirements and validate against development plans. |
| **Non-Conformance Reports (NCRs)** | Audit logs of NCRs, root cause analysis documents, non-conformance resolution reports. | Monitor and track issue resolution progress and ensure alignment with required standards. |
| **Change Tracking Logs** | Configuration control logs, change requests (CRs), version management databases. | Ensure completeness and alignment of change control processes with the CM plan. |
| **Software Metrics** | Metrics dashboards/reports, analysis on metrics (e.g., defect density trends, test adequacy rates). | Monitor project health using collected metrics to ensure project milestones are on track. |

By maintaining the above practices and producing the required products and objective evidence, SA can confidently ensure compliance with this requirement while providing valuable oversight and risk reduction for the project.

#### What Needs To Be Accessible?

* Software, executable, and source code
* Models and simulations
* Programmable Logic Device logic and software
* Trade study data, including software tools, is used to help formulate an analysis of alternative results if any scenarios need to be re-run later
* Prototype software, including prototype architectures/designs
* Data definitions and data sets
* Software ground products
* Software build products
* Build tools
* Software documentation, including data presented during any early design reviews
* Metric data
* Software cost data and parameters
* Software database(s)
* Software development environment
* Software Test Scripts and the results of software testing
* Results of software static analysis activities
* Bi-directional traceability for the software products
* Software analyses and compliance data

#### Other documentation and products to consider include:

* Summary and status of all accepted Change Requests to the baselined Software Requirements Specifications.
* Summary and status of all major software capability changes since baselining of the Software Design Documents
* Summary and status of all major software tests (including development, verification, and performance testing).
* Summary and status of all Problem Report written against the software.
* Summary and status of all software requirements deviations and waivers.
* Summary and status of all software user notes.
* Summary and status of all quality measures historically and for this software.
* Definition of openwork, if any.
* Software configuration records define the verified and validated software, including requirements verification data (e.g., requirements verification matrix).
* The final version of the software documentation, including the final Software Version Description document(s).
* Summary and status of any open software-related risks.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) |

# 8. Objective Evidence

Objective evidence consists of documented artifacts, data, and outputs that Software Assurance (SA) personnel can use to assess compliance with this requirement. These artifacts provide verifiable proof that the software developer has delivered the required products, maintained proper traceability, tracked changes, reported non-conformances, and provided software metrics as specified. The **Goals of Objective Evidence Collection** are:

1. Ensure **traceability** is valid and gaps are addressed.
2. Verify that **changes** are tracked and resolved systematically.
3. Confirm **non-conformances** are reported, managed, and resolved effectively.
4. Enable SA personnel to use **metrics** to assess software maturity and development progress.
5. Validate compliance with NASA standards and project requirements for electronic formats.

By focusing on these objective evidence artifacts, Software Assurance personnel can monitor, evaluate, and report on compliance with this requirement while identifying risks and promoting high-quality software deliverables.

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

Below is a list of **objective evidence** categorized by the key elements of the requirement.

## 8.1 Software Products in Electronic Format

**Objective Evidence Required:**

1. **Source Code**:

   * Verified version-controlled source code files (e.g., Git repositories or equivalent).
   * Documentation of code updates, review records, and code quality analysis reports.
   * Release version information and baseline approvals.
2. **Design and Architecture Documentation**:

   * Electronic copies of architectural diagrams, module designs, and interface definitions.
   * Compliant with standards such as NASA-STD-8739.8.
3. **Software Test Artifacts**:

   * Test plans, test case definitions, test results, and associated logs.
   * Test execution reports showing pass/fail status and mapping to requirements.
4. **Supporting Documents**:

   * Software development plans (SDP), software safety plan, and other lifecycle documents.
   * User manuals or operational guides for delivered software.

**Purpose:**  
Ensures all key software products are delivered electronically in the appropriate format and can be independently verified for completeness, correctness, and compliance.

## 8.2 Requirements Traceability

**Objective Evidence Required:**

1. **Requirements Traceability Matrix (RTM)**:

   * A comprehensive matrix linking:
     + High-level system requirements to software design elements.
     + Design elements to code components.
     + Code components to verification tests.
   * Machine-readable formats (e.g., DOORS, Excel spreadsheets, or equivalent).
2. **Traceability Bi-Directional Analysis Reports**:

   * Evidence of forward and backward traceability:
     + Forward traceability: Requirements → Design → Code → Testing.
     + Backward traceability: Testing → Code → Design → Requirements.
   * Reports identifying traceability gaps (or absence thereof).
3. **Updates Related to Requirements Changes**:

   * Documentation showing updates to traceability matrices after requirement changes.
   * Risk logs detailing impacts of traceability gaps, if any.

**Purpose:**  
Confirms that every requirement is traced to design, implementation, and verification activities to ensure full coverage and eliminate orphaned items. Verifies completeness of traceability across the lifecycle.

## 8.3 Software Change Tracking Information

**Objective Evidence Required:**

1. **Change Request Logs**:

   * Details of submitted change requests, including:
     + Description of change.
     + Rationale and priority level.
     + Impact analysis (linked to affected requirements, design, code, and test artifacts).
     + Approval and status (e.g., open, in progress, completed).
2. **Configuration Management Records**:

   * Logs of changes tracked using configuration management systems (e.g., Git, JIRA, or equivalent tool).
   * Documentation for baseline changes and software versioning.
   * Records of release approvals for changes incorporated into deliverables.
3. **Change Tracking Metrics Reports**:

   * Metrics summarizing trends in changes, such as:
     + Average time to evaluate and approve change requests.
     + Number of rejected vs. approved changes.
     + Impact analysis resolution rates.

**Purpose:**  
Ensures all changes to software artifacts are documented, tracked, and managed consistently. Provides oversight on configuration management processes and ensures impacts are addressed appropriately.

## 8.4 Non-Conformance Reports

**Objective Evidence Required:**

1. **Non-Conformance Reports (NCRs)**:

   * Documentation for each non-conformance that includes:
     + Description of the issue or defect.
     + Affected artifacts (e.g., requirements, design, implementation, testing).
     + Root cause analysis (RCA) to identify underlying causes.
     + Resolution details and follow-up actions.
     + NCR status (open, resolved, closed).
2. **Corrective Action Records**:

   * Evidence of corrective actions taken to address non-conformances:
     + Updated design artifacts.
     + Code fixes and retesting results.
     + Documentation of regression testing.
3. **Non-Conformance Metrics Reports**:

   * Reports summarizing non-conformance trends, including:
     + Total number of NCRs identified.
     + Resolution rates and average resolution times.
     + Recurrence rates of non-conformances.

**Purpose:**  
Provides evidence that non-conformances are documented, tracked, analyzed, and resolved appropriately. Confirms issues are reported in a standard electronic format accessible to NASA personnel.

## 8.5 Software Development and Management Metrics

#### Objective Evidence Required:

1. **Development Metrics**:

   * Defect metrics (e.g., defect density, defect trend reports).
   * Coding activity trends (e.g., lines of code added, modified, removed).
   * Percentage of requirements implemented and tested.
2. **Test Metrics**:

   * Test case execution summaries:
     + Pass/fail rates.
     + Coverage metrics (e.g., requirement coverage, code coverage).
   * Regression testing metrics, including defect recurrence rates.
3. **Schedule and Progress Metrics**:

   * Iteration completion rates (e.g., agile sprint velocity metrics).
   * Metrics showing release progress (e.g., milestone completion rates).
4. **Non-Conformance Metrics**:

   * Percentage of non-conformances resolved vs. identified.
   * Average time to resolve non-conformances.
5. **Change Management Metrics**:

   * Approval and closure rates for change requests.
   * Average resolution times for submitted changes.

**Purpose:**  
Ensures measurable insight into software development and management processes. Enables SA personnel to analyze performance trends, identify risks, and ensure developers meet lifecycle expectations.

#### Formats for Objective Evidence

All evidence should be in **electronic formats** that are accessible, consistent, and compatible with project tools and systems. Examples include:

* **Datasets:** Excel spreadsheets, CSV files, or other structured data formats for metrics, NCRs, and traceability matrices.
* **Documentation:** PDF files for plans, reports, and architecture diagrams, along with Word or equivalent editable formats.
* **Tools/Platforms:** Configuration management tools (e.g., Git logs, JIRA tickets), traceability tools (e.g., DOORS), and test management tools (e.g., TestRail or equivalent).

## 8.6 Summary of Required Objective Evidence

| **Category** | **Examples of Objective Evidence** | **Purpose** |
| --- | --- | --- |
| **Software Products** | Source code files, design documentation, test artifacts, development lifecycle documents. | Verifies delivery of key electronic artifacts supporting the development lifecycle. |
| **Traceability** | Traceability matrices, forward/backward trace analysis reports, updates for requirement changes. | Ensures all requirements are linked to design/code/tests and updated when changes occur. |
| **Change Tracking** | Change request logs, configuration management records, metrics on change handling. | Confirms that change requests are tracked, analyzed, and resolved properly. |
| **Non-Conformance Management** | NCRs, corrective action documentation, resolution metrics, RCA reports. | Provides oversight of issue identification, tracking, and resolution for non-conformance items. |
| **Software Metrics** | Development metrics (defects, LOC changes), test execution metrics, progress metrics, change management metrics. | Enables SA to assess software quality, schedule adherence, and defect trends. |
