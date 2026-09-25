# SWE-092 - Using Measurement Data

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695478. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data

SWE-092 - Using Measurement Data

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695478)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695478&showCommentArea=true&showComments=true#addcomment)

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

2.1.5.8 For Class A, B, and C software projects, the Center Director, or designee, shall utilize software measurement data for monitoring software engineering capability, improving software quality, and to track the status of software engineering improvement activities. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-092 History

SWE-092 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.4.3 The project shall specify and record data collection and storage procedures for their selected software measures and collect and store measures accordingly. |
| Difference between A and B | Re-write of software measures requirement to not just collect and store but to utilize the data. |
| B | 2.1.3.10 For Class A, B, C, and safety-critical software projects, the Center Director shall utilize software measurement data for monitoring software engineering capability, improving software quality, and tracking the status of software engineering improvement activities. |
| Difference between B and C | Removed "safety-critical" from the requirement. |
| C | 2.1.5.10 For Class A, B, and C software projects, the Center Director, or designee, shall utilize software measurement data for monitoring software engineering capability, improving software quality, and to track the status of software engineering improvement activities. |
| Difference between C and D | No Change |
| D | 2.1.5.8 For Class A, B, and C software projects, the Center Director, or designee, shall utilize software measurement data for monitoring software engineering capability, improving software quality, and to track the status of software engineering improvement activities. |

## 1.3 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.11 Software Measurements](/spaces/SWEHBVD/pages/133235387/A.11+Software+Measurements) * [A.13 NASA Institutional Requirements](/spaces/SWEHBVD/pages/133235389/A.13+NASA+Institutional+Requirements) |

# 2. Rationale

What gets measured, gets managed. Software measurement programs are established to meet objectives at multiple levels and structured to satisfy particular organization, project, program, and Mission Directorate needs. The data gained from these measurement programs assist in managing projects, assuring quality, and improving overall software engineering practices.

Effective management of software projects requires the ability to monitor, assess, and improve software engineering processes and outcomes. Software measurement data provides objective, quantifiable insights into key aspects of the software's development lifecycle, such as project progress, process efficiency, product quality, and risk management. For critical software projects (Class A, B, and C), leveraging this data is essential to ensure that project objectives are met within defined constraints such as cost, schedule, and performance requirements.

Utilizing software measurement data allows Center Directors, or their designees, to:

1. **Monitor Software Engineering Capability**: By tracking relevant metrics, leadership can evaluate the maturity and efficiency of software development practices, identify bottlenecks, and ensure alignment with organizational standards and goals.
2. **Improve Software Quality**: Measurement data helps identify trends, recurring issues, and opportunities for process improvements, directly contributing to the delivery of reliable, safe, and high-quality software products.
3. **Track Software Improvement Activities**: Measurement data enables a structured approach to tracking the implementation and effectiveness of engineering improvements. It helps assess whether targeted initiatives are achieving their goals and identify areas requiring further action.

For projects critical to mission success, such as Class A, B, and C software, the structured use of measurement data not only facilitates proactive management but also reduces risks and enhances accountability. Through regular monitoring and data-driven decision-making, the organization can ensure continuous improvement in software practices and the delivery of dependable systems.

# 3. Guidance

## 3.1 Organization's Measurement Program:

Each organization is expected to establish and maintain a comprehensive measurement program tailored to its unique needs, environment, and objectives, while aligning with the overarching organizational goals (see [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements)). Refer to Topic [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) for additional guidance.

The measurement program should systematically collect, analyze, and utilize meaningful metrics to support informed decision-making, improve software engineering processes, and enhance mission success. Effective measurement programs provide leadership with the necessary tools to evaluate performance, identify risks, and drive continuous improvement.

### 3.1.1  Importance and Benefits of Measurements/Metrics

Key advantages of measurements and metrics include:

* **Improved Motivation**
  + Involving employees in the process of setting goals and defining metrics fosters ownership and empowerment, increasing job satisfaction and commitment to organizational objectives.
* **Enhanced Communication and Coordination**
  + Frequent reviews and data-driven discussions improve transparency, harmonize relationships among team members, and resolve challenges more effectively.
* **Clarity of Goals**
  + Teams develop a clearer understanding of their objectives, ensuring alignment with organizational goals.
  + Employees are more committed to self-defined goals rather than externally imposed targets.
  + Managers can use metrics to link employee goals to high-level strategic objectives, promoting shared accountability.

### 3.1.2  Purpose of Software Measurements

#### For Current Projects

* Objectively monitor and manage project progress.
* Use metrics for planning, tracking, and resolving issues during the project lifecycle.

#### For Future Projects (Organizational Level)

* Establish baselines to support planning for similar projects.
* Collect lessons learned to enhance software engineering practices.
* Maintain a repository of historical data to inform process improvements and better estimates.

