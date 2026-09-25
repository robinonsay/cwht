# SWE-054 - Corrective Action for Inconsistencies

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695439. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies

SWE-054 - Corrective Action for Inconsistencies

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695439)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695439&showCommentArea=true&showComments=true#addcomment)

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

4.1.6 The project manager shall identify, initiate corrective actions, and track until closure inconsistencies among requirements, project plans, and software products. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-054 History

SWE-054 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.1.2.2 The project shall identify, initiate corrective actions, and track until closure inconsistencies among requirements, project plans, and software products. |
| Difference between A and B | No change |
| B | 4.1.3.2 The project manager shall identify, initiate corrective actions, and track until closure inconsistencies among requirements, project plans, and software products. |
| Difference between B and C | No change |
| C | 4.1.6 The project manager shall identify, initiate corrective actions, and track until closure inconsistencies among requirements, project plans, and software products. |
| Difference between C and D | No change |
| D | 4.1.6 The project manager shall identify, initiate corrective actions, and track until closure inconsistencies among requirements, project plans, and software products. |

## 1.3 Applicability Across Classes

If Class D software is safety-critical, this requirement applies to the safety-critical aspects of the software.

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

Requirements are the basis for a project. They identify the need to be addressed, the behavior of the system, and the constraints under which the problem is to be solved. They also specify the product to be delivered by the software provider. Software project plans describe how the project will create a software product that fulfills those requirements. Any inconsistencies among these three - requirements, project plans, and software products – will most likely result in a product that does not meet its objectives. These inconsistencies are identified and rectified via corrective actions. Corrective actions address not only new or changed requirements, but also failures and defects in the work products (requirements, project plans, and software products). Corrective actions need to be analyzed to determine the impact that the change will have on the work product, related work products, budget, and schedule. Corrective actions need to be tracked until closure to ensure decisions regarding the closure of those actions are followed through and to prevent the problems described in those corrective actions from propagating through the project or recurring.

Identifying and correcting inconsistencies early and continuously means that a project is more likely to produce a result that satisfies the need for which it was established. Identifying and correcting inconsistencies early (rather than later) also reduces overall project cost as inconsistencies will not propagate forward in the project life cycle (which would require rework).

Consistency between software requirements, project plans, and software products is critical to ensuring mission success, preventing costly rework, and mitigating risks to safety, quality, and system performance. Discrepancies among these components can lead to misunderstandings, implementation errors, or operational failures, especially in highly complex or safety-critical NASA systems.

Ensuring that inconsistencies are actively identified, addressed, and tracked to resolution provides a structured approach to aligning stakeholder expectations with the software being developed. It also ensures project commitments (e.g., schedule, resources, and deliverables) are realistic and achievable, which reduces the likelihood of project delays, budget overruns, and system defects.

---

### **Key Supporting Points for the Rationale**

#### **1. Prevention of Integration and System-Level Failures**

* **Why It's Important:** Inconsistencies between requirements, products, and plans can propagate across different system components, leading to failures during integration, testing, or operation. NASA systems often rely on tight coordination between hardware, software, and operations, making alignment a necessity.
* **Example:** If a requirement specifies that a sensor's temperature range is -50°C to +100°C, but a software control module incorrectly implements a narrower range of -40°C to +90°C, it may lead to inaccurate or unsafe system responses in extreme conditions.

#### **2. Avoidance of Costly Rework**

* **Why It's Important:** Undetected discrepancies often result in significant rework, particularly if discovered late in the software lifecycle (e.g., during integration or validation testing). Addressing inconsistencies early minimizes project costs and avoids cascading delays.
* **Example:** A faulty interpretation of a requirement at the design phase could lead to several subsequent iterations of redesign, recoding, and retesting—consuming resources unnecessarily.

#### **3. Alignment of Project Plans with Evolving Requirements**

* **Why It's Important:** NASA projects often involve evolving requirements due to changes in mission objectives, technology shifts, or updated risk assessments. Project plans need to reflect these changes to ensure resource availability, schedule feasibility, and compliance with updated requirements.
* **Example:** If a critical software feature is added mid-project to address a newly identified safety risk, but the project plan is not updated to allocate additional time and resources for its development, it could lead to missed deadlines or insufficient validation.

#### **4. Mitigation of Risks in Safety-Critical Systems**

* **Why It's Important:** Many NASA systems involve safety-critical software. Inconsistencies between requirements (e.g., hazard mitigations), software design, and implementation can lead to catastrophic consequences, such as loss of life, mission failure, or damage to expensive assets.
* **Example:** A disconnect between a hazard control requirement and its software implementation could result in an emergency system failing to activate under unsafe conditions (e.g., an actuator not responding to a stall detection).

#### **5. Ensuring Synchronized Documentation and Communication**

* **Why It's Important:** Accurate and consistent documentation promotes clear communication between teams (e.g., hardware, software, systems engineering). Any misalignment creates confusion, misinterpretation, or redundant work.
* **Example:** A configuration file parameter that is modified after a requirement change must be updated in all associated documents (e.g., software requirements specification, user manual, and test procedures). If this is not done, teams may use outdated information.

#### **6. Alignment with NASA’s System Development Standards**

* **Why It's Important:** NASA’s software and project management standards (e.g., NASA-STD-8739.8) emphasize rigorous control of inconsistencies to ensure traceability and quality across the lifecycle. Inconsistencies undermine traceability, making it difficult to ensure that all requirements are properly implemented and tested.
* **Example:** If verification plans call for a specific software feature that has been re-scoped or eliminated, the test effort might result in unnecessary work or fail to validate current mission-critical functionality.

---

### **Benefits of Enforcing Requirement 4.1.6**

1. **Improved Software and System Quality:**

   * Consistency ensures that the software performs as expected under all conditions, aligns with specifications, and reduces the number of latent defects.
2. **Reduced Risk of Mission Failure:**

   * Aligning requirements, plans, and products minimizes the potential for integration issues, testing failures, or operational mishaps that could lead to mission failure.
3. **Cost and Schedule Control:**

   * Detecting inconsistencies early avoids expensive late-stage rework and helps to keep projects on budget and on time.
4. **Increased Traceability and Accountability:**

   * By tracking inconsistencies and their resolutions, project managers can demonstrate compliance, maintain proper documentation, and improve lessons learned for future projects.
5. **Promotion of Team Collaboration:**

   * Consistency across all project elements fosters a shared understanding among team members, reducing communication gaps and unnecessary conflict during development.

---

### **Summary**

Requirement 4.1.6 ensures that inconsistencies between requirements, project plans, and software products are identified, resolved, and tracked consistently throughout the project lifecycle. This structured approach is crucial for maintaining alignment, ensuring quality, and minimizing risks in safety-critical, mission-critical, or resource-constrained environments.

Tracking and resolving inconsistencies early mitigates risks that could otherwise lead to integration challenges, operational failures, or rework. This requirement supports NASA’s commitment to program excellence, safety assurance, and mission success.

# 3. Guidance

Typically, the corrective action process is described in a plan, such as the software development or software management plan ([5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)) or the Software Assurance Plan ([8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan)). Follow this documented process to capture and track to closure inconsistencies among requirements, plans, and software products.

A recommended practice for this requirement is that all corrective actions be formally submitted with descriptions of the desired modifications to work products. If corrective actions are not documented consistently, they are difficult to analyze and track. A database provides a flexible environment for storing and tracking corrective actions.

See also [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking),

## 3.1 Identify inconsistencies among requirements, project plans, and software products

Suggested activities to identify inconsistencies and ensure that plans and activities or work products remain consistent with requirements, include:

* Review plans, activities, and work products for consistency with requirements and changes made to them.
* Record inconsistencies and their source.
* Initiate and record any necessary corrective actions and communicate results to affected stakeholders.
* Maintaining bidirectional traceability is critical to maintaining consistency between requirements, work products, and plans.
* Identify any changes that should be made to plans and projects resulting from changes to the requirements.

When looking for inconsistencies, consider these "warning signs" or potential causes:

* Unstable requirements.
* Unclear, incomplete, inconsistent, non-cohesive requirements.
* Incomplete project plans or plans developed before requirements stabilize.
* Budgetary issues that result in changes to staff and/or the requirements.
* Inadequate communications among the development team, management, customers, contractors, and other stakeholders.
* Inadequate change or configuration management procedures.
* Inexperienced staff.
* Personnel turnover.

Inconsistencies among plans, requirements, and the resulting software products need to be identified throughout the project life cycle.  One way to ensure this activity is not forgotten is to conduct periodic reviews of requirements to ensure the requirements, project plans, and software products are consistent. See also [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) and [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes), [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements).

At a minimum, project teams need to note which requirements change and where those requirements flow into plans and products so those plans and products can be reconciled with the changed requirements. This needs to be a standard part of the change control process when a change is being evaluated.

Before corrective action can be taken, consider performing an analysis to identify and weigh options when the corrective action is not readily apparent. This analysis could be similar to that used for change requests and problem reports (see [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report)).

Test plans/procedures need to be modified to reflect requirement changes and resulting implementation changes.  Testing of code changes should be conducted, including regression testing.  If the software is safety-critical, a full set of regression tests should be run to ensure that there was no impact on the safety-critical functions.  Refer to Software Assurance section.

## 3.2 Initiate corrective actions and track until closure

Sample corrective actions include:

* Split development into multiple releases, addressing unstable requirements later.
* Use more experienced or senior personnel.
* Stabilize project personnel, i.e., reduce turnover.
* Audit project processes and act on the findings.

**NASA/SP-2016-6105 Rev2, NASA Systems Engineering Handbook**

