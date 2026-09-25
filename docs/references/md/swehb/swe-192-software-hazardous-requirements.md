# SWE-192 - Software Hazardous Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695527. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements

SWE-192 - Software Hazardous Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695527)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695527&showCommentArea=true&showComments=true#addcomment)

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

4.5.12 The project manager shall verify through test the software requirements that trace to a hazardous event, cause, or mitigation technique.

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-192 History

SWE-192 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.5.12 The project manager shall verify through test the software requirements that trace to a hazardous event, cause, or mitigation technique. |
| Difference between C and D | No change |
| D | 4.5.12 The project manager shall verify through test the software requirements that trace to a hazardous event, cause, or mitigation technique. |

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

Verify by the test that any safety features related to system hazards, fault trees, or FMEA events are reliable and work as planned.

Hazard-related software requirements are directly tied to the system’s ability to operate safely in environments with potential risks. These requirements include functionality that either prevents, mitigates, or responds to hazardous conditions triggered by software, hardware, or external environmental factors. The verification of such requirements through testing is critical to ensuring the mission’s safety and success. Below is the rationale for this requirement:

---

### **1. Ensuring the System Can Address Hazards**

* **Hazards and Their Impact:**  
  Hazardous events occur when a system behaves in a way that creates significant safety, operational, or mission risks. For example:
  + A malfunction in an autonomous vehicle software might lead to navigation into unsafe terrain.
  + Spacecraft software may fail to prevent overheating or overloading hardware.
* **Requirement Verification to Ensure Safety:**  
  Software requirements that trace to such hazards define the system’s behavior to either prevent the hazard or mitigate its outcome, such as:
  + Shutdown mechanisms for unsafe operating conditions.
  + Warning systems that alert operators of hazardous states.
  + Autonomy modes that safely manage the system under failure conditions.
* Testing verifies that these requirements effectively prevent or mitigate hazards in operational environments.

---

### **2. Validation of Hazard Mitigation Techniques**

* Verification through testing ensures that hazard mitigation strategies embedded in the software function as intended under realistic scenarios. For example:
  + A fault-detection algorithm is designed to detect and isolate hardware faults to prevent hazards.
  + Safety-critical control functions like automatic shutdown, fallback modes, or deliberate "safe states" must be tested to confirm their implementation.
* Testing these functionalities under controlled but realistic hazardous conditions validates the effectiveness of the embedded mitigation techniques.

---

### **3. Risk Reduction for Mission and Personnel**

* **Critical Role of Software in Safety-Critical Systems:**  
  In modern systems, software is often the primary mechanism for many safety-critical functions, such as detecting hazards, initiating contingencies, and mitigating risks. Failures in these functions can result in:
  + Loss of mission.
  + Damage to hardware or external infrastructure.
  + Injury or risk to personnel.  
    Testing hazard-related requirements reduces the risk of such failures and ensures that the verified system meets safety standards.
* **Failure Consequences:**  
  A failure to identify and mitigate potential hazards can lead to catastrophic consequences if software errors, design flaws, or integration issues remain undetected.

---

### **4. Help Identify Software Contribution to Hazards**

* **Software Contribution to Hazards:**  
  Software can contribute to hazardous conditions in multiple ways:

  + **Incorrect Inputs**: The software fails to read or interpret sensor data accurately, leading to incorrect decisions.
  + **Timing Errors**: Missed deadlines or asynchronous events can result in uncoordinated actions across systems.
  + **Incorrect Logic**: Design flaws in algorithms may cause unsafe decisions.
  + **Failure to Act**: The software fails to execute hazard mitigation routines or does so incorrectly.  
    Testing hazard-related requirements allows defects that may initiate or contribute to hazardous conditions to be uncovered and resolved.
* **Dynamic and Edge-Case Scenarios:**  
  Testing enables the evaluation of the system’s ability to handle hazards under operational dynamics, edge cases, and unexpected conditions, which are often difficult to predict during design.

---

### **5. Compliance with Safety Standards and Protocols**

* **Alignment with Safety Engineering Best Practices:**  
  Verifying hazard-related software requirements through testing aligns with industry standards such as:
  + **NASA’s Software Safety Standard (NASA-STD-8739.8):** Requires that risk reduction and hazard control mechanisms in software be confirmed through testing.
  + **Military and Aerospace Standards (MIL-STD-882E):** Emphasizes that hazard mitigations must be verified.
  + Other standards like **ISO 26262** (functional safety for automotive) and **DO-178C** (aerospace software guidance) similarly require rigorous testing for software that prevents or mitigates hazards.
* Compliance with these standards ensures that the system meets regulatory and mission-critical safety requirements.

---

### **6. Traceability and Requirement Validation**

* **Requirement Traceability:**  
  Testing hazard-related software requirements ensures complete traceability between:

  + Identified hazards or hazardous events.
  + The software requirements designed to prevent, mitigate, or resolve those hazards.
  + The test cases developed to verify those software requirements.  
    Traceability ensures that all hazards identified in the **hazard analysis process** are addressed by corresponding test cases and verified before the system operates in its intended environment.
* **Accountability for Hazard Control Mechanisms:**  
  Testing ties the requirement back to the documented hazard causal chain (cause → hazard → consequence), verifying the adequacy of hazard control techniques.

---

### **7. Verification vs. Validation**

* **Verification Ensures "Built Correctly":**  
  Hazard-related requirement testing confirms that the software was implemented according to the design specifications and matches anticipated functionality. Examples include:
  + Confirming the software attempts to shut down critical systems when instructed to.
  + Ensuring alarms are triggered at appropriate threshold levels.
* **Validation Ensures "Correct System":**  
  Verification testing can also address aspects of validation by confirming that the final integrated system behaves consistently with operational needs related to hazard control.

---

### **8. Confidence in Decision Making**

