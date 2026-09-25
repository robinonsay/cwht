# SWE-196 - Software Retirement Archival

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695531. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695531/SWE-196+-+Software+Retirement+Archival

SWE-196 - Software Retirement Archival

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695531/SWE-196+-+Software+Retirement+Archival#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695531)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695531&showCommentArea=true&showComments=true#addcomment)

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

4.6.6 The project manager shall identify the records and software tools to be archived, the location of the archive, and procedures for access to the products for software retirement or disposal.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-196 History

SWE-196 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.6.6 The project manager shall identify the records and software tools to be archived, the location of the archive, and procedures for access to the products for software retirement or disposal. |
| Difference between C and D | No change |
| D | 4.6.6 The project manager shall identify the records and software tools to be archived, the location of the archive, and procedures for access to the products for software retirement or disposal. |

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

Retirement should be considered for software that is beyond end-of-life and no longer supported by the software publisher. To retire the software, the following should be specified:

1. the identification of records and software tools to be archived,
2. the location of the archive, and
3. procedures for access.

The rationale behind Requirement 4.6.6 is to ensure that the valuable knowledge, data, software, and tools associated with a project are appropriately preserved, organized, and accessible, even after the software reaches the end of its lifecycle. Proper archiving and disposal are critical for legal, historical, reuse, and accountability reasons, as well as to manage risks related to software dependencies and intellectual property.

Software often plays a critical role in NASA missions, including spacecraft operations, data processing, scientific modeling, and other mission-support systems. Ensuring that software-related artifacts are correctly handled during retirement or disposal enables continuity of knowledge, potential reuse, and compliance with applicable policies. This requirement emphasizes the need for a clearly defined archival and access process to address these concerns.

---

### **Key Objectives of the Requirement**

The goal of archiving and retirement processes is to ensure that all necessary software artifacts are preserved for potential future use, auditing, analysis, or lesson extraction. Specific objectives include:

1. **Preservation of Software Products:**

   * Ensure that all versions of the software, including the final operational version, are archived to create a complete historical record that may be necessary for reuse, lessons learned, legal purposes, or auditing.
   * Preserve associated tools, libraries, and supporting artifacts to enable future reexecution, reuse, or analysis.
2. **Legal and Contractual Compliance:**

   * Meet governmental, agency, or contractual requirements for data and software preservation.
   * Ensure compliance with export-control laws, intellectual property rights, and software licensing agreements during archiving or disposal.
3. **Knowledge Management for Reuse:**

   * Retain valuable intellectual property that may aid future missions or research. Archived software and documentation can be adapted or repurposed to save time and resources in future projects.
   * Enable upstream and downstream teams to analyze older systems when developing or maintaining derivative systems or successor tools.
4. **Enablement of Verification and Auditing:**

   * Archive all relevant artifacts to support post-mission analysis, audits, or re-verification activities. This can be critical in legal inquiries, anomaly or failure investigations, or historical reviews.
5. **Managing Historical and Strategic Value:**

   * Support NASA’s broader knowledge management goals by maintaining an archive of software materials that represent a record of innovation and advancement in the software engineering discipline.
   * Record the historical significance of tools and software for future retrospectives or research.
6. **Proper Disposal to Reduce Risks:**

   * Ensure data security, minimize residual risks (e.g., cybersecurity vulnerabilities), and handle the deprecation of external relationships (e.g., licensed proprietary software) properly during disposal.
   * Prevent unintentional release of sensitive, classified, or proprietary information.

---

### **Rationale in Context of NASA Missions**

#### **1. Mission Continuity and Technical Integrity**

Many missions rely on complex software systems that may require updates or access even after formal retirement. Without proper archiving, retrieving information about critical algorithms, tools, or systems dependencies may become infeasible during post-mission phases or when repurposing systems on new platforms.

#### **2. Failure and Anomaly Investigations**

Post-mission analysis frequently requires revisiting software to analyze issues, anomalies, or contributions to mission failures. Properly archived systems, tools, and records can facilitate these investigations through traceability back to the version of software involved.

#### **3. Reuse for Cost Savings**

NASA frequently reuses software products and tools to lower costs and speed up development for new projects. For example, flight software and ground systems used in one mission have been adapted to serve others (e.g., the Mars rovers and orbiters). Without clear archiving procedures or necessary access mechanisms, recovering reusable components becomes inefficient or impossible.

#### **4. Record of Compliance and Documentation**

For legal, contractual, and compliance-related purposes, software projects need to preserve a complete record of work done during development, operation, maintenance, and retirement. This ensures that the lifecycle of the software can be reviewed or audited at any point, especially as part of responding to external agencies or NASA's internal review mechanisms.

#### **5. Managing Security Risks**

Improper disposal of software, tools, or artifacts can expose sensitive information such as mission data, infrastructure details, or proprietary intellectual property. Without proper archiving and disposal procedures, such materials can be inadvertently exposed, leading to potential cybersecurity, intellectual property, or compliance risks.

---

### **Key Areas of Focus for This Requirement**

#### **1. Identification of Records**

Critical records associated with a software project vary depending on scope and classification but generally include:

