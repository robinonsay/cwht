# SWE-193 - Acceptance Testing for Affected System and Software Behavior

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695528. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior

SWE-193 - Acceptance Testing for Affected System and Software Behavior

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695528)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695528&showCommentArea=true&showComments=true#addcomment)

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

4.5.13 The project manager shall develop acceptance tests for loaded or uplinked data, rules, and code that affects software and software system behavior.  

## 1.1 Notes

These acceptance tests should validate and verify the data, rules, and code for nominal and off-nominal scenarios.

## 1.2 History

Click here to view the history of this requirement: SWE-193 History

SWE-193 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW  Class A or B only |
| C | 4.5.13 The project manager shall develop acceptance tests for loaded or uplinked data, rules, and code that affects software and software system behavior. |
| Difference between C and D | No change |
| D | 4.5.13 The project manager shall develop acceptance tests for loaded or uplinked data, rules, and code that affects software and software system behavior. |

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

Any uploaded or uplinked data, rules, and code can affect the behavior of the software and/or system. Special acceptance tests should be developed to validate and verify the uplinked or uploaded information for nominal and off-nominal scenarios.

This requirement ensures that any **loaded or uplinked data**, **rules**, and/or **code** that affects **software and system behavior** is thoroughly tested to verify its correctness, safeguard system integrity, and prevent unintended consequences during operational use. This testing serves as a critical gate to ensure that data and software updates do not negatively impact system performance or introduce undetected faults to safety-critical systems.

---

### **Key Concepts Behind the Rationale**

#### **1. Ensuring Data and Code Integration Integrity**

* Loaded or uplinked data, rules, or code changes can alter or influence software behavior in real-time or during mission-critical operations.
* This requirement ensures that such externally introduced data and software are verified to:
  + Operate correctly with the existing system.
  + Maintain the expected functioning of the software and the system.
  + Avoid unintended interactions, bugs, or glitches.

### **2. Preventing Software, Logic, or Data Failures**

* Uplinks or real-time updates may include dynamic data such as:
  + Configuration files (e.g., mission parameters, sensor thresholds).
  + Control logic or rules (e.g., fault response conditions, command sequencing).
  + Software patches or small code modules that modify specific software behaviors.
* Errors in loaded or uplinked data (e.g., improper formats, corrupted files, incorrect thresholds) can lead to software faults that:
  + Trigger false alarms or inhibit expected responses (e.g., excessive noise or spurious signals).
  + Cause catastrophic behavior, such as loss of mission or harm to safety-critical systems.

---

#### **3. Uplinks Are Common in NASA Missions**

* NASA systems often require frequent data or rule updates, including:
  + Adjustments to spacecraft trajectory or control logic.
  + Modifications to onboard decision-making algorithms (e.g., hazard avoidance, fault handling).
  + Mission phases with unique data needs (e.g., landing sequences, deep-space maneuvers).
* These uplinks are integral to mission success and safety but also carry significant risks if errors are introduced. By thoroughly testing uplinked updates, the integrity of mission-critical systems is preserved.

---

#### **4. Mitigating the Risks of Uplinked Data and Code**

Errors caused by incorrect or untested uplinked data, rules, or code have historically resulted in mission failures. For example:

* Some missions failed due to improper or erroneous uplinked parameters controlling trajectory, sequencing, or subsystem responses.
  + Real-world example: The **Mars Climate Orbiter** mission failure was due to improper handling of metric and imperial unit conversions in transmitted data, emphasizing the need for stringent testing of incoming data.
* Other spacecraft experienced unexpected faults after receiving incorrect or poorly tested updates that caused system instabilities.

Acceptance testing helps eliminate these risks by ensuring all new data, rules, or code loaded into a system:

* Align with predefined requirements.
* Function safely and predictably under nominal and off-nominal conditions.
* Have been tested for full compatibility with existing software and hardware systems.

---

#### **5. Maintaining Consistency and Reliability in Critical Operations**

* Spacecraft and mission-critical systems operate in highly constrained, autonomous environments where even small changes to data or logic can cascade into significant issues.
* This requirement ensures the system remains reliable by:
  + Preventing updates from introducing behavior inconsistent with the mission objectives.
  + Validating that all modified system functionality complies with the intended rules and constraints.

---

### **Benefits of Acceptance Testing for Loaded/Uplinked Data, Rules, and Code**

1. **System Integrity and Safety:**

   * Validates that any updates to the system do not exacerbate existing hazards, introduce new ones, or compromise overall system integrity.
   * Prevents unintended or unsafe changes in behavior, especially in autonomous systems.
2. **Mitigation of Uplink-Related Errors:**

   * Identifies and corrects syntactical, logical, or data integrity errors before uplinks are accepted and applied to the system.
   * Reduces the risk of mission-critical errors caused by improper data, rules, or code.
3. **Operational Assurance:**

   * Ensures software continues to function within requirements despite dynamic updates during operations.
   * Validates that the system meets predefined behavioral expectations under both nominal and off-nominal conditions.
4. **Improved Mission Success Probability:**

   * Uplinked data, rules, and code frequently control time-critical and mission-defining events. By verifying their correctness, the likelihood of mission success is significantly enhanced.
5. **Compliance with Safety-Critical Standards:**

   * Ensures compliance with industry and NASA safety standards, particularly for software systems managing hazards, redundancy, or human safety.
6. **Error Isolation and Recovery:**

   * Acceptance testing provides an early opportunity to identify potential risks with loaded data or code before deployment or execution, enabling recovery and safeguarding the system environment.

---

### **Objective Goals of the Requirement**

Acceptance tests for loaded or uplinked data, rules, and code must accomplish the following:

1. **Verify Accuracy**:
   * Check that loaded updates match their design intent and specification requirements (e.g., correct values, formats, and units).
2. **Validate Behavior**:
   * Confirm that the software system behaves as intended after the update, under both nominal and stress conditions.
3. **Detect Malfunctions or Incompatibilities**:
   * Identify and address misalignments, bugs, or regressions resulting from newly introduced data or code.
4. **Ensure Safety and Quality**:
   * Validate that hazard mitigation controls or operational constraints remain intact and unaffected by changes.
5. **Provide Confidence**:
   * Demonstrate to stakeholders that new updates are thoroughly assessed, safe, and reliable.

---

### **Acceptance Testing Scope**

To meet the requirements for loaded or uplinked updates:

* **Test Loaded Data:**
  + Input data that affects thresholds, configuration parameters, and mission-specific directives.
  + Includes checks for format, range limits, and consistency.
