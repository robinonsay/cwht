# SWE-200 - Software Requirements Volatility Metrics

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695533. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics

SWE-200 - Software Requirements Volatility Metrics

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695533)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695533&showCommentArea=true&showComments=true#addcomment)

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

5.4.6 The project manager shall collect, track, and report software requirements volatility metrics.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-200 History

SWE-200 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW  Class A or B only |
| C | 5.4.6 The project manager shall collect, track, and report software requirements volatility metrics. |
| Difference between C and D | No change |
| D | 5.4.6 The project manager shall collect, track, and report software requirements volatility metrics. |

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
| * [A.11 Software Measurements](/spaces/SWEHBVD/pages/133235387/A.11+Software+Measurements) |

# 2. Rationale

Requirements volatility is one of the leading causes of the software development effort not completing on schedule and budget.  Software requirements volatility is one key factor in assessing the status of a software project.  The later in the project requirements changes occur, the more impact those changes can have on project completion on time and within budget.

### **Definition of Requirements Volatility:**

Requirements volatility refers to the frequency and magnitude of changes made to software requirements during the development lifecycle. Changes can include requirement additions, deletions, modifications, or clarifications. Volatility can arise from evolving stakeholder needs, unexpected findings during testing, external factors (e.g., funding, mission scope changes), or misunderstandings during early requirements definition.

---

### **Why This Requirement Is Important:**

#### **1. Early Identification of Risks**

Changes to requirements beyond the early stages of development can lead to cascading risks across the project, such as delays, rework, unanticipated costs, and quality degradation. Tracking requirements volatility helps project managers:

* Identify trends and predict areas likely to be impacted by changes (design, implementation, testing).
* Mitigate risks related to schedule disruptions or incomplete requirement implementations.

**Example:** If requirements volatility increases drastically during implementation, it may signal insufficient requirements clarity or stakeholder misalignment, requiring immediate attention to stabilize the baseline.

---

#### **2. Ensuring Project Stability**

High requirements volatility may indicate that the software baseline is unstable, which undermines the ability to plan scheduling, testing, and critical milestones effectively. Regular tracking provides insight into how stable the requirements are and helps project managers determine whether the project is on track or in danger.

**Example:** Uncontrolled volatility during late development stages can disrupt high-cost, resource-heavy testing phases, leading to budget overruns and mission-critical delays.

---

#### **3. Budget and Resource Optimization**

Changing requirements often demands reallocation of already committed resources: teams may need to redo designs, rewrite code, or retest functionality. Understanding volatility helps managers quantify the potential cost of requirement changes and proactively adjust resource allocations before significant rework occurs.

**Example:** Knowing mid-development volatility trends (modifications to 20% of requirements) allows a more accurate estimate of additional testing costs for regression testing.

---

#### **4. Improves Confidence in Meeting Mission Goals**

Software for NASA missions must operate under strict constraints (e.g., timing, reliability, accuracy), often in unforgiving environments. Fluctuating requirements increase the risk of introducing unforeseen defects, mismatched interfaces, performance degradation, or system failure. Tracking volatility ensures changes are scrutinized and assessed against performance, functionality, and constraint impacts.

**Example:** Requirements volatility metrics can highlight critical areas impacted by changes (e.g., navigation system requirements updates affecting integration testing schedules), increasing assurance for mission success.

---

#### **5. Facilitates Better Communication**

Reporting requirements volatility provides stakeholders and team members with shared visibility into how dynamic the requirements are and the resulting impacts on planning, testing, and delivery. It promotes transparency and ensures all parties are made aware of evolving risks or delays early.

**Example:** By reporting that requirements action items increased by 10% during implementation, project managers can justify extending the integration timeline to stakeholders before critical testing begins.

---

#### **6. Enhances Quality and Reduces Defects**

Constant changes in requirements can obscure the original intent of the system, introduce defects, or cause misalignment between various development teams. Formal tracking allows project managers to verify that changes are assessed for correctness, traceability, and completeness, thus reducing errors and improving overall quality.

**Example:** By identifying trends where vague requirement updates frequently trigger defects, the team can refine its process for reviewing requirement changes and ensure clarity in future updates.

---

#### **7. Supports Continuous Improvement**

By analyzing historical volatility metrics, future projects can learn from trends in past development efforts. Frequent changes to specific requirement types (e.g., performance requirements) could highlight weaknesses in early stages of requirements elicitation. Future risk mitigation efforts can focus on improving upfront requirement stability.

**Example:** Data from previous missions showing high volatility in requirements related to real-time processing might prompt future teams to engage earlier with stakeholders to improve clarity before formal requirements approval.

---

### **Benefits of Tracking Requirements Volatility Metrics:**

| **Benefit Area** | **Description** |
| --- | --- |
| **Schedule Management** | Tracks whether high volatility is jeopardizing delivery timelines and facilitates corrective action. |
| **Cost Management** | Quantifies the cost associated with changes, helping manage budgets and mitigating overruns. |
| **Risk Identification** | Highlights areas of instability and risks that could lead to defects, integration failures, or noncompliance. |
| **Stakeholder Alignment** | Improves visibility and communication between stakeholders regarding evolving requirements. |
| **Quality Assurance** | Ensures appropriate analysis and testing of changes to avoid introducing defects or inconsistencies. |
| **Process Improvement** | Facilitates learning by analyzing volatility trends that can guide future requirement management practices. |

---

### **Monitoring Volatility Metrics with Tools**

Effective tracking can include collecting data like:

* **Number of requirements added, deleted, or modified (per unit of time).**
* **Percentage of baseline requirements that remain unchanged over each phase.**
* **Time required to evaluate and incorporate requirement changes.**

Metrics can be incorporated into dashboards or reports, allowing project managers to illustrate trends and impacts clearly to teams and stakeholders.

The rationale for tracking requirements volatility metrics lies in early risk identification, stabilizing project execution, optimizing resources, achieving stakeholder alignment, and enhancing quality. By collecting and analyzing these metrics, project managers gain valuable insights into system stability, reduce uncertainties, and improve the confidence that the software will meet predefined performance and functionality goals without jeopardizing schedules, budgets, or mission success.

# 3. Guidance

## 3.1 Applicability

This requirement applies to **all NASA centers** for **Class A and B software**, where mission-critical importance and safety implications make it essential to track requirements volatility throughout the software lifecycle.

For **Class C software**, collecting requirements volatility metrics is recommended **when project constraints warrant additional monitoring**, such as in the case of:

* Fast-paced development schedules.
* Complex interfaces with higher-risk subsystems.
* Resource-intensive mission objectives.

Even if not mandatory, tracking these metrics for Class C software can lead to better decision-making and identification of risks early in the project.

Cross-reference: **Topic 5.01 - CR-PR (Software Change Request - Problem Report)** to understand how requirements changes are managed in the broader context of change control.

## 3.2 Impact of Requirements Changes

#### **Requirements Changes During the Lifecycle**

* **Requirements changes during early development** phases, such as Pre-Phase A through the Preliminary Design Review (PDR), are relatively common. These changes are typically adjustments for clarification, missing requirements, or overlooked functionality. At these stages, the cost of changes is anticipated as part of the project’s risk and cost baselines.
* However, **requirements changes after PDR** or later in the lifecycle have significantly higher impacts. These later changes can result in:
  + Rework of already implemented designs.
  + Impacted integration schedules.
  + Increased verification and validation overhead.
  + Potential budget overruns and delays.

#### **Proactive Measures at PDR**:

* By PDR, the majority of the system’s requirements should be **identified, refined, and traceable**. Early and comprehensive stakeholder engagement can reduce late-stage requirements volatility.
* The cost of requirements changes made **post-PDR** can escalate significantly, so project managers must assess:
  + The justification for the change.
  + The consequences (schedule, cost, and risk) of implementing the change.
  + Alternative mitigations to reduce impacts.

## 3.3 Tracking Requirements Volatility

#### **Why Track Requirements Volatility?**

Tracking requirements changes ensures that the project is monitoring key areas of instability that could impact the overall development effort. Uncontrolled or frequent changes can signal deficiencies in requirements definition, stakeholder alignment, or subsystem integration planning.

Key reasons to track requirements volatility include:

1. **Cost/Schedule Impact Analysis:** Allows project managers to evaluate whether the proposed change aligns with project constraints.
2. **Risk Management:** Identifies unstable or frequently changing requirement areas that may require additional attention or contingency planning.
3. **Process Improvement:** Analyzing volatility trends can highlight inefficiencies or bottlenecks in the requirements management process, enabling improvements for future projects.

---

#### **Tracking Requirements Across the Lifecycle**

* To effectively track volatility, every requirement addition, modification, or deletion must be documented and **traceable** to its source (e.g., stakeholder request, change request).
* **Stability Over Time:** Metric trends should reflect stability over time. For instance:
  + Post-PDR, total number of requirements changes should plateau.
  + An unexpected increase in changes during implementation suggests risks that must be explored (e.g., misunderstood stakeholder intent or design errors).

#### **Monitor Codebase Stability**

Additionally, tracking changes in the software codebase can provide indirect insight into ongoing requirements volatility and areas of the system that require extra testing rigor.

* Frequent modifications to specific modules could indicate that related requirements are evolving inconsistently, or implementation challenges exist.
* Stability in code changes or fewer rework iterations may align with stabilized requirements.

Refer to **HR-33 - Inadvertent Operator Action** to address broader impacts on operability in systems influenced by late modifications.

## 3.4 Reporting Requirements Volatility Metrics

**Regular Reports to Encourage Stakeholder Transparency**

* Requirements volatility metrics must be reported **regularly** to the **project manager and relevant stakeholders** as part of progress reviews (e.g., Lifecycle Gates, Milestone Reviews, Risk Review Boards):

  + Trend analysis and assessment of requirements changes, focusing on schedule and budget risks.
  + List of all changes, justification for the changes, and associated impacts on downstream phases (e.g., development, integration, testing).
* In addition to project leadership, volatility metrics should be shared with the **Software Engineering Process Group (SEPG)**. The SEPG will use this data to refine organizational processes, improve cost estimation methods, and provide lessons learned for future projects. For instance:

  + How frequently were late-stage requirements changes made?
  + What percentage of the changes were avoidable through better early requirements definition?

---

#### **Metrics to Track and Report**

Metrics should focus on monitoring requirements evolution, assessing impacts on the current project, and guiding future improvements.

**General Metrics to Monitor and Report:**

1. **Scope Metrics:**

   * Total number of requirements (baseline).
   * Number of requirements added, modified, or deleted in a given phase or milestone.
   * Number of TBD/TBR (To Be Determined/To Be Resolved) requirements over time. A high or persistent number indicates incomplete requirement definition.