* Configuration management artifacts (e.g., baselines, change logs).
* Requirements documentation (e.g., Software Requirements Specifications, traceability matrices).
* Design documentation (e.g., Software Design Descriptions, architecture diagrams).
* Source code repositories and version histories.
* Testing artifacts (e.g., test plans, test reports, regression tests, safety-critical test results).
* User manuals and operational documentation.
* Deployment logs and instructions.
* Historical and final metrics reports.

#### **2. Archiving Software Tools**

Archiving software tools associated with a project ensures that the full development and runtime environment remains accessible in the future:

* Compilers, simulators, libraries, and build systems.
* Testing frameworks used for validation and verification.
* Proprietary or third-party tools (note: licensing restrictions may apply).
* Hardware/software specifications for tools and platforms used during development or operations.

#### **3. Archive Location and Format**

To successfully achieve long-term storage and access while reducing future challenges:

* Archives should follow NASA-approved formats, platforms, and physical or digital storage standards.
* Storage locations should ensure accessibility while safeguarding sensitive artifacts (e.g., adhere to security classifications or data governance requirements).
* Redundancy and backup strategies should be developed to prevent data loss over time.

#### **4. Access Procedures**

Archives must include well-defined access procedures to enable proper authentication, authorization, and retrieval of the materials:

* Access control policies (e.g., who is authorized to retrieve software, tools, or historical artifacts).
* Instructions for using archived software, tools, or supporting environments.
* Tracking mechanisms for monitoring access to archived materials.

#### **5. Disposal of Software**

When retirement of software tools or archives is necessary, proper procedures ensure that materials are disposed of securely and in compliance with policies:

* Permanent deletion of sensitive or non-reusable data (secured erasure or destruction).
* Revocation of licenses/access for proprietary or external tools.
* Documentation of disposal records (e.g., certificates of destruction).

---

### **Conclusion of the Rationale**

Requirement 4.6.6 reflects NASA’s emphasis on lifecycle responsibility for software. Proper identification, archiving, and disposal of software artifacts are critical for ensuring mission continuity, compliance, reuse potential, knowledge retention, and risk mitigation. By meeting this requirement, project managers establish traceability, accountability, and organizational memory, ensuring software maintains its value even beyond operational use.

# 3. Guidance

## 3.1 Retirement Procedures

This improved guidance offers added clarity, structure, and actionable steps to ensure a robust, comprehensive, and compliant retirement process for software. It emphasizes proper archival, security, disposal, and coordination with key stakeholders while promoting efficient reuse wherever applicable.

#### **Documenting Retirement Procedures**

The retirement procedures must be thoroughly documented in the **Software Maintenance Plan (SMP)** or the **Software Development/Management Plan (SDP/SMP)**, following guidance provided in:

* **NPR 7150.2, NASA Software Engineering Requirements**, which mandate proper handling of software at the end of its life.
* **NPR 1441.1, NASA Records Retention Schedules**, which dictate requirements for archival, retention, and disposal of project and program artifacts.

The documented process should:

1. Clearly define the tasks involved in the archival, disposal, and potential reuse of software and associated artifacts.
2. Specify roles and responsibilities for retirement activities, including those of the Project Manager, Technical Point of Contact (POC), Software Assurance (SA) team, Center Chief Information Officer (CIO), and other relevant stakeholders.

---

### **1. Reasons for Retirement**

Retirement should be triggered when software fulfills one of the following conditions:

* **End-of-Life Status:**  
  The software has reached the end of its operational life and is no longer needed to support the mission or program.
* **Lack of Support:**  
  The software publisher no longer supports the tool, system, or application, and its usability or reliability cannot be reasonably maintained.
* **Obsolescence:**  
  The software is outdated and incompatible with current hardware, operating systems, or mission requirements.
* **Mission/Program Completion:**  
  The associated mission, program, or project has been completed, and the software is no longer required for operational or future use.
* **Cost Inefficiency or Security Risk:**  
  The software is no longer cost-effective to maintain or poses cybersecurity risks that outweigh its continued usage.

---

### **2. Steps for Software Retirement**

The retirement process for software involves a structured set of steps to ensure compliance with NASA policies, proper retention or disposal of assets, and mitigation of risks associated with improperly retired software.

#### **Step 1: Notification and Coordination**

1. Inform the Center CIO or designee about the plan to retire the software, following Center-specific notification guidelines.
2. Ensure coordination between the project team, Technical POC, SA personnel, and records management personnel for alignment on roles and responsibilities during retirement.

#### **Step 2: Identification of Records and Tools to Be Archived**

1. Identify the records, tools, and associated artifacts to be archived:
   * **Software Products:** Source code, executables, object code, installation packages, and development libraries.
   * **Documentation:** Software Requirements Specifications (SRS), Software Design Descriptions (SDD), test plans, test results, user manuals, operations manuals, and release notes.
   * **Historical Artifacts:** Change logs, version histories, configuration management records, and defect tracking records.
   * **Tools:** Development environments, compilers, testing frameworks, and any proprietary tools used in the software lifecycle.
2. Engage the SA team to review artifacts for completeness and compliance with NASA policies.

#### **Step 3: Archive Definition**

1. Specify the **location of the archive**, ensuring that it meets the requirements of NPR 1441.1 for secure and accessible storage. Potential locations include:
   * NASA’s centralized repositories for mission-critical software archives.
   * Secure cloud-based repositories that comply with federal and NASA security standards.
   * On-premises storage under the control of the Center CIO, with backups for redundancy.
