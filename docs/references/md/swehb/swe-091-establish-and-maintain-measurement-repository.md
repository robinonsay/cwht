# SWE-091 - Establish and Maintain Measurement Repository

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695477. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository

SWE-091 - Establish and Maintain Measurement Repository

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695477)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695477&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)

# 1. Requirements

2.1.5.7 For Class A, B, and C software projects, the Center Director, or designee, shall establish and maintain a software measurement repository for software project measurements containing at a minimum: 

a. Software development tracking data.  
b. Software functionality achieved data.  
c. Software quality data.  
d. Software development effort and cost data.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-091 History

SWE-091 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.4.2 The project shall select and record the selection of specific measures in the following areas:   1. 1. Software progress tracking.    2. Software functionality.    3. Software quality.    4. Software requirements volatility.    5. Software characteristics |
| Difference between A and B | Made the requirement based on software Class and Safety Criticality; Added requirement to establish metrics repository / system from Rev A SWE-095. Removed requirement for requirements volatility and software characteristics; Added development effort and cost data to list of measures. |
| B | 2.1.3.9 For Class A, B, C, and safety-critical software projects, the Center Director shall establish and maintain a software measurement repository for software project measurements containing at a minimum:   1. 1. Software development tracking data.    2. Software functionality achieved data.    3. Software quality data.    4. Software development effort and cost data. |
| Difference between B and C | Removed "safety-critical" from the requirement. |
| C | 2.1.5.9 For Class A, B, and C software projects, the Center Director, or designee, shall establish and maintain a software measurement repository for software project measurements containing at a minimum:   1. 1. Software development tracking data.    2. Software functionality achieved data.    3. Software quality data.    4. Software development effort and cost data. |
| Difference between C and D | No Change |
| D | 2.1.5.7 For Class A, B, and C software projects, the Center Director, or designee, shall establish and maintain a software measurement repository for software project measurements containing at a minimum:   a. Software development tracking data. b. Software functionality achieved data. c. Software quality data. d. Software development effort and cost data. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.11 Software Measurements](/spaces/SWEHBVD/pages/133235387/A.11+Software+Measurements) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

Software measurement programs play a critical role in achieving objectives and goals across multiple levels, from project management and safety assurance to quality improvement and process refinement. The data collected from these measurement programs provides valuable insights that inform decision-making, enhance performance, and ensure alignment with mission-critical requirements. To enable effective use of this data, software measurement repositories serve as centralized systems for collecting, storing, analyzing, and reporting measurement data, tailored to the specific needs of the Center and its projects.

## 2.1 Key Rationale for the Requirement

### 1. Facilitates Effective Project Management

Software measurement repositories provide essential data that helps project managers track progress, identify risks, and take corrective actions. By storing and analyzing key metrics—such as software development effort, functionality achieved, quality indicators, and cost—Centers can:

* **Monitor Software Project Status:** Gain real-time visibility into project milestones and detect deviations from planned objectives.
* **Optimize Resource Allocation:** Use measurement data to ensure efficient distribution of funding, effort, and personnel across software initiatives.
* **Support Strategic Decision-Making:** Enable informed decisions based on performance trends and risk indicators tied to safety-critical systems and high-priority software projects.

### 2. Enhances Safety and Quality Assurance

Measurement repositories play a key role in guaranteeing the safety and quality of software systems, especially for mission-critical and safety-critical applications:

* **Safety Assurance:** By providing metrics linked to defect counts, failure rates, and other reliability factors, repositories ensure that hazards are proactively flagged and safety-critical software systems are rigorously tested.
* **Quality Monitoring:** Tracking quality data (e.g., fault density, defect removal efficiency) supports continuous improvement efforts and ensures the software meets high standards of reliability and functionality, particularly for human-rated and Class A systems.

### 3. Improves Software Engineering Practices

The establishment of repositories enables Centers to analyze and refine their software engineering processes based on historical and current data:

* **Process Improvement Opportunities:** Measurement data allows Centers to identify bottlenecks, inefficiencies, and recurring issues in software development processes for targeted improvements.
* **Lessons Learned:** The ability to analyze prior project performance data fosters institutional learning across all Centers, enabling cross-project knowledge-sharing and refinement of best practices.
* **Performance Benchmarking:** Measurement repositories allow Centers to benchmark their engineering practices against historical data or industry standards to achieve continuous growth and excellence.

### **4. Promotes Center-Wide Assessments**

Software measurement systems empower Centers to assess their current software engineering capabilities and the competencies of their workforce and providers:

* **Workforce Skill Analysis:** Insight gained from measurement repositories helps identify strengths and weaknesses across engineering teams, enabling training and development opportunities to address gaps.
* **Provider Capability Assessment:** For projects involving external contractors or vendors, measurement data helps evaluate their performance, ensuring accountability and reliability for future work.
* **Comprehensive Status Reports:** Centers can leverage measurement repositories to generate detailed reports on current software project status, risks, and trends, facilitating periodic Center-wide reviews and audits.

### 5. Supports Future Planning and Resource Allocation

Software repositories provide longitudinal data that helps Centers assess trends, establish cost baselines, and plan for future software initiatives:

* **Predictive Analysis:** By using historical measurements, Centers can make more accurate predictions about future software timelines, costs, and resource needs.
* **Proactive Resource Planning:** Measurement data enables Centers to allocate resources effectively based on past project experiences, avoiding under- or over-investment for new initiatives.

### 6. Enables Center-Wide and Agency-Wide Collaboration

Once measurement systems are established, Centers can conduct analyses that enable collaboration within the Center and across Agency-wide programs:

* **Cross-Center Data Insights:** Shared access to data allows Centers to learn from successful practices of others.
* **Standardized Metrics:** A repository supports the harmonization of measurement terminology and practices across NASA Centers, ensuring consistent evaluation criteria.
* **Enhances Accountability:** Measurement repositories promote data-driven decision-making, helping align local practices with Agency-wide expectations for software tracking and reporting.

## 2.2 Conclusion

A software measurement repository is an essential tool for NASA Centers, enabling leadership to track progress, ensure safety and quality, improve software engineering practices, and optimize workforce capabilities. When effectively implemented and maintained, repositories transform raw metrics into actionable insights, supporting Center-wide and Agency-wide objectives like mission assurance, cost efficiency, and organizational improvement. By establishing robust software measurement systems, NASA Centers ensure the successful execution of software initiatives on the cutting edge of safety, reliability, and engineering excellence.

# 3. Guidance

To ensure consistency, reliability, and actionable insights across software measurement programs, software organizations are expected to collect and manage metrics through a standardized approach. This guidance outlines key best practices for the establishment, data collection, and maintenance of software measurement repositories, as well as the goals and activities they support at Center and organization levels.

## 3.1 Purpose and Role of Measurement Repositories

Software measurement repositories serve as centralized systems for collecting, storing, analyzing, and reporting software project metrics. These repositories enable effective management of projects, enhance safety and quality assurance processes, and drive overall improvements in software engineering practices. Repositories are essential for:

* Long-term access to historical and current project measurement data.
* Supporting trending assessments, predictive analyses, and benchmarking activities.
* Providing insight into the status and capabilities of ongoing and future software initiatives.

Measurement repositories can be established at:

* **Center-Level:** For overarching Center-wide evaluations.
* **Organizational/Project-Level:** For program-specific insights and tailored assessments.

Each Center must determine the repository structure and location that best supports its unique needs and software development environment.

## 3.2. Relationship to Related Topics

Related guidance and frameworks that support measurement repositories include:

* Topic[7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects)
* Topic [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)**:** Planning measurements in the Software Development and Management Plan (SDP/SMP).

## 3.3. Measurement System Goals

The software measurement systems established at the Center level are designed to meet the following high-level objectives:

* **Improved Planning and Cost Estimation:** Use historical data to inform realistic schedules, resource allocation, and budget estimates.
* **Realistic Data for Progress Tracking:** Enable tracking of milestones and deliverables while providing insights into project performance compared to plans.
* **Software Quality Indicators:** Provide metrics to evaluate software reliability, identify risks, and ensure compliance with quality standards.
* **Baseline Data for Process Improvement:** Use metrics to identify inefficiencies, plan corrective actions, and improve software engineering practices for future projects.

## 3.4. Establishing a Measurement Repository

A software measurement repository should include data that meets minimum reporting requirements across key measurement categories for effective analysis and trend discovery. These categories are described below:

### 3.4.1 Software Development Tracking Data

This data tracks progress throughout the lifecycle and includes the planned vs. actual values for essential metrics such as:

* Resource allocation and utilization.
* Development and implementation schedules.
* Testing and validation status.

Tracking through a formal process, such as the **Software Metrics Report** (see Topic [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report)), ensures consistent reporting and monitoring of development metrics.

### 3.4.2 Software Functionality Achieved Data

This data monitors achieved functionality versus planned functionality, which includes:

* Requirements implemented versus total requirements planned.
* Functional points achieved within the system (for feature-level tracking).
* Utilization of computational resources for efficiency monitoring.

Ensure this data is included in the **Software Metrics Report** for function-point-level visibility and performance validation.

### 3.4.3 Software Quality Data

Software quality metrics enable evaluations of product reliability and defect rates. This data includes:

