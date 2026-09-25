# SWE-046 - Supplier Software Schedule

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695420. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule

SWE-046 - Supplier Software Schedule

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695420)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695420&showCommentArea=true&showComments=true#addcomment)

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

3.3.3 The project manager shall require the software developer(s) to provide a software schedule for the project’s review, and schedule updates as requested.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-046 History

SWE-046 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.6.2.4 The project shall require the software supplier(s) to provide a software schedule for the project's review and schedule updates as requested. |
| Difference between A and B | No change |
| B | 3.13.3 The project manager  shall require the software supplier(s) to provide a software schedule for the project's review and schedule updates as requested. |
| Difference between B and C | Changed "software supplier(s)" TO "software developer(s)" |
| C | 3.3.3 The project manager shall require the software developer(s) to provide a software schedule for the project's review, and schedule updates as requested. |
| Difference between C and D | No change |
| D | 3.3.3 The project manager shall require the software developer(s) to provide a software schedule for the project’s review, and schedule updates as requested. |

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

Software supplier scheduling activities must be monitored to assure the software work products that are required by a project are produced when they are needed by the project. NASA's insight into a supplier's development schedule provides a view of the software developer's activities and plans. The supplier's schedule allows the software team to determine the expected state of development of the software product. It then serves as a benchmark for measuring supplier accomplishment during regular reviews or formal design reviews. 

The purpose of this requirement and schedule management is to provide the framework for time-phasing, resource planning, coordination, and communicating the necessary tasks within a work effort. Sound schedule management requires the establishment, utilization, and control of a baseline master schedule and its derivative schedules (e.g., software schedules). An Integrated Master Schedule (IMS) provides the framework for time phasing and coordinating all project efforts into a master plan to ensure that objectives are accomplished within project or program commitments.

Schedule management encompasses the development, maintenance, control, and archival of the project schedules. The software schedule constitutes the basis for time phasing and coordinating all program/project software efforts to ensure that objectives are accomplished within approved commitments. Integrated schedules are crucial for all levels of management oversight within NASA and its contractor community. Software schedules contain the necessary tasks and milestones that reflect the total integrated plans for each software component within the program. While it is true that all software work scope must be included within a program IMS, the levels of detail may vary to accommodate the specific management needs established at the program level. Software schedule management entails the creation of a software schedule that contains integrated tasks and milestones for both contractor effort and effort being worked by in-house NASA government personnel.

Regardless of the type of project being implemented, the software schedule must contain data addressing the total scope of work at a consistent level of detail to allow for discrete progress measurement, management visibility, and critical path identification and control. This approach will allow Program and Project Managers greater visibility and capability to adequately plan the necessary resources, and to ensure an adequate budget will be available to accomplish the planned work.

The software schedule is an essential tool for aligning software development activities with broader project goals, achieving milestones, and meeting mission deadlines. Ensuring the development of a clear, accurate, and regularly updated schedule by the software developers allows the project manager and stakeholders to monitor progress, mitigate risks, and adapt to evolving circumstances effectively.

Requiring software developers to provide a schedule for the project and periodic updates facilitates effective project management, oversight, and execution. The software schedule serves as a living document that provides visibility into progress, identifies potential risks, documents dependencies, and enables timely adaptations to changing circumstances. Regular updates empower project managers with real-time insights necessary to keep projects on track while maintaining accountability and alignment with overall mission objectives. This requirement is vital for ensuring the efficient execution and success of NASA software projects.

## 2.1 Key Reasons for Requiring a Project Schedule

### 2.1.1 Coordination Across Teams

* **Why It's Important**: Software development activities are typically one part of a larger project involving multiple disciplines (e.g., systems engineering, hardware development, testing, and operational readiness). A software schedule ensures alignment between teams and avoids mismatches in timelines that can lead to delays or technical issues.
* **How It Helps**: Developers providing the schedule ensures their tasks are properly integrated with the overall project schedule, enabling seamless coordination and collaboration.

### 2.1.2 Monitoring Progress

* **Why It's Important**: A detailed software schedule provides visibility into task completion, milestone achievement, and potential bottlenecks.
* **How It Helps**: The project manager can use the schedule to evaluate whether the software team is meeting deadlines, identify areas that need attention, and ensure progress aligns with expected milestones. Regular updates allow the team to adapt dynamically to evolving timelines or challenges.

### 2.1.3 Risk Identification and Mitigation

* **Why It's Important**: Without a schedule, it can be difficult to assess the impact of risks or delays on the critical path (tasks that directly affect the project’s timeline). A lack of documented timelines increases the risk of unpreparedness, cascading delays, or unresolved dependencies.
* **How It Helps**: Requiring a schedule from the software developers equips the project manager with insights into potential risks early. Regular updates ensure emerging risks (e.g., delays in testing or resource unavailability) are documented and addressed promptly.

### 2.1.1.4 Documentation of Dependencies

* **Why It's Important**: Software development schedules typically include dependencies on external teams (e.g., hardware readiness, data delivery, or external tools/libraries). Failure to track dependencies can lead to miscommunication, delays, or unexpected obstacles.
* **How It Helps**: Developers providing a schedule allows dependencies to be identified, tracked, and actively managed. Updates confirm whether dependent elements are progressing on time or require actions to address delays.

### 2.1.5 Accountability and Performance Management

