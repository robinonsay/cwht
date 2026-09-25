# SWE-203 - Mandatory Assessments for Non-Conformances

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695537. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances

SWE-203 - Mandatory Assessments for Non-Conformances

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695537)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695537&showCommentArea=true&showComments=true#addcomment)

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

5.5.3 The project manager shall implement mandatory assessments of reported non-conformances for all COTS, GOTS, MOTS, OSS, and/or reused software components.

## 1.1 Notes

This includes operating systems, run-time systems, device drivers, code generators, compilers, math libraries, and build and Configuration Management (CM) tools. It should be performed pre-flight, with mandatory code audits for critical defects.

## 1.2 History

Click here to view the history of this requirement: SWE-203 History

SWE-203 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 5.5.3 The project manager shall implement mandatory assessments of reported non-conformances for all COTS, GOTS, MOTS, OSS, or reused software components. |
| Difference between C and D | Change "or" to "and/or" |
| D | 5.5.3 The project manager shall implement mandatory assessments of reported non-conformances for all COTS, GOTS, MOTS, OSS, and/or reused software components. |

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
| * [A.12 Software Non-conformance or Defect Management](/spaces/SWEHBVD/pages/133235388/A.12+Software+Non-conformance+or+Defect+Management) |

# 2. Rationale

Software components that are used to build the software product (e.g., compilers) or become a part of the software (e.g., Operating Systems) can introduce unexpected defects in the delivered product.  Whenever non-conformances in these products are discovered, a thorough assessment is required to identify any other potential impacts.

This requirement exists to ensure that all software components integrated into NASA systems—whether developed in-house or externally sourced (e.g., commercial off-the-shelf (COTS), government off-the-shelf (GOTS), modified off-the-shelf (MOTS), open-source software (OSS), or reused software)—are rigorously assessed for any non-conformances (defects, issues, or risks). By requiring mandatory assessments of reported non-conformances, NASA aims to mitigate risks associated with external or legacy software and ensure these components meet the project’s quality, reliability, performance, and safety standards.

---

### **Key Rationale**

#### **1. COTS, GOTS, MOTS, OSS, and Reused Software Pose Additional Risks**

Unlike internally developed software, external and reused software components often carry pre-existing defects or functionality limits that must be carefully managed:

* **Limited Insight into Development Practices:** COTS, GOTS, MOTS, and OSS software are typically not developed under NASA’s rigorous processes, leading to potential gaps in understanding the reliability, robustness, and safety of these components.
* **Unresolved Defects:** Vendors and open-source communities may provide known lists of defects or issue databases, but these issues may not have been resolved before product delivery. Without assessments, there's a risk these non-conformances can propagate into NASA's systems.
* **Distributed Ownership:** OSS and reused software may lack centralized authority, leading to challenges in resolving non-conformances in a timely manner.
* **Versioning and Update Challenges:** External software introduces risks related to patching, version control, and compatibility with NASA’s specific mission context. New updates may introduce unresolved bugs, or vendors may no longer support old versions of packaged software.

#### **2. Critical Mission Risks Require Vigilance**

COTS, GOTS, MOTS, OSS, and reused software could be part of mission-critical systems, including:

* **Safety-Critical Systems:** Issues in reused software components could affect systems essential to astronaut safety, hardware reliability, and ground-control tools.
* **Systems Affecting Mission Performance:** Errors in third-party libraries or reused tools can impact scientific data integrity, timing, computations, or automation processes essential to mission success. Mandatory assessment of all non-conformances ensures that NASA’s mission-critical software does not suffer from latent defects in external components.

#### **3. Consistent and Transparent Risk Evaluations**

By implementing mandatory assessments:

* **All Non-conformances Are Evaluated:** Every reported defect is systematically analyzed for its impact and likelihood of occurrence within NASA's operational context.
* **Consistency Across Projects:** Ensuring mandatory assessments standardizes the treatment and evaluation of third-party and reused software risks across all projects, eliminating gaps in process discipline.
* **Traceability:** Mandatory assessments ensure that defect tracking systems document all known risks, aiding oversight and facilitating future audits and safety reviews. This level of transparency helps maintain confidence in NASA's rigorous software assurance processes.

#### **4. Mitigation of Integration Complexity**

Non-conformances encountered in third-party software are especially problematic when integrating these components into NASA’s systems because:

* Interfaces or interactions with other subsystems may cause latent defects in external components to manifest in unforeseen ways.
* Improper configuration of COTS and OSS could amplify risks during system testing, integration, or operations. Mandatory assessments help identify potential integration risks early and ensure that reuse decisions are backed by careful evaluation of non-conformance-driven risks.

#### **5. Lessons Learned from Previous NASA Projects**

NASA’s **Lessons Learned database** provides multiple examples where improper management of third-party or reused software resulted in project delays, cost overruns, risks to safety, or degraded mission performance. For example:

* **LLIS-2215** – Issues with COTS/OSS scalability and reliability affected system performance during operations.
* **LLIS-1543** – Hidden defects in reused software components caused system failures and required expensive rework during final system integration testing. These lessons highlight the need for mandatory assessments to prevent recurrence of such issues.

#### **6. Responsiveness to Vendor/Third-Party Ecosystem**

Mandatory assessment forces project teams to:

* Actively monitor vendor issue tracking systems, release notes, or open-source repositories for updates on unresolved defects.
* Engage with vendors or communities to evaluate potential fixes and determine NASA’s mitigation strategies if vendor support or patching is unavailable. This ensures proactive risk management rather than a reactive approach after defects are discovered in operations.

---

### **Benefits of Mandatory Assessments**

#### **1. Enhanced Risk Management**

Mandatory assessments ensure all identified non-conformances in external or reused software components are properly evaluated, allowing project teams to:

* Quantify risks posed by defects.
* Prioritize efforts on resolving defects with the highest impact on safety, performance, and mission objectives.
* Establish contingency plans for defects that cannot be resolved prior to deployment.