* **Test Loaded Rules:**
  + Decision logic, if/then statements, runtime constraints, or onboard autonomy rules.
* **Test Loaded Code:**
  + Software modules, patches, or other system-level updates that directly affect software functionality and behavior.

---

### **Key Testing Activities**

1. **Unit Testing:**
   * Validate individual components of uplinked data or code at a granular level (e.g., format validation, data range checks).
2. **Integration Testing:**
   * Confirm compatibility between the updated data/code and the existing software environment.
3. **System-Level Testing:**
   * Assess the system’s overall behavior under real-world operational scenarios that mimic the effects of the uplink.
4. **Error Injection/Stress Testing:**
   * Simulate faults or extreme conditions to verify how the system performs after applying the update.
5. **Regression Testing:**
   * Ensure new updates do not break previously validated software functionality.

---

### **Historical Failures That Drive the Rationale**

1. **Mars Climate Orbiter (1999)**:

   * Root Cause: Miscommunication between teams caused metric-to-imperial conversions to fail. Faulty uplinked data went untested, leading to trajectory errors and mission loss.
   * Lesson: All uplinked data (especially those affecting critical mission operations) must be tested for accuracy, consistency, and compatibility.
2. **Ariane 5 Rocket Explosion (1996)**:

   * Root Cause: Unhandled overflow error in reused flight software. Code changes were not properly validated at an acceptance testing phase.
   * Lesson: Loaded code affecting on-system software must undergo rigorous acceptance testing to avoid catastrophic failures.
3. **Mars Polar Lander (1999)**:

   * Root Cause: Faulty decision logic caused premature shutdown of descent engines. Updates to autonomously loaded rules for descent behavior lacked sufficient testing.
   * Lesson: Decision-making rules require extensive validation to ensure they behave as intended under operational conditions.

---

### **Conclusion**

Requirement 4.5.13 emphasizes the critical need for thorough and rigorous acceptance testing of all loaded or uplinked data, rules, and code. By validating these updates prior to integration into operational systems, project managers and Software Assurance teams can prevent errors, maintain software integrity, and safeguard mission success. Historical incidents highlight the high stakes of overlooking such testing, and implementing this requirement remains crucial for safe, reliable, and effective mission execution.

# 3. Guidance

## 3.1 Acceptance Test

Acceptance testing is a critical milestone in ensuring the system-level readiness of software for its intended operations. It is typically performed during the final integration of formally tested software with flight or operational hardware prior to project-level acceptance.

**Objectives:**  
The primary purpose of acceptance testing is to validate that the software conforms to its requirements and works as intended in the end-system environment. This includes nominal and off-nominal operational scenarios to verify robustness.

**Key Considerations:**

* **System-Level Integration:** Acceptance tests should comprehensively evaluate the software's interactions with the system's hardware and other components to ensure seamless functionality.
* **Uplinked or Uploaded Data Impact:** Uploaded or uplinked data, such as configurations, rules, and code, can alter the behavior of the software/system. Special acceptance tests must be developed to validate and verify these inputs and their effects in both nominal and off-nominal conditions.
* **References for Supporting Processes:** Further guidance can be found in NPR 7123.1 (NASA Systems Engineering Processes and Requirements) and NASA-SP-2007-6105 (NASA Software Engineering Handbook).

**Related Requirements:**

* **SWE-034:** Define clear acceptance criteria that match system requirements.
* **Topic 8.01 - Off-Nominal Testing:** Pay special attention to scenarios that simulate unusual or fault conditions to ensure system resilience.
* **SWE-066 - Perform Testing and SWE-068 - Evaluate Test Results:** Ensure thorough execution and evaluation of acceptance tests for comprehensive validation.

---

## 3.2 Acceptance Criteria

The acceptance criteria for software development should be established early in the **Formulation phase** and must evolve alongside the growing understanding of system requirements.

**Steps for Effective Acceptance Criteria Development:**

1. **Initial Planning:**

   * Define initial acceptance criteria in the Software Development/Management Plan (SDP/SMP) or Software Verification & Validation (V&V) Plan.
   * Ensure criteria align with the project's objectives, stakeholder requirements, and system design.
2. **Iterative Refinement:**

   * Continuously review acceptance criteria throughout the project lifecycle to ensure alignment with real-world constraints and requirements as they evolve.
   * Adjust criteria to reflect refined system and software requirements during later phases of development.
3. **Documentation:**

   * Clearly document acceptance criteria and rationale to provide traceability, support decision-making, and assist stakeholders in understanding expectations.
4. **System Acceptance Review:**

   * Conclude acceptance activities with a formal System Acceptance Review (SAR) in the **Implementation phase**. Ensure entrance and exit criteria are met (see **Topic 7.09 - Entrance and Exit Criteria**).

---

## 3.3 Acceptance Testing

Acceptance testing verifies if the delivered software meets the pre-defined acceptance criteria and is fit for its intended operational use by the customer. It is a vital step before final project delivery.

**Acceptance Testing Workflow:**

1. **Test Design:**

   * Create a formalized acceptance testing plan, complete with a well-documented test suite covering nominal and off-nominal input conditions. Incorporate all uploaded and uplinked data validation scenarios to ensure comprehensive testing.
2. **Execution Environment:**

   * Conduct tests on the hardware and system environment intended for mission operations, ensuring the scenario is as close to the real-world environment as possible.
3. **Test Execution:**

   * Use a structured test suite to evaluate compliance with the acceptance criteria. Each test case should address specific requirements derived from the system specification.
4. **Personnel Involvement:**

   * Independent testing personnel are preferred to ensure unbiased evaluation. Software assurance personnel (e.g., Quality Assurance engineers) should observe to validate testing integrity.
5. **Outcome Evaluation:**

   * Compare observed results against predefined, expected results. Define acceptance tolerances for any variation.
   * If results meet criteria or fall within agreed tolerance bands, the software is accepted. Otherwise, the team documents deficiencies and either rejects the software or seeks conditional acceptance (e.g., delivering with known risks).
6. **Customer Agreement:**

   * Establish clear agreements between the development team and stakeholders to define thresholds for acceptance or conditional approval upfront.

---

## 3.4 Test Results

Documentation of test results is essential for maintaining project traceability, supporting future audits, and validating the acceptance decision.

**Key Guidelines for Reporting Results:**

1. **Verification Reports:**

   * Document all software verification results that support the acceptance review in comprehensive **Software Verification Reports**. Use these reports to demonstrate requirements compliance.
