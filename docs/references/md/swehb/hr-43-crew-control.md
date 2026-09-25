# HR-43 - Crew Control

> NASA Software Engineering Handbook (SWEHB Ver D), page id 171508219. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508219/HR-43+-+Crew+Control

HR-43 - Crew Control

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508219/HR-43+-+Crew+Control#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=171508219)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=171508219&showCommentArea=true&showComments=true#addcomment)

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

4.4.3 The space system shall provide the capability for humans to remotely monitor, operate, and control the crewed system elements and subsystems, where:

1. 1. The remote capability is necessary to execute the mission; or
   2. The remote capability would prevent a catastrophic event; or
   3. The remote capability would prevent an abort.

## 1.1 Notes

This capability is not intended to force 100 percent of communication coverage for all elements of the system. The communication coverage is planned to implement the capability to meet the three conditions.

For EVA suits, this capability does not mean that the EVA suit requires constant monitoring between EVAs (missions). If the suit is powered off and stowed, periodic checks or inspections may be all that is required.

## 1.2 History

Click here to view the history of this requirement: HR-43 History

HR-43 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.4.3 The space system shall provide the capability for humans to remotely monitor, operate, and control the crewed system elements and subsystems, where:  1. 1. The remote capability is necessary to execute the mission; or    2. The remote capability would prevent a catastrophic event; or    3. The remote capability would prevent an abort. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

This capability will likely be implemented using a mission control on Earth. Logically, there will be times when the crew is unavailable to monitor, operate, and control the system. If the crew vacates one element of the system or transfers to another Human-Rated system as part of the reference mission, there is a capability for humans to monitor the unoccupied elements. In some of these cases, the crew may be able to perform this function from their new location. In other cases, mission control may perform this function.

This requirement ensures that the crewed space system includes robust remote capabilities for monitoring, operating, and controlling system elements and subsystems, enabling human intervention outside of direct onboard control. Such capabilities are critical for ensuring mission success, achieving operational flexibility, mitigating risks during emergencies, and optimizing overall system performance while protecting human lives and preventing mission loss.

Human spaceflight involves inherently unpredictable and dynamic environments, where immediate human action—either onboard or remote—is often necessary to ensure safety and mission success. Providing remote capabilities for monitoring, operating, and controlling crewed systems:

1. Enhances mission resilience by enabling external intervention during emergencies or complex operations.
2. Ensures operational flexibility to reduce mission downtime or unnecessary aborts.
3. Augments onboard capabilities, allowing humans—whether on the ground or elsewhere in the mission ecosystem—to interact with crewed systems when onboard systems are inadequate, overloaded, or in distress.

This requirement aligns with NASA’s overarching safety, reliability, and risk mitigation goals, ensuring operational effectiveness and protecting human lives in space.

## 2.1. Criticality for Mission Success

Remote capabilities serve essential functions when onboard control is insufficient, unavailable, or impractical due to mission constraints:

* **Complex Missions:** Certain missions necessitate continuous remote interaction (e.g., deep-space missions, automated dockings, lunar or planetary surface operations). Human operators, either on Earth or within nearby spacecraft, must monitor and control systems remotely to ensure mission-critical tasks are executed reliably.
* **Extended Durations:** Long-duration missions may face unforeseen system anomalies or resource constraints. Remote capabilities enable offboard operators to assist with system adjustments, troubleshooting, and resource management, supporting mission continuity.
* **Distance Challenges:** For missions beyond Earth orbit, onboard personnel may require external remote capabilities to complement automated controls. For example, during surface operations, personnel on lunar or Martian ground stations might need remote control over orbital systems or rovers.

## 2.2. Safety Assurance

Catastrophic risks can arise from system failures or anomalies during a mission. Remote capabilities ensure a secondary control mechanism is available to mitigate life-threatening hazards and prevent mission loss:

* **Avoidance of Catastrophic Events:** If onboard control is compromised (e.g., due to hardware failure, software errors, or loss of crew awareness), remote operations allow immediate intervention, such as engaging emergency protocols, reconfiguring systems, or stabilizing critical subsystems to ensure continued spacecraft integrity.
* **Enhanced Situational Awareness:** Remote monitoring ensures that operators external to the crewed system (e.g., ground control or nearby spacecraft) can detect anomalies that might escape onboard crew attention, giving an additional layer of fault detection and response.

## 2.3. Prevention of Mission Abort

Ability to remotely intervene during certain operational phases can prevent aborting a mission unnecessarily:

* **System Anomaly Handling:** Remote control allows external operators to diagnose and resolve minor issues affecting crewed systems rather than initiating premature mission termination (e.g., addressing hardware malfunction, recalibrating faulty sensors, or reloading mission-critical software).
* **Operational Flexibility:** Aborts often result in costly, irreversible mission outcomes. Remote capabilities enhance operational flexibility by giving external operators the ability to stabilize systems, optimize trajectories, or resolve anomalies to avoid aborts and extend mission viability.

## 2.4 Operational Scenarios Justifying the Requirement

#### **Scenario 1: Remote Support for Crew During System Failures**

In a space environment, complex crewed systems may experience failures or degraded performance due to unforeseen conditions. Remote monitoring and intervention allow ground operators or remote crew teams to:

* Diagnose system anomalies based on telemetry.
* Execute control commands to stabilize or recover system states.
* Provide operational guidance to the onboard crew without the burden of manual troubleshooting during emergencies.

#### **Scenario 2: Mission Phases Requiring Remote Operations**

Certain mission phases inherently require remote-controlled operations due to constraints of onboard control capabilities:

* **Docking and Rendezvous:** Remote operators (ground-based teams or proximity crewed vehicles) may need to control subsystems to ensure precise alignment and safe docking.
* **Surface Operations:** Orbital assets supporting planetary exploration may require ground station operators to control or monitor subsystems remotely, such as landing or resource deployment.

#### **Scenario 3: Mitigating Time-Sensitive Aborts**

In cases where onboard systems initiate an abort, external remote capabilities allow ground control teams to take corrective measures:

* Overriding automatic abort sequences triggered by faulty sensor data.
* Reconfiguring systems to stabilize operations and allow continued mission execution.
* Resolving minor errors that would otherwise result in major mission setbacks.

## 2.5 Technical and Design Implications

This requirement introduces several design and technical considerations to ensure remote capabilities are reliable, safe, and integrable within the crewed space system:

### 2.5.1 Communication Infrastructure

Design must ensure robust communication channels between the remote operators and the crewed system:

* **Low-Latency Communications:** Especially necessary for missions operating near Earth orbit or lunar proximity.
* **High Reliability:** Redundancy in communication pathways (e.g., RF, optical links) to mitigate disruptions.
* **Bandwidth Management:** Support high telemetry rates to ensure external operators can monitor extensive system status and make informed decisions.

### 2.5.2 Remote Control Interfaces

Remote operators need intuitive, functional interfaces to monitor and control crewed system elements:

* **Telemetry Information:** Full access to real-time system data, health/status indicators, and anomaly alerts.
* **Control Authority:** Capability to execute control commands with clear system feedback loops.
* **Override Features:** Ability to intervene in automated processes safely and effectively.

### 2.5.3 Safety Considerations

Remote capabilities must include safeguards to prevent:

* **Erroneous Commands:** Mitigate risks of external operators issuing incorrect or conflicting commands that could endanger the mission or the crew.
* **Unauthorized Access:** Ensure strong encryption and authentication mechanisms to prevent cyber-attacks or accidental activation of remote control systems.
* **Catastrophic Failures:** Design systems to ensure remote commands cannot create hazardous conditions or escalate risks unintentionally.

### 2.5.4 Redundancy and Fault Tolerance

Remote capabilities should incorporate fail-over provisions:

* Ground systems need backup teams, control terminals, and simulations prepared for rapid responses during remote interventions.
* Satellite relays and distributed control systems should allow seamless transition of control during communication blackouts.

## 2.6 Lessons Learned

#### **Apollo 13 (1970): Remote Ground Support**

Following the oxygen tank explosion on Apollo 13, ground-based operators played a vital role in assisting the crew remotely:

* Guided the crew through reconfiguring power systems and life support manually to prevent catastrophe.
* Solved computational and procedural challenges that were beyond the immediate capability of onboard systems.

#### **Mars Rover Missions: Remote Operations**

Mars rover missions (e.g., Perseverance, Curiosity) demonstrate the criticality of remote control capabilities:

* Ground operations routinely issue remote commands to adjust trajectories, software behaviors, and power systems, ensuring mission success.

#### **ISS Ammonia Leak Detection (2015): Remote Monitoring**

Remote telemetry of the ISS cooling system helped operators assess potential ammonia leaks and provide guidance to the crew to prevent false alarms and mitigate risks.

# 3. Guidance

This guidance outlines the software engineering considerations and tasks to ensure that the crewed system meets these remote capability requirements, improving operational flexibility, safety, and mission reliability.

By implementing the tasks and considerations outlined below, the space system will achieve:

1. **Reliable Remote Operation and Monitoring:** Robust, fault-tolerant systems enabling safe remote control and intervention.
2. **Prevention of Abort and Catastrophic Events:** Remote systems will mitigate failure risks during both nominal and off-nominal conditions.
3. **Mission Success Assurance:** Support operational flexibility and mission continuity through seamless remote control integrations.

For further compliance, refer to **NPR 7150.2 (Software Engineering Requirements)** [083](#_tabs-<p></p>) and other applicable NASA standards. This ensures the system is well-engineered for remote capabilities, contributing to crew and mission safety.

## 3.1 Operational Context

* Remote capabilities are crucial during instances when the crew cannot directly monitor, operate, or control the system due to mission requirements or unforeseen events:
  + **Unoccupied Elements:** When crew vacates an element during the mission, they or ground operators must remotely monitor and operate it to maintain system integrity.
  + **System Redundancy:** When transitioning to another human-rated system (e.g., orbital vehicles, surface habitats), the ability to oversee and operate unoccupied systems remotely becomes critical for mission safety.
* Remote monitoring and control can be implemented through a **Mission Control Center (MCC)** on Earth or other locations, including support from other spacecraft or habitats.
* **Guidelines for Communication Coverage:**
  + While 100% communication coverage is not expected for all system elements at all times, sufficient coverage must exist to meet the three specified conditions (mission execution, catastrophic event prevention, and abort prevention).

## 3.2 System-Specific Use Case: EVA Suits

For **Extravehicular Activity (EVA) suits**, this requirement does not mandate continuous remote monitoring between EVA operations. If the suit is powered off and stowed, periodic checks (e.g., status inspections) may suffice. Remote tracking is critical only for periods of active operation or pre/post-mission diagnostics.

#### **References:**

* Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) **:** Provides further guidance on remote software requirements for human-rated systems.
* **NASA Spaceflight Human-System Standard, Volume 2 (NASA-STD-3001, Vol 2, Rev D)** [498](#_tabs-<p></p>) : Standards on the design of human-system interactions, such as displays for remote operators.

## 3.3 Software Engineering Tasks for Remote Capabilities

To meet this requirement, the following **software engineering tasks** should be implemented across the software lifecycle:

#### **3.3.1. Remote Monitoring Systems**

* Design and implement robust systems to enable **real-time remote monitoring** of system status, health, and performance.
  + Key data to include: subsystem statuses, resource levels, anomaly alerts, critical thresholds (e.g., temperature, pressure, power).
  + Provide configurable telemetry channels tailored for remote operator needs to ensure clarity and relevance.
  + Architect data redundancy (e.g., onboard and ground-station logs) to ensure no critical information is lost during communication blackouts.

**Success Criteria:**

* Full, real-time remote status visibility for mission-critical systems during active phases, with degraded but functional status reports for passive phases.

#### **3.3.2 Remote Operations and Control**

* Develop user-friendly but **secure remote operation interfaces** to allow remote execution of system commands and corrective actions to:

  1. Complete mission tasks (e.g., orbital adjustments, system reconfigurations).
  2. Manage off-nominal conditions (e.g., failover to redundant systems, anomaly corrections).
  3. Prevent catastrophic failures or unnecessary mission aborts.
* Follow **NASA Display Standards (Appendix F, NASA-STD-3001 Vol 2)** to create ergonomic and accessible Human-Machine Interfaces (HMI).
* Implement **secure command transmission protocols** with:

  + Authentication mechanisms (e.g., multi-factor authentication).
  + Encryption for command and telemetry data (compliance with **NASA-STD-1006, Space System Protection Standard**). [361](#_tabs-<p></p>)

#### **3.3.3 Redundancy and Fault Tolerance**

* Incorporate redundancy in hardware/software systems for remote control loops:
  + **Backup communication channels** (e.g., RF relays, optical links).
  + Redundant remote control systems to maintain operation even after faults in primary systems.
* Implement self-repairing capabilities (e.g., automated error correction mechanisms) to maintain availability of remote capabilities during faults.

#### **3.3.4 Error Handling and Recovery**

* Design error-handling mechanisms that enable remote operators to:
  1. Detect anomalies in real-time through alerts and logs.
  2. Mitigate and recover system operations safely (e.g., initiate safe shutdowns, restart failed components via remote commands).

#### **3.3.5 Cybersecurity**

* Implement strong cybersecurity measures to ensure remote systems cannot be accessed or controlled by unauthorized entities:
  + **Regular security assessments** and penetration testing.
  + Ensure compliance with **NASA-STD-1006** for mitigating the risk of cyber vulnerabilities.

#### **3.3.6 Independent Verification and Validation (IV&V)**

* Conduct IV&V activities focusing on:
  1. Accuracy of remote monitoring data under both nominal and off-nominal conditions.
  2. Remote control system integrity for critical functions (e.g., safety-critical overrides).
  3. Simulations of operator-driven commands under mission scenarios.
* Ensure IV&V participation during design reviews, testing cycles, and change analyses.

#### **3.3.7 Simulation and Testing**

* Simulate a comprehensive set of **nominal and off-nominal scenarios**, including:
  + Loss of onboard control modes requiring remote recovery.
  + Fault injection tests to assess error-handling under remote operation.
  + Abnormal mission conditions requiring EVA or module detachment monitoring.
* Test protocols must address boundary conditions (e.g., extreme latencies, lossy communication links) and ensure no single-point-of-failure scenarios can result in catastrophic system loss.

#### **3.3.8 Code Coverage and Safety Testing**

* Achieve **100% Modified Condition/Decision Coverage (MC/DC)** for safety-critical software related to remote operation and control.
* Verify that remote systems function seamlessly with onboard systems under all defined operational conditions.

#### **3.3.9 Configuration Management and Traceability**

* Maintain **rigorous configuration management** to ensure remote system software is consistent with onboard versions.
* Use bidirectional traceability to track all remote capability requirements:
  + From high-level mission objectives.
  + Down through hazards, designs, source code, and verification tests.

#### **3.3.10 Training and Documentation**

* Develop comprehensive training programs and **remote operations manuals** for:
  1. Ground operators to ensure familiarity with the system's remote interfaces, error-handling commands, and contingency protocols.
  2. Crew in scenarios where onboard systems require remote troubleshooting support.

**Manuals** should include:

* Contingency command workflows for anomaly resolution.
* Troubleshooting checklists for cascading system failures.
* Scenarios for transitioning between automated, onboard, and remote operations.

#### **3.3.11 Audits and Assessments**

* Perform regular audits to:
  + Verify compliance with **NASA-STD-8739.8, Software Assurance and Safety Standard**. [278](#_tabs-<p></p>)
  + Ensure that remote capabilities’ performance meets mission-critical requirements.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)       * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

For small projects, the implementation, verification, and management of this requirement must be appropriately scaled to the project's complexity, size, and resource constraints while ensuring safety and compliance with critical standards. Below is tailored guidance to support small teams and projects in addressing this requirement.

For small projects, the implementation of remote capabilities can be achieved by focusing on **critical needs**, utilizing simple tools, reducing complexity, and leveraging commercially available or open-source frameworks. The goal is to deliver effective, safe, and sustainable remote-control functionality while avoiding unnecessary overhead. Careful prioritization of tasks, rigorous yet scaled-down validation/testing, and minimized but clear interfaces and documentation form the foundation of success.

## 4.1 Key Considerations for Small Projects

1. **Focus on Critical Functions:**

   * Prioritize remote monitoring, operations, and control capabilities related to mission-critical systems (e.g., life support, power, propulsion).
   * Scale implementations to the minimum viable feature set that ensures compliance with the requirement.
2. **Leverage Existing Tools and Frameworks:**

   * Utilize off-the-shelf software, libraries, and communication tools where possible to reduce development costs and testing effort.
   * Explore open-source frameworks for telemetry, ground control, and remote monitoring to speed up development.
3. **Simplicity in Design:**

   * Avoid overly intricate architectures. Design simple, modular solutions that allow for remote access and control of critical subsystems.
   * Use straightforward user interfaces to ensure usability and minimize human error during remote operation.
4. **Risk Awareness and Mitigation:**

   * Conduct a focused analysis to identify failure scenarios most relevant to your project and mitigate risks effectively.

## 4.2 Small Project Software Engineering Tasks

To meet the requirements efficiently, focus on the following high-priority tasks:

### 4.2.1 Define Requirements and Use Cases

* **Document Minimal Success Criteria:**
  + Define the critical elements of the system to be monitored and controlled remotely (e.g., environmental monitoring, mode changes, abort initiation).
  + Clearly specify when remote capability is required (under what conditions: mission execution, anomaly, or abort scenarios).
* **Create Key Scenarios:**
  + Nominal operations (e.g., regular subsystem monitoring).
  + Off-nominal responses (e.g., remote activation of failsafe protocols during system faults).

**Examples of Metrics:**

* List of critical telemetry parameters (e.g., temperature, pressure, voltage).
* Flow diagrams summarizing remote intervention scenarios for small subsystems.

### 4.2.2 Establish Remote Monitoring Capabilities

* **Scope:** Build or integrate basic telemetry systems to provide **status and health data** of critical subsystems.
* **Low-Cost Implementation Options:**
  + Select an open-source or low-cost telemetry data system (e.g., COSMOS, MQTT for lightweight message exchanges).
  + Implement web-based or simple console dashboards for real-time operator monitoring.
* **Telemetry Design Guidelines:**
  + Ensure reliable data formatting (e.g., JSON or XML-based for compatibility).
  + Develop a priority-based alert mechanism for off-nominal events.

**Practical Tips:**

* For very small projects, a cloud-based IoT infrastructure (e.g., AWS, Azure, or Google Cloud with IoT/telemetry features) may reduce setup complexity and costs.

### 4.2.3 Enable Remote Operations and Control

* **Scope:** Design basic remote-control logic for mission-critical actions:
  + Safe mode activation.
  + Abort sequence override or initiation.
  + Power adjustments for uncrewed elements.
* **Simplified Operability:**
  + Implement straightforward commands with acknowledgment protocols (e.g., “command-receipt-execute” feedback loop).
  + Focus on remote command reliability rather than high-frequency capabilities.
* **User Interface:**
  + Develop a simple user interface (UI), such as web-based dashboards or terminal interfaces, that allows remote operators to select and execute predefined commands.

**Examples of Tasks:**

* Use lightweight frameworks (e.g., Flask for web-based interfaces with buttons/sliders).
* Implement role-based authorization for issuing critical remote commands.

### 4.2.4 Implement Cybersecurity for Scalability

* Minimize cybersecurity risks by adopting NASA-recommended practices:
  + Use TLS (Transport Layer Security) for command and telemetry data.
  + Implement basic multi-factor authentication (MFA) for accessing remote control interfaces.
  + Source tools compliant with **NASA-STD-1006 Space System Protection Standard**.

**Simplified Tools for Small Scale:**

* Secure Shell (SSH) tunnels for remote communication.
* API Gateways with manual failover features for secure and controlled access.

### 4.2.5 Test and Validate Remote Capabilities

Perform scaled-down but effective testing:

* **Simulation Testing:**
  + Use small-scale hardware-in-the-loop (HIL) setups to simulate remote command impacts under nominal and failure conditions.
  + Test latency and robustness in common failure scenarios (e.g., network or computation delays).
* **Verification Tasks:**
  + Ensure basic redundancy in command paths to mitigate single points of failure.
  + Achieve minimal-but-sufficient code coverage (Modified Condition/Decision Coverage, or MC/DC, for critical logic).

**Tools:**

* Open-source testing tools like Jenkins for automation or simulation environments like Gazebo for simple scenarios.

### 4.2.6 Maintain Effective Configuration Management

* Maintain a lightweight configuration management system:
  + Track changes to software, test cases, and telemetry parameters using basic tools like GitHub or GitLab.
  + Document all configurations in plain language and ensure operators have real-time access to the latest versions.

### 4.2.7 Develop Lightweight Training and Documentation

* Provide **focus-based training** to operators:
  + How to interpret telemetry data and respond to alerts.
  + How to execute time-sensitive commands via the remote interface.
* Deliver minimal but clear user manuals with:
  + Step-by-step troubleshooting guides.
  + Emergency response procedures (e.g., for communication disruptions or subsystem malfunctions).

## 4.3 Key System Features for Small Projects

Here are the minimum deliverables to achieve compliance with this requirement within a small project:

#### **Telemetry and Monitoring**

* Collection and remote access to health/status data of critical system parameters (e.g., environmental control, power status).
* A simple, prioritized alerting system for anomalies (e.g., flashing alerts on the dashboard).

#### **Remote Command Execution**

* A mechanism to send and receive critical commands to the spacecraft’s subsystems (e.g., turning subsystems on/off, abort activation).
* Simple feedback to confirm command execution (acknowledgment messages or notifications).

#### **Cybersecurity**

* Basic protections such as encryption and authentication for telemetry and command data.

#### **Error Handling and Recovery**

* Implement predefined recovery procedures triggered by ground commands for common off-nominal scenarios (e.g., subsystem resets).

#### **Testing**

* Results from small-scale simulation or hardware testing covering nominal and at least one off-nominal scenario.

## 4.4 Reduced Scope Example: Small Unpressurized Payload System

Imagine a small satellite or unpressurized payload designed to monitor environmental data.

1. **Telemetry Scope:**
   * Monitor temperature, battery level, data transmissions.
2. **Operational Capability:**
   * Remotely reboot the payload, initiate data collection, or power down the system.
3. **Testing:**
   * Simulate communication outages and measure telemetry/command resilience.
4. **Cybersecurity:**
   * Use basic encryption and authentication for communication.
5. **User Interface:**
   * A simple web-based interface for displaying data and issuing basic commands (e.g., "Reboot System").

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-361)

  [SPACE SYSTEM PROTECTION STANDARD](https://standards.nasa.gov/standard/NASA/NASA-STD-1006 "Click to open in new window")

   NASA-STD-1006A, Approved 7/15/2022,  PUBLIC: Upload Publicly Available Standard
  https://standards.nasa.gov/sites/default/files/standards/NASA/A/0/2022-07-15-NASA-STD-1006A-Approved.pdf
* (SWEREF-458)

  [NASA Technical Requirements for Human-Rating](https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/0/NASA-STD-871929-Baseline-draft.pdf "Click to open in new window")

  NASA-STD-8719.29, National Aeronautics and Space Administration, Approved:2023-12-11 Baseline,  This standard establishes technical requirements necessary to produce human-rated space
  systems that protect the safety of the crew and passengers on NASA space missions
* (SWEREF-498)

  [NASA Space Flight Human-System Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-3001-vol-2 "Click to open in new window")

  NASA-STD\_3001, Volume 2: Human Factors, Habitability, and Environmental Health, Revision A, 2015.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA has a long history of valuable lessons learned from remote operations, monitoring, and control that highlight the importance of implementing and verifying this requirement. These lessons are based on numerous space missions that have faced challenges and successes with remote systems, and they provide critical insights into planning, design, and testing.

---

### **Key Lessons Learned**

#### **1. Apollo 13 - Remote Support Saved the Mission**

**LLIS Reference:** Apollo Program Lessons Learned (LLIS-2504)

* **Overview:** During the Apollo 13 mission, a catastrophic failure (an oxygen tank explosion) required the crew to rely on ground controllers for diagnosing the failure, managing power resources, and assisting with life support systems reconfiguration.
* **Lesson:** Remote monitoring and control capabilities are critical for assisting the crew during unforeseen anomalies. Ground control’s ability to analyze telemetry data played a key role in helping the crew develop and execute workarounds to ensure safe mission completion.
* **Relevance to Requirement 4.4.3:** This lesson reinforces the need for robust remote telemetry and control capabilities to assist in preventing catastrophic events or aiding in recovery from failures.

---

#### **2. ISS Ammonia Leak Detection – Remote Anomaly Analysis**

**LLIS Reference:** Systems Engineering Management of the ISS Program (LLIS-4932)

* **Overview:** In 2015, the International Space Station (ISS) triggered a false alarm about ammonia leaks in its cooling system. The ground controllers analyzed telemetry remotely and determined that there was no actual leak, allowing the crew to bypass unnecessary and potentially disruptive emergency protocols.
* **Lesson:** False alarms from on-board systems can lead to unnecessary or costly responses. Remote monitoring by ground controllers can verify whether an anomaly requires action, thereby avoiding future unintended aborts or interruptions.
* **Relevance to Requirement 4.4.3:** This emphasizes the need for real-time remote telemetry and diagnostic capabilities to prevent false positives that may lead to mission aborts or delays.

---

#### **3. Mars Exploration Rovers – Remote Contingency Planning**

**LLIS Reference:** Mars Rovers Design Lessons (LLIS-2507)

* **Overview:** NASA’s Mars rovers (Spirit, Opportunity, and more recently Perseverance) relied on extensive remote operations to perform tasks, diagnose issues, and recover from anomalies. For example:
  + Spirit’s stuck wheel was resolved by remote algorithms.
  + Opportunity recovered from a memory corruption issue due to remote software uploads.
* **Lesson:** Remote systems benefit from built-in autonomy but must always leave room for remote human intervention to adapt to unexpected scenarios. Implementing recovery procedures remotely can prevent mission losses and ensure continued operations under degraded conditions.
* **Relevance to Requirement 4.4.3:** Remotely operating critical systems provides flexibility during anomalies, allowing humans to intervene and reconfigure systems to prevent catastrophic outcomes or mission failures.

---

#### **4. Skylab Program – Spacecraft “Rescue Operations”**

**LLIS Reference:** Skylab Program Lessons Learned (LLIS-0569)

* **Overview:** Skylab encountered several early mission issues, including damage to its meteoroid shield and solar array during launch. Remote teams designed and tested repair procedures and worked with the astronauts to deploy a sunshield and adjust system configurations.
* **Lesson:** Crew and ground-based remote intervention can be used synergistically when real-time in-situ solutions are required. Collaboration between the crew and ground controllers allowed quick troubleshooting and problem solving.
* **Relevance to Requirement 4.4.3:** Systems must enable seamless communication and control by ground-based operators for manual recovery in complex scenarios that are critical to mission sustainability.

---

#### **5. James Webb Space Telescope (JWST) – Remote Deployment Tests**

**LLIS Reference:** JWST Program Lessons (no LLIS citation; program publications)

* **Overview:** JWST required precise, remotely conducted deployment of its mirrors, sunshield, and calibration systems post-launch. Extensive pre-mission simulations were performed to test remote operability and identify potential challenges.
* **Lesson:** Remote control systems, particularly those used for high-stakes missions, must be rigorously simulated and validated for complex operations in advance. This involves testing under both nominal and off-nominal conditions to ensure operational reliability.
* **Relevance to Requirement 4.4.3:** Advanced simulation and testing of remote capabilities protect systems from failure during high-risk scenarios like deployment or configuration adjustments.

---

#### **6. Hubble Space Telescope (HST) – On-orbit Repair and Servicing**

**LLIS Reference:** Hubble Space Telescope Servicing Missions (LLIS-1717)

* **Overview:** The Hubble Space Telescope required multiple servicing missions to correct issues (e.g., initial lens defect) and upgrade technology. Remote capabilities allowed ground teams to monitor HST telemetry and design corrective processes even after launch.
* **Lesson:** Continuous telemetry access and well-designed remote operational interfaces allow extensive post-deployment servicing options, reducing the risk of hardware failures jeopardizing the entire mission.
* **Relevance to Requirement 4.4.3:** Remote capabilities give missions longevity and adaptability, reducing operational risks and preventing mission failure.

---

#### **7. Columbia Accident Investigation Board (CAIB) Report**

**LLIS Reference:** Lessons from STS-107 Columbia Loss (CAIB Final Report)

* **Overview:** The Columbia disaster highlighted the risk of failing to fully utilize remote monitoring data. Engineers on the ground detected and analyzed data that could have predicted the wing damage, but decision-making was limited due to communication and procedural gaps.
* **Lesson:** Fully implementing and acting on remote monitoring systems in real-time is vital to provide actionable data that can inform decisions and prevent catastrophic events.
* **Relevance to Requirement 4.4.3:** Remote monitoring systems must be paired with robust decision-making frameworks to ensure that anomalies are identified and addressed proactively.

---

#### **8. Mars Climate Orbiter (MCO) – Communication and Navigation Risks**

**LLIS Reference:** Mars Climate Orbiter Mishap Investigation Board (LLIS-0337)

* **Overview:** A unit mismatch between metric and imperial systems caused the spacecraft to enter a hazardous atmosphere, resulting in mission failure. The anomaly could have been detected and corrected remotely if better telemetry and validation systems had been in place.
* **Lesson:** Remote systems must have robust validation and monitoring mechanisms to verify all calculations, commands, and subsystems. Humans in remote operation centers must confirm system data for early anomaly detection.
* **Relevance to Requirement 4.4.3:** Remote monitoring must include cross-checks, validation, and confirmation to prevent errors that could lead to catastrophic mission outcomes.

---

#### **9. Artemis I Lessons – Remote Monitoring of Uncrewed Systems**

**LLIS Reference:** Artemis Program Development Lessons (no LLIS citation; mission planning reports)

* **Overview:** During Artemis I, extensive ground control systems were developed to monitor and operate the uncrewed systems in the Orion spacecraft. Telemetry analysis ensured smooth transition between mission phases and early detection of anomalies.
* **Lesson:** Even autonomous systems benefit greatly from human-monitored remote capabilities, particularly for preventing abort scenarios during unexpected transitions.
* **Relevance to Requirement 4.4.3:** Implementing reliable telemetry to allow intervention, even in autonomous systems, ensures mission sustainability.

---

### **Summary of Lessons and Their Application**

| **Lesson** | **Key Takeaway** | **Relevance to Requirement 4.4.3** |
| --- | --- | --- |
| Apollo 13 Emergency Operations | Remote monitoring enables recovery from failure and avoids catastrophic events. | Monitor critical system elements for anomaly detection and command response. |
| ISS Ammonia Leak Analysis | Remote verification prevents false alarms from disrupting operations. | Ensure telemetry systems can accurately validate anomalies. |
| Mars Rover Remote Operations | Remote control ensures operational flexibility during anomalies. | Allow remote reconfiguration to recover from off-nominal conditions. |
| Skylab Repairs | Ground and crew collaboration prevents mission failure. | Enable integrated remote and crew control for complex scenarios. |
| James Webb Telescope Simulation | Pre-validated remote operations ensure deployment success. | Test remote capability in nominal and boundary conditions pre-deployment. |
| Hubble Space Telescope Servicing | Telemetry enables post-launch calibration and longevity. | Allow for maintenance and upgrades via remote intervention. |
| Columbia Analysis (CAIB) Results | Fully utilize remote monitoring during anomalous conditions. | Build frameworks for anomaly detection and clarity in remote decision-making. |

Through these lessons, NASA has demonstrated that robust **remote monitoring, operation, and control systems** are vital to ensure mission success, enhance adaptability, and protect assets and safety.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-43 - Crew Control**

4.4.3 The space system shall provide the capability for humans to remotely monitor, operate, and control the crewed system elements and subsystems, where:

1. 1. The remote capability is necessary to execute the mission; or
   2. The remote capability would prevent a catastrophic event; or
   3. The remote capability would prevent an abort.

By implementing these improved Software Assurance plans, NASA can ensure the space system’s capabilities for remote monitoring, operation, and control are robust, safe, and mission-ready. This guidance emphasizes traceability, metrics, simulation testing, and risk management to protect crew safety and mission objectives.

## 7.1 Tasking for Software Assurance

1. Ensure the development, implementation, and testing of robust control algorithms capable of managing critical functions with crew control. These algorithms must undergo thorough testing to guarantee their reliability and safety in all operational scenarios.
2. Ensure redundancy and fault tolerance are included in the design to ensure that critical functions can continue to operate autonomously or operators can remotely monitor, operate, and control the crewed system elements and subsystems, even in the presence of faults or failures. This includes implementing backup systems and failover mechanisms.
3. Ensure that Integrated real-time monitoring and diagnostic tools are used to continuously assess the health and status of critical systems and subsystems. These tools should detect anomalies and trigger autonomous responses to mitigate potential catastrophic events and alert the operators and crew of the situation for potential intervention.
4. Employ safety analysis techniques such as [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) and [8.05 - Software Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) to identify potential hazards and failure modes. This helps in designing controls and mitigations for the operators to remotely monitor, operate, and control the crewed system elements and subsystems.
5. Ensure extensive simulations and testing to verify that the operators can remotely monitor, operate, and control the crewed system elements and subsystems under various conditions, including nominal and off-nominal scenarios. This includes testing for unexpected situations and boundary conditions.
6. Confirm that strict configuration management to ensure that the correct software versions and configurations are used. This reduces the risk of errors due to incorrect or inconsistent configurations that could impact remote operations.
7. Ensure robust error handling and recovery mechanisms to address errors stemming from detected faults. This ensures that error handling is adequate and that the system may be accessed remotely to allow recovery from errors without leading to hazardous or catastrophic events.
8. Confirm strong cybersecurity measures are implemented to protect the remote monitoring and control systems from unauthorized access and cyber threats. This includes performing cybersecurity assessments and implementing protections as per **NASA-STD-1006, Space System Protection Standard** [361](#_tabs-<p></p>) .
9. Perform safety reviews on all software changes and software defects.
10. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.
11. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically that the operators can remotely monitor, operate, and control the crewed system elements and subsystems under various conditions, including nominal and off-nominal scenarios. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks). Ensure that the project has developed and executed test cases to test the software system’s recovery from faults via remote operations.
12. Analyze the software test procedures for the following:
    1. Coverage of the software requirements.
    2. Acceptance or pass/fail criteria,
    3. The inclusion of operational and off-nominal conditions, including boundary conditions,
    4. Requirements coverage and hazards per [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) and [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), respectively.
13. Perform test witnessing for safety-critical software to ensure that the operators can remotely monitor, operate, and control the crewed system elements and subsystems under various conditions, including nominal and off-nominal scenarios.
14. Confirm that test results are sufficient verification artifacts for the hazard reports.
15. Ensure comprehensive training and documentation for operators is available.

## 7.2 Software Assurance Products

This guidance focuses on software assurance (SA) activities, tasks, products, and metrics necessary to ensure the space system complies with the requirement, providing robust and safe remote monitoring, operation, and control capabilities while preventing catastrophic events and mission aborts. It incorporates streamlined processes, actionable steps, and visual traceability designed for mission-critical software.

To address this requirement, the following software assurance products should be developed, reviewed, maintained, and validated:

### 7.2.1 System Design Visibility

1. **System Design Analysis**:

   * Provide evidence that the system design includes remote monitoring, operation, and control capabilities for nominal and off-nominal scenarios.
   * Include system architecture diagrams showing telemetry, remote interfaces, communication configurations, and fail-safe mechanisms.
2. **Software Design Documentation**:

   * Analyze how the crewed system software enables remote monitoring and control functions under various conditions, including decomposition of functional behaviors (e.g., monitoring health status, command execution).
   * Ensure software design is modularized to isolate safety-critical components, allowing redundancy and fault-tolerant controls.

### 7.2.2 Safety Assurance Products

1. **Completed Hazard Analyses and Reports**:

   * Develop hazard analyses for remote operations, identifying potential faults (e.g., communication loss, command delays) and any cascading impact on mission systems.
   * Include failure propagation analyses, control strategies, and mitigation mechanisms to address potential risks.
2. **Software Safety Analysis**:

   * Perform in-depth **Software Fault Tree Analysis (FTA)** to trace faults and hazards impacting remote capabilities.
   * Conduct **Software Failure Modes and Effects Analysis (FMEA)** to identify software failure modes (e.g., failure in telemetry updates or command validation) and their impacts on overall mission safety.

### 7.2.3 Testing and Verification

1. **Functional Configuration Audit (FCA) and Physical Configuration Audit (PCA)**:

   * Complete FCA to confirm that all remote monitoring and control functions align with requirements and interfaces.
   * Conduct PCA to ensure that physical software artifacts (source code, logs, design documents) meet technical specifications.
2. **Test Results and Analysis**:

   * Deliver and evaluate test results for remote monitoring, operation, and control, including:
     + Automated test tool outputs (e.g., code coverage and static analysis metrics).
     + Validation of fail-safe behaviors during communication loss or remote command anomalies.
   * Incorporate both simulation-based testing and live hardware-in-the-loop (HIL) testing.
3. **SWE Work Product Assessments**:

   * Complete assessments for the **Software Test Plan**, **Software Test Procedures**, **Software Test Reports**, and **User Manuals** to verify traceability and alignment with mission safety and operational goals.

### 7.2.4 Tools and Artifacts

1. **Automated Analysis Results**:

   * Use automated tools for:
     + **Static Code Analysis (SCA):** Detect potential vulnerabilities, safety-critical weaknesses, and coding errors.
     + **Dynamic Analysis:** Evaluate remote system performance and fault tolerance under simulated real-time conditions.
     + **Code Coverage Analysis:** Ensure Modified Condition/Decision Coverage (MC/DC) for all safety-critical software.
2. **Audit Reports**:

   * Produce post-review audit reports for SA reviews, peer inspections, and system-wide assessments to ensure adherence to safety-critical compliance standards.

## 7.3 Metrics

### 7.3.1 Verification and Validation Metrics

1. **Test Coverage:**

   * Ensure all nominal and off-nominal scenarios for remote monitoring, operation, and control are fully tested, including operational failures, hardware/software faults, and recovery protocols.
   * Measure coverage for edge cases, including latency under extreme loads and communication disruptions.
2. **Defect Density:**

   * Identify the number of defects per thousand lines of code (KLoC) during testing to track software robustness.
3. **Requirements Traceability:**

   * Verify all remote operation requirements are traced to system functions, software components, and test artifacts.

### 7.3.2 Safety Metrics

1. **Hazard Mitigation Verification:**

   * Track the percentage of hazards mitigated through software controls, including hazards resulting from remote operations.
2. **Safety-critical Requirements Compliance:**

   * Measure compliance with NASA-STD-8739.8, verifying all safety-critical functions for remote monitoring, operation, and control.

### 7.3.3 Quality Metrics

1. **Cyclomatic Complexity:**

   * Measure and review software complexity to ensure it is maintainable and adheres to safety-critical coding standards.
2. **Code Churn:**

   * Monitor code modifications and identify modules with frequent changes to prioritize additional testing efforts.

### 7.3.4 Performance Metrics

1. **Response Time:**

   * Track system latency between remote command issuance and execution to ensure suitable response times during mission-critical moments.
2. **System Uptime:**

   * Measure the percentage of time the system remains operational and responsive to remote commands.

### 7.3.5 Configuration Management Metrics

1. **Version Control Accuracy:**

   * Verify consistency in tracked versions of remote capability software artifacts over development and testing phases.
2. **Change Requests:**

   * Identify the impact of changes on overall system safety and mission schedule adherence.

### 7.3.6 Training Metrics

1. **Training Completion:**
   * Monitor completion rates for personnel training related to software use, remote operation procedures, and troubleshooting.

### 7.3.7 Independent Verification and Validation Metrics

1. **IV&V Analysis Results:**
   * Track completion rates for IV&V reviews on safety-critical functions for remote capabilities.
2. **IV&V Test Coverage:**
   * Ensure IV&V validation includes all identified failure modes and mission-critical operations.

### 7.3.8 Cybersecurity Metrics

1. **Cybersecurity Risks Identified:**
   * Track open and resolved cybersecurity risks to monitor progress in mitigating vulnerabilities.
2. **Mitigation Effectiveness:**
   * Evaluate the success rate of implemented controls for detected cybersecurity risks.

## 7.4 Examples of SA Metrics for Tracking

| Metric | Description |
| --- | --- |
| **# of Catastrophic Hazards Identified and Mitigated** | Tracks hazards related to remote operations to ensure safety-critical compliance. |
| **% of Code Coverage for Safety-critical Components** | Monitors MC/DC for remote monitoring and operation software. |
| **Defect Trend Analysis** | Monitors trends in detected defects (e.g., static code errors, dynamic failures). |
| **# of Safety-related Non-Conformances Resolved** | Tracks closure rate for non-conformances tied to safety-critical requirements. |
| **Performance Latency Metrics** | Measures command execution time to assess responsiveness for remote operation scenarios. |
| **Training Completion Ratios** | Ensures all operators are trained and capable of performing remote operations safely and effectively. |

## 7.5 Guidance

To ensure comprehensive software assurance for remote monitoring and control capabilities, implement the following steps:

#### **Remote Monitoring**

* Design real-time remote monitoring systems that prioritize:
  + Health and status telemetry updates.
  + Early anomaly detection via alert thresholds.
* Verify the functionality by testing against simulated off-nominal conditions.

#### **Remote Operation Interfaces**

* Develop and secure interfaces for remote operations, following NASA-STD-1006 and NASA cybersecurity guidance.
* Test interfaces for usability and operator accessibility under mission conditions.

#### **Simulation and Testing**

* Conduct simulations to test the system’s ability to handle:
  + Communication loss scenarios.
  + Cascading fault conditions during remote operations and software recovery.
* Document test results and track trends in failure rates and recovery success.

#### **Safety Reviews and SA Validation**

* Validate remote operations safety-critical functions using fault detection and isolation protocols.
* Perform peer reviews for all changes or updates affecting remote monitoring and control components.

#### **Documentation and Training**

* Develop specialized documentation (e.g., User Manuals, Operator Guides) for operators, including procedures for handling anomalies and failures.

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)       * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.22 - Space Security: Best Practices Guide](/spaces/SWEHBVD/pages/146540183/7.22+-+Space+Security+Best+Practices+Guide) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.12 - Basics of Software Auditing](/spaces/SWEHBVD/pages/102695731/8.12+-+Basics+of+Software+Auditing) * [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence is critical for demonstrating compliance with this requirement. It consists of verifiable artifacts, analyses, test results, and other work products that provide proof that the system meets the required capabilities for remote monitoring, operation, and control under both nominal and off-nominal conditions.

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

Objective evidence such as system design documents, test results, safety analyses, and verification metrics provides comprehensive, traceable proof that the system meets the specified requirement for remote monitoring, operation, and control. By integrating strong practices in testing, IV&V, and operational preparation, teams can ensure safety, reliability, and mission success.

## **8.1 Categories of Objective Evidence**

The following categories of evidence ensure thorough verification and validation of the requirement:

### 8.1.1 System Design Evidence

Objective: Confirm that the system design supports remote monitoring, operation, and control capabilities.

* **Architecture Diagrams**:

  + **Evidence:** System architecture diagrams showing the inclusion of components for telemetry, remote data transmission, command reception, and fault-tolerant pathways.
  + **Verification Method:** Review and trace architecture components to key requirements.
* **System Decomposition**:

  + **Evidence:** Functional decomposition showing how system-level requirements (e.g., remote operation) are allocated to software or hardware components.
  + **Verification Method:** Standards-based design review (e.g., according to NASA-STD-1006, Space System Protection Standard).
* **Communication Design Analysis**:

  + **Evidence:** Layered communication protocols and redundancy designs to ensure commands and telemetry data can be reliably transmitted and received.
  + **Verification Method:** Ensure design includes fault-handling mechanisms (e.g., alternative communication channels, cyclic redundancy checks).
* **Interface Definitions**:

  + **Evidence:** Detailed Interface Control Documents (ICDs) and specifications for human-machine interfaces (HMI) used by remote operators.
  + **Verification Method:** Verify the completeness of HMI designs to ensure they include controls, feedback loops, and usability testing results (in compliance with NASA-STD-3001 Vol. 2).

### 8.1.2 Software Requirements Evidence

Objective: Show that software requirements specify capabilities for remote monitoring, operation, and control, including safety-critical functions.

* **Requirements Document**:

  + **Evidence:** Software Requirements Specification (SRS) with explicitly stated requirements for:
    - Remote telemetry.
    - Remote command execution.
    - Error detection and reporting.
    - Fault recovery and redundancy.
  + **Verification Method:** Traceability matrix linking each requirement to system-level capabilities and corresponding tests.
* **Requirements Coverage Metrics**:

  + **Evidence:** Requirements traceability and coverage completion statistics showing 100% traceability between remote operation requirements and test cases.
  + **Verification Method:** Automated or manual traceability reviews.

### 8.1.3 Software Design Evidence

Objective: Ensure the software is designed to enable human operators to monitor and control the system remotely under all conditions.

* **Software Design Document (SDD)**:

  + **Evidence:** Detailed software design demonstrating how the system enables remote interaction, fault tolerance, and error handling on a functional/module level.
  + **Verification Method:** Completeness review aligned with applicable standards (e.g., NPR 7150.2, NASA Software Engineering Requirements).
* **Component Mapping**:

  + **Evidence:** Diagrams or descriptive mappings of critical software components responsible for telemetry, command handling, and fault management.
  + **Verification Method:** Peer review or structured technical inspection for completeness and correctness.

### 8.1.4 Hazard and Safety Analyses

Objective: Identify and mitigate risks associated with system faults and failure modes related to remote operations.

* **Hazard Analyses**:

  + **Evidence:** Completed hazard analysis reports detailing:
    - Failure scenarios linked to remote monitoring and control (e.g., loss of telemetry, delayed command response).
    - Risk mitigations integrated into software and system design.
  + **Verification Method:** Cross-check hazard controls with identified hazards using bi-directional traceability.
* **FTA and FMEA Results**:

  + **Evidence:** Completed Software Fault Tree Analysis (FTA) and Failure Modes and Effects Analysis (FMEA) specific to remote operations, highlighting critical safety mitigations.
  + **Verification Method:** Independent Verification and Validation (IV&V) review of analysis outputs.

### 8.1.5 Test Evidence

Objective: Demonstrate that the system meets requirements through verification testing in nominal and off-nominal conditions.

* **Test Plans, Procedures, and Reports**:

  + **Evidence:**
    - Approved Software Test Plan describing remote capabilities to be tested under normal, degraded, and failure scenarios.
    - Test procedures showing step-by-step processes for validating remote monitoring, operation, and control.
    - Test reports documenting results of all test cases, including success rates and anomalies.
  + **Verification Method:** Ensure 100% execution of test procedures and trace results to requirements.
* **Test Cases and Coverage Results**:

  + **Evidence:**
    - Test cases targeting safety-critical remote capabilities, including:
      * Fault detection and reporting.
      * Failover procedures for communication loss.
      * Recovery from invalid or failed commands.
    - Code coverage metrics (e.g., Modified Condition/Decision Coverage) for all path executions in remote control software.
  + **Verification Method:** Analyze test case results and coverage data against predetermined thresholds.
* **Simulation Evidence**:

  + **Evidence:** Results from simulations mimicking system operation under nominal and degraded conditions. Examples include:
    - Communication latency testing.
    - Multi-fault scenarios.
    - Interrupted remote telemetry cases verifying reconnection or failover mechanisms.
  + **Verification Method:** Validate simulation results against pre-defined success criteria.

### 8.1.6 Cybersecurity Validation Evidence

Objective: Ensure remote monitoring and control systems are secure from unauthorized access or harm.

* **Vulnerability Assessment Results**:

  + **Evidence:** Results of static/dynamic security scans showing no high-severity vulnerabilities in safety-critical components.
  + **Verification Method:** Use NASA-STD-1006 requirements to evaluate and mitigate risks based on output from automated tools.
* **Cybersecurity Mitigation Testing**:

  + **Evidence:** Test results for implemented cybersecurity controls, such as:
    - Authentication and encryption mechanisms.
    - Secure transmission and failure recovery mechanisms.
  + **Verification Method:** Ensure outputs demonstrate mitigated risks identified in cybersecurity assessments.

### 8.1.7 Configuration Management Evidence

Objective: Demonstrate strict version control and management for remote operation systems.

* **CM Reports**:
  + **Evidence:** Configuration control logs documenting:
    - Changes to software or systems related to remote operation and telemetry.
    - Justifications for changes, including risk analysis.
  + **Verification Method:** Ensure that all changes are tracked, tested, and approved through review boards.

### 8.1.8 IV&V Evidence

Objective: Ensure remote control systems meet mission safety and reliability through independent reviews.

* **IV&V Reports**:

  + **Evidence:** Completed IV&V reports showing evaluation of remote monitoring and operation capabilities for design compliance, test sufficiency, and safety risk assessments.
  + **Verification Method:** Validate IV&V findings against system test and safety metrics.
* **IV&V Participation Logs**:

  + **Evidence:** Meeting logs and review documents showing IV&V participation in critical inspections and design reviews.
  + **Verification Method:** Cross-check IV&V coverage of all stages in the software lifecycle.

### 8.1.9 Operational and Training Evidence

Objective: Ensure readiness of operators and mission control for remote operations.

* **Operator Training Records**:

  + **Evidence:** Training completion certificates and operator evaluation results demonstrating proficiency in remote system use, troubleshooting, and recovery protocols.
  + **Verification Method:** Tracking of training metrics and post-simulation exercises.
* **Operational Readiness Demonstration**:

  + **Evidence:** Records from operational readiness testing, such as system-in-the-loop simulations involving mission control operations for remote capabilities.
  + **Verification Method:** Analysis of test results against mission operational requirements.

## 8.2 Examples of Specific Artifacts for Objective Evidence

| **Artifact** | **Description** | **Verification Method** |
| --- | --- | --- |
| System Architecture Diagrams | Shows how remote control components are integrated into the overall system architecture. | Design review and traceability exercise. |
| Software Requirements Analysis Document (SRAD) | Enumerates remote operation requirements and their mapping to subsystems and software. | Requirements traceability matrix review. |
| Hazard Analysis Reports | Identifies remote-related hazards and mitigation strategies. | Peer-reviewed hazard control checklist. |
| Test Reports (Nominal and Off-nominal Conditions) | Provides results for all test cases related to remote operations. | Test pass/fail analysis and anomaly tracking. |
| Static and Dynamic Code Analysis Results | Includes results for code quality, vulnerability checks, and compliance with safety-critical standards. | IV&V evaluation for compliance. |
| Operator Training Logs | Confirms personnel readiness for normal and fault scenarios. | Audit training records for completeness and results. |
