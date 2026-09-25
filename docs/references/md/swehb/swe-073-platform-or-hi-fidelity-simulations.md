# SWE-073 - Platform or Hi-Fidelity Simulations

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695454. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations

SWE-073 - Platform or Hi-Fidelity Simulations

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695454)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695454&showCommentArea=true&showComments=true#addcomment)

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

4.5.8 The project manager shall validate the software system on the targeted platform or high-fidelity simulation.

## 1.1 Notes

Typically, a high-fidelity simulation has the exact processor, processor performance, timing, memory size, and interfaces as the target system.

## 1.2 History

Click here to view the history of this requirement: SWE-073 History

SWE-073 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.4.9 The project shall ensure that the software system is validated on the targeted platform or high-fidelity simulation. |
| Difference between A and B | No change |
| B | 4.5.10 The project manager shall validate the software system on the targeted platform or high-fidelity simulation. |
| Difference between B and C | No change |
| C | 4.5.8 The project manager shall validate the software system on the targeted platform or high-fidelity simulation |
| Difference between C and D | No change |
| D | 4.5.8 The project manager shall validate the software system on the targeted platform or high-fidelity simulation. |

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

Validation is a process of evaluating work products to ensure that the right behaviors have been built into the work products. The right behaviors adequately describe what the system is supposed to do and what the system is supposed to do under adverse conditions. They may also describe what the system is not supposed to do.

