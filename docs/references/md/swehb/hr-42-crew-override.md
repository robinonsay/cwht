# HR-42 - Crew Override

> NASA Software Engineering Handbook (SWEHB Ver D), page id 171508217. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508217/HR-42+-+Crew+Override

HR-42 - Crew Override

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/171508217/HR-42+-+Crew+Override#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=171508217)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=171508217&showCommentArea=true&showComments=true#addcomment)

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

4.4.2 The crewed space system shall provide the capability for the crew to manually override higher level software control and automation (such as automated abort initiation, configuration change, and mode change) when the transition to manual control of the system will not cause a catastrophic event.

## 1.1 Notes

NASA-STD-8719.29 , NASA Technical Requirements for Human-Rating, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: HR-42 History

HR-42 - First published in NASA-STD-8719.29. First used in Software Engineering Handbook Version D.

| SWEHB Rev | HR Rev | Requirement Statement |
| --- | --- | --- |
| D | Baseline | 4.4.2 The crewed space system shall provide the capability for the crew to manually override higher level software control and automation (such as automated abort initiation, configuration change, and mode change) when the transition to manual control of the system will not cause a catastrophic event. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

# 2. Rationale

This is a specific capability necessary for the crew to control the crewed space system. While this capability should be derived by the program per [HR-31 - Single Failure Tolerance](/spaces/SWEHBVD/pages/167805124/HR-31+-+Single+Failure+Tolerance) (paragraph 4.3.1 of NASA-STD-8719.29), the critical nature of software control and automation at the highest system level dictates specific mention in this standard. Therefore, the crew has the capability to control automated configuration changes and mode changes, including automated aborts, at the system level as long as the transition to manual control is feasible and will not cause a catastrophic event. The program and Technical Authorities will determine the appropriate implementation of this requirement - which is documented in the program’s Human Rating Certification Plan (HRCP) and evidenced by HRCP deliverables.

This requirement is rooted in a crucial principle of human spaceflight: maintaining the crew's authority to intervene in critical system operations when necessary to ensure mission success, safety, and adaptability to unforeseen circumstances. While automation and advanced software control significantly reduce operational complexity and human workload, they are not infallible. Ensuring manual override capabilities allows the crew to address scenarios where software automation may fail, behave unexpectedly, or act in a manner counter to mission objectives.

## 2.1 Automation Failure or Limitations

* Automated systems are designed to respond to pre-defined conditions and scenarios programmed into their software. However, unexpected or un-modeled conditions, such as sensor malfunctions, software errors, or hardware anomalies, can lead to improper automated actions (e.g., premature abort sequences, incorrect mode transitions, errant commands).
* A manual override allows the crew to take control in cases where automation performs inappropriately or fails to address the real-time situation.

**Example:** During Apollo 11's lunar landing, the onboard guidance computer became overloaded with data and issued alarms. This could have led to an automated abort. Instead, Neil Armstrong manually controlled the descent and successfully landed the spacecraft. This highlights the importance of retaining crew authority over higher-level automation.

## 2.2 Need for Human Adaptability

* Humans possess cognitive abilities such as situational awareness, adaptability, and judgment that exceed the capabilities of automated systems in novel or complex scenarios. In dynamic and high-risk environments, the crew may have superior understanding or intent than pre-programmed software logic.
* Manual overrides empower the crew to apply their judgment based on their observations, training, and real-time situational analysis.

**Example:** Apollo 13's oxygen tank explosion required the crew to bypass standard operating protocols and devise manual configurations to stabilize spacecraft life support and propulsion systems. Automation alone could not have handled such a novel situation.

## 2.3 Unpredictable External Influences

* Space environments involve variables such as radiation, micrometeoroids, and thermal extremes that can interfere with automated systems. Environmental conditions may lead to unexpected sensor readings or degraded automation performance.
* A manual override ensures that, even in extreme environments or when automation fails to sense external influences correctly, the crew can intervene to stabilize or maintain system control.

**Example:** The ISS experienced an ammonia leak in its thermal system. While automation detected the issue, the manual crew intervention was required to configure the system for isolation and external repairs.

## 2.4 Prevention of Unnecessary Aborts

* Automated abort systems are critical safety mechanisms; however, they carry the risk of initiating an abort unnecessarily due to faulty inputs, incorrect configurations, or failure to account for the full operational context.
* A manual override provides crew members with the opportunity to prevent unnecessary aborts, conserving mission objectives and avoiding high-risk abort maneuvers in cases where the automated sequence is inappropriate.

**Example:** The Space Shuttle program incorporated abort override functionality to ensure that the crew and flight director could suppress abort triggers caused by faulty sensor data (e.g., spurious readings from temperature or pressure sensors).

## 2.5 Alignment with Human-Rated Design Principles

* A human-rated system is designed to accommodate and prioritize human needs while leveraging human strengths. This requirement emphasizes that the system’s design must reinforce crew control as a failsafe to augment software operation.
* Providing manual override capabilities reflects a fundamental principle of human spaceflight: **humans can always take necessary steps to preserve their safety and mission objectives, regardless of automation readiness.**

**Relevant Standards:**

