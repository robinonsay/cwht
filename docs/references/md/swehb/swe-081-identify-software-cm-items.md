# SWE-081 - Identify Software CM Items

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695461. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items

SWE-081 - Identify Software CM Items

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695461)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695461&showCommentArea=true&showComments=true#addcomment)

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

5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project.

## 1.1 Notes

The items to be controlled include tools, items, or settings used to develop the software, which could impact the software. Examples of such items include compiler/assembler versions, makefiles, batch files, and specific environment settings.

## 1.2 History

Click here to view the history of this requirement: SWE-081 History

SWE-081 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.1.3 The project shall identify the software configuration items (e.g., software documents, code, data, tools, models, scripts) and their versions to be controlled for the project. |
| Difference between A and B | No change |
| B | 5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project. |
| Difference between B and C | No change |
| C | 5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project. |
| Difference between C and D | No change |
| D | 5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project. |

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

For Software Configuration Management to be implemented on a project, the project has to identify what software configuration items are to be controlled for the project. Software Configuration Management encompasses the practices and procedures for administering source code, producing software development builds, controlling change, and managing software configurations for all of the software products, tools, data, and components produced by the project.

The identification and control of Software Configuration Items (SCI) are foundational for Configuration Management (CM). This process ensures that all elements of a software project’s development, testing, and deployment lifecycle are properly documented, managed, and maintained. Specifically, this requirement ensures that only authorized and validated versions of a project's deliverables are used, thereby enhancing traceability, integrity, and reproducibility while preventing errors introduced by mismanagement or lack of control.

### **1. Ensuring Traceability**

* **Rationale:**

  + Identifying configuration items (CIs) establishes a clear baseline of all project artifacts that directly or indirectly contribute to the software system (e.g., design documents, requirements, source code, test scripts, models). By maintaining configuration control, every change, update, or modification can be traced back to its origin, ensuring accountability and traceability.
  + This is particularly essential for software that interfaces with other systems, as changes to one item (e.g., source code) may impact downstream or related items (e.g., test cases, user manuals).
* **Example:** In safety-critical systems, the ability to trace a software defect back to a specific requirement or version of the code can identify where corrective actions must occur without ambiguity.

---

### **2. Managing Complexity and Enforcing Consistency**

* **Rationale:**

  + Software development projects involve multiple artifacts (e.g., requirements, tools, libraries, datasets, and their dependencies). Without identifying and managing these configuration items, inconsistencies can arise, leading to confusion, loss of productivity, and errors in the system.
  + Identifying and consistently controlling the specific versions of software artifacts ensures that every team member is working with synchronized and approved project components.
  + This is vital in collaborative environments where teams may work on different facets of a project globally.
* **Example:** If a script used for automated testing is not under version control, modifications by one team member could inadvertently lead to failed tests or inaccurate results for others, ultimately compromising the project.

---

### **3. Ensuring Configuration Control of Critical Elements**

* **Rationale:**

  + Failure to identify critical configuration items can lead to unauthorized changes slipping through the system, ultimately resulting in unpredictable or unstable software. This is especially important for safety-critical environments, where uncontrolled changes to software operations, data, or configurations can have severe consequences.
  + By establishing explicit configuration control over items such as source code, tools, and operational data, the project ensures proper oversight, auditability, and validation before deployment.
* **Example:** A small, unintended change in input data, if not controlled and tracked as a configuration item, may alter the behavior of a safety-critical system without being noticed.

---

### **4. Supporting Repeatability and Reproducibility**

* **Rationale:**

  + SCI identification is essential to ensure the reproducibility of results during testing and in future system maintenance. When projects are revisited or handed to new teams for maintenance or upgrades, a complete and well-documented list of SCIs guarantees that teams can reconstruct the system.
  + Reproducibility is vital for audits, certification, and long-term operations of NASA projects.
* **Example:** If an exploratory analysis tool or algorithm’s version is not documented, reconstructing historical analysis or identifying why results may differ becomes virtually impossible.

---

### **5. Meeting Industry Standards and Regulatory Requirements**

* **Rationale:**

  + Software standards such as ISO/IEC 12207, CMMI, and IEEE emphasize the importance of configuration management to maintain integrity and ensure compliance with project objectives.
  + For NASA projects, compliance with **NPR 7150.2** ensures that software artifacts are controlled under formal configuration management processes to meet safety, reliability, and performance requirements.
* **Example:** An external audit or review may request evidence that all versions of the software used in the project align with baseline, approved versions. SCI identification ensures that these artifacts are accounted for.

---

### **6. Minimizing Risks in a Multi-Version Environment**

* **Rationale:**

  + Throughout the project lifecycle, multiple versions of source code, tools, libraries, and other items will exist. Managing SCIs ensures that only approved versions are promoted to the operational baseline and eliminates the risk of unintended or older versions being used.
* **Example:** For mission-critical systems, ensuring that the flight software tools match operational software versions is critical to mitigating risks.

---

### **7. Facilitating Change Management and Impact Analysis**

* **Rationale:**

  + Accurate identification of SCIs allows for efficient change management and impact analysis. When a component is proposed to be modified, having all associated SCIs identified allows teams to understand which other items would be affected.
  + This ensures complete coverage of changes during impact analysis and avoids unintended consequences of incomplete updates.
