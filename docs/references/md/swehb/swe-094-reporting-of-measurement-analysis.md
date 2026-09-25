# SWE-094 - Reporting of Measurement Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695481. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis

SWE-094 - Reporting of Measurement Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695481)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695481&showCommentArea=true&showComments=true#addcomment)

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

5.4.4 The project manager shall provide access to the software measurement data, measurement analyses, and software development status as requested to the sponsoring Mission Directorate, the NASA Chief Engineer, the Center Technical Authorities, HQ SMA, and other organizations as appropriate. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-094 History

SWE-094 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.4.5 The project shall report measurement analysis results periodically and allow access to measurement information by Center-defined organizational measurement programs. |
| Difference between A and B | Removes the requirement to report analysis results;  Changes the access requirement from "measurement information" to "software measurement data, measurement analyses, and software development status";  Specifies who can request. |
| B | 5.4.4 The project manager shall provide access to the software measurement data, measurement analyses and software development status as requested to the sponsoring Mission Directorate, the NASA Chief Engineer, Center and Headquarters SMA, and Center repositories. |
| Difference between B and C | Removed Center Repositories;  Removed Center SMA requirement but replaced it with Center Technical Authorities. |
| C | 5.4.4 The project manager shall provide access to the software measurement data, measurement analyses, and software development status as requested to the sponsoring Mission Directorate, the NASA Chief Engineer, the Center Technical Authorities, and Headquarters SMA. |
| Difference between C and D | Included other organizations in the list. |
| D | 5.4.4 The project manager shall provide access to the software measurement data, measurement analyses, and software development status as requested to the sponsoring Mission Directorate, the NASA Chief Engineer, the Center Technical Authorities, HQ SMA, and other organizations as appropriate. |

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

This requirement intends to provide access to the software metric data during the project life cycle for those Agency and Center-defined organizations responsible for assessing and utilizing the metric data. The software development project organizations can provide access to several organizations tasked to review or access the software development progress and quality. When a software effort is acquired from an industry partner, the contractor and/or subcontractors provide NASA with access to the software metric information on time to allow usage of the information.

NASA established software measurement programs to meet measurement objectives at multiple levels within the Agency. In particular, measurement programs are established at the project and also at the Center levels to satisfy organizational, project, program, and Directorate needs. Centers have measurement systems and record repositories that are used for records retention, and subsequent analysis and interpretation to identify overall levels of Center competence in software engineering, and to identify future opportunities for training and software process improvements.

**"The project manager shall provide access to the software measurement data, measurement analyses, and software development status as requested to the sponsoring Mission Directorate, the NASA Chief Engineer, the Center Technical Authorities, HQ SMA, and other organizations as appropriate."**

---

### **Ensuring Accountability and Transparency**

* Access to software measurement data, analyses, and development status ensures **transparency** and **accountability** in the execution of the project.
* The Mission Directorate, NASA Chief Engineer, Center Technical Authorities (TA), and other organizations involved in governance rely on this data to:
  + Evaluate compliance with NASA standards and mission objectives.
  + Assess technical progress and ensure alignment with design requirements, safety standards, and organizational goals.

---

### **Supporting Risk Management and Corrective Actions**

* Software measurements and analyses (such as defect data, progress metrics, and performance benchmarks) are critical for identifying and monitoring **risks** related to software development, integration, and verification.
* These metrics allow governing bodies, like HQ SMA (Safety and Mission Assurance), to detect early warning signs of issues such as schedule slippage, unaddressed defects, or gaps in compliance with safety and reliability standards.
* Providing timely access enables these organizations to take proactive **corrective actions** and mitigate risks before they impact mission success.

---

### **Enhancing Collaboration and Decision-Making**

* Access to software development status and analytics supports **collaboration** between stakeholders, decision-makers, and technical experts.
* This shared knowledge fosters more effective issue resolution and more informed decision-making, especially in critical areas like resource allocation, operational constraints, and the management of technical or safety risks.
* It ensures that concerns raised by all relevant entities (e.g., the Mission Directorate or NASA Chief Engineer) are recognized and addressed coherently across the project lifecycle.

---

### **Ensuring Compliance with System-Level Requirements and Standards**

* Software development is a key component of NASA systems, and its quality directly impacts the safety, functionality, and reliability of the overarching system.
* By allowing governing bodies access to software measurement data and analyses, the project manager ensures that software aligns with system-level requirements, standards, and mission directives.
* This also enables **independent verification and validation (IV&V)** by technical authorities and other organizational units.

