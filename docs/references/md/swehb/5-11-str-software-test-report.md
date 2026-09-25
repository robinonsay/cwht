# 5.11 - STR - Software Test Report

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695672. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report

5.11 - STR - Software Test Report

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695672)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695672&showCommentArea=true&showComments=true#addcomment)

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

Minimum recommended content for the Software Test Report. 

a. Overview of the test results:

1. Testing Conclusions – Overall evaluation of the software as shown by the test results.
2. Remaining deficiencies, limitations, or constraints detected by testing (e.g., including description of the impact on software and system performance, the impact a correction would have on software and system design, and recommendations for correcting the deficiency, limitation, or constraint).
3. Impact of test environment.

b. Detailed test results:

1. Test Identifier – Project-unique identifier of a test and test procedure(s).
2. Summary of test results (e.g., including requirements verified).
3. Problems encountered (e.g., anomalies, defects).
4. Deviations from test cases/procedures.

c. Test log:

1. Date(s), time(s), and location(s) of tests performed.
2. Software version(s) tested – Identification of all software (e.g., CSCI) and version(s) being tested.
3. Test Configuration/Setup – Test environment, hardware, and software configurations used for each test. Include data storage location for the test data.
4. Test Personnel and Activities – Date and time of each test-related activity, the identity of the individual(s) who performed the activity, and the identities of witnesses, as applicable.

d. Rationale for decisions.

# 2. Rationale

When testing software, it is important to capture the outcome of tests used to verify requirements, functionality, safety, and other aspects of the software. It is also important to capture any decisions based on the outcome of those tests. Test reports capture that information and more for purposes including but not limited to:

* Documenting what was done and how the results match or differ from the expected results.
* Identification and isolation of the source of any error found in the software.
* Verification that testing was completed as planned.
* Verification that safety-critical elements were properly tested.
* Verification that all identified hazards have been eliminated or controlled to an acceptable level of risk.
* Reporting safety-critical findings that should be used to update hazard reports.
* Generating data for evaluating the quality of tested products and the effectiveness of testing processes.

# 3. Guidance

As noted above, software test reports document an assessment of the software based on the test results, the detailed test results, a log of the testing activities, and the rationale for any decisions made during the testing process.

The software test reports may be tailored by software classification. Goddard Space Flight Center's (GSFC)'s 580-STD-077-01, Requirements for Minimum Contents of Software Documents, provides one suggestion for tailoring software test reports based on the required contents and the classification of the software being tested.

Test reports are to be written following each type of testing activity, such as a pass of unit or integration tests. Note that NASA-GB-8719.13, NASA Software Safety Guidebook [276](#_tabs-<p></p>), recommends formal unit test reports to be written for safety-critical unit tests, while other unit tests' reports may be as simple as notes in a log book. Also note, however, that project planning will include a determination of the degree of formality for the various types of testing, including unit and integration testing, and that formality needs to be documented in the project's software development plan ( [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)). See also Topic [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels)

## 3.1 Types of Reports

Depending on a project's defined procedures, test reports can be of multiple types:

| Preliminary Test Reports | Detailed Test Reports |
| --- | --- |
| Prepared at the end of each test session. | Prepared within a week of test execution. |
| Provide rapid assessment of how software is working. | Describe problems but do not identify their sources in the code. |
| Provide early indications of any major problems. | Prepared by test team by analyzing results obtained during test sessions, using hand calculations and detailed comparisons with expected results. |
| Prepared by test team on basis of a "quick-look" evaluation of the executions. |  |

See also [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing), [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior),

## 3.2 Additional Information In Reports

To identify and properly configuration manage the test environment used for testing, include the following information in the test report:

* Version numbers of all software elements used to support testing, such as simulators and monitoring tools.
* Inventory numbers and calibration dates for tools such as logic analyzers, oscilloscopes, multimeters.
* Version numbers for all FPGA (Field Programmable Gate Array) components present on the testbed.
* Serial numbers of the testbed elements.

Test reports are to provide evidence of the thoroughness of the testing, including:

* Differences in the test environment and the operational environment and any effects those differences had on the test results.
* Any test anomalies and the disposition of any related corrective actions or problem reports.
* Details of the test results (see requirement text), including test case identifications, test version, completion status, etc., along with the associated item tested as required by the project's software test plan.
* Location of original test results (output from tests, screen shots, error messages, etc., as captured during the actual testing activity).

Issues that may arise related to software test reports include:

* If acquired software does not include complete (meet the required content) test reports, it is prudent for the acquirer to conduct additional testing upon delivery of the software from the provider.
* Test reports may not be available for acquired off-the-shelf (OTS) products. [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) requires the project to ensure OTS is verified and validated to the same level of confidence as a developed software component. Lack of existing OTS test reports, does not relieve the project from subsequent tests and test reports to determine fitness for use.

See also [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results), Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews),

Useful processes or recommended practices for software test reports include:

* Review and signoff by Software Assurance and Software Safety for software safety verifications; may include NASA Independent Verification and Validation (IV&V) if those services are being used for the project.
* Maintenance under configuration management.
* If software is acquired, the provider needs to provide software test reports containing the required information.
* Use of templates or checklists to ensure accurate capture and recording of detailed information such as the test logs and deviations from planned test cases/test procedures.
* Use of tables to summarize test results, including requirements tested, pass/fail results, identification of tests performed, etc.
* Referencing of problem reports/change requests when documenting details of remaining deficiencies, limitations, constraints, etc., rather than duplication of the information contained in those reports/requests.

See also Topic [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing).

## 3.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

For projects with small budgets or small team size, the following approaches may be helpful in reducing the time and cost of preparing software test reports:

* Automate collection of detailed report data and/or test logs for the test report, particularly if the automated tools already exist at the Center.
* Use existing templates rather than create new ones.
* Use less formal reporting for unit tests, if Center procedures allow.
* Tailor the contents of the software test reports, where allowed and appropriate.
* Reference existing content rather than duplicate it in the test report.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-047)

  ["Recommended Approach to Software Development,"](http://everyspec.com/NASA/NASA-GSFC/GSFC-General/SEL-81-305_REV-3_2419/ "Click to open in new window")

  SEL-81-305, Revision 3, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1992.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| Unable to render {include} The included page could not be found. |

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

## 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
