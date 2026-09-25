# 7.14 - Implementing Measurement Requirements and Analysis for Projects

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695648. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects

7.14 - Implementing Measurement Requirements and Analysis for Projects

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695648)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695648&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Metrics Overview](#tabs-1)
* [2. Sample Measurements](#tabs-2)
* [3. Planning the Measurement Activities](#tabs-3)
* [4. Measurement Activities During the Project](#tabs-4)
* [5. Project Completion](#tabs-5)
* [6. Roles](#tabs-6)
* [7. Resources](#tabs-7)

# 1. Purpose

Provides guidance for projects implementing the NPR 7150.2 requirements addressing or including software measurement. This guidance is intended for all persons responsible for the software measurement process from the planning stages through the implementation stages of collection, storage, analysis, and reporting.

# **Think about both of these statements:**

# Management without metrics is just guessing

# and

# "What gets measured, gets managed." - Peter Drucker

# 2. Candidate Software Management Indicators That Might Be Used On A Software Development Project:

* Requirements volatility: The total number of requirements and requirements changes over time.
* Bidirectional traceability: Percentage complete of System-level requirements to Software Requirements, Software Requirements to Design, Design to Code, Software Requirements to Test Procedures
* Software size: planned and the actual number of units, lines of code, or other size measurements over time.
* Software staffing:  planned and actual staffing levels over time.
* Software complexity: the complexity of each software unit. Cyclomatic Complexity (if applicable).
* Software progress:  planned and actual number of software units designed, implemented, unit tested, and integrated over time, code developed.
* Problem/Change (Defect) report status:  total number, number closed, the number opened in the current reporting period, age, severity.
* Software test coverage: a measure used to describe the degree to which the source code of a project is tested by a particular test suite.
* Requirements verified: a measure used to help determine how far along in the implementation and verification phases the project is. This number should be a percentage.
* Build release content:  planned and the actual number of software units released in each build.
* Build release volatility:  planned and the actual number of software requirements implemented in each build.
* Computer hardware and data resource utilization: planned and actual use of computer hardware resources over time.
* Milestone performance:  planned and actual dates of key project milestones.
* Scrap/rework: the number of resources expended to replace or revise software products after they are placed under any level of configuration control above the individual author/developer level.
* Effect of reuse: a breakout of each of the indicators above for reused versus new software products.
* Cost performance: identifies how efficiently the project team has turned costs into progress to date.
* Budgeted cost of work performed: identifies the cumulative work that has been delivered to date.
* Audit performance: Are you following a defined process, how many audits have been completed, audit findings, audit findings open/closed numbers.
* Risk Mitigation: Number of identified software risks, risk migration status, risk probability, risk severity
* Hazard analysis: number of hazard analysis completed, hazards mitigation steps addressed in software requirements and design, number of mitigation steps tested.

Reference Metrics:

[Topic 8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

# 3. Planning the Measurement Activities

When a software lead on a project begins to plan the project's software measurement task, he/she needs to determine what the project's information needs are and how to satisfy them. There are two commonly used methodologies to help a software lead determine these needs. They are the Goal/Question/Metric (GQM) [391](#_tabs-<p></p>) methodology originally developed by Vic Basili of the Software Engineering Laboratory and the similar Goal/Question/Indicator/Metric (GQIM) [392](#_tabs-<p></p>) methodology developed by the Software Engineering Institute.

The first step in both is to define the goals or objectives desired by the project for the measurement task. The goal specifies the purpose of the measurement, the object to be measured (usually a project product, process or resource), the issue to be measured and the viewpoint to be considered. An example of a typical project goal is to ensure that the software is delivered on schedule.

The next step is to refine the goal into questions that break down the issue into its major component. For the timely delivery goal, some questions might be: What is the planned delivery schedule? How much work needs to be completed before the delivery can be made? What is the planned rate of completing that work? Is the project completing the work as planned?

Using the questions, it is possible to determine what metrics can be collected to help answer the questions. Some potential measures might be the planned and the actual schedule as well as the current rate of work compared to the planned rate of work. Using this process to derive the measures is consistent with the GQM methodology.

In the case of the GQIM methodology, there is an extra step after refining the goal into questions in which consideration is given regarding the information to be displayed for easy analysis; in other words, consideration is given to what the charts look like (or what indicators would be helpful). In the above example, several charts might be useful to a software manager such as a Gantt chart with the planned versus actual schedule or an earned value chart showing the value of the work actually performed compared to the value of the work that was planned by this point in the schedule. (A higher-level manager may only be interested in a top-level indicator like a red/yellow/green flag to indicate the project schedule health.) As in the GQM methodology, once the questions and indicators have been determined, the metrics can also be determined.

Planning steps for the software lead are:

**Step 1:** Establish the measurement objectives for the project (See [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements)).

**Step 2:** Identify the measurement analyses that support these objectives (questions, indicators, as above). See [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)

**Step 3:** Specify the measures to be collected (See [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements)).

**Step 4:** Specify the data collection and storage procedures (See [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements)).

**Step 5:** Specify the analysis procedures (See [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements)).

## 3.1 Step 1: Establish the measurement objectives for the project

In order to **establish the measurement** **objectives** or goals of the project, there are usually several things to consider. Typically, software projects are most interested in the following:

* Managing the project with objective data
* Providing data for planning future projects
* Meeting any specific requirements that may have been levied on them

There is often an overlap in the information needed for the items above. For example, Class A and B projects need to consider measurements that might be expected to help satisfy Capability Maturity Model Integration® (CMMI®)  requirements and all classes of software need to comply with the requirements in NPR 7150.2. Measurement objectives that are established for the project are to be consistent with the objectives specified in the NPR and any specific measurement objectives specified by the project's organizational measurement groups.

In addition to the organizational objectives and the NASA requirements, other sources for objectives include management, technical, product, or process implementation needs such as:

* Achieve completion by the scheduled date
* Complete the project within the budget
* Devote adequate resources to each process area

Corresponding objectives might be:

* Measure project progress to ensure that it is adequate to achieve completion by the scheduled date
* Track cost and effort to ensure the project is within budget
* Measure the resources devoted to each process area

Additional sources for information needs and objectives include strategic plans, high-level requirements, the project Software Management Plan and operational concepts.

Once the project has established the measurement objectives and information needs, they are documented in either the project's Software Management Plan (see [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)) or in a separate measurement plan.

## 3.2 Step 2: Identify the measurement analysis that supports these objectives

The software lead **identifies the measurement analyses** that will be done to support the objectives chosen. In order to help with this, think about the questions that need to be answered to provide the needed information. If there are multiple analyses that can be used, prioritize the candidates and select the key analysis that will provide the best information to satisfy the objective. There are resources that could potentially assist with selecting the measurement analyses and also with the selection of the corresponding measures to be collected. Goddard Space Flight Center has a Measurement Planning Table (accessible to NASA users from the SPAN tab in this Handbook)that shows some common objectives with measurement analyses and corresponding measures. The selected analyses are documented in the Software Management Plan or measurement plan, maintaining the traceability to the objectives. Note: Analysis can be as simple as comparing the planned values to the actual values over time. [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)

## 3.3 Step 3: Specify the measures to be collected

Continue to use the methodology and **select the measures needed** to support the analyses and the objectives already chosen. It is helpful to think about what types of indicators or charts are needed in each area. Possibilities include tables, trend charts, stoplight charts, bar chart comparing points in time, etc. The resources listed in Step 2 can assist with the selection of measures. According to [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository), measures are required (at a minimum) to be selected and maintained in the Center’s repository in the following areas:

* Software development tracking data
* Software functionality achieved data
* Software quality data
* Software development effort and cost data

These areas will provide information that can be used in the management of the project, to address objectives such as completion of the project on-time and within budget, delivery of the planned functionality, and delivery of high-quality software. Measures that are selected for the project are defined by name, type, and unit and documented in the measurement plan or Software Management Plan.

Candidate management indicators that might be used on a software development project can include requirements volatility, software size, software staffing, software complexity and more, as shown below (also found in [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements)).

Examples of Measures in Recommended Areas:

1. Progress Tracking Measures - planned vs. actual: cost, effort, schedule milestones, # of units designed, coded, tested; point counting or earned value.
2. Functionality – number of requirements included in build vs. number planned, the number of function points implemented.
3. Quality Measures – number of software problem reports/defects (new, open, closed, severity), number of review item discrepancies (open, closed), number of peer reviews planned vs. actual, number of software audits planned vs. actual, number of software audit findings.
4. Software Volatility Measures – number of software requirements, number of software requirement changes (additions, deletions, modifications), number of software TBDs.
5. Characteristics - project name, language, size of software (SLOC), domain (flight software, ground software, etc.), reuse (% new, modified, reused).
6. Peer Review Measures - time spent on peer review, number of participants and area of expertise, item inspected, #number of defects found (major, minor) types of defects.

## 3.4 Step 4: Specify the data collection and storage procedures

During this step, the project must decide how they are going to handle the logistics of collecting the measurement data they have chosen. The items to be decided and documented for each measurement collected are the following: Who is going to be responsible for collecting the data? How often will it be collected? Where will the responsible person find the data? Is there any data manipulation to be done (i.e., change in units, extraction from one tool and entry into another to produce charts, etc.?) Where will the data be stored? (Consider both the raw data and the resultant charts with analysis). Once the details of collection and storage have been determined, they are documented in a collection and storage procedure that describes these specific details for the project. An example template for a storage and collection procedure can be found in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook. Measurement collection is always easier if there are tools that provide the measures as the work is being performed.

## 3.5 Step 5: Specify the analysis procedures

The final step in planning for measurement is to develop the analysis and reporting procedures. Essentially, this step provides objective data that can be used to evaluate the information provided by the measurement data collected. This type of information can help the project manager determine whether the data shown on the measurement charts is indicating a problem or a good trend.

For many of the types of measurement charts, the analysis will be based on whether the data is within certain expected or planned boundaries as specified in the analysis procedures. For example, to analyze a chart showing cost over time compared with the planned cost, the analysis might be to compare the planned and actual costs and investigate further if the actual cost deviates from the plan by more than 10%. Often to complete the analysis, other measurement charts and information need to be considered. In the case of cost, the next step might be to look at the other information affecting cost. (Is the staffing higher than planned? Have the requirements increased? Did some piece of equipment cost more than planned?)

Another type of boundary that is used for analysis is an organization "norm" for that type of data. For example, an organization might have a normal or expected set of ranges for the numbers of defects found during each test phase. If a project has either considerably more or less defects, during that phase, further investigation is warranted.

Analysis procedures typically specify the thresholds on boundaries used to trigger further investigation. The analysis procedures also specify other charts that might provide a more complete picture of the information being provided by the measurements.

The reporting procedures specify the types of measurement charts that will be reported to each level of management. Typically, the technical software managers need more detailed levels of measurement data and the higher-level managers are more interested in seeing red/yellow/green indicators that only provide an indication of potential problems. When red/yellow/green indicators are used, more detailed data can be made available to support these indicators. An example of an analysis and reporting procedure can be found in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.

Even though reporting procedures are established and implemented, it is important to provide access to the software measurements, analysis results, and development status to sponsoring organizations and other groups tasked to review or assess software development progress and quality.  The needs of these groups may not be fully covered in standard reports, may not require the effort needed to generate separate reports, or may be better met with access to the raw data (see [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis)).

## 3.6 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 4. Measurement Activities During the Project

Several primary measurement activities are conducted continuously during and throughout the project:

* Collect the measurement data
* Analyze the collected data
* Take appropriate corrective actions, based on the data
* Store collected data and analysis results
* Communicate the results to the project team and appropriate management/organizations

During the **collection of the measurement data**, the responsible measurement person collects all the measurement data as specified in the project's Software Management Plan, or measurement collection and storage plan, and performs any of the data manipulations to produce the charts and graphs that have been specified in the plan. Different types of data will be collected at different points in the project's life cycle and at different intervals. For example, earned value information may be collected in all phases of the project, but other progress tracking information such as units designed versus units planned or the number of tests performed/passed versus the number of tests planned would be collected only in the design or test phase, respectively. The raw data is stored for potential further analysis later in the project or for use by the organization to establish baselines.

Once the data has been collected and put into the planned charts or tables, the software manager will need to **analyze the collected data** (see [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data)). The software manager uses the guidelines established in the analysis and reporting procedure developed during the planning process. The purpose of the data analysis is to get an objective view of the project's health and to determine whether there are any issues that may need corrective action. In order to determine the full status of the project, it is often necessary to consider several sources of information together. For example, a progress tracking chart may show that several subsystems are not being implemented as quickly as planned. If the staffing chart showing the planned versus actual staffing is examined, it may show that the staffing level has fallen way below the effort planned. Now the software manager may need to investigate further to determine whether to **take corrective action**. It is possible that several team members have been on vacation or have spent a portion of their time on another project. This may have been a temporary problem, but it could affect the delivery date. Another possibility is that the team has lost one or more members. In this case, the manager may need to bring on additional staff or adjust the delivery date.

Another example of a situation where measures can highlight an issue for the software manager is shown in the following case of defect data during testing. Analysis of defect data that shows the number of defects open versus the number of defects closed and the number of new defects may show that a large number of defects are still open and that new defects are still being discovered. This would indicate that the project is not close to completing this test cycle. If the project had planned to end testing shortly and deliver the software, the software manager may need to extend the delivery schedule or plan for an additional build to fix the remaining errors.

It may be helpful to see the data represented in different ways to obtain a complete analysis of a situation. Using trend-charts rather than a point in time charts often provide more useful information to help in determining whether corrective action is required. In the previous case of defect data, one chart representation might be simply to show the number of defects that were opened or closed for the week. A more useful representation might show the trend of the total number opened and closed over several weeks.

Analysis of the measurement charts is recorded with the measurement charts and both charts and analyses are stored together. Since the raw data was stored previously when it was collected, the project now has both the **measurement data and its analysis stored** for future reference.

During all phases of the project, the software manager reviews the measurement data regularly, analyzing it to determine whether any corrective action is necessary on the project. These activities occur whenever there is a need to determine the health of the project.

At regular intervals during the project, the software manager reports measurement results to appropriate stakeholders. However, when the software manager does the regular reporting to his team, customers, line managers or other interested stakeholders, he will want to use some of the measurement charts to show how the project is progressing. The software manager chooses the measurement charts that are most applicable for the phase of the project and most useful for the particular stakeholder. For example, the line managers and mission project managers are generally interested in knowing whether the project is on schedule and within budget. A line manager who helps assign staffing will be interested in seeing the staffing profiles. A requirements volatility chart is probably the most interesting during the requirements and early design phases.

Often the higher-level managers are not interested in actually seeing detailed measurement charts, but would like to see red/yellow/green indicators of status or trend arrows to show the general direction a project is going. If the indicators do not all indicate a positive status, then the prudent software manager is prepared to describe the situation using the more detailed measurement information he has already analyzed.

NASA-specific measurement and analysis process information is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.

## 4.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 5. Project Completion

At the end of the project, all the measurement data on the project is archived along with the rest of the project information. Selected measurement data is sent to the organizational measurement team who will use this data to create planning models to describe the expected behavior of projects. For the purposes of this collection, project completion is generally defined as the delivery of the final version of the system for operations and maintenance. Typical data collected organizationally includes the project cost and size estimates with the corresponding assumptions (initial estimates, as well as those re-estimates made at milestones), milestone dates, the effort by phase, size of the system as implementation progresses and completes, number of requirements and number of changes, and defects per testing phase. See also [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository).

This type of information across a number of similar projects can provide baselines that future projects can use for comparison with their measurement results. The collection of the estimation data throughout the project and the actual size and effort data at completion will provide information on the accuracy of the estimates and will help refine future estimates on similar projects. [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) includes additional features and advantages of collecting and retaining measurements, some of which are shown below:

Motivation – Involving employees in the whole process of goal setting and increasing employee empowerment. This increases employee job satisfaction and commitment.

Better communication and coordination – Frequent reviews and interactions between superiors and subordinates help to maintain harmonious relationships within the organization and also to solve many problems.

Clarity of goals:

* Subordinates tend to have a higher commitment to the objectives they set for themselves than those imposed on them by another person.
* Managers can ensure that the objectives of subordinates are linked to the organization's objectives.
* Everyone will have a common goal for the whole organization.

See also [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report).

## 5.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 6. Roles

| **Role** | **Responsibility** |
| --- | --- |
| Software Project Lead | Prepares a measurement plan, ensures measures are collected and stored as planned, analyzes measures and takes appropriate actions, reports measurement results to appropriate stakeholders. Responsible for using measurements to assist with the management of the software project. |
| Project Measurement Support Person | Collects measurements from project members and project tools, stores measures in the specified storage location generates measurement charts ready for analysis. |
| Project members | Supplies measurement data and populates tools designed to capture measurement data. |
| SEPG Lead or organizational measurement team representative | Provides the software project with the organizational measurement objectives and the organizational defined set of measures. Collects the organizational defined set of measures, analyzes the data across projects and develops organizational models to aid in evaluating project performance and to identify opportunities for process improvement. |
| Relevant line and project managers | Review measurement reports and analysis results to identify any areas that need higher-level management attention. |

# 7. Resources

## 7.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-367)

  [IEEE Standard Dictionary of Measures of the Software Aspects of Dependability,](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1634994 "Click to open in new window")

  IEEE Computer Society, Sponsored by the Software Engineering Standards Committee, IEEE Std 982.1™-2005, (Revision of IEEE Std 982.1-1988),
* (SWEREF-391)

  [The Goal Question Metric Approach,](http://www.cs.umd.edu/~mvz/handouts/gqm.pdf "Click to open in new window")

  Basili, V., Caldiera, G. and Rombach, H. D., Institute for Advanced Computer Studies, Department of Computer Science, University Of Maryland, College Park, Maryland. FB Informatik, Universität Kaiserslautern, Kaiserslautern, Germany.
* (SWEREF-392)

  [Goal-Driven Software Measurement,](http://www.sei.cmu.edu/library/abstracts/reports/96hb002.cfm "Click to open in new window")

  Park, R., Goethert, W., and Florac, W. CMU/SEI-96-HB-002.
* (SWEREF-413)

  [NASA Earned Value Management (EVM) Website.](http://evm.nasa.gov/ "Click to open in new window")
