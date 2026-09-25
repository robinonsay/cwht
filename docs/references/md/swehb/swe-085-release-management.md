# SWE-085 - Release Management

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695469. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management

SWE-085 - Release Management

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695469)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695469&showCommentArea=true&showComments=true#addcomment)

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

5.1.8 The project manager shall establish and implement procedures for the storage, handling, delivery, release, and maintenance of deliverable software products.  

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-085 History

SWE-085 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.1.7 The project shall establish and implement procedures for the storage, handling, delivery, release, and maintenance of deliverable software products. |
| Difference between A and B | No change |
| B | 5.1.8 The project manager shall establish and implement procedures for the storage, handling, delivery, release, and maintenance of deliverable software products. |
| Difference between B and C | No change |
| C | 5.1.8 The project manager shall establish and implement procedures for the storage, handling, delivery, release, and maintenance of deliverable software products. |
| Difference between C and D | No change |
| D | 5.1.8 The project manager shall establish and implement procedures for the storage, handling, delivery, release, and maintenance of deliverable software products. |

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

Given that software is considered a significant Agency investment, it is important to ensure that the delivered software is created and maintained from a controlled repository. Configuration management (CM) processes and controls provide the rigor and organization necessary for developers and their customers to have confidence that all changes to the code and documents are included in the released products. It is also important that the released product is stored, maintained, and delivered following a repeatable, controlled process.

Proper management of deliverable software products is critical to ensuring their quality, integrity, and operational readiness. Establishing and implementing procedures for the **storage**, **handling**, **delivery**, **release**, and **maintenance** of software provides a structured approach to safeguarding software assets and ensuring that they are used and maintained correctly throughout the lifecycle of the project.

This requirement focuses on preventing risks during transition points in a software product's lifecycle, including storage mismanagement, improper handling, delivery errors, and inadequate support for software during its operational use. Below are the key aspects of the rationale:

---

### **1. Ensuring Software Quality and Integrity**

* **Rationale:** Procedures for storing and handling software ensure that original artifacts remain tamper-proof, consistent, and error-free throughout the development, delivery, and maintenance phases.
  + Software artifacts, including source code, executables, documentation, and configuration files, need to be stored securely to prevent unauthorized modifications or loss.
  + Robust handling practices ensure that no corruption, incomplete transfers, or errors occur when software is retrieved for testing or delivery.

---

### **2. Preventing Configuration Errors During Release and Delivery**

* **Rationale:** Establishing clear, repeatable steps for software delivery and release avoids costly mistakes or inconsistencies in what is provided to end users. This also guarantees that the product being delivered matches the approved and tested configuration baseline.
  + For example, failure to implement proper version control at the point of delivery could result in outdated or incorrect software reaching the end user.
  + These errors could directly compromise mission performance, safety, or security.

---

### **3. Supporting Operational Use and Mission Success**

* **Rationale:** Well-maintained deliverable software is vital for supporting mission objectives. After delivery, software products often require updates, patches, or long-term maintenance to remain effective in meeting operational requirements.
  + Without pre-established procedures, updates may inadvertently introduce defects or result in incompatible configurations.
  + Deliverable software used in mission-critical systems (e.g., embedded software for space exploration vehicles or satellites) requires consistent maintenance to ensure reliability and safety.

---

### **4. Ensuring Traceability and Accountability**

* **Rationale:** Clear procedures provide traceability from the development phase through delivery, ensuring that every software item, version, and revision can be tracked and audited.
  + In the event of errors or mission anomalies, traceability ensures that the exact state of the software used (e.g., delivered version, patches, or updates) can be reviewed and analyzed.
  + Responsibilities for each stage of the process can be assigned and monitored through well-defined procedures.

---

### **5. Enabling Compliance with Agency Standards**

* **Rationale:** NASA has strict requirements for software safety, quality assurance, and configuration management. Establishing and implementing procedures for storage, handling, delivery, release, and maintenance ensures compliance with:
  + **NASA Procedural Requirements (NPR)**, including NPR 7150.2 (NASA Software Engineering Requirements) and NPR 7120.5 (NASA Space Flight Program and Project Management Requirements).
  + Industry standards such as ISO 9001:2015 (Quality Management Systems) and CMMI (Capability Maturity Model Integration).

---

### **6. Mitigating Risks and Vulnerabilities**

* **Rationale:** Software is vulnerable to a wide range of risks, including:

  + **Loss or Corruption:** Unprotected software artifacts can be corrupted due to improper storage or delivery practices.
  + **Unauthorized Access:** Insecure handling or delivery processes could result in malicious modifications or theft of proprietary software.
  + **Operational Disruptions:** Failure to properly deliver or maintain software can disrupt mission-critical operations, resulting in mission delays or failures.

  By implementing strong procedures for software storage, handling, delivery, release, and maintenance, the project ensures a robust risk mitigation strategy.

---

### **7. Supporting Long-Term Sustainment**

* **Rationale:** Deliverable software often needs to be maintained and supported for years, especially for long-term missions (e.g., Mars rovers, space telescopes, satellite systems). Proper procedures guarantee consistency during:

  + Software upgrades and patches.
  + Data migration to different hardware or platforms.
  + Future audits for safety, functionality, or quality assessment.

  These processes ensure that the software remains functional and secure over its operational life.

---

### **8. Enabling Collaboration Across Teams/Contractors**

* **Rationale:** Deliverable software often involves multiple teams (e.g., NASA, contractors, stakeholders). Consistent storage, handling, and delivery procedures reduce communication errors and ensure seamless transitions across interfaces.

---

### **Key Outcomes of Implementing This Requirement**

1. **Improved Software Quality:** Deliverables are complete, functional, and defect-free.
2. **Greater Reliability:** Software is secured against tampering or corruption through proper storage and handling procedures.
3. **Mission Safety and Operational Readiness:** Delivered software performs as expected under mission-critical scenarios.
4. **Efficient Maintenance:** Established maintenance procedures allow smooth updates without disruption.
5. **Accountable Processes:** Provides a well-documented, traceable path from software creation to delivery, enabling audits and accountability.

---

### **Conclusion**

This requirement underscores the importance of establishing and implementing repeatable, systematic procedures for the storage, handling, delivery, release, and maintenance of deliverable software products. These procedures serve as the foundation for maintaining the integrity, functionality, and usability of mission-critical software throughout its lifecycle. The consequences of poor management at any stage can compromise mission performance, safety, or operational readiness, making this requirement key to NASA’s rigorous engineering and quality assurance standards.

# 3. Guidance

## 3.1 Definitions

The deliverable software release includes dynamically packaged configuration items (CIs) that are formally transitioned from controlled environments to their intended use, ensuring verification, completeness, and operational fitness. Below is an improved summary and integration of the referenced definitions:

#### **Release Definition**

A software release refers to a formalized version of a software product or application (including associated artifacts such as documentation, installation packages, or user guides) that is prepared for deployment, delivery, or operational use. Releases align with predefined baselines and are characterized by specific goals and scope, including functionality updates, patches, or incremental improvements.

##### **Key Characteristics of Releases:**

1. **Version-Specific:**

   * Every release represents a particular version of configuration items designed for specific purposes. Versions often include **major** (functional or interface changes) and **minor** (incremental fixes and updates) identifiers to track release maturity.
   * Unique identifiers convey the revision history and provide traceability (e.g., version numbers like "v3.2.1").
2. **Cohesive Package:**

   * Releases bundle one or more new or changed configuration items, tested together, for simultaneous deployment into a target environment.
3. **Deployment Scope:**

   * Releases may be internal (e.g., baselines for testing teams) or external (to customers or users).
   * Types of release packages include:
     + **Full Versions:** Complete software systems.
     + **Incremental Updates:** Changes designed to be added to a previously installed version.
     + **Patches:** A subset of incremental changes to correct bugs or vulnerabilities.
4. **Transfer:**

   * The release transitions from development and testing phases into operational environments, ensuring readiness and conformance to quality requirements.

#### **Release Management Overview**

Release management governs all activities related to the preparation, creation, delivery, storage, and maintenance of releases. It ensures that the release meets quality, security, and functional requirements while minimizing risks during transitions.

**Key Goals:**

* Guarantee the integrity, traceability, and usability of deliverable software.
* Align controlled environments (e.g., CM systems) with operational environments and user needs.
* Define quality approval criteria and sign-off procedures for software readiness.

**Elements of Release Management Procedures:**

1. Preparation of release package contents.
2. Creation and verification of the release package.
3. Delivery and installation procedures.
4. Storage and long-term maintenance of release artifacts.

**3.1.1 IEEE Definition for Release.**

