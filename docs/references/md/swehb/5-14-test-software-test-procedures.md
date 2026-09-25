# 5.14 - Test - Software Test Procedures

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695675. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures

5.14 - Test - Software Test Procedures

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695675)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695675&showCommentArea=true&showComments=true#addcomment)

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

Minimum recommended content for the Software Test Procedures Plan.  The Test Procedure Document contains all the detailed information needed to run the test cases identified for the level of testing:

1. 1. Detailed description of the planned test environment including:
      1. Identification of hardware,
      2. flight components used for test,
      3. software needed to run test (operating system, simulators used, hardware test beds, etc.)
   2. Planned test schedule
   3. Detailed description of each test case defined for the level of testing being performed, It should include for each test:
      1. Test identifier
      2. Test grouping (required verification, hazard control verification, etc.)
      3. Purpose of the test (proof requirement is satisfied, software works properly at boundary limits, handles fault, etc.)
      4. Identification of software version(s) being tested
      5. Description of any prerequisite condition(s)
      6. Description of steps performed to execute the test including test setup/test preparation steps
      7. Input and output parameters/files
      8. Expected results, including assumptions and constraints, criteria for evaluating results
      9. Pass/Fail Criteria for the test
      10. Any other information needed to rerun test
   4. Recommended: Traceability Matrix, listing set of test cases for level of testing traced to requirement satisfied or aspect of software verified (for example: identification of erroneous inputs)

# 2. Rationale

When testing software, it is important to capture the setup, steps, data, test cases, etc., used to verify requirements, functionality, safety, and other aspects of the software.  Test procedures capture that information and more for purposes including but not limited to:

* Verification of defined software functionality.
* Verification that all requirements were tested.
* Verification of test procedure validity, applicability, adequacy, completeness, and accuracy before use.
* Stakeholder understanding and agreement of test methods.
* Repeatability of tests and use of tests in regression testing.

# 3. Guidance

The Software Test Procedures describe the test preparations, test configuration, test cases, and test methods to be used to perform qualification testing of a computer software configuration item (CSCI) or a software system or subsystem. The test procedures also describe the expected test results and include bidirectional traceability to the requirements or a reference to the document containing that trace. See also [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing), Topic [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels), [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews),

## 3.1 Related Documents

The following documents are useful when developing test procedures:

* Software Requirements Specification ( [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification))
* Software Data Dictionary ([5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary))
* Software Design Description ( [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description))
* Interface Design Description ([5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description))
* SW Change Requests\_Problem Reports ( [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report))
* Software Architecture ([SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture)).

## 3.2 Writing Test Procedures

When writing test procedures, remember to:

* Include non-functional requirements, including safety, security, performance, etc.
* Ensure all requirements are covered by the full set of test procedures.
* Maintain the bidirectional test-to-requirements trace when modifying test procedures.
* Include test preparations for both software and hardware:

* Noting in the test procedure any dependencies in the order the test procedures must be run.
* Noting or setting the state of the system to that required to run the test procedure.
* Noting or setting the status of data values required to run the test procedure.

* Include tests to:
  + Confirm the software does what it is supposed to do.
  + Confirm the software does not do what it should not do.
  + Confirm the software behaves in an expected manner under adverse or off-nominal conditions.
  + Confirm the software can handle faults and failures through mitigation or return to a known safe condition.
  + Cover the range of allowable inputs, boundary conditions, false or invalid inputs, load tests, stress tests, interrupt execution and processing, etc.
* Include performance testing.

When writing test procedures, be sure to use these helpful processes and practices:

* Include very clear, understandable, detailed, step-by-step explanations of how to run each test case.
* Use templates and examples from your NASA Center, company, or the NASA Process Asset Library (PAL).
* Include references to any test scripts or other automated procedures, as appropriate.
* Include references to any documents describing the test configuration, if configuration is not captured in the test procedure.
* Include place to document expected results, not just actual results.
* Include a signature block at appropriate points in the procedure so that Software Assurance can sign off on a formal test when it is completed.
* Include provisions to add redlines to the test procedures when they are executed so that configuration management steps are not required to make a minor change to a procedure. The redlines become the official record and can be initialed by Software Assurance to show their concurrence on the changes.

## 3.3 Reusing Test Procedures

