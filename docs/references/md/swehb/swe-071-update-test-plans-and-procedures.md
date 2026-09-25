# SWE-071 - Update Test Plans and Procedures

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695453. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures

SWE-071 - Update Test Plans and Procedures

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695453)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695453&showCommentArea=true&showComments=true#addcomment)

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

4.5.7 The project manager shall update the software test and verification plan(s) and procedure(s) to be consistent with software requirements.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-071 History

SWE-071 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.4.7 The project shall update Software Test Plan(s) and Software Test Procedure(s) to be consistent with software requirements. |
| Difference between A and B | No change |
| B | 4.5.8 The project manager  shall update software test plan(s) and software test procedure(s) to be consistent with software requirements. |
| Difference between B and C | No change |
| C | 4.5.7 The project manager shall update the software test plan(s) and the software test procedure(s) to be consistent with software requirements. |
| Difference between C and D | Editorial clarification (added verification plans). |
| D | 4.5.7 The project manager shall update the software test and verification plan(s) and procedure(s) to be consistent with software requirements. |

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

Software test plans and test procedures are the main tools used to ensure proper implementation of the requirements and are developed based on those requirements. Therefore, if the requirements change, the test plans and procedures must also change to ensure that the test activity is accurate, complete, and consistent with the requirements.

Software test plans and test procedures are a key element of ensuring that the requirements that specify a product are completely and accurately implemented; in other words, that the delivered product is the right product.

The purpose of this requirement is to ensure that all aspects of software testing and verification align with the current and evolving set of software requirements throughout the lifecycle of the project. Software requirements often evolve due to changes in system design, discovery of new conditions, or stakeholder needs. This requirement ensures that the software test and verification plans and procedures remain accurate, complete, and relevant, aligning with the most up-to-date requirements, thereby reducing the risk of undetected errors, incomplete testing, or non-compliance with project goals.

---

### **Rationale:**

**1.Ensures Traceability Between Requirements and Testing**

* Changes to software requirements necessitate corresponding updates to the software test and verification plans and procedures. Without this, there is a risk of untested requirements, discrepancies between the system's intended functionality and its verification, or incorrectly validated features.
* Maintaining traceability ensures that all requirements have corresponding test cases and that no requirement is overlooked.

**Example:** If a new feature or constraint is added (e.g., a safety-critical feature), the test plan must be updated to include test cases to verify whether the feature operates reliably in all expected and unexpected scenarios.

---

**2. Mitigates the Risk of Testing Gaps**

* Software systems are often complex and contain many interdependent modules. If test plans are not updated to reflect current requirements, errors may go undetected because the testing will be insufficient or outdated.
* Consistency between requirements and plans ensures that every functionality, boundary condition, and requirement change is accounted for in the testing process.

**Example:** A change to a performance requirement (e.g., increasing response time from 100ms to 200ms) requires new verification tests to confirm compliance with the updated metric. If not addressed, the software may not meet user expectations or contractual specifications.

---

**3. Improves the Quality and Reliability of the Software**

* Testing ensures the software meets defined requirements and behaves as expected under all operational conditions. When test plans and procedures reflect outdated requirements, critical quality and reliability issues may remain undetected until later project phases or even after deployment.
* Keeping testing plans consistent with current requirements enhances overall software reliability, minimizes late-stage issues, and reduces the likelihood of post-deployment failures.

**Example:** For flight software systems, overlooking updates to requirements could lead to incorrect environmental simulations or missed edge cases in mission-critical scenarios.

---

**4. Facilitates Compliance with Life-Cycle Standards and Best Practices**

* NASA's software development and assurance processes (such as NPR 7150.2) emphasize continual alignment between requirements, design, implementation, and testing. Consistently updating test plans to reflect changing requirements ensures adherence to these standards, which is essential for project and mission success.
* Best practices in software engineering place a high emphasis on requirements-driven testing (e.g., **requirements-based testing**) to confirm all specified functionalities meet their acceptance criteria.

**Example:** **DO-178C (used in aerospace software certification)** mandates that all software verification activities—including test plans and test cases—demonstrate full bidirectional traceability between requirements and tests.

---

**5. Reduces the Impact of Late-Stage Changes**

* In complex projects, upstream changes to requirements or design (even small changes) can create ripple effects across multiple areas of the system, including testing. By proactively updating test plans to reflect changes, the project minimizes the risk of discovering issues late in development.
* Late-stage integration and system testing are particularly expensive, both in financial and schedule terms. Addressing requirement changes early ensures these phases are not unnecessarily costly and risky.

**Example:** Introducing a hardware change mid-project could alter timing constraints in software. Updating the verification plan to include stress tests ensures the software integrates correctly with the updated hardware.

---

**6. Supports Effective Risk Management**

* Consistent updates to test plans help identify risks associated with new or modified requirements. Such risks could include untested requirements, incorrect assumptions, or changes conflicting with existing functionality.
* Well-maintained test plans allow early identification of potential issues, enabling better risk mitigation strategies.

**Example:** When adding functionality to handle redundant subsystems, the test plan must verify potential failure modes. Without an updated plan, these risks might not be systematically addressed in testing.

---

**7. Ensures Stakeholder and Mission Needs Are Met**

