# SWE-090 - Management and Technical Measurements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695475. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements

SWE-090 - Management and Technical Measurements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695475)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695475&showCommentArea=true&showComments=true#addcomment)

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

5.4.2 The project manager shall establish, record, maintain, report, and utilize software management and technical measurements.

## 1.1 Notes

The NASA-HDBK-2203 contains a set of candidate management indicators that may be used on a software development project. The NASA Chief Engineer may identify and document additional Center measurement objectives, software measurements, collection procedures and guidelines, and analysis procedures for selected software projects and software development organizations. The software measurement process includes collecting software technical measurement data from the project’s software developer(s).

## 1.2 History

Click here to view the history of this requirement: SWE-090 History

SWE-090 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.4.1 The project shall establish and document specific measurement objectives for their project. |
| Difference between A and B | Expanded scope of metrics.  Added requirements to record, maintain, report, and utilize software management and technical measurements. |
| B | 5.4.2 The project manager shall establish, record, maintain, report and utilize software management and technical measurements. |
| Difference between B and C | No change |
| C | 5.4.2 The project manager shall establish, record, maintain, report, and utilize software management and technical measurements |
| Difference between C and D | No change |
| D | 5.4.2 The project manager shall establish, record, maintain, report, and utilize software management and technical measurements. |

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

Numerous years of experience on many NASA projects demonstrate the following three key reasons for software measurement activities [329](#_tabs-<p></p>):

1. To understand and model software engineering processes and products.
2. To aid in assessing the status of software projects.
3. To guide improvements in software engineering processes.

The requirement outlined in 5.4.2 ensures the effective management and monitoring of a software project by requiring the project manager to establish, record, maintain, report, and utilize software management and technical measurements. Below is the rationale for this requirement:

1. **Improved Decision-Making**:

   * Software management and technical measurements provide quantitative data that support informed decision-making. By tracking project metrics (e.g., schedule variance, defect density, or resource utilization), the project manager can assess the health and progress of the project and make necessary adjustments to stay on track.
2. **Progress Tracking**:

   * Establishing and maintaining metrics ensures that the project is consistently monitored over time. This helps in tracking whether the project is meeting its goals, whether deadlines can be adhered to, and whether resources are being used effectively.
3. **Risk Management**:

   * Continuous monitoring of software metrics aids in the early identification of issues or risks. For example, if productivity metrics or defect rates deviate significantly from the baseline, potential risks can be mitigated before they impact the project's success.
4. **Accountability and Transparency**:

   * Recording and reporting the measurements ensures accountability and transparency. Stakeholders can review the metrics and gain insights into project performance, increasing trust and engagement among team members and clients.
5. **Ensures Quality**:

   * Technical measurements, such as code quality metrics, defect density, or test coverage, help ensure that the delivered software meets quality standards. These metrics can uncover technical debt, ensure compliance with coding standards, and verify that the end product aligns with user requirements.
6. **Process Improvement**:

   * By analyzing recorded metrics after project completion, the organization can identify trends and opportunities for process improvement. This allows the team to refine workflows, optimize resource allocation, and enhance overall project efficiency in future endeavors.
7. **Compliance with Standards**:

   * Many software development methodologies, frameworks, and standards (e.g., ISO/IEC standards, CMMI, or Agile methodologies) include requirements to track and report management and technical measures. Compliance with these requirements ensures alignment with industry best practices.
8. **Communication with Stakeholders**:

   * Metrics serve as a common language for communication between technical teams, management, and other stakeholders. They provide an objective way to discuss project progress, performance, and issues, reducing ambiguity and misunderstandings.
9. **Facilitates Continuous Monitoring**:

   * Maintaining and updating these measurements consistently throughout the project lifecycle allows for ongoing assessment. This is critical for developing a proactive approach to managing the project rather than waiting for major issues to arise.
10. **Supports Utilization of Data for Future Projects**:

    * Historical data gathered from software management and technical measurements can help estimate and plan for future projects by providing baseline information on project duration, costs, and resource needs.

In summary, the requirement to establish, record, maintain, report, and utilize software management and technical measurements ensures that a software project is well-managed, transparent, and aligned with organizational goals. It enhances the likelihood of delivering a high-quality product on time and within budget while promoting continuous improvement.

# 3. Guidance

Software engineering projects benefit significantly from data-driven decision-making. Accurately understanding the status of a project or evaluating the effectiveness of development processes can be challenging without reliable performance measures and baseline comparisons. The collection, analysis, and utilization of metrics enable project managers to monitor progress, assess quality, identify risks, and support continuous improvement initiatives. Metrics are not just numbers—they are an essential part of ensuring effective project control, process improvement, and stakeholder communication.

### Purpose of Software Measurements

There are four key reasons for measuring processes, products, and resources within software projects: **Characterization, Evaluation, Prediction, and Improvement**:

1. **Characterization**:

   * Measurements are conducted to understand processes, products, resources, and environments.
   * Baselines are established to enable comparisons with future efforts and drive consistency.
   * Metrics provide the foundation for understanding "how we work" and inform process baselines that organizational stakeholders and teams can improve over time.
2. **Evaluation**:

   * Measurements allow project teams to assess whether plans are on track (e.g., schedule, budget, resource allocation).
   * They act as early warning systems—helping identify deviations so adjustments can be made proactively.
   * Evaluation ensures alignment with quality standards and helps gauge the impact of technology or process changes on project outcomes.
3. **Prediction**:

   * Metrics generate data that supports proactive planning and informed forecasting (e.g., schedule adjustments, risk impact analysis).
   * Understanding correlations between metrics can set achievable goals for projects in terms of **cost**, **schedule**, and **quality**.
   * Predictions, derived from historical data, enable the development of more reliable estimates for future projects or project phases.
4. **Improvement**:

   * Measurements are a cornerstone of continuous improvement initiatives. Data-driven evaluations highlight inefficiencies or areas for enhancement.
   * Metrics allow organizations to validate the effectiveness of corrective actions and ensure improvement projects achieve their intended results.
   * Quantitative data also fosters communication by making improvement goals tangible and relatable to all stakeholders.

### Key Benefits of Software Measurement Programs

The primary goals of a successful software measurement program include:

* Providing objective insight into project progress to ensure alignment with planned schedules and budgets.
* Ensuring the software developed meets requirements and satisfies user needs.
* Establishing quality benchmarks to enhance both product reliability and process robustness.
* Supporting early identification and management of risks.
* Tracking the volatility of requirements to improve requirements stability and project outcomes.
* Building a historical repository of data to refine future cost estimation, resource planning, and delivery schedules.
* Creating feedback loops for process improvement and future project optimizations.

Metrics are therefore not only tools for *current project control* but also for *enhancing organizational maturity and readiness* over time.

---

### Establishing and Utilizing Key Software Measurements

#### 1. **Measurement Objectives**

* Measurement objectives must align with both project and organizational goals.
* Objectives should answer specific, actionable questions related to progress, quality, resources, cost, and risk (e.g., "What is the current defect rate? Are we on track for schedule performance?").
* Clear and measurable objectives guide the selection and prioritization of appropriate metrics. Per NASA’s standards, objectives address organizational goals such as:
  + Delivering software on time and within budget.
  + Improving cost estimation and planning accuracy.
  + Reducing software defects and rework.
  + Enhancing resource allocation.

#### 2. **Measurement Categories**

* Projects need to define and track both **management-driven metrics** and **technical-driven metrics**. These two categories encompass a range of potential measurements, including but not limited to:
  + **Management-Included Metrics**:
    - **Schedule Performance**: Planned vs. actual milestone completion.
    - **Cost Metrics**: Projected vs. actual staffing levels, work-effort costs.
    - **Resource Utilization**: Hardware or personnel capacities.
    - **Defect Rates**: Open and closed defect reports by severity.
    - **Requirements Stability**: Frequency and volume of changes to requirements.
  + **Technical Indicators**:
    - Code quality (cyclomatic complexity, defect density).
    - Traceability metrics (e.g., bi-directional linking between requirements, design, and test artifacts).
    - Test coverage (percentage of code tested by validation suites).
    - Integration progress (modules integrated over time).

#### 3. **Establishing Baselines**

* Initial baseline data captures project-specific measures early in the lifecycle, allowing the team to set realistic benchmarks for comparison.
* Periodic reassessment of baselines helps measure long-term project trends and improvements.

#### 4. **Selecting and Standardizing Measures**

* Keep the set of collected measures manageable by prioritizing those aligned with objectives.
* Use tools and automated systems when possible (e.g., **JIRA** for issue tracking, **DOORS** for requirements management) to ensure consistency in measurement collection and reduce manual effort.
* Define each measure clearly (e.g., “defect density calculates defects per unit of code”) to avoid ambiguity or misinterpretation.

### Reporting and Analysis of Measurements

#### **Key Reporting Elements**:

* **Stakeholders**: Metrics data supports diverse stakeholders, including developers, project managers, and policymakers. Tailor reports to match stakeholder needs (e.g., detailed technical metrics for engineers, summary-level management indicators for executives).
* **Visualization**: Charts, dashboards, and trend graphs can enhance communication by making data insights more intuitive.
* **Frequency**: Generate regular progress reports (e.g., weekly, biweekly, monthly) and provide stakeholders with the option for ad hoc reporting on demand.
* **Level of Detail**:
  + Managers: Comparative trends (e.g., schedule variance, defect containment trends).
  + Developers/Teams: Actionable task-based metrics (e.g., code review outputs or defect-resolution timelines).

#### **Utilization of Metrics Analysis**:

* **Identifying Trends**: Metrics not only capture the “current status” but also highlight emerging trends that may affect project success.
* **Process Corrections**: Analysis of deviations informs process improvement plans, ensuring rapid responses to project drift.
* **Performance Monitoring**: Continuous tracking provides assurance that the development effort will meet delivery timelines and budget constraints.

### Guidance for Measurement Programs and Data Analysis

#### **Establishing Data Collection Systems**

* Define systematic and repeatable data collection procedures for each metric category.
* Include automation tools to capture metrics reliably, such as static analysis tools (e.g., Coverity, SonarQube) for source code measurements.
* Clearly document data definitions, roles responsible for collection, and submission procedures.

#### **Alignment of Metrics to Goals**

* Ensure measures directly trace to project and organizational goals, validating their relevance and usefulness.
* Incorporate periodic reviews to assess whether chosen metrics adequately address evolving project needs.

### Continuous Improvement Through Metrics

Effective measurement systems extend beyond meeting immediate project needs. They also provide baseline data critical for advancing organizational learning and process maturity. For example, historical analysis of defect trends and resource utilization can lead to:

* Enhanced prediction accuracy for future projects.
* Faster identification of root causes during retrospectives.
* Increased organizational efficiency through better resource allocation.

Metrics programs are a **foundational pillar of continuous improvement**, ensuring that lessons learned from one project are effectively transferred to the next.

By effectively defining, recording, analyzing, and utilizing management and technical measurements, project teams can ensure delivery success while fostering long-term organizational growth.

**12 Steps to Useful Software Metrics**

Step 2 Target Goals  
"At the organizational level, we typically examine high-level strategic goals like being the low cost provider, maintaining a high level of customer satisfaction, or meeting projected revenue or profit margin target. At the project level, we typically look at goals that emphasize project management and control issues or project level requirements and objectives. These goals typically reflect the project success factors like on time delivery, finishing the project within budget or delivering software with the required level of quality or performance. At the specific task level, we consider goals that emphasize task success factors. Many times these are expressed in terms of the entry and exit criteria for the task."[355](#_tabs-<p></p>)

See also Topic [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects).

There are specific example measurements listed in the software metrics report (see [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report)) that were chosen based on identified informational needs and from questions shared during several NASA software measurement workshops.

Activities within the data collection procedure include:

* A clear description of all data is to be provided. This includes a description of each item and its format, a description of the physical or electronic form to be used, and the location or address for the data to be sent.

* A clear and precise definition of terms. This includes a description of the project or organization-specific criteria, definitions, and a description of how to perform each step in the collection process.

**12 Steps to Useful Software Metrics**

Step 5 Standardize Definitions  
"When we use terms like defect, problem report, size, and even project, other people will interpret these words in their own context with meanings that may differ from our intended definition. These interpretation differences increase when more ambiguous terms like quality, maintainability, and user-friendliness are used."[355](#_tabs-<p></p>)

* Who is responsible for providing which data. This may be easily expressed in matrix form, with clarifying notes appended to any particular cell of the matrix.
* When and to whom the data are to be provided. This describes the recipient(s) and management chain for the submission of the data; it also specifies the submission dates, periodic intervals, or special events for the collection and submission of the data.

## 3.1 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVB/pages/32604383/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVB/pages/32604385/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.2 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics) |

# 4. Small Projects

Small projects often operate with constrained budgets, limited staff, and tighter schedules. These constraints can make it challenging to implement comprehensive measurement programs. However, tailored and focused measurement objectives can still provide significant value in ensuring project success while aligning with sponsor and institutional requirements. The following guidance provides practical and scalable support for small projects to fulfill software management and technical measurement requirements effectively while balancing their resource limitations.

---

### Key Considerations for Small Projects

#### 1. **Prioritize Objectives and Measures**

* Focus on **critical metrics** that are most important to achieving project goals, meeting sponsor requirements, and aligning with institutional objectives. Examples of key areas include:
  + **Schedule monitoring**: Are milestones being met?
  + **Resource utilization**: Are costs and effort within budget?
  + **Defect density**: Is the software achieving the required quality level?
  + **Requirements volatility**: How stable are the requirements?
* Check your Center’s tailored measurement requirements for small projects when selecting objectives. Many Centers have pre-defined metrics or reduced sets of requirements designed specifically for small-scale projects to minimize administrative overhead.

#### 2. **Limit Measurement Scope and Frequency**

* For small projects, a **limited set of essential measures** is often sufficient to track status effectively. Collect only the data necessary to monitor progress, ensure acceptable risk levels, and demonstrate compliance with quality and safety standards.
* **Adjust frequency of data collection** based on project needs. For example:
  + Small projects may collect and analyze data at key milestones or during reviews instead of generating weekly or monthly reports.
  + Data reporting can be streamlined for **major reviews**, such as design reviews, implementation milestones, or annual reporting cycles.

#### 3. **Leverage Automation and Tools**

* The use of tools that **automatically collect, track, and store project data** can drastically reduce the manual effort and cost of implementing a measurement program. For example:
  + Many projects within NASA use **JIRA** and its plug-ins, which support automated tracking of work items, progress, and other metrics.
  + Consider using configuration management systems or development environments with built-in measurement capabilities to automate data collection.
* If specialized tools are cost-prohibitive, explore low-cost or shared solutions:
  + Some Centers, like **Goddard Space Flight Center (GSFC)**, have developed simple tools (e.g., Excel-based templates) to automate measurements such as staffing, requirements metrics, issue tracking, and risk management.
  + Collaborate with your Center or organization to access shared tools, resources, or personnel who can assist with measurement collection, storage, and analysis.

#### 4. **Document Measurement Procedures**

* Even for small projects, it is essential to document how metrics will be collected, stored, and used. This ensures clarity and aligns with organizational requirements.
* Include procedures for data collection and reporting in the **Software Development Plan (SDP)**, even if the plan is scaled down for the project. These procedures should provide clear instructions on:
  + What data is to be collected.
  + When and how often data is collected and reported.
  + Who is responsible for collecting and analyzing data.

---

### Data Reporting for Small Projects

* **Streamline Reporting for Efficiency**: Reporting activities for small projects can be limited to key metrics that demonstrate compliance with **safety, quality, and institutional objectives**. Examples include:
  + Metrics required for process improvement (e.g., defect trends, rework rates).
  + Quality and performance indicators.
  + Risk-related metrics.
* **Frequency of Reports**: For small projects, measurement reporting may not need to be as frequent as for larger efforts. For example:
  + Annual or milestone-specific reports may be sufficient.
  + Focus on presenting aggregated data during major project reviews or audits.

---

### Addressing Common Challenges

#### **Challenge: Limited Access to Tools or Resources**

* **Solution**: Collaborate with your Center to leverage shared resources, such as software tools, templates, or personnel support. Examples:
  + Some Centers offer **measurement specialists** who can assist small projects with setup, collection, and analysis of data.
  + Utilize **free or low-cost tools** created by Centers like GSFC (e.g., Excel-based tools for staffing, metrics tracking, and risk reporting).
* **Example GSFC Tools**:
  + **Staffing Tool**: Tracks planned vs. actual staffing across the project lifecycle.
  + **Requirements Metrics Tool**: Monitors requirements change volatility and traceability.
  + **Risk Tool**: Captures and tracks identified project risks.
  + **Problem Reporting Tool**: Tracks open/closed problem reports and severity analysis.

#### **Challenge: Budget and Staff Constraints**

* **Solution**: Minimize measurement costs by:
  + Reducing the number of metrics collected to focus only on essential measures tied to **project success**.
  + Using automation to reduce manual efforts wherever possible.
  + Incorporating measurement planning into **existing workflows or tools** (e.g., Jira, GitHub action logs, or automated CI/CD pipelines for test coverage).

#### **Challenge: Justifying Minimal Measurement Sets**

* **Solution**: Clearly align chosen metrics with project and organizational goals. For example:
  + **Risk Metrics**: Demonstrate how tracking open risks aligns with quality assurance goals.
  + **Defect Metrics**: Show how defect density measurements ensure the software will meet safety-critical criteria in resource-constrained environments.

---

### Practical Recommendations for Small Projects

1. **Start Simple**:

   * Begin with basic metrics tied to project success, such as progress tracking (planned vs. actual) and defect management.
   * Gradually expand metrics only if additional data becomes critical for decision-making.
2. **Use Scalable and Flexible Tools**:

   * Tools like JIRA, Trello, or even simple Excel spreadsheets can be adapted for small projects. Look for tools with **plug-ins** that streamline data collection and reporting.
3. **Collaborate with Center Resources**:

   * Engage with your Center’s software engineering team to access shared tools, training, or measurement expertise. Centers like GSFC or others may have dedicated organizational assistance for small projects.
4. **Integrate Measurement into Agile Processes**:

   * If using Agile, align tracking metrics (e.g., sprint velocity, backlog progress) with measurement objectives for streamlined integration into existing workflows.

---

### Summary

Small projects can achieve effective software measurement by focusing on **critical metrics**, **leveraging automation**, and adopting **shared resources** to minimize effort and cost. By tailoring measurement programs to their specific needs, small projects avoid overburdening limited resources while still ensuring compliance with organizational standards and achieving project success.

Key points for small projects:

* Select and focus only on a **few essential measures** tied to project objectives.
* Utilize tools, whether shared or simple templates, to automate and support measurement collection.
* Document and streamline data collection, storage, and reporting procedures in the Software Development Plan.
* Leverage shared organizational tools and resources to reduce cost and effort.

By creating focused, efficient, and practical measurement systems, small projects can meet their objectives while staying within constraints, enabling smooth progress and high-quality outcomes.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-032) Measurement and Analysis for Projects,  580-PC-048-04, NASA Goddard Space Flight Center (GSFC), 2019.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-089) Project-Type/Goal/Metric Matrix, developed by NASA Software Working Group Metrics Subgroup, 2004.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-252)

  [Software Metrics: SEI Curriculum Module SEI-CM-12-1.1.](http://www.sei.cmu.edu/reports/88cm012.pdf "Click to open in new window")

  Mills, Everald E. (1988). Carnegie-Mellon University-Software Engineering Institute.  Retrieved on December 2017 from http://www.sei.cmu.edu/reports/88cm012.pdf.
* (SWEREF-329)

  [Software Measurement Guidebook,](https://ntrs.nasa.gov/search.jsp?R=19980228474 "Click to open in new window")

  Technical Report - NASA-GB-001-94 - Doc ID: 19980228474 (Acquired Nov 14, 1998), Software Engineering Program,
* (SWEREF-336)

  [Software Metrics Capability Evaluation Guide,](http://www.dtic.mil/docs/citations/ADA325385 "Click to open in new window")

  Software Technology Support Center (STSC) (1995), Hill Air Force Base. Accessed 6/25/2019.
* (SWEREF-355)

  [12 Steps to Useful Software Metrics,](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics_in_12_steps_paper.pdf "Click to open in new window")

  Westfall, Linda, The Westfall Team (2005),   Retrieved November 3, 2014 from http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics\_in\_12\_steps\_paper.pdf
* (SWEREF-367)

  [IEEE Standard Dictionary of Measures of the Software Aspects of Dependability,](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1634994 "Click to open in new window")

  IEEE Computer Society, Sponsored by the Software Engineering Standards Committee, IEEE Std 982.1™-2005, (Revision of IEEE Std 982.1-1988),
* (SWEREF-378)

  [Systems and software engineering — Measurement process](https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:15939:ed-1:v1:en "Click to open in new window")

  ISO/IEC/IEEE 15939:2017(en) NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-430)

  ["Lessons learned from 25 years of process improvement: The Rise and Fall of the NASA Software Engineering Laboratory,"](http://www.cs.umd.edu/projects/SoftEng/ESEG/papers/83.88.pdf "Click to open in new window")

  Basili, V.R., et al. (May, 2002). University of Maryland, College Park. Experimental Software Engineering Group (ESEG). Lessons Learned Reference.
* (SWEREF-567)

  [Know How Your Software Measurement Data Will Be Used](https://llis.nasa.gov/lesson/1772 "Click to open in new window")

  Public Lessons Learned Entry: 1772.
* (SWEREF-572)

  [Flight Software Engineering Lessons](https://llis.nasa.gov/lesson/2218 "Click to open in new window")

  Public Lessons Learned Entry: 2218.
* (SWEREF-577)

  [Selection and use of Software Metrics for Software Development Projects](https://llis.nasa.gov/lesson/3556 "Click to open in new window")

  Public Lessons Learned Entry: 3556.
* (SWEREF-583)

  [Space Shuttle Program/Operations-Processing/Workforce](https://llis.nasa.gov/lesson/1024 "Click to open in new window")

  Public Lessons Learned Entry: 1024.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA’s Lesson Learned database provides valuable insights into topics that must be carefully addressed when planning and implementing a software measurement program. These lessons emphasize the importance of understanding how measurement data will be used, selecting appropriate metrics, fostering a safety-centric culture, and ensuring that measures drive meaningful improvements in software processes. Below are key lessons learned and their relevance to selecting objectives and related measures for software measurement programs.

---

#### **1. Understand How Software Measurement Data Will Be Used**

**Lesson Number 1772**:  
When software measurement data is provided for critical purposes, such as supporting **cost estimates** for projects, it is paramount to understand how the data will be interpreted and applied. Failure to align expectations between project teams and NASA evaluators can result in major discrepancies and erroneous estimates, disrupting the assessment, approval, and planning processes.

**Recommendation**:

* Verify how the collected software metrics will be used, particularly in **cost estimation models** or other formal analyses. For large or high-profile projects, such as major flight missions, efforts should be made to duplicate or simulate NASA’s processes wherever possible to ensure consistency before submission.
* Communicate proactively with NASA's cost estimation teams to verify assumptions, modeling techniques, and data formats, ensuring accurate and meaningful input.

---

#### **2. Prioritize Safety in Metrics Over Schedule and Cost**

**Lesson Number 1042**:  
In environments with **competing priorities** (e.g., meeting deadlines, budget constraints), there is a tendency to prioritize schedule or cost over safety, particularly in operational and maintenance phases. This lesson highlights the importance of fostering a culture that places safety above all other considerations.

**Recommendation**:

* **Integrate safety-related metrics** into measurement programs to ensure it remains a priority. Examples of safety-focused metrics include:
  + The number of critical or hazard-related defects identified and resolved.
  + The frequency of reviews or audits for safety compliance.
  + The effectiveness of mitigation strategies for identified software hazards.
* Maintain open communication channels to promote candor and collaborative efforts to refine meaningful operational effectiveness measures.

---

#### **3. Tailor Metrics to Project Needs and Usefulness**

**Lesson Number 3556**:  
The lesson is drawn from the **Space Shuttle Program's Launch Processing System (LPS)** and stresses that metrics provide critical visibility into a project’s status throughout its lifecycle. However, it also underscores that selecting metrics without consideration of their appropriateness can waste resources without bringing value to the project.

**Recommendation**:

* Perform a **thorough analysis during project planning** to determine the most relevant and valuable metrics for the unique needs and risks of the project.
* Only select and use metrics that enhance decision-making and produce measurable efficiencies in the development process.
* Examples of **useful metrics** include:
  + **Requirements volatility**: Number of software requirements added, deleted, or modified during each development phase (e.g., design, testing).
  + **Validation and defect metrics**: Number of defects identified during testing versus post-delivery (to gauge process escapes).
  + **Effort estimation accuracy**: Projected vs. actual labor hours expended.
  + **Code metrics**: Projected vs. actual lines of code or number of function points in delivered software.

**Additional Note**: Ensure metrics are aligned with results—measurements should focus on providing actionable insights and not merely tracking for the sake of compliance.

---

#### **4. Use Objective Measures to Track Progress and Mitigate Software Development Risks**

**Lesson Number 2218**:  
This lesson, derived from **NASA/Caltech Jet Propulsion Laboratory (JPL)** flight software projects, underscores the role of objective metrics in safeguarding the cost, schedule, and quality of flight software (FSW) development. Given the complexity of FSW and the need for significant new functionality in every mission, the risks in software production, testing, and verification must be carefully managed.

**Recommendation**:

* **Adopt objective measures** to monitor the health and progress of software development. Valuable metrics include:
  + **Requirements metrics**: Percentage of allocated requirements, system-level requirements, and software-specific requirements that have been defined, baselined, or implemented.
  + **Testing metrics**:
    - Percentage of code, requirements, and faults tested.
    - Percentage of tests passed in simulation environments versus physical testbeds.
    - Success rates of stress and integration tests.
  + Development milestones:
    - Number of software units at various stages of completion (e.g., coding completed, unit testing passed, integration tested).
  + Defect tracking: Number of major or critical defects identified during system testing phases.
* Leverage these metrics to assess the **adequacy of verification activities**. Tie progress monitoring to project risk management processes to anticipate and mitigate challenges early in the lifecycle.

---

#### **5. Key Takeaways to Enhance Measurement Program Planning**

**Integrate Lessons Learned**: Incorporating these lessons into your measurement program ensures:

1. **Alignment with organizational goals**: Collaborate with stakeholders to ensure chosen metrics support both project and institutional requirements, such as cost estimation, safety assurance, and process improvement.
2. **Tailored metrics**: Metrics must be customized to align with the project’s scope, technology maturity, and anticipated risks. A small number of meaningful measures often delivers more value than an exhaustive, comprehensive set of metrics.
3. **Proactive risk management**: Effective metrics allow early identification and resolution of risks across cost, schedule, quality, and safety dimensions.

**Emphasize Continuous Improvement**:

* Use the insights from lessons learned to guide post-project reflection. For example, ask:
  + Were the selected metrics sufficient to detect risks early?
  + Did the measures guide decisions that led to the successful delivery of high-quality products?
  + What additional metrics or refinements are needed for future projects?
* Refine measurement processes based on documented past challenges to improve efficiency and effectiveness in subsequent projects.

---

### 6. **Poor Metrics and Lack of Visibility into Software Health**

**Incident:**  
Psyche’s project metrics masked true software progress. Software risk was consistently under‑reported due to an aversion to categorizing issues as “red,” preventing leadership from recognizing schedule‑threatening problems.

**Lesson Learned:**

* **Objective Software Metrics:** Software maturity must be tracked using measurable indicators such as defect trends, verification progress, and test coverage.
* **Risk Transparency:** Leadership must encourage open reporting and avoid cultural pressures that suppress accurate risk assessments.

**Implication:**  
When metrics fail to reflect reality, management loses the ability to make timely decisions, creating preventable launch‑critical failures.

### Conclusion

The NASA Lesson Learned Database provides a rich resource for planning effective software measurement programs. By adopting and adapting these lessons, projects can improve visibility, reduce risks, and ensure that measurement programs deliver meaningful and actionable insights. Whether tracking costs, evaluating progress, or assessing safety and quality, measurement programs that incorporate these lessons will foster improved processes, higher-quality products, and greater overall project success.

### 6.2 Other Lessons Learned

* Much of NASA's software development experience that was accomplished in the NASA/GSFC Software Engineering Laboratory (SEL) is captured in "Lessons learned from 25 years of process improvement: The Rise and Fall of the NASA Software Engineering Laboratory"[430](#_tabs-<p></p>). The document describes numerous lessons learned that apply to the Agency's software development activities. From their early studies, they were able to build models of the environment and develop profiles for their organization. One of the key lessons in the document is "Lesson 6: The accuracy of the measurement data will always be suspect, but you have to learn to live with it and understand its limitations."

# 7. Software Assurance

**SWE-090 - Management and Technical Measurements**

5.4.2 The project manager shall establish, record, maintain, report, and utilize software management and technical measurements.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that a measurement program establishes, records, maintains, reports, and uses software assurance, management, and technical measures. 

2. Perform trending analyses on metrics (quality metrics, defect metrics) and report. 

3. Collect any identified organizational metrics and submit them to the organizational repository.

## 7.2 Software Assurance Products

The **Software Assurance (SA) products** play a critical role in meeting the requirements of a measurement program and supporting project success. These products are developed to ensure that the project lifecycle adheres to applicable quality standards, safety requirements, and process controls. They provide insight into the project’s health, identify risks early, confirm compliance, and assist in decision-making.

Key Software Assurance products may include but are not limited to:

* **SA Evaluation Reports**: Comprehensive reports capturing the results of software assurance activities, including verification of compliance with requirements, processes, and standards.
* **Audit and Assessment Reports**: Results from process and product audits, identifying gaps, risks, and areas of non-compliance, along with recommended corrective actions.
* **Anomaly and Defect Analysis Reports**: Identifications and analyses of defects or anomalies discovered during development, tracking their resolution, and evaluating the root causes to prevent recurrence.
* **Risk Management Inputs**: Contributions to project risk management, including identifying risks associated with software metrics data, verification/validation results, or software processes.
* **Process Compliance Checklists**: Detailed checklists documenting adherence to planned processes, workflows, and standards.
* **Software Measurement Review Reports**: Evaluations of the measurement program and the metrics being collected, ensuring alignment with project goals and organizational objectives. These reports may include findings and recommendations for improvement.
* **Safety and Quality Assurance Evidence Artifacts**: Documentation supporting software safety and quality, such as hazard analysis inputs, safety-critical software assessments, and test coverage evidence.
* **Lessons Learned Contributions**: Inputs to the lessons learned repository that promote continuous organizational improvement and provide guidance for future projects.
* **SA Status Updates for Milestone Reviews**: Contributions to key milestone reviews, including Preliminary Design Review (PDR), Critical Design Review (CDR), and Software Acceptance Review (SAR), providing data-backed assurance that the project is on track.

These products form the backbone of software assurance by not only ensuring compliance but also enabling proactive identification and mitigation of risks across the software lifecycle.

## 7.3 Metrics for Software Assurance

Effective metrics are essential for assessing the success, progress, and quality of software assurance activities. While each project must tailor its metrics based on its unique information needs, selecting relevant and meaningful metrics ensures that the data collected provides actionable insights. Metrics must align with project goals, organizational objectives, and risk management priorities.

#### Key Considerations for SA Metrics:

* **Tailored Metric Selection**: Each project selects a specific set of metrics that address critical project pain points, risks, and improvement areas. Consider factors such as software criticality, complexity, resources, and customer expectations.
* **Traceability to Objectives**: Metrics must tie directly to SA requirements, ensuring alignment with overall project and organizational goals (e.g., defect reduction, process adherence, and quality assurance).
* **Balanced Coverage**: Choose metrics that balance technical and management perspectives (e.g., quality metrics, schedule tracking, defect resolution, and process adherence) to provide a holistic view of software assurance effectiveness.

Common categories of software assurance metrics include:

* **Process Metrics**:

  + Number of process audits conducted and the percentage of nonconformities resolved.
  + Number of completed process compliance checklists versus planned.
  + Percentage of processes with updated and validated procedures.
* **Defect and Quality Metrics**:

  + Defect density (defects per size unit, e.g., per KLOC or function point).
  + Number of defects related to safety-critical concerns.
  + Average time to resolve Anomalies, Changes, and Problem Reports (ACPRs).
* **Verification and Validation Metrics**:

  + Percentage of test cases designed, executed, and passed.
  + Percentage of requirements verified and validated.
  + Defect detection effectiveness (defects found during testing vs. post-deployment).
* **Risk Management Metrics**:

  + Percentage of software assurance risks identified and mitigated.
  + Number of residual high-severity risks remaining at key milestones.
* **Safety and Security Metrics**:

  + Percentage of safety-critical software items analyzed and assured.
  + Number of unresolved security vulnerabilities reported in software.

For additional guidance on selecting and implementing software assurance metrics, refer to **SWE Handbook Topic 8.18 - SA Suggested Metrics**, which provides a comprehensive list of potential SA metrics that can be adapted to fit project-specific needs.

Summary

Both **Software Assurance Products** and **Metrics** provide the foundation for reliable oversight, informed decision-making, and continuous improvement in software projects. By tailoring assurance products and metrics to individual project and organizational contexts, teams can maximize the value of SA outcomes while maintaining compliance, quality, and risk management priorities at every stage of the software lifecycle.

## 7.4 Guidance

This requirement—requiring a project manager to establish, record, maintain, report, and utilize software management and technical measurements—provides the foundation for effective project monitoring, control, and improvement. Software assurance plays a critical role by ensuring that the measurement processes, data collection, reporting, and analysis are accurate, transparent, and aligned with both project and organizational objectives. Below is practical guidance for implementing effective software assurance practices for this requirement:

---

### **Purpose of Software Assurance in Measurement Programs**

Software assurance (SA) ensures that software management and technical measurements:

1. **Support Decision-Making**: Ensure project managers and stakeholders have accurate, relevant, and timely data for informed decision-making.
2. **Align with Objectives**: Verify that the selected metrics and measures align with project goals, customer requirements, risk management efforts, and organizational quality standards.
3. **Enforce Integrity**: Establish confidence in the integrity, accuracy, and consistency of collected data.
4. **Mitigate Risks**: Identify risks in the measurement program itself, such as incomplete data collection, misaligned metrics, or improper data handling and reporting.

---

### **Key Software Assurance Activities for Meeting Requirement 5.4.2**

#### **1. Verify Measurement Plan and Objectives**

* **Review the Software Development Plan (SDP):**
  + Confirm that objectives for measurements are clearly defined, linked to organizational and project goals, and include measurable outcomes (e.g., cost, schedule, quality, and risk indicators).
  + Assess whether planned measures cover critical areas such as defect density, requirements volatility, code quality, progress tracking, and resource utilization.
* **Check Tailoring for Specific Projects:**
  + Assure that the measurement plan is appropriately tailored to the project size, scope, risks, and lifecycle model.
  + Verify the alignment of objectives with programmatic, mission assurance, and safety-critical requirements.

#### **2. Confirm Accuracy and Reliability of Measurement Data**

* **Define Data Collection Standards:**
  + Review procedures for data collection and ensure they define standards for collecting, formatting, and maintaining consistency of measurement data.
  + Ensure clearly defined roles and responsibilities for data collection, with minimal ambiguity.
* **Validate Measurement Tools:**
  + Assure that tools used for automated data collection (e.g., JIRA, DOORS, SonarQube) are configured correctly, produce accurate results, and are calibrated to project needs.
  + Confirm alignment between intended data capture and tool capability.
* **Perform Data Integrity and Quality Checks:**
  + Ensure that data is free from errors, outliers, and duplication. Verify data completeness for each reporting interval to avoid misinterpretation of results.
  + Validate that the granularity of data aligns with its intended use (e.g., aggregated data for management reports, detailed datasets for technical evaluations).

#### **3. Assess and Track Metrics**

* **Evaluate Metric Relevance:**
  + Software assurance should periodically evaluate whether each selected metric remains relevant, actionable, and aligned with current project priorities.
  + Ensure a balance between quantitative (e.g., defect density trends) and qualitative measures (e.g., stakeholder satisfaction from reviews).
* **Track Metrics Over Time:**
  + Review trends in key metrics to identify anomalies, deviations, or emerging risks:
    - Is schedule performance slipping significantly from the baseline?
    - Are software defects increasing in severity or frequency during late development phases?
    - Is project resource usage aligned with planned versus actual allocations?
  + Use metrics to support proactive risk management and course correction.
* **Monitor Thresholds and Limits:**
  + Confirm that thresholds for acceptable, warning, and unacceptable metric values are established and adhered to. For example:
    - Define acceptable ranges for defect density in delivered code.
    - Flag early warning signals when resource utilization exceeds planned capacity.

#### **4. Assure Transparent Reporting**

* **Review Reporting Procedures:**
  + Verify that the procedures for reporting and presenting metric data are consistent, repeatable, and documented in project plans (e.g., SDP, Software Metrics Report).
  + Assure the frequency of reporting aligns with project needs—e.g., weekly for high-risk areas and broader metrics for milestone reviews.
* **Ensure Data Visualization:**
  + Confirm that metrics are displayed using clear, actionable formats such as dashboards, charts, trend graphs, and summary tables. Ensure appropriate levels of detail for each stakeholder group (e.g., developers, project managers, customers).
* **Support Timely Decision-Making:**
  + Encourage meaningful analysis focused on actionable insights to trigger decisions, such as:
    - Revising defective work products.
    - Imposing additional reviews on “at risk” areas.
    - Assigning additional resources in case of schedule slippage.

#### **5. Mitigate Risks in the Measurement Process**

* **Proactive Risk Identification**:
  + Assess risks directly related to the measurement program itself. For example:
    - Inconsistencies in definitions or measurements (e.g., different interpretations of “defect” across teams).
    - Overhead from excessive measurement collecting, leading to wasted time and resources.
    - Lack of stakeholder buy-in, reducing adherence to measurement processes.
* **Training and Awareness:**
  + Ensure all team members involved in collecting, maintaining, or interpreting measurement data are properly trained on tools, processes, and expectations.
  + Highlight the importance of accurate and timely data for overall project success.
* **Periodic Reviews of Metrics:**
  + Conduct software assurance reviews of the measurement program throughout the lifecycle, adjusting metrics as project needs evolve and ensuring their continued validity.

#### **6. Validate Usage of Measurement Data**

* **Support Decision-Making Processes:**
  + Confirm that measurement data is being used meaningfully to support project objectives, such as monitoring progress, assessing risks, and improving quality.
  + Ensure data is not merely being collected for compliance but is actively driving actionable outcomes.
* **Evaluate Measurement-Driven Improvements:**
  + Provide assurance checks to evaluate the success of improvement actions initiated based on metric data. For example:
    - Does defect trend analysis lead to targeted fixes and reduced defect rates over time?
    - Are corrective actions taken when resource or schedule metrics identify bottlenecks?

#### **7. Promote Process Improvement**

* **Foster Organizational Learning from Metrics:**
  + Monitor whether lessons learned from measurement reviews were documented and incorporated into **future projects** or **continuous improvement programs**.
  + Verify that metrics contribute to creating historical baselines that inform future forecasting and estimation efforts.
* **Benchmarking:**
  + Encourage comparisons of project metrics with organizational, industry, or historical benchmarks to identify process improvement opportunities.

---

### **Additional Considerations for Software Assurance**

* **Alignment with Standards**: Ensure the measurement program complies with NASA’s NPR 7150.2 and other relevant standards.
* **Small Projects**: For smaller-scale efforts, software assurance should confirm that a limited but meaningful set of metrics has been selected. Emphasize simplicity, automation, and adaptation to resource constraints.
* **Lifecycle Support**: Verify that metrics address all relevant project lifecycle stages, enabling end-to-end monitoring.
* **Tool Selection Oversight**: If automated tools are being used, verify their reliability, outputs, and compliance with planned measurement objectives.

---

### **Software Assurance Responsibilities Summary**

To ensure effective implementation of this requirement, software assurance must:

1. Review and approve measurement plans as part of the Software Development Plan and associated documents.
2. Monitor, validate, and report on the accuracy, consistency, and utility of measurement data.
3. Evaluate and mitigate risks to the measurement program itself.
4. Validate that metric results are actively used to make decisions, track progress, and improve project outcomes.
5. Advocate for lessons learned and continual refinements in the measurement process.

By rigorously adhering to these guidance principles, software assurance ensures that the software measurement program is not only compliant but also a powerful tool for managing software development success.

Organizational Goals of Software Assurance metrics:

| Goal Statements | Goal | Question | SA Metric |
| --- | --- | --- | --- |
| Assure delivery of quality software requirements to assure safe and secure products in support of mission success and customer objectives. | Quality Software   Requirements | Are the software requirements detailed enough for development and testing? | The ratio of the number of detailed software requirements to the number of SLOC to be developed by the project. |
| The percentage is complete for each area of traceability. |
| Are requirements stable? | Software requirements volatility trended after the project baseline (e.g., # of requirements added,   deleted, or modified; tbds). |
| Are the software hazards adequately addressed in the software requirements? | The percentage is complete of traceability to each hazard with software items. (New) |
| Assure delivery of quality, safe, and secure code. | Quality Code | Is the code secure and has the code addressed cybersecurity requirements? | Number of cybersecurity   secure coding violations per number of developed lines of code; |
| List of types of secure coding violations found. |
| Is the safety-critical code safe? | Software cyclomatic   complexity data for all identified safety-critical software components; |
| What is the quality of the code? | Number of defects or   issues found in the software after delivery; |
| The number of defects or non-conformances found in flight code, ground code, tools, and COTs products used. |
| Do the requirements adequately address cybersecurity? | Number and type of identified cybersecurity vulnerabilities and weaknesses found by the project. |
| Continuously improve the quality and adequacy of software testing to assure safe and reliable products and services are delivered. | Quality Software Testing | Does the test program provide adequate coverage? | Software Code Coverage   data; |
| Software requirements   test coverage percentages, including the percentage of testing completed and   the percentage of the detailed software requirements, successfully tested to   date; |
| Number of issues and   discrepancies found during each test; |
| The number of lines of code tested. |
| Does the software test program test all of the safety-critical code? | Test coverage data for all identified safety-critical software components. |
| Continuously monitor software projects to improve the management of Software Plans, Procedures, and   Defects to assure quality products and services are delivered on time and within budget. | Quality Software Plans,   Procedures, and Defect Tracking | Is the SW project proceeding as planned? | Compare initial cost   estimate and final actual cost, noting assumptions and differences in cost   parameters; |
| Is the SW project addressing identified problems? | The number of finding from process non-compliances and process maturity. |
| Is the SW project using peer reviews to increase product quality? | Number of peer reviews   performed vs. # planned; the number of defects found in each peer review; |
| How well is the project following its processes and procedures? | Number of audits findings   per audit; |
| The time required to close the audit findings; |
| Defect Tracking status and why the Defect occurred? | Problem/change report   status: total number, number closed, the number opened in the current   reporting period, age, severity; |
| Number of defects or   issues found in the software after delivery; |
| The number of defects or non-conformances found in flight code, ground code, tools, and COTs products used. |
| Number of software non-conformances at each severity level for each software configuration item. |
| The number of root cause analyses performed; list of finding identified by each root cause analysis. |
| The trend shows the closure of corrective actions over time. |
| Maintain and advance organizational capability in software assurance processes and practices to meet   NASA-STD-8739.8 requirements. | SA Process Improvements | Are SA findings providing valueto software development? | The number of SA findings (e.g., #   open, closed, latency, # accepted) mapped against SA activities, through the life cycle, including process non-compliances, and process maturity. |
| The number of defects found by software assurance during each peer review activity. |
| Is the SA effort proceeding as planned? | Trend the software assurance cost estimates through the project life cycle; |
| Planned SA resource allocation versus actual SA resource allocation. |
| Percent of the required training completed for each of the project SA personnel. |
| The number of compliance audits planned vs. the number of compliance audits completed and trends on non-conformances from the audits. |

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVB/pages/32604383/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVB/pages/32604385/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence provides tangible proof that a project has complied with Requirement 5.4.2, which focuses on establishing, recording, maintaining, reporting, and utilizing software management and technical measurements. The evidence demonstrates that measurement programs are properly implemented, accurately tracked, and effectively utilized to support both project and organizational goals. Below is a list of key objective evidence that may be required for software assurance and verification purposes:

---

### **1. Planning Evidence**

* **Software Measurement Plan**:

  + A documented plan within the Software Development Plan (SDP) or a separate measurement planning document that defines:
    - The specific objectives for software management and technical measurements.
    - The selected set of metrics aligned to those objectives.
    - The procedures, tools, and frequency used to collect, maintain, and report measurement data.
  + Includes tailoring decisions for specific project conditions, particularly in the case of small projects or safety-critical missions.
* **Metric Selection Justification**:

  + Evidence explaining why specific metrics were chosen, their alignment with project goals, and their value in tracking risks, progress, quality, and performance.
* **Defined Baselines**:

  + Documentation that establishes initial baselines for measures such as schedule performance (e.g., planned vs. actual), cost estimation, requirements volatility, defect density, and other key metrics.
* **Tools Implementation Evidence**:

  + Documentation showing that tools for tracking and storing measurements (e.g., JIRA, DOORS, Excel-based templates) have been appropriately configured, tested, and deployed.

---

### **2. Implementation Evidence**

* **Data Collection Logs**:

  + Logs or automated reports from tools (e.g., JIRA, SonarQube, Git, configuration management systems) showing consistent collection of measurement data according to the project’s defined procedures and frequency.
* **Raw Metric Data**:

  + Objective, unprocessed data or snapshots, such as:
    - Defect logs with severity classification and resolution details.
    - Requirement change logs, showing added, modified, or deleted requirements during various lifecycle phases.
    - Code complexity reports (e.g., cyclomatic complexity metrics from static analysis tools).
    - Test case execution data (e.g., number of executed tests, pass/fail status, associated defects).
* **Audit and Inspection Records**:

  + Results of software assurance reviews, inspections, or audits that validate the accuracy and completeness of measurement processes and ensure compliance with the defined measurement plan.

---

### **3. Reporting Evidence**

* **Measurement Reports**:

  + Completed periodic reports (e.g., weekly, monthly, quarterly) summarizing collected metrics and analyzing trends related to project objectives such as schedule adherence, defect rates, resource usage, and requirements changes.
  + Includes graphical or tabular representations (e.g., charts, dashboards, heatmaps) for better interpretation of the data by stakeholders.
* **Milestone Review Data**:

  + Measurement data presented at key project milestones, such as Preliminary Design Reviews (PDRs), Critical Design Reviews (CDRs), and Software Acceptance Reviews (SARs), to demonstrate compliance with project goals and ensure the project is on track.
* **Risk and Decision Records**:

  + Documentation linking metric data to project decisions, showing how measurement trends influenced actions such as resource adjustments, schedule modifications, or defect-resolution prioritization.

---

### **4. Analysis and Utilization Evidence**

* **Trend Analysis Reports**:

  + Evidence of analysis performed to identify trends, risks, or patterns in the collected data, such as:
    - Increasing defect densities that may signify quality issues.
    - Escalating requirements volatility potentially impacting schedule or budget.
    - Coverage gaps in testing metrics.
    - Variances in resource utilization or performance baselines.
* **Corrective Actions**:

  + Records showing actions taken to address issues identified by metrics, such as:
    - Adjusting project workflows to reduce defect introduction.
    - Adding resources or extending deadlines due to inadequate progress.
    - Revising risk mitigation plans to address critical problem areas identified by measurement analysis.
* **Lessons Learned Contributions**:

  + Evidence demonstrating how collected metrics and their outcomes were used to inform lessons learned or process improvements for current or future projects.

---

### **5. Verification and Validation Evidence**

* **Verification Checklists**:

  + Completed checklists or forms verifying that the defined measures were fully implemented, data was measured consistently, and reporting aligns with the approved measurement plan.
* **Tool Validation Evidence**:

  + Records demonstrating that tools used for data collection and reporting were validated to confirm they are producing accurate, repeatable, and reliable data.
* **SA Reviews and Sign-offs**:

  + Review documentation from software assurance teams verifying that:
    - Measurement processes are in compliance with applicable standards (e.g., NASA-STD-8739.8, NPR 7150.2).
    - Metrics align with the project’s defined goals and objectives.
    - Data collection and analysis are accurate, timely, and complete.

---

### **6. Closeout Evidence**

* **Final Project Metric Summary Report**:

  + A final summary of all key metrics at the end of the project lifecycle, showing how metrics trended over time, whether project goals were met, and documenting lessons learned.
* **Historical Data Archive**:

  + Repository of all raw and processed measurement data stored for future reference (e.g., for cost estimation, process improvement, or similar mission planning).
* **Process Refinement Recommendations**:

  + Recommendations or after-action reviews identifying any gaps in the current measurement program and proposing updates to improve future metrics collection, monitoring, and utilization.

---

### **Examples of Key Metrics and Associated Evidence**

Below are examples of metrics commonly used to provide objective evidence, including potential artifacts supporting compliance with these metrics:

| **Metric** | **Objective Evidence** |
| --- | --- |
| Defect Density | Defect logs, severity classifications, resolution times, defect trend reports |
| Requirements Volatility | Change logs, updated requirements traceability matrices, justification records for added/removed/modified requirements |
| Test Coverage | Test case reports, percent coverage documentation, reports from automated tools (e.g., code coverage reports) |
| Schedule Adherence | Earned Value Reports, milestone tracking dashboards, Gantt charts, status updates |
| Resource Utilization | Staffing reports, budget usage summaries, task allocation records |
| Compliance Metrics | Process audit reports, conformance checklists, SA review checklists |

---

### Summary

Objective evidence for Requirement 5.4.2 ensures transparency, accountability, and compliance in software measurement programs. These deliverables—ranging from planning artifacts like the Software Measurement Plan to implementation data such as defect logs, and final closeout reports—demonstrate that metrics are more than just numbers: they are actionable tools for managing progress, identifying risks, and driving improvements across the software development lifecycle.

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