* **Why It's Important**: A defined software schedule serves as a benchmark for effort and performance tracking. Without this tool, it is difficult to measure progress or hold developers accountable for meeting deadlines.
* **How It Helps**: Requiring software developers to produce and update a schedule helps project managers ensure that developers are delivering tasks in accordance with agreed-upon timelines, fostering accountability and transparency.

### 2.1.6 Effective Resource Allocation

* **Why It's Important**: Software activities require specific resources (e.g., personnel, tools, environments, and budgets). Without a clear schedule, it may be difficult to predict the demand for these resources or identify gaps early.
* **How It Helps**: An updated software schedule empowers the project manager to allocate resources appropriately, shifting priorities or reallocating as needed to prevent delays and ensure timely execution.

### 2.1.7 Adaptability in a Dynamic Environment

* **Why It's Important**: Software projects are dynamic, with changing requirements, technical challenges, or external dependencies often impacting timelines. A static or poorly updated schedule is insufficient for addressing these realities.
* **How It Helps**: By requiring schedules and updates from developers, project managers can adjust plans as new challenges or opportunities arise while keeping the project on track and within scope.

### 2.2 Benefits of Regular Schedule Updates

1. **Real-Time Visibility**:

   * Schedule updates offered upon request keep stakeholders informed of the current status of software tasks, milestones, and dependencies.
2. **Proactive Risk Management**:

   * Updated schedules reflect changes in task sequencing, delays, or resource availability, enabling advanced planning to mitigate risks.
3. **Improved Decision-Making**:

   * A current, accurate schedule allows project managers to make data-driven decisions about resource reallocation, task prioritization, or early intervention where necessary.
4. **Stakeholder Alignment**:

   * Updated schedules ensure that all stakeholders, both internal and external, are working with the same information, fostering collaboration and minimizing miscommunication.
5. **Tracking Changes Effectively**:

   * Updated schedules document changes to timelines or deliverables, creating an auditable record of adjustments made during the project lifecycle.

# 3. Guidance

Effective software scheduling is critical to ensure that project objectives are met while maintaining alignment with broader mission requirements, risk management goals, and resource constraints. The software schedule provides visibility into development activities, dependencies, milestones, and deliverables, enabling the project team to monitor progress, identify risks, and adapt to changes effectively. Below is enhanced guidance for managing software schedules across NASA projects.

A well-defined software development schedule is fundamental to ensuring the project aligns with timelines, milestones, budgets, and mission objectives. By requiring detailed schedules from suppliers, operational linkages with project schedules, and regular updates, NASA can effectively manage risks, address variances, and maintain project oversight. Incorporating best practices for baseline establishment, resource tracking, and contractual flexibility ensures that software schedules remain dynamic tools for achieving mission success. The integration of these practices into the Work Breakdown Structure (**WBS**), SOW, and configuration management systems enhances the project's ability to adapt to changing conditions while maintaining rigorous accountability and progress tracking.

### 3.1 Software Scheduling

### 3.1.1 Linking Software Development Schedules to Project Objectives

Scheduling begins at the project level, aligning objectives with higher-level deliverables as specified in the Work Breakdown Structure (WBS) (see [7.05 - Work Breakdown Structures That Include Software](/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software)). Through iterative refinement, the schedule evolves down to the software development level, detailing the activities and milestones required to deliver the software components outlined in the WBS.

To ensure comprehensive scheduling:

* **Software Deliverables:** The supplier must document descriptions of software versions and their functionalities in the Version Description Document (VDD) and report on development progress in the Software Metrics Report (see [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) and [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report)).
* **Schedule Requirements in SOW:** The contract Statement of Work (**SOW**) must include explicit requirements for the supplier to deliver a complete software development schedule.
  + This schedule must provide sufficient detail for NASA to gain insight into the supplier's progress, risks, and resource allocation (see [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight)).

### 3.1.2 Components of Networked Schedule Data

Networked schedule data provide the foundation for effective project oversight and include:

1. **Activities and Tasks**:
   * A breakdown of all necessary activities and subtasks involved in the software development life cycle.
2. **Dependencies**:
   * Links between activities, including where one activity relies on another for inputs, data, or deliverables.
3. **Milestones and Products**:
   * Documented outputs (e.g., completed modules, tests passed) and key milestones marking development progress.
4. **Activity Duration**:
   * The estimated time required for each activity, enabling accurate predictions of project timelines.

### 3.1.3 Establishing Firm Schedule Estimates

To create reliable schedules:

* Technical requirements must be sufficiently detailed to support accurate activity time estimates.
* The schedule should outline the major development phases, critical milestones, and the critical path (i.e., tasks that directly affect the project's timeline).
* See [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) for best practices on preparing detailed software development schedules.

## 3.2 Linkages Across Schedules

### 3.2.1 Integrating Supplier and Project Schedules

The software schedules provided by the supplier must be linked to the overall project schedule to maintain alignment and ensure technical and programmatic synchronization. Linkages are crucial for:

* **Risk Assessment**:
  + Analyze the supplier schedule for potential risks, such as long-lead hardware procurement, critical path constraints, or limited schedule slack.
* **Resource Allocation**:
  + Use scheduling tools to evaluate resource utilization over time, ensuring feasibility within resource constraints.
  + Resource-loaded schedules allow close tracking of milestones, budgets, and technical deliverables, enabling corrective actions in response to undesirable trends (e.g., cost overruns, unexpected growth in lines of code).

#### 3.2.2 Proactive Schedule Management

An effective scheduling system must:

* Show resource requirements across the development life cycle, allowing adjustments to maintain feasibility.
* Highlight critical paths and tasks, enabling prioritization of key activities and workflows.
* Integrate technical and financial parameters to ensure the project team can monitor cost and effort alongside progress.

## 3.3 Schedule Baseline

### 3.3.1 Establishing and Controlling the Baseline

Once the supplier delivers firm schedule estimates, the project team must baseline the schedule in the project's configuration management system. A baselined schedule serves as the official reference point for tracking progress and managing changes.

Key considerations:

* **Review for Consistency**:
  + Project teams must ensure baselined schedules align with the overarching project schedule, avoiding conflicts or discrepancies.
* **Controlled Updates**:
  + Baselined schedules are updated in the configuration management system only when major changes or schedule variances occur.

## 3.4 Managing Schedule Variance

### 3.4.1 Tracking and Addressing Variance

Schedule variance is a critical measure of whether work is progressing as planned. It reflects the difference between the budgeted cost of work performed (**BCWP**) and the budgeted cost of work scheduled (**BCWS**) at a given point in time (t). Key strategies for variance management include:

1. **Identify Variance Early**:
   * Negative schedule variance (indicating delays) should be flagged in regular reviews.
2. **Utilize Schedule Management Tools**:
   * Employ tools to assess supplier schedules and identify opportunities for corrective action, such as reallocating resources or reprioritizing critical tasks.
3. **Request Updates**:
   * When major planning changes occur, the supplier must provide updated schedules, ensuring the project team has sufficient visibility into adjustments.

### 3.4.2 Flexibility and Updates

Regular schedule submissions and periodic updates must be required in the SOW and maintained throughout the software development life cycle. NASA projects often experience changes in requirements, funding, or scope, necessitating timely updates to maintain coordination and mitigate risks. Contract clauses should specify the ability for NASA to request updates whenever necessary to ensure continued insight into supplier progress.

## 3.5 Ensuring Effective Schedule Management

#### **Key Best Practices**

1. **Detailed Technical Requirements**:
   * Clearly define technical requirements to support accurate scheduling of activities and deliverables.
2. **Frequency of Updates**:
   * Request periodic updates to evaluate progress against the baseline and address schedule shifts caused by external factors or development challenges.
3. **Resource-Loaded Schedules**:
   * Enable tracking of resources, costs, and efforts across the schedule to maintain feasibility and identify potential issues early.
4. **Alignment with Risk Management**:
   * Integrate schedule reviews with risk management tools to ensure that risks affecting the critical path or resource allocation are addressed promptly.
5. **Contractual Flexibility**:
   * Include clauses in the SOW to ensure suppliers provide updates in response to major changes in requirements or project priorities.

## 3.6 Additional Guidance

Additional guidance may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.05 - Work Breakdown Structures That Include Software](/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Contracting](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Contracting) |

# 4. Small Projects

Small projects typically have less complexity, fewer deliverables, and fewer resources but must still adhere to NASA's standards for managing software schedules effectively. For small software projects, the process can be streamlined, balancing the need for rigorous oversight with the realities of a smaller scope and lower risk. Below is tailored guidance for small projects.

Small software projects may operate with reduced scope and lower risk, but they still benefit from structured scheduling and scheduling discipline. By simplifying schedules, maintaining flexibility in reviews and updates, and focusing on milestones and critical path items, small projects can streamline processes while meeting NASA's expectations. Periodic evaluations of software classification and risk levels ensure review frequency remains appropriate, scaling up or down as needed. Tailored approaches for documentation, resource allocation, and schedule management empower small projects to achieve efficiency while maintaining alignment with project-level objectives and deliverables.

Small projects often rely on reduced schedules in terms of granularity, frequency of updates, and review intensity. This reduction is appropriate if the project's software classification level indicates a lower risk to the mission and program (see [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification)). However, even for smaller projects, schedules must ensure transparency, accountability, and mission alignment. Periodic evaluations of classification and risk level may recommend scaling up or down the frequency and detail of schedule reviews over the life cycle.

## 4.1. Software Schedule Creation and Content

### 4.1.1 Simplified Scheduling

For small projects, scheduling can focus on key milestones and deliverables rather than detailing every sub-task. Consider these steps:

* **Scope Definition**:
  + Build the schedule around high-level activities in software development phases (e.g., planning, coding, integration, testing, and delivery).
* **Critical Milestones**:
  + Identify significant milestones such as preliminary design, integration readiness, and testing completion.
* **Dependencies**:
  + Document key dependencies (e.g., hardware readiness, external tools, or other system inputs) in a straightforward manner.
* **Time Estimates**:
  + Include realistic time durations for each activity, emphasizing main tasks rather than granular breakdowns typically found in larger projects.

### 4.1.2 Supplier Deliverables

* Ensure deliverables, such as software versions and functionality descriptions, are incorporated into the schedule using Version Description Documents (**VDD**) and Software Metrics Reports to track progress efficiently (see [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight)).

## 4.2. Linkages to Project-Level Schedules

### 4.2.1 High-Level Alignment

Small software schedules should still integrate with overall project schedules, even if the schedules have fewer components. Key considerations include:

* **Linkages**:
  + Map software milestones to broader project milestones (e.g., system integration, flight readiness).