2. Document procedures for **access to archived materials**, such as:
   * Authentication and authorization requirements.
   * Roles designated for retrieval (e.g., project leads, software assurance personnel).
   * How to handle sensitive, classified, or export-controlled materials.

#### **Step 4: Cessation of Software Usage**

1. Immediately stop all running instances of the software:
   * Uninstall or delete software installed on NASA Center IT infrastructure and mission systems.
   * Revoke access credentials and terminate all access points to retired software.
2. Conduct **verification** by the Center CIO or IT infrastructure team to confirm no residual copies of the software remain accessible or active.

#### **Step 5: Update Inventories**

1. Update the **Center Inventory** and other applicable records to reflect the retired status of the software. Information should include:
   * Date of retirement.
   * Reason for retirement (e.g., end of life, obsolescence, lack of support).
   * Responsibility for archive access and maintenance.
2. Ensure retired software is accurately categorized for future reference or auditing.

#### **Step 6: Software Recycling and Reuse**

1. Evaluate the software for future utility:
   * Can the software or components be repurposed for other missions or projects?
   * Are there reusable algorithms, features, or libraries that could be valuable?
   * Are there licensing restrictions that impact reuse opportunities?
2. For reusable software:
   * Incorporate it into NASA’s software **pool for reuse** or share it via platforms like the **NASA Open Source Software Catalog**, if appropriate.
3. If not reusable, document the decision to decommission the software.

#### **Step 7: Final Disposal**

1. For non-archived software, ensure secure disposal:
   * Permanently delete any digital artifacts, ensuring compliance with federal data erasure standards.
   * Revoke licenses and clean up licensing agreements with vendors or third parties.
2. Create **disposal records**, including certificates of destruction where applicable.
   * Include information about the type of software, security classification, and method of disposal in compliance with NPR 1441.1.

#### **Step 8: Validation and Reporting**

1. Validate that retirement tasks have been completed as planned:
   * SA personnel can independently verify that the activities align with procedures documented in the Software Maintenance Plan.
   * Include validation records in the retirement closeout package.
2. Report the completion of retirement activities to the Center CIO, SA team, and other relevant stakeholders.

---

### **3. Software Assurance Responsibilities**

Software Assurance personnel play a vital role during software retirement:

1. **Audit the Retirement Plan:**
   * Review the retirement procedures to confirm compliance with NPR 7150.2, NPR 1441.1, and Center-specific guidelines.
2. **Verify Completeness of Archiving:**
   * Check that all identified records and tools are archived in approved locations and formats.
3. **Confirm Secure Disposal:**
   * Inspect records of disposal activities to ensure that non-archived software items were securely and permanently removed.
4. **Track Compliance with Contracts:**
   * Ensure licenses for third-party or proprietary software are appropriately terminated or aligned with future reuse plans.

---

### **4. Software Recycling Considerations**

* **License Pooling:**
  + Centralize retired software licenses into a managed pool for potential reassignment, reducing costs and maximizing proprietary software utility.
* **Reuse Evaluation:**
  + Include automated tools or reusable code modules from the retired software in inventories for potential reference or repurposing in future projects.

---

### **Key Points to Remember**

1. **Security is Critical:**
   * Archiving and disposal of retired software must follow cybersecurity best practices to prevent unauthorized access or data leaks.
2. **Coordination Matters:**
   * The Technical POC must work closely with the Center CIO and other stakeholders to align retirement tasks with technical, operational, and policy requirements.
3. **Documentation is Mandatory:**
   * Ensure that all retirement activities, including archival and disposal, are well-documented as part of NASA’s formal records management processes.

---

### **Conclusion**

This guidance ensures that software retirement is a controlled, secure, and compliant process that preserves essential knowledge and eliminates residual risks. It aligns with NASA’s broader mission goals of resource stewardship, knowledge management, and operational security while promoting the reuse of software components where applicable.

See also [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement),

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement)        * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

# 4. Small Projects

For small projects, where resources, complexity, and scale are typically limited, the retirement of software must still follow a structured process to ensure compliance with NASA policies and requirements (e.g., NPR 7150.2, NPR 1441.1). This guidance simplifies the steps for small project teams to meet the requirement efficiently, with a focus on practicality, minimal overhead, and streamlined processes.

---

### **1. Importance for Small Projects**

Even for small projects, software retirement ensures:

* Preservation of project artifacts for potential future reuse or analysis.
* Traceability and compliance with NASA records management policies.
* Secure disposal of sensitive information and intellectual property.
* Mitigation of risks from ongoing vulnerabilities in unsupported software.
* Knowledge retention for lessons learned or historical value.

Small projects must plan for archival and disposal activities, even if the software has a short lifespan or limited operational scope, to ensure proper lifecycle management.

---

### **2. Simplified Retirement Process**

#### **Step 1: Identify Records and Tools**

