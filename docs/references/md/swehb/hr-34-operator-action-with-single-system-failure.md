# HR-34 - Operator Action With Single System Failure

> NASA Software Engineering Handbook (SWEHB Ver D), page id 171508198. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508198/HR-34+-+Operator+Action+With+Single+System+Failure

HR-34 - Operator Action With Single System Failure

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508198/HR-34+-+Operator+Action+With+Single+System+Failure#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=171508198)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=171508198&showCommentArea=true&showComments=true#addcomment)

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

4.3.4 The space system shall tolerate inadvertent operator action, as described in Section 4.3.3, in the presence of any single system failure.

## 1.1 Notes

An operator is defined as any human that commands or interfaces with the space system during the mission, including humans in the control centers. The appropriate level of protection (i.e., one, two, or more inadvertent actions) is determined by the integrated human error and hazard analysis per NPR 8705.2. [024](#_tabs-<p></p>)

For reference, the requirement wording "as described in Section 4.3.3" is from Section 4.3.3 of NASA-STD-8719.29, which states: 

4.3.3 The space system shall be designed to tolerate inadvertent operator action (minimum of one inadvertent action), as verified by a human error analysis, without causing a catastrophic  
event.  
Note: An operator is defined as any human that commands or interfaces with the space system during the mission, including humans in the control centers. The appropriate level of protection (i.e., one, two, or more inadvertent actions) is determined by the integrated human error and hazard analysis per NPR 8705.2.)

## 1.2 History

Click here to view the history of this requirement: HR-34 History

HR-34 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.3.4 The space system shall tolerate inadvertent operator action, as described in Section 4.3.3, in the presence of any single system failure. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

The intent of this requirement is to provide a robust human-system interface design that cannot be defeated by a system failure. Where the system is designed to protect for more than one inadvertent action, the level of protection after a single system failure may be reduced - but still protects from a single inadvertent operator action.

This requirement emphasizes the importance of designing space systems that not only tolerate **inadvertent operator actions** (as described in [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action) ) but also maintain this tolerance even when a **single system failure** occurs during operations. The goal is to ensure that human error combined with a system fault does not lead to **catastrophic consequences**.

This requirement is critical to ensuring space systems are robust enough to tolerate cumulative risks posed by **operator errors** combined with failures in **hardware/software systems**. It builds upon[HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action) by extending tolerance to compound risk conditions where operators must manage both their own inadvertent actions and system faults without escalating failures. This ensures mission safety, system resilience, and operational integrity, even under dual failure scenarios.

## 2.1 Why This Requirement Is Necessary

### 2.1.1 Mission Safety

Space systems operate in high-risk environments where errors (both human and system-related) have the potential to cause catastrophic events. By combining **human error tolerance** with **system fault tolerance**, Requirement 4.3.4 ensures:

* Critical safety functions remain intact even under dual conditions of stress: inadvertent operator actions and any system failure.
* The risk of cascading failures from the interplay of human actions and hardware/software faults is minimized.

### 2.1.2 Redundancy and Robustness

System failures are expected in space missions due to:

* Hardware degradation in extreme environments (e.g., radiation, thermal stress).
* Software errors triggered by unforeseen edge cases or environmental factors.

Adding tolerance to inadvertent operator actions in the context of such single-point failures ensures:

* **Robust and redundant designs** capable of maintaining safe operations in degraded states.
* Continuity of life-critical or mission-critical systems during high-risk scenarios.

### 2.1.3 Minimizing Human Error Cascades

* **Stress and work overload** affect operator performance, increasing the likelihood of errors—especially during a system failure when operators may be overwhelmed managing fault responses.
* Tolerating inadvertent operator actions under **single failure conditions** ensures that the compounded effect of human error and system failure does not lead to catastrophic results.

### 2.1.4 Historical Lessons Learned

Various NASA mishaps and near-misses emphasize the interplay between human error and system failures. Learning from past incidents highlights the critical need for this requirement.

1. **Apollo 12 Lightning Strike Incident (1969)**:

   * Lightning struck the Saturn V rocket during launch, causing automatic instrumentation failure.
   * Quick operator actions based on prior training saved the mission. However, if a human error had occurred during fault recovery (e.g., mis-commanding the restart process), it could have cascaded into a catastrophic mission failure.
   * **Takeaway**: In cases of system failures, robust safeguards are needed to tolerate inadvertent operator actions.
2. **Mars Climate Orbiter (1999)**:

   * Software errors (metric vs. imperial units) led to the spacecraft's loss. If the operators had the ability to override or detect erroneous system behavior sooner, failure could have been mitigated.
   * **Takeaway**: System failure combined with miscommunication or inadvertent inputs amplifies risks.
3. **Columbia Accident Investigation Board Findings (2003)**:

   * The failure of the thermal protection system caused by external damage cascaded into a catastrophic event.
   * Lack of system-level redundancies and timely operator awareness worsened the situation.
   * **Takeaway**: Space systems must manage multiple concurrent threats, including human error and system failures.

### 2.1.5 Limited Opportunities for Recovery in Space

Unlike terrestrial operations, space missions provide little to no margin of recovery once errors compound:

* **Distance from Earth**: Communication delays limit real-time assistance, requiring robust on-board autonomy and safeguards.
* **System Criticality**: Single failures often lead directly to degraded or catastrophic system states. Coupled with human error, recovery can become impossible.
* **Safety Margin on Redundant Systems**: Even redundant systems are vulnerable to inadvertent operator actions during failure states. Protecting the redundancy itself is crucial.

This requirement ensures the system can safely tolerate dual fault scenarios to provide operators with time and capacity for safe recovery.

## **2.2. Design Considerations**

### 2.2.1 Independent Redundancies

* Redundant systems (e.g., backup propulsion, life support subsystems) must function independently to prevent failure propagation during human error or single faults.
* When one string fails due to hardware/software issues, the redundant string must remain available and protected from adverse operator commands.

### 2.2.2 Fail-Safe Mechanisms

* Fail-safe designs that:
  + Automatically isolate failed components.
  + Detect and block invalid commands resulting from human error (e.g., accidental disabling of the redundant system during fault management).
  + Protect critical failure recovery paths.

### 2.2.3 Automated Recovery

* Incorporate automation and intelligence for:
  + Error detection and response.
  + Operator prompts/warnings to prevent cascading failures.
  + Recovery into degraded but safe states during combined human error/system fault scenarios.

### 2.2.4 Safeguards Against Human-Error Compounding

