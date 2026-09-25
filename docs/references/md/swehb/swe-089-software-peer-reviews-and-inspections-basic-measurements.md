# SWE-089 - Software Peer Reviews and Inspections - Basic Measurements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695474. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements

SWE-089 - Software Peer Reviews and Inspections - Basic Measurements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695474)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695474&showCommentArea=true&showComments=true#addcomment)

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

5.3.4 The project manager shall, for each planned software peer review or software inspection, record necessary measurements. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-089 History

SWE-089 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.3.4 The project shall, for each planned software peer review/inspection, record basic measurements. |
| Difference between A and B | No change |
| B | 5.3.4 The project manager shall, for each planned software peer review or software inspection, record basic measurements. |
| Difference between B and C | Changed "basic" to "necessary" measurements |
| C | 5.3.4 The project manager shall, for each planned software peer review or software inspection, record necessary measurements. |
| Difference between C and D | No change |
| D | 5.3.4 The project manager shall, for each planned software peer review or software inspection, record necessary measurements. |

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
| * [A.10 Software Peer Reviews and Inspections](/spaces/SWEHBVD/pages/133235386/A.10+Software+Peer+Reviews+and+Inspections) |

# 2. Rationale

As with other engineering practices, it is important to monitor defects, pass/fail results, and effort. This is necessary to ensure that peer reviews and software inspections are being used appropriately as part of the overall software development life cycle, and to be able to improve the process itself over time. Moreover, key measurements are required to interpret inspection results correctly. For example, if very little effort is expended on an inspection or key phrases (such as individual preparation) are skipped altogether, it is very unlikely that the inspection will have found a majority of the existing defects.

The rationale behind **Requirement 5.3.4** is to ensure that **software peer reviews and inspections** are not only conducted effectively but also produce measurable data that allows for **process evaluation, improvement**, and **informed decision-making**. By recording necessary measurements during each peer review or inspection, NASA ensures that the activities contribute to improving the software's quality, the review process, and the overall project management efforts.

---

### **Key Reasons for Recording Measurements:**

#### **1. Improve Software Quality**

Tracking and analyzing measurement data from each peer review or inspection helps ensure that **defects** and **process issues** are identified and addressed early in the development lifecycle.

* **Why It Matters:**
  + Significant defects in requirements, designs, code, or test artifacts often lead to **costly rework** and even **mission failures** if not addressed early.
  + Collecting metrics such as the number and severity of defects found helps verify the **effectiveness** of peer reviews in detecting issues.
* **Benefit:**
  + Higher quality work products result in fewer defects during testing and operational phases, enhancing software reliability and reducing risks for critical NASA missions.

---

#### **2. Drive Process Improvement**

Measurements collected from peer reviews provide insights into the **effectiveness of the review process** itself, allowing for iterative improvement.

* **Why It Matters:**
  + Without data, it is challenging to evaluate whether the peer review process is efficient in identifying non-conformances or if the process is being followed consistently.
  + Metrics such as **participant preparation time**, **time spent in reviews**, and defect density can reveal inefficiencies in the review process (e.g., inadequate preparation or incomplete artifacts).
* **Benefit:**
  + NASA teams can use these measurements to refine peer review methods, update checklists, improve preparation protocols, select better participants, and optimize resource allocation.

---

#### **3. Enable Defect Tracking and Trend Analysis**

Recording defect-related measurements during each review allows teams to track **trends** over time and across different lifecycle phases or work products.

* **Why It Matters:**
  + Defect trends (e.g., recurring issues in similar areas of the codebase or documents) can indicate systemic problems that need to be addressed (e.g., inadequate training, unclear requirements, or recurring design flaws).
  + Data such as **defects found per lifecycle phase**, **open vs. closed defects**, and the **time taken to close defects** enables early identification of project risks.
* **Benefit:**
  + Trend analysis provides actionable insights to **prevent defects at the source**, reduce review cycle time, and ultimately deliver higher-quality software.

---

#### **4. Support Metrics-Driven Decision-Making**

Captured peer review measurements provide valuable data that guide **project management decisions**.

* **Why It Matters:**

  + Decisions regarding resource allocation, schedule adjustments, and risk mitigation need to be grounded in evidence (rather than assumptions).
  + For example:
    - Do the metrics indicate a need for additional peer reviews in areas of high defect density or high mission risk?
    - Is the team spending excessive time preparing for reviews compared to the defects identified, suggesting better checklists or training may be needed?
* **Benefit:**

  + Empirical, metrics-driven decision-making enables projects to not only remain compliant with NPR 7150.2 requirements but to also allocate resources and mitigate risks with higher confidence and precision.

---

#### **5. Ensure Compliance and Traceability**

Recording and preserving peer review measurements ensures compliance with NASA standards (e.g., NPR 7150.2, NASA-STD-8739.8/9) while providing full **traceability** for auditing, reporting, and documentation purposes.

* **Why It Matters:**
  + Compliance with NASA standards requires evidence that peer reviews are conducted properly and consistently.
  + Captured metrics provide objective evidence to demonstrate due diligence in carrying out reviews in a systematic, traceable, and measurable manner to prevent deviations from required practices.
* **Benefit:**
  + Compliance assurance fosters accountability, reinforces traceability, and builds confidence among stakeholders, ensuring the software development process is aligned with mission needs.

---

#### **6. Foster Stakeholder Confidence**

Recorded metrics and their trends can be used to build **stakeholder trust** by showing that peer review and inspection processes are robust, iterative, and producing measurable results.

* **Why It Matters:**

  + Peer reviews occur at the intersection of process oversight, quality assurance, and technical rigor. Validating these activities with measurable metrics reassures stakeholders that their expectations for quality, safety, and compliance are being met.
  + Sharing metrics with leadership allows for transparent discussions about risks, process maturity, and quality goals.
* **Benefit:**

  + Confidence in peer review processes and documented measurements helps secure stakeholder alignment, continued funding, and buy-in for iterative process improvements.

---

#### **7. Enable Accountability Across Teams**

Measurements from reviews establish a clear **record of responsibilities** for participants and their contributions to defect identification and resolution.

* **Why It Matters:**

  + Metrics such as "number of defects identified per participant" or "number of defects remaining unresolved" help ensure that personnel remain accountable for their roles in peer reviews.
  + Metrics also confirm that project managers, reviewers, and software assurance personnel are actively addressing issues.
* **Benefit:**

  + Fosters individual and team accountability, driving thorough defect resolution and minimizing risks caused by overlooked problem areas.

---

#### **8. Facilitate Lessons Learned**

