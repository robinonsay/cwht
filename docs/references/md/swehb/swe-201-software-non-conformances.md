# SWE-201 - Software Non-Conformances

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695535. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances

SWE-201 - Software Non-Conformances

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695535)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695535&showCommentArea=true&showComments=true#addcomment)

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

5.5.1 The project manager shall track and maintain software non-conformances (including defects in tools and appropriate ground software). 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-201 History

SWE-201 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW Replaces [SWE-069](/spaces/SITE/pages/81691111/SWE-069+History) |
| C | 5.5.1 The project manager shall track and maintain software non-conformances (including defects in tools and appropriate ground software). |
| Difference between C and D | No change |
| D | 5.5.1 The project manager shall track and maintain software non-conformances (including defects in tools and appropriate ground software). |

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

To make sure that all software non-conformances are addressed. Managing and tracking non-conformances, software problem reports, or software issues are critical steps to ensuring that software defects are flagged and handled properly.

The rationale behind tracking and maintaining software non-conformances (including defects) is to ensure software quality, reliability, and mission success. Properly identifying, tracking, and managing non-conformances allows the project manager and engineering team to evaluate and address software deficiencies systematically, preventing unresolved issues from propagating through the software lifecycle and affecting mission outcomes.

Since defects or non-conformances in software tools, ground systems, and flight software can affect both operational performance and mission safety, this requirement emphasizes rigorous accountability for identifying and resolving these issues.

---

### **Key Reasons for the Requirement:**

#### **1. Ensuring Mission Success**

Non-conformances in software can lead to catastrophic effects during mission-critical operations. Undetected or unresolved defects—whether in flight software, ground software, or tools used during development—can cascade to system-level failures, jeopardizing both the mission and its objectives. Tracking and resolving these non-conformances:

* Reduces the likelihood of defects escaping into later stages of design, testing, or operations.
* Minimizes the potential for mission abort scenarios caused by software malfunctions.
* Ensures that the software reliably performs its intended function throughout all mission phases.

---

#### **2. Managing and Reducing Risk**

This requirement directly addresses software risks by enabling proactive identification and resolution of software anomalies or deviations from expected behaviors. By continuously tracking software non-conformances, the project improves situational awareness of potential risks, such as:

* Safety risks for crewed or autonomous missions.
* Performance risks leading to degraded objectives or operational delays.
* Financial risks stemming from rework costs, contract penalties, or schedule overruns.

By maintaining a comprehensive list of software non-conformances, project managers ensure that risks associated with unresolved or ignored software defects are minimized.

---

#### **3. Supporting Continuous Improvement**

Tracking non-conformances provides a historical record of software development challenges, enabling teams to learn and improve processes. This record acts as a repository for:

* Root cause analysis: Identifying why defects occurred in the first place to avoid repetitive errors.
* Lessons learned: Informing future projects or software iterations about common pitfalls encountered during development.
* Statistical analysis: Providing metrics to evaluate the effectiveness of testing, the number of defects over time, and areas most susceptible to errors (e.g., interfaces, algorithms, requirements).

These insights not only improve the current project but also contribute to better software engineering practices within NASA’s institutional knowledge base.

---

#### **4. Ensuring Visibility and Accountability**

This requirement ensures transparency and accountability by mandating that all software non-conformances are tracked in a systematic and auditable manner. This has several benefits:

* Visibility: Provides stakeholders, including project managers and software assurance teams, with a clear picture of software quality and progress in resolving issues.
* Collaboration: Encourages team alignment between developers, testers, and project stakeholders for prioritizing and resolving non-conformances.
* Accountability: Assigning responsibility to address non-conformances ensures they are not overlooked and remain visible until resolution.

---

#### **5. Enabling Effective Decision-Making**

When all non-conformances are tracked and maintained, the project manager has the data needed to make informed decisions:

* Which non-conformances need to be resolved immediately due to their mission-critical nature?
* Which issues carry less priority and can be deferred to a maintenance release (post-deployment)?
* What additional resources (time, budget, personnel) are required to address a backlog of non-conformances?

In the absence of systematic tracking, informed resource allocation and effective decision-making become challenging, leading to delays and higher costs.

---

#### **6. Managing Tool and Ground Software Defects**

This requirement explicitly includes defects in **development tools** (e.g., compilers, integrated development environments) and **ground systems software** used to support testing and operations. These components are critical for:

* Verifying the correctness of mission software.
* Ensuring operational readiness (e.g., command-and-control systems, simulation environments).

Defects in these supporting systems can compromise the integrity of the software lifecycle:

* A faulty configuration management tool could corrupt source code or version histories.
* An error in ground control software might result in missed telemetry data or misinterpreted commands.
* Bugs in simulation tools could lead to false validation and undetected issues in operational software.

Ensuring that these components are error-free helps maintain the integrity of the development and operational workflows.

---

#### **7. Compliance with NASA Standards and Best Practices**

Tracking non-conformances aligns with NASA’s overarching focus on reliability, safety, and quality assurance as outlined in the NASA Software Engineering Handbook. In particular:

* **Non-conformance tracking** feeds directly into defect prevention, a core principle in software quality assurance (SQA).
* Adherence to this practice ensures compliance with other NASA requirements for accountability, including:
  + **SWE-079**: Software Change Request Management.
  + **SWE-098**: Defect Metrics Reporting.
  + **SWE-052**: Traceability between requirements, design, and non-conformance reports.

This systematic approach reinforces NASA’s commitment to highly reliable, rigorously validated software systems.

---

### **Consequences of Non-Compliance**