Validation is performed to assure that the specified software systems fulfill their intended use when placed on the targeted platform in the target environment (or simulated target environment). The methods used to accomplish validation on the actual target platform or in a high fidelity simulator may include aspects that were applied to previous software work products (requirements, designs, prototypes, etc.). The use of these methods provides continuity of results through the assembling system. The use of the high-fidelity or targeted system allows the software developers to check systems-level interfaces, memory performance and constraints, event timing, and other characteristics that can only be evaluated properly in the real system or near-system environment (see [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation)). Validation activities include preparation, performance, analysis of results, and identification of corrective action. Validation at the systems level ensures that the correct product has been built. [001](#_tabs-<p></p>)

Validating the software system on the actual **targeted platform** (or a **high-fidelity simulation** when the platform is unavailable) ensures that the software operates as intended within the real-world conditions or as close to them as possible. This step is critical for confirming that the system is both functionally correct and capable of meeting mission needs. Below is the rationale for this requirement across various technical, operational, and risk management contexts.

---

### **1. Verification vs. Validation Distinction**

* **Verification** involves checking that the software meets its specifications (e.g., through reviews, inspections, and unit tests).
* **Validation**, by contrast, confirms that the software meets the actual needs of the user and operates correctly within the specific mission or operational environment.

Validating the software on its **intended platform**—or a high-fidelity simulation if the platform is inaccessible—provides definitive evidence that the software can fulfill its mission objectives in real-world conditions.

---

### **2. Real-World Context: Targeted Platform Validation**

Validating the software on the **actual targeted platform** ensures:

#### a. **Hardware–Software Interaction Validation:**

* Software systems heavily interact with hardware components such as sensors, actuators, controllers, and interfaces. Validation ensures:
  + Proper communication between the software and hardware interfaces.
  + Accurate timing, processing, and functional execution on real hardware.
  + Detection and mitigation of bottlenecks caused by platform-specific hardware constraints (e.g., CPU, memory, bus bandwidth).
* **Example:** A rover's real-time obstacle avoidance code must be validated against its physical hardware sensors and onboard constraints.

#### b. **System Integration Validation:**

* Real-world operational systems (e.g., embedded systems) rely on full integration between software, hardware, and system components. Platform-dependent issues, such as interrupt handling, memory conflicts, or I/O operations, are often detected only during platform-specific testing.
* **Example:** Integration of software with spacecraft navigation interfaces like star trackers or gyroscopes may show timing mismatches that were undetectable in isolated software tests.

#### c. **Environmental Validation:**

* The actual targeted platform exposes the software to its operational environment. Problems not observable during unit or integration testing—such as thermal drift, clock synchronization issues, or response lag—can emerge when validating the system in the intended mission environment.

---

### **3. When the Targeted Platform is Unavailable: High-Fidelity Simulation**

If validating directly on the targeted platform is not feasible, **high-fidelity simulations** serve as the next best alternative:

#### a. **Simulation Advantages:**

* High-fidelity simulations emulate hardware behavior, environmental conditions, and system constraints with sufficient accuracy, enabling the validation of:
  + Timing-critical operations.
  + Fault recovery and fallback procedures.
  + Nominal and off-nominal conditions and edge cases.
* **Example:** For deep space exploration missions where there is only one flight model of the spacecraft software running on the actual spacecraft hardware, high-fidelity ground-based simulators can closely replicate flight conditions.

#### b. **Use Cases for High-Fidelity Simulations:**

* Situations where the actual hardware is unavailable, inaccessible, or expensive to use:
  + Hardware prototypes not ready in early phases.
  + Software being developed in parallel with hardware.
  + Critical missions with a single hardware instance.
* **Limitations:** While simulations are valuable, validation that does not involve the actual platform might fail to expose platform-specific errors (e.g., real hardware misbehavior). Therefore, the software should ultimately be validated on the real platform where possible.

---

### **4. Risk Mitigation**

Validating software on the actual platform or a high-fidelity simulation addresses critical risks:

#### a. **Mission Risk Reduction:**

* Failure to validate on the correct platform could lead to undetected issues that result in mission failure or degraded mission performance.
* **Example:** The Mars Climate Orbiter failure (1999) was partially attributed to unverified integration between software and mission systems, which led to a metric-imperial unit conversion error.

#### b. **Hazard and Safety Mitigation:**

* Safety-critical software—such as that for spacecraft fault protection—must be validated on the targeted platform to ensure the proper functioning of hazard controls under mission-specific conditions.
* **Example:** Fault protection software for managing excessive attitude control errors must be tested on actual hardware (or its high-fidelity simulation counterpart) to ensure timely fault detection and response, as highlighted by **NASA Lesson Learned 0345 (Mars Observer failure).**

#### c. **Early Defect Detection:**

* Platform-specific errors, such as timing, memory utilization, and hardware interrupts, are typically detected only when software runs on the platform itself.

---

### **5. Performance Validation and Optimization**

Software's real-world performance can significantly differ from laboratory or simulated conditions:

* Validating software on the **targeted platform** ensures:
  + Accurate profiling of execution times, resource utilization, and system load under real conditions.
  + Benchmarking of software performance against mission requirements.
  + Optimization opportunities for software based on actual performance data (e.g., reducing latency, optimizing I/O operations).
* **Example:** Validating guidance, navigation, and control (GN&C) software for a lander ensures it meets real-time deadlines during descent phases.

---

### **6. Example Scenarios Supporting the Rationale**

#### a. **Rover Missions:**

* Testing the software driving a Mars rover must involve its actual platform or a high-accuracy simulator. This ensures control algorithms interact properly with the rover’s wheel drive system, onboard sensors, and the constraints of the Martian environment.

#### b. **Satellites/Spacecraft:**

* Software managing telemetry data must be validated onboard to confirm compatibility with actual communication subsystems and avoid loss of data or communication blackouts.

#### c. **Aerospace Flight Systems:**

* Aircraft or spacecraft avionics software must be validated in high-fidelity simulators when flight hardware testing is expensive or impractical prior to launch.

#### d. **Robotics Systems:**

* Off-nominal event handling (e.g., collision avoidance) in robotic arms must reflect hardware constraints during validation.

---

### **7. Lessons Learned Supporting the Rationale**

Numerous NASA Lessons Learned highlight cases where inadequate or platform-dissimilar validation led to mission failures:

1. **Mars Observer (Lesson Learned 0345):**
   * Fault protection software was never tested on the flight spacecraft, leading to system failure. **Lesson:** Always test software on the actual platform or high-fidelity equivalent.
2. **Mars Climate Orbiter (MCO):**
   * Integration issues between interfacing systems were missed because real mission profiles were not sufficiently validated.
3. **Juno Spacecraft Deployment Delay:**
   * Successful deployment delays were mitigated through high-fidelity ground simulations that allowed engineers to debug critical timing issues.

---

### **8. Compliance Validation**

How this requirement is met:

* If the **targeted platform** is available and accessible, execute the validation tests directly on it.
* When the platform is not available, create and verify the fidelity of the **high-fidelity simulation** before using it for validation.
* Document the validation process thoroughly with:
  + Test plans, procedures, and results.
  + Traceability to requirements and high-risk use cases.
  + Non-conformance reports and the resolutions made, including regression testing as necessary.

---

### **Conclusion**

Validating software on the targeted platform or high-fidelity simulation is essential for ensuring mission success, software reliability, and adherence to safety-critical requirements. It confirms that the software will operate correctly in its intended operational environment and reduces the risk of mission failure due to platform-specific or system-level integration issues. This validation step is indispensable for achieving the high standards of quality and safety necessary for NASA missions.

See also [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results).

# 3. Guidance

## 3.1 Validation Process

#### **Distinction Between Validation and Verification**

* Validation and verification are **separate but complementary processes** integral to software development:

  + **Validation** answers the question, "**Did we build the right product?**" by ensuring that the software satisfies stakeholder needs, addresses the intended use, and behaves correctly across the entire system.
  + **Verification** answers the question, "**Did we build the product right?**" by confirming conformity to specific requirements, technical specifications, and design standards.

  Validation focuses on **system-level functionality and user needs**, while verification ensures **artifact-level compliance** (i.e., that requirements have been correctly implemented).

---

#### **Scope of Validation in this Requirement**

Validation activities, as used in this requirement, address two key domains:

1. **Requirements Validation with Stakeholders:**

   * Ensure requirements are clear, correct, complete, and consistent, with active confirmation from stakeholders. Misunderstandings or assumptions in requirements can lead to downstream system-level failures.
   * Address implied or derived requirements (e.g., "X must occur before Y"), ensuring they are thoroughly identified, documented, and validated.
2. **System-Level Validation After Integration:**

   * Validation focuses on ensuring that the **fully integrated software system** meets the operational needs of the stakeholders and functions as intended in the target deployment or simulated environment.
   * This includes:
     + Analysis of **system-level interactions** (e.g., module dependencies, interface behavior, end-to-end scenarios).
     + Examination of the system as a **cohesive whole**, ensuring it delivers the desired functionality derived from multiple individual software components.
     + Validation in either the actual operational environment or, when infeasible, through a **high-fidelity simulation**.

---

#### **Validation in Real vs. Simulated Environments**

1. **Targeted Platform Validation:**

   * Validate the software directly on the **target operational platform**, verifying real-world conditions such as:
     + Specific hardware configurations and architectural constraints (e.g., processors, memory limits).
     + Real-life timing behavior and resource consumption.
     + **Stakeholder demonstrations**, where users interact with the actual product.
   * Benefits:
     + Identifies platform-specific issues related to hardware-software integration, resource utilization, and timing that may not appear in simulations.
     + Provides the closest approximation to the eventual mission deployment.
2. **High-Fidelity Simulation Validation:**

   * When validating in the actual operational environment is impractical (e.g., cost, high risk, hardware unavailability), simulate the operational platform with high fidelity (e.g., exact processor type, memory size, hierarchical interfaces, and timing performance).
   * Scenarios to consider:
     + Nominal and off-nominal behaviors.
     + Hazardous situations, safety-critical functions, and recoverability after failures.
   * Limitations:
     + Simulation may not capture rare real-world anomalies, such as environmental coupling effects or unforeseen platform-specific dependencies.

---

#### **Consideration for Safety-Critical Software**

For **Class A software** (typically critical to mission or operator safety), specific care must be taken to validate:

* All software functionality that may impact **safety-critical systems**, particularly interactions with hardware and fault protection mechanisms.
* **Hazardous situations** modeled after potential operator errors or operational constraints, including scenarios like:
  + **HR-33: Inadvertent Operator Action**—Validating safeguards to prevent unintended system commands.
  + Hardware or system malfunctions that could escalate if software fails to detect or mitigate issues promptly.
* **Behavior under extreme, boundary, or fault conditions** (e.g., high-latency communications, unexpected sensor failures).

---

## 3.2 Validation Approach

The validation approach should be tailored to the specific system and operational scenario. The two key approaches—real-world and simulated—both focus on determining if the fully integrated software product fulfills its **intended use** as a system and addresses stakeholder expectations, derived requirements, and overall usability.

#### **Operational Environment Demonstrations**

Using the **actual operational environment** is preferred whenever possible, as this provides the highest fidelity and most realistic validation. Examples include:

1. **Purpose:**
   * Confirm **correctness of implied, derived, or inherent requirements**:
     + Example: “Software must operate continuously under specific environmental conditions” without external intervention.
   * Validate the system fulfills its ultimate purpose, going beyond verifying isolated individual components or functions.
2. **Key Goals:**
   * Prove that the system, as a collected implementation of all requirements, functions cohesively across:
     + Intended user workflows and mission objectives.
     + Integration with hardware and physical subsystems.
3. **Benefits:**
   * Allows for real-world testing of **user-created scenarios** to validate that the system satisfies unanticipated user needs and edge cases.
   * Simulates operational risks realistically (e.g., weather conditions, power fluctuations, ground-station communication delays).

---

#### **Simulated Operational Environment**

When running software on the actual operational platform is impractical, a **high-fidelity simulated environment** is an effective alternative, designed to emulate as many aspects of the target platform as possible.

1. **Objectives:**
   * Confirm that the functional and performance goals of the software system are met when working as part of a complete mission system (e.g., integration with other software subsystems, hardware interfaces, timing behaviors).
   * Identify potential operational risks prior to deployment on the actual platform.
2. **Key Considerations:**
   * Ensure simulation accuracy includes:
     + Processor architecture and performance.
     + I/O interfaces and response timing.
     + Simulated mission scenarios with nominal and off-nominal conditions.
   * Maintain focus on **collected system requirements**:
     + Validate not just individual requirements but how the system performs holistically in fulfilling mission or end-user objectives.
3. **Examples:**
   * Simulated landing scenarios for spacecraft.
   * Simulated latency for deep space communication systems.

---

#### **Portability Validation**

For systems requiring portability across multiple platforms:

1. Test software on the complete suite of required platforms.
2. Confirm compatibility with platform-specific variations, including OS versions, hardware configurations, performance metrics, and timing.
3. Include user-submitted operational scenarios to expose platform-specific boundary conditions.

---

### **Key Lessons Learned**

* Utilize **user-created operational scenarios** to confirm usability and functional fitness across intended operational situations. Users often bring unique perspectives that exploratory testing might not identify.
* High-fidelity simulations are valuable for hazard mitigation and failover testing but must be rigorously validated for accuracy to avoid false positives or undetected errors.

---

### **Connection to Related Guidance**

* **SWE-055 – Requirements Validation:** For detailed guidance on validating requirements in early lifecycle stages.
* **SWE-191 – Regression Testing:** When validating defect fixes, ensure previously tested requirements and functionalities hold true.
* **Topic 7.15 – Relationship Between NPR 7150.2 and NASA-STD-7009:** For understanding how validation activities align with NASA standards.

---

### **Conclusion**

Validation is an essential aspect of the software engineering process that confirms the system meets operational needs holistically. Whether through physical testing on the target platform or a high-fidelity simulation, the goal is to ensure stakeholder requirements—including implied, derived, and operational requirements—are satisfied in practical terms. Focusing on system-level interactions, safety-critical behavior, and real-world user scenarios improves the quality and reliability of software systems before deployment.

The basic validation process is shown below with the steps addressed by this requirement highlighted:

Validation activities are not be confused with verification activities as each has a specific goal. Validation is designed to confirm the right product is being produced while verification is conducted to confirm the product being produced meets the specified requirements correctly.

See Lessons Learned for other considerations related to simulated environment validation.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

For small projects, where resources (time, budget, personnel, and infrastructure) are typically limited, the general goals of **validation** remain the same: ensure that the software meets the operational needs and expectations of stakeholders. However, the **approach must be tailored** to fit the project's scale while maintaining quality and reliability. Below is simplified guidance to help small projects meet the intent of the validation process effectively.

---

### **Key Considerations for Small Projects:**

1. **Keep Validation Efforts Proportional:**

   * Scale the validation process to the size and complexity of the project while still addressing critical system-level behavior, safety, and operational fit.
   * Prioritize validation activities based on **risk**, **criticality** of requirements, and **available resources**.
2. **Focus on Stakeholder-Driven Validation:**

   * Engage stakeholders early and continuously to confirm their needs are understood and the software is delivering value.
   * Concentrate on confirming that end-user and stakeholder objectives—not just technical requirements—are satisfied.
3. **Leverage Simplified Tools and Techniques:**

   * Use lightweight approaches to traceability, validation planning, and simulation instead of complex, resource-heavy methods.

---

### **Guidance Specific to Small Projects:**

#### **1. Requirements Validation with Stakeholders**

* **Validate Early and Often:**
  + Schedule quick validation sessions during requirements elicitation or definition.
  + Confirm that requirements are correct, clear, complete, and feasible.
* **Focus on Critical Requirements:**
  + Rank requirements based on criticality (e.g., those impacting safety, hazards, or core functionality).
  + Priority should always be given to validating safety-critical and mission-critical requirements.
* **Utilize Simplicity for Clarity:**
  + Use diagrams, prototypes, or user stories to work with stakeholders and validate understanding of the software’s purpose.
* **Practical Tip for Small Teams:**
  + Create a lightweight **requirements validation checklist** and systematically review requirements with all stakeholders.

---

#### **2. System-Level Validation**

In small projects, resources may prevent thorough validation at every lifecycle stage. Focus your efforts on the **integrated system** rather than isolated components to ensure the software works as a cohesive whole.

##### **Key Steps:**

1. **Validate Core System Interactions and Critical Scenarios:**
   * Test the fully integrated system under key workflows or use cases to confirm it meets actual operational needs.
   * Address critical behaviors, such as:
     + Interaction between subsystems.
     + Data handoffs across interfaces.
     + Budgeted execution timing for operations with deadlines.
     + Proper handling of fault or error conditions.
2. **Use Lightweight Validation Strategies:**
   * **Check system behavior with specific operational scenarios:**
     + Conduct small-scale demonstrations for nominal (expected) and off-nominal (unexpected) scenarios.
   * Leverage basic peer reviews or team walk-throughs to validate system-level workflows during testing.
3. **Focus Validation on Risk and Criticality:**
   * Small projects should explicitly validate any functionality that could result in significant mission failure, safety issues, or cost overruns if it does not work as intended.

##### **Tools to Simplify Validation on Small Projects:**

* Use a **traceability matrix** in a basic spreadsheet rather than a complex tool to align requirements, validation activities, and test results.
* Consider open-source or affordable test automation frameworks (if applicable), such as **JUnit** for Java, **pytest** for Python, or **TestNG**.
* Implement high-priority system integration and critical functionality tests in a series of small, focused sessions.

---

#### **3. Validation on the Target Platform or Simulation**

* **Use the Target Platform (Preferred):**

  + Where possible, validate the software on the actual hardware or deployment environment, even in a scaled-down context.
  + Example:
    - If the target is an embedded system, test it on a “breadboard” version of the hardware.
    - If the target is a web app, deploy to a staging environment that mirrors production.
* **Leverage Simulations When Necessary:**

  + When it is not practical to test in the actual environment (e.g., hardware unavailability, cost), use low-cost, high-fidelity simulations or virtualization.
  + Example:
    - Deploy on a local development machine configured as close as possible to the operational target (use virtual machines to mimic hardware configurations).
* **Focus Simulated Testing on Realistic Scenarios:**

  + Small projects cannot afford exhaustive validation, so concentrate simulated testing on:
    - **Critical Use Cases:** Does the software successfully accomplish the most important goals from the stakeholder perspective?
    - **Failure Scenarios:** Can the software recover from errors safely and reliably?

---

#### **4. User-Created Scenarios**

* **Partner with Users for Validation:**
  + For small projects, user-created validation scenarios are especially valuable and cost-effective.
  + **Example:** Solicit typical workflows or edge cases from stakeholders that represent real-world use.
* **Simplified End-User Testing:**
  + Provide users with prototype builds or deployments to validate functionality directly in operational or simulated environments.
  + Focus on hands-on usability testing to confirm that the system satisfies stakeholder needs as a cohesive solution.

---

#### **5. Safety-Critical and Hazardous Functionality**

Small projects managing safety-critical systems (e.g., Class A software) must validate specific behaviors with additional care despite limited resources:

* **Focus on Safety-Critical Scenarios:**
  + Validate the software’s protection mechanisms against issues like:
    - HR-33: **Inadvertent Operator Action**—Test safeguards to prevent unsafe or unintended operations.
    - Timing-based hazards—Ensure time-critical functions (e.g., fault protection) execute within acceptable thresholds.
* **Perform Targeted Fault Injection Testing:**
  + Simulate failures or hazards within the system to validate the software’s response.
  + Examples: Introduce sensor errors, data corruption, or deliberate faults to test fault tolerance and safety responses.

---

#### **6. Validation Metrics for Small Projects**

Tracking validation progress is important even for small projects, but reporting should remain lightweight:

* **Minimal Metrics to Track:**
  + Percentage of requirements validated to date vs. total requirements.
  + Number of critical scenarios validated successfully.
  + Number of defects identified during validation activities.
  + Regression test results after defect fixes, focusing on impacted areas.
* Use simple tools (e.g., spreadsheets) or visualization dashboards to track and share metrics with stakeholders.

---

### **Small Project Validation Checklist**

Use the following checklist to ensure a simplified yet effective validation process:

1. **Requirements Validation:**

   * Have all requirements been reviewed with stakeholders for completeness, clarity, and feasibility?
   * Are implied and derived requirements explicitly validated (e.g., sequences like "X must occur before Y")?
2. **System-Level Testing:**

   * Has the software been integrated and tested as a fully functioning system?
   * Have critical workflows been validated end-to-end?
3. **Target Platform or Simulation:**

   * Has validation occurred on the actual platform? If not, has a high-fidelity simulated environment been used?
   * Have operational environment constraints been sufficiently simulated?
4. **Safety and Risk:**

   * Have all safety-critical and hazardous functionalities been validated (e.g., HR-33, timing-critical failures, recoverability)?
   * Have off-nominal conditions and failure scenarios been tested?
5. **Stakeholder and Usability Testing:**

   * Have stakeholders been actively engaged in validating user-created scenarios?
   * Has small-scale, hands-on usability testing been conducted?
6. **Metrics:**

   * Have validation activities been tracked using lightweight metrics (e.g., % validated requirements, defect count)?

---

### **Conclusion**

Small projects can achieve effective validation by focusing on critical areas such as stakeholder-driven requirements, system-level behavior, operational scenarios, and safety-critical features. A lightweight and methodical approach to validation—adapted to resource constraints—enables projects to deliver high-quality software that meets stakeholder needs and operational expectations while mitigating key risks. The practicality of user-created scenarios, lightweight simulations, and focused testing provides the best balance between effort and quality for small projects.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-209)

  [IEEE Standard for System, Software, and Hardware Verification, and Validation](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8055462 "Click to open in new window")

  IEEE Computer Society, IEEE Std 1012-2016 (Revision of IEEE Std 1012-2012), Published September 29, 2017,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards. Non-NASA users may purchase the document from: http://standards.ieee.org/findstds/standard/1012-2012.html