Properly recorded measurements allow teams to evaluate **lessons learned** from peer reviews and inspections and to apply these lessons to future projects.

* **Why It Matters:**

  + Peer review metrics help organizations understand recurrent issues, identify best practices, and create knowledge repositories that can improve future project practices.
  + For example, noticing that a specific artifact type (e.g., requirements) consistently produces a high number of defects can guide teams to invest in better artifact preparation.
* **Benefit:**

  + Captures institutional knowledge and facilitates continuous improvement across NASA projects.

---

### **Examples of Measurements to Record:**

To fulfill this requirement, the following **quantifiable metrics** should be documented:

1. **Defect Metrics:**

   * Number of defects by type (e.g., major, minor, critical).
   * Number of defects per phase (e.g., requirements, design, code).
2. **Process Metrics:**

   * Time spent by participants preparing for peer reviews.
   * Total time spent during peer review meetings.
   * Time to resolve and close defects.
3. **Participation Metrics:**

   * Number of participants vs. number invited.
   * Preparation time per participant.
   * Defects found per reviewer.
4. **Compliance and Audit Metrics:**

   * Number of peer reviews planned vs. performed.
   * Number of process non-conformances identified during reviews.
   * Number of discrepancies found during compliance audits.

---

### **Conclusion**

Recording necessary measurements for peer reviews and inspections ensures that these activities remain impactful, measurable, and aligned with both project goals and NASA standards. These measurements serve as a foundation for **improving software quality, ensuring compliance, optimizing processes**, and **building stakeholder trust**. By adopting a metrics-driven approach, NASA projects maximize the effectiveness of peer reviews and reduce mission risks.

# 3. Guidance

## 3.1 Best Practices

#### **Importance of Best Practices**

NASA-STD-8739.9 captures lessons learned from software engineering practitioners, and formal inspections and peer reviews have proven to be effective when implemented systematically. Peer reviews and inspections should focus on **early defect detection** and **process compliance**, ensuring adherence to standards, and continuous improvement.

#### **Recommended Best Practices**

1. **Collect and Use Inspection Data Effectively**

   * Maintain consistent policies to collect, analyze, and use peer review and inspection data, including:

     + **Effort Metrics**: Record preparation time spent by reviewers, meeting duration, and follow-up effort.
     + **Participants**: Document the total number of reviewers and their roles (e.g., moderator, recorder, reviewer).
     + **Defect Metrics**: Track the number and classification of defects (e.g., critical, major, minor) found and their resolution status (e.g., open, closed).
     + **Artifact Outcomes**: Record the pass/fail criteria for artifacts (e.g., requirements, test procedures) and the rationale for decisions.
   * Use data from inspections to identify **root causes** of defects, recurring problem areas (e.g., ambiguous requirements, flawed designs), and **process inefficiencies**.
2. **Review Appropriateness of Peer Reviews and Inspections** To ensure maximum benefit, evaluate whether peer reviews are targeting appropriate artifacts and being applied effectively:

   * **Target Artifacts**: Confirm that inspections prioritize artifacts most prone to defects and mission-critical risks (e.g., requirements, test plans).
     + Refer to SWE-087 rationale that highlights inspections as particularly beneficial for early lifecycle artifacts like **requirements specifications** and **design diagrams**, where defects are cheaper to fix.
   * **Coordination with Other V&V Activities**: Assess whether peer reviews complement or duplicate other verification and validation (V&V) processes (e.g., unit testing, automated static analysis). Avoid inefficiencies by ensuring peer reviews address defects **not easily caught by other techniques**.
3. **Ensure Inspection Process Integrity** Effective peer reviews depend on strict adherence to inspection processes:

   * **Avoid Tailoring Away Key Steps**: Skipping steps such as **planning**, **preparation**, or excluding participants with critical expertise diminishes inspection quality.
   * **Selection of Participants**: Ensure diverse team perspectives (e.g., requirements developer, coder, tester, software assurance) to identify defects across domains.
   * **Quality Checklists and Structure**: Use artifact-specific checklists tailored to NASA standards (e.g., NPR 7150.2, NASA-STD-8739.9) to focus on common defect patterns and criteria for compliance.
4. **Leverage Lessons Learned**

   * Incorporate lessons learned from past reviews to improve processes. For instance, recurring defects or missed issues may trigger updates to checklists, training, or preparation protocols.

#### **Key Questions to Address**

Where peer reviews and inspections produce less-than-expected results, consider the following:

* Are appropriate artifacts being reviewed? See Topic 7.10 for guidance on artifact prioritization and the benefits of checklists.
* Are review processes complementing other V&V activities without redundancy?
* Are inspection practices being followed rigorously, or are critical steps (planning, preparation) being skipped?
* Is the team equipped with sufficient domain expertise, diversity of perspectives, and training?

Refer to **Topic 5.03: Inspect—Software Inspection, Peer Reviews, Inspections** for additional details.

## 3.2 Collection and Analysis of Data

#### **Importance of Data Collection and Analysis**

Inspection data provides measurable insights into the efficiency, effectiveness, and impact of peer reviews. Proper collection and analysis practices ensure data accuracy and enable evidence-based decisions.

#### **Recommended Best Practices**

1. **Triggers for Data Collection and Analysis**

   * Define **clear triggers** for when metrics are collected and analyzed:
     + Post-inspection review meetings.
     + Periodic updates (e.g., monthly or per milestone).
     + Project audits or compliance evaluations.
2. **Assignment of Responsibilities**

   * Assign **individual roles** for collecting and analyzing inspection data:
     + Moderators compile and report inspection results.
     + Project managers specify the format and location of the recorded data.
     + Software assurance personnel verify data consistency.
3. **Consistency in Data Collection**

   * Ensure all recorded data uses consistent units of measurement and definitions:
     + If effort is recorded in person-hours, maintain that standard across inspections.
     + Clearly define defect categories, severity levels, and terms like "effort" or "inspection rate."
4. **Data Verification and Outlier Investigation**

   * Investigate metrics that deviate from norms (outliers) to check for errors or deeper issues:
     + Examples of outliers:
       - Higher-than-usual defect rates in one artifact type may indicate systemic documentation problems.
       - Excessive preparation time for one team may suggest clarity issues in the provided materials.
5. **Periodic Analysis of Inspection Data**

   * Perform regular analyses of inspection metrics to monitor progress and understand costs vs. benefits:
     + **Metrics to Monitor**:
       - Number of inspections planned vs. completed.
       - Rate of inspections (e.g., artifacts reviewed per hour).
       - Density and closure time of defects across lifecycle phases.
6. **Support Continuous Improvement** Use insights from recorded data to refine:

   * Checklists for artifacts.
   * Participant training protocols.
   * Scheduling guidelines and team selection criteria.

## 3.3 Metrics for Projects Using Acquisition

#### **Importance of Metrics in Acquisition Context**

Metrics play a critical role in acquisition scenarios. Clearly defining and tracking these metrics ensures that software providers adhere to contractual, quality, and compliance expectations.

#### **Recommended Best Practices**

1. **Define Metrics in Contracts**

   * Specify the exact inspection metrics to be furnished by software providers, including:
     + Preparation time for reviews and inspections.
     + Defect counts (categorized by severity and type).
     + Effort reporting (e.g., duration of review meetings, preparation effort).
2. **Defect Taxonomies**

   * Agree on a defect taxonomy to ensure consistency in defect classification:
     + If providers use custom defect taxonomies, require them to furnish definitions or data dictionaries.
     + Verify consistency in defect definitions across all subcontractors involved.
3. **Effort Reporting Consistency**

   * Ensure metrics tracking aligns across contributors (providers and subcontractors).
     + All contributors must use the same definitions for reporting effort (e.g., preparation time, inspection rate, total time spent in reviews).
4. **Compliance Monitoring**

   * Periodically audit provider adherence to contractual metrics requirements. Ensure all subcontractors meet the same standards to avoid inconsistencies in measurements and defect reporting.

---

### **Summary of Best Practices**

| **Best Practice Area** | **Key Recommendations** |
| --- | --- |
| Target Artifacts | Focus reviews on critical early lifecycle artifacts, such as requirements and test plans. |
| Inspection Process Integrity | Enforce adherence to planning, preparation, checklists, and artifact-specific protocols. |
| Data Collection Consistency | Maintain uniform units of measurement, investigate outliers, and periodically analyze trends. |
| Acquisition Metrics | Define metrics in contracts, agree on defect taxonomies, and ensure effort reporting consistency. |
| Process Improvement | Use metrics and lessons learned to update checklists, improve preparation, and optimize inspection efforts. |

---

### **Conclusion**

Effective implementation of SWE-087 requires rigorous adherence to best practices, systematic collection and analysis of inspection data, and consistent measurement approaches—particularly in acquisition contexts. By following this guidance, NASA teams can improve the impact of peer reviews and inspections, drive process improvement, and ensure compliance across projects.

## 3.4 Base Metrics

**Examples of Software Peer Review Base Metrics**

|  |  |  |
| --- | --- | --- |
| Category | Base Metric | Description |
| Size | Size planned | Lines of code or document pages that you planned to inspect |
| Size | Size Actual | Lines of code or documents pages that were inspected or peer-reviewed |
| Time | Time Meeting | The time required to complete the inspection, if done over several meetings then add up the total time required |
| Effort | Planning | Total number of hours spent planning and preparing for the review |
|  | Meeting time | Total number of hours spent in the inspection meeting (multiply the Time meeting by the number of participates |
|  | Rework | The total number of hours spent by the author making improvements based on the findings. |
| Defects | Major Defects found | Number of Major defects found during the review |
|  | Minor Defect found | Number of Minor defects found during the review |
|  | Major Defects Corrected | Number of major defects corrected during rework |
|  | Minor Defects Corrected | Number of minor defects corrected during rework |
| Other | Number of Inspectors | Number of people, not counting observers, who participated in the review |
|  | Product Appraisal | Review teams assessment of the work product (accepted, accepted conditionally, review again following rework, review not complete, etc.) |
| Derived Data | Peer Review Defects | The Peer Review Defect metric measures the average number of defects per peer review to determine defect density over time.  Number of defects found per Peer Review = [Total number of defects] / [To number of Peer Reviews] |

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures),        * [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Peer Review](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Peer+Review) |

# 4. Small Projects

Small projects often face constraints in terms of **time**, **resources**, and **personnel**, yet software peer reviews and inspections remain critical to ensuring mission success, reducing risk, and preventing costly defects. Tailoring SWE-087 for small projects involves simplifying processes while retaining the effectiveness of peer reviews. Below is specific guidance to help small projects implement peer reviews and inspections efficiently and effectively.

---

### **1. Tailoring the Peer Review and Inspection Process**

#### **Objective: Simplify the process without sacrificing quality or compliance.**

Small projects can adapt the formal peer review and inspection process to fit their size, resource limitations, and complexity. Tailoring recommendations include:

1. **Streamline the Process:**

   * Combine certain activities (e.g., preparation and pre-review discussions) to optimize limited time and personnel.
   * Focus on **critical work products**, such as those related to **mission-critical functionality**, safety, or high-risk areas.
2. **Scale Down Participation:**

   * Aim for **smaller review teams** (e.g., 3–5 people), ensuring at least **one software assurance representative** or independent reviewer is included.
   * Cross-train team members to play multiple roles (e.g., one person serving as both recorder and reviewer).
3. **Simplify Entrance and Exit Criteria:**

   * Use lightweight readiness checklists to confirm:
     + Artifacts are stable enough for review.
     + Participants are prepared with limited time spent on pre-review activities.
   * Simplify exit criteria to focus on key outputs, such as tracking identified defects and capturing high-priority metrics.
4. **Leverage Existing Tools:**

   * Use free or low-cost tools (e.g., GitHub Issues, JIRA, Microsoft Excel) to manage defect tracking, actions, and metrics.

---

### **2. Focus on High-Impact Artifacts**

#### **Objective: Dedicate peer reviews to the most critical artifacts to optimize resource utilization.**

For small projects, it’s essential to prioritize peer reviews for work products that are likely sources of defects with significant downstream impacts.

1. **Prioritized Artifacts:**

   * **Requirements Documentation:** Ensure clarity, completeness, traceability, and eliminate ambiguity early.
   * **Design Artifacts:** Focus on high-complexity designs (e.g., algorithms, interfaces, safety-critical modules).
   * **Code Reviews:** Conduct targeted reviews of high-risk or mission-critical code elements.
   * **Test Plans/Procedures:** Review test documentation for scope, completeness, and test case alignment with requirements.
2. **Avoid Over-Inspection:**

   * Skip reviews for low-complexity artifacts or stable components that have a proven track record of quality unless they involve high-risk systems.

---

### **3. Use Lightweight Checklists**

#### **Objective: Maintain focus and consistency in defect identification while minimizing effort.**

Checklists provide a structured framework for defect discovery, even in a resource-constrained environment.