#### General Benefits

* Encourage advanced and detailed planning.
* Enable data-driven decision-making and alignment with project goals.
* Provide objectivity when assessing progress, especially when subjective judgment may be unreliable.
* Ensure early detection of risks and support timely corrective actions to minimize potential crises.
* Improve the accuracy of estimates for costs and schedules by analyzing historical data and trends.

### 3.1.3  Components of a Measurement Program

A successful measurement program includes:

1. **Measurement Objectives**:
   * Align metrics with organizational and project goals, such as improving cost estimation, meeting quality objectives, or ensuring timely delivery.
   * Examples: Track test completion rates, assess operational performance goals, and identify project risks early.
2. **Defined Measures**:
   * Clearly specify the measures that will support the defined objectives.
   * Include both organizational (e.g., quality improvement) and project-specific (e.g., cost, schedule) metrics.
3. **Collection and Storage Methods**:
   * Determine how data will be collected, who is responsible, and whether tools or repositories are required.
4. **Analysis Methods**:
   * Define processes for analyzing the data, such as trending, comparing measures, or aggregating related data.
   * Identify acceptable thresholds for each measure to distinguish between expected and undesired outcomes.
5. **Reporting and Communication**:
   * Specify how results will be shared with the team and management.
   * Highlight key insights that facilitate actionable decisions.
6. **Team and Management Commitment**:
   * Ensure buy-in from stakeholders for the program’s success, including compliance with and usage of the measurement plan.

### 3.1.4  Examples of Organizational Goals and Corresponding Metrics

* **High-Level Strategic Goals**: Meet customer satisfaction, reduce operational costs, or increase mission success rates.
* **Project-Level Goals**: Deliver quality software on time, meet project requirements, and stay within budget.
* **Task-Level Goals**: Meet specific success criteria, such as entry and exit conditions for critical project tasks.

### 3.1.5  Utilization of Software Measurements

Once a software measurement system is in place, the collected metric data enables:

1. **Assessment of Workforce Capability**
   * Analyze workforce skills, training, and development opportunities to identify strengths and gaps.
2. **Enhancement of Software Quality**
   * Monitor and analyze defect rates, problem reports, audit findings, and discrepancies.
   * Use static analysis tools and peer review results to identify and mitigate quality risks early.
3. **Improvement of Development Efficiency**
   * Track and analyze productivity metrics, schedule adherence, and cost performance.
   * Monitor risk mitigations and process improvement initiatives to optimize resource utilization.
4. **Tracking Status of Improvement Activities**
   * Measure progress toward software engineering improvement goals using objective data.

### 3.1.6  Typical Categories of Software Measurement Data ([SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository))

* **Software Development Tracking Data**: Progress relative to schedule and goals.
* **Software Functionality Achieved Data**: Measure functional requirements met.
* **Software Quality Data**: Trends in defect rates, severity, and issue resolution.
* **Software Development Effort and Cost Data**: Track planned vs. actual effort and associated costs.

### 3.1.7  Examples of Measurement Categories and Metrics

#### Measurements for Monitoring Engineering Capability

* Training metrics (e.g., workforce participation in skill development).
* Workforce experience levels.
* Metrics for Agile vs. waterfall project models.

#### Measurements for Improving Software Quality

* Defects reported in problem/change requests.
* Peer review/inspection rates and findings.
* Audit results and findings, including defect classifications.
* Verification/validation metrics (e.g., requirements tested or validated).

#### Measurements for Tracking Improvement Progress

* Results of CMMI assessments.
* Improvements in defect containment rates.
* Progress toward productivity improvements.
* Workforce metrics related to skill enhancement and training.

### 3.1.8  Analysis and Reporting

Metrics are calculated and analyzed using approved methods (see [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)). Findings from these analyses are used to identify trends, detect risks, and evaluate performance. Trends over time provide early warnings of deviations from targets or opportunities for process optimization.

**Key Reporting Priorities**

* Ensure transparency of results across teams.
* Focus on leadership-level reports that enable strategic decision-making.

For detailed usage of measurement data, refer to [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) and [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) to ensure accessibility and continual refinement of data usage practices.

This guidance provides a clear and actionable framework for developing and implementing effective measurement programs that drive software engineering excellence across Class A, B, and C software projects.

