# SWE-191 - Software Regression Testing

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695526. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing

SWE-191 - Software Regression Testing

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695526)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695526&showCommentArea=true&showComments=true#addcomment)

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

4.5.11 The project manager shall plan and conduct software regression testing to demonstrate that defects have not been introduced into previously integrated or tested software and have not produced a security vulnerability.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-191 History

SWE-191 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.5.11 The project manager shall plan and conduct software regression testing to demonstrate that defects have not been introduced into previously integrated or tested software and have not produced a security vulnerability. |
| Difference between C and D | No change |
| D | 4.5.11 The project manager shall plan and conduct software regression testing to demonstrate that defects have not been introduced into previously integrated or tested software and have not produced a security vulnerability. |

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

The purpose of regression testing is to ensure that changes made to the software have not introduced new defects. One of the main reasons for regression testing is to determine whether a change in one part of the software affects other parts of the software. To ensure no new defects are injected into the previously integrated or tested software, the project manager should both plan and conduct regression testing to demonstrate the newly integrated software.

Software regression testing is the process of systematically re-testing previously integrated or tested software after changes (e.g., modifications, bug fixes, updates, or enhancements) have been made. The goal is to ensure that these changes do not introduce new defects, break existing functionality, or create security vulnerabilities in the software. Regression testing is critical for maintaining software reliability, functionality, and security as it evolves over its lifecycle.

---

### **Rationale**

1. **Prevent the Introduction of New Defects**:

   * Software development is inherently iterative, and changes (such as fixing bugs, addressing performance issues, or implementing new features) can inadvertently cause unintended consequences in unrelated or previously functioning parts of the system.
   * Regression testing provides confidence that existing functionality continues to operate as intended after changes, reducing the likelihood of introducing defects that degrade system performance or reliability.
2. **Ensure System Stability and Reliability**:

   * Integrated software often involves interdependencies between modules, where changes to one module impact other modules in subtle or unforeseen ways. Without regression testing, these issues might go undetected, compromising overall system stability.
   * By systematically verifying previously tested functionalities, regression testing helps ensure the robustness and quality of the software.
3. **Protect Against Security Vulnerabilities**:

   * Changes in software can inadvertently introduce new security vulnerabilities. For example:
     + Updates may unintentionally bypass established security checks.
     + Added functionality can expose previously hidden attack surfaces or weaknesses.
   * Regression testing for security vulnerabilities not only validates functional correctness, but also ensures that security controls remain effective and no new exploits are introduced as a result of changes.
4. **Demonstrate Compliance with Standards and Mission Requirements**:

   * Many mission-critical systems must comply with regulatory, safety, and security standards, such as NASA-specific engineering standards or industry standards like ISO 26262 (safety-critical systems) and OWASP (secure software development).
   * Regression testing helps prove compliance by demonstrating that system updates maintain previously verified levels of performance and security.
5. **Risk Mitigation**:

   * Failure to address regression testing can result in costly system failures during operations, mission-critical failures, or security breaches. Early detection of regressions through testing mitigates these risks.
   * The financial and reputational cost of such failures far exceeds the cost of implementing a comprehensive regression testing process.
6. **Facilitate Continuous Software Evolution**:

   * Projects often encounter iterative updates and evolving requirements throughout development and maintenance. Regression testing ensures that changes can be made confidently without compromising software quality or functionality.
   * It allows teams to integrate new features while preserving existing functionality and meeting schedule and mission requirements.
7. **Support Maintenance Activities**:

   * Systems in long-term operation frequently undergo maintenance for bug fixes, patches, or hardware compatibility updates. Regression testing ensures these changes do not degrade the system or cause regressions in previously functioning components of legacy software.

---

### **Benefits of Regression Testing for Preventing Defects and Vulnerabilities**

1. **Functional Verification**:

   * Ensures that previously verified functions continue to work correctly and consistently after modifications are made.
   * Reduces risks of introducing defects that compromise mission-critical software components.
2. **Security Assurance**:

   * Identifies potential security vulnerabilities introduced during updates or fixes.
   * Ensures security features (e.g., authentication, encryption, error handling) are tested and remain robust after any changes.
3. **Better Test Coverage**:

   * Improves test coverage for scenarios where recent changes interact with existing functionality.
   * Allows teams to identify edge cases and integration defects that otherwise may slip through testing.
4. **Early Defect Identification**:

   * Detects regressions early in the lifecycle before they propagate to later stages, reducing debugging costs and risks during operations.
5. **Cost and Resource Efficiency**:

   * By automating regression tests, teams can efficiently test large portions of code to identify regressions without requiring exhaustive manual testing.
   * Regression testing minimizes the need for repeated manual validation of unchanged code, saving time and resources.
6. **Build Confidence in Software Quality**:

   * Provides team members and stakeholders with confidence that the delivered software continues to meet functional, security, and performance expectations—even as it evolves with new updates.

---

### **Key Components of Regression Testing**

1. **Test Planning**:

   * Regression tests must be planned and prioritized based on mission risks, criticality, and anticipated areas of change (e.g., vulnerable modules, newly introduced features).
2. **Automated Regression Testing**:

   * Incorporating automated test suites reduces the time and effort required for regression testing and ensures consistent execution of tests across multiple iterations.
   * Automated tools can track test coverage, detect regressions, and verify that fixes or changes do not affect existing systems.
3. **Security Validation**:

   * Security regression testing should include testing for vulnerabilities such as injection attacks, unauthorized access, performance under malicious input, and verification of security controls (e.g., role-based access, encryption protocols).
4. **Baseline Testing**:

   * A "baseline" set of tests based on previously verified functionality is essential for regression testing. These tests ensure that unchanged functionality remains stable and reliable over time.
