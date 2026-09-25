# SWE-053 - Manage Requirements Changes

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695435. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes

SWE-053 - Manage Requirements Changes

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695435)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695435&showCommentArea=true&showComments=true#addcomment)

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

4.1.5 The project manager shall track and manage changes to the software requirements. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-053 History

SWE-053 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.1.2.1 The project shall collect and manage changes to the software requirements. |
| Difference between A and B | Changed "collect" to "track". |
| B | 4.1.3.1 The project manager shall track and manage changes to the software requirements. |
| Difference between B and C | No change |
| C | 4.1.5 The project manager shall track and manage changes to the software requirements. |
| Difference between C and D | No change |
| D | 4.1.5 The project manager shall track and manage changes to the software requirements. |

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
| * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) |

# 2. Rationale

Requirements change management helps ensure alignment between the software requirements and the project’s software plans and software work products. Collecting, analyzing, and managing requirements changes allow a project to control those changes and measure their impact. Requirements change management can also provide early insights into the impact of those changes to the overall project's budget and schedule, including the ability to plan how to address changes rather than simply reacting when a change is made.

Effective tracking and management of changes to software requirements is **critical to the success of a software development project**, particularly for NASA projects where safety, mission success, and system reliability are paramount. Below is a detailed explanation of why this requirement is necessary and how it contributes to the overall project lifecycle.

---

### **1. Managing Complexity in NASA Projects**

#### Rationale:

NASA software is often embedded within complex systems involving hardware, operators, and environmental interaction. These systems are inherently dynamic, and requirements are subject to change due to evolving risks, technical refinements, discoveries, or mission scope adjustments.

* **Impact:** Unmanaged or poorly tracked changes can lead to misaligned hardware/software integration, outdated test plans, or compatibility issues between system components.
* **Why It's Critical:** Tracking changes ensures that all stakeholders understand the evolving requirements and can adjust system design, software functionality, and testing activities accordingly.

#### Example:

If the requirement for a sensor’s operational range changes (e.g., from 100°C to 120°C), the software must be updated to handle the new limits. Failure to track and manage such changes could result in the software erroneously shutting down the system during normal operations.

---

### **2. Preventing Scope Creep**

#### Rationale:

Software requirements represent the agreed-upon functionality and features needed for successful project execution. Uncontrolled changes to requirements can lead to scope creep, where added functionalities unnecessarily increase development time, cost, and complexity.

* **Impact:** Scope creep often results from informal or undocumented changes, leading to unplanned resource allocation and delays.
* **Why It's Critical:** By tracking changes, project managers ensure that every change request undergoes proper review, justification, and approval.

#### Example:

A request to add new non-critical features late in the project lifecycle could jeopardize delivery schedules. Tracking ensures a formal process evaluates whether the added feature is justified or should be deferred.

---

### **3. Safety Assurance and Risk Mitigation**

#### Rationale:

Software requirements often include **safety-critical functionality** tied to hazard controls, hardware redundancy, or fault tolerance. Unmanaged changes to these requirements could introduce new hazards, invalidate previous analyses, or compromise mission safety.

* **Impact:** Changes to safety or operational requirements without adequate tracking can lead to undetected vulnerabilities or the introduction of failure points.
* **Why It's Critical:** Tracking ensures that any changes in safety-related requirements trigger associated updates in hazard analyses, testing plans, and fallback mechanisms.

#### Example:

If the requirement specifying a spacecraft’s emergency shutdown threshold changes, and the update isn't tracked, the software might fail to meet new system thresholds, ultimately risking the mission or crew safety.

---

### **4. Maintaining Requirements Traceability**

#### Rationale:

Requirements are linked to various project artifacts—including design documents, code, test cases, validation results, and hazard analyses. Changes must be tracked to maintain traceability and ensure the development pipeline aligns with the latest requirements.

* **Impact:** Failure to update linked artifacts after requirements changes can lead to inconsistencies, such as testing outdated functionality or incorrect implementation.
* **Why It's Critical:** Tracking changes ensures requirements are fully traceable throughout development, enabling engineers to verify functionality and validate safety.

#### Example:

A requirement update specifying a different communications protocol must cascade through interface designs, test cases, and code implementation. Without tracking, teams may overlook these updates, creating defects.

---

### **5. Regulatory Compliance with Standards**

#### Rationale:

NASA projects are subject to rigorous safety, quality, and mission assurance standards (e.g., NASA-STD-8739.8 and NASA-STD-8719.13). Many of these standards require documentation and validation of requirements changes.

* **Impact:** Poor change management can result in noncompliance with NASA standards, potentially leading to failed audits, mission delays, or unsafe operations.
* **Why It's Critical:** Tracking changes ensures all modifications are reviewed, documented, and validated to meet compliance and certification requirements.

#### Example:

If a software requirement for environmental shielding changes due to a new NASA safety guideline, failure to formally track and implement the change could result in mission delays during regulatory review.

---

### **6. Cost and Schedule Control**

#### Rationale:

Changes to requirements almost always impact project cost and schedule. Each update requires additional design, implementation, testing, and validation—each of which consumes resources.

* **Impact:** Untracked requirements changes can lead to uncontrolled cost increases and schedule overruns, especially in large, resource-intensive NASA projects.
* **Why It's Critical:** Formal tracking provides visibility on the scope of changes, allowing the project manager to assess and manage the financial and temporal impact of each change.

#### Example:

A propulsion system's software requirement changes to accommodate a new actuator design late in the project lifecycle. Proper tracking ensures the change is reviewed by all stakeholders, and the cost/schedule impact is transparently managed.

---

### **7. Facilitating Communication and Collaboration**

#### Rationale:

Changes to software requirements affect multiple teams, including software engineers, safety analysts, hardware designers, system architects, and mission operators. Without effective tracking mechanisms, teams may operate on outdated requirements, leading to errors or miscommunication.

* **Impact:** Misaligned actions caused by untracked or undocumented changes can compromise the system’s functionality or safety.
* **Why It's Critical:** Tracking changes ensures all stakeholders are notified and aligned, fostering collaboration and efficient integration of updates.

#### Example:

A minor change to user interface software requirements (e.g., adding an alert feature) could affect operator training materials. Tracking ensures operators are informed of both the change and its impact.

---

### **8. Supporting Verification and Validation (V&V)**

#### Rationale:

Verification and validation (V&V) processes ensure requirements are implemented correctly and fulfill their intended purpose. Requirements changes must be tracked to verify they are properly integrated into the software and validated to meet safety and performance goals.

* **Impact:** Untracked changes can lead to gaps in V&V activities, leaving vulnerabilities untested.
* **Why It's Critical:** Tracking changes ensures updated requirements are verified (against original expectations) and validated (that the software fulfills its purpose in mission scenarios).

#### Example:

A requirement update specifying faster data processing speeds would necessitate additional performance validation tests. Failure to track this change could lead to unnoticed defects during deployment.

---

### **9. Enabling Historical Accountability**

#### Rationale:

A comprehensive record of requirement changes provides historical accountability, allowing the team to:

* Diagnose past design decisions.
* Understand how systems evolved over time.
* Learn from previously rejected or approved changes for future reference.
* **Impact:** Lack of historical accountability can result in repeated mistakes or an inability to trace root causes during post-mission reviews.
* **Why It's Critical:** Tracking enables a full audit trail, essential for lessons learned and retrospective analysis.

#### Example:

After a mission anomaly, engineers can analyze the history of requirement changes to identify whether an overlooked modification contributed to the issue.

---

### **10. Reducing Integration Risks**

#### Rationale:

Since software must function seamlessly with hardware and operators, even minor updates to requirements can lead to incompatibility or new hazards.

* **Impact:** If these updates are unmanaged, integration testing may fail, jeopardizing mission readiness.
* **Why It's Critical:** Proper tracking mitigates integration risks by ensuring all changes are reviewed for downstream effects.

#### Example:

A requirement change to hardware telemetry frequency needs corresponding software updates for data processing. Untracked updates could lead to communication failures during integration testing.

---

### **Conclusion**

The rationale for Requirement 4.1.5 is rooted in ensuring transparency, control, and accountability throughout the software development lifecycle. By tracking and managing changes to software requirements:

* Projects minimize safety risks and defects.
* Teams maintain alignment and traceability across all phases.
* NASA ensures compliance with its standards for quality, reliability, and mission assurance.

Effective change management protects mission success, enhances collaboration, and ensures that software systems remain safe, functional, and aligned with the evolving needs of the hardware, operators, and overall mission objectives.

# 3. Guidance

## 3.1 Requirements Changes

Quoting [Wikipedia](https://en.wikipedia.org/wiki/Requirements_management), “Requirements Management is the process of documenting, analyzing, tracing, prioritizing and agreeing on requirements and then controlling change and communicating to relevant stakeholders. It is a continuous process throughout a project.”

As a project progresses and requirements are flown down, the requirements are decomposed into functional and performance requirements and allocated across the system. These are then further decomposed and allocated among the elements and subsystems. This decomposition and allocation process continues until a complete set of design-to requirements is achieved. During this process, it may become apparent that there are requirements that are missing, conflicting, unfeasible, etc. resulting in the need to modify the baselined requirements set. When changes to the requirements are required, it becomes necessary to track and manage those changes.

Requirements management practices control how requirements are introduced, changed, and removed. The average project experiences changes in requirements after the requirements have been defined for the first system release, which causes schedule slip.

Several studies also have shown that volatility in requirements contributes to the inefficient production of low-quality software. Consequently, requirements should be managed using a defined configuration management process that uses Change Control Boards (CCBs) and automated change control tools that manage each requirement as a separate item. Using a configuration management tool permits personnel to identify which requirements have been added, removed, or changed since the last baseline (requirements volatility), who has made these changes, when they were made, and the reason for making them. In addition, by maintaining requirements in a configuration management tool, they can be traced to the artifacts that realize them.

Changes to requirements can be an indicator of software instability or unclear description of the end product. Regardless of the reason, requirement changes often mean increased costs, longer schedules, and changes in the technical features of the software. Changes in requirements can result in rework and can affect software safety.

The actual process of making changes should be a structured, defined process. This process should describe how a proposed change is submitted, evaluated, decided upon, and incorporated into the requirements baseline. Usually, a Change Control Board, consisting of people from various disciplines and perspectives, will review potential changes and either approve or reject them. A requirements management tool can help manage the changes made to many individual requirements, maintain revision histories, and communicate changes to those affected by them.

Part of the change management process should be an evaluation of the impact the change will have on the system and other requirements especially safety and security requirements. See [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) for guidance on impact analysis, including cost, technical, and schedule impacts. Traceability information is an important tool in this evaluation. See [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) for guidance on requirements traceability.

Requirements management also includes the management of the software data dictionary content or ICD content.  Examples of the content contained in a software data dictionary may be found in topic [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary). Examples of content contained in an Interface Control Document (ICD) may be found in a future topic.

Keep in mind that managing changes to requirements is an ongoing process that occurs throughout the project life cycle and needs to be planned for during project planning activities.

For Class A software take care to analyze all software changes and software defects affecting safety-critical software  and hazardous functionality including [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action), 

See also [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements), [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis).

## 3.2 Capture And Manage The Changes

Consider using configuration management tools, requirements management tools, or change request tools to capture changes to requirements. Many of these tools will keep version histories and are able to provide reports on the changes. Some of those reports may be useful to management when analyzing the impact of the requirements changes on the project.

Regardless of the capture method, projects need to collect a minimum set of data to describe the requested change.  See topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report), for more information.

As part of managing requirements changes, the team needs to keep in mind the effect of "requirements creep" on software development, including its costs and complexity. Those performing impact analyses or approving/disapproving requirements changes need to carefully scrutinize requests to avoid approving enhancements not required to accomplish the project goals and objectives.

## 3.3 Analyze The Changes For Cost, Technical, And Schedule Impacts

**NASA/SP-2016-6105 Rev 2, NASA Systems Engineering Handbook**

