# 8.01 - Off Nominal Testing

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695701. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing

8.01 - Off Nominal Testing

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695701)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695701&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Topic](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Assets](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)

# 1. Topic

Guidance focusing on out of bounds parameters, failure scenarios, unexpected conditions, and capabilities that are typically considered as "must not work" functions.

# 2. Rationale

Off-nominal behaviors (ONBs) are unexpected or unintended behaviors a system may exhibit. They arise when unexpected external stimuli, such as unpredicted sequences of events, out-of-range data values, and environmental issues (e.g., unexpected issues related to hardware, memory, and network) disrupt a system. It is commonly thought that critical ONBs lack identification and testing coverage. Occurrences of ONBs can compromise the safety and reliability of a system, which can be very dangerous in safety-critical systems like NASA’s spacecraft, where software issues can lead to expensive mission failures [622](#_tabs-<p>5</p>), [624](#_tabs-<p>5</p>) injuries, or even loss of life [625](#_tabs-<p>5</p>). To ensure the safety of the system, engineers must identify potential causes of ONBs, and the system must specify and verify the handling of ONBs.

See also:

* [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)
* [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior)

# 3. Guidance

Engineers often treat Off-nominal behaviors (ONBs) as an afterthought. The causes of ONBs and how the system should react to ONBs often are nonexistent, incomplete, or vague in project documentation, including design, requirements, and tests. The lack of documentation on ONBs makes testing the system much harder. To address this problem, engineers can understand the notion of ONBs based on whether the system functions correctly and whether all system behaviors are specified or documented explicitly. See the categorization scheme shown in table 1 below.

Table 1. Categorization Scheme of Behaviors

|  | In Requirements | Not In Requirements |
| --- | --- | --- |
| Functioning | Good Behavior | Good Surprise |
| Not Functioning | Bug / Defect | Bad surprise |

**Good behavior**: Good behavior encompasses all behaviors that function correctly. Engineers can trace back the behaviors in this category to a requirement or design artifact. This is the nominal behavior of a system.

**Bug/defect**: Bugs or defects are issues in a system (e.g., due to incorrect implementation) that are traceable from the intended/correct behavior to a requirement or design artifact. These are considered ONBs because these behaviors are not intentional and cause the system to behave in an incorrect way. These behaviors violate the requirements and design documents, which formalize the intentions and expectations.

**Surprise**: The surprise category contains behaviors that function without detrimental effects on the system and serve a distinct purpose but are not documented in the requirements. These are ONB because the behavior is undocumented. This class of behaviors is often overlooked; instead, the focus is on behaviors that tend to have detrimental effects on the system. However, undocumented good behavior can be problematic as well. For example, a back door that provides a utility to the developers and testers of the system can become a security vulnerability. System behavior that is not well-documented also can create problems if the system has to be maintained or extended. Developers could, for example, alter or remove undocumented behaviors without realizing it.

**Bad surprise**: Bad surprises encompass all the off-nominal behaviors with detrimental effects on the system that are not traceable to a requirement or design artifact. A system crash due to an unspecified, and therefore missing, the error-handling routine is an example of a bad surprise. Depending on their nature, the impact of the off-nominal behaviors in this category can be more severe than the off-nominal behaviors in the bug/defect category. The severity of the ONB and the nature of the system dictate if and how the ONBs should be addressed. In less safety-critical systems (e.g., regular websites), ONBs like these might be ignored unless the customers specifically complain about them; however, in safety-critical systems, these kinds of the off-nominal behaviors can be dangerous. Knowing that an ONB exists and what impact it has on the system allows developers to make informed decisions when addressing the ONB.

See also:

* [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design)
* [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test)
* [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) - The software responds to an off-nominal condition within the time needed to prevent a hazardous event.
* [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis)
* [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists)
* [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase)
* [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis)
* [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis)
* [9.03 Coding Standards](/spaces/SWEHBVD/pages/102695794/9.03+Coding+Standards) +
* [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response)
* [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode)
* [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling)

## 3.1 Managing ONBs

The first step to managing ONBs is to identify off-nominal scenarios and specify their expected behaviors during the requirements elicitation phase. Engineers or system analysts can leverage several of the following requirements engineering methods to identify ONBs:

1. 1. **Misuse case [626](#_tabs-<p>5</p>)** is a form of use case that focuses on negative-use scenarios. It describes how a user can misuse a system and how the system should react to the misuse. Software engineers or requirement analysts typically use the misuse case approach for eliciting security requirements, but the technique is also useful for threat and hazard analysis. For such analysis, the negative agent is usually the failure of a safety-related device, such as a car brake, or an inanimate external force, such as dangerous weather. See [4] for more information about the misuse case.
   2. **Hazard analysis** is a technique for systematically identifying potential hazards to the system as well as their causes and controls. ONB is a common cause of hazards. An example of a hazard analysis technique for a software-intensive system is the Systems-Theoretic Process Analysis (STPA) proposed by Takuto Ishimatsu and Nancy G, Levenson [627](#_tabs-<p>5</p>), [628](#_tabs-<p>5</p>). STPA includes a broad set of potential hazard scenarios, including those in which no failures occur but problems arise due to unsafe and unintended system component interactions, which can result from design flaws or unsafe interactions among nonfailing (operational) components.
   3. **Requirements modeling** is an approach for formalizing requirements into models (e.g., Systems Modelling Language (SysML)). Engineers (or in some cases, tools) can analyze the models for correctness and completeness. For example, one can negate nominal system activities modeled in SysML activity diagrams (e.g., “spin-up” activity is turned into “failure to spin up”). Engineers can analyze the relationships between the negated activity, the component that allocates the activity, the state variables that characterize the component, and the relationships among the variables, to derive the failure modes and ONBs leading to the failure modes [629](#_tabs-<p>5</p>). Sequence-based enumeration is a method that systematically specifies all possible sequences and therefore also covers those sequences that normally would have been forgotten and could result in ONB [630](#_tabs-<p>5</p>).

Just by conducting requirements engineering, engineers cannot ensure that all ONBs will be identified because they cannot feasibly enumerate all of the many potential causes of ONBs. Rather, engineers need a complementary approach that leverages artifacts from the testing process (e.g., models, source code, executables of the system, or executable models) as well as execution data from test case executions or log files).

See also:

* [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) - checking for software responding to an off-nominal condition within the time needed to prevent a hazardous event
* [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements)
* [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements)
* [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis)
* [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation)
* [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)
* [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements)
* [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)

## 3.2 Robustness testing

**Robustness testing** is a testing method and approach that focuses on verifying and validating the system’s ability to operate correctly or safely or to degrade gracefully in the presence of exceptional or unforeseen scenarios (e.g., invalid or unexpected input, network failures, hazardous environment conditions). What differentiates robustness testing approaches are the methods of choosing or generating input (including simulating stressful conditions) to provide to the system under test.

Fuzz or fuzzy testing is a class of robustness testing that focuses on providing randomly generated data as (sequences of) input to the system. The data provided are typically, but not limited to, invalid and unexpected input for the purpose of identifying a system’s vulnerability related to boundary values and insufficient validation of input. The latter vulnerability, especially, can lead to security breaches (e.g., Structured Query Language injection attacks, memory leaks). Multiple approaches exist for generating the input values: 1) mutating an initial sample of input randomly or semi-randomly using heuristics or 2) generating the values based on specifications or models of the input.

Another robustness testing approach utilizes fault injections to test ONBs of systems. Engineers instrument the system under test and inject faults, such as ones that corrupt the data variables (e.g., negated Boolean variables, buffers overrun to modify return address of stack frame) or simulate failing system resources (e.g., memory allocation errors, network failures, file input and output problems) during runtime [631](#_tabs-<p>5</p>), [632](#_tabs-<p>5</p>).

Model-based testing is an approach where the engineers or testers create a model of a system, usually represented as a finite state diagram, from existing specifications, and generate test cases systematically to ensure sufficient coverage of the model and, therefore, the system behavior. Studies [633](#_tabs-<p>5</p>), [634](#_tabs-<p>5</p>), [635](#_tabs-<p>5</p>) have shown that model-based testing to be an effective and efficient testing approach [633](#_tabs-<p>5</p>), [635](#_tabs-<p>5</p>), [636](#_tabs-<p>5</p>). Engineers can apply model-based testing to test the system’s off-nominal behaviors; however, the approach requires that the testing model also includes ONBs. Manually constructing testing models that include ONBs (an off-nominal model) can be time-consuming and error-prone due to a large amount of the potential the off-nominal behaviors. Instead, engineers can implement a tool to create an off-nominal model automatically from an existing nominal model following these steps:

1. the algorithm iterates through each state in the nominal model (with the exception of the start and potential exit states);
2. in each state, the algorithm compares the outgoing transitions to the list of all possible transitions and adds all unspecified transitions to the state;
3. the algorithm then generates a test case for each of the newly added transitions and executes it. 
   1. If the execution of the test case reveals that the transition is not feasible, the algorithm will remove the transition.
   2. Otherwise, the algorithm will add the transition as a loop to its state of origin. This represents the behavior where the system ignores an illegal or invalid input (e.g. a command) and, therefore, it does not affect or change the state of the system. If the test execution incorrectly changed the state, then the test case will fail and detect an ONB.

See also

* [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures)
* [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels)
* [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality)
* [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis)
* [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports)
* [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)
* [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)
* [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures)
* [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan)
* [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation)

## 3.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Assets

## 4.1  Tools

The testing framework for model-based testing that can be used to test for off-nominal behaviors (ONB) consists of two components: yEd  [638](#_tabs-<p>5</p>), which is a graphical editor used to model the behavior of the system under test as a black box, and the Fraunhofer Approach to Software Testing (FAST) tool, which generates test cases from such models. The modeling part is agnostic to the underlying technologies used to implement the system under test. FAST has been used to test web-based systems and other systems implemented in C/C++, C#, Python, Java, etc. A test execution framework such as Junit [639](#_tabs-<p>5</p>) is necessary to execute the generated test cases. The topic of test execution frameworks is, however, out of scope in this context.

The Fraunhofer Center for Experimental Software Engineering developed the FAST tool as part of several Software Assurance Research Program (SARP) projects. It enables a straightforward approach to model-based testing and is based on GraphWalker [640](#_tabs-<p>5</p>), which is a model-based testing tool built in Java. The FAST tool reads models in the form of finite-state diagrams or directed graphs and generates tests from the models. The FAST tool also allows testers to manage, maintain, and visualize (e.g., test coverage) their model-based testing efforts [633](#_tabs-<p>5</p>).

The yEd tool is freely available. Fraunhofer has uploaded the FAST tool to NASA NEN together with a complete tutorial on how to use yEd and FAST to model and generate test cases. The tutorial package includes a set of models that can be used to experiment with the toolset. To illustrate the full life cycle from creating a test model to running test cases that can find defects in the system under test, a full example including links to the Selenium [641](#_tabs-<p>5</p>) testing framework is included. The generated test cases run immediately without any editing in the Selenium integrated development environment. Please forward any questions on FAST and the tutorial to [mikli@fc-md.umd.edu](mailto:mikli@fc-md.umd.edu).

## 4.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-622)

  [Role of Software in Spacecraft Accidents](http://sunnyday.mit.edu/papers/jsr.pdf "Click to open in new window")

  N. G. Leveson, Journal of Spacecraft and Rockets, vol. 41, no. 4, pp. 564–575, Jul. 2004
* (SWEREF-624)

  [ARIANE 5 Flight 501 Failure](http://sunnyday.mit.edu/nasa-class/Ariane5-report.html "Click to open in new window")

  Report by the Inquiry Board, The Chairman of the Board : Prof. J. L. LIONS
* (SWEREF-625)

  [An investigation of the Therac-25 accidents](https://web.stanford.edu/class/cs240/old/sp2014/readings/therac-25.pdf "Click to open in new window")

  Leveson, N. G. and Turner, C. S. ; Computer (Long. Beach. Calif)., vol. 26, no. 7, pp. 18–41, Jul. 1993.
* (SWEREF-626)

  [Misuse Cases: Use Cases with Hostile Intent](https://pdfs.semanticscholar.org/225b/b4941eb421f7fa2548fd7c087ff1a3c3f8f9.pdf "Click to open in new window")

  Alexander, Ian; IEEE Softw., vol. 20, no. 1, pp. 58–66, Jan. 2003.
* (SWEREF-627)

  [Hazard Analysis of Complex Spacecraft using SystemsTheoretic Process Analysis \*](http://sunnyday.mit.edu/papers/JSR-paper-published.pdf "Click to open in new window")

  T. Ishimatsu, N. G. Leveson, J. P. Thomas, C. H. Fleming, M. Katahira, Y. Miyamoto, R. Ujiie, H. Nakao, and N. Hoshino, J. Spacecr. Rockets, vol. 51, no. 2, pp. 509–522, Mar. 2014
* (SWEREF-628)

  [An STPA Primer](http://www.santoslab.org/pub/high-assurance/module-risk-management/reading/STPA-Primer-v0.pdf "Click to open in new window")

  Leveson, Nancy ; Version 1, August 2013 The old STPA Primer (2013) has been replaced by the STPA Handbook (2018), which provides updated guidance and more information. See http://mit.edu/psas to download a free copy of the STPA Handbook.
* (SWEREF-629)

  [Modeling Off-Nominal Behavior in SysML](https://pdfs.semanticscholar.org/1a13/40a86826d89b7ceebcb2d198a0643db39f12.pdf "Click to open in new window")

  John C. Day, Kenneth Donahue , Michel Ingham, Alex Kadesch, Andrew K. Kennedy and Ethan Post; Jet Propulsion Laboratory, California Institute of Technology, Pasadena, CA, 91109
* (SWEREF-630)

  [Foundations of Sequence-Based Software Specification](https://dl.acm.org/citation.cfm?id=776809 "Click to open in new window")

  S. J. Prowell and J. H. Poore, IEEE Transactions on Software Engineering, vol. 29, no. 5, pp. 417-429, May 2003,
* (SWEREF-631)

  [Inoculating software for SURVIVABILITY](https://www.semanticscholar.org/paper/Inoculating-software-for-SURVIVABILITY-An-old-adage-Voas/9428e09f1709dae265372c08a3d92cec788e1f02 "Click to open in new window")

  A. K. Ghosh and J. M. Voas, Commun. ACM, vol. 42, no. 7, pp. 38–44, Jul. 1999.
* (SWEREF-632)

  [An Approach to Testing COTS Software for Robustness to Operating System Exceptions and Errors](https://dl.acm.org/citation.cfm?id=856201 "Click to open in new window")

  A. K. Ghosh and M. Schmid, in Proceedings 10th International Symposium on Software Reliability Engineering (Cat. No.PR00443), 1999, pp. 166–174.
* (SWEREF-633)

  [Testing object-oriented systems: models, patterns, and tools](https://dl.acm.org/citation.cfm?id=338330 "Click to open in new window")

  R. Binder; Addison-Wesley Professional, 2000.
* (SWEREF-634)

  [Model-based testing of NASA’s GMSEC, a reusable framework for ground system software](https://link.springer.com/article/10.1007/s11334-015-0254-6 "Click to open in new window")

  Vignir Gudmundsson , Christoph Schulze, Dharmalingam Ganesan, Mikael Lindvall and Robert Wiegand; Innovations in Systems and Software Engineering, Volume (ISSE), Vol 11, Number 3, 217—232, 2015
* (SWEREF-635)

  [Assessing model-based testing: an empirical study conducted in industry](https://dl.acm.org/citation.cfm?id=2591180 "Click to open in new window")

  Christoph Schulze, Dharmalingam Ganesan, Mikael Lindvall, Rance Cleaveland, Daniel Goldman; ICSE Companion 2014: 135-144
* (SWEREF-636)

  [Model Generation to support Model-based Testing Applied on NASA DAT](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20180004562.pdf "Click to open in new window")

  Christoph Schulze, Mikael Lindvall, Sigurthor Bjorgvinsson, Robert Wiegand; ISSRE 2015: 77-87
* (SWEREF-637) Improving model based testing to detect off-nominal Behaviors, Christoph Schulze, Mikael Lindvall, Dharmalingam Ganesan, Arnab Ray; Fraunhofer Technical Report, December 2015. Available upon request from Fraunhofer.
* (SWEREF-638)

  [yEd Graph Editor](http://www.yworks.com/en/products_yed_about.html "Click to open in new window")

  yEd is a powerful desktop application that can be used to quickly and effectively generate high-quality diagrams
* (SWEREF-639)

  [JUnit](https://en.wikipedia.org/wiki/JUnit "Click to open in new window")

  JUnit is a unit testing framework for the Java programming language. JUnit has been important in the development of test-driven development, and is one of a family of unit testing frameworks which is collectively known as xUnit that originated with SUnit
* (SWEREF-640)

  [GraphWalker,](http://www.graphwalker.org/ "Click to open in new window")

  GraphWalker, an open-source model-based testing tool
* (SWEREF-641)

  [Selenium](http://www.seleniumhq.org/ "Click to open in new window")

  Selenium automates browsers.
* (SWEREF-642)

  [Goddard Mission Services Evolution Center (GMSEC) API](https://opensource.gsfc.nasa.gov/projects/GMSEC_API_30/index.php "Click to open in new window")

  Goddard Mission Services Evolution Center (GMSEC)

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-131 - Independent Verification and Validation Project Execution Plan](/spaces/SWEHBVD/pages/102695492/SWE-131+-+Independent+Verification+and+Validation+Project+Execution+Plan) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-141 - Software Independent Verification and Validation](/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)       * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists) * [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [9.03 Coding Standards](/spaces/SWEHBVD/pages/102695794/9.03+Coding+Standards) * [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response) * [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode) * [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>5</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Requirements](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Requirements)      * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design)      * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration)      * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

Lessons that appear in the NASA LLIS or Center Lessons Learned Databases.

### 6.2 Other Lessons Learned

Lessons that appear in the sources outside of NASA Lessons Learned databases.

* **Model-based testing approach and ONBs**: With the model-based testing approach, adding off-nominal behaviors (ONBs) to a testing model can significantly increase the model’s size and complexity and, therefore, also increase the number and length of test cases the model can generate. Because model-based testing automatically generates test cases, there is no added cost for generating the test cases; however, more tests are not always the solution. It still costs money to execute the test cases, making it necessary to prioritize test cases for execution—especially if it takes a long time to execute each test case. More importantly, in the context of testing for ONBs, because the off-nominal testing model will include both nominal and off-nominal behaviors of the system, a test case generated from the model may also include both behaviors. This can make the generated test cases harder to comprehend. In the case of failures in the test execution, these test cases also can become harder to analyze and debug because it is not clear what the objective of each test case is. The solution to this problem is to conduct the testing in layers, as well as to annotate the model with requirements or use cases. The engineers would start by generating short test cases that are requirements- or use-case-oriented, making the objective clear for each test case. As the engineers uncover and then remove ONBs[TD(1], they can have the higher trust of the basic layer of functionality and generate more complex variants of test cases[TD(2] . Furthermore, due to the length of more complex test cases, it often takes more time to analyze the root cause of an issue. The solution is to include enough information in the generated test cases that one can quickly identify the cause when the test case fails.  
    
  Fraunhofer investigated the use of a generic approach that leverages the concept of abstract fault models to generate test cases that better target specific ONBs. It constructed abstract fault models by examining common testing scenarios and deriving testing patterns that can identify a specific issue (e.g., failure to release resources). The following is an example of fault models that include ONB according to patterns based on inverse characteristics [17]:

**INVERSE CHARACTERISTIC**: In mathematics, an inverse function (??−1(??)) is a function that "reverses" another function (??(??)). Examples of this are the functions publish and getMessage from the Goddard Mission Services Evolution Center (GMSEC) system [642](#_tabs-<p>5</p>), [633](#_tabs-<p>5</p>). Publish adds an element to the message queue, thereby changing the state space of the system, and getMessage removes the element again, which reverses the change to the state space that publish performed.

FAULT MODELS: The inverse characteristic has the following fault models:

1.) Repeated calling: This fault model checks that the system behaves properly even if stressed by repeatedly calling function ?? and its inverse ??−1. This behavior identified an issue in the connect and disconnect functionality of GMSEC.

2.) Cleanup: This fault model is known in the literature as a sneak path [633](#_tabs-<p>5</p>). Fraunhofer uses the term cleanup instead because the term is more representative of the fault scenario. It first calls function ?? followed by its inverse ??−1. It then checks if the inverse function ??−1 correctly removed the changes from ?? by calling ??−1 again. This behavior identified an issue in the publish and getMessage functionality of GMSEC. It identified an issue where one published message could be received twice if the getMessage and getMessage ONB calls were in close succession.

* **Stopping Criteria**: The traditional stopping criteria for test-case generation is based on transition coverage of the model or on a random traversal through the model with a fixed number of transitions. Such stopping criteria are not always adequate in identifying all the issues in the system, even with a “complete” model. Using stopping criteria based on the coverage of scenarios derived from the abstract fault modes generates more thorough test cases.