#### **2. Improved System Integrity**

By rigorously assessing non-conformances, NASA ensures:

* Critical defects in third-party software do not propagate into integrated systems.
* Important system functionality (e.g., timing, computations, safety features) is not undermined by latent risks.

#### **3. Reduced Costs and Delays**

Mandatory assessments reduce the likelihood of expensive late-stage rework by identifying potential risks early, before testing or operations. For example:

* Catching unresolved OSS vulnerabilities in ground software during the development phase eliminates the need for urgent security patches later.
* Mitigating integration issues from defective reused software prevents mission delays.

#### **4. Greater Accountability**

Systematic assessments ensure all third-party and reused software non-conformances are documented, categorized by severity, and tracked to closure. This promotes accountability across all stakeholders, including subcontractors and external vendors.

#### **5. Support for Data-Driven Decision Making**

Mandatory assessments generate detailed data that can be used to:

* Inform decisions about continuing to use specific COTS, GOTS, OSS, or reused components.
* Evaluate whether concerns raised in vendor documentation or OSS defect logs require changes in architecture or design.
* Justify mitigation strategies (e.g., workarounds, custom patches, compensating measures).

---

### **Challenges Addressed by Mandatory Assessments**

| **Challenge** | **How Mandatory Assessments Address This Challenge** |
| --- | --- |
| Lack of visibility into third-party software risks | Evaluates vendor-reported defects in the context of system integration and mission needs. |
| Overlooked defects in external systems | Forces systematic evaluation of all known non-conformances, even those considered “low priority.” |
| Hidden integration risks | Identifies latent risks related to subsystem interfaces before system-level testing or operations. |
| Vendor updates and patching gaps | Tracks evolving non-conformance status (open vs. closed) and ensures NASA has plans for vendor-driven changes. |
| Risk prioritization inconsistencies | Establishes common processes for evaluating and categorizing risks of third-party issues. |

---

### **Why It Is Mandatory**

* **Critical Mission Assurance:** External software components are often critical to success but have varying levels of quality assurance. Mandatory assessments ensure every known non-conformance is evaluated and the associated risks documented, helping NASA maintain high-quality standards for all software.
* **Uniform Application Across Projects:** By mandating assessments, NASA ensures every project aligns with the Agency’s emphasis on safety, security, and mission success, regardless of the component’s origin.
* **Increased Accountability:** Mandatory assessments compel project teams to account for system-wide risks associated with third-party components, ensuring all stakeholders actively address external software concerns.

---

### **Conclusion**

Mandatory assessments of non-conformances in COTS, GOTS, MOTS, OSS, and reused software protect NASA’s systems from introducing latent defect risks. This requirement also ensures transparency, traceability, and prioritization of risks, enabling proactive mitigation. It builds on lessons from previous projects and underscores the importance of maintaining rigorous software assurance for external components critical to mission success.

# 3. Guidance

The following software engineering guidance provides clarity and practical actions to support compliance with SWE Requirement 5.5.3. This guidance incorporates key best practices and considerations for assessing non-conformances in externally acquired and reused software components.

---

### **3.1 Non-conformances in Commercial or Reused Software**

#### **Challenges with Non-Conformance Management**

Non-conformances discovered in COTS (Commercial Off-the-Shelf), GOTS (Government Off-the-Shelf), MOTS (Modified Off-the-Shelf), OSS (Open-Source Software), and reused software components are particularly challenging to manage because:

* **Limited Transparency:** For externally developed software, insight into the development, testing, and quality assurance practices used to build the software is often unavailable.
* **Uncertainty in Risk Assessment:** Determining the impact of known defects on the broader system can be difficult, especially if the project does not have access to source code.
* **Dependency on External Entities:** NASA projects often rely on the vendor, supplier, or open-source community to provide fixes or updates to non-conformances, which can introduce delays or risks if unresolved defects impact critical operations.

#### **Required Activities for Non-Conformance Management**

To address these challenges, project teams must take the following specific actions:

1. **Catalog Known Defects and Non-Conformances**:

   * Identify whether the COTS, GOTS, MOTS, OSS, or reused software component has a list of known defects or non-conformances. This list is often shared via:
     + **Vendor portals or documentation** for COTS/GOTS/MOTS.
     + **Bug trackers or repositories** for OSS (e.g., GitHub Issues, Bugzilla).
     + Release notes, change logs, or issue databases maintained by developers.
   * Research these sources to evaluate whether any known issues could directly or indirectly impact the software’s functionality, performance, or mission-critical operations. Document this evaluation for each known defect.
2. **Assess System-Level Risk from Known Non-Conformances**:

   * Perform an **impact assessment** of each known defect on the software within the specific context of its use in the NASA system.
     + Example Considerations:
       - Does the defect affect safety-critical functions?
       - Could the defect compromise system integrity, timing, or availability?
       - Are there workarounds to mitigate the defect’s impact at the system level?
   * Use a **risk assessment framework** (e.g., likelihood and consequence analysis) to prioritize non-conformance review and mitigation.
3. **Engage with the Software Supplier or Community**:

   * Ensure that non-conformances discovered at the project level are communicated back to the supplier or developer to inform future updates or fixes.
   * For OSS:
     + Contribute issue reports to the open-source community to trigger collaborative resolution efforts.
     + Stay engaged in the community to monitor progress on critical defect resolutions.
   * For COTS/GOTS/MOTS:
     + Interface with the vendor to request updates, patches, or mitigation plans for unresolved defects.
   * Document all correspondence for traceability.
4. **Adjust Development or Integration Plans Based on Impact**:

   * Incorporate compensating measures for unresolved non-conformances:
     + Modify system architecture or design to minimize reliance on the defect-prone component.
     + Increase testing for areas suspected of defect interactions.
   * Document these changes and evaluate the residual risks.
