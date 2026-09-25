# 5.05 - Metrics - Software Metrics Report

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695659. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report

5.05 - Metrics - Software Metrics Report

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695659)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695659&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Minimum Recommended Content](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)

Return to [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)

# 1. Minimum Recommended Content

Minimum recommended content for the Software Metrics Report. 

1. Software progress tracking measures.
2. Software functionality measures.
3. Software quality measures.
4. Software requirement volatility.
5. Software characteristics.

An example set of software progress tracking measures include, but are not limited to:

1. 1. Software resources, such as budget and effort (planned vs. actual).
   2. Software development schedule tasks (e.g., milestones) (planned vs. actual).
   3. Implementation status information (e.g., number of computer software units in design phase, coded, unit tested, and integrated into computer software configuration item vs. planned).
   4. Test status information (e.g., number of tests developed, executed, passed).
   5. Number of replans/baselines performed.

An example set of software functionality measures include, but are not limited to:

1. 1. Number of requirements included in a completed build/release (planned vs. actual).
   2. Function points (planned vs. actual).

An example set of software quality measures include, but are not limited to:

1. 1. Number of software Problem Reports/Change Requests (new, open, closed, severity).
   2. Review of item discrepancies (open, closed, and withdrawn).
   3. Number of software peer reviews/inspections (planned vs. actual).
   4. Software peer review/inspection information (e.g., effort, review rate, defect data).
   5. Number of software audits (planned vs. actual).
   6. Software audit findings information (e.g., number and classification of findings).
   7. Software risks and mitigations.
   8. Number of requirements verified or status of requirements validation.
   9. Results from static code analysis tools.

An example set of software requirement volatility measures include, but are not limited to:

1. 1. Number of software requirements.
   2. Number of software requirements changes (additions, modifications, deletions) per month.
   3. Number of "to be determined" items.

An example set of software characteristics include, but are not limited to:

1. 1. Project name.
   2. Language.
   3. Software domain (flight software, ground software, Web application).
   4. Number of source lines of code by categories (e.g., new, modified, reuse) (planned vs. actual).
   5. Computer resource utilization in percentage of capacity.

Other information may be provided at the supplier's discretion to assist in evaluating the cost, technical, and schedule performance; e.g., innovative processes and cost reduction initiatives.

# 2. Rationale

The Software Metrics Report (SMR) provides data to the project for the assessment of software cost, technical, and schedule progress. The reports provide a project or software lead:

* Tracking measures to indicate progress achieved to date and relates them to cost.
* Functionality measures to indicate the capabilities achieved to date.
* Quality measures to indicate the degree to which checks and inspections have found and removed problems and defects in the software.
* Requirements volatility measures to indicate current project/product stability and the potential for future iterations and changes in the product.
* Software characteristics to help to uniquely identify the project and its work products, along with its major features.

Measurement is a key process area for successful management and is applied to all engineering disciplines. Measurement helps to define and implement more realistic plans, as well as to monitor progress against those plans. Measurement data provides objective information that helps project management to perform the following:

* More accurately plan a project or program that is similar to one that has been completed.
* Identify and correct problems early in the life cycle (more proactive than reactive).
* Assess impact of problems that relate to project or program objectives.
* Make proper decisions that best meet program objectives.
* Defend and justify decisions.

These metrics serve as the major foundation for efforts to manage, assess, correct, report, and complete the software development activities. Since a computer software configuration item (CSCI) is a group of software that is treated as a single entity by a configuration management system, it is the lowest level of a product that can be effectively tracked. The SMR typically uses this CSCI information to aggregate management metrics for current project statusing and future project planning.

See also Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews),

# 3. Guidance

The SMR captures all the information that results from exercising and completing the requirements for [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements), [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository), [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data), [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data), and [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis).

The SMR serves as a single repository for collecting the information developed from these activities and saving and presenting them to the appropriate stakeholders and project personnel. They result from the chosen measurement objectives (see [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements)) and provide a view into the types of actions or decisions that may be made based on the results of the analysis and help prioritize the areas where measures need to be collected. [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) calls for the project to develop and record measures in software progress tracking, software functionality, software quality, software requirements volatility, and software characteristics. [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) indicates that data collection and storage procedures are specified and that the data itself needs to be then collected and stored. According to [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data), the collected software measures are to be analyzed with project- and Center-approved methods. Finally, [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis) calls for the results to be periodically reported and for access to the measurement information to be made available. All of this information may feed into Mission Directorate measurement and metrics programs (see [SWE-095 - Report Engineering Discipline Status](/spaces/SWEHBVD/pages/102695482/SWE-095+-+Report+Engineering+Discipline+Status)).

See also Topic [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects). See also [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products),

## 3.1 Software Tracking Measures

Typically, the most common reason for implementing a measurement program is to track progress, one of the hardest things to do effectively. Consider the following four attributes for selecting effective tracking measures:

* Objectivity: The measurement needs to be based on criteria that are observable and verifiable.
* Near Real Time: The measurement reflects what is happening now in the project.
* Multiple Levels: The measure needs to have both drill-down capability and be able to be rolled up to summary levels.
* Prediction: The measure must support projections about future progress.

An example set of measures for tracking the project are shown in the recommended content:

1. **Software resources, such as budget and effort (planned vs. actual).** Manpower and dollar planning levels are typically found in the project plan or the Software Development or Management Plan.  Actuals are available from the task reports and time card charges. Tools such as Earned Value management are useful for interpreting these measures to determine project impacts and accomplishments.
2. **Software development schedule tasks and milestones (planned vs. actual).** Milestones that describe life cycle phase completions, major work product events, and code deliveries are managed by a comparison of planned vs. actual dates. Other key milestones may also be selected for tracking to manage risk and safety activities (see [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule), also [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule)).
3. **Implementation status information, e.g., number of computer software units in design phase, coded, unit tested, and integrated into CSCI vs. planned.** Quantitative measures that describe progress can be easily counted and reported. Variations of actual results from planned results indicate problem and risk areas.
4. **Test status information, e.g., number of tests developed, executed, passed.** Software unit testing and systems testing are a strong indicator that design and coding activities are being completed. The execution and passing of tests indicate the quality of the resulting work products.
5. **Number of replans/baselines performed.** Increased numbers of replans or rebaselining indicate a project in flux. Lengthening times between replans and rebaselines indicate a project that has a settled set of requirements and one that is closer to completion.

## 3.2 Software Functionality Measures