5. **Risk Management**:

   * Regression testing should focus on modules with the highest risk of regressions, such as modules with complex interdependencies, dynamically updated components, and interfaces prone to security exploits.
6. **Comprehensive Coverage**:

   * Regression tests should exercise critical functionality, decision points, and edge cases. Complex algorithms, safety-critical components, and high-risk error-handling paths must receive special attention.
7. **Impact Analysis**:

   * Before deciding on which regression tests to execute, an impact analysis should be conducted to determine how changes influence the software architecture and what areas require testing.

---

### **Objective Evidence for Compliance with Requirement 4.5.11**

The following artifacts can be used to demonstrate compliance with this requirement:

1. **Regression Test Plans**:

   * Document identifying how regression tests are planned, prioritized, and executed.
   * Includes focus areas such as functional correctness and security validation.
2. **Test Results from Regression Suites**:

   * Evidence showing that tests were executed to verify no defects or vulnerabilities were introduced after changes.
   * Includes pass/fail results and analysis of uncovered gaps.
3. **Software Test Reports**:

   * Detailed reports outlining issues identified during regression testing and their resolution.
   * Includes risk assessments related to uncovered regressions and mitigation actions.
4. **Defect Tracking Logs**:

   * Logs showing issues identified during regression testing and their closure status.
   * Demonstrates that no unresolved defects or vulnerabilities exist post-testing.
5. **Code Coverage Reports**:

   * Objective evidence from tools confirming that code coverage was achieved during regression testing.
6. **Security Vulnerability Analysis Outputs**:

   * Reports or automated scans validating that no new vulnerabilities have been introduced after modifications.
7. **Regression Test Execution Logs**:

   * Logs showing which test cases were executed, the test results, and the areas of code covered by the regression testing.
8. **Automation Test Tool Reports**:

   * Evidence of automated regression testing execution and results (e.g., from tools like Selenium, TestNG, or proprietary NASA automated platforms).

---

### **Conclusion**

Requirement 4.5.11 ensures that project managers plan and conduct rigorous regression testing to safeguard previously tested software while avoiding the introduction of defects or security vulnerabilities. Regression testing maintains system stability, protects mission-critical functionality, and prevents risks, making it a vital activity for reliable software delivery and maintenance. By coupling regression testing with security validation and continuous improvement practices, this requirement supports NASA’s commitment to delivering robust, secure, and high-quality systems.

# 3. Guidance

### **Importance of Regression Testing**

Regression testing is essential in maintaining the reliability, functionality, and safety of software as it evolves through modifications, updates, enhancements, and patches. It ensures that previously developed and tested software continues to function as intended after changes are introduced. It also uncovers new bugs introduced by those changes, which may affect performance, functionality, or security.

Key reasons for regression testing include:

1. **Verifying Stability**: Confirms that existing features and functionality are unaffected by modifications.
2. **Detecting New Defects**: Identifies unintended consequences or new errors caused by recent changes.
3. **Maintaining Performance**: Ensures changes do not introduce performance issues, race conditions, or other unintended computational problems.
4. **Guaranteeing Security**: Verifies that changes do not create new vulnerabilities or compromise existing security controls.
5. **Compliance**: Ensures the software remains compliant with project requirements, safety standards, and operational criteria.

---

### **Regression Testing Across the Lifecycle**

Regression testing applies at all **levels of testing**—unit, integration, system, and acceptance testing—and should be executed **after any modification** to code, design, or requirements. This ensures that:

* The implemented changes work as intended.
* No new defects or errors were introduced.

For any system modifications after the baseline (first software release), regression testing is **mandatory**. These changes include:

* Software enhancements.
* Bug fixes (patches).
* Configuration changes.
* Integration with other systems or software.

> **Reminder**: "Fixed" code often introduces its own set of errors. Regression testing is therefore critical to ensuring stability and safety. Even minor changes may affect system performance when close to capacity limits, and dependencies between components can cause cascading errors.

---

### **Key Elements of Regression Testing**

1. **Re-Test and Verify**:

   * Regression testing involves re-executing specific test cases on the modified code to ensure that prior functionality is intact.
   * It verifies that the system performs at least as well **after the change** as it did **before the change**.
2. **Software Change-Impact Analysis**:

   * Conduct an impact analysis to determine which areas of the software could be affected by the proposed changes.
   * Use this analysis to guide the selection of tests in the regression test suite.
   * Changes to **safety-critical code within the revised areas** require an especially thorough analysis.
3. **Requirements Coverage**:

   * Trace each software change back to identified requirements to ensure test coverage, especially for **safety-critical requirements within the revised areas**.
   * Every modified block or statement of code should have at least one corresponding test to verify it.
4. **Testing Strategy**:

   * To optimize resources, regression test strategies may vary based on the complexity and importance of the system. Appropriate test subsets should be carefully selected, and tests that previously detected errors or failures should always be included in any regression suite.
   * **Safety-Critical Code**: All safety tests within the revised areas must be repeated, even for seemingly minor changes.

---

### **Sources for Regression Test Cases**

* **Unit Tests**:
  + Existing unit tests can be saved, adapted, and reused as regression test cases.
  + These tests often require scripting or tailoring to align with changes in the software.
* **Defect-Based Tests**:
  + Test cases created to reproduce and validate defects should be stored and reused in the regression test suite, ensuring that resolved defects do not reoccur.
* **System and Integration Tests**:
  + System and integration tests for verifying external interfaces, subsystem communication, and overall functionality provide valuable regression test cases.
* **Requirement-Based Tests**:
  + Regression tests may be derived by identifying which requirements have been impacted by the change. This is particularly effective for tracing safety-critical requirements back to test cases.

---