5. **Focus on Criticality**:

   * Not all non-conformances will affect the system’s behavior or success. Assessments should prioritize defects with the **highest severity** levels, such as those impacting safety, mission operations, performance, or compliance with critical requirements.

#### **Best Practices**:

* Use **NASA Lessons Learned** (e.g., LLIS-2215) to understand historical challenges with these types of software and adjust risk assessment processes accordingly.
* Maintain **traceability** between non-conformances, severity levels, system impact assessments, and any mitigations implemented.

---

### **3.2 Assessments**

#### **Purpose of Mandatory Assessments**

Thorough assessments of all reported non-conformances in COTS, GOTS, MOTS, OSS, and reused software are **critical to mission success**. These assessments:

* Ensure non-conformances from these components are fully understood within the context of the NASA system.
* Provide opportunities to mitigate risks well before system integration or critical milestones.
* Identify gaps in the supplier’s testing and issue response processes, providing input to improve future versions or patches.

#### **Assessment Approach**

Conduct mandatory assessments using the following process:

1. **Engage Qualified Personnel**:

   * Assemble a cross-functional team that includes:
     + **Software Engineers**: To analyze technical risks and system interactions.
     + **Systems Engineers**: To assess end-to-end impacts of non-conformances on system operations.
     + **Software Assurance Personnel**: To verify that non-conformance assessments align with NASA’s quality standards, safety requirements, and severity categorizations.
   * Ensure that personnel evaluating the non-conformances understand both the system requirements and the operational environment.
2. **Assess Non-Conformances Against Project Requirements**:

   * Review all reported non-conformances in the software component against project-specific requirements, such as:
     + Functional requirements.
     + Safety-critical requirements.
     + Performance thresholds.
     + NASA standards for software integrity and reliability.
   * Use defect severity levels (e.g., "Critical," "Major," "Minor") to prioritize issues for resolution or mitigation. Severity definitions should align with those established by the project.
3. **Collaborate with the Supplier for Analysis**:

   * For externally developed software, report any newly discovered non-conformances back to the supplier or development organization.
   * Request an analysis from the supplier or community on the root cause of defects and their expected impact. If possible, coordinate for fixes or receive mitigation guidance.
4. **Schedule Regular Updates to Non-Conformance Reviews**:

   * Non-conformance lists for external software components are **living documents** that require ongoing review throughout the lifecycle:
     + Conduct regular follow-ups to identify any newly reported issues in updated versions of the software.
     + Track the status of open issues, ensuring that resolutions or mitigating measures are incorporated into the system design and risk management plan.
5. **Document Residual Risk of Unresolved Defects**:

   * If the supplier or community is unable to resolve all non-conformances, document the residual risks and justify their acceptance.
   * Ensure that the decision to retain a component with unresolved issues includes:
     + A rationale for continuing use.
     + Mitigation measures.
     + Safety and operational impacts.
6. **Incorporate Non-Conformance Data into Project Processes**:

   * Track non-conformance assessments in the project defect reporting system or risk registers.
   * Tie impact assessments to key project processes, such as trade studies and system test planning.

#### **Reporting and Tracking**

* Record the results of each non-conformance assessment in:
  + **Problem Reports or Change Requests (CR/PR):** Centralize communication and tracking for discovered non-conformances.
  + **Risk Management System:** Ensure non-conformances impacting requirements or operational safety are treated as risks and integrated into the project's risk review board.
  + **Configuration Management System (CMS):** Manage how any changes to address non-conformances are documented and implemented in system baselines.

---

### **References**

* **SWE-201 (Software Non-Conformances)**: Provides additional context and requirements for managing non-conformances across all types of software.
* **SWE-204 (Process Assessments)**: Highlights the importance of embedding process assessments as part of non-conformance evaluation.
* **Topic 8.08 (COTS Software Safety Considerations)**: Addresses safety-specific challenges related to the use of off-the-shelf software components.
* **Topic 5.01 (CR-PR - Software Change Request - Problem Report)**: Guides the tracking and resolution of non-conformances within a formal change management framework.

---

### **Conclusion**

This enhanced guidance ensures that NASA consistently evaluates and manages non-conformances in externally developed and reused software. By applying a rigorous, structured assessment process, projects minimize risk, improve system reliability, and ensure mission success.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances) * [SWE-204 - Process Assessments](/spaces/SWEHBVD/pages/102695538/SWE-204+-+Process+Assessments)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

See also Topic [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations).

See also [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances)

See also [SWE-204 - Process Assessments](/spaces/SWEHBVD/pages/102695538/SWE-204+-+Process+Assessments).

See also Topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) for reporting and tracking.

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Monitoring and Control](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Monitoring+and+Control)      * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

When dealing with smaller projects, the same core principles of mandatory assessments for non-conformances apply. However, small projects often have limited resources (e.g., fewer personnel, reduced budgets, tighter timelines). This tailored guidance provides streamlined, practical methods for meeting this requirement efficiently while still maintaining quality, safety, and mission assurance.

---

### **Understanding the Small Project Context**

Small projects may rely more heavily on external software components like COTS, GOTS, MOTS, OSS, or reused software due to resource constraints. Therefore:

* The risk of integrating software with unresolved defects can be higher, given fewer resources for mitigation.
* Teams must prioritize and simplify processes without skipping critical assessments.
* Emphasizing risk-based and lightweight approaches is key to balancing compliance with efficiency.

---

### **Key Goals for Small Projects**

1. Establish a **simple framework** for evaluating and tracking non-conformances.
2. **Focus on criticality** to prioritize high-severity defects with potential mission or safety impacts.
3. Leverage **existing resources and tools** (e.g., vendor-provided data, open-source issue trackers).
4. Eliminate redundant or overly complex processes that don’t add value.

---

### **Practical Steps for Small Projects**

#### **1. Use Risk-Based Prioritization for Assessments**

