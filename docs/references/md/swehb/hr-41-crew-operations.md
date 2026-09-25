# HR-41 - Crew Operations

> NASA Software Engineering Handbook (SWEHB Ver D), page id 171508215. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508215/HR-41+-+Crew+Operations

HR-41 - Crew Operations

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508215/HR-41+-+Crew+Operations#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=171508215)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=171508215&showCommentArea=true&showComments=true#addcomment)

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

4.4.1 The crewed space system shall provide the capability for the crew to monitor, operate, and control the crewed space system and subsystems, where:

1. 1. The capability is necessary to execute the mission; or
   2. The capability would prevent a catastrophic event; or
   3. The capability would prevent an abort.

## 1.1 Notes

NASA-STD-8719.29, NASA Technical Requirements for Human-Rating, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: HR-41 History

HR-41 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.4.1 The crewed space system shall provide the capability for the crew to monitor, operate, and control the crewed space system and subsystems, where:  1. 1. The capability is necessary to execute the mission; or    2. The capability would prevent a catastrophic event; or    3. The capability would prevent an abort. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

This capability flows directly from the definition of human-rating. Within the context of this requirement, monitoring is the ability to determine where the vehicle is, its condition, and what it is doing. Monitoring helps to create situational awareness that improves the performance of the human operator and enhances the mission. Determining the level of operation over individual functions is a decision made separately for specific space systems. Specifically, if a valve or relay can be controlled by a computer, then that same control could be offered to the crew to perform that function. However, a crew member probably could not operate individual valves that meter the flow of propellant to the engines, but the function could be replaced by a throttle that incorporates multiple valve movements to achieve a desired end state (reduce or increase thrust). Meeting any of the three stated conditions invokes the requirement. The first condition recognizes that the crew performs functions to meet mission objectives and, in those cases, the crew is provided the designated capabilities. This does not mean that the crew is provided these capabilities for all elements of a mission. Many considerations are involved in making these determinations, including the capability to perform the function and reaction time. The second and third conditions recognize that, in many scenarios, the crew improves the performance of the system and that the designated capabilities support that performance improvement.

This requirement ensures that the crew has direct access to system and subsystem controls and real-time monitoring capabilities to address operational challenges during critical moments. Crewed intervention, when appropriately designed into the system, provides an essential layer of redundancy, adaptability, and mission flexibility by enabling human oversight and decision-making when automated systems alone may fail to manage dynamic, unforeseen conditions.

This requirement acknowledges the critical role of human capabilities in monitoring, operating, and controlling crewed systems during dynamic, unforeseen challenges. By enabling the crew’s direct involvement, this requirement:

* Safeguards mission-critical systems and objectives.
* Prevents catastrophic outcomes through proactive intervention.
* Provides essential redundancy against failures in autonomous control systems.
* Ensures compliance with human-rating standards, prioritizing crew safety and mission reliability.

Incorporating robust monitoring and control capabilities into crewed space systems is vital for achieving mission success and ensuring the safety of human occupants.

## 2.1 Mission Success

A crewed space system must enable the execution of its mission objectives, which often involves tasks requiring human intelligence, intuition, and adaptability. While autonomous systems handle routine and pre-programmed actions, certain operations rely on human decision-making due to the complexity and unpredictability of challenges in space. For example:

* Complex docking procedures, surface maneuvers, or scientific experiments may require real-time human adjustments based on environmental conditions.
* Reacting to unexpected scenarios where pre-programmed logic may not foresee or appropriately address nuanced conditions, such as spacecraft alignment shifts or surface terrain changes during landing.

By providing the crew with monitoring and control capabilities, the system ensures that human intervention can support the achievement of mission-critical objectives.

## 2.2 Prevention of Catastrophic Events

Catastrophic events, such as uncontrolled cabin depressurization, power system failure, or critical malfunctions in life-support systems, require an immediate response. Autonomous systems provide initial fault detection and correction, but may have failure points, conflicting responses, or errors that only human insight can safely resolve.

* **Examples:**
  + If onboard sensors providing false-positive data were to disable critical systems autonomously, the crew could intervene and restore those systems in time to avoid catastrophic consequences.
  + Failure of an autonomous control algorithm (due to unforeseen conditions) during attitude maintenance might require the crew to manually stabilize the spacecraft to prevent structural damage.

Providing the crew with the capability to monitor and intervene safeguards life, the spacecraft, and mission success when automated systems encounter limitations or faults.

## 2.3 Prevention of Mission Abort

Abort scenarios pose significant risks to program cost, safety, and strategic goals. Equipping the crew with control features allows them to address anomalies or system failures that might otherwise lead to an unnecessary mission abort.

* **Examples:**
  + A propulsion system anomaly might initially suggest an abort, but real-time crew adjustments (e.g., by redistributing power, isolating faulty modules, or manually configuring backup systems) could ensure completion of the mission.
  + A malfunctioning sensor flagging non-critical issues might initiate abort procedures in autonomous systems, but with the crew's capability to analyze and override such abort actions, the mission could continue as planned.

Proactive involvement by the crew provides an additional layer of risk mitigation, potentially recovering from partial failures and avoiding aborts when systems retain operable functionality.

## 2.4 Human Flexibility in Dynamic Environments

Space missions frequently operate in environments where conditions may evolve unpredictably. While autonomous systems excel in processing structured tasks, humans bring adaptability, creativity, and decision-making under uncertain circumstances that exceed the capacity of predefined logic or algorithms. This is particularly true in crewed systems where safety and overall mission success hinge on responding to situations outside the boundaries of typical operational parameters.

* **Examples:**
  + Environmental factors such as solar storms or micrometeoroid impacts may cause peripheral damage that autonomous diagnostics might fail to contextualize properly. Crew response and decision-making can rapidly adapt to such conditions and prioritize recovery actions.

## 2.5 Redundancy and Reliability

Crew intervention serves as a vital layer of redundancy for system functionality, adding reliability in situations where software or hardware malfunctions occur. Relying exclusively on autonomous systems without redundant crew oversight introduces risks associated with system-level failures, software bugs, and physical wear and tear.

* **Examples:**
  + In the case of Apollo missions, human decision-making was integral to compensating for technical limitations or unexpected failures (e.g., manual adjustments during the Apollo 11 lunar landing).
  + Recent examples such as ISS ammonia leaks demonstrate the need for crew-led diagnostics when critical systems begin degrading unexpectedly.

By empowering the crew with monitoring, operation, and control capabilities, the system achieves higher resilience against any cascading failures.

## 2.6 Alignment with Human-Rating Principles

NASA’s **Human-Rating Standards** require crewed systems to prioritize crew safety, mission success, and fault tolerance. A key principle of human-rating is that humans provide a final layer of oversight and intervention to safeguard the spacecraft and its crew.

* This requirement aligns with the core tenants of NPR 8705.2, ensuring crew involvement in managing spacecraft operations and enabling immediate intervention when systems require repair, adjustment, or redundancy.

## 2.7 Examples of Catastrophic or Abortive Scenarios Addressed by the Requirement

#### **Catastrophic Scenarios:**

1. **Life-Support System Malfunctions:** The crew can intervene in oxygen production, CO₂ removal, or temperature regulation failures when autonomous systems fail.
2. **Power Failures:** Manual power redistribution or activation of alternative backups can prevent critical system shutdowns.
3. **Propulsion Failures:** The crew can manually stabilize or reconfigure attitude control thrusters to avert catastrophic loss of control.

#### **Abortive Scenarios:**

1. **Sensor Errors Triggering Abort Signals:** Manual analysis can override false abort signals caused by faulty sensor data if conditions are still within mission tolerances.
2. **Docking or Maneuvering Failures:** Crew manual control can ensure precision maneuvering and avoid abort if autonomous systems encounter misalignment or hardware irregularities.
3. **Environmental Emergencies:** Crew response to micrometeoroid penetrations or atmospheric anomalies can prevent unnecessary abort decisions by autonomously controlled systems.

## 2.8 Historical NASA Lessons Relevant to the Requirement

1. **Apollo 11 Lunar Landing:** Neil Armstrong manually took over the lunar module's control when onboard sensors flagged terrain issues during landing. Without manual control, the mission could have led to failure.
2. **Apollo 13 Oxygen Failure:** The crew manually managed life support and propulsion systems following the oxygen tank explosion. Their ability to monitor and control the spacecraft prevented catastrophic outcomes.
3. **International Space Station (ISS) Incidents:** Multiple instances where manual crew adjustments to life-support and power systems prevented catastrophic failures.

## 2.9 Relationship to Other Requirements:

This requirement complements the autonomy-related requirement [HR-39 - Autonomous Operation](/spaces/SWEHBVD/pages/171508213/HR-39+-+Autonomous+Operation) (autonomous control of critical functions). Autonomous systems provide initial fault detection and mitigation, while this requirement ensures human redundancy for monitoring, operating, and controlling systems under failure scenarios.

# 3. Guidance

As stated in NPR 8705.2, a human-rated system must accommodate human needs, leverage human capabilities, and ensure safety for human operations while allowing safe recovery from emergencies. The heart of a human-rated system is its ability to provide the crew with effective tools to monitor, operate, and control space systems, particularly when performing mission-critical tasks, preventing catastrophic events, or avoiding mission aborts. This guidance emphasizes the necessary software engineering tasks for achieving these objectives with a focus on reliability, usability, and safety.

By implementing intuitive HMI design, fault tolerance, error-handling mechanisms, and comprehensive training/testing, software systems can empower the crew to maintain situational awareness and intervene when necessary. Satisfying this requirement ensures that crewed space systems adequately accommodate human needs, enhance mission success, mitigate catastrophic risks, and maintain safety under both nominal and off-nominal conditions.

## 3.1 Human-Rating Principles Overview

The principle of human-rating a space system rests on three interconnected tenets:

1. A human-rated system must enable the safe conduct of required missions.
2. Human interaction with the system must be accommodated to enhance both safety and mission success.
3. Design features must include capabilities for safe recovery of the crew from hazardous or emergency situations.

Under this requirement, **crew monitoring** refers to the ability to determine the spacecraft's location, status, and ongoing activities, while **crew operations** involve the ability to intervene, operate, and configure subsystems as needed. This dual approach ensures situational awareness for the crew and supports critical decision-making in real-time.

Designing software to satisfy this requirement involves balancing **automated functionality** with **manual crew control**, carefully determining which functions require crew input without overburdening the crew. The role of software is to act as an enabler, improving crew efficiency, safety, and mission objectives.

## 3.2 Key Software Tasks for Crew Operations and Monitoring

To meet the requirement, the following software engineering tasks should be implemented. These tasks ensure comprehensive planning, design, and validation of the crew's ability to monitor, operate, and control critical systems.

### 3.2.1 Human-Machine Interface (HMI) Design

* **Objective:** Develop an intuitive and robust Human-Machine Interface (HMI) to enable the crew to monitor system status and take control efficiently when needed.
* **Key Actions:**
  + Follow NASA HMI design standards as outlined in **Appendix F of NASA-STD-3001, Volume 2** [498](#_tabs-<p></p>) .
  + Ensure clear presentation of critical information, including system conditions, alerts, and health metrics, arranged by priority.
  + Optimize control usability, enabling quick and unambiguous actions during abnormal situations.
  + Provide visual and auditory feedback to confirm crew commands are received and executed.

### 3.2.2 Real-Time Data Monitoring

* **Objective:** Provide continuous, real-time monitoring of all critical subsystems to facilitate crew situational awareness and timely decision-making.
* **Key Actions:**
  + Build robust telemetry software that captures and displays system health, status, and performance data.
  + Enable configurable alert notifications, prioritizing mission-critical or safety-critical conditions.
  + Ensure the monitoring system displays operational context, such as spacecraft attitude, position, and environmental conditions.

### 3.2.3 Crew Control System Implementation

* **Objective:** Design control software that enables the crew to interact directly with critical subsystems and override automated processes when needed.
* **Key Actions:**
  + Develop user-configurable control modes, allowing flexibility in switching between autonomous, semi-autonomous, and manual operations.
  + Incorporate **manual override capabilities** to empower the crew to take full control during emergencies.
  + Ensure that user commands take priority without conflicting with automated processes, preserving system integrity.
  + Incorporate a layered design approach that allows crew commands to operate at different abstraction levels (e.g., a single "throttle" control may govern the operation of multiple valves simultaneously).

### 3.2.4 Safety-Critical Software Engineering

* Define, implement, and thoroughly verify safety-critical software elements:
  + **Fault Detection, Isolation, and Recovery (FDIR):** Ensure subsystems include robust software to identify and recover from failures autonomously, while also allowing the crew to intervene manually if needed.
  + **Hazard Mitigations:** Implement software-based controls designed to mitigate hazards identified through hazard analyses (e.g., loss of propulsion, life-support failures).

### 3.2.5 Redundancy and Fault Tolerance

* **Objective:** Ensure critical systems remain functional even in the presence of faults.
* **Key Actions:**
  + Incorporate software managing redundant paths for critical subsystems (e.g., redundant avionics, fault-tolerant communications).
  + Build failover logic that automatically switches to redundant components, notifying the crew of the failure and recovery state.

### 3.2.6 Error Handling and Recovery

* **Objective:** Ensure the software detects and mitigates errors without destabilizing the system or introducing hazards.
* **Key Actions:**
  + Design robust error-handling mechanisms for edge cases, anomalies, and faults in the operational software.
  + Include real-time error logging and status updates for the crew.
  + Provide recovery procedures initiated by either the system or the crew, as appropriate.

### 3.2.7 Independent Verification and Validation (IV&V)

* Independent assurance is critical to qualifying software for safety and mission requirements.
* **Key Actions:**
  + Include IV&V reviews for all HMI functions, telemetry systems, crew control features, fault-handling systems, and recovery mechanisms.
  + Validate the redundancy strategies and failover mechanisms through rigorous fault injection tests during IV&V.

### 3.2.8 Simulation and Testing

* **Objective:** Validate software functionality, robustness, and crew usability under multiple scenarios.
* **Key Actions:**
  + Conduct simulations covering nominal scenarios (normal operation), off-nominal conditions (anomalies or partial failures), and emergency situations.
  + Use hardware-in-the-loop (HIL) testing to assess the software’s ability to interact with physical systems and validate crew control responses.
  + Perform boundary testing to identify potential points of failure under stressed or extreme conditions.

### 3.2.9 Configuration Management

* Maintain strict version control over safety-critical software artifacts to ensure consistency and traceability.
* **Key Actions:**
  + Ensure all updates to monitoring, control, and recovery capabilities are fully validated before deployment.
  + Track all historical versions of software modules relevant to mission-critical systems for auditability.

### 3.2.10 Training and Documentation

* **Objective:** Ensure the crew understands how to efficiently operate the tools provided for monitoring and control.
* **Key Actions:**
  + Provide **training simulators** that allow realistic practice with HMI, telemetry, and recovery systems.
  + Develop **procedures manuals and troubleshooting guides** that document error-handling workflows for off-nominal scenarios.
  + Develop a **User Manual** for all monitoring and control systems, including annotated examples of key actions and recovery strategies.

## 3.3 Additional Supporting Guidance

* Refer to **NASA Spaceflight Human-System Standard, NASA-STD-3001** for additional crew interaction principles.
* Consult Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for complementary software engineering considerations.
* Follow **NASA-STD-8739.8 (Software Assurance and Software Safety Standard** [278](#_tabs-<p></p>) ) for safety-critical software development.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Requirements related to Human Rated Software.

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

For small-scale space projects, such as CubeSats, small lunar rovers, or other crewed systems with limited complexity, meeting this requirement must focus on simplicity, efficiency, and cost-effectiveness while maintaining compliance with safety-critical standards. Below is tailored guidance for implementing this requirement for small projects, considering resource constraints.

Small projects can implement this requirement by focusing on simplicity, prioritization of critical functions, and streamlined crew capabilities. Building intuitive interfaces, real-time telemetry systems, and manual overrides—with minimal resource investment—ensures project compliance without the complexity or overhead of larger space systems. These steps ensure crew readiness to monitor, operate, and control vital systems for mission execution and safety.

## 4.1 Key Considerations for Small Projects

1. **Simplicity and Focus:**  
   Maintain simplicity in design and implementation by focusing on critical systems and subsystems necessary to satisfy mission success, crew safety, and abort prevention. Avoid over-engineering or incorporating unnecessary features.
2. **Prioritization of Safety-Critical Functions:**  
   Delegate crew monitoring and control capabilities only for highly critical functions (e.g., propulsion control, life-support management), balancing automation and manual intervention wisely.
3. **Scalability:**  
   Leverage modular and scalable software design principles, allowing incremental upgrades without introducing significant complexity.
4. **Cost and Resource Efficiency:**  
   Develop lightweight solutions (e.g., streamlined human-machine interfaces and telemetry systems) and utilize existing tools and frameworks to save development time.

## 4.2 Steps to Implement the Requirement in Small Projects

### 4.2.1 Identify Critical Systems and Subsystems

Focus first on identifying key operations that:

* Support **mission execution** (e.g., propulsion adjustments for orbital transfers).
* Prevent **catastrophic events** (e.g., manual control of life-support or thermal regulation systems).
* Prevent **mission aborts** (e.g., overriding faulty sensors or reconfiguring communications).

#### **Deliverable**:

A concise **Critical System List**, documented to show which subsystems require crew involvement based on mission risk analysis (e.g., crew medicinal countermeasures, basic propulsion adjustments).

### 4.2.2 Minimal Human-Machine Interface (HMI) Design

* **Objective:** Develop a simple interface for crew monitoring and control.
* **Design Features:**
  + Basic visual dashboards presenting health and status indicators for critical systems.
  + Controls for simple and direct manual override (e.g., stop/start critical subsystems, propulsion throttle adjustments).
  + Minimal navigation complexity prioritizing ease-of-use (e.g., one-screen status dashboard or single-button controls).

#### **Guideline for Small Projects**:

* Use frameworks or tools that simplify HMI design (e.g., Python with Tkinter, web-based interfaces for telemetry).
* Tailor design for low-complexity systems while following NASA-STD-3001 (Human-System Interaction) for safety-critical displays.

#### **Deliverable**:

A **Crew Interface Prototype** with basic controls and indicators, validated with crew simulations.

### 4.2.3 Real-Time Monitoring with Alert Functionality

* **Objective:** Implement lightweight software that provides real-time updates on critical systems and sends alerts for anomalies or safety-critical events.
* **Monitoring Features:**
  + Status indicators for propulsion, life-support, and other mission-essential subsystems.
  + Alert notifications (e.g., color-coded visual or audio tones) for faults or warnings.

#### **Guideline for Small Projects**:

* Implement telemetry software using open-source libraries (e.g., MQTT, ZeroMQ for data verification).
* Build simple dashboards for crews to visualize system health efficiently.

#### **Deliverable**:

A **Basic Telemetry System** that displays real-time status and key alerts for critical systems.

### 4.2.4 Manual Override Capabilities

* **Objective:** Provide the crew with the ability to intervene in case automated control systems fail or anomalous conditions arise.
* **Manual Control Design:**
  + Limited manual control capabilities for mission-critical systems (e.g., toggling life-support systems, adjusting propulsion thrust).
  + Local or remote overrides independent from automation logic.

#### **Guideline for Small Projects**:

* Implement hardware/software switches (e.g., physical push buttons or basic control menus) for manual overrides where computational control is unsafe.
* Ensure controls are straightforward and reliable with minimal failure points.

#### **Deliverable**:

A **Hardware or Software Override Subsystem** tested under simulated failure conditions to demonstrate crew intervention capabilities.

### 4.2.5 Testing and Simulation

* **Objective:** Perform basic yet rigorous testing of crew monitoring, operation, and control features.
* **Activities:**
  + Simulate nominal and off-nominal conditions (e.g., system faults, anomalies) where crew interventions are required.
  + Test the user interface and telemetry system for responsiveness and robustness in real-time monitoring.
  + Validate manual override mechanisms and verify fault-tolerant behavior.

#### **Guideline for Small Projects**:

* Create simple testbeds tailored to the small system’s operations (e.g., software-in-the-loop testing, hardware-in-the-loop testing if feasible).
* Use automated testing tools for telemetry verification (e.g., unit tests for fault detection routines).

#### **Deliverable**:

A **Test Report** with results demonstrating crew capabilities under nominal and off-nominal conditions.

### 4.2.6 Documentation and Training

* **Objective:** Provide concise documentation to train the crew on system monitoring, operation, and control procedures.
* **Features of Documentation:**
  + User manuals with screenshots of the dashboard and troubleshooting workflows.
  + Quick reference guides for recovering from faults using manual overrides.

#### **Guideline for Small Projects**:

* Keep documentation short and practical, prioritizing critical information over exhaustive details.
* Provide explanations for possible recovery scenarios and their required crew actions.

#### **Deliverable**:

A **User Manual** and **Training Module**, tested with a small number of crew training sessions.

## 4.3 Small Project Example: CubeSat Crewed Operation

For a CubeSat mission to maintain station-keeping in LEO, the following implementation could satisfy the requirement:

1. **Critical System List**:

   * Attitude control subsystem for orbit stability.
   * Power subsystem to maintain thermal and electrical equilibrium.
2. **HMI Design**:  
   A tablet-based dashboard with real-time CubeSat status (attitude stability and power generation metrics). Manual controls provided for thruster adjustments and power resets.
3. **Real-Time Monitoring**:  
   A telemetry system that visualizes CubeSat health using onboard sensors. Simple color-coded alerts for low power or attitude misalignment.
4. **Manual Override**:  
   Physical switches or commands to reboot the CubeSat controller or recalibrate thrusters.
5. **Simulation and Testing**:  
   Simulated power failures tested in software/hardware environments to validate crew response effectiveness.
6. **Documentation and Training**:  
   A short PDF manual explaining dashboard use and step-by-step procedures for manual calibration or system reboot.

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
* (SWEREF-498)

  [NASA Space Flight Human-System Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-3001-vol-2 "Click to open in new window")

  NASA-STD\_3001, Volume 2: Human Factors, Habitability, and Environmental Health, Revision A, 2015.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA's history is rich with mission scenarios that underscore the importance of providing crewed space systems with robust monitoring, operation, and control capabilities. These lessons learned demonstrate how incorporating effective interfaces, manual override options, and human adaptability mitigates risks, prevents catastrophes, and ensures mission success.

Below is a collection of key lessons learned from NASA missions that reinforce the relevance and importance of Requirement 4.4.1.

---

### **1. Apollo 13: Critical Crew Intervention Following System Failure**

**Lesson:**  
Apollo 13 experienced a catastrophic failure when an oxygen tank exploded, disabling the spacecraft’s power, oxygen, and propulsion systems. The crew leveraged their monitoring capabilities, manual control interfaces, and operational training to manage the situation. Key actions taken by the crew:

* Utilizing real-time data monitoring to assess the extent of damage and prioritize life-support and energy resources.
* Manually configuring the Lunar Module (LM) as a "lifeboat" to support life-support systems and maintain attitude control.
* Implementing improvised operations guided by telemetry and ground support to return safely to Earth.

**Key Takeaways for Requirement 4.4.1:**

* **Real-Time Monitoring:** Enables situational awareness during emergencies.
* **Manual Operation and Control:** The crew’s ability to take manual control of subsystems (e.g., power or propulsion) can prevent catastrophic outcomes.
* **Training and Documentation:** Crew training in fault isolation and subsystem control was critical in navigating the crisis.

---

### **2. Apollo 11: Manual Control During Lunar Landing**

**Lesson:**  
During the Apollo 11 lunar landing, Neil Armstrong manually took over the Lunar Module’s control when onboard navigation software flagged unsafe landing conditions in an area with boulders and craters. Armstrong adjusted the descent trajectory manually and successfully landed the spacecraft.

**Key Takeaways for Requirement 4.4.1:**

* **Manual Override Capability:** The ability to manually override automated systems is critical for handling unforeseen conditions that automation may misinterpret or fail to resolve.
* **Crew Situational Awareness:** Monitoring the Lunar Module's sensors and adjusting based on real-time observations contributed directly to mission success.
* **HMI Design:** Simple and functional interfaces allowed Armstrong to focus on manual operations without being overwhelmed.

---

### **3. Skylab 1: Crew Intervention Addressed Launch Damage**

**Lesson:**  
The Skylab spacecraft suffered significant damage during launch, including the loss of its protective micrometeoroid shield and part of the solar array. The crew onboard Skylab was able to monitor the station’s deteriorating conditions and execute manual operations to address the damage:

* Deploying a thermal shield to regulate temperature manually.
* Performing repairs on power generation and communication systems.

**Key Takeaways for Requirement 4.4.1:**

* **Crew Monitoring:** Real-time data monitoring allowed the crew to identify threats to habitability and station functionality.
* **Manual Repair Tools and Interfaces:** The ability to perform manual interventions provided a critical lifeline to recover operational capability.
* **Human Adaptability:** The crew’s ability to improvise mitigated the loss of mission-critical systems.

---

### **4. International Space Station (ISS): Ammonia Leak Incident**

**Lesson:**  
During an ISS ammonia leak in the cooling system, the astronauts were able to monitor anomalous pressure levels in the cooling system and manually activate backup systems to isolate the affected loop. The crew also performed an extravehicular activity (EVA) for repairs.

**Key Takeaways for Requirement 4.4.1:**

* **Real-Time Monitoring:** Monitoring system conditions, such as pressure, allowed the crew to respond promptly to anomalies.
* **Manual System Control:** The ability to operate and isolate specific cooling loops was essential for mitigating hazards.
* **Crew-Ground Collaboration:** Situational awareness and manual adjustments combined with ground support ensured timely decision-making.

---

### **5. Shuttle Columbia STS-3: Manual Override of Reaction Control System**

**Lesson:**  
During STS-3, Columbia’s reaction control system exhibited problems during descent due to sensor drift. The crew manually adjusted the control inputs to stabilize the shuttle and ensure a safe landing.

**Key Takeaways for Requirement 4.4.1:**

* **Manual Override Capability:** Enabled the crew to address stability issues that automation alone could not resolve.
* **Redundancy and Fault Tolerance:** Fault isolation and manual adjustments ensured the mission was not aborted prematurely.
* **Crew Judgment and Training:** Manually operating the shuttle without relying solely on data from faulty sensors prevented catastrophic outcomes.

---

### **6. Apollo Program: Lessons on HMI Design**

**Lesson:**  
Throughout the Apollo program, human-machine interfaces were continually refined based on crew feedback during training and flight:

* The simple and intuitive design of Apollo spacecraft controls allowed crews to handle complex mission scenarios without confusion.
* Poorly designed HMIs in early iterations led to inefficiencies during crew operation and required additional training and redesigns.

**Key Takeaways for Requirement 4.4.1:**

* **HMI Usability:** The success or failure of manual crew operations often depends on the interface’s ability to provide unambiguous status information and controls.
* **Crew Feedback:** Iterative improvements in the HMI design based on astronaut feedback enhanced operational performance and mission success.

---

### **7. Space Shuttle Challenger Disaster: Importance of Crew Monitoring**

**Lesson:**  
Although the Challenger disaster was ultimately fatal, lessons learned highlighted the need for improved real-time monitoring and controls that allow the crew to recognize and respond to catastrophic failures earlier:

* Crew monitoring capabilities must include robust telemetry systems for real-time anomaly detection across mission-critical subsystems.

**Key Takeaways for Requirement 4.4.1:**

* **Comprehensive Monitoring Systems:** A failure in robust monitoring contributed to an inability to mitigate risks in earlier phases of the failure cascade.
* **Emergent Redundancy:** Ensuring independent and redundant monitoring systems for safety-critical functions could improve response time during catastrophic scenarios.

---

### **Key Themes Across NASA Lessons Learned**

From NASA’s mission history, several recurring themes emerge that are directly applicable to Requirement 4.4.1:

#### **1. Real-Time Monitoring and Situational Awareness**

* Crew access to real-time telemetry is critical for identifying system anomalies early and responding proactively.
* Monitoring systems should feature alerts and easy-to-interpret health metrics for safety-critical subsystems.

#### **2. Manual Override**

* Automated systems may fail or misinterpret conditions, requiring manual intervention by the crew.
* Manual override capabilities ensure that the crew can stabilize or recover functionality despite software or hardware faults.

#### **3. Human-Machine Interface Design**

* Interfaces must be intuitive and display information clearly, enabling quick decision-making during emergencies.
* Complex or poorly designed interfaces can hinder crew performance and compromise mission success.

#### **4. Crew Training and Operational Confidence**

* Training is essential to ensure the crew is familiar with monitoring systems, manual controls, and troubleshooting protocols.
* Operational simulations help build crew confidence in handling nominal and off-nominal scenarios.

#### **5. Fault Tolerance and Redundancy**

* Systems must be designed with redundancy and recovery mechanisms to ensure continuity of critical functions.
* Independent systems for manual operation should be integrated into the spacecraft’s architecture.

#### **6. Collaboration Between Crew and Ground Teams**

* Effective monitoring and control systems should support collaboration between onboard crews and ground personnel for jointly managing anomalies and mission-critical operations.

---

### **Conclusion**

NASA’s lessons learned highlight the critical role of crew monitoring, operation, and control capabilities in ensuring mission success and safety. Designing spacecraft systems to accommodate human needs, empower manual interventions, and provide situational awareness reinforces the importance of Requirement 4.4.1 by mitigating risks of catastrophic events, mission aborts, or operational failures. These lessons emphasize the balance between automation and human interaction, proving that robust monitoring and control systems are indispensable for crewed spaceflight.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-41 - Crew Operations**

4.4.1 The crewed space system shall provide the capability for the crew to monitor, operate, and control the crewed space system and subsystems, where:

1. 1. The capability is necessary to execute the mission; or
   2. The capability would prevent a catastrophic event; or
   3. The capability would prevent an abort.

This guidance ensures software assurance tasks comprehensively address the crew’s ability to monitor, operate, and control safety-critical subsystems. The combination of well-defined metrics, iterative testing, design reviews, robust hazard analyses, and traceability ensures compliance with this requirement.  By leveraging lessons learned and standards such as **NASA-STD-8739.8** [278](#_tabs-<p></p>), projects can ensure software is safe, reliable, and mission-ready.

## 7.1 Tasking for Software Assurance

1. Ensure the development, implementation, and testing of robust control algorithms capable of managing critical functions with crew intervention. These algorithms must undergo thorough testing to guarantee their reliability and safety in all operational scenarios.
2. Ensure redundancy and fault tolerance are included in the design to ensure that critical functions can continue to operate autonomously or the crew can monitor, operate, and control the crewed space system and subsystems, , even in the presence of faults or failures. This includes implementing backup systems and failover mechanisms.
3. Ensure that Integrated real-time monitoring and diagnostic tools are used to continuously assess the health and status of critical systems and subsystems. These tools should detect anomalies and trigger autonomous responses to mitigate potential catastrophic events and alert the crew of the situation for potential intervention.
4. Employ safety analysis techniques such as [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) and [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) to identify potential hazards and failure modes. This helps in designing controls and mitigations to allow the crew to effectively monitor, operate, and control the space system during various critical operations.
5. Ensure extensive simulations and testing are conducted to verify that the crew can effectively monitor, operate, and control the space system under various conditions, including nominal and off-nominal scenarios. This includes testing for unexpected situations and boundary conditions.
6. Confirm that strict configuration management to ensure that the correct software versions and configurations are used. This reduces the risk of errors due to incorrect or inconsistent configurations that could impact crew operations.
7. Ensure robust error handling and recovery mechanisms to address errors stemming from detected faults. This ensures that error handling is adequate and that the system can recover from errors without leading to hazardous or catastrophic events.
8. Perform safety reviews on all software changes and software defects.
9. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.
10. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically that the crew can effectively monitor, operate, and control the space system under various conditions, including nominal and off-nominal scenarios. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks). Ensure that the project has developed and executed test cases to test the software system’s recovery from faults.
11. Analyze the software test procedures for the following:
    1. Coverage of the software requirements.
    2. Acceptance or pass/fail criteria,
    3. The inclusion of operational and off-nominal conditions, including boundary conditions,
    4. Requirements coverage and hazards per [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) and [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), respectively.
12. Perform test witnessing for safety-critical software to ensure that the crew can effectively monitor, operate, and control the space system under various conditions, including nominal and off-nominal scenarios.
13. Confirm that test results are sufficient verification artifacts for the hazard reports.
14. Confirm independent software testing, including IV&V testing, is performed to verify that the capability is available for the crew to monitor, operate, and control the crewed space system and subsystems, where:
    1. The capability is necessary to execute the mission; or
    2. The capability would prevent a catastrophic event; or
    3. The capability would prevent an abort.
15. Ensure comprehensive training and documentation for operators are available.

## 7.2 Software Assurance Products

The purpose of software assurance guidance is to ensure the reliability, safety, and effectiveness of the software that enables crew monitoring, operation, and control capabilities across all mission scenarios. This improved guidance builds on established NASA standards, lessons learned, and best practices to address the life cycle of software development, from requirements through testing and deployment.

To ensure compliance with the requirement, the following software assurance products are necessary for validation and verification:

#### **Core Software Assurance Products**

1. **Software Assurance Status Reports**

   * Periodic status updates summarizing tasks completed, findings, identified risks, and mitigation actions related to the system's ability to support crew monitoring and control.
2. **Software Requirements Analysis**

   * Analysis to confirm that all crew-centric capabilities, such as monitoring, operation, and control, trace back to clear, verifiable requirements. Ensure that safety-critical requirements specific to system control functions are adequately identified (see [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements)).
3. **Software Design Analysis**

   * Analysis to evaluate the design architecture, including algorithms supporting crew capabilities. Ensure appropriate interfaces exist for monitoring system telemetry, controlling subsystems, and enabling manual overrides.
4. **Source Code Quality Analysis**

   * Demonstrate adherence to coding standards and assess software for defects, maintainability, and robustness. Key metrics include cyclomatic complexity, static analysis results, and code compliance with safety requirements (NASA-STD-8739.8 Appendix A).
5. **Testing Analysis**

   * Evaluate the testing process and results for software supporting crew monitoring, operation, and control. Verify that scenarios include both nominal and off-nominal conditions, failure modes, and system recovery.
6. **Software Safety and Hazard Analysis**

   * Completed hazard analyses and reports listing potential faults, failure response plans, and mitigations. Ensure all identified software hazards involving crew operations are traceable to resolved safety measures in software requirements and design.
7. **Fault Tree Analysis (FTA) and Failure Modes and Effects Analysis (FMEA)**

   * Detailed FTAs and FMEAs focused on software behavior in safety-critical scenarios.
8. **Audit Reports**

   * Ensure audits (Functional Configuration Audit [FCA] and Physical Configuration Audit [PCA]) verify that all software matches specified requirements and complies with safety-critical standards.
9. **Test Witnessing Evidence**

   * Test witnessing ([SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)) signatures to confirm software has been tested thoroughly under all operational and fault scenarios required by the project.

#### **Additional Deliverables**

* **Traceability Matrices:** Documenting traceability from hazard analyses to software requirements, design, implementation, and testing ( [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability)).
* **Verification Artifacts:** Results demonstrating automated test coverage, including code coverage metrics for safety-critical components, fault detection/recovery routines, and manual override paths.
* **User Manual:** Comprehensive documentation providing guidance to the crew for monitoring, operation, and recovery from anomalies and off-nominal conditions.

## 7.3 Recommended Metrics

### 7.3.1 Verification and Validation Metrics

1. **Test Coverage:**

   * Ensure ≥95% test coverage for critical paths enabling crew monitoring and control capabilities. This includes normal operations, off-nominal scenarios, and recovery processes.
   * Code coverage ≥90% for safety-critical components and all manual override paths.
2. **Defect Density:**

   * Track defects per 1,000 lines of code for crew support functions; a defect density ≤1.0 is desired for safety-critical systems.
3. **Requirements Traceability:**

   * 100% traceability from crew monitoring, operation, and control requirements to design, code, tests, and verification artifacts.

### 7.3.2 Safety Metrics

1. **Hazard Analysis:**

   * Ensure mitigation exists for 100% of hazards identified in software hazard analyses.
2. **Safety-Critical Requirements Compliance:**

   * Track the number of safety-critical requirements verified successfully vs. total requirements.

### 7.3.3 Quality Metrics

1. **Code Quality Metrics:**

   * Cyclomatic complexity ≤15 for critical code.
   * ≤10% code rework rate for defects discovered during integration testing.
2. **Code Churn:**

   * Measure code changes to monitor stability. Excessive churn indicates unclear requirements or design issues that require risk assessment.

### 7.3.4 Performance Metrics

1. **Response Time:**

   * Measure time-to-detect and resolve critical anomalies via crew interaction—specific thresholds based on mission parameters.
2. **System Uptime:**

   * ≥99.5% availability for systems during mission-critical phases.

### 7.3.5 Configuration Management Metrics

1. **Version Control:**

   * Ensure all software builds are tracked, with a complete record of changes and corresponding configuration compliance.
2. **Change Requests:**

   * Monitor approved software change requests and assess for impacts on functional and safety-critical software performance.

## 7.4 Software Assurance Guidance

To ensure the crewed space system is fully capable of satisfying Requirement 4.4.1, the following software assurance and safety engineering tasks provide a comprehensive approach:

### 7.4.1 Human-Machine Interface (HMI) Assurance

* Confirm that HMI designs meet usability and safety standards outlined in **NASA-STD-3001, Vol 2**.
* Verify interfaces clearly display critical telemetry data in failure scenarios, provide immediate feedback for user actions, and ensure guided workflows that reduce human errors.

### 7.4.2 Real-Time Data Monitoring

* Verify the telemetry system scans for faults continuously and displays anomalies prominently in a format understandable by the crew.
* Test all scenarios where anomalies can propagate into hazardous situations and confirm the system provides timely alerts.

### 7.4.3 Control Capability Validation

* Confirm that all automated functions have manual override options for critical systems (e.g., propulsion, life support, power distribution).
* Test manual controls to ensure they are fail-safe and operational under emergency conditions.

### 7.4.4 Fault Detection, Isolation, and Recovery (FDIR)

* Verify that software reliably detects faults, isolates failing components, and recovers systems without external intervention where feasible.
* Test FDIR compatibility with crew interaction, ensuring interventions are supported when FDIR limits are exceeded.

### 7.4.5 Software Safety and Hazard Analysis

* Conduct **Software Fault Tree Analysis (FTA)** and **Failure Modes and Effects Analysis (FMEA)** to identify and mitigate fault propagation risks.
* Include "what-if" fault scenarios for both crew-involved and autonomous monitoring systems to ensure robust software mitigations.

## 7.5 Expanded Testing and Review Tasks

### 7.5.1 Testing

* **Nominal Testing:** Verify that software meets performance requirements under normal operational conditions.
* **Off-Nominal Testing:** Introduce simulated faults or degraded scenarios (e.g., sensor malfunctions) to test crew ability to respond and recover.
* **End-to-End Testing:** Simulate an entire mission phase to confirm integrated crew monitoring, operation, and control features function as intended.

### 7.5.2 Configuration Management

* Perform configuration audits for software items (SWE-187).
* Include hazard reports and safety analysis in configuration-managed items.

### 7.5.3 Training

* Confirm that operational training for using software-based monitoring and control systems prepares the crew for off-nominal and emergency conditions.

## 7.6 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence demonstrates compliance with this requirement by verifying that the necessary capabilities for crew monitoring, operation, and control are implemented in the design, software, testing, and operational procedures of the crewed space system. It should be measurable, traceable, and independently verifiable.

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

Below is a comprehensive list of suggested objective evidence types categorized by system design, software engineering, testing, safety, and documentation artifacts.

## 8.1 System Design Evidence

#### **a. Functional System Design Documents**

* **Evidence:** System architecture diagrams showing how crew monitoring, operation, and control capabilities are integrated.
* **Details:** Highlight interfaces for telemetry, manual control systems, and fault recovery logic for critical mission subsystems (e.g., propulsion, life support).

#### **b. Human-Machine Interface (HMI) Design Documents**

* **Evidence:** HMI requirement specifications and design artifacts.
* **Details:** Screenshots or mockups of the crew interface demonstrating functionality for monitoring telemetry, manual overrides, system controls, and fault visualization.
* **Verification:** Conformance to NASA Standards for HMIs (*NASA-STD-3001, Vol 2*).

#### **c. Crew Operational Flow Diagrams**

* **Evidence:** Diagrams showing step-by-step crew workflows for normal operation, fault detection, and manual intervention.
* **Details:** Include triggers for manual overrides, system recovery actions, and fault confirmation processes.

## 8.2 Software Design and Development Evidence

#### **a. Software Requirements Specifications**

* **Evidence:** Traceable software requirements related to crew monitoring, operation, and control (e.g., SWE-050 compliant requirement documents).
* **Details:** Include requirements for real-time data access, fault diagnostics, system overrides, and manual recovery capabilities.

#### **b. Software Architecture Design**

* **Evidence:** Design diagrams showing crew-accessible monitoring and control software modules.
* **Details:** Include information on how telemetry and control subsystems interface with crew interfaces, identify fault-tolerant and redundant pathways.

#### **c. Source Code and Analysis Reports**

* **Evidence:** Static analysis/compliance tools verifying that safety-critical software follows coding standards.
* **Details:** Demonstrate adherence to guidelines from **NASA-STD-8739.8** (e.g., low cyclomatic complexity, no memory leaks, no untraceable code).

## 8.3 Software Safety and Hazard Analysis Evidence

#### **a. Hazard Reports and Mitigation Plans**

* **Evidence:** Completed hazard analysis documents identifying fault scenarios related to crew operations (e.g., system shutdown, sensor failures).
* **Details:** Include hazard classifications, fault consequences, and mitigation strategies such as fallback operations or manual overrides.
* **Specific Deliverables:**
  + Software Fault Tree Analysis (FTA).
  + Failure Mode and Effects Analysis (FMEA).
  + Software Safety and Hazard Analysis Report.

#### **b. Risk Assessments for Safety-Critical Software**

* **Evidence:** Documents showing the risk-ranking of failure modes resolved by software in the context of crew involvement.
* **Details:** Include risk controls, software safeguards, and rationale for unmitigated risks.

## 8.4 Verification and Validation Evidence

#### **a. Test Plans and Procedures**

* **Evidence:** Validation test plans that include scenarios for normal operations, fault detection, anomalous conditions, and recovery.
* **Details:** Confirm compliance with the requirement by incorporating crew monitoring and control assessments into specific test cases (e.g., thermal regulation manual override).
* **Documents:** V&V Plan (ensures traceability from requirement to test results).

#### **b. Test Reports and Results**

* **Evidence:** Reports from nominal and off-nominal testing verifying crew capabilities to monitor, operate, and control the system.
* **Details:** Include metrics for test coverage, success rates for recovery operations, and usability testing for crew interfaces.
* **Specific Deliverables:**
  + Test execution logs for fault management and manual override testing.
  + Fault detection latency measurements to ensure timely crew responses.
  + Test coverage reports for safety-critical paths and conditions.

#### **c. Hardware-in-the-Loop (HIL) Testing Evidence**

* **Evidence:** Results from running integrated HIL simulations of onboard systems, including crew interactions during critical scenarios.
* **Details:** Evaluate crew response timing, the robustness of HMIs, and the execution of recovery protocols during simulated anomalies.

#### **d. Code Coverage Reports**

* **Evidence:** Code and path coverage data demonstrating sufficient testing of safety-critical functions.
* **Details:** Highlight specific coverage percentages for crew-related functionality, such as redundancy logic, fault recovery, and telemetry display software.

## 8.5 Audit and Review Evidence

#### **a. Functional Configuration Audit (FCA)**

* **Evidence:** FCA documentation verifying that all functional requirements related to crew monitoring, operation, and control capabilities have been met.

#### **b. Physical Configuration Audit (PCA)**

* **Evidence:** PCA confirming that software systems conform to the documented configuration, including interfaces for the crew and underlying fault-tolerant systems.

#### **c. Peer Review Records**

* **Evidence:** Documented results from peer reviews of safety-critical design artifacts, software, and test procedures.
* **Details:** Include checklists and action items related to crew support functions.

#### **d. IV&V Review Reports**

* **Evidence:** Reports from Independent Verification and Validation (IV&V) identifying how crew interactions with monitoring and control systems have been independently assessed for safety and mission performance.

## 8.6 Configuration Management Evidence

#### **a. Change Control Records**

* **Evidence:** Records of all changes to safety-critical software, including impacts on crew monitoring and control systems.
* **Details:** Trace all updates to or deviations from original requirements and ensure they are consistent with hazard analysis findings.

#### **b. Configuration Management Reports**

* **Evidence:** Reports detailing reviews of all configuration items, including interface designs, telemetry logic, and crew recovery systems.
* **Details:** Track compliance against **SWE-081** (configuration identification for hazard-linked software).

## 8.7 Training and Documentation Evidence

#### **a. Comprehensive User Manuals**

* **Evidence:** A user manual tailored explicitly for crew operations, including:
  + Detailed procedures for monitoring telemetry systems.
  + Step-by-step instructions for responding to faults (manual overrides, recovery).
  + Troubleshooting guides for managing anomalies during critical phases.
  + Emergency protocols tailored to high-risk failure conditions.

#### **b. Training Program Records**

* **Evidence:** Records demonstrating that the crew has been trained in the use of monitoring, operation, and control systems.
* **Details:** Include training plans, session logs, and post-training evaluation results to verify crew readiness.

## 8.8 Key Metrics for Monitoring Compliance

#### **Sample Metrics:**

* Percentage of test cases covering fault scenarios requiring crew intervention.
* Number of faults successfully mitigated during manual override testing.
* Time-to-recovery benchmarks for manual fault management processes.
* Code coverage percentages for safety-critical subsystems directly linked to crew monitoring and control.

## 8.9 Summary of Objective Evidence

**System Design:** System architecture diagrams, HMI designs, functional workflow diagrams.  
**Software Development:** Requirements analysis, source code tests, compliance with standards.  
**Safety Analysis:** Hazard reports, FTA/FMEA analyses, risk assessments.  
**Verification and Validation:** Test reports, HIL results, code coverage metrics, IV&V verification findings.  
**Audits and Reviews:** FCA/PCA reviews, peer reviews, change impact assessments.  
**Training and Documentation:** Crew operation manuals, training records, troubleshooting protocols.

Each piece of evidence supports compliance with this requirement's intent to enable safe, effective, and mission-critical crew operations within the space system. Together, they provide a traceable and auditable path to requirement fulfillment.
