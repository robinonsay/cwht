# SWE-189 - Code Coverage Measurements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695524. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements

SWE-189 - Code Coverage Measurements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695524)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695524&showCommentArea=true&showComments=true#addcomment)

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

4.5.9 The project manager shall ensure that the code coverage measurements for the software are selected, implemented, tracked, recorded, and reported.

## 1.1 Notes

This requirement can be met by running unit, integration, and validation tests; measuring the code coverage; and achieving the code coverage by additional (requirement based) tests, inspection, or analysis.

If the project does not get 100 percent structural coverage, it means one of four things and each requires action on the project manager’s part:

* Requirement missing - the code that hasn’t been covered is performing an essential activity, but no requirement indicates that this should be done;
* Test missing - the code that hasn’t been covered relates to an existing requirement, but no test was implemented for it;
* Extraneous/dead code – the code that hasn’t been covered is not traceable to any requirement and isn’t needed by the software;
* Deactivated code - the code that hasn’t been covered isn’t traceable to any requirements for the current system, but is intended to be executed in specific configurations.

The code coverage data and any rationale for uncovered code should be presented and reviewed at major project milestones.

## 1.2 History

Click here to view the history of this requirement: SWE-189 History

SWE-189 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.5.9 The project manager shall ensure that the code coverage measurements for the software are selected, implemented, tracked, recorded, and reported. |
| Difference between C and D | No change |
| D | 4.5.9 The project manager shall ensure that the code coverage measurements for the software are selected, implemented, tracked, recorded, and reported. |

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

To identify which lines of source code have been tested and which lines of your source code have not been tested and to provide data showing the completeness of the executed software tests. This helps to identify what areas of the code are needed and what areas may not be needed or are only used in specific scenarios. Code coverage can provide a profile of what software gets tested the most and the metrics can help guide where more involved or rigorous testing needs to occur, potentially at other levels of the system.

Code coverage is an essential software quality metric that ensures the thoroughness of software testing by identifying the percentage of code executed during validation. This requirement ensures that the project's testing strategy achieves sufficient depth to validate that the software behaves as intended under all relevant conditions, including nominal and off-nominal (failure) scenarios. Code coverage measurement plays a critical role in:

1. **Reducing Risks:** Higher coverage decreases the likelihood of undetected defects in untested code paths, particularly in safety- and mission-critical software.
2. **Demonstrating Test Completeness:** Ensures that testing activities cover the intended functionality and logic.
3. **Maintaining Software Reliability:** Confirms that all critical software requirements are implemented, functional, and testable.
4. **Facilitating Certification and Compliance:** High code coverage often meets industry standards, regulatory requirements, and stakeholder expectations for software quality.

---

### **Key Rationale Points:**

#### **1. Ensuring Thorough Validation of Software Functionality**

* Code is the foundation of software behavior. If parts of the code remain unexecuted during testing, the risk of undetected defects increases, especially in critical system functions.
* By tracking and ensuring adequate code coverage for the software, the project manager ensures that potential defects in code related to safety, mission-critical operations, or operational functionality are addressed before deployment.

#### **2. Improving Software Reliability and Reducing Complexity Risks**

* In complex systems, code paths may include intricate logic, edge cases, or unanticipated conditions. Measuring and reviewing code coverage helps identify untested paths and scenarios that may lead to incorrect or unpredictable behavior during operations.
* High reliability is critical for NASA's mission software, as failures may lead to mission delays, unacceptable costs, or catastrophic outcomes.

#### **3. Risk Management for Safety- and Mission-Critical Applications**

* Validating code paths in safety-critical software (e.g., Class A or Class B) is vital because untested code could lead to system hazards or failures. Code coverage analysis ensures all safety-critical and fault-handling logic is executed during testing.
* Example scenarios where untested code could be catastrophic:
  + Fault protection mechanisms for spacecraft during autonomous operations.
  + Redundancy and recovery routines in flight software.

#### **4. Meaningful Testing Through Coverage Criteria**

* Code coverage measurements (e.g., statement, branch, decision, or condition coverage) ensure testing rigor and completeness. For instance:
  + **Statement Coverage** confirms that all lines of code are executed during testing.
  + **Branch or Decision Coverage** ensures all branches (e.g., `if-else` conditions) in the logic are evaluated.
  + **Modified Condition/Decision Coverage (MC/DC)**, often required for safety-critical software (e.g., FAA DO-178C standards), ensures that conditions within decisions independently affect decision outcomes.
* By selecting appropriate coverage criteria based on software criticality, the project manager ensures that tests align with the software's risk profile and operational importance.

#### **5. Supporting Continuous Improvement of Testing Processes**

* Tracking and reporting code coverage over time helps identify gaps in test case design, allowing teams to iteratively improve their test suites.
* Code coverage metrics provide quantifiable feedback for evaluating and improving software testing strategies, ensuring sufficient depth and breadth for test completeness.

#### **6. Documenting and Communicating Coverage Results**

* Recording and reporting coverage provides evidence of thorough testing efforts. This is crucial for:
  + Stakeholders who expect transparency in risk mitigation and quality assurance.
  + Audits and reviews, such as milestone gate reviews, where test coverage is a critical factor.

#### **7. Supporting Compliance with Standards**

