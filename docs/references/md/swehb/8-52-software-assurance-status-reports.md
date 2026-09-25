# 8.52 - Software Assurance Status Reports

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695754. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports

8.52 - Software Assurance Status Reports

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695754)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695754&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Recommended Content](#tabs-2)
* [3. High Level Summary](#tabs-3)
* [4. SA Analyses](#tabs-4)
* [5. SA Assessments](#tabs-5)
* [6. SA Audits](#tabs-6)
* [7. Resources](#tabs-7)

Return to [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products)

# 1. Introduction

A primary function of software assurance is to help determine the status of the software project and the quality of the products being produced. The Status Report is a scheduled periodic communication tool to help manage expectations between the SA and Safety Assurance representative(s), project engineering and management, and OSMA stakeholders. It provides insight into the overall status relative to the value SA adds to the project as well as performance against the SA plan. Pre-coordinate with the stakeholders receiving the status reports and define the specifics/content of the status report in the SA Plan. Status reports should provide the information to satisfy the needs of the stakeholders receiving the report. The SA teams will probably be participating in status reporting presented during reviews, such as the milestone reviews and they should also be giving status reports to their management, the project management, and certain other stakeholders more frequently to keep them well informed. When SA has findings or issues of potential high risk, they should not wait until the regularly scheduled status reports to bring those to management.

The information in this topic is divided into several tabs as follows:

* Tab 1 – Introduction
* Tab 2 – Recommended Content – provides guidance on the minimum SA Status report product content (Note: The contents in Tab 2 was previously in 7.18 as SASTATUS.)
* Tab 3 – High Level Summary – provides additional guidance and examples of high-level summary of SA activities that may be included in the status report when the reporting time slot is very short.
* Tab 4 – SA Analysis – provides reporting guidance on analyses performed during a reporting period
* Tab 5 – SA Assessments – provides guidance on assessments performed and reporting on them
* Tab 6 – SA Audits – provides reporting guidance on audits performed during a reporting period
* Tab 7 – Resources for this topic

The following is a list of the applicable SWE requirements that relate to the generation of SA Status Reports:

|  |  |  |
| --- | --- | --- |
| **SWE #** | **NPR 7150.2 Requirement [083](#_tabs-<p>7</p>)** | **NASA-STD-8739.8 Software Assurance and Software Safety Tasks  [278](#_tabs-<p>7</p>)** |
| 033 | 3.1.2 The project manager shall assess options for software acquisition versus development.    Notes:      a. Acquire an off-the-shelf software product that satisfies the requirement.      b. Develop a software product or obtain the software service internally.      c. Develop the software product or obtain the software service through contract.      d. Enhance an existing software product or service.      e. Reuse an existing software product or service.      f. Source code available external to NASA. | 3. Assess any risks with acquisition versus development decision(s). |
| 024 | 3.1.4 The project manager shall track the actual results and performance of software activities against the software plans.   1. 1. Corrective actions are taken, recorded, and managed to closure.    2. Changes to commitments (e.g., software plans) that have been agreed to by the affected groups and individuals are taken, recorded, and managed. | 1. Assess plans for compliance with NPR 7150.2 requirements, NASA-STD-8739.8, including changes to commitments. |
| 034 | 3.1.5 The project manager shall define and document the acceptance criteria for the software. | 1. Confirm software acceptance criteria are defined and assess the criteria based on guidance in the NASA Software Engineering Handbook, NASA-HDBK-2203. |
| 037 | 3.1.7 The project manager shall define and document the milestones at which the software developer(s) progress will be reviewed and audited. | 2. Participate in project milestones reviews. |
| 039 | 3.1.8 The project manager shall require the software developer(s) to periodically report status and provide insight into software development and test activities; at a minimum, the software developer(s) will be required to allow the project manager and software assurance personnel to:   1. 1. Monitor product integration.    2. Review the verification activities to ensure adequacy.    3. Review trade studies and source data.    4. Audit the software development processes and practices.    5. Participate in software reviews and technical interchange meetings. | 1. Confirm that software developer(s) periodically report status and provide insight to the project manager.    2. Monitor product integration.  3. Analyze the verification activities to ensure adequacy.  4. Assess trade studies, source data, software reviews, and technical interchange meetings.  6. Develop and provide status reports.  7. Develop and maintain a list of all software assurance review discrepancies, risks, issues, findings, and concerns. |
| 139 | 3.1.11 The project manager shall comply with the requirements in this NPR that are marked with an “X” in Appendix C consistent with their software classification. | 1. Assess that the project's software requirements, products, procedures, and processes are compliant with the NPR 7150.2 requirements per the software classification and safety criticality for software. |
| 151 | 3.2.2 The project manager’s software cost estimate(s) shall satisfy the following conditions:   a. Covers the entire software life cycle. b. Is based on selected project attributes (e.g., programmatic assumptions/constraints, assessment of the size, functionality, complexity, criticality, reuse code, modified code, and risk of the software processes and products). c. Is based on the cost implications of the technology to be used and the required maturation of that technology. d. Incorporates risk and uncertainty, including end state risk and threat assessments for cybersecurity. e. Includes the cost of the required software assurance support. f. Includes other direct costs. | 1. Assess the project's software cost estimate(s) to determine if the stated criteria listed in "a" through "f" are satisfied. |
| 016 | 3.3.1 The project manager shall document and maintain a software schedule that satisfies the following conditions:   1. 1. Coordinates with the overall project schedule.    2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.    3. Reflects the critical dependencies for software development activities.    4. Identifies and accounts for dependencies with other projects and cross-program dependencies. | 1. Assess that the software schedule satisfies the conditions in the requirement.  2. Develop a software assurance schedule, including software assurance products, audits, reporting, and reviews. |
| 205 | 3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each software component is considered to be safety-critical per the criteria defined in NASA-STD-8739.8. | 2. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.  3. Assess that hazard analyses (including hazard reports) identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.  5. Develop and maintain a software safety analysis throughout the software development life cycle. |
| 134 | 3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:   a. The software is initialized, at first start and restarts, to a known safe state. b. The software safely transitions between all predefined known states. c. Termination performed by software functions is performed to a known safe state. d. Operator overrides of software functions require at least two independent actions by an operator. e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard. f. The software detects inadvertent memory modification and recovers to a known safe state. g. The software performs integrity checks on inputs and outputs to/from the software system. h. The software performs prerequisite checks prior to the execution of safety-critical software commands. i. No single software event or action is allowed to initiate an identified hazard. j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event. k. The software provides error handling. l. The software can place the system into a safe state. | 5. Participate in software reviews affecting safety-critical software products. |
| 146 | 3.8.1 The project manager shall define the approach to the automatic generation of software source code including:   a. Validation and verification of auto-generation tools. b. Configuration management of the auto-generation tools and associated data. c. Description of the limits and the allowable scope for the use of the auto-generated software. d. Verification and validation of auto-generated source code using the same software standards and processes as hand-generated code. e. Monitoring the actual use of auto-generated source code compared to the planned use. f. Policies and procedures for making manual changes to auto-generated source code. g. Configuration management of the input to the auto-generation tool, the output of the auto-generation tool, and modifications made to the output of the auto-generation tools. | 1. Assess that the approach for the auto-generation software source code is defined, and the approach satisfies at least the conditions “a” through “g.” |
| 032 | 3.9.2 The project manager shall acquire, develop, and maintain software from an organization with a non-expired CMMI-DEV rating as measured by a CMMI Institute Certified Lead Appraiser as follows:   1. 1. For Class A software: CMMI-DEV Maturity Level 3 Rating or higher for software.    2. For Class B software (except Class B software on NASA Class D payloads, as defined in NPR 8705.4): CMMI-DEV Maturity Level 2 Rating or higher for software. | 2. Assess potential process-related issues, findings, or risks identified from the CMMI assessment findings. |
| 054 | 4.1.6 The project manager shall identify, initiate corrective actions, and track until closure inconsistencies among requirements, project plans, and software products. | 3. Assess any risks with acquisition versus development decision(s).  1. Monitor identified differences among requirements, project plans, and confirm differences are addressed and corrective actions are tracked until closure. |
| 143 | 4.2.4 The project manager shall perform a software architecture review on the following categories of projects:   a. Category 1 Projects as defined in NPR 7120.5. b. Category 2 Projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4. | 1. Assess the results of or participate in software architecture review activities held by the project. |
| 191 | 4.5.11 The project manager shall plan and conduct software regression testing to demonstrate that defects have not been introduced into previously integrated or tested software and have not produced a security vulnerability. | 3. Identify any risks and issues associated with the regression test set selection and execution. |
| 075 | 4.6.2 The project manager shall plan and implement software operations, maintenance, and retirement activities. | 1. Assess the maintenance, operations, and retirement plans for completeness of the required software engineering and software assurance activities. |
| 079 | 5.1.2 The project manager shall develop a software configuration management plan that describes the functions, responsibilities, and authority for the implementation of software configuration management for the project. | 1. Assess that a software configuration management plan has been developed and complies with the requirements in NPR 7150.2 and Center/project guidance. |
| 081 | 5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project. | 2. Assess that the software safety-critical items are configuration-managed, including hazard reports and safety analysis. |
| 045 | 5.1.9 The project manager shall participate in any joint NASA/developer audits. | 1. Participate in or assess the results from any joint NASA/developer audits. Track any findings to closure. |
| 086 | 5.2.1 The project manager shall record, analyze, plan, track, control, and communicate all of the software risks and mitigation plans. | 1. Confirm and assess that a risk management process includes recording, analyzing, planning, tracking, controlling, and communicating all software risks and mitigation plans. |
| 090 | 5.4.2 The project manager shall establish, record, maintain, report, and utilize software management and technical measurements. | 2. Perform trending analyses on metrics (quality metrics, defect metrics) and report. |
| 093 | 5.4.3 The project manager shall analyze software measurement data collected using documented project-specified and Center/organizational analysis procedures. | 2. Analyze software assurance measurement data. |
| 199 | 5.4.5 The project manager shall monitor measures to ensure the software will meet or exceed performance and functionality requirements, including satisfying constraints. | 2. Monitor and track any performance or functionality requirements that are not being met or are at risk of not being met. |
| 200 | 5.4.6 The project manager shall collect, track, and report software requirements volatility metrics. | 2. Analyze software volatility metrics to evaluate requirements stability as an early indicator of project problems. |
| 202 | 5.5.2 The project manager shall define and implement clear software severity levels for all software non-conformances (including tools, COTS, GOTS, MOTS, OSS, reused software components, and applicable ground systems). | 2. Assess the application and accuracy of the defined severity levels to software non-conformances.    4. Maintain or access the number of software non-conformances at each severity level for each software configuration item. |
| 204 | 5.5.4 The project manager shall implement process assessments for all high-severity software non-conformances (closed-loop process). | 1. Perform or confirm that a root cause analysis has been completed on all identified high severity software non-conformances, and that the results are recorded and have been assessed for adequacy.    3. Assess opportunities for improvement on the processes identified in the root cause analysis associated with the high severity software non-conformances.   4. Perform or confirm tracking of corrective actions to closure on high severity software non-conformances. |

## 1.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 2. Recommended Content

## 2.1 Software Assurance Status Report

This is a scheduled periodic communication to help manage expectations between the SA and Safety Assurance representative(s) and project engineering, project management, and OSMA stakeholders. It provides insight into the overall status of the project and SA’s performance with respect to the SA Plan, and raises the awareness of SA’s overall value. The specific content of the status report is pre-coordinated and defined in the SA Plan. If safety-critical software is involved, SA should consult with Safety Assurance to obtain any safety status contributions.

The Software Assurance Status Reports content, SASTATUS (previously in Topic 7.18), in no specific order, addresses:

1. SA Project Title and Date – Identify the project and the date(s) of the reporting period.
2. Overall Status Dashboard or Stoplight Table – Provide a high-level status of progress, risk, schedule, and whether or not assistance/awareness is required. Typically, a Green/Yellow/Red scheme is used for indicating go, no-go status and approaching minimum threshold or limits. See Tab 3 – High Level Summary for more details.
3. Key Contributions/Accomplishments/Results (Value-Added) – Identify any activities/tasks performed during the reporting period that added value to the project. The reporting should include key SA contributions, accomplishments, and results of SA Tasking activities performed in Table 1 (SA Requirements Mapping Matrix). Examples are:
   1. Analyses performed (e.g., Requirements Analysis, Design Analysis, PHAs, HAs, FMEAs, FTAs, Static Code Analysis) See Tab 4. SA Analysis for more details.
   2. Audits performed (e.g., process, product, PCAs, FCAs) See Tab 6. SA Audits for more details.
   3. Products Reviewed (e.g., Project Plans, SA Plans, Safety Plan, Requirements, Design, Code, Test docs)
   4. Tests witnessed
   5. Assessments performed (e.g., Safety Criticality, Software Classification, Risk, Cybersecurity) See Tab 5. SA Assessments for more details.
4. Current/Slated Tasks – Identify in-work and upcoming assurance activities. Identify (planned and unplanned) software assurance and oversight activities for the next reporting period. Examples are:
   1. Analyses performed (e.g., Requirements Analysis, Design Analysis, PHAs, HAs, FMEAs, FTAs, Static Code Analysis) See Tab 4. SA Analysis for more details.
   2. Audits performed (e.g., process, product, PCAs, FCAs) See Tab 6. SA Audits for more details.
   3. Products Reviewed (e.g., Project Plans, SA Plans, Safety Plan, Requirements, Design, Code, Test docs)
   4. Tests witnessed
   5. Assessments (e.g., Safety Criticality, Software Classification, Risk, Cybersecurity) See Tab 5. SA Assessments for more details.
5. Issue Tracking – Record and track software issues identified until resolved. Track issues by priority status, safety, criticality, or some other criteria combination
6. List of SA Non-Conformances – Record and track all Non-conformances (i.e., SA Findings, Discrepancies, PRs, Defects) identified by SA. Track the non-conformances by priority status, safety, criticality, or some other criteria combination. Follow the progression until resolution. Provide the list (or location) and a high-level closure status (e.g., trend of open versus closed over time of the non-conformances.) For high severity non-conformances, provide a short status and their estimated time to closure.
7. Metrics – Identify the set of SA metrics used and analyzed for the reporting period. At a minimum, collect and report on the list of SA metrics specified in the SA Standard. Include analysis results, trends, or updates and provide supportive descriptions of methodology and criteria. Charts and graphs that show trends (both good and bad) on project activities and products may be useful to convey the data. Since new data may not be available each reporting period, it may be necessary to designate certain reporting periods (e.g., bi-weekly, monthly) for various metrics. Some of the more important metrics should be placed in the section “Overall Status Dashboard or Stoplight Table” discussed above.
8. Process Improvement suggestions and observations.
9. Obstacles/Watch Items – Identify and describe any obstacles, roadblocks, and watch items for the reporting period. Obstacles/Watch Items are an informal list of potential concerns.
10. Risk Summary – List and provide status on SA risks associated with any activities/tasks required by the SA Standard. Highlight status changes and trending. “High” risks should be reviewed periodically.
11. Funding (As Applicable) – Provide funding status and trending information as needed to support the SA tasking for the project. Consider how the data/information can be used for future planning and cost estimating.
12. Schedule – Provide the necessary schedule/information to communicate the status of the SA tasking in support of the scope and timeline established for the project.

## 2.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 3. High Level Summary

In cases where time is critical, it may be necessary to provide management and stakeholders with a high-level SA Status Summary Report. This report should include a brief summary of the activities performed by the Software Assurance or Software Safety personnel during the reporting period to give an overall project status at a glance. (Note: This is not intended to be a substitute for a full status report as described on Tab 2. Recommended Content.)

The specific content of a high-level SA Status Summary Report should be pre-coordinated and agreed to by the customers of the Status Report. Although this Handbook provides a recommended set of content (see below), projects have the liberty to adjust it to meet their specific needs. Any high-risk items or issues should always be included in the status reports as well as any key information from any of the listed analyses that have not been reported on previously or that have provided new information.

When preparing a high-level SA Status Summary Report, the following defines the minimum recommended contents:

* High-level status of progress and schedule. Include:
  + Overall evaluation, based on judgement
  + Issues and concerns,
  + Whether or not assistance/awareness is required.
* High-level summary of work performed – Identify what was done, overall evaluation, and number of findings for:
  + Assessments, analyses, and audits performed
  + Products reviewed, and
  + Number of Tests Witnessed
* High-level summary of work in-progress
* High-level summary of upcoming work
* Major findings and associated risk – These could be newly identified or existing.
* Risk summary – These could be newly identified or high-visibility/high-priority risks.
* Metrics – Current status of findings/corrective actions: open/closed; projection for closure timeframe. For example, a trend chart (e.g., testing progress, non-conformance closure rate), or product quality attributes (# of SA findings per review or audit).

This information could be presented in many ways such as:

* Dashboard or Stoplight Table – Typically, a Green/Yellow/Red scheme is used for indicating go, no-go status and approaching minimum threshold or limits.
* Quad Chart – A chart with 4 sections e.g., Project Status, Work Completed, Upcoming/In-Progress Work, and Risks/Issues/Concerns
* Trend Chart – A chart that shows changes of a metric over time, such as requirements volatility over time or closure of discrepancies over time.
* Burndown Chart – A chart to show project progress (i.e., work completed and work remaining) for a certain time frame. This could be for an entire project or for an Agile sprint.

If major findings or issues are high risk items, they should be reported to management and the development team immediately. Project managers and software leads don’t like to be surprised, so the sooner the issue/risk becomes known, the sooner it can be addressed and the better the chance that the impact can be minimized.

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

See also [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review),

# 4. SA Analysis

What does it mean to perform an “analysis”? The Software Assurance and Software Safety Standard (SASS), NASA-STD-8739.8[278](#_tabs-<p>7</p>), defines “analyze” as:

Review results in-depth, look at relationships of activities, examine methodologies in detail, follow methodologies such as Failure Mode and Effects Analysis, Fault Tree Analysis, trending, and metrics analysis. Examine processes, plans, products, and task lists for completeness, consistency, accuracy, reasonableness, and compliance with requirements. The analysis may include identifying missing, incomplete, or inaccurate products, relationships, deliverables, activities, required actions, etc.

Thus, the analyses performed by Software Assurance and Software Safety personnel are intended to provide an in-depth look at the products generated by the software engineering organization during the software development life cycle. These analyses are more than reviews as they require personnel to study and scrutinize the engineering products to identify strengths and weaknesses (e.g., in the design, code, test coverage, security vulnerabilities, hazard analysis) as well as errors, potential problems, issues and risks. Each required analysis type is covered in detail in other sections of Topic [**8.16 – SA Products**](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) and are listed below:

* [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis)
* [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis)
* [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis)
* [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis)
* [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis)

There are two additional analyses not covered under separate topics that Software Assurance performs. They are:

* Verification Activities Analysis – Software Verification is the “confirmation that products properly reflect the requirements specified for them” – NASA-STD-8739.8. As such, any analysis performed on verification activities should be included in status reporting, particularly if any findings show problems that may be difficult/time-consuming to fix or cause a redesign/or considerable rework.
* Root Cause Analysis – If any root cause analysis has been performed on a high severity non-conformance, report the results as well as the impact on the project, plans to identify similar problems in other areas of the project, and the selected method of preventing similar problems in future projects.

During each status reporting period, a high-level summary of any analysis done during the reporting period should be reported. The specific SA Status Report content for each SA product listed above is defined in the product pages. However, in general, when reporting the results of an analysis in a SA Status Report, the following defines the minimum recommended contents:

* Identification of what was analyzed: Mission/Project/Application
* Period/Timeframe/Phase analysis performed during
* Summary of analysis techniques used
* Overall assessment of the software engineering work product, based on analysis
* Major findings and associated risk
* Current status of findings: open/closed; projection for closure timeframe

If a time-critical issue is uncovered, it should be reported to management immediately so that the affected organization may begin addressing it at once.

## 4.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 5. SA Assessments

What does it mean to perform an “assessment”? The Software Assurance and Software Safety Standard (SASS), NASA-STD-8739.8 [278](#_tabs-<p>7</p>), defines “assess” as:

Judge results against plans or work product requirements. “Assess” includes judging for practicality, timeliness, correctness, completeness, compliance, evaluation of rationale, etc., reviewing activities performed, and independently tracking corrective actions to closure.

Therefore, when performing an assessment/evaluation of a project product or doing a compliance check, SA and Software Safety personnel will use their judgement to determine if the item being evaluated meets expectations.

There are 29 SASS tasks in NASA-STD-8739.8 that require the Software Assurance or Software Safety personnel to “assess” something and another set of tasks where they are required to confirm that an assessment has been done.

The number of assessments required may vary based on the software classification and the approved tailoring of the SWE and SASS requirements in the Requirements Mapping Matrix. When appropriate, each assessment should be performed in the timeframe corresponding to the performance of the associated SWE task. See the table below for the list of required assessments in NASA-STD-8739.8.

The results of any assessments performed are recorded and reported on at either (or both) the next regular management meeting or included in the SA Status Report. Depending on the type of assessment performed, it may be more appropriate to document the results in the associated SA analysis product rather than a status report. For example, an assessment performed on the software architecture (SWE-057) should be documented as part of the [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) product as it is relevant to the overall analysis.  If there is no related SA product, document it separately and include the results in the SA Status Report for the applicable reporting period.

When reporting the results of an assessment in a SA Status Report, the following defines the minimum recommended contents:

* Identification of what was assessed: Mission/Project/Application
* Type of Assessment
* Period/Timeframe/Phase assessment performed during
* Overall evaluation of the assessment target
* Major findings and associated risk
* Current status of findings: open/closed; projection for closure timeframe

Note: Table below was done with NASA-STD-8739.8B draft as of 11/10/21.Will need updating when Rev B is official.

**List of Assessments in NASA-STD-8739.8**

| **SWE #** | **NPR 7150.2 [083](#_tabs-<p>7</p>) Requirement** | **Software Assurance and Software Safety Tasks  - Required assessments** |
| --- | --- | --- |
| 033 | 3.1.2 The project manager shall assess options for software acquisition versus development. | 3. Assess any risks with acquisition versus development decision(s). |
| 024 | 3.1.4 The project manager shall track the actual results and performance of software activities against the software plans.   1. 1. Corrective actions are taken, recorded, and managed to closure.    2. Changes to commitments (e.g., software plans) that have been agreed to by the affected groups and individuals are taken, recorded, and managed. | 1. Assess plans for compliance with NPR 7150.2 requirements, NASA-STD-8739.8, including changes to commitments. |
| 034 | 3.1.5 The project manager shall define and document the acceptance criteria for the software. | 1. Confirm software acceptance criteria are defined and assess the criteria based on guidance in the NASA Software Engineering Handbook, NASA-HDBK-2203. |
| 039 | 3.1.8 The project manager shall require the software developer(s) to periodically report status and provide insight into software development and test activities; at a minimum, the software developer(s) will be required to allow the project manager and software assurance personnel to:   1. 1. Monitor product integration.    2. Review the verification activities to ensure adequacy.    3. Review trade studies and source data.    4. Audit the software development processes and practices.    5. Participate in software reviews and technical interchange meetings. | 4. Assess trade studies, source data, software reviews, and technical interchange meetings. |
| 139 | 3.1.11 The project manager shall comply with the requirements in this NPR that are marked with an “X” in Appendix C consistent with their software classification. | 1. Assess that the project's software requirements, products, procedures, and processes are compliant with the NPR 7150.2 requirements per the software classification and safety criticality for software. |
| 151 | 3.2.2 The project manager’s software cost estimate(s) shall satisfy the following conditions:   a. Covers the entire software life cycle. b. Is based on selected project attributes (e.g., programmatic assumptions/constraints, assessment of the size, functionality, complexity, criticality, reuse code, modified code, and risk of the software processes and products). c. Is based on the cost implications of the technology to be used and the required maturation of that technology. d. Incorporates risk and uncertainty, including end state risk and threat assessments for cybersecurity. e. Includes the cost of the required software assurance support. f. Includes other direct costs. | 1. Assess the project's software cost estimate(s) to determine if the stated criteria listed in "a" through "f" are satisfied. |
| 016 | 3.3.1 The project manager shall document and maintain a software schedule that satisfies the following conditions:   1. 1. Coordinates with the overall project schedule.    2. Documents the interactions of milestones and deliverables between software, hardware, operations, and the rest of the system.    3. Reflects the critical dependencies for software development activities.    4. Identifies and accounts for dependencies with other projects and cross-program dependencies. | 1. Assess that the software schedule satisfies the conditions in the requirement. |
| 205 | 3.7.1 The project manager, in conjunction with the SMA organization, shall determine if each software component is considered to be safety-critical per the criteria defined in NASA-STD-8739.8. | 2. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.  3. Assess that hazard analyses (including hazard reports) identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A. |
| 134 | 3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:   a. The software is initialized, at first start and restarts, to a known safe state. b. The software safely transitions between all predefined known states. c. Termination performed by software functions is performed to a known safe state. d. Operator overrides of software functions require at least two independent actions by an operator. e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard. f. The software detects inadvertent memory modification and recovers to a known safe state. g. The software performs integrity checks on inputs and outputs to/from the software system. h. The software performs prerequisite checks prior to the execution of safety-critical software commands. i. No single software event or action is allowed to initiate an identified hazard. j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event. k. The software provides error handling. l. The software can place the system into a safe state. | 2. Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone. |
| 146 | 3.8.1 The project manager shall define the approach to the automatic generation of software source code including:   a. Validation and verification of auto-generation tools. b. Configuration management of the auto-generation tools and associated data. c. Description of the limits and the allowable scope for the use of the auto-generated software. d. Verification and validation of auto-generated source code using the same software standards and processes as hand-generated code. e. Monitoring the actual use of auto-generated source code compared to the planned use. f. Policies and procedures for making manual changes to auto-generated source code. g. Configuration management of the input to the auto-generation tool, the output of the auto-generation tool, and modifications made to the output of the auto-generation tools. | 1. Assess that the approach for the auto-generation software source code is defined, and the approach satisfies at least the conditions “a” through “g.” |
| 032 | 3.9.2 The project manager shall acquire, develop, and maintain software from an organization with a non-expired CMMI-DEV rating as measured by a CMMI Institute Certified Lead Appraiser as follows:   1. 1. For Class A software: CMMI-DEV Maturity Level 3 Rating or higher for software.    2. For Class B software (except Class B software on NASA Class D payloads, as defined in NPR 8705.4): CMMI-DEV Maturity Level 2 Rating or higher for software. | 2. Assess potential process-related issues, findings, or risks identified from the CMMI assessment findings. |
| 159 | 3.11.5 The project manager shall test the software and record test results for the required software cybersecurity mitigation implementations identified from the security vulnerabilities and security weaknesses analysis. | 2. Assess the quality of the cybersecurity mitigation implementation testing and the test results. |
| 207 | 3.11.6 The project manager shall identify, record, and implement secure coding practices. | 1. Assess that the software coding guidelines (e.g., coding standards) includes secure coding practices. |
| 057 | 4.2.3 The project manager shall transform the requirements for the software into a recorded software architecture. | 1. Assess that the software architecture addresses or contains the software structure, qualities, interfaces, and external/internal components. |
| 143 | 4.2.4 The project manager shall perform a software architecture review on the following categories of projects:   a. Category 1 Projects as defined in NPR 7120.5. b. Category 2 Projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4. | 1. Assess the results of or participate in software architecture review activities held by the project. |
| 058 | 4.3.2 The project manager shall develop, record, and maintain a software design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested. | 1. Assess the software design against the hardware and software requirements and identify any gaps.  2. Assess the software design to verify that the design is consistent with the software architectural design concepts and that the software design describes the lower-level units to be coded, compiled, and tested.   3. Assess that the design does not introduce undesirable behaviors or unnecessary capabilities. |
| 135 | 4.4.4 The project manager shall use static analysis tools to analyze the code during the development and testing phases to, at a minimum, detect defects, software security, code coverage, and software complexity. | 3. Assess that the project addresses the results from the static analysis tools used by software assurance, software safety, engineering, or the project. |
| 190 | 4.5.10 The project manager shall verify code coverage is measured by analysis of the results of the execution of tests. | 3. Assess any uncovered software code for potential risk, issues, or findings. |
| 075 | 4.6.2 The project manager shall plan and implement software operations, maintenance, and retirement activities. | 1. Assess the maintenance, operations, and retirement plans for completeness of the required software engineering and software assurance activities. |
| 079 | 5.1.2 The project manager shall develop a software configuration management plan that describes the functions, responsibilities, and authority for the implementation of software configuration management for the project. | 1. Assess that a software configuration management plan has been developed and complies with the requirements in NPR 7150.2 and Center/project guidance. |
| 081 | 5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project. | 2. Assess that the software safety-critical items are configuration-managed, including hazard reports and safety analysis. |
| 045 | 5.1.9 The project manager shall participate in any joint NASA/developer audits. | 1. Participate in or assess the results from any joint NASA/developer audits. Track any findings to closure. |
| 086 | 5.2.1 The project manager shall record, analyze, plan, track, control, and communicate all of the software risks and mitigation plans. | 1. Confirm and assess that a risk management process includes recording, analyzing, planning, tracking, controlling, and communicating all software risks and mitigation plans. |
| 202 | 5.5.2 The project manager shall define and implement clear software severity levels for all software non-conformances (including tools, COTS, GOTS, MOTS, OSS, reused software components, and applicable ground systems). | 2. Assess the application and accuracy of the defined severity levels to software non-conformances. |
| 203 | 5.5.3 The project manager shall implement mandatory assessments of reported non-conformances for all COTS, GOTS, MOTS, OSS, and/or reused software components. | 2. Assess the impact of non-conformances on the project software's safety, quality, and reliability. |
| 204 | 5.5.4 The project manager shall implement process assessments for all high-severity software non-conformances (closed-loop process). | 3. Assess opportunities for improvement on the processes identified in the root cause analysis associated with the high severity software non-conformances. |

## 5.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 6. SA Audits

The Software Assurance and Software Safety Standard (SASS), NASA-STD-8739.8 [278](#_tabs-<p>7</p>), defines “audit” as:

* systematic, independent, and documented process for obtaining audit evidence and evaluating it objectively to determine the extent to which audit criteria are fulfilled
* independent examination of a work product or set of work products to assess compliance with specifications, standards, contractual agreements, or other criteria
* independent examination of a software product, software process, or set of software processes to assess compliance with specifications, standards, contractual agreements, or other criteria
* systematic, independent, documented process for obtaining records, statements of fact, or other relevant information and assessing them objectively, to determine the extent to which specified requirements are fulfilled. Note: An audit can be an internal audit (first-party) or an external audit (second party or a third party), and it can be a combined or integrated audit (combining two or more disciplines). Audit results are a clear indication of whether the audit criteria have been met. (IEEE Definition

Therefore, when performing audits, SA personnel are checking to determine compliance or the extent to which certain requirements are fulfilled. SA may also use audits to assess work being performed using an established set of expectations (e.g., coding standards, software engineering work product content – see [**7.18 - Documentation Guidance**](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)).

There are 9 SASS tasks in NASA-STD-8739.8 that require the Software Assurance or Software Safety personnel to “audit” processes, procedures, and standards. (See [**Topic 8.16 – Audit Reports**](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) (Tab 2) for the list of audits). Due to the nature of some SASS audit requirements, the findings from audits may provide information on process-related problems rather than specific technical issues. Both types are important to bring to management’s attention early so they can be addressed as soon as possible.

The results of any audits performed are recorded, and reported on at either (or both) the next regular management meeting or included in the SA Status Report. There are two types of Audit Reports – Audit Summary and Detailed Audit Report. For SA Status Reports, the Audit Summary content should be used.

**See Topic [8.16 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) (Tab 4) for report contents****.**

For more information on conducting audits, see Topic [**8.12 – Basics of Software Auditing**.](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing)

## 6.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 7. Resources

## 7.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-048)

  [Risk Classification for NASA Payloads](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=4A "Click to open in new window")

  NPR 8705.4A, Office of Safety and Mission Assurance, Effective Date: April 29, 2021, Expiration Date: April 29, 2026
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 7.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 7.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review)        * [5.19 - Software Assurance Status Report Minimum Content](/spaces/SWEHBVD/pages/138707621/5.19+-+Software+Assurance+Status+Report+Minimum+Content) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.12 – Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) |

## 7.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>7</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 7.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
