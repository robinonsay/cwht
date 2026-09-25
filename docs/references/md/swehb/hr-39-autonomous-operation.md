# HR-39 - Autonomous Operation

> NASA Software Engineering Handbook (SWEHB Ver D), page id 171508213. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508213/HR-39+-+Autonomous+Operation

HR-39 - Autonomous Operation

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508213/HR-39+-+Autonomous+Operation#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=171508213)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=171508213&showCommentArea=true&showComments=true#addcomment)

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

4.3.9 The crewed space system shall provide the capability for autonomous operation of system and subsystem functions which, if lost, would result in a catastrophic event.

## 1.1 Notes

This capability means that the crewed system does not depend on communication with Earth (e.g., mission control) to perform functions that are required to keep the crew alive (refer to the definition for Autonomous in Section 3.2 [458](#_tabs-<p></p>)).

**Autonomous**. The ability of a space system to perform operations independent from any Earth-based system. This includes no communication with, or real-time support from, mission control or other Earth systems. (source NPR 8705.2 [024](#_tabs-<p></p>))

## 1.2 History

Click here to view the history of this requirement: HR-39 History

HR-39 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.3.9 The crewed space system shall provide the capability for autonomous operation of system and subsystem functions which, if lost, would result in a catastrophic event. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

For critical functions on a crewed vehicle,  if a loss of communication occurs or the crew is unavailable/incapacitated, the system must have the capability to safe itself autonomously without crew or ground intervention in order to keep the crew alive.

In summary, the requirement for autonomous operation of system and subsystem functions that prevent catastrophic events is essential for ensuring mission success, crew survival, and system resilience even in the presence of failures, communication delays, or other unforeseen circumstances. It reflects the fundamental principles of risk mitigation, redundancy, fail-safe design, and human-centered engineering in the field of crewed space exploration.

This requirement is rooted in the need to ensure mission safety and the well-being of the crew during unforeseen circumstances. Below is the rationale for this requirement.

## 2.1 Mitigation of Catastrophic Risks

* Crewed space systems operate in environments where even minor failures can escalate into catastrophic events due to the harsh conditions of space (e.g., vacuum, microgravity, radiation).
* Ensuring systems and subsystems can operate autonomously minimizes reliance on external inputs (such as ground control or manual intervention by the crew) during critical events, reducing the likelihood of catastrophic situations caused by equipment malfunction or human error.

## 2.2 Crew Safety and Survival

* The safety of astronauts is the top priority in space exploration. Autonomous operation ensures essential life-supporting systems—such as oxygen flow, temperature regulation, and pressure maintenance—function without interruption, even in situations where crew assistance or communication with ground control is impaired.
* Autonomous systems provide a failsafe mode when the crew is incapacitated, distracted by other mission-critical tasks, or unable to respond in time to emergencies.

## 2.3 Communication Latency in Space

* During space missions, especially those based on distant planetary exploration (e.g., lunar or Mars missions), communication delays between the spacecraft and ground control can range from several seconds to minutes or longer.
* Autonomous systems ensure that critical functions and subsystem operations are maintained without needing real-time instructions from Earth.

## 2.4 Unpredictability of Space Environments

* Space conditions (e.g., micrometeoroid impacts, radiation storms, hardware anomalies) can trigger sudden system failures. Autonomous operation allows the spacecraft to respond in real-time to unexpected events, maintaining subsystem functionality that is essential for mission survival.
* This approach provides the system with built-in resilience to respond dynamically under such scenarios without waiting for human intervention.

## 2.5 Reduced Burden on Crew

* During emergencies or high-stress operational situations, astronauts benefit from autonomous systems actively managing critical functions and subsystems. This reduces the cognitive and physical load on the crew and allows them to focus on solving problems or evacuating if necessary.
* Autonomous systems decrease the risk of crew errors during high-pressure moments where manual control of all systems simultaneously may be impractical.

## 2.6 Compliance with Redundancy and Fail-Safe Design Principles

* Autonomous functionality is an extension of redundancy and fail-safe principles commonly used in engineering. This requirement complements the design philosophy of ensuring systems continue to operate under failure conditions, particularly for mission-critical and life-support systems.
* By integrating autonomous systems, the spacecraft reduces its dependency on a single point of failure (human or hardware).

## 2.7 Alignment with Long-Duration and Deep Space Missions

* As space exploration shifts toward long-duration missions (e.g., Mars missions or lunar colonization), the need for autonomous systems becomes even more pronounced. Crewed missions will increasingly require systems that can self-diagnose, self-repair, and self-operate for extended periods in isolation from Earth.
* Autonomous operation ensures mission sustainability and crew safety in scenarios where ground support is unavailable or infeasible.

## 2.8 Legal and Ethical Standards

* Space organizations, such as NASA and ESA, adhere to strict safety standards and ethical practices that prioritize minimizing risks to human life. Ensuring the availability of autonomous mechanisms aligns with these standards, demonstrating a commitment to astronaut safety and responsible mission design.

# 3. Guidance

For crewed vehicles, the loss of communication with Earth or an incapacitated crew must not compromise critical systems required to sustain life or prevent catastrophic events. The system must be capable of autonomously safeguarding itself without relying on mission control or crew intervention. This ensures crew safety even in conditions of communication loss or crew unavailability as outlined in NPR 8705.2.

By implementing these tasks, the software can ensure the functionality and safety of critical systems on a crewed vehicle, even during communication loss or crew incapacitation. These design and testing practices reduce mission risk, safeguard the crew, and provide redundancy against unforeseen failures or external hazards.

Definition: Autonomous Operations

The ability of a space system to independently perform critical operations without relying on Earth-based systems (e.g., mission control) or real-time support. Autonomous operations also include responding to anomalies or hazardous conditions while ensuring continuous proper functioning of critical systems.

## 3.1 Software Tasks for Autonomous Operations

To meet the requirement for autonomous operation of critical functions, the following key software engineering tasks must be considered:

### 3.1.1 Autonomous Control and Decision-Making Algorithms

* Develop and implement robust control algorithms capable of managing critical functions without human intervention.
* Test algorithms under all operational and off-nominal scenarios to validate safety and reliability.

### 3.1.2 Redundancy and Fault Tolerance

* Design and implement redundancy and fault-tolerant mechanisms to ensure uninterrupted operation of critical functions in the presence of faults or failures.
* Include backup systems and automated failover capabilities.

### 3.1.3 Real-Time Monitoring and Diagnostics

* Integrate real-time monitoring tools to continuously assess the health and status of critical systems and subsystems.
* Enable automated anomaly detection and responsive mitigation to prevent escalation into catastrophic events.

### 3.1.4 Safety and Failure Analysis

* Apply safety analysis techniques, such as:
  + **Software Fault Tree Analysis (SFTA)**
  + **Software Failure Modes and Effects Analysis (SFMEA)** See [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis)
* Use these techniques to identify hazards, failure modes, and mitigations for autonomous functions.

### 3.1.5 Software Change Safety Reviews

* Conduct safety reviews for all software changes, including defect fixes or updates, to verify that:
  + Fault redundancy and recovery mechanisms remain intact.
  + No new vulnerabilities or risks are introduced.

### 3.1.6 Independent Verification and Validation (IV&V)

* Perform rigorous independent verification and validation to ensure:
  + Autonomous systems meet specified safety and mission requirements.
  + Proper functionality is maintained under nominal and off-nominal conditions.
* IV&V activities should include:
  + Participation in reviews, inspections, and testing.
  + Monitoring IV&V metrics to ensure continuous quality improvement.

### 3.1.7 Simulation and Testing

* Conduct extensive simulations and scenario testing, including:
  + Nominal and off-nominal conditions.
  + Failure scenarios, edge cases, and boundary conditions.
* Involve the flight operations team in simulations to ensure realistic testing of scenarios that may require autonomous actions.

### 3.1.8 Code Coverage with MC/DC Criterion

* Achieve 100% code coverage for all safety-critical software components using the **Modified Condition/Decision Coverage (MC/DC)** standard. See Topic [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements).
* Develop and execute test cases for:
  + Normal operations, failure modes, and fault recovery.
  + Detection, isolation, and autonomous recovery from failures.

### 3.1.9 Configuration and Version Management

* Implement robust configuration management processes to ensure the correct versions of software and configurations are used.
* Guard against errors caused by inconsistent or outdated software changes that could impair autonomous operations.

### 3.1.10 Error Handling and Recovery Mechanisms

* Design robust error handling mechanisms to autonomously detect, report, and recover from faults.
* Ensure that these systems can handle errors without leading to hazardous or catastrophic events.

### 3.1.11 Operator Training and User Documentation

* Provide clear documentation, including a comprehensive User Manual, to help operators:
  + Understand system status, error messages, and recovery behavior.
  + Interpret system logs and take corrective actions (if necessary).
* Include training materials on system responses, fault recovery mechanisms, and interpreting autonomous behaviors.

## 3.2 Implementation Support

* Refer to Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for further details on safety-critical software requirements.
* Consult NPR 8705.2 [024](#_tabs-<p></p>) for additional definitions and alignment with human-rating standards.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Requirements related to Human Rated Software.

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

When addressing this requirement for small projects, the approach should focus on simplicity, scalability, and efficiency while still ensuring mission safety and compliance. Below is tailored guidance specifically for small projects, emphasizing minimal resources while maintaining high reliability.

Ensure autonomous functionality for critical systems in a cost-effective and scalable manner, enabling the system to safeguard itself against catastrophic events even in the absence of external communication or available crew.

Small projects can meet this requirement effectively by focusing on critical systems, employing lightweight design and testing methods, and leveraging external tools where necessary. By following these principles, even resource-constrained projects can achieve safe and reliable autonomous operation of systems crucial to the crew’s survival. This approach maintains compliance with human-rated software standards while minimizing complexity and effort.

## 4.1 Key Simplified Strategies

### 4.1.1 Focus on Priority Systems

For small projects with constrained resources, identify and prioritize *essential functions* that directly protect the crew and maintain mission-critical conditions (e.g., life support, power systems, thermal control).

* Perform a **Critical Systems Identification** analysis to categorize functions based on their impact on crew safety and mission success. For example:
  + Life support systems (e.g., oxygen generation, CO₂ removal).
  + Power systems (e.g., ensuring uninterrupted electricity to critical subsystems).
  + Navigation and attitude control systems (e.g., maintaining proper spacecraft orientation to prevent damage or loss of control).

### 4.1.2 Streamlined Redundancy Approach

Small projects cannot afford extensive redundancies, but core critical systems must be equipped with:

* **Basic passive redundancy:** Essential backup systems that kick in automatically in the event of primary system failure.
* **Simpler fault-tolerant designs:** Incorporate error detection with pre-programmed responses (e.g., switching to backup circuits or performing predefined safe shutdown sequences).

### 4.1.3 Software Design Principles

* Develop lightweight **autonomous control algorithms** focused on directly safeguarding priority systems.
* Encode basic "if-then" logic or decision trees for anomalies, ensuring critical system recovery actions can execute without complex reasoning.
* Use modular software design to allow future scalability or extensions while staying manageable in early project phases.

### 4.1.4 Limited Real-Time Monitoring

For small projects, real-time monitoring can be streamlined:

* Focus monitoring and diagnostics specifically on *catastrophic-event-related parameters* (e.g., internal pressure, life support flow rates, battery health).
* Utilize lightweight anomaly detection methods and hard-coded thresholds that trigger immediate autonomous corrective actions.

### 4.1.5 Lightweight Safety Analysis

To minimize effort in safety analysis processes while ensuring thoroughness, perform small-scale versions of:

* **Software Fault Tree Analysis (SFTA):** Identify the simplest paths leading to catastrophic failures.
* **Failure Modes and Effects Analysis (FMEA):** Quickly evaluate which system and software failures must be mitigated and design straightforward responses.
* Use checklists or templates suited to small projects to minimize complexity in documentation and execution.

### 4.1.6 Simplified Testing and Simulation Procedures

For small projects, prioritize achievable simulation and testing based on resource constraints:

* Develop test cases in stages, starting with normal operation scenarios followed by basic failure scenarios for autonomous responses.
* Use low-cost simulation environments to verify software behavior under nominal and failure conditions, including communication loss and incapacitated crew situations.
* Conduct integration tests with hardware prototypes only for priority systems.

### 4.1.7 Code Coverage with Practical Tools

Per the Modified Condition/Decision Coverage (MC/DC) criterion for safety-critical software, implement basic testing practices:

* Focus on achieving high code coverage for mission-critical systems functions only (e.g., failure detection routines, autonomous corrective actions).
* Use open-source or affordable testing tools designed for small projects to verify code adequacy.

### 4.1.8 Minimal Configuration Management

Small projects benefit from lightweight configuration management tools:

* Use simple version control systems (e.g., Git) to manage software changes.
* Maintain clear documentation of configuration details for autonomous systems to prevent mismatches or errors.

### 4.1.9 Error Handling and Minimal Recovery Mechanisms

Simplify error handling systems by:

* Defining straightforward recovery sequences for critical faults.
* Using "safe modes" with predefined autonomous actions that deactivate nonessential systems while protecting mission-critical functions.

### 4.1.10 Leverage External Tools and Resources

Small-scale projects may lack extensive resources for independent verification and validation (IV&V) or simulations. As a result:

* **Contract or leverage external support** from industry partners with expertise in safety-critical space software.
* Use commercial off-the-shelf (COTS) software tools designed for safety-critical systems if available.
* Involve oversight teams for periodic technical reviews to ensure compliance with human-rating standards.

## 4.2 Additional Best Practices

* **Developer Collaboration:** Ensure developers thoroughly understand the minimal scope of critical systems and autonomous requirements early in the design phase.
* **Streamlined Documentation:** Document key autonomous functionality and safety mechanisms in a simple format to streamline internal reviews and audits.
* **Training and Operator Support:** Provide clear training materials and manuals that describe autonomous system behaviors and fault recovery mechanisms for easy onboarding.

## 4.3 Checklist for Small Projects

1. **Critical Functions Identified**: Life-support, power supply, navigation/attitude control.
2. **Autonomous Safeguarding Logic** Defined and Encoded.
3. **Basic Redundancy Designed**: Simple fallback systems and failover mechanisms.
4. **Safety Analysis Completed**: Streamlined versions of SFTA/FMEA.
5. **Testing Performed**: Nominal and off-nominal scenarios simulated.
6. **Monitoring Parameters Specified**: Select critical metrics for diagnostics and anomaly detection.
7. **Software Validated**: Tests focused on MC/DC-critical areas.
8. **Documentation Updated**: User guides for autonomous behaviors.

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

To address Requirement 4.3.9, “The crewed space system shall provide the capability for autonomous operation of system and subsystem functions which, if lost, would result in a catastrophic event,” it is essential to draw from real-world lessons learned by NASA. These lessons come from past missions and focused studies, emphasizing the importance of autonomy in ensuring crew safety and mission success during critical or unforeseen conditions. Below are some NASA lessons learned associated with this requirement, which provide insight into why it is critical and how to address it effectively.

---

### **1. Apollo 13 (1970): Importance of Autonomous Capability for Critical Systems**

**Lesson Learned:** The explosion of an oxygen tank during the Apollo 13 mission highlighted the importance of having robust autonomous operational capabilities to safeguard critical systems. The incident disrupted life-support functions and power supply, requiring quick adaptation and the autonomous functionality of subsystems to maintain survival conditions.

**Takeaway:**

* Autonomous operations must ensure life-support systems can continue functioning independently of immediate ground intervention in the event of catastrophic hardware failure.
* Crew systems must offer built-in contingency modes that automatically prevent failure propagation (e.g., emergency oxygen routing or power rationing).

---

### **2. Mars Polar Lander (1999): Failure of Fault Detection and Recovery**

**Lesson Learned:** The Mars Polar Lander’s mission failed due to a software-generated spurious signal interpreted as a successful landing, resulting in premature engine cutoff and the spacecraft's destruction. This highlighted the need for robust fault detection and recovery mechanisms in autonomous systems.

**Takeaway:**

* Autonomy must rely on reliable fault detection algorithms to differentiate anomalies from nominal operations.
* Software must include fail-safe mechanisms to recover from incorrect commands or false-positive signals that could trigger catastrophic events.

---

### **3. Skylab (1973): Thermal Shield Deployment Failure**

**Lesson Learned:** During Skylab's deployment, a critical thermal protection system was damaged, leading to potentially life-threatening increases in onboard temperatures. Autonomous systems were unable to mitigate the thermal issues, and manual crew intervention (alongside rapid ground team problem-solving) was required to stabilize the spacecraft.

**Takeaway:**

* Autonomous systems should be capable of real-time reaction to environmental changes (e.g., overheating, radiation) and safeguard critical life-support conditions without requiring immediate ground or crew input.
* Systems should be designed to execute pre-programmed recovery modes that protect against catastrophic environmental impacts on hardware components.

---

### **4. Space Shuttle Challenger Disaster (1986): Automation and Monitoring**

**Lesson Learned:** The Space Shuttle *Challenger* disaster, caused by the failure of the O-ring seals in the solid rocket boosters, emphasized the need for continuous, autonomous real-time monitoring of critical components and integrated fail-safe mechanisms. Poor awareness of system failures in real time led to catastrophic consequences.

**Takeaway:**

* Systems must include automated health monitoring that detects faults, predicts anomalies, and initiates autonomous safing or shutdown mechanisms before catastrophic chain reactions occur.
* Continuous diagnostics and redundancy should be prioritized for high-risk systems.

---

### **5. International Space Station (ISS): Autonomous Life-Support Systems**

**Lesson Learned:** The ISS has faced multiple instances where autonomous life-support system functions were critical for maintaining air quality and pressure—such as in managing CO₂ removal with the Carbon Dioxide Removal Assembly (CDRA) and handling ammonia leaks from thermal control systems. Quick autonomous responses prevented threats to crew safety when external communication delays or crew workload made immediate interventions impractical.

**Takeaway:**

* Autonomous operation of life-support systems (e.g., oxygen, CO₂ removal, temperature management) is essential for ensuring crew safety during anomalies.
* Systems undergoing frequent wear and tear must have fault-tolerant autonomous processes, enabling basic life-support operations without the need for ground control intervention.

---

### **6. Mars Rover Spirit and Opportunity (2004–2019): Redundant and Autonomous Operations**

**Lesson Learned:** NASA's Mars rovers demonstrated the importance of autonomous operations for long-distance exploration. Spirit overcame significant challenges with its wheel failure and dust storms, where autonomy allowed it to continue its mission by redistributing power and reprogramming mobility strategies without real-time control from Earth.

**Takeaway:**

* Autonomous systems must be able to detect failures in real time and adapt operations (e.g., power redistribution, safing protocols) to maintain mission-critical functions.
* Redundant hardware and failover mechanisms are essential to ensure continuity of operations when primary systems fail.

---

### **7. Columbia Accident (2003): Monitoring Heat Shields**

**Lesson Learned:** The Space Shuttle *Columbia* was lost upon reentry due to damage to its heat shield caused during launch. Limited autonomous diagnostic capability on the shuttle's thermal protection system (TPS) prevented early detection of the issue, which could have been addressed had it been identified sooner.

**Takeaway:**

* Autonomous systems must constantly monitor critical subsystems (e.g., thermal protection, cabin pressure) and detect early signs of damage that could lead to catastrophic events.
* Fault detection thresholds for high-risk systems should be conservative, prioritizing crew safety over system operational continuity.

---

### **8. Artemis I Predecessors: Early Lunar Programs**

**Lesson Learned:** Failures in early lunar missions highlighted the importance of autonomous spacecraft for lunar and deep-space missions. As communication delays make real-time intervention challenging, systems must independently manage mission- and life-critical functions.

**Takeaway:**

* Autonomous systems must operate with minimal reliance on Earth-based mission control in deep space scenarios.
* For crewed missions, redundancy and fault tolerance become non-negotiable design principles to maintain autonomy when crew or Earth intervention is unavailable.

---

### **9. Mars Climate Orbiter (1999): Importance of Software Validation**

**Lesson Learned:** The Mars Climate Orbiter mission failed due to improper unit conversions between software subsystems (metric vs. imperial units), leading to a trajectory error. This mission underscores the importance of independent verification and validation (IV&V) to ensure software functionality and safety for autonomous systems.

**Takeaway:**

* Rigorous testing and IV&V are essential for autonomous systems, verifying that the software operates correctly in all scenarios.
* Autonomous software logic must be validated to ensure seamless integration across subsystems and eliminate design inconsistencies.

---

### **Key Lessons Consolidated**

1. **Critical Redundancy:** Ensure every critical function has autonomous fail-safe and fallback capabilities.
2. **Fault Tolerance:** Software must include real-time anomaly detection, error-handling, and autonomous recovery mechanisms.
3. **Real-Time Monitoring:** Implement diagnostics that detect hazardous conditions early and initiate recovery actions without requiring ground intervention.
4. **Validation and Testing:** Perform independent verification and validation (IV&V) to ensure compliance with safety standards, reducing the risk of software failures.
5. **Environmental Resilience:** Design systems to withstand environmental hazards (e.g., overheating, radiation, micrometeoroids) without immediate crew or mission control input.
6. **Edge Case Coverage:** Test for all foreseeable nominal and off-nominal scenarios, particularly conditions where communication or human input is unavailable.

---

### **Conclusion**

NASA's lessons learned underscore the importance of robust autonomous systems to prevent catastrophic failures during crewed missions. Past incidents and challenges emphasize the need for redundancy, fault-tolerant algorithms, real-time monitoring, and IV&V to ensure that critical systems can function independently, safeguarding the crew and mission under the most adverse conditions.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-39 - Autonomous Operation**

4.3.9 The crewed space system shall provide the capability for autonomous operation of system and subsystem functions which, if lost, would result in a catastrophic event.

By implementing these Software Assurance deliverables, metrics, and tasks, the crewed system will achieve robust and reliable autonomous control capabilities. Adhering to NASA safety and procedural standards (e.g., NASA-STD-8739.8, NPR 7150.2) and leveraging lessons learned will ensure that fault detection, isolation, and recovery are successfully implemented—mitigating risks to crew safety and mission success. This approach guarantees resilience against faults and failures while addressing the unique challenges of autonomous operations.

## 7.1 Tasking for Software Assurance

1. Ensure the development, implementation, and testing of robust autonomous control algorithms capable of managing critical functions without human intervention. These algorithms must undergo thorough testing to guarantee their reliability and safety in all operational scenarios.
2. Ensure redundancy and fault tolerance is included in the design so that critical functions continue to operate autonomously, even in the presence of faults or failures. This includes implementing backup systems and failover mechanisms.
3. Ensure that integrated real-time monitoring and diagnostic tools are used to continuously assess the health and status of critical systems and subsystems. These tools should detect anomalies and trigger autonomous responses to mitigate potential catastrophic events.
4. Employ safety analysis techniques such as [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) and [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) to identify potential hazards and failure modes. This helps in designing controls and mitigations for the autonomous operation of critical functions.
5. Ensure comprehensive test coverage for all autonomous operation scenarios, including normal operations, failure modes, and recovery scenarios, to verify that these functions operate correctly and reliably. This includes testing for unexpected situations and boundary conditions.
6. Confirm that strict configuration management to ensure that the correct software versions and configurations are used. This reduces the risk of errors due to incorrect or inconsistent configurations that could impact autonomous operations.
7. Ensure robust error handling and recovery mechanisms to address errors stemming from detected faults. This ensures that error handling is adequate and that the system can autonomously recover from errors without leading to hazardous or catastrophic events.
8. Perform safety reviews on all software changes and software defects.
9. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.
10. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically that the autonomous control systems can handle all nominal and off-nominal scenarios without human intervention. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks). Ensure that the project has developed and executed test cases to test the software system’s recovery from faults.
11. Analyze the software test procedures for the following:
    1. Coverage of the software requirements.
    2. Acceptance or pass/fail criteria,
    3. The inclusion of operational and off-nominal conditions, including boundary conditions,
    4. Requirements coverage and hazards per [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) and [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), respectively.
12. Perform test witnessing for safety-critical software to ensure that the autonomous control systems can handle all nominal and off-nominal scenarios without human intervention.
13. Confirm that test results are sufficient verification artifacts for the hazard reports.
14. Ensure comprehensive training and documentation for operators is available.

## 7.2 Software Assurance Products

Guarantee that software supporting critical autonomous operations in crewed systems is reliable, safe, and capable of independently managing functions that, if lost, would lead to catastrophic events. The following Software Assurance (SA) tasks, processes, and metrics provide a comprehensive approach to meet this requirement, ensuring appropriate verification, validation, and safety analyses.

The following deliverables must be completed and maintained throughout the software lifecycle:

### 7.2.1 Core SA Deliverables:

1. **Software Assurance Status Reports (** [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports)): Regular status updates documenting findings, risks, and progress for autonomous system assurance activities.
2. **Requirements Analysis (** [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis)): Validation that system and software requirements for autonomous operations meet safety and reliability standards.
3. **Design Analysis** ( [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis)**):** Verification that the software design aligns with system-level autonomous functionality.
4. **Source Code Quality Analysis (** [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis)**):** Assurance that the code adheres to safety, maintainability, and reliability standards.
5. **Test Analysis** ( [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis)): Evaluations ensuring testing adequately addresses all autonomous operation scenarios.
6. **Software Safety and Hazard Analysis (** [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis)**):** Comprehensive identification of hazards and mitigation through software design and implementation.
7. **Audit Reports (** [8.59 - Assessment Schedule](/spaces/SWEHBVD/pages/203391032/8.59+-+Assessment+Schedule)**):** Functional (FCA) and Physical (PCA) Configuration Audits verifying the software matches design documentation and mission requirements.
8. **Peer Review Findings:** Results from peer reviews of safety-critical autonomous systems and associated software changes.

### 7.2.2 Hazard Analysis and Software Safety:

* **Hazard Reports (**Topic [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content)**):** Fully document hazards, their control mechanisms, and results of safety mitigations for software-related risks.
* **Software Fault Tree Analysis (FTA) & Failure Modes and Effects Analysis (FMEA) (**[8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis), [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis)**):** Use these methods to identify failure modes, hazards, and mitigation strategies for faults jeopardizing critical operations.
* **Verification Artifacts:** Ensure hazard mitigations are properly verified and backed by traceable test results.

### 7.2.3 Testing and Verification:

* **Test Witnessing Signatures (** [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)**):** Sign-off ensuring tests fully validate software’s autonomous fault detection, isolation, and recovery capabilities.
* **Code Coverage Verification (** [S](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements)[WE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) **):** Confirm that testing addresses 100% of safety-critical paths, or document rationale for any exceptions.

### 7.2.4 Configuration Management:

* Maintain strict control over software versions, artifacts, hazard reports, and safety analyses ( [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items), [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items)).

## 7.3 Software Assurance Metrics

Metrics are essential in tracking the safety and reliability of autonomous software. Below are key categories, their respective purposes, and example metrics:

### 7.3.1 Verification and Validation Metrics:

* **Test Coverage:** Measure the percentage of autonomous operation scenarios verified (e.g., normal, failure, recovery modes).
* **Defect Density:** Track defects per thousand lines of code for safety-critical components.
* **Requirements Traceability:** Ensure full traceability from software requirements to implementation and test cases.
  + Metric: % of requirements traced to test procedures.

### 7.3.2 Safety Metrics:

* **Hazard Analysis:** Track hazards identified, controlled, and tested systematically.
  + Metric: % of hazards mapped to mitigations with verified test cases.
* **Non-Conformances:** Monitor open vs. resolved safety-critical non-conformances discovered during testing.
  + Metric: # of safety-related non-conformances by severity.

### 7.3.3 Performance Metrics:

* **Response Time to Faults:** Measure how quickly the system detects and mitigates faults autonomously.
* **System Availability:** Ensure autonomous critical systems meet uptime requirements, especially during mission-critical phases.

### 7.3.4 Quality Metrics:

* **Code Complexity:** Monitor cyclomatic complexity values and static analysis outcomes for maintainability.
* **Code Churn:** Track code modifications to identify stability or rapidly changing risky areas.

### 7.3.5 Configuration Management Metrics:

* **Version Control Compliance:** Measure adherence to configuration management (CM) policies.
  + Metric: % of approved artifacts under CM.
* **Change Requests:** Track the impact of changes to autonomous capabilities through defect and change request management.

### 7.3.6 IV&V Metrics:

* **Coverage Metrics:** Assess the completeness of independent verification and validation for autonomous system requirements.
  + Metric: % of safety-critical codepaths independently verified.
* **IV&V Participation:** Track involvement in design reviews, test witnessing, and simulations.

### 7.3.7 Training Metrics:

* **Training Completion Rates:** Monitor training progress for team members in autonomous control system development and testing.

## 7.4 Software Assurance and Safety Tasks

### 7.4.1 Assurance of Autonomous Control Algorithms

* Verify algorithms can independently manage critical functions without human intervention.
* Ensure extensive simulation and boundary testing of all critical scenarios, including nominal and off-nominal operations.

### 7.4.2 Redundancy and Fault Tolerance Assurance

* Confirm that backup systems and failover mechanisms are designed, tested, and validated for critical autonomous operations.
* Verify that software supports autonomous fault detection and recovery to prevent catastrophic events.

### 7.4.3 Software Safety and Hazard Analysis

* Conduct **Software Safety Analysis (**Topic [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis)**)** to identify risks associated with critical functions.
  + Examples: Evaluate hazard controls such as isolation, redundancy, or failover responses.
* Perform safety reviews for requirement changes or defect fixes to ensure they don’t compromise autonomy of critical operations.

### 7.4.4 Test Planning and Witnessing

* Validate test plans and procedures related to safety-critical autonomy, ensuring they address detection, isolation, and recovery of all identified hazards.
* Witness critical tests to ensure adherence to test requirements and autonomous fault recovery goals.

### 7.4.5 Configuration and Documentation Assurance

* Verify all software supporting autonomous operations is captured and tracked via configuration management (SWE-187, SWE-081).
* Maintain updated safety-critical documents (e.g., hazard reports, FTAs, FMEAs).

### 7.4.6 Independent Verification and Validation (IV&V)

* Engage IV&V early in the development lifecycle, ensuring autonomous functionality meets safety and mission-critical standards.
* Include IV&V assessments in reviews to provide independent perspectives and thorough evaluation.

### 7.4.7 Training and Operator Support

* Ensure developers, testers, and operators understand emergent behaviors and limitations of the autonomous systems via training programs and user documentation.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence is critical for demonstrating compliance with the requirement that **“The crewed space system shall provide the capability for autonomous operation of system and subsystem functions which, if lost, would result in a catastrophic event”** (Requirement 4.3.9). Objective evidence consists of artifacts, observations, and test results that verify the software and systems meet the specified requirements for autonomous critical systems. This provides auditable proof of compliance and mitigates risk by ensuring that critical functions operate reliably and independently.

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

Below is a structured list of objective evidence that supports this requirement, organized by key assurance categories.

## 8.1 Software Requirements Evidence

#### **Documentation:**

* **System Requirements Specifications (SRS):**
  + Evidence that system-level autonomous operation requirements for critical functions are fully defined and meet safety and mission-critical needs.
  + Traceability matrix linking these high-level system requirements to lower-tier software requirements.
* **Software Requirements Specifications (SWRS):**
  + Detailed documentation of software-level requirements derived from or supporting the system autonomy goals.

#### **Verification Artifacts:**

* **Requirements Traceability Matrix (RTM):**
  + Demonstrates end-to-end traceability between system-level autonomous operation requirements, software requirements, software design, test plans, and test results.
  + Includes traceability to associated hazard reports and safety-critical requirements.

## 8.2 Software Design Evidence

#### **Documentation:**

* **Software Design Description (SDD):**

  + Evidence of how the software architecture and control algorithms enable autonomous operations without human intervention during both nominal and off-nominal scenarios.
  + Block diagrams, flow charts, and data flow diagrams illustrating autonomous signal processing, decision-making algorithms, and execution.
* **Embedded Fault Detection & Response Design:**

  + Description of mechanisms for fault detection, isolation, and recovery (FDIR) processes within safety-critical autonomous functions.
  + Evidence of redundancy designs (e.g., primary and backup systems, failover transitions).
* **Failure Propagation Analysis:**

  + Analysis of how the software design prevents single-point failures or cascading faults from causing catastrophic consequences.

#### **Verification Artifacts:**

* Design review reports (e.g., Preliminary Design Review [PDR], Critical Design Review [CDR]).
* Results from peer design evaluations for autonomous control and fault-tolerant subsystems.
* Updated design documentation following review feedback.

## 8.3 Implementation/Source Code Evidence

#### **Artifacts:**

* **Source Code Documentation:**

  + Code repository snapshots with evidence of autonomous control logic implementation.
  + Evidence of error handling mechanisms supporting fault tolerance (e.g., redundant execution paths, self-checking routines).
* **Source Code Quality Analysis Reports:**

  + Results from static analysis tools showing adherence to coding standards (e.g., MISRA, NASA coding standards).
  + Code complexity metrics (cyclomatic complexity) and identification of critical areas requiring further assurance.
* **Code Coverage Reports:**

  + Detailed results showing the percentage of autonomous functions executed during testing.
  + Evidence satisfying Modified Condition/Decision Coverage (MC/DC) for safety-critical paths.

## 8.4 Validation and Testing Evidence

#### **Test Artifacts:**

* **Test Plans:**

  + Evidence that the test plans include validation of autonomous operation scenarios, such as:
    - Nominal operations.
    - Nominal faults that trigger recovery.
    - Off-nominal fault propagation scenarios that require failover operation.
    - Loss of communication or delayed ground intervention.
* **Test Procedures and Cases:**

  + Test procedures specifically for evaluating critical system autonomy (e.g., fault detection, degraded modes, failover operation, safing procedures).
  + Test coverage demonstrating that all critical functions are validated under nominal and fault scenarios.
* **Test Results and Reports:**

  + Evidence showing successful execution of test cases for:
    - Automated fault detection and recovery within specified response times.
    - Autonomous handling of catastrophic failure scenarios (e.g., cabin depressurization, life-support interruptions).
  + Reports should document anomalies, resolutions, and re-testing for closure.

#### **Simulation Results:**

* Evidence of tests conducted in a simulated operational environment, including boundary and stress conditions.
* Results from hardware-in-the-loop (HIL) or software-in-the-loop (SIL) tests that validate autonomous operation in mission-like scenarios.

#### **Test Witnessing:**

* Evidence of Software Assurance and IV&V witness participation in tests (signatures or reports confirming adherence to test protocols).

## 8.5 Safety and Hazard Analysis Evidence

#### **Safety Analysis Reports:**

* **Hazard Analysis Reports (HAR):**
  + Evidence identifying hazards related to loss of critical autonomy with associated hazard mitigations (e.g., redundancy, fault tolerance).
* **Hazard Tracking Log:**
  + Evidence of all hazards being tracked and mitigated to acceptable residual risk levels.
* **Analysis Techniques:**
  + Completed **Software Fault Tree Analysis (FTA):** Evidence of a systematic risk analysis identifying fault propagation paths.
  + Completed **Software Failure Modes and Effects Analysis (FMEA):** Includes mitigation strategies for failure scenarios threatening system autonomy.

#### **Safety Certification:**

* Certificates or management approval confirming compliance with safety-critical requirements.

## 8.6 Independent Verification and Validation (IV&V) Evidence

#### **IV&V Artifacts:**

* **IV&V Analysis Results:**
  + Evidence showing independent verification of autonomous control logic against requirements.
  + Reports detailing IV&V participation in all major reviews and tests.
* **IV&V Test Report:**
  + Validation of safety-critical software paths, fault-tolerant algorithms, and autonomous operation recovery scenarios.

#### **Review and Inspection Reports:**

* Reports from IV&V participation in design reviews, code inspections, and test witnessing activities.

## 8.7 Configuration Management Evidence

#### **CM Artifacts:**

* Configuration management (CM) records showing proper versioning and tracking of:
  + Software modules related to critical autonomous functions.
  + Embedded test cases and test results.
  + FTA, FMEA, and hazard reports.
* Change request logs showing all updates to autonomous features and their evaluation for safety and reliability.

## 8.8 Operational Training and Documentation Evidence

#### **Training Evidence:**

* Training completion records for personnel involved in operating and monitoring the autonomous systems.

#### **User Manuals:**

* Documentation that clearly explains the behavior of autonomous systems, fault recovery, and fail-safe modes for operators.

## 8.9 Summary of Objective Evidence

The following table summarizes the key artifacts needed for auditing compliance with Requirement 4.3.9:

| Category | Objective Evidence Examples |
| --- | --- |
| **Requirements** | SRS, SWRS, RTM |
| **Design** | SDD, FDIR design, redundancy analysis, reviews |
| **Implementation** | Code snapshots, static analysis reports, code coverage results |
| **Validation & Testing** | Test plans, procedures, results, coverage reports, test witnessing |
| **Safety/Hazard Analysis** | HAR, FTA, FMEA reports, mitigation tracking |
| **IV&V** | IV&V reports, test witnessing, independent design reviews |
| **Configuration Management** | Configuration audits, version logs, CR logs |
| **Operational Evidence** | Training records, user documentation |

By collecting these artifacts, a project can comprehensively demonstrate that all elements of autonomy for safety-critical systems have been properly implemented, analyzed, tested, and validated. This ensures compliance with the requirement and safeguards mission success.