* Mission-critical systems (such as flight software) require complete confidence that software meets stakeholder expectations and performs without failure in the operational environment. Testing consistency ensures stakeholders’ evolving needs are adequately validated during testing phases.
* Well-documented and up-to-date test plans demonstrate to stakeholders that the system has been rigorously verified against the latest requirements.

**Example:** In human spaceflight systems, a late-stage clarification of user needs for crew autonomy (e.g., user overrides during software-controlled functions) requires not just software updates but also updated verification procedures to validate the new user interface requirements.

---

**8. Improves Project Transparency and Auditability**

* Any project subject to reviews, audits, or certification processes (common in NASA projects) requires detailed documentation demonstrating that testing and verification were continuously aligned with current requirements.
* Updated test plans provide auditable evidence that the software has been validated against all relevant requirements, delivering a clear and complete development record.

**Example:** During a final project review, a project with outdated test plans would face scrutiny for not demonstrating that critical, requirement-driven behaviors have been verified.

---

**9. Supports Agile and Incremental Development Approaches**

* In modern software development, especially iterative development lifecycles (e.g., Agile, hybrid Agile), requirements evolve incrementally. Verification plans and procedures must adapt to each incremental change to keep the development process in sync with testing.
* Keeping test plans consistent avoids mismatches during each iteration and provides ongoing assurance that new requirements or changes function as expected before deployment.

**Example:** When developing software for orbital debris avoidance, incremental updates to operational requirements (like near-real-time decision-making) must be tested during each sprint. Synchronizing the test plan ensures continuous verification during each incremental cycle.

---

**10. Supports Continuous Improvement**

* Test plans and procedures can benefit from lessons learned and feedback during their execution. Updating the test plan as requirements evolve creates opportunities to refine the test strategy continuously, improving test effectiveness over time.

**Example:** If tests for failure modes in initial versions of a requirement uncovered specific vulnerabilities, future changes to the requirement would benefit from updated procedures that integrate this feedback.

---

### **Summary of the Rationale**

Requirement 4.5.7 is critical for ensuring that software test and verification plans remain a dynamic and integral part of the software development process. Software testing and verification are only as effective as their alignment with current requirements. As project requirements evolve, maintaining consistency between the requirements and the test plans ensures:

* Full traceability and requirements coverage.
* Reduction of risks tied to undetected issues.
* Confidence in software quality and reliability.
* Cost savings through early error detection.
* Compliance with NASA standards, stakeholder expectations, and certification requirements.

This approach is essential for delivering software systems that are both technically sound and operationally aligned with mission-critical goals.

# 3. Guidance

This updated guidance strengthens the key practices for developing, maintaining, and executing software test plans and procedures throughout the project life cycle. The improvements focus on ensuring alignment with requirements, enabling traceability, managing requirements changes, including off-nominal scenarios, and applying configuration management to ensure accuracy and consistency.

---

### **3.1 Developing and Maintaining Test Plans and Procedures**

The **test plans and procedures** should represent comprehensive strategies for verifying all critical software requirements and mitigating potential project and mission risks. They must remain continuously aligned with software requirements, design, and project milestones to ensure their effectiveness throughout the life cycle.

#### **Key Guidance for Developing and Maintaining Test Plans:**

1. **Early Development of Test Plans and Procedures**

   * Teams should develop test plans and procedures **as soon as the relevant stage in the software life cycle is completed**, such as requirements definition, design, or implementation.
   * Initial test documents should outline:
     + Test objectives.
     + Strategies for verifying nominal and off-nominal requirements.
     + Resource estimates, including time, personnel, and tools.
     + A timeline for test development, execution, and reporting.
2. **Continuous Updates to Test Plans**

   * Changes to requirements, system design, or project goals necessitate **frequent updates** to all test-related documentation. Delays in updating test plans can lead to discrepancies, missed requirements tests, and unforeseen project delays.
   * **Benefits of Continuous Updates:**
     + Avoid last-minute corrections that can delay testing activities.
     + Ensure consistency between test cases and the latest requirements.
     + Helps maintain test validity, even when requirements are updated.
3. **Test Documentation to Keep Updated**:  
   The following test-related documents should be reviewed and updated as necessary:

   * **System test plans and procedures.**
   * **Acceptance test plans and procedures.**
   * **Unit test plans and procedures.**
   * **Integration test plans and procedures.**
   * **End-to-end test plans and procedures.**
   * **Regression test plans and procedures.**
   * **Test data and test scripts.**
   * **Test cases to reflect updated requirements.**
   * **Test schedule and resource estimates.**
   * **Traceability matrix to determine coverage for changes.**

#### **Specific Considerations:**

* **Hazard Mitigation and Off-Nominal Scenarios:**

  + Test plans and procedures must specifically address requirements associated with hazard controls, including **off-nominal commanding scenarios**.
  + Hazard controls should be thoroughly verified using test cases that simulate inadvertent operator actions and other edge conditions. This is critical for ensuring system safety in adverse and unexpected situations.
  + **Reference:** HR-33, "Inadvertent Operator Action."
* **References for Test Procedures:**

  + For detailed documentation development guidance, refer to relevant topics, including **SWE-065 - Test Plan, Procedures, and Reports**.

---

### **3.2 Testing Traceability Matrix**

A **traceability matrix** is a critical tool for ensuring full alignment between requirements, test plans, and testing activities. It links each software requirement to associated test plans, test procedures, test cases, and test data. Using this tool at all stages of validation and verification enables thorough risk management, visibility into coverage, and efficient response to requirements changes.

#### **Guidance on Traceability:**

1. **Purpose of the Traceability Matrix:**

   * Ensures bidirectional traceability between requirements and testing artifacts, such as test cases, scripts, and data.
   * Helps test teams **evaluate the impact of requirements changes** on testing plans and procedures. Teams can identify which test cases and artifacts may need updates or additions and ensure nothing is overlooked.
2. **Recommended Practices for Using the Traceability Matrix:**

   * Develop the matrix alongside test plans and procedures early in the life cycle and keep it updated as the project evolves.
   * Include test plans, procedures, scripts, and data in the matrix and relate these items directly to software requirements.
   * Use **test design reviews** and **life-cycle reviews** as checkpoints to verify the traceability matrix reflects all changes made to requirements.
3. **Checklists for Traceability Validation:**

   * Include checklist items in project life-cycle reviews (e.g., Preliminary Design Review, Test Readiness Review) to confirm:
     + All test documentation has been updated for approved requirements changes.
     + All test artifacts align with the associated requirements in the traceability matrix.
   * Use these checklists to **reassess the traceability matrix** when a revised version of test plans or procedures is created.
4. **Developing Effective Traceability Metrics:**

   * Example Metric: Percentage of requirements with corresponding and verified test cases.
   * Refer to **SWE-052 - Bidirectional Traceability** for implementation guidance.

---

### **3.3 Managing Requirements Changes and Their Impact on Testing**

Requirements often evolve throughout the project lifecycle due to changes in stakeholder needs, system design, or operational constraints. To address the impact of these changes on testing processes, it is essential to proactively manage communication and updates between requirements and testing teams.

#### **Recommended Practices:**

1. **Notification Mechanisms for Change Management:**

   * Establish processes to notify test plan developers of **approved requirements changes**, ensuring test plans are promptly updated. Examples include:
     + Providing the **Software Lead Engineer** with copies of approved change requests for dissemination to test teams.
     + Distributing **Change Control Board (CCB)** minutes and decisions to maintain transparency.
     + Including a **test team representative** in the CCB or similar groups to ensure testing considerations are factored into decision-making.
2. **Change Impact Assessment:**

   * Require the test team to conduct impact analyses to identify:
     + The specific test documentation that needs revision.
     + New or modified test cases required for verifying updated requirements.
     + Any ripple effects on existing test plans or procedures.
3. **Mitigating Gaps Caused by Delays:**

   * Implement interim test process updates while formal requirement changes are being approved to minimize downtime or wasted effort.

---

### **3.4 Configuration Management and Testing**

Configuration management (CM) ensures the integrity of software test plans and procedures as they evolve and prevents unauthorized or inconsistent changes. CM helps preserve the accuracy and traceability of testing artifacts through controlled updates while reducing the risk of errors.

#### **How to Apply Configuration Management to Testing:**

1. **Use Version Control for Test Documents:**

   * Employ CM tools to track revisions of all test-related documents, including test plans, cases, scripts, and data.
   * Each update to test plans and procedures should include a **clear change description**, reason for the update, and authorization.
2. **Keep Testing Aligned with Software Baselines:**

   * Align test plans and procedures with specific baselines of software requirements/design to prevent mismatches between the software under test and the scope of testing activities.
   * Use labels/tags in the CM system to associate test plan versions with their corresponding software versions.
3. **Review Change Requests for Consistency:**

   * Every change to the test plan or procedures should be reviewed for consistency with updated requirements or hazard mitigations.
   * Refer to **SWE-080 - Track and Evaluate Changes** for CM best practices.
4. **Audit and Trace Configurations:**

   * Periodically audit test documentation and CM records to ensure compliance with NASA’s software assurance standards.

---

### **Summary of Key Practices:**

* Develop and maintain **up-to-date test plans and procedures** that align with evolving requirements and address nominal, off-nominal, and edge-case scenarios.
* Foster **traceability** between requirements and all testing artifacts to manage complexity and streamline updates.
* Manage the impact of **requirements changes** through defined communication mechanisms and careful revision of testing artifacts.
* Apply **configuration management** principles to maintain control over test plans and ensure their alignment with software baselines and requirements.

By implementing these practices, projects will reduce the risk of overlooking critical requirements tests, improve the confidence in test results, and enhance the reliability of the final software product.

Consult Center Process Asset Libraries (PALs) for center-specific guidance and resources related to keeping test plans and procedures current as requirements change.

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)       * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

When developing test procedures, maintaining traceability to software requirements is critical for ensuring the accuracy and relevance of testing activities throughout the project life cycle. For small projects, where resources and tools may be limited, adopting practical and efficient methods for managing this traceability can make a significant impact on project success. Below is enhanced guidance to ensure robust test documentation practices.

---

### **Guidance for Traceability in Test Procedures:**

1. **Add Direct Links or Notes to Related Procedures:**

   * Incorporate **links or annotations** within test procedures that reference other procedures tracing back to the same requirement. For example:
     + Directly highlight related test cases, scripts, or test data that are derived from the same requirement.
     + Use internal comments, references, or cross-references within the documentation to indicate dependencies between test procedures.
   * This linking will enable the test team to **quickly identify related artifacts** when a requirement is changed, reducing the effort required to update all relevant documentation.

   **Example:**

   * Requirement: "The software shall validate input data for correctness within 2 seconds."
   * Test Procedure Linking:
     + Procedure A: Validate nominal input data is processed correctly.
       - **Linked Note**: This procedure relates to Procedure B (correctness) and Procedure C (timing verification).
     + Procedure B: Verify invalid input data is rejected.
