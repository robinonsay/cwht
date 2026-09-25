# 8.13 - Test Witnessing

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695739. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing

8.13 - Test Witnessing

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695739)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695739&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Preparation for Test Witnessing](#tabs-1)
* [2. Activities during Test Execution](#tabs-2)
* [3. Activities Following Test Execution](#tabs-3)
* [4. Resources](#tabs-4)
* [5. Lessons Learned](#tabs-5)

# 1. Preparation For Test Witnessing

* Software Assurance personnel chosen to witness testing should be familiar with the following governing documents:
  + NASA-STD-8739.8 [278](#_tabs-<p>4</p>) requirements related to testing,
  + NPR-7150.2 [083](#_tabs-<p>4</p>) requirements related to testing, and
  + Any Center or project level standards or procedures relating to test witnessing and safety-critical software, if applicable.
* Test Witnesses should have the appropriate training for the facility.
* Software Assurance planning activities associated with test witnessing should be based on the software classification and software safety-criticality of the software under test. Software Assurance should witness all software tests for the safety-critical software components.
* Software Assurance personnel witnessing the test should be familiar with the following project-specific documents:
  + Project software requirements,
  + Software design,
  + Software bi-directional traceability,
  + Open software problem reports,
  + Software data loads required for the test,
  + Fidelity of the test environments,
  + Fidelity and maturity of any simulations,
  + Emulator or models used in the software testing,
  + Software configuration and software configuration management state for the software under test,
  + Test plans, procedures, test cases, acceptance criteria for each test set and expected results for each test.
* Software Assurance personnel should be familiar with the operational scenarios and have some knowledge of the project domain.
* Software Assurance personnel should develop a checklist of items to be checked before, during, and after the test(s). Be sure to provide a space to record any observations.
* Software Assurance should verify that all tests listed in the test plan trace back to one or more requirements and trace back to the hazard reports, as applicable.
* All requirements should trace to one or more tests; for safety-critical software, all software features in hazard reports (e.g., mitigations, controls, warnings, barriers and other safety designs, etc.) should trace to one or more tests.
* Check to determine if planned software tests provide good coverage of the requirements under test.
  + Verify that test set includes limit/range/boundary testing, operational scenario testing (day-in-the-life-of), off-nominal conditions, end-to-end tests, regression tests, stress testing, load and performance testing, as well as security testing and hazard report verifications (as applicable), etc.
  + Verify that any COTS, MOTS, GOTS, Open Source, reused code is being used within the operational assumptions for the code and is tested just as thoroughly as the developed code.
  + Testing of some functionality can only occur during the unit testing level. For these items, Software Assurance personnel should review the unit test and unit test results, especially for safety-critical capabilities/functions/requirements.

See also Topic [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan), [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels), [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis), [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing),

* If Software Assurance or the project has identified high risk, high complexity, and highly critical system components, confirm that the planned tests adequately cover those components.
* Software Assurance personnel should confirm that the project is ready to do the testing. See Test Readiness Review information in NASA-HDBK-2203, Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews). Perform a formal or informal Test Readiness Review before any formal testing. A few reminders:
  + Note the software version(s) to be tested.
  + Software, test scripts, input data files, etc. to be used in the test need to be under configuration management.
  + Test plans, procedures, and test cases need to be peer-reviewed and under configuration management.
  + The operational environment or high- fidelity test environment needs to be ready.
  + The defect tracking system needs to be in place.

## 1.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 2. Activities During and After Test Execution

## 2.1 During Test Execution

* Ensure that the correct version(s) of software is under test.
  + If not, record any differences. If the versions don’t match, terminate the test.
* Verify that the test environment is either the operational environment or a high-fidelity test environment (e.g., software simulator)
  + Record any differences in the test environment or test set-up, including scripts, data files, and configurations.
  + Capture any exceptions to test-as-you-fly/operate and the rationale for those exceptions (e.g., HW not available for testing). Test environment elements (simulators, emulators, etc.) could be areas where defects could go undetected.
* Verify that the inputs for the test are the ones listed in the test procedures.
  + Record any differences. Any changes made during the test must at least be red-lined and approved (signed off) by the appropriate authority, according to the procedures for conducting testing.
* Observe that the operator’s actions match those planned in the test procedures.
  + Note any differences; any deviations made during the test must at least be red-lined and approved (signed off) by the appropriate authority.
* When failures occur, record a full description of the anomalous behavior and the conditions under which it occurred, including the sequence of events, the environment characteristics (e.g., platform, O/S and version, activity type), when the failure occurred, and user actions that preceded the failure.
  + Assure that all unintended failures or anomalous behavior are recorded in the project defect tracking system, along with all the descriptive details. Assure that enough details are captured for a developer to identify the possible area of the code that caused the failure.
  + Capture a description of the consequence of the failure or anomalous behavior – Does it prevent the software from continuing to execute? Does the software go into a fault protection mode or a safe state? (If so, was this the fault protection mode or safe state specified in the requirements?) Does the software continue to execute, but produces incorrect results, or unpredictable behavior?
* Observe the operator’s interactions with the user interface (UI). Note: There are multiple ways to interface with software. The UI could be hardware (switches/buttons) or software (command line, graphical UI, or input script).
  + Is the user interface easy to understand?
  + Are the controls the operator needs to use clearly identified?
  + Is there a separation between primary operator control mechanisms (buttons, switches, items to choose, etc.), so there is little likelihood of the operator hitting the wrong choice by mistake?
  + For Commanding software, is it a two-step process to issue the command (arm & fire)? Is there a way to override/revise/review the command before execution?
  + Record any significant issues observed. (Anything that might need correction or adjustment, should be captured in the software defect tracking system.)
  + Do alerts for immediate operator action stand out, so the operator immediately sees them? (For example, the color changes, words flash, there’s a pop-up, etc.)
* If any changes occur during the test session, are additional regression tests needed? (If updates to the software or operational environment are made, the answer is “yes.”)
  + If the software is safety-critical, all regression tests should be rerun.
* Confirm the tester has recorded all of the test results accurately.
* Confirm the tester recorded any discrepancies observed during test execution in the project defect tracking system, including a full description (as above).

## 2.2 After Test Execution

Depending on the type of test results expected, the following may happen after test execution:

* Confirm test results match the expected test results in the test case? (This analysis may occur following the test)
* Software Assurance personnel sign-off on test plans, test procedures, test results, and reports.
* Software Assurance personnel witnessing the tests signs-off on the safety-critical tests run:
  + Sign-off for a “Pass” indicates that the test is successful according to the plan, and test results match the expected test results.
  + For a “Fail” on a test, Software Assurance should note any of the following that apply:
    - The test was unsuccessful according to plan
    - The tester recorded the software failures or defects
    - Test results did not agree with expected test results
    - Other-specify

## 2.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Activities Following Test Execution

* Confirm that the test team has analyzed the test results and confirmed that they meet the pass/fail criteria.
* Confirm that any defects or failures noted during the test execution are recorded in the project defect tracking system. Track the defects to closure.
  + If the decision is made to not to fix a defect, then Software Assurance should check to see if an Ops Note was written or added to a Knowledge Management system for operators to reference during real-time ops.
* Confirm that the test report is complete and includes test data, test results, and required approvals. The test report contains issues and discrepancies found during each test. See the NASA-HDBK-2203, Topic 7.18: Documentation Guidance for [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) content.
* Confirm that the appropriate metrics from the test have been recorded/updated. (Examples: # of tests run/passed, # of tests that need to be rerun, # of defects recorded/fixed, etc.)
* Track the defects to closure.
* Confirm any necessary documentation is updated. Example: An operator error during testing may indicate a change is needed in an operations manual.

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
| * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)        * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

## 4.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 4.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 5. Lessons Learned

### 5.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this topic.

### 5.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this topic.