Failure to track and maintain non-conformances consistently can result in:

1. **Undetected Defects Escaping Through the Lifecycle:**

   * Without tracking, defects may go unresolved, leading to rework, delays, or even mission failure.
   * Late detection of defects increases the cost of resolution exponentially (e.g., defects discovered during operations are far more costly to fix than in development).
2. **Reduced Stakeholder Confidence:**

   * Lack of visibility into non-conformance management reduces trust between the development team, software assurance, and mission stakeholders.
3. **Increased Risk of System Failure:**

   * Overlooking software defects—whether in mission-critical software or supporting systems—can lead to catastrophic failures such as data loss, misdirected commands, or safety violations in launched systems.

---

### **Benefits of Compliance**

1. **High Quality Software:**

   * Leads to software systems that meet all functional, operational, and safety requirements.
2. **Reduced Rework Costs:**

   * Early identification of defects reduces the cost and time required for defect resolution.
3. **Improved Efficiency and Collaboration:**

   * Clear, auditable processes for tracking defects streamline communication between developers, testers, and project leadership.
4. **Enhanced Process Maturity:**

   * Systematic tracking and maintenance of non-conformances contribute to continuous improvement, reducing errors in both current and future projects.

---

### **Conclusion**

This requirement emphasizes the importance of a proactive, systematic approach to managing software non-conformances and defects as they arise throughout the project lifecycle. By ensuring full visibility, traceability, and accountability, project managers can mitigate risks, ensure software quality, and achieve mission objectives efficiently and safely. This is particularly critical for NASA's mission environment, where system reliability and operational excellence are non-negotiable.

# 3. Guidance

## 3.1 Definition of Non-Conformance

A **software non-conformance** is any deviation between the documented plans, specifications, or intended functionality and the actual behavior or characteristics of the software product, either during development or after delivery. Non-conformance occurs when the delivered software fails to meet the project requirements or specifications. This may include:

* Functional errors (e.g., unintended behavior that is inconsistent with requirements).
* Violations of design constraints or standards.
* Discrepancies between the software’s documented functionality and observed operation.
* Defects caused by design flaws, coding errors, configuration issues, or unanticipated operational environments.

Even with robust development processes, software testing, and validation strategies, some non-conformances can persist post-delivery due to the inherent complexity of software systems.

Examples of software non-conformances include:

* Runtime exceptions or crashes during system operation.
* Incorrect calculations or system behaviors.
* Documentation that does not reflect the implemented functionality.
* Unanticipated behavior when interfacing with hardware or external systems.

**Why Non-Conformance Management is Important:**  
Properly defining, identifying, and managing software non-conformance is critical for ensuring:

1. Mission readiness and safety are not compromised.
2. The software system remains functional and reliable across its lifecycle.
3. Future teams can reuse the software effectively while addressing any constraints and limitations.

## 3.2 Records of Non-Conformances

Maintaining detailed records of software non-conformances is vital to ensure **data transparency**, **traceability**, and **continuous improvement** throughout the software lifecycle. This is especially important in the context of future reuse, upgrades, or anomaly investigations.

Non-conformance records allow teams to:

1. **Guide Reuse and Planning for Upgrades:**

   * Engineers reusing existing software products must evaluate the software’s constraints, limitations, and any behavior inconsistent with project objectives.
   * Documentation describing known issues, associated operational constraints, or workarounds ensures informed deployment decisions.
2. **Analyze Software Reliability:**

   * Non-conformance records provide insight into overall software quality and any systemic issues within software components.
   * By tracking and analyzing non-conformances, teams can identify subsystems or modules with excessive defects and focus on improvement in those areas.
3. **Enable Root Cause Analysis and Knowledge Sharing:**

   * Documentation of non-conformance records supports the identification of areas needing process improvement.
   * Historical records of non-conformance issues help educate current and future teams, fostering institutional learning.

---

**Suggested Information for Non-Conformance Records:**  
A robust and well-documented non-conformance tracking system should include the following key data points:

1. **Date of Discovery:** When the non-conformance was identified.
2. **Discovery Context:** How and under what conditions the non-conformance was discovered (e.g., during testing, operations, or user feedback).
3. **Severity of Non-Conformance:**
   * Align severity levels with NASA standards (Refer to SWE-202 - Software Severity Levels).
   * Categorize defects (e.g., critical, high, moderate, low) based on their impact on mission objectives, safety, and system operations.
4. **Configuration Information:**
   * Specific software version where the defect occurred.
   * Versions of tools and libraries used.
   * Document revision numbers tied to the identified non-conformance.
5. **Impact Scope and Associated Systems:** Trace the components or subsystems impacted by the non-conformance.
6. **Contact Information:** Point of contact for engineers or team members responsible for investigating or resolving the issue.
7. **Supporting Evidence:** Links to logs, screenshots, test reports, or incident data that illustrate the problem.
8. **Status of the Issue:** Track whether the defect is open, in analysis, under resolution, or closed.
9. **Mitigation or Workarounds:** Document any operational or procedural workarounds implemented to address the non-conformance temporarily.

**Additional Records:**

* **Linkage to Change Requests:** Corresponding software change requests (CR) or problem reports (PR) that account for corrections or enhancements related to the non-conformance.
* **Approval Decisions:** Capturing decisions deliberated by Configuration Control Boards (CCBs) regarding defect prioritization and impact mitigation.

---

**Accessibility of Non-Conformance Data:**

* Store non-conformance data in **centralized and traceable databases** or tools (such as Jira, IBM DOORS, or custom change management tools).
* Ensure current and future software teams can access these records, especially for systems intended for reuse or long-term maintenance (20+ year lifecycle for some NASA systems).
* Use tagging, version control, or metadata indexing to enable efficient retrieval of non-conformance tracking data.

