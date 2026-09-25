# SWE-093 - Analysis of Measurement Data

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695480. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data

SWE-093 - Analysis of Measurement Data

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695480)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695480&showCommentArea=true&showComments=true#addcomment)

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

5.4.3 The project manager shall analyze software measurement data collected using documented project-specified and Center/organizational analysis procedures.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-093 History

SWE-093 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 4.4.4 The project shall analyze software measurement data collected using documented project-specified and Center/organizational analysis procedures. |
| Difference between A and B | No change |
| B | 5.4.3 The project shall analyze software measurement data collected using documented project-specified and Center/organizational analysis procedures. |
| Difference between B and C | No change |
| C | 5.4.3 The project manager shall analyze software measurement data collected using documented project-specified and Center/organizational analysis procedures. |
| Difference between C and D | No change |
| D | 5.4.3 The project manager shall analyze software measurement data collected using documented project-specified and Center/organizational analysis procedures. |

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

NASA software measurement programs are now being designed [297](#_tabs-<p></p>) to provide the specific information necessary to manage software products, projects, and services. Center, organizational, project, and task goals (see [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements)) are determined in advance and then measurements and metrics are selected (see [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository)) based on those goals. These software measurements are used to make effective management decisions as they relate to established goals. Documented procedures are used to calculate and analyze metrics that indicate overall effectiveness in meeting the goals.

Typically, the effectiveness of the project in producing a quality product is characterized by measurement levels associated with the previously chosen metric. The use of measurement functions and analysis procedures that are chosen in advance helps assure that Center/organizational goals are being addressed.

### **Purpose of the Requirement**

This requirement ensures that software measurement data is **not just collected**, but is also analyzed systematically to extract actionable insights that support effective decision-making, risk management, and project success. By requiring the analysis of measurement data and adherence to documented analysis procedures, this requirement promotes **consistency, traceability**, and the use of best practices in the interpretation of the data.

Effective analysis ensures:

1. **Informed Decision-Making**: Analysis transforms raw data into meaningful reports and trends, giving project managers and stakeholders a clear view of the project’s health, risks, and performance.
2. **Identification of Issues**: Data analysis enables the detection of deviations, anomalies, and risks early in the development lifecycle, allowing corrective actions to be taken before they escalate.
3. **Process Improvement**: Consistent analysis highlights trends and patterns over time, providing opportunities for continuous process improvements for the current project and future efforts.
4. **Compliance and Standardization**: Center or organizational analysis procedures provide a common framework and methodology for analyzing data, ensuring consistency and alignment with NASA’s broader mission goals and standards.
5. **Accountability and Traceability**: Documented procedures help ensure that the data analysis process is traceable, repeatable, and reliable, supporting audits and independent verification activities.

---

### **Why This Requirement is Important**

#### **1. Actionability of Data**

Simply collecting measurement data without performing thorough analysis does not yield any benefit. Data must be analyzed to draw meaningful conclusions and make proactive adjustments. For example:

* **Defect Data**: Analysis of collected defect data helps identify root causes (e.g., coding errors, unclear requirements) and prioritize defect fixes to minimize impact.
* **Schedule Data**: Analyzing project milestones and progress trends can help identify schedule slippage and enable the team to reallocate resources or adjust timelines.
* **Testing Trends**: Analysis of test results (e.g., passed/failed cases, code coverage) provides insights into software quality, risks, and areas that need more attention.

Without analysis, data is merely a collection of numbers, offering no insight or value to the project.

---

#### **2. Preventing Bias and Inconsistency**

Adhering to documented project-specific and Center/organizational analysis procedures ensures the analysis is conducted systematically, unbiased, and consistent with industry and organizational best practices. It mitigates:

* **Ad hoc or inconsistent data interpretation**: Different interpretations of the same data by various stakeholders can lead to inconsistencies and conflicts.
* **Human bias**: Objective procedures prevent reliance on subjective judgment, ensuring data results drive decisions.

---

#### **3. Early Identification of Risks**

Data analysis helps to identify critical risks and issues in their early stages, rather than waiting for them to manifest into larger problems. Examples include:

* Increasing defect trends indicating potential quality concerns.
* Resource over-allocation or under-utilization leading to unbalanced workloads.
* A higher-than-expected number of late-stage requirements changes, which can increase project complexity.

Proactive identification and mitigation of risks is one of the key reasons why this requirement exists.

---

#### **4. Supports Continuous Improvement**

Analyzing measurement data not only helps improve the current project but also contributes to NASA’s objective of institutional learning and organizational process improvement. Consistently analyzed measurement data helps to:

* Identify patterns and systemic issues (e.g., common causes of defects, recurring schedule delays).
* Highlight areas where process efficiency can be improved (e.g., better resource allocation, improvements in validation processes).

Projects that use systematic analysis procedures are better positioned to develop valuable lessons learned and contribute to broader organizational improvements.

---

#### **5. Institutional Alignment**

NASA operates in a highly collaborative and multi-disciplinary environment where projects work across multiple Centers, teams, and contractors. Using project-specific and **Center/organizational analysis procedures** ensures alignment across organizations and promotes a consistent approach to analyzing measurement data. This ensures:

* Data analysis aligns with organizational-level objectives and reporting requirements.
* Cross-program consistency, enabling benchmarking and comparisons (e.g., between similar missions or lifecycle phases).
* Standardized methodologies for audits, reviews, and evaluations conducted by oversight organizations.

Consistency in analysis processes ensures a shared understanding and fosters trust in the data and its derived insights.

---

### **Examples of Analysis and Benefits**

| **Example** | **Data** | **Analysis** | **Benefit** |
| --- | --- | --- | --- |
| Schedule Adherence | Planned vs. actual milestone dates | Analyze schedule slippage trends. Identify tasks consistently running late. | Enables managers to take corrective action, such as additional resources or task reprioritization. |
| Defect Density | Number of defects found per KLOC during testing | Monitor defect trends and severity classification over time. | Identifies high-risk areas in the software and helps focus validation efforts. |
| Requirements Volatility | Number of changes (additions, deletions, modifications) | Track frequency of changes. Correlate changes with schedule impacts. | Identifies instability in requirements definition, enabling mitigation actions. |
| Resource Utilization | Hours worked versus planned hours | Compare actual utilization to projections across roles and teams. | Prevents resource overloading/bottlenecks and ensures staffing aligns with project needs. |
| Testing Coverage | Percent of requirements tested, passed/failed tests | Track coverage gaps and pass/fail rates. | Ensures all requirements are tested and risks related to uncovered requirements are minimized. |

These examples highlight how documented and systematic analysis of measurement data can directly benefit project management, decision-making, and risk management.

---

### **Non-Compliance Risks**

Failure to properly analyze collected measurement data as required may result in several risks:

1. **Undetected Issues**: Problems such as cost overruns, schedule delays, poor quality, or increasing risks may go unnoticed until they escalate, leading to expensive or mission-critical consequences.
2. **Inconsistent Analysis**: Without adhering to established procedures, teams may use inconsistent approaches, leading to incorrect conclusions or conflicting decisions.
3. **Missed Opportunities for Improvement**: Lack of systematic analysis prevents teams from identifying process efficiencies and lessons learned for future use.
4. **Non-Alignment with Standards**: Failing to comply with organizational procedures risks audits or reviews flagging issues, requiring costly rework.

---

### **Conclusion**

The rationale for Requirement 5.4.3 lies in the need to ensure that collected measurement data is **systematically analyzed** to detect trends, support informed decisions, mitigate risks, and continuously improve processes. Documented analysis procedures ensure consistency, objectivity, traceability, and alignment with organizational best practices. By requiring such analysis, NASA enhances its ability to achieve mission success, foster process improvement, and ensure compliance with internal and external standards. This requirement directly contributes to the delivery of safe, high-quality, and cost-effective software solutions.

# 3. Guidance

**Management without metrics****is just guessing**

***"What gets measured, gets managed."*** *- Peter Drucker*

There is so much power in this quote. If you've never tracked yourself, you don't even know how much power there is in tracking. I couldn't even explain it adequately. You wouldn't believe me. You'd think I was exaggerating. The simple act of paying attention to something will cause you to make connections you never did before, and you'll improve those areas - almost without any extra effort.

## **Overview**

SWE-093 focuses on ensuring that the software measurement data collected over the course of a project is analyzed systematically using documented procedures specific to the project, Center, or organization. Successful compliance with this requirement ensures that the measurement program not only generates actionable insights but also supports effective decision-making, risk mitigation, and alignment with project objectives. Guidance under this requirement emphasizes the importance of defining clear metrics, establishing robust analysis procedures, and maintaining traceability and objectivity throughout the lifecycle.

The following improved guidance provides a structured framework for selecting and analyzing software metrics while addressing common challenges and best practices, incorporating flexibility to address the dynamic nature of software projects.

---

### **1. Defining Analysis Procedures**

Analysis of collected software measurement data should adhere to robust, documented procedures to ensure consistency, traceability, and reliability. Implicit within SWE-093 is the need to carefully **define, evaluate, and select analysis procedures** before the project begins. These analysis methods must align with project-specific measurement goals as well as any higher-level objectives outlined by the Center or organizational standards.

Key considerations:

* Establish documented analysis procedures early in the project lifecycle (e.g., detailed in the **Software Development Plan (SDP)** or **Software Management Plan (SMP)**).
* Ensure that analysis procedures evolve alongside the project and its changing requirements, addressing updates to metrics where new risks or objectives are identified.
* Demonstrate traceability between the analyzed metrics, the procedures used, and their alignment with specific project objectives.

---

### **2. Selecting Meaningful Software Metrics**

The success of measurement analysis hinges on selecting well-defined and actionable metrics. SWE-093 requires that *appropriate* software metrics be chosen to capture key performance, quality, and process indicators. To ensure the metrics are valuable, consider the following principles:

#### **2.1 Metric Types**

* **Primitive Metrics** (Base Metrics): These metrics are directly measurable or observable and form the foundation of most analysis procedures. Examples:
  + Source Lines of Code (SLOC).
  + Number of defects found during each development phase (e.g., unit testing, integration testing).
  + Time spent on specific activities (e.g., code reviews, inspections, testing).
* **Derived Metrics** (Computed Metrics): These metrics are calculated through formulas or models combining base metrics or other derived metrics. These are often more useful in understanding project progress or predicting outcomes. Examples:
  + Defect density (defects per KLOC).
  + Productivity (SLOC per person-month).
  + Test execution efficiency (e.g., passed test cases versus total attempted cases).

#### **2.2 Metric Characteristics**

Ideal metrics should have the following characteristics:

* **Traceable**: Directly traceable to organizational or project-specific goals (e.g., quality improvement or risk mitigation).
* **Simple and Precisely Defined**: Minimizing ambiguity in their definition and ensuring consistent interpretation across stakeholders.
* **Objective**: Free from subjective bias or inconsistent interpretation.
* **Easily Obtainable**: Collectible and computable using existing tools and processes at reasonable cost and effort.
* **Valid**: Accurately measuring what it is supposed to measure (e.g., defect rate as a quality indicator).
* **Robust**: Reliable and not overly sensitive to small, inconsequential variations.

---

### **3. Developing Metric Analysis Procedures**

The following framework ensures clarity and consistency in defining analysis procedures for software measurement data:

#### **3.1 Approaches to Metric Analysis**

* **Use an Existing Model**: Proven models from prior NASA projects or industry standards (e.g., materials in the NASA Software Measurement Guidebook) should be leveraged wherever possible to avoid reinventing the wheel. This ensures alignment with established best practices and reduces analysis design effort.
* **Develop a New Model**: When no existing analysis model accurately fits the unique requirements of the project, collaborate with project engineers and domain experts to design a custom model. Use iterative testing (e.g., applying models to historical projects) to verify its validity and suitability.

#### **3.2 Simplifying Analysis Models**

Avoid overly complex analysis procedures that incorporate excessive or extraneous parameters, making the tools impractical or difficult to manage:

* Focus on the most critical metrics that align with project goals.
* Balance simplicity and insight—ensure the analysis models are pragmatic but robust enough to generate actionable results.

#### **3.3 Lines of Code Example**

Lines of Code (LOC) represents a commonly used and often misapplied primitive metric. Since LOC lacks industry-wide consistency in its definition, every project must document the exact method of counting and interpreting LOC (e.g., handling blank lines, counting comments and reused code, etc.) to prevent confusion, misinterpretation, or invalid comparisons.

---

### **4. Performing Effective Metric Analysis**

Ask the following questions to ensure that your analysis aligns with project objectives and delivers meaningful results:

1. **Does the analysis procedure provide additional insight compared to raw data alone?**
2. **Is the resulting information actionable for decision-making?**
3. **Does the analysis process satisfy the software measurement program’s goals?**
4. **Does the analyzed data align with what stakeholders need to know to monitor progress or mitigate risks?**

---

### **5. Supporting Decision-Making with Metrics**

Effective analysis of software measurement data should directly support technical and managerial decision-making. SWE-093 emphasizes the importance of using metrics to identify risks, predict future project behavior, and assess overall project health:

* **Control Metrics**: Monitor software processes and highlight areas where corrective action is required (e.g., rising defect density trends).
* **Evaluation Metrics**: Help managers assess whether current project plans and procedures are meeting objectives.
* **Prediction Metrics**: Support long-term planning and forecasting (e.g., predicting the remaining effort for test execution or completion timelines).

Document clear thresholds, targets, or decision triggers for each metric to ensure results are actionable and facilitate appropriate responses.

---

### **6. Reporting & Presentation of Analysis Results**

* **Visualization**: Present metrics using clear charts, graphs, or dashboards tailored to the audience (e.g., line graphs showing defect trends for engineers, high-level summaries for managers).
* **Consistency**: Ensure that reporting formats follow Center or organizational guidelines to maintain traceability and ensure repeatability.
* **Stakeholder Understanding**: Simplify the presentation of derived metric computations to make results more interpretable to non-technical stakeholders.

---

### **7. Continuous Metric Evaluation**

As projects evolve, the collected metrics and their associated analysis procedures may need refinement. Periodic reviews of metrics must ensure:

* They remain aligned with project and organizational objectives.
* They are adequately addressing emerging challenges or risks.
* They are adaptable to changes in project scale, scope, or technology.

---

### **8. Key References**

To further implement SWE-093 effectively:

* Refer to **SWE-092 (Using Measurement Data)** for guidance on tailoring measurement data to specific project needs.
* Review **5.05 (Software Metrics Report)** for reporting and format standards.
* Use **NASA Software Measurement Guidebook** for examples of existing metrics and their analysis methods.
* Explore **SWE-090 (Management and Technical Measurements)** for defining the measurement objectives driving metric selection.

---

### **Conclusion**

By combining appropriate metrics with robust, documented analysis procedures, SWE-093 ensures the transformation of raw software measurement data into actionable insights. These insights guide project health assessments, improve decision-making, and promote a culture of data-driven risk management. Clear traceability, stakeholder engagement, and continuous refinement of metrics are the cornerstones of successful compliance with SWE-093.

SWE-093 requires the analysis of the collected software measurements with the documented project-specified and Center and organizational analysis procedures. Implicit in the requirement is the need to investigate, evaluate and select the appropriate analysis procedures and software metrics. The Software Development (SDP) or Management Plan (see [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)) lists software metrics as part of the SDP content. This indicates the need to develop the software metrics for the project early in the software development life cycle. The evolution of the software development project and its requirements may necessitate a similar evolution in the required software measures and software metrics (see [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data)). See also Topic [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects), [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report),

Good metrics facilitate the development of models that are capable of predicting process or product parameters, not just describing them.

See also [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis).

See [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data)).

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics). |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics) |

# 4. Small Projects

For small projects, while **SWE-091** allows flexibility in the type and frequency of measures to be recorded, the project must still collect and analyze selected software measurement data to develop essential software metrics. The success of even small projects depends on leveraging these metrics to monitor progress, manage risks, and ensure software quality.

Here is improved guidance to help small projects optimize their measurement and analysis efforts:

---

### **1. Tailored Data Collection and Analysis**

* **Focus on Key Metrics**: Small projects often have limited resources, so it is essential to focus on a minimal but impactful set of software metrics that align with project goals and critical success factors. Examples:
  + Defect density.
  + Test coverage.
  + Requirements volatility.
  + Schedule adherence.
* **Adjust Measurement Intervals**: Collect data at intervals that reflect the pacing of project milestones, ensuring resource efficiency without sacrificing visibility into critical risks.
  + Example: Weekly collection during high-risk phases, and biweekly or milestone-based collection during lower-risk phases.

---

### **2. Reuse of Existing Analysis Procedures**

* **Leverage Existing Resources**: Use previously defined analysis procedures from prior projects or organizational repositories to save time and reduce the effort required to develop new processes. This also ensures alignment with organizational standards.
  + Example: Consult organizational best practices, metrics guidelines, or procedures documented in the **NASA Software Measurement Guidebook**.
* **Simplify Procedures**: Select straightforward analysis methods that balance simplicity and value. For example, trend analysis of defect reduction or velocity tracking for agile projects can provide actionable insights with minimal overhead.

---

### **3. Automation and Tool Support**

Small projects can significantly reduce manual effort and errors by using tools and automation for collecting, analyzing, and reporting metrics.

* **Utilize Development Tools**: Environments such as **JIRA** and their associated plug-ins can automate the tracking and reporting of development metrics, such as:
  + Story point completion rates.
  + Average time to resolve issues.
  + Defect trends over iterations.
* **Configuration Management Systems**: Tools like Git, Bitbucket, or equivalent configuration management systems can provide automated insights into code changes, commits, and even peer review activity.
* **Automated Collection and Distribution**: Many tools offer built-in reporting and dashboard capabilities to streamline the sharing of analysis results with stakeholders, reducing manual workload.

---

### **4. Practical Considerations for Small Projects**

* **Balance Effort and Value**: Small projects should prioritize collecting and analyzing metrics that provide the most value relative to their size and scope. Data collection should not overwhelm development efforts but should still ensure key risks and constraints are actively monitored.
* **Start Small, Evolve Over Time**: Begin with minimal but high-impact metrics, and further refine or expand the metrics suite as the project progresses or risks/needs evolve.