1. Develop a list of **records and software tools** that need archival or disposal. Include:

   * Final source code and compiled binaries.
   * Supporting libraries and dependencies (ensure licensing details are documented).
   * Documentation (e.g., requirements, design, user guide, testing results).
   * Communication artifacts (e.g., key decision logs, final metrics reports).
   * Configuration management records, such as baseline definitions and version histories.
   * Tools used for development, testing, or operations (e.g., compilers, simulators).

   **Tip for Small Projects:**  
   Use a simple inventory spreadsheet to track all the items that need archiving or disposal.

#### **Step 2: Determine Archive Location**

1. Select a storage location, such as:

   * NASA Center's repository or shared drive (if applicable).
   * Secure external repository or cloud-based service that complies with NASA regulations.
   * Local secure storage, such as an encrypted drive, for smaller-scale artifacts.

   **Tip for Small Projects:**  
   For limited software and artifacts, use existing project storage solutions managed by the Center or project team to avoid unnecessary complexity.
2. **Coordinate Access Procedures:**  
   Define minimal access mechanisms:

   * Name key personnel who should have access (e.g., project manager, technical lead).
   * Specify how authorized users can retrieve archived data (e.g., simple shared folder access with role-based security).

#### **Step 3: Plan for Cessation**

1. Stop all instances of the software:

   * Uninstall it from systems where it was deployed.
   * Verify that active processes or background scripts for the software are terminated.
   * Disconnect linked software systems to prevent unintended residual data usage.

   **Tip for Small Projects:**  
   Assign one person to confirm cessation on all relevant systems (e.g., delete software from servers/computers or revoke deployment credentials). Use a simple checklist for verification.

#### **Step 4: Archiving**

1. Retain final copies of identified records and tools in the chosen archive.

   * If the software or tools are reusable, clearly label them for potential use in future projects.
   * Archive small project documentation and logs (e.g., a zipped folder with labeled subdirectories for code, documentation, licenses, and tools).

   **Tip for Small Projects:**  
   Use folder naming conventions and metadata (e.g., dates, project codes) to help users easily identify archived materials.

#### **Step 5: Secure Disposal**

If artifacts are no longer needed or cannot be archived:

1. Permanently delete sensitive information and clean any environments used during the project.
2. Revoke licenses for proprietary tools, if applicable.
3. Document disposal actions in a simple record (e.g., a short memo noting the deletion of certain files/tools).

   **Tip for Small Projects:**  
   Free tools like secure file shredding utilities (e.g., Eraser/DBAN) are effective for ensuring sensitive data is fully erased. Confirm with the Center CIO for disposal methods.

#### **Step 6: Update Records**

Update NASA records and inventories, including:

1. Flag the software as "retired" in any relevant tracking systems.
2. Add metadata in the archive system that records:

   * Retirement date.
   * Responsible personnel.
   * Summary of archived artifacts and their use.

   **Tip for Small Projects:**  
   Use simple updates in shared project documentation or Center systems to avoid introducing additional tools or complexity.

---

### **3. Roles and Responsibilities**

For small projects, roles can be consolidated to efficiently manage the software's archiving and disposal:

1. **Project Manager:**

   * Oversees the retirement process and ensures compliance with policies.
   * Approves the list of archived items and access procedures.
2. **Technical Lead or Technical Point of Contact (POC):**

   * Identifies the artifacts to be archived or disposed.
   * Leads cessation tasks (e.g., deletion from all instances) and validates the retired status of the software.
3. **Software Assurance Personnel:**

   * Conducts a simple audit to confirm compliance with archival/disposal standards.
   * Reviews the completeness of the archival activity and validates secure disposal.
4. **Center CIO or Designee:**

   * Ensures compliance with NASA standards for archiving/storage.
   * Advises on disposal methods and verifies completion.

---

### **4. Special Considerations for Small Projects**

#### **Reuse and Recycling of Software**

For software that holds potential value for reuse:

* **Centralize Licenses:**  
  If proprietary licenses are involved, coordinate with the Center CIO to transfer them to a reuse pool.
* **Document Opportunities for Future Use:**  
  Clearly label reusable components or tools in the archive (e.g., "Reusable algorithms for data analysis").

#### **Handling Sensitive Artifacts**

Small projects may still handle proprietary, classified, or export-controlled materials:

* **Consult Early:**  
  Confirm with the Center CIO how sensitive materials should be archived or disposed.
* **Encrypt Data:**  
  For archived sensitive materials, use NASA-approved encryption methods (e.g., AES-based encryption tools).

---

### **5. Documentation Requirements**

For small projects, documentation of retirement activities can be streamlined:

1. **Retirement Plan:**  
   Include the software retirement procedures in the given project Software Maintenance Plan (SMP) or Software Development/Management Plan (SDP/SMP).
2. **Retirement Completion Memo:**  
   After the artifacts are archived and/or disposed:
   * Create a short memo summarizing that retirement is complete.
   * Include the archive location, list of archived artifacts, disposal methods used for non-archived items, and access procedures.

---

### **6. Checklist for Small Project Software Retirement**

Here’s a simple checklist for small teams managing software retirement:

* Identify records and tools to be archived.
* Confirm the archive location and access procedures.
* Stop all active instances of software and uninstall where necessary.
* Archive the identified artifacts (code, tools, documentation, etc.).
* Validate the security/sensitivity requirements of archived materials.
* Dispose of unneeded digital artifacts securely.
* Update the Center inventory or record system to reflect retirement.
* Prepare and submit the retirement completion memo or records.

