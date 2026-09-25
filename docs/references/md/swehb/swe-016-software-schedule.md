# SWE-016 - Software Schedule

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695402. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule

SWE-016 - Software Schedule

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695402)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695402&showCommentArea=true&showComments=true#addcomment)

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

3.3.1 The project manager shall document and maintain a software schedule that satisfies the following conditions:

1. 1. Coordinates with the overall project schedule.
   2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.
   3. Reflects the critical dependencies for software development activities.
   4. Identifies and accounts for dependencies with other projects and cross-program dependencies.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-016 History

SWE-016 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.4 The project shall document and maintain a software schedule that satisfies the following conditions:   1. 1. Coordinates with the overall project schedule.    2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.    3. Reflects the critical path for the software development activities. |
| Difference between A and B | Rev B adds item d. for adherence to NASA/SP-2010-3403 |
| B | 3.3.1 The project manager shall document and maintain a software schedule that satisfies the following conditions:   1. 1. Coordinates with the overall project schedule.    2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.    3. eflects the critical path for the software development activities.    4. Adhere to the guidance provided in NASA/SP-2010-3403, NASA Scheduling Management Handbook. |
| Difference between B and C | Removed reference to  NASA/SP-2010-3403; Changed critical path to critical dependency; Added identification and accountability for dependencies. |
| C | 3.3.1 The project manager shall document and maintain a software schedule that satisfies the following conditions:   1. 1. Coordinates with the overall project schedule.    2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.    3. Reflects the critical dependencies for software development activities.    4. Identifies and accounts for dependencies with other projects and cross-program dependencies. |
| Difference between C and D | No change |
| D | 3.3.1 The project manager shall document and maintain a software schedule that satisfies the following conditions:   1. 1. Coordinates with the overall project schedule.    2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.    3. Reflects the critical dependencies for software development activities.    4. Identifies and accounts for dependencies with other projects and cross-program dependencies. |

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

To manage resource allocations and support the system development activities software projects need a detailed software schedule.

The requirement for the project manager to document and maintain a software schedule that satisfies key conditions ensures that software development activities are well-aligned within the broader project and system lifecycle. This disciplined approach allows for greater predictability, improved coordination, risk mitigation, and accountability, ensuring project success.

The overall rationale for documenting and maintaining a detailed software schedule is to ensure **alignment, transparency, and proactive management** of all software-related activities within both the project and the broader system. By meeting the conditions outlined in the requirement, the project can:

1. **Mitigate Risks**: Reduce risks associated with misaligned schedules, missed milestones, and delayed components.
2. **Improve Coordination**: Foster better communication and collaboration among cross-disciplinary teams and external programs.
3. **Support Integration**: Ensure that all software deliverables are available when required for system-level testing and mission milestones.
4. **Enable Accountability**: Create a clear record of responsibilities, timelines, and interactions, allowing for better tracking of progress and adherence to project objectives.

Through this requirement, NASA projects can ensure that software development is seamlessly integrated into the overall mission lifecycle, maximizing efficiency, reducing delays, and improving the likelihood of successful mission outcomes.

Below is an enhanced explanation of the rationale behind each condition outlined in the requirement:

## 2.1 Coordinates with the Overall Project Schedule

* **Rationale**: Software is rarely developed in isolation; it is typically one component of a larger system involving hardware, operations, integration, and testing. The software schedule must be closely aligned with the overall project timeline to avoid delays that could disrupt the overall mission.
  + For example, if hardware integration requires software to be ready at a specific time, a mismatch in schedules could delay integration testing and potentially jeopardize critical milestones.
* **Benefit**: A synchronized schedule ensures that software deliverables are available when needed for broader project activities, minimizing risks of schedule conflicts while allowing teams to effectively manage shared resources, dependencies, and deadlines.

## 2.2 Documents the Interactions of Milestones and Deliverables Between Software, Hardware, Operations, and the Rest of the System

* **Rationale**: Software development is intertwined with the development and delivery of other system components such as hardware, operations procedures, and system testing. Clearly identifying and documenting interaction points and shared milestones ensures alignment and reduces the likelihood of surprise incompatibilities or delays.
  + For instance, coordinated milestones for hardware readiness and software testing ensure that both subsystems are tested together at the critical integration stage.
* **Benefit**: Documenting these interactions reduces miscommunication, enables integrated planning across teams, and ensures compatibility between subsystems. It also helps uncover and address inconsistencies early in the lifecycle, reducing risks to the overall system.

## 2.3 Reflects the Critical Dependencies for Software Development Activities

* **Rationale**: The software lifecycle often includes multiple interdependent activities (e.g., requirements analysis, design, implementation, testing, and delivery). Identifying critical dependencies ensures that activities and their sequencing are realistic and achievable within the planned schedule.
  + For example, software testing cannot begin until the relevant test environment is configured, and some features may require foundational development work to be completed first.
* **Benefit**: Critical dependencies enable the project manager to establish realistic, logically sequenced schedules, preventing bottlenecks, missed deadlines, or unproductive team idle periods. This leads to better risk mitigation and resource utilization for timely delivery.

## 2.4 Identifies and Accounts for Dependencies with Other Projects and Cross-Program Dependencies

* **Rationale**: Modern software often relies on deliverables or inputs from external projects, programs, or teams, such as libraries, APIs, shared infrastructure, or interoperable subsystems. Failing to account for these external dependencies can result in delays if the necessary inputs are unavailable when needed.
  + For example, software for a space mission may depend on tools or models developed by another program. If the external program’s schedule slips, the dependent project could face significant delays unless contingencies are considered.
* **Benefit**: Supporting cross-project and cross-program coordination ensures that external dependencies are acknowledged and properly managed. This allows the project team to make informed decisions, adjust schedules proactively, and establish contingency plans to reduce the risk of cascading delays.

# 3. Guidance

Effective software scheduling is essential for achieving project goals on time, within budget, and aligned with broader system objectives. The software schedule must integrate seamlessly with the overall project/system schedule and address major milestones, deliverables, dependencies, and resource needs. This enhanced guidance focuses on best practices, tools, processes, and considerations for achieving these objectives while minimizing risks and ensuring transparency in project execution.

Creating and maintaining a comprehensive software schedule is critical to ensuring timely delivery, efficient execution, and alignment of software development activities with broader project/system goals. By incorporating detailed planned activities, milestones, deliverables, and dependencies, and leveraging proven tools and techniques, project teams can mitigate risks, optimize resources, and manage constraints. With regular evaluation and proactive updates, the software schedule becomes a powerful tool for maintaining accountability and achieving mission success.

## 3.1 Importance of Schedule Management

The achievement of project goals and objectives requires careful planning and proactive management of resources, tasks, and dependencies. By developing and maintaining a comprehensive software schedule:

1. **Improved Integration:** The software schedule ensures that software development activities are synchronized with other project components (hardware, operations, system testing, etc.).
2. **Enhanced Visibility:** Clear schedules promote visibility into deadlines, dependencies, and risks, giving teams and stakeholders confidence in project execution.
3. **Proactive Risk Mitigation:** Continuous updates to the schedule enable the identification of potential delays or bottlenecks early, allowing corrective actions to be taken.
4. **Optimized Resource Allocation:** Scheduling ensures efficient utilization of personnel and resources, eliminating redundancy and overlapping demands.

## 3.2 Key Elements of a Software Schedule

### 3.2.1 Planned Activities

* **Definition**: Planned software activities include detailed steps and tasks that map to the software development plan and integrate seamlessly with the overall project schedule.
* **Guidance**:
  + Collaborate closely with system-level teams to align software activities with the overall project milestones and deliverables.
  + Ensure detailed activities such as requirements gathering, design, coding, testing, and verification are fully planned and resourced.
  + Account for interdependencies between software work products and other components (e.g., hardware testing or operational readiness).

### 3.2.2 Milestones and Deliverables

* **Definition**: Milestones correspond to critical events (e.g., major reviews, delivery dates, subsystem integration) within the software lifecycle, while deliverables represent tangible software work products.
* **Guidance**:
  + Document milestones such as Preliminary Design Review (PDR), Critical Design Review (CDR), integration/testing dates, and delivery schedules.
  + Consider dependencies such as hardware readiness, training needs, and configurations required by other teams to avoid mismatches.
  + Include all supporting deliverables like documentation, configuration management updates, and assurance activities.

### 3.2.3 Critical Dependencies

* **Definition**: Dependencies reflect interactions between software tasks and other project/system elements or cross-program activities.
* **Guidance**:
  + Identify how software tasks drive or are impacted by the broader system (e.g., software integration with hardware testing or operational deployment).
  + Perform "critical path" analysis to assess tasks that directly affect the project's timeline and make necessary adjustments.
  + Monitor evolving dependencies throughout the project lifecycle, as changes in scope or requirements may alter task sequencing.

### 3.2.4 Other Project and Cross-Program Dependencies

* **Definition**: These dependencies involve external factors such as interrelated projects or programs contributing resources, technologies, or deliverables essential to software development.
* **Guidance**:
  + Factor in external programs’ schedules that supply APIs, libraries, or tools to avoid schedule conflicts.
  + Use dependency tracking to ensure inputs from cross-program activities arrive when needed and establish contingency plans for delays.

## 3.3 Process for Developing and Maintaining the Software Schedule

### 3.3.1 Developing the Schedule

1. **Develop Work Breakdown Structure (WBS)**:

   * Create an organized WBS that identifies tasks, timelines, and resources for all software activities.
   * Ensure tasks are sufficiently detailed to minimize ambiguity and enable accurate tracking.
2. **Define Milestones and Constraints**:

   * Identify start/end dates, project reviews, dependencies, and hard constraints (e.g., delivery dates or system integration deadlines).
3. **Sequence Tasks**:

   * Use tools like Gantt charts or Program Evaluation and Review Technique (PERT) charts to visualize task sequencing and dependencies.
   * Incorporate float or slack time based on project length, team experience, and risk margin.
4. **Iterate with Resource Planning**:

   * Assign resources (e.g., personnel, tools, and environments) to tasks and refine durations based on availability.
   * Adjust the schedule collaboratively with the team to ensure practicality.
5. **Establish the Baseline**:

   * Secure management approval for the initial schedule and document it in the Software Development/Management Plan (SDP/SMP).

### 3.3.2 Maintaining the Schedule

1. **Monitor and Report Status**:

   * Regularly update progress and report on task completion through status meetings.
   * Use tools (e.g., Microsoft Project, Primavera, OmniPlan) to automate status tracking and reporting.
2. **Handle Schedule Changes**:

   * Evaluate the impact of requirement or project scope changes, resolving conflicts with the project team and stakeholders.
   * Revise timelines or negotiate trade-offs (e.g., reducing scope) if changes cannot be accommodated within the current schedule.
3. **Manage Slack Time and Risks**:

   * Monitor remaining float or margin to identify potential schedule compression risks.
   * Perform ongoing risk assessments to address issues that could disrupt critical tasks or dependencies.

## 3.4 Tools and Techniques for Schedule Management

### 3.4.1 Scheduling Tools

* Use project management tools like Microsoft Office Project®, Oracle® Primavera, or OmniGroup OmniPlan® to build, track, and analyze schedules efficiently.
* Employ Gantt charts for timeline visualization and PERT charts for dependency analysis.

### 3.4.2 Critical Path Analysis

* Perform regular critical path analysis to identify tasks that will determine the overall project's timeline. Adjust resources or sequence tasks to address delays on critical path activities.

### 3.4.3 Dependency Management

* Map dependencies using visual models (e.g., network schedules) and categorize them by importance (critical vs. non-critical).
* Use dependency analysis and tracking tools to avoid delays caused by upstream or external inputs.

### 3.4.4 Schedule Integration

* Leverage the NASA Schedule Management Handbook (*NASA/SP-2010-3403*) to align the software schedule with lifecycle milestones for system-level reviews (e.g., PDR, CDR, TRR).
* Document software schedule information as part of the SDP/SMP and refine it regularly.

## 3.5 Best Practices for Scheduling

1. **Collaborate Across Disciplines**:
   * Work closely with hardware, operations, assurance, and other system teams to ensure schedules are interdependent and realistic.
2. **Monitor Continuously**:
   * Regularly update schedules to reflect progress, changes, or risks that arise during development.
3. **Use Metrics**:
   * Refer to metrics reports (e.g., *Topic 5.05 - Metrics - Software Metrics Report*) to track schedule adherence and productivity.

See also, [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule)

## 3.6 Additional Guidance

Additional guidance related to software project schedules may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning)      * [Contracting](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Contracting) |

# 4. Small Projects

Small projects typically operate with fewer resources, shorter timelines, and reduced complexity compared to larger initiatives. As such, scheduling tools and practices should be tailored to match the scale and scope of the project, ensuring efficiency and effectiveness while avoiding unnecessary overhead. The following guidance provides practical recommendations for developing, documenting, and tracking schedules for small projects in a way that balances detail and usability.

For small projects, the focus should be on simplicity and efficiency in both schedule creation and tracking. Lightweight tools like Excel, Word, or text-based formats are often sufficient, saving valuable time for smaller teams or initiatives. When appropriate, more advanced tools like Microsoft Project® or OmniPlan® can be utilized to manage integration and dependencies with larger efforts. By tailoring the scheduling approach to the scale and complexity of the project, teams can maintain clarity, reduce overhead, and achieve successful project outcomes.

## 4.1 Use Tools Appropriate for the Scale of Your Project

The choice of scheduling tool for a small project should be guided by the size of the team, project duration, available resources, and ease of use. While sophisticated project management tools like Microsoft's Project, OmniPlan®, and Oracle® Primavera are powerful, smaller projects may benefit from simpler alternatives.

#### **Key Recommendations:**

1. **Microsoft Project® or OmniPlan®**:

   * These professional tools provide robust scheduling features to track dependencies, milestones, and timelines but may introduce unnecessary overhead for very small projects.
   * **Best Use**: Use these tools if they are already accessible to the team and the schedule requires tracking multiple dependencies or coordinating with larger systems. For example, a small but complex project integrated into a larger NASA program might benefit from using these tools.
2. **Spreadsheet-Based Tools (e.g., Microsoft Excel®):**

   * Spreadsheets offer flexibility for small-scale scheduling and allow teams to easily create lists of tasks, milestones, and deadlines without needing specialized software.
   * **Best Use**: Ideal for very small projects (e.g., 2–3 team members or duration of less than a month) when simplicity and efficiency are priorities.
3. **Text-Based Schedules (e.g., Microsoft Word® or plain text):**

   * Text documents or lists can be sufficient for projects with minimal dependencies or straightforward schedules.
   * **Best Use**: Projects with simple milestones and deliverables where the focus is on clarity rather than visualization (e.g., small prototype builds, short-duration R&D efforts).
4. **Low-Cost or Free Tools:**

   * For teams without access to professional software, consider using lightweight tools such as open-source project management software or platforms like Trello, Asana, or Google Sheets—particularly when collaboration is required.

## 4.2 Tailor the Level of Schedule Detail to the Project's Needs

Small projects benefit from minimizing complexity in their schedules while ensuring critical tasks, milestones, and deliverables are clearly identified and tracked.

#### **Simplified Scheduling Guidelines:**

* **Reduce Granularity:** Unlike larger projects that require detailed breakdowns for each task, small projects can consolidate activities into broader categories. For example:
  + Instead of breaking "coding tasks" into daily items, group them into weekly goals like "Develop Feature A" or "Complete Module Testing."
* **Focus on Key Milestones:** Document high-level milestones such as project start, major reviews, deliverable dates, and completion—without tracking nonessential details that add overhead.
* **Dependencies:** Map only critical dependencies among tasks or external inputs (e.g., hardware availability or data readiness).
* **Visual Tools:** Use basic charts (e.g., Gantt charts or simple tables) to visually track progress, without the need for sophisticated visualizations.

#### **Example of a Small Project Schedule (Text or Excel-Based)**

| **Task/Activity** | **Start Date** | **End Date** | **Owner** | **Dependencies** |
| --- | --- | --- | --- | --- |
| Develop Prototype UI | 10/05 | 10/12 | Developer Team A | Requirements complete |
| Conduct Alpha Testing | 10/13 | 10/20 | QA Lead | UI Completion |
| Submit Deliverable | 10/21 | 10/22 | Project Manager | Testing approved |

## 4.3. Benefits of Simple Scheduling for Small Projects

Adopting a streamlined approach to scheduling ensures that small projects can focus on execution rather than administrative overhead. The benefits include:

* **Time Efficiency**: Less time spent building and maintaining elaborate schedules.
* **Ease of Use**: Simplified tools can be implemented quickly, requiring minimal training or setup.
* **Flexibility**: For fast-moving or short-term projects, lightweight schedules allow adjustments to be made easily without impacting the project's workflow.
* **Accessibility**: Tools like Excel or Word are widely available, making them practical for small teams or organizations without access to high-cost software.

## 4.4. When to Consider Professional Tools for Small Projects

Although simplified approaches frequently suffice, there are scenarios where professional tools may be justified for small projects:

* **Integration with Larger Programs:** If the small project is part of a broader mission or system, use tools compatible with larger schedules to maintain alignment and data consistency.
* **Complex Dependencies:** When dependencies involve multiple external organizations, hardware/software dependencies, or cross-team inputs, professional tools help manage and track these critical elements.
* **Need for Visualization:** If stakeholders require detailed graphical representations of timelines, dependencies, and milestones, tools like Microsoft Project® serve this purpose effectively.

## 4.5. Training and Resource Considerations

For very small projects (e.g., teams of 2–3 people or projects lasting less than one month), introducing a new tool that requires training or setup may be counterproductive. In such cases:

1. **Use Familiar Tools**: Leverage software already accessible to the team, like Excel, Google Sheets, or integrated tools within existing platforms.
2. **Prioritize Usability**: Choose tools based on their ease of use and the team’s familiarity with them. Avoid tools that add complexity or require specialized expertise.

## 4.6. Practical Recommendations

* **Set Clear Expectations**: Even if using lightweight tools, define clear start dates, end dates, and deliverables for all tasks and milestones.
* **Collaborate Early**: Discuss the schedule with all team members to ensure agreement and alignment on priorities and deadlines.
* **Update Regularly**: Small project schedules still need periodic updates to account for changes, risks, or delays.
* **Monitor Progress**: Continuously track task completion and adjust the schedule for flexibility while maintaining goals.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-192)

  [Gantt Chart](http://www.ganttchart.com/ "Click to open in new window")
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-264)

  [NASA Information Technology Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=7A "Click to open in new window")

  NPR 7120.7A, Office of the Chief Information Officer, Effective Date: August 17, 2020,
  Expiration Date: August 17, 2025
  .
* (SWEREF-269)

  [NASA Research and Technology Program and Project Management Requirements (Updated w/Change 5)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7120_008A_&page_name=main "Click to open in new window")

  NPR 7120.8A, NASA Office of the Chief Engineer, 2018, Effective Date: September 14, 2018, Expiration Date: September 14, 2028
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-445) Orbital Space Program Lessons Learned, Realistic and Integrated Schedule, Lesson Number OSP.01.0042, NASA, Agency IHM Team, March 29, 2004.  Lesson Number OSP.01.0042, NASA, Agency IHM Team, March 29, 2004.
* (SWEREF-446)

  [Continuous Risk Management.](http://www.spmn.com/lessons.html#three "Click to open in new window")

  Software Program Managers Network, http://www.spmn.com
* (SWEREF-488)

  [NASA Schedule Management Handbook,](https://www.nasa.gov/pdf/420297main_NASA-SP-2010-3403.pdf "Click to open in new window")

  NASA/SP-2010-3403, NASA Headquarters, January 2010.
* (SWEREF-489)

  [NPD 1000.5,B, Policy for NASA Acquisition,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=1000&s=5C "Click to open in new window")

  NPD 1000.5C, Policy for NASA Acquisition, Effective Date: July 13, 2020, Expiration Date: July 13, 2025
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

### **Late and Incomplete Flight Software (FSW) Delivery**

**Incident:**  
The Psyche mission experienced an eight‑month late delivery of the final GNC flight software build, with hundreds of control parameters and fault protection behaviors still undefined. This delay, combined with numerous unresolved software issues, contributed directly to the missed 2022 launch opportunity. citeturn1search1.page21

**Lesson Learned:**

* **Early Software Definition & Maturity:** Mission‑critical software requirements, parameters, and behaviors must be fully defined and matured early to prevent cascading delays.
* **Rigorous Defect Disposition:** “Use‑as‑is” and unverified failure dispositions must undergo strict technical review to prevent acceptance of excessive residual risk. citeturn1search1.page22

**Implication:**  
Delays and ambiguity in software maturity directly threaten launch schedules, increasing cost, workforce strain, and mission‑risk exposure.

## 6.2 Other Lessons Learned

* One of the activities in the Orbital Space Plane (OSP) program required the review of a project schedule in a short time (9000 pages in 45 days). However, the lack of integration between NASA's schedule and the contractors' schedules led to a failure to foresee the consequences of accelerating the schedule. The overall finding recommends that the program should integrate both the NASA and contractor schedules and those schedules should be resource loaded. [445](#_tabs-<p></p>)
* If only high-level schedule risks are considered because of the lack of an integrated continuous risk management plan, longer-term risks ("Risks beyond a short time...") to the overall schedule may not be identified and mitigated.  See the Software Program Managers Network lesson learned schedule entry under "Continuous Risk Management." [446](#_tabs-<p></p>)
* The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:
  + **[Pressing software schedule and staffing plans too hard](https://software.gsfc.nasa.gov/lesson-details/5/). Lesson Number 5**: The recommendation states: "Beware of pressing software schedule and staffing plans too hard to help meet competitive cost caps."
  + **[Integrated project schedules, with dependencies, ensure critical interfaces are managed](https://software.gsfc.nasa.gov/lesson-details/64/). Lesson Number 64**: The recommendation states: "Integrated project schedules, with dependencies, ensure critical interfaces are managed."
  + **[Integrated project schedules, with dependencies, ensure the proper sequencing of deliverables](https://software.gsfc.nasa.gov/lesson-details/67/). Lesson Number 67**: The recommendation states: "Integrated project schedules, with dependencies, ensure the proper sequencing of deliverables."
  + **[Projects should work with the Space Network (SN)](https://software.gsfc.nasa.gov/lesson-details/83/). Lesson Number 83**: The recommendation states: "Projects should work with the Space Network (SN) to understand and consider the mission's (and other SN customer's) operational constraints."
  + **[Responding to cost/schedule/performance challenges may require hard choices](https://software.gsfc.nasa.gov/lesson-details/154/). Lesson Number 154**: The recommendation states: "Responding to cost/schedule/performance challenges may require hard choices."
  + **[End-to-End Testing through satellite I&T](https://software.gsfc.nasa.gov/lesson-details/172/). Lesson Number 172**: The recommendation states: "End-to-End Testing should be planned for smaller events spread out through satellite (i.e., spacecraft with integrated payload/science instruments) I&T."
  + **[For an agile development approach, plan for a hardening sprint with any build](https://software.gsfc.nasa.gov/lesson-details/284/). Lesson Number 284**: The recommendation states: "When using an agile development approach, plan for additional time at the end of the build for a hardening sprint, which can be used for fixing remaining bugs, as well as other technical debt."
  + **[Challenges when project members’ time is split between multiple projects](https://software.gsfc.nasa.gov/lesson-details/287/). Lesson Number 287**: The recommendation states: "When a project member’s time is split between multiple projects, the project/team lead needs to understand and manage the availability and expectations for the member’s contribution to the project. Time allocation among projects and work priorities for these "shared" people needs to be discussed (and revisited, as needed) and the project leads, employee, and supervisor/task manager need to be in agreement at all times. When needed, Branch Management should also be informed and/or involved, to ensure that the project's staffing plan does not overly rely on part-time staff during life cycle phases of critical or "high tempo" activities."
  + **[Key Paths Schedule Visualization for Ground / Operations Readiness](https://software.gsfc.nasa.gov/lesson-details/322/). Lesson Number 322**: The recommendation states: "Track multiple key dependency paths in top-level schedule visually."
  + **[Use Risk and Schedule for communicating “up the chain.”](https://software.gsfc.nasa.gov/lesson-details/326/) Lesson Number 326**: The recommendation states: "Use quantitative tools (risk and schedule) for communicating, in addition to qualitative status reports."
  + **[Schedule estimates should include confidence level](https://software.gsfc.nasa.gov/lesson-details/334/). Lesson Number 334**: The recommendation states: "Include a confidence level for schedule estimates and, if forced to adopt a low-confidence schedule, submit a risk."
  + **[Carefully consider team organization structure during planning](https://software.gsfc.nasa.gov/lesson-details/335/).** **Lesson Number 335**: The recommendation states: "Ensure that team structure provides clear lines of responsibility and sufficient avenues for communication."

# 7. Software Assurance

**SWE-016 - Software Schedule**

3.3.1 The project manager shall document and maintain a software schedule that satisfies the following conditions:

1. 1. Coordinates with the overall project schedule.
   2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.
   3. Reflects the critical dependencies for software development activities.
   4. Identifies and accounts for dependencies with other projects and cross-program dependencies.

This requirement emphasizes the need for a well-integrated software schedule that accounts for project dependencies while providing sufficient visibility into software development, assurance, and safety activities. Software Assurance (SA) guidance and practices should ensure alignment, evaluation, and management of software-specific schedule activities to mitigate risks and maintain timely delivery of project goals.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Assess that the software schedule satisfies the conditions in the requirement.

2. Develop a software assurance schedule, including software assurance products, audits, reporting, and reviews.

## 7.2 Software Assurance Products

### 7.2.1 Software Assurance Schedule

**Purpose**: Documents all SA and software safety activities, milestones, and deliverables, aligned with the overall project schedule, ensuring critical interactions and dependencies are accounted for.  
**Contents**:

* SA activity schedule with defined start and completion dates, milestones, and slack time (margins).
* Alignment of SA milestones with project reviews and deliverables (e.g., SDR, PDR, CDR, TRR).
* Integration of SA audits, assessments, and analysis activities with software milestones (e.g., design review, coding phase, testing phase).
* Identification of cross-program dependencies and coordination points (e.g., software-hardware integration, operations dependencies).

### 7.2.2 Software Assurance Plan (SAP)

**Purpose**: Outlines SA activities, methods, and deliverables, ensuring alignment with the software schedule.  
**Contents**:

* SA tasks mapped to software development lifecycle phases (e.g., static code analysis during coding, audit checklists during reviews).
* Dependencies between SA activities and other project disciplines, with reference to coordination responsibilities.
* Software assurance risk identification related to schedule adherence.

### 7.2.3 Software Assurance Schedule Assessment Report

**Purpose**: Evaluates the software schedule for inconsistencies, risks, and opportunities for improvement.  
**Contents**:

* Analysis results comparing the software schedule against the project schedule (e.g., milestone alignment, review timelines).
* Identification of critical dependencies across systems engineering, operations, hardware, and other disciplines.
* Documentation of schedule risks (e.g., insufficient margins, unrealistic timelines, missing dependencies).
* Recommendations to resolve inconsistencies or mitigate risks for schedule alignment.

### 7.2.4 Software Engineering Plan Assessment

**Purpose**: Verifies software engineering activities align with the documented software schedule.  
**Contents**:

* Assessment of lifecycle phase durations against resources needed to perform scheduled tasks/activities.
* Confirmation of interactions and dependencies between software engineering, hardware, and operations milestones.
* Identification of any discrepancies impacting software engineering deliverables or cross-program dependencies.

### 7.2.5 SA Risk Management Plan and Logs

**Purpose**: Tracks risks specifically related to schedule deviations, missed dependencies, and software delays impacting the overall project.  
**Contents**:

* Logs of identified schedule-related risks with mitigation plans and tracking statuses.
* Metrics monitoring margin usage, slack time, and dependency conflicts between software assurance and project schedules.

## 7.3 Metrics

Metrics track software schedule progress, peer review activities, and risk management to identify trends that may impact project deliverables.

### Key Metrics

### 7.3.1 Schedule Progress Metrics:

* Deviations in schedule progress over time:
  + Planned vs. actual milestone completions exceeding defined thresholds.
* Critical path analysis showing delays impacting dependencies between software, hardware, and operations.

### 7.3.2 SA Audit Activity Metrics:

* **# of Peer Reviews Performed vs. Peer Reviews Scheduled:** Indicates peer review adherence to the documented schedule.
* **# of SA Audits Planned vs. Performed:** Tracks whether planned audits occur in alignment with software milestones.
* **# of Open vs. Closed Audit Non-Conformances Over Time:** Monitors whether non-conformance findings from audits are resolved efficiently within the project timeline.

### 7.3.3 Risk Metrics:

* Trends in slack/margin usage over time, identifying:
  + Schedule compression impacts.
  + Increased likelihood of cascading delays.
* **# of Process Non-Conformances Identified vs. Accepted by the Project:** Tracks SA-specified schedule recommendations accepted into project actions versus recommendations not incorporated.

### 7.3.4 Dependency Metrics:

* **# of Dependencies Evaluated:** Tracks dependencies (internal and external) reviewed during schedule maintenance.
* **Trends in Dependency Conflicts Identified:** Measures recurring or unresolved dependency risks across disciplines.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.4 Guidance

Software Assurance personnel must take an active role in evaluating, aligning, and maintaining the software schedule to meet the requirement. Key steps are outlined below:

### Step 1: **Assess the Software Schedule**

* **Coordinate with the Project Schedule**: Ensure the software schedule aligns with overall project milestones, incorporates realistic margins, and accounts for the type of software development activities (e.g., iterative development versus traditional V-model).
* **Document System-wide Interactions**: Verify that dependencies between software, hardware, and operations are well-defined and visible on the schedule:
  + Example: Ensure software milestones allow appropriate time for hardware integration and testing.
  + Example: Operational timelines allow buffer periods for software testing and deployment.
* **Reflect Dependencies for Software Development Activities**:
  + Confirm critical dependencies (e.g., design completion before coding, hardware-logic syncing before integration testing) are explicitly included.
* **Account for External Dependencies**: Verify coordination with cross-program dependencies (e.g., data dependency from external projects, hardware from third-party vendors).

### Step 2: **Develop and Maintain the SA Schedule**

* **Define Constraints**: Identify start dates, review milestones, and completion deadlines for SA activities (e.g., audits, analysis).
* **Review Task Requirements**: Populate specific SA tasks, including required resources, durations, and responsible personnel.
* **Incorporate Margins and Slack Time**: Schedule slack or buffer periods for SA tasks based on project risk, complexity, and team experience.
* **Coordinate Dependencies**: Ensure SA products depend on and provide input to other project disciplines (e.g., hazard analyses impacting design reviews).
* **Establish Baselines**: Finalize the SA schedule, review it against project milestones, and obtain management approval.

### Step 3: **Integrate SA Activities**

Examples of SA Schedule Items to Include:

* SA plan and audit milestones (e.g., SDR audit checklist, final TRR compliance report).
* Static code analysis (e.g., cybersecurity vulnerability detection).
* Review and milestone audits (e.g., verifying alignment of software design with system requirements).
* Safety-critical assessments (e.g., hazard analysis inputs to risk tracking).
* Peer reviews for SA metrics tracking and reporting.

### Step 4: **Address Schedule Risks**

* **Track Slack Margins**: Monitor remaining slack or margins to identify risk triggers and prevent cascading delays.
* **Resolve Issues Promptly**: Report schedule conflicts or resource gaps impacting SA activities to management for resolution.
* **Monitor Dependencies**: Continuously evaluate dependencies with other disciplines for new risks.

By following these steps and tracking metrics, Software Assurance personnel can ensure the software schedule is aligned, realistic, and contributes effectively to project-wide goals while mitigating risks. This framework strengthens compliance with the requirement and provides traceability for SA efforts.

See also Topic [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing).

### 7.4.1 Examples of items on a Software Assurance schedule could include:

* Software Assurance plan,
* Software Assurance audit,
* Software Assurance status reports,
* Software assurance and software safety requirements mapping table for the Software Assurance and Software Safety standard requirements, the cost estimate for the project’s Software Assurance support, Software Assurance and software safety reviews and software assurance review support,
* IV&V planning and risk assessment, if required.
* The IV&V Execution Plan, if required.
* System hazard analysis assessment activities,
* Software Safety Analysis,
* Software Assurance independent static code analysis for cybersecurity vulnerabilities and weaknesses,
* Software Assurance independent static code analysis, on the source code, showing that the source code follows the defined secure coding practices,
* Software Assurance analysis performed on the detailed software requirements,
* Software assurance design analysis, SA peer reviews,
* Software Assurance metric data, reporting, and analysis activities,
* Software Assurance status reviews.

See also Topic [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan),

### 7.4.2 Maintain the schedule:

* Report the status of the development effort to project management through status meetings.
* Report issues that impact the software assurance team's ability to adhere to the schedule to senior management and to project management as appropriate.
* Monitor the remaining slack or margin in the project to help identify quickly if requirement changes or schedule modifications are required.
* Resolve issues and/or revise the schedule.
* Resolve any resource issues with the project.

The software schedule is an integral part of the overall project/system schedule and as such contributes to the critical path for the project.  The software assurance must identify and understand the impact that the software development activities have on the overall integrated project schedule.  It is also important that software assurance understand the relationship between software development tasks and their interfaces with other project tasks. This will allow the software assurance to assess changes to the project schedule that may affect software development as well as software changes that may affect the integrated project schedule. The software assurance team regularly evaluates the software schedule for apparent and hidden issues and risks.

Schedule path analysis constructs a model of the project that includes the following:

* A list of all activities required to complete the project (typically categorized within a work breakdown structure).
* The time (duration) that each activity will take to be completed.
* The dependencies between the activities.

## 7.5 Additional Guidance

Additional guidance related to software project schedules may be found in the following related requirements in this Handbook:

| Related Links |
| --- |
| * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) |

# 8. Objective Evidence

Objective evidence substantiates that software assurance activities align with the project schedule and comply with **Requirement 3.3.1**.

### Definition of Objective Evidence

Objective evidence includes project schedules, documented assessments, plans, reviews, audit reports, and risk logs that demonstrate the integration, maintenance, and alignment of software schedules with project milestones and dependencies.

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

## 8.1. Objective Evidence to Be Collected

### 8.1.1 Software Schedule:

* Complete project software schedule showing:
  + Milestones for all software engineering activities (development, testing, delivery).
  + SA-specific audits, reviews, and analyses integrated into the schedule.
  + Dependencies (e.g., software-hardware integration).
  + Slack time or resource buffer zones critical to software assurance and safety activities.

### 8.1.2 SA/Software Engineering Plan:

* Approved plans outlining coordination between SA activities and software engineering efforts.
* Cross-references to project-level schedules and dependencies.

### 8.1.3 Assessment Results:

* Evaluation reports on the software schedule, showing alignment with project-level milestones and identification of issues or risks.

### 8.1.4 Dependency Mapping Documentation:

* Evidence that software schedule dependencies are tracked, accounted for, and monitored (e.g., hardware development dependencies, data acquisition from external projects).

### 8.1.5 Risk Logs:

* Risks and mitigation plans specific to software schedule misalignments or dependencies with other systems/programs.
