# SWE-079 - Develop CM Plan

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695458. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan

SWE-079 - Develop CM Plan

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695458)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695458&showCommentArea=true&showComments=true#addcomment)

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

5.1.2 The project manager shall develop a software configuration management plan that describes the functions, responsibilities, and authority for the implementation of software configuration management for the project.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-079 History

SWE-079 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.1.1 The project shall develop a Software Configuration Management Plan that describes the functions, responsibilities, and authority for the implementation of software configuration management for the project. |
| Difference between A and B | No change |
| B | 5.1.2 The project manager shall develop a software configuration management plan that describes the functions, responsibilities, and authority for the implementation of software configuration management for the project. |
| Difference between B and C | No change |
| C | 5.1.2 The project manager shall develop a software configuration management plan that describes the functions, responsibilities, and authority for the implementation of software configuration management for the project. |
| Difference between C and D | No change |
| D | 5.1.2 The project manager shall develop a software configuration management plan that describes the functions, responsibilities, and authority for the implementation of software configuration management for the project. |

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

Software Configuration Management planning encompasses the practices and procedures for administering source code, producing software development builds, controlling change, and managing software configurations for all of the software products, tools, data, and components produced by the project.

A **Software Configuration Management (SCM) Plan** is a critical document that ensures the software development and delivery process is well-controlled, traceable, and efficient. The rationale for requiring such a plan is rooted in maintaining project integrity, reducing risks, and ensuring accountability across the development lifecycle. Here's the **rationale for this requirement**:

---

### **1. Provides Clear Direction and Accountability**

The SCM plan:

* Defines **roles and responsibilities** for all stakeholders in the configuration management process, ensuring there is clear accountability for tasks like version control, change requests, and audits.
* Prevents gaps or misunderstandings by explicitly outlining **process ownership** for implementation, reviews, and updates to the configuration system.

Without an SCM plan, ambiguity in authority or responsibilities can lead to delays, conflicts, or errors in managing software assets.

---

### **2. Ensures Consistent and Controlled Development**

Software projects often involve multiple contributors (developers, testers, integrators), and changes to software artifacts (e.g., source code, requirements, documentation) can introduce errors or inconsistencies. An SCM plan:

* Defines how version control will be managed to prevent **unauthorized changes** or accidental overwrites.
* Establishes processes to ensure consistent **tracking of changes** and clear identification of software baselines (e.g., initial release, incremental updates).

This consistency reduces integration issues, rework, and confusion, especially in complex systems with multiple interdependent components.

---

### **3. Enables Efficient Change Control**

Change is inevitable in software development, whether due to shifting requirements, bug fixes, or functionality enhancements. The SCM plan provides:

* A **structured process to evaluate, authorize, and implement software changes** efficiently.
* Transparency in decision-making through traceable **change request documentation** and approval workflows.

This minimizes disruptions caused by unmanaged changes and ensures stakeholders stay aligned on project updates.

---

### **4. Supports Traceability and Audits**

Software development often demands rigorous **traceability** and compatibility between versions:

* The SCM plan defines the mechanisms to ensure all changes are recorded and traceable to specific requirements, code changes, test cases, and release versions.
* Provides the organization with a foundation for conducting **audits** to confirm compliance with standards (e.g., regulatory, contractual, or organizational).

This traceability is particularly critical in:

* **Safety-critical systems** where every change must be fully documented and justified.
* Projects following industry standards (e.g., ISO, CMMI, or NASA SWE processes).

---

### **5. Facilitates Collaboration Across Teams**

For larger projects involving multiple teams (development, testing, quality assurance, operations), the SCM plan:

* Serves as a **guidance document** to ensure all teams follow the same configuration processes.
* Specifies standard tools, workflows, and repositories, avoiding misalignment or conflicting practices across the organization.

Collaborative efficiency improves as teams share a common understanding of how software artifacts are organized and managed.

---

### **6. Mitigates Risks**

Software projects face risks such as:

* **Loss of artifacts** (e.g., source code, documentation) due to poor version control.
* **Defects** introduced by untested or unapproved changes.
* **Schedule delays** caused by time spent tracking down unaccounted changes or managing conflicts.

An SCM plan mitigates these risks by establishing preventive measures for proper configuration control practices. It also ensures quicker identification and resolution of issues when deviations occur.

---

### **7. Critical for Long-Term Maintenance**

Software projects must often continue beyond the initial delivery for post-release actions like maintenance, upgrades, and fixes. An SCM plan ensures:

* Proper versioning of software artifacts for **repeatability** (e.g., recreating previous configurations for troubleshooting).
* Historical documentation of changes for **future maintainers** or handoffs to other teams.
* Simplified updates and modifications while preserving the integrity of the baseline software.

This makes the system more maintainable and adaptable as requirements evolve.

---

### **8. Regulatory and Quality Compliance**

Many contractual or regulatory frameworks (e.g., NASA, ISO 9001, or DO-178B for aerospace software) mandate documented and enforced SCM practices to ensure software quality and compliance. An SCM plan:

* Demonstrates adherence to industry best practices.
* Satisfies customer, organizational, or legal requirements related to proper management of software configurations.

---

### **Conclusion**

Requiring the development of a Software Configuration Management Plan ensures the project manager proactively addresses challenges related to configuration control, software traceability, team collaboration, and long-term maintainability. It defines the framework for safeguarding software integrity, reducing risks, and ensuring accountability across the project lifecycle, resulting in more efficient delivery, compliance, and quality assurance.

# 3. Guidance

## 3.1 Configuration Management

This guidance provides a streamlined, concise, and clear explanation of Configuration Management (CM) and the Software Configuration Management (SCM) process while emphasizing its critical role in the software development lifecycle, tailoring options, and practical considerations for effective implementation.

Configuration Management (CM) is essential throughout the project lifecycle to:

1. Ensure the **current configuration** of items is known, including their evolving states.
2. Manage, control, and document **changes to configuration items** (e.g., software, hardware, and associated artifacts) efficiently and correctly.

The Software Configuration Management (SCM) Plan defines policies, processes, roles, responsibilities, and tools necessary to implement CM for the project. This plan is developed early in the project lifecycle to establish control over changes as soon as the requirements baseline is approved.

#### **Key Dependencies:**

For detailed actions related to CM, refer to:

* **SWE-187**: Control of Software Items
* **SWE-080**: Track and Evaluate Changes
* **SWE-082**: Authorizing Changes

These dependencies ensure CM activities align with lifecycle requirements and project goals.

## 3.2 Importance and Scope of the Software Configuration Management Plan

Software Configuration Management (SCM) includes both technical and managerial processes. Its primary goal is to maintain consistency across:

* Product requirements.
* Product implementation (software and hardware).
* Associated product configuration information (e.g., documentation and baselines).

The SCM Plan specifies:

* The **functions, responsibilities**, and authority for CM implementation.
* How CM integrates with other project plans (e.g., Software Development Plan (SDP), or Project CM Plan). If standalone, it must describe its relationship with other plans.

#### **Why It Matters:**

1. **Prevents Issues:** CM mitigates risks such as retaining outdated files, losing updates, or introducing unsynchronized changes.
2. **Defines What’s Controlled:** The plan specifies what products fall under configuration management (e.g., source code, documentation, test cases) and how items are added/removed from the CM system.

## 3.3 Configuration Management Plan Goals

The SCM plan serves two critical purposes:

1. **Internal Use:** Guides the project team, monitors progress, defines roles, and schedules CM activities for future phases.
2. **External Use:** Communicates CM expectations and approaches to contractors, ensuring consistency across organizations.

#### **Key Content of the SCM Plan:**

The plan should specify:

* **What to Configuration Manage:** List controlled items, such as:
  + Documentation (requirements, design, test plans).
  + Source code, object code, executables, models, etc.
  + Test environments, tools, and procedures.
  + COTS software and license records.
  + Metrics collected from CM activities (e.g., code defects, effort estimation).
* **How to Configuration Manage:** Defined processes for tracking, auditing, and updating controlled items.
* **When Configuration Management Begins:** Control mechanisms applied once items reach their initial baseline configuration and continue throughout the lifecycle.

## 3.4 Why It's Essential

#### **Internal Benefits:**

* Prevents unauthorized changes.
* Offers traceability for requirements, code builds, and test cases.
* Ensures consistent collaboration across teams.

#### **External Benefits:**

* Aligns contractors to a common CM process.
* Maintains trust in the project’s ability to handle changes systematically.
* Demonstrates compliance with standards and regulatory requirements.

## 3.5 Developing the SCM Plan

#### **Recommended Steps for Creating the SCM Plan:**

1. **Define Configuration Items:** Identify all artifacts requiring CM, including documentation, source code, executables, test tools, environments, and metrics.
2. **Establish Tailoring Options:** Reflect the current project environment and use familiar terms/processes. Justify tailored inclusions/exclusions:
   * When adding SCM requirements, perform a **cost-benefit analysis**.
   * When removing SCM requirements, document rationale, and gain agreement from stakeholders.
3. **Include CM Metrics:** Determine key metrics to track, such as defect density, time estimates, and configuration impacts for evaluation and process improvement.
4. **Account for Classified/Sensitive Data:** Define handling procedures if applicable to the project environment.

#### **Integrated Activities:**

Include **data management** in the SCM plan or a standalone DM plan. This ensures all deliverables are safely stored, organized, and used as needed throughout the lifecycle.

## 3.6 Key Considerations for CM Across the Lifecycle

CM spans the entire lifecycle, including control of:

* **Documentation/artifacts:** Specifications, design docs, traceability matrices, interfaces, and build procedures.
* **Software components:** Source/object code, executables, data formats, simulators, and applicable test suites.
* **Development & test environments:** Tools, processes, and configurations.
* **Safety-critical change evaluation:** Assess impacts of changes on system safety.
* **Release management:** Tracking and documenting all versions of the software and delivery timelines.

#### **Minimum Requirements:**

Every configuration management process must:

* Define the content of released computing system items.
* Produce records demonstrating their configuration for compliance and traceability.

Special attention must be given to **safety-critical changes**, as modifications to these systems could impact operational safety.

## 3.7 Completing the Plan

#### **Process of Development:**

1. Begin during project formulation to ensure an early baseline of control over all artifacts.
2. Refer to best practices and templates like IEEE STD 828-2012 or agency-specific guidance.

#### **Validation and Approval Process:**

* Conduct **peer reviews** of the SCM Plan (SWE-087) to identify gaps, verify compliance, and ensure consistent implementation.
* Review SCM content at major project milestones (e.g., System Requirements Review (SRR), Software Requirements Review (SwRR), Mission Definition Review (MDR)).
* Include **Software Assurance** reviews to confirm adherence to applicable standards and compliance with SWE requirements.

## 3.8 Summary

The SCM Plan is a cornerstone of effective software engineering and lifecycle management. It:

* Reduces risks by providing structured control of configuration items.
* Ensures quality, traceability, and integrity across all phases of development and release.
* Supports collaboration by aligning internal and external stakeholders to consistent CM processes.
* Demonstrates readiness for audits, regulatory compliance, and safety-critical oversight.

By tailoring the plan to the project’s scope and environment while maintaining minimum requirements, teams can optimize CM processes and improve outcomes across the lifecycle.

See also [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items), [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes), [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes),

See also [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management).

## 3.9 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.10 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Configuration Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Configuration+Management) |

# 4. Small Projects

For **small projects**, where team size or budget is limited, Software Configuration Management (SCM) activities should focus on balancing complexity with project risks. While small projects might not require the full formality of a standalone SCM plan, it is still necessary to ensure that SCM processes are in place to manage software artifacts, maintain traceability, and control configuration changes.

#### **Key Guidance for Small Projects:**

1. **Risk-Based Approach to SCM:**

   * Evaluate the size, complexity, and criticality of the project to determine the **level of formality** and **depth of configuration management** needed.
   * Carefully review the recommended SCM content detailed in **7.18 - Documentation Guidance**, but implement only the processes and structures that align with the **risk profile** of the project. This ensures that resources are allocated efficiently without unnecessary overhead.
2. **Simplify SCM Processes and Tools:**

   * Use **simpler tools** (e.g., version control systems like Git, or shared folders with change tracking) that sufficiently satisfy the project’s configuration management needs.
   * Minimize the overhead of tool management by using a single tool for **multiple functions** (e.g., a single platform for version control, change tracking, and code review).
   * Ensure that the tools employed are appropriate for the volume and complexity of configuration items.
3. **Personnel Efficiency:**

   * Assign **multiple SCM roles** to a single team member where resources are constrained. For example, the same individual may oversee version control, change tracking, and release management as long as the workload is manageable and responsibilities are well-defined.
   * Clearly document and communicate the assigned roles and responsibilities to maintain accountability and avoid confusion.
4. **SCM Documentation Alternatives:**

   * Instead of creating a standalone SCM plan, **integrate SCM planning** into a section of the project’s **Software Management Plan (SMP)** or another overarching project document.
   * For organizations managing **multiple small projects**, consider developing a **master SCM plan** that outlines shared SCM processes for all projects. Add project-specific sections to address unique needs or requirements for each project.
5. **Maintain Essential SCM Principles:**

   * Even in a simplified plan, small projects should:
     + Identify the **configuration items** to be managed (e.g., source code, design documents, testing artifacts).
     + Define lightweight but clear **processes** for change control, versioning, and baselining.
     + Track and document all changes to ensure traceability and accountability.
   * Regularly review and adjust SCM processes as the project evolves, ensuring they remain aligned with changing risks and resources.
6. **Balance SCM Formality with Project Needs:**

   * Small projects typically benefit from less formality, but it’s important not to omit critical processes that could jeopardize project outcomes. Examples of tailoring SCM for small projects might include:
     + **Simplified change tracking:** Using a spreadsheet coupled with a version control tool instead of a full-ticketing system.
     + **Direct communication:** Holding regular informal reviews of configuration items within the team to ensure alignment, rather than setting up more formal audits.
     + **Lightweight baselines:** Establishing milestones with minimal documentation—but ensuring key configurations are well-defined and version-controlled before major releases.

### **Conclusion:**

For small projects, the key to effective Software Configuration Management is **proportional implementation**—selecting only those activities and tools that directly address project risks and ensure consistency and control. Scaling down formal processes doesn’t mean ignoring them; instead, using lightweight methods, tools, and multi-role assignments can deliver the benefits of configuration management without overburdening the team or the budget.

