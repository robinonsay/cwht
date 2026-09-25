# 5.01 - CR-PR - Software Change Request - Problem Report

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695655. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report

5.01 - CR-PR - Software Change Request - Problem Report

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695655)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695655&showCommentArea=true&showComments=true#addcomment)

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

The Software Change Request/Problem Report provides a means for identifying and recording the resolution to software anomalous behavior, process non-compliance with plans and standards, and deficiencies in life cycle data or for identifying and recording the implementation of a change or modification in a software item.

Minimum recommended content for the Software Change Request - Problem Report. 

1. 1. Identification of the software item.
   2. Description of the problem or change to enable problem resolution or justification for and the nature of the change, including: assumptions/constraints and change to correct software error.
   3. Originator of Software Change Request/Problem Report and originator's assessment of priority/severity.
   4. Description of the corrective action taken to resolve the reported problem or analysis and evaluation of the change or problem, changed software configuration item, schedules, cost, products, or test.
   5. Life cycle phase in which problem was discovered or in which change was requested.
   6. Approval or disapproval of Software Change Request/Problem Report.
   7. Verification of the implementation and release of modified system.
   8. Date problem discovered.
   9. Status of problem.
   10. Identify the person or organization assigned to investigate and implement a solution for the problem.
   11. Identify any safety-related aspects/considerations/impacts associated with the proposed change and/or identified problem.
   12. Configuration of system and software when problem is identified (e.g., system/software configuration identifier or list of components and their versions).
   13. Any workaround to the problem that can be used while a change is being developed or tested.

# 2. Rationale

Using standard formats for capturing requests for changes and problems found with software allows review boards (e.g., Change Control Boards or Configuration Control Boards) to have a standard format for reviewing and dispositioning the requests/reports. Including required content in these standard formats also helps capture the important information needed to review and resolve the documented change or problem. Capturing descriptions, dates, and corrective actions provides for a complete picture of the request, its resolution, and its progress (for tracking purposes). This information can be critical to project management. Some captured information may also allow for trending (life cycle phase), estimation of future efforts (date found, date resolved) for similar issues, and lessons learned.

# 3. Guidance

**NASA Software Safety Guidebook - NASA-GB-8719.13**

