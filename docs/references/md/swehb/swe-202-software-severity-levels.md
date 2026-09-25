# SWE-202 - Software Severity Levels

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695536. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels

SWE-202 - Software Severity Levels

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695536)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695536&showCommentArea=true&showComments=true#addcomment)

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

5.5.2 The project manager shall define and implement clear software severity levels for all software non-conformances (including tools, COTS, GOTS, MOTS, OSS, reused software components, and applicable ground systems).

## 1.1 Notes

At a minimum, classes should include loss of life or loss of vehicle, mission success, visible to the user with operational workarounds, and an ‘other’ class that does not meet previous criteria.

## 1.2 History

Click here to view the history of this requirement: SWE-202 History

SWE-202 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 5.5.2 The project manager shall define and implement clear software severity levels for all software non-conformances (including tools, COTS, GOTS, MOTS, OSS, reused software components, and applicable ground systems). |
| Difference between C and D | No change |
| D | 5.5.2 The project manager shall define and implement clear software severity levels for all software non-conformances (including tools, COTS, GOTS, MOTS, OSS, reused software components, and applicable ground systems). |

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

Severity is defined as the degree of impact a defect has on the development or operation of the software being tested.  A higher effect on the system functionality will lead to the assignment of higher severity to the bug. Severity indicates the seriousness of the defect in the software functionality.  These software severity levels should be defined and implemented clearly.

This requirement establishes the foundation for managing software non-conformances by categorizing their impact based on **severity**. By clearly defining and implementing severity levels, the project manager ensures that all non-conformances (errors, defects, or discrepancies) are assessed, prioritized, and addressed appropriately based on their potential impact on the system, mission, or safety. Below is the rationale for this requirement:

---

### **1. Prioritizing Defect Resolution to Protect Mission Success**

* **Rationale:** In complex software systems, not all non-conformances carry the same level of impact. Severity levels provide a structured way to prioritize the resolution of issues based on their potential consequences.
* **Why It’s Important:**
  + High-severity non-conformances (e.g., critical calculation errors or system crashes) directly impact mission objectives and need immediate attention.
  + Medium or low-severity defects (e.g., minor user interface bugs) can be deferred until higher-severity issues are resolved.
* **Outcome:** Resources are allocated efficiently, ensuring that critical mission functionality is protected, and less urgent issues do not overwhelm the defect management pipeline.

---

### **2. Ensuring Safety and Risk Mitigation**

* **Rationale:** For life-critical software (e.g., human spaceflight, environmental control), defining severity levels is essential to prioritize defects that pose the highest risks to safety or operational stability.
* **Why It’s Important:**
  + Failures in ground systems, reused software components, or third-party tools (like COTS or MOTS) can cascade into mission-critical systems.
  + High-severity classifications ensure focus on potential risks to human life, equipment, or mission-critical operations.
* **Outcome:** Safety-related issues are elevated for immediate resolution, and risks are managed proactively to mitigate life-threatening or mission-jeopardizing scenarios.

---

### **3. Establishing Clear Communication Across Teams**

* **Rationale:** By defining and implementing severity levels, the project team establishes a **common language** for discussing and managing non-conformances.
* **Why It’s Important:**
  + Cross-disciplinary teams (e.g., testers, developers, system engineers, and software assurance) need clearly defined terms to evaluate and respond to issues consistently.
  + Severity levels reduce ambiguity in understanding the impact of defects and enable better decision-making at Configuration Control Boards (CCBs) or defect management reviews.
* **Outcome:** Improved coordination, streamlined decision-making, and fewer delays in addressing critical software issues.

---

### **4. Enabling Consistency in Assessing Non-Conformances Across All Software**

* **Rationale:** This requirement ensures that all types of software in the project, from mission-critical software to ground systems and third-party software components, are evaluated consistently.
* **Why It’s Important:**
  + Tools (used for development, testing, or deployment) and external software components (e.g., COTS, GOTS, MOTS, OSS) can often cause defects in mission software. These must be assigned appropriate severity levels based on their downstream effects.
  + Clear severity definitions ensure that reused software and third-party systems are assessed under the same criteria as project-specific software.
* **Outcome:** Comprehensive and consistent severity assignment creates a universal standard for evaluating issues, reducing oversights of important software defects.

---

### **5. Supporting Compliance with NASA Standards and Software Safety Policies**

* **Rationale:** NASA requires rigorous processes for categorizing and managing software defects (e.g., SWE-202). Severity levels align with these standards to ensure compliance across all software lifecycle phases.
* **Why It’s Important:**
  + Severity levels assist in applying quality assurance policies and processes, and tracking software metrics as mandated by NASA standards (e.g., tracking open vs. closed non-conformances by severity).
  + They provide the required evidence for audits, reviews, and compliance during major milestones, such as PDRs, CDRs, and TRRs.
* **Outcome:** Ensures adherence to NASA’s safety-critical processes, software lifecycle standards, and regulatory compliance.

---

### **6. Improving Long-Term Maintenance, Reuse, and Continuous Improvement**

* **Rationale:** Non-conformance severity definitions are a critical component of defect logging and traceability, enabling informed decisions for software maintenance and reuse.
* **Why It’s Important:**
  + Defects categorized by severity create a historical record, allowing future teams to evaluate and mitigate risks when reusing or upgrading existing software.
  + Weak spots in development processes can be identified by analyzing trends in defect severity over time (e.g., repeated high-severity defects linked to poorly defined requirements).
* **Outcome:** Leads to a more robust defect resolution history, enabling continuous improvement of software quality and easier reuse of software products in future missions.

---

### **7. Guiding Resource Allocation for Timely Resolution**

* **Rationale:** Defining severity levels ensures that resources (e.g., time, personnel, budget) are concentrated effectively on the most critical software issues.
* **Why It’s Important:**
  + Time-sensitive missions require balancing ongoing development with defect management. A severity classification system helps focus resources where they are needed most.
  + Limited resources during testing, validation, or operation phases can be used effectively by prioritizing severe non-conformances.
* **Outcome:** Prevents wasted effort on resolving low-impact defects ahead of critical issues, ensuring timely delivery and mission-readiness.

---

### **8. Supporting Cybersecurity Response**

* **Rationale:** In the context of evolving threats, severity levels help triage cybersecurity vulnerabilities discovered in software systems and third-party components.
* **Why It’s Important:**
  + Cybersecurity vulnerabilities with severe consequences (e.g., exposing mission-critical systems to malicious attacks) can lead to catastrophic failures if unresolved.
  + Severity classifications help differentiate between routine weaknesses and urgent vulnerabilities, guiding appropriate response plans.
* **Outcome:** A defined severity framework provides the grounding for rapid responses to high-severity cybersecurity vulnerabilities, reducing the likelihood of mission disruptions due to external threats.

---

### **Key Considerations for Implementing Severity Levels:**

* **Tailored Definitions:** Severity levels should be tailored to the project’s mission, operational environment, software type (e.g., ground systems vs. flight systems), and stakeholder risk tolerances.
* **Comprehensive Scope:** Non-conformances must cover issues in all relevant software categories, including:
  + Mission-critical software.
  + Development tools and test systems.
  + Third-party software (COTS, GOTS, MOTS, OSS).
  + Reused software components.
* **Regular Refinement:** Project managers should periodically review and refine severity definitions to address unforeseen risks and anomalies encountered during development/testing.

---

### **Conclusion**

Requirement 5.5.2 ensures that every software non-conformance—regardless of its origin—can be categorized and prioritized based on its severity. The explicit definition of software severity levels ensures **consistency, risk mitigation, efficient resource allocation, and streamlined project management** while supporting mission success. By classifying the impact of all software defects, this requirement forms the foundation for effective defect management processes across NASA projects.

# 3. Guidance

This guidance refines the process for defining and implementing clear severity levels for software non-conformances. The aim is to ensure consistency, traceability, and risk-based prioritization of software issues, enabling better resource allocation and alignment with NASA's mission goals.

---

## 3.1 Severity Level Definitions

Assigning severity levels to software non-conformances is a critical step in managing software quality and ensuring that defects are prioritized based on their impact. By defining severity levels tailored to the project’s specific requirements, project managers and engineering teams can ensure that resources are focused on correcting high-risk defects while still tracking and addressing less critical issues.

### **Key Objectives for Software Severity Level Definitions:**

1. **Prioritize Defect Resolution:** Ensure that issues with the highest impact on mission success, safety, or system integrity are addressed first.
2. **Facilitate Collaboration and Consistency:** Create a common framework for classifying and prioritizing issues across multidisciplinary teams, including software engineers, systems engineers, subsystem engineers, and other stakeholders.
3. **Simplify Reporting and Metrics:** Provide clear, consistent severity classifications to improve the tracking, reporting, and trend analysis of software defects.
4. **Enhance Risk Management:** Reduce the latent risk associated with unresolved defects in software components, particularly those related to tools, COTS, GOTS, MOTS, OSS, and reused code.

---

### **Defining Severity Levels**

Severity levels should reflect the unique mission-critical characteristics of each project and software component. Teams should take into account the following:

* System criticality (e.g., human-rated systems, mission-critical payloads, operations software).
* Risks to astronaut, employee, and public safety.
* Disruption to mission timelines, system functionality, or science data collection.
* Possible loss of government investments (e.g., equipment damage, missed science opportunities).
* Dependencies on third-party components, particularly tools, COTS, GOTS, MOTS, OSS, and reused software.

**Key Actions for Defining Severity Levels:**

* Involve **cross-disciplinary teams** to ensure that severity levels comprehensively address software’s impact on all project systems and stakeholders.
* Regularly **review and refine severity definitions** in response to emerging risks or project requirements.
* Document severity definitions in project guidelines and ensure alignment with industry standards (e.g., NASA Software Engineering Handbook, SWE-202).

### **Example Severity Level Framework**

Below is a more robust and clearly structured severity level framework, building on the existing examples:

#### **1. Critical (P1):**

* **Definition:** An issue that poses an immediate threat to mission success, safety, or system integrity. Critical defects require immediate resolution to avoid catastrophic failure or unacceptable risk.
* **Examples:**
  + Bugs that cause a system crash of mission-critical subsystems.
  + Defects that compromise human safety or operational control.
  + Non-conformances in ground systems that halt launch readiness.
  + Cybersecurity vulnerabilities resulting in system compromise or data breaches.
* **Response Time:** <1 week.
* **Action Required:** Must be resolved immediately. Requires management escalation.

#### **2. High (P2):**

* **Definition:** An issue that impacts mission objectives significantly but does not pose an immediate threat. Addressing these issues reduces the likelihood of failure or significant impact on operations.
* **Examples:**
  + Software defects that reduce system performance, reliability, or functionality.
  + Data integrity issues in payload or mission data systems.
  + Reused software (e.g., OSS) behaving unpredictably under specific conditions.
* **Response Time:** 1–2 weeks.
* **Action Required:** Planned for resolution during the development/testing lifecycle.

#### **3. Medium (P3):**

* **Definition:** An issue that could impact components or work products but does not threaten immediate mission success. Addressed after higher-priority issues.
* **Examples:**
  + Defects causing minor workflow interruptions in data processing systems.
  + Bugs with workaround solutions that maintain operational functionality.
  + Discrepancies in user interfaces or development tools.
* **Response Time:** 3–6 weeks.
* **Action Required:** To be resolved during iterative development, if resources are available.

#### **4. Low (P4):**

* **Definition:** An issue that has minimal or no significant impact on mission objectives and functionality. Typically cosmetic or non-essential.
* **Examples:**
  + Usability improvements, minor typos in documentation.
  + Graphical presentation bugs in non-critical displays.
* **Response Time:** >6 weeks (or when resources permit).
* **Action Required:** Addressed as part of continuous refinement or maintenance.

#### **5. Trivial or Editorial:**

* **Definition:** A non-conformance with no measurable impact on system functionality, performance, or operations.
* **Examples:**
  + Changes to styles in reports, comments, or logging messages.
  + Test scripts with minor formatting errors.
* **Action Required:** Resolved at the project team’s discretion.

---

### **Special Considerations for Third-Party Software (COTS, GOTS, MOTS, OSS, Reused Software):**

1. **Research Known Defects:**

   * Check public or vendor-maintained websites for bug lists, release notes, and known issues.
   * Verify whether known issues impact your project’s implementation context.
2. **Evaluate Risk Exposure:**

   * Assign severity levels to known issues and document their potential risk based on your system’s requirements.
   * For reused or open-source software, collaborate with original developers or maintainers to assess the inherent risk of unresolved defects.
3. **Track Vendor Updates:**

   * Ensure that patches or updates from the vendor are aligned with your project's software configuration. Incorporate defect fixes into your system as required.
4. **Assess Latent Risks:**

   * Non-conformance tracking data for third-party software should be integrated into the project’s risk management assessments. This helps evaluate the cumulative risk posed by unresolved defects in external components.

---

### **Guidance for Implementing Severity Levels**

#### **1. Simplify the Severity Levels Where Appropriate:**

* Strive for a **manageable number of severity levels**—typically between 3 and 5—to simplify tracking, classification, and reporting.
* Avoid overly granular definitions that can complicate prioritization.

#### **2. Document Severity Classifications in Project-Specific Terms:**

* Clearly define and tailor severity levels based on the **project’s unique mission requirements** and risks.
* Include definitions in project-level documentation, such as:
  + Configuration management plans.
  + Software assurance documents.
  + Project charters.

#### **3. Communicate and Align Definitions Across Teams:**

* Train all engineers and stakeholders (e.g., software developers, software assurance personnel, systems engineers) on severity definitions to ensure consistent classification of issues.
* Collaborate with subsystem engineers to align severity rankings across software and hardware domains.

#### **4. Continuously Improve Severity Definitions:**

* Analyze metrics for trends (e.g., defect closure rates by severity) and adjust severity level definitions as needed.
* Use lessons learned and outcomes from project reviews to inform and refine severity categorizations.

#### **5. Track and Report Metrics by Severity:**

* Monitor:
  + Open vs. closed non-conformances by severity.
  + Trends in severity over phases (e.g., testing, operations).
  + Cumulative risk exposure for unresolved non-conformances.

---

### **Conclusion**

Clear severity level definitions are fundamental to effective non-conformance tracking, prioritization, and resolution. By tailoring and simplifying severity levels, ensuring consistency across teams, and incorporating feedback from all relevant stakeholders, project teams can maintain focus on resolving defects that have the greatest impact on mission success and safety. This guidance enables robust decision-making and enhances long-term project efficiency while aligning with NASA's stringent software quality requirements.

See also [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances). [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes),

See also Topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) for tracking and reporting.

See also Topic [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations).

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Monitoring and Control](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Monitoring+and+Control)      * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

Small projects often face constraints such as limited budgets, compressed schedules, and smaller teams. As such, the implementation of software severity levels and non-conformance management must use a **simplified, efficient, and resource-conscious approach** while still meeting NASA’s software quality requirements. Below is a tailored guide for small projects to define and implement software severity levels, enabling effective prioritization of issues without excessive overhead.

---

### **1. Simplify Severity Level Structure**

For small projects, it is recommended to use a **minimal number of severity levels** to reduce complexity while still categorizing non-conformances adequately.

#### **Recommended Severity Levels:**

Use three to four severity levels:

1. **Critical (High):** Issues that must be resolved immediately to ensure mission success.

   * Example: Software crashes, data corruption, or safety-critical failures.
   * **Action:** Assign top priority and address immediately.
2. **Major (Medium-High):** Issues that significantly impact system functionality but have a temporary workaround or limited impact.

   * Example: Reduced performance, intermittent failures.
   * **Action:** Work on these as resources allow but address within a defined timeframe.
3. **Minor (Low):** Issues with minimal or no impact on the system’s core functionality or objectives.

   * Example: Cosmetic defects, formatting issues, minor discrepancies in reports.
   * **Action:** Fix when time and resources are available.
4. **Editorial/Trivial (Optional):** Very low-impact issues that do not require immediate attention or may be ignored.

   * Example: Typos or minor spelling/grammar issues in documentation or logs.

#### **Benefits for Small Projects:**

* Simplifies prioritization during development and testing.
* Reduces the burden of meticulous tracking while ensuring critical issues get addressed.
* Allows the team to focus on delivering functioning systems on time and within the available resources.

---

### **2. Leverage Existing Tools and Processes**