2. **Test Report or Data Package:**

   * Record the outcomes of all acceptance testing in a structured **Software Test Report (STR)** or **Acceptance Data Package**. Include:
     + Test objectives and acceptance criteria.
     + Test approach and methodology.
     + Detailed results for each test.
     + Deviations, failures, and follow-up actions.
     + Final recommendations on software acceptance.
3. **Transparency and Stakeholder Communication:**

   * Share documented test results with stakeholders, ensuring alignment on acceptance outcomes and next steps.

**Related References:**

* **STR - Software Test Report (Section 5.11):** Follow standards for presenting clear, complete test results documentation.

By adhering to these improved guidelines, the acceptance process will remain thorough, consistent, and well-documented, fostering successful delivery and operational deployment of software systems.

Acceptance Test (see [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria)) is a system-level test, usually performed during the final integration of formally tested software with the intended flight or operations hardware before Project level acceptance. Additional information may be found in NPR 7123.1 [041](#_tabs-<p></p>) and NASA-SP-2007-6105.  [273](#_tabs-<p></p>)

Uploaded or uplinked data, rules, and code may affect the behavior of the software and/or system. Special acceptance tests should be developed to validate and verify the uplinked or uploaded information for nominal and off-nominal scenarios. See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

See also [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results), 

## 3.5 Data Load Testing

Test data loads and configuration values are critical for validating the behavior and performance of software under realistic operational and edge-case conditions. Proper management of test data and configurations ensures the alignment of acceptance tests with real-world scenarios and reduces the risk of late-stage failures in deployment.

---

### **3.5 Test Data Loads and Configuration Values**

Test data loads refer to the datasets used for evaluating software during testing, while configuration values include the parameters, rules, and system settings that define and control software behavior. Both elements must be carefully designed, managed, and validated during the acceptance testing process to ensure meaningful and comprehensive software validation.

#### **Best Practices for Managing Test Data Loads and Configuration Values**

#### **1. Identification and Definition**

* **Align Test Data and Configuration with Requirements:**

  + Test data loads and configurations should reflect both nominal and off-nominal scenarios to verify all relevant use cases in operational environments. Generate test data and configurations that comprehensively cover functional, non-functional (e.g., performance, robustness), and integration requirements.
  + Collaborate with stakeholders, system engineers, and subject matter experts to understand operational scenarios, edge cases, and special conditions.
* **Categorize Data and Configuration Values Based on Use Cases:**

  + **Nominal Data:** Includes inputs, telemetry, and performance parameters that represent expected operational conditions.
  + **Off-Nominal and Edge Case Data:** Includes invalid, boundary, fault-prone, or unexpected data scenarios to test how the system handles error conditions and ensures robustness.
  + **Historical Data:** Utilize archived or historical mission data (if applicable) to simulate operations and validate expected outcomes.
  + **Flight-Like and Ground Testing Data:** Define the configuration and data loads to ensure parity between test environments and the actual operational system.
* **Parameterization of Data and Configuration:**

  + Parameterize test data and configurations to make them reusable, modular, and easily adjustable during test iterations. Automate the generation of variations to explore all possible boundary conditions.

---

#### **2. Data Integrity and Configuration Validation**

* **Establish Data Validity Checks:**

  + Ensure test data is accurate, complete, and representative of operational inputs. Develop validation procedures to detect anomalies or inconsistencies in test datasets.
  + Use validation scripts or tools to pre-check data integrity before loading it for testing. Include checks for data type, range, format, and correctness.
* **Configuration Validation:**

  + Verify that configuration settings align with test objectives and intended system behavior. Develop automated tools to scan and validate configuration files (e.g., XML, JSON, YAML) against predefined schema or rulesets.
* **Consider Data Transmission Effects:**

  + If the test involves uplinking or uploading data or configurations to the system, simulate communication links to account for transmission-induced corruption, latency, or inconsistencies.

---

#### **3. Versioning and Traceability**

* **Implement Version Control:**

  + Maintain version control for test data loads and configurations using tools such as Git or configuration management databases. Use descriptive tags and commit messages to track changes and their rationale.
  + Ensure test artifacts (e.g., datasets, configuration files) are traceable to the software/system requirements and test cases they are associated with.
* **Baseline Management:**

  + Define baselines for critical testing datasets and configurations to ensure consistency across multiple test runs, and document approved baselines as part of the test repository.
  + Limit changes to baselines without proper change control processes.
* **Audit Readiness:**

  + Include test data load and configuration version histories in test reports for traceability and future audits. Ensure the ability to reproduce test conditions.

---

#### **4. Automation and Tooling**

* **Automated Data and Configuration Loading:**

  + Develop or use automated tools to load test data and configuration values into the test environment. Automating this step minimizes human error and ensures the repeatability of test setups.
  + Incorporate data loaders into test automation frameworks to enable seamless integration and repeatable execution in regression tests.
* **Tool Support for Cross-Verification:**

  + Use software tools to automatically cross-verify test data inputs and configuration values against specified system requirements or constraints. Tools can also help simulate the operational environment and automate validation reports.
* **Simulated Data Generators:**

  + Use simulation tools to create synthetic datasets to simulate real-world scenarios, e.g., sensor readings, telemetry, or user inputs. These tools are also helpful in generating difficult-to-obtain or edge-case data.

---

#### **5. Testing and Validation with Realistic Data and Configurations**

* **Integrated Testing with Full System Context:**

  + Conduct end-to-end tests with real or representative data loads and configurations under system-level conditions. Ensure the software can handle the complexities of its operational environment (e.g., unexpected sequences of data or resource limits).
  + Consider the impact of multi-threaded, concurrent processing on configuration values if the system supports parallel data streams (e.g., flight systems, real-time systems).
* **Stress Testing and Resource Validation:**

  + Test configurations under stress conditions (e.g., high data throughput, limited system memory, or degraded hardware conditions). This ensures the system's behavior is consistent and within tolerance under all expected operational conditions.
* **Boundary Value Analysis:**

  + Use boundary-value datasets to deliberately push the limits of configuration values and software constraints. Confirm safe and correct outcomes for edge-case scenarios.

---

#### **6. Monitoring and Error Handling**

* Design acceptance tests to monitor the software's response to loaded data and configurations, validating appropriate error handling and system behavior, including:
  + **Fault Recovery:** Test how the system recovers from incorrect or mismatched configuration values or corrupted data.
  + **Error Reporting:** Validate that errors in data or configurations are logged, flagged, and communicated to operators in a clear and actionable format.
  + **Failsafe Mechanisms:** Ensure unexpected configurations default to safe operational parameters (if applicable).

---

#### **7. Special Considerations for Uplinked/Uploded Data**

* **Real-Time Validation of Uplinked Data:**

  + Develop specialized tests to validate and verify data that is uplinked to the system in real time, testing both nominal and fault conditions.
  + Ensure that protocols for uplinking data (e.g., encryption, checksum validations) work as intended.
* **System State Dependence:**

  + Account for scenarios where test data or configuration loads depend on the current state of the system (e.g., a flight system transitioning between phases). Ensure acceptance tests validate state-aware behaviors.

---

### **Related Requirements and References**

* **SWE-034 - Acceptance Criteria:** Ensure test data and configuration values align with acceptance criteria.
* **SWE-066 - Perform Testing:** Leverage traceable test data and configurations for comprehensive system validation.
* **SWE-068 - Evaluate Test Results:** Analyze the system’s response to various input data loads and configurations during acceptance tests.
* **Topic 8.01 - Off-Nominal Testing:** Validate configurations and data for fault and off-nominal conditions to ensure system reliability.

By incorporating these additional practices for test data loads and configuration values, the acceptance testing process can ensure a higher level of quality, predictability, and robustness in the delivered system. This approach mitigates risks while ensuring the software performs under expected real-world and edge-case scenarios.

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

**"Perform acceptance testing for nominal scenarios on final hardware against input data and conditions that affect the behavior of the system. Validation tests may be used as the acceptance test. Test results need to be documented and evaluated against expected results to determine whether the software passes or is determined to be acceptable by the customer."**

For small projects with limited resources, personnel, and budget, the focus should be on implementing a simplified, efficient, and well-documented acceptance testing process that ensures the correctness of loaded or uplinked data, rules, and code. Below is a step-by-step guide tailored to small projects to meet this requirement:

---

### **1. Plan and Prioritize Acceptance Tests**

#### A. Identify Critical Uplinks or Inputs

* Focus on **critical input data, rules, or code** that significantly impacts the behavior of the system. Examples:
  + Configuration data that includes thresholds, parameters, or settings (e.g., sensor limits, control gains).
  + Uploaded decision rules (e.g., fault-handling logic, command sequences).
  + Software updates or patches.

#### B. Define Nominal Test Scenarios

* Develop **nominal scenarios** in which the system operates as expected under typical mission conditions:
  + Ensure uplinked data, rules, or code affects the system according to the predefined operational requirements.
  + Verify that hazard mitigation and critical system responses are not unintentionally affected.

#### C. Leverage Validation Tests Where Feasible

* In small projects, it is practical to reuse **validation tests** as part of your acceptance tests:
  + Validation testing (performed to ensure the system meets requirements and operates as designed) can overlap significantly with acceptance testing.
  + Identify aspects of existing validation tests that align with acceptance criteria for loaded or uplinked data and software.

---

### **2. Perform Acceptance Testing on Final Hardware**

#### A. Use Final Hardware for Testing

* Test nominal scenarios on **final hardware** whenever possible:
  + Acceptance testing should simulate the real operational environment, as system behavior could differ between simulated environments and final hardware.

#### B. Simulate Loaded Inputs and Conditions

* Test against **all inputs and conditions** that could influence the system:
  + Simulate loaded or uplinked data that might affect behavior (e.g., sensor values, actuator commands, control logic thresholds).
  + Ensure that edge conditions or limits for these inputs do not cause the system to respond unpredictably.

#### C. Verify Hazard Response

* As part of nominal condition testing, confirm that hazard-related scenarios (e.g., thresholds, system triggers that drive hazard mitigations) are not negatively impacted by the loaded data/rules/code.

#### D. Monitor System Behavior

* Continuously monitor the system’s real-time behavior during testing, looking for:
  + Deviations from expected behavior.
  + Evidence of unintended interactions between uplinked updates and preexisting functionality.

---

### **3. Document Test Results Thoroughly**

#### A. Record Test Procedures and Conditions

* For every test executed:
  + Document the procedure, scenario, and hardware/software configurations.
  + Record the specific input data, uplinked rules, or code being tested.

#### B. Capture Observations and Outputs

* Use tools such as logs, reports, and screen recordings to capture:
  + All system responses under nominal conditions.
  + Any anomalies, issues, or near-misses encountered during testing.

#### C. Compare Results Against Expectations

* Clearly define what “expected results” look like for nominal scenarios (e.g., specific outputs, system behavior, state transitions).
* Evaluate actual test results against these expectations to:
  + Verify success or failure.
  + Identify unexpected or erroneous behavior.

---

### **4. Perform Customer Evaluation (Acceptance Decision)**

#### A. Present Test Results for Review

* Summarize test results and provide clear evidence for customer evaluation:
  + Highlight how each nominal test confirms compliance with the defined requirements.
  + List any issues encountered and their corresponding resolutions or justifications.

#### B. Validate Acceptance Criteria

* The customer or designated acceptance authority will use documented evidence to:
  + Determine whether the loaded or uplinked data, rules, and code are acceptable.
  + Approve or recommend further corrective actions based on the test outcomes.

---

### **5. Incorporate Efficient Practices for Small Projects**

#### A. Focus on Critical Scenarios

* Small projects with limited resources may not be able to test every minor aspect or edge case. Instead:
  + Prioritize **high-impact inputs** and **critical functions** that directly affect system behavior.
  + Only test nominal scenarios unless specific additional risks are flagged.

#### B. Simplify Documentation Where Possible

* Use lightweight documentation approaches to save time:
  + Spreadsheets for results tracking (vs. complex formal reports).
  + Simple templates for test procedures and logs.

#### C. Start Small with Automation

* If feasible, automate:
  + The generation of test stimuli (e.g., simulating loaded data or uplinks).
  + Test scenario execution for repetitive or high-priority inputs.
  + Test result comparisons for elements like output thresholds or system state checks.

#### D. Reuse Assets from Validation Testing

* Reuse validation artifacts to minimize duplication of effort, such as:
  + Test plans or cases that already cover portions of nominal acceptance tests.
  + Previous logs or results that show baseline system functionality prior to loaded data/rules.

---

### **6. Address Failures or Anomalies**

#### A. Document Issues for Review

* For any anomalies or issues encountered:
  + Record the conditions that caused the issue and the resulting behavior.
  + Log the issue into your project tracking system, including its severity and potential impact.

#### B. Iterate and Retest After Fixes

* Address issues via corrective actions, such as:
  + Correcting erroneous input data, logic, or threshold values.
  + Fixing bugs in uploaded code.
* Retest to confirm that the fix resolves the issue *without introducing new problems*.

---

### **7. Manage Traceability and Configuration**

#### A. Trace All Tests to Their Requirements

* Even for small projects, maintain basic traceability between:
  + Software/system requirements for nominal conditions.
  + Acceptance test cases/scenarios executed.
  + Test results (including pass/fail status).

#### B. Use a Simple Version Control System

* Track the versions of:
  + Loaded data, rules, and code tested.
  + Final hardware used in acceptance tests.
* Ensure test results are tied to the specific versions tested (to prevent errors during deployment operations).

---

### **8. Example Workflow for Small Projects**

#### **Step 1: Plan the Tests**

* Example: For a spacecraft instrument, test the uploaded configuration file containing sensor thresholds under nominal ranges (e.g., temperature, response time).

#### **Step 2: Execute Tests on Final Hardware**

* Load the configuration file onto the final hardware.
* Simulate normal operational inputs (e.g., sensor readings at nominal levels).

#### **Step 3: Collect Results and Compare**

* Verify whether sensor readings produce the correct system output as expected.
* Compare outputs to baseline requirements (e.g., values in the configuration behave according to mission thresholds).

#### **Step 4: Document and Decide**

* Record the configuration inputs and results.
* Highlight anomalies or error-free outputs. Submit results to the customer for acceptance.

---

### **9. Metrics for Small Projects**

Even for small projects, track basic metrics to assess test progress and success:

* **Acceptance Test Completion:** Number of acceptance tests completed vs. planned.
* **Pass Rate:** Number of passed tests vs. total tests performed.
* **Anomalies Detected:** Number and severity of anomalies detected during tests.
* **Retests:** Number of retests vs. original tests due to failure or required corrections.

---

### **Conclusion**

Acceptance testing for nominal scenarios on final hardware is critical to ensuring the correctness of loaded or uplinked data, rules, and code. For small projects, focusing efforts on critical scenarios, reusing validation tests, simplifying documentation, and automating where feasible helps achieve high confidence in system performance while remaining resource-efficient. By collecting documented results and aligning with customer expectations, small projects can demonstrate compliance and readiness for final deployment.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-041)

  [NASA Systems Engineering Processes and Requirements Updated w/Change 2](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D "Click to open in new window")

  NPR 7123.1D, Office of the Chief Engineer, Effective Date: July 05, 2023, Expiration Date: July 05, 2028
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA’s history of space exploration and software-integration efforts provides valuable lessons regarding the importance of developing and performing rigorous acceptance tests for **loaded or uplinked data**, **rules**, and **code**. These lessons emphasize the critical need to verify updates that affect system behavior to prevent mission-critical anomalies, ensure safety, and maintain operational integrity. Below are **NASA-related lessons learned** that directly or indirectly relate to this requirement.