* **Risk Analysis**:
  + Analyze risks from dependencies (e.g., hardware delays, coding backlogs) that could affect project schedules. While small projects may have fewer risks, the critical path should still be documented.

### 4.2.2 Resource-Loaded Schedules

For small projects, resource loading can be simplified:

* Focus on critical resources such as staffing levels, budgets, and development tools.
* Simplified tools can track costs, staffing, and line-of-code growth without overloading teams with unnecessary technical detail.
* Regularly assess resource constraints, as even small variances may disproportionately affect smaller projects.

## 4.3. Establishing the Schedule Baseline

### 4.3.1 Streamlined Baseline Creation

The baseline schedule serves as the official reference point for tracking progress and changes. For small projects:

* Baseline the schedule as early as possible once major deliverables and time estimates are finalized.
* Ensure updates are only made for significant shifts in project scope, funding, or timeline.

### 4.3.2 Configuration Management Integration

While smaller projects may not require complex configuration management systems, the schedule baseline should still be integrated into lightweight systems or plans that document updates and changes.

## 4.4. Managing Schedule Variance

### 4.3.1 Simplified Tools for Managing Variance

Small projects often lack the resources for managing schedule variances through advanced tools. However:

* Regular reviews of work against the schedule can track variance between planned and actual progress (e.g., delays in coding, testing, or integration).
* Address negative variances promptly to avoid downstream impacts on overall project milestones.
* Small projects should establish informal mechanisms to flag potential schedule risks for early corrective actions.

### 4.3.2 Regular Updates

Updates to the schedule should remain flexible but limited to significant changes. NASA projects often experience changes in requirements or funding; for small projects, updates can usually be requested on a less frequent basis than for larger, riskier projects.

## 4.5. Maximizing Limited Resources

### 4.5.1 Focus Areas for Resource Allocation

Small projects must prioritize the efficient use of resources to avoid bottlenecks. Key considerations include:

* Identify dependencies (e.g., hardware delivery, external teams) early, even if fewer resources are allocated.
* Track key metrics such as budget utilization, staff workload, and testing results to ensure the project remains feasible.

## 4.6. Schedule Reviews

### 4.6.1 Periodic and Event-Driven Reviews

Instead of frequent periodic reviews, small projects can schedule reviews linked to specific milestones or events. For example:

* **Milestone-Based Reviews**:
  + Conduct reviews at critical points (e.g., completion of preliminary design, integration readiness, or testing results) rather than adhering to fixed frequency.
* **Scaling Frequency**:
  + If the project classification or risk level changes, adjust the review schedule accordingly to ensure that risks are addressed.

## 4.7. Evaluating Risk Levels

### 4.7.1 Periodic Classification and Risk Reevaluation

Small projects often have lower inherent risks, but simple periodic evaluations are critical to ensure the project remains within acceptable levels. Over time:

* Confirm that the classification level (see SWE-020) continues to justify reduced oversight.
* Ensure any risks from integration dependencies, testing, or resource constraints are reflected in the schedule.

## 4.8 Best Practices for Small Projects

1. **Simplify Documentation**:
   * Focus on essential milestones, deliverables, and resources rather than creating a full breakdown of all tasks and subtasks.
2. **Leverage Lightweight Tools**:
   * Use simpler project management tools that align with the smaller scope and scale of the project.
3. **Encourage Flexibility**:
   * Maintain adaptability to request updates or changes based on scope shifts, resource availability, or deliverable adjustments.
4. **Focus on Critical Path**:
   * Prioritize tasks on the critical path that directly influence project success, minimizing unnecessary oversight for non-critical tasks.
5. **Minimize Review Overhead**:
   * Conduct milestone-driven reviews without imposing excessive periodic reporting requirements.
6. **Align with Center Procedures**:
   * Adopt NASA Center-specific practices that support tailoring processes to smaller-scale projects.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

**Misalignment with Commercial Vendor Software Capabilities**

**Incident:**  
Misaligned expectations for vendor simulation, interface details, and heritage design significantly delayed testing and integration activities. COVID‑related limitations reduced the required face‑to‑face interaction needed to align on software behaviors.

**Lesson Learned:**

* **Deep Early Integration:** NASA personnel must work side‑by‑side with commercial partners early to align on simulation capabilities, interface assumptions, and development processes.
* **Contractual Clarity:** Software deliverables and testbed capabilities must be unambiguously specified in contracts.

