# SWE-190 - Verify Code Coverage

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695525. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage

SWE-190 - Verify Code Coverage

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695525)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695525&showCommentArea=true&showComments=true#addcomment)

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

4.5.10 The project manager shall verify code coverage is measured by analysis of the results of the execution of tests.

## 1.1 Notes

If it can be justified that the required percentage cannot be achieved by test execution, the analysis, inspection, or review of design can be applied to the non-covered code. The goal of the complementary analysis is to assess that the non-covered code behavior is as expected.

This requirement can be met by running unit, integration, and validation tests; measuring the code coverage; and achieving the code coverage by additional (requirement based) tests, inspection, or analysis. (For more guidance in using test coverage to improve the code, see Tab 3 of SWE-190 in the Software Engineering Handbook (NASA-HDBK-2203)).

The code coverage data and any rationale for uncovered code should be presented and reviewed at major project milestones. 

## 1.2 History

Click here to view the history of this requirement: SWE-190 History

SWE-190 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.5.10 The project manager shall verify code coverage is measured by analysis of the results of the execution of tests. |
| Difference between C and D | No change |
| D | 4.5.10 The project manager shall verify code coverage is measured by analysis of the results of the execution of tests. |

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

Code coverage helps to identify which lines of source code have been tested and which lines of your source code have not been tested and to provide data showing the completeness of the executed software tests. This helps to identify what areas of the code are needed and what areas may not be needed or are only used in specific scenarios. Code coverage can provide a profile of what software gets tested the most and the metrics can help guide where more involved or rigorous testing needs to occur, potentially at other levels of the system. 

This requirement mandates that the project manager ensures code coverage measurements are verified, tracked, and analyzed based on executed tests. Code coverage analysis is critical for validating that the software has been thoroughly exercised under testing conditions, especially for safety-critical and mission-critical systems. This process ensures the reliability, robustness, and correctness of the software, uncovering potential risks and gaps in testing that could lead to failures during operation.

---

### **Key Reasons for the Requirement**

#### **1. Validation of Test Completeness**

* Code coverage analysis provides quantitative proof of the effectiveness and completeness of the test suite:
  + It shows which parts of the code have been executed during tests and identifies untested areas.
  + Without this verification, there is no way to reliably determine whether testing has adequately exercised the codebase.

#### **2. Identification of Untested or Unreachable Code**

* Measuring code coverage is essential to identify:
  + Critical areas of the code that are untested (e.g., decision branches or fault-handling logic).
  + Dead or unreachable code that may be unnecessary and require refactoring.
* This helps focus testing efforts on eliminating gaps in safety-critical or high-risk areas.

#### **3. Support for Risk Management**

* Uncovered code presents potential risks to software correctness and performance:
  + If critical code paths are not exercised, latent defects may persist and lead to system failures during operation.
  + By analyzing coverage results, the project manager ensures appropriate risk mitigation measures are applied, including adding tests, improving test coverage, or refactoring redundant/dead code.
* For safety-critical software (Class A/B), achieving 100% coverage minimizes risk by ensuring all code paths are verified.

#### **4. Ensuring Compliance with Software Classification Requirements**

* Code coverage requirements vary depending on the software classification (e.g., Class A, B, C, D), but all classifications require coverage to be measured and tracked:
  + Class A/B systems demand 100% coverage of safety-critical components (MC/DC for decision logic, as applicable).
  + Class C/D may use aligned metrics with agreed-upon thresholds.
* Measuring coverage ensures the project adheres to NASA's standards for software development and assurance (e.g., SWE-190).

#### **5. Supporting Decision-Making for Code Changes**

* Coverage metrics help the project manager make informed decisions about further testing, code modifications, or acceptance criteria:
  + If tests consistently miss key code paths, the coverage results may prompt investigations into design or implementation changes.
  + Achieving acceptable coverage thresholds provides confidence in the software's readiness for deployment.

---

### **Benefits of Verifying Code Coverage Measurement**

#### **Improved Software Quality**

* Comprehensive testing guided by coverage metrics ensures the software performs as intended under all required conditions and edge cases.

#### **Early Defect Detection**

* Coverage analysis identifies areas of code that are prone to defects because they remain untested or are sparsely tested, allowing for proactive remediation.

#### **Safety and Mission Success**

* Prevents failures in critical mission operations by verifying that core functionality and fault management logic are fully exercised and validated.

#### **Transparency and Accountability**

* The inclusion of code coverage analysis in project reporting (e.g., test readiness and assurance reviews) provides confidence to stakeholders and aligns with NASA’s emphasis on rigorous software assurance practices.

#### **Efficient Use of Resources**

* Coverage analysis prioritizes testing efforts by focusing on high-risk, untested areas, reducing wasteful retesting of already well-tested sections.

---

### **How the Requirement Supports NASA Projects**

#### **Safety-Critical Software**

In the context of NASA's safety-critical software (e.g., Class A/B systems for spacecraft, life-support systems):

* Measuring and analyzing code coverage ensures **100% verification of critical code paths**, particularly for:
  + Decision logic.
  + Fault protection.
  + Error handling during off-nominal conditions.
* Uncovered code in safety-critical systems could lead to catastrophic failures, jeopardizing mission success and/or human life.

#### **Mission-Critical Software**

For mission-critical software (e.g., Class B systems managing science data, navigation):

* Code coverage ensures all mission-impacting workflows are tested to meet reliability and performance expectations.

#### **Non-Critical Software**

For Class C/D software, coverage measurement helps to:

* Provide visibility into the adequacy of testing while ensuring resources are allocated efficiently.
* Align uncovered code analysis and testing priorities with project risk posture.

---

### **Implementation of the Requirement**

To fulfill this requirement, the project manager should:

1. **Ensure Tools and Processes are in Place**:

   * Verify that code coverage measurement tools (e.g., JaCoCo, LCOV, BullseyeCoverage, SonarQube) are integrated into the testing environment and CI/CD pipeline.
   * Ensure measurement criteria (e.g., branch, statement, MC/DC) align with project classification.
2. **Review Coverage Metrics Frequently**:

   * Set milestones to analyze code coverage results (e.g., during unit testing, system testing, regression testing).
   * Use these results to evaluate testing adequacy or recommend new tests.
3. **Collaborate on Risk Analysis**:

   * Work with software assurance and engineering teams to assess risks associated with uncovered code. Work to address gaps or justify exclusions (e.g., dead code, deactivated code).
4. **Incorporate Coverage Results into Reporting**:

   * Include code coverage data in project reviews (e.g., Test Readiness Review (TRR), Software Acceptance Review (SAR)).
   * Use reports to support deployment decisions and demonstrate compliance with NASA standards.

---

### **Conclusion**

This requirement ensures that the **project manager actively monitors and verifies the adequacy of code coverage measurement** during testing. By analyzing coverage results, the project manager ensures that testing is comprehensive, gaps in coverage are addressed, risks are mitigated, and software meets the high standards necessary for mission safety and success.

# 3. Guidance

## 3.1 Test Coverage

#### **Purpose of Code Coverage**

Code coverage is a fundamental software engineering practice for enhancing software reliability and quality. It is a metric that determines which lines of code have been executed during testing ("covered") and highlights lines that remain untested. This insight allows teams to:

* Improve testing coverage by identifying untested areas.
* Ensure comprehensive validation of critical code paths.
* Maintain test quality throughout the software's lifecycle.

Code coverage measurement supports **risk reduction**, software correctness, and verification that the software performs as intended under all required conditions.

#### **Key Goals of Measuring Code Coverage**

* **Improve Testing Effectiveness**: Evaluate how thorough test suites are in exercising code functionality.
* **Generate Actionable Insights**: Pinpoint gaps in testing and allow teams to address those gaps (e.g., adding missing tests).
* **Ensure Software Safety and Reliability**: Verify that safety-critical and mission-critical software paths are exercised during testing to reduce risks of undetected errors.

#### **Why Code Coverage is Measured**

1. **Assess Testing Rigorousness**:
   * Understand whether tests adequately exercise the functionality of the code.
2. **Increase Test Completeness**:
   * Ensure coverage of unexpected failure/error paths and edge cases.
3. **Maintain Quality Over the Lifecycle**:
   * Continuously monitor code coverage during updates, modifications, regression testing, and maintenance activities.

Programs with **high test coverage** typically have fewer hidden bugs compared to programs with low test coverage, particularly for safety-critical software where errors could lead to catastrophic outcomes.

---

### **Uncovered Code Analysis**

If the project does not achieve 100% code coverage, the **uncovered code** must be classified and analyzed to mitigate risks. Common reasons for uncovered code and required actions include:

1. **Requirement Missing**:

   * The untested code fulfills an essential activity but lacks a corresponding requirement.
   * **Action**: Revise requirements documentation to reflect the activity and add tests to cover the code.
2. **Test Missing**:

   * The untested code corresponds to a requirement but lacks a test case.
   * **Action**: Create new test cases or fix gaps in the existing test suite to ensure coverage.
3. **Extraneous/Dead Code**:

   * The untested code does not trace to any requirements and serves no functional purpose.
   * **Action**: Remove redundant code; perform static analysis to locate other instances of dead code.
4. **Deactivated Code**:

   * The untested code serves a future configuration/scenario or aligns with system configurations not currently implemented.
   * **Action**: Document the inactive code and disable it to prevent accidental execution.

#### **Project Manager’s Role**

The project manager must ensure uncovered code is documented, analyzed for risk, and mapped to corrective actions. This analysis aids resource allocation for testing improvement and ensures compliance with safety and reliability standards.

---

## 3.2 Coverage Criteria

#### **Key Coverage Criteria for Code**

Coverage criteria define rules for measuring the extent to which the code is exercised during testing. These metrics help assess the thoroughness of testing and guide improvement efforts. Recommended coverage criteria include:

1. **Function Coverage**:

   * Verifies all functions or subroutines in the program have been called during testing.
2. **Statement Coverage**:

   * Determines whether every individual line of code (statement) has been executed.
3. **Branch Coverage**:

   * Verifies coverage of all branches within decision constructs (e.g., `if`, `case` statements). Ensures both true and false branches of Boolean expressions are tested.
4. **Edge Coverage**:

   * Ensures execution of all **edges** in the control flow graph of the program, capturing all transitions between nodes.
5. **Condition Coverage**:

   * Verifies all Boolean sub-expressions in conditional statements have been evaluated to both true and false.

#### **Software Class Targets**

Code coverage requirements vary based on software classification (aligned with SWE-190):

| **Coverage Criteria** | **Class A** | **Class B** | **Class C** | **Class D** |
| --- | --- | --- | --- | --- |
| **Statement Coverage** | 100% | 100% | AM | AM |
| **Decision Coverage** | 100% | 100% | AM | AM |
| **Modified Condition/Decision Coverage** | 100% | AM | AM | AM |

**Note:** "AM" indicates that coverage thresholds must be agreed upon and signed off by the **Center’s Engineering Technical Authority (TA)**.

---

## 3.3 Code Coverage Measurements

#### **Defining and Reporting Code Coverage**

* Code coverage measurements should be defined (**SWE-189**) and tracked across the lifecycle, including unit testing, integration testing, system testing, regression testing, and maintenance activities.
* Coverage analysis encompasses:
  1. Identifying untested areas of code.
  2. Developing additional test cases to improve coverage.
  3. Quantitatively evaluating coverage metrics as an indirect measure of software quality.

#### **Project Manager’s Role**

The project manager should verify code coverage measurements using testing logs, reports, and risk analysis artifacts. If coverage is insufficient, the **project manager's corrective actions** include addressing missing requirements/tests or justifying uncovered code through proper risk analysis.

---

## 3.4 Code Coverage Tools

#### **Tool Selection**

Code coverage measurement tools vary by programming language, and teams should select tools compatible with their development environment. Examples include:

* **Java**: JaCoCo, Clover.
* **C/C++**: LCOV, BullseyeCoverage.
* **Python**: Coverage.py.
* **C#**: dotCover.

#### **Tool Limitations**

While automated tools work well during component/unit testing, manual code coverage may be required for systems embedded in hardware, as tools may have limited ability to handle hardware-software integration.

#### **Integration into Lifecycle Artifacts**

Coverage metrics and goals should be specified in:

* **Software Development/Management Plan (SDMP):** Define coverage percentage goals for specific source code sections.
* **Software Test Plan (STP):** Include coverage metrics alongside test results, documenting untested lines and their rationale.

---

## 3.5 Systems in Operation and Maintenance

#### **Code Coverage During Modifications**

For systems in operation and maintenance:

* Modifications to the software must include a review of code coverage metrics to ensure no new untested code is introduced.
* Regression testing and requalification must include code coverage analysis to validate changes and ensure continued conformance with safety-critical standards.

---

### **Best Practices for Code Coverage**

1. **Set Realistic Goals**:

   * For safety-critical systems (Class A/B), aim for 100% code coverage, prioritizing structural and decision-based coverage (e.g., MC/DC).
   * For non-critical systems, coverage thresholds should be tailored to project risk levels and signed off by the Technical Authority.
2. **Measure and Monitor**:

   * Continuously measure coverage at all testing phases to identify test gaps.
   * Analyze configuration-specific code (e.g., libraries used conditionally) for coverage sufficiency.
3. **Collaborate and Communicate**:

   * Work with software assurance and testing teams to develop comprehensive coverage reports, highlighting risks and rationale for exceptions.
   * Communicate covered and uncovered areas to stakeholders regularly.
4. **Automate Coverage Analysis**:

   * Tools integrated into CI/CD pipelines can streamline coverage reporting and ensure consistency in measurement throughout the lifecycle.

---

### **Conclusion**

By measuring code coverage, addressing gaps, and tracking coverage metrics throughout development, testing, and maintenance phases, teams can achieve higher reliability, better safety compliance, and reduced defects. Integrating coverage guidance into lifecycle plans ensures projects remain aligned with NASA's software development and assurance standards.

See also Topic [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels), [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements), [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software), [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase), [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test), 

Within the [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan), define the code coverage metric to be used, and the metric goal percentage of the testing suite rigor.  Code coverage metrics and goals can differ for specific source code sections requiring more rigor.

Within the [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan), include the code coverage metrics as part of the test results.  The code coverage metrics should include a reason for the source code lines reported as not covered in testing.

See also [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis), [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software),

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

For small projects, the intensity and rigor applied to code coverage measurement can be tailored to the project's size, scope, available resources, and risk posture. While these projects may not have the same level of complexity as large-scale programs, a strategic approach to code coverage ensures that critical areas are tested thoroughly without overloading the team.

#### **Key Considerations for Small Projects:**

1. **Prioritize Core and Critical Code Coverage:**

   * Focus testing efforts on the **core functionality** of the software, ensuring key logic, decision points, and critical workflows have high coverage.
   * Decisions and error-handling code should be top priorities, as faults in these areas typically carry the most risk.
2. **Align Coverage with Project Risk Posture:**

   * The required percentage of code coverage should be based on the **safety, mission, and operational risks** posed by the software.
     + For high-risk projects (e.g., Class A/B), coverage should aim for 100% for critical sections of the code.
     + For lower-risk projects, the percentage can be lower, provided metrics and their rationale are formally assessed and documented.
3. **Leverage Static Analysis and Automation:**

   * Use **static analysis tools** (e.g., SonarQube, Coverity, Pylint) to identify untested code paths, dead code, and other gaps in the source code. These tools can also offer insights into coding quality and adherence to standards.
   * When integrated with **continuous integration (CI) pipelines**, static analysis tools can automatically analyze code coverage as part of the development process, reducing the manual overhead for the team.
   * This automation ensures timely feedback, saving resources and highlighting gaps during early phases of development.
4. **Document Untested Code:**

   * For any **untested code sections**, provide clear documentation detailing:
     + Whether the code is deactivated, unnecessary (e.g., unused legacy code), or impractical to test.
     + A **rationale** for not testing the specific area (e.g., configuration settings that will not execute in this deployment).
   * Ensure the project team, project manager, and stakeholder(s) **review and agree** to accept this approach to untested code.
5. **Focus on Impact and Efficiency:**

   * For small projects, avoid exhaustive testing of non-critical or rarely executed routines unless they significantly impact system safety or performance.
   * Allocate effort proportionally to the importance of the code (e.g., prioritize high-use paths, safety-critical components, and mission-specific functionality).

---

#### **Best Practices for Small Projects:**

1. **Define Minimum Code Coverage Targets at the Outset:**

   * Decide an appropriate coverage threshold that balances **project goals, available resources, and risk posture**.
   * Example tool-based goals for small projects:
     + **Core functionality** (decision points, critical algorithms): >90% statement and branch coverage.
     + **Non-safety-critical components**: 60%-80%, adjusted as necessary by the Center’s Technical Authority.
2. **Leverage Lightweight Tooling and Techniques:**

   * Choose tools that are simple to set up, use, and embed within the small project workflow. Tools that work with your project's development environment save time and prevent unnecessary maintenance overhead.
   * Conduct **peer reviews** or manual walk-throughs of untestable sections to identify risks or implementation flaws.
3. **Integrate Test Coverage Metrics into Regular Reports:**

   * Even for small projects, ensure periodic review of code coverage metrics during updates or milestones (e.g., code freeze, delivery deadlines, regression testing).
   * Use concise summaries to highlight uncovered areas and provide context.
4. **Balance Rigor with Realism:**

   * Align the rigor of code coverage analysis with the project's lifecycle stage and budget. Early-stage experimental projects may require less test coverage, while production-level or safety-relevant updates demand higher levels of rigor.
5. **Continuously Reassess Code Coverage Needs:**

   * As new features or changes are introduced, re-evaluate the code coverage targets and address uncovered code dynamically during maintenance and updates.

---

#### **Example Workflow for Small Projects**

1. **Set Coverage Goals Based on Risk:**

   * For critical code paths: Target >90%-100% coverage.
   * For non-critical paths or configurations: Align with an appropriate percentage and explicitly document gaps.
   * Confirm achievable goals with the Technical Authority for any deviations.
2. **Incorporate Automated Coverage Analysis:**

   * Integrate a simple static analysis tool into the CI pipeline to report coverage on each build.
   * Example tools: LCOV, Codecov, SonarQube, or tools specific to your favored language (e.g., Coverage.py for Python).
3. **Track and Report Regularly:**

   * Review code coverage metrics at key project checkpoints. Ensure all stakeholders understand any gaps and their associated risk.
4. **Document Untested Code with Rationale:**

   * Create and maintain a list or report of uncovered code sections along with justifications (e.g., dormant or unreachable code).
5. **Address Critical Gaps Prior to Delivery:**

   * Before deployment, re-prioritize efforts to maximize the coverage of high-risk and mission-critical areas.

---

#### **Example Documentation for Small Projects**

**Scenario:** A small project delivering telemetry data for a low-risk operation. Coverage needs to balance limited resources with ensuring core functionality.

* **Coverage Goal:**

  + 90% coverage for telemetry processing, decision points, and error handling.
  + 70% coverage for logging outputs (low priority).
* **Example Coverage Report Section:**

| **Module/File** | **Coverage (%)** | **Goal (%)** | **Notes/Rationale** |
| --- | --- | --- | --- |
| Telemetry.cpp | 95% | 90% | Fully tested. Test gaps cover extraneous logging. |
| Logging.cs | 65% | 70% | Low-risk. Uncovered code relates to rare debug paths. |
| Config.cfg | 45% | --- | Dynamic configuration settings unlikely to execute. |

* **Risk Management:**
  + Configuration scripts are untested but highly constrained to known responses.
  + Gaps in logging will not affect operational performance. Approved by Project Manager.

---

#### **Benefits of This Approach for Small Projects:**

1. **Efficient Resource Allocation:**

   * Focuses testing effort on the most critical parts of the code, avoiding wasted time on low-impact or unreachable code.
2. **Project Risk Awareness:**

   * Ensures that even minimal testing efforts are deliberate and aligned with the risk tolerance of the stakeholders.
3. **Time Savings Through Automation:**

   * Automated tools integrated into CI pipelines reduce manual analysis effort and enable prompt identification of gaps.
4. **Clear Communication:**

   * Documented rationale for untested code ensures all decisions are transparent and appropriately evaluated before the software is delivered.

---

This guidance ensures that small projects can apply code coverage practices effectively without being overburdened, while still meeting the quality, safety, and risk management expectations necessary for NASA projects. Regular monitoring, automation, and documented decisions provide an efficient yet rigorous approach to ensure reliable software delivery.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA's lessons learned database provides valuable insights into best practices, challenges, and recommendations that can inform the implementation of code coverage requirements for software development. Below are key lessons learned related to achieving and verifying code coverage:

---

### **1. Neglected Code Coverage Leads to Undetected Defects**

**Lesson Learned:**

* Projects that did not prioritize code coverage or relied on inadequate coverage metrics experienced critical software defects that were only detected late in the development cycle or during operations.
  + Example: A missing test path for a rarely executed fault-handling routine caused erroneous spacecraft behavior in an off-nominal condition.

**Recommendation:**

* Prioritize sufficient code coverage early in the lifecycle for **critical decision points**, fault-handling routines, and high-risk algorithms, even if the system is low complexity or designed for a narrow range of operations.

---

### **2. Overlooking MC/DC Coverage in Safety-Critical Systems**

**Lesson Learned:**