* Problem reports, change requests, and defect statistics.
* Results from peer reviews, inspections, audits, and risk mitigations.
* Discrepancies and actions tracked throughout the software lifecycle.

Including quality metrics in periodic analyses provides insight into code health, identifying areas that require increased focus during development and testing.

### 3.4.4 Software Development Effort and Cost Data

Effort and cost data support accurate progress monitoring and resource management. This includes:

* Metrics showing progress toward planned milestones, schedule adherence, and delays.
* Tool expenses, resource allocation, and costs associated with testing and verification facilities.
* Trending analyses showing resource utilization and areas of potential inefficiency.

Develop a methodology to include this data in project status reports or scheduling tools for easier integration into repository systems.

## 3.5. Measurement Collection Process

Measurement repositories depend on clearly defined, repeatable data collection processes designed to support accurate and consistent reporting across programs and projects:

### 3.5.1 Data Collection Framework

Each Center must establish a measurement collection plan that aligns with its specific requirements. This plan should include:

* **Data Description:** Provide a clear explanation of the metrics to be collected, including format, scope, and physical or electronic forms.
* **Term Definitions:** Create precise definitions for terms and criteria to standardize the collection process across projects.
* **Responsibilities:** Define roles and responsibilities for data provision, validation, analysis, and reporting.
* **Timeframes:** Set timelines for the reception and validation of data and any analyses derived from it.

## 3.6. Data Storage Processes

To ensure long-term usability and accessibility, repository data must follow structured storage protocols:

### 3.6.1 Validation and Verification (V&V):

Before data is stored in the repository, perform quality checks to ensure:

* Correct formats and completeness.
* Logical consistency, including avoidance of missing or repetitive entries.
* Adherence to expected value ranges based on predefined criteria.

### 3.6.2 Managing Analyses:

Repositories should identify which analyses are stored permanently and which intermediate results can be discarded (with options to reconstruct them later).

* Maintain a list of requested analyses from stakeholders.
* Incorporate metrics that reflect changes or advancements in the software development lifecycle.

### 3.6.3 Data Repository Identification and Access:

Clearly define:

* The location and management protocol for repository data storage.
* Database management systems (DBMS) that allow efficient repository access for cross-project and organizational objectives.

**Goal:** Ensure that multiple projects or teams can access the repository and use metrics to meet their specific objectives without compromising data integrity.

## 3.7. Metrics and Indicators

Metrics derived from the repository enable actionable insights into project performance:

* **Trend Indicators:** Metrics track trends over time, showing improvements, deterioration, or breaches of predefined limits (e.g., latent defect thresholds).
* **Management Metrics:** Metrics evaluate the success of development activities across projects, highlighting areas for process adjustment, troubleshooting, and progress forecasting.

Metrics should reflect well-defined quantitative indices to reliably evaluate software products, processes, or systems.

## 3.8. Benefits of Measurement Repositories

Measurement repositories provide critical insights and enable Centers to:

1. **Focus on Continuous Improvement:** Use metrics to identify weaknesses, refine processes, and establish best practices.
2. **Enhance Mission Assurance:** Track safety-critical metrics to reduce risk and enhance quality for mission-critical systems.
3. **Improve Resource Management:** Use cost-effort tracking data to allocate funding, personnel, and tools effectively.
4. **Support Decision-Making:** Provide leadership with actionable insights into project status, risks, and performance trends.
5. **Enable Knowledge Sharing:** Promote cross-Center collaboration by providing consistent, accessible metrics for benchmarking and analysis.

## 3.9 Conclusion

An effective software measurement repository is an invaluable tool for managing software projects, ensuring safety and quality, and driving process improvement across NASA Centers. By implementing structured data collection, validation, and storage frameworks, Centers can enable long-term access to actionable measurement data that enhances planning, resource management, and decision-making at both organizational and Agency-wide levels.

See also [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements), [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data), [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data), [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis).

## 3.10 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) |

## 3.11 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics)      * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

For small projects, where resources, complexity, or mission criticality may be limited, the software measurement repository requirement can be tailored to ensure effective compliance without creating unnecessary burden. Small projects should still benefit from measurement data to monitor progress, ensure quality, and support process improvement, but the approach to data collection, storage, and analysis can be simplified. Below is guidance on how small projects can implement this requirement in a streamlined and practical manner.

## 4.1 Guidance for Small Projects

### 4.1.1  Overview of the Requirement

For projects classified as Class A, B, or C, Centers are required to establish and maintain a software measurement repository containing:

1. **Software development tracking data**
2. **Software functionality achieved data**
3. **Software quality data**
4. **Software development effort and cost data**

Small projects may reduce the scope of this requirement while maintaining key measurement activities that align with the project’s complexity, size, classification, and Center needs.

### 4.1.2  Tailoring the Software Measurement Repository for Small Projects

Small projects often involve fewer people, smaller codebases, simpler designs, and relatively short lifecycles. As such, small projects can implement the measurement repository requirement using a lightweight approach that leverages existing tools and focuses on simplicity and efficiency.

#### **Key Tailoring Principles for Small Projects**

* **Streamline Data Collection:** Limit the number of metrics collected to those critical for tracking progress, ensuring quality, and meeting project objectives.
* **Leverage Existing Tools:** Use accessible tools such as spreadsheets, simple web-based repositories, or lightweight databases to store and analyze measurement data.
* **Simplify Reporting:** Focus on high-impact metrics that align with the project’s priorities, avoiding overly detailed or redundant reporting.
* **Emphasize Scalability:** As the complexity or scope of the small project increases, the measurement practices can expand to include additional metrics or more advanced reporting mechanisms.

### 4.1.3  Simplified Measurement Repository Implementation for Small Projects

Below is guidance on how small projects can implement each category of the software measurement repository:

#### 4.1.3.1 Software Development Tracking Data

* **Purpose:** Monitor project progress, milestones, and resource usage.
* **Simplified Approach for Small Projects:**
  + Collect planned vs. actual schedule data at key milestones, such as start and completion of major design, development, testing, and deployment phases.
  + Use simple tracking methods such as Gantt charts, Kanban boards, or task management tools (e.g., Jira, Trello, Excel).
  + Track and report major changes to schedules, scope, or dependencies.
  + Maintain periodic updates (e.g., weekly or biweekly) based on the project's cadence.

#### 4.1.3.2  Software Functionality Achieved Data

* **Purpose:** Track progress in delivering software features or requirements.
* **Simplified Approach for Small Projects:**
  + Focus on planned vs. delivered functionality based on high-priority requirements, such as user stories, acceptance criteria, or system-level requirements.
  + Use metrics such as:
    - Number of baseline requirements delivered versus planned.
    - Simple counts of implemented features or function points.
    - Resource utilization data, such as CPU, memory, or storage efficiency.
  + Report this data at a minimum by major project milestones (e.g., after prototyping, development, and testing).

#### 4.1.3.3  Software Quality Data

* **Purpose:** Ensure that the developed software meets quality standards and is free of critical defects.
* **Simplified Approach for Small Projects:**
  + Focus on key quality metrics that give an indication of software health. Examples:
    - Number of open vs. closed problem reports or defects.
    - Peer review or inspection outcomes (e.g., defect density in inspected code).
    - Results from testing phases (e.g., number of test cases passed vs. failed, code coverage for critical functions).
  + Collect only essential data such as significant test failures, high-priority defects, and major risks.
  + Use readily available tools like Excel, Google Sheets, or lightweight defect tracking tools (e.g., Bugzilla, GitHub Issues).

#### 4.1.3.4  Software Development Effort and Cost Data

* **Purpose:** Track how resources (personnel, time, and budget) are used during the software lifecycle.
* **Simplified Approach for Small Projects:**
  + Focus only on broad-level effort data, such as:
    - Total person-hours per lifecycle phase (e.g., high-level effort breakdown for design, coding, testing).
    - A simplified budget view with actual vs. planned cost for major milestones.
  + Use high-level tools for time tracking (e.g., project time logs or reports from contract management systems).
  + Instead of detailed cost tracking, rely on estimated figures for smaller phases or weekly reporting.

### 4.1.4  Common Tools for Small Projects

Small projects can implement measurement repositories using accessible and lightweight tools:

* **Data Collection and Tracking:**
  + Google Sheets, Microsoft Excel, or Airtable for manual tracking.
  + Trello, Notion, or Asana for task and milestone progress.
* **Metrics Reporting:**
  + Jira or GitHub Projects for issue tracking and progress visualization.
  + Free or low-cost defect management tools (e.g., Bugzilla, GitHub, Redmine).
* **Storage and Organization:**
  + Cloud storage (e.g., OneDrive, Google Drive) for centralized metric repositories.
  + Local databases or flat files for small-scale projects.

The tools selected should prioritize simplicity, familiarity, and accessibility for the project team.

### 4.1.5  Reporting and Documentation for Small Projects

* Minimize documentation overhead by focusing on essential reporting that highlights:
  + Status updates on progress in key metrics (e.g., schedule tracking, functional progress).
  + Summary-level quality data (e.g., major defect trends or critical test results).
  + Resource and cost trends, summarized in a weekly or milestone-based report.
* Use standard templates provided by the Center wherever possible to streamline reporting processes.