Small projects often have limited access to large-scale tools and platforms for defect tracking. However, effective severity level implementation can still be achieved using lightweight or free tools.

#### **Recommended Tools:**

* **Simple Spreadsheets:** Use Excel, Google Sheets, or any spreadsheet application to create a defect tracking log with columns for:

  + Unique issue ID.
  + Severity level (e.g., High, Medium, Low).
  + Description of the defect.
  + Status (Open/Closed/Deferred).
  + Assigned personnel.
* **Existing Ticketing Systems (Where Available):**

  + Use software tools like **Trello, Jira, GitHub Issues, or Bugzilla** for tracking.
  + Mark severity levels as priority tags or labels (e.g., "P1" for Critical).
* **Manual Notebooks or Logs (in very small teams):**

  + Document non-conformances in a centralized physical or digital notebook. Use simple fields to record severity and resolution status.

#### **Integration with Small Project Workflows:**

For ease of use:

* Assign a single person to maintain the defect log (e.g., the project manager or a lead developer).
* Incorporate severity assignment into the regular team workflow (e.g., during daily team check-ins or test result discussions).

---

### **3. Define Severity Criteria Based on Project Needs**

Tailor the definitions for severity levels based on the small project’s specific goals and risks. For small projects, emphasize **simplified and high-impact criteria**:

#### **Key Severity Evaluation Questions:**

1. **Impact on Mission Goals:** Does the defect prevent the completion of key objectives?
2. **Impact on System Functionality:** Does the issue cause the software or system to fail or produce invalid results?
3. **Safety Risks:** Does the issue pose a risk to the safety of personnel, equipment, or the environment?
4. **Project Schedule/Budget Risks:** Will leaving the defect unresolved jeopardize the timeline or cost objectives of the project?
5. **Workarounds Available:** Can the issue be mitigated temporarily without significant resource investment?

---

### **4. Focus on Critical and Major Issues**

In small projects, the primary focus should be on addressing **Critical** and **Major** issues to ensure mission success. Minor and trivial issues can often be deferred or revisited if time permits later.

#### **Practical Tips for Prioritization:**

* Assign Critical issues top priority and set a deadline for resolution. Allocate dedicated time during team meetings to review these issues until resolved.
* Use **daily stand-ups or weekly reviews** to assess progress on Major issues.
* Defer Minor issues to a backlog or a "Wishlist" section for fixes during spare cycles, as long as they do not impact the mission.

---

### **5. Incorporate Third-Party Software Non-Conformances**

Small projects often rely on third-party software (COTS, GOTS, MOTS, OSS) and reused components to reduce development efforts. These components must still be managed for non-conformances.

#### **Steps for Managing Third-Party Software Issues:**

1. **Verify Known Issues:**

   * Check online resources or vendor websites for lists of known issues.
   * Note relevant defects that could impact your system.
2. **Assign Severity to External Defects:**

   * Assess which of the external issues apply to your system's usage and assign severity levels accordingly.
3. **Collaborate with Vendors/Contributors:**

   * Contact the vendor or open-source community to understand resolution timelines or implement workarounds if feasible.
4. **Document Risks from Unresolved Defects:**

   * Evaluate and document any risks associated with unresolved external non-conformances for project stakeholders.

---

### **6. Keep Severity Level Definitions Lightweight and Accessible**

For small teams, overly detailed documentation can be counterproductive. Define and communicate severity levels in a **simplified format** that is easy for everyone in the team to understand and apply.

#### **Example Severity Level Table for Small Projects:**

| **Severity Level** | **Definition** | **Impact** | **Action Required** |
| --- | --- | --- | --- |
| Critical (P1) | Immediate risk to mission success, system functionality, or safety. | High risk. Needs immediate attention. | Resolve within 1 week. Notify management immediately. |
| Major (P2) | Significant disruption to system operations but workaround available. | Moderate risk. Can delay mission objectives. | Resolve within 2–3 weeks. |
| Minor (P3) | Small or cosmetic issues. Does not affect core functionality. | Low risk. No immediate impact on the project. | Resolve when resources permit. |
| Trivial/Editorial | Negligible impact (e.g., spelling errors, logs formatting). | No risk. No functional or operational impact. | Resolve based on discretionary effort. |

---

### **7. Track Metrics and Use Results to Improve Processes**

For small projects, even a few metrics can help track progress and identify potential bottlenecks in defect resolution.

#### **Key Metrics to Track:**

* Total number of open non-conformances by severity.
* Time-to-resolution for Critical and Major issues.
* Count of unresolved third-party software issues.
* Trends in non-conformance discovery over time (e.g., by test phase).

---

### **8. Instill a Flexible, Team-Oriented Approach**

Small projects often operate with minimal bureaucracy and greater agility. Use this flexibility to:

* **Encourage cross-functional reviews:** In small teams, multiple members often take on overlapping roles. Ensure everyone understands severity definitions and participates in reviewing critical issues.
* **Use iterative refinement:** Revisit severity-level assignments as more information about the defect’s impact becomes known during development and testing.

---

### **Conclusion**

For small projects, implementing severity levels doesn't need to be a resource-intensive process. By focusing on simplicity, leveraging existing tools, and tailoring severity definitions to the specific needs and risks of the project, small teams can efficiently prioritize and resolve software non-conformances. This approach helps ensure mission objectives are met while maintaining compliance with NASA’s software assurance requirements.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA’s Lessons Learned database contains decades of insights from prior missions and projects, many of which provide valuable context for the importance of clearly defining and implementing severity levels for software non-conformances. Below are the most relevant lessons learned, categorized to guide the implementation of this requirement effectively.

---