The table [497](#_tabs-<p></p>) below provides an example of mapping organizational goals/objectives to metrics:

The specific measurement systems for particular programs and projects enable reporting on the minimum requirements categories listed in [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository), and repeated here:

See also [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) regarding the use of measurement data in software activities reviews.

See also [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) regarding access to measurement data.

## 3.2 Software Assurance Metrics

### 3.2.1  Overview

The use of software assurance (SA) and software safety metrics plays a critical role in assessing the effectiveness of software assurance work, monitoring software engineering progress, and supporting overall mission success. Metrics provide a structured and objective method for evaluating the quality, reliability, and safety of software throughout its lifecycle. Additionally, they help identify risks early, support decision-making, and drive continuous improvement.

Guidance is provided in Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics), which outlines a comprehensive list of SA and safety metrics recommended for use with the SA tasks defined in **NASA-STD-8739.8[278](#_tabs-<p></p>)**. This list of suggested metrics allows SA and safety personnel to collect relevant data that informs their assessments and ensures monitoring of software development aligns with organizational goals and project needs.

### 3.2.2  Accessing and Using the Suggested Metrics

The metrics are available in a detailed table format, including a downloadable Excel file that enhances usability with filtering and sorting capabilities. These tools enable targeted exploration and application of metrics that are most relevant to specific software requirements and phases of the development lifecycle.

**Key features of the metrics table include**:

* A comprehensive list of suggested metrics that align with specific SA tasks in **NASA-STD-8739.8**.
* The ability to trace metrics to specific Software Requirements (SWEs) and filter out tailored-out SWEs based on project scope.
* Suggested metrics collection phases that indicate when each metric should ideally be collected during the software lifecycle.
* Additional notes and guidance at the top of each metrics sheet to ensure correct interpretation and usage.

### 3.2.3  Project-Specific Metrics Application

Every project should carefully review the metrics table and determine which metrics are most suitable for their specific objectives, taking into consideration:

1. **Relevance**
   * Select metrics that align with project-specific goals, risks, and technical needs.
   * Focus on metrics that provide actionable insights for both software assurance and software safety tasks.
2. **Value**
   * Choose metrics that offer the greatest value by providing essential information for evaluating software assurance/safety effectiveness and identifying potential process or product risks.
3. **Tailoring**
   * Eliminate metrics for SWEs that have been tailored out of the project scope, ensuring efficiency and focus on relevant activities.

### 3.2.4  Purpose of Software Assurance Metrics

1. **Assessment of Software Assurance/Safety Work**:
   * Metrics enable objective evaluation of SA processes and their contributions to software quality, reliability, and safety.
   * They also allow tracking of SA tasks to ensure they are performed with sufficient rigor throughout the software lifecycle.
2. **Monitoring Software Engineering Progress**:
   * Metrics provide visibility into the progress of development activities, allowing for early identification of risks, delays, or deviations from project goals.
   * Regular monitoring helps ensure alignment with project requirements and improves decision-making through data-driven insights.

### 3.2.5  Guidelines for Metric Implementation

To ensure effective collection and utilization of metrics, the following steps are recommended:

1. **Alignment to Lifecycle Phase**:  
   Map each selected metric to the appropriate lifecycle phase. Ensure the metrics are collected at times that provide the most useful insights for SA tasks (e.g., planning, design, implementation, testing, or deployment).
2. **Customization and Prioritization**:  
   Tailor the metrics to address the unique characteristics of your software project, including criticality, safety requirements, and mission objectives. Prioritize metrics that are directly relevant to the most critical areas of software assurance and safety.
3. **Consistency and Traceability**:
   * Ensure that the chosen metrics are consistently applied and properly documented.
   * Trace metrics to their associated SWEs and project objectives to provide a clear line of accountability.
4. **Regular Review**:  
   Review the metrics periodically to ensure they continue to meet project needs and adapt to changes in the development process or scope.
5. **Analysis and Reporting**:  
   Use well-defined analysis techniques to interpret metric data and generate actionable insights. Clearly communicate findings through reports tailored to the audience (e.g., developers, managers, or safety regulators).

### 3.2.6  Additional Tools and Resources:

* **Excel Metrics Sheet**:  
  The downloadable Excel file, accompanying the metrics table, allows for:
  + Filtering of metrics by phase, SWE, or relevance to specific assurance tasks.
  + Simplified identification of applicable metrics for tailored projects.

**Tip**: Ensure that project teams refer to the guidance provided at the top of the metrics sheet to fully understand its use and interpret the data effectively.

* **Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)**
  + Refer to this topic for the complete, up-to-date list of suggested metrics.
  + It provides additional context and examples for using metrics in SA tasks.
* **Topic [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report)**
  + Refer to this topic for guidance on the minimum recommended content of a Software Metrics Report.

### 3.2.7  Value of SA Metrics:

The thoughtful collection and application of software assurance metrics provide the following benefits:

1. **Increased Transparency**
   * Metrics provide objective evidence of software assurance and safety work progress, enabling better visibility for stakeholders at all project levels.
2. **Improved Risk Management**
   * By monitoring quality and safety trends, metrics help identify emerging risks early, allowing for timely corrective actions.
3. **Enhanced Decision-Making**
   * Data-driven insights gained from metrics enable more informed and confident decisions throughout the software lifecycle.
4. **Aligned Assurance Efforts**
   * Metrics help ensure that assurance activities remain aligned with project requirements and organizational goals, improving accountability and outcomes.
5. **Continuous Improvement**
   * Metrics provide a feedback mechanism for identifying opportunities to improve software assurance processes, tools, and techniques.

## 3.3 Conclusion

A well-implemented software assurance metrics program helps ensure that software assurance activities are effective, efficient, and aligned with project and mission objectives. Ensuring proper customization, collection, analysis, and communication of metrics is essential for maximizing their value. By leveraging the recommended metrics and tools, projects can better assess the health and safety of their software while enabling better monitoring of engineering progress and overall quality improvement.

**Related References**:

* **[SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository)**: For repositories to store and track metrics data.
* **[SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)**: For proper analysis techniques.
* **NASA-STD-8739.8**: For complete details on software assurance and safety expectations.
* **[SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review)**: For leveraging measurement data in software reviews.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics)      * [Improvement](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Improvement) |

# 4. Small Projects

## 4.1 Guidance for Small Projects

Even for small projects, implementing software measurement programs is critical for tracking progress, ensuring quality, and identifying improvement opportunities. However, small projects often have fewer resources and simpler scopes than larger projects, so the approach to measurement should be lightweight, focused, and practical. The following guidance tailors this requirement to small projects:

### 4.1.1  Start Small – Focus on Key Metrics

Small projects don’t need an extensive set of metrics. Focus only on a few that provide the most value to your specific objectives. Recommended metrics could include:

* **Schedule Adherence**: Track planned vs. actual completion dates to monitor progress.
* **Defect Density**: Identify the number of defects per unit of software (e.g., per 1,000 lines of code or per function point).
* **Effort Tracking**: Record actual hours worked to assess resource usage against estimates.

These simple metrics help ensure oversight while minimizing administrative effort.

### 4.1.2  Use Existing Tools and Processes

Small projects often have limited access to specialized tools. Take advantage of tools already in use within the organization, such as:

* Project management or task tracking software (e.g., Jira, Trello, MS Project) for tracking milestones and effort.
* Code repositories (e.g., Git, GitHub) for logging commits and monitoring code development trends.
* Static analysis tools (e.g., SonarQube, Coverity) for collecting code quality metrics.

**Tip:** Use built-in reporting features in these tools to simplify metric collection.

### 4.1.3  Minimal Overhead for Metric Collection

* Focus on automating data collection wherever possible. For example, use automated testing tools, version control systems, or build pipelines to gather defect rates, code coverage, or progress metrics.
* If automation isn’t feasible, designate a single team member (e.g., the project manager or software lead) to collect and log data periodically.
* Avoid collecting data "just for the sake of it." Ensure each metric has a clear purpose and actionable insights tied to it.

### 4.1.4  Simplify the Measurement Plan

Small projects can use a lightweight measurement plan that includes:

* The **objectives**: Define what you hope to achieve with the metrics (e.g., ensuring on-time delivery, tracking quality).
* The **metrics**: List the key metrics you’ll collect (3–5 metrics max).
* The **collection process**: State how the data will be collected (e.g., from tools, manual entry) and how often (e.g., every two weeks).
* The **reporting structure**: Identify how metrics will be communicated (e.g., a brief dashboard or Excel report shared during weekly meetings).

**Example of a Simplified Measurement Plan**:

| Objective | Metric | Collection Frequency | Data Source | Reporting Method |
| --- | --- | --- | --- | --- |
| Track progress | Schedule adherence | Weekly | Gantt chart | Email update |
| Ensure software quality | Defect density | End of sprint | Issue tracker | Dashboard slide |
| Manage resource usage | Actual vs. estimated effort | Biweekly | Timesheets | Progress report |

### 4.1.5  Use Metrics for Early Risk Detection and Continuous Feedback

Regularly review the collected metrics to identify risks and adjust as needed. For example:

* **Schedule slippage**: If schedule adherence metrics indicate delays, hold a team review to identify the root cause and mitigate future impacts.
* **Increasing defect rates**: High defect density may point to gaps in requirements, coding practices, or testing coverage. Address these issues early through targeted actions, such as improved peer reviews or strengthening regression testing.

### 4.1.6  Track Improvement Activities on a Small Scale

Improvement activities for small projects should focus on manageable, high-impact initiatives. Examples include:

* Conducting lightweight retrospectives at the end of each sprint or milestone to reflect on lessons learned.
* Using defect trend analysis to identify frequently occurring issues and implementing targeted changes (e.g., improving testing protocols, refining code reviews).
* Sharing insights and lessons learned with the broader organization to contribute to continuous improvement efforts at the Center level.

### 4.1.7  Reporting and Communication

Small projects can simplify how they communicate software measurement results:

* Keep reports concise (e.g., 1-page summaries, dashboards, or short team presentations).
* Focus on key findings and their implications rather than overwhelming stakeholders with raw data.
* Highlight actionable insights to reinforce the value of metrics collection.

### 4.1.8  Template for Small Project Implementation

Below is an example of a simple implementation checklist for small projects:

#### **Quick Checklist for Compliance**:

* **Define objectives**: Document which project goals the metrics will support (e.g., quality, timeline compliance).
* **Select 3–5 key metrics**: Choose metrics that provide the greatest insight into project health.
* **Assign responsibilities**: Assign a single person to oversee metric collection and reporting.
* **Automate when possible**: Use tools to automate data gathering and reduce manual effort.
* **Establish a reporting plan**: Share metric results weekly or biweekly in a simple, actionable format (e.g., charts, trend lines).
* **Review regularly**: Use metrics to drive periodic discussions about project risks and improvement opportunities.
* **Contribute lessons learned**: Share insights with the organizational repository (if applicable).

## 4.2  Example in Practice

#### A Small Project Scenario:

A small team of 5 developers is building a software module for a larger system. The following approach is used to apply the requirements outlined:

1. **Core Metrics**:   
   The team selects:
   * Schedule adherence (% tasks completed on time).
   * Defect density (defects per 1,000 lines of code).
   * Team effort (hours worked vs. hours estimated).
2. **Collection Plan**:
   * Schedule data is tracked in their project board (e.g., Jira).
   * Defect data is tracked using the bug tracker.
   * Effort data is recorded in timesheets submitted weekly.
3. **Review Process**:
   * Metrics are reviewed during biweekly sprint reviews.
   * The team identifies and resolves risks (e.g., missed milestones, high bug count) collaboratively.

#### Outcome:

Through lightweight metric tracking, the team detects and corrects schedule delays early, reduces post-development defects by improving code review processes, and ultimately delivers the project on time with minimal rework.

## 4.3 Conclusion