### **Challenges and Cost Considerations**

For complex systems, exhaustive regression testing (retesting the **entire system**) can be prohibitively expensive and time-consuming. As such, effective regression-test selection techniques are vital to balance **thoroughness** with **efficiency**.

#### **Selecting Test Subsets:**

1. **Picking the Right Subset**:
   * Selecting a proper subset of test cases is critical and often requires skill and experience. Important considerations for selection include:
     + Risk of potential defects in the changed components.
     + Dependencies and interfaces impacted.
     + Criticality of the changed software section.
   * Focus on modules that form the foundation for safety-critical operations.
2. **Testing Minor Code Changes**:
   * Minor code changes generally require less regression testing unless they occur in high-impact or safety-critical areas.
   * Regression tests for safety-critical systems should always include safety performance and stress tests regardless of the perceived magnitude of changes.

---

### **Automation of Regression Testing**

Regression test automation is **highly recommended** to reduce the time and cost associated with manual testing. Automated tests provide several benefits:

* Faster execution and repeatability.
* Ensured consistency during multiple iterations of regression testing.
* Easier integration into **continuous integration/continuous deployment (CI/CD)** pipelines.

Utilize regression testing tools and frameworks such as:

* JUnit, Selenium, TestNG, or PyTest for automated test execution.
* Scripted unit tests for fast verification of module-level changes.
* Coverage analysis tools like LCOV, JaCoCo, or Code Coverage for tracking test coverage of impacted areas.

---

### **Regression Test Methodologies**

#### **1. Minimization Approach:**

* Goal: Create a **minimal set of regression tests** that exercise the changed code.
* Focus: Coverage-based criteria where each changed code statement and modified block must be executed by at least one test.

#### **2. Coverage-Based Approach:**

* Involves running all system tests that exercise changed or affected components.
* Focuses on achieving **comprehensive coverage** of modified areas without explicitly minimizing the tests.

#### **3. "Safe" Selection Approach:**

* Selects all tests that could cause the modified program to produce different outputs compared to the original.
* Ensures no tests are excluded that might identify defects in the modified software.

#### **4. Program Slicing:**

* Analyzes the program to determine what variables or statements are impacted by code changes.
* Determines which test cases must be executed based on the code areas affected by slicing.

#### **5. Requirement-Based Approach:**

* Utilizes requirements traceability to determine which requirements and associated tests are impacted by software changes.
* **Critical for safety-critical systems**, ensuring all safety or mission-critical requirements are re-tested along with their dependencies.

---

### **Recommendations for Effective Regression Testing**

1. **Test Selection Strategy**:
   * Carefully balance risk, time, and resources when selecting regression tests.
   * Include tests for:
     + Error-prone modules.
     + Modules with critical dependencies.
     + Tests that previously found defects.
     + System stress and performance tests.
2. **Risk-Based Prioritization**:
   * Prioritize testing of high-risk or safety-critical code paths.
   * Even minor changes to safety-critical code should trigger a comprehensive regression suite.
3. **Test Planning**:
   * Define regression test suites during test planning and document them in the **Software Test Plan (STP)**.
   * Include rationale for selected test subsets, ensuring traceability to impacted requirements and risks.
4. **Regular Automation Updates**:
   * Ensure automated tests are regularly maintained and updated based on the latest changes in software requirements and code.
5. **Test Result Analysis**:
   * Use robust analysis tools to evaluate test outcomes, identify coverage gaps, and measure system performance changes post-modification.

---

### **Conclusion**

Regression testing is a core part of the software lifecycle that ensures continuous reliability, performance, and safety of software systems. A well-planned regression testing process, supported by automation, a risk-based test selection strategy, and change-impact analysis, mitigates the risk of introducing defects or vulnerabilities as the software evolves. For mission-critical and safety-critical systems, regression testing is **non-negotiable**—it is vital to the success of the mission and the safety of operations.

## 3.1 Regression Test approaches:

**Minimization** is one approach to regression test selection. The goal is to create a regression test suite with a minimal number of tests that will cover the code change and modified blocks. The criteria for this approach is coverage – what statements are executed by the test. In particular, every statement in the changed code must be executed, and every modified block must have at least one test.

**Coverage** approaches are based on coverage criteria, like the minimization approach, but they are not concerned about minimizing the number of tests. Instead, all system tests that exercise the changed or affected program component(s) are used.

**Safe** approaches place less emphasis on coverage criteria and attempt instead to select every test that will cause the modified program to produce different output than the original program. Safe regression test selection techniques select subsets that, under certain well-defined conditions, exclude no tests (from the original test suite) that if executed would reveal faults in the modified software.

**Program slicing** can be a helpful technique for determining what tests to run. Slicing finds all the statements that can affect a variable or all statements that a variable is involved with. Depending on the changes, slicing may be able to show what components may be affected by the modification.

A requirements management program is a useful tool in determining what tests need to be run. When changes impact a specific requirement, especially a safety requirement, all test cases that test that requirement should be run. Knowing what test cases test what requirements is one aspect of requirements traceability.

Whatever strategy is used to select the regression tests, it should be a well thought out process. Balance the risks of missing an error with the time and money spent on regression testing. Very minor code changes usually require less regression testing, unless they are in a very critical area of the software. Also, consider including in the regression suite tests that previously found errors, tests that stress the system, and performance tests. You want the system to run at least as well *after* the change as it did *before* the change! For safety-critical code, or software that resides on the same platform as safety-critical code, the **software safety tests must be repeated**, even for minor changes. See also [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).

See also [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures), [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification)

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan), * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.10 - Related Activities](/spaces/SWEHBVD/pages/146539354/7.10+-+Related+Activities) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