2. **Rework and Impact Metrics:**

   * **Rework Trends:** Track trends in rework activities triggered by requirements changes.
     + Example: Percentage of completed design documents that required rework due to late-stage requirements evolution.
   * **Cost and Time Impacts:** Quantify the impact of requirements changes in terms of cost (engineering hours) and schedule delays.
3. **Stability Metrics:**

   * The percentage of requirements in the baseline that remain stable or unchanged across milestones.
   * Timeline showing cumulative changes to requirements over critical lifecycle phases.
4. **Change Backlog Metrics:**

   * Number of open (pending) change requests related to requirements. Highlight risks if unresolved changes relate to high-priority requirements.

---

#### **Reporting Schedule and Format**

**Frequency:**

* Metrics should be reported with a consistent cadence, tied to key milestones (e.g., SRR, PDR, TRR, ORR), and as part of periodic project status updates.

**Recommended Reporting Format:**

* **Dashboards:** Visualize trends (e.g., bar graphs, line charts for cumulative changes, volatility by subsystem/module).
* **Risk Summary:** Highlight unresolved TBRs/TBDs and overall requirements evolution risks.

---

#### **Examples of Metrics Reports to Include:**

1. **Number of Changes Over Time:**

   * A line graph showing weekly or monthly changes (e.g., added, modified, deleted) relative to the project schedule milestones.
2. **Cumulative Change Impact:**

   * A summary table detailing requirements added/modified alongside cost and schedule impacts (in hours/days).
3. **Subsystem-Specific Volatility:**

   * A breakdown showing specific subsystems or modules where volatility is concentrated (e.g., power systems, navigation software).

---

#### **Cross-Reference Additional Guidance:**

* For metric analysis reporting, see **SWE-094** (Reporting of Measurement Analysis).
* For related processes on documenting change requests (CRs), refer to **Topic 5.01 – CR-PR (Software Change Request - Problem Report).**

Tracking and reporting requirements volatility metrics are fundamental for enabling the project team to remain adaptive and informed throughout the software lifecycle. The effort helps ensure that projects stay aligned with constraints on cost, schedule, functionality, and performance while also improving efficiency in handling dynamic requirements. Reporting this data transparently supports continuous process improvement and enhances future estimation capabilities through lessons learned analysis.

See also Topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report),

Measure changes in the codebase to monitor stability and identify areas of frequent modification that may need more rigorous testing. [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action), 

See also [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis).

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics) |

# 4. Small Projects

For smaller projects, where resources and schedules are often constrained, the focus should be on a streamlined approach that balances cost and effort with the necessity of understanding and managing requirements volatility. Below is tailored guidance for small projects, highlighting simplified tools, processes, and methods to ensure compliance without overburdening the project team.

---

### **1. Why It Matters for Small Projects**

While small projects may not have the complexity of larger efforts, even modest changes to requirements can disproportionately impact tight schedules, budgets, and resources. Tracking and reporting requirements volatility ensures small projects can:

* Maintain clear scope boundaries and avoid uncontrolled changes.
* Quickly assess the impact of changes without requiring significant time or documentation.
* Provide transparency to stakeholders, preventing late surprises.

---

### **2. Simplified Guidance for Requirements Volatility Metrics**

#### **Step 1: Establish a Lightweight Change Management Process**

* Create a **simple procedure** for capturing, approving, and tracking requirements changes. Key recommendations:

  + Use a shared Excel spreadsheet, Google Sheet, Jira board, or simple tool to manage requirement changes for small projects.
  + Track:
    - **ID/Name of the Requirement**
    - **Type of Change** (Add, Modify, Delete)
    - **Reason for the Change**
    - **Impact** (e.g., time estimate, resource adjustments, or rework descriptions).
    - **Approval Status** (Pending, Approved, Rejected).
* Define **approval criteria** for changes to prevent unnecessary modifications from being pushed through. For instance:

  + Changes impacting the delivery schedule or core functionality must involve the project manager and stakeholders.

> **Example Tool:** Use free task-tracking tools, like Trello or Airtable, for real-time updates and visibility on requirements changes.

---

#### **Step 2: Prioritize Tracking Essential Volatility Metrics**

Focus on metrics that are **most relevant for small projects** and reduce unnecessary data collection. Keep metrics lean and impactful.

**Key Metrics to Track for Small Projects:**

* **Total Number of Requirements:** Provide a baseline count, which serves as a benchmark for detecting the volume of changes.
* **Number of Changes (Add/Modify/Delete):** A simple tally of changes per month or per phase.
* **Open TBD/TBR (To Be Determined/Resolved):** Track unresolved placeholder requirements, such as incomplete definitions or pending approvals.
* **Percentage of Requirements Impacted:** This highlights the scope of volatility.  
  *Formula*:  
  `(Number of Changed Requirements / Total Number of Baseline Requirements) x 100`