* For Class A and Class B software, reliance on basic coverage criteria (e.g., statement or branch coverage) resulted in inadequate testing for decision paths, especially where **high-complexity, multi-condition logic** was involved.
  + Example: Failure to achieve Modified Condition/Decision Coverage (MC/DC) in a safety-critical avionics system led to insufficient testing of decision-making algorithms, resulting in a corrective action delay of 6+ months for additional testing.

**Recommendation:**

* For software classification requiring MC/DC coverage (Classes A/B), ensure testing fully exercises all Boolean sub-expressions, particularly for critical logic paths and state transitions.

---

### **3. The "Illusion of Sufficient Coverage" in Embedded Systems**

**Lesson Learned:**

* In embedded systems, hardware-software integration often caused **coverage blind spots** where certain code paths were impossible to test due to hardware constraints, leading to latent defects.
  + Example: An embedded system for optical sensor readout failed during initial deployment due to an untested initialization sequence that was not detected in unit testing.

**Recommendation:**

* During testing of embedded systems, set realistic coverage goals while carefully analyzing uncovered paths. Use simulated environments or cross-compilation techniques to test hardware-dependent paths whenever practical.

---

### **4. Untracked Dead Code Introduces Risks**

**Lesson Learned:**

* Dead or extraneous code left untested and untracked caused software defects during operations when unexpected conditions triggered those paths. This occurred because inactive code was not properly disabled or documented.
  + Example: Extraneous code in a dormant subsystem caused a memory corruption issue when inadvertently executed following system configuration changes.

**Recommendation:**

* Perform static analysis early and regularly during development to detect and remove dead code. For deactivated paths, thoroughly document their purpose and ensure they remain disabled in production builds.

---

### **5. Insufficient Code Coverage Documentation**

**Lesson Learned:**

* In multiple instances across small-to-medium scale projects, discrepancies in code coverage thresholds arose due to the failure to document uncovered code areas and their rationale.
  + Example: A Class C software project had untested paths that later became critical during adaptive reuse of the software, requiring unplanned re-engineering.

**Recommendation:**

* Even for small projects, provide detailed rationale for **untested code** sections, including risk analysis, justification, and plans for mitigation (if required). Ensure the rationale is reviewed and signed off by stakeholders before delivery.

---

### **6. Static Analysis Tools Increase Code Coverage Efficiency**

**Lesson Learned:**

* Projects that integrated static analysis tools in **continuous integration pipelines** consistently achieved better code coverage with fewer overlooked areas, while saving time during testing.
  + Example: A Class D software project for ground telemetry achieved reliable coverage by automating analysis using open-source tools integrated into its CI process.

**Recommendation:**

* Leverage static analysis tools early in the development cycle to identify gaps, dead code, and redundant logic. Automate testing within CI/CD pipelines to make coverage tracking cost-effective.

---

### **7. Lack of Coverage Metrics Led to Poor Regression Testing**

**Lesson Learned:**

* Projects that did not monitor or retain code coverage metrics struggled to maintain testing quality during regression testing, introducing risks after later software modifications.
  + Example: A regression test suite failed to re-test certain paths in command sequences, leading to command errors during operations.

**Recommendation:**

* Track code coverage metrics throughout development and use them as part of regression testing workflows to ensure paths impacted by software updates are re-tested.

---

### **8. Tailoring Coverage Goals to Project Risk Improves Resource Allocation**

**Lesson Learned:**

* Small projects with limited resources often inefficiently focused on exhaustive coverage of low-risk components, leaving insufficient effort for exercising critical code paths.
  + Example: A modest Class C project spent significant effort testing passive functionality, while critical state transitions and failure conditions had partial coverage, leading to NASA Technical Authority intervention.

**Recommendation:**

* Align code coverage rigor with the **risk posture** of the project:
  + **High-risk components** should receive close to 100% testing coverage (e.g., decision logic, critical algorithms).
  + **Low-risk components** can have agreed-upon thresholds with the Technical Authority.

---

### **9. Unclear Responsibility for Measuring Code Coverage**

**Lesson Learned:**

* Instances arose where unclear roles in measuring and analyzing code coverage resulted in gaps in testing and inconsistent reporting.
  + Example: A Class B software project had unexplored code paths because software assurance personnel were not directly involved in validating coverage metrics or test adequacy.

**Recommendation:**

* Clearly define and assign responsibility for:
  + Collecting code coverage metrics.
  + Ensuring coverage thresholds are met.
  + Conducting risk analysis and rationale for untested code areas.

The roles should be documented and reviewed during major project milestones.

---

### **10. Code Coverage Reporting Enhances Project Transparency**

**Lesson Learned:**

* Projects that failed to report detailed coverage metrics in design reviews, test readiness reviews (TRRs), and software acceptance reviews (SARs) faced delays due to stakeholder concerns over testing adequacy.
  + Example: A Class B mission project encountered sign-off delays due to insufficient visibility into code coverage metrics for fault-handling routines.

**Recommendation:**

* Incorporate code coverage metrics into regular reviews and reports, such as Test Readiness Reviews (TRRs) and Software Acceptance Reviews (SARs). Provide stakeholders visibility into uncovered code areas alongside risk analysis and justification.

---

### **11. Continuous Code Coverage Monitoring Prevents Late-Stage Risks**

**Lesson Learned:**

* Inadequate tracking and reassessment of code coverage during updates introduced latent defects late in the project lifecycle.
  + Example: A project operating under maintenance ignored code coverage for new features, causing a data processing error during operations after an untested path was introduced.

**Recommendation:**