**Implication:**  
Weak alignment with vendor software ecosystems causes delays, rework, and verification gaps that can push missions off launch schedules.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Pressing software schedule and staffing plans too hard](https://software.gsfc.nasa.gov/lesson-details/5/). **Lesson Number 5**: The recommendation states: "Beware of pressing software schedule and staffing plans too hard to help meet competitive cost caps."
* [For an agile development approach, plan for a hardening sprint with any build](https://software.gsfc.nasa.gov/lesson-details/284/). **Lesson Number 284**: The recommendation states: "When using an agile development approach, plan for additional time at the end of the build for a hardening sprint, which can be used for fixing remaining bugs, as well as other technical debt."

# 7. Software Assurance

**SWE-046 - Supplier Software Schedule**

3.3.3 The project manager shall require the software developer(s) to provide a software schedule for the project’s review, and schedule updates as requested.

Software assurance activities for schedule management are vital in ensuring that both the initial software schedule and subsequent updates provide an accurate, realistic, and actionable plan for software development. By focusing on areas such as schedule validation, risk analysis, metrics tracking, and variance resolution, software assurance supports the project team in maintaining progress, mitigating risks, and achieving milestones. Even for small projects, assurance activities should scale appropriately to ensure software schedules remain transparent, reliable, and responsive to project goals.

See guidance listed in [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) and [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review).

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm the project's schedules, including the software assurance’s/software safety’s schedules, are updated.

## 7.2 Software Assurance Products

Schedule of Software Assurance activities see Objective Evidence in tab  8.

## 7.3 Metrics

Effective monitoring and management of software schedules rely on a set of meaningful and actionable metrics. These metrics help ensure that software schedules are realistic, aligned with project milestones, and adjusted appropriately in response to changes. By tracking these metrics, stakeholders can identify risks early, monitor progress, and assess whether the software development activities are on track.

Below are **good software metrics** tailored to this requirement, organized by specific aspects of schedule management.

### 7.3.1 Schedule Planning and Tracking Metrics

#### 7.3.1.1 On-Time Task Completion Rate

* **Definition**: The percentage of scheduled tasks completed within their planned durations.
* **Purpose**: Provides insight into the team's ability to adhere to scheduled timelines and identifies tasks that are delayed.
* **Formula**:

  ```
  On-Time Task Completion = (Number of Tasks Completed On Time / Total Number of Completed Tasks) × 100
  ```
* **Acceptance Criteria**: A higher percentage indicates better adherence to the schedule (target typically >90%).

#### 7.3.1.2 Milestone Performance Index (MPI)

* **Definition**: Tracks how well milestones are being achieved according to the planned schedule.
* **Purpose**: Examines whether key project milestones are achieved on time, providing insight into overall progress.
* **Formula**:

  ```
  MPI = (Number of Achieved Milestones / Total Scheduled Milestones To-Date) × 100
  ```
* **Acceptance Criteria**: Close to 100%, with tolerance for minor delays (may differ based on project criticality).

#### 7.3.1.3 Activity Tracking Metric

* **Definition**: Tracks the ratio of completed tasks or activities within a specific time period against planned activities.
* **Purpose**: Enables the project manager to monitor day-to-day or week-to-week adherence to detailed phases or tasks within the schedule.
* **Formula**:

  ```
  Activity Tracking Ratio = Completed Activities / Planned Activities
  ```
* **Acceptance Criteria**: Maintain positive trends (ratio greater than or equal to 1 over time).

#### 7.3.1.4 Schedule Growth

* **Definition**: Measures increases in the total project duration over time due to schedule changes (e.g., added activities, delayed milestones).
* **Purpose**: Highlights how much the project schedule is extending beyond the original baseline.
* **Formula**:

  ```
  Schedule Growth (%) = ((Current Project Duration - Baseline Duration) / Baseline Duration) × 100
  ```
* **Acceptance Criteria**: Small projected growth (target <10%, depending on project constraints).

#### 7.3.1.5 Critical Path Completion

* **Definition**: Tracks progress on critical path activities that directly impact the overall project timeline.
* **Purpose**: Ensures the critical path stays on track to avoid delays in final delivery.
* **Formula**:

  ```
  Critical Path Progress (%) = (Number of Critical Path Tasks Completed / Total Critical Path Tasks) × 100
  ```
* **Acceptance Criteria**: Sufficient to meet overarching project milestones without delays in the final timeline.

### 7.3.2 Risk and Variance Management Metrics

#### 7.3.2.1 Schedule Variance (SV)

* **Definition**: The difference between the work that was planned to be completed (BCWS) and the work that was actually completed (BCWP).
* **Purpose**: Helps determine whether the project is ahead of or behind schedule.
* **Formula**:

  ```
  SV = BCWP - BCWS
  ```

  Where:
  + BCWP = Budgeted Cost of Work Performed (earned value of the work completed).
  + BCWS = Budgeted Cost of Work Scheduled (value of planned work at point *t*).
* **Acceptance Criteria**:
  + SV ≥ 0 indicates the project is on or ahead of schedule.
  + A significantly negative SV indicates potential risks requiring corrective action.

#### 7.3.2.2 Schedule Performance Index (SPI)

* **Definition**: A measure of schedule efficiency, capturing how effectively planned activities are completed.
* **Purpose**: Indicates how well the team is staying on schedule.
* **Formula**:

  ```
  SPI = BCWP / BCWS
  ```
* **Acceptance Criteria**:
  + SPI ≥ 1 indicates work efficiency is equal to or better than planned.
  + SPI < 1 may indicate delays or inefficiencies.

#### 7.3.2.3 Risk Exposure Due to Schedule Compression

* **Definition**: The percentage of tasks on accelerated or compressed timelines that are considered high risk.
* **Purpose**: Tracks the number of high-risk schedule adjustments (e.g., overlapping tasks, reduced buffers) to help manage risks from aggressive scheduling.
* **Formula**:

  ```
  Risk Exposure (%) = (High-Risk Compressed Tasks / Total Tasks) × 100
  ```
* **Acceptance Criteria**: Minimized schedule risks (<10% of total tasks, depending on project scope).

### 7.3.3 Resource and Efficiency Metrics

#### 7.3.3.1 Resource Availability vs. Allocation

* **Definition**: Monitors whether the personnel and tools/resources required for task completion are fully available and allocated.
* **Purpose**: Ensures availability of resources aligns with schedule demands and avoids resource-based delays.
* **How to Measure**: Compare actual availability of staff and tools vs. planned allocations for a given time period.
* **Acceptance Criteria**: Minimal discrepancies; resource shortages must be resolved promptly.

#### 7.3.3.2 Effort Deviation

* **Definition**: Measures differences between the time estimated for a task and the actual time spent on its completion.
* **Purpose**: Provides insight into the accuracy of time estimates and helps refine future planning.
* **Formula**:

  ```
  Effort Deviation (%) = ((Actual Effort - Estimated Effort) / Estimated Effort) × 100
  ```
* **Acceptance Criteria**: Deviations should remain within allowable thresholds (e.g., ±10-20%).

### 7.3.4 Software-Specific Metrics

#### 7.3.4.1 Lines of Code Growth (% Growth)

* **Definition**: Tracks the change in the estimated total number of lines of code (LOC) over time as software requirements evolve.
* **Purpose**: LOC growth impacts overall schedule and resource allocation.
* **Formula**:

  ```
  LOC Growth (%) = ((Current LOC Estimate - Baseline LOC Estimate) / Baseline LOC Estimate) × 100
  ```
* **Acceptance Criteria**: Small growth (e.g., <10%) unless justified by new requirements or features.

#### 7.3.4.2 Testing Progress

* **Definition**: Tracks the percentage of planned software tests that are completed over time.
* **Purpose**: Ensures testing milestones remain aligned with the broader schedule.
* **Formula**:

  ```
  Testing Progress (%) = (Tests Completed / Total Tests Planned) × 100
  ```
* **Acceptance Criteria**: Sufficient progress to meet overall integration and delivery deadlines.

### 7.3.5 Communication Metrics

#### 7.3.5.1 Update Frequency

* **Definition**: The percentage of schedule updates delivered by the supplier within the requested timeframe.
* **Purpose**: Monitors the timeliness and responsiveness of schedule updates.
* **Formula**:

  ```
  Update Delivery Timeliness (%) = (On-Time Updates / Total Updates Requested) × 100
  ```
* **Acceptance Criteria**: High compliance (target: ≥90%).

### 7.3.6 Key Takeaways

* **Balance Simplicity and Insight**: Choose metrics that align with the project size and scope. For small projects, focus on fewer critical metrics (e.g., on-time task completion, SPI, and milestones).
* **Automate Metrics Tracking where Possible**: Leverage scheduling tools to track and report metrics with minimal manual effort.
* **Use Metrics for Decision Support**: Metrics are not just numbers—they should guide decisions, risk mitigation, and corrective actions.
* **Tailor Metrics to Stakeholders**: Ensure that the metrics collected provide actionable insights to both project managers and software developers.

By integrating these metrics effectively into schedule management, NASA projects can ensure greater control, transparency, and confidence in achieving their software and mission objectives.

* Deviations of actual schedule progress vs. planned scheduled progress above defined thresholds.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance

****SWE-046 - Supplier Software Schedule****

**3.3.3 The project manager shall require the software developer(s) to provide a software schedule for the project’s review, and schedule updates as requested.**

Software assurance plays a crucial role in ensuring that the software schedule provides valid, clear, and accurate information about the development activities, milestones, dependencies, and outcomes. It also ensures that risks related to schedule planning, execution, and updates are identified, tracked, and mitigated throughout the project lifecycle. Below is tailored guidance and relevant software assurance activities to support this requirement.

### 7.4.1 Software Assurance Guidance

#### **7.4.1.1 Purpose of Software Assurance in Scheduling**

Software assurance ensures resilience and reliability in the schedule management process. By analyzing, validating, and monitoring schedules, assurance activities help minimize risks, identify variances early, and provide confidence in schedule feasibility and alignment with project goals. This includes ensuring the software schedule:

* Reflects realistic timelines for activities and milestones.
* Aligns with technical requirements and project-level schedules.
* Is updated as needed to reflect changes in scope, resources, or risks.
* Allows monitoring of metrics critical to schedule performance and variance.

#### **7.4.1.2 Software Assurance Goals**

1. Validate schedule planning for completeness, accuracy, and alignment with project objectives.
2. Identify and manage risks associated with dependencies, critical paths, and resource constraints.
3. Ensure the delivery of periodic schedule updates and assess their impact on project objectives.
4. Support schedule variance tracking to ensure corrective actions are taken when needed.

### 7.4.2 Software Assurance Activities

#### 7.4.2.1 Schedule Development Review

* **Review the Initial Schedule**:

  + Validate that the software schedule includes all required activities, dependencies, milestones, and expected deliverables.
  + Confirm that time estimates for activities are realistic and reflect technical complexity.
  + Ensure schedules are aligned with the **Work Breakdown Structure** (**WBS**) and project-level milestones.
  + Verify the inclusion of the critical path and dependencies clearly documented in the schedule.
* **Assess Resource Allocation**:

  + Confirm that resource requirements (e.g., staff, tools, environments) are accounted for and consistent with project constraints.
  + Evaluate whether resource-loaded schedules enable tracking of workload and budget.
* **Collaborate on SOW Requirements**:

  + Ensure the **Statement of Work** (**SOW**) defines requirements for schedule delivery and periodic updates by the software supplier.

#### 7.4.2.2 Periodic Schedule Updates

* **Schedule Review After Updates**:

  + Validate updates to ensure they reflect realistic adjustments due to changes in scope, timeline, or resources.
  + Assess whether updated schedules include new or modified milestones, dependencies, and risk mitigations.
  + Verify consistency of schedule updates with baselined project schedules stored in configuration management systems.
* **Monitor Critical Path**:

  + Ensure updates address key tasks on the critical path and mitigate any impact on project deliverables.

#### 7.4.2.3 Risk Identification and Mitigation

* **Dependency Risk Analysis**:

  + Identify risks related to dependencies documented in the schedule (e.g., dependence on hardware delivery, external system interfaces).
  + Confirm contingency plans exist for tasks dependent on external teams or long-lead items.
* **Monitor Schedule-Driven Risks**:

  + Track risks impacting schedule feasibility, such as underestimation of task durations, resource constraints, or unanticipated challenges.
  + Recommend adjustments to mitigate risks such as adding schedule buffer or prioritizing tasks on the critical path.

#### 7.4.2.4 Schedule Metrics Validation

* **Validate Metrics Reporting**:

  + Review metrics such as earned value management (EVM), schedule variance, or cost variance to ensure accurate tracking of progress and deviations.
  + Assess whether unexpected growth in technical parameters (e.g., lines of code, testing effort) is reflected in updated schedules and adequately addressed.
* **Monitor Trends**:

  + Analyze trends in schedule performance, including tasks behind schedule, growing resource needs, or delays in integration testing.
  + Support the project team in identifying corrective actions for emerging schedule risks or undesirable trends.

#### 7.4.2.5 Configuration Management and Schedule Baseline

* **Baseline Assessment**:

  + Verify that the baselined schedule matches the project’s configuration management system and reflects accurate deliverables and timelines.
  + Confirm updates to baselines occur only in response to major scope or requirement changes.
* **Change Tracking**:

  + Track changes to the baselined schedule and validate that modifications are documented, justified, and approved.

#### 7.4.2.6 Variance Tracking and Resolution

* **Monitor Schedule Variance**:
  + Review the difference between the **budgeted cost of work performed** (**BCWP**) and the **budgeted cost of work scheduled** (**BCWS**).
  + Verify that the project has systems or tools capable of tracking and reporting schedule variance.
  + Support the software development team in analyzing negative variances and proposing corrective actions.

#### 7.4.2.7 Collaboration with Supplier

* **Supplier Schedule Insight**:

  + Provide assurance activities to evaluate the supplier’s schedule for completeness and alignment with NASA expectations (see [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight)).
  + Validate supplier deliverables such as the **Version Description Document** (**VDD**) and Software Metrics Report, ensuring schedules correspond to recognized milestones. See [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document).
* **Request and Review Updates**:

  + Ensure suppliers periodically provide updated schedules that reflect new risks, scope changes, or resource availability constraints.

### 7.4.3 Tools and Resources for Software Assurance

* **Configuration Management Systems**:

  + Ensure the software schedule is under version control, allowing the project to manage updates and baseline changes effectively.
* **Metrics and Analysis Tools**:

  + Use tools capable of managing earned value metrics, schedule variance reporting, and dependency tracking.
* **Risk Management Framework**:

  + Leverage NASA-approved risk tools and databases to track risks identified from software scheduling activities (see [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)).

### 7.4.4 Additional Best Practices

#### 7.4.4.1 Collaborative Schedule Management

* Facilitate collaboration between software assurance, development teams, and project managers to ensure shared accountability for schedule adherence.

#### 7.4.4.2 Proactive Risk Identification

* Engage in early identification of schedule risks related to resource allocation, dependencies, or deliverable uncertainty to provide actionable recommendations for mitigation.

#### 7.4.4.3 Continuous Monitoring

* Conduct periodic reviews to ensure the schedule remains aligned with changing project requirements and provides effective insight into the supplier's activities.

#### 7.4.4.4 Streamlined Processes for Small Projects

* For small projects, focus assurance efforts on reviewing critical path activities, risks, and milestone alignment rather than on exhaustive oversight.

## 7.5 Additional Guidance

Additional guidance may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.05 - Work Breakdown Structures That Include Software](/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective evidence refers to documented artifacts, records, or outputs that demonstrate compliance with this requirement. It must provide tangible, verifiable, and auditable proof that the software schedule is created, reviewed, updated, and maintained as per the requirement. Below is a list of examples and types of objective evidence for this requirement.

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

## 8.1 Initial Schedule Delivery

Objective evidence demonstrating that the software schedule has been developed and submitted as part of the project lifecycle.

* **Example Artifacts**:
  1. **Software Development Schedule**:
     + A detailed timeline outlining planned software tasks, milestones, dependencies, required resources, and activity sequences in formats such as Gantt charts, task breakdowns, or network diagrams.
  2. **Work Breakdown Structure (WBS)**:
     + Includes software-related tasks in alignment with project deliverables and dependencies (see WBS documentation that reflects software activities integrated with the larger project-level schedule).
  3. **Milestone Plan**:
     + List and timing of key milestones (e.g., preliminary design, code completion, integration readiness, testing stages, and final delivery).
  4. **Critical Path Analysis**:
     + Documentation highlighting tasks on the critical path and identifying dependencies that may impact the overall schedule.

## 8.2  Periodic Schedule Updates

Evidence that the software schedule is being updated throughout the lifecycle as requested or triggered by project changes (e.g., scope changes, timeline adjustments, new risks, resource constraints).

* **Example Artifacts**:
  1. **Updated Software Development Schedule**:
     + A snapshot of the revised schedule indicating changes to tasks, milestones, durations, or resources (e.g., updated Gantt charts).
  2. **Change Logs**:
     + Records detailing modifications to the schedule, reasons for the changes, and approvals. Includes links between schedule changes and updates to baselines or project timelines.
  3. **Configuration Management Records**:
     + Evidence of baselined schedules stored in configuration management systems (e.g., versioned schedule files, change control documentation).
  4. **Schedule Metrics Reports**:
     + Reports tracking deviations or changes, such as schedule variance, SPI, or other metrics reflecting the current progress against the baseline.

## 8.3 Supplier Compliance

Objective evidence showing that the software supplier or contractor has provided required schedule deliverables.

* **Example Artifacts**:
  1. **Supplier Schedule Submission**:
     + Documented schedules provided by the software supplier (e.g., initial software schedules, milestone plans, or task-level schedules).
  2. **Contract Statement of Work (SOW)**:
     + The SOW explicitly specifying the requirement for schedule submissions and updates.
  3. **Meeting Minutes/Documentation**:
     + Records of supplier interactions where schedules were discussed, reviewed, or updated, including NASA feedback and resolution of issues.
  4. **Version Description Document (VDD)**:
     + Documentation of delivered software versions and related functional descriptions that align with schedule updates.

## 8.4 Schedule Insight/Traceability

Evidence to ensure schedules provide the necessary insight into software activities and progress.

* **Example Artifacts**:
  1. **Dependency Mapping**:
     + Diagrams or documentation of dependencies between software activities and external tasks (e.g., hardware dependencies, integration dependencies, or prerequisite approvals).
  2. **Risk Analysis Reports**:
     + Reports outlining risks associated with the schedule (e.g., tight dependencies, long lead items) and proposed mitigations.
  3. **Earned Value Management (EVM) Reports**:
     + Documents that provide visibility into task execution progress, including metrics such as schedule variance (SV) and schedule performance index (SPI).
  4. **Task/Activity Lists with Durations**:
     + Detailed lists of software tasks broken down with assigned durations and dependencies to ensure traceability (e.g., network diagrams or task dependency charts).

## 8.5 Monitoring and Reporting

Evidence confirming the review and monitoring of the software schedule and its updates by the project manager and assurance team.

* **Example Artifacts**:
  1. **Schedule Review Documentation**:
     + Meeting minutes, review checklists, or evaluation reports confirming that schedules (initial or updated) were reviewed for consistency and feasibility.
  2. **Periodic Reports**:
     + Regular project status reports or software development progress updates that reflect adherence to the schedule.
  3. **Change Requests**:
     + Records of formal requests for schedule updates, including justification for changes, related approvals, and evaluation of new schedule impact.
  4. **Risk Mitigation Plans**:
     + Plans tied directly to schedule risks, documenting how these risks are actively monitored and addressed.

## 8.6 Metrics and Performance Data

Evidence of metrics and analysis tied to the software schedule to confirm progress, alignment, and performance.

* **Example Artifacts**:
  1. **Schedule Metrics Reports**:
     + Reports measuring schedule adherence (e.g., SPI, SV, milestone completion rate, or task tracking ratios).
  2. **Testing Metrics**:
     + Percentage completion of planned tests tied to software milestones (e.g., testing readiness and progress reports).
  3. **Effort Analysis Reports**:
     + Reports comparing estimated effort to actual effort for tasks identified in the schedule.
  4. **Schedule Health Assessments**:
     + High-level evaluations of the schedule’s progress, risk exposures, and any recommendations for adjustments.

## 8.7 Evidence of Risk and Schedule Integration

Objective evidence linking schedule risk management to project planning and implementation activities.

* **Example Artifacts**:
  1. **Risk Tracking Logs**:
     + Risks identified as part of the schedule updates, including mitigation plans and links to the affected milestones.
  2. **Risk Management Plans**:
     + Documentation of risks associated with critical paths or specific schedule events (e.g., delayed integration testing due to hardware dependencies).
  3. **Schedule Contingency Plans**:
     + Evidence of contingency buffers for task timelines, dependencies, or milestones to mitigate potential delays.

## 8.8 Communication and Contractual Evidence

Objective evidence of communication and agreements between stakeholders regarding schedule requirements and updates.

* **Example Artifacts**:
  1. **Stakeholder Meeting Notes**:
     + Documentation of discussions on schedule creation, updates, or adjustments, including comments from project leads, developers, and assurance teams.
  2. **Contractual Documents**:
     + Contracts or agreements that specify the delivery, review, and update requirements regarding the software schedule (e.g., SOW clauses, supplier deliverable commitments).

## 8.9 Key Considerations for Objective Evidence

Objective evidence must:

* Be verifiable, traceable, and auditable for compliance with the requirement.
* Clearly document schedule creation, updates, and reviews expected from the software developer or contractor.
* Demonstrate alignment with project milestones, dependencies, and deliverables.

By ensuring that all aspects of the software scheduling process are documented, monitored, and controlled, this evidence provides confidence in project execution and compliance with NASA requirements.