---

### **1. Mars Climate Orbiter – Mishandling of Units in Uplinked Commands (1999)**

#### **What Happened:**

* The Mars Climate Orbiter mission failed because a navigation-related software component generated outputs in **imperial** units (pounds-force), while the spacecraft's onboard software expected **metric** units (newtons).
* This mismatch in uplinked data caused the spacecraft to deviate from its intended trajectory and enter the Martian atmosphere at too low an altitude, leading to its destruction.

#### **Lesson:**

* Acceptance testing must validate that loaded or uplinked data is compatible with the system’s expected input assumptions, units, and formats.

#### **Relevance to Requirement 4.5.13:**

* Loaded data (e.g., trajectory correction commands) affects system behavior significantly and must be validated through acceptance tests to ensure that no errors (such as unit mismatches) are introduced.

#### **Mitigation Strategy:**

* Introduce rigorous acceptance tests to validate that uplinked data follows the agreed-upon formats, conventions, and units.
* Simulate loaded data during acceptance testing to confirm correct system execution in real-world scenarios.

---

### **2. Mars Polar Lander – Premature Engine Shutdown Due to Faulty Rules (1999)**

#### **What Happened:**

* The Mars Polar Lander mission failed because the spacecraft’s onboard software prematurely interpreted vibration data as a touchdown event during descent.
* This incorrect interpretation, caused by a lack of proper decision-making rules validation, resulted in the premature shutdown of the descent engines.

#### **Lesson:**

* Changes to onboard decision-making rules, thresholds, or logic parameters (e.g., touchdown detection logic in this case) must be comprehensively validated through acceptance and verification tests.

#### **Relevance to Requirement 4.5.13:**

* Decision-making rules are critical to system behavior. If invalid or incorrectly loaded, they can lead to catastrophic failures.

#### **Mitigation Strategy:**

* Acceptance tests must simulate operational scenarios (e.g., vibrations during descent) to validate decision-making logic and how the system reacts to inputs under expected conditions.
* Verify that any rule updates introduced via uplinks still lead to correct decision-making within the software.

---

### **3. Genesis Spacecraft – Faulty Loaded Logic Led to Parachute Deployment Failure (2004)**

#### **What Happened:**

* The Genesis spacecraft crashed because sensors responsible for detecting reentry forces were improperly installed. However, the software’s **fault-handling rules** and logic (determined during prelaunch) did not adequately account for failures in these sensors.
* Poor validation of the input conditions that these rules depended upon meant the spacecraft failed to deploy its parachutes, leading to the loss of mission-critical science data.

#### **Lesson:**

* Acceptance tests must validate **uplinked rules** against realistic sensor failure or hardware error scenarios.
* Software handling critical fault conditions (e.g., input sensor failures) must be tested rigorously to ensure proper behavior based on the provided rules or code.

#### **Relevance to Requirement 4.5.13:**

* Loaded decision rules or fault-handling logic must be validated under both nominal and off-nominal scenarios to ensure they align with safety and mission-critical requirements.

#### **Mitigation Strategy:**

* Acceptance tests must simulate all fault-handling scenarios that the uploaded data, rules, or code are expected to address.
* Develop comprehensive tests to validate input-handling logic under nominal and faulty conditions.

---

### **4. STS-41-D Challenger Liftoff Abort – Fault in Loaded Data Configuration (1984)**

#### **What Happened:**

* A **data mismatch** between the Shuttle’s main engine system and an STS-specific test configuration caused the system to detect an incorrect engine condition, leading to an aborted liftoff just seconds before launch.
* The issue stemmed from failure to validate that the loaded data was correct for the programmed operating conditions.

#### **Lesson:**

* Acceptance testing for loaded configurations or inputs is critical to ensuring mission success. Data mismatches, even in pre-launch scenarios, can disrupt system behavior and trigger fault conditions.

#### **Relevance to Requirement 4.5.13:**

* Loaded data affecting software or system configurations must go through systematic acceptance testing during pre-launch or pre-transition to operation.

#### **Mitigation Strategy:**