1. particular version of a configuration item that is made available for a specific purpose 
   1. (IEEE Std 828-2012, IEEE Standard for Configuration Management in Systems and Software Engineering [216](#_tabs-<p></p>), 2.12)
   2. (ISO/IEC/IEEE 12207:2017 - Systems and software engineering — Software life cycle processes [415](#_tabs-<p></p>), 3.1.43)
2. collection of new or changed configuration items that are tested and introduced into a live environment together 
   1. (IEEE Std 828-2012, IEEE Standard for Configuration Management in Systems and Software Engineering [216](#_tabs-<p></p>), 2.1)
3. collection of one or more new or changed configuration items deployed into the live environment as a result of one or more changes 
   1. (ISO/IEC 19770-5:2015(en) Information technology — IT asset management — Overview and vocabulary [059](#_tabs-<p></p>), 3.28)
4. software version that is made formally available to a wider community 
   1. (IEEE Std 828-2012, IEEE Standard for Configuration Management in Systems and Software Engineering [216](#_tabs-<p></p>), 2.1)
5. delivered version of an application which includes all or part of an application 
   1. (IEEE Std 828-2012, IEEE Standard for Configuration Management in Systems and Software Engineering [216](#_tabs-<p></p>), 2.1)
6. set of grouped change requests, established in the Application Change Management Process, which are designed, developed, tested, and deployed as a cohesive whole 
   1. (ISO/IEC 16350:2015 - Information technology — Systems and software engineering — Application management [412](#_tabs-<p></p>), 4.28)
7. distribution of a product increment to a customer or users 
   1. (ISO/IEC TR 24587:2021 - Software and systems engineering — Agile development — Agile adoption considerations [423](#_tabs-<p></p>)ISO/IEC TR 24587:2021 - Software and systems engineering — Agile development — Agile adoption considerations [423](#_tabs-<p></p>), 3.13)

**Example:**source code, code for execution, or multiple software assets packaged into an internal production release and tested for a target platform, test release 

Release management includes defining acceptable quality levels for release, authority to authorize the release, and release procedures. See Also: version

**3.1.2 IEEE definition for version.**

1. (1) initial release or re-release of a computer software configuration item, associated with a complete compilation or recompilation of the computer software configuration item (IEEE Std 828-2012, IEEE Standard for Configuration Management in Systems and Software Engineering [216](#_tabs-<p></p>), 2.1)
2. (2) initial release or complete re-release of a document, as opposed to a revision resulting from issuing change pages to a previous release (IEEE Std 828-2012, IEEE Standard for Configuration Management in Systems and Software Engineering [216](#_tabs-<p></p>), 2.1)
3. (3) operational software product that differs from similar products in terms of capability, environmental requirements, and configuration (ISO/IEC/IEEE 24765:2017 Systems and software engineering – Vocabulary [230](#_tabs-<p></p>))
4. (4) identified instance of a configuration item (ISO/IEC TR 18018:2010 - Information technology — Systems and software engineering — Guide for configuration management tool capabilities [429](#_tabs-<p></p>), 3.15)
5. (5) unique string of number and letter values indicating a unique revision of an item (ISO/IEC 19770-5:2015(en) Information technology — IT asset management — Overview and vocabulary [059](#_tabs-<p></p>), 3.54)

Versions often identify revisions of software that provide unique functionality or fixes. A version typically has multiple parts, such as a major version, indicating large changes in functionality or user interface changes, and a minor version, indicating smaller changes in functionality or user interface changes.

## 3.2 Release Management Procedures

#### **3.2.1 Preparation of the Release Package**

Preparation involves verifying and assembling all components necessary for the deployment of the release. Proper preparation ensures that deliverable software meets all compliance and quality requirements.

##### **Preparation Activities:**

A checklist can be established to streamline preparation of the release package. Activities to consider include:

1. **Approval and Verification:**

   * Confirm proper approvals have been documented and signed off.
     + **Software Assurance Approval:** Ensure objective evidence of readiness for operational use is provided.
     + **Configuration Management Approval:** Ensure authorized Change Control Board (CCB) members approve all changes included in the release.
2. **Data and Documentation:**

   * Ensure the **Acceptance Data Package** is complete and includes required artifacts, such as:
     + Version Description Document (VDD).
     + Training materials, user guides, and operator manuals.
     + Installation documents, including special considerations for customizations or configurations.
     + Release notes summarizing changes, known issues, and installation instructions.
3. **Configuration Audit Results:**

   * Confirm all configuration audits (FCA and PCA) have been successfully completed, with non-conformances resolved and documented (see SWE-084).
4. **Deviations and Waivers:**

   * Ensure all approved waivers and deviations are documented in the release package.
5. **Change Requests:**

   * Confirm all change requests (CRs) have been fully developed, tested, verified, and closed.
6. **Legal Compliance:**

   * Address any licensing or export regulations, including ITAR considerations, as needed.
7. **Site Readiness:**

   * Ensure installation sites are prepared and pre-installation visits are conducted where applicable.
   * Verify trained personnel are available for troubleshooting and support.

---

#### **3.2.2 Creation and Delivery of the Release Package**

Once preparation is complete, formal procedures guide the creation, validation, and delivery of the release package to customers or users. This phase is critical for ensuring consistency, security, and usability of deliverable software.

##### **Creation Procedures:**

1. **Scope Definition:**

   * Identify all CIs included in the release, their versions, revisions, and dependencies.
2. **Tool and Software Settings:**

   * Specify compilers, linkers, operating systems, macros, libraries, and environmental parameters required to build the release.
3. **Master Copy Creation:**

   * Clearly document procedures for generating the master release package, including the format, layout, and media type (e.g., USB drives, DVDs, cloud distribution).
   * Verify the master copy contains all intended items using comparison techniques (e.g., checksum validation, CI traceability).
4. **Replication:**

   * Document replication procedures for producing additional copies, ensuring consistency with the master copy.
   * Confirm copies match the master via testing and quality assurance processes (e.g., byte-level checks or selective validation tests).
5. **Security Measures:**

   * Conduct virus checks and ensure compliance with secure handling procedures.

#### **Delivery Procedures:**

1. Define delivery responsibilities, including logistics (e.g., shipping methods) and installation schedules for customer sites.
2. Verify installation guides, testing plans, and rollback procedures are included with the release package.
3. Ensure release distribution accounts for full versions, partial releases, and patches, with clear documentation for each type.

---

#### **3.2.3 Storage and Maintenance of the Release Package**

Proper storage and maintenance procedures preserve deliverable software for future use, audits, and long-term operational support.

##### **Storage Guidelines:**

1. **Retention Period:**

   * Establish a policy for retaining the master copy and associated records for the life of the product.
2. **Configuration Management Integration:**

   * Place the master copy and its associated artifacts into the configuration management system under a unique identifier.
3. **Access Control:**

   * Implement access restrictions for sensitive releases or safety-critical items.
4. **Safety and Security Requirements:**

   * Follow procedures for storing critical code and documentation, particularly for safety-sensitive functions.

##### **Maintenance Procedures:**

1. **Version Updates:**
   * Maintain ongoing traceability of updates, patches, or incremental improvements to the original release package.
2. **Release Records:**
   * Include the Version Description Document (VDD), build artifacts, and CI identifiers for reference during audits or debugging efforts.

### **Key Principles Across the Release Lifecycle**

#### **Quality Assurance**

Release management prioritizes compliance with quality benchmarks for testing, traceability, and delivery.

#### **Risk Mitigation**

Managing legal, technical, and operational risks (e.g., configuration errors, installation failures, or regulatory violations) ensures consistent delivery performance.

#### **Traceability**

Detailed release procedures ensure auditability and transparency at every stage.

#### **Collaboration**

Release preparation and delivery benefit from coordinated efforts between development, testing, assurance, and operational teams.

### **References to Related Guidance**

* **SWE-077:** Deliver Software Products.
* **SWE-071:** Configuration Management Requirements Implementation.
* **SWE-084:** Configuration Audits Guidance.
* **NASA-GB-8719.13:** NASA Software Safety Guidebook.
* **IEEE Std 828-2012:** Software Configuration Management.
* **ISO/IEC 12207:2017:** Software Update and Deployment Lifecycle Best Practices.

By following the guidelines above, project managers can establish robust procedures for the storage, handling, delivery, release, and maintenance of deliverable software products, ensuring NASA mission success and compliance with required standards.

See also [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products), [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification),

See also [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting), [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items).

See also Topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report), [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan),

A basic description of data management is provided in [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan).

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting) * [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Configuration Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Configuration+Management) |

# 4. Small Projects

For small projects, implementing procedures for the storage, handling, delivery, release, and maintenance of deliverable software products can be streamlined while still ensuring compliance with NASA requirements. These simplified processes should scale to the smaller team size, limited resources, and reduced complexity of the deliverables, without compromising quality, security, or traceability.

Below is tailored guidance for small projects:

---

### **1. Objectives for Small Projects**

* **Streamline Configuration Management:** Use lightweight tools and processes that maintain basic CM functionality (e.g., version tracking, artifacts control, and traceability) without requiring large-scale systems.
* **Ensure Quality and Integrity:** Establish a simple checklist and maintain minimal but effective documentation to track approvals, testing, and readiness for delivery.
* **Enhance Collaboration:** In smaller teams, communication is critical. Maintain transparency with all stakeholders about upcoming releases and their contents.
* **Mitigate Risks:** Identify the biggest risks (e.g., deploying wrong versions) with minimal personnel and tools and implement safeguards (even if informal) to mitigate them.

---

### **2. Key Process Areas for Small Projects**

#### **2.1 Storage**

##### Recommended Approach for Small Projects:

* Store all deliverables (source code, executables, installation scripts, documentation, etc.) in a single, organized location, such as a version-controlled repository (e.g., Git, Mercurial, or any similar lightweight tool).
* Use **branching strategies** in version control systems to isolate changes (e.g., one branch for stable releases and another for development work).
* Clearly **label versions** with tags or commit messages in the repository (e.g., "v1.0.0-production") to signify approved releases.
* For backup and redundancy, ensure the repository is mirrored to a cloud storage service or an external drive.

##### Resource Tip:

For small teams, a free or low-cost version control hosting site (e.g., GitHub, GitLab, Bitbucket) can be used if requirements for security and compliance are met.

---

#### **2.2 Handling**

##### Recommended Approach for Small Projects:

* Assign a single project member to act as the **configuration manager** or release focal point, responsible for documenting and controlling all artifacts.
* Use an **approval checklist** before moving files between environments (e.g., development → testing → production) to ensure proper processes have been followed.
* Clearly document any environmental changes or software dependencies required to execute the deliverable software.

##### Example Checklist for Handling:

* Verify the **appropriate version** of the software is selected for testing or delivery.
* Verify compatibility with the target environment (e.g., operating system, database, or hardware platform).
* Ensure any required licenses, third-party libraries, or dependencies are tracked and included where applicable.

---

#### **2.3 Delivery**

##### Recommended Approach for Small Projects:

* Define simple steps for creating a **release package**, which can be a compressed archive (e.g., zip file), a deployment script, or other format appropriate for the project.
* Include all necessary components:
  + Application/software executables.
  + User manuals and installation guides.
  + Any required testing data or test results to demonstrate readiness.
* Deliver the software through a controlled channel:
  + Secure email with encryption.
  + A trusted hosting platform (e.g., a secured and authorized portion of the repository platform).
  + A physical medium, such as USB drives, for highly secure environments.
* Record delivery details (who, when, and how) in a shared project log for traceability.

##### Emphasis on Security:

* If delivering software externally, confirm compliance with any export control regulations (e.g., International Traffic in Arms Regulations [ITAR]).
* Verify distribution files for viruses or malware before delivery.

---

#### **2.4 Release**

##### Recommended Approach for Small Projects:

* Establish a **lightweight release process** tailored to the project size:
  + Ensure the deliverable software has been tested and verified.
  + Secure approvals from the project lead and software assurance focal points.
  + Prepare a minimal **Version Description Document (VDD)** to accompany the release, even if it’s structured as a simple document listing:
    - The release identifier (e.g., "v1.1.0-beta").
    - Changes or updates included in the release.
    - Known issues or limitations.
    - Verification results specific to testing for this release.

##### Internal vs. External Releases:

* For internal releases (e.g., testing milestones), emphasize speed and practicality (e.g., share the latest version on a shared drive), but still retain version control.
* For external releases to customers/users, track formal delivery checkpoints (e.g., a signed email confirmation or delivery receipt).

---

#### **2.5 Maintenance**

##### Recommended Approach for Small Projects:

* For released software, maintain a **single source** of truth for the deliverable software in the configuration management system. Archive past versions for traceability and auditing.
* Maintain a lightweight tracking tool for:
  + Bug reports or issue logs (e.g., a shared spreadsheet or simple tools like Trello, Jira, GitHub Issues).
  + Requests for minor updates or patches.
  + Changes made after the original release (trace them back to the appropriate version).
* Prepare a simple plan for applying patches or updates to previously delivered software versions, especially for scenarios where users cannot easily apply updates independently.

##### Pro Tip:

Establish a **periodic review plan**, even if informal. For longer-lived projects, review maintenance needs every 6–12 months to confirm the software remains functional and secure.

---

### **3. Simplified Release Management Procedures**

#### **3.1 Preparation for a Release**

For small projects, simplify the preparation phase:

* Use a basic **pre-release checklist** that ensures approved and tested software is ready for deployment.
* Example activities include:
  + Obtaining necessary approvals (from the project lead and software assurance focal point).
  + Ensuring proper documentation is included (even briefly).
  + Verifying all dependencies (e.g., libraries) are properly packaged or referenced.

---

#### **3.2 Creating and Delivering the Release**

* Keep it simple:
  + Create a zip file or other standard file format containing all configuration items and instructions.
  + Test the release package in a clean (production-similar) environment before delivery.
  + Deliver the package securely, ensuring logs or emails document the recipient and method.

---

#### **3.3 Storage and Archiving**

* Retain the **final release package** and its version-controlled artifacts (source code, VDD, etc.) in the repository under a specific folder or branch.
* Archive superseded versions (but do not delete them) for traceability.

---

### **4. Tools and Practices for Small Projects**

* **Version Control Systems (VCS):** Use Git or a similar lightweight VCS for tracking code and configuration changes.
* **File Encryption Tools:** Tools like 7-Zip can be used to encrypt and password-protect release packages for secure delivery.
* **Simple Checklists or Templates:** Develop reusable release checklists to guide preparation, delivery, and follow-up for each release cycle.

---

### **5. Scale-Appropriate Metrics**

Small projects should track a limited set of simple metrics to ensure compliance and identify areas for improvement:

* **Number of Releases Delivered (Planned vs. Actual).**
* **Number of Open/Resolved Issues per Release.**
* **Time to Close Critical Bugs in Maintenance.**

---

### **6. Final Recommendations**

* **Keep It Lightweight:** Use only necessary procedures that align with the project size, but ensure traceability and quality remain priorities.
* **Balance Formality:** Maintain enough documentation and approvals to support audits without creating unnecessary overhead.
* **Monitor Success:** Periodically review the simplicity and effectiveness of these processes with your team.

By streamlining release management procedures to align with the scope of a small project, teams can efficiently meet the technical, quality, and traceability requirements of Requirement 5.1.8.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document, EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. See Chapter 13. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-059)

  [ISO/IEC 19770-5:2015(en) Information technology — IT asset management — Overview and vocabulary](https://www.iso.org/obp/ui/#iso:std:iso-iec:19770:-5:ed-2:v1:en "Click to open in new window")

  ISO/IEC 19770-5:2015(en), Information technology — IT asset management —
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-212)

  [IEEE Guide to Software Configuration Management,](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=89631&tag=1 "Click to open in new window")

  IEEE Computer Society, IEEE STD 1042-1987, 1987.  This link requires an account on the NASA START (AGCY NTSS) system (https://standards.nasa.gov ). Once logged in, users can access Standards Organizations, IEEE and then search to get to authorized copies of IEEE standards.
* (SWEREF-216)

  [828-2012 - IEEE Standard for Configuration Management in Systems and Software Engineering](https://ieeexplore.ieee.org/document/6197683 "Click to open in new window")

  IEEE STD IEEE 828-2012, 2012.,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-230)

  [ISO/IEC/IEEE 24765:2017 Systems and software engineering -- Vocabulary.](https://www.iso.org/standard/71952.html "Click to open in new window")

  ISO/IEC/IEEE 24765:2017  It was prepared to collect and standardize terminology. Copy attached.
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
* (SWEREF-337)

  [Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf "Click to open in new window")

  Souppaya, Murugiah, Scarfone, Karen, NIST Special Publication NIST SP 800-40r4, April, 2022
* (SWEREF-343)

  [STEP Level 2 Software Configuration Management and Data Management course, SMA-SA-WBT-204, SATERN (need user account to access SATERN courses).](https://saterninfo.nasa.gov/ "Click to open in new window")

  This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022
* (SWEREF-412)

  [ISO/IEC 16350:2015 - Information technology — Systems and software engineering — Application management](https://www.iso.org/standard/57922.html "Click to open in new window")

  ISO 16350:2015 establishes a common framework for application management processes with well-defined terminology that can be referenced by the software industry.
* (SWEREF-415)

  [ISO/IEC/IEEE 12207:2017 - Systems and software engineering — Software life cycle processes](https://www.iso.org/standard/63712.html "Click to open in new window")

  ISO/IEC/IEEE 12207:2017 also provides processes that can be employed for defining, controlling, and improving software life cycle processes within an organization or a project.
* (SWEREF-423)

  [ISO/IEC TR 24587:2021 - Software and systems engineering — Agile development — Agile adoption considerations](https://www.iso.org/standard/79011.html "Click to open in new window")

  This document provides an overview of agile readiness factors that are likely to determine whether an organization, project, product or team is ready to start the transition to using an agile approach to their system and software development and maintenance activities.
* (SWEREF-429)

  [ISO/IEC TR 18018:2010 - Information technology — Systems and software engineering — Guide for configuration management tool capabilities](https://www.iso.org/standard/51042.html "Click to open in new window")

  ISO/IEC TR 18018:2010 provides guidance in the evaluation and selection for CM tools during acquisition.
* (SWEREF-526)

  [Software Design for Maintainability](https://llis.nasa.gov/lesson/838 "Click to open in new window")

  Public Lessons Learned Entry: 838.
* (SWEREF-541)

  [Computer Hardware-Software/International Space Station/Software Configuration Management](https://llis.nasa.gov/lesson/1130 "Click to open in new window")

  Public Lessons Learned Entry: 1130.
* (SWEREF-574)

  [Place Flight Scripts Under Configuration Management Prior to ORT](https://llis.nasa.gov/lesson/2476 "Click to open in new window")

  Public Lessons Learned Entry: 2476.
* (SWEREF-580) COTS Change Processing Lessons Learned Entry:3457. No longer available
* (SWEREF-585)

  [International Space Station (ISS)/Multiple Element Integrated Testing (MEIT)/Software Configuration Management Public Lessons Learned Entry: 1165.](https://llis.nasa.gov/lesson/1165 "Click to open in new window")

  In NASA Engineering Network.
* (SWEREF-586)

  [Redundant Verification of Critical Command Timing (1995) Public Lesson Learned Entry: 559.](https://llis.nasa.gov/lesson/559 "Click to open in new window")

  Public Lessons Learned Entry: 559.
* (SWEREF-587)

  [Reuse of Analysis Software](https://llis.nasa.gov/lesson/2158 "Click to open in new window")

  Public Lessons Learned Entry: 2158.
* (SWEREF-588)

  [Institutional Configuration Management Organization,](https://llis.nasa.gov/lesson/4516 "Click to open in new window")

  Public Lessons Learned Entry: 4516.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The lessons learned database entries provide valuable insights that can help shape better procedures for software storage, handling, delivery, release, and maintenance. Below, each lesson is summarized with its relevance to release management, followed by suggestions for applying these lessons to future projects.

---

### **NASA Lesson Learnings Analysis and Application**

#### **1. Source Code Access and Supplier Agreements (Lesson No. 1130)**

**Key Point:**  
NASA does not have source code access for all partner-delivered software for the ISS due to concerns over proprietary data protection. This lack of access creates challenges during anomaly resolution, as visibility into the source code is critical for diagnosing and fixing issues.

**Relevance:**

* Insufficient source code visibility can hinder post-release maintenance, anomaly resolution, and operational updates.
* Supplier agreements that fail to mandate appropriate levels of source code access can increase project risks, especially when working with international partners.

**Application to Release Management:**

* **Source Code in Supplier Contracts:** Ensure supplier agreements require a pre-negotiated level of source code access for anomaly resolution or updates, incorporating appropriate non-disclosure agreements (NDAs) to protect proprietary data.
* **Escrow Agreements:** Establish source code escrow arrangements, where partners submit source code to a trusted third party to be released to NASA under predefined conditions (e.g., unresolved anomalies or supplier dissolution).
* Incorporate access requirements in the **Configuration Management Plan** to ensure consistent management of both proprietary and shared code.

---

#### **2. Configuration Control for Flight Scripts (Lesson No. 2476)**

**Key Point:**  
Flight scripts not placed under configuration control early in the development process caused proliferation of multiple uncoordinated script versions, leading to confusion and delays in missions like MER, Juno, and GRAIL.

**Relevance:**

* A lack of early configuration management can lead to inconsistencies during software testing, delivery, and operational use.
* Controlling scripts and configuration items early mitigates risks of operational confusion.

**Application to Release Management:**

* **Configuration Management of Scripts:** Place flight scripts or related artifact subsets under strict configuration control early in the project lifecycle (prior to Operational Readiness Testing). This prevents the propagation of unapproved script versions.
* **Version Control Tools:** Use lightweight and user-friendly version management systems to track script updates and ensure only approved versions are used.
* **Release Procedures:** Include a validation step that ensures all script versions in the release package are consistent with configuration control records.

---

#### **3. COTS Change Management (Lesson No. 3457)**

**Key Point:**  
Routine patches and changes to commercial-off-the-shelf (COTS) components often cannot follow time-intensive configuration processes designed for custom software. The management of both COTS and custom products requires differentiated CM practices.

**Relevance:**

* Standard CM tools and practices for custom software may not meet the rapid update cycles and vendor-defined schedules for COTS patching.

**Application to Release Management:**

* **Separate Processes for COTS:** Establish a streamlined configuration management process for COTS patches that accounts for their time-sensitive nature while still maintaining traceability.
* **Patch Validation:** Even for expedited COTS patches, require basic regression testing in a staging environment to assess compatibility with custom software.
* **Coordination with Vendors:** Engage early with COTS vendors to identify anticipated update cycles and integrate this into project release planning.

---

#### **4. Software Design for Maintainability (Lesson No. 0838)**

**Key Point:**  
Large and complex software systems become increasingly difficult to maintain over time. Maintenance should not be treated as an afterthought—it must be built into software design from the start.

**Relevance:**

* Poorly designed software can lead to maintenance bottlenecks and operational risks post-release.
* Post-release maintenance depends on the design’s support for modular adjustments, debugging, and enhancements.

**Application to Release Management:**

* **Maintainable Design Principles:** During development, enforce coding standards geared toward improving modularity, documentation, and ease of updates (e.g., adherence to NASA's software engineering best practices).
* **Maintenance Readiness Checklist:** Integrate a pre-release verification step to assess the maintainability of the software, including modularity and internal documentation.

---

#### **5. Testing Under Operational Loads (Lesson No. 1165)**

**Key Point:**  
Due to time constraints, regression testing of the ISS’s PCS software under operational loads may only be performed briefly, limiting discovery of configuration incompatibilities that arise during testing.

**Relevance:**

* Limited regression testing under operational loads increases the risk of post-release failures or unexpected operational issues.

**Application to Release Management:**

* **Extend Operational Testing with Automation:** Automate as much of the regression testing process as possible to maximize test coverage within short time frames.
* **Staged Rollout Strategy:** Begin with incremental, staged deployments in operational environments to reduce risks of system-wide issues.
* Ensure that critical release artifacts undergo stress testing under operational workloads before approval.

---

#### **6. Verification of Critical Command Timing (Lesson No. 559)**

**Key Point:**  
A launch mission was terminated because of an overlooked software patch during inflight updates, which led to missed command timing. An independent watchdog timer was not implemented due to resource constraints.

**Relevance:**

* Skipping redundant or independent checks for software release quality can lead to catastrophic mission failure.

**Application to Release Management:**

* **Redundancy in Validation:** Require independent verification/validation of critical software commands, functionalities, and patches before deployment.
* **Watchdog Systems:** Design fail-safes or other methods to monitor command execution timing to prevent single-point failures.

---

#### **7. Institutional Configuration Management Consistency (Lesson No. 4516)**

**Key Point:**  
Inconsistent configuration and data management (CDM) practices across programs and centers lead to inefficiencies in transaction, integration, and compliance reporting.

**Relevance:**

* Uniformity in tools, guidelines, and practices allows seamless coordination across stakeholders working on software releases.

**Application to Release Management:**

* **Centralized Governance:** Establish a center-level CDM organization that provides consistent standards and tools for release management and CM practices.
* **Unified Tools:** Use consistent tools and platforms for managing release-related data across programs.

---

#### **8. Independent Review for Reuse of Software (Lesson No. 2158)**

**Key Point:**  
Reusing analytical software without thoroughly reviewing its suitability and compatibility with new interfaces can lead to integration issues.

**Relevance:**

* Reusing legacy or existing software increases risk if new contexts or interfaces are not thoroughly validated.

**Application to Release Management:**

* **Validation of Reused Software:** Before including reused software in a release, perform independent reviews to validate compatibility with newly designed systems.
* **Release Documentation:** Explicitly identify reused artifacts in release notes, highlighting their traceability and adjustments made for the new application.

---

### **Summary Recommendations:**

1. Negotiate source code access or escrow for proprietary deliveries to ensure adequate anomaly resolution.
2. Implement stringent configuration control for all artifacts, including flight scripts and reused CIs.
3. Adapt COTS configuration management to meet the unique challenges of vendor-driven update models.
4. Prioritize software design principles that simplify post-release maintenance and feature updates.
5. Incorporate robust validation and pre-release operational testing under realistic conditions.
6. Pursue institutional consistency in release management tools and practices.
7. Utilize redundancy in software verification for critical operational sequences.

By treating these lessons as actionable guidance, NASA projects can achieve enhanced reliability, traceability, and supportability of deliverable software products.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Apply Change Management principles to test hardware/software](https://software.gsfc.nasa.gov/lesson-details/65/).**Lesson Number 65**: The recommendation states: "Apply Change Management principles to test hardware/software."
* [Simulations/rehearsals with the SC and execute re cover prior to launch](https://software.gsfc.nasa.gov/lesson-details/94/). **Lesson Number 94**: The recommendation states: "Execute simulations/rehearsals with the SC where EEPROM is loaded (to all available processors/banks of EEPROM) and execute recovery prior to launch."
* [Ability to load to EEPROM without booting Spacecraft processor](https://software.gsfc.nasa.gov/lesson-details/95/). **Lesson Number 95**: The recommendation states: "It would be desirable to be able to load to EEPROM without booting Spacecraft processor. Likewise, it would also be beneficial to be able to load to the backup processor without switching control from the Primary."
* [Incorporate automation into operations prior to launch](https://software.gsfc.nasa.gov/lesson-details/98/).**Lesson Number 98**: The recommendation states: "Incorporate automation into operations prior to launch, instead of waiting until after launch."
* ["Day in the Life" simulations using automation prior to launch](https://software.gsfc.nasa.gov/lesson-details/99/).**Lesson Number 99**: The recommendation states: "Execute "Day in the Life" simulations using automation prior to launch."
* [Configuration Management of Ops Products should NOT be a manual process](https://software.gsfc.nasa.gov/lesson-details/100/). **Lesson Number 100**: The recommendation states: "Configuration Management of Ops Products should NOT be a manual process."
* [Plan for the impacts of assembling and moving the Flight Software simulator](https://software.gsfc.nasa.gov/lesson-details/108/). **Lesson Number 108**: The recommendation states: "Plan for the impacts of assembling and moving the Flight Software simulator."
* [Integrate FSW builds into I&T earlier than later](https://software.gsfc.nasa.gov/lesson-details/130/). **Lesson Number 130**: The recommendation states: "Integrate FSW builds into I&T earlier than later."
* [Understand configuration differences between ground stations](https://software.gsfc.nasa.gov/lesson-details/138/). **Lesson Number 138**: The recommendation states: "Understand any configuration differences between ground stations - and test accordingly pre-launch."
* [Include a requirement for spacecraft FSW to provide the capability to update the flight code without mission interruption](https://software.gsfc.nasa.gov/lesson-details/156/). **Lesson Number 156**: The recommendation states: "When developing or acquiring spacecraft flight software, the design should provide the capability to update the flight software (in RAM and EEPROM) without impacting current mission data collection or pointing (i.e., without interrupting the mission due to entering safe hold)."
* [Consider PROM based boot loaders to support updates to non-volatile memory](https://software.gsfc.nasa.gov/lesson-details/238/). **Lesson Number 238**: The recommendation states: "There is and always has been the possibility of corrupting a non-volatile FSW image (error in FSW, error in load, error in command, error in command sequence, adversarial actions, etc.).  In addition, EEPROMs have a data retention issue which would corrupt the FSW image. Given enough time EEPROMs can lose their charge. This is normally not a concern except in harsh environments like space.   Also, board designs can allow EEPROM corruption during power down sequences (some board designs protect against this). Ideally there would be a way to reload a non-volatile image via a method that cannot be corrupted, such as a PROM based boot loader (PROM is a fused chip and not subject to accidental/intentional modification, radiation upset, data retention, or any other modification)."
* [Store NTRs in project repository](https://software.gsfc.nasa.gov/lesson-details/297/). **Lesson Number 297**: The recommendation states: "Store New Technology Reports (NTRs) in the project repository, so information is available and can be reused later, when new NTRs need to be submitted for innovations/changes to the same software."
* [Establish processes early in development](https://software.gsfc.nasa.gov/lesson-details/331/). **Lesson Number 331**: The recommendation states: "Establish development and testing methodology and process early in the lifecycle."

# 7. Software Assurance

**SWE-085 - Release Management**

5.1.8 The project manager shall establish and implement procedures for the storage, handling, delivery, release, and maintenance of deliverable software products.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project establishes procedures for storage, processing, distribution, release, and support of deliverable software products.

2. Perform audits on the project to ensure that the project follows defined procedures for deliverable software products.

## 7.2 Software Assurance Products

This guidance refines and expands existing Software Assurance (SA) practices for Requirement 5.1.8, enhancing clarity, ensuring comprehensive coverage, and adding actionable steps to strengthen software assurance deliverables and processes. Additionally, lessons from previous missions and industry standards are integrated to make the guidance more robust and applicable to real-world scenarios.

The following items represent the deliverables and outcomes of software assurance activities for this requirement. These products aim to ensure proper configuration management and compliance during all stages of software release and maintenance:

#### **Enhanced List of Software Assurance Products:**

1. **Software Configuration Management Baseline and Process/Procedure Audit Report:**

   * Results, findings, and recommendations from audits assessing adherence to configuration management (CM) processes and procedures.
   * Identification of risks, issues, and improvement opportunities in CM practices.
2. **Software Configuration Management Plan Review:**

   * Validation of the Software Configuration Management Plan (SCMP) to confirm its adequacy, completeness, and compliance with NPR 7150.2 and Center-specific requirements.
   * Identification of areas where CM procedures or baselining controls need to be improved.
3. **Defect and Problem Reporting Data:**

   * Audit trail of problem reports (PRs), defect logs, and how these issues are addressed and tracked through closure using the CM system.
   * Trend analysis of defect rates to identify process inefficiencies.
4. **Audit Results for Configuration Management Processes:**

   * Audit summaries evaluating the performance and consistency of CM processes as they relate to software storage, handling, release, and delivery.
   * Ensure that configuration items (CIs), baselines, and documentation are managed in a secure and controlled manner.
5. **Software Data File Location and Integrity Information:**

   * Recorded details on where all key artifacts are stored (e.g., repositories, backup systems), ensuring traceability and accessibility.
6. **Software Version Description Document (VDD):**

   * Confirm that the VDD for every release clearly defines:
     + Version identifiers, baseline scope, changes, and testing status.
     + Target environments, operational constraints, and installation instructions.
7. **Configuration Audit Verification Reports (FCA/PCA):**

   * Findings and sign-off results from Functional and Physical Configuration Audits to validate that baselines and software delivery match requirements and comply with project needs.

## 7.3 Metrics

Metrics are critical tools for monitoring compliance, assessing trends, and identifying process gaps. Improved Software Assurance metrics include:

#### **Key Software Assurance Metrics:**

1. **Compliance Metrics:**

   * Number of **Compliance Audits Planned vs. Performed**: Tracks how well projects adhere to planned compliance audits.
   * Number of **Non-Conformances in Process Audits**: Identifies gaps in procedures across the project lifecycle.
2. **Non-Conformance Metrics:**

   * Number of software **Non-Conformances Detected in Release Documents** (e.g., VDDs, delivery instructions) broken down into "Open" and "Closed."
   * **Non-Conformance Resolution Trends:** Track the number of open/closed non-conformances over time to assess resolution effectiveness.
3. **Process Health Trends:**

   * Number of **Non-Conformances per Audit**, including findings from CM processes, standards compliance, and work product audits.
   * **Trend Analysis:** Track the number of Process/Standards Audits, open compliance issues, and their resolution rates over time.
4. **Software Delivery Health Metrics:**

   * Number of **Open vs. Closed Audit Non-Conformances**, related to releases over time.
   * Trends in the **Number of Risks Identified During Release Phases** and their mitigations.

#### **See also:**

Topic 8.18 - Software Assurance Suggested Metrics for additional examples and tailoring guidance.

## 7.4 Guidance:

Software Assurance workflows ensure compliance, verification, and quality in processes related to software release, storage, handling, maintenance, and delivery. The following steps build on the original guidance and provide additional detail.

#### **Task 1: Review Project Documentation**

* **Purpose:** Confirm that project-level processes and procedures address the tasks of storage, handling, release, delivery, and maintenance.
* **Approach:**
  + Review documents such as:
    - Software Development/Management Plan (SDP/SMP).
    - Software Configuration Management Plan (SCMP).
    - Data Management Plan.
    - Maintenance Plans or Center Procedure References.
  + Identify project-specific tailoring of Center-level processes. Ensure those adaptations are compliant with NPR 7150.2 and any additional Center or Agency requirements.
* **Lesson Applied:** Clearly document how processes are tailored for unique project challenges (e.g., hybrid workflows involving both legacy and COTS software).

#### **Task 2: Perform Configuration Management and Release Audits**

* **Purpose:** Ensure that established CM procedures are followed during software development and release cycles.
* **Approach:**
  + Plan and execute **process/procedure audits**, ensuring that project teams adhere to approved processes for storing, baselining, and releasing software.
  + Perform **pre-delivery audits** such as:
    - Functional Configuration Audit (FCA): Confirm the completeness and accuracy of software functional capabilities against documented baselines.
    - Physical Configuration Audit (PCA): Confirm that deliverables (source code, binaries, and documentation) reflect the approved baselines and meet project requirements.
  + Conduct periodic CM audits to ensure that storage, baselining, and procedure adherence remain consistent throughout the lifecycle.
  + Share audit outcomes (including risks, issues, and recommendations) with project teams promptly.

**See Also:**  
Guidance in Topic 8.12 (Basics of Software Auditing) and SWE-084 (Configuration Audits).

#### **Task 3: Verify and Sign-Off on Delivery Documentation**

* **Purpose:** Validate all software delivery artifacts and ensure that delivery conditions meet requirements.
* **Approach:**
  + Ensure that the FCA and PCA confirm successful completion of all pre-delivery activities.
  + Verify the following:
    - Acceptance of software based on test plan criteria and technical requirements.
    - Delivery matches NPR 7150.2, NASA-STD-8739.8, and other applicable standards.
    - Configuration audits capture all open issues, defects, and deviations.
  + Confirm readiness of the operations/maintenance environment:
    - Validate resource availability, including licenses, simulators, and test equipment.
    - Ensure integrity of the installed software by comparing installation artifacts (files, data, configurations) with delivery documentation.
  + Validate the completeness and usability of operations and maintenance documents, including licenses, reuse elements (e.g., open-source, glueware), and tools.

#### **Task 4: Assurance for Operations, Maintenance, and Retirement**

* **Purpose:** Maintain oversight of software processes post-delivery, ensuring readiness of maintenance and retirement processes.
* **Approach:**
  + Verify that planned processes for operations, maintenance, and retirement are adhered to and that they align with requirements for safety, reliability, and NPR 7150.2 compliance.
  + Review and sign off on approved software changes, ensuring:
    - Risks to quality, safety, and project reliability are mitigated.
    - Regression testing is conducted for any changes.
    - "As-built" documentation reflects approved changes, ensuring traceability.
  + Oversee software retirement to ensure:
    - All software and documentation are archived.
    - Licenses and resources are transferred or canceled.
    - Physical assets in labs (e.g., equipment) are securely disposed of or repurposed.

### **Key Enhancements to Guidance:**

1. **Audit Integration:** Regular audits ensure compliance across lifecycle phases, emphasizing pre-release checks such as FCA/PCA and ongoing configuration monitoring.
2. **Proactive Metric Monitoring:** Track metrics for process audits, non-conformance resolution, and delivery compliance to highlight trends and refine processes in real time.
3. **Tailored Oversight:** Adapt Center-level procedures to meet project-defined needs while maintaining strict adherence to NASA standards.
4. **Lifecycle Alignment:** Include assurance activities spanning development, post-delivery maintenance, and retirement to ensure traceability and operational continuity.

By refining these software assurance activities and deliverables, the project’s software release, storage, and maintenance processes will align more effectively with NASA’s quality and compliance expectations.

Some of the activities and conditions that need to be considered are below:

* The software is accepted. Generally, the software is considered when it has met the acceptance criteria as defined in the test plan, satisfies the technical requirements, and meets the requirements in NPR 7150.2, NASA-STD-8739.8 [278](#_tabs-<p></p>), and any Center-level requirements, and any additional contract, MOA, or MOU software requirements. Software acceptance can be rolled into the system acceptance as long as the software has all been tested and signed off by software assurance as concurrence indicates the software meets the requirements for SW quality, SW safety, SW reliability, SW security, and SW V&V, and SW IV&V.
* Software assurance has evaluated and concurred that Project/Provider has satisfactorily completed SW and system verification and validation plans and procedures and that test results are acceptable for the target environment and the intended software use.
* Software assurance has verified SW deliveries by conducting or participating in (and signing off on) the execution of configuration audits, such as Functional Configuration Audit (FCA) and Physical Configuration Audit (PCA). Software Assurance accepts or rejects SW deliveries based on the state of the SW resolution of DRs/PRs and any outstanding risks and satisfactory completion of any safety and reliability verifications.
* Software assurance has verified the integrity of SW installations against the delivery documentation, data checks, operational set-up, and configuration managed versions.
* Software assurance has assured that the operations and maintenance environment is prepared for software delivery, installation, operations, and maintenance including the transfer or acquisition of resources (e.g., licenses, test benches, simulators) necessary to conduct operations and maintenance.

SA should assure that the delivered SW is placed under configuration control and for OTS or reuse SW, that all processes for baselining and assuring the acquired SW, including any wrappers, glueware, or applications that may run on the OTS, are secure, documented and under configuration control.

* Software assurance confirms that any operations or maintenance documents are complete, usable, and delivered, including such information as licenses, simulators, models, COTS, open-source, tools, or reuse code incorporated or used, as applicable.

Software assurance will do the following activities and deliverables for the operations, maintenance, and retirement of the software:

* Assure that the processes for maintenance and retirement are being followed as per their plans
* Assure that the plans for maintenance, operations, and retirement are complete.
* Review changes approved for implementation during maintenance and confirm that:
  + Changes will not impact Project risk posture concerning quality, safety, reliability, security, or NPR 7150.2 compliance
  + Changes are being tested thoroughly, including regression testing
  + Approved changes are documented and reflected in “as-built” documentation
  + Document and raise to the Project any issues, risks, or concerns
* Confirm that retirement is carried out as per the retirement plan and that:
  + All software and documentation are archived
  + Licenses are transferred or canceled
  + Any equipment or furniture in associated labs is properly transferred or disposed of
  + Report on any issues, concerns

Every task that involves performing an audit should also clarify that all audit findings are promptly shared with the project and will be addressed in the handbook guidance.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting) * [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence serves as documentation or artifacts that demonstrate compliance with Requirement 5.1.8. These artifacts ensure accountability, traceability, and adherence to NASA's standards for software storage, handling, delivery, release, and maintenance.

---

### **Evidence Categories**

Objective evidence can be divided into certain categories corresponding to each aspect of the requirement (storage, handling, delivery, release, and maintenance). Each category includes examples of artifacts that demonstrate compliance.

---

#### **1. Storage**

Evidence that software and related artifacts are securely stored with appropriate configuration controls.

* **Configuration Management System Records:**

  + Version-controlled repositories (e.g., Git, SVN) showing storage of source code, binaries, and artifacts.
  + Logs of changes or updates made to stored files, including timestamps and user identifiers.
  + Archived configurations and baselines demonstrating traceability through the lifecycle.
* **Storage Security Documentation:**

  + Evidence of access controls applied to repository data (e.g., role-based access permissions, encryption).
  + Backup plan documentation showing redundancy procedures, recovery targets, and backup logs.
* **Data File Location Evidence:**

  + Documented storage locations for software artifacts, including directories for build versions, test data, release packages, and documentation.

---

#### **2. Handling**

Evidence of activities ensuring proper treatment and tracking of software between environments and stakeholders.

* **Approval Records:**

  + Signed Change Control Board (CCB) approvals for configuration changes and artifact updates.
  + Evidence of stakeholder agreement for changes in stored or handled artifacts.
* **Test Environment Logs:**

  + Documentation showing how software was packaged for testing, including handling of dependencies, configurations, and external libraries.
* **Tracking of Intermediate Versions:**

  + Logs showing movement of software artifacts between development, integration, testing, and production environments.
  + Environment-specific validation results confirming proper handling of configuration items.
* **Handling Procedures Documentation:**

  + A documented process for moving software artifacts between environments, including quality gates and validation criteria.

---

#### **3. Delivery**

Evidence associated with the software delivery process and its approvals.

* **Delivery Documentation:**

  + Signed delivery validation reports confirming that deliverable software matches its intended baseline (e.g., FCA/PCA validation).
  + Software Version Description Document (VDD) detailing version identifiers, release notes, included features, and known issues.
* **Release Package:**

  + Contents of release package (executables, installation scripts, supporting documentation, and test results).
  + Delivery media (cloud links, physical drives) securely documented and verified.
* **Delivery Verification Proof:**

  + Logs of delivery receipts signed by recipients confirming successful handover and readiness for installation.
  + Checklist verifying deployment instructions, installation guidelines, and operational setup.
* **Software Assurance Sign-Off Documentation:**

  + Records showing software assurance approval of release packages, including endorsements of FCA, PCA, and testing validation.

---

#### **4. Release**

Evidence confirming that release procedures are followed and that released software meets all predefined requirements.

* **Release Plan:**

  + Documentation describing the release process, including steps for validation, packaging, testing, approval, and distribution.
* **Functional and Physical Configuration Audit Results:**

  + Audit results confirming that the deliverable software matches its approved baseline and functional requirements.
  + Closure reports for all release issues (open, resolved, or deferred).
* **Traceability Artifacts:**

  + Traceability matrices linking requirements, test cases, code modules, and versions deployed.
  + Logs describing release progression (e.g., staging → external release) and dependencies managed.
* **End-User Documentation:**

  + Installation guides, configuration manuals, and operational instructions delivered alongside the software package.
  + Training materials for end-users, if applicable.

---

#### **5. Maintenance**

Evidence that maintenance processes comply with procedures and preserve software integrity after delivery.

* **Maintenance Records:**

  + Logs detailing all changes applied to released software, including patches, updates, and test results.
  + Regression testing reports and results confirming maintenance activities do not break baseline functionality.
* **Change Approval Documentation:**

  + Signed change requests for all modifications to operational software, including stakeholder and quality assurance approvals.
* **Problem Reports (PRs)/Defect Reports (DRs):**

  + Logs showing issues identified during maintenance, including detailed descriptions, resolutions, and traceability to affected modules.
  + Metrics indicating defects discovered and resolved during maintenance efforts.
* **Retirement Plans:**

  + Documentation of procedures for software retirement, including:
    - Software archiving plans.
    - License transfer or cancellation evidence.
    - Disposal logs for tools and equipment associated with the software.

---

---

### Example Artifacts That Provide Objective Evidence

#### **Configuration Management-Related Artifacts**

1. Version-controlled repositories containing software baselines.
2. Configuration Item (CI) logs, including changes tracked across artifacts.
3. Physical and Functional Configuration Audit Reports signed by software assurance personnel.
4. Backup plans and restoration logs.

---

#### **Release Approval Documentation**

1. VDDs signed off after review and approval.
2. FCA/PCA official sign-off forms.
3. Deployment checklists demonstrating readiness for installation.
4. Delivery receipts or logged acknowledgments from receiving stakeholders.

---

#### **Problem Tracking and Maintenance**

1. Logs from defect tracking systems with resolutions attached.
2. Regression test reports after patches or updates.
3. Approved change requests demonstrating impact assessments for maintenance modifications.
4. Metrics showing trends in defect resolution and open/closed counts during operations.

---

### Additional Sources for Evidence:

1. **Software Assurance Audits**: Reports showing periodic audits of CM systems and procedures.
2. **Risk Management Documentation**: Records showing identified risks during release and mitigation efforts taken.
3. **Project Management Plans**: Plans cross-referenced with SCMP and deployment tasks.

---

### Summary:

Objective evidence illustrates not just compliance but the quality and readiness of software deliverables, from initial storage through delivery, release, maintenance, and retirement. Collecting these artifacts provides a clear picture of adherence to NASA standards and fosters traceability for audits, user confidence, and long-term operational success.

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
