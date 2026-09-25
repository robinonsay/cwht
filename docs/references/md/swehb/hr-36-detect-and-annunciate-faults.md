# HR-36 - Detect And Annunciate Faults

> NASA Software Engineering Handbook (SWEHB Ver D), page id 171508203. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508203/HR-36+-+Detect+And+Annunciate+Faults

HR-36 - Detect And Annunciate Faults

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508203/HR-36+-+Detect+And+Annunciate+Faults#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=171508203)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=171508203&showCommentArea=true&showComments=true#addcomment)

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

4.3.6 The space system shall provide the capability to detect and annunciate faults that affect critical systems, subsystems, or crew health.

## 1.1 Notes

NASA-STD-8719.29, NASA Technical Requirements for Human-Rating, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: HR-36 History

HR-36 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.3.6 The space system shall provide the capability to detect and annunciate faults that affect critical systems, subsystems, or crew health. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

It is necessary to alert the crew to faults (not just failures) that affect critical functions. A fault is defined as an undesired system state. A failure is an actual malfunction of a hardware or software item's intended function. The definition of the term fault envelopes the word failure since faults include other undesired events such as software anomalies and operational anomalies.

The ability to detect and annunciate faults is foundational to ensuring mission safety, preserving system integrity, and maintaining crew health in hazardous or complex space environments. This requirement addresses the need for timely fault management to prevent minor issues from escalating into catastrophic events, which is critical for mission success and life protection.

## 2.1 Fault Management in Space Systems

Space systems operate in high-risk environments where faults—whether minor or severe—can jeopardize mission objectives, system functionality, or even human lives. Fault management is the strategic discipline of **detecting, isolating, and addressing errors** in a way that minimizes impact, mitigates risks, and provides actionable information to the crew or ground control. Detecting and annunciating faults in a timely manner ensures proper responses to such faults are executed, preserving mission continuity and safety.

#### Real-World Relevance

* Unlike terrestrial systems, space systems cannot rely on quick physical intervention or external corrections, so automated fault detection and annunciation are vital.
* For crewed missions, detecting faults in systems like life support, propulsion, or thermal regulation directly prevents harm to astronauts and ensures survivability.

## 2.2 Components of Fault Management Addressed by the Requirement

This requirement emphasizes two critical capabilities:

1. **Fault Detection**:

   * The system must identify anomalies or deviations in critical systems, components, or performance metrics.
   * Detection must be accurate, reliable, and capable of identifying fault types relevant to mission-critical operations.
2. **Fault Annunciation**:

   * The system must communicate detected faults effectively to the appropriate stakeholders, such as crew members, ground systems, or automated control mechanisms.
   * Annunciation must enable prompt corrective action by providing clear, prioritized, and actionable fault notifications (e.g., alerts, warnings).

## 2.3 Specific Goals of the Requirement

#### a. **Protecting Crew Health**

* **Rationale**: In human spaceflight, astronaut safety is the highest priority. Detecting and annunciating faults in life support systems (e.g., oxygen, CO₂ scrubbers, thermal control) ensures that environmental parameters critical to life are continuously monitored.
* **Examples**:
  + Faults in fire detection and suppression systems must be annunciated to avoid accidents.
  + Anomalies in biomedical monitoring systems must be flagged to prevent health deterioration.

#### b. **Ensuring System and Subsystem Availability**

* **Rationale**: Space missions rely on highly interdependent and critical systems (e.g., propulsion, power, thermal control). Timely fault detection and annunciation minimize disruptions by enabling quick responses.
* **Examples**:
  + Detection of a power supply fault could initiate recovery actions, such as switching to redundant systems.
  + An early warning about coolant system failure could permit preventive measures, preserving temperature control for sensitive hardware.

#### c. **Preventing Fault Propagation**

* **Rationale**: Small faults in interconnected spacecraft systems can propagate, impacting adjacent systems (e.g., thermal hot spots degrading electronics, which then fail to maintain attitude control). Detecting faults early and annuncing them prevents cascading failures.
* **Example**: A minor valve failure in a fuel delivery subsystem may eventually lead to engine shutdown if not identified and resolved early.

#### d. **Enabling Automation and Operational Decisions**

* **Rationale**: Automated responses are critical in environments where real-time human intervention is delayed, such as deep space or autonomous planetary explorers. Annunciating faults to automation systems supports responses such as failover, self-repair, or system reconfiguration.
* **Examples**:
  + A robotic Mars rover detecting—but failing to annunciate—a wheel motor fault might lose mobility unnecessarily with no opportunity for alternative maneuvers.
  + Spacecraft fault annunciation systems alert the crew or automation system to initiate fallback transitions (e.g., switching to a backup module).

#### e. **Supporting Mission Control and Diagnostics**

* **Rationale**: For crewed and unmanned missions, ground operators rely on real-time fault annunciation to track system status, identify corrective actions, and monitor spacecraft health—ensuring situational awareness without direct physical access.
* **Examples**:
  + During the Apollo 13 incident, fault detection and annuncation systems alerted mission control to oxygen tank failures, enabling the team to formulate critical recovery plans.
  + On the ISS, command and control relies on fault annunciation systems for air quality monitoring or solar array power fluctuations.

## 2.4 Failures of Fault Detection and Annunciation: Case Examples

#### **a. Challenger Space Shuttle Disaster (1986)**

* Cause: System failures related to an O-ring design flaw led to a catastrophic explosion. No real-time fault detection and annunciation mechanisms were present to observe anomalous temperature effects on the O-rings.
* Rationale Reinforcement:
  + If real-time detection of solid rocket motor joint issues had been annunciated, the mission could have been aborted before launch.

#### **b. Mars Polar Lander (1999)**

* Cause: Fault in landing sequence software caused the spacecraft to crash. The lack of annunciation prevented early detection of the premature engine shutdown issue resulting from spurious sensor signals.
* Rationale Reinforcement:
  + Annunciating false sensor readings could have triggered overrides or led to a diagnostic loop preventing mission loss.

#### **c. Columbia Space Shuttle Disaster (2003)**

* Cause: A foam strike at launch damaged thermal protection tiles, which later led to catastrophic reentry failure. Traditional fault detection failed to detect or annunciate damage during flight.
* Rationale Reinforcement:
  + Annunciating anomalies (such as abnormal heat during re-entry) could have led to mission adaptations or inspections.

## 2.5 Tie to System-Level and Programmatic Goals

#### **a. Space System Resilience**

* The resilience of a space system heavily depends on its ability to self-monitor and detect faults in critical systems. This enables redundancy, fallback modes, and corrective actions to be implemented, minimizing failure risks.

#### **b. Integration with Fault Management Strategies**

* Fault detection and annunciation are part of higher-order fault management plans that include **Fault Detection, Isolation, and Recovery (FDIR)** mechanisms. For example:
  + **Detection**: Identify faulty conditions or components.
  + **Isolation**: Determine the specific failure source.
  + **Recovery**: Initiate pre-planned procedures that reconfigure or fix the system.

#### **c. Responding to Disparate Failure Modes**

* Critical systems such as power, propulsion, thermal, and life support systems can experience a variety of failure modes, including hardware failures, software anomalies, and environmental interactions (e.g., radiation). Fault detection is necessary to address the wide range of possibilities effectively.

## 2.6 Risk Reduction and Justification for Annunciation

#### **a. Supports Early Warning**

* Provides proactive alerts to prevent faults from escalating into catastrophic events.

#### **b. Reduces Mission Abort Risk**

* Early fault isolation may allow continuation of the mission in degraded modes rather than forcing an abort.

#### **c. Aids Crew Survival**

* Announcing environmental and life support issues facilitates immediate crew action to mitigate hazards.

#### **d. Ensures Data Logging for Post-Event Analysis**

* Annunciation systems store fault data for diagnostics, contributing to lessons learned and future risk reductions.

### **2.7 Summary of the Rationale**

Fault detection and annunciation are critical for the following reasons:

* **Safety**: Protects astronauts by detecting life-threatening faults and alerting crews in time to take corrective action.
* **Reliability**: Preserves system integrity by addressing common or rare faults before they propagate into system-wide failures.
* **Mission Success**: Ensures mission objectives are met despite off-nominal situations through timely recognition and suitable response.
* **Diagnostics and Future Learnings**: Provides real-time and post-mission feedback for operational decision-making and design improvement.

Complying with this requirement ensures a robust fault management capability that enhances system resilience, crew survival, and mission accomplishment in the unforgiving, high-risk environment of space.

# 3. Guidance

This guidance incorporates industry best practices, detailed tasks, lessons learned, and alignment with NASA standards such as **NPR 7150.2**, **NASA-STD-8739.8**, and fault management principles. It provides a structured, actionable roadmap for ensuring that software can effectively detect and communicate faults.

By implementing these enhanced software engineering tasks, the space system ensures it can reliably detect, annunciate, and respond to faults that affect critical systems, subsystems, or crew health. These measures safeguard mission success and human safety under both nominal and unexpected conditions.

## 3.1 Enhanced Software Engineering Tasks to Detect and Annunciate Faults

To ensure the space system can reliably detect and correctly annunciates faults affecting critical systems, subsystems, or crew health, software tasks must integrate a fault management lifecycle composed of **detection, isolation, reporting, and annunciation**. The following tasks should be implemented:

### 3.1.1 Fault Detection and Reporting Mechanisms

* **Objective**: Develop robust mechanisms to monitor critical systems, detect faults, and report them in a timely and actionable manner.
* **Key Activities**:
  + **Real-Time Monitoring**: Design software with real-time telemetry monitoring to detect anomalies in performance parameters (e.g., temperature, pressure, voltages, health status).
  + **Threshold-Based Detection**: Implement threshold-based limits for key metrics (e.g., "out of bounds" values or trends indicating potential degradation).
  + **Event Detection**: Use event-driven logging systems to recognize specific sequences of actions or states (e.g., command or sensor failure sequences).
  + **Self-Monitoring Software**: Create mechanisms for the software to detect its own anomalies, such as timing errors, task overruns, or memory corruption.

### 3.1.2 Safety Analysis Techniques

* **Objective**: Identify and analyze software-related failure modes or hazards to define effective fault detection and annunciation mechanisms.
* **Key Activities**:
  + Perform **Software Fault Tree Analysis (FTA)** to identify critical fault paths and interdependencies among subsystems.
  + Conduct **Software Failure Modes and Effects Analysis (FMEA)** to systematically evaluate failure impacts, root causes, and detection methods.
  + Leverage outputs of FTA and FMEA to:
    - Define software responses for each critical fault.
    - Ensure system redundancies adequately support fault resilience.

### 3.1.3 Fault Annunciation Mechanisms

* **Objective**: Develop fault annunciation capabilities that inform users (crew, ground operators, or automation systems) about detected faults in a clear, actionable manner.
* **Key Activities**:
  + **Prioritized Alerts**: Ensure the software differentiates by fault severity (e.g., *warnings, errors, critical faults affecting crew health*). Use prioritization to prevent alarm fatigue.
  + **Localization**: Provide specific information on the source of faults, subsystem affected, and suggested recovery actions.
  + **User Interface Integration**: Design interface systems (e.g., crew displays or telemetry consoles) that provide intuitive annunciation, system status dashboards, and fault diagnostics.
  + **Automated Annunciation**: Integrate with downstream systems to trigger automated recovery protocols where possible and notify mission control for further analysis.

### 3.1.4 Safety Reviews & Change Assessments

* **Objective**: Ensure updates to software (new requirements or changes) maintain fault detection and annunciation reliability and do not introduce new vulnerabilities.
* **Key Activities**:
  + Integrate fault detection mechanisms into software safety reviews at **all developmental gates**.
  + Perform specific audits for every software change (including bug corrections or new features) to evaluate:
    - Impact on existing fault detection mechanisms.
    - Introduction of new fault risks.
  + Confirm that all fault-related safety requirements remain valid following software modifications.

### 3.1.5 Configuration Management

* **Objective**: Ensure that only verified and validated software configurations, fault detection logic, and control algorithms are deployed.
* **Key Activities**:
  + Utilize **software version control systems (e.g., Git, Subversion)** to maintain a configuration baseline for critical fault detection modules.
  + Manage configurations for software components specific to safety-critical systems, ensuring no deviations occur during updates.
  + Conduct **Functional Configuration Audits (FCA)** and **Physical Configuration Audits (PCA)** to confirm the fault detection software matches approved specifications and baselines.

### 3.1.6 Independent Verification and Validation (IV&V)

* **Objective**: Confirm that fault detection and annunciation software meets its requirements through independent oversight and testing.
* **Key Activities**:
  + Validate that detection algorithms account for all identified fault scenarios (nominal, off-nominal, operational edge cases, and degraded modes).
  + Review annunciation systems to ensure actionable data is conveyed (e.g., error type, affected system, and next steps).
  + Audit IV&V test reports, tracing defects or anomalies back to their root causes and ensuring fixes resolve identified gaps.

### 3.1.7 Error Handling and Recovery Mechanisms

* **Objective**: Implement robust recovery mechanisms that address detected faults, mitigating their impact on critical systems and preventing escalation.
* **Key Activities**:
  + Design software for **graceful degradation**: Ensure the system continues operating at reduced functionality when faults occur.
  + Implement **error isolation** routines: Confine detected faults to prevent their propagation (e.g., isolate failed nodes in a network or disable failed components).
  + Develop recovery protocols, including:
    - Automatic failover logic to redundant systems.
    - Reset mechanisms to clear transient faults.
    - Alerts to the operator for manual recovery if automation fails.

### 3.1.8 Simulations and Testing

* **Objective**: Validate detection and annunciation systems using a robust test suite simulating fault conditions.
* **Key Activities**:
  + Conduct **off-nominal and boundary condition tests** to confirm accurate fault detection (e.g., testing input parameter extremes and invalid data scenarios).
  + Perform **fault injection tests** in simulated hardware/software environments to verify that:
    - Faults are correctly detected.
    - Annunciations provide timely and actionable notifications.
    - Responses prevent cascading failures.
  + Integrate hardware-in-the-loop (HIL) simulations for end-to-end testing of mission-critical systems.

### 3.1.9 Code Coverage using MC/DC Criterion

* **Objective**: Ensure comprehensive test coverage for safety-critical fault-handling code paths, avoiding gaps in validation.
* **Key Activities**:
  + Measure and document **100% Modified Condition/Decision Coverage (MC/DC)** for:
    - Fault detection logic.
    - Annunciation pathways.
    - Recovery algorithms.
  + Identify and address untested code regions or failure conditions not covered during development or unit testing.

### 3.1.10 Safety-Critical Software Requirements

* **Objective**: Demonstrate that all hazard-related software requirements from the **NPR 7150.2 Requirements Mapping Matrix** are implemented and tested.
* **Key Activities**:
  + Map safety-critical requirements to their corresponding design, implementation, and test cases in the **Requirements Traceability Matrix (RTM)**.
  + Verify that the software meets the design intent:
    - Detects faults for all components identified as critical to crew health or system success.
    - Executes annunciation routines upon detection.

### 3.1.11 Training and Documentation

* **Objective**: Ensure end-users can interpret annunciated faults and respond effectively.
* **Key Activities**:
  + Develop **operator training programs** that include fault recognition, annunciation interpretation, and recovery protocol execution.
  + Write and distribute a **user manual** detailing:
    - Possible fault types, causes, and impacts.
    - Recovery steps for each fault.
    - Methods to escalate faults to ground control for additional diagnostics.
  + Provide system engineers with documentation explaining the fault management architecture (detection algorithms, external triggers, and dependencies).

## 3.2 Expected Software Engineering Products

1. **Fault Response Mapping**:  
   Matrix linking fault scenarios to detection mechanisms, annunciations, and recovery procedures.
2. **Testing Results**:
   * Fault injection reports.
   * MC/DC coverage reports.
3. **Safety-Critical Traceability Matrix (Requirements ↔ Tests)**:  
   Verifies end-to-end traceability between faults and corresponding mitigations.
4. **IV&V Results**:  
   Independent fault detection and annunciation validation reports.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-](https://swehb-pri.msfc.nasa.gov/display/SWEHBVD/SWE-134+-+Safety-Critical+Software+Design+Requirements)[053 - Manage Requirements Changes](https://swehb-pri.msfc.nasa.gov/display/SWEHBVD/SWE-053+-+Manage+Requirements+Changes) - * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) - * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) - * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) - * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) - * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) - * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) - * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) - * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) - * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) - * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) - * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) -        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Requirements related to Human Rated Software.

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

For smaller projects, the scope, resources, and complexity may be limited, but the critical nature of fault detection and annunciation remains essential. The guidance below simplifies processes and scales to smaller projects while meeting the intent of this requirement. It focuses on lean practices, automation, and streamlined oversight to ensure critical fault management capabilities are implemented without excessive cost or complexity.

For smaller projects, focus on lightweight implementations while ensuring compliance with the requirement's intent. By minimizing scope, using automation tools, and focusing on critical subsystems, small projects can meet fault detection and annunciation needs without overly complex or resource-intensive processes.

## 4.1 Key Considerations for Small Projects

1. **Risk-Based Prioritization**: Focus on fault detection and annunciation for the systems and subsystems with the **highest risk** to mission success or crew health. Minimize investment in non-critical systems.
2. **Iterative Development and Testing**: Adopt lightweight development practices (e.g., agile or incremental prototypes) to build, test, and refine fault management systems progressively.
3. **Leverage Automation and Open Tools**: Utilize automated testing tools, static code analyzers, and open-source libraries to detect and validate faults effectively without requiring specialized resources.
4. **Streamlined Documentation**: Produce concise documentation targeting key artifacts necessary to demonstrate compliance (e.g., hazard reports, fault detection flow diagrams, test logs, simplified traceability matrices).

## 4.2 Simplified Guidance for Fault Detection and Annunciation

### 4.2.1. Implement Simplified Fault Detection Mechanisms

Due to resource limitations, small projects prioritize essential fault detection techniques for critical systems:

* **Threshold Monitoring**: Establish basic threshold parameters (e.g., acceptable ranges for temperature, pressure, voltage, etc.).
* **Rule-Based Detection**: Use simple "if/then" logic to detect out-of-spec values or failure indications (e.g., sensor flags, invalid data inputs).
* **Minimal Event Logging**: Implement lightweight logging systems to record anomalies for diagnostics and performance monitoring.

**Example**: For a small satellite with limited propulsion systems, monitor fuel pressure and temperature against predetermined thresholds, and log deviations for fault identification.

### 4.2.2 Implement Clear Fault Annunciation Mechanisms

Small projects can use straightforward fault annunciation methods to notify operators or trigger response logic:

* Use **Basic Notification Systems**, such as:
  + Crew or ground-based **alerts via displays** (e.g., visual cues like color-coded indicators for warnings/errors).
  + **Telemetry Messages**: Pack fault data into telemetry streams for ground processing.
* **Prioritized Annunciation**: Ensure faults are categorized by severity (e.g., critical faults triggering immediate alerts vs. minor anomalies logged for further assessment).

**Example**: An onboard temperature monitoring system triggers a yellow light for warnings and switches to red with audio for critical faults affecting crew health.

### 4.2.3 Focused Safety Analysis and Hazard Assessments

Perform lightweight hazard and safety analyses targeting only the most critical subsystems.

* **Small-Scale FTA/FMEA**:
  + Perform Fault Tree Analysis (FTA) or Failure Modes and Effects Analysis (FMEA) to identify failure risks for critical subsystems.
  + Focus only on key hazards that impact safety or mission success (e.g., life support failure or communication blackout).
* **Hazard Prioritization**: Rank faults by risk/impact, prioritizing those that could lead to catastrophic events.

**Example**: For a small rover, analyze failure scenarios for mobility components (e.g., wheel motors), but omit low-risk components like ancillary payloads.

### 4.2.4 Limited Configuration Management

Small projects can simplify configuration management practices while maintaining consistency:

* Use a **Version Control System**: Tools like Git ensure fault detection code is consistently maintained and tracked.
* Maintain a **Change Log**: Document code or requirement changes related to fault monitoring/control to avoid introducing vulnerabilities.

### 4.2.5 Perform Lean Independent Verification and Validation (IV&V)

Small projects can engage in streamlined IV&V approaches to validate fault detection and annunciation systems:

* **Early IV&V**: Conduct IV&V in a focused manner early in the project lifecycle to ensure essential fault detection and annunciation functionality meets intent.
* **Targeted IV&V Scope**: Validate only safety-critical software components rather than the full system.
* Use automated IV&V tools for tests like static analysis and fault injection simulation.

### 4.2.6 Simplify Error Handling and Recovery Mechanisms

Due to resource constraints, keep error handling and recovery mechanisms basic:

* Define **Fallback Procedures**: Default the system to safe modes for detected faults (e.g., standby or reduced functionality).
* **Basic Recovery Logic**: Implement simple error isolation routines for detected faults, such as isolating failed components or restarting software services.

**Example**: For a power system anomaly, detect zero voltage conditions and automatically trigger a failover to backup batteries or initiate system shutdown protocols.

### 4.2.7 Conduct Lightweight Simulations and Testing

Small projects can validate fault detection and annunciation capabilities through focused and cost-effective testing:

* **Unit Tests**: Develop and execute unit tests for fault detection algorithms (e.g., boundary value, edge case tests).
* **Fault Injection**: Simulate simple fault scenarios to test responses (e.g., feeding "out of range" values into the system).
* **Integration Tests**: Verify that fault detection modules interact correctly with other mission-critical components (e.g., sensors, displays).
* Conduct **Basic Scenario Simulations**: Test workflows under nominal and off-nominal conditions using a small dataset.

**Example**: Simulate an invalid pressure reading for a fuel tank to verify that the software correctly detects the fault and triggers a notification to ground systems.

### 4.2.8 Documentation and Training

Focus on minimal yet practical documents and training materials:

* **User Manuals**: Include fault descriptions, notifications, and simple recovery procedures for crew or operators.
* **Fault Scenarios Reference**: Provide brief documentation on common operational fault scenarios and software responses.
* **Training Programs**: Conduct small-scale workshops or recorded sessions to familiarize operators or ground teams with fault recognition and recovery workflows.

**Example**: Draft a one-page guide for fault handling that describes annunciation patterns (e.g., light or sound codes) and recovery steps.

## 4.3 Expected Artifacts for Small Projects

1. **Fault Detection Logic Documentation**: Simplified schematics outlining detection and annunciation logic.
2. **Hazard Analysis Reports**: Prioritized list of hazards with detection methods for top risks.
3. **Test Reports**: Evidence of unit tests, fault injection tests, and basic integration tests.
4. **User Manual**: Step-by-step instructions for identifying faults and executing recovery.
5. **Configuration Log**: Documentation of software changes and versions affecting fault detection modules.

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

NASA’s vast history of system development, flight operations, and incident investigations offers valuable lessons that can guide the implementation of fault detection and annunciation systems. The following lessons learned are drawn from documented experiences, mishaps, and successes in NASA programs and are directly applicable to ensuring robust fault detection and annunciation capabilities.

---

### **1. Challenger Space Shuttle Disaster (1986)**

* **Lesson Learned**: Detect and annunciate critical system failures early to allow time for corrective action.
* **Key Issue**: The Challenger disaster was caused by the failure of an O-ring in a solid rocket booster. Pre-launch conditions (low temperatures) increased O-ring vulnerability, but no real-time monitoring or annunciation system provided insight into this critical issue.
* **Application to Requirement 4.3.6**:
  + Implement proactive fault monitoring for critical systems during all mission phases (pre-launch, launch, and operations).
  + Ensure environmental conditions (temperature, pressure, etc.) that impact system performance are assessed in real time, and errors are annunciated before faults escalate.
  + Tie fault detection thresholds to pre-analyzed hazard conditions (e.g., out-of-limit temperatures triggering a system hold).

---

### **2. Mars Polar Lander Loss (1999)**

* **Lesson Learned**: Ensure fault detection and annunciation systems cover all stages of the mission, including transients and mode changes.
* **Key Issue**: During the spacecraft's descent, the flight computer incorrectly interpreted a transient signal from a micro-switch as a completed landing event. This fault was not detected or annunciated, leading to premature engine shutdown and the loss of the lander.
* **Application to Requirement 4.3.6**:
  + Fault detection systems must account for transient signals or system mode transitions, avoiding false positive or false negative detection.
  + Test fault annunciation thoroughly in simulated off-nominal conditions, especially transitions between mission phases.
  + Include redundancy in fault annunciation to ensure accuracy; for example, validate a landing signal by cross-checking multiple sensor readings.

---

### **3. International Space Station (ISS) Ammonia Leak Detection (2013)**

* **Lesson Learned**: Annunciate critical faults in a crew-accessible and unambiguous manner to enable rapid decision-making.
* **Key Issue**: In 2013, the ISS experienced an ammonia coolant leak that was detected by telemetry and eventually confirmed by visual inspection during a spacewalk. While the detection system functioned, there were delays in annunciating the severity of the issue to the ISS crew for timely mitigation.
* **Application to Requirement 4.3.6**:
  + Design annunciation systems to clearly indicate the severity and priority of critical faults using human-readable formats (e.g., dashboards or audible alerts).
  + Use prioritization frameworks (e.g., critical, warning, advisory levels) to reduce confusion and alarm fatigue during fault notification.
  + Train operators and crew on the interpretation of fault notifications, ensuring they can quickly recognize and respond to critical alerts.

---

### **4. Columbia Space Shuttle Disaster (2003)**

* **Lesson Learned**: Provide cross-system fault annunciation to ensure mission operators have complete situational awareness.
* **Key Issue**: Damage to Columbia’s thermal protection system occurred during launch, caused by foam debris striking the wing. Fault detection systems for the tiles were absent, and mission controllers only became aware of the damage after reentry, by which time the fault led to a catastrophic failure.
* **Application to Requirement 4.3.6**:
  + Implement instrumentation to monitor structural integrity and detect critical damage (e.g., real-time sensors to monitor external impacts or structural stress).
  + Ensure the fault annunciation system transmits detected anomalies across spacecraft systems and to ground control in real time for collaborative decision-making.
  + Establish contingency plans for handling undetected faults and incorporate periodic fault detection sweeps.

---

### **5. Apollo 13 Oxygen Tank Explosion (1970)**

* **Lesson Learned**: Fault annunciation during cascading failure events must prioritize root causes over symptoms.
* **Key Issue**: An explosion in one of Apollo 13’s oxygen tanks caused cascading failures in the spacecraft’s power and life support systems. The fault detection system raised multiple, simultaneous alarms, making it difficult for the crew to quickly diagnose the root cause versus secondary effects.
* **Application to Requirement 4.3.6**:
  + Design software systems to prioritize annunciation of root cause faults over secondary effects to guide operators toward effective mitigation.
  + Include hierarchical fault filtering to suppress redundant or cascading alarms, avoiding operator overload.
  + Conduct fault injection tests to simulate cascading fault scenarios and evaluate system behavior in diagnosing and annunciating faults.

---

### **6. Crew-1 Mission (2020) – SpaceX Dragon**

* **Lesson Learned**: Autonomous fault detection should supplement manual detection in advanced systems with limited operator interaction.
* **Key Issue**: The Crew-1 mission of the SpaceX Dragon vehicle relied heavily on autonomous systems for piloting and fault management, with limited manual fault detection by the crew. The mission highlighted the importance of ensuring autonomous fault detection systems operate robustly, even under degraded conditions.
* **Application to Requirement 4.3.6**:
  + Incorporate redundant fault detection systems (e.g., hardware- and software-based approaches) for autonomous operations.
  + Test autonomous systems under degraded conditions (e.g., partial system failures) to validate fault detection and annunciation robustness.
  + Ensure that detected faults are clearly annunciated to both the crew and ground operators, allowing for coordinated responses.

---

### **7. Skylab Gyroscope Failures (1973)**

* **Lesson Learned**: Annunciate non-critical faults if they have potential to trigger future critical failures.
* **Key Issue**: Skylab experienced gyroscope failures that were initially categorized as minor. However, these malfunctions later escalated and endangered the spacecraft's attitude control. Fault annunciation focused on immediate critical faults, overlooking warnings of increasing stress on non-critical components.
* **Application to Requirement 4.3.6**:
  + Detect and annunciation "leading indicators" of critical system faults (e.g., trends in power consumption, vibration levels, or temperature increases).
  + Design the fault system to provide predictive alerts for non-critical anomalies that could contribute to mission-critical failures.
  + Establish thresholds that prompt early intervention to avoid escalation.

---

### **8. Mars Curiosity Rover (2012) – Communication Anomaly**

* **Lesson Learned**: Comprehensive fault testing needs to include all operational environments (e.g., hardware, software, communication, etc.).
* **Key Issue**: During early operations, a transient communications anomaly temporarily disrupted telemetry signals from Curiosity. While the rover’s internal systems detected the issue, proper annunciation to ground operators was delayed due to outdated protocols.
* **Application to Requirement 4.3.6**:
  + Ensure fault annunciation systems cover the entire operational context, including communication channels and ground interfaces.
  + Test annunciation systems for loss of communication or intermittent fault responses, ensuring operators are informed even under degraded conditions.
  + Include fault detection pathways for communication protocols to enhance mission reliability.

---

### **9. Hubble Space Telescope Gyroscope Anomalies**

* **Lesson Learned**: Regular updates to fault detection/annunciation software can extend system lifespan and mitigate emerging issues.
* **Key Issue**: The Hubble Space Telescope encountered repeated failures of its gyroscopes during operation. Over time, updated software added more refined failure thresholds and annunciation priority, aiding decision-making and enhancing the system’s longevity.
* **Application to Requirement 4.3.6**:
  + Design fault systems for modularity, allowing updates during the mission to refine detection thresholds and annunciation criteria.
  + Use post-mission evaluations of past fault detections to improve future fault monitoring system designs.

---

### **Conclusion**

NASA’s lessons learned emphasize the importance of fault detection and annunciation systems that are proactive, reliable, and capable of providing actionable information. Implementing these insights can ensure the timely identification of critical faults, protect crew health, and enhance the survivability of space systems. By analyzing historical successes and failures, small and large projects alike can establish resilient systems that safeguard mission success.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-36 - Detect And Annunciate Faults**

4.3.6 The space system shall provide the capability to detect and annunciate faults that affect critical systems, subsystems, or crew health.

This improved guidance ensures that software assurance efforts for detecting and annunciating faults are comprehensive, measurable, and aligned with critical mission requirements. By integrating enhanced software assurance products, metrics, and processes, NASA projects can confidently implement reliable fault management systems that safeguard mission success and crew health.

## 7.1 Tasking for Software Assurance

1. Confirm that the hazard reports or safety data packages contain all known software contributions or events where software, either by its action, inaction, or incorrect action, leads to a hazard.
2. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
3. Assess that hazard analyses (including hazard reports) identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
4. Confirm that the traceability between software requirements and hazards with software contributions exists.
5. Develop and maintain a software safety analysis throughout the software development life cycle.
6. Ensure that safety-critical software requirements are implemented per the NPR 7150.2 Requirements Mapping Matrix and tested or verified.
7. Perform safety reviews on all software changes and software defects.
8. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.
9. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically the off-nominal scenarios to mitigate the impact of hazardous behaviors. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks.) Ensure that the project has developed and executed test cases to test the detection and annunciation of faults.
10. Analyze the software test procedures for the following:  
    a.    Coverage of the software requirements.   
    b.    Acceptance or pass/fail criteria,  
    c.    The inclusion of operational and off-nominal conditions, including boundary conditions,   
    d.    Requirements coverage and hazards per [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) and [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), respectively.
11. Perform test witnessing for safety-critical software to ensure that all faults that affect critical systems are detected and annunciated.
12. Confirm that test results are sufficient verification artifacts for the hazard reports.
13. Confirm that strict configuration management is maintained to ensure that the correct software versions and configurations are used.
14. Ensure comprehensive training and documentation for operators is available.

## 7.2 Software Assurance Products

This improved software assurance guidance builds upon the original framework, emphasizing actionable steps, scalability, and alignment with NASA standards. It provides clarity on software assurance tasks, necessary metrics, and expected software assurance products to ensure the space system meets this critical requirement effectively.

To achieve comprehensive assurance, the following artifacts should be produced and evaluated throughout the software development lifecycle, ensuring robust fault detection and annunciation mechanisms are in place:

#### **Key Software Assurance Products**

1. **Software Assurance Status Reports**:

   * Periodic reports summarizing assurance activities, findings, and status of fault detection/annunciation implementation.
   * Include summaries of defects, risks, and mitigation actions related to critical fault detection scenarios.
2. **Software Requirements Analysis**:

   * Confirm that requirements are complete, traceable, and validated, with explicit focus on detecting and annunciating faults affecting critical systems, subsystems, and crew health.
3. **Software Design Analysis**:

   * Review system design artifacts (e.g., architecture diagrams, UML models) to ensure fault detection and annunciation mechanisms are correctly integrated and meet the required failure reporting thresholds.
4. **Source Code Quality Analysis**:

   * Use automated tools (e.g., static analysis, linting) to identify safety-related anomalies and ensure compliance with coding standards for safety-critical software.
5. **Testing Analysis**:

   * Report on the adequacy of test designs and executions, ensuring all fault detection and annunciation scenarios are thoroughly tested, including nominal, off-nominal, boundary cases, and recovery procedures.
6. **Software Safety and Hazard Analysis**:

   * Perform iterative software safety analyses that map faults to hazards and mitigation strategies. Ensure hazard reports align with project safety objectives and NASA-STD-8739.8.
7. **Software Fault Tree Analysis (FTA) & Failure Modes and Effects Analysis (FMEA)**:

   * Complete these analyses for fault detection and annunciation scenarios to identify potential failures and dependencies across critical subsystems.
8. **Audit Reports (FCA/PCA)**:

   * Functional Configuration Audit (FCA) and Physical Configuration Audit (PCA) reports ensure critical software items for fault handling are correctly implemented, tested, and documented according to project baseline.
9. **SWEs Work Product Assessments**:

   * Evaluate key work products (Software Test Plan, Procedures, Reports, and User Manuals) to ensure the quality and consistency of fault detection and annunciation functionalities across the lifecycle.
10. **Automated Tool Results**:

    * Submit reports from static/dynamic code analysis tools, debuggers, and testing frameworks showing coverage and validation of safety-critical fault-handling software components.

## 7.3 Enhanced Metrics for Software Assurance

For fault detection and annunciation mechanisms, focus on quantitative metrics that ensure systematic verification and validation (V&V), safety-critical compliance, and overall reliability:

### 7.3.1 Verification and Validation Metrics

1. **Test Coverage**:

   * Target 100% code coverage as measured by MC/DC for all fault detection and annunciation software paths (including nominal and failure modes).
   * Report percentage of test coverage for safety-critical fault-handling routines.
2. **Defect Density**:

   * Track the number of defects detected during testing per thousand lines of code, emphasizing safety-critical components.
3. **Requirements Traceability**:

   * Ensure traceability metrics demonstrate that all requirements for fault detection/annunciation link to design components and corresponding test cases.

### 7.3.2 Safety Metrics

1. **Hazard Analysis Coverage**:

   * Measure the number of hazards analyzed versus total identified, ensuring alignment with fault-related software components and mitigation strategies.
2. **Safety-critical Requirements Compliance**:

   * Report the percentage of safety-related requirements implemented and validated, including fault detection logic and annunciation features.
3. **Safety-Related Defect Trends**:

   * Monitor frequency and severity of defects identified in safety-critical components over time to assess improvement and residual risk.

### 7.3.3 Quality Metrics

1. **Code Quality Metrics**:

   * Measure cyclomatic complexity for fault-handling logic, targeting ≤15 for safety-critical segments to minimize risk of error.
   * Report results of static analysis tools identifying code violations, concurrency issues, or untested paths.
2. **Code Churn**:

   * Evaluate the frequency and extent of code changes for fault-related components, ensuring stability over iterations.

### 7.3.4 Performance Metrics

1. **Fault Detection Response Time**:

   * Measure system latency in detecting and annunciating faults—prioritize efficiency to reduce delays in operator or automated responses.
2. **System Uptime**:

   * Quantify system operational availability during critical mission phases to verify fault detection reliability in degraded conditions.

### 7.3.5 Configuration Management Metrics

1. **Version Control**:

   * Ensure 100% tracking of configuration changes for fault detection/annunciation modules via source control tools.
2. **Change Requests Impact**:

   * Analyze frequency, scope, and resolution time of defect-related change requests that affect fault detection functions.

### 7.3.6 Training Metrics

1. **Training Completion Rates**:

   * Track the percentage of personnel trained on fault detection/annunciation workflows, including response procedures and recovery execution.
2. **Operator Fault Recognitions**:

   * Measure success rates in simulation exercises where operators interpret annunciated faults correctly (e.g., mappings to mitigative actions).

## 7.4 Enhanced Guidance for Software Assurance Tasks

### 7.4.1. Fault Detection and Reporting Mechanisms

* Verify that robust mechanisms are implemented, including:
  + Threshold monitoring for critical parameters (e.g., pressure, temperature).
  + Event-driven systems handling transient anomalies.
* Confirm built-in redundancy in fault detection logic to preserve reliability.

### 7.4.2 Software Safety and Hazard Analysis

* Ensure hazard analyses include thorough evaluations of potential faults:
  + Use Software Fault Tree Analysis and FMEA for identifying dependencies and failure propagation.
  + Track mitigation effectiveness for hazards related to fault annunciation processes documented in hazard reports.

### 7.4.3 Peer Reviews for Safety-Critical Software

* Participate in dedicated peer reviews designed to detect gaps in fault response logic or annunciation mechanisms. Focus reviews on:
  + Handling ambiguous or cascading faults.
  + Confirmation of fault behaviors during extreme or boundary conditions.

### 7.4.4 Test Witnessing for Recovery Processes

* Actively witness tests for safety-critical fault detection and annunciation outcomes. Focus assurance efforts on:
  + Verifying automated and operator-driven recovery steps.
  + Confirming error isolation routines prevent cascading faults.
  + Documenting recovery success rates in off-nominal scenarios.

### 7.4.5 Configuration Management and Simulations

* Ensure strict version control and audit trails for software changes during fault-related updates.
* Confirm simulation exercises model realistic fault conditions for verification.

### 7.4.6 Training and Documentation

* Expand assurance oversight for operator training programs, ensuring competency in fault interpretation and recovery.
* Evaluate manuals for accuracy and inclusion of detailed fault handling procedures.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-](https://swehb-pri.msfc.nasa.gov/display/SWEHBVD/SWE-134+-+Safety-Critical+Software+Design+Requirements)[053 - Manage Requirements Changes](https://swehb-pri.msfc.nasa.gov/display/SWEHBVD/SWE-053+-+Manage+Requirements+Changes) - * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) - * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) - * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) - * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) - * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) - * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) - * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) - * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) - * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) - * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) - * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) -        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence demonstrates compliance with this requirement through verified documentation, testing results, reports, and artifacts generated during the software/system development lifecycle. This evidence provides independent, traceable proof that the fault detection and annunciation systems are implemented, functional, validated, and meet mission-critical needs.

By ensuring these categories of objective evidence are produced, reviewed, and approved, compliance with this requirement can be clearly demonstrated, supporting mission readiness and safety.

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

### 8.1.1. Requirements and Design Artifacts

These artifacts document and validate how the requirement is implemented in the system.

1. **System-Level Design Documentation**:

   * System architectures, schematics, and Unified Modeling Language (UML) diagrams showing fault detection and annunciation pathways.
   * Diagrams indicating interactions between subsystems (e.g., sensors, data processors, displays) supporting fault detection.
   * Descriptions of prioritization schemes for faults (e.g., warnings, errors, and critical failures).
2. **Software-Level Design Documentation**:

   * Software architecture design showing:
     + Integration of fault detection logic into system components.
     + Annunciation mechanisms for fault severity (e.g., crew displays and ground telemetry).
   * Data flow diagrams showing input/output interactions for fault detection and annunciation.
3. **Requirements Traceability Matrix (RTM)**:

   * Evidence showing each fault detection and annunciation requirement is:
     + Linked to its corresponding design feature.
     + Tied to relevant test cases for verification.
4. **Hazard Analysis Reports**:

   * Documentation identifying potential hazards caused by faults in safety-critical systems, subsystems, or components.
   * Traceability of hazard mitigation strategies to specific fault detection and annunciation implementation.

### 8.1.2 Testing and Validation Evidence

This category focuses on the results of testing and validation activities that verify fault detection and annunciation performance under nominal, degraded, and off-nominal conditions.

1. **Software Test Results**:

   * Unit test results demonstrating that fault detection mechanisms correctly identify anomalies in system parameters (e.g., pressure, temperature, power).
   * Integration test results showing fault detection interactions between software modules.
   * System-level regression test results ensuring previous fault detection logic remains valid despite updates to the software or system.
2. **Fault Injection Test Reports**:

   * Evidence of testing scenarios where faults were intentionally inserted into subsystems to confirm:
     + Fault detection thresholds are correctly triggered.
     + Annunciation mechanisms notify operators appropriately.
   * Simulation outputs of nominal, boundary, and degraded operating conditions.
3. **Code Coverage Reports**:

   * Test coverage results showing all fault detection/annunciation paths are tested and validated.
   * Metrics such as **Modified Condition/Decision Coverage (MC/DC)** for safety-critical components, targeting 100% critical-path coverage.
4. **Automated Tool Results**:

   * Reports from static analysis tools confirming the reliability, performance, and correctness of fault detection software.
   * Results from dynamic analysis tools showing runtime performance during fault handling.

### 8.1.3 Safety Assurance Evidence

Provides proof that all safety-critical software elements directly tied to fault detection and annunciation are analyzed and reviewed to meet safety standards.

1. **Hazard Reports**:

   * Detailed reports identifying faults that could lead to hazardous events.
   * Verification of annunciation thresholds tied to mitigating such hazards.
   * Evidence showing that faults have recovery procedures designed to prevent escalation into catastrophic outcomes.
2. **Software Safety Analysis**:

   * Evidence from techniques such as:
     + **Fault Tree Analysis (FTA)** tracing root causes of faults and confirming detection mechanisms.
     + **Failure Modes and Effects Analysis (FMEA)** mapping fault effects and annunciation pathways.
3. **Safety Reviews Documentation**:

   * Meeting minutes or review documentation showing:
     + Approval from safety reviewers for fault detection thresholds and annunciation strategies.
     + Verification of compliance with safety-related fault handling requirements.

### 8.1.4 Independent Verification and Validation (IV&V) Evidence

Provides independent assurance that the fault detection and annunciation system meets its requirements.

1. **IV&V Test Reports**:

   * Results showing independent validation of software fault detection algorithms and annunciation features aligning with mission scenarios.
   * Confirmation that safety-critical fault paths were tested and mitigations verified.
2. **Test Witnessing Records**:

   * Signatures or documented observations from IV&V personnel confirming test execution and results, particularly for safety-critical systems.
3. **Non-Conformance Reports (NCRs)**:

   * Documentation of issues discovered during IV&V testing tied to fault detection/software failure mechanisms.
   * Evidence showing corrective actions resolved non-conformances in these areas.

### **8.1.5** Configuration **Management Evidence**

Ensures that the correct versions of software and documentation related to fault detection and annunciation are delivered and baselined.

1. **Configuration Audit Reports**:

   * Functional Configuration Audit (FCA) verifying that fault detection features are implemented and functional as designed.
   * Physical Configuration Audit (PCA) confirming hardware/software integration for fault-related components.
2. **Version Control Records**:

   * Logs showing version tracking and updates specific to fault detection and annunciation systems.
   * Mapping of specific releases to resolved defects in fault detection/annunciation features.

### 8.1.6 Operational Readiness Evidence

Supports the operational readiness of the fault detection and annunciation system for its intended environment.

1. **Simulation Results**:

   * Results from simulated mission scenarios covering normal operations, failure modes, degraded system conditions, and fault recovery.
   * Evidence that operators correctly interpreted annunciated faults and executed recovery procedures.
2. **Training Records**:

   * Documentation confirming personnel were trained to respond to annunciated faults. Demonstrates understanding of trigger thresholds, system responses, and recovery workflows.

### 8.1.7 General Metrics and Reporting Evidence

Metrics provide quantitative proof that the fault detection and annunciation system performs as intended and meets mission goals.

1. **System Performance Metrics**:

   * Response times for fault detection and annunciation during testing scenarios.
   * System uptime demonstrating fault handling reliability during critical mission phases.
2. **Defect Resolution Metrics**:

   * Trends showing closure of defects related to fault detection/annunciation functionality.
   * Evidence that defect correction does not degrade the fault handling system.
3. **Test Execution Metrics**:

   * Logs showing test coverage percentages for all fault-handling logic.
   * Details of faults tested across nominal, degraded, and boundary condition testing scenarios.

## 8.2 Specific Examples of Objective Evidence

1. **Design Evidence**:

   * Fault Detection System Block Diagram.
   * Annunciation Workflow Details (e.g., system priority levels for fault reporting).
2. **Testing Evidence**:

   * Fault injections successfully triggering warning lights and telemetry outputs.
   * Logs from autonomous recovery tests showing execution of fallback protocols.
3. **Safety Evidence**:

   * A Hazard Report tracing a CO₂ scrubber failure fault to recommended annunciation thresholds for crew notification.
4. **IV&V Evidence**:

   * Documentation of IV&V participation in test witnessing for fault response simulations where a critical pressure anomaly was detected and annunciated.