* Code coverage measurement is often required to comply with external or internal standards for software engineering (e.g., NASA-STD-8739.8, NASA-7150.2, DO-178C, ISO 26262 for automotive software).
* Code coverage provides evidence that testing sufficiently addresses software requirements and risks.

---

### **Coverage Measurement and Its Implementation**

#### **Why Select Appropriate Coverage Metrics?**

Code coverage must align with the software's **complexity** and **criticality**. Here are examples:

1. **Statement Coverage:** Ensures basic execution of every line of code. Useful for low-complexity or less critical software.
2. **Branch or Decision Coverage:** Ensures all decision paths within the software are exercised. Necessary for moderate-criticality systems.
3. **Condition/MC/DC Coverage:** Ensures decisions and each condition within a decision are independently tested. Required for high-criticality, safety-critical systems.

#### **Why Track and Report Coverage?**

* Tracking coverage helps monitor progress toward validation goals during a project.
* Reporting ensures transparency and allows stakeholders to verify that testing completeness aligns with the project's objectives.

---

### **Examples of Code Coverage in Context**

1. **Mission-Critical Software (e.g., Navigation Control):**

   * Coverage would focus on validating navigation and flight software's fault tolerance, redundancy mechanisms, and real-time responses. Failure to validate edge cases could result in spacecraft failure.
   * Reporting results would provide evidence of tested safety mechanisms (e.g., a fallback when primary controls fail).
2. **Safety-Critical Software (e.g., Spacecraft Life Support):**

   * MC/DC would likely be a requirement to validate fault conditions and redundant capabilities fully.
   * Tracking coverage during testing would ensure all life-sustaining measures are tested before deployment.
3. **Research and Scientific Analysis Software:**

   * Statement coverage might suffice for non-critical systems where reliability is important but not safety-related.

---

### **Consequences of Inadequate Code Coverage**

Failing to ensure adequate code coverage can lead to multiple risks, including:

1. **Undetected Defects:** Untested code paths could harbor logic flaws or bugs that manifest during real-world operations.
2. **System Failures:** Incomplete validation increases the likelihood of undetected failure modes, especially in safety- and mission-critical software.
3. **Reduced Stakeholder Confidence:** Limited test coverage may fail to meet assurance requirements for high-reliability systems.
4. **Non-Compliance with Standards:** Many safety-critical standards mandate minimum levels of code coverage for certification.
5. **Expensive or Hazardous Post-Deployment Errors:** Late-stage defects in operational software are far costlier to identify and resolve than early-stage rework.

---

### **Responsibilities of the Project Manager:**

The project manager ensures the following for code coverage:

* Selection of **appropriate measurement techniques** based on software safety and criticality (e.g., statement coverage vs. MC/DC).
* Implementation of tools and processes for accurate coverage measurement.
* Regular **tracking** of coverage progress throughout testing cycles.
* Documentation of coverage results, including reporting of gaps, untested code regions, and mitigations.
* Oversight of corrective actions for insufficient coverage, ensuring the codebase and tests align with mission objectives.

---

### **Summary of Rationale:**

The requirement to manage **code coverage measurements** ensures software is rigorously tested, reducing risks, improving defect detection, and enhancing reliability for critical NASA missions. By creating procedures for selecting, tracking, recording, and reporting code coverage, the project ensures thorough validation that aligns with mission goals, compliance standards, and stakeholder confidence. This requirement reflects NASA's commitment to engineering software that meets the highest safety and reliability standards.

# 3. Guidance

## 3.1 Code Coverage

Code coverage is a key metric of software engineering best practices that provides insights into the thoroughness of software testing efforts. By identifying which parts of the codebase have been executed through testing and which parts remain untested, project teams can assess the adequacy of their test suites and focus efforts on improving software reliability and quality. Proper management of code coverage is especially critical for safety- and mission-critical systems, which demand rigorous verification to eliminate risks that could compromise operations.

This guidance expands on the original content by offering practical implementation steps, recommendations, considerations for handling less-than-100% coverage, specific coverage criteria, and tailored guidance for different software classifications.

#### **Definition and Purpose**

Code coverage is a **structural testing metric** that measures the percentage of software source code exercised by test cases. Its goal is to ensure sufficient testing coverage across the software to:

1. Identify untested parts of the code (e.g., omissions or defects in test design).
2. Improve testing effectiveness and focus testing efforts on critical code paths.
3. Support risk reduction and increase the reliability of the software for its intended operations.

#### **Key Engineering Practices for Code Coverage:**

1. **Selection of Code Coverage Metrics:**

   * Identify which coverage criteria are relevant based on software classification and system requirements (e.g., statement coverage, branch coverage, MC/DC coverage).
   * Tailor the selection to address safety-critical software requirements and risks (e.g., HR-33, inadvertent operator actions).
2. **Implementation:**

   * Integrate code coverage measurement tools into the test environment (e.g., JaCoCo, LCOV, Codecov, BullseyeCoverage, etc.).
   * Ensure configuration management practices support reproducibility of code coverage metrics throughout the lifecycle.
3. **Tracking and Monitoring:**

   * Use automated reporting tools to track code coverage metrics across builds and iterations.
   * Continuously monitor trends in coverage metrics, especially during system changes or regression testing.
4. **Recording and Reporting:**

   * Maintain detailed code coverage reports for milestones, peer reviews, and audits.
   * Create traceability between code coverage results and requirements verification.

---

## 3.2 Dealing with Less Than 100% Coverage

Achieving **100% code coverage** for **safety-critical components** is mandatory, but there are scenarios where full structural code coverage is infeasible or inappropriate. When coverage falls below 100%, the project team must analyze the uncovered code and take appropriate actions as outlined below:

#### **Reasons for Less Than 100% Coverage and Required Actions**

1. **Missing Requirements:**

   * **Issue:** Uncovered code executes essential functionality, but no requirement explicitly calls for its execution.
   * **Action:** Perform requirements gap analysis to identify missing requirements and update the system's requirement set. Ensure tests are designed to cover the new requirements.
2. **Missing Tests:**

   * **Issue:** Uncovered code is tied to an existing requirement, but corresponding tests were not implemented.
   * **Action:** Update the test suite to address gaps and ensure test case completeness. Perform root cause analysis on why tests were omitted.
3. **Extraneous/Dead Code:**

   * **Issue:** Uncovered code is not traceable to any system requirement and is not necessary for the software.
   * **Action:** Perform **dead-code analysis** and refactor or remove extraneous code. Document findings in code review reports.
4. **Deactivated Code:**

   * **Issue:** Uncovered code is intended for use in other system configurations but is not relevant to current testing (e.g., dormant functionality for future system expansions).
   * **Action:** Document deactivated code explicitly as part of the test plan and justify its existence in validation reports.

#### **Handling Risks from Uncovered Code:**

* Provide **risk assessments** for safety-critical software components where 100% structural code coverage is impossible.
* Develop mitigations for untested code paths, such as exploratory testing, static analysis, or operational monitoring during deployment.

---

## 3.3 Coverage Criteria

Code coverage provides actionable insights only if meaningful metrics are selected. Engineering teams must adapt coverage criteria based on the **criticality of the software** and project-specific objectives.

#### **Types of Coverage Criteria**

1. **Function Coverage:**

   * Measures whether every function (or subroutine) in the program has been executed.
   * Useful for ensuring high-level functionality testing, but does not cover internal paths within functions.
2. **Statement Coverage:**

   * Measures whether every individual statement in the code has been executed.
   * Provides a baseline for structural testing.
3. **Branch Coverage:**

   * Measures whether each branch of control structures (e.g., `if`, `case`, loops) has been executed.
   * Confirms that all control-flow paths are exercised, including both true and false outcomes in conditional statements.
4. **Condition Coverage (Predicate Coverage):**

   * Measures whether each condition within decision-making structures evaluates both true and false.
   * Example: Ensures evaluation of all sub-conditions in complex Boolean expressions.
5. **Modified Condition/Decision Coverage (MC/DC):**

   * Measures whether each condition in a complex decision independently affects the overall outcome of the decision.
   * Required for **safety-critical software** per NASA standards and industry certifications such as DO-178C.

#### **Coverage Criteria for Safety Classes:**

Coverage expectations vary by software classification (see Classification A-D) and safety criticality:

| Coverage Type | Class A Safety Critical | Class B Mission Critical | Class C | Class D |
| --- | --- | --- | --- | --- |
| **Source Code Statement Coverage** | 100% | 100% | AM | AM |
| **Source Code Decision Coverage** | 100% | 100% | AM | AM |
| **Source Code MC/DC Coverage** | 100% | AM | AM | AM |

**AM (Agreed Measurement):** Coverage levels for Classes C and D must be approved by the Center's Engineering Technical Authority (TA).

---

## 3.4 Code Coverage of Libraries/Objects

For projects utilizing third-party libraries or shared code objects:

* Evaluate whether all critical library functions invoked by the software are covered.
* Ensure tests are focused on **only the relevant functionality** that impacts the software's operational and safety-critical behavior.
* For unused library functions, validate their exclusion through proper documentation in the test plan.

---

## 3.5 Best Practices for Code Coverage Implementation

#### **Tool Selection and Integration**

* Choose coverage measurement tools compatible with the project’s programming language and development environment.
* Integrate tools into your CI/CD pipeline for automated measurement collection across builds.

#### **Continuous Coverage Analysis**

* Perform regular coverage analysis during regression testing, development milestones, and software updates to ensure that coverage trends remain consistent.
* Review uncovered code paths to determine if additional testing is required.

#### **MITIGATION OF LOW COVERAGE**

* Use complementary techniques like **static code analysis**, **model-based testing**, and **fault injection testing** to evaluate untested or unreachable parts of the codebase.
* Incorporate targeted exploratory testing for operational workflows that are difficult to replicate in traditional test cases.

---

### **Conclusion**

Code coverage is foundational to achieving robust software validation. It provides actionable insights into test completeness, exposes risks associated with untested code paths, and ensures safety-critical software meets NASA's high standards. By implementing structured coverage criteria, addressing low coverage scenarios effectively, and applying tailored strategies based on software classification, project teams can deliver reliable, high-quality software that meets mission and operational goals.

See also [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing),

Confirm that 100% code test coverage is addressed for all identified software safety-critical software components or ensure that software developers provide a risk assessment explaining why the test coverage is impossible for the safety-critical code component: [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action), 

See also Topic [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software),

## 3.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

For small projects, the required rigor in achieving code coverage can be appropriately tailored based on the **scope, criticality, and risk posture** of the project. While full code coverage may not always be necessary, small projects should ensure that **key functionality and decision pathways** are adequately tested to maintain software quality and reliability.

---

### **Key Small Project Code Coverage Practices:**

1. **Focus on High-Impact Areas:**

   * Prioritize test coverage for critical and essential portions of the codebase (e.g., core functionality, safety-critical decisions, and risk-sensitive operations).
   * Ensure that **key decision points** and branches (e.g., `if`, `else`, `switch`, and loops) are thoroughly exercised by your test suite.
2. **Tailor Coverage Based on Risk:**

   * Determine the appropriate code coverage percentage in proportion to the **risk posture** of the project:
     + **Higher Risk Posture:** Projects with higher risks to safety, mission success, or functionality (e.g., critical decision-making software or those operating in constrained hardware environments) require greater coverage and rigor.
     + **Lower Risk Posture:** For less critical projects, pragmatically focus your testing based on core functional requirements and known areas of complexity in the software, while documenting coverage gaps.
3. **Leverage Static Analysis for Efficiency:**

   * Use static analysis tools to automate code coverage reporting and integrate them into your Continuous Integration (CI) pipeline. These tools can:
     + Identify untested code sections quickly.
     + Provide meaningful insights on coverage, with metrics for specific coverage criteria (e.g., statement, branch, or function coverage).
   * Embedding static analysis into the CI process saves time, reduces manual effort, and ensures consistent measurement across iterations.
4. **Document Untested Code Thoroughly:**

   * Any untested portions of code should be documented clearly, along with a rationale explaining why they are being excluded from the test suite. Common examples may include:
     + Dead or extraneous code intentionally left in the codebase.
     + Low-risk or error-prone code paths that are infeasible to test but evaluated through other means (e.g., manual inspections, static analysis).
     + Deactivated code meant for future scenarios or alternative configurations.
   * Documentation of these sections ensures transparency and confirms that the project team acknowledges and agrees with the rationale for exclusion.

---

### **Suggested Workflow for Code Coverage in Small Projects:**

1. **Plan Code Coverage Targets Early:**

   * Define realistic code coverage goals aligned with the project's requirements and risk tolerance.
   * Establish which areas of the code require rigorous coverage (e.g., core logic, decision branches, interfaces) versus lesser coverage (e.g., configuration files, logging/debugging functions).
2. **Use Lightweight Tools and Practices:**

   * Simplify workflows by using **lightweight tools** that are easy to integrate, such as:
     + Static analysis tools that generate coverage reports (e.g., SonarQube, JaCoCo, LCOV).
     + CI tools that support automated test frameworks and coverage tracking (e.g., GitHub Actions, Jenkins, GitLab CI/CD).
3. **Iteratively Analyze and Improve:**

   * Incorporate frequent reviews of code coverage metrics during agile iterations or project milestones.
   * Revisit and refactor test gaps where the risks of insufficient testing are significant.
4. **Regularly Communicate Coverage Results:**

   * Provide periodic updates to the team, stakeholders, or management on current coverage levels, documented exclusions, and areas needing further testing.
   * Transparency in code coverage discussions allows for informed decisions and risk awareness.

---

### **Core Guidance: Balancing Rigor and Feasibility**

For small projects, it is important to balance testing rigor with the available resources and timeline. While the overall coverage goal may allow for flexibility, **key principles must still be observed**:

* **Critical Sections Must Be Tested:** Ensure tests sufficiently validate the core logic, decision pathways, and high-risk components.
* **Document Gaps:** Any untested code should be accounted for with a clear justification.
* **Reflect on Risk:** Use the project’s risk assessment to drive how much coverage is needed, focusing efforts on where failures would carry the greatest impact.
* **Leverage Automation:** Incorporate tools and CI automation to reduce test effort while maximizing coverage insights.

By applying these practices, small projects can maintain focus on quality and reliability without exceeding their resource constraints.

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

Here are some relevant **NASA Lessons Learned** sourced from historical experiences and records associated with the requirement for **code coverage measurements (SWE-190)** and its importance in ensuring software reliability, safety, and mission success. These lessons are derived from the **NASA Lessons Learned Information System (LLIS)** database and other documented NASA experiences.

---

### **1. Mars Observer Failure Due to Insufficient Testing**

**Lesson Learned ID:** 0370  
**Summary:**  
The 1993 failure of the Mars Observer spacecraft was attributed, in part, to **inadequate software testing coverage**, particularly for the propulsion system. The validation and verification activities failed to test key failure scenarios and unanticipated code paths, leaving gaps in the fault protection software. This lack of thorough coverage contributed to the mission-ending explosion of the spacecraft during its insertion into Mars orbit.

**Key Takeaways:**

* Software must be rigorously tested for all possible operational scenarios, with sufficient code coverage to identify gaps in paths where defects could manifest.
* **Recommendation:** Ensure 100% code coverage for all safety-critical and fault-handling routines, with a detailed accounting of any untested code.

---

### **2. Venus Mariner I Failure due to Coding Error**

**Lesson Learned ID:** 0798  
**Summary:**  
In 1962, the Mariner I spacecraft was lost shortly after launch due to a software coding error. The issue occurred because a single typographic omission in the software prevented correct execution of a control algorithm. A contributing factor was the **failure to test the software thoroughly**—this critical error was not identified during testing, and insufficient testing coverage allowed the flawed code path to remain unverified.

**Key Takeaways:**

* Code coverage metrics should include **decision and branch coverage** to ensure all control paths are exercised.
* Even seemingly minor code paths in flight-critical software demand thorough testing.
* **Recommendation:** Apply rigorous coverage measurement tools and comprehensive processes to validate critical algorithms.

---

### **3. Radiation Effects on Code Execution in the Galileo Spacecraft**

**Lesson Learned ID:** 1121  
**Summary:**  
The Galileo spacecraft, launched in 1989, encountered memory upsets caused by radiation-induced Single Event Upsets (SEUs) during its mission to Jupiter. Some of these SEUs caused execution errors that affected untested portions of fault protection software. The software did not always handle these issues as anticipated since certain failure modes had **not been adequately tested** due to incomplete code coverage during preflight testing.

**Key Takeaways:**

* In environments prone to radiation or resource-limiting conditions, **fault-handling code** (even less frequently used code paths) must be rigorously covered during testing.
* **Recommendation:** 100% code coverage must be applied to all safety-critical software components, particularly for handling off-nominal conditions.

---

### **4. Dead Code Risk in the Ariane 5 Failed Launch**

**Lesson Learned ID:** (Derived from cross-agency failures)  
**Summary:**  
While not a NASA mission, the infamous Ariane 5 failure in 1996 revealed a software defect in **dead code**—a section of software that was inherited but untested for the operational configuration of Ariane 5. During flight, an untested part of the legacy system caused the rocket to fail mid-flight, resulting in a complete loss of the mission.

**Key Takeaways:**

* **Dead or dormant code** must always be analyzed for safety and operational impact, and either fully tested or justified/documented if left untested.
* **Recommendation:** Use **static analysis** to identify dead or dormant code. If dead code is identified, ensure it is tested, analyzed, or explicitly removed from the codebase.

---

### **5. Fault Protection Deficiency in the Mars Climate Orbiter**

**Lesson Learned ID:** 0838  
**Summary:**  
The Mars Climate Orbiter, lost in 1999, experienced a mission-ending failure partly due to insufficient testing coverage of the system's **fault protection software**. Only nominal scenarios had been tested prior to launch, leaving some critical off-nominal conditions unvalidated.  
The lack of comprehensive code testing (both in the nominal and failure conditions) contributed to the spacecraft's demise.

**Key Takeaways:**

* Complete **branch coverage** is essential to ensure fault-protection logic is robust, especially for off-nominal workflows.
* **Recommendation:** Testing must exercise fault conditions and edge cases, not just primary use cases. Coverage metrics must validate the behavior of code paths for abnormal operating conditions.

---

### **6. Space Shuttle Software Code Coverage Lessons**

**Lesson Learned ID:** 2152 (Software Validation for the Space Shuttle Program)  
**Summary:**  
The Space Shuttle program implemented rigorous software validation and verification processes, including 100% **Modified Condition/Decision Coverage (MC/DC)** for safety-critical software. This rigorous approach proved essential in ensuring software robustness, reliability, and continuous success across the Shuttle’s 135 missions.

**Key Takeaways:**

* For safety-critical systems, **100% MC/DC coverage** is necessary to verify all conditions within decisions independently.
* Properly implemented code coverage mitigates the risk of undetected bugs manifesting during live operations.
* **Recommendation:** Adopt **MC/DC** or relevant high-fidelity coverage criteria to reflect the safety and mission-criticality of the software.

---

### **7. Lessons from the International Space Station (ISS)**

**Lesson Learned ID:** 2358 (Software Flexibility and Testing)  
**Summary:**  
The ISS program experienced challenges when dormant software components created risks during configuration changes across system iterations. Due to incomplete testing coverage, certain code paths responsible for managing redundant systems were inadequately tested, leading to operational inefficiencies.

**Key Takeaways:**

* Software updates and dormant code must be tested whenever changes to core configurations occur.
* Code coverage tracking should be continuous to ensure older code paths or dormant functionality are not overlooked during software updates.
* **Recommendation:** Develop configuration-aware scenarios when planning code coverage, ensuring all potential software states are exercised during testing.

---

### **8. Genesis Spacecraft Mishap**

**Lesson Learned ID:** 0500  
**Summary:**  
In 2004, the Genesis spacecraft crashed upon Earth return due to a fault in its reentry software logic. This fault was a result of **untested fault-handling code** being left dormant in the spacecraft. This failure highlighted the risks of untested or inactive code paths, which were improperly assumed to be safe.

**Key Takeaways:**

* Ensure that **dormant or fault-handling code** is actively tested or removed if not required. Never assume that dormant or unused sections are safe without proper verification.
* **Recommendation:** Include dormant and safety-critical code in coverage metrics, with procedures for risk approval when 100% coverage is infeasible.

---

### **Conclusion: Lessons for Code Coverage**

These lessons demonstrate the critical role that complete and rigorous code coverage plays in mission success, particularly for NASA’s highly reliable software systems. Key overarching takeaways include the need for:

1. **100% Structural and Functional Coverage** for safety-critical code, especially in decision-making and fault-handling paths.
2. **Thorough Testing of Off-Nominal and Edge Cases**, not just nominal workflows.
3. **Proactive Management of Dead/Dormant Code** to ensure it is either tested or explicitly removed.
4. **Continuous Monitoring and Documentation** of untested code, test limitations, and the justification for gaps in coverage.

Applying these lessons enhances the reliability, safety, and robustness of NASA software and reduces the likelihood of software-related mission failures.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Going Beyond the Formal Qualification Test (FQT) Scripts: Data Reduction/Automation](https://software.gsfc.nasa.gov/lesson-details/295/). **Lesson Number 295**: The recommendation states: "As early as feasible in the program (pre-FQT time frame), ascertain whether automated testing is planned for Software FQT and ensure that the vendor will provide all relevant test articles well in advance of test run-for-record (will likely require NASA Program Management buy in and support as well). Identify any calls to open up additional views to EGSE, Simulators, raw hex dumps, etc., that may be used to assist with data analysis/processing/reduction in the scripts. Request clarification on how data captured in those views will be used and have snapshots provided (or travel to vendor site) to fully understand verification extent. For automated testing, the Software Systems Engineer should evaluate whether the provider has allocated sufficient time and training to fully understand how the automated testing program will exercise and verify all required functions and behaviors. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
* [Remove Debug Settings and Code Prior to Benchmarking](https://software.gsfc.nasa.gov/lesson-details/338/). **Lesson Number 338**: The recommendation states: "Remove or disable debug code and settings before benchmarking to ensure that timing numbers are accurate."

# 7. Software Assurance

**SWE-189 - Code Coverage Measurements**

4.5.9 The project manager shall ensure that the code coverage measurements for the software are selected, implemented, tracked, recorded, and reported.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that code coverage measurements have been selected, performed, tracked, recorded, and communicated with each release.

## 7.2 Software Assurance Products

#### **Required Software Assurance (SA) Outputs:**

1. **Risk Analysis and Rationale for Uncovered Code:**

   * Software assurance must assess any **uncovered code** and provide a thorough risk analysis addressing:
     + The **potential impact** of the uncovered code remaining untested.
     + The **likelihood** of execution and failure in untested paths.
   * Rationale must justify why it is acceptable or unacceptable to leave certain code untested, including proper classification of uncovered code (e.g., extraneous, deactivated, or untestable code justified by infeasibility).
2. **Code Coverage Metric Data:**

   * Collect and document code coverage results at every release milestone.
   * Include key metrics such as:
     + Percentage of **tested paths vs. total possible paths** for each software component.
     + Code coverage percentages specifically for **safety-critical components**.
     + **Source Lines of Code (SLOC)** tested vs. total SLOC.
   * Clearly differentiate coverage for **safety-critical software (Class A/B)** components vs. non-critical software (Class C/D).

---

## 7.3 Metrics

#### **Required Code Coverage Metrics:**

* **Percentage of code/test coverage for safety-critical components:**
  + Example: (Tested paths ÷ Total paths) × 100%.
* **Percentage of SLOC tested vs. total SLOC:**
  + Tracks code coverage at the file or project level.
* **Combining metrics with risk analysis:**
  + Metrics should include data for **untested code**, including the justification or rationale for its status.

#### **Measuring and Monitoring Coverage Across the Lifecycle:**

* Regularly report on coverage metrics during key project phases, including **design reviews (e.g., CDR, PDR)** and major **testing milestones (e.g., unit testing, system integration testing).**
* Compare actual coverage rates to planned targets (e.g., start with incremental goals toward 100% for Class A/B).

---

## 7.4 Guidance

To evaluate and confirm code coverage across the life cycle, **software assurance** must work collaboratively with software engineers and project leads, following these steps:

#### **Step 1: Verification of Coverage Selection and Management**

* Confirm that engineering has:
  + Selected appropriate **code coverage measurements** (e.g., statement, branch, or MC/DC) based on the software class and safety-criticality (see SWE-190).
  + Implemented tools for **tracking, collecting, and recording** code coverage metrics.
  + Integrated coverage measurements into test plans and workflows (e.g., automated reporting in CI pipelines).
* Ensure the project communicates code coverage metrics at **regular intervals** with all key stakeholders (e.g., software engineers, assurance personnel, project management).

#### **Step 2: Identification of Uncovered Code**

* Analyze code coverage measurement data to:
  + Identify software components with **partial or no coverage.**
  + Classify uncovered sections of code into the following categories:
    - **Missing requirement:** Code performing an essential activity without a corresponding requirement.
    - **Missing test:** Code linked to an existing requirement but lacking test coverage.
    - **Extraneous/dead code:** Code without requirements and unnecessary for the software's functionality.
    - **Deactivated code:** Code tied to configurations or scenarios not relevant to the current system.
* Document each case and collaborate with software engineers to understand the context (e.g., temporary testing gaps or intentional exclusions).

#### **Step 3: Development of Risk Assessment and Rationale**

* Work with engineering to develop a **risk analysis** for uncovered code, including:
  + **Impact assessment:** Determine the risk posed by untested code (e.g., Could the code lead to a safety hazard? A mission failure?).
  + **Likelihood analysis:** Evaluate the probability of uncovered code executing in the operational environment.
  + **Rationale for coverage gaps:** Provide explicit reasoning for any uncovered code, focusing on technical or operational constraints:
    - Justify missing or deactivated code—as long as it poses no safety or mission risks.
    - Recommend actions for missing requirements or tests.
* Ensure the rationale and risk analysis are recorded in relevant documentation (e.g., software assurance reports, review logs).

#### **Step 4: Reporting and Communication**

* Report **code coverage metrics and analysis** results to:
  + The **software project manager**, detailing code gaps and associated risks.
  + The **center’s Engineering Technical Authority** for approval when less than 100% coverage is deemed acceptable.
* Include actionable recommendations, such as:
  + Adding missing requirements or test cases to eliminate gaps.
  + Refactoring or removing unnecessary dead/extraneous code.
  + Validating untested/deactivated code to ensure it cannot execute unintentionally.

---

### **Key Considerations for Ensuring Code Coverage Goals**

1. **Recommended Coverage Levels:**

   * **Safety-Critical Software** (Class A or B):
     + Aim for 100% code coverage, including **MC/DC coverage** where applicable.
   * **Class C and D Software:**
     + Code coverage targets may be risk-based and agreed upon with the Center’s **Engineering Technical Authority**.
   * Ensure **component-level coverage metrics** are consistent with the project's classification chart.
2. **Testing Quality vs. Quantity:**

   * While achieving a high code coverage percentage is essential, focus on **test quality**:
     + Ensure tests validate the software’s intended functionality and robustness under nominal and off-nominal conditions.
     + Prioritize testing for high-risk code paths, safety-critical modules, and decision/branch points.
3. **Static and Dynamic Analysis:**

   * Use **static analysis tools** to complement code coverage metrics by identifying:
     + Dead code or unreachable paths.
     + Coding standard violations that could pose risks to untested areas.
   * Use **dynamic analysis tools** to measure test coverage during execution and identify runtime issues.
4. **Continuous Monitoring Across the Lifecycle:**

   * Re-evaluate code coverage metrics periodically, especially after:
     + Major system requirements changes or software updates.
     + Addition of new functionality.
     + Identification of bugs linked to untested code paths.
5. **Managing Untested Code:**

   * For **extraneous/deactivated code** deemed acceptable to leave untested:
     + Document its existence and ensure these paths remain disabled where applicable.
     + Include safeguards to prevent accidental execution (e.g., error handling or conditional triggers).

---

### **Guidance Recap**

* **SA Responsibilities:** Software assurance ensures code coverage is planned, tracked, and reported while analyzing gaps for risk.
* **Collaboration with Engineering:** Work closely with engineers to refine tests for high-risk and critical components.
* **Proactive Risk Mitigation:** Identify, address, and document risks associated with uncovered code paths.
* **Lifecycle Integration**: Code coverage must be monitored throughout design, testing, and post-deployment to maintain high software quality.

By following this enhanced guidance, software assurance can help projects achieve **reliable, safe, and mission-compliant software** while ensuring both cost-effective testing approaches and transparency in handling gaps or exceptions.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is essential to demonstrate that the requirement for **code coverage measurements (SWE-190)** has been satisfied. This evidence provides verifiable documentation and artifacts to confirm that required actions related to code coverage have been performed, tracked, and managed across the software lifecycle.

Here is a comprehensive list of **objective evidence** for this requirement:

---

### **1. Code Coverage Plan and Criteria Selection**

* **Artifact:** **Test Plan Document** (aligned with SWE-065)
  + Description: Includes the code coverage approach, metrics, and targets for the project, specifying the coverage criteria chosen (e.g., statement, branch, MC/DC).
  + Evidence:
    - Documentation of the coverage methodology (e.g., “Code coverage will implement MC/DC for Class A components and branch coverage for Class C components”).
    - Justification for the selected coverage criteria based on software classification and system criticality.
    - Criteria and rationale for acceptable coverage percentages for non-Class A/B software.

---

### **2. Code Coverage Measurement and Reporting**

* **Artifact:** **Code Coverage Reports**
  + Description: Reports that provide detailed metrics showing the percentage of code executed during testing, broken down by subsystem, module, or component.
  + Evidence:
    - Metrics such as code test coverage rates for safety-critical components (e.g., "# of tested paths vs. total # of paths").
    - Source Lines of Code (SLOC) tested vs. total SLOC.
    - Trend analysis or snapshots showing how code coverage improved over time or across testing phases (e.g., unit testing, integration testing, system testing).
  + Tools commonly used to produce these reports:
    - JaCoCo, LCOV, BullseyeCoverage, or other coverage tools.
  + Example Evidence Table:

    | **Component** | **Coverage (%)** | **Criteria** | **Date Collected** |
    | --- | --- | --- | --- |
    | FlightLogic.c | 100% | MC/DC | October 15, 2023 |
    | Telemetry.cpp | 92% | Branch | October 15, 2023 |
    | Logging.cs | 85% | Statement | October 15, 2023 |

---

### **3. Evidence of Coverage Tool Integration**

* **Artifact:** **Continuous Integration (CI) Logs** or **Tool Configuration Files**
  + Description: Documents confirming code coverage tools (e.g., SonarQube, LCOV, JaCoCo) have been configured and run as part of the CI pipeline to automate coverage collection and reporting.
  + Evidence:
    - Logs from test automation pipelines verifying execution of test cases and generation of code coverage results.
    - Screenshots or output from coverage tools integrated into CI systems (e.g., Jenkins, GitLab CI, GitHub Actions).
    - Repository of historical test execution results showing consistent code coverage reporting.

---

### **4. Documentation of Uncovered Code Analysis**

* **Artifact:** **Risk Analysis Reports (Aligned with 7.2 Software Assurance Products)**
  + Description: Analysis and rationale documented for any uncovered code, including its classification and the associated risks of leaving it untested.
  + Evidence Includes:
    - Rationale for uncovered code, classified into categories such as:
      1. Missing requirement.
      2. Missing test.
      3. Extraneous/dead code.
      4. Deactivated code.
    - Risk assessment for uncovered code, including:
      * Likelihood of execution in the system.
      * Potential risks and their impact on system safety, functionality, or critical operations.
      * Mitigation strategies where applicable (e.g., additional reviews, alternative testing methods, removal of dead code).
  + Example Output:

    ```
    Component: FaultProtection.cpp
    Uncovered Code: Line 347 (Deactivated code linked to a future configuration)
    Rationale: Code will only execute in post-mission scenarios. No risk to nominal mission operations.
    Action: Reviewed and approved by Technical Authority.
    ```

---

### **5. Testing Artifacts**

* **Artifact:** **Test Results Documentation**
  + Description: Detailed results from executed test cases showing exercised paths in the codebase.
  + Evidence Includes:
    - Test execution logs indicating the success/failure of test cases corresponding to different portions of the source code.
    - Mapping between test cases and code coverage metrics:
      * E.g., “Test Case TC\_003 validated execution of decision logic in FaultHandler() function, achieving 100% branch coverage.”
    - Evidence of edge cases tested (e.g., error handling, fault management routines, boundary values).

---

### **6. Approval of Code Coverage Results**

* **Artifact:** **Code Coverage Review Meeting Minutes/Sign-Off Records**
  + Description: Evidence of project management, software engineering, and software assurance reviewing and approving code coverage results at various milestones.
  + Evidence Includes:
    - Meeting minutes documenting discussions on coverage metrics, anomalies, risks, and uncovered code justification.
    - Approval signatures from the **Center Engineering Technical Authority (TA)** for agreed-upon target coverage levels (particularly for Classes C/D software).
    - Example: Signed-off records for software assurance approval of metrics reports.

---

### **7. Approved Exclusions or Waivers**

* **Artifact:** **Deviation/Waiver Documentation**
  + Description: Evidence of approved waivers for achieving less-than-100% coverage for specific software paths or components.
  + Evidence Includes:
    - Formal records of exceptions to the code coverage requirement.
    - Justifications for waivers, including risks, mitigations, and sign-offs by appropriate authorities.
    - Example waiver:

      ```
      Deviation: Achieving 100% coverage for error-handling module X is infeasible due to hardware constraints in testing.
      Mitigation: Risk assessment confirms minimal impact, monitored operational environment will detect issues.
      Approved by: Technical Authority [Signature]
      ```

---

### **8. Code Coverage Retrospective (Post-Testing Validation)**

* **Artifact:** **Lessons Learned Documentation**
  + Description: Post-project lessons learned to evaluate the effectiveness and adequacy of code coverage.
  + Evidence Includes:
    - Reports documenting successes, failures, or gaps in aligning code coverage practices with testing goals.
    - Adjustments for future projects based on insights from coverage analysis.

---

### **9. Traceability Artifacts**

* **Artifact:** **Traceability Matrix**
  + Description: A Requirements-to-Test Coverage Matrix showing the linkage between software requirements, test cases, and associated coverage.
  + Evidence Includes:
    - Confirmation that all safety-critical requirements have corresponding test cases with sufficient code coverage.
    - Identification of test gaps or redundant requirements.
  + Example:

    | **Requirement ID** | **Test Case ID(s)** | **Code Coverage (%)** | **Notes** |
    | --- | --- | --- | --- |
    | SAF-REQ-001 | TC\_001, TC\_002 | 100% | Fully tested |
    | NOM-REQ-005 | TC\_010 | 95% | Branch coverage incomplete |

---

### **10. Project Summary Reports**

* **Artifact:** **Final Code Coverage Report**
  + Description: A consolidated report summarizing code coverage metrics for the entire project, including:
    - Final coverage achieved for all project components.
    - Justification for any untested code paths or exceptions.
    - Risk analysis and lessons learned.
  + Evidence Includes:
    - Comprehensive and signed-off reports submitted during major project reviews (e.g., Test Readiness Review (TRR), Software Acceptance Review (SAR)).

---

### **Expected Evidence Requirements for Software Classes**

| **Project Class** | **Code Coverage Artifacts Expected** |
| --- | --- |
| **Class A/B** | Test Plan, Code Coverage Reports, Full Coverage Rationale, Risk Analysis for any exceptions, Traceability Matrix. |
| **Class C/D** | Test Plan, Selected Metrics Data, TA-approved Coverage Goals, Deviation/Waiver Documents for partial coverage. |

---

### **Conclusion**

The above objective evidence provides traceable, verifiable artifacts that validate compliance with the code coverage requirements. By collecting and presenting this evidence at various project phases and reviews, the team can ensure **transparency, accountability, and rigor in software verification and assurance.**

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
