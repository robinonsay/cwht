# SWE-186 - Unit Test Repeatability

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695522. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability

SWE-186 - Unit Test Repeatability

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695522)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695522&showCommentArea=true&showComments=true#addcomment)

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

4.4.6 The project manager shall assure that the unit test results are repeatable.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-186 History

SWE-186 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.4.6 The project manager shall assure that the unit test results are repeatable. |
| Difference between C and D | No change |
| D | 4.4.6 The project manager shall assure that the unit test results are repeatable. |

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
| * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) |

# 2. Rationale

Unit test procedures are to be repeatable so that future runs can confirm that any identified flaws have been corrected and for regression purposes to ensure that any new changes do not introduce new flaws in the software. As stated in [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test),  unit testing can be described as the confirmation that the unit performs the capability assigned to it, correctly interfaces with other units and data, and represents a faithful implementation of the unit design.

The project manager is required to ensure that unit test results are **repeatable**—that is, the same set of unit tests, when executed under the same conditions, should consistently yield the same outcomes. This ensures the reliability and validity of the testing process and confirms the robustness of the software under test. The rationale for this requirement is grounded in the need for consistency, defect isolation, and quality assurance throughout the software development lifecycle.

---

#### **Key Reasons for Ensuring Unit Test Repeatability**

##### 1. **Promotes Confidence in Software Quality**

* Consistency in test results provides confidence that unit tests are trustworthy and accurately assess the unit’s behavior.
* Repeatable tests ensure that any failures or issues identified during testing are reproducible and not sporadic or random, making them easier to diagnose and resolve.
* Inconsistent results can mask defects or lead to wasted debug efforts.

##### 2. **Facilitates Debugging and Root Cause Analysis**

* Repeatable tests enable developers to reliably reproduce issues, which is essential for debugging and performing root cause analysis.
* Without repeatable results, developers cannot confidently isolate whether defects are due to the code under test, the test conditions, or the testing environment.
* Diagnosing the cause of failures is faster and more efficient when the conditions that produce them are predictable and consistent.

##### 3. **Minimizes Environmental Dependencies**

* Ensures that unit tests are not reliant on external factors such as hardware variations, network conditions, or other non-deterministic behaviors.
* Highlighting and reducing dependencies on external conditions helps to create a clean and controlled test environment in which only the software unit is being evaluated.

##### 4. **Supports Regression Testing**

* When code changes are made, rerunning unit tests is necessary to confirm that no new defects have been introduced (regression testing).
* Repeatable results ensure the validity of regression testing by providing conclusive evidence regarding whether a change has caused failures or impacted existing functionality.
* Inconsistent results undermine the value of regression testing and can lead to undetected regressions.

##### 5. **Improves Software Reliability, Especially for Safety-Critical Systems**

* For safety-critical software (e.g., software used to control spacecraft, medical devices, or autonomous systems), repeatability ensures that functional verification is robust enough to uncover critical errors.
* Failures in safety-critical systems can have catastrophic consequences, making precise and consistent testing outcomes a non-negotiable requirement.

##### 6. **Provides Objective Evidence for Validation**

* Repeatable results provide objective evidence to support software assurance, quality audits, and compliance verification processes.
* Ensures that any findings, defect corrections, or requirement verifications documented during testing can be readily reproduced during subsequent reviews or by independent evaluators.

##### 7. **Ensures Integrity of the Testing Process**

* Assures that the test procedures, scripts, and test cases themselves are reliable and free of errors or indeterminate behavior.
* Unreliable tests can lead to false positives (reporting failures when the software is correct) or false negatives (failing to detect issues) that compromise the integrity of the software and the testing process.

---

#### **Challenges This Requirement Addresses**

1. **Human and Environmental Factors**:  
   When test results are not repeatable, it may indicate that external or environmental conditions like hardware specifications, dependencies, or test setup are influencing test outcomes. This requirement addresses the need to control these external variables.
2. **Non-Deterministic Behavior**:  
   Non-deterministic behavior, such as race conditions or improper handling of concurrency, can result in inconsistent test results. Repeatable tests help identify and eliminate these risks.
3. **Configuration Overlaps**:  
   Differences in test environments or misconfigurations (e.g., missing files, incorrect system paths, or outdated dependencies) can create variability. Enforcing repeatability highlights and removes such inconsistencies.

---

#### **Practical Implications of the Requirement**

* **Repeatability Encourages Automation**:  
  Automated test suites, when designed correctly, inherently prioritize repeatability as they eliminate human interaction and external biases during test execution.
* **Helps Establish Test Baselines**:  
  Repeatable results allow projects to create a **baseline** set of test outcomes that can be reliably compared against future executions to track progress and detect violations of expected behaviors.
* **Supports Collaboration Across Teams**:  
  Reliable and repeatable unit tests allow multiple teams (e.g., development, quality assurance, software assurance, and integration teams) to share test artifacts and results, ensuring consistency across environments and processes.

---

#### **Connection to NASA’s Mission and Standards**

1. **Mission Success**:

   * NASA's software is often deployed in environments where failures can be catastrophic. Repeatable unit testing ensures that every function behaves predictably and reliably, reducing the likelihood of mission disruptions caused by unexpected software failures.