For small projects, the most important steps are to keep the metrics program simple, focused, and actionable. A lightweight, targeted approach saves resources while still providing the oversight needed to meet the requirements of monitoring software engineering capability, improving software quality, and tracking improvement activities. By emphasizing automation, clarity, and relevance, small projects can achieve measurable benefits with minimal overhead.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-252)

  [Software Metrics: SEI Curriculum Module SEI-CM-12-1.1.](http://www.sei.cmu.edu/reports/88cm012.pdf "Click to open in new window")

  Mills, Everald E. (1988). Carnegie-Mellon University-Software Engineering Institute.  Retrieved on December 2017 from http://www.sei.cmu.edu/reports/88cm012.pdf.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-355)

  [12 Steps to Useful Software Metrics,](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics_in_12_steps_paper.pdf "Click to open in new window")

  Westfall, Linda, The Westfall Team (2005),   Retrieved November 3, 2014 from http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics\_in\_12\_steps\_paper.pdf
* (SWEREF-367)

  [IEEE Standard Dictionary of Measures of the Software Aspects of Dependability,](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1634994 "Click to open in new window")

  IEEE Computer Society, Sponsored by the Software Engineering Standards Committee, IEEE Std 982.1™-2005, (Revision of IEEE Std 982.1-1988),
* (SWEREF-430)

  ["Lessons learned from 25 years of process improvement: The Rise and Fall of the NASA Software Engineering Laboratory,"](http://www.cs.umd.edu/projects/SoftEng/ESEG/papers/83.88.pdf "Click to open in new window")

  Basili, V.R., et al. (May, 2002). University of Maryland, College Park. Experimental Software Engineering Group (ESEG). Lessons Learned Reference.
* (SWEREF-497) MSFC Flight & Ground Software Division (ES50) Organizational Metrics Plan, EI32-OMP Revision D April 29, 2013. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA’s **[Lessons Learned Information System (LLIS)](https://llis.nasa.gov/)** contains numerous case studies and insights emphasizing the importance of software measurement, project monitoring, and process improvements. Below are relevant lessons learned tied to this requirement.

### 6.1.1  Relevant NASA Lessons Learned

#### 1.  Importance of Metrics in Preventing Software Failures

* **Lesson Number**: LLIS-2204
* **Description**: The lack of early, meaningful metrics was identified as a contributing factor in multiple costly project delays and overruns. Establishing and using metrics to monitor software engineering progress earlier in the lifecycle could have mitigated risks and enabled proactive corrections.
* **Relevance to Requirement**:  
  This lesson underscores the importance of using software metrics to monitor progress and identify issues early. Center Directors and project managers can leverage metrics such as defect density, effort tracking, or productivity to reduce technical and programmatic risks.
* **Key Insight**: Incorporate metrics as a routine part of status reviews, starting from the early lifecycle stages, to track progress and establish clear baselines.

#### 2.  Software Quality Metrics Avoid Costly Post-Launch Defects

* **Lesson Number**: LLIS-1842
* **Description**: On the Mars Climate Orbiter, insufficient use of software measurement and validation metrics led to a critical error in units (imperial vs. metric) between ground systems and flight software. Early use of validation metrics could have detected the inconsistency before integration.
* **Relevance to Requirement**:  
  Metrics related to software functionality tests, validation checks, and integration progress allow for early detection of critical inconsistencies. The failure to implement robust measurement processes contributed to the mission’s loss, demonstrating why quality metrics are essential.
* **Key Insight**: Validation metrics during critical phases (e.g., testing, integration) greatly reduce the likelihood of unforeseen technical issues reaching deployment.

#### 3.  Monitoring Software Risks and Trends [529](#_tabs-<p></p>)

* **Lesson Number**: LLIS-0938
* **Description**: During the development of a flight software component for a large mission, defect metrics and schedule adherence metrics were tracked inconsistently. This led to a late recognition of resource constraints and schedule overruns, resulting in excessive overtime and reduced software quality.
* **Relevance to Requirement**:  
  This highlights the need for routine monitoring of software engineering capability metrics. Tracking workforce metrics (e.g., team productivity, overtime, experience), along with technical metrics, helps management identify risks stemming from resource issues.
* **Key Insight**: Comprehensive tracking of both technical progress (bugs fixed, requirements met) and team capacity (availability, overtime) ensures informed decision-making and reduces workload imbalances.

#### 4.  Lessons from the James Webb Space Telescope (JWST) Software Development

* **Lesson Number**: LLIS-2310
* **Description**: For large, complex projects like JWST, inconsistent collection and application of software engineering metrics led to gaps in status tracking. A lack of formalized processes for analyzing and acting on software measurements delayed the identification of underlying engineering and quality defects, requiring unplanned rework late in the project.
* **Relevance to Requirement**:  
  Predefined metrics for software engineering quality and improvement activities need to be consistently monitored to enable early risk mitigation. Without a formalized feedback cycle, metrics lose their effectiveness.
* **Key Insight**: Metrics should always include clear analysis, communication, and feedback loops to support proactive decision-making and continuous improvement activities.

#### 5.  Apply Lessons from CMMI to Improvement Activities

* **Lesson Number**: LLIS-1680
* **Description**: Projects that implemented CMMI (Capability Maturity Model Integration)-based process improvement activities showed significant reductions in defect rates and improved schedule performance. However, projects that didn’t track metrics to assess improvement progress struggled to sustain long-term improvements.
* **Relevance to Requirement**:  
  This lesson reinforces the importance of tracking the status of software engineering improvement activities using metrics (e.g., defect reduction trends, productivity improvements). Measuring the effectiveness of improvement actions allows projects to validate and institutionalize process changes.
* **Key Insight**: Metrics tied to improvement goals (e.g., fewer post-delivery defects, better testing coverage) are essential for evaluating the success of long-term engineering upgrades.

#### 6.  Prioritize Metrics for Software Assurance Reviews

* **Lesson Number**: LLIS-1921
* **Description**: During a major Earth Science mission, software assurance metrics (e.g., peer review effectiveness, test coverage, and defect closure rates) were inconsistently integrated into programmatic reviews. This led to unbalanced quality assessments and risks slipping through unnoticed.
* **Relevance to Requirement**:  
  Incorporating assurance-related metrics (e.g., requirement verification success rates, problem report trends) into regular reviews ensures that software assurance and quality objectives are consistently monitored and addressed.
* **Key Insight**: Metrics must explicitly flow into project reviews to ensure that software risks, quality, and assurance progress are consistently evaluated. This improves accountability across the software lifecycle.

#### 7.  Software Measurements Reduce Overcommitments

* **Lesson Number**: LLIS-1273
* **Description**: Projects without robust software measurement practices frequently overcommitted to overly ambitious schedules and underestimated resource needs. This was a significant factor in the delay and cost impact on several missions.
* **Relevance to Requirement**:  
  Metrics like actual vs. planned effort, backlog tracking, and milestone adherence provide early warnings of resource over-allocation or unrealistic schedules, allowing leadership to adjust expectations and plans.
* **Key Insight**: Use metrics to manage stakeholder expectations realistically. Regularly compare planned vs. actual performance to identify disconnects and rebaseline, if necessary.

#### 8.  Tailoring Metrics for Small Projects

* **Lesson Number**: LLIS-1532
* **Description**: On smaller software projects, overly cumbersome metrics programs caused administrative burdens without adding proportional value. Tailored, lightweight metrics (e.g., weekly task completion rates, functional test success rates) were more effective in meeting project needs without overwhelming the team.
* **Relevance to Requirement**:  
  This lesson highlights the importance of scaling metrics programs to the size and complexity of the project. Tailoring ensures that only the most actionable and relevant metrics are collected, avoiding unnecessary resource usage.
* **Key Insight**: Emphasize lightweight, streamlined metrics for small projects to balance insight with practicality.

### 6.1.2  Summary of Lessons Applicable to the Requirement:

1. **Start Early**: Establish metrics at the beginning of the project to track baseline and progress over time.
2. **Focus on Quality and Risk Mitigation**: Use metrics to monitor defect trends, validation success, and software quality.
3. **Connect Metrics to Improvement**: Align metrics with software engineering improvement goals to measure their effectiveness.
4. **Regular Reporting and Communication**: Ensure metrics are analyzed, reviewed, and communicated to support informed decisions.
5. **Tailor Metrics to the Project’s Needs**: Ensure metrics programs are scalable and practical, especially on smaller projects.

### 6.1.3  References and Tools:

* **NASA Lessons Learned Information System (LLIS)**: (<https://llis.nasa.gov/>) - Explore detailed case studies and official NASA lessons learned.
* **NASA-STD-8739.8 [278](#_tabs-<p></p>)**: Defines software assurance and software safety standards.
* **[SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository)**: Guidance on establishing and maintaining a measurement repository.

## 6.2 Other Lessons Learned

* Much of NASA's software development experience that was accomplished in the NASA/GSFC Software Engineering Laboratory (SEL) is captured in "Lessons learned from 25 years of process improvement: The Rise and Fall of the NASA Software Engineering Laboratory[430](#_tabs-<p></p>). The document describes numerous lessons learned that are applicable to the Agency's software development activities. From their early studies, they were able to build models of the environment and develop profiles for their organization. One of the key lessons in the document is "Lesson 6: The accuracy of the measurement data will always be suspect, but you have to learn to live with it and understand its limitations."

# 7. Software Assurance

**SWE-092 - Using Measurement Data**

2.1.5.8 For Class A, B, and C software projects, the Center Director, or designee, shall utilize software measurement data for monitoring software engineering capability, improving software quality, and to track the status of software engineering improvement activities.

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

This requirement ensures that the Center uses software measurement data for actionable decision-making to:

1. **Monitor Software Engineering Capability**: Assess and track the effectiveness of software engineering processes.
2. **Improve Software Quality**: Identify and address quality issues to increase reliability, performance, and compliance.
3. **Track Software Engineering Improvement Activities**: Evaluate progress and outcomes of efforts aimed at enhancing software engineering practices.

Software Assurance (SA) personnel play a critical role in validating the use of measurement data to meet these goals by ensuring its accuracy, relevance, and proper application for monitoring, improvement, and tracking activities.

### 7.4.2  Software Assurance Responsibilities

#### 7.4.2.1  Verify the Collection and Relevance of Measurement Data

1. **Ensure Relevant Measurements Are Collected**
   * Confirm that measurement data collected for Class A, B, and C software projects aligns with the following broad categories:
     + **Software Engineering Process Metrics**:
       - Examples: Task completion rates, schedule variance, process compliance metrics, rework rates.
     + **Software Quality Metrics**:
       - Examples: Defect density, test coverage, severity distribution of anomalies, number of safety-critical issues identified/resolved.
     + **Improvement Activity Metrics**:
       - Examples: Baseline and post-implementation data for changes in process effectiveness, training outcomes, and adoption of best practices.
     + **Other Performance Metrics**:
       - Examples: Requirements volatility, productivity (e.g., KSLOCs per hour), and resource utilization.
2. **Verify Completeness and Accuracy**
   * Periodically review collected data to confirm that it is:
     + **Complete**: Includes valid and sufficient data from all applicable Class A, B, and C projects.
     + **Accurate**: Free from errors and traceable to source documents such as software plans, test results, and review reports.
   * Validate measurement tools and methods to ensure consistent and trustworthy results.

#### 7.4.2.2  Assess How the Center Uses Measurement Data

1. **Monitor Software Engineering Capability**
   * Verify that software measurement data is actively used to assess the effectiveness of the Center’s software engineering processes. Examples include:
     + Tracking adherence to established schedules, budgets, and plans.
     + Identifying inefficiencies in engineering practices (e.g., excessive delays in reviews or incomplete implementation of required processes).
     + Analyzing the frequency and causes of rework or requirement changes to identify potential systemic issues.

*SA Oversight*:

1. * + Ensure that measurement data is compared against defined baselines or benchmarks to assess capabilities.
     + Monitor whether changes are implemented for low-performing processes based on these insights.
2. **Improve Software Quality**
   * Confirm that the Center uses data to drive software quality improvements by:
     + Identifying trends in defect insertion and removal rates.
     + Monitoring test coverage and identifying gaps leading to quality risks.
     + Analyzing severity or recurrence of software issues to target process fixes or additional testing.
   * Provide feedback on the effectiveness of quality improvement activities based on measurable outcomes (e.g., improved defect density over time).  

     *SA Oversight*:

     + Check whether quality-related findings are shared with project teams and inform corrective action plans.
     + Monitor whether recurring issues are managed through process improvement initiatives.
3. **Track Software Engineering Improvement Activities**
   * Ensure metrics are used to track the outcomes of improvement activities, such as:
     + Adoption of new tools, methodologies, or training programs (e.g., Agile, DevOps, automated testing).
     + Reduction in project delays, defect counts, or rework efforts following implemented improvements.
     + The measurable impact of compliance reviews or audits on process discipline.

*SA Oversight*:

1. * + Verify that improvement activities are well-documented and include metrics for before-and-after comparisons.
     + Confirm that progress is reported to relevant stakeholders (e.g., Center leadership, OCE, OSMA) using clear and reliable data.

#### 7.4.2.3  Analyze and Use Trends for Continuous Improvement

1. **Perform Trend Analysis**
   * Verify that the Center regularly analyzes long-term trends using measurement data. Examples of trend analysis include:
     + Identifying patterns in software development schedule delays or quality issues.
     + Tracking how defect density evolves over different project phases.
     + Comparing testing efficiency across multiple projects.
2. **Support Lessons Learned Activities**
   * Use insights from trend analysis to identify lessons learned and provide recommendations for future projects. Examples:
     + Highlighting process inefficiencies and areas requiring additional training.
     + Sharing successful practices across teams to replicate improvements.

*SA Oversight*:

* + Ensure that lessons learned are documented, shared, and incorporated into future project plans and Center policies.

#### 7.4.2.4  Ensure Effective Communication of Measurement Data Results

1. **Validate Reporting of Measurement Data**
   * Confirm that reporting on measurement data explicitly highlights how the data is used to:
     + Evaluate software engineering performance and capability.
     + Track progress on specific improvement activities.
     + Drive actionable quality improvements based on data-driven insights.
2. **Provide Feedback for Decision-Making**
   * Ensure that measurement data results are communicated clearly to Center leadership and project teams to inform management decisions.
   * Verify that data is used during milestone reviews (e.g., Software Peer Reviews, Technical Reviews) to assess progress, pinpoint risks, and ensure compliance.
3. **Report Software Metrics**
   * See Topic [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report): This topic provides guidance on the minimum recommended content of a Software Metrics Report.

#### 7.4.2.5  Monitor Compliance with Metrics Use

1. **Audit the Use of Measurement Data**
   * Assess whether the collected measurement data is being actively used in the areas of capability monitoring, quality improvement, and improvement tracking.
   * Identify gaps where data is not being leveraged effectively and provide recommendations to address them.
2. **Ensure Timeliness and Consistency**
   * Validate the timeliness of measurement data collection and reporting to ensure that actionable insights are available when needed.
   * Monitor consistency in how measurement data is interpreted and applied across projects.

#### 7.4.2.6  Recommend Enhancements to the Use of Metrics

1. **Encourage Proactive Metrics Use**
   * Promote a culture of proactive metrics usage by encouraging teams to:
     + Set targets for key performance indicators (KPIs).
     + Use predictive metrics (e.g., defect prediction models) to identify problems early.
     + Integrate dashboards or visualization tools for accessible metrics analysis.
2. **Advocate for Metrics Expansion**
   * Where gaps exist, recommend expanding the types of metrics collected to provide better insight into problem areas such as testing, cybersecurity, or process adherence.

### 7.4.3  Expected Outcomes

Through diligent application of these responsibilities, Software Assurance personnel will help ensure that:

1. **Improved Monitoring**:
   * The Center effectively monitors its software engineering capability using actionable metrics.
2. **Enhanced Quality**:
   * Regular data analysis and use result in measurable improvements in software quality.
3. **Successful Improvement Initiatives**:
   * Metrics provide reliable tracking of software improvement activities, enabling better management of process enhancements.
4. **Data-Driven Decision-Making**:
   * Measurement data supports informed decision-making and strategic planning for both ongoing and future projects.
5. **Compliance**:
   * The Center complies with NASA directives, particularly **NPR 7150.2[083](#_tabs-<p></p>)**, regarding metrics usage for Class A, B, and C software.

### 7.4.4  Conclusion

Software Assurance (SA) personnel are responsible for validating that software measurement data is actively utilized to monitor, improve, and track software engineering processes and quality for Class A, B, and C software projects. By ensuring completeness, accuracy, relevance, and proper use of the data, SA contributes to the Center’s ability to make data-driven decisions, improve software quality, and achieve compliance with NASA requirements. Continuous monitoring, trend analysis, and feedback loops will further support a culture of excellence and improvement in software engineering.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |
