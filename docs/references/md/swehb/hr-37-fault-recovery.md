# HR-37 - Fault Recovery

> NASA Software Engineering Handbook (SWEHB Ver D), page id 171508207. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508207/HR-37+-+Fault+Recovery

HR-37 - Fault Recovery

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508207/HR-37+-+Fault+Recovery#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=171508207)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=171508207&showCommentArea=true&showComments=true#addcomment)

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

4.3.7 The space system shall provide the capability to isolate and recover from faults identified during system development or mission operations that would result in a catastrophic event.

## 1.1 Notes

This capability is not intended to imply a failure tolerance capability or expand upon the failure tolerance capability. The intent is to provide isolation and recovery from faults where the system design (e.g., redundant strings or system isolation) enables the implementation of this capability. Also, any faults identified during system development should be protected by isolation and recovery. However, it is acknowledged that not all faults that would cause catastrophic events can be detected or isolated in time to avoid the event. Similarly, system design cannot ensure that once the fault is detected and isolated that a recovery is always possible. In cases where recovery is not possible, isolation of the fault needs to be sufficient on its own to prevent the catastrophic event.

## 1.2 History

Click here to view the history of this requirement: HR-37 History

HR-37 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.3.7 The space system shall provide the capability to isolate and recover from faults identified during system development or mission operations that would result in a catastrophic event. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

If a fault occurs that could be catastrophic, a determination of the cause must first be made or “isolated” to within the smallest containment region as allowed within system design constraints, after which recovery processes should start to achieve safety fault tolerance to catastrophic events.

This requirement is fundamental to ensuring the safety, reliability, and success of space missions. Developing space systems inherently involves addressing the risks posed by faults that can lead to catastrophic events. These events include the loss of crew, mission failure, or damage to critical subsystems or payloads. The isolation and recovery from such faults reduce their impact and ensure continued mission operations or safe system shutdown.

The rationale for this requirement is driven by the following principles: **mission assurance, crew and system safety, operational reliability, risk mitigation, and compliance with aerospace standards**. This rationale ensures the system can operate within acceptable levels of risk, even in the presence of faults.

This requirement is critical for ensuring the **safety, reliability, and robustness** of space systems under both expected and unexpected conditions. By enforcing **fault detection, isolation, and recovery** capabilities, NASA can address critical risks, maximize mission success rates, and protect human lives and mission assets. This requirement aligns with lessons learned, space standards, and operational best practices, making it foundational for any space system operating in high-risk or autonomous environments.

## 2.1 Key Motivations Behind the Requirement

### 2.1.1 Prevention of Catastrophic Events

The primary motivation for this requirement is to prevent faults that could escalate into events with catastrophic consequences. Catastrophic events include:

* Loss of crew and life (e.g., crew health risks in human-rated systems).
* Damage to expensive spacecraft or critical mission payloads.
* Failure to achieve mission-critical objectives (e.g., science data collection, satellite deployment).

By requiring fault isolation and recovery mechanisms, the system is better equipped to prevent faults from cascading or causing catastrophic consequences.

### 2.1.2 Fault Tolerance for Long-Duration and Autonomous Missions

Space systems often operate in remote or inaccessible environments where human intervention is impossible or significantly delayed. Examples include:

* **Interplanetary Missions (e.g., Mars rovers, planetary orbiters)**: Long communication delays may prevent real-time ground intervention. The system must autonomously isolate and mitigate faults to continue operations.
* **Deep Space Missions (e.g., James Webb Space Telescope)**: Fault repair is impossible in unreachable environments, necessitating robust recovery designs.
* **Human Spaceflight Missions (e.g., Artemis, ISS)**: Crew safety and mission success require systems capable of isolating and mitigating faults autonomously in life-critical systems.

Fault isolation and recovery in these scenarios enhance the system’s robustness to operate with minimal external support while maximizing operational longevity.

### 2.1.3 Improved Mission Resilience and Availability

Faults in space systems are inevitable, given the extreme operational conditions, including radiation, thermal cycling, vacuum, and micrometeoroid impacts. This requirement ensures that the system is designed to minimize the **Mean Time to Repair (MTTR)** while maximizing operational uptime, even after a fault occurs, by enabling:

* **Fault Isolation**: Containing the fault to prevent it from propagating and affecting other subsystems.
* **Fault Recovery**: Restoring functionality or enabling reduced-capability operations to maintain mission objectives.

This ensures that critical missions and payloads can continue to provide value despite the occurrence of faults, avoiding total mission loss.

### 2.1.4 Hazard Mitigation and Spacecraft Survivability

Faults that are not managed could lead to system hazards. Examples include:

* Uncontrolled temperature fluctuations in spacecraft components causing material damage.
* Propellant leaks leading to loss of maneuvering capabilities or explosions.
* Electrical faults causing permanent subsystem failures (e.g., avionics or communication systems).

Designing systems to isolate and recover from faults mitigates these hazards, enhancing overall spacecraft survivability while preserving human lives and/or system integrity.

### 2.1.5 Lessons Learned from Historical NASA Experiences

Failures of past missions underscore the critical importance of fault isolation and recovery mechanisms:

1. **Apollo 13 (1970)**:

   * The oxygen tank explosion was isolated, and recovery strategies (e.g., using the lunar module as a "lifeboat") allowed the crew to return safely.
   * **Lesson**: Effective isolation and recovery capabilities are critical for crew survivability following system-level faults.
2. **Mars Polar Lander (1999)**:

   * The failure of the spacecraft’s descent system was undetected and unrecoverable, ultimately leading to mission loss.
   * **Lesson**: Fault recovery mechanisms must include redundancy and active logic to identify and handle critical failures dynamically.
3. **Kepler Space Telescope (2013)**:

   * After multiple reaction wheel failures, the team found creative ways to recover from the fault, enabling the telescope to achieve an extended mission.
   * **Lesson**: Building fault-tolerant systems allows recovery and mission continuation after hardware degradation.