* **Focus on the essentials:** Identify and assess only the non-conformances that have the potential to impact:
  + **Safety** (astronaut, personnel, or system safety).
  + **Mission Success/Critical Functions**.
  + **System Performance** (e.g., data accuracy, timeliness, or reliability).
* Rely on historical mission risks, lessons learned from the NASA Lessons Learned database, and existing project risk analyses to inform prioritization.
* Example:
  + *For an OSS library with 50 logged non-conformances, focus only on those that affect the specific features or functions used in the project. Ignore irrelevant issues.*

#### **2. Leverage Existing Vendor or Community Data**

* **Simplify data collection by leveraging available resources:**
  + Vendor release notes, changelogs, issue trackers, and known defect lists for COTS/GOTS/MOTS.
  + Public repositories or bug trackers for OSS (e.g., GitHub Issues, Bugzilla, etc.).
  + Documentation or defect lists provided by prior teams using reused software.
* Review these sources to:
  + Identify known non-conformances.
  + Cross-check which known issues directly impact your project’s use of the software component.
  + Example: If a MOTS product has 10 known bugs, check which ones apply to your operational scenario.

#### **3. Streamline the Assessment Process**

* Conduct **lightweight assessments**:
  + Use a basic checklist or simplified template to record known non-conformances, their severity, and their potential impact on your project.
  + Include columns such as:
    - Non-conformance description.
    - Severity (Critical, Major, Minor, Trivial).
    - Potential impact (e.g., safety, mission success, operational disruption).
    - Mitigation plan (e.g., escalate to vendor, apply a workaround, monitor in operations).
* Example: A one-page assessment table can often replace in-depth analyses for small projects.

#### **4. Take Advantage of Team Expertise**

* For smaller teams, involve team members wearing multiple hats:
  + **Software engineers:** Analyze how non-conformances could interact with your system.
  + **Systems engineers:** Assess cross-system impacts.
  + **Software assurance lead (if available):** Verify risk assessments and mitigation plans.
* Keep team meetings for non-conformance assessments frequent but brief, focusing on critical issues.

#### **5. Emphasize a Direct Supplier or Vendor Partnership**

* For COTS/MOTS/GOTS components:
  + Establish a point of contact with the supplier or development organization to:
    - Report unresolved defects that impact your project.
    - Request vendor patches, updates, or mitigation guidance.
  + Document all communications for traceability.
* For OSS:
  + Submit impactful non-conformance reports directly to the open-source repository/community.
* Example: Use a NASA project email or shared repository for logging vendor communications and follow-ups.

#### **6. Monitor Open Issues Over Time**

* Use **simple tracking mechanisms** to manage ongoing non-conformances:
  + A spreadsheet or defect-tracking tool (e.g., Excel, Trello) is often sufficient for small projects.
  + Track the status of each issue (e.g., Open, In Progress, Closed) and associated resolution timelines.
  + Regularly review unresolved high-severity non-conformances during team meetings.
* Minimal effort yet effective tracking ensures important issues are not overlooked.

#### **7. Tailor Non-Conformance Closure Efforts**

* **Work smarter, not harder:**
  + Focus closure efforts on addressing "Critical" and "High" severity non-conformances.
  + Track "Low" severity or non-critical issues only for situational awareness.
* Clearly document any known, unresolved issues that are accepted or deferred, explaining why they are low priority.

---

### **Small Project Example Workflow**

1. **Discovery of Non-Conformances:**

   * The project identifies non-conformance reports via:
     + Vendor or OSS issue repositories.
     + Internal testing or simulations.
2. **Record and Assess:**

   * Use a one-page table or tracking sheet to log non-conformances.
   * Classify severity levels based on specific project impact.
3. **Develop and Track Mitigation Plans:**

   * For each non-conformance:
     + Determine if it impacts safety or mission success.
     + If critical, escalate to the vendor or identify workarounds.
     + Monitor progress and track closure of high-severity issues.
4. **Review Progress Regularly:**

   * Conduct bi-weekly team check-ins to discuss high-severity non-conformances that are still open.
   * Update tracking sheets or tools when new non-conformances are identified or resolved.
5. **Prepare for Milestones:**

   * Present an updated summary of unresolved non-conformances (if any) during review milestones (e.g., PDR, CDR).
   * Justify why unresolved issues do not compromise the project scope.

---

### **Simplified Tools and Resources for Small Projects**

1. **Spreadsheets for Tracking:**
   * Use templates in Excel, Google Sheets, or similar tools with columns for tracking non-conformance details, severity level, status, and resolution efforts.
2. **Open-Source or Free Bug Tracking Tools:**
   * Tools like Trello, OpenProject, or even GitHub Issues can be employed to simplify issue tracking and collaboration.
3. **Vendor Resources:**
   * Download and maintain archives of COTS/GOTS/MOTS release notes, defect lists, and known bugs for reference.
4. **Risk Registers:**
   * If tracking unresolved defects as risk, incorporate them into a lightweight risk register, prioritizing safety and mission-critical items.

---

### **Key Considerations for Small Projects**

* **Be resource-savvy**: Use easily accessible tools, data, and processes. Avoid creating complex systems unless truly needed.
* **Focus where it matters most**: Spend the majority of assessment time on defects with high project impact.
* **Leverage external support**: When overwhelmed with unresolved issues, engage suppliers, open-source communities, or NASA cross-program expertise for guidance.

---

### **Conclusion**

Small projects can efficiently meet SWE Requirement 5.5.3 by focusing on criticality, leveraging existing data and relationships, and using lightweight tools and methods. The goal remains the same: ensure that non-conformances in external or reused software are assessed and mitigated to avoid risks to the project’s safety, quality, and success while staying cost-effective and resource-efficient.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

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

NASA’s **Lessons Learned Information System (LLIS)** documents a wealth of knowledge derived from past projects, including cases where inadequate assessment and management of COTS, GOTS, MOTS, OSS, and reused software non-conformances impacted safety, mission success, cost, and schedule. These lessons can inform and guide the implementation of SWE 5.5.3. Below are key lessons learned that highlight the importance of compliance with this requirement:

---

### **1. LLIS-2215: Lack of Scalability and Reliability in COTS Software**

* **Lesson Learned:**  
  During integration and testing of a NASA system reliant on COTS software, unaddressed non-conformances in the software led to significant performance degradation under load. The scalability issues, though documented by the vendor, were not thoroughly assessed for their impact on NASA’s specific operational environment.
* **Connection to SWE 5.5.3:**  
  This lesson emphasizes the need to:

  + Assess vendor-documented non-conformances for their impact on scalability and reliability in NASA’s mission context.
  + Test externally acquired software in conditions that mimic the operational environment.
  + Implement contingency or mitigation plans for unresolved issues.
* **Relevant Action:**  
  Verify the operational limits of the software and conduct mandatory assessments against expected system loads and mission scenarios to ensure performance adequacy.

---

### **2. LLIS-1543: Unresolved Defects in Reused Software Caused System Failures**

* **Lesson Learned:**  
  A reused software component in a NASA ground system contained known unresolved non-conformances that the prior project deemed low risk; however, the new project’s operational context amplified the defects, leading to system failures and costly rework.
* **Connection to SWE 5.5.3:**  
  This lesson highlights the importance of:

  + Re-assessing the risks of known non-conformances in reused software within the specific use case of the current project.
  + Avoiding over-reliance on past risk assessments without validating against new mission-critical requirements.
* **Relevant Action:**  
  For each reused software component:

  + Conduct an updated evaluation of the known defects’ impact on the new system.
  + Document acceptance of residual risks, ensuring proper justification and traceability.

---

### **3. LLIS-31763: Vendor-Assumed Responsibility for Non-Conformances Requires Scrutiny**

* **Lesson Learned:**  
  A NASA mission suffered delays because the project team relied on a COTS vendor's assurances that critical non-conformances would be resolved in future product updates. The vendor failed to provide fixes on time, leading to integration delays and the need for late-stage workarounds.
* **Connection to SWE 5.5.3:**  
  Mandatory assessments must not only catalog known non-conformances but also account for the vendor's track record, support capabilities, and ability to deliver promised fixes. Dependence on external fixes must be part of the risk assessment, with mitigation strategies in place for delays or failure to resolve the issues.
* **Relevant Action:**
* Develop contingency plans to reduce reliance on vendor timelines for non-conformance resolution.
* Escalate issues earlier and establish robust communication with the vendor.

---

### **4. LLIS-3026: Insufficient Testing of OSS Components Introduced Vulnerabilities**

* **Lesson Learned:**  
  An open-source library used in a NASA mission contained several known vulnerabilities documented in the project’s tracking system but not fully evaluated. Some of these vulnerabilities were exploited by automated tools during system tests, jeopardizing security and system integrity.
* **Connection to SWE 5.5.3:**  
  This lesson underscores the importance of thoroughly assessing OSS non-conformances, especially where security risks or vulnerabilities are involved.
* **Relevant Action:**  
  Mandatory assessments for OSS must prioritize:

  + Evaluating known security vulnerabilities.
  + Testing for exploitability in the operational environment.
  + Applying updates, patches, or mitigations before deployment in mission-critical systems.

---

### **5. LLIS-1590: Overlooking Integration Risks of COTS Software**

* **Lesson Learned:**  
  For a NASA satellite mission, integration risks of a COTS software application were not thoroughly assessed. While the software performed well in isolation, system testing revealed conflicts between the COTS software and custom modules, resulting in mission-critical delays.
* **Connection to SWE 5.5.3:**  
  This lesson demonstrates the necessity of assessing non-conformances not just within the external software itself, but also how those non-conformances might interact with other components or systems.
* **Relevant Action:**
* Include interface and integration testing in the non-conformance assessment process.
* Document risks related to interactions with other software and mitigate during design or testing.

---

### **6. LLIS-1819: Failure to Track Vendor Issue Resolution**

* **Lesson Learned:**  
  A reused GOTS software product had several known issues flagged by NASA field centers, but the lack of centralized tracking led to inconsistent assessments across projects. As a result, critical defects in the software were rediscovered, causing avoidable rework and project delays.
* **Connection to SWE 5.5.3:**  
  Without effective tracking and reporting of vendor-reported non-conformances, the same issues can recur across multiple projects, resulting in inefficiencies and risks.
* **Relevant Action:**
* Maintain centralized records of vendor-reported non-conformances and their impact on NASA projects.
* Use lessons learned from other projects to guide reuse and risk-assessment efforts.

---

### **7. LLIS-21407: Time-Critical Missions and Oversight of COTS Non-Conformances**

* **Lesson Learned:**  
  A fast-paced NASA project skipped mandatory assessments for COTS software non-conformances due to schedule pressure. This decision led to significant downstream schedule overruns, as defects became apparent during late-stage testing, requiring re-evaluation and mitigation.
* **Connection to SWE 5.5.3:**  
  Schedule constraints must not override the requirement to assess non-conformances in acquired software. The long-term cost of skipping assessments often outweighs the short-term gain in project speed.
* **Relevant Action:**  
  Plan for early non-conformance assessments and build schedule flexibility to accommodate any mitigation actions. Use a **risk-based approach** to prioritize critical assessments when resources are tight.

---

### **8. LLIS-1367: Managing Non-Conformances in International GOTS Collaboration**

* **Lesson Learned:**  
  In a collaborative international mission, a GOTS software package developed by a partner organization included known issues that were not assessed against NASA’s mission requirements. The misalignment of issue prioritization between the partner and NASA led to integration conflicts.
* **Connection to SWE 5.5.3:**  
  Joint international efforts require clear communication and alignment on GOTS non-conformance impacts. Assessments must account for gaps in how different organizations define severity and criticality.