"Function measurement methods rely on some definition of what constitutes software functionality." [365](#_tabs-<p></p>)  "Function Point Analysis has been proven as a reliable method for measuring the size of computer software. In addition to measuring output, Function Point Analysis is extremely useful in estimating projects, managing change of scope, measuring productivity, and communicating functional requirements." [203](#_tabs-<p></p>)

1. **Number of requirements included in a completed build/release (planned vs. actual).** The tracking of completed requirements assists in the verification and validation activities. Consideration for assigning weighted values to each requirement may provide a better insight into the true level of completion of the software development activities.
2. **Function Points (planned vs. actual).** The identification of and planned completion rates or dates for function points vs. actual results indicates the level of control being maintained on the complexity and the productivity of the software. Care must be taken to define and count function points in a common manner across all the organizations developing software. In addition, the reporting and recording needs to include sufficient information for the user or reader of the SMR to understand the function point reporting methodology.

## 3.3 Software Quality Measures

"Historically, software quality metrics have been the measurement of exactly their opposite-that is, the frequency of bugs and defects." [232](#_tabs-<p></p>)  Crosby has defined software quality as conformance to a specification. [169](#_tabs-<p></p>)

1. **Number of software Problem Reports/Change Requests (new, open, closed, severity).** The Center or project configuration management system, the change management process, and the problem reporting and corrective action systems need to be described in consistent terms. If other or additional nomenclature or measures (new, open, closed, severity) are used, explain them in the SMR.
2. **Review of item discrepancies (open, closed, and withdrawn).** Actual discrepancy reports and their storage procedures are the source for this metric input. Sufficient references and or citations are needed to enable readers or users of the SMR to find individual reports.
3. **Number of software peer reviews/inspections (planned vs. actual).** This information comes from the Software Development or Management Plan and from periodic reports and status meetings on peer reviews.
4. **Software peer review/inspection information, e.g., effort, review rate, defect data.** This information is defined in the Software Development or Management Plan and from periodic reports and status meetings.
5. **Number of software audits (planned vs. actual).** This information is defined in the Quality Assurance Plan and from periodic reports and status meetings (see [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance)).
6. **Software audit findings information, e.g., number and classification of findings.** This information is defined in the Quality Assurance Plan and from periodic reports and status meetings.
7. **Software risks and mitigations.** This information is typically a summary of the risk management system and related tracking reports for risk mitigation (see [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management)).
8. **Number of requirements verified or status of requirements validation.** This information is typically a summary of verification and validation (V&V) activities, testing reports, and completed design reviews.
9. **Results from static code analysis tools.** The importance given to the analysis results from using the static analyzers indicates a confidence in this type of quality assurance activity. Methods for reporting these results are based on the tool outputs and the project's needs. Again, sufficient descriptive information needs to be included to make these metrics understandable to the user.

## 3.4 Software Requirement Volatility

"The identified causes of requirements volatility include presence of inconsistencies or conflicts among requirements; evolving user/customer knowledge and priorities; project concurrent activities like defect fixing, functionality correction; technical, schedule or cost related problems; change in work environment; and process model selection decisions." [347](#_tabs-<p></p>)

1. **Number of software requirements.** Indicate the source of the identified requirements, e.g., the Software Requirements Specification, lower level specifications. Describe if the count is by unique paragraph (line) number or by the number of "shall" statements. (Unfortunately, not all requirements specifications practice good requirement writing techniques by having only one 'shall" per paragraph (line).)
2. **Number of software requirements changes (additions, modifications, deletions) per month.** The SMR may include trend lines for running averages, life cycle phases, or annual totals. Describe the metric, especially if time periods other than or in addition to the requested 'per month' period are used.
3. **Number of To Be Determined items.** Be careful to differentiate between To Be Revised (i.e., an approximate or initial condition value exists) and To Be Determined (entry is blank) values.

## **3.5 Software Characteristics**

Software characteristics are sometimes called software attributes. These basic characteristics are necessary for developing cost models, planning aids, and general management principles. [329](#_tabs-<p></p>)   A simple X-row by Y-column table can be used to capture and effectively display this information.

1. **Project name.** Consider if there are naming conventions or if additional informative material is needed to differentiate between similarly entitled projects.
2. **Language.** Larger projects may use multiple languages. Identify versions and service pack information, if appropriate.
3. **Software domain (flight software, ground software, Web application).** Identify plans to use software in multiple domains.
4. **Number of source lines of code by categories, e.g., new, modified, reuse, (planned vs. actual).** Include counting methodologies and conventions to assure numbers are provided on a common basis.
5. **Computer resource utilization in percentage of capacity.** Allot enough space in the SMR if this utilization varies by software domain, life cycle phase, or any other discriminator.

## 3.6 Formats

The SMR can be provided in an electronic format or via access to the software metric data repository. It is preferred that the software metric data be provided in an electronic format or method. This document does not have to be a formal hard copy Data Requirement Document if electronic access of the information is provided. It is also acceptable for an organization to provide this information as a part of a monthly software review process. The final set of metrics used by a project needs to be determined by the project and organizational needs and the software development life cycle phase. Which software metrics are reported at what point in the development or maintenance life cycle needs to be addressed in the software planning documents or organizational planning documents.

## 3.7 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

This guidance lists a minimum recommendation for providing five areas of information on a Computer Software Configuration Item (CSCI) basis. Smaller projects may consider providing less information than listed in the example sets for each information item. The information included in the SMR needs to be sufficient to manage the project, manage risk, and maintain safety throughout the project's life cycle.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-151)

  [An Axiomatic Approach of Software Functionality Measure,](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=243908&userType=inst "Click to open in new window")

  Chen, Yuan-Tsong; Tanik, Murat M.; Southern Methodist University, Dallas, TX IEEE0-8186-3520-7/92, 1992. Published in: 1992 Proceedings - The Third International Workshop on Rapid System Prototyping
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-169)

  [Quality Is Free: The Art of Making Quality Certain.](https://www.amazon.com/Quality-Free-Certain-Becomes-Business/dp/0070145121 "Click to open in new window")

  Crosby, P.B. New York, McGraw-Hill, 1979.
* (SWEREF-188)

  [Software Quality Measurement: A Framework for Counting Problems and Defects,](http://www.sei.cmu.edu/reports/92tr022.pdf "Click to open in new window")

  Florac, William; CMU/SEI-92-TR-022, Software Engineering Institute. 1992.
* (SWEREF-203)

  [An Introduction to Function Point Analysis,](http://www.qpmg.com/fp-intro.htm "Click to open in new window")

  Heller, Roger, Q/P Management Group, Inc. 2002,
* (SWEREF-232)

  [Software Quality Metrics,](http://www.developer.com/tech/article.php/3644656/Software-Quality-Metrics.htm "Click to open in new window")

  Jayaswal, Bijay, and Patton, Peter. (2006). Developer.com.
* (SWEREF-252)

  [Software Metrics: SEI Curriculum Module SEI-CM-12-1.1.](http://www.sei.cmu.edu/reports/88cm012.pdf "Click to open in new window")

  Mills, Everald E. (1988). Carnegie-Mellon University-Software Engineering Institute.  Retrieved on December 2017 from http://www.sei.cmu.edu/reports/88cm012.pdf.
* (SWEREF-287)

  [Analysis of Requirements Volatility during Software Development Life Cycle,](https://opus.lib.uts.edu.au/handle/10453/2603 "Click to open in new window")

  Nurmuliani, N; Zowghi, Didar; Fowell, Sue. Proceedings of the 2004 Australian Software Engineering Conference, 2004, pp. 28 - 37, University of technology, Sydney, ASWEC'04, 2004.
* (SWEREF-329)

  [Software Measurement Guidebook,](https://ntrs.nasa.gov/search.jsp?R=19980228474 "Click to open in new window")

  Technical Report - NASA-GB-001-94 - Doc ID: 19980228474 (Acquired Nov 14, 1998), Software Engineering Program,
* (SWEREF-336)

  [Software Metrics Capability Evaluation Guide,](http://www.dtic.mil/docs/citations/ADA325385 "Click to open in new window")

  Software Technology Support Center (STSC) (1995), Hill Air Force Base. Accessed 6/25/2019.
* (SWEREF-347)

  [Understanding Requirements Volatility in Software Projects,](http://ieeexplore.ieee.org/Xplore/login.jsp?url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F5428222%2F5428274%2F05428606.pdf%3Farnumber%3D5428606&authDecision=-203 "Click to open in new window")

  Thakurta, Rahul; Ahlemann, Frederick, Proceedings of the 43rd Hawaii International Conference on System Sciences, 2010. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-355)

  [12 Steps to Useful Software Metrics,](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics_in_12_steps_paper.pdf "Click to open in new window")

  Westfall, Linda, The Westfall Team (2005),   Retrieved November 3, 2014 from http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics\_in\_12\_steps\_paper.pdf
* (SWEREF-365)

  [Conceptualizing Measures of Required Software Functionality,](http://www.cc.uah.es/ssalonso/papers/Ontose07.pdf "Click to open in new window")

  Lopez, C., Cuadrado, J.J. and Sánchez-Alonso, S. (2007). In Proceedings of ONTOSE 2007 -Second International Workshop on Ontology, Conceptualizations and Epistemology for Software and Systems Engineering.
* (SWEREF-448) Software Process Improvement Plan EI32-SPIP,  Revision F, NASA Marshall Space Flight Center (MSFC) Flight Software Branch, 10-26-2010.  Replaces SWEREF-058

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-022 - Software Assurance](/spaces/SWEHBVD/pages/102695407/SWE-022+-+Software+Assurance) * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-090 - Management and Technical Measurements](/spaces/SWEHBVD/pages/102695475/SWE-090+-+Management+and+Technical+Measurements) * [SWE-091 - Establish and Maintain Measurement Repository](/spaces/SWEHBVD/pages/102695477/SWE-091+-+Establish+and+Maintain+Measurement+Repository) * [SWE-092 - Using Measurement Data](/spaces/SWEHBVD/pages/102695478/SWE-092+-+Using+Measurement+Data) * [SWE-093 - Analysis of Measurement Data](/spaces/SWEHBVD/pages/102695480/SWE-093+-+Analysis+of+Measurement+Data) * [SWE-094 - Reporting of Measurement Analysis](/spaces/SWEHBVD/pages/102695481/SWE-094+-+Reporting+of+Measurement+Analysis) * [SWE-095 - Report Engineering Discipline Status](/spaces/SWEHBVD/pages/102695482/SWE-095+-+Report+Engineering+Discipline+Status)        * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.14 - Implementing Measurement Requirements and Analysis for Projects](/spaces/SWEHBVD/pages/102695648/7.14+-+Implementing+Measurement+Requirements+and+Analysis+for+Projects) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Metrics](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Metrics) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.11 Software Measurements](/spaces/SWEHBVD/pages/133235387/A.11+Software+Measurements) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