* Confirm consistency and correctness of loaded data configurations in the actual mission environment before launch or operational use through validation and acceptance tests.

---

### **5. Mars Exploration Rover Spirit – Flash Memory Data Anomaly (2004)**

#### **What Happened:**

* The Spirit rover experienced a **system reboot anomaly** when managing flash memory. This issue resulted from software mishandling leading to improper sequencing of boot-up operations.
* The root cause was traced to unvalidated configurations of loaded parameters affecting memory management components.

#### **Lesson:**

* Update scenarios for mission-critical data systems—including software for memory management—must be tested extensively under both normal and stress conditions. Loaded configurations need to be checked for adverse effects during operations.

#### **Relevance to Requirement 4.5.13:**

* Data and code updates that directly affect system startup or runtime behavior must pass proper acceptance testing to catch and mitigate adverse impacts.

#### **Mitigation Strategy:**

* Perform rigorous tests on parameters affecting startup operations and runtime behaviors before uploading or enabling the configuration changes.
* Validation tests conducted in simulation environments may need to be replicated on final hardware to ensure real-world behavior matches expectations.

---

### **6. Apollo 11 – Incorrect Formatting of Uplinked Data (1969)**

#### **What Happened:**

* During the Apollo 11 mission, updates were required for the lunar landing guidance computer. One loaded data update introduced a formatting error, causing excessive system alarms during the lunar descent.
* This issue was caught and managed during the mission, but it highlighted the importance of validating input formats and logic for uplinked updates.

#### **Lesson:**

* Testing acceptance of uplinked data must include verification of input formatting, input constraints, and system reaction under operational scenarios to prevent alarms or disruptions.

#### **Relevance to Requirement 4.5.13:**

* Loaded or uplinked data affecting guidance or decision-making logic must be validated for correctness and formatting consistency prior to impacting operational behavior.

#### **Mitigation Strategy:**

* Perform acceptance tests to ensure loaded data adheres to system formatting requirements, constraints, and expected ranges.

---

### **7. NOAA-N-Prime Satellite – Mishandling of Uploaded Configuration Tables (2003)**

#### **What Happened:**

* An error in loading configuration tables for spacecraft operations resulted in unintended system responses. The updates underwent insufficient end-to-end verification before being uplinked.

#### **Lesson:**

* Configuration tables or operational data uplinks, even for routine adjustments, must be subject to full acceptance testing to prevent unintended consequences.

#### **Relevance to Requirement 4.5.13:**

* Every update, parameter, or configuration change loaded to an operational system must be validated through acceptance testing, regardless of its perceived simplicity.

#### **Mitigation Strategy:**

* Validate backward compatibility and correct functionality for all loaded changes before operational use during acceptance testing.

---

### **Summary of NASA Lessons Learned**

| **Key Lesson Area** | **Lesson Learned** | **Testing Focus for Requirement 4.5.13** |
| --- | --- | --- |
| **Input Format Validation** | Ensure uplinked/loaded data formats are correct and compatible with the system. | Validate units, ranges, and input data assumptions (e.g., Mars Climate Orbiter issue). |
| **Rule Logic Validation** | Verify decision-making rules and thresholds under expected scenarios. | Test uplinked thresholds under nominal conditions and fault scenarios (e.g., Mars Polar Lander). |
| **Configuration Data Validation** | Validate configuration updates in realistic operational environments. | Test conditions and loaded configurations under realistic and final hardware setups. |
| **Code & Patch Updates** | Ensure software patches or code uplinks are compatible with current software/hardware. | Acceptance tests must include testing all modifications from uploaded code. |
| **Comprehensive End-to-End Testing** | Uplinks must be tested end-to-end for expected outcomes and adverse effects. | Test operational changes in a representative environment before applying uplinks. |

By applying these historical lessons, NASA projects ensure rigorous testing and validation of all loaded and uplinked data, rules, and code to avoid mission risks and ensure safe, predictable system behavior.

## 6.2 Other Lessons Learned

### 6.2.1 Configurable Data Loads (CDL)

**Lessons Learned:**

* Definition: CDLs contains updateable parameters that are loaded into flight software and can control safety-critical functions.
* Safety-critical data is a shared responsibility between Subsystem Responsible Engineers and Flight Software Team with oversight from Systems Engineering.
* Maintain traceability between data loads and software verification test procedures to support timely verification of late-breaking changes.
* Predefine verification/validation is needed for all CDLs.
* Pre-declare CDL values that are expected/allowed to change with associated nominal verification activities.
  + Changes outside this list need Engineering Control Board approval and must have a verification plan for every change.

**Bottom** **Line: Safety-critical data must be treated with the same rigor as safety-critical software**

* Configuration Management
* Verification and Validation