2. **Alignment with NASA Standards**:

   * NASA's software engineering practices emphasize verification, validation, and configuration control. Repeatable unit tests are key to ensuring that software adheres to its requirements and performs as expected under the defined conditions.
   * This requirement aligns with [SWE-186 - Unit Test Repeatability](https://chat.nasa.gov/chats) and [SWE-219 - Code Coverage for Safety-Critical Software](https://chat.nasa.gov/chats), which highlight the importance of robust testing processes.
3. **Compliance with Lessons Learned**:

   * The requirement directly addresses historical lessons learned from NASA missions, such as ensuring that all test cases account for the full range of expected parameters and that code is thoroughly retested after changes (e.g., Mars Polar Lander and auto-code experiences). Repeatability ensures these critical lessons are applied effectively.

---

#### **Conclusion**

Repeatable unit test results play a foundational role in delivering high-quality, reliable, and safe software. This requirement helps ensure that test outcomes are consistent, trustworthy, and not influenced by irrelevant factors. By enforcing repeatability, the project manager ensures that software defects are easier to identify, regression testing remains meaningful, compliance with requirements is verifiable, and NASA’s safety-critical mission goals are upheld.

# 3. Guidance

## 3.1 Performing Unit Tests

Unit testing serves as the first line of defense against software defects, ensuring individual units of code perform as intended before integration with other components. This guidance incorporates best practices for preparing, performing, documenting, and evaluating unit tests, while addressing the specific considerations for NASA projects, particularly safety-critical software.

Unit tests should be performed in accordance with [SWE-062 - Unit Test](https://chat.nasa.gov/chats), ensuring that the results are repeatable for consistent quality and validation. The definition of a **unit** is central to understanding the scope of unit testing:

#### **Definition of a Unit (From IEEE STD 610.12-1990)**:

1. **A separately testable element** specified in the design of a computer software component.
2. **A logically separable part** of a computer program.
3. **A software component** that is not subdivided into smaller components.

Given the low-level and specific nature of software units, the **developer who implements the unit** is typically best positioned to fully understand its behavior and ensure thorough testing. That said, to ensure objectivity and rigor, results should also be evaluated by individuals other than the original developer (peer reviews or software assurance personnel).

Repeatability is essential: unit test results must follow test procedures and produce the same outcomes under identical conditions, in alignment with [SWE-186 - Unit Test Repeatability](https://chat.nasa.gov/chats).

---

## 3.2 Preparing for Unit Testing

Proper preparation is critical for meaningful and robust unit testing. Projects must ensure that the necessary test environments, tools, materials, training, and plans are in place before executing unit tests. Key preparatory steps include:

#### **1. Establishing the Unit Test Environment**

* Set up a test environment that matches, as closely as possible, the actual operating conditions of the software, including relevant inputs, outputs, and external stimuli.
* Document and control the test environment configuration to prevent inconsistency or variation in the test results.
* Identify and document any **gaps or differences** between the test environment and the target operational environment (e.g., hardware, dependencies). Such differences must be considered when evaluating test results.

#### **2. Ensuring Detailed and Approved Plans**

* Conduct unit tests **per the approved Software Test Plan (5.10 - STP)** and ensure the plan:
  + Defines success criteria for each test.
  + Identifies test cases that cover boundary values, nominal conditions, off-nominal conditions, and edge cases.
  + Details the schedule for testing per [SWE-016 - Software Schedule](https://chat.nasa.gov/chats).
  + Includes monitoring guidelines for software assurance as detailed in the Software Assurance Plan.

#### **3. Establishing Test Artifacts**

* Prepare all necessary **test drivers, test stubs, scripts, and test data.** These artifacts should be designed for repeatability and reuse to support both initial and regression testing.
* Provide appropriate training for all team members involved in testing, as highlighted in [SWE-017 - Project and Software Training](https://chat.nasa.gov/chats), to ensure they fully understand the tools, methods, and objectives of the unit test phase.

---

## 3.3 Conducting Unit Testing

Following proper preparation, unit testing executes procedures that systematically evaluate the unit’s functionality and robustness. Testing should:

1. **Capture Test Results:**

   * Record outcomes and compare actual results to expected results based on the approved test procedures.
   * Document any differences or unexpected behaviors, even if minor, for further evaluation.
2. **Track and Correct Issues:**

   * For every anomaly or failure identified, generate a defect report and determine the root cause. Common issues include:
     1. Problems in the unit's code (e.g., logic errors, boundary issues).
     2. Problems in the test tools or instruments (e.g., incorrect scripts, invalid data).
     3. Issues in the test environment configuration.
   * Once issues are resolved, **retest units** to verify that the corrective actions were effective, ensuring no new issues were introduced.
3. **Evaluate and Review Results:**

   * Test results must undergo evaluation by a reviewer independent of the tester (e.g., peer reviews or Quality Assurance personnel).
   * Ensure that evaluations confirm compliance with the test objectives and document the evaluation outcomes for traceability.
4. **Capture Supporting Artifacts:**

   * Maintain **all test-related artifacts** for troubleshooting, audits, and regression testing, including:
     + Test data, scripts, test cases, procedures, test drivers, and test stubs.
     + Logs of test execution, including inputs used and outputs observed.
     + Engineer’s notes, observations, or annotations during testing.

---

## 3.4 Special Considerations for Safety-Critical Software

**Unit testing plays a crucial role for safety-critical modules,** as these modules often cannot be thoroughly tested during later integration or system tests due to their specific functionality or operational conditions. For safety-critical software:

1. Ensure that every safety-related requirement and functionality is covered comprehensively by unit tests.
2. Rigorously verify fault handling, boundary conditions, and off-nominal input scenarios.
3. Ensure that all safety-critical unit test cases are witnessed, reviewed, and documented as part of the evidence for safety assurance.

---

## 3.5 Evidence of Successful Unit Testing

To ensure compliance with [SWE-066 - Perform Testing](https://chat.nasa.gov/chats) and associated requirements, all relevant unit testing artifacts must be documented and stored securely. These artifacts include:

1. **Test Results and Evaluation Reports:**

   * Evidence that each unit test was executed.
   * Clear documentation of both successful and failed tests, including expected vs. actual results.
   * Evaluations or reviews performed by independent personnel, especially for high-risk or safety-critical tests.
2. **Problem and Defect Reports:**

   * Detailed reports of identified issues, including their resolution and verification.
3. **Configuration Evidence:**

   * Versioning of the unit under test, confirming that testing aligns with the correct codebase.
4. **Metrics and Traceability Reports:**

   * Metrics such as coverage (functional and code), pass/fail rates, and the outcome of regression tests.
   * Traceability matrix linking test cases to detailed software requirements.
5. **Test Records for Repeatability:**

   * Logs that confirm consistent results in repeated test executions under identical conditions.
6. **Software Development Folder (SDF) Entries:**

   * All artifacts (test data, scripts, defect reports, evaluations, etc.) properly stored in the designated project repositories as outlined in the Software Configuration Management Plan ([5.06 - SCMP](https://chat.nasa.gov/chats)).

---

## 3.6 Validating Repeatability

Once unit tests are completed, they should be executed again to ensure the results are **repeatable** under the same conditions. This validation step is critical for:

* Confirming the reliability and robustness of the test procedures and tools.
* Ensuring that subsequent changes or fixes did not introduce inconsistencies.
* Providing a foundation for establishing confidence in the repeatability of results, which is essential for safety-critical software certification.

By ensuring that unit tests and their results are fully repeatable, projects uphold software quality standards, reduce risks, and support future regression testing. This reinforces confidence that the software behaves as expected and meets the required level of trustworthiness, even for NASA’s most critical missions.

---

This improved guidance ensures proper planning, execution, and evaluation of unit tests while addressing the requirements of traceability, repeatability, and compliance. Meeting these best practices is crucial for delivering high-quality, reliable, and mission-ready software.

Unit tests are performed per [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test). Unit test results should follow test procedures and be repeatable.

IEEE STD 610.12-1990, IEEE Standard Glossary of Software Engineering Terminology, a "unit" is defined as:

1. A separately testable element specified in the design of a computer software component.
2. A logically separable part of a computer program.
3. A software component that is not subdivided into other components.

Given the low-level nature of a unit of code, the person most able to fully test that unit is the developer who created it.

## 3.7 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.8 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

For small projects, ensuring that unit test results are **repeatable** requires a streamlined approach that balances efficiency, minimal overhead, and adherence to quality assurance principles. The following guidance is tailored for smaller projects where resources, timelines, and complexity are more constrained than larger-scale initiatives but the need for robust and reliable software remains paramount.

---

### **Simplified Process for Small Projects**

While the core concepts remain the same, small projects can simplify unit testing by focusing on key principles:

---

#### **1. Keep Tests Small and Focused**

* **Guidance**: Write unit tests that cover small, logically separable parts of functionality. Ensure each test targets a specific behavior, function, or logic branch. Smaller tests are easier to understand, maintain, and repeat.
* **Practice**:
  + For example, if a function calculates the sum of two numbers, create one test case for nominal values (e.g., `2 + 2`), one for extreme values (e.g., `INT_MAX + 1`), and one for non-standard inputs (e.g., a string).
  + Limit complex test conditions to the most critical scenarios, focusing testing on key areas of risk.

---

#### **2. Use Automated Testing Tools**

* **Guidance**: Automate unit tests wherever possible to minimize manual intervention and ensure repeatability. Automation reduces human error and allows tests to be re-run reliably on demand.
* **Tools for Small Projects** (choose lightweight and user-friendly tools):
  + Use popular frameworks like **JUnit** (for Java), **PyTest/UnitTest** (for Python), **CppUnit** (for C++), or **NUnit** (for .NET).
  + Consider simple Continuous Integration (CI) tools (e.g., **GitHub Actions** or **GitLab CI**).

---

#### **3. Simplify the Test Environment**

* **Guidance**: For small projects, focus on ensuring that the **test environment is consistent** and easy to duplicate.
* **Small Project Practices**:
  1. Use **mocking libraries** or test doubles for external dependencies (e.g., databases, APIs) to create a controlled test environment. Tools like **Mockito** (Java), **unittest.mock** (Python), or **FakeIt** (C++) are lightweight options.
  2. Document the environment setup clearly, such as specific versions of compilers, libraries, or configurations required.
  3. When possible, use **containerized environments** (e.g., Docker containers) for easy replication.
  4. Avoid dependencies on hardware that are difficult to replicate—use simulations if real hardware is required only for integration testing.

---

#### **4. Define Clear Success Criteria for Each Test**

* **Guidance**: Ensure that each test has predefined success criteria. Test outputs need to be explicitly compared to expected values. This provides clear evidence of repeatability.
* **Practices**:
  + Use assertions within test scripts to verify if actual results match the expected ones. (E.g., `assertEqual(actual, expected)` in Python.)
  + Document edge cases and criteria (e.g., **boundary tests**, invalid inputs).

---

#### **5. Keep Tests Repeatable and Deterministic**

* **Guidance**: Ensure that tests produce the same results if the code and test environment are unchanged. Random or inconsistent behavior undermines test repeatability.
* **Practices**:
  + Avoid using non-deterministic or time-dependent logic in unit tests (e.g., functions that rely on the current timestamp should use fixed or mocked dates instead).
  + Randomized inputs should use fixed seeds (e.g., setting a known random number generator seed).

---

#### **6. Keep Documentation Lightweight but Useful**

* **Guidance**: Document the testing process and results without introducing excessive overhead. For small projects, concise and focused documentation suffices.
* **Practices**:
  + Use templates to record test results, e.g.:
    - Test ID
    - Test description
    - Input data and parameters
    - Expected output
    - Actual output (when running the test)
    - Pass/Fail status
  + Store test results in a version-controlled repository alongside the code for traceability and easy access during audits.

---

#### **7. Review Results for Objectivity**

* **Guidance**: Even in small teams, ensure there is a second pair of eyes (e.g., another developer or software assurance engineer) who reviews and validates the test results. Independent reviews help identify issues and ensure repeatability.
* **Practices**:
  + Use **peer reviews** or lightweight code reviews to confirm test results and ensure results meet the success criteria.
  + Document informal evaluation findings in a shared space (e.g., team Confluence, GitHub issues, or lightweight meeting minutes).

---

### **Step-by-Step Implementation for Small Projects**

1. **Test Planning**

   * Write only the tests defined in a lightweight **unit test plan** (or include unit testing naturally in a broader development plan).
   * Focus testing on:
     + Core functionality or high-risk areas.
     + Edge cases and important boundaries (especially for **safety-critical units**).
2. **Test Execution**

   * Use automated scripts to execute tests in a controlled environment to ensure consistent results.
   * Rerun tests immediately after changes are made (e.g., bug fixes or small enhancements) to verify **repeatability** and avoid introducing regressions.
3. **Test Result Validation**

   * Confirm that test execution output matches expected results. A simple **pass/fail log** is sufficient for smaller efforts.
   * Automated systems reduce overhead by auto-generating logs and result comparisons.
4. **Document Results and Evidence**

   * Store test results (e.g., pass/fail logs, comparisons, screenshots, or defect tickets) in a lightweight and accessible repository.
   * Use version control (e.g., Git) to document code versions associated with test outcomes.
5. **Fix and Re-run Tests**

   * If issues are found, document them briefly and fix the underlying cause.
   * Rerun tests to validate that corrections have resolved the issues and confirm repeatability.

---

### **Safety-Critical Software Considerations**

Even on small projects, **safety-critical software** requires additional effort to ensure robustness:

1. Identify which units have **safety-critical functions** and prioritize their testing. These tests should have high coverage (e.g., **MC/DC or decision coverage**) and be reviewed independently.
2. Ensure the test results for these units are fully documented and auditable, including comparisons to requirements and hazard analyses.
3. Incorporate tests for fault handling and error scenarios, ensuring repeatability under both **normal** and **off-nominal conditions**.

---

### **Example Tools and Techniques for Small Projects**

* **Version Control**: Ensure both the test scripts and the code under test are version controlled (e.g., Git).
* **Lightweight CI Systems**: Set up simple automated pipelines (e.g., GitHub Actions, GitLab CI, Bitbucket Pipelines) to ensure repeated executions automatically verify test results.
* **Automation Frameworks**: Use frameworks suitable for the language in use (e.g., PyTest, JUnit, NUnit).
* **Mocking/Simulation Tools**: Use test doubles (mock objects or simulated resources) to avoid dependencies that affect repeatability.

---

### **Approach to Evidence Collection (Minimal Overhead)**

For small projects, evidence collection should focus on practical and lightweight logging/documentation:

1. **Test Logs**: Automatically collect logs for each test run using the testing tool or script.
2. **Screenshots/Outputs**: Save evidence like screenshots or textual outputs for manual tests.
3. **Defect Tracker**: Use a simple tracker (e.g., Excel, JIRA, or GitHub Issues) to log problems, fixes, and resolution verification.
4. **Central Repository**: Store artifacts (e.g., test plans, logs, scripts, and results) in a single, shared location for version control.

---

### **Conclusion**

Small projects can adhere to the requirement for repeatable unit tests by leveraging automation, focusing on simplicity, and documenting results in accessible, lightweight formats. Ensuring consistency and repeatability in unit test results provides confidence in software functionality, supports debugging, and minimizes the risk of defects propagating to later development phases.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-013) "Code and Unit Test,"  HOU-EGP-310, Boeing, 2002. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

Ensuring unit test results are **repeatable** is critical for uncovering defects early, validating fixes, and building confidence in software reliability. NASA has gathered numerous lessons learned from past projects and missions that emphasize the importance of unit testing and repeatability. These lessons highlight the potential risks of inadequate unit testing and provide insights on how to prevent issues that can affect mission success. Below are relevant NASA lessons learned associated with this requirement:

---

### **1. Lesson Learned: Testing Early and Rigorously**

* **Lesson ID:** [0939: MPL Software/Test Errors](https://llis.nasa.gov/lesson/0939)
* **Summary:**
  + The Mars Polar Lander (MPL) mission experienced software errors that contributed to mission failure. These errors were partially due to insufficient unit testing that failed to adequately verify the functionality of individual components.
  + Unit test results were inadequate to detect certain failure modes in edge-case scenarios or off-nominal conditions. Testing was not repeatable or robust enough to ensure proper system functionality under all expected conditions.
* **Key Takeaways:**
  + Unit tests must rigorously verify software functionality at the **lowest level**, especially edge cases and boundary conditions. Repeatability ensures that defects are consistent and can be isolated early rather than being passed to integration.
  + Tests should be re-run after any code changes (regression testing), and discrepancies in results must be documented and resolved.
  + During the MPL mission, issues in error-handling functions occurred partly because they were inadequately tested in a safe, isolated environment.

---

### **2. Lesson Learned: Faulty Use of Auto-Code Tools**

* **Lesson ID:** [1298: Auto-Code Tools](https://llis.nasa.gov/lesson/1298)
* **Summary:**
  + Auto-code generation tools were used to develop software in a NASA mission, but insufficient unit testing for the auto-generated code led to functional issues being discovered late in development, when integration testing was conducted.
  + Issues arose from a lack of repeatable and controlled unit tests to verify behavior after each code iteration. Problems surfaced when auto-code outputs changed unexpectedly due to updates in the auto-code tool or minor changes in input parameters.
* **Key Takeaways:**
  + Unit testing must validate **auto-generated code** repeatedly to ensure that outputs are consistent across tool versions and changes. Test repeatability is crucial for verifying that updates do not introduce variances or regressions.
  + Projects should capture **baseline test results** early and rerun tests after each change to compare outcomes.

---

### **3. Lesson Learned: Software Insufficiently Tested for Safety-Critical Functions**

* **Lesson ID:** [5390: Unit-Level Testing of Software](https://llis.nasa.gov/lesson/5390)
* **Summary:**
  + A NASA safety-critical software project identified severe defects that arose because individual software modules were not fully tested. Errors in **fault-tolerant functions** were missed because unit testing was inconsistent and outputs were not compared across repeated runs.
  + Some functional areas were tested only during integration, leaving unit-level details unverified and resulting in missed or latent defects.
* **Key Takeaways:**
  + Safety-critical software requires **rigorous and repeatable unit tests** because integration testing cannot fully exercise individual components.
  + Repeatability in safety-critical unit tests ensures the reliable identification and resolution of faults. Discrepancies in test outcomes must be investigated fully.
  + Unit tests are particularly valuable for **off-nominal conditions**, as these scenarios may be impossible to reliably simulate at the system level.

---

### **4. Lesson Learned: Lack of Formal Test Procedures**

* **Lesson ID:** [0794: Formal Test Procedures](https://llis.nasa.gov/lesson/0794)
* **Summary:**
  + Formal test procedures were deemed insufficient for several NASA missions, leading to test results that were inconsistent and difficult to replicate.
  + Informal testing methods failed to ensure repeatability, especially for software modules with complex dependencies, producing unreliable results and masking defects.
* **Key Takeaways:**
  + Repeatable test procedures must be **formalized**, clearly documented, and adhered to, to ensure that tests yield consistent results under identical conditions.
  + Informal or ad hoc testing introduces errors and inconsistencies that compromise the ability to reliably verify changes or fixes.
  + Lightweight processes (formal yet simple) are preferable for smaller projects to maintain repeatability without adding significant overhead.

---

### **5. Lesson Learned: Regression Testing for Software Changes**

* **Lesson ID:** [1216: Regression Testing](https://llis.nasa.gov/lesson/1216)
* **Summary:**
  + A software project encountered multiple regressions after changes were made to the code without rerunning unit tests. This led to costly bug fixes late in system testing and integration phases.
  + Unit test results were inconsistent because regression testing was not performed after incremental updates, and discrepancies between test results were not investigated adequately.
* **Key Takeaways:**
  + Unit test results must be repeated following **any changes to the code**, configuration, test environment, or dependencies.
  + Regression testing is essential to confirm that changes do not introduce new defects or modify existing functionality. Using automated tests is key to ensuring repeatability during regression testing.

---

### **6. Lesson Learned: Inadequate Edge-Case Testing**

* **Lesson ID:** [1341: Edge Cases in Unit Tests](https://llis.nasa.gov/lesson/1341)
* **Summary:**
  + During a NASA ground software project, defects were found in edge-case scenarios because unit testing did not adequately cover boundary values or non-standard inputs.
  + Non-repeatable tests resulted in inconsistent results when edge cases were tested multiple times, making it difficult to pinpoint failures reliably.
* **Key Takeaways:**
  + Unit tests must consistently validate edge cases and anomalous inputs, ensuring that results are repeatable across runs.
  + Failing to execute repeatable tests for **edge cases** risks allowing latent defects to propagate to later testing phases when they are harder and costlier to fix.

---

### **7. Lesson Learned: Lack of Repeatability in Hazard Analysis Testing**

* **Lesson ID:** [2048: Hazard Analysis Testing](https://llis.nasa.gov/lesson/2048)
* **Summary:**
  + A spacecraft software component failed to respond as expected in hazardous conditions due to insufficient unit testing of its hazard mitigation functions. Unit tests for hazard-related code were inconsistent and not repeatable, leading to missed opportunities to catch defects early.
* **Key Takeaways:**
  + Hazard-related software functions must undergo **repeatable unit testing** to confirm their reliability across multiple runs.
  + These tests are especially important for verifying that hazard mitigation logic works correctly under **both nominal and off-nominal conditions**.
  + Repeatability ensures that evidence of successful hazard-handling results can be confidently presented for safety certifications.

---

### **Summary of NASA Lessons Learned**

Unit test repeatability is consistently highlighted in NASA lessons learned as a key factor in ensuring software reliability, uncovering defects early, and preventing regressions. These lessons emphasize that repeatable tests support the following principles:

1. **Early Defect Identification**: Repeatability ensures that unit-level issues can be isolated and resolved before integration, reducing costs later in development.
2. **Safety Assurance**: Safety-critical software must undergo rigorous and repeatable unit testing to meet mission-critical reliability standards.
3. **Regression Testing**: Unit tests must be rerun after code changes to confirm that functionality remains consistent and no new defects are introduced.
4. **Edge Case Validation**: Repeatable tests help verify software behavior under extreme conditions or abnormal inputs.
5. **Validation via Documentation**: Repeatable tests support audits and reviews by providing reliable, traceable evidence of defect resolution and requirements compliance.

By incorporating repeatability into unit testing practices, NASA ensures that its software systems meet the stringent reliability and safety requirements necessary for mission success.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-186 - Unit Test Repeatability**

4.4.6 The project manager shall assure that the unit test results are repeatable.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project maintains the procedures, scripts, results, and data needed to repeat the unit testing (e.g., as-run scripts, test procedures, results).

## 7.2 Software Assurance Products

This guidance expands and clarifies the responsibilities of software assurance (SA) in verifying the quality and repeatability of unit tests, ensuring that issues found during unit testing are effectively addressed and that test results are reliable, consistent, and documented. Repeatability is critical for identifying defects, confirming fixes, and providing confidence in the software's readiness for integration and system-level testing.

---

Software assurance plays an integral role in ensuring the repeatability and validity of unit test results. The following products should be generated and monitored by SA as part of the assurance of unit testing:

#### 1. Unit Test Results

* The actual results of all unit tests, including:
  + Pass/fail outcomes for each test case.
  + Observed vs. expected outputs for all tests.
  + Logs or reports generated by test automation or manual testing.
* Any inconsistencies in repeated test executions should be flagged by SA.

#### 2. Software Problem or Defect Reports

* Findings related to issues identified during unit testing should be:
  + Recorded in a defect tracking system.
  + Linked directly to the test case(s) that revealed the defect.
  + Categorized by severity, including priority for safety-critical defects.
* SA ensures that defect reports adequately describe the cause, resolution, and verification of each issue.

#### 3. Unit Test Configuration Data

* All configuration details associated with the execution of unit tests. This includes:
  + The version of the software tested.
  + The tools, operating systems, and environments used.
  + Documentation of any differences between the unit test environment and the intended operational environment.

By collecting and reviewing these products, software assurance ensures that the unit tests meet the requirements of completeness, traceability, and repeatability.

---

## 7.3 Metrics

Metrics provide insight into the effectiveness, coverage, and consistency of the unit test process. Software assurance should monitor and evaluate the following key metrics for unit testing:

#### **1. Test Case Metrics**

* **# of Planned Unit Test Cases vs. # of Actual Unit Test Cases Successfully Completed**
  + Tracks whether the planned scope of unit testing has been fully executed and identifies gaps where test cases were not completed successfully.

#### **2. Safety-Critical Test Metrics**

* **# of Safety-Critical Tests Executed vs. # of Safety-Critical Tests Witnessed by SA**
  + Ensures SA oversight in the execution of safety-critical unit tests to confirm adherence to project safety requirements and compliance with standards.

#### **3. Repeatability Metrics**

* **# of Test Cases Re-run vs. # of Test Cases Repeatable Without Discrepancy**
  + Measures the consistency of test results when tests are re-executed under identical conditions. This identifies reliability issues in either the test setup or the unit under test.

#### **4. Defect Metrics**

* **# of Defects Found During Unit Testing vs. # Resolved and Retested**
  + Tracks the resolution of issues and verifies that defects identified during testing have been properly corrected and confirmed through retesting.

#### **5. Coverage Metrics**

* **Code Coverage (e.g., Statement, Branch, or MC/DC for Safety-Critical Software)**
  + Tracks how thoroughly the code is tested, ensuring all logical paths, decisions, and conditions are exercised.

#### **See Also**: [Topic 8.18 - SA Suggested Metrics](https://chat.nasa.gov/chats)

---

## 7.4 Guidance for Assuring Unit Test Repeatability

Software assurance plays a key role in ensuring that unit tests are repeatable. SA verifies that tests produce consistent and reliable results when repeated under the same conditions. To achieve this, SA should ensure that the following items are recorded, reviewed, and stored in accordance with project standards and requirements:

---

#### **1. Test Cases and Procedures**

* **What SA Ensures**:
  + Unit tests are executed in accordance with the approved test procedures.
  + Test cases represent all planned inputs, outputs, boundary conditions, and corner cases relevant to the unit under test.
  + Automated test scripts are verified for consistency and reliability.

---

#### **2. Input Data and Stimulus**

* **What SA Ensures**:
  + All input data and external stimuli required during testing are recorded and reproducible.
  + Dependencies such as input databases, static datasets, or mock configurations used in the test environment must be controlled and well-documented.
  + Any special input conditions, randomized inputs, or external resource mocks are captured and repeatable.

---

#### **3. Test Environment and Configuration**

* **What SA Ensures**:
  + **Configurations Captured**: Versions of the operating systems, compilers, libraries, tools, and other dependencies used in the testing process.
  + Any differences between the **unit test environment** and the intended **target operational environment** (e.g., hardware vs. simulation) are noted and assessed for their impact on test validity.
  + Test executions are tracked to the specific version of the unit being tested (e.g., build numbers or commit hashes).

---

#### **4. Test Artifacts**

* **What SA Ensures**:
  + Test drivers, stubs, and custom test scripts used during unit testing are documented, controlled, and stored for future audit or reuse.
  + Build instructions, test procedures, and test execution instructions are clearly documented to ensure precise replication of the test process.
  + Captured execution logs (e.g., standard output, error messages, debugging information) are stored for traceability and issue evaluation.

---

#### **5. Test Results and Discrepancies**

* **What SA Ensures**:
  + Expected vs. actual results for all test cases are documented. Any mismatches are flagged and thoroughly reviewed.
  + Discrepancies, anomalies, or unexpected behaviors are logged in problem reports and tracked to resolution.
  + Test reports summarize results for all executed test cases, including any failed tests and their corresponding defect reports.

---

#### **6. Responsible Oversight by SA**

* **What SA Ensures**:
  + Verification of test repeatability:
    - Tests must consistently produce identical results under the same environmental conditions and with the same input data.
    - For any failures that are not repeatable, the root cause must be identified (e.g., issues in the unit under test, ambiguities in the test procedure, or environmental instability).
  + Independent evaluation of test procedures and results:
    - SA personnel confirm that test results meet the pre-defined success criteria and that testing aligns with the project's objectives and engineering standards.
  + Regression testing:
    - Unit tests are re-run after any code changes to validate fixes and confirm no new defects have been introduced.

---

#### **7. Objective Evidence for Compliance**

Software assurance ensures the project provides **objective evidence** of unit test execution and repeatability. The following artifacts should be available and stored in the project repository for oversight:

1. **Test Cases and Procedures**: The unit test cases, approved test procedures, and test input/output data.
2. **Test Results/Logs**: Pass/fail logs, execution records, and outputs covering nominal, edge-case, and off-nominal scenarios.
3. **Defect Reports**: Anomalies, discrepancies, issues, and their resolutions, tracked via controlled problem reports.
4. **Configuration Records**: Test environment documentation, including all tools and software versions used during testing.
5. **Verification of Repeatability**: Evidence that tests were repeated successfully after code changes or during regression testing.

---

### **Additional Considerations**

* For **safety-critical software**, SA ensures that test repeatability is particularly rigorous and tests explicitly cover failure scenarios, fault handling, and hazard-related functionality.
* SA should periodically review the unit testing process itself, not just the outputs, to confirm that testing practices are sufficient for ensuring repeatability and robust defect detection.

By ensuring the proper recording, review, and evaluation of unit test artifacts, software assurance validates the consistency and reliability of unit testing and supports the overall quality and safety of the project.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)        * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is vital to demonstrating compliance with the requirement that unit test results are repeatable. Well-documented and verifiable evidence ensures that stakeholders, reviewers, and auditors have confidence in the quality and reliability of the unit testing process. Below are practical examples of objective evidence that support this requirement, categorized for clarity.

---

### **1. Test Cases and Procedures**

* **Artifacts**:
  + Approved test procedures outlining the detailed steps for executing unit tests (e.g., setup instructions, inputs, execution rules, expected outputs).
  + Individual test cases, including:
    - Test descriptions (what functionality is being tested).
    - Inputs and expected outputs, including boundary and edge cases.
    - Success criteria (how a "pass" is determined).
  + Versioned test scripts (for automated testing) or manual test instructions.
* **Why It’s Important**: Ensures all tests have predefined steps and expectations, and that these procedures were followed during test execution.

---

### **2. Test Environment Documentation**

* **Artifacts**:
  + Environment setup details:
    - Operating system version and configuration.
    - Software versions (e.g., compilers, interpreters, libraries, dependencies).
    - Test tool versions (e.g., test automation frameworks or stubs).
  + Configuration control records:
    - Descriptions of any test modifications, such as simulated resources, stubs, or mocks.
    - Differences between the test environment (e.g., a lab or simulator) and the target operational environment (e.g., actual hardware).
* **Why It’s Important**: Ensures that the repeatability of test results is not compromised by changes or inconsistencies in the testing environment.

---

### **3. Test Execution Records**

* **Artifacts**:
  + Detailed execution logs:
    - State of the test environment at the time of test execution.
    - Input data applied during testing.
    - Test execution timestamps.
  + Test output logs:
    - Raw outputs generated by the software under test.
    - Comparison of actual to expected outputs.
  + Screenshots or console logs of test executions, particularly for manual testing.
  + Build logs showing the exact version of the software tested (including commit IDs or build numbers).
* **Why It’s Important**: Provides direct evidence of how tests were executed and what results were produced, allowing for detailed analysis and reproducibility.

---

### **4. Test Results and Reports**

* **Artifacts**:
  + Test result summaries for each unit, such as:
    - Pass/fail statuses.
    - Detailed results for each test case (e.g., success/failure, actual vs. expected outcomes).
  + Unit-level test reports:
    - Traceability to requirements (mapping test cases to specific software requirements or system-level needs).
  + Coverage reports (from tools such as LCOV, JaCoCo, or gcov):
    - Functional test coverage (which requirements are tested).
    - Code coverage (e.g., statement, branch, decision, and sometimes MC/DC for safety-critical software).
  + Discrepancy reports:
    - Records of all test failures, anomalies, or deviations from expected behavior.
* **Why It’s Important**: Provides evidence that all test outcomes are fully documented and evaluated, ensuring repeatability and compliance.

---

### **5. Regression and Re-Execution Evidence**

* **Artifacts**:
  + Logs showing that tests were re-executed under identical conditions and yielded consistent results.
  + Regression test execution records to verify that any modifications to the code did not compromise existing functionality.
  + Comparisons of test results before and after changes, demonstrating that results remain consistent (or discrepancies are explained).
* **Why It’s Important**: Confirms that test results are repeatable and that changes do not introduce new defects or inconsistencies.

---

### **6. Version Control and Configuration Management Records**

* **Artifacts**:
  + Software version metadata linked to test results:
    - Commit IDs, build identifiers, or other markers showing the relationship between the version of the software under test and the test results.
  + Configuration management logs for test-related artifacts:
    - Version-controlled test cases, scripts, drivers, stubs, inputs, outputs, and environmental configurations.
* **Why It’s Important**: Ensures that the specific context of each test execution is traceable and reproducible, even if changes are made to the test environment or the software under test.

---

### **7. Defect Logs and Problem Resolution Evidence**

* **Artifacts**:
  + Defect/problem reports for issues identified during unit testing:
    - Description of the issue (e.g., discrepancy between actual and expected results).
    - Link to the specific test case(s) that failed.
  + Root cause analyses:
    - Explanations of why the issue occurred and how it was resolved.
  + Test results demonstrating that the defect was successfully fixed and verified (retesting evidence).
* **Why It’s Important**: Ensures that every discrepancy is addressed, resolved, and tested again, and that resolution verification is repeatable.

---

### **8. Witnessing and Review Logs**

* **Artifacts**:
  + Logs of tests witnessed by software assurance (SA) representatives or other stakeholders:
    - Specific test cases or scenarios observed.
    - Actions performed by witnesses (e.g., signing off on results).
  + Peer reviews of test procedures, test scripts, and test results:
    - Review comments and evidence of resulting changes or updates to tests.
  + Independent evaluation reports by software assurance or quality personnel verifying repeatability.
* **Why It’s Important**: Documents third-party validation and ensures concurrence on the repeatability and correctness of test results.

---

### **9. Safety-Critical Test Evidence**

* **Artifacts**:
  + Evidence that safety-critical unit tests were executed with heightened rigor:
    - Coverage of fault-handling logic, off-nominal scenarios, and boundary cases.
    - Logs of witnessed safety-critical test runs.
  + Repeatability testing evidence for safety-critical units:
    - Confirmation that tests yielded consistent results even when conducted in different environments (e.g., simulated vs. actual hardware).
* **Why It’s Important**: Demonstrates that safety-critical software was tested under controlled conditions and that the results are reliable and repeatable.

---

### **10. Test Improvement and Lessons Learned Records**

* **Artifacts**:
  + Post-test evaluation reports identifying improvements to test processes:
    - Suggestions to improve the repeatability of tests in future iterations.
  + Lessons learned related to test failures, inconsistencies, or misconfigurations:
    - Root causes and mitigation measures for unreliability in testing.
* **Why It’s Important**: Drives continuous improvement in testing practices and ensures that repeatable test results can be reproduced more efficiently in subsequent phases.

---

### **Summary of Key Evidence**

The table below consolidates the primary artifacts that constitute objective evidence:

| **Category** | **Objective Evidence** |
| --- | --- |
| Test Cases and Procedures | Test descriptions, test scripts, planned test cases, success criteria, and automated/manual instructions. |
| Test Environment | Environment configurations, versions of OS/tools, and hardware/software differences documented. |
| Test Execution Records | Input data, raw outputs, execution logs, build logs, timestamps. |
| Test Results and Reports | Summaries, coverage reports, pass/fail logs, and discrepancy reports. |
| Regression and Re-Execution | Logs of test consistency when re-executed, and regression comparisons. |
| Configuration Records | Version-controlled test scripts, drivers, and software artifacts. |
| Defect Fixes | Problem reports, root cause analysis, and retest results. |
| Witness/SA Logs | Records of independent reviews, witnessing, and signed-off results. |

---

### **Conclusion**

Providing comprehensive, organized, and accessible objective evidence supports compliance with the requirement to ensure unit test repeatability. These artifacts not only demonstrate adherence to the requirement but also enable traceability, accountability, and continuous improvement in the testing process. By collecting evidence proactively, teams mitigate risks and strengthen confidence in software reliability, especially for safety-critical systems.

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