---

### **7. Summary of Key Points**

* **Simplicity Is Key:** Use tools and processes already available to manage retirement efficiently.
* **Archive Thoughtfully:** Even in small projects, components may hold future reuse value.
* **Ensure Security:** Properly dispose of sensitive materials to avoid data breaches or compliance issues.
* **Document Actions:** Even small projects should record key retirement activities for traceability.

By following this simplified guidance, small projects can meet Requirement 4.6.6 efficiently while maintaining compliance with NASA policies.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-037)

  [NASA Records Management Program Requirements (Updated w/Change 3),](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=1441&s=1E "Click to open in new window")

  NPR 1441.1E, NASA Office of the Chief Information Officer, Effective Date: January 29, 2015, Expiration Date: January 29, 2024
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
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

NASA has a solid history of software-intensive projects that demonstrate the importance of proper software retirement, archival, and reuse processes. Over time, key lessons learned have been documented in the **NASA Lessons Learned Information System (LLIS)** to guide current and future practices for software management, including retirement and disposal. Below, relevant lessons learned are summarized and aligned with Requirement 4.6.6.

---

### **Lesson 1: Inadequate Archival Practices Can Hinder Future Investigations or Reuse**

#### **Case Study: Apollo Program Lessons (LLIS #0338)**

The Apollo program demonstrated the value of properly archiving software and records when attempting to apply lessons learned for future missions. While essential mission artifacts were preserved, some original resources (e.g., software and accompanying documentation) were lost or not organized systematically, complicating efforts to derive information for later programs like Shuttle and Artemis.

#### **Key Takeaway:**

* Ensure that **all software and associated documentation** (including requirements, design, test data, and configurations) are archived in an organized and accessible repository to allow for future use when developing derivative systems or investigating anomalies.

#### **Action for 4.6.6 Compliance:**

* Define a thorough list of records and tools to archive, ensuring no critical artifacts are excluded from long-term storage.
* Use a reliable, central repository with metadata to make future retrieval efficient.

---

### **Lesson 2: Failure to Coordinate Software Retirement Led to Redundant Costs**

#### **Case Study: Space Shuttle Program Software Retirement (LLIS #0548)**

The retirement of specific ground support and simulation software on the Space Shuttle Program revealed gaps in coordination between teams responsible for the software's future use. Certain components that had potential for reuse were prematurely disposed of, requiring expensive reinvention of similar tools for future missions.

#### **Key Takeaway:**

* Proper **coordination across teams and stakeholders** is crucial during software retirement to avoid unintentional disposal of reusable software or tools.

#### **Action for 4.6.6 Compliance:**

* Before disposing of any software, consult stakeholders (e.g., Center CIO, Software Assurance personnel, other project teams) to identify potential reuse.
* Establish and document explicit decision-making criteria for distinguishing between software to be archived, retired, or disposed of.

---

### **Lesson 3: Retiring Legacy Systems Can Expose Security Vulnerabilities**

#### **Case Study: Legacy Software Systems for Data Archival (LLIS #2205)**

In some instances, legacy systems being retired continued to run in the background after being replaced, creating security vulnerabilities that allowed unauthorized access to sensitive mission data. A critical lesson was the need for **complete cessation of legacy software usage** and ensuring proper disposal.

#### **Key Takeaway:**

* Legacy systems must be thoroughly decommissioned, files deleted, and access revoked to mitigate cybersecurity risks.

#### **Action for 4.6.6 Compliance:**

* As part of retirement, verify that the software has been fully removed from all operational systems.
* Work with the Center CIO to ensure that deletion follows NASA cybersecurity protocols.

---

### **Lesson 4: Insufficient Archival Documentation Reduces Reuse Potential**

#### **Case Study: Mars Pathfinder Software Reuse (LLIS #0612)**

The Mars Pathfinder mission included innovative software that could have been reused on subsequent rover missions. However, documentation for some aspects of the software was incomplete or missing, making it difficult to adapt the software efficiently to new mission environments.

#### **Key Takeaway:**

* Comprehensive and well-maintained documentation is as critical to archiving as the software itself because it provides the context needed for future reuse.

#### **Action for 4.6.6 Compliance:**

* Ensure that all documentation (e.g., operation manuals, design documents, test reports) is archived alongside the software in an organized and easily searchable structure.

---

### **Lesson 5: Software Licensing Can Complicate Reuse and Recycling**

#### **Case Study: Third-Party Software Licensing Issues (LLIS #2358)**

Lessons learned from projects involving third-party proprietary software have highlighted the complexity of managing software licenses during and after retirement. Failure to track appropriate licensing terms led to legal risks and prevented certain tools from being properly reused in subsequent projects.

#### **Key Takeaway:**

* Ensure that licensing terms for any third-party software are well-understood and documented when retiring or archiving licensed tools.

#### **Action for 4.6.6 Compliance:**

* Maintain a record of all licenses used for software tools as part of the retention process.
* Retire or transfer licenses per vendor agreements, and clearly identify restrictions on reuse.

---

### **Lesson 6: Long-Term Storage Formats Matter**

#### **Case Study: Use of Obsolete Archival Formats (LLIS #0897)**