4. **Columbia Disaster (2003)**:

   * Damage to the thermal protection system during launch went undetected and unmitigated, ultimately leading to loss of the crew upon reentry.
   * **Lesson**: Systems need mechanisms to isolate and mitigate faults during all mission stages, especially those that pose catastrophic risk.

### 2.1.6 Compliance with Aerospace Standards and Practices

NASA standards and industry-wide practices emphasize the need for fault isolation and recovery mechanisms as part of system dependability:

* **NASA-STD-8739.8 (Software Assurance and Software Safety Standard):**

  + Specifies that software must detect, isolate, and recover from faults to prevent catastrophic events.
* **NPR 7150.2 (Software Engineering Requirements):**

  + Requires software fault management to handle faults proactively, including mitigation of high-risk software triggers.
* **ISO 26262 and MIL-STD-882:**

  + Focus on hazard control, fault-tolerant recovery, and system reliability in safety-critical systems.

### 2.1.7 Achieving Systematic Risk Mitigation

Catastrophic risks are identified via risk assessments, such as Hazard Analysis, Fault Tree Analysis (FTA), and Failure Modes and Effects Analysis (FMEA). This requirement inherently supports systematic risk mitigation by enforcing:

* Design decisions that manage identified risks during the development phase.
* Isolation strategies that limit the spread of faults to critical subsystems.
* Recovery strategies that reduce the likelihood of catastrophic outcomes through automated or operator-driven responses.

### 2.1.8 Enhancing Crew and Operator Confidence

For human-rated systems or crew-assisted operations, fault isolation and recovery directly contribute to crew confidence in the system’s ability to detect issues, manage risks, and safeguard both lives and mission success. For unmanned systems, it assures mission operators that system failures will not compromise critical objectives unnecessarily.

## 2.2 Benefits of Meeting the Requirement

### Technical Benefits

1. **Enhanced System Resilience**: Enables the system to continue functioning even after critical faults are introduced.
2. **Improved Fault Containment**: Fault isolation ensures a problem in one subsystem does not cascade to others.

### Operational Benefits

1. **Minimized Downtime**: Rapid isolation and recovery reduce system downtime, maintaining mission-critical operations.
2. **Support for Long-Duration Operations**: Recovery ensures the mission can persist to completion, even in degraded conditions.

### Safety Benefits

1. **Risk Reduction**: Proactively addresses catastrophic risks to minimize the likelihood of mission or crew loss.
2. **Reliability Under Extreme Conditions**: Enables the system to handle unforeseen events (e.g., radiation-induced faults, component failures).

# 3. Guidance

This expanded software engineering guidance aims to provide clear, actionable, and systematic instructions for designing, verifying, and validating fault isolation and recovery capabilities critical to preventing catastrophic events. It incorporates iterative testing, risk-based prioritization, and lessons learned from past missions, while maintaining alignment with NASA standards (e.g., NPR 7150.2 and NASA-STD-8739.8).

The expanded software engineering guidance supports efficient implementation of fault isolation and recovery capabilities that reduce mission risks, ensure system robustness, and safeguard critical assets. By implementing iterative risk assessments, robust fault-handling algorithms, independent verification, and rigorous testing, space systems can meet the demands of extreme environments while mitigating the likelihood of catastrophic outcomes. The focus on fault-handling resiliency ultimately ensures mission success and operational safety.

## 3.1 Enhanced Context and Purpose

### Intent of the Requirement

The system design must ensure that faults leading to catastrophic events are:

1. **Detected**: Faults are identified in real-time or near-real-time via sensors, software monitoring, and built-in fault-detection capabilities.
2. **Isolated**: Once detected, faults must be isolated to prevent propagation across subsystems and to enable continued partial or full operation of unaffected components.
3. **Recovered**: The system should recover to a safe or degraded-but-stable operational state wherever possible. In cases where recovery is infeasible, isolation must be sufficient to prevent escalation of the fault into catastrophic outcomes.

### Considerations:

* The requirement acknowledges that not all potential faults will be detectable or recoverable before escalating. Therefore, system-level redundancy, robustness, and designs that anticipate graceful degradation are critical.
* Fault-handling design decisions must balance software complexity with reliability, ensuring detection, isolation, and recovery mechanisms introduce minimal additional risk to the system.

## 3.2 Expanded Software Engineering Guidance

### 3.2.1 Fault Detection, Isolation, and Recovery Mechanisms

##### **Fault Detection**

* Develop algorithms and mechanisms for real-time fault detection using:
  + Threshold and range monitoring (e.g., temperature, pressure, power levels).
  + Fault signature recognition (e.g., specific sensor patterns or anomalies).
  + Predictive models and trend analysis to anticipate potential faults using historical or telemetry data.
  + Heartbeats/ping monitoring to detect component activity or liveness.

**Best Practice**: Implement multiple detection layers, including built-in self-test (BIST) routines, periodic diagnostic scans, and cross-checks between redundant subsystems to reduce false positives/negatives.

##### **Fault Isolation**

* Incorporate mechanisms to detect and isolate faults efficiently and prevent fault propagation:
  + Use subsystem isolation (e.g., physical or logical isolation) to ensure faults do not cascade across the system.
  + Enable **segregation of critical subsystems** using hardware or software partitioning (e.g., memory protection, fault containment regions).
  + Design fallback states (e.g., degrade operational capabilities gracefully) to prevent complete mission loss.
  + Implement watchdog timers to automatically trigger isolation mechanisms when an unresponsive component is detected.

##### **Fault Recovery**

* Establish robust recovery paths, including:
  + Automatic recovery: Software resets, component reinitialization, or switching to redundant systems with minimal operator input.
  + Operator-enabled recovery: Provide mechanisms for spacecraft operators to remotely execute recovery commands.
  + Graceful degradation: Transition the system to a reduced-function mode when full recovery is infeasible, ensuring at least minimal mission objectives can still be met.

**Critical Consideration**: Include fault recovery testing under worst-case conditions (e.g., degraded power, high latency in communications) to ensure effectiveness under operational constraints.

### 3.2.2 Risk-Based Design and Implementation

* **Failure Mode Prioritization**: Use risk analysis techniques (e.g., Fault Tree Analysis, Failure Modes and Effects Analysis) to identify the most critical faults with catastrophic potential and prioritize fault detection and recovery mechanisms.
* **Hazard Mitigation Strategies**: Ensure fault isolation and recovery mechanisms explicitly mitigate hazards identified during hazard analysis reports (link to the system safety process).
* **Timing Constraints**: Define time-critical requirements for fault detection, isolation, and recovery based on the mission phase and operational context. For instance:
  + Human-rated systems: Require sub-second isolation for life-critical functions.
  + Deep-space systems: Recovery timelines may account for communication delays.

### 3.2.3 Iterative Safety Analysis Techniques

* **Software Fault Tree Analysis (FTA)**:
  + Analyze potential failure points in software for critical systems, tracing top-level hazards (e.g., loss of life support) to possible fault sources in code logic or interfaces.
* **Software Failure Modes and Effects Analysis (SFMEA)**:
  + Establish the impact chains for individual software component failures and verify these align with isolation/recovery designs.
* **Software Safety and Hazard Analysis (SSHA)**:
  + Continually refine fault isolation and recovery logic as potential hazards or operational scenarios evolve during system development.

### 3.2.4 Safety Reviews and Independent Assessments

* **Team Reviews**: Collaborate with safety, operations, and software engineering teams to:
  + Identify gaps in fault isolation/recovery logic.
  + Assess adherence to redundancy and fail-safe design principles.
* **IV&V**: Engage independent reviewers to:
  + Verify that all safety-critical faults are associated with isolation/recovery strategies.
  + Validate software responses to a range of failure scenarios using fault injection tests.

### 3.2.5 Configuration Management and Code Quality

* Ensure strict configuration control for all versions of safety-critical software:
  + Clearly define baselines for fault handling components.
  + Track changes to fault isolation/recovery code in version control systems, linking each change to defect reports or corrective actions taken.
* **Code Quality Objectives**:
  + Adhere to robust coding standards (e.g., MISRA for C/C++ or NASA’s JPL-style guidelines for Python).
  + Limit cyclomatic complexity for fault-critical code to ensure maintainability and minimize hidden risks.

### 3.2.6 Comprehensive Testing and Simulations

* **End-to-End Testing**: Simulate realistic mission scenarios (e.g., launch, deep-space conditions, and return-to-Earth) to verify fault detection, isolation, and recovery capabilities.
* **Fault Injection Testing**:
  + Inject hardware and software faults into critical subsystems to test fault isolation/recovery performance under failure scenarios.
  + Examples of injection: Sensor corruption, communication delays, memory corruption, or random hardware failures.
* **Modified Condition/Decision Coverage (MC/DC)**:
  + Use MC/DC criteria for all safety-critical components to ensure 100% test coverage of detection, isolation, and recovery paths.

### 3.2.7 Training and Documentation

* Provide comprehensive training for operators and controllers:
  + Scenarios for interpreting and responding to annunciated faults.
  + Training in remote recovery processes and constraints (e.g., power management during fault recovery).
* **User Manuals**:
  + Document each fault type, its corresponding detection mechanisms, recovery procedures, fallback states, and potential risks.
  + Ensure manuals are accessible to both operations teams and software developers.

### 3.2.8 Robust Error Handling

* Incorporate fault-tolerant error handling mechanisms:
  + Fail-safes for unrecoverable conditions to preserve spacecraft integrity.
  + Graceful degradation mechanisms for extended missions requiring manual controller intervention (e.g., deep-space missions).

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Requirements related to Human Rated Software.

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

For small projects, limited resources, time constraints, and smaller teams necessitate streamlined processes. This guidance tailors best practices for fault isolation and recovery to smaller projects while maintaining compliance with NASA’s safety-critical standards.

**Key Focus Areas for Small Projects:**

1. Prioritization of critical risks for catastrophic faults.
2. Minimizing complexity in fault detection, isolation, and recovery mechanisms.
3. Leveraging off-the-shelf tools and modular designs for efficient implementation.
4. Maintaining a balance between compliance, capability, and resource limitations.

Small projects can meet the objectives of this requirement by focusing on critical fault scenarios, leveraging lightweight processes, and streamlining testing and documentation. By prioritizing functionality over complexity and leveraging reusable solutions, small projects can effectively deliver fault isolation and recovery mechanisms that help safeguard mission success and mitigate catastrophic events.

## 4.1. Simplify Requirements Analysis and Prioritization

Due to limited resources, small projects must focus on the most **critical faults** that could result in catastrophic events.

* **Perform a fault criticality assessment**:

  + Use simple risk matrices to evaluate faults based on:
    - **Impact**: What components or subsystems would fail?
    - **Likelihood of occurrence**: How likely is the fault under expected mission conditions?
    - **Mission/crew impact**: Could the fault disrupt mission-critical objectives, jeopardize systems, or risk crew safety?
* **Focus on high-priority faults**:

  + Clearly identify safety-critical systems that require fault isolation and recovery mechanisms.
  + Trace faults to hazards (if applicable) using a lightweight approach such as a reduced **Fault Tree Analysis (FTA)** or simplified **Failure Modes and Effects Analysis (FMEA)**.

**Output for Small Projects**:

* A list of critical faults with corresponding fault detection, isolation, and recovery strategies to address catastrophic risks.
* A minimal **Requirements Traceability Matrix (RTM)** tracking faults to system and software requirements.

## 4.2 Simplify Detection, Isolation, and Recovery Mechanisms

**Fault Detection**:

* Leverage hardware protections: Use sensors, watchdog timers, voltage monitors, and checksum validation where possible for real-time fault monitoring.
* Develop basic fault detection logic:
  + Use threshold detection for simpler faults (e.g., temperature ranges, voltage levels).
  + Implement periodic monitoring routines to check system health.
* Rely on onboard diagnostics or off-the-shelf solutions to reduce development time.

**Fault Isolation**:

* Create simple isolation mechanisms:
  + Use redundancy strategies: Design redundant strings or components for critical subsystems. For small projects, redundancy can often be implemented with backups for key components instead of entire subsystems.
  + Logical isolation: Separate critical subsystems in software to prevent cascading effects (e.g., partitions or sandboxing).

**Fault Recovery**:

* Focus on fail-safe rather than full recovery:
  + Implement simple recovery routines, such as resetting software components or switching to redundant systems.
  + Add fallback states or "graceful degradation" modes where the system operates with minimal functionality rather than ceasing operation entirely.

**Key for Small Projects**:

* Use basic state machines or modular fault-handling logic to reduce software complexity.

## 4.3 Adapt Testing and Validation to Scale

Testing in small projects should focus on critical areas by leveraging available tools and simulations without consuming excessive time or resources.

* **Focused Simulations**:

  + Test only the scenarios most relevant to the faults identified as catastrophic (e.g., hardware malfunctions, software failures).
  + Develop simple simulation models to recreate scenarios like sensor failures, power loss, or communication interruptions.
* **Fault Injection**:

  + Insert basic simulated faults (e.g., sensor disconnections, memory overflows) into the software to validate detection, isolation, and recovery processes.
* **Adequate Test Coverage**:

  + Concentrate on safety-critical code paths.
  + Aim for near-complete test coverage using **Modified Condition/Decision Coverage (MC/DC)** for fault-handling modules.
* **Automated Testing**:

  + Use lightweight testing frameworks (like Python’s `pytest` or open-source tools) to validate software behavior under failure scenarios.
* **Independent Peer Reviews**:

  + If a formal IV&V is not feasible, assign team members to independently review each other's code/modules to ensure compliance with safety-critical requirements.

**Small Project Testing Outputs**:

* Test logs showing successful detection, isolation, and recovery from predefined faults.
* Fault injection results documenting software behaviors under failure conditions.
* Coverage reports focused on critical fault-handling modules.

## 4.4 Small-Scale Configuration Management

Given the lean nature of small projects, configuration management must be simple but consistent to prevent errors, especially for safety-critical components.

* Use a **light version control system**: Tools like Git can track changes effectively. Organize branches specifically for:
  + Safety-critical components.
  + Fault-handling routines.
* Maintain disciplined version tracking for safety-critical modules:
  + Clearly identify final baselined versions submitted for testing.
  + Use automated CI/CD pipelines to ensure fault-handling code remains consistent through different build environments.
* Store artifacts centrally:
  + Place fault-related analysis (e.g., FMEA, fault-recovery strategies) in a single accessible repository, along with test cases and test results for traceability.

## 4.5 Safety-Critical Software Considerations

Small projects with safety-critical software must ensure compliance with minimum safety standards without introducing unnecessary scope creep:

* **Adopt NASA’s Minimum Safety Guidelines**:

  + Even for small systems, follow NASA’s Software Assurance and Software Safety Standard (NASA-STD-8739.8) for identifying and mitigating software-related hazards.
* **Identify Safety-Critical Requirements**:

  + Perform a small-scale assessment to determine which software components control safety-critical functionality (e.g., human-rated subsystems, failure-prone logic tied to hazards).
* **Lightweight Error Handling**:

  + Implement centralized error-handling routines (e.g., "try-catch" blocks for critical operations).
  + Ensure the system avoids crashing due to uncaught exceptions or errors.

## 4.6 Training and Documentation

Small teams can streamline training and documentation while ensuring key personnel understand how fault-handling processes work.

* **Simplify Operator Training**:

  + Provide a short guide or quick-reference card for operators.
  + Include step-by-step instructions for handling annunciated faults and manual recovery operations.
* **Streamline Documentation**:

  + Reduce complexity in fault-related documentation:
    - Focus on creating concise fault handling and recovery procedures that detail the type of fault, its detection mechanism, and recovery protocol.
    - Generate lightweight manuals for safety-critical processes tied to commonly identified risks.

Examples of streamlined documentation include:

* **Fault Action Tables**: A table summarizing fault types, detection mechanisms, recovery actions, and fallback behaviors.
* **Minimal User Manuals**: Describe fault behaviors and crew/operator steps for manual override or recovery.

## 4.7 Leveraging Off-the-Shelf and Reusable Components

Small projects should consider adopting or reusing existing hardware and software modules to reduce development time and cost.

* Use **commercial off-the-shelf (COTS) tools** for fault detection, isolation, and recovery when feasible.
* Incorporate **flight-proven designs or open-source codebases**:
  + Examples: Basic fault-tolerant frameworks, data verification libraries, or watchdog timer configurations.
* Customize existing spacecraft subsystems from a prior mission (if applicable) to create a more reliable solution at lower cost.

## 4.8 Checkpoints for Small Projects

To stay aligned with NASA’s objectives while staying resource efficient:

1. **Fault Management Plan**: Concise documentation summarizing fault isolation and recovery design, testing, and mitigation strategies.
2. **Critical Fault Testing**: Evidence of focused tests for catastrophic failure scenarios conducted in realistic environments.
3. **Minimal Artifact Set**:
   * Simplified hazard/fault analysis (e.g., high-level FMEA and FTA).
   * Peer-reviewed fault-handling code modules.
   * User manual addressing fault annunciation, isolation, and recovery.

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

NASA has a long history of analyzing mission successes and failures to derive lessons learned that inform future designs, processes, and procedures. The following lessons address the importance of fault detection, isolation, and recovery capabilities to prevent catastrophic events. These examples provide valuable insights into engineering, operations, and decision-making critical to satisfying Requirement 4.3.7.

