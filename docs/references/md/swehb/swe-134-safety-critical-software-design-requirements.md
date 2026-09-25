# SWE-134 - Safety-Critical Software Design Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695493. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements

SWE-134 - Safety-Critical Software Design Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695493)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695493&showCommentArea=true&showComments=true#addcomment)

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

3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software: 

a. The software is initialized, at first start and restarts, to a known safe state.  
b. The software safely transitions between all predefined known states.  
c. Termination performed by software functions is performed to a known safe state.  
d. Operator overrides of software functions require at least two independent actions by an operator.  
e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard.  
f. The software detects inadvertent memory modification and recovers to a known safe state.  
g. The software performs integrity checks on inputs and outputs to/from the software system.  
h. The software performs prerequisite checks prior to the execution of safety-critical software commands.  
i. No single software event or action is allowed to initiate an identified hazard.  
j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event.  
k. The software provides error handling.  
l. The software can place the system into a safe state.

## 1.1 Notes

These requirements apply to components that reside in a mission-critical or safety-critical system, and the components control, mitigate, or contribute to a hazard as well as software used to command hazardous operations/activities. 

## 1.2 History

Click here to view the history of this requirement: SWE-134 History

SWE-134 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.12 When a project is determined to have safety-critical software, the project shall ensure the following items are implemented in the software:  a. Safety-critical software is initialized, at first start and at restarts, to a known safe state. b. Safety-critical software safely transitions between all predefined known states. c. Termination performed by software of safety-critical functions is performed to a known safe state. d. Operator overrides of safety-critical software functions require at least two independent actions by an operator. e. Safety-critical software rejects commands received out of sequence, when execution of those commands out of sequence can cause a hazard. f.  Safety-critical software detects inadvertent memory modification and recovers to a known safe state. g. Safety-critical software performs integrity checks on inputs and outputs to/from the software system. h. Safety-critical software performs prerequisite checks prior to the execution of safety-critical software commands. i.  No single software event or action is allowed to initiate an identified hazard. j.  Safety-critical software responds to an off nominal condition within the time needed to prevent a hazardous event. k. Software provides error handling of safety-critical functions. l.  Safety-critical software has the capability to place the system into a safe state. m. Safety-critical elements (requirements, design elements, code components, and interfaces) are uniquely identified as safety-critical. n.  Incorporate requirements in the coding methods, standards, and/or criteria to clearly identify safety-critical code and data within source code comments. |
| Difference between A and B | No change |
| B | 3.7.2When a project is determined to have safety-critical software, the project manager shall implement the following items in the software:  a. Safety-critical software is initialized, at first start and at restarts, to a known safe state. b. Safety-critical software safely transitions between all predefined known states. c. Termination performed by software of safety-critical functions is performed to a known safe state. d. Operator overrides of safety-critical software functions require at least two independent actions by an operator. e. Safety-criticalsoftware rejects commands received out of sequence, when execution of those commands out of sequence can cause a hazard. f. Safety-criticalsoftware detects inadvertent memory modification and recovers to a known safe state. g. Safety-criticalsoftware performs integrity checks on inputs and outputs to/from the software system. h. Safety-criticalsoftware performs prerequisite checks prior to the execution of safety-critical software commands. i. No single software event or action is allowed to initiate an identified hazard. j. Safety-critical software responds to an off nominal condition within the time needed to prevent a hazardous event. k. Software provides error handling of safety-critical functions. l. Safety-critical software has the capability to place the system into a safe state. m. Safety-critical elements (requirements, design elements, code components, and interfaces) are uniquely identified as safety-critical. n. Requirements are incorporated in the coding methods, standards, and/or criteria to clearly identify safety-critical code and data within source code comments. |
| Difference between B and C | Changed "When a project is determined to have" to "If a project has " safety-critical software;  Added mission-critical software to the requirement;  Removed "Safety-Critical" from items a. - l. as the entire requirement pertains to it;  Changed "has the capability to"  to "can" in item l.;  Deleted items m. and n. |
| C | 3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:  a. The software is initialized, at first start and restarts, to a known safe state.  b. The software safely transitions between all predefined known states.  c. Termination performed by the software functions is performed to a known safe state.  d. Operator overrides of software functions require at least two independent actions by an operator.  e. The software rejects commands received out of sequence when the execution of those commands out of sequence can cause a hazard.  f. The software detects inadvertent memory modification and recovers to a known safe state.  g. The software performs integrity checks on inputs and outputs to/from the software system.  h. The software performs prerequisite checks prior to the execution of safety-critical software commands.  i. No single software event or action is allowed to initiate an identified hazard.  j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event.  k. The software provides error handling.  l. The software can place the system into a safe state. |
| Difference between C and D | No change |
| D | 3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:   a. The software is initialized, at first start and restarts, to a known safe state. b. The software safely transitions between all predefined known states. c. Termination performed by software functions is performed to a known safe state. d. Operator overrides of software functions require at least two independent actions by an operator. e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard. f. The software detects inadvertent memory modification and recovers to a known safe state. g. The software performs integrity checks on inputs and outputs to/from the software system. h. The software performs prerequisite checks prior to the execution of safety-critical software commands. i. No single software event or action is allowed to initiate an identified hazard. j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event. k. The software provides error handling. l. The software can place the system into a safe state. |

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
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) |

# 2. Rationale

Implementing safety-critical software or mission-critical software design requirements helps ensure that the systems are safe and that the safety-critical software or mission-critical software requirements and processes are followed.

Safety-critical and mission-critical software are integral to ensuring the reliability and safety of projects where failure could result in catastrophic consequences, including loss of life, equipment, data, or mission objectives. Implementing the specified requirements ensures that the software operates in a robust, predictable, and safe manner even in adverse or unexpected circumstances.

Each provision of this requirement is designed to reduce risks associated with software malfunctions or operator errors in environments where safety and mission success are paramount. Implementing these measures protects against hazards, preserves asset integrity, and ensures compliance with industry safety standards for critical software systems. Failure to incorporate these safety mechanisms could lead to catastrophic outcomes, including harm to personnel, equipment failure, mission compromise, or environmental hazards. This requirement reinforces a culture of safety, reliability, and robust design within projects of high consequence.

Below is a clear and direct rationale for each sub-requirement:

## 2.1 The software is initialized, at first start and restarts, to a known safe state.

* Ensures that the system begins operation from a predefined stable, hazard-free condition, mitigating risks associated with unpredictable or unsafe states during boot-up or restart.

## 2.2  The software safely transitions between all predefined known states.

* Guarantees that transitions between operational states occur in a controlled, safe manner, reducing the risk of unexpected states leading to hazards or system instability.

## 2.3  Termination performed by software functions is performed to a known safe state.

* Ensures safe system shutdown or termination, preventing erratic behavior or lingering hazardous conditions during cessation of operations.

## 2.4  Operator overrides of software functions require at least two independent actions by an operator.

* Reduces the likelihood of accidental or unintended overrides, ensuring intentional and deliberate operator input before changing critical functions, thus minimizing human error.

## 2.5  Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard.

* Prevents unsafe outcomes from commands being executed in a potentially hazardous order, maintaining control and integrity of the system's operations.

## 2.6  The software detects inadvertent memory modification and recovers to a known safe state.

* Inadvertent memory modifications caused by errors or hardware faults could lead to unpredictable system behavior. Detection and recovery ensure the system returns to a stable and non-hazardous state, preserving safety.

## 2.7  The software performs integrity checks on inputs and outputs to/from the software system.

* Validates the correctness of critical data that influences system behavior, ensuring erroneous or corrupted data does not lead to unsafe operations or states.

## 2.8  The software performs prerequisite checks prior to the execution of safety-critical software commands.

* Verifies that all preconditions are met before executing critical commands, avoiding scenarios where premature execution could result in hazards or compromised reliability.

### 2.9  No single software event or action is allowed to initiate an identified hazard.

* Introduces redundancy and barriers to prevent system hazards from being caused by a single point of failure, thereby increasing fault tolerance and safety.

### 2.10 The software responds to an off-nominal condition within the time needed to prevent a hazardous event.

* Timely responses to abnormal conditions ensure proactive mitigation of risks and prevent escalation into hazardous events, preserving the system's safe operation.

## 2.11  The software provides error handling.

* Robust error handling prevents unhandled faults from destabilizing the system and propagating unsafe conditions, ensuring reliable continuance or controlled recovery.

## 2.12 The software can place the system into a safe state.

* Provides an ultimate safeguard by ensuring the system can be intentionally moved into a safe condition under any circumstances, mitigating risks from unforeseen failures or hazards.

# 3. Guidance

## 3.1 Safety-Critical Software and Mission-Critical Software

This requirement applies to safety-critical software and mission-critical software.  These items are design practices that should be followed when developing safety-critical software and mission-critical software.

**Software safety requirements contained in NASA-STD-8739.8B**

Derived from NPR 7150.2D para 3.7.3 SWE 134: Table 1, SA Tasks 1 - 6

1. Analyze the software requirements and the software design and work with the project to implement NPR 7150.2 requirement items "a" through "l."

2. Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone.

3. Confirm that the values of the safety-critical loaded data, uplinked data, rules, and scripts that affect hazardous system behavior have been tested.

4. Analyze the software design to ensure the following:  
   a. Use of partitioning or isolation methods in the   
         design and code,  
   b. That the design logically isolates the safety-critical   
         design elements and data from those that are   
         non-safety-critical.

5. Participate in software reviews affecting safety-critical software products.

6. Ensure the SWE-134 implementation supports and is consistent with the system hazard analysis.

See the software assurance tab for additional guidance material.

See also [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements), Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements).

## 3.2 Requirement Notes

The following clarifications and enhancements aim to make the guidance more precise, actionable, and relevant for practical software engineering applications. The goal is to improve the interpretability of requirements while providing specific measures to ensure compliance.

### **Item a**: *(The software is initialized, at first start, and restarts, to a known safe state.)*

* **Improved Guidance:**  
  A *known safe state* is a system state where hazards are mitigated, and the system is ready for reliable operation. To establish this state, ensure that the following components are inspected and verified:
  + **Hardware state**: Ensure hardware configuration matches predefined, verified initialization parameters. Include hardware self-test routines during the startup sequence.
  + **Software state**: Confirm critical software modules are loaded correctly, and any volatile settings are initialized to nominal values.
  + **Operational phase**: Validate initial operational mode (e.g., standby mode vs. active operation) based on system requirements.
  + **Device capability**: Verify hardware fault indicators and ensure initial settings are compatible with device tolerances.
  + **Configuration**: Ensure network, file system, and device configurations are consistent with system specifications.
  + **Memory integrity**: Perform integrity checks on boot code and file allocation tables before system initialization.

### **Item d**: *(Operator overrides of software functions require at least two independent actions by an operator.)*

* **Improved Guidance:**  
  Requiring multiple, independent actions reduces the risks of accidental overrides by human operators. Examples include:
  + Physical actions, such as pressing two separate buttons simultaneously or sequentially within a confirmed timeframe.
  + Logical actions, such as entering an override confirmation in the software followed by user authentication or a verification code.
  + Independent actions must require distinct input mechanisms (e.g., touchscreen + physical button) or software contexts (e.g., separate windows or modes).  
    This approach minimizes the probability of unintended actions resulting from human error or confusion.

### **Item f**: *(The software detects inadvertent memory modification and recovers to a known safe state.)*

* **Improved Guidance:**  
  Inadvertent memory modifications can have catastrophic impacts, particularly in systems exposed to extreme environments (e.g., radiation environments). The following strategies can mitigate these risks:
  + **Detection mechanisms**:
    - Implement error detection codes (EDC), such as parity checks, cyclic redundancy checks (CRC), and checksums.
    - Use memory protection hardware features, such as memory access control (lock bits) and write protection.
    - Monitor dynamic memory access for anomalies using runtime validation routines.
  + **Recovery mechanisms**:
    - Utilize error-correcting codes (ECC) to correct bit errors where feasible.
    - Periodically scrub memory (e.g., refresh memory cells and correct errors in non-volatile memory).
  + **Prevention strategies**:
    - Employ software authentication (e.g., verifying code and data integrity before execution).
    - Design memory partitioning to isolate critical portions from non-critical areas.

### **Item g**: *(The software performs integrity checks on inputs and outputs to/from the software system.)*

* **Improved Guidance:**  
  Input-output integrity is essential for safe system behavior. Design guidelines include:
  + **Input validation**:
    - Validate nominal input ranges during run-time and reject out-of-spec inputs.
    - Detect and mitigate transient startup input anomalies using low-pass filters or stabilization logic.
  + **Output verification**:
    - Implement sanity checks on output settings before external actuation (e.g., throttle limits or safety valve thresholds).
  + **Interface documentation**:
    - Provide detailed interface specifications including expected ranges, timing requirements, and fault conditions.
    - Include clear contingency actions in case of interface errors or anomalies (e.g., fallback routines).

### **Item h**: *(The software performs prerequisite checks prior to the execution of safety-critical software commands.)*

* **Improved Guidance:**  
  Prerequisite checks ensure that commands are executed in the correct operational sequence, mode, and state. To achieve this:
  + **Sequence validation**:
    - Design command sequencing rules to identify inappropriate or unsafe sequences. For example, transitions between modes or states must follow predefined workflows.
  + **Mode/state verification**:
    - Verify device or system state compatibility before executing safety-critical commands (e.g., ensure a "disarmed state" before entering maintenance mode).
  + **Command gating**:
    - Implement logic that prohibits execution of commands until all prerequisites are explicitly met. This includes environmental conditions, sensor validation, and operator confirmation.

### **Item j**: *(The software responds to an off-nominal condition within the time needed to prevent a hazardous event.)*

* **Improved Guidance:**  
  The system must proactively detect and respond to off-nominal conditions within required timeframes to prevent hazards. Key considerations include:
  + **Detection mechanisms**: Sensors must identify anomalies such as temperature thresholds, out-of-bounds motion, or voltage variations.
  + **Response timing**:
    - Perform real-time timing analysis to ensure mitigation routines execute within specified windows.
    - Include fail-safe mechanisms that trigger mitigation when fault detection exceeds real-time processing capability.
  + **Mitigation strategies**:
    - Correct faults when possible (e.g., failed sensor recalibration).
    - Transition to a known safe state when fault correction or continuation is infeasible.

### **Item k**: *(The software provides error handling.)*

* **Improved Guidance:**  
  Robust error handling ensures runtime faults or failures do not escalate into hazards. Design considerations for error handling include:
  + **Fault detection**:
    - Integrate mechanisms to detect operational, hardware, and software anomalies.
  + **Error isolation**:
    - Segment error-handling routines to prevent propagation of faults across system boundaries (e.g., isolate affected subsystems).
  + **Error recovery**:
    - Choose recovery techniques including rollback operations, system resets, or fallback modes based on fault criticality.
  + **Minimization of common failure modes**:
    - Apply design redundancy to eliminate single points of failure (e.g., replicate critical subsystems).
    - Explicitly handle all exception cases within software, rather than relying on default behavior.

### **Item l**: *(The software can place the system into a safe state.)*

* **Improved Guidance:**  
  A safe state ensures all hazards are neutralized while retaining limited system functionality if feasible. Guidelines for achieving a safe state include:
  + **Safe state definition**:
    - Establish specific safe states early in system design. Examples include "disarmed" mode, "power off", or "standby mode".
  + **Sensor design**:
    - Design fault-tolerant sensors capable of robustly monitoring hazardous conditions and accurately transitioning the system into a safe state during detection.
  + **Verification**:
    - Validate safe-state transitions through rigorous testing and failure mode analysis to ensure all paths lead to non-hazardous conditions.
  + **Timed response**:
    - Ensure software can achieve the safe state transition within the time constraints imposed by the hazardous condition.

### **Additional Safety-Critical Software Design Guidelines**

(Note: Improved to enhance readability and applicability.)

1. **Minimize complexity**: Keep safety-critical code simple and testable. Review code with complexity metrics above threshold (e.g., cyclomatic complexity > 15).
2. **Avoid unsafe constructs**: Disallow recursion, `goto`, and infinite loops. Ensure bounds are fixed for loops.
3. **Heap memory**: Avoid dynamic memory allocation at runtime; preallocate memory during initialization.
4. **Assertions**: Use at least two runtime assertions per function to enforce assumptions and invariants.
5. **Pointer usage**: Limit pointer usage to non-functional pointers, and avoid multiple dereferences where possible to reduce error risks.
6. **Compile rigorously**: Enable all compiler warnings, and resolve them prior to software release.
7. **Security**: Apply security best practices at all development levels, including data validation, boundary checks, and threat mitigation measures.

Improving safety-critical software design reduces risks and builds resilience in systems where safety, reliability, and performance are paramount.

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing), [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software). If software is acquired from a supplier, see Topic [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance).  See also Topic [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements), [7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance), 

See also [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)

Participate in peer reviews on all software changes and software defects affecting safety-critical software and hazardous functionality: [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action), 

## 3.3 Checklist for Safety-Critical or Mission-Critical Software

 The checklist in **PAT-035 - Checklist for Safety-Critical or Mission-Critical Software** [PAT-035](#tabs-5) may be used to review the items in this requirement. Download the worksheet and make any modifications necessary for your project. Use the checklist as many times as necessary. 

**PAT-035 - Checklist for Safety-Critical or Mission-Critical Software**

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-035 - Checklist for Safety-Critical or Mission-Critical Software**

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) * [7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-035 - Checklist for Safety-Critical or Mission-Critical Software](/spaces/SITE/pages/180584532/PAT-035+-+Checklist+for+Safety-Critical+or+Mission-Critical+Software) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

# 4. Small Projects

The following simplified guidance is tailored for small projects where resources, complexity, and scope are more limited. The focus for small projects is maximizing safety with streamlined processes and practical implementation.

## 4.1 General Approach for Small Projects

1. **Prioritize Safe States**: Even in small projects, define concrete safe states early and ensure these states are achievable in failures or hazards.
2. **Simplify Design**: Minimize software complexity while ensuring all safety-critical functions are deterministic, reliable, and testable.
3. **Automate Safety Features**: When possible, automate detection, recovery, and safe-state transitions to minimize reliance on operator intervention.
4. **Leverage Tools**: Utilize existing software libraries, tools, or hardware capabilities to implement safety features (e.g., memory protection or error correction) without reinventing systems.

## 4.2 Item-Specific Guidance for Small Projects

#### **Item a**: *(The software is initialized, at first start and restarts, to a known safe state.)*

* Simplify initialization routines by ensuring the system starts in a default, non-hazardous state (e.g., powered off motors, communications disabled).
* Perform basic checks, such as verifying hardware status (e.g., sensors reading nominal values) and initializing software configurations to default, tested settings.

#### **Item d**: *(Operator overrides of software functions require at least two independent actions by an operator.)*

* Require two distinct actions, such as:
  + Physically pressing two separate buttons or switches.
  + Software and hardware confirmation, such as entering an override password and simultaneously toggling a hardware switch.
* Avoid complex override procedures; keep it simple but effective (e.g., "Confirm action" prompts with a second verification step).

#### **Item f**: *(The software detects inadvertent memory modification and recovers to a known safe state.)*

* Use basic error detection mechanisms available in hardware (e.g., parity checks or watchdog timers).
* Perform regular memory integrity checks on critical variables, especially after system interruptions or major events like resets.
* Define a fallback routine that resets or reinitializes the system in case memory corruption is detected.

#### **Item g**: *(The software performs integrity checks on inputs and outputs to/from the software system.)*

* Validate all inputs as a simple check (e.g., confirm values are within expected ranges) before acting on them.
* Ensure outputs are validated before execution (e.g., limit physical actuation commands to avoid damaging hardware or creating unsafe conditions).
* Document and test all interface specifications, defining acceptable inputs/outputs explicitly.

#### **Item h**: *(The software performs prerequisite checks prior to the execution of safety-critical commands.)*

* Implement basic checks for prerequisites, such as ensuring the system is in the right state (e.g., standby mode) before executing a command.
  + Example: If a command requires the system to be powered on, reject commands when the system is off.