* (SWEREF-219)

  [IEEE Standard for Software Reviews and Audits](https://ieeexplore.ieee.org/document/4601584 "Click to open in new window")

  IEEE Std 1028, 2008. IEEE Computer Society, NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-277)

  [Software Formal Inspections Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-87399 "Click to open in new window")

  NASA-STD-8739.9, NASA Office of Safety and Mission Assurance, 2013. Change Date:
  2016-10-07, Change Number: 1
* (SWEREF-405)

  ["Guide to software verification and validation",ESA PSS-05-10,](http://www.esa.int/TEC/Software_engineering_and_standardisation/TECBUCUXBQE_0.html "Click to open in new window")

  Issue 1, Revision 1, ESA Board for Software Standardization and Control, 1995.  FOR SECURITY REASONS, ALL LINKS TO THE ftp.estec.esa.int SERVER ARE DISABLED. YOU MAY REQUEST RELATED DOCUMENTS TO bssc@esa.int
* (SWEREF-539)

  [Aero-Space Technology/X-34 In-Flight Separation from L-1011 Carrier](https://llis.nasa.gov/lesson/1122 "Click to open in new window")

  Public Lessons Learned Entry: 1122.
* (SWEREF-578)

  [Testbed Limitations May Impact End-to-End Flight System Testing](https://llis.nasa.gov/lesson/3716 "Click to open in new window")

  Public Lessons Learned Entry: 3716.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The provided lessons learned underscore the importance of **simulations in validating flight systems and software**, particularly when direct validation on the actual operational platform is infeasible. Below, the lessons are broken down with an emphasis on key insights, their implications for software validation processes, and actionable recommendations based on the scenarios.

---

### **1. Aero-Space Technology/X-34 In-Flight Separation from L-1011 Carrier, Lesson No. 1122**

#### **Key Details:**

* **Challenge:** The X-34 mission was unable to validate flight software directly on the targeted platform (the X-34 spacecraft separating from its L-1011 carrier aircraft). This raised concerns about the reliability of the software in real-world operational conditions.
* **Contributing Factors:**
  + Inability to conduct real-world validation.
  + Concern regarding the **distributed nature of safety functions**, which likely increased the complexity of verifying system interactions and safety-critical requirements spread across development participants.

#### **Key Insights:**

* Lack of validation on the operational platform limited confidence in system performance during critical mission phases (e.g., in-flight separation).
* For systems with **distributed safety functions**, simulations must extend beyond individual system verification to **holistic system and safety interaction validation**.
* System-level concerns are heightened when multiple project participants or contractors are involved, requiring **more robust integration testing** supported by simulations.

#### **Recommendations:**

1. **Develop Comprehensive Simulations:**
   * High-fidelity simulations must account for the full system, including critical safety interactions involving all integrated subsystems.
   * In the case of separation events, simulate:
     + Dynamic interactions between the carrier and the payload.
     + Actuator responses and timing alignment with physical conditions.
     + Potential failures during separation sequences.
2. **Validate Mission Safety Functions:**
   * Specifically validate distributed safety-critical functions using end-to-end simulation to ensure proper coordination and failover mechanisms (e.g., redundancy, fault recovery paths).
3. **Establish Early Validation Alternatives:**
   * If the operational platform is unavailable until late in the project timeline, validate subsets of the software and system behaviors earlier in the process using simulators, prototypes, or hardware-in-the-loop (HIL) testing. This reduces last-minute risks.

---

### **2. Testbed Limitations May Impact End-to-End Flight System Testing, Lesson No. 3716 (Stardust/NExT Spacecraft)**

#### **Key Details:**

* **Challenge:** Software changes made **three weeks before launch** introduced an issue that inhibited redundancy swapping between flight systems. The testbed used to validate the software changes lacked *high fidelity*, leading to undetected issues with critical redundancy functions.
* **Result:** The spacecraft was incapable of switching to its redundant flight string during 11 years of operations. Testing limitations on the simulation testbed directly contributed to risks in long-term mission reliability.

#### **Key Insights:**

* **High-fidelity simulations** are critical for detecting latent failures introduced by late-stage software or system changes. Testing limitations (such as the inability to simulate redundancy switching) leave significant functionality unverified.
* Testing **last-minute changes** via simulation without a fully equipped testbed may provide limited assurance, especially for fault protection or redundancy mechanisms critical to mission success.
* **End-to-end functional validation** in dual-redundant systems requires simulation environments capable of reproducing the full operating state and conditions of the actual spacecraft.
* Poor validation processes at this level impact not just mission-critical operations but also long-term mission success.

#### **Recommendations:**

1. **Prioritize High-Fidelity Features in Testbeds:**
   * Design system testbeds with high-fidelity capabilities to simulate all critical mission functions, including:
     + Fault protection mechanisms.
     + Redundancy switching (e.g., dual or multi-string configurations).
     + Communication subsystems and timing-sensitive operations.
   * Testbeds must model **real-world hardware/software conditions**, not a limited subset of them.
2. **Early Risk Identification for Simulation Limitations:**
   * Projects must **identify fidelity gaps** in the testbed early in the lifecycle and establish mitigation strategies to address limitations for late-stage validation activities. This can involve:
     + Adding high-fidelity modules to the testbed gradually for critical features.
     + Explicitly documenting **validation shortfalls** and using alternative measures (e.g., code review, additional analysis) to account for the gaps.
3. **System-Wide Validation for Last-Minute Changes:**
   * When late-stage software changes are introduced, utilize end-to-end simulations to validate the **cascading effects** of those changes, particularly for critical subsystems like:
     + Fault detection and recovery mechanisms.
     + Redundant or backup operational states.
   * Incorporate a regression test suite that validates not just the software change but its integration with the overall flight system.
4. **Improve Fly-Off Testing When Feasible:**
   * For long-term missions (like Stardust/NExT), test critical fault protection and redundancy directly on **flight hardware** or use HIL setups partially integrated with operational components to identify corner cases.

---

### **3.** Lessons Learned: Class D Budget and Schedule Pressure Leading to Reduced Software Maturity at ATLO

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

### **4.** Lessons Learned: In Class D, Fault Protection Becomes the Safety Net—So It Must Be Excellent

**Problem/Observation:**  
Class D missions accept higher hardware and redundancy risk, which places greater reliance on software‑based fault protection (FP). The Anomaly Review Board (ARB) emphasized that FP must be robust enough to compensate for these elevated risks. For LTB, several FP weaknesses emerged that limited the system’s ability to autonomously protect itself.

**ARB Context:**  
The ARB explicitly stated:  
“On a Class D mission that assumes risk, ensure that the safety net of fault protection can adequately mitigate some of the risks.”

**Contributing Factors:**  
• Incorrect or insufficiently validated FP thresholds.  
• Fault protection logic split across multiple authorities and implementation paths.  
• Sequence‑based safing behaviors and FSW‑based safing behaviors were never tested together end‑to‑end.  
• Missing telemetry limited situational awareness and inhibited on‑orbit diagnosis.  
• Reset behavior and recovery paths were not fully characterized or validated.

**Resulting Impacts:**  
The spacecraft’s ability to safely respond to anomalies was compromised. Fragmented FP design, incomplete testing, and unclear behavior under reset conditions reduced system resilience during off‑nominal events.

**Relevant SWEHB Guidance:**  
Core SWEHB requirements remain applicable even when tailored for Class D:  
• SWE‑057 (Software Architecture) requires the design and documentation of fault management behavior.  
• SWE‑050, SWE‑051, and SWE‑055 require verifiable, traceable FP‑related requirements and logic.  
• SWE‑070 and SWE‑073 require modeling, simulation, and end‑to‑end testing to validate FP behavior under nominal and off‑nominal conditions.

**Lesson Learned:**  
Class D missions rely disproportionately on software fault protection because hardware redundancy is limited. For this reason, FP must be designed, validated, and tested with exceptional rigor. Software fault protection is a mission‑critical system—not an optional enhancement—and must be treated as such from architecture through ATLO and operations.

### **5.** **Lesson Learned (Starliner CFT):** **Integrated modeling and simulation must exercise end‑to‑end behaviors with sufficient fidelity and data capture.**

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

**Recommended Practices (Aligned to SWE‑071/073):**

* Build **scenario libraries** covering nominal, off‑nominal, safing, resets, degraded modes.
* Ensure **telemetry fidelity** (rates, fields, timestamps) supports validation and anomaly reproduction.
* Validate **model fidelity** against flight‑like data; maintain model‑to‑flight delta logs.

**Actionable Checks:**

* Scenario coverage matrices exist and are maintained.
* Telemetry requirements specify minimum sample rates and precision.
* Model validation reports compare against integrated test/flight‑like runs.

### **General Guidance Based on These Lessons Learned**

#### **A. High-Fidelity vs. Low-Fidelity Simulations**

* **Key Distinction:** High-fidelity simulations mimic the exact operational environment (e.g., processor performance, timing, redundancy, and hardware interfaces), while low-fidelity simulations are approximate models of the system.
* High-fidelity simulations are essential for validating:
  + Safety-critical functionality.
  + Timing and sequence-dependent operations (e.g., hardware responses, multi-subsystem coordination).
  + Fault protection and failure recovery systems, especially for redundant architectures.
* Low-fidelity simulations can be used for early validation of high-level functionality but must transition to high fidelity for final validations.

---

#### **B. Recommendations for Simulations:**

1. **Start Testbed Development Early:**

   * Begin building simulation environments in parallel with software and system design. Early prototype testbeds can help identify major validation gaps and provide early-stage feedback.
   * Incrementally improve the simulation environment as the system design matures.
2. **Use Simulations for Fault Protection Validation:**

   * Fault protection systems must be carefully validated in simulations to:
     + Emulate faults and measure system responses.
     + Confirm fallback mechanisms under nominal and stress conditions (e.g., thermal extremes, power interruptions).
   * Example Scenarios:
     + Sensor failures or incorrect readings.
     + Software-triggered redundancy switching under detected anomalies.
     + Successful fault recovery and failsafe operations.
3. **Ensure End-to-End Validation:**

   * Break complex systems validation into **logical segments** but conduct **end-to-end testing** before the mission-critical milestone (e.g., integration, deployment, or launch).
   * End-to-end validation must include:
     + Complete interface testing across subsystems.
     + Verification of operational workflows (e.g., command sequences, routine switching).
4. **Simulate Sequences and Timing of Events:**

   * Simulations should model event-driven systems with explicit time delays to reflect real-world execution:
     + Timing between activations and responses.
     + Synchronized or asynchronous fault detection on redundant systems.
5. **Mitigate Testbed Limitations:**

   * If your testbed lacks fidelity in certain areas:
     + Document the limitation explicitly.
     + Cross-validate testbed results with hardware prototypes, targeted platform tests, or analytical models.
     + Inform stakeholders of risks and validation constraints.

---

#### **C. Lessons Learned Applied to Small and Large Projects**

* **For Small Projects:**
  + Use targeted simulations to address safety-critical areas.
  + If high-fidelity testbeds are not feasible, focus resources on validating critical subsystems and document areas left unverified.
* **For Large and Complex Systems:**
  + Acknowledge the risks of incomplete simulations for distributed systems and redundancy mechanisms.
  + Invest in high-fidelity testbeds to assure accurate integration results for long-duration projects.

---

### **Conclusion**

The lessons from the X-34 and Stardust/NExT missions highlight critical gaps in simulation-based validation and emphasize the need for high-fidelity, end-to-end simulation environments. By focusing on early planning, comprehensive testbed development, validation of fault protection mechanisms, and addressing simulation limitations, future projects can safeguard system reliability, even in scenarios where direct system testing is infeasible. These lessons also reinforce the importance of recognizing simulation limitations as risks and addressing them systematically.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [High fidelity simulation systems are centrally important in test efforts](https://software.gsfc.nasa.gov/lesson-details/3/). **Lesson Number 3**: The recommendation states: "High fidelity simulation systems are centrally important in test efforts."
* [Test, test, and re-test, and "test as you fly"](https://software.gsfc.nasa.gov/lesson-details/4/).**Lesson Number 4**: The recommendation states: "Test, test, and re-test, and "test as you fly" are keys to successful development."
* [Evaluate new software along the full range of operational scenarios](https://software.gsfc.nasa.gov/lesson-details/91/). **Lesson Number 91**: The recommendation states: "Evaluate new software along the full range of operational scenarios."
* [Simulations/rehearsals with the SC and execute re cover prior to launch](https://software.gsfc.nasa.gov/lesson-details/94/). **Lesson Number 94**: The recommendation states: "Execute simulations/rehearsals with the SC where EEPROM is loaded (to all available processors/banks of EEPROM) and execute recovery prior to launch."
* ["Day in the Life" simulations using automation prior to launch](https://software.gsfc.nasa.gov/lesson-details/99/).**Lesson Number 99**: The recommendation states: "Execute "Day in the Life" simulations using automation prior to launch."
* [Impacts caused by interfaces that are not tested pre-launch](https://software.gsfc.nasa.gov/lesson-details/124/).**Lesson Number 124**: The recommendation states: "Develop mitigations for impacts caused by interfaces that are not tested pre-launch."
* [Perform pre-launch end-to-end testing between the spacecraft and all primary primary ground stations](https://software.gsfc.nasa.gov/lesson-details/126/).**Lesson Number 126**: The recommendation states: "Perform pre-launch end-to-end testing between the spacecraft and all primary primary ground stations."
* [Assumptions for both over- and under-allocated RF Link margins](https://software.gsfc.nasa.gov/lesson-details/127/).**Lesson Number 127**: The recommendation states: "Examine and rationalize assumptions for both over- and under-allocated RF Link margins."
* [Essential to have Hi-Fidelity FlatSat](https://software.gsfc.nasa.gov/lesson-details/131/). **Lesson Number 131**: The recommendation states: "It is essential to have Hi-Fidelity FlatSat."
* [If ground systems are not available, a dedicated test needs to be performed](https://software.gsfc.nasa.gov/lesson-details/144/).**Lesson Number 144**: The recommendation states: "Maintaining spacecraft schedule is critical: if ground systems are not available, a dedicated test needs to be performed."
* [Loading analysis for station usage includes contingency scenarios](https://software.gsfc.nasa.gov/lesson-details/163/). **Lesson Number 163**: The recommendation states: "Ensure loading analysis for station usage includes contingency scenarios (e.g., loss of a ground station for 1 pass, or 1 day, or 1 week)."
* [End-to-End Testing through satellite I&T](https://software.gsfc.nasa.gov/lesson-details/172/).**Lesson Number 172**: The recommendation states: "End-to-End Testing should be planned for smaller events spread out through satellite (i.e., spacecraft with integrated payload/science instruments) I&T."
* [Software Requirement Sell-Off Expedience](https://software.gsfc.nasa.gov/lesson-details/177/).**Lesson Number 177**: The recommendation states: "As early as feasible in the program (EPR-CDR time frame) ensure that the project will be provided with all relevant test articles well in advance of the test’s run-for-record (will likely require NASA Program Management buy-in as well). This will allow the time necessary for: review of requirement test coverage, accumulation of all comments (especially if IV&V are supporting the program), and vendor disposition of all comments to project satisfaction. In this manner, when test artifacts from the FQT run-for-record are provided for requirement sell-off, the Flight Software SME will have a high level of confidence in the artifacts provided (knowing how each requirement has been tested) to expedite the sign-off process. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
* [Key Mission Ops Tests essential to timely V&V of flight design/mission ops concept& launch readiness](https://software.gsfc.nasa.gov/lesson-details/342/).**Lesson Number 342**: The recommendation states: "Develop/iterate/execute system level tests to verify/validate data system/mission Concept of Operations during Observatory I&T (e.g., the Comprehensive Performance Test (CPT) and Day-in-the-Life (DiTL) test). The CPT should be: a) thorough (exercising all copper paths, as many key data paths as reasonable, and using operational procedures); b) executed prior to/post significant events throughout Spacecraft & Observatory I&T; and c) designed comprehensive, yet short enough to be executed multiple times (e.g., the PACE CPT was specifically designed to be 4-5 days). The multi-pass DiTL test can demonstrate nominal operational procedures/processes and, when executed prior to the pre-environmental CPT, can be the basis for the instrument functionals during the environmental cycles and post environmental functional checkouts of the instruments."

# 7. Software Assurance

**SWE-073 - Platform or Hi-Fidelity Simulations**

4.5.8 The project manager shall validate the software system on the targeted platform or high-fidelity simulation.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project validates the software components on the targeted platform or a high-fidelity simulation.

## 7.2 Software Assurance Products

For this requirement, the following Software Assurance (SA) deliverables should be developed and reviewed to ensure that the validation activities meet the mission objectives and are conducted with sufficient rigor and traceability:

1. **Validation Analysis:**

   * Document that the validation strategy includes testing on either the targeted platform or a high-fidelity simulation.
   * Provide an **analysis of simulator fidelity**, including its limitations and risks.
2. **Software Test Procedures:**

   * Ensure procedures for validation testing clearly describe the configurations and steps for testing on the target platform or simulator.
   * Include specific procedures for verifying:
     + Interfaces to hardware.
     + Timing-sensitive operations.
     + Behaviors under fault conditions.
3. **Software Test Plan:**

   * Ensure the test plan includes scenarios covering operational workflows in both nominal and off-nominal conditions.
   * The test plan should identify testing constraints due to simulation limitations (if applicable) and mitigation strategies.
4. **Software Test Reports:**

   * Capture detailed outcomes of validation testing. This should include:
     + Results from validation on the actual platform (if used).
     + Simulated test results, including comparisons to expected outcomes and any identified gaps.
     + Coverage of requirements validated successfully, requirements left unverified, and defect findings.
     + Risk analysis of the simulator-based testing.
5. **Simulator Validation Report (if simulation is used):**

   * Document validation that the **high-fidelity simulation itself is accurate**, replicating the functionality, hardware characteristics, and environmental conditions of the targeted platform. This report should include:
     + Any mismatches or discrepancies between the simulator and the actual platform.
     + Impacts of simulator limitations on the quality or completeness of validation results.

---

## 7.3 Metrics

Tracking relevant metrics enables systematic identification of risks, progress, and effectiveness of the validation activities.

1. **Planned vs. Released Components:** Track the number of components (e.g., modules, routines, subsystems) planned versus those released into each build. This metric should inform whether validation testing on the integrated build is sufficiently scoped.
2. **Validation Coverage Metrics:**

   * **Percentage of Requirements Validated:**
     + Total # of validated requirements versus the total requirements for each build (focus on functional, safety-critical, performance-related requirements).
   * **Platform Validation Coverage:**
     + Percentage of requirements validated using the actual target environment.
     + Percentage of requirements validated exclusively in high-fidelity simulation and associated risks.
   * **Interface Coverage:**
     + Percentage of internal and external system interfaces tested successfully in the operational environment or simulation.
3. **Defect Metrics:**

   * **Defects Identified:** Track the number of defects discovered during validation testing and classify them (critical, non-critical).
   * **Defects Found in Simulation vs. Real Platform:** Analyze whether defects are surfacing differently due to simulation fidelity gaps.
4. **Risk Metrics:**

   * Capture the number of risks identified related to simulator fidelity.
   * Risk reduction percentage (planned mitigations versus mitigations implemented) regarding simulation limitations.

**Reference:** For additional metrics and examples, see **Topic 8.18–SA Suggested Metrics.**

---

## 7.4 Guidance

#### **General Steps for Assurance of Validation Activities**

1. **Confirm Validation Environment:**

   * Validate that the software system is tested either on the:
     + **Target operational platform** under realistic conditions.
     + **High-fidelity simulation** replicating the characteristics and constraints of the operational environment.
   * Ensure that the test environment meets mission requirements, capturing the **real-world performance and system behaviors.**
2. **Assess Simulator Fidelity:**

   * Confirm whether the simulation replicates hardware configuration, timing details, operational interfaces, and real-world conditions with sufficient accuracy.
   * Identify **any fidelity gaps** in the simulation that could impact validation, including:
     + Missing interface support for specific hardware or subsystems.
     + Unrealistic environmental inputs (e.g., incorrect sensor or actuator responses).
     + Inability to reproduce simultaneous real-world constraints (e.g., thermal, radiation, or dynamic loads).
3. **Identify and Document Risks:**

   * Capture risks associated with using simulations instead of the target environment.
   * Specific focus areas should include:
     + **Boundary Conditions Not Replicated:** Scenarios involving edge cases that might expose flaws only in the real-world environment.
     + **Critical Interfaces:** Interfaces between hardware and software that cannot be fully validated under simulation conditions.
     + **Timing-sensitive Operations:** Operations that rely on real-world synchronization and concurrency that may be simplified in simulations.
     + **Environmental Inputs:** Gaps in environmental emulation (e.g., operating temperature, vibrations, radiation effects, signal interference).
   * Ensure risk documentation includes mitigation strategies before deployment (e.g., testing fallback mechanisms, introducing validation for simulation assumptions).
4. **Mitigation Strategies for Simulation Risks:**

   * Recommend additional efforts in areas where simulator fidelity is lacking:
     + **Regression Testing Later on Hardware:** Plan testing directly on the operational platform once available.
     + **Hardware-in-the-Loop (HIL):** Use physical hardware interfaced with simulation as part of testing to increase fidelity.
     + **Alternative Tools:** Supplement simulation testing with detailed code inspections, data analysis, and manual walkthroughs to validate untestable scenarios.
   * Document **assumptions** in simulator-based validation (e.g., expected interface behaviors or timing approximations) and explicitly test them on the actual hardware when feasible.
5. **Cross-Validate Simulation Tools:**

   * Ensure the simulation testbed itself has been validated:
     + Have tools been calibrated or benchmarked against known system behaviors from prior missions or laboratory setups?
     + Are the simulator outputs consistent with platform-level expectations?

#### **Safety-Critical Validation Guidance**

For systems involving **safety-critical functionality**, risks related to simulation fidelity need to be rigorously evaluated. Software assurance activities should focus on:

1. **Fault Injection Testing:**
   * Simulate failure modes (e.g., hardware malfunctions, erroneous sensor inputs) and validate the software responses under load.
2. **Redundancy Testing:**
   * If dual strings or failover systems are required, ensure redundancy mechanisms are validated even in simulation (e.g., switching between redundant flight software systems in the Stardust/NExT Lesson).
3. **Operator Safety Scenarios:** Validate safeguards for HR-33 (**Inadvertent Operator Action**) and other hazardous functions using realistic input.

---

### **Additional Assurance Considerations**

#### **1. Focus on Subsystem Validation:**

Even for small projects, validate critical **subsystems** independently (e.g., navigation, telemetry handling, fault protection) if the full platform or system simulation experiences fidelity issues. Testing smaller subsystems in isolated environments can help reduce risks before integration testing.

#### **2. Traceability Validation for Critical Scenarios:**

* Ensure testing scenarios **map directly to requirements** (positive tests, stress tests, and fault tests).
* Confirm safety-critical requirements are validated explicitly in validation reports.

#### **3. Stakeholder Collaboration:**

* **Engage domain experts** (hardware designers, users, operational engineers) to confirm that high-fidelity simulation outputs align with their expectations.

---

### **Conclusion**

Software assurance activities for validation require robust oversight, particularly when high-fidelity simulation testbeds replace direct testing on the operational platform. By ensuring traceability, identifying risks, and cross-checking simulation fidelity, assurance personnel can proactively safeguard system validation quality. Validation plans, procedures, and reports must account for simulator limitations and define mitigation strategies, addressing potential unverified functionality before deployment. Safety-critical features demand additional scrutiny to reduce operational hazards and meet system reliability targets.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical in assessing whether a project's validation efforts sufficiently demonstrate that the software meets its intended purpose and operates correctly in its target environment. For Requirement 3.1, objective evidence ensures that:

1. Validation activities are executed as intended.
2. Results align with requirements and stakeholder expectations.
3. Risks, limitations, and gaps are identified and mitigated.

Below is a detailed list of **objective evidence artifacts** that can be submitted and reviewed to comply with this requirement.

---

### **1. Validation Plans and Strategies**

**Artifacts:**

* **Software Validation Plan (SVP):**

  + Describes the tasks, activities, and methodologies for validation.
  + Specifies whether validation is done on the actual hardware (target platform) or on a high-fidelity simulation.
  + Includes:
    - Scenarios planned for testing.
    - Procedures for validating system-level requirements (e.g., functional, safety-critical, performance-related).
    - Risk mitigation strategies for simulation-based testing.
  + **Objective Evidence:** The plan itself provides a roadmap showing how software validation ensures system reliability.
* **Simulation Validation Strategy:**

  + A document outlining how the fidelity of the simulation will be established, including details on the environment configuration, interfaces, timing accuracy, hardware emulation, and boundary condition replication.
  + Addresses configuration control for simulator changes throughout the lifecycle.

---

### **2. Validation Test Artifacts**

**Artifacts:**

* **Test Procedures and Test Scripts:**

  + Written steps or automated scripts used to execute validation tests, including:
    - Target platform tests.
    - High-fidelity simulation tests.
    - Procedures for safety-critical tests (e.g., failover, redundancy).
  + Links to specific system requirements for traceability.
* **Validation Test Cases:**

  + Descriptions of test cases based on real-world scenarios and operational needs—both nominal and off-nominal.
  + Include traceability to design requirements, hazard reports, and safety analyses.
* **End-to-End Test Descriptions:**

  + Definition of end-to-end system workflows and scenarios that validate the system holistically.
  + Objective evidence includes detailed descriptions of how these tests cover:
    - Software functionality across integrated subsystems.
    - Interfaces between components.
    - Timing and environmental conditions.

---

### **3. Validation Test Execution Logs and Reports**

**Artifacts:**

* **Validation Test Reports:**

  + Output reports detailing the execution of test cases, including:
    - Results (pass, fail, or inconclusive).
    - Descriptions of test results ensuring coverage of requirements.
    - A summary of testing completed on the target platform versus simulation.
    - Description of any discrepancies between expected and actual results, with mitigation plans if applicable.
    - Regression test results ensuring changes don't introduce defects.
  + **Objective Evidence:** Provides raw data or summaries demonstrating validation success rates and identified issues.
* **Test Logs and Test Results:**

  + Logs generated during test execution that provide evidence of compliance, including:
    - Time-stamped records showing when tests were run and their outcomes.
    - Inputs, outputs, and success/failure metrics.
* **Simulation Test Logs:**

  + Evidence documenting that validation was conducted in a high-fidelity simulation, with details of:
    - Configurations tested.
    - Inputs (realistic or simulated) and expected outcomes.
    - Fault protection or recovery scenarios tested.
* **Re-execution Reports for Issue Fixes:**

  + Evidence showing that test failures were analyzed, fixes were applied, and validation tests were reexecuted with passing results.

---

### **4. Analysis and Risk Artifacts**

**Artifacts:**

* **Simulation Validation Analysis:**

  + Detailed analysis of the **capabilities and limitations** of the simulator, including:
    - Hardware and interface fidelity.
    - Specific behaviors it can or cannot replicate.
    - Analysis of timing accuracy, environmental conditions, fault injection capabilities, etc.
  + Identified validation constraints and mitigations explicitly documented.
* **Platform vs. Simulation Risk Assessment:**

  + Detailed assessment identifying risks associated with using simulation instead of the target platform, including:
    - Scenarios that cannot be tested on the simulator.
    - Gaps in simulator replication (e.g., timing, interface accuracy).
    - Probability and impact of identified risks.
* **Requirements and Coverage Matrix:**

  + A traceability matrix mapping system requirements to the validation tests performed on both the target platform and simulation.
  + Evidence that all functional, performance, and safety-critical requirements are validated and coverage gaps are documented.

---

### **5. Stakeholder and Peer Review Documents**

**Artifacts:**

* **Validation Review Records:**

  + Minutes or notes from peer reviews, design reviews, or validation-specific reviews.
  + Evidence that stakeholders and project participants reviewed and accepted validation results and associated risks.
* **Stakeholder Feedback and Approval:**

  + Records of stakeholder feedback confirming the validation results align with their expectations (e.g., user-acceptance criteria or feedback in validation demonstration sessions).

---

### **6. Simulator Validation Evidence (If Applicable)**

**Artifacts:**

* **Simulator Qualification Report:**

  + Evidence demonstrating that the simulation testbed:
    - Accurately emulates hardware interfaces and environmental conditions.
    - Has been calibrated/validated against historical data, real system data, or characterized hardware behaviors.
* **Comparison of Actual vs. Simulated Results:**

  + Reports comparing outcomes from the simulator with results from the operational platform (if available) to validate simulator fidelity.
* **Simulator Change Records:**

  + Evidence that the simulation environment has been maintained under configuration control (e.g., logs of changes to simulation software or hardware over time).

---

### **7. Defect and Issue Tracking Artifacts**

**Artifacts:**

* **Defect Reports:**
  + Records of defects identified during validation testing, with full descriptions and analysis of the software's improper behavior.
* **Defect Correction Evidence:**
  + Documentation showing corrected issues were successfully retested and confirmed as resolved.
* **Unresolved Issue Risk Assessment:**
  + For any defects left unresolved due to simulation limitations, risk assessments documenting the likelihood and impact, including justifications for deferring resolution.

---

### **8. Safety and Fault Protection Evidence**

**Artifacts:**

* **Fault Injection Test Evidence:**
  + Reports and outputs from tests designed to simulate failure modes (e.g., device communication failures, sensor faults) and verify the software's fault protection behaviors.
* **Redundancy and Failover Validation:**
  + Evidence showing redundancy mechanisms operate as intended under failure conditions, whether tested on the platform or simulated.
* **HR-33 Validation (For Safety):**
  + Evidence confirming safeguards against inadvertent operator actions (e.g., redundant controls, “Are you sure?” dialogs) were validated.

---

### **9. Lessons Learned and Process Improvement Evidence**

**Artifacts:**

* **Lessons Learned Reports:**

  + Records documenting insights gained during validation activities, particularly limitations or gaps in simulation testing, risks addressed, and proposed improvements for future projects.
* **Simulation Improvement Recommendations:**

  + Suggested upgrades, enhancements, or alternative strategies for increasing simulator fidelity or addressing systemic risks in validation practices.

---

### **Conclusion**

Objective evidence is essential to demonstrate compliance with validation requirements, providing transparency, traceability, and confidence in the testing process. Artifacts such as validation test reports, simulator qualifications, risk assessments, and traceability matrices directly substantiate that the system has been thoroughly validated against its requirements. Properly maintaining and reviewing this evidence ensures that all stakeholders can trust the quality and reliability of the software system.

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