* Testing hazard-related software requirements provides project managers, teams, and stakeholders with evidence that:
  + Hazard-related risks are effectively mitigated by the software.
  + The software will operate safely under both normal and abnormal conditions.
  + Hazard requirements testing is complete and robust.

Confidence ensures that the software is ready for integration into live systems and operation in hazardous environments.

---

### **Examples of Hazard-Related Requirement Testing**

* Testing the software’s response to an overheating condition:
  + Requirement: System reduces power output when temperature exceeds a threshold.
  + Hazard Testing: Simulate high temperatures and verify power reducers.
* Validation of alarm detection:
  + Requirement: Alert operator when oxygen pressure falls below threshold.
  + Hazard Testing: Simulate low oxygen conditions and confirm system alert.
* Testing redundancy mechanisms for safety-critical systems:
  + Requirement: In the event of subsystem failure, software reroutes operations to redundant subsystems.
  + Hazard Testing: Simulate subsystem failure in test environments.

---

### **Conclusion**

Testing software requirements that trace to hazardous events ensures the mitigations, controls, and safeguards function as intended under operational conditions. It reduces the risk of catastrophic consequences, validates system safety, and provides confidence that the software will operate safely and effectively in its intended role. This requirement directly supports NASA’s objective to protect mission assets, personnel, and overall success.

# 3. Guidance

Software testing is **essential** to demonstrate that software functions are reliable and perform as expected, particularly for safety-critical software requirements. These requirements link to hazardous events, causes, or mitigation techniques, and their verification ensures:

* **Safety**: Reliable operation in hazardous circumstances to protect human life, critical assets, and mission success.
* **Compliance**: Alignment with safety standards and regulations, including those derived from systems such as Fault Tree Analysis (FTA), Failure Modes and Effects Analysis (FMEA), Preliminary Hazard Analysis (PHA), and subsystem hazard analyses.
* **Mission Success**: Prevention of system or mission failures stemming from improperly implemented or untested hazard-related software.

Testing confirms that such safety features operate correctly under nominal and off-nominal conditions.

---

### **Key Guidance for Testing Hazard-Related Software**

#### **1. Testing as the Primary Verification Method**

* Verification for safety-critical software requirements must be performed **through testing** rather than relying solely on analysis, demonstration, or inspection. Testing is the most robust way to verify:
  + **Controls**: Software mechanisms designed to prevent hazards.
  + **Inhibits**: Safety mechanisms that block unwanted actions.
  + **Mitigations**: Software responses designed to reduce the severity of hazard consequences.
* This testing ensures software operates as intended in **realistic and edge-case scenarios** that cannot be fully predicted by analysis alone.

#### **2. Test Case Development for Safety-Critical Functions**

* Test cases for safety-critical software must be derived from:
  + System safety analyses, such as PHA, FMEA, and FTA.
  + Hazard control documentation, which defines the safety strategies the software must adhere to.
  + Requirements traceability matrices, ensuring complete coverage of all hazard-related functionality.
* Test cases need to address:
  + **Nominal Scenarios**: Normal operating conditions.
  + **Abnormal Scenarios**: Situations such as incorrect operator commands, invalid inputs, or hardware failures.
  + **Off-Nominal Scenarios**: Extreme or unexpected events beyond typical operational thresholds.

#### **3. Configuration Management of Test Artifacts**

* Test procedures, test software, test hardware, and results must be placed under **configuration management** to ensure:
  + Traceability between hazard-related requirements, software design, and test artifacts.
  + Accurate documentation of test conditions and outcomes for repeatability and auditability.

#### **4. Code Coverage for Safety-Critical Software**

* **Modified Condition/Decision Coverage (MC/DC)**: This stringent criterion must be applied for safety-critical software to verify every decision, path, and condition is tested.
* Code coverage goals:
  + Strive for **100% code coverage** of all safety-critical software components.
  + Identify and address untested paths or "dead code" to ensure no orphaned software exists within the hazard mitigation functions.
* Challenges in achieving 100%:
  + When test cases cannot address hardware-specific failures (e.g., radiation effects), justify gaps in code coverage and attempt to mitigate through simulations or fault injection.

#### **5. Testing Hazard Controls and Mitigation Techniques**

All hazard-related software features must be tested under **realistic operational conditions** to ensure reliability. Key elements include:

* **Comprehensive Scenarios**: Include edge cases and abnormal inputs to validate that safety-critical software can manage unexpected scenarios.
  + See also **Topic 8.01 - Off-Nominal Testing.**
* **Failure Detection, Isolation, and Recovery (FDIR)**:
  + Validate that the software detects faults promptly and prevents escalation into system-wide failures.
  + Verify recovery mechanisms designed to bring the system into a known safe state during hazardous conditions.
* Test both:
  + **Software Failures** (e.g., incorrect fault detection algorithms, race conditions).
  + **Hardware Failures** that software is expected to mitigate (e.g., redundant sensor overrides).

#### **6. Failure Modes and Effects Analysis (FMEA)**

* Testing should include scenarios derived from **FMEA** and ensure:
  + All failure modes identified in system safety analyses are reproduced in the test environment as realistically as possible.
  + Safety-critical software responds as intended to detect and mitigate those failure modes.
* See also **Topic 8.05 - SW Failure Modes and Effects Analysis.**

#### **7. Testing Hazardous Commands and Fault Trees**

* Use fault tree models to define critical failure scenarios.
* Test safeguards preventing execution of hazardous commands, particularly under:
  + Inadvertent operator actions.
    - See **HR-33 - Inadvertent Operator Action.**
  + Faulty or corrupted data inputs.
  + Concurrency and timing issues in fault detection routines.

#### **8. Testing for Traceability to Requirements**

* Every test case must map to one or more software requirements, particularly those traced to hazards. The **bidirectional traceability** ensures:
  + All hazard-related requirements have corresponding test cases.
  + All testing ties back to specific system safety goals.

#### **9. Validating Code Coverage and Test Completeness**

* Use **code coverage tools** to confirm all decision paths and logic within the software are executed during testing. These tools support:
  + Identification of incomplete test cases.
  + Discovery of orphaned or dead code, which is a potential source of risk in hazard-critical systems (e.g., paths that are inactive but pose risks if inadvertently triggered).

#### **10. Regression Testing for Safety Requirements**

* After any code or system changes, **regression testing** ensures that hazardous functions are not negatively impacted by new defects:
  + Verify that all safety-critical software still meets safety requirements after modifications.
  + Focus on safety controls, inhibits, and mitigations that are related to hazards.

---

### **Special Considerations**

#### **1. Independent Verification and Validation (IV&V)**

* Wherever possible, test safety-critical software with teams that are independent of the original developers. Independent testing increases confidence by identifying issues developers might overlook.

#### **2. Testing in Safe and Simulated Environments**

* Hazardous commands or fault conditions should first be tested:
  + In a simulated environment to mitigate risks to hardware, personnel, or other operational systems.
  + Through dry-runs, fault injection, and system-level simulations prior to integrated testing on actual hardware.

#### **3. Testing Commercial-Off-The-Shelf (COTS) Software Safety**

* Verify that any COTS software used for safety-critical functions operates as expected within the integrated system. Add compensating safety measures if behavior is inconsistent or unreliable.

---

### **Best Practices for Testing Hazard-Linked Software**

1. **Plan Early**:
   * Develop a **Test Plan** early in the project lifecycle (See **SWE-065**).
   * Include a verification matrix linking safety-critical requirements to test cases.
2. **Validate Test Completeness**:
   * Confirm 100% requirement coverage and pursue 100% code coverage of all safety-critical functions.
3. **Use Fault Injection Techniques**:
   * Introduce failures (e.g., hardware or environmental) to evaluate the software’s robustness and response mechanisms.
4. **Continuous Process Improvement**:
   * Record all test results, analyze failed tests, and use lessons learned to refine testing efforts.

---

### **Conclusion**

Testing safety-critical software requirements linked to hazardous events, causes, or mitigation techniques ensures the software performs as intended and mitigates risks to an acceptable level. The combination of robust planning, comprehensive test execution, and strict adherence to code coverage metrics equips software engineers with tools and methods to ensure mission safety and success. By verifying these requirements under nominal, abnormal, and off-nominal conditions, projects can mitigate hazards and build confidence in the reliability of their software systems.

See also Topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis),

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing). 

See also [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements). 

Code Coverage should be 100% for all safety-critical software functions or components. See also [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage).

See also [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior).

See also [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results), [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures).

See [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action), 

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)       * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

## 3.7 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

# 4. Small Projects

For small projects, where resources, personnel, and budget may be limited, testing safety-critical software requirements that address hazards requires a focused and streamlined approach. Below is tailored guidance for **small projects** to ensure compliance with this crucial requirement without unnecessary complexity.

---

### **1. Understand the Scope of Safety-Critical Software**

* Identify **safety-critical software requirements** traced to hazardous events, causes, or mitigation techniques:
  + Use system safety analyses (e.g., Preliminary Hazard Analysis (PHA), Failure Modes and Effects Analysis (FMEA)) to identify hazard-related software.
  + Focus only on software that directly:
    - Prevents hazards (e.g., inhibiting commands leading to collisions).
    - Mitigates hazards (e.g., activating alarms when thresholds are breached).
    - Manages fault detection, isolation, and recovery (FDIR).

#### **Tips for Small Projects:**

* Collaborate with the system engineer and safety team to prioritize **critical areas**—those with the biggest potential impact on safety.
* Limit the scope to high-risk hazards and avoid overcomplicating the analysis.

---

### **2. Plan Simple but Comprehensive Tests**

* Develop a small **Software Test Plan (STP)** that describes:
  + The identified safety-critical software functionalities.
  + How each safety-critical function will be tested.
  + Scenarios for both nominal and abnormal (off-nominal) conditions.
* **Include key elements:**
  + Nominal tests: Verify the software behaves correctly under standard conditions.
  + Off-nominal tests: Verify the software detects, mitigates, or recovers from failures or potential hazards.
  + Edge-case tests: Simulate extreme or rare inputs to confirm robust performance under unexpected conditions.

#### **Tips for Small Projects:**

* Use **test case templates** to streamline documentation (e.g., inputs, expected outputs, results).
* Reuse existing test cases if similar hazards or functionalities exist across components.
* Avoid writing unnecessarily complex scenarios—focus on **operationally relevant situations**.

---

### **3. Streamline Hazard Testing**

* Develop simple test cases for hazard-related functionality:
  + Hazard **controls**: Verify the software prevents unsafe conditions from occurring (e.g., inhibit accidental shutoffs).
  + Hazard **mitigations**: Validate that the software takes appropriate actions after a hazard is detected (e.g., initiate emergency stop sequences).
  + **Safe states**: Test the software’s ability to drive the system to a safe, idle, or shutdown state when hazards remain unresolved.
* Use realistic conditions and **simulate abnormalities** or faults (e.g., invalid operator inputs, system sensor failures).

#### **Tips for Small Projects:**

* Adopt simulation tools for testing hazardous conditions if hardware testing is cost-prohibitive or unsafe.
* Prioritize the highest-risk scenarios if time and resources are constrained.

---

### **4. Simplify Traceability**

* Use a simple **requirements traceability matrix** (RTM) to track safety-critical requirements and their linked tests:
  + Requirement → Hazard/Event → Test Case → Test Result.
* Focus traceability only on safety-critical areas defined from your hazard analysis.

#### **Tips for Small Projects:**

* Use a spreadsheet to manage traceability—it’s low-cost and sufficient for small teams.
* Limit traceability to **bidirectional links** between hazardous events and corresponding test procedures.

---

### **5. Balance Code Coverage Goals**