1. **Develop Focused Checklists:**

   * Keep checklists concise, containing only essential questions tailored to artifact type and project-specific risks.
   * Example: For code reviews, include prompts for error-prone areas like boundary conditions, algorithm correctness, and compliance with coding standards.
2. **Borrow from Existing Resources:**

   * Use templates and examples for inspection checklists available on NASA’s **SPAN** (or similar repositories).
3. **Update Over Time:**

   * Refine checklists as the team discovers recurring defects or areas needing further inspection during past reviews.

---

### **4. Metrics for Small Projects**

#### **Objective: Collect only essential metrics that directly inform project progress and quality.**

Small projects can focus on collecting a minimal set of key metrics to monitor the efficiency and effectiveness of peer reviews without overburdening the team.

1. **Recommended Minimal Metrics:**

   * **Defect Metrics:**
     + Number of defects found, classified by severity (critical, major, minor).
     + Number of open vs. closed defects over time.
   * **Process Metrics:**
     + Time spent on preparation and reviews (aggregated for all reviewers).
     + Number of participants vs. number required.
     + Number of artifacts reviewed vs. planned.
2. **Use Metrics to Optimize Resources:**

   * Track trends (e.g., high defect density in specific areas of code) and adjust inspection focus accordingly.
   * Share metrics with the team during regular project reviews to drive process improvement.

---

### **5. Best Practices for Small Projects**

1. **Set Realistic Schedules:**

   * Schedule reviews early and integrate them into existing milestones to minimize rework in later phases.
   * Use time-boxed inspections (e.g., no longer than 2 hours per session) to encourage efficiency.
2. **Consider Peer Substitution or External Reviewers:**

   * For very small teams, consider bringing in reviewers from other teams or depend on **external expertise** to leverage diverse perspectives and eliminate bias.
3. **Focus on Collaboration:**

   * Promote a team culture of constructive feedback to ensure reports of defects are detailed without causing unnecessary interpersonal friction.
   * Use informal pair programming or walkthroughs as lighter alternatives for early defect detection when schedules are tight.
4. **Automate Routine Checks Where Possible:**

   * Use automated tools (e.g., static code analyzers) to augment manual inspections and identify violations of coding standards or other low-level issues.
   * Focus manual reviews on high-risk areas that tools cannot address, such as logic errors, design flaws, or ambiguous requirements.
5. **Leverage Lessons Learned:**

   * Keep a "lessons learned" log for future process improvement. This can help streamline checklists, focus efforts, and identify which review practices generate the most benefit.

---

### **6. Leveraging Software Assurance for Small Projects**

#### **Objective: Ensure proper implementation of peer reviews without additional overhead.**

Software assurance (SA) personnel can enhance small project success by tailoring their involvement appropriately:

1. **Role Adjustment for SA Personnel:**

   * Serve as **review moderator** or independent observer to ensure adherence to process steps and entrance/exit criteria.
   * Verify that identified defects are properly tracked and resolved.
2. **Audit and Compliance Support:**

   * Conduct lightweight audits to confirm compliance with review processes, emphasizing critical metrics and areas of risk without excessive documentation overhead.
3. **Guidance on Tools and Templates:**

   * Assist small teams by providing ready-to-use checklist templates, metrics dashboards, or defect tracking workflows.

---

### **7. Common Pitfalls and Strategies**

#### **Pitfalls to Avoid:**

* **Skipping Preparation:** Rushed inspections without preparation limit defect discovery. Ensure the review package reaches participants in advance.
* **Overloading Inspectors:** Assigning the same personnel across many inspections can result in fatigue. Balance responsibilities or limit scope.
* **Focusing Only on Surface-Level Issues:** Without tailored checklists, participants may overlook deeper risks, especially in high-complexity artifacts.

#### **Mitigation Strategies:**

* Prioritize preparation by reserving time in the project schedule for artifact review.
* Use portion-based reviews (e.g., focus on one section of code/design at a time) to reduce fatigue.
* Encourage reviewers to address both low-level defects (e.g., coding issues) and high-level concerns (e.g., logic, design).

---

### **Summary for Small Projects**

#### **Tailored Approach:**

| **Aspect** | **Tailored Recommendation for Small Projects** |
| --- | --- |
| **Team Size** | 3–5 participants; cross-functional roles where possible. |
| **Artifacts Reviewed** | Requirements, mission-critical assets, and high-risk work products. |
| **Checklists** | Simple, lightweight, artifact-specific checklists. |
| **Review Timing** | Early reviews to prevent defects downstream. |
| **Metrics** | Focus on time, defect density, and open/closed defect trends. |
| **Tools** | Use free or low-cost tools for defect tracking and metrics collection. |
| **Support** | Leverage external reviewers or software assurance personnel for added expertise. |

