# 8.18 - SA Suggested Metrics

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695756. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics

8.18 - SA Suggested Metrics

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695756)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695756&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction and Metrics Table](#tabs-1)
* [2. GQM](#tabs-2)
* [3. Resources](#tabs-3)

# 1. Introduction

This topic contains the complete list of software assurance/safety metrics that are suggested for use with the Software Assurance tasks in NASA-STD-8739.8.These suggested metrics will provide SA and safety personnel with much of the information they will need to assess both the software assurance/safety work, as well as providing information to help with the monitoring of the software engineering progress.

The Metrics Table tab shows the set of metrics in a table and provides a way to download an Excel file. The Excel file contains the same metrics but has the capability of being able to filter the columns. This provides an easy way to see which metrics are associated with a particular SWE, and to filter out SWEs that may be tailored out in your project. These tables provide information on potential phases in which each metric might be collected. Be sure to read the information at the top of each metrics sheet for more specific information on the use of the tables.

Each project should review the table and decide which metrics they want to collect, based on the metrics that they think will provide them with the most information for their activities.

See also [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects).

## 1.1 Metrics Table

The table below provides suggested metrics for the SWE requirements in Sections 7.3 of the SA tabs in the SWEs of this Handbook.

There are multiple “**Metrics Types**”, and each type includes optional “**Measurements**” by life cycle phase for the “Associated SWE Requirements”. Many of the measurements were reworded to clarify them or to make them more generic so they could be applied in multiple places. For example, the word ***“non-conformance” was used in lieu of findings, problem reports, defects, or errors to cover all types of non-conformances.*** When choosing a measurement, change the word “non-conformance” to the one that best fits the situation to be monitored. (Note: these may be collected by the project and analyzed by SA.) Projects should choose a set of measurements to provide information on the project being implemented. The measurements do not have to be implemented as written. They may be modified to best fit the characteristics of the project.

The life cycle phases listed below indicate the recommended phase the data may be collected (color has been added only to provide a visual reference as you scroll down the page). However, it does not mean it has to be collected in each phase. Establish a set of measurements that best suits the project taking into consideration the size and applicability of the activity. For example, if a configuration audit metric is collected, it may be appropriate to collect those measurements during most of the life cycle phases listed, but the project may not be doing configuration audits in all the listed phases.

The **NPR 7150.2** [083](#_tabs-<p>3</p>)  SWE requirement numbers listed in the table below are associated with the SA tasking in **NASA-STD-8739.8** [278](#_tabs-<p>3</p>)  but may not be the only applicable SWE requirement for a particular metric.

There are a few measurements that are required specifically for analysis in NASA-STD-8739.8. They are listed in **bold type**. Other measurements listed in the charts should be considered when performing the tasking activities associated with the SWE numbers for the metric.

In some cases, in order to understand the full context of the metric listed in a requirement, look at the metrics in 8.18 to see other measures that contribute to the metric in a particular requirement.

For example,  the table shows SWE-036 with the metric, “# of software components (e.g. programs, modules, routines, functions, etc.) planned versus the number actually released in each build.” SWE-036, task 1c would provide the planning information for the scheduled deliverables. However, in order to complete the metric in SWE-036, it would be necessary to use the information collected in SWE-077 to get the  “# of components actually released in each build.”

| **Metrics Type** | **Measurements** | PLAN | REQ | DES | IMP | TEST | DEL | **Associated SWE Reqt #** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peer Review Metrics | # of peer reviews performed vs. # of peer reviews planned |  | X | X | X | X | X | SWE-016  SWE-087  SWE-089 |
| Peer Review Metrics | # of Non-Conformances identified in each peer review |  | X | X | X | X | X | SWE-087  SWE-089 |
| Peer Review Metrics | # of Non-Conformances identified by software assurance during each peer review |  | X | X | X | X | X | SWE-087  SWE-088  SWE-089 |
| Peer Review Metrics | Total # of peer review Non-Conformances (Open, Closed) |  | X | X | X | X | X | SWE-087  SWE-088  SWE-089 |
| Peer Review Metrics | Preparation time each review participant spent preparing for the review |  | X | X | X | X | X | SWE-088  SWE-089 |
| Peer Review Metrics | Time required to close review Non-Conformances |  | X | X | X | X | X | SWE-087  SWE-088  SWE-089 |
| Peer Review Metrics | # of peer review participants vs. total # invited |  | X | X | X | X | X | SWE-088  SWE-089 |
| Peer Review Metrics | # of peer review Non-Conformances per work product vs. # of peer reviewers |  | X | X | X | X | X | SWE-088  SWE-089 |
| Peer Review Audit Metrics | # of audit Non-Conformances per peer review audit |  | X | X | X | X | X | SWE-088 |
| Peer Review Audit Metrics | # of Peer Review Audits planned vs. # of Peer Review Audits performed |  | X | X | X | X | X | SWE-016  SWE-087  SWE-088 |
| Peer Review Audit Metrics | Trends on non-conformances from audits (Open, Closed, Life cycle Phase) |  | X | X | X | X | X | SWE-088  SWE-089 |
| Peer Review Audit Metrics | Time required to close peer review audit Non-Conformances |  | X | X | X | X | X | SWE-088  SWE-089 |
| Peer Review Audit Metrics | Preparation time each audit participant spent preparing for audit |  | X | X | X | X | X | SWE-088  SWE-089 |
| Problem/Change Report Status Metrics | Total # of Non-Conformances over time (Open, Closed, # of days Open, and Severity of Open)  # of Non-Conformances in current reporting period (Open, Closed, Severity) | X | X | X | X | X | X | SWE-062  SWE-065c  SWE-065d  SWE-068  SWE-202  SWE-203  SWE-204 |
| Problem/Change Report Status Metrics | # of safety-related Non-Conformances |  | X | X | X | X | X | SWE-203  SWE-068  SWE-071 |
| Problem/Change Report Status Metrics | Trend of Open vs. Closed Non-Conformances over time | X | X | X | X | X | X | SWE-053  SWE-054  SWE-065 |
| Problem/Change Report Status Metrics | Trend of change status over time (# of changes approved, # in implementation, # in test, # closed) | X | X | X | X | X | X | SWE-018  SWE-053  SWE-080 |
| Problem/Change Report Status Metrics | # of Non-Conformances identified in embedded COTS, GOT, MOTS, OSS, or reused components in ground or flight software vs. # of Non-Conformances closed |  |  | X | X | X |  | SWE-136  SWE-202  SWE-203  SWE-211 |
| Problem/Change Report Status Metrics | # of Non-Conformances identified in source code products used (Open, Closed) |  |  | X | X | X |  | SWE-202  SWE-203 |
| Problem/Change Report Status Metrics | **# of software Non-Conformances at each Severity level for each software configuration item (Open, Closed)**  **Bold type indicates a required item** |  |  |  | **X** | **X** | **X** | **SWE-202** |
| Problem/Change Report Status Metrics | # of Closed action items vs. # of Open action items | X | X | X | X | X | X | SWE-062 SWE-62c  SWE-065d |
| Problem/Change Report Status Metrics | # of Root Cause Analyses performed;  # of Non-Conformances identified by each root cause analysis |  |  | X | X | X | X | SWE-204 |
| SA Corrective Action (CA) metrics (Issues, Risks) | # of Corrective Actions (CAs) raised by SA vs. total #         Attributes (Type, Severity, # of days Open, Life cycle Phase Found)        State (Open, In work, Closed)        Trends of CA Open vs. Closures over time | X | X | X | X | X | X | SWE-024  SWE-204  SWE-054 |
| SA Corrective Action (CA) metrics (Issues, Risks) | Trend the # of inconsistencies or corrective actions identified, and # closed. | X | X | X | X | X |  | SWE-054  SWE-024  SWE-204 |
| SA Corrective Action (CA) metrics (Issues, Risks) | # of open vs. closed issues over time and latency | X | X | X | X | X | X | SWE-018 |
| Process Improvement Metrics | # of software work product Non-Conformances identified by life cycle phase over time | X | X | X | X | X | X | SWE-013  SWE-022  SWE-024  SWE-039  SWE-051  SWE-054  SWE-057  SWE-058  SWE-062  SWE-065b  SWE-065c  SWE-065d  SWE-068  SWE-071  SWE-075  SWE-079  SWE-084  SWE-086  SWE-087  SWE-125  SWE-134  SWE-139  SWE-146  SWE-157  SWE-159  SWE-184  SWE-185  SWE-187  SWE-191  SWE-194  SWE-201  SWE-204  SWE-205 |
| Process Improvement Metrics | # of software process Non-Conformances by life cycle phase over time | X | X | X | X | X | X | SWE-032  SWE-039  SWE-061  SWE-077  SWE-080  SWE-082  SWE-085  SWE-086  SWE-088  SWE-139  SWE-195  SWE-204 |
| Process Improvement Metrics | Identify the specific requirements in NASA-STD-8739.8 that are being tailored by the projects (\*organizational metric) | X | X | X | X | X | X | SWE-121  SWE-125  SWE-013  SWE-176 |
| Process Improvement Metrics | # of projects tailoring each requirement (\*organizational measure)  % of requirements tailored per project (\*organizational measure) | X | X | X | X |  |  | SWE-125  SWE-013  SWE-121 |
| Process Improvement Metrics | % of Total Source Code for each Software Classification (\*organizational measure) |  |  |  | X | X | X | SWE-020  SWE-176  SWE-087 |
| Cost/ Effort Metrics | Planned SA resource allocation vs. actual SA resource allocation | X | X | X | X | X | X | SWE-015  SWE-174  SWE-151 |
| Cost/ Effort Metrics | Comparison of initial SA cost estimates vs. final cost (capturing assumptions and differences) | X |  |  |  |  | X | SWE-174  SWE-015  SWE-151 |
| Cost/ Effort Metrics | Trend SA cost estimates throughout life cycle | X | X | X | X | X | X | SWE-174 |
| Training Metrics | % of required training completed for each of the project SA personnel | X | X | X | X |  |  | SWE-017 |
| Training Metrics | % of project personnel that have completed project specific training against the planned training schedule |  | X | X | X | X | X | SWE-017 |
| Compliance Audit Metrics | # of Compliance Audits planned vs. # of Compliance Audits performed | X | X | X | X | X | X | SWE-024  SWE-039  SWE-139  SWE-016  SWE-032  SWE-077  SWE-195  SWE-082  SWE-084  SWE-085  SWE-086  SWE-088  SWE-079 SWE-201 |
| Compliance Audit Metrics | # of Open vs. Closed Audit Non-Conformances over time  # of Non-Conformances per audit (including findings from process and compliance audits, process maturity) | X | X | X | X | X | X | SWE-022  SWE-024  SWE-039  SWE-139  SWE-016  SWE-032  SWE-077  SWE-079  SWE-195  SWE-082  SWE-084  SWE-085  SWE-086  SWE-088  SWE-201 |
| Compliance Audit Metrics | # of Non-Conformances identified in plans (e.g., SMPs, SDPs, CM Plans, SA Plans, Safety Plans, Test Plans) | X | X | X | X | X |  | SWE-024  SWE-013  SWE-075  SWE-079  SWE-139  SWE-071 |
| Compliance Audit Metrics | #  of Non-Conformances identified in the software Configuration Management Plan  Trends of # Open vs. # Closed over time |  | X | X | X | X | X | SWE-079 |
| Compliance Audit Metrics | #  of Configuration Management Audits conducted by the project – Planned vs. Actual |  | X | X | X | X | X | SWE-082  SWE-077  SWE-084 |
| Compliance Audit Metrics | # of Non-Conformances per audit (including findings from process and compliance audits, process maturity) | X | X | X | X | X | X | SWE-024  SWE-039  SWE-139  SWE-016  SWE-032  SWE-077  SWE-195  SWE-082  SWE-084  SWE-085  SWE-086  SWE-088  SWE-079 |
| Compliance Audit Metrics | # of process Non-Conformances (e.g., activities not performed) identified by SA vs. # accepted by the project  Trends of # Open vs. # Closed over time | X | X | X | X | X | X | SWE-016  SWE-039  SWE-032  SWE-077  SWE-195  SWE-082  SWE-084  SWE-085  SWE-086  SWE-088 |
| Compliance Audit Metrics | # of Non-Conformances found in flight code, ground code, tools, and COTs products used (Open vs. Closed). |  |  | X | X | X | X | SWE-136 |
| Compliance Audit Metrics | # of open non-compliances vs. # of closed non-compliances found in security scans or coding standard compliance audits. |  |  | X | X | X | X | SWE-63 |
| Project Acceptance Metrics | # of Non-Conformances (activities not being performed)  # of Non-Conformances accepted by project  # of Non-Conformances (Open, Closed, Total)  Trends of Open vs, Closed Non-Conformances over time | X | X | X | X | X | X | SWE-087  SWE-201  SWE-039  SWE-139 |
| Progress Tracking Metrics | Deviations of actual schedule progress vs. planned schedule progress above defined threshold | X | X | X | X | X | X | SWE-016  SWE-018  SWE-046 |
| Progress Tracking Metrics | # of Software Requirements (e.g. Project, Application, Subsystem, System, etc.) |  | X | X | X | X | X | SWE-050  SWE-051  SWE-052  SWE-065b  SWE-066  SWE-194  SWE-027 |
| Progress Tracking Metrics | # of Software Requirements that do not trace to a parent requirement |  | X | X | X |  |  | SWE-033  SWE-050  SWE-051 |
| Progress Tracking Metrics | # of architectural issues identified vs. number closed |  |  | X |  |  |  | SWE-057  SWE-058  SWE-143 |
| Progress Tracking Metrics | # of planned units for implementation vs. # of units tested and implemented |  |  |  | X |  |  | SWE-060 |
| Progress Tracking Metrics | # of planned unit test cases vs. # of actual unit test cases completed |  |  |  | X |  |  | SWE-062  SWE-186 |
| Progress Tracking Metrics | Total # of tests completed vs. # of test results evaluated and signed off |  |  |  |  | X | X | SWE-066  SWE-068  SWE-065d  SWE-159 |
| Progress Tracking Metrics | # of Safety-Critical tests executed vs. # of Safety-Critical tests witnessed by SA |  |  |  | X | X | X | SWE-066  SWE-068  SWE-065d  SWE-159  SWE-062  SWE-186 |
| Progress Tracking Metrics | # of software components (e.g. programs, modules, routines, functions, etc.) planned vs. # actually released in each build |  |  |  |  | X | X | SWE-194  SWE-077  SWE-073  SWE-036 |
| Progress Tracking Metrics | # of Non-Conformances from reviews (Open vs. Closed; # of days Open) | X | X | X | X | X | X | SWE-134  SWE-037  SWE-039  SWE-087  SWE-088  SWE-089  SWE-143 |
| Progress Tracking Metrics | # of Software Requirements being met via satisfactory testing vs. total # of Software Requirements |  |  |  | X | X | X | SWE-065d  SWE-066  SWE-192  SWE-071 |
| Progress Tracking Metrics | # of Software Requirements without associated test cases |  |  |  | X | X | X | SWE-066  SWE-065b  SWE-071 |
| Progress Tracking Metrics | # of  design issues found vs. # of design issues resolved |  |  | X | X |  |  | SWE-058 |
| Progress Tracking Metrics | # of planned units for implementation vs. # of units implemented and unit tested. |  |  | X | X | X |  | SWE-060 |
| Risk Management Metrics | # of Risks identified in each life cycle phase (Open, Closed) | X | X | X | X | X | X | SWE-086  SWE-039  SWE-179  SWE-154  SWE-156  SWE-190 |
| Risk Management Metrics | # of Risks by Severity (e.g., red, yellow, green) over time | X | X | X | X | X | X | SWE-032  SWE-033  SWE-039  SWE-086  SWE-154  SWE-156  SWE-179  SWE-190  SWE-191 |
| Risk Management Metrics | # of Risks with mitigation plans vs. total # of Risks | X | X | X | X | X | X | SWE-032  SWE-033  SWE-039  SWE-086  SWE-154  SWE-156  SWE-179  SWE-190  SWE-191 |
| Risk Management Metrics | # of Risks trending up over time  # of Risks trending down over time | X | X | X | X | X | X | SWE-032  SWE-033  SWE-039  SWE-086  SWE-154  SWE-156  SWE-179  SWE-190  SWE-191 |
| Cybersecurity Risk Metrics | # of Cybersecurity Risks identified (Open, Closed, Severity) |  |  | X | X | X | X | SWE-154  SWE-156 |
| Cybersecurity Risk Metrics | ·of Cybersecurity Risks with Mitigations vs. # of Cybersecurity Risks identified |  |  | X | X | X | X | SWE-154  SWE-156  SWE-159 |
| Traceability Metrics | % of traceability completed in each area: System Level requirements to Software requirements; Software Requirements to Design; Design to Code; Software Requirements to Test Procedures |  | X | X | X | X |  | SWE-052 |
| Traceability Metrics | % of traceability completed for all hazards to software requirements and test procedures |  | X | X | X | X |  | SWE-052 |
| Traceability Metrics | Defect trends for trace quality (# of circular traces, orphans, widows, etc.) |  | X |  |  |  |  | SWE-051  SWE-052 |
| Requirements Metrics | # of detailed software requirements vs. # of estimated SLOC to be developed by the project |  | X | X |  | X |  | SWE-050  SWE-051  SWE-151  SWE-174 |
| Requirements Metrics | # of incorrect, missing and incomplete requirements (i.e., # of requirements issues) vs. # of requirements issues resolved |  | X | X |  |  |  | SWE-051  SWE-053  SWE-054 |
| Requirements Metrics | **Software Requirements Volatility (# of requirements added, deleted, modified, # of TBDs over time)** |  | **X** | **X** | **X** | **X** |  | **SWE-200**  **SWE-053** |
| Requirements Metrics | # of TBD/TBC/TBR requirements trended over time |  |  | X | X | X | X | SWE-066 |
| Safety Metrics | # of safety-related requirement issues (Open, Closed) over time |  | X | X | X | X | X | SWE-039  SWE-139  SWE-205  SWE-023  SWE-134  SWE-184  SWE-052  SWE-051  SWE-058  SWE-065b  SWE-066  SWE-071  SWE-192  SWE-080  SWE-087 |
| Safety Metrics | # of safety-related non-conformances identified by life cycle phase (over time, Open vs. Closed, # of days) |  | X | X | X | X | X | SWE-013  SWE-039  SWE-139  SWE-143  SWE-121  SWE-184  SWE-023  SWE-134  SWE-052  SWE-051  SWE-057  SWE-058  SWE-135  SWE-062  SWE-065a  SWE-065b  SWE-065c  SWE-065d  SWE-066  SWE-068  SWE-071  SWE-191  SWE-080  SWE-081  SWE-087  SWE-205 |
| Reuse Metrics | # of products submitted for reuse;  # of developed products submitted for reuse vs. total # of developed products |  |  |  |  |  | X | SWE-147  SWE-148 |
| Reuse Metrics | # of developed products entered in NASA Internal Sharing & Reuse System vs. total # of developed products |  |  |  |  |  | X | SWE-147  SWE-148 |
| Reuse Metrics | # of products submitted for reuse vs. # of products entered into NASA Internal Sharing & Reuse Systems |  |  |  |  |  | X | SWE-147  SWE-148 |
| Cybersecurity Metrics | # of Cybersecurity vulnerabilities and weaknesses identified  # of Cybersecurity vulnerabilities and weaknesses (Open, Closed, Severity)  Trending of Open vs. Closed over time | X | X | X | X | X | X | SWE-159  SWE-135  SWE-063 |
| Cybersecurity Metrics | # and type of vulnerabilities and weaknesses identified by the project | X | X | X | X | X |  | SWE-135  SWE-063 |
| Cybersecurity Metrics | # of Cybersecurity vulnerabilities and weaknesses identified by life cycle phase |  | X | X | X | X | X | SWE-159  SWE-135  SWE-063 |
| Cybersecurity Metrics | # of Cybersecurity vulnerabilities and weaknesses identified vs. # resolved during Implementation |  |  |  | X | X | X | SWE-159  SWE-135  SWE-063 |
| Cybersecurity Metrics | # of requirements specified relating to detection of adversarial actions vs. # of requirements related to detection of adversarial actions actually implemented |  |  |  | X | X | X | SWE-210 |
| Cybersecurity Metrics | # of Non-Conformances identified in Cybersecurity coding standard compliance (Open, Closed) |  |  |  | X | X | X | SWE-063  SWE-135  SWE-207 |
| Test Coverage Metrics | **Software code/test coverage percentages for all identified safety-critical components (e.g., # of paths tested vs. total # of possible paths)**  **Note: Metrics in bold type are required by all projects** |  |  |  |  | X |  | SWE-066 SWE-190 SWE-189  SWE-219 |
| Test Coverage Metrics | **Test coverage data for all identified safety-critical software components.** |  |  |  |  | X |  | SWE-219 |
| Test Coverage Metrics | % of code that has been executed during testing |  |  |  |  | X |  | SWE-060 |
| Static Code Metrics | Document the Static Code Analysis tools used with associated Non-Conformances  ·of total errors and warnings identified by the tool  # of errors and warnings evaluated vs. # of total errors and warnings identified by the tool |  |  |  | X |  |  | SWE-135  SWE-185 |
| Static Code Metrics | # of Non-Conformances raised by SA vs. total # of raised Non-Conformances |  |  |  | X |  |  | SWE-135  SWE-185 |
| Static Code Metrics | # of static code errors and warnings identified as “positives” vs. # of total errors and warnings identified by the tool  Total # of static code analysis "positives" vs.  # of "positives" resolved. Trend over time.  # of static code errors and warnings resolved by Severity vs. # of static code errors and warnings identified by Severity by the tool |  |  |  | X |  |  | SWE-135  SWE-185 |
| Static Code Metrics | # of static code “positives” over time (Open, Closed, Severity) |  |  |  | X | X |  | SWE-135  SWE-185 |
| Static Code Metrics | # of Cybersecurity vulnerabilities and weaknesses identified by the tool |  |  |  | X | X |  | SWE-135  SWE-185 |
| Static Code Metrics | # of coding standard violations identified (Open, Closed, type of violation, Severity) |  |  |  | X |  |  | SWE-061  SWE-185 |
| Static Code Metrics | Software cyclomatic complexity # for all identified safety-critical components |  |  |  | X | X |  | SWE-087  SWE-134 |
| Static Code Metrics | Trend of # of total errors and warnings identified per SCA Tool, Language, and SLOC size |  |  |  | X |  |  | SWE-135 |
| Static Code Metrics | Total # of static code analysis "positives" vs.  # of "positives" resolved. Trend over time. |  |  |  | X |  |  | SWE-135 |
| Test Procedures Metrics | #  of Non-Conformances and risks open vs. # of Non-Conformances, risks, identified with test procedures |  |  |  | X | X |  | SWE-087  SWE-065b  SWE-071  SWE-191 |
| Test Procedures Metrics | # of hazards with completed test procedures/cases vs. total number of hazards over time |  |  |  | X | X |  | SWE-065b  SWE-068  SWE-191 |
| Test Procedures Metrics | # of software requirements with completed test procedures/cases over time |  |  |  | X | X |  | SWE-065b  SWE-071  SWE-066 |
| Test Procedures Metrics | # of Non-Conformances identified when the approved, updated requirements are not reflected in test procedures |  |  |  | X | X |  | SWE-065b  SWE-071  SWE-052  SWE-066  SWE-191 |
| Test Procedures Metrics | # of Non-Conformances identified while confirming hazard controls are verified through test plans/procedures/cases |  |  |  | X | X |  | SWE-065b  SWE-071  SWE-066  SWE-068  SWE-191 |
| Test Procedures Metrics | # of issues and risks/corrective actions open vs. total # of issues and risks/corrective actions identified with test procedures |  |  | X | X | X |  | SWE-065b |
| Test Metrics | # of tests executed vs. # of tests completed |  |  |  | X | X | X | SWE-062  SWE-066  SWE-065d  SWE-068  SWE-159  SWE-190  SWE-192  SWE-055  SWE-080  SWE-191  SWE-194  SWE-211 |
| Test Metrics | # of Non-Conformances identified during each testing phase (Open, Closed, Severity) |  |  |  | X | X | X | SWE-062  SWE-065d  SWE-066  SWE-068  SWE-080  SWE-159  SWE-190  SWE-191  SWE-192  SWE-194  SWE-211 |
| Test Metrics | ·of Requirements tested vs. total # of Requirements |  |  |  | X | X | X | SWE-062  SWE-065b  SWE-065d  SWE-066  SWE-080  SWE-191  SWE-192  SWE-194 |
| Test Metrics | # of Hazards containing software that have been tested vs. total # of Hazards containing software |  |  |  | X | X | X | SWE-062  SWE-066  SWE-068  SWE-080  SWE-134  SWE-192  SWE-205 |
| Test Metrics | # of Non-Conformances identified in models, simulations, and tools over time (Open, Closed, Severity) |  |  |  | X | X | X | SWE-070 |
| Test Metrics | # of Regression test set Non-Conformances/Risks over time (Open, Closed, Severity) |  |  |  | X | X | X | SWE-191 |
| Test Metrics | # of risks and Non-conformances open vs. total # of risks and Non-Conformances identified with test code |  |  |  | X | X | X | SWE-065c |
| Test Metrics | # of Requirements tested in customer environment vs. # of Requirements |  |  |  |  | X | X | SWE-055 |
| Cybersecurity Metrics During Testing Metrics | # of Cybersecurity mitigation implementations identified from the security vulnerabilities and security weaknesses |  |  |  | X | X | X | SWE-154  SWE-159  SWE-191 |
| Cybersecurity Metrics During Testing Metrics | # of Cybersecurity mitigation implementations identified with associated test procedures vs. # of Cybersecurity mitigation implementations identified |  |  |  | X | X | X | SWE-154  SWE-159  SWE-191 |
| Cybersecurity Metrics During Testing Metrics | # of Cybersecurity mitigation tests completed vs. total # of Cybersecurity mitigation tests |  |  |  | X | X | X | SWE-159 |
| Cybersecurity Metrics During Testing Metrics | # of Non-Conformances identified during Cybersecurity mitigation testing (Open, Closed, Severity) |  |  |  | X | X | X | SWE-159 |
| Cybersecurity Metrics During Testing Metrics | Trends of Cybersecurity Non-Conformances over time |  |  |  | X | X | X | SWE-159  SWE-063  SWE-135  SWE-201 |
| Test Coverage Metrics | **Software code/test coverage percentages for all identified safety-critical components (e.g., # of paths tested vs. total # of possible paths)** |  |  |  | **X** | **X** | **X** | **SWE-066**  **SWE-190**  **SWE-134**  **SWE-189** |
| Test Coverage Metrics | # of tests completed vs. total # of tests |  |  |  | X | X | X | SWE-055  SWE-062  SWE-066  SWE-065d  SWE-068  SWE-080  SWE-159  SWE-190  SWE-191  SWE-192  SWE-194  SWE-211 |
| Test Coverage Metrics | # of detailed software requirements tested to date vs. total # of detailed software requirements |  |  |  | X | X | X | SWE-055  SWE-062  SWE-065b  SWE-065d  SWE-066  SWE-071  SWE-080  SWE-191  SWE-192  SWE-194  SWE-159 |
| Test Coverage Metrics | # of safety-critical requirement verifications vs. total # of safety-critical requirement verifications completed  # of Open issues vs. # of Closed over time |  |  |  | X | X | X | SWE-062  SWE-066  SWE-191  SWE-192  SWE-068 |
| Test Coverage Metrics | # of Source Lines of Code (SLOC) tested vs. total # of SLOC |  |  |  | X | X | X | SWE-066  SWE-134  SWE-189  SWE-190  SWE-219 |
| Build/Release Content Metrics | # of software units planned vs. # actually built |  |  | X | X | X | X | SWE-063  SWE-194 |
| Build/Release Content Metrics | # of planned software requirements implemented in each build vs. # of actual software requirements implemented in each build |  |  |  | X | X | X | SWE-063  SWE-194 |
| Build/Release Content Metrics | # of Non-Conformances identified in release documentation (Open, Closed) |  |  |  | X | X | X | SWE-063  SWE-077  SWE-084  SWE-085 |
| Operations/ Maintenance Metrics | # of Non-Conformances identified in the software after delivery |  |  |  |  |  | X | SWE-195 |
| Other Metrics | Measures relating to status and performance as identified in other requirements. (Schedule deviations, closure of corrective actions, product and process audit results, peer review result, etc) |  |  | X | X | X | X | SWE-093 |
| Other Metrics | # of requirements being met, any TBD/TBC/TBR requirements, or any requirements that are not being met  Performance and functionality measures (Schedule deviations, closure of corrective actions, product and process audit results, peer review results, requirements volatility, # of requirements satisfactorily tested vs. total # of requirements, etc.) |  |  | X | X | X | X | SWE-199 |
| Other Metrics | # of findings open vs. # of findings identified | X | X | X | X | X |  | SWE-082 |
| Other Metrics | Trends of Open vs. Closed Non-Conformances change reports over time. | X | X | X | X | X |  | SWE-065d |
| IV&V Metrics (Kept by IV&V) | # of IV&V Non-Conformances/issues,/risks (Open, Closed, accepted by the project, severity, category of Non-Conformance (e.g., requirements severity, category (requirements, design, code, test, documentation, etc.))  Kept by IV&V team, not SA | X | X | X | X | X | X | SWE-179 |
| Coverage Metrics | Code coverage data: % of code that has been executed during testing |  |  |  | X | X | X | SWE-060 |
| Coverage Metrics | Test coverage data for all identified safety-critical software components. |  |  |  | X | X | X | SWE-219 |

**For a usable MS Excel version of this table, click on the image below and download the file.**

## 1.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-3) in the Resources tab.

# 2. Goal-Question-Metric (GQM) method

The **Goal-Question-Metric (GQM) method** is a structured framework used for defining and measuring software processes, products, and organizational goals. It provides a systematic approach to developing metrics to assess the progress, quality, and effectiveness of a given project or process. The GQM method ensures that metrics are directly tied to objectives, making them practical, relevant, and actionable, rather than arbitrary.

## 2.1 Core Concepts of GQM

The GQM method is based on three hierarchical levels:

#### **1. Goal:**

* The top level involves defining **what you want to accomplish**.
* Goals are strategic and high-level, reflecting the broader objectives of a project, product, or organizational initiative.
* They should clearly describe the intended outcome in measurable terms, such as improving quality, enhancing productivity, or reducing defects.

**Example of a Goal:**

* "Ensure the delivery of high-quality, secure software that meets customer requirements."

#### **2. Question:**

* Goals are then broken down into **questions** that need to be answered in order to determine whether the goals are being achieved.
* Questions define **what aspects of the goal** should be measured, and they help specify the focus areas for collecting and evaluating data.
* These questions serve as an intermediary level between the desired goal and the measurable metrics.

**Example of Questions:**

* "Are software requirements adequately detailed for development and testing?"
* "Has the number of defects in safety-critical code decreased over time?"

#### **3. Metric:**

* At the bottom level, **metrics are defined to answer the questions**.
* Metrics provide the actual data to be collected, measured, and analyzed. They are quantitative or qualitative measurements that indicate progress toward the goal.
* A metric must be actionable, useful, and relevant to the associated question and goal.

**Example of Metrics:**

* "The percentage of detailed requirements that are traceable to development and test cases."
* "The number of security vulnerabilities found per 1,000 lines of code."

## 2.2 How GQM Works

The process of applying the GQM method involves:

1. **Define Goals:**

   * Identify the high-level objectives for the product, process, or organization.
   * Goals can vary by stakeholders, such as managers focusing on cost and schedule or engineers focusing on defect rates.
2. **Generate Questions:**

   * Derive specific questions that clarify what information is needed to evaluate whether the goals are being achieved.
   * Every question needs to be concrete and tied to some aspect of the goal.
3. **Identify Metrics:**

   * Choose or design metrics that provide the necessary data to answer the questions.
   * Metrics can be directly measurable (e.g., defect count, test coverage) or derived (e.g., defect density, failure rate).
4. **Collect Data and Analyze:**

   * Gather the required data according to the metrics.
   * Interpret the results to answer the questions and determine if the goals are being achieved.

## 2.3 Benefits of GQM

* **Alignment with Goals:** Ensures that every metric has a clear purpose and directly contributes toward achieving a goal.
* **Focus on Relevance:** Avoids collecting unnecessary or irrelevant data by tying metrics to specific questions and goals.
* **Improves Decision-Making:** Provides actionable insights to stakeholders by connecting data with strategic objectives.
* **Customizability:** Can be tailored to specific organizational needs, projects, or domains.
* **Enables Traceability:** Ensures traceability from high-level goals to low-level metrics.

## 2.4 Example Application of GQM

#### Goal:

> Improve software quality by reducing the number of critical defects in delivered products.

#### Questions:

1. How many critical defects are found during development and testing phases?
2. What types of defects are the most common?
3. Are code reviews effective in detecting critical defects?

#### Metrics:

1. Number of critical defects per 1,000 lines of code (defect density).
2. Percentage of defects categorized by type (functional, security-related, etc.).
3. Number of defects detected per peer review session.

## 2.5 Conclusion

The **Goal-Question-Metric (GQM) method** is a powerful framework to ensure that measurement activities are directly aligned with stakeholder objectives and project needs. It turns abstract goals into actionable insights by connecting broad objectives with specific questions and quantifiable metrics. This structured approach reduces ambiguity, promotes focus, and enhances the quality of data-driven decisions.

## 2.6 Derivation of SA Metrics from the Goal Statements using the Goal, Question, Metric method.

The table below shows the derivation of SA Metrics from the Goal Statements using the Goal, Question, Metric method.

| **Goal Statements** | **Goal** | **Question** | **SA Metric** |
| --- | --- | --- | --- |
| Assure delivery of quality software requirements to assure safe and secure products in support of mission success and customer objectives. | Quality Software Requirements | Are the software requirements detailed enough for development and test? | The ratio of the number of detailed software requirements to the number of SLOC to be developed by the project. |
| Percentage complete of each area of traceability. |
| Are requirements stable? | Software requirements volatility trended after project baseline (e.g., # of requirements added, deleted, or modified; tbds). |
| Are the software hazards adequately addressed in the software requirements? | Percentage complete of traceability to each hazard with software items. |
| Assure delivery of quality, safe, and secure code. | Quality Code | Is the code secure and has the code addressed cybersecurity requirements? | Number of cybersecurity secure coding violations per number of developed lines of code; |
| List of types of secure coding violations found. |
| Is the safety-critical code safe? | Software cyclomatic complexity data for all identified safety-critical software component; |
| What is the quality of the code? | Number of defects or issues found in the software after delivery; |
| The number of defects or non-conformances found in flight code, ground code, tools, and COTs products used. |
| Do the requirements adequately address cybersecurity? | Number and type of identified cybersecurity vulnerabilities and weaknesses found by the project. |
| Continuously improve the quality and adequacy of software testing to assure safe and reliable products and services are delivered. | Quality Software Testing | Does the test program provide adequate coverage? | Software Code Coverage data; |
| Software requirements test coverage percentages, including the percentage of testing completed and the percentage of the detailed software requirements, successfully tested to date; |
| Number of issues and discrepancies found during each test; |
| The number of lines of code tested. |
| Does the software test program test all of the safety-critical code? | Test coverage data for all identified safety-critical software components. |
| Continuously monitor software projects to improve management of Software Plans, Procedures, and Defects to assure quality products and services are delivered on-time and within budget. | Quality Software Plans, Procedures, and Defect Tracking | Is the SW project proceeding as planned? | Compare initial cost estimate and final actual cost, noting assumption and differences in cost parameters; |
| Is the SW project addressing identified problems? | The number of finding from process non-compliances and process maturity. |
| Is the SW project using peer reviews to increase product quality? | Number of peer reviews performed vs. # planned; the number of defects found in each peer review; |
| How well is the project following its processes and procedures? | Number of audits findings per audit; |
| The time required to close the audit findings; |
| Defect Tracking status and why the Defect occurred? | Problem/change report status: total number, number closed, the number opened in the current reporting period, age, severity; |
| Number of defects or issues found in the software after delivery; |
| The number of defects or non-conformances found in flight code, ground code, tools, and COTs products used. |
| Number of software non-conformances at each severity level for each software configuration item. |
| The number of root cause analyses performed; list of finding identified by each root cause analysis. |
| The trend showing the closure of corrective actions over time. |
| Maintain and advance organizational capability in software assurance processes and practices to meet NASA-STD-8739.8 requirements. | SA Process Improvements | Are SA findings providing valueto software development? | The number of SA findings (e.g., # open, closed, latency, # accepted) mapped against SA activities, through the life cycle, including process non-compliances, process maturity. |
| The number of defects found by software assurance during each peer review activity. |
| Is the SA effort proceeding as planned? | Trend the software assurance cost estimates through the project life cycle; |
| Planned SA resource allocation versus actual SA resource allocation. |
| Percent of the required training completed for each of the project SA personnel. |
| The number of compliance audits planned vs. the number of compliance audits complete and trends on non-conformances from the audits. |

See also [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 2.7 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-3) in the Resources tab.

# 3. Resources

## 3.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-391)

  [The Goal Question Metric Approach,](http://www.cs.umd.edu/~mvz/handouts/gqm.pdf "Click to open in new window")

  Basili, V., Caldiera, G. and Rombach, H. D., Institute for Advanced Computer Studies, Department of Computer Science, University Of Maryland, College Park, Maryland. FB Informatik, Universität Kaiserslautern, Kaiserslautern, Germany.
* (SWEREF-392)

  [Goal-Driven Software Measurement,](http://www.sei.cmu.edu/library/abstracts/reports/96hb002.cfm "Click to open in new window")

  Park, R., Goethert, W., and Florac, W. CMU/SEI-96-HB-002.

## 3.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-024 - Plan Tracking](/spaces/7150/pages/16449729/SWE-024+-+Plan+Tracking) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-032 - CMMI Levels for Class A and B Software](/spaces/SWEHBVD/pages/102695411/SWE-032+-+CMMI+Levels+for+Class+A+and+B+Software) * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/7150/pages/16450267/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-121 - Document Tailored Requirements](/spaces/SWEHBVD/pages/102695487/SWE-121+-+Document+Tailored+Requirements) * [SWE-125 - Requirements Compliance Matrix](/spaces/SWEHBVD/pages/102695489/SWE-125+-+Requirements+Compliance+Matrix) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) * [SWE-143 - Software Architecture Review](/spaces/SWEHBVD/pages/102695501/SWE-143+-+Software+Architecture+Review) * [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code) * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-148 - Contribute to Agency Software Catalog](/spaces/SWEHBVD/pages/102695505/SWE-148+-+Contribute+to+Agency+Software+Catalog) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-174 - Software Planning Parameters](/spaces/SWEHBVD/pages/102695516/SWE-174+-+Software+Planning+Parameters) * [SWE-176 - Software Records](/spaces/SWEHBVD/pages/102695517/SWE-176+-+Software+Records) * [SWE-179 - IV&V Submitted Issues and Risks](/spaces/SWEHBVD/pages/102695519/SWE-179+-+IV+V+Submitted+Issues+and+Risks) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-195 - Software Maintenance Phase](/spaces/SWEHBVD/pages/102695530/SWE-195+-+Software+Maintenance+Phase) * [SWE-199 - Performance Measures](/spaces/SWEHBVD/pages/102695532/SWE-199+-+Performance+Measures) * [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics) * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances) * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [SWE-203 - Mandatory Assessments for Non-Conformances](/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances) * [SWE-204 - Process Assessments](/spaces/SWEHBVD/pages/102695538/SWE-204+-+Process+Assessments) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices) * [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>3</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics) |

## 3.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.11 Software Measurements](/spaces/SWEHBVD/pages/133235387/A.11+Software+Measurements) |
