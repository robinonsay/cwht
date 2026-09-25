# HR-33 - Inadvertent Operator Action

> NASA Software Engineering Handbook (SWEHB Ver D), page id 167805149. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action

HR-33 - Inadvertent Operator Action

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=167805149)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=167805149&showCommentArea=true&showComments=true#addcomment)

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

4.3.3 The space system shall be designed to tolerate inadvertent operator action (minimum of one inadvertent action), as verified by a human error analysis, without causing a catastrophic event.

## 1.1 Notes

An operator is defined as any human that commands or interfaces with the space system during the mission, including humans in the control centers. The appropriate level of protection (i.e., one, two, or more inadvertent actions) is determined by the integrated human error and hazard analysis per NPR 8705.2. [024](#_tabs-<p></p>)

## 1.2 History

Click here to view the history of this requirement: HR-33 History

HR-33 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.3.3 The space system shall be designed to tolerate inadvertent operator action (minimum of one inadvertent action), as verified by a human error analysis, without causing a catastrophic event. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

One of the main causes of erroneous software behavior is through inadvertent or erroneous operator input.  Tolerating inadvertent operator input requires general one-fault systems tolerance (i.e., error checking).    This requirement ensures that multiple, unique, and independent commands are used when disabling a Must Work Function and forces operator error analysis before execution. This requirement protects against disabling redundant control strings by preventing the scripting or combining two or more of the “unique and independent” commands, such that multiple commands can be issued by a single operator action without error checking.

This requirement ensures that **space systems** are robust against the unavoidable risk of human error. Human operators are inherently prone to making inadvertent actions, especially in high-stress environments such as space missions or real-time ground control operations. This requirement is essential because **inadvertent operator actions**—whether they stem from misperception, fatigue, or simply unanticipated conditions—can introduce hazards that may result in **catastrophic events** like loss of crew, loss of mission, or damage to expensive hardware/systems.

Designing for fault tolerance to inadvertent operator action reduces the risk of catastrophic hazards caused by such errors, creating safer and more reliable systems for space operations.

The rationale for this requirement is rooted in the fundamental understanding that **humans are inherently prone to making errors**, particularly under high-stress conditions typical of space operations. By designing space systems to tolerate at least **one inadvertent operator action**, NASA ensures the **safety, reliability, and robustness** of its missions. This requirement not only mitigates catastrophic hazards but also aligns with NASA’s commitment to prioritize risk reduction for **both crew safety and successful mission execution**.

## 2.1 Rationale Breakdown

### 2.1.1 Human Fallibility

* Humans are an indispensable element of space system operation, but they are also error-prone. Mistakes can occur due to:
  + Fatigue, stress, time pressure, or distraction.
  + Limited situational awareness in complex or high-stakes scenarios.
  + Incomplete or ambiguous communication.
  + Misinterpretation of system feedback or alerts.
* Systems should be designed to "expect" human errors and provide safeguards to prevent those errors from escalating into catastrophic incidents.

**Example Rationale**: During a mission, an operator might inadvertently activate a system shutdown or incorrectly enter commands due to stress or ambiguous user interfaces. If the system is not tolerant to these errors, a critical system might be disabled, endangering the mission and crew.

### 2.1.2 Mitigation of Catastrophic Hazards

* Inadvertent operator actions can have catastrophic consequences depending on the system's complexity, the type of actions possible, and the criticality of the systems under operator control. The purpose of this requirement is to ensure that **at least one inadvertent action** does not lead to a catastrophic event.
* Safeguards, validations, or recovery mechanisms should catch or mitigate such unintended actions before risk escalates to a catastrophic level.

**Example Rationale**: For space systems with propulsion or life support systems:

* A single wrong command (e.g., activating the wrong thruster system or disabling oxygen supply) could present catastrophic outcomes if not caught or mitigated by system safeguards.

### 2.1.3 Human Error Is Often Predictable

* Historical data from **human error analysis** in past space missions and other similar operations have shown distinct patterns in operator error. These include, but are not limited to:
  + **Entering an incorrect value** (e.g., upload of wrong orbital parameters).
  + **Issuing the wrong command** (e.g., commanding a system shutdown instead of a reboot).
  + **Failing to complete a process properly** (e.g., skipping a step during manual override, or performing actions out of sequence).
* Because human errors are common and predictable, many of these scenarios can be accounted for in the design phase using recognized **human factors engineering** principles and robust **error analysis techniques**.

**Example Rationale**: Operational procedures often require input confirmation or "are you sure?" prompts. Such measures are examples of how we can predict errors and design systems to mitigate their impact.

### 2.1.4 Preventing "Single-Point Errors" Caused by Humans

* This requirement aligns with system fault tolerance goals by ensuring that **no single inadvertent human action** can trigger a catastrophic event. By analogy, this is similar to engineering designs that avoid "single point failures" in physical systems.
* Human input, when unchecked, can act as a "single point of failure" if it directly triggers or propagates dangerous system states. Designing layers of **error-clearing mechanisms** or requiring **multi-step confirmations** for critical commands introduces redundancy into human-system interactions and protects against such single-point errors.

**Example Rationale**: A flight control system can be designed so that critical commands, such as activating self-destruct systems or orbital changes, require a multi-step authorization process or additional confirmations from independent operators.

### 2.1.5 Alignment with NASA’s Risk Management Approach

* This requirement reflects NASA's **risk-based approach to safety**, as defined in **NPR 8705.2** and related standards, which prioritize the prevention of catastrophic hazards through an integrated approach involving hardware, software, and human factors.
* Human errors are recognized as significant contributors to risk in complex, high-pressure environments:
  + Studies and reports from past NASA missions (e.g., **Columbia Accident Investigation Board**) indicate that both active errors (mistakes made during operations) and latent errors (system design flaws that allow mistakes to propagate) can introduce catastrophic consequences if not addressed.
* Designing for this requirement supports the **"hazard elimination hierarchy"**: avoiding or mitigating human-induced hazards is treated as a fundamental baseline for system design.

**Example Rationale**: By integrating human error analysis into the design phase, latent design flaws enabling harmful human errors can be identified and addressed early, avoiding propagation of larger, potentially fatal risks to the mission.

### 2.1.6 Ensuring Mission Success and Crew Safety

* If human error in the operation of the system is not managed, failure events could lead to severe outcomes, including:
  + **Catastrophic loss of vehicle and mission** (e.g., inadvertent software uploads or destabilizing engine shutdowns during staging or reentry).
  + **Loss of crew safety** or life (e.g., activating life support shutdowns).
  + **Environmental hazards**—damage to external infrastructure or contamination during planetary missions or launch vehicle operations.
* By designing failure-tolerant systems that anticipate human errors, the overall reliability and safety margin of the space system increases, directly supporting mission success.

## 2.2 Verification Through Human Error Analysis

The requirement specifies that compliance is **verified by human error analysis**, a structured evaluation methodology that ensures all potential operator error modes are identified, modeled, and mitigated.

1. **Conduct Human Error Modes and Effects Analysis (HEMEA)**:

   * Similar to FMEA, this analysis identifies potential inadvertent operator actions, their likelihood, and the effects on the system.
   * Example: Evaluate scenarios where an astronaut enters an unintended command, such as selecting the wrong valve to close in a process sequence.
2. **Cognitive Workload and User Interface Analysis**:

   * Assess whether the system design introduces unnecessary complexity or relies too heavily on the operator's memory or reaction during critical interactions.
   * Example: Systems designed with overly complex or ambiguous user interfaces increase operator error probability.
3. **Operational Validation and User Testing**:

   * Evaluate the system during simulations with human operators to identify actual sources of inadvertent actions.
   * Example: Simulating a high-stress docking operation to determine whether the user interface or control process leads the operator to inadvertently activate the wrong inputs.

## 2.3 Design Features to Support Compliance

The system design should incorporate the following elements to ensure operator error mitigation:

1. **Confirmation Mechanisms**:

   * Require multi-step confirmation for safety- and mission-critical actions.
   * Example: A "double-confirmation" system to ensure commands leading to significant changes are intentional.
2. **Error-Prevention Features**:

   * Use engineering controls (e.g., interlocks, limits) to prevent invalid operator actions.
   * Example: Disable commands that issue destructive actions unless specific conditions are met.
3. **Error Detection and Recovery**:

   * Implement real-time error detection monitoring and automatic recovery mechanisms.
   * Example: If an inadvertent command disables atmospheric controls, automatic recovery triggers to restore previous configurations.
4. **Enhanced User Interfaces**:

   * Design intuitive and error-resistant system interfaces (e.g., minimizing clutter or ambiguous icons).
   * Example: Grouping high-priority functions separately from non-critical or hazardous functions.

# 3. Guidance

The space system must be designed to tolerate inadvertent operator actions (minimum of one) without causing catastrophic events. To achieve compliance, software engineering plays a critical role by implementing safeguards and robust system design concepts that mitigate operator-induced risks. This improved guidance builds on the outlined strategies, offering deeper technical insight and actionable implementation steps.

The improved software engineering guidance ensures robust fault tolerance to inadvertent operator actions by coupling layered safeguards, intuitive design, error telemetry, thorough testing, and IV&V processes together. This approach aligns with NASA’s rigorous safety standards (e.g., NASA-STD-8739.8 [278](#_tabs-<p></p>) ) and ensures compliance with this requirement, ultimately enabling safer and more reliable space system operations.

## 3.1 Objective

To design, develop, and validate software that ensures fault tolerance for inadvertent operator actions by:

1. Mitigating risks associated with operator errors through safeguards.
2. Providing recovery mechanisms to avoid catastrophic system impacts.
3. Ensuring all error-tolerance features align with safety-critical requirements and operational goals.

## 3.2 Key Design Strategies

### 3.2.1 Fault Tolerance Mechanisms

The system must tolerate inadvertent operator actions by integrating:

1. **Two-Stage Commanding**:

   * Critical actions require multi-step confirmations with clear implications displayed before execution.
   * Example: "Activate thruster shutdown" command requires a two-stage process:
     + Step 1: Command input is validated and flagged as potentially hazardous.
     + Step 2: Operator confirms the action with feedback on system state changes.
2. **Input Validation and Error Checks**:

   * Implement context-dependent error validation in all operator input pathways:
     + Reject invalid or dangerous commands during unsafe system states.
     + Example: Prevent an operator from disabling propulsion in a critical orbital adjustment phase.
   * Use real-time feedback mechanisms to flag and reject unintended or conflicting operator entries.
3. **Command Fault Tolerance**: For disabling primary and redundant control strings:

   * **Case A**: Systems with redundant control strings active before disabling the primary string:
     + Require independent and unique command inputs to disable each control string.
   * **Case B**: Systems with redundant backup control strings activated after disabling the primary string:
     + Require two independent and unique commands to deactivate/disable control strings after activating redundancy.
4. **Graceful Recovery**:

   * Ensure the software can recover from erroneous commands before irreversible consequences occur:
     + Example: Automatically re-enable disabled system functions or restore safe configurations if the operator inadvertently disrupts operations.

### 3.2.2 Design Principles for Human Error Tolerance

#### Human-Machine Interface Design

1. **Intuitive Interface**:

   * Design operator interfaces to reduce complexity and ambiguity:
     + Use organized, hierarchical layouts that separate critical controls from non-critical controls.
     + Example: Group critical commands (e.g., "shutdown operations") in protected menus.
2. **Error Feedback and Annunciation**:

   * Provide clear, real-time feedback when errors are detected:
     + Example: Display warnings for invalid operator actions with suggested corrections ("Cannot disable oxygen supply during life-critical operations.").
3. **Command Grouping and Interlock Mechanisms**:

   * For safety-critical sequences, ensure commands are logically grouped and require context-based unlocks/interlocks (e.g., prevent disabling propulsion until the backup system is fully initialized).

#### Fail-Safe Command Processing and Graceful Degradation

1. **Redundant Command Isolation**:

   * Segregate processing pathways for safety-critical commands to ensure no single fault propagates through redundant systems.
2. **Predictable System Responses**:

   * Implement safeguards to avoid catastrophic cascading events:
     + Example: Disallow shutdown commands unless redundancy is established and verified.

## 3.3 Verification, Validation, and Testing Tasks

### 3.3.1 Human Error Analysis

**Objective**: Identify potential operator-induced errors and design mitigation strategies.

* Conduct formal **Human Error Modes and Effects Analysis (HEMEA)**:
  + Examine operator inputs, workflows, and control sequences for fault-prone areas.
  + Example: Identify scenarios where operators might inadvertently select the wrong control input.
* Create error impact models based on historical human error data and operational testing findings.
* Collaborate with human factors experts to:
  + Ensure operator actions align with cognitive strengths and minimize ambiguity.

**Outputs**:

* Completion of HEMEA with mapped error scenarios and mitigations.
* Traceability matrix linking human error findings to software design features.

### 3.3.2 Simulation and Testing

**Objective**: Model and validate inadvertent operator action tolerance in realistic operational environments.

* **Scenario Simulations**:
  + Conduct simulations targeting error-prone situations (e.g., under stress or high workload) to validate operator fault tolerance mechanisms.
  + Example: Simulate errors like premature shutdown or incorrect sequence activation during time-critical events.
* **Failure Injection Testing**:
  + Inject erroneous inputs to test system responses at software and hardware integration levels:
    - Example: Inject invalid command input for system shutdown during operation and ensure safeguards prevent non-confirmed disabling actions.

**Outputs**:

* Test reports with evidence of error tolerance performance.
* Results from fault injection testing confirming recovery and failover mechanisms.

### 3.3.3 Formal and Informal Testing

**Objective**: Validate software robustness across varying operational conditions.

* Formal testing approaches:
  + Execute functional tests verifying that the software can handle at least one inadvertent operator action without propagating catastrophic consequences.
  + Validate all error-checking and recovery mechanisms.
* Informal testing approaches:
  + Conduct exploratory and boundary testing on operator input pathways to identify unrecorded defects or potential vulnerabilities.

**Outputs**:

* Comprehensive test results covering both expected and unexpected conditions.
* Boundary test findings for validation of limits on operator actions.

### 3.3.4 Error Handling and Recovery Validation

**Objective**: Ensure the software includes built-in recovery mechanisms that handle inadvertent operator errors gracefully.

* Validate robustness of error-handling code:
  + Test error detection rates, exception resolution, and system recovery capabilities.
  + Example: Verify automatic restoration of safety-critical configurations after system disruption.
* Execute recovery failure scenarios:
  + Measure time-to-event recovery for safety-critical systems when fallback or manual overrides are triggered.

**Outputs**:

* Validation plans and reports for error handling and system recovery.

### 3.3.5 Automated Verification and Validation

**Objective**: Identify and resolve software defects that could propagate errors.

* Use automated tools for software quality assurance:
  + Static analysis: Detect syntax errors and potential vulnerabilities.
  + Dynamic analysis: Validate real-time system integrity during error-induced scenarios.
  + Code coverage and complexity metrics:
    - Ensure critical functions (e.g., command validation) achieve close to 100% coverage in tests.

**Outputs**:

* Automated tool results showing compliance with error tolerance benchmarks (e.g., fault recovery within acceptable time limits).

### 3.3.6 Configuration Management

**Objective**: Reduce risks from configuration anomalies introduced through human error.

* Implement strict version control protocols:
  + Prevent mismatched redundancy configurations or inadvertent changes to safety-critical systems.
* Audit configuration baselines for consistency across redundant control systems.

**Outputs**:

* Configuration management artifacts evidencing strict adherence to version control protocols.

### 3.3.7 Independent Verification and Validation (IV&V)

**Objective**: Ensure unbiased assessment of error tolerance design and implementation.

* Perform IV&V activities focusing on software features supporting human error tolerance:
  + Review HEMEA results for completeness and accuracy.
  + Validate error recovery scenarios and safeguard mechanisms during testing phases.
* Track IV&V participation metrics:
  + Coverage of error-tolerance scenarios.
  + Feedback into requirements revision process.

**Outputs**:

* IV&V reports certifying compliance with operator error tolerance requirements.
* IV&V metrics for improvement tracking.

## 3.4 Training and User-Centered Documentation

**Objective**: Minimize operator error likelihood through proper training and documentation.

* Develop operator training programs focused on:
  + Correct command sequences and error recovery procedures.
  + Recognition and avoidance of hazardous unintended actions during operations.
* Provide **comprehensive user manuals**:
  + Include error warnings, troubleshooting guides, and fallback recovery procedures.
  + Example: Document best practices for manual overrides during system emergencies.

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) - * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Requirements related to Human Rated Software.

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

For small-scale projects, implementing this requirement —ensuring a system can tolerate at least **one inadvertent operator action** without causing **catastrophic events**—requires **focused, lightweight, and scalable approaches**. This guidance outlines how small project teams can address this requirement effectively while managing constraints such as limited resources, smaller teams, and shorter timelines.

## 4.1 Goals for Small Projects

1. **Practical Error Mitigation:** Design software and systems to minimize the risk of inadvertent operator actions.
2. **Lightweight Verification:** Use cost-effective testing and validation processes.
3. **Efficient Collaboration:** Integrate safety, software, and operator knowledge effectively within a smaller team.
4. **Documentation Simplicity:** Keep required documentation concise but sufficient to demonstrate compliance.

## 4.2 Small Project Guidance Steps

### 4.2.1 Simplify Risk Identification and Analysis

**Objective**: Identify and prioritize the operator errors that could cause catastrophic events while maintaining a lightweight, actionable process.

* **Key Activities**:

  1. **Collaborate with Key Stakeholders**:
     + Meet with operations staff, system users, and safety representatives.
     + Discuss critical systems, operator controls, and potential error scenarios.
  2. **Use Focused Human Error Analysis**:
     + Apply a simple **task breakdown**:
       - Identify operator tasks and inputs for safety-critical systems.
       - Highlight "dangerous" commands (e.g., shutdown, activation of hazardous systems).
     + Use **low-effort brainstorming** or checklist approaches for human error analysis:
       - What could go wrong in normal operations?
       - What commands could be issued unintentionally?
       - What operational conditions could lead to inadvertent inputs (e.g., fatigue)?
  3. **Evaluate Likelihood and Severity**:
     + Prioritize errors that:
       - Have **high severity** impacts (e.g., catastrophic hazards).
       - Are **plausibly likely** in operation.
* **Output**:

  + A prioritized list of potential operator errors and their associated risks.
  + Simple human error scenarios documented in tables or spreadsheets (can replace full-fledged models/tools).

### 4.2.2 Streamline Safeguard Design

**Objective**: Implement lightweight yet robust design measures to tolerate a single inadvertent operator action.

* **Key Design Strategies**:

  1. **Simplified Command Confirmation**:
     + Implement **two-stage confirmation** for safety-critical commands (e.g., "Are you sure you want to deactivate life support?"):
       - **First Prompt**: Ask for confirmation of the action.
       - **Final Check**: Require a secondary, deliberate step (e.g., "Enter code XYZ to confirm shutdown.").
  2. **Input Validation**:
     + Add simple checks to reject invalid inputs:
       - Example: Prevent deactivating the primary propulsion unless backup propulsion is ready and operational.
     + Use **context awareness**:
       - Commands should be valid only in certain system states.
  3. **Disabling Dangerous Commands**:
     + Disable problematic commands or enforce system locks under certain conditions:
       - Example: Lock manual override commands during automatic recovery actions.
  4. **Self-Correcting Mechanisms**:
     + Automate recovery within the system when possible:
       - Example: If the operator sends a shutdown command inadvertently, the system automatically reverts to a previous safe state unless overridden by an authorized, multi-step manual process.
* **Effort Tips**:

  + Leverage guardrails in User Interface Design:
    - Separate critical commands from others by grouping them in protected menus.
    - Provide **alerts** showing the impact of selected commands (e.g., if a command will disable a safety-critical function, flag this visually in bold "STOP" prompts).
* **Output**:

  + Simple design documentation (e.g., a table of safeguards linked to prioritized operator errors).
  + Modifications to command input handling logic to ensure error tolerance.

### 4.2.3 Focused Testing for Error Handling

**Objective**: Validate that the system can tolerate identified operator errors using focused, resource-efficient testing techniques.

* **Key Testing Tasks**:

  1. **Scenarios for Testing**:
     + Create a small number of test scenarios based on the prioritized operator errors.
     + Example test cases:
       - Issue an accidental shutdown command during nominal operations.
       - Activate manual override without initializing backup systems.
       - Perform destructive input sequences (e.g., disabling propulsion during ascent).
  2. **Manual Testing First**:
     + Use **manual testing** instead of automation for smaller projects to reduce complexity:
       - Create ready-to-execute scripts for testers to follow and introduce realistic errors during simulation.
  3. **Lightweight Fault Injection**:
     + Simulate one or two potential operator errors in a controlled testing environment:
       - Example: Testing a "cancel engine shutdown" scenario when initiated accidentally.
     + Observe whether the system detects, mitigates, or recovers from the error.
  4. **Small-Scale Simulation (Optional for Small Projects)**:
     + Run informal scenario simulations (e.g., in a hardware-in-the-loop testbed) to observe the system's performance with simulated operator errors.
* **Output**:

  + Test results showing the system mitigates at least one error case without causing a catastrophic event.
  + Lightweight test reports summarizing operator error scenarios and outcomes.

### 4.2.4 Documentation Simplification

**Objective**: Fulfill documentation needs by focusing on clarity and traceability, without overburdening resources.

* **Key Documentation Artifacts**:
  1. **Error Scenario Table**:
     + Table format listing:
       - Identified operator errors.
       - Mitigation methods (e.g., "two-step confirmation", "state-based locks").
  2. **Test Summary**:
     + Summarized test results, such as:
       - "Command input for safely detected as invalid and rejected, no impact on system safety."
       - A brief pass/fail assessment.
  3. **Traceability Matrix**:
     + Simple matrix linking operator errors ↔ safeguards ↔ test cases.
     + Example (one row might look like this):

       ```
       Error: Accidental engine shutdown
       Safeguard: Two-step confirmation and automation rollback
       Test Case: Command input validation during ascent sim (pass)
       ```

### 4.2.5 Prioritize Independent Verification and Validation (IV&V) Participation

**Objective**: Involve IV&V early and with reduced scope to avoid costly corrections later.

* **Key Tasks for Small IV&V Effort**:

  1. Brief the IV&V team using **error scenarios and design safeguards** so they can focus assessments on fault-tolerance mechanisms.
  2. Request feedback only on safety-critical elements (avoid entire-system reviews).
  3. Leverage IV&V testing to validate edge cases and catastrophic hazards.
* **Output**:

  + Summary report or quick validation statements provided by IV&V for software safeguards.

### 4.2.6 Operator Training and Simple Guides

**Objective**: Ensure operators understand human errors and safeguards.

* Use **concise materials** (e.g., one-page quick guides or tooltips) to explain:

  + Commands requiring confirmation.
  + How the system responds to inadvertent errors.
  + Recovery procedures for common operator mistakes.
* Conduct brief training with operators to demonstrate safeguards.
* **Output**:

  + A quick-start guide for operators (e.g., PDF or laminated card).

## 4.3 Final Deliverables for Small Projects

By following this guidance, a small project team can deliver the following artifacts:

1. **Prioritized human error analysis results** (focus on high-severity risks).
2. **Software safeguards** (e.g., validation and recovery mechanisms).
3. **Simplified test reports** verifying the system tolerates at least one inadvertent operator action.
4. **Concise documentation**:
   * Error scenarios and mitigations.
   * Test findings for safety-critical cases.
5. **Operator training materials**.

This focused approach ensures compliance with requirement while staying manageable for the constraints of small projects. The simplicity allows small teams to maintain high-quality outputs while adhering to NASA’s safety standards.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-024)

  [Human-Rating Requirements for Space Systems (Updated w/Change 2)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=2C "Click to open in new window")

  NPR 8705.2C, NASA Office of Safety and Mission Assurance, 2008.,
  Effective Date: July 10, 2017, Expiration Date: July 10, 2025
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
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

NASA’s extensive history of missions, coupled with post-mission reviews and analysis, provides valuable lessons learned about **human error tolerance** and the importance of designing systems that can recover from inadvertent operator actions. These lessons emphasize the need for safeguards, robust designs, and human error mitigation strategies to ensure system safety and functionality. Below are key lessons learned from notable incidents, reports, and studies relevant to **Requirement 4.3.3**.

---

### **Lesson 1: Anticipate and Mitigate Operator Error Early in Design**

* **Source**: NASA's Columbia Accident Investigation Board (CAIB) Report.
* **Lesson**: Human error is inevitable, and the risk must be accounted for during design, testing, and operational planning.
* **Example**:

  + During the **Columbia Space Shuttle Mission (STS-107)**, inadequate feedback mechanisms contributed to the late realization of critical issues after damage occurred to the orbiter. While not an operator error, the incident demonstrated the lack of critical safeguards for decision-making and error-handling in high-pressure environments.
* **Takeaway for Requirement 4.3.3**:

  + Design systems assuming that operators will make mistakes under stress or ambiguity.
  + Implement safeguards and redundancies to prevent cascading consequences from a single erroneous action.
  + Ensure timely and unambiguous feedback loops that inform operators of the system state.

---

### **Lesson 2: Use Two-Step Verification for Critical Commands**

* **Source**: International Space Station (ISS) Operations.
* **Lesson**: Avoid direct execution of critical commands without operator acknowledgment or confirmation.
* **Example**:

  + During ISS operations, incorrect manual commands nearly disabled a primary cooling system. The system was saved by the requirement for a follow-up verification and redundant command confirmation, which caught the error.
* **Takeaway for Requirement 4.3.3**:

  + Critical commands should always require **two-step (dual-stage) verification**, such as:
    - Operator confirmation: “Are you sure you want to proceed?”
    - Contextual validation: “This action may disrupt a critical function. Confirm the backup system is operational.”
  + Systems should provide real-time warnings to operators about the **consequences of their actions** before execution.

---

### **Lesson 3: Simplify User Interfaces to Prevent Mistakes**

* **Source**: Apollo 11 Lunar Landing Incident (1969).
* **Lesson**: Overly complex interfaces or undertrained operators increase the likelihood of inadvertent errors during time-critical scenarios.
* **Example**:

  + During Apollo 11's descent to the lunar surface, pilot Neil Armstrong and system monitors faced input overload when the radar interface displayed unexpected alarms caused by program errors. The cluttered and limited user interface compounded time pressure and could have endangered the mission.
* **Takeaway for Requirement 4.3.3**:

  + Design user interfaces to **minimize complexity**:
    - Consolidate or abstract non-critical actions during high-stakes operations.
    - Ensure critical commands are visually distinct and cannot be confused with routine inputs.
  + Use clear error messages and status indicators to assist operator decision-making.

---

### **Lesson 4: Ensure Error Recovery Systems Are Robust**

* **Source**: Mars Climate Orbiter (1998) Failure.
* **Lesson**: Lack of system-level error recovery mechanisms can lead to catastrophic results.
* **Example**:

  + The Mars Climate Orbiter failed due to a **miscommunication of units (metric vs. imperial)** between ground software systems. There were no automated recovery mechanisms or manual checks in place to identify and correct the error before it cascaded into mission failure.
* **Takeaway for Requirement 4.3.3**:

  + Software systems must be designed with **error recovery mechanisms**:
    - Detect erroneous operator commands before execution.
    - Automatically revert or mitigate invalid actions.
    - Provide operators the ability to **undo or correct improper inputs** if detected late.

---

### **Lesson 5: Test for Human Error in Simulated Environments**

* **Source**: Human Spaceflight Simulations and Training in the Space Shuttle and ISS Programs.
* **Lesson**: Testing for potential operator errors in realistic simulations reduces the likelihood of errors during actual missions.
* **Example**:

  + In training simulations, astronauts repeatedly practiced scenarios where they unintentionally triggered system interruptions. Lessons learned during these exercises led to improvements in the interface design and safeguards.
* **Takeaway for Requirement 4.3.3**:

  + Thoroughly test the system’s response to **human error scenarios**:
    - Simulate stress conditions, fatigue, and uncertainty.
    - Validate the safeguards and command confirmations by forcing errors during simulation.
  + Use simulation findings to refine the system’s user interface and decision support tools.

---

### **Lesson 6: Maintain Redundancies to Tolerate Failures**

* **Source**: Gemini 8 Mission (1966).
* **Lesson**: Redundancy in control systems is essential to tolerate inadvertent actions or hardware/software failures.
* **Example**:

  + During Gemini 8, a malfunction in one of the spacecraft’s thrusters caused it to spin uncontrollably. The astronauts relied on redundant manual systems to regain control after disabling the malfunctioning systems.
* **Takeaway for Requirement 4.3.3**:

  + Ensure all critical systems include **redundant pathways** that are independent and diverse:
    - For systems like propulsion or life support, disabling the primary string should have a **backup string that activates automatically or under operator control**.
    - For systems requiring manual input, the process should include state validation, ensuring redundancy activation occurs prior to disabling primary systems.

---

### **Lesson 7: Avoid Single-Point Failures From Operator Actions**

* **Source**: Skylab Program (1973-1974).
* **Lesson**: Never allow a single operator action or single-command sequence to lead to a catastrophic failure.
* **Example**:

  + During Skylab operations, a miscommand temporarily disrupted thermal regulation of the spacecraft, endangering onboard equipment. Safeguards, such as secondary options for command scheduling, prevented significant damage.
* **Takeaway for Requirement 4.3.3**:

  + Design systems to ensure:
    - No single action can directly result in disabling critical subsystems.
    - Command pathways include **interlocks** and context-based restrictions:
      * Example: Require multiple independent confirmations or system checks to execute any shutdown or function-disabling operations.

---

### **Lesson 8: Provide Operator Feedback to Prevent Repeating Errors**

* **Source**: NASA Human Error Research (Post-Challenger and Post-Columbia).
* **Lesson**: Operators need clear and informative feedback to recognize errors in real-time and take corrective actions.
* **Example**:

  + Human-in-the-loop studies show that ambiguous or delayed feedback increases the chance of an operator repeating the same mistake.
* **Takeaway for Requirement 4.3.3**:

  + Include **clear feedback systems** that:
    - Prompt operators if an action conflicts with system state.
    - Explain the system’s status after operator input ("System remains active due to operational constraints.").
  + Use **audible alerts, visual indications, and logs** to make error identification easy.

---

### **Lesson 9: Design for Predictable and Safe Degradation**

* **Source**: Galileo Spacecraft Anomaly (1991).
* **Lesson**: When a critical system is compromised, the system must degrade gracefully into a safe configuration rather than escalate problems.
* **Example**:

  + The Galileo spacecraft experienced an issue with its high-gain antenna but entered a controlled degradation state using its low-gain antenna as a fallback. This design decision prevented full mission failure.
* **Takeaway for Requirement 4.3.3**:

  + Design software to:
    - Transition to safe, degraded operational modes if an unexpected operator error disables a subsystem.
    - Ensure operator error does not lead to unpredictable or runaway system behavior.

---

### **Lesson 10: Train Operators to Be Familiar With System Safeguards**

* **Source**: Apollo 12 Lightning Strike Incident (1969).
* **Lesson**: Operator knowledge of system safeguard configurations is crucial for prompt response.
* **Example**:

  + During Apollo 12’s ascent, lightning struck the spacecraft, disrupting key systems. Quick operator response, based on their prior training, restored critical functions.
* **Takeaway for Requirement 4.3.3**:

  + Comprehensive operator training should include:
    - Error recognition.
    - Responses to mitigation systems (e.g., safeties, interlocks).
    - Effective recovery steps if an inadvertent action occurs.

---

### **Summary of Lessons Learned**

NASA's lessons emphasize designing systems resilient to human error by combining safeguards, intuitive user interfaces, robust redundancies, thorough testing, and operator training. These lessons are directly applicable to **Requirement 4.3.3** and underscore the importance of **error prevention**, **error detection**, and **error recovery mechanisms** to protect against catastrophic consequences.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-33 - Inadvertent Operator Action**

4.3.3 The space system shall be designed to tolerate inadvertent operator action (minimum of one inadvertent action), as verified by a human error analysis, without causing a catastrophic event.

Improving the software assurance guidance for this requirement focuses on:

1. **Structured mitigation of human error risks**.
2. **Robust testing and verification frameworks** tailored to inadvertent operator actions.
3. **Actionable metrics** for monitoring and continuous improvement.
4. **Clear documentation and training efforts** for operators and developers.

This ensures compliance with safety-critical requirements and aligns with NASA software assurance standards (e.g., **NASA-STD-8739.8**, **NPR 7150.2**) to deliver reliable and resilient space systems.

## 7.1 Tasking for Software Assurance

1. Confirm that a detailed software command error analysis is complete to identify potential operator errors that could lead to catastrophic events. This analysis should include various commanding scenarios and the likelihood of each command error occurring.
2. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically the off-nominal commanding scenarios to mitigate the impact of inadvertent operator actions. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks). Ensure that the project has developed and executed test cases to test the impact of inadvertent operator actions. This includes conducting tests to verify that the system can handle at least one inadvertent action without resulting in catastrophic consequences.
3. Perform safety reviews on all software changes and software defects. This ensures that any modifications do not introduce new vulnerabilities or increase the risk of inadvertent actions leading to catastrophic events.
4. Perform test witnessing for safety-critical software to ensure the impact of inadvertent operator actions is mitigated. (See [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) tasks)
5. Confirm that both formal and informal testing to uncover unrecorded software defects has been completed. This includes testing unexpected conditions, boundary conditions, hazardous conditions, and software/interface inputs.
6. Confirm robust error handling and recovery mechanisms to address errors resulting from inadvertent operator actions. This includes ensuring adequate error handling and that the system can recover from errors without leading to catastrophic events.
7. Confirm the use of automated tools for static analysis, dynamic analysis, and other verification and validation activities. This helps identify potential software defects that could result in catastrophic events due to inadvertent operator actions.
8. Confirm that strict configuration management is maintained to ensure that the correct software versions and configurations are used. This reduces the risk of errors due to incorrect or inconsistent configurations. (See tasks in [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items))
9. Ensure comprehensive training and documentation for operators to minimize the chances of inadvertent actions is available. This includes clear instructions, warnings, and recovery procedures.

## 7.2 Software Assurance Products

The revised software assurance guidance aligns with Requirement 4.3.3 by reducing risks associated with inadvertent operator actions in a systematic, streamlined, and scalable manner for space systems. This guidance improves clarity, emphasizes actionable steps, and ensures compliance while maintaining efficiency across software development processes.

The following **Software Assurance Products** are essential for ensuring that the space system can tolerate inadvertent operator actions without causing catastrophic events:

### 7.2.1 Human Error Analysis

* Conduct and document **Human Error Analysis**:
  + Identify software-driven scenarios where operator errors (e.g., wrongful command issuance) may trigger catastrophic consequences.
  + Evaluate the likelihood, severity, and potential propagation of errors within the software control system.
  + Incorporate findings into system requirements, user interface design, and test plans.

**Deliverables**:

* Human error analysis reports that assess potential risk scenarios and mitigation strategies.
* Traceability mappings between potential error scenarios, mitigations, and software design elements.

### 7.2.2 Verification Test Results

* Develop **Verification Test Reports** documenting test cases and results proving the system can tolerate at least one inadvertent action without catastrophic outcomes:
  + Include tests for **boundary conditions, failure modes, and recovery procedures**.
  + Focus specifically on safety-critical software components.

**Deliverables**:

* Verification test results demonstrating compliance with error tolerance requirements.
* Include test data capturing system recovery times, error handling performance, and impacts of incorrectly issued commands.

### 7.2.3 Audit Reports

* Conduct **Functional Configuration Audits (FCA)** and **Physical Configuration Audits (PCA)**:
  + Verify that all safety-critical software requirements associated with tolerating human errors are implemented and documented.
  + Ensure alignment between design documents, software artifacts, and testing.

**Deliverables**:

* FCA and PCA reports confirming software readiness and compliance with configuration and safety requirements.

### 7.2.4 Source Code Quality Analysis

* Use automated tools to analyze source code for maintainability, reliability, and safety:
  + Perform static analysis (syntax errors, unreachable code, etc.), dynamic analysis, and review cyclomatic complexity.
  + Validate that safety-critical software meets **NASA-STD-8739.8** safety design standards (e.g., cyclomatic complexity ≤15).

**Deliverables**:

* Reports summarizing tool outputs, with identified defects categorized by severity.
* Include resolved metrics and remaining software issues impacting error tolerance.

### 7.2.5 Software Safety and Hazard Analysis

* Perform comprehensive **Software Safety Analysis** using techniques such as Fault Tree Analysis (FTA) and Failure Modes and Effects Analysis (FMEA).
* Identify hazards related to inadvertent operator actions:
  + Evaluate functional impacts caused by erroneous commands, such as disabling propulsion, shutting down life support systems, etc.
  + Define mitigation and recovery mechanisms (e.g., automated rollback procedures, confirmation checks).

**Deliverables**:

* Hazard analysis reports with safety-critical software-specific controls aligned with Requirement 4.3.3.
* Traceability between mitigations and testing procedures.

### 7.2.6 Testing Analysis

* Perform testing analysis—including formal and informal testing—to uncover defects tied to inadvertent operator actions:
  + Verify that the system’s error-handling mechanisms prevent cascading effects.
  + Use simulation environments to mimic realistic operator errors during various mission phases.

**Deliverables**:

* Testing analysis reports summarizing test coverage, safety-critical paths, and verified operator error scenarios.
* Trend data indicating testing coverage improvements over time.

### 7.2.7 SWE Work Product Assessments

Assess project SWE-related artifacts to confirm the correct implementation of safeguards for erroneous operator actions:

* **Software Test Plan**: Ensure proper testing of scenarios involving inadvertent operator actions.
* **Software Test Procedures and Reports**: Confirm traceability against error scenarios and hazards.
* **User Manuals**: Validate documentation that provides operators with error recovery procedures and system implications.

## 7.3 Metrics

Use the following metrics to monitor compliance with Requirement 4.3.3 and ensure robust software assurance.

### 7.3.1 Human Error Metrics

* **Number of identified human error hazards**: Track hazards related to inadvertent actions and associated mitigation strategies.
* **Likelihood evaluation completeness**: Confirm coverage for scenarios of human-induced command errors.

### 7.3.2 Verification and Validation Metrics

* **Test Coverage**: ~~%~~ percent of safety-critical software tested against error scenarios involving inadvertent operator actions.
* **Defect Density**: Count and analyze defects per thousand lines of code; target lower complexity in error-sensitive components.
* **Requirements Traceability**: Percent traceability of safety-critical requirements (e.g., error recovery mechanisms) to test cases.

### 7.3.3 Safety Metrics

* **Hazard Mitigations**: Number and effectiveness of mitigations defined for hazards originating from human error.
* **Safety-critical Compliance**: Verification artifacts showing test execution of safety-critical error cases.

### 7.3.4 Code Quality Metrics

* **Cyclomatic Complexity**: Average complexity in safety-critical components; flag if exceeding industry-standard thresholds (<15).
* **Static Analysis**: Number of unresolved errors flagged by analysis tools.

### 7.3.5 Performance Metrics

* **Response Time**: Time taken for the system to detect and recover from human error-induced disruptions.
* **Uptime**: Availability rate for systems under normal and degraded modes (safe fallback operations).

### 7.3.6 Configuration Management Metrics

* **Version Compliance**: Number of deviations from correct version baselines tracked and resolved.
* **Change Request Impact**: Number of changes affecting error recovery performance tracked over milestones.

### 7.3.7 Independent Verification and Validation Metrics

* **Participation**: Number of IV&V reviews attended; include IV&V feedback integration rate into delivered reports.
* **Coverage**: Percent of critical error cases assessed independently by IV&V audits and testing.

## 7.4 Guidance

To address this requirement in software assurance and ensure error tolerance, implement the following tasks effectively:

To ensure that the space system can tolerate inadvertent operator actions without causing catastrophic events, the following software assurance and software safety tasks should be implemented:

1. **Human Error Analysis**: Confirm that a detailed software error analysis is complete to identify potential operator errors that could lead to catastrophic events. This analysis should include various scenarios and the likelihood of each error occurring. This analysis should also include the various scenarios and the likelihood of each error occurring along with ensuring:   
   1. Comprehensive test coverage for scenarios involving inadvertent operator actions, including normal operations, failure modes, and recovery procedures.
   2. Tests for unexpected conditions, boundary conditions, and software/interface inputs will be performed including robust error handling and recovery mechanisms to address errors resulting from inadvertent operator actions.
   3. The project has developed and plans to execute simulations that model and test the impact of inadvertent operator actions. This includes conducting tests to verify that the software system can handle inadvertent actions without resulting in catastrophic consequences.
   4. Each requirement, including those for tolerating inadvertent operator actions, is traced to its implementation and corresponding test cases to maintain comprehensive coverage and validation.
2. **Simulations and Testing:** Ensure that the project has developed and executed simulations to model and test the impact of inadvertent operator actions. This includes conducting tests to verify that the system can handle at least one inadvertent action without resulting in catastrophic consequences.
3. **Test Witnessing**: Perform test witnessing for safety-critical software to ensure the impact of inadvertent operator actions is mitigated. (See [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)) This includes witnessing tests to:  
   1. Confirm that the system can handle inadvertent actions without resulting in catastrophic consequences. This could include: 
      1. Measuring the time taken for the system to detect and respond to inadvertent operator actions to ensure timely and accurate execution of mitigation procedures. A prolonged period could cause catastrophic consequences.
      2. Ensuring the system is available and operational when needed, especially during critical mission phases, to support tolerance of inadvertent operator actions.
   2. Uncover unrecorded software defects and confirm they get documented and recorded.
   3. Confirm there is robust error handling and recovery mechanisms to address errors resulting from inadvertent operator actions. This includes ensuring adequate error handling and that the system can recover from errors without leading to catastrophic events.
4. **Software Safety and Hazard Analysis**: Develop and maintain a Software Safety Analysis throughout the software development life cycle. Assess that the Hazard Analyses (including hazard reports) identify the software components associated with the system hazards per the criteria defined in NASA-STD- 8739.8, Appendix A. (See [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)) Perform these on all new requirements, requirement changes, and software defects to determine their impact on the software system's reliability and safety. Confirm that all safety-critical requirements related to tolerating inadvertent operator actions have been implemented and adequately tested to prevent catastrophic events during mission-critical operations. It may be necessary to discuss these findings during the Safety Review so the reviewers can weigh the impact of implementing the changes. (See Topic [8.58 – Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis).)
   1. **Hazard Analysis/Hazard Reports:**Confirm that a comprehensive hazard analysis was conducted to identify potential hazards related to inadvertent operator actions that could result from critical software behavior. This analysis should include evaluating existing and potential hazards and recommending mitigation strategies for identified hazards. The Hazard Reports should contain the results of the analyses and proposed mitigations (See Topic [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content))
   2. **Software Safety Analysis:** To develop this analysis, utilize safety analysis techniques such as [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) and [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) to identify potential hazards and failure modes. This helps in designing controls and mitigations for the operation of critical functions. When generating this SA product, see Topic [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) for additional guidance.
5. **Safety Reviews**: Perform safety reviews on all software changes and software defects. This ensures that any modifications do not introduce new vulnerabilities or increase the risk of inadvertent actions leading to catastrophic events.
6. **Peer Reviews**: Participate in peer reviews on all software changes and software defects affecting safety-critical software and hazardous functionality. (See [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) tasks.) This ensures that any modifications control the input of bad data and do not introduce new vulnerabilities or increase the risk of inadvertent actions leading to catastrophic events. 
   1. **Change Requests**: Monitor the number of software change requests and software defects and their impact on the system's reliability and safety. Increases in the number of changes may be indicative of requirements issues or code quality issues resulting in potential schedule slips. (See [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) , [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes))
