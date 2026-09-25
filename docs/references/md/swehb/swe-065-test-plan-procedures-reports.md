# SWE-065 - Test Plan Procedures Reports

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695448. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports

SWE-065 - Test Plan, Procedures, Reports

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695448)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695448&showCommentArea=true&showComments=true#addcomment)

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

4.5.2 The project manager shall establish and maintain: 

a. Software test plan(s).  
b. Software test procedure(s).  
c. Software test(s), including any code specifically written to perform test procedures.  
d. Software test report(s).

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-065 History

SWE-065 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.4.1 The project shall establish and maintain:         a.    Software Test Plan(s).         b.    Software Test Procedure(s).         c.    Software Test Report(s). |
| Difference between A and B | No change |
| B | 4.5.2 The project manager shall establish and maintain:         a.    Software test plan(s).         b.    Software test procedure(s).         c.    Software test report(s). |
| Difference between B and C | No change |
| C | 4.5.2 The project manager shall establish and maintain:   1. 1. Software test plan(s).    2. Software test procedure(s).    3. Software test report(s) |
| Difference between C and D | Requirement updated to added tests and code (item c). |
| D | 4.5.2 The project manager shall establish and maintain:   a. Software test plan(s). b. Software test procedure(s). c. Software test(s), including any code specifically written to perform test procedures. d. Software test report(s). |

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
| [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 2. Rationale

Having plans and procedures in place ensures that all necessary and required tasks are performed and performed consistently. The development of plans and procedures provides the opportunity for stakeholders to give input and assist with the documentation and tailoring of the planned testing activities to ensure the outcome will meet the expectations and goals of the project. Test reports ensure that the results of verification activities are documented and stored in the configuration management system for use in acceptance reviews or readiness reviews.

Ensuring the test plans, procedures, and reports follow templates ensures consistency of documents across projects, ensures proper planning occurs, ensures proper activity and results are captured, and prevents repeating problems of the past.

Ensuring high-quality, reliable, and mission-compliant software for NASA projects requires a well-defined and robust testing process. This requirement mandates that the project manager establish and maintain critical artifacts—test plans, test procedures, tests, and test reports—because these documents and outputs serve as a foundation for validating the software against its requirements and proving its readiness for deployment. Below is a detailed rationale for each part of the requirement:

---

### **Requirement 4.5.2a: Software Test Plan(s)**

#### **Rationale:**

The **Software Test Plan (STP)** is the roadmap for the testing process. It defines the "what, why, when, where, and how" of testing, ensuring a structured approach to verifying software functionality, performance, and reliability.

* **Purpose of the Test Plan**:

  + Establishes the scope, objectives, environmental prerequisites, and resources required for software testing.
  + Provides a comprehensive overview of testing activities, including schedules, levels of testing (e.g., unit, integration, system, acceptance testing), and testing criteria.
  + Serves as a control mechanism to ensure all necessary testing is aligned with the project lifecycle and system-level milestones.
* **Importance**:

  + Ensures that all stakeholders (e.g., developers, test engineers, managers) share the same understanding of testing expectations.
  + Mitigates project risks by identifying and planning for resource limitations, schedule constraints, and potential testing challenges before issues arise.
  + Documented testing roadmaps are especially critical for safety- or mission-critical systems, where precise testing practices ensure mission success.

---

### **Requirement 4.5.2b: Software Test Procedure(s)**

#### **Rationale:**

The **Software Test Procedure(s)** translate the test plan into actionable testing activities by detailing the step-by-step instructions for executing test cases.

* **Purpose of the Test Procedures**:

  + Define the "how" of execution for each test identified in the test plan, including setup, execution steps, inputs, expected outputs, and pass/fail criteria.
  + Ensure the repeatability of the test process, even when executed by different testing personnel.
  + Provide detailed actions that allow for traceability between requirements, test cases, and defects uncovered during testing.
* **Importance**:

  + Establishes consistency and precision, ensuring that the software is tested against all functional and non-functional requirements without deviation or oversight.
  + Increases test coverage, as well-defined procedures ensure that edge cases, corner cases, and integration points are systematically tested.
  + Facilitates efficient troubleshooting by outlining failure recovery actions, evaluation criteria, and steps for post-test analysis.
  + Ensures traceability and compliance with NASA standards and guidelines, particularly for safety- and mission-critical systems.
  + Procedures also provide evidence during post-mission audits that thorough and systematic testing was performed.

---

### **Requirement 4.5.2c: Software Test(s), Including Any Code Specifically Written to Perform Test Procedures**

#### **Rationale:**

The **Software Tests** refer to the actual execution of planned and procedural actions to evaluate the software's behavior or performance under specified conditions. In addition to tests themselves, code written specifically to support testing (e.g., test scripts, stubs, drivers, simulators) must also be maintained because it directly ensures proper testing coverage.

* **Purpose of the Tests**:

  + Provide tangible results on whether the software meets its functional and performance requirements.
  + Detect and diagnose errors, oversights, or inconsistencies in the software to ensure its reliability before deployment.
  + Validate interactions between software components, between the software and the hardware, and between the software and external systems.
* **Importance**:

  + Helps uncover critical bugs early in the development cycle, reducing cost and schedule risk.
  + For mission-critical systems, testing is the only way to simulate real-world scenarios that the system will face, including failures, anomalies, or extreme inputs.
  + Test code (e.g., stubs and drivers) ensures that test scenarios can address software in isolation, allowing defective subsystems to be identified without contamination from other parts of the system.
  + Comprehensive testing, including boundary, stress, regression, and interface testing, ensures software robustness and reliability under worst-case conditions.

---

### **Requirement 4.5.2d: Software Test Report(s)**

#### **Rationale:**

The **Software Test Report (STR)** serves as the formal documentation of testing efforts, outcomes, and resulting evaluations. It confirms whether the system has met its testing objectives and provides evidence of software maturity.

* **Purpose of the Test Reports**:

  + Summarizes test results, identifying tests that passed, failed, or encountered unexpected behavior.
  + Provides analysis of failures or anomalies encountered during testing, including root cause analysis and corrective action reports.
  + Captures deviations from the test plan or procedure, documenting their resolution or justification.
  + Provides a historical record of testing activities, outcomes, and overall confidence in the product's reliability for stakeholders or auditors.
* **Importance**:

  + Ensures accountability and transparency in the testing process, allowing technical leads and managers to confidently endorse system readiness.
  + Demonstrates traceability between project requirements and test results, ensuring that all requirements (functional, performance, safety) have been tested thoroughly.
  + Generates evidence for NASA's rigorous safety and quality assurance processes, thereby serving as formal documentation for agency reviews, external authorities, or mission partners.
  + Test reports serve as a key reference in future lifecycle phases, especially when evaluating issues discovered post-launch or during operational use.

---

### **Overall Importance of Maintaining These Testing Artifacts**

1. **Risk Mitigation**:

   * Testing is the frontline defense against software defects reaching mission-critical operations. These artifacts (plans, procedures, tests, and reports) ensure that errors are detected and resolved early in the lifecycle, minimizing risks to cost, schedule, and mission success.
2. **Compliance and Certification**:

   * NASA projects operate under strict safety, quality, and mission assurance requirements. Testing artifacts provide demonstrable evidence of compliance with agency standards and guidelines, without which key stakeholders may not approve or certify system readiness.
3. **Repeatability and Reproducibility**:

   * Documented test plans, procedures, and reports allow tests to be repeated across teams, facilities, and lifecycle phases. This is essential for regression testing during updates, upgrades, or maintenance activities.
4. **Traceability and Accountability**:

   * Testing artifacts establish traceability between software requirements, testing activities, and final deliverable quality. This fosters accountability among teams and ensures that no requirement is overlooked or inadequately tested.
   * For example, a test failure can be traced back to its source (requirement, code, or design defect), enabling focused corrective action.
5. **Support for Audits and Stakeholder Confidence**:

   * NASA missions are often scrutinized by internal and external entities. Well-maintained testing artifacts provide stakeholders with confidence that every necessary step has been taken to validate and verify the software.
6. **Preparation for Real-World Scenarios**:

   * The increasingly complex and autonomous nature of modern NASA systems requires rigorous testing to ensure the software behaves predictably in real-world conditions. Test plans, procedures, and results ensure the system is validated for extreme edge cases and operational anomalies.
7. **Facilitates Knowledge Transfer and Scalability**:

   * Detailed testing documents help future teams understand project testing history, workflows, and decisions. This is invaluable when scaling existing systems or developing derivatives of prior software.

---

### **Alignment with NASA's Mission Assurance Philosophy**

NASA mandates stringent software assurance processes for all projects, particularly those involving flight and mission-critical systems. This requirement directly supports the agency's goals to minimize mission risk, maintain software quality, and ensure the safety of crew members, hardware, and scientific payloads.

By developing and maintaining detailed test plans, procedures, tests, and reports, projects can ensure the software functions as intended, is robust under all operating conditions, and aligns with NASA's high standards for mission success and safety.

# 3. Guidance

To ensure the successful execution of software testing and adherence to NASA's high standards for quality, safety, and reliability, this enhanced guidance establishes clear expectations for creating, executing, documenting, and maintaining test plans, procedures, and reports. Following these principles ensures traceability, accountability, and the ability to adapt dynamically to project changes.

---

### **1. Software Test Plans, Procedures, and Reports: Comprehensive Development Guidelines**

#### **Test Plans (STP)**:

1. **Objective**:

   * Define the scope, purpose, and strategy for software testing activities, including responsibilities, resources, test levels, and test timelines.
   * Establish high-level testing goals to ensure that all software requirements (functional, performance, safety, and interface) are met.
2. **Content Recommendations**:

   * Use the content guidance from **Topic 5.10 - Software Test Plan (STP)** to include:
     + Scope of testing.
     + Test objectives and test levels (unit, integration, system, regression, etc.).
     + Roles and responsibilities for test execution.
     + Tools, environments, and hardware/software configurations.
     + Risk assessment and mitigation plans for testing.
     + Resource estimates, schedules, and budget allocations.
3. **Planning for Progressive Builds**:

   * For software developed in multiple builds, test plans must include phased validations to ensure requirements implemented incrementally in earlier builds are tested thoroughly. Final testing should incorporate end-to-end integration and verification.

---

#### **Test Procedures**:

1. **Objective**:

   * Provide detailed, actionable instructions for executing each test case identified in the test plan.
   * Ensure consistency and repeatability across execution efforts by clearly defining inputs, expected outputs, and step-by-step actions.
2. **Guidelines**:

   * Develop test cases that align with **SWE-187** and documented through **Topic 5.14 - Test Procedure Guidance**:
     + Covering all functional and design requirements, including boundary conditions, error handling, and performance constraints.
     + Addressing all software interfaces between internal and external systems or units.
     + Including stress, load, and fault recovery tests to simulate real-world and worst-case scenarios.
   * Include procedural steps to evaluate:
     + Limits and boundary condition handling.
     + Algorithms and correctness of calculations.
     + Operational accuracy of hazard mitigations and fault recovery mechanisms.
3. **Reuse and Legacy Software**:

   * Legacy or reused software components must undergo comprehensive testing with updated requirements to ensure compatibility and correctness:
     + Test all modified components.
     + Test all critical components, regardless of whether they were modified.
     + Target components with known or past performance risks.
4. **Dry Runs**:

   * Require all software test procedures to undergo dry runs to:
     + Confirm procedure completeness and adequacy.
     + Ensure tools, test data, and environmental resources are ready.
     + Identify potential gaps or missing steps prior to formal execution.

---

#### **Test Execution**:

1. **Independence in Testing (Topic 3.1)**:

   * Establish clear independence in software testing for Classes A, B, and safety-critical Class C software:
     + Testers must be independent of the personnel responsible for the detailed design, implementation, or unit testing of the software item.
     + Design and implementation knowledge contributors are encouraged to assist in the process by providing test case insight.
   * Independence reduces bias and improves defect detection during testing.
2. **Testing in the Target Environment (Topic 3.3)**:

   * Perform qualification and final testing on hardware that closely matches the target system's operational configuration, including:
     + Processor architecture, memory size, timing, and performance characteristics.
     + Interfaces and data I/O rates.
     + High-fidelity simulations (see **SWE-073 - Platform or Hi-Fidelity Simulations**).
   * Testing on high-fidelity hardware ensures that system-level performance, timing, and operational requirements are met.
3. **Test Rig Sufficient for Objectives**:

   * Verify that test configurations include sufficient hardware and software fidelity to comprehensively simulate actual use conditions. This minimizes the introduction of false negatives due to unrealistic environmental constraints.

---

#### **Test Reports**:

1. **Objective**:

   * Document the outcomes of the software testing, analyze results, assess anomalies, and provide traceability to test plans and procedures.
2. **Key Content**:

   * Include all required artifacts described in **Topic 5.11 - Software Test Report Guidance** and ensure the report covers:
     + Test cases executed, pass/fail results, and deviations from expected outcomes.
     + Analysis of data captured during testing, including evidence of requirement fulfillment.
     + Any failures or anomalies observed, accompanied by root cause analysis and recommendations for corrective actions.
   * Confirm traceability between test results and project requirements, test plans, and procedures.

---

### **2. Specialized Testing Recommendations**

#### **Regression Testing (SWE-191)**:

* After any modification (e.g., bug fixes, enhancements, or new requirements), regression testing must be conducted to ensure no unintended impacts on previously tested functionality. Include test procedures to validate:
  + Newly modified or added code.
  + Existing functionality and interfaces against updated code.

#### **Fault Recovery and Robustness Testing**:

* Create test cases that simulate fault and recovery scenarios to evaluate:
  + The software’s ability to detect, respond to, and recover from failures.
  + Correct operation during low-power modes, unexpected shutdowns, or resource unavailability.

#### **Stress and Performance Testing**:

* Evaluate the software's ability to operate under peak loads, high data rates, and adverse environmental conditions.

---

### **3. Documentation Maintenance**

#### **Dynamic Updates to Test Plans, Procedures, and Reports**:

1. **Trigger Points for Updates**:

   * Updates are required when:
     + The project design evolves, or requirements change (**SWE-071**).
     + New test tools or resources are introduced.
     + Test results identify inadequacies in coverage or procedures.
   * Test documents must also evolve when software classification or safety-criticality changes.
2. **Change Management**:

   * Incorporate updates via formal review and approval processes. Changes must be reviewed, peer-inspected, and validated to align with evolving project needs.

---

### **4. Software Assurance Role in Testing**

1. **Witness Testing**:

   * Ensure software test procedures are dry-run before formal witnessed testing (Topic 3.4). The presence of software assurance during formal tests ensures:
     + Procedures are executed as planned.
     + Results are properly documented and discrepancies addressed.
   * Review results to confirm whether requirements verification and validation are complete.
2. **Review Analysis and Documentation**:

   * Software assurance must evaluate test reports to verify:
     + Coverage of all requirements.
     + Adequacy of regression tests and failure analyses.
     + Updates accurately reflect changes to requirements or system configurations.

---

### **5. Process Improvement and Best Practices**

1. **Leverage Historical Data**:

   * Integrate lessons learned from previous projects (reuse test assets where applicable) to improve efficiency and reduce risks.
2. **Incorporate Metrics and Audits**:

   * Track metrics for test effectiveness (e.g., defect density, requirements coverage, open vs. closed defects).
   * Audit the testing process to ensure adherence to documented plans and procedures.

---

Adhering to these guidelines ensures comprehensive, repeatable, and traceable testing processes, ultimately contributing to the software's safety, reliability, and mission success. Software testing is not only a verification and validation activity—it forms the cornerstone of high-quality software engineering.

Projects create test plans, procedures, and reports following the content recommendations in topic [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance). [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan), [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures),

See also Topic [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels), [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing),

see [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations))