### **1. The Importance of Clear Severity Definitions**

**Lesson Learned Reference**:  
LLIS-0934 – *Lack of Standardized Discrepancy Severity Definitions in Software Results in Ineffective Prioritization of Issues*

* **Summary**: Projects with poorly defined or inconsistent severity classifications failed to prioritize mission-critical software defects, resulting in last-minute updates, testing delays, and reduced operational readiness.
* **Key Insight**: Undefined or vague severity levels caused misunderstandings among team members about which defects were truly critical, leading to low-priority fixes consuming valuable resources and attention.
* **Actionable Takeaway**:
  + Establish **clear, measurable criteria** for severity levels that align with project objectives, safety standards, and mission risks.
  + Use a collaborative process to define severity levels with input from all relevant stakeholders (e.g., software, systems, and mission operations engineers).

---

### **2. Visibility and Traceability of Non-Conformance Data**

**Lesson Learned Reference**:  
LLIS-2504 – *Need for Consistent and Traceable Software Discrepancy Tracking*

* **Summary**: During a mission’s development and testing phases, disparate defect tracking methods across subcontractors led to incomplete resolution of issues. Certain critical non-conformances “fell through the cracks” because the severity levels were not consistently understood or applied.
* **Key Insight**: Lack of traceability and a clear severity-level framework made it difficult for software assurance personnel to verify that non-conformances had been adequately addressed.
* **Actionable Takeaway**:
  + Ensure that severity levels are not only well defined but also **tracked uniformly across teams** using a common repository (e.g., defect tracking tools like Jira, Bugzilla).
  + Maintain a full trace of non-conformances, linking their severity to testing results, corrective actions, and verification status.

---

### **3. Challenges with Third-Party Software (COTS, GOTS, MOTS, OSS, Reused Software)**

**Lesson Learned Reference**:  
LLIS-2215 – *Software Defect Risks Associated with COTS and Reused Software*

* **Summary**: The over-reliance on third-party software components (COTS, GOTS, OSS) without carefully reviewing their known issues severely impacted mission timelines. Known defects in reused software were not properly assessed for their impact on NASA systems, resulting in downstream failures.
* **Key Insight**: Third-party software was often treated as a "black box," leading to insufficient application of severity classifications to known defects. Consequently, risks were underestimated, resulting in mission delays and increased costs.
* **Actionable Takeaway**:
  + For third-party software components, **research published defect lists** (e.g., vendor portals) and assess each known issue for its severity relative to the system’s expected use.
  + Assign internal severity levels to external software defects based on their potential impact on mission safety and functionality, as well as ensure mitigation plans are clearly documented and communicated.

---

### **4. Risk of Skipping Low-Severity Issues That Cause Cumulative Failures**

**Lesson Learned Reference**:  
LLIS-1669 – *Accumulation of Minor Software Issues Leading to Major Failures*

* **Summary**: A major failure in a NASA ground system was traced to an accumulation of deferred minor issues. The organization overlooked the aggregate impact of these low-severity non-conformances, some of which compounded into system malfunctions during operations.
* **Key Insight**: Even low-priority software issues can lead to mission-impacting failures if left unresolved, especially when multiple small issues interact with one another.
* **Actionable Takeaway**:
  + When assigning severity levels, include **periodic reviews of deferred or low-priority issues** to evaluate their cumulative risk.
  + Monitor ongoing trends in low-severity non-conformances to identify recurring patterns or underlying systemic issues.

---

### **5. Safety-Critical Systems Require a Rigorous Focus on High-Severity Issues**

**Lesson Learned Reference**:  
LLIS-3092 – *Failure to Expedite Resolution of Critical Software Issues in Safety-Critical Systems*

* **Summary**: An incident during testing revealed that high-severity issues in a safety-critical system were not resolved in a timely manner due to a lack of clear priority-setting guidelines. Risk mitigation efforts were ineffective because the severity assignment process did not adequately account for human safety risks.
* **Key Insight**: Severity levels must be defined to include specific criteria for identifying and expediting issues in safety-critical systems, such as human-rated systems or environmental control.
* **Actionable Takeaway**:
  + Explicitly define severity levels for safety risks (e.g., "Critical – Safety Impact") to ensure these issues are elevated and resolved on a priority basis.
  + Dedicate a safety engineer or an experienced risk manager to oversee the classification of non-conformances in safety-critical systems.

---

### **6. Importance of Tailoring Severity Definitions to the Mission Context**

**Lesson Learned Reference**:  
LLIS-1850 – *Misclassification of Software Issues Due to Misaligned Severity Definitions*

* **Summary**: Generic severity level definitions did not account for project-specific mission risks (e.g., science errors for data collection systems or timing issues in autonomous systems), leading to misclassification of defects and suboptimal resource allocation.
* **Key Insight**: Severity classifications that are not tailored to the mission context can lead to improper prioritization of defects and, in some cases, missed science opportunities or reduced system performance.
* **Actionable Takeaway**:
  + Customize severity level definitions for the project, with specific consideration of mission-critical objectives such as:
    - Science data integrity.
    - Timing precision for autonomous systems.
    - Reliability of communication subsystems.
  + Ensure that **stakeholders from system engineering, software development, and mission operations** participate in defining severity levels.

---

### **7. Lessons on Simplicity and Efficiency for Small Projects**

**Lesson Learned Reference**:  
LLIS-1543 – *Excessive Complexity in Defect Management Overburdened Smaller Projects*