In one case, archived software and documentation were stored in formats that became obsolete, such as tapes or file formats no longer supported by modern operating systems. This created challenges in accessing critical assets years after the systems were retired.

#### **Key Takeaway:**

* Choose long-term storage formats that are well-documented and futureproof, ensuring accessibility even as technology changes.

#### **Action for 4.6.6 Compliance:**

* Use widely adopted, non-proprietary formats (e.g., PDF/A for documentation, XML or JSON for data) for all archives.
* Regularly audit archived materials to ensure they remain accessible and aligned with current technologies and infrastructure.

---

### **Lesson 7: Improper Archiving Can Cause Gaps in Post-Mission Analysis**

#### **Case Study: Lessons from the Climate Research Missions (LLIS #1981)**

Improper archival of software artifacts from a climate research satellite mission led to difficulty in conducting post-mission analysis of anomalies. Software tools used to process key mission data were missing, and there was no clear procedure for accessing what remained.

#### **Key Takeaway:**

* Archiving should include a clear procedure for locating and accessing records to facilitate post-mission analysis or follow-up on anomalies.

#### **Action for 4.6.6 Compliance:**

* Document procedures for future access to archives as part of the retirement plan, including roles, responsibilities, and tools needed for retrieval.

---

### **Lesson 8: Proper Software Recycling Saves Time and Costs**

#### **Case Study: Software Recycling on Mars Exploration Rover Program (LLIS #1034)**

The Mars Exploration Rover (MER) program successfully repurposed software originally developed for earlier projects (including flight software and ground systems). Lessons learned emphasized the importance of evaluating software for recycling opportunities before retirement or disposal.

#### **Key Takeaway:**

* Evaluate software for recycling opportunities as part of the retirement process to reduce development time and costs for future missions.

#### **Action for 4.6.6 Compliance:**

* Formalize software recycling as part of the retirement process by integrating it into the archiving plan:
  + Identify components that can be repurposed for other NASA missions.
  + Make reusable components accessible to other project teams via shared repositories or catalogs.

---

### **Summary of NASA Lessons Learned**

NASA’s historical experiences emphasize the following key points for effective software retirement, in line with Requirement 4.6.6:

1. Comprehensive archival is critical for future investigations, reuse, and audits.
2. Coordination with stakeholders is necessary to avoid premature disposal of valuable software.
3. Legacy systems must be properly decommissioned to avoid security risks.
4. Adequate documentation enhances the long-term value of archived software.
5. Licensing management ensures compliance for proprietary tools and software.
6. Choose robust and futureproof archival formats to prevent obsolescence.
7. Accessibility to archives simplifies anomaly investigations and post-mission analyses.
8. Recycling software reduces costs and accelerates development for future projects.