* For systems in **operation and maintenance**, ensure all software modifications undergo reassessment of coverage metrics. Include regression testing to prevent untested paths from becoming operational risks.

---

### **Lessons Learned Summary**

NASA's success and challenges with code coverage highlight critical practices:

1. Ensure **sufficient coverage** for critical and safety-relevant components.
2. Tailor coverage rigor to **project risk posture**.
3. Use **static analysis tools and automation** to improve efficiency.
4. Document and analyze **untested code** for transparency and risk management.
5. Continuously monitor coverage metrics during **maintenance** and updates.

Incorporating these lessons ensures software quality, safety, and compliance with NASA's standards and objectives, while avoiding costly errors or delays associated with insufficient testing coverage.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Going Beyond the Formal Qualification Test (FQT) Scripts: Data Reduction/Automation](https://software.gsfc.nasa.gov/lesson-details/295/). **Lesson Number 295**: The recommendation states: "As early as feasible in the program (pre-FQT time frame), ascertain whether automated testing is planned for Software FQT and ensure that the vendor will provide all relevant test articles well in advance of test run-for-record (will likely require NASA Program Management buy in and support as well). Identify any calls to open up additional views to EGSE, Simulators, raw hex dumps, etc., that may be used to assist with data analysis/processing/reduction in the scripts. Request clarification on how data captured in those views will be used and have snapshots provided (or travel to vendor site) to fully understand verification extent. For automated testing, the Software Systems Engineer should evaluate whether the provider has allocated sufficient time and training to fully understand how the automated testing program will exercise and verify all required functions and behaviors. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
* [Remove Debug Settings and Code Prior to Benchmarking](https://software.gsfc.nasa.gov/lesson-details/338/). **Lesson Number 338**: The recommendation states: "Remove or disable debug code and settings before benchmarking to ensure that timing numbers are accurate."

# 7. Software Assurance

**SWE-190 - Verify Code Coverage**

4.5.10 The project manager shall verify code coverage is measured by analysis of the results of the execution of tests.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project performs code coverage analysis using the results of the tests or a code coverage tool. 

2. Analyze the code coverage measurements to identify uncovered software code.

3. Assess any uncovered software code for potential risk, issues, or findings.

## 7.2 Software Assurance Products

### **7.2 Software Assurance Products**

#### **SA Risk Analysis and Rationale for Uncovered Code**

Software assurance (SA) plays a critical role in analyzing, documenting, and mitigating risks associated with uncovered software code. When code coverage is less than 100%, it is imperative that SA provides a comprehensive analysis of the uncovered code and communicates the rationale for any acceptance of uncovered portions. This includes:

1. **Assessment of Uncovered Code:**
   * Analyze code coverage data to identify uncovered code.
   * Categorize uncovered code (e.g., missing requirements, missing tests, extraneous code, deactivated code).
2. **Risk Analysis and Mitigation:**
   * Collaborate with engineering to assess the risks associated with uncovered areas.
   * Document the rationale for allowing uncovered code (if applicable), including operational impacts, risks, and proposed mitigations.
3. **Action Plan for Risk Reduction:**
   * Recommend corrective actions (e.g., additional tests, requirements definition, or code removal if extraneous).
   * Ensure that project management agrees to and signs off on decisions.

Deliverables should include:

* A **Risk Assessment Report** detailing the uncovered code, its justification, associated risks, and mitigation strategies.
* Transparency through logs/reports that track code coverage changes over time.

---

#### **Verification and Results Analysis**

SA must verify the accuracy of code coverage measurements and ensure the project is following the necessary processes:

* **Verification of Coverage Metrics:**
  + Confirm that code coverage metrics are selected, implemented, tracked, and reported across the software lifecycle.
  + Use random spot checks to ensure accuracy (e.g., verify traceability from test cases to code via a requirements-to-test matrix).
* **Code Coverage Analysis Results:**
  + Collaborate with engineering to analyze and evaluate the results of testing.
  + Verify whether code coverage analysis identifies and addresses high-risk untested paths, safety-critical code paths, and decision logic.

---

#### **Potential Risks and Issues**

For portions of software code that remain untested, SA has the responsibility to:

1. **Identify and Quantify Risks:**
   * Assess operational risks, safety concerns, or mission impacts related to uncovered code.
   * Analyze whether the uncovered code paths affect fault protection, decision-making, safety-critical operations, or mission reliability.
2. **Communicate Findings:**
   * Report untested code and associated risks to the project manager, software assurance authority, and software manager.
   * Highlight potential consequences of leaving code untested, such as latent defects, reliability risks, or unverified error/fault-handling paths.

---

## 7.3 Metrics

SA should track and analyze specific metrics to ensure visibility into software reliability, testing progress, and risk management. Below are the key metrics that SA should collect, with required metrics marked in bold:

1. Test Coverage Metrics:
   * # of Source Lines of Code (SLOC) tested vs. total # of SLOC.
   * Software code/test coverage percentages for all identified safety-critical components (e.g., # of paths tested vs. total # of possible paths).
   * # of tests completed vs. total # of tests.
   * of test cases executed vs. # of test cases planned to validate test completeness.
2. Non-Conformance and Risk Metrics:
   * of Non-Conformances identified by testing phase (Open, Closed, Severity Levels).
   * # of risks trending up or down over time.
   * of risks with active mitigation plans vs. total # of risks.
   * Severity distribution of risks (e.g., red/yellow/green) over each project phase.
3. Life Cycle and Testing Phase Metrics:
   * of risks identified in each life cycle phase (including open vs. closed).
   * Verification test execution trends by testing phase.

#### **Operational Insights:**

Tracking these metrics over time provides critical insights into:

* Testing completeness and maturity.
* Identification of high-risk trends requiring management attention.
* Continuous improvement in software test and assurance processes.

**Note**: Metrics in **bold** are required for all software projects, regardless of classification.

---

## 7.4 Assurance Guidance

#### **SA's Role in Code Coverage Verification**

SA must confirm that the project is correctly measuring code coverage and using metrics to guide testing improvements. This involves:

1. **Spot Checks and Random Verification:**
   * Review how the project is measuring code coverage (e.g., testing execution logs, trace matrices showing test-to-code relationships, and tools used to analyze results).
   * Ensure that selected coverage criteria (e.g., statement, branch, or MC/DC for Class A/B software) are being applied correctly.
2. **Lifecycle Oversight:**
   * Ensure adequate code coverage tracking, recording, and reporting occurs at all phases, including regression testing phases for systems under modification or maintenance.

---

## 7.4.1 Maintenance Guidance

For systems in **operation or maintenance**, SA should ensure that modifications adhere to existing code coverage standards. This may require recalibration of coverage expectations and testing due to changes in operational requirements or software configuration:

1. **Monitoring Modifications:**
   * Ensure code coverage metrics are re-evaluated for all software updates and changes.
   * Validate that regression testing includes code coverage for both new and existing code paths impacted by the modifications.
2. **Steps for SA on Maintenance Projects:**
   * **Step 1**: Confirm that code coverage measurements are being defined, tracked, and reported for modified or requalified software.
   * **Step 2**: Evaluate testing adequacy by identifying newly uncovered portions of code.
   * **Step 3**: Perform a joint risk assessment with engineering for uncovered code components, with mitigation and rationale documented.

---

### **SA Approach for Code Coverage Below 100%**

When projects cannot reach 100% code coverage, SA must:

1. **Perform Comprehensive Uncovered Code Analysis:**

   * Evaluate untested code to identify whether gaps arise from missing requirements, missing tests, extraneous/dead code, or deactivated code.
   * Collaborate with engineers to rationalize uncovered portions of code and gauge the acceptable operational impacts.
2. **Report Risk and Provide Transparency:**

   * Communicate untested code rationales and associated risks to stakeholders (e.g., software manager, project manager) during project reviews.
   * Provide specific recommendations:
     + Determine if new tests or requirements should be created to address gaps.
     + Validate that deactivated/extraneous code is appropriately managed (e.g., safely disabled or flagged to prevent accidental execution).
3. **Key Categories of Untested Code:**

   * **Requirement Missing**: Indicates incomplete requirements traceability.
   * **Test Missing**: Indicates gaps in the test suite.
   * **Extraneous/Dead Code**: Code that is not mapped to requirements; recommend removal.
   * **Deactivated Code**: Code for future configurations; ensure adequate documentation and safeguards.

---

## 7.5 Summary of Responsibilities

#### **Software Assurance Responsibilities**

1. Verify code coverage metrics are being measured and tracked using the project’s agreed-upon tools and criteria.
2. Analyze code coverage results and untested code to identify risks and rationale.
3. Ensure that risk assessments for uncovered code are well-documented and formally accepted by project leadership.
4. Monitor code coverage practices across the lifecycle, including development, regression testing, and maintenance.

#### **Risk Communication**

* Code coverage gaps and their impacts must be reported transparently to all stakeholders. SA provides recommendations for addressing gaps or mitigating risks for uncovered code, even in small or low-risk projects.

---

### **Conclusion**

Software assurance ensures that code coverage requirements are adequately addressed throughout the software development and maintenance lifecycle. By verifying metrics, analyzing risks, and ensuring the rationale for untested code is documented, SA plays a pivotal role in upholding the quality, reliability, and safety of NASA’s software systems.

* SA risk analysis and rationale on any uncovered software code percentage.
* Verification Activities Analysis
* Software assurance results of code coverage analysis.
* Potential risks, and issues resulting from uncovered code during testing.

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical in verifying compliance with the code coverage requirement. It provides tangible artifacts or documentation to demonstrate that code coverage has been measured, tracked, reported, and analyzed throughout the development lifecycle. Below are examples of objective evidence that can be used to satisfy this requirement:

---

### **1. Code Coverage Reports**

* **Description**: Detailed reports generated from tools or manual analyses that display code coverage percentages for the software under test.
* **Components**:
  + **Statement Coverage**: Percentage of lines of code executed during testing.
  + **Branch Coverage**: Percentage of decision-making branches (e.g., `if`, `else`) executed in the code.
  + **Modified Condition/Decision Coverage (MC/DC)**: Percentage of decision logic paths evaluated for safety-critical software.
  + Untested sections of code clearly identified.
* **Example Tools**: JaCoCo, LCOV, BullseyeCoverage, SonarQube, Coverage.py, or other relevant tools.

---

### **2. Code Coverage Metrics Summary**

* **Description**: A cumulative summary that details key metrics tracked for code coverage across the software lifecycle.
* **Components**:
  + Total **Source Lines of Code (SLOC)** vs. tested SLOC.
  + Total number of test cases executed vs. planned.
  + Coverage percentages for individual components or modules, particularly for safety-critical sections of the code.
  + Breakdown of tested vs. untested code paths, highlighting potential risks.
* **Validation**: Demonstrates testing progress over time and compliance with project-specific coverage goals or thresholds (e.g., 100% for Class A/B software, or agreed-upon metrics for Class C/D software).

---

### **3. Traceability Matrix (Requirements to Code to Tests)**

* **Description**: A traceability matrix linking requirements to the code and then to the corresponding test cases, providing evidence that:
  + All requirements have corresponding code implementations.
  + All code is associated with one or more tests.
* **Components**:
  + Requirements mapped to code modules/functions.
  + Tests mapped to code paths/decision points.
  + Gaps or missing coverage identified.
* **Validation**: Provides comprehensive assurance that all requirements are being tested, and untested code sections are understood and evaluated.

---

### **4. Risk Assessment Report for Uncovered Code**

* **Description**: Documented risk analysis detailing the rationale for any uncovered areas of code and their associated risks.
* **Components**:
  + Identification of untested code segments.
  + Categorization of uncovered code (e.g., missing requirements, missing tests, extraneous/dead code, deactivated code).
  + Risk analysis for each uncovered code path, including safety, mission, and operational risks.
  + Mitigation plans for medium/high-risk untested code (e.g., additional requirements, new testing, removal of redundant code).
* **Validation**: Demonstrates that any deviation from 100% coverage is deliberate, justified, and formally accepted by the project and Technical Authority.

---

### **5. Test Execution Logs**

* **Description**: Logs generated during test execution showing which tests were run, their results, and which segments of code they exercised.
* **Components**:
  + List of test cases executed with pass/fail status.
  + Test logs aligning with coverage tools showing paths or code lines exercised during execution.
  + Evidence of testing edge cases, exception handling, and high-risk paths.
* **Validation**: Confirms that coverage measurements were gathered properly and represent the actual tested state of the software.

---

### **6. Software Test Plan (STP)**

* **Description**: The project’s Software Test Plan should include code coverage objectives, methodologies, criteria, and thresholds.
* **Components**:
  + Code coverage goals (e.g., 100% for Class A/B or other thresholds for Class C/D software as agreed by the Center's Engineering Technical Authority).
  + Test strategies (e.g., unit, integration, system, and regression testing).
  + Planned use of code coverage tools and their configuration.
  + Reporting methods and review milestones for coverage tracking.
* **Validation**: Ensures that code coverage has been an upfront, planned activity integrated into the overall testing strategy.

---

### **7. Software Test Results and Reports**

* **Description**: Reports documenting the results of executed tests, including code coverage measurements and analysis.
* **Components**:
  + Test results summary (e.g., which test cases passed/failed and what functionality they covered).
  + Code coverage percentages and trends for various modules across testing phases.
  + Coverage of safety-critical components explicitly highlighted.
  + Risks or open issues identified during testing.
* **Validation**: Demonstrates the adequacy of coverage achieved relative to project requirements.

---

### **8. Software Development and Management Plan (SDMP)**

* **Description**: Documentation specifying the planning and implementation of code coverage requirements.
* **Components**:
  + Defined code coverage metric and thresholds for the project.
  + Procedures for monitoring, tracking, and reporting coverage across the software lifecycle.
  + Resources and tools allocated for achieving coverage goals.
  + Criteria for assessing and mitigating risks associated with uncovered code.
* **Validation**: Confirms that code coverage expectations were established and resources were allocated to fulfill them.

---

### **9. Regression Testing Reports**

* **Description**: Documentation ensuring that modifications to the software do not introduce untested code or regressions into previously tested modules.
* **Components**:
  + Code coverage summaries for regression tests.
  + Evidence that previously covered code paths remain tested after updates.
  + Testing results for new or modified code.
  + Justification for any uncovered code (if applicable).
* **Validation**: Confirms that coverage is maintained, even as the software evolves.

---

### **10. Static Analysis Reports**

* **Description**: Reports generated by static analysis tools that identify untested code paths, dead code, and structural deficiencies.
* **Components**:
  + Output from tools such as Coverity, SonarQube, or CodeSonar.
  + Highlighted regions of untested or unreachable code.
  + Evidence of alignment between static analysis findings and test coverage metrics.
* **Validation**: Ensures that no code path has been overlooked, especially in cases where dynamic testing is challenging (e.g., embedded systems).

---

### **11. Spot-Check Verification Records**

* **Description**: Records from software assurance activities performing spot checks of the processes used to gather code coverage measurements.
* **Components**:
  + Independent artifacts showing specific tests and their alignment to coverage results (e.g., verification of traceability between code and testing).
  + Confidence-building evidence that the project is meeting its coverage obligations and appropriately addressing untested code.
* **Validation**: Provides independent verification of proper code coverage measurement and analysis practices.

---

### **12. Management Review Meeting Notes**

* **Description**: Notes or minutes from milestone reviews (e.g., Test Readiness Reviews (TRRs), Software Acceptance Reviews (SARs), or project management reviews) where code coverage metrics and rationale for uncovered code were presented and discussed.
* **Components**:
  + Details of code coverage achievements to date.
  + Discussion of uncovered code, rationale, and any associated risks.
  + Decisions made regarding further testing or acceptance of untested code.
* **Validation**: Confirms the project's commitment to transparency and stakeholder engagement regarding code coverage.

---

### **Conclusion**

The objective evidence outlined above provides comprehensive documentation of code coverage practices, demonstrating compliance with NASA's requirements. By collecting and analyzing these artifacts throughout each phase of the software lifecycle, the project ensures that software has been adequately tested, with a full understanding of risks associated with any uncovered code. This evidence supports accountability, risk management, and stakeholder confidence in the delivered software.

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