### 4.1.6  Coordination with the Center’s Measurement Repository

* Small projects should coordinate with the Center to submit minimal reporting data to the Center’s software measurement repository (if applicable).
* Submit key metrics (e.g., planned vs. actual progress, major milestones, defect counts) on a periodic basis aligned with review milestones (e.g., Software Requirements Review, Critical Design Review).
* Where Center-level repositories are not required, retain the small project’s data within its local repository for potential audits or future analysis.

### 4.1.7  Scaling Metrics for Small Projects

As a small project’s complexity or importance grows, its software measurement practices should scale accordingly:

* Include additional metrics over time, as warranted by project risks or needs (e.g., detailed defect analysis or advanced test coverage metrics).
* Transition from manual reporting to more automated tools as the project evolves.
* Periodically review whether additional tailoring is required to meet the Center’s or Agency's software measurement objectives.

### 4.1.8  Example Metrics for Small Projects

Here’s an example of the types of metrics a small project should focus on maintaining:

| Metric Category | Example Metric | Frequency |
| --- | --- | --- |
| Development Tracking Data | Planned vs. actual task completion dates | Reviewed biweekly |
| Functionality Achieved Data | Number of requirements implemented vs. planned | At major milestones |
| Software Quality Data | Number of critical defects introduced/resolved | Every test cycle |
| Development Effort & Cost Data | Total person-hours per lifecycle phase | At the end of each phase |

## 4.2 Conclusion

For small projects, implementing a software measurement repository does not need to be resource-intensive or overly complex. By focusing on essential metrics, leveraging simple tools, and reporting data at a high level, small projects can achieve compliance with the measurement repository requirements while ensuring effective project tracking, quality assurance, and resource management. This tailored approach ensures that smaller efforts remain lightweight while still providing sufficient visibility and accountability for reporting and decision-making.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

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
* (SWEREF-316) Software Metrics Selection Presentation: A tutorial prepared for NASA personnel by the NASA Software Working Group and the Fraunhofer Center for Empirical Software Engineering College Park, MD. Seaman, Carolyn (2005) This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
  Retrieved on February 27, 2012 from https://nen.nasa.gov/web/software/nasa-software-process-asset-library-pal?.