4.3.6 Products from the Development Process - Problem or Anomaly Reports  
"unexpected behavior of the software or system, the analysis performed to determine the cause, and what was done to correct the problem. Projects usually have a formal system for problem reports after the software has reached a level of maturity. However, defects or problems that occur before this time are also important. Tracking these problems, or at least reviewing them to make sure no major defect slips through, is recommended in safety-critical systems."[276](#_tabs-<p></p>)

"Discrepancy Reports (DR) and Problem Reports (PR) contain a description of each problem encountered, recommended solutions, and the final disposition of the problem." This is typically minimal content for a change request or problem report. Recommended content is intended to capture:

* Information that describes what needs to be changed and why.
* Information necessary to process the request, e.g., by a Change Control Board or Configuration Control Board (CCB).
* Information needed to authorize the change.
* Information needed to determine the impact and necessity of the change.

Typically, change requests are initiated by the person finding the problem, such as the customer, developer, or tester. These reports are reviewed for safety implications; therefore, the content needs to be as clear and as complete as possible.

For contracted software development, required problem report/change request content needs to be included in any contract or Memorandum of Agreement/Memorandum of Understanding (MOA/MOU) so that contractors (providers) capture the required information in their reporting systems.

Projects may choose to use change tracking, change management, problem reporting, or other tools to capture and manage change requests and problem reports to closure (see [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes)). These tools may also facilitate metrics capture and trending. Most tools allow some type of customization such that the project's required information can be captured and managed within the tool. Projects may want to prepopulate fields using defined choices or example text to ensure only allowable values are chosen. When choosing a change request or problem report tool, consider the information that must be captured and the ability of the tool to collect or be configured to collect that information. See also [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances).

If a tool is not used, a project may want to capture in the appropriate project documentation project-defined choices for change request/problem report fields that lend themselves to defined lists. This practice limits field content to acceptable project values and helps ensure change request/problem report uniformity.

Guidance for individual elements of the recommended change request/problem report content is included below:

**Identification of the software item** – name and version of configuration item (code module, document, test, or other item).

**Description of the problem or change to enable problem resolution or justification for and the nature of the change, including assumptions/constraints and change to correct software error** – description of the problem, including steps to reproduce the issue, data entered, expected results, actual results, what the user sees or experiences; need for the requested change, including relevant details to explain the reason for the change.

**Originator of Software Change Request/Problem Report** – originator's name, organization, and contact information.

**Originator's assessment of priority/severity** – originator's opinion regarding urgency of the problem or requested change; may not be the same as the development organization's assessment since originator and developer have different perspectives; may be one of high, major, low, or any other defined criteria that can be used to classify the request/report. See also [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels).

**Description of the corrective action taken to resolve the reported problem or analysis and evaluation of the change or problem, changed software configuration item, schedules, cost, products, or test** – description of the changes made to address the change request or problem report; description of any associated problem analysis, such as an impact analysis; list of changed configuration items, including code modules, test documentation, requirements, design, and other project documents. See also [SWE-203 - Mandatory Assessments for Non-Conformances](/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances).

**Life cycle phase in which problem was discovered or in which change was requested** – for example, Phase B (Preliminary Design), Phase E (Operations & Sustainment); or requirements, design, development/implementation, integration test, etc.

**Approval or disapproval of Software Change Request/Problem Report** – disposition of the request/report, typically from a configuration control board (CCB); additional details such as urgency category, disposition date, priority (high, medium, low), severity (inconvenience, halts operation, safety issue, security issue), comments.

**Verification of the implementation and release of modified system** – unit, integration, system tests run to verify the change and their respective results; test witnesses, if appropriate; name of verifier; date of verification; released software version that contains the change; release date.

**Date problem discovered** – date of request or date when problem first surfaced.

**Status of problem** – current status of the change request/problem report using predefined status values such as new, analysis, assigned, implemented, tested, closed; will change as the request is processed and the problem or change is addressed and moved to resolution; could include status change date for tracking purposes.

**Identify the person(s) or organization assigned to investigate and implement a solution for the problem** – name of the person(s) or organization assigned to investigate the change request/problem report. If a solution is found, identify who will be implementing the solution/fix and resolving the problem.

**Identify any safety-related aspects/considerations/impacts associated with the proposed change and/or identified problem** – description of features, effects, impacts, behavior, or other factors related to or which affect or could affect the safety of the software or system.

**Configuration of system and software when problem is identified, e.g., system/software configuration identifier or list of components and their versions** – software version, system configuration/setup, installed options/components, hardware configuration; when dealing with embedded system development, capture board serial numbers, FPGA (Field Programmable Gate Array) version numbers, simulator version numbers, etc.; when developing for PCs, important configuration information includes brand/make, ancillary cards, and drivers installed.

**Any workaround to the problem that can be used while a change is being developed or tested** – steps to keep system functioning without triggering the problem while the problem is addressed and corrected.

Additional information may be captured based on project needs, tracking requirements, data for metrics, or other reasons. Sample information includes:

* Change request/problem report number/identifier; unique identifier.
* Brief title or description for the request/report.
* Date entered - date report submitted; may not be same as date problem discovered.
* Project name or identifier, if change request/problem reports for multiple projects are captured in a single tool.
* Requirements statement, if request is for enhancement.
* Attempts to repeat the problem (not typical for customer-entered reports but expected for testers).
* Witnesses, observers (may be able to provide analysis data from their perspective).
* Attachments – additional explanatory data such as test data or results.
* Additional comments.
* Detailed analysis data, e.g., analysis effort, recommendation, analyst name, completion date, analysis text, root cause (problem reports only).
* Assigned developer.
* Effort spent designing, implementing, testing the change or correction.
* Type of change: logic, interface, data, computation, or other defined change category.
* Lines of code (LOC) affected by the change.
* Affected baseline: functional, allocated, product.
* Date completed.

3.1 Typical Usage

This document is typically used in the following other Topics and SWEs

* [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) for change management
* [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) for reporting problems
* [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) for tracking problems
* [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) for change requests
* [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) for tracking corrective action
* [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) for tracking changes
* [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) for change control
* [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting) for change tracking
* [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management)
* [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) for change tracking
* [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) for change tracking
* [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics) for change tracking

3.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

Projects with limited budgets may consider using simple tools such as document templates (MS Word) to capture change requests/problem reports and spreadsheets or simple databases for tracking and metrics generation. Another option is to determine if any tools are available at the Center level or from previous projects that can be used at no or low cost to the current project.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-216)

  [828-2012 - IEEE Standard for Configuration Management in Systems and Software Engineering](https://ieeexplore.ieee.org/document/6197683 "Click to open in new window")

  IEEE STD IEEE 828-2012, 2012.,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-329)

  [Software Measurement Guidebook,](https://ntrs.nasa.gov/search.jsp?R=19980228474 "Click to open in new window")

  Technical Report - NASA-GB-001-94 - Doc ID: 19980228474 (Acquired Nov 14, 1998), Software Engineering Program,
* (SWEREF-343)

  [STEP Level 2 Software Configuration Management and Data Management course, SMA-SA-WBT-204, SATERN (need user account to access SATERN courses).](https://saterninfo.nasa.gov/ "Click to open in new window")

  This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-519)

  [Pre-Flight Problem/Failure Reporting Procedures](https://llis.nasa.gov/lesson/733 "Click to open in new window")

  Public Lessons Learned Entry: 733.
* (SWEREF-520)

  [Problem Reporting and Corrective Action System](https://llis.nasa.gov/lesson/738 "Click to open in new window")

  Public Lessons Learned Entry: 738.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-054 - Corrective Action for Inconsistencies](/spaces/SWEHBVD/pages/102695439/SWE-054+-+Corrective+Action+for+Inconsistencies) * [SWE-080 - Track and Evaluate Change](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics) * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances) * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [SWE-203 - Mandatory Assessments for Non-Conformances](/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Configuration Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Configuration+Management)      * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) * [A.08 Software Configuration Management](/spaces/SWEHBVD/pages/133235384/A.08+Software+Configuration+Management) * [A.12 Software Non-conformance or Defect Management](/spaces/SWEHBVD/pages/133235388/A.12+Software+Non-conformance+or+Defect+Management) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

* **Pre-Flight Problem/Failure Reporting Procedures. Lesson Number 0733[519](#_tabs-<p></p>)**: Impact of Non-Practice states: "Without ... formal reporting procedures, problems/failures, particularly minor glitches, may be overlooked or not considered serious enough to investigate or report to Project Management. This could result in recurrence of the problem/failure during the mission and result in significant degradation in performance."
* **Problem Reporting and Corrective Action System. Lesson Number 0738[520](#_tabs-<p></p>)**: Impact of Non-Practice states: "Hardware/software problems that require further investigation may not be identified and tracked. Development of corrective action and need for improvement will not be highlighted to engineering. Opportunities for early elimination of the causes of failures and valuable trending data can be overlooked." Practice states: "A closed-loop Problem (or Failure) Reporting and Corrective Action System ( PRACAS or FRACAS ) is implemented to obtain feedback about the operation of ground support equipment used for the manned spaceflight program."

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