For smaller projects, where resources and budgets are limited, it is critical to maximize the reuse of existing resources and adopt efficient strategies to create and maintain regression tests. Below are practical ways to implement regression testing for small projects:

---

### **1. Reuse Existing Resources**

1. **Leverage Unit Tests**:

   * Unit tests developed during the implementation phase can serve as the foundation for regression testing. These tests already target specific code segments and can help validate changes without additional overhead.
   * Maintain and update unit tests as the project evolves to always reflect the current state of the software.
2. **Reuse Defect Replication Tests**:

   * When addressing bugs or defects, create reproducible test cases to validate that the issue is fixed.
   * Store these defect replication tests in a regression test suite, as they ensure that the resolved issue remains fixed in future builds.
3. **Repurpose Formal Tests as Regression Tests**:

   * Formal tests designed to validate requirements or overall system functionality (e.g., integration tests, system tests) can also be reused as regression tests.
   * These tests should be retained and rerun for future builds to confirm that core functionality remains intact.

---

### **2. Incremental Testing for Cost Reduction**

* Rather than executing a full regression suite every time, adopt **incremental testing**:
  + Focus only on the parts of the software impacted by recent code changes or specific bug fixes, as identified through **change-impact analysis**.
  + If time and resources permit, broaden the regression scope to include high-priority or safety-critical tests.

---

### **3. Automate Where Possible**

* Small projects often have limited manual testing bandwidth, so automation becomes a critical cost-saving mechanism:
  + Use **scripted unit tests** with tools like PyTest, JUnit, or NUnit, enabling quick re-execution of test cases in each build cycle.
  + Incrementally build an automated test suite to reduce manual effort and ensure consistent execution of regression tests over time.

---

### **4. Build Test Suites for Current and Future Builds**

* Treat every formal test created during development as a potential regression test for future builds:
  + Clearly document and organize tests, associating them with the feature, requirement, or defect they validate.
  + This ensures that as the project progresses, you accumulate a reusable and cost-effective regression test suite.

---

### **5. Prioritize Testing for Small Teams**

For projects with limited resources, prioritize regression tests based on impact and importance:

1. **Critical Functionality**:
   * Test areas most critical to the system (e.g., core functionalities, safety requirements, high-risk areas).
2. **Frequent Changes**:
   * Focus on modules or code that are frequently updated or highly interconnected with other components.
3. **Defect-Prone Areas**:
   * Include tests in areas where bugs have historically occurred or are statistically more likely.

---

### **6. Adopt Lightweight Processes**

Keep regression testing for smaller projects simple and practical:

* **Document as You Go**:
  + Avoid creating unnecessary test artifacts. Focus on lightweight documentation that captures essential details (e.g., what a test validates and how to execute it).
* **Start Small, Iterate Over Time**:
  + Small projects may begin with a modest suite of regression tests and expand incrementally. Focus first on key tests, adding more as the project scales.

---

### **7. Communication with Team**

* For small teams, ensure regression test plans are clearly communicated among developers and testers. Everyone should understand:
  + Which tests are designated for regression.
  + How to execute these tests for future iterations.
  + The importance of regression testing in preventing new errors.

---

### **Summary for Small Projects**

* **Reuse**: Maximize reuse of unit tests, defect replication tests, and formal tests to save time and effort.
* **Incremental**: Focus on testing impacted areas, prioritize high-risk or critical components, and evaluate broader coverage if resources allow.
* **Automate**: Invest in simple automation tools to enable consistent and repeatable testing.
* **Evolve**: Create and expand regression testing incrementally for current and future builds.

By following these strategies, smaller projects can implement effective and manageable regression testing processes without exceeding time or cost constraints.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-337)

  [Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf "Click to open in new window")

  Souppaya, Murugiah, Scarfone, Karen, NIST Special Publication NIST SP 800-40r4, April, 2022
* (SWEREF-367)

  [IEEE Standard Dictionary of Measures of the Software Aspects of Dependability,](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1634994 "Click to open in new window")

  IEEE Computer Society, Sponsored by the Software Engineering Standards Committee, IEEE Std 982.1™-2005, (Revision of IEEE Std 982.1-1988),
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following lessons learned are derived from **NASA's Lessons Learned Information System (LLIS)** and other documented experiences. They emphasize the importance of planning and conducting regression testing to prevent defects and ensure software remains reliable, safe, and functional after updates or modifications.

---

### **1. Lesson Learned: Lack of Comprehensive Regression Testing Can Introduce Critical Failures**