---

### **Summary**

For small projects, SWE-091 promotes resource-efficient measurement programs that still deliver actionable insights. By focusing on essential metrics, reusing existing analysis procedures, and leveraging tools like **JIRA** or configuration management systems, small projects can streamline data collection and analysis, minimize overhead, and maintain high standards for software quality and delivery success. Automation, combined with a tailored approach to metrics, ensures that small projects remain nimble while still fulfilling critical measurement requirements.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-137) Boeing Houston Site Metrics Manual, HOU-EGM-308, January 17, 2002. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-146)

  [Estimating Software Costs: Bringing Realism to Estimating,](http://www.amazon.com/dp/0071483004/ref=rdr_ext_tmb "Click to open in new window")

  Capers Jones, 2007, McGraw Hill, New York.
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-222)

  [IEEE Computer Society, "IEEE Standard Glossary of Software Engineering Terminology,"](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=2238 "Click to open in new window")

  IEEE STD 610.12-1990, 1990. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-236)

  [Programming Productivity,](https://books.google.com/books/about/Programming_Productivity.html?id=CIxQAAAAMAAJ "Click to open in new window")

  Jones, Capers (1986), McGraw Hill, New York.
* (SWEREF-252)

  [Software Metrics: SEI Curriculum Module SEI-CM-12-1.1.](http://www.sei.cmu.edu/reports/88cm012.pdf "Click to open in new window")

  Mills, Everald E. (1988). Carnegie-Mellon University-Software Engineering Institute.  Retrieved on December 2017 from http://www.sei.cmu.edu/reports/88cm012.pdf.
* (SWEREF-297)

  [Practical Implementation of Software Metrics.](https://books.google.com/books/about/Practical_Implementation_of_Software_Met.html?id=SaVQAAAAMAAJ "Click to open in new window")

  Paul Goodman (1993). London: McGraw Hill. Available in ACM digital Library at: https://dl.acm.org/citation.cfm?id=541761
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
* (SWEREF-567)

  [Know How Your Software Measurement Data Will Be Used](https://llis.nasa.gov/lesson/1772 "Click to open in new window")

  Public Lessons Learned Entry: 1772.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

Capturing accurate and well-defined software measurement data is critical for supporting Center/organizational needs, especially in the context of cost estimation and project reviews. Lessons learned from past NASA projects highlight the importance of aligning measurement data definitions and usage expectations to avoid misinterpretations, inefficiencies, and conflicts during key reviews.

---

#### **Key NASA Lesson Learned**

**Title:** "Know-How Your Software Measurement Data will be Used"  
**Lesson No. 1772**

During the Mars Science Laboratory (MSL) flight project, software measurement data related to estimated **source lines of code (SLOC)** was submitted in the **Cost Analysis Data Requirement (CADRe)** to the Independent Program Assessment Office (IPAO). This data was used as input for a parametric cost estimation model. However, inconsistencies in the data's interpretation resulted in significant disagreements between the cost office's estimate and the project's software cost estimate. Specifically:

* The project reported **physical SLOC values**, which were misinterpreted as **logical SLOC counts** in the cost model, leading to a **50% higher cost estimate**.
* Reconciliation of this discrepancy required substantial time and effort, delaying the clarity and acceptance of the resulting cost estimate.

#### **Lesson Summary:**

Before submitting software cost estimate data (e.g., total SLOC estimations, software reuse information) to NASA or other organizational entities, verify **how the recipient plans to interpret and use the data** in their cost estimation models. To preclude misinterpretation:

1. Clearly describe the **definitions** and **parameters** of the provided metrics.
2. Ensure alignment between the project's reporting methods and the organization's interpretation processes (e.g., specify physical SLOC vs. logical SLOC).
3. Consider duplicating the NASA cost estimation process using the same parametric model or equivalent tools. This enables comparison, validation, and reconciliation of results before submission.

---

**Poor Metrics and Lack of Visibility into Software Health**

**Incident:**  
Psyche’s project metrics masked true software progress. Software risk was consistently under‑reported due to an aversion to categorizing issues as “red,” preventing leadership from recognizing schedule‑threatening problems.

**Lesson Learned:**

* **Objective Software Metrics:** Software maturity must be tracked using measurable indicators such as defect trends, verification progress, and test coverage.
* **Risk Transparency:** Leadership must encourage open reporting and avoid cultural pressures that suppress accurate risk assessments.

**Implication:**  
When metrics fail to reflect reality, management loses the ability to make timely decisions, creating preventable launch‑critical failures.

### **Additional Lessons and Recommendations**

Expanding on Lesson No. 1772, the following considerations have been derived from other documented NASA experiences and industry best practices:

---

#### **1. Standardize Metric Definitions**

One consistent challenge is the absence of universally accepted definitions for software metrics, such as **lines of code** (physical versus logical), defect classifications, or productivity rate calculations. To avoid confusion:

* **Develop and Communicate Clear Definitions:** Document and explicitly define all metrics (e.g., physical vs. logical SLOC) to ensure stakeholders interpret measurements uniformly. These definitions should accompany all reports and estimates.
* **Adopt Established Standards:** Where possible, reference recognized standards (e.g., ISO/IEC standards, NASA Software Measurement Guidebook) to ensure common interpretation.

---

#### **2. Perform Metric Verification and Validation**

Before submitting measurement data for flight reviews, assessments, or cost modeling purposes:

* **Conduct Internal Validation:** Verify collected and reported metrics against historical data, expected trends, or benchmarks (for similar missions or organizations).
* **Crosscheck Against Models:** Test parametric models similar to the organization's model to identify discrepancies between inputs and outputs. Allow sufficient time for reconciliation.

Lesson Example from NASA:

* Earlier projects have shown that discrepancies in defect classification and severity estimations led to overstated risk projections. Reconciliation required involving software assurance teams during early review stages, preventing costly delays.

---

#### **3. Engage Stakeholders Early**

* Collaborate with recipients (e.g., IPAO, cost offices) **early in the process** to ensure mutual understanding of measurement needs, reporting requirements, and expected usage.
* For projects exceeding $500 million, these proactive conversations can align expectations and avoid high-profile misunderstandings during critical reviews.

---

#### **4. Select Measurement Tools Carefully**

Utilize measurement tools that support accuracy, traceability, and standardized reporting.

* Many modern tools (e.g., automated code analysis tools like SonarQube or software repositories like Git and Bitbucket) can provide reliable measurements for parameters such as SLOC, defect rates, and reuse rates.
* Tools should include mechanisms for **data export** or **report generation** in formats compatible with cost estimation models.

---

#### **5. Plan for Measurement Evolution**

Measurement needs often change as projects grow in complexity. Early metrics, such as SLOC estimates, may require refinement or updates during later stages of development. Having processes in place for updating measurement definitions and estimates can improve data quality over time and minimize disagreements.

---

#### **6. Train Team Members on Metric Usage**

Teams responsible for reporting software metrics should be competent in both their collection and their interpretation. Provide training to software engineers, managers, and analysts on how data will be used downstream, especially in cost modeling.

---

#### **7. Learn from Historical Cases**

NASA’s Lessons Learned database provides valuable insights into common pitfalls and best practices. Regular reviews of past experiences, such as misinterpretation or incorrect application of measurement data, can inform current projects to avoid repeating mistakes.

---

### **Common Risks and Mitigation Strategies**

| **Risk** | **Impact** | **Mitigation Strategy** |
| --- | --- | --- |
| Metric misinterpretation (e.g., SLOC type) | Inflated cost estimates | Clearly define measurement parameters and crosscheck project and NASA estimation models before submission. |
| Ambiguous reporting formats | Delays in review or reconciliation | Standardize reporting templates and formats with clear definitions for metrics generated from tools or manual processes. |
| Insufficient stakeholder collaboration | Misaligned expectations | Engage stakeholders early to align on expectations, definitions, and interpretation methodologies before major reviews or submissions. |
| Evolving metrics during development | Outdated or invalid metrics | Establish a process for updating and refining metrics to accommodate project changes (e.g., increased scope, new requirements, technical complexities). |

---

### **Summary**

The lesson from the Mars Science Laboratory (MSL) emphasizes the importance of clear and consistent definitions for software measurement data to avoid misinterpretations during cost estimation and mission reviews. Further lessons from NASA experiences highlight forward-thinking strategies such as verifying parametric models, aligning stakeholders early, and simplifying data reporting to avoid delays and disputes in high-stakes reviews.

By defining metrics clearly, validating their usage, and maintaining robust reporting standards, projects can ensure accurate communication, reduce risks, and facilitate collaborative success across NASA's Centers and independent review offices.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Collect lessons learned about CCSDS File Delivery Protocol (CFDP)](https://software.gsfc.nasa.gov/lesson-details/75/). **Lesson Number 75**: The recommendation states: "Collect lessons learned and strategies for how to best use CFDP now that we have experience on multiple missions."
* [Gather lessons learned throughout the project life cycle](https://software.gsfc.nasa.gov/lesson-details/110/). **Lesson Number 110**: The recommendation states: "Gather lessons learned throughout the project life cycle."

# 7. Software Assurance

**SWE-093 - Analysis of Measurement Data**

5.4.3 The project manager shall analyze software measurement data collected using documented project-specified and Center/organizational analysis procedures.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm software measurement data analysis conforms to documented analysis procedures.

2. Analyze software assurance measurement data.

## 7.2 Software Assurance Products

Software assurance (SA) plays a critical role in verifying that software development activities align with measurement and analysis requirements, ensuring that risks, issues, and trends are promptly identified and mitigated. To improve this guidance, we will provide clarity, structure, and actionable best practices for SA professionals involved in the analysis and oversight of software metrics across the lifecycle.

Software assurance products include measurement and metric analysis results, audit findings, and ongoing evaluation of software against project requirements. These outputs provide actionable insights into project health and compliance.

#### **Updated List of Software Assurance Products**:

1. **Software Measurement or Metric Data**:

   * Includes raw data directly collected from development and assurance processes (e.g., defect counts, peer review results, test coverage rates, schedule adherence rates).
   * Data should be accompanied by clear definitions to avoid ambiguity or misinterpretation.
2. **Integrated Trends and Analysis Results**:

   * Represents overall trends (e.g., rising defect density, declining test progress) and aggregated insights across the metric set.
   * Trends must be interpreted within the context of project objectives (e.g., conformance to safety-critical requirements, adherence to schedules).
3. **Status Presentations**:

   * Compiled reports or dashboards displaying:
     + Key metrics (e.g., defect closure rates, requirement verification status).
     + Emerging trends to highlight ongoing risks or upcoming concerns (e.g., schedule forecast slips).
   * Should include comparisons against baselines, thresholds, and targets.
4. **Audit Reports on Software Metric Processes** (`Verification Artifacts`):

   * Documents detailing findings from software assurance audits of metric collection, analysis, and reporting processes.
   * Focus areas include adherence to documented procedures, consistency, traceability, and alignment with project assurance plans.

## 7.3 Metrics

Metrics are essential tools for assessing performance, status, and areas of concern in both software development and assurance processes. The guidance expands on suggested measures and best practices.

#### **Updated Examples of SA Metrics**:

Software assurance metrics should be tailored to support tracking of critical elements, focusing on areas such as project performance, software quality, and compliance with requirements. Suggested metrics include:

1. **Key Status Metrics**:

   * **Schedule Deviations**: Number or percentage of tasks falling behind schedule, including analysis of the impact on overall project milestones.
   * **Corrective Action Closure**: Tracking the resolution time for identified issues and defects.
   * **Defect Trends**: Quantity/quality trends of software defects discovered across testing phases (e.g., unit, integration, acceptance).
   * **Peer Review Coverage**: Percentage of code or requirements reviewed and defect density identified during reviews.
2. **Audit Metrics**:

   * Product and process audit results, capturing adherence to requirements, standards, and procedures.
   * Peer reviews, including planned versus executed reviews and corrective actions taken after findings.
3. **SA Task Execution Metrics**:

   * Completion rates of planned software assurance activities (e.g., audits, reviews, testing oversight) versus actual activities performed.
   * Identification of gaps between planned and completed tasks and associated impacts.
4. **SA Effectiveness Metrics**:

   * Proactive identification of risks or defects before system testing, indicating the quality of early-phase assurance activities.
   * Reduction in downstream issues tied to software assurance feedback.

#### **Additional Metrics Categories**:

Metrics can also support:

* **Prediction and Trend Forecasting**: Predict future risks in software performance or delivery timelines based on current trends (e.g., defect rate prediction using historical metrics).
* **Root Cause Analysis Insights**: Identification of systemic concerns (e.g., recurring defects originating in requirements analysis phase) to support process improvement.

## 7.4 Guidance

Tasks related to software assurance should focus on understanding and using software metrics to make actionable corrections in assurance work while supporting project compliance and process improvement.

---

#### **Task 1: Oversight of Project's Measurement Analysis Procedures**

**SA Review Goals**:

* Confirm that the **software development plan/software management plan** or **measurement plan** includes documented procedures for software metric analysis.
  + Determine if the procedures were adopted from an Agency, Center, or project library or developed project-specific analysis methods.
* Validate implementation of these analysis procedures in the project's activities:
  + Ensure that **analysis of collected measures** has adhered to documented procedures.
  + When project measures exceed pre-established thresholds, confirm that root causes have been analyzed thoroughly and corrective actions have been defined to mitigate the issue.

**Key Steps**:

1. Verify that analysis procedures include evaluation mechanisms for detecting threshold violations (e.g., predefined defect density limits or schedule slippage rates).
2. Assess whether corrective actions address the root causes (e.g., insufficient resources, coding errors) effectively and prevent recurrence.
3. Ensure findings and corrective actions are traceable in project reporting and assurance metrics.

#### **Task 2: Software Assurance’s Independent Metric Analysis**

**SA Evaluation Goals**: Software assurance is responsible for analyzing *its own measurement data* independently using procedures documented in the **software assurance plan**. The focus is to proactively flag risks and recommend corrective actions.

**Key Focus Areas**:

1. **Analyzing Trends**:

   * Identify concerning trends in SA activity performance, software product quality, or process adherence (e.g., late delivery of SA activities, uncovering systemic defects in audits or reviews).
   * Pay special attention to trends that could impact project outcomes, such as defects surfacing late in the lifecycle or repeated deviations from scheduled tasks.
2. **Root Cause Analysis**:

   * Investigate undesirable trends or anomalies (e.g., increased schedule deviations or low peer review coverage rates).
   * Identify **causal factors** (e.g., staffing shortages, overlooked requirements complexity, poor communication).
   * Collaborate with the project team to plan corrective actions targeted at eliminating the identified root causes.
3. **Corrective Actions**:

   * Develop actionable improvements to address assurance gaps (e.g., increasing staff for reviews, scheduling additional testing oversight).
   * Monitor the implementation of corrective actions to verify their effectiveness.
4. **Metrics Interpretation Example**:  
   Suppose SA charts reveal that **SA activities performed vs. scheduled SA tasks** show a consistent lag:

   * Analyze the reasons behind the lag (staffing issues, unplanned work, project delays).
   * Recommend adjustments, such as reprioritizing assurance activities, adding staff, or extending schedules to match project needs.

#### **Additional Actions**:

* Regularly present **SA findings** to stakeholders using clear visualization methods (e.g., trend charts, risk dashboards, bar graphs highlighting deviations).
* Monitor progress on proposed corrective actions to assess whether assurance metrics improve post-implementation.

---

### **Lessons Learned**

To ensure high-quality assurance outcomes based on metrics:

1. **Collaborate Closely with Project Teams:** Jointly analyze deviations, root causes, and corrective actions to improve coordination and alignment.
2. **Start Metrics Early:** Collect assurance metrics from the beginning of the lifecycle to monitor trends and risks before significant issues arise.
3. **Automate Where Possible:** Use tools such as dashboards and trending software (e.g., JIRA plugins, code analysis tools) to simplify and accelerate analysis/reporting for assurance activities.
4. **Plan for Evolving Metrics:** Update SA metrics and analysis procedures as the project progresses or changes in scope occur, ensuring they remain relevant to emerging risks.

---

### **Summary of Software Assurance Guidance**

Software assurance should focus on monitoring and analyzing key metrics related to software performance, schedule deviations, compliance, and assurance tasks. SA teams must verify adherence to documented procedures, conduct independent metric analyses, and identify actionable corrective actions when anomalies or undesirable trends arise. Clear communication with stakeholders, proactive planning, and continuous refinement of metrics are foundational to effective software assurance. This guidance ensures traceability, robust risk mitigation, and improved assurance quality across projects.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)        * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics). |

# 8. Objective Evidence

Objective Evidence

Objective evidence demonstrates compliance with **SWE-093**, which requires the analysis of software measurement data using documented project-specified, Center, or organizational analysis procedures. The evidence ensures that the data analysis activities are systematic, repeatable, traceable, and effective. Below are examples of objective evidence that can be provided to verify compliance:

---

### **1. Documented Procedures for Metric Analysis**

* **Documents**:
  + The **Software Development Plan (SDP)** or **Software Management Plan (SMP)** containing the documented procedures for analyzing metrics.
  + A **Measurement Plan** that describes the types of metrics to be collected, analysis methods, thresholds, and corrective actions.
  + The **Software Assurance Plan**, detailing assurance-specific analysis procedures, including root cause analysis protocols.
  + Organizational standards or guidelines related to software measurement analysis, such as those from the **NASA Software Measurement Guidebook**.

---

### **2. Defined and Updated Measurement Metrics**

* **Artifacts**:
  + A list of metrics collected for the project, categorized as **primitive metrics** (e.g., defect counts, SLOC, execution time) and **derived metrics** (e.g., defect density, productivity).
  + Metric definitions and calculations, including any algorithms and formulas used to compute derived metrics.
  + Documentation of thresholds or limits for metrics (e.g., maximum defect density before triggering corrective action).

---

### **3. Reports and Presentations**

* **Artifacts**:
  + **Analysis Reports** detailing the interpretation of collected data, comparisons against baselines, trends, and identified risks/issues.
  + Periodic **status reports**, **dashboards**, or **graphics** describing metric trends (e.g., defect curves, test progress, schedule adherence trends) provided to stakeholders.
  + Presentation materials showing metric data and trends (e.g., charts, bar graphs, tables) shared in reviews such as **Preliminary Mission & Systems Review (PMSR)** or **Critical Design Review (CDR)**.

---

### **4. Root Cause Analysis Documentation**

* **Artifacts**:
  + Documentation showing investigations into anomalies or threshold violations (e.g., defect spikes, schedule slips).
  + Root cause analysis reports identifying the reasons for metric deviations and actionable steps for mitigation.
  + Logs of actions taken to address trends or anomalies, including planned and completed corrective actions.

---

### **5. Audit Reports**

* **Artifacts**:
  + **SA audit reports** verifying that the project followed documented metric analysis procedures.
  + Audit reports specifically focused on data integrity and consistency of measurement practices (e.g., adherence to defined thresholds, appropriate interpretation of metrics).
  + Findings from audits or inspections showing compliance with project-specific and organizational metrics analysis requirements.

---

### **6. Historical Data and Trends**

* **Artifacts**:
  + Time-series data related to metrics collected over the lifecycle (e.g., defect trends over iterations, productivity changes over time).
  + Benchmarking analyses comparing project metrics against previous missions or similar projects.
  + Graphs, charts, or dashboards showing historical trends (e.g., defect density reduction, testing progress, requirement volatility trends).

---

### **7. Corrective Action Records**

* **Artifacts**:
  + Records of corrective actions initiated in response to metric threshold violations or analysis findings (e.g., additional testing resources allocated after test coverage trends fell below thresholds).
  + Documentation linking the outcome of corrective actions to improved metric trends or project performance.

---

### **8. Meeting Minutes**

* **Artifacts**:
  + Minutes from review or status meetings where metrics were discussed, analyzed, and correction plans were developed.
  + Records of decisions made in meetings to address risks or issues identified through metric analysis.

---

### **9. Tools and Automation Artifacts**

* **Artifacts**:
  + Evidence of the use of tool-generated metric reports (e.g., from tools like JIRA, SonarQube, Git, or dashboards tied to configuration management systems).
  + Logs or outputs showing automated collection, analysis, and reporting of metrics.

---

### **10. Validation of Procedures**

* **Artifacts**:
  + Test results or reviews demonstrating the validity of the analysis procedures used for interpreting metric data (e.g., consistency of trends with expected outcomes or model predictions).
  + Proof of alignment between raw data inputs and analysis results (e.g., matching physical versus logical SLOC counts).

---

### **11. Miscellaneous Evidence**

* **Artifacts**:
  + Training materials provided to team members regarding metric definitions, collection processes, or analysis procedures.
  + Approval records or signatures from stakeholders confirming acceptance of metric analysis results for final reports.

---

### **Examples of Objective Evidence**

#### **Example 1: Software Quality Metrics Report**

An analysis report that includes metrics such as defect density, requirement volatility trends, and code coverage measures, presented with corresponding graphs and interpretations. The report highlights violations of thresholds, their root causes, and implemented corrective actions.

#### **Example 2: Root Cause Analysis Report**

A detailed investigation of increasing defect density during system testing, identifying the root cause as inadequate test coverage during unit testing. The report outlines corrective actions such as targeted testing and additional resources, as well as follow-up metric analysis to measure improvement.

#### **Example 3: Tools and Dashboards**

Screenshots or exports from automated tools (e.g., JIRA) showing workflow progress, defects logged and resolved, and team velocity. Accompanied by automated trend charts comparing development milestones and team performance metrics.

---

By providing this objective evidence, projects can ensure compliance with SWE-093, demonstrate that software measurement data has been correctly analyzed, and confirm alignment with project and organizational procedures. This documentation also supports audits, reviews, and validates the use of metrics in guiding corrective actions and improving processes.

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
