# HR-35 - Mitigate Hazardous Behavior Of Critical Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 167805151. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805151/HR-35+-+Mitigate+Hazardous+Behavior+Of+Critical+Software

HR-35 - Mitigate Hazardous Behavior Of Critical Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805151/HR-35+-+Mitigate+Hazardous+Behavior+Of+Critical+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=167805151)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=167805151&showCommentArea=true&showComments=true#addcomment)

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

4.3.5 The space system shall provide the capability to mitigate the hazardous behavior of critical software where the hazardous behavior would result in a catastrophic event.

## 1.1 Notes

According to current software standards, the software system will be designed, developed, and tested to:

1. Prevent hazardous software behavior.
2. Reduce the likelihood of hazardous software behavior.
3. Mitigate the negative effects of hazardous software behavior.

However, for complex software systems, it is very difficult to definitively prove the absence of hazardous behavior. Therefore, the crewed system has the capability to mitigate this hazardous behavior if it occurs. The mitigation strategy will depend on the phase of flight and the time to effect of the potential hazard. Hazardous behavior includes erroneous software outputs or performance.

## 1.2 History

Click here to view the history of this requirement: HR-35 History

HR-35 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.3.5 The space system shall provide the capability to mitigate the hazardous behavior of critical software where the hazardous behavior would result in a catastrophic event. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

For complex software systems, it is very difficult to definitively prove the absence of hazardous behavior and anticipate all circumstances, and studies have shown historical reoccurrence of software performing unexpectedly in flight. Therefore, the crewed system should both be developed with best practices to minimize the chances of software/automation errors, but also mitigate this hazardous behavior should it occur during flight in line with basic fault tolerance. The mitigation strategy will depend on the phase of flight and the time to affect the potential hazard. Hazardous behavior includes erroneous software outputs, poor performance, or ceasing to operate.

This requirement ensures that space systems operate safely and reliably by addressing one of the highest risks in software engineering for safety-critical systems: **hazardous behaviors in critical software that can lead to catastrophic events.** It emphasizes the need to implement mechanisms that predict, detect, prevent, and mitigate hazardous software behaviors that could cause loss of life, mission failure, or destruction of assets.

This requirement is critical to the safety, reliability, and resilience of space systems. By providing strong capabilities to mitigate hazardous software behavior, this requirement ensures that potential catastrophic events are averted—preserving mission success, protecting human lives, and safeguarding invaluable space assets. This requirement also aligns with NASA’s standards for developing and operating safety-critical software systems essential to achieving mission goals.

## 2.1 Key Concepts and Rationale

### 2.1.1 Critical Software Hazard Risk

Space systems rely heavily on software to control critical functions such as propulsion, navigation, life support, and communication. Failures or hazardous behaviors in these software components can result in catastrophic outcomes. Hazardous software behaviors include:

* Miscalculations in trajectory leading to collisions or loss of orbit.
* Incorrect or unsafe command execution, such as unintended engine shutdowns.
* System lockups or unresponsiveness during critical mission phases.
* Corruption of sensor data leading to faulty decisions.

This requirement recognizes that while preventing all software defects may be unrealistic, it is essential to **mitigate the effects of hazardous behaviors** when they manifest.

### 2.1.2 Catastrophic Event Avoidance

A catastrophic event is defined by NASA as one resulting in **loss of life, permanent disability, loss of a spacecraft or a mission, or significant damage to facilities or the environment.** Critical software directly controls or influences hardware systems where even a minor error can escalate into catastrophic outcomes.

* This requirement ensures that the system does not rely solely on **defensive coding or perfect design** but also provides **safeguards and fallback mechanisms** to address potential hazardous scenarios.

### 2.1.3 High Complexity of Critical Software

Software controlling space systems is inherently complex due to:

* Interaction with unpredictable environmental conditions (e.g., radiation, solar storms).
* Constrained computational resources on spacecraft.
* Real-time decision-making requirements in safety-critical moments.

The nature of this complexity makes it possible for rare, unforeseen hazardous behaviors to arise in critical software. Therefore, this requirement ensures that mitigation capabilities are inherent in the system design to address these complexities systematically.

### 2.1.4 Single Points of Failure

Critical software often interacts with single points of failure in the system, such as:

* Thruster control systems for orbital adjustments.
* Power management systems ensuring functionality during critical phases.
* Fault detection and recovery systems themselves (e.g., watchdog timers).

Without proper safeguards, hazardous software behaviors could propagate through these single points of failure, **compounding risks.** This requirement mandates software-driven mitigation strategies (such as redundancy and fault isolation) to ensure catastrophic events do not materialize.

### 2.1.5 Need for Resilience and Reliability

Space systems must meet **mission assurance objectives** by:

* Surviving unexpected environmental conditions.
* Completing critical objectives within tightly constrained timelines and resources.

This resilience depends on the ability to:

* Contain software faults and prevent their propagation.
* Recover the system to a safe or operational state after hazardous software is detected.

This requirement ensures that critical software is equipped to handle "what if" failure scenarios that could arise from design oversights, rare inputs, or hardware constraints.

### 2.1.6 Aligned with NASA Safety Standards

The rationale for this requirement stems from and aligns with NASA’s safety and assurance standards, including:

* **NASA-STD-8739.8 [278](#_tabs-<p></p>)** (*Software Assurance and Software Safety Standard*): Requires that all safety-critical software includes provisions for fault detection, isolation, mitigation, and/or recovery.
* **NPR 8715.3**  (*NASA General Safety Program Requirements*): Establishes software as a primary driver in maintaining safe operations in hazardous environments.
* **NPR 7150.2** [083](#_tabs-<p></p>) (*NASA Software Engineering Requirements*): Defines measures for identifying and controlling safety-critical software functionality, particularly in catastrophic event scenarios.

The implementation of this requirement ensures compliance with these overarching safety standards.

## 2.2 Scenarios Supporting the Rationale

1. **Thruster Control Malfunction**:

   * Hazard: A bug in the logic controlling thruster firings causes unplanned maneuvers during orbital insertion.
   * Catastrophic Consequences: Colliding with planetary bodies, losing orbit, or depleting fuel reserves.
   * Mitigation: Include software redundancy, safeguards (limits to thruster firings), and autonomous shutdown before catastrophic events occur.
2. **Sensor Data Corruption**:

   * Hazard: Faulty sensor data, combined with poor error handling, leads to incorrect navigation decisions.
   * Catastrophic Consequences: Deviations result in an unrecoverable trajectory, system destruction, or mission failure.
   * Mitigation: Implement robust software validation of sensor data, automated fault detection, and fault-tolerant algorithms to reroute or switch to alternative sensors.
3. **Software Deadlock**:

   * Hazard: A multitasking program locks critical operations (e.g., power redistribution logic freezes during eclipse survival mode).
   * Catastrophic Consequences: Loss of power leads to permanent damage to the spacecraft, jeopardizing the mission.
   * Mitigation: Enforce watchdog timers, heartbeat signals, or automatic restart/reboot strategies to recover from deadlock situations.
4. **Command Execution Error**:

   * Hazard: Critical software misinterprets a ground command due to a mismatch in command parameters.
   * Catastrophic Consequences: Overwrites mission data, renders a key subsystem inoperable, or disables redundancy during critical phases.
   * Mitigation: Implement software safeguards to block invalid or incomplete commands and notify operators immediately.

## 2.3 Approach to Meeting the Requirement

To meet this requirement, mitigation capabilities must be embedded in the software design and development lifecycle:

1. **Risk Identification and Hazard Analysis**:

   * Use techniques such as Fault Tree Analysis (FTA) and Failure Modes and Effects Analysis (FMEA) to identify potential hazardous software behaviors.
2. **Mitigation Mechanisms**:

   * Include automated software mechanisms, such as:
     + **Error Detection and Recovery (EDR)**: Automatically detect anomalies and recover from faults.
     + **Redundancy Managers**: Maintain alternate control paths or backup systems for safety-critical operations.
     + **Safe State Control**: Transition the system to a safe mode when hazards are detected.
3. **Verification and Validation**:

   * Thoroughly simulate and test scenarios where hazardous software behaviors could result in catastrophic events.
   * Develop and test recovery workflows for worst-case scenarios.
4. **Operator Feedback**:

   * Ensure the system provides meaningful diagnostics, alerts, or intervention capabilities for operators to intervene or manage hazardous software behavior.
5. **Defensive Coding Techniques**:

   * Incorporate practices to prevent latent defects (e.g., input validation, error trapping, and fail-safes).

## 2.4 Consequences Without the Requirement

Failing to provide mitigation capabilities for hazardous software behavior increases the risk of catastrophic events, such as:

* Loss of life or injury to astronauts or ground personnel.
* Mission failure due to unrecoverable software logic issues.
* Loss of multi-million or multi-billion-dollar assets, affecting program credibility and future funding.
* Irreversible environmental impacts (e.g., collisions with planetary bodies or space debris generation).

# 3. Guidance

This guidance strengthens the original practices and incorporates deeper strategies to align with current best practices, ensure compliance with NASA standards, and address the challenges of mitigating hazardous software behavior in space systems.

This revised guidance solidifies the software engineering principles necessary to meet the requirement. By utilizing best practices from NPR 7150.2, leveraging robust analysis and validation techniques, and incorporating defensive and resilient software design, the system can mitigate risks associated with hazardous software behavior. This ensures a safer, more reliable software architecture capable of preventing catastrophic outcomes in flight and improving success rates for mission-critical operations.

## 3.1 General Software Engineering Strategy

1. **Prevention (Pre-flight Phase)**:

   * Design, develop, and rigorously test software to reduce the likelihood of hazardous behavior.
   * Focus on proactive analysis, robust design principles, and stringent verification and validation (V&V) to identify and address risky scenarios prior to deployment.
2. **Mitigation (In-flight Phase)**:

   * Implement fail-safe mechanisms, error detection and recovery systems, and fallback strategies to minimize the risks and consequences of hazardous behavior in critical software during operations.
   * Build robust fault tolerance into the software to ensure ongoing system functionality without jeopardizing mission objectives or safety.
3. **Resilience**:

   * Plan for partial or degraded scenarios by designing systems to remain operational with a controlled fallback or safe mode during anomalous events.
   * Incorporate human-automation teaming to enable operators to identify and mitigate software-induced hazards during critical mission operations.

## 3.2  Challenges of Hazard Mitigation in Complex Software

While it is difficult to definitively prove the absence of hazardous software behavior during development, **evidence-based engineering and mitigation practices** ensure that the system is robust against unforeseen events:

* Acknowledge the recurrence of unexpected software behavior in historical spaceflight events.
* Minimize the likelihood of latent faults emerging by utilizing advanced validation techniques, extensive testing, and mitigation strategies.
* Implement best practices like those in **NPR 7150.2** while preparing for contingencies during flight with adaptive software design and fail-safe measures.

## 3.3 Software Engineering Tasks to Mitigate Hazardous Behavior

To mitigate potential hazards caused by critical software, the following tasks should be carried out:

### **3.3.1** Hazard **Analysis (Prevention and Mitigation Phases)**

1. **Comprehensive Hazard Identification**:

   * Identify and document all potential hazards arising from both software behavior (e.g., failure to perform, erroneous actions) and hardware-software interactions.
   * Account for both **active failures** (e.g., erroneous output) and **passive failures** (e.g., software ceases operation).
2. **Integration with Human Factors**:

   * Evaluate human-machine interfaces to identify inadvertent operator actions that could interact with hazardous software behaviors.
   * Integrate mitigations (e.g., procedural or design-based) for operator involvement in risky scenarios.
3. **Refine Mitigation Areas**:

   * Focus on areas where coding or procedural mitigations can prevent hazardous events, such as:
     + Automated recovery strategies.
     + Clear boundaries for restricting cascading software faults.

### 3.3.2 Safety Analysis Techniques

1. **Utilize Advanced Analytical Models**:

   * Fault Tree Analysis (FTA): Identifies hazardous conditions and their triggering faults.
   * Software Failure Modes and Effects Analysis (SFMEA): Evaluates how faults propagate through the software and their impact on system functions.
   * Hazard Analysis and Critical Control Points (HACCP): Provides checkpoints for mitigating hazardous scenarios.
2. **Layered Controls**:

   * Ensure redundancy and robustness at both the system and software levels.
   * Combine software controls with hardware interlocks (if applicable) to further contain risks.

### 3.3.3 Safety Reviews

* Conduct software safety reviews **early and iteratively**. Involve subject-matter experts, system engineers, software developers, and operators to:
  + Assess risk with every software update, configuration change, or defect fix.
  + Confirm that modifications do not compromise previously validated hazard mitigations.

### 3.3.4 Safety-Critical Software Requirements

1. **Precise Specification and Implementation**:

   * Ensure that critical software explicitly adheres to requirements in **NPR 7150.2** and flows down from hazard analyses.
   * Implement and verify requirements for:
     + Boundary conditions handling.
     + Safe state transitions.
     + Controlled shutdown or fallback mechanisms to mitigate catastrophic consequences during failures.
2. **Automated Safeguards and Built-In Integrity Checks**:

   * Input/output validation.
   * Pre-condition checks for all safety-critical commands.
   * Hard stops or warning prompts for commands with catastrophic potential.

### 3.3.5 Error Handling and Recovery Mechanisms

1. **Robust Error Detection and Recovery**:

   * Implement automated detection mechanisms for anomalous states, with real-time recovery logic.
   * Examples:
     + Heartbeat signals to detect "silent failures."
     + Default system resets (if safe) after a predetermined timeout.
2. **Built-In Redundancies**:

   * Provide alternate paths or fallback operations for key functions to ensure continuity.
   * Use **graceful degradation** to ensure critical operations can still function at reduced capacity.

### 3.3.6 Simulations and Testing

1. **Scenario-based Testing**:

   * Develop test cases reflecting **nominal, off-nominal, and fault-injected operational scenarios** to verify fault tolerance mechanisms.
   * Use simulations to replicate worst-case interactions between software faults and physical systems.
2. **Stress and Boundary Testing**:

   * Test system performance under extreme input conditions to detect potential flaws.
   * Verify safe handling of boundary states, edge cases, and rare fault conditions.
3. **Test Campaign Objectives**:

   * Validate that error-handling procedures do not conflict with existing functionality.
   * Ensure safe transitions to pre-defined states in case of fault detection.
   * Certify **time-to-mitigation** aligns with the hazard's time-criticality.

### 3.3.7 Code Coverage

1. **MC/DC (Modified Condition/Decision Coverage)**:

   * Ensure every condition in a decision structure independently affects the decision outcome.
   * Achieve **100% test coverage** of safety-critical software components where feasible.
2. **Risk-Based Justifications**:

   * Document reasonable and technically supported exceptions for unachievable test coverage, with alternative risk-mitigation measures implemented.

### 3.3.8 Independent Verification and Validation (IV&V)

1. **Early Engagement in Life Cycle**:

   * IV&V participants should evaluate safety-critical requirements, designs, and hazard mitigations at all stages.
2. **Focus Areas**:

   * Functional validation of error-handling procedures.
   * Risk evaluations for safety-control efficacy and software interactions with other subsystems.
3. **Comprehensive Review Participation**:

   * IV&V participation in peer reviews, verifications, and technical assessments to uncover gaps.

### 3.3.9 Safety-Critical Software Design

1. **Input/Output Integrity**:

   * Verify that inputs and outputs within safety-critical routines are:
     + Validated.
     + Error-trapped.
     + Logged for traceability and diagnosis.
2. **State Transitions**:

   * Implement:
     + Controlled transitions between operational and fail-safe modes.
     + Safeguards to prevent hazardous states during transient faults.

## 3.4 Other Important Practices

1. **Configuration Management**:

   * Use version controls and baselines for all updates to track and validate safety-critical components.
   * Prevent deployment of unapproved or unverified modifications.
2. **Training and Documentation**:

   * Provide **clear guidance** to operators and flight teams, including:
     + Hazard recovery steps.
     + Anomalous behavior diagnostics.
   * Update manuals as system changes are integrated.

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Requirements related to Human Rated Software.

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

Small projects often face resource and time constraints that require a tailored, streamlined approach to meet safety requirements. This guidance is designed to help small projects implement practices for mitigating hazardous software behavior efficiently while satisfying NASA’s software engineering and safety standards.

## 4.1 Key Principles for Small Projects

1. **Prioritize Critical Risks**:

   * Focus on identifying and mitigating the software functionality with the **greatest potential for catastrophic outcomes**.
   * Use a risk-based approach to allocate resources to safety-critical software components only.
2. **Streamlined Activities**:

   * Combine or simplify processes where feasible (e.g., integrating hazard analysis with software requirements development).
   * Scale processes to match the complexity of the system and the project.
3. **Leverage Existing Tools and Resources**:

   * Use existing software templates, checklists, automated tools, and processes to reduce development overhead.
   * Collaborate with subject-matter experts and reuse validated safety artifacts or patterns when applicable.
4. **Iterative Development**:

   * Incrementally develop, test, and validate software features, focusing on early identification of safety risks.
   * Avoid deferring safety considerations until late in the project life cycle.
5. **Fully Utilize Independent Verification and Validation (IV&V)**:

   * Small projects should leverage IV&V selectively, targeting **safety-critical areas only** for independent review and validation.

## 4.2 Stepped Guidance for Small Projects

### 4.2.1 Planning and Requirements

1. **Identify Safety-Critical Software**:

   * Use checklists and simple Failure Modes and Effects Analysis (FMEA) to:
     + Identify software components that directly control or influence safety-critical features.
     + Identify scenarios where hazardous software behavior might lead to catastrophic consequences (e.g., loss of mission, fatal injury, or unrecoverable system failure).
2. **Document Requirements**:

   * Develop clear, concise safety-critical software requirements. Examples:
     + *“The software shall detect and terminate infinite loops after one second.”*
     + *“The software shall revert to a safe state if an erroneous command is received while the system is in degraded power mode.”*
3. **Integrate Hazard Analysis into Requirements**:

   * For a small project, include hazard mitigation considerations directly in the Software Requirements Specification (SRS).
   * Trace each hazard to one or more software safety-critical requirements.

### 4.2.2 Design

1. **Simplify the Design**:

   * Use well-established, deterministic design patterns that reduce complexity in safety-critical systems. Examples:
     + Watchdog timers for detecting hung processes.
     + Precondition checks for inputs before executing safety-critical commands.
2. **Safety Mitigations**:

   * For small projects, build the following simple but effective mitigations into the design:
     + **Safe State Transitions**: Create a predefined "safe mode" or degraded state the system can default to during faults.
     + **Isolation of Critical Functions**: Keep safety-critical components independent of non-critical functions (e.g., use separate threads, modules, or subsystems for critical software).
3. **Human-In-The-Loop (HITL) Design**:

   * For systems with operators, include clear recoverable controls, prompts, or warnings for hazardous situations.
4. **Use Redundancy** (if feasible):

   * For small projects, redundancy can be "logical" (e.g., multiple verification layers for the same input) rather than requiring complex hardware redundancy.

### 4.2.3 Implementation

1. **Adopt Defensive Coding Practices**:

   * Use coding standards designed for critical systems (e.g., MISRA or NASA coding standards).
   * Defensive methods should include:
     + Input validation (e.g., range checks on all inputs).
     + Output verification (e.g., ensuring critical outputs conform to predefined limits).
     + Exception handling for failure scenarios.
2. **Cyclomatic Complexity Management**:

   * Keep cyclomatic complexity of safety-critical code below **15** wherever possible; for small projects, complexity reduction can significantly ease testing and maintenance.
   * If exceeding this threshold, document why and perform additional focused reviews and tests for high-complexity modules.
3. **Logging and Diagnostics**:

   * Add lightweight logging for debugging and post-failure analysis. Ensure logs are structured to help understand what caused any hazardous behavior.

### 4.2.4 Testing and Validation

1. **Test Safety-Critical Behavior First**:

   * Focus initial testing on the pathways or operations where failure could lead to catastrophic events.
   * Prioritize:
     + Nominal cases (e.g., correct operation).
     + Off-nominal scenarios (e.g., unexpected inputs).
     + Stress or boundary conditions.
2. **Simulations and Fault Injection**:

   * Run simplified fault injection tests (e.g., introducing corrupted sensor data, simulating timing delays) to verify recovery mechanisms.
3. **Code Coverage Analysis**:

   * Aim for 100% **Modified Condition/Decision Coverage (MC/DC)** for safety-critical code.
   * For resource-constrained projects, document untested areas and their associated mitigation rationale (e.g., redundancy).
4. **Automated Testing**:

   * Use automated unit and integration testing tools to minimize human error and quickly identify defects. Open-source testing frameworks (e.g., Google Test or NUnit) can reduce costs.

### 4.2.5 Configuration Management

1. **Version Control for All Safety-Critical Components**:

   * Use a version control system (e.g., Git) for code, requirements, and test cases.
   * Maintain baselines of all tested and approved versions.
2. **Change Control Process**:

   * For safety-critical software, ensure that **no changes are implemented without review and approval**, even in a small team.

### 4.2.6 Independent Verification and Validation (IV&V)

1. **Selective IV&V Engagement**:

   * Focus IV&V efforts on the highest-risk areas of the software, such as:
     + Critical control loops.
     + Fault-detection mechanisms.
     + Safe mode transitions.
2. **IV&V Participation in Key Reviews**:

   * Include IV&V in at least two core stages:
     + Requirements/design peer review.
     + Final test result review (to confirm mitigation strategies are effective).

### 4.2.7 Training and Documentation

1. **Operator Procedures**:

   * Provide **simple operational instructions** to the ground/flight team to reduce operator failures during software anomalies:
     + Include checklists for recovery from hazardous behavior.
     + Provide clear error logs and status messages for troubleshooting.
2. **Safety Documentation**:

   * Document all assumptions, hazards, and safety-critical requirements alongside mitigations.
   * Consolidate information in a **User Manual** or **Software Safety Handbook** to support future system upgrades or reuse.
3. **Training**:

   * Conduct operator training that simulates recovery from hazardous software conditions. This could involve basic failure-mode rehearsals for critical mission phases.

## 4.3 Deliverables for Small Projects

Even small projects need to produce essential artifacts to demonstrate compliance with Requirement 4.3.5. Key deliverables include:

1. Hazard Report: Lists all potential software hazards, mitigations, and links to safety requirements.
2. Software Requirements Traceability Matrix (RTM): Maps hazards and mitigations to the implemented software functions and test cases.
3. Simulation/Test Results: Demonstrates that hazardous behaviors are identified, tested, and mitigated.
4. Safety Manual: Outlines operator instructions and recovery procedures.

## 4.4 Scalable Strategies for a Small Project

By tailoring the practices above to small project constraints, teams can minimize overhead while ensuring safety. Proper automation, simplicity in design, and a focus on testing safety-critical paths early will help small projects efficiently mitigate hazardous software behavior and maintain alignment with NASA safety standards like **NPR 7150.2** and **NPR 8715.3**.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-458)

  [NASA Technical Requirements for Human-Rating](https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/0/NASA-STD-871929-Baseline-draft.pdf "Click to open in new window")

  NASA-STD-8719.29, National Aeronautics and Space Administration, Approved:2023-12-11 Baseline,  This standard establishes technical requirements necessary to produce human-rated space
  systems that protect the safety of the crew and passengers on NASA space missions
* (SWEREF-596)

  [Software Error Incident Categorizations in Aerospace](https://arc.aiaa.org/doi/10.2514/1.I011240 "Click to open in new window")

  Prokop, Lorraine, JAIS, Vol. 21, No. 10 (2024), pp. 775-789 doi: doi/abs/10.2514/1.I011240.
* (SWEREF-606)

  [Historical Aerospace Software Errors Categorized to Influence Fault Tolerance](https://ntrs.nasa.gov/citations/20230012909 "Click to open in new window")

  Prokop, Lorraine, AIAA Aerospace Conference 2024, March 2024,
* (SWEREF-607)

  [Software Error Incident Categorizations in Aerospace](https://ntrs.nasa.gov/citations/20230012154 "Click to open in new window")

  Prokop, Lorraine, NASA Technical Publication,  NASA/TP−20230012154.  August 2023.
* (SWEREF-687)

  [NESC Technical Bulletin 23-06: Considerations for Software Fault Prevention and Tolerance](https://ntrs.nasa.gov/api/citations/20230013383/downloads/TB23%2006%20Software%20Errors%20FINAL%20091923.pdf "Click to open in new window")

  NASA Engineering and Safety Center, Lorraine Prokop, 09/19/23,

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA has faced numerous challenges related to hazardous software behaviors in its missions, some of which have led to catastrophic events or near-misses. These lessons learned, derived from historical missions, accidents, and post-flight analyses, provide valuable insights for implementing this requirement. Incorporating these lessons into small and large projects will help mitigate risks, increase system safety, and improve mission outcomes.

---

### **Relevant NASA Lessons Learned**

The following lessons are directly tied to hazardous behavior in software and its mitigation strategies within space systems. The authoritative sources include NASA's **Lessons Learned Information System (LLIS)**, reviews of mission failures, and safety investigations.

---

### **1. Mars Climate Orbiter Loss Due to Software Error**

**Incident Summary**:  
In 1999, the Mars Climate Orbiter mission failed when the spacecraft entered the Martian atmosphere at the wrong trajectory due to a software-related issue involving unit mismatches (imperial versus metric). The error originated from inconsistent software inputs during orbital insertion calculations.

**Lesson Learned**:

* *“Integration testing must verify that all software components correctly validate and process inputs, especially for safety-critical system calculations.”*
* **Relevance** to Requirement 4.3.5:
  + Critical software must include checks for input validation, preventing hazardous errors during key mission phases like orbital maneuvers.
  + Mitigation strategies should include exception handling or fallback logic when receiving invalid inputs.

---

### **2. Ariane 5 Flight 501 Failure**

**Incident Summary**:  
In 1996, the Ariane 5 rocket failed during launch due to a software exception in a reused inertial reference system module. The software attempted to write out-of-bound data, causing an unhandled exception, which led to a catastrophic flight termination.

**Lesson Learned**:

* *“Reused software must be reevaluated under new operational conditions, including environmental changes introduced by system upgrades.”*
* **Relevance** to Requirement 4.3.5:
  + Hazard analysis and testing must account for environmental differences when reusing software in new systems.
  + Implement robust error handling to recover from exceptions without cascading catastrophic failures.

---

### **3. Apollo 11 Lunar Module Guidance System Reset**

**Incident Summary**:  
During Apollo 11’s lunar descent, the onboard computer (AGC) experienced overruns due to unanticipated input tasks competing for system resources. Despite the erroneous behavior, the mission was saved by built-in safeguards that allowed the software to prioritize safety-critical tasks while ignoring non-essential ones.

**Lesson Learned**:

* *“Safety-critical software must prioritize essential functions during fault conditions, enabling degraded operations instead of catastrophic failure.”*
* **Relevance** to Requirement 4.3.5:
  + Design software to operate under **graceful degradation** during hazardous conditions.
  + Mitigation strategies should include task prioritization at runtime, ensuring essential functions are preserved.

---

### **4. Space Shuttle Challenger Disaster**

**Incident Summary**:  
While primarily caused by hardware issues (O-ring failure), software played an indirect role by failing to properly monitor and flag hazardous pre-launch conditions. Pressure sensor data during ignition was not utilized effectively to halt the launch.

**Lesson Learned**:

* *“Critical software must account for monitoring all relevant real-time data and provide clear indicators of safety concerns to human operators.”*
* **Relevance** to Requirement 4.3.5:
  + Include software monitoring capabilities with sensor validation and operator feedback mechanisms to flag hazardous conditions.
  + Build warning and diagnostic subsystems to signal hardware-software interactions that may lead to unsafe behavior.

---

### **5. Mars Polar Lander Loss**

**Incident Summary**:  
In 1999, Mars Polar Lander was destroyed during its entry, descent, and landing phase when premature engine cutoff occurred due to a software misinterpretation of sensor data. The software erroneously concluded that the spacecraft had landed while it was still in free fall.

**Lesson Learned**:

* *“Error detection mechanisms should cross-verify critical decision points with redundant data sources to avoid single points of software failure.”*
* **Relevance** to Requirement 4.3.5:
  + Implement redundancy in critical sensors and software validation mechanisms to cross-check decisions that may lead to catastrophic consequences.
  + Apply bounds-checking and data consistency logic to mitigate hazardous interpretations.

---

### **6. Genesis Capsule Crash**

**Incident Summary**:  
In 2004, the Genesis capsule carrying solar wind samples crashed upon its return to Earth due to software faults that failed to deploy its parachute system. The faulty logic bypassed key commands during re-entry, directly contributing to the catastrophic failure.

**Lesson Learned**:

* *“Safety-critical software logic should include fallback scenarios for mission-critical hardware commands, such as parachute deployment or thruster activation.”*
* **Relevance** to Requirement 4.3.5:
  + Design software logic with fallback provisions to execute backup commands or enter safe modes when primary operations fail.

---

### **7. Helios Prototype Aircraft Loss**

**Incident Summary**:  
The Helios Prototype Aircraft disintegrated in 2003 when software controlling the stability subsystem failed to account for extreme environmental conditions (high winds). Hazardous behavior escalated due to the software’s inability to recover from destabilization.

**Lesson Learned**:

* *“Software must include environmental fail-safes and operate effectively under off-nominal conditions.”*
* **Relevance** to Requirement 4.3.5:
  + Develop software fail-safes that respond to adverse environmental interactions, such as extreme weather or system stress.

---

### **8. Software Issues on the International Space Station (ISS)**

**Incident Summary**:  
Over various expeditions, the ISS experienced multiple software anomalies, including command delays, conflicting software inputs, and unresponsive systems. Fortunately, redundancy and manual interventions prevented catastrophic outcomes.

**Lesson Learned**:

* *“Human-automation collaboration systems must account for operator inputs to bypass hazardous software behavior during critical operations.”*
* **Relevance** to Requirement 4.3.5:
  + Design HITL (Human-In-The-Loop) mechanisms to allow operators to override hazardous software behaviors and manually control critical functions.

---

### **Best Practices Emerging from NASA Lessons Learned**

#### **Hazard Analysis and Mitigations**

* Conduct thorough hazard analyses using tools like **Fault Tree Analysis (FTA)** and **Failure Modes and Effects Analysis (FMEA)** to identify software risks early. Ensure failure tolerance provisions are linked to mitigation strategies.

#### **Redundancy**

* Implement redundancy in hardware and software to reduce reliance on single points of failure. Example: Dual data validation systems integrating secondary sensor feedback.

#### **Fail-Safe Mechanisms**

* Design software fail-safes that allow for safe mode transitions and recovery procedures to limit catastrophic consequences during hazardous behavior.

#### **Operator Feedback and Training**

* Ensure software provides clear error diagnostics and warnings to operators to help them identify and mitigate hazards in real time. Include operator training as part of hazard mitigation planning.

#### **Iterative Testing**

* Simulate fault-injection scenarios with degraded inputs and failure conditions to verify mitigation capabilities. Incorporate off-nominal and boundary tests in safety-critical test campaigns.

#### **Configuration Management**

* Maintain consistent software versions, ensure traceability, and document all software changes systematically to minimize risk during modifications.

---

### **Conclusion**

NASA’s lessons learned underscore the criticality of designing and verifying software to lead with **preventive measures, robust error-handling mechanisms, redundancy, operator control capabilities, and safe fallback modes**. Incorporating these lessons into small and large projects ensures that systems are equipped to mitigate hazardous behaviors before they escalate into catastrophic events, protecting lives, mission assets, and scientific objectives.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-35 - Mitigate Hazardous Behavior Of Critical Software**

4.3.5 The space system shall provide the capability to mitigate the hazardous behavior of critical software where the hazardous behavior would result in a catastrophic event.

This expanded guidance strengthens NASA’s assurance process by providing detailed steps, product expectations, and metrics that integrate seamlessly into projects aimed at mitigating critical software hazards. By aligning with NASA standards, leveraging real-world lessons learned, and prioritizing validation at every stage, this guidance ensures the safety-critical functionality of space systems with optimized software safety practices.

## 7.1 Tasking for Software Assurance

1. Confirm that the hazard reports or safety data packages contain all known software contributions or events where software, either by its action, inaction, or incorrect action, leads to a hazard.
2. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
3. Assess that hazard analyses (including hazard reports)identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
4. Confirm that the traceability between software requirements and hazards with software contributions exists.
5. Develop and maintain a software safety analysis throughout the software development life cycle.
6. Ensure that safety-critical software requirements are implemented per the NPR 7150.2 Requirements Mapping Matrix and tested or verified.
7. Perform or analyze Cyclomatic Complexity metrics on all identified safety-critical software components.
8. Confirm that all identified safety-critical software components have a cyclomatic complexity value of 15 or lower. If not, assure that software developers provide a technically acceptable risk assessment, accepted by the proper technical authority, explaining why the cyclomatic complexity value needs to be higher than 15 and why the software component cannot be structured to be lower than 15 or why the cost and risk of reducing the complexity to below 15 are not justified by the risk inherent in modifying the software component.
9. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.
10. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically the off-nominal scenarios to mitigate the impact of hazardous behaviors. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks.) Ensure that the project has developed and executed test cases to test the impact of hazardous behaviors.
11. Perform safety reviews on all software changes and software defects.
12. Perform test witnessing for safety-critical software to ensure the impact of hazardous behavior is mitigated.
13. Confirm that strict configuration management is maintained to ensure that the correct software versions and configurations are used.
14. Ensure comprehensive training and documentation for operators is available.

## 7.2 Software Assurance Products

This enhanced guidance streamlines and deepens the Software Assurance (SA) practices for mitigating hazardous software behavior in space systems. It emphasizes scalability for small and large projects, integrates lessons learned, and aligns with NASA-STD-8739.8, NPR 7150.2, and NASA’s systems engineering and safety standards. The goal is to ensure traceability, minimize risks, and verify robust mitigation strategies that support mission success.

### 7.2.1 Mandatory Software Assurance Deliverables

The following **artifacts** ensure a thorough assessment of safety and mitigation measures for hazardous software behavior:

1. **Software Assurance Status Reports (Ref:** [SWE-028 - Verification Planning](/pages/viewpage.action?pageId=102695283)**)**:

   * Regularly communicate the status of mitigation-related tasks, including identified issues, defect resolution progress, and recommendations for reducing risks.
2. **Software Requirements Analysis (Ref:** [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements)**,** [SWE-051 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695426/SWE-051+-+Software+Requirements+Analysis)**)**:

   * Document the analysis of all software requirements to validate traceability to system hazards and verify that each requirement includes mitigation strategies for hazardous behavior.
3. **Software Design Analysis (Ref:** [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability)**)**:

   * Evaluate whether the design incorporates required safety and reliability features, such as safe state transitions, redundancy, and error recovery mechanisms, specifically for hazardous behaviors.
4. **Source Code Quality Analysis (Ref:** [SWE-067 - Verify Implementation](/pages/viewpage.action?pageId=102695298)**,** [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)**)**:

   * Perform detailed reviews and analysis of the code to ensure:
     + Standards compliance.
     + Input/output integrity checks.
     + Low cyclomatic complexity (≤15 for safety-critical software).
5. **Testing Analysis (Ref:** [SWE-029 - Validation Planning](/pages/viewpage.action?pageId=102695284)**,** [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)**)**:

   * Assess test plans, procedures, and results to measure the adequacy of verification and validation for hazardous behavior mitigation.
6. **Software Safety and Hazard Analysis (Ref:** [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)**)**:

   * Continually evaluate hazards (independently and iteratively) throughout the software development life cycle. Ensure:
     + The software safety analysis maps hazards to mitigations.
     + All new requirements, design changes, and defects are analyzed for their hazard impact.
7. **Audit Reports (Ref:** [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes), [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items)**)**:

   * Provide detailed records from safety and configuration audits, specifically:
     + **Functional Configuration Audit (FCA)**: Verifies software capability against documented safety requirements.
     + **Physical Configuration Audit (PCA)**: Confirms the correct design and tested firmware/software baselines.
8. **Completed Hazard Analyses, Reports, and Mitigation Mapping (Ref:** [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)**)**:

   * A comprehensive report identifying:
     + Software hazards.
     + Traceability to mitigations implemented in software/system design.
     + Results from fault trees, failure modes, and effects analysis (FMEA).
9. **Code Coverage and Complexity Reports (Ref:** [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements)**)**:

   * Provide automated tool results for:
     + Code coverage criteria: 100% Modified Condition/Decision Coverage (MC/DC) for critical paths.
     + Cyclomatic complexity metrics, ensuring they meet safety-critical thresholds (e.g., ≤15, unless valid technical justifications exist).
10. **Automated Tool Analysis Reports (Ref:** [SWE-056 - Document Design](/pages/viewpage.action?pageId=102695292)**)**:

    * Provide detailed results from static analysis, dynamic analysis, and fault-injection tools. Reports should validate code correctness and system response under stress.
11. **Test Witnessing Signatures (Ref:** [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)**)**:

    * Ensure a certified witness verifies that all safety-critical test activities, including hazardous behavior scenarios, are conducted according to test plans.
12. **Traceability Matrices (Ref:** [SWE-064 - Bidirectional Traceability Between Software Design and Software Code](/pages/viewpage.action?pageId=102695295)**)**:

    * Deliver completed system-to-software traceability reports that map hazards, requirements, design, and verification test cases.
13. **User Manual Verification (Ref:** [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test)**)**:

    * Ensure operator documentation provides clear recovery procedures and lists mitigations for hazardous software conditions.

## 7.3 Metrics for Software Assurance in Hazard Mitigation

The following **Software Assurance Metrics** are essential to measure and monitor the effectiveness of efforts to mitigate hazardous software behavior and ensure safety-critical compliance:

### 7.3.1 Verification and Validation Metrics

1. **Test Coverage Metrics**:

   * Measure the proportion of safety-critical code and hazardous pathways exercised during testing.
   * For the most critical software, ensure:
     + 100% function test coverage.
     + 100% MC/DC test coverage.
2. **Defect Density**:

   * Track the number of defects discovered during testing per thousand lines of code (KLOC). Ensure defects found in safety-critical code are resolved immediately.
3. **Requirements Coverage and Traceability**:

   * Metric: % of safety-critical requirements traced to implementation and test cases.
   * Goal: 100% traceability across hazards, mitigations, and validations.
4. **Non-Conformances**:

   * Track the number of non-conformances related to hazardous behavior:
     + Identified during each testing phase.
     + Severity distribution (e.g., critical vs. minor).

### 7.3.2 Safety Metrics

1. **Hazard Analysis Compliance**:

   * Number of hazards requiring mitigations vs. hazards with complete software mitigations tested.
2. **Safety-critical Software Metrics**:

   * % of safety-critical requirements accepted through final verification.
   * % of safety-critical paths tested to mitigate risk.

### 7.3.3 Code Quality Metrics

1. **Cyclomatic Complexity**:

   * Objective: Ensure ≤15 for safety-critical software components unless documented rationale is provided.
   * Monitor the distribution of complexity values across modules.
2. **Code Churn**:

   * Measure frequent code modifications, as areas with high churn may affect safety-critical functions.

### 7.3.4 Performance Metrics

1. **Response Time**:

   * Time taken for the system to detect, respond, and mitigate hazardous software behavior.
   * Benchmark these times during FDIR (Fault Detection, Isolation, and Recovery) scenarios.
2. **System Uptime During Critical Phases**:

   * Measure availability of safety-critical systems during mission-critical windows.

### 7.3.5 Independent Verification and Validation (IV&V) Metrics

1. **IV&V Coverage**:

   * Percentage of safety-critical software components independently verified.
   * Focus on highly critical test cases and peer-reviewed findings.
2. **IV&V Action Items**:

   * Track number of findings raised and addressed by IV&V teams.

### 7.3.6 Configuration Management Metrics

1. **Audit Counts**:

   * Track the number of configuration management audits conducted, completed, and with findings resolved.
2. **Version Control Stability**:

   * Track metrics for changes to key safety-critical components, including frequency and state upon deployment.

## 7.4 Software Assurance Guidance

#### **Core Software Assurance Tasks for Mitigating Hazardous Behavior**

1. **Software Safety and Hazard Analysis**:

   * Ensure each hazard analysis prioritizes traceability, identifying both functional controls and software mitigations for catastrophic hazards.
   * Update analyses throughout the lifecycle to ensure all new features or defect fixes meet safety needs.
2. **Configuration Management (CM)**:

   * Strictly implement [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) and [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items), ensuring:
     + All tested configurations are documented.
     + All safety-related items (e.g., hazard reports, test results, software baselines) are revision-controlled.
3. **Test Witnessing and Validation**:

   * Ensure verification tests thoroughly evaluate:
     + System transitions from hazardous states to safe states.
     + Safe handling of invalid or erroneous operator inputs during system faults.
   * Record signatures from all responsible parties.
4. **Independent Assessment Processes**:

   * Involve IV&V early in requirements and design reviews to provide objective feedback on safety-critical SW mitigations.
5. **Training and Operations Testing**:

   * Perform end-user training to simulate hazardous scenarios, where operators perform recovery actions in partnership with automated safety controls.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

To demonstrate compliance with this requirement, **objective evidence** must be collected, documented, and traceable across all phases of the software development life cycle (SDLC). Objective evidence includes artifacts, test results, analyses, and documented processes that show the mitigation of hazardous behaviors has been implemented, verified, and validated.

The objective evidence should be credible, measurable, independently verifiable, and aligned with NASA standards, such as **NPR 7150.2** and **NASA-STD-8739.8**. Below is a comprehensive list of objective evidence that supports this requirement.

This objective evidence ensures that every phase of the SDLC incorporates and verifies hazard mitigation processes for critical software. By collecting these artifacts, a project demonstrates that the system meets this requirements mandate to handle hazardous software behaviors in a way that guarantees safety and reliability even under potential failure conditions.

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

# 8.1. Hazard Analysis Evidence

#### a. **Completed Hazard Analysis Reports**

* **Description**: Identify software-related hazards that could lead to catastrophic events and document mitigation strategies.
* **Key Components**:
  + Hazard descriptions, sources, and criticality.
  + Associated software components.
  + Likelihood/consequences of hazards.
  + Mitigations (e.g., error-handling mechanisms, fail-safe transitions).
* **Examples of Artifacts**:
  + Fault Tree Analysis (FTA) diagrams.
  + Failure Modes and Effects Analysis (FMEA) reports.
  + Hazard Analysis and Risk Assessment (HARA) documents.
  + Hazard tracking data.

#### b. **Traceability Matrices Linking Hazards to Mitigations**

* Matrices showing traceability from hazards → software requirements → design → test cases → results.

#### c. **Risk Management Logs**

* Risk identification and status logs showing how hazardous software behaviors were assessed and mitigated.

## 8.2. Software Requirements Evidence

#### a. **Safety-Critical Software Requirements Documentation**

* **Description**: Clearly defined safety-critical requirements that specify how software will detect, reduce, or mitigate hazardous behaviors.
* **Key Evidence**:
  + Requirements specifying fail-safe states, error detection events, and recovery protocols.
  + Requirements for redundancy, boundary condition handling, validation of critical inputs, and output monitoring.
  + Requirements for hazardous operation overrides or manual operator intervention.

#### b. **Requirements Validation Report**

* Identification of high-level system hazards linked to specific software requirements.
* Evidence that all safety-critical requirements were validated.

#### c. **Requirements Peer Review Records**

* Documentation of safety-critical software requirement peer reviews to confirm accuracy, completeness, and mitigation of hazard-related risks.

## 8.3 Software Design Evidence

#### a. **Software Design Documents (SDDs)**

* Include documented architectures, detailed designs, and diagrams addressing hazardous software behavior.
* Evidence of fault tolerance capabilities, isolation of safety-critical components, and transitions to safe states.

#### b. **Design Analysis Report**

* Documented analysis evaluating the robustness of the design for handling hazardous software behaviors.
* Includes:
  + Mitigations for single-point software failures.
  + Analysis of redundancy and independence in safety-critical software.

#### c. **Peer Review and Inspection Records**

* Results from structured design peer reviews specifically ensuring implementation of hazard mitigations.

#### d. **Simulation Models**

* Models demonstrating that safety-critical and fallback functions operate reliably in off-nominal conditions.

## 8.4 Implementation (Code) Evidence

#### a. **Source Code Analysis Reports**

* Static and dynamic analysis results, including:
  + Compliance with safety-critical coding standards (e.g., MISRA, NASA guidelines).
  + Evidence of defensive programming techniques.
  + Low cyclomatic complexity (≤15 for hazard mitigation code paths).

#### b. **Test Coverage Reports**

* Documentation showing that 100% of safety-critical code paths and identified hazardous scenarios are tested.
* Includes **Modified Condition/Decision Coverage (MC/DC)** metrics.

#### c. **Code Peer Review Records**

* Inspections of hazard-mitigation code for correctness, maintainability, and traceability to requirements.

#### d. **Configuration Management Evidence**

* Systems and logs showing that all software builds containing hazard mitigations have been version-controlled and undergo proper change management.

## 8.5 Verification and Validation (V&V) Evidence

#### a. **Test Plans and Procedures**

* Detailed test plans and procedures covering:
  + Nominal and off-nominal conditions.
  + Fault injection and stress scenarios.
  + Anomalous input handling, error recovery, and fail-safe state transitions.

#### b. **Test Results**

* Evidence that tests were executed, documented, and passed for all hazardous software behaviors, including:
  + Functional tests.
  + Fault injection tests.
  + Boundary tests.
  + Recovery tests showing system transition to safe states under hazardous software conditions.

#### c. **Simulations and Execution Logs**

* Recorded outputs of hazard scenarios executed in simulated or emulated environments to confirm software mitigation strategies work as expected.

#### d. **Independent Verification & Validation (IV&V) Records**

* Reports from IV&V providers confirming safety-critical requirements, design, code, and V&V processes mitigate hazardous software behaviors.
* Evidence includes findings, risks, and resolutions.

#### e. **Failure Recovery and Error Handling Verification**

* Test results demonstrating proper execution of error detection, isolation, reporting, and recovery mechanisms.

#### f. **System Integration Test Results**

* Evidence confirming all software integration dependencies passed, with specific emphasis on safety-critical interactions.

## 8.6 Safety Assurance Evidence

#### a. **Software Safety Analysis**

* Comprehensive analysis of how the software behaves under hazardous scenarios, including rationale for mitigation strategies.

#### b. **Safety Review Records**

* Evidence that software safety was reviewed in all phases (requirements, design, testing, and deployment).

#### c. **Non-Conformance Reports (NCRs)**

* Evidence of identified hazardous software behaviors, resolutions implemented, and their successful validation.

#### d. **Operator and Human-in-the-Loop Testing Results**

* Evidence of training and testing for system operators:
  + Ensure operators can detect and respond to hazardous behaviors identified by the software.
  + Demonstrate recovery scenarios involving human intervention.

## 8.7 Documentation and Training Evidence

#### a. **Safety-Critical Software User Manual**

* Operating instructions detailing:
  + Potential hazardous conditions.
  + Safety precautions and warnings.
  + Recovery procedures for hazardous software scenarios.

#### b. **Operator Training Document**

* Records confirming that training for mitigating hazardous software behavior was successfully completed.

#### c. **Lessons Learned Integration**

* Documentation showing how NASA lessons learned applicable to hazardous software behavior (e.g., Mars Climate Orbiter, Ariane 5 incidents) were considered and integrated into the software/system design.

## 8.8 Configuration and Release Control Evidence

#### a. **Functional and Physical Configuration Audit (FCA/PCA) Reports**

* Evidence of audits showing that implemented software matches the documented design for hazard mitigation.

#### b. **Change Records**

* Logs of changes made to safety-critical code to address hazardous software behaviors.
* Includes regression testing results to verify continued compliance after changes.

#### c. **Release Notes**

* Release notes documenting safety-critical features intended to address hazardous software behavior.

## 8.9 Objective Evidence Table

| **Artifact** | **Phase** | **Purpose** |
| --- | --- | --- |
| Hazard Analysis Reports | Requirements | Identify risks and mitigations |
| Software Requirements Traceability | Requirements | Verify coverage of hazards |
| Safety-Critical Software Design Docs | Design | Ensure proper mitigation implementation |
| Code Analysis and Complexity Reports | Implementation | Verify code correctness/robustness |
| Test Results (functional, fault injection) | Validation | Confirm mitigation of hazards |
| IV&V Reports | Validation | Independent assurance review |
| Configuration Audit Reports | Deployment | Verify CM controls for safety-critical artifacts |
| Operator Training Records | Training | Ensure readiness for in-flight hazard response |