If reusing test procedures, be sure to:

* Check that those procedures adhere to the content and helpful practice guidance above.
* Revise those test procedures to align with testing planned for the current project.

See also [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures)

## 3.4 Pitfalls and Issues

Here are some pitfalls and issues when writing test procedures:

* Do not guess at how the software works. If the requirements are not clear enough to write the test procedures, ask questions of the appropriate project team members.
* Do not assume the tester understands the intricacies of the software design. The test procedures must be easy to follow.

## 3.5 Best Practices

Some other best practices to consider:

* Identify in each test procedure all requirements being verified by that test procedure.
* Establish bidirectional trace early, and maintain it throughout the test life cycle.
* Sequentially number the steps in the test procedure.
* Tailor the level of detail in each procedure step to allow:

* + Clear specification of expected results.
  + Meaningful comparison of expected results to actual results.

* Include cleanup steps to leave the system in a known state at the end of the test procedure.
* Use multiple test cases for each requirement, basing the number of test cases on the criticality of the requirement.
* Design test cases to address several related requirements. [140](#_tabs-<p></p>)
* Arrange test cases in the order that minimizes the effort required for test setup and that keeps related functions together. [140](#_tabs-<p></p>)
* Include a setup procedure or test case to place (or restore) the system in a known state, and call that test case repeatedly rather than repeating those setup steps in each test procedure.
* Peer review test procedures checking for, at a minimum:

* Completeness of test procedure content.
* Understandable and clear steps.
* Requirements coverage.
* Test procedure validity, applicability, completeness, adequacy, and accuracy.

[PAT-019 - Test Procedure Checklist](/spaces/SITE/pages/114328380/PAT-019+-+Test+Procedure+Checklist) is available to use when performing a Test Procedure analysis. 

## 3.6 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

Test procedures are needed regardless of project size. However, in situations involving small projects, the following relaxations in rigor (but still in compliance with the recommended content) may be appropriate:

* Combine the Test Plan and test procedures into one document.

+ The Test Plan is developed before the test procedures, but each test procedure could be added later to the Test Plan as a chapter or appendix.

* Use redlines during review and approval process versus update in configuration management to save time.
* If using a model-based development system, use the model to generate test cases automatically when possible and appropriate to do so.

+ Model-generated test cases typically follow a standard approach (range of allowable inputs, boundary conditions, false or invalid inputs, stress tests, etc.).

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-074)

  ["David Bowman's Information Management Checklist, Software Testing Procedures" (2009).](http://www.information-management-architect.com/software-testing-procedures.html "Click to open in new window")

  At www.information-management-architect.com. Retrieved May 17, 2011, from http://www.information-management-architect.com/software-testing-procedures.html.
* (SWEREF-110)

  ["Test Plan Template (IEEE 829-1998 Format)", Version 7.0, Software Quality Engineering, 2001.](http://www.ecs.csun.edu/~rlingard/comp480/TestPlanTemplate.pdf "Click to open in new window")
* (SWEREF-140)

  [Sample Software Testing Standards and Procedures,](http://it.toolbox.com/blogs/enterprise-solutions/sample-software-testing-standards-and-procedures-12772 "Click to open in new window")

  Borysowich, Craig, 2006. Observations from a Tech Architect: Enterprise Implementation Issus & Solutions,
* (SWEREF-215)

  [IEEE Standard for Software and System Test Documentation,](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4578271 "Click to open in new window")

  IEEE Computer Society, IEEE Std 829-2008, 2008.  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing)   * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [PAT-019 - Test Procedure Checklist](/spaces/SITE/pages/114328380/PAT-019+-+Test+Procedure+Checklist) |

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
| * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

* **Probable Scenario for Mars Polar Lander Mission Loss (1998)** **(Importance of including known hardware characteristics). Lesson Number 0938[529](#_tabs-<p></p>):**  "1. Project test policy and procedures should specify actions to be taken when a failure occurs during test. When tests are aborted, or known to have had flawed procedures, they must be rerun after the test deficiencies are corrected. When test article hardware or software is changed, the test should be rerun unless there is a clear rationale for omitting the rerun. 2. All known hardware operational characteristics, including transients and spurious signals, must be reflected in the software requirements documents and verified by test."

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