> **Reference:** See also **Topic 5.01 - CR-PR (Software Change Request/Problem Report)** for further details on how to manage and process defect reporting.

## 3.3 Tracking and Analysis of Non-Conformance

Tracking and analyzing non-conformance data is a **best practice** that addresses the following key objectives:

1. **Root Cause Identification:** (Refer to SWE-204 - Process Assessments)

   * Understand the fundamental issues that caused the non-conformance to prevent reoccurrence.
   * Perform root cause analysis for high-severity or recurring defects to identify:
     + Whether defects stemmed from unclear requirements, coding errors, or environmental/test conditions.
     + Weaknesses in team processes or development tooling.
2. **Systematic Monitoring of Trends:**

   * Monitor the frequency, distribution, and types of non-conformances over time.
   * Identify **patterns or systemic issues** to determine if certain projects, modules, or tools contribute disproportionately to software quality challenges.
   * Use trend data to inform process optimization initiatives, particularly in defect-prone areas (e.g., interfaces, reusable components).
3. **Verification and Retesting:**

   * Ensure all overlapping or interdependent non-conformance issues are closed only after thorough retesting.
   * Validate that defect fixes do not introduce secondary issues (e.g., regression).
   * Establish clear linkage between test cases and resolved non-conformance records to ensure all unique test scopes are covered.
4. **Change Control and Auditability:**

   * Document any updates to artifacts impacted by non-conformances (e.g., requirements, design documentation, test plans) and submit them for re-approval if necessary.
   * Ensure Configuration Control Boards (CCBs) review and re-approve all decisions where modifications to scope or impact have occurred.

---

**Best Practices for Tracking and Analysis:**

1. **Use Comprehensive Tracking Tools:**

   * Use software change tracking tools (e.g., Jira, Bugzilla, IBM Engineering Workflow Management) to manage non-conformance records with proper workflow configurations (status changes, categorization, and severity tagging).
   * Track dependencies between changes and ensure traceability to ensure integrity across software artifacts.
2. **Automate Reporting and Analysis:**

   * Automate metric collection to generate insights into defect density, resolution cycles, and defect closure rates.
   * Use automated tools to cross-check for duplicate tickets and prevent redundant issue closure.
3. **Regular Review Process:**

   * Review non-conformance records and trends periodically (e.g., bi-weekly or monthly) to detect risks early.
   * Align reviews with major project milestones (e.g., SRR, PDR, CDR, TRR).
4. **Ensure Retest Completeness:**

   * Before closing non-conformance tickets, verify that the **full scope** of test cases tied to the defect has been re-executed. Missing test or retest cases could cause residual issues to persist undetected.
   * Avoid premature closure of issues due to overlapping or cross-cutting changes without ensuring that unique aspects of the defects are addressed.
5. **Adhere to NASA Process Standards:**

   * Refer to SWE-204 for process assessments and SWE-202 for severity classification to validate and prioritize non-conformances consistently.

This guidance emphasizes the importance of defining, documenting, and analyzing non-conformances to ensure continuous improvement, minimize defect severity in future missions, and maintain software system integrity over its operational lifetime. A structured process to track, manage, and analyze non-conformances addresses not only immediate project risks but also provides long-term benefits in system reliability, reusability, and maintainability.

See also Topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report),

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [SWE-204 - Process Assessments](/spaces/SWEHBVD/pages/102695538/SWE-204+-+Process+Assessments)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Monitoring and Control](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Monitoring+and+Control)      * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

Managing software non-conformances is critical for all projects, regardless of size. While smaller projects may have fewer resources, a streamlined and lightweight approach can ensure compliance with this requirement without sacrificing software quality or risking project outcomes. Below is tailored guidance for small projects to help meet this requirement efficiently.

---

### **1. Definition of Non-Conformance for Small Projects**

On small projects, software non-conformances can include:

* Mismatches between the software behavior and the documented requirements.
* Defects in the functionality of tools used during development or testing.
* Configuration issues (e.g., incorrect versioning or setup of libraries/frameworks).

**Key Considerations for Small Projects:**

* Focus on **critical defects**—those that have a tangible impact on safety, performance, or functionality.
* Document even minor issues (e.g., operational anomalies or mismatched documentation) to provide a complete historical record for future reuse or upgrades.

---

### **2. Simplified Record-Keeping**

Small projects can use simplified tools and processes for tracking non-conformances. A full-scale defect tracking system may not be practical, so small teams can select lightweight alternatives.

#### **Tools for Small Projects:**

* **Spreadsheet-Based Tracking**:  
  Use tools like Microsoft Excel, Google Sheets, or similar to log and manage non-conformances. Include fields for:

  + Date discovered.
  + Description of the issue.
  + Severity level (e.g., low, medium, high, critical).
  + Responsible team member for resolution.
  + Status (open, in progress, resolved, verified).
  + Notes on resolution steps or workarounds.

  **Example Template:**

  | **ID** | **Date** | **Description** | **Severity** | **Assigned To** | **Status** | **Resolution Notes** |
  | --- | --- | --- | --- | --- | --- | --- |
  | 001 | 2023-11-01 | Interface timeout in function X | High | Jane Smith | In Progress | Reviewing input validation code. |
  | 002 | 2023-11-02 | Documentation mismatch in API | Low | John Doe | Resolved | Updated API manual to correct outputs. |