* **Example:** A proposed change to a specific COTS library version can ripple through all dependent configuration items. Identifying the affected items upfront ensures that each component is tested and verified for compatibility.

---

### **8. Supporting Audits and Reviews**

* **Rationale:**

  + Configuration Management is commonly reviewed during project audits (e.g., lifecycle milestone reviews, safety audits). Accurate SCI identification ensures that auditors can confirm the control, traceability, and completeness of project artifacts during each milestone.
  + SCI lists and associated historical records substantiate compliance with the required software engineering processes.
* **Example:** During a Software Acceptance Review, the identified SCI list serves as the baseline for final checks on approved documentation, code, and data integrity.

---

### **Summary of Key Goals**

Identifying software configuration items ensures that:

1. All artifacts that contribute to the software system's functionality and safety are properly managed and controlled.
2. Traceability is maintained across the software development lifecycle, improving accountability and quality assurance.
3. The software system retains consistency, reproducibility, and maintainability across iterations and versions.
4. Regulatory requirements (e.g., **NPR 7150.2**, ISO/IEC Standards) are consistently fulfilled, ensuring the integrity of the delivered software.
5. Risks related to unmanaged or unauthorized changes are minimized.

By implementing a robust process to identify, document, and control SCIs, project managers help ensure successful project execution and product delivery, while maintaining the integrity and reliability of the software system.

# 3. Guidance

## 3.1 Version Control

Efficient and effective configuration management depends on properly identifying, managing, and controlling software configuration items (SCIs). Proper configuration identification provides the foundation for all subsequent configuration management activities, such as configuration control, status accounting, and audits. Mismanagement or incomplete configuration identification can lead to defective products, schedule delays, missed safety requirements, and increased long-term maintenance costs.

#### **Importance of Version Control**:

* Version control is a **core activity of configuration management** designed to manage changes to items under configuration control.
* It ensures the accurate identification of all releases of SCIs, enabling the retrieval of previous versions if problems arise.
* Version control supports **traceability**, enabling teams to determine precisely when, why, and how a configuration item was altered.

#### **Benefits of Version Control**:

1. **Historical Traceability**: Provides a clear timeline and context for changes.
2. **Problem Resolution**: Allows reversion to earlier configurations if new issues arise.
3. **Collaboration**: Facilitates coordination among teams by ensuring all stakeholders work on the approved versions of configuration items.
4. **Audit Evidence**: Serves as a key resource during reviews, audits, and certification processes.

Key activities within version control include establishing baselines to lock approved artifacts and tracking future changes against these baselines.

**MIL-HDBK-61 Department of Defense Configuration Management Guidance Handbook**

