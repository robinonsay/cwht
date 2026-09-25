# 8.17 - Software Safety Audit Checklists

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695755. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists

8.17 - Software Safety Audit Checklists

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695755)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695755&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Process Audit](#tabs-2)
* [3. Activities Checklist](#tabs-3)
* [4. Resources](#tabs-4)

# 1. Introduction

This topic contains checklists for use by Software Assurance and Software  Safety  personnel when they are auditing projects with safety-critical software.  The first checklist, **Software Safety Process Audit Checklist,** is intended to be used primarily with contractor organizations doing the safety-critical software and has more of a focus on the processes in place as well as checking on activities. The second checklist, **Software Safety Activities Checklist for Internal Audits** is intended to be used when the software safety personnel are in-house and focuses more on the compliance with the specific required activities for  safety-critical software.

# 2. Software Safety Process Audit Checklist

The **Software Safety Process Audit Checklist**is intended to be used primarily with contractor organizations doing the safety-critical software and has more of a focus on the processes in place as well as checking on activities.

Click to download a usable copy of this checklist: **[Software Safety Process Audit Checklist](/download/attachments/102695755/Software%20Safety%20Process%20Audit%20Checklist%20Final%20v3.docx?version=1&modificationDate=1647965681000&api=v2).**

|  |  |  |  |
| --- | --- | --- | --- |
| This checklist is designed to check the processes in place for performing software safety activities, either in the contract organization or in the in-house organization. | | | |
| **#** | **Description** | **Y/N** | **O/E** |
| General | | | |
| 1 | Is there a software safety process in place for the development of software? |  |  |
| 2 | Is this process documented? |  |  |
| 3 | Is safety-critical software identified? |  |  |
| 4 | Has a software safety requirements analysis been done? |  |  |
| 5 | Are safety-critical requirements identified? |  |  |
| 6 | Is there CM in place for tracking all software safety-critical requirements? |  |  |
| 7 | Is the software analyzed throughout the design, development, test and the V&V process to verify and validate that the safety design requirements have been correctly and completely implemented? |  |  |
| 8 | Does software design analysis include Fault Tree Analysis (FTA), Failure Modes and Effects Analysis (FMEA), Code/Logic Analysis, & Traceability to assess the adequacy of hazard controls? |  |  |
| 9 | Is there a Safety Assessment Report? Is there end-to-end traceability of software safety activities, from initial system assessment through implementation and verification of Safety-Critical Software Functions (SCSFs), software release, deployment, operations, and maintenance? |  |  |
| 10 | Have the verification methods been identified and applied for each software safety-critical requirement? |  |  |
| 11 | Does the safety organization have work instructions for each task that is performed? |  |  |
| 12 | Does the safety organization participate in milestone and software reviews, including |  |  |
|  | a)    Conceptual review? |  |  |
|  | b)    Requirement review? |  |  |
|  | c)     Design reviews? |  |  |
|  | d)    Code reviews? |  |  |
|  | e)    Test readiness reviews? |  |  |
|  | f)      System acceptance reviews? |  |  |
|  | g)    Peer reviews? |  |  |
| 13 | Has safety/software safety reviewed the SRS? |  |  |
|  | a)    Were safety-critical requirements identified? |  |  |
|  | b)    Are all software controls, mitigations included in the Software Requirements Specification (SRS)? |  |  |
| 14 | Does safety track safety-critical requirements throughout the system lifecycle to ensure they are correctly coded, tested, and verified? |  |  |
| 15 | Is there a current process for formally documenting software safety-critical issues? |  |  |
| 16 | Does the software safety-critical organization review and approve all changes to the software safety-critical requirements during the change review process? |  |  |
| 17 | Is there objective data or evidence that shows the software development organizations followed good software processes? |  |  |
| 18 | Is there objective evidence that the system engineers and hardware engineers have reviewed the software requirements, software design, software testing and participated in the software peer reviews associated with software safety-critical functions? |  |  |
| Hazard Analysis | | | |
| 1 | Does the safety process include a hazard identification and analysis process? |  |  |
| 2 | Are system-level hazards identified and tracked? |  |  |
| 3 | Have all of the software contributions to the system hazard been identified? |  |  |
| 4 | Have software/hardware controls been identified to mitigate software contributions to system hazards? |  |  |
| 5 | Have adequate verification methods been identified for each hazard mitigation? |  |  |
| Requirements Phase | | | |
| 1 | Are all safety-critical software requirements traced through the software products (i.e., software requirements, software design, software code, software test documents)? |  |  |
| 2 | Are the interfaces in an ICD or equivalent clearly defined? |  |  |
| 3 | What was the method for documenting discrepancies in the requirements? Were all discrepancies in the requirements documented in a tracking system? |  |  |
| 4 | Did the safety organization provide objective evidence that all safety-related discrepancies in the requirements review were fixed and closed? |  |  |
| Design Phase | | | |
| 1 | Did safety ensure that all safety-related requirements have been satisfied by the design? |  |  |
| 2 | Is there evidence of closure of all safety-related action items from the software design reviews? |  |  |
| 3 | Did safety participate in design evaluations before release for coding? |  |  |
| 4 | Does the software architecture consistently define and support the implementation of all software safety-critical requirements and all applicable computer-based control system requirements? |  |  |
| 5 | Does the software architecture consistently define and support the implementation of Fault Detection, Isolation, and Recovery functions for all safety-critical activities? |  |  |
| 6 | Does the software design address software fault management functions? |  |  |
| 7 | Does the software design address cybersecurity requirements and functions? |  |  |
| 8 | Are all of the software design functionally traceable to the software requirements? |  |  |
| Coding Phase | | | |
| 1 | Did the software development engineers follow a secure coding standard when creating code? |  |  |
| 2 | Did the safety organization perform traceability from the requirements down to the design and code? |  |  |
| 3 | Was safety involved in the code peer reviews and/or code walkthroughs? |  |  |
| 4 | What was the method for documenting discrepancies in the code? |  |  |
| 5 | Is there objective evidence that all safety-related discrepancies identified in code reviews were fixed and closed? |  |  |
| 6 | Are all of the safety-critical code components below the cyclomatic complexity requirement of 15? |  |  |
| 7 | Is there evidence of repeatable software unit tests for all software safety-critical components? |  |  |
| 8 | Has an independent software code quality risk assessment been done? And is the software code risk acceptable? |  |  |
| Testing Phase | | | |
| 1 | Was the safety organization involved in test peer reviews for safety-critical test cases? |  |  |
| 2 | What were the methods for documenting discrepancies in the test? |  |  |
| 3 | Was traceability performed from the requirements and code to the test cases? |  |  |
| 4 | Was software assurance involved in the test readiness review? |  |  |
| 5 | Is there objective evidence that all safety-related discrepancies in the test reviews are fixed and closed? |  |  |
| 6 | Did software assurance witness all safety-critical formal qualification tests? |  |  |
| 7 | Does the test verify all software safety-critical components? |  |  |
| 8 | Do all software safety-critical components have 100% test coverage? |  |  |
| 9 | Is there objective evidence that the software being used is the same software version tested, including the software configuration items (e.g., software records, code, configuration data, tools, models, scripts)? |  |  |
| System Acceptance Review | | | |
| 1 | Have safety issues been identified, documented, and resolved throughout the software lifecycle? |  |  |
| 2 | Is there evidence that all software changes are tracked and evaluated? |  |  |
| 3 | Is there a plan in place for maintenance, changes, and operations of the software? |  |  |

