# 7.06 - Software Test Estimation and Testing Levels

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695626. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels

7.06 - Software Test Estimation and Testing Levels

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695626)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695626&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Considerations and Influencing Factors](#tabs-2)
* [3. Software Test Estimation Principles](#tabs-3)
* [4. Estimating Techniques](#tabs-4)
* [5. Levels of Testing](#tabs-5)
* [6. Resources](#tabs-6)
* [7. Lessons Learned](#tabs-7)

# 1. Purpose

Provide guiding principles and best practices pertaining to software test estimation and a description of the typical "levels" of testing performed for a software project.The content herein does not describe an all-inclusive solution for software test estimation but does contain valuable information that is useful to consider when planning software test activities. Estimation in general and specific software test estimation is one of the most difficult and critical activities in achieving project success.

## 1.1 Introduction

Software test estimation is the ability to accurately predict (through estimation techniques) the effort, time, and cost it will take to effectively test a defined software suite. It is important to combine good estimation techniques with an understanding of the factors that can influence effort, time, dependencies, and resources. Further information related to estimation can be found in [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation).

## 1.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 2. Considerations and Influencing Factors

There are many factors to consider in producing accurate software test estimates. The following guidelines are based on common experiences and industry best practices.

## 2.1 Schedule Margin Inputs

The good estimation includes adding some margin in the schedule – the class, size, and complexity of the project helps determine the appropriate reserve. The bigger and more complex the project, the more margin time needed.  Software schedule margins may be included in overall project development schedule margins; if so, margins are typically bigger in Phase A/B of the life cycle, and reduced when entering Phase C. It is vital that margins are realistic and based on defendable rationale. A realistic margin helps ensure maximum test coverage and takes into consideration the inevitable delays that occur. Although estimates are highly dependent on the software class, size and complexity, the following rules-of-thumb for the scheduled duration of the various parts of software development activity are profitably used when quantifying the margin:

* Integration and testing of flight software can be between 22 percent and 40 percent of the total schedule.
* Ground software integration and test (mostly new development) is about 25 percent of the schedule.
* Ground data software integration and test (with significant inheritance) is about 16 percent of the schedule.

See also [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage),

## 2.2 Availability of Resources for Estimated Period

A good estimate will include a fixed number of resources for each test cycle. If the number of resources declines, then the estimate can be re-visited and updated accordingly when assessing if the availability of testbeds and environments and simulators is adequate, account for the use (shared, in series, in parallel) of these resources by the development and test teams. Software test estimation should always consider events like long vacations planned by the team members to help ensure that the estimations are realistic.

## 2.3 Estimate Early and Update as Necessary

In the early planning stage, frequently re-visit the test estimations and make modifications as needed. Estimates are not usually extended once an agreement has been made unless there are major changes in requirements. Estimates will improve as more information becomes known about the requirements, design, code, environments, test levels, and use cases.

## 2.4 Remember Your Past Experiences

Past experiences play a significant role when preparing estimates. Utilizing documented lessons learned and pitfalls encountered in previous projects can help avoid some of these difficulties. In addition, analysis of past successes in delivering on-time products can provide direction for the things to consider repeating. Keep in mind that the overall growth in software complexity and size for flight systems are two factors to be taken into consideration in the estimation process. [170](#_tabs-<p>6</p>)

## 2.5 Consider the Scope of Project

Identify project software test goals and software product deliverables. Factors to be considered differ among projects, application domains, [348](#_tabs-<p>6</p>) etc.  For some projects, typically the test cycle includes test case development, execution, and regression testing. Other projects may include setting up one or more testbeds, test plan/procedure development, generating and analyzing test data, test scripts, etc. Estimations, therefore, are to be based on all of these factors. Project limitations such as cost, schedule, and technical characteristics are also to be considered.

## 2.6 Does your team have the appropriate skills and knowledge?

Knowing your team's strengths and weaknesses can help you estimate testing tasks more accurately. Consider the fact that all team members may not yield the same productivity level and may not possess the skills to perform tasks independently. Some people can execute tasks faster, some are more accurate, and some are both fast and accurate. While this is not a major factor, it can impact product deliverables. Proper skills, experience, and attitudes in the project team, especially in the managers and key players are discriminating factors. Remember, the time to complete a project is not proportional to the number of people working on the project.

## 2.7 Reuse of Test Assets

Depending on the software test goals, another consideration is the reuse of test assets such as test plans, procedures, cases, environments, tools, scripts, testbeds, etc. In the case of previously tested software that is in the maintenance phase with only minimal software enhancements, test procedures may only require a small amount of effort to update. For a new project, review the local requirements, related to testing, that are flowed down from NPR 7150.2, NASA Software Engineering Requirements, for the class of software being tested to determine the usability of any existing assets.

## 2.8 Process Maturity

Process maturity plays a significant role in accurately estimating software test activities. For example, Class A/B and/or safety-critical projects are required to have a more rigorous process than a Class D non-safety-critical project (in accordance with NPR 7150.2). The basis of the estimate is more credible in an organization when test methods and activities are infused into the project vs. being tacked on at the end. Clearly defined interfaces and expectations between the test team and the rest of the organization make it easier to predict (estimate) the task. A managed configuration and change management process for test work products saves time and effort at the end of the product life cycle. Timely and reliable bug fixes, realistic test schedules, the timely arrival of high-quality test deliverables, and proper execution of early test phases (unit and integration) all provide a basis for software test estimates.

## 2.9 Lines of Code and Complexity

A major consideration in developing good software test estimates is an understanding of the number of lines of code, complexity, classification, safety-criticality, programming language, and code structure of the software under test. Object-oriented languages and component-based indices tend to increase complexity making test estimates challenging. The complexity includes the number of requirements needing verification through testing, how well the architecture and the design can be assessed by testing, the number of use cases or operational scenarios to be evaluated, and the extent of off-nominal testing.

## 2.10 Test Environment

Another factor in preparing effective estimations is the identification of an adequate, dedicated, and secure test environment and a separate, adequate development debugging environment. Competent, responsive test environment support also plays a part in the accuracy of test estimates.

## 2.11 Automated Testing

A key indicator in software test estimation is automated testing. Automation helps with recurring test activities, such as regression testing.  There is a tradeoff to use or not to use automation during testing. It is very time-consuming to build automated test suites, but if the project desires a high rate of repeatability, test automation can be useful. Projects should stay away from using automation when it does not support testing goals. Automation estimates should be based on quantifiable repeatability and reusability factors. Automation may not realize benefits for a one-time effort.

## 2.12 Consider the Test-Fix Cycle

The test-fix cycle is one of the most common pitfalls in software test estimation. Software size/complexity, number of stakeholders, distributed nature of the test activities, availability of resources, configuration management maturity, and knowledge/skill of team members all play a role in estimating the test-fix cycle. The test cycle depends on the stability of the build. If the build is not stable, more time is needed to test-fix, therefore, extending the test cycle.

## 2.13 Test Reporting

Test reporting is a major activity not usually accounted for in the test estimate. Reporting needs are based on process maturity and methodologies and require management involvement to identify reporting needs and evolve estimations.

## 2.14 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 3. Software Test Estimation Principles

In this section, a few "rules of the road" for software test estimation are discussed.  Software test engineers and managers often struggle with how to estimate the software testing effort. Estimation is performed on a project-by-project basis, however, software development has so many universal characteristics that general guidelines can be recognized and considered in establishing test estimates for a wide variety of projects.

## 3.1 Estimate early and update as needed.

As with any estimation task, it is important to establish and re-establish estimates based on changes in project requirements, objectives, and/or resources. It is also important to capture the basis of the estimate and record assumptions and rationale for changes in estimates as the project progresses. An accurate accounting of estimates and the data surrounding those estimates are valuable assets for predicting future estimation tasks. Estimates can be by parametric, model-based (analogy), or bottom-up.

## 3.2 Estimates are based on software requirements.

Estimation should be based on what is to be tested (i.e., software requirements). In some cases, the software requirements are established by the requirements and/or development team without participation from the test team. As a primary stakeholder, the test team should review and understand the software requirements. Without the test team's contribution, no credible estimation can be established.

## 3.3 Estimates are influenced by expert judgment.

Before estimation begins, the test team may consider categorizing the software requirements into the following categories:

* Critical – The development team has little knowledge about how to implement it.
* High – The development team has a good understanding of how to implement, but it is not easy.
* Normal – The development team knows how to implement.

The test team expert(s) for each requirement should estimate how long it would take for testing the requirement. The categories would assist the experts in estimating the effort for testing the requirements. Expert judgment by experienced developers is used to influence and adjust the estimates. For updated estimates, the test team may consider revisions based on better knowledge of the critical, high, and normal categories. The knowledge or determination that some requirements gain higher priorities over other requirements may be factored into the updated estimates.

## 3.4 Estimation tools should be used.

Tools that take into consideration the estimation principles and influencing factors help to quickly reach the estimate. A tool (spreadsheet) will automatically calculate the costs and duration for each testing activity and produce an estimate based on the known assumptions.

## 3.5 Estimates should be verified.

Estimates can be verified by a subject matter expert (other than the one that developed the estimate) and/or other tools. A comparison of estimates that reveal similar trends confirms the estimate, but if significant deviations are present, analysis is done and a re-estimate is performed.

## 3.6 Other Considerations.

The estimate will include consideration for the development and/or acquisition of the test environment, the procurement or lease of any testing-related tools, and training of personnel who either operate the test environment or the software under test itself.

## 3.7 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 4. Estimating Techniques

Estimation is not only about effort. The importance of domain knowledge, risk, complexity, historical data, and resource availability all play a role in successful estimating. Therefore, different cost estimation techniques should be used.

Analogy and parametric (model-based; see [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation)) methods are the most widely used because of their repeatable and re-usable nature.  COCOMO [159](#_tabs-<p>6</p>) and its variants are prime examples. These methods reflect an algorithmic approach based on metrics and historical data to calculate the estimate. However, the algorithmic estimation can be difficult because of the need to estimate the attributes of the finished product. Algorithmic cost models support quantitative option analysis.

Another estimating technique is the Use-Case Point Method [416](#_tabs-<p>6</p>).  This method is based on the use cases where the unadjusted actor weights and unadjusted use case weights are calculated to determine the software test estimates. The formula used for this technique is:

* Unadjusted actor weights = total number of actors (positive, negative, and exceptional).
* Unadjusted use case weight = total number of use cases.
* Unadjusted use case points = Unadjusted actor weights + Unadjusted use case weight.
* Adjusted use case point = Unadjusted use case point \* [0.65+ (0.01 \* 50].
* Total Effort = Adjusted use case point \* 2.

In the Wideband Delphi Method, [349](#_tabs-<p>6</p>) the work breakdown structure is decomposed for each task and is distributed to a team of 3-7 members for estimating the task. The final estimate is the result of the summarized estimates based on the team consensus. This method speaks more on experience rather than any statistical formula. This method was popularized by Dr. Barry Boehm, TRW Emeritus Professor of Software Engineering at the Computer Science Department of the University of Southern California, to emphasize group iteration to reach a consensus where the team visualized on the different aspects of the problems while estimating the test effort.

Software test estimate techniques just provide the means for estimating. They depend heavily on the team productivity variations, individual skills, complexity of the unknown factors like system environment and downtime.  In any method, expert judgment from domain experts provides insight, often arriving at the final estimate agreement through an iterative process.  Because no model is exact, all models can be useful.  Different techniques of cost estimation should be used to derive the most accurate estimate.

## 4.1 Summary

Even though estimates can be imprecise, they are extremely useful in planning the software test activities. Like all "living" documents, estimates are iterative and should be revised and controlled.

Estimates should be frequently analyzed and corrected as assumptions change. Collecting metrics and creating estimating "intelligence" is essential for on-going success. The metrics will also help build contingency and risk mitigation plans and gain confidence in management.

For each project, specific aspects of the project (process, resources, and complexity) influence the time required for various activities. When preparing a test estimate, it is important for management and the test team (who help with estimation) to consider how each of these factors affects the estimate. Forgetting just one of these factors can turn a reasonable estimate into an improbable one. Experience is often the ultimate teacher of these factors, but smart test managers can learn to ask smart questions about whether and how each factor will affect their project.

Start early and stay focused!

## 4.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 5. Levels of Testing

The test estimation effort is also impacted by the varying test levels that may be necessary during the implementation and test phases of the Software Project. The Software Test Plan (STP) is developed to document the test methodology and plans. The major test cycles applicable throughout software development are shown graphically and described below. Further information on test planning can be found in [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan). Software Assurance (SA) is typically present at the Flight Software (FSW) Acceptance Review.

## 5.1 Unit Test

Unit Test often equates to the smallest testable piece of code that may be isolated, or Computer Software Unit (CSU), but may also include a group of closely related units. Testing at this level is intended to determine if the software performs as designed and may employ techniques such as model checking, static analysis, and code inspections. These tests are usually performed in isolation by the development team members using drivers or stubs developed for test execution. For more guidance on software unit tests, see [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test).

## 5.2 Integration Test

The focus of software integration testing is to ensure that the progressive aggregation of CSUs into Computer Software Components (CSCs) and Computer Software Configuration Items (CSCIs) satisfy the designed interactions between the lower-level units. As with Unit Testing, the development of drivers or stubs may be necessary to simulate the lower and higher levels as the environment transitions from the host platform to the target hardware. Integration testing also provides statement coverage, path coverage and interface testing between CSUs and CSCs, and whether the desired functions have been met. Integration testing may also provide integration with hardware components and systems. These tests may be performed by developers and/or test engineers independent of the software development activities.

Integration testing may also be considered the White Box testing method, where knowledge of the design implementation is necessary to develop and execute the test procedure.

## 5.3 Informal Test

Informal Test is typically limited to an individual, configured software CSCI or combination of CSCIs prior to the formal test phase. The informal test phase is usually a familiarization with the software and environment and allows for the development of test cases and test procedures. By executing the software under these conditions, the test engineer may initially have an ad hoc approach focused on the discovery of errors or defects.  But as the software matures and problem reports are addressed, the test procedures are refined to include traceability to requirements and objective evidence that the software implements the defined requirements. A Software Test Procedure (STP) document is produced to describe all necessary verification test steps. Further information on software test procedures can be found in [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan).

## 5.4 Formal Test

Formal Test is typically limited to an individual software CSCI or combination of CSCIs prior to the final integration with hardware. This testing ensures the software implementation of the defined requirements has been satisfied through verification activities. Prior to the start of formal test activities, a Test Readiness Review (TRR) is conducted to ensure that the TRR entrance criteria have been met and testing may begin.  Additional information may be found in NPR 7123.1, NASA Systems Engineering Processes and Requirements, [041](#_tabs-<p>6</p>) and NASA-SP-2007-6105, NASA Systems Engineering Handbook. [273](#_tabs-<p>6</p>)  The formal test phase typically requires Software Assurance participation and approval. During Formal Test, Software Assurance witnesses that problem reports are addressed, the procedures have been performed as documented, and that the objective evidence for pass/fail criteria is defined and observed during test execution. Development and execution of formal test procedure are typically performed by test engineers independent of the software development activities. See [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures), [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures).

Formal testing may also be referred to as Black Box testing where the inputs and outputs are defined as requirements and verified. While knowledge of the software design is preferred, Black Box testing does not require that the test engineer has insight into the actual implementation details of the design. A Software Test Report (see [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report)) is produced to document testing results.

## 5.5 Acceptance Test

Acceptance Test (see [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria)) is a system-level test, usually performed during the final integration of formally tested software with the intended flight or operations hardware prior to Project level acceptance. Additional information may be found in NPR 7123.1 [041](#_tabs-<p>6</p>) and NASA-SP-2007-6105. [273](#_tabs-<p>6</p>)

## 5.6 Regression Test

Regression Test is a test method that is applicable at all levels of testing. Performed after any modifications to code, design or requirements, it assures that the implemented changes have not introduced new defects or errors. Regression testing may be completed by re-execution of existing tests that are traceable to the modified code or requirement. See also [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) .

## 5.7 Testing Techniques

## 5.8 Independence in Software Item Testing

For Class A, B, and Safety-critical class C software:

* The person(s) responsible for software testing of a given software item should not be the persons who performed detailed design, implementation or unit testing of the software item.
* This does not preclude persons who performed detailed design, implementation or unit testing of the software item from contributing to the process, for example by contributing test cases that rely on knowledge of the software items' internal implementation.

## 5.9 Software Assurance Witnessing

* The software test procedure developer should dry run the software item test cases and procedures to ensure that they are complete and accurate and that the software is ready for witnessed testing.
* The developer should record the results of this activity in the appropriate SDFs and should update the software test cases and procedures as appropriate.
* Formal and acceptance software testing is witnessed by software assurance personnel to verify satisfactory completion and outcome.
* Software assurance is required to witness or review/audit results of software testing and demonstration.

See also Topic [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing)

## 5.10 Testing on the Target Computer System

* Software testing should be performed using the target hardware.
* The target hardware used for software qualification testing should be as close as possible to the operational target hardware and should be in a configuration as close as possible to the operational configuration.
* Typically, high-fidelity simulation has the exact processor, processor performance, timing, memory size, and interfaces as the target system.

## 5.11 Capturing and Analyzing The Results

**Capture the results to:**

* Capture outcome of tests used to verify requirements, functionality, safety, etc.
* Capture decisions based on the outcome of tests
* Provide evidence of thoroughness of testing
  + Differences in the test environment and operational environment and any effects those differences had on test results
  + Test anomalies and disposition of related corrective actions or problem reports
  + Details of test results (e.g., test case identifications, test version, completion status, etc., along with associated item tested)
  + Location of original test results (output from tests, screenshots, error messages, etc., as captured during actual testing)

**Analyze results to:**

* Evaluate the quality of tested products and the effectiveness of testing processes
* Identify and isolate the source of errors found in software
* Verify testing was completed as planned
* Verify requirements have been satisfied
* Verify safety-critical elements were properly tested
* Verify all identified software hazards eliminated or controlled to an acceptable level of risk
* Report safety-critical findings used to update hazard reports
* Compare actual to expected results
* Identify discrepancies or mismatches in specification or behavior
* Document discrepancies individually for ease of tracking through the resolution process
* Determine the cause of an issue, including problems with testing methods, criteria, or environment
* Identify changes required to address discrepancies
* Evaluate and record the impact of changes needed to correct issues/discrepancies
* Plan for any repeat of the testing effort
* Obtain and record approval for changes to be made versus those to be addressed at different time
* Measure and predict the quality of the software based on the testing results (typically, a software assurance activity)

See [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results).

## 5.12 Test Metrics

**Sample Software Test Metrics**

* Defects or problem reports found
* Static code analysis metrics
* Code coverage
* Test schedule metrics
* Test Procedure Development Status
* Software Release/Build Status
* Number of tested requirements
* Traceability – Software Requirements to Test Procedures
* Defects or problem reports open and closed, trending for closure

## 5.13 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 6. References

## 6.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-135)

  [Software Cost Estimation with COCOMO II,](https://www.amazon.com/Software-Cost-Estimation-COCOMO-II/dp/0137025769 "Click to open in new window")

  Boehm, B., et. al. (2000). Prentice Hall, Upper Saddle River, N.J.,  ISBN-10: 0130266922
* (SWEREF-159)

  [COCOMOTM II.](https://csse.usc.edu/csse/research/COCOMOII/cocomo_main.html "Click to open in new window")

  In Center for Systems and Software Engineering, University of Southern California.
* (SWEREF-170)

  [NASA Study on Flight Software Complexity.](https://www.nasa.gov/pdf/418878main_FSWC_Final_Report.pdf "Click to open in new window")

  D. Dvorak, Presented at AIAA Infotech@Aerospace, Seattle, WA, April 2009. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-348)

  [An Investigation on Application Domains for Software Effort Distribution Patterns,](https://sercuarc.org/publication/?id=54&pub-type=Conference%20Paper&title=An+Investigation+on+Application+Domains+for+Software+Effort+Distribution+Patterns "Click to open in new window")

  Thomas Tan, Barry Boehm, Brad Clark (2011), Systems Engineering Research Center, http://www.sercuarc.org/news/view/7.
* (SWEREF-349)

  [Wideband Delphi Method,](http://leansoftwareengineering.com/wideband-delphi/ "Click to open in new window")

  Thompson, Bernie. (2012). In Lean Software Engineering: Essays on the Continuous Delivery of High Quality Information Systems. Retrieved March 20 from http://leansoftwareengineering.com/wideband-delphi/.
* (SWEREF-416)

  ["Software cost estimation using use case points: Getting use case transactions straight"](http://www.ibm.com/developerworks/rational/library/edge/09/mar09/collaris_dekker/ "Click to open in new window")

  Collaris, R.A. and Dekker, E. (March 15, 2009). IBM. Developer Works website.

  

## 6.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 6.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing)       * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) |

## 6.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>6</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation)      * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

## 6.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 7. Lessons Learned

### 7.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 7.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
