# HR-38 - Data Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 171508210. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508210/HR-38+-+Data+Analysis

HR-38 - Data Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508210/HR-38+-+Data+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=171508210)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=171508210&showCommentArea=true&showComments=true#addcomment)

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

4.3.8 The space system shall provide the capability to utilize health and status data (including system performance data) of critical systems and subsystems to facilitate anomaly resolution during and after the mission.

## 1.1 Notes

NASA-STD-8719.29, NASA Technical Requirements for Human-Rating, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: HR-38 History

HR-38 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.3.8 The space system shall provide the capability to utilize health and status data (including system performance data) of critical systems and subsystems to facilitate anomaly resolution during and after the mission. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

Access to health and status data is a key element of anomaly resolution during the mission, which could prevent the crew from executing an abort or prevent the situation from developing into a catastrophic event. Resolving anomalies between missions is just as important. This requirement intentionally does not specify a crash-survivable data recorder. That determination is left for the program. The program also determines what data should be available to facilitate anomaly resolution.

Anomaly resolution is critical for ensuring the success, safety, and longevity of space missions, especially when dealing with complex systems operating in remote and extreme environments. The capability to gather, analyze, and act on health and status data of critical systems and subsystems serves as the foundation for detecting and resolving anomalies that could compromise mission objectives, spacecraft integrity, or crew safety.

This requirement provides the necessary infrastructure and processes to enable mission teams to quickly diagnose and respond to anomalies, leveraging real-time and post-mission data analysis to support operational decisions and improve future mission designs.

The rationale for this requirement is clear: Utilization of health and status data is indispensable for effective anomaly resolution during and after the mission, ensuring system resilience, safety, and operational continuity. By systematically collecting and analyzing health and performance data from critical systems and subsystems, space missions can respond proactively to anomalies, preventing catastrophic failures and extending their operational lifespan. The lessons learned and benefits derived from utilizing this data pave the way for safer and more reliable space missions in the future.

## 2.1 Ensuring Mission Success

Space missions involve systems and subsystems that are subjected to challenging environmental conditions, including radiation, temperature extremes, and mechanical stress. Critical systems (e.g., propulsion, communication, power generation, life support, etc.) must be monitored continuously to ensure they function reliably. Health and status data provide essential information to:

* Detect system degradation or faults before they result in mission-critical failures.
* Diagnose anomalies in real time and prevent the escalation of minor faults into catastrophic events.
* Enable quick decision-making during emergencies by providing detailed insights into subsystem performance.

## 2.2 Supporting Safety and Reliability

For crewed missions, ensuring the safety of astronauts is paramount. For uncrewed missions, spacecraft reliability is critical to protecting scientific payloads and achieving mission objectives. Health and status data help:

* **Prevent cascading failures**: Detailed monitoring allows faults in one subsystem to be quickly isolated, preventing them from propagating and affecting other subsystems.
* **Facilitate rapid recovery**: A continuous flow of performance and health data enables effective and timely anomaly resolution, bringing systems back to stable states faster.
* **Enhance redundancy utilization**: By quickly identifying degraded systems, health monitoring enables redundant systems to be activated or reconfigured to maintain mission continuity.

## 2.3 Driving Operational Efficiency

The access to accurate health and status data improves decision-making during mission operations by enabling anomaly resolution with minimal disruption:

* **Real-time resolution**: System telemetry provides operators with actionable insights to mitigate anomalies during the mission without halting operations.
* **Post-mission analysis**: Historical health data supports thorough failure analysis to identify root causes and generate solutions that improve the design and reliability of future missions.
* **Reduced downtime**: Leveraging performance data ensures systems are operational during their critical phases (e.g., launch, landing, or scientific data collection).

## 2.4 Enhancing Fault Detection and Performance Monitoring

The utilization of health data provides deeper insight into system behavior, enabling proactive anomaly detection:

* **Failure Prediction**: Advanced monitoring can detect subtle trends indicative of future failures, enabling anomaly resolution before issues arise.
* **Operational Optimization**: Health data allows mission planners to identify inefficiencies and optimize system performance, conserving resources such as fuel or power.

## 2.5 Autonomous Operations

As missions increasingly operate in deep-space environments, autonomy becomes vital. Health and status data are essential for autonomous systems to:

* **Detect anomalies**: Autonomous spacecraft rely on real-time health monitoring to identify and react to failures in their subsystems.
* **Perform corrective actions**: Performance data enables onboard systems to take preprogrammed corrective measures, ensuring mission continuity in low-latency or communication blackout scenarios.
* **Support ground teams remotely**: In cases where an anomaly exceeds autonomous resolution capabilities, detailed telemetry enables ground teams to more effectively diagnose and resolve the issue.

## 2.6 Post-Mission Benefits

Beyond mission completion, utilizing health and performance data ensures long-term benefits for future space systems:

* **Root Cause Analysis**: Health monitoring data provides engineers with a detailed record of system behaviors leading up to anomalies, enabling in-depth post-mission failure investigations.
* **Improved Designs**: Lessons learned from health data analysis can inform better designs for future spacecraft by addressing recurring issues or improving system redundancy.
* **Mission Cost Optimization**: Leveraging historical data minimizes the risk of repeating the same failures and reduces lifecycle costs by improving system reliability.

## 2.7 Connection to NASA Standards and Best Practices

NASA missions have repeatedly demonstrated the importance of real-time health monitoring for anomaly resolution. For instance:

* **Apollo 13 ("Houston, we’ve had a problem")**: Health and status telemetry data were vital in diagnosing the explosion in the oxygen tanks and supporting resolution strategies that brought the crew home safely.
* **Mars Pathfinder Anomalies**: Health data enabled ground teams to identify a resource conflict in its software and implement corrective measures remotely.
* **James Webb Space Telescope (JWST)**: Complex deployment sequences relied heavily on subsystem health telemetry to validate successful steps and quickly address anomalies in real time.

The Software Assurance and Software Safety Standard (NASA-STD-8739.8) emphasizes the importance of accurate health and status data for detecting and mitigating hazards in mission-critical software.

## 2.8 Technical Implementation Considerations

To meet this requirement, the system should:

1. **Provide Comprehensive Instrumentation**:
   * Ensure telemetry systems continuously collect detailed health data (e.g., power levels, sensor readings, thermal states, network errors).
2. **Support Data Storage and Retrieval**:
   * Enable real-time and historical access to performance data for anomaly detection and advanced post-mission analysis.
3. **Include Fault-Tolerant Data Systems**:
   * Equip spacecraft with fault-tolerant data generation, collection, and communication subsystems to limit data loss during anomalies.
4. **Promote Ground-Operator Accessibility**:
   * Deliver actionable information using health monitoring dashboards accessible by mission controllers.
5. **Establish Recovery Protocols**:
   * Build automated and manual resolution processes that leverage health data for fault isolation, troubleshooting, and system reconfiguration.

# 3. Guidance

The ability to effectively utilize health and status data is critical for resolving anomalies during and after a mission. Proper design, implementation, analysis, testing, and training ensure that systems are equipped to prevent anomalies from escalating into catastrophic events or recurring issues. Below is enhanced guidance tailored to modern software engineering practices, addressing critical aspects of data management, verification, and operational readiness for anomaly resolution.

Access to and proper utilization of health and status data is critical for preventing issues from escalating into major mission risks. This data provides essential insight to:

* Detect anomalies during flight and enable real-time responses that safeguard mission objectives.
* Support post-mission analysis to identify root causes and improve future designs.
* Enable crew responses or autonomous correction mechanisms in missions with limited ground communication. This guidance emphasizes proactive and comprehensive software engineering practices to meet these objectives.

By implementing these software engineering practices:

1. The system will be equipped to handle anomalies during critical mission operations.
2. Post-mission analysis using health and status data will provide insights for improving future missions.
3. Automated tools and robust testing will minimize human error while improving operational efficiency and safety.

This guidance ensures the health and status data systems are designed with the necessary monitoring, detection, and resolution capabilities to meet mission reliability and safety standards.

## 3.1 Enhanced Software Tasks for Data Management

### 3.1.1 Data Collection and Monitoring

* **Task**: Implement mechanisms to collect and monitor real-time health and status data from all critical systems and subsystems. Data should include sensor outputs, telemetry streams, event logs, monitoring thresholds, and error diagnostics.
* **Key Considerations**:
  + Use fail-safe and redundant data pathways to minimize data loss during critical mission phases or faults.
  + Incorporate health monitoring interfaces (e.g., telemetry dashboards) that can display live and historical data for operator situational awareness.
  + Prioritize the collection of data relevant to known high-risk components or systems (e.g., power systems, thermal controls, propulsion systems).

### 3.1.2 Real-Time Data Analysis

* **Task**: Design software systems capable of ingesting telemetry and health data in real time, identifying abnormal patterns and unusual system behaviors.
* **Key Considerations**:
  + Utilize edge computing techniques to ensure real-time analysis on the spacecraft, reducing reliance on ground communication delays (key for deep-space missions).
  + Use signal processing techniques to filter noise from sensor data, ensuring accurate anomaly detection.
  + Establish normalization benchmarks for subsystems' health parameters, differentiating between transient anomalies and true degradation.

### 3.1.3 Anomaly Detection Algorithms

* **Task**: Design and implement advanced algorithms to automatically detect anomalies by analyzing telemetry streams and health data.
* **Key Features**:
  + **Machine Learning Models**:
    - Incorporate machine learning (ML) or pattern-recognition models to predict anomalies based on historical trends.
    - Use ML to differentiate between nominal responses and statistically significant deviation.
  + **Threshold-Based Logic**:
    - Define parameter-specific thresholds (e.g., voltage, temperature, pressure) for immediate anomaly flagging when limits are exceeded.
  + **Event Correlation**:
    - Include the ability to correlate events across systems to identify systemic anomalies caused by interaction faults.

### 3.1.4 Historical Data Analysis

* **Task**: Develop and integrate systems for long-term storage and retrieval of health and status data to enable in-depth post-mission analysis.
* **Key Considerations**:
  + Implement efficient data storage methods with compression to handle large amounts of telemetry data without information loss.
  + Enable data visualization tools (e.g., plotting tools) for operators to analyze trends.
  + Use playback capabilities to recreate past telemetry streams for training and failure analysis purposes.

### 3.1.5 Fault Isolation and Diagnosis

* **Task**: Software should incorporate fault diagnosis capabilities to isolate affected systems, pinpointing root causes of anomalies.
* **Key Considerations**:
  + Design systems to map telemetry faults to physical subsystems or software modules to streamline troubleshooting.
  + Employ automated diagnostic tools to recommend specific recovery actions based on pre-defined logic trees or historical resolutions.

### 3.1.6 Automated Response Systems

* **Task**: Implement automated response systems that execute predefined actions when anomalies are detected.
* **Key Features**:
  + Fault recovery logic to bring the system into a safe state.
  + Examples include automatic failover systems (e.g., backup servers, redundant paths), reconfiguration protocols, and hardware resets.
  + Support for command override by ground operators or crew for faults exceeding programmed recovery capabilities.

### 3.1.7 Data Verification

* Ensure data integrity using fault-tolerant communication protocols, error-checking algorithms (e.g., checksums, cyclic redundancy checks [CRC]), and redundant data comparison between subsystems.

### 3.1.8 Independent Verification and Validation (IV&V)

* **Role of IV&V**: Critically evaluate the systems, algorithms, and processes involved in anomaly detection and response to ensure compliance with mission requirements and safety goals.
* **Key IV&V Activities**:
  + **Technical Reviews**: Assess the adequacy and fidelity of data collection, anomaly detection, and automated response methods.
  + **Simulation Analysis**: Validate the system's response to a representative set of induced faults through simulations.
  + **Document Review**: Confirm consistency and completeness of anomaly-related documentation and processes.

### 3.1.9 Simulation and Testing

* **Comprehensive Fault Scenario Testing**:
  + Simulate expected anomalies and random faults to test the robustness of data collection, detection, and recovery systems under various stress conditions.
* **Validation Framework**:
  + Test hardware-in-the-loop (HIL) interfaces for sensor anomalies.
  + Include extreme edge cases (e.g., simultaneous telemetry faults, cascading failures).
* **Key Deliverable**: Evidence of system readiness for fault identification and resolution before deployment (test reports with metrics and results).

### 3.1.10 Code Coverage and MC/DC Testing

* **Objective**:
  + Achieve **100% Modified Condition/Decision Coverage (MC/DC)** to ensure all possible system states, decision paths, and control structures in critical fault-management software have been rigorously tested.
  + Include MC/DC for health data processing, anomaly flag triggers, and recovery algorithms.

### 3.1.11 Configuration Management

* **Ensure Strict Version Control**:
  + Track and manage versions of software tools used for telemetry capture, anomaly analysis, and fault resolution algorithms.
* **Key Considerations**:
  + Maintain a stable baseline but adapt software configurations if new risks or anomalies are discovered post-deployment.

### 3.1.12 Training and Documentation

* **Operator and Crew Preparedness**:
  + Deliver operators and crew a **comprehensive user manual** explaining telemetry interpretation, known fault responses, and recovery protocols. Include:
    - Recognized anomaly patterns and thresholds.
    - Primary and secondary resolution steps.
* **Training Simulations**:
  + Conduct training exercises simulating fault conditions to prepare personnel for anomaly interpretation and resolution during live missions.

## 3.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

Small projects typically operate with constrained resources, limited budgets, and shorter timelines, yet this requirement remains critical to the safe and successful operation of the system. Below is practical guidance tailored to small projects to meet this requirement effectively while optimizing resource use.

Small projects can meet this requirement by focusing on the essential health and status data tasks, prioritizing critical subsystems, leveraging simple tools and techniques, and streamlining processes. By focusing efforts on high-value activities and affordable solutions, small teams can ensure the system's safety and reliability while managing resource constraints.

## 4.1 Key Considerations for Small Projects

1. **Prioritize Critical Systems**:  
   Focus effort on monitoring and utilizing health and status data for the most mission-critical systems and subsystems to resolve anomalies effectively and prevent catastrophic events.
2. **Leverage Simple Architecture**:  
   Implement lightweight and scalable architectures tailored to small projects that can collect, analyze, and respond to data without over-complicating the system.
3. **Use Off-the-Shelf Tools Where Feasible**:  
   Take advantage of commercial off-the-shelf (COTS) hardware, open-source software tools, and reusable components to manage health data and anomaly resolution capabilities.
4. **Scale-Down Documentation Efforts**:  
   Maintain minimal but critical documentation. Focus on critical artifacts like a fault-handling playbook, test results, and configuration control to avoid unnecessary overhead.
5. **Iterative and Focused Testing**:  
   Concentrate testing efforts on high-probability anomaly scenarios while ensuring minimal coverage for less critical aspects.

## 4.2 Simplified Guidance for Small Projects

### 4.2.1 Data Collection and Monitoring

* **Approach**:
  + Identify and monitor key telemetry points (e.g., voltage, temperature, pressure) for *critical systems only* instead of all subsystems.
  + Use low-cost data acquisition tools or sensors to monitor system health, e.g., small microcontroller-based logging solutions (e.g., Arduino or Raspberry Pi).
* **Deliverables**:
  + A small set of key parameters to monitor for mission-critical functionality.
  + Simple periodic data logging to onboard memory or ground systems.

### 4.2.2 Real-Time Data Analysis

* **Approach**:
  + Restrict real-time analysis to top-priority anomaly scenarios (e.g., overheating, power loss, communication failure).
  + Use simple decision thresholds for triggers, such as *if voltage > threshold → flag anomaly*.
* **Tools**:
  + Utilize open-source libraries like Python’s NumPy or Pandas for basic data analysis to identify out-of-range values quickly.
* **Deliverables**:
  + A lightweight real-time monitoring system with hard-coded thresholds for actionable metrics.

### 4.2.3 Anomaly Detection Algorithms

* **Approach**:
  + Focus on rule-based algorithms (simple threshold limits) for anomaly detection instead of complex AI/ML models.
  + Example: Use **if-else rules** to detect anomalies in critical components like power and temperature.
* **Tools**:
  + Use algorithms built directly into lightweight onboard software systems.
* **Deliverables**:
  + A table of anomaly thresholds for each key subsystem.
  + Algorithm scripts to assess telemetry against basic rules.

### 4.2.4 Historical Data Analysis

* **Approach**:
  + Archive key health/status data for post-mission analysis on low-cost storage devices (e.g., SD cards) or via partial uplinks to the ground.
  + Use Excel, simple databases (e.g., SQLite), or cloud platforms for offline analysis.
* **Deliverables**:
  + Downloadable logs of critical anomalies and associated telemetry for later investigation.

### 4.2.5 Fault Isolation and Diagnosis

* **Approach**:
  + Tie known faults to pre-determined fault codes and recommend recovery actions through a library of fault-handling steps.
  + Simple tagging of telemetry with subsystem names allows for quick isolation.
* **Deliverables**:
  + Fault-handling logic that maps anomalies to affected subsystems and suggests actions (e.g., subsystem reset or manual inspection).

### 4.2.6 Automated Response Systems

* **Approach**:
  + Focus on one or two critical automated responses (e.g., "power reset if voltage low" or switch to backup communication path on failure).
  + Implement redundancy in high-priority areas to build confidence in fault tolerance.
* **Deliverables**:
  + Examples: Automatic failover logic for a communication system; shutdown of non-critical components during fault recovery.

### 4.2.7 Testing and Simulation

* **Approach**:
  + Set up simple testing and simulation environments to validate fault-handling performance.
  + Use fault injection for only the most critical subsystems to simulate anomalies and evaluate recovery.
* **Affordable Methods**:
  + Use software-based simulators or inexpensive hardware-in-the-loop (HIL) setups.
* **Deliverables**:
  + A focused report summarizing test results for critical scenarios (e.g., overheating, power failures).

### 4.2.8 Code and Test Coverage

* **Approach**:
  + Achieve partial Modified Condition/Decision Coverage (MC/DC) or other appropriate test coverage metrics for critical fault-handling software (e.g., fault detection and real-time telemetry).
* **Deliverables**:
  + Test reports confirming that fault detection thresholds, alerts, and recovery responses for critical systems have been verified.

### 4.2.9 Configuration Management

* **Approach**:
  + Use version control tools like **Git** to track software revisions.
  + Keep a well-documented change log that highlights modifications influencing data collection or fault-handling logic.
* **Deliverables**:
  + Version-controlled configurations and software source files tied to key project milestones.

### 4.2.10 Training and Documentation

* **Approach**:
  + Deliver a simplified fault-resolution playbook with step-by-step procedures for common anomalies.
  + Train operators using affordable fault simulation scenarios.
* **Deliverables**:
  + One concise user manual covering:
    - Health monitoring dashboard explanations.
    - Recovery instructions categorized by anomaly type.

## 4.3 Resource Recommendations for Cost-Effective Implementation

* **Open-Source Libraries and Tools**:

  + **Telemetry Analysis**: Python packages (e.g., NumPy, Pandas, Matplotlib, PyCharm).
  + **Data Storage**: SQLite or cloud storage platforms (e.g., AWS free-tier).
  + **Version Control**: GitHub or GitLab.
* **Hardware**:

  + Use low-cost processors (e.g., Raspberry Pi or Arduino boards) for monitoring and logging tasks.
  + Inexpensive sensors for temperature, pressure, and vibrations (<$50 each).
* **Cloud Software Solutions**:

  + Use free or inexpensive cloud-based dashboards (e.g., Grafana with InfluxDB) for health monitoring and anomaly notifications during testing.

## 4.4 Checklist for Small Projects

1. **Critical System Identification**:

   * ✔ Identify 3-5 key critical systems for telemetry and fault-handling implementation.
2. **Telemetry and Health Monitoring**:

   * ✔ Install low-cost sensors and logging tools to collect data continuously.
3. **Anomaly Detection**:

   * ✔ Define threshold-based rules for anomaly identification.
   * ✔ Validate real-time detection logic on simulated data.
4. **Automated Response**:

   * ✔ Develop 1-2 automated recovery actions for the most critical anomalies.
5. **Testing**:

   * ✔ Test fault recovery for priority scenarios using simulated telemetry.
6. **Documentation and Training**:

   * ✔ Create simplified user manuals and fault-handling playbooks.
   * ✔ Train mission operators with 1-2 anomaly simulation exercises.
7. **Post-Mission Analysis**:

   * ✔ Record and store key telemetry for playback and root cause analysis.

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

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

NASA has a rich history of successful (and challenging) space missions, which has led to valuable lessons learned in system health and status monitoring. These lessons ensure space systems are designed and operated to detect, analyze, and resolve anomalies efficiently. Drawing from NASA's Lessons Learned Information System (LLIS) and past mission reports, here are relevant lessons for implementing and enhancing this requirement in a practical project:

---

### **1. Capture Key Metrics for Critical Systems**

**Lesson**: *Monitor only the most critical health and status metrics for fault detection.*

* **Case Example**: *Mars Climate Orbiter (1999)*  
  The Mars Climate Orbiter failed due to a discrepancy between metric and imperial units, which could have been prevented with more robust telemetry and system data monitoring for navigation conversions. Misdiagnosed anomalies prior to orbital insertion emphasized the importance of monitoring and validating critical parameters.
* **Takeaway**: Ensure health/status data collection targets **key system parameters** that would have the biggest impact on mission outcome (e.g., propulsion, thermal systems, guidance systems).

---

### **2. Design Fault Management Systems to Handle Unanticipated Anomalies**

**Lesson**: *Anticipate and prepare for unknown or unmodeled anomalies by building flexible, adaptable fault management capabilities.*

* **Case Example**: *Apollo 13 (“Houston, we’ve had a problem”) – 1970*  
  During Apollo 13, an oxygen tank explosion created an unanticipated anomaly requiring real-time health data to diagnose and execute recovery strategies. Continuous telemetry prevented further loss of control and enabled engineers to troubleshoot and implement safe return strategies.
* **Takeaway**: Fault management systems should allow the integration of **real-time anomaly resolution via telemetry analysis**, even for unimagined fault scenarios. Health data must be detailed and accessible for rapid decision-making.

---

### **3. Test and Simulate Critical Failure Scenarios Under Realistic Conditions**

**Lesson**: *Comprehensive failure-mode testing under realistic mission conditions is essential to ensure the system performs as intended.*

* **Case Example**: *Mars Polar Lander (1999)*  
  The Mars Polar Lander's failure was attributed to premature engine shutdown due to a faulty signal interpreted as landing. Testing of health and status data systems could have revealed the improper triggering condition for the anomaly, preventing the spacecraft from failing during descent.
* **Takeaway**: Prioritize **simulation and fault injection** testing for all health monitoring mechanisms and verify proper anomaly handling in simulated mission scenarios. Test software to ensure anomalies are detected and resolved in scenarios where health data signals may be ambiguous.

---

### **4. Build in Margin and Redundancy for Health Monitoring**

**Lesson**: *Spacecraft and software systems must be capable of operating redundantly and handling degraded systems, while still providing actionable health data.*

* **Case Example**: *Hubble Space Telescope Gyroscope Failures (1999)*  
  Hubble experienced gyroscope failures but was able to switch to backup systems. This anomaly was resolved because robust health monitoring systems flagged faults early, allowing controllers to switch to the redundant gyroscopes in time to save the mission.
* **Takeaway**: Design health data systems with **redundancy and fault tolerance** capabilities, ensuring critical anomaly resolution actions can be taken even when primary systems fail.

---

### **5. Maintain Consistency Between Telemetry Data and System Models**

**Lesson**: *Errors in software or data inconsistencies can mask critical anomalies.*

* **Case Example**: *Mars Pathfinder Mission (1997)*  
  The "priority inversion" bug in the Pathfinder's operating system halted telemetry data while it recovered from a fault. Without consistent telemetry, diagnosing the issue would have been difficult. Early investigation revealed the anomaly, and software changes restored consistent operations.
* **Takeaway**: Verify that **health status telemetry** reflects systems accurately, especially after fault recovery. Design data flows to ensure they are always synchronized with the current state of the system.

---

### **6. Ensure Lessons Learned from Past Anomalies Inform Future Designs**

**Lesson**: *Capture lessons learned from prior missions and implement process improvements in new projects.*

* **Case Example**: *Space Shuttle Challenger Disaster (1986) and Reforms after Columbia Disaster (2003)*  
  Both failures emphasized the need to track and analyze available system status data comprehensively and ensure health monitoring systems are capable of highlighting hazardous trends before catastrophic events occur.
* **Takeaway**: Implement mechanisms to archive and utilize **health and status data post-mission** for root-cause analysis to drive system and process improvements for future missions.

---

### **7. Use Automation Judiciously for Anomaly Response**

**Lesson**: *Balance automation and human oversight to optimize anomaly resolution capabilities.*

* **Case Example**: *SOHO (Solar and Heliospheric Observatory) Recovery (1998)*  
  SOHO lost contact with Earth due to multiple subsystem failures, leading to loss of spacecraft orientation. Autonomous fault management could not recover the spacecraft, requiring engineers to manually restore operations. Lessons emphasized the need for balanced automated systems and human override capability when automation fails.
* **Takeaway**: Automate common or predictable fault responses (e.g., system resets or power redistribution) but ensure anomalies that exceed automation logic allow for **manual intervention** informed by health and status data.

---

### **8. Train Operators with Fault-Handling Scenarios**

**Lesson**: *Operators must be familiar with how to interpret and act on health and status data in real-time during anomalies.*

* **Case Example**: *Apollo 11 – Lunar Module Radar Anomalies*  
  During Apollo 11’s descent, the Lunar Module's computer became overloaded with radar data. Training ensured the crew could prioritize critical systems while Mission Control diagnosed the issue and confirmed it was not dangerous. This avoided an abort decision fueled by incomplete information.
* **Takeaway**: Conduct regular training that uses **anomaly scenarios** based on health and status data. Simulations should give real-world experience in diagnosing telemetry anomalies and executing recovery operations.

---

### **9. Continuously Validate Data Systems During the Mission**

**Lesson**: *Live validation of telemetry data ensures health systems continue to perform as intended during operation.*

* **Case Example**: *James Webb Space Telescope (2021 Launch)*  
  While deploying the complex systems of the JWST, engineers monitored every step with detailed telemetry validation. This approach caught small anomalies before they could escalate into mission-compromising faults.
* **Takeaway**: Use **progressive validation of health data systems** to confirm system-wide health and redundancy during all mission phases, especially critical moments like deployment or insertion.

---

### **10. Simplify Data Presentation for Operators**

**Lesson**: *Operators need health data presented in a clear and actionable format to facilitate rapid and reliable responses to anomalies.*

* **Case Example**: *Curiosity Rover (2012)*  
  Telemetry systems on Curiosity were designed to present diagnostic information in user-friendly dashboards, enabling ground control to quickly diagnose and react to anomalies, saving time during Mars operations.
* **Takeaway**: Use **concise visualizations** (e.g., live dashboards, alerts, and status summaries) for health data to help operators focus on critical anomalies.

---

### **Conclusion**

NASA’s historical lessons emphasize the importance of telemetry and health/status monitoring for detecting, diagnosing, and resolving anomalies. By incorporating these lessons into your project, you can ensure that your systems are reliable and capable of addressing operational challenges effectively. The overarching goals are to develop simple, redundant, and actionable data systems, perform robust testing and training, and use health data for continuous mission safety and improvement. These practices are just as applicable to small projects as they are to complex flagship missions.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-38 - Data Analysis**

4.3.8 The space system shall provide the capability to utilize health and status data (including system performance data) of critical systems and subsystems to facilitate anomaly resolution during and after the mission.

Enhanced software assurance guidance ensures that the space system delivers a reliable, safe, and capable mechanism for health and status data utilization. By implementing rigorous SA controls, addressing potential hazards early, and validating software extensively, the mission-critical requirement of enabling anomaly resolution is assured. These improved practices, driven by metrics and lessons learned, guarantee mission success and safety.

## 7.1 Tasking for Software Assurance

1. Confirm that the hazard reports or safety data packages contain all known software contributions or events where software, either by its action, inaction, or incorrect action, leads to a hazard.
2. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
3. Assess that hazard analyses (including hazard reports)identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
4. Confirm that the traceability between software requirements and hazards with software contributions exists.
5. Develop and maintain a software safety analysis throughout the software development life cycle.
6. Confirm software testing is complete and accurate.
7. Ensure that safety-critical software requirements are implemented per the NPR 7150.2 Requirements Mapping Matrix and tested or verified.
8. Perform safety reviews on all software changes and software defects.
9. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.
10. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically collection of health and status data. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks.) Ensure that the project has developed and executed test cases to test the software system’s ability to utilize health and status data (including system performance data) of critical systems and subsystems.
11. Analyze the software test procedures for the following:
    1. Coverage of the software requirements.
    2. Acceptance or pass/fail criteria,
    3. The inclusion of operational and off-nominal conditions, including boundary conditions,
    4. Requirements coverage and hazards per [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) and [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), respectively.
12. Perform test witnessing for safety-critical software to ensure that all faults identified during system development or mission operations are detected, isolated, and recovered from.
13. Confirm that test results are sufficient verification artifacts for the hazard reports.
14. Confirm that strict configuration management is maintained to ensure that the correct software versions and configurations are used.
15. Ensure comprehensive training and documentation for operators is available.

## 7.2 Software Assurance Products

To meet the requirement that the space system shall provide the capability to utilize health and status data (including system performance data) of critical systems and subsystems to facilitate anomaly resolution during and after the mission, enhanced software assurance (SA) guidance is critical. Below is a streamlined, actionable, and comprehensive framework that integrates best practices, NASA standards, and risk-based decision-making.

To achieve compliance with the requirement and ensure the safety and reliability of the system, the following software assurance products must be developed, rigorously evaluated, and maintained:

#### **Essential Work Products**

1. **System Design Evaluation**:

   * **Required Levels of Failure Reporting/Annunciation**:
     + Evaluate system designs to verify all critical subsystems implement real-time failure detection mechanisms (e.g., alarms, thresholds, logs).
   * **Software Implementation of Failure Reporting**:
     + Verify that the software design translates the system-level failure reporting requirements into effective code-level implementations.
     + Ensure compatibility between telemetry systems and onboard logic.
2. **Completed Analyses and Results**:

   * **Hazard Reports and Hazard Analyses**:
     + Identify all potential hazard faults along with their associated isolation and recovery mechanisms.
     + Confirm traceability from hazard controls to software design and test procedures.
   * **Software Safety Analysis Results**:
     + Perform iterative analyses of software contributions to hazards across development phases.
   * **Software Fault Tree Analysis (FTA) and Failure Modes and Effects Analysis (FMEA)**:
     + Document fault effects, detection points, and mitigation strategies, focusing particularly on safety-critical subsystems.
3. **Audit Reports**:

   * Audit outputs from:
     + Functional Configuration Audit (FCA) — Assess adequacy in meeting functional requirements.
     + Physical Configuration Audit (PCA) — Confirm delivered code conforms to approved configuration items.
4. **Verification and Validation Artifacts**:

   * SWE-Work Product Assessments:
     + **Test Plans, Test Procedures, and Test Reports**:
       - Ensure thorough coverage of anomaly resolution scenarios, including both failure and recovery operations.
     + **User Manuals**:
       - Confirm accuracy of manuals for operators, emphasizing how to interpret telemetry data during anomalies.
   * **Code Coverage Results**:
     + Use automated tools to measure code coverage during testing (e.g., Modified Condition/Decision Coverage [MC/DC]) and verify a minimum threshold of 100% for critical modules.
   * **Test Witnessing Signatures (SWE-066)**:
     + Maintain records of test witnessing for safety-critical scenarios, ensuring all identified hazards and mitigation mechanisms are thoroughly validated.
5. **Configuration Management Artifacts**:

   * Ensure all hazard reports, safety analyses, test plans, code versions, and related documents are under strict configuration control (SWE-187).

## 7.3 Metrics

Software assurance metrics are critical for monitoring compliance, addressing deviations early, and ensuring mission reliability. The following metrics provide insight into development and testing progress, safety assurance, and fault-handling robustness:

### 7.3.1 Verification and Validation Metrics

1. **Test Coverage**:
   * Measure test coverage for all critical scenarios (normal operations, fault modes, recovery actions) and achieve 100% code coverage for safety-critical software components.
2. **Defect Density**:
   * Track defects per 1,000 lines of code to ensure fault-tolerant and reliable code. Aim for reduced rates across phases.
3. **Requirements Traceability**:
   * Ensure full traceability:
     + From system requirements → software requirements → design → implementation → test cases.
     + From hazard analyses → software functionality → test verification.

### 7.3.2 Safety Metrics

1. **Hazard Mitigation Compliance**:
   * Percentage of identified hazards with completed test verification.
   * Number of non-conformances tied to hazard controls or test failures (open, closed, severity-based trends).
2. **Safety-Critical Code Coverage**:
   * Measure the % of test cases executed for all safety-critical modules and paths (including exception handling, fault recovery, etc.).

### 7.3.3 Quality Metrics

1. **Code Complexity and Maintainability**:
   * Monitor cyclomatic complexity and ensure adherence to predefined thresholds for mission-critical software.
2. **Code Stability (Code Churn)**:
   * Analyze high-frequency code modifications to focus additional SA scrutiny on unstable areas.

### 7.3.4 Performance Metrics

1. **Anomaly Response Timing**:
   * Measure the system's response time to anomalies, ensuring resolution occurs within acceptable mission parameters.
2. **System Availability/Uptime**:
   * Ensure the system remains operational during critical mission phases despite anomalies.

### 7.3.5 Configuration **Management Metrics**

1. **Version Control Metrics**:
   * Track the number of baselined versus modified software components.
2. **Change Request Analysis**:
   * Analyze submitted change requests (e.g., frequency, type, resolution time) to identify underlying issues.

### 7.3.6 Training Metrics

1. **Operator Training Completion**:
   * Ensure completion of required training for anomaly resolution tools and processes.

### 7.3.7 Independent Verification and Validation (IV&V) Metrics

1. **IV&V Traceability and Coverage**:
   * Track IV&V confirmation of functionality for all hazard controls and anomaly response features.
2. **IV&V Findings and Issue Resolution**:
   * Monitor the number and severity of issues raised by IV&V efforts and their resolution status.

## 7.4 Software Assurance and Safety Guidance

To ensure the requirement is met, the following SA activities are recommended throughout the software development life cycle:

### 7.4.1 Design and Development Phase

* **Requirements Review**:
  + Confirm all requirements (including failure detection, reporting, isolation, and recovery) are explicitly defined and traceable.
* **Design Analysis**:
  + Assess that all health monitoring and reporting mechanisms are integrated at the design level.
* **Automated Tools**:
  + Utilize static analyses for early defect detection and coverage analysis tools to verify completeness during development.

### 7.4.2 Testing and Verification Phase

* **Test Case Development**:
  + Develop robust test cases covering:
    - Normal operations and fault-free conditions.
    - Failures identified during hazard analyses (e.g., thresholds, configuration errors).
    - Recovery scenarios for critical faults.
* **Test Witnessing**:
  + Witness safety-critical tests with special attention to recovery after anomalies.
* **Code Coverage**:
  + Validate MC/DC coverage to ensure all decision paths for anomaly resolution are traversed.

### 7.4.3 Safety and Hazard Analyses

* **Focus Areas**:
  + Ensure FTA and FMEA results are continuously updated to identify and mitigate new hazards as design evolves.
  + Verify anomaly response times prevent cascading faults.
  + Confirm that all fault paths are tested under edge-case scenarios.

### 7.4.4 Audits and Configuration Management

* **Audits**:
  + Conduct FCA and PCA audits to verify both functionality and physical artifact compliance.
* **Configuration Management**:
  + Enforce version control for all software components and associated analyses.

### 7.4.5 Training and Documentation

* **Training**:
  + Conduct operator and test team training on health and status monitoring dashboards and fault-handling playbooks.
* **Documentation**:
  + Provide concise, scenario-focused documentation for anomaly response actions.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence refers to verifiable artifacts, documentation, and deliverables that demonstrate compliance with the requirement

**HR-38 - Data Analysis**

4.3.8 The space system shall provide the capability to utilize health and status data (including system performance data) of critical systems and subsystems to facilitate anomaly resolution during and after the mission.

This evidence serves to confirm that the system is capable of collecting, monitoring, analyzing, and using health and status data for fault detection, isolation, and recovery. Below, objective evidence is categorized based on the software development lifecycle phases.

This evidence demonstrates a comprehensive approach to proving compliance with the requirement, covering detection, isolation, and mitigation of anomalies during all mission phases.

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

## 8.1 System and Software Requirements Phase

#### **Objective Evidence Artifacts:**

1. **Requirements Traceability Matrix (RTM)**:

   * Demonstrates that health and status data requirements are captured and traced to:
     + System-level requirements (e.g., failure detection thresholds).
     + Software design, implementations, and testing efforts.
   * Traceability should link anomaly resolution requirements to system hazard reports and safety-critical requirements.
2. **Use Cases/Scenarios**:

   * Clearly defined use cases for how health and status telemetry will facilitate:
     + Real-time anomaly resolution during the mission.
     + Post-mission analysis for recurring fault identification.
   * Scenarios covering nominal operations, fault conditions, and recovery operations.
3. **Requirements Review Records**:

   * Review minutes showing that stakeholders verified and approved requirements for monitoring and processing health data.
   * Evidence that system constraints, failure thresholds, and reporting mechanisms were appropriately analyzed.

## 8.2 System and Software Design Phase

#### **Objective Evidence Artifacts:**

1. **Software Architecture Document (SAD)**:

   * Captures the overall architecture showing:
     + Data flow for health and status telemetry.
     + Interfaces between hardware, software, and external monitoring systems.
     + Subsystems responsible for fault isolation and recovery mechanisms.
2. **Detailed Design Documents**:

   * Evidence describing:
     + Health monitoring algorithms (e.g., failure thresholds, anomaly detection logic).
     + Design of failure reporting and annunciation mechanisms.
     + Design integration of fault-handling and isolation mechanisms.
3. **Fault Detection and Recovery Flowcharts**:

   * Visual workflows showing how the system resolves anomalies:
     + Detection of an anomaly (e.g., parameter monitoring thresholds violated).
     + Isolation to the affected component/subsystem.
     + Recovery action (e.g., failover, reinitialization, notification).
4. **Interface Control Documents (ICD)**:

   * Specification of how health and status data is transmitted, stored, and accessed by subsystems and ground systems:
     + Format of telemetry data.
     + Communication protocols (redundancy considerations).
5. **Link to Hazard Analysis Updates**:

   * Updates to system hazard reports that document how software design addresses identified safety risks.
6. **Peer Review Records**:

   * Documented results of peer reviews for design elements related to health and status telemetry, anomaly detection, and redundancy.

## 8.3 Implementation Phase

#### **Objective Evidence Artifacts:**

1. **Source Code and Version History**:

   * Evidence that the implemented code includes functions for:
     + Data collection from sensors or system instrumentation.
     + Anomaly detection algorithms (e.g., thresholds, alerts).
     + Recovery mechanisms for safety-critical features.
2. **Static Analysis Reports**:

   * Results from automated tools that:
     + Validate code quality metrics like cyclomatic complexity.
     + Detect potential issues in critical paths for health and status data processing.
3. **Version Control Logs**:

   * Logs showing configuration control for all software modules implementing health monitoring and anomaly resolution.
4. **Unit Test Results**:

   * Unit test artifacts for modules responsible for telemetry collection, data processing, and fault handling.
   * Verified against all applicable requirements.
5. **Integration Test Results**:

   * Validates the functional integration of health and status telemetry subsystems:
     + Software with hardware sensors.
     + Onboard telemetry with ground communication links.

## 8.4 Verification and Validation (V&V) Phase

#### **Objective Evidence Artifacts:**

1. **Software Test Plans (STP)**:

   * Test plans documenting:
     + Scenarios, environments, and procedures for verifying health data collection and usage in anomaly detection.
     + Tests for nominal operation, failure detection, and recovery scenarios.
2. **Software Test Procedures (STPR)**:

   * Detailed step-by-step test procedures for:
     + Validating each use case and data pathway for health and status functionality.
     + Injecting simulated anomalies to test fault-handling paths and recovery mechanisms.
3. **Software Test Reports (STR)**:

   * Results of testing that demonstrate:
     + Fault detection when out-of-threshold conditions occur.
     + Fault isolation and subsystem recovery actions as expected.
     + Post-fault system stability metrics and responsiveness.
4. **Code Coverage Reports**:

   * Evidence that critical software paths for health telemetry (normal operations, anomaly detection, fault recovery) achieved 100% Modified Condition/Decision Coverage (MC/DC).
5. **Simulation Logs**:

   * Logs from fault-injection simulations showing the system’s performance under:
     + Normal and high-risk fault conditions.
     + Stress conditions (e.g., multiple failures).
6. **Verification Artifacts**:

   * Confirmation that tests demonstrate requirements, including:
     + Sensor data processing limits.
     + Hazard mitigation workflows.
7. **Independent Verification and Validation (IV&V) Artifacts**:

   * Records of IV&V participation in:
     + Requirements review to confirm completeness of fault-handling requirements.
     + Software design review to ensure anomaly resolution integration.
     + Test witnessing and reporting.

## 8.5 Operations Phase

#### **Objective Evidence Artifacts:**

1. **Operational Logs**:

   * Real-time telemetry showing system responses during mission-critical events:
     + System behavior during anomalies.
     + Onboard recovery execution and telemetry reporting accuracy.
2. **Post-Mission Analysis Reports**:

   * Evaluation reports detailing:
     + Root-cause investigations for anomalies identified during the mission.
     + Effectiveness of telemetry data for diagnosing faults during post-mission analysis.
3. **Change and Corrective Action Records**:

   * Records showing how changes to health monitoring, fault detection, or recovery mechanisms addressed defects or gaps discovered in testing or operations.
4. **Maintenance Logs**:

   * Changes to health monitoring or fault detection thresholds based on operational lessons.

## 8.6 Safety and Configuration Management

#### **Objective Evidence Artifacts:**

1. **Hazard Reports and Controls Verification**:

   * Evidence showing hazard controls have been tested and linked to software verification.
2. **Configuration Management Baseline**:

   * Configuration control data for the:
     + Software versions implementing fault monitoring.
     + Test cases and their results.
3. **Audit Reports**:

   * Functional Configuration Audit (FCA) and Physical Configuration Audit (PCA) reports demonstrating:
     + Consistency between design, implementation, and delivered system.

## 8.7 Lessons Learned Implementation

#### **Objective Evidence Artifacts:**

1. **Archived Analysis of Previous Missions**:

   * Leveraging past anomaly data and telemetry lessons to improve system design and fault tolerance.
2. **Training Records**:

   * Evidence of operator training on:
     + Identifying anomalies in telemetry dashboards.
     + Executing recovery procedures based on software-generated alerts.

## 8.8 Final Checklist: Evidence for Compliance

* **Traceability Matrix** (requirements → implementation → testing → validation).
* **Design Documents** (telemetry collection, processing, fault-detection logic, recovery workflows).
* **Source Code Repositories** (versioning and configuration control for fault-related code).
* **Test Artifacts** (plan, procedures, results, coverage reports).
* **IV&V Reports** (independent assessments and witnessing records).
* **Operational Logs** (real-world performance of health monitoring and anomaly resolution mechanisms).
* **Post-Mission Reports** (lessons learned and feedback loops).
