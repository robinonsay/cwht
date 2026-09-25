# SWE-024 - Plan Tracking

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695409. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking

SWE-024 - Plan Tracking

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695409)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695409&showCommentArea=true&showComments=true#addcomment)

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

3.1.4 The project manager shall track the actual results and performance of software activities against the software plans.

1. 1. Corrective actions are taken, recorded, and managed to closure.
   2. Changes to commitments (e.g., software plans) that have been agreed to by the affected groups and individuals are taken, recorded, and managed.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-024 History

SWE-024 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.13 The project shall ensure that actual results and performance of software activities are tracked against the software plans. |
| Difference between A and B | "No change in applicability. SWE-025 (a.) and SWE-026 (b.) were rolled into this requirement.  By doing this, it expanded the scope of tracking to include corrective actions and changes in commitments." |
| B | 3.1.3 The project manager shall track the actual results and performance of software activities against the software plans.  a. Corrective actions are taken, recorded, and managed to closure.  b. Changes to commitments (e.g., software plans) are agreed to by the affected groups and individuals. |
| Difference between B and C | No change |
| C | 3.1.4 The project manager shall track the actual results and performance of software activities against the software plans.   1. 1. Corrective actions are taken, recorded, and managed to closure.    2. Including changes to commitments (e.g., software plans) that have been agreed to by the affected groups and individuals. |
| Difference between C and D | Updated part b. of this requirement to take, record, and manage changes in commitments. |
| D | 3.1.4 The project manager shall track the actual results and performance of software activities against the software plans.   1. 1. Corrective actions are taken, recorded, and managed to closure.    2. Changes to commitments (e.g., software plans) that have been agreed to by the affected groups and individuals are taken, recorded, and managed. |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. Rationale

The purpose of this requirement is to determine the status of the project and ensure that the project performs according to plans and schedules, within projected budgets, and that it satisfies technical objectives. This includes redirecting the project activities, as appropriate, to correct identified deviations and variations from other project management or technical processes. Redirection may include replanning as appropriate. The satisfaction of commitments in this plan, as well as subordinate software plans, helps assure that the safety, technical integrity, performance, and mission success criteria for the project will be met.

This requirement ensures **accountability, transparency, adaptability, and alignment** between planned software activities and the actual outcomes during the project execution phase. Tracking software activity performance, executing corrective actions, and managing changes enable the project manager to **navigate deviations, mitigate risks, and maintain project goals** while ensuring all stakeholders are fully informed. The rationale for this requirement is broken down below.

This requirement ensures that **tracking, corrective actions, and recorded changes** form the backbone of project management for aerospace software systems. By continuously monitoring performance against plans, resolving issues, and managing modifications, the project remains aligned with mission objectives while reducing risks and improving operational outcomes. **In high-stakes environments like aerospace, this structured approach is essential to ensuring safety, compliance, and mission success.**

## 2.1 Ensuring Alignment with Software Plans

* **Why It Matters:**
  + Aerospace software development follows meticulously documented plans that outline timelines, resources, deliverables, and compliance requirements. Deviations from these plans—such as delays, defects, resource constraints, or scope changes—can impact mission objectives or safety-critical functions.
  + Periodic tracking of results ensures that outcomes consistently align with goals and that deviations are promptly addressed.
* **Rationale:**
  + Tracking performance against plans ensures the project remains on schedule, within budget, and aligned with mission-critical requirements, reducing the risk of software-related failures.

## 2.2 Enabling Early Identification of Problems

* **Why It Matters:**
  + Without tracking mechanisms, issues such as delays in development, missed functionality, insufficient testing, or resource shortfalls may be discovered too late, leading to costly fixes, untested systems, or delayed certification.
  + Timely detection of discrepancies allows corrective actions—such as modifying plans, reallocating resources, or refining processes—to minimize project disruption.
* **Rationale:**
  + Tracking ensures that problems are identified early, when they are easier and less costly to resolve, rather than during critical later stages where they can jeopardize mission success.

## 2.3 Managing Corrective Actions to Closure

* **Why It Matters:**
  + Corrective actions taken to address issues like unmet milestones, safety-critical failures, or integration challenges must be documented, tracked, and resolved fully. Leaving corrective actions unresolved risks:
    - Recurrence of the same issue.
    - A cascading effect where unresolved issues create new problems in subsequent phases (e.g., unverified features causing faults in operational testing).
  + Formal closure of corrective actions ensures accountability and prevents lingering defects or risks.
* **Rationale:**
  + Managing corrective actions to closure demonstrates diligence in problem-solving and risk management, ensuring project leadership and stakeholders have confidence in project execution and completion.

## 2.4 Promoting Accountability and Transparency

* **Why It Matters:**
  + Aerospace projects involve multi-team collaboration with shared responsibilities (e.g., software engineers, hardware teams, cybersecurity specialists). Tracking actual results ensures visibility into progress across teams and facilitates transparent reporting to stakeholders (e.g., leadership, auditors, regulatory agencies).
  + Changes to plans or commitments must be agreed upon by all affected teams and recorded to avoid miscommunication.
* **Rationale:**
  + This requirement ensures that all teams are accountable for their deliverables, promoting better coordination, clearer communication, and improved team performance.

## 2.5 Mitigating Risks

* **Why It Matters:**
  + Deviations from plans can introduce risks to **mission-critical functions, schedules, and budgets.** For example, failure to deliver safety-critical software on time could cause testing delays, certification risks, and compromised mission safety.
  + Tracking allows the project manager to identify and analyze how variances affect risks and execute corrective actions proactively.
* **Rationale:**
  + Risk management becomes more effective with continuous tracking, allowing the project to maintain a standard of safety and reliability necessary for aerospace missions.

## 2.6 Adapting to Changing Conditions

* **Why It Matters:**
  + Aerospace projects often face unforeseen circumstances, such as emerging technical challenges, scope changes, external dependencies (e.g., third-party software delivery delays), or new mission objectives. Rigid adherence to plans without flexibility for adjustments may result in suboptimal outcomes or missed opportunities.
  + Recorded changes ensure plans remain adaptable without compromising other deliverables or commitments.
* **Rationale:**
  + Managing changes to commitments ensures the project remains responsive to evolving needs while maintaining transparency and accountability.

## 2.7 Facilitating Continuous Improvement

* **Why It Matters:**
  + Tracking results and corrective actions provides insights into process inefficiencies, resource constraints, and recurring challenges, enabling the project team to refine and optimize future processes.
  + Recording and analyzing performance data ensures lessons learned during development are available for future missions or phases, fostering improvement.
* **Rationale:**
  + Tracking and corrective action processes lead to continuous improvement, helping to ensure future success in software development and mission execution.

## 2.8 Supporting Certification, Audit, and Compliance

* **Why It Matters:**
  + Aerospace software development must comply with standards like **NASA NPR 7150.2D** [083](#_tabs-<p></p>) **, DO-178C** [493](#_tabs-<p></p>) **, and FAA mandates**, which require detailed documentation of all processes, corrective actions, and changes. Tracking results ensures that:
    - All deviations (e.g., missed test cases, failure to meet functional requirements) are addressed and documented.
    - Auditable records of changes, resolutions, and impacts are available for certification purposes.
  + Changes to software plans must be traceable to demonstrate compliance with tailored rules and prove that deviations were controlled and verified.
* **Rationale:**
  + Tracking enhances compliance with regulatory requirements, ensuring smooth audits, certifications, and safety assurances for mission-critical software.

## 2.9 Protecting Cost and Schedule

* **Why It Matters:**
  + Untracked deviations from software plans—such as delays or scope creep—can lead to unexpected cost increases or schedule overruns. Recording and addressing these variances ensures:
    - Timely corrective actions to prevent lengthy and costly deviations.
    - Accurate updates to planning based on recorded changes for realistic budgeting and scheduling.
* **Rationale:**
  + This requirement ensures that the project stays as close as possible to its planned budget and schedule, minimizing financial risks and delays.

## 2.10 Maintaining Stakeholder Confidence

* **Why It Matters:**
  + Stakeholders, including mission owners, project leadership, and regulatory agencies, depend on accurate project tracking to gauge progress, risk mitigation, and adherence to objectives. Poor tracking or unmanaged corrective actions erodes their confidence and trust.
  + Recording changes shows stakeholders that deviations are being managed effectively, fostering greater transparency and trust.
* **Rationale:**
  + Stakeholder confidence is maintained when project tracking demonstrates accountability, effective responses to deviations, and documentation of all corrective actions and changes.

## 2.11 Key Reasons Why This Requirement Matters

1. **Alignment with Plans:** Tracking ensures project deliverables consistently align with the planned goals and requirements.
2. **Early Problem Detection:** Identifies and resolves issues early, reducing delays and costs.
3. **Accountability:** Holds all project contributors accountable for their deliverables and corrective actions.
4. **Risk Management:** Proactively mitigates risks caused by deviations from the original plans.
5. **Adaptability:** Allows flexibility to adapt plans while maintaining transparency and control.
6. **Compliance:** Demonstrates regulatory compliance through comprehensive documentation of activities, corrections, and plan changes.
7. **Cost and Schedule Protection:** Prevents unanticipated cost overruns or schedule delays by tracking and resolving variances.
8. **Stakeholder Confidence:** Builds trust with stakeholders by showcasing consistent tracking, corrective measures, and decision-making.

# 3. Guidance

The purpose of the Planning Process is to produce and communicate effective and workable project software plans. This process determines the scope of the software management and technical activities, identifies process outputs, software tasks, and deliverables, and establishes schedules for software task conduct, including achievement criteria, and required resources to accomplish the software tasks. The software lead generally has the responsibility for periodically evaluating the cost, schedule, risk, technical performance, and content of the software work product development activity. See also [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans),

The guidelines for different types of software plans are contained in [7.18 – Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance). Whenever baselined software plans (e.g., [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan), [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan), Software Independent Verification and Validation (IV&V) Plan) are changed, previous commitments and agreements are likely to be impacted. Affected parties, whether they are stakeholders or other interested parties, [041](#_tabs-<p></p>) need to be solicited for their concurrence with the new plan. With concurrence comes the commitment to support the revised work plan. Without commitment, the risk arises that not all elements of the work plan will be performed or completed on time. The risk may also occur that customers and stakeholders will not accept the final software work products because they no longer meet customer needs and expectations.

The project is responsible for ensuring that commitments are met throughout the project life cycle.  Tracking results and performance of software activities against software plans, including managing corrective actions and changes to those plans, is the primary method for carrying out that responsibility.

## 3.1 Results and Performance Tracking

The planning and requirements documentation developed during the early phases of the project guides the development of software work products. The project management team and the software development lead work together to construct a work plan that is logical and achievable in the allotted time and budget. During the early phases, key performance factors, schedules, and milestones are composed. As scheduled work is performed the results need to be reviewed to assure conformance with these plans and to assess if the expected performance has been achieved. The CMMI Institute's capability maturity model (*CMMI**®**-DEV*) considers the evaluation of these work activities to be part of its Project Monitoring and Control process.

**CMMI® for Development, Version 1.3**

Project Monitoring and Control - Introductory Notes:   
"A project's documented plan is the basis for monitoring activities, communicating status, and taking corrective action. Progress is primarily determined by comparing actual work product and task attributes, effort, cost, and schedule to the plan prescribed milestones or control levels within the project schedule or work breakdown structure (WBS)."[157](#_tabs-<p></p>)

Per the Lesson Learned **Acquisition and Oversight of Contracted Software Development (1999), Lesson No. 0921**[528](#_tabs-<p></p>), it is important to ensure that software plans go across contract boundaries (as well as memorandums of understanding and other agreements) are adequately tracked by the project.

The project teams can use several tools to develop insight into the progress of the work. For tracking the progress of activities against plans the use of the following tools and techniques could be helpful:

* Charts - comparisons of planned vs. achieved values.
* Documents - statusing the document tree.
* Schedules - baselined, updates, variances.
* Reports - monthly technical, schedule, and cost narratives; performance measures.
* Project integration meetings and telephone conferences - cross-discipline evaluations.
* Test observations - unit test and integration test activities.
* Team meetings - issue (current and forecasted) and problem reporting; resolution options and tracking completion status.

Results and analysis of these tracking activities can serve as the basis for reviews by stakeholders and advocates (see [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review)).

In addition to the software lead, software assurance personnel have a responsibility for this requirement. (see [Tab 7 - Software Assurance](#tabs-7) )

The software development team uses approved engineering processes to achieve specified results and performance. Reviews, audits, and tracking of the actual use of the specified processes by the software development team is a function of software assurance (see [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance)).

## 3.2 Corrective Actions

Often the evaluation of actual results versus expected performance reveals issues, discrepancies, or deviations that need to be corrected. Typically these findings require further evaluations, replanning, and additional time in the schedule to correct. The software development lead must track these issues to closure to ensure the intent of this requirement.

Tools, such as Excel*®*-based checklists, planning, and tracking tools (such as Omniplan*®* and Primavera®),  and/or formal configuration management systems/change control tools, are used to identify, resolve, and track closure discrepancies and other shortfalls to project performance.

It is important to understand that the activities of "identification," "recording," and "tracking to closure" are techniques that the software development engineering team uses to address and satisfy **NPR 7150.2, NASA Software Engineering Requirements [083](#_tabs-<p></p>)**, requirements related to many areas in the project, such as

* life cycle planning ([SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review)),
* requirements development and management ([SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies)),
* configuration management systems ([SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes)), and the
* preparation of documentation to measure and record these activities ([SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository),

Topic [7.18 – Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)). **NPR 7150.2** uses these terms repetitively, but users of this Handbook are expected to use them and interpret them in the context of the SWE guidance being read.

During the software development activity, once a discrepancy is found that meets the criteria for formal reporting, the software development team clearly states the issue, its area of applicability across the software development activity, and the spectrum of relevant stakeholders it involves. As this information is obtained, the issue is documented in the approved process tool or data repository, and an analysis is conducted of the discrepancy. The results of a properly completed analysis provide a clear understanding of the discrepancy and a proposed course of action to further investigate and resolve the discrepancy as necessary. [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) provides specific details for the information needed for documenting a problem report. Occasionally these reviews surface a significant discrepancy between the actual and expected results of an activity. Some discrepancies are a normal part of project development activity and are resolved through the normal course of the scheduled activity. These discrepancies are typically tracked informally until the developers establish a product baseline after which discrepancies/problems are formally tracked (usually in the Problem Report and Corrective Action (PRACA) system) which requires evaluation, disposition, and assurance oversight of the problem. The [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) or the [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) typically defines the level of the discrepancies that are required to be recorded and tracked in the formal tracking systems. Typically a Center has an approved process for PRACA activities. This requirement does not mandate a particular approach or tool as long the key elements of a corrective action activity that are described in the following paragraph are employed.

Once a corrective action activity has been approved and initiated, its progress is reviewed regularly for progress and its use of planned resources. This information is used to assess whether the action itself is on the course or deviating from the expected result.

An important element of the corrective action activity is the proper closeout of the action. After the activity has concluded, or when the discrepancy has been narrowed to within acceptable limits, the closeout is recorded and may include the following information:

* Description of the issue/discrepancy.
* Proposed corrective action, with acceptable limits.
* Actual results/impacts from the effort.
* Listing of required changes to requirements, schedules, and resources, if any, to accommodate the result.
* Signature(s)/concurrence by all relevant stakeholders.

Once the documentation has been completed, it can be entered into a suitable repository or configuration management system.

## 3.3 Commitment Changes

During the software development life cycle, results can deviate from expectations, and funding or workforce levels may be altered.  Baselined requirements (see topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) in this Handbook for phases of the Space Flight Project life cycle at which software plans typically become baselined) changes become necessary based on these and other factors. It may be necessary to update planning documentation and development schedules to account for corrective action activity (see [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes)). Once it becomes clear that plans need to be changed, and/or schedules need to be altered, the software development lead and the relevant stakeholders recommit to these revised plans. The new commitments assure the availability of resources and unified expectations regarding the revised project.

Several avenues exist to obtain a formal commitment to changes in plans. First, the change control process requires formal evaluation and agreement, and signoff by relevant parties. The software development team must involve all the relevant stakeholders and other interested parties through the exercise of its configuration management change control system (see [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes)). Less formal methods may be used, e.g., jointly written and signed memos of understanding between or among the various parties involved. The concurrence and signature to these documents are usually sufficient to provide binding commitments. Finally, organizational policies can also provide the required formality. Software development team organizational charters may require the team to automatically support any changes, subject to resource availability, because of Center, Agency, or national priorities. It is still important for the project and software development teams to strive for concurrence and commitment by the customers and stakeholders to mitigate risks engendered by unhappy and dysfunctional team members.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 – Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Project Monitoring and Control](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Monitoring+and+Control) |

# 4. Small Projects

This requirement applies to all projects regardless of size. It's not unusual for smaller and less critical projects to utilize engineering personnel to fulfill some or all of the assurance duties (rather than personnel from the Center's Safety and Mission Assurance Organization).

Smaller projects may also consider using a work tracking system or configuration management tool that provides automatic notification and tracking when updates to documentation occur and re-baselining is necessary. Several small projects have begun using wikis to create and maintain project documentation. The use of a wiki allows those working on the project to be notified of changes as they occur.

For small projects, applying this requirement effectively involves tailoring the tracking, recording, and change management processes to ensure compliance without adding unnecessary complexity or overhead. Here’s an approach designed to help small projects execute the requirement efficiently:

## 4.1 Simplify Performance Tracking of Software Activities

#### **Objectives**:

* Monitor progress of software activities to ensure alignment with the plans, including development, testing, configuration management, assurance, security, and risk management.
* Compare actual results (e.g., schedules, milestones, defect metrics) to planned expectations at regular intervals.

#### **Steps**:

1. **Understand the Software Plans**:

   * Identify the key software plans for the project (as outlined in Requirement 3.1.3) and their measurable objectives or deliverables.
   * Identify the software activities/tasks that are critical to the project's objectives (development, assurance, testing, etc.).
2. **Define Key Metrics and Milestones**:

   * Use the software plans to define simple, measurable metrics for tracking.
     + Examples:
       - Testing progression: Percentage of test cases executed and passed.
       - Completion of milestones: Number of completed milestones versus planned milestones.
       - Defect trends: Number of defects found and resolved over time.
   * Focus on visible outcomes and critical-path activities to minimize effort.
3. **Implement Lightweight Status Tracking**:

   * Track performance against plans using simple tools:
     + **For scheduling & task progress**: Use a Gantt chart, Kanban board (Trello, Jira), or simple Excel tracking with columns for planned vs. actual progress.
     + **For testing and assurance**: Leverage simple test case management tools or spreadsheets to track test results and defect closure.
     + **For performance metrics**: Consolidate metrics into a single status report.
4. **Schedule Regular Checkpoints**:

   * Conduct frequent but short status checks (weekly/bi-weekly for small projects).
   * Track compliance with milestones, schedules, budgets, and defect metrics.

#### **Tips for Small Projects**:

* Combine status tracking across plans if resources are limited (e.g., develop a single consolidated tracking document covering schedule, testing, risk, and assurance).
* Clearly define who is responsible for tracking, reporting, and documenting progress—this may be the project manager or a small software assurance team.

#### **Outputs**:

* A regularly updated performance tracking document (e.g., an Excel table or simple automated report from project management tools).
* Status updates that indicate alignment with plans or deviations that require attention.

## 4.2 Ensure Corrective Actions Are Managed to Closure

#### **Objectives**:

* Identify deviations from the software plans (e.g., delays, quality issues, missed goals).
* Document, track, and resolve these deviations systematically and efficiently to ensure alignment with overall project goals.

#### **Steps**:

1. **Identify Deviations Early**:

   * During regular checkpoints, compare actual results to planned outcomes/milestones to identify early warnings of delayed progress, unexpected defects, or resource bottlenecks.
   * Common examples of deviations:
     + Missed schedule milestones.
     + High-priority defects found in late-stage testing.
     + Unexpected resource constraints (e.g., developer unavailability).
2. **Decide on Corrective Actions**:

   * Work with the project team to discuss root causes and feasible corrective actions during a short team meeting.
     + Examples of corrective actions:
       - Adding time to milestones or reducing scope to meet schedules.
       - Reallocating resources for high-priority development tasks.
       - Adjusting test strategies to delay non-critical testing.
3. **Record and Track Corrective Actions**:

   * Document each corrective action in a simple issue-tracking tool or spreadsheet with at least the following fields:
     + **Issue/Deviation ID**
     + **Description of Issue** (e.g., “Milestone X delayed by 2 weeks due to testing bottleneck”.)
     + **Proposed Corrective Action**
     + **Responsible Party**
     + **Target Resolution Date**
     + **Status** (Open, In Progress, Closed)
4. **Verify Completion of Corrective Actions**:

   * Add a final checkpoint to verify that the problem was fully resolved and did not cause cascading effects.

#### **Tips for Small Projects**:

* Use simple issue-tracking tools (e.g., Excel or free tools like Trello/JIRA) for corrective actions instead of heavy process-based tools.
* Delegate responsibility for tracking some corrective actions to team members, but ensure the project manager maintains accountability for final resolution.

#### **Outputs**:

* A log of corrective actions tied to performance deviations, with updates indicating closure or ongoing issues.
* A summary report for stakeholders showing discrepancies and resolutions.

## 4.3 Manage Changes to Commitments Effectively

#### **Objectives**:

* Ensure all changes to commitments (e.g., project objectives, software plans, schedules, resources) are agreed upon by all affected teams and stakeholders.
* Record these changes systematically, and maintain up-to-date project documentation as new commitments are made.

#### **Steps**:

1. **Identify Proposed Changes to Commitments**:

   * Common examples of changes include:
     + Plan updates based on stakeholder or customer feedback.
     + Adjustments to schedule milestones.
     + Scope additions or reductions.
2. **Evaluate the Impact of Changes**:

   * Assess how the proposed changes will affect:
     + Milestones and schedules.
     + Budget/resources.
     + Test plans, assurance activities, and project risks.
   * Generate a simple **impact assessment document** for review (use a checklist format for quick analysis).
3. **Seek Agreement From Affected Parties**:

   * Conduct a short meeting or exchange formal communications to ensure all affected stakeholders agree to the changes.
   * Document stakeholder approval to changes (e.g., via signed document, email, or meeting notes).
4. **Record Changes**:

   * Use a **Change Log** to record all changes in one place. Key fields to include:
     + **Change ID**
     + **Proposed Change Description**
     + **Reason for Change**
     + **Impact Summary**
     + **Approval(s)**
     + **Status**
5. **Communicate with the Team**:

   * Inform the development and assurance teams of new commitments and instructions to ensure clear alignment.
6. **Update Related Plans**:

   * Revise the appropriate sections of the software plans to reflect the agreed changes. Ensure the updated plans are re-baselined and communicated to the team.

#### **Tips for Small Projects**:

* For small projects, simplify change management (e.g., combine impact analysis and approval process into a single meeting or email exchange).
* Consider using version control (e.g., SharePoint version history, Git) to track changes for auditable records.

#### **Outputs**:

* A centralized **Change Log** that lists all changes, their impacts, and their approvals.
* Updated versions of relevant software plans that reflect confirmed commitments.

## 4.4 Reporting and Oversight

#### **Key Reporting Practices**:

* Provide summary updates to stakeholders through structured but concise status reports. Reports should include:
  + Overall progress against plans.
  + Key deviations and their resolutions.
  + Changes to commitments and their impacts.

#### **Audit and Compliance**:

* Document all performance tracking, corrective actions, and change management efforts for potential audits or reviews. This can be as simple as consolidating **status reports**, **corrective action logs**, and **change logs** into a single archive.

## 4.5 Lightweight Tools for Small Projects

* **Tracking Progress**: Trello, Jira (free version), Excel.
* **Corrective Actions**: Issue-trackers in Jira, or customized spreadsheets/logs.
* **Change Management**: Google Docs/SharePoint with trackers for approvals.
* **Performance Metrics**: Kanban boards or lightweight Gantt charts.

## 4.6 Example: Consolidated Workflow for Small Projects

#### Weekly Status Workflow:

1. Software plan milestones are tracked using a central checklist.
2. Deviations or issues are discussed in a weekly meeting. Corrective actions are assigned and logged.
3. Any required changes to commitments are evaluated and documented.
4. Status, risks, and plan updates are reported using a lightweight template.

By simplifying and tailoring these practices, small projects can efficiently meet the goals of this requirement while maintaining compliance and focusing on mission-critical outcomes.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-219)

  [IEEE Standard for Software Reviews and Audits](https://ieeexplore.ieee.org/document/4601584 "Click to open in new window")

  IEEE Std 1028, 2008. IEEE Computer Society, NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-277)

  [Software Formal Inspections Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-87399 "Click to open in new window")

  NASA-STD-8739.9, NASA Office of Safety and Mission Assurance, 2013. Change Date:
  2016-10-07, Change Number: 1
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-520)

  [Problem Reporting and Corrective Action System](https://llis.nasa.gov/lesson/738 "Click to open in new window")

  Public Lessons Learned Entry: 738.
* (SWEREF-528)

  [Acquisition and Oversight of Contracted Software Development (1999)](https://llis.nasa.gov/lesson/921 "Click to open in new window")

  Public Lessons Learned Entry: 921,
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database contains the following lessons learned related to planning tracking, corrective actions, and commitment changes: :

* **Acquisition and Oversight of Contracted Software Development (1999), Lesson No. 0921**[528](#_tabs-<p></p>): "The loss of Mars Climate Orbiter (MCO) was attributed to, among other causes, the lack of a controlled and effective process for acquisition of contractor-developed, mission-critical software. NASA Centers should develop and implement acquisition plans for contractor-developed software and this should be described in each Project Implementation Plan. These plans must provide for Software Requirements, Software Management Planning, and Acceptance Testing and assure NASA Center verification of the adequacy of the software design approach and overall contractor implementation throughout the software life cycle.".
* **Probable Scenario for Mars Polar Lander (MPL) Mission Loss (1998), Lesson No. 0938**[529](#_tabs-<p></p>): "Description: Neither the MPL software requirements specification nor the software, subsystem, or system test plans required verification of immunity to transient signals. MPL touchdown sensors generated known transient signals at leg deployment. The full leg deployment test was not repeated after wiring corrections. Tests should be re-run after test deficiencies are corrected or hardware or software is revised unless a clear rationale exists for not doing so. Hardware operational characteristics, including transients and spurious signals, must be reflected in software requirements and verified by test."
* **Problem Reporting and Corrective Action System, Lesson No. 0738**[520](#_tabs-<p></p>): "This Lesson Learned is based on Reliability Practice No. PD-ED-1255; from NASA Technical Memorandum 4322A, NASA Reliability Preferred Practices for Design and Test."
* **Lesson Learned (Starliner CFT):****Risk acceptance must be data‑driven; unexplained anomalies should not be normalized.**

  **Project Context:**  
  Derived from Starliner CFT Investigation.

  **Problem/Observation:**  
  Risk posture shifted toward accepting operation with unexplained behaviors; burden of proof moved to NASA to demonstrate risk instead of the provider proving safety.

  **Contributing Factors:**

  + Repeated acceptance of intermittent or unexplained anomalies without root cause.
  + Insufficient linkage between anomalies and risk registers; limited trend analysis.

  **Impacts:**

  + Recurrence of anomalies, degraded confidence, and late discovery of fault‑tolerance gaps.
  + Increased mission risk during integrated operations.

  **Recommended Practices (Aligned to SWE‑023/024):**

  + Require **root cause, corrective action (RCCA)** closure (or documented risk acceptance with quantified hazard impact).
  + Tie every anomaly to a **risk register item**; maintain trend dashboards with thresholds for escalation.
  + Enforce **Go/No‑Go criteria** that prohibit proceeding with unresolved critical anomalies.

  **Actionable Checks:**

  + RCCA records include verification evidence of fixes.
  + Risk register references anomalies and test data; trends are reviewed at each milestone.
  + Go/No‑Go templates include explicit anomaly disposition criteria.

* **Undefined and Insufficiently Tested Fault Protection**

  **Incident:**  
  Fault protection logic was not fully defined or validated prior to the launch delay, leaving mission‑critical behaviors unverified.

  **Lesson Learned:**

  + **Early Fault Management Definition:** Fault detection, isolation, and recovery logic must be fully specified and integrated into system testing well before ATLO.
  + **Hazard‑Driven Validation:** Fault responses must be validated against hazards and off‑nominal scenarios using high‑fidelity simulations.

  **Implication:**  
  Incomplete fault protection risks spacecraft safety, autonomy, and ability to recover from anomalies during critical mission phases.

* **Insufficient Staffing in Software, GNC, and Systems Engineering**

  **Incident:**  
  Psyche suffered from persistent understaffing in key areas such as flight software, GNC, systems engineering, and V&V. Many roles were filled with inexperienced personnel, with excessive reliance on stretch assignments and limited mentoring.

  **Lesson Learned:**

  + **Adequate Expertise:** Complex missions require experienced staff in critical roles (e.g., Project Chief Engineer, GNC CogE, Fault Protection Lead).
  + **Sustainable Staffing Models:** Workforce planning must account for burnout, skill mix, mentoring, and retention of highly specialized talent.

  **Implication:**  
  Understaffing reduces software quality, increases risk of technical debt, delays development, and undermines mission execution.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Commitments for the resources needed for all levels of testing](https://software.gsfc.nasa.gov/lesson-details/89/). **Lesson Number 89**: The recommendation states: "Plan for and obtain commitments for the resources needed for all levels of testing."
* [Control GN&C algorithm changes with the same rigor as software requirements changes](https://software.gsfc.nasa.gov/lesson-details/111/). **Lesson Number 111**: The recommendation states: "Control GN&C algorithm changes with the same rigor as software requirements changes. The algorithm document needs to baselined and subsequently controlled like any other requirement."
* [Downstream impacts of decisions made early in the development life cycle](https://software.gsfc.nasa.gov/lesson-details/158/). **Lesson Number 158**: The recommendation states: "Fully evaluate downstream impacts of decisions made early in the development life cycle, particularly on testing."
* [Documenting commitment with stakeholders](https://software.gsfc.nasa.gov/lesson-details/166/). **Lesson Number 166**: The recommendation states: "Obtain commitments (e.g., staff, schedule, resources) from stakeholders in writing, and clarify whether the agreement is based on implementation of a requirement, reaching a project milestone, or a specified time frame."

# 7. Software Assurance

**SWE-024 - Plan Tracking**

3.1.4 The project manager shall track the actual results and performance of software activities against the software plans.

1. 1. Corrective actions are taken, recorded, and managed to closure.
   2. Changes to commitments (e.g., software plans) that have been agreed to by the affected groups and individuals are taken, recorded, and managed.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess plans for compliance with NPR 7150.2 requirements, NASA-STD-8739.8, including changes to commitments.

2. Confirm that closure of corrective actions associated with the performance of software activities against the software plans, including closure rationale.

3. Confirm changes to commitments are recorded and managed.

## 7.2 Software Assurance Products

* To comply with this requirement, software assurance personnel provide the following deliverables at regular intervals (e.g., milestone reviews):

  1. **Activity Tracking Reports**:
     + Results of comparisons between planned activities and actual progress, identifying alignment or discrepancies.
  2. **Issue/Corrective Action Reports**:
     + A log of open and closed issues, including evidence for corrective action closures.
  3. **Trend Analysis Reports** (Task 2):
     + Graphical or statistical representations showing trends in issue identification and resolution across time.
     + Recommendations to improve closure rates or address bottlenecks.
  4. **Change Impact Assessment**:
     + Documentation of updates to plans due to project changes (e.g., updated software classification or responsibilities).

## 7.3 Metrics

This requirement specifies that the project manager must track actual results and performance of software activities against the software plans, take corrective actions as needed, and manage changes to commitments. Software assurance (SA) personnel play a critical role in monitoring these processes and ensuring compliance. For SA personnel, metrics provide measurable insights into the effectiveness of performance tracking, corrective action management, and change management processes.

Below is a detailed list of **Software Assurance Metrics** designed to assess compliance, monitor progress, and provide actionable insights for this requirement:

### 7.3.1 Metrics for Tracking Activities Against Software Plans

#### **Metric 1: Plan Adherence Rate**

**Definition**: Percentage of software activities completed on schedule compared to the activities planned in the software development/management plans.

* **Formula**: [ \text{Plan Adherence Rate} = \left( \frac{\text{Number of Activities Completed on Time}}{\text{Total Planned Activities}} \right) \times 100 ]
* **Purpose**:
  + Tracks how closely the project adheres to its planned schedule for software development, assurance, and testing activities.
  + Identifies potential delays in milestones or deliverables.
* **Target**: ≥90% adherence to planned activities.

#### **Metric 2: Milestone Completion Rate**

**Definition**: Percentage of project milestones completed by their scheduled deadlines.

* **Formula**: [ \text{Milestone Completion Rate} = \left( \frac{\text{Number of Completed Milestones}}{\text{Total Scheduled Milestones}} \right) \times 100 ]
* **Purpose**:
  + Reflects overall progress in meeting critical milestones, such as software requirements reviews, design reviews, testing phases, and deployment.
* **Target**: ≥95% completion by scheduled deadlines.

#### **Metric 3: Schedule Deviation Rate**

**Definition**: Percentage of tasks or milestones delayed from their planned schedule.

* **Formula**: [ \text{Schedule Deviation Rate} = \left( \frac{\text{Number of Delayed Tasks/Milestones}}{\text{Total Planned Tasks/Milestones}} \right) \times 100 ]
* **Purpose**:
  + Measures the degree of deviation from project schedules, helping to identify areas that require corrective actions.
* **Target**: ≤10% schedule deviation.

### 7.3.2 Metrics for Corrective Action Management

#### **Metric 4: Corrective Action Closure Rate**

**Definition**: Percentage of identified corrective actions that have been closed successfully.

* **Formula**: [ \text{Corrective Action Closure Rate} = \left( \frac{\text{Resolved Corrective Actions}}{\text{Total Identified Corrective Actions}} \right) \times 100 ]
* **Purpose**:
  + Tracks the efficiency and effectiveness of resolving identified issues or deviations.
  + Indicates whether corrective actions are being managed promptly.
* **Target**: ≥95% corrective actions closed.

#### **Metric 5: Average Corrective Action Closure Time**

**Definition**: Average time it takes to resolve and close a corrective action from the point of identification.

* **Formula**: [ \text{Average Closure Time} = \frac{\text{Total Time Taken for Closure}}{\text{Number of Closed Corrective Actions}} ]
* **Purpose**:
  + Measures how quickly corrective actions are resolved.
  + Identifies bottlenecks in issue management workflows.
* **Target**: Closure within ≤30 days for non-critical issues and within ≤15 days for critical issues.

#### **Metric 6: Recurring Issue Rate**

**Definition**: Percentage of issues or corrective actions that reoccur after being closed.

* **Formula**: [ \text{Recurring Issue Rate} = \left( \frac{\text{Number of Recurring Issues}}{\text{Total Closed Issues}} \right) \times 100 ]
* **Purpose**:
  + Assesses the effectiveness of corrective actions by identifying whether issues are fully resolved or merely mitigated temporarily.
* **Target**: ≤5% recurring issues.

#### **Metric 7: Open Issue Count**

**Definition**: Total number of unresolved issues or corrective actions remaining open at any given point.

* **Formula**: No formula—track the count of open issues in the corrective action log.
* **Purpose**:
  + Reflects the project’s backlog of unresolved issues.
  + Helps SA personnel determine whether the issue resolution process is keeping pace with issue identification.
* **Target**: Aim for <5% of total identified actions remaining open by project completion.

### 7.3.3 Metrics for Change Management

#### **Metric 8: Percentage of Changes Documented**

**Definition**: Percentage of changes to software plans, project commitments, or personnel responsibilities that are fully documented.

* **Formula**: [ \text{Documented Changes Rate} = \left( \frac{\text{Number of Documented Changes}}{\text{Total Changes Identified}} \right) \times 100 ]
* **Purpose**:
  + Ensures accountability and traceability for changes in the project.
  + Measures whether all changes to commitments are recorded properly for visibility and tracking.
* **Target**: 100% of changes need to be documented.

#### **Metric 9: Change Approval Rate**

**Definition**: Percentage of changes to commitments or plans that are approved by affected stakeholders.

* **Formula**: [ \text{Change Approval Rate} = \left( \frac{\text{Changes Approved by Stakeholders}}{\text{Total Proposed Changes}} \right) \times 100 ]
* **Purpose**:
  + Tracks stakeholder engagement in the change management process to ensure acceptance of changes to software plans or commitments.
* **Target**: ≥90% of changes approved.

#### **Metric 10: Revision Compliance Rate**

**Definition**: Percentage of revised project documentation that reflects agreed-upon changes accurately.

* **Formula**: [ \text{Revision Compliance Rate} = \left( \frac{\text{Revised Documents Accurately Updated}}{\text{Total Changed Documents}} \right) \times 100 ]
* **Purpose**:
  + Ensures that updated commitments, plans, and personnel responsibilities are accurately recorded in revised project documentation.
* **Target**: 100% accurate documentation after revisions.

### 7.3.4 Metrics for Trend Analysis

Tracking trends provides insights into project performance over time and helps identify systemic issues related to corrective actions, tracking, and change management.

#### **Metric 11: Total Number of Open Action Items Over Time**

**Definition**: Number of unresolved action items (corrective actions, issues, or concerns) tracked incrementally over time (e.g., per month or milestone).

* **Purpose**:
  + Provides visibility into whether the backlog of unresolved items is growing or shrinking over time.
* **Target**: Consistent reduction in open action items, with no large spikes indicating bottlenecks.

#### **Metric 12: Corrective Action Closure Trend**

**Definition**: Number of corrective actions closed over time, tracked per month or milestone.

* **Purpose**:
  + Provides insight into whether the project is resolving issues proactively or accumulating unresolved actions.
* **Target**: Steady increase in closure rates over time, with 100% closure achieved by project completion.

#### **Metric 13: Issue Identification-to-Resolution Ratio**

**Definition**: Ratio of identified issues or concerns to resolved issues over time.

* **Formula**: [ \text{Issue Resolution Ratio} = \frac{\text{Issues Identified}}{\text{Issues Resolved}} ]
* **Purpose**:
  + Tracks whether the project resolves issues at a rate that matches or exceeds the rate at which new issues are identified.
* **Target**: Ratio ≤ 1 (i.e., more issues resolved than identified).

### 7.3.5 Metrics Reporting

#### Reporting Frequency:

* Metrics should be tracked and reported at regular intervals aligned with the project’s life cycle milestones (e.g., monthly, per milestone review, or during major status meetings).

#### Presentation Formats:

* Use dashboards or reports to present metrics visually, such as:
  + **Graphs** (e.g., bar charts for closure trends or line charts for schedule adherence).
  + **Tables** (e.g., corrective action logs with counts and resolutions).
  + **Scorecards** summarizing metric performance against thresholds/targets.

### 7.3.6 Example Dashboard Template

| **Metric** | **Current Value** | **Target Value** | **Status** |
| --- | --- | --- | --- |
| Plan Adherence Rate | 92% | ≥90% | **On Target** |
| Corrective Action Closure Rate | 87% | ≥95% | **Needs Attention** |
| Average Closure Time (Days) | 18 Days | ≤30 Days | **On Target** |
| Open Issue Count | 7 | <5 Issues | **Needs Attention** |
| Change Approval Rate | 94% | ≥90% | **On Target** |

  

By using these metrics, **Software Assurance** personnel can ensure compliance with this requirement, identify areas for improvement, and provide measurable data to stakeholders to guide decision-making and enhance project success. These metrics emphasize clarity, accountability, and continuous improvement throughout the software development life cycle.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

This guidance aims to strengthen the processes and structure software assurance (SA) personnel use to ensure compliance with this requirement, with a focus on tracking software activities against plans, managing corrective actions, and enforcing accountability throughout the project life cycle. For each task, actionable steps and additional recommendations are provided to enhance effectiveness, ensure traceability, and add value to the project.

### Task 1: Monitoring Activities and Ensuring Proper Tracking Against Plans

#### **Objective**:

Software assurance personnel must verify that the project is adhering to its software management/development plans, tracking progress and activities against these plans, and implementing corrective actions for issues and deviations.

#### **Enhanced SA Actions**:

1. **Review and Understand the Project Plans**:

   * Obtain and review all relevant project plans, including (but not limited to) the **Software Management Plan (SMP**), Development Plan, Software Test Plan, and Configuration Management Plan.
   * Ensure the plans contain:
     + A clear schedule of software activities.
     + Defined responsibilities for personnel.
     + Defined milestones, deliverables, and performance metrics.
   * Identify key software development activities and their expected timelines. Example: Requirements analysis completion (by Milestone A), testing targets, or status reviews.
2. **Monitor Project Progress Against Plans**:

   * Participate in status reviews, scheduling meetings, and milestone reviews to confirm whether activities are on track.
   * Verify actual progress (e.g., completed milestones or deliverables) against planned progress using evidence, such as:
     + Activity completion reports.
     + Test execution/coverage reports.
     + Configuration management records.
   * Document progress gaps, if any, along with potential causes (e.g., resource shortages, unmitigated risks, or process inefficiencies).
3. **Identify Issues and Confirm Corrective Actions**:

   * Review and assess the project’s ability to detect, document, and respond to deviations from the software plans. Examples include:
     + Schedule slippages.
     + Missed quality standards.
     + Incorrect implementation of planned assurance activities.
   * Verify that the project team:
     + Records all issues and concerns in an issue-tracking system.
     + Proposes actual corrective action plans (CAPs) to address root causes of deviations.
   * Ensure corrective actions address **specific root causes**, not just symptoms, and are practical to implement within resource constraints.
4. **Ensure Proper Documentation and Closure of Issues**:

   * Verify that all identified issues/concerns during the reviews (status meetings, milestone reviews, etc.) are:
     + Documented in a project issue/action item log.
     + Tracked explicitly to closure, along with evidence of resolution.
   * Confirm that corrective actions are communicated to all affected stakeholders (e.g., developers, testers, assurance personnel).
5. **Key Outputs for Task 1**:

   * **Review Reports**: Findings from project activity tracking, including documented progress vs. plans, issues, and areas needing corrective actions.
   * **Issue/Action Logs**:
     + A list of issues or gaps identified during the reviews.
     + Status of corrective actions (i.e., open, in-progress, or closed).
   * **Closure Evidence**: Documentation that proves implementation of corrective actions, such as updated code, re-run test results, or changes to the software plan.

### Task 2: Managing and Tracking Corrective Actions and Analyzing Trends

#### **Objective**:

Ensure corrective actions are tracked systematically, verified for implementation, and fully closed with supporting evidence. Detect trends in corrective action throughput over time to assess the project’s ability to resolve issues efficiently.

#### **Enhanced SA Actions**:

1. **Track Corrective Actions and Confirm their Closure**:

   * **Create and Maintain a Corrective Action Log**:
     + Track every corrective action identified, including:
       - A unique ID for each issue.
       - Description of the issue/concern.
       - Defined corrective action plan.
       - Evidence required to confirm closure.
       - Assignment of responsibility for resolution.
       - Target completion date.
     + Simple tools such as spreadsheets, Trello, or Jira can be used.
   * **Verify Evidence of Closure**:
     + Assess the evidence submitted for corrective action closure to confirm that it addresses the root cause.
     + Validate that corrective actions are implemented, such as:
       - Updated test results showing that defect resolutions are verified.
       - Updated plans reflecting revised processes or milestones.
       - Codebase changes for defect fixes, with regression tests passed.
   * **Prevent “Premature Closure”**:
     + Ensure corrective actions are not marked as "closed" without actual evidence that demonstrates implementation and resolution of the problem.
2. **Report and Escalate Critical Issues**:

   * Document and report unresolved or persistently recurring issues and escalate to the project manager if necessary.
   * Provide software assurance’s independent assessment of the risk associated with unresolved corrective actions or delayed responses.
3. **Ensure the Project Responds to Changes**:

   * Validate that any significant changes affecting the project—such as software classification, criticality, personnel assignments, or project commitments—are promptly reflected in the software plans.
   * Confirm that revised plans are communicated to the development team and that the project is tracking activities against the updated plans.
4. **Develop and Analyze Trends Over Time**:

   * Track corrective action trends using the following metrics:
     + **Open Issue Count Over Time**:
       - The total number of open issues at given time intervals.
       - Tracks whether the project is consistently resolving identified issues.
     + **Action Item Completion Rate**:
       - Percentage of resolved corrective actions per time period.
       - Demonstrates closure rate efficiency.
     + **Recurring Issues**:
       - Percentage of issues that reoccur, which may indicate deficiencies in root cause analysis or quality control processes.
   * Analyze trends to identify systemic problems or process delays.
     + Example: A rising trend in open issues over time may indicate resource bottlenecks or weak corrective action tracking mechanisms.
5. **Key Outputs for Task 2**:

   * **Corrective Action Log**: A continuously updated log of all issues, concerns, and resulting corrective actions with current statuses and resolutions.
   * **Trend and Analysis Reports**:
     + Graphs showing open issues, closure rates, and average closure time across milestones.
     + Insights into sustained or recurring challenges.
   * **Change Review Records**:
     + Evidence that changes in project scope, responsibility, classification, or criticality are reflected in revised plans and tracked correctly.

### 7.4.1 Software Assurance Key Deliverables:

To comply with this requirement, software assurance personnel provide the following deliverables at regular intervals (e.g., milestone reviews):

1. **Activity Tracking Reports**:
   * Results of comparisons between planned activities and actual progress, identifying alignment or discrepancies.
2. **Issue/Corrective Action Reports**:
   * A log of open and closed issues, including evidence for corrective action closures.
3. **Trend Analysis Reports** (Task 2):
   * Graphical or statistical representations showing trends in issue identification and resolution across time.
   * Recommendations to improve closure rates or address bottlenecks.
4. **Change Impact Assessment**:
   * Documentation of updates to plans due to project changes (e.g., updated software classification or responsibilities).

### 7.4.2 Summary of Best Practices:

* **Proactively Involve SA in Reviews**: SA personnel should have a standing role in project status meetings, software milestone reviews, and schedule updates.
* **Close the Loop on Corrective Actions**: Confirm corrective actions are fully implemented with evidence and guard against premature closures.
* **Track Progress in Real Time**: Use lightweight tools to maintain up-to-date logs, enabling immediate visibility into project status and risks.
* **Perform Trend Analysis**: Reviewing trends over time helps identify systemic issues, inefficiencies, or areas where corrective action performance can improve.
* **Focus on Communication**: Maintain regular communication with the project management team to ensure that SA findings are acted upon in a timely manner.

This guidance ensures that software assurance personnel remain active participants in tracking project performance, resolving issues, and adapting to changes, ultimately driving software project success through structured and tailored oversight.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.18 – Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

This requirement specifies that the project manager must track the actual results and performance of software activities against the software management/development plans while ensuring issues are addressed with corrective actions, and changes to commitments are managed properly. Software Assurance (SA) personnel must provide objective evidence that validates compliance with these requirements.

Objective evidence consists of **tangible, verifiable artifacts** produced throughout the software life cycle that demonstrate alignment with software plans, the effectiveness of corrective actions, and proper change management practices.

Below is a list of objective evidence items Software Assurance personnel should collect, review, and audit to fulfill this requirement:

## 8.1 Evidence for Tracking Results and Performance Against Plans

### 8.1.1 Progress Reports

* **Description**: Regularly generated reports detailing actual progress versus planned progress for software activities.
* **Examples**:
  + Status reports/milestone reviews documenting completion percentages for planned tasks.
  + Project schedule updates showing adherence to timelines or identifying slippages.
  + Key Performance Indicators (KPIs) such as test coverage rates, milestone completion rates, and defect resolution rates.
* **Purpose**: Demonstrates whether the project is meeting planned activities and maintaining alignment with the software management/development plan.

### 8.1.2 Milestone Review Records

* **Description**: Records from software life cycle milestone reviews that evaluate project progress against plans.
* **Examples**:
  + Meeting minutes from milestone reviews (e.g., Software Requirements Review, Preliminary Design Review, Critical Design Review).
  + Review findings documenting any discrepancies between planned and actual deliverables.
* **Purpose**: Confirms whether each software milestone is completed on time and meets its goals.

### 8.1.3 Schedule Management Records

* **Description**: Evidence that the project tracks and monitors schedules for software activities.
* **Examples**:
  + Updated project schedules (e.g., Gantt charts or task management timelines).
  + Logs of delayed or rescheduled tasks, with explanations and corrective actions planned.
* **Purpose**: Ensures the project tracks its activities closely against the planned timeline.

### 8.1.4 Execution Metrics

* **Description**: Quantitative evidence that tracks measurable software assurance and development activities relative to plans.
* **Examples**:
  + Test execution results showing planned vs. actual test coverage.
  + Resource utilization metrics comparing planned resources (developers, budget, tools) to actual usage.
  + Defect density trends showing progress in meeting quality standards.
* **Purpose**: Verifies performance tracking using measurable indicators derived from software plans.

## 8.2 Evidence for Corrective Actions

### 8.2.1 Corrective Action Tracking Logs

* **Description**: Logs or databases tracking issues identified during reviews or progress checks and any resulting corrective actions.
* **Examples**:
  + Formal issue/corrective action tracking log with fields such as:
    - Issue ID and description.
    - Proposed corrective action and rationale.
    - Assigned personnel and timeline for resolution.
    - Status (Open, In-Progress, Closed) and closure evidence.
* **Purpose**: Demonstrates systematic identification, management, and resolution of issues requiring corrective actions.

### 8.2.2 Evidence of Corrective Action Implementation

* **Description**: Artifacts showing that corrective actions were implemented and tested for effectiveness.
* **Examples**:
  + Updated test results verifying defect resolution.
  + Approved changes to processes or plans (e.g., re-baselined schedules or revised test strategies).
  + Documentation of tools or resources added to mitigate deviations (e.g., adding automated testing tools to improve test coverage).
* **Purpose**: Confirms that corrective actions are not only planned but implemented effectively, with measurable results.

### 8..2.3 Corrective Action Closure Records

* **Description**: Records demonstrating that corrective actions have been resolved and verified to address identified issues.
* **Examples**:
  + Signed closure reports marking issues resolved, with evidence such as:
    - Test results confirming issue mitigation.
    - Development artifacts showing code fixes or updates.
* **Purpose**: Ensures corrective actions are not prematurely closed without proper verification.

### 8.2.4 Root Cause Analysis Reports

* **Description**: Reports showing analyses performed to identify the root cause of deviations or issues and determine appropriate corrective actions.
* **Examples**:
  + Documentation for identifying recurring issues (e.g., systematic process failures).
  + Recommendations and action plans developed from root cause analysis findings.
* **Purpose**: Supports evidence that corrective actions address the origin of a problem rather than treating symptoms.

## 8.3 Evidence for Managing Changes to Commitments

### 8.3.1 Change Management Logs

* **Description**: Logs or records that document all changes made to project commitments (e.g., software plans, responsibilities, or classification).
* **Examples**:
  + Change control records with:
    - Change ID and description.
    - Justification for the change.
    - Approval signatures from affected stakeholders.
    - Implementation status (Open, In-Progress, Closed).
* **Purpose**: Demonstrates that changes are systematically tracked and approved by all affected parties.

### 8.3.2 Impact Assessment Documentation

* **Description**: Records showing the impact of changes to project plans or commitments on schedules, resources, risks, and quality.
* **Examples**:
  + Revised risk assessment logs showing how changes affected project risks.
  + Updated resource allocation reports reflecting adjustments in personnel or tooling due to changes.
* **Purpose**: Ensures the project evaluates impacts of changes before implementing them and maintains visibility across teams.

### 8.3.3 Updated and Approved Plans

* **Description**: Revised versions of software plans that reflect agreed-upon changes to commitments.
* **Examples**:
  + Updated Software Management Plans (SMPs), Test Plans, or Configuration Management Plans showing new schedules or deliverables.
  + Revised Software Assurance Plans accounting for updates to project classification or criticality.
* **Purpose**: Demonstrates that project documentation reflects current commitments and is aligned with changes.

### 8.3.4 Stakeholder Communication Records

* **Description**: Records proving effective communication of changes to all affected stakeholders, including approvals.
* **Examples**:
  + Meeting minutes discussing key changes and their impacts.
  + Signed stakeholder communications validating agreement to changes.
* **Purpose**: Verifies that changes are transparent and agreed upon by all stakeholders.

## 8.4 Evidence for Trend Analysis

### 8.4.1 Issue and Corrective Action Trend Reports

* **Description**: Graphical or statistical reports showing trends in issue identification and resolution over time.
* **Examples**:
  + Charts showing open versus closed actions by month or milestone.
  + Reports highlighting recurring issues or delayed closures.
* **Purpose**: Provides insights into the effectiveness of corrective action management and identifies patterns that may indicate systemic issues.

### 8.4.2 Progress Performance Logs

* **Description**: Logs summarizing project tracking performance metrics over time (e.g., Plan Adherence Rate, Milestone Completion Rate).
* **Examples**:
  + Time-series logs tracking metrics at each status or milestone review.
  + Consolidated reports analyzing deviations and their impacts.
* **Purpose**: Enables SA personnel to monitor the project's ability to maintain consistency in performance tracking and issue resolution.

## 8.5 Auditable Evidence for Compliance

### 8.5.1 Software Assurance Audit Records

* **Description**: Records from internal or external audits verifying that project progress tracking, corrective action management, and change management comply with this requirement.
* **Examples**:
  + Audit checklists validating compliance with software plans and corrective action standards.
  + Findings from **NASA’s Office of Safety and Mission Assurance (OSMA)** audits.
* **Purpose**: Demonstrates third-party verification of compliance.

### 8.5.2 Training Records

* **Description**: Documentation proving SA personnel and project team members are trained to perform tracking, corrective action, and change management tasks effectively.
* **Examples**:
  + Certificates of training completion for SA software assurance tasks.
  + Training session attendance logs for tools or processes (e.g., issue tracking tools, change control practices).
* **Purpose**: Ensures teams have the skills to execute all activities required by the requirement.

## 8.6 Summary of Objective Evidence Categories

| **Category** | **Key Evidence Types** | **Purpose** |
| --- | --- | --- |
| **Tracking Results** | Progress reports, milestone checklists, execution metrics | Monitor adherence to software plans. |
| **Corrective Actions** | Action logs, closure records, root cause analysis | Verify proper management and resolution of issues. |
| **Managing Changes** | Change logs, impact assessments, updated plans | Ensure transparency and traceability of project adjustments. |
| **Trend Analysis** | Issue trends, performance metrics logs | Identify patterns and systemic problems over time. |
| **Audit and Training Records** | Audit results, training certificates | Validate compliance and capability. |

By consolidating and reviewing these artifacts, Software Assurance personnel ensure robust compliance with this requirement and provide auditable evidence that supports project success and accountability.

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