### 6.2.2 GSFC Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Use the Flight Ops team to perform ground system acceptance testing](https://software.gsfc.nasa.gov/lesson-details/123/).**Lesson Number 123**: The recommendation states: "Use the Flight Ops team to perform ground system acceptance testing."
* [Impacts caused by interfaces that are not tested pre-launch](https://software.gsfc.nasa.gov/lesson-details/124/).**Lesson Number 124**: The recommendation states: "Develop mitigations for impacts caused by interfaces that are not tested pre-launch."
* [Perform pre-launch end-to-end testing between the spacecraft and all primary primary ground stations](https://software.gsfc.nasa.gov/lesson-details/126/).**Lesson Number 126**: The recommendation states: "Perform pre-launch end-to-end testing between the spacecraft and all primary primary ground stations."
* [Assumptions for both over- and under-allocated RF Link margins](https://software.gsfc.nasa.gov/lesson-details/127/). **Lesson Number 127**: The recommendation states: "Examine and rationalize assumptions for both over- and under-allocated RF Link margins."
* [Loading analysis for station usage includes contingency scenarios](https://software.gsfc.nasa.gov/lesson-details/163/). **Lesson Number 163**: The recommendation states: "Ensure loading analysis for station usage includes contingency scenarios (e.g., loss of a ground station for 1 pass, or 1 day, or 1 week)."
* [Software Requirement Sell-Off Expedience](https://software.gsfc.nasa.gov/lesson-details/177/).**Lesson Number 177**: The recommendation states: "As early as feasible in the program (EPR-CDR time frame) ensure that the project will be provided with all relevant test articles well in advance of the test’s run-for-record (will likely require NASA Program Management buy-in as well). This will allow the time necessary for: review of requirement test coverage, accumulation of all comments (especially if IV&V are supporting the program), and vendor disposition of all comments to project satisfaction. In this manner, when test artifacts from the FQT run-for-record are provided for requirement sell-off, the Flight Software SME will have a high level of confidence in the artifacts provided (knowing how each requirement has been tested) to expedite the sign-off process. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
* [GOLD Rule 1.43 provides end-to-end demonstration for each SW component that can be changed in flight](https://software.gsfc.nasa.gov/lesson-details/343/). **Lesson Number 343**: The recommendation states: "There are multiple Observatory components with loadable flight software - demonstrating the code change process for each spacecraft and instrument FSW component can be very beneficial and useful. Incorporate into project plans and budgets and provide resources for the satisfaction of the GOLD Rule 1.43 requirement for pre-flight end-to-end code change demonstrations."

# 7. Software Assurance

**SWE-193 - Acceptance Testing for Affected System and Software Behavior**

4.5.13 The project manager shall develop acceptance tests for loaded or uplinked data, rules, and code that affects software and software system behavior.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project develops acceptance tests for loaded or uplinked data, rules, and code that affect software and software system behavior.

2. Confirm that the loaded or uplinked data, rules, scripts, or code that affect software and software system behavior are baselined in the software configuration system.

3. Confirm that loaded or uplinked data, rules, and scripts are verified as correct prior to operations, particularly for safety-critical operations.

## 7.2 Software Assurance Products

Software assurance plays a critical role in ensuring that the software and its associated artifacts meet quality standards and effectively mitigate risks throughout the project lifecycle. In the context of acceptance testing, the following software assurance products should be developed, reviewed, and maintained:

1. **Software Test Reports:**

   * Documents the results of acceptance testing, detailing test execution, issues encountered, and overall compliance with acceptance criteria.
   * Includes coverage metrics that show how much of the system (e.g., functions, requirements, code) has been tested.
2. **Software Test Procedures:**

   * Captures the step-by-step instructions for executing acceptance tests, including preconditions, expected outcomes, tolerances, and handling procedures for deviations.
   * Validates that the tests are aligned with system requirements and address both nominal and off-nominal conditions.
3. **Software Configuration Data:**

   * Includes version-controlled artifacts such as the source code, uploaded/uplinked data, scripts, rules, and associated configuration files.
   * Ensures traceability between configuration data, tests performed, and specific software versions used during the acceptance process.
4. **Software Risk Assessments (Optional):**

   * Includes risks identified based on acceptance testing results, especially for system behavior in off-nominal and fault conditions.
   * Tracks the state of mitigations for those risks in alignment with project-level standards.

---

## 7.3 Metrics

Software assurance metrics provide insight into the quality and maturity of the software product, as well as the effectiveness of testing processes. While specific metrics were not initially identified, the following examples can be added to strengthen assurance processes:

1. **Test Coverage Metrics:**

   * Percentage of system requirements covered by acceptance tests.
   * Percentage of testable code/functions exercised during acceptance testing.
2. **Defect Metrics:**

   * Number and severity of defects detected during acceptance tests versus the number resolved before delivery.
   * Recurrence of defects caused by loaded or uplinked data, rules, scripts, or configuration errors.
3. **Configuration Management Metrics:**

   * Frequency of changes to uploaded or uplinked data, rules, scripts, or configurations.
   * Percentage of undocumented/unapproved changes detected during review.
4. **Off-Nominal Test Metrics:**

   * Percentage of off-nominal scenarios identified and tested relative to the total test cases executed during acceptance testing.
5. **Test Execution Metrics:**

   * Proportion of planned acceptance tests completed successfully on the first attempt versus those that needed rework.

Collecting and analyzing these metrics will allow the software assurance team to monitor and improve the confidence and reliability of the software under test.

---

## 7.4 Guidance

**Acceptance Testing Context:**  
The primary goal of software acceptance testing is to ensure that the software performs correctly in its intended operational environment. This includes confirming that the software, in combination with its uploaded/uplinked data, rules, scripts, and code, meets the requirements for normal and fault-tolerant conditions.

### **Key Activities for Software Assurance During Acceptance Testing:**

1. **Validation of Test Planning:**

   * Ensure that acceptance test plans address all critical scenarios, including uploaded/uplinked data, rules, and scripts.
   * Verify that the test plans align with system requirements and acceptance criteria.
   * Confirm that off-nominal scenarios have been identified and appropriately included in the test procedures (see **8.01 - Off-Nominal Testing**).
2. **Verification of Test Execution:**

   * Observe and review the execution of acceptance tests to ensure that:
     + Test conditions match the intended operational and hardware environment.
     + Test procedures are followed in a consistent and documented way.
   * Ensure special tests have been successfully run to validate and verify uploaded/uplinked data and configurations.
3. **Data and Configuration Validation:**

   * Confirm that all uploaded/uplinked data, rules, and configurations are:
     + Syntactically and semantically correct.
     + Representative of actual operational conditions, including edge cases.
     + Consistent with software requirements and functional expectations.

### **Configuration Management Assurance for Uploaded Data and Rules:**

Uploaded or uplinked data, rules, scripts, and code are dynamic in nature and can often require modification after deployment. Mismanagement of these changes poses a significant risk to the system’s operational reliability. The following activities ensure robust configuration management:

1. **Establishing Configuration Management Practices:**

   * Ensure all uploaded/uplinked data, rules, scripts, and configurations are placed under formal **configuration management (CM)**. Each change must be version-controlled, reviewed, and traceable to an approved configuration change request.
   * Confirm that change control processes are followed consistently to evaluate potential impacts and to coordinate acceptance tests for updated configurations.
2. **Baseline Management and Verification:**

   * Validate that baselines for test data and configuration values have been clearly defined and approved prior to acceptance testing.
   * Track any updates to data or configurations during testing and ensure these updates are archived and referenced appropriately for traceability.
3. **Post-Deployment Change Assurance:**

   * Ensure post-deployment processes to modify uploaded or uplinked data follow the same configuration management practices as during development, with comprehensive documentation and stakeholder approval.

### **Special Considerations for Nominal and Off-Nominal Scenarios:**

1. **Nominal Scenarios:**

   * Confirm that all correctly formatted, typical operational data loaded into the software produces expected outcomes during nominal test cases.
2. **Off-Nominal Scenarios:**

   * Ensure software assurance reviews include the validation of test procedures for extreme, unlikely, or incorrect operational conditions. For example:
     + Malformed or out-of-range data.
     + Concurrency issues from multiple simultaneous uplinks.
     + Unexpected sequences of commands or configurations.
   * Validate that the system correctly handles these scenarios, such as reverting to default-safe parameters, logging errors, or providing appropriate alerts.

---

### **Conclusion:**

By implementing the improved guidance above, software assurance ensures that acceptance testing delivers reliable, operationally ready software. Special attention to the dynamic nature of uploaded/uplinked data, rules, scripts, and configurations—particularly their management, testing, and validation—enhances the overall confidence in the software’s performance under both nominal and off-nominal operations. The additional focus on test metrics, test execution, and configuration management further ensures traceability, process maturity, and conformance with the project's quality standards.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical for demonstrating compliance with requirements, ensuring the software meets quality standards, and providing confidence in the results of acceptance testing. Below is a detailed outline of objective evidence for software assurance activities related to acceptance testing, uploaded/uplinked data, rules, scripts, and configuration management:

---

### **1. Test Planning and Execution**

#### **Key Evidence:**

1. **Acceptance Test Plan**:

   * Document detailing the entire scope of acceptance testing, including objectives, test cases, environments, nominal and off-nominal scenarios, dependencies, and expected outcomes.
   * Verification that uploaded/uplinked data and configuration scenarios (nominal and off-nominal) are included.
2. **Acceptance Test Procedures**:

   * Step-by-step instructions for executing all acceptance tests, including specific procedures for validating dynamic inputs such as uploaded data, rules, and scripts.
   * Evidence that test procedures were peer reviewed and approved.
3. **Test Traceability Matrix**:

   * A matrix mapping acceptance test cases directly to requirements, showing coverage of uploaded/uplinked data, rules, scripts, and configurations.
   * Tracks compliance and completeness of testing.
4. **Test Execution Logs**:

   * Automated test execution logs or manually maintained records showing test runs.
   * Recorded system outputs for uploaded/uplinked data during both nominal and off-nominal scenarios.
5. **Observed/Reviewed Test Sessions**:

   * Signed records or reports from software assurance personnel who participated as observers during acceptance test execution, confirming procedural adherence and compliance with requirements.

---

### **2. Test Results and Outcomes**

#### **Key Evidence:**

1. **Software Test Report**:

   * Comprehensive documentation of test results that includes:
     + Test outcomes for every test case, including the impact on uploaded/uplinked data, rules, and scripts.
     + Instances of discrepancies detected during acceptance testing.
     + Results of off-nominal test cases simulating malformed or incorrect data inputs.
   * Evidence that test results were reviewed and approved by software assurance personnel.
2. **Defect Logs**:

   * Traceable log of detected defects and discrepancies, including:
     + Recorded issues caused by uploaded/uplinked data, rules, or configuration items.
     + Resolution status and any re-tests performed after fixing these issues.
   * Evidence that defect resolution was validated by software assurance.
3. **Test Completion Certificate**:

   * Signed certification showing the completion and approval of acceptance testing activities, confirming that the software met its acceptance criteria.

---

### **3. Validation of Uploaded/Uplinked Data, Rules, Scripts, and Configurations**

#### **Key Evidence:**

1. **Configuration Files with Version History**:

   * Complete records of uploaded/uplinked data configurations and scripts with version control logs, showing:
     + What was tested and when.
     + Traceability to change requests or requirements.
2. **Validation Test Results**:

   * Specific test results for validating the integrity and correctness of uploaded/uplinked data, rules, and scripts.
   * Results of syntax/criteria checks, edge case testing, and fault handling tests.
3. **Configuration Management Audit Reports**:

   * Evidence proving uploaded/uplinked data, rules, and configuration files underwent auditing for adherence to configuration management practices.
   * Reports showing approved baselines and changes with stakeholder authorization.
4. **Data Integrity Checks**:

   * Documented proof of integrity checks performed on loaded data sets, ensuring proper format, completeness, and operational relevance.
   * Results of automated tools for verifying correct parameter values, schemas, and formats.

---

### **4. Process Compliance and Assurance**

#### **Key Evidence:**

1. **Software Assurance Review Reports**:

   * Formal reports from assurance personnel confirming test plans and procedures adhered to requirement expectations.
   * Results of reviews ensuring proper coverage of expected scenarios, including nominal, off-nominal, and configuration management-related conditions.
2. **Configuration Change Records**:

   * Approved forms or requests for changes to uploaded/uplinked data, rules, scripts, and configurations.
   * Evidence that changes were reviewed, tested, and traceable to documented requirements.
3. **Verification and Validation Reports**:

   * Comprehensive documents demonstrating successful execution of verification activities and validation testing.
   * Reports from assurance personnel confirming that tests adequately validated system behavior for all uplinked or uploaded inputs.
4. **Non-Compliance Reports (NCRs)**:

   * Reports documenting any deviations from accepted processes or unexpected test results.
   * Evidence of corrective action taken and successful retesting results.

---

### **5. Metrics Reporting**

#### **Key Evidence:**

1. **Test Metrics Dashboard**:

   * Graphical or tabular representation of test coverage, showing the percentage of requirements and code covered by acceptance testing.
   * Specific metrics demonstrating how much of the uploaded/uplinked data rules, scripts, and configurations were tested.
2. **Defect Metrics**:

   * Quantitative data showing the number of defects detected and resolved during acceptance testing, categorized by severity.
3. **Configuration Management Metrics**:

   * Reports detailing the frequency of changes made to configured uplinked data and how many of those changes required updates to acceptance tests.

---

### **6. Documentation of Off-Nominal Testing**

#### **Key Evidence:**

1. **Off-Nominal Test Results**:

   * Detailed results of tests simulating invalid data inputs, corrupted uplinks, or incorrect configurations.
   * Analysis showing the software’s response to off-nominal scenarios, including error detection, fault recovery, and safe handling mechanisms.
2. **Simulated Environment Reports**:

   * Evidence of testing performed in a simulated operational environment to evaluate system behavior under faulty conditions.

---

### **7. Configuration Management Assurance**

#### **Key Evidence:**

1. **Configuration Management Plan**:

   * Formal plan outlining the procedures, roles, and tools used to manage uploaded/uplinked data, rules, and scripts under version control.
2. **Configuration Audits**:

   * Reports of audits conducted to verify that configuration changes were approved, tested, and implemented using prescribed processes.
3. **Baseline Approval Documents**:

   * Records demonstrating approval of baselines used during testing for uploaded/uplinked data, rules, and scripts.

---

### **Summary of Objective Evidence**

Objective evidence ensures that software assurance activities provide tangible, traceable, and verifiable proof of compliance with requirements. The evidence listed above includes items that cover planning, execution, results, configuration management, and metrics. By collecting and documenting this evidence, the software development and assurance teams build confidence that acceptance testing has achieved its goals and the delivered system meets operational requirements.

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
