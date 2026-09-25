# HR-31 - Single Failure Tolerance

> NASA Software Engineering Handbook (SWEHB Ver D), page id 167805124. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805124/HR-31+-+Single+Failure+Tolerance

HR-31 - Single Failure Tolerance

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805124/HR-31+-+Single+Failure+Tolerance#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=167805124)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=167805124&showCommentArea=true&showComments=true#addcomment)

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

4.3.1 The space system shall provide at least single failure tolerance to catastrophic events, with specific levels of failure tolerance and implementation (similar or dissimilar redundancy) derived via an integration of the design and safety analysis (required by NPR 8705.2).[024](#_tabs-<p></p>)

## 1.1 Notes

Redundancy alone does not meet the intent of this requirement. When a critical system fails because of improper or unexpected performance due to unanticipated conditions, similar redundancy can be ineffective at preventing the complete loss of the system. Dissimilar redundancy can be very effective provided there is sufficient separation among the redundant legs. (For example, dissimilar redundancy where the power for all redundant capability was routed through a common conduit would not survive a failure where the conduit was severed). It is also highly desirable that the spaceflight system performance degrades in a predictable fashion to allow sufficient time for failure detection and, when possible, system recovery even when experiencing multiple failures.

There are examples of dissimilar redundancy in current systems. For Earth reentry, the Soyuz spacecraft has a dissimilar backup ballistic entry mode to protect for loss of the primary attitude control system and a backup parachute for landing. Other examples include backup batteries for critical systems that protect from loss of the primary electrical system and the use of pressure suits during reentry to protect for loss of cabin pressure.

Ultimately, the program and Technical Authorities evaluate and agree on the failure scenarios/modes and determine the appropriate level of failure tolerance and the practicality of using dissimilar redundancy or backup systems to protect for common cause failures.

Where failure tolerance is not the appropriate approach to control hazards, specific measures need to be employed to:

1. Identify applicable hazards and their associated controls;
2. Ensure the robustness of the design; and
3. Ensure adequate attention/focus is being applied to the design, manufacture, test, analysis, and inspection of the items.

In the area of design, in addition to the application of specifically approved standards and specifications, these measures can include the identification of specific design features that minimize the probability of occurrence of failure modes, such as the application of stringent factors of safety or other design margins. For manufacturers, these measures can include establishing special process controls and documentation, special handling, and highlighting the importance of the item for those involved in the manufacturing process. For testing, this can include accelerated life testing, fleet leader testing program, testing to understand failure modes, or other testing to establish additional confidence and margin in the design. For analysis (in lieu of tests), these measures can include correlation with the testing representative of the actual configuration and the collection, management, and analysis of data used in trending failures, verifying loss of crew requirements, and evaluating flight anomalies. For inspection, these measures can include the identification of specific inspection criteria to be applied to the item or the application of Government Mandatory Inspection Points or similar audits for important characteristics of the item. This approach to hazard control takes advantage of existing standards or standards approved by the Technical Authorities to control hazards associated with the physical properties of the hardware and are typically controlled via the application of margin to the environments experienced by the design or system properties affected by the environment. Acceptance of these approaches by the Technical Authorities avoids processing waivers for numerous hazard causes where failure tolerance is not the appropriate approach. This includes, but is not limited to, Electro-Magnetic Interference, Ionizing Radiation, Micrometeoroid Orbital Debris, structural failure, pressure vessel failure, and aerothermal shell shape for flight.

## 1.2 History

Click here to view the history of this requirement: HR-31 History

HR-31 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.3.1 The space system shall provide at least single failure tolerance to catastrophic events, with specific levels of failure tolerance and implementation (similar or dissimilar redundancy) derived via an integration of the design and safety analysis (required by NPR 8705.2). |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

The objective is to arrive at the safest practical design to accomplish a mission. Since space system development will always have mass, volume, schedule, and cost constraints, choosing where and how to apply failure tolerance requires integrated analyses at the system level to assess safety and mission risks, guided by a commonly understood level of risk tolerance at the system and local (individual hazard) levels.

The rationale for this requirement is rooted in ensuring mission safety, human survivability, and minimizing the likelihood of catastrophic events due to unexpected failures, based on the principles outlined in **NASA-STD-8719.29** and **NPR 8705.2**. Below are the detailed reasons and considerations behind this requirement:

## 2.1 Ensuring Human Safety and Survivability

* **Crew Safety is Paramount**: Space systems are often tasked with carrying human crews, where the consequences of a catastrophic event (such as loss of life, permanent injury, or critical system loss) are unacceptable. Providing single failure tolerance ensures that the system remains functional even after the failure of one critical component, thereby protecting the crew.
* **Disaster Mitigation**: If a failure occurs in a critical component without redundancy, there is no opportunity to prevent a cascading series of events that could result in mission compromise, loss of the crew, or destruction of the space system. Single failure tolerance acts as the first line of defense against such scenarios.

## 2.2 System Reliability and Mission Success

* **Resilience to Inherent Risks of Space Operations**: Space environments are inherently high-risk due to factors like extreme temperatures, vacuum conditions, space radiation, and micrometeoroid impacts. A single failure-tolerant design ensures the system can continue functioning under these challenging conditions.
* **Optimization of Risk Management**: As stated in **NASA-STD-8719.29, Section 4.3.1**, integrated design analyses allow for a balance between system-level redundancy, functionality, and mass/power constraints. By implementing single failure tolerance, systems add a vital layer of reliability while accommodating mission-specific risks.
* **Historical Lessons Learned**: Multiple historical failures, including loss of life in spaceflight disasters (e.g., Space Shuttle Challenger and Columbia), highlight the need for resilient designs that tolerate isolated component or subsystem failures.

## 2.3 Balancing Redundancy, Mass, and Power

* **Informed Redundancy Strategies**: Not all components are equally critical; hence, the guidance in **Section 4.3.1** focuses on tailoring redundancy strategies (similar or dissimilar) toward catastrophic failure scenarios. The use of "dissimilar redundancy" (e.g., a backup parachute or multiple independent power sources) provides additional protection.
  + Dissimilar redundancy offers protection from **common-cause failures**, where faults might propagate due to a single shared design flaw.
* **Design Optimization**: Single failure-tolerant designs are critical in missions where mass, power, and volume constraints must be considered. For example, adding unnecessary duplication in non-essential systems risks compromising mission success while using excessive resources.

## 2.4 Integrated and Tailored Safety Analysis

* **Use of Probabilistic Safety Analysis (PSA)**: Section 4.2.2 emphasizes utilizing targeted probabilistic analyses to balance risk and redundancy. Engineers derive redundancy options based on the likelihood of failures, potential consequences, and ability to tolerate said failures.

  + For safety-critical systems, redundancy ensures that single-component failures do not progress to mission-ending outcomes.
* **Flexibility in Implementation**: Redundancy for single failure tolerance is informed by integrating safety analysis into the design process (e.g., failure modes, fault trees, and hazard assessments). This ensures appropriate levels of redundancy are applied to various systems (e.g., similar redundancy for straightforward systems, dissimilar redundancy for more complex or interdependent systems).

## 2.5 Practical Insights from Real-World Systems

* **Examples of Redundant Systems**:
  + The **Soyuz spacecraft** provides a dissimilar backup ballistic entry mode and redundant parachutes during Earth reentry.
  + Backup batteries and pressure suits extend survivability if primary systems fail.
* **Design Trade-offs**: While adding redundancy inherently increases system complexity, mass, and cost (e.g., wiring, structures), careful analysis ensures the safest practical solution per mission.

## 2.6 Preventing Reliance on Emergency Equipment

* **Emergency Systems as Secondary Lines of Defense**: Section 4.3.2 clarifies that emergency equipment (e.g., fire extinguishers, suits) is not sufficient as failure tolerance measures, as their purpose is mitigating impacts—rather than directly preventing hazardous states.
  + Systems with built-in failure tolerance (redundant engines, structural protections, fail-safe communication) prevent reliance on these reactive backup systems.
  + For example, a fire extinguisher may mitigate the post-failure effects of a fire, but redundant electrical systems reduce the likelihood of the ignition source itself.

## 2.7 Designing for Predictable Degradation

* **Rationale for Controlled Degradation**: The failure-tolerant design ensures systems degrade predictably, allowing early fault detection and sufficient time for mitigation.
  + For instance, critical systems like propulsion include staggered layers of redundancy so the impact of sequential failures can be managed without catastrophic events occurring.
* **Integration with Crew Awareness**: Adequate monitoring capabilities (per Section 4.3.6–4.3.7) are necessary to detect and isolate faults before failure tolerance redundancy is threatened.

## 2.8 Risk Posture Alignment with Mission Objectives

* **Mission-Specific Risk Tolerance**: **NASA-STD-8719.29, Section 4.1.1** calls for assessing each space system against its mission-specific hazards (e.g., crewed lunar landings vs. deep space exploratory missions). Single failure tolerance allows Technical Authorities to align risk postures with the mission and make informed tradeoffs.
* **Adaptive Approaches**: When failure tolerance cannot be used (e.g., primary structure cracks), **Section 4.3.1.1** discusses alternative risk management measures:
  + Using stringent design margins/factors of safety.
  + Heightening inspection protocols.
  + Increasing the robustness of process controls (manufacturing, testing).

## 2.9 Contribution to Sustainable Operations

* **Lessons Propagated Forward**: Single failure-tolerant designs establish a standard of sustainability and reliability across NASA programs. These designs reduce maintenance costs, simplify anomaly investigation, and ensure long-term consistency across future iterations of the system.

## 2.10 Related Rationale Summary

The specific rationale for this requirement can be summarized as:

1. **Safety-first Design**: Ensures crew and system survival in the event of single-point failures.
2. **Tailored Redundancy**: Allows flexible implementation (e.g., similar redundancy vs. dissimilar redundancy) to address unique mission risks.
3. **Fault Detection and Recovery**: Provides time for fault detection, isolation, and recovery, reducing dependencies on emergency systems.
4. **Optimized Risk vs. Resource Trade-offs**: Balances science, reliability, and engineering constraints in critical design architecture.

Ultimately, this requirement is borne out of historical lessons, advancing risk-informed engineering approaches, and ensuring the robustness of mission-critical systems under the most stringent conditions. It embodies **NASA’s commitment to designing space systems that are resilient, sustainable, and capable of performing within high-stakes operational environment**

# 3. Guidance

The guidance provided has been refined to offer greater clarity, structure, and actionable detail in implementing failure tolerance for catastrophic events, particularly in software-dependent systems. It reflects the integration of lessons learned, modern best practices, and established standards like NASA-STD-8719.29 and NPR 8705.2. This version emphasizes system-wide considerations, with a focus on ensuring safety and mission success while managing complexity.

To control and mitigate software common mode failures, there are required risk minimization activities as well as three options for control/mitigation strategies (System Failure Tolerance, Recover/Repair, and Risk Acceptance).  If Risk Acceptance is the selected option, the Variance, and NCR acceptance rationale should describe the risk minimization activities and address how these eight items are being implemented or provide compatible alternatives that meet their intent.

By adhering to this guidance, failure tolerance can be achieved effectively for software-dependent space systems. It ensures safe operations even under catastrophic failure scenarios, aligns with NASA's rigorous safety and mission assurance standards, and establishes the foundation for sustainable innovation in future human-rated spaceflight systems.

For software failure tolerance specifically, more detailed considerations and strategies are summarized in **NESC Technical Bulletin 23-06: Considerations for Software Fault Prevention and Tolerance** [687](#_tabs-<p></p>)

## 3.1 Purpose of Requirement

The requirement addresses the critical need for space systems to ensure **failure tolerance** to catastrophic events by implementing specific levels of redundancy and analyzing both hardware and software risks at the integrated system level. Catastrophic hazards are events that compromise crew safety, mission objectives, or system functionality, requiring design features that mitigate or eliminate such risks.

## 3.2 Key Principles of Failure Tolerance Implementation

Failure tolerance must be addressed comprehensively, considering the interplay between hardware, software, operational procedures, and environmental challenges. Below are principles for applying failure tolerance:

1. **Integrated System-Level Focus**:

   * Failure tolerance must encompass **the entirety of the system**, including hardware, avionics, software, crew operations, and ground support infrastructure.
   * The requirement applies universally to all critical system capabilities, with no distinction between hardware or software failures, which must both adhere to the same criteria for catastrophic hazard prevention.
2. **Balanced Redundancy**:

   * Redundancy may include **similar systems** (identical replicas), **dissimilar systems** (unique alternatives), **cross-strapping architectures**, and **functional interrelationships** that provide equivalent redundancy to prevent failures.
   * While redundancy inherently increases complexity, resource utilization (e.g., mass, power, computational load) and mission constraints must be considered to optimize reliable system design.
3. **Software-Specific Considerations**:

   * Address software common-mode failures (e.g., task overruns, stack overflow, input handling errors) that occur simultaneously across redundant instances.
   * Ensure failure tolerance to both erroneous software outputs and silent failure (software ceasing to function during critical operations).
   * Even with rigorous software development, verification, and validation processes, software failures can and do occur—requiring additional layers of mitigation and recovery strategies.
4. **Differentiated Approaches for Controlled Hazards**:

   * Exemptions for hazards like structural or pressurized system failures are governed by alternate robust control standards, as outlined in **NASA-STD-8719.29** Section 4.3.1.1.
   * Any hazard exempted from failure tolerance must be rigorously managed using approved standards, margins, and mandatory concurrence by technical authorities.

## 3.3 Steps to Implement Failure Tolerance for Software Systems

### 3.3.1 Identify Applicable Hazards and Controls

* **Hazard Analysis**:

  + Extend hazard analysis processes to include software-specific risks and failure scenarios, including common-mode failures or cascading failure risks.
  + Perform detailed assessments tied to *Concept of Operations* (CONOPS) for mission phases and operational environments.
  + Evaluate the **time-to-criticality** for each identified catastrophic hazard to determine whether failures can be recovered before consequences are realized.
* **Failure Modes and Effects Analysis (FMEA)**:

  + Conduct FMEA for critical functions and their software components to systematically identify failure modes, their severity, likelihood, and redundancy measures.

Other potentially catastrophic hazards that cannot be controlled using failure tolerance are exempted from the failure tolerance requirements with mandatory concurrence (as required by NPR 8705.2) from the Technical Authorities and the Director, JSC (for crew risk acceptance) provided the hazards are controlled through a defined process in which approved standards and margins are implemented that account for the absence of failure tolerance.

### 3.3.2 Integrate Redundancy

* **Dissimilar Redundancy**:

  + Create redundancy using diverse implementations (e.g., distinct algorithms, hardware, or architectures) to avoid shared vulnerabilities that could lead to simultaneous failure.
  + Examples:
    - Backup critical vehicle system functions (attitude control, propulsion, etc.) with dissimilar software or hybrid hardware/software solutions.
    - Distribute software functions in **virtual partitions** or across **distributed network architectures** such as ARINC 653 standards.
* **Predictable Degradation**:

  + Design redundant systems to degrade gracefully under failure conditions, providing time for detection, response, and recovery without catastrophic progression.

Redundancy alone does not meet the intent of this requirement. When a critical system fails because of improper or unexpected performance due to unanticipated conditions, similar redundancy can be ineffective at preventing the complete loss of the system. Dissimilar redundancy can be very effective provided there is sufficient separation among the redundant legs. For example, dissimilar redundancy where a crew member uses or portion of the same software that is behaving erroneously to override automated with manual control may not survive the failure since the approaches share a common failure point.  Areas in the system architecture should be analyzed for this commonality.   It is also highly desirable that the spaceflight system performance degrades predictably to allow sufficient time for failure detection and, when possible, system recovery even when experiencing multiple failures.

### 3.3.3 Define Software Mitigation for Common-Mode Failures

* **Risk Reduction Techniques**:

  + Apply robust software development practices, safety-critical programming standards (NASA-STD-8739.8), and stringent coding practices (defined in SSP 50808).
  + Implement runtime tools such as watchdog timers and **self-checking logic** for automated detection and correction of faults.
  + Establish **manual override controls** for critical flight systems, ensuring crew can bypass automated software functions during unexpected failures.
* **Fault Detection and Isolation**:

  + Include fail-safe mechanisms to detect and isolate faults, faults in shared resources (e.g., memory, processor load), and errors in data processing.

### 3.3.4 Recovery and Repair Strategies

* **Recovery Processes**:

  + Design robust mechanisms to restore software functionality during failures:
    - **Reboot and Reinitialize**: Clear system states after encountering failures.
    - Integrate **software audits** to repair corrupted software structures dynamically.
    - Provide "fault-down/safe mode" embedded software capabilities to maintain minimal operation during software fault recovery.
* **Supporting Hardware/Software Synergy**:

  + Combine software recovery protocols with hardware redundancy to maintain continued safe operation under degraded conditions.

### 3.3.5 Testing and Validation

* **Simulations**:

  + Conduct environmental and stress testing to validate software response to failure scenarios. Include plausible real-world cases like hostile space conditions and unexpected operator inputs.
  + Examples of tests:
    - Monte Carlo simulations to model catastrophic hazard behavior.
    - Parameter value coverage tests to identify edge cases where failure may emerge.
* **Independent Verification & Validation (IV&V)**:

  + Engage IV&V to ensure proper implementation of failure tolerance strategies, particularly for human-rated software systems where safety is paramount.

### 3.3.6 Metrics and Feedback for Continuous Improvement

* **Process Metrics**:

  + Track progress in detecting and resolving failure tolerance gaps during development phases. Examples include:
    - Percentage of code coverage during test.
    - Frequency and type of defects detected after deployment.
    - Memory and processing utilization rates during hard fault conditions.
* **Post-Flight Learning**:

  + Collect in-flight software performance data to refine redundancy designs and mitigate recurring risks for future missions.

## 3.4 Guidance for Risk Acceptance

### 3.4.1 Non-Compliance Reporting (NCR) and Variances

* When failure tolerance approaches are impractical (e.g., "blackout zones" or transient conditions where complete mitigation is unachievable), submit detailed NCRs supported by *specific hazard reports* and supplemented by robust mitigation measures.
* Risk acceptance rationale must demonstrate exhaustive analysis of constraints and alternative controls.

### 3.4.2 Continuous Audits

* Perform mandatory audits for high-severity escapes and assess gaps in coding standards and testing processes.
* Evidence of periodic audits and corrective action must be presented for flight readiness review and ongoing missions.

### 3.4.3. Coordination Across Teams

* Ensure a multidisciplinary team—software developers, safety experts, requirements authorities, subsystem owners, and mission operations—reviews and approves high-risk software design decisions.

3.5 Example Applications in Space Systems

1. **Earth Reentry**:

   * Soyuz spacecraft dissimilar redundancy approach for ballistic entry and backup parachutes exemplifies robust redundancy mitigating critical failures.
2. **Distributed Architectures**:

   * Implementation of ARINC 653 partitions ensures critical systems (flight control, propulsion, and navigation) remain isolated during shared resource failures.

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Requirements related to Human Rated Software.

## 3.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

## 3.6 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

For small projects, implementing failure tolerance effectively should balance **simplicity, resource constraints**, and **risk management** while still meeting the intent of Requirement 4.3.1. This requires focusing on **practical strategies**, using lightweight processes, and leveraging proven tools and techniques. Below is streamlined guidance tailored for smaller-scale projects with moderate resource availability.

For small projects, the failure tolerance requirement can be met through **well-targeted redundancy, lightweight analysis, and using practical, proven tools**. By focusing resources on high-priority hazards, ensuring recoverability in critical situations, and leveraging existing technologies, small projects can maintain high safety standards while staying on track with budget, schedule, and resource constraints. **Iterative validation and simplicity are key to success.**

### 4.1 Key Principles for Small Projects

1. **Simplified Approaches**: Use straightforward failure tolerance mechanisms (e.g., basic redundancy, modular designs) to meet failure tolerance requirements without overcomplicating system design.
2. **Prioritized Risk Management**:
   * Concentrate efforts on **critical systems and software** most likely to create catastrophic hazards.
   * Start with known high-risk scenarios and expand coverage iteratively.
3. **Leverage Existing Tools/Technologies**: Where possible, reuse components, architectures, and software modules with proven reliability to save development effort.
4. **Iterative Validation**: Perform small, frequent system checks during development, reducing the need for heavy up-front planning while still validating failure tolerance throughout.

### 4.2 Planning and Hazard Identification

#### **Goals**

* Ensure all possible failure modes leading to **catastrophic events** are understood and documented.
* Keep focus on the **critical few** catastrophic hazards to optimize time and costs.

#### **Steps**:

1. **Define Critical Capabilities**:

   * Focus on the systems/functions required for crew safety, mission success, or preventing catastrophic failure (e.g., life support, propulsion, navigation systems, or essential software).
   * Keep scope manageable: Typically identify 3–5 key systems or failure scenarios.
2. **Simplify Fault Analysis**:

   * Use a lightweight **Failure Modes and Effects Analysis (FMEA)** process:
     + List potential failure modes of hardware/software.
     + Assess the likelihood, severity, and detectability of each failure.
     + Prioritize **catastrophic-hazard-related failures** (those with high severity).
   * Example: If a propulsion system failure can directly result in loss of crew or vehicle, it should receive the highest priority.
3. **Document Hazards Clearly**:

   * Use simplified hazard tables to capture:
     + System/Component.
     + Failure mode.
     + Potential Hazard (e.g., loss of thrust).
     + Possible Mitigation.
     + Priority Level.
   * Keep concise—1–2 pages per system/hazard.

### 4.3 Implementing Failure Tolerance

#### **Goals**

* Create redundancy and error-handling mechanisms that minimize the risk of catastrophic outcomes within resource limitations.

#### **Strategies**:

1. **Use Redundancy Sparingly**:
   * **Similar Redundancy**: Use redundant hardware components or identical software copies for simpler systems.
     + **Example**: Include a backup battery for power systems or duplicate communication links for critical signals.
   * **Dissimilar Redundancy**: Where possible, use diverse implementations of key systems (e.g., alternative algorithms in software, different sensors for measuring the same parameter).
     + **Example**: Use two distinct propulsion controllers—one software-driven, the other hardware-only.
2. **Design for Graceful Degradation**:
   * Ensure the system can still operate in a **limited or degraded state** during a failure.
     + Example: If primary navigation fails, switch to backup sensors providing reduced precision but sufficient for mission continuation.
3. **Implement Recovery/Repair Mechanisms**:
   * Include mechanisms to recover system functionality without requiring immediate human intervention:
     + System reboots for software.
     + Watchdog timers to detect and respond to software stalls.
     + Safe modes for hardware recovery when failures occur (e.g., switching to standby power).
4. **Manual Overrides for Safety-Critical Software**:
   * Allow operators (crew or ground control) to manually override software functions during anomalies.
     + Example: Ability to trigger spacecraft reentry manually if software automation fails.

### 4.4 Testing and Validation

#### **Goals**

* Verify failure tolerance strategies function as intended.
* Ensure reliable detection and response to failure scenarios.

#### **Small Project Testing Approach**:

1. **Functional Testing of Redundancies**:
   * Verify backup components or software successfully take over when the primary fails.
   * Example: Disconnect the primary navigation sensor to confirm the backup sensor provides adequate data.
2. **Software Failure Simulations**:
   * Use fault injection (manually enforcing failures, such as crashing a process or breaking an input sequence) to simulate software common-mode failures:
     + Test for proper handling of conditions like task overruns, divide-by-zero errors, etc.
     + Ensure the system responds predictably to cascading software failures (e.g., recovery or reboot sequences trigger as expected).
   * Use tools like hardware-in-the-loop testing if feasible to validate redundant critical systems.
3. **Time-to-Criticality Verification**:
   * For each catastrophic hazard, test whether recovery or mitigation occurs within the allowable timeframe before crew/mission loss.
   * Example: Simulate a power failure and measure the time to switch to backup batteries.
4. **Documentation via Checklist**:
   * Create simple checklists for testing outcomes:
     + Tests completed.
     + Expected vs. actual behavior.
     + Changes needed, if any.

### 4.5 Risk Acceptance for Exempt Systems

#### **Goals**

* Recognize limitations where failure tolerance cannot be achieved and formally accept the residual risk.

#### **Steps**:

1. **Analyze Alternate Controls**:
   * If single-point failures exist (e.g., unavoidable design limitations due to mass or resource constraints), list compensating controls:
     + Example: Apply rigorous process controls for manufacturing a pressure vessel that cannot meet redundancy standards.
2. **Submit Non-Compliance Reports (NCRs)**:
   * Provide detailed rationale for why failure tolerance cannot be implemented, including:
     + Technical constraints.
     + Analysis of alternate mitigations used.
     + Residual risks and their justifications.
3. **Seek Technical Authority Review**:
   * Engage stakeholders (e.g., project safety lead, Technical Authority reviewers) for approval of NCR or variance in line with NPR 8705.2.

### 4.6 Leveraging Existing Resources and Practices

#### **Goals**

* Avoid reinventing solutions; adapt and apply proven components, tools, and processes.

#### **Techniques**:

1. **Reuse Proven Components**:
   * Where practical, use commercial-off-the-shelf (COTS) or heritage systems with proven use cases in similar domains.
     + Example: Choosing a certified flight-management software module validated for fault-tolerance.
2. **Adopt Industry Standards**:
   * Follow simplified practices from NASA-STD-8739.8 (software assurance) and NASA-NPR-7150.2 to minimize software risks.
   * Use pre-existing risk templates, review checklists, and design artifacts to avoid duplicating effort.
3. **Small-Scale Automation**:
   * Incorporate lightweight automation for routine safety checks and fault detection (e.g., automated logging of failure reports or validation results).

### 4.7 Continuous Monitoring and Operational Readiness

#### **Goals**

* Maintain operational awareness for potential system issues during both development and mission operations.

#### **Approach**:

1. **Real-Time Alerts**:
   * Build simple, real-time monitoring layers into the system, such as health-check subsystems for core functions (e.g., redundant sensors to validate fault detection in propulsion).
2. **Crew/Operator Training**:
   * Provide personnel with straightforward procedures for managing failure scenarios—focus on manual overrides and redundancy recovery processes.
3. **Review Lessons Learned**:
   * Post-mission, review faults and evaluate the effectiveness of redundancy/recovery strategies. Apply improvements to future efforts.

### 4.8 Example: Simplified Implementation of Redundancy

#### **Scenario**:

A small-scale satellite project for deep-space communication.

* **Critical Hazard**: Loss of navigation during orbit insertion.
  + Primary control: Automated propulsion control software relying on GPS data.
  + Failure tolerance:
    - Redundant GPS sensors (hardware redundancy).
    - Manual override allowing ground station to send trajectory commands (dissimilar redundancy).
    - Recovery: Safe mode to maintain minimal orbital stabilization while awaiting corrective commands.

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

The following lessons are derived from real-world missions and accidents documented by NASA's **Lessons Learned Information System (LLIS)** and historical reviews of space systems. They highlight important insights that guide the effective implementation of **failure tolerance requirements** to ensure safety, reliability, and mission success. Understanding these lessons can help small and large projects alike avoid repeating past mistakes and adopt best practices.

---

### **1. Challenger Disaster (1986) — Insufficient Failure Tolerance for Critical Systems**

#### **Description**:

The failure of the Space Shuttle Challenger’s solid rocket booster (SRB) O-ring joint illustrates the catastrophic consequences of inadequate failure tolerance in critical systems. A single failure mode (the O-ring seal failure) resulted in the loss of the vehicle and crew.

#### **Key Lessons**:

* **Failure Redundancy Must Account for Environmental Conditions**:

  + The O-rings were not designed to tolerate the low temperatures present at launch, which impaired their performance. Failure tolerance strategies must consider **the full range of operational environments**, from temperature extremes to dynamic loads.
  + Redundancy strategies must explicitly model these environments to ensure robustness.
* **Engineering and Safety Must Be Integrated**:

  + The decision-making process prioritized schedule pressures over design safety. Independent safety authorities must advocate for mission-critical design integrity over external pressures.
* **Actionable Guidance**:

  + Implement rigorous **hazard analysis** that includes environmental factors.
  + Elevate **independent technical authority** in decision-making on safety-critical systems to prevent external stakeholder influence from overruling safety concerns.

---

### **2. Columbia Disaster (2003) — Failure to Address Known Hazards**

#### **Description**:

The Space Shuttle Columbia disintegrated on reentry due to damage sustained by its thermal protection system (TPS) upon launch. Foam debris impacts on the shuttle wing were a known but **unmitigated hazard**, with no effective redundancy or repair strategy integrated into the design.

#### **Key Lessons**:

* **Known Hazards Must Have Redundant Controls or Accepted Mitigations**:

  + Columbia’s wing was vulnerable to foam impacts, and no redundancy for mitigating a compromised TPS was designed. This highlights the risk of relying on performance without backup systems.
* **Timely Detection of Faults Is Essential**:

  + The shuttle program lacked the means for inflight detection and repair of TPS damage. Without the capability to monitor critical systems in real time, catastrophic situations can escalate without crew or ground intervention.

#### **Actionable Guidance**:

* **Ensure Hazard Mitigation and Redundancy for Critical Systems**:

  + Design all systems that protect against catastrophic hazards (such as the TPS) to include redundant or compensatory controls.
  + If recovery is impossible in-flight (e.g., TPS repair in orbit), assess alternate **abandon mission strategies**, such as crew escape pods or immediate return capabilities.
* **Establish Inflight Monitoring**:

  + Implement inflight diagnostics for critical systems, such as **real-time telemetry** to detect potential hazards (e.g., TPS damage, system degradation).

---

### **3. Apollo 13 (1970) — Failure-Tolerant Design Saved Crew**

#### **Description**:

When an oxygen tank exploded aboard the Apollo 13 spacecraft, the mission was saved due to the redundancy and failure tolerance designed into the life support systems, communications, and navigation. The crew survived because all mission-critical systems had failover mechanisms, and the Lunar Module acted as a lifeboat.

#### **Key Lessons**:

* **Multiple Layers of Redundancy Saved the Crew**:

  + Apollo 13’s systems featured dissimilar redundancies, such as the capacity of the Lunar Module to serve as an alternate life support system.
  + System degradation was controlled in a **predictable manner**, allowing the crew time to adapt and recover functionality.
* **Recovery and Adaptation Can Be Critical**:

  + Rigorous **training and contingency planning** enabled the crew and ground control to adapt to unforeseen situations effectively, demonstrating the importance of human-in-the-loop capabilities.
* **Lifesaving Guidance Adaptation**:

  + Include dissimilar redundancy in **life-critical systems** to ensure redundancy failures are independent of one another.
  + For software, implement predictable failure modes so systems degrade gracefully, maintaining functionality while providing sufficient time to recover.

---

### **4. Mars Climate Orbiter (1999) — Failure in Software Coordination**

#### **Description**:

The Mars Climate Orbiter was lost due to a software error stemming from mismatched metric and imperial units in data exchanges between the spacecraft control system and ground-based operations. The lack of redundancy to validate navigation commands caused the orbiter to enter an incorrect trajectory, ultimately resulting in its destruction.

#### **Key Lessons**:

* **Software Redundancy Is Just as Critical as Hardware Redundancy**:

  + Inadequate validation of software interactions led to a system-level failure. Failure tolerance in software systems must include error monitoring and validation to catch data inconsistencies.
* **Cross-System Integration Brings Risk**:

  + Complex interactions between systems (e.g., ground software, orbital software) introduce the risk of **common-mode software failures**, which must be mitigated through redundancy and robust system interfaces.

#### **Actionable Guidance**:

* **Implement Software Validation Mechanisms**:

  + Incorporate **end-to-end validation processes** for software, ensuring that data exchanged between systems is consistent, logical, and within tolerable error margins.
  + Use **independent, dissimilar software systems** for cross-verification of critical parameters (e.g., trajectory calculations).
* **Emphasize Standards in Software Development**:

  + Establish standardized units, protocols, and processes for development, testing, and integration to prevent similar software incompatibility issues.

---

### **5. James Webb Space Telescope (2021) — Fault Management Success**

#### **Description**:

The James Webb Space Telescope (JWST) exemplifies failure-tolerant design. Given the telescope’s inability to be serviced post-launch, its design adopted a **multi-layered fault tolerance approach**, which relied on predictive fault isolation, self-diagnostics, and redundant systems.

#### **Key Lessons**:

* **Autonomous Failure Management is Key for Remote Operations**:

  + With no possibility for physical maintenance, redundant control and monitoring systems were essential to resolving potential onboard failures autonomously.
  + Fault detection, isolation, and recovery (FDIR) strategies helped protect the telescope from catastrophic effects of thermal or software failures.
* **Testing Redundancy and Fault Isolation Was Critical to Success**:

  + Extensive testing under realistic mission scenarios ensured redundancy systems activated as expected under failure conditions, minimizing risks of design oversights.

#### **Actionable Guidance**:

* **Incorporate FDIR into System Design**:
  + Build fault detection and containment into both hardware and software architectures. For example:
    - Enable software to detect failed subsystems and isolate them from critical operations.
    - Ensure backup hardware systems engage automatically when failures are identified.
* **Validate Redundancy Through Testing**:
  + Use environmental simulations, heat maps, and failure tests to confirm redundancy activation under real-world conditions.

---

### **6. Lessons from Non-NASA Missions**

#### Highlight: European Space Agency’s **Ariane 5 Maiden Flight Failure (1996)**

* The loss of the Ariane 5 rocket was caused by a **software error** in the inertial navigation system, which lacked adequate failure tolerance for handling out-of-range acceleration values.
* **Lesson**: Implement runtime checks to prevent software outputs from cascading after encountering a fault. Include dissimilar software redundancy when failures cannot be “resilient.”

---

### **General Best Practices Learned Across NASA Missions**

* **Human-In-The-Loop Redundancy**:
  + Manual override systems remain vital as a backup to automated systems in time-critical scenarios. Ensure operators (e.g., crew) can intervene effectively if safety-critical automation fails.
* **Test Like You Fly**:
  + Perform extensive testing for redundancy strategies under realistic mission conditions. Ground scenarios must include simulated failure cases to validate system behavior.
* **Configuration Management**:
  + Strict configuration control of software and hardware is essential to ensuring all redundant components align with the intended system state. Divergences in configurations can propagate failures within a redundant setup.
* **Consistent Reviews and Audits**:
  + Independent reviews throughout development help ensure safety-critical hazards are identified and mitigated before they are baked into the design.

---

### **Final Thought: Making Failure Tolerance a Core Design Principle**

Failure tolerance is not only about redundancy—it is about **understanding vulnerabilities, integrating smart mitigations, and designing for recovery**. Lessons learned from both failures and successes demonstrate that proactive analysis and robust design processes are key to protecting lives, ensuring mission success, and advancing NASA’s legacy of innovation in space exploration.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-31 - Single Failure Tolerance**

4.3.1 The space system shall provide at least single failure tolerance to catastrophic events, with specific levels of failure tolerance and implementation (similar or dissimilar redundancy) derived via an integration of the design and safety analysis (required by NPR 8705.2).

Software assurance for this requirement focuses on integrating software safety, redundancy, and fault recovery into system designs to address single failure tolerance for catastrophic hazards. Key practices include ensuring traceability of hazard controls to software, incorporating dissimilar redundancy to prevent common-mode failures, validating failover mechanisms, and tracking progress via meaningful metrics. By following this guidance, projects can build robust, failure-tolerant systems that fulfill the requirement's intent and mitigate catastrophic risks effectively.

See also Topic [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics)

## 7.1 Tasking for Software Assurance

1. Confirm implementation of redundancy in the software design to achieve the required levels of failure tolerance.
2. Confirm that the hazard reports or safety data packages contain all known software contributions or events where software, either by its action, inaction, or incorrect action, leads to a hazard.
3. Assess that the hazard reports identify the software components associated with the system hazards per the criteria defined in NASA-STD-8739.8, Appendix A.
4. Ensure that redundancy management is robust and supports fault tolerance requirements.

## 7.2 Software Assurance Products

The software assurance guidance is focused on ensuring software assurance and failure tolerance are integrated consistently across the software life cycle, emphasizing practical implementation, effective communication, and robust verification methodologies. The aim is to reduce common-mode failures, streamline analyses, and ensure clear traceability for all safety-critical components.

### 7.2.1 Software Failure Tolerance Analysis

* Use advanced safety techniques like **Fault Tree Analysis (FTA)** and **Failure Modes and Effects Analysis (FMEA)** to model software-related risks associated with catastrophic hazards.
* Ensure the software design explicitly accounts for **failure modes**, including:
  + **Erroneous behavior** (outputs causing catastrophic outcomes).
  + **Silent failure** (software ceasing operation during critical scenarios).
* Incorporate analyses that ensure **common cause failures** (e.g., simultaneous failures of redundant software due to shared vulnerabilities) are mitigated effectively.

### 7.2.2 Software Design Documentation

* Strongly emphasize software designs that show:
  + How the **system and software architecture achieve failure tolerance**.
  + Redundancy mechanisms (similar and dissimilar) for **software and automation functions** supporting critical operations.
  + Fault isolation and graceful degradation strategies.
* Include dependency mappings where **critical software functions are associated with hardware failure tolerance mechanisms** (e.g., backups, cross-strapping).

### 7.2.3 Hazard Analysis Integration

* Ensure **completed hazard analyses and hazard reports**:
  + Identify every software-driven hazard that could lead to catastrophic events.
  + Showcase mitigation strategies like fault recovery, fallback to redundant systems, and human-in-the-loop overrides.
* Integrate specific **software safety analyses** (Example: fault propagation analysis) into hazard reports for clarity and traceability.

### 7.2.4 Metrics for Safety and Development Progress

Implement measurable, actionable metrics to assess software assurance success:

* **Traceability Metrics**: Percent of hazards and associated failure tolerance requirements traced to software requirements, designs, and test cases.
* **Testing Completion Metrics**: Ratio of hazards tested to total hazards, especially for safety-critical components.
* **Non-Conformance Metrics**:
  + Number of unresolved non-conformances tied to safety-critical software defects and controls.
  + Number of non-conformances directly impacting hazard controls during test procedures.
* **Coverage Metrics**:
  + Code/test coverage percentages for all **safety-critical components**.
  + Path coverage across failure scenarios (e.g., % of paths exercised for real-time monitoring functions).

### 7.2.5 Failure Tolerance Analysis

* Conduct **failure tolerance analysis** early in the development cycle to identify and prioritize catastrophic hazards related to software:
  + Analyze the range of scenarios where software failure could trigger catastrophic events.
  + For software-driven systems, evaluate both **functional degradation** and the possibility of silent errors affecting redundant systems.
* Apply **common-cause analysis**:
  + Identify shared vulnerabilities between redundant components, such as software dependencies on hardware subsystems or single points of failure in communication protocols.
  + Mitigate issues where redundant designs fail simultaneously due to dependency conflicts (e.g., power interruptions, shared memory).

### 7.2.6 Addressing Redundancy

* **Dissimilar Redundancy**:

  + Implement **redundant capabilities** using different approaches and technologies for safety-critical functions to avoid common-mode failures. Examples:
    - Diverse algorithms for navigation (e.g., inertial vs. GPS-based).
    - Hybrid manual and automated controls for mission-critical systems.
  + Ensure independent validation paths for dissimilar redundancy components.
* **Predictable Degradation**:

  + Design software to reduce risk by **gracefully degrading critical functions** rather than failing entirely.
  + Example: Downgrade navigation precision in case of sensor failure, preserving coarse-level trajectory control until recovery.

### 7.2.7 Software Hazard Analysis

* Perform detailed **Software Safety and Hazard Analyses**:
  + Use **hazard-specific software fault analyses** (e.g., task overrun, buffer overflow, divide-by-zero errors) to guide risk reduction measures.
  + Ensure hazard reports document controls for all software behaviors impacting safety-critical system hazards.
* Use clear traceability between hazard reports and software requirements/design artifacts, ensuring streamlined updates during revisions.

### 7.2.8 Verification and Validation (V&V)

* Conduct **Independent Verification and Validation (IV&V)** activities:
  + Verify software elements meet redundancy and fault tolerance requirements.
  + Validate software recovery mechanisms under simulated catastrophic hazard conditions (e.g., silent failures, incorrect outputs).
* Include **failure injection testing** to simulate worst-case scenarios:
  + Inject faults and monitor recovery actions for all safety-critical software components.
  + Test software failover protocols under time-critical constraints.

### 7.2.9 Real-Time Monitoring Design

* Ensure software includes:
  + **Real-time fault detection and annunciation** systems to warn operators before catastrophic hazards occur.
  + Dashboards for monitoring performance metrics and actionable telemetry values from onboard systems.

### 7.2.10 Safety-Critical Requirement Testing

* Focus on testing all **must-work and must-not-work functions** for safety-critical systems.
* Ensure safety-critical software requirements include:
  + Redundancy management and proper interactions with failover mechanisms.
  + Notification systems for failure detection and alerts.
* Include testing scenarios that require operator involvement to recover function after failures.

### 7.2.11 Configuration Management and Continuous Monitoring

* Prevent misconfiguration errors:
  + Maintain strict version control for redundant software components during updates or bug fixes.
  + Ensure synchronization of redundant elements across hardware/software interfaces (e.g., sensor-error propagation between components).
* Monitor for post-deployment anomalies:
  + Use telemetry to track conflicts across redundant software systems (e.g., mismatches between outputs of dissimilar algorithms).

### 7.2.12 Continuous Improvement

* Deploy a feedback loop for lessons learned from testing, simulations, and flight systems:
  + Post-mission results should update hazard reports, redundancy designs, and metrics.
  + Implement changes based on monitoring outcomes to improve future performance.

## 7.3 Example Software Assurance Metrics

NASA's lessons learned and standards (e.g., NASA-STD-8739.8 and NPR 8705.2) emphasize a robust, integrated approach to software assurance and failure tolerance for catastrophic hazards. By leveraging these updated strategies and metrics, projects can better achieve compliance with the requirement, refine redundant systems, monitor risks in real time, and continuously improve safety-critical software functionality.

Use the below metrics to assess compliance with the failure tolerance requirement:

**7.3.1 Design and Development Metrics**:

1. Percent traceability achieved for hazardous software requirements, designs, tests, and mitigations.
2. Number of safety-critical tests executed vs. total planned tests for failover mechanisms.
3. Ratio of verified redundancy logic to total redundancy elements incorporated.

**7.3.2 Testing Metrics**:

4. Code coverage percentages for safety-critical systems (e.g., % of critical paths tested).

5. Time-to-recovery metrics for catastrophic software failure scenarios (measured simulated recovery speed vs. required time-to-criticality).

6. Number of software safeguards successfully protecting against simulated common-mode failures.

**7.3.3 Operational Metrics**:

7. Real-time monitoring effectiveness:

* + Alerts triggered vs. total fault conditions detected.
  + Duration of monitoring delays in detecting faults.

8. Ratio of crew/operator manual recoveries performed during simulated software failures vs. automated recoveries.

## 7.4 Software Assurance Guidance

Redundancy alone does not meet the intent of this requirement. When a critical system fails because of improper or unexpected performance due to unanticipated conditions, similar redundancy can be ineffective at preventing the complete loss of the system. Dissimilar redundancy can be very effective provided there is sufficient separation among the redundant legs. For example, dissimilar redundancy where a crew member uses or portion of the same software that is behaving erroneously to override automated with manual control may not survive the failure since the approaches share a common failure point.  Areas in the system architecture should be analyzed for this commonality.   It is also highly desirable that the spaceflight system performance degrades predictably to allow sufficient time for failure detection and, when possible, system recovery even when experiencing multiple failures.

Software assurance (SA) plays a critical role in ensuring that space systems achieve the required **single failure tolerance for catastrophic events**. The goal is to develop and implement fault-tolerant software that can mitigate catastrophic hazards arising from software-induced errors or failures. The guidance below outlines key processes, tools, and techniques to integrate software assurance effectively across all phases of the software life cycle for this requirement.

### 7.4.1 Purpose of Software Assurance for This Requirement

The overarching purpose of software assurance is to:

1. Provide **confidence** that software will behave as intended under all operational conditions, including in the presence of failures.
2. Mitigate risks of **catastrophic hazards arising from software errors**, including both erroneous outputs and silent failures.
3. **Validate the implementation** of redundancy and failure recovery mechanisms.
4. Ensure **traceability and accountability** for hazard mitigation within software systems.

### 7.4.2 Key Areas of Software Assurance

#### 1. System-Level Integration

**Objective**: Ensure software assurance activities align with hardware, system, and safety analyses to achieve an integrated and holistic fault-tolerant system.

* Collaborate with system and hardware assurance teams on **fault tree analysis (FTA)** and **failure modes and effects analysis (FMEA)**:
  + Map software contributions to catastrophic hazards.
  + Ensure failure pathways are identified and mitigated with redundancy (e.g., failover mechanisms or manual overrides).
* Verify that the **software's redundancy design (similar or dissimilar)** aligns with and supports system-level failure tolerance strategies.

#### 2. Software Requirements Assurance

**Objective**: Confirm that safety-critical requirements fully address single failure tolerance and redundancy needs.

* **Safety-Critical Software Requirements**:
  + Identify and classify **safety-critical requirements and functions** using NASA-STD-8739.8 and SWE-205.
  + Ensure requirements address:
    - **Must-Work Functions**: Software critical to hazard control or mitigation.
    - **Must-Not-Work Functions**: Software that must be inhibited under specific conditions to prevent hazards.
  + Include redundancy requirements for critical functions (similar and dissimilar redundancy strategies).
* **Traceability**:
  + Establish full traceability from **catastrophic hazard scenarios** to software requirements.
  + Develop traceability matrices for software requirements ↔ design ↔ implementation ↔ testing.

**Outputs**:

* Software safety-related requirements traceability.
* Evidence of system hazard mitigation linkage.

#### 3. Software Design Assurance

**Objective**: Validate that the software design supports redundancy and failure tolerance.

* **Redundancy Mechanisms**:
  + Ensure all safety-critical software components incorporate appropriate **redundancy mechanisms** (e.g., voting logic, watchdog timers, error correction protocols).
  + Include dissimilar redundancy where possible to prevent **common-mode failures** (e.g., alternative algorithms or hardware for performing critical functions).
* **Predictable Degradation**:
  + Confirm the design incorporates strategies for **graceful system degradation** when failures occur, allowing recovery or fallback operations to occur within the system’s time-to-criticality.
  + Example: Limit software shutdowns to non-critical subsystems during failures.
* **Design Analysis Techniques**:
  + Use **interface analysis** to ensure modules have clear failure boundaries and can recover from faults independently.
  + Perform **common cause analysis** to check for dependencies that may introduce simultaneous failures in redundant software paths.

**Outputs**:

* Software design artifacts (including redundancy and fault handling logic) reviewed and approved.
* Evidence of software fault tolerance plans (e.g., error detection and recovery mechanisms).

#### 4. Hazard Analysis and Safety Analysis

**Objective**: Assess the role of software in system hazards and validate that software contributes to hazard mitigation.

* Complete **software safety assessments**:
  + Map software functions to known hazards in hazard analysis.
  + Include unique software-induced risks that could lead to catastrophic outcomes (e.g., software timing errors, overloads, or invalid input handling).
* Perform **Failure Modes and Effects Analysis (FMEA)** for software:
  + Identify failure modes within the software.
  + Evaluate their impact on redundancy mechanisms and associated hazards.
  + Example: Assess whether variable overflows or task overruns can propagate and defeat fault tolerance.
* Update and maintain **hazard reports**:
  + Document all software-related hazards, fault-tolerant mitigation strategies, and test results.
  + Include recovery paths for specific failure scenarios based on hazard severity.

**Outputs**:

* Completed hazard reports demonstrating software’s contribution to meeting failure tolerance requirements.

#### 5. Verification and Validation Assurance

**Objective**: Verify and validate software redundancy mechanisms and compliance with failure tolerance requirements.

* **Functional Testing**:
  + Verify that failover and redundant system recovery operate as intended during simulated failures.
  + Test failover scenarios to validate **time-to-criticality** constraints for catastrophic hazards.
* **Fault Injection Testing**:
  + Validate fault detection, isolation, and recovery (FDIR) mechanisms by injecting simulated software faults, such as:
    - Corrupted state variables.
    - Task overruns and race conditions.
    - Out-of-range input values and sensor malfunctions.
* **Common-Mode Failure Simulations**:
  + Test dissimilar redundancy strategies to confirm:
    - No shared vulnerabilities between redundant software functions.
    - No cascading failures across redundant or backup systems.
* **Independent Verification and Validation (IV&V)**:
  + Conduct IV&V activities specifically targeting hazard scenarios and software safety configurations, ensuring correctness in high-risk areas.

**Outputs**:

* Test reports confirming redundancy mechanisms and recovery processes.
* Evidence of fault detection and isolation capabilities (including effectiveness under time-critical scenarios).

#### 6. Metrics and Continuous Monitoring

**Objective**: Track progress in meeting failure tolerance and identify areas for continuous improvement.

**Key Metrics**:

* **Traceability**:
  + % of hazards traced to software requirements, design, and test cases.
* **Testing Completion**:
  + Number of hazards mitigated/tested vs. total identified hazards.
  + Test coverage for safety-critical components (e.g., % of paths exercised).
* **Failure Identification**:
  + Number of safety-critical non-conformances identified during testing.
  + Ratio of resolved vs. unresolved safety-related defects.
* **Redundancy Validation**:
  + Number of redundant failure tolerance scenarios validated via fault injections.

**Continuous Monitoring**:

* Post-deployment, monitor mission telemetry for actual or potential software faults.
* Establish a **feedback loop** to improve fault tolerance designs based on failures encountered during testing or flight operations.

#### 7. Configuration Management Assurance

**Objective**: Ensure redundancy mechanisms are not compromised by errors in configuration or integration.

* Maintain strict version control for all redundant software configurations.
* Ensure uniformity and completeness in deployed configurations for **redundant components**.
* Regularly audit configuration baselines to prevent silent misconfigurations that could undermine fault tolerance.

### **References**

Follow established standards to guide software assurance practices:

1. **NASA-STD-8739.8** [278](#_tabs-<p></p>) **, Software Assurance and Software Safety**
2. **NASA-STD-8719.13** [276](#_tabs-<p></p>) **, Software Safety Standard**
3. **NPR 7150.2 [083](#_tabs-<p></p>) , NASA Software Engineering Requirements**
4. **NASA-STD-8719.13, Appendix A, Hazard Analysis Techniques**

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software)        * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

# 8. Objective Evidence

To demonstrate compliance with the requirement, **objective evidence** is required to show that the software and system meet the required levels of single failure tolerance for catastrophic events. This evidence must be documented, traceable, and verifiable throughout the software development life cycle.

The collection of objective evidence ensures that the software fully meets the **single failure tolerance requirement** to prevent catastrophic events. These artifacts collectively demonstrate that catastrophic scenarios have been thoroughly analyzed, mitigated, and tested, and that redundancy strategies have been integrated effectively into the software design. This documentation is critical for verifying compliance with **NASA-STD-8739.8**, **NPR 8705.2**, and other applicable standards.

Below is a comprehensive list of objective evidence, organized by software development stages and assurance activities, that can be presented to demonstrate compliance.

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

## 8.1 Requirement and Traceability Evidence

**Objective**: Verify that all catastrophic hazard-related controls and their associated failure tolerance requirements are accounted for in the software.

* **Software Requirements Traceability Matrix (RTM)**:
  + Demonstrates traceability of catastrophic hazard mitigations to software requirements, design elements, and test cases/procedures.
  + Includes mapping of **safety-critical software components** to system hazards identified in the hazard analysis.
* **Safety-Critical Software Requirements**:
  + Clearly defined **must-work** and **must-not-work** requirements linked to catastrophic hazard scenarios and failure tolerance mechanisms.
  + Includes redundancy requirements for single failure tolerance, both for similar and dissimilar redundancy.
* **Derived Requirements Justification**:
  + Evidence of software requirements derived from system safety analysis, hazard reports, or redundancy evaluations.
  + Approval records for derived requirements by safety and engineering technical authorities.

## 8.2 Hazard and Safety Analysis Evidence

**Objective**: Show that software contributions to system hazards are understood, controlled, and mitigated.

* **Hazard Analysis Reports (HARs)**:

  + Comprehensive system-level hazard analysis, including software’s contribution to catastrophic hazards and the specific software controls implemented.
  + Clear identification of hazards associated with software behaviors that lead to catastrophic risk (e.g., unintended activation, output failure, silent faults).
* **Software Fault Tree Analysis (FTA)**:

  + Diagrams and analysis results identifying software-related failure paths for safety-critical functions.
  + Evidence that fault recovery or redundant controls exist to eliminate or reduce the risk of catastrophic outcomes.
* **Software Failure Modes and Effects Analysis (FMEA)**:

  + Analysis reports showing potential failure modes in safety-critical software modules (e.g., task timing errors, infinite loops, computational overflows) and their impact on system hazards.
  + Mitigation strategies for each identified failure mode (e.g., exception handling, failover mechanisms).
* **Common Cause Analysis (CCA)**:

  + Documentation of shared vulnerabilities between redundant software or system components.
  + Mitigation plans for common mode failures, such as dissimilar redundancy designs or separation of failure domains.
* **Hazard Reports Containing Software**:

  + Hazard reports for catastrophic risks involving software, detailing:
    - Hazard description.
    - Software hazard controls.
    - Verification status.

## 8.3 Design and Implementation Evidence

**Objective**: Verify that the software design supports the required levels of failure tolerance.

* **Software Architecture Diagrams**:

  + System architecture showing redundancy strategies (similar and dissimilar) for failure tolerance.
  + Includes mappings of safety-critical software components and their interactions with redundant backups.
* **Software Fault Tolerance Design**:

  + Design artifacts showing integration of fault-tolerant features:
    - Recovery logic (e.g., automatic failover between redundant systems).
    - Watchdog timers for detecting silent failures.
    - Dissimilar redundancy designs (e.g., alternative algorithms or diverse implementations of the same critical function).
* **Predictable Degradation Design**:

  + Evidence of how the software supports controlled and predictable degradation during failure scenarios (e.g., reducing functionality while maintaining safety-critical operations).
* **Design Review Records**:

  + Records of peer reviews, safety reviews, and technical authority sign-offs demonstrating that the design meets failure tolerance standards.

## 8.4 Verification and Validation Evidence

**Objective**: Validate the implementation of software failure tolerance and test its effectiveness in mitigating catastrophic hazards.

Test Artifacts:

* **Test Plans**:
  + Detailed test plans defining how failure tolerance, redundancy, and failover mechanisms will be verified.
  + Includes test scenarios derived from hazard analysis (e.g., failover activation upon primary system failure).
* **Test Procedures**:
  + Step-by-step procedures for validating safety-critical software functions and failover mechanisms.
  + Includes fault injection and failure simulation steps (e.g., simulating hardware malfunctions or software timing errors).
* **Test Reports**:
  + Results from functional and fault-injection testing demonstrating:
    - Redundant components activate correctly when primary systems fail.
    - Mitigations effectively prevent catastrophic events.
    - Failover mechanisms operate within acceptable time-to-criticality limits.
* **Independent Verification and Validation (IV&V) Reports**:
  + IV&V artifacts confirming that:
    - Failure scenarios are correctly mitigated.
    - Dissimilar redundancy mechanisms do not share common vulnerabilities.
    - Safety-critical requirements are fully implemented and tested.

Fault Tolerance Validation:

* **Fault Injection Testing Evidence**:
  + Logs and reports from fault injection testing (e.g., simulating errors like stack overflow, task overrun).
  + Includes details of faults tested, redundancy activation, and system recovery actions.
* **Coverage Reports**:
  + Code coverage and test coverage reports for safety-critical components (e.g., % of decision points covered in critical functions).
  + Path testing coverage for redundancy logic across critical failure scenarios.

## 8.5 Configuration Management Evidence

**Objective**: Ensure consistency and reliability in software versions supporting redundant systems.

* **Configuration Baselines**:
  + Records of software configuration items for safety-critical systems, including redundant paths.
  + Version histories showing alignment between redundant components at each release.
* **Build and Release Logs**:
  + Documentation showing synchronized releases of redundant software modules and components.
* **Change Control Records**:
  + Logs of changes to redundant configurations with risk assessments conducted for all modifications.

## 8.6 Operational and Deployment Evidence

**Objective**: Demonstrate that failure tolerance is sustained throughout mission operations.

* **Flight Readiness Review (FRR) Findings**:
  + Review reports confirming software readiness for flight, particularly focusing on safety-critical failure tolerance.
  + Includes validation of redundancy mechanisms in operational environments.
* **Real-Time Monitoring Evidence**:
  + Records of implemented real-time failure monitoring systems (e.g., telemetry alerts for fault conditions).
  + Evidence of system alerts and automated initiations of recovery protocols during testing.
* **Post-Mission/Event Analysis Reports**:
  + Analysis of operational data from telemetry to confirm redundancy mechanisms operated as intended during anomalies.
  + Lessons learned reports identifying improvements for redundancy or fault tolerance.

## 8.7 Metrics and Continuous Improvement Evidence

**Objective**: Track and evaluate the effectiveness of redundancy and failure tolerance strategies.

* **Metric Reports**:
  + Evidence of tracked and met software assurance metrics (e.g., % hazards covered by tests, % of executed vs. planned safety-critical tests).
* **Non-Conformance Records**:
  + Records of non-conformances related to safety-critical systems, with resolutions for all deviations.
  + **Continuous Improvement Documentation**:
    - Updates to hazard reports, test procedures, and designs based on test results, anomalies, or lessons learned.