6.2.1.2.5 Key Issues for Requirements Management - Requirements Changes  
"Effective management of requirements changes requires a process that assesses the impact of the proposed changes prior to approval and implementation of the change."[273](#_tabs-<p></p>)

**LLIS3377: Software Requirements Management**

In Lesson Learned Number 3377, the Space Shuttle Program learned that the use of manual methods for managing requirements resulted in a major impact on  cost and schedule over the entire software development life cycle.

Abstract:   
"The ability to manage and trace software requirements is critical to achieve success in any software project and to produce software products in a cost-effective and timely fashion. Conversely, incomplete, incorrect, or changing software requirements result in cost and schedule impacts that increase the later they occur (or are discovered) in the software life cycle."[576](#_tabs-<p></p>)

Once change requests are documented, the team analyzes them for their effect on all parts of the software system as well as their effect on the overall system and project, as applicable to the level of change. Typically, changes are reviewed by a CCB or other review board (see [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes)) who can request or perform an impact analysis (see [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes)) before determining how to disposition the change. 

When performing an analysis on the changes, look for impacts such as:

* Impact on other parts of the software system (not just the immediate design or code where the change will occur): architecture, design, interfaces, the concept of operations, higher- and lower-level requirements.
* Impact on other parts of the overall system (e.g., system requirements, interfaces, hardware).
* Safety, reliability, performance impacts.
* Skills needed (e.g., special expertise, additional developers, consultants).
* Rework effort (e.g., requirements specification, design, code, test, user manuals).
* New effort (e.g., code development, documentation, test case development, software assurance).
* Impact to stakeholders.
* Potential to introduce errors into the software.
* The criticality of the affected software.

Traceability matrices and tools are useful when determining the impact of a change, but the team needs to update the traceability information to keep it current as changes to the requirements occur (see [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability)).  Other relevant items, from NASA/SP-2016-6105 Rev 2, NASA Systems Engineering Handbook [273](#_tabs-<p></p>), include:

* Performance margins – "a list of key performance margins for the system and the current status of the margin... the propellant performance margin will provide the necessary propellant available versus the propellant necessary to complete the mission."
* Configuration management top evaluators list – "appropriate persons [to evaluate] the changes and providing impacts to the change... changes need to be routed to the appropriate individuals to ensure that the change has had all impacts identified."
* Risk system and threats list – "used to identify risks to the project and the cost, schedule, and technical aspects of the risk...A threat list is normally used to identify the costs associated with all the risks for the project."

The team uses the results of the impact assessment to determine the effect the change has on the project in terms of:

* Cost including personnel and equipment costs.
* Schedule including new or revised design, development, testing, and documentation effort.
* Technical impacts on the function of the software and overall system.

## 3.4 Document Analysis Results

Document and maintain the results of the impact analysis and any decisions based on that analysis with the project's records. Communicate the results to the appropriate stakeholders, i.e., project personnel who must implement approved changes, must update documentation related to those changes, or must test those changes; system-level personnel who must coordinate changes in response to this requirements change; as well as those affected if a requested change is *not* approved for implementation, including stakeholders outside the development team.

See also Topic [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)

## 3.5 Other Tasks

In addition to the activities noted above, managing changes to requirements may also include the following:

* Ensuring that relevant project plans are updated to reflect approved requirements changes.
* Ensuring change requests are created, assigned, and completed for work products affected by approved requirements changes, e.g., design documents, user manuals, interface specifications.
* Ensuring changed requirements and all related changed work products are verified and validated.
* Ensuring traceability documents are updated to reflect the requirements change.
* Ensuring that the rest of the project uses only the latest, updated project documents that reflect the requirements change.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)       * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements) |

# 4. Small Projects

Small projects, often constrained by limited resources and smaller teams, can simplify their approach to tracking and managing requirement changes while still maintaining rigorous compliance. This guidance focuses on streamlining activities and leveraging lightweight processes to ensure requirements changes are effectively managed.

---

### **1. Use Simple Tools for Requirement Change Tracking**

Avoid complex requirement management systems that may be excessive for small projects. Instead:

* **Use a Requirements Log:**

  + Maintain a spreadsheet (e.g., Microsoft Excel or Google Sheets) or a shared document to track software requirements, including changes.
  + Include columns such as:

    | **Requirement ID** | **Original Requirement** | **Proposed Change** | **Reason** | **Approval Status** | **Date Modified** | **Related Tests/Artifacts** |
    | --- | --- | --- | --- | --- | --- | --- |
* **Collaborative Tools:**  
  Use project management tools like Jira, Trello, or Confluence with tags or cards dedicated to tracking requirement updates and approvals.

#### Example:

For a small robotic control system project, a simple spreadsheet tracking updates to environmental resistance requirements (e.g., temperature limits) ensures changes are documented and understood by both software and hardware teams.

---

### **2. Establish Clear Change Control Process**

Create lightweight processes to manage requirement changes. Keep it simple but formal enough to ensure accountability.

#### Steps:

1. **Request for Change** (RFC):

   * Require a brief RFC from team members if a change to software requirements is needed.
   * Use an email or a simple form to document:
     + The proposed change.
     + Justification (e.g., updated hardware specs, new hazard analysis, operator feedback).
     + Impacts on other requirements, design, or testing.
2. **Review and Approval:**

   * Assign a small, agile group (e.g., the project manager and lead engineer) to review and approve changes.
   * Include stakeholders from hardware or operations to understand cross-disciplinary impacts.
3. **Update and Notify:**

   * Update the requirements log/documentation once changes are approved.
   * Notify all relevant team members of the change (via email, project tool notifications, etc.).

#### Example Process:

If an operator interface requirement changes (e.g., from minimal to complete touchscreen controls), the project manager would review the RFC, approve with input from operators, update both the requirements log and SRS, and notify the software developer handling the interface.

---

### **3. Apply Frequent Miniature Requirements Reviews**

Small projects benefit from frequent but brief requirements reviews during team meetings or sprint planning sessions. These informal reviews ensure that changes are manageable and tracked consistently.

#### Actions:

* Discuss updated or proposed requirements change in weekly meetings.
* Confirm impacts on design, development, and testing.
* Verify traceability between the updated requirement and related development artifacts.

#### Example:

For a small sensor-monitoring project, discuss a change to the sensor sampling frequency requirement during the weekly meeting and resolve any impacts on software processing speed.

---

### **4. Simplify Traceability**

Small projects need traceability to manage requirement updates effectively, particularly safety-critical requirements. Use lightweight methods to ensure linked artifacts remain current.

#### Actions:

* Maintain a **Traceability Table** manually or in project tools:

  | **Requirement ID** | **Linked Design Doc** | **Test Case** | **Change Date** | **Change Impact** |
  | --- | --- | --- | --- | --- |
* Update the table whenever a requirement change is made to ensure:

  + Design documents reflect updated requirements.
  + Test cases validate modified functionality or safety features.

#### Example:

For a temperature control system, if the maximum temperature threshold increases, update the design document to reflect hardware compatibility and add new test cases to verify the updated software response.

---

### **5. Focus on Communication**

In small projects, clear, frequent communication is essential for effectively managing requirement changes.

#### Tips:

* Schedule quick discussions or stand-ups to confirm changes with all affected team members (especially hardware developers, software engineers, operators, and testers).
* Use **shared online documentation** to make requirement changes visible to all team members in real-time.
* Provide a simple email summary of completed changes after every requirements modification.

#### Example:

Notify the team via email or messaging tool when there’s a change:  
*"The software requirement for hardware sensor A's response time has been reduced from 10ms to 5ms due to new hardware specs. The update will affect timing in modules X, Y. New test cases have been added to validate this adjustment."*

---

### **6. Prioritize Safety-Critical Changes**

Small projects should emphasize safety-critical requirement changes to avoid severe risks during integration or operation.

#### Steps:

* Assign priority labels (e.g., High, Medium, Low) to requirements, focusing time and effort on changes affecting safety-critical functions.
* Document safety-related changes separately in the Requirements Log for visibility and independent review by the team.
* Perform additional **Safety Impact Reviews** for each change to verify:
  + No new hazards have been introduced.
  + Existing mitigations remain valid.

#### Example:

For a robotic arm, a change that modifies the emergency stop threshold (e.g., maximum force detection) gets marked as “High Priority.” A safety review ensures the updated threshold doesn’t introduce unintended safety risks.

---

### **7. Keep Historical Records for Future Reference**

Small projects still require basic historical accountability for changes to trace root causes of design decisions and maintain lessons learned for future projects.

#### Actions:

* Archive past versions of the SRS and requirements logs.
* Mark entries with time-stamps and reasons for rejected or approved changes.

#### Example:

For a small environmental monitoring system, store a backup of original requirements showing the initial temperature limits, why they were updated, and the date of approval.

---

### **8. Automate Notifications (Optional Enhancement)**

If resources allow, automate tracking and notification processes to streamline requirement updates.

#### Tips:

* Use lightweight tools like **Trello** or **Jira** with automated alerts to notify affected teams when requirements change.
* Set up a shared workspace (e.g., Confluence page or Google Docs) where revised requirements show highlights of changed text.

#### Example:

For a small robotic project, a developer gets a notification in Trello when the actuator movement threshold increases, prompting updates to the control algorithm code.

---

### **9. Perform Informal Audits**

While formal audits may not always be feasible for small projects, conduct informal audits periodically to ensure requirement changes are well-documented and traceable.

#### Actions:

* Review the Requirements Log or SRS to ensure all tracked changes link to design, code, and test cases.
* Validate that all stakeholders (hardware, software, testing teams) are aligned after the latest changes.

#### Example:

For a small atmospheric data-collection project, the project manager does a quick review every two weeks to confirm requirements updates are traceable to corresponding design and testing artifacts.

---

### Example Requirements Change Workflow for Small Projects:

1. **Identify Change**: Proposed sensor adjustment for temperature tolerance from 100°C to 120°C.
2. **Document Change**: Stakeholder submits an RFC via email or simple tracking tool.
3. **Review Change**: Project manager reviews the need and impact, collaborates with hardware/software teams.
4. **Approve/Reject**: Discuss in a team meeting or informal approval group; document the decision.
5. **Update Artifacts**: Modify Requirements Log, SRS, linked design/test cases.
6. **Notify Team**: Email or message summarizing the approved change.
7. **Verify Impact**: Ensure tests are updated and results properly documented.

---

### **Summary Checklist for Small Projects**

To manage requirement changes under limited resources:

* Use simple tools (e.g., spreadsheets, collaborative software like Trello).
* Establish a lightweight change control process with quick reviews.
* Maintain a clear Requirements Log with timestamps and rationale.
* Focus on traceability for high-priority (especially safety-critical) requirements.
* Communicate changes clearly and frequently with all stakeholders.
* Archive historical changes for accountability and lessons learned.

By following this approach, small projects can effectively meet Requirement 4.1.5 while maintaining efficiency and resource alignment. This ensures requirements updates are tracked, controlled, and integrated without introducing risks or overwhelming the team.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-441)

  [Requirements Management Process and Database](https://llis.nasa.gov/search?page=1&query=23801 "Click to open in new window")

  Public Lessons Learned Entry: 23801.
* (SWEREF-512)

  [Lewis Spacecraft Mission Failure Investigation Board](https://llis.nasa.gov/lesson/625 "Click to open in new window")

  Public Lessons Learned Entry: 625.
* (SWEREF-576)

  [Software Requirements Management](https://llis.nasa.gov/lesson/3377 "Click to open in new window")

  Public Lessons Learned Entry: 3377.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Managing requirements change is critical to the success of NASA projects, and the NASA Lessons Learned Database highlights key examples illustrating the importance of effectively tracking and managing requirements. These lessons emphasize the impact of unmanaged or poorly implemented requirements changes on cost, schedule, system certification, and mission success — particularly in complex and safety-critical systems. Additional relevant lessons associated with requirements change management have been included to further reinforce the importance of this practice.

---

### **Relevant Lessons Learned:**

---

#### **1. Lewis Spacecraft Mission Failure Investigation Board (Indirect contributors to loss of spacecraft)**

**Lesson Number:** 0625  
**Summary:**  
The investigation into the loss of the Lewis Spacecraft revealed indirect contributors tied to the "Faster, Better, Cheaper" approach, which included changes to requirements without adequately adjusting resources (such as funding, personnel, and schedule). Insufficient resources meant that the project failed to fully assess the impacts of requirements changes, leading to system inadequacies and eventual mission failure.

**Key Takeaways:**

* Requirements changes must be accompanied by adjustments in project resources and schedules to address potential impacts across the lifecycle.
* Failure to manage resource allocation following requirement changes can lead to insufficient implementation, testing gaps, or hazards left unaccounted for.

**Connection to Requirement 4.1.5:**  
Tracking and managing requirements changes should include a mechanism to assess and allocate additional resources needed for implementation of the change. This practice prevents cascading failures caused by inadequate assessments.

---

#### **2. Software Requirements Management (Space Shuttle Program)**

**Lesson Number:** 3377  
**Summary:**  
The legacy manual methods used throughout the Space Shuttle Program for managing software requirements caused major cost and schedule impacts. Poor visibility into requirements change history, limited traceability, and cumbersome manual processes delayed progress and added unnecessary complexity throughout the software development lifecycle.

**Key Takeaways:**

* Automated tools for managing requirements change are essential for minimizing cost and schedule impacts, improving traceability, and enabling efficient integration of updates.
* Legacy methods that lack visibility into change history and connections between artifacts create unnecessary risk and inefficiency.

**Connection to Requirement 4.1.5:**  
Implement simple, efficient requirements tracking mechanisms, even for small projects, to enable full traceability and reduce delays caused by outdated, manual processes.

---

#### **3. Requirements Management Process and Database (Ground Systems Development and Operations Program)**

**Lesson Number:** 23801  
**Summary:**  
The Ground Systems Development and Operations (GSDO) Program implemented a commercially available requirements management tool, but still faced cost and schedule impacts due to structural and procedural issues with managing requirements changes. Problems included the inefficient closure of requirements, lack of configuration management for closure evidence, and significant effort required to correct issues in the requirements set.

**Key Takeaways:**

* A well-defined and efficient requirements management process is critical, even when using advanced tools.
* Configuration management of closure evidence is essential to streamline certification and acceptance reviews.
* Structural issues with the requirements allocation and tracking process can create cascading delays and require significant rework.

**Connection to Requirement 4.1.5:**  
Structure requirements change tracking processes to ensure efficient allocation, traceability, and closure, while maintaining configuration-managed repositories for evidence of compliance.

---

### **Additional Lessons Learned On Requirements Management:**

---

#### **4. Mars Climate Orbiter (1999)**

**Lesson Number:** Not Assigned  
**Summary:**  
The loss of the Mars Climate Orbiter was ultimately caused by failures in requirements management, including a failure to manage the crucial requirement of unit consistency between software subsystems (Imperial vs. Metric). Requirements changes or assumptions were not adequately tracked or validated, leading to the orbiter entering the Martian atmosphere at an incorrect trajectory angle, causing catastrophic mission failure.

**Key Takeaways:**

* Each requirement change must be assessed for its downstream impacts on development, testing, and integration efforts, including the propagation of changes across interfaces between teams.
* High-priority requirements, such as unit compatibility, should undergo rigorous validation when modified to avoid mission-critical integration errors.

**Connection to Requirement 4.1.5:**  
Tracking requirements changes and ensuring traceability between hardware, operators, and software systems prevents costly mistakes and integration errors that can jeopardize safety or mission success.

---

#### **5. Mars Polar Lander (1999)**

**Lesson Number:** Not Assigned  
**Summary:**  
Premature shutdown of the Mars Polar Lander’s descent engines was caused by requirements oversight related to the software’s handling of hardware sensor data. Requirements changes made late in development introduced assumptions between hardware and software systems that were not properly validated or tracked, resulting in the misinterpretation of sensor vibrations as a landing signal.

**Key Takeaways:**

* Requirements changes involving critical interfaces (hardware-software or operator-software) must be tracked and validated to ensure correct implementation and elimination of invalid assumptions.
* Late-stage requirements changes should be thoroughly reviewed for unintended consequences before implementation.

**Connection to Requirement 4.1.5:**  
Track and manage all late-stage requirements changes systematically to mitigate risks, especially for safety-critical systems with hardware-software dependencies.

---

#### **6. Genesis Spacecraft Crash (2004)**

**Lesson Number:** Not Assigned  
**Summary:**  
The Genesis spacecraft experienced a crash due to failure to deploy its parachutes properly, caused by software requirements that did not adequately handle sensor data or fallback modes for deployment. Requirements for handling off-nominal conditions and failure modes were not robust, and changes were not systematically tracked or validated during development.

**Key Takeaways:**

* Requirements for handling off-nominal conditions should be explicitly defined and updated based on hazard analyses, then tracked to ensure implementation.
* Any changes to safety-critical requirements must involve systematic downstream testing and verification.

**Connection to Requirement 4.1.5:**  
Ensure safety-critical requirements changes are tracked throughout the lifecycle and evaluate their impact on failure modes and contingency systems.

---

#### **7. Apollo 12 Lightning Strike Incident (1969)**

**Lesson Number:** Not Assigned  
**Summary:**  
During Apollo 12’s launch, lightning strikes resulted in unexpected system data anomalies, highlighting the importance of proper requirements for fallback and diagnostic modes. Lessons learned emphasized that tracking requirements for abnormal conditions and integrating fallback systems are essential for mission success.

**Key Takeaways:**

* Requirements changes related to contingency or fail-safe modes must be formally tracked, validated, and tested to ensure the system makes correct decisions during unexpected incidents.
* Changes to abnormal-condition handling must address requirements dependencies with hardware, software, and operators to prevent cascading failures.

**Connection to Requirement 4.1.5:**  
Track and manage all changes to fallback mode requirements to enhance system robustness and resilience to unplanned conditions.

---

### **Conclusion: Lessons Learned and Best Practices**

These NASA Lessons Learned underscore the critical importance of tracking and managing requirements changes, especially in safety-critical and mission-critical systems. Common themes include:

1. **Resource Alignment**: Ensure adequate resources—including time, funding, and personnel—are allocated for implementing and testing requirements changes.
2. **Traceability**: Provide full traceability between requirements changes and downstream artifacts, including design, code, and testing.
3. **Validation and Certification**: Ensure efficient processes for validating and certifying updated requirements, especially in safety-critical systems.
4. **Late-Stage Risk Mitigation**: Apply rigorous reviews to late-stage requirements changes to prevent avoidable risks or defects.
5. **Interdisciplinary Coordination**: Coordinate changes across hardware, software, and operator teams to minimize integration risks.

By addressing these lessons in compliance with Requirement 4.1.5, projects can avoid cost and schedule overruns, minimize risks to safety and mission success, and ensure efficient implementation of updated requirements across all lifecycle phases.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [In the FSW plan, include staffing for FSW GN&C requirements](https://software.gsfc.nasa.gov/lesson-details/69/). **Lesson Number 69**: The recommendation states: "In the FSW plan, include staffing for FSW GN&C requirements definition/refinement throughout the entire lifetime of FSW GNC development."
* [A single requirements repository should be used on a project](https://software.gsfc.nasa.gov/lesson-details/88/). **Lesson Number 88**: The recommendation states: "A single requirements repository should be used on a project (or closely coordinate when requirements must appear in multiple specs, such as GN&C)."
* [Delete obsolete requirements](https://software.gsfc.nasa.gov/lesson-details/96/). **Lesson Number 96**: The recommendation states: "Do not be reluctant to delete obsolete requirements."
* [Control GN&C algorithm changes with the same rigor as software requirements changes](https://software.gsfc.nasa.gov/lesson-details/111/). **Lesson Number 111**: The recommendation states: "Control GN&C algorithm changes with the same rigor as software requirements changes. The algorithm document needs to baselined and subsequently controlled like any other requirement."
* [Satisfy critical functionality with systems developed against key requirements, not as a Tech Demo](https://software.gsfc.nasa.gov/lesson-details/341/).**Lesson Number 341**: The recommendation states: "It is risky to assume that functionality developed as Tech Demo will receive sufficient attention/resource to achieve operational status. Instead, designate desirable functions as requirements, so they receive project resources and priority."

# 7. Software Assurance

**SWE-053 - Manage Requirements Changes**

4.1.5 The project manager shall track and manage changes to the software requirements.

## 7.1 Tasking For Software Assurance

**From NASA-STD-8739.8B**

1. Confirm the software requirements changes are documented, tracked, approved, and maintained throughout the project life cycle.

## 7.2 Software Assurance Products

Software assurance (SA) should generate high-quality products to identify, monitor, and communicate issues, trends, and recommendations concerning requirements changes. These products capture the outcomes of requirements change management processes and highlight opportunities for improvement to prevent risks.

#### **1. Issues and Concerns from Requirements Volatility Trending**

* **Enhanced Guidance:**  
  SA analyzes and reports **requirements volatility** (i.e., frequent changes to requirements) to identify risks associated with unstable requirements. Volatility can impact cost, schedule, testing, and quality, and it must be proactively monitored to ensure project stability.

  **Products:**

  + **Volatility Analysis Report**: A report summarizing key requirement fluctuations over the lifecycle (e.g., % of requirements added, deleted, or updated per milestone).
    - Include assessments of the root causes of volatility (e.g., unclear initial requirements, scope creep, incomplete stakeholder input).
    - Evaluate whether volatility is acceptable or repetitive and whether it introduces delays, scope changes, or testing risks.
  + **Risk Assessment for Volatility Trends**: Identify high-risk areas associated with constant requirement changes (e.g., safety-critical or interface requirements).
    - Actionable recommendations tied to stability goals.

**Example:** If the number of software requirements for a spacecraft increases by 35% mid-project to accommodate unforeseen hardware changes, the SA report highlights risks of integration rework, increases in unvalidated functionality, and the need for additional time/resources.

---

#### **2. Document Change Management System Results**

* **Enhanced Guidance:**  
  SA monitors the performance of the **change management system** to ensure requirements changes are tracked, implemented, and closed efficiently. This involves reviewing the **Change Control Board (CCB)** records, analyzing approval timelines, and assessing how effectively the system identifies, communicates, and resolves issues related to requirements updates.

  **Products:**

  + **Change Management System Audit Report**: Highlights findings from SA’s review of the change management system, including:
    - Number of submitted change requests vs. those approved/rejected.
    - Average time to process a requirements change (e.g., submission to approval; approval to closure).
    - Identification of delays or inefficiencies (e.g., bottlenecks in impact analysis or alignment across teams).
    - Recommendations to improve responsiveness and coordination in the change control process.
  + **Compliance Report**: Confirms whether the change management system adheres to project policies, NASA standards (e.g., NASA-STD-8739.8), and configuration management best practices.

**Example:** Delayed implementation of safety-critical changes due to a slow CR approval process may lead to a recommendation for streamlining stakeholder coordination or automating steps to alert teams to pending actions.

---

#### **3. Software Problem Reporting or Defect Tracking System Results**

* **Enhanced Guidance:**  
  Requirements volatility can result in incorrect, incomplete, or inconsistent updates to downstream design, code, or testing. The **issue tracking system** must capture and report these defects to assess the quality of requirements changes and identify recurring problems.

  **Products:**

  + **Defect Analysis Report**: Analyze trends in the defect tracking system as they relate to requirements changes, including:
    - Number of defects introduced by requirements changes.
    - Defect root causes (e.g., poorly understood impacts, incomplete testing of changes).
    - Time and effort required to resolve defects introduced by requirements changes.
  + **Recommendations for Issue Mitigation**: Actions for improving the requirement change process (e.g., improving traceability, more rigorous validation testing) to reduce defects introduced by frequent or late-stage changes.

**Example:** If 25% of defects are traced to unclear requirements updates (e.g., incomplete test coverage for new requirement integration), an SA recommendation might include mandatory peer reviews before implementing changed requirements.

---

### **7.3 Metrics**

Software assurance monitors key metrics to evaluate the stability, reliability, and quality of the requirements change management process. These metrics help assess risks and track the effectiveness of risk mitigation activities over time.

#### **Recommended Metrics:**

---

#### **1. Software Requirements Volatility**

**What It Measures:** The number and proportion of requirements added, deleted, or modified over time, including the number of TBD (“To Be Determined”) items as requirements evolve.

* **Purpose:** Allows SA to monitor the stability of the requirements baseline.
* **Calculation Examples:**
  + % Change in Total Requirements per Milestone: [ \text{Volatility Rate} = \frac{\text{# of Changes (added + deleted + modified)}}{\text{Total # of Baseline Requirements}} \times 100 ]
  + Tracking TBDs over time to ensure all open items are resolved before critical development milestones.

---

#### **2. Change Status Trend Over Time**

**What It Measures:** Tracks the lifecycle status of all requirements change requests (CRs) across time, such as the numbers of changes in "Proposed," "Approved," "In Implementation," "In Test," and "Closed" phases.

* **Purpose:** Provides visibility into how efficiently changes are processed and resolved.
* **SA Focus:**
  + Identify bottlenecks (e.g., changes stuck in review for extended periods).
  + Highlight trends indicating excessive late-stage changes during critical milestones.
* **Visualization Example:** Trend of CR status over time, displayed as a stacked bar chart or line graph.

---

#### **3. Open vs. Closed Non-Conformances (Defects)**

**What It Measures:** Tracks the number of open (unresolved) vs. closed (resolved) defects related to requirements changes over time.

* **Purpose:** Measures the effectiveness of the change management process in reducing defects and ensures timely closure of issues.
* **SA Focus:**
  + Identify if requirements changes are introducing a disproportionate number of defects, adversely affecting quality.
  + Ensure prompt remediation of non-conformances, particularly for high-priority or safety-critical issues.

---

#### **4. Number of Requirements Issues vs. Resolutions**

**What It Measures:** Tracks the total number of issues (e.g., incorrect, missing, incomplete requirements) versus the number of resolutions over time.

* **Purpose:** Provides insight into the quality of initial and updated requirements and ensures all identified issues are resolved before major milestones.
* **SA Focus:**
  + Monitor resolution rates to ensure problem backlogs are being managed effectively.
  + Highlight persistent issues with requirement clarity that could suggest systemic process gaps.

---

#### **Additional Optional and Extended Metrics**

For projects requiring greater insight into requirements management:

1. **Change Impact Audit Results:** Monitor whether all impacted artifacts related to a requirements change (e.g., design, code, tests) were updated correctly.
2. **Percent of Requirements Tested After Changes:** Ensures updated requirements have been fully validated through testing.
3. **Average Time to Resolve Change-Associated Defects:** Tracks how long it takes to identify, fix, and verify defects caused by changing requirements.

---

**Important Note:**

Metrics displayed in **bold** are **required for all projects** under NASA’s software assurance policies:

* **Software Requirements Volatility**
* **Change Status Trend Over Time**
* **Open vs. Closed Non-Conformances Over Time**

By tailoring these metrics to project size and complexity, software assurance personnel can maintain efficient oversight while proactively identifying risks and driving process improvements.

---

### **Summary**

By monitoring **products** (volatility trends, change management results, defect reports) and leveraging **key metrics**, software assurance provides actionable insights into the requirements change process, ensuring it is well-managed and does not introduce unnecessary risk. These improvements align with NASA’s mission-critical standards for quality, safety, and reliability.

 See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance

Software assurance (SA) plays a critical role in ensuring that requirement changes are effectively managed, implemented, and verified. The SA team evaluates the processes, tools, and outcomes associated with requirements changes to identify risks, ensure traceability, and confirm adherence to standards. Below is a detailed software assurance guidance framework to assist in meeting the goals of Requirement 4.1.5.

Software assurance plays a critical role in ensuring that requirements changes are systematically tracked, analyzed, implemented, and verified. By focusing on process adherence, traceability, safety, testing, and configuration management, SA ensures that projects meet the goals of Requirement 4.1.5 while minimizing project risks and ensuring mission success. This guidance encourages rigor but also adaptability for projects of varying size and complexity.

---

### **1. Ensure a Defined Process for Requirements Change Management**

Software assurance personnel should verify that the project has an established **process for managing requirements changes** that includes the following elements:

* A clear **Change Request Process** for proposing, reviewing, approving, and implementing changes.
* Criteria for evaluating the **impact** of changes on project cost, schedule, and system design.
* Defined roles and responsibilities for reviewing and approving changes (e.g., Change Control Board (CCB)).
* Consistent documentation of changes throughout the lifecycle, including justification, impact analysis, and approval status.

#### **SA Actions:**

* **Review the Requirements Change Control Plan or Procedures:**
  + Check if the plan defines clear steps for identifying, documenting, evaluating, and approving changes.
* **Audit Change Requests (CRs):**
  + Independently review the CRs for proper documentation, including descriptions of the change, rationale, and impact assessment.
  + Verify that each CR has been reviewed and authorized by relevant stakeholders.
* **Ensure Process Compliance:**
  + Evaluate whether the project consistently follows the approved change control process across the software lifecycle.

---

### **2. Assess Impact Analysis for Requirements Changes**

Whenever a requirements change is requested, it is essential that the project team performs an **impact analysis** to evaluate how the change affects the system, software, hardware, testing, cost, schedule, and safety.

#### **SA Actions:**

* **Review Impact Analysis Reports:**
  + Verify that the reports:
    - Address corresponding changes to other requirements, interfaces, and dependencies.
    - Include assessments of the effects on safety-critical systems and hazard controls.
    - Evaluate impacts on the project schedule and cost.
* **Check Consistency:**
  + Ensure that impact analysis has been completed for all proposed requirement changes.
  + Confirm that technical and programmatic risks arising from the changes have been identified and mitigated.
* **Assess Traceability:**
  + Verify that the full scope of the impact (e.g., design documents, test cases, software modules) is reflected in updated requirements traceability matrices.

#### **Best Practice:** Create a checklist for every impact analysis that ensures safety, cost, schedule, and risk impacts have been fully considered.

---

### **3. Verify Bi-Directional Traceability**

Requirement changes must be traced to impacted design elements, source code, test cases, and hazard analyses for both forward and backward traceability. This ensures that changes are properly implemented and all downstream artifacts reflect the latest approved requirements.

#### **SA Actions:**

* **Validate Requirement Traceability:**
  + Ensure updated requirements are:
    - Linked to software design artifacts.
    - Traceable through implementation in the source code.
    - Mapped to test plans and test cases.
  + Confirm that impacted test cases are updated and re-run to verify the implemented change.
* **Verify Traceability Matrices:**
  + Review the traceability matrices for consistency between requirements and downstream products (e.g., design documents, test scripts, verification results).
* **Spot-Check Key Software Work Products:**
  + Independently trace requirement updates to their associated design, code, and test elements to confirm accuracy.

#### **Best Practice:** Include automated tools for managing traceability whenever possible.

---

### **4. Conduct Independent Reviews of Safety-Critical Requirements Changes**

Changes to safety-critical requirements require additional scrutiny, as they can introduce new risks or vulnerabilities. Software Assurance must evaluate these changes to ensure that:

1. All hazards and controls are explicitly addressed and traced.
2. Testing validates safety requirements in both nominal and off-nominal conditions.

#### **SA Actions:**

* **Review Safety-Related Requirements Changes:**
  + Ensure the change request explicitly details how safety is preserved.
  + Verify that revised requirements reflect updated hazard mitigation strategies.
* **Check Validation Testing:**
  + Confirm that any affected safety functionality has been tested under both nominal and failure conditions.
* **Request Additional Analysis When Needed:**
  + If safety-critical requirements are unclear or insufficiently tested, recommend additional fault tree analysis (FTA), hazard analysis, or scenario-based testing.

#### **Best Practice:** Require a documented safety impact assessment for every safety-critical requirements change.

---

### **5. Evaluate the Configuration Management of Change Artifacts**

Software assurance should verify that all artifacts related to requirements changes are maintained in a **configuration management system** (e.g., requirements documents, design changes, test cases, traceability matrices, impact analyses). Configuration-controlled repositories ensure consistency and versioning to avoid errors and rework.

#### **SA Actions:**

* **Verify Configuration Management Policies:**
  + Ensure requirements-related artifacts (e.g., SRS, CRs, test plans) are stored under version control with timestamps, authorship, and approvals clearly documented.
* **Audit Change Records:**
  + Review version history to confirm that updates follow the approved change control process and are synchronized across all repositories.
* **Ensure Evidence for Requirement Closure:**
  + Verify that closure evidence (e.g., test results, validation reports) for updated requirements is stored in configuration-controlled systems for easy retrieval during project reviews (e.g., safety audits, certification reviews).

#### **Best Practice:** Use a single configuration management system to integrate all lifecycle products, minimizing the risk of inconsistency.

---

### **6. Oversee Communication and Coordination**

Effective communication across teams is essential to understanding the implications of a requirements change—especially when working with hardware, software, and operators. Software assurance should oversee this coordination to ensure all stakeholders are aware of updates and their impacts.

#### **SA Actions:**

* **Monitor Stakeholder Involvement:**
  + Ensure that all relevant teams (e.g., hardware, software, safety, operations) review and approve changes that impact their areas.
  + Verify that change notifications are communicated effectively.
* **Evaluate Cross-Disciplinary Coordination:**
  + Confirm that interdependencies between disciplines (e.g., software responding to hardware changes) are accounted for and resolved during impact analysis and implementation.
* **Participate in Change Control Board Reviews:**
  + Attend and review deliberations of the Change Control Board (CCB) to ensure that software-related impacts are evaluated rigorously.

#### **Best Practice:** Document stakeholder feedback and final consensus for all major changes.

---

### **7. Verify Testing for Changed Requirements**

Once a requirement change has been implemented, all related functionality must undergo appropriate verification and validation testing to ensure the updated requirement performs as expected and does not introduce defects.

#### **SA Actions:**

* **Review Updated Test Plans:**
  + Ensure test cases are updated or added to reflect changed requirements, particularly for:
    - Safety-critical functionality.
    - Hardware-software interface changes.
    - Operator interactions.
  + Verify that regression tests are scheduled to ensure no unrelated functionality is broken by the change.
* **Monitor Test Execution:**
  + Confirm that all tests pass criteria related to the change and its downstream impacts.
  + Review test reports for changed requirements, checking for open issues or anomalies.
* **Audit Bug/Defect Tracking:**
  + Ensure issues uncovered during testing are tracked, resolved, and re-tested prior to approval.

#### **Best Practice:** Require that evidence of test completion and success is linked directly to the requirements change in the configuration management system.

---

### **8. Provide Metric-Based Oversight**

Software assurance can use metrics to monitor the effectiveness of requirements change management and identify areas for improvement in tracking, analysis, and implementation processes.

#### Recommended Metrics:

* **Change Request Metrics:**
  + Total number of change requests submitted, approved, and rejected.
  + Percentage of CRs related to safety-critical requirements.
* **Impact Metrics:**
  + Average time to analyze and approve requirements changes.
  + Number of downstream defects introduced as a result of poorly implemented changes.
* **Traceability Metrics:**
  + Percentage of changed requirements with complete forward and backward traceability.
* **Test Coverage Metrics:**
  + Percentage of updated requirements verified through testing.

#### **SA Actions:**

* Collect and analyze metrics on the project’s requirements change process.
* Use the findings to recommend process improvements or identify bottlenecks.

---

### **9. Ensure Compliance with Relevant Standards and Policies**

Software assurance personnel should ensure that requirements change management complies with NASA-specific standards, including:

* **NASA-STD-8739.8:** Software Assurance Standard.
* **NASA-STD-8719.13:** Software Safety.

#### **SA Actions:**

* Conduct audits to assess compliance with these standards during reviews.
* Recommend corrective actions for any identified gaps in requirements change management policies.

Confirm the software requirements changes (e.g., CRs) are documented, tracked, approved, and maintained throughout the project life cycle.

1. Software assurance should analyze all proposed changes for impacts, looking closely at any impacts the change may have in any of the software related to safety or security. The analysis should also consider whether there will be any impacts on existing interfaces or the use of any COTS, GOTS, MOTS, or reused software in the system and whether the change will impact any future maintenance effort. Any identified risks should be brought up in the CCB meeting to discuss approval/rejection of the change.
2. Confirm:

* + That the project tracks the changes

Software assurance will check to see that any changes that are submitted are properly documented and tracked through all the states of resolution (investigation, acceptance/rejection, implementation, test, closure) in the project tracking system.

* + That the changes are approved and documented before implementation

Software assurance should track the changes from their submission to their closure or rejection. Initially, SA should confirm that all changes follow the change management process that the project has established. Initially, the change will be documented and submitted to the authorizing CCB for consideration. The authorizing CCB (which will include a software assurance person) will evaluate any changes for impacts. See [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes).

If the software is safety-critical, the responsible software assurance personnel will perform software safety change analysis to evaluate whether the proposed change could invoke a hazardous state, affect a control for a hazard, condition, or state, increase the likelihood or severity of a hazardous state, adversely affect safety-critical software, or change the safety criticality of an existing software element.  It needs to be kept in mind that changes to the hardware or the software can impact the overall system’s safety and while the focus is on software changes, the software also needs to be aware of changes to the hardware that may impact how software controls, monitors and analyzes inputs from that hardware.  Hardware and software changes can alter the role of software from non-safety-critical to safety-critical or change the severity from moderate to critical.

Some other considerations for the evaluation of changes:

* + - Is the change an error correction or a new requirement?
    - Will the change fix the problem without major changes to other areas?
    - If major changes to other areas are needed, are they specified, and is this change really necessary?
    - If the change is a requirements change, has the new requirement been approved?
    - How much effort will be required to implement the change?
    - If there is an impact on safety or reliability, are there additional changes that need to be made in those areas? Note: If there is a conflict between safety and security, safety changes have priority.

When all the impacts are considered, the CCB votes on acceptance/rejection. Software assurance is a voting member of the CCB.  Software assurance verifies that the decision is recorded and is acceptable, defined as:

- When the resolution is to “accept as is”, verify that the impact of that resolution on quality, safety, reliability, and security is compatible with the Project’s risk posture and is compliant with NPR 7150.2 and other Center and Agency requirements for risk.
- When the resolution is a change to the SW, the change will sufficiently address the problem and will not impact quality, safety, reliability, security, and compliance with NPR 7150.2; the change will not introduce new or exacerbate other, discrepancies or problems.
- In either case, the presence of other instances of the same kind of discrepancy/problem has been sought out and, if detected, addressed accordingly.
- Verify that appropriate software severity levels are assigned and maintained.
- Assure any risk associated with the change is added to the Project/facility risk management system and is addressed, as needed, in safety, reliability, or other risk systems

* + That the implementation of the changes is complete

Software assurance will check to see if the implementation of the approved changes has been coded as per the change request. Check to see that any associated documentation changes are submitted/approved and/made as needed (i.e., updates to requirements, design, test plans/procedures, etc.)

* + That the project tests the changes

Software assurance will check to see that the project test any of the code that has changed and runs a set of regression tests to see that the change has not caused a problem anywhere else in the software system. If the software is safety-critical, a full set of regression tests should be run to ensure that there was no impact on the safety-critical functions.

3. Confirm software changes are done in the software control process

Software assurance will check that the software control process has been followed throughout the handling of the submitted change and that the status of the change is recorded and confirmed as closed.

Develop any issues and concerns from the requirements volatility trending.

Requirements volatility is the change in requirements (added, deleted, and modified) over a given time interval.  The success of software projects is dependent on the quality of requirements. Requirements are the basis for planning project schedules as well as for designing and testing specifications.

Examples:

Software requirements volatility is expected during the early stages of a project (conceptualize / requirements phase). It becomes a concern when it occurs after the software requirements phase (after CDR) is complete because it is likely to result in the re-work of the software components. 

Even though the requirements may be thought of as stable when baselined, some of them may change as the project progresses. Software requirement changes during the software development process are also known as Requirements Volatility.

Requirements volatility has a great impact on the cost, the schedule, and the quality of the final product. Due to requirements volatility, some projects may only be partially completed or even fail. Requirements volatility cannot be fully overcome but can be exposed with some requirement measures or metrics. Requirements volatility metrics could be early indicators of project risks. 

Generally, the software engineers will be producing trend charts of the software volatility. If they are not, the SA personnel should take the software requirements to change data and produce the volatility trend charts. In performing an analysis of the trending data, they should follow the project or SA analysis procedures. As a general guideline, the amount of volatility should be leveling off by the end of the requirements analysis phase. If there is considerable requirements volatility on into development, it is cause for concern. A project that has a lot of requirements volatility when it is nearing a test or delivery period has a major problem. There may be good reasons for this increased volatility (for example, a major design change in a spacecraft), but such a level of change requires careful analysis and probably replanning of activities. The earlier these trends can be identified, the better chance the project has of correcting the problem or replanning to adjust to the requirements changes. 

Requirements evolution is due to factors.

1. External Factors:
   1. Government regulations
   2. project direction and changes
   3. project funding
2. Internal factors
   1. Hardware and interface constraints and unknowns
   2. Lack of experience of the system requirements and software requirements development team
   3. Feedback from milestone reviews and peer reviews
   4. Complexity
   5. Customer, operational, software, and hardware changes
   6. Hazard identifications
   7. Lack of process maturity in requirements generation and requirements management
   8. Requirement or hardware reuse
   9. Environmental changes or mission profile changes
3. Requirements instability (the extent of fluctuation in user requirements)
4. Requirements diversity (the extent to which stakeholders disagree among themselves deciding on requirements).
5. Requirements analyzability (the extent to which the process of producing requirement -specification can be reduced to objective procedure).
6. Poor communication between users and the development team.

Requirements volatility contains schedule, cost, and performance risk factors. Developing and maintaining a trending of software requirements volatility measurements is critical to determine the risks associated with the project.

Requirement volatility is not the only reason contributing to the success of any project, by can be a key indicator in the project risk and success.

Several challenges lead to Requirement Volatility.

1. The change request form was not always complete. A change request form may have little information about the reason for the proposed change.
2. No formal impact analysis and incomplete change effort estimation.
3. Traceability between requirements and other software artifacts is not established. See [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability)

The impact of requirement volatility on the software project has been seen as:

1. Projects Schedule: If the schedule of one activity delays, obviously all subsequent activities schedule will be disturbed.
2. Project Performance: Project performance decreases due to the change in requirements. Requirement Volatility has a high impact on the coding and maintenance phases.
3. Project Cost: Project cost increases due to the change in requirements.
4. S/W Maintenance Project cost increases due to the change in requirements.
5. S/W Quality: Quality of software decreases due to continuous changes in requirements.

Though requirements volatility has an impact on the project schedule, project performance, project cost, software maintenance, and software quality, it may have some positive effects as well as it may help us to have a better understanding of user requirements.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)       * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence is tangible, auditable information that supports compliance with Requirement 4.1.5. It serves as verification that requirements changes are tracked, reviewed, approved, managed, implemented, and validated effectively.

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

Below is a breakdown of **good objective evidence** for this requirement, covering the entire lifecycle of software requirements change management.

---

### **1. Change Request Documentation**

#### Purpose:

Demonstrates that all requests to modify requirements are formally documented, reviewed, and approved before being implemented.

#### Objective Evidence:

* **Change Request Forms (CRs):**
  + Evidence of submitted requests specifying the original requirement, the proposed change, rationale, and impact analysis (e.g., hardware, software, operators, cost, test plans).
* **Change Control Board (CCB) Review Documents:**
  + Meeting minutes showing review, discussion, and approval/rejection of CRs by stakeholders (e.g., project manager, software assurance, hardware and software teams).
* **Change Request Logs:**
  + Complete log of all CRs, including:
    - CR ID.
    - Submission date.
    - Status (e.g., proposed, approved, in implementation, closed).
    - Decision rationale for approval or rejection.

#### Example:

"CR-27: Increase sample rate of Sensor A from 50 ms to 25 ms due to updated hardware capability."

* Documented in CR form with impact analysis (safety, timing, testing), reviewed and approved in the CCB meeting held on [date].

---

### **2. Updated Requirements Specification**

#### Purpose:

Shows that the Software Requirements Specification (SRS) or equivalent document is updated in response to approved changes.

#### Objective Evidence:

* **Updated SRS Document:**
  + Demonstrates that the SRS reflects the approved requirements change, showing before-and-after revisions and version history.
  + Clear versioning with uniquely identified requirements IDs.
* **Change Logs in SRS:**
  + A subsection documenting all changes made, why they were made, and their approval status.
* **Requirements Traceability Matrix Updates:**
  + Shows the updated traceability of changed requirements to design, code, test cases, and hazard analyses.

#### Example:

* SRS Version 2.1, Requirement R-102: "Sensor A sample rate increased to 25 ms, aligned with updated hardware capability (per CCB approval #CR-27)."

---

### **3. Impact Analysis Documentation**

#### Purpose:

Confirms that proposed requirements changes are analyzed thoroughly for technical, programmatic, and safety impacts before approval.

#### Objective Evidence:

* **Impact Analysis Reports:**
  + Detailed analysis addressing:
    - Impact on other requirements (e.g., dependency updates).
    - Impact on hardware, software, safety-critical functionality.
    - Cost, schedule, and resource implications.
    - Risks introduced or mitigated by the change.
* **Hazard Analyses Updated Based on Requirement Changes:**
  + Evidence that the change’s impact on identified hazards and controls has been reviewed and updated.
* **Interdisciplinary Coordination Records:**
  + Emails, meeting notes, or tool-based notifications showing hardware, software, and operator teams have been consulted on impacts.

#### Example:

Impact analysis for CR-27 details how faster sample rates will affect processing speeds, timing constraints, and test coverage. Specific downstream dependencies identified and flagged for updates.

---

### **4. Configuration Management Records**

#### Purpose:

Demonstrates that all artifacts (e.g., requirements, design, code, test plans) affected by the change are adequately tracked and updated in a controlled and traceable manner.

#### Objective Evidence:

* **Configuration Management Repository Logs:**
  + Audit trails from a configuration management system (e.g., Git, DOORS, Cradle) showing who made the change, when, and why the version was updated.
* **History and Version Control of Requirements:**
  + Evidence that the SRS, design, and other documentation reflect requirements changes without introducing inconsistencies.
* **Closure Evidence for Changes:**
  + Evidence that all affected items (e.g., documentation, test artifacts, design models) have been updated in alignment with the approved change.

#### Example:

* Repository log snapshot showing updates to "SRS\_R27.v2.xml" committed on [date] by [developer], tagged with CR-27 and justification.

---

### **5. Requirements Validation and Verification Results**

#### Purpose:

Ensures that requirements changes have been verified and validated through updated test plans and executed test results.

#### Objective Evidence:

* **Test Plan Updates:**
  + Updated testing plans reflecting new, changed, or deleted requirements.
  + Regression test plans to ensure unrelated functionality has not been impacted.
* **Test Results:**
  + Evidence that all affected requirements have been tested successfully (e.g., specific test case IDs, execution logs).
* **Requirement Validation Summary Report:**
  + A summary of how the updated requirement was validated against both functional expectations and project goals.
* **Traceability to Updated Test Cases:**
  + Updated Requirement-to-Test linkage demonstrating comprehensive test coverage of the updated requirement.

#### Example:

Test Plan updated to include a new test case (e.g., TC-57) validating CR-27 for Sensor A's increased sample rate. Execution logs on [date] confirm successful validation.

---

### **6. Risk Management Artifacts**

#### Purpose:

Provides evidence that risks introduced by requirements changes have been identified, mitigated, and tracked over the project lifecycle.

#### Objective Evidence:

* **Risk Register or Database Entries:**
  + Identifies risks introduced by requirements changes (e.g., late-stage updates, safety-critical implications).
  + Documents contingency and mitigation actions.
* **Updated FMEA or Fault Tree Analysis:**
  + Evidence that risks to system reliability, functionality, and safety were analyzed in light of requirement changes.
* **Risk Closure Reports:**
  + Assurance documents showing how risks from requirement updates were addressed successfully.

#### Example:

Risk #105 added to Risk Register: “Increased Sensor A sample rate could introduce timing errors during peak operation.” Actions: (1) Timing analysis, (2) System-wide regression testing.

---

### **7. Metrics Reports**

#### Purpose:

Demonstrates ongoing monitoring of requirements management processes to support project health and highlight bottlenecks, risks, or areas for improvement.

#### Objective Evidence:

* **Requirements Volatility Metrics Over Time:**
  + Charts showing the trend of added, deleted, and modified requirements over key milestones.
  + Measurements of TBD resolutions (e.g., % resolved before PDR or CDR).
* **Change Status Metrics:**
  + Reports or graphs showing how quickly requirements changes are progressing through approval, implementation, and closure phases.
* **Open vs. Closed Non-Conformances Metrics:**
  + Trends to demonstrate timely resolution of defects linked to requirements changes.

#### Example:

Metric chart showing monthly change activity:

* 12 new requirements added, 5 modified, and 2 deleted during Month 4.
* All TBDs resolved before Preliminary Design Review (PDR).

---

### **8. Audit and Review Records**

#### Purpose:

Provides evidence that requirements management processes (including change control) were reviewed, monitored, and aligned with organizational policies and standards.

#### Objective Evidence:

* **Internal Audit Findings:**
  + Evidence from software assurance audits of the change control process.
  + Verifications of compliance with NASA-STD-8739.8 and project-specific requirements standards.
* **External Review Board Reports:**
  + Findings from independent reviews (e.g., safety audits, IV&V reports).
* **Lessons Learned Documentation:**
  + Project records that identify lessons learned connected to requirements changes.

#### Example:

Audit Report: "All 15 submitted changes for Sprint 3 were fully documented, and downstream impacts were traced in DOORS. No deviations from the process were noted."

---

### **Summary**

Good objective evidence for Requirement 4.1.5 makes the case that requirements changes are managed systematically, transparently, and effectively through:

1. Comprehensive documentation.
2. Robust traceability across the lifecycle.
3. Rigorous testing and validation.
4. Continuous monitoring and improvement metrics.

This evidence not only ensures compliance with NASA standards but also mitigates risks to safety, schedule, and mission success.