---

### **1. Apollo 13 - Oxygen Tank Explosion (1970)**

* **Incident**: An oxygen tank explosion caused a loss of electricity and life-support capabilities in the Command Module. The crew was forced to use the Lunar Module as a "lifeboat."
* **Lesson Learned**:  
  Effective **fault isolation** prevented cascading failures that could have destroyed the spacecraft (e.g., isolating the Command Module from the affected systems). Recovery strategies involving redundant systems allowed the crew to return safely, despite operating in a degraded state.
* **Takeaway for Requirement**:
  + Design systems with redundancy (e.g., backup subsystems) to provide failover capabilities in catastrophic scenarios.
  + Prioritize real-time fault containment to prevent further propagation of a detected fault.

**Source**: NASA LLIS Reference #10166

---

### **2. Columbia Space Shuttle Disaster (2003)**

* **Incident**: A piece of foam insulation struck the orbiter's left wing during launch, damaging the thermal protection system. This went undetected and unrecoverable, leading to a catastrophic reentry failure, resulting in the loss of the spacecraft and crew.
* **Lesson Learned**:  
  Failure to detect and isolate physical damage in flight (and a lack of viable recovery mechanisms) led to the catastrophic loss. Design processes, including pre-launch inspection and in-flight damage detection, were inadequate to identify and address this failure in time.
* **Takeaway for Requirement**:
  + Implement robust fault detection mechanisms to identify critical damage or failures during all mission phases.
  + Ensure recovery options exist for faults detected during operations, especially faults affecting safety-critical systems (e.g., redundant thermal protection measures or damage inspection/repair capabilities).

**Source**: NASA CAIB (Columbia Accident Investigation Board) Report

---

### **3. Mars Polar Lander (MPL) – Premature Shutdown of Descent Engines (1999)**

* **Incident**: During the spacecraft's descent, high-frequency noise in one of the detectors was interpreted as ground contact by the software, leading to premature shutdown of the descent engines. The spacecraft likely crashed on the surface.
* **Lesson Learned**:  
  Faults (such as sensor noise) must be detected, isolated, and recovered early to avoid critical mission loss. Software designed to handle faults must account for off-nominal conditions and provide mechanisms for autonomous recovery.
* **Takeaway for Requirement**:
  + Fault detection mechanisms must include robust validation against sensor noise or erroneous fault triggers.
  + Test fault-handling mechanisms under off-nominal scenarios to validate their effectiveness.
  + Isolation and recovery strategies, such as retries or alternative logic paths, are essential in time-critical sequences.

**Source**: NASA LLIS Reference #18206

---

### **4. Kepler Space Telescope – Reaction Wheel Failure (2013)**

* **Incident**: Kepler experienced the failure of multiple reaction wheels needed for fine-pointing accuracy. The initial recovery efforts focused on isolating the failed reaction wheels and reconfiguring operations. Scientists successfully transitioned to modified mission objectives, extending the spacecraft's productivity.
* **Lesson Learned**:  
  Rapid fault isolation and creative recovery strategies can extend system utility after a critical failure. While the original mission design assumed full reaction wheel functionality, the team demonstrated the importance of adaptability in handling faults during operation.
* **Takeaway for Requirement**:
  + Incorporate fallback or "degraded mode" operational plans into the system design to support recovery in the event of catastrophic faults.
  + Develop operations teams prepared to assess system capabilities post-fault dynamically.
  + Recovery strategies may include adapting mission goals or priorities to work around failed components.

**Source**: NASA LLIS Reference #19758

---

### **5. James Webb Space Telescope (JWST) – Post-Deployment Anomaly Management (2022)**

* **Incident**: During JWST’s complex deployment sequence, unexpected telemetry data in a subsystem raised alarms. The operations team quickly isolated the anomaly, investigated the problem, and allowed the mission to proceed without impacting the telescope’s mission-critical functionality.
* **Lesson Learned**:  
  Predefined fault isolation and recovery procedures must address unexpected anomalies and support decision-making under time constraints. The use of detailed simulations, rehearsals, and contingency planning enabled resolution without mission impact.
* **Takeaway for Requirement**:
  + Pre-plan for anomalies in critical deployment or operational stages, including detailed diagnostic and recovery procedures.
  + Use extensive testing and rehearsals to validate fault-handling mechanisms.
  + Implement telemetry systems capable of providing detailed diagnostic data during fault events.

**Source**: NASA Mission Case Study

---

### **6. ISS – Electrical Power System Fault Tolerance**

* **Incident**: The International Space Station (ISS) experienced multiple electrical faults, including issues with power channels, failed hardware components, and solar array degradation. Effective isolation and redundancy allowed continuous crew support and mission operations despite these failures.
* **Lesson Learned**:  
  System-level redundancy, fault isolation within subsystems, and rapid crew coordination ensured power system faults did not propagate or result in life-threatening conditions.
* **Takeaway for Requirement**:
  + Safety-critical systems (e.g., life support, power management) must be designed with contingency options such as system-level isolation and highly redundant architectures.
  + Isolation mechanisms must ensure partial system continuity during fault investigation and repair.
  + Crew/operator training about fault recovery processes (e.g., equipment replacement, reconfiguration) is essential.

**Source**: NASA LLIS Reference #22376

---

### **7. Software Fault Management – Mars Pathfinder (1997)**

* **Incident**: During operations, the Mars Pathfinder rover experienced recurring resets due to a software architecture issue. A priority inversion in the task scheduler caused the system to become unresponsive. Engineers recovered remotely by reconfiguring the software parameters.
* **Lesson Learned**:  
  Software must be designed to handle resource conflicts gracefully and provide recovery mechanisms for faults such as priority inversion or deadlocks.
* **Takeaway for Requirement**:
  + Implement fault detection for software-triggered anomalies, including resource management failures.
  + Include remote recovery options for software faults (e.g., parameter reconfiguration or full reboot).
  + Resource management logic should include safety-code constructs to prevent or recover from deadlock scenarios.

**Source**: NASA Jet Propulsion Laboratory Study

---

### **8. Viking 1 Lander – Fault Recovery Capabilities (1976)**

* **Incident**: Unexpected faults in the Viking lander’s soil sample collecting arm were identified and isolated early, preventing mission disruption. Recovery mechanisms allowed the system to continue sample collection and analysis, meeting mission goals.
* **Lesson Learned**:  
  Incorporating automated fault recovery logic, combined with fault-tolerant hardware design, ensured mission-critical science objectives were completed under unexpected circumstances.
* **Takeaway for Requirement**:
  + Design fault-tolerant mechanisms in hardware/software for autonomy under time-critical scenarios.
  + Include automated logic to attempt recovery steps before requiring ground intervention.

**Source**: NASA Viking Mission Archives

---

### **Summary of Key Lessons Learned**

1. **Fault Detection**: Ensure robust and validated mechanisms to detect both hardware and software anomalies during all mission stages (e.g., launch, cruise, operations).
2. **Fault Isolation**: Design subsystems to isolate faults to prevent cascading failures or mission-wide impacts. Use physical or logical partitioning when feasible.
3. **Fault Recovery**: Account for degraded operational modes, failovers, or retry mechanisms to extend mission life or prevent complete loss.
4. **Redundancy**: Use redundancy (both hardware and software) as a critical design feature for catastrophic fault management.
5. **Operator Training**: Ensure operators receive detailed anomaly-response training to support fault isolation and recovery during mission operations.
6. **Testing and Simulations**: Validate all fault-management mechanisms using realistic fault injection and operational environment simulations.

By leveraging these lessons, engineers can ensure space systems are better equipped to handle faults effectively, reducing the likelihood of catastrophic mission outcomes.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-37 - Fault Recovery**

4.3.7 The space system shall provide the capability to isolate and recover from faults identified during system development or mission operations that would result in a catastrophic event.

By implementing these improvements, the software assurance and software safety practices can systematically identify gaps, reduce risks, and ensure compliance with this requirement. This approach focuses on delivering high-reliability systems capable of handling faults effectively under all operational conditions while minimizing the risk of catastrophic outcomes.

## 7.1 Tasking for Software Assurance

1. Confirm that the hazard reports or safety data packages contain all known software contributions or events where software, either by its action, inaction, or incorrect action, leads to a hazard.
2. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
3. Assess that hazard analyses (including hazard reports)identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
4. Confirm that the traceability between software requirements and hazards with software contributions exists.
5. Develop and maintain a software safety analysis throughout the software development life cycle.
6. Ensure that safety-critical software requirements are implemented per the NPR 7150.2 Requirements Mapping Matrix and tested or verified.
7. Perform safety reviews on all software changes and software defects.
8. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.
9. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically the off-nominal scenarios to mitigate the impact of hazardous behaviors. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks). Ensure that the project has developed and executed test cases to test the software system’s recovery from faults.
10. Analyze the software test procedures for the following:
    1. Coverage of the software requirements.
    2. Acceptance or pass/fail criteria,
    3. The inclusion of operational and off-nominal conditions, including boundary conditions,
    4. Requirements coverage and hazards per [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) and [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), respectively.
11. Perform test witnessing for safety-critical software to ensure that all faults identified during system development or mission operations are detected, isolated, and recovered from.
12. Confirm that test results are sufficient verification artifacts for the hazard reports.
13. Confirm that strict configuration management is maintained to ensure that the correct software versions and configurations are used.
14. Ensure comprehensive training and documentation for operators is available.

## 7.2 Software Assurance Products

This enhanced guidance builds on the provided framework, streamlining tasks and refining critical processes for clarity and ease of implementation while maintaining adherence to NASA standards such as NASA-STD-8739.8 and NPR 7150.2. The improvements focus on actionable recommendations, proper categorization of assurance activities, and alignment with software lifecycle stages.

The following software assurance products support fault isolation and recovery capabilities. These artifacts provide the necessary evidence that the system design, implementation, and testing processes meet mission-critical safety and reliability requirements.

1. **Software Assurance Status Reports (8.52)**

   * Regularly generate reports summarizing assurance activities, defect trends, and progress toward fault isolation/recovery compliance.
   * Highlight open issues related to catastrophic fault-handling mechanisms and track them to closure.
2. **Software Requirements Analysis (8.54)**

   * Evaluate the completeness, correctness, and traceability of all software requirements tied to fault detection, isolation, and recovery (FDIR).
   * Confirm that fault-handling requirements comply with NASA safety standards and prevent catastrophic outcomes.
3. **Software Design Analysis (8.55)**

   * Verify that software architecture accommodates necessary fault isolation and recovery mechanisms.
   * Assess design scalability to ensure additional fault scenarios, if discovered, can be incorporated without significant rework.
4. **Source Code Quality Analysis (8.56)**

   * Conduct static code analysis to identify defects, unsafe constructs, or deviations from coding standards.
   * Focus on safety-critical paths tied to fault management.
   * Evaluate cyclomatic complexity to ensure maintainability and minimize logic errors in fault detection/recovery handling.
5. **Testing Analysis (8.57)**

   * Review all testing artifacts (e.g., plans, procedures, and results) for adequate verification of fault-handling capabilities.
   * Ensure that FDIR scenarios (normal operations, failure modes, and recovery procedures) are comprehensively tested.
6. **Software Safety and Hazard Analysis (8.58)**

   * Maintain continuous hazard analysis throughout development to identify new software-induced hazards or fault scenarios.
   * Evaluate mitigations for hazards linked to software-related fault isolation and recovery.
7. **Audit Reports (8.59)**

   * Document findings from process and product audits to confirm adherence to safety-critical software assurance requirements.
8. **Test Witnessing Signatures (SWE-066)**

   * Certify that all safety-critical fault isolation and recovery procedures have been tested, witnessed, and evaluated.

## 7.3 Metrics

Defining and tracking software assurance (SA) metrics is critical to evaluating compliance with the requirement, identifying potential gaps, and monitoring progress toward delivering reliable and safe software systems.

### 7.3.1 Verification & Validation Metrics

* **Test Coverage**:
  + **Goal**: Achieve 100% test coverage for safety-critical code paths that involve fault detection, isolation, and recovery.
  + Cover both nominal and off-nominal scenarios, with emphasis on boundary conditions and failure states.
* **Defect Density**:
  + Measure the number of defects per thousand lines of code during testing to assess software reliability and track progress in reducing fault proneness.
* **Requirements Traceability**:
  + Stay above 95% traceability between requirements, design, code, test cases, and test results to ensure fault isolation and recovery requirements are systematically addressed.

### 7.3.2 Safety Metrics

* **Hazard Coverage**:
  + Track the percentage of hazards related to fault-handling addressed during testing.
* **Safety-Critical Compliance**:
  + Monitor the implementation and verification of all safety-critical requirements tied to FDIR to ensure fault-handling compliance.

### 7.3.3 Quality Metrics

* **Code Quality**:
  + Leverage tools to measure code maintainability (e.g., adherence to coding standards, cyclomatic complexity).
* **Code Churn**:
  + Monitor areas of code with frequent modifications that may introduce defects into fault-handling logic.

### 7.3.4 Performance Metrics

* **Fault Response Time**:
  + Measure the latency between fault detection, isolation, and recovery to ensure timely response to avoid catastrophic events.
* **System Uptime**:
  + Assess system availability, focusing on its ability to operate under faults during critical mission phases.

### 7.3.5 Configuration Management Metrics

* **Version Completeness**:
  + Confirm updates to safety-critical software versions are tracked and verified.
* **Change Requests**:
  + Track safety-related change requests and measure their impact on schedules and fault-related defect introduction.

### 7.3.6 Training Metrics

* **Training Coverage**:
  + Track completion rates for training programs related to fault isolation and recovery, especially among developers and operators.

### 7.3.7 IV&V Metrics

* **IV&V Participation**:
  + Record involvement in safety reviews and ensure feedback is systematically incorporated.
* **IV&V Outcomes**:
  + Track IV&V findings and resolutions, with emphasis on fault-handling scenarios.

## 7.4 Examples of Software Assurance Metrics

Metrics are critical indicators of progress and areas needing remediation. Examples include:

* **Defect Metrics**:
  + Total non-conformances discovered during each testing phase (categorized by status: open/closed) and their severity.
  + Number of safety-related non-conformances reported during fault-handling testing.
* **Traceability Metrics**:
  + Percentage of requirements traced to tests for hazard controls.
  + Number of hazards tested vs. total identified hazards containing software.
* **Code Coverage Metrics**:
  + Percentage of safety-critical code tested.
  + Modified Condition/Decision Coverage (MC/DC) metrics for fault-handling logic.
* **Safety Metrics**:
  + Number of hazards verified with tests and hazard reports.
  + Safety-critical requirement verification trends.
* **Configuration Metrics**:
  + Total number of configuration audits vs. planned audits.

## 7.5 Guidance

The following assurance tasks ensure that fault isolation and recovery systems are designed, implemented, and tested effectively:

### 7.5.1 Analysis and Design Assurance

* Ensure that fault-handling mechanisms are addressed early in requirements analysis, ensuring clarity and completeness.
  + Confirm fault requirements are derived from system safety analysis (e.g., hazard reports, FTA, or FMEA).
* Verify fault isolation and recovery algorithms during design analysis, focusing on their modularity and fail-safe characteristics.

### 7.5.2 Testing Assurance

1. **Witnessing Tests**:
   * Observe tests for fault detection, isolation, and recovery to validate that catastrophic events are prevented.
   * Validate timing metrics—such as fault detection duration—to ensure that faults are resolved before escalating into hazardous conditions.
2. **Simulations**:
   * Confirm the execution of simulations modeling fault impacts and recovery performance during mission-critical scenarios.
3. **Test Artifact Review**:
   * Certify test results as acceptable verification evidence, aligning them with hazard analyses.

### 7.5.3 Configuration Management Assurance

* Ensure proper tracking of fault-handling software, hazard analyses, and test artifacts to prevent inconsistencies.

### 7.5.4 Safety Reviews

* Confirm that changes to software tied to fault isolation/recovery mechanisms are peer-reviewed.
* Validate that defect fixes do not introduce new risks.

### 7.5.5 Training and Documentation

* Confirm availability of user manuals and operator training emphasizing fault annunciation, recovery execution, and fallback procedures.

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence ensures that this system requirement is verifiably implemented, validated, and meets mission safety and reliability criteria. Below is a comprehensive framework for the types of objective evidence that can demonstrate compliance with this requirement.

Objective evidence combines requirements traceability, safety analysis, testing outcomes, metrics, operational scenarios, independent reviews, and documentation artifacts. Below is how the evidence aligns with key activities:

* **Design**: Fault management architecture diagrams, software safety analyses.
* **Development**: Source code reviews, static analysis, and configuration control items.
* **Testing**: Fault injection results, test coverage reports, and anomaly resolution.
* **Operations**: Telemetry logs, operator manuals, and training records.

By gathering and organizing this evidence throughout the software lifecycle, teams ensure compliance with Requirement 4.3.7 while building confidence in the system's ability to handle faults effectively and safely.

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

### 8.1.1 Requirements Compliance Evidence

* **Requirements Traceability Matrix (RTM)**:
  + Demonstrates traceability of fault detection, isolation, and recovery (FDIR) requirements through all stages (system, software, hardware, and test).
  + Confirm that every FDIR requirement is linked to design artifacts, test cases, and verification methods.
* **Safety-Critical Requirements Mapping**:
  + A compiled list of safety-critical software and hardware requirements tied to catastrophic events and fault management.
  + Clearly identifies which faults are linked to system hazards, consistent with safety reports (e.g., derived from hazard reports or fault trees).

### 8.1.2 Software Design and Architecture Evidence

* **Fault Management Architecture Diagrams**:
  + Software and architecture documentation visually depicting fault detection, isolation, and recovery mechanisms.
  + Includes subsystem/component relationships, fault paths, isolation layers, and recovery processes.
* **Redundancy Design Report**:
  + Evidence of redundancy in system design (e.g., redundant components, backup processes) to handle single-point failures.
* **Failure Propagation Analysis**:
  + Analysis showing how fault isolation mechanisms prevent faults from propagating to other subsystems.

### 8.1.3 Hazard Analysis and Safety Assessment Evidence

* **Hazard Analysis Reports**:
  + Reports (e.g., from Failure Modes and Effects Analysis [FMEA] or Fault Tree Analysis [FTA]) that identify potential hazards due to software faults and their mitigations.
  + Includes classifications of faults (e.g., identified during design, operations, or testing) and their risk prioritization.
* **Software Safety Analysis**:
  + Evidence documenting software-specific hazards and their mitigations, including measures to prevent software faults from triggering hardware or operational hazards.
  + Utilizes safety techniques (e.g., Software Fault Tree Analysis [SFTA], hazard cause tracing).
* **Test Evidence for Hazard Verification**:
  + Results showing that hazard controls (e.g., fault isolation/recovery procedures) have been tested and verified.

### 8.1.4 Test and Validation Evidence

* **Test Plans and Procedures**:
  + Test plans explicitly covering fault condition scenarios for detection, isolation, and recovery.
  + Includes simulations, fault injection testing, and end-to-end operational testing that replicate real-world conditions.
* **Test Results**:
  + Test results confirming successful execution of fault handling mechanisms under normal and off-nominal conditions.
  + Includes measurable data:
    - Time to detect, isolate, and recover faults.
    - Accuracy of fault identification (e.g., false positives/negatives).
* **Code Test Coverage Reports**:
  + Reports verifying that all safety-critical software related to fault detection, isolation, and recovery has achieved 100% Modified Condition/Decision Coverage (MC/DC).
  + Demonstrates that all fault paths, handling logic, and recovery mechanisms are tested.
* **Fault Injection Test Results**:
  + Evidence from simulated faults (e.g., sensor failures, hardware disconnections, software exceptions) showing the system can detect, isolate, and recover without cascading failures.
  + Fault scenarios should cover:
    - Random hardware failures.
    - Redundant system failover.
    - Boundary and overload conditions.

### 8.1.5 Performance Evidence

* **Response Time Metrics Report**:
  + Metrics tracking the time taken for the fault management system to:
    - Detect and isolate faults.
    - Recover to a safe or degraded state.
  + Evidence that the response time is fast enough to prevent catastrophic consequences.
* **System Availability and Uptime Reports**:
  + Evidence showing that the system remains fully or partially operational during and after faults.

### 8.1.6 Configuration Management Evidence

* **Configuration Item List (CIL)**:
  + A controlled list of software and hardware items identified as safety-critical for fault isolation and recovery.
  + Ensures that versions of fault isolation/recovery algorithms are documented and reviewed.
* **Change Logs**:
  + Records of updates and modifications to safety-critical software, hardware, and firmware components related to fault-handling capabilities.
  + Includes justifications for changes, potential impacts on fault management, and results of regression tests.

### 8.1.7 Independent Verification and Validation (IV&V) Evidence

* **IV&V Reports**:
  + Reports demonstrating independent assessment of FDIR mechanisms and their compliance with safety and system requirements.
  + Includes:
    - Inspection reports for fault detection algorithms.
    - Validation test reports for isolation efficiency and recovery effectiveness.
* **Anomaly Resolution Reports**:
  + Documentation of IV&V-identified issues related to fault management and evidence showing their resolution.

### 8.1.8 Operational Evidence (Mission Context)

* **Operational Fault Scenarios**:
  + A record of faults encountered during testing or mission operations, including:
    - Description of the fault.
    - Detection, isolation, and recovery actions performed.
    - Outcome of the scenario.
* **Telemetry Logs**:
  + Telemetry data showing fault detection and isolation during mission simulation or operational scenarios.
  + Verifies that system response aligns with predefined recovery protocols.
* **Operator Procedures Documentation**:
  + Evidence that mission operators are provided with clear, tested fault-handling protocols to execute recovery in cases where automated recovery fails.

### 8.1.9 Training and Documentation Evidence

* **Training Records**:
  + Evidence showing that personnel involved with FDIR development, testing, and operations have completed required training.
  + Includes fault-handling scenarios and recovery procedures.
* **User Manual**:
  + Manuals documenting fault annunciation, operator responses, recovery protocols, and warnings.
  + Provides a step-by-step guide for fault recovery in scenarios where automation is unavailable.

### 8.1.10 Code and Quality Evidence

* **Source Code Analysis Results**:
  + Static code analysis report showing adherence to coding standards for safety-critical software.
  + Focus on fault handling paths, error recovery mechanisms, and absence of unsafe constructs.
* **Code Review Records**:
  + Peer review comments and resolutions for safety-critical code modules handling FDIR.
* **Defect Trend Reports**:
  + Evidence documenting the defect density, including historical data showing improvements in fault-handling logic through the lifecycle.

### 8.1.11 Reporting and Metrics Evidence

* **Metrics Reports**:
  + Reports documenting key metrics, such as:
    - Fault detection coverage.
    - Test coverage for fault scenarios.
    - Number of unresolved safety-related non-conformances.
    - Time metrics for fault detection, isolation, and recovery.
    - Retest metrics linked to resolved faults.
* **Lessons Learned**:
  + Documentation of lessons learned from previous projects, operations, or tests that influenced the design or testing of fault-handling mechanisms for the current project.