See also Topic [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009)

See also Topic [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing), [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification)

See also Topic [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report),

NASA users should consult Center Process Asset Libraries (PALs) for Center-specific guidance and resources related to the test plan, test procedures, and test reports, including templates and examples.

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification)       * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

For small projects, it is essential to streamline test documentation to reduce overhead while ensuring that sufficient testing rigor is maintained. Small projects often have limited resources, including personnel, time, and budget, requiring a practical approach to meet testing objectives. The following enhanced guidance provides strategies to balance efficiency with quality in software testing documentation.

---

### **1. Combining Test Documentation**

Small projects can benefit from combining various test documents to reduce duplication of effort and simplify management while maintaining traceability and thoroughness.

#### **Best Practices**:

1. **Test Plan, Procedures, and Results in a Single Document**:

   * Instead of creating separate documents for the **Software Test Plan (STP)**, **Software Test Procedures (STPR)**, and **Test Results**, small projects can consolidate them into one unified document.
   * In this format:
     + Use one section to define test objectives, scope, and responsibilities.
     + Detail the step-by-step test procedures, with space to directly record test results and observations.
     + Include placeholders for analyzing results and documenting anomalies or corrective actions.

   **Benefits**:

   * Reduces the number of deliverables to manage, review, and maintain.
   * Provides end-to-end traceability in a single location.
   * Simplifies updates when requirements or procedures change.
2. **Templates with Embedded Result Fields**:

   * Develop test procedures with embedded fields for directly capturing test results.
     + Example: Test step descriptions, input/output parameters, execution timestamps, pass/fail status, and remarks can all be documented in the same table or structured section.
   * This reduces the need for separate, standalone test results documents while ensuring that results are directly traceable to their corresponding procedures.
3. **Leverage Lightweight Documentation**:

   * Use concise formats such as tables or checklists for smaller test cases or simpler software modules:
     + Include basic fields such as test ID, requirement verified, test description, expected result, actual result, pass/fail status, and notes.
   * Avoid excessive formality while still adhering to essential documentation standards.

---

### **2. Standardized Testing Frameworks**

For organizations that manage multiple small projects, establishing standardized testing documentation and processes can reduce repeated efforts while ensuring consistency across all projects.

#### **Framework Development**:

1. **Create Flexible, Modular Templates**:

   * Develop standardized templates for:
     + Test Plans: Include placeholders for custom project-specific information, such as scope, resource allocation, and schedules.
     + Test Procedures: Provide a baseline set of procedural steps that can be tailored for each project, reducing the need to create procedures from scratch.
     + Test Reports: Include pre-defined fields for results summaries, trends, and analysis.
   * Templates should follow best practices but remain lightweight, allowing projects to complete only the sections relevant to their needs.
2. **Include a Checklist-Driven Approach**:

   * Standardize testing processes using checklists that align with high-level requirements:
     + Ensure coverage for key areas such as functional verification, performance testing, boundary testing, and fault recovery.
     + Checklists can simplify reporting by serving as both the procedure and a validation artifact when completed.
3. **Maintain Flexibility**:

   * Allow projects to customize and scale down the framework to suit their size and complexity:
     + Projects can add sections, tailor procedural steps, or omit unnecessary detail, depending on their specific software scope and classification.

#### **Centralized Resources for Small Projects**:

1. **Create and Maintain a Reusable Test Repository**:

   * Store reusable test cases, test data, and prior validation artifacts in a **Process Asset Library (PAL)** or testing repository.
   * Small projects can pull pre-existing test assets and adapt them to their own requirements, leveraging institutional knowledge from past projects.
2. **Tool Recommendations for Standardization**:

   * Use shared tools or platforms to enforce consistency in documentation:
     + For example, using NASA’s standardized tools (or custom organization-developed tools) for test planning, execution, and reporting, which provide pre-defined frameworks.

---

### **3. Maximizing Efficiency in Small Projects**

Small projects often face constraints and competing priorities, so efficient testing practices are critical.

#### **Lean Testing Strategies**:

1. **Risk-based Testing**:

   * Focus testing efforts on high-risk and mission-critical requirements. Use a simplified risk assessment to prioritize test cases:
     + Rank requirements by risk factors such as failure impact, likelihood, and importance to overall functionality.
   * Defer less critical testing tasks to later stages or minimize testing of low-risk functionality.
2. **Systematic Reuse of Legacy Tests**:

   * For projects involving reused or legacy software, prioritize regression and integration testing over complete re-verification of unmodified components:
     + Test only modified or high-risk sections of the reused software.
     + Use prior test documentation as a baseline, ensuring new test procedures and results only extend the existing framework.
3. **Encourage Cross-Disciplinary Roles**:

   * In small teams, testing roles may overlap with development or design roles. While independence of testers is ideal (per the guideline for Classes A, B, and safety-critical Class C software), small teams should:
     + Ensure critical tests are peer-reviewed or reviewed externally to maintain testing objectivity.
     + Leverage tools or automation to increase consistency and reduce bias when tester independence cannot be fully achieved.

#### **Minimize Overhead with Automation and Tools**:

1. **Automated Test Scripts**:

   * Develop reusable test scripts that can quickly execute test procedures and collect results, especially for time-consuming regression testing.
   * Tools like continuous integration pipelines (e.g., Jenkins, GitLab CI) can automate testing workflows and reduce overall documentation and execution time.
2. **Use Simple Tracking Systems for Test Documentation**:

   * Instead of complex document management systems, consider lightweight tools (e.g., shared spreadsheets or simple databases) to track test cases, procedures, and results.

---

### **4. Maintenance of Documentation**

Even for small projects, documentation must remain up-to-date to ensure continuity, traceability, and compliance throughout the project lifecycle.

#### **Guidelines for Effective Maintenance**:

1. **Use Configuration Management**:

   * Store test documents in a version-controlled repository, allowing updates to reflect changes in requirements, design, or test scope.
   * Document updates such as:
     + New or revised requirements (SWE-071).
     + Changes resulting from defect reports or anomalies.
     + Modifications due to new hardware/software tools included in testing.
2. **Periodic Reviews**:

   * Even small projects should conduct periodic reviews of test documentation and results:
     + Use peer reviews or lightweight audits to validate documents for relevance and sufficiency.
     + Ensure completed tests are adequately marked as resolved and traceable to the original requirements.
3. **Test Documentation into Operations and Maintenance**:

   * Maintain accurate test documentation into operational phases:
     + This ensures that any future updates, maintenance, or anomaly investigations have a reliable baseline from which to work.

---

### **5. Collaboration and Knowledge Sharing**

#### **Shared Teams, Shared Knowledge**:

* Encourage small project teams to collaborate and share test strategies, lessons learned, and reusable assets to reduce development time.
* Implement tools for quick knowledge sharing, such as Confluence pages, chat platforms, or internal wikis.

---

### **Summary of Improved Small Project Strategies**:

| **Guidance Area** | **Key Improvement** |
| --- | --- |
| Combine Documentation | Use unified documents for plans, procedures, and results to streamline testing and reduce redundancies. |
| Standardization Framework | Establish reusable templates and checklists that can be customized per project. |
| Efficiency Practices | Employ risk-based testing, reuse legacy test assets, and focus on high-priority requirements. |
| Automation Tools | Leverage automation and lightweight tracking systems for consistent, low-overhead execution. |
| Maintenance | Use configuration management and conduct periodic reviews to maintain up-to-date documentation. |
| Shared Knowledge | Develop repositories and foster collaboration between teams for reusable testing resources. |

---

By focusing on reducing overhead, leveraging standardization, and prioritizing high-value activities, this improved guidance helps small projects meet NASA's rigorous quality standards while operating within resource constraints.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-209)

  [IEEE Standard for System, Software, and Hardware Verification, and Validation](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8055462 "Click to open in new window")

  IEEE Computer Society, IEEE Std 1012-2016 (Revision of IEEE Std 1012-2012), Published September 29, 2017,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards. Non-NASA users may purchase the document from: http://standards.ieee.org/findstds/standard/1012-2012.html
* (SWEREF-211)

  [IEEE Guide for Software Verification and Validation Plans,](http://standards.ieee.org/findstds/standard/1059-1993.html "Click to open in new window")

  IEEE Computer Society, IEEE STD 1059-1993, 1993. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-478)

  [Software Development Standard for Space Systems,](http://everyspec.com/USAF/TORs/download.php?spec=TOR2004-3909-3537B.026755.pdf "Click to open in new window")

  Aerospace Report No. TOR-2004(3909)-3537, Revision B, March 11, 2005.
* (SWEREF-561)

  [Ensure Test Monitoring Software Imposes Limits to Prevent Overtest (2003)](https://llis.nasa.gov/lesson/1529 "Click to open in new window")

  Public Lessons Learned Entry: 1529.
* (SWEREF-573)

  [Aquarius Reflector Over-Test Incident](https://llis.nasa.gov/lesson/2419 "Click to open in new window")

  Public Lessons Learned Entry: 2419.
* (SWEREF-579)

  [Planning and Conduct of Hazardous Tests Require Extra Precautions (2000-2001)](https://llis.nasa.gov/lesson/991 "Click to open in new window")

  Lessons Learned Entry: 991.
* (SWEREF-581)

  [CAMS 10188 Process Escape PR LCA 4168 - GOAL Booster APU/Hydraulics program BAT04 did not execute per requirements](https://llis.nasa.gov/llis_lib/pdf/1035716main_PR%20LCA%204168.pdf "Click to open in new window")

  CAMS 10188. In NASA Engineering Network.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The NASA Lessons Learned database contains crucial insights from past incidents related to software testing and testing plans. Proper planning, preparation, execution, and review of test procedures are essential to ensure safe, reliable, and effective testing in NASA projects, especially for safety-critical systems and scenarios involving hardware integration. This section summarizes key lessons learned and actionable recommendations from the database to help avoid similar shortcomings in future projects:

---

### **1. Aquarius Reflector Over-Test Incident**

**Lesson Number: 2419**  
This incident highlighted the importance of comprehensive test procedures and clearly defined roles and responsibilities to prevent confusion during operations and ensure successful test execution.

#### **Key Points**:

* **Lesson Learned No. 1**:

  + "The Aquarius Reflector test procedure lacked complete instructions for configuring the controller software before the test."
  + **Actionable Takeaway**: Test procedures must be fully detailed, including software setup and configuration steps, to minimize the risk of errors or omissions during execution. Missing instructions can lead to operational anomalies or test failures.
* **Lesson Learned No. 4**:

  + "The roles and responsibilities of the various personnel involved in the Aquarius acoustic test operations were not documented. This could lead to confusion during test operations."
  + **Actionable Takeaway**: Ensure test plans and procedures clearly define the roles and responsibilities of all personnel involved. This includes engineers, quality assurance personnel, and safety monitors—role clarity is critical for smooth execution and timely responses to anomalies.

**Recommendation**: Review test procedures for completeness and ensure personnel roles are documented within the test plan to prevent misunderstandings during execution.

---

### **2. Planning and Conducting Hazardous Tests**

**Lesson Number: 0991**  
Testing involving hazardous conditions, such as extreme temperatures, pressures, energy storage, or deployable systems, requires heightened precautions. This set of lessons emphasized special measures to mitigate risks to personnel, flight hardware, and facilities.

#### **Key Points**:

1. **Comprehensive Test Documentation**:

   * Test procedures must be **well written**, **well organized**, and **easy to interpret** for both engineering and quality assurance personnel.
   * **Actionable Takeaway**: Simplify and clarify documentation for high-risk tests, ensuring technical details are accurate and understandable by all stakeholders.
2. **Pre-Test Training**:

   * Document inherent test anomalies (known issues associated with the test equipment or conditions, including likely causes, effects, and remedies) and include them in pre-test training.
   * **Actionable Takeaway**: Equip personnel with knowledge of historical anomalies and potential challenges before testing begins, to reduce error frequency and improve test readiness.
3. **Safety-Critical Data Readouts**:

   * Ensure test control data is presented in clear and easily understood formats (e.g., audible alarms, visible indicators, or graphical visualizations).
   * **Actionable Takeaway**: Use intuitive safety mechanisms to protect flight hardware during hazardous tests.
4. **Test Readiness Reviews and Equipment Verification**:

   * A formal test readiness review must confirm that all Ground Support Equipment (GSE), test devices, and sensors have been properly calibrated and maintained.
   * **Actionable Takeaway**: Validate equipment health and configuration prior to test execution to avoid premature failures or misreading.
5. **Ensuring Quality Assurance Oversight**:

   * Quality assurance personnel need to be actively involved throughout hazardous testing to monitor adherence to procedures and prescribed responses to anomalies.
   * **Actionable Takeaway**: Make quality assurance witness testing mandatory for high-risk scenarios to complement engineering oversight.

**Recommendation**: For hazardous tests, implement rigorous procedural reviews, comprehensive pre-test training, well-maintained equipment, and clear safety-critical data displays to protect personnel and hardware.

---

### **3. Proper Test Configuration for Fully Loaded Scenarios**

**Lesson Number: Not Specified (Testing for Configurations)**  
Inadequate test planning contributed to testing gaps in integrated and formal test levels. Testing scenarios did not account for concurrent operation of BAT06 and BAT04 in a fully loaded launch configuration, leading to timing-related code errors.

#### **Key Points**:

* **Integrated and Acceptance Testing**:
  + "Neither test plan had steps where BAT06 and BAT04 were running concurrently in a launch configuration scenario. Thus, no test runs were conducted reflecting the new fully loaded console configuration."
  + **Actionable Takeaway**: Test plans must include accurate operational scenarios, including all relevant hardware/software interactions, to ensure tests reflect system behavior under real-world mission conditions.

**Recommendation**: Include fully loaded configuration scenarios in integrated and acceptance testing to uncover timing or interaction-related issues that might occur during actual use.

---

### **4. Ensure Test Monitoring Software Prevents Over-Test**

**Lesson Number: 1529**  
This lesson emphasized the critical role of test monitoring software and hardware safeguards to avoid over-testing, a condition that could lead to damaging flight hardware.

#### **Key Points**:

* **Test Monitoring Software Limits**:
  + "Under the principle of 'First, Do No Harm,' ensure test monitoring and control software is programmed or limiting hardware devices are installed to prevent over-test conditions under all circumstances."
  + **Actionable Takeaway**: Implement software safeguards or physical limiting devices as part of the test environment to prevent over-exposure or unintended stress on flight equipment during testing.

**Recommendation**: Develop automated limits in test monitoring software or insert hardware safety devices to avoid harmful over-test conditions.

---

### **5.** Lessons Learned: Class D Budget and Schedule Pressure Leading to Reduced Software Maturity at ATLO

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
While Class D missions are allowed to tailor processes, the SWEHB still requires adherence to core engineering and assurance expectations.

**Lesson Learned:**  
Regardless of mission class, flight software must reach sufficient maturity before entering ATLO. Tailoring does not remove the need for complete architectures, characterized behaviors, and integrated test evidence. The LTB demonstrates the risks introduced when these fundamentals are compressed or deferred, particularly in resource‑limited Class D environments.

### **6.** **Lesson Learned (Starliner CFT):** **Verification must be comprehensive and mission‑representative; limited evidence for critical systems is unacceptable.**

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

**Recommended Practices (Aligned to SWE‑065/066):**

* Create **mission‑representative test plans**: include environment profiles, timing/network conditions, off‑nominal paths.
* Require **evidence completeness reviews**: trace requirements → tests → results → defects/resolutions.
* Enforce **end‑to‑end verification** of safing and FP across all implementation paths (sequences + FSW).

**Actionable Checks:**

* Verification plans show explicit coverage of mission environments and edge cases.
* Traceability matrices demonstrate complete requirement‑to‑evidence mapping.
* End‑to‑end test reports include integrated FP/safing results.

### **Summary of Actionable Recommendations from Lessons Learned**

1. **Complete Documented Procedures**:

   * Ensure test procedures fully detail all necessary steps, configurations, and personnel roles to avoid confusion and test deficiencies.
2. **Comprehensive Testing for Operational Scenarios**:

   * Reflect accurate mission configurations (fully loaded conditions) during integrated and formal testing to identify timing or interaction-related errors.
3. **Handle Hazardous Tests with Care**:

   * Use extra precautions, including pre-test training, quality assurance oversight, clear documentation, intuitive safety-critical data displays, and rigorous test readiness reviews to ensure personnel and hardware safety during high-risk tests.
4. **Prevent Over-Test Conditions**:

   * Include safeguards within test monitoring software or hardware devices to prevent unintended stress or damage to flight hardware.

By integrating these lessons learned into future test plans, projects can significantly reduce testing risks, ensure thorough validation coverage, and improve the chances of mission success while safeguarding both personnel and hardware.

### 7. **Incomplete Verification & Validation (V&V)**

**Incident:**  
The project faced major V&V shortfalls, including approximately 1,000 unverified system requirements and incomplete GNC, fault protection, and FSW test coverage. Immature and incompatible testbeds further hindered simulation and closed‑loop testing.

**Lesson Learned:**

* **Comprehensive V&V Execution:** V&V must be resourced, scheduled, and monitored with the same rigor as hardware development.
* **Validated Testbeds:** Testbeds and simulations must be synchronized early with vendor tools to ensure accurate system‑level testing.

**Implication:**  
Insufficient V&V undermines mission confidence and may conceal system defects until it is too late to correct them within the launch window.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Test plans should cover all aspects of testing](https://software.gsfc.nasa.gov/lesson-details/56/). **Lesson Number 56**: The recommendation states: "Test plans should cover all aspects of testing, including specific sequencing and/or data flow requirements."
* [Apply Change Management principles to test hardware/software](https://software.gsfc.nasa.gov/lesson-details/65/). **Lesson Number 65**: The recommendation states: "Apply Change Management principles to test hardware/software."
* [Proper sequencing of stress tests can make root cause analysis easier when failures occur](https://software.gsfc.nasa.gov/lesson-details/68/). **Lesson Number 68**: The recommendation states: "Proper sequencing of stress tests can make root cause analysis easier when failures occur."
* [Hire people on the FOT side in prelaunch to focus on ground system testing](https://software.gsfc.nasa.gov/lesson-details/97/). **Lesson Number 97**: The recommendation states: "Hire 2-3 people on the FOT side in prelaunch to focus on ground system testing and not put this on the flight ops personnel of the FOT."
* [Incorporate automation into operations prior to launch](https://software.gsfc.nasa.gov/lesson-details/98/). **Lesson Number 98**: The recommendation states: "Incorporate automation into operations prior to launch, instead of waiting until after launch."
* ["Day in the Life" simulations using automation prior to launch](https://software.gsfc.nasa.gov/lesson-details/99/). **Lesson Number 99**: The recommendation states: "Execute "Day in the Life" simulations using automation prior to launch."
* [Leverage planned testing activities to verify ground system requirements](https://software.gsfc.nasa.gov/lesson-details/122/). **Lesson Number 122**: The recommendation states: "Leverage planned testing activities to verify ground system requirements."
* [Use the Flight Ops team to perform ground system acceptance testing](https://software.gsfc.nasa.gov/lesson-details/123/). **Lesson Number 123**: The recommendation states: "Use the Flight Ops team to perform ground system acceptance testing."
* [Impacts caused by interfaces that are not tested pre-launch](https://software.gsfc.nasa.gov/lesson-details/124/). **Lesson Number 124**: The recommendation states: "Develop mitigations for impacts caused by interfaces that are not tested pre-launch."
* [Perform pre-launch end-to-end testing between the spacecraft and all primary primary ground stations](https://software.gsfc.nasa.gov/lesson-details/126/). **Lesson Number 126**: The recommendation states: "Perform pre-launch end-to-end testing between the spacecraft and all primary primary ground stations."
* [If ground systems are not available, a dedicated test needs to be performed](https://software.gsfc.nasa.gov/lesson-details/144/). **Lesson Number 144**: The recommendation states: "Maintaining spacecraft schedule is critical: if ground systems are not available, a dedicated test needs to be performed."
* [For a flight mission, plan and budget from outset for full end-to-end testing simulating an "orbit in the life"](https://software.gsfc.nasa.gov/lesson-details/161/). **Lesson Number 161**: The recommendation states: "For a flight mission, plan and budget from outset for full end-to-end testing simulating an "orbit in the life"."
* [End-to-End Testing through satellite I&T](https://software.gsfc.nasa.gov/lesson-details/172/). **Lesson Number 172**: The recommendation states: "End-to-End Testing should be planned for smaller events spread out through satellite (i.e., spacecraft with integrated payload/science instruments) I&T."
* [Software Requirement Sell-Off Expedience](https://software.gsfc.nasa.gov/lesson-details/177/). **Lesson Number 177**: The recommendation states: "As early as feasible in the program (EPR-CDR time frame) ensure that the project will be provided with all relevant test articles well in advance of the test’s run-for-record (will likely require NASA Program Management buy-in as well). This will allow the time necessary for: review of requirement test coverage, accumulation of all comments (especially if IV&V are supporting the program), and vendor disposition of all comments to project satisfaction. In this manner, when test artifacts from the FQT run-for-record are provided for requirement sell-off, the Flight Software SME will have a high level of confidence in the artifacts provided (knowing how each requirement has been tested) to expedite the sign-off process. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
* [Going Beyond the Formal Qualification Test (FQT) Scripts: Data Reduction/Automation](https://software.gsfc.nasa.gov/lesson-details/295/). **Lesson Number 295**: The recommendation states: "As early as feasible in the program (pre-FQT time frame), ascertain whether automated testing is planned for Software FQT and ensure that the vendor will provide all relevant test articles well in advance of test run-for-record (will likely require NASA Program Management buy in and support as well). Identify any calls to open up additional views to EGSE, Simulators, raw hex dumps, etc., that may be used to assist with data analysis/processing/reduction in the scripts. Request clarification on how data captured in those views will be used and have snapshots provided (or travel to vendor site) to fully understand verification extent. For automated testing, the Software Systems Engineer should evaluate whether the provider has allocated sufficient time and training to fully understand how the automated testing program will exercise and verify all required functions and behaviors. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
* [Consider a streamlined review process for lower maturity products](https://software.gsfc.nasa.gov/lesson-details/332/). **Lesson Number 332**: The recommendation states: "Start with a small group for initial review, and then add reviewers later."
* [Key Mission Ops Tests essential to timely V&V of flight design/mission ops concept& launch readiness](https://software.gsfc.nasa.gov/lesson-details/342/). **Lesson Number 342**: The recommendation states: "Develop/iterate/execute system level tests to verify/validate data system/mission Concept of Operations during Observatory I&T (e.g., the Comprehensive Performance Test (CPT) and Day-in-the-Life (DiTL) test). The CPT should be: a) thorough (exercising all copper paths, as many key data paths as reasonable, and using operational procedures); b) executed prior to/post significant events throughout Spacecraft & Observatory I&T; and c) designed comprehensive, yet short enough to be executed multiple times (e.g., the PACE CPT was specifically designed to be 4-5 days). The multi-pass DiTL test can demonstrate nominal operational procedures/processes and, when executed prior to the pre-environmental CPT, can be the basis for the instrument functionals during the environmental cycles and post environmental functional checkouts of the instruments."

# 7. Software Assurance

**SWE-065 - Test Plan, Procedures, Reports**

4.5.2 The project manager shall establish and maintain:

a. Software test plan(s).  
b. Software test procedure(s).  
c. Software test(s), including any code specifically written to perform test procedures.  
d. Software test report(s).

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

**For part a:**

1. Confirm that software test plans have been established, contain correct content, and are maintained.

2. Confirm that the software test plan addresses the verification of safety-critical software, specifically the off-nominal scenarios.

**For part b:**

**1. Confirm that the test procedures have been established and are updated when changes to tests or requirements occur.**

**2. Analyze the software test procedures for the following:   
   a. Coverage of the software requirements.  
   b. Acceptance or pass/fail criteria,   
   c. The inclusion of operational and off-nominal conditions,   
       including boundary conditions,   
   d. Requirements coverage and hazards per SWE-066 and   
       SWE-192, respectively.  
   e. Requirements coverage for cybersecurity per SWE-157   
       and SWE-210.**

**For part c:**

1. Confirm that the project creates and maintains any code specifically written to perform test procedures in a software configuration management system.

2. Confirm that the project records all issues and discrepancies in the code specifically written to perform test procedures.

3. Confirm that the project tracks to closure errors and defects found in the code specifically written to perform test procedures.

**For part d:**

1. Confirm that the project creates and maintains the test reports throughout software integration and test.

2. Confirm that the project records the test report data and that the data contains the as-run test data, the test results, and required approvals. 

3. Confirm that the project records all issues and discrepancies found during each test.

4. Confirm that the project tracks to closure errors and defects found during testing.

## 7.2 Software Assurance Products

This enhanced guidance provides a structured framework for software assurance (SA) activities, ensuring robust validation and verification of test artifacts, procedures, and results across the software lifecycle. The goal of this guidance is to emphasize traceability, safety, and continuous quality improvement while reducing risks through proactive oversight of testing processes.

Software assurance contributes to ensuring that test plans, procedures, and reports meet project and safety objectives. Below are key SA deliverables and corresponding responsibilities for each stage of the test lifecycle:

#### **1. Test Plan Review and Confirmation**

1. **Correct Test Plan Content**:

   * Ensure that test plans include all applicable content as specified in **NPR 7150.2 Guidance** and **7.18 - Documentation Guidance**:
     + Objectives, scope, and strategy of testing.
     + Traceability to software requirements, including safety-critical requirements.
     + Coverage of operational, off-nominal, boundary, and failure scenarios.
   * Confirm updates to the test plan as requirements or project objectives evolve.
2. **Safety-Critical Requirements**:

   * Verify that the plan addresses all safety-critical requirements and hazard controls.
   * Ensure test objectives cover operational safety scenarios as well as failure detection, mitigation, and recovery.
3. **Peer Review Results**:

   * Assess the results of test plan peer reviews to identify deficiencies.
   * Track and confirm that all issues and corrective actions associated with peer reviews have been resolved.
4. **Evidence of Approval**:

   * Provide formal evidence (signatures, approvals, or documented assessments) verifying that the software assurance team has approved the test plans.

---

#### **2. Test Procedure Review and Maintenance**

1. **Established and Maintained Procedures**:

   * Confirm that test procedures are developed, maintained, and updated as tests, requirements, or designs change through the software lifecycle.
   * Verify that procedures align with updates to software safety analyses, hazard reports, or other critical project documentation.
2. **Identify Issues During Procedure Peer Reviews**:

   * Participate in and review peer evaluations of test procedures to identify potential deficiencies or discrepancies.
   * Ensure corrective actions for any identified issues are implemented and documented.
3. **Procedure Attributes**:

   * Review and analyze test procedures for:
     + **Coverage**: Ensure procedures encapsulate all software requirements (functional, interface, boundary, and safety-related).
     + **Pass/Fail Criteria**: Confirm the presence of clear and measurable evaluation criteria for each test.
     + **Scenario Testing**: Validate that procedures address:
       - Normal operational conditions.
       - Off-nominal and boundary conditions.
       - Stress, performance, and fault recovery scenarios.
     + **Traceability**: Confirm test procedures link explicitly to software requirements, design elements, hazard reports, and system-level tests.
4. **Traceability of Requirements to Procedures**:

   * Use and validate traceability matrices to ensure all software requirements are covered by appropriate tests.
   * Pay special attention to requirements derived from safety analyses (e.g., fault-tree analysis, hazard reports) and verify that hazard controls are rigorously tested.

---

#### **3. Test Execution Monitoring and Assessment**

1. **Assessment of Test Status**:

   * Continuously monitor testing progress and compliance with the test plan.
   * Analyze and report on the status of test execution, highlighting test completion rates, anomalies identified, and corrective actions taken.
2. **SA Role in Safety-Critical Testing**:

   * Witness safety-critical tests to ensure adherence to test procedures and evaluate the proper functioning of hazard controls.
   * Focus on fault detection, isolation, recovery mechanisms, and the software’s performance under concurrent hardware or software failures.
3. **Approval of Test Reports**:

   * Where required (e.g., for safety-critical software), provide formal approval of test reports after verifying:
     + All test objectives were met.
     + All discrepancies were adequately addressed.
     + All safety-related requirements were verified.
   * Ensure test results reflect an accurate assessment of the system’s quality and safety readiness.

---

#### **4. Issues and Discrepancies Resolution**

1. **Identification of Testing Issues**:

   * Track and document issues, anomalies, and discrepancies identified during test planning, test execution, or peer reviews of test procedures.
   * Analyze the root causes of testing issues and recommend corrective actions to prevent recurrence.
2. **Types of Issues to Monitor**:

   * **Non-Conformances**: Software misbehavior during tests, such as deviation from expected results or unhandled exceptions.
   * **Safety Gaps**: Missing or insufficient test cases for safety-critical requirements, hazard mitigations, or fault recovery.
   * **Requirement Inadequacies**: Unclear, conflicting, or incomplete requirements leading to testing ambiguity.
   * **Test Procedure Deficiencies**: Gaps, errors, or inconsistencies within the testing procedures or expected results.
3. **Feedback and Continuous Improvement**:

   * Provide detailed issue summaries and corrective action recommendations to the project team for process improvement and future testing iterations.

---

#### **5. Software Safety Testing**

1. **Validation of Safety Mechanisms**:

   * Ensure that the test plan and procedures validate the software’s fault detection, isolation, and recovery mechanisms as derived from safety analyses (e.g., PHA, FMEA, and fault-tree analysis).
   * Confirm that testing encompasses:
     + Interface robustness testing for hardware/software interactions.
     + Multiple concurrent failure scenarios (e.g., simultaneous hardware and software faults).
     + FDIR (Fault Detection, Isolation, and Recovery) operation under nominal, degraded, and failure conditions.
2. **Unit and Component Testing for Safety Features**:

   * Confirm that safety features are tested at the unit level for both normal and unexpected inputs (e.g., out-of-sequence, malformed, or extreme data).
   * Ensure test artifacts such as drivers, stubs, and simulations used for unit testing are maintained for future regression testing.

---

#### **6. Reporting and Documentation**

1. **Test Results Analysis**:

   * Analyze the outcome of tests and summarize findings in detailed, actionable reports.
   * Develop a categorized list of issues and discrepancies observed during testing to inform management and future projects.
2. **Maintain Artifacts**:

   * Ensure all test-related documentation (plans, procedures, reports, etc.) is up to date and accurately reflects the current software baseline.
   * Provide ongoing oversight during updates caused by changes in requirements, design, or implementation.

---

## 7.3 Software Assurance Metrics

Software assurance should utilize metrics to monitor and improve the effectiveness of testing activities. These metrics provide a quantifiable basis for assessing progress, identifying trends, and implementing data-driven decisions.

#### **Recommended Metrics Categories**:

1. **Test Coverage Metrics**:

   * Total number of requirements versus completed tests.
   * Number of safety-critical tests executed versus those witnessed by SA.
   * Detailed requirements tested versus total detailed requirements.
2. **Discrepancy Metrics**:

   * Types and severity of issues identified during testing.
   * Open versus closed non-conformances, with time to closure.
3. **Risk and Non-Conformance Metrics**:

   * Risks or non-conformances related to test code or test procedures.
4. **Process Trends**:

   * Trends in test outcomes (e.g., pass/fail percentages over time).
   * Open versus closed action items, risks, and non-conformances.

**See Also**: Topic 8.18 - SA Suggested Metrics.

---

## 7.4 Software Assurance Activities and Reviews

Software assurance personnel should perform the following at each stage of the software lifecycle:

1. **Preliminary Design Review (PDR)**:

   * Confirm the test plan has been started and includes placeholders for safety-critical scenarios.
2. **Critical Design Review (CDR)**:

   * Assess that test procedures have been started, align with system requirements, and address operational, off-nominal, and boundary conditions.
3. **Implementation and Beyond**:

   * Monitor updates to test plans and procedures as requirements, hazards, or designs change.
   * Actively witness critical tests, validate results, and ensure traceability to requirements.
4. **Post-Test Activities**:

   * Verify that corrective actions are completed and regression tests are re-executed for modified software.

---

By embedding software assurance throughout the test lifecycle and prioritizing traceability, analysis, and safety, NASA can ensure the successful verification and validation of software systems while maintaining the highest standards for mission safety and quality.

 See also [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements),

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification)       * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.13 - Test Witnessing](/spaces/SWEHBVD/pages/102695739/8.13+-+Test+Witnessing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

# 8. Objective Evidence

Objective Evidence

To ensure compliance with **Requirement 4.5.2**, objective evidence should be demonstrable, measurable, and documented to substantiate that all software testing activities—including test plans, test procedures, actual tests, and reports—are being created, maintained, and utilized effectively. Below is a detailed breakdown of the required objective evidence that addresses each aspect of the requirement:

This requirement involves the creation and upkeep of the following software testing artifacts, with documentation and records serving as tangible, auditable proof of compliance.

---

### **1. Test Plans**

#### **Evidence**:

1. **Test Plan Document**:

   * A finalized and version-controlled document that outlines the scope, objectives, testing phases, environments, resources, risk mitigations, and schedules.
   * The document must include traceability to software requirements and a rationale for safety considerations.
   * Reference: Include document revision control logs or an artifact repository record (e.g., showing "baselined at CDR" with updates tracked).
2. **Approval Record**:

   * Evidence of approval/signoff by:
     + Project manager or technical lead.
     + Software assurance or quality assurance teams (SA/QA).
     + Independent reviewers (if required for safety or criticality).
3. **Peer Review Artifacts**:

   * Peer review reports or meeting minutes, including:
     + List of attendees.
     + Anomalies, action items, and resolutions (e.g., tracked through change request systems).
4. **Content Coverage Analysis**:

   * Records demonstrating that the test plan covers:
     + Functional and non-functional requirements (e.g., performance, safety, boundary conditions, fault recovery, off-nominal scenarios).
     + Verification of safety-critical components and hazardous conditions (linked to system-level hazard analyses).

---

### **2. Test Procedures**

#### **Evidence**:

1. **Test Procedure Document**:

   * Detailed instructions covering the steps, configurations, inputs, and pass/fail criteria for the execution of test cases.
   * The procedures should include test artifacts for specific test cases traced to the software requirements.
2. **Traceability Matrix**:

   * A matrix linking software test cases and procedures to:
     + Software requirements (functional, safety-critical, interface, and performance).
     + Hazard controls (for systems with hazard reports).
3. **Dry Run Records**:

   * Logs, test data, or engineer-noted outcomes of dry-run executions, with evidence of updates/refinements based on pre-execution findings.
4. **Configuration Management Evidence**:

   * Maintenance records showing test procedures are updated (e.g., after changes in requirements, design, or implementation). Include version-controlled revisions in configuration tools.
5. **Approval and Audit Records**:

   * Records of SA/QA signoff for updated or revised procedures after periodic reviews or significant changes.

---

### **3. Test Execution and Data**

#### **Evidence**:

1. **Test Execution Logs**:

   * Timestamped and version-controlled records of actual test runs, detailing:
     + Test case ID (from the procedure or matrix).
     + Input data, output results, and observed anomalies.
     + Test environment configuration (platform, simulator, hardware, software versions).
2. **Automation Evidence (if applicable)**:

   * Logs or screenshots from automated test frameworks/tools (e.g., Jenkins, Selenium, or Python-generated test results).
   * Evidence of compliance with automated regression test cycles.
3. **Test Monitoring and Witness Checklists**:

   * Recorded observations from software assurance personnel or third-party witnesses confirming:
     + Tests were executed per the approved procedures.
     + Safety-critical tests were executed in the specified operational or simulation environment(s).

---

### **4. Test Reports**

#### **Evidence**:

1. **Software Test Reports**:

   * Formal, version-controlled artifacts documenting the following:
     + Test cases executed and their outcomes (pass/fail criteria met).
     + Summary of discrepancies, root causes, corrective actions, and resolutions.
     + Coverage analysis (e.g., percentage of requirements tested, untested requirements, gaps, and mitigations).
2. **Metrics or Performance Analysis**:

   * Data-driven evidence of test effectiveness, such as:
     + Tests executed versus total planned tests.
     + Requirements tested versus total requirements.
     + Defect density trends over time to demonstrate improvement.
   * Compliance with **SWE-191: Regression Testing** metrics for modified code/components.
3. **Approvals**:

   * Test reports signed off by SA/QA with evidence showing their verification of accuracy and completeness.

---

### **5. Safety Assurance Evidence**

For safety-critical software, additional evidence is required to verify that hazardous scenarios or off-nominal events have been considered and tested adequately:

#### **Evidence**:

1. **Hazard Traceability**:

   * A traceability matrix showing links between:
     + System-level hazards (from hazard reports) and safety-related software requirements.
     + Safety-related software requirements and corresponding test cases/procedures.
2. **Off-Nominal Test Logs**:

   * Results of fault-injection testing, stress/stability testing, and boundary testing to confirm:
     + System responses to failures and hazardous states (e.g., power loss, invalid inputs, timing issues).
     + Validation of fault detection, isolation, and recovery (FDIR) mechanisms.
3. **Witness Checklist from Hazard Testing**:

   * Documentation indicating hazardous tests were witnessed and validated (SWE-194) by software assurance or safety experts.

---

### **6. Updates and Maintenance Evidence**

#### **Evidence**:

1. **Configuration Management and Change Logs**:

   * Documented updates to test plans, procedures, and reports after any changes to requirements, designs, or code (SWE-071 compliance).
   * Historical logs showing:
     + What was changed.
     + Why the change was necessary (link to defect reports, design updates, or requirement changes).
     + When and who approved the changes.
2. **Revised Test Artifacts**:

   * Updated versions of test documents after defect resolution or corrective actions.
   * Records of re-executed test cases (e.g., regression tests) after code updates with the revised test results.

---

### **7. Metrics-Based Monitoring Evidence**

#### **Evidence**:

Metrics to provide a quantifiable view of software progress, quality, and risks. Examples of evidence include:

1. **Requirements Coverage**:

   * Charts or reports tracking:
     + Number of requirements tested versus total number of requirements.
     + Percentage of safety-critical requirements executed successfully.
2. **Defect and Anomaly Trends**:

   * Reports or plotted graphs showing:
     + Non-conformances (open/closed) over time.
     + Severity and resolution timeframes for defects.
     + Defect density trends (e.g., issues per test case or line of code).
3. **Testing Progress**:

   * Summary reports of completed versus planned tests.
   * Execution breakdowns across testing levels (unit, subsystem, integration, and acceptance).
4. **Safety Metrics**:

   * Number of safety-critical tests executed versus witnessed.
   * Non-conformances in safety mitigations or fault-handling procedures.

---

### **8. Tools and Repository Artifacts**

#### **Evidence**:

1. **Test Repository Records**:

   * Screenshots or exports from tools like JIRA, TestRail, or equivalent (if applicable), showing:
     + Test plans, procedures, execution logs, and approvals in one central repository.
     + Issue and action item tracking linked to test artifacts.
2. **Automation Artifacts**:

   * Logs from automation frameworks for regression testing and repeated execution of test scripts.

---

### **Summary of Objective Evidence Types**

| **Artifact** | **Example Evidence** |
| --- | --- |
| Test Plan | Baseline document, version control logs, review approval reports. |
| Test Procedure | Detailed test steps, traceability matrices, peer review comments. |
| Test Results | Execution logs, automation logs, safety-critical test records with traces to requirements. |
| Test Reports | Signed-off reports, discrepancy analysis summaries, metrics tracking reports. |
| Safety Artifacts | Traceability to hazard reports, fault injection results, boundary/stress test reports. |
| Maintenance Artifacts | Configuration change logs, newly updated artifacts reflecting requirements or design changes. |
| Metrics | Reports showing testing trends, requirements/test coverage, defect closure rates, and safety-critical test data. |

By maintaining these evidences, compliance with **Requirement 4.5.2** can be demonstrated effectively, ensuring thorough validation and verification processes for mission-critical software.

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