**LLIS Reference**: [Lesson Number 1770](https://llis.nasa.gov/lesson/1770) - **Mars Climate Orbiter Mishap**

* **Description**: The Mars Climate Orbiter mission failed due to a navigation error caused by improper usage of two different units of measurement (imperial vs. metric) between collaborating software modules. Regression testing was insufficient to identify this integration error after software changes were applied.
* **Root Cause**: Changes or modifications were implemented in the navigation software, but the broader impact was not verified adequately through regression testing. This oversight propagated an undetected mismatch between the modules.
* **Lesson**: Regression testing must verify that changes at all levels (unit, integration, system) do not introduce unintended interactions between components. For systems with interdependencies, integration tests should be reused or expanded during regression testing to confirm proper communication between software modules.

---

### **2. Lesson Learned: Regression Testing of Safety-Critical Systems**

**LLIS Reference**: [Lesson Number 1183](https://llis.nasa.gov/lesson/1183) - **Recommendation for Programmable Logic Device Failures**

* **Description**: Programmable logic devices (PLDs) and software systems in safety-critical flight hardware were modified following performance updates. However, insufficient or incomplete regression testing failed to uncover unintended consequences introduced by these changes. This posed risks to safety-critical functions during operation.
* **Root Cause**: Updates to software were improperly tested for their impact on safety-critical code, resulting in potential safety violations.
* **Lesson**:
  + Always re-execute **safety-critical tests**, even for minor changes, as their disruption could lead to catastrophic mission failure.
  + Regression test planning for safety-critical systems must explicitly include tests that validate system-level safety and performance requirements after updates.
  + Utilize **change-impact analysis** to identify areas where safety-critical tests should be concentrated.

---

### **3. Lesson Learned: Incomplete Regression Testing Due to Time/Human Resource Constraints**

**LLIS Reference**: [Lesson Number 3430](https://llis.nasa.gov/lesson/3430) - **Software Validation and Verification Planning**

* **Description**: In certain projects, a lack of time and resource allocation limited the scope of regression testing. Only the directly modified software modules were retested, while potentially affected modules and system-level operations were ignored, leading to untested latent errors.
* **Root Cause**: Underestimating the effort and resources required to perform effective regression testing caused tests to be overly narrow. Modules indirectly affected by changes were overlooked in testing.
* **Lesson**:
  + Schedule adequate time and resources for regression testing as part of the **Software Test Plan (STP)**.
  + Ensure impact analysis includes testing of dependent modules, interfaces, and systems to prevent cascading errors.
  + The cost of regression testing is significantly lower than the cost of uncovering defects during operations.

---

### **4. Lesson Learned: Automation is Key for Efficient Regression Testing**

**LLIS Reference**: [Lesson Number 2158](https://llis.nasa.gov/lesson/2158) - **Software Automation Benefit in Testing Knowledge**

* **Description**: Manual regression testing for large-scale software systems was time-consuming and resource-intensive. Attempts to improve efficiency led to the adoption of automated software testing, which significantly reduced costs, increased test coverage, and enabled consistent execution of regression tests following software updates.
* **Lesson**:
  + Leverage test automation tools to manage regression testing in complex software systems. Automated tests can be repeated consistently after modifications, especially for routine builds or patches.
  + Design and script regression tests early in development to facilitate automated execution during iterative testing cycles.
  + Automate high-risk or repetitive test cases while leaving exploratory or edge-case testing for manual testers.

---

### **5. Lesson Learned: Defining Regression Tests During Initial Test Planning**

**LLIS Reference**: [Lesson Number 1954](https://llis.nasa.gov/lesson/1954) - **Software Test Planning Insufficient for Change Management**

* **Description**: A project failed to effectively define its regression test suite as part of the overall test planning process, forcing teams to retroactively identify test components after software updates were made. This reactive approach resulted in insufficient test coverage and overlooked defects.
* **Lesson**:
  + Define regression testing approaches in the **Software Test Plan (STP)** early in the lifecycle.
  + Identify reusable tests, including unit tests and formal system tests, that can later serve as regression tests.
  + Plan for regular updates of the regression test suite as the software evolves, maintaining traceability to requirements.

---

### **6. Lesson Learned: Failures Due to Missing Tests for Non-Critical Changes**

**LLIS Reference**: [Lesson Number 1704](https://llis.nasa.gov/lesson/1704) - **Leverage Small Code Changes to Maximize Testing Opportunities**

* **Description**: A non-critical code change for a mission component was assumed to have no impact on system performance. Limited regression testing was performed, overlooking the fact that the change indirectly influenced interactions with other modules. The resulting error caused an operational anomaly that required emergency recovery measures.
* **Lesson**:
  + Even minor code changes can have unexpected consequences, especially in interconnected or integrated systems.
  + Revision to **safety-related tests** and thorough regression test coverage should be performed for all changes, regardless of their apparent criticality.
  + Use approaches like **program slicing** or **change-impact analysis** to identify and test all downstream areas impacted by changes.

---

### **7. Lesson Learned: Historical Defects Are Valuable for Regression Testing**

**LLIS Reference**: No direct LLIS number but general industry guidance from NASA projects such as **Space Shuttle Software Development**.

* **Description**: Over the operational life of the Space Shuttle, repeat problems with software errors re-introduced defects into the code that had been resolved earlier. These regressions could have been uncovered earlier if prior defect resolution tests had been included in regression suites.
* **Lesson**:
  + Historical defects and their associated test cases ("defect replication tests") are valuable. Always include test cases for resolved bugs in the regression suite to ensure known issues do not reoccur.
  + Maintain a comprehensive test case repository explicitly tied to defect tracking systems for reuse during regression.

---

### **Recommendations for Projects Based on NASA Lessons Learned**

* **Plan Regression Testing from the Start**: Incorporate regression test plans into the **Software Test Plan (STP)** early.
* **Reuse and Automate**: Reuse unit tests, defect replication tests, and formal system tests. Automate these tests wherever possible to reduce cost and achieve consistency.
* **Perform Change-Impact Analysis**: Always conduct a software change-impact analysis to identify all affected areas requiring regression testing.
* **Prioritize Testing for Safety-Critical Systems**: Safety-critical tests must always be executed, regardless of the size or perceived criticality of the change.
* **Use Historical Data**: Include regression tests for fixed defects to protect against reintroduction of historical bugs.
* **Allocate Resources Appropriately**: Underestimate neither the time nor the resources required for effective regression testing in the project schedule.
* **Leverage Tools and Techniques**: Use slicing, coverage approaches, and automated frameworks to optimize regression tests and ensure thorough coverage.

---

### **Conclusion**

The lessons learned from NASA emphasize that effective regression testing is vital to ensuring the stability, safety, and compliance of software systems, regardless of the size or complexity of changes. Proper planning, automation, reuse of resources, and attention to safety-critical functions are recurring themes in preventing costly mission failures. By applying these lessons, teams can reduce risks, uncover latent defects early, and deliver high-quality software under both budget and time constraints.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Consider impact on testing when developing requirements in early lifecycle phases.](https://software.gsfc.nasa.gov/lesson-details/84/) **Lesson Number 84**: The recommendation states: "Consider impact on testing when developing requirements in early lifecycle phases, and ensure a critical review by operations team members."
* [Employ regression testing as risk mitigation](https://software.gsfc.nasa.gov/lesson-details/112/). **Lesson Number 112**: The recommendation states: "Employ regression testing as risk mitigation when delivering builds to I&T before build verification testing (BVT) is completed."
* [Lab functional test helps verify lab is working, following any lab changes](https://software.gsfc.nasa.gov/lesson-details/306/). **Lesson Number 306**: The recommendation states: "Lab changes can and will have unintended side effects.  Develop a comprehensive lab functional test that verifies all components in the lab.  Run the functional test periodically as well as before and after any lab changes (this allows identification of problems before changes are made).  It’s not easy to see the impacts that changes might have, but in a lab where machines must do their job and talk to each other any change could break something.  Changes include, but are not limited to: 1) Operating system upgrades, 2) simulator updates, 3) FSW updates, 4) Other application updates (like ITOS), 5) power supply changes (they talk on the network), and 6) anything else that changes."
* [Key Mission Ops Tests essential to timely V&V of flight design/mission ops concept& launch readiness](https://software.gsfc.nasa.gov/lesson-details/342/). **Lesson Number 342**: The recommendation states: "Develop/iterate/execute system level tests to verify/validate data system/mission Concept of Operations during Observatory I&T (e.g., the Comprehensive Performance Test (CPT) and Day-in-the-Life (DiTL) test). The CPT should be: a) thorough (exercising all copper paths, as many key data paths as reasonable, and using operational procedures); b) executed prior to/post significant events throughout Spacecraft & Observatory I&T; and c) designed comprehensive, yet short enough to be executed multiple times (e.g., the PACE CPT was specifically designed to be 4-5 days). The multi-pass DiTL test can demonstrate nominal operational procedures/processes and, when executed prior to the pre-environmental CPT, can be the basis for the instrument functionals during the environmental cycles and post environmental functional checkouts of the instruments."

# 7. Software Assurance

**SWE-191 - Software Regression Testing**

4.5.11 The project manager shall plan and conduct software regression testing to demonstrate that defects have not been introduced into previously integrated or tested software and have not produced a security vulnerability.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project plans regression testing and that the regression testing is adequate and includes retesting of all safety-critical code components.

2. Confirm that the project performs the planned regression testing. 

3. Identify any risks and issues associated with the regression test set selection and execution.

4. Confirm that the regression test procedures are updated to incorporate tests that validate the correction of critical anomalies.

## 7.2 Software Assurance Products

Software assurance (SA) plays a critical role in ensuring that regression testing is planned, comprehensive, and effective in confirming that software changes do not introduce defects, compromise functionality, or create new hazards. This includes verifying the adequacy of regression test plans, analyzing test sets, tracking issues and risks, and ensuring that regression testing aligns with safety, security, and performance goals.

The goals of SA during regression testing include:

* Verifying that regression testing is appropriately planned and executed.
* Ensuring that previous functionality remains intact after changes.
* Confirming that changes do not introduce new defects or hazards.
* Enhancing the regression testing process by identifying gaps or areas of improvement.

**1. Software Assessment of Regression Test Sets**

* **Objective:**  
  To ensure the selected regression test set thoroughly exercises all impacted areas, including verifying that every safety‑critical function within the revised or modified portions of the software is fully tested to mitigate associated risks.
* **SA Activities:**

  + Analyze the regression test set’s completeness, focusing on its ability to validate the modified areas and assess any ripple effects on other parts of the system.
  + Verify that all safety‑critical functions within the revised areas—are included in and fully exercised by the test set.
  + Review the impact analysis associated with software changes to confirm that all affected areas are tested.
  + Identify risks or issues in the regression testing process, such as inadequate test coverage or improperly selected test cases.
  + Track identified risks and issues in the project tracking system, ensuring they are mitigated and resolved.

**2. Review Regression Test Artifacts**

* SA will review the following key artifacts to verify the adequacy of the regression testing process:
  + **Software Regression Test Procedures**: Ensure that procedures are complete, clear, and aligned with the testing scope.
  + **Software Regression Test Reports**: Confirm thorough documentation of regression test execution and results.
  + **Software Test Plan (STP)**: Verify that the STP includes regression test planning, selection criteria, and integration into the overall test strategy.

**3. Analyze Regression Test Results**

* SA will compare the current regression test results with:
  + Results from previous regression tests.
  + Results obtained during earlier functional or system testing.
  + Expected test results based on software design and requirements.
* Any discrepancies in results should be brought to the attention of the development and testing teams for resolution.

**4. Monitor Change-Driven Testing Activities**

* Track whether regression tests are re-executed for all planned changes and ensure that additional tests are added as new risks or issues are discovered.

---

## 7.3 Metrics for Regression Testing Assurance

SA should track and evaluate key metrics to assess the effectiveness of regression testing processes. These metrics also provide insight into areas that might require corrective actions or additional attention. Examples include:

#### **Key Metrics**

1. **Requirement Verification**:

   * **# of safety-critical requirement verifications vs. total # of safety-critical requirement verifications completed.**
   * **# of detailed software requirements tested to date vs. total # of detailed software requirements.**
2. **Test Coverage and Completion**:

   * **# of tests completed vs. total # of tests planned.**
   * **# of tests executed vs. # of tests completed.**
   * **# of requirements tested vs. total # of requirements.**
   * **# of cybersecurity mitigation implementations tested vs. total # of cybersecurity mitigation implementations identified.**
3. **Defect Tracking**:

   * **# of non-conformances identified during regression testing phases (e.g., Open/Closed, severity by priority).**
   * **# of safety-related non-conformances identified over time.**
   * **# of risks trending up vs. # of risks trending down over time.**
4. **Regression Suite Effectiveness**:

   * **# of regression test set non-conformances/risks over time (Open, Closed, Severity).**
   * **# of previous failures in regression suite successfully retested.**

Additional metrics and breakdowns can be referenced in **Topic 8.18 - SA Suggested Metrics.**

---

## 7.4 Guidance for Software Assurance During Regression Testing

#### **1. Review and Confirm the Adequacy of Regression Testing Plans**

* SA will review the project’s **Software Test Plan (STP)** and associated test procedures to confirm the following:
  + Regression testing is **accounted for** in the overall test strategy.
  + The planned regression test set adequately validates changes and their impacts while maintaining coverage for safety-critical and mission-critical components.
  + Test selection balances efficiency (time, cost) with testing rigor, ensuring risks are mitigated while resources are used effectively.

#### **2. Ensure Proper Test Case Selection**

Regression testing typically involves re-executing a subset of previously executed tests. To confirm this subset is appropriate, SA will evaluate if:

* **Safety-Critical Code**: All safety‑critical functions within the revised areas are included.
* **Core Functional Areas**: Test cases that validate primary system functions and essential operations are included.
* **High-Risk Areas**: Focus on areas with:
  + Frequent errors.
  + High complexity or interdependencies.
  + Recent or repeated changes.
* **Stress, Boundary, and Security Testing**:
  + Include stress tests simulating high-load or edge-case scenarios.
  + Include any security vulnerability-related tests covering newly mitigated risks.
* **Historical Issues**:
  + Regression test sets include test cases for defect replication and previously failed tests.

#### **3. Assess Coverage in Specific Testing Categories**

Regression testing should extend to the following testing categories:

* **Functional Testing**: Confirm functionality operates as designed.
* **Performance Testing**: Verify performance remains within acceptable parameters after changes. Prevent performance degradations due to memory leaks, inefficiencies, or race conditions.
* **Integration Testing**: Ensure that changes did not disrupt software interactions or system communication.
* **Security Testing**: Address changes that might introduce security-related vulnerabilities by including mitigation-identified test cases.
* **System Testing**: Confirm the software operates correctly as part of the broader system.

---

### **4. Support and Monitor Test Execution**

Once the test set is confirmed as adequate, software assurance will:

* Verify that regression testing is executed **according to the plan**.
* Ensure all safety-critical and cybersecurity test cases are run and **properly documented**.
* Analyze the test sets and results to ensure:
  + **Defects are properly addressed** in follow-up testing cycles.
  + Essential operational activities and safety-critical operations are validated.

---

### **5. Assist in Discrepancy Resolution**

Software assurance will:

* Identify and document any **discrepancies** during regression testing, including failed tests or mismatches with expected outcomes.
* Track identified issues or risks in a **project tracking system**, from discovery through closure.
* Confirm all identified issues are addressed, with applicable test updates included in the regression set for future builds.

---

### **6. Continuous Process Improvement**

SA teams will analyze issues and risks identified during regression testing and use this information to:

* Improve the **test selection and execution process**.
* Inform future test planning with lessons learned.
* Ensure regression test sets are updated to remain relevant across the software lifecycle.

---

### **Special Considerations for Safety-Critical Software**

For **safety-critical software within the revised areas**, regression tests must demonstrate:

* Correct execution of critical software functions.
* Compatibility and correctness of integrated critical units.
* The absence of new hazards arising due to changes, including abnormal scenarios such as overload conditions.

> *Refer to SWE-205 - Determination of Safety-Critical Software for additional guidance.*

---

### **7. Closing the Loop: Test Results Verification**

SA will analyze test results from regression testing and compare them with:

* Previous test runs.
* Baseline results from system and functional tests.
* Acceptance criteria outlined in the test plan.

Discrepancies, risks, and improvement opportunities will be communicated to the development and testing teams for resolution.

---

### **Conclusion**

Software assurance ensures that regression testing is planned, executed, and analyzed effectively to mitigate risks, validate software changes, and maintain system integrity. By confirming adequate test planning, reviewing test execution, addressing issues, and driving continuous improvement, SA upholds high standards of quality, safety, and security throughout the software lifecycle.

  

If using an Agile or incremental development process, then code verification and verification of Sprint and daily tasks need to be assured within the Sprint time frame. Daily testing is done on the new capability and regression tests must be done on previously tested features, so the regression test set builds up as the Sprint progresses. Generally, an automated process is used for testing. At the end of the Sprint, the code and any supporting products such as documentation and test suites needed to meet the definition of “Done” as determined by the Project are saved.  Daily regression testing needs to be updated with new features and functions.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan), * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.10 - Related Activities](/spaces/SWEHBVD/pages/146539354/7.10+-+Related+Activities) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is essential for software assurance (SA) to verify compliance with regression testing requirements. Below are the types of objective evidence that may be collected and evaluated for demonstrating adherence to this requirement:

---

### **1. Documentation and Plans**

1. **Software Test Plan (STP)**

   * Contains the project's test strategy, including plans for regression testing.
   * Describes the criteria for selecting regression test cases and the scope of regression testing.
   * Documents how regression testing integrates into the testing lifecycle (e.g., unit testing, system testing, integration testing).
   * Reference: SWE-065 - Test Plan.
2. **Change-Impact Analysis Report**

   * Identifies the areas of the software affected by changes and highlights the corresponding tests selected for regression.
   * Documents analysis on how the changes may impact other areas of the system or introduce risks (functionality, performance, safety, security).
3. **Requirements Traceability Matrix (RTM)**

   * Demonstrates traceability from software changes to impacted requirements and corresponding test cases in the regression test set.
   * Confirms that all modified and safety-critical requirements are covered by regression testing.
   * Reference: SWE-052 - Software Verification Requirements.
4. **Configuration Management Records**

   * Shows version history of the software code, regression test cases, and test data.
   * Evidence of baseline and post-change comparison for regression testing consistency.

---

### **2. Test Artifacts**

1. **Regression Test Procedures**

   * Defined test procedures for regression testing, including tests for altered functionality and ripple effects on related modules.
   * Evidence that safety-critical elements, performance bottlenecks, and operational limits are adequately tested.
2. **Regression Test Cases**

   * List of previously executed test cases being reused in the regression test set.
   * Include cases that verify:
     + Safety-critical operations.
     + High-risk areas of the software.
     + System boundary conditions.
     + Historical defects (confirmed fixed defects re-tested).
   * Includes prioritization of test cases based on change impact and risk assessment.
3. **Test Environment Configuration Reports**

   * Explain the setup for running regression tests, including hardware, software versions, and network dependencies.
   * Evidence that the same controlled environment used for initial testing is retained for regression testing.
4. **Regression Test Automation Scripts** *(if applicable)*

   * Includes evidence that automated regression efforts have been implemented for repeated test execution.
   * Scripting libraries or tools used to execute regression test cases.

---

### **3. Test Execution Artifacts**

1. **Regression Test Execution Records**

   * Logs from the execution of regression tests, including timestamps and the sequence of the test runs.
   * Evidence of test case execution results, including:
     + Passed Test Cases.
     + Failed Test Cases, with explanations.
     + Incomplete or blocked Test Cases (with justifications).
   * Includes regression test data (inputs, outputs, comparison baselines).
2. **Regression Test Reports**

   * Summarizes the results of the regression testing process, including:
     + Coverage analysis of the executed regression tests.
     + The current status of safety-critical functions and requirements.
     + Analysis of discrepancies between the test results and expected outcomes.
   * Allows comparison with results from previous regression test cycles to identify any degradation.
3. **Defect/Non-Conformance Reports** (NCRs)

   * Evidence of any non-conformances or defects found during regression testing.
   * Defect reports include information such as:
     + Severity, location, and impact of the defect.
     + Steps taken for resolution and retesting.
     + Evidence that the defect resolution process includes updating regression tests to prevent reoccurrence.
4. **Security Vulnerability Test Results**

   * Demonstrates that regression testing detected and validated changes related to cybersecurity vulnerability mitigations.
   * Evidence of retests to ensure no new security issues were introduced during software modifications.
   * Reference: SWE-156 - Evaluate Systems for Security Risks.

---

### **4. Verification and Risk Closure**

1. **Risk Logs**

   * Risks identified from change-impact analysis, regression test set selection, and execution, including:
     + Open risks being tracked.
     + Resolved risks, with evidence of mitigation.
     + Trends in risks (e.g., closure rate, recurring risks).
2. **Safety Test Records**

   * Evidence that regression testing includes verification of all safety-critical functionality as listed in SWE-205 - Determination of Safety-Critical Software.
   * Records demonstrating the safety tests validate proper function under abnormal scenarios (e.g., system overload, invalid inputs).
3. **Requirements Validation Records**

   * Evidence that regression testing fulfills updated or modified requirements.
   * Evidence of validated software work products and test procedures.
4. **Cybersecurity Test Logs**

   * Evidence that regression tests validate all updated cybersecurity requirements or mitigations identified in the test plan.
   * Vulnerability scans or penetration tests may be part of this evidence.

---

### **5. Lessons Learned and Continuous Improvement**

1. **Lessons Learned Documentation**

   * Documents issues or challenges faced during regression testing, mitigation efforts, and improvements for future test cycles.
   * Evidence that this information feeds into future regression testing plans.
2. **Post-Test Analysis Reports**

   * Reports comparing current test results with historical baselines or prior regression test cycles to analyze trends (e.g., recurring issues, improvements in defect density).
3. **Updated Regression Test Suites**

   * Records showing that the regression test suite is updated to include new test cases addressing recently fixed issues, areas of repeated failure, or untested functionalities.
4. **Test Process Review Records**

   * Audit records or walkthrough logs showing that the regression test process, selection strategy, and execution have been reviewed and approved.

---

### **6. Metrics Supporting Compliance**

SA collects and tracks metrics that provide quantitative evidence of regression testing effectiveness. Examples include:

* **Test Coverage**:
  + **# of tests planned vs. # of tests executed.**
  + **# of executed regression tests vs. # of planned regression tests.**
  + **% of regression tests tied to safety-critical requirements.**
* **Defect Metrics**:
  + **# of defects or non-conformances identified during regression testing.**
  + **# of historical issues prevented in current testing.**
  + **% of defect fixes verified by regression tests.**
* **Risk Metrics**:
  + **# of risks identified during regression testing vs. # of risks mitigated.**
  + **Trend of risks (Open, Closed, or Severe) over time.**
* **Performance Metrics**:
  + **Comparison of current test results to historical baselines (e.g., execution time, defect density, system performance metrics).**
  + **Mean time to close test-related defects or risks.**

---

### **Conclusion**

Objective evidence is necessary to instill confidence in the effectiveness of regression testing and to ensure compliance with project requirements, including safety, performance, and security goals. By carefully collecting and reviewing the above artifacts, SA can validate that regression tests are planned, executed, and analyzed properly, thereby minimizing software risks and ensuring prior functionality remains intact after changes.

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
