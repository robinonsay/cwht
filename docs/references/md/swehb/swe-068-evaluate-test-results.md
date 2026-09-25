# SWE-068 - Evaluate Test Results

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695451. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results

SWE-068 - Evaluate Test Results

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695451)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695451&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. The Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)
* [8. Objective Evidence](#tabs-8)

# 1. Requirements

4.5.5 The project manager shall evaluate test results and record the evaluation.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-068 History

SWE-068 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.4.4 The project shall evaluate test results and document the evaluation. |
| Difference between A and B | No change |
| B | 4.5.5 The project manager shall evaluate test results and record the evaluation. |
| Difference between B and C | No change |
| C | 4.5.5 The project manager shall evaluate test results and record the evaluation. |
| Difference between C and D | No change |
| D | 4.5.5 The project manager shall evaluate test results and record the evaluation. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 2. Rationale

Test results are the basis for confirming that the team has fulfilled the software requirements in the resulting software product. To make such decisions, test results must be reviewed and evaluated using a documented, repeatable process. The team can derive quality conclusions by capturing the actual test results, comparing them to expected results, analyzing those results against pre-established criteria, and documenting that analysis/evaluation process.

It is important to document and retain elements used to generate and analyze the results for future regression testing and related test results analysis.

The act of evaluating test results and recording the evaluation is a critical step in the software development and assurance process. This requirement ensures that test results are properly reviewed, analyzed, and documented, providing an evidence-based foundation for advancing to subsequent lifecycle phases. Below are several key considerations that highlight the rationale behind this requirement:

---

### **1. Ensuring Product Quality and Readiness**

* **Purpose**: Evaluating test results provides assurance that software meets its intended functionality, performance, and requirements. This includes identifying and addressing errors, defects, and anomalies revealed during testing.
* **Outcome**: This evaluation ensures the readiness of the software for further testing phases, integration, or deployment, minimizing risks during critical phases (e.g., operations, flight).

---

### **2. Accountability and Risk Management**

* **Purpose**: Recording the evaluation provides a formal, auditable track of decision-making and accountability. It ensures that test results are tied to specific decisions (e.g., "proceed with deployment," "retry test after addressing anomalies").
* **Outcome**: The project manager's recorded evaluation allows stakeholders to understand the logic behind crucial project decisions, mitigating risks of unreviewed or improperly handled results.

---

### **3. Support Change Control and Traceability**

* **Purpose**: By formally documenting test result evaluations, the project maintains traceability for change requests or problem reports that are tied to specific tests. This is crucial for understanding the impact of defects or changes on the project.
* **Outcome**: Enables better CM (Configuration Management) practices by linking test results to baselines, builds, and requirements.

---

### **4. Data Integrity and Knowledge Retention**

* **Purpose**: Testing produces valuable insights about the software, its interactions, and edge case behaviors. Properly recording evaluations ensures retention of this knowledge for reference in future phases or in lessons learned for future projects.
* **Outcome**: Documentation preserves critical data for validation, safety certification, regression testing, or failure analysis.

---

### **5. Alignment with NASA Mission Assurance**

* **Purpose**: NASA's processes emphasize rigor and reproducibility to enable mission success. Evaluating and recording test results supports compliance with NASA-required assurance steps to ensure software reliability and performance.
* **Outcome**: This requirement aligns with NASA safety, quality, and assurance policies for verifiable and traceable decision-making.

---

### **6. Identifying Trends and Systemic Issues**

* **Purpose**: Evaluating test results allows the project manager to identify trends (recurring defects, frequent failures in specific modules, etc.) and systemic issues across software functionality or test environments.
* **Outcome**: By understanding trends, the project can implement corrective actions that prevent recurring issues, saving time and resources in future tests or phases.

---

### **7. Communication and Transparency**

* **Purpose**: Clear evaluation and recording of test results ensure all project stakeholders, including the customer, Software Assurance team, and IV&V team (Independent Verification and Validation), are aware of the status of the software and any remaining issues.
* **Outcome**: Builds confidence and trust among stakeholders and ensures alignment between the development team and external assurances.

---

### **Consequences of Not Meeting the Requirement**

Failing to evaluate and record test results can lead to several negative consequences:

1. **Inappropriate Decision-Making**: Without proper test result evaluation, decisions may be made based on incomplete or inaccurate information, increasing the risk of software failures in operational phases.
2. **Loss of Accountability**: Test results will lack traceability, reducing auditability and credibility in critical reviews (e.g., Test Readiness Review [TRR], Safety Reviews).
3. **Reduced Quality Assurance**: Missed defects or unresolved issues could escape review and propagate to later stages, causing deficiencies in critical systems.
4. **Missed Lessons Learned**: Valuable insights from testing may not be recorded or analyzed, preventing process improvement or awareness of potential risks.

---

### **Conclusion**

[SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) ensures that test results are not just treated as outputs from testing activities but are actively reviewed, analyzed, and documented to inform project decisions and improve product quality. By mandating that the project manager evaluate and record these results, the process formalizes critical activities, ensures accountability, promotes traceability, and supports NASA’s overarching goal of delivering reliable, mission-critical software systems.

# 3. Guidance

## 3.1 Evaluation Of Software Testing

The evaluation of software testing is a highly detailed and systematic process essential for ensuring that software meets its functional, safety, and performance requirements. It involves examining test results, validating outputs against expected results, assessing coverage, and ensuring traceability to requirements. Below, the guidance has been refined to provide clear, actionable, and robust techniques for Software Assurance (SA) personnel to evaluate software testing more effectively.

Improving the evaluation of software testing transforms raw data into actionable insights. By maintaining rigorous processes, complete documentation, and repeatable procedures, Software Assurance ensures that every critical system's behavior conforms to mission safety, reliability, and quality standards. Following this upgraded guidance will provide consistent and traceable evaluations, mitigating risks across NASA’s software development lifecycle.

### 3.1.1 Proper Management of Software Test Data

* **Thorough Evaluation of Results**: All software test data should be evaluated comprehensively and compared systematically to the expected results defined in the test plan or requirements specifications. Any discrepancies must be fully documented and analyzed.
* **Addressing Large Test Data Volume**: Testing often generates substantial amounts of data. SA personnel should ensure:
  + Testing tools are configured to log only necessary and actionable data to prevent overwhelming analysis teams.
  + Automated tools are employed for filtering, processing, and analyzing test data, especially for larger projects.
  + Critical test results (e.g., safety-critical outputs) are prioritized for detailed evaluation.
* **Recording the Evaluation Process**: The process, criteria, and any tools used for test evaluations must be documented. This ensures repeatability and allows evaluation procedures to be easily reviewed during audits or reused in future assessments.

### 3.1.2 Repeatability and Consistency of Testing

* **Why Repeatability Matters**: Repeatable tests allow for consistent validation of results and ensure that identified defects can be addressed and resolved reliably. Tests should produce identical results each time they are conducted under the same configuration.
* **Documentation of Test Context**: To ensure repeatability, the test configuration and environment must be carefully documented, including:
  + **Test Tools and Infrastructure**: Record details such as specific test tools, compilers, operating systems, and third-party testing software.
  + **Code Version**: The exact software version or build under test must be recorded, ideally tagged in the version control system.
  + **Test Environment**: Include platform specifications such as hardware configurations (including memory, CPU, firmware versions) and simulation environments.
  + **Test Limitations**: Record any assumptions about the test's scope and limitations, such as components not covered or specific scenarios excluded.

### 3.1.3 Risk-Based Testing Prioritization

Software test evaluations should be performed across all projects, regardless of size; however, the level of rigor in testing should align with the risk profile of the project. SA personnel should ensure:

* **Safety-Critical Software**: Code classified as safety-critical requires the highest level of testing rigor and focus, adhering to NASA-STD-8739.8 [278](#_tabs-<p></p>) guidelines to ensure compliance with safety requirements.
  + Prioritize test cases that cover hazardous functions and potential mission-critical failure points.
* **High-Risk Areas**: Components with higher operational, safety, or mission-critical risks should be evaluated next. These may include modules with a history of defects, complex algorithms, or functions that are closely connected to interfacing subsystems.
* **Regression Testing**: Maintenance activities, patches, or updates to previously tested code must incorporate sufficient regression testing to ensure no unintended effects occur in safety-critical or high-priority areas.

### 3.1.4 Test Article Considerations

* **Testing Platforms**:
  + Hi-Fidelity Simulators or hardware-in-the-loop (HIL) testing environments should be used when possible to capture realistic behaviors.
  + Testing on actual flight hardware should be considered only when necessary and should be carefully planned to protect equipment. Refer to [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) for alternatives to real hardware testing.
* **Test Artifacts**:
  + Ensure that all test artifacts (e.g., models, simulators, and ground support software) are under configuration management, and record their versions to ensure traceability.

### 3.1.5 Analysis of Safety-Critical Software Test Results

Software assurance personnel should refer to NASA-STD-8739.8 and this handbook for structured analysis methodologies to evaluate the completeness and correctness of safety-critical testing results:

* Verify that all safety-critical software requirements are tested or evaluated, including any hazardous functionality (e.g., inadvertent operator action per [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)).
* Evaluate whether the tests adequately demonstrate that all identified hazards have been eliminated or mitigated to an acceptable level.
* Ensure that safety-critical functions perform as expected and do not perform unintended or unsafe operations.

## 3.2 Developing a Comprehensive Test Results Analysis Methodology

To ensure consistency and thoroughness, Software Assurance should adopt a structured methodology for analyzing test results. Referencing IEEE-STD-1012-2004, the methodology should include the following steps:

1. **Validation of Results Against Requirements**:

   * Ensure software test results trace back to the test planning criteria and align with the established system requirements and test acceptance criteria.
2. **Analyze Coverage**:

   * Verify that all functional, performance, and safety requirements are exercised by the tests.
   * Identify gaps or areas requiring additional test cases.
3. **Test Conditions and Standards**:

   * Evaluate whether the testing approach (e.g., unit, integration, or system-level) applies adequate rigor based on the project’s risk level.
   * Assess the sufficiency of testing methods, inputs, and boundary conditions.
4. **Resolution of Discrepancies**:

   * Confirm that any anomalies or discrepancies (even minor ones) between test results and expected outcomes are resolved or properly dispositioned.

## 3.3 Items to Record and Relate to Test Analysis

All items associated with the generation and collection of test results must be documented for traceability and analysis. These include:

* **Test Drivers and Stubs**: Component-level drivers or stubs used to simulate external functionality.
* **Simulators and Models**: Any models or simulators used to replicate real-world environments during testing.
* **Test Suites, Cases, and Data**: Scripts or data used to conduct the tests.
* **Configuration Context**: Record of tools, versions, hardware, and environment settings utilized during testing.

## 3.4 Inputs to Test Results Evaluation

Additional factors for consideration during test result evaluations include:

* **Discrepancy Logs**: Capture discrepancies between actual and expected results, their causes, and resolutions.
* **Retest History and Justifications**: Document cases where tests were repeated due to environment issues, changes, or unexpected conditions.

## 3.5 Recommended Practices for Test Result Evaluations

To enhance the quality of test evaluations:

* Use checklists to ensure consistent analysis and verification of test results.
* Incorporate domain experts to validate results for specialized or critical software.
* Use automation tools where possible to sift through data, streamline analysis, and identify potential issues more efficiently.

## 3.6 Recording and Reporting the Results of Evaluation

At the conclusion of test results analysis:

* Record anomalies, problem reports, operational difficulties, root cause analysis, and any actions taken (e.g., fixes, mitigation steps).
* Document tests that could not be fully evaluated, including associated reasons.
* Clearly mark the pass/fail status of tests with justifications for all decisions.

**Related Requirements and Resources**

* NPR 7150.2 Section 4.5: Structured guidance on SWE, software assurance, and testing procedures including:
  + [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)
  + [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)
  + [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations)
  + [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior)
* NASA Software Engineering and Software Assurance Handbook

## 3.7 Analysis Practices

When performing the actual test results analysis/evaluation, consider the following practices [047](#_tabs-<p></p>)  :

* Use application or domain specialists as part of the analysis/evaluation team.
* Use checklists to assist in the analysis and ensure consistency.
* Use automated tools to perform the analysis, when possible.
* Capture a complete account of the procedures that were followed.
* If a test cannot be evaluated, capture that fact and the reasons for it.
* Plan the criteria to be used to evaluate the test results, consider (from a 1997 University of Southern California Center for System and Software Engineering project file entitled, “Software Test Description and Results”):
* The range or accuracy over which output can vary and still be acceptable.
* The minimum number of combinations or alternatives of input and output conditions constitute an acceptable test result.
* Maximum/minimum allowable test duration, in terms of time or number of events.
* The maximum number of interrupts, halts or other system breaks that may occur.
* Allowable severity of processing errors.
* Conditions under which the result is inconclusive and retesting is to be performed.
* Conditions under which the outputs are to be interpreted as indicating irregularities in input test data, in the test database/data files, or test procedures.
* Allowable indications of the control, status, and results of the test and the readiness for the next test case (maybe the output of auxiliary test software).
* Additional criteria not mentioned above.
* Any information about the setup of the test (including versions of tools, hardware, simulations, …) to make the test repeatable and provide context on assumptions and limitations.

When recording the outcome of the analysis, important items to include are:

* Major anomalies.
* Problem reports were generated as a result of the test.
* Operational difficulties (e.g., constraints or restrictions imposed by the test, aspects of the requirement under test that could not be fully verified due to test design or testbed limitations).
* Abnormal terminations.
* Reasons/justifications for discrepancies (e.g., caused by test cases or procedures, not a product issue).
* Any known requirement deficiencies present in the software element tested.
* Corrective actions were taken during testing.
* Success/failure status of the test.

Additional guidance related to software test results may be found in the following related requirements in this Handbook:

* [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)

NPR 7150.2 - Section 4.5 SWEs including:

* [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports)
* [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)
* [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)
* [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools)
* [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures)
* [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations)
* [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items)
* [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements)
* [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage)
* [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing)
* [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements)
* [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior)
* [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software)

## 3.8 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action),      * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

## 3.9 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only).

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

Software testing is an essential activity regardless of project size. Even small projects require structured testing to ensure that the software meets its requirements and operates safely and effectively. The approach to testing in small projects must balance the needs for rigor and practicality, taking into account the scope, risk, and constraints specific to the project. Below is enhanced guidance for testing activities in small projects, with a focus on prioritization, risk assessment, and repeatability.

---

### **1. Tailored Testing Based on Risk Posture**

* **Risk-Based Testing**:

  + The level of testing rigor should align with the risk posture of the project. Projects with lower risk (non-critical applications) may require less comprehensive testing, while higher-risk projects must adopt stringent practices.
  + Safety-Critical Software is the highest priority and must receive the full spectrum of testing activities, following NASA-tested protocols (e.g., [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements)). Always prioritize tests that demonstrate compliance with safety-critical requirements and eliminate or mitigate hazards.
  + Functions deemed critical to mission success (but not explicitly safety-related) should be tested next, focusing on reliability, accuracy, and performance.
* **Examples of Risk Prioritization**:

  + For non-critical projects like research software or data visualization tools, focus may be on functional testing without extensive coverage metrics.
  + For small projects involving spacecraft or operational systems, adopt rigorous testing methods (e.g., unit, integration, regression, and performance testing).

---

### **2. Testing Scope and Approach**

* **Unit Testing for Small Components**:

  + Unit tests are foundational and ensure that individual functions or modules work as intended. Small projects should prioritize writing unit tests for key components, especially those with complex logic or interfaces.
  + For reusable or shared components, achieve sufficient test coverage to verify their functionality across diverse scenarios.
* **Use of Coverage Testing**:

  + Perform code coverage analysis to verify that all parts of the software are exercised during testing.
  + Be cautious with 100% coverage metrics; while coverage is valuable, the absence of coverage gaps doesn’t guarantee defect-free code. Focus instead on branch, context, and functional coverage for safety-critical portions.
* **Risk-Mitigation Testing**:

  + Run regression tests periodically if any new changes are introduced, especially for critical functionality. This ensures that updates don’t inadvertently introduce defects into previously stable code.
* **Higher-Level (System or Integration) Tests**:

  + Where possible, conduct simulations and system-level tests to validate interoperability and performance across project components.
  + Use models or simulators for hardware/software integration testing to reduce the risk of damaging real “flight” hardware during testing.

---

### **3. Use of Test Articles**

* **Simulators and Models**:

  + Test articles such as simulators or models are strongly recommended for small projects where hardware may be expensive, unavailable, or vulnerable to damage. (Refer to [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) for guidance on using high-fidelity simulations).
  + High-quality simulators can emulate operational environments, allowing for realistic validation without posing risks to physical equipment.
* **Flight Hardware Testing**:

  + Testing on actual “flight” hardware should be minimized unless necessary. It must involve careful planning to avoid costly damage or operational failures.
  + Ensure tests conducted on hardware are systematically logged and reviewed to preempt future equipment issues.

---

### **4. Testing Tools and Practices**

* **Automation for Efficiency**:

  + Small projects often have limited resources. Use automated testing tools to simplify and streamline testing processes (e.g., unit test scripts, regression testing frameworks).
  + Leverage tools that align with project needs (GitLab CI, Jenkins, PyTest, etc.) to enforce continuous testing for small software projects.
* **Configuring Test Environments**:

  + Maintain consistent testing environments and clearly log environmental setups (e.g., versions of compilers, operating systems, configurations for models or simulations) for future reference. This ensures repeatability and reliability.

---

### **5. Documentation and Repeatability**

* **Test Records**:

  + Even for small projects, careful documentation is mandatory. Record all test plans, procedures, and results. These records provide traceability, demonstrate compliance, and can reveal trends or insights for process improvement.
  + Include the following in your documentation:
    - Version of software tested, linked to version control systems.
    - Configuration of test environment (e.g., compiler versions, OS, hardware).
    - Expected results, actual results, discrepancies, and dispositions.
    - Any anomalies detected and steps taken to resolve them.
* **Repeatable Tests**:

  + Design tests so they can be repeated in the same configuration to validate resolution of issues. Repeatability is key for proving reliability and establishing trust in the software.
  + Use testing tools and frameworks that enforce controlled environments, ensuring consistent results across multiple test cycles.

---

### **6. Prioritization of Test Types**

Small projects have finite resources, so testing activities should be prioritized based on the criticality of the functionality under test:

1. **Safety-Critical Testing**:
   * Prioritize software that directly impacts mission safety and operational risks.
   * Ensure thorough coverage and validations of safety-related functions, hazard mitigations, and failure scenarios.
2. **Mission-Critical Testing**:
   * Tests critical system operations tied to mission success, such as communications, navigation, or data processing.
3. **Basic Functional Testing**:
   * Verify that essential features meet requirements and perform correctly under expected operating conditions.
4. **Performance Testing**:
   * If applicable, validate that the software meets its expected performance metrics (e.g., execution time, memory usage).

---

### **7. Adapting for Small Team Constraints**

For small projects with fewer personnel or limited resources:

* **Focus on Risk Areas**:
  + Apply testing rigor to areas with the highest potential impact to mission or safety. Low-impact areas can be documented with reduced testing investments.
* **Tool Selection**:
  + Choose lightweight tools suitable for small teams and projects. Open-source testing frameworks (e.g., JUnit, PyTest, or TestNG) can provide effective solutions without the complexity of enterprise-grade tools.
* **Leverage Collaboration**:
  + Engage all stakeholders (developers, testers, project managers) collaboratively during testing activities to avoid miscommunication and inefficiencies.

---

### **8. Additional Considerations**

* **Continuous Testing**: Even for small projects, adopt continuous integration practices where testing becomes part of the software lifecycle (e.g., automated testing triggered by every commit).
* **Testing Constraints**: Recognize and document testing limitations for small projects. For example, restricted access to hardware or simulators may require focused testing on available resources.

---

### **Conclusion**

Testing is essential for all projects—large and small. While small projects may face resource constraints, safety-critical and mission-critical functionality should never be compromised. By tailoring testing activities to the project's risk profile, maintaining thorough documentation, and ensuring repeatability, small projects can deliver reliable, high-quality software capable of supporting NASA’s mission objectives. This guidance provides tools and techniques for effectively managing software testing in small projects, balancing practicality with compliance to standards ([SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations), [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements)).

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-047)

  ["Recommended Approach to Software Development,"](http://everyspec.com/NASA/NASA-GSFC/GSFC-General/SEL-81-305_REV-3_2419/ "Click to open in new window")

  SEL-81-305, Revision 3, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1992.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-209)

  [IEEE Standard for System, Software, and Hardware Verification, and Validation](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8055462 "Click to open in new window")

  IEEE Computer Society, IEEE Std 1012-2016 (Revision of IEEE Std 1012-2012), Published September 29, 2017,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards. Non-NASA users may purchase the document from: http://standards.ieee.org/findstds/standard/1012-2012.html
* (SWEREF-224)

  [IEEE Computer Society, "Systems and software engineering - Software life cycle processes,"](http://standards.ieee.org/findstds/standard/12207-2008.html "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. See Key section: Software Integration Process, Software Qualification Testing Process, Software Verification Process. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-337)

  [Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf "Click to open in new window")

  Souppaya, Murugiah, Scarfone, Karen, NIST Special Publication NIST SP 800-40r4, April, 2022
* (SWEREF-548)

  [Flight Software Reviews](https://llis.nasa.gov/lesson/1294 "Click to open in new window")

  Public Lessons Learned Entry: 1294.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned Database highlights a critical insight in **Lesson Number 1294**:

> "Rigorous peer reviews of spacecraft bus software resulted in good on-orbit performance. A lack of rigorous peer reviews of instrument software has resulted in numerous on-orbit patches and changes."

This lesson underscores the necessity of **rigorous peer reviews of test results** to ensure the robustness and reliability of software. The distinction between spacecraft bus software (where peer review contributed to good performance) and instrument software (where inadequate reviews led to issues) highlights the variable outcomes based on how well verification efforts are performed pre-deployment. It serves as a cautionary example of the importance of early defect detection and the role of peer reviews in mitigating costly, complex, and risky post-deployment fixes.

### Key Enhancements and Expanded Lessons for Testing and Peer Review

#### **1. The Value of Peer Reviews for Flight Software**

**Peer Review Enhances Defect Detection**:

* + - Peer reviews allow for multiple perspectives when analyzing test results, improving the likelihood of detecting subtle or hidden defects before integration, launch, or deployment.
    - Rigorous peer reviews of spacecraft bus software test results in the documented example contributed directly to stable on-orbit performance, avoiding costly and complex post-launch mitigations.

**Instruments at Greater Risk Without Rigorous Testing**:

* + - Instrument software often deals with specialized functionalities and interactions with payload hardware, which may not receive equal attention or review rigor. As documented, insufficient peer reviews of instrument software led to unexpected on-orbit issues, requiring numerous patches and updates—introducing risks, additional costs, and operational inefficiencies.

#### **2. Best Practices for Peer Reviewing Test Results in Flight Software**

1. 1. **Institutionalize Peer Reviews Across Subsystems:**

      * Ensure peer reviews are conducted not just for spacecraft bus software, but for all critical software components (e.g., instruments, payload systems, peripheral controllers, etc.).
      * Apply the same level of rigor to both core infrastructure and auxiliary software, regardless of perceived criticality.
   2. **Standardize Peer Review Processes:**

      * Develop checklists tailored to the functional domain of the software being tested, ensuring a consistent review framework.
      * Use the checklists to verify:
        + Completeness and accuracy of the test results.
        + Correct association of test results with requirements.
        + Adequacy of defect resolution for any issues detected in earlier phases.
        + Testing coverage, particularly for edge cases and failure scenarios.
   3. **Include Multidisciplinary Reviewers:**

      * Include team members with diverse expertise (e.g., domain experts, Software Assurance, Independent Verification and Validation [IV&V] personnel) who can scrutinize the specific context of the software.
      * Ensure at least one reviewer understands mission-level and subsystem-level requirements for the functional area under review.
   4. **Integrate Peer Reviews with Test Readiness Milestones:**

      * Schedule peer reviews of test results as an integral part of the major project reviews, such as:
        + Test Readiness Reviews (TRRs)
        + Flight Readiness Reviews (FRRs)
        + Post-Test Reviews (PTRs)
      * Test failures, discrepancies, and issues must be reviewed to determine whether they:
        + Require additional testing or fixes.
        + Impact other areas of the software or system.
        + Justify a re-definition of pass/fail criteria for affected tests.

#### **3. Expanding Lessons for Testing and Peer Review of Flight Software**

**Lesson 1: "Equally Rigorous Reviews Yield Equal Reliability Across Subsystems"**

* + - Observation: Disparities in peer review practice lead to inconsistent results: spacecraft bus software exhibited fewer problems due to rigorous reviews, while instrument software suffered from costly post-deployment issues due to lack of thorough review.
    - Remedy: Ensure all subsystems—both core and auxiliary—undergo the same rigorous review processes. Subsystems perceived as secondary may still experience critical failures that impact the mission as a whole.
    - Example: For instrument software, include experts in payload operations to review both test cases and results for adequacy.

**Lesson 2: "Peer Reviews Reduce Risk for On-Orbit Recovery"**

* + - Observation: On-orbit patches may resolve problems but often introduce secondary risks (e.g., operational downtime, new software defects).
    - Remedy: Rigorous peer review of testing results reduces the likelihood of needing risky on-orbit software adjustments by catching potential issues earlier in the lifecycle.
    - Example: The International Space Station's reliance on software updates during operational missions illustrates both the capabilities and dangers of on-orbit patching, highlighting the need for flawless execution in the pre-launch phases.

**Lesson 3: "High-Fidelity Simulations Enhance Test Evaluations"**

* + - Observation: Even thorough peer reviews may fail to catch issues if the test environment doesn't accurately reflect real-world conditions. Low-fidelity simulations or incomplete test setups may yield incomplete insights into software behavior.
    - Remedy: Prioritize high-fidelity simulations in tandem with peer reviews (see [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations)). Ensure peer reviewers assess the adequacy of the simulation environment and its ability to replicate operational scenarios.
    - Example: A mission that uses hardware-in-the-loop (HIL) simulations combined with peer-reviewed test analyses encounters fewer unexpected issues during deployment.

**Lesson 4: "Peer Reviews Ensure Coverage Completeness"**

* + - Observation: Test result peer reviews surface discrepancies in coverage, ensuring all requirements—particularly safety-critical and high-risk items—are tested adequately.
    - Remedy: Use traceability matrices during peer reviews to link test results to requirements, verifying that the testing thoroughly covers all critical functionality.
    - Example: For safety-critical software, reviewers should verify that testing includes boundary conditions, failover scenarios, and interactions with hardware components.

#### **4. Peer Review Benefits Highlighted by the Lesson**

* + **Improved Defect Detection**: Early identification of errors during peer review reduces the likelihood of expensive and schedule-impacting errors found in later stages (e.g., post-launch).
  + **Increased Test Result Credibility**: Peer reviews ensure transparency and foster confidence in test results, especially for safety-critical or high-priority systems.
  + **Reduction in Post-Deployment Risks**: Rigorous pre-emptive reviews reduce the likelihood of on-orbit patches, where corrective actions are costlier and introduce operational risk.

### Related NASA Lessons Learned

1. **Lesson Number 0721: Test as You Fly**:

   * Testing in an operationally relevant environment reduces surprises during on-orbit operations.
   * Peer reviews should include validation of environmental realism during testing.
2. **Lesson Number 1258: Software Verification and Validation**:

   * Emphasizes using strong V&V processes, along with independent assessments, to confirm software reliability.
   * Incorporating this into peer reviews of test results ensures alignment with best practices.
3. **Lesson Number 1038: Software Costs and Risks Mitigation**:

   * Documenting and reviewing test strategies reduces software risks and allows for early course corrections.

### Conclusion

Lesson 1294 serves as a compelling example of the value of conducting **rigorous peer reviews of software test results** to ensure mission success. Whether for spacecraft bus software or instrument software, thorough peer reviews highlight gaps in test coverage, improve defect detection, and reduce the risk of costly post-deployment patches. By institutionalizing these practices, teams can enhance the reliability, safety, and performance of software systems across all NASA missions.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Going Beyond the Formal Qualification Test (FQT) Scripts: Data Reduction/Automation](https://software.gsfc.nasa.gov/lesson-details/295/). **Lesson Number 295**: The recommendation states: "As early as feasible in the program (pre-FQT time frame), ascertain whether automated testing is planned for Software FQT and ensure that the vendor will provide all relevant test articles well in advance of test run-for-record (will likely require NASA Program Management buy in and support as well). Identify any calls to open up additional views to EGSE, Simulators, raw hex dumps, etc., that may be used to assist with data analysis/processing/reduction in the scripts. Request clarification on how data captured in those views will be used and have snapshots provided (or travel to vendor site) to fully understand verification extent. For automated testing, the Software Systems Engineer should evaluate whether the provider has allocated sufficient time and training to fully understand how the automated testing program will exercise and verify all required functions and behaviors. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
* [Detailed timing measurements are needed to verify timing requirements](https://software.gsfc.nasa.gov/lesson-details/302/). **Lesson Number 302**: The recommendation states: "Systems with timing requirements by definition need to prove that the timing requirements are met.  The software development team will need a means to capture and interpret the system timing.  This may include using a system tool, a real time operating system tool, CFE timing tool, or external pins captured by a logic analyzer.  Take this need into account when planning the lab setup, as purchases will likely be required."

# 7. Software Assurance

**SWE-068 - Evaluate Test Results**

4.5.5 The project manager shall evaluate test results and record the evaluation.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that test results are assessed and recorded. 

2. Confirm that the project documents software non-conformances in a tracking system.

3. Confirm that test results are sufficient verification artifacts for the hazard reports.

## 7.2 Software Assurance Products

This requirement emphasizes the critical role of Software Assurance (SA) in assessing and verifying the completeness, correctness, and adequacy of software testing as it pertains to hazard reports. Key SA products ensure that software hazard controls have been thoroughly verified at all stages of the software development and testing lifecycle, with a focus on hazard mitigation, safety-critical requirements, and operational assurance.

#### **Key SA Products Include:**

1. **Software Test Reports**:

   * Test reports should provide detailed analysis of test results, focusing on software hazard control verifications included in hazard reports.
   * SA must confirm that the test reports fully document discrepancies, include pass/fail criteria for hazard controls, and establish traceability to safety-critical test requirements.
   * These reports must cover all test cases, including nominal, off-nominal, load, and stress tests related to identified hazards.
2. **Software Problem Report or Defect Data**:

   * Non-conformances (e.g., defects, problems, or discrepancies identified during testing) must be thoroughly captured and analyzed.
   * SA will verify that defects affecting safety-critical functionality are classified by severity, resolve the root cause of detected issues, and track corrective actions in the project’s problem-tracking system.
   * Open issues must be tracked to closure, with clear evidence that resolutions have been verified through re-testing.
3. **Software Test Coverage Metric Data**:

   * Test coverage metrics must demonstrate the adequacy of testing across all safety-critical and hazard-related requirements.
   * Examples of metrics to evaluate include code coverage (e.g., statement, branch, decision), functional coverage for hazard control requirements, and test case execution completion rate.
   * SA ensures that gaps in test coverage for hazard-related scenarios are identified and addressed.

## 7.3 Metrics for Monitoring Software Assurance Objectives

Tracking metrics is essential for SA to ensure hazard controls and safety-critical requirements have been adequately tested and verified. Recommended metrics for evaluating SA objectives include:

#### **Testing Metrics**:

1. **Non-Conformances by Lifecycle Phase**:
   * The number of non-conformances detected, categorized by each lifecycle phase (e.g., requirements, design, coding, integration, testing).
   * Trends over time to identify phases where issues are introduced most frequently.
2. **Safety-Related Non-Conformances**:
   * Count of non-conformances associated with safety-critical functions or requirements to track and mitigate risks.
3. **Open vs. Closed Non-Conformances**:
   * Number of unresolved (open) versus resolved (closed) non-conformances, tracked by severity and time open.
4. **Testing Completion Rate**:
   * Number of tests executed vs. total planned tests.
   * Number of tests completed vs. test results evaluated and signed off by SA.
5. **Hazard Verification Metrics**:
   * Number of hazards containing software that have been tested vs. total hazards identified.
   * Number of hazard test procedures/reports completed vs. total planned, tracked over time.
6. **Safety-Critical Requirement Verification**:
   * Number of safety-critical verifications completed compared to the total number of safety-critical verifications required.
7. **Metrics on Hazard Controls**:
   * Number of non-conformances identified while validating that hazard controls are verified through test plans/procedures/test cases.
8. **SA Involvement Metrics**:
   * Number of safety-critical tests executed vs. the number of safety-critical tests witnessed or reviewed by SA.

#### **Non-Conformance Trends**:

* Total number of non-conformances (open, closed, by severity).
* Number of non-conformances per testing phase (e.g., unit, integration, system, validation).
* Count and severity of non-conformances associated with hazard controls over time.

## 7.4 Guidance: SA Review of Hazard Verification Testing

1. **Reviewing Test Reports**Software Assurance must:
   * **Assess Accuracy of Test Reports**:
     + Review all software test reports to ensure results are complete, accurate, and traceable to both requirements and hazard control verifications.
     + Verify that the test report identifies any **discrepancies or non-conformances**, with clear descriptions of their nature, locations, and severity.
   * **Trace Test Results to Requirements**:
     + Ensure every discrepancy is documented in the problem-tracking tool, and verify the traceability of test results to safety-critical and hazard-related requirements.
   * **Confirm Resolution of Issues**:
     + All discrepancies, defects, or non-conformances must be resolved (or safety mitigations adequately implemented) before SA signs off on the test completion.
2. **Hazard Reports and Safety Verification**  
   SA plays a critical role in verifying that all hazard controls listed in Hazard Reports or Safety Packages are adequately tested. This includes:
   * **Ensuring Test Completeness**:
     + Confirm that all software safety-related verifications identified in the hazard report have been thoroughly tested, including tests specified in safety plans, test plans, and test procedures.
     + Verifications must encompass:
       - **Nominal cases**: Safe and correct functionality under all standard operating conditions.
       - **Off-Nominal Cases**: Software's ability to handle unexpected inputs or failure modes gracefully (e.g., by initiating fail-safe actions, fault detection, or management of edge cases).
     + Hazard mitigation tests must include behavior under:
       - **Load and Stress Conditions**: Validate software’s ability to perform under maximum load or resource-constrained conditions (e.g., high CPU or memory usage).
       - **Boundary Conditions:** Ensure proper handling of edge cases or operational boundary conditions in known and unforeseen scenarios.
       - **Mode and State Transitions**: Verify the proper operation of hazard mitigations in all software modes and states.
   * **Testing for Safe State Transition**:
     + Confirm that tests demonstrate the software can detect hazards, take appropriate actions, and transition the system to a safe state.
3. **Handling Non-Conformances**
   * **Non-Conformance Identification**:
     + Validate that every discrepancy, anomaly, or error during testing is captured, categorized by severity, and documented within the project’s issue-tracking system.
     + Each non-conformance must be addressed with corrective actions, and its resolution must be verified via re-testing.
   * **Resolution Before Hazard Verification Closure**:
     + SA must confirm that all outstanding issues and failures related to a hazard control are fully resolved before the hazard verification can be considered complete.

This guidance ensures that **Software Assurance Products** related to hazard assessment and testing rigorously verify that hazard controls and safety-critical requirements are tested, well-documented, and resolved in compliance with project safety standards. By tracking metrics, monitoring discrepancies, and verifying hazard mitigation, Software Assurance successfully manages risks, enhances reliability, and ensures that hazard-related issues are identified and resolved before deployment.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) for comprehensive metrics for monitoring SA activities.

See also Topic Topic [8.57 - Testing Analysis by SA](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) for detailed guidance on analyzing test results and supporting corrective actions.

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) and NASA-STD-8739.8: Software Fault Tolerance Testing.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action),      * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

# 8. Objective Evidence

Objective Evidence

Objective evidence refers to documented records or artifacts that demonstrate compliance with a requirement or process, in this case, the adequacy of software assurance (SA) efforts in verifying hazard-related software. Below is a categorized list of tangible deliverables that provide proof that SA activities were conducted, hazard controls were verified, and all related discrepancies have been resolved.

---

### **1. Evidence of Test Planning and Procedures**

**Artifacts:**

1. **Test Plan Documentation**:
   * The project’s approved Software Test Plan outlining:
     + Strategies for testing hazard controls and safety-critical software.
     + Risk assessment for hazard-related test cases.
     + Testing schedules, resources, and roles (including SA involvement).
2. **Test Procedures**:
   * Detailed procedures for verifying hazard controls, including:
     + Each test case, test scenario, and hazard-related requirement verification.
     + Test configurations (e.g., hardware platforms, software builds, simulations).
     + Steps for executing functional, stress, boundary, fault-tolerance, recovery, and load testing.
3. **Hazard Test Planning Artifacts**:
   * Hazard-specific test plans that include the mapping of each hazard report hazard control to corresponding test cases.
   * Traceability matrices or tools showing linkage between:
     + Safety-critical requirements → Hazard Report hazard controls → Test procedures.

---

### **2. Evidence of Testing Execution**

**Artifacts:**

1. **Test Execution Logs**:
   * Execution logs that include test IDs, timestamps, results (pass/fail), and detailed logging of system responses during test cases related to hazard verifications.
   * Listings for nominal, off-nominal, and stress-related scenarios.
2. **Test Artifacts for Safety Controls**:
   * Test results for safety-critical controls and hazard mitigations demonstrating:
     + The ability to transition to a safe state in failure scenarios.
     + Handling of operational stress conditions, high loads, or edge-case inputs.
3. **High-Fidelity Simulation Logs**:
   * Records of hardware-in-the-loop (HIL) tests, platform simulations, or other high-fidelity test articles demonstrating hazard control testing.
   * Evidence of the test environment's alignment with mission/operational scenarios (per [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations)).

---

### **3. Evidence of Testing Results and Analysis**

**Artifacts:**

1. **Software Test Reports (STRs)**:
   * Comprehensive reports documenting the results of executed test cases, including:
     + Hazard-related test case results with pass/fail status.
     + Analysis of test coverage for safety-critical and hazard-related requirements.
     + Any discrepancies or deviations from expected results.
2. **Test Coverage Reports**:
   * Metrics and evidence demonstrating the extent of test coverage, specifically:
     + Code coverage data (e.g., statement, branch, decision) for software elements tied to hazard mitigations.
     + Functional coverage metrics showing the percentage of hazard control requirements verified.
3. **Discrepancy or Test Failure Logs**:
   * Logs of test failures or non-conformances identified during the test campaign.
   * Documented root causes, corrective actions, and retesting results to verify resolution.

---

### **4. Evidence of Defect Tracking and Resolution**

**Artifacts:**

1. **Non-Conformance/Problem Reports**:

   * Formal records of all discrepancies, defects, or anomalies identified during hazard testing.
   * Evidence of proper classification, risk assessment, and prioritization based on the impact of the issue.
2. **Defect Tracking Database/Logs**:

   * A defect tracking tool or log detailing:
     + The status of non-conformances (open/closed/days open).
     + Cross-references to test cases and actual hazard controls.
     + Approvals and verification sign-offs for resolutions.
   * Specific tracking of safety-related and hazard-associated non-conformances.
3. **Anomaly Reports and Dispositions**:

   * Reports documenting test anomalies, including their analysis and disposition outcomes.
   * Evidence of corrective actions applied for safety-critical software discrepancies.
4. **Re-Test Evidence**:

   * Results of re-tests conducted to confirm that corrective actions resolved safety-critical issues.
   * Approvals from SA personnel confirming successful resolution.

---

### **5. Evidence of Verification Adequacy and SA Sign-Off**

**Artifacts:**

1. **Hazard Traceability Evidence**:

   * Completed traceability matrix or database showing:
     + All hazard controls verified, corresponding test procedures, results, and discrepancies resolved.
   * Confirmation that all hazard-related requirements were verified (nominal and off-nominal cases).
2. **Hazard Closure Evidence**:

   * Reports documenting the closure of hazards, signed off by SA, confirming:
     + All safety controls for the hazard have been fully tested, verified, and meet requirements.
     + Any non-conformances have been adequately addressed.
3. **Test Completion Sign-Off**:

   * Records of SA personnel sign-off on all test-related artifacts, including:
     + Test procedures used for hazard verifications.
     + Test results for safety-critical mitigations corroborated by SA validation.
     + Test execution, coverage, and effective defect resolutions.
4. **Safety Control Verification Records**:

   * Records demonstrating that all safety-critical requirements and hazard mitigations have been successfully executed, validated under operational scenarios, and signed off by SA.

---

### **6. Evidence of Metrics Monitoring & Continuous Assurance**

**Artifacts:**

1. **SA-Captured Metrics**:
   * Quantitative metrics that demonstrate test progress, such as:
     + Test execution (e.g., tests completed vs. total tests planned).
     + Reduction in open non-conformances over time.
     + Hazard tests completed vs. total hazard tests planned.
     + Control effectiveness from test reports (e.g., ability to detect/mitigate faults).
2. **SA Dashboards or Progress Summaries**:
   * Reports or dashboards summarizing test progress and completion of hazard verifications, including:
     + Open vs. closed safety-related non-conformances.
     + Completion percentages for test case execution and hazard verification.
3. **Discrepancy Trends and Reports**:
   * Trends showing non-conformance reduction across lifecycle phases and testing iterations.

---

### **7. Evidence of Peer Review and Oversight**

**Artifacts:**

1. **Peer Review Records**:
   * Evidence that SA conducted structured peer reviews of the test documents and results, with sign-offs and corrective feedback.
   * Reviewer comments or minutes from peer review sessions assessing test adequacy.
2. **IV&V Confirmation (if applicable)**:
   * Validation records from Independent Verification and Validation (IV&V) teams confirming that hazard verifications were conducted appropriately.

---

### **Conclusion**

The artifacts outlined above provide robust, tangible evidence of compliance with the requirement to assess verification adequacy for hazard reports. By meticulously documenting test planning, execution, results, and discrepancy resolutions, and by monitoring metrics and traceability, SA aligns these deliverables with NASA’s rigorous standards for safety-critical software development and assurance. These products ensure stakeholder confidence in verifying all hazard-related requirements and controls effectively.

Definition of objective evidence

Objective evidence is an unbiased, documented fact showing that an activity was confirmed or performed by the software assurance/safety person(s). The evidence for confirmation of the activity can take any number of different forms, depending on the activity in the task. Examples are:

* Observations, findings, issues, risks found by the SA/safety person and may be expressed in an audit or checklist record, email, memo or entry into a tracking system (e.g. Risk Log).
* Meeting minutes with attendance lists or SA meeting notes or assessments of the activities and recorded in the project repository.
* Status report, email or memo containing statements that confirmation has been performed with date (a checklist of confirmations could be used to record when each confirmation has been done!).
* Signatures on SA reviewed or witnessed products or activities, or
* Status report, email or memo containing a short summary of information gained by performing the activity. Some examples of using a “short summary” as objective evidence of a confirmation are:
  + To confirm that: “IV&V Program Execution exists”, the summary might be: IV&V Plan is in draft state. It is expected to be complete by (some date).
  + To confirm that: “Traceability between software requirements and hazards with SW contributions exists”, the summary might be x% of the hazards with software contributions are traced to the requirements.
* The specific products listed in the Introduction of 8.16 are also objective evidence as well as the examples listed above.