---

### **Facilitating Mission Assurance Reviews and Audits**

* Organizations like HQ SMA and Center Technical Authorities often conduct **reviews and audits** to ensure compliance with safety-critical requirements, technical standards, and programmatic constraints.
* Access to software measurement data and analyses enables these reviews to be **comprehensive** and **data-driven**, allowing for more accurate assessments of program health and progress.

---

### **Allowing for Organizational Oversight and Funding Justification**

* The sponsoring Mission Directorate and leadership bodies such as the NASA Chief Engineer require visibility into software progress to:
  + Track resource usage.
  + Justify program funding.
  + Ensure that deliverables are produced on time, within budget, and meet safety and quality expectations.
* Without access to development metrics, organizational oversight would be limited, increasing the risk of undetected issues that could jeopardize the success of the mission.

---

### **Conclusion**

Providing access to software measurement data, analyses, and development statuses ensures transparency, fosters collaboration, and supports effective governance across the project. By enabling detailed oversight and risk management, this requirement directly contributes to the safety, reliability, and success of NASA’s missions.

# 3. Guidance

Metrics play a vital role in software engineering by providing insights into the effectiveness, efficiency, and quality of software development activities across NASA projects. The following sections clarify how metrics inform project management and process improvement, their practical uses, and the roles responsible for managing and utilizing metrics data to meet organizational goals.

## 3.1 What Do Metrics Tell Us?

Metrics are key measurements that enable project managers, technical leads, and stakeholders to evaluate how effectively software development activities are being conducted across multiple development organizations and projects. Specifically, metrics provide the following benefits:

* **Performance Evaluation**:  
  Metrics quantify how well software development efforts align with planned objectives, enabling the evaluation of team and organizational performance.
* **Trend Analysis and Forecasting**:  
  By monitoring trends over time, metrics offer predictive insights, helping teams forecast future development progress and assess the likelihood of meeting milestones and deadlines.
* **Early Issue Detection**:  
  Metrics highlight deviations from planned performance or quality standards, enabling early detection of potential risks or issues in the development process. For example, metrics can reveal declining defect resolution rates, signaling potential trouble in meeting project quality goals.
* **Process Improvement and Adjustment**:  
  Adjustments to development processes can be evaluated quantitatively by observing the impact on relevant metrics. This data-driven approach ensures that process changes lead to measurable improvements.
* **Organizational Oversight and Capability Assessment**:  
  The collection and analysis of organization-wide (Center-wide) measurement data help senior leadership evaluate the overall maturity and capability of software practices, enabling better planning for process improvements and the identification of training opportunities to advance software engineering competencies.

For additional guidance on implementing measurement requirements, analyzing data, and interpreting results, refer to **Topic 7.14 - Implementing Measurement Requirements and Analysis for Projects.**

## 3.2 Uses of Metrics

Metrics provide valuable data to help manage projects, assure safety and quality, and enhance software processes. The overarching goals for both project-level and Center-level metrics programs include:

1. **Improving Future Planning and Cost Estimation**:

   * Metrics offer historical data that can be used to create realistic cost estimates, resource allocations, and schedules for future projects.
2. **Tracking Progress Realistically**:

   * Data-driven insights from metrics enable stakeholders to monitor actual progress against planned milestones and make informed adjustments to keep development on track.
3. **Evaluating and Improving Software Quality**:

   * Metrics such as defect density, mean time to failure, or test coverage provide indicators of software quality, enabling teams to prioritize quality improvements.
4. **Driving Process Improvement**:

   * Baseline metrics form the foundation for identifying opportunities to streamline processes, resolve inefficiencies, and enhance engineering capabilities.

#### **Related Requirements**

The following requirements outline the broader context of software measurement and reporting:

* **SWE-090 - Management and Technical Measurements**: Defines the types of management and technical metrics required for effective oversight.
* **SWE-091 - Establish and Maintain a Measurement Repository**: Specifies the need to centrally store measurement data, ensuring availability and traceability.
* **SWE-092 - Using Measurement Data**: Addresses the use of metrics for decision-making, compliance verification, and analyzing project performance.
* **SWE-093 - Analysis of Measurement Data**: Focuses on applying analytical methods to extract meaningful insights from measurement data.

These requirements support **SWE-094 - Reporting of Measurement Analysis**, which emphasizes timely and accurate communication of measurement results to appropriate stakeholders. This data is recorded in the Center repository and documented in the Software Metrics Report (see **5.05 - Metrics - Software Metrics Report**).

## 3.3 Users of Metrics Data

The responsibility for **collecting, analyzing, and sharing metrics data** falls on the project team. It is critical that measurement results are delivered properly, communicated on time, and made available to the appropriate stakeholders. Key users of metrics data include:

* **Sponsoring Mission Directorate**:  
  Mission leadership requires regular access to metrics to evaluate project progress, analyze budgetary conformity, and ensure the project meets mission goals and constraints.
* **NASA Chief Engineer**:  
  Metrics support the Chief Engineer's oversight of technical standards, risk management, and the engineering excellence of software development activities.
* **Center Technical Authorities (TAs)**:  
  Metrics allow TAs to oversee compliance with Center and Agency engineering requirements, ensuring software meets required safety, reliability, and quality standards.
* **HQ SMA (Safety and Mission Assurance)**:  
  Metrics help SMA personnel evaluate the safety and assurance aspects of the project, enabling oversight of risk mitigation efforts and compliance with critical safety standards.
* **Center Repository Managers**:  
  Metrics collected for project-level activities often feed into Center-wide repositories for broader analysis and benchmarking. Repository managers require regular updates to ensure data consistency and completeness.

#### **Ensuring Accessibility**

The project is required to:

* Collect and report metrics data **periodically** based on established collection, reporting, and storage procedures (see **SWE-090 - Management and Technical Measurements**).
* Make measurement data and analysis results available **on demand** to authorized recipients, including the Mission Directorate, NASA Chief Engineer, HQ SMA, and Center repositories.

This practice ensures timely access to critical information for oversight, decision-making, and process improvement, fostering accountability and transparency.

Metrics are a cornerstone of effective software engineering governance, providing essential insights into development performance, product quality, and process maturity. By leveraging metrics for progress tracking, issue detection, and process improvement, NASA ensures that software development activities align with mission objectives, safety standards, and engineering excellence. Proper sharing and management of metrics data enable collaboration among key stakeholders while supporting broader organizational goals. For successful implementation, projects must prioritize the accurate collection, rigorous analysis, and timely dissemination of metrics data.

See also Topic [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects).

Other requirements ([SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements), [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository), [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data), and [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)) provide the software measurement data and the analysis methods that are used to produce the results being accessed by this SWE-094 - Reporting of Measurement Analysis. The information is stored in the center repository ([SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository)) and recorded in a Software Metrics Report (see [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report)).

Software measurement data which includes software development status (see [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements)) and measurement analyses (see [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)) should be accessible to sponsoring Mission Directorate, NASA Chief Engineer, Center, and Headquarters SMA, and able to be captured in Center repositories.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics) |

# 4. Small Projects

For smaller projects, resource limitations and simpler organizational structures require a streamlined approach to meet this requirement effectively. The following guidance is tailored to meet the needs of smaller projects while maintaining compliance, efficiency, and alignment with NASA processes:

---

### 1. **Simplify Metrics Selection**

* **Focus on Key Metrics**: Identify and prioritize a small set of critical metrics that provide the most value for tracking progress, ensuring quality, and assessing risks. Examples include:
  + **Cost and Schedule Metrics**: Planned vs. actual effort, milestone completion status.
  + **Quality Metrics**: Defect density, open/closed defect trends.
  + **Process Metrics**: Requirements verification status, code coverage, or test progress.
* **Avoid Overhead**: Do not collect excessive data; focus on metrics that directly align with project objectives and risks.

---

### 2. **Leverage Existing Tools and Processes**

* Use **simple tools** like Excel, Google Sheets, or lightweight project management software (e.g., Asana, Trello, or Jira) to track and store metrics data.
* If the Center provides a repository for measurement data (see **SWE-091**), work with the Center’s repository managers to populate the required data efficiently. For smaller projects, this reduces duplication of effort.
* Standardize reporting templates to reduce administrative workload. NASA may provide existing templates (e.g., Software Metrics Report) that can be tailored for a small project.

---

### 3. **Establish a Lightweight Data Collection and Reporting Plan**

* **Define Data Collection Frequency**: Instead of frequent metric updates, determine a cadence that balances effort with project needs. For example:
  + Collect data and provide status reports monthly or bi-weekly as necessary (or according to the project’s milestones).
* **Use Summary Reporting**: Create **high-level visualizations** or summaries (e.g., status dashboards, trend charts) to communicate metrics data clearly and concisely. Highlight critical insights only—leave detailed analyses for on-request access.
* Example: A simple bar chart showing defect status trends (e.g., open vs. closed defects over time) is sufficient for updates.