* **Issue Tracking Software:**  
  Use free or low-cost tools like Trello, Asana, or open-source issue-tracking platforms like Trac, Redmine, or GitLab. These tools can provide automated workflows while being lightweight enough for small teams.
* **Bug-Tracking in Version Control Systems**:  
  Utilize comments and tags in systems like Git. For example, log non-conformances using annotated commits or issue trackers within GitHub/GitLab.

---

### **3. Streamlined Processes for Tracking and Analysis**

Small projects can use the following simplified practices for tracking and analyzing non-conformances:

* **Prioritization of Issues:**  
  Focus resources on resolving **critical** and **high-severity** non-conformances that impact functionality, safety, or performance. Minor issues can be addressed in subsequent iterations or maintenance updates.

**Small-Scale Prioritization Example:**

* **Critical:** Bugs that prevent core functionality or threaten mission success (must fix immediately).
* **High:** Defects that affect major operations but have workarounds available (fix before delivery).
* **Moderate/Low:** Cosmetic or non-critical issues (deferred to post-delivery or future updates).

---

### **4. Communication and Accountability**

With smaller teams, clear roles and communication are critical to ensure non-conformances are resolved efficiently.

* Assign a **single point of contact** (such as the project manager or lead developer) to oversee non-conformance tracking and ensure status updates are documented.
* Discuss open non-conformances during weekly or bi-weekly team meetings to maintain team awareness.

---

### **5. Simplified Root Cause Analysis**

For small projects, performing a detailed root cause analysis for every issue may not be feasible. Instead:

* **Focus on Recurring Issues or High-Severity Problems:**  
  If the same type of defect appears frequently, investigate its origin (e.g., flawed requirements, repeated coding errors) to prevent future occurrences.
* Use a simple "5 Whys" approach to identify root causes for critical non-conformances.

**Example:**

* **Problem:** Function X creates a timeout.
  + Why? Invalid inputs cause an infinite loop.
  + Why? Input validation was missing in function X.
  + Why? Requirements for function X did not include input validation specifications.
  + Solution: Add input validation requirements and update coding standards.

---

### **6. Configuration Control for Small Projects**

Small projects must still maintain **configuration management discipline** to track software versions, tool versions, and related documentation.

* Establish a simple **version history log** that records:
  + Software version number.
  + Tool versions (compilers, libraries, etc.).
  + Environment or configuration details for each delivered build.
* Use Git (or similar) for branch management to differentiate production, development, and test versions of the software.

---

### **7. Non-Conformance Data Accessibility**

Ensure that non-conformance records are maintained and accessible to team members and stakeholders. This is crucial for:

1. **Future Upgrades or Maintenance:** Even if the project is handed off to another organization, clear records of defects and resolutions ensure continuity.
2. **Software Reuse:** NASA projects often reuse software; having a record of non-conformances ensures that reusable components are well-understood.

**Storage Options for Small Projects:**

* Use project file repositories (e.g., SharePoint, OneDrive, or Google Drive) to centralize non-conformance records and logs.
* Store non-conformance data alongside related documentation in version-controlled environments, like GitHub/GitLab repositories.

---

### **8. Leveraging Lessons Learned**

Even small projects can gain valuable insights from tracking non-conformances:

* At project closeout, review all recorded defects and their resolutions.
* Document recurring issues and any process improvements implemented during the project.
* Incorporate lessons learned into future projects to avoid similar issues.

**Example Lessons Learned Summary:**

* Common Defects: High rate of interface mismatches due to incomplete requirements.
* Action Plan: Improved requirements review process to clarify all input/output expectations before development.
* Tool Issues: Outdated debugging tool caused delays; standardized tools for future projects.

---

### **9. Suggested Minimal Effort Workflow for Small Projects**

**Step 1: During Development and Testing**

* Assign responsibility for recording all software non-conformances (e.g., defects identified during testing).
* Log each issue's details (minimal data fields: description, date, severity).
* Classify defects as **critical**, **high**, or **moderate/low** severity.

**Step 2: During Retests or Fixes**

* Verify all fixes and update status in the tracking tool. Use a **test checklist** for simpler verification instead of full formal test procedures if team resources are limited.

**Step 3: During Delivery/Closeout**

* Deliver the final software build with a concise **defect report summary**, highlighting:
  + Remaining known issues (if any).
  + Resolutions and workarounds implemented during the project lifecycle.
  + Any restrictions on reuse due to unresolved non-conformances.

---

### **10. Key Resource Recommendations for Small Projects**

* **SWE-202:** Use severity level guidance to evaluate defect criticality.
* **SWE-204:** Refer to root cause analysis recommendations for major or recurring issues.
* Tools: Jira (free tier), Google Sheets, GitHub Projects, Trello, or any lightweight bug-tracking framework tailored to your team's size.

---

### **Key Takeaway**

Small projects should focus on lightweight, efficient, and low-cost processes to track and resolve non-conformances. By tailoring non-conformance management, small teams can maintain software quality and comply with NASA requirements while avoiding unnecessary overhead. With appropriate prioritization, streamlined documentation, and good communication, small projects can achieve strong outcomes with limited resources.

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

The requirement to systematically track and maintain software non-conformances, including those in development tools and ground software, is supported by a history of lessons learned from NASA's missions and projects. These lessons highlight the importance of thorough defect tracking, robust documentation, and accountability to ensure software quality, mitigate risks, and improve future project outcomes. Below are specific lessons learned from NASA’s archives that directly relate to this requirement.

---

### **Key Lessons Learned from NASA Projects**

#### **1. Failure to Track and Resolve Non-Conformances Can Lead to Mission-Critical Failures**

* **Case Study: Mars Climate Orbiter (1999)**
  + **Issue:** A critical navigation error occurred due to a software defect in the data conversion process (imperial-to-metric units mismatch). Developers overlooked this error because non-conformances in ground tools and software were not tracked or resolved appropriately.
  + **Impact:** The orbiter was lost during its attempt to enter Mars’ atmosphere, leading to mission failure and a loss of $125 million in mission costs.
  + **Lesson Learned:** Ensure **rigorous tracking and resolution of all non-conformances** in both mission-critical software and supporting tools. Trace defects back to their root cause, document lessons learned, and enforce accountability for quality assurance.

---

#### **2. Comprehensive Non-Conformance Records Drive System Reliability**

* **Case Study: Space Shuttle Program**
  + **Issue:** Over the course of the Space Shuttle program, unresolved non-conformances in ground control systems periodically influenced delays in mission readiness. These issues highlighted the importance of clearly documenting and addressing non-conformances.
  + **Impact:** Overly complex non-conformance management practices often prevented effective prioritization of critical issues, resulting in inefficiencies during preparation and testing phases.
  + **Lesson Learned:**
    - Simplify non-conformance tracking and focus resources on **critical issues** affecting mission safety or performance.
    - Maintain **comprehensive, structured records** to ensure visibility into all defects and long-term traceability.
    - Robust documentation allows for systemic improvement and reliable reuse of software across missions.

---

#### **3. Delayed Tracking of Defects Increases Costs**

* **Case Study: James Webb Space Telescope (JWST)**
  + **Issue:** During integration and testing phases, software defects in control and simulation tools were identified but not logged or resolved during the early phases of development. This delayed the detection of critical software issues into later stages, when debugging became more expensive and time-consuming.
  + **Impact:** The resolution of delayed error tracking, rework efforts, and retesting contributed to budget overrun and schedule delays for software subsystems.
  + **Lesson Learned:** Log **non-conformance records immediately upon discovery** and assign priorities quickly. Delaying defect tracking can lead to cascading costs and schedule overruns. Prompt attention to issues during early lifecycle phases minimizes long-term risks.

---

#### **4. Ensure Non-Conformance Tracking Includes Development and Testing Tools**

* **Case Study: SOHO Satellite Communications Loss (1998)**
  + **Issue:** A bug in simulation software, used to verify spacecraft operations, led to undetected conditions that in turn contributed to a communication loss with the satellite. Testing tools were not included in the formal defect tracking process, and critical issues remained unresolved.
  + **Impact:** Although communication was restored later, the spacecraft became inoperable for weeks, disrupting mission continuity.
  + **Lesson Learned:** Extend defect tracking to include **development tools, ground software, and test systems.** Failures in these systems can propagate into mission-critical software and lead to unexpected gaps in operational readiness or performance.

---

#### **5. Proper Root Cause Analysis is Essential**

* **Case Study: Mars Exploration Rover (Spirit and Opportunity, 2004)**
  + **Issue:** Early in operation, the Spirit rover encountered a software reset problem caused by insufficient file system memory. Root cause analysis revealed the issue stemmed from a design oversight during initial development but was not marked as a priority during defect tracking phases.
  + **Impact:** The Spirit rover entered a "safe mode" and required days to troubleshoot and apply a fix, delaying scientific activities.
  + **Lesson Learned:**
    - Perform proper **root cause analysis** for all non-conformances, especially during development phases.
    - Small, unresolved defects can lead to **cascading failures** or mission interruptions during operations.

---

#### **6. Non-Conformance Documentation Enables Software Reuse**

* **Case Study: International Space Station (ISS) Payload Software**
  + **Issue:** During upgrades to payload control software, the development team failed to account for prior non-conformance records, resulting in repeated errors caused by unresolved legacy issues. Some of these defects were poorly documented, making root cause diagnosis time-intensive.
  + **Impact:** Reuse of software became costly due to a lack of visibility into previously discovered issues and their resolution history.
  + **Lesson Learned:** Maintain **clear and reusable non-conformance records** to support future upgrades, reduce redundancy, and enable seamless adaptation of existing software for new missions.

---

#### **7. Inaccessible Non-Conformance Data Can Complicate Future Use**

* **Case Study: Chandra X-ray Observatory (1999–Present)**
  + **Issue:** Non-conformance data from earlier phases of the Chandra project was scattered across multiple tools and repositories, making it difficult for engineers to locate relevant defect records for future updates.
  + **Impact:** Non-conformance tracking inefficiencies led to difficulties maintaining the software decades after its launch, as gaps in historical records required additional effort to address recurring anomalies.
  + **Lesson Learned:** Centralize and **organize defect tracking data** into a unified, accessible repository. Future software maintenance and upgrades rely heavily on consistent documentation practices. Ensure that historical records are available to both current and future stakeholders.

### 8.  **Communication Failures Suppressing Software Concerns**

**Incident:**  
Software and system engineers raised concerns that were not acted upon. The culture fostered a “prove there is a problem” mentality, making it difficult to elevate software risks. No Independent Technical Authority (ITA) dissents were filed despite significant issues.

**Lesson Learned:**

* **Open Technical Channels:** Projects must maintain safe, responsive pathways for raising technical concerns, including through independent authorities.
* **Cultural Reinforcement:** Leadership must encourage early reporting and prohibit cultures that penalize raising risks.

**Implication:**  
When team members feel unheard, systemic issues go unaddressed, increasing mission risk and slowing problem resolution.

---

### **NASA-Wide Best Practices Derived from Lessons Learned**

1. **Prioritize Critical and High-Severity Issues:** Address defects that directly affect mission safety and performance as top priorities, with established workflows to resolve them promptly.
2. **Maintain Centralized Non-Conformance Records:** Use a unified defect tracking system (e.g., Jira, Git, or a centralized defect database) to log, update, and access non-conformance records for complete traceability.
3. **Include Development Tools and Test Software in Defect Tracking:** Ensure issues with compilers, simulators, and ground control systems are logged and addressed as part of the overall non-conformance tracking process.
4. **Perform Comprehensive Root Cause Analysis:** For recurring or high-priority defects, document the root cause to prevent similar issues from recurring in future projects. Use NASA standards (e.g., SWE-204) as guidance for process assessments.
5. **Improve Accessibility of Historical Data:** Standardize formats and archival practices to ensure future teams can understand defect history and incorporate it into reuse planning.
6. **Implement Lessons Learned Into Future Projects:** Build on prior non-conformance data to introduce process improvements, prevent repeating errors, and enhance quality assurance.

---

### **Related NASA Resources and References**

1. **NASA Lessons Learned Database:**

   * Case studies derived from historical NASA missions and programs available as a resource for analyzing prior non-conformance management cases.
   * Website: [https://llis.nasa.gov](https://llis.nasa.gov/)
2. **Key NASA Standards and Guidance Documents:**

   * SWE-202: Software Severity Levels for Non-Conformance Classification.
   * SWE-204: Root Cause Analysis and Process Assessments.
   * SWE-205: Defect Reporting and Metrics.
3. **Software Engineering Handbook (NASA-STD-8739.8):**

   * Sections on defect tracking, problem reporting, and software assurance processes.

By incorporating the lessons above, project managers and engineers can improve their ability to identify, track, and resolve software non-conformances—building more reliable and reusable software systems.

## 6.2 Other Lessons Learned

### 6.2.1 Software Change Tickets

* Any tests (formal or informal) that fail should be rerun and verified before software change tickets are closed, in the original environment, or as close to it as possible. Preferably this would be done with the original author of the software change ticket but with appropriate control board approval.
* Be cautious about closing overlapping software change tickets to ensure that the full scope of all associated software change tickets is addressed via retest. Be careful about missing any unique elements to the individual software change ticket.

### 6.2.2 GSFC Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Communicate FSW problems found in BVT to the I&T team](https://software.gsfc.nasa.gov/lesson-details/113/). **Lesson Number 113**: The recommendation states: "Communicate FSW problems found in Build Verification Testing (BVT) to the I&T team."

# 7. Software Assurance

**SWE-201 - Software Non-Conformances**

5.5.1 The project manager shall track and maintain software non-conformances (including defects in tools and appropriate ground software).

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that all software non-conformances are recorded and tracked to resolution.

2. Confirm that accepted non-conformances include the rationale for the non-conformance.

## 7.2 Software Assurance Products

This improved guidance aims to emphasize clarity, completeness, and system-wide accountability for software assurance (SA) activities associated with managing software non-conformances. The guidance includes updated recommendations for practices, SA products, metrics, and actions to ensure the highest quality and traceability for managing software defects, discrepancies, and other types of non-conformances throughout the software lifecycle. Highlighting automation, efficiency, and best practices allows teams to effectively meet NASA standards while addressing mission-specific needs.

Software Assurance (SA) must generate and maintain the following **key artifacts and deliverables** to ensure full visibility of the software non-conformance process:

#### **Updated List of Non-Conformance Tracking Records and Verified Closures**

SA must maintain a **comprehensive list of software non-conformances** verified for closure. The record must include:

* Complete traceability from their discovery (including test phases) to their resolution.
* Verification artifacts associated with closure activities, including test evidence and system state after resolution.

#### **Recommended SA Deliverables:**

1. **Defect/Problem Reporting Data:**

   * Updated logs of software defects, discrepancies, and non-conformances, categorized by severity.
   * Include trends over time to monitor the effectiveness of the defect management process.  
     *Tool Recommendations:* Use defect tracking systems (e.g., Jira, Bugzilla) with detailed data fields such as priority, age, root cause, and resolution status.
2. **Software Configuration Management Data:**

   * Configuration details from tools, environments, and baseline revisions to provide context for resolving non-conformances.
   * Validation that software configuration items match the version specified in the defect repository/log before defect reproduction and resolution.
3. **SA Audit Results on Change Management Process:**

   * Records from audits of workflows for identifying, reviewing, and closing non-conformances.
   * Include findings related to process gaps or violations of SWE-201, SWE-202, SWE-204, and related standards.
4. **Software Milestone Results:**

   * Assurance reports detailing the status of non-conformance resolution at major software lifecycle milestones (e.g., PDR, CDR, TRR). Use milestone reports to establish a correlation between successful defect resolution and system readiness.
5. **Software Version Description Documents (VDDS):**

   * Detailed documentation of updates to software versions that specify which non-conformances have been addressed. Include traceability for each resolved discrepancy.
6. **Software Control Board Data or Presentations:**

   * Meeting minutes, decision logs, and rationales from control board reviews of non-conformances and the approval status of associated corrective actions.
   * Verification of updates to the impacted artifacts as re-approved by the board.

#### **Enhancements:**

* Maintain **real-time synchronization** between defect-tracking records and SA verification logs to provide instantaneous alignment between project teams and software assurance.

## 7.3 Metrics

Metrics are crucial in software assurance for assessing the frequency, severity, and resolution trends of non-conformances. The following metrics improve insight and decision-making for managing discrepancies:

#### **Expanded Metrics for Enhanced Monitoring:**

**1. Cybersecurity Vulnerabilities and Weaknesses:**

* Number and severity of cybersecurity-related non-conformances.
* Open vs. closed cybersecurity vulnerabilities over time.
* Time to resolution for critical vulnerabilities (ensuring alignment with cybersecurity response protocols).
* Trends showing improvements in vulnerability resolution rates across releases.

**2. Non-Conformance Tracking Metrics:**

* Total number of non-conformances identified at each severity level (using SWE-202 severity classifications).
* Number and percentage of non-conformances resolved or deferred (by root cause area).
* Average age of unresolved non-conformances (track aging tickets to identify bottlenecks).
* Count of non-conformances introduced at each phase of the development lifecycle (e.g., requirements, design, implementation, testing).

**3. Metrics on Process and Work Product Audit Non-Conformances:**

* Number of audit non-conformances (categorized as process-related or work product-related).
* Trends of audit non-conformances over time, broken down by project lifecycle phases.
* Correlations between work product quality metrics and unresolved audit findings.

#### **Recommended Metric Visualizations:**

* **Bar Graphs or Heatmaps:** Severity distribution of non-conformances.
* **Trend Lines:** Progress of closing non-conformances over time (Open vs. Closed).
* **Radar Charts:** Comparisons of defect distribution across lifecycle phases and subsystems.

> **Reference:** Use **Topic 8.18 - SA Suggested Metrics** for further implementation examples.

## 7.4 Software Assurance Guidance

#### **Importance of Non-Conformance Management in SA:**

One of the critical elements in achieving software quality is ensuring that all discrepancies, errors, and non-conformances identified across the lifecycle are systematically addressed. This involves **proactive monitoring, recording, and verifying** the resolution of all issues, particularly during testing, integration, and operations.

#### **Recommended SA Activities for Non-Conformance Management:**

1. **Active Oversight of Discrepancies Across Testing Levels:**

   * Prioritize SA involvement in test execution to **witness tests in real time** or review test reports.
   * Confirm the fidelity of recorded test results, validating that any discrepancy or failure is logged in the defect tracking system (per SWE-201).
2. **Verification of Discrepancies in All Software Types:**

   * Confirm that discrepancies in mission software, development tools, and ground systems are accurately logged. Track issues surfaced in external systems (e.g., COTS, MOTS, GOTS, OSS) found during testing of project software.
   * Collaborate with vendors or developers to address known issues in reused software. Leverage online vendor portals to cross-check defect lists for COTS/MOTS.
3. **Validate Severity Assignment:**

   * Ensure each non-conformance is categorized using **SWE-202 severity classifications.**
   * Review severity definitions consistently with the project team to avoid errors in prioritizing defect resolution.
4. **Proactively Investigating Similar Issues in Codebase:**

   * Collaborate with development teams to identify repeated patterns of code, logic, or design vulnerabilities.
   * Lead an effort to confirm that similar discrepancies do not exist within corresponding software modules or systems.
5. **Tracking Defects to Full Resolution:**

   * Periodically review the defect database to confirm that:
     + Open non-conformances are actively being worked on and are not stagnant.
     + Approved corrections are fully implemented and regression-tested.
     + Deferred or rejected discrepancies are justified with documented rationales.
6. **Integration of Non-Conformance Metrics into Assurance Assessments:**

   * Monitor compliance with non-conformance management processes through audits (e.g., SWE-204).
   * Report unresolved issues, aging tickets, and trends to project management and stakeholders while using failure trends for strategic process improvement.
7. **Prevent "Duplicate Closure" of Overlapping Issues:**

   * Validate the full resolution of overlapping tickets to ensure **unique discrepancies** have not been inadvertently missed during testing.
8. **Audit and Document Changes to Impacted Artifacts:**

   * Support control boards in tracking decisions related to non-conformance resolution. Ensure processes for closing tickets also capture updates to impacted documents (e.g., requirements baselines, ICDs, test plans).

### **Additional Recommendations for SA Based on Lessons Learned**

* Prioritize **earlier involvement**: Engage SA earlier in lifecycle phases to ensure discrepancies are tracked starting from requirements validation.
* **Automate workflows:** Use automated tools for defect reporting, test verification, and metrics generation to reduce manual errors.
* Centralize non-conformance tracking data into a **version-controlled database** accessible across teams to avoid disjointed records.

By following the enhanced set of software assurance activities and metrics described above, project teams can uphold NASA’s rigorous quality standards while ensuring traceable and actionable management of software non-conformances across the entire lifecycle.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [SWE-204 - Process Assessments](/spaces/SWEHBVD/pages/102695538/SWE-204+-+Process+Assessments)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical for demonstrating compliance with this requirement and ensuring that all software non-conformances are properly tracked, addressed, and resolved. This evidence provides a traceable record that validates the implementation of defect management processes and supports assurance activities. Below is a comprehensive list of objective evidence that aligns with this requirement.

---

### **1. Defect and Non-Conformance Records**

* **Defect Tracking Logs:**

  + A complete repository of all non-conformances identified in the project (e.g., defect reports, problem reports).
  + Include critical details such as:
    - Unique defect ID.
    - Description of the non-conformance.
    - Date discovered.
    - Severity level (refer to SWE-202).
    - Status (Open, In Progress, Resolved, Closed).
    - Root cause analysis results (if applicable).
    - Assigned team/individual responsible for resolution.
    - Action taken to address the defect and supporting test results.
* **Examples:**

  + Jira reports or exported logs.
  + Excel or database records for defect tracking.
  + Problem reports from internal or external tools (e.g., GitHub, GitLab, Bugzilla).

---

### **2. Configuration Management Artifacts**

* **Version Control History:**

  + A record of modifications made to the software associated with resolving non-conformances, including linked change requests and defect IDs.
  + Commit history from version control systems (e.g., Git) that tracks changes made to address specific defects.
* **Baseline Configuration Records:**

  + Evidence showing that the project configuration matches the documentation of the software version at the time the defect occurred.
* **Software Version Description Documents (VDDs):**

  + Documents detailing the baseline version of software, which include:
    - Known non-conformances and their resolutions.
    - Any open, deferred, or accepted defects remaining in the delivered software.

---

### **3. Test Results and Discrepancy Reports**

* **Test Execution Logs:**

  + Evidence of testing activities during which non-conformances were discovered.
  + Traceability between test case results and defects logged.
* **Discrepancy Reporting System Output:**

  + Reports documenting discrepancies identified during subsystem testing, integration testing, or system verification.
* **Regression Test Results:**

  + Testcase results showing that non-conformance fixes were validated in production or test environments.
  + Artifacts proving that software after defect resolution did not regress any functionality (e.g., software test logs, automated test scripts, simulation results).

---

### **4. Change Management Process Documentation**

* **Change Requests (CRs)/Problem Reports (PRs):**

  + Objective evidence linking non-conformances to:
    1. Associated change request documentation.
    2. Configuration items updated.
    3. Disposition (e.g., approved, denied, deferred).
* **Control Board Records/Meeting Minutes:**

  + Minutes of Configuration Control Board (CCB) reviews for non-conformance prioritization and defect closure approval.
  + Rationale for decisions made by the CCB (e.g., accepting a deferred fix, limiting impact of changes).

---

### **5. Software Assurance Artifacts**

* **Audit Results and Checklists:**

  + Evidence of software assurance audits performed on the defect tracking process.
  + Include compliance checks for:
    - Adequacy of defect logging.
    - Severity assignment alignment with defined criteria (SWE-202).
    - Timeliness and thoroughness of resolutions.
* **Metrics Reports:**

  + Reports generated by software assurance to provide insights into defect management, such as:
    1. Number of open/closed non-conformances over time.
    2. Defect severity level trends.
    3. Closure rates and backlog trends.
    4. Non-conformances detected and resolved by lifecycle phase.
    5. Age of unresolved defects, emphasizing critical or high-severity issues.

---

### **6. Vendor and Reuse Evidence**

* **COTS, MOTS, GOTS, and Reuse Discrepancy Records:**

  + Evidence from vendor documentation or communication (e.g., lists of known product bugs and discrepancies).
  + Integration test reports showing the impact of reused software or externally sourced components on project-level software.
* **Vendor/Developer Correspondence:**

  + Communication logs verifying that discrepancies discovered in COTS, MOTS, OSS, or reused software were logged and addressed.
  + Mechanisms for notifying vendors of newly-discovered defects for external components.

---

### **7. Root Cause Analysis Documentation**

* **Root Cause Reports:**

  + Evidence of analysis performed for high-severity or recurring non-conformances. Include:
    - Root cause summary.
    - Recommendations to prevent recurrence in future projects or iterations.
    - Traceability to corrective actions implemented.
* **Lessons Learned Documentation:**

  + Records summarizing insights from analysis of non-conformance trends, used to inform similar issues in future projects.

---

### **8. Non-Conformance Tracking System Outputs**

* **Captured System Data:**

  + Exported reports from defect tracking systems detailing all logged non-conformance activity (open, closed, deferred).
* **Integrated Traceability Data:**

  + Evidence that shows traceability between identified non-conformances and related artifacts such as:
    - Requirements (to show requirement gaps or violations).
    - Design specifications.
    - Code changes.
    - Test cases.

---

### **9. Cybersecurity Records**

* **Cybersecurity Vulnerability Logs:**

  + Reports of all cybersecurity-related vulnerabilities identified during testing, including mitigation status and severity rates.
  + Evidence of security patches or corrective software updates made to address these vulnerabilities.
* **Vulnerability Scanning Reports:**

  + Automated scanning results validating that security-related non-conformances were resolved and vulnerabilities closed.

---

### **10. Final Delivery Artifacts**

* **Non-Conformance Summary Reports:**

  + Final project report documenting all non-conformances handled during the project lifecycle, including:
    - Remaining open non-conformances.
    - Impact analysis of unresolved or deferred non-conformances.
    - Workarounds or recommendations for future project teams.
* **Certification and Verification Reports:**

  + Evidence affirming that all critical non-conformances were resolved as part of delivery criteria.

---

### **Important Considerations for Objective Evidence**

1. **Traceability:**

   * Ensure evidence links non-conformances with resolution actions, associated artifacts, and verification activities. Use unique identifiers to support end-to-end traceability.
2. **Clarity and Accessibility:**

   * Maintain clear and centralized storage for all objective evidence, allowing historical records to be easily accessed.
   * Use search-friendly tracking tools for efficient access to defect resolution records.
3. **Timeliness:**

   * Provide objective evidence at required milestones (e.g., PDR, CDR, TRR) to demonstrate the status of non-conformance management at each lifecycle stage.
4. **Alignment with Standards:**

   * Ensure objective evidence complies with NASA standards such as SWE-201 (Discrepancy Reporting) and SWE-204 (Process Assessments).

---

**By gathering and organizing the above categories of objective evidence, project teams can demonstrate compliance with non-conformance tracking requirements, drive process improvements, and assure stakeholders of software quality and reliability.**

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