By incorporating these lessons into small and large project practices, NASA can ensure efficient, compliant, and valuable software retirement processes.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Archived technical data for projects put on-hold must be sufficient to restart the project with minimal impact](https://software.gsfc.nasa.gov/lesson-details/59/). **Lesson Number 59**: The recommendation states: "Ensure that archived technical data for projects put on-hold is sufficient to restart the project with minimal impact."

# 7. Software Assurance

**SWE-196 - Software Retirement Archival**

4.6.6 The project manager shall identify the records and software tools to be archived, the location of the archive, and procedures for access to the products for software retirement or disposal.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project has identified the records and software tools for archival.

2. Confirm that the project archives all software and records selected for archival, as planned.

## 7.2 Software Assurance Products

#### **Updated Products List**:

Software assurance personnel play a critical role in confirming that proper planning, execution, and compliance are achieved during the software retirement process. The following assurance products should be maintained as part of the software assurance process for this requirement:

1. **Audit Findings and Results:**

   * Results from audits or reviews confirming that all retirement processes align with the project's documented plans, NASA policies (e.g., NPR 7150.2 and NPR 1441.1), and Center-level procedures.
   * Assurance review logs verifying that the retirement process followed approved project or Center retirement guidelines.
2. **Archival Confirmation Report:**

   * Formal evidence that all software, software records, metrics, tools, and supporting documentation have been archived properly in the planned organizational repository.
   * The report should specify the archived location(s), file inventory, and accessibility procedures.
3. **License Management Confirmation:**

   * Documentation that confirms proper transfer, cancellation, or disposition of software licenses associated with retired tools or products.
4. **Disposal Records:**

   * Evidence showing secure disposal of any software or tools that are not planned for archival due to obsolescence, sensitivity, or lack of reuse potential.
   * Includes certificates of destruction or secure deletion documentation.

---

## 7.3: Metrics

#### **Updated Metrics for Tracking and Verification:**

Metrics identified for this requirement should help evaluate the completeness and effectiveness of the software assurance process during retirement. Suggested metrics include:

1. **Metrics for Archival Completeness:**

   * Percentage of identified records and tools successfully archived versus planned items.
   * Number of artifacts missing or delayed during archival.
2. **License Management Metrics:**

   * The number of licenses successfully transferred or canceled.
   * The number of licenses with unresolved or pending actions.
3. **Disposal Metrics:**

   * Number of software tools securely deleted or destroyed (if not archived).
   * Time required to complete secure disposal of retired materials after cessation.
4. **Compliance Metrics:**

   * Percentage of audits completed without findings or non-compliances during the retirement phase.
   * Number and type of issues raised during audit reviews.

---

## 7.4: Enhanced Guidance for Software Assurance

#### **Planning for Software Retirement**:

To confirm proper retirement planning:

1. **Review Documented Plans:**

   * Verify that the retirement procedures are clearly documented in the **Software Management/Development Plan (SDP)** and/or **Software Maintenance Plan (SMP)**. These plans should include:
     + The identification of records, tools, and software products requiring archival.
     + The planned repository location(s) for archival items.
     + Procedures for accessing archived records.
2. **Review Related Plans for Completeness:**

   * Check the **Data Management Plan (DMP)** or equivalent documentation for detailed information on the files and tools to be archived and planned data storage locations.
   * Verify traceability between identified archival items and these plans.
3. **Ensure Procedure Documentation:**

   * Confirm that the procedures for archiving, accessing, and disposing of software products are documented either at the project or Center level.
   * Ensure that project-level procedures reference Center-level processes for standardization (where applicable) and include tailored adjustments for project-specific needs.

---

#### **Execution of Software Archival and Disposal**:

To verify successful software retirement execution:

1. **Audit Retirement Activities:**

   * Conduct audits to verify compliance with the approved retirement plan and procedures.
   * Validate that all identified records, tools, and software artifacts have been archived or securely disposed as planned.
2. **Validate Artifact Inventory:**

   * Compare the archived items with the finalized inventory list identified during planning to ensure completeness. This includes:
     + All versions of the software (source and binary code).
     + Software-related documentation (e.g., requirements, design, testing artifacts, user guides, operational manuals).
     + Configuration and change management records.
     + Metrics tracking historical software performance.
     + Supporting tools essential for executing or reusing the software (e.g., compilers, libraries, proprietary tools).
3. **Verify Secure Disposal Procedures:**

   * Confirm that items not planned for archival have been securely deleted or disposed of to prevent unauthorized access or use.
   * Review disposal records, which should document the method used (e.g., secure deletion, destruction).
4. **Check Licensing Compliance:**

   * Ensure all software tools or products with associated licenses have been properly handled (transferred to other projects, canceled, or retired according to vendor agreements).
   * Confirm compliance with licensing agreements to avoid legal or financial risks.

---

#### **Post-Retirement Assurance Checks**:

After completing the retirement process:

1. **Access Procedures Validation:**

   * Validate that archived artifacts can be securely retrieved by authorized personnel using documented access procedures.
   * Ensure access credentials are assigned based on specific roles (e.g., project personnel, software assurance teams) and comply with organizational security policies.
2. **Verify Proper Documentation:**

   * Confirm that all retirement activities, including archival, disposal, and licensing actions, are well-documented for future audits or inquiries.
   * Ensure that final copies of all documentation (e.g., audit findings, archival confirmation, disposal records) are included in the project closeout package.

---

#### **Specific Tasks for Software Assurance Personnel**:

1. **Audit Planning**:

   * Generate an audit plan that evaluates compliance with software retirement activities and standards outlined in NPR 7150.2 and NPR 1441.1.
2. **Confirmation of Archival Completeness**:

   * Use checklists to confirm that all necessary software, tools, metrics, and documentation have been archived successfully.
   * If any items identified in the project plan (SDP or SMP) are missing or delayed, issue findings to correct the situation before project closure.
3. **Disposal Security Verification**:

   * Validate proper disposal methods for items marked for retirement but not archived. For example:
     + Confirm secure deletion of sensitive artifacts using NASA-approved tools.
     + Review certificates of destruction where applicable.
4. **Licensing Oversight**:

   * Ensure that software licenses are closed out appropriately (e.g., canceled or transferred to new projects).

---

#### **Periodic Oversight After Retirement**:

Software assurance personnel should periodically validate archived materials (if feasible) post-retirement:

* Ensure continued accessibility.
* Confirm that sensitive or restricted information remains secured in the archive.
* Verify compliance with NASA’s ongoing records management standards.

---

This updated software assurance guidance enhances the process for Requirement 4.6.6, ensuring traceability, completeness, and compliance while providing software assurance personnel with actionable steps to oversee and validate retirement and archival activities.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement)        * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) |

# 8. Objective Evidence

Objective Evidence

Objective evidence serves as concrete proof that the requirement has been planned, implemented, and verified successfully. This evidence supports compliance with NASA policies (e.g., NPR 7150.2, NPR 1441.1) and provides an audit trail for software retirement activities. Below is a categorized list of objective evidence that demonstrates adherence to this requirement.

---

### **1. Planning Evidence**

These artifacts ensure that retirement planning activities have been documented and address the necessary elements of software retirement and archival.

1. **Software Maintenance Plan (SMP):**

   * Documented procedures for software retirement, including:
     + Identification of software products, tools, and associated records to be archived.
     + Specific archive locations (e.g., repository, server, or cloud storage).
     + Steps for securely disposing of software and tools no longer needed.
2. **Software Development/Management Plan (SDP/SMP):**

   * Details retirement activities embedded in the broader software lifecycle management process.
   * Includes tasks, timelines, roles, and responsibilities for archival and disposal.