---

### 4. **Streamline Communication**

* **Identify Primary Stakeholders**: Determine who needs the metrics (e.g., Mission Directorate, Chief Engineer, SMA, etc.). Coordinate early to clarify exactly what data they need and how often they expect reports.
* **Minimize Disruption**: Make data available as needed but limit efforts to produce analysis reports until formally requested. This reduces the burden on smaller teams while ensuring stakeholder engagement.
* **Provide Self-Service Access**: If possible, automate sharing of summarized data through email or make it available in online repositories, so stakeholders can access it directly as required.

---

### 5. **Coordinate with Center-Level Guidance**

* Collaborate with Center representatives (e.g., SMA, repository managers) to understand requirements for storing metrics data centrally. Standard NASA processes, repositories, and tools may reduce the burden on small projects by offering central support for data management.
* Leverage Center-wide repositories (see **SWE-091**) for sharing data, ensuring minimal duplication of efforts and compliance with agency-wide requirements.

---

### 6. **Integrate Metrics into Existing Workflows**

* Incorporate metrics collection and analysis into routine activities rather than treating it as separate overhead. For example:
  + Use sprint reviews or milestone meetings to update metrics like progress tracking or defect trends.
  + Request developers to document data during routine work (e.g., test logs or defect resolution tools) instead of relying on additional reporting steps.
* By embedding metrics into day-to-day activities, smaller projects can reduce redundant data collection efforts.

---

### 7. **Leverage Risk-Based Metrics for Small Projects**

* Focus metrics on areas of the highest technical or programmatic risk. For small projects, resource constraints make it impractical to track a comprehensive set of metrics across all domains. Examples:
  + For software interfacing with hardware, prioritize integration testing completion rates or interface defect tracking.
  + For projects with tight schedules, focus on planned vs. actual milestone completion rates.
* Tailor metric collection and reporting to areas with the greatest need for oversight.

---

### 8. **Fulfill Stakeholder On-Demand Requests**

* Ensure all required metrics are recorded and accessible (e.g., stored in the Center repository for compliance with **SWE-094**), but **only provide analysis reports on request**. For small projects, this reduces unnecessary reporting workload while maintaining compliance with sponsor requirements.
* When responding to requests:
  + Provide straightforward summaries where possible.
  + Use tools to present the data visually for quick comprehension.

---

### 9. **Assign Ownership of Metrics**

* Designate a **point of contact (POC)** for collecting, managing, and reporting metrics data. For small projects, this could be:
  + The project manager, systems engineer, or a lead developer with oversight of the development process.
* Having one responsible POC ensures clarity in communication, reduces redundancy, and allows stakeholders to know whom to contact for metrics data requests.

---

### Example: Small Project Implementation

* **Small CubeSat Software Development Project**:
  + Key Metrics:
    1. Total number of defects open/closed by week.
    2. Percentage of requirements verified.
    3. Code coverage from unit and system tests.
    4. Planned vs. actual milestone completion.
  + Metrics Collection: Defects tracked in Jira; test coverage tracked in CI/CD pipeline. Data summarized monthly in a status report.
  + Stakeholder Reports: Provide summary data (with charts) to the Mission Directorate and SMA quarterly. On-request access to data is fulfilled by exporting reports from the tracking tools and repositories.

---

### **Conclusion**

Smaller projects can meet the requirements for providing metrics data by selecting and tracking a focused set of critical metrics, leveraging existing tools and resources, and streamlining data collection and reporting processes. By embedding metrics into standard workflows, ensuring stakeholders have appropriate on-demand access, and minimizing administrative overhead, small projects can effectively balance compliance, efficiency, and data accessibility.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-329)

  [Software Measurement Guidebook,](https://ntrs.nasa.gov/search.jsp?R=19980228474 "Click to open in new window")

  Technical Report - NASA-GB-001-94 - Doc ID: 19980228474 (Acquired Nov 14, 1998), Software Engineering Program,
* (SWEREF-336)

  [Software Metrics Capability Evaluation Guide,](http://www.dtic.mil/docs/citations/ADA325385 "Click to open in new window")

  Software Technology Support Center (STSC) (1995), Hill Air Force Base. Accessed 6/25/2019.
* (SWEREF-355)

  [12 Steps to Useful Software Metrics,](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics_in_12_steps_paper.pdf "Click to open in new window")

  Westfall, Linda, The Westfall Team (2005),   Retrieved November 3, 2014 from http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics\_in\_12\_steps\_paper.pdf
* (SWEREF-567)

  [Know How Your Software Measurement Data Will Be Used](https://llis.nasa.gov/lesson/1772 "Click to open in new window")

  Public Lessons Learned Entry: 1772.
* (SWEREF-577)

  [Selection and use of Software Metrics for Software Development Projects](https://llis.nasa.gov/lesson/3556 "Click to open in new window")

  Public Lessons Learned Entry: 3556.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The NASA Lessons Learned database contains key insights related to the effective use of software measurement data and metrics in project management. The following lessons emphasize the importance of understanding how data will be used, selecting appropriate metrics, and applying them effectively across the software development lifecycle.

### **1. Lesson No. 1772: "Know How Your Software Measurement Data Will Be Used"**

#### **The Scenario**

During the Preliminary Mission & Systems Review (PMSR) for the Mars Science Laboratory (MSL) flight project, the team submitted a **Cost Analysis Data Requirement (CADRe)** document to the Independent Program Assessment Office (IPAO). This document included measurements such as **Source Lines of Code (SLOC)** estimates and other descriptive data for the proposed flight software. However, issues arose when the IPAO input this data into its **parametric cost estimation model**, resulting in:

* A misinterpretation of the submitted data (physical SLOC counts were misconstrued as logical SLOC counts).
* A **50% higher cost estimate** produced by the IPAO model compared to the project's estimate.

It became extremely difficult and time-consuming to reconcile these differences and correct the misunderstanding.

#### **Recommendation**

* **Clarify Data Use**: Before submitting software cost estimates or measurement data (e.g., SLOC, software reuse estimates) to NASA for evaluation—especially for major flight projects exceeding $500 million—verify how the recipient plans to interpret and utilize the data in their cost estimation models.
* **Duplicate and Compare**: To prevent misinterpretation, consider replicating the NASA analysis using the same or a similar parametric model. Compare the results to ensure alignment with NASA’s expectations and correct usage of the inputs.

### **2. Lesson No. 3556: "Selection and Use of Software Metrics for Development Projects"**

#### **The Scenario**

The design, development, and sustaining support of the Launch Processing System (LPS) application software for the Space Shuttle Program highlighted the importance of **appropriate metric selection** to enable visibility into a project’s status throughout the software development lifecycle. Metrics were found to be essential for detecting risks, maintaining efficiency, and facilitating project success.

#### **Recommendation**

#### **Early Planning for Metrics**

* As early as the **planning stage**, analyze and define the **measures or metrics** that will represent the "health" of the project and uncover potential risks (hindrances).
* Tailor the selection of metrics to the **unique characteristics** of the software project. Prioritize metrics that directly support decision-making and project efficiencies, as collecting and analyzing metrics requires additional resources.

#### **Examples of Useful Metrics:**

1. **Requirements Changes**: Track the number of added, deleted, or modified software requirements during each phase of the software process (e.g., design, development, testing).
2. **Errors During Validation**: Measure the number of errors identified during software verification and validation efforts.
3. **Delivered Software Errors**: Record the number of defects detected in delivered software (commonly referred to as "process escapes").
4. **Labor Hours**: Compare projected versus actual labor hours expended during the project.
5. **Code and Function Points**: Analyze projected versus actual lines of code developed and the number of function points in delivered software.

#### **Key Takeaways**

* Metrics or measurements facilitate **visibility** at all stages of development, enabling better project management and risk mitigation.
* Only collect metrics if their use directly translates into actionable insights or efficiency gains for the project. Prioritize quality over quantity to optimize the value of metric collection and analysis.

### 3. **Poor Metrics and Lack of Visibility into Software Health**

**Incident:**  
Psyche’s project metrics masked true software progress. Software risk was consistently under‑reported due to an aversion to categorizing issues as “red,” preventing leadership from recognizing schedule‑threatening problems.

**Lesson Learned:**

* **Objective Software Metrics:** Software maturity must be tracked using measurable indicators such as defect trends, verification progress, and test coverage.
* **Risk Transparency:** Leadership must encourage open reporting and avoid cultural pressures that suppress accurate risk assessments.

**Implication:**  
When metrics fail to reflect reality, management loses the ability to make timely decisions, creating preventable launch‑critical failures.

These lessons demonstrate the critical importance of understanding how measurement data will be used, selecting appropriate metrics for the project's specific needs, and ensuring alignment between stakeholders. Misinterpretation or inaccurate use of metrics, such as in cost models, can lead to costly delays, while tailored and carefully selected metrics enable better decision-making, risk detection, and process improvement. By applying these insights, project teams can enhance their software development practices and improve overall project outcomes.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-094 - Reporting of Measurement Analysis**

5.4.4 The project manager shall provide access to the software measurement data, measurement analyses, and software development status as requested to the sponsoring Mission Directorate, the NASA Chief Engineer, the Center Technical Authorities, HQ SMA, and other organizations as appropriate.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm access to software measurement data, analysis, and status as requested to the following entities, at a minimum:  
   - Sponsoring Mission Directorate  
   - NASA Chief Engineer  
   - Center Technical Authorities  
   - Headquarters SMA

## 7.2 Software Assurance Products

**7.2 Software Assurance Products**

Software Assurance (SA) activities for this requirement focus on ensuring that the appropriate stakeholders have access to measurement data, analyses, and development status as requested. This can include verifying evidence of compliance, confirming timely distribution of information, and addressing gaps in communication.

### **7.2.1 Status Presentation Showing Metrics and Trending Data**

One possible Software Assurance product for this requirement is to use a **status presentation** or report that includes:

1. **Key Metrics**: Data that reflects the health, progress, and risks associated with a software project.
2. **Trending Analysis**: Historical insights from metrics to evaluate progress over time or identify early signs of issues.
3. Major insights from **software measurement analysis** related to schedule, quality, defects, and risks.  
   This can serve as a tool for confirming compliance with this requirement during major reviews or audits.

## 7.3 Metrics

No specific metrics have been defined for this requirement at this time. However, Software Assurance activities can leverage existing project metrics (see **SWE-090** and SWE-093) to verify accessibility and utility of the measurement data. Examples may include:

* **Defect metrics**: Open vs. closed defects or defect density trends.
* **Schedule metrics**: Planned vs. actual milestone completion.
* **Progress metrics**: Percentage of requirements implemented and verified.  
  These metrics should align with the specific needs of the project and help satisfy the measurement data requirements of the key stakeholders.

## 7.4 Software Assurance Guidance

The primary Software Assurance responsibility for this requirement is to confirm that the following groups have access to the software measurement data, measurement analysis, and software development status when requested:

1. Sponsoring Mission Directorate
2. NASA Chief Engineer
3. Center Technical Authorities
4. Headquarters SMA

The guidance below outlines a streamlined, structured approach for this confirmation.

#### **1. Verify the Inclusion of Data in Status Reporting**

* Review **status reports**, presentations, or other deliverables to check if the required information (e.g., software measurement data, analyses, development status) is included.
* Confirm that the status reports:
  1. **Identify key metrics** that summarize the project’s health, progress, and risks.
  2. Highlight trends or major takeaways from the **measurement analysis**.
  3. Include updates on the **software development status**, such as milestone progress, testing status, and risks/issues identified.
* If the information is included in reports or presentations, verify evidence that these were **distributed** or communicated to the four groups on the requested timeline.

#### **2. Confirm Data Availability for On-Demand Requests**

* As part of Software Assurance, check whether the software measurement data, measurement analysis, and development status were made **available upon request** to the four key groups.

  + Ensure no outstanding gaps in fulfilling **data requests** (e.g., verify whether all requested data was provided in full and on time).
* **Ask Proactively**: If feasible, engage with the recipients to determine whether:

  1. Any **specific requests** to the project for measurement data or analysis went unanswered.
  2. Any results provided were incomplete, misleading, or delayed.  
     This step ensures that any compliance gaps in providing data can be addressed promptly.

#### **3. Confirm Metrics Are Identified in Project Management Documents**

* Software Assurance should verify that the project’s plans (e.g., Software Management Plan, Software Development Plan, Measurement Plan) specify:
  + The **metrics and measurements** being collected.
  + The methods and tools used to collect, analyze, and manage these metrics.
  + The process for **distributing results** to the required stakeholders.
* This ensures that metric collection and reporting are defined clearly and integrated into the project workflow, reducing the likelihood of oversight or missed communications.

#### **4. Leverage Organizational Tools to Track Metrics**

* Collaborate with the project team to verify the use of a **centralized repository** (see SWE-091) or tool to store software measurement data.
  + Confirm whether the repository or tool facilitates **easy data access** for the four groups identified.
* Ensure that the project’s selected metrics (e.g., cost, quality, schedule) align with relevant stakeholder concerns and **organizational assurance goals**.

#### **5. Verify Data Completeness and Consistency**

* Conduct periodic reviews of measurement data and analyses to confirm they are:
  + **Complete**: All expected metrics, trends, and insights are provided.
  + **Consistent**: Data aligns with the project’s stated measurement and collection processes.
  + **Accurate**: Metrics represent the true state of the project as approved by the project team.

#### **6. Provide Additional Assurance Metrics (If Applicable)**

* Software Assurance activities may include collecting **separate assurance metrics** (if relevant to project goals) to validate the consistency and completeness of measurement data. Refer to **Topic 8.18,** which provides guidance on:
  + Assurance metric goals.
  + Questions these metrics can answer for oversight.

#### **7. Address Stakeholder Collaboration Early**

* Engage with the Sponsoring Mission Directorate, NASA Chief Engineer, Center Technical Authorities, and HQ SMA early in the project lifecycle to **understand their expectations**:

  + What data do they require?
  + When and how should the data be distributed (e.g., in periodic reports, reviews, or via ad-hoc requests)?
* Establishing clear communication protocols ensures that Software Assurance can proactively verify compliance.

Software Assurance plays a critical role in verifying that software measurement data, analysis, and development status are accessible to key stakeholders (Mission Directorate, NASA Chief Engineer, Center TAs, HQ SMA). By confirming that data is properly documented, accessible, and delivered as requested, Software Assurance ensures transparency, accountability, and compliance with this requirement. Engaging with stakeholders early and leveraging organizational repositories and reporting processes will help streamline data access while minimizing risks of compliance gaps. For additional assistance, refer to **Topic 8.18** for metrics related to organizational assurance goals.

See topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics). For a table of software assurance metrics with their associated goals and questions.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

The following examples of **Objective Evidence** help demonstrate compliance with the requirement that the project manager "provides access to the software measurement data, measurement analyses, and software development status as requested" to specific key stakeholders:

---

### 1. **Status Reports or Presentations**

* **Description**: Reports or presentations that include updates on software measurement data, analysis, and development status.
* **Examples**:
  + Weekly/monthly status reports showing project milestones, progress, and performance metrics.
  + Presentations prepared for mission reviews, such as the Preliminary Design Review (PDR), Critical Design Review (CDR), and other lifecycle reviews.
  + Slides or documents presenting key metrics such as defect counts, requirement verification progress, or schedule performance.
* **Evidence to Collect**:
  + Dated reports/presentations to confirm they were delivered on time.
  + Distribution lists or records of recipients (e.g., Mission Directorate, NASA Chief Engineer, etc.).

---

### 2. **Meeting Minutes or Attendance Logs**

* **Description**: Documentation from meetings or reviews where software metrics and status updates were discussed with stakeholders.
* **Examples**:
  + Minutes from project review boards, risk management meetings, or metrics review sessions.
  + Evidence that stakeholders (e.g., Center Technical Authorities, SMA personnel) were present during discussions of project status.
  + Meeting agendas that include specific items related to software measurement data and analysis.
* **Evidence to Collect**:
  + Signed or approved meeting minutes.
  + Attendance rosters or confirmation emails.
  + Action items or resolutions related to requested metrics.

---

### 3. **Email or Communication Records (Request/Response)**

* **Description**: Correspondence demonstrating that stakeholders requested and received access to the required measurement data, analyses, and development status.
* **Examples**:
  + Email threads with attached reports or links to repositories.
  + Requests from stakeholders for specific data/analyses and corresponding responses confirming delivery.
  + Notifications sent regarding data availability in repositories or tools.
* **Evidence to Collect**:
  + Timestamped emails.
  + Attachments or links to requested metrics/documents.
  + Confirmation or acknowledgment responses from stakeholders.

---

### 4. **Access Logs for Centralized Repositories or Tools**

* **Description**: Logs confirming that stakeholders were granted access to the software measurement data and repositories where data is housed.
* **Examples**:
  + Records of access to tools like JIRA, DOORS, Confluence, or NASA repositories for metric management.
  + Evidence of data uploads to Center repositories (per **SWE-091**).
  + Permission documentation showing stakeholder access to relevant tools or dashboards.
* **Evidence to Collect**:
  + Access logs showing stakeholder interactions with the repository.
  + Audit trails verifying that data was uploaded on time and made available.
  + Screenshots of dashboards or tools demonstrating that visuals and metrics were available.

---

### 5. **Project-Specific Management or Development Plans**

* **Description**: Plans or documents detailing the metrics being collected, their analysis, and the reporting process for making the data accessible to stakeholders.
* **Examples**:
  + Software Development Plan (SDP).
  + Software Management Plan (SMP).
  + Measurement Plan identifying key metrics, collection schedules, and distribution processes.
  + Compliance matrices linking metrics or data categories to stakeholder requirements.
* **Evidence to Collect**:
  + Copies of approved plans.
  + Sections of the plan identifying how data is provided to the Sponsoring Mission Directorate, NASA Chief Engineer, Center Technical Authorities, and HQ SMA.
  + Change logs demonstrating updates and reviews of these plans.

---

### 6. **Software Metrics Reports**

* **Description**: Documents summarizing the software metrics collected during the project’s lifecycle, trends analyzed, and their implications for project success.
* **Examples**:
  + Standard **Software Metrics Reports** prepared during project monitoring.
  + Metrics tables summarizing major milestones, KPIs (Key Performance Indicators), or risk indicators.
* **Evidence to Collect**:
  + Final or draft versions of metrics reports.
  + Distribution logs confirming that these reports were shared with relevant stakeholders.
  + Versions filed in the Center repository for historical records.

---

### 7. **Requests for Inputs during Reviews or Audits**

* **Description**: Evidence of compliance gathered during formal reviews (e.g., Peer Reviews, Lifecycle Reviews, Audits). This may include stakeholder feedback on data clarity, availability, or completeness.
* **Examples**:
  + Action items raised in PDR, CDR, or software readiness reviews requesting more detailed metrics or clarifications.
  + Non-conformance reports (NCRs) or Corrective Action Records related to metrics accessibility, if applicable.
* **Evidence to Collect**:
  + Review documents with clear resolutions showing compliance with data requests.
  + Feedback reports confirming the requested data was evaluated successfully.
  + Formal sign-offs or approvals from stakeholders.

---

### 8. **Software Assurance Verification Records**

* **Description**: Records from **Software Assurance (SA)** activities confirming that software measurement data, analysis, and status updates were made available and compliant with requirements.
* **Examples**:
  + SA audits verifying end-to-end compliance with SWE-094.
  + Records of SA reviews confirming that data was distributed to relevant groups.
* **Evidence to Collect**:
  + Signed SA verification checklists.
  + Records of communication between SA and project teams.
  + Reports demonstrating SA audits or reviews of project metrics and accessibility.

---

### 9. **Stakeholder Feedback or Survey Results**

* **Description**: Collect stakeholder feedback to confirm whether their needs were met regarding access to data, timeliness of delivery, and completeness.
* **Examples**:
  + Completed stakeholder satisfaction surveys or feedback forms.
  + Emails or review comments acknowledging or confirming receipt of the required metrics.
* **Evidence to Collect**:
  + Completed forms or summaries of stakeholder feedback.
  + Confirmations of satisfaction with the measurement data and analyses provided.

---

### Summary Table of Objective Evidence

| **Category** | **Example Evidence** |
| --- | --- |
| Status Reports/Presentations | Dated reports, presentations with distribution records or acknowledgments. |
| Meeting Records | Approved meeting minutes, attendance logs, or action item resolutions. |
| Communication Records | Email threads, attachments, or notifications confirming requested data was delivered. |
| Repository Access Logs | Repository access/audit logs, screenshots of uploaded metrics, or tool permissions documentation. |
| Management Plans | Approved Software/Measurement Plans, highlighting reporting and data accessibility. |
| Software Metrics Reports | Metrics summaries/trends with distribution records. |
| Audit/Review Documentation | Action items, resolutions, or feedback records confirming compliance with required data access. |
| Software Assurance Records | SA verification checklists, audit reports, or records demonstrating assurance reviews. |
| Stakeholder Feedback | Completed surveys, acknowledgment emails, or stakeholder comments affirming the availability/sufficiency of measurement data. |

---

### Key Considerations

* All objective evidence must clearly demonstrate **traceability** to specific requests or reporting commitments for measurement data, analyses, and development status.
* When possible, collect **timestamped records** to confirm that data was delivered in a timely and complete manner.
* Address corrective actions (if needed) with documented resolutions to ensure stakeholders have the confidence that data accessibility issues will not recur.

This comprehensive objective evidence ensures that compliance with the requirement is well-documented, verifiable, and readily demonstrable to all relevant stakeholders.

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
