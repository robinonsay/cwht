# 8.57 - Testing Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695752. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis

8.57 - Testing Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695752)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695752&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Test Plan Analysis](#tabs-2)
* [3. Test Procedures Analysis](#tabs-3)
* [4. Test Results Analysis](#tabs-4)
* [5. Safety Analysis During Test](#tabs-5)
* [6. Test Support Software](#tabs-6)
* [7. Test Analysis Report](#tabs-7)
* [8. Resources](#tabs-8)

Return to [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products)

# 1. Introduction

A test plan is a detailed document which describes software testing areas and activities. It outlines the test scope, objectives, types of testing to be done, progression of testing, test schedule, pass/fail criteria, required resources (human resources, software, and hardware), test estimation and test deliverables. Detailed guidance for the contents of a test plan can be found in this Topic in Testing Analysis, tab 2 under [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan). Tab 3 in [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) provides some guidance on the development of test plans, and test procedures. Tab 2 of this topic  will discuss analysis that helps determine the quality and completeness of the test plan.

A test procedure is a formal detailed document describing each planned test case. It includes an identification number, requirement or function being tested, description of the test environment, input data, instructions for conducting the test, and the expected output with pass/fail criteria for each test. Detailed guidance for the contents of the test procedures can be found in this Topic in Testing Analysis, tab 3 under [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures). Tab 3 of this topic will discuss analysis that helps determine the completeness and quality of the test procedures.

The test report is a summary of the final results of testing and the final details of each test run. The recommended contents for the test report can be found in this Topic, in Testing Analysis, tab 7 under [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report). [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) Tab 3 discusses contents of the test report. Tab 4 of this topic will discuss analysis of the test report.

Tab 5 contains information on testing safety-critical software and discusses additional testing methodologies that can be used for safety-critical software.

Tab 6 provides information on software that is developed to support testing.

Tab 7 provides more information on testing methodologies

Tab 8 lists available resources

See also [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation),

## 1.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 2. Test Plan Analysis

Testing is an important part of ensuring that the software will be a safe, reliable system. Planning for testing usually consists of a test plan, and test procedures. The test plan sets up the general overview of the whole testing program, including the types of testing that will be done, the test environment and conditions, ordering of the types of tests, the planned tests, grouping of the test cases, test coverage, recording and analysis of information, roles and responsibilities, traceability information and planned schedules. The general contents for a test plan document are found in Topic 7.18 at [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan).

Software Assurance and Software Safety personnel will be performing analysis on the test plan to ensure that the planned test program is adequate for the level of confidence needed in the software. All software test plans should be reviewed/analyzed  to ensure the **test plans contain the basic information listed in the test plan contents** in Topic 7.18. This can be done with a checklist verifying each of the items has been considered and is included.  A more thorough examination of the test plan can be done  with a peer review or inspection and this is recommended for all safety-critical software systems. There are more analysis methods and additional guidance for test plans that include safety-critical software listed in the Safety Specific Test Analysis section of this topic.

Analysis done on all **test plans should consider the following**:

* Have all the right levels of testing needed been considered? (Unit testing, integration testing, system testing, end-to-end testing, acceptance testing, regression testing) Each of the levels of testing should be designed to focus on the types of tests where that level is best suited to find errors. For example, unit testing is more likely to find errors in logic, errors in coding, or requirements implementation errors. Integration testing generally consists of testing modules of two or more units that provide more higher-level functionality and provide a portion of the higher-level system. The functionality of these modules can be tested. The Integration testing should also exercise the connections between safety- critical units and non-critical units or systems. System testing includes testing of the nominal functions of the system, as well as non-nominal situations like boundary conditions and includes tests for timing, through-put, sizing analysis.
* Have all the different types of testing been considered? Which types of tests should be in the different levels of testing? Example types are: White-Box Testing, Black-Box Testing, Stress Testing, Tests for timing, sizing and throughput, Endurance Testing, User Interface Testing, Fault Insertion Testing (See Safety-Critical Techniques), Failure Modes and Effects Testing (See Safety-Critical Techniques), Testing for Boundary Conditions, and Testing of operational scenarios.
* Are there tests selected for Regression testing? Regression tests are tests that should be rerun after changes have been made in a module or system to show that the previous functionality still works as planned. As the system matures, there should be a selected set of tests to verify all the basic functionality of the system, not just the functionality of the area where the change was made. For safety-critical software, any regression tests in safety-critical areas should be rerun, not just those in the area of the change.
* Has code coverage been considered so the coverage is adequate for the software being tested? Generally, code coverage is defined as exercising every state and path of the code. Achieving the 100% number can be very difficult in large, complex systems, so some analysis is needed to determine the best set of tests versus time to execute them in order to achieve the best coverage. Minimally, each statement should be executed once, and all paths and branches through the software should be executed. If the software is safety-critical, see the safety analysis section for more details. Some other types of computing code coverage include: Statement coverage, Decision coverage, Condition coverage, Multi-Condition Coverage, Path Coverage, Function Coverage,  Call Coverage, Loop Coverage, Race Coverage, Relational Operator Coverage, Integration coverage versus individual code coverage (i.e., through a module/class)  and [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) (See Topic 7.21 for details on this method). Many tools are available to help determine code coverage.
* Have COTS, MOTS, Open Source and reused code been considered when defining tests? These classes of software need to be tested thoroughly even if they have been used previously in similar systems. The first step is to determine what testing has already been done by the vendor/development group. If it is not possible to obtain the previous test analysis and records, and the source code is available, tests for this software should be developed following the same level of testing applied to the rest of the system. If the source code is not available, black box testing needs to be used and the test plan should include tests to exercise all functions required by the COTS, MOTS, Open Source, reused code in both nominal or off-nominal scenarios. For additional considerations and analysis for safety-critical or safety related testing of COTS, MOTS, Open Source, reused code, **see the tab on Safety Specific Test Analysis.** See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

* Has auto-generated code been considered in both high level and lower level testing when defining tests? Auto-generated code needs to be tested in the traditional functional types of test but think about whether the results are actually what you need, rather than what it expected. The code execution needs to produce the correct behavior without other unexpected side effects. Sometimes peer reviews of the actual code can help find errors that are not easily found in testing. See also Topic [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code).
* Have some of the basic principles (see below) been followed for the test planning?
  + Are all tests traceable to the requirements and are all requirements tested?
  + Tests should be complete before testing starts, although testing may lead to more tests being defined. More information on other types of testing is covered in Tab 5. Safety Specific Analysis During Test. Test planning generally can start when the requirements are complete.
  + Apply the 80/20 rule when developing tests, if a limited number of tests are being developed (otherwise thorough testing should be done). The rule says 80% of the errors can often be traced back to 20% of the components. Try to determine which components are the ones mostly likely to contain errors (more complex, high risk, too many interfaces, timing constraints, etc.) and focus more testing efforts in those areas.
  + Begin testing on the small (unit) level and gradually increase the size of the modules, components being tested. It is much easier to isolate errors in smaller systems than it is to wait until the entire system has been integrated.
  + In large complex systems, it is usually not possible to test everything (this is an example of when to apply the 80/20 rule), so plan the code coverage carefully. Using a good code coverage plan, it is possible to test all parts of the system.
  + Plan for testing to be done by an independent party. Developers of the code who do testing have more trouble identifying their errors, this is often due to the developers being too “close” to the code.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 3. Test Procedures Analysis

## 3.1 Ensure NASA-STD-8739.8[278](#_tabs-<p>8</p>) Requirements are met:

* **Analyze the test procedures for coverage of the requirements** – Use the trace matrix tracing each requirement to a test procedure. Each requirement should have at least one test case and will likely have multiple test cases depending on the different conditions that can apply in the requirement. Include test cases for boundary cases and different operational scenarios. For safety-critical software, MC/DC testing should be used to ensure every path through the software has been tested at least once. Test coverage tools are available to help determine code coverage.
* Analyze test procedures **for defined acceptance or pass/fail criteria** for each test case.
* Analyze test procedures to ensure tests include **boundary conditions and different operational (use case) scenarios, including both operational scenarios and off-nominal scenarios.** See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

* Analyze test procedures to ensure all **software requirements that trace to a hazardous event, cause, or mitigation technique are included in the test cases.**
* Analyze test procedures to ensure that any **newly identified contributions to hazards, events, or conditions during testing are included in test cases.**
* Analyze test procedures to determine if inverse test is simpler and still proves concept. (Proving the negative.)

See also [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software), 

## 3.2 Other Areas for Consideration:

* Analyze the test cases for functions provided by **COTS, MOTS, GOTS, OSS and auto-generated code** to ensure they are being tested to the same level as the developed software. For more information on testing these types of software, see the **tab on Safety Specific Test Analysis.**See also Topic [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code).
* Analyze the test cases to ensure that that the test cases include testing the **validation of any inputs** to the software.
* Analyze the test cases to determine whether all the **interfaces** have been tested.
* Check that the test procedures Include some **long duration tests** in the test set, if applicable
* Analyze the test cases for safety-critical software to ensure that all safety features have been tested, including all error handling, controls, mitigations, inhibits, and fault tolerance capabilities.
* Analyze the test cases to ensure the software can return to a safe known state if faults or failures occur.
* Analyze that testing of **interrupt behaviors** has been included in the test procedures
* Analyze test procedures to insure that:
  + Each test case in the test procedure has an identifier
  + Relevant requirements being tested are indicated for each test case
  + All inputs for tests are specified, including appropriate units
  + Expected results are specified, including appropriate units, and detailed instructions for evaluating the results of executing the test cases
  + Operational environment is specified, including any software generated for testing purposes
  + Step by step instructions for executing the test, including safety verification steps, are specified
  + Each test includes an area for signatures, indicating the successful completion of the test
  + Detailed results of executing the test cases should be recorded and any non-conformances recorded in the project defect-tracking system
* Analyze that the test procedures include testing to ensure that no safety inhibits or controls have been compromised by other testing
* Analyze the requirements to be tested in each component and determine whether the **tests defined adequately verify the requirement**
* Analyze the tests for safety-critical software to ensure that “Test for Failure” tests have been included. See **Testing for Failure in Tab 5** of this topic. More information on other types of testing is covered in Tab 5. Safety Specific Analysis During Test.

[PAT-019 - Test Procedure Checklist](/spaces/SITE/pages/114328380/PAT-019+-+Test+Procedure+Checklist) is available to use when performing this analysis.

## 3.3 Test Witnessing

* Ensure that all test cases are run as specified, results are recorded and test results meet pass criteria before test is considered complete. See Topic [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing)

## 3.4 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 4. Test Results Analysis

The test report is the document where the results of the testing is captured. It should contain information on each test case, indicating exactly how the test was run and documenting the detailed results. The documentation included should be complete enough to ensure that the test could be repeated, if needed, at a later date. Analysis of the test reports will include comparing the detailed recorded results against the expected results in the test procedures and noting any deviations. Any deviations, discrepancies in expected results or unexpected behavior during the test execution should be documented in the project defect-tracking system. All recorded discrepancies should be tracked to closure, either by correcting the problem or dispositioning it in some previously agreed-upon manner (such as use a work-around, pass the defect on for later maintenance, or document that the system does not have the capability in question).

Any changes made to the system to correct problems must be approved by the project configuration control board and the project documentation (including any applicable hazard reports) must be updated to reflect the changes.

Software assurance personnel should be able to verify that all tests were completed as planned and that all safety-critical interfaces were adequately tested. Test reports can be analyzed for requirements and path coverage. The analysis of the test results should provide the information to determine whether the system meets the criteria for “passing” the testing. If it does not meet the “passing” criteria, make a listing  of any activities that are needed to bring the system up to the “passing” level and report this to the project management.  Software assurance should be able to make an overall assessment of the quality of the system using the results documented in the test reports and any remaining problem reports.

See also [PAT-027 - Test Review Checklist For Review Teams](/spaces/SITE/pages/118161596/PAT-027+-+Test+Review+Checklist+For+Review+Teams)

## 4.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 5. Safety Specific Analysis During Test

Testing is an important part of ensuring that the software will be a safe, reliable system. In order to establish a good testing program for safety-critical software, it is first necessary to establish a good general test program and then pay particular attention to the safety-specific aspects of the test program. This section focuses on some of the areas that need additional attention and some of the techniques that are particularly helpful with safety-critical software.

The first step in analyzing the test plans for safety-critical software is use the guidance in the section of this topic, titled Test Plan Analysis. Start by assuring the contents of the test plan is complete and has considered the testing of safety-related features. The basic contents of a safety-critical test plan should follow the contents listed in Topic 7.18 under STP – Software Test Plan, but more consideration will be given to verification of any of the hazard controls, mitigations, and safety features. The other considerations listed should also be reviewed with a particular emphasis on safety impacts. Some of the areas needing special attention or additional methods/techniques are listed below.

See also [SWE-066 - Perform Testing](/spaces/7150/pages/16450267/SWE-066+-+Perform+Testing),

## 5.1 Unit Testing of Safety-Critical Units:

Unit testing is particularly important in safety-critical systems because there are often aspects of the safety-critical code that cannot be accessed once the units are more integrated. Thus, unit testing may be the only time these components can be tested thoroughly. Safety-related unit tests should be formally documented and reviewed by software assurance and safety. The tests on safety-critical units should be witnessed and formal results recorded and reviewed by both assurance and safety personnel. One of the most typical software coding errors is the use of uninitialized variables and these errors are often not found in unit testing unless tests are specifically designed to check for this problem. As the system is built up and integrated, safety features should be tested as early as possible, making it easier to isolate and fix any problems found.

## 5.2 COTS, Open Source, reused software

**COTS, Open Source, reused software** used in safety-critical systems: Often much of the information needed for thorough safety testing (source code, design information, operational constraints like boundary conditions, etc.) is not available with COTS software which forces the COTS testing to generally be black box testing. Black box testing typically has a specific set of inputs and expects a specific set of outputs, without knowing what is happening inside the COTS software. Below are some items to keep in mind when testing safety-critical systems:

* Determine whether the COTS/reused software has any inherent hazards, is part of any safety-critical function or can contribute to any hazards when integrated into the system
* Identify the project requirements that are satisfied by the COTS/reused software. Determine what the capabilities and limitations of the COTS, reused software, are with respect to the project’s
* Ensure that the test procedures include tests to test the safety-critical features of the COTS/reused software ***independent*** of the project’s
* In addition, ensure that the test procedures include tests to test the safety-critical features of the COTS/reused software **with** the project’s
* If the COTS/reused contains any dormant/dead code, consider any potential way that code might be activated (executed). Possibilities might include command invocation, function calls to specific routines, or calls from required functions based on the software state or parameters passed. If the source code is available, look for any undefined ways of entering the dormant/dead code. Static code analyzers can be used to identify unused code.
* Consider the amount of resources (memory space, disk/storage space) that might be used by any dormant/dead code. Is this extra resource usage likely to stress the system limits of resource usage?

* As much as possible, consider the interactions of the COTS/reused software with the safety-critical code. Look for ways that this software can influence the safety-critical code. Some possibilities to look for in integration testing:
  + Overwriting a memory location that stores a safety-critical variable
  + Instances where the OTS or reused code might use all the memory or other resources so a safety-critical function doesn’t have the necessary resources to execute
  + Overwhelming the message queue so critical message can’t get through in a timely manner
* As the test procedures are developed, and different scenarios are considered, it may be necessary to update the previous Hazard Analyses to include new information and tests following the in-depth looks at the COTS/reused code.

See also Topic [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations), [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software)

**Other types of testing that should be considered or augmented for the test plans for safety-critical software:**

## 5.3 Regression Testing:

When reviewing the test plan, verify that regression testing is planned after any change,  includes any safety-related functions of the system, any special safety tests, and will be witnessed.

## 5.4 Testing For Failure

Testing for failure is the concept of performing tests for situations that should not happen under normal operations. This includes testing for bad inputs, operating system failures, improper operator actions and any other possible off nominal condition.   
The first thing to understand about Testing For Failure is that it should be part of the initial requirements and should be part of all testing regiments. Every module, function or action needs to be tested for both success and failure. The requirements should also define how the software is to react to the given failures.   
*Things to consider:*  
Having a requirement that the hardware must handle an error is not the same as testing for the error. When you test for an error, the purpose is to define how the software reacts to the error. Testing for error handling of that error just shows that the handling worked. This means if you want to fully test a possible error you need to test:  
              *How the software reacts when no error occurs.  
              How the software reacts to the error with no error handling.  
              How the software reacts to the error with error handling.*

This allows the developer to ensure that the software reacts as expected to errors.  
***Example:***  
              A software initially reacts to a Memory failure by reporting a segmentation fault and then crashes. Error handling is written to handle that exception. Changes to the OS later alters the error to be a MAMORY\_ALLOCATION Exception. If the software is not tested for failure, then the developer will not be aware that the segmentation fault is no longer valid and a memory error would now cause the software to crash. By having a test specifically testing for the correct exception, then when running the tests on the new OS would immediately identify the issue and it could be corrected.

Additionally, Testing For Failure also involves testing for performance limitations, input limitations and general robustness of the code. A good set of failure tests will be able to provide data of what the overall limitations of the software is and how reliable it will be when put under stress.

## 5.5 Interrupt Test Analysis

Test plans for safety-critical software should include tests for interrupt handling. Consider tests for the following:

* Worst case interrupt sequences (e.g., Can interrupts impact timing for critical events?)
* Undefined responses to an interrupt
* Interrupts uninitialized to a return
* Significant chains of interrupts
* Buffering capacity of inhibited interrupts
* Priority processing of interrupts
* Can interrupt deadlocks occur?

## 5.6 Software Fault Injection

This is a process of injecting faults and then examining the results to see if the software is robust enough to handle it. (Did the software propagate the error? Was the end result undesirable? Could the system handle the fault gracefully?) This technique initially used code modifications to inject the fault but can also be used for interfaces and to test OTS software.

## 5.7 Failure Mode and Effects Testing:

For failure modes and effects testing, the test plan will consider all the failures identified and include tests intentionally  producing the identified possible failures. This will demonstrate whether the system is robust enough to handle the failures tested. If the tests results in unpredictable behavior or undesirable results, then some additional mitigations will be needed in the software.

## 5.8 Mutation Testing

Mutation Testing is just another form of Testing for Failure where the code in a unit or module is  modified to produce a particular result or behavior. It can also be used to output a result at a particular point in a program so the result can be checked for correctness.

## 5.9 Perturbation Testing:

In this form of testing, change or “perturbations” are made to the operational environment or the operating system to observe the software’s behavior. This can be used to produce security issues and observe the software’s behavior. It can also be used to force exceptions, or induce errors in communications between modules, or forcing interrupts to verify these can be handled by the system. This form of testing is very useful in integration testing where it is more difficult to test these types of conditions.

Another techniques that might be considered when developing a test plan is **Test-Driven Analysis.** This is really a development methodology concept focused on facilitating testing. It is more related to Development rather than testing specifically and needs to be incorporated into the entire process, not just focused on unit testing.

## 5.10 Test Driven Development

*Test-driven development (TDD) is a software development process relying on software requirements being converted to test cases before software is fully developed and tracking all software development by repeatedly testing the software against all test cases. This is as opposed to software being developed first and test cases created later.*

This concept helps to maintain adherence to the initial requirements as the test cases for those requirements are defined and written before the code itself is actually developed. This concept is dependent on ensuring tests cover all possibilities and puts more emphasis on testability of the code. This inherently drives development to be more modular, testable and readable.  
              **Example:**

              The requirement is:  The system shall perform addition using a combination  of data types (INT, FLOAT, DOUBLE) to an accuracy of at least 5 decimal points. The requirement would be similar to the following: (+-(INT, FLOAT, DOUBLE)) + (+-(INT, FLOAT, DOUBLE)). Meaning that to test all possible permutations would require positive and negative signs for three different types and both sides of the addition signs, so (2(3))(2(3)) or 36 tests to properly verify all possible combinations of inputs can be calculated to requirements. Therefore, tests are written for all 36 permutations and the code is written to satisfy these tests and not cause others to fail.  Once completed the code and new tests are checked in.  
              **Note:** testing (-INT)+(INT) is not the same as testing (INT)+(-INT). While mathematically this is the same equation, in code it is using two different calls that could potentially have different results.

When developing the module, the developer writes the code to make all the tests pass one at a time. This ensures all requirements are met and that all tests continue to pass as each subsequent one is completed. This also helps to ensure that future development does not break requirements since you have tests in place that ensure they continue to be met.

Also, since each test verifies a requirement, and each requirement is attached to a test, it’s much easier to document, verify and maintain the code.

## 5.11 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 6. Test Support Software

Throughout the many levels of testing, there are many commercial tools that can assist with testing certain aspects of the system, such as performance, or checking the values of a parameters in mid-execution. In addition to these commercial tools, it is still often necessary to develop custom software or pieces of software to provide inputs or drive expected conditions that are needed to test portions of the code. Some examples are tools that may be developed specifically for the benefit of testing portions of a system or particular capabilities of the system. For example, a code portion may be written to provide input values for  testing an input validation portion of the software.

Some types of supporting test software are listed below:

* Test Drivers – These are special purpose program interfaces written by the developers to test internal software by providing specific sets of inputs to force designated actions.
* Test Data Drivers – These are special purpose tools that can emulate streaming data such as vehicle tracking data and telemetry. These special tools provide data in the same format as the actual data.
* Test Data Simulators – These are special purpose tools that can generate realistic data such as telemetry data and tracking data that match operational conditions on a spacecraft.
* Debuggers – Debuggers are developer tools that assist in viewing program internal actions, stored values, steps executed, etc. Debuggers may be available in some of the commercial tools, allowing programs to display specific values at different points in the program or recording the steps executed for later inspection.
* Checkpoints – Checkpoints are normally data sets initialized to set a program to a predefined condition or force a condition to identify a problem. Checkpoints may be data sets input or output by the program under specific condition.
* Debug prints – These are print statements compiled into the program to provide outputs at needed times or from needed locations.
* Database Browser – These tools permit direct viewing and editing of parameters in a database.
* Developer Displays – These displays mimic the actions available to a user for special interactive testing.

These support tools are often used in conjunction with each other to verify requirements, code, and program capabilities. Even the simplest of these tools will need to be checked for correctness, kept under configuration control, updated when requirements change and listed in the appropriate test documentation (test procedures, test report).  Any required system configuration or required data sets should also be documented in the appropriate test documentation (test procedures, test report).

Many other types of support tools may be necessary to help determine whether a system meets its requirements. In complex cases, it is not sufficient to just compare the results with a simple set of numbers. Other tools may be necessary to generate the types of results needed for comparison to determine whether the results are correct. For example, if a software tool designed to generate a flight envelope by executing numerous simulations, each dispersed randomly, it might be evaluated through the use of numerous methods including, but not limited to:

1. Statistical sampling and comparisons to verify that the data is randomized using the required distribution
2. Graphical comparisons of simulation results to flight data as well as the flight rules to ensure that the simulations are being executed correctly
3. Comparisons to bench programs where the differences between the tools are known and accounted for in the results
4. Hand calculation of the initial dispersions to compare the results with those dispersions generated by the tool
5. Sampling of data at key points in the simulation for comparison with bench programs, flight rules, and the specific requirements of the tool

Some of the tools mentioned in this section would be stand-alone, separate programs, while others would result in direct changes or additions to the code portion or program being tested. In cases where the code being tested was modified for testing, the test code portions should be removed before the final delivery. It is recommended that regression tests be run following this removal to ensure that the code removal did not cause other problems in the deliverable code. Measuring or instrumenting the code can change the results of the code, (observer effect).

Stand-alone test support programs such as simulators should be tested separately and accredited prior to their use in testing.

## 6.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-8) in the Resources tab.

# 7. Testing Analysis Report

**Documenting and Reporting of Analysis Results for testing artifacts (Plans, Procedures, Test Results)**

When the test Plans, test procedures, or test reports are analyzed, a Software Testing Analysis work product is generated to document results capturing the findings and corrective actions that need to be addressed to improve the overall test artifact. It should include a detailed report of the test analysis results. Test artifacts results should also be reported in a high-level summary and conveyed as part of weekly or monthly SA Status Reports. The high-level summary should provide an overall evaluation of the analysis, any issues/concerns, and any associated risks. If a time-critical issue is uncovered, it should be reported to management immediately so that the affected organization may begin addressing it at once.

When a project has safety-critical software, analysis results should be shared with the Software Safety personnel. The results of analysis conducted by Software Assurance personnel and those done by Software Safety personnel may be combined into one analysis report, if desired.

## 7.1 High-Level Analysis Content for an SA Status Report

Any test analysis performed since the last SA Status Report or project management meeting should be reported to project management and the rest of the Software Assurance team. When a project has safety-critical software, any analysis done by Software Assurance should be shared with the Software Safety personnel.

When reporting the results of an analysis in a SA Status Report, the following defines the minimum recommended contents:

* Identification of what was analyzed: Mission/Project/Application
* Period/Timeframe/Phase analysis performed during
* Summary of analysis techniques used
* Overall assessment of test artifact or testing, based on analysis
* Major findings and associated risk
* Current status of findings: open/closed; projection for closure timeframe

## 7.2 Detailed Content for Analysis Product:

The detailed results of all software testing analysis activities are captured in the Software Test Analysis products along with the types of analysis techniques used to provide information on the robustness of the analysis done. The techniques/methods used provide information on those that produced the most useful results . This document is placed under configuration management and delivered to the project management team as the Software Assurance record for the activity. When a project has safety-critical software, this product should be shared with the Software Safety personnel.

When reporting the detailed results of the software testing analysis, the following defines the minimum recommended content:

* Identification of what was analyzed: Mission/Project/Application
* Person(s) or group/role performing the analysis
* Period/Timeframe/Phase analysis performed
* Documents used in analysis (e.g., versions of the system and software test artifact, interfaces document, Concept of Operations)
* A high-level scope and description of the techniques/methodologies used in the analysis
  + Use the list of possible analysis techniques/methodologies listed in Analysis Tabs  as a starting point.
  + For each technique/methodology on the list, state why/or why not it was used.
  + List any additional techniques/methodologies used that were not included in the Analysis Tabs list.
* Summary of results found using each technique/methodology
  + How many findings resulted from each technique/methodology?
  + Difficulty/Ease of technique/methodology used
  + The general assessment of the technique/methodology
  + High-Level Summary of the findings
* Results, major findings, and associated risk:
  + Overall assessment of the quality/completeness of the requirements, based on the analysis
  + Either list each result, finding, or corrective action or summarize them and list the links to the detailed findings.
  + Assessment of the overall risk involved with the findings.
* Documentation should include the types of findings:
* Minor findings
* Current status of findings: open/closed; projection for closure timeframe
  + Include counts for those discovered by SA and Software Safety
  + Include overall counts from the Project’s problem/issue tracking system.

# 8. Resources

## 8.1 References

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

## 8.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 8.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [5.23 - Testing Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641646/5.23+-+Testing+Analysis+Report+Minimum+Content) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) * [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [PAT-019 - Test Procedure Checklist](/spaces/SITE/pages/114328380/PAT-019+-+Test+Procedure+Checklist) * [PAT-026 - Test Review Checklist For Test Leads](/spaces/SITE/pages/117211498/PAT-026+-+Test+Review+Checklist+For+Test+Leads) * [PAT-027 - Test Review Checklist For Review Teams](/spaces/SITE/pages/118161596/PAT-027+-+Test+Review+Checklist+For+Review+Teams) |

## 8.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>8</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 8.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |
