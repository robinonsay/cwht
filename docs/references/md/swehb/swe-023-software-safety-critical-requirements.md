# SWE-023 - Software Safety-Critical Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695408. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements

SWE-023 - Software Safety-Critical Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695408)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695408&showCommentArea=true&showComments=true#addcomment)

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

3.7.2 If a project has safety-critical software, the project manager shall implement the safety-critical software requirements contained in NASA-STD-8739.8.

## 1.1 Notes

 NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-023 History

SWE-023 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 2.2.11 When a project is determined to have safety-critical software, the project shall ensure that the safety requirements of NASA-STD-8719.13, NASA Software Safety Standard, are implemented by the project. |
| Difference between A and B | No change |
| B | 3.7.1 When a project is determined to have safety-critical software, the project manager shall implement the requirements of NASA-STD-8719.13. |
| Difference between B and C | Updated NASA-STD-8719.13 to the new combined Software Assurance and Software Safety Standard, NASA-STD-8739.8. |
| C | 3.7.2 If a project has safety-critical software, the project manager shall implement the safety-critical software requirements contained in NASA-STD-8739.8. |
| Difference between C and D | No change |
| D | 3.7.2 If a project has safety-critical software, the project manager shall implement the safety-critical software requirements contained in NASA-STD-8739.8. |

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
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |

# 2. Rationale

The implementation of the safety-critical software requirements and processes helps ensure that a safe product is produced.

The implementation of safety-critical software requirements detailed in NASA-STD-8739.8 [278](#_tabs-<p></p>) ensures the reliability, safety, and robustness of software systems critical to mission success. This requirement addresses both the immediate risks to human life, property, and mission success, as well as broader systemic risks associated with non-compliance, such as rework, delays, and cascading system failures. By mandating adherence, NASA ensures that all safety-critical software meets the highest possible standards for safety and assurance, enabling safer operations and successful missions.

## 2.1 Ensures Mission and Human Safety

* Safety-critical software directly impacts functions that, if performed incorrectly, could lead to:
  + **Loss of life** or serious injury to personnel.
  + **Significant property damage** (e.g., spacecraft, ground support systems).
  + **Mission failure** or loss of valuable scientific data.
* Implementing the rigorous safety-critical software requirements outlined in NASA-STD-8739.8 ensures that these high-risk systems are designed, tested, and validated to prevent hazards from causing unmitigated consequences.

## 2.2 Elevates Standards for High-Risk Software

* Safety-critical software has stricter requirements to address its potential role in hazardous operations. Without implementing safety-critical requirements, such software:
  + May not be robust enough to mitigate critical hazards.
  + May lack sufficient safeguards (e.g., redundancy, fault tolerance, fail-safes).
  + Would be inadequately tested under off-nominal scenarios that could trigger hazardous conditions during operations.

## 2.3 Aligns with a Proven, Systematic Approach to Safety

* NASA-STD-8739.8 provides a **systematic framework** for managing safety-critical software, including:
  + Hazard analysis and mitigation.
  + Safety-specific requirements in design, development, and testing phases.
  + Assurance processes to validate safety compliance.
* Adherence to these requirements ensures consistency and thoroughness across all NASA projects, preventing oversights that could jeopardize mission success and safety.

## 2.4 Establishes Traceability and Accountability

* Safety-critical software requirements enforce **traceability** between:
  + Identified hazards.
  + Safety-specific software requirements and design elements.
  + Verification and validation (V&V) activities ensuring hazards are mitigated or controlled.
* This traceability not only ensures project accountability but also provides detailed documentation for safety audits, reviews, and lessons learned.

## 2.5 Mitigates Potential Risks Early and Effectively

* Safety-critical software requirements mandate proactive risk identification and mitigation:
  + Hazards involving software are identified from the earliest phases (e.g., formulation, design).
  + Risk mitigation strategies are incorporated into the software design, reducing the likelihood of design flaws leading to safety incidents.
  + Rigorous testing and assurance processes ensure safety-critical functionality behaves correctly under all operating conditions, including failures.

## 2.6 Reduces the Likelihood of Costly Rework and Delays

* Software that is not designed and validated to the level required for safety-critical systems may require rework later, causing:
  + Unplanned **project delays**.
  + **Increased costs** associated with redesign, re-verification, or re-certification.
  + **Compromised schedules** for broader system integration and deployment.
* Ensuring compliance with NASA-STD-8739.8 from the start reduces these risks and ensures software is right the first time.

## 2.7 Supports NASA’s Goal of Risk-Informed Decision Making

* NASA-STD-8739.8 incorporates decades of lessons learned into its requirements to systematically manage software-related risks. By implementing these requirements, the project demonstrates a **risk-informed approach to safety** that prioritizes protecting people, property, and mission objectives.

## 2.8 Promotes Consistency Across NASA Projects

* Implementing safety-critical software requirements ensures that high-risk software systems across all NASA projects are developed with consistent levels of rigor. This standardization:
  + Supports **collaboration** and reuse across projects.
  + Ensures compliance with **NASA-wide safety policies**.
  + Builds on lessons learned to prevent repeating known issues.

# 3. Guidance

The primary goal of software safety is ensuring the software performs consistently as required, especially in scenarios where incorrect operation or failure of the software could result in hazards. Software safety practices prevent, mitigate, or control hazards associated with software systems throughout the entire software development lifecycle.

## 3.1 Key Software Safety Activities

To achieve software safety objectives, the following systematic activities are essential:

### 3.1.1 Detecting and Recovering from Memory Modifications

* **Purpose**: Protect the software system from inadvertent or malicious changes to memory that could lead to unsafe states or hazardous failures.
* **Implementation Guidance**:
  + Utilize **runtime memory checks** to detect memory corruption (e.g., cyclic redundancy checks, watchpoints, memory bounds checks).
  + Implement robust **fault recovery mechanisms** to place the system into a safe state if memory corruption is detected.

### 3.1.2 Performing Input and Output Integrity Checks

* **Purpose**: Ensure the accuracy and validity of data exchanged internally and externally before safety-critical decisions or actions are taken.
* **Implementation Guidance**:
  + Validate all inputs using **range checks, format checks**, and logical checks.
  + Perform **data integrity verification** on outputs to ensure safety-critical commands and data transfer are consistent with system expectations.
  + Utilize **redundancy mechanisms** where applicable (e.g., multiple sensors or inputs to verify critical parameters).

### 3.1.3 Executing Prerequisite Checks for Safety-Critical Commands

* **Purpose**: Prevent unsafe software behavior by verifying system readiness before executing safety-critical commands.
* **Implementation Guidance**:
  + Identify and document **safety-critical commands** during design and review phases.
  + Define **preconditions and prerequisites** required for executing each command (e.g., system state, environmental conditions, hardware readiness).
  + Implement mechanisms to enforce prerequisite checks at runtime, ensuring commands cannot execute without meeting conditions.

### 3.1.4 Preventing Single Software Events from Initiating Hazards

* **Purpose**: Avoid scenarios where one single-point software failure or event triggers unintended hazardous conditions.
* **Implementation Guidance**:
  + Partition software and system designs to ensure **fail-safe mechanisms** are independent of single software failure modes.
  + Enforce redundancy and **multi-event safeguarding** (e.g., requiring at least two distinct, validated software actions to initiate hazardous operations).
  + Perform **fault tolerance testing** to validate the robustness of the system under various failure scenarios.

### 3.1.5 Responding to Off-Nominal Conditions Within Necessary Time Frames

* **Purpose**: Ensure the software can promptly react to unexpected or abnormal conditions to prevent hazards from escalating.
* **Implementation Guidance**:
  + Define **acceptable time windows** for responses to conditions that could lead to hazards.
  + Implement **real-time monitoring and fault detection** systems to identify off-nominal conditions early.
  + Design active response mechanisms (e.g., switching to backup systems, alerting operators, deactivating unsafe components) to mitigate risks within critical time frames.

### 3.1.6 Providing Error Handling Mechanisms

* **Purpose**: Ensure software can detect and handle errors without causing hazardous conditions or cascading failures.
* **Implementation Guidance**:
  + Implement **structured error handling** at the system and software levels, ensuring appropriate recovery mechanisms are in place for faults (e.g., retries, safe shutdown, alerts).
  + Test error-handling routines extensively under nominal, off-nominal, and failure scenarios to ensure reliability.

### 3.1.7 Ensuring the Software Can Place the System into a Safe State

* **Purpose**: Enable the software to effectively handle hazardous conditions by safely shutting down or transitioning the system to a non-hazardous state.
* **Implementation Guidance**:
  + Design system-level and software-level **safe state criteria** based on hazard analysis.
  + Incorporate software behaviors that actively transition the system to safety states during failures or risks (e.g., disabling actuators, isolating subsystems, triggering machine shutdown).
  + Prioritize **safe recovery mechanisms** during testing to ensure software can reliably transition systems into non-hazardous states.

### 3.1.8 Collective Impact

These activities work together to ensure:

* **Reliability**: The software consistently performs its intended function under all conditions.
* **Safety**: The system avoids hazardous conditions by detecting and mitigating failures through robust software design and operation.
* **Resilience**: The software is fault-tolerant and capable of recovering from errors or abnormal conditions without exacerbating risks.

## 3.2 Software Safety Definition

**Software Safety** is defined as “the aspects of software engineering and assurance that systematically identify, analyze, track, mitigate, and control hazards and hazardous functions of a system where software may contribute either to the hazard or its mitigation or control, ensuring safe system operation.”

## 3.3 Importance of a Systematic Approach to Software Safety

### 3.3.1. Safety by Design

Safety must be embedded during the early design phase to reduce risks at the foundational level. It is more effective and cost-efficient to design software to prevent hazards than to retrofit safety controls later in development.

### 3.3.2. Continuous Lifecycle Safety

Safety cannot be a one-time effort. A systematic approach ensures safety is considered throughout acquisition, development, testing, operation, and maintenance phases. This includes:

* **Early Hazard Identification**: Software's contribution to hazards should be evaluated during the **concept phase** and iteratively reviewed as designs mature at each major milestone or phase (e.g., Preliminary Design Review, Critical Design Review).
* **Maintaining Safe Operations**: Safety-critical functions must be protected during software updates and throughout system operations.

## 3.4 Role of NASA-STD-8739.8B

#### **Comprehensive Guidance**

The **NASA Software Assurance Standard (NASA-STD-8739.8B)** provides the framework for designing, developing, and assuring software within safety-critical systems. It outlines:

* Required safety activities.
* Key deliverables, including the data and documentation necessary for safety validation.
* Assurance measures for maintaining compliance throughout the software/system lifecycle.

#### **Repeatable Assessments**

Evaluation for software contributions to system hazards must occur:

1. During the **concept phase** to identify initial safety risks.
2. At **major milestones** as the design evolves and new hazards emerge.
3. During software integration, testing, and deployment to ensure robust mitigation strategies remain effective.

## 3.5 Best Practices for Implementing Software Safety in Safety-Critical Systems

Software safety ensures that high-stakes systems—where software failure could lead to hazards—operate safely and reliably. By embedding safety systematically into software engineering processes and adhering to NASA-STD-8739.8B, projects can effectively prevent, control, and mitigate risks, ensuring successful and safe mission execution.

See also Topic [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance), [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects)

### 3.5.1. Start Early

* Incorporate safety considerations during the earliest phases of system development.
* Perform initial hazard and safety analyses to identify how software may contribute to or mitigate hazards.

### 3.5.2. Collaborate Cross-Disciplinary

* Work closely with systems engineers, safety analysts, and operations staff to understand the broader system context.

### 3.5.3. Follow Mature Standards

* Leverage NASA-STD-8739.8B to guide all software safety activities within the project.

### 3.5.4. Regularly Reassess

* Continuously evaluate software contributions to hazards throughout the lifecycle and update hazard analyses during major reviews.

### 3.5.5. Test Extensively

* Conduct thorough testing of both nominal and off-nominal scenarios to verify safety-critical functions perform as required under all conditions.

## 3.6 Software Safety Requirements

After the project has determined that the project has safety-critical software, the project manager should implement the safety-critical software requirements contained in NASA-STD-8739.8B in the project's software plans and the project's software requirements specification(s). The safety-critical software requirements contained in NASA-STD-8739.8B are listed below:

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

## 3.7 Determining If Software Is Safety Critical

The determination of whether software is **safety-critical** is a critical activity that directly impacts the application of additional safety and assurance requirements. The "safety-critical" designation ensures appropriate rigor is applied to the software development process to prevent, mitigate, or manage risks related to hazards caused by or involving software.

### 3.7.1 Roles and Responsibilities

#### **1. Engineering Technical Authority (ETA) and S&MA Technical Authority (S&MA TA):**

* The **ETA** and **S&MA TA** are jointly responsible for determining if software is classified as **safety-critical**.
* The designation must be based on the **criteria and guidance provided in NASA-STD-8739.8** and **NASA-HDBK-2203**. This determination ensures consistency in the application of hazard assessment methodologies.
* **Key Principles:**
  + The evaluation considers the allocation of **system safety requirements**, associated hardware, and risks.
  + Agreement on the safety-critical determination is essential—disagreements are escalated through the respective ETA and S&MA TA organizational chains.

### 3.7.2 Process for Determining Safety-Critical Software

1. **Initial Evaluation During Formulation Phase**:
   * **When**: The determination process begins during the **formulation phase** of the project or program.
   * **Purpose**: To identify **high-level hazards** and assess whether software contributes to or mitigates these hazards (based on **criteria outlined in NASA-STD-8739.8**).
   * **Collaboration**:
     + Engineering and software assurance work together initially to determine software’s potential safety-criticality.
     + The results of these independent analyses are compared and any discrepancies are resolved collaboratively.

1. **Guidance Tools for Safety-Critical Determination**:
   * **NASA-STD-8739.8**: Provides detailed criteria and processes for identifying safety-critical software.
   * **NASA-HDBK-2203**: Includes a Software Safety-Critical Assessment Tool for consistent and thorough evaluations.
   * Use these tools to ensure the methodology is systematic, objective, and traceable.

1. **Criteria for Safety-Critical Software**: Software is classified as **safety-critical** if:
   * It **causes or contributes to hazards** defined in the system hazard analysis.
   * It **controls safety-critical functions or hardware**.
   * It **performs hazard mitigation actions** such as fail-safe operations or reducing risk.
   * It **prevents undesired consequences** by ensuring safety-critical activities occur under controlled conditions.
   * It **responds to hazards or errors within time-critical windows**.
   * It **detects and alerts operators of hazardous states and provides corrective actions**.

Refer to **Appendix A of NASA-STD-8739.8** for more detailed examples and criteria.

1. **Reassessing Safety-Critical Software Throughout the Lifecycle**:
   * As the project evolves, **safety-criticality must be reassessed** at all levels of the software architecture:
     + **System-Level Components**: Evaluate entire software systems for safety-critical contributions.
     + **Subsystem Software**: Perform focused analyses as specific subsystems and components are developed.
     + **Models and Simulations**: Include software simulations in hazard analysis if they influence decision-making for critical systems.
   * Assessments should occur at every project milestone (e.g., Preliminary Design Review, Critical Design Review) to account for evolving designs, requirements, and new hazard information.

1. **Handling Discrepancies and Disagreements**:
   * If the **ETA** and **S&MA TA** have differing views on safety-criticality:
     + Escalate unresolved issues through the **Engineering Technical Authority and S&MA Technical Authority chains** for resolution.
     + While resolving disagreements, document reasoning and provide evidence for all decisions to enable a traceable process.

### 3.7.3 Software Safety Requirements: Coverage

For software designated as safety-critical, specific safety requirements must be defined, implemented, and documented. These requirements address both **process-oriented safety activities** and **technical implementation requirements**:

1. **"Must Work" and "Must Not Work" Requirements**:

   * "Must Work": The software must perform specific safety-critical functions as intended (e.g., initiating hazard mitigation responses).
   * "Must Not Work": The software must explicitly prevent harmful actions (e.g., triggering hazardous operations without meeting critical prerequisites).
2. **Process Requirements**:

   * Conduct software hazard analyses in coordination with the system hazard analyses.
   * Develop structured processes for tracking, mitigating, and verifying software safety risks.
3. **Technical Requirements**:

   * Follow **SWE-134** to ensure software design supports safety-critical requirements.
   * Implement software mechanisms to:
     + Maintain redundancy and fault isolation.
     + Detect and recover from unsafe states.
     + Ensure hazard inhibits remain independent.

### 3.7.4 Supplemental Activities: Software Safety Analysis

#### **1. Integration with System Hazard Analysis**

* Perform software safety analyses to supplement the **system hazard analysis**, ensuring:
  + The software meets **levied safety-critical functional requirements**.
  + **Independence of hazard inhibits** is maintained (e.g., software must not bypass hardware safety constraints).
  + **Hardware redundancy independence** is preserved (e.g., software faults do not invalidate redundant hardware paths).

#### **2. Phased Software Safety Analysis**

* **Phase 1: Identifying Action and Inaction Functions**:
  + Define critical "must work" (e.g., solar array deployment) and "must not work" (e.g., unauthorized command execution) functions during preliminary hazard analysis.
* **Phase 2: Assessment of Fault Tolerance and Design Alignment**:
  + Validate the alignment between software functionality and fault tolerance requirements, ensuring no single-point software failure triggers hazardous conditions.
* **Phase 3: Test Plan and Verification Assessment**:
  + Evaluate test plans for off-nominal scenarios and verify that software test results close all hazard verifications.

### 3.7.5 Examples of Software Contributions to Complex Systems

#### **Cyclomatic Complexity and Hazard Analysis**:

* **Cyclomatic Complexity** measures the number of paths in the code and is a useful heuristic for analyzing software maintainability and identifying critical areas in safety-critical software.
* When evaluating cyclomatic complexity, focus on safety-critical sections of the code where:
  + Multiple paths need prerequisite checks to avoid initiating hazards.
  + Fault detection and recovery paths need comprehensive testing.

#### **Critical Sequence Example: Solar Array Deployment**

* For a "must work" function like solar array deployment:
  + Software must initialize and execute commands in the correct sequence (e.g., within 4 CPU cycles) to avoid removing safety inhibits prematurely.
  + Communication channels between sensors and effectors must be independently verified to maintain redundancy.

### 3.7.6 Conclusion

Determining whether software is safety-critical is an essential step for identifying and applying additional safety requirements as mandated by **NASA-STD-8739.8**. The process ensures that software is rigorously evaluated for its role in preventing or controlling hazards. By following the detailed guidance:

* Safety-critical software is identified early and reassessed continuously.
* The collaboration between **ETA** and **S&MA TA** provides accountability and alignment between disciplines.
* Proper safety coverage ensures that both technical and process safety aspects are addressed, preserving the independence of inhibits, redundancy, and fault tolerance in safety-critical systems.

Systematic adherence to these procedures guarantees that safety-critical functionality is designed, implemented, verified, and maintained, ensuring mission success and safety.

See also Topic [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations).

See also, [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software).

## 3.8 Design Analysis

The design analysis portion of software safety analysis should be completed by Phase 2 safety reviews. At this point, the software safety analysis supports a requirements gap analysis to identify any gaps ([SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)) and ensure the risk and control strategy documented in hazard reports are correct as stated. Between Phase 2 and 3 safety reviews, the system hazard analysis and software safety analysis supports the analysis of test plans to assure adequate off-nominal scenarios ([SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test), [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) - a). Finally, in Phase 3, the system hazards analysis must verify the final implementation and verification upholds the analysis by ensuring test results permit closure of hazard verifications ([SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)) and that the final hazardous commands support the single command and multi-step command needs and finalized pre-requisite checks are in place.

Additional specific clarifications for the NPR 7150.2 SWE 134 requirement items "a" through "l." :

* **Item a:**Aspects to consider when establishing a known safe state includes state of the hardware and software, operational phase, device capability, configuration, file allocation tables, and boot code in memory.

  Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical software at each code inspection, test review, safety review, and project review milestone.
* **Item d:** Multiple independent actions by the operator help to reduce potential operator mistakes.
* **Item f:** Memory modifications may occur due to radiation-induced errors, uplink errors, configuration errors, or other causes so the computing system must be able to detect the problem and recover to a safe state. As an example, computing systems may implement error detection and correction, software executable and data load authentication, periodic memory scrub, and space partitioning to protect against inadvertent memory modification. Features of the processor and/or operating system can be utilized to protect against incorrect memory use.
* **Item g:** Software needs to accommodate both nominal inputs (within specifications) and off-nominal inputs, from which recovery may be required.
* **Item h:** The requirement is intended to preclude the inappropriate sequencing of commands. Appropriateness is determined by the project and conditions designed into the safety-critical system. Safety-critical software commands are commands that can cause or contribute to a hazardous event or operation. One must consider not only the inappropriate sequencing of commands (as described in the original note) but also the execution of a command in the wrong mode or state. Safety-critical software commands must perform when needed (must work) or be prevented from performing when the system is not in a proper mode or state (must-not work).
* **Item j:**The intent is to establish a safe state following the detection of an off-nominal indication. The safety mitigation must complete between the time that the off-nominal condition is detected and the time the hazard would occur without the mitigation. The safe state can either be an alternate state from normal operations or can be accomplished by detecting and correcting the fault or failure within the timeframe necessary to prevent a hazard and continuing with normal operations. The intent is to design in the ability of software to detect and respond to a fault or failure before it causes the system or subsystem to fail. If failure cannot be prevented, then design in the ability for the software to place the system into a safe state from which it can later recover. In this safe state, the system may not have full functionality but will operate with this reduced-functionality.
* **Item k:**Error handling is an implementation mechanism or design technique by which software faults and/or failures are detected, isolated, and recovered to allow for correct run-time program execution. The software error handling features that support safety-critical functions must detect and respond to hardware and operational faults and/or failures as well as faults in software data and commands from within a program or from other software programs.
* **Item l:** The design of the system must provide sufficient sensors and effectors, as well as self-checks within the software, to enable the software to detect and respond to system potential hazards.

See also [7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance),

## 3.9 Training and Acquisition Guidance

For additional considerations when acquiring safety-critical software, see Topic [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance).

Training in software safety is available in the NASA SMA Technical Excellence Program (STEP).

These topics and more are expanded in NASA-GB-8719.13 [276](#_tabs-<p></p>). Consult the guidebook for additional guidance, techniques, analysis, references, resources, and more for software developers creating safety-critical software as well as guidance for project managers, software assurance personnel, system engineers, and safety engineers.  Knowledge of the software safety tasks performed by persons in roles outside of software engineering will help engineering personnel understand requests from these persons for software engineering products and processes.

## 3.10 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) - ("a" portion) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)        * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) * [7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase) |

## 3.11 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

# 4. Small Projects

The requirement emphasizes the need for software safety activities and analyses to be tailored to the project's scope, complexity, and associated risk. While small projects must meet NASA's software safety requirements, the approach to their implementation can be adjusted to reflect the project constraints, such as limited personnel, budget, or resources.

Small projects benefit from a tailored, resource-conscious approach to implementing software safety requirements while maintaining compliance with NASA-STD-8739.8. By adapting validated tools, reusing safety plans, assigning multi-functional roles, and focusing on critical risks, small projects can ensure safety without overburdening personnel or budgets. Collaboration and systematic prioritization of high-risk functions allow small projects to achieve their objectives efficiently while upholding NASA’s commitment to quality, safety, and reliability.

The specific activities and depth of analyses needed to meet the requirements can, and should, be modified to the software safety risk. In other words, while the requirements must be met, the implementation and approach to meeting those requirements may and should vary to reflect the system to which they are applied. Substantial differences may exist when the same software safety requirements are applied to dissimilar projects.

For projects designated as a small project based on personnel or budget, the following options may be considered to assist in the fulfillment of this requirement:

* Utilize existing tools already validated and approved for use in the development of safety-critical software.  
  + If a standard set of validated and approved tools does not exist, consider establishing them for future projects.
* Use an existing safety plan specifically developed for small projects.  
  + If such a plan does not exist, consider creating one so future projects do not have to create a new one.
* Use one person to fill multiple roles.  
  + The software safety engineer may have other project roles or fill similar roles for other projects.
  + Keep in mind, that safety, quality, and reliability analyses and activities must be either performed or assessed, verified, and validated by a party independent of those developing the product.

This tailored approach ensures safety compliance without unnecessary overhead, while maintaining the integrity of the safety process.

## 4.1 Guidance for Small Projects

#### **General Principles**

1. **Risk-Based Tailoring**: The depth and scope of software safety analyses should be proportionate to the **system’s safety risk** and its role in contributing to or mitigating hazards.
2. **Adapted Implementation**: While requirements remain mandatory, their execution can leverage existing resources, multi-functional roles, and streamlined documentation to achieve compliance efficiently.
3. **Preserving Independence**: Safety activities (e.g., verification and validation) must remain independent of the software development process, even in resource-constrained environments.

## 4.2 Practical Options for Small Projects

### 4.2.1 Leverage Existing Tools

* **Utilize Validated Tools**:

  + Use pre-approved and validated tools for hazard analysis, testing, and software safety assurance, where applicable.
  + Examples include tools for **code analysis**, **automated testing**, and **traceability management**.
  + Reference tools validated by previous NASA projects and supported by existing documentation.
* **Establish Standard Tools for Future Use**:

  + If validated tools are not available, consider investing time or resources to identify or validate a set of tools that can be reused by other small projects.
  + Communicate lessons learned to enable tool reuse across project teams.

### 4.2.2 Use an Established Safety Plan

* **Reuse Existing Safety Plans**:

  + Adopt or adapt safety plans developed for other small projects with similar scope or system complexity.
  + This avoids the need to create new plans from scratch and provides a baseline for compliance.
* **Develop Templates for Future Projects**:

  + If a relevant safety plan does not exist, consider creating a lightweight, reusable safety plan specific to small projects.
  + Document processes, safety requirements, and tailored implementation strategies to help streamline future projects.

### 4.2.3 Assign Multi-Functional Roles

* **Leverage Limited Personnel**:

  + Assign the software safety engineer additional project roles to maximize efficiency without compromising safety. For example:
    - Combining the roles of a software safety engineer and a system engineer.
    - Supporting multiple projects with similar small-scale safety needs.
  + Ensure the individual has appropriate qualifications and sufficient bandwidth to perform software safety work effectively.
* **Safeguard Independence**:

  + Activities related to software safety (e.g., assessments, verification, and validation) must be reviewed by an independent party, even if personnel overlap in roles. Independence ensures unbiased evaluation of safety compliance.

### 4.2.4 Perform Risk-Based Simplification

* **Focus on High-Risk Scenarios**:

  + Prioritize safety analysis around high-risk functionalities and hazard exposure conditions specific to the software and system.
  + Tailor depth of analysis to the **impact and probability of risk**, ensuring coverage without over analysis for low-risk areas.
* **Streamline Documentation Requirements**:

  + Use concise, focused documentation formats for hazard analyses, test results, and verification artifacts to reduce administrative burden.

### 4.2.5 Collaborate and Share Resources

* **Knowledge Sharing**:

  + Collaborate with other small projects to share validated tools, templates, and best practices that reduce effort and rework.
  + Utilize existing NASA safety data packages, historical hazard analysis results, or lessons learned.
* **Cross-Functional Training**:

  + Provide training for personnel to perform multiple safety-related functions effectively (e.g., combining hazard analysis with requirements tracing).
  + Training prioritizes resource utilization while maintaining compliance.

## 4.3 Special Considerations for Small Projects

### 4.3.1 Maintaining Safety, Quality, and Reliability

* Activities related to safety, quality, and reliability must not be compromised by project constraints.
  + These activities should be assessed, verified, and validated independently of the software development process to avoid potential conflicts of interest.
  + Use external reviewers or independent entities (e.g., cross-project personnel) to perform these evaluations where personnel overlap occurs.

### 4.3.2 Customizing Depth of Analysis

* While fewer resources may be available for analyses, small projects should:
  + Identify **critical hazards** and the software’s role in contributing to or mitigating them.
  + Ensure all safety-critical functions are systematically analyzed throughout the project lifecycle.
* Tailor the rigor of analysis toward essential requirements (e.g., high-impact hazards with defined "must work" and "must not work" functions).

### 4.3.3 Incorporating NASA-STD-8739.8 Guidance

* NASA-STD-8739.8 provides scalable software safety guidance that supports tailored implementation for projects of varying size. By following NASA's Software Assurance Standard:
  + Small projects can embed safety into their processes while adjusting depth and resource allocation to suit their size and risk level.

## 4.4 Examples of Tailored Application

#### **Use of Validated Tools**:

* A previously validated traceability tool can be reused to establish connections between safety-critical software requirements, design elements, and test cases.

#### **Streamlined Hazard Analysis**:

* For a small propulsion project, focus the hazard analysis on the software controlling thrust sequences and ignore ancillary functions that pose negligible safety risk.

#### **Simple Safety Plan Implementation**:

* Adopt a one-page safety plan that outlines essential activities, including independent verification, applicable software tools, assessment guidelines, and review checkpoints.

#### **Multi-Function Roles**:

* A systems engineer can perform initial hazard analysis for software safety while collaborating with an independent reviewer for final validation.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document, EI32-OI-001,  Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. See Chapter 8. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-034)

  [NASA Complex Electronics Handbook for Assurance Professionals,](https://standards.nasa.gov/standard/nasa/nasa-hdbk-873923 "Click to open in new window")

   NASA-HDBK 8739.23A, Approved: 02-02-2016,  Superseding: NASA-HDBK-8739.23
  With Change 1,
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
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
* (SWEREF-294)

  [OSMA/NSC's SMA Technical Excellence Program (STEP) program.](https://nsc.nasa.gov/professional-development/safety-and-mission-assurance-technical-excellence-program "Click to open in new window")

  The Safety and Mission Assurance (SMA) Technical Excellence Program (STEP) is a career-oriented, professional development roadmap for SMA professionals.
* (SWEREF-342)

  [STEP Level 2 Overview of Software Safety course,](https://saterninfo.nasa.gov/ "Click to open in new window")

  SMA-SA-WBT-230 SATERN (need user account to access SATERN courses). This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-344)

  [STEP Level 3 Software Safety for Practitioners course, SMA-SOFT-NSC-1005](https://saterninfo.nasa.gov/ "Click to open in new window")

   SATERN  Need user account to access SATERN courses.This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-350)

  [Military Standard System Safety Program Requirements,](http://www.everyspec.com/MIL-STD/MIL-STD+%280800+-+0899%29/download.php?spec=MIL_STD_882C.965.pdf "Click to open in new window")

  U.S. Department of Defense (1993). MIL-STD-882C, 1993. Note that MIL-STD-882D exists, but that the NASA Software Safety Guidebook recommends using MIL-STD-882C.
* (SWEREF-504)

  [Mars Observer Inappropriate Fault Protection Response Following Contingency Mode Entry due to a Postulated Propulsion Subsystem Breach](https://llis.nasa.gov/lesson/343 "Click to open in new window")

  Public Lessons Learned Entry: 343.
* (SWEREF-517)

  [Fault Tolerant Design](https://llis.nasa.gov/lesson/707 "Click to open in new window")

  Public Lessons Learned Entry: 707.
* (SWEREF-522)

  [Fault Protection](https://llis.nasa.gov/lesson/772 "Click to open in new window")

  Public Lessons Learned Entry: 772.
* (SWEREF-527)

  [Fault-Detection, Fault-Isolation and Recovery (FDIR) Techniques](https://llis.nasa.gov/lesson/839 "Click to open in new window")

  Public Lessons Learned Entry: 839.
* (SWEREF-539)

  [Aero-Space Technology/X-34 In-Flight Separation from L-1011 Carrier](https://llis.nasa.gov/lesson/1122 "Click to open in new window")

  Public Lessons Learned Entry: 1122.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

The following lessons learned are derived from both the **NASA Lessons Learned Information System (LLIS)** and historical experiences related to software safety in the development and operation of space systems. These lessons, aligned with Requirement 3.7.2, emphasize the importance of fault tolerance, fault protection, safety assurance practices, rigorous validation, and well-defined roles and responsibilities in implementing the safety-critical software requirements of **NASA-STD-8739.8**.

---

### **1. Fault-Detection, Fault-Isolation, and Recovery (FDIR) Techniques**

**Lesson Number 0839: "Optimize FDIR to Increase System Availability and Mission Success"**

* **Context**: In critical environments like space, the ability to quickly detect, isolate, and recover from faults significantly impacts crew survival, system availability, and mission success.
* **Summary**: The implementation of **Fault-Detection, Fault-Isolation, and Recovery (FDIR)** techniques (e.g., Built-in Test [BIT], strategically placed sensors, centralized architecture) ensures rapid fault diagnosis and recovery with minimal impact on mission-critical activities.
* **Recommendation**:
  + Adopt robust **FDIR techniques** in safety-critical software to monitor, identify, isolate, and recover from failures.
  + Ensure **redundancy** in safety-critical systems and prioritize quick recovery from anomalies, as this improves reliability and mission availability.
  + Integrate FDIR algorithms into software that oversees astronaut safety-critical operations and real-time system decision-making.
* **Example**: For a spacecraft supporting astronauts, integrating BIT and strategic sensors in flight software helped detect propulsion system anomalies early, allowing time for recovery while maintaining system control.

---

### **2. Fault-Tolerant Design**

**Lesson Number 0707: "Incorporate Fault-Tolerant Software and Hardware Features"**

* **Context**: Fault-tolerant systems ensure that minor software or hardware failures do not propagate into catastrophic mission failures. This design principle increases reliability while minimizing unnecessary switchovers to backup systems.
* **Summary**: Fault tolerance in software and hardware should be an inherent design principle for safety-critical systems. Minor subsystem failures should not affect the system-wide reliability and availability of primary mission-critical functions.
* **Recommendation**:
  + Design safety-critical software to manage **faults in primary systems** effectively and transition to secondary systems only when absolutely necessary.
  + Implement fault-tolerant software features that use **redundancy, error-checking, and fail-safe modes** to prevent single-point failures from affecting system integrity.
  + Test fault-handling software under realistic fault conditions.
* **Example**: On a deep-space mission, fault-tolerant software design allowed continued operation of spacecraft communications after a subsystem memory corruption, avoiding an unnecessary switchover to the backup system.

---

### **3. Fault Protection**

**Lesson Number 0772: "Fault Protection as a Cooperative Design Element"**

* **Context**: Fault protection is developed as a collaborative approach across flight and ground systems, integrating software, hardware, and operational procedures to detect and respond to perceived faults.
* **Summary**: Fault protection is vital for safety-critical software, as it not only prevents catastrophic system failures but ensures resilient behavior under anomalous conditions. Eliminating single-point failures or their impacts is a key goal of cooperative designs for fault protection.
* **Recommendation**:
  + Design **cooperative fault protection mechanisms** between flight software, ground-based support systems, and operational procedures to identify and respond to anomalies autonomously.
  + Ensure robust fault protection software is capable of isolating errors and maintaining spacecraft/system integrity during unexpected conditions.
  + Validate the fault protection system thoroughly to ensure it functions as intended in all operational modes.
* **Example**: On a satellite mission, a cooperative effort between ground procedures and fault management flight software helped detect a critical battery failure during a power cycle anomaly and prevented a complete power loss.

---

### **4. Mars Observer Fault Protection Response**

**Lesson Number 0343: "Lessons from Inadequate Fault Protection on the Mars Observer"**

* **Context**: The Mars Observer spacecraft entered a failure state due to a postulated propulsion subsystem breach, and the fault protection responses at the time were not appropriate for the spacecraft’s state, resulting in mission loss.
* **Summary**: Fault responses must be carefully designed to ensure they do not interrupt critical mission activities unnecessarily and are appropriate for all spacecraft states. Inadequate or inappropriate fault protection actions can lead to mission failure.
* **Key Recommendations**:
  1. Spacecraft designers must evaluate the consequences of all anomalies across all mission phases and ensure the fault protection system responses are suitable.
  2. Fault protection responses should not interrupt critical activities unless they can ensure successful completion of these activities.
  3. Stable fault protection modes (e.g., contingency mode) should autonomously ensure reliable communication with ground control.
* **Example**: This lesson emphasizes the need for exhaustive fault protection testing during the developmental phase of safety-critical software to identify weaknesses or incomplete logic paths.

---

### **5. Distribution of Safety Responsibilities**

**Lesson Number 1122: "X-34 Program Demonstrates Risks of Undefined Safety Roles"**

* **Context**: The X-34 technology demonstrator program faced challenges due to undefined safety roles distributed across various NASA contractors and subcontractors. Inadequacies in validating flight software and assigning safety responsibilities delayed resolving these risks.
* **Summary**: Distributed safety functions without clearly defined roles or integration can result in incomplete validation of safety-critical elements, including improperly tested software. This can increase the likelihood of safety failures during operations.
* **Recommendation**:
  + Clearly define **roles and responsibilities** among contractors, subcontractors, and NASA stakeholders to ensure accountability for validating safety-critical software and managing safety functions during the lifecycle.
  + Focus on **thorough and comprehensive validation** of flight software, particularly in scenarios involving potentially hazardous operations (e.g., flight separation, autonomous functionality).
* **Example**: Reform in the X-34 program allocated explicit responsibilities for validating separation critical maneuvers and ensuring software governing flight operations met safety requirements.

---

### **6. Safety-Critical Fault Detection in Software Validation**

In addition to the official LLIS entries, **lessons from spacecraft fault detection validation** demonstrate that inadequate or insufficient testing, especially for safety-critical software modes, can miss unforeseen failure mechanisms.

* **Recommendation**:
  + Use **advanced testing techniques** for fault detection, including:
    - Anomaly injection.
    - Edge-case scenario simulations.
    - End-to-end systems testing.
  + Test safety-critical software jointly with hardware-in-the-loop environments or specialized simulators to identify hidden issues in fault detection and recovery systems.
* **Example**: In a planetary rover mission, joint testing between flight software and simulated terrain identified a crucial fault-handling issue with the hazard avoidance functionality.

---

### **7.** **Lesson Learned (Starliner CFT):** **Risk acceptance must be data‑driven; unexplained anomalies should not be normalized.**

**Project Context:**  
Derived from Starliner CFT Investigation.

**Problem/Observation:**  
Risk posture shifted toward accepting operation with unexplained behaviors; burden of proof moved to NASA to demonstrate risk instead of the provider proving safety.

**Contributing Factors:**

* Repeated acceptance of intermittent or unexplained anomalies without root cause.
* Insufficient linkage between anomalies and risk registers; limited trend analysis.

**Impacts:**

* Recurrence of anomalies, degraded confidence, and late discovery of fault‑tolerance gaps.
* Increased mission risk during integrated operations.

**Recommended Practices (Aligned to SWE‑023/024):**

* Require **root cause, corrective action (RCCA)** closure (or documented risk acceptance with quantified hazard impact).
* Tie every anomaly to a **risk register item**; maintain trend dashboards with thresholds for escalation.
* Enforce **Go/No‑Go criteria** that prohibit proceeding with unresolved critical anomalies.

**Actionable Checks:**

* RCCA records include verification evidence of fixes.
* Risk register references anomalies and test data; trends are reviewed at each milestone.
* Go/No‑Go templates include explicit anomaly disposition criteria.

### **Summary of NASA Lessons Learned for 3.7.2**

| **Lesson** | **Recommendation** | **Key Example** |
| --- | --- | --- |
| FDIR Techniques | Introduce fault detection, isolation, and recovery (FDIR) mechanisms to mitigate risks and ensure system continuity. | Sensors and BIT reduced response times for propulsion failures on orbiting spacecraft. |
| Fault-Tolerant Design | Incorporate fault-tolerant principles for software and hardware to prevent minor subsystem failures from escalating. | A redundant fault-tolerant design avoided unnecessary switchover during a memory corruption. |
| Fault Protection | Use cooperative design between flight and ground systems to ensure autonomous and robust anomaly responses. | Coordinated software/hardware fault protection preserved satellite integrity during power loss. |
| Mars Observer Fault Protection Response | Design fault responses carefully to ensure they do not interrupt critical activities unnecessarily. | Misapplied propulsion fault protection behaviors led to mission failure. |
| Clear Responsibility Assignment (X-34 Risks) | Clearly define roles and ensure comprehensive validation for all contractors/subcontractors involved in safety-critical work. | Improved clarity in X-34 responsibilities ensured flight maneuvers were properly validated. |
| Comprehensive Software Validation | Use anomaly injection and edge case testing for fault detection validation to verify software responses to critical events. | Hazard avoidance fault-handling issues were revealed during rover simulations. |

---

These lessons reinforce the criticality of a robust safety-critical software program, as mandated by **NASA-STD-8739.8**, through fault detection, fault tolerance, coordinated fault protection, proper roles and responsibilities, and rigorous software validation activities. They serve as invaluable guidance for ensuring compliance with Requirement 3.7.2 while promoting safety and mission success.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-023 - Software Safety-Critical Requirements**

3.7.2 If a project has safety-critical software, the project manager shall implement the safety-critical software requirements contained in NASA-STD-8739.8.

The systematic implementation of NASA-STD-8739.8 ensures that safety-critical software components are rigorously analyzed, designed, tested, and validated throughout the lifecycle. By aligning engineering practices to comply with standards like SWE-134 and leveraging tailored tools, methods, and metrics, projects can minimize risks tied to hazardous software contributions, maintain system safety, and fulfill mission objectives successfully.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the identified safety-critical software components and data have implemented the safety-critical software assurance requirements listed in this standard.

## 7.2 Software Assurance Products

The objective of software assurance in safety-critical systems is to ensure compliance with NASA standards for safety-critical software, preserve system integrity, and mitigate risks through a systematic approach to safety analysis, design, verification, and validation.

### 7.2.1 Software Safety Requirements Mapping Table

* **Purpose**: The mapping table documents the traceability of each safety-critical software requirement, ensuring compliance with **NASA-STD-8739.8B** (Software Assurance Standard) [278](#_tabs-<p></p>) and **NPR 7150.2D** [083](#_tabs-<p></p>) (Software Engineering Requirements).
* **Designated Authorities**: Mapping matrices must be signed by the **Engineering Technical Authority (ETA)** and the **Safety and Mission Assurance Technical Authority (S&MA TA)** for each development organization.
* **Objective Evidence Requirements**:
  + Confirm implementation of safety-critical requirements for identified software components.
  + Provide evidence showing compliance with **NASA-STD-8739.8B** and [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements).

## 7.3 Metrics for Safety Assurance

To evaluate the effectiveness and progress of safety assurance activities, track the following metrics:

1. **Safety-Related Requirement Issues**:

   * Open and closed issues tracked over time to pinpoint recurring challenges and resolution rates.
2. **Safety-Related Non-Conformance by Life Cycle Phase**:

   * Number of non-conformances identified in:
     + Requirements phase.
     + Design phase.
     + Testing phase.
     + Operational phase.

These metrics help in monitoring risk trends, refining project processes, and tracking compliance across the development lifecycle. See Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) for additional metric recommendations.

## 7.4 Software Assurance Guidance

### 7.4.1 Step-by-Step Implementation of Safety Assurance

1. **Step 1: Confirm Identification of Safety-Critical Components**:

   * Use **NASA-STD-8739.8**, [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements), and [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) for guidance to determine if software components are safety-critical.
   * Evaluate the software’s role in causing or mitigating hazards identified in the system hazard analysis.
2. **Step 2: Analyze Software Design**:

   * Confirm **partitioning or isolation** of safety-critical elements in software design and code.
   * Ensure the design:
     + Logically separates safety-critical components from non-safety-critical software.
     + Implements fault-tolerant mechanisms to preserve system functionality during failures.
3. **Step 3: Validate Functionality and Data Integrity**:

   * Assess compliance with SWE-134 "a" through "l" at every life cycle milestone (e.g., design reviews, safety reviews, testing). Examples include:
     + **Memory Management (Item f)**:
       - Ensure systems can detect and recover from memory issues (e.g., radiation-induced errors, configuration errors) using techniques like error-checking, memory scrubbing, and authentication.
     + **Command Sequencing (Item h)**:
       - Verify inappropriate command sequencing and commands executed in improper modes/states do not contribute to hazards.
     + **Off-Nominal Condition Responses (Item j)**:
       - Design the ability to detect and mitigate off-nominal conditions within acceptable timeframes before hazards occur.
4. **Step 4: Participate in Reviews**:

   * Safety Engineers should participate in all software reviews impacting safety-critical components, ensuring compliance, traceability, and hazard resolution.
5. **Step 5: Support System Hazard Analysis**:

   * Ensure software contributions are properly documented in hazard reports.
   * Verify safety-critical software designs do not violate independence of hazard inhibits or hardware redundancy.
6. **Step 6: Conduct Safety-Specific Testing**:

   * Test off-nominal scenarios, fault recovery pathways, and safety-critical commands.
   * Validate through unit testing, integration testing, and system testing that safety-critical elements perform as designed under edge cases (e.g., stress testing, disaster testing).

### 7.4.2 Lifecycle-Specific Software Safety Activities

Refer to topic [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase) for details on safety-specific activities by development phase:

1. **Formulation Phase**:

   * Initial hazard identification.
   * Preliminary analysis of safety-critical software contributions.
   * Agreement between ETA and S&MA TA regarding safety-critical designation based on NASA-HDBK-2203 Software Assessment Tool.
2. **Design Phase**:

   * Trace compliance with [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) for safety-critical software features.
   * Validate design isolation mechanisms for safety elements.
   * Ensure design supports system hazard analysis outputs.
3. **Testing Phase**:

   * Assess testing plans for off-nominal scenarios and system faults.
   * Verify proper responses to safety-critical conditions.
   * Confirm test results support closure of hazard verifications ( [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test), [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)).
4. **Operations Phase**:

   * Perform regression testing for software updates.
   * Reassess software contributions to hazards based on operational data.

### 7.4.3 Additional Specific Clarifications for SWE-134 Requirements

Outlined below are examples of clarifications for SWE-134 items **“a” through “l”**:

* **Item a**: Establish Known Safe State.

  + Account for all contributors to "safe state" (e.g., hardware configurations, operational phase, boot code integrity).
* **Item f**: Memory Modifications.

  + Protect against inadvertent memory changes using robust software methodologies (e.g., error detection and correction techniques).
* **Item h**: Command Sequencing.

  + Design and verify commands to ensure adherence to correct sequence and operational mode conditions.
* **Item j**: Off-Nominal Conditions.

  + Implement mechanisms to detect hazards early and transition into safe states promptly or continue operations in reduced functionality.

### **7.4.4 Engineering and SMA Obligations**

NASA-STD-8739.8 obligates the program, engineering, and S&MA teams to ensure:

* Safety-critical software is thoroughly analyzed, implemented, and proven effective.
* Software safety is maintained throughout the system lifecycle: requirements, design, coding, testing, operations, and maintenance.
* Contracts for software acquisition specify safety assurance deliverables and address risks posed by off-the-shelf software.

### **7.4.5 Best Practices for Safety Assurance**

1. **Fault Tolerance**:

   * Design fault-tolerant systems to mitigate software and hardware failures effectively.
2. **Safe Programming Language**:

   * Use programming languages designed for safety-critical applications (e.g., strict type enforcement, compile-time error detection).
3. **Defensive Programming**:

   * Implement programming techniques to anticipate, detect, and recover from potential faults.
4. **Robust Testing**:

   * Conduct exhaustive testing, including off-nominal scenarios, interrupt analysis, stress testing, stability testing, disaster recovery testing, and test coverage analysis.
5. **Peer Reviews**:

   * Collaborate effectively through software reviews to identify and resolve safety-implicated issues early.

### **7.4.6 Special Considerations for Tools and Off-the-Shelf Software**

* Validate tools used in safety-critical development or revalidate them if project-specific conditions differ significantly.
* Assess OTS software contributions to system safety and isolate or integrate components as required by design.

The safety-critical software assurance requirements listed in NASA-STD-8739.8 [278](#_tabs-<p></p>) are:

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

For a list of Safety-Specific Activities by general life-cycle phases, refer to Topic [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase).

The project and engineering have responsibilities to implement an approach that minimizes the risk associated with safety-critical software. The panel below defined what engineering should do when a project has determined that the software is safety-critical.

Additional specific clarifications for the NPR 7150.2 [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) requirement items "a" through "l." :

* **Item a:**Aspects to consider when establishing a known safe state includes the state of the hardware and software, operational phase, device capability, configuration, file allocation tables, and boot code in memory.
* **Item d:** Multiple independent actions by the operator help to reduce potential operator mistakes.
* **Item f:** Memory modifications may occur due to radiation-induced errors, uplink errors, configuration errors, or other causes so the computing system must be able to detect the problem and recover to a safe state. As an example, computing systems may implement error detection and correction, software executable and data load authentication, periodic memory scrub, and space partitioning to protect against inadvertent memory modification. Features of the processor and/or operating system can be utilized to protect against incorrect memory use.
* **Item g:** Software needs to accommodate both nominal inputs (within specifications) and off-nominal inputs, from which recovery may be required.
* **Item h:** The requirement is intended to preclude the inappropriate sequencing of commands. Appropriateness is determined by the project and conditions designed into the safety-critical system. Safety-critical software commands are commands that can cause or contribute to a hazardous event or operation. One must consider not only the inappropriate sequencing of commands (as described in the original note) but also the execution of a command in the wrong mode or state. Safety-critical software commands must perform when needed (must work) or be prevented from performing when the system is not in a proper mode or state (must-not work).
* **Item j:** The intent is to establish a safe state following the detection of an off-nominal indication. The safety mitigation must complete between the time that the off-nominal condition is detected and the time the hazard would occur without the mitigation. The safe state can either be an alternate state from normal operations or can be accomplished by detecting and correcting the fault or failure within the timeframe necessary to prevent a hazard and continuing with normal operations. The intent is to design in the ability of software to detect and respond to a fault or failure before it causes the system or subsystem to fail. If failure cannot be prevented, then design in the ability for the software to place the system into a safe state from which it can later recover. In this safe state, the system may not have full functionality but will operate with this reduced functionality.
* **Item k:** Error handling is an implementation mechanism or design technique by which software faults and/or failures are detected, isolated, and recovered to allow for correct run-time program execution. The software error handling features that support safety-critical functions must detect and respond to hardware and operational faults and/or failures as well as faults in software data and commands from within a program or from other software programs.
* **Item l:** The design of the system must provide sufficient sensors and effectors, as well as self-checks within the software, to enable the software to detect and respond to system potential hazards.

See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing).

Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical software at each code inspection, test review, safety review, and project review milestone.

Software safety requirements must cover “both action (must work) and inaction (must not work). There are two kinds of software safety requirements: process and technical. Both need to be addressed and properly documented within a program, project, or facility.” The Standard required in this requirement was “developed by the NASA Office of Safety and Mission Assurance (OSMA) to provide the requirements for ensuring software safety across all NASA Centers, programs, projects, and facilities. It describes the activities necessary to ensure that safety is designed into the software.  The magnitude and depth of software safety activities should be commensurate with ... the risk posed by the software.”

Software safety is defined as “the aspects of software engineering and software assurance that provide a systematic approach to identifying, analyzing, tracking, mitigating, and controlling hazards and hazardous functions of a system where software may contribute either to the hazard or to its mitigation or control, to ensure safe operation of the system.”

It is important to have a systematic, planned approach for ensuring that safety is designed into developed or acquired software and that safety is maintained throughout the software and system life cycle. NASA-STD-8739.8 specifies the software safety activities, data, and documentation necessary for the acquisition and development of software in a safety-critical system... Safety-critical systems that include software are evaluated for the software's contribution to the safety of the system during the concept phase and should be repeated at each major milestone as the design matures.

Engineering and software assurance initially determine software safety criticality in the formulation phase per NASA-STD-8739.8, Software Assurance Standard; the results are compared and any differences are resolved. As the software is developed or changed and the software components, software models, and software simulations are identified, the safety-critical software determination can be reassessed and applied at lower levels.

The Engineering Technical Authority and S&MA Technical Authority shall jointly determine if the software is designated as “safety-critical.”  The “safety-critical” designation defines additional requirements mapping within this NPR.  Software Safety-Critical Assessment Tool guidance is provided in NASA-HDBK-2203 as well as the software safety-critical determination process defined in NASA-STD-8739.8. Allocation of system safety requirements, hardware, and risk need to be considered in the assessment. The Engineering Technical Authority and S&MA Technical Authority must reach an agreement on the safety-critical designation of software. Disagreements are elevated via both the Engineering Technical Authority and Safety and Mission Assurance Technical Authority chains.

*Cyclomatic complexity* is a software metric used to indicate the *complexity* of a program. It is a quantitative measure of the number of linearly independent paths through a program's source code.

**See the software assurance tab in [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) for an explanation of cyclomatic complexity and code coverage guidance.**

Software Safety Analysis supplements the system hazard analysis by assessing the software performing critical functions serving as a hazard cause or control. The review assures compliance to the levied functional software requirements, including [SWE-134](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements), the software doesn’t violate the independence of hazard inhibits, and the software doesn’t violate the independence of hardware redundancy. The Software Safety Analysis should follow the phased hazard analysis process. A typical Software Safety Analysis process begins by identifying the must work and must not work functions in Phase 1 hazard reports. The system hazard analysis and software safety analysis process should assess each function, between Phase 1 and 2 hazard analysis, for compliance with the levied functional software requirements, including SWE-134. For example, Solar Array deployment (must work function) software should place deployment effectors in the powered-off state when it boots up and requires to initialize and execute commands in the correct order within 4 CPU cycles before removing a deployment inhibit. The analysis also assesses the channelization of the communication paths between the inputs/sensors and the effectors to assure there is no violation of fault tolerance by routing a redundant communication path through a single component. The system hazard analysis and software safety analysis also assure the redundancy management performed by the software supports fault tolerance requirements. For example, software can’t trigger a critical sequence in a single fault-tolerant manner using single sensor input. Considering how software can trigger a critical sequence is true for triggering events such as payload separation, tripping FDIR responses that turn off critical subsystems, failover to redundant components, and providing closed-loop control of critical functions such as propellant tank pressurization.

See also, [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software).

The design analysis portion of software safety analysis should be completed by Phase 2 safety reviews. At this point, the software safety analysis supports a requirements gap analysis to identify any gaps ([SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions)) and ensure the risk and control strategy documented in hazard reports are correct as stated. Between Phase 2 and 3 safety reviews, the system hazard analysis and software safety analysis supports the analysis of test plans to assure adequate off-nominal scenarios [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test), [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) a). Finally, in Phase 3, the system hazards analysis must verify the final implementation and verification upholds the analysis by ensuring test results permit closure of hazard verifications ([SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results)) and that the final hazardous commands support the single command and multi-step command needs and finalized pre-requisite checks are in place.

The requirements specified in this Standard obligate the program, project, and facility, and safety and mission assurance organizations to:

* Identify when software plays a part in system safety and generate appropriate requirements to ensure the safe operation of the system.
* Ensure that software is considered within the context of system safety, and that appropriate measures are taken to create safe software.
* Ensure that software safety is addressed in project acquisition, planning, management, and control activities.
* Ensure that software safety is considered throughout the system life-cycle, including mission concept, generation of requirements, design, coding, test, maintenance, and operation of the software.
* Ensure that the acquisition of software, whether off-the-shelf or contracted, includes evaluation, assessment, and planning for addressing and mitigating risks due to the software’s contribution to safety and any limitations of the software.
* Ensure that software verification and validation activities include software safety verifications and validations.
* Ensure that the proper certification requirements are in place and accomplished before the actual operational use of the software.
* Ensure that changes and reconfigurations of the software, during development, testing, and operational use of the software, are analyzed for their impacts on system safety.”

See also Topic [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations).

The Engineering Technical Authority and S&MA Technical Authority shall jointly determine if the software is designated as “safety-critical.”

### 7.4.7 Basic Steps for Implementing NASA-STD-8739.8

When implementing the requirements of NASA-STD-8739.8, follow the basic steps summarized below:

* Identify safety-critical software.

+ Document identification efforts and results.
  - If no safety-critical software is found, stop.

+ Determine the software safety criticality.
+ Determine the safety effort and oversight required.

### 7.4.8 Development Activities

The appropriate project personnel performs the following development activities to fulfill the software safety requirements:

+ Analyzing or working with system safety to analyze software control of critical functions and the identification of software that causes, controls, mitigates, or contributes to hazards.

+ Identify software safety design features and methods in design documents.
+ Follow proper coding standards (which may include safety features) (See [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards)).
+ Use hazards analysis to identify failures and failure combinations to be tested.

### 7.4.9 Safety and Risk

When identifying software safety requirements applicable to a project, consult existing lists of software safety requirements to identify generic safety requirements. In addition, use techniques such as hazard analysis and design analysis to identify safety requirements specific to a particular project. NASA-GB-8719.13 [276](#_tabs-<p></p>)  provides a list of sources for generic requirements. Appendix H of that guidebook includes a checklist of generic software safety requirements from the Marshall Space Flight Center (MSFC).

Remember to include risk as a factor when determining which requirements are more critical than others.

When developing safety-critical software, the project needs to:

* Design in a degree of fault tolerance, since not all faults can be prevented
* Choose a "safe" programming language; one that enforces good programming practices finds errors at compile-time, has strict data types, bounds checking on arrays, discourages the use of pointers, etc.
* Use coding standards that enforce "safe and secure" programming practices.
* Implement defensive programming.
* Look specifically for unexpected interactions among units during integration testing.
* Evaluate the complexity of software components and interfaces.
* Design for maintainability and reliability.
* Use software peer reviews.
* Use design data analysis, design interface analysis, and design traceability analysis.
* Develop safety tests for safety-critical software units that cannot be fully tested once the units are integrated.
* Use code logic analysis, code data analysis, code interface analysis, and unused code analysis.
* Use interrupt analysis.
* Use test coverage analysis.
* Use stress testing, stability testing, resistance to failure tests, disaster testing.
* Evaluate operating systems for safety before choosing one for the project.
* Review the Design for Safety checklist in Appendix H of the NASA Software Safety Guidebook [276](#_tabs-<p></p>)

See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality).

### 7.4.10 Programmable Logic Devices, Tools, and Off-the-Shelf (OTS) Software

If the project involves programmable logic devices, consult NASA-HDBK-8739.23, NASA Complex Electronics Handbook for Assurance Professionals.  [034](#_tabs-<p></p>)

For tools that are used in the development of safety-critical software, including compilers, linkers, debuggers, test environments, simulators, code generators, etc., consider the following:

* Use tools previously validated for use in the development of safety-critical software, but consider the differences in how those tools were used on the projects for which they were validated and their use on the new project to determine if re-validation is required.
* Tools previously validated for use in the development of safety-critical software and which have been in use for many years in the same environment for the same purposes may not require re-validation.
* For tools not yet approved or for which re-validation is being considered:

+ Consider the tool's maturity.
+ Try to obtain any known bug lists for the tool.
+ Try to obtain any existing tests, analyses, and results for the tool.
+ Obtain an understanding of how the tool could fail and determine if those failures could negatively affect the safety of the software or system for which they are used.
+ Perform safety testing and analysis to ensure that the tools do not influence known hazards or adversely affect the residual risk of the software.
+ Consider independent validation for the tool.

If the project involves off-the-shelf (OTS) or reused software, the project needs to:

* Evaluate system differences that could affect safety.
* Look at interfaces needed to incorporate it into the system or isolate it from critical or non-critical software, as appropriate.
* Perform analysis of the impacts of this software on the overall project, such as:

+ Identifying extra functions that could cause safety hazards.
+ Determining the effects of extra functionality needed to integrate the software with the rest of the system.

* Evaluate the cost of extra analysis and tests needed to ensure system safety due to the use of OTS or reused software.
* Seek insight into the practices used to develop the software.
* Evaluate the V&V results of OTS software to make sure that it is consistent with the level of V&V of the developed software.

For contractor-developed software, the project:

* Includes in the contract:

+ Surveillance or insight activities for the contractor development process.
+ Identification of responsibility for preparing and presenting the Safety Compliance Data Package to the Safety Review Panel.
+ Safety analysis and test requirements.
+ Requirements for delivery of software safety deliverables including software safety plan, all-hazard analyses, audit reports, verification reports, etc.

* Evaluate contractor/provider track record, skills, capabilities, stability.
* Considers performing additional software testing beyond that conducted by the provider.

### 7.4.11 Training and Additional Guidance

For additional considerations when acquiring safety-critical software, see [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance).

Training in software safety is available in the NASA SMA Technical Excellence Program (STEP).

Step 2. Analyze the software design to ensure that partitioning or isolation methods are used in the design to logically isolate the safety-critical design elements from those that are non-safety-critical. - Methods to separate the safety-critical software from software that is not safety-critical, such as partitioning, may be used.

When developing safety-critical software, the project needs to:

* Design in a degree of fault tolerance, since not all faults can be prevented
* Choose a "safe" programming language; one that enforces good programming practices finds errors at compile-time, has strict data types, bounds checking on arrays, discourages the use of pointers, etc.
* Use coding standards that enforce "safe and secure" programming practices.
* Implement defensive programming.
* Look specifically for unexpected interactions among units during integration testing.
* Evaluate the complexity of software components and interfaces.
* Design for maintainability and reliability.
* Use software peer reviews.
* Use design data analysis, design interface analysis, and design traceability analysis.
* Develop safety tests for safety-critical software units that cannot be fully tested once the units are integrated.
* Use code logic analysis, code data analysis, code interface analysis, and unused code analysis.
* Use interrupt analysis.
* Use test coverage analysis.
* Use stress testing, stability testing, resistance to failure tests, disaster testing.
* Evaluate operating systems for safety before choosing one for the project.
* Review the Design for Safety checklist in Appendix H of the NASA Software Safety Guidebook [276](#_tabs-<p></p>)

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) - ("a" portion) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-184 - Software-related Constraints and Assumptions](/spaces/SWEHBVD/pages/102695520/SWE-184+-+Software-related+Constraints+and+Assumptions) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)        * [7.03 - Acquisition Guidance](/spaces/SWEHBVD/pages/102695620/7.03+-+Acquisition+Guidance) * [7.04 - Flow Down of NPR Requirements on Contracts and to Other Centers in Multi-Center Projects](/spaces/SWEHBVD/pages/102695621/7.04+-+Flow+Down+of+NPR+Requirements+on+Contracts+and+to+Other+Centers+in+Multi-Center+Projects) * [7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.10 - Facility Software with Safety Considerations](/spaces/SWEHBVD/pages/102695728/8.10+-+Facility+Software+with+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase) |

# 8. Objective Evidence

This requirement ensures that **NASA-STD-8739.8 [278](#_tabs-<p></p>)** is applied to safety-critical software to minimize risk to personnel safety, mission success, and critical systems. Good objective evidence involves documentation, processes, configurations, and assessments showing that the safety-critical software requirements were implemented as mandated by the standard.

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

This comprehensive set of objective evidence demonstrates that **NASA-STD-8739.8**safety-critical requirements were fully implemented for the software. It underscores compliance throughout development, verification, and testing phases, ensuring safety-critical software is robust, reliable, and adequately managed to meet mission safety goals.

Below are detailed categories of objective evidence aligned with the requirements of **NASA-STD-8739.8**.

## 8.1 Safety-Critical Software Determination and Documentation

Evidence that the software was classified as **safety-critical** using criteria in **NASA-STD-8739.8** and documentation that all safety processes were initiated accordingly.

##### **Must Include**:

* Clear documentation identifying software as **safety-critical** (e.g., from Requirement 3.7.1 determinations).
* Signed records corroborating the classification, rationale, and concurrence from the Safety and Mission Assurance (SMA) and project teams.

##### **Examples of Evidence**:

* Record of decision from a Safety Review Board (SRB) or SMA approval showing the software classification as safety-critical.
* Safety-Critical Software Classification Checklist with detailed criteria and signatures.
* Traceability matrix linking software components to system hazards and showing rationale for classification.

## 8.2 Software Safety Plan

An **approved Software Safety Plan** demonstrates how the project manager ensured compliance with the safety-critical requirements of NASA-STD-8739.8.

##### **Must Include**:

* Description of processes, methods, and tools used to comply with NASA-STD-8739.8 safety-critical software requirements.
* Specific requirements identified by NASA-STD-8739.8 and how they will be implemented for the project.
* Roles and responsibilities for software safety, including SMA’s involvement.
* Strategies for hazard analysis, verification, and validation of safety-critical components.

##### **Examples of Evidence**:

* Signed **Software Safety Plan**, including:
  + Specific NASA-STD-8739.8 paragraphs addressed (e.g., requirements on testing, fault management, code design practices, hazard control, etc.).
  + A list of software development processes modified or tailored to meet safety-critical requirements.
  + SMA and Technical Authority (TA) approval of the plan.
* Inclusion of safety-critical software actions in the project’s broader Software Development Plan or Systems Engineering Management Plan.

## 8.3 Hazard Tracking and Mitigation Evidence

Hazard analysis performed for safety-critical software and linked verification strategies provide concrete evidence of implementing hazard control and risk mitigation requirements from NASA-STD-8739.8.

##### **Must Include**:

* Hazard tracking tools, logs, or reports documenting identified software-level hazards and associated risk rankings.
* Verification and validation procedures to ensure hazard mitigations are implemented and effective.
* Linkage of safety mitigations to specific software components and requirements.

##### **Examples of Evidence**:

* **Hazard Tracking Report**:
  + Identification of hazards involving software failure modes and their associated risk levels.
  + Example: Hazard - “Loss of Rover Navigation”; Software - “Pathfinding Algorithm”; Verification: “Simulations confirm proper execution under fault injections.”
* Evidence showing elimination or mitigation of high-risk hazards (e.g., testing records, inspection charts).
* Regular updates tracking the status of identified hazards (e.g., closed, open, in progress) aligned with project milestones like PDR, CDR, or TRR.

## 8.4 Design and Development Evidence

Objective evidence must confirm compliance with safety design requirements per **NASA-STD-8739.8** during the software development phase.

##### **Must Include**:

* Design artifacts showing adherence to safety-critical requirements, including:
  + Fault tolerance inclusion and redundancies.
  + Isolation mechanisms between safety-critical and non-safety-critical software components.
  + Defensive programming techniques.
* Code analysis or code reviews demonstrating adherence to NASA-STD-8739.8 coding and architectural guidelines.

##### **Examples of Evidence**:

* Signed **Software Design Document (SDD)** detailing:
  + Fault detection and recovery mechanisms, contingency responses.
  + Functional decomposition separating safety-critical modules from non-critical functionality.
* **Code Review Records**:
  + Example findings such as: “Reviewed Fault Handling Module; implemented two-fault tolerance rule. Verified adherence to 100% unit test coverage.”
* **Architecture Diagrams**:
  + Visual representations showing isolation of safety-critical software elements.

## 8.5 Verification and Validation Artifacts

Testing and validation records provide clear evidence that the safety-critical implementation matches NASA-STD-8739.8 requirements. This includes proof of rigorous testing beyond standard software to address criticality.

##### **Must Include**:

* Test plans explicitly addressing safety-critical scenarios or edge cases.
* Evidence of testing for hazardous conditions, failure mode behaviors, and nominal performance of safety-critical functions.
* Traceability of test cases to software-level safety requirements.

##### **Examples of Evidence**:

* **Test Results Documentation**:
  + Example: “Test Case TC-004 validated emergency shutdown mechanism for overheating event within the 1-second response threshold.”
  + Evidence of anomaly/failure injection testing to evaluate fault tolerance and exception handling.
* Signed **Verification Closeout Reports** documenting test coverage and results:
  + “Safety-critical thrust control software passed all V&V criteria outlined in Software Safety Plan and hazard mitigation V&V matrix.”
* Independent Validation Reports demonstrating that V&V activities were executed by an independent team, as required for safety-critical software.

## 8.6 Safety Assurance and SMA Concurrence

To implement **NASA-STD-8739.8**, confirmation from the Safety and Mission Assurance (SMA) organization is required at key milestones.

##### **Must Include**:

* Signed SMA concurrence reports showing they reviewed and approved:
  + Safety-related hazard analyses.
  + Safety-critical classification and mitigation strategies.
  + Safety-critical software test results and verification plans.
* Documentation of SMA verification activities performed.

##### **Examples of Evidence**:

* Formal **Concurrence Letter** signed by SMA Lead stating: “SMA has reviewed and confirmed implementation of safety-critical software standards (NASA-STD-8739.8) for [specific components].”
* Meeting minutes showing SMA review discussions during milestone reviews like PDR, CDR, or TRR.

## 8.7 Configuration Management Processes

Safety-critical software must be rigorously controlled and maintained. Evidence of configuration management practices (e.g., change control) aligned with NASA-STD-8739.8 is critical.

##### **Must Include**:

* Configuration management logs tracking software changes, ensuring changes to safety-critical components follow strict approval processes.
* Documented rationale for any updates or code changes to safety-critical software components.
* Baseline change management records.

##### **Examples of Evidence**:

* Configuration control logs showing:
  + “Change Request CR-045: Adjust thermal control logic. Approved by SMA and CM Board.”
* Baseline documents (e.g., source code repositories) showing status lock for reviewed artifacts.
* Change impact analysis reports linking every safety-critical software modification to hazards and V&V processes.

## 8.8 Training Records

Evidence that staff working on safety-critical software received training on NASA-STD-8739.8 and safety assurance principles helps demonstrate compliance.

##### **Must Include**:

* Attendance lists and materials from safety-related training.
* Certifications for key project personnel (software engineers, testers, SMA team).

##### **Examples of Evidence**:

* Certificate stating: “Jane Doe completed training on NASA software safety standards (NASA-STD-8739.8).”
* Signed meeting minutes from training sessions for safety compliance processes.

## 8.9 Summary of Objective Evidence

| **Category** | **Examples of Evidence** |
| --- | --- |
| **Safety-Critical Software Documentation** | Signed classifications, rationales, and linked hazard analyses. |
| **Software Safety Plan** | Plan demonstrating process adherence, approved by SMA. |
| **Hazard Analysis Reports** | Logs and mitigation strategies addressing software-driven risks or faults. |
| **Design and Development Artifacts** | Design documents, architecture isolating safety-critical code, fault handling reviews. |
| **V&V Evidence** | Test plans, anomaly injection results, module-level validation reports for hazards and fault scenarios. |
| **Safety Assurance (SMA) Concurrence** | Signed SMA review approvals at project milestones. |
| **Configuration Management Logs** | Change control records tracking updates and approval for safety-critical components. |
| **Training Records** | Evidence of team training in safety-critical software requirements. |
