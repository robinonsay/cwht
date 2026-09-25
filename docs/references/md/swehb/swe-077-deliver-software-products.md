# SWE-077 - Deliver Software Products

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695457. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products

SWE-077 - Deliver Software Products

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695457)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695457&showCommentArea=true&showComments=true#addcomment)

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

4.6.3 The project manager shall complete and deliver the software product to the customer with appropriate records, including as-built records, to support the operations and maintenance phase of the software’s life cycle. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-077 History

SWE-077 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.5.4 The project shall complete and deliver the software product to the customer with appropriate documentation to support the operations and maintenance phase of the software's life cycle. |
| Difference between A and B | Added "as-built records" to the scope of coverage. |
| B | 4.6.3 The project manager shall complete and deliver the software product to the customer with appropriate records, including as-built records, to support the operations and maintenance phase of the software's life cycle. |
| Difference between B and C | No change |
| C | 4.6.3 The project manager shall complete and deliver the software product to the customer with appropriate records, including as-built records, to support the operations and maintenance phase of the software’s life cycle. |
| Difference between C and D | No change |
| D | 4.6.3 The project manager shall complete and deliver the software product to the customer with appropriate records, including as-built records, to support the operations and maintenance phase of the software’s life cycle. |

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
| * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) |

# 2. Rationale

The ultimate goal of software development is to provide a product to the customer. Documentation must accompany that delivery to ensure proper understanding, use, and maintenance of the delivered product.

This requirement ensures that the delivered software product is accompanied by comprehensive and accurate documentation to facilitate operations, maintenance, and sustainment activities throughout its lifecycle. Proper documentation and as-built records are crucial for ensuring that the software can be accurately understood, operated, and maintained by the customer or other stakeholders, thereby enabling successful mission outcomes and reducing long-term risks and costs.

---

### **Key Aspects of the Rationale:**

#### **1. Enable Successful Operations**

* Operations teams rely on clear and accurate documentation to operate the software safely and efficiently.
* Providing operational records—such as updated user manuals, release notes, and operational procedures—ensures that the system operates as designed and adheres to mission-critical safety and performance requirements.
* Without complete records, operators may encounter difficulties understanding system behaviors, leading to errors, inefficiencies, or mission failures.

---

#### **2. Reduce Maintenance Risks and Complexity**

* Maintenance activities, such as defect resolution, adaptive updates, and performance tuning, depend on access to the **as-built records** of the software. These records include the design, architecture, source code, configuration settings, test results, and all modifications made during development.
* Providing the customer with thorough as-built documentation ensures maintainers have sufficient insight into the software’s structure and functionality to implement changes without introducing unintended errors.
* Lack of complete as-built records increases the likelihood of miscommunication, longer turnaround times for fixes, and higher maintenance costs over the software’s lifecycle.

---

#### **3. Support Long-Term Sustainability**

* Many NASA software systems are intended for long-term use, sometimes spanning decades. Over time, team members may leave, tools may change, and institutional knowledge may be lost. Comprehensive records allow future teams to sustain and manage the software system effectively, regardless of personnel turnover or reliance on legacy technologies.
* Having the full historical context of the software’s design and development ensures that legacy systems can evolve to meet new mission needs without requiring complete redevelopment.

---

#### **4. Facilitate Verification and Validation (V&V)**

* The as-built records provide the customer and stakeholders with visibility into how the software was developed, validated, and verified. This allows the customer to confirm that the delivered product aligns with the original system requirements and meets safety, reliability, and performance criteria.
* Providing these records ensures traceability between the system’s requirements, design, implementation, and test results, giving the customer confidence in the quality of the delivered product.

---

#### **5. Mitigation of Knowledge Gaps Post-Delivery**

* Proper documentation allows customers to bridge the knowledge gap between the development team and the operations/maintenance team.
* Transferring detailed, verifiable records minimizes the risk of operational or maintenance personnel misunderstanding the system’s intricacies, reducing the risk of introducing errors during operations, updates, or problem resolution.

---

#### **6. Risk Management During Handover**

* A documented handover process that includes as-built records reduces the risk associated with transitioning the software to another entity or team.
* Inadequate documentation at delivery can lead to lost knowledge that would require expensive reverse engineering or a steep learning curve for the new team.
* Clearly organized and complete records reduce the possibility of mission downtime or interruptions during transitional periods.

---

#### **7. Regulatory and Contractual Compliance**

* Many NASA missions are subject to external reviews, audits, and compliance requirements. This requirement ensures that all documentation and records are available and archived to fulfill these obligations.
* Delivering as-built records allows the customer to evaluate adherence to standards, such as NASA-STD-8739.8, NPR 7150.2, or project-specific agreements and protocols. Furthermore, this documentation supports lessons-learned efforts and continuous improvement in other NASA projects.

---

#### **8. Allows for Improved Scalability and Reusability**

* By providing the customer with detailed as-built records, the delivered software is better positioned for scalability or reuse in comparable projects. This aligns with NASA’s goal of efficient resource use and long-term cost-effectiveness.
* Reusable software or components require proper documentation to allow a new development team to adapt them to new mission objectives or hardware platforms.

---

### **Summary of Key Objectives for the Rationale:**

* **Transparency:** Delivering records improves visibility into the software’s capabilities, processes, and design.
* **Operability:** Ensures operators have clear instructions for using the software in a safe and efficient manner.
* **Maintainability:** Provides maintainers with the tools and knowledge to extend the software’s lifecycle and address defects or updates with minimal disruption.
* **Sustainability:** Helps future teams manage the software system regardless of changes in personnel, tools, or technology.
* **Risk Reduction:** Reduces long-term mission risks by mitigating knowledge loss and ensuring proper continuity between development and operational phases.

By meeting this requirement, project management fulfills a critical responsibility to ensure the delivered software product is not only functional at delivery but remains a robust, maintainable, and reliable asset throughout its intended lifecycle.

# 3. Guidance

## 3.1 Delivery Package

This updated guidance builds on the original text to provide additional clarity, structure, and actionable recommendations for creating and delivering a comprehensive software delivery package. It emphasizes the importance of including all necessary artifacts to support software operations, maintenance, and retirement while ensuring consistency, traceability, and quality compliance.

#### **Definition of Delivery Package**

A comprehensive software delivery package is the collection of software artifacts, executable deliverables, and supporting documentation necessary for the customer to operate, maintain, and manage the software effectively throughout its lifecycle. The delivery package should align with the project’s requirements, classification, and contractual obligations, ensuring no critical gaps exist in information transfer.

#### **Typical Contents of a Software Delivery Package**

A typical delivery package includes the following **essential items**:

1. **Software Artifacts:**

   * **Source Code**: Includes all libraries, modules, and scripts required to compile and execute the software.
   * **Executables**: The compiled and tested software product ready for deployment.
   * **Version Description Document (VDD)**: Provides details about the delivered software version, including instructions for recreating the executable software and applying approved modifications.
2. **Core Documentation:**

   * **Final Software User Manual**: Describes the software functionality, operating instructions, reference material, limitations, assumptions, and safety-critical procedures (See Topic 5.12 - SUM - Software User Manual guidance).
   * **As-Built Records**: Documents capturing the final verified and validated state of the software, including requirements verification data, design details, and configuration snapshots.
   * **Change Management Summaries**: History and status of all approved Change Requests since baseline, detailing their impact on the delivered software.
   * **Test Reports**: Summary and results of verification, validation, and performance tests conducted prior to delivery.
   * **Problem Reports**: Summary and analysis of all documented issues encountered during development and their resolutions.
3. **Safety and Risk Artifacts (as applicable):**

   * **Software Safety Plan**: Outlines the procedures for identifying and mitigating risks related to safety-critical elements of the software throughout its lifecycle.
   * **Hazard Analyses**: Detailed assessment of safety risks identified during development and how they are addressed.
   * **Safety Verification Reports**: Summary of safety-related testing and validation undertaken to ensure safety-critical requirements are met.
   * **Open Software-Related Risks**: Documentation of unresolved risks, their implications, and the mitigation or contingency plans in place.
4. **Operational and Maintenance Content:**

   * **Installation Instructions**: Detailed guidance for installing the software, including hardware/environment requirements.
   * **Configuration Files**: Specifies required settings or parameters for the software environment.
   * **Operational Constraints**: Documentation of environmental limitations, dependencies, or conditions under which the software operates correctly.
   * **Training Documentation**: Manuals and materials to support training operators and maintainers.
5. **Additional Deliverables (as necessary for maintenance support):**

   * **Development Environment Details**: Description of specialized hardware, software, or tools needed to compile and modify the delivered software over its lifecycle.
   * **Specialized Testing Equipment**: Any proprietary or mission-specific hardware required for software testing during maintenance.
   * **Maintenance Agreements**: Process and support agreements for ongoing updates or service activities.
6. **Intellectual Property and Licensing:**

   * **Open-Source Licenses**: Reviewed and approved by the Chief of Patent/Intellectual Property Counsel.
   * **Commercial/Government Licenses**: Documentation related to the use of off-the-shelf (OTS) software or licensing restrictions.
7. **Final Project Documentation Archive:**

   * Software Management Plan (SMP), Software Development Plan (SDP), Configuration Management Plan (CMP), Test Plans.
   * Historical Quality Metrics: Summary of quality measures collected throughout the project.
   * Lessons Learned: Insights and recommendations for future projects (particularly related to operations and maintenance).

#### **Ensuring Alignment with Software Classification**

* Tailor the delivery package to the software classification (see SWE-020 - Software Classification). Higher-class software may require more rigorous documentation, safety artifacts, and risk analysis to fulfill compliance obligations.

---

## 3.2 Generating and Delivering the Package

#### **1. Generating the Delivery Package**

* **Use Configuration Management (CM) System:**

  + All delivered software and documentation should be generated or delivered as baselines from the project’s configuration management system to ensure version accuracy and traceability (See SWE-085 – Release Management).
  + The CM system should include verified source code, test results, VDDs, and documentation baselines.
* **Maintain Up-to-Date Documentation:**

  + Ensure documentation is consistently updated throughout the lifecycle to minimize inconsistencies or delivery delays.
  + Near the completion of the lifecycle, review and align all technical documentation with the final delivered software to avoid mismatches.

#### **2. Delivery Package Verification**

* **Perform Pre-Delivery Audits:**

  + Conduct formal audits to verify that "all delivered products are complete, contain the correct versions, and that all discrepancies, openwork, deviations, and waivers are properly documented and approved."
  + Include configuration audits to check the integrity and consistency of baselines stored in the CM system.
* **Ensure Traceability:**

  + Confirm that requirements traceability matrix verifies all baselined requirements have been fulfilled and validated by the as-built software and supporting documentation.
* **Customer Checklists:**

  + Develop delivery acceptance checklists to ensure delivery artifacts meet expectations, minimize risks, and address customer contract requirements.

#### **3. Contract-Specific Deliverables (for acquired software):**

For software acquired via contract, ensure the delivery package is described in the contractual documentation (See SWE-042 - Source Code Electronic Access). Typical considerations include:

* **Ownership Agreements:**
  + Ensure the source code, executables, and associated documentation are explicitly included and assigned to the customer.
* **Usage Provisions for OTS Software:**
  + Define allowable use, licensing restrictions, and maintenance obligations for proprietary OTS software.
* **Delivery Format and Security Protocols:**
  + Specify file formats, encryption requirements, and safe transfer methods for deliverables.
* **Acceptance Criteria:**
  + Include specific criteria for customer acceptance, ensuring they outline functional requirements, traceability, and artifact completeness (See SWE-034 - Acceptance Criteria).

#### **4. Delivery Format and Method**

* **Select Appropriate Delivery Format:**

  + Deliver software in machine-readable and compiled formats, accompanied by source code stored in standard CM repositories (e.g., Git, Bitbucket).
  + Ensure physical drives, tapes, or other hardware mediums are suitable for the customer’s requirements and environment.
* **Secure Delivery:**

  + Use encryption and secure delivery channels (physical or online) to protect sensitive software and documentation.
  + Include integrity checks (e.g., checksums, cryptographic hashes) for delivered software files.

---

### **Additional Guidance**

#### **Post-Delivery Considerations**

1. **Customer Feedback:**

   * Engage the customer for feedback on the delivery package and identify outstanding concerns or additional needs for operational success.
2. **Operational Verification Support:**

   * Provide technical assistance during the initial installation phase to verify delivered software operates as intended in the customer’s environment.

---

### **Conclusion**

By ensuring that the software delivery package is comprehensive, accurate, and tailored to the software's lifecycle phase and classification, NASA projects can achieve seamless hand-offs, reduce risks, and support long-term operability and maintainability of delivered systems. A well-structured delivery process builds trust with the customer and ensures the success of subsequent phases, including operations, maintenance, and retirement.

See also Topic [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document), [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description)

See also [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement),

See topic [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) in this Handbook for additional guidance regarding delivery for contracted software development.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement), * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management)        * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

# 4. Small Projects

For small projects, the emphasis is on streamlining processes while maintaining the quality, completeness, and compliance of the delivery package necessary to sustain operations, maintenance, and eventual software retirement. The approach for fulfilling this requirement can be scaled to meet the reduced complexity, staffing, and resource constraints typical of small projects.

---

### **Key Considerations for Small Projects**

1. **Simplified Documentation**: Focus only on essential documentation necessary for operations and maintenance activities, while omitting non-critical items that may not add value to small software systems.
2. **Automation and Standardized Tools**: Leverage simple version control systems, templates, or automated tools to create and manage records efficiently.
3. **Team Collaboration**: Small teams can allocate single roles for overlapping functions (e.g., configuration management and documentation updates) to avoid redundancies.
4. **Customer Alignment**: Engage closely with the customer to understand their specific needs and directly tailor the delivery package to their expectations.

---

### **Small Project Software Delivery Package**

The following streamlined delivery package items are recommended for small projects:

#### **Core Elements (Essential for Any Small Project):**

1. **Source Code**: Provide the project’s source code files, organized with clear directory structures and comments for maintainability.

   * Use a simple configuration management system (e.g., Git or Subversion) to store and version control the code.
   * Add simple build scripts or notes to explain how to compile the software from source.
2. **Executable Files**: Deliver all compiled executables, ready for deployment or testing in the customer’s environment.
3. **Version Description Document (VDD)**:

   * Summarize the delivered version, including version number, notable changes, software dependencies, and build instructions.
   * Provide instructions for modifying the software, if necessary.
4. **User Manual**:

   * Develop a simplified **Software User Manual** containing operating instructions, critical commands, and troubleshooting guidance.
   * Include lists of known limitations, assumptions, and error messages along with corrective actions.
5. **Testing Results Summary**:

   * Deliver a concise summary of software testing (e.g., unit, functional, performance testing), including major issues resolved and any known risks.
   * Highlight any safety-critical testing results in systems involving hazardous or mission-critical components.
6. **Configuration Documentation**:

   * Provide a basic overview of the software’s configuration files and settings.
   * Include instructions for applying these configurations to set up the software successfully in the customer’s environment.

---

#### **Additional Elements (Optional for Small Projects):**

If applicable, include these items based on the software's scope, classification, or customer requirements:

1. **Change Request Summary**: Provide a summarized list of approved changes made to the baseline requirements or design, if significant updates occurred during development.
2. **Problem Reports**: Deliver a brief record of prior issues that were resolved or remain open at delivery, focusing on their impact and resolution status.
3. **Risk Assessment Summary**: Document any notable software-related risks still open and identify recommended mitigation strategies for the customer.
4. **Development Environment Information**: If the software requires specialized tools for maintenance, include details about the development environment (e.g., hardware specifications, compilers, frameworks).

---

### **Delivery Format for Small Projects**

#### **1. File Organization**

* Organize the delivery package into clearly titled folders for the source code, executables, documentation, and testing results.
* Use zip files or cloud-based repositories (with appropriate security measures) for simplified delivery.

#### **2. Secure Delivery Method**

* For small projects, deliver the package using secure methods such as:
  + **Online Delivery**: Encrypted file transfer (e.g., NASA-supported secure FTP servers).
  + **Physical Delivery**: USB drives or external storage devices with encryption for transferring large files or sensitive software.

---

### **Streamlined Process for Small Projects**

Follow these simplified steps to generate and deliver the software package efficiently:

#### **Step 1: Finalize Documentation**

* Examine all project artifacts (e.g., change records, test reports, user manuals) and update them to reflect the final state of the software.
* Use simple tools or templates to ensure consistency across all project documents.

#### **Step 2: Package Software**

* Ensure source code and executables are the latest verified versions, pulled from the configuration management system or code repository.
* Ensure that build instructions or scripts for recreating the software are documented clearly.

#### **Step 3: Perform Pre-Delivery Audit**

* Conduct a small-scale checklist-based review prior to delivery:
  + Verify that all files are included and versions are consistent.
  + Check for documentation updates to reflect the as-built state of the software.
  + Confirm completeness of testing records (including failure resolutions).

#### **Step 4: Deliver to the Customer**

* Provide the delivery package through a secure method.
* Provide the customer with an **Acceptance Checklist**, listing expected deliverables and allowing them to confirm successful receipt and review.

---

### **Best Practices for Small Projects**

1. **Reuse Templates and Tools**: Simplify the creation of documentation by reusing existing templates, tools, or processes from prior NASA small projects.
2. **Customer Engagement**: Work closely with the customer throughout the development and delivery process to clarify their expectations and avoid unnecessary deliverables.
3. **Test Verification**: Ensure delivered executables match the functional and safety requirements verified through testing.
4. **Minimize Complexity**: Avoid over-documentation; focus on the critical artifacts necessary for operations and maintenance in the customer’s environment.

---

### **Conclusion**

For small projects, the delivery package should prioritize critical items that ensure the customer's ability to use, maintain, and update the software effectively, while streamlining the generation and auditing processes. By focusing on essential deliverables and leveraging streamlined tools and methods, small projects can fulfill Requirement 4.6.3 efficiently without compromising quality or customer satisfaction.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-216)

  [828-2012 - IEEE Standard for Configuration Management in Systems and Software Engineering](https://ieeexplore.ieee.org/document/6197683 "Click to open in new window")

  IEEE STD IEEE 828-2012, 2012.,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-534)

  [International Space Station (ISS) Program/Command and Data Handling/Firmware Documentation](https://llis.nasa.gov/lesson/1024 "Click to open in new window")

  Public Lessons Learned Entry: 1024.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA has accumulated substantial lessons from past projects, highlighting the critical importance of ensuring proper delivery practices for software and its associated documentation. One such lesson recorded in the **NASA Lessons Learned database** emphasizes the challenges and risks posed by insufficient documentation and archival practices for firmware and software products.

---

### **Lesson Learned (Starliner CFT):** **Unexplained anomalies must not be normalized; disciplined tracking and resolution are mandatory.**

**Project Context:**  
Derived from Starliner CFT Investigation.

**Problem/Observation:**  
Programs repeatedly accepted unexplained anomalies; data management (central repository, telemetry fidelity) hindered diagnosis and trending.

**Contributing Factors:**

* Lack of centralized, queryable anomaly data with cross‑links to tests, risks, and design changes.
* Inadequate telemetry sample rates and timestamps for precise analysis.

**Impacts:**

* Recurrence of anomalies and slow resolution cycles.
* Difficulty assessing system health and readiness.

**Recommended Practices (Aligned to SWE‑077/078):**

* Maintain a **central anomaly repository** linked to requirements, tests, risks, and RCCA records.
* Define **telemetry minimums** (fields, rates, precision) needed for anomaly investigation.
* Require **closure criteria** (root cause or bounded risk acceptance with mitigation) before milestone exits.

**Actionable Checks:**

* Anomaly records include evidence, cause, corrective action, and verification.
* Dashboards trend anomalies; thresholds trigger board review/escalation.
* Milestone checklists include anomaly disposition gates.

### **Key Lesson: Firmware Documentation (Lesson Number 1024)**

**International Space Station (ISS) Program / Command and Data Handling / Firmware Documentation**

**Summary of Lesson Learned:**  
This documented lesson underscores the importance of delivering comprehensive software and firmware documentation to support ongoing operations, maintenance, and potential future reuse of systems. It particularly applies to software and firmware developed by external vendors or contractors, where NASA must maintain control over the delivered artifacts. Key takeaways from the lesson include:

1. **Ensure Complete Documentation is Delivered and Archived:**

   * All firmware and software code must be thoroughly documented and archived. This includes requirements, design specifications, and test artifacts produced during the development process.
   * Without complete documentation, future teams face significant challenges in maintaining and modifying the software, risking increased costs, operational inefficiencies, and mission vulnerabilities.
2. **Retain Rights to Software and Documentation:**

   * NASA must secure rights to access, modify, and use the delivered software, firmware, and associated documentation.
   * Contracts with vendors must specify the ownership and delivery of source code, design documentation, and test results to ensure NASA does not become overly reliant on external entities for maintenance or operational support.
3. **Vendors Must Deliver Development Artifacts as Part of the Delivery Package:**

   * Vendors contracted to develop firmware or software are required to deliver all development-related documentation as part of their final product. This includes requirements, design documents, testing procedures, test results, and any unique considerations relevant to maintaining the software.
   * This direction ensures that all key artifacts remain accessible to NASA, ensuring continuity even in cases of vendor transition or long-term system reusability.

---

### **Application to Requirement 4.6.3**

This lesson directly applies to Requirement 4.6.3, reinforcing the critical need for complete, well-documented, and traceable delivery packages. Following these practices ensures that NASA projects retain control over the software lifecycle, mitigate unexpected maintenance burdens, and preserve essential knowledge for future work.

#### **Practical Recommendations Based on the Lesson Learned:**

1. **Comprehensive Delivery Package:**

   * For both in-house and contracted software, ensure that all lifecycle documentation is included in the delivery package.
   * Essential artifacts include a user manual, as-built records, test results, the source code, design documents, and traceability records.
2. **Vendor Contractual Requirements:**

   * Explicitly mandate the delivery of all software development artifacts in vendor contracts (e.g., requirements, design, test cases, and results).
   * Include clauses regarding intellectual property (IP) rights to secure ongoing access to software and firmware even after vendor contracts end.
3. **Archival and Accessibility:**

   * Archive delivered records in configurations that are easily searchable and accessible for future maintenance teams.
   * Use approved NASA repositories or configuration management systems to ensure long-term availability and version traceability.
4. **Planning for Long-Term Maintenance:**

   * Confirm that documentation is detailed and structured in a way that enables future developers to maintain or enhance the software with minimal knowledge transfer gaps.
5. **Independent Audits Prior to Delivery:**

   * Before software is accepted and archived, perform audits to verify the quality of delivered documentation and ensure it adequately supports operations and maintenance.
   * Address any gaps (missing deliverables, ambiguous documentation, etc.) with vendors or internal teams before project closure.

---

### **Broader Implications of the Lesson Learned**

This lesson demonstrates the downstream consequences of inadequate delivery practices. For example:

* A lack of adequate documentation can delay or prevent timely software fixes, especially in critical systems like the ISS.
* Insufficient control over software artifacts can result in unexpected costs, vendor lock-in, or legal complexities, especially for long-duration NASA missions where system sustainability is a priority.
* Conversely, delivering well-documented software reduces risks, costs, and operational bottlenecks in the long run, ensuring NASA’s ability to sustain critical systems with minimal disruptions.

---

### **Conclusion**

The lesson from ISS firmware documentation highlights the importance of proper delivery processes for all NASA software systems. By adhering to Requirement 4.6.3 and ensuring that software packages include all necessary artifacts while retaining rights to software and documentation, NASA can achieve greater operational continuity, efficient maintenance cycles, and long-term sustainability of its missions. Small- and large-scale projects alike must plan for and implement these best practices to ensure their software’s lifecycle is fully supported post-delivery.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Dedicate more hours to FSSE preparation for post-commissioning](https://software.gsfc.nasa.gov/lesson-details/79/).**Lesson Number 79**: The recommendation states: "Dedicate more hours to FSSE preparation for post-commissioning, particularly in the preparation of the Lab as long-term asset for the mission."
* [Plan for the impacts of assembling and moving the Flight Software simulator](https://software.gsfc.nasa.gov/lesson-details/108/). **Lesson Number 108**: The recommendation states: "Plan for the impacts of assembling and moving the Flight Software simulator."
* [When using commercial BSP for VxWorks don't forget to include yearly maintenance fees](https://software.gsfc.nasa.gov/lesson-details/304/). **Lesson Number 304**: The recommendation states: "When costing a mission that has software licenses, these fees must be accounted for the duration of the mission, including post launch (through Phase E)."

# 7. Software Assurance

**SWE-077 - Deliver Software Products**

4.6.3 The project manager shall complete and deliver the software product to the customer with appropriate records, including as-built records, to support the operations and maintenance phase of the software’s life cycle.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the correct version of the products is delivered, including as-built documentation and project records.

2. Perform audits for all deliveries per the configuration management processes to verify that all products are being delivered and are the correct versions.

## 7.2 Software Assurance Products

Software Assurance (SA) plays a critical role in verifying that the software product and all associated artifacts delivered to the customer meet the applicable standards, requirements, and quality expectations. The guidance below refines and expands upon the original, focusing on ensuring thorough oversight, accurate audits, metric tracking, and comprehensive testing to certify readiness for operations and maintenance.

#### **1. Baseline Verification and Configuration Management Audit:**

* Compile a **Software Configuration Management Baseline Verification Report** to ensure that the latest, approved versions of all software and documentation artifacts match the delivery baseline in the project’s configuration management system.
  + Verify that the configuration management processes align with the planned procedures and that the delivered products comply with these processes.
  + Confirm that all deviations, waivers, or open change requests are approved and documented before delivery.

#### **2. Key Audit Deliverables:**

Software assurance should ensure the following products and deliverables are prepared during the delivery process:

* **Configuration Management Process/Procedure Audit Report**:

  + Assess findings from audits of the configuration management process, identifying gaps, risks, or non-conformances.
  + Ensure corrective actions are defined and tracked to closure.
* **Delivery Product Verification**:

  + Perform configuration management audits to confirm that the final delivery includes all planned artifacts, as defined in the project's Version Description Document (VDD) and delivery plan.
  + Record all audit findings (including any missing or incorrect components, as well as mismatches in software versions) and ensure that discrepancies are fully resolved before delivery.
* **Version Description Documentation Review**:

  + Verify the accuracy of the **Version Description Document (VDD)** for the delivered build, including:
    - Changes made since prior builds.
    - Updated requirements traceability matrices, reflecting the successful implementation and verification of all as-built capabilities.
* **Software Configuration Records Review**:

  + Validate software configuration logs (e.g., change records) to confirm adherence to the project baseline.
* **Defect and Change Records Review**:

  + Confirm that all implemented defect resolutions, feature requests, and late-stage changes are documented and that associated test results are included in the delivery package.
  + Verify that any unresolved defects (e.g., deferred changes, items with workarounds) are listed in the delivery documentation, with associated risks clearly noted.
* **Software Assurance Audit Results**:

  + Provide a consolidated SA Audit Report detailing findings from all process, procedure, and product audits.

---

## 7.3 Metrics for Software Assurance

To continually monitor delivery readiness and identify trends, SA should collect the following metrics and share them during project reviews:

#### **1. Configuration Management Metrics:**

* Number of configuration management audits conducted (Planned vs. Actual).
* Number and type of configuration management non-conformances identified during delivery audits.
* Open vs. Closed configuration-related non-conformances over time.
* Trends in the number of non-conformances by life cycle phase (e.g., requirements, design, testing, and delivery).

#### **2. Software Process and Compliance Metrics:**

* Number of compliance audits planned versus performed.
* Non-conformance trends for both compliance and software process audits.

#### **3. Release Documentation Quality:**

* Number of defects or non-conformances identified in release documentation.
* Open vs. Closed non-conformances in release documentation over time.

#### **4. Build and Delivery Metrics:**

* Number of software components planned for release versus delivered in each build (e.g., programs, modules, files).
* Number of process deviations or missed activities (e.g., skipped regression testing) identified by SA versus officially accepted by the project.

#### **5. Risk Metrics:**

* Known defects and their status at the time of delivery.
* Trends in the number of open risks associated with deliverables.

Refer to **Topic 8.18 - Software Assurance Suggested Metrics** for further detailed metrics that support continuous improvement.

---

## 7.4 Guidance for Software Assurance

Software assurance must verify that all aspects of the software, deliverables, and documentation align with customer expectations and requirements. SA’s responsibilities include certifying the following:

#### **1. Delivery Completeness and Baseline Verification**

* Verify that all **software planned for delivery** has been implemented, including all features listed in the baseline requirements.
* Confirm that all **changes made since baseline** have been documented, implemented, and successfully tested.

#### **2. Software Testing Completion**

* Ensure that the software meets acceptance test criteria, demonstrating full traceability to system, functional, and performance requirements.
* Confirm that regression testing has verified there are no adverse impacts from changes, and verify that defect resolutions are properly retested.

#### **3. Documentation and Release Artifacts**

* Ensure that all planned documentation is included in the delivery, such as:
  + Software User Manuals, As-Built Documentation, Operations Manuals.
  + Build Procedures or Scripts.
  + Regression Test Sets with Expected Results.
  + Maintenance Handbooks.
* Confirm that the delivery identifies any deferred or unresolved defects (along with their risks, workarounds, or rationale).

---

### **Functional Configuration Audit (FCA)**

To verify that the delivered software meets its operational and functional requirements, SA will:

* Conduct (or participate in) an FCA to ensure every requirement has been implemented and is verified/tested.
* Confirm that changes or defect resolutions have been successfully validated, including via regression testing.

---

### **Physical Configuration Audit (PCA)**

The PCA ensures the delivered software package matches the associated documentation and that all items are complete. SA will:

* Perform or participate in the PCA to confirm that the final delivery items match their planned baseline.
* Verify that all recorded version numbers match the configuration management system records.
* Ensure that discrepancies, deviations, waivers, or openwork items are fully accounted for in delivery documents, such as the VDD or delivery correspondence.

---

### **Handling Known Defects in the Delivered System**

If the software is delivered with known defects:

1. Document the defects and their implications (e.g., risks to safety, security, or reliability).
2. Confirm customer approval of delivery despite these defects, noting any workarounds provided.
3. Highlight any critical risks in the SA report, particularly for defects affecting safety-critical operations, and (if necessary) recommend delaying delivery until risks are resolved.

---

### **Post-Delivery Follow-Up**

Software assurance should ensure that the customer has the necessary records to operate and maintain the software. If necessary, provide oversight or audits for post-delivery changes or updates.

---

### **Conclusion**

By following this improved guidance, software assurance ensures that the delivered software product is complete, verified, and ready for operations and maintenance. SA activities, including audits, metrics tracking, testing oversight, and risk analysis, provide transparency and confidence in the integrity of the delivery process. All findings must be clearly communicated to the project team to address potential issues promptly and ensure compliance with Requirement 4.6.3.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement), * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management)        * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical to demonstrate compliance with this requirement. It ensures that deliverables, processes, and outcomes are documented and traceable, providing verifiable proof that the software product and associated artifacts meet all requirements for delivery, operations, and maintenance.

The following is a comprehensive list of objective evidence categories and examples that align with **Requirement 4.6.3**:

---

### **1. Evidence from the Software Delivery Package**

The delivery package is the primary artifact that demonstrates delivery readiness. Objective evidence within the package includes the following:

#### **a. Software Artifacts:**

* **Source Code Repository Checkout Logs**: Verifies that the final version of the source code matches the delivery baseline configuration.
* **Executable Software Binaries**: Stored in a controlled configuration baseline and validated as the deliverable product.
* **Build Scripts or Procedures**: Shows how to reproduce the executable from the source code.

#### **b. Version Description Document (VDD):**

* Identifies the delivered software version, associated changes, and testing status.
* Includes a detailed change history and lists all approved changes implemented in the version.
* Provides instructions for implementation, setup, and maintenance.

#### **c. As-Built Documentation:**

* Includes a requirements traceability matrix (RTM) demonstrating that all software requirements are fulfilled and verified.
* Finalized software architecture and design documents.
* Records of configuration changes and software interfaces.

#### **d. Test Results and Coverage Evidence:**

* Test logs, summaries, and reports demonstrating the pass/fail status of all tests, including unit, functional, regression, and acceptance testing.
* Evidence showing that all defect resolutions have passed validation tests and were included in the final build.
* Code coverage reports (if applicable), showing that tests covered key functionalities.

#### **e. Release Notes/Delivery Letter:**

* Describes the contents of the delivery package.
* Includes identified open issues, deferred changes, and known defects, along with their statuses, risks, and workarounds.
* Contains customer acceptance signoffs or agreements for items not resolved before delivery.

---

### **2. Documentation Evidence**

#### **a. Planned Documentation (Complete and Finalized):**

Objective evidence includes the completion of all documentation necessary to support operations and maintenance. Such items may include:

* **Software User Manual (SUM):** Describes how to operate the software system, including operational constraints, hardware/software dependencies, and troubleshooting instructions.
* **Operations and Maintenance Manual:** Provides detailed maintenance instructions, periodic update requirements, and service recommendations.
* **Software Development and Management Artifacts:**
  + Configuration Management Plan (CMP).
  + Software Requirements Specifications (SRS).
  + Design Documents.
  + Test Plans and Testing Procedures.
* **Regression Test Suites and Expected Results**: Ensures maintenance teams can validate future changes or upgrades.
* **Change History Logs**: Records of all approved changes since project inception.

#### **b. Approval Records:**

* **Defect Resolution Records:** Proof that all closed defect resolutions were tested and validated prior to delivery.
* **Change Request Approvals:** Signed approvals for changes implemented in the release.
* **Waivers and Deviation Approvals:** For any open or deferred issues, formal documentation of deviations and their approvals by project authorities and customers.

---

### **3. Audit Evidence**

Audits provide critical, independent confirmation that all deliverables meet requirements. Audit findings include:

#### **a. Functional Configuration Audit (FCA):**

* Confirmation that all software functional requirements have been implemented, tested, and verified.
* Approval of the FCA report signed by software assurance or quality assurance personnel.
* Test metrics and supporting documentation from the FCA process.

#### **b. Physical Configuration Audit (PCA):**

* Documentation verifying that all delivered items (e.g., software, documentation, and accompanying artifacts) align with the planned delivery baseline.
* Signoff by software assurance that each item matches its recorded version in the project’s configuration management system.
* PCA checklist with results, confirming the completeness and correctness of all delivery components.

#### **c. Configuration Management Audit:**

* Evidence showing compliance with established configuration management processes (e.g., logs showing version control activity, compliance with baselines).
* Non-conformance reports for any discrepancies found, with records of their resolution.

#### **d. Software Process and Compliance Audits:**

* Records of audits verifying that software development, testing, and release processes were followed.
* Metrics tracking open and closed non-conformances, trends over the lifecycle, and their resolution.

---

### **4. Configuration Management and Change Evidence**

Configuration management activities ensure that the delivered software and its artifacts are consistent with the as-built documentation. Key evidence includes:

* **Baseline Configuration Records:** Snapshots of the final configuration, showing delivered source code versions, test artifacts, and documentation versions.
* **Change Tracking Logs:** Records of software changes, approvals, and implementation status for the final delivery.
* **Access Logs for Configuration Management Systems (e.g., Git or similar):** Verifying project team activity in modifying, reviewing, and finalizing items in the delivery configuration.

---

### **5. Testing and Quality Assurance Evidence**

#### **a. Requirements Traceability Evidence:**

* Requirements Verification Matrix: Shows 100% traceability between requirements, design, implementation, and test cases.

#### **b. Test Artifacts:**

* Acceptance Test Report: Confirms that delivered software passed acceptance testing and meets the customer’s functional requirements.
* Regression Testing Report: Demonstrates that changes and bug fixes did not negatively impact existing functionality.

#### **c. Defect Management Evidence:**

* Defect Reports: Includes the status of all defects at delivery (e.g., resolved, deferred, or accepted as-is).
* Risk Analysis Reports: Identifies potential risks posed by unresolved defects.
* Workaround Instructions: For critical defects that remain unresolved at delivery, documented explanations of how to mitigate their impact.

---

### **6. Evidence of Customer Agreement and Signoff**

Before final acceptance, evidence should be collected to confirm that the customer is aware of and agrees to the delivered state of the software:

* **Customer Acceptance Signoff:** Documentation of the customer’s formal acceptance of the software, delivery package, and any associated items.
* **Defect and Risk Agreement:** Signed acknowledgment from the customer that explicitly lists known defects and risks associated with delivery.
* **Delivery Acceptance Review (DAR):** Meeting minutes or signed records from the delivery review.

---

### **7. Supporting Evidence for Post-Delivery Support**

#### **a. Maintenance Plans:**

* Documentation of ongoing support agreements, including planned training materials, maintenance schedules, and responsibilities for future updates.

#### **b. Training Documentation:**

* Manuals, checklists, or session tracking confirming that customer teams have been provided with adequate training for operations and maintenance.

#### **c. Issue Tracking System Access:**

* Evidence that issue tracking systems (e.g., JIRA, Bugzilla) remain accessible to both the project team and customer for post-delivery support.

---

### **8. Metrics and Trend Reports**

Demonstrate project quality and process oversight by compiling metrics during and after delivery:

* Configuration management metrics (e.g., planned vs. completed audits).
* Non-conformance trends by phase and product.
* Completion metrics for planned activities (e.g., percentage of resolved deliverables, closed problem reports, or deferred changes).

---

### **Conclusion**

Objective evidence provides both the project team and the customer with confidence that the delivered software and accompanying records fulfill all requirements of **Requirement 4.6.3**. By providing tangible, well-organized evidence across all project phases, NASA ensures maintainability, traceability, and operational readiness for the delivered system, minimizing risks and facilitating long-term success.

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