* **Effort Estimate for Rework (Optional):** A rough estimate (e.g., # of hours or days) to track how much effort changes are introducing to the project.

**Tracking Example for a Small Project:**  
A small rover software project with 50 total baseline requirements may have the following metrics outcomes:

* Total Requirements: **50**
* Requirements Changed (Last Month): **3 Modified, 1 Added**
* Overall Impact: **8% of Baseline Scope Impacted**

This gives the project manager visibility into the change frequency and whether further scope stabilization is needed.

---

#### **Step 3: Conduct Brief, Impact-Focused Change Assessments**

Small projects should avoid extensive documentation or multi-stage reviews for every requirements change. Instead, conduct brief assessments of each change using a simplified Impact Evaluation Form or Checklist.

**Impact Checklist for Small Projects:** For every requirements change:

1. **What will this requirement change affect?**
   * Design?
   * Implementation?
   * Testing?
   * Schedule?
2. **Does this change carry a cascading impact (e.g., related features or subsystems)?**
3. **Can this change be incorporated without significant rework?**
4. **What is the estimated time (in hours/days) and resources required for the change?**

> **Example Document:** Use a two-column template ("Change Description," "Impact Assessment") in Word/Excel for simplicity.

---

#### **Step 4: Schedule Periodic Metrics Checkpoints**

For small projects, regular reporting does not need to be a labor-intensive task. Plan **short, periodic updates** to review volatility metrics and assess project stability.

**Timing:**

* **Frequency:** Once every 2-4 weeks, or tied to major project milestones.
* **Attendees:** Project manager, developer lead, and key stakeholders.

**Metrics Reporting Format (Simplified):**

* **Summary (1-2 Sentences):** "We had 2 new requirements changes this month. This included one modification to the payload interface design, requiring 2 hours of rework."
* **Key Statistics:**
  + Total requirements.
  + Changes this period and since the project started.
  + Total tasks or work items impacted by changes.
* **Visual Aids (Optional):** Use basic graphs in Excel/Google Sheets for easy visibility.

---

#### **Step 5: Communicate and Learn**

* **Ongoing Communication:** Keep stakeholders in the loop. Requirements volatility metrics can be shared during project updates to highlight the impact of late changes on actual delivery.
* **Post-Project Analysis:** Once the project is completed, record lessons learned. For instance:
  + What drove the majority of changes (stakeholders, technical gaps, unclear early requirements)?
  + How could the process for tracking requirements have been improved?

---

### **3. Best Practices Tailored for Small Projects**

#### **1. Start Small, Keep It Simple:**

For a small software project, sophisticated tracking tools and processes are unnecessary. Use shared documents (like spreadsheets) or free tools (like Trello boards or Notion) to organize requirements changes effectively without over-complication.

#### **2. Focus on Stabilization:**

As a small project often has faster lifecycles, strive to stabilize requirements as early as possible. Identify any TBDs early and ensure all open gaps are resolved before the implementation phase begins.

#### **3. Minimize Rework Through Early Alignment:**

Actively engage stakeholders during requirements definition to minimize late-stage changes. The smaller the project, the more impactful even one or two changes late in development can be.

#### **4. Automate Where Possible:**

For very small teams, integrate lightweight automation. For example:

* Track requirement changes alongside code updates in version control tools like **Git**.
* Use built-in reporting in tools like **Jira**, **Asana**, or **[Monday.com](http://Monday.com)** to monitor progress and change trends automatically.

#### **5. Learn From Metrics Over Time:**

Even on small projects, tracking requirements volatility provides valuable insight for efficiency in future missions. Document key takeaways:

* What types of requirements were prone to changes?
* Were stakeholders fully engaged during early requirements activities?
* What tools/processes worked best for tracking and managing changes?

---

### **4. Example Scenario: Small Satellite Project**

#### **Scenario:**

A team is developing software for a small CubeSat mission. The project has limited resources (4 developers, 6-month schedule) and 40 requirements.

**Steps Taken:**

1. **Change Log Established:** A simple Google Sheet is created, tracking all changes (ID, type, rationale, impact).
2. **Basic Metrics Tracked:** Total requirements, number of changes, percentage impacted, and estimated rework effort are updated bi-weekly.
3. **Stakeholder Alignment:** The project manager holds quick stand-up meetings every two weeks to review volatility metrics.
4. **Lightweight Impact Assessment:** Any change that impacts integration or extends testing time requires a one-paragraph analysis to assess risks.

**Metrics Results After 3 Months:**

* Total Requirements: 40
* Number of Changes: 4 (10% impact).
* Iterative Improvements: Realized that stakeholder misalignment early in interface requirements caused 50% of the changes; additional review steps are added for future projects.

For small projects, focusing on **simple tools**, **essential metrics**, and **streamlined processes** will minimize overhead while enabling successful tracking and reporting of requirements volatility. This ensures scope stability, informed decision-making, and well-managed project outcomes within the constraints of small-scale missions.

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

Tracking, monitoring, and reporting requirements volatility is a critical aspect of software engineering at NASA. Numerous lessons learned have been documented from past projects that emphasize both the importance of managing requirements changes and the practical challenges of implementing a robust process for requirements volatility metrics. Below are some relevant lessons learned derived from NASA’s experience, reflecting the value of proactive requirements management and its role in project success.

---

### **Lesson 1: Requirements Volatility Can Cause Cost Growth and Delays**

**Case Study:** The **James Webb Space Telescope (JWST)** encountered significant scope growth and delays due to late-identified or evolving requirements.

* **Problem:** Requirements changes later in the lifecycle resulted in extensive rework during integration and testing, heavily impacting schedule and cost.
* **Lesson Learned:** Requirements volatility is directly correlated with cost and schedule risks. Tracking and reporting volatility metrics allows visibility into evolving requirements, enabling stakeholders to prioritize changes and mitigate impacts more effectively.
* **Actionable Insight:** Post-PDR changes should be minimized and required changes should be scrutinized for their necessity and cascading impacts. Implement a process that evaluates each requirement change based on its impact on project constraints (time, budget, and risk).

---

### **Lesson 2: Incomplete Early Requirements Increase Risk of Volatility**

**Case Study:** The **Space Shuttle Integrated Main Propulsion System Software** suffered from incomplete early requirements, which led to ongoing changes in the implementation phase.

* **Problem:** Many critical requirements were missing at System Requirements Review (SRR) or were too vague, requiring repeated clarification and revision during development. Misaligned expectations among teams worsened the problem.
* **Lesson Learned:** Early refinement and stabilization of requirements (and reduction of TBDs/TBRs at SRR and PDR) is critical to reduce volatility later in the lifecycle.
* **Actionable Insight:** Implement formal reviews of requirements completeness with stakeholders early in the project. Integrate requirements traceability tools to flag unresolved or incomplete requirements. For smaller projects, emphasize resolving TBDs/TBRs before design phases begin.

---

### **Lesson 3: Requirements Changes Often Cascade to Subsystems and Interfaces**

**Case Study:** During the development of the **Mars Climate Orbiter**, a small change to a requirement governing interface behavior resulted in misalignment between software subsystems, leading to the infamous system failure due to mismatched unit conversions.

* **Problem:** A seemingly small change to one requirement (related to subsystem input/output) created larger cascading impacts that were not fully analyzed or accounted for, resulting in system-wide issues during mission operations.
* **Lesson Learned:** Even minor requirements changes can propagate to multiple interdependent subsystems or interfaces, amplifying their impact. Tracking and reporting requirements volatility must include assessing downstream impacts on interfaces.
* **Actionable Insight:** For every requirement change, perform an "impact analysis" that includes subsystems, interfaces, performance requirements, and testing. Maintain traceability across subsystems to highlight dependencies.

---

### **Lesson 4: Poor Configuration Control Exacerbates Volatility Impact**

**Case Study:** During the development of **Hubble Space Telescope Ground Systems**, poorly managed configuration control led to conflicting versions of requirements being implemented by different teams, creating delays and integration mismatches.

* **Problem:** Lack of central oversight and metrics reporting for versioned requirements changes caused multiple teams to work on outdated or misunderstood requirements. This led to duplicated efforts and unrecoverable resource losses.
* **Lesson Learned:** Strong configuration control and communication of requirements changes are crucial to managing volatility. Ensure all team members are working from an "approved" baseline that is updated and version-controlled after each requirement change.
* **Actionable Insight:** Use automated tools or repositories (e.g., Jira, Git, or NASA's tailored configuration tools) to track and annotate requirements evolution. Any requirement that changes must trigger immediate notification to all affected teams.

---

### **Lesson 5: Requirements Volatility Should Be Monitored in Both Development and Operations**

**Case Study:** The **International Space Station (ISS)** software faced ongoing requirements changes after deployment due to evolving operational needs and updates to hardware.

* **Problem:** Requirements volatility was seen not only during the development phases but also during post-deployment operation, requiring frequent updates to performance and functional requirements. These changes often required urgent rework, creating unexpected cost and schedule burdens.
* **Lesson Learned:** Requirements management is an ongoing process that extends beyond initial implementation and development. For long-duration missions or software with extended lifecycles, volatility should be tracked in both development and operations to allow early forecasting of update needs.
* **Actionable Insight:** Establish a lightweight volatility monitoring process for operational updates. Post-deployment changes should be evaluated for cost and risk impact just as they are during initial development. Include this process in your software maintenance plan.

---

### **Lesson 6: Small Projects Are Not Exempt from the Risks of Volatility**

**Case Study:** During the development of **SmallSat projects**, there was an assumption that fewer requirements or a smaller team would naturally limit volatility. However, rapid development cycles meant that even small requirement changes disproportionately disrupted schedules.

* **Problem:** This assumption led to limited oversight of volatility, which caused disjointed development efforts and late-stage testing failures. For example, a single requirement modification about payload data caused rippling effects across onboard telemetry systems, delaying software testing.
* **Lesson Learned:** Tracking requirements volatility, even for small projects, ensures that short development cycles are not derailed by undetected changes. Small projects suffer a greater impact from uncontrolled change due to smaller margins for error.
* **Actionable Insight:** Implement lightweight requirements tracking for small projects (e.g., spreadsheets or Trello boards). Use time-limited change windows (e.g., weekly reviews) to stabilize scope during development.

---

### **Lesson 7: Volatility Metrics Improve Future Cost and Schedule Estimation**

**Case Study:** In hindsight, projects like **Curiosity Rover** showed that analyzing historical requirements volatility data enhanced the ability to estimate costs and risks for successor projects such as the **Perseverance Rover**.

* **Problem:** Early cost and schedule estimates consistently underestimated the time and resource requirements for handling requirements-driven rework. Without tracking volatility metrics thoroughly, teams were unable to accurately predict impacts.
* **Lesson Learned:** Volatility metrics are not just for managing the current project but also provide valuable insights for estimating costs, schedules, and risks for future missions. By recording trends (e.g., requirements changes per phase or subsystem), teams can better anticipate impacts.
* **Actionable Insight:** Ensure volatility metrics (e.g., number of changes, rework costs) are archived alongside lessons learned. Review them during planning phases of follow-on projects. Regularly communicate these insights to the Software Engineering Process Group (SEPG).

---

### **Applicable NASA Lessons Learned Repository Entries**

Some entries directly related to requirements volatility can be found in NASA’s **Lessons Learned Information System (LLIS)**. Detailed examples include:

* **LLIS-0441:** Cost Growth Due to Late Requirements Changes
* **LLIS-0574:** Ensuring Traceability for Requirements Changes
* **LLIS-0888:** Interface Management and Propagation of Requirements Changes
* **LLIS-1593:** Lessons Learned in Small Satellite Projects

---

### **Key Takeaways**

1. **Control Early-Stage Volatility:** The majority of requirements volatility should be addressed and resolved before PDR.
2. **Assess Downstream Impacts:** Changes can magnify risks when they involve interdependent subsystems or interfaces.
3. **Simplify for Small Projects:** Small teams must track volatility with lightweight tools and methods to avoid resource strain.
4. **Utilize Metrics for Continuous Improvement:** Historical volatility data must inform future project planning to reduce risk and improve predictability.

These lessons emphasize the importance of managing requirements volatility at all stages, regardless of project size or complexity, to ensure mission success and minimize development risks.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Control GN&C algorithm changes with the same rigor as software requirements changes](https://software.gsfc.nasa.gov/lesson-details/111/). **Lesson Number 111**: The recommendation states: "Control GN&C algorithm changes with the same rigor as software requirements changes. The algorithm document needs to baselined and subsequently controlled like any other requirement.."
* [Design for volatility](https://software.gsfc.nasa.gov/lesson-details/336/). **Lesson Number 336**: The recommendation states: "Consider design choices that make the FSW design more robust to changing requirements."

# 7. Software Assurance

**SWE-200 - Software Requirements Volatility Metrics**

5.4.6 The project manager shall collect, track, and report software requirements volatility metrics.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project collects, tracks, and reports on the software volatility metrics.

2. Analyze software volatility metrics to evaluate requirements stability as an early indicator of project problems.

## 7.2 Software Assurance Products

Software Assurance (SA) plays a critical role in analyzing, monitoring, and mitigating the impacts of requirements volatility on cost, schedule, and quality. The SA team provides insight into risks and trends associated with requirements changes to improve confidence in meeting mission objectives.

**Key Products Delivered by SA Include:**

1. **Analysis of Software Volatility Measures:**

   * Comprehensive analysis of software requirements volatility trends, tracked over project phases to identify risks arising from frequent or late-stage changes.
   * Highlighting dependencies between requirements volatility and software quality issues, cost overruns, and schedule delays.
2. **Software Measurement and Metric Data:**

   * Collection of data showing requirements volatility (e.g., specific metrics for requirements added, deleted, modified, and unresolved TBD/TBR items).
   * Identification of metrics trends and predictive insights into areas of potential instability.
3. **Trend and Impact Analysis Results:**

   * Detailed results from trend analysis reports demonstrate how requirements volatility evolves over time and correlates to project metrics such as quality defects, rework effort, integration bottlenecks, and risk exposure.
4. **Status Presentations of Metrics and Trends:**

   * Regular updates delivered in milestone reviews and project manager briefings (e.g., PDR, CDR, TRR), summarizing requirements volatility data, visualized trend graphs, and associated recommendations for mitigating risks.

## 7.3 Metrics

Tracking requirements volatility requires monitoring specific metrics that provide visibility into change frequency, scope evolution, and resulting impacts across the project lifecycle.

**Key Metrics for Requirements Volatility Include:**

* **Number of Requirements Added:** Tracks new requirements introduced during development. Indicates scope growth and potential stress on project resources.
* **Number of Requirements Deleted:** Monitors scope reduction, which may impact baseline functionality.
* **Number of Requirements Modified:** Shows how many existing requirements were updated due to clarifications or late-stage stakeholder changes.
* **Number of TBDs or TBRs Over Time:** Identifies unresolved requirements placeholders, pointing to areas of uncertainty in the project scope.
* **Ratio of Changed Requirements to Total Requirements:** Provides quantitative insight into how much of the requirements baseline has been affected by volatility.

**Note:** Metrics in bold type are required for all projects across NASA to ensure consistent measurement practices.

*Reference:* See **Topic 8.18 - SA Suggested Metrics** for additional metrics applicable across software assurance activities.

## 7.4 Guidance

Requirements volatility refers to the **frequency and magnitude of changes** to software requirements (addition, deletion, modification) within a defined period during the lifecycle. Managing requirements volatility is critical for ensuring project success, as requirements serve as the foundational basis for project schedules, software design, and test specifications.

---

**Guidance on Software Volatility Management:**

* **Early Lifecycle Volatility is Expected:**  
  In the conceptualization and requirements phase, requirements volatility is considered normal as teams refine unclear or missing requirements. During SRR and PDR, the volatility trend typically decreases as requirements converge and stabilize.
* **Post-PDR Volatility Raises Concerns:**  
  After PDR, especially after software requirements have been finalized and designs are baselined (post-CDR), late-stage requirements changes often result in costly rework and ripple effects across development, integration, and testing phases. These changes should undergo formal rigor, including automated tracking, traceability, and impact analysis.
* **Why Requirements Volatility Matters:**  
  Uncontrolled requirements volatility has substantial impacts on:

  + **Cost:** Increased costs due to rework activities, resource adjustments, and testing.
  + **Schedule:** Delays in milestones such as integration testing and verification activities due to updated changes.
  + **Quality:** Higher risk of introducing defects, particularly in coding and testing phases, from changes propagating through requirements, interfaces, and modules.
  + **Software Maintenance:** Continuous changes complicate defect resolution and regression testing during maintenance phases.
  + **Project Performance:** Unstable requirements often cause downstream inefficiencies and misalignment between engineering teams and stakeholders.

---

#### **Examples and Key Insights:**

1. **Volatility During Development:**  
   Even when projects begin with well-defined requirements, requirements may evolve during the development phase as new user needs are clarified or technical constraints arise. Requirements volatility during this phase should be monitored to avoid cascading impacts.
2. **Volatility After Requirements Phase:**  
   Changes after the software requirements phase should be minimized, as late-stage fluctuation disrupts schedules, increases errors, and forces teams to rework tested and integrated components. Requirement changes during implementation or testing phases often have amplified impacts compared to changes during early development.
3. **Impact of Volatility Across Key Metrics:**  
   Tracking requirements volatility metrics helps Software Assurance identify project risks early, enabling teams to stabilize requirements and minimize cascading effects. Effective requirements volatility management has the potential to prevent project failure and improve stakeholder alignment.

---

### **Common Causes of Requirements Volatility (Internal and External Factors):**

* **External Factors:**

  + Regulatory changes (e.g., government compliance rules).
  + Project scope changes due to funding adjustments.
  + Customer-driven updates or mission profile changes.
* **Internal Factors:**

  + Unresolved hardware or interface constraints.
  + Lack of team experience in system and software requirements definition.
  + Feedback from milestone and peer reviews introducing stakeholder-driven changes.
  + Poor communication across stakeholders and engineering teams.
  + Complexity of the mission and interdependencies between hardware, software, and operations.
  + Hazard identification processes triggering major requirement updates.

---

**Challenges Contributing to Requirements Volatility:**

* **Inadequate Change Request Management:**

  + Change requests often lack sufficient reasoning or justification.
  + Impact analyses tied to individual requirements changes are rarely thorough or standardized.
* **Incomplete Traceability:**

  + Lack of bidirectional traceability between requirements and downstream artifacts (e.g., code, tests) disrupts visibility into potential impacts.
  + Reference: See **SWE-052 - Bidirectional Traceability** for best practices in requirements traceability.
* **Communication Gaps:**

  + Lack of clarity in communication between stakeholders and engineering teams leads to frequent misunderstandings or mismatches between requirements and final implementation.

---

#### **Positive Effects of Requirements Volatility:**

While requirements volatility is often seen as a risk, it can have positive impacts:

1. **Improved Requirements Understanding:** Continuous iterations on requirements provide opportunities to refine, clarify, and better align development outcomes with user needs.
2. **Innovation Opportunities:** Requirements modifications can introduce opportunities to enhance system performance or address unforeseen user needs.
3. **Adaptability:** Reactive changes during development enable software teams to remain flexible to mission scope evolution.

---

**Takeaway:**  
Although requirements volatility may have some positive effects, its **negative impacts far outweigh the positives** when not managed. Requirements volatility must be tracked diligently, analyzed for its effects on cost, schedule, quality, and utilized proactively to stabilize project outcomes.

Develop a **requirements volatility trending mechanism** to flag risk areas and improve alignment among development teams, stakeholders, and mission planners. Measuring, analyzing, and reporting requirements volatility metrics provides strong assurance that project risks are being identified, tracked, and controlled effectively.

---

Software Assurance Recommendations:

1. Establish clear requirements volatility thresholds post-PDR to identify unstable areas and enforce risk controls.
2. Use automated tools for tracking requirements, comparing changes against baselines, and calculating impacts to cost or rework efforts.
3. Provide stakeholders and project managers with visualized metrics dashboards showing:
   * Number of requirements changes.
   * Trending graphs for changes by phase (SRR, PDR, CDR, etc.).
   * Estimated impacts on cost and risk.
4. Integrate bidirectional traceability tools to improve the ability to assess impacts across subsystems efficiently (SWE-052).

By managing requirements volatility effectively, NASA projects can ensure improved project stability, cost-efficiency, and final product quality while minimizing disruption risks.

Examples:

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence refers to tangible and verifiable artifacts, reports, and data that demonstrate compliance with the requirement to monitor, track, and report requirements volatility metrics. For this requirement, objective evidence should showcase that processes are being followed, metrics are being tracked, and the project manager is informed of the impact of requirements changes on project cost, schedule, and quality.

---

### **Types of Objective Evidence for Requirements Volatility**

Below is a structured list of artifacts and activities that serve as objective evidence for this requirement. These may vary slightly based on the project size and classification (e.g., Class A, B, or C software).

---

#### **1. Documentation of Requirements Changes**

Artifacts that demonstrate that requirements changes are identified, documented, and tracked systematically:

* **Change Logs** or a **Requirements Change Database**, including:
  + Unique requirement IDs.
  + Nature of the change (added, deleted, modified).
  + Date of the change.
  + Justification or reason for the modification (e.g., stakeholder-driven, technical constraint).
  + Impact analysis (schedule, cost, quality, subsystem dependencies).
  + Approval status (e.g., pending, approved, rejected).
* **Change Request Forms:**
  + Completed forms that specify the rationale, impacts, and traces to affected artifacts, demonstrating that all changes undergo formal impact analysis.

---

#### **2. Requirements Management System Outputs**

If automated tools (e.g., DOORS, Jira, Jama Connect, or a custom database) are used for managing requirements:

* Reports extracted from the tool showing:
  + **Baseline Requirements:** Initial list of approved software requirements.
  + **Version History:** Full audit trail showing additions, modifications, and deletions.
  + **TBD/TBR Tracking:** Trends of unresolved "To Be Determined" or "To Be Resolved" placeholders over time.
  + **Traceability Reports:** Bidirectional traceability between requirements, design, testing, and code artifacts to confirm the impact of changes is evaluated.

> **Example:** A formal export from Jira showing a summary of requirements changes annotated with associated user stories and subtasks.

---

#### **3. Requirements Volatility Metrics and Reports**

Artifacts that demonstrate the systematic collection, analysis, and reporting of volatility:

* **Requirements Volatility Metrics:**
  + Summary metrics showing the number of requirements added, modified, deleted, and outstanding TBD/TBRs.
  + *Example Table:*

| Time Period | # Added | # Modified | # Deleted | # TBD/TBRs Resolved | % of Baseline Changed |
| --- | --- | --- | --- | --- | --- |
| Q1 2023 | 5 | 3 | 2 | 8 | 10% |
| Q2 2023 | 2 | 1 | 0 | 5 | 5% |

* **Trend Analysis Reports:**

  + Graphical outputs showing the volatility trend over time, such as bar graphs or line charts that track cumulative changes to the requirements baseline.
  + Highlight commentary identifying root causes of volatility spikes at specific intervals.
* **Status Presentations:**

  + Presentations delivered at milestone reviews (e.g., PDR, CDR, TRR) that include historical volatility trends, open TBDs/TBRs, impacts on cost and schedule, and associated risks.
  + *Evidence:* A slide deck or project review minutes documenting that the SA team presented metrics for volatility tracking.

---

#### **4. Risk Management Evidence**

Demonstrates that requirements volatility is incorporated into the project’s risk management process:

* **Risk Analysis Reports:**

  + Evidence that the risks associated with requirements volatility (e.g., rework, integration disruptions) are identified, analyzed, and tracked in the project’s risk register.
  + Associated mitigation plans for volatility, such as engaging stakeholders earlier in the design or holding additional reviews.
* **Risk Assessments:**

  + Correlation between requirements volatility metrics and the likelihood of schedule/budget risks, validated through impact analysis.

> **Example Artifact:** Risk Register entry that states, “Late-stage requirements volatility may increase rework efforts, delaying delivery by 6 weeks.”

---

#### **5. Process Compliance Evidence**

Demonstrates that standard processes for managing requirements volatility are being followed:

* **Configuration Control Board (CCB) Records:**
  + Meeting minutes, attendee lists, and decisions made during formal reviews of requirements changes. Demonstrates that each change was rigorously evaluated before being implemented.
* **Baseline Reviews:**
  + Approval records from System Requirements Review (SRR), Preliminary Design Review (PDR), and Critical Design Review (CDR), including evidence of requirements baseline stability and volatility metrics presented at these reviews.
* **Process Audit Results:**
  + Results of internal or external audits confirming adherence to requirements volatility tracking and reporting processes, including compliance with relevant NASA standards (e.g., SWE-052 - Bidirectional Traceability).

---

#### **6. Rework and Impact Evidence**

Artifacts demonstrating the downstream impacts of requirements volatility:

* **Rework Logs:**
  + Records of rework activities, showing tasks or modules needing changes/retesting due to late requirements modifications.
  + Metrics capturing rework time, effort, and associated costs (staff hours, budget impacted).
* **Testing Impact Reports:**
  + Evidence of adjusted test plans or regression tests triggered by changed requirements, with an assessment of associated costs.

> **Example Artifact:** A regression testing report showing areas impacted by a requirements change, along with defect/missed dependency trends tied to volatility.

---

#### **7. Lessons Learned Documentation**

Artifacts demonstrating that lessons about requirements volatility from the current project are collected and analyzed:

* **Post-Project Review Reports:**
  + Summarized analysis of how requirements volatility impacted project outcomes (time, cost, quality).
  + Recommendations on improving requirements management for future projects.

> *Example Artifact:* A section in the Final Mission Report discussing volatility metrics during the project lifecycle and lessons learned for similar future endeavors.

---

### **Example Objective Evidence by Project Phase**

Here is a breakdown of evidence that may be generated across different lifecycle phases:

| **Phase** | **Objective Evidence** |
| --- | --- |
| **Concept Phase (Pre-PDR)** | Initial baseline requirements, instability metrics, TBD/TBR tracking, and stakeholder review sign-off. |
| **Preliminary/Design (PDR/CDR)** | Baseline refinement, requirement changes (logs or database), and formal presentations of metrics at design reviews. |
| **Implementation** | Change requests, requirements-to-code traceability reports, analysis reports demonstrating cost/schedule delays. |
| **Testing and Verification** | Logs of requirements-triggered rework, regression testing reports, change impacts on testing resources. |
| **Post-Deployment** | Final volatility report, lessons learned documentation, and metrics trends over the full lifecycle. |

---

### **Connection to NASA Standards**

The objective evidence aligns with key SWE requirements for traceability, measurement, and reporting. References include:

* **SWE-052:** Ensures bidirectional traceability between requirements and downstream artifacts.
* **SWE-094:** Guides reporting of measurement and analysis results, including requirements volatility metrics.
* **SWE-085:** Emphasizes the maintenance of records for software assurance and software engineering activities, including tracking volatility risks.

---

### **Summary of Key Objective Evidence:**

1. Requirements change logs and CCB decisions.
2. Volatility metrics and trend analysis reports.
3. Traceability reports demonstrating requirements-to-design and requirements-to-testing links.
4. Presentation slides from milestone reviews showing status updates on volatility impacts.
5. Risk register items reflecting volatility impact and mitigation strategies.
6. Rework effort tracking, including cost/schedule impacts due to late changes.
7. Final lessons learned documentation and volatility insights for future projects.

By producing this objective evidence, NASA projects can ensure that requirements volatility risks are tracked, reported, and mitigated appropriately while supporting project success and continuous improvement.

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