2. **Use and Maintain a Traceability Matrix:**

   * **Organize a Simplified Traceability Matrix**:
     + For small projects, creating and **managing a lightweight traceability matrix** can significantly improve documentation management.
     + The matrix links requirements to corresponding test artifacts (test cases, procedures, scripts, and data) and identifies where changes need to cascade through the documentation.

   **Example Traceability Matrix Structure:**

   | **Requirement ID** | **Description** | **Test Procedure ID(s)** | **Test Case ID(s)** | **Test Data** | **Related Notes** |
   | --- | --- | --- | --- | --- | --- |
   | RQ-001 | Validate input data correctness | TP-A, TP-B | TC-01, TC-02 | Dataset-A, Dataset-B | Links to timing tests in TP-C |
   | RQ-002 | Ensure system response in <2s | TP-C | TC-03 | Dataset-C | Timing validation tests |

   * **Benefits:**
     + A centralized matrix simplifies the process of identifying all test artifacts affected by a requirement change.
     + The traceability matrix can be maintained in a spreadsheet, document, or lightweight database for ease of access and use.

---

### **Strategies for Handling Requirement Changes:**

1. **Efficient Updates Using Traceability:**

   * When a requirement is updated or changed, use the traceability matrix or linked references to quickly identify:
     + Which **test procedures** need updates.
     + Related test cases, scripts, and data that may require modification.
     + Dependencies between multiple test artifacts to avoid inconsistencies.
2. **Consistency with Project Resources:**

   * In small projects, streamline the effort by focusing on:
     + **Critical requirements**: Prioritize traceability for high-impact or safety-critical requirements.
     + **Automation where possible**: If tools are used, integrate traceability tracking with the existing development and testing tools.

---

### **Additional Tips for Small Projects:**

1. **Regularly Review and Verify Traceability Links:**

   * During project milestones (e.g., test planning, Test Readiness Review), ensure that:
     + Test procedures are accurately aligned with requirements.
     + Any missing or outdated links in the matrix are updated.
2. **Document Traceability Updates:**

   * When edits are made to test documentation (e.g., procedures, cases, scripts), document these changes in the traceability matrix or test notes. This creates a clear, auditable record of modifications.
3. **Simplify Cross-Team Communication:**

   * Ensure all team members understand the traceability mechanism in use (e.g., links or matrix), so everyone can easily maintain and utilize it.

---

### **Conclusion:**

For small projects, the method of linking related test procedures to the same requirements—whether via direct notes or a manageable traceability matrix—ensures that testing documentation remains consistent and easily navigable. This approach minimizes the overhead of handling requirement changes, reduces errors from missed updates, and maintains test coverage against project requirements, even with limited resources.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-072) Checklist for the Contents of Software Critical Design Review (CDR),
   580-CK-008-02, Software Engineering Division, NASA Goddard Space Flight Center (GSFC), 2010.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-505)

  [Mars Observer Attitude Control Fault Protection](https://llis.nasa.gov/lesson/345 "Click to open in new window")

  Public Lessons Learned Entry: 345.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The following lesson learned from NASA’s Lessons Learned database emphasizes the criticality of comprehensive system engineering practices, fault protection design, and validation through complete and thorough testing.

#### **Lesson Summary: Mars Observer Attitude Control Fault Protection**

* **Lesson ID:** 0345
* **Event:** The Mars Observer (MO) mission failure.
* **Root Causes Analysis:**
  + **System Engineering Deficiency:** A lack of a cohesive, top-down system engineering design approach led to gaps in fault protection. Fault protection was primarily implemented as low-level redundancy management rather than being integrated into a comprehensive fault management strategy at the system level.
  + **Incomplete Testing Practices:** The fault protection software was never fully tested on the actual flight spacecraft before launch. This omission prevented detection of critical issues related to the system’s ability to monitor and respond to excessive attitude control errors.

---

### **Lessons Learned:**

1. **Develop Fault Protection from a Top-Down Perspective:**

   * Fault protection should be designed as part of a cohesive, system-level engineering approach that seamlessly integrates hardware and software fault-handling capabilities. A bottom-up or piecemeal approach may leave critical fault scenarios unaddressed and increase the likelihood of failure during flight.
2. **Design Fault Protection for Critical Scenarios:**

   * Include explicit fault protection measures to detect and respond to excessive attitude control errors or similar mission-critical failures. Utilize redundancy at higher levels (e.g., system-wide fault management frameworks) rather than relying solely on low-level redundancy mechanisms.
3. **Test Fault Protection Software on the Flight Spacecraft:**

   * Thoroughly test all aspects of the fault protection software, particularly its interactions with flight hardware, before launch. Testing fault protection software in the actual mission configuration (e.g., flight spacecraft plus final deployment conditions) ensures realistic validation of its functionality.

---

### **Key Recommendations (Lessons Applied):**

Based on this lesson, the following actions can help mitigate similar risks in future projects:

#### **1. Incorporate Comprehensive System Engineering Practices**

* Use a **top-down system engineering design approach** during system development. This ensures fault protection is integrated into the entire spacecraft subsystem hierarchy, addressing interactions among hardware, software, and mission operations.
* Perform **system-level hazard analysis** to identify all possible failure scenarios that fault management systems must address. Clearly document these scenarios in system engineering and fault management design documents.
* Include fault management design reviews during critical design phases (e.g., Preliminary Design Review, Critical Design Review) to ensure fault protection is robust and complete.

#### **2. Design Fault Protection Strategies Proactively**

* Fault protection strategies should identify key mission-critical subsystems, like attitude control, as **priority areas for fault detection and mitigation.**
* Ensure fault protection can respond to both **nominal and off-nominal commanding scenarios**, including unintended operator interventions, excessive errors, and hardware malfunctions.
* Implement holistic redundancy strategies that span system layers (e.g., sensors, software, thrusters) and provide end-to-end coverage of failure modes, rather than piecemeal management of individual subsystems.

#### **3. Perform End-to-End Validation Testing**

* Conduct fault protection software and hardware **validation testing on the flight spacecraft** under real or realistic operational conditions. This includes:
  + Testing for mission-critical errors, system health monitoring, and recovery sequences.
  + Simulating off-nominal conditions, environmental constraints, and fault scenarios (including attitude errors or reaction control thruster [RCS] failures).
* Verification efforts should **go beyond individual subsystem tests** and include full system integration tests, including hardware–software interactions.
* Use a Hardware-in-the-Loop (HIL) or Software-in-the-Loop (SIL) setup for testing wherever possible. This approach ensures any discrepancies or emergent issues between software and hardware are discovered before launch.

#### **4. Test the Entire Fault Protection Workflow**

* Fault protection testing must encompass:
  + Detection mechanisms (e.g., thresholds for excessive attitude control errors).
  + Fault isolation to determine the source of the error (e.g., gyroscope malfunction, thruster misalignment).
  + Recovery mechanisms (e.g., transitioning to backup systems, RCS thruster interventions) and functionality verification.

#### **5. Apply Lessons Learned Across Similar NASA Missions:**

* Deploy mechanisms to analyze fault management frameworks from past projects systematically. Incorporate lessons learned not just into similar planetary missions, but also into any spacecraft systems with autonomous fault management requirements.
* Update relevant NASA standards and fault management design guidelines (e.g., **SWE-086** for fault detection) with examples from this and similar mission issues.

---

### **Broader Implications:**

* The Mars Observer failure illustrates the potential risks of late-stage testing omissions and incomplete fault management strategies. Similar lessons can be applied to:
  + Pointing systems for satellites and telescopes.
  + Reaction control systems for planetary landers, rovers, and deep-space probes.
  + Critical autonomous systems (e.g., collision avoidance, thermal protection, and guidance software).

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

### **7.** **Lesson Learned (Starliner CFT):** **Integrated modeling and simulation must exercise end‑to‑end behaviors with sufficient fidelity and data capture.**

**Project Context:**  
Derived from Starliner CFT Investigation.

**Problem/Observation:**  
Simulation and integrated testing did not fully reflect mission operations and off‑nominal transitions; telemetry sample rates were inadequate for meaningful analysis.

**Contributing Factors:**

* Low telemetry fidelity limited comparison between simulation and flight.
* Simulation scenarios missed combined safing and reset behavior interactions.

**Impacts:**

* Hidden interactions persisted, fault‑tolerance gaps remained undetected.
* Difficulty in reproducing and understanding flight anomalies.

**Recommended Practices (Aligned to SWE‑029/071/073):**

* Build **scenario libraries** covering nominal, off‑nominal, safing, resets, degraded modes.
* Ensure **telemetry fidelity** (rates, fields, timestamps) supports validation and anomaly reproduction.
* Validate **model fidelity** against flight‑like data; maintain model‑to‑flight delta logs.

**Actionable Checks:**

* Scenario coverage matrices exist and are maintained.
* Telemetry requirements specify minimum sample rates and precision.
* Model validation reports compare against integrated test/flight‑like runs.

### **Additional Lessons Learned from NASA Database:**

1. **Lesson Learned from the Mars Climate Orbiter (MCO) Incident:**

   * **Lesson ID:** 5683
   * Ensure that system integration tests account for interface mismatches and unit errors (e.g., metric-imperial unit errors that led to trajectory miscalculation).
   * **Takeaway:** Like the Mars Observer, MCO suffered from incomplete system-level validation and insufficient end-to-end testing. Fault recovery should validate hardware and trajectory alignment thoroughly in all conditions.
2. **Lesson Learned from the Spirit and Opportunity Rovers:**

   * **Lesson ID:** 6348
   * **Lesson Summary:** Include thorough simulation of fault scenarios to validate the fault protection software’s decision-making capabilities under a wider range of conditions.
   * **Takeaway:** Small, seemingly benign faults that cascade should be vigorously tested. Early identification and on-orbit validation of fault protection strategies can improve long-term system autonomy and reliability.

**Conclusion:**

This lesson from the Mars Observer emphasizes the importance of:

* Incorporating **robust fault protection design** throughout the system design and engineering process.
* Conducting **complete and thorough validation tests** of fault protection software on the flight spacecraft or its equivalent representative testing environment under mission-like conditions.  
  Adopting these best practices can reduce the likelihood of similar failures in future missions, ensuring fault handling is robust, fully tested, and aligned with mission objectives.

### 8. **Incomplete Verification & Validation (V&V)**

**Incident:**  
The project faced major V&V shortfalls, including approximately 1,000 unverified system requirements and incomplete GNC, fault protection, and FSW test coverage. Immature and incompatible testbeds further hindered simulation and closed‑loop testing.

**Lesson Learned:**

* **Comprehensive V&V Execution:** V&V must be resourced, scheduled, and monitored with the same rigor as hardware development.
* **Validated Testbeds:** Testbeds and simulations must be synchronized early with vendor tools to ensure accurate system‑level testing.

**Implication:**  
Insufficient V&V undermines mission confidence and may conceal system defects until it is too late to correct them within the launch window.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Key Mission Ops Tests essential to timely V&V of flight design/mission ops concept& launch readiness](https://software.gsfc.nasa.gov/lesson-details/342/).**Lesson Number 342**: The recommendation states: "Develop/iterate/execute system level tests to verify/validate data system/mission Concept of Operations during Observatory I&T (e.g., the Comprehensive Performance Test (CPT) and Day-in-the-Life (DiTL) test). The CPT should be: a) thorough (exercising all copper paths, as many key data paths as reasonable, and using operational procedures); b) executed prior to/post significant events throughout Spacecraft & Observatory I&T; and c) designed comprehensive, yet short enough to be executed multiple times (e.g., the PACE CPT was specifically designed to be 4-5 days). The multi-pass DiTL test can demonstrate nominal operational procedures/processes and, when executed prior to the pre-environmental CPT, can be the basis for the instrument functionals during the environmental cycles and post environmental functional checkouts of the instruments."
* [Goddard Dynamic Simulator (GDS) Fault Management derived Requirements](https://software.gsfc.nasa.gov/lesson-details/344/).**Lesson Number 344**: The recommendation states: "The Goddard Dynamic Simulator (GDS) team needs to review the GDS requirements when the fault management table is initially defined (as well as when there are changes to the tables), and during the FSW Build Testing phase, at the start of Systems Testing. This review should include working with the Flight Software team at the contents of the Fault Detection and Correction (FDC) tables to determine what telemetry needs to be simulated. This review may result in new GDS requirement(s)."

# 7. Software Assurance

**SWE-071 - Update Test Plans and Procedures**

4.5.7 The project manager shall update the software test and verification plan(s) and procedure(s) to be consistent with software requirements.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Analyze that software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically the off-nominal scenarios.

## 7.2 Software Assurance Products

**Objective:** Ensure all software requirements, including safety-critical and hazard controls, are fully tested and verified through systematic planning, execution, and analysis. Software assurance (SA) products should provide evidence of requirement coverage, hazard mitigation validation, and corrective actions where necessary.

#### **Evidence and Artifacts to Include:**

Software assurance products should demonstrate comprehensive test coverage and a complete verification of all requirements. Relevant artifacts and evidence include, but are not limited to:

* **Software Test Plan(s):** Documented plans specifying the scope, approach, resources, schedule, and methods for testing software requirements and hazard controls.
* **Software Test Procedure(s):** Step-by-step instructions to execute specific test cases, ensuring accurate and repeatable results.
* **Traceability Matrix:** Establishes bidirectional traceability between software requirements and test procedures to verify complete coverage and identify gaps.
* **Test Coverage Metric Data:** Metrics illustrating the extent to which software requirements, safety-related functions, and hazard mitigations are covered by test cases—both nominal and off-nominal scenarios.
* **Analysis Results:** Results from reviews, inspections, or audits, showing the adequacy of the test plans and procedures in meeting software assurance requirements.
* **Defect and Non-Conformance Reports:** Summarize corrective actions for identified issues.
* **Peer Review Documentation:** Evidence of peer reviews conducted for the test plans and procedures, ensuring consensus and quality.
* **Test Execution Logs:** Detailed execution results, including tests passed, failed, or blocked, and links to defect reports and regression test impacts.

The combination of the artifacts above provides assurance that testing is comprehensive, aligned with up-to-date requirements, and capable of identifying both nominal and fault conditions.

---

## 7.3 Metrics

**Objective:** Use metrics to monitor and measure test coverage, risk exposure, and the effectiveness of software assurance tasks throughout the software development lifecycle. Metrics serve as critical tools for tracking progress, identifying gaps, and ensuring compliance with requirements.

#### **Recommended Metrics:**

1. **Testing Progress and Coverage:**

   * Number of detailed software requirements tested to date vs. the total number of detailed software requirements.
   * Number of software requirements with completed test procedures/cases over time.
   * Percentage of software requirements adequately covered by test cases (nominal and off-nominal).
   * Number of software requirements being met via satisfactory testing vs. the total number of software requirements.
2. **Traceability and Test Documentation:**

   * Number of software requirements without associated test cases—a critical metric for identifying gaps in traceability.
   * Number of non-conformances identified when approved, updated requirements are not reflected in test procedures.
   * Traceability completeness: Number of requirements with verified test cases vs. total requirements.
3. **Safety and Hazard Verification:**

   * Number of non-conformances identified while confirming hazard controls are adequately verified through test plans, procedures, and test cases.
   * Number of safety-related non-conformances identified over time and by life cycle phase.
   * Number of safety-related requirement issues (open vs. closed) tracked over time.
4. **Defect and Non-Conformance Monitoring:**

   * Number of non-conformances and risks open vs. total non-conformances and risks identified within test procedures.
   * Number of non-conformances identified in test documentation (e.g., in test plans, schedules, procedures).
   * Number of software work product non-conformances identified by life cycle phase.
5. **Regression and Change Impacts:**

   * Number of regression tests executed over time to verify safety-critical code and requirement adherence after defect fixes or changes.
   * Number of new issues introduced during fixes or changes, identified by regression testing.

**Reference:** Also see **Topic 8.18 - SA Suggested Metrics** for additional examples and best practices for tailoring metrics to project needs.

---

## 7.4 Expanded Guidance

#### **Analyzing Test Plans and Procedures:**

1. Ensure that test plans and procedures provide **complete coverage of software requirements**, with a particular focus on:

   * **Safety-critical requirements:** Verify all hazard controls, mitigations, and fail-safes are adequately accounted for and tested.
   * Nominal, operational, and **off-nominal scenarios**, along with boundary conditions, to simulate real-world edge cases.
   * All phases of testing, including unit testing, integration testing, system/end-to-end testing, regression testing, acceptance testing, and interface testing.
2. Use **checklists** during reviews to confirm that:

   * Test plans include detailed descriptions of the scope, test environments, tools, and constraints.
   * Test procedures outline repeatable and traceable steps to validate each requirement.
   * Boundary conditions, failure modes, and hazardous scenarios are specifically called out in the tests.

#### **Tracking Updates to Test Documentation:**

Test plans and procedures should evolve as software requirements change throughout the life cycle. Key documents to update include:

* System test plans and procedures.
* Unit/regression/integration test plans, test cases, and scripts.
* Safety-related test cases and test matrices.
* Test schedules to reflect changes in scope, timeline, or resource allocation.

When requirements change:

1. **Traceability Matrices:** Update and review traceability matrices to ensure test documentation aligns with the updated requirements. Check if change impacts ripple through related test artifacts.
2. **Regression Testing:** Confirm that regression test suites are updated to include scenarios impacted by the change while ensuring previously tested requirements and safety-related cases are not compromised.
3. **Analysis and Verification:** Re-analyze linked test artifacts (e.g., cases, data, scripts) to ensure they address the changes.

---

#### **Testing for Corrective Actions (Defects and Changes):**

1. When defect fixes or requirement changes are tested, always run **regression tests** to verify:
   * The specific issue was resolved as intended.
   * No other requirements, especially safety-related requirements, were inadvertently affected.
2. Use **risk-based criteria** when selecting regression test cases (per **SWE-191 - Software Regression Testing**). Prioritize:
   * Safety-critical functionality.
   * Code/modules with a history of defects.
   * High-complexity or high-risk areas of the software.

#### **Ensuring Safety Through Testing:**

* **Safety Verification:** All safety features, controls, failure modes, and boundary conditions should be explicitly defined and verified in test documents.
* Plan for **off-nominal testing** to validate the software’s ability to respond to unexpected or adverse inputs gracefully. See **Topic 8.01 - Off Nominal Testing** for strategies.

---

### **Additional Best Practices:**

1. **Peer Reviews:**

   * Perform peer reviews of test plans and procedures to ensure quality before the documents are executed. Address any gaps flagged during these reviews.
2. **Independent Oversight:**

   * Engage software assurance engineers to **independently verify** that all test plans, cases, and results support requirements coverage and hazard mitigation strategies.
3. **Maintain Configuration Control:**

   * Implement appropriate **configuration management** (see **SWE-080 - Track and Evaluate Changes**) to ensure test plans, procedures, and matrices remain consistent with evolving software baselines.
4. **Automated Tools:**

   * Use automated test case management tools to link test artifacts (test plans, results, scripts) with requirements and track real-time metrics.

---

### **Conclusion:**

Following this enhanced guidance ensures that software assurance adequately verifies all software requirements, including hazard controls, throughout the project life cycle. By developing clear test documentation, maintaining traceability, using metrics, and thoroughly analyzing safety-critical scenarios, projects will minimize risks, improve test coverage, and support mission success.

 See the software assurance guidance in [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) for selecting regression test sets.

See also [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification),

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)       * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence refers to tangible artifacts, outputs, or documentation that validate compliance with requirements, demonstrate test coverage, and substantiate claims of effective verification. Below are examples of objective evidence that can be provided for Requirement 7.2:

---

### **1. Artifacts Demonstrating Test Planning**

These artifacts ensure testing processes align with software requirements and hazard control coverage:

* **Software Test Plan(s):**
  + A detailed document outlining the testing scope, schedule, tools, objectives, and strategies for verifying software requirements and hazard controls.
  + Includes plans for unit testing, integration testing, system testing, acceptance testing, and regression testing.
* **Test Planning Peer Reviews:**
  + Minutes from peer reviews that evaluate the completeness and accuracy of the test plans.

---

### **2. Traceability Artifacts**

Demonstrate full alignment between software requirements, test procedures, and hazard controls to ensure nothing is overlooked:

* **Requirements Traceability Matrix (RTM):**
  + Provides bidirectional traceability between software requirements and their associated test cases, test procedures, and test results.
  + Includes test traceability to hazard controls, safety-critical requirements, boundary conditions, and off-nominal scenarios.
  + Documents updates and impacts as requirements evolve.
* **Traceability Compliance Report:**
  + Summarizes the traceability matrix results, listing requirements with complete or incomplete coverage by tests.

---

### **3. Artifacts Demonstrating Test Execution**

Evidence that all planned tests have been executed and aligned to the approved test plan.

* **Test Procedures:**
  + Detailed documentation of how each test is executed, including inputs, expected results, actual results, and criteria for passing or failing the test.
  + Includes references to specific hazards or failure conditions being tested.
* **Test Cases:**
  + Individual descriptions of tests and their conditions, e.g.:
    - Inputs: Specific values/conditions tested.
    - Outputs: Expected software behavior.
    - Results: Pass, fail, or blocked.
* **Test Results and Execution Logs:**
  + Logs generated by the test execution process, showing:
    - Date, time, and environment of execution.
    - Successfully passed, failed, or pending tests.
    - Test execution evidence, such as screenshots, simulator output, or hardware-in-the-loop (HIL) responses.
  + Regression test results to confirm that software changes have not introduced new defects.

---

### **4. Metrics Reports**

Provide insights into testing progress, coverage, and identified issues. Examples:

* **Test Coverage Metrics:**
  + Percentage of software requirements covered by tests.
  + Percentage of safety-critical or hazard control requirements tested.
* **Test Progress Metrics:**
  + Number of software requirements with completed test procedures to date vs. the total number of requirements.
* **Defect Identified Metrics:**
  + Number and severity of non-conformances discovered during testing.
  + Trends over time in safety-related non-conformances and issue closure rates.

---

### **5. Supporting Evidence for Safety and Hazard Controls**

Show explicit testing and validation of safety-critical requirements:

* **Safety Test Plan and Procedures:**
  + A section or standalone document that addresses all safety-specific tests, including hazard mitigations, fault detection and response, and off-nominal scenarios.
  + Example: Test cases that simulate excessive attitude control errors and validate system responses (e.g., activation of thrusters, fault-handling algorithms), as might have prevented the **Mars Observer incident** (Lesson 0345).
* **Test Results for Safety Features:**
  + Logs of safety feature tests, demonstrating that all safety controls and mitigations function as intended.
  + Evidence of off-nominal performance, including logs verifying correct behavior in adverse or boundary conditions.

---

### **6. Analysis Reports**

* **Gap Analysis Reports:**
  + Documents gaps between requirements and testing (e.g., missing test cases or associated risk areas).
  + Includes mitigation strategies to address gaps.
* **Impact Analysis Reports:**
  + Detailed evaluation of the impact of requirement or design changes on test plans, procedures, and executed tests.
* **Traceability Check Analysis:**
  + Demonstrates regular updates and validation of traceability between requirements, tests, and defect reports.

---

### **7. Defect and Corrective Action Reports**

Evidence of successful identification, reporting, and resolution of issues during the testing process:

* **Non-Conformance Reports (NCRs):**
  + For identified test failures, defects, or hazards, describing the issue, its criticality, and associated corrective actions.
* **Defect Reports:**
  + Logs of defect tracking and closure, with details of affected test cases and requirements.
* **Corrective Action Validation:**
  + Evidence (e.g., regression tests) that defects and safety-critical issues have been corrected effectively without introducing new issues.

---

### **8. Review Documentation**

Documented evidence of test process validation and assurance:

* **Test Plan Review Report:**
  + Ensures test plans meet project requirements and objectives.
* **Test Execution Review Reports:**
  + Assessments of test results, highlighting conformity, anomalies, issues, and testing gaps.
* **Configuration Management Reports:**
  + Verification that updates to test documentation were properly managed under configuration control processes.

---

### **9. Training and Team Readiness**

Evidence that the testing team is adequately trained and qualified to execute the test plans effectively:

* **Training Records:**
  + Document training on test environments, tools, and procedures.
* **Tool Verification Reports:**
  + Ensure the tools used for test execution and analysis are correctly installed, verified, and validated.

---

### **10. Lessons Learned Integration**

Evidence that lessons from previous projects and NASA’s Lessons Learned database are incorporated:

* **Fault Protection Test Evidence:**
  + Specific test cases addressing lessons like **Lesson 0345**, ensuring fault protection software is tested for attitude control errors or other mission-critical scenarios before launch.
* **Off-Nominal Test Coverage Report:**
  + Evidence of off-nominal tests derived from historic root cause analyses in similar missions.

---

### **Example Artifacts Deliverable Checklist:**

* Software Test Plan and Procedures.
* Traceability Matrix between Requirements and Test Cases.
* Test Case Documents and Actual Test Results.
* Coverage Report (e.g., list of tested vs. untested requirements).
* Metrics Dashboard for Coverage, Progress, and Defects.
* Safety Test Reports: Nominal and Off-Nominal Scenarios.
* Non-Conformance Reports Logged During Testing.
* Regression Test Results (if applicable).
* Peer Review Minutes for Testing Artifacts.
* Impact and Change Analysis Due to Requirement Updates.

---

### **Conclusion:**

Objective evidence ensures the software assurance process is both systematic and verifiable, with a direct connection to software requirements, test results, and corrective actions. Providing such evidence creates transparency, confirms compliance, and mitigates risks associated with incomplete testing or unverified safety-critical requirements.

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