* Multi-level confirmation protocols for safety-critical actions during degraded system states.
* Design restrictions preventing commands that exacerbate failure (e.g., disallowing propulsion shutdown if redundancy is compromised).

## 2.3 Benefits

### 2.3.1 Enhanced Safety and Reliability

By addressing the interplay of operator errors and system failures, Requirement 4.3.4 ensures:

* Higher reliability for space missions, particularly in life-supporting and payload-critical systems.
* Operators can handle emergencies safely without inadvertently worsening the situation.

### 2.3.2 Preventing Cascading Failures

Human error often exacerbates single-point system failures by triggering unexpected state transitions, such as disabling redundant systems or invoking an untested operation. Requirement 4.3.4 mitigates these risks through safeguards that:

* Block dangerous operator actions during degraded states.
* Restore safe configurations automatically under dual failure/error conditions.

### 2.3.3 Operational Resilience

Resilience is essential in space systems due to:

* Limited external intervention opportunities during missions.
* High stakes associated with error propagation (e.g., catastrophic impact on crew safety, mission equipment, or scientific objectives).

### 2.3.4 Alignment with NASA Safety Standards

This requirement aligns with NASA’s emphasis on:

* Building **fault-tolerant systems** (NASA-STD-8739.8).
* Preventing **catastrophic consequences** through rigorous hardware/software redundancy, safeguards, and operator training (NPR 7150.2).

# 3. Guidance

This enhanced software engineering guidance ensures the space system can tolerate **inadvertent operator actions** in the **presence of any single system failure** without jeopardizing mission-critical safety or functional objectives. These improvements focus on strengthening software engineering practices, providing actionable strategies, and ensuring compliance with NASA standards to build robust and reliable systems.

By applying this guidance, the space system will achieve:

1. **Resilience to compounded failures** caused by operator errors and single system faults.
2. **Effective safeguards** that minimize the risk of cascading consequences during critical operations.
3. **Compliance with NASA standards** for fault tolerance and human error mitigation, ensuring safe and reliable missions.

This builds confidence in operator and system performance during degraded scenarios while protecting mission objectives and crew safety.

## 3.1 Guidance for Input Fault Mitigation and Command Design

### 3.1.1 Input Validation with Enhanced Command Safeguards

* **Two-Stage Commanding for Critical Functions**:

  + Implement critical commands with **two independent confirmation stages**:
    1. Operator prompts to confirm the intent of their command (e.g., "Are you sure you want to disable Primary Control String A?").
    2. System checks to ensure current system conditions allow safe execution (e.g., redundant paths verified as operational before processing the command).
* **Command Implication Feedback**:

  + Provide descriptive feedback to operators detailing the **impacts of a command**:
    - Clear warnings before disabling critical control strings: "Disabling this control string will end propulsion support unless secondary control string is active."
    - Use visual, auditory, and textual feedback mechanisms to assist operators in making accurate decisions under stress.
* **Error Checks on Operator Inputs**:

  + Validate all operator inputs for correctness, safety, and operational limits.
  + Reject invalid or unsafe commands automatically and present actionable error messages to the operator.

### 3.1.2 Fault Tolerance in Redundant Control Strings

Where faults overlap with operator errors, implement the following **command fault tolerance mechanisms for redundant control strings**:

##### **Primary String Active with Redundant Control Available**:

* **One Independent Command to Disable Each String**:
  + Disable redundant control strings through **separate commands**, each requiring validation independent of the primary control string.

##### **Primary String Disabled with Redundancy Activation Required**:

* **Two Unique and Independent Commands**:
  + Require **two distinct commands** to activate and then disable the redundant control string, ensuring complete operator awareness and mitigation before deactivation occurs.
  + This prevents accidental command cascades under high-stress or degraded mission states.

## 3.2 Improved Software Engineering Tasks

### 3.2.1 Comprehensive Hazard Analysis

Conduct a full **Software Hazard Analysis** identifying potential risks associated with inadvertent operator actions combined with single system failures.

* Assess how **sensor failures, command errors, processing faults, or effector capability loss** can interact with inadvertent operator actions to create hazardous conditions.
* Incorporate the following proactive measures:
  + Analyze **human-machine interface design** to minimize error-prone interactions.
  + Ensure **operator training and operational procedures** include scenarios where system failures occur concurrently with inadvertent inputs.
  + Design safeguards to mitigate inadvertent actions caused by misunderstanding degraded system states.

**Deliverable**: A hazard report mapping each identified risk to mitigations implemented in software design.

### 3.2.2 Safety Analysis Techniques

Use advanced **Safety Analysis Techniques** throughout the development lifecycle:

* **Software Fault Tree Analysis (FTA)**:
  + Identify fault propagation pathways arising from human errors combined with system failures.
  + Design software controls to isolate faults and prevent escalation.
* **Software Failure Modes and Effects Analysis (FMEA)**:
  + Examine failure conditions triggered by erroneous human inputs during active system faults.
  + Define mitigations and recovery strategies for each failure mode.

**Deliverable**: Fault Tree Diagrams and FMEA reports for all safety-critical system functions.

### 3.2.3 Independent Verification and Validation (IV&V)

Ensure **Independent Verification and Validation (IV&V)** processes are applied to confirm compliance with Requirement 4.3.4.

* Validate both **error-tolerance mechanisms** and system safeguards against compounded human errors and single system failures.
* Focus IV&V testing on scenarios where:
  + Critical control strings fail due to hardware/software faults.
  + The operator issues erroneous commands that impact redundancy paths.

**Deliverables**:

* **IV&V Reports** providing verification of system readiness for human error and fault tolerance.
* Participation records documenting IV&V involvement in reviews, testing, and technical assessments.

### 3.2.4 Simulations and Testing

Develop and execute robust testing strategies:

* **Simulations**:

  + Model real-world scenarios with compounding operator error and system failure conditions (e.g., inadvertent engine shutdown coupled with redundancy hardware failure).
  + Test the system's ability to isolate, contain, and recover from degraded states.
* **Testing**:

  + Perform boundary and stress testing to identify failures and operator missteps under unusual or extreme operating conditions.
  + Validate that **Fault Detection, Isolation, and Recovery (FDIR)** mechanisms meet time-to-event requirements to prevent cascading hazards.

**Deliverables**:

* Simulation logs demonstrating system behavior in compounded failure scenarios.
* Test reports proving the system recovers from simulated operator errors and faults without catastrophic impact.

### 3.2.5 Error Handling and Recovery Mechanisms

Develop **robust error-handling mechanisms** capable of preventing escalation during compounded fault scenarios:

* Detect invalid commands and block them before execution.
* Automatically transition the system to a **safe mode** when simultaneous operator errors and system faults create hazardous conditions.
* Implement **rollback mechanisms** for inadmissible operator actions or unexpected system states.

**Deliverable**: Documented error-handling procedures, including test coverage results verifying recovery mechanisms.

### 3.2.6 Configuration Management

Ensure strict **Configuration Management** to reduce risks associated with incorrect or mismatched software versions:

* Establish version control for all software components that mitigate operator error and system fault interactions.
* Regularly audit configurations after software changes to verify continued alignment with safety-critical standards.

**Deliverable**: Configuration management reports verifying software version consistency during testing and delivery.

### 3.2.7 Safety-Critical Software Requirements Implementation

Implement and verify all software requirements for safety-critical systems per **NASA NPR 7150.2** standards:

* Ensure **redundancy management requirements** are fully implemented to prevent loss of safe operational states despite overlapping errors/faults.
* Address hazards identified directly from software-related failures or operator misuse of control paths.

**Deliverables**:

* Test results verifying implementation of requirements, including fault tolerance mechanisms and operator safeguards.

### 3.2.8 Training and Documentation

Provide **comprehensive operator training and documentation** to prevent inadvertent actions during system fault states:

* Develop detailed **User Manuals** with guidance on:
  + Identifying system failure conditions.
  + Issuing validated commands during redundancy control scenarios.
  + Recovering from inadvertent actions safely.
* Include operator training in simulated environments featuring concurrent faults and missteps to ensure familiarity with safeguards.

**Deliverable**: Training completion records and user guides outlining error recovery approaches.

## 3.3 Additional Recommendations

* Enforce **Human Factors Engineering (HFE)** principles in interface designs to ensure safety-critical commands are protected by clear prompts, physical separation, or hierarchical menu settings.
* Continuously monitor all operator input systems for unintended patterns during mission simulations, providing adjustment opportunities before actual deployment.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)[053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

Also, see the SWE Handbook pages for [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action). 

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Requirements related to Human Rated Software. 

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

Small projects generally operate with limited resources, simplified systems, and shorter timelines. Therefore, implementing this requirement within small projects requires a **scaled-down approach** that prioritizes critical safety and system robustness while maintaining feasibility and efficiency. This guidance provides actionable strategies designed specifically for small projects.

Summary of Deliverables for Small Projects:

1. **Hazard Analysis Report** identifying key risks and mitigations.
2. **Two-Stage Command Flow Design** with safeguards for redundancy handling.
3. **Recovery Flowchart** for error handling and redundancy management.
4. **Test Summary Report** demonstrating key mitigation behaviors.
5. **Change Log** for configuration and management consistency.
6. **User Manual** and operator training materials focused on error prevention and recovery.
7. **IV&V Assessment Report** focused on lightweight validation activities.

By scaling down processes while maintaining compliance with NASA standards, small projects can achieve robust systems capable of tolerating inadvertent operator actions during single system failures efficiently and affordably.

## 4.1 Simplify Redundancy Management

#### **Goal**: Implement a basic yet effective fault tolerance strategy for critical system functions without over-engineering.

1. **Critical Path Identification**:

   * Focus on **safety-critical functions** where human errors and system failures could lead to hazards (e.g., propulsion, power distribution, or life support).
   * Map out the redundant control paths and failure modes for each Must Work Function. For a small project, minimize the number of redundant paths to reduce complexity.
2. **Command Safeguards**:

   * Use **two-stage command confirmation**:
     + **Stage 1**: Ask the operator to confirm intent ("Are you sure you want to disable this function?").
     + **Stage 2**: Validate system readiness (e.g., "Backup system activated; operation approved").
   * Place **stop-check commands** for critical disabling processes:
     + For **primary string disabling**, require one command and verify redundant control is available.
     + For **redundant string disabling**, require two independent commands to ensure deliberate action.
3. **Automated Validation**:

   * Automate system checks to ensure operator commands align with acceptable states (e.g., redundant strings active).
   * Block invalid inputs and provide descriptive feedback to the operator.

## 4.2 Perform Lightweight Hazard Analysis

#### **Goal**: Identify and mitigate risks efficiently within the safety-critical software scope.

1. **Hazard Identification**:

   * Use a simple tabular method to capture **potential hazards**, their causes, consequences, and mitigations:

     | **Hazard** | **Operator Action** | **System Failure** | **Mitigation** |
     | --- | --- | --- | --- |
     | Loss of propulsion | Operator shuts down a control string | Backup string fails | Require two-stage confirmation |
     | Power loss | Operator disables power-routing software | Sensor input failure | Auto-switch to backup routing |
2. **Minimize Risk Scope**:

   * Focus only on **direct operator interactions** and their impact on failure-prone systems (e.g., critical commands and sensor input reliance).
   * Avoid exhaustive analyses to save resources, focusing instead on key scenarios.
3. **Deliverable**:

   * Develop a **short hazard analysis report** (e.g., 1-2 pages) with precise recommendations for software mitigations.

## 4.3 Implement Error Handling and Recovery Mechanisms

#### **Goal**: Build basic but reliable error detection and recovery into the system.

1. **Error Detection**:

   * Build minimalistic error detection for **operator inputs**:
     + Use assertions or rules to check input validity before executing commands.
     + Automatically detect errors in system output states (e.g., primary control disabled prematurely).
2. **Recovery Mechanisms**:

   * Implement basic recovery actions for degraded states:
     + **Rollback mechanisms** for invalid operator commands (e.g., re-enable primary string if redundant string is inactive).
     + **Failover actions** for single system failures (e.g., automatically activate backup control strings).
3. **Deliverable**:

   * Provide a **functional recovery flowchart** for software modules detailing error detection and resolution paths.

## 4.4 Streamline Testing and Verification

#### **Goal**: Ensure compliance with this requirement without exhaustive testing.

1. **Simple Test Coverage**:

   * Focus on testing **critical operator-error scenarios**:
     + Testing command inputs for misbehavior during system faults (e.g., inadvertent shutdowns during failure cases).
     + Simulating system recovery from combined operator and fault errors.
2. **Minimal Simulation Efforts**:

   * Develop simple simulation environments to mimic key redundant system failure cases:
     + Inject faults during critical operator commands to verify system behavior.
     + Test system’s ability to isolate, recover, or prevent escalation of hazards.
3. **Deliverable**:

   * Create a **Test Summary Report** with only critical scenarios tested, including input error detection and recovery results.

## 4.5 Simplify Configuration Management

#### **Goal**: Implement basic software configuration controls to reduce risks.

1. **Version Control**:

   * Use lightweight version control tools (e.g., **Git**) to track software changes for safety-critical modules.
   * Maintain records of changes and testing results for modules involved in managing errors or redundant controls.
2. **Baseline Management**:

   * Define a clear baseline for all safety-critical software functions and components.
   * Use simple checklists to verify consistency during testing and simulation.
3. **Deliverable**:

   * Maintain a **Change Log** to document changes specific to inadvertent operator error handling and recovery systems.

## 4.6 Documentation and Operator Training

#### **Goal**: Provide clear guidance and training materials to prevent operator errors.

1. **User Documentation**:

   * Create a simplified **User Manual** focused on:
     + Procedures for managing redundancy systems during failures.
     + Clear instructions for issuing commands safely.
     + Recovery steps for inadvertent erroneous commands.
2. **Training Plan**:

   * Provide short **training sessions** with hands-on exercises:
     + Demonstrate safe operating practices for critical systems.
     + Train operators to identify faulty feedback systems and recover safely.
3. **Deliverable**:

   * Supply a **User Manual** with step-by-step recovery instructions and command warnings.

## 4.7 Independent Verification & Validation (IV&V)

#### **Goal**: Use lightweight, targeted IV&V activities to assess safety requirements.

1. **Key IV&V Focus Areas**:

   * Ensure basic error recovery mechanisms work as intended.
   * Verify:
     + Operator command validation.
     + Fault detection for redundant system failures.
   * Review how system safeguards (e.g., command confirmations) mitigate errors and hazards.
2. **Deliverable**:

   * Provide IV&V documentation with high-level assessments of compliance for key scenarios.

## 4.8 Tailored Safety-Critical Software Requirements

#### **Goal**: Implement NPR 7150.2 standards in areas most relevant to small projects.

1. **Focus Areas**:

   * Address redundancy safety requirements only for **essential critical paths**.
   * Conduct simplified tests that tie hazard mitigations directly to software responses.
2. **Deliverable**:

   * Maintain compliance matrix tracking requirements specifically tied to inadvertent operator error handling and recovery mechanisms.

## 4.9 Key Considerations for Small Projects

1. **Prioritize Safety**: Allocate resources to safety-critical pathways and automation that minimize error propagation during failure scenarios.
2. **Keep Design Simple**: Avoid overcomplicated solutions and focus on practical, minimalist designs that are easy to validate and implement.
3. **Leverage Existing Tools**: Utilize open-source or readily available tools for simulations, configuration management, and IV&V activities to reduce cost and time.
4. **Collaborate with Operators Early**: Engage operators early in development to understand their workflows and potential error-prone actions.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-024)

  [Human-Rating Requirements for Space Systems (Updated w/Change 2)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=2C "Click to open in new window")

  NPR 8705.2C, NASA Office of Safety and Mission Assurance, 2008.,
  Effective Date: July 10, 2017, Expiration Date: July 10, 2025
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-458)

  [NASA Technical Requirements for Human-Rating](https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/0/NASA-STD-871929-Baseline-draft.pdf "Click to open in new window")

  NASA-STD-8719.29, National Aeronautics and Space Administration, Approved:2023-12-11 Baseline,  This standard establishes technical requirements necessary to produce human-rated space
  systems that protect the safety of the crew and passengers on NASA space missions

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA’s robust history of missions has revealed several incidents where inadvertent operator actions or systemic failures either compounded risks or highlighted the importance of implementing robust fault and error-tolerant mechanisms. The following lessons learned reflect both successes and challenges that provide critical insights into the rationale, implementation, and importance of Requirement 4.3.4.

---

### **Key Lessons Learned**

#### **1. Apollo 12 Lightning Strike Incident (1969)**

* **Event**: During the Apollo 12 launch, the Saturn V rocket was struck by lightning twice, causing a temporary loss of telemetry and guidance system data. Quick operator intervention saved the mission with the switch to backup systems.
* **Relevance to Requirement 4.3.4**:
  + Space systems need **redundant control strings to remain functional** despite single failure events and inadvertent operator actions.
  + Human operators under stress may inadvertently disable critical systems unless clear procedures exist to validate their actions.
  + For Apollo 12, failure to safeguard primary and backup control systems against operator error could have led to mission failure.
* **Lesson**: **Require automated recovery mechanisms** and enhanced command safeguards to maintain critical functions during single faults.

---

#### **2. Mars Climate Orbiter (1999)**

* **Event**: The Mars Climate Orbiter was lost because of a unit mismatch between metric and imperial systems. Ground operators inadvertently sent erroneous commands, which were compounded by inadequate software validation checks.
* **Relevance to Requirement 4.3.4**:
  + Inadequate **input validation** led to a catastrophic failure.
  + Redundant systems could have cross-checked operator input or flagged commands when inconsistencies were detected.
  + The system failed to tolerate **both human error and software insufficiencies**.
* **Lesson**: **Implement automated validation mechanisms** for operator inputs, especially in the presence of potential single system failures.

---

#### **3. Space Shuttle Columbia Accident (2003)**

* **Event**: Damage to the Columbia Shuttle’s heat shield during launch led to its disintegration on re-entry. Despite reports of foam strikes and sensor malfunctions, no corrective actions were made in-flight.
* **Relevance to Requirement 4.3.4**:
  + The disaster underscored the dangers of **overlapping failures**: physical hardware damage (a sensor or structural failure) and an inability to act effectively (manual or automated safeguards inadequately implemented at the systems level).
  + Had greater error-detection or automated action been in place, mitigation or risk reduction strategies could have been applied.
* **Lesson**: System designs must ensure tolerance against **multiple potential fault sources**, including inadvertent operator inaction or unforeseen failures.

---

#### **4. Perseverance Rover Mission (2020)** – A Success Story

* **Event**: During the Perseverance Rover landing, mission controllers anticipated the possibility of faulty operator commands interfering with the critical Entry, Descent, and Landing (EDL) phase. To mitigate risks, an autonomous and heavily tested redundancy strategy was implemented, with "human-in-the-loop" safeguards.
* **Relevance to Requirement 4.3.4**:
  + Operators are prone to inadvertent commands during high-stakes operations where system degradation or faults may already exist.
  + Multiple fail-safe systems and precise simulation testing ensured that both automation and manual responses were robust enough to avoid cascading failures.
* **Lesson**: Redundant systems, simulation-backed failure testing, and human-interaction safeguards are necessary to build fault-tolerant systems.

---

#### **5. SOHO (Solar and Heliospheric Observatory) Mission Recovery**

* **Event**: During SOHO operations in 1998, a series of operator errors (power cycling and safe mode triggers) combined with a system anomaly caused the spacecraft to lose orientation and enter "emergency sun reacquisition mode." This sequence nearly resulted in the loss of the mission. Recovery efforts were successful only due to redundancy in the spacecraft's gyroscopes and error recovery systems.
* **Relevance to Requirement 4.3.4**:
  + Operator commands issued while a **single hardware failure** was already present led to cascading issues that compounded recovery efforts.
  + Disabling redundant systems before validating backup readiness puts the system at catastrophic risk.
* **Lesson**: Implement **preventative checks** that restrict inadvertently disabling redundant systems when one or more systems are already non-operational.

---

#### **6. Skylab (1973)**

* **Event**: During the Skylab mission, a solar panel failed to deploy, and the spacecraft experienced temperature control issues due to both hardware failures and potential miscommunication of commands. Operator and engineering decisions were influenced by incomplete data, which delayed mitigation.
* **Relevance to Requirement 4.3.4**:
  + **Operator miscommunication** and **single string control errors** delayed mission recovery.
  + Redundancy and protections for backup systems should have been more rigorously incorporated.
* **Lesson**: Redundant systems and checks must guard against **both hardware failures and compounded operator errors** involving faulty sensor data.

---

#### **7. Kepler Spacecraft Reaction Wheel Failures (2013)**

* **Event**: The Kepler spacecraft lost two of four reaction wheels used for attitude control, rendering it incapable of meeting its original mission objectives. Operators modified commands to use existing systems to salvage the mission.
* **Relevance to Requirement 4.3.4**:
  + Failure of redundant control systems highlights the importance of **preventing inadvertent commands that disable working components or mismanage degraded states**.
  + Operator decisions must be supported with **automated validation** and clear fallback mechanisms.
* **Lesson**: Fault recovery must include tolerance for potential operator-induced error alongside automated system-level safeguards.

---

### **Cross-Cutting Lessons for Requirement 4.3.4 Implementation**

#### **Lesson 1: Redundant Command Isolation**

Avoid reliance on shared resources between primary and backup control paths. In critical systems, redundancy should:

* Operate independently.
* Require distinct, unique commands for control, ensuring one pathway cannot degrade the other inadvertently.

#### **Lesson 2: Automated Input Validation**

Operator inputs should always be validated against:

* Current system state (e.g., checking that redundant control strings are operational before disabling a primary string).
* System failure conditions that increase risk (e.g., a fault in sensor input).

#### **Lesson 3: Human Factors Engineering**

Design the operator interface to:

* Prevent inadvertent input by requiring confirmation (multi-step validations).
* Reduce cognitive overload during fault scenarios—clear warnings about system degradation must be prominently displayed.

#### **Lesson 4: Simulation Training for Overlapping Failures**

Simulating concurrent single system failure and inadvertent operator actions is critical for:

* Testing both automated and manual recovery mechanisms.
* Preparing operators to function effectively under high-risk, high-stress scenarios.

#### **Lesson 5: Time-to-Recovery Criticality**

Fault Detection, Isolation, and Recovery (FDIR) systems need to:

* Meet time-sensitive hazard requirements to minimize cascading results.
* Include failover logic to maintain safety-critical functions even under dual-failure cases.

---

### **Practical Applications of These Lessons**

1. **Two-Stage Commanding**: Implement two-stage commands for critical systems, especially when disabling functionality critical to safety.
2. **Automated Safeguards**: Validate commands against system state (e.g., confirm active redundancy before executing).
3. **Independent Testing**: Test error-tolerance mechanisms with failure injection scenarios involving operator inputs and hardware/software failures.
4. **Redundancy Controls**: Ensure redundant systems are not linked by shared points of failure or commands.

---

By leveraging these lessons learned, systems can be designed and tested to meet Requirement 4.3.4 with confidence in their ability to handle the compounded risks of inadvertent operator actions and system failures.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-34 - Operator Action With Single System Failure**

4.3.4 The space system shall tolerate inadvertent operator action, as described in Section 4.3.3, in the presence of any single system failure.

By implementing these enhanced SA guidance practices, small and large NASA projects can create robust, fault-tolerant systems capable of mitigating the risks posed by inadvertent operator actions and hardware/software failures. These refinements ensure safety-critical behaviors are thoroughly analyzed, tested, and validated while ensuring NASA’s high standards for mission reliability and safety.

## 7.1 Tasking for Software Assurance

1. Confirm that the hazard reports or safety data packages contain all known software contributions or events where software, either by its action, inaction, or incorrect action, leads to a hazard.
2. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8 [278](#_tabs-<p></p>), Appendix A.
3. Assess that hazard analyses (including hazard reports)identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
4. Confirm that the traceability between software requirements and hazards with software contributions exists.
5. Develop and maintain a software safety analysis throughout the software development life cycle.
6. Ensure that safety-critical software requirements are implemented per the NPR 7150.2 Requirements Mapping Matrix and tested or verified.
7. Perform the SA tasking for [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action). 
   1. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically the off-nominal scenarios to mitigate the impact of inadvertent operator actions. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks.) Ensure that the project has developed and executed test cases to test the impact of inadvertent operator actions.
   2. Perform safety reviews on all software changes and software defects.
   3. Perform test witnessing for safety-critical software to ensure the impact of inadvertent operator actions is mitigated.
   4. Confirm the use of automated tools for static analysis, dynamic analysis, and other verification and validation activities.
   5. Confirm that strict configuration management is maintained to ensure that the correct software versions and configurations are used.
   6. Ensure comprehensive training and documentation for operators to minimize the chances of inadvertent actions is available.

## 7.2 Software Assurance Products

To ensure the space system can **tolerate inadvertent operator actions** in the presence of any single system failure without resulting in catastrophic consequences. This guidance consolidates best practices for software assurance, software design, testing, and operational safeguarding to meet NASA’s stringent safety and quality standards.

To provide comprehensive support for Requirement 4.3.4, SA must deliver the following **improved products and practices**:

### 7.2.1 Comprehensive Analysis

* [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis)

  + Confirm that safety-critical software requirements explicitly address:
    - Tolerance to inadvertent operator actions.
    - Fault recovery capabilities during single system failures.
  + Verify that all safety requirements are measurable, testable, and traceable.
  + Ensure hazard mitigations (as identified in hazard reports and safety analysis) are fully traced to software implementation and test cases.
* [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis)

  + Assess that architectural design supports:
    - Protective mechanisms (e.g., automated confirmation, multi-step commands) for inadvertent operator commands.
    - Redundancy management and fault containment.
  + Evaluate interfaces between operators and systems to ensure robust error prevention.
* [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis)

  + Ensure hazard analyses identify:
    - Interaction between operator actions and system failure conditions.
    - Full scope of cascading risks from compounding failures.
    - Confirm that mitigation strategies (e.g., lockout for high-risk commands) are implemented and validated.
  + Verify any hazards tied to software are clearly linked to their corresponding safety-critical software components.

### 7.2.2 Control and Quality Practices

* [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis)

  + Verify that code complies with safety-critical requirements for cyclomatic complexity (≤15 unless justified with a rationale).
  + Validate coding standards adherence to minimize defects that could lead to hazardous operator-input behavior.
  + Validate defensive programming techniques to ensure invariants for redundant systems and safeguard checks are addressed.
* [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports)

  + Functional Configuration Audit (FCA): Confirm that all safety-critical functionality is implemented correctly.
  + Physical Configuration Audit (PCA): Validate proper implementation of controls for inadvertent commands and redundancy handling.
* **Test Witnessing and Signatures**

  + Ensure test witnessing is documented for all safety-critical functions, specifically for:
    - Fault injection scenarios combining operator and single-fault conditions.
    - Validation of recovery mechanisms and automated mitigations.
    - Test environments simulating operational stress where errors are likely.

### 7.2.3 Automated Tools and Results

* Utilize automated tools for:

  + **Static and Dynamic Analysis**:
    - Identify unused or unsafe software components.
    - Detect and eliminate defects that could trigger operator error mishandling.
  + **Code Coverage Analysis**:
    - Ensure complete coverage of safety-critical control paths, particularly those implementing handling for single-fault events and inadvertent operator actions.
  + **Cyclomatic Complexity Analysis and Metrics**:
    - Ensure maintainable, reliable code for safety-critical software. Flag and assess any areas exceeding complexity limits.
* **Software Work Product Assessments**

  + Ensure assessments cover plans, procedures, and user manuals that explain protective measures, backup activation, and operator recovery directions.
  + Evaluate that results from test reports align with safety-critical and fault-tolerant requirements.

### 7.2.4 Software Hazard Reports

* Hazard reports must include:
  + Traced mitigations linking faults and recovery mechanisms to software.
  + Validations for operator command protections and fault-tolerant design.
  + Test results from controlled scenarios covering inadvertent actions compounded with faults.

## 7.3 Metrics

To verify that the space system meets the tolerance requirements, several key **metrics** should be monitored and reported. These metrics guide development progress, track safety-critical requirements, and evaluate system readiness.

### 7.3.1 Verification and Validation Metrics

1. **Test Coverage**:

   * Percentage of test coverage for functions handling single-fault and operator-error scenarios.
   * Aim for **100% test coverage** of all identified safety-critical software components.
2. **Defect Density**:

   * Track defects related to safety-critical sections.
   * **Target**: No unresolved safety-critical defects in final software delivery.
3. **Requirements Traceability**:

   * Percentage of requirements traced to their implementation and linked to test cases.
   * **Goal**: Full traceability for tolerating operator actions and fault tolerance.

### 7.3.2 Safety Metrics

1. **Hazard Mitigation Efficiency**:

   * Measure the number of hazards with mitigations implemented and validated.
   * Track unresolved hazards and their projected impacts.
2. **Safety Reviews Completed**:

   * Percentage of safety-related artifacts (e.g., hazard analyses) peer-reviewed.
3. **Control Path Validation**:

   * Metric for confirmed isolation between redundant control strings.

### 7.3.3 Quality Metrics

1. **Cyclomatic Complexity**:

   * Ensure all safety-critical components meet a complexity threshold (≤15). Track instances exceeding this threshold and document technical justifications.
2. **Code Stability (Churn)**:

   * Measure code change frequency for safety-critical functions to target areas for detailed testing.

### 7.3.4 Performance Metrics

1. **Response Time for Mitigation**:
   * Measure the time taken to respond to inadvertent operator actions under simulated single-fault conditions.
   * **Target**: Recovery procedures complete within time-to-event limits that prevent hazards.

### 7.3.5 Configuration Management Metrics

1. **Version Control Effectiveness**:
   * Track versions used during tests and resolve inconsistencies or errors stemming from incorrect configurations.

### 7.3.6 Independent Verification & Validation (IV&V) Metrics

1. **IV&V Issue Resolution**:
   * Number of open safety-related issues raised by IV&V assessments.
   * Ensure consistent closure rates before delivery milestones.

## 7.4 Guidance for Software Assurance Tasks

The following updated tasks refine the scope and precision required to meet this requirement:

### 7.4.1 Software Safety and Hazard Analysis

1. Utilize **Fault Tree Analysis (FTA)** and **Failure Modes and Effects Analysis (FMEA)** to:

   * Identify paths where operator errors intersect with single-component failures.
   * Develop controls for mitigating cascading effects.
2. Validate that all **software-controlled hazard mitigations** are implemented and tested:

   * E.g., safeguards like automatic failovers, tiered command confirmations, or default safe modes.

### 7.4.2 Testing and Test Witnessing

1. Perform tests for:

   * Scenarios combining operator errors and active system faults.
   * Validation of safeguard effectiveness for incorrect command blocks and backups.
2. Witnessing:

   * Document and oversee a broad test suite targeting safety-critical components.

### 7.4.3 Verification and Validation (V&V)

1. Verify:

   * That all recovery mechanisms meet **time-to-event constraints** to avoid escalating hazards.
2. Validate:

   * The software system performs as intended in its operational context, with all redundant controls functioning independently.

### 7.4.4 Change Management

1. Record and track:
   * All defects that influence operator safeguards or redundancy mechanisms.

### 7.4.5 Training and Documentation

1. Ensure operators are trained with simulations of:

   * Recovery from inadvertent commands under failed system states.
2. Deliver **clear user manuals** with descriptions of:

   * Critical safety features, workflows for recovery, and warnings for high-risk commands.

## 7.5 Software Assurance And Software Safety Tasks

To ensure that the space system can tolerate inadvertent operator actions in the presence of any single system failure, the following software assurance and software safety tasks should be implemented:

1. **Software Safety and Hazard Analysis**: Develop and maintain a Software Safety Analysis throughout the software development life cycle. Assess that the Hazard Analyses (including hazard reports) identify the software components associated with the system hazards per the criteria defined in NASA-STD- 8739.8, Appendix A. (See SWE-205 tasks.) Perform these on all new requirements, requirement changes, and software defects to determine their impact on the software system's reliability and safety. Confirm that all safety-critical requirements related to tolerating inadvertent operator actions are met and adequately tested to prevent failures during mission-critical operations. It may be necessary to discuss these findings during the Safety Review so the reviewers can weigh the impact of implementing the changes. (See Topic [8.58 – Software Safety and Hazard Analysis](https://swehb.nasa.gov/display/SWEHBVD/8.58+-+Software+Safety+and+Hazard+Analysis).)  
   1. **Hazard Analysis/Hazard Reports**: Confirm that a comprehensive Hazard Analysis is completed to identify potential hazards that could result from inadvertent operator actions combined with single system failures. This analysis should include evaluating existing and potential hazards and recommending mitigation strategies for identified hazards. The Hazard Reports should contain the results of the analyses and proposed mitigations (See Topic [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content).)
   2. **Software Safety Analysis**: To develop this analysis, utilize safety analysis techniques such as [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) and [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) to identify safety risks and formulate effective controls. These techniques help identify hazards, hazard causes, and potential failure modes. When generating this SA product, see Topic [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) for additional guidance.
2. **Safety Reviews**: Perform safety reviews on all software changes and software defects. This ensures that any modifications do not introduce new vulnerabilities or increase the risk of a single system failure leading to catastrophic events.
3. **Peer Reviews**: Participate in peer reviews on all software changes and software defects affecting safety-critical software and hazardous functionality. (See [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) tasks.) This ensures that any modifications control the input of bad data and do not introduce new vulnerabilities or increase the risk of inadvertent actions leading to a single system failure.
4. **Change Requests**: Monitor the number of software change requests and software defects and their impact on the system's reliability and safety. Increases in the number of changes may be indicative of requirements issues or code quality issues resulting in potential schedule slips. (See [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes), [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes).)
5. **Test Witnessing**: Perform test witnessing for safety-critical software to ensure the impact of inadvertent operator actions is mitigated. (See [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing).) This includes witnessing tests to:   
   1. Confirm that the system can handle inadvertent actions without resulting in catastrophic consequences from any single system failure. This could include:  
      1. Measuring the time taken for the system to detect and respond to inadvertent operator actions to ensure timely and accurate execution of mitigation procedures. A prolonged period could cause catastrophic consequences.
      2. Ensuring the system is available and operational when needed, especially during critical mission phases, to support tolerance of inadvertent operator actions.
   2. Uncover unrecorded software defects and confirm they get documented and recorded.
   3. Confirm robust error handling and recovery mechanisms to address errors resulting from inadvertent operator actions are implemented. This includes ensuring adequate error handling and that the system can recover from errors without leading to catastrophic events.
6. **Simulations and Testing**: Ensure that the project has developed and executed simulations to model and test the impact of inadvertent operator actions in the presence of single system failures. This includes conducting tests to verify that the software system can handle these scenarios without resulting in catastrophic consequences.
7. **Test Results Assessment**: Confirm that test results are assessed and recorded and that the test results are sufficient verification artifacts for the hazard reports. (See [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results).)
8. **Automated Verification and Validation**: Confirm the use of automated tools for static analysis, dynamic analysis, code coverage, cyclomatic complexity, and other verification and validation activities. This helps identify potential software defects that could result in catastrophic events due to inadvertent operator actions in the presence of any single system failure. (See [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) tasks.)  
   1. **Code Quality**: Use metrics such as cyclomatic complexity and static analysis results to ensure the code is maintainable and less prone to errors. Specifically, confirm that safety-critical software components have a cyclomatic complexity value of 15 or lower, or software developers must provide a technically acceptable rationale if this value is exceeded. (See [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software), [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis).)
   2. **Code Coverage**: Confirm that 100% code test coverage is addressed for all identified software safety-critical software components or ensure that software developers provide a risk assessment explaining why the test coverage is impossible for the safety-critical code component. (See [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements), [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software).)
   3. **Software Volatility**: Measure changes in the codebase to monitor stability and identify areas of frequent modification that may need more rigorous testing. (See [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics).)
   4. **Verification Testing**: The verification analysis activity ensures that the safety requirements for the software were properly flowed down from the system safety requirements, traced to test/test procedures and that they have been adequately tested. (See [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures), [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification), and Topic [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis).)
   5. **Validation Testing**: Software validation is a software engineering activity that shows confirmation that the software product, as provided (or as it will be provided), fulfills its intended use in its intended environment.  In other words, validation testing ensures that “you built the right thing.” (See [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation), [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools), [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations), and Topic [8.57 - Testing Analysis](https://swehb.nasa.gov/display/SWEHBVD/8.57+-+Testing+Analysis).)
9. **Configuration Management**: Ensure that strict configuration management is maintained to ensure that the correct software versions and configurations are used.  See [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) for more information. This reduces the risk of errors due to incorrect or inconsistent configurations, tracks changes, and maintains consistency. This also includes performing the SWE-187 tasking. 
   1. Assess that the software safety-critical items, including the hazard reports and safety analysis, are configuration-managed (See [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) tasking.)
10. **Safety-Critical Software Requirements**: Ensure that safety-critical software requirements are implemented per the NPR 7150.2 Requirements Mapping Matrix and tested or verified. This includes confirming that the software control functions in a system hazard are identified and providing mitigations for hazardous conditions.
11. **Training and Documentation**: Ensure comprehensive training and documentation for operators to minimize the chances of inadvertent actions is available. This includes clear instructions, warnings, and recovery procedures.

By performing these tasks, the space system can be designed to mitigate the hazardous behavior of critical software, ensuring safety and reliability.

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)[053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence refers to tangible, documented artifacts and results that demonstrate compliance with this requirement. The purpose of objective evidence is to provide verifiable proof that a system can tolerate inadvertent operator actions in the presence of any single system failure, ensuring that the system meets safety, reliability, and mission-critical standards.

Objective evidence is critical in proving compliance with this requirement. These tangible deliverables span system lifecycle stages—from requirements to training—to ensure that inadvertent operator commands and system failures are properly mitigated during operations. Collecting, documenting, and maintaining this evidence also reinforces accountability and supports future audits, validations, and safety certifications.

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

## 8.1 Categories of Objective Evidence

Below, the evidence is organized by key phases of the software engineering lifecycle, with specific examples for each category tailored to this requirement:

### 8.1.1 Requirements Evidence

Objective evidence from the requirements phase ensures traceability, completeness, and clarity in defining the feature of tolerating operator error during system failures.

1. **Requirements Documents**:

   * Software Requirements Specification (SRS), verified to explicitly address:
     + Tolerance for inadvertent operator actions.
     + Recovery mechanisms in the presence of single system failures.
   * Clearly traced safety-critical requirements linked to higher-level system requirements.
2. **Requirements Traceability Matrix (RTM)**:

   * Mapping between:
     + The requirements for fault tolerance and operator error handling, their implementation, and the associated test cases.
   * Evidence of system requirements flowing down to software-level requirements.
3. **Review Records**:

   * Records of peer reviews or walkthroughs of the SRS performed to verify that requirements related to inadvertent operator actions are:
     + Specific, measurable, achievable, relevant, and testable (SMART).
   * Evidence from defect tracking tools showing the resolution of gaps identified during reviews.

### 8.1.2 Design Evidence

The system’s design must show it accounts for the prevention, detection, and mitigation of inadvertent operator actions under failure scenarios.

1. **Software Design Specification (SDS)**:

   * Architectural evidence demonstrating:
     + Built-in command safeguards (e.g., multi-step confirmations, block mechanisms for invalid inputs).
     + Independence of redundant control strings.
     + Fault detection, isolation, and recovery (FDIR) mechanisms.
     + Graceful degradation strategies for handling failures while keeping the system operational.
2. **Interface Control Documents (ICDs)**:

   * Records showing clear command pathways to and from human-machine interfaces.
   * Evidence that safeguarding mechanisms in the interface design prevent mis-commands (e.g., warning prompts, input validation).
3. **Software Safety Analysis**:

   * Evidence of design adherence to safety-critical standards, including:
     + Hazard controls (e.g., redundancy, fail-safes).
     + Operator protections built into the system’s architecture.
4. **Review Artifacts**:

   * Records of Software Design Reviews (SDRs) verifying that the design includes mitigation strategies for risks related to inadvertent operator actions during component-level failures.

### 8.1.3 Code and Implementation Evidence

Completed and implemented code, aligned with safety and quality standards, demonstrates that the system meets its design goals.

1. **Source Code Artifacts**:

   * Source code implementing:
     + Multi-layered operator protections for high-risk commands.
     + Error and input validation modules ensuring that faulty commands cannot be executed during degraded states.
     + Backup system activation logic for redundant control paths.
2. **Static Analysis Reports**:

   * Results from automated tools (e.g., for static and dynamic analysis) showing:
     + Errors, warnings, and resolved defects related to safety-critical components.
     + Code logic to handle fault detection and operator error cases.
   * Evidence that safety-critical components meet the defined coding standards (e.g., cyclomatic complexity thresholds ≤ 15).
3. **Peer Review Records**:

   * Documentation from peer reviews showing the source code is reviewed to verify:
     + Operator error safeguards are properly implemented.
     + Defensive coding techniques have been applied to prevent cascading failures.

### 8.1.4 Testing and Validation Evidence

Testing evidence proves that the system tolerates operator error during a single system failure through simulation, analysis, and results.

1. **Test Plans and Procedures**:

   * Comprehensive system and software test plans addressing:
     + Normal operations.
     + Scenarios combining inadvertent operator actions and single system failures.
     + Edge cases for simultaneous operator-induced errors and fault recovery.
2. **Test Reports**:

   * Reports from validation and verification (V&V) tests proving:
     + The system prevented hazardous outcomes resulting from operator mistakes during degraded states.
     + FDIR mechanisms activated within time-to-event limits to avoid cascading hazards.
3. **Simulations and Fault Injection Records**:

   * Results from conducted simulations and fault recovery tests demonstrating:
     + Operator errors and hardware/software faults were injected to rule out potential risk scenarios.
     + Fault containment and recovery mechanisms successfully restored safe functionality.
4. **Test Witness Statements**:

   * Witness signatures and checklists proving safety-critical tests, including those for inadvertent operator action scenarios, were observed and verified by Assurance Engineers.
5. **Test Coverage Metrics**:

   * Data showing:
     + Coverage of safety-critical code under failure/command error tests.
     + Overall testing confidence levels (e.g., 100% functional coverage for safety-critical paths).

### 8.1.5 Safety and Hazard Analysis Evidence

Demonstrate that safety-critical hazards related to operator actions, single system failures, and their interplay have been analyzed and mitigated.

1. **Hazard Reports and Logs**:

   * Hazard reports documenting:
     + Identification of hazards stemming from inadvertent operator actions and overlapping hardware/software faults.
     + Mitigations tied to each identified risk.
2. **Hazard Analyses Outputs**:

   * Artifacts from Fault Tree Analysis (FTA) and Failure Modes and Effects Analysis (FMEA) showing:
     + Identification of operator error-induced hazards.
     + Controls for fault conditions that could coincide with an inadvertent command.
3. **Safety Review Records**:

   * Documentation of safety reviews verifying that:
     + All identified hazards have corresponding mitigations.
     + Actions were taken to resolve safety-critical risks.

### 8.1.6 Configuration Management Evidence

Provides assurance that all software artifacts are controlled, valid, and traceable.

1. **Configuration Management Records**:

   * Evidence of proper version control for modules implementing safeguards (e.g., command validation, redundancy handling).
   * Audit trails validating that updates to safety-critical code were tracked and documented.
2. **Version Lists**:

   * Verified lists of software and hardware versions used during testing to ensure consistency with delivered systems.

### 8.1.7 Training and Documentation Evidence

Documentation related to operator training and user guidance ensures operators understand the safeguards and recovery procedures.

1. **User Manuals**:

   * Manuals containing:
     + Clear instructions for approving commands and interpreting warnings.
     + Recovery procedures to address inadvertent actions during single failure scenarios.
2. **Training Records**:

   * Evidence of training conducted for operators, focusing on how to manage inadvertent actions and recover mis-commands during system faults.

### 8.1.8 Independent Verification and Validation (IV&V) Evidence

IV&V records offer additional assurance of system compliance and robustness.

1. **IV&V Test Reports**:

   * Reports from independent tests validating that the system tolerates all inadvertent operator error scenarios combined with hardware/software faults.
2. **IV&V Review Participation Records**:

   * Evidence of IV&V involvement in design reviews, test witnessing, and analysis of safety results.
