# HR-51 - Crew Flight Control

> NASA Software Engineering Handbook (SWEHB Ver D), page id 167805155. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805155/HR-51+-+Crew+Flight+Control

HR-51 - Crew Flight Control

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/167805155/HR-51+-+Crew+Flight+Control#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=167805155)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=167805155&showCommentArea=true&showComments=true#addcomment)

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

4.5.1 The crewed space system shall provide the capability for the crew to manually control the flight path and attitude of their spacecraft, with the following exception: during the atmospheric portion of Earth ascent when structural and thermal margins have been determined to negate the benefits of manual control.

## 1.1 Notes

For phases of flight where there is no active control of the spacecraft, such as when under passive parachutes, then manual control cannot be provided and this requirement would not apply. For a space station, when there is no propulsion system available for reboost, then manual control of the flight path (orbital parameters) cannot be provided, and this requirement would not apply. During the atmospheric portion of Earth ascent (approximately the first 100,000 feet), where the trajectory and attitude are tightly constrained to maintain positive structural and thermal margins, the trajectory and attitude constraints are not typically available independent of guidance. In this case, if the only option is for the crew to follow guidance then nothing is gained by manual control over automated control.

Manual control cannot be safely or accurately performed without the situational awareness tools to provide status, feedback, and flight control direction. Safe operation requires both accuracy of crew inputs and piloting handling qualities to meet human rating requirements. Tools include, but are not limited to, telemetry, displays, video, instrumentation, and windows. Tools will be verified in a cockpit environment to ensure they are adequate to support manual control and operations.

## 1.2 History

Click here to view the history of this requirement: HR-51 History

HR-51 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.5.1 The crewed space system shall provide the capability for the crew to manually control the flight path and attitude of their spacecraft, with the following exception: during the atmospheric portion of Earth ascent when structural and thermal margins have been determined to negate the benefits of manual control. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

The capability of the crew to control the spacecraft's flight path is a fundamental element of crew survival. The most robust satisfaction of this requirement is provided by direct manual control of the vehicle flight path, through an independent flight control system (bypassing the affected vehicle guidance, navigation, and flight control system failures). A minimum implementation of manual control allows for the crew to bypass the automated guidance of the vehicle by interfacing directly with the flight control system to affect any possible flight path within the capability of the flight control system. Limiting the crew to choices presented by the automated guidance function is not a valid implementation of manual control.  There have been several historical incidents demonstrating the effectiveness of manual control over automation leading to crew survival.  For further reading, see "Software Error Incident Categorizations in Aerospace" [596](#tabs-5) and other citations listed under Resources.

This requirement serves to enhance **mission flexibility, safety, and redundancy** under nominal and off-nominal conditions while recognizing the constraints during Earth ascent. Manual control enables the crew to respond intelligently and independently to contingencies across all mission phases, except when structural and thermal dynamics mandate exclusive reliance on automated systems. This layered approach aligns with NASA’s safety standards, historical lessons learned, and the best practices of the global human spaceflight community. Key Rationale Points:

## 2.1 Safeguarding Mission Success and Crew Safety

* **Primary Safety Consideration:** Crewed missions involve complex and dynamic flight environments (e.g., orbit insertion, docking, and landing). The ability for crew members to manually control the flight path and attitude provides a critical layer of redundancy that complements automated systems.
  + Systems can fail due to unforeseen anomalies like sensor errors, software malfunctions, or communication disruptions.
  + Manual control serves as a "last line of defense" in scenarios where automated systems fail or produce unanticipated behavior, potentially avoiding mission failure or catastrophic outcomes.
* **Emergency Recovery:** In emergency situations, manual control capability allows the crew to take immediate corrective actions, especially in scenarios with degraded automation or navigation errors.

## 2.2 Addressing Off-Nominal Scenarios

* **Manual Overriding Capability:** Automated systems are designed to handle nominal and some off-nominal scenarios, but they cannot account for all possible anomalies. Examples include:
  + Collision avoidance in orbital phases.
  + Adjustments needed due to improperly aligned docking paths.
  + Safe reentry corrections in the event of inaccurate trajectory predictions.
* By enabling manual intervention, the spacecraft remains flexible and adaptable, giving the crew control in unpredictable scenarios.

## 2.3 Improving Operational Flexibility

* **Adaptability Across Mission Phases:** Certain mission scenarios, such as rendezvous and docking, demand precision that can be influenced by environmental factors (e.g., unmodeled spacecraft interactions or debris). Humans may be able to account for and respond to unique environmental conditions more effectively than automated systems in some cases.
* **Operational Decision-Making:** Human situational awareness allows the crew to use real-time judgment and decision-making that can override predefined automated behavior when appropriate.

## 2.4 Exception for Earth Ascent

* **Atmospheric Ascent Limitations:** During Earth ascent, the system experiences extreme structural and thermal stresses, which require precise pre-planned control to maximize structural integrity and thermal safety:
  + Manual interventions during ascent could introduce erratic or delayed flight path changes, compounding thermal or aerodynamic loads, and potentially causing structural damage, loss of stability, or mission failure.
  + Automated control systems are optimized for maintaining strict structural and aerodynamic limits under these ascent conditions.
* **Operational Redundancy Not Necessary:** Investigations and analyses of ascent dynamics have determined that sufficient redundancy in automated systems makes manual crew intervention unnecessary and counterproductive during this mission phase.

## 2.5 Crew Confidence in Spacecraft

* **Psychological Preparedness and Confidence:** Providing manual control capability serves as a backup and builds crew trust in the spacecraft systems. Crew members are more confident and capable when they know they can intervene to influence spacecraft behavior if needed.

## 2.6 Lessons Learned from Historical Spaceflights

NASA has accumulated decades of lessons from historical crewed space missions that have repeatedly underscored the importance of manual control as a contingency measure. Key examples include:

1. **Gemini Missions:** Manual control was vital in rendezvous and docking operations due to limited autopilot sophistication. Crew members could make real-time adjustments when automated systems fell short.
2. **Apollo 11 Lunar Landing:** Neil Armstrong famously overrode the automated landing program to steer the Lunar Module to a safe landing site when predicted landing zones were found to be unsuitable.
3. **Apollo 13 Accident:** Manual control during key reentry procedures allowed compensatory adjustments following the failure of multiple systems.
4. **STS (Space Shuttle) Operations:** During emergency return-to-launch-site (RTLS) scenarios, the ability to abort and manually pilot the spacecraft was essential for crew safety.
5. **Soyuz Missions (Historical Issues):** Several Soyuz missions have relied on manual control to correct descent trajectories when automated systems experienced malfunctions or guidance errors.

## 2.7 International and Commercial Standards Alignment

* Providing manual control for flight path and attitude reflects best practices in modern crewed spacecraft design. Both NASA and its international/commercial partners (e.g., ESA’s Orion, SpaceX’s Crew Dragon, Boeing Starliner) incorporate manual control for crew operational autonomy as a critical safety layer.

## 2.8 Compliance with Human Spaceflight Certification and Safety Standards

* **NASA-STD-3001 (Volume 2)** [498](#_tabs-<p></p>) **:** Human Factors Engineering standards dictate that human crews must be able to monitor and control system functions to ensure safety in all mission phases.
* **Fault Tolerance Requirements (NPR 8705.2)** [024](#_tabs-<p></p>) **:** Establish clear mandates that the system must be fault-tolerant and offer manual alternatives as part of failure recovery.

# 3. Guidance

This guidance provides an improved structure, actionable steps, and clarity to ensure compliance with this requirement. The focus is on ensuring robustness, safety, redundancy, system usability, and compliance with standards while balancing the exceptions introduced during mission-critical flight phases.

The capability for crew members to manually control their spacecraft is a fundamental aspect of mission resilience and safety. Automated systems, despite their reliability, cannot anticipate all off-nominal or emergency scenarios, and the crew must have the tools to intervene when necessary. This manual control acts as a critical safety layer, ensuring mission success and crew survival. The guidance below ensures that the software design both meets this requirement and appropriately addresses the flight conditions under which manual control is limited.

By implementing the outlined software engineering tasks, including thorough analysis, rigorous verification, and robust design principles, this requirement can be executed to provide a crewed spacecraft with safe, intuitive, and reliable manual control capabilities within mission constraints. The guidance ensures redundancy, situational awareness, fault tolerance, and proper exception handling, contributing to both mission success and crew safety.

## 3.1 Guidance: Principles of Manual Control in Software Systems

1. **Direct Versus Limited Control:**

   * The most robust implementation allows the crew to directly interact with the flight control system to influence the flight path/attitude, even bypassing automated software functions if these functions are erroneous.
   * Limiting manual control to pre-programmed options determined by automated systems is not a valid implementation; the crew must have access to unrestricted manual control where feasible.
2. **Dissimilar Software Fault Tolerances:**

   * The ability to bypass software automation provides a dissimilar fault-tolerant mechanism, thereby mitigating risks associated with software failures.
3. **Exception Handling for Manual Control:**

   * This requirement explicitly excludes phases of flight where manual control is not feasible or introduces risks beyond acceptable margins, such as:
     + Atmospheric ascent (first 100,000 feet): Manual control could exacerbate structural and thermal stresses.
     + Passive parachute phases: Control is either unnecessary or infeasible.
     + Non-propulsive stations (e.g., orbital space stations with no active propulsion systems).
4. **Human Factors Considerations:**

   * For situations where manual control is appropriate, software systems must provide intuitive tools and feedback mechanisms tailored to support situational awareness, accurate decision-making, and error resilience under high cognitive load.

## 3.2 Software Engineering Tasks for Compliance

To ensure compliance with this requirement, the following software engineering tasks are proposed:

### 3.2.1 Robust Manual Control Systems

* **Implementation:** Develop software that enables robust manual override of automated systems. This override must:
  + Function independently of the automated guidance system and actively bypass it in failure scenarios.
  + Provide the crew full control of flight path and attitude within flight system constraints.
* **Verification:** Ensure the manual control system functions in all operational scenarios except during the specified phase of atmospheric ascent.

### 3.2.2 Human-Machine Interface (HMI) Design

* **Design Objectives:**

  + Create user-friendly control interfaces that minimize cognitive overload.
  + Provide clear visual and sensory feedback (e.g., status indicators) to notify the crew when manual control is available and when it is not (such as during atmospheric ascent).
* **Standard Compliance:** Follow display and control guidelines outlined in NASA-STD-3001 (Volume 2, Rev D) and ensure the HMI is verified in cockpit simulations.
* **Tools and Displays:**  
  Telemetry, displays, video feeds, physical controls (joysticks, touchscreen redundancies), and other sensors must accurately convey spacecraft status and allow the crew to make informed decisions during manual control.

### 3.2.3 Safety Analyses for Manual Control

* **Safety Tasks:**
  + Perform **Software Hazard Analysis** to evaluate potential system hazards introduced by manual control (e.g., crew-induced errors).
  + Conduct:
    - **Software Fault Tree Analysis (FTA):** Identify root causes of failures in manual control pathways and mitigate them.
    - **Software Failure Modes and Effects Analysis (FMEA):** Identify software failure modes that could impact manual control, ensuring mitigation strategies are in place.
  + Verify that manual control maintains compliance with structural and thermal margins where applicable.

### 3.2.4 Automated Transition to Manual Control

* **Implementation:** Develop automated transition logic to safely hand off control to the crew when transitioning out of ascent conditions or other phases.
* **Hazard Mitigations:** Ensure seamless transitions to avoid introducing hazards (e.g., abrupt system state changes or control instabilities during the transition).

### 3.2.5 Redundancy and Fault Tolerance

* **Redundancy Design:** Implement redundant, fault-tolerant pathways for manual control software:
  + Redundancy in flight control systems (e.g., dual or triple-redundant manual control channels).
  + Independent failover mechanisms for backup systems.
* **Error Resilience:** Ensure the system retains manual functionality even if one or more subsystems fail.

### 3.2.6 Real-time Monitoring and Alerts

* **Systems Design:** Provide real-time monitoring and alerting systems that supply the crew with continuously updated information about spacecraft status and potential risks to manual control.
* **Alert Categories:**
  + Indicate when manual control becomes available or unavailable.
  + Warn against incongruent commands or inputs that may endanger spacecraft integrity.

### 3.2.7 Independent Verification and Validation (IV&V)

* **Verification Approaches:**
  + Ensure IV&V activities independently validate that manual control capabilities meet mission and safety-critical requirements.
  + Conduct IV&V evaluations of HMI, redundancy, and failover mechanisms to confirm compliance with fault tolerance and usability standards.
* **Testing Participation:**
  + Include IV&V in software testing, design reviews, and hazard analysis assessments.

### 3.2.8 Simulation and Testing

* **Simulation Tasks:**
  + Conduct flight operation simulations under nominal and off-nominal conditions to verify the robustness of manual control.
  + Simulate boundary scenarios, stress-testing flight control systems where manual transitions occur at the limits of system capability.
* **Integration with Training:**
  + Collaborate with flight crews to conduct functional and usability testing in realistic environments (e.g., mission simulations, hardware-in-the-loop (HIL) tests).
  + Collect feedback to refine manual control system design.

### 3.2.9 Code Coverage and Quality

* **Code Coverage:**
  + Use the **Modified Condition/Decision Coverage (MC/DC)** criterion to ensure 100% coverage of safety-critical paths for manual control functionality.
  + Include edge cases such as software errors or anomalies in manual control transition logic.
* **Static Code Analysis:** Ensure code quality and adherence to relevant safety and cybersecurity standards.

### 3.2.10 Error Handling and Recovery

* **Recovery Mechanisms:**
  + Implement robust error detection, correction, and handling mechanisms.
  + Include fail-safe procedures that allow recovery from control losses in manual and automated modes.

### 3.2.11 Documentation and Training

* **Deliverables:**
  + Provide a **User Manual** that includes error handling procedures, troubleshooting guides, and detailed instructions for manual control under various operational scenarios.
* **Training Programs:**
  + Train crew members using simulations and operational exercises to ensure readiness for manual control in off-nominal scenarios.

## 3.3 Key Considerations for Exception Phases

1. **Atmospheric Ascent (First 100,000 Feet):**
   * Do not design manual control for ascent conditions to avoid risking thermal or structural integrity. Ensure automated guidance fully supports ascent requirements.
2. **Non-Propulsive Phases:**
   * Clearly define the limits of this requirement for phases requiring no propulsion or attitude control.

## 3.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

## 3.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

For a small project, resource limitations (e.g., manpower, budget, schedule) necessitate a streamlined yet robust approach to developing, verifying, and validating the capability for manual control. This guidance provides a practical, step-by-step approach tailored to the challenges and constraints of small-scale development while still ensuring quality, safety, and mission reliability.

Even in small projects, the capability for manual control is mission-critical and must be implemented with robust fault-tolerance and usability in mind. Focus on balancing minimal design complexity with safety, functional integrity, and realistic testing to meet the requirement efficiently. This lean approach ensures the system meets key operational needs without overextending resources.

## 4.1. Scope the Requirement

Before diving into development, refine the scope to focus on the minimal viable implementation of manual control:

* **Functional Scope**:

  + Ensure the crew can directly control the spacecraft’s flight path and attitude in real-time (e.g., using a joystick or control interface).
  + Exclude manual control during **non-applicable phases**, such as the atmospheric portion of ascent and other passive phases (e.g., parachute deployment or station-keeping without propulsion).
  + Focus on nominal operations (e.g., orbit adjustments) and a subset of critical off-nominal scenarios (e.g., system recovery after loss of automation).
* **Deliverables**:

  + A simplified **Human-Machine Interface (HMI)** to meet safety and usability requirements.
  + Basic fault-tolerant design to revert to automated systems if manual control fails.
  + Test results verifying basic functionality under both nominal and edge-case scenarios.

## 4.2 Plan Manual Control Implementation

Develop a clear project plan with time-scaling and resource allocation specific to manual control.

### 4.2.1 Prioritization of Capabilities

1. **Critical Functions**:

   * Real-time manual adjustment of flight path and attitude.
   * Fault-tolerant transition from automated to manual control and back.
   * Alerts and notifications for the crew, including status of manual controls.
2. **Secondary Functions**:

   * Situational awareness tools (e.g., simplified telemetry display).
   * Limited real-time feedback (e.g., a graphical representation of spacecraft orientation).
3. **Deferrable Options (Future Scope)**:

   * Full redundancy across multiple manual control interfaces.
   * Advanced visual tools (e.g., live video feeds).
   * Extensive operational simulations or training systems.

### 4.2.2 Schedule for Small Milestones and Deliverables

* **Phase 1:** System design and HMI prototyping (Weeks 1–4).
* **Phase 2:** Software implementation of manual control logic (Weeks 5–9).
* **Phase 3:** Integration testing with hardware-in-the-loop (HIL) testing (Weeks 10–12).
* **Phase 4:** Final validation, safety checks, and readiness review (Weeks 13–15).

## 4.3 Simplified Software Engineering Approach

Focus on high-impact tasks with minimal overhead while maintaining safety and functional integrity.

### 4.3.1 Manual Control Software Development

* **Flight Control Logic**:

  + Implement a basic override system that allows the crew to bypass the automated flight control logic for real-time adjustments.
  + Directly interface with the spacecraft’s guidance, navigation, and control (GNC) software.
* **Human-Machine Interface (HMI)**:

  + Develop a simple, intuitive interface (e.g., joystick, touchscreen buttons) that maps directly to flight attitude and path adjustments.
  + Add visual indicators for:
    - Active manual control status.
    - Alerts when manual control is disabled (e.g., during atmospheric ascent).
  + Use NASA-STD-3001 guidelines to optimize design simplicity for space-rated systems.

### 4.3.2 Fault-Tolerant Design

* Implement a low-complexity backup mechanism:
  + If manual control fails, the system automatically reverts to automated systems.
  + Add redundant pathways (e.g., dual communication links or control paths) for key manual control commands.

## 4.4 Testing and Validation

Testing activities for a small project need to focus on verifying minimal compliance for safety-critical scenarios while maintaining a reasonable scope.

### 4.4.1 Test Scenarios

Design a minimal set of test scenarios to validate the manual control system:

1. **Nominal Operations**:

   * Verify that manual controls can adjust trajectory and attitude in stable flight conditions.
   * Measure response times to ensure real-time system performance.
2. **Off-Nominal Scenarios**:

   * Implement high-priority failures to verify system safety, such as:
     + Transition from automation to manual control when a hypothetical automation fault is detected.
     + Testing manual recovery during a diverging trajectory scenario.
3. **Boundary Conditions**:

   * Simulate transition points between phases where manual control is disabled and re-enabled (e.g., post-ascent).

### 4.4.2 Tools for Testing

For a small project, prioritize the use of automated tools and simple environments:

* **Simulated Hardware Environments**:
  + Use software-in-the-loop (SIL) and hardware-in-the-loop (HIL) test environments for initial verification.
* **Code Coverage**:
  + Ensure test coverage of 100% for safety-critical manual control paths using Modified Condition/Decision Coverage (MC/DC).
* **Simulation Tools**:
  + Leverage existing mission simulation platforms or simplified commercial-off-the-shelf (COTS) simulators to run test cases efficiently.

### 4.4.3 Validation Metrics

* Percentage of test case success for nominal and off-nominal scenarios.
* Response latency under manual control (e.g., acceptable threshold = ≤200 milliseconds).
* Transition accuracy (i.e., no uncommanded changes during automation-to-manual transitions).

## 4.5 Documentation and Training

Even for a small project, documentation and crew preparation are essential to success.

### 4.5.1 Minimal Documentation

* **System Design Document (SDD)**: Simplified documentation of flight control system architecture, focusing on manual control components.
* **User Guide**: Develop a lightweight guide explaining:
  + How the manual control system functions.
  + Scenarios where manual control is unavailable.
  + Emergency recovery procedures.

### 4.5.2 Crew Training

* Provide basic training simulations for demonstration and familiarization.
* Focus on:
  + Manual control practice scenarios.
  + Recognizing alerts for manual control transitions.

## 4.6 Configuration Management

* Utilize a lightweight configuration management (CM) process:
  + Track version changes for manual control software.
  + Include a simple change approval process for testing hotfixes or improvements.

## 4.7 Key Lessons Learned for Small Projects

From historical missions and small-scale efforts:

* **Apollo 11 Lunar Landing (Manual Override Success):** Even with limited development time, manual override allowed astronauts like Neil Armstrong to intervene and divert to a safe landing site manually when automated systems fell short.
* **Soyuz Manual Recovery (Critical Backup):** Soyuz missions demonstrated the importance of manual reentry controls as a fail-safe backup to automated systems in certain off-nominal scenarios.

## **4.8 Checklist for Small Project Guidance:**

| **Activity** | **Outcome Goal** |
| --- | --- |
| Manual Control Logic Implementation | Override automated system; allow real-time path and attitude control. |
| Simplified HMI Development | Usable, intuitive interface for error-free manual control. |
| Fault-Tolerant Design | Redundant backups; automatic transitions between manual and automated systems. |
| Nominal and Off-Nominal Tests | Validate all flight phases; simulate failure modes and boundary conditions. |
| Code Coverage | Achieve 100% MC/DC coverage for critical manual control paths. |
| Documentation | Limited but detailed user manuals; simple design and test deliverables. |
| Crew Simulation Training | Prepare crew to use manual control under nominal and emergency conditions. |

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
* (SWEREF-498)

  [NASA Space Flight Human-System Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-3001-vol-2 "Click to open in new window")

  NASA-STD\_3001, Volume 2: Human Factors, Habitability, and Environmental Health, Revision A, 2015.
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

NASA has a long history of crewed space missions, which provides valuable lessons learned illustrating the importance of manual control capabilities. These lessons emphasize the need for redundancy, robust Human-Machine Interfaces (HMI), human-in-the-loop designs, and contingency planning to ensure crew safety and mission success under unforeseen conditions. Below are key lessons learned extracted from NASA's historical programs, mishap investigations, and technical bulletins.

---

### **1. Apollo Program: Manual Control Reliance**

#### **Lesson Learned:**

Manual control is an essential safety mechanism for human spaceflight, especially during off-nominal scenarios where automated systems fail or encounter unanticipated conditions.

#### **Evidence:**

* **Apollo 11 Lunar Module (LM) Landing (1969):** During lunar descent, the onboard guidance computer provided landing site data that was unsuitable (it directed the Lunar Module toward a field of boulders). Astronaut Neil Armstrong manually piloted the LM to a safer landing site.  
  **Implication on Requirement:** Manual flight path and attitude control must function effectively as a backup in situations where automation cannot account for unexpected flight dynamics or environmental factors.

#### **Takeaway for 4.5.1:**

* Manual control should provide unrestricted and precise input capability independent of automated functions. The capability must be implemented with intuitive controls and situational awareness tools to empower the crew to respond effectively to dynamic and adverse conditions.

---

### **2. Gemini Program: Limitations of Early Automation**

#### **Lesson Learned:**

Underdeveloped or overly simplified automated systems often require manual intervention as a backup.

#### **Evidence:**

* **Gemini 8 Mission (1966):** After successfully docking with an Agena target vehicle, a stuck attitude control thruster caused the combined spacecraft to spin uncontrollably. Astronauts Neil Armstrong and Dave Scott manually undocked from the Agena and stabilized the Gemini spacecraft using its reentry control system.  
  **Implication on Requirement:** Automated systems, while capable, may behave unpredictably during anomalous operations. Having a fallback manual control system is critical to preserving vehicle and crew safety.

#### **Takeaway for 4.5.1:**

* Manual control mechanisms should be designed as a low-complexity option capable of handling unanticipated anomalies, including automation system failures. The transition between automation and manual control should be seamless to allow rapid recovery.

---

### **3. Apollo 13: Critical Backup for System Failures**

#### **Lesson Learned:**

Manual control systems must be flexible and accommodate unusual failure modes that are not anticipated during design.

#### **Evidence:**

* **Apollo 13 Lunar Flight (1970):** After an oxygen tank explosion disabled key systems onboard, the crew needed to use the Lunar Module as a "lifeboat." Astronauts manually controlled aspects of the spacecraft’s trajectory to execute a free-return trajectory to Earth and performed engine burns to fine-tune reentry.  
  **Implication on Requirement:** Manual control must support the ability to fine-tune flight paths in failures involving complete or partial system loss. Simplicity and clear operational command interfaces are vital.

#### **Takeaway for 4.5.1:**

* Implement manual control systems with interfaces and algorithms robust enough to handle contingency scenarios where the spacecraft’s primary automated systems are unavailable or unreliable.

---

### **4. STS-1 (Space Shuttle Columbia): Automation versus Crew Input**

#### **Lesson Learned:**

The transition between manual control and automated systems must minimize operational complexity to avoid hazardous outcomes.

#### **Evidence:**

* During the first Shuttle flight (1981), automation and manual override options were critical for ascent and entry operations. One important takeaway was the need for a feedback-rich environment in which the crew was made aware of flight control system status and priorities when manual interaction occurred.  
  **Implication on Requirement:** During transition phases (e.g., ascent or descent), manual controls should provide clear status indicators, and the interface must support fast decision-making. Astronauts require situational awareness and the ability to understand control inputs in both automated and manual states.

#### **Takeaway for 4.5.1:**

* Design manual control systems to offer clear feedback (telemetry, alerts, visual displays) and ensure that transitions between automation and manual control are seamless and intuitive.

---

### **5. Soyuz 1 Disaster: Overreliance on Automation**

#### **Lesson Learned:**

Crewed systems that do not adequately incorporate manual control may result in catastrophic failures during hardware or software anomalies.

#### **Evidence:**

* **Soyuz 1 Mission (1967):** Cosmonaut Vladimir Komarov experienced multiple systems failures, including automated attitude control issues. A lack of sufficient manual control options prevented recovery of the vehicle’s descent trajectory, leading to mission failure and loss of life.  
  **Implication on Requirement:** Overreliance on automation without providing manual control as a viable fallback significantly increases mission risk, especially during descent or reentry operations.

#### **Takeaway for 4.5.1:**

* Ensure crewed systems facilitate manual control for critical flight operations such as trajectory adjustments, descent, and reentry. Manual controls must remain responsive and functional, even in cases of significant system degradation.

---

### **6. NESC Technical Bulletin 23-06: Software Fault Tolerance**

#### **Lesson Learned:**

To mitigate risks associated with software failures, systems should provide dissimilar redundancy, such as manual control pathways that function independently of the primary software system.

#### **Evidence:**

* The bulletin highlights historical incidents in which software automation failures could have been avoided or mitigated by incorporating independent fallback systems, such as manual control.  
  **Implication on Requirement:** Manual control provides fault tolerance by functioning independently of automated software systems. This dissimilarity ensures that software faults do not propagate into catastrophic failure modes.

#### **Takeaway for 4.5.1:**

* Design manual control mechanisms to bypass automated systems entirely. This dissimilar redundancy ensures fault-tolerant operations and enhances system reliability during mission-critical phases.

---

### **7. SpaceX Crew Dragon (Demo-2): Importance of Autonomous and Manual Balance**

#### **Lesson Learned:**

Modern spacecraft must achieve a balance between automation and manual control to maximize crew safety while simplifying operational requirements.

#### **Evidence:**

* During the **SpaceX Demo-2 mission (2020)**, astronauts performed successful manual control tests of Crew Dragon’s touchscreen interface while the spacecraft was fully capable of automated flight. The crew noted that the system was intuitive and required minimal effort to operate manually, providing vital redundancy in a safe and controlled environment.  
  **Implication on Requirement:** Modern manual control systems should focus on user-friendliness and incorporate intuitive controls that augment crew decision-making, especially under off-nominal conditions.

#### **Takeaway for 4.5.1:**

* Use modern HMI designs to simplify manual control, ensuring that crew input is efficient and safe even when used as a contingency during automated operations.

---

### **8. Columbia Disaster (STS-107): Human Factors and Feedback**

#### **Lesson Learned:**

Insufficient situational awareness during critical phases like reentry can prevent the crew from fully utilizing available control options.

#### **Evidence:**

* The loss of Space Shuttle Columbia (2003) highlighted that situational awareness systems and real-time feedback could have supported better crew decision-making if implemented.  
  **Implication on Requirement:** Manual control systems must be integrated with real-time situational awareness tools to ensure the crew is fully informed about the spacecraft’s operational status.

#### **Takeaway for 4.5.1:**

* Comprehensive situational awareness tools must be incorporated into manual control systems to help astronauts understand system behavior and maintain control during critical phases of flight.

---

### **General Recommendations Based on Lessons Learned**

1. **Redundancy:** Include dissimilar fault-tolerant paths, enabling manual control to bypass the primary software in case of failure.
2. **HMI Optimization:** Use intuitive, human-centered designs for manual input and feedback tools.
3. **Seamless Transitions:** Minimize hazards during transitions between manual and automated system modes.
4. **Real-time Feedback:** Provide situational awareness via easily interpretable displays, telemetry, and alerts.
5. **Robust Testing:** Rigorously test manual systems under nominal, off-nominal, and edge-case scenarios.

---

These lessons learned emphasize that designing, verifying, and validating manual control systems must be integral to spacecraft development, ensuring crewed systems can address nominal and off-nominal situations while maximizing safety and mitigating mission risks.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-51 - Crew Flight Control**

4.5.1 The crewed space system shall provide the capability for the crew to manually control the flight path and attitude of their spacecraft, with the following exception: during the atmospheric portion of Earth ascent when structural and thermal margins have been determined to negate the benefits of manual control.

This improved Software Assurance guidance focuses on traceability, robustness, and risk mitigation in manually controlled flight systems. By emphasizing thorough analyses, rigorous testing, and clear metrics, this approach ensures that the crewed system meets its requirements with minimal risk, even under challenging operational conditions.

## 7.1 Tasking for Software Assurance

1. Ensure the development, implementation, and testing of robust control algorithms capable of managing critical functions with crew intervention for flight control. These algorithms must undergo thorough testing to guarantee their reliability and safety in all operational scenarios.
2. Ensure redundancy and fault tolerance are included in the design to ensure that critical functions can continue to operate autonomously or the crew can assume manual control of the flight path and attitude of the spacecraft, even in the presence of faults or failures. This includes implementing backup systems and failover mechanisms.
3. Ensure that Integrated real-time monitoring and diagnostic tools are used to continuously assess the health and status of critical systems and subsystems. These tools should detect anomalies and trigger autonomous responses to mitigate potential catastrophic events and alert the operators and crew of the situation for potential intervention.
4. Employ safety analysis techniques such as [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) and [8.05 - Software Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) to identify potential hazards and failure modes. This helps in designing controls and mitigations for the manual operation of critical functions.
5. Ensure extensive simulations and testing are conducted to verify that the crew can assume and manually control the flight path and attitude of their spacecraft, with the exception of the atmospheric portion of Earth ascent, and can handle all nominal and off-nominal scenarios. This includes testing for unexpected situations and boundary conditions.
6. Ensure strict configuration management to ensure that the correct software versions and configurations are used. This reduces the risk of errors due to incorrect or inconsistent configurations that could impact manual operations.
7. Ensure robust error handling and recovery mechanisms to address errors stemming from detected faults. This ensures that error handling is adequate and that the system can recover from errors without leading to hazardous or catastrophic events.
8. Perform safety reviews on all software changes and software defects.
9. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.
10. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically that the crew can assume manual control of the flight path and attitude of the spacecraft under various conditions, including nominal and off-nominal scenarios. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks). Ensure that the project has developed and executed test cases to test the software system’s recovery from faults during manual operations.
11. Analyze the software test procedures for the following:
    1. Coverage of the software requirements.
    2. Acceptance or pass/fail criteria,
    3. The inclusion of operational and off-nominal conditions, including boundary conditions,
    4. Requirements coverage and hazards per [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) and [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), respectively.
12. Perform test witnessing for safety-critical software to ensure that the crew can assume manual control of the flight path and attitude of the spacecraft under various conditions, including nominal and off-nominal scenarios.
13. Confirm that test results are sufficient verification artifacts for the hazard reports.
14. Ensure comprehensive training and documentation for operators is available.

## 7.2 Software Assurance Products

The following Software Assurance (SA) deliverables provide the foundation for ensuring that the spacecraft meets the manual control requirements under nominal and off-nominal scenarios. These products assess software design, performance, safety, and reliability, validating that the system functions as intended.

#### **Mandatory SA Deliverables**

1. **Software Assurance Status Reports (SA Reports):**
   * Summarize the status of SA activities, findings, compliance, and coverage of manual control requirements.
2. **Software Requirements Analysis (SWE-050):**
   * Confirm that requirements related to manual control capabilities and exceptions (e.g., atmospheric ascent) are clear, complete, testable, and traceable. Focus on safety-critical requirements.
3. **Software Design Analysis (SWE-051):**
   * Analyze the software design to verify its ability to support manual control under nominal and off-nominal conditions. Assess the architecture, fault tolerance, and redundancy mechanisms.
4. **Source Code Quality Analysis (SWE-056):**
   * Evaluate the manual control software's implementation for adherence to coding standards, maintainability, and robustness using static analysis tools.
5. **Testing Analysis (SWE-065):**
   * Perform a thorough analysis of test artifacts (plans, procedures, and results) to ensure safety-critical manual control paths are comprehensively tested, including fault scenarios and boundary conditions.
6. **Software Safety and Hazard Analysis (SWE-205, SWE-213):**
   * Ensure all software-related hazards for manual control are identified and mitigated, focusing on safety-critical paths. This analysis includes causal factors, areas affected by control system failures, and fault tolerance.
7. **Audit Reports (e.g., FCA & PCA):**
   * Perform Functional Configuration Audits (FCA) and Physical Configuration Audits (PCA) to confirm that design, code, and documentation align with the baseline configuration for manual control systems.
8. **Software Test Documentation (SWE-066):**
   * Evaluate deliverables such as Software Test Plans, Test Procedures, and Test Reports to ensure that manual control features are verified.
9. **Safety Artifact Traceability:**
   * Verify traceability of each hazard, requirement, and mitigation strategy to corresponding test cases and software components.
10. **Results of Automated Tools:**
    * Utilize static/dynamic analysis tools to track defect density, code coverage, cyclomatic complexity, and compliance with safety-critical software practices.

## 7.3 Metrics

The following SA metrics provide actionable insights into the effectiveness, safety, and reliability of software systems supporting manual control. Metrics are grouped by focus areas:

### 7.3.1 Verification & Validation Metrics

* **Test Coverage:**
  + Total % of manual control scenarios simulated and tested (including nominal operations, off-nominal scenarios, and fault conditions).
* **Defect Density:**
  + Number of defects discovered per thousand source lines of code (SLOC) during testing and reviews.
* **Requirements Traceability:**
  + % of traceability completed for:
    - Manual control requirements ➔ design ➔ implementation ➔ test scenarios.
* **Code Coverage:**
  + % of safety-critical software code paths executed during tests (target 100%, provided it is feasible).

### 7.3.2 Safety Metrics

* **Hazard Analysis Completion:**
  + % of hazards identified with completed test cases vs. total number of software hazards.
* **Safety-critical Tests Executed:**
  + Ratio of safety-critical test cases executed to those witnessed or validated by Software Assurance.
* **Safety-related Non-Conformances:**
  + Number of open, closed, and recurring safety-critical defects.

### 7.3.3 Quality Metrics

* **Code Complexity:**
  + Use cyclomatic complexity or similar metrics to monitor complexity thresholds for safety-critical modules.
* **Configuration Stability:**
  + % of software builds with verified configurations and traceable changes.

### 7.3.4 Performance Metrics

* **Response Time:**
  + Average system response time to manual control input in critical mission phases.
* **System Uptime:**
  + % availability of manual control systems in scenarios where automation is bypassed.

### 7.3.5 Configuration Management Metrics

* **Version Control Compliance:**
  + % of software changes compliant with version tracking requirements.
* **Change Impact Analysis:**
  + Number of safety-critical changes reviewed vs. total changes implemented.

### 7.3.6 Training and IV&V Metrics

* **Training Completion:**
  + % of personnel certified for manual control testing, development, and monitoring.
* **IV&V Outcomes:**
  + Number of findings during Independent Verification and Validation efforts, categorized by severity.

## 7.4 Software Assurance Guidance

The following tasks outline the SA activities necessary to ensure compliance with Requirement 4.5.1. These tasks ensure that the system's software is reliable, fault-tolerant, and capable of handling manual control responsibilities with minimal risk.

### 7.4.1 Manual Control Systems

* Verify the robustness and independence of manual control systems, ensuring they bypass faulty or unavailable automated systems.
* Confirm that these systems enable manual control under nominal, off-nominal, and failure scenarios while adhering to constraints during atmospheric ascent.

### 7.4.2 Software Safety and Hazard Analysis

* **Software-Specific Hazard Analysis:**
  + Evaluate software elements associated with critical hazards.
  + Conduct Fault Tree Analysis (FTA), Software Failure Modes and Effects Analysis (SFMEA), and causal analysis.
* **Mitigation Verification:**
  + Ensure that mitigation strategies align with NASA-STD-8739.8 and verify that all hazard-related requirements have corresponding test cases.

### 7.4.3 Human-Machine Interface (HMI)

* Verify that manual control displays provide situational awareness, such as:
  + Clear visual status indicators for manual/automated control.
  + Crew notifications during fast condition transitions.
* Ensure the HMI meets NASA-STD-3001, Volume 2, guidelines.

### 7.4.4 Automated Transitions

* Evaluate and test the system’s automated transition between ascent (automated control only) and normal mission phases (where manual control is possible). Ensure the transition does not induce instability or unsafe conditions.

### 7.4.5 Fault Tolerance and Independence

* Test fault injection scenarios where automation fails, ensuring manual control seamlessly assumes responsibility.
* Verify that manual control systems remain functional even under degraded system states.

### 7.4.6 Real-Time Feedback and Alerts

* Evaluate if telemetry systems provide live status updates and alerts to support timely crew decision-making.

### 7.4.7 Test Witnessing

* Witness functional tests that validate manual control performance criteria, including:
  + Fault initiation scenarios.
  + Response time measurements.
  + Transitions between manual and automated controls.

### 7.4.8 Configuration and Code Management

* Verify that all manual control configurations, builds, and updates are strictly managed to prevent mismatches.
* Ensure 100% code coverage for safety-critical manual control paths or conduct a risk assessment for uncovered areas.

### 7.4.9 IV&V Participation

* Confirm IV&V involvement in the review of:
  + Requirements traceability.
  + Test results under fault conditions.
  + Operational readiness and hazard reports.

### 7.4.10 Documentation and Training

* Verify that all documentation (user manuals, error handling guides, etc.) is thorough and understandable.
* Provide simulation-based training to certify personnel in using manual control systems under off-nominal conditions.

### 7.4.11 Continuous Risk Assessment

* Assess software safety risks during milestone reviews and flight readiness processes, updating previous findings based on new data.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence refers to documented and verifiable artifacts that demonstrate compliance with the requirement and ensure that the implementation is robust, safe, and mission-critical functionalities are met. Below is a detailed set of objective evidence that can be used to verify and validate compliance with this requirement.

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

Providing comprehensive and verified objective evidence ensures compliance with this requirement while addressing safety, reliability, and robustness. These artifacts not only verify the system's capability but also demonstrate best practices and lessons learned from NASA’s extensive history in crewed spaceflight.

## 8.1 Requirements Evidence

### 8.1.1 Requirements Traceability Matrix (RTM)

* Trace the manual control requirement to the following:
  + System-level requirements specifying manual control functionality.
  + Software requirements capturing manual control implementation, safety, and redundancy.
  + Design artifacts, test cases, and validation reports.
* Include the exception for atmospheric ascent in the RTM to ensure proper implementation during non-applicable conditions.

**Objective Evidence:** Completed and verified RTM with links to software requirements, design documents, and test cases.

## 8.2 System Design Evidence

### 8.2.1 System Architecture Documents

* Provide system design documentation describing how manual control is incorporated into the spacecraft architecture, including:
  + Manual control pathways (direct interface or bypass of automated systems).
  + Fault tolerance and redundancy mechanisms.
  + Interfaces with the Guidance, Navigation, and Control (GNC) system.
  + Exception handling during atmospheric ascent.

**Objective Evidence:** System design document (SDD) showing how the design accomplishes manual control capabilities and restricts manual input during ascent.

### 8.2.2 Design to Support Off-Nominal Scenarios

* Include design documentation showing scenarios where the crew:
  + Overrides automated systems during nominal operations.
  + Corrects unexpected off-nominal flight trajectories or attitude anomalies manually.
  + Operates in degraded modes where automated systems are partially or fully unavailable.

**Objective Evidence:** Documented use case diagrams, sequence diagrams, and design documents for nominal and off-nominal manual control scenarios.

## 8.3 Software Design and Implementation Evidence

### 8.3.1 Software Design Documents

* Provide design documents verifying that software is capable of implementing manual control, including:
  + Details on Human-Machine Interface (HMI) software and crew input methods (e.g., joystick, touchscreen).
  + Fault detection and automated/manual transition mechanisms.
  + Methods for disabling manual control during ascent to prevent structural/thermal risk.
  + Control responsiveness under nominal and degraded system configurations.

**Objective Evidence:** Software design specifications with detailed descriptions, flow diagrams, and state diagrams of manual control logic.

### 8.3.2 Source Code and Static/Dynamic Analysis

* Perform static and dynamic analyses to confirm that:
  + Safety-critical sections of code related to manual control are implemented correctly (review of cyclomatic complexity, adherence to coding standards, etc.).
  + Manual control logic adequately bypasses automated systems during anomalies.
  + Exception handling is robust for phases like atmospheric ascent.

**Objective Evidence:** Static analysis results, code inspection reports, adherence to software coding standards.

## 8.4 Test Evidence

### 8.4.1 Test Plans, Procedures, and Reports

* Document that each aspect of manual control, including edge cases, has been tested using the following:
  + **Functional Tests:** Validate all manual control-enabled functions, including direct intervention by the crew and error overrides.
  + **Boundary Tests:** Test transitions between automated and manual control at flight boundary conditions (e.g., exit from atmospheric ascent).
  + **Stress Tests:** Test manual control under degraded conditions, such as partial loss of GNC inputs or hardware failures.
  + **Exception Tests:** Validate that manual control is disabled during non-applicable phases (e.g., ascent).

**Objective Evidence:**

* **Test Plan:** Comprehensive test plan identifying manual control test cases for all nominal and off-nominal cases.
* **Test Procedures:** Step-by-step procedures for functional, boundary, stress, and exception tests.
* **Test Reports:** Results of tests showing successful execution and any anomalies addressed.
* **Metrics Reports:** Test coverage reports (e.g., % safety-critical requirements tested, code coverage for manual control paths).

### 8.4.2 Hardware-in-the-Loop and Simulation Results

* Provide results from simulations and hardware-in-the-loop (HIL) testing, including:
  + Nominal crew interaction trials.
  + Worst-case scenarios (e.g., automation failure or simulated debris collision during mid-mission).
  + Crew responsiveness to system feedback.

**Objective Evidence:** HIL test reports, automated simulation logs, and results of nominals/off-nominals.

## 8.5 Safety and Risk Mitigation Evidence

### 8.5.1 Software Hazard Analysis

* Perform hazard analysis of software behavior in manual control scenarios:
  + Identify hazards associated with enabling/disabling manual control.
  + Evaluate scenarios where manual control causes unsafe conditions (e.g., unstable trajectories).
  + Clarify crew error scenarios and mitigation strategies.

**Objective Evidence:** Hazard Reports, including:

* **Software Fault Tree Analysis (FTA):** Tracing hazardous conditions to software-level faults.
* **Software Failure Modes and Effects Analysis (SFMEA):** Analysis of software malfunctions in manual control conditions and mitigations.

### 8.5.2 Safety-related Testing

* Test safety-critical aspects of manual control, including:
  + Response times to manual inputs.
  + Fault injection tests verifying system resilience to dynamic failures during manual control.
  + Confirmation that disabling manual control (e.g., during ascent) prevents unintended inputs from jeopardizing safety.

**Objective Evidence:**

* Test result reports for fault-injection, risk mitigation tests, and confirmation of hazards under SWE-205 compliance.
* Metrics showing all hazards traced to safety-critical requirements, tests, and mitigations.

## 8.6 Independent Verification & Validation (IV&V) Evidence

* Conduct IV&V activities to confirm:
  + Complete traceability between manual control requirements, design, implementation, and test cases.
  + Independent tests validating safety and mission compliance (e.g., responsiveness, redundancy).

**Objective Evidence:**

* IV&V compliance reports.
* IV&V participation checklists for design reviews, test witnessing events, and risk management activities.

## 8.7 Configuration Management Evidence

* Verify proper CM for manual control software artifacts, including:
  + Version control logs tracking all changes related to manual control functionality.
  + Audit reports from Functional Configuration Audits (FCA) and Physical Configuration Audits (PCA) for manual control subsystems.
  + Evidence that safety-critical software elements are under strict configuration management.

**Objective Evidence:**

* Configuration management reports, test-attached version control evidence, and FCA/PCA findings.

## 8.8 Training and Documentation Evidence

* Confirm training and documentation for manual control functionality, including user manuals for the crew:
  + **Crew Training:** Evidence of crew readiness to operate manual control under both nominal and emergency conditions.
  + **User Manuals:** Manuals detailing how to operate manual control systems, troubleshooting steps, and safety considerations.

**Objective Evidence:**

* Training completion logs.
* User manuals for manual control systems with step-by-step instructions.

## 8.9 Metrics Evidence

* Collect and analyze comprehensive metrics throughout the software lifecycle, including:
  + Test coverage data.
  + Defect density trends for manual control paths.
  + Validation coverage for safety-critical requirements.

**Objective Evidence:** Metric reports on traceability, test coverage, defect density, safety compliance, hazard mitigations, and audit findings.

## 8.10 Lessons Learned Integration

* Document lessons learned from historical missions or development phases (e.g., Apollo, Gemini, and Soyuz programs).

**Objective Evidence:** A lessons-learned register showing how historical inputs influenced the design, implementation, and testing of manual control systems.