3. **Data Management Plan (DMP):**

   * A comprehensive list of artifacts to be archived (e.g., source code, binaries, project documentation, metrics).
   * Defined organizational repositories or systems for storing archival items.
   * Access control policies for the archived data.
4. **Archival and Disposal Procedures:**

   * Documented steps for:
     + Archiving software and records.
     + How disposal of unneeded artifacts will be handled securely.
     + Processes to manage software licenses (transfer, cancellation, etc.).
5. **Records Retention Plan:**

   * Alignment with NPR 1441.1 (NASA Records Retention Schedules) for retention durations and methods.

---

### **2. Implementation Evidence (Execution)**

These records verify that the planned retirement and archival tasks were executed as intended.

#### **Archival Completion**

1. **Inventory of Archived Items:**

   * A complete, itemized list of the software, tools, and records archived (e.g., source code, configuration files, test results, user guides).
   * Metadata for each artifact, including:
     + File name.
     + Type of artifact (e.g., code file, report, metric).
     + Archive location.
     + Archive date.
2. **Archive Confirmation Report:**

   * A summary report confirming the archival activity has been completed, with details such as:
     + Items archived and their locations.
     + Verification that all planned items were preserved.
     + Access instructions or credentials for the repository.
3. **Archiving Approval Signature Records:**

   * Sign-offs by the Project Manager, Technical Lead, and Software Assurance (SA) personnel confirming that all required artifacts have been properly archived.
4. **Repository Directory Snapshots:**

   * Screenshots or exports of the repository folder structure showing the archived files and locations.

---

#### **Disposal Execution**

1. **Secure Disposal Records:**

   * Evidence of software and tools disposed of securely, such as:
     + Certificates of destruction.
     + Logs of secure deletion activities.
     + Screenshots of deletion confirmations.
2. **License Management Logs:**

   * Records documenting license transfers to other projects, cancelation requests, or termination confirmations.
   * Vendor communications regarding license closure.
3. **Disposal Verification Report:**

   * A report from software assurance personnel confirming that disposal was carried out securely and in compliance with standards.

---

#### **Stakeholder Communication**

1. **Retirement Notices:**

   * Notifications sent to stakeholders (e.g., Center CIO, project teams, software engineers) regarding the cessation of software use and the successful completion of archival or disposal activities.
   * Email chains, meeting minutes, or memos documenting stakeholder acknowledgment.
2. **Licensing Closure Documentation:**

   * Formal correspondence with software vendors regarding license transfers or cancellations.

---

### **3. Verification and Audit Evidence**

These artifacts prove that the retirement activities were reviewed and validated by relevant teams to ensure compliance with NASA standards.

1. **Software Assurance Audit Report:**

   * Results of audits conducted to verify:
     + The completeness of the archival process.
     + Secure disposal of unneeded software.
     + License compliance.
2. **Verification Checklists:**

   * Checklists or worksheets used by software assurance personnel to confirm that:
     + All listed items in the retirement plan were archived or disposed.
     + Archived artifacts match the inventory list.
     + Archived software is accessible using the documented procedures.
3. **Gap Analysis Results:**

   * Any issues or gaps identified during retirement audits and how they were resolved (e.g., missing records or delayed disposal activities).
4. **Retention Compliance Confirmation:**

   * Evidence that archived items comply with NPR 1441.1’s retention schedules and classifications.

---

### **4. Post-Retirement Evidence**

These artifacts ensure that long-term accessibility and compliance have been addressed after the software retirement is complete.

1. **Access Logs for Archived Materials:**

   * Automated or manually maintained logs verifying that authorized personnel can access the archived software, records, and tools as specified.
2. **Cybersecurity Validation:**

   * Validation reports ensuring that the archive storage complies with NASA security standards to prevent unauthorized access or data breaches.
3. **Periodic Availability Checks:**

   * Evidence of regular checks confirming continued accessibility, data integrity, and alignment with retention policies.
4. **Knowledge Sharing or Handoff Records:**

   * Records indicating that archived software and artifacts have been handed over to another party or repository for reuse (if applicable).

---

### **Examples of Objective Evidence for a Typical NASA Project**

Here’s an example of objective evidence for meeting Requirement 4.6.6 in a NASA software development project:

| **Category** | **Example Evidence** |
| --- | --- |
| Planning Evidence | Approved software maintenance plan with outlined retirement procedures. |
| Planning Evidence | Data management plan listing artifacts to be archived and storage locations. |
| Implementation Evidence | Archive Confirmation Report with metadata for archived items and storage paths. |
| Implementation Evidence | Secure disposal logs confirming deletion of sensitive data using approved tools. |
| Verification Evidence | Software Assurance Audit Report verifying all planned software artifacts were archived or disposed of. |
| Post-Retirement Evidence | Repository snapshot showing folder and artifact organization for long-term access. |
| Post-Retirement Evidence | Access logs confirming authorized retrieval of archived records. |

---

### **Final Notes on Objective Evidence**

Objective evidence is critical for demonstrating regulatory compliance, validating the successful execution of retirement tasks, and ensuring that software and associated records are handled securely and thoughtfully during their lifecycle's end. By maintaining complete and organized evidence, teams protect the integrity of NASA's software assets and allow for future reuse, auditing, and mission support.

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