* NASA-STD-3001 Vol 2 (Human System Integration Standards) [498](#_tabs-<p></p>) .
* NPR 8705.2 (Human-Rating Requirements for Space Systems) [024](#_tabs-<p></p>) .

## 2.6 Risk Mitigation in Complex Scenarios

* Space missions encounter complex nominal and off-nominal scenarios. Software control logic is often simplified to cover well-understood scenarios, which may overlook the specific nuances of rare or complex situations. Manual overrides enable the crew to adapt to these complex or compounded situations.
* while manual control itself adds risk, its inclusion here is designed carefully to meet the core rule safe

# 3. Guidance

This requirement emphasizes the critical need for the crew to manually intervene and override automated systems when decisions or actions made by automation do not align with mission outcomes or safety objectives. This capability safeguards against failures or limitations of automated systems, ensuring continuous mission operability, enhanced fault tolerance, and crew safety. The implementation of this requirement must balance automation, manual control, system design robustness, and ease of use for the crew, while thoroughly analyzing and mitigating risks related to transitioning to manual override modes.

This enhanced software engineering guidance ensures that the crewed space system provides robust, intuitive, and reliable manual override capabilities that meet safety, usability, and mission success requirements. By implementing safety analyses, dissimilar redundancy, fault tolerance, comprehensive testing, and HMI design tailored for crew use, the system can empower the crew in all mission scenarios—ensuring they retain ultimate control when automation behaves incorrectly or is insufficient for a given task.

For further details on related guidelines, consult **NASA-STD-8739.8** [278](#_tabs-<p></p>) and Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements).

## 3.1 Key Considerations:

* **Human-in-the-Loop Design Philosophy:** The system design must consider the crew's cognitive and operational roles when overriding automation to ensure tasks are manageable and situational awareness is maintained.
* **Risk Management:** The transition to manual control should not introduce additional risks that could compromise mission success or safety. Proper safety analysis, simulation, and test coverage are required.
* **Redundancy in Fault Recovery:** Integration of manual override capabilities should serve as a key component of dissimilar redundancy, especially when automation software encounters faults or failures.

## 3.2 Software Engineering Guidance

### 3.2.1 Manual Override Capabilities and Mechanisms

* **Objective:** Design and implement robust manual override mechanisms that allow the crew to safely and effectively take control of higher-level software operations.
* **Implementation Recommendations:**
  + Provide the crew with the ability to manually:
    - Abort inappropriate automated operations (e.g., abort sequences activated due to false sensor readings).
    - Change system configurations or mission modes.
    - Override flight paths or system responses as appropriate to restore control.
  + Ensure direct and unambiguous response to crew commands initiating overrides.
  + Categorize the functions that require manual overrides (e.g., abort sequences, life support controls) and address them as software-critical paths.
  + Use robust state-locking mechanisms such that the system and automation cannot attempt to reclaim control of the system once an override is initiated unless explicitly commanded to do so by the crew.

### 3.2.2 Safety Analysis and Risk Mitigation

* **Objective:** Ensure that transitioning to manual control does not introduce hazardous consequences or result in catastrophic events.
* **Implementation Recommendations:**
  + Perform **Software Fault Tree Analysis (FTA)** and **Software Failure Modes and Effects Analysis (SFMEA)** to:
    - Identify potential failures or risks introduced by manual override mechanisms.
    - Ensure hazards related to software behavior are mitigated when manual control is activated.
  + Simulate and verify transitions from automated to manual control under all operational conditions, including nominal, off-nominal, and degraded scenarios, focusing on avoiding unintended outcomes (e.g., oscillations or mode conflicts).
  + Collaborate with system safety engineers to ensure hazard analyses are fully integrated into the software development lifecycle.

### 3.2.3 Human-Machine Interface (HMI) Design

* **Objective:** Develop an intuitive, user-centric HMI that enables the crew to efficiently enact manual overrides without excessive cognitive load.
* **Implementation Recommendations:**
  + Comply with **NASA-STD-3001 Vol 2** [498](#_tabs-<p></p>) for design standards related to human factors and display interaction.
  + Ensure the HMI reflects the following:
    - **Status Transparency:** Display the current state of both automated and manual operations.
    - **Clear Indications:** Visual and auditory cues for active automation modes and when overrides are engaged.
    - **Feedback Mechanisms:** Immediate feedback provided to the crew to confirm the system's manual control state and verify the effect of their input.
  + Avoid overloading the crew with excess information while still providing the insight necessary to make informed decisions for manual interventions.
  + Perform usability testing with representative crews in realistic mission scenarios to evaluate effectiveness and error rates during overrides.

### 3.2.4 Real-Time Monitoring, Alerts, and Decision Support

* **Objective:** Provide the crew with up-to-date information to support timely and informed decisions on override actions.
* **Implementation Recommendations:**
  + Implement real-time system performance monitoring and fault detection algorithms.
  + Develop an alert system to notify the crew of operational deviations or conditions requiring manual intervention.
  + Incorporate decision support tools in the HMI that suggest or recommend actions based on real-time telemetry or situational context but still allow the crew to exercise ultimate discretion.

### 3.2.5 Redundancy and Fault Tolerance

* **Objective:** Ensure system availability and robustness during and after the transition between automated and manual control.
* **Implementation Recommendations:**
  + Use manual override as a layer of dissimilar redundancy in fault-tolerant system design.
  + Include secondary backup systems, such as redundant pathways for critical override operations (e.g., direct hardware connections when software fails).
  + Validate that control handover mechanisms avoid failure modes such as race conditions or lockouts between manual and automated systems.

### 3.2.6 Rigorous Verification, Validation, and Testing

* **Objective:** Validate that the manual override mechanisms are safe, intuitive, and perform correctly under all conditions.
* **Implementation Recommendations:**
  + Ensure **IV&V (Independent Verification and Validation)** activities include:
    - Assessment of manual override design against safety and mission requirements.
    - Validation of end-to-end system behavior, tracing requirements and testing alignment for expected outcomes during manual engagement.
  + Perform exhaustive simulations, including nominal, off-nominal, and boundary condition scenarios:
    - Fault-triggered transitions to manual control.
    - Full crew-initiated overrides in simulated mission scenarios.
    - Scenarios where automation is bypassed for fault mitigation or mission-critical adjustments.
  + Apply **Modified Condition/Decision Coverage (MC/DC)** metrics to ensure 100% test coverage of safety-critical software related to manual overrides.
  + Validate error-handling mechanisms under simulated abnormal conditions.

### 3.2.7 Configuration Management

* **Objective:** Ensure software integrity and reduce risks related to improper configurations affecting manual override operations.
* **Implementation Recommendations:**
  + Maintain strict version control and audit trails for software builds containing override logic.
  + Validate software builds and configuration changes during pre-flight and test operations to prevent override inconsistencies.

### 3.2.8 Training and Crew Readiness

* **Objective:** Ensure the crew has the skills and knowledge to effectively utilize manual overrides.
* **Implementation Recommendations:**
  + Provide practical training on using manual override systems, focusing on emergency scenarios.
  + Include procedural steps for activating overrides and reverting back to automation (if needed).
  + Develop detailed **user manuals** describing typical and emergency use cases, along with operational best practices.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [HR-31 - Single Failure Tolerance](/spaces/SWEHBVD/pages/167805124/HR-31+-+Single+Failure+Tolerance)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

See Topic [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) for other Software Requirements related to Human Rated Software.

## 3.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |

# 4. Small Projects

For small projects, this requirement must be implemented in a feasible, efficient manner while maintaining safety, reliability, and mission success objectives. The key is to simplify processes, minimize resource usage, and prioritize the most critical aspects of manual override functionality within the constraints of the project's size and scope.

For small projects, requirement must be implemented in scope-limited yet robust ways to ensure the crew can manually override higher-level automation in critical situations without increasing risks. By prioritizing essential functionality, simplifying safety and testing efforts, and providing clear, practical documentation and crew training, small projects can meet the intent of this requirement within their constrained resources.

## 4.1 Simplified Approach for Small Projects

### 4.1.1 Requirement Prioritization

Focus only on the essential aspects of manual override functionality:

* Identify key automated systems that require manual override based on mission-criticality (e.g., life support systems, propulsion control, abort sequences).
* Limit the number of override scenarios to the most likely or potentially hazardous conditions.
* Collaborate with stakeholders to define “catastrophic event” thresholds and the scope of feasible manual control.

### 4.1.2 Streamlined System Design

Design and implement the manual override capability by using simplified processes:

* **Direct Control Pathways:** Implement manual override functionality through simple, direct hardware/software interfaces that bypass complex automated logic.
  + Example: A physical switch or button linked directly to critical functions.
* **Fail-Safe Design:** Ensure the system transitions to manual override in a stable state without introducing further risks.
* **Small-Scale HMI Design:** Develop minimalistic Human-Machine Interface (HMI) components that allow intuitive activation of manual override, making use of existing display or control systems.

**Example Solution:**  
For propulsion system control, the manual override could involve toggling between automation and crew control using a simple UI panel with “ENABLE MANUAL CONTROL” and “REVERT TO AUTOMATION” buttons.

### 4.1.3 Safety Assurance

Perform simplified analyses to verify safety:

* **Fault Tree Analysis (FTA):** Determine simple fault paths for transitioning from automation to manual control and identify catastrophic risks. See [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis).
* **Failure Modes and Effects Analysis (FMEA):** Ensure coverage for the few critical components linked to manual overrides; prioritize higher-risk elements. See [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis).

Focus on lightweight reviews and analyses that address the most pressing risks within the scope of the system functionality.

**Key Deliverables:**

* Hazard identification sheets.
* Basic safety checklist for manual override activation scenarios.

### 4.1.4 Testing and Validation

For small projects, testing should focus on essential software and system behaviors:

* Simulate minimal operational scenarios:
  + Nominal transition to manual control (e.g., for configuration changes).
  + Off-nominal conditions where overriding automation is necessary (e.g., sensor failure triggering unnecessary aborts).
* Conduct basic verification to check:
  + Manual commands override automated decisions.
  + No catastrophic effects arise during or after the manual transition.
* Use simple testing environments:
  + Software-in-the-loop (SIL) or hardware-in-the-loop (HIL) testing for core manual override functions.
  + Basic simulations of off-nominal scenarios (e.g., failure cascades).

### 4.1.5 Documentation and Configuration Management

Prioritize essential documentation and configuration control practices:

* **Requirement Traceability:** Ensure traceability aligns manual override functionality with specific high-level requirements. Keep traceability lightweight.
* **Configuration Tracking:** Document which software modules and functions include manual override capabilities. Use basic version control mechanisms (e.g., Git).
* **User Procedures:** Develop simple crew instructions that focus on:
  + When and how to activate a manual override.
  + Expected system behavior during a transition.
  + Emergency protocols for handling manual control scenarios.

### 4.1.6 Crew Training

For small projects, training programs should focus on specific functionality:

* Provide concise training materials focused solely on manual override activation, steps, and potential outcomes.
* Include tabletop simulations or low-fidelity exercises to ensure crew familiarity with override operations.

## 4.2 Sample Implementation Checklist for Small Projects:

#### **Design Phase**

* Identify critical systems requiring manual override.
* Create simple manual override logic that bypasses automation.
* Design basic HMI for override activation and feedback.

#### **Analysis Phase**

* Perform lightweight FTA and FMEA for override-related hazards.
* Verify that transitioning to manual control does not increase catastrophic risks.

#### **Testing Phase**

* Test override functions in nominal and off-nominal conditions.
* Verify fail-safe operation during transitions.

#### **Documentation**

* Ensure traceability from requirements to implementation and testing.
* Provide clear user instructions for crew training and operational use.
* Maintain basic configuration control for override-related software and interfaces.

#### **Training**

* Develop procedural training using minimal resources.
* Conduct basic tabletop simulations or low-fidelity training exercises.

## 4.3 Small Project Example

**Scenario:** Manual override for automated abort sequence.  
**System Design:**

* Manual "ABORT DISABLE" switch integrated into the flight control panel.
* HMI displays the status of the abort system (e.g., "ABORT ENABLED," "MANUAL ABORT DISABLED").

**Safety Analysis:**

* Ensure terminating the abort sequence does not result in catastrophic failure (e.g., ensure propulsion systems remain active and controllable).

**Testing:**

* Simulate a scenario where faulty sensor data triggers an abort.
* Validate that the "ABORT DISABLE" switch suppresses the abort sequence and transitions system control to manual mode without adverse outcomes.

**Training:**

* Provide crew with a 1-page procedural document outlining when, why, and how to use the manual "ABORT DISABLE" capability.

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

The importance of providing manual override capabilities in crewed space systems has been reinforced by lessons learned from historical NASA missions. These lessons highlight scenarios where manual control succeeded in mitigating risks, as well as cases where insufficient manual override functionality contributed to mission complications or near-misses.

---

### **1. Apollo Program (Apollo 11 Lunar Landing - 1969)**

**Lesson Learned:** Human-in-the-loop decision-making can prevent automated systems from making incorrect choices during critical situations.

**Context:** During the Apollo 11 lunar landing, the onboard guidance computer encountered overload issues caused by a flood of data from a radar system. It issued program alarms, which could have triggered an automated abort due to the perceived fault. Instead, the astronauts, particularly Neil Armstrong, manually controlled the Lunar Module’s descent and landed safely on the moon.

**Implications for Requirement 4.4.2:**

* Automated systems must provide clear status information to the crew, enabling them to assess the situation and decide when an override is required.
* Manual override capabilities must be tested under simulated conditions to ensure the crew can successfully intervene during high-pressure scenarios.
* The design must prioritize trust in human judgment, especially during unexpected situations.

**Relevant Documentation:** Apollo 11 report detailing computer issues during descent.

---

### **2. Apollo 13 (Oxygen Tank Explosion - 1970)**

**Lesson Learned:** The ability for the crew to adapt and override failed automated systems can mean the difference between mission failure and crew survival.

**Context:** Following an oxygen tank explosion, the Apollo 13 spacecraft underwent a cascade of system failures. Many automated systems were rendered ineffective due to unusual spacecraft conditions. The crew's manual reconfiguration of life-support systems, power management, and trajectory adjustments—guided by ground control—enabled the spacecraft’s safe return to Earth.

**Implications for Requirement 4.4.2:**

* Manual override systems must be flexible enough to allow the crew to deal with novel failures not originally anticipated in the design process.
* Override capabilities should not rely exclusively on the software; robust hardware interfaces, such as physical switches, should also be available for critical systems.
* Clear, concise procedures for switching between automation and manual control are critical to mitigate risks in high-stress situations.

**Relevant Documentation:** Apollo 13 accident investigation and debrief.

---

### **3. Space Shuttle Program (Abort Scenarios and Sensor Failures)**

**Lesson Learned:** Dependence on automation without manual override provisions can lead to unnecessary aborts or system disruptions caused by faulty sensor inputs.

**Context:** The Space Shuttle program featured automated abort capabilities during ascent, but it also allowed manual intervention to prevent faulty sensor data from triggering unnecessary aborts. On multiple occasions, sensor issues falsely indicated serious anomalies (e.g., engine temperature or pressure anomalies) that might have triggered an automated abort. In such cases, manual overrides by either the crew or ground controllers averted unnecessary aborts and ensured mission success.

**Implications for Requirement 4.4.2:**

* Automated abort systems must be designed with clear pathways for crew-in-the-loop intervention.
* Sensor validation techniques should complement manual override functionality to reduce reliance on potentially incorrect automated decisions.
* Redundant displays and alarms are critical for providing situational awareness to the crew, enabling rapid and accurate manual decisions.

**Relevant Documentation:** Shuttle ascent anomaly analysis reports.

---

### **4. Mars Climate Orbiter (Metric Conversion Error - 1999)**

**Lesson Learned:** Lack of manual intervention capabilities can lead to irretrievable consequences, especially when automation depends on incorrect parameters.

**Context:** The Mars Climate Orbiter was lost due to a navigation error caused by a failure to convert units (imperial to metric). The automation followed incorrect navigation commands derived from software that produced improper thrust data. No manual override capability was available to correct course in response to this error.

**Implications for Requirement 4.4.2:**

* Automation should be implemented with oversight mechanisms that allow human operators—onboard or on the ground—to assess and override erroneous operations.
* Real-time data displays and manual adjustment controls for mission-critical parameters (e.g., trajectory and navigation) should always be part of human-rated systems.
* Human operators must have enough visibility into system behavior to identify software anomalies and make corrective actions.

**Relevant Documentation:** Mars Climate Orbiter Mishap Investigation Board Report.

---

### **5. Boeing CST-100 Starliner OFT (Unintended Automation Event - 2019)**

**Lesson Learned:** Software and automation anomalies can produce unsafe mission configurations if manual overrides are not properly integrated and tested.

**Context:** During Boeing’s CST-100 Starliner Orbital Flight Test (OFT), a timing error in the spacecraft’s mission event sequencing software caused the spacecraft to execute incorrect propulsion burns. As a result, the spacecraft was placed into an incorrect orbit, preventing it from reaching the International Space Station (ISS). A lack of situational awareness and insufficient manual override provisions further complicated the situation.

**Implications for Requirement 4.4.2:**

* Manual override capabilities should be part of a broader fault-management strategy that includes situational awareness systems to assist the crew in identifying the need for intervention.
* Mission-critical software systems must undergo rigorous pre-flight testing for anomalies, with provisions for real-time manual adjustments to mitigate software failures.
* Ensure end-to-end integration testing for both automated and manual control systems, specifically for event sequences affecting mission-critical operations.

**Relevant Documentation:** NASA/Boeing Joint Investigation of OFT anomalies.

---

### **6. ISS Ammonia Leak Detection (2015)**

**Lesson Learned:** Automation and manual control must complement each other to respond effectively during off-nominal situations.

**Context:** On the ISS, telemetry suggested a possible ammonia leak in a cooling system. Automated systems alerted the crew and initiated pre-programmed responses to contain the potential hazard. The crew investigated the leak and manually activated control systems to reconfigure the thermal system while awaiting confirmation of the leak.

**Implications for Requirement 4.4.2:**

* Automated monitoring and response systems should provide clear indications of off-nominal conditions to the crew, accompanied by manual controls to take further actions if needed.
* A balance between automation and manual control is essential in fault management, especially in space station environments where continuous operational control is needed.
* Override design should leverage local crew control (manual overrides) in combination with ground control support to improve fault management efficiency.

**Relevant Documentation:** ISS anomaly resolution reports.

---

### **Key Takeaways from Lessons Learned:**

1. **Situational Awareness is Critical:** Crew must be provided with sufficient information about the automated system's operations and any anomalies to make informed override decisions.
2. **Human Judgment is Invaluable:** Automation cannot account for all scenarios; the ability for humans to intervene remains a vital component of mission safety.
3. **Redundancy in Manual Overrides:** Ensure hardware pathways (e.g., physical toggles or switches) are available for overriding critical automated systems when software fails.
4. **Seamless Transitions:** Design systems such that the transition between automation and manual control is smooth, predictable, and free of uncertainties.
5. **Rigorous Testing:** Both automation and manual override systems must be tested extensively in simulated and boundary-condition scenarios to account for potential failures and off-nominal situations.
6. **Usability and Training:** Manual overrides must be intuitive and thoroughly practiced by the crew to instill confidence and ensure effectiveness in high-stakes situations.
7. **Configuration Awareness:** Flight-critical software and automation changes must be validated with consideration for their interaction with manual override systems.

---

### **Conclusion:**

NASA’s lessons from previous missions emphasize that manual override capabilities are indispensable for the success and safety of crewed missions. Automation has brought efficiency and reliability to spaceflight, but it is not infallible—human involvement remains the ultimate safeguard. By integrating these lessons learned into system design and implementation, projects can meet Requirement 4.4.2 and ensure robust manual override mechanisms that protect both missions and human life.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**HR-42 - Crew Override**

4.4.2 The crewed space system shall provide the capability for the crew to manually override higher level software control and automation (such as automated abort initiation, configuration change, and mode change) when the transition to manual control of the system will not cause a catastrophic event.

This enhanced guidance ensures that manual override capabilities are rigorously assured through verified requirements traceability, robust testing, hazard evaluations, and adherence to software assurance standards. Independent reviews, adequate metrics, and comprehensive safety analyses protect mission objectives while providing the crew with reliable control during emergencies. For additional details, refer to **NASA-STD-8739.8: Software Assurance and Software Safety Standard** [278](#_tabs-<p></p>) and **NPR 7150.2: NASA Software Engineering Requirements**[083](#_tabs-<p></p>).

## 7.1 Tasking for Software Assurance

1. Ensure the development, implementation, and testing of robust control algorithms capable of managing critical functions with crew overrides. These algorithms must undergo thorough testing to guarantee their reliability and safety in all operational scenarios.
2. Ensure redundancy and fault tolerance are included in the design to ensure that critical functions can continue to operate autonomously or the crew can perform overrides, even in the presence of faults or failures. This includes implementing backup systems and failover mechanisms.
3. Ensure that Integrated real-time monitoring and diagnostic tools are used to continuously assess the health and status of critical systems and subsystems. These tools should detect anomalies and trigger autonomous responses to mitigate potential catastrophic events.
4. Employ safety analysis techniques such as [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) and [8.05 - Software Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) to identify potential hazards and failure modes. This helps in designing controls and mitigations to allow the crew to manually override higher level software controls and automations to prevent the system from causing a catastrophic event.
5. Ensure extensive simulations and testing are conducted to verify that the manual override of systems can handle all nominal and off-nominal scenarios without causing catastrophic events. This includes testing for unexpected situations and boundary conditions.
6. Confirm that strict configuration management to ensure that the correct software versions and configurations are used. This reduces the risk of errors due to incorrect or inconsistent configurations that could impact crew operations.
7. Ensure robust error handling and recovery mechanisms to address errors stemming from detected faults or failures. This ensures that error handling is adequate and that the crew can manually override the system to prevent it from executing autonomous functions that could lead to hazardous or catastrophic events.
8. Perform safety reviews on all software changes and software defects.
9. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.
10. Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically that the crew is able to manually override the system under various conditions, including nominal and off-nominal scenarios, without causing catastrophic events. (See [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) tasks). Ensure that the project has developed and executed test cases to test the software system’s recovery from faults and failures.
11. Analyze the software test procedures for the following:
    1. Coverage of the software requirements.
    2. Acceptance or pass/fail criteria,
    3. The inclusion of operational and off-nominal conditions, including boundary conditions,
    4. Requirements coverage and hazards per [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) and [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), respectively.
12. Perform test witnessing for safety-critical software to ensure that the crew can manually override systems under various conditions, including nominal and off-nominal scenarios.
13. Confirm that test results are sufficient verification artifacts for the hazard reports.
14. Ensure comprehensive training and documentation for operators is available.

## 7.2 Software Assurance Products

This software assurance guidance integrates lessons learned, NASA standards, and best practices to ensure that manual override capabilities are implemented safely, thoroughly tested, and sufficiently documented, while aligning software assurance with mission and program goals.

### 7.2.1 Core Deliverables

1. **Software Assurance Status Reports**: Regular reporting on the progress of assurance activities for manual override functionality, including verification and validation tasks, test results, and defect resolutions.
2. **Software Requirements Analysis**:
   * Analyze requirements specific to manual override functionality for completeness, clarity, and traceability to mission objectives.
   * Ensure requirements for override conditions, transitions, and safety-critical states are clearly defined and validated against system hazard analyses.
3. **Software Design Analysis**:
   * Verify that manual override design aligns with safety requirements and allows seamless transitions between automated and manual control modes.
   * Confirm redundancy and fault tolerance are incorporated into design elements for manual overrides.
4. **Source Code Quality Analysis**:
   * Leverage automated tools to assess coding standards compliance for safety-critical code.
   * Identify potential vulnerabilities in code written to support manual override functions (e.g., race conditions, deadlocks).
   * Evaluate complexity metrics (e.g., cyclomatic complexity) to ensure maintainability.
5. **Testing Analysis**:
   * Confirm that manual override functionalities have been thoroughly tested under nominal and off-nominal scenarios, including boundary conditions and system failures.
   * Include test results and recommendations for improving test coverage or addressing defects.
6. **Software Safety and Hazard Analysis**:
   * Complete hazard analyses related to manual override functionality.
   * Ensure fault detection mechanisms and mitigation strategies are implemented to avoid catastrophic outcomes from override actions.
7. **Audit Reports**:
   * Include assessments from Functional Configuration Audit (FCA) and Physical Configuration Audit (PCA) to verify that manual override capabilities are fully implemented and conform to documentation and requirements.
8. **Manual Override Test Witnessing Signatures**:
   * Document witnessed execution of system validation tests to verify that manual override functionalities meet mission safety requirements. Ensure compliance with **SWE-066** for testing processes.

### 7.2.2 Additional Verification Artifacts

* System design demonstrating how the crew can manually override automated systems under nominal and off-nominal conditions.
* Completed hazard reports identifying potential hazards caused by override actions, with mitigation strategies and implementation instructions.
* Results from automated tools (e.g., code coverage, static analysis).
* Traceability matrices confirming links between requirements, design, implementation, and test artifacts.

## 7.3 Metrics for Software Assurance

### 7.3.1 Verification and Validation Metrics

1. **Test Coverage**:
   * Percentage of safety-critical software code tested for manual override functions.
   * Number of test cases executed for nominal and off-nominal scenarios involving overrides.
2. **Defect Density**:
   * Number of override-related defects per thousand lines of code detected during testing phases.
   * Monitor defect trends for severity and frequency related to manual control code sections.
3. **Requirements Traceability**:
   * Percentage of traceability completed for override-related requirements linking them to design, code, and test procedures.

### 7.3.2 Safety Metrics

1. **Hazard Analysis Completion**:
   * Number of hazards identified and mitigated that involve manual override transitions.
2. **Safety-critical Requirements Compliance**:
   * Percentage of safety-critical requirements verified via testing for manual override conditions.

### 7.3.3 Quality Metrics

1. **Code Quality**:
   * Cyclomatic complexity scores for manual override software modules.
   * Static analysis results (e.g., memory leaks, error-prone constructs).
2. **Code Churn**:
   * Number of code revisions for manual override functionality to identify stability or problem areas.

### 7.3.4 Performance Metrics

1. **Response Time**:
   * Time required for the system to react to crew manual override commands under emergency conditions.
2. **System Uptime**:
   * Percentage of operational availability for manual override functions during critical scenarios.

### 7.3.5 Configuration Management Metrics

1. **Version Control**:
   * Number of changes recorded for manual override-related software modules with corresponding impact assessments.
2. **Change Requests**:
   * Number of override-related defects or changes logged, including resolution time and effect on system performance.

### 7.3.6 Training Metrics

1. **Training Completion**:
   * Percentage of crew members and flight hardware/software teams completing manual override system training.
2. **Manual Proficiency**:
   * Effectiveness scores from training simulations for manual override scenarios involving time-critical decisions.

### 7.3.7 Independent Verification and Validation (IV&V) Metrics

1. **IV&V Coverage**:
   * Percentage of manual override functionality subjected to IV&V analysis.
2. **IV&V Results**:
   * Number of findings and recommendations related to manual override implementation during IV&V activities.

Examples of potential metrics for tracking progress include:

* % of safety-critical tests executed vs. witnessed by software assurance teams.
* % of traceability between safety-related hazards and test cases linked to manual override capabilities
* defects related to override features identified and resolved.
* Safety-critical code coverage (% of tested paths vs. total identifiable paths).

## 7.4 Software Assurance Guidance

### 7.4.1 Key Assurance Tasks

1. **Manual Override Mechanisms**:
   * Ensure that manual override functions are implemented with a fail-safe design. These mechanisms must support safe transitions, even under degraded system conditions.
2. **Human-Machine Interface (HMI)**:
   * Verify the HMI meets usability and safety standards, providing key information such as system status, activation feedback, and override safety checks in real-time.
3. **Real-time Monitoring and Alerts**:
   * Confirm that system alerts for conditions requiring manual intervention are clearly visible and actionable by the crew. Provide situational context for decision-making.
4. **Redundancy and Fault Tolerance**:
   * Validate that backup systems can seamlessly continue operation during a manual override and compensate for software failure.
5. **Software Safety and Hazard Analysis**:
   * Review hazard reports to assess manual override-related risks and confirm that mitigation strategies are implemented, tested, and operational.
   * Complete Software Fault Tree Analysis (FTA) and Failure Modes and Effects Analysis (FMEA) for all software override paths.
6. **Safety Reviews**:
   * Conduct periodic reviews of manual override impacts on system safety throughout the software lifecycle. Present findings during Safety Reviews for further refinement.
7. **Test Witnessing**:
   * Participate in witnessing all safety-critical tests relevant to manual override functionality. Use test witnessing opportunities to uncover defects, validate behavior, and confirm compliance.
8. **Simulation and Testing**:
   * Ensure simulations cover both nominal and extreme off-nominal scenarios. Verify robustness and reliability of manual override systems.

### 7.4.2 Configuration Management Guidance

* Enforce strict configuration management for software versions, manual override logic, and hazard reports.
* Assess modifications to software items to ensure that override functions remain consistent and fully traceable.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [HR-31 - Single Failure Tolerance](/spaces/SWEHBVD/pages/167805124/HR-31+-+Single+Failure+Tolerance)        * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [7.24 - Human Rated Software Requirements](/spaces/SWEHBVD/pages/167805194/7.24+-+Human+Rated+Software+Requirements) * [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) * [8.59 - Audit Reports](/spaces/SWEHBVD/pages/102695745/8.59+-+Audit+Reports) |

# 8. Objective Evidence

Objective evidence refers to tangible, verifiable artifacts, data, and documentation that demonstrate compliance with the requirement. Below is a categorized list of objective evidence for this requirement, ensuring the system meets the requirement through requirements analysis, design verification, testing, and system validation.

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

The objective evidence outlined above covers every aspect of this requirement —from requirements analysis, design, safety assurance, testing, and training to configuration management and IV&V. Each piece of evidence verifies that manual override functionality is comprehensively implemented, rigorously tested, and fully aligned with crew safety and mission objectives. This provides confidence that the crew can reliably take control of the system without causing catastrophic events.

## 8.1 Requirements and Systems Engineering Evidence

* **Requirements Documentation**:
  + Approved requirements document defining all manual override functionality, including specific use cases such as abort initiation prevention, automated mode change overrides, and automated configuration transitions.
  + Traceability matrix linking manual override requirements to higher-level mission, system, and safety requirements.
* **Use Case Scenarios**:
  + Defined scenarios for manual override usage, including nominal and off-nominal situations (e.g., false abort triggers, faulty sensor data, mode transition issues).
  + Documentation of potential hazards associated with manual overrides, including scenarios where transitions to manual control could create additional risks.
* **Functional Flow Diagrams**:
  + Detailed functional flow and system architecture diagrams showing the interactions and transitions between automated systems and manual override mechanisms.
  + State transition diagrams depicting system responses when a manual override is activated.

## 8.2 Design and Development Evidence

* **Software Design Documentation**:

  + Software design documents illustrating the integration of manual override pathways in the system logic and architecture, including control flow diagrams for switching between automated and manual modes.
  + Software design control measures for safety-critical functions, demonstrating fault detection and fail-safe states when manual overrides are engaged.
  + Documentation ensuring dissimilar redundancy strategies for override mechanisms (e.g., hardware and software redundancy).
* **Hardware Design Documentation**:

  + Evidence of physical hardware controls (e.g., toggles, switches, keypads) for initiating manual override, including Human-Machine Interface (HMI) designs.
  + Design review reports for manual override interfaces to ensure usability during high-stress/emergency conditions.
* **Requirements Traceability Matrix (RTM)**:

  + Evidence of traced linking from system-level manual override requirements to:
    - Software design decisions.
    - Test cases and validation criteria.

## 8.3 Software Assurance and Safety Evidence

* **Hazard Analysis and Reports**:

  + Completed Hazard Analyses identifying override-related hazards with mitigations.
  + Hazard Reports listing hazards, associated software components, hazard controls, and test verification results.
  + Evidence that transition to manual control under hazardous conditions has been analyzed to ensure it avoids catastrophic events.
* **Software Safety Analysis**:

  + Results of **Software Fault Tree Analysis (FTA)** identifying failure paths that may impact manual override functions. See topic [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) .
  + Completed **Software Failure Modes and Effects Analysis (SFMEA)** demonstrating assessment of potential software failure modes during manual override events. See topic [8.05 - SW Failure Modes and Effects Analysis](/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis).
* **Traceability of Safety-Critical Functions**:

  + Clear traceability showing how manual override capabilities are aligned to safety-critical requirements per **NASA-STD-8739.8 [278](#_tabs-<p></p>)** .

## 8.4 Testing and Validation Evidence

* **Manual Override Test Plan and Procedures**:

  + Test Plan that includes detailed test cases covering all manual override scenarios:
    - Nominal Scenario Testing: Verifying that manual overrides override automation as expected under normal conditions.
    - Off-Nominal Scenario Testing: Validating that overrides work during failure scenarios (e.g., simulated sensor malfunctions or software faults).
    - Timing and Performance Tests: Verifying the response time of the system when overrides are initiated.
    - Fail-Safe Switching Tests: Ensuring the system remains stable during transitions between manual and automated modes.
* **Test Results and Reports**:

  + Test reports showing that manual override functions were tested under all operational conditions, including both nominal and off-nominal scenarios.
  + Data validating that no catastrophic events occurred when transitioning to manual control during test scenarios.
  + Code Coverage Metrics with MC/DC (Modified Condition/Decision Coverage) results showing 100% coverage of safety-critical software components related to manual overrides.
* **Simulation Records**:

  + Results from simulations demonstrating that the crew can safely, effectively, and quickly activate manual overrides during high-stress situations.
  + Evidence comparing simulation outcomes with expected system behavior to ensure the system performs reliably.
* **Integrated System Testing Evidence**:

  + System-level test results verifying that all manual override functions are integrated and work seamlessly with other subsystems, such as propulsion, life support, or power systems.
  + Test records from witnessed system test events confirming the behavior of manual overrides (as required by [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)).

## 8.5 Configuration and Quality Management Evidence

* **Version Control and Configuration Management Records**:

  + Records verifying the specific versions of software and hardware used for implementing and testing manual override functions (per [SWE-187 - Control of Software Items](/spaces/SWEHBVD/pages/102695523/SWE-187+-+Control+of+Software+Items)).
  + Change request logs demonstrating tracking and impact assessments of changes affecting manual override capabilities.
* **Code Quality Analysis Reports**:

  + Results from static analysis tools showing adherence to coding standards related to safety-critical software.
  + Cyclomatic complexity reports for manual override software modules to ensure maintainability and low fault potential.
* **Defect Reports**:

  + Documentation of detected defects during manual override testing, including classification by severity and resolution status.
* **Independent Verification and Validation (IV&V) Reports**:

  + IV&V evidence confirming compliance of manual override functionality with all safety-critical requirements.
  + IV&V participation records in peer reviews, configuration audits, and hazard review boards.

## 8.6 Training and Operational Readiness Evidence

* **Training Materials and Records**:

  + Documentation of crew training sessions focused on manual override activation and related emergency procedures.
  + Simulated training records showing crew performance during manual override scenarios, including response times and success rates.
* **Crew Procedures and User Manuals**:

  + Crew procedural documentation detailing:
    - Manual override activation steps under different conditions.
    - Emergency protocols for transitioning to manual control during high-risk scenarios.
    - Troubleshooting and recovery steps for override functionality.
* **Operational Validation Evidence**:

  + Results from Crew-in-the-Loop simulations verifying the usability of manual override controls under expected mission conditions.
  + Feedback reports from crew training and mission rehearsals to identify gaps in override usability or effectiveness.

## 8.7 Examples of Objective Evidence

| **Type** | **Document/Artifact** |
| --- | --- |
| **Requirements Definition** | Approved requirement document, Use Case Scenarios, Requirements Traceability Matrix |
| **System & Software Design** | Functional block diagrams, HMI design drawings, Software Design Documentation |
| **Safety Analysis** | Hazard Reports, Software FTA and FMEA |
| **Testing Evidence** | Test Reports, Code Coverage Metrics, Test Observation Signatures (e.g., SWE-066 test witnessing) |
| **Configuration Management** | Version control logs, Change request records, Audit findings (FCA/PCA) |
| **IV&V Deliverables** | IV&V Reports, Simulation results, Peer review findings |
| **Crew Readiness** | Training documentation, User Manuals, Simulation/Training Results |