* Set **Modified Condition/Decision Coverage (MC/DC)** as the standard for testing safety-critical code paths.
* If 100% code coverage isn’t achievable (e.g., due to limited off-nominal test conditions or resource-intensive scenarios), document a rationale for untested paths and focus testing on:
  + High-risk components.
  + Complex decision-making logic that directly relates to hazard control.

#### **Tips for Small Projects:**

* Use **automated code coverage tools** to identify untested code.
* Focus on covering **every critical logic branch** of safety controls or mitigations rather than less relevant paths.

---

### **6. Implement Regression Testing Efficiently**

* Perform **regression testing** after changes to the software to verify no new risks are introduced:
  + Reuse test cases for safety-critical functionality in regression test sets.
  + Test previously fixed defects to ensure they are not reintroduced into the system.

#### **Tips for Small Projects:**

* Use automated scripts or frameworks (if feasible) for repetitive testing to save time during regression testing.
* Focus regression tests specifically on functionality impacted by the change.

---

### **7. Streamline Test Documentation**

* Keep test documentation concise but sufficient:
  + Record test inputs, outputs, and comparisons with expected results.
  + Clearly flag any issues, defects, or failures for follow-up action.
* Place test procedures and results under configuration management to ensure traceability and accountability.

#### **Tips for Small Projects:**

* Simplify test reporting formats.
  + For example, consolidate test procedures, observations, and results into a single document.
* For smaller teams, use lightweight **document control solutions** (e.g., shared drives, basic versioning tools).

---

### **8. Simulate Instead of Building Full Test Environments**

* If testing on actual hardware is too costly or impractical (e.g., hazardous conditions), use simulation tools where possible:
  + Conduct tests in a **software-in-the-loop (SIL)** environment.
  + Use fault injection and scenario simulations for off-nominal testing.

#### **Tips for Small Projects:**

* Leverage open-source or low-cost simulation tools that fit your project’s scope (e.g., MATLAB, Python scripts).
* Where simulation isn’t possible, test in small incremental stages on actual hardware—first under safe conditions, then under controlled fault conditions.

---

### **9. Independent Review and Small-Team Collaboration**

* Testing safety-critical requirements often benefits from independent verification:
  + If possible, allocate a team member not directly involved in software development to run or review tests.
* Encourage team reviews of test plans, procedures, and results, as small teams often foster close collaboration and shared responsibilities.

#### **Tips for Small Projects:**

* Perform "peer reviews" within the small project team.
* Invite system engineers or safety analysts to contribute during reviews for fresh perspectives on hazard scenarios.

---

### **10. Focus on High-Impact Metrics**

Track **key metrics** to measure progress and ensure thorough testing of safety-critical requirements:

1. **% of safety-critical requirements tested.**
2. **% of tests passing vs. planned test cases.**
3. **Code coverage for safety-critical components.**
4. **# of open vs. resolved issues in safety-critical code.**

#### **Tips for Small Projects:**

* Use simplified tracking tools (e.g., shared spreadsheets, lightweight Jira setups).
* Establish modest but meaningful metric goals to focus testing efforts.

---

### **Practical Example – Small Project Implementation**

#### Project Overview:

* **System Functionality**: Automated shutdown system for a small rover operating in hazardous terrains.
* **Identified Hazards**:
  + Collision with obstacles.
  + Overheating of critical components.
* **Mitigation Techniques**:
  + Software inhibits movement when obstacle detected (< 1 meter).
  + Software triggers cooling systems and powers down non-essential components during overheating events.

#### Practical Steps for Testing:

1. **Analyze System Hazards**:

   * Use FMEA to identify software-driven hazard mitigations (e.g., collision detection and cooling responses).
2. **Define and Plan Tests**:

   * Collision Mitigation:
     + Test case 1: Stop movement when obstacle sensors detect <1m range.
     + Test case 2: Verify "safe state" transition when collisions cannot be avoided.
   * Overheat Mitigation:
     + Test case 3: Verify activation of cooling systems at 80% thermal threshold.
     + Test case 4: Safe shutdown when thermal levels exceed critical limit.
3. **Simulate Edge Scenarios**:

   * Fault inject extreme sensor values (e.g., invalid distance or temperature readings).
   * Introduce hardware faults in cooling components (simulate failure).
4. **Streamline Documentation**:

   * Record all test results in simplified templates showing:
     + Requirement traced to hazard.
     + Test outcome.
     + Issues logged.
5. **Perform Regression Testing After Software Changes**:

   * Re-test both collision and thermal mitigations to ensure new updates didn’t impact safety behavior.

---

### **Conclusion for Small Projects**