See also Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis), [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis)

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Software Safety Activities Checklist for Internal Audits

The **Software Safety Activities Checklist for Internal Audits** is intended to be used when the software safety personnel are in-house and focuses more on the compliance with the specific required activities for  safety-critical software.

Click to download a usable copy of this checklist:**[Software Safety Activities Checklist for Internal Audits](/download/attachments/102695755/SW%20Safety%20Activities%20Checklist%20for%20Internal%20Audits%20Final_v3.docx?version=1&modificationDate=1647965688000&api=v2).**

Date(s) of Audit: \_\_\_\_\_\_\_\_\_\_\_\_\_\_               Project: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Auditor(s): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_         Organization Examined: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_                                               \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Software Safety Activities Checklist for Internal Audits

|  |  |  |  |
| --- | --- | --- | --- |
| **This checklist is intended for use in auditing the performance of software safety activities** | | | |
|  | | | |
|  | (Y=Yes, N=No, NA=Not Applicable) | | |
| **#** | **Description** | **(Y / N / NA)** | **w/Comments** |
|  | **General Safety/Software Safety** |  |  |
| **1.** | Has the Project determined that there are safety-critical components in the system using the criteria in NASA-STD-8739.8? |  |  |
| **2.** | Is there a process in place that defines the necessary activities and products for the Software Safety personnel? |  |  |
|  | **Hazard Analysis** |  |  |
| **3.** | Have the Software Safety personnel performed a software Hazard Analysis (HA)? |  |  |
| **4.** | If not, have the Software Safety personnel participated in the System Preliminary Hazard Analysis to help identify where software needs to be included? |  |  |
| **5.** | Have the software contributions to the system hazards been identified? |  |  |
| **6.** | Has there been identification of software and hardware controls to mitigate software contributions to system hazards? |  |  |
| **7.** | Have adequate verification methods been identified for each hazard mitigation to ensure an acceptable level of safety? |  |  |
| **8.** | Has the list of generic software-based hazards, hazard contributions and hazard controls been reviewed to determine whether any of these might be applicable for this project? See the NASA Software Engineering and Assurance Handbook, NASA-HDBK-2203 and Appendix A in NASA-STD-8739.8 for a list of generic software-based hazards. |  |  |
| **9.** | Have any potential software-related risks been identified in the Project Concept or Operational Concept? If so, have mitigations been planned for them? |  |  |
| **10.** | Do your Software Safety personnel and the subcontractor organization share the safety information, if applicable? |  |  |
| **11.** | Did the hazard analysis include any COTS, OTS, OSS, reused or heritage/legacy code? |  |  |
| **12.** | Did the hazard analysis include any cybersecurity considerations? |  |  |
| **13.** | Do the hazard reports include all software hazard causes, software contributions to systems hazards, any software mitigations for the hazards, and adequate verification methods for each hazard to ensure an acceptable level of safety? |  |  |
|  | **Planning Phase** |  |  |
| **14.** | Does the project have software safety resources addressed in project acquisition, planning, management, and control activities? |  |  |
| **15.** | Have the Software Safety personnel confirmed that security has been considered and addressed in all safety-related areas? |  |  |
| **16.** | Does any acquisition of software (either contracted or Commercial- off-the-Shelf (COTS)) include evaluation and assessment of risks due to the software’s contribution to safety and any limitations of the software? |  |  |
| **17.** | Does the acquisition have a plan to address and mitigate any risks identified? |  |  |
| **18.** | Have the Engineering and Safety and Mission Assurance (S&MA) Technical Authorities agreed on the software components that are safety-critical? |  |  |
| **19.** | Is there a Safety Plan in place for the Project? (It can be part of the Software Assurance Plan, Safety and Mission Assurance (SMA) plan, or Software Management/Development Plan) |  |  |
| **20.** | Has the project defined the required software safety requirements to be used by the project? |  |  |
| **21.** | Has the project completed a requirements mapping matrix for all of the software assurance and software safety requirements per NASA-STD-8739.8? |  |  |
|  | **Requirements Phase** |  |  |
| **22.** | Is there a plan to place the software safety products under configuration management? |  |  |
| **23.** | Have the systems/development groups identified the safety related system level, hardware and software requirements? |  |  |
| **24.** | Did the Software Safety personnel attend the Systems Requirements Review? The Software Requirements Review? |  |  |
| **25.** | Have the Software Safety personnel reviewed the Systems and Software Requirements Documents? Have they confirmed that the software-related safety requirements in the Systems Requirements Document have been passed down to the Software Requirements? |  |  |
| **26.** | Have the Software Safety personnel confirmed that the software safety requirements are traced bi-directionally to the system hazards and system requirements? |  |  |
| **27.** | Have the Software Safety personnel confirmed at least one requirement exists for each software hazard control? |  |  |
| **28.** | Have the Software Safety personnel confirmed that the mitigations for any requirements that may affect software/system safety are included in the requirements? |  |  |
| **29.** | Has a requirements safety analysis been performed? |  |  |
| **30.** | Have the Software Safety personnel reviewed the interface documentation for completeness, and consistency? Are any findings documented? |  |  |
| **31.** | Are any findings that may affect software/system safety documented? |  |  |
| **32.** | Is the method for documenting discrepancies in the requirements specified? |  |  |
| **33.** | Do the software requirements include all of the applicable software safety requirements (i.e., SWE-134) and any applicable computer-based control system requirements (SSP 50038)? |  |  |
| **34.** | Do the software requirements address all of the known hazards associated with the software? |  |  |
|  | **Design Phase** |  |  |
| **35.** | Have the Software Safety personnel attended the design peer review(s) for the safety-critical components? |  |  |
| **36.** | Have the Software Safety personnel attended the milestone reviews for the safety-critical software? (Mission Design Review, System Design Review, Preliminary Design Review, Critical Design Review, etc.) |  |  |
| **37.** | Have the Software Safety personnel analyzed the design to verify the requirements in SWE-134 are implemented in the design? |  |  |
| **38.** | Have the Software Safety personnel confirmed that peer reviews are being held for safety-critical components? |  |  |
| **39.** | Have the Software Safety personnel confirmed that maintainability and reliability are being considered in the design? |  |  |
| **40.** | Have any identified issues been addressed? |  |  |
| **41.** | Have the Software Safety personnel performed the safety analysis for design, including analyzing the design for interface code, interrupt code, data code, logic analysis, and partitioning/isolation of safety-critical code? |  |  |
| **42.** | Have the Software Safety personnel confirmed that all the safety related requirements and functions have been implemented in the design? |  |  |
| **43.** | Have the Software Safety personnel evaluated the balance between fault tolerance and failure tolerance? |  |  |
| **44.** | Does software design analysis include Fault Tree Analysis (FTA), and Failure Modes and Effects Analysis (FMEA) to assess adequacy of hazard mitigations (controls)? |  |  |
|  | **Implementation** |  |  |
| **45.** | Do the software Safety personnel participate in software code peer reviews for safety-critical components? |  |  |
| **46.** | Have the Software Safety personnel confirmed that static analysis is being done on the safety-critical components? |  |  |
| **47.** | Have the Software Safety personnel evaluated all change requests for their impact on safety? |  |  |
| **48.** | Have the Software Safety personnel confirmed that the developers are using coding standards that support safety-critical coding practices? |  |  |
| **49.** | Have the Software Safety personnel confirmed the static code analyzer(s) that is being used supports safety-critical coding practices? |  |  |
| **50.** | Has the static code analyzer that is being used been configured properly? |  |  |
| **51.** | Have the Software Safety personnel confirmed that all safety-related design elements are correctly and completely implemented into code? |  |  |
| **52.** | Have the Software Safety personnel reviewed the static code analysis findings and confirmed that all safety-related findings have been addressed? |  |  |
| **53.** | Have the Software Safety personnel reviewed the static code analysis findings and confirmed that all security-related findings have been addressed? |  |  |
| **54.** | Have the Software Safety personnel confirmed that all safety-critical code has been unit tested? |  |  |
| **55.** | Have the Software Safety personnel confirmed that all approved safety-related changes have been implemented and unit tested? |  |  |
| **56.** | Have the Software Safety personnel confirmed that all discrepancies in the code were reviewed, fixed, and closed? |  |  |
| **57.** | Have the Software Safety personnel assessed that the source code satisfies the conditions in the NPR 7150.2, SWE-134 requirement for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone? |  |  |
| **58.** | Have the Software Safety personnel confirmed that all identified safety-critical software components have a cyclomatic complexity value of 15 or lower? |  |  |
| **59.** | If the cyclomatic complexity is not 15 or lower, is there a justification for why the complexity needs to be higher than 15? |  |  |
| **60.** | Have the Software Safety personnel reviewed the implementations of hazard mitigations, controls, constraints, etc.? |  |  |
| **61.** | Have the Software Safety personnel analyzed the interfaces of safety-critical systems for potential safety or security risks? |  |  |
| **62.** | Do the Software Safety personnel participate in test case peer reviews and test procedure peer reviews for safety-critical components? |  |  |
| **63.** | Do the Software Safety personnel participate in Test Readiness Reviews for safety-critical software? |  |  |
|  | **Testing Phases** |  |  |
| **64.** | Have the Software Safety personnel confirmed that the test procedures are bi-directionally mapped to all the safety-related requirements? |  |  |
| **65.** | Have the Software Safety personnel confirmed that the test environment is as close as possible to the operational environment? |  |  |
| **66.** | Have the Software Safety personnel confirmed that software verification and validation activities include software safety verifications and validations? |  |  |
| **67.** | Are the safety features used to mitigate hazards being verified by test? |  |  |
| **68.** | Have the Software Safety personnel confirmed 100% test coverage?  If not, have the Software Engineering personnel provided a risk assessment and an explanation of why 100% coverage cannot be achieved? |  |  |
| **69.** | Are the Software Safety personnel witnessing tests for safety-critical components? If not, is Software Assurance witnessing the testing? |  |  |
| **70.** | Have the Software Safety personnel confirmed that the test set includes both nominal and off-nominal operational scenarios, boundary testing, stress testing, resistance to failure testing and disaster testing?  See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing). |  |  |
| **71.** | Have the Software Safety personnel confirmed that regression testing is adequate and includes retesting of all related safety-critical software code components? |  |  |
| **72.** | Have the Software Safety personnel confirmed regression test procedures are updated to incorporate tests that validate the correction of critical anomalies? |  |  |
| **73.** | Have the Software Safety personnel confirmed that all approved/implemented changes to the requirements, design or code for safety-critical software components have been accounted for in the updates to the test procedures for those components? |  |  |
| **74.** | Have the Software Safety personnel confirmed that the values of the safety-critical loaded data, uplinked data, rules, scripts, and configurations that affect hazardous system behavior have been tested or verified? |  |  |
|  | **Acceptance and Delivery** |  |  |
| **75.** | Did the Software Safety personnel participate in the System/Software Acceptance Review? |  |  |
| **76.** | Have the Software Safety personnel confirmed that all safety issues identified throughout the lifecycle have been addressed and are closed? |  |  |
| **77.** | Have the Software Safety personnel confirmed that the project has identified all the safety-related requirements, approved changes to be implemented, and defects to be resolved for each delivery? |  |  |
| **78.** | Have the Software Safety personnel confirmed that the project has met all software safety-related requirements identified for the delivery? |  |  |
| **79.** | Have all approved safety-related changes been implemented and successfully tested? |  |  |
| **80.** | Have the Software Safety personnel confirmed that all the correct safety-related products are being delivered? |  |  |
|  | **Operational Readiness** |  |  |
| **81.** | Have the Software Safety personnel witnessed any pre-operations testing? |  |  |
| **82.** | Have the Software Safety personnel confirmed that the proper certification requirements are in place and accomplished prior to the actual operational use of the software? |  |  |
| **83.** | Have the Software Safety personnel attended the Operational Readiness Review? |  |  |
|  | **Operations / Maintenance** |  |  |
| **84.** | Has Software Safety confirmed the operating manual/procedures include a list of potential safety issues and work-around’s for those anomalies? |  |  |
| **85.** | Has Software Safety confirmed that changes and reconfigurations of the software, during operational use and maintenance of the software, are analyzed for their impacts on system safety??? |  |  |
| **86.** | Does Software Safety monitor the handling of operational inputs, such as command data, and data loads to validate the accuracy of the data before uploading? |  |  |
| **87.** | Does Software Safety analyze actual operational scenarios and activities to identify any new or previously unrecognized hazards and develop mitigations for them? |  |  |
| **88.** | Do the Software Safety personnel document newly discovered or previously unrecognized hazards and their mitigations and verifications in a Hazard Report? |  |  |
| **89.** | Do the Software Safety personnel submit problem reports to the maintenance team when errors or operational issues during operations are discovered, and work to develop safe workarounds for the problems until fixes can be included in a maintenance release? |  |  |
| **90.** | Do the Software Safety personnel confirm regression testing of work-around fixes or maintenance releases include retesting of all related safety-critical software code components? |  |  |

Date(s) of Audit: \_\_\_\_\_\_\_\_\_\_\_\_\_\_               Project: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Auditor(s): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_         Document Examined: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_                                               \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**COMMENTS PAGE \_\_\_\_  of  \_\_\_\_**

|  |  |
| --- | --- |
| **#** | **Comments from Audit.** |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

See also Topic [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis)

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 4.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 4.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) |

## 4.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety)      * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

## 4.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