5.4.1.2.3 Analyze Product Validation Results - Validation Deficiencies  
"Care should be exercised to ensure that the corrective actions identified to remove validation deficiencies do not conflict with the baselined stakeholder expectations without first coordinating such changes with the appropriate stakeholders."[273](#_tabs-<p></p>)

To initiate corrective actions and track them to closure, consider the following for implementation on the project:

* A system or process for entering and tracking corrective actions (e.g., Problem Report and Corrective Action (PRACA), change request/problem reporting system or tool).
* A corrective action review process - typically involves a review panel or board including engineers and assurance personnel (e.g., Configuration Control Board (CCB)).
* A corrective action implementation process, including updates to test procedures and identification of regression tests.
* A time frame for resolution (i.e., number of days or weeks).
* An escalation procedure (e.g., report to Project Manager (PM)).
* A procedure to archive actions and conclusions for reference, and input to future projects.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements) |

# 4. Small Projects

For smaller projects, processes and tools should be scaled appropriately to fit the scope, complexity, and resource availability. While small projects may not have the same resources or risk profile as larger efforts, Requirement 4.1.6 remains essential to ensure alignment between requirements, plans, and products to avoid inefficiencies, errors, or risks to project success.

Here’s a practical and streamlined approach to meeting this requirement for small projects:

---

### **1. Keep the Process Simple**

For small projects, adopt a light and easy-to-follow process to track and resolve inconsistencies. Avoid overcomplicating workflows. Focus on:

* Consistent communication among team members.
* Early detection of discrepancies.
* Prompt corrective actions with minimal backlogs.

#### Recommended Steps:

1. **Define Initial Baselines:**

   * Document your baseline requirements, project plans, and software product definitions at the start of the project.
   * Use simple, consolidated documents (e.g., a single spreadsheet or well-organized document) to track all three elements in one place.
2. **Capture and Update Changes:**

   * Establish a basic process for tracking changes. For example:
     + If project scope, schedule, or resources change, update the project plan.
     + If a requirement is modified, ensure affected software code/modules and test plans are updated.
3. **Regular Reconciliation:**

   * At key project milestones (e.g., design, coding, testing), compare requirements, project plans, and software products for consistency.
   * Address any identified mismatches promptly.

---

### **2. Use Simplified Tools**

Small projects do not always need large-scale requirements management or configuration management tools. Instead, utilize lightweight, readily available tools.

#### Suggested Tools:

* **Spreadsheet Tools** (e.g., Microsoft Excel, Google Sheets):

  + Track requirements, project plans, and software product status in a single shared sheet.
  + Include a column to flag inconsistencies and record resolutions.
* **Document Management Tools** (e.g., Microsoft Word or Google Docs):

  + Maintain simple, version-controlled documents for requirements and project plans.
  + Record change history manually if needed.
* **Free/Low-Cost Issue Trackers** (e.g., Trello, Azure DevOps Free Tier, or Jira Software Free):

  + Use lightweight task management or ticket systems to assign and track corrective actions.

#### Example:

* Create a simple "Inconsistency Tracker" spreadsheet with the following fields:
  + **ID:** Unique identifier for the issue.
  + **Affected Artifact(s):** Indicate whether it affects requirements, plans, or software products.
  + **Inconsistency Description:** Briefly explain the problem.
  + **Corrective Action Needed:** State what needs to be done.
  + **Responsible Individual:** Assign someone to resolve the issue.
  + **Status:** Track the status (open/in-progress/closed).
  + **Date Closed:** Record when the issue was resolved.

---

### **3. Leverage Team Meetings for Collaboration**

For small projects with fewer team members, frequent and focused meetings can effectively identify and resolve inconsistencies.

#### Steps for Team Meetings:

1. **Set an Agenda:**
   * Include time to review alignment between requirements, plans, and products at regular intervals (e.g., weekly/bi-weekly).
2. **Focus on Key Questions:**
   * Are the requirements reflected in the software development?
   * Are the project plans and resources aligned with the latest requirements?
   * Are the test plans updated to reflect the current state of requirements/software?
3. **Track Actions:**
   * Assign action items for inconsistencies raised during the meeting, and update progress in a tracker (e.g., spreadsheet).

#### Example:

An inconsistency is identified during a weekly meeting: A safety-related software feature was deprioritized to save time, but the test plan still includes test cases for it. The team decides to modify the test plan accordingly, and the action is tracked to completion in the "Inconsistency Tracker."

---

### **4. Assign a Single Point of Responsibility**

For small teams, managing corrective actions and discrepancies can be streamlined by having a single individual (preferably the project manager or systems engineer) responsible for ensuring these tasks are completed.

#### Responsibilities of the Assigned Person:

1. Regularly review project artifacts (requirements, plans, and software products) for alignment.
2. Record any identified inconsistencies using the chosen tool (spreadsheet, task tracker, etc.).
3. Assign corrective actions to team members and follow up to ensure resolution.

#### Example:

In a two-person team, the project manager identifies that the software developer misunderstood a newly added requirement. The project manager communicates the issue, clarifies the requirement, and confirms the developer updates the software promptly to avoid delays.

---

### **5. Incorporate Consistency Checks in Reviews**

Small projects may have fewer formal review processes, but consistency checks should be integrated into **lightweight reviews** at key lifecycle checkpoints.

#### Review Points:

1. **Requirements Review:**

   * Conduct an informal review of the requirements baseline to check for clarity, correctness, and completeness.
   * Ensure all project team members agree on the meaning of the requirements.
2. **Milestone Reviews:**

   * For milestones such as design, coding, testing, or delivery, include a "Consistency Check" step:
     + Compare requirements against the developed software.
     + Verify test plans cover all requirements.
     + Check schedules reflect the efforts required for the next phase.
3. **Final Review:**

   * Confirm all inconsistencies are resolved before the project closure or delivery phase.

#### Example:

During the pre-delivery review of a CubeSat software project, the team verifies that the telemetry control feature described in the requirements document is fully implemented and validated in the software and is not flagged as incomplete in the project schedule.

---

### **6. Apply Risk-Based Prioritization**

Small projects may have limited time and resources, so focus on addressing inconsistencies related to **high-risk** areas such as:

* **Safety-Critical Requirements:** Ensure all safety-critical functionality is implemented, tested, and consistent with the requirements.
* **Interfaces:** Verify consistency between software and hardware interfaces to avoid integration issues.
* **Milestone Blockers:** Prioritize fixing issues that block progress to the next phase or milestone.

#### Example:

For a small satellite navigation system, verify that:

1. Requirements specifying hardware communication protocols align with the actual software implementation.
2. Test plans validate that the software correctly interfaces with onboard sensors.

---

### **7. Close the Loop on Corrective Actions**

For every identified inconsistency:

1. **Document the Inconsistency:** Log it in your tracker.
2. **Resolve It:** Assign responsibility and carry out the corrective action.
3. **Close and Verify:** Close the inconsistency only after confirming the corrective action is complete and the artifacts (e.g., requirements, code, tests) are consistent.

#### Example:

An inconsistency is identified between the planned memory usage in the project plan (200 MB) and the current software product (210 MB). The team revises the project plan and confirms the allocated hardware resources can support the updated usage. The issue is logged as resolved in the tracker.

---

### **Summary for Small Projects**

1. **Use Simple Processes and Tools:** Spreadsheets, lightweight trackers, and frequent communication are often sufficient.
2. **Regularly Reconcile Artifacts:** Compare requirements, plans, and products during team meetings or milestone reviews.
3. **Assign Responsibility:** Have one person track and monitor inconsistencies.
4. **Prioritize Risks:** Focus on safety-critical and interface issues.
5. **Verify Fixes:** Ensure every inconsistency is closed and validated.

By using a streamlined and scalable approach, small projects can effectively manage and resolve inconsistencies without imposing unnecessary overhead. This keeps the project aligned, reduces risks, and helps ensure successful delivery, even with limited resources.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-521)

  [Deficiencies in Mission Critical Software Development for Mars Climate Orbiter (1999)](https://llis.nasa.gov/lesson/740 "Click to open in new window")

  Public Lessons Learned Entry: 740.
* (SWEREF-549)

  [Risk Assessment in Software Development Projects](https://llis.nasa.gov/lesson/1321 "Click to open in new window")

  Public Lessons Learned Entry: 1321.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The NASA Lessons Learned database contains the following lessons learned that emphasize the critical importance of ensuring alignment between requirements, plans, and products and the detrimental consequences of failing to address inconsistencies properly:

---

### **1. Risk Assessment in Software Development Projects**

**Lesson Number 1321:**  
*"Uncertainty caused by changing requirements."*

* **Description:**  
  "Even with expert and experienced programmers, each new software program presents technical challenges that must be carefully managed. Changing methodologies and requirements during the design phase introduces additional uncertainty into software development projects. Flexible, adaptive planning and monitoring systems are necessary to ensure alignment and to mitigate risks introduced by evolving requirements."
* **Lesson and Relevance to Requirement 4.1.6:**  
  This lesson emphasizes that evolving requirements (requirements volatility) inherently increase project uncertainty. If changes are not adequately reflected in project plans and software products, inconsistencies arise, resulting in delays, defects, and rework. Ongoing identification and resolution of changes, with traceability to updated plans and products, is essential for reducing ambiguity and uncertainty.
* **Implementation Tip:**  
  Use lightweight risk assessments to evaluate the impact of changing requirements on downstream artifacts and enforce frequent synchronization between requirements, project plans, and implementation details.

---

### **2. Deficiencies in Mission-Critical Software Development for Mars Climate Orbiter (MCO)**

**Lesson Number 0740:**  
*"Inconsistency during development led to loss of mission."*

* **Description:**  
  The root cause of the Mars Climate Orbiter (MCO) mission failure stemmed from a unit inconsistency between the "Sm\_forces" program output files, which reported values in **English units (pounds-force seconds)** instead of the specified **metric units (Newton-seconds)**. This discrepancy was not identified and corrected during the reviews and verification phases, leading directly to the loss of the spacecraft due to navigation errors.
* **Lesson and Relevance to Requirement 4.1.6:**  
  Inconsistencies between system requirements, project plans, and software products can have catastrophic consequences, especially for mission-critical systems. This example highlights the importance of:

  + Conducting proper software reviews and walkthroughs.
  + Verifying compliance with specified requirements throughout the lifecycle.
  + Ensuring **consistent engineering units** are applied in all output, interface, and product definitions to avoid conflicts across teams and systems.
* **Implementation Tip:**  
  For every requirement involving physical or measurable parameters (e.g., units of measure, tolerances, constraints), implement automated **tool-based checks or validation scripts** to ensure consistency. Cross-check critical data interfaces and outputs during all reviews and validation processes.

---

### **3. Requirement Traceability and Testing in the Space Shuttle Program**

**Lesson Number 0100:**  
*"Lack of traceability can cause oversight in verifying critical requirements."*

* **Description:**  
  During the Space Shuttle program, it was noted in several early projects that missed or misaligned requirements created unintended gaps in testing. Safety-critical requirements that lacked clear traceability to validation procedures or software components were sometimes overlooked, leading to incomplete system verification. Establishing **bidirectional traceability** between requirements, project plans, and software verification efforts was introduced as a key mitigation measure.
* **Lesson and Relevance to Requirement 4.1.6:**  
  Establishing bidirectional traceability ensures every requirement is implemented and verified in downstream processes. Discrepancies often occur when testing plans or implementation details do not reflect evolving requirements. Actively reconciling inconsistencies ensures appropriate testing coverage for all system functions.
* **Implementation Tip:**  
  Use a **traceability matrix** for small or large projects, ensuring that all requirements map directly to software components, test plans, and verification artifacts. Continuously validate this matrix for consistency after each major review or change.

---

### **4. Columbia Space Shuttle Accident (2003): Communication and Process Gaps**

**Lesson Number 1122:**  
*"Failure to resolve organizational inconsistencies contributed to the Columbia disaster."*

* **Description:**  
  The Columbia Accident Investigation Board (CAIB) attributed one of the contributing factors of the loss of the Columbia Space Shuttle to **inconsistencies in communication, delayed resolutions of identified risks, and lack of clear accountability in resolving process gaps.** Critical vulnerability assessments were misaligned between engineering reports and decision-making bodies due to differing priorities or incomplete information.
* **Lesson and Relevance to Requirement 4.1.6:**  
  This lesson highlights that resolving inconsistencies between requirements, plans, and products is not simply a technical activity but also requires **effective coordination, accountability, and follow-through** across teams and disciplines. Vague ownership of issues or delays in addressing known inconsistencies can result in catastrophic consequences.
* **Implementation Tip:**  
  Assign **clear accountability** for identifying, documenting, and resolving inconsistencies early. Use simple tools (e.g., checklists, logs, or trackers) to ensure everyone understands who is responsible for each corrective action and tracks each inconsistency until closure.

---

### **5. Navigation Software Lessons from the Galileo Program**

**Lesson Number 0756:**  
*"Unexpected operational scenarios amplified inconsistencies between test plans and real-world use cases."*

* **Description:**  
  The Galileo spacecraft’s navigation software experienced performance issues in early testing because test plans did not account for real-world scenarios. Certain operational use cases deviated from expected test conditions, exposing inconsistencies between initial requirements, the implemented software, and test environments. Overlooked edge cases were traced back to incomplete validation.
* **Lesson and Relevance to Requirement 4.1.6:**  
  Misalignment between test plans (based on project assumptions) and real-world conditions creates vulnerabilities, especially in systems reliant on complex operational scenarios. Requirements and test environments must comprehensively address all expected use cases, including edge cases, to avoid inconsistencies during operational deployment.
* **Implementation Tip:**  
  Regularly validate testing artifacts against updated requirements and project assumptions. Include edge cases, off-nominal conditions, and operational variance in both the requirements definition and test environments.

---

### **6. Early Identification of Volatility in Software Requirements**

**Lesson Number 0991:**  
*"Requirement changes late in the development cycle amplify inconsistencies."*

* **Description:**  
  Multiple NASA projects have identified that **late changes to requirements** significantly increase project risk, especially when updates are not fully reflected in project plans or software products. Requirements affected by late-stage changes may not align with testing, integration, or final validation, resulting in costly rework, defects, or functional discrepancies.
* **Lesson and Relevance to Requirement 4.1.6:**  
  Late-stage requirement revisions are a major source of misalignment between plans and products. Proactively managing **requirements volatility** (including early identification, prioritization, and communication of changes) mitigates inconsistencies. The corrective action process is especially important in smaller teams or faster-paced projects.
* **Implementation Tip:**  
  Use incremental deliveries and **agile practices** (if applicable) to manage evolving requirements and ensure alignment between plans and products through frequent reviews and feedback loops. Ensure the team has a clear change control process to evaluate and incorporate updates systematically.

---

### **Concluding Relevance**

These lessons align with Requirement 4.1.6 by demonstrating the importance of identifying and correcting inconsistencies to prevent mission failures, reduce risk, and ensure alignment between requirements, project plans, and software products. Small projects can extract relevant lessons—like the importance of early traceability, consistency checks, clear ownership, and incremental validations—to mitigate common pitfalls even in simpler or resource-constrained environments.

Applying these historical insights helps reinforce the importance of rigor and vigilance in all stages of the software lifecycle to avoid repeating past mistakes and ensure project success.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-054 - Corrective Action for Inconsistencies**

4.1.6 The project manager shall identify, initiate corrective actions, and track until closure inconsistencies among requirements, project plans, and software products.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Monitor identified differences among requirements, project plans, and software products and confirm differences are addressed and corrective actions are tracked until closure.

## 7.2 Software Assurance Products

Software assurance (SA) plays a critical role in identifying and resolving inconsistencies across the requirements, project plans, and delivered software products. The following SA products ensure systematic monitoring, corrective actions, and alignment:

#### **1. List of Inconsistencies Identified Among Products**

SA identifies discrepancies between the following artifacts:

* Requirements and software designs or implementation.
* Project schedules and product development timelines.
* Test plans and requirements coverage.

**Key Elements:**

* Documented inconsistencies should include the following details:
  + Artifact(s) affected (e.g., SRS, mission schedule, code modules, test cases).
  + Description of the inconsistency (e.g., missing requirement, misalignment between planned and actual effort).
  + Associated risks or impacts (e.g., safety, reliability, missed milestones).
  + Suggested corrective action steps.
  + Assignment of responsibility and tracking to closure.

**Example:**  
*Inconsistency:* Test plan TC-101 references out-of-date metric units for thrust parameters, while the requirements specify updated NASA-mandated units under NPR 7150.2.  
*Risk:* Mismatches could impact system validation.  
*Corrective Action:* Update relevant test cases and validation results traceable to the corrected units.

---

#### **2. Change Management System Results**

* SA reviews change control documentation to ensure requirements changes and associated corrective actions are documented and tracked through the project's **Change Control Board (CCB)**.
* Key outcomes include:
  + Number of submitted change requests (CRs).
  + Status tracking (e.g., *Open, In Review, Approved, Rejected, Done*).
  + Identification of bottlenecks (e.g., delayed approvals or unresolved action items).
  + Closure results, including the successful implementation of corrective actions.

**Example:**  
SA analysis shows that CR-75 addressing inconsistent subsystem allocation plans remains open for 90 days due to missed coordination with external hardware teams. Corrective action initiated to prioritize CCB review.

---

#### **3. Software Problem Reporting or Defect Tracking System Results**

SA uses defect tracking systems to monitor and analyze inconsistencies discovered during development phases. These should include:

* Defects discovered that indicate upstream inconsistencies (e.g., incomplete requirements leading to code implementation errors).
* Trends and patterns in defect occurrence to identify systemic issues.
* Verification that problematic artifacts (e.g., code, test cases) have been updated.

**Example:**  
Defect #128 documents missing test validation for edge cases triggered by late-stage requirements changes. The SA report recommends updates to the Requirements Traceability Matrix (RTM) and additional test case coverage.

---

## 7.3 Metrics

Software assurance relies on key metrics to evaluate how effectively inconsistencies are tracked and resolved, providing actionable insights for process improvement:

#### **Required Metrics:**

1. **# of Corrective Actions (CAs) Raised by SA vs. Total # of CAs:**

   * Tracks the proportion of corrective actions initiated by SA compared to total corrective actions to gauge SA's impact on issue identification.
   * Highlights areas where SA may need to improve issue discovery processes.
2. **Attributes of Each Corrective Action:**

   * *Type*: Requirement-based, implementation-based, schedule-based, etc.
   * *Severity*: High-risk safety-related issues, operational impacts, or low-priority inconsistencies.
   * *Life Cycle Phase Found*: Requirements, design, coding, testing, or maintenance.
   * *# of Days Open*: Tracks resolution time, identifying patterns in delays.
3. **State of Corrective Actions:**

   * Tracks *Open, In Work, Closed* statuses to measure the team's progress over time.
4. **Trend of CA Open vs. Closures Over Time:**

   * Provides insight into whether inconsistencies are being resolved in pace with their discovery.
5. **# of Incorrect, Missing, and Incomplete Requirements vs. Resolved Requirements Issues:**

   * Tracks discrepancies identified in requirements and measures efficiency in resolving them.
6. **Trend of Inconsistencies or Corrective Actions Identified vs. Closed:**

   * Ensures that issues identified during the lifecycle (e.g., scheduling gaps, implementation misalignments) are being resolved at a steady rate.
7. **# of Software Work Product Non-Conformances by Life Cycle Phase:**

   * Tracks phase-specific issues (e.g., design phase incomplete traceability).
8. **Trend of Open vs. Closed Non-Conformances Over Time:**

   * Measures consistency improvements over the lifecycle.

---

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance

#### **Analyzing Project Planning Documents**

SA must consistently analyze project reference documents (e.g., Resource Allocation Plans, Development Schedules, Requirements Specification, and Test Plans) for alignment and gaps.

Items often overlooked:

* **Effort mismatches in schedules:** Confirm that the work effort for each set of requirements corresponds with the resources defined in budgets and timelines.
* **Late integration or hardware purchases:** Check alignment between planned purchases/development schedules and critical need dates for integration tasks.
* **Activity misalignments:** Assurance activities in project plans may not align with key project phases (e.g., validation activities delayed beyond code completion milestones).
* **Lack of coordinated expertise:** Ensure requirements needing cross-discipline expertise (e.g., hardware interfacing or safety-critical analyses) have resources planned and have completed coordination steps with external groups.

---

#### **Proposed Changes Analysis**

For all change requests, SA evaluates the risk and impact, especially with focus on **safety** and **security** considerations:

1. **Safety/Security Impact Analysis:**

   * Assess whether the change introduces hazardous conditions, affects hazard controls, or alters hazard severities.
   * Review impacts on **COTS, GOTS, MOTS systems**, or potential future maintenance challenges.
2. **Interface Impacts:**

   * Evaluate whether proposed changes affect hardware/software interfaces or system-level dependencies.

**Example:**  
Software updating a safety-critical shutdown procedure must consider whether input from updated hardware sensors introduces operational timing risks.

---

#### **Evaluation Checklist:**

* Has the change been properly documented and processed through the project’s CCB?
* Was a safety-critical evaluation conducted for safety-impacting software updates?
* Was the change categorized as an error correction or new requirement?
* Have affected downstream artifacts been updated (e.g., design specs, test cases, operational plans)?
* Has regression testing demonstrated that the change does not introduce new problems?

---

#### **Tracking Changes Through Implementation**

SA ensures changes are:

1. **Properly approved:** Verified through the established change control process, including a SA review during CCB discussions.
2. **Fully implemented:** Code and associated documentation reflect the approved changes.
3. **Tested thoroughly:** Regression tests and validation procedures must confirm no adverse impacts or defects due to the change.
4. **Tracked through closure:** Monitoring all phases, from CR submission to final resolution.

---

#### **Safety Priority in Conflicts:**

For conflicts between safety and security, **safety** considerations should take precedence. These changes must align with the project’s risk profile and NASA directives.

---

## 7.5 Additional Guidance

1. **Documentation Consistency:** Ensure all changes cascade into associated documentation, including requirements, user guides, interface definitions, and test plans.
2. **Regression Testing:** Always conduct regression testing for safety-critical changes to confirm there are no impacts on functionality.
3. **Proactive Coordination:** Collaborate with hardware teams to validate whether hardware changes impact software functionality, especially where safety features are involved.
4. **Software Severity Levels:** Confirm issue severity is appropriately categorized and risks entered into the facility risk management system.

**Implementation Tip:**  
Use lightweight tools to track corrective actions and inconsistencies for small projects while scaling for larger systems. Integrate automated scripts/tools for validation wherever possible.

---

This improved section emphasizes actionable guidance, consistent methodologies, and links corrective actions to metrics tracking, ensuring effective oversight of inconsistencies across the software lifecycle.

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

# 8. Objective Evidence

Objective Evidence

Objective evidence serves as verifiable documentation or data confirming compliance with this requirement. This evidence demonstrates that inconsistencies are identified, corrective actions are carried out, and alignment between requirements, project plans, and software products is maintained throughout the software lifecycle.

---

### **Categories of Objective Evidence**

#### **1. Documentation of Identified Inconsistencies**

Objective evidence must include records showing inconsistencies among requirements, project plans, and software products have been flagged, documented, categorized, and tracked.

**Evidence Examples:**

* **Inconsistency Tracking Logs:**
  + Records showing issues identified, the impacted artifacts (e.g., requirements, test plans, code), and resolution actions. Fields may include:
    - Unique issue identifier (e.g., INC-001).
    - Affected artifacts (e.g., Requirement ID R-103, test case TC-45).
    - Description of inconsistency.
    - Risk assessment (severity and priority).
    - Assigned team or individual for corrective actions.
    - Status (open, under review, implemented, closed).

**Artifacts:**

* A sample entry might state:

  + INC-025: “Mismatch between Requirement R-201 stating output in Newtons and software implementation that reports output in pounds-force. Assigned corrective action to update test cases and align code with specified units.”
* **Meeting Minutes and Logs:**

  + Minutes from review meetings (e.g., requirements review, CCB meetings, milestone reviews) where inconsistencies and corrective actions were discussed. These minutes should document:
    - Identified issues.
    - Responsible party for resolution.
    - Target resolution timeline.
* **Root Cause Analysis Reports:**

  + For major or recurring inconsistencies, evidence of root cause analysis performed (e.g., was the requirement unclear, or project planning insufficient?).

---

#### **2. Corrective Action Records**

Evidence that corrective actions have been defined, assigned, implemented, and tracked to closure.

**Evidence Examples:**

* **Corrective Action Tracker or Database Logs:**
  + Logs that document the lifecycle of corrective actions, from issue identification to closure. Typical fields include:
    - Action ID (e.g., CA-102).
    - Description of the corrective action.
    - Priority/severity level.
    - Owner (person/team responsible for implementation).
    - Action steps required.
    - Status (e.g., Open, In Progress, Resolved, Rejected, Verified, Closed).

**Artifacts:**

* Corrective actions cross-referenced with the inconsistencies they address.
* Documentation that shows actions such as code revisions, test case updates, or plan modifications have been implemented successfully.
* Example entry:

  + CA-102: Resolved inconsistency in timing of testing plans versus software delivery dates by realigning the project schedule with integration dates.
* **Closure Validation Reports:**

  + Evidence that corrective actions were reviewed and tested for effectiveness prior to closure.

---

#### **3. Change Management Artifacts**

Evidence that changes were properly managed through the project’s change control process, ensuring consistency is restored among all affected items (e.g., requirements, plans, code, tests).

**Evidence Examples:**

* **Change Request Forms:**

  + CRs describing the inconsistency, its impact, necessary updates, and approval by the Change Control Board (CCB).
  + Example: *CR-0082: Update subsystem integration plan to address schedule conflict and mitigate risks of late hardware availability.*
* **Change Control Board (CCB) Minutes:**

  + Meeting logs showing that the CCB assessed the impact of changes and approved or rejected proposed solutions.
* **Updated Project Artifacts:**

  + Updated requirements documents, project schedules, test plans, or code repositories reflecting approved changes.
  + Version histories in configuration management systems with comments showing why and how the updates were made.

**Artifacts:**

* Example:
  + In DOORS, Requirement R-103 was updated from “Test telemetry between 5 pm and 6 pm UTC” to “Test telemetry between 4 pm and 5 pm UTC” after approving CR-134.

---

#### **4. Consistency Review Checklists and Reports**

Evidence of regular reviews ensuring alignment between project artifacts, including the resolution of inconsistencies.

**Evidence Examples:**

* **Consistency Review Reports:**

  + Reports from lifecycle reviews (e.g., Preliminary Design Review, Critical Design Review, Test Readiness Review) that confirm alignment between:
    - Requirements and software design.
    - Software design and test cases.
    - Project plans and implementation schedules.
* **Review Checklists:**

  + Checklists used during peer reviews, inspections, or audits to verify consistency, with evidence of completed checks and identified discrepancies.
  + Example checklist item: "Ensure test cases cover all updated requirements and reflect metric unit conversions."

**Artifacts:**

* Completed checklists for items like configuration management, validation processes, or design traceability.

---

#### **5. Traceability Matrix Updates**

Objective evidence must show that inconsistencies are tracked and resolved through the requirements traceability matrix and associated lifecycle artifacts.

**Evidence Examples:**

* **Requirements Traceability Matrix (RTM):**

  + Updated RTM showing bidirectional traceability between:
    - Requirements.
    - System design and implemented software products.
    - Test cases and validation results.
* **RTM Version Control Logs:**

  + Logs showing how the RTM was updated to reconcile new or changed requirements with downstream products.

**Artifacts:**

* For example:
  + Requirement R-045 is labeled as "changed" in the RTM, with updated test cases TC-12 and TC-15 linked after implementation of the corrective action to resolve testing issues.

---

#### **6. Test and Verification Evidence**

Testing ensures inconsistencies have been fully resolved and requirements, plans, and products are aligned.

**Evidence Examples:**

* **Test Reports:**

  + Reports demonstrating successful execution of test cases related to previously inconsistent items.
  + Evidence that all affected artifacts (e.g., updated code, test cases) have been revalidated through regression testing.
* **Defect Closure Records:**

  + Evidence that defects raised from inconsistent requirements, plans, or code were resolved and retested successfully.

**Artifacts:**

* Examples:
  + Automated test results and logs confirming alignment with updated requirements.
  + Updated safety-critical validation reports addressing inconsistent execution of safety-critical tests.

---

#### **7. Metrics Reporting**

Metrics provide evidence of the project's performance in identifying, addressing, and resolving inconsistencies.

**Evidence Examples:**

* **Corrective Action Metrics:**

  + Total number of corrective actions raised, in progress, closed, or overdue.
  + Average resolution time for inconsistencies.
* **Requirements Consistency Metrics:**

  + Number of inconsistencies identified vs. resolved per phase.
  + Ratio of resolved requirements issues to total issues identified (trending over time).
* **Defect and Work Product Metrics:**

  + Trends in discrepancies tracked by life cycle phase.
  + Open vs. Closed inconsistency and defect counts over time.

**Artifacts:**

* Example metric: "98% of identified inconsistencies were resolved prior to Test Readiness Review."

---

### **Summary of Objective Evidence**

Objective evidence for Requirement 4.1.6 supports a comprehensive view of how inconsistencies are identified, tracked, and closed. To ensure compliance, a wide range of auditable artifacts should be collected, including:

1. Inconsistency identification logs and root cause analyses.
2. Corrective action tracking and closure records.
3. Change management records (CRs, CCB minutes).
4. Updated RTM and associated design or test documentation.
5. Test results and regression testing evidence.
6. Metrics to measure the tracking and resolution process.

These artifacts provide clear evidence that the project manager and team systematically work to maintain alignment between requirements, project plans, and software products while addressing any discrepancies effectively and efficiently.

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