7. **Test Results Assessment**: Confirm that test results are assessed and recorded and that the test results are sufficient verification artifacts for the hazard reports. (See [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) tasks.)
8. **Formal and Informal Testing**: Ensure that both formal and informal testing to uncover unrecorded software defects has been completed. This includes testing unexpected conditions, boundary conditions, and software/interface inputs.
9. **Automated Verification and Validation**: Confirm the use of automated tools for static analysis, dynamic analysis, code coverage, cyclomatic complexity, and other verification and validation activities. This helps identify potential software defects that could result in catastrophic events due to inadvertent operator actions. (See [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) ) 
   1. **Code Quality**: Use metrics such as cyclomatic complexity and static analysis results to ensure the code is maintainable and less prone to errors. Specifically, confirm that safety-critical software components have a cyclomatic complexity value of 15 or lower, or software developers must provide a technically acceptable rationale if this value is exceeded. (See [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software), [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis))
   2. **Code Coverage**: Confirm that 100% code test coverage is addressed for all identified software safety-critical software components or ensure that software developers provide a risk assessment explaining why the test coverage is impossible for the safety-critical code component. (See [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements), [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software))
   3. **Software Volatility**: Measure changes in the codebase to monitor stability and identify areas of frequent modification that may need more rigorous testing. (See [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics))
   4. **Verification Testing**: The verification analysis activity ensures that the safety requirements for the software were properly flowed down from the system safety requirements, traced to test/test procedures, and that they have been adequality tested. (See [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures), [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification), and Topic  [8.57 - Testing Analysis](https://swehb.nasa.gov/display/SWEHBVD/8.57+-+Testing+Analysis))
   5. **Validation Testing**: Software validation is a software engineering activity that shows confirmation that the software product, as provided (or as it will be provided), fulfills its intended use in its intended environment.  In other words, validation testing ensures that “you built the right thing.” (See [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation), [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools), [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations), and Topic [8.57 - Testing Analysis](https://swehb.nasa.gov/display/SWEHBVD/8.57+-+Testing+Analysis))
10. **Configuration Management**: Ensure that strict configuration management is maintained to ensure that the correct software versions and configurations are used. See [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) for more information. This reduces the risk of errors due to incorrect or inconsistent configurations, tracks changes, and maintains consistency. This also includes performing the [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) tasking.
11. **Training and Documentation**: Ensure comprehensive training and documentation for operators to minimize the chances of inadvertent actions is available. This includes clear instructions, warnings, and recovery procedures.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-194 - Delivery Requirements Verification](/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification) * [SWE-200 - Software Requirements Volatility Metrics](/spaces/SWEHBVD/pages/102695533/SWE-200+-+Software+Requirements+Volatility+Metrics) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) - * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence is the documentation, artifacts, or data that demonstrate this requirement has been addressed, implemented correctly, and verified through engineering processes. Below is a breakdown of the **required objective evidence** to support compliance with NASA's rigorous safety and assurance standards.

Objective evidence for Requirement 4.3.3 ensures that safety-critical software designs, development processes, and operational scenarios proactively account for and mitigate risks caused by inadvertent operator actions. Thorough documentation, traceability, testing, and validation artifacts support compliance while building mission confidence and robustness.

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

## 8.1 Requirements and Risk Management Evidence

#### **Traceability Artifacts**

* **Requirement Traceability Matrix (RTM)**:
  + Evidence that the requirement for tolerating inadvertent operator actions has been allocated, designed, implemented, and verified.
  + Links Requirement 4.3.3 to:
    - Software design features (e.g., validation checks, recovery mechanisms),
    - Safety-critical components,
    - Test cases and procedures for error scenarios.

#### **Risk Identification and Analysis**

* **Risk Assessment Reports**:

  + Identify risks stemming from inadvertent operator actions and their potential consequences (e.g., catastrophic system failures).
  + Evaluate the severity and likelihood of operator errors in simulation or operational conditions.
  + Evidence of applied mitigations (e.g., redundant systems, interlocks).
* **Risk Hazard Analysis Reports (RHA)**:

  + Documentation detailing hazard analysis and control measures designed to eliminate or mitigate operator action risks.

## 8.2 Software Safety Analysis Evidence

#### **Hazard Controls Verification**

* **Software Hazard Reports**:
  + Identify software-controlled functions where inadvertent operator actions could result in hazards.
  + Document hazard mitigations and link to specific software controls (e.g., automated rollbacks, lockouts).
  + Ensure hazard control verification through detailed test plans and procedures.

#### **Software Fault Tree Analysis (FTA)**:

* Fault tracing diagrams showing how erroneous operator inputs propagate through the software and validating implementation of error-tolerant mitigations.

#### **Failure Modes and Effects Analysis (FMEA)**:

* Evidence of systematic evaluation of potential software failure modes caused by erroneous inputs and their mitigations.

## 8.3 Design Evidence

#### **Human Error Analysis**

* **Reports Summarizing Human Error Analysis (HEMEA)**:
  + Documentation of systematically identified operator error scenarios and their mitigations.
  + Characterizes error likelihood and severity in various operational environments and stress conditions.

#### **Design Documentation**

* **Design Specifications**:

  + Documentation describing safeguards (e.g., layered confirmations, input validations, interlocks) applied to critical operator inputs.
  + Evidence the system separates safety-critical commands from routine operations.
  + Descriptions of automated recovery mechanisms in the design.
* **User Interface Evaluations**:

  + Records of Human Factors Engineering (HFE) assessments ensuring the interface minimizes user confusion and errors.
  + Design features that prevent inadvertent actions (e.g., grouping critical commands, requiring multi-step confirmations).
* **Safety-Critical Command Pathway Diagrams**:

  + Visual representation of command pathways showing layers of validation and safeguards implemented to prevent or recover from erroneous operator actions.

## 8.4 Verification and Validation Evidence

#### **Test Documentation**

* **Verification and Validation Test Results**:

  + Artifacts demonstrating the system can tolerate at least one inadvertent operator action without resulting in catastrophic consequences.
  + Validation of end-to-end scenarios, including:
    - Error injection cases (e.g., premature shutdown, invalid inputs to the system),
    - Boundary conditions testing.
* **Test Coverage Data**:

  + Reports confirming 100% test coverage for all safety-critical software components associated with error-tolerant functions.
  + Evidence from unit tests, integration tests, and system-level tests.
* **Error Recovery Test Reports**:

  + Results of tests verifying recovery mechanisms for inadvertent actions (e.g., automated rollback, failover recovery).
  + Record of system performance during fault detection and mitigation.
* **Failure Injection Testing Results**:

  + Evidence showing system response to simulated real-world human errors, focusing on recovery without catastrophic consequences.

#### **Validation Artifacts**

* **Validation Plan and Reports**:

  + Evidence supporting that the software fulfills the requirement to tolerate erroneous actions in realistic mission scenarios.
* **Simulation Reports**:

  + Logs and results from operational simulations that model inadvertent operator scenarios and prove safeguards work as intended.
* **Test Witness Reports**:

  + Documentation from witnessed test cases, particularly for safety-critical software behaviors, ensuring rigorous oversight during testing phases.

## 8.5 Source Code Quality Evidence

#### **Static and Dynamic Analysis**

* **Static Analysis Reports**:

  + Output from automated tools verifying:
    - Absence of unnecessary complexity in safety-critical functions (e.g., cyclomatic complexity ≤15 unless justified).
    - No integration or logic flaws in command input validation and error-recovery mechanisms.
* **Dynamic Analysis Reports**:

  + Evidence of runtime behavior analysis indicating the effectiveness of recovery mechanisms for erroneous operator actions.
  + Reports covering memory use, thread synchronization (if applicable), and fault isolation.

#### **Coding Standards Compliance**

* **Code Review Reports**:
  + Evidence from peer reviews and inspections confirming code implementing error tolerance adheres to software safety standards (e.g., **NASA-STD-8739.8**).
  + Records of any issues identified and remediated.

#### **Code Coverage Reports**:

* Evidence of test coverage for critical paths (e.g., command validation, recovery mechanisms) associated with the requirement to tolerate operator errors.
* Demonstrate that every safety-critical component is exercised during testing.

## 8.6 Configuration Management Evidence

#### **Version Data**

* **Configuration Baselines**:
  + Evidence confirming proper versioning and consistency of all software configurations for error-tolerant components.

#### **Change Control Documentation**:

* Records of software changes, particularly for safety-critical items or updates tied to Requirement 4.3.3.
* Justifications for changes and their impact assessments.

## 8.7 Training and Documentation Evidence

#### **User Manuals**

* Documentation explaining how operators:
  + Execute safety-critical procedures correctly.
  + Recognize and recover from inadvertent actions.
  + Understand implications of specific commands (e.g., step-by-step guides for overriding automated recovery mechanisms).

#### **Training Records**:

* Evidence that mission operators, test teams, and relevant personnel completed training to ensure proper system use and reduce the likelihood of human errors.

## 8.8 Peer and Independent Verification and Validation (IV&V)

#### **IV&V Evidence**

* **IV&V Analysis Reports**:

  + Independent assessments verifying the implementation of tolerance for inadvertent actions.
  + Evidence of error-tolerant behavioral testing and error reporting in reviewed software modules.
* **IV&V Peer Review Participation Reports**:

  + Records of IV&V feedback on software design, testing, and operational safeguards.

#### **Safety Peer Review Records**

* Evidence documenting discussions on error tolerance in major safety assessments.
* Peer-reviewed resolutions to potential gaps or identified risks.

## 8.9 Examples of Objective Evidence Artifacts

| **Artifact Type** | **Description** |
| --- | --- |
| Requirement Trace Matrix | Links Requirement 4.3.3 to software design, test plans, and validation artifacts. |
| Test Results Reports | Documents system response to operator errors and mitigations implemented. |
| Hazard Reports | Details hazard scenarios and risk mitigations for inadvertent actions. |
| Static Analysis Outputs | Verifies code quality and adherence to safety standards. |
| Test Witness Logs | Confirms systematic oversight for safety-critical test cases. |
| Simulation Reports | Proves safeguards through modeled real-world ergonomic and failure scenarios. |
| Validation Reports | Confirms end-user satisfaction and system performance under real-world conditions. |