3.1 Configuration Identification Activity  
"Effective configuration identification is a pre-requisite for the other configuration management activities (configuration control, status accounting, audit), which all use the products of configuration identification. If CIs and their associated configuration documentation are not properly identified, it is impossible to control the changes to the items' configuration, establish accurate records and reports, or validate the configuration through the audit. Inaccurate or incomplete configuration documentation may result in defective products, schedule delays, and higher maintenance costs after delivery."[351](#_tabs-<p></p>)

## 3.2 Configuration Identification Process

#### **Four Elements of Configuration Identification**:

Configuration identification encompasses the following steps essential for effective software lifecycle management:

1. **Identify the Items to be Controlled**:

   * Identify the CIs to be placed under configuration control. These may include software (e.g., source code, models, scripts), data (e.g., test inputs, datasets), and supporting assets (e.g., tools, V&V plans).
   * Ensure all safety-critical software elements are explicitly identified as separate configuration items.
2. **Provide Unique Identifiers for Each Item**:

   * Assign unique identifiers (e.g., version numbers, labels) to differentiate items and track changes over time.
3. **Capture the Key Characteristics of Each Item**:

   * Define the functional, performance, physical, and interface-related attributes of the CI.
   * Document associated metadata, relationships with other artifacts, and ownership.
4. **Define the Acquisition Point for Each CI**:

   * Specify when each CI enters configuration control. For example:
     + During peer reviews (for requirements documents, designs).
     + After passing specific milestones (e.g., Test Readiness Review (TRR)).
     + After the integration of a defined set of software components.

#### **Outcome of Configuration Identification**:

* An accurate inventory of all controlled assets with clear relationships and identifiers.
* Documentation of the configuration identification process in the **Configuration Management Plan (CMP)**.

## 3.3 Items to Be Controlled

#### **Categories of Items**:

When determining what to place under configuration control, consider a **broad spectrum of artifacts**, including but not limited to the following:

1. **Core Software Artifacts**:

   * Source code, executables, scripts, and models (including auto-generated code models).
   * Internal work products, such as requirements documents, interface documents, and design blueprints.
   * Test-related assets: Test cases, test plans, procedures, data, and scripts.
2. **Support and External Tools**:

   * Compilers, linkers, CM tools, simulators, modeling tools, and their documentation (e.g., licenses, customizations, upgrades).
3. **COTS/GOTS/MOTS or Customer Software**:

   * Vendor- or customer-provided libraries, tools, and other software.
4. **Documentation**:

   * Plans (e.g., Software Assurance Plan, CM Plan, SDP/SMP).
   * Reports (e.g., hazard reports, safety analyses, software classification or tailoring matrices).
5. **Baselines**:

   * Baseline descriptions, including all items and versions included in approved baselines (e.g., requirements baseline, design baseline).

#### **Granularity Consideration for Items**:

When identifying controlled items, carefully evaluate the appropriate **level of granularity**:

* Control at the **higher level** (e.g., entire document) when lower-level control adds limited value.
* Control at a **more granular level** (e.g., individual sections, components) when frequent changes, reuse, or modularity are key.

## 3.4 Data Management and Control

#### **Integration with Configuration Management**:

* SCIs related to **data** (e.g., large datasets, test files, input/output files) require the same level of control as software artifacts.
* Data management ensures that project teams work with accurate, version-controlled data representing the correct state of the project at any given point.

#### **Considerations for Data Control**:

* Versioning: Each dataset must be versioned to allow rollback and change tracking.
* Metadata: Include metadata that captures the source, generation method, date of creation, and owner of the data.
* Storage: Ensure secure, redundant, and scalable storage for controlled data.

## 3.5 Generating Identifiers

#### **Principles of Identifier Design**:

The identifiers for configuration items must:

* Be unique, descriptive, and systematically aligned with the level of control.
* Be scalable to handle changes or version sequences over time.
* Support traceability by embedding relevant context (e.g., revision history or baseline identifiers).

#### **Key Components of Identifiers**:

* Revision/version numbers (e.g., v1.1.0).
* Document or module names.
* Baseline tags for grouping items into logical builds.
* Additional context-specific elements (e.g., "SAFETY" tag for safety-related elements).

## 3.6 Capturing Key Characteristics for Items

#### **Recommended Attributes to Capture for Each CI**:

1. Allocated requirements for the CI.
2. Associated design and test cases.
3. Owner or approver responsible for the CI.
4. Unique attributes tied to baselines, such as:
   * Specific performance or functional features.
   * Versions and procedures associated with developing that CI.
   * Interface considerations (e.g., dependencies or hardware interaction).

#### **Benefits of Capturing Key Characteristics**:

* Ensures comprehensive documentation for audits and troubleshooting.
* Builds a clear context for how each CI relates to the broader project baseline.

## 3.7 Acquisition Points and Acceptance Criteria

#### **Defining Acquisition Points**:

To optimize configuration management:

* Choose acquisition points that balance **flexibility** (to iteratively improve items) with **control** (to establish baseline traceability).
* Examples:
  + **Before peer reviews**: Allows iteration but still provides baseline security for subsequent modifications.
  + **After formal reviews (e.g., Test Readiness Review or Software Requirements Review)**: Ensures only validated, finalized versions enter baseline control.

#### **Acceptance Criteria for Acquisition**:

Criteria should clearly define when a CI is considered ready for control, such as:

* All open issues resolved.
* Peer review or audit findings closed.
* Formal approvals/documentation complete.

### **Key Takeaways on Configuration Identification and Control**:

1. **Foundation of Configuration Management**: Proper identification ensures that all aspects of configuration control, status tracking, and auditing can occur seamlessly.
2. **Comprehensive Coverage**: It is critical to identify, track, and control a broad set of SCIs (including code, tests, documentation, and tools).
3. **Granularity and Acquisition Point**: Balancing the level of detail and timing of control ensures efficiency without sacrificing traceability or accountability.
4. **Integration with Safety and Quality Goals**: For safety-critical systems, identifying and tracing safety software attributes ensures compliance and reduces risk.

By following these enhanced guidelines, projects can ensure their **Software Configuration Management Plans (SCMPs)** support delivery goals while sustaining traceability, safety, and quality standards.

The process elements are documented in the CM plan (see [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) and [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan)).

The following diagram from the superseded 2005 version of the IEEE Standard for Software Configuration Management Plans (IEEE STD 828-2005), shows a sample process overview for identifying CIs:

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Configuration Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Configuration+Management) |

# 4. Small Projects

For smaller projects, configuration management (CM) must be tailored to be lightweight, efficient, and easy to adopt while ensuring the integrity, traceability, and quality of software products. Small projects typically have fewer resources and simpler processes, so the strategies below focus on clear priorities, practical tools, and streamlined processes without compromising the core principles of configuration management.

---

### **1. Adopt Lightweight Configuration Processes**

#### Focus on Core Outcomes:

Even for small projects, configuration management ensures:

* **Traceability**: Tracking changes across software artifacts.
* **Integrity**: Preventing unauthorized or accidental changes.
* **Accountability**: Maintaining a historical record of decisions and updates.

Small projects can reduce complexity by focusing configuration management activities on the **most critical items** and avoiding unnecessary formalities.

---

### **2. Identify the Most Critical Configuration Items (CIs)**

For small projects, not every artifact needs to be controlled. Start by identifying the most critical CIs that impact project functionality, quality, and delivery. Consider prioritizing the following:

#### **Minimum CIs to Control:**

1. **Core Development Artifacts**:

   * Source code (e.g., scripts, libraries, core code repositories).
   * Software build scripts.
   * Configuration setup files for software environments.
2. **Testing Artifacts**:

   * Automated test scripts.
   * Test data/files.
   * Regression test suites.
3. **Key Supporting Documentation**:

   * Requirements documentation (can be as simple as a spreadsheet or shared document).
   * Interface control documents or any data exchange agreements.
   * High-level design artifacts like block diagrams or flowcharts.
   * Test plans and reports.