By tailoring SCM activities and documentation to the project's scope, small teams can maintain control of their software products while reducing complexity, ensuring scalability, and maintaining alignment with organizational standards.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document, EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. See Chapter 13. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-212)

  [IEEE Guide to Software Configuration Management,](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=89631&tag=1 "Click to open in new window")

  IEEE Computer Society, IEEE STD 1042-1987, 1987.  This link requires an account on the NASA START (AGCY NTSS) system (https://standards.nasa.gov ). Once logged in, users can access Standards Organizations, IEEE and then search to get to authorized copies of IEEE standards.
* (SWEREF-216)

  [828-2012 - IEEE Standard for Configuration Management in Systems and Software Engineering](https://ieeexplore.ieee.org/document/6197683 "Click to open in new window")

  IEEE STD IEEE 828-2012, 2012.,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-526)

  [Software Design for Maintainability](https://llis.nasa.gov/lesson/838 "Click to open in new window")

  Public Lessons Learned Entry: 838.
* (SWEREF-533)

  [Computer Software/Configuration Control/Verification and Validation (V&V)](https://llis.nasa.gov/lesson/1023 "Click to open in new window")

  Public Lessons Learned Entry: 1023.
* (SWEREF-556)

  [Take CM Measures to Control the Renaming and Reuse of Old Command Files (2002)](https://llis.nasa.gov/lesson/1481 "Click to open in new window")

  Public Lessons Learned Entry: 1481.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following lessons from the **NASA Lessons Learned Database** emphasize the critical role of Configuration Management (CM) in ensuring software maintainability, controlling auto-generated code, and preventing issues with file reuse. These lessons, along with additional insights, demonstrate the importance of rigorous CM practices throughout the software lifecycle.

### **1. Software Design for Maintainability**

**Lesson Number: 0838**  
**Key Issue:** Lack of CM adversely impacts software maintainability.

**Description:**  
"Configuration management of software is probably the single most important management and maintainability concept utilized in software development. The utilization of coding standards, documentation standards, release standards, common languages, and other methods will provide for good configuration management. A plan should be developed very early in the development cycle for managing the configuration of the software under development, and that plan should be followed rigorously. If configuration management breaks down, the code under development is doomed to be extremely troublesome when released for operations."

**Takeaway/Lesson:**

* Establish an **SCM Plan** early in the development lifecycle and enforce it rigorously.
* Use practices like **coding standards, release standards, and documentation standards** to ensure consistency across all development artifacts.
* Weak or broken CM results in software that is difficult to maintain and prone to errors, particularly in operational scenarios.

**Additional Recommendation:**

* Perform periodic **audits** and reviews of CM adherence during key project milestones to ensure maintainability goals are achieved.

### **2. Configuration Control of Auto-Generated Code**

**Lesson Number: 1023**  
**Key Issue:** Auto-generated code requires robust CM and validation to prevent critical issues.

**Description:**  
"The use of the [auto] code generator for ISS software can lead to serious problems if the generated code and [tool] itself is not subjected to effective configuration control or the products are not subjected to unit-level Verification and Validation (V&V). These problems can be exacerbated if the code generated ... is modified by hand."

**Takeaway/Lesson:**

* Auto-generated code **must be version-controlled** as rigorously as manually written code to ensure traceability and reproducibility.
* The **code generation tool itself**, including its version, settings, and environment, must be placed under configuration control to prevent discrepancies between generated outputs.
* Mixing **hand-modified code** with auto-generated code increases the risk of introducing untraceable errors—use strict CM measures to track changes.

**Additional Recommendation:**

* Implement **unit-level V&V** for auto-generated code to ensure compliance with system requirements.
* Establish and enforce **rules for when and how generated code can be modified** manually, documenting all changes meticulously in the CM system.

### **3. Controlling File Renaming and Reuse**

**Lesson Number: 1481**  
**Key Issue:** Improper file renaming led to operational inefficiencies.

**Description:**  
"The team renamed a file prepared for a previous mission for use on a current mission without changing the file creation time recorded in the file header. This error caused the new file to be repeatedly recognized as an 'old' file, and required operations personnel for several months to manually specify the correct file. Implement Configuration Management (CM) measures to assure adequate oversight when renaming old command sequence resources for reuse."

**Takeaway/Lesson:**

* **Renaming and reusing old files** must be done with strong CM controls to avoid file conflicts or misidentification during mission operations.
* File headers must be **updated to reflect the new context**, including creation time, version, purpose, and any associated metadata.
* Operations personnel spent significant effort addressing the issue, which could have been avoided with better CM tracking of reused resources.

**Additional Recommendation:**

* Use **automated CM tools** to track and control file renaming across projects.
* Establish **naming conventions** that embed critical information (e.g., version, mission ID) to reduce ambiguity.

### **4. Version Tracking and Baseline Control**

**Lesson Derived from Historical Project Issues**  
**Key Issue:** Lack of version tracking for test environments caused discrepancies between development and production systems.

**Description:**  
On several projects, failure to version-control test environments, including hardware and software dependencies, led to mismatches between the development and operational systems. These differences caused failures in final software deployment that were not observed in testing. The issue was further exacerbated by incomplete documentation of environment configurations.

**Takeaway/Lesson:**

* **Treat environments as configuration items** by establishing a baseline for both development and operational setups. Track changes to both environments.
* Use tools like **Infrastructure-as-Code (IaC)** or virtual machines to enforce consistency across environments.

**Additional Recommendation:**

* Document and version-control all environment dependencies, including hardware specifications, operating systems, software libraries, and test case configurations.
* Regularly verify environment baselines to ensure alignment across all project phases.

### **5. Rigorous Control of Open-Source and COTS Software**

**Key Issue:** Failure to properly manage COTS and open-source software dependencies caused integration issues.

**Description:**  
Teams often integrate third-party software components (COTS or open-source libraries) into their projects. Without proper CM applied to third-party components (e.g., tracking versions or updates), projects have faced **integration failures** or vulnerabilities introduced by unverified updates.

**Takeaway/Lesson:**

* **Identify COTS and open-source items** as part of the configuration baseline. Version-control them along with internal software artifacts to maintain traceability and reproducibility.
* Apply **rigorous testing** when updating third-party components, and document any incompatibilities or changes.

**Additional Recommendation:**

* Establish a **dependency management process** that includes routine validation of third-party updates (e.g., scans for security patches or functional regressions).
* Evaluate the **licensing and legal risks** of open-source software to avoid compliance issues.

### **6. Importance of Stakeholder Buy-In for CM**

**Lesson Derived from Project Transitions**  
**Key Issue:** Lack of stakeholder involvement in CM planning and enforcement caused confusion during project transitions.

**Description:**  
Several projects failed to effectively implement or enforce CM plans because stakeholders were not engaged early. Teams introduced ad-hoc CM solutions, leading to inconsistencies, lack of traceability, and increased difficulty in transitioning systems to new teams.

**Takeaway/Lesson:**

* **Engage key stakeholders (developers, project managers, and operations staff)** in the creation and review of CM processes.
* Ensure that the CM plan is **well-documented, widely communicated**, and regularly updated based on team and stakeholder feedback.

**Additional Recommendation:**

* Use **training sessions** and **tools tailored to the team’s skill set** to enhance adherence to CM procedures.
* Align CM milestones with major project reviews so stakeholders can evaluate and accept baseline changes.

### **Conclusion:**

The NASA Lessons Learned database highlights recurring themes that demonstrate the importance of stringent Configuration Management (CM) practices. Effective CM:

* Ensures software maintainability.
* Reduces risks associated with poorly managed file reuse, auto-generated code, and third-party software.
* Aligns stakeholders and prevents mission disruptions caused by inconsistent version tracking or inadequate oversight.

By leveraging these lessons learned, projects can proactively strengthen their CM processes early, avoid operational inefficiencies, and enhance overall mission success.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Test plans should cover all aspects of testing](https://software.gsfc.nasa.gov/lesson-details/56/). **Lesson Number 56**: The recommendation states: "Test plans should cover all aspects of testing, including specific sequencing and/or data flow requirements."
* [Tagging builds for comprehensive functional testing vs for final release](https://software.gsfc.nasa.gov/lesson-details/283/). **Lesson Number 283**: The recommendation states: "Do not designate (tag) a build intended for comprehensive functional testing as the final release, because it is likely that the testing will result in findings that will require a subsequent build."
* [Establish processes early in development](https://software.gsfc.nasa.gov/lesson-details/331/). **Lesson Number 331**: The recommendation states: "Establish development and testing methodology and process early in the lifecycle."

# 7. Software Assurance

**SWE-079 - Develop CM Plan**

5.1.2 The project manager shall develop a software configuration management plan that describes the functions, responsibilities, and authority for the implementation of software configuration management for the project.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess that a software configuration management plan has been developed and complies with the requirements in NPR 7150.2 and Center/project guidance.

## 7.2 Software Assurance Products

This guidance for software assurance (SA) emphasizes clear, practical actions for assessing and verifying the compliance of a Software Configuration Management Plan (SCMP) with **NPR 7150.2** and other applicable requirements. It consolidates steps into coherent sections, smoothens language, and integrates best practices based on real-world needs.

The role of Software Assurance in relation to Software Configuration Management (SCM) is to verify compliance with requirements, monitor processes for effectiveness, and identify issues or risks early in the software lifecycle. Key SA deliverables include:

#### **Required SA Products:**

1. **Assessment of Software Engineering Compliance with NPR 7150.2**
   * Confirm that the SCMP satisfies the mandatory requirements outlined in **NPR 7150.2** and any Center-specific configurations or processes.
2. **Assessment of the SCMP:**
   * Identify issues or corrective actions needed for compliance. Ensure corrective actions are tracked and resolved.
3. **SA Concurrence on the SCMP:**
   * Software Assurance must sign off on the SCMP to ensure it aligns with the project needs and lifecycle requirements.
4. **Audit Results of the SCMP:**
   * Include findings from records of physical configuration audits, functional configuration audits, process compliance audits, and product audits.
5. **SA-Specific Configuration Management Plan (if applicable):**
   * In some cases, SA may develop its own plan to oversee SCM independently of the project’s SCMP.

## 7.3 Metrics for Monitoring SCM Effectiveness

Metrics play a critical role in tracking the performance and compliance of configuration management activities. Software Assurance should maintain oversight of the following indicators:

#### **Example Metrics:**

* **Non-Conformances:**

  1. Number of software work product **non-conformances** identified by lifecycle phase over time.
  2. Number of non-conformances per audit (including process and compliance audits).
  3. Number of **non-conformances identified in the SCMP.**
  4. Trends in **open vs. closed non-conformances** over time.
* **Audit Performance:**

  1. Trends in non-conformances from configuration and process audits over time.
  2. Number of compliance audits **planned vs. performed.**
* **Trends Across Plans:**

  1. Number of non-conformances in key plans such as SMPs, SDPs, CM Plans, SA Plans, Safety Plans, and Test Plans.
* **Process Maturity and Tracking:**

  1. Ratio of non-conformances from audits categorized by process maturity.

For additional details and metrics, refer to **Topic 8.18 - SA Suggested Metrics.**

## 7.4 Software Assurance Guidance for Configuration Management

#### **SCMP Assessment:**

Software Assurance must validate the SCMP against both **NPR 7150.2** and project or Center-specific requirements. The SCMP defines how configuration items are controlled, tracked, and managed throughout the software lifecycle. Use **5.06 - SCMP** and **7.18 - Documentation Guidance** as references for determining the accurate content and structure of the SCMP.

**Key Considerations During Assessment:**

1. **SCMP Content Completeness:**

   * Verify the SCMP includes all required sections (per **5.06 & SWE-079**), covering roles, processes, baselines, audits, and tool descriptions.
   * Ensure it appropriately tailors configuration management practices to project size, classification, and risk.
2. **State of Maturity:**

   * Ensure the SCMP is mature enough by project milestones (e.g., System Requirements Review (SRR), Software Requirements Review (SwRR)) to handle initial baselines and early documentation needs.
3. **Configuration Items (CIs):**

   * Verify the existence and completeness of a **list of configuration items (CIs)** in the SCMP to ensure all critical software artifacts are accounted for. Potential CIs include source code, test cases, builds, and safety-critical resources.
4. **Data Management Integration:**

   * Confirm the SCMP addresses **Data Management (DM)** for non-CCB-controlled items or specifies appropriate delegation to a standalone DM plan if necessary.

#### **Configuration Control Board (CCB):**

1. Verify that a **CCB has been formally established**.

   * Check that the SCMP lists all CCB members, including a Software Assurance representative.
   * Ensure the hierarchy and authority levels of multiple CCBs are clearly defined within the SCMP.
2. **Role Identification:**

   * Review the alignment of roles and responsibilities for all individuals participating in CM activities. Ensure Software Assurance concurrence/sign-off on all CCB-controlled items is incorporated.

#### **Tool Selection and Setup:**

1. Verify that the project has selected and implemented appropriate **CM tools** to manage configuration and data items.

   * **Capabilities to assess:** Baseline management, version control, authorized access, retrieval, and reporting.
   * Ensure tools allow traceability between configurations, changes, and baselines.
2. Confirm that the SCMP includes **processes** for:

   * Establishing baselines and releases.
   * Requesting, tracking, and controlling changes to products or baselines.
3. Identify whether the CM system provides:

   * Automated reports for audits.
   * Appropriate measures to protect the integrity of controlled data (e.g., backups, encryption).

#### **Audit Processes:**

Software Assurance ensures that **audit responsibilities** and oversight of SCM activities are properly documented and maintained.

**CM Records and Audits:**

1. Verify the plan includes records for **configuration audits**, such as:
   * Physical Configuration Audits (PCAs).
   * Functional Configuration Audits (FCAs).
   * CM Process Audits (e.g., verifying adherence to CM processes).
2. Identify roles responsible for conducting audits:
   * In some cases, SA may conduct audits directly; in others, SCM personnel will perform audits with SA overseeing or reviewing results.

### **Other Guidance:**

1. Ensure SCM **Change Processes** and **Release Management** align with NPR 7150.2 and lifecycle maturity.
2. Validate linkage between CCB actions and approved documentation changes to ensure traceability and avoid disruptions.
3. Confirm that **SCMP tailoring** aligns with the project’s classification and risk profile. Simpler projects may use relaxed approaches but must still meet minimum compliance requirements.

### **Conclusion:**

This enhanced Software Assurance guidance reinforces the importance of validating the Software Configuration Management Plan (SCMP) and ensuring alignment with **NPR 7150.2**, project-specific requirements, and CM best practices. By focusing on assessments, audits, metrics, tool implementation, and team roles, Software Assurance can ensure that CM processes are robust, effective, and tailored to the needs and risks of the project—leading to improved software quality, traceability, and reliability.

* Assessment of Software Engineering Compliance w/ NPR 7150.2
* Software assurance assessment of the software configuration management plan, including any issues or corrective actions.
* SA concurrence on configuration plan.
* Audit results and findings on software configuration plan.
* Software assurance configuration management plan.

See also [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits),

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical to demonstrate that Configuration Management (CM) processes and the associated Software Configuration Management Plan (SCMP) meet the requirements outlined in **NPR 7150.2** and related standards. Below is a comprehensive list of **good objective evidence** that can be collected, reviewed, and presented to support compliance with CM requirements.

---

### **1. Documentation Evidence**

#### **1.1 Software Configuration Management Plan (SCMP):**

* Approved version of the SCMP.
* Records of SCMP peer reviews, sign-off sheets, or comments resolution logs.
* Documented tailoring rationale (if the SCMP was simplified or integrated into another plan) and approvals.

#### **1.2 Configuration Item (CI) Lists and Baselines:**

* Comprehensive **CI identification lists** for all software work products, including:

  + Source code files.
  + Requirements documents.
  + Design artifacts (e.g., architecture diagrams, UML models).
  + Test plans, cases, and procedures.
  + Build procedures, executables, and release notes.
  + External dependencies (e.g., COTS/archive libraries).
* Records of **baseline approvals**, reflecting sign-off by the Configuration Control Board (CCB) or project management.
* Change history showing updates to CIs and the alignment of changes with approved baselines.

---

### **2. Configuration Management Process Records**

#### **2.1 Change Control Records:**

* Approved **change control process** (e.g., flowcharts, workflows, or a written procedure).
* Records of **change requests (CRs)**, including:

  + CR submissions with complete details and supporting documentation.
  + CR review/assessment logs.
  + CCB meeting minutes or decisions (approve/reject).
  + Traceability between CRs and requirements, source code changes, and test results.
* **Impact assessments** performed for changes (e.g., impact on safety-critical systems, cost, and schedule).

#### **2.2 Version and Revision Histories:**

* Version-controlled repositories (e.g., Git, Subversion, or equivalent) showing:
  + Unique identifiers for all versions of software items.
  + Log entries that trace code changes to specific requirements or issue reports.
* History of revisions for non-software items (e.g., specifications, designs, procedures).

---

### **3. Audit and Review Records**

#### **3.1 Configuration Audits:**

* **Audit reports** documenting the results of:

  + **Physical Configuration Audits (PCAs):** Ensuring the as-built system matches its recorded baseline.
  + **Functional Configuration Audits (FCAs):** Confirming that the system meets its functional and performance requirements.
  + Process and compliance audits examining adherence to the SCMP.
* Identified **issues or corrective actions** resulting from audits, including:

  + Records of problem reports.
  + Resolution or mitigation of audit findings (e.g., action items, updated processes).

#### **3.2 Traceability and Closure of Non-Conformances:**

* Reports on **non-conformances** with:

  + Tracking of open vs. closed non-conformances over time.
  + Evidence of resolution and validation for each closed finding.
* **SA concurrence statements** on audit results, confirming that findings meet compliance requirements.

---

### **4. Tools and Automation Evidence**

#### **4.1 Configuration Management System Logs:**

* Logs from CM tools (e.g., GitHub, Bitbucket, SVN, or other repositories) showing:
  + Access control and permissions management (ensuring only authorized personnel perform changes).
  + Records of CI check-ins, check-outs, and updates.
  + Baseline creation and versioning operations.
  + Automated audits or alerts for unauthorized changes.

#### **4.2 Tool Setup and Integration:**

* Evidence of tool implementation and configuration:
  + Screencaptures or logs showing tools set up to manage baselines, track changes, and generate CM reports.
  + Integration of tools with project management systems for synchronized updates.

---

### **5. Roles, Responsibilities, and Training Evidence**

#### **5.1 Configuration Control Board (CCB) Evidence:**

* Formal **charter or documentation** of CCB roles and responsibilities.
* Roster of CCB members, including Software Assurance personnel.
* Minutes from CCB meetings showing:
  + Approval or rejection of changes.
  + Discussion of risks, impacts, and necessary remediation.
  + Evidence of quorum and responsible decision-making.

#### **5.2 Staff Training Records:**

* Records of SCM-related training sessions for team members.
* Proof that CCB members and CM personnel are trained on CM tools, processes, and their specific roles.

---

### **6. Release Management and Delivery Evidence**

#### **6.1 Software Build and Release Records:**

* Documentation of the **build process**, including:

  + Scripts, procedures, and tools used.
  + Configurations applied to the development, test, and operational environments.
* Release notes for each version, including:

  + Features, changes, and known issues.
  + Relevant documentation updates.
  + Traceability between the release and baseline configurations.

#### **6.2 Delivery and Deployment Logs:**

* Logs showing software delivery to target environments (e.g., production systems, test simulations).
* Correspondence or evidence showing customer verification or approval of delivered baselines.

---

### **7. Risk Assessments and Tailoring**

#### **7.1 Tailoring Documentation:**

* Records of tailored CM requirements for projects with special circumstances (e.g., size, scope, classification).
* Documented rationale for excluding certain items (e.g., minimal risk conditions, short project timelines).

#### **7.2 Risk Analysis Records:**

* Risk assessments for configuration management, including consideration of:
  + Impacts of improper CM on safety-critical systems.
  + Risks related to inadequate versioning, lost work products, or mismanaged changes.

---

### **8. Metrics Evidence**

Metrics provide insights into the performance and effectiveness of the CM process. Examples of objective evidence include:

* Trend data for **open vs. closed non-conformances**.
* Data from compliance audits indicating the percentage of planned audits performed.
* Charts of non-conformances by audit type (e.g., process audits vs. product audits).
* Metrics related to change request lifecycles, such as average time-to-closure.

---

### **Conclusion**

Objective evidence for Software Configuration Management (SCM) should capture all key activities, from planning and implementation to audit results and compliance metrics. By collecting the right set of documentation, process records, tool logs, and baseline reports, projects can demonstrate that their CM processes are compliant, traceable, and robust. This evidence not only ensures compliance with **NPR 7150.2** but also supports project stakeholders in maintaining software integrity and controlling risks effectively.

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