By applying these lean processes, small projects can ensure reliable verification of safety-critical software requirements while maintaining efficiency and staying within budget. The key is prioritization, leveraging existing tools, focusing on high-risk areas, and ensuring testing remains traceable, repeatable, and well-documented.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-002)

  [IEEE 730-2014 - IEEE Standard for Software Quality Assurance Processes](https://ieeexplore.ieee.org/document/6835311 "Click to open in new window")

  C/S2ESC - Software & Systems Engineering Standards Committee, Published Date:2014-06-13
* (SWEREF-020)

  [Software Engineering Body of Knowledge (SWEBOK)](https://www.computer.org/education/bodies-of-knowledge/software-engineering "Click to open in new window")

  IEEE, Version 3.0 describes generally accepted knowledge about software engineering. Its 15 knowledge areas (KAs) summarize basic concepts and include a reference list pointing to more detailed information.
* (SWEREF-026)

  [ISO/IEC 19759:2005, A Guide to the Software Engineering Body of Knowledge (SWEBOK)](https://www.sis.se/api/document/preview/906568/ "Click to open in new window")

  ISO/IEC TR 19759 was prepared by the IEEE Computer Society, 2005
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-207)

  [The Software QA and Testing Resource Center - Table of Contents,](http://www.softwareqatest.com/ "Click to open in new window")

  Hower, Rick. (December, 2016), Software QA and Testing Resource Center,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The verification of safety-critical software requirements linked to hazards is a mission-critical activity for NASA, informed by lessons learned from past projects and incidents. These lessons underscore the need to ensure thorough, rigorous testing and hazard evaluation to protect spacecraft, payloads, personnel, and missions. Below are relevant **NASA lessons learned** drawn from historical incidents, investigations, and project retrospectives that highlight best practices and cautionary insights.

---

### **1. Test Coverage for Safety-Critical Software**

#### **Lesson Learned**: *Inadequate test coverage leads to safety-critical failures.*

* **Example**: **Mars Climate Orbiter Failure (1998)**
  + *What Happened*: The failure of Mars Climate Orbiter resulted from a mismatch between metric and imperial units in a software interface. The mission did not adequately test critical software, including scenarios involving unit conversions.
  + *Lesson*: Safety-critical software must undergo **complete and rigorous testing**, including tests specific to scenarios driven by hazardous consequences, such as software handling of external data or interfaces.
  + *Key Takeaway*: Ensure **high code coverage** (preferably 100%) for safety-critical components and thorough end-to-end testing of software interfaces to detect issues impacting mission safety.

---

### **2. Traceability Between Requirements, Hazards, and Testing**

#### **Lesson Learned**: *Inadequate traceability results in untested hazard-related software conditions.*

* **Example**: **Helios Prototype Aircraft Loss (2003)**
  + *What Happened*: The Helios prototype, a high-altitude, long-endurance aircraft, was lost due to unanticipated oscillatory phenomena. The hazard was known, but the corresponding software mitigations were not tested under combined environmental stress conditions (e.g., high turbulence).
  + *Lesson*: Traceability between hazards, requirements, and test cases must be complete to ensure hazard mitigations and cause-response mechanisms are verified in appropriate test conditions.
  + *Key Takeaway*: Use a requirements traceability matrix to confirm that all safety-critical requirements linked to hazardous events are included in the test plan and verified.

---

### **3. Importance of Testing Off-Nominal Scenarios**

#### **Lesson Learned**: *Failure to test off-nominal conditions can result in hazardous outcomes.*

* **Example**: **Genesis Capsule Parachute Deployment Failure (2004)**
  + *What Happened*: The Genesis sample return capsule crashed due to a design error in its fault detection sensors. The software did not account for sensor failure scenarios because off-nominal conditions related to fault responses were excluded from testing.
  + *Lesson*: Incorporate off-nominal and fault conditions into software tests to validate system behavior under potential hazard-inducing conditions (e.g., failed sensor inputs, unexpected operational limits).
  + *Key Takeaway*: Safety-critical testing must include **abnormal and extreme operational scenarios** to confirm reliable software performance.

---

### **4. Rigorous Testing of Fault Recovery Mechanisms**

#### **Lesson Learned**: *Fault recovery systems must be verified to avoid hazard escalation.*

* **Example**: **Hubble Space Telescope Safe Mode Incident (2008)**
  + *What Happened*: The Hubble Space Telescope entered safe mode following a failure in its data handling unit. The designed fault recovery mechanisms behaved unpredictably, leading to unexplored failure states.
  + *Lesson*: Test recovery mechanisms rigorously to ensure that the system can transition to a pre-defined "safe state" during hazardous conditions, particularly when faults escalate.
  + *Key Takeaway*: Failure detection, isolation, and recovery (FDIR) functionalities need **comprehensive validation under simulated failure conditions.**

---

### **5. Hazard Analysis and Requirement Gaps**

#### **Lesson Learned**: *Incomplete hazard analysis leads to overlooked safety-critical requirements.*

* **Example**: **Apollo 13 Oxygen Tank Explosion (1970)**
  + *What Happened*: The Apollo 13 oxygen tank explosion occurred due to thermal insulation design issues that were not accounted for in hazard analyses. Software controlling tank safety mechanisms did not account for such scenarios.
  + *Lesson*: Hazard analyses (e.g., Fault Tree Analysis or FMEA) must be comprehensive, and all identified hazard mitigations must translate into verifiable software requirements.
  + *Key Takeaway*: Regularly review and update system hazard analyses, ensuring that **no gaps exist** in the linkage between hazards, software requirements, and verification tests.

---

### **6. Integration of Safety Testing in Simulated Environments**

#### **Lesson Learned**: *Testing hazardous conditions only in hardware environments may be impractical without controlled simulations.*

* **Example**: **Challenger Disaster (1986)**
  + *What Happened*: The Challenger disaster involved a failure of the solid rocket booster O-ring in low-temperature conditions. The simulator and software systems contributing to monitoring safety-critical conditions were not extensively tested under similar extreme conditions.
  + *Lesson*: For hazards that cannot be directly tested in live environments due to cost or safety risks, use **simulation environments** to validate how the software responds to hazardous scenarios and their mitigation techniques.
  + *Key Takeaway*: Create realistic **simulations of hazardous conditions**, incorporating both nominal and off-nominal scenarios during safety-critical software verification.

---

### **7. Thorough Verification of Automated Safety Responses**

#### **Lesson Learned**: *Automated hazard mitigations must operate predictably under stress conditions.*

* **Example**: **Mars Polar Lander Failure (1999)**
  + *What Happened*: The Mars Polar Lander's descent engine prematurely shut off because the software misinterpreted vibrations as touchdown. This automated response was not adequately tested for false-positive scenarios.
  + *Lesson*: Automated systems managing safety-critical functions (e.g., shutdowns or hazard mitigations) must undergo exhaustive testing for **false-positive and false-negative failure scenarios**.
  + *Key Takeaway*: Ensure testing validates automated responses under nominal, off-nominal, and edge-case conditions.

---

### **8. Testing for Software Interactions with Hardware**

#### **Lesson Learned**: *Software and hardware interactions must be tested comprehensively to avoid triggering hazards.*

* **Example**: **Viking Lander Sensor Inconsistencies (1976)**
  + *What Happened*: Inaccuracies in software processing caused sensor measurement inconsistencies, affecting safe EDL (Entry, Descent, and Landing) operations.
  + *Lesson*: Test safety-critical software in conjunction with the hardware it controls, especially where sensors, actuators, or decision-making algorithms are involved.
  + *Key Takeaway*: Test the **end-to-end integration** between software and hardware under hazardous scenarios.

---

### **9. Documentation and Test Record Keeping**

#### **Lesson Learned**: *Inadequate documentation weakens verification and follow-up analysis.*

* **Example**: **NOAA-N Prime Satellite Mishap (2003)**
  + *What Happened*: A testing error caused an inadvertent application of hazardous conditions, resulting in satellite damage. Insufficient documentation of previous hazard tests prevented teams from identifying and mitigating the issue earlier.
  + *Lesson*: Maintain fully documented test procedures, results, and lessons learned for traceability and future reference.
  + *Key Takeaway*: Place **all test artifacts under configuration management** to ensure traceability and reliability in hazard-related testing procedures.

---

### **10. Lessons for Small Projects**

While small projects often have limited resources, past lessons show that safety-critical requirements and hazard-related software still demand robust testing. Even for small-scale missions:

* Prioritize safety-critical software and focus testing on **high-risk hazards.**
* Use **simulations** and **simplified traceability matrices** to manage testing coverage within resource constraints.
* Ensure comprehensive coverage of **failure detection and recovery mechanisms.**

---

### **Conclusion**

NASA’s lessons learned from various projects highlight that testing safety-critical software requirements is crucial to preventing catastrophic events and ensuring mission success. Comprehensive planning, rigorous testing under nominal and off-nominal conditions, integration with hazard analyses, and proper documentation are foundational for verifying hazard-related requirements. By leveraging these lessons, projects can establish robust verification frameworks that safeguard against foreseeable risks and maintain operational integrity.

 

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-192 - Software Hazardous Requirements**

4.5.12 The project manager shall verify through test the software requirements that trace to a hazardous event, cause, or mitigation technique.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Through testing, confirm that the project verifies the software requirements which trace to a hazardous event, cause, or mitigation techniques.

## 7.2 Software Assurance Products

To ensure proper software assurance for testing safety-critical requirements traceable to hazardous events, causes, or mitigations, the following work products should be generated, reviewed, and managed:

1. **Software Assurance Hazard Analysis Artifacts:**

   * Documentation confirming that hazard controls and mitigation techniques are adequately traced to system/software requirements.
   * A Hazard Requirements Flow Down Matrix linking hazard controls to safety-critical software functions and tests.
2. **Software Test Reports:**

   * Comprehensive test reports for safety-critical requirements, including:
     + Passed/failed test results.
     + Comparison of results to expected behavior (nominal, off-nominal, and hazardous conditions).
     + Justification for untested scenarios or exceptions.
   * Detailed documentation for any non-conformances, open test issues, and actions for resolution.
3. **Traceability Evidence:**

   * A documented **traceability matrix** or equivalent data showing:
     + Systematic mapping of hazards, requirements, and test cases.
     + Bi-directional traceability: Hazard → Software Requirement → Test Case → Result.
   * Evidence that all requirements linked to hazardous software functions are verified via test.
4. **Test Readiness and Approval Evidence:**

   * Records of Software Assurance’s (SA) formal **approval or sign-off** on:
     + Test plans, test procedures, and test cases for safety-critical software components.
     + Test results and associated metrics demonstrating compliance.
5. **Safety-Critical Software Assessments:**

   * Hazard-specific software analyses (e.g., Software Fault Tree Analysis or Timing/Throughput Analyses).
   * Verification that identified hazards and mitigations have been addressed by software functionality and validated through testing.

---

## 7.3 Metrics

Software Assurance (SA) tracks and monitors the following metrics to assess overall compliance, testing progress, and the quality of safety-critical software:

1. **Verification Progress:**

   * ✅ **Number of safety-critical software requirements verified vs. total** safety-critical requirements.
   * ✅ **Number of hazards containing software tested vs. total** hazards containing software.
   * ✅ **Number of requirements tested vs. total** system/software requirements.
   * ✅ **Number of detailed safety-related software requirements tested to date vs. total**.
2. **Test Execution:**

   * ✅ **Number of tests executed vs. total number of tests completed.**
   * ✅ **Number of tests completed vs. total number of tests planned.**
3. **Compliance and Defects:**

   * ✅ **Number of uncovered non-conformances** identified during each testing phase (tracked as open, closed, and by severity level).
   * ✅ **Number of open issues vs. number of closed issues** over time.
   * ✅ **Number of tests passed for safety-critical requirements vs. total** safety-critical requirements tested.
4. **Safety-Related Requirement Analysis:**

   * ✅ **Number of safety-related requirements with verification through test.**
   * ✅ \*\*Number (or %) of safety-critical hazards mitigated via \*\*safety-related software tests.
5. **Traceability Coverage:**

   * ✅ Percentage of hazards, mitigation techniques, and safety requirements fully traced to system/software testing.

---

## 7.4 Guidance for Software Assurance Activities

To meet Requirement 4.5.12, Software Assurance (SA) teams must play an active role in ensuring that safety-critical software requirements linked to hazards are adequately tested, verified, and documented. These activities include:

---

### **1. Verify Traceability of Hazard-Related Software Requirements**

* **Review the Traceability Matrix:**

  + Confirm that all hazard-related software requirements are fully documented and linked to:
    - Identified hazards or hazardous control mechanisms.
    - Corresponding software functions and system interactions.
    - Explicit test procedures.
  + Ensure bi-directional traceability exists between the system hazards, software requirements, and test artifacts.
* **Require a Hazard Requirements Flow Down Matrix:**

  + Ensure all safety requirements and hazard controls flow down appropriately to system/software functions.
  + Verify that the matrix includes mappings of hazard-related requirements to specific test cases and results.
* **Ensure All Hazard-Related Tests Are Executed:**

  + Confirm test procedures fully cover requirements tied to hazardous causes, events, and mitigation techniques.
  + Verify that the software correctly implements all hazard controls or mitigations.

---

### **2. Perform Comprehensive Requirements Analysis**

* Conduct both **top-down** and **bottom-up** analyses of safety-critical software requirements:

  #### Top-Down Analysis:

  + Determine if safety requirements are accurately **flowed down/allocated** from system safety requirements.
  + Identify potential new hazards or unaccounted failure modes in the system design or software.
  + Check for potential **unexpected software behaviors** that could impact safety or hazard response.

  #### Bottom-Up Analysis:

  + Perform **Requirements Criticality Analysis** to identify software behaviors that could create hazardous conditions.
  + Iterate and refine the **Preliminary Hazard Analysis (PHA)** and determine if additional software requirements are necessary.
  + Ensure any new requirements are included in the traceability framework.
* Conduct **Specification Verification Activities**:

  + Confirm that safety-critical requirements are consistent, complete, unambiguous, and feasible within implementation constraints.
  + Document missing, conflicting, or ambiguous software requirements and address them before moving to testing.

---

### **3. Review and Approve Test Plans and Procedures**

* **Ensure Quality of Test Plans:**

  + All safety-critical software requirements must be traced to test cases in the test plan to ensure coverage.
  + Confirm that the tests address nominal, abnormal, and off-nominal scenarios.
* **Approve Test Procedures:**

  + SA should formally approve test procedures related to safety-critical components:
    - Ensure realistic fault injection and simulation-based testing are included.
    - Verify hazard scenarios are adequately modeled and tested.
  + Review procedures to confirm validation of system transition to **safe states** under hazardous or abnormal conditions.
* **Witness Hazards-Related Test Execution:**

  + Attend critical test events or simulations where safety-critical functions are validated.
  + Document observations, non-conformances, or gaps relating to hazard mitigations.

---

### **4. Perform Safety-Related Software Analyses**

During the **Requirements Phase**, SA should assess the following for safety-critical requirements:

* **Software Safety Requirements Flow Down Analysis:**
  + Confirms that hazard requirements are decomposed and implemented within software functionality.
* **Requirements Criticality Analysis:**
  + Helps identify how software might introduce or exacerbate hazards.
* **Specification Analysis and Inspections:**
  + Ensures high-quality software requirements specifications.
* **Timing and Throughput Analysis:**
  + Verifies that safety-critical software functions operate within acceptable response times.
* **Preliminary Fault Tree Analysis (FTA):**
  + Tests coverage of fault paths originating within the software or leading to hazardous conditions.

---

### **5. Manage Software Safety Testing**

* Ensure software safety test verification includes:
  + Test scenarios derived from system hazard analyses like FMEA, PHA, FTA, and subsystem safety analyses.
  + Validation of Failure Detection, Isolation, and Recovery (FDIR) mechanisms.
  + Nominal tests to verify proper hazard control functionality.
  + Off-nominal tests to validate the software’s ability to manage abnormal operating conditions.

---

### **6. Document Results and Track Metrics**

* Ensure all test results, gaps, and associated corrective actions are documented and placed under **configuration management** for future reference.
* Track safety-critical metrics (see **7.3 Metrics**) to assess progress and ensure complete verification of hazard-related software.

---

### **7. Improve Communication**

* Collaborate closely with developers, safety engineers, and test teams.
* Facilitate reviews of safety-critical software requirements and test plans.
* Provide guidance on improving the coverage and quality of hazard-related testing.

---

This improved guidance provides clear direction for Software Assurance teams to support Requirement 4.5.12, ensuring that hazard-related requirements are fully tested, verified, and managed in alignment with safety and mission assurance goals. Use this process to maintain traceability, quality, and confidence in safety-critical software testing.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)       * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

# 8. Objective Evidence

Objective Evidence

Objective evidence refers to documented proof that demonstrates a requirement has been fulfilled. For Requirement 4.5.12, which mandates the testing of software requirements associated with hazardous events, causes, or mitigation techniques, objective evidence must confirm that such testing was conducted successfully and comprehensively, with results thoroughly documented. Below are examples of objective evidence and associated artifacts for this requirement.

---

### **1. Traceability Evidence**

Objective evidence should demonstrate the complete traceability between:

* Hazard analysis.
* Safety-critical software requirements.
* Test cases.
* Test results.

Artifacts:

* **Requirements Traceability Matrix (RTM):**
  + Shows the relationship between hazards, their mitigations, corresponding software requirements, and associated test cases.
  + Documents bi-directional traceability: From hazards to tests and from tests back to the requirement mitigation.

---

### **2. Completed Hazard Requirements Flow Down Matrix**

Objective evidence should show that system-level hazards and mitigations have been correctly translated into software requirements and corresponding tests.

Artifacts:

* **Hazard Requirements Flow Down Matrix:**
  + Maps system hazards and controls to specific software requirements and their associated test cases.
  + Includes links to the functional implementation of hazard mitigations in the software.
* Example elements:
  + Hazard → Cause → Software Function → Requirement → Test Procedure/Test Result.

---

### **3. Test Plans and Procedures**

Objective evidence should confirm that safety-critical software requirements tied to hazards were successfully planned and executed.

Artifacts:

* **Test Plan for Safety-Critical Software:**
  + Lists all software requirements linked to hazards and defines test strategies for nominal, off-nominal, and abnormal conditions.
  + Outlines methodology for safety control testing and mitigation validation.
* **Test Procedures:**
  + Detailed steps for executing tests associated with hazard-related software functionality, including expected behaviors, inputs, and outputs.
  + Fault injection procedures for simulating hazardous conditions.

---

### **4. Test Execution Results**

Objective evidence includes all data generated during test execution that demonstrates hazard-related requirements were verified successfully.

Artifacts:

* **Test Results Reports:**
  + Results of safety-critical software tests, including:
    - Success/failure status.
    - Observed behaviors compared to expected results.
    - Anomalies, discrepancies, and corrective actions.
  + Results for testing hazard prevention, mitigations, safe state transitions, and fault recovery mechanisms.
* **Test Logs/Data:**
  + Raw data from executed tests showing how the software handled hazardous scenarios (e.g., system logs, telemetry, simulation outputs).

---

### **5. Approval Signatures**

Objective evidence should confirm that Software Assurance (SA) and relevant stakeholders reviewed and approved safety-critical test procedures and results.

Artifacts:

* **SA Approval Documentation:**
  + Signed approval of the test procedures and test results targeting safety-critical requirements linked to hazards.
* **Review and Inspection Reports:**
  + Formal review documentation that verifies test artifacts conform to safety standards and project requirements.

---

### **6. Code Coverage Reports**

Code coverage metrics provide objective evidence that safety-critical software components and branches were tested rigorously, ensuring all paths related to hazard controls were executed.

Artifacts:

* **Code Coverage Metrics Report:**
  + Provides Modified Condition/Decision Coverage (MC/DC) data showing:
    - Percentage of executed code paths for hazard-related functions.
    - Identification and mitigation of “dead code” (if any).
* **Coverage Analysis Tools Output:**
  + Evidence generated by automated coverage tools showing safety-related code paths tested successfully.

---

### **7. Simulation and Fault-Injection Data**

Evidence from testing simulated hazardous conditions or injecting faults must confirm that hazard-related requirements are validated in stressful and abnormal scenarios.

Artifacts:

* **Simulation Test Results:**
  + Logs of tests performed using simulated environmental conditions or software-in-the-loop (SIL) environments.
* **Fault Injection Test Results:**
  + Logs showing injected sensor failures, invalid inputs, hardware malfunctions, or concurrent faults to verify robustness of hazard mitigations.
* **Safe State Testing Reports:**
  + Evidence that software takes the system to a predefined safe state under hazardous or unresolved conditions.

---

### **8. Hazard Validation Metrics**

Metrics are essential to show quantitative evidence of testing progress and compliance with safety-critical requirements.

Artifacts:

* **Metrics Dashboard or Reports:**
  + Percentage of safety-related requirements verified vs. total requirements.
  + Number of hazards containing software tested vs. total hazards.
  + Number of open/closed issues identified during safety-critical test phases.
  + Code coverage percentages for safety-critical functions.
  + Test pass/fail percentages for hazard-related scenarios.

---

### **9. Discrepancy or Non-Conformance Reports**

Evidence must include documentation addressing failures or anomalies identified during hazard-related tests and their resolution.

Artifacts:

* **Non-Conformance Reports (NCRs):**
  + Documentation of failed tests where hazard mitigation did not meet expectations.
  + Detailed information on the root causes of issues, corrective actions taken, and resolution verification.
* **Corrective Action Reports (CARs):**
  + Formal resolutions for the discrepancies identified during hazard-related testing.

---

### **10. Configuration Management Evidence**

Objective evidence must show that all safety-related testing artifacts were placed under configuration management for traceability and future reference.

Artifacts:

* **Configuration Management Logs:**
  + Confirm that all test plans, procedures, execution logs, results, and reviews for hazard-related software requirements are version-controlled and accessible.
* **Change History Documentation:**
  + Record of modifications made to safety-critical tests and how prior results were affected, if necessary.

---

### **11. Independent Verification and Validation (IV&V) Evidence**

for high-risk or critical projects with independent testing, evidence from IV&V activities adds a layer of assurance.

Artifacts:

* **IV&V Test Results Reports:**
  + Independent results validating hazard-related software behavior under nominal, abnormal, and extreme conditions.
* **IV&V Approval Documentation:**
  + Sign-off confirming the adequacy of safety-critical software verification.

---

### **12. Lessons Learned Documentation**

Objective evidence should capture lessons learned during testing hazard-related software requirements, such as:

* Challenges encountered during verification.
* Adjustments made to test strategies.
* Effectiveness of mitigations during fault injection tests.

Artifacts:

* **Lessons Learned Report:**
  + Summary of testing successes, gaps, and future recommendations for improving hazard-related software verification.

---

### **Summary of Objective Evidence**

| **Area** | **Objective Evidence Artifacts** |
| --- | --- |
| **Traceability** | Requirements Traceability Matrix (RTM), Hazard Requirements Flow Down Matrix |
| **Test Documentation** | Test Plan, Test Procedures, Simulation/Fault Injection Results, Test Results Reports |
| **Verification Approval** | Software Assurance (SA) and stakeholder sign-offs, Review and Inspection Reports |
| **Code Coverage** | Code Coverage Metrics Reports, Coverage Analysis Output |
| **Simulation/Off-Nominal** | Simulation Logs, Fault Injection Logs, Safe State Testing Reports |
| **Defects/Issues** | Non-Conformance Reports, Corrective Action Reports |
| **Metrics** | Verification Metrics Dashboard (e.g., requirements tested vs. total, hazards tested vs. total hazards, etc.) |
| **Configuration Management** | Configuration Logs, Version-Control History |
| **IV&V Evidence** | Independent Verification and Validation (IV&V) Test Results |
| **Lessons Learned** | Documented insights and recommendations for improving hazard-related software verification |

---

### **Conclusion**

Objective evidence is critical for demonstrating compliance with Requirement 4.5.12. By collecting and organizing traceability data, test results, and formal approvals, along with robust documentation and metrics, project teams can confirm that hazard-related software requirements have been adequately tested to ensure safety, reliability, and mission success.

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