By simplifying the inspection process, tailoring priorities, and maintaining focus on essential metrics and artifacts, small projects can meet the intent of SWE-087 effectively while managing limited resources. Continuous refinement of this approach ensures that reviews improve software quality and align with project goals.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-235)

  [An analysis of defect densities found during software inspections](https://ntrs.nasa.gov/search.jsp?R=19920010193 "Click to open in new window")

  John C. Kelly, Joseph S. Sherif, Jonathan Hops, NASA. Goddard Space Flight Center, Proceedings of the 15th Annual Software Engineering Workshop; 35 p
* (SWEREF-277)

  [Software Formal Inspections Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-87399 "Click to open in new window")

  NASA-STD-8739.9, NASA Office of Safety and Mission Assurance, 2013. Change Date:
  2016-10-07, Change Number: 1

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA has documented extensive lessons learned from its projects and missions to help improve software development processes, including peer reviews and inspections. These lessons highlight best practices, common pitfalls, and strategies to ensure the success of software peer reviews and inspections, in line with the intent of **SWE-087: Software Peer Reviews and Inspections**. Below are relevant lessons learned from NASA’s **Lessons Learned Information System (LLIS)** and other sources, tailored to the requirements of SWE-087.

---

### **1. Focus on Early Reviews of Requirements and Design**

#### **Lesson Learned:**

Issues in requirements and design are **exponentially more expensive to fix** when discovered late in the project lifecycle. Peer reviews and inspections are most effective when applied to **early lifecycle artifacts** such as requirements, architecture, and design documents.

#### **Example:**

* **Apollo Program Software Development:** Early review processes uncovered ambiguities and omissions in requirements, preventing costly redesigns during implementation and testing phases.

#### **Guidance:**

* Prioritize peer reviews for high-impact artifacts:
  + Requirements Specifications — Clarity, completeness, and consistency.
  + Design Documents — Alignment with requirements and feasibility of implementation.

---

### **2. Conduct Thorough Preparation**

#### **Lesson Learned:**

The lack of preparation by peer review participants has consistently resulted in **low-quality defect identification** and missed opportunities to uncover major issues. Participants must enter reviews fully prepared to provide meaningful feedback.

#### **Example:**

* **Mars Climate Orbiter (MCO):** Insufficient review preparation failed to catch a critical design issue related to metric/imperial unit conversions, leading to a mission failure.

#### **Guidance:**

* Share artifacts with reviewers well ahead of the sessions and provide **tailored checklists** to guide their preparation.
* Allocate dedicated time for reviewers to study materials, especially for complex or safety-critical systems.

---

### **3. Ensure Diverse Team Members in Inspections**

#### **Lesson Learned:**

Inspection teams composed of individuals with **diverse roles and expertise** uncover more defects and prevent groupthink. A lack of diverse perspectives can result in recurring blind spots and incomplete coverage of defect-prone areas.

#### **Example:**

* **Mars Polar Lander:** Failure to include test engineers in earlier design reviews resulted in a missed opportunity to catch a critical fault in the software’s handling of sensor input, contributing to mission loss.

#### **Guidance:**

* Include cross-functional team members in peer reviews:
  + Software development team members.
  + Experts from systems engineering, testing, operations, and software assurance.
* Ensure no key roles (e.g., independent moderator) are omitted.

---

### **4. Use Checklists to Standardize Review Focus**

#### **Lesson Learned:**

Peer reviews without structured checklists often fail to detect critical defects consistently. Using **standardized checklists** tailored to artifact types ensures coverage of common defect categories and conformance to standards.

#### **Example:**

* **International Space Station (ISS) Software:** Successful implementation of tailored code review checklists helped catch recurring issues related to memory use, thread synchronization, and coding standard violations.

#### **Guidance:**

* Develop artifact-specific checklists (e.g., requirements, design, code, test plans).
* Regularly update checklists based on lessons learned and past defect trends.

---

### **5. Establish and Enforce Entrance and Exit Criteria**

#### **Lesson Learned:**

Reviews conducted without established and enforced **entrance/exit criteria** often result in unprepared participants and incomplete inspections. Rigorous criteria ensure that work products are ready for review and that defects are logged and addressed systematically.

#### **Example:**

* **Space Shuttle Program:** Reviews that lacked entrance criteria for design diagrams led to incomplete analysis, forcing re-reviews and delaying downstream tasks.

#### **Guidance:**

* Establish entrance criteria to ensure the readiness of artifacts (e.g., complete, up-to-date, and approved versions).
* Define and apply exit criteria to ensure all action items are logged, resolved, and verified.

---

### **6. Monitor Metrics for Continuous Improvement**

#### **Lesson Learned:**

Without **metrics tracking and trend analysis**, projects fail to evaluate the effectiveness of peer reviews and inspections. This leads to inefficiencies, recurrence of the same defects, and lack of process improvement over time.

#### **Example:**

* **Hubble Space Telescope (HST):** Early projects that closely tracked peer review trends identified recurring defects and optimized checklists and preparation time, significantly improving defect detection rates.

#### **Guidance:**

* Track and analyze key peer review metrics, such as:
  + Number of defects found (by type and severity).
  + Preparation and review effort (hours per artifact).
  + Defect resolution trends (time to close/open defect ratios).
* Use metrics to refine processes, target training needs, and provide feedback to participants.

---

### **7. Avoid Skipping the Planning and Follow-Up Stages**

#### **Lesson Learned:**

Teams that skip planning or neglect defect follow-up often render the review process ineffective. Planning ensures that the peer review scope and personnel are adequate, while follow-up ensures that identified defects are resolved.

#### **Example:**

* **James Webb Space Telescope (JWST):** Initial omission of detailed planning and follow-ups in some reviews led to a backlog of unresolved defects. A revised defect tracking strategy resolved many of these inefficiencies, enabling better adherence to schedule milestones.

#### **Guidance:**

* Plan all peer reviews in collaboration with project leads, ensuring alignment on artifacts, participants, timing, and expectations.
* Implement a centralized defect tracking process to monitor all reported issues until closure.

---

### **8. Avoid Overloading the Review Team**

#### **Lesson Learned:**

Overloading review teams with excessive artifacts or review responsibilities results in **review fatigue** and decreases defect detection rates. Reviews conducted in shorter, focused sessions are more effective.

#### **Example:**

* **Software-intensive projects at JPL:** Large artifacts reviewed in a single pass led to oversight of major issues. Dividing artifacts into manageable portions improved focus and defect identification.

#### **Guidance:**

* Limit peer review sessions to **2–3 hours** to maintain participant engagement and focus.
* Break complex artifacts into smaller sections, conducting multiple sessions if necessary.

---

### **9. Ensure Inspections are Integrated with V&V**

#### **Lesson Learned:**

Peer reviews and inspections that are poorly integrated with other **Verification and Validation (V&V)** activities often lead to overlap or gaps in defect detection, especially for safety-critical software.

#### **Example:**

* **NASA Robotic Missions:** Some projects experienced significant rework because integration of inspections with testing activities was insufficient, causing duplication of effort and oversight of risks.

#### **Guidance:**

* Coordinate peer review schedules with other V&V tasks, such as unit testing or static code analysis, to ensure complementary defect coverage.
* Avoid redundancy by using inspection data to inform later V&V steps.

---

### **10. Train Teams on the Inspection Process**

#### **Lesson Learned:**

Teams that lack training on peer review processes often fail to follow established procedures (e.g., preparation, using checklists) and misclassify or overlook critical defects. Training ensures that all participants understand their roles and responsibilities.

#### **Example:**

* **Constellation Program:** Defects were missed due to incomplete reviewer preparation and lack of focused training. Later incorporation of training modules on effective peer reviews mitigated such problems.

#### **Guidance:**

* Provide role-based training to reviewers, moderators, and recorders on the inspection process.
* Include examples of past defects and how to identify them effectively.

---

### **11.** **LL‑SW‑01 — Standards for Heritage Software Reuse and Testing**

* **Source LL ID(s):** IVV‑01
* **Discipline(s):** Software Assurance, IV&V
* **Context/Background:** Program teams planned to reuse “legacy” flight software; significant defects emerged late, revealing the misconception that heritage code needs minimal testing.
* **Lesson Learned:** Treat heritage software **as if new**—perform full requirements validation, interface verification, regression testing, and environmental qualification for the new mission context.
* **Evidence/Observation:** PPE planned legacy reuse; issues were still open at the pause; reuse assumptions delayed defect discovery and correction.
* **Cause(s):** Belief that prior flight history obviates testing; lack of program‑level reuse standards.
* **Recommendation/Corrective Action:** Establish **project‑level reuse standards** specifying test scope (regression, interface, environment), verification criteria, and acceptance gates for heritage software.
* **Implementation Guidance:** Embed reuse criteria in plans (SWE‑013), trace reused functionality to requirements/design/tests (SWE‑052/059/064/072), and determine safety classification impacts (SWE‑133/134).
* **Success Criteria/Verification:** Documented reuse plan; executed test campaigns; evidence of bidirectional traceability and IV&V closure; defect rates comparable to new development baselines.
* **Applicability/Scope:** All mission/safety‑critical software; heritage and third‑party components.
* **Related Standards/Requirements:** **SWE‑027 (COTS/legacy use), SWE‑013 (Plans), SWE‑050 (Requirements), SWE‑052/059/064/072 (Traceability), SWE‑133/134 (Safety)**.

**LL‑SW‑06 — Provide Design Artifacts Early and In‑Phase with Development**

* **Source LL ID(s):** IVV‑02
* **Discipline(s):** Software Assurance, IV&V, Software Design
* **Context/Background:** Early design visibility enables cheaper, timely feedback; late delivery limits IV&V value.
* **Lesson Learned:** Share evolving designs **before coding**; IV&V supports iterative updates and identifies issues when change costs are lowest.
* **Evidence/Observation:** Difficulties obtaining early design artifacts on HALO/PPE reduced synchronization and defect prevention.
* **Cause(s):** Perception that IV&V slows design.
* **Recommendation/Corrective Action:** Include design artifact delivery milestones in IV&V PEP; allow early access to drafts.
* **Implementation Guidance:** **SWE‑013** (planning), **SWE‑018** (reviews), **SWE‑131/141** (IV&V).
* **Success Criteria/Verification:** Reduced design‑phase rework; fewer late defects; on‑time IV&V reviews.
* **Applicability/Scope:** All mission/safety‑critical designs.
* **Related Standards/Requirements:** **SWE‑013, SWE‑018, SWE‑131, SWE‑141**.
* **References:** Gateway S&MA LL deck.

**LL‑SW‑08 — Include Subcontractor Documentation in Deliveries**

* **Source LL ID(s):** IVV‑08
* **Discipline(s):** Software Assurance, IV&V, Acquisition
* **Context/Background:** Prime docs lacked detail for subcontractor‑developed functionality; IV&V couldn’t assess low‑level designs.
* **Lesson Learned:** Require subcontractor **low‑level design/documentation** availability to IV&V (as legally permissible).
* **Evidence/Observation:** More complete documentation reduced false positives and improved issue identification.
* **Cause(s):** Undefined contractual expectations for lower‑tier artifacts.
* **Recommendation/Corrective Action:** Include flow‑downs mandating artifact delivery/access rights; define content/format.
* **Implementation Guidance:** Plans (**SWE‑013**), requirements (**SWE‑050**), and IV&V (**SWE‑131/141**) should specify subcontractor documentation scope.
* **Success Criteria/Verification:** IV&V can compile/build/analyze with full design context; decreased unactionable findings.
* **Applicability/Scope:** Multi‑tier development efforts.
* **Related Standards/Requirements:** **SWE‑013, SWE‑050, SWE‑131, SWE‑141**.

**LL‑SW‑17 — Tool and Database Usability Drives Process Quality**

* **Source LL ID(s):** CP‑Hazard/SharePoint/ARM usability LLs (GW‑SMA‑LL‑019/026/036/048‑054/084)
* **Discipline(s):** Software Tools/Process, Assurance Data Mgmt
* **Context/Background:** Tools lacked features/automation; partitions caused visibility leaks; usability issues degraded reviews and traceability.
* **Lesson Learned:** Select/configure tools based on **process needs**; mandate usability, automation, partitioning, and reporting capabilities.
* **Evidence/Observation:** Commenting, partitioning, PDF generation, and access governance weaknesses added workload and risk.
* **Cause(s):** Sustainment‑only funding; late tool development; ad‑hoc admin.
* **Recommendation/Corrective Action:** Conduct **analysis of alternatives**; fund capability expansion; embed operational architects; standardize partitions and role models.
* **Implementation Guidance:** Capture in **SWE‑013** (plans) and **SWE‑091** (measurement repositories) with defined KPIs for tool performance.
* **Success Criteria/Verification:** Reduced manual auditing; reliable exports; secure access; KPI improvements (latency, completeness).
* **Applicability/Scope:** All assurance tools, requirements DBs, risk systems.
* **Related Standards/Requirements:** **SWE‑013, SWE‑091**.

### **Conclusion**

NASA’s **SWE-087** requires systematic peer reviews and inspections to enhance software quality, reduce risk, and ensure defect discovery at the earliest possible stage. Lessons learned from past projects emphasize the importance of **planning, training, metrics monitoring, preparation**, and **process compliance** to maximize inspection effectiveness. By applying these practices, small and large projects alike can improve quality assurance outcomes and align with mission-critical objectives.

### 6.2 Other Lessons Learned

* Throughout hundreds of inspections and analyses of their results, the Jet Propulsion Laboratory (JPL) has identified key lessons learned that lead to more effective inspections[235](#_tabs-<p></p>), including:
  + Capturing statistics on the number of defects, the types of defects, and the time expended by engineers on the inspections.

# 7. Software Assurance

**SWE-089 - Software Peer Reviews and Inspections - Basic Measurements**

5.3.4 The project manager shall, for each planned software peer review or software inspection, record necessary measurements.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project records the software peer reviews and results of software inspection measurements.

## 7.2 Software Assurance Products

Software assurance (SA) plays an essential role in ensuring that SWE-087 is implemented effectively by verifying process compliance, monitoring peer review outcomes, and tracking metrics to continuously improve the software quality assurance process. The following enhanced guidance emphasizes actionable steps, strengthens alignment with project goals, and provides strategies for collecting, analyzing, and demonstrating the value of software assurance contributions.

#### **Objective: Deliver tangible, actionable outputs to maintain compliance and drive improvement.**

Software assurance must provide documented evidence demonstrating its involvement in and oversight of peer reviews. Suggested products include:

1. **Peer Review Metrics, Reports, Data, and Findings**:

   * Compile peer review metrics for all reviews conducted, including defect counts, participant data, and actionable findings.
   * Highlight recurring issues or trends related to compliance or artifact quality.
2. **List of Participants in Software Peer Reviews**:

   * Document participants (name, role, and functional area) to verify that diverse expertise has been included and confirm proper team composition.
3. **Defect or Problem Reporting Tracking Data**:

   * Maintain a defect log showing issues identified, severity classifications, tracking information, and closure histories.
   * Prioritize tracking defects found by SA personnel in peer reviews.
4. **Software Assurance Audit Reports**:

   * Audit reports verifying:
     + Compliance with NPR 7150.2 requirements during peer review processes.
     + Completion of entrance and exit criteria, adherence to checklists, and artifact readiness.
   * Identify process gaps or non-conformances and recommend corrective actions.
5. **Closure Reports for Non-Conformances**:

   * Provide evidence of resolution for all peer review findings, detailing actions taken and the timeframe for defect closure.

## 7.3 Metrics: Strengthened Software Assurance Metrics

#### **Objective: Focus on actionable insights that demonstrate the effectiveness, efficiency, and value of peer reviews and software assurance involvement.**

Software assurance should play a critical role in tracking and analyzing peer review metrics. Enhanced metrics to track include:

1. **Non-Conformances Metrics:**

   * Number of non-conformances identified:
     + **By artifact type.**
     + **By participant role (developer, software assurance, independent reviewers).**
   * Trends showing non-conformances over lifecycle phases (e.g., requirements vs. design inspections).
   * Analysis of open/closed findings and average time to closure.
2. **Peer Review Metrics:**

   * Preparation time per reviewer and audit participants.
   * Time spent by reviewers and SA personnel in review meetings vs. total planned.
   * Time required to close audit-related findings and peer review non-conformances.
3. **Participant Metrics:**

   * Number of peer review participants vs. total invited (e.g., missed contributions due to absent reviewers).
   * Number of SA members participating in peer review activities (planning, preparation, review).
4. **Software Assurance-Specific Metrics:**

   * Number and percentage of defects or issues identified by SA personnel:
     + Include severity breakdowns of findings (e.g., critical, major, minor defects).
   * Total time spent by software assurance on activities:
     + Preparation before the review meeting.
     + Monitoring the meeting itself.
     + Post-review follow-up and tracking defect closure.
5. **Peer Review Effectiveness Metrics:**

   * Number of reviews conducted vs. planned.
   * Artifact defect density trends (defects per artifact reviewed).
   * The rate of inspection coverage (e.g., number of defects found per preparation time).

## 7.4 Software Assurance Guidance

#### **Objective: Provide actionable recommendations for SA personnel to integrate effectively into the peer review process, ensuring quality while improving efficiency.**

1. **Verification of Metrics Collection Process:**

   * Confirm that all peer review metrics (as defined by the organization or center) are collected, recorded, and stored systematically.
   * Verify adherence to standard practices for recording peer review data, including formats, definitions, and units of measurement (e.g., person-hours for effort).
2. **Focus on Critical Artifacts:**

   * Ensure that peer reviews emphasize critical or high-risk work products, such as:
     + Requirements specifications.
     + Architecture and design artifacts.
     + Mission-critical code modules.
     + Test plans and procedures.
   * Monitor artifact prioritization to prevent wasted resources on non-essential reviews.
3. **Software Assurance Involvement Metrics:** Collect specific data regarding software assurance participation in peer reviews to improve project estimates and demonstrate SA value:

   * Hours spent by SA personnel in:
     + Ensuring planning and preparation were performed correctly.
     + Reviewing artifacts before the peer review meeting.
     + Attending peer review meetings.
     + Following up on findings until closure.
   * Defects or issues:
     + Number of issues found by software assurance.
     + Severity breakdown of SA findings.
     + Comparison of SA findings vs. those found by other reviewers (demonstrating SA’s contribution to review quality).
4. **Process Compliance Monitoring:**

   * Ensure peer reviews meet process compliance criteria:
     + Artifact readiness confirmed (entrance criteria met).
     + Proper use of tailored checklists aligned with artifact type and project needs.
     + Exit criteria applied (defect tracking initiated, necessary actions logged for closure).
5. **Improvement of Peer Review Processes:**

   * Record observations from SA personnel about the peer review process:
     + Are entrance and exit criteria consistently applied?
     + Are critical steps skipped (e.g., preparation)?
     + Are participants sufficiently trained in their review roles?
   * Provide recommendations for improving peer review effectiveness based on SA findings.
6. **Demonstrating Software Assurance Value:**

   * Compile data on SA findings and participation to demonstrate their impact on peer review outcomes:
     + Compare SA defect identification rates with overall review-defect finding.
     + Report mission-critical defects found exclusively by SA personnel.
     + Highlight corrective actions initiated by SA oversight (e.g., resolution of recurring issues through process improvement).

### **Additional Recommendations**

1. **Center-Specific Guidance and Tailoring:**

   * Use metrics outlined in the center’s process asset library (PAL) if available. Verify compliance with center-specific requirements for peer reviews and tracking.
   * Tailor SA involvement and metrics collection to the size and complexity of the project to balance resource constraints and effectiveness.
2. **Integration of Peer Review Metrics into Project Oversight:**

   * Leverage peer review reports and findings in **project risk assessments** (e.g., defect trends indicating systemic risks in artifact generation).
   * Use defect closure metrics to evaluate project schedule risks for unresolved issues.
3. **Facilitate Lessons Learned Collection:**

   * Encourage SA personnel to document lessons learned from peer reviews, focusing on:
     + Identified gaps in the peer review process.
     + Opportunities to improve planning and review defect tracking.
     + Artifact-specific defect patterns that should inform checklist updates.

### **Conclusion**

By applying enhanced software assurance guidance, metrics tracking, and oversight activities, SA personnel can ensure that SWE-087 peer reviews are conducted systematically and effectively. This refined approach not only strengthens process compliance and defect identification but also demonstrates the value of software assurance through measurable contributions to project quality and mission-critical success.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures),        * [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is necessary to demonstrate compliance with the requirements of SWE-087. It serves to verify that peer reviews and inspections are performed systematically, meet the requirements of NPR 7150.2, and contribute to overall software quality improvements. Below is a detailed list of potential objective evidence that supports the execution of SWE-087.

---

### **1. Peer Review Planning Documentation**

**Purpose:** To demonstrate that peer reviews were planned systematically and aligned with project needs and requirements.

**Objective Evidence Examples:**

* Peer review plan(s) outlining:
  + Artifacts to be reviewed (e.g., requirements, design, code, test plans).
  + Review schedules and milestones.
  + Review goals and objectives (e.g., identifying defects, ensuring artifact quality).
* Review meeting agenda(s) showing planned duration, scope, and discussion points.
* Role assignments for participants, including reviewer, moderator, recorder, and software assurance roles.
* Entrance and exit criteria for each planned peer review.
* List of tailored checklists for the selected artifact types.

---

### **2. Peer Review Artifacts**

**Purpose:** To confirm that the required artifacts were identified, prepared, and made available during peer reviews.

**Objective Evidence Examples:**

* Reviewed artifacts:
  + Requirements specifications (e.g., in a final or draft state).
  + Design documents, architecture diagrams, or APIs.
  + Source code modules or scripts.
  + Test plans, test cases, and procedures.
  + User manuals or operational documentation.
* Record of artifact readiness checks for compliance with entrance criteria.
* Evidence of artifact updates or rework post-review to meet peer review findings.

---

### **3. Peer Review Participation Records**

**Purpose:** To verify that peer reviews were conducted with the participation of qualified reviewers and include diverse perspectives.

**Objective Evidence Examples:**

* Attendance records of review meetings, including:
  + List of participants (names, roles, and expertise areas, e.g., requirements engineer, developer, tester, software assurance).
  + A record of participants who were responsible for preparation and whether they completed their assignments.
* Invitations or scheduling evidence distributed to team members.
* Evidence of participant cross-discipline reviews (ensuring different areas of expertise contributed).

---

### **4. Peer Review Execution Documentation**

**Purpose:** To provide evidence that peer reviews were conducted with adherence to the defined process.

**Objective Evidence Examples:**

* Completed moderator reports, documenting:
  + Actions taken during the review meeting.
  + Summaries of discussions, findings, and resolutions.
* Meeting minutes or session transcripts that document:
  + Key discussion points.
  + Critical defects or issues raised.
  + Responses or decisions made during the review.
* Defect logs with details of defects or issues identified:
  + Defect severity and classification (e.g., critical, major, minor).
  + Defect description and location (e.g., line of code, section of requirements).
  + Reviewer(s) who identified each defect.

---

### **5. Peer Review Metrics**

**Purpose:** To demonstrate that measurement data were collected for process evaluation and improvement.

**Objective Evidence Examples:**

* Metrics reports showing:
  + Total number of peer reviews conducted vs. planned.
  + Number of defects found, categorized by type and severity.
  + Trends in defect density (e.g., defects per artifact or defects per lifecycle phase).
  + Time spent on peer reviews:
    - Preparation time (participants and software assurance personnel).
    - Time spent in peer review meetings.
* Participant preparation effort data:
  + Time spent by each reviewer reading and reviewing the artifact.
* Open vs. closed defect tracking over time.
* Number of defects discovered by software assurance (compared to other reviewers).

---

### **6. Defect or Non-Conformance Tracking**

**Purpose:** To show documented evidence of defects identified during the peer review process and their subsequent tracking and resolution.

**Objective Evidence Examples:**

* Recorded defect or non-conformance reports, including:
  + Issue description.
  + Source artifact or work product where the defect was found.
  + Assignee(s) for defect resolution.
  + Current status of the defect (open, closed, in-progress).
  + Time to resolve the defect.
* Evidence of defect closure and verification steps:
  + Re-review reports showing corrective actions taken.
  + Updated artifacts showing resolution of identified defects.
* Defect aggregation reports to track trends.

---

### **7. Peer Review Checklists**

**Purpose:** To validate that peer review processes used structured, artifact-specific checklists aligned with project needs and standards.

**Objective Evidence Examples:**

* Completed and signed checklists documenting:
  + Review items verified during inspection (e.g., clarity, correctness, traceability, compliance to standards).
  + Sections of the artifact reviewed.
  + Defects found during checklist-driven evaluations.
* Evidence that checklist outcomes were integrated with defect tracking.

---

### **8. Peer Review Audit Records (Software Assurance Oversight)**

**Purpose:** To confirm that peer reviews were conducted in compliance with documented processes and standards (e.g., NPR 7150.2, NASA-STD-8739.9).

**Objective Evidence Examples:**

* Audit reports from software assurance personnel verifying:
  + Adequacy of planning, execution, and defect tracking processes.
  + Compliance with entrance and exit criteria.
  + Use of approved checklists during inspection.
* Non-conformance reports generated during software assurance audits of the peer review process.
* Software assurance defect tracking data showing:
  + Issues identified by SA personnel.
  + Resolution and verification of software assurance findings.

---

### **9. Process Improvement Reports**

**Purpose:** To show how data and findings from peer reviews were used for continuous process improvement.

**Objective Evidence Examples:**

* Lessons learned reports documenting:
  + Process inefficiencies noted during reviews.
  + Areas identified for improvement (e.g., better checklists, improved training for reviewers).
* Changes to peer review processes resulting from lessons learned:
  + Updated procedures or policies.
  + Revised participant training materials.
  + Improvements to pre-review planning.
* Historical trends illustrating:
  + Reduction in defect rates over lifecycle phases.
  + Improved efficiency of peer reviews (e.g., reduced time spent or faster defect closure).

---

### **10. Process Compliance and Tailoring Documentation**

**Purpose:** To confirm that the peer review process followed established standards or approved tailoring.

**Objective Evidence Examples:**

* Tailoring approval documenting deviations from standard peer review processes and justifications for those changes.
* Process compliance reports demonstrating alignment with SWE-087 and other relevant standards (e.g., NASA-STD-8739.9).
* Evidence of alignment with the project's software development plan (SDP) or software assurance plan (SAP).

---

### **11. Training and Preparation Records**

**Purpose:** To ensure that participants, including software assurance personnel, were adequately trained and prepared for peer reviews.

**Objective Evidence Examples:**

* Training records for participants on peer review processes, tools, and techniques.
* Evidence of participant preparation:
  + Documentation showing artifacts were distributed to participants ahead of time.
  + Preparation verification checklists completed by participants.

---

### **12. Summary Dashboards and Reports**

**Purpose:** To provide a high-level view of peer review performance, effectiveness, and compliance for project stakeholders.

**Objective Evidence Examples:**

* Dashboards summarizing peer review statistics (e.g., total defects, trends, preparation time).
* Status reports provided for management showing peer review progress and findings.

---

### **Conclusion**

Objective evidence for SWE-087 must demonstrate that software peer reviews and inspections align with NPR 7150.2, are executed systematically, and are enabling defect detection and resolution effectively. The collection and organization of artifacts, participant data, defect logs, and metrics ensure traceability and accountability while helping to validate compliance with NASA's software engineering and assurance requirements. Ensuring robust documentation also facilitates opportunities for continuous process improvement, aligning with NASA’s commitment to delivering high-quality software for mission-critical applications.

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