* Use simple rules that prevent unsafe sequencing, such as "command A must always precede command B."

#### **Item j**: *(The software responds to an off-nominal condition within the time needed to prevent a hazardous event.)*

* Detect abnormal conditions (e.g., sensor failure or hardware faults) and respond immediately by:
  + Logging the fault and disabling unsafe system components.
  + Transitioning to a predefined safe state, such as pausing operations safely.
* Use simple timers to ensure mitigation routines execute within required time limits.

#### **Item k**: *(The software provides error handling.)*

* Simplify error handling by focusing on:
  + Detection: Include basic fault checks, such as unavailable hardware or invalid inputs.
  + Isolation: Deactivate affected components (e.g., disable a jammed actuator).
  + Recovery: Reset operations to a known safe state or restart the system as a fallback.

#### **Item l**: *(The software can place the system into a safe state.)*

* Define safe states early such as “stop all motion,” “power down non-critical systems,” or “disable unsafe components.”
* Ensure basic sensors can identify hazards (e.g., temperature sensors for overheating) that trigger safe-state transitions.
* Verify through testing that the system successfully transitions to safe states under various fault conditions.

## 4.3 Additional Streamlined Design Guidelines for Small Projects

1. **Simplify Code**:
   * Code complexity should remain low (e.g., cyclomatic complexity < 10). Avoid recursive functions and excessive branching.
   * Use small, modular functions with clear entry and exit points to make testing and debugging easier.
2. **Limit Dependencies**:
   * Use simple constructs (e.g., `if` and `switch` instead of `goto`).
   * Avoid relying on dynamic memory allocation (use arrays or preallocated buffers).
3. **Error Prevention**:
   * Always check function return values (for errors) and handle them appropriately.
   * Use assertions to enforce conditions during execution (e.g., "value X must always be positive").
4. **Testing**:
   * Test all code paths for both nominal and off-nominal conditions.
   * Automate safety-critical tests where possible to reduce errors during validation.
5. **Safety Documentation**:
   * Create simple documentation defining safe states, prerequisites, interfaces, and mitigation actions.
   * Keep records streamlined but explicit, focusing on actions necessary to maintain safety.

## 4.4 Simplified Off-the-Shelf Solutions

Small projects can leverage existing tools or hardware/software features to meet safety requirements efficiently:

* **Error detection/recovery**: Use processors or microcontrollers with built-in ECC, memory parity checking, and interrupts.
* **Software validation**: Many development platforms (e.g., Arduino, Raspberry Pi) provide libraries for input/output validation, timers, and fail-safe measures.
* **State handling**: Develop state machines using modular approaches, making transitions between known states easy to program and test.