* **Relevant Action:**
* Establish clear cross-organizational communication regarding non-conformance impacts.
* Document all defect evaluations in a shared system for easy reference during joint integration efforts.

### 9. **Communication Failures Suppressing Software Concerns**

**Incident:**  
Software and system engineers raised concerns that were not acted upon. The culture fostered a “prove there is a problem” mentality, making it difficult to elevate software risks. No Independent Technical Authority (ITA) dissents were filed despite significant issues.

**Lesson Learned:**

* **Open Technical Channels:** Projects must maintain safe, responsive pathways for raising technical concerns, including through independent authorities.
* **Cultural Reinforcement:** Leadership must encourage early reporting and prohibit cultures that penalize raising risks.

**Implication:**  
When team members feel unheard, systemic issues go unaddressed, increasing mission risk and slowing problem resolution.

---

### **Summary of Key Takeaways from NASA Lessons Learned**

1. **Assess Non-Conformances for Context**: Known defects in reused, COTS, GOTS, MOTS, and OSS components may have different impacts in new systems—context-specific evaluation is critical.
2. **Prioritize Criticality and Utilize Vendor/Community Data**:  
   Focus on addressing high-severity issues and use existing defect databases or bug trackers to inform assessments.
3. **Maintain Centralized Tracking**:  
   Track known non-conformances across the software lifecycle to prevent rediscovery and streamline reuse decisions.
4. **Engage Vendors and Communities**:  
   Involve external developers in resolution tracking and maintain clear communication about impacts and timelines.
5. **Integrate Risk Mitigation Early**:  
   Identify and mitigate risks from non-conformances during design and integration phases to avoid costly late-stage rework.

By applying these lessons learned, NASA projects can better implement SWE 5.5.3, ensuring the integrity of mission-critical systems using external or reused software components.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [FSW/FSSE anomaly investigations and FSW changes](https://software.gsfc.nasa.gov/lesson-details/80/). **Lesson Number 80**: The recommendation states: "Have one FSW/FSSE person not assigned to console support, dedicated specifically to anomaly investigations and FSW changes."

# 7. Software Assurance

**SWE-203 - Mandatory Assessments for Non-Conformances**

5.5.3 The project manager shall implement mandatory assessments of reported non-conformances for all COTS, GOTS, MOTS, OSS, and/or reused software components.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm the evaluations of reported non-conformances for all COTS, GOTS, MOTS, OSS, or reused software components are occurring throughout the project life cycle.

2. Assess the impact of non-conformances on the project software's safety, quality, and reliability.

## 7.2 Software Assurance Products

This guidance provides a structured, actionable framework for software assurance activities related to the assessment of non-conformances in COTS, GOTS, MOTS, OSS, and reused software components, ensuring all issues are identified, analyzed, tracked, and resolved efficiently with special attention to safety-critical and mission-critical considerations.

#### **Improved List of Products**

1. **Software Design Analysis**:

   * Assess how the design interacts with COTS, GOTS, MOTS, OSS, or reused components. Verify whether known non-conformances could disrupt design assumptions, such as interfaces, dependencies, and integration.
   * Documentation: Provide reports detailing the integration impact analysis of non-conformances.
2. **Source Code Analysis**:

   * For reused components or OSS where source code is accessible:
     + Analyze the code for issues flagged in non-conformance reports using static analysis tools.
     + Document areas where known non-conformances could propagate errors or vulnerabilities within operational scenarios.
3. **Verification Activities Analysis**:

   * Ensure that test plans, procedures, and results comprehensively address reported non-conformances.
   * Assure that verification coverage explicitly includes those areas affected by unresolved defects.
4. **SA Impact Assessment of Non-Conformances on Safety, Quality, and Reliability**:

   * Conduct detailed analyses of reported non-conformances, focusing on risks to safety-critical areas, system reliability, and operational integrity.
   * Prepare impact assessment checklists and traceability matrices to show links between potential defect impacts and project quality metrics.
5. **Defect or Problem Reporting Data**:

   * Compile a centralized list of non-conformances or defects for external components used in the system (COTS, GOTS, MOTS, OSS, reused).
   * Ensure the accuracy and completeness of data within the project’s discrepancy database, including severity level, status, and timeframe for resolution.
6. **Software Configuration Management Data**:

   * Verify that all non-conformances or associated fixes are properly recorded and baselined. Review version histories for any COTS/OSS/MOTS updates and mitigation measures applied.
7. **Software Assurance Audit Results in Change/Defect Management Processes**:

   * Audit the defect tracking system and change records to ensure all reported non-conformances are appropriately categorized, assessed, and resolved.
   * Verify that high-priority issues (e.g., safety-impacting defects) are escalated quickly.
8. **Milestone Results**:

   * Review non-conformance status across project milestones (PDR, CDR, TRR, and operational readiness reviews) to verify that defects have been adequately assessed and addressed before advancing.
9. **Software Version Description Documents (VDDs)**:

   * Ensure that VDDs explicitly define residual risks related to unresolved COTS, GOTS, MOTS, OSS, or reused software issues. Provide clear justification for their acceptance (if applicable).
10. **Software Control Board Data or Presentations**:

    * Confirm SCB meeting minutes include discussions about unresolved non-conformances. Verify that action plans and resolutions are documented for defects flagged as high-risk.

## 7.3 Metrics

#### **Refined Metrics for Tracking Non-Conformances**

1. **Total Number of Non-Conformances**:

   * Track the cumulative number of non-conformances across the lifecycle (open, closed, # of days open, severity of open).
   * Include counts for defects flagged during system integration that originate from COTS, GOTS, OSS, MOTS, or reused software.
2. **Non-Conformances in Current Reporting Period**:

   * Metric: Measure the number of newly identified non-conformances (open and closed), focusing on severity levels to prioritize resolution.
3. **Source Code Non-Conformances**:

   * Track non-conformances specific to source code where analysis tools have flagged unresolved issues (e.g., OSS reuse components or other accessible code).
4. **Safety-Related Non-Conformances**:

   * Metric: Track the number of safety-critical non-conformances systematically and ensure these are given utmost priority in corrective action plans.
5. **Non-Conformance Closure Rates**:

   * Compare the total number of non-conformances identified in embedded COTS, GOTS, MOTS, OSS, or reused components to the number successfully closed and mitigated.

#### **Additional Metrics for Mitigation Progress**:

* Time to first mitigation action for high-severity issues.
* Vendor responsiveness (for external fixes).
* Non-conformance trends by component over time.

## 7.4 Software Assurance Guidance

#### **Software Assurance Responsibilities**

1. **Verify Regular Reporting of Non-Conformances**:

   * Ensure that the project team is receiving periodic updates from vendors, open-source repositories, or other stakeholders on existing and newly reported non-conformances.
   * Use a discrepancy tracking system or centralized registry to log and monitor all defects.
2. **Assess Project Impacts**:

   * Confirm that the project team is reviewing non-conformance lists to assess impacts on:
     + **Safety:** Review how non-conformances interact with hazard analyses, particularly for safety-critical areas.
     + **Quality:** Ensure defect impacts on data accuracy, processing integrity, or software functions are evaluated.
     + **Reliability:** Determine whether reported issues could compromise the system’s ability to perform mission-critical operations without failure.

#### **Assessing Safety-Critical Software**:

For non-conformances affecting safety-critical areas:

* Conduct detailed reviews of associated hazard analyses to quantify the operational and physical risks.
* Example: Determine whether the defect impacts redundancy or fault-tolerant mechanisms designed to ensure mission survivability.

#### **Assessing Non-Safety Software Impact**:

For defects in non-safety-critical code, evaluate:

* Computational accuracy: Does the defect lead to incorrect results?
* Functional reliability: Can the defect disrupt operation of critical software modules?
* Performance degradations: Does the defect cause unacceptable delays or resource consumption?
* Visual/Display issues: Determine whether the defect reduces human operator effectiveness or usability.

#### **Use Code Analyzers Where Source Code is Available**:

When the source code is provided:

* Apply static or dynamic code analyzers to establish whether non-conformances are reproducible.
* Use results from analyzers to validate severity classifications, supporting risk mitigation prioritization.

#### **Track Fixes to Closure**:

Verify that all significant non-conformances are:

* Registered in the project discrepancy database.
* Tracked to closure with clear evidence of resolution or mitigation.

---

#### **Mitigation and Change Implementation**

1. **Vendor Updates and Fixes**:

   * Ensure the project is implementing all vendor-provided patches, updates, or workarounds for defects that affect operations.
   * Provide oversight to confirm these updates do not introduce additional risks or defects.
2. **Residual Risk Acceptance**:

   * Verify that any unresolved non-conformances are documented with clear rationale for acceptance, considering operational impact and risk mitigation strategies.
3. **Operational Testing for Risk Acceptance**:

   * Perform robust testing for scenarios where non-conformance residual risks were accepted. Ensure the system can handle edge cases safely and effectively.

---

#### **Proactive Actions for Software Assurance**

1. **Training**:  
   Provide training to software assurance personnel on best practices for assessing vendor-reported COTS, GOTS, MOTS, OSS non-conformances, and interpreting source code impacts.
2. **Interfacing with External Teams**:  
   Ensure that software assurance actively interfaces with vendors, suppliers, and open-source communities to verify resolutions and advocate for fixes where high-risk defects exist.
3. **Review Milestones**:  
   Actively participate in milestone reviews (PDR, CDR, TRR) to ensure non-conformance status is accurately reported and risks are fully assessed before proceeding.

---

### **Conclusion**

This improved guidance provides actionable activities and relevant products to help software assurance teams verify compliance with SWE Requirement 5.5.3. It incorporates systematic tracking, prioritization, impact assessment, and resolution of all non-conformances in COTS, GOTS, MOTS, OSS, and reused software, enhancing mission safety, quality, and reliability. The additional emphasis on proactive engagement with vendors and targeted metrics ensures effective control over potential defects throughout the lifecycle.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances) * [SWE-204 - Process Assessments](/spaces/SWEHBVD/pages/102695538/SWE-204+-+Process+Assessments)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

The objective evidence is the documented proof and artifacts that demonstrate compliance with this requirement, verifying that the project has implemented the necessary processes for assessing and managing non-conformances in externally acquired or reused software components (COTS, GOTS, MOTS, OSS, reused). Below is a list of suggested objective evidence:

---

### **1. Records of Non-Conformance Reports (NCRs)**

* **Description**: A log or list of all reported non-conformances associated with COTS, GOTS, MOTS, OSS, or reused software components.
* **Details to Include**:
  + Non-conformance description.
  + Identified component (e.g., library, tool, or subsystem).
  + Severity categorization (e.g., Critical, Major, Minor).
  + Status (Open, In Progress, Closed).
  + Date of identification and target resolution date.
  + Source of the report (e.g., vendor, open-source repository, internal discovery).
  + Reference to supporting defect or issue trackers.
* **Example Tool**: Spreadsheets, Jira, Azure DevOps Query or Defect Tracking Reports, or in-house discrepancy systems.

---

### **2. Non-Conformance Impact Assessment Reports**

* **Description**: Documentation demonstrating that each identified non-conformance has been assessed for its impact on the project.
* **Key Elements**:
  + Evaluation criteria: Safety, quality, reliability, and operational impacts.
  + Hazard and risk analysis (especially for safety-critical software).
  + Residual risk justification for unresolved issues.
  + Mitigation plans or compensating measures implemented for non-conformances flagged as high-risk.
* **Examples**:
  + Risk assessment matrices or fault trees.
  + Traceability tables linking non-conformances to system requirements or hazards.
  + Documentation of risk acceptance approvals.

---

### **3. Vendor or Open-Source Non-Conformance Data**

* **Description**: Copies or summaries of non-conformance reports obtained from external sources.
* **Sources May Include**:
  + Vendor release notes documenting known issues and limitations.
  + Open-source software issue trackers (e.g., GitHub Issue List, Bugzilla entries).
  + Changelogs showing known defects resolved, introduced, or outstanding in each version.
  + Prior project defect reports related to reused software components.
* **Examples**:
  + Screenshots or PDFs of issue information from vendor/customer portals.
  + Repository snapshots or a copy of a known-defects database for OSS.

---

### **4. Discrepancy Database Entries and Tracking**

* **Description**: Centralized entries in the project’s discrepancy database for tracking all non-conformances related to external software.
* **Key Details to Verify**:
  + Every significant COTS, GOTS, MOTS, OSS, or reused component non-conformance is logged in the database.
  + Lifecycle data: Date opened, status, resolution plan, closure details.
  + Links to software assurance audit findings, system integration tests, and configuration management records.
* **Example Tools**: NASA’s Problem Reporting and Corrective Action System (PRACA), software defect tracking systems.

---

### **5. Test Results Related to Non-Conformance Mitigation**

* **Description**: Test results showing how non-conformance risks were addressed or mitigated during verification and validation activities.
* **Key Evidence**:
  + Test procedures designed specifically to validate software mitigations for reported defects.
  + Results of regression tests after applying vendor patches or updates.
  + Operational readiness tests tied to risk-based scenarios related to unresolved non-conformances.
* **Examples**:
  + Test reports or acceptance data demonstrating defect coverage.
  + Bug fix verification test logs.

---

### **6. Software Configuration Management Artifacts**

* **Description**: Evidence that changes to address non-conformances have been managed in the software configuration management process.
* **Key Evidence**:
  + Version control logs showing updates or patches.
  + Software version description documents (VDDs) for releases with known defects or fixes applied.
  + Change requests documenting defect-related updates.
* **Examples**:
  + Software configuration change logs.
  + VDDs with descriptions of non-conformance resolutions in specific versions.

---

### **7. Meeting Minutes and Reviews (e.g., SCB, SRBs)**

* **Description**: Minutes or presentations documenting discussions and decisions related to non-conformances.
* **Relevant Meetings**:
  + Software Configuration Boards (SCB) to discuss configuration changes linked to defect resolution.
  + Safety Review Boards (SRB) evaluating safety risks of unresolved non-conformances.
  + Test Readiness Reviews (TRR) or Operational Readiness Reviews (ORR) ensuring all non-conformances have been addressed.
* **Examples**:
  + Agendas and minutes showing non-conformance prioritization and resolution progress.
  + Presentation slides summarizing non-conformance impact analyses.

---

### **8. Correspondence with Vendors/Developers**

* **Description**: Records showing engagement with vendors (COTS/MOTS/GOTS) or open-source communities.
* **Key Evidence**:
  + Emails, meeting notes, or support tickets requesting updates, mitigations, or clarification about unresolved defects.
  + Vendor responses clarifying non-conformance impacts or timeline for fixes.
  + Community contributions for OSS non-conformance reports (e.g., GitHub issue reports).
* **Examples**:
  + Emails documenting defect communication.
  + Support tickets tracking vendor or community engagement.

---

### **9. Software Assurance Audit Reports**

* **Description**: Reports from software assurance audits of the change management and defect management processes related to the project.
* **Key Audit Topics**:
  + Assurance that all non-conformances are being tracked, assessed, and mitigated.
  + Verification that high-severity non-conformances (e.g., safety-critical) are appropriately prioritized.
* **Examples**:
  + Audit reports documenting findings on non-conformance controls and compliance.
  + Observed discrepancies and corrective actions.

---

### **10. Milestone Review Data**

* **Description**: Artifacts from project milestone reviews demonstrating that non-conformance assessments and resolutions were completed as part of readiness criteria.
* **Key Reviews**:
  + Preliminary Design Review (PDR): Evidence of non-conformance analysis at the design stage.
  + Critical Design Review (CDR): Evidence of planned mitigations for unresolved non-conformances.
  + Test Readiness Review (TRR): Evidence of testing coverage for reported defects.
  + Deployment Readiness Review: Assessment of acceptable residual risks.
* **Examples**:
  + Checklists verifying non-conformance closure before phase transitions.
  + Action items for addressing unresolved or new non-conformances.

---

### **11. Risk Management Documentation**

* **Description**: Risk management artifacts showing how unresolved non-conformances were treated or accepted.
* **Key Evidence**:
  + Risk registers detailing entries for critical non-conformances.
  + Mitigation plans or trade studies addressing risk acceptability.
  + Approved changes to non-conformance status or acceptance rationales.
* **Examples**:
  + Risk acceptance documentation (signed by appropriate authorities).
  + Hazard reports for safety-impacting software.

---

### **12. Metrics on Non-Conformance Trends**

* **Description**: Quantitative data showing the project's progress in identifying, managing, and resolving non-conformances.
* **Metrics Should Include**:
  + Total number of defects (open, closed, resolved over time).
  + Average time to closure.
  + Breakdown of severity levels (Critical, Major, Minor).
  + Closure rates for COTS, GOTS, MOTS, OSS, and reused software components.
  + Percent of safety-critical non-conformances resolved.
* **Examples**:
  + Graphs or tables tracking non-conformance status over time.
  + Reports comparing open defects vs. resolved defects at each milestone.

---

### **Key Takeaways**

The objective evidence for SWE Requirement 5.5.3 should demonstrate that non-conformances have been identified, assessed, documented, tracked, and closed (or accepted with justification). The artifacts ensure transparency, traceability, and confidence that non-conformance risks are being mitigated effectively to safeguard system success and mission performance.

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