* (SWEREF-329)

  [Software Measurement Guidebook,](https://ntrs.nasa.gov/search.jsp?R=19980228474 "Click to open in new window")

  Technical Report - NASA-GB-001-94 - Doc ID: 19980228474 (Acquired Nov 14, 1998), Software Engineering Program,
* (SWEREF-336)

  [Software Metrics Capability Evaluation Guide,](http://www.dtic.mil/docs/citations/ADA325385 "Click to open in new window")

  Software Technology Support Center (STSC) (1995), Hill Air Force Base. Accessed 6/25/2019.
* (SWEREF-355)

  [12 Steps to Useful Software Metrics,](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics_in_12_steps_paper.pdf "Click to open in new window")

  Westfall, Linda, The Westfall Team (2005),   Retrieved November 3, 2014 from http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics\_in\_12\_steps\_paper.pdf
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.
* (SWEREF-572)

  [Flight Software Engineering Lessons](https://llis.nasa.gov/lesson/2218 "Click to open in new window")

  Public Lessons Learned Entry: 2218.
* (SWEREF-577)

  [Selection and use of Software Metrics for Software Development Projects](https://llis.nasa.gov/lesson/3556 "Click to open in new window")

  Public Lessons Learned Entry: 3556.
* (SWEREF-683)

  [Anomalous Flight Conditions May Trigger Common-Mode Failures in Highly Redundant Systems](http://llis.nasa.gov/lesson/1778 "Click to open in new window")

  Public Lessons Learned Entry: 1778, Date: 2007-03-6. Submitting Organization: JPL, Submitted by: Martin Ratliff

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The establishment and maintenance of a software measurement repository as required for Class A, B, and C software projects is strongly supported by lessons learned in previous NASA initiatives. The following lessons from the NASA **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** highlight the importance of proper measurement selection, tracking, and analysis in software development projects. These lessons underscore the critical role of software metrics in managing project performance, detecting risks, improving quality, and ensuring mission success.

### 6.1.1  Relevant NASA Lessons Learned

#### 1. Selection and Use of Software Metrics for Software Development Projects [577](#_tabs-<p></p>)

* **Lesson Number: 3556**
* **Context:** This lesson comes from the Launch Processing System (LPS) application software for the Space Shuttle Program, where software metrics enabled better project visibility throughout the software lifecycle.
* **Key Takeaways and Recommendations:**
  1. **Early Selection of Tailored Metrics:** During the planning stages, it is essential to define metrics that are specific to the unique characteristics of the software project. This ensures that only meaningful metrics are collected, avoiding unnecessary overhead.
     + Example metrics include the number of requirement changes, errors during validation, delivered software defects, and projected versus actual labor hours or lines of code.
  2. **Efficiency Gains Through Metrics:** Metrics should only be collected if they provide actionable insights that lead to project efficiencies, such as enhanced schedule tracking, defect reduction, or improved resource allocation.
  3. **Measurement for Risk Identification:** Metrics enable early identification of risks or challenges in the project lifecycle, allowing teams to take corrective actions before they escalate into larger issues.
* **Relevance to the Requirement:**
  + This lesson reinforces the need for a tailored measurement repository that includes only useful metrics aligned with project needs.
  + Metrics stored in the repository, such as defect counts, requirement changes, and progress tracking (planned vs. actual), are directly aligned with the recommendations from this lesson.
  + Early metric selection and ongoing visibility into the “health” of the software project improve the overall efficacy of the repository.

#### 2. Flight Software Engineering Lessons [572](#_tabs-<p></p>)

* **Lesson Number: 2218**
* **Context:** The engineering of flight software (FSW) at NASA’s Jet Propulsion Laboratory (JPL) proved to be a major driver of cost and schedule due to the substantial amount of new software required for unique mission functionality.
* **Key Takeaways and Recommendations:**
  1. **Objective Measures to Monitor Progress:** Regularly track progress and assess adequacy of software development. Useful metrics include:
     + Percentage of requirements verified.
     + Percentage of code completed and tested in simulated and testbed environments.
     + Percentage of unit tests passed.
     + Number of stress tests completed.
  2. **Verification and Validation (V&V) Metrics:** Collect and analyze metrics to confirm that all requirements are adequately coded, tested, and validated against mission needs.
  3. **Early Detection of Defects:** By quantifying metrics such as testing progress and fault coverage, the project can identify and mitigate software defects earlier in the lifecycle, reducing costs and delays later in development.
* **Relevance to the Requirement:**
  + Software measurement repositories should include metrics on testing progress, defect density, and validation coverage to detect defects early and ensure quality (software quality data and development tracking data).
  + The systematic use of software metrics for progress and quality monitoring aligns with the repository’s focus on enabling realistic tracking and data-driven project assessments.

#### 3. Mars Climate Orbiter Failure Due to Inadequate Testing and Measurement Oversight [529](#_tabs-<p></p>)

* **Lesson Number: 0938**
* **Context:** The Mars Climate Orbiter mission failure was caused by a unit conversion error in its software, which arose from a lack of adequate oversight and inconsistent measurement practices.
* **Key Takeaways and Recommendations:**
  1. **Ensure Critical Metrics are Tracked:** Measurement repositories should capture relevant measurements related to testing, such as unit-level validation results, system-level functional verification, and performance margins.
  2. **Integration of Third-Party and Contractor Metrics:** Ensure that all development organizations (internal or external) report their progress using an agreed-upon set of metrics. These metrics should be stored in a centralized repository to ensure consistency and completeness.
* **Relevance to the Requirement:**
  + Storing software quality data (e.g., identification of discrepancies during validation and defects during testing) in a central repository would have mitigated the Mars Climate Orbiter’s error.
  + Small projects or contractor-led projects can use the repository as a shared location for tracking metrics consistently across teams and phases.

#### 4. Mars Polar Lander (MPL) Mission Failure [683](#_tabs-<p></p>)

* **Lesson Number: 1778**
* **Context:** The failure of the Mars Polar Lander was partially attributed to poorly tested software and incomplete tracking of verification and validation (V&V) metrics.
* **Key Takeaways and Recommendations:**
  1. **Establish Baselines for Testing Metrics:** Metrics such as the number of anomalous results during testing, fault coverage, and testing completion percentages should be used to track V&V adequacy and ensure that critical test cases are never skipped.
  2. **Real-Time Metrics Reporting:** Data from V&V activities should be regularly stored and analyzed for trends that might indicate potential failures or issues before launch.
* **Relevance to the Requirement:**
  + By maintaining a formal repository of software testing metrics, Centers can ensure that mission-critical functions are adequately validated and tracked at each stage of development.
  + Metrics such as the number of test cases executed, passed, and failed can provide an objective indication of software readiness before deployment.

#### 5. Software Quality Oversight on Space Shuttle Block II Engine Controller

* **Lesson Number: 2686**
* **Context:** The development of flight software for the Space Shuttle Block II Engine Controller revealed gaps in quality oversight due to insufficient tracking of metrics associated with development progress and software risks.
* **Key Takeaways and Recommendations:**
  1. **Link Metrics to Risk Mitigation:** Measurement repositories should track and report risks identified during different development phases and whether they have been mitigated.
  2. **Quality Metrics as Decision Support Tools:** Software quality should be assessed using metrics such as defect density, percentage of resolved risks, and assurance reviews.
* **Relevance to the Requirement:**
  + Repositories must include risk-related metrics and data on software defects to ensure that risks are effectively identified and mitigated.
  + Metrics enable improved oversight of mission-critical components and provide insight into areas needing additional testing or review.

#### 6. International Space Station (ISS) Joint Integrated Simulation Challenges

* **Key Insight:** The ISS program faced challenges in integrating software systems due to inconsistencies in tracking and reporting functionality and test coverage.
* **Key Takeaways and Recommendations:**
  1. **Functional Testing Metrics:** Track planned vs. achieved functionality, with emphasis on dependencies between subsystems.
  2. **Record Integration Progress:** Report metrics such as the number of interfaces tested, system compatibility measures, and integration test successes vs. failures.
* **Relevance to the Requirement:**
  + By including integration-focused metrics in the repository, projects can better coordinate and track system-level functionality achievements, especially in multi-subsystem contexts.

### 6.1.2  Conclusion

The lessons from NASA’s history underscore the value of implementing a robust software measurement repository to track progress, assess quality, detect risks, and support data-driven decision-making. Including metrics on testing, validation, progress tracking, functionality, and risks directly addresses the challenges faced in past NASA projects, ensuring a structured approach to quality and mission assurance. By tailoring metrics selection, collecting data early, and leveraging the repository as a collaborative tool, Centers can position themselves for greater project success.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-091 - Establish and Maintain Measurement Repository**

2.1.5.7 For Class A, B, and C software projects, the Center Director, or designee, shall establish and maintain a software measurement repository for software project measurements containing at a minimum:

a. Software development tracking data.  
b. Software functionality achieved data.  
c. Software quality data.  
d. Software development effort and cost data.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

None identified at this time.

## 7.2 Software Assurance Products

Software Assurance (SA) products are tangible outputs created by Software Assurance personnel to support oversight, validate compliance, manage risks, and ensure the quality of delivered products. These products are essential to demonstrate that SA objectives are being met, and they serve as evidence of the thoroughness and effectiveness of the assurance activities performed.

No specific deliverables are currently identified.

## 7.3 Metrics

No standard metrics are currently specified.

## 7.4 Guidance

### 7.4.1  Objective of the Guidance

The purpose of this requirement is to ensure that Centers maintain a centralized software measurement repository to capture and store essential software project data for Class A, B, and C software. This repository helps track progress, measure performance, analyze quality, provide cost-effort visibility, and identify trends across projects.

Software Assurance (SA) personnel play a critical role in verifying that the repository is correctly established, populated, and maintained, and that the data it contains is accurate and used to support software assurance objectives like risk assessment, compliance tracking, and process improvements.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Ensure the Establishment of the Software Measurement Repository

1. **Verify Repository Exists**:
   * Confirm with the Center Director or designee that a centralized and accessible software measurement repository has been established.
   * Ensure the repository can securely capture, store, and maintain software project measurement data in a reliable and organized manner.
2. **Review Repository Content Requirements**:
   * Verify that the repository is designed to support Class A, B, and C software projects and contains, at a minimum, the following categories of data:
     1. Software development tracking data.
     2. Software functionality achieved data.
     3. Software quality data.
     4. Software development effort and cost data.
3. **Evaluate Repository Accessibility**:
   * Ensure the repository is accessible to relevant stakeholders (e.g., software assurance personnel, project managers, and responsible engineers).
   * Confirm proper version control, security measures, and backup procedures are in place to avoid data loss or unauthorized access.

#### 7.4.2.2  Ensure Core Categories of Measurements Are Collected and Stored

##### (a) **Software Development Tracking Data**

SA personnel should verify that tracking data is collected and stored to provide insights into the project’s progress and ensure timeliness. Examples of data include:

* + Software schedules (planned vs. actual milestones, such as requirements reviews, design reviews, and test completions).
  + Task completion rates and adherence to baselined project timelines.
  + Metrics tracking rework or changes to software during development.

*SA Oversight*:

* + Confirm tracking data aligns with the project's software development plan.
  + Ensure progress metrics include earned value data or metrics, as applicable, for Class A, B, or C software.

##### (b) **Software Functionality Achieved Data**

Functionality achievement data confirms whether the software being developed meets its functional requirements over time. Examples of data include:

* + Functions delivered vs. planned at each milestone.
  + Status of planned capabilities still in progress (e.g., partially implemented or deferred).
  + Achievement metrics during testing phases (e.g., percentage of test cases passed or failed).

*SA Oversight*:

* + Verify functionality tracking includes a mapping to project requirements, showing adherence or alignment with approved requirements baselines.
  + Check that missed or deferred functionality is documented, with evidence of decision approval.

##### (c) **Software Quality Data**

Quality data tracks defects, errors, and related metrics to assess the performance and reliability of the software. Examples of data include:

* + Total defects, defect density, and types of defects (categorized by severity).
  + Mean time to failure (MTTF) for operational software.
  + Results from peer reviews, formal inspections, and testing activities.

*SA Oversight*:

* + Verify defect reports are documented in an artifact management tool and properly categorized (e.g., critical, high, medium, low severity).
  + Confirm that quality metrics trend analysis (e.g., identifying root causes of recurring issues) is used to inform process improvements.

##### (d) **Software Development Effort and Cost Data**

Effort and cost data enable the Center to analyze the resources expended on software development. Examples of data include:

* + Hours or effort by lifecycle activity (e.g., requirements, design, coding, testing).
  + Number of Full-Time Equivalent (FTE) personnel per project phase.
  + Software cost estimates vs. actual expenditures per milestone or phase.

*SA Oversight*:

* + Verify estimates align with work plans and track actual effort/cost accurately.
  + Check that cost overruns and their corrective actions are captured and tracked at an appropriate level of detail.

#### 7.4.2.3  Monitor Repository Utilization and Data Quality

1. **Perform Data Validations**:
   * Verify that all captured data in the repository is accurate, complete, and consistent with project reporting artifacts (e.g., schedules, test records, and cost reports).
   * Check for missing or outdated measurement data that could inhibit assessment or reporting accuracy.
2. **Support Regular Updates**:
   * Confirm that the repository is updated consistently (e.g., at project milestones or on a defined schedule) and reflects the most current project measurement data.
3. **Audit Repository and Processes**:
   * Include verification of the repository in routine SA audits to ensure it provides useful, traceable, and compliant data.
4. **Report on Data Trends and Effectiveness**:
   * Use repository data to monitor trends like defect reduction, process efficiency improvements, or adherence to project schedules.
   * Identify gaps in meeting performance or assurance targets and suggest adjustments as needed.

#### 7.4.2.4  Use Repository Data to Support Software Assurance Activities

1. **Identify and Mitigate Risks**:
   * Leverage repository data to identify software project risks, such as:
     + Missed milestones or delayed functionality.
     + Trends in defect density that suggest diminishing quality.
     + Cost overruns indicating resource allocation challenges.
     + Ensure these risks are logged, tracked, and addressed during software assurance reviews.
2. **Facilitate Compliance Reporting**:
   * Use the data in the repository to generate compliance reports or provide evidence during audits and external reviews (e.g., from OSMA or OCE).
   * Confirm that repository metrics align with **NPR 7150.2**[083](#_tabs-<p></p>) and related software assurance standards.
3. **Analyze Lessons Learned**:
   * Extract repository data after project completion to identify lessons learned, especially in areas like cost estimation, risk management, and defect mitigation.

#### 7.4.2.5  Advocate for Repository Improvement

1. **Recommend Enhancements**:
   * If measurement gaps or process inefficiencies are identified, provide recommendations to improve the quality, scope, or usefulness of repository data.
   * Advocate for automation of metrics collection wherever feasible, ensuring consistency and reducing manual effort.
2. **Ensure Scalability**:
   * Promote the repository’s use not only for individual projects but also for aggregate analysis across multiple projects to inform organizational improvements.

### 7.4.3  Expected Outcomes

Through the diligent implementation of these responsibilities, Software Assurance personnel will support the following outcomes:

1. **Centralized Data Repository**:
   * A reliable and complete repository exists to track Class A, B, and C software project measurements.
2. **Data Accuracy**:
   * The repository’s data is complete, accurate, and actively used to evaluate project performance and adherence to requirements.
3. **Improved Risk Management**:
   * Repository data is leveraged for identifying risks and process improvements, increasing software quality, functionality, and productivity.
4. **Compliance**:
   * The repository ensures the Center is compliant with NASA requirements, including **NPR 7150.2**, enabling traceability and effective oversight.

### 7.4.4  Conclusion

Software Assurance personnel are responsible for verifying that the Center establishes and maintains a software measurement repository containing complete and accurate tracking, functionality, quality, and effort/cost data for Class A, B, and C software projects. SA ensures the repository supports decision-making, enables compliance, and facilitates the continuous improvement of the Center’s software engineering and assurance practices. Regularly monitoring, validating, and leveraging this data will ensure success in meeting both project objectives and organizational goals.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) |