By leveraging simple, streamlined strategies and focusing on safety-critical aspects, small projects can achieve compliance with these requirements without unnecessary complexity or resource strain.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-014)

  [Computer-Based Control System Safety Requirements](https://swehb.nasa.gov/download/attachments/16450414/SSP%2050038-Rev%20C.docx?api=v2 "Click to open in new window")

  SSP 50038, Revision C, NASA International Space Station Program, 1995.
* (SWEREF-017) Constellation Computing Safety Requirements, CxP 70065, Revision A, 2005.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-260)

  [NASA Fault Management Community of Practice](https://nen.nasa.gov/web/faultmanagement "Click to open in new window")

  This NASA-only resource is available to NASA-users at https://nen.nasa.gov/web/faultmanagement.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-375)

  [IEC 62304](https://en.m.wikipedia.org/wiki/IEC_62304# "Click to open in new window")

  IEC 62304:2006, Medical device software — Software life cycle processes A copy of this standard is available from https://www.iso.org/standard/38421.html
* (SWEREF-376)

  [ISO 26262](https://en.m.wikipedia.org/wiki/ISO_26262 "Click to open in new window")

  ISO 26262-1:2011, Road vehicles — Functional safety — Part 1: Vocabulary A copy of this standard is available from: https://www.iso.org/standard/43464.html
* (SWEREF-432)

  [Overview of the DART Mishap Investigation Results.](http://www.nasa.gov/pdf/148072main_DART_mishap_overview.pdf "Click to open in new window")

  For Public Release. (2006). Lessons Learned Reference.
* (SWEREF-521)

  [Deficiencies in Mission Critical Software Development for Mars Climate Orbiter (1999)](https://llis.nasa.gov/lesson/740 "Click to open in new window")

  Public Lessons Learned Entry: 740.
* (SWEREF-603)

  [MCDC Coverage Video example.](https://www.youtube.com/watch?v=Cg1J-_ReKmM "Click to open in new window")

  Carnegie Mellon University course 18-642 updated Fall 2020, Koopman, Phil
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Process Asset Templates

Click on a link to download a usable copy of the template.

* (PAT-035 - )

  [PAT-035 - Checklist for Safety-Critical or Mission-Critical Software](https://swehb.nasa.gov/download/attachments/180584532/PAT-035%20-%20Checklist%20for%20Safety-Critical%20or%20Mission-Critical%20Software.xlsx?api=v2 "Click to open in new window")

  SWE-134, For use in checking aspects of Safety-Critical or Mission-Critical Software.
* (PAT-036 - )

  [PAT-036 Software Architecture and Design Process Audit](https://swehb.nasa.gov/download/attachments/198770701/PAT-036%20-%20Architecture%20and%20Design%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Architecture and Design.
* (PAT-038 - )

  [PAT-038 - Implementation Process Audit](https://swehb.nasa.gov/download/attachments/198770739/PAT-038%20-%20Implementation%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Implementation Process.
* (PAT-042 - )

  [PAT-042 - Requirements Development and Mgmt Audit](https://swehb.nasa.gov/download/attachments/198770759/PAT-042%20-%20Requirements%20Development%20and%20Mgmt%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to Software Requirements Development and Management.
* (PAT-044 - )

  [PAT-044 - Software Hazard Development Process Audit](https://swehb.nasa.gov/download/attachments/198770763/PAT-044%20-%20Software%20Hazard%20Development%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Hazard Development Process.
* (PAT-045 - )

  [PAT-045 - Software Peer Review Inspection Report Audit](https://swehb.nasa.gov/download/attachments/198770772/PAT-045%20-%20Software%20Peer%20Review%20Inspection%20Report%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Peer Review Inspection Report Process.
* (PAT-046 - )

  [PAT-046 - Test Verification and Validation Process Audit](https://swehb.nasa.gov/download/attachments/198770767/PAT-046%20-%20Test%20Verification%20and%20Validation%20Process%20Audit.docx?api=v2 "Click to open in new window")

  Topic 8.12, Checklist for Auditing the SWE Requirements related to the Software Test Verification and Validation Process.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

**LL‑SW‑11 — COTS/Reuse Software Policy for Safety‑Critical Systems**

* **Source LL ID(s):** GW‑SMA‑LL‑069, GW‑SMA‑LL‑082 (CBCS)
* **Discipline(s):** Computer‑Based Control Systems (CBCS), Software Assurance
* **Context/Background:** Teams struggled to apply NPRs to COTS/reuse; safety controls were missing in COTS; design changes and insight were difficult.
* **Lesson Learned:** Create program‑specific **COTS/reuse policy** clarifying applicability of NPR 7150.2/standards to CBCS, including safety control expectations.
* **Evidence/Observation:** Reliability/availability/upgradeability issues with COTS critical items; provider resistance to design insights.
* **Cause(s):** Undefined requirements/expectations; lack of upfront safety control provisions.
* **Recommendation/Corrective Action:** Update Agency NPRs/standards (or tailor for program) to address COTS in human‑rated contexts; perform early feasibility analysis against safety controls.
* **Implementation Guidance:** Align with **SWE‑027** (COTS/legacy), **SWE‑133/134** (safety determination & safety‑critical), **SWE‑158** (security).
* **Success Criteria/Verification:** Documented COTS policies; hazard controls traceable to requirements; successful verification closeouts.
* **Applicability/Scope:** All safety‑critical CBCS, avionics, and integrated systems.
* **Related Standards/Requirements:** **SWE‑027, SWE‑133, SWE‑134, SWE‑158**.

**LL‑SW‑13 — Centralize Safety Requirements and Clarify Verification Closeout**

* **Source LL ID(s):** GW‑SMA‑LL‑007, GW‑SMA‑LL‑033 (SE&I)
* **Discipline(s):** SE&I, Software, CBCS
* **Context/Background:** Safety requirements scattered across subsystem specs; unclear verification responsibilities/closure at L3 caused confusion.
* **Lesson Learned:** Maintain a **single S&MA requirements document** with clear verification strategies, roles, and cross‑level closure definitions.
* **Evidence/Observation:** L3 compliance and verification closure not understood; differences for hardware delivery vs. integrated configuration.
* **Cause(s):** Distributed ownership; late/immature TVV tools/processes.
* **Recommendation/Corrective Action:** Decompose L2→L3 requirements; define verification terminology and responsibilities early; maintain numbering/titles/types.
* **Implementation Guidance:** **SWE‑050** (requirements captured/maintained), **SWE‑052/072** (traceability), **SWE‑018** (reviews).
* **Success Criteria/Verification:** Auditable verification closure at provider and integrated levels; consistent numbering and traceability reports.
* **Applicability/Scope:** All elements and interfaces.
* **Related Standards/Requirements:** **SWE‑050, SWE‑052, SWE‑072, SWE‑018**.

**LL‑SW‑14 — Strengthen Fault Tolerance Requirements**

* **Source LL ID(s):** GW‑SMA‑LL‑011 (IHA)
* **Discipline(s):** Software Safety, SE&I, CBCS
* **Context/Background:** Wording emphasized single‑fault tolerance; permanent crew goals argue for dual‑fault tolerance in many cases.
* **Lesson Learned:** Encourage **dual+ fault tolerance** for systems supporting crewed missions, aligning with long‑duration requirements.
* **Evidence/Observation:** Gateway’s short crewed periods differed from Moon Base permanence; ISS practices emphasize dual FT.
* **Cause(s):** Ambiguous FT wording; provider minimal compliance.
* **Recommendation/Corrective Action:** Update safety requirement language; define explicit FT targets and verification.
* **Implementation Guidance:** **SWE‑133/134** (safety determination/safety‑critical requirements), **SWE‑050** (requirements).
* **Success Criteria/Verification:** Documented FT analyses; verification evidence across nominal and off‑nominal scenarios.
* **Applicability/Scope:** Safety‑critical software and interfaces.
* **Related Standards/Requirements:** **SWE‑133, SWE‑134, SWE‑050**.

**LL‑SW‑15 — Early Safety Applicability to “Uncrewed” Systems that Interface with Crew**

* **Source LL ID(s):** GW‑SMA‑LL‑102
* **Discipline(s):** Procurement, Contracting, Requirements
* **Context/Background:** PPE initially excluded from human‑rating reqs; later interfaces with crewed systems demanded safety compliance, causing costly remedies.
* **Lesson Learned:** Apply **safety requirements early** to any system that **interfaces** with crewed systems.
* **Evidence/Observation:** Delays/confusion in HR scope and expensive fixes to improve.
* **Cause(s):** Procurement/requirements processes lacked SMA inputs.
* **Recommendation/Corrective Action:** Engage SMA in procurement; include safety clauses in contracts; classify software appropriately (SWE‑020/160/133).
* **Implementation Guidance:** **SWE‑020** (classification), **SWE‑133/134** (safety), **SWE‑013** (planning).
* **Success Criteria/Verification:** No late adds of safety requirements; HR scope correct at start; reduced variance requests.
* **Applicability/Scope:** All interfacing systems, crew‑adjacent.
* **Related Standards/Requirements:** **SWE‑020, SWE‑133, SWE‑134, SWE‑013**.

**LL‑SW‑19 — Security of Interfaces that Are Hazard Controls**

* **Source LL ID(s):** GW‑SMA‑LL‑046 (flag interface req/verification tied to hazard control)
* **Discipline(s):** SE&I, IHA, Software Requirements
* **Context/Background:** DNG lacked attribute to flag when interface requirement/verification implements a hazard control; gaps and IHCRs increased.
* **Lesson Learned:** Add explicit **tool attributes/flags** to mark interface requirements/verifications that serve as hazard controls; set early in lifecycle.
* **Evidence/Observation:** Beneficial to reduce IHCRs and clarify cross‑element dependencies.
* **Cause(s):** Attribute never implemented; ICD/IDD artifacts were outside DNG.
* **Recommendation/Corrective Action:** Implement DNG attribute; define process to set flags prior to hazard Phase II.
* **Implementation Guidance:** **SWE‑052/072** (traceability) and **SWE‑050** (requirements) for consistent cross‑artifact linking and reporting.
* **Success Criteria/Verification:** Interface hazard controls are discoverable via reports; fewer transfer requests; clearer verification ownership.
* **Applicability/Scope:** All interface‑heavy systems.
* **Related Standards/Requirements:** **SWE‑050, SWE‑052, SWE‑072**.

Early planning and coordination between **Software Engineering**, **Software Safety**, and **Software Assurance** teams regarding the applicability and implementation of the **SWE-134 software safety requirements** are crucial for identifying and mitigating software-related risks. This proactive approach reduces schedule impacts, prevents costly late-phase rework, and ensures consistent adherence to safety and mission-critical requirements. Effective early collaboration establishes clear roles and responsibilities for identifying safety-critical software, performing hazard analysis, and verifying compliance with software safety standards.

**Deficiencies in Mission Critical Software Development for Mars Climate Orbiter (MCO) (1999)**  
**Lesson Number 0740: "Ensure Consistent Unit Conventions and Formal Software Review Processes"**

* **Context**: The Mars Climate Orbiter was lost due to a conversion error in the "Sm\_forces" program, which output data in English units (pounds-force seconds) instead of the required metric units (Newton-seconds). This discrepancy caused navigational errors that ultimately resulted in mission failure.
* **Summary of Lessons Learned**:

  + The loss was directly tied to insufficient software safety planning and software engineering integration. Software Assurance and Safety teams were not fully engaged early in the software lifecycle, resulting in the omission of critical checks for unit consistency. This highlights the importance of rigorous software reviews, staff participation in design walkthroughs, and adequate training on software safety practices.
  + Mission-critical software must be clearly identified, and both software and operational requirements need robust traceability to safety requirements like SWE-134.
  + Formal **unit consistency verifications** should be explicitly tested and reviewed to prevent errors during design and implementation.
* **Recommendations**:

  1. **Identify Mission-Critical Software Early**: Collaborate between software engineering and the software safety team early to identify mission-critical and safety-critical software through a structured review process.
  2. **Enforce Rigorous Software Review Practices**: Ensure participation of software assurance and safety staff in major software lifecycle events (design reviews, code walkthroughs, and test result reviews).
  3. **Standardize Units and Parameters**: Verify the consistency of all engineering units and key system parameters to prevent misinterpretations during data handling between systems.
  4. **Train Key Personnel**: Provide training for staff to identify safety risks, perform software reviews, conduct hazard analyses, and comply with SWE-134 safety requirements.
  5. **Include Unit Validation in Test Plans**: Integrate unit validation, consistency checks, and data flow validation as part of formal software tests.
* **Key Takeaway**: The Mars Climate Orbiter mission underscores the importance of proactive software safety planning and coordination. SWE-134 requirements (e.g., ensuring hazard analyses are performed and validated, consistent engineering practices, error detection, and fault handling) need to be embedded early in the software lifecycle to avoid mission-critical errors and delays.

#### Broader Applications from This Lesson:

The MCO lessons emphasize the following additional actions to implement safety-critical software effectively and mitigate failure risks:

* **Cross-Disciplinary Coordination**: Create a collaborative environment where software engineers, systems engineers, and hazard analysts work together to ensure all safety-critical software is properly identified, validated, and reviewed.
* **Integrated Safety and Mission Assurance**: Leverage SMA input during software testing and V&V processes to identify risks related to data handling, unit conversions, and fault handling.
* **Automated Verification Tools**: Use validation tools to check for critical issues like parameter mismatches, inconsistent interfaces, or unit errors during development, testing, and integration.

By addressing these lessons early in the planning and development phases, project managers can avoid the devastating consequences of inadequate software safety practices, as seen in the Mars Climate Orbiter mission.

* **Undefined and Insufficiently Tested Fault Protection**

**Incident:**  
Fault protection logic was not fully defined or validated prior to the launch delay, leaving mission‑critical behaviors unverified.

**Lesson Learned:**

* + **Early Fault Management Definition:** Fault detection, isolation, and recovery logic must be fully specified and integrated into system testing well before ATLO.
  + **Hazard‑Driven Validation:** Fault responses must be validated against hazards and off‑nominal scenarios using high‑fidelity simulations.

**Implication:**  
Incomplete fault protection risks spacecraft safety, autonomy, and ability to recover from anomalies during critical mission phases.

## 6.2 Other Lessons Learned

* **Demonstration of Autonomous Rendezvous Technology (DART) spacecraft Type A Mishap[432](#_tabs-<p></p>)**: "NASA has completed its assessment of the DART MIB (Mishap Investigation Board) report, which included a classification review by the Department of Defense. The report was NASA-sensitive but unclassified because it contained information restricted by International Traffic in Arms Regulations (ITAR) and Export Administration Regulations (EAR). As a result, the DART mishap investigation report was deemed not releasable to the public." The LL also "provides an overview of publicly releasable findings and recommendations regarding the DART mishap."
* The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

  + [Test all commands to GNC simulated hardware](https://software.gsfc.nasa.gov/lesson-details/345/). **Lesson Number 345**: The recommendation states: "Once the Spacecraft Command and Telemetry database is established, test all defined GNC hardware commands against the spacecraft simulator."

# 7. Software Assurance

**SWE-134 - Safety-Critical Software Design Requirements**

3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:

a. The software is initialized, at first start and restarts, to a known safe state.  
b. The software safely transitions between all predefined known states.  
c. Termination performed by software functions is performed to a known safe state.  
d. Operator overrides of software functions require at least two independent actions by an operator.  
e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard.  
f. The software detects inadvertent memory modification and recovers to a known safe state.  
g. The software performs integrity checks on inputs and outputs to/from the software system.  
h. The software performs prerequisite checks prior to the execution of safety-critical software commands.  
i. No single software event or action is allowed to initiate an identified hazard.  
j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event.  
k. The software provides error handling.  
l. The software can place the system into a safe state.

## 7.1 Tasking for Software Assurance

**Software safety requirements contained in NASA-STD-8739.8B**

Derived from NPR 7150.2D para 3.7.3 SWE 134: Table 1, SA Tasks 1 - 6

1. Analyze the software requirements and the software design and work with the project to implement NPR 7150.2 requirement items "a" through "l."

2. Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone.

3. Confirm that the values of the safety-critical loaded data, uplinked data, rules, and scripts that affect hazardous system behavior have been tested.

4. Analyze the software design to ensure the following:  
   a. Use of partitioning or isolation methods in the   
         design and code,  
   b. That the design logically isolates the safety-critical   
         design elements and data from those that are   
         non-safety-critical.

5. Participate in software reviews affecting safety-critical software products.

6. Ensure the SWE-134 implementation supports and is consistent with the system hazard analysis.

## 7.2 Software Assurance Products

This revised guidance aims to enhance clarity, practicality, and alignment with safety-critical software needs while emphasizing early integration, risk management, and consistent assessment throughout the software life cycle.

### 7.2.1. Software Assurance Status Reports:

* Provide regular updates on the implementation status and compliance of safety-critical design elements related to items "a" through "l."
* Include progress tracking, identified risks, and mitigation strategies to help maintain visibility and accountability throughout the life cycle.

### 7.2.2 Software Design Analysis:

* Conduct thorough analysis of software requirements and design to confirm implementation of items "a" through "l." This includes checking for logical consistency, feasibility, and safety within the project's operational context.
* Specifically, analyze the design to ensure compliance with:
  + Items **a** and **b**: Verify that initial states, safe states, and transitions between them are well-defined, tested, and achievable under all error conditions.
  + Logical isolation of safety-critical components to prevent interference from non-safety-critical systems.

### 7.2.3 Source Code Analysis:

* Perform detailed code inspections to confirm that safety-critical requirements (items "a" through "l") are appropriately implemented:

  + Verify adherence to safety-related coding practices, including handling errors, input/output validation, memory protection, and state management.
  + Identify and document any risks or issues associated with the code during reviews.
* Assess the rationale provided by developers if requirements are not fully met, documenting these gaps and associated mitigations.

### 7.2.4 Verification Activities Analysis:

* Confirm that all verification tests (e.g., unit tests, integration tests) meet test standards for coverage, complexity, and thoroughness, including support files that affect hazardous systems.
* Validate simulation data and test environments to ensure accurate replication of real-world conditions and off-nominal scenarios.

### 7.2.5 Evidence of Testing for Safety-Critical Elements:

* Verify that safety-critical loaded data, uplinked data, scripted rules, and automated sequences affecting hazardous system behavior are thoroughly tested.
* Confirm that test results demonstrate proper behavior under nominal and degraded conditions and document validation as part of deliverables.

### 7.2.6 Requirements Mapping and Authority Approvals:

* Ensure NPR 7150.2 and NASA-STD-8739.8 requirements mapping matrices are signed by both engineering and SMA technical authorities for each development organization.
* Document traceability from requirements items "a" through "l" to specific design, implementation, and testing artifacts.

## 7.3 Metrics

Establish clear and actionable metrics to monitor and evaluate the progress and quality of safety-critical software assurance activities. Aim for trends that reduce risks and improve compliance with requirements over time.

1. **Software Product Non-Conformances:**

   * Track the number of non-conformances (issues and defects) identified by life cycle phase to monitor and proactively address recurring problems early in development.
2. **Review Non-Conformances:**

   * Record metrics from reviews (open vs. closed issues) and track issue resolution times (days open).
   * Focus on reducing the duration that safety-related non-conformances remain unresolved.
3. **Safety-Related Requirement Issues:**

   * Capture metrics on safety-related requirement issues (open vs. closed) to measure alignment with hazard mitigation strategies.
4. **Hazard Testing Completion:**

   * Monitor the number of hazards containing software that have been tested versus the total number of hazards containing software to ensure comprehensive risk analysis.
5. **Source Code Testing Coverage:**

   * Record the ratio of source lines of code (SLOC) tested versus total SLOC to ensure adequate verification of all software components impacting safety.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics).

## 7.4 Guidance

### 7.4.1 General Approach:

* The sub-requirements listed in items "a" through "l" constitute industry best practices for implementing safety-critical software. These requirements focus on controlling, mitigating, or contributing to hazards in systems that command hazardous operations.
* Software engineering and software assurance teams must collaborate closely to deliver high-quality work products that comply with safety, reliability, and quality standards while meeting project objectives.

## Steps for Implementation:

**Step 1**: **Analysis of Software Requirements**

* Conduct an early and comprehensive evaluation of software requirements against items "a" through "l." Identify gaps or inconsistencies and collaboratively address them with the development team.

**Step 2**: **Analysis of Software Design**

* Verify that the software design supports the implementation of items "a" through "l" and integrates safety features such as error handling, safe state transitions, and memory protection.
* Ensure the design isolates and prioritizes safety-critical components logically and physically from non-safety-critical elements.

**Step 3**: **Testing Safety-Critical Data, Rules, and Scripts**

* Confirm that safety-critical data (e.g., loaded values, uplinked updates) and automated rules/scripts are tested under all expected conditions, including off-nominal states.
* Prioritize hazardous operations in testing plans to mitigate risks early.

**Step 4**: **Partitioning and Isolation**

* Implement partitioning or isolation methods in design and code to:
  + Prevent interference between safety-critical and non-safety-critical components.
  + Ensure safety-critical elements maintain integrity under adverse conditions, such as memory faults or external perturbations.

**Step 5**: **Participation in Software Reviews**

* Actively participate in all life cycle reviews (including code inspections, test reviews, safety reviews, and project milestones) to assess compliance with safety requirements.
* Provide actionable feedback and independently assess risks associated with any deviations from items "a" through "l."

**Step 6**: **Alignment with System Hazard Analysis**

* Ensure that the software's implementation aligns with and supports the system hazard analysis for managing safety risks.
* Use data from hazard analysis to refine testing, design, and integration strategies.

### 7.4.2 Additional Guidance

**Early Planning**:

* Incorporating safety features and requirements early in the development life cycle reduces project costs, schedule disruptions, and risks. Integrated design approaches improve reliability and simplicity.

**Implementation Trade-Offs**:

* Projects may use different failure philosophies (e.g., fault tolerance, control-path separation) depending on system requirements and constraints. Ensure trade-offs are documented and assessed for their impact on safety, performance, and compliance.

**Conflict Resolution**:

* If conflicting program safety requirements arise, prioritize program safety requirements over software-specific features to align with broader system-level safety objectives.

### 7.4.3 Tools and Techniques for Small Projects

* **Static Code Analysis Tools**: Use tools to automate code inspections for compliance with items "a" through "l."
* **Simulation Frameworks**: Test safety-critical operations and off-nominal conditions using simulation environments to replicate real-world scenarios.
* **Requirement Traceability Tools**: Ensure each item in "a" through "l" is mapped to design and test stages using traceability matrices for transparency.

This guidance streamlines assurance practices while maintaining a robust focus on actionable measures to reduce risks and promote safety throughout the software life cycle.

See also [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software). 

## 7.5 Checklist for Safety-Critical or Mission-Critical Software

The checklist in **PAT-035 - Checklist for Safety-Critical or Mission-Critical Software** [PAT-035](#tabs-5) may be used to review the items in this requirement. Download the worksheet and make any modifications necessary for your project. Use the checklist as many times as necessary. 

**PAT-035 - Checklist for Safety-Critical or Mission-Critical Software**

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-035 - Checklist for Safety-Critical or Mission-Critical Software**

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) * [7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.04 - Additional Requirements Considerations for Use with Safety-Critical Software](/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [PAT-035 - Checklist for Safety-Critical or Mission-Critical Software](/spaces/SITE/pages/180584532/PAT-035+-+Checklist+for+Safety-Critical+or+Mission-Critical+Software) |

# 8. Objective Evidence

Requirement 3.7.3 ensures that safety-critical or mission-critical software meets stringent safety, integrity, and fault-handling requirements. Below is comprehensive guidance on specific **objective evidence** that can be provided to demonstrate compliance with each of the listed sub-requirements.

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

## 8.1 Objective Evidence Categories and Examples

#### **a. The software is initialized, at first start and restarts, to a known safe state.**

##### **Must Include**:

* Design documentation explaining the implemented safe initialization process.
* Test results demonstrating that software initializes or restarts into a verified predefined safe state under nominal and faulty conditions.
* Evidence for recovery processes after power-on or after unexpected application restart.

##### **Examples of Evidence**:

* **Software Design Document (SDD)**: Description of initialization logic to establish a safe state (e.g., disable actuators, hold commands, etc.).
* **Test Records**: Show results of cold and warm start conditions transitioning the system into a safe state. Example: "At first start, software places all propulsion activators in a safe OFF state."
* **Code Review Reports**: Documentation proving initialization routines were implemented and verified in the source code.

#### **b. The software safely transitions between all predefined known states.**

##### **Must Include**:

* State diagrams showing all predefined safe states and transitions.
* Test artifacts demonstrating successful state transition scenarios, including edge cases and failure conditions.
* Evidence of automated monitoring or checks during state transitions.

##### **Examples of Evidence**:

* **State Transition Diagrams**: Graphical or tabular representation showing all controlled transitions (e.g., Start → Idle → Active → Safe Failure Mode).
* **Test Reports**: Results confirming that state transitions succeed safely under nominal and fault conditions.
* **Scenario Simulations**: Evidence from simulations showing transitions between operational, standby, and failure recovery states.

#### **c. Termination performed by software functions is performed to a known safe state.**

##### **Must Include**:

* Requirements defining termination processes and behaviors to achieve a safe state.
* Test evidence for software-initiated or operator-initiated termination leading to safe conditions.

##### **Examples of Evidence**:

* **Verification Test Cases**: Test results showing all possible termination scenarios result in controlled transitions to safe states.
* **Algorithms Documentation**: Description of termination routines and their relationship to safe state logic.

#### **d. Operator overrides of software functions require at least two independent actions by an operator.**

##### **Must Include**:

* Operator input/override sequence logic and instructions that enforce the two-action rule.
* Verification tests confirming successful dual-action overrides and rejection of single-action overrides.

##### **Examples of Evidence**:

* **Software Requirements Specification (SRS)**: Description of two independent actions required for overrides.
* **Test Results**: Examples: "Single-action overrides for emergency shutdown rejected; two-step confirmation override successfully executed."
* **Procedures for Crew Actions**: Operator guides explaining override actions (e.g., unique button combinations or input sequences).

#### **e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard.**

##### **Must Include**:

* Command sequence control descriptions in software requirements and design documents.
* Verification test cases demonstrating rejection of out-of-sequence commands.

##### **Examples of Evidence**:

* **Command Handling Test Reports**: Results showing invalid or out-of-sequence commands are rejected.
* **Command Execution Logs**: Evidence that hazard-inducing commands received out of sequence were ignored/rejected (e.g., "Command A rejected because Command B was not yet executed").

#### **f. The software detects inadvertent memory modification and recovers to a known safe state.**

##### **Must Include**:

* Description of memory integrity tests and fault recovery functionality in software design.
* Memory corruption injection tests showing transition to a safe state upon detection.

##### **Examples of Evidence**:

* **Fault-Injection Test Results**: Example: "Test of simulated memory corruption triggered recovery to a predefined safe baseline state."
* **Dynamic Memory Integrity Check Reports**: Logs showing runtime detection of memory modification events.

#### **g. The software performs integrity checks on inputs and outputs to/from the software system.**

##### **Must Include**:

* Input/output validation logic descriptions.
* Test records showing integrity checks detect and handle invalid data.

##### **Examples of Evidence**:

* **Test Results**: Tests demonstrating input validation (e.g., incorrect data formats are flagged and ignored).
* **Boundary Analysis Reports**: Evidence supporting edge-case validation.

#### **h. The software performs prerequisite checks prior to the execution of safety-critical software commands.**

##### **Must Include**:

* Documentation of prerequisite check logic and implementation.
* Test records showing validation of required conditions for critical commands.

##### **Examples of Evidence**:

* **Test Reports**: Example: "Prerequisite check for ‘Engine Start’ rejected due to unsafe system state."
* **Code Inspection Reports**: Proof that checks were implemented for required preconditions.

#### **i. No single software event or action is allowed to initiate an identified hazard.**

##### **Must Include**:

* Analysis of redundancy mechanisms ensuring no single action leads to hazard initiation.
* Test results proving protection through multi-layer checks and redundancy.

##### **Examples of Evidence**:

* **Failure Mode and Effects Analysis (FMEA)**: Showing mitigations for single-event hazards.
* **Test Success Reports**: Example: "Single failures (e.g., sensor reading error) did not trigger hazard.”

#### **j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event.**

##### **Must Include**:

* Time-critical requirements for off-nominal conditions.
* Testing results of event response latency compared to hazard prevention thresholds.

##### **Examples of Evidence**:

* **Latency and Response Test Results**: Example: "Anomaly detected and response initiated in 500ms, within threshold of 1 second."
* **Real-Time Simulation Results**: Showing software reacting appropriately in simulated off-nominal fault scenarios.

#### **k. The software provides error handling.**

##### **Must Include**:

* Error-handling routines documented in design artifacts.
* Test results demonstrating the proper handling of runtime errors.

##### **Examples of Evidence**:

* **Error Handling Logs**: Evidence showing consistent software behavior during runtime errors.
* **Validation Documents**: Test cases proving errors are addressed appropriately without crashing the system.

#### **l. The software can place the system into a safe state.**

##### **Must Include**:

* Description of safe-state entry logic linked to system controls.
* Evidence showing successful execution of safe-state commands.

##### **Examples of Evidence**:

* **Test Reports**: Example: "Tested emergency abort functionality transitioned spacecraft to contingency mode safely during engine failure."
* **Safe-State Recovery Simulations**: Simulated failure scenarios validating transitions.

### **Summary of Objective Evidence**

| **Sub-Requirement** | **Examples of Evidence** |
| --- | --- |
| **a** | SDD for initialization logic, test results for cold/warm start, review logs of the safe state mechanism. |
| **b** | State transition diagrams, test case reports, state machine simulation evidence. |
| **c** | Termination test logs, verified contingency mode design descriptions. |
| **d** | SRS for override logic, dual-action override test results. |
| **e** | Command sequence test reports, command rejection logs. |
| **f** | Fault injection results for memory corruption, memory integrity check reports. |
| **g** | Input/output validation test reports, boundary value analysis. |
| **h** | Prerequisite check test cases, code review documentation. |
| **i** | FMEA showing redundancy, validation demonstrating no single-point failure leads to hazards. |
| **j** | Real-time response latency test logs, simulated hazard prevention data. |
| **k** | Error-handling reports, validation logs for runtime scenarios. |
| **l** | Contingency mode test results, verification reports for automated safe-state transitions. |

This comprehensive set of evidence demonstrates that safety-critical and mission-critical software is compliant with Requirement 3.7.3 and is resilient, fault-tolerant, and meets NASA’s safety assurance standards.
