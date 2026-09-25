# SWE-066 - Perform Testing

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695449. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing

SWE-066 - Perform Testing

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695449)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695449&showCommentArea=true&showComments=true#addcomment)

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

4.5.3 The project manager shall test the software against its requirements.

## 1.1 Notes

A best practice for Class A, B, and C software projects is to have formal software testing planned, conducted, witnessed, and approved by an independent organization outside of the development team.

## 1.2 History

Click here to view the history of this requirement: SWE-066 History

SWE-066 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.4.2 The project shall perform software testing as defined in the Software Test Plan. |
| Difference between A and B | Removed reference to the  Software Test Plan which is defined in SWE-104. |
| B | 4.5.3 The project manager shall perform software testing. |
| Difference between B and C | Instead of just performing testing, specifies testing shall be done against the requirements. |
| C | 4.5.3 The project manager shall test the software against its requirements. |
| Difference between C and D | No change |
| D | 4.5.3 The project manager shall test the software against its requirements. |

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

Software testing is required to ensure that the software meets the agreed requirements and design. The application works as expected. The application doesn’t contain serious bugs, and the software meets its intended use as per user expectations.

#### **Purpose of the Requirement:**

This requirement ensures that software undergoes rigorous testing to verify that it fulfills all documented requirements, including functional, performance, interface, and safety-critical aspects. Testing against requirements is an essential verification and validation activity aimed at achieving mission assurance, reducing risks, and confirming that the software is ready for deployment in its intended operating environment.

---

### **Key Rationales**

#### **1. Ensures Correct Implementation of Requirements**

* **Purpose**: Testing software against its requirements ensures that the software is developed and implemented as intended, meeting the needs of the mission and avoiding deviations that could introduce defects or fail to satisfy user expectations.
* **Why It Matters**: Requirements are the foundation for software functionality, and untested or improperly tested software may lead to incomplete or incorrect functionalities.
  + For example, critical missions may require precise timing, proper command sequences, and specific safety features. Testing validates that the software executes these features as specified.

#### **2. Promotes Requirements Traceability**

* **Purpose**: Testing provides traceability by confirming that each software requirement has been thoroughly verified through one or more test cases.
* **Why It Matters**: Ensuring traceability reduces the risk of overlooking or under-testing any requirements (e.g., critical requirements for flight control systems or hazard mitigations). Uncovered defects in overlooked areas may result in costly rework and risk the success of the mission.

#### **3. Confirms Functional and Performance Objectives**

* **Purpose**: Requirements testing confirms that the software provides the expected behavior under normal conditions and meets performance thresholds identified during system development.
* **Why It Matters**:
  + Functional validation ensures the software accomplishes its intended tasks, such as data processing, command execution, or interface communication.
  + Performance testing confirms that the software can operate within the resource constraints, timing requirements, and data volumes anticipated by the mission.

#### **4. Validates Safety and Reliability**

* **Purpose**: Testing ensures that all safety-critical and reliability requirements are addressed—both for nominal operations and edge cases (e.g., off-nominal conditions, anomaly recovery, and fault detection and response).
* **Why It Matters**:
  + Software used in high-stakes environments (e.g., space systems, satellites, human-rated missions) typically has safety-critical aspects. Testing ensures proper handling of faults and hazards, including system recoverability and mitigation of potential failures.
  + For example, testing ensures that hazard control mechanisms (e.g., abort triggers, limiters, or fail-safe states) work as specified and comply with higher-level system hazard analyses.

#### **5. Mitigates Risk and Prevents Costly Failures**

* **Purpose**: Testing against requirements identifies issues early in the software lifecycle, reducing the likelihood of expensive fixes or failures during operational deployment.
* **Why It Matters**:
  + Undetected issues can have catastrophic impacts during flight missions, delaying schedules, increasing costs, or even causing mission failures and loss of hardware or lives.
  + According to historical data, correcting issues during testing (prior to deployment) is far less expensive than correcting those discovered after the system is delivered (10-100x less expensive).

#### **6. Confirms Readiness for Integration and Deployment**

* **Purpose**: Testing ensures that the software is production-ready and integrates correctly with the target hardware and other software systems while meeting mission requirements.
* **Why It Matters**:
  + Software is often only one component of a larger system. For example, a spacecraft relies on proper interactions between ground systems, communication systems, and onboard software. Testing ensures software aligns with system-level architecture and behaves as intended when deployed.

#### **7. Maintains Compliance with NASA Standards and Mission Assurance**

* **Purpose**: Testing requirements ensure that NASA's stringent safety and mission-critical standards (e.g., **NPR 7150.2**, **NASA-STD-8739.8**) are met, including verification and validation (V&V) of requirements.
* **Why It Matters**:
  + Compliance with NASA guidelines ensures consistent and thorough testing processes across the agency and promotes quality, reliability, safety, and accountability.

#### **8. Addresses Both Nominal and Off-Nominal Scenarios**

* **Purpose**: Testing verifies that software works correctly in normal operational conditions, as well as under boundary conditions, edge cases, and failure conditions.
* **Why It Matters**:
  + Space missions operate in unpredictable environments. Environmental factors such as radiation, thermal variability, and communication delays can impact software. Testing against requirements ensures the system can operate reliably in these scenarios.

---

### **Practical Benefits of Testing Against Requirements**

1. **Error Prevention**:

   * By testing against requirements, errors and gaps in implementation are identified and corrected early in the software lifecycle.
   * Prevents software mismatches that lead to mission-critical issues.
2. **Test Repeatability**:

   * Well-documented requirements and corresponding test cases allow repeatable and consistent testing, especially useful for regression testing after design or code changes.
3. **Verification of Changes**:

   * Testing against requirements ensures that any newly implemented requirements or changes (e.g., defect fixes, feature modifications) do not unintentionally affect other system components.
4. **Improved Communication Across Teams**:

   * Requirements testing ensures that all stakeholders (e.g., testers, developers, systems engineers) share a common understanding of what the software is supposed to do.
   * Promotes transparency by providing clear evidence that requirements have been met.
5. **Foundation for Certification and Validation**:

   * Testing provides auditable, measurable proof that the software meets project certification, safety, and regulatory standards.

---

### **Examples of Real-World Problems that Could Be Avoided**

1. **Mars Climate Orbiter (1999)**:

   * Failure to verify key requirements for software that converted units between metric and imperial systems led to the loss of the spacecraft.
   * Testing software against its requirements would have revealed this inconsistency in calculations.
2. **Ariane 5 Launch Failure (1996)**:

   * A software requirement mismatch in handling floating-point errors during integration testing led to a critical failure and the destruction of the rocket.
   * Testing against system-level performance and failure requirements could have addressed this.

---

### **Conclusion**

Testing software against its requirements is a cornerstone of ensuring mission success. By verifying that the software performs as specified, NASA reduces risks, ensures traceability, confirms safety and functional compliance, and avoids costly errors during operations or deployment. This requirement reflects the criticality of aligning software testing with mission objectives, safety standards, and system responsibilities, making it an indispensable activity in the software engineering process for NASA missions.

# 3. Guidance

This enhanced guidance provides a structured and comprehensive overview of software testing as a critical activity to verify and validate software against its requirements. It incorporates best practices, standards, and proven approaches to ensure mission-critical software adheres to reliability, performance, and safety expectations in alignment with NASA's high standards.

---

### **Overview of Software Testing**

According to **IEEE 730-2014**, software testing involves executing a system or component under specified conditions, observing and recording the results, and evaluating whether the system meets defined requirements. Similarly, **ISO/IEC TR 19759:2005 (SWEBOK)** defines software testing as the dynamic verification of program behavior on a finite set of test cases selected from an infinite execution domain against expected behavior.

This requirement directs software engineers and project managers to implement thorough testing practices to confirm that the software meets all documented functional, performance, safety-critical, and interface requirements, ensuring system reliability and mission success.

---

### **Purposes of Software Testing**

Software testing serves multiple critical objectives throughout the development lifecycle:

1. **Defect Identification and Mitigation**:

   * Testing identifies defects and errors early to reduce downstream risks and ensure the software is reliable and safe for operational use.
2. **Requirement Verification**:

   * Verifies that the software meets all documented requirements, including functional, performance, and interface specifications.
3. **Safety and Hazard Mitigation**:

   * Confirms that safety-critical requirements and hazard controls (nominal and off-nominal) are implemented effectively, reducing risks to personnel, systems, and mission objectives.
4. **Quality Assurance**:

   * Demonstrates the software's quality by ensuring it behaves consistently under expected and stress conditions.
5. **Performance Validation**:

   * Ensures the software performs effectively under typical conditions and meets resource, timing, and scalability constraints.

---

### **Software Testing Essentials**

The foundational concepts and practices for software testing include:

#### **1. Independent Testing**

* The personnel responsible for qualification or formal testing of software components must be independent of those involved in the detailed design and implementation phases. This independence minimizes bias and ensures objective assessment and compliance.

#### **2. Qualification Testing for Multi-Build Software**

* For software developed in multiple builds, qualification testing should be deferred to the final build for that item. Earlier builds may undergo informal or incremental testing, but full qualification occurs only once the item reaches maturity.

#### **3. Traceability**

* All testing activities should be traceable to specific software requirements. This ensures complete coverage and reduces the risk of unverified features or functions. Traceability matrices should link:
  + Requirements ⇄ Test Cases ⇄ Code ⇄ Test Results.

---

### **Levels and Types of Testing**

Software testing spans multiple levels of granularity, including:

#### **1. Unit Testing**

* **Goal**: Validate individual components, modules, or functions.
* **Practices**:
  + Developers perform unit tests to verify logic, interfaces, and performance.
  + Use stubs, drivers, and simulations to isolate components during testing.
* **Considerations**: Leverage code coverage tools to ensure all functional paths are exercised.

#### **2. Integration Testing**

* **Goal**: Ensure the software components interact correctly when combined.
* **Practices**:
  + Focus on data flow, performance, and error-handling across interfaces.
  + Use simulated environments before integrating with actual hardware.

#### **3. System Testing**

* **Goal**: Validate the behavior, performance, and safety requirements of the integrated system.
* **Practices**:
  + Conduct tests in both simulated environments and actual mission hardware where applicable.
  + Include off-nominal scenarios and edge case evaluations to ensure robustness.

#### **4. Regression Testing**

* **Goal**: Verify that software changes, patches, or updates do not introduce new defects or impact functionality.
* **Practices**:
  + Use automated tools to re-run previous test cases with the updated codebase.
  + Confirm proper operation of hazard controls after updates.

#### **5. Special Testing (Safety and Performance)**:

* **Stress Testing**:
  + Validate performance under extreme conditions, such as loads and system failures.
* **Stability Testing**:
  + Confirm long-term reliability and graceful degradation during anomalies.
* **Safety Testing**:
  + Prioritize validation of hazardous functions and failure recovery mechanisms.
  + Ensure that controls, inhibits, and fault recovery pathways operate without failure.

---

### **Code Coverage Analysis**

**Purpose**: One intent of software testing is verifying all paths through the code, including decisions, loops, boundary conditions, and off-nominal paths. Code coverage analysis highlights unexecuted paths, orphaned code, and potential areas requiring additional test cases.

#### **Key Practices**:

1. **Code Coverage Metrics**:

   * Use tools to measure structural code coverage during unit, integration, and system tests.
   * Identify code paths not exercised by current tests and address gaps by developing supplementary cases.
2. **Challenges with 100% Coverage**:

   * Achieving 100% coverage may not always be feasible due to hardware constraints, environmental factors, or rare fault conditions.
   * Focus coverage efforts on areas impacting functionality, performance, and safety.

**Common Misconceptions About 100% Code Coverage**:

* **Does Not Guarantee Code Correctness**: High coverage does not mean all bugs are identified or resolved.
* **Does Not Validate Requirements**: Coverage ensures code execution but does not indicate whether requirements themselves are correct.
* **Importance of Traceability**: Coverage must be analyzed alongside requirements testing to ensure full alignment with project objectives.

#### **Tools and Techniques**:

* Use non-intrusive hardware-based tools or instrumented code to generate coverage data without affecting software execution.
* Perform acceptance testing separately for unmodified production builds.

---

### **Testing for AI/ML Software**

For systems incorporating Artificial Intelligence (AI) or Machine Learning (ML), testing requires additional considerations:

#### **Specific Guidance**:

1. Validation of training data and algorithms to ensure AI does not introduce unpredictable risks.
2. Behavior testing under novel input conditions to confirm reliability and performance.
3. Refer to **Topics 7.25** and **8.25** (Artificial Intelligence and Software Engineering/Assurance) for further guidance.

---

### **Best Practices**

#### **General Testing Principles**:

1. **Requirement Traceability**:

   * Each test must link to one or more requirements to ensure complete coverage and accountability.
   * Traceability matrices should be continually updated as requirements change.
2. **Defect Identification and Resolution**:

   * Defect reports must include severity classification, root cause analysis, and corrective actions.
   * Rerun failed tests after corrective actions are implemented to confirm defect resolution.
3. **Regression Testing After Changes**:

   * Perform regression testing at every stage where requirements, code, or interfaces are altered.
4. **Test Reports**:

   * Maintain detailed test reports summarizing execution outcomes, anomalies, corrective actions, and test coverage analysis.
5. **Simulated and Controlled Environments**:

   * Use simulated environments for hazardous functions before testing on live hardware.
   * Ensure test setups replicate operational conditions as closely as possible.

#### **Risk-Based Testing**:

When time and resources are constrained:

1. Prioritize testing based on areas of highest risk (e.g., safety-critical functions, complex components, or known defects).
2. Allocate resources intelligently to ensure coverage of critical paths and edge cases.

---

### **Useful Tools for Testing Activities**

Projects should leverage appropriate tools for their testing efforts. Examples include:

* Code coverage tools (e.g., gcov, JaCoCo).
* Debuggers (e.g., GDB, Visual Studio Debugger).
* Static and dynamic analysis tools (e.g., Coverity, Valgrind).
* Configuration and defect tracking systems (e.g., JIRA, GitLab, or Rational tools).
* Simulation and modeling tools for hazardous conditions.

---

### **References and Additional Topics**

1. **NASA-STD-8739.8** – Software Assurance and Software Safety Standards.
2. **SWE-189** – Code Coverage Measurements.
3. **SWE-193** – Acceptance Testing for Affected System and Software Behavior.
4. **NASA-GB-8719.13** – Software Safety Guidebook.
5. **Topic 8.08** – COTS Software Safety Considerations.

---

### **Conclusion**

Software testing is a mission-critical activity that involves verifying software behavior against documented requirements, ensuring reliability, safety, and performance. By following structured testing practices, leveraging traceability matrices, utilizing code coverage analysis, and prioritizing risk-based approaches, NASA software teams can produce high-quality systems that meet stringent safety and mission assurance standards.

See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality), [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan), [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results),

see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing), [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software),

See also [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test)

See also [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements), [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage), Topic [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels).

For Class A software take care to analyze all software affecting safety-critical software  and hazardous functionality including [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action), 

**NASA-GB-8719.13, NASA Software Safety Guidebook**

4.3.5 Testing  
"Testing serves several purposes: to find defects; to validate the system or an element of the system; and to verify functionality, performance, and safety requirements. The focus of testing is often on the verification and validation aspects. However, defect detection is probably the most important aspect of testing. While you cannot test quality into the software, you can certainly work to remove as many defects as possible."[276](#_tabs-<p></p>)

See also Topic [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing).

See also [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior).

See also Topic [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations).

See also [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools), Topic [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009),

The following chart shows a basic flow for software testing activities from planning through maintenance. Several elements of this flow are addressed in related requirements in this Handbook (listed in the table at the end of this section).

## 3.3 Guidance for the Test Lead When Preparing for Testing

The **TEST REVIEW CHECKLIST FOR TEST LEADS** [PAT-026](#_tabs-<p></p>)  can be used to help a test lead determine whether the team is ready for testing and what processes and other preparations need to be in place before beginning testing.

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-026 - Test Review Checklist For Test Leads**

See also Topic [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis), [PAT-026 - Test Review Checklist For Test Leads](/spaces/SITE/pages/117211498/PAT-026+-+Test+Review+Checklist+For+Test+Leads), [PAT-027 - Test Review Checklist For Review Teams](/spaces/SITE/pages/118161596/PAT-027+-+Test+Review+Checklist+For+Review+Teams),

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action),        * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [PAT-026 - Test Review Checklist For Test Leads](/spaces/SITE/pages/117211498/PAT-026+-+Test+Review+Checklist+For+Test+Leads) * [PAT-027 - Test Review Checklist For Review Teams](/spaces/SITE/pages/118161596/PAT-027+-+Test+Review+Checklist+For+Review+Teams) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

Software testing is essential for all projects, regardless of size. For smaller projects, adopting a tailored and scalable approach to testing ensures efficiency while maintaining compliance with NASA’s quality and safety standards. The guidance below provides principles and practices for managing software testing in small projects while balancing limited resources, project constraints, and risk.

---

### **Principles for Small Project Software Testing**

1. **Prioritize Risk-Based Testing**:

   * Testing should focus on areas that pose the highest risk to mission success based on the overall **risk posture** of the project.
     + Safety-critical software must always take the **highest priority** for testing.
     + Functional areas deemed critical to success or with significant potential mission impacts take the next priority.
     + Lower-risk, non-critical code may receive reduced rigor, but all areas must undergo some form of verification.
2. **Tailor the Testing Effort Based on Project Scale**:

   * Flexibility in test scope and depth is necessary to balance limited resources and project size. Smaller projects may not have access to advanced simulators, models, or multiple hardware configurations, but the core objectives of testing (i.e., defect detection, requirement validation, and quality assurance) remain unchanged.
3. **Understand the Impact of Testing Environment Constraints**:

   * Clearly assess whether testing will use models, simulators, or the actual “flight” hardware. Testing on physical hardware should be performed with extreme care to prevent **equipment damage** or **premature wear.**
   * Use **SWE-073 (Platform or High-Fidelity Simulations)** for guidance on determining when high-fidelity simulations versus actual hardware testing are most suitable.
4. **Maintain Test Repeatability and Traceability**:

   * Regardless of the scope of the testing effort, tests must be repeatable and executed under the same conditions to ensure issues are identifiable, reproducible, and traceable to resolution.
   * Maintain accurate records and logs (e.g., input configurations, test environments, and results) to support defect resolution and compliance with verification procedures.

---

### **Key Testing Approaches for Small Projects**

#### **1. Focus on Safety-Critical and High-Risk Areas**

* **Safety-Critical Code**:
  + Prioritize the execution of detailed testing for software that interacts with safety-critical systems (e.g., navigation, hazard detection, and fault recovery systems).
  + Include boundary testing, off-nominal scenarios, and stress testing to evaluate the software’s ability to handle hazardous situations.
* **High-Risk Features**:
  + Identify key components or functions critical to mission success and emphasize comprehensive testing in these areas.

#### **2. Unit Testing and Low-Level Validation**

* Unit testing, which verifies the correctness of individual software units or modules, should be rigorously performed for critical components.
* Code coverage tools can assist in ensuring multiple paths (nominal and off-nominal) within safety-critical code are tested.
  + Be mindful that 100% coverage does not guarantee correctness but highlights untested areas.
* Ensure proper stubbing and simulation for components with external dependencies (e.g., hardware).

#### **3. Incremental Test Approach with Reusability**

* For small projects with limited resources, incremental testing helps manage the workload:
  + Start with **unit tests** → progress to **integration tests** → conclude with **system-level tests.**
  + Utilize reusable tests across project phases where applicable (e.g., regression tests for updated builds).

#### **4. Simplified Test Articles and Simulations**

* If high-fidelity simulators or models are unavailable, leverage simpler test articles such as:
  + Mock environments,
  + Test harnesses or scripts, and
  + Low-cost simulators for basic operational testing.
* Ensure the environment is adequate to simulate operational conditions where the software will execute.
* Exercise caution when transitioning from low-fidelity simulations to higher-fidelity environments or actual “flight” hardware.

---

### **Test Execution Guidelines**

1. **Prevent Potential Damage to Flight Hardware**:

   * When executing tests on the actual hardware, evaluate risk factors and failure modes that could damage the equipment.
   * For critical functions, use a **progressive simulation-to-hardware approach**, where functions are thoroughly tested in simulators and development environments before running on live hardware.
2. **Test Coverage Considerations**:

   * Apply **code coverage tools** to identify untested paths (e.g., decisions, loops) and reduce dead or unused code.
   * Code coverage for small projects may be scaled to focus primarily on safety-critical and high-risk areas to maximize available resources and testing effectiveness.
3. **Formalize Test Procedures and Logs**:

   * Even for small projects, maintain concise but comprehensive:
     + Test procedures to define how tests are executed, including setup, inputs, expected results, and teardown steps.
     + Test logs to capture details of each execution, such as:
       - Software build number,
       - Test environment configuration,
       - Pass/fail status, and
       - Issues or anomalies observed.
4. **Repeatability**:

   * Verify that tests are repeatable within the same configuration and controlled environment to ensure defect consistency and proper resolution tracking.

---

### **Test Documentation for Small Projects**

#### **1. Test Plan**:

* Even for small projects, a lightweight test plan is essential to define:
  + Risk analysis and prioritization of components or functions.
  + Test scope, objectives, and constraints (e.g., hardware availability).
  + Types of testing to be performed (unit, integration, system, regression).

#### **2. Test Procedures**:

* Include concise, step-by-step instructions for executing specific test cases or scenarios.
* Ensure safety-critical procedures encompass both nominal and off-nominal conditions.

#### **3. Test Results and Reporting**:

* Test reports must document:
  + Pass/fail status for each test,
  + Defects or anomalies discovered, and
  + Corrective actions/resolutions.
* Include regression test results demonstrating the resolution of issues without introducing new ones.

#### **4. Configuration Management**:

* Maintain a version-controlled repository of test artifacts:
  + Test plans,
  + Procedures,
  + Test results/logs, and
  + Known issue reports.
* Track all changes to test environments or procedures.

---

### **Example Use Cases of Prioritization in Small Projects**

**Case 1: Performance Validation in Resource-Constrained Systems**

* Allocate resources to test modules responsible for memory management, timing-critical operations, or real-time data transmission to ensure compliance with resource constraints inherent in small systems.

**Case 2: Flight Hardware and Environmental Safety**

* Avoid direct execution of unvalidated code on flight hardware. Where actual hardware testing is unavoidable, validate in staging simulations before physical execution to protect expensive equipment.

**Case 3: Hazard Mitigation in Safety-Critical Functions**

* Prioritize testing for fault detection, isolation, and recovery mechanisms in a simulator to safely evaluate response under hazardous conditions.

---

### **Best Practices for Small Project Software Testing**

1. **Simplify Without Compromising Objectives**:

   * Follow the same core principles as larger projects but tailor plans, tools, and oversight based on project complexity and resource constraints.
2. **Automate Where Feasible**:

   * For smaller projects, automation tools (even lightweight ones) can significantly reduce manual testing efforts and enhance regression testing efficiency.
3. **Adapt Risk Prioritization Frameworks**:

   * Focus testing on high-priority areas using an adapted **risk matrix** that ranks components by likelihood of failure and mission impact.
4. **Balance Rigor with Resources**:

   * For lower-risk areas, leverage lightweight testing methodologies or informal verification, but always document the rationale for reduced rigor.
5. **Collaborate Across Roles**:

   * Encourage collaboration between small development teams and independent reviewers to bring additional perspectives and improve overall test quality.

---

### **References and Related Topics**

* **SWE-073 (Platform or High-Fidelity Simulations)**
* **SWE-065 (Test Plans, Procedures, and Reports)**
* **NASA-STD-8739.8** – Software Assurance and Software Safety Standards
* **Topic 8.17** – Incremental Verification and Validation for Small Projects
* **SWE-190 (Verify Code Coverage)**

---

Testing, even for small software projects, plays a critical role in ensuring safety, reliability, and mission success. By aligning testing rigor with risk, leveraging tools and resources judiciously, and maintaining thorough documentation, small projects can achieve NASA’s high standards for software quality and assurance while staying within resource constraints.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document, EI32-OI-001,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. See Chapter 12. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-008)

  [Acceptance Test Readiness Review (ATTR) Checklist,](https://nen.nasa.gov/web/software/nasa-software-process-asset-library-pal?p_p_id=webconnector_WAR_webconnector_INSTANCE_PA7b&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_webconnector_WAR_webconnector_INSTANCE_PA7b_edu.wisc.my.webproxy.URL=https%3A%2F%2Fdocs-nen.nasa.gov%2Fcloudrepo%2Ffile%2Fd3db8013-11eb-4820-928a-ce5626ff2f2c%2FPA2.5.4.3_ATRR_v2clean.docx "Click to open in new window")

  580-CK-032-02, Software Engineering Division, NASA Goddard Space Flight Center, 2010.
* (SWEREF-020)

  [Software Engineering Body of Knowledge (SWEBOK)](https://www.computer.org/education/bodies-of-knowledge/software-engineering "Click to open in new window")

  IEEE, Version 3.0 describes generally accepted knowledge about software engineering. Its 15 knowledge areas (KAs) summarize basic concepts and include a reference list pointing to more detailed information.
* (SWEREF-071) Acceptance Review Checklist,  NASA Marshall Space Flight Center (MSFC). This NASA-specific information and resource may be available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-112) Test Readiness Review Checklist,  NASA Marshall Space Flight Center. This NASA-specific information and resource may be available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-115) Verification Handbook, Volume 1: Verification Process,  MSFC-HDBK-2221, NASA Marshall Space Flight Center (MSFC), 1994.
* (SWEREF-152)

  [Software Testing Best Practices,](http://www.chillarege.com/authwork/TestingBestPractice.pdf "Click to open in new window")

  Chillarege, Ram (1999). Technical Report RC 21457 Log 96856. Center for Software Engineering/IBM Research.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-207)

  [The Software QA and Testing Resource Center - Table of Contents,](http://www.softwareqatest.com/ "Click to open in new window")

  Hower, Rick. (December, 2016), Software QA and Testing Resource Center,
* (SWEREF-234) Software Stress-Testing Guide,  JPL D-24472, NASA Jet Propulsion Laboratory (JPL), 2001. This NASA-specific information and resource may be available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-299)

  [Software Testing Hotlist, Resources for Professional Software Testers.](http://www.prismnet.com/~wazmo/qa/ "Click to open in new window")

  Pettichord, Bret, editor (August, 2001). In PrismNet: The Complete Business Internet.  Retrieved August 04, 2015 from http://www.prismnet.com/~wazmo/qa/.
* (SWEREF-469)

  [IEEE Computer Society, "IEEE Standard for Software Quality Assurance Plans,"](https://ieeexplore.ieee.org/document/6835311 "Click to open in new window")

  IEEE Std 730: 2014, 2014. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.
* (SWEREF-530)

  [MPL Uplink Loss Timer Software/Test Errors (1998)](https://llis.nasa.gov/lesson/939 "Click to open in new window")

  Public Lessons Learned Entry: 939.
* (SWEREF-537)

  [International Space Station Program/Hardware-Software/Qualification Testing-Verification and Validation](https://llis.nasa.gov/lesson/1104 "Click to open in new window")

  Public Lessons Learned Entry: 1104.
* (SWEREF-538)

  [International Space Station Program/Hardware-Software/Integration Testing](https://llis.nasa.gov/lesson/1106 "Click to open in new window")

  Public Lessons Learned Entry: 1106.
* (SWEREF-545)

  [Deep Space 2 Telecom Hardware-Software Interaction (1999)](https://llis.nasa.gov/lesson/1197 "Click to open in new window")

  Public Lessons Learned Entry: 1197.
* (SWEREF-685)

  [The Inquiry Board's Recommendations](https://www.esa.int/esapub/bulletin/bullet89/recom89.htm "Click to open in new window")

  Arianne 5 Inquiry Board - European Space Agency
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Process Asset Templates

**SWE-066 Process Asset Templates**

Click on a link to download a usable copy of the template.

* (PAT-026 - )

  [PAT-026 - TEST REVIEW CHECKLIST FOR TEST LEADS](https://swehb.nasa.gov/download/attachments/117211498/Test%20Review%20Checklist%20for%20Test%20Lead.docx?api=v2 "Click to open in new window")

  SWE-066, tab 3.3, Also in Testing Analysis, tab ? and Test Results and Documentation Process Asset Templates.
* (PAT-027 - )

  [PAT-027 - TEST REVIEW CHECKLIST FOR REVIEW TEAMS](https://swehb.nasa.gov/download/attachments/118161596/Test%20Review%20Checklist%20for%20Review%20Teams.docx?api=v2 "Click to open in new window")

  SWE-066, tab 7.4, Also in Peer Reviews, SA Tasking, Test Analysis, and Test Docs.
* (PAT-044 - )

  [PAT-044 - Software Hazard Development Process Audit](https://swehb.nasa.gov/download/attachments/198770763/PAT-044%20-%20Software%20Hazard%20Development%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Hazard Development Process.
* (PAT-046 - )

  [PAT-046 - Test Verification and Validation Process Audit](https://swehb.nasa.gov/download/attachments/198770767/PAT-046%20-%20Test%20Verification%20and%20Validation%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Test Verification and Validation Process.
* (PAT-056 - )

  [PAT-056 - Software Development Management Plan Assessment](https://swehb.nasa.gov/download/attachments/198770884/PAT-056%20-%20Software%20Development%20Management%20Plan%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Development - Management Plan. Based on the minimum recommended content for a Software Development - Management Plan.
* (PAT-061 - )

  [PAT-061 - Software Test Procedures Assessment](https://swehb.nasa.gov/download/attachments/198770894/PAT-061%20-%20Software%20Test%20Procedures%20Assessment.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for assessing the content of the Software Test Procedures document. Based on the minimum recommended content for a Software Test Procedures.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA’s extensive history of missions and software development efforts has provided valuable lessons on the importance of software testing in preventing mission failures, reducing risks, and ensuring the success of high-stakes projects. These lessons emphasize the critical role of rigorous testing, the involvement of end-users, exhaustive coverage of high-risk areas, and the necessity of addressing interactions between software, hardware, and environmental conditions.

This section consolidates lessons learned from NASA's **Lessons Learned Information System (LLIS)** and other significant programs, with additional insights to reinforce best practices for software testing.

---

### **6.1 Lessons Learned from NASA's Lessons Learned Database**

#### **1. Use of Software Before Complete Verification and Validation**

**Lesson Number: 1104**

* **Program**: International Space Station Program – **Hardware-Software Qualification Testing / Verification and Validation**
* **Key Lesson**:
  + Issue: Hardware and software were utilized before completing qualification testing, which resulted in potential invalidation of the test results.
  + Resolution:
    - Ensure **qualification testing** is complete before operational use, including end-to-end testing with hardware/software integration.
    - Changes made to hardware or software after incomplete testing necessitate re-verification under similar conditions to maintain test fidelity.

---

#### **2. Importance of End-User Involvement**

**Lesson Number: 1106**

* **Program**: International Space Station Program – **Hardware-Software Integration Testing**
* **Key Lesson**:
  + Astronaut crew participation in testing significantly improved test fidelity and helped familiarize the crew with operational systems and procedures.
  + Resolution:
    - Involve **end-users** (e.g., astronauts, operators, or engineers) in critical software testing processes.
    - End-user engagement ensures that tests reflect realistic scenarios and enable users to learn the system’s limitations and functions.

---

#### **3. Testing High-Risk Sequence Transitions**

**Lesson Number: 0939**

* **Program**: Mars Polar Lander (MPL) Uplink Loss Timer Software
* **Key Lessons**:
  1. Transitional mission phases (e.g., Entry, Descent, and Landing [EDL]) are inherently **high risk** and require extra planning for testing.
  2. Changes to database parameters that affect software logic (or system behavior) require re-testing of affected logic.
  + **Resolution**:
    - Design test plans that focus heavily on **testing transitional mission phases**, as these represent some of the most failure-prone operations.
    - Implement thorough **parameter integrity checks**, with all updated values validated against the intended logic.

---

#### **4. Integration of Software & Hardware in Operational Environments**

**Lesson Number: 1197**

* **Program**: Deep Space 2 Telecom Hardware-Software Interaction (1999)
* **Key Lessons**:
  + Issue: Testing software and hardware integration without assessing operational temperature ranges failed to mimic "as-flown" conditions.
  + **Recommendation**:
    - Implement the principle of **"Test as you fly, fly as you test."** Ensure integrated software and hardware systems are validated under expected **operational environmental conditions** (e.g., flight temperature ranges, radiation environments).
    - Integrate environmental testing criteria early into the project test plan.

---

#### **5. Comprehensive Retesting After Test Failures**

**Lesson Number: 0938**

* **Program**: Mars Polar Lander (Probable Mission Loss, 1998)
* **Key Lessons**:
  1. Establish a test policy clearly defining **mandatory retesting** when failures occur or flawed procedures are identified.
  2. Modified hardware or software must be retested unless there is documented justification for omission.
  3. Software requirements must reflect all known hardware operational behaviors, including anomalies (e.g., transients or spurious signals), and must be **verified via testing**.
  + **Resolution**:
    - For failures or aborted tests, rerun tests after correcting deficiencies in procedures or the system.
    - Ensure test plans explicitly document corrective actions to enhance traceability.

---

### **6.** Lessons Learned: Class D Budget and Schedule Pressure Leading to Reduced Software Maturity at ATLO

**Problem/Observation:**  
A combination of Class D mission constraints and schedule compression resulted in flight software (FSW) entering Assembly, Test, and Launch Operations (ATLO) with insufficient maturity. The Anomaly Review Board (ARB) highlighted several systemic contributors to this reduced readiness.

**Contributing Factors:**  
• Cancellation of the Janus mission reduced opportunities for heritage software reuse.  
• The IM‑2 rideshare shift forced accelerated delivery timelines.  
• Class D budget constraints limited staffing, depth, and robustness of software development and assurance activities.

**Resulting Impacts:**  
• FSW command sequences were still undergoing validation up to the eve of launch.  
• Key elements of the fault protection architecture entered ATLO in an immature state.  
• COTS software behaviors were not fully characterized before integration.  
• Critical end‑to‑end tests—such as SA phasing and GNC phasing—were never executed.

**Relevant SWEHB Guidance:**  
While Class D missions are allowed to tailor processes, the SWEHB still requires adherence to core engineering and assurance expectations, including:  
• SWE‑028, SWE‑065, SWE‑066: Verification planning and execution.  
• SWE‑057: Ensuring the software architecture is complete and validated.  
• SWE‑071, SWE‑073: Integrated testing, simulation, and end‑to‑end verification.

**Lesson Learned:**  
Regardless of mission class, flight software must reach sufficient maturity before entering ATLO. Tailoring does not remove the need for complete architectures, characterized behaviors, and integrated test evidence. The LTB demonstrates the risks introduced when these fundamentals are compressed or deferred, particularly in resource‑limited Class D environments.

### **7.** **Lesson Learned (Starliner CFT):** **Verification must be comprehensive and mission‑representative; limited evidence for critical systems is unacceptable.**

**Project Context:**  
Derived from Starliner CFT Investigation.

**Problem/Observation:**  
Qualification and integrated verification lacked full mission representativeness (environmental profiles, timing/network conditions, operational edge cases). Critical systems accepted with insufficient V&V evidence.

**Contributing Factors:**

* Test environments did not fully emulate flight dynamics, thermal ranges, and timing jitter.
* Limited end‑to‑end testing of safing and fault protection across sequences and FSW.

**Impacts:**

* Late discovery of functional gaps and system interactions.
* Increased risk entering integrated test and operations.

**Recommended Practices (Aligned to SWE‑028/065/066):**

* Create **mission‑representative test plans**: include environment profiles, timing/network conditions, off‑nominal paths.
* Require **evidence completeness reviews**: trace requirements → tests → results → defects/resolutions.
* Enforce **end‑to‑end verification** of safing and FP across all implementation paths (sequences + FSW).

**Actionable Checks:**

* Verification plans show explicit coverage of mission environments and edge cases.
* Traceability matrices demonstrate complete requirement‑to‑evidence mapping.
* End‑to‑end test reports include integrated FP/safing results.

### **8. Lessons Learned Beyond NASA**

#### **Ariane 5 Flight 501 Failure**

Ariane 5 rocket’s maiden flight resulted in a spectacular failure attributed to untested software behavior under actual launch conditions. The European Space Agency’s inquiry board provided recommendations reflecting valuable lessons:

1. **Prepare Realistic Test Environments**:

   * Develop a test environment using real hardware interfaces, simulated trajectories, and closed-loop system testing to replicate operational behavior accurately.
   * Prioritize complete, end-to-end system-level simulation before missions.
2. **Extend Test Coverage for Complex Components**:

   * Ensure the coverage of existing equipment is reviewed rigorously. Extend the testing of software components with a **high degree of complexity**, particularly those interacting with other critical subsystems.
3. **Synchronize Specification and Code Justifications**:

   * Maintain consistency between the software code and accompanying documentation (justification documents). Both must be updated concurrently to reflect the latest version.
4. **Formalize Qualification Procedures**:

   * Instill systematic qualification procedures, including stringent quality checks by an independent panel of **experts in Reliability, Availability, Maintainability, and Safety (RAMS).**
   * Enhance verification and testing of specification requirements for software critical to mission operations.

---

### **Additional NASA Lessons**

#### **9. Lessons for Unit and Integration Testing**

* Unit and integration testing often fail due to poor testing coverage or lack of attention to edge cases. Examples include:
  + Overlooking scenarios that involve **timing anomalies** (e.g., delayed data packets).
  + Insufficient input validation cases, where invalid inputs cause unexpected results.

**Resolution**:

* Expand unit and integration test cases to include all boundary conditions and fault scenarios. Ensure changes at lower levels (e.g., individual modules) are reflected in integration tests.

---

#### **10. Lessons for Regression Testing**

* Inadequate regression testing can lead to undetected defects reintroduced during system updates or modifications.

**Resolution**:

* Implement automated regression test suites to execute a comprehensive set of previous test cases after software updates. Validate that fixed defects remain resolved and no additional functionality has been negatively impacted.

---

#### **11. Lessons on Configuration Management**

* Automated testing environments can fail to reproduce past results due to insufficient configuration control. Missing dependencies, environment changes, or mismatched software baselines can invalidate future regressions.

**Resolution**:

* Implement strict **configuration management practices** for test environments. Fully document test dependencies, libraries, and hardware/software versions to ensure reproducibility.

---

### **Best Practices Derived from NASA Lessons**

1. Start **testing early** in development and progressively test as systems become more integrated.
2. Focus test resources on **high-risk transitions** and **safety-critical operations**.
3. Involve **independent test teams** or reviewers to challenge assumptions and improve fault detection.
4. Include **end-user participation** to improve test realism and familiarize users with potential anomalies.
5. Maintain **detailed documentation** to ensure changes, test failures, and corrective actions are traceable.

---

### **Summary**

NASA’s lessons emphasize the importance of comprehensive, rigorous, and well-documented software testing to ensure mission success. Adhering to these principles, reusing lessons learned, and integrating testing processes with **risk management frameworks** can prevent costly failures and deliver reliable systems even in high-stakes environments. Through application of successful practices, future projects can mitigate risks, reduce testing inefficiencies, and enhance overall system readiness.

## 6.2 Other Lessons Learned

* **All software requirements with multiple logic conditions require Formal Qualification Testing (FQT) to exercise all logic conditions.**
  + If unable to provide this via FQT, the FQT test designer must confirm coverage via other means, e.g., by leveraging lower-level unit tests.  Exceptions are to be documented and approved by the software control board.
  + Guidance for test case coverage must be documented.
* **Be judicious in identifying software flaws during testing**
  + Review all test scripts and test procedures for occurrences of non-flight-like actions. All occurrences must be approved (program to decide appropriate approval level).
  + Apply the ‘Test Like You Fly’ exception process to test scripts and procedures applied to the scenario and validation testing.
* **Hardware/software integration** **testing campaign** 
  + Avoid reliance on lower-level software tests to verify system-level requirements.
  + Hardware/Software Integration test campaign must be used to verify critical vehicle and system functions (system spec) and utilize a high fidelity test environment (e.g., flight-like hardware in the loop), especially for external and internal interfaces.
  + Ensure test rig configuration sufficiency for planned testing (e.g., sufficient real hardware included) and the data captured is analyzed.
* **Perform** **end-to-end** **mission scenario testing**
  + Programs must establish an end-to-end “run for record” test before each flight to include all applicable dynamic/critical phases of flight using a maximum available suite of flight hardware.
* **Simulation** **validation**
  + Simulations/emulations must be validated by the system provider **and** with real hardware data signatures.
  + Simulations/emulations must be kept in sync with hardware/software updates.
* **Increase** **involvement** **of SE&I in the development** **life cycle**
  + Quality spacecraft software development and test require deep and persistent partnership and joint accountability between SE&I, subsystem designers, software community, and external suppliers.
* **Software Change Tickets**
  + Any tests (formal or informal) that fail should be rerun and verified before software change tickets are closed, in the original environment, or as close to it as possible. Preferably this would be done with the original author of the software change ticket but with appropriate control board approval.
  + Be cautious about closing overlapping software change tickets to ensure that the full scope of all associated software change tickets is addressed via retest. Be careful about missing any unique elements to the individual software change ticket.
* **Modifications to board decisions**
  + Any aspects of control board decisions that are modified must be re-approved by the board (e.g., impacted artifacts that need updating).
* The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

  + [Test, test, and re-test, and "test as you fly"](https://software.gsfc.nasa.gov/lesson-details/4/). **Lesson Number 4**: The recommendation states: "Test, test, and re-test, and "test as you fly" are keys to successful development."
  + [Need for an expanded Project system V&V program](https://software.gsfc.nasa.gov/lesson-details/7/). **Lesson Number 7**: The recommendation states: "With increased SW complexity (e.g., multiple onboard computers) and functionality, there comes the need for an expanded Project system verification and validation program that cannot be compromised.  Increased capability also means increased SW costs."
  + [Hire people on the FOT side in prelaunch to focus on ground system testing](https://software.gsfc.nasa.gov/lesson-details/97/). **Lesson Number 97**: The recommendation states: "Hire 2-3 people on the FOT side in prelaunch to focus on ground system testing and not put this on the flight ops personnel of the FOT."
  + [Incorporate automation into operations prior to launch](https://software.gsfc.nasa.gov/lesson-details/98/). **Lesson Number 98**: The recommendation states: "Incorporate automation into operations prior to launch, instead of waiting until after launch."
  + ["Day in the Life" simulations using automation prior to launch](https://software.gsfc.nasa.gov/lesson-details/99/). **Lesson Number 99**: The recommendation states: "Execute "Day in the Life" simulations using automation prior to launch."
  + [Involving dedicated V&V team earlier is effective](https://software.gsfc.nasa.gov/lesson-details/286/). **Lesson Number 286**: The recommendation states: "If the project has a dedicated V&V team,  this team should get involved earlier, rather than waiting until developers make the software available to V&V for the start of the “formal” build testing. Overlapping development and V&V leads to reduced build testing time at the completion of build development, in favor of additional development time. Moreover, developers will get earlier feedback about defects and can address them as they are uncovered."
  + [Detailed timing measurements are needed to verify timing requirements](https://software.gsfc.nasa.gov/lesson-details/302/). **Lesson Number 302**: The recommendation states: "Systems with timing requirements by definition need to prove that the timing requirements are met.  The software development team will need a means to capture and interpret the system timing.  This may include using a system tool, a real time operating system tool, CFE timing tool, or external pins captured by a logic analyzer.  Take this need into account when planning the lab setup, as purchases will likely be required."
  + [Consider a streamlined review process for lower maturity products](https://software.gsfc.nasa.gov/lesson-details/332/). **Lesson Number 332**: The recommendation states: "Start with a small group for initial review, and then add reviewers later."
  + [Key Mission Ops Tests essential to timely V&V of flight design/mission ops concept& launch readiness](https://software.gsfc.nasa.gov/lesson-details/342/). **Lesson Number 342**: The recommendation states: "Develop/iterate/execute system level tests to verify/validate data system/mission Concept of Operations during Observatory I&T (e.g., the Comprehensive Performance Test (CPT) and Day-in-the-Life (DiTL) test). The CPT should be: a) thorough (exercising all copper paths, as many key data paths as reasonable, and using operational procedures); b) executed prior to/post significant events throughout Spacecraft & Observatory I&T; and c) designed comprehensive, yet short enough to be executed multiple times (e.g., the PACE CPT was specifically designed to be 4-5 days). The multi-pass DiTL test can demonstrate nominal operational procedures/processes and, when executed prior to the pre-environmental CPT, can be the basis for the instrument functionals during the environmental cycles and post environmental functional checkouts of the instruments."
  + [Goddard Dynamic Simulator (GDS) Fault Management derived Requirements](https://software.gsfc.nasa.gov/lesson-details/344/). **Lesson Number 344**: The recommendation states: "The Goddard Dynamic Simulator (GDS) team needs to review the GDS requirements when the fault management table is initially defined (as well as when there are changes to the tables), and during the FSW Build Testing phase, at the start of Systems Testing. This review should include working with the Flight Software team at the contents of the Fault Detection and Correction (FDC) tables to determine what telemetry needs to be simulated. This review may result in new GDS requirement(s)."
  + [Test all commands to GNC simulated hardware](https://software.gsfc.nasa.gov/lesson-details/345/). **Lesson Number 345**: The recommendation states: "Once the Spacecraft Command and Telemetry database is established, test all defined GNC hardware commands against the spacecraft simulator."

# 7. Software Assurance

**SWE-066 - Perform Testing**

4.5.3 The project manager shall test the software against its requirements.

This section has been refined to provide clearer and more actionable guidance on the role of software assurance in software testing, the necessary metrics to monitor progress, and the processes for ensuring the readiness of testing efforts. The improvements emphasize best practices for reviewing tests, ensuring test traceability, validating safety-critical functions, and improving test management for various types of projects, including those involving Artificial Intelligence (AI) and Machine Learning (ML).

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm test coverage of the requirements through the execution of the test procedures.

2. Perform test witnessing for safety-critical software.

3. Confirm that any newly identified software contributions to hazards, events, or conditions found during testing are in the system safety data package.

---

## 7.2 Software Assurance Products

Software Assurance (SA) plays a critical role in ensuring software safety, effectiveness, and compliance with testing objectives. SA should validate the completeness and accuracy of the following products:

1. **Test Witnessing Signatures**:

   * Evidence demonstrating that software assurance has directly observed and verified critical tests, particularly for safety-critical systems.
2. **Test Coverage Metrics**:

   * Data that confirms the extent of requirements and code coverage achieved through testing (see Section 7.3 Metrics).
3. **Confirmation of Hazard Resolution Testing**:

   * Validation that the system safety data package includes all newly identified software-related contributions to hazards, conditions, or events discovered during testing.
4. **Software Test Artifacts**:

   * **Test Plans**: Ensure the completeness and alignment of planned tests with requirements and hazard controls.
   * **Test Procedures**: Review for accuracy, completeness, and bidirectional traceability to both requirements and test results.
   * **Test Reports**: Verify that these reports clearly document outcomes, including the details of passed/failed tests, any anomalies, and corrective actions.

---

## 7.3 Key Metrics for Software Assurance

Software testing metrics are critical for monitoring progress, evaluating coverage, identifying gaps, and ensuring compliance with project objectives. The following set of metrics can help Software Assurance track testing activities effectively:

#### **Core Testing Metrics (Required by All Projects)**:

* **# of Software Requirements** (at various levels: project, application, subsystem, system).
* **# of Software Requirements with Completed Test Procedures/Cases Over Time**.
* **# of Safety-Critical Requirement Verifications Completed vs. Total # of Safety-Critical Requirement Verifications**.
* **# of Source Lines of Code (SLOC) Tested vs. Total SLOC**.
* **Percentage of Software Code/Test Coverage for Safety-Critical Components** (e.g., # of tested paths vs. total paths).
* **Total # of Tests Completed vs. Total # of Test Results Evaluated and Signed Off**.
* **# of Tests Executed vs. Total # of Tests Completed**.
* **# of Safety-Critical Tests Executed vs. # of Safety-Critical Tests Witnessed by SA**.

#### **Additional Recommended Metrics**:

* **# of Requirements Tested vs. Total # of Requirements**.
* **# of Detailed Software Requirements Tested to Date vs. Total # of Detailed Software Requirements**.
* **# of Open Issues vs. Closed Issues Over Time**.
* **# of Hazards Containing Software Tested vs. Total # of Hazards Containing Software**.
* **# of Non-Conformances Identified (Open/Closed/Severity)—Tracked Per Testing Phase**.
* **# of Requirements with Issues (Open/Closed) Over Time**.
* **# of Software Requirements Without Associated Test Cases**.
* **# of Requirements Being Met via Satisfactory Testing vs. Total # of Requirements**.
* **# of Safety-Related Non-Conformances Tracked Over the Lifecycle**.
* **# of TBD/TBC/TBR Requirements (To Be Determined, Confirmed, Resolved)—Trended Over Time**.
* **# of Non-Conformances Identified While Verifying Hazard Controls via Test Procedures**.

#### **Usage of Metrics**:

* Metrics should be **reviewed periodically** to evaluate progress on testing milestones.
* Action plans should be developed to address metrics showing insufficient test coverage, an increasing number of open issues, or incomplete hazard verifications.

> **Note**: Bolded metrics are recommended for all projects. Refer to Topic 8.18 for further SA-suggested metrics.

---

## 7.4 Software Assurance Guidance

### **7.4.1 Review of Test Procedures, Plans, and Results**

* **Test Procedure and Test Plan Review**:
  + Ensure **bidirectional traceability** between test procedures and requirements (refer to SWE-052 for traceability).
  + Validate that all **safety-critical features** are captured in the test plan and traced back to hazard reports, requirements, and expected operational scenarios.
* **Test Results and Witnessing**:
  + Review test outcomes or witness the tests directly to confirm:
    - Test coverage aligns with predefined requirements.
    - Safety-critical validations (nominal, off-nominal, stress, and error conditions) are successfully passed.
  + Validate that **regression testing** is performed after every software modification.

### **7.4.2 Safety-Critical and Hazard-Related Testing**

* The presence of **safety-critical code** necessitates added scrutiny by SA:
  + All safety-related software functionality must be tested under:
    - **Nominal Conditions**: Expected operating conditions.
    - **Off-Nominal Conditions**: Edge and failure scenarios.
    - **Stress Conditions**: High-load environments.
    - **Error Conditions**: Situations requiring safe-mode execution.
  + Confirm all **hazards reported in the safety data package** are addressed through relevant test cases. Include hazard closure validations (refer to SWE-192).

### **7.4.3 Regression Testing**

* SA ensures that regression tests:
  + Cover **all identified safety-critical functions**.
  + Validate that fixes do not reintroduce old defects or cause new impacts on unrelated functions.
  + Include tests affected by requirements or parameter updates during the test process.

### **7.4.4 Formal Qualification Testing (FQT)**

* All software requirements that involve multiple logical conditions must undergo **Formal Qualification Testing (FQT)**. This ensures all possible paths and conditions have been evaluated.
* If certain conditions cannot be tested during FQT, unit or lower-level tests must be used to validate coverage.
* Document and approve exceptions to complete coverage through the **software control board.**

#### **Extra Guidance for AI-ML Projects**

* AI/ML systems introduce unique testing and assurance challenges:
  + Verify AI/ML behavior under a variety of **training, operational, and failure conditions**.
  + Validate the decisions of AI/ML software are explainable, traceable, and aligned with mission objectives.
* Refer to **Topics 7.25 and 8.25** for additional AI/ML-specific software assurance guidance.

---

### **7.4.5 Test Readiness Guidance**

#### **For Review Teams**:

* Use the **TEST REVIEW CHECKLIST FOR REVIEW TEAMS** to assess the project’s readiness for testing. Key items to evaluate include:
  + Maturity and completeness of test artifacts.
  + Development readiness for transitioning to the testing phase.

#### **For Test Leads**:

* Use the **TEST REVIEW CHECKLIST FOR TEST LEADS** to confirm:
  + Processes and preparations are in place for efficient and effective testing.
  + All configurations and dependencies required for full test coverage are accounted for.

Test readiness assessments should include criteria for test environment maturity, software stability, and alignment of the test scope with identified risks and objectives.

---

### **Summary of Software Assurance Roles in Testing**

1. **Test Validation and Witnessing**:

   * Ensure independent review and validation of all safety-related tests.
   * Witness tests where required by project classification or risk.
2. **Metrics Tracking and Analysis**:

   * Routinely analyze test metrics to identify gaps or risks in the testing process.
3. **Regression and Qualification Testing**:

   * Confirm all changes are followed by comprehensive regression tests and identify critical areas requiring FQT.
4. **Focus on Safety and Hazard Controls**:

   * Prioritize evaluations of safety-critical components and ensure hazard-related software functions are fully tested.
5. **AI/ML-Specific Testing**:

   * Implement rigorous validation and explanation criteria for AI/ML functionalities, ensuring alignment with project goals.

By following these guidelines, Software Assurance ensures that all testing activities align with project objectives, adhere to safety and quality standards, and mitigate risks in mission-critical software development.

#### AI-ML Software

If Artificial Intelligence software is to be used, see topics [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) and [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action),        * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.25 - Artificial Intelligence And Software Engineering](/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [8.25 - Artificial Intelligence And Software Assurance](/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [PAT-026 - Test Review Checklist For Test Leads](/spaces/SITE/pages/117211498/PAT-026+-+Test+Review+Checklist+For+Test+Leads) * [PAT-027 - Test Review Checklist For Review Teams](/spaces/SITE/pages/118161596/PAT-027+-+Test+Review+Checklist+For+Review+Teams) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical for demonstrating compliance with software testing activities and ensuring that all requirements (functional, performance, safety-critical, and interface) are satisfied. This evidence provides a verifiable trail that confirms the testing process followed all relevant standards and guidelines.

Below is a comprehensive list of objective evidence that should be generated and maintained for this requirement, organized by stages of the testing lifecycle:

---

### **1. Test Planning Evidence**

**Purpose**: To demonstrate that tests are planned, requirements are traceable, and test procedures are prepared and approved before execution.

#### Artifacts:

* **Software Test Plan**:
  + Evidence of compliance with documented requirements.
  + Description of testing approach (e.g., unit, integration, system, regression, safety-critical tests) and alignment with risk priorities.
  + Test environment descriptions (e.g., hardware/software configuration, simulators).
* **Test Traceability Matrix (TTM)**:
  + A table linking every software requirement to its corresponding test procedure, identification numbers, and test cases.
  + Ensures bidirectional traceability between requirements and test artifacts (see **SWE-052**).
    - **Forward Traceability**: All requirements have matching tests.
    - **Backward Traceability**: All tests correspond to one or more requirements.
* **Defined Entry/Exit Criteria for Testing**:
  + Criteria for transitioning between testing phases (e.g., readiness for integration or system testing).
* **Checklist for Test Readiness**:
  + Evidence derived from the **TEST REVIEW CHECKLIST FOR REVIEW TEAMS** or **TEST REVIEW CHECKLIST FOR TEST LEADS**.

---

### **2. Test Procedure Evidence**

**Purpose**: To verify that detailed and approved procedures exist for conducting tests under specified conditions, including safety-critical and off-nominal scenarios.

#### Artifacts:

* **Approved Software Test Procedures**:
  + Step-by-step instructions for executing each test case.
  + Clearly defined objectives, expected results, and conditions of execution.
  + Coverage of nominal, off-nominal, stress, and recovery scenarios (see **Topic 8.01 - Off-Nominal Testing**).
* **Annotated Test Sets**:
  + Documentation of test datasets to be used with specific test cases, including boundary conditions, failure scenarios, and stress environments.
* **Testing Constraints Documentation**:
  + Any limitations related to testing (e.g., cannot test specific hardware in-flight).
  + Simulator or model performance versus real hardware capabilities.

---

### **3. Test Execution Evidence**

**Purpose**: To confirm that all planned testing activities have been carried out under the specified conditions and any deviations were documented and justified.

#### Artifacts:

* **Test Execution Logs**:
  + Detailed logs of test runs, capturing:
    - Date, time, environment configurations, and test personnel.
    - Test inputs, outputs, and test execution status (e.g., Passed, Failed, Blocked, Skipped).
  + Evidence of regression testing for all software modifications after the original test plan (see **SWE-191**).
* **Software Test Witnessing Signatures**:
  + Evidence that Software Assurance (SA) or authorized individuals witnessed critical tests and verified execution integrity, especially for **safety-critical software**.
* **Dynamic Testing Results**:
  + Test results demonstrating observed versus expected behavior (e.g., pass/fail outputs, discrepancies).

---

### **4. Test Coverage and Validation Evidence**

**Purpose**: To ensure thorough testing, address untested paths, and confirm all software logic is verified.

#### Artifacts:

* **Code Coverage Reports (Structural Coverage Analysis)**:
  + Results from tools like gcov, JaCoCo, or LDRA showing the percentage of the code executed during tests:
    - Include **function, statement, branch, and decision coverage**, especially for safety-critical paths.
  + Mapping of tests to untested areas and plans to address gaps.
* **Regression Test Results**:
  + Evidence of successful execution of the regression test suite after any software changes.
  + Comparison with results from earlier testing to ensure no regressions occurred.
* **Test Discrepancy Logs (Non-Conformance Reports)**:
  + Documented discrepancies, anomalies, or failed tests.
  + Any required corrective actions, including:
    - Root cause analysis.
    - Retesting evidence to close discrepancies.

---

### **5. Safety and Hazard Evidence**

**Purpose**: To validate that testing addressed all safety-critical software and ensured hazards were mitigated or controlled.

#### Artifacts:

* **Safety-Critical Testing Results**:
  + Evidence that all hazard-specific requirements were tested successfully.
  + Results of tests covering fault recovery, safety inhibits, and "safe mode" functions.
* **Hazard Reports Addressed Through Tests**:
  + Confirmation that all software contributions to hazards (found in safety data packages) were tested and resolved during verification.
  + Evidence of SA review and sign-off for hazard traceability (see SWE-192).
* **Off-Nominal and Stress Testing Results**:
  + Test outcomes proving software handles edge cases beyond typical operational conditions without failure.

---

### **6. Test Results and Reporting Evidence**

**Purpose**: To document the results of all executed tests and demonstrate changes made based on test outcomes.

#### Artifacts:

* **Test Reports**:
  + Summarized outcomes of all tests, indicating:
    - Passed, failed, or blocked test cases.
    - Any anomalies or observations requiring further investigation.
    - Coverage metrics and unmet requirements.
* **Metrics Reports**:
  + Tracked metrics over time, including:
    - Safety-critical functions tested vs. total safety-critical:
      * **(# Safety Tests Completed vs. Total Safety Tests)**
    - Percentage of code/test coverage for safety-critical components.
    - **Test Completion Rates**:
      * **(# Completed Tests vs. Total # Tests Planned)**
      * **(Completion Rates for Critical vs. Non-Critical Requirements)**.
* **Updated Traceability Matrices**:
  + Confirm coverage for all requirements and trace unmet requirements or gaps to corresponding open issues.
  + For example:
    - Identify software functionalities without test cases.
    - Update test cases for new/changing requirements as part of regression testing.

---

### **7. Non-Conformance and Issue Resolution Evidence**

**Purpose**: To ensure defects or anomalies identified during testing are documented, corrected, and verified.

#### Artifacts:

* **Non-Conformance Reports**:
  + List of all software non-conformances identified during testing, organized by severity.
* **Defect Tracking and Resolution Logs**:
  + Documented lifecycle for all defects from discovery to resolution, including retesting evidence after resolution.
* **Change Management Logs**:
  + Records of software changes (tracked per **SWE-080**) and associated regression testing evidence.

---

### **8. Other Supplementary Evidence**

Depending on the project size, scope, and criticality, the following evidence may also be required:

* **Simulation Environment Validation Reports**:
  + Confirm the simulation environment is high fidelity and matches operational conditions.
* **Test Readiness Review (TRR) Minutes and Approvals**:
  + Evidence that the testing team and stakeholders approved test readiness.
* **Formal Qualification Testing (FQT) Results**:
  + Evidence all logic paths for requirements with multiple conditions were tested (or documented exceptions with approval).
* **AI/ML-Specific Test Results (if applicable)**:
  + AI-specific testing evidence (e.g., training data integrity, behavioral testing, and explainability).

---

### **Summary**

To comply with **Requirement 4.5.3**, objective evidence must show that software testing:

1. Fully aligns with requirements (functional, performance, safety-critical).
2. Covers all code paths and essential scenarios (nominal and off-nominal).
3. Provides verifiable results and resolutions for failures, with full traceability.

Maintaining comprehensive, well-organized evidence enables efficient reviews, supports audit compliance, and ensures overall mission success.

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