4. **Baseline Releases**:

   * Complete builds that represent major checkpoints of development.
   * Include all associated artifacts marked for a specific release (e.g., code, documentation, test results).
5. **Tool Configurations (if applicable)**:

   * Project-specific configurations of tools such as compilers or third-party integrations.
   * Versions of reused software such as COTS or open-source libraries.

---

### **3. Use Simple Tools for Configuration Tracking**

Small projects don’t need robust, enterprise-level CM tools. Lightweight solutions are sufficient to track version history, maintain consistency, and manage artifacts.

#### **Examples of Tools for Small Projects:**

* **Version Control**: Use tools like **Git** with platforms such as GitHub, GitLab, or Bitbucket to track source code, test scripts, or small documents.
  + Create branches for different baselines and utilize tags to mark releases.
  + Use simple naming conventions (e.g., "v1.0", "Hotfix-1.2") for version tracking.
* **Document Tracking**:
  + Use shared online tools like **Google Drive** or **Microsoft SharePoint** for requirements or other documents.
  + Maintain file naming conventions to indicate versions (e.g., "Requirements\_v1.0").
* **Integrated Issue Tracking**:
  + Incorporate tools such as **JIRA**, **Trello**, or **Asana** to manage changes to CIs with associated tasks or tickets.
* **Manual Logs (if Required)**:
  + For very low-complexity projects, a manual log (e.g., a spreadsheet with CI names, versions, and descriptions) can be maintained, provided it is strictly updated.

---

### **4. Establish Simple Configuration Identification Practices**

In smaller projects, CI identification does not require elaborate processes. Follow these simplified steps to identify, manage, and track your CIs:

1. **Start with a Checklist or Inventory of CIs**: Create a simple table containing:

   * Item name or identifier.
   * Item type (e.g., code, document, test artifact).
   * Version/Revision details.
   * Owner(s) responsible for updates.
   * Dependencies (e.g., links with other CIs).

   Example:

   | CI Name | Type | Version | Owner | Dependencies |
   | --- | --- | --- | --- | --- |
   | Source\_Code\_MainRepo | Source Code | v1.0 | Dev Team | Unit Tests, Interface |
   | API\_Test\_Suite | Test Artifact | v0.2 | QA Team | API Document |
   | Requirements\_Specification | Document | Rev A | PM | None |
2. **Assign Unique Identifiers to CIs**:

   * For source code, use repository names or branch names (e.g., "CoreApp\_v1.0").
   * For documents, assign simple identifiers (e.g., ReqDoc\_v1.2, TestPlan\_RevB).
   * For test scripts or datasets, use descriptive identifiers tied to their purpose (e.g., "Dataset\_Test\_Inputs\_v0.1").
3. **Focus on Critical Baselines**:

   * Identify key project milestones (e.g., first prototype, initial deployment) and create formal baseline snapshots of all controlled items for those points.
   * These provide a clear 'freeze point' for development and track what was delivered.

---

### **5. Streamline Change Control**

Smaller projects can reduce overhead by taking a streamlined approach to managing changes:

1. **Simple Recording of Change Requests**:

   * Use an online tracker or a shared spreadsheet to log proposed changes.
   * Track minimal attributes:
     + Change description.
     + Affected item(s).
     + Reason for the change.
     + Approval status.
     + Owner or implementer.
2. **Lightweight Approval Processes**:

   * For low-risk changes (e.g., bug fixes), informal approval via team communication (e.g., email, chat, or short meetings) may suffice.
   * For high-priority changes affecting baselines, hold a short team review (with notes taken in simple minutes or logs).
3. **Focus on Impact Analysis**:

   * Ensure proposed changes are assessed for risks before implementation.
   * For small teams, ask:
     + What other items might this change affect (e.g., breaking dependencies, design compatibility)?
     + Could this change affect the system's safety, reliability, or performance?

---

### **6. Integrate with Safety for Small Safety-Critical Projects**

Even for small projects, safety-critical items need additional scrutiny:

* Clearly identify safety-related CIs (e.g., hazard analyses, essential safety logic embedded in the code).
* Use specific tags or labels (e.g., "SafetyCritical") in your configuration management system to isolate these items for stricter review and control.

---

### **7. Gradually Define Acceptance Criteria**

For small projects, it is unnecessary to define time-intensive acceptance criteria for every individual artifact. Instead:

1. **Focus on the Core Outcome**:
   * Require "signoff" or team agreement that CIs meet functionality, quality, and completeness standards before entering the baseline.
2. **Capture Verification Evidence**:
   * Maintain simple records of completed reviews or tests for software, documents, or datasets.

#### Example Acceptance Points:

* Source code added to configuration control after:
  + Peer review and compilation check.
  + Critical automated tests pass.
* Documents added to configuration control after:
  + Review and iteration are complete.
  + Action-item lists from reviews have been closed.

---

### **8. Keep Things Lean but Disciplined**

In small projects, avoid overcomplicating processes. However:

* Ensure **all changes are traceable** to prevent errors due to uncontrolled updates.
* Periodically assess whether the CM process aligns with the project size and complexity.
* Adjust the process as the project evolves (e.g., adding automation or tools as needed).

---

### **Small Project Success Tips**:

* **Communication Is Key**: Keep the team well-informed about which items are under control and how to contribute.
* **Automate When Possible**: Use simple tools to reduce manual effort.
* **Prioritize Critical Artifacts**: Not everything needs tight control—focus on items most critical to the project's success.
* **Scale Gradually**: Start with simple practices, and add complexity (only if needed) as the project evolves.

By adopting these lightweight but structured practices for identifying and managing CIs, small projects can maintain agility while still achieving robust configuration management and consistent delivery quality.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

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
* (SWEREF-343)

  [STEP Level 2 Software Configuration Management and Data Management course, SMA-SA-WBT-204, SATERN (need user account to access SATERN courses).](https://saterninfo.nasa.gov/ "Click to open in new window")

  This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-351)

  ["Department of Defense Configuration Management Guidance Handbook," MIL-HDBK-61. Revision A.](http://everyspec.com/MIL-HDBK/MIL-HDBK-0001-0099/MIL-HDBK-61_11531/ "Click to open in new window")

  U.S. Department of Defense (1997). Editor Note: Revision A is the reference. This URL is the download page for this document. The download is free.
* (SWEREF-506)

  [Galileo Spacecraft Safing Recovery Anomalies](https://llis.nasa.gov/lesson/391 "Click to open in new window")

  Public Lessons Learned Entry: 391.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Maintaining current and accurate configuration items (CIs), including software and documentation, is critical to preventing anomalies, ensuring recovery processes are effective, and maintaining the reliability of mission operations. Proper identification of software configuration items and their control contributes to the success of projects by enabling traceability, supporting anomaly resolution, and mitigating risks related to outdated or incomplete configuration data.

#### **Documented Lesson from NASA's Lessons Learned Database: Galileo Spacecraft Safing Recovery Anomalies (Lesson Number 0391)**

The **Galileo mission** encountered challenges during recovery from safing errors due to inadequacies in software and documentation related to spacecraft states. Specifically:

* **Issue**: A lack of a formal safing recovery plan and outdated or incomplete software/documentation on spacecraft states contributed to difficulties in resolving safing errors.
* **Lesson Learned**:
  + Maintain and **update anomaly recovery plans** to ensure readiness for issues.
  + Log spacecraft event updates to capture real-time configurations and changes to states.
  + Exercise caution when **reusing previously successful command packages**, as mission conditions or spacecraft states may differ.
  + Properly identify and account for **nonstandard ground system configurations** in the anomaly recovery process.

---

### **Key Takeaways from the Lesson**

This documented anomaly highlights the importance of maintaining up-to-date, controlled software and documentation artifacts. Specifically, the following principles emerge:

1. **Configuration Identification**:

   * Comprehensive identification of all artifacts related to safing recovery plans, spacecraft states, and ground system configurations is essential to ensure traceability during anomaly resolution.
2. **Configuration Maintenance**:

   * Configuration artifacts must be regularly updated to reflect changes in spacecraft software, operational states, recovery processes, and ground system configurations.
3. **Preventing Over-Reliance on Past Success**:

   * Previously successful command packages and configurations may become invalid due to project or system evolution. Correct identification and verification of reused items are vital.
4. **Nonstandard Configurations**:

   * Nonstandard or mission-specific configurations require explicit documentation and identifiers to prevent misalignment during safing or anomaly resolution tasks.

---

### **Additional Lessons Related to Configuration Identification and Maintenance**

#### **1. Lesson: Importance of Clear Baselines**

* **Background**: In certain NASA missions, inaccurate baselines or poorly tracked configuration items resulted in deployment failures and maintenance challenges.
* **Lesson Learned**:
  + Define and maintain clear baselines for all software and documentation artifacts, including recovery plans, operational configurations, and spacecraft states.
  + Regularly update baselines to reflect approved changes and capture complete artifact histories.

---

#### **2. Lesson: Managing Configuration Drift**

* **Background**: Configuration drift, where software or documentation artifacts diverge from their authorized versions, has led to inconsistencies during testing and operations in several projects.
* **Lesson Learned**:
  + Implement rigorous **version control** to monitor changes and prevent drift in software, recovery plans, and operational configurations.
  + Schedule regular audits to confirm that baselines and operational artifacts align with documented requirements and system states.

---

#### **3. Lesson: Traceability for Anomaly Resolution**

* **Background**: Lack of traceability between configuration items has made anomaly troubleshooting and root-cause analysis difficult in past missions.
* **Lesson Learned**:
  + Ensure CIs are traceable across their lifecycle (e.g., from requirements to code, test artifacts, documentation).
  + Maintain comprehensive metadata for each CI, including relationships and dependencies.

---

#### **4. Lesson: Planning for Reuse**

* **Background**: Improper reuse of artifacts (e.g., software or command packages) without verification caused system failures during certain missions.
* **Lesson Learned**:
  + Establish a checklist to vet reused items (e.g., compatibility tests, verification against current system states).
  + Document the conditions under which artifacts were originally developed to assess applicability to new contexts.

---

#### **5. Lesson: Integration with Ground Systems**

* **Background**: In past missions, gaps between onboard spacecraft documentation and nonstandard ground system configurations led to process failures during recovery operations.
* **Lesson Learned**:
  + Clearly document ground system configurations and integration points to ensure compatibility during anomaly recovery or standard operations.
  + Identify and track nonstandard configurations explicitly as CIs and include them in safing plans.

---

#### **Summary and Best Practices Based on Lessons Learned**

The Galileo mission's safing recovery anomalies, as well as other lessons learned across NASA projects, underscore the critical role of **up-to-date, controlled, and accurately identified configuration items**. Successful management of software CIs requires:

1. **Maintaining Current Documentation**:

   * Proactively update recovery plans and spacecraft state documentation.
   * Ensure that all changes to system configurations are logged and approved.
2. **Implementation of Comprehensive Configuration Management**:

   * Identify all relevant configuration items, including nonstandard artifacts and ground system dependencies.
   * Enable traceability between software, documentation, and operational states.
3. **Safeguarding Against Configuration Drift**:

   * Establish clear processes for updating configuration artifacts and performing regular audits.
   * Use version control systems to manage all software and documentation updates.
4. **Preparation for Reuse**:

   * Include compatibility assessments before reusing command sequences or nonstandard configurations.
   * Retain historical context for each reused artifact.
5. **Accountability and Operational Awareness**:

   * Treat anomaly recovery plans, ground configurations, and spacecraft state documentation as safety-critical artifacts requiring ongoing configuration control.

By following these lessons, small and large projects alike can prevent operational delays, reduce recovery time during safing states, and maintain reliable system performance for mission success.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Tagging builds for comprehensive functional testing vs for final release](https://software.gsfc.nasa.gov/lesson-details/283/).**Lesson Number 283**: The recommendation states: "Do not designate (tag) a build intended for comprehensive functional testing as the final release, because it is likely that the testing will result in findings that will require a subsequent build."

# 7. Software Assurance

**SWE-081 - Identify Software CM Items**

5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project has identified the configuration items and their versions to be controlled.

2. Assess that the software safety-critical items are configuration-managed, including hazard reports and safety analysis.

## 7.2 Software Assurance Products

Ensuring that software assurance personnel (SAP) confirm the completeness and correctness of configuration items (CIs) is critical for maintaining a project's integrity, managing risks, tracking safety-critical elements, and supporting recovery or anomaly resolution throughout the software lifecycle. This improved guidance provides deeper insights, refined processes, and specific steps to help ensure compliance with **SWE-081** while integrating safety analysis and configuration management effectively.

#### **Key SA Products to Support SWE-081 Compliance**

Software assurance personnel must produce and leverage the following products to fulfill their responsibilities for configuration management:

1. **Software Design Analysis**:

   * Review the traceability of design artifacts to ensure all components identified as configuration items (CIs) are aligned with the software architecture and overall system design.
   * Confirm that safety-critical components (e.g., modules controlling hazardous functions) and all associated design specifications are properly identified and included as CIs.
2. **Assessment of Hazard Analyses and Reports**:

   * Evaluate the hazard analyses and reports provided by the project to identify safety-critical code segments, data, and operational configurations.
   * Cross-check these safety-related items against the list of identified configuration items to ensure inclusion in the **Software Configuration Management Plan (SCMP)**.
3. **Source Code Analysis**:

   * Perform source code assurance to identify critical dependencies or unsafe coding practices that could affect functionality tied to hazard controls.
   * Confirm that all safety-critical source code files are under strict configuration control.
4. **Verification Activities Analysis**:

   * Review the project's verification plans, test cases, and procedures to ensure the completeness and traceability of safety-critical components.
   * Verify that all test-related artifacts (e.g., test data, scripts, results) are flagged as configuration items and controlled appropriately.
5. **Assessment of Configuration Management (CM) for Safety-Critical Items**:

   * Evaluate the project's CM processes to confirm proper tracking, updates, and versioning of safety-critical CIs.
   * Assess risks and issues associated with incomplete identification or mismanagement of CIs and provide recommendations for mitigation.

#### **Configuration Management Artifacts Relevant to Safety-Critical Items**

* **Hazard Analyses and Reports**:

  + Verify that all hazard-related documents, analyses, and reports are managed as configuration items.
  + Ensure these artifacts are version-controlled and linked to corresponding code/design elements in the baseline.
* **Software Configuration Management Plan (SCMP)**:

  + Confirm that the SCMP outlines procedures for identifying, categorizing, controlling, and updating all safety-critical items.
  + Review the plan for inclusion of specific safety-critical workflows tied to hazard-related software assurance tasks.
* **Software Configuration Management System Data**:

  + Assess the CM system’s data records to validate inclusion of identified CIs (e.g., source code files, design documents, test assets).
  + Ensure the system maintains proper versioning and traceability for safety-critical configurations.

## 7.3 Metrics

#### **Suggested Software Assurance Metrics for Tracking Configuration Control Effectiveness**

To assess and improve the project's handling of configuration management, safety-critical items, and associated risks, SAP should track the following metrics:

1. **Number of Safety-Related Non-Conformances Identified**:

   * Track safety-related non-conformances throughout the lifecycle phases (e.g., requirements, design, implementation, testing, acceptance, operations).
   * Categorize non-conformances by type, severity, lifecycle phase, and resolution time.
2. **Traceability Coverage**:

   * Measure the percentage of safety-critical requirements traced to corresponding configurations (source code, design artifacts, test cases, etc.).
3. **Configuration Change Impact Analysis Efficiency**:

   * Track how often a configuration item's change impacts downstream safety-critical items or operational artifacts.
   * Monitor the average response time for analyzing and mitigating change-related risks.
4. **Baseline Stability Metrics**:

   * Measure how often the safety-critical baseline is disrupted due to undocumented or unreviewed changes.

For additional guidance, see **Topic 8.18: SA Suggested Metrics**.

## 7.4 Guidance

#### **Software Assurance Tasks for SWE-081 Compliance**

To ensure proper identification and control of configuration items, SAP should perform the following:

1. **Review the Project’s Inventory of Configuration Items**:

   * Confirm that the project has identified the **complete list of software configuration items (SCIs)**, referencing the types outlined in **SWE-081 Guidance** (e.g., source code, design documents, test-related artifacts, safety-critical configurations).
   * Validate completeness against project-specific requirements, safety-critical areas, and reuse considerations.
2. **Assess Inclusion of Safety-Critical Components**:

   * Evaluate the list of **safety-critical components** to ensure alignment with hazard analyses, failure modes, and critical functions.
   * Check that hazard reports and associated safety-related artifacts (e.g., data packages, recovery documents) are controlled as CIs.

#### **Actions to Confirm Completeness**:

1. **Trace Safety-Critical Items to Requirements**:

   * Verify that each CI related to hazard controls or safety features is clearly mapped to the corresponding software and system requirements.
   * Ensure that changes to requirements automatically trigger evaluation of their associated safety-critical CIs.
2. **Collaborate on CM Plan Development**:

   * Partner with the project team to develop and review the **Software Configuration Management Plan (SCMP)**, ensuring it includes:
     + Clearly defined procedures for identifying safety-critical CIs.
     + Versioning rules for safety and hazard-related items.
     + Specific workflows for control and review of safety-critical baselines.
3. **Evaluate Project CM Processes**:

   * Review the configuration management system and assess its capability to handle safety-critical items effectively. Key considerations:
     + Does the system track changes and versions for all relevant artifacts (e.g., source code, test scripts, hazard documentation)?
     + Are approval processes (e.g., change control boards) adequately defined for safety-critical elements?
   * Identify and report risks or issues caused by gaps in configuration control.

#### **Tasks Specific to Hazard-Related Items**:

1. **Hazard Analysis Review**:

   * Cross-check identified hazard-related items (e.g., failure analyses, warnings, safing procedures) against the list of configuration-controlled items.
   * Ensure consistency between hazard analysis outputs and safety-critical code libraries or operational configurations.
2. **Safeguard Against Reuse Risks**:

   * Confirm that reused components, safety-related data, or command packages meet current project baselines and safety-critical requirements.
   * Identify risks stemming from outdated or partially compatible reused artifacts.
3. **Coordinate Safety Assurance with CM Activities**:

   * Work with teams managing safety-critical systems to integrate safety analysis updates into configuration-controlled artifacts directly.

### **Additional Improvements Based on Best Practices**

#### **Proactive Lessons Integrated into SWE-081 Compliance**:

1. **Real-Time Updates**:

   * Ensure configuration systems capture real-time updates to safety-related artifacts during reviews, testing, and operational phases.
2. **Automated Configuration System**:

   * Suggest adopting tools with automatic version control and traceability features tailored to managing safety-critical items (e.g., Git, Nexus, or enterprise CM tools).
3. **Periodic Audit Reviews**:

   * Conduct periodic audits of configuration-managed items to identify missed safety-critical artifacts or potential configuration drift.
4. **Minimize Configuration Fragmentation**:

   * Consolidate configurations into logical groups (e.g., baselines of hazard-related items) to reduce risks associated with tracking multiple small artifacts.

### **Final Remarks**

Software assurance personnel play a critical role in ensuring proper identification and management of configuration items, particularly safety-critical components. By rigorously reviewing, assessing, and validating the complete list of safety-critical artifacts, SAP can strengthen the project's ability to manage risks, comply with safety standards, and ensure the integrity of the system design and operation. Collaboration with the broader team is necessary to ensure that configuration management processes and tools are capable of meeting the project's safety assurance goals.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

To comply with **SWE-081**, projects must provide documentation, records, and artifacts that demonstrate the identification, control, and management of software configuration items. The objective evidence should not only show that the CIs have been identified but also confirm that they are tracked, adequately version-controlled, and updated throughout the software lifecycle. Below is a list of objective evidence that satisfies the requirement:

---

### **1. Configuration Identification Evidence**

#### **Artifact: List/Inventory of Software Configuration Items (SCI)**

* **Description**: A comprehensive list of all identified CIs, including safety-critical items, with unique identifiers for each CI.
* **Attributes**:
  + Item name.
  + CI type (e.g., source code, design document, test script).
  + Version/revision.
  + Responsible owner.
  + Dependencies or relationships between items.
* **Source**: Configuration Management Plan (SCMP) or a dedicated document (e.g., CI Inventory or CI Register).

#### **Artifact: Configuration Item Metadata**

* **Description**: Metadata associated with each CI recorded in the configuration management system, including:
  + Creation date.
  + Author.
  + Associated project milestone or baseline.
  + Approval history (e.g., Change Control Board (CCB) decisions).

---

### **2. Software Configuration Management Plan (SCMP)**

* **Description**: The SCMP outlines processes and procedures for managing CIs, including how items are identified, updated, and governed.
* **Key Elements**:
  + Procedures for CI identification.
  + Types of items (e.g., code, documents, tools) subject to configuration management.
  + Guidelines for CI versioning, status tracking, and control.
  + Role definitions, including responsibility for assessing, approving, and controlling CIs.
* **Source**: Created during the CM planning phase; reviewed in project milestone reviews (e.g., Preliminary Design Review, Critical Design Review).

---

### **3. Baseline Documentation**

#### **Artifact: Baseline Identification**

* **Description**: Evidence that CIs are associated with specific baselines, such as:
  + Requirements baseline.
  + Design baseline.
  + Code baseline.
  + Test baseline.
* **Attributes**:
  + List of items included in each baseline.
  + Approved versions of items in the baseline.
  + Documentation of baseline approval by the Change Control Board (CCB).
* **Source**: Baseline records from configuration management systems or milestone review documentation.

#### **Artifact: Baseline Change Records**

* **Description**: Evidence of how baseline items were updated or changed, including:
  + Details of version changes.
  + Approvals for modifications.
  + Impact analysis for changes.

---

### **4. Safety-Critical CI Evidence**

#### **Artifact: Hazard Analysis and Safety Reports**

* **Description**: Outputs from hazard analyses showing safety-critical software, data, and components that must be controlled.
* **Attributes**:
  + Safety-critical configuration items identified.
  + Links to hazard documentation or relevant requirements.
* **Source**: Safety analyses, hazard reports, or related deliverables.

#### **Artifact: Safety Assessment Reports (SARs)**

* **Description**: Evidence of software assurance personnel’s review and approval of safety-critical CIs.
* **Attributes**:
  + Confirmation that hazard-related artifacts (e.g., fail-safes, critical functions) are controlled.
  + Review comments and closure of action items.

---

### **5. Tools, Data, and Environmental Items**

#### **Artifact: List of Tool and Support Items**

* **Description**: A record of tools, scripts, simulators, and environments under configuration control.
* **Attributes**:
  + Name and version of each tool (e.g., compilers, build tools).
  + Description of use in the project.
  + Status of licensing/certifications.
  + Configuration control evidence for tool updates.
* **Source**: Configuration Management System or SCMP.

#### **Artifact: Versioning Records for Data and Tools**

* **Description**: Evidence that the tools and operational data used in the software are version-controlled.
* **Attributes**:
  + Version history.
  + Dates and approvals for new versions or changes.
* **Source**: System repositories, tool usage logs.

---

### **6. Change Control Records**

#### **Artifact: Change Request Records**

* **Description**: Formal documentation of change requests for configuration items.
* **Attributes**:
  + CI names affected by the request.
  + Reason for change.
  + Review and approval history (e.g., Change Control Board approval).
  + Risk and impact assessments for safety-critical items.
* **Source**: Change control tools or logs.

#### **Artifact: Change Log**

* **Description**: Evidence of changes made to CIs (e.g., source code, documents, test artifacts) throughout the lifecycle.
* **Source**: Project repositories, manual change logs, or version histories.

---

### **7. Traceability Evidence**

#### **Artifact: Requirements Traceability Matrix (RTM)**

* **Description**: Evidence linking software requirements to software CIs, ensuring traceability across the lifecycle.
* **Attributes**:
  + Linkages between requirements, design, code, and test cases.
  + Identification of safety-critical or high-priority requirements.
* **Source**: Traceability tool or RTM maintained by the project.

#### **Artifact: Safety-Critical CI Mapping**

* **Description**: A map showing the relationships between safety-critical hazards and their corresponding configuration items.
* **Source**: Included in hazard analysis reports or safety assurance reports.

---

### **8. Software Configuration Management System Data**

#### **Artifact: CM System Logs**

* **Description**: Outputs from configuration management tools demonstrating that identified CIs are under control.
* **Attributes**:
  + CI version histories.
  + Check-in/check-out records for source code or documents.
  + Approval actions for each CI change.
* **Source**: CM systems (e.g., Git, SVN, IBM Rational).

#### **Artifact: Automated Version Control Evidence**

* **Description**: Evidence generated by version control tools that show branch histories, commit logs, and tagged versions for releases.
* **Source**: Git repository reports, including branch protection policies.

---

### **9. Peer Review Records**

#### **Artifact: Peer Review Reports**

* **Description**: Reports from peer reviews of the SCI list, ensuring its completeness and correctness.
* **Attributes**:
  + Comments and resolutions for SCI completeness checks.
  + Evidence of review and approval.
* **Source**: Review checklists and meeting minutes.

---

### **10. Software Assurance Assessments**

#### **Artifact: SA Review Records**

* **Description**: Evidence that software assurance personnel reviewed and approved the SCI list, with special attention to safety-critical items.
* **Attributes**:
  + Review comments and closure evidence.
  + Final approval notes indicating SCI compliance with project standards.
* **Source**: SA review checklists, reports, and signoff documents.

#### **Artifact: Metrics Reports**

* **Description**: Reports showing software assurance metrics for configuration control, such as the number of safety-related non-conformances identified.
* **Source**: SA logs, status reports.

---

### **Conclusion**

This collection of objective evidence ensures compliance with SWE-081 by thoroughly identifying, controlling, and managing software configuration items, particularly safety-critical components. Comprehensive documentation and traceability provide confidence that project artifacts are under proper control, meet traceability requirements, and prevent failures due to mismanagement or omissions in configuration management.

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