* **Summary**: A small NASA project struggled with non-conformance tracking due to an overly complex system of severity levels and defect reporting, which consumed significant resources without corresponding benefits for the mission.
* **Key Insight**: Small projects benefit from simpler, more focused severity level frameworks to prevent overhead while still addressing critical issues effectively.
* **Actionable Takeaway**:
  + Use **three to four severity levels** (e.g., Critical, Major, Minor, Trivial), with clear and concise definitions.
  + Limit reporting requirements to focus only on essential metrics (e.g., number of unresolved Critical and Major issues).

---

### **Key Recommendations Derived from Lessons Learned**

1. **Collaborative Development**: Always involve a cross-functional team when defining severity levels to ensure that risk factors related to mission success, safety, and performance are captured accurately.
2. **Document and Communicate**: Formalize severity level definitions in a brief, accessible format and ensure all team members are trained to apply them consistently.
3. **Address Third-Party Risks**: Extend the severity framework to assess and track defects in COTS, GOTS, MOTS, OSS, and reused software components, as these often introduce latent risks.
4. **Monitor and Adjust Over Time**: Continuously revisit severity classifications and deferred defects to evaluate whether risks or cumulative issues need to be reclassified or reprioritized.
5. **Integrate into Existing Processes**: Use severity levels in defect tracking tools and integrate them into regular workflows, audits, and reviews.

---

### **Conclusion**

The lessons learned from previous NASA projects highlight the critical importance of tailoring and implementing severity levels for software non-conformances. By addressing these lessons proactively, project managers can ensure efficient prioritization of issues, reduce project risks, and maintain compliance with NASA’s software assurance standards.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-202 - Software Severity Levels**

5.5.2 The project manager shall define and implement clear software severity levels for all software non-conformances (including tools, COTS, GOTS, MOTS, OSS, reused software components, and applicable ground systems).

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that all software non-conformances severity levels are defined.

2. Assess the application and accuracy of the defined severity levels to software non-conformances.

3. Confirm that the project assigns severity levels to non-conformances associated with tools, COTS, GOTS, MOTS, OSS, and reused software components.

4. Maintain or access the number of software non-conformances at each severity level for each software configuration item.

## 7.2 Software Assurance Products

This improved software assurance (SA) guidance clarifies the role of software assurance in verifying and monitoring compliance with severity level definitions, tracking non-conformance resolution, and ensuring quality and safety in software systems. By using a streamlined, proactive approach, software assurance can provide the necessary oversight to ensure non-conformances are accurately classified and appropriately managed throughout the software development lifecycle.

#### **Essential Responsibilities and Documentation:**

Software assurance must verify that severity levels for non-conformances are defined, applied, and monitored in compliance with project-specific and NASA standards. Below are the key products and specific SA-related tasks that support this requirement.

**1. Accuracy Assessment of Severity Level Assignments to Non-conformances:**  
SA should assess whether severity levels are assigned correctly to each discovered software non-conformance.

* Ensure severity levels align with **project definitions** of criticality and NASA’s standard severity scale (e.g., 1 = Critical, 4/5 = Low Priority).
* Confirm non-conformance severity reflects mission risks, including safety, performance, and operational impact.
* Verify that risks from external software components (COTS, GOTS, MOTS, OSS, reused software) are appropriately assessed within the project context.

**2. Assurance of Non-Conformance Tracking Across Artifacts:**  
SA should obtain and review the following data to trace and evaluate non-conformance records:

* **Software Defect or Problem Reporting Data:** Ensure complete and accurate records of non-conformances in the defect tracking system.
* **Configuration Management Data:** Verify that discrepancies are tied to the correct software configuration items (SCI) and track lifecycle changes for each non-conformance.
* **Test Results and Discrepancy Reports:** Confirm that all non-conformances discovered during various testing levels are tied back to appropriate severity levels.
* **Audit Results from Change Management Process:** Ensure change requests address non-conformances, and defect fixes follow appropriate workflows for tracking and approval.
* **Software Control Board (SCB) Data:** Review SCB meeting documentation to monitor decisions related to high-severity non-conformances.
* **Version Description Documents (VDDs):** Check that all unresolved or deferred non-conformances are documented, with justification and associated risks captured.

## 7.3 Metrics

Metrics are critical for tracking software non-conformance trends and assessing the effectiveness of severity-level application. Below are the recommended metrics, with special emphasis on those required for all projects:

#### **Required Metrics:**

1. **Total Number of Non-Conformances Over Time (Open, Closed, # of Days Open, and Severity of Open):**

   * Measure the volume and severity of open issues to track backlog and ensure resources are appropriately allocated.
2. **Trend of Open Versus Closed Non-Conformances Over Time:**

   * Monitor the project’s ability to resolve issues in a timely manner.
3. **Number of Non-Conformances in Current Reporting Period (Open, Closed, by Severity):**

   * Allows for specific period-based analysis of productivity and risk reduction.
4. **Number of Non-Conformances Identified in Embedded COTS, GOTS, MOTS, OSS, or Reused Components vs. Number Successfully Closed:**

   * Track external software risks and measure the success of mitigation efforts.
5. **Number of Non-Conformances per Severity Level for Each Software Configuration Item:**

   * Enables detailed analysis of non-conformance distribution and identification of problematic components.

#### **Optional or Supplemental Metrics:**

* **Number of Non-Conformances Identified in Source Code Products (Open, Closed):**
  + Track specific risks introduced through custom software development.
* **Age of Open Non-Conformances:**
  + Monitor and address stagnation in resolving non-conformances, emphasizing closure of high-severity issues.

## 7.4 Guidance

The assurance of software non-conformances depends on a proactive approach that begins early in the development lifecycle and continues through testing, operation, and maintenance. Below are the refined steps for software assurance activities to meet SWE 5.5.2 effectively:

#### **1. Confirm the Existence of Defined and Documented Severity Levels:**

* Verify that severity levels for software non-conformances are **defined and documented before any testing begins.**
  + Confirm that the severity levels reflect risk categories across safety, performance, and mission-critical operations. Example: Use a 1–4 or 1–5 scale where “Critical” represents life/safety issues.
* Confirm severity level definitions are available in:
  + **Test Plans or Test Procedures:** Verify the alignment of severity guidance with planned testing activities.
  + **Discrepancy Tracking Tools:** Ensure severity levels are embedded in tools (e.g., Jira, Bugzilla). Embedded definitions aid real-time categorization.
* Verify that severity levels are used consistently for testing at **all levels**, particularly system-level testing and higher.

#### **2. Monitor Assignment of Severity Levels During Testing:**

* Witness testing sessions or review test reports to confirm all non-conformances are:
  + **Documented in the project discrepancy reporting system.**
  + Assigned severity levels in accordance with predefined severity definitions.
  + Mapped to their respective software configuration items (SCIs), ensuring traceability.
* Review the application of severity levels to ensure the **accuracy and consistency** of assignments. For example:
  + Did the assigned severity reflect the actual mission-criticality of the failure?
  + Were safety-critical issues escalated and fixed as defined in the project’s risk and resolution processes?

#### **3. Evaluate Third-Party Software Non-Conformances:**

* **Review Reused Software Issue Lists:** For COTS, GOTS, MOTS, OSS, or reused software, validate the severity assigned to known defects.
  + Confirm that reused software issues are **reassessed in the context of the project’s system.** Vendor-provided severity levels may not always align with NASA’s expectations (e.g., a "low" severity usability issue in the vendor’s context could have a higher severity if it disrupts automation or ground operations).
  + Ensure the project tracks risks associated with external software issues and mitigates appropriately.

#### **4. Monitor Metrics and Enforce Non-Conformance Closure:**

* Confirm the project is collecting the **required metrics** for open/closed non-conformances across all severity levels and software components.
  + Verify that non-conformance metrics (e.g., age, closure rates) are **regularly reviewed** by project managers and software control boards.
  + Track deferred or open non-conformances and periodically reassess their risk—**especially high-severity issues.**

#### **5. Ensure Alignment Across Configuration Items:**

* Conduct focused assessments to ensure each software configuration item (SCI) has an accurate non-conformance log, including:
  + Severity level for each non-conformance.
  + Resolution status (e.g., “Open,” “Fixed,” or “Deferred”).
  + Rationale for any unresolved non-conformances (especially for Critical or Major issues).

---

### **SA Tasking for SWE 5.5.2**

To support compliance, SA should focus on:

* **Accuracy of Severity Assignments:** Confirm severity levels are defined, applied, and reassessed as needed.
* **Complete Traceability:** Ensure all non-conformances are documented and tied to software work products.
* **Proactive Monitoring of Metrics:** Use metrics to identify risks, ensure timely corrective actions, and align tracking across severity levels.
* **Vendor/Third-Party Assessment:** Validate third-party software issue classifications in the context of NASA’s mission.

---

### **Conclusion**

Effective software assurance for SWE 5.5.2 requires continuous oversight of severity level definitions, assignment accuracy, non-conformance tracking, and metric monitoring. By proactively verifying these elements, Software Assurance ensures risks are effectively managed, defects are prioritized consistently, and high-quality, safe software is delivered for NASA missions. Lessons learned from previous projects should also guide and refine ongoing assurance efforts.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

The objective evidence serves as documentation that demonstrates compliance with SWE Requirement 5.5.2. It verifies that severity levels for software non-conformances are clearly defined, systematically applied, tracked, and monitored throughout the software's lifecycle. Below is a breakdown of potential objective evidence that meets this requirement:

---

### **1. Evidence of Defined and Documented Severity Levels**

#### **a. Severity Definitions Document**

* Document describing severity levels (e.g., “Critical,” “High,” “Medium,” “Low,” and "Trivial") and their associated criteria (e.g., impact on mission objectives, safety, and system functionality).
* Example Elements:
  + Severity definitions tailored to project needs.
  + Definitions documented in applicable project documents such as:
    - **Project/Software Management Plan** (PMP/SMP).
    - **Risk Management Plan (RMP)**.
    - **Software Assurance Plan (SAP)**.
    - **Test Plans/Test Procedures** detailing how severity levels apply to discrepancies identified during testing.

#### **b. Embedded Severity Levels in Defect Tracking Systems**

* Configuration of discrepancy reporting or defect tracking tools (e.g., Jira, Bugzilla, GitHub Issues) with built-in severity levels available for selection.
* Evidence includes:
  + Screenshots or configuration settings demonstrating inclusion of severity categories.
  + Exported reports/logs showing non-conformances categorized by severity.

#### **c. Severity Definitions in Reused/Third-Party Software Context**

* Documented assessments of vendor-provided severity levels for COTS, GOTS, MOTS, OSS, or reused components, showing alignment with project-specific criteria.
* Evidence could include:
  + Cross-reference documents showing adjustments to vendor-provided severity levels based on the project's mission context.
  + Risk analysis documents that re-evaluate severity based on the operational environment.

---

### **2. Evidence of Severity Level Usage and Correct Assignment**

#### **a. Defect/Non-Conformance Reports**

* Individual or aggregated defect reports showing that severity levels were assigned to all identified software non-conformances during testing, integration, or operations.
* Evidence includes:
  + Detailed logs from the defect tracking system, showing severity levels assigned to open and closed defects.
  + Test-level discrepancy reports listing the failures, their assigned severity, and their resolution status.

#### **b. Test Reports and Discrepancy Logs**

* Test reports (e.g., Unit Test Report, Integration Test Report, System Test Report) that include:
  + All discrepancies or failures.
  + Their assigned severity levels, justification for the severity categorization, and corrective actions.
* Evidence may also include:
  + Post-test review records showing discussions and agreement on severity classifications.

#### **c. Software Assurance Review Records**

* Records of software assurance (SA) reviews verifying the correct application of severity levels as per project guidelines.
* Evidence Examples:
  + SA review checklists, audit logs, or findings showing confirmation (or corrections) of severity classifications.
  + SA assessment reports on third-party software severity classification alignment (COTS, OSS, etc.).

---

### **3. Evidence of Metrics Tracking Non-Conformance Resolution**

#### **a. Non-Conformance Tracking and Metrics Reports**

* Reports showing the metrics required by the project for non-conformance tracking, including:
  + Total number of non-conformances (e.g., Open, Closed, Severity, Age).
  + Trends of Open vs. Closed non-conformances over time.
  + The number of non-conformances at each severity level for each software configuration item (SCI).
  + COTS, GOTS, OSS, MOTS metrics:
    - Non-conformances identified in these components.
    - Total resolved/closed versus open issues.
* Tools like Excel spreadsheets, Jira reports, or otherwise exportable trend analysis charts for non-conformance metrics.

#### **b. Milestone Reports Incorporating Non-Conformance Data**

* Evidence that non-conformance closure and severity allocations were part of milestone reviews, such as:
  + Preliminary Design Review (PDR) packages.
  + Critical Design Review (CDR) presentations/reports.
  + Test Readiness Review (TRR) results identifying open critical issues and their impact on flight readiness.

#### **c. Dashboard Visualizations (Optional Evidence)**

* Generated dashboards or visualizations used to track:
  + The number and distribution of open/closed non-conformances over time, organized by severity level.
  + Resolution closure rates categorized by severity and SCI.

---

### **4. Evidence from Change Management and Configuration Control**

#### **a. Software Configuration Management Records**

* Records showing that configuration items (CIs) where non-conformances were recorded and fixed are documented, including:
  + Version Description Documents (VDDs) listing open or deferred non-conformances and rationale for severity levels.
  + Change Requests (CRs) or Problem Reports (PRs) for non-conformances tied to specific software releases and aligned with identified severity levels.

#### **b. Software Control Board (SCB) Meeting Records**

* SCB minutes or decisions documenting:
  + Discussions of high-severity (Critical/High) non-conformances.
  + Decisions for prioritization, resolution timelines, or deferral, including rationale.
  + Evidence of mitigation strategies for deferred issues, especially high-severity ones.

#### **c. Audit and Inspection Logs for the Change Management Process**

* Results from software assurance or third-party audits evaluating whether:
  + The change management process adheres to severity level handling criteria.
  + Non-conformances assigned the "Critical" level are treated with the highest priority and resolved appropriately.

---

### **5. Evidence from Third-Party/External Software Assurance**

#### **a. Vendor Non-Conformance Lists**

* Vendor-provided defect lists (COTS, OSS, MOTS, or GOTS components) reviewed and annotated to align with the project context.
* Evidence includes:
  + Risk assessments of unresolved third-party software issues.
  + Documentation showing the reclassification of vendor severity to project-specific severity levels.

---

### **6. Lessons Learned Documentation**

* Evidence that review and refinement of severity levels were informed by lessons learned (e.g., NASA LLIS lessons or post-mission reviews).
* Documentation showing how lessons learned influenced:
  + Revised severity definitions.
  + Process improvements for severity reassessment during testing or operations.

---

### **7. Software Assurance Reports and Reviews**

* Comprehensive SA reports documenting oversight activities related to severity levels, such as:
  + Audit findings regarding severity classifications and resolutions.
  + Recommendations made to change severity assignments where misalignments were identified.
  + Summaries of SA participation in defect-tracking reviews or SCB meetings.

---

### **Key Notes on Objective Evidence Quality:**

* **Completeness:** All assigned severity levels should be justified with clear rationale tied to project definitions.
* **Traceability:** Evidence must link severity levels to specific software items, configuration items (CIs), and resolutions.
* **Timeliness:** Evidence should demonstrate continuous monitoring—testing/reporting metrics should be up-to-date during audits/milestones.
* **Context-Specific:** Severity level definitions and applications should align with mission-specific risks and criticality (not generic).

---

### **Objective Evidence Checklist Summary:**

| **Category** | **Evidence Type** |
| --- | --- |
| Definitions and Documentation | Severity definitions, test plans, discrepancy tool configurations |
| Severity Application Accuracy | Test reports, discrepancy logs, SA review checklists, external vendor assessments |
| Metrics for Tracking Non-Conformance | Open/closed trends, severity-specific resolutions, milestone reports |
| Configuration and Change Control | SCM records, SCB minutes, VDDs, risk mitigation for unresolved critical issues |
| Third-Party Software Compliance | COTS/OSS defect lists with re-assessed severity, risk analysis for reuse components |
| Oversight and Lessons Learned | SA reports, audit findings, application of lessons learned, closure rate efficiency improvements over milestones. |

---

Meeting SWE Requirement 5.5.2 through well-documented, traceable, and comprehensive objective evidence helps ensure severity levels allow for effective prioritization, resolution, and risk mitigation across the entirety of the software lifecycle.

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
